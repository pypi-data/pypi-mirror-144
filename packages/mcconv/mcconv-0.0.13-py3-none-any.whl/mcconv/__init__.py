import argparse
import glob
import logging
import math
import sys

import pyHepMC3.pyHepMC3.HepMC3
import vector

from .detect import detect_mc_type
from .file_types import McFileTypes, parse_file_type
from .generic_reader import UnparsedTextEvent, GenericTextReader
from .hepmc_convert import hepmc_convert

_app_descr = """
Tool that allows to convert old (and new) EIC MCEG formats to HepMC3 and HepMC2. 

Example 1. Minimal:
  mcconv input.txt -o output.hepmc
  
Example 2. Convert Lund GEMC with 10x110 beam (must be set manually):
  mcconv input.txt -i lund_gemc -b 10x100

Example 3. Convert first 1000 events to HepMC2
  mcconv input.txt -p 1000 -f 2
 

Please read full documentation at:
  https://eicweb.phy.anl.gov/monte_carlo/mcconv
  
INPUT FORMAT NAMES
-------------------

=============   ============  ==================================
format          -i arg        alternative
=============   ============  ==================================
BeAGLE          beagle
HepMC2          hepmc2
HepMC3          hepmc3
Pythia EIC      pythia_eic    pythia_bnl
Pythia6/LUND    lund          pythia_lund, lund_pythia, lund_py6
Lund GEMC       lund_gemc     pythia_gemc
Lund MesonStr   lund_alt
EIC Smear       eic_smear
=============   ============  ==================================

BEAM PARAMETERS
---------------

Some formats have beam information, others don't provide it. 
HepMC requires at least 1 input particle for the event. 
So users have to provide beam particle information it is absent

Flag -b or --beam can be used for that in 2 forms:

1. Beam given in short form like 10x100 or 5x41
   In is case the assumed is e-p interaction with no crossing angle
   Example: 
      mcconv input.txt -i lund_gemc -b 10x100
   
2. Each particle info is given in form (px,py,pz,e,pdg)
   Example:
      mcconv input.txt -i lund_gemc -b "0,0,-10,-10,11" -b "0,0,100,100,2212"

The both above examples are equal. 

----------

"""

# the default ccdb logger
logger = logging.getLogger("mcconv")


def show_progress(event_index, evt):
    if event_index and event_index % 1000 == 0:
        logger.info(f"Events processed: {event_index:<10}")


def apply_crossing_angle(evt_index, hepmc_event, args):
    """
    The function applies boost+rotate of events
    """
    angle = args["cross_angle"]
    beam_ele = vector.obj(x=0, y=0, z=-1)
    beam_ion = vector.obj(x=0, y=0, z=1).rotateY(angle)
    boost_axis = beam_ion + beam_ele
    boost_axis *= 0.5

    boost_vector = pyHepMC3.pyHepMC3.HepMC3.FourVector(boost_axis.x, boost_axis.y, boost_axis.z, 0)
    result = hepmc_event.boost(boost_vector)
    if not result:
        raise ValueError(f"Can't boost event to {boost_vector}")

    # rotation half of the angle
    rotate_vector = pyHepMC3.pyHepMC3.HepMC3.FourVector(0, 0.5*angle, 0, 0)
    result = hepmc_event.rotate(rotate_vector)
    if not result:
        raise ValueError(f"Can't rotate event to {0.5*angle}")


def parse_short_beam_str(beam_str):
    """Parses a string like '10x100' and returns normal beam form like [(0,0,pz,e,11), (0,0,pz,e,2212)]"""
    tokens = beam_str.split('x')
    if len(tokens) != 2:
        err_msg = f"Short beam string is '{beam_str}' but should be AxB, dividing by 'x' gives: {tokens}"
        raise ValueError(err_msg)
    lep = float(tokens[0])
    ion = float(tokens[1])
    return [(0, 0, -lep, lep, 11), (0, 0, ion, ion, 2212)]


def process_beam_arguments(beams):
    # parse beam particles
    beam_particles = []

    if not beams:
        return None

    for beam_str in beams:
        # is it 10x100 form of the string?
        if "x" in beam_str:
            return parse_short_beam_str(beam_str)

        isinstance(beam_str, str)
        tokens = [token.strip() for token in beam_str.split(",")]
        if len(tokens) != 5:
            msg = f"--beam flag must be a string with 5 comma separated values: px,py,pz,e,pdg. You given: '{beam_str}'"
            raise ValueError(msg)

        px = float(tokens[0])
        py = float(tokens[1])
        pz = float(tokens[2])
        e = float(tokens[3])
        pdg = int(tokens[4])
        beam_particles.append((px, py, pz, e, pdg), )

    return beam_particles


def hepmc_convert_cli(argv):
    """Main entry point of mcconv executable"""

    parser = argparse.ArgumentParser(description=_app_descr, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('inputs', nargs='+', help="File name (wildcards allowed)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output. Info level")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debugging output. More than verbose")
    parser.add_argument("-i", "--in-type", default="", help="Input file type: [auto, pythia6-bnl]")
    parser.add_argument("-f", "--format", default="3", help="HepMC format [2,3]")
    parser.add_argument("-o", "--output", default="output.hepmc", help="File name of resulting hepmc")
    parser.add_argument("-s", "--nskip", default=0, type=int, help="Number of events to skip")
    parser.add_argument("-p", "--nprocess", default=0, type=int, help="Number of events to process")
    parser.add_argument("-b", "--beam", action='append', help="Beam parameters: Given in short form like 10x100"
                                                              "Or given in form of (px,py,pz,e,pdg)")

    args = parser.parse_args(argv)

    args.cross_angle = 0        # No crossing angle. Use afterburner

    # Configuring logger
    # create and set console handler
    stdout_handler = logging.StreamHandler()
    stdout_handler.stream = sys.stdout
    logger.addHandler(stdout_handler)

    # create stderr handler
    stderr_handler = logging.StreamHandler()
    stderr_handler.stream = sys.stderr
    stderr_handler.setLevel(logging.ERROR)
    logger.addHandler(stderr_handler)

    # Logger level from arguments
    if args.debug:
        logger.setLevel(logging.DEBUG)
    if args.verbose:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.WARNING)

    # What files to process
    file_paths = []
    for user_input in args.inputs:
        # use Glob to convert something like some_dir/* to file names
        file_paths.extend([file_path for file_path in glob.glob(user_input)])

    if not file_paths:
        msg = "None input files are found"
        raise ValueError(msg)

    if len(file_paths) > 1:
        logger.warning(f"(!)warning: more than one file found (n={len(file_paths)})."
                       f" Currently mcconv converts only 1 file at a time. Only the first file will be converted")

    # Process beam particles
    beam_particles = process_beam_arguments(args.beam)
    # Check if user provided beam particles there are 2 particles
    if beam_particles and len(beam_particles) != 2:
        logger.warning(f"(!)warning: provided n={len(beam_particles)} beam particles. "
                       f"Are you sure? (mcconv anticipates 2 beam particles or none)")

    # >oO DEBUG output
    logger.debug("Found files to process:")
    for file_path in file_paths:
        logger.debug(f"  {file_path}")

    input_file_type = parse_file_type(args.in_type)

    if math.isclose(args.cross_angle, 0):
        logger.debug("No crossing angle adjustment (no --cross-angle flag given or it is 0)")
        transform_func = None
        transform_args = None
    else:
        logger.debug(f"Apply crossing angle of '{args.cross_angle}'[mrad]")
        transform_func = apply_crossing_angle
        transform_args = {"cross_angle": args.cross_angle/1000}

    hepmc_convert(input_file=file_paths[0],  # TODO many files input
                  output_file=args.output,
                  input_type=input_file_type,
                  hepmc_vers=args.format,
                  progress_func=show_progress,
                  transform_func=transform_func,
                  transform_args=transform_args,
                  nskip=args.nskip,
                  nprocess=args.nprocess,
                  beam_particles=beam_particles)


if __name__ == '__main__':
    hepmc_convert_cli(sys.argv[1:])

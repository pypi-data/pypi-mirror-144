from .file_types import McFileTypes
import pathlib


def detect_mc_type(file_name: str) -> McFileTypes:
    """Tries to detect a file type"""

    if pathlib.Path(file_name).suffix == ".root":
        return McFileTypes.EIC_SMEAR

    with open(file_name, 'r') as f:
        line = ""
        try:
            i = 0
            while not line:                 # Just to fake a lot of readlines and hit the end
                line = next(f).replace('\n', '')
                i += 1

                # We don't need HepMC::Version ... lines, they are the same for Hepmc2 and 3
                if "HepMC::Version" in line.strip():
                    line = None
                    continue

                # Don't go too far away if one can't determine file type
                if i > 20:
                    break

        except StopIteration:
            return McFileTypes.UNKNOWN

        # Determining file types
        if "BEAGLE EVENT FILE" in line:
            return McFileTypes.BEAGLE
        elif "HepMC::IO_GenEvent-START_EVENT_LISTING" in line:
            return McFileTypes.HEPMC2
        elif "HepMC::Asciiv3-START_EVENT_LISTING" in line:
            return McFileTypes.HEPMC3
        elif "PYTHIA EVENT FILE" in line:
            return McFileTypes.PYTHIA6_EIC
        elif "Adjusted LUND Type" in line:
            return McFileTypes.LUND_ALT
        elif len(line.split()) == 10:
            return McFileTypes.LUND_GEMC
    return McFileTypes.UNKNOWN


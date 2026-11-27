"""Reproduce the exploratory WWOX sphingosine-pathway RNA panel."""

import argparse
from pathlib import Path
import sys

COMPOUNDS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(COMPOUNDS / "clemizole"))
from replay_receptors_and_exposure import bulk_panel, formatted, verified_expression
from coagonist_screen import nuclei_panel

PANEL = (
    "S1pr1", "S1pr3", "S1pr5", "Sphk1", "Sphk2", "Pdgfra",
    "Mbp", "Plp1", "Mog", "Sox10", "Gfap", "Aif1",
)


def main(files):
    verified_expression(files)
    print(
        "model\taccession\tgene\tctrl_n\tko_n\tctrl_positive\tko_positive\t"
        "ctrl_mean\tko_mean\tlog2_delta\tomit_min\tomit_max\tmapping"
    )
    for row in formatted(bulk_panel(files, PANEL)):
        print("\t".join(map(str, row)))


def print_nuclei(files):
    print("pool\tclass\tgene\tnuclei\tall_UMI\tgene_UMI\tCPM")
    for row in formatted(nuclei_panel(files, PANEL[:5])):
        print("\t".join(map(str, row)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path, help="Shared checkout's files directory")
    parser.add_argument("--nuclei", action="store_true", help="Replay the two pooled hippocampal libraries")
    options = parser.parse_args()
    replay = print_nuclei if options.nuclei else main
    replay(options.files)

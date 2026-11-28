"""Reproduce an untreated-WWOX sensitivity screen for DCA uptake and PDC regulation."""
import argparse
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    sys.path.insert(0, str(args.repo / "disease-models/wwox/research/drug_repurposing"
                           / "continuous_compounds/thiamine"))
    from screen import run

    targets = ["Slc5a8", "Slc16a1", "Slc16a3", "Slc16a7",
               "Pdk1", "Pdk2", "Pdk3", "Pdk4", "Pdp1", "Pdp2", "Dlat", "Glo1", "Hagh"]
    run(args.files, target_genes=targets, output=args.output, missing_value="NA")


if __name__ == "__main__":
    main()

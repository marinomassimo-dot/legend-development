"""Replay the prespecified deoxycytidine salvage RNA comparison."""
import argparse
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drug_repurposing", type=Path)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    cbdv = args.drug_repurposing / "continuous_compounds" / "cannabidivarin"
    sys.path.insert(0, str(cbdv))
    from replay_trp_expression import compare_expression

    compare_expression(args.drug_repurposing, args.files, args.output,
                       ("Dck", "Tk2", "Tk1", "Cda", "Dctd", "Slc29a1", "Slc29a2", "Slc25a33",
                        "Slc25a36", "Rrm2b", "Polg"), "wwox_bulk.tsv")


if __name__ == "__main__":
    main()

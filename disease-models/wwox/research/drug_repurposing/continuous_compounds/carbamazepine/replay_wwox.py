"""Replay the RNA plausibility comparison for the carbamazepine inositol hypothesis."""
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

    targets = ("Slc5a3", "Slc5a11", "Slc2a13", "Isyna1", "Impa1", "Cdipt", "Pip5k1c", "Kcnq2")
    compare_expression(args.drug_repurposing, args.files, args.output, targets, "wwox_bulk.tsv")


if __name__ == "__main__":
    main()

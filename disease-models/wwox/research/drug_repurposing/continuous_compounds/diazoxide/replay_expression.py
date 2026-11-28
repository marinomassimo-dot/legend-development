"""Replay the held WWOX RNA comparison for both canonical neuronal KATP subunits."""
import argparse
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drug_repurposing", type=Path)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    compounds = args.drug_repurposing / "continuous_compounds"
    sys.path.insert(0, str(compounds / "cannabidivarin"))
    from replay_trp_expression import compare_expression

    compare_expression(args.drug_repurposing, args.files, args.output, ("Abcc8", "Kcnj11"), "katp_bulk.tsv")


if __name__ == "__main__":
    main()

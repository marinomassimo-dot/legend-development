"""Replay sodium-channel expression coverage in the existing WWOX model matrices."""
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
                       ("Scn1a", "Scn2a", "Scn8a"), "sodium_bulk.tsv")


if __name__ == "__main__":
    main()

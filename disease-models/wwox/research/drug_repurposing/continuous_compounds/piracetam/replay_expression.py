"""Replay fixed mouse and organoid transcript and assigned-nucleus comparisons."""
import argparse
from pathlib import Path
import sys


TARGETS = (
    "Gria1", "Gria2", "Gria3", "Gria4", "Cacng2", "Cacng3", "Cacng4",
    "Cacng7", "Cacng8", "Cnih2", "Cnih3", "Cacna1b", "Cacna1a",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drug_repurposing", type=Path)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    cbdv = args.drug_repurposing / "continuous_compounds" / "cannabidivarin"
    sys.path.insert(0, str(cbdv))
    from replay_trp_expression import compare_expression

    compare_expression(args.drug_repurposing, args.files, args.output, TARGETS, "expression.tsv")


if __name__ == "__main__":
    main()

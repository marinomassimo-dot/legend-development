"""Recompute WWOX oxytocin receptor and chloride regulation contrasts."""
import argparse
from pathlib import Path
import sys


TARGETS = (
    "Oxt", "Oxtr", "Avpr1a", "Avpr1b", "Slc12a5", "Slc12a2",
    "Wnk1", "Wnk3", "Stk39", "Oxsr1", "Prkca", "Slc4a3",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drug_repurposing", type=Path)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    existing = args.drug_repurposing / "continuous_compounds" / "cannabidivarin"
    sys.path.insert(0, str(existing))
    from replay_trp_expression import compare_expression

    compare_expression(args.drug_repurposing, args.files, args.output, TARGETS, "bulk.tsv")


if __name__ == "__main__":
    main()

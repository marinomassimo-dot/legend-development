"""Recompute WWOX cytosolic mevalonate, prenylation and cargo expression checks."""
import argparse
from pathlib import Path
import sys


TARGETS = (
    "Hmgcr", "Mvk", "Fdps", "Ggps1", "Fdft1", "Rabggta", "Rabggtb",
    "Chm", "Chml", "Pggt1b", "Rac1", "Rhoa", "Rab3a", "Rab6a", "Rab6b",
    "Gdi1", "Copb2", "Cyp46a1",
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

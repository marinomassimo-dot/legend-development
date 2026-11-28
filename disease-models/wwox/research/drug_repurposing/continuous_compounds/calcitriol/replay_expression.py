"""Replay the VDR axis transcript comparison and cell-mixture controls."""
import argparse
from pathlib import Path
import sys


TARGETS = (
    "Vdr", "Rxra", "Rxrb", "Rxrg", "Cyp27b1", "Cyp24a1", "Gc", "Lrp2",
    "Pdgfra", "Olig2", "Mbp", "Mog", "Plp1",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drug_repurposing", type=Path)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    cbv = args.drug_repurposing / "continuous_compounds" / "cannabidivarin"
    sys.path.insert(0, str(cbv))
    from replay_trp_expression import compare_expression

    compare_expression(args.drug_repurposing, args.files, args.output, TARGETS, "expression.tsv")


if __name__ == "__main__":
    main()

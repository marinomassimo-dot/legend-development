"""Replay NMDA subunit, HCN and inhibitory context in public WWOX datasets."""
import argparse
from pathlib import Path
import sys


TARGETS = ("Grin1", "Grin2a", "Grin2b", "Grin2c", "Grin2d", "Hcn1", "Hcn2",
           "Pvalb", "Sst", "Slc12a5", "Slc12a2")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drug_repurposing", type=Path)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    sys.path.insert(0, str(args.drug_repurposing / "continuous_compounds" / "cannabidivarin"))
    from replay_trp_expression import compare_expression

    compare_expression(args.drug_repurposing, args.files, args.output, TARGETS, "bulk.tsv")


if __name__ == "__main__":
    main()

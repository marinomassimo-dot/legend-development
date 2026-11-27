"""Replay WWOX valine transport, mitochondrial disposal and charging RNA."""
import argparse
from pathlib import Path
import sys


TARGETS = (
    "Slc7a5", "Slc3a2", "Slc43a1", "Slc43a2", "Slc25a44", "Bcat1", "Bcat2",
    "Bckdha", "Dbt", "Bckdk", "Ppm1k", "Acad8", "Echs1", "Hibch", "Hibadh",
    "Aldh6a1", "Pcca", "Pccb", "Mut", "Pdha1", "Dlat", "Vars", "Vars2",
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

"""Check transcripts for SK, BK and the calcium-entry and voltage-history comparators."""
import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "cannabidivarin"))
from replay_trp_expression import compare_expression


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drug_repurposing", type=Path)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    targets = tuple("Kcnn1 Kcnn2 Kcnn3 Kcnma1 Kcnmb4 Cacna1a Hcn1".split())
    compare_expression(args.drug_repurposing, args.files, args.output, targets, "native_bulk.tsv")

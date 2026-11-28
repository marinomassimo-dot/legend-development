"""Replay the predeclared retinoid and sterol-transfer transcripts in held WWOX models."""
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
    targets = tuple("Rxra Rxrb Rxrg Nr1h3 Nr1h2 Abca1 Abcg1 Apoe".split())
    compare_expression(args.drug_repurposing, args.files, args.output, targets, "native_bulk.tsv")

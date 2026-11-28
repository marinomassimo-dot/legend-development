"""Replay the predeclared adenosine-pathway transcripts in held WWOX models."""
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
    targets = tuple("Adora2a Adora1 Entpd1 Nt5e Slc29a1 Slc29a2 Ada".split())
    compare_expression(args.drug_repurposing, args.files, args.output, targets, "native_bulk.tsv")

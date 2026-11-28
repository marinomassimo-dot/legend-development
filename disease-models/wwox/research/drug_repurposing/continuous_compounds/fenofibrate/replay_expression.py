"""Replay PPAR pathway and ketone-handling transcripts in WWOX models."""
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
    targets = tuple("Ppara Ppargc1a Acox1 Cpt1a Hmgcs2 Bdh1 Oxct1 Slc16a1 Slc16a7 Chrnb2".split())
    compare_expression(args.drug_repurposing, args.files, args.output, targets, "native_bulk.tsv")

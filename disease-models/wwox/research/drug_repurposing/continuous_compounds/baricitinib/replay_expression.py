"""Replay JAK cytokine responses and trophic receptor transcripts in public WWOX models."""
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
    targets = tuple("Ifnar1 Ifnar2 Jak1 Jak2 Tyk2 Stat1 Stat3 Cxcl10 Isg15 Ifit1 Irf7 Usp18 Il6ra Il6st Lifr Cntfr Socs3 Klf6".split())
    compare_expression(args.drug_repurposing, args.files, args.output, targets, "native_bulk.tsv")

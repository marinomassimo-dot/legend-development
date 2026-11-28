"""Check the nervonic acid pathway and mature oligodendrocyte markers."""
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
    targets = tuple("Elovl1 Cers2 Ugt8a Gal3st1 Gltp Mbp Plp1 Mog Pdgfra".split())
    compare_expression(args.drug_repurposing, args.files, args.output, targets, "native_bulk.tsv",
                       human_symbols={"Ugt8a": "UGT8"})

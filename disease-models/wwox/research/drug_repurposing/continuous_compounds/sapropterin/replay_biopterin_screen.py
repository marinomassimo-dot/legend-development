"""Replay existing WWOX RNA contrasts for biopterin synthesis and NOS context."""

import argparse
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE.parent / "ribitol"), str(HERE.parent / "thiamine")]
import replay_matriglycan_screen as bulk
from cell_types import run as summarize_nuclei


PANEL = {
    "de_novo": ("Gch1", "Gchfr", "Pts", "Spr"),
    "recycling": ("Pcbd1", "Qdpr", "Dhfr"),
    "nos": ("Nos1", "Nos2", "Nos3"),
    "monoamine_context": ("Th", "Tph2"),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("--out", type=Path, default=HERE)
    args = parser.parse_args()

    bulk.GENES = PANEL
    bulk.ALIASES = {}
    bulk.verified_expression(args.files)
    args.out.mkdir(parents=True, exist_ok=True)
    bulk.tsv(args.out / "biopterin_bulk.tsv",
             "model accession category gene mapped_symbol ctrl_n ko_n ctrl_positive ko_positive "
             "ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(), bulk.bulk_rows(args.files))

    nuclei = args.out / "nuclei"
    nuclei.mkdir(exist_ok=True)
    summarize_nuclei(args.files, [gene for group in PANEL.values() for gene in group], nuclei)


if __name__ == "__main__":
    main()

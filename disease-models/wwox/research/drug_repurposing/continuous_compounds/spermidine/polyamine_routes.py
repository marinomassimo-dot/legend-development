"""Replay the spermidine routing panel across the held WWOX expression datasets."""

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sodium_benzoate"))
from coagonist_screen import bulk_panel, nuclei_panel, tsv


PANEL = (
    "Odc1", "Amd1", "Srm", "Sms", "Sat1", "Paox", "Smox", "Atp13a2",
    "Atp13a3", "Dhps", "Dohh", "Eif5a", "Atg3", "Sqstm1",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--atp13a4", action="store_true",
                        help="Replay the separate ATP13A4 follow-up comparison.")
    args = parser.parse_args()
    panel = ("Atp13a4",) if args.atp13a4 else PANEL
    args.output.mkdir(parents=True, exist_ok=True)
    tsv(args.output / "contrasts.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_panel(args.files, panel))
    tsv(args.output / "nuclei.tsv", "pool cell_class gene nuclei all_UMI gene_UMI CPM".split(),
        nuclei_panel(args.files, panel))


if __name__ == "__main__":
    main()

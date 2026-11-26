"""Replay WWOX GABA-B, rebound and myelin lineage RNA comparisons."""

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sodium_benzoate"))
from coagonist_screen import bulk_panel, nuclei_panel, tsv


PANEL = (
    "Gabbr1", "Gabbr2", "Kcnj3", "Kcnj6", "Kcnj9", "Cacna1g", "Cacna1h", "Cacna1i",
    "Pdgfra", "Olig2", "Sox10", "Myrf", "Mbp", "Plp1",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    tsv(
        args.output / "contrasts.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_panel(args.files, PANEL),
    )
    tsv(
        args.output / "nuclei.tsv",
        "pool cell_class gene nuclei all_UMI gene_UMI CPM".split(),
        nuclei_panel(args.files, PANEL),
    )


if __name__ == "__main__":
    main()

"""Replay the fixed allopurinol pathway panel in held WWOX expression datasets."""

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sodium_benzoate"))
from coagonist_screen import bulk_panel, nuclei_panel, tsv


MOUSE_PANEL = (
    "Xdh", "Pnp", "Ada", "Hprt", "Aprt", "Adsl", "Adss",
    "Prps1", "Prps2", "Slc29a1", "Slc29a2", "Nt5e", "Abcg2", "Ampd2",
)
OUTPUT_SYMBOLS = {"HPRT": "HPRT1", "ADSS": "ADSS2"}


def harmonized_bulk(files):
    for model, accession, gene, *values in bulk_panel(files, (*MOUSE_PANEL, "Hprt1")):
        duplicate = "HPRT" if model == "human_organoid" else "HPRT1"
        if gene != duplicate:
            yield model, accession, OUTPUT_SYMBOLS.get(gene, gene), *values


def harmonized_nuclei(files):
    for pool, cell_class, gene, *values in nuclei_panel(files, MOUSE_PANEL):
        yield pool, cell_class, OUTPUT_SYMBOLS.get(gene, gene), *values


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    tsv(
        args.output / "bulk.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        harmonized_bulk(args.files),
    )
    tsv(
        args.output / "nuclei.tsv",
        "pool cell_class gene nuclei all_UMI gene_UMI CPM".split(),
        harmonized_nuclei(args.files),
    )


if __name__ == "__main__":
    main()

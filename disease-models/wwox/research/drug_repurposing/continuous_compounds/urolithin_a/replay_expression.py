"""Replay the fixed Urolithin A pathway panel in held public WWOX datasets."""

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sodium_benzoate"))
from coagonist_screen import bulk_panel, nuclei_panel, tsv


PANEL = (
    "Pink1", "Park2", "Optn", "Bnip3", "Bnip3l", "Fundc1",
    "Dnm1l", "Mfn2", "Opa1", "Tfam", "Ppargc1a", "Tomm20",
    "Lamp1", "Ctsd", "Sqstm1",
)


def harmonized_bulk(files):
    for row in bulk_panel(files, (*PANEL, "Prkn")):
        model, accession, gene, *values = row
        source_symbol = "PRKN" if model == "human_organoid" else "PARK2"
        if gene in ("PARK2", "PRKN") and gene != source_symbol:
            continue
        yield model, accession, "PRKN" if gene == "PARK2" else gene, *values


def harmonized_nuclei(files):
    for pool, cell_class, gene, *values in nuclei_panel(files, PANEL):
        yield pool, cell_class, "PRKN" if gene == "PARK2" else gene, *values


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    bulk = list(harmonized_bulk(args.files))
    nuclei = list(harmonized_nuclei(args.files))
    args.output.mkdir(parents=True, exist_ok=True)
    tsv(
        args.output / "bulk.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk,
    )
    tsv(
        args.output / "nuclei.tsv",
        "pool cell_class gene nuclei all_UMI gene_UMI CPM".split(),
        nuclei,
    )


if __name__ == "__main__":
    main()

"""Compare ergothioneine transport and mitochondrial or lipid redox transcripts."""

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sodium_benzoate"))
from coagonist_screen import bulk_panel, nuclei_panel, tsv


PANEL = (
    "Slc22a4", "Slc22a15", "Slc22a5", "Gpx4", "Slc7a11", "Gclc", "Gsr",
    "Aifm2", "Sod2", "Prdx3", "Hmox1",
)

DEVELOPMENT_PANEL = (
    "Ntrk2", "Ntf5", "Bdnf", "Atoh1", "Hes1", "Mki67", "Satb2", "Slc12a5",
)
DEVELOPMENT_BULK_PANEL = ("Ntrk2", "Ntf5", "Ntf4", *DEVELOPMENT_PANEL[2:])


def development_bulk(files):
    for row in bulk_panel(files, DEVELOPMENT_BULK_PANEL):
        # The held mouse annotation uses Ntf5 for the human NTF4 orthologue.
        model, _, gene, *_ = row
        unused_alias = "NTF5" if model == "human_organoid" else "NTF4"
        if gene != unused_alias:
            yield row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--panel", choices=("uptake", "development"), default="uptake")
    args = parser.parse_args()
    panel = DEVELOPMENT_PANEL if args.panel == "development" else PANEL
    bulk_rows = development_bulk(args.files) if args.panel == "development" else bulk_panel(args.files, panel)
    args.output.mkdir(parents=True, exist_ok=True)
    tsv(args.output / "contrasts.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_rows)
    tsv(args.output / "nuclei.tsv", "pool cell_class gene nuclei all_UMI gene_UMI CPM".split(),
        nuclei_panel(args.files, panel))


if __name__ == "__main__":
    main()

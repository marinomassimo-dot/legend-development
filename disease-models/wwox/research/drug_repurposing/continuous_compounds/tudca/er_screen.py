"""Replay descriptive WWOX RNA comparisons for TUDCA and ER stress context."""

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sodium_benzoate"))
from coagonist_screen import bulk_panel, nuclei_panel, tsv


PANEL = (
    "Echs1", "Fasn", "Eif2ak3", "Eif2s1", "Atf4", "Ddit3", "Ppp1r15a", "Ern1", "Xbp1",
    "Hspa5", "Hsp90b1", "Herpud1", "Dnajb9", "Atp2a2", "Ryr2", "Calr", "Gpbar1",
    "Nr1h4", "Slc10a1", "Slc51a", "Slc51b",
)

LIPID_PANEL = ("Acadl", "Acat1", "Hadha", "Cpt1a", "Acadvl", "Srebf1", "Pdha1")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--lipid-panel", action="store_true", help="replay the secondary lipid comparison")
    args = parser.parse_args()

    panel = LIPID_PANEL if args.lipid_panel else PANEL
    args.output.mkdir(parents=True, exist_ok=True)
    bulk_columns = (
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean "
        "ko_mean log2_delta omit_min omit_max mapping"
    ).split()
    nuclei_columns = "pool cell_class gene nuclei all_UMI gene_UMI CPM".split()
    bulk_output = "lipid_bulk.tsv" if args.lipid_panel else "contrasts.tsv"
    nuclei_output = "lipid_nuclei.tsv" if args.lipid_panel else "nuclei.tsv"
    tsv(args.output / bulk_output, bulk_columns, bulk_panel(args.files, panel))
    tsv(args.output / nuclei_output, nuclei_columns, nuclei_panel(args.files, panel))


if __name__ == "__main__":
    main()

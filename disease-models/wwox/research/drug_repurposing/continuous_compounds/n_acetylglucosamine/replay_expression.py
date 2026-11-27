"""Replay the fixed GlcNAc salvage, branching and oligodendrocyte panel."""

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sodium_benzoate"))
from coagonist_screen import bulk_panel, nuclei_panel, tsv


PANEL = (
    "Nagk", "Pgm3", "Uap1", "Gnpnat1", "Slc35a3", "Mgat1", "Mgat2",
    "Mgat4a", "Mgat4b", "Mgat5", "Pdgfra", "Cspg4", "Olig2", "Sox10",
    "Myrf", "Plp1", "Mbp",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    arguments = parser.parse_args()
    arguments.output.mkdir(parents=True, exist_ok=True)
    tsv(
        arguments.output / "bulk.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_panel(arguments.files, PANEL),
    )
    tsv(
        arguments.output / "nuclei.tsv",
        "pool cell_class gene nuclei all_UMI gene_UMI CPM".split(),
        nuclei_panel(arguments.files, PANEL),
    )


if __name__ == "__main__":
    main()

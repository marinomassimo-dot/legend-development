"""Compare quinone reduction and respiratory context across held WWOX RNA data."""

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sodium_benzoate"))
from coagonist_screen import bulk_panel, nuclei_panel, tsv


PANEL = (
    "Nqo1", "Nqo2", "Nfe2l2", "Keap1", "G6pdx", "Pgd", "Idh1", "Me1", "Ndufs2",
    "Ndufv1", "Uqcrc1", "Uqcrfs1", "Aifm2",
)
BULK_PANEL = (*PANEL, "G6pd")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    rows = (
        row
        for row in bulk_panel(args.files, BULK_PANEL)
        # The held mouse annotation calls the human G6PD orthologue G6pdx.
        if row[2] != ("G6PDX" if row[0] == "human_organoid" else "G6PD")
    )
    tsv(
        args.output / "contrasts.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        rows,
    )
    tsv(
        args.output / "nuclei.tsv",
        "pool cell_class gene nuclei all_UMI gene_UMI CPM".split(),
        nuclei_panel(args.files, PANEL),
    )


if __name__ == "__main__":
    main()

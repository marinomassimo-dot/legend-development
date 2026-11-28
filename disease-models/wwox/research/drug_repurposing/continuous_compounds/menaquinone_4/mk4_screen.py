"""Compare MK-4 reduction, reconstruction and carboxylation pathway transcripts."""

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sodium_benzoate"))
from coagonist_screen import bulk_panel, nuclei_panel, tsv


PANEL = (
    "Aifm2", "Vkorc1", "Vkorc1l1",  # Quinone reduction routes
    "Ubiad1",  # Side-chain reconstruction
    "Ggcx", "Gas6", "Tyro3", "Axl",  # Carboxylation and distinct receptors
    "Gpx4", "Acsl4",  # Lipid oxidation pathway and substrate controls
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    tsv(args.output / "contrasts.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_panel(args.files, PANEL))
    tsv(args.output / "nuclei.tsv", "pool cell_class gene nuclei all_UMI gene_UMI CPM".split(),
        nuclei_panel(args.files, PANEL))


if __name__ == "__main__":
    main()

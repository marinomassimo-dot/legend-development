"""Screen WWOX neural datasets for cystine export and competing lysosomal routes."""

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sodium_benzoate"))
from coagonist_screen import bulk_panel, nuclei_panel, tsv


MOUSE_PANEL = (
    "Ctns", "Pqlc2",  # Cystine and mixed-disulfide export
    "Wdr41", "3110043O21Rik", "Smcr8",  # Amino-acid sensing complex
    "Atp6v1a", "Lamp1", "Sqstm1", "Chac1",  # pH, lysosome, cargo and GSH controls
)
HUMAN_PANEL = ("CTNS", "PQLC2", "WDR41", "C9orf72", "SMCR8", "ATP6V1A", "LAMP1", "SQSTM1", "CHAC1")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    tsv(args.output / "contrasts.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_panel(args.files, MOUSE_PANEL, human_panel=HUMAN_PANEL))
    tsv(args.output / "nuclei.tsv", "pool cell_class gene nuclei all_UMI gene_UMI CPM".split(),
        nuclei_panel(args.files, MOUSE_PANEL))


if __name__ == "__main__":
    main()

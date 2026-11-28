"""Replay the fixed WWOX fucose salvage and core fucosylation panel."""

import argparse
from pathlib import Path
import sys

COMPOUNDS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(COMPOUNDS / "sodium_benzoate"), str(COMPOUNDS / "jbpos0101")]
from coagonist_screen import bulk_panel, nuclei_panel, tsv
from replay_exposure_and_receptors import verified_expression

PANEL = ("Fuk", "Fpgt", "Gmds", "Tsta3", "Slc35c1", "Fut8", "Il6st", "Gria2", "L1cam")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    verified_expression(args.files)
    args.out.mkdir(parents=True, exist_ok=True)
    tsv(args.out / "wwox_fucose_bulk.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_panel(args.files, PANEL))
    tsv(args.out / "wwox_fucose_nuclei.tsv",
        "pool cell_class gene nuclei all_UMI gene_UMI CPM".split(),
        nuclei_panel(args.files, PANEL))

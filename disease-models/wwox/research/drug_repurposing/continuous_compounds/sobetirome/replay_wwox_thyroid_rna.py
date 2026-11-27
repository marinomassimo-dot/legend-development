"""Replay the fixed WWOX thyroid signaling and lineage RNA panel."""

import argparse
from pathlib import Path
import sys

COMPOUNDS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(COMPOUNDS / "sodium_benzoate"), str(COMPOUNDS / "jbpos0101")]
from coagonist_screen import bulk_panel, nuclei_panel, tsv
from replay_exposure_and_receptors import verified_expression

PANEL = (
    "Thra", "Thrb", "Slc16a2", "Slco1c1", "Dio2", "Dio3",
    "Klf9", "Hr", "Cnp", "Mog",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    verified_expression(args.files)
    args.out.mkdir(parents=True, exist_ok=True)
    tsv(
        args.out / "wwox_thyroid_bulk.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_panel(args.files, PANEL),
    )
    tsv(
        args.out / "wwox_thyroid_nuclei.tsv",
        "pool cell_class gene nuclei all_UMI gene_UMI CPM".split(),
        nuclei_panel(args.files, PANEL),
    )


if __name__ == "__main__":
    main()

"""Replay a descriptive WWOX RNA panel using the established LEGEND mapping."""

import argparse
from pathlib import Path
import sys


PANEL = ("Gapdh", "Pcx", "Hcar2", "Nfe2l2", "Nqo1", "Hmox1", "Gclc")
HUMAN_PANEL = ("GAPDH", "PC", "HCAR2", "NFE2L2", "NQO1", "HMOX1", "GCLC")
HERE = Path(__file__).resolve().parent
BULK_HEADER = "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping"
NUCLEAR_HEADER = "pool class gene nuclei all_UMI gene_UMI CPM"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("--out", type=Path, default=HERE)
    args = parser.parse_args()
    sys.path.insert(0, str(HERE.parent / "jbpos0101"))
    from replay_exposure_and_receptors import bulk_panel, nuclei_panel, tsv, verified_expression

    verified_expression(args.files)
    args.out.mkdir(parents=True, exist_ok=True)
    tsv(args.out / "wwox_bulk.tsv", BULK_HEADER.split(), bulk_panel(args.files, PANEL, human_panel=HUMAN_PANEL))
    tsv(args.out / "wwox_nuclei.tsv", NUCLEAR_HEADER.split(), nuclei_panel(args.files, PANEL))


if __name__ == "__main__":
    main()

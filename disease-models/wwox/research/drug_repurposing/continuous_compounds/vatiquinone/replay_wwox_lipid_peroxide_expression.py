"""Descriptive expression screen for the held WWOX lipid-peroxide comparison."""

import argparse
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "ribitol"))
import replay_matriglycan_screen as common

GENES = {
    "lipoxygenases": ("Alox15", "Alox15b", "Alox12", "Pebp1"),
    "phospholipid_substrate": ("Acsl4", "Lpcat3"),
    "peroxide_defenses": ("Gpx4", "Slc7a11", "Aifm2"),
    "quinone_reduction_context": ("Nqo1",),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    args = parser.parse_args()
    common.GENES = GENES
    common.ALIASES = {"Alox15b": ("Alox8",), "Aifm2": ("Fsp1",)}
    common.verified_expression(args.files)
    common.tsv(
        HERE / "wwox_lipid_peroxide_expression.tsv",
        "model accession pathway gene mapped_symbol ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        common.bulk_rows(args.files),
    )


if __name__ == "__main__":
    main()

"""Reproduce the descriptive bulk expression contrast for RT001 conversion."""

import argparse
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "ribitol"))
import replay_matriglycan_screen as common


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("shared_files", type=Path)
    args = parser.parse_args()
    common.GENES = {
        "precursor_desaturation_elongation": ("Fads2", "Elovl5", "Fads1", "Elovl2"),
        "membrane_allocation": ("Acsl4", "Lpcat3", "Agpat3", "Pla2g6", "Tmem189", "Gnpat", "Agps"),
        "product_context": ("Alox15", "Ptgs2", "Gpx4"),
    }
    common.ALIASES = {"Tmem189": ("Peds1",)}
    common.verified_expression(args.shared_files)
    common.tsv(
        HERE / "wwox_conversion_expression.tsv",
        "model accession category gene mapped_symbol ctrl_n ko_n ctrl_positive ko_positive "
        "ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        common.bulk_rows(args.shared_files),
    )


if __name__ == "__main__":
    main()

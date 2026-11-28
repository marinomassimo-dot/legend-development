"""Replay approximate Phensy panel means and source concentration arithmetic."""

from collections import defaultdict
import csv
from pathlib import Path
import sys


def main():
    with Path(__file__).with_name("panel_readouts.tsv").open(newline="") as source:
        histories = defaultdict(dict)
        for row in csv.DictReader(source, delimiter="\t"):
            zero_y, two_y, bar_y = (int(row[key]) for key in ("zero_y", "two_y", "bar_y"))
            ratio_per_pixel = 2 / (zero_y - two_y)
            ratio = (zero_y - bar_y) * ratio_per_pixel
            histories[row["history"]][row["group"]] = (
                ratio, ratio_per_pixel, int(row["cells"]), int(row["mice"]),
            )

    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("comparison", "history", "group", "estimate", "reading_low", "reading_high", "cells", "mice"))
    for history, groups in histories.items():
        saline, saline_unit, _, _ = groups["ethanol_saline"]
        for group, (ratio, unit, cells, mice) in groups.items():
            writer.writerow(("figure_mean", history, group, f"{ratio:.4f}", "", "", cells, mice))
            if group.startswith("ethanol_") and group != "ethanol_saline":
                delta = ratio - saline
                reading_error = 3 * (unit + saline_unit)
                low, high = (round(delta + offset, 4) + 0.0 for offset in (-reading_error, reading_error))
                writer.writerow(("difference_vs_ethanol_saline", history, group, f"{delta:.4f}",
                                 f"{low:.4f}", f"{high:.4f}", "NA", "NA"))

    # Hammarberg abstract, assuming mass-equivalent free acid (FDA chemistry review).
    highest_csf_estimate_um = 33 / 181.21
    writer.writerow(("upper_semiquantitative_csf_uM", "", "free_acid_basis",
                     f"{highest_csf_estimate_um:.6f}", "NA", "NA", "NA", "NA"))
    # Spanagel Results, the lowest stated competitive assay concentration.
    for anions_per_nominal_unit in (1, 2):
        approximate_ratio = 100 * anions_per_nominal_unit / highest_csf_estimate_um
        writer.writerow(("assay_to_csf_concentration_ratio", "", f"{anions_per_nominal_unit}_anion_per_reported_unit",
                         f"{approximate_ratio:.1f}", "NA", "NA", "NA", "NA"))


if __name__ == "__main__":
    main()

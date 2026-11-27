"""Replay the Gerin figure estimates and US label's clinical benchmarks."""

import csv
import sys

MOLAR_MASS = 152.15


def comparisons():
    # Gerin et al. Fig. 7B, printed/PDF p. 9 rendered at 160 dpi.
    # Bar fills, not upper error bars. The published graph reports normalized HPLC peak areas.
    y_zero, y_06 = 579, 419
    for tissue, untreated_y, ribitol_y in (("brain", 501, 448), ("muscle", 549, 484)):
        untreated, ribitol = (0.6 * (y_zero - y) / (y_zero - y_06) for y in (untreated_y, ribitol_y))
        yield ("Gerin 2016 Fig. 7B", tissue, f"{untreated:.4f}", f"{ribitol:.4f}",
               f"{ribitol / untreated:.3f}", "HPLC peak a.u.; treated/control; control n=4, treated n=3")
    peak_mg_per_l = 141
    day_average_mg_per_l = 788 / 24
    for measure, mg_per_l in (("mean plasma peak", peak_mg_per_l), ("AUC0–24/24", day_average_mg_per_l)):
        mm = mg_per_l / MOLAR_MASS
        yield ("US label §12.3 and Gerin Fig. 7D–E", measure, f"{mm:.4f}", "3.0000",
               f"{3 / mm:.3f}", "mM; nominal fibroblast medium/total plasma; not a site-exposure match")
    for month, control, treated in ((3, -0.04, 17.12), (12, 0.82, 23.60)):
        yield ("US label §12.2", f"muscle αDG at month {month}", control, treated,
               f"{treated-control:.2f}", "points of glycosylated αDG relative to assay control")
    for endpoint, control, treated, contrast, note in (
        ("100MTT velocity", -0.12, 0.14, 0.27, "m/s; n=21 placebo, n=40 ribitol"),
        ("seated FVC percent predicted", -1.92, 2.97, 4.89, "points; n=22 placebo, n=35 ribitol"),
    ):
        yield "US label Table 2", endpoint, control, treated, contrast, note


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("source", "endpoint", "reference", "comparison", "reported_or_replayed_contrast", "unit_and_denominator"))
    writer.writerows(comparisons())


if __name__ == "__main__":
    main()

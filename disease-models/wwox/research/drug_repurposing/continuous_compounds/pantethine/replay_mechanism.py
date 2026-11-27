#!/usr/bin/env python3
"""Replay descriptive contrasts from identified pantethine primary evidence."""

from itertools import product

# Brunetti et al., Brain (2014), Fig. 7, print p. 65.
# Render the Groningen repository PDF (13 pages with cover) with:
# pdftoppm -f 10 -l 10 -r 170 -gray brunetti_primary.pdf fig7
# Figure axes at rows 885 (0) and 664 (600); read the white bar's
# upper edge offset from its center, away from the error bar.
# Rows bounds below test raster/edge reading, never sampling uncertainty.
axis_zero, axis_600 = 885, 664
bar_rows = (796, 814, 740, 728)
reading_radius = 2


def oxygen_consumption(row):
    return 600 * (axis_zero - row) / (axis_zero - axis_600)


def respiration_contrasts(control_wt, control_ko, treated_wt, treated_ko):
    wt_change = treated_wt - control_wt
    ko_change = treated_ko - control_ko
    return (
        wt_change,
        ko_change,
        ko_change - wt_change,
        treated_wt / control_wt,
        treated_ko / control_ko,
    )


labels = ("WT_difference", "KO_difference", "KO_minus_WT_difference", "WT_ratio", "KO_ratio")
nominal_ocr = tuple(map(oxygen_consumption, bar_rows))
nominal_contrasts = respiration_contrasts(*nominal_ocr)
edge_contrasts = [
    respiration_contrasts(*(oxygen_consumption(row + delta) for row, delta in zip(bar_rows, shifts)))
    for shifts in product((-reading_radius, reading_radius), repeat=len(bar_rows))
]

print("source\tmetric\tnominal\tmin_edge\tmax_edge\tunits")
for label, ocr in zip(("WT_control", "KO_control", "WT_pantethine", "KO_pantethine"), nominal_ocr):
    print(f"Brunetti_Fig7_OCR_ADP\t{label}\t{ocr:.2f}\tNA\tNA\tOCR_axis")
for label, nominal, edge_values in zip(labels, nominal_contrasts, zip(*edge_contrasts)):
    unit = "ratio" if label.endswith("_ratio") else "OCR_axis"
    print(f"Brunetti_Fig7_OCR_ADP\t{label}\t{nominal:.2f}\t{min(edge_values):.2f}\t{max(edge_values):.2f}\t{unit}")

# Rana et al., PNAS (2010), Results and Fig. 3D: 42% lower JC-1
# signal/positive fraction relative to WT (set 100%), then 84% of WT.
baseline_fraction, treated_fraction = 1 - 0.42, 0.84
fraction_of_loss_restored = (treated_fraction - baseline_fraction) / (1 - baseline_fraction)
print(f"Rana_Fig3D_JC1\tfraction_of_WT_gap_closed\t{fraction_of_loss_restored:.4f}\tNA\tNA\tratio")

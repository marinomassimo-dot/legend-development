"""Reproduce approximate bar means from manually read pixel coordinates (top-origin)."""
import csv
import sys

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("PMID", "panel", "measure", "control", "treated", "unit", "fold",
                 "unit_per_pixel", "comparison_annotated"))
# Zero and upper reference tick, its value, control and treated bar tops.
# Supplement p.8 rendered at a 1000-pixel maximum dimension using pdftoppm.
for pmid, panel, measure, unit, zero, tick, tick_value, ctrl, drug, annotated in (
    (32753675, "5A", "Slc7a11_injured", "relative_RNA", 246, 60, 8, 153, 131, "no"),
    (32753675, "S2B", "Slc7a11_stressed_astrocytes", "relative_RNA", 617, 472, 60, 562, 522, "no"),
    (32753675, "5C", "GSH_in_ChAT_cells", "relative_staining", 998, 767, 2.5, 905, 847, "yes_unit_unresolved"),
    (26571146, "1B", "selected_neurite_length_10uM", "um", 373, 90, 140, 144, 117, "yes"),
    (26571146, "1D", "neurite_bearing_cells_10uM", "percent", 751, 498, 60, 521, 528, "no"),
    (26571146, "4", "oxidant_exposed_MTS_10uM", "percent_of_unstressed", 458, 65, 100, 127, 95, "yes"),
):
    scale = tick_value / (zero - tick)
    vehicle, exposed = (zero - ctrl) * scale, (zero - drug) * scale
    writer.writerow([pmid, panel, measure, round(vehicle, 1), round(exposed, 1), unit,
                     round(exposed / vehicle, 2), round(scale, 3), annotated])

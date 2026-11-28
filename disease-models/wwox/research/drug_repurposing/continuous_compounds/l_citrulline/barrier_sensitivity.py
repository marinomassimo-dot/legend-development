"""Dimensionless occupancy of the fitted rat endothelial uptake components."""
import csv
import sys

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("assay_nominal_citrulline_uM", "Km_high_affinity_uM",
                 "fraction_of_high_affinity_component_Vmax", "Km_low_affinity_uM",
                 "fraction_of_low_affinity_component_Vmax"))
# Concentrations drawn from the pediatric MELAS group plasma means (before/after).
# Rat immortalized-cell uptake model, no competition and no cross-barrier flux.
for concentration in (21, 156):
    writer.writerow((concentration, 30.9, round(concentration / (30.9 + concentration), 4),
                     1690, round(concentration / (1690 + concentration), 4)))

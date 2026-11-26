"""Reproduce descriptive turnover ratios from El-Hattab et al., Results §3 / Fig. 2."""
import csv
import sys

# Group means: NO production, total arginine flux and de novo arginine synthesis
# in µmol/kg/h; plasma arginine and citrulline in µmol/L.
measurements = [
    ("arginine", "before", 0.13, 66, 5.3, 59, 22),
    ("arginine", "after", 0.23, 145, 6.4, 184, 21),
    ("citrulline", "before", 0.13, 67, 5.3, 64, 21),
    ("citrulline", "after", 0.41, 186, 36.3, 257, 156),
]
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("supplement", "time", "NO_umol_kg_h", "arginine_flux_umol_kg_h",
                 "arginine_synthesis_umol_kg_h", "plasma_arginine_uM", "plasma_citrulline_uM",
                 "NO_divided_by_arginine_flux_pct", "synthesis_divided_by_flux_pct"))
for arm, phase, no, flux, synthesis, plasma_arg, plasma_cit in measurements:
    writer.writerow((arm, phase, no, flux, synthesis, plasma_arg, plasma_cit,
                     round(100 * no / flux, 3), round(100 * synthesis / flux, 2)))

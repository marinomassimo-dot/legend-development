"""Reproduce unit conversions and the separate culture decay scenario."""
import csv
import sys

MOLAR_MASS = 176.124  # g/mol, L-ascorbic acid
out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
out.writerow(("source", "group_or_time", "measurement", "value", "unit"))
csf = [
    ("3975061", "normal CSF laboratory values", 30.1),
    ("3975061", "premature infants subgroup", 118.2),
    ("3975061", "school-age subgroup", 28.3),
    ("1794949", "term day one", 3.8 * 10),
    ("1794949", "preterm day one", 5.2 * 10),
    ("1794949", "later neonatal estimates", 2.9 * 10),
]
for source, group, mg_per_liter in csf:
    out.writerow((source, group, "reported_CSF_mean", round(1000 * mg_per_liter / MOLAR_MASS, 1), "µM"))
out.writerow(("29423921", "nominal 150 µM L-ascorbic acid", "initial_nominal", round(0.150 * MOLAR_MASS, 2), "mg/L"))
for hour, percent_loss in ((6, 87.0), (8, 93.7), (24, 98.6)):
    out.writerow(("36418489", f"{hour} h from 200 µM nominal bolus in N2B27",
                  "scaled_initial_by_measured_retention", round(200 * (1 - percent_loss / 100), 2), "µM"))

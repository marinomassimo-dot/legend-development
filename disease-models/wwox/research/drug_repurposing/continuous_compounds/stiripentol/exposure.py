"""Reproduce the distinct comparisons in the FDA 2018 review, pp. 8, 14 and 15."""
import csv
import sys

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("measure", "comparison", "reference", "STP", "STP_over_reference"))
entries = (
    ("clobazam_mg_L", "between_arms", 0.20, 0.31),
    ("norclobazam_mg_L", "between_arms", 0.95, 4.32),
    ("clobazam_dose_normalized", "between_arms", 0.45, 0.84),
    ("norclobazam_dose_normalized", "between_arms", 2.1, 11.6),
    ("clobazam_dose_normalized", "within_STP_arm_periods", 0.39, 0.84),
    ("norclobazam_dose_normalized", "within_STP_arm_periods", 3.6, 11.6),
    ("norclobazam_over_clobazam_mass_ratio_of_group_values", "between_arms",
     0.95/0.20, 4.32/0.31),
)
for measure, comparison, baseline, treated in entries:
    writer.writerow((measure, comparison, f"{baseline:.4f}", f"{treated:.4f}", f"{treated/baseline:.4f}"))

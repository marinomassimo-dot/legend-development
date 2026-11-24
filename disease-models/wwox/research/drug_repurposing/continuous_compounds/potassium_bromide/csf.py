"""Recalculate the Table 7 CSF site comparison (Hunter et al., 1954)."""
import csv
import sys

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(["table7_case", "lumbar_mg_dL", "ventricular_mg_dL", "lumbar_mM",
                 "ventricular_mM", "ventricular_over_lumbar"])
for case, lumbar, ventricular in [
    ("36X", 5.4, 2.7), ("39X", 12.1, 7.1), ("34X", 4.5, 2.8),
    ("65X", 12.1, 6.9), ("50X", 11.0, 7.8), ("88X", 23.5, 10.5)
]:
    # Reported mass is bromide ion. One mmol is 79.904 mg.
    writer.writerow([case, lumbar, ventricular, f"{lumbar * 10 / 79.904:.3f}",
                     f"{ventricular * 10 / 79.904:.3f}", f"{ventricular / lumbar:.3f}"])

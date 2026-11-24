"""Concentrations in distinct systems; do not infer a CNS target-occupancy margin."""
import csv
import sys

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("study", "observation", "unit", "value"))
for sample, fraction in (("S1", 0.021), ("S2", 0.021), ("S3", 0.020)):
    writer.writerow((28082409, f"unbound_DHA_{sample}", "pM", round(1.6 * fraction * 1000, 1)))
writer.writerow((8938727, "Kv1.2_nominal_Kd_at_+40mV", "nM", 1800))
writer.writerow((8938727, "Kv3.1a_nominal_Kd_at_+40mV", "nM", 690))
writer.writerow((28355511, "physiological_BPD_imputed_difference", "percentage_points", round(49.1 - 43.9, 1)))
writer.writerow((36300974, "assessed_among_eligible_survivors", "percent", round(100 * 480 / 656, 1)))

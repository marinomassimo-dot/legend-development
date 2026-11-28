"""Reproduce the charging bounds and nominal deprivation conditions."""
import csv
import sys


writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("comparison", "quantity", "value", "unit"))
for percentage in (0, 0.5, 1, 5, 100):
    nominal_reference = 100
    writer.writerow(("Kok_Fig_1c", f"{percentage:g}_percent_of_plasma_reference",
                     f"{nominal_reference * percentage / 100:.3f}", "micromolar_nominal"))
for label, charging_km in (("bacterial_expression", 2.97), ("baculovirus_expression", 7.5)):
    writer.writerow(("Chen_Table_3_vs_Table_2", label, f"{45.6 / charging_km:.4f}",
                     "activation_Km_over_aminoacylation_Km"))

# Sensitivity scenarios only. x is control free intracellular leucine divided
# by the apparent charging Km. r is hypothetical KO/control maximal rate.
for ratio in (0.5, 0.7, 0.9):
    for x in (0.25, 1.0, 4.0):
        label = f"scenario_r_{ratio:g}_x_{x:g}"
        control_baseline_rate = x / (1 + x)
        ko_double_rate = ratio * 2 * x / (1 + 2 * x)
        gap = ratio - control_baseline_rate
        match = 1 / ((1 + x) * gap) if gap > 0 else None
        writer.writerow((label, "ko_charging_at_double_leucine",
                         f"{ko_double_rate / control_baseline_rate:.4f}",
                         "fraction_of_WT_baseline_rate"))
        writer.writerow((label, "ko_charging_at_unlimited_leucine",
                         f"{ratio / control_baseline_rate:.4f}",
                         "fraction_of_WT_baseline_rate"))
        writer.writerow((label, "intracellular_leucine_to_match_WT_baseline",
                         "no_finite_match" if match is None else f"{match:.4f}",
                         "multiple_of_WT_baseline_leucine"))

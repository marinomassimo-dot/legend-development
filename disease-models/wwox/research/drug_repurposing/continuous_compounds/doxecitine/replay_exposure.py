"""Reproduce the concentration-scale check, keeping compartments distinct."""
import csv
import sys


def main():
    molar_mass = 227.22
    cmax_total = 12 / molar_mass
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("comparison", "value", "unit", "evidence"))
    rows = (
        ("TK2_label_steady_state_plasma_Cmax", cmax_total, "uM",
         "model_estimated_geometric_mean_total_baseline_unadjusted_n18"),
        ("TK2_label_steady_state_plasma_AUC_0_24", 108 / molar_mass, "uM_h",
         "model_estimated_geometric_mean_total_baseline_unadjusted_n18"),
        ("fibroblast_lowest_tested_nominal_dC_over_plasma_Cmax", 1 / cmax_total, "fold",
         "scale_check_not_free_CNS"),
        ("fibroblast_multi_nucleoside_nominal_dC_over_plasma_Cmax", 50 / cmax_total, "fold",
         "scale_check_not_free_CNS"),
    )
    for comparison, value, unit, evidence in rows:
        writer.writerow((comparison, f"{value:.5f}", unit, evidence))


if __name__ == "__main__":
    main()

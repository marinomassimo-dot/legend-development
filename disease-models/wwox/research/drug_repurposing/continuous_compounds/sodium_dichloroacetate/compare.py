"""Reproduce endpoint and exposure sensitivity from the cited group summaries."""
import csv
from math import comb
import sys


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("comparison", "quantity", "value"))
    placebo_above, dca_above, size = 18, 11, 34
    writer.writerow(("threshold_lactate", "DCA_minus_placebo_pct_points",
                     f"{100 * (dca_above - placebo_above) / size:.3f}"))
    minimum_overlap = max(0, placebo_above + dca_above - size)
    maximum_overlap = min(placebo_above, dca_above)
    for overlap in range(minimum_overlap, maximum_overlap + 1):
        placebo_only = placebo_above - overlap
        dca_only = dca_above - overlap
        discordant = placebo_only + dca_only
        exact_p = min(1, 2 * sum(comb(discordant, k) for k in range(dca_only + 1))
                      / 2**discordant)
        writer.writerow(("threshold_lactate", f"exact_p_if_both_above_{overlap}", f"{exact_p:.6f}"))
    writer.writerow(("plasma_PK", "six_month_AUC_divided_by_first_dose_AUC", f"{340 / 83:.3f}"))
    for basis, mass in (("unlabelled_acid_equivalent", 128.94), ("sodium_salt_equivalent", 150.92)):
        for label, peak in (("first_dose", 23), ("six_month", 35)):
            peak_mm = peak / mass
            writer.writerow(("plasma_PK", f"{basis}_{label}_mean_total_Cmax_mM", f"{peak_mm:.4f}"))
            for context, ic50 in (("core_free", .29), ("core_bound", .48)):
                writer.writerow(("plasma_PK", f"{basis}_{label}_Cmax_divided_by_{context}_IC50",
                                 f"{peak_mm / ic50:.4f}"))


if __name__ == "__main__":
    main()

"""Reproduce the sultiame electrophysiology, pediatric EEG and fibroblast comparisons."""
import csv
from math import comb
from statistics import mean, median
import sys


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("comparison", "quantity", "value"))
    for mass in (1, 10):
        writer.writerow(("Madeja_bath", f"{mass}_ug_per_mL_to_uM", f"{1000 * mass / 290.4:.3f}"))
    writer.writerow(("LHON_exposure", "150_uM_divided_by_adult_max_observed_total_trough",
                     f"{150 / (1000 * 9.37 / 290.4):.3f}"))

    # Reinert et al. Fig. 2a–c. Last displayed FCCP point (around 65 min),
    # before antimycin/rotenone, read from the plot and rounded to pmol/min.
    for line, vehicle, drug in (("healthy", 35, 35), ("MT_ND1", 37, 20), ("MT_ND6", 27, 16)):
        writer.writerow(("LHON_uncoupled_OCR", f"{line}_drug_divided_by_vehicle",
                         f"{drug / vehicle:.3f}"))
        writer.writerow(("LHON_uncoupled_OCR", f"{line}_ratio_min_with_one_unit_read_error",
                         f"{(drug - 1) / (vehicle + 1):.3f}"))
        writer.writerow(("LHON_uncoupled_OCR", f"{line}_ratio_max_with_one_unit_read_error",
                         f"{(drug + 1) / (vehicle - 1):.3f}"))

    # Laliberté et al. Table 1, all eight complete before/after SWI measurements.
    pairs = [(65.3, 21.0), (90.2, 0), (99.5, 82.8), (56.8, 60.5),
             (99.3, 99.8), (93.2, 47.5), (60.7, 0), (84.3, 48.8)]
    deltas = [after - before for before, after in pairs]
    omissions = [mean(deltas[:index] + deltas[index + 1:]) for index in range(len(deltas))]
    results = {"mean_change_pp": mean(deltas), "median_change_pp": median(deltas),
               "leave_one_out_min_pp": min(omissions), "leave_one_out_max_pp": max(omissions)}
    for name, value in results.items():
        writer.writerow(("pediatric_sleep_SWI", name, f"{value:.3f}"))
    decreases = sum(delta < 0 for delta in deltas)
    writer.writerow(("pediatric_sleep_SWI", "decrease_count", decreases))
    tail_count = min(decreases, len(deltas) - decreases)
    exact_p = min(1, 2 * sum(comb(len(deltas), k) for k in range(tail_count + 1)) / 2**len(deltas))
    writer.writerow(("pediatric_sleep_SWI", "exact_sign_test_p", f"{exact_p:.6f}"))


if __name__ == "__main__":
    main()

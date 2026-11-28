"""Replay aggregate source arithmetic and the synthetic circuit counterexample."""

import csv
import sys


def main():
    # Yang et al. 2014, Fig. 3A and Results, inward peak magnitudes (nA).
    fixed_input_peak_ratio = 2.30 / 0.89

    # Bernini et al. 2022, Tables 2–4 and Results, hypertonic lactate minus saline.
    pressure_difference = -13 - (-12)
    chloride_difference = -1 - 4
    lactate_difference_of_medians = 4.0 - 3.2

    # Wolahan et al. 2018, Results, modeled arteriovenous differences (mmol/L).
    modeled_gradient_shift = 0.090 - (-0.078)

    # Only the scale of the gain is anchored to Yang. This uses peak as an
    # illustrative multiplier for charge. Other factors are not biological estimates.
    input_fraction = 0.70
    neutral_nmda_share = (1 / input_fraction - 1) / (fixed_input_peak_ratio - 1)

    rows = [
        ("source_arithmetic", "fixed_input_peak_ratio", "ratio", fixed_input_peak_ratio),
        ("source_arithmetic", "pressure_change_median_lactate_minus_saline", "mmHg", pressure_difference),
        ("source_arithmetic", "chloride_change_mean_lactate_minus_saline", "mmol/L", chloride_difference),
        ("source_arithmetic", "dialysate_lactate_difference_of_visit_medians", "mmol/L", lactate_difference_of_medians),
        ("source_arithmetic", "modeled_arteriovenous_gradient_shift", "mmol/L", modeled_gradient_shift),
        ("illustration", "neutral_baseline_nmda_share", "fraction", neutral_nmda_share),
    ]
    for nmda_share in (0.20, 0.40):
        charge_fraction = input_fraction * (1 - nmda_share + nmda_share * fixed_input_peak_ratio)
        rows.append(("illustration", f"charge_at_nmda_share_{nmda_share:.2f}", "fraction", charge_fraction))

    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("kind", "comparison", "units", "value"))
    for kind, comparison, units, value in rows:
        writer.writerow((kind, comparison, units, f"{value:.6f}"))


if __name__ == "__main__":
    main()

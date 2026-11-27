"""Replay same-assay response ratios and an illustrative reserve-versus-mixture test."""

import csv
import sys


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("comparison", "scope", "unit", "value"))

    def emit(comparison, scope, unit, value):
        writer.writerow((comparison, scope, unit, f"{value:.6f}"))

    # Dravid et al., Table 1 and Results accompanying Fig. 7.
    efficacy_b, efficacy_c = 0.65, 1.90
    emit("maximal_dcs_relative_efficacy_ratio", "GluN2C_over_GluN2B", "ratio", efficacy_c / efficacy_b)
    emit("single_channel_mean_probability_ratio", "GluN2C", "ratio", 0.029 / 0.018)

    # Lench et al., group means accompanying Fig. 4.
    emit("ratio_of_group_mean_decay", "entorhinal_30uM", "fraction", 417.4 / 593.8)
    emit("ratio_of_group_mean_peak", "entorhinal_30uM", "fraction", 160.6 / 190.9)

    # ClinicalTrials.gov NCT01086475, registered week-11 outcome means.
    emit("difference_of_registered_mean_change", "ASD_week11", "SRS_points", -13.39 - (-17))

    # Effective interpolation. Replacement fractions and reference-current weights are synthetic.
    for scenario, baseline, c_share in (
        ("low_baseline_B_only", 0.40, 0.00),
        ("high_baseline_B_only", 0.90, 0.00),
        ("high_baseline_10pct_C", 0.90, 0.10),
        ("high_baseline_30pct_C", 0.90, 0.30),
    ):
        replacement_current = (1 - c_share) * efficacy_b + c_share * efficacy_c
        emit("synthetic_current_change", scenario, "reference_current_fraction",
             replacement_current - baseline)

    baseline = 0.90
    for scenario, b_replacement, c_replacement in (("equal", 1.0, 1.0), ("unequal", 0.50, 0.80)):
        b_loss = b_replacement * (baseline - efficacy_b)
        c_gain = c_replacement * (efficacy_c - baseline)
        emit("synthetic_neutral_C_share", scenario, "reference_current_fraction", b_loss / (b_loss + c_gain))


if __name__ == "__main__":
    main()

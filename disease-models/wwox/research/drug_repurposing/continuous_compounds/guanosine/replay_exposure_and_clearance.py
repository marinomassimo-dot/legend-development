"""Replay aggregate source comparisons and a one-compartment clearance counterexample."""

import argparse
import csv
from math import log, sqrt
from pathlib import Path


def write_table(directory, filename, header, rows):
    with (directory / filename).open("w", newline="") as output:
        writer = csv.writer(output, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def exposure_rows():
    # 2-week SD and 6-week SEM come from distinct studies and remain separate.
    exposures = (
        ("Vinade_Wistar_two_weeks", 0.46, 0.40, 1.05, 0.60, "SD", "20_reported", "15558762 Results and Fig. 4"),
        ("Ganzella_sham_six_weeks", 0.10, 0.01, 0.10, 0.02, "SEM", 10, "22167652 Table 1a"),
        ("Ganzella_2VO_six_weeks", 0.10, 0.10, 0.12, 0.03, "SEM", 10, "22167652 Table 1a"),
    )
    for name, control, control_error, treated, treated_error, error, sample_size, source in exposures:
        yield (
            name, control, control_error, treated, treated_error, error, sample_size,
            f"{treated / control:.3f}", f"{treated:.3f}", f"{treated / 2.47:.3f}",
            f"{treated / 10:.3f}", f"{treated / 100:.4f}", source,
        )


def scenario_rows():
    # From dG/dt = -Vmax * G / (Km + G), integrated after a single pulse.
    # Vmax = 1 is an arbitrary reference. +23% is an illustrative lift from PMID 16133942.
    capacity_ratio = 1.23
    for km in (5, 20, 50):
        for initial in (1, 10, 100):
            control_half_time = initial / 2 + km * log(2)
            control_auc = initial * (km + initial / 2)
            increased_capacity_auc = control_auc / capacity_ratio
            # Positive root of g*(Km + g/2) = increased_capacity_auc.
            reduced_initial = 2 * increased_capacity_auc / (km + sqrt(km**2 + 2 * increased_capacity_auc))
            reduced_release_auc = reduced_initial * (km + reduced_initial / 2)
            assert abs(reduced_release_auc - increased_capacity_auc) < 1e-9
            yield (
                km, initial, f"{reduced_initial / initial:.4f}",
                f"{reduced_release_auc / control_auc:.4f}",
                f"{(reduced_initial / 2 + km * log(2)) / control_half_time:.4f}",
                "1.0000", f"{increased_capacity_auc / control_auc:.4f}", f"{1 / capacity_ratio:.4f}",
            )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    write_table(
        args.output, "csf_to_nominal_assay.tsv",
        ("study_arm", "control_CSF_uM", "control_error_uM", "treated_CSF_uM", "treated_error_uM", "error_type",
         "n_per_arm_reported", "treated_over_control", "treated_over_1uM", "treated_over_2p47uM",
         "treated_over_10uM", "treated_over_100uM", "source"),
        exposure_rows(),
    )
    write_table(
        args.output, "release_clearance_scenarios.tsv",
        ("illustrative_Km_uM", "control_peak_uM", "reduced_release_peak_ratio", "reduced_release_AUC_ratio",
         "reduced_release_evoked_half_time_ratio", "reduced_release_fixed_input_half_time_ratio",
         "higher_capacity_AUC_ratio", "higher_capacity_fixed_input_half_time_ratio"),
        scenario_rows(),
    )


if __name__ == "__main__":
    main()

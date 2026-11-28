"""Replay denominators and exploratory missing-data sensitivity for bexarotene."""
import argparse
import csv
from pathlib import Path


def compare(x):
    for metric in ("hypothyroid", "hypertriglyceridemia", "discontinued_for_ae"):
        active = x[f"trial_drug_{metric}"] / x["trial_drug_exposed"]
        placebo = x[f"trial_placebo_{metric}"] / x["trial_placebo_exposed"]
        yield f"trial_{metric}_exposed_risk_difference", 100 * (active - placebo), "percentage points"
    yield "primary_mtr_design_target_minus_ci_upper", x["trial_mtr_target"] - x["trial_mtr_upper_ci"], "percentage units"
    for prefix in ("followup", "followup_delayed"):
        active = x[f"{prefix}_drug_improved"] / x[f"{prefix}_drug_recordable"]
        placebo = x[f"{prefix}_placebo_improved"] / x[f"{prefix}_placebo_recordable"]
        yield f"{prefix}_observed_eye_risk_difference", 100 * (active - placebo), "percentage points, post hoc"
    total_eyes_per_arm = x["trial_randomized_per_arm"] * 2
    active_missing = total_eyes_per_arm - x["followup_drug_recordable"]
    placebo_missing = total_eyes_per_arm - x["followup_placebo_recordable"]
    active = x["followup_drug_improved"]
    placebo = x["followup_placebo_improved"]
    yield "followup_no_assumption_eye_risk_difference_lower", 100 * (active - placebo - placebo_missing) / total_eyes_per_arm, "percentage points, hypothetical"
    yield "followup_no_assumption_eye_risk_difference_upper", 100 * (active + active_missing - placebo) / total_eyes_per_arm, "percentage points, hypothetical"
    yield "followup_missing_placebo_responses_to_tie_if_no_missing_active", active - placebo, "eyes, hypothetical"
    yield "healthy_csf_limit_over_average_plasma_peak", 100 * x["healthy_csf_limit"] / x["healthy_plasma_peak"], "percent, scale comparison"
    yield "healthy_quantifiable_subset_csf_fraction_of_plasma", 100 / x["healthy_csf_plasma_ratio_inverse"], "percent, author-estimated ratio inverted"
    yield "qki_myelinated_fraction_treatment_ratio", 1 + x["qki_myelinated_gain"] / 100, "ratio to untreated Qki iCKO"
    yield "qki_myelin_lipid_stain_treatment_ratio", 1 + x["qki_myelin_fluorescence_gain"] / 100, "ratio to untreated Qki iCKO"


def main(source, output):
    with source.open() as handle:
        x = {row["key"]: float(row["value"]) for row in csv.DictReader(handle, delimiter="\t")}
    with output.open("w") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(("comparison", "value", "unit"))
        writer.writerows((label, f"{value:.7g}", unit) for label, value, unit in compare(x))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    main(args.source, args.output)

"""Replay aggregate seizure, metabolite, PET and receptor selectivity contrasts."""
import argparse
import csv
from pathlib import Path


def occupancy(free_concentration, ki):
    return free_concentration / (free_concentration + ki)


def main(inputs, output):
    with inputs.open() as handle:
        x = {r["key"]: float(r["value"]) for r in csv.DictReader(handle, delimiter="\t")}

    drug_risk = x["hyperoxia_drug_events"] / x["hyperoxia_n"]
    control_risk = x["hyperoxia_control_events"] / x["hyperoxia_n"]
    a2a, a2b, a1_floor = (x[k] for k in ("a2a_ki", "a2b_ki", "a1_ki_floor"))
    # Algebraic scenarios for a single site at equilibrium without endogenous ligand.
    min_for_80_a2a = a2a * 0.8 / 0.2
    max_for_10_a2b = a2b * 0.1 / 0.9
    gaba_gap = x["gaba_normal"] - x["gaba_control"]

    results = [
        ("hyperoxia_control_30min_behavioral_risk", control_risk, "fraction"),
        ("hyperoxia_drug_30min_behavioral_risk", drug_risk, "fraction"),
        ("hyperoxia_30min_risk_difference_drug_minus_control", drug_risk - control_risk, "fraction"),
        ("hyperoxia_30min_risk_difference_one_reclassification_toward_null", drug_risk + 1 / x["hyperoxia_n"] - control_risk, "fraction"),
        ("cortical_GABA_gap_recovered", (x["gaba_drug"] - x["gaba_control"]) / gaba_gap, "fraction"),
        ("cortical_glutamate_treated_relative_to_exposed_control", x["glu_drug"] / x["glu_control"], "ratio"),
        ("cortical_Glu_GABA_reported_mean_ratio_relative_to_control", x["ratio_drug"] / x["ratio_control"], "ratio"),
        ("cortical_Glu_GABA_reported_mean_ratio_relative_to_normal", x["ratio_drug"] / x["ratio_normal"], "ratio"),
        ("A2B_to_A2A_Ki", a2b / a2a, "ratio"),
        ("A1_to_A2A_Ki_lower_bound", a1_floor / a2a, "ratio"),
        ("minimum_free_for_80pct_A2A_scenario", min_for_80_a2a, "nM"),
        ("maximum_free_for_10pct_A2B_scenario", max_for_10_a2b, "nM"),
        ("A2B_occupancy_at_80pct_A2A_scenario", occupancy(min_for_80_a2a, a2b), "fraction"),
        ("A1_occupancy_upper_bound_at_80pct_A2A_scenario", occupancy(min_for_80_a2a, a1_floor), "fraction"),
        ("A2A_occupancy_at_10pct_A2B_scenario", occupancy(max_for_10_a2b, a2a), "fraction"),
        ("striatal_PET_long_minus_single_lower_arm", x["long_pet_lower"] - x["acute_pet_lower"], "percentage points"),
        ("striatal_PET_long_minus_single_higher_arm", x["long_pet_higher"] - x["acute_pet_higher"], "percentage points"),
    ]
    with output.open("w") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["comparison", "value", "unit"])
        writer.writerows((name, f"{value:.7g}", unit) for name, value, unit in results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    main(args.inputs, args.output)

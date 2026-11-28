"""Replay Figure 3 extracellular AUCs and prespecified exposure comparisons."""
import argparse
import csv
from pathlib import Path


def trapezoids(times, values):
    return sum((t1 - t0) * (v0 + v1) / 2
               for t0, t1, v0, v1 in zip(times, times[1:], values, values[1:]))


def main(inputs, points, output):
    with inputs.open() as handle:
        x = {r["key"]: float(r["value"]) for r in csv.DictReader(handle, delimiter="\t")}
    with points.open() as handle:
        figure = list(csv.DictReader(handle, delimiter="\t"))

    values = []
    for probe, panel in (("phenytoin", "3A"), ("carbamazepine", "3B")):
        rows = [r for r in figure if r["panel"] == panel]
        times = [int(r["minute"]) for r in rows]
        axis = x[f"{probe}_axis_bottom"]
        per_px = x[f"{probe}_axis_height"] / (axis - x[f"{probe}_axis_top"])
        groups = ("control", "kindled", "verapamil")
        auc_by_group = {
            g: trapezoids(times, [(axis - int(r[f"{g}_y"])) * per_px for r in rows])
            for g in groups
        }
        for group, auc in auc_by_group.items():
            values.append((f"{probe}_{group}_ecf_auc_15_to_180", auc, "µg·min/mL"))
        treated, kindled = auc_by_group["verapamil"], auc_by_group["kindled"]
        # Move all treated and kindled marker centers by 2 px in opposing directions.
        margin = 2 * (times[-1] - times[0]) * per_px
        values.extend([
            (f"{probe}_ecf_auc_treated_vs_kindled", treated / kindled, "ratio"),
            (f"{probe}_ecf_ratio_lower_digitization", (treated - margin) / (kindled + margin), "ratio"),
            (f"{probe}_ecf_ratio_upper_digitization", (treated + margin) / (kindled - margin), "ratio"),
            (f"{probe}_serum_exposure_change_explaining_ecf_at_fixed_ratio",
             100 * (treated / kindled - 1), "percent hypothetical"),
        ])

    total = (x["adult_r_peak"] + x["adult_s_peak"]) / x["parent_mass"]
    free = total * x["parent_unbound_fraction"]
    dravet_ratio = x["dravet_active_count"] / x["dravet_baseline_count"]
    values.extend([
        ("tracer_baseline_abcb1_loss_vs_wt", x["tracer_abcb1_ko"] / x["tracer_wt"], "ratio"),
        ("tracer_baseline_additional_abcg2_loss_vs_abcb1_only",
         x["tracer_abcb1_abcg2_ko"] / x["tracer_abcb1_ko"], "ratio"),
        ("human_k1_resistant_minus_healthy_lower", x["adult_resistant_k1_low"] - x["adult_healthy_k1_low"], "percentage points"),
        ("human_k1_resistant_minus_healthy_higher", x["adult_resistant_k1_high"] - x["adult_healthy_k1_high"], "percentage points"),
        ("sum_of_mean_parent_peak_concentrations", total, "µM"),
        ("parent_free_peak_scenario", free, "µM"),
        ("parent_digoxin_ic50_over_free_plasma_scenario", x["parent_digoxin_ic50"] / free, "ratio"),
        ("parent_digoxin_ic50_over_total_plasma_upper_scenario", x["parent_digoxin_ic50"] / total, "ratio"),
        ("parent_to_norverapamil_digoxin_assay_ic50", x["parent_digoxin_ic50"] / x["nor_digoxin_ic50"], "ratio"),
        ("cav_pulse1_ic50_over_pulse2", x["cav_pulse1_ic50"] / x["cav_pulse2_ic50"], "ratio"),
        ("conditioned_cav_ic50_over_free_plasma_scenario", x["cav_conditioned_ic50"] / free, "ratio"),
        ("adult_randomized_fraction_completing", x["adult_completed"] / x["adult_randomized"], "fraction"),
        ("dravet_raw_count_ratio", dravet_ratio, "ratio"),
        ("dravet_rate_ratio_if_baseline_is_eight_weeks_and_active_is_four",
         dravet_ratio * x["dravet_baseline_weeks"] / x["dravet_active_weeks"], "ratio scenario"),
    ])
    with output.open("w") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["comparison", "value", "unit"])
        writer.writerows((label, f"{value:.7g}", unit) for label, value, unit in values)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", type=Path)
    parser.add_argument("figure_points", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    main(args.inputs, args.figure_points, args.output)

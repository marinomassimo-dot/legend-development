"""Recompute within-mouse EEG contrasts and independently sourced scale checks."""
import argparse
import csv
from pathlib import Path
from statistics import mean, median


def read_rows(path):
    with path.open() as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def eeg_comparisons(mice):
    phases = ("pre", "during", "post")
    pre, active, post = ([int(mouse[f"{phase}_total"]) / 3 for mouse in mice] for phase in phases)
    midpoint = [mean((before, after)) for before, after in zip(pre, post)]
    mouse_reductions = [100 * (1 - during / before) for before, during in zip(pre, active)]
    centered_reductions = [100 * (1 - during / reference)
                           for reference, during in zip(midpoint, active)]
    omission_reductions = [
        100 * (1 - mean(active[:index] + active[index + 1:]) /
               mean(pre[:index] + pre[index + 1:]))
        for index in range(len(mice))
    ]
    for label, phase in zip(phases, (pre, active, post)):
        yield f"eeg_{label}_mean", mean(phase), "events per recorded 8 h"
    yield "eeg_during_vs_pre_group_reduction", 100 * (1 - mean(active) / mean(pre)), "percent"
    yield "eeg_during_vs_pre_median_within_mouse_reduction", median(mouse_reductions), "percent"
    yield "eeg_during_below_pre_mice", sum(value > 0 for value in mouse_reductions), "mice"
    yield "eeg_omit_one_mouse_group_reduction_min", min(omission_reductions), "percent"
    yield "eeg_omit_one_mouse_group_reduction_max", max(omission_reductions), "percent"
    yield "eeg_pre_post_midpoint_median_within_mouse_reduction", median(centered_reductions), "percent"
    yield "eeg_during_below_pre_post_midpoint_mice", sum(value > 0 for value in centered_reductions), "mice"
    yield "eeg_post_above_during_mice", sum(after > during for during, after in zip(active, post)), "mice"
    for day in range(4, 7):
        below = sum(int(mouse[f"day{day}_below_pre_mean"]) for mouse in mice)
        yield f"eeg_day{day}_below_own_pre_mean_mice", below, "mice"


def other_comparisons(x):
    for genotype in ("wt", "scn1a"):
        decrease = x[f"{genotype}_20ma_vehicle_events"] - x[f"{genotype}_20ma_treated_events"]
        yield f"{genotype}_6hz_20ma_behavioral_event_reduction", 100 * decrease / x["n_20ma"], "percentage points"
    yield "flurothyl_treated_death_fraction", x["flurothyl_treated_deaths"] / x["flurothyl_treated_n"], "fraction"
    adult_peak = x["pk_total_peak"] / x["parent_mass"]
    yield "adult_tablet_total_plasma_peak", 1000 * adult_peak, "nM"
    yield "rat_nmda_nominal_ic50_over_adult_total_plasma_peak", x["nmda_current_half"] / adult_peak, "cross-study ratio"
    yield "rat_nmda_nominal_ic50_over_mouse_local_kindling_solution", 1000 * x["nmda_current_half"] / x["local_dca1"], "cross-assay ratio"
    yield "sponsor_interim_maintenance_completion", x["interim_maintenance_complete"] / x["interim_enrolled"], "fraction at cutoff"
    responder_estimate = round(x["interim_focal_half_percent"] * x["interim_focal_n"] / 100)
    yield "sponsor_interim_focal_responders_reconstructed", responder_estimate, "adults, from rounded percent"


def main(directory, output):
    mice = read_rows(directory / "figure3d_by_mouse.tsv")
    x = {row["key"]: float(row["value"]) for row in read_rows(directory / "source_inputs.tsv")}
    with output.open("w") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["comparison", "value", "unit"])
        writer.writerows((label, f"{value:.7g}", unit) for label, value, unit in eeg_comparisons(mice))
        writer.writerows((label, f"{value:.7g}", unit) for label, value, unit in other_comparisons(x))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    main(args.directory, args.output)

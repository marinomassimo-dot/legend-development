#!/usr/bin/env python3
"""Replay published aggregate comparisons and explicitly labeled sensitivity scenarios."""
import csv
import math
from pathlib import Path
import sys


def main():
    with Path(__file__).with_name("source_inputs.tsv").open(encoding="utf-8") as source:
        values = {row["key"]: float(row["value"]) for row in csv.DictReader(source, delimiter="\t")}

    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("comparison", "value", "unit"))

    def report(name, value, unit):
        writer.writerow((name, f"{value:.9g}", unit))

    def unbound(total):
        return total * 1000 * values["plasma_free_fraction"] / values["parent_molecular_mass"]

    median = unbound(values["peak_total_plasma_median"])
    maximum = unbound(values["peak_total_plasma_high"])
    report("plasma_total_median", median / values["plasma_free_fraction"], "nM")
    report("plasma_unbound_low", unbound(values["peak_total_plasma_low"]), "nM")
    report("plasma_unbound_median", median, "nM")
    report("plasma_unbound_high", maximum, "nM")
    ki = 1000 * values["human_tspo_ki"]
    for enrichment in (1, 10, 100):
        local = enrichment * median
        report(f"hypothetical_TSPO_occupancy_at_{enrichment}x", 100 * local / (local + ki), "%")
    report("enrichment_needed_for_10pct_at_median_plasma", ki / (9 * median), "fold")
    report("enrichment_needed_for_10pct_at_max_plasma_low_Ki", 1000 * values["human_tspo_ki_low"] / (9 * maximum), "fold")
    report("enrichment_needed_for_10pct_at_median_plasma_high_Ki", 1000 * values["human_tspo_ki_high"] / (9 * median), "fold")
    for name in ("fast_gaba_low_nominal", "fast_gaba_peak_nominal", "frog_homogenate_nominal", "frog_explant_timecourse_nominal"):
        report(f"{name}_over_median_unbound_plasma", 1000 * values[name] / median, "fold")

    report("plasma_allo_mean_difference_etifoxine_minus_placebo",
           values["human_plasma_allo_etifoxine_mean"] - values["human_plasma_allo_placebo_mean"], "ng/mL")

    treated = values["seizures_etifoxine"]
    placebo = values["seizures_placebo"]
    treated_rate = treated / values["followup_etifoxine"]
    placebo_rate = placebo / values["followup_placebo"]
    rate_ratio = treated_rate / placebo_rate
    report("seizure_rate_etifoxine", treated_rate, "events/person-month")
    report("seizure_rate_placebo", placebo_rate, "events/person-month")
    report("crude_seizure_rate_ratio", rate_ratio, "ratio")
    report("crude_relative_seizure_rate_reduction", 100 * (1 - rate_ratio), "%")
    log_ratio = math.log(rate_ratio)
    # A count-only worked example. Recurrent events within participants can be correlated.
    se = math.sqrt(1 / treated + 1 / placebo)
    report("independent_Poisson_count_CI_low", math.exp(log_ratio - 1.96 * se), "ratio")
    report("independent_Poisson_count_CI_high", math.exp(log_ratio + 1.96 * se), "ratio")
    report("independent_Poisson_count_two_sided_p", math.erfc(abs(log_ratio) / (se * math.sqrt(2))), "p")


if __name__ == "__main__":
    main()

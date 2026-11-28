"""Reproduce the amantadine exposure comparisons and EEG denominator checks."""

import csv
from pathlib import Path
import sys


def main():
    with Path(__file__).with_name("inputs.tsv").open(newline="") as stream:
        inputs = {row["id"]: row for row in csv.DictReader(stream, delimiter="\t")}

    def get(name, unit):
        row = inputs[name]
        if row["unit"] != unit:
            raise ValueError(f"{name}: expected {unit}, found {row['unit']}")
        return float(row["value"])

    reference = get("pediatric_avg_reference", "mg/L")
    base_reference = 1000 * reference / get("parent_mw", "g/mol")
    salt_reference = 1000 * reference / get("hcl_mw", "g/mol")
    free_fraction = 1 - get("plasma_binding", "percent") / 100
    amantadine_0mg = get("amantadine_ic50_0mg", "umol/L")
    amantadine_1mg = get("amantadine_ic50_1mg", "umol/L")
    memantine_0mg = get("memantine_ic50_0mg", "umol/L")
    memantine_1mg = get("memantine_ic50_1mg", "umol/L")
    swas = get("swas_n", "count")
    improved = get("swas_pattern_improved", "count")
    absent = get("swas_none_explicit", "count")
    residual = get("swas_residual_among_improved", "count")
    unchanged = get("swas_unchanged", "count")
    if improved + unchanged != swas or absent + residual != improved:
        raise ValueError("SWAS groups do not reconcile")

    nrem_drop_bound = get("nrem_baseline_lower_bound", "percent") - get("nrem_followup", "percent")
    results = (
        ("pediatric_average_reference_parent_basis", base_reference, "umol/L"),
        ("pediatric_average_reference_if_HCl_basis", salt_reference, "umol/L"),
        ("conditional_free_plasma_parent_basis", base_reference * free_fraction, "umol/L"),
        ("conditional_free_plasma_if_HCl_basis", salt_reference * free_fraction, "umol/L"),
        ("amantadine_Mg_potency_shift", amantadine_1mg / amantadine_0mg, "ratio"),
        ("memantine_Mg_potency_shift", memantine_1mg / memantine_0mg, "ratio"),
        ("amantadine_over_memantine_1mM_Mg", amantadine_1mg / memantine_1mg, "ratio"),
        ("amantadine_IC50_over_pediatric_total_reference", amantadine_1mg / base_reference, "ratio"),
        ("amantadine_IC50_over_conditional_free_reference", amantadine_1mg / (base_reference * free_fraction), "ratio"),
        ("amantadine_IC50_over_high_rat_dialysate", amantadine_1mg / get("rat_striatal_ecf_high", "umol/L"), "ratio"),
        ("amantadine_IC50_over_low_rat_dialysate", amantadine_1mg / get("rat_striatal_ecf_low", "umol/L"), "ratio"),
        ("rat_nicotinic_IC50_over_conditional_free_reference", get("rat_nicotinic_ic50", "umol/L") / (base_reference * free_fraction), "ratio"),
        ("soto_pattern_improved", 100 * improved / swas, "percent"),
        ("soto_explicit_epileptiform_discharge_absence", 100 * absent / swas, "percent"),
        ("soto_residual_discharges_among_pattern_improved", 100 * residual / improved, "percent"),
        ("illustrative_NREM_drop_strict_lower_bound", nrem_drop_bound, "percentage_points"),
        ("mixture_only_required_total_variation_strict_lower_bound", nrem_drop_bound / 100, "probability"),
        ("wilson_followup_minus_baseline_medians", get("wilson_followup_median", "percent") - get("wilson_baseline_median", "percent"), "percentage_points"),
    )
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("comparison", "value", "unit"))
    writer.writerows((label, f"{value:.3f}", unit) for label, value, unit in results)


if __name__ == "__main__":
    main()

"""Replay descriptive trial contrasts and assay-specific DMGDH rate comparisons."""
import csv
from pathlib import Path
import sys


def main():
    with Path(__file__).with_name("source_inputs.tsv").open(newline="") as source:
        data = {row["key"]: float(row["value"]) for row in csv.DictReader(source, delimiter="\t")}
    output = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    output.writerow(("metric", "value", "unit"))

    def result(label, value, unit):
        output.writerow((label, f"{value:.8g}", unit))

    for acceptor in ("dcpip", "ferrocene"):
        parameters = {}
        for form in ("wt", "h109r"):
            label = f"{form}_{acceptor}"
            km, kcat = (data[f"{label}_{term}"] for term in ("km", "kcat"))
            parameters[form] = (km, kcat)
            result(f"{label}_ratio_of_printed_kcat_to_km", kcat / km, "mM^-1 min^-1")
        wt_km, wt_rate = parameters["wt"]
        variant_km, variant_rate = parameters["h109r"]
        result(f"{acceptor}_wt_over_variant_printed_efficiency",
               data[f"wt_{acceptor}_efficiency_printed"] / data[f"h109r_{acceptor}_efficiency_printed"], "fold")
        result(f"{acceptor}_wt_over_variant_recalculated_efficiency",
               (wt_rate / wt_km) / (variant_rate / variant_km), "fold")
        for substrate in (0.01, 0.1, 1.0):
            wt_turnover = wt_rate * substrate / (substrate + wt_km)
            variant_turnover = variant_rate * substrate / (substrate + variant_km)
            result(f"{acceptor}_wt_over_variant_modeled_turnover_at_{substrate:g}_mM",
                   wt_turnover / variant_turnover, "fold")

    result("child_vo2_mean_change_parent_minus_placebo",
           data["child_vo2_change_parent"] - data["child_vo2_change_placebo"], "mL min^-1 m^-2")
    for condition in ("parent", "placebo"):
        change = data[f"child_intake_during_{condition}"] - data[f"child_intake_before_{condition}"]
        result(f"child_mean_caloric_change_{condition}", change, "kcal m^-2 day^-1")
    result("literal_printed_blood_unit_mass_check",
           data["child_blood_parent_reported_number"] * data["parent_molar_mass"] / 1000,
           "g/L under literal printed mmol/L")
    result("alternative_unit_mass_check_only",
           data["child_blood_parent_reported_number"] * data["parent_molar_mass"] / 1e6,
           "g/L if number were in umol/L")


if __name__ == "__main__":
    main()

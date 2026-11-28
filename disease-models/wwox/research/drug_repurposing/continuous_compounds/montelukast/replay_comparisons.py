"""Replay exposure-scale and optic-nerve group-summary comparisons."""
import csv
from pathlib import Path
import sys


def main():
    with Path(__file__).with_name("source_inputs.tsv").open(newline="") as table:
        values = {row["key"]: float(row["value"]) for row in csv.DictReader(table, delimiter="\t")}

    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("comparison", "value", "unit"))

    def row(key, value, unit):
        writer.writerow((key, f"{value:.8g}", unit))

    for name in ("film_total_csf_min", "film_total_csf_max", "film_total_csf_mean_3h",
                 "film_total_csf_mean_7h", "pd_total_csf_mean", "organoid_nominal_low",
                 "organoid_nominal_high"):
        row(f"{name}_converted", values[name] * 1000 / values["parent_mass"], "nM")

    largest_film_mean = values["film_total_csf_mean_7h"]
    largest_film_mean_nm = largest_film_mean * 1000 / values["parent_mass"]
    for name in ("cyslt1_ltd4_ic50", "gpr17_ltd4_ic50", "opcs_nominal"):
        row(f"{name}_over_film_csf_mean_7h", values[name] / largest_film_mean_nm, "fold")
    for name in ("organoid_nominal_low", "organoid_nominal_high"):
        row(f"{name}_over_film_csf_mean_7h", values[name] / largest_film_mean, "fold")
    row("pd_unpaired_group_means_total_csf_over_total_plasma",
        100 * values["pd_total_csf_mean"] / values["pd_total_plasma_mean"], "percent")
    row("pediatric_12_23m_free_plasma_scenario_ceiling",
        values["pediatric_granules_12_23m_mean_total_cmax"] * values["plasma_fraction_illustrative_ceiling"]
        * 1000 / values["parent_mass"], "nM")
    row("optic_combination_minus_montelukast", values["optic_regrowth_combination"]
        - values["optic_regrowth_montelukast"], "percentage points")
    row("optic_combination_minus_larger_single_arm", values["optic_regrowth_combination"]
        - max(values["optic_regrowth_montelukast"], values["optic_regrowth_plx3397"]), "percentage points")


if __name__ == "__main__":
    main()

"""Convert scoped published exposure anchors without imputing central exposure."""

import csv
import sys
from pathlib import Path


def main():
    inputs = Path(__file__).with_name("exposure_inputs.tsv")
    with inputs.open(encoding="utf-8", newline="") as stream:
        values = {row["condition"]: float(row["value"]) for row in csv.DictReader(stream, delimiter="\t")}

    mass = values["parent_molar_mass"]
    fraction_unbound = values["parent_plasma_unbound_fraction"]
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("condition", "analyte", "compartment", "statistic", "value", "unit"))
    for condition in (
        "adult_fasted_peak", "adult_liquid_peak", "adult_solid_meal_peak",
        "under7_fa_week4_pre", "under7_fa_week12_3to6h",
    ):
        total_nm = values[condition] * 1000 / mass
        writer.writerow((condition, "parent", "plasma", "converted total", f"{total_nm:.2f}", "nmol/L"))
        writer.writerow((condition, "parent", "plasma", "conditional free at fu=0.022",
                         f"{total_nm * fraction_unbound:.2f}", "nmol/L"))

    peak_ratio = values["adult_solid_meal_peak"] / values["adult_liquid_peak"]
    auc_ratio = values["adult_solid_meal_auc"] / values["adult_liquid_auc"]
    parent_fraction = values["healthy_human_parent_auc"] / values["healthy_human_radioactivity_auc"]
    tissue_bql = values["rat_tissue_radioactivity_bql"] * 1_000_000 / mass
    writer.writerow(("solid_to_liquid", "parent", "plasma", "Cmax ratio", f"{peak_ratio:.2f}", "fold"))
    writer.writerow(("solid_to_liquid", "parent", "plasma", "AUC0–t ratio", f"{auc_ratio:.2f}", "fold"))
    writer.writerow(("parent_in_total_radioactivity", "parent", "plasma", "AUC0–t share",
                     f"{100 * parent_fraction:.2f}", "%"))
    writer.writerow(("rat_general_tissue_bql", "total radiolabel", "whole-tissue calibration",
                     "reference quantification limit", f"{tissue_bql:.2f}", "nmol equivalents/kg"))


if __name__ == "__main__":
    main()

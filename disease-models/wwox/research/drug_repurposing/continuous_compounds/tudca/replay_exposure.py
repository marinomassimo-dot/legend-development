"""Replay reported TUDCA exposure contrasts without pooling unlike compartments."""

import csv
from pathlib import Path
import sys


def main():
    inputs = Path(__file__).with_name("exposure_inputs.tsv")
    with inputs.open(encoding="utf-8", newline="") as handle:
        values = {row["key"]: float(row["value"]) for row in csv.DictReader(handle, delimiter="\t")}
    mass = values["parent_mass"]
    fasted = values["adult_combo_fasted"] / mass
    fed = values["adult_combo_fed"] / mass
    alone = values["rat_oral_alone_cmax"] / mass
    combined = values["rat_oral_combo_cmax"] / mass
    glutamate = values["glutamate_ldh"]
    rows = [
        ("adult_fasted_plasma", fasted, "uM total plasma"),
        ("adult_fed_plasma", fed, "uM total plasma"),
        ("rat_oral_alone_plasma", alone, "uM total plasma"),
        ("rat_oral_combined_plasma", combined, "uM total plasma"),
        ("rat_oral_alone_over_combo_cmax", alone / combined, "ratio of reported means"),
        ("rat_oral_alone_over_combo_auc", values["rat_oral_alone_auc"] / values["rat_oral_combo_auc"], "ratio of reported means"),
        ("echs1_bath_over_adult_total_plasma", values["echs1_proliferation_bath"] / fasted, "descriptive ratio across compartments"),
        ("lebeau_bath_over_adult_total_plasma", values["lebeau_er_bath"] / fasted, "descriptive ratio across compartments"),
        ("mouse_genetic_plasma_table_ratio", values["mouse_genetic_plasma_ko"] / values["mouse_genetic_plasma_ctrl"], "ratio of reported means"),
        ("mouse_genetic_plasma_figure_ratio", values["mouse_genetic_plasma_figure"], "reported relative value"),
        ("mouse_genetic_brain_table_ratio", values["mouse_genetic_brain_ko"] / values["mouse_genetic_brain_ctrl"], "ratio of reported means"),
        ("mouse_genetic_brain_figure_ratio", values["mouse_genetic_brain_figure"], "reported relative value"),
        ("rat_iv_poststroke_reconstructed_taurine_conjugate",
         1000 * values["rat_iv_poststroke_udca_pool"] * values["rat_iv_poststroke_tauro_fraction"],
         "pmol/g tissue, approximate derived conjugate"),
        ("tudca_associated_ldh_change", values["glutamate_tudca_ldh"] - glutamate, "percentage points relative to vehicle"),
        ("cdca_associated_ldh_change", values["glutamate_cdca_ldh"] - glutamate, "percentage points relative to vehicle"),
    ]
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("comparison", "value", "units_and_scope"))
    writer.writerows((name, f"{value:.6g}", units) for name, value, units in rows)


if __name__ == "__main__":
    main()

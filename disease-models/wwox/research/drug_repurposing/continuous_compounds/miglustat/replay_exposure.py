"""Compare observed human CSF exposure and published assay scales."""

import argparse
import csv
from pathlib import Path
import sys


def write_affinity_comparison(values, writer):
    writer.writerow(("csf_observation", "uM_parent", "CSF_over_GBA2_Ki", "GCS_IC50_over_CSF"))
    for label in ("csf_trough_min", "csf_trough_max"):
        parent = values[label] / values["parent_mass"]
        writer.writerow((
            label, f"{parent:.6g}", f"{parent / values['human_gba2_ki']:.6g}",
            f"{values['gcs_ic50'] / parent:.6g}",
        ))


def write_developmental_comparison(values, writer):
    mass = values["parent_mass"]
    low = values["csf_trough_min"] / mass
    high = values["csf_trough_max"] / mass
    bath = values["neurite_bath"]
    rows = [
        ("neurite_bath_over_high_GD3_CSF_trough", bath / high, "descriptive ratio"),
        ("neurite_bath_over_low_GD3_CSF_trough", bath / low, "descriptive ratio"),
        ("older_NPC_group_plasma_Cmax", values["npc_older_plasma_peak"] / mass, "uM total plasma"),
        ("younger_NPC_group_plasma_Cmax", values["npc_younger_plasma_peak"] / mass, "uM total plasma"),
        ("monkey_radioassay_CSF_6th", values["monkey_csf_6th"] / mass, "uM equivalent, radiotracer design"),
        ("monkey_radioassay_CSF_7th", values["monkey_csf_7th"] / mass, "uM equivalent, radiotracer design"),
        ("liver_lysate_with_over_without_detergent", values["liver_with_detergent"] /
         values["liver_without_detergent"], "apparent IC50 ratio, mixed activities"),
    ]
    writer.writerow(("comparison", "value", "units_and_scope"))
    writer.writerows((label, f"{value:.6g}", units) for label, value, units in rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--developmental", action="store_true")
    args = parser.parse_args()

    inputs = Path(__file__).with_name("exposure_inputs.tsv")
    with inputs.open(encoding="utf-8", newline="") as handle:
        values = {row["key"]: float(row["value"]) for row in csv.DictReader(handle, delimiter="\t")}
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    if args.developmental:
        write_developmental_comparison(values, writer)
    else:
        write_affinity_comparison(values, writer)


if __name__ == "__main__":
    main()

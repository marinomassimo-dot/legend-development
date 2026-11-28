"""Replay descriptive exposure sensitivity and capacitance scaling from primary data."""

import csv
from math import sqrt
from pathlib import Path


TREHALOSE_MASS = 342.3


def main():
    with Path(__file__).with_name("route_flux_inputs.tsv").open() as source:
        value = {row["estimate"]: float(row["value"]) for row in csv.DictReader(source, delimiter="\t")}

    csf = value["Macaque_CSF"] / TREHALOSE_MASS
    print(f"Macaque CSF: {csf:.3f} ± {value['Macaque_CSF_SEM'] / TREHALOSE_MASS:.3f} µM")
    for endpoint in ("Hippocampal_preconditioning_bath", "High_neuronal_bath"):
        print(f"{endpoint} / macaque CSF mean: {value[endpoint] / csf:.1f}")

    for day in (1, 7):
        brain = value[f"Rat_day{day}_brain"]
        plasma = value[f"Rat_day{day}_plasma"]
        print(f"Rat day {day} apparent volume: {1000 * brain / plasma:.2f} µL/g")
        for term in ("water", "protein"):
            residual = plasma * value[f"Rat_residual_plasma_{term}"] / 1000
            print(f"    illustrative residual from plasma-{term} space: {residual:.2f} ng/g")

    control_cap = value["Male_control_capacitance"]
    treated_cap = value["Male_treated_capacitance"]
    print(f"Male fixed 100 pA: {100 / control_cap:.2f} versus {100 / treated_cap:.2f} pA/pF")
    matched_control_pa = 120 * control_cap / treated_cap
    pixel_90 = value["Male_control_firing_at_90"]
    pixel_100 = value["Male_control_firing_at_100"]
    control_pixel = pixel_90 + (matched_control_pa - 90) * (pixel_100 - pixel_90) / 10
    axis_zero = value["AP_axis_zero"]
    pixels_per_ap = (axis_zero - value["AP_axis_twelve"]) / 12
    control_ap = (axis_zero - control_pixel) / pixels_per_ap
    treated_ap = (axis_zero - value["Male_treated_firing_at_120"]) / pixels_per_ap
    print(f"Matched group means at {120 / treated_cap:.2f} pA/pF: {control_ap:.1f} versus {treated_ap:.1f} AP")

    male_change = value["Spatial_male_treated"] - value["Spatial_male_control"]
    female_change = value["Spatial_female_treated"] - value["Spatial_female_control"]
    sem_values = [measurement for key, measurement in value.items() if key.startswith("Spatial_") and key.endswith("_SEM")]
    print(f"Descriptive spatial treatment-by-sex contrast: {male_change - female_change:.2f} ± "
          f"{sqrt(sum(sem ** 2 for sem in sem_values)):.2f} (independent-group SE)")


if __name__ == "__main__":
    main()

"""Reproduce cross-assay scale checks, without inferring free brain exposure."""
import argparse
import csv
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    base_mass_g_per_mol = 378.31  # PubChem CID 4046
    free_fraction_plasma = 0.02  # Approximation from DailyMed, not measured in this cohort
    recombinant_ic50_um = 0.31  # Cruikshank, Fig. 1
    native_approximate_ic50_um = 15.0  # Cruikshank, Results and Fig. 3
    proposed_concentration_um = 0.025
    recombinant_hill_1_fraction = proposed_concentration_um / (recombinant_ic50_um + proposed_concentration_um)

    rows = [
        ("slice_estimated_IC50_over_recombinant_IC50", native_approximate_ic50_um / recombinant_ic50_um, "ratio"),
        ("25nM_recombinant_Hill1_fraction_of_maximum", recombinant_hill_1_fraction, "fraction"),
    ]
    # Ramharter, Results and Table 1. Concentration at 54 h, not measured Cmax.
    for group, median_ng_ml in (("granules_age_2.3_to_6.0", 2550.0), ("tablets_age_6.3_to_12.0", 1815.0)):
        total_um = median_ng_ml / base_mass_g_per_mol
        free_um = total_um * free_fraction_plasma
        rows.extend((
            (f"{group}_total_at_54h", total_um, "uM"),
            (f"{group}_free_at_54h_scenario", free_um, "uM"),
            (f"{group}_10uM_nominal_slice_over_free_scenario", 10 / free_um, "ratio"),
            (f"{group}_25uM_nominal_slice_over_free_scenario", 25 / free_um, "ratio"),
        ))
    with args.output.open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(("comparison", "value", "unit"))
        writer.writerows((name, f"{value:.4f}", unit) for name, value, unit in rows)


if __name__ == "__main__":
    main()

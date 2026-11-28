"""Reproduce the descriptive bicarbonate contrasts from Jones et al. (2014)."""
import csv
from math import log10
import sys


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("source", "contrast", "higher_bicarbonate", "lower_bicarbonate",
                     "lower_over_higher", "lower_minus_higher", "unit"))
    contrasts = [
        ("Fig_4", "nominal_pipette_26_to_13_AIS_median", 13, 4, "spikes_per_ramp"),
        ("Fig_4", "nominal_pipette_26_to_13_somatic_median", 22, 19, "spikes_per_ramp"),
        ("Fig_1C_Table_2", "nominal_pipette_26_to_0_mAHP_area_magnitude", .68, 1.12, "mV_s"),
        ("Fig_7A", "bath_26_vs_0_no_blocker_mean", 53, 17, "spikes_per_ramp"),
        ("Fig_7A", "bath_26_vs_0_with_XE991_mean", 40, 49, "spikes_per_ramp"),
    ]
    for source, name, higher, lower, unit in contrasts:
        writer.writerow((source, name, higher, lower, f"{lower / higher:.4f}",
                         f"{lower - higher:.4f}", unit))
    # Henderson–Hasselbalch at equilibrium: pH = pKa + log10([HCO3-] / [CO2]).
    # A halving of HCO3- requires a halving of dissolved CO2 to preserve pH.
    writer.writerow(("equilibrium_scenario", "half_HCO3_with_CO2_held_pH_shift", "",
                     "", "", f"{log10(.5):.4f}", "pH_units"))
    writer.writerow(("equilibrium_scenario", "half_HCO3_with_pH_held_CO2_ratio", "",
                     "", "0.5000", "", "ratio"))


if __name__ == "__main__":
    main()

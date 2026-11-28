"""Reproduce concentration and time comparisons for the DCA exposure checkpoint."""
import csv
import math
import sys


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("quantity", "basis", "unit", "value"))
    writer.writerow(("Kuroda_CSF_to_blood", "reported_mass_values", "ratio", 125 / 250))
    writer.writerow(("Brandsma_apparent_two_point_half_time", "14_day_interval", "days",
                     f"{14 * math.log(2) / math.log(78 / 11):.4f}"))
    samples = [
        ("Kuroda_adolescent_CSF", 125), ("Kuroda_adolescent_blood", 250),
        ("Shroads_pediatric_mean_plasma_peak_month_6", 35),
        ("Brandsma_adult_CSF_day_2", 78), ("Brandsma_adult_CSF_day_16", 11),
    ]
    for basis, mass in (("unlabelled_acid_equivalent", 128.94), ("sodium_salt_equivalent", 150.92)):
        for name, mass_concentration in samples:
            writer.writerow((name, basis, "mM", f"{mass_concentration / mass:.4f}"))
        for context, enzyme_ic50 in (("core_free", .29), ("core_bound", .48)):
            mass_threshold = enzyme_ic50 * mass
            writer.writerow((f"PDK2_{context}_IC50", basis, "mg/L_equivalent",
                             f"{mass_threshold:.4f}"))
            writer.writerow((f"CSF_over_plasma_needed_at_35_mg_L_for_{context}_IC50",
                             basis, "scenario_ratio", f"{mass_threshold / 35:.4f}"))


if __name__ == "__main__":
    main()

"""Convert aggregate exposure benchmarks without assuming free CNS equilibrium."""
import csv
import sys


PARENT = 236.27
EPOXIDE = 252.27


def micromolar(mass_concentration, molar_mass=PARENT):
    return 1000 * mass_concentration / molar_mass


def main():
    total_low, total_high = map(micromolar, (4, 12))
    free_low, free_high = (total_low * .24, total_high * .24)
    sensitivity_low, sensitivity_high = (total_low * .33, total_high * .33)
    parent_csf_min, parent_csf_max = map(micromolar, (1.0, 3.1))
    rows = [
        ("Tegretol_label_total_parent_plasma_reference", "label_range", total_low, total_high, "uM"),
        ("Tegretol_label_parent_plasma_reference_x_0.24", "scenario", free_low, free_high, "uM"),
        ("Pynnonen_aggregate_CSF_fraction_0.33_x_label_plasma_reference",
         "cross_study_scenario", sensitivity_low, sensitivity_high, "uM"),
        ("Riva_Table1_free_parent_plasma_CBZ_only_n22", "measured_pediatric_mean", 5.17, 5.17, "uM"),
        ("Riva_Table1_free_parent_plasma_plus_phenobarbital_n17", "measured_pediatric_mean",
         4.41, 4.41, "uM"),
        ("Riva_Table1_free_epoxide_plasma_CBZ_only_n22", "measured_pediatric_mean", 1.84, 1.84, "uM"),
        ("Riva_Table1_free_epoxide_plasma_plus_phenobarbital_n17", "measured_pediatric_mean",
         2.08, 2.08, "uM"),
        ("Liu_abstract_free_parent_serum_n55", "measured_pediatric_mean",
         micromolar(2.59), micromolar(2.59), "uM"),
        ("Liu_abstract_free_epoxide_serum_n55", "measured_pediatric_mean",
         micromolar(1.05, EPOXIDE), micromolar(1.05, EPOXIDE), "uM"),
        ("Johannessen_Table4_parent_CSF_range", "measured_17plus", parent_csf_min, parent_csf_max, "uM"),
        ("Johannessen_Table4_parent_CSF_mean", "measured_17plus", micromolar(2.1), micromolar(2.1), "uM"),
        ("Johannessen_Table4_epoxide_CSF_mean", "measured_17plus",
         micromolar(.7, EPOXIDE), micromolar(.7, EPOXIDE), "uM"),
        ("Schiebler_nominal_parent_over_max_Johannessen_parent_CSF", "scale_ratio",
         50 / parent_csf_max, 50 / parent_csf_max, "fold"),
        ("Schiebler_nominal_parent_over_upper_0.33_CSF_scenario", "scale_ratio",
         50 / sensitivity_high, 50 / sensitivity_high, "fold"),
    ]
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("benchmark", "evidence_type", "lower_or_mean", "upper_or_mean", "unit"))
    for benchmark, evidence_type, lower, upper, unit in rows:
        writer.writerow((benchmark, evidence_type, f"{lower:.4f}", f"{upper:.4f}", unit))


if __name__ == "__main__":
    main()

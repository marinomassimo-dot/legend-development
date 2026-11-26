"""Reproduce the sultiame exposure comparison and the infant trial count check."""
import csv
from math import comb
import sys


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("quantity", "study_condition", "unit", "value"))
    # Dao et al., Table 1, geometric means of individual Cmax values.
    for dose, plasma, blood in ((50, 0.02, 7.91), (100, 0.18, 15.87), (200, 1.88, 17.19)):
        condition = f"Dao_single_oral_{dose}_mg"
        plasma_um = 1000 * plasma / 290.4
        writer.writerow(("total_plasma_Cmax", condition, "uM", f"{plasma_um:.4f}"))
        writer.writerow(("total_whole_blood_Cmax", condition, "uM", f"{1000 * blood / 290.4:.4f}"))
        writer.writerow(("whole_blood_to_plasma_separate_Cmax", condition, "ratio", f"{blood / plasma:.4f}"))
        for bath_um in (1000, 2500):
            writer.writerow((f"Leniger_{bath_um}_uM_bath_to_plasma_Cmax", condition,
                             "ratio", f"{bath_um / plasma_um:.4f}"))

    # Hoff et al., Results and Fig. 3: separate adult OSA cohort, total plasma trough.
    for label, mass_concentration in (("mean_high_dose_group", 5.68), ("highest_observed", 9.37)):
        micromolar = 1000 * mass_concentration / 290.4
        writer.writerow(("total_plasma_trough", label, "uM", f"{micromolar:.4f}"))
        writer.writerow(("Leniger_1000_uM_bath_to_total_plasma_trough", label,
                         "ratio", f"{1000 / micromolar:.4f}"))
    # Sleep Breath 2025, Experiment 6: mean enzyme activities before intervention.
    writer.writerow(("CSF_to_whole_blood_CA_activity_ratio_of_means", "untreated_adults", "ratio",
                     f"{2.78 / 14.38:.4f}"))

    # Debus and Kurlemann, intention-to-treat complete electroclinical response.
    successes, treated, controls = 6, 20, 17
    denominator = comb(treated + controls, successes)
    allocation_weights = [comb(treated, treated_successes) * comb(controls, successes - treated_successes)
                          for treated_successes in range(successes + 1)]
    observed_weight = allocation_weights[successes]
    fisher = sum(weight for weight in allocation_weights if weight <= observed_weight) / denominator
    writer.writerow(("treated_minus_placebo_complete_response", "Debus_day_9", "percentage_points",
                     f"{100 * successes / treated:.2f}"))
    writer.writerow(("fisher_two_sided", "Debus_day_9", "p", f"{fisher:.6f}"))


if __name__ == "__main__":
    main()

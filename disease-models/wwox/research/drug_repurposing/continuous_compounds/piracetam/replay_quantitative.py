"""Reproduce labelled concentration, count and circuit sensitivity calculations."""
import csv
from itertools import product
from math import sqrt
import sys


PIRACETAM_G_MOL = 142.16


def main():
    output = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    output.writerow(("source", "contrast", "value", "unit", "basis"))

    plasma = (
        ("Yan Table 2", "fed_test", 20.4429),
        ("Yan Table 2", "fed_reference", 20.7750),
        ("Yan Table 2", "fasting_test", 31.6786),
        ("Yan Table 2", "fasting_reference", 32.1179),
        ("AEMPS §5.2", "historical_single", 84.0),
        ("AEMPS §5.2", "historical_repeated", 115.0),
    )
    for source, name, ug_ml in plasma:
        peak = 1000 * ug_ml / PIRACETAM_G_MOL
        output.writerow((source, name, f"{peak:.2f}", "µM_total_plasma",
                         f"input={ug_ml} µg/mL; MW={PIRACETAM_G_MOL} g/mol"))
        output.writerow((source, name + "_SCG_IC50_scale", f"{100 * 3.4 / peak:.2f}", "%",
                         "3.4 µM / measured total plasma peak; no CNS exposure inference"))

    control_current = 7.79
    exposed_current = 1.90
    block = 1 - exposed_current / control_current
    output.writerow(("Bravo Fig. 2Ac", "mean_current_density_reduction", f"{100 * block:.2f}",
                     "%", "1 − 1.90 / 7.79; ratio of reported means, pA/pF"))

    counts = (
        ("Fig. 5Cb", "CA1_AP", 133, 97, 11, 10),
        ("Fig. 5Cc", "CA1_EPSP", 80, 18, 7, 3),
        ("Fig. 6B", "low_Mg_high_K_AP", 77.5, 37.3, 0.9, 1.8),
    )
    for panel, name, control, treated, sem_control, sem_treated in counts:
        output.writerow(("Bravo " + panel, name, f"{100 * (treated / control - 1):.2f}",
                         "%", f"{treated} / {control} − 1; per 20 s"))
        for corr in (-1, 0, 1):
            variance = sem_control**2 + sem_treated**2 - 2 * corr * sem_control * sem_treated
            se_difference = sqrt(variance)
            output.writerow(("Bravo " + panel, name + "_illustrative_paired_SE",
                             f"{se_difference:.2f}", "events_per_20_s",
                             f"within-pair correlation={corr}; assumes paired cell means"))

    output.writerow(("Bravo Fig. 5Cc", "gain_per_event_to_hold_total_charge",
                     f"{80 / 18:.3f}", "fold", "count ratio alone; each event must carry equal mean charge after scaling"))

    output.writerow(("Breton §2.3", "threshold_KO_to_WT_peak_for_equal_charge", f"{5.18 / 4.84:.3f}",
                     "fold", "single exponential, multiply peak by effective decay; group means only"))
    for exc_fraction, inh_fraction in product((0.2, 0.5, 0.8), repeat=2):
        relative_gain = (1 - block * exc_fraction) / (1 - block * inh_fraction)
        output.writerow(("Illustrative terminal model", "minimum_gI_over_gE_for_relative_improvement",
                         f"{relative_gain:.3f}", "fold",
                         f"b={block:.4f}; fE={exc_fraction}; fI={inh_fraction}; no native release estimate"))


if __name__ == "__main__":
    main()

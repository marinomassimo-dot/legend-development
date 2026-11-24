"""Aggregate serum scenarios; fractions from a separate analysis, with no CNS assumption."""
import csv
import sys

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("population_summary", "total_ug_ml", "fraction_assumed", "calculated_unbound_uM"))
for population, total in (("1994_seizure_free_mean", 9.7), ("2004_trough_mean", 27.0),
                          ("2004_peak_mean", 33.8)):
    for fraction in (0.51, 0.61):
        writer.writerow((population, total, fraction, round(total * 1000 / 212.23 * fraction, 2)))

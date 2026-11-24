"""Recalculate ratios of the published group means in PMID 21379380, Table 2."""
import csv
import sys

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("measure", "reference", "comparison", "reference_mean", "comparison_mean", "ratio"))
observations = [
    ("peak uridine, uM", "pure uridine", "TAU-rich supplement day 1", 36.1, 150.9),
    ("baseline-adjusted AUC to infinity", "pure uridine", "TAU-rich supplement day 1", 135.4, 599.5),
    ("baseline uridine, uM", "supplement day 1", "supplement day 7", 4.7, 31.1),
    ("unadjusted AUC to infinity", "supplement day 1", "supplement day 7", 620.8, 843.6),
    ("baseline-adjusted AUC to infinity", "supplement day 1", "supplement day 7", 599.5, 606.2),
]
for measure, reference, comparison, first, second in observations:
    writer.writerow((measure, reference, comparison, first, second, round(second/first, 4)))

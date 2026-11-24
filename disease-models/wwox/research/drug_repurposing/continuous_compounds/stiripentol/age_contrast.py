"""Arithmetic from Cao et al. (2012), pp. 1142–43, Tables 2–3."""
import csv
import math
import sys

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("measure", "group", "before", "after", "difference_C", "approx_SE_C",
                 "lower_95_C", "upper_95_C"))
# The reported within-age t statistics and the means are rounded.
# Use df=5 for both six-mouse paired contrasts and as a conservative
# critical value for their independent Welch contrast (df about 5.96).
critical = 2.570582
estimates = []
for group, before, after, paired_t in [
    ("4_weeks", 39.67, 41.32, 3.097),
    ("5_to_10_months", 40.82, 40.98, 0.966),
]:
    change = after - before
    se = change / paired_t
    estimates.append((change, se))
    writer.writerow(("STP_alone_thermal_threshold", group, before, after,
                     f"{change:.2f}", f"{se:.3f}", f"{change-critical*se:.3f}",
                     f"{change+critical*se:.3f}"))

(young, se_young), (older, se_older) = estimates
difference = young - older
se = math.hypot(se_young, se_older)
writer.writerow(("difference_of_changes", "young_minus_older", "", "",
                 f"{difference:.2f}", f"{se:.3f}", f"{difference-critical*se:.3f}",
                 f"{difference+critical*se:.3f}"))

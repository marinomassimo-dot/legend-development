"""Recalculate group-level agonist increments and the molar plasma trough scale."""
import csv
from pathlib import Path
import sys

out = Path(sys.argv[1])
with (out / "agonist.tsv").open("w") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(("topiramate_bath_uM", "ATPA_current_pct_control",
                     "sIPSC_frequency_pct_baseline", "pct_of_ATPA_frequency_increment_remaining"))
    for bath, current, frequency in [(0, 100, 895), (.3, 71.9, 697), (1, 54.2, 466), (10, 12.3, 108)]:
        writer.writerow((bath, current, frequency, round(100 * (frequency-100) / (895-100), 1)))
with (out / "trough.tsv").open("w") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(("published_arm_mg_per_kg_day", "n", "infant_total_plasma_mean_ug_ml",
                     "SD_ug_ml", "total_plasma_mean_uM", "adult_partition_scenario_total_CSF_uM"))
    for arm, n, mean, sd in [(3,9,1.91,1.04),(5,9,3.25,1.89),(15,8,9.74,4.82),(25,9,13.6,5.19)]:
        plasma = 1000 * mean / 339.36
        writer.writerow((arm,n,mean,sd,round(plasma,2),round(plasma*.85,2)))

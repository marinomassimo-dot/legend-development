"""Reproduce plotted/table-derived contrasts and the conditional CNS exposure bridge."""
import csv
from pathlib import Path
import sys


MASS_G_PER_MOL = 169.57
ADULT_FU_SCENARIO = 0.039


def rows(filename):
    with Path(__file__).with_name(filename).open(newline="") as handle:
        yield from csv.DictReader(handle, delimiter="\t")


def main():
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(("comparison", "metric", "value", "unit"))
    for row in rows("source_contrasts.tsv"):
        reference = float(row["reference"])
        result = float(row["comparison"])
        out.writerow((row["contrast"], "comparison_over_reference",
                      f"{result / reference:.5f}", "ratio"))
        out.writerow((row["contrast"], "difference",
                      f"{result - reference:.5f}", row["unit"]))

    for row in rows("exposure_inputs.tsv"):
        population = row["population"]
        total_uM = float(row["total_peak_mg_per_ml"]) * 1e6 / MASS_G_PER_MOL
        out.writerow((population, "total_plasma_or_serum_peak", f"{total_uM:.3f}", "uM"))
        if row["measured_fu"] != "NA":
            scenario_fu = float(row["measured_fu"])
            basis = "adult_measured_fu"
        else:
            scenario_fu = ADULT_FU_SCENARIO
            basis = "borrowed_adult_fu"
        free_systemic = total_uM * scenario_fu
        out.writerow((population, "free_systemic_peak_using_" + basis,
                      f"{free_systemic:.3f}", "uM"))
        for benchmark in (30, 60, 100):
            out.writerow((population, f"min_fu_times_Kpuu_for_{benchmark}uM",
                          f"{benchmark / total_uM:.3f}", "ratio"))
            out.writerow((population, f"min_Kpuu_for_{benchmark}uM_using_" + basis,
                          f"{benchmark / free_systemic:.2f}", "ratio"))


if __name__ == "__main__":
    main()

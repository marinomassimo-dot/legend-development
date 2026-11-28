"""Recalculate descriptive glycan contrasts from the cited primary values."""

import csv
import sys
from decimal import Decimal
from pathlib import Path
from statistics import median


def main():
    with Path(__file__).with_name("processing_inputs.tsv").open(
        encoding="utf-8", newline=""
    ) as source:
        values = {
            row["key"]: Decimal(row["value"])
            for row in csv.DictReader(source, delimiter="\t")
        }

    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("comparison", "measure", "value", "unit"))

    for lineage in ("ipsc", "inn", "iad"):
        ratio = values[f"{lineage}_man5"] / values[f"{lineage}_man9"]
        writer.writerow((lineage, "Man5_to_Man9", f"{ratio:.3f}", "ratio"))

    for measure in ("high", "sialic", "man5"):
        for end, start in (("inn", "ipsc"), ("iad", "ipsc"), ("iad", "inn")):
            change = values[f"{end}_{measure}"] - values[f"{start}_{measure}"]
            writer.writerow((f"{end}_minus_{start}", measure, f"{change:.1f}", "pp"))

    case = values["cog_case_oligomannose"] / values["cog_case_sialic"]
    control = values["cog_control_oligomannose"] / values["cog_control_sialic"]
    for measure, ratio in (
        ("oligomannose_to_sialic_case", case),
        ("oligomannose_to_sialic_control", control),
        ("case_over_control_ratio", case / control),
    ):
        writer.writerow(("COG6-CDG_fibroblast", measure, f"{ratio:.3f}", "ratio"))
    serum = values["cog_case_disialylated"] - values["cog_control_disialylated"]
    writer.writerow(("COG6-CDG_serum", "case_minus_control_disialylated", f"{serum:.1f}", "pp"))

    ratios = []
    for experiment in (1, 3, 4):
        ratio = values[f"mpi_{experiment}_500"] / values[f"mpi_{experiment}_100"]
        ratios.append(ratio)
        writer.writerow((f"Mpi_null_{experiment}", "mature_LLO_500uM_over_100uM", f"{ratio:.3f}", "ratio"))
    writer.writerow(("Mpi_null_median", "mature_LLO_500uM_over_100uM", f"{median(ratios):.3f}", "ratio"))


if __name__ == "__main__":
    main()

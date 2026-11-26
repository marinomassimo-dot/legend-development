"""Check the held fly study for explicitly named galactose pathway metabolites."""

import argparse
import csv
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "l_glutamine"))
from feature_identity import worksheet_rows


def is_target(name):
    name = re.sub(r"[^a-z0-9]", "", name.lower())
    name = re.sub(r"alpha|beta", "", name)
    if name.startswith("d"):
        name = name[1:]
    return name in {"galactose", "galactose1phosphate", "galactose1p", "galactitol"} or bool(
        re.fullmatch(r"(udp|uridinediphosphate)d?galactose", name)
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", type=Path)
    parser.add_argument("assignments", type=Path)
    args = parser.parse_args()
    table = list(worksheet_rows(args.workbook))
    with args.assignments.open(encoding="utf-8") as source:
        records = json.load(source)["data"]["rows"]

    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("source", "total_rows", "rows_with_named_target"))
    writer.writerow(("knockdown_significant_peak_candidates", len(table),
                     sum(any(is_target(name) for name in row.get("D", "").split(";")) for row in table)))
    writer.writerow(("knockdown_significant_peak_assignments", len(table),
                     sum(is_target(row.get("E", "")) for row in table)))
    writer.writerow(("deposit_assigned_peaks", len(records),
                     sum(is_target(row.get("metabolite_identification", "")) for row in records)))


if __name__ == "__main__":
    main()

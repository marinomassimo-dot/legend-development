"""Reproduce the parent-exposure and adult adverse-event checkpoint from primary sources."""
import argparse
import csv
from hashlib import sha256
from pathlib import Path
from statistics import mean
import sys
import xml.etree.ElementTree as ET


RETT_DIGEST = "a94f145b9533c357dbc8145448f309cf3ec28723e4213b6e7f33776db9c81b02"
TARGET_NOMINAL_UM = 10.0
PARENT_MASS = 286.41


def parent_measurements(source):
    if sha256(source).hexdigest() != RETT_DIGEST:
        raise ValueError("Unexpected Rett article XML version")
    root = ET.fromstring(source)
    table, = (e for e in root.findall(".//table-wrap") if e.findtext("label") == "TABLE 6")
    rows = [["".join(cell.itertext()).strip() for cell in row] for row in table.findall(".//tr")]
    start = rows.index(["CBDV"])
    cmax = [float(value) for value in rows[start + 1][1:-1] if value]
    eot = [float(value) for value in rows[start + 4][1:-1] if value]
    same_columns = [float(eot_value) for first, eot_value in
                    zip(rows[start + 1][1:-1], rows[start + 4][1:-1], strict=True) if first and eot_value]
    assert len(cmax) == len(same_columns) == 4 and len(eot) == 5
    return cmax, eot, same_columns


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("rett_xml", type=Path)
    args = parser.parse_args()
    cmax, eot, same_columns = parent_measurements(args.rett_xml.read_bytes())
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(("comparison", "value", "units", "denominator"))
    for label, samples in (("first-exposure parent Cmax", cmax),
                           ("end-of-treatment parent trough, all values", eot),
                           ("end-of-treatment parent trough, first-exposure PK columns", same_columns)):
        out.writerow((label, f"{mean(samples):.6f}", "ng/mL", len(samples)))
        out.writerow((label, f"{mean(samples)/PARENT_MASS:.6f}", "micromolar total plasma", len(samples)))

    out.writerow(("10 micromolar nominal / mean pediatric first Cmax",
                  f"{TARGET_NOMINAL_UM/(mean(cmax)/PARENT_MASS):.4f}", "cross-matrix ratio", "4 first-exposure measured"))
    for label, active, placebo in (("any adverse event", 59, 39), ("adverse-event discontinuation", 11, 2)):
        out.writerow((label + ", active minus placebo", f"{100 * (active - placebo) / 81:.4f}",
                      "percentage points", "81/81 randomized"))


if __name__ == "__main__":
    main()

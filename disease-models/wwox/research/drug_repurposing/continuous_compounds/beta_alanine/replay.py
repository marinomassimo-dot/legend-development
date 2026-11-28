"""Replay aggregate MRS change and carnosine signal sensitivity.

Input: unmodified Solis et al. S1 XLSX. Only paired metabolite cells are read.
The Hoffman values are derived from the vector figure, not individual animal data.
"""

import argparse
import csv
import hashlib
import statistics
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path


WORKBOOK_SHA256 = "6f7a5aec63a5646143790fd5d54af165b5a6636766e954aa310fef52c804fec2"
XLSX_NAMESPACE = {"x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
T_CRITICAL = 2.160368656461013  # Two-sided 95%, 13 degrees of freedom.


def read_pairs(path):
    if hashlib.sha256(path.read_bytes()).hexdigest() != WORKBOOK_SHA256:
        raise ValueError("S1 workbook fingerprint does not match the cited file")
    rows = [*range(5, 12), *range(17, 24)]
    wanted = {f"{column}{row}" for column in ("B", "D") for row in rows}
    with zipfile.ZipFile(path) as workbook:
        worksheet = ET.fromstring(workbook.read("xl/worksheets/sheet2.xml"))
    values = {
        cell.attrib["r"]: float(cell.findtext("x:v", namespaces=XLSX_NAMESPACE))
        for cell in worksheet.findall(".//x:c", XLSX_NAMESPACE)
        if cell.attrib["r"] in wanted
    }
    return [(values[f"B{row}"], values[f"D{row}"]) for row in rows]


def comparison(pairs):
    before = statistics.mean(pre for pre, _ in pairs)
    after = statistics.mean(post for _, post in pairs)
    changes = [post - pre for pre, post in pairs]
    delta = statistics.mean(changes)
    standard_error = statistics.stdev(changes) / len(changes) ** 0.5
    lower = delta - T_CRITICAL * standard_error
    upper = delta + T_CRITICAL * standard_error
    yield "Solis paired adult MRS", "participants", len(pairs), "count"
    yield "Solis paired adult MRS", "mean pre", before, "band/creatine"
    yield "Solis paired adult MRS", "mean post", after, "band/creatine"
    yield "Solis paired adult MRS", "mean paired change", delta, "band/creatine"
    yield "Solis paired adult MRS", "paired SE", standard_error, "band/creatine"
    yield "Solis paired adult MRS", "paired t", delta / standard_error, "ratio"
    yield "Solis paired adult MRS", "95% lower", lower, "band/creatine"
    yield "Solis paired adult MRS", "95% upper", upper, "band/creatine"
    yield "Solis scaled to observed mean pre", "mean", 100 * delta / before, "%"
    yield "Solis scaled to observed mean pre", "95% lower", 100 * lower / before, "%"
    yield "Solis scaled to observed mean pre", "95% upper", 100 * upper / before, "%"

    # Hoffman Fig. 1, manuscript page 14, PDF page 15. PDF coordinates increase down.
    zero_y, forty_y = 470.76, 47.76
    control = 40 * (zero_y - 315.36) / (zero_y - forty_y)
    exposed = 40 * (zero_y - 175.68) / (zero_y - forty_y)
    yield "Hoffman Fig. 1 vector estimate", "control mean", control, "nmol/g"
    yield "Hoffman Fig. 1 vector estimate", "exposed mean", exposed, "nmol/g"
    yield "Hoffman Fig. 1 vector estimate", "relative increase", 100 * (exposed / control - 1), "%"
    reported_rat_change = 0.895
    for fraction in (0.05, 0.10, 0.20, 0.30):
        yield "Carnosine-only increase of 89.5%", f"MRS change at f={fraction:.2f}", 100 * fraction * reported_rat_change, "%"
    yield "Carnosine-only increase of 89.5%", "f at observed scaled upper interval", upper / before / reported_rat_change, "fraction"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", type=Path)
    inputs = parser.parse_args()
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("comparison", "statistic", "value", "unit"))
    for contrast, statistic, value, unit in comparison(read_pairs(inputs.workbook)):
        writer.writerow((contrast, statistic, f"{value:.8g}", unit))


if __name__ == "__main__":
    main()

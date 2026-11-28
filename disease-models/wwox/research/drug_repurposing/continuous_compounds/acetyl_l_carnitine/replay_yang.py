"""Recompute aggregate C0 and C2 contrasts from the Yang et al. supplement DOCX."""

import argparse
from collections import defaultdict
from math import sqrt
from statistics import mean, stdev
import xml.etree.ElementTree as ET
from zipfile import ZipFile


WORD = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
TABLES = {
    "S4": ("Oli-neu", "nmol/mg protein"),
    "S6": ("serum", "uM"),
    "S8": ("mPFC", "nmol/mg protein"),
}
COEFFICIENTS = {"SI-ALC": 1, "SI-DW": -1, "RE-ALC": -1, "RE-DW": 1}


def cell_text(cell):
    return "".join(node.text or "" for node in cell.findall(".//w:t", WORD))


def observations(docx):
    with ZipFile(docx) as source:
        document = ET.fromstring(source.read("word/document.xml"))
    table = ""
    groups = defaultdict(list)
    for node in document.find("w:body", WORD):
        if node.tag.endswith("}p"):
            heading = cell_text(node)
            if heading.startswith("Supplementary Table "):
                table = heading.split()[2].rstrip(".")
        elif node.tag.endswith("}tbl") and table in TABLES:
            for row in node.findall("w:tr", WORD):
                cells = [cell_text(cell) for cell in row.findall("w:tc", WORD)]
                if len(cells) != 4:
                    continue
                group = cells[0] if table == "S4" else cells[1]
                try:
                    c0, c2 = map(float, cells[2:])
                except ValueError:
                    continue
                groups[table, "C0", group].append(c0)
                groups[table, "C2", group].append(c2)
    return groups


def report(groups):
    print("table\tcompartment\tunit\tanalyte\tcomparison\tn\testimate\tSD_or_SE\tomit_min\tomit_max")
    for table, (compartment, units) in TABLES.items():
        for analyte in ("C0", "C2"):
            prefix = f"{table}\t{compartment}\t{units}\t{analyte}"
            subset = {group: values for (key, species, group), values in groups.items()
                      if (key, species) == (table, analyte)}
            if table == "S4":
                expected = {"Con": 6, "ALC": 6, "LC": 6}
            else:
                expected = {"RE-DW": 5, "RE-ALC": 4, "SI-DW": 5, "SI-ALC": 4}
            if {group: len(values) for group, values in subset.items()} != expected:
                raise ValueError(f"Unexpected sample counts in {table} {analyte}")
            averages = {group: mean(values) for group, values in subset.items()}
            for group in expected:
                values = subset[group]
                print(f"{prefix}\t{group} mean\t{len(values)}\t{averages[group]:.3f}\t{stdev(values):.3f}\t.\t.")
            if table == "S4":
                continue
            for housing in ("RE", "SI"):
                delta = averages[f"{housing}-ALC"] - averages[f"{housing}-DW"]
                print(f"{prefix}\t{housing} ALC - DW\t.\t{delta:.3f}\t.\t.\t.")
            delta = sum(COEFFICIENTS[group] * average for group, average in averages.items())
            se = sqrt(sum(stdev(values)**2 / len(values) for values in subset.values()))
            omissions = [
                delta + COEFFICIENTS[group] * (mean(values[:i] + values[i + 1:]) - averages[group])
                for group, values in subset.items() for i in range(len(values))
            ]
            print(f"{prefix}\tSI increment - RE increment\t.\t{delta:.3f}\t{se:.3f}"
                   f"\t{min(omissions):.3f}\t{max(omissions):.3f}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("supplement", help="Publisher's DOCX supplementary information")
    args = parser.parse_args()
    report(observations(args.supplement))


if __name__ == "__main__":
    main()

"""Summarize public Fig. 8 Echs1 treatment means and additive interaction contrasts."""

import argparse
from math import sqrt
from pathlib import Path
from statistics import mean, variance
from xml.etree import ElementTree
from zipfile import ZipFile

NS = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
PANELS = (
    ("8b ATF4, fold", "BCDE", 4, (3, 3, 3, 3), True),
    ("8c FASN, fold", "BCDE", 9, (3, 3, 3, 3), True),
    ("8e droplets/NSPC", "HIJK", 4, (59, 60, 62, 61), False),
    ("8f droplet diameter, um", "NOPQ", 4, (145, 169, 174, 171), False),
    ("8i SVZ labelled cells/mm^3", "BCDE", 16, (4, 4, 4, 4), True),
    ("8j DG labelled cells/mm^3", "BCDE", 26, (4, 4, 4, 4), True),
    ("8m DG NeuN among BrdU, percent", "BCDE", 36, (4, 4, 4, 4), True),
    ("8n DG DCX among BrdU, percent", "BCDE", 44, (4, 4, 4, 4), True),
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", type=Path, help="published Echs1 Source Data XLSX")
    args = parser.parse_args()

    with ZipFile(args.workbook) as workbook:
        sheet = ElementTree.fromstring(workbook.read("xl/worksheets/sheet8.xml"))
    cells = {cell.get("r"): cell.findtext("s:v", namespaces=NS)
             for cell in sheet.findall(".//s:c", NS)}
    print("panel\tWT control\tKO control\tWT TUDCA\tKO TUDCA\tWT effect\tKO effect\tKO minus WT effect\tSE independent arms")
    for label, columns, first_row, counts, animals in PANELS:
        groups = [[float(cells[f"{column}{row}"]) for row in range(first_row, first_row + count)]
                  for column, count in zip(columns, counts)]
        wild, knock, wild_treated, knock_treated = map(mean, groups)
        wt_effect = wild_treated - wild
        ko_effect = knock_treated - knock
        interaction = ko_effect - wt_effect
        # The figure reports multiple cells or droplets for panels e and f. Their
        # descriptive means are replayed without treating those rows as animals.
        se = f"{sqrt(sum(variance(group) / len(group) for group in groups)):.4g}" if animals else "not estimated"
        fields = [f"{value:.5g}" for value in
                  (wild, knock, wild_treated, knock_treated, wt_effect, ko_effect, interaction)]
        print("\t".join([label, *fields, se]))


if __name__ == "__main__":
    main()

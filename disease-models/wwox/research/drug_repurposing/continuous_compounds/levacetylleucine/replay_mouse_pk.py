"""Summarize the L-enantiomer columns of Churchill et al. 2020 S1/S2."""

import argparse
import csv
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
from statistics import mean
from zipfile import ZipFile

WORD = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def parse_table(path):
    with ZipFile(path) as source:
        document = ET.fromstring(source.read("word/document.xml"))
    groups = defaultdict(list)
    for item in document.findall(".//w:tr", WORD)[2:]:
        row = [
            "".join(node.text or "" for node in cell.findall(".//w:t", WORD))
            for cell in item.findall("w:tc", WORD)
        ]
        time, plasma, brain = row[1:4]
        groups[time].append((plasma, brain))
    return groups


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("documents", type=Path, nargs=2, metavar="DOCX")
    args = parser.parse_args()
    output = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    output.writerow(("table", "source_time_label", "plasma_numeric_n", "plasma_mean_ng_per_ml",
                     "brain_nd_n", "brain_blank_n", "brain_other_n"))
    for label, document in zip(("S1", "S2"), args.documents):
        for time, observations in parse_table(document).items():
            plasma = [float(value) for value, _ in observations if value.replace(".", "", 1).isdigit()]
            brain = [value for _, value in observations]
            nd = brain.count("ND")
            blank = brain.count("")
            output.writerow((label, time, len(plasma), f"{mean(plasma):.3f}" if plasma else "",
                             nd, blank, len(brain) - nd - blank))


if __name__ == "__main__":
    main()

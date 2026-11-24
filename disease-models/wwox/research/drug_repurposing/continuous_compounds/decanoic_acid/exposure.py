"""Reproduce the slice-to-dialysate comparison using the archived primary reports."""
import csv
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def run(files, output):
    paper = files / "deepening_downloads"
    adult = Text()
    adult.feed((paper / "d_bhb_loop_20261123/interstitial.html").read_text())
    content = " ".join(" ".join(adult.parts).split())
    match = re.search(r"Brain C8 and C10 ranged between (\d+) and (\d+) [µμ]mol/L", content)
    if not match:
        raise ValueError("Brain microdialysis range was not located")
    brain_range = [float(value) for value in match.groups()]
    article = ET.parse(paper / "triheptanoin_loop_20261123/PMC4805082.xml")
    paragraphs = [" ".join("".join(p.itertext()).split()) for p in article.findall(".//p")]
    matched = [p for p in paragraphs if "38.9" in p and "300" in p]
    if not matched:
        raise ValueError("Expected CA1 concentration and response were not found in the same paragraph")
    bath = 300.0
    with output.open("w", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(["dialysate_uM", "slice_bath_uM", "bath_over_dialysate", "recovery_pct_if_equal"])
        for value in brain_range:
            writer.writerow([value, bath, bath / value, 100 * value / bath])


if __name__ == "__main__":
    run(Path(sys.argv[1]), Path(sys.argv[2]))

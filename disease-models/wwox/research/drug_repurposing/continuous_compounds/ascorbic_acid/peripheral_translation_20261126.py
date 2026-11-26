"""Extract study measures from the open Verhamme 2009 article (PMID 19909499)."""
import csv
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

study = ET.parse(Path(sys.argv[1]))
assert study.findtext(".//article-id[@pub-id-type='pmid']") == "19909499"
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("table", "reported_measure", "placebo_reported", "ascorbate_reported",
                 "difference_with_CI_when_reported", "p_when_reported"))
for table in study.findall(".//table-wrap"):
    label = table.findtext("label")
    for row in table.findall(".//tr"):
        cells = [" ".join("".join(cell.itertext()).split()) for cell in row]
        if not cells or not cells[0].startswith("Median nerve MNCV (m/s)"):
            continue
        writer.writerow([label, *cells, *["NA"] * (5 - len(cells))])

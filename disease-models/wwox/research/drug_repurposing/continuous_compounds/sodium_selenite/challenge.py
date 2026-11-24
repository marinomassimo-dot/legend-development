"""Reproduce the two-point comparisons from the N27 neuronal study, Table 1."""
import csv
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

article = Path(sys.argv[1]).read_text()
section = article.split('id="Tab1"', 1)[1]
start = section.index("<table")
end = section.index("</table>", start) + len("</table>")
table = ET.fromstring(section[start:end])
header = ["".join(cell.itertext()).strip() for cell in table.find("thead/tr")]
selected = ["Selenite", "Selenate", "Selenomethionine", "Liproxstatin-1"]
out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
out.writerow(["challenge", "compound", "EC50_nM", "EC50_relative_to_selenite"])
for row in table.findall("tbody/tr"):
    values = ["".join(cell.itertext()).strip() for cell in row]
    assert len(header) == len(values)
    measurements = dict(zip(header, values))
    for compound in selected:
        value = int(measurements[compound])
        out.writerow([values[0], compound, value, f"{value / int(measurements['Selenite']):.2f}"])

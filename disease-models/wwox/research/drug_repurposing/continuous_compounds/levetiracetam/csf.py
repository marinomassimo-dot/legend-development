"""Summarize ventricular CSF measurements in Zampella et al., Table 2."""
import csv
from pathlib import Path
from statistics import median
import sys
import xml.etree.ElementTree as ET

MOLAR_MASS = 170.21  # levetiracetam, g/mol
REFERENCE_UM = 30  # Rigo et al., full reversal under the hippocampal zinc challenge
table, = (t for t in ET.parse(Path(sys.argv[1])).findall(".//table-wrap")
          if t.findtext("label") == "Table 2")
assert "levetiracetam" in "".join(table.find("caption").itertext()).lower()
patients = {}
for row in table.findall(".//tr")[1:]:
    cells = ["".join(c.itertext()).strip() for c in row]
    patient, sample = cells[0].split("-")
    series = patients.setdefault(patient, {})
    assert sample not in series
    series[sample] = float(cells[1])

assert len(patients) == 6 and all(set(s) == {"1", "2", "3"} for s in patients.values())
out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
out.writerow(["hours", "patients", "min_uM", "median_uM", "max_uM",
              "at_or_above_30uM", "at_or_above_30uM_after_baseline_subtraction"])
for sample, hours in [("1", 0), ("2", 1), ("3", 6)]:
    values = [s[sample] * 1000 / MOLAR_MASS for s in patients.values()]
    changes = [(s[sample] - s["1"]) * 1000 / MOLAR_MASS for s in patients.values()]
    out.writerow([hours, len(values), *[f"{n:.2f}" for n in (min(values), median(values), max(values))],
                  sum(n >= REFERENCE_UM for n in values), sum(n >= REFERENCE_UM for n in changes)])

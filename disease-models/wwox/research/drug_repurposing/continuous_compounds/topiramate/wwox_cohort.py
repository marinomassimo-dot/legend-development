"""Count trialled and underlined current topiramate entries in Oliver Table 2."""
import re
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

path = Path(sys.argv[1]) / "fulltext/PMID36779245_Oliver2023_PMC_2026-09-27.xml"
root = ET.parse(path)
table, = (t for t in root.findall(".//table-wrap") if t.findtext("label") == "TABLE 2")
rows = table.findall(".//tr")
arm, = (r for r in rows if "ASMs trialed" in "".join(r[0].itertext()))
assert "current" in "".join(arm[0].itertext()) and len(arm) == len(rows[0]) == 14
pattern = re.compile(r"\bTPM\b")
ever = current = 0
for cell in arm[1:]:
    ever += bool(pattern.search(" ".join(cell.itertext())))
    current += any(pattern.search(" ".join(element.itertext())) for element in cell.iter("underline"))
print("patients\tTPM_trialled\tTPM_underlined_current")
print(len(arm)-1, ever, current, sep="\t")

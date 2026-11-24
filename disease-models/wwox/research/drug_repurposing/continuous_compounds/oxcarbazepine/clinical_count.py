"""Count exposure and current-at-report status using Oliver Table 2's original markup."""
import csv
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

study = ET.parse(Path(sys.argv[1]))
table, = [t for t in study.findall(".//table-wrap") if t.findtext("label") == "TABLE 2"]
rows = {}
for row in table.findall(".//tr"):
    label, *cells = list(row)
    rows["".join(label.itertext()).strip()] = cells
meds = next(cells for label,cells in rows.items() if label.startswith("ASMs trialed"))
resistance = next(cells for label,cells in rows.items() if "resistant" in label)
assert len(meds) == len(resistance) == 13
out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
out.writerow(("table_column","OXC_listed","OXC_underlined_current","count_current_list_entries","drug_resistant_as_reported"))
for i,(c,r) in enumerate(zip(meds,resistance),1):
    all_names = [s.strip() for s in "".join(c.itertext()).split(",")]
    current = [s.strip() for e in c.iter("underline") for s in "".join(e.itertext()).split(",") if s.strip()]
    out.writerow((i,int("OXC" in all_names),int("OXC" in current),len(current),"".join(r.itertext()).strip()))

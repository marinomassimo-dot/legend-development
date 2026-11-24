"""Reproduce the two Table 1 contrasts from the two unmodified article XML files in the supplied directory."""
from pathlib import Path
from xml.etree import ElementTree
import csv
import sys

folder = Path(sys.argv[1])

def rows(pmid):
    table = ElementTree.parse(folder / f"{pmid}.xml").find(".//table-wrap")
    assert table.findtext("label").strip().lower().rstrip(".:") == "table 1"
    for row in table.findall(".//tr"):
        yield [" ".join("".join(cell.itertext()).split()).replace("‐", "-") for cell in row]

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(["PMID", "endpoint", "analyte", "compartment", "unit", "CLB_VPA", "CLB_VPA_STP", "fold"])
def report(pmid, endpoint, data, units):
    for analyte in ("CLB", "N-CLB"):
        for i, compartment in enumerate(("plasma", "brain")):
            before, after = [data[triple, analyte][i] for triple in (False, True)]
            writer.writerow([pmid, endpoint, analyte, compartment, units[i], before, after, f"{float(after)/float(before):.3f}"])

acute = {}
arm = ""
for row in rows("39212337"):
    if len(row) == 10:
        arm, *row = row
    if len(row) == 9 and row[0] in ("CLB", "N-CLB") and arm in ("Double (CLB+VPA)", "Triple (CLB+VPA+STP)"):
        acute[arm.startswith("Triple"), row[0]] = row[1], row[4]
report("39212337", "acute_total_AUC_0_inf_WT", acute, ["ug*h/mL", "ug*h/g"])

chronic = {}
for row in rows("40586768"):
    analyte = row[0].split()[0]
    if analyte in ("CLB", "N-CLB"):
        chronic["STP" in row[0], analyte] = row[2:4]
report("40586768", "day14_total_mean_Scn1a_A1783V_WT", chronic, ["ug/mL", "ug/g"])

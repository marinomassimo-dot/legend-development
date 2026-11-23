"""Summarize nonempty observations in Oberländer et al., Supplementary Data 2."""
import argparse
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile

import numpy as np

from learn_signature import write


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", type=Path)
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    args.out.mkdir(exist_ok=True, parents=True)
    with zipfile.ZipFile(args.workbook) as z:
        sheets = ET.fromstring(z.read("xl/workbook.xml")).findall(".//{*}sheet")
        assert sheets[3].get("name") == "Figure 5"
        page = ET.fromstring(z.read("xl/worksheets/sheet4.xml"))
        cells = {c.get("r"): float(c.findtext("{*}v")) for c in page.findall(".//{*}c")
                 if c.get("t") in (None, "n") and c.findtext("{*}v") is not None}
    rows = []
    def summary(panel, endpoint, condition, unit, column, first, last):
        values = [cells[f"{column}{i}"] for i in range(first,last+1) if f"{column}{i}" in cells]
        rows.append([panel,endpoint,condition,unit,len(values),np.mean(values),
                     np.std(values, ddof=1)/np.sqrt(len(values)),min(values),max(values)])
    for col,cond in zip("ABCD",["control","memantine_10uM","memantine_100uM","MK801_APV"]):
        summary("5A","induced_cell_death",cond,"percent",col,3,6)
    for i,endpoint in enumerate(["Inhba","Bdnf_exon_IV","Npas4","Nr4a1"]):
        for j,cond in enumerate(["memantine_10uM","memantine_100uM","MK801_APV"]):
            summary("5B",endpoint,cond,"percent_of_Bic",chr(65+3*i+j),12,15)
        first = 21 if i < 2 else 30
        for col,cond in zip("ABCDE" if i%2==0 else "HIJKL",["TTX","NMDA","TBOA","memantine_10uM_NMDA","memantine_10uM_TBOA"]):
            summary("5C",endpoint,cond,"percent_of_Bic",col,first,first+5)
    write(args.out/"figure5.tsv","panel endpoint condition unit n mean SEM min max",rows)


if __name__ == "__main__":
    main()

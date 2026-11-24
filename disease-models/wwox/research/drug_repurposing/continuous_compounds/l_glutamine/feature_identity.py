"""Cross-check fly Supplementary Table 4 with the MTBLS12344 public MAF JSON."""
import argparse
import csv
import json
import sys
import xml.etree.ElementTree as ET
from zipfile import ZipFile


def worksheet_rows(path):
    with ZipFile(path) as workbook:
        strings = ["".join(node.itertext()) for node in
                   ET.fromstring(workbook.read("xl/sharedStrings.xml"))]
        for name in workbook.namelist():
            if not name.startswith("xl/worksheets/sheet") or not name.endswith(".xml"):
                continue
            rows = ET.fromstring(workbook.read(name)).findall(".//{*}row")
            title = rows[0].find("{*}c")
            index = title.findtext("{*}v")
            if title.get("t") != "s" or not strings[int(index)].startswith("Supplementary Table 4."):
                continue
            for row in rows[4:]:
                values = {}
                for cell in row.findall("{*}c"):
                    value = cell.findtext("{*}v", "")
                    column = cell.get("r").rstrip("0123456789")
                    values[column] = strings[int(value)] if cell.get("t") == "s" else value
                yield values
            return
        raise ValueError("Knockdown metabolite table missing")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook")
    parser.add_argument("maf", help="MetaboLights API JSON response for the study's MAF")
    args = parser.parse_args()
    with open(args.maf, encoding="utf-8") as file:
        assignments = json.load(file)["data"]["rows"]
    selected = {"231", "791", "1665"}
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("peak", "mz", "rt_s", "paper_identity", "deposited_identity",
                     "deposited_reliability", "KD_adj_p", "KD_logFC", "KD_LacZ_logFC",
                     "KD_Abeta_logFC", "interaction_adj_p"))
    found = set()
    for row in worksheet_rows(args.workbook):
        if row.get("A") not in selected:
            continue
        mz, rt = float(row["B"]), float(row["C"])
        matches = [r for r in assignments if round(float(r["mass_to_charge"]), 4) == round(mz, 4)
                   and round(float(r["retention_time"]), 2) == round(rt, 2)]
        if len(matches) > 1 or row["A"] in found:
            raise ValueError("Ambiguous feature match")
        found.add(row["A"])
        hit = matches[0] if matches else {}
        writer.writerow((row["A"], f"{mz:.4f}", f"{rt:.2f}", row.get("E") or "unassigned",
                         hit.get("metabolite_identification", "unassigned"), hit.get("reliability", ""),
                         *(f"{float(row[col]):.8g}" for col in ("I", "J", "S", "R", "Q"))))
    if found != selected:
        raise ValueError("Incomplete feature comparison")


if __name__ == "__main__":
    main()

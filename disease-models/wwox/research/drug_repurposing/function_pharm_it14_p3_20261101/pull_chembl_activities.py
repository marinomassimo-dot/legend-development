#!/usr/bin/env python3
"""Public ChEMBL REST activities for a fixed list of molecule IDs; keeps rows with a numeric
standard_value, records assay description, target, organism, doc year and PMID. No aggregation.
Usage: pull_chembl_activities.py <out.tsv>"""
import json, sys, urllib.request, urllib.parse, time
BASE = "https://www.ebi.ac.uk/chembl/api/data/"
IDS = ["CHEMBL70418","CHEMBL2260842","CHEMBL1027","CHEMBL89598","CHEMBL41355","CHEMBL182066","CHEMBL1568698","CHEMBL5095264","CHEMBL696"]
def page(url):
    with urllib.request.urlopen(url, timeout=90) as r:
        return json.loads(r.read())
def main():
    if len(sys.argv) != 2 or sys.argv[1] in ("-h","--help"):
        print(__doc__); return 0 if len(sys.argv) > 1 else 2
    rows = []
    for cid in IDS:
        url = BASE + "activity.json?" + urllib.parse.urlencode({"molecule_chembl_id": cid, "limit": 200})
        n = 0
        while url and n < 10:
            d = page(url); n += 1
            for a in d["activities"]:
                if a.get("standard_value") is None: continue
                rows.append([cid, a.get("molecule_pref_name") or "", a.get("target_chembl_id") or "", a.get("target_pref_name") or "",
                             a.get("target_organism") or "", a.get("standard_type") or "", a.get("standard_relation") or "",
                             a.get("standard_value"), a.get("standard_units") or "", a.get("pchembl_value") or "",
                             (a.get("assay_description") or "").replace("\t"," ").replace("\n"," ")[:220], a.get("assay_type") or "",
                             a.get("document_chembl_id") or "", a.get("document_year") or "", a.get("activity_id")])
            nxt = d["page_meta"].get("next")
            url = ("https://www.ebi.ac.uk" + nxt) if nxt else None
            time.sleep(0.2)
    with open(sys.argv[1], "w", encoding="utf8") as fh:
        fh.write("molecule\tpref_name\ttarget\ttarget_name\torganism\ttype\trel\tvalue\tunits\tpchembl\tassay\tassay_type\tdocument\tyear\tactivity_id\n")
        for r in rows: fh.write("\t".join(str(x) for x in r) + "\n")
    print(len(rows), "rows")
    return 0
if __name__ == "__main__": sys.exit(main())

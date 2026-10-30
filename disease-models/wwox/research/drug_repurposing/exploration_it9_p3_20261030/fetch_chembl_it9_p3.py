#!/usr/bin/env python3
"""IT9 P3: fetch ChEMBL molecule + parent records for a list of CHEMBL ids (only ChEMBL ids are sent). Usage: fetch_chembl_it9_p3.py --ids ids.txt --out chembl_profile.tsv"""
import argparse, csv, json, sys, time, urllib.request, datetime
ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("--ids", required=True); ap.add_argument("--out", required=True); a = ap.parse_args()
ids = sorted({x.strip() for x in open(a.ids) if x.strip()})
BASE = "https://www.ebi.ac.uk/chembl/api/data/molecule.json?limit=100&molecule_chembl_id__in="
def get(batch):
    for t in range(4):
        try:
            with urllib.request.urlopen(BASE + ",".join(batch), timeout=60) as r: return json.load(r)["molecules"]
        except Exception as e:
            time.sleep(2 + 3 * t); err = e
    print("FAILED batch", batch[:2], err, file=sys.stderr); return None
rec = {}; failed = []
def run(idlist):
    for i in range(0, len(idlist), 40):
        b = idlist[i:i + 40]; m = get(b)
        if m is None: failed.extend(b); continue
        for x in m: rec[x["molecule_chembl_id"]] = x
run(ids)
parents = sorted({(x.get("molecule_hierarchy") or {}).get("parent_chembl_id") for x in rec.values()} - {None} - set(rec))
run(parents)
today = datetime.date.today().isoformat()
cols = ["chembl_id", "pref_name", "parent_chembl_id", "parent_pref_name", "max_phase", "molecule_type", "oral", "parenteral", "topical", "withdrawn_flag", "atc", "first_approval", "therapeutic_flag", "natural_product", "black_box_warning", "fetched", "state"]
with open(a.out, "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t"); w.writerow(cols)
    for i in ids:
        x = rec.get(i)
        if not x: w.writerow([i] + [""] * 14 + [today, "SERVICE_ERROR" if i in failed else "NOT_RETURNED"]); continue
        pid = (x.get("molecule_hierarchy") or {}).get("parent_chembl_id") or i; p = rec.get(pid, x)
        w.writerow([i, x.get("pref_name") or "", pid, p.get("pref_name") or "", p.get("max_phase") or "", x.get("molecule_type") or "", x.get("oral"), x.get("parenteral"), x.get("topical"), x.get("withdrawn_flag"),
                    ";".join(p.get("atc_classifications") or x.get("atc_classifications") or []), p.get("first_approval") or "", x.get("therapeutic_flag"), x.get("natural_product"), x.get("black_box_warning"), today, "OK"])
print(len(ids), "ids;", len(rec), "records;", len(failed), "failed", file=sys.stderr)

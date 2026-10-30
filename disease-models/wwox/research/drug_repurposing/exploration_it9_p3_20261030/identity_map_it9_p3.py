#!/usr/bin/env python3
"""IT9 P3 (Amendment 2): identity routes for the families in the P2 tables. Only compound names are sent to ChEMBL (exact-name lookups). Usage: identity_map_it9_p3.py --out identity_map.tsv"""
import argparse, csv, glob, gzip, json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path
H = Path(__file__).resolve().parent; D = H.parent
ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("--out", required=True); ap.add_argument("--pool", required=True); ap.add_argument("--no-name-lookup", action="store_true"); a = ap.parse_args()
fams = set()
for f in glob.glob(str(D / "generation_it9_p2_20261030/results/candidates_Q*.tsv")):
    fams |= {r["family_id"] for r in csv.DictReader(open(f), delimiter="\t")}
fams |= {r["family_id"] for r in csv.DictReader(open(a.pool), delimiter="\t")}
rec = {}
for l in gzip.open(D / "catalog/catalog.jsonl.gz", "rt"):
    r = json.loads(l); fid = "FAM:" + r["id"]
    if fid in fams: rec[fid] = r
recon = {}
for r in csv.DictReader(open(D / "catalog/ligand_reconciliation.tsv"), delimiter="\t"): recon[r["candidate"]] = r
def q(url):
    for t in range(3):
        try:
            with urllib.request.urlopen(url, timeout=40) as r: return json.load(r)["molecules"]
        except Exception as e: time.sleep(1 + 2 * t); err = e
    return None
from concurrent.futures import ThreadPoolExecutor
def lookup(nme):
    hits = set(); note = ""
    for fld in ("pref_name__iexact", "molecule_synonyms__molecule_synonym__iexact"):
        ms = q("https://www.ebi.ac.uk/chembl/api/data/molecule.json?limit=5&only=molecule_chembl_id,molecule_hierarchy&" + fld + "=" + urllib.parse.quote(nme))
        if ms is None: return None, "SERVICE_ERROR"
        hits |= {(x.get("molecule_hierarchy") or {}).get("parent_chembl_id") or x["molecule_chembl_id"] for x in ms}
    return hits, note
out = {}; todo = {}
for fid in sorted(fams):
    r = rec.get(fid); name = (r or {}).get("name", ""); route = "unresolved"; cid = ""; note = ""
    m = re.match(r"FAM:CAT:(CHEMBL\d+)$", fid)
    if m: route, cid = "catalogue_chembl", m.group(1)
    elif r:
        rc = recon.get(fid[4:]); ids = r.get("ids", {})
        if rc and rc["chembl_ref"] and rc["decision"] in ("merged", "out_of_selection") and rc.get("structure_check"): route, cid, note = "reconciliation_chembl", rc["chembl_ref"], "structure_check=" + rc["structure_check"]
        elif ids.get("chembl_from_dgidb_concept_not_enumerated"): route, cid = "dgidb_concept_chembl", ids["chembl_from_dgidb_concept_not_enumerated"][0]
        elif not a.no_name_lookup and name and not re.search(r"\[|\bcompound\b|inhibitor|antagonist|agonist|antibody|vaccine", name, re.I): todo[fid] = (ids.get("dgidb_drug_name") or name)
        else: note = "name pattern not looked up (code name / class name)"
    out[fid] = [fid, name, (r or {}).get("origin", ""), route, cid, note]
nm = len(todo)
with ThreadPoolExecutor(4) as ex: res = dict(zip(todo, ex.map(lookup, todo.values())))
for fid, (hits, note) in res.items():
    if hits is None: out[fid][5] = note
    elif len(hits) == 1: out[fid][3:6] = ["name_exact_unique", sorted(hits)[0], "identity UNVERIFIED (no structure check)"]
    elif len(hits) > 1: out[fid][5] = "name matches %d ChEMBL parents" % len(hits)
    else: out[fid][5] = "no exact name match"
out = [out[k] for k in sorted(out)]
with open(a.out, "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t"); w.writerow(["family_id", "name", "origin", "identity_route", "chembl_id", "note"]); w.writerows(out)
import collections; print(len(out), "families;", nm, "name lookups;", collections.Counter(x[3] for x in out), file=sys.stderr)

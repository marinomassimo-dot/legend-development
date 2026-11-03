#!/usr/bin/env python3
"""IT22 P4 batch2: ChEMBL REST molecule, mechanism and activities (grouped by target/type/unit, never pooled) for three compounds. No account, no contact string sent.
usage: collect_chembl_batch2.py run   (writes chembl_batch2_*.tsv next to this file)"""
import sys, json, time, urllib.request, urllib.parse, collections, statistics
from pathlib import Path
if len(sys.argv) < 2 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
HERE = Path(__file__).resolve().parent
C = "https://www.ebi.ac.uk/chembl/api/data"
cpds = {"IT21P2-0425": ("Epz004777", "CHEMBL2169919"), "IT21P2-0431": ("TAK-901", "CHEMBL3544932"), "IT21P2-1008": ("Tapinarof", "CHEMBL259571")}
def get(u, p=None):
    if p: u += "?" + urllib.parse.urlencode(p)
    for i in range(4):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"Accept": "application/json"}), timeout=90))
        except Exception as e:
            err = e; time.sleep(3)
    return {"error": str(err)}
def pages(u, key, p):
    out = []; p = dict(p, limit=1000, offset=0)
    while True:
        d = get(u, p)
        if "error" in d: return out, d["error"]
        out += d[key]
        if not d["page_meta"]["next"]: return out, "ok"
        p["offset"] += 1000
mol_rows, mech_rows, act_rows = [], [], []
for pid, (nm, cid) in cpds.items():
    m = get(C + f"/molecule/{cid}.json")
    mol_rows.append([pid, nm, cid, m.get("pref_name"), m.get("max_phase"), m.get("molecule_type"), m.get("first_approval"), (m.get("molecule_structures") or {}).get("standard_inchi_key"), m.get("chemical_probe"), m.get("black_box_warning"), m.get("oral"), m.get("topical"), m.get("parenteral")])
    mech, st = pages(C + "/mechanism.json", "mechanisms", {"molecule_chembl_id": cid})
    for x in mech: mech_rows.append([pid, nm, x["target_chembl_id"], x["mechanism_of_action"], x["action_type"], json.dumps([r.get("ref_id") for r in x.get("mechanism_refs", [])])])
    acts, st2 = pages(C + "/activity.json", "activities", {"molecule_chembl_id": cid})
    tids = sorted({a["target_chembl_id"] for a in acts if a.get("target_chembl_id")})
    tg = {}
    for i in range(0, len(tids), 40):
        d = get(C + "/target.json", {"target_chembl_id__in": ",".join(tids[i:i+40]), "limit": 100})
        for t in d.get("targets", []):
            tg[t["target_chembl_id"]] = (t["pref_name"], t["organism"], ";".join(sorted({c["component_synonym"] for comp in t["target_components"] for c in comp["target_component_synonyms"] if c["syn_type"] == "GENE_SYMBOL"})))
    g = collections.defaultdict(list)
    for a in acts:
        if a.get("standard_value") in (None, ""): continue
        g[(a.get("target_chembl_id"), a["standard_type"], a["standard_units"], a["standard_relation"] or "=")].append(a)
    for (t, ty, un, rel), L in sorted(g.items(), key=lambda kv: (str(kv[0][0]), kv[0][1])):
        v = [float(a["standard_value"]) for a in L]
        ti = tg.get(t, ("", "", ""))
        act_rows.append([pid, nm, t, ti[0], ti[2], ti[1], ty, rel, un, len(L), min(v), max(v), len({a["document_chembl_id"] for a in L}), ";".join(sorted({a["document_chembl_id"] for a in L})[:6]), ";".join(sorted({(a.get("assay_description") or "")[:90] for a in L})[:2])])
    print(pid, nm, "mech", len(mech), st, "acts", len(acts), st2, flush=True)
def w(f, h, rows):
    (HERE / f).write_text("\t".join(h) + "\n" + "".join("\t".join("" if c is None else str(c).replace("\t", " ").replace("\n", " ") for c in r) + "\n" for r in rows))
w("chembl_batch2_molecules.tsv", ["proposal", "name", "chembl_id", "pref_name", "max_phase", "type", "first_approval", "inchikey", "chemical_probe", "black_box", "oral", "topical", "parenteral"], mol_rows)
w("chembl_batch2_mechanism.tsv", ["proposal", "name", "target", "mechanism", "action_type", "refs"], mech_rows)
w("chembl_batch2_activities_by_target.tsv", ["proposal", "name", "target_id", "target_name", "genes", "organism", "type", "rel", "units", "n_rows", "min", "max", "n_docs", "docs", "assay_examples"], act_rows)

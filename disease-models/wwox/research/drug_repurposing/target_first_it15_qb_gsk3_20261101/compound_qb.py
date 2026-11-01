#!/usr/bin/env python3
"""IT15 Q-B step 3: compound-level pulls through framework/adapters/chembl.py (mechanism + molecule activities), with the retry rule and perimeter log.
Usage: compound_qb.py --raw DIR --names "tideglusib,TDZD-8,..."   (identity search)   |   --mols CHEMBL..,CHEMBL..  (activities, mechanism)"""
import sys, os, json, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import retrieve_qb as R
from framework.adapters import chembl
def fetch(url): return R.get(url, "compound")
ap = argparse.ArgumentParser(); ap.add_argument("--raw", required=True); ap.add_argument("--names", default=""); ap.add_argument("--mols", default="")
a = ap.parse_args()
for n in [x for x in a.names.split(",") if x]:
    o = chembl.query({"drug": n}, fetch=fetch)
    json.dump(o, open(os.path.join(a.raw, "name_" + n.replace(" ", "_").replace("/", "_") + ".json"), "w"))
    print("NAME", n, o["status"], o.get("error", "")[:60], [(h.get("molecule_chembl_id"), h.get("pref_name"), h.get("action_type"), h.get("target_chembl_id")) for h in o["hits"]][:4], str(o.get("nearest"))[:150])
for m in [x for x in a.mols.split(",") if x]:
    o = chembl.query({"molecule": m, "types": ["IC50", "Ki", "Kd"], "max_rows": 2000}, fetch=fetch)
    json.dump(o, open(os.path.join(a.raw, "mol_" + m + ".json"), "w"))
    print("MOL", m, o["status"], o.get("total_count"), o.get("retrieved"), o.get("truncated"), o.get("error", "")[:80], o.get("note", "")[:100])
    mo = chembl.query({"drug": m}, fetch=fetch) if False else None

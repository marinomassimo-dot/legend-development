#!/usr/bin/env python3
"""IT15 Q-B step 5: target-first MECHANISM lists (ChEMBL mechanism endpoint) for the GSK3 targets, and the Axin-1/GSK3B PPI target activity census."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import retrieve_qb as R
RAW = sys.argv[1]; B = R.BASE
out = {}
for t in ("CHEMBL262", "CHEMBL2850", "CHEMBL2095188", "CHEMBL3883309", "CHEMBL3669", "CHEMBL1075321"):
    st, p = R.get(f"{B}/mechanism.json?target_chembl_id={t}&limit=100", "mech:" + t)
    out["mech_" + t] = {"http": st, "rows": [(m["molecule_chembl_id"], m.get("action_type"), m.get("mechanism_of_action"), [r.get("ref_id") for r in m.get("mechanism_refs", [])][:3]) for m in p.get("mechanisms", [])] if isinstance(p, dict) else None}
st, p = R.get(f"{B}/activity.json?target_chembl_id=CHEMBL3883309&limit=200", "acts:CHEMBL3883309")
out["axin_gsk3b_ppi_acts"] = {"http": st, "total": (p.get("page_meta") or {}).get("total_count") if isinstance(p, dict) else None,
    "rows": [(a["molecule_chembl_id"], a.get("molecule_pref_name"), a["standard_type"], a["standard_relation"], a["standard_value"], a["standard_units"], a["document_chembl_id"], a["assay_description"][:160]) for a in p.get("activities", [])] if isinstance(p, dict) else None}
json.dump(out, open(os.path.join(RAW, "mechanism_lists.json"), "w"), indent=1)
for k, v in out.items(): print(k, v.get("http"), (len(v["rows"]) if v.get("rows") is not None else None), v.get("total", ""))

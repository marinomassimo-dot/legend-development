#!/usr/bin/env python3
"""ChEMBL bioactivity measurements per resolved target (single-protein targets), top by pchembl_value, plus a name
lookup for the named tool compounds. Key-less, same door as the adapters. Output chembl_activities.tsv.
A pchembl value is a potency in a stated assay, not efficacy and not a statement about WWOX."""
import json, sys, time
from urllib.parse import quote
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "framework" / "adapters"))
import _http
BASE = "https://www.ebi.ac.uk/chembl/api/data"
HERE = Path(__file__).resolve().parent
T = {"LDHA":"CHEMBL4835","LDHB":"CHEMBL4940","PDK1":"CHEMBL4766","PDK2":"CHEMBL3861","PDK3":"CHEMBL3893","PDK4":"CHEMBL4141",
     "PERK":"CHEMBL6030","GCN2":"CHEMBL5358","EIF2B2":"CHEMBL6067331","EIF2B5":"CHEMBL5725120","EIF2B4":"CHEMBL6067328","EIF2B3":"CHEMBL4295961",
     "MCT1":"CHEMBL4360"}
def get(u):
    time.sleep(0.4); return _http.get_json(u, timeout=40)
rows = ["target\ttarget_id\tmolecule_chembl_id\tpref_name\tmax_phase\ttype\trelation\tvalue\tunits\tpchembl\tassay_type\tassay_description\tdoc_chembl_id"]
seen_counts = {}
for lab, tid in T.items():
    st, a = get(f"{BASE}/activity.json?target_chembl_id={tid}&pchembl_value__isnull=false&order_by=-pchembl_value&limit=25")
    acts = (a.get("activities") if isinstance(a, dict) else None) or []
    seen_counts[lab] = {"http": st, "returned": len(acts), "total_with_pchembl": (a.get("page_meta") or {}).get("total_count") if isinstance(a, dict) else None}
    for x in acts:
        rows.append("\t".join(str(v) for v in [lab, tid, x.get("molecule_chembl_id"), x.get("molecule_pref_name") or "", "", x.get("standard_type"),
            x.get("standard_relation"), x.get("standard_value"), x.get("standard_units"), x.get("pchembl_value"), x.get("assay_type"),
            (x.get("assay_description") or "").replace("\t"," ")[:120], x.get("document_chembl_id")]))
(HERE / "chembl_activities.tsv").write_text("\n".join(rows) + "\n")
names = ["stiripentol","ISRIB","trazodone","dibenzoylmethane","fosigotifator","GSK2837808A","FX11","oxamate","galloflavin","gossypol","sephin1","guanabenz",
         "salubrinal","GSK2606414","dichloroacetate","AZD7545","diazoxide","vigabatrin","oxamic acid","NHI-2","GNE-140","AZD3965","isosafrole","valproic acid"]
out = ["query_name\tmolecule_chembl_id\tpref_name\tmax_phase\tn_hits_total"]
for n in names:
    st, m = get(f"{BASE}/molecule/search.json?q={quote(n)}&limit=3")
    ms = (m.get("molecules") if isinstance(m, dict) else None) or []
    out.append("\t".join([n, ";".join(x["molecule_chembl_id"] for x in ms), ";".join(str(x.get("pref_name")) for x in ms), ";".join(str(x.get("max_phase")) for x in ms), str((m.get("page_meta") or {}).get("total_count") if isinstance(m, dict) else st)]))
(HERE / "chembl_name_lookup.tsv").write_text("\n".join(out) + "\n")
print(json.dumps(seen_counts))

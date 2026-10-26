#!/usr/bin/env python3
"""ChEMBL activity rows for NAMED candidate compounds (ids from chembl_name_lookup.tsv), all targets, pchembl or not:
what ChEMBL actually holds as a measurement for stiripentol, GSK2837808A, FX11, oxamate, ISRIB, fosigotifator, DCA, trazodone.
Output chembl_named_activities.tsv. Potency in a stated assay only."""
import sys as _sys
if any(a in ("-h", "--help") for a in _sys.argv[1:]):  # a documented command must answer --help without touching the network or any file
    print(__doc__)
    raise SystemExit(0)

import json, sys, time
from pathlib import Path
from urllib.parse import quote
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "framework" / "adapters"))
import _http
BASE = "https://www.ebi.ac.uk/chembl/api/data"; HERE = Path(__file__).resolve().parent
M = {"stiripentol":"CHEMBL1983350","GSK2837808A":"CHEMBL3335794","FX11":"CHEMBL126519","oxamate":"CHEMBL15976","ISRIB":"CHEMBL4303573",
     "fosigotifator":"CHEMBL5315045","DCA":"CHEMBL306823","trazodone":"CHEMBL621","AZD7545":"CHEMBL3392645","GSK2606414":"CHEMBL2171124","AZD3965":"CHEMBL3335793","guanabenz":"CHEMBL420"}
rows=["compound\tmolecule\ttarget_chembl_id\ttarget_name\ttype\trel\tvalue\tunits\tassay_description\tdoc"]
cnt={}
for n,mid in M.items():
    time.sleep(0.4)
    st,a=_http.get_json(f"{BASE}/activity.json?molecule_chembl_id={mid}&limit=200", timeout=40)
    acts=(a.get("activities") if isinstance(a,dict) else None) or []
    cnt[n]={"http":st,"rows":len(acts),"total":(a.get("page_meta") or {}).get("total_count") if isinstance(a,dict) else None}
    for x in acts:
        if x.get("standard_type") in ("IC50","Ki","Kd","EC50","Potency","Inhibition") or True:
            rows.append("\t".join(str(v) for v in [n,mid,x.get("target_chembl_id"),x.get("target_pref_name"),x.get("standard_type"),x.get("standard_relation"),x.get("standard_value"),x.get("standard_units"),(x.get("assay_description") or "").replace("\t"," ")[:110],x.get("document_chembl_id")]))
(HERE/"chembl_named_activities.tsv").write_text("\n".join(rows)+"\n"); print(json.dumps(cnt))

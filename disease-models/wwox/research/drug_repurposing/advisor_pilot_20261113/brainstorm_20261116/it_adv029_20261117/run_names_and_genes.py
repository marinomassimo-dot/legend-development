import sys, json
sys.path.insert(0,"/home/desktop/legend-development")
from framework.adapters import chembl, _http
f=_http.make_fetch("/tmp/it56_adv029/cache", retries=2, pause=6.0)
out=[]
for g in ["LDHA","LDHB","SLC2A1","PDHA1","DLAT","LIAS"]:
    r=chembl.query({"gene":g},fetch=f)
    out.append({"q":"gene "+g,"status":r["status"],"hits":[(h["target_chembl_id"],h["pref_name"],h["organism"],h["target_type"]) for h in r.get("hits",[])][:8]})
for n in ["GSK2837808A","GNE-140","FX11","oxamate","galloflavin","BAY-876","WZB117","STF-31","fasentin","phloretin","devimistat","CPI-613"]:
    r=chembl.query({"drug":n},fetch=f)
    out.append({"q":"drug "+n,"status":r["status"],"hits":[(h.get("molecule_chembl_id"),h.get("pref_name"),h.get("max_phase"),h.get("action_type"),h.get("mechanism_of_action"),h.get("target_chembl_id")) for h in r.get("hits",[])][:4],"nearest":[(h["molecule_chembl_id"],h["pref_name"]) for h in r.get("nearest",[])][:3]})
json.dump(out,open("/tmp/it56_adv029/batch1.json","w"),indent=1)
for o in out: print(json.dumps(o)[:420])
print("failures",f.failures[:3] if hasattr(f,"failures") else None, f.stats)

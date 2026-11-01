import json,sys,time
from g import get
def pull(q,tag):
    off=0; out=[]
    while True:
        p=get(f"/assay.json?description__icontains={q}&limit=1000&offset={off}")
        if p is None: print("INCOMPLETE",q,off); return out,False
        out+=p["assays"]; off+=len(p["assays"])
        if not p["page_meta"].get("next"): break
    json.dump(out,open(f"../raw/assay_{tag}.json","w")); print(q,len(out)); return out,True
for q,t in (("tau","tau"),("catenin","cat"),("wnt","wnt"),("topflash","top"),("tcf","tcf")):
    pull(q,t)

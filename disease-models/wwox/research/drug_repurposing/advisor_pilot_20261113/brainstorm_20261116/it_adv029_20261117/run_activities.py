import sys, json, collections
sys.path.insert(0,"/home/desktop/legend-development")
from framework.adapters import chembl, _http
f=_http.make_fetch("/tmp/it56_adv029/cache", retries=2, pause=6.0)
res={}
for tag,req in [("LDHA human CHEMBL4835",{"target":"CHEMBL4835","max_rows":2000}),
                ("SLC2A1 human CHEMBL2535",{"target":"CHEMBL2535","max_rows":2000}),
                ("PDHA1 human CHEMBL2092",{"target":"CHEMBL2092","max_rows":2000}),
                ("DLAT human CHEMBL4523180",{"target":"CHEMBL4523180","max_rows":2000}),
                ("BAY-876 any target",{"molecule":"CHEMBL4448899","max_rows":400}),
                ("CPI-613 any target",{"molecule":"CHEMBL3186849","max_rows":400})]:
    r=chembl.query(req,fetch=f)
    hs=r.get("hits",[])
    res[tag]={"status":r["status"],"coverage":r.get("coverage"),"total":r.get("total_count"),"retrieved":r.get("retrieved"),"rows":hs}
    print("##",tag,r["status"],r.get("coverage"),r.get("total_count"),r.get("retrieved"))
json.dump(res,open("/tmp/it56_adv029/act.json","w"),default=str)
print(f.stats, f.failures[:2])

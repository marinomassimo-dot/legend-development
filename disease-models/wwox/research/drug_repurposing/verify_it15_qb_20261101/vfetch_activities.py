import urllib.request, json, time, sys, os
RAW="/tmp/claude-1000/-home-desktop-legend-development/4325d70d-8bea-4789-8046-d7a9ee74c97f/scratchpad/raw"
B="https://www.ebi.ac.uk/chembl/api/data"
def get(url):
    for a in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={"Accept":"application/json"}),timeout=60) as r:
                return json.load(r)
        except Exception as e:
            print("fail",a,url[-80:],str(e)[:60],flush=True); time.sleep(6)
    return None
tid=sys.argv[1]; lim=200; off=0; rows=[]
while True:
    p=get(f"{B}/activity.json?target_chembl_id={tid}&standard_type__in=IC50,Ki,Kd&limit={lim}&offset={off}")
    if p is None: print("STOP",off); break
    pg=p["activities"]; rows+=pg; off+=len(pg); tot=p["page_meta"]["total_count"]
    if not pg or not p["page_meta"].get("next"): break
json.dump({"total":tot,"rows":rows,"complete":len(rows)>=tot},open(f"{RAW}/acts_{tid}_v.json","w"))
print(tid,tot,len(rows),len(set(r['activity_id'] for r in rows)))

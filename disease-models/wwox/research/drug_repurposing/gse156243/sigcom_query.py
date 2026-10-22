#!/usr/bin/env python3
"""POST one declared gene set to SigCom LINCS enrich/ranktwosided; store the ORIGINAL response bytes + headers verbatim.
Usage: sigcom_query.py <set name S0..S3> <database> <limit>"""
import json,sys,urllib.request,datetime,hashlib
name,db,limit=sys.argv[1],sys.argv[2],int(sys.argv[3])
sets=json.load(open('derived/query_sets.json'))[name]
mp=json.load(open('derived/sigcom_entity_map.json'))['map']
body={"up_entities":[mp[g] for g in sets['up'] if g in mp],"down_entities":[mp[g] for g in sets['down'] if g in mp],"limit":limit,"database":db}
req=urllib.request.Request('https://data-api.sigcom-lincs.k8s.maayanlab.cloud/v1/api/v1/enrich/ranktwosided',json.dumps(body).encode(),{'Content-Type':'application/json'})
t=datetime.datetime.now(datetime.timezone.utc).isoformat()
r=urllib.request.urlopen(req,timeout=600); raw=r.read()
tag=f"{name}_sigcom_ranktwosided"
open(f'tool_responses/{tag}_response.json','wb').write(raw)
json.dump({'utc':t,'final_url':r.geturl(),'status':r.status,'headers':dict(r.headers),'request_body_counts':{'up':len(body['up_entities']),'down':len(body['down_entities'])},'database':db,'limit':limit,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)},open(f'tool_responses/{tag}_meta.json','w'),indent=1)
json.dump(body,open(f'tool_responses/{tag}_request.json','w'))
print(len(raw),raw[:300])

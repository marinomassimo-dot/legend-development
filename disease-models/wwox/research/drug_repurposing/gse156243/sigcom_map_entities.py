#!/usr/bin/env python3
"""Map HGNC symbols to SigCom LINCS gene entity UUIDs via the key-less metadata API (symbol or ensembl id).
Usage: sigcom_map_entities.py <derived/query_sets.json> <out json>"""
import json,sys,urllib.request,urllib.parse
sets=json.load(open(sys.argv[1]))
genes=sorted({g for s in sets.values() for v in s.values() for g in v})
B='https://maayanlab.cloud/sigcom-lincs/metadata-api/entities?filter='
m={}
for i in range(0,len(genes),150):
    ch=genes[i:i+150]
    f={"where":{"meta.symbol":{"inq":ch}},"fields":["id","meta.symbol"],"limit":1000}
    r=json.load(urllib.request.urlopen(B+urllib.parse.quote(json.dumps(f)),timeout=120))
    for e in r: m[e['meta']['symbol']]=e['id']
json.dump({'n_requested':len(genes),'n_mapped':len(m),'unmapped':[g for g in genes if g not in m],'map':m},open(sys.argv[2],'w'),indent=0)
print(len(genes),len(m))

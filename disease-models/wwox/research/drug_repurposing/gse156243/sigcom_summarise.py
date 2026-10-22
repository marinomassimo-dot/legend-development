#!/usr/bin/env python3
"""Fetch signature metadata (key-less metadata API) for every returned uuid, store verbatim, and summarise reversers per declared rules."""
import json,urllib.request,urllib.parse,collections
runs=['S1','S2','S3','S0'];meta={};R={}
for s in runs:
    R[s]=[x for x in json.load(open(f'tool_responses/{s}_sigcom_ranktwosided_response.json'))['results'] if x['type']=='reversers']
ids=sorted({x['uuid'] for s in runs for x in R[s]})
B='https://maayanlab.cloud/sigcom-lincs/metadata-api/signatures?filter='
raw=[]
for i in range(0,len(ids),100):
    f={"where":{"id":{"inq":ids[i:i+100]}},"limit":200}
    raw+=json.load(urllib.request.urlopen(B+urllib.parse.quote(json.dumps(f)),timeout=120))
json.dump(raw,open('tool_responses/signature_metadata_for_returned_uuids.json','w'))
for e in raw: meta[e['id']]=e['meta']
out={}
for s in runs:
    rows=sorted(R[s],key=lambda x:x['z-sum'])  # most negative z-sum = strongest reverser
    out[s]=[(r['uuid'],r['z-sum'],r['fdr-up'],r['fdr-down'],meta[r['uuid']]['pert_name'],meta[r['uuid']]['cell_line'],meta[r['uuid']]['pert_dose'],meta[r['uuid']]['pert_time']) for r in rows]
with open('derived/sigcom_reverser_summary.tsv','w') as f:
    f.write('set\trank\tpert_name\tcell_line\tdose\ttime\tz_sum\tfdr_up\tfdr_down\n')
    for s in runs:
        for i,r in enumerate(out[s]): f.write(f'{s}\t{i+1}\t{r[4]}\t{r[5]}\t{r[6]}\t{r[7]}\t{r[1]:.3f}\t{r[2]:.3g}\t{r[3]:.3g}\n')
top=lambda s,n:[o[4] for o in out[s][:n]]
print('S1 top25:',[(o[4],o[5]) for o in out['S1'][:25]])
for s in runs:
    cl=collections.defaultdict(set)
    for o in out[s]: cl[o[4]].add(o[5])
    print(s,'recurrent(>=3 cell lines in top100):',{k:len(v) for k,v in cl.items() if len(v)>=3})
    print(s,'distinct compounds in top100',len(cl),'overlap top25 with S1',len(set(top(s,25))&set(top('S1',25))),'n compounds top100 shared with S1:',len(set(top(s,100))&set(top('S1',100))))

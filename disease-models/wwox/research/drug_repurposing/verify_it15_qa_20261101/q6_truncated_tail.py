#!/usr/bin/env python3
"""Verifier item 6: read the rows beyond the 2000-row cap for the three truncated queries.
Public ChEMBL GET only. Retries: at most 2 per request. Outputs q6_tail_rows.tsv and q6_tail_summary.tsv"""
import json, time, urllib.request, os, collections
OUT=os.path.dirname(os.path.abspath(__file__))
def get(u):
    for a in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'Accept':'application/json'}),timeout=90))
        except Exception as e: err=str(e); time.sleep(4)
    return {'_error':err}
rows=[]; summ=[]
for t in ['CHEMBL1904','CHEMBL1907603','CHEMBL1907608']:
    base=f'https://www.ebi.ac.uk/chembl/api/data/activity.json?target_chembl_id={t}&standard_type=IC50'
    first=get(base+'&limit=1')
    if '_error' in first: summ.append([t,'NOT_VERIFIED',first['_error']]); continue
    total=first['page_meta']['total_count']; got=0
    for off in range(2000,total,500):
        d=get(base+f'&limit=500&offset={off}')
        if '_error' in d: summ.append([t,'PARTIAL_NOT_VERIFIED',f'offset {off}: '+d['_error']]); break
        for a in d['activities']:
            got+=1
            rows.append([t,a['activity_id'],a['molecule_chembl_id'],a.get('molecule_pref_name'),a['document_chembl_id'],a['assay_chembl_id'],a['standard_type'],a['standard_relation'],a['standard_value'],a['standard_units'],a.get('assay_description','')[:160],a.get('target_organism')])
    summ.append([t,'total_count_now=%d'%total,'tail_rows_read=%d'%got])
with open(f'{OUT}/q6_tail_rows.tsv','w') as f:
    f.write('target\tactivity_id\tmolecule\tpref_name\tdocument\tassay\ttype\trel\tvalue\tunits\tassay_description\torganism\n')
    for r in rows: f.write('\t'.join('' if x is None else str(x) for x in r)+'\n')
with open(f'{OUT}/q6_tail_summary.tsv','w') as f:
    for r in summ: f.write('\t'.join(map(str,r))+'\n')
print(summ)

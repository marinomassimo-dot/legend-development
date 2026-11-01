#!/usr/bin/env python3
"""Verifier item 8: ChEMBL mechanism records for NMDAR drugs (public GET, 2 retries)."""
import json, time, urllib.request, os
OUT=os.path.dirname(os.path.abspath(__file__))
M={'memantine':'CHEMBL807','ketamine':'CHEMBL742','esketamine':'CHEMBL395091','dextromethorphan':'CHEMBL52440','amantadine':'CHEMBL660','dizocilpine':'CHEMBL284237','ifenprodil':'CHEMBL305187','traxoprodil':'CHEMBL17350','radiprodil':'CHEMBL182066','rislenemdaz':'CHEMBL3545350'}
def get(u):
    for a in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'Accept':'application/json'}),timeout=40))
        except Exception as e: err=str(e); time.sleep(3)
    return {'_error':err}
with open(f'{OUT}/q8_mechanism.tsv','w') as f:
    f.write('drug\tchembl_id\taction_type\tmechanism_of_action\ttarget_chembl_id\tdirect_interaction\tmechanism_comment\tselectivity_comment\tbinding_site_comment\tmech_refs\n')
    for n,i in M.items():
        d=get(f'https://www.ebi.ac.uk/chembl/api/data/mechanism.json?molecule_chembl_id={i}&limit=50')
        if '_error' in d: f.write(f'{n}\t{i}\tNOT_VERIFIED\t{d["_error"]}\n'); continue
        if not d['mechanisms']: f.write(f'{n}\t{i}\tNO_MECHANISM_RECORD\n')
        for m in d['mechanisms']:
            f.write('\t'.join(str(x) for x in [n,i,m['action_type'],m['mechanism_of_action'],m['target_chembl_id'],m['direct_interaction'],m['mechanism_comment'],m['selectivity_comment'],m['binding_site_comment'],';'.join(r['ref_type']+':'+r['ref_id'] for r in m.get('mechanism_refs',[]))])+'\n')
print(open(f'{OUT}/q8_mechanism.tsv').read())

#!/usr/bin/env python3
"""Verifier IT15 Q-A item 4: for the queue compounds the producer called 'not found', look them up in ChEMBL by
molecule_chembl_id taken from deepening_queue.tsv, then pull mechanism records and NMDAR-target activities.
Public GET only, no e-mail, at most 2 retries per request. Output: q4_chembl_queue.tsv and raw/q4_*.json"""
import json, sys, time, urllib.request, urllib.parse, os
OUT = os.path.dirname(os.path.abspath(__file__))
IDS = {'acamprosate':'CHEMBL1201293','AV-101':'CHEMBL3545351','AZD8108':'CHEMBL3707355','delucemine':'CHEMBL2106165',
       'indantadol':'CHEMBL3707400','neramexane':'CHEMBL2106798','ralfinamide':'CHEMBL2107771','felbamate':'CHEMBL1094'}
NMDA_T = {'CHEMBL1904','CHEMBL1972','CHEMBL1907603','CHEMBL1907604','CHEMBL1907608','CHEMBL2015','CHEMBL2591','CHEMBL4109'}
def get(url):
    for a in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'Accept':'application/json'}), timeout=40) as r:
                return json.load(r)
        except Exception as e:
            err = str(e); time.sleep(3)
    return {'_error': err}
rows = []
for name, mid in IDS.items():
    mol = get(f'https://www.ebi.ac.uk/chembl/api/data/molecule/{mid}.json')
    json.dump(mol, open(f'{OUT}/raw/q4_mol_{mid}.json','w'))
    mech = get(f'https://www.ebi.ac.uk/chembl/api/data/mechanism.json?molecule_chembl_id={mid}&limit=100')
    json.dump(mech, open(f'{OUT}/raw/q4_mech_{mid}.json','w'))
    act = get(f'https://www.ebi.ac.uk/chembl/api/data/activity.json?molecule_chembl_id={mid}&limit=1000')
    json.dump(act, open(f'{OUT}/raw/q4_act_{mid}.json','w'))
    if '_error' in mol:
        rows.append([name, mid, 'NOT_VERIFIED', mol['_error'], '', '', '', '', '']); continue
    syn = sorted({s['molecule_synonym'] for s in mol.get('molecule_synonyms', [])})
    ik = (mol.get('molecule_structures') or {}).get('standard_inchi_key')
    mechs = [(m.get('mechanism_of_action'), m.get('action_type'), m.get('target_chembl_id')) for m in mech.get('mechanisms', [])] if '_error' not in mech else 'ERR '+mech['_error']
    acts = act.get('activities', []) if '_error' not in act else None
    nm = [(a['target_chembl_id'], a['standard_type'], a['standard_relation'], a['standard_value'], a['standard_units']) for a in acts if a.get('target_chembl_id') in NMDA_T] if acts is not None else 'ERR '+act['_error']
    rows.append([name, mid, mol.get('pref_name'), mol.get('max_phase'), ik, '; '.join(syn)[:200], json.dumps(mechs), (act.get('page_meta') or {}).get('total_count') if acts is not None else 'ERR', json.dumps(nm)])
with open(f'{OUT}/q4_chembl_queue.tsv','w') as f:
    f.write('queue_name\tchembl_id\tpref_name\tmax_phase\tinchikey\tsynonyms\tmechanisms(text,action,target)\tn_activities_total\tnmdar_target_activities\n')
    for r in rows: f.write('\t'.join(str(x) for x in r)+'\n')
print(open(f'{OUT}/q4_chembl_queue.tsv').read())

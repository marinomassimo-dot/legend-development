#!/usr/bin/env python3
"""Apply needs_patch_proposal.json to a SCRATCH copy of needs.json and run check_needs.py on it (nothing in the repository is edited).
Usage: python3 -I apply_and_check_patch.py --repo-root ROOT --out SCRATCH_NEEDS.json"""
import json,argparse,subprocess,sys,copy
ap=argparse.ArgumentParser(); ap.add_argument('--repo-root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
R=a.repo_root+'/disease-models/wwox/research/drug_repurposing/'
n=json.load(open(R+'needs/needs.json')); p=json.load(open(R+'axis_it10_p22_20261031/needs_patch_proposal.json'))
by={x['id']:x for x in n['needs']}
for op in p['ops']:
    if op['op']=='replace_observed_statement':
        o=[x for x in by[op['need']]['observed'] if x['id']==op['observation']][0]; o['statement']=op['new_statement']; o['limits']+=op['new_limits_append']
    elif op['op']=='add_counter_evidence': by[op['need']]['counter_evidence'].append(op['text'])
    elif op['op']=='add_need': n['needs'].append(op['need'])
json.dump(n,open(a.out,'w'),indent=1,ensure_ascii=False)
r=subprocess.run([sys.executable,'-I',R+'needs/check_needs.py','--file',a.out],capture_output=True,text=True); print(r.stdout[-1500:],r.stderr[-800:]); print('exit',r.returncode)

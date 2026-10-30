#!/usr/bin/env python3
"""Apply needs_patch_proposal.json to a SCRATCH copy of needs.json and run check_needs.py on it (nothing in the repository is edited).
Usage: python3 -I apply_and_check_patch.py --repo-root ROOT --out SCRATCH_NEEDS.json   (--help prints this)"""
import json, argparse, subprocess, sys
ap = argparse.ArgumentParser(description=__doc__); ap.add_argument('--repo-root', required=True); ap.add_argument('--out', required=True); a = ap.parse_args()
R = a.repo_root + '/disease-models/wwox/research/drug_repurposing/'
n = json.load(open(R + 'needs/needs.json')); p = json.load(open(R + 'question_it11_p22_20261031/needs_patch_proposal.json'))
by = {x['id']: x for x in n['needs']}
for op in p['ops']:
    k = op['op']
    if k == 'append_observation_limits':
        o = [x for x in by[op['need']]['observed'] if x['id'] == op['observation']][0]; o['limits'] += op['append']
    elif k == 'add_observation': by[op['need']]['observed'].append(op['observation'])
    elif k == 'add_counter_evidence': by[op['need']]['counter_evidence'].append(op['text'])
    elif k == 'replace_intervention_direction_do_not_assume': by[op['need']]['intervention_direction']['do_not_assume'] = op['new']
    elif k == 'add_card_pointer_after_card_exists': pass
json.dump(n, open(a.out, 'w'), indent=1, ensure_ascii=False)
r = subprocess.run([sys.executable, '-I', R + 'needs/check_needs.py', '--file', a.out], capture_output=True, text=True)
print(r.stdout[-1500:], r.stderr[-800:]); print('exit', r.returncode)
sys.exit(r.returncode)

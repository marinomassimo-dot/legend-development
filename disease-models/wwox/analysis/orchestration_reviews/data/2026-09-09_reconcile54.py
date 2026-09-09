#!/usr/bin/env python3
"""Reconcile the operator's 54-PMID Aqeilan list against the ledger, manifests and queue.
Re-runnable: every column is derived, none is typed by hand."""
import json, glob, os, collections, subprocess, sys
ROOT='/root/legend-development'
SP=os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
L=open(f'{SP}/pmids54.txt').read().split()
assigned=set()
for f in glob.glob('ledger/tasks/scientist-*/AQEILAN-FT-*.json'):
    d=json.load(open(f))
    for x in d['SCOPE']['assigned_pmids']: assigned.add(str(x))
owner={}
for f in glob.glob('ledger/tasks/scientist-*/AQEILAN-FT-*.json'):
    d=json.load(open(f))
    for x in d['SCOPE']['assigned_pmids']: owner[str(x)]=d['ACTOR_ID']

recs=[json.loads(l) for l in open('disease-models/wwox/registries/fulltext_read_receipts.jsonl') if l.strip()]
before=collections.defaultdict(list); today=collections.defaultdict(list)
for r in recs:
    p=str((r.get('study_id') or {}).get('pmid'))
    (today if (r.get('event_at') or '').startswith('2026-09-09') else before)[p].append(r)
def depth(rs):
    d={x.get('evidence_depth') for x in rs}
    if 'complete_fulltext_read' in d: return 'complete'
    if 'partial_fulltext_read' in d: return 'partial'
    return sorted(d)[0] if d else 'none'

ep={}
for l in open(f'{SP}/ep31.jsonl'):
    if l.startswith('{'):
        d=json.loads(l)
        if 'artifacts' in d:
            ep[d['pmid']]=(sum(1 for a in d['artifacts'] if a['state']=='PRESENT'), len(d['artifacts']))
drift={}
cur=None
for line in open(f'{SP}/drift31.txt'):
    if line.startswith('### '): cur=line[4:].strip()
    elif 'FLAG DRIFT' in line: drift[cur]=line.strip()

man={os.path.basename(f)[4:-5] for f in glob.glob('disease-models/wwox/research/deepdive_manifests/PMID*.json')}
cands=collections.defaultdict(list)
for f in glob.glob('disease-models/wwox/research/commit_candidates/*.md'):
    b=os.path.basename(f)
    for p in L:
        if p in b: cands[p].append(b)
doss={os.path.basename(f)[4:-3] for f in glob.glob('disease-models/wwox/research/fulltext_dossiers/PMID*.md')}

rows=[]
for p in L:
    b, t = before.get(p,[]), today.get(p,[])
    rows.append(dict(
        pmid=p,
        set=('23 assegnati' if p in assigned else '31 esclusi'),
        owner=owner.get(p,'-'),
        state_before=depth(b),
        state_now=depth(b+t),
        receipts_before=len(b), receipts_today=len(t),
        receipt_ids=[x.get('event_id') for x in t],
        manifest=('si' if p in man else 'NO'),
        dossier=('si' if p in doss else 'no'),
        evidence=(f"{ep[p][0]}/{ep[p][1]}" if p in ep else 'non misurata (nel lotto 23)'),
        flag_drift=('SI' if p in drift else 'no' if p in ep else '-'),
        candidates=sorted(cands.get(p,[])),
        integrated='no - in coda a BATCH_COMMIT' if cands.get(p) else 'nessun candidato',
    ))
json.dump(rows, open(f'{SP}/reconcile54.json','w'), indent=1)
c=collections.Counter((r['set'], r['state_now']) for r in rows)
print(json.dumps({f'{k[0]} / {k[1]}': v for k,v in sorted(c.items())}, indent=1))
print('receipt oggi:', sum(r['receipts_today'] for r in rows), '| studi (dei 54) toccati oggi:', sum(1 for r in rows if r['receipts_today']))
print('candidati totali sui 54:', sum(len(r['candidates']) for r in rows))

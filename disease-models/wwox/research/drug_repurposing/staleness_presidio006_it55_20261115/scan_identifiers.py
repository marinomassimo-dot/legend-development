import csv,re,subprocess,sys
D="disease-models/wwox/research/drug_repurposing/"
M=D+"batch_sci_20261105/map/open_questions_map.tsv"
rows=list(csv.DictReader(open(M),delimiter='\t'))
sel=[x for x in rows if x['status']=='OPEN' and x['kind'] in('literature_executable','data_access_blocked') and x['executable_zero_spend'] in('yes','partial')]
def sh(c): return subprocess.run(c,shell=True,capture_output=True,text=True).stdout
EXC0=("open_questions_map.tsv","map/README.md","fulltext_read_receipts.jsonl","reading_state.md","coverage_report.md","state_manifest","registries/papers","ledger/")
out=[]
for x in sel:
    txt=' '.join([x['source_ref'],x['question_text_max300'],x['decision_at_stake_max200'],x['status_evidence'],x['blocking_reason']])
    toks=set(re.findall(r'\b\d{7,8}\b',txt))|set(re.findall(r'PMC\d{5,8}',txt))|set(re.findall(r'CHEMBL\d{4,8}',txt))
    toks.add(x['qid'])
    
    d=x['last_touched']
    hits={}
    for t in sorted(toks):
        files=sh(f"git grep -l -F -e '{t}' HEAD -- . ':!*open_questions_map.tsv' ':!*fulltext_read_receipts.jsonl'").split('\n')
        for f in files:
            f=f.replace('HEAD:','')
            if not f or any(e in f for e in EXC0): continue
            c=sh(f"git log --since='{d}T23:59:59Z' --format='%h %cs' -1 -- '{f}'").strip()
            if c: hits.setdefault(f,[]).append((t,c))
    out.append((x['qid'],d,len(toks),hits))
for q,d,n,h in out:
    pass # last={d} tokens={n} files_after={len(h)}")
    for f,v in list(h.items())[:6]: print("   ",f.replace(D,''),sorted({a for a,_ in v})[:3],v[0][1])

import re as _r
print()
for q,d,n,h in out:
    keep={f:v for f,v in h.items() if not _r.search(r'advisor_|BRIEF|brief|assessment|meta.json|source_items_index|FROM_THE_MAP|CONSUMERS|/map/|STATUS|VERIFICATION|batch_queue|ORCHESTRATOR_EDITS|capability_scout|next_batch|rp008_unread|presidio|PRESIDIO|probes_run|inputs_it4',f)}
    print('##',q,d,'tokens',n,'result-like files',len(keep))
    for f,v in list(keep.items())[:7]: print('   ',f.replace(D,''),sorted({a for a,_ in v})[:3],v[0][1])

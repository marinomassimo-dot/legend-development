import csv,re
csv.field_size_limit(10**8)
b='/home/desktop/legend-development/.claude/worktrees/pres001/disease-models/wwox/research/drug_repurposing/'
def n(s): return re.sub(r'\s+',' ',s).strip()
L=list(csv.DictReader(open(b+'inhibitory_defect_sci47_20261112/output/levers.tsv'),delimiter='\t'))
G={r['proposal_id'].split('::')[-1]:r for r in csv.DictReader(open(b+'generation_it40_20261109/conditional_proposals_packages_it47.tsv'),delimiter='\t') if r['proposal_id'].startswith('CP-inhibitory_defect_sci47_20261112::')}
tot=0;bad=[]
for l in L:
    g=n(' '.join(G[l['lever_id']].values()))
    for k,v in l.items():
        if k=='lever_id': continue
        tot+=1
        if n(v) not in g: bad.append((l['lever_id'],k))
print(tot,'cells checked; not found:',bad)

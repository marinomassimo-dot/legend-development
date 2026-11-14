import csv,re
csv.field_size_limit(10**8)
ROOT='/home/desktop/legend-development/.claude/worktrees/adv006/'
OUT=ROOT+'disease-models/wwox/research/drug_repurposing/measurement_reconciliation_adv006_20261114/output/'
n=lambda s: re.sub(r'\s+',' ',s).strip()
bad=0;tot=0
for r in csv.DictReader(open(OUT+'measurement_quotes.tsv'),delimiter='\t'):
    tot+=1
    t=n(open(ROOT+r['source_path'],encoding='utf-8').read())
    ok=n(r['quote']) in t
    if not ok: bad+=1; print('NOT FOUND',r['m_id'],r['field'],r['source_path'][-50:],r['quote'][:100])
print(tot,bad)

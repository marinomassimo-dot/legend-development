import csv,re
csv.field_size_limit(10**8)
b='/home/desktop/legend-development/.claude/worktrees/pres001/disease-models/wwox/research/drug_repurposing/'
M=list(csv.DictReader(open(b+'inhibitory_defect_sci47_20261112/output/matrix.tsv'),delimiter='\t'))
def has(E,s):
    if re.search(r'\b%s\b'%E,s): return True
    # ranges E1-E4
    for m in re.finditer(r'\bE(\d)-E(\d)\b',s):
        if int(m.group(1))<=int(E[1])<=int(m.group(2)): return True
    return False
def route(E,cols):
    return [r['obs_id'] for r in M if any(has(E,r[c]) for c in cols)]
oc=['what_each_outcome_would_favour','pharmacological_decision_it_would_change']
al=['compatible_explanations','weakened_explanations','why']+oc
for E in ['E1','E2','E3','E4','E5','E6']:
    print(E,'outcome+decision:',route(E,oc),' | plus compat/weak/why:',sorted(set(route(E,al))-set(route(E,oc))))
# ADV-006 declarations
Ms=list(csv.DictReader(open(b+'measurement_reconciliation_adv006_20261114/output/measurements.tsv'),delimiter='\t'))
decl={}
for r in Ms:
    for tok in r['requests_merged'].split(' ; '):
        tok=tok.split(' | ')[0].strip()
        m=re.match(r'sci47_inhibitory#(matrix|levers|design_review):(.*)',tok)
        if m: decl.setdefault((m.group(1),m.group(2)),[]).append(r['m_id'])
for k in sorted(decl): print(k,decl[k])
# L1 O-ids -> M rows; also attached O set -> M rows
att=['O01','O04','O06','O10','O14','O03','O02','O05','O12']
for o in att: print(o,'->',decl.get(('matrix',o)))

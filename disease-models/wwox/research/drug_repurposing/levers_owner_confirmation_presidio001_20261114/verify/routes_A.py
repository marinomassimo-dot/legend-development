import csv,re,sys
csv.field_size_limit(10**8)
base='inhibitory_defect_sci47_20261112/output/'
M=list(csv.DictReader(open(base+'matrix.tsv'),delimiter='\t'))
L={r['lever_id']:r for r in csv.DictReader(open(base+'levers.tsv'),delimiter='\t')}
cols=['compatible_explanations','weakened_explanations','why','what_each_outcome_would_favour','pharmacological_decision_it_would_change','discriminating_measure','observation']
def ids(s,p): return sorted(set(re.findall(p,s)))
for lv in ('L1','L2'):
    cells=L[lv]
    print('=====',lv)
    for k,v in cells.items():
        o=ids(v,r'\bO\d\d\b'); e=ids(v,r'\bE\d\b'); l=ids(v,r'\bL\d\b')
        if o or e or l: print(k,'O',o,'E',e,'L',l)
# matrix rows reached by E-ids
for E in ['E1','E2','E3','E4','E5','E6']:
    print('--',E)
    for r in M:
        hit=[c for c in cols if re.search(r'\b%s\b'%E,r[c])]
        if hit: print(r['obs_id'],hit)
print('-- L-ids in matrix')
for r in M:
    for c in M[0].keys():
        if re.search(r'\bL\d\b',r[c]): print(r['obs_id'],c,re.findall(r'\bL\d\b',r[c]))
print('-- "all E1-E6" ranges / generic')
for r in M:
    for c in cols:
        if re.search(r'E1-E[3-6]|all of E1|all E1|\bany\b.*lever|every',r[c]): print(r['obs_id'],c,re.findall(r'E1-E\d|all of E1-E6|any \w+ lever|every \w+',r[c]))

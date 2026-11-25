import re,sys
sys.path.insert(0,'disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_adv263_20261125')
import enumerate_adv263 as E
P='disease-models/wwox/analysis/mechanism_intervention_map.md'
NEG=re.compile(r"(?<!\w)(never|no|none|nobody|nothing|unmeasured|untested|absent|mai|nessun|nessuno|nessuna|not measured|not tested|not been|non misurato|non testato)(?!\w)",re.I)
out=[];seen=set()
for rid,block in E.md_blocks(P):
    if rid=='(preamble)' or 'STRESS' in block[:200] or block.startswith('| This file says') or block.startswith('**Correction (ADV-263') : continue
    for s in E.sentences(block):
        if NEG.search(s) and s not in seen:
            seen.add(s); out.append((rid,s))
start=next(i for i,(r,s) in enumerate(out) if True)
print(len(out))
for i,(r,s) in enumerate(out,1):
    if i<=int(sys.argv[1]) and i>int(sys.argv[2]):
        m=NEG.search(s); a=max(0,m.start()-140)
        print(i,r[:14],'|',s[a:a+260])

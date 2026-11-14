import csv,re,sys,os
csv.field_size_limit(10**8)
root='/home/desktop/legend-development/.claude/worktrees/pres001/'
base=root+'disease-models/wwox/research/drug_repurposing/levers_owner_confirmation_presidio001_20261114/'
def norm(s): return re.sub(r'\s+',' ',s.replace(' ',' ')).strip()
cache={}
def load(p):
    if p not in cache:
        cache[p]=norm(open(root+p,encoding='utf-8').read()) if os.path.exists(root+p) else None
    return cache[p]
rows=list(csv.DictReader(open(base+'confirmation.tsv'),delimiter='\t'))
out=[]
for r in rows:
    loc=r['source_locator']
    files=[f.strip() for f in loc.split('| files:')[1].split(';')] if '| files:' in loc else []
    files=[f for f in files if f]
    # also files named before '#'
    for part in re.split(r';\s*',loc.split('| files:')[0]):
        f=part.split('#')[0].strip()
        if f.endswith(('.tsv','.md','.py')) and f not in files: files.append(f)
    sv=r['source_verbatim']
    frs=[x for x in sv.split(' || ') if x.strip()] if sv.strip() else []
    for i,fr in enumerate(frs):
        fn=norm(fr)
        hits=[f for f in files if load(f) and fn in load(f)]
        # try without trailing ellipsis
        status='OK' if hits else 'MISMATCH'
        if not hits:
            # try prefix before '...'
            parts=[p.strip() for p in re.split(r'\.\.\.|…',fn) if p.strip()]
            if len(parts)>1 and all(any(p in (load(f) or '') for f in files) for p in parts):
                status='OK_ELLIPSIS'
                hits=['(parts)']
            else:
                # search any file anywhere in listed dirs: all repo sources
                status='MISMATCH'
        out.append((r['item'],i,status,';'.join(hits)[:150],fn[:160],len(fn)))
        if not r['source_verbatim']: pass
    if not frs: out.append((r['item'],0,'NO_VERBATIM','','',0))
bad=[o for o in out if o[2] not in('OK','OK_ELLIPSIS')]
print('fragments',len(out),'ok',len([o for o in out if o[2].startswith('OK')]),'bad',len(bad))
for o in out:
    if o[2] in('MISMATCH',): print(o)
print('NO_VERBATIM rows:',[o[0] for o in out if o[2]=='NO_VERBATIM'])
import json
with open(base+'verify/verbatim_results.tsv','w') as f:
    f.write('item\tfragment_no\tstatus\tfound_in\tfragment_start\tlen\n')
    for o in out: f.write('\t'.join(str(x) for x in o)+'\n')

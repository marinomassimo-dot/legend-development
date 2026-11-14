import csv,re
csv.field_size_limit(10**8)
ROOT='/home/desktop/legend-development/.claude/worktrees/adv006/'
OUT=ROOT+'disease-models/wwox/research/drug_repurposing/measurement_reconciliation_adv006_20261114/output/'
def norm(s): return re.sub(r'\s+',' ',s).strip()
items=[]
for r in csv.DictReader(open(OUT+'crosswalk.tsv'),delimiter='\t'):
    if r['source_path'].endswith('.md'):
        for i,p in enumerate(r['request_verbatim'].split(' || ')): items.append((r['req_id'],r['source_path'],r['locator'],p))
for r in csv.DictReader(open(OUT+'conflicts.tsv'),delimiter='\t'):
    for s in 'AB':
        path,loc=r['source_'+s].split('#',1)
        if path.endswith('.md'): items.append(('conflict '+r['conflict_id']+s,path,loc,r['quote_'+s]))
for rid,path,loc,q in items:
    lines=open(ROOT+path,encoding='utf-8').read().split('\n')
    # build whitespace-joined text with line offsets
    qn=norm(q); hit=None
    for i in range(len(lines)):
        for j in range(i,min(i+6,len(lines))):
            if qn in norm(' '.join(lines[i:j+1])): hit=i; break
        if hit is not None: break
    head=None
    if hit is not None:
        for k in range(hit,-1,-1):
            if lines[k].startswith('#') or lines[k].startswith('**') and k==hit-0 and False: head=(k+1,lines[k][:90]); break
    print(rid,'|',path.split('/')[-1],'|',loc[:70],'|line',None if hit is None else hit+1,'|',head)

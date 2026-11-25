import re,os,json,glob,sys
root='disease-models/wwox'
T=re.compile(r'valpro\w*|entinostat|MS-275|trichostatin|panobinostat|vorinostat|\bSAHA\b|belinostat|(?:sodium )?butyrate|phenylbutyr\w*|histone deacetylase inhibit\w*|HDAC ?inhibit\w*|HDACIs?\b',re.I)
Tc=re.compile(r'\bSAHA\b')   # case-sensitive for SAHA
W=re.compile(r'WWOX|WW domain.containing oxidoreductase',re.I)
def ctx(r,win=220):
    out=[]
    for m in T.finditer(r):
        if m.group(0).lower()=='saha' and not Tc.match(m.group(0)): continue
        a=max(0,m.start()-win); b=min(len(r),m.end()+win); seg=r[a:b]
        if W.search(seg): out.append(re.sub(r'\s+',' ',seg))
    return out
res=[]
srcs={'discovery_ledger':('research/discovery_ledger_current.md',r'(?m)^(?=### )'),'paper_registry':('registries/paper_registry_current.md',r'(?m)^(?=## )'),'literature_log':('registries/literature_tracking_log_current.md',r'(?m)^(?=## )'),'claim_registry':('registries/claim_registry_current.md',r'(?m)^(?=## )')}
for k,(p,pat) in srcs.items():
    t=open(os.path.join(root,p),encoding='utf-8',errors='replace').read()
    for r in re.split(pat,t):
        c=ctx(r)
        if c: res.append((k,r.strip().split('\n')[0][:70],len(c),c[0][:420]))
for l in open(root+'/registries/fulltext_read_receipts.jsonl',encoding='utf-8'):
    d=json.loads(l); s=json.dumps(d)
    c=ctx(s,150)
    if c: res.append(('receipt '+d['event_id'],d.get('study_id',{}).get('pmid','?'),len(c),c[0][:300]))
for x in res: print(x[0][:34],'|',x[1],'|',x[2],'|',x[3],'\n')
print(len(res))

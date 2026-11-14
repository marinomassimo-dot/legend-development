# Verifier V own substring test (independent of the producer's quote_check.py)
import csv, re, sys, os
csv.field_size_limit(10**8)
ROOT='/home/desktop/legend-development/.claude/worktrees/adv006/'
OUT=ROOT+'disease-models/wwox/research/drug_repurposing/measurement_reconciliation_adv006_20261114/output/'
def norm(s): return re.sub(r'\s+',' ',s.replace(' ',' ')).strip()
cache={}
def load(path):
    if path in cache: return cache[path]
    p=ROOT+path
    txt=open(p,encoding='utf-8').read()
    tab=None
    if path.endswith('.tsv'):
        tab=list(csv.reader(open(p,encoding='utf-8',newline=''),delimiter='\t'))
    cache[path]=(txt,tab); return cache[path]
def find_row(tab,rowkey):
    hdr=tab[0]
    for r in tab[1:]:
        if r and r[0]==rowkey: return hdr,r
    return hdr,None
def check(path,locator,quote):
    """returns (in_file, in_row, in_named_col, note)"""
    txt,tab=load(path)
    q=norm(quote)
    in_file = q in norm(txt)
    in_row=None; in_col=None; note=''
    if tab:
        # locator forms
        m=re.match(r'^([^,#]+?)(?:#|:)?(?:, column[s]? | ?column[s]? )?',locator)
        # determine row key and columns
        rowkey=None; cols=[]
        mm=re.match(r'^([A-Za-z0-9\-]+)(?:, columns? (.*))?$',locator)
        if mm:
            rowkey=mm.group(1); 
            if mm.group(2): cols=[c.strip() for c in re.split(r' and |, ',mm.group(2))]
        else:
            mr=re.match(r'^row (\d+) \(.*\), column (\S+)$',locator)
            if mr:
                idx=int(mr.group(1)); hdr=tab[0]; r=tab[idx]
                in_row = q in norm(' '.join(r)); cols=[mr.group(2)]
                in_col = q in norm(r[hdr.index(cols[0])])
                return in_file,in_row,in_col,'direct-row %d (header excluded)'%idx
        if rowkey:
            hdr,r=find_row(tab,rowkey)
            if r is None: note='rowkey not found '+rowkey; in_row=False
            else:
                in_row= q in norm(' '.join(r))
                if cols:
                    vals=[]
                    for c in cols:
                        if c in hdr: vals.append(norm(r[hdr.index(c)]))
                        else: note+=' col?%s'%c
                    in_col = any(q in v for v in vals)
    return in_file,in_row,in_col,note
res=[]
# crosswalk
cw=list(csv.DictReader(open(OUT+'crosswalk.tsv',encoding='utf-8'),delimiter='\t'))
for r in cw:
    parts=[p for p in r['request_verbatim'].split(' || ')]
    for i,p in enumerate(parts):
        f,rw,c,n=check(r['source_path'],r['locator'],p)
        res.append(('crosswalk',r['req_id'],i+1,r['locator'],f,rw,c,n))
# conflicts
cf=list(csv.DictReader(open(OUT+'conflicts.tsv',encoding='utf-8'),delimiter='\t'))
for r in cf:
    for side in 'AB':
        src=r['source_'+side]; path,loc=src.split('#',1)
        q=r['quote_'+side]
        # locator forms: ROW:column  or section
        m=re.match(r'^([A-Za-z0-9\-]+):(\S+)$',loc)
        if m and path.endswith('.tsv'):
            L='%s, column %s'%(m.group(1),m.group(2))
        else: L=loc
        f,rw,c,n=check(path,L,q)
        res.append(('conflict',r['conflict_id'],side,loc,f,rw,c,n))
with open('v_quote_check_results.tsv','w') as fo:
    fo.write('kind\tid\tpart\tlocator\tin_file\tin_row\tin_named_col\tnote\n')
    for x in res: fo.write('\t'.join(str(y) for y in x)+'\n')
bad=[x for x in res if not x[4] or x[5] is False or x[6] is False]
print('checked',len(res),'not-ok',len(bad))
for x in bad: print(x)

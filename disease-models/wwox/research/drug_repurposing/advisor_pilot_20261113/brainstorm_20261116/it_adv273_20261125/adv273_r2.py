import re,os,glob,sys
root='/home/desktop/legend-development/files/fulltext'
T=re.compile(r'valpro\w*|entinostat|MS-275|trichostatin|panobinostat|vorinostat|\bSAHA\b|belinostat|butyrate|phenylbutyr\w*|histone deacetylase inhibit\w*|HDAC ?inhibit\w*|HDACIs?\b',re.I)
W=re.compile(r'WWOX|WW domain.containing oxidoreductase',re.I)
rows=[];n=0
for dp,dn,fn in os.walk(root):
    for f in fn:
        if not f.lower().endswith(('.xml','.txt','.html','.md')): continue
        p=os.path.join(dp,f)
        try: s=open(p,encoding='utf-8',errors='replace').read()
        except: continue
        n+=1
        w=len(W.findall(s))
        if not w: continue
        c={}
        for m in T.finditer(s):
            k=m.group(0).lower()
            if k=='saha' and m.group(0)!='SAHA': continue
            c[k]=c.get(k,0)+1
        if not c: continue
        # co-occurrence within 300 chars
        near=0
        for m in T.finditer(s):
            if m.group(0).lower()=='saha' and m.group(0)!='SAHA': continue
            a=max(0,m.start()-300); b=m.end()+300
            if W.search(s[a:b]): near+=1
        rows.append((os.path.relpath(p,root),w,sum(c.values()),near,sorted(c)[:4]))
print('files scanned',n,'with WWOX and a compound term',len(rows))
for r in sorted(rows,key=lambda x:-x[3]):
    if r[3]>0: print(r[3],r[1],r[2],r[0][:90],r[4])

import json,collections,hashlib,re
rows=json.load(open('an/koz_rows.json'))
cls={'Purkinje':r'^Purkinje','Bergmann':r'^Bergmann','Astrocyte':r'^Astrocyte','ODC':r'^ODC','OPC':r'^OPC','Granule':r'^Granule','MLI':r'^MLI','Microglia':r'^Microglia$'}
def cl(s):
    for k,p in cls.items():
        if re.match(p,s): return k
ok=[r for r in rows if r['padj']<0.01 and r['pin']>=50 and r['pout']<=20 and r['logFC']>1.0]
by=collections.defaultdict(lambda: collections.defaultdict(float))
for r in ok:
    k=cl(r['sub'])
    if k: by[r['gene']][k]=max(by[r['gene']][k],r['logFC'])
sets={}
for k in cls:
    g=[(max(v.values()),gene) for gene,v in by.items() if set(v)=={k}]
    g.sort(reverse=True)
    sets[k]=[x[1] for x in g[:15]]
    print(k,len(g),sets[k])
json.dump(sets,open('an/marker_sets_frozen.json','w'),indent=1,sort_keys=True)
core="Hmgcs1 Hmgcr Mvk Pmvk Mvd Idi1 Fdps Fdft1 Sqle Lss Cyp51 Msmo1 Nsdhl Hsd17b7 Sc5d Dhcr7 Dhcr24 Ldlr Insig1 Srebf2".split()
# human hallmark 2020 cholesterol homeostasis -> mouse title-case
txt=open('/home/desktop/legend-development/files/reach_audit_downloads/MSigDB_Hallmark_2020.gmt').read().splitlines()
hm=[l.split('\t') for l in txt if l.startswith('Cholesterol Homeostasis')]
hall=[g.capitalize() for g in hm[0][2:] if g] if hm else []
print('hallmark',len(hall))
json.dump({'sterol_core':core,'hallmark_cholesterol_homeostasis_mouse_title_case':hall},open('an/sterol_sets_frozen.json','w'),indent=1,sort_keys=True)
# cell-class membership of sterol core (qualitative, from Kozareva table 2: any subtype with logFC>0.5 & padj<0.01, pct_in>=40)
for g in core:
    m=collections.defaultdict(float)
    for r in rows:
        if r['gene']==g and r['padj']<0.01 and r['pin']>=40 and r['logFC']>0.5:
            k=cl(r['sub'])
            if k: m[k]=max(m[k],r['logFC'])
    print(g,dict(sorted(m.items(),key=lambda x:-x[1])))
for f in ('marker_sets_frozen.json','sterol_sets_frozen.json'):
    print(f,hashlib.sha256(open('an/'+f,'rb').read()).hexdigest())

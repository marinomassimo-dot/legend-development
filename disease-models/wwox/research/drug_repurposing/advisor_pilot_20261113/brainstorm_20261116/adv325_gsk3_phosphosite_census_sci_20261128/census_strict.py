import re,sys,os
files=[l.strip() for l in open(sys.argv[1])]
base='/home/desktop/legend-development/files/fulltext/'
P=[('GSK3 pSer9/21 or pTyr216/279',r'(p-?GSK-?3|phospho-?GSK-?3|GSK-?3\s?[αβab]?\s?[\(\-]?\s?(?:p|phospho|ser|tyr)[^.]{0,30}(?:9|21|216|279)|(?:Ser|S)\s?-?(?:9|21)\b[^.]{0,40}GSK|GSK[^.]{0,60}(?:Ser|S)\s?-?(?:9|21)\b|Tyr\s?-?(?:216|279)[^.]{0,40}GSK|GSK[^.]{0,60}Tyr\s?-?(?:216|279))'),
 ('beta-catenin S33/S37/T41',r'(catenin[^.]{0,60}(?:Ser|S)\s?-?(?:33|37)\b|(?:Ser|S)\s?-?(?:33|37)\b[^.]{0,40}catenin|catenin[^.]{0,40}phospho)'),
 ('CRMP2 T514',r'(CRMP-?2[^.]{0,80}(?:Thr|T)\s?-?514|(?:Thr|T)\s?-?514[^.]{0,40}CRMP)'),
 ('GS S641',r'(glycogen synthase[^.]{0,60}(?:Ser|S)\s?-?641|(?:Ser|S)\s?-?641[^.]{0,30}glycogen)'),
 ('Tau sites',r'((?:p|phospho)-?Tau|Tau[^.]{0,60}(?:Ser|S|Thr|T)\s?-?(?:199|231|396|404)\b|AT100|AT8\b|PHF-?1)')]
P=[(n,re.compile(r,re.I)) for n,r in P]
byp={}
for f in files:
    f=f.lstrip('./'); m=re.match(r'(PMID\d+|PPR\d+|PMC\d+)',f); k=m.group(1) if m else f[:30]
    byp.setdefault(k,[]).append(f)
out=[]
for k,fs in sorted(byp.items()):
    f=sorted(fs,key=lambda x:-os.path.getsize(base+x))[0]
    t=open(base+f,encoding='utf-8',errors='ignore').read()
    t=re.sub(r'<[^>]+>',' ',t); t=re.sub(r'\s+',' ',t)
    c={n:len(p.findall(t)) for n,p in P}
    if sum(c.values()): out.append((k,f[:60],{a:b for a,b in c.items() if b}))
print(len(byp),'distinct ids;',len(out),'with a strict site-term hit')
for o in out: print(o)

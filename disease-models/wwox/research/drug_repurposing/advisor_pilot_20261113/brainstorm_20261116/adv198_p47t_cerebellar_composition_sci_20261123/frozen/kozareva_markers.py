import zipfile,re,html,collections,sys,json,hashlib
z=zipfile.ZipFile('koz/MOESM4.xlsx')
ss=[html.unescape(re.sub(r'<[^>]+>','',s)) for s in re.findall(r'<si>(.*?)</si>',z.read('xl/sharedStrings.xml').decode(),flags=re.S)]
sh=z.read('xl/worksheets/sheet2.xml').decode()
R=[]
for r in re.finditer(r'<row [^>]*>(.*?)</row>',sh,flags=re.S):
    out=[]
    for col,attr,v in re.findall(r'<c r="([A-Z]+)\d+"([^>]*?)(?:/>|>(?:<f>.*?</f>)?(?:<v>(.*?)</v>)?)',r.group(1)):
        out.append(ss[int(v)] if v and 't="s"' in attr else (v or ''))
    R.append(out)
rows=[dict(gene=r[1],sub=r[2],logFC=float(r[4]),padj=float(r[6]),pin=float(r[7]),pout=float(r[8])) for r in R[1:] if len(r)>=9 and r[4]]
c=collections.Counter(x['sub'] for x in rows)
print(sorted(c.items()))
json.dump(rows,open('an/koz_rows.json','w'))

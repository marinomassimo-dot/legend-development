import sys,zipfile,re,io
from xml.etree import ElementTree as ET
NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'
def col(ref):
    n=0
    for ch in re.match(r'[A-Z]+',ref).group(0): n=n*26+ord(ch)-64
    return n-1
def sheets(path):
    z=zipfile.ZipFile(path)
    ss=[]
    if 'xl/sharedStrings.xml' in z.namelist():
        for si in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',NS):
            ss.append(''.join(t.text or '' for t in si.iter('{%s}t'%NS['m'])))
    wb=ET.fromstring(z.read('xl/workbook.xml'))
    rels={r.get('Id'):r.get('Target') for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
    for s in wb.find('m:sheets',NS):
        t=rels[s.get(R)].lstrip('/'); t=t if t.startswith('xl/') else 'xl/'+t
        rows=[]
        for ev,el in ET.iterparse(io.BytesIO(z.read(t))):
            if el.tag=='{%s}row'%NS['m']:
                row={}
                for i,c in enumerate(el.findall('m:c',NS)):
                    v=c.find('m:v',NS); ty=c.get('t')
                    if ty=='inlineStr': val=''.join(x.text or '' for x in c.iter('{%s}t'%NS['m']))
                    elif v is None: continue
                    elif ty=='s': val=ss[int(v.text)]
                    else: val=v.text
                    row[col(c.get('r')) if c.get('r') else i]=val
                rows.append([row.get(i,'') for i in range(max(row)+1)] if row else [])
                el.clear()
        yield s.get('name'),rows
if __name__=='__main__':
    for p in sys.argv[1:]:
        try:
            for name,rows in sheets(p):
                print("##",p.split('/')[-1],'|',name,'| rows',len(rows))
                for r in rows[:3]: print("    ",[str(x)[:28] for x in r][:24])
                for r in rows:
                    if any(re.fullmatch(r'(?i)wwox|q9nzc7|q91wl8|.*\bGN=Wwox\b.*|Q91WL8.*|Q9NZC7.*',str(x).strip()) for x in r): print("  WWOX:",[str(x)[:40] for x in r][:30])
        except Exception as e: print("##",p,'ERR',repr(e))

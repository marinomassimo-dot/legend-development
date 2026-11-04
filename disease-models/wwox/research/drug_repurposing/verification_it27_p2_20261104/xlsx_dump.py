"""Minimal stdlib xlsx reader (no openpyxl available). Usage: xlsx_dump.py file.xlsx [sheetname_substring] [maxrows]"""
import sys, zipfile, re, xml.etree.ElementTree as ET
NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
def load(fn):
    z=zipfile.ZipFile(fn)
    ss=[]
    if 'xl/sharedStrings.xml' in z.namelist():
        for si in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',NS):
            ss.append(''.join(t.text or '' for t in si.iter('{%s}t'%NS['m'])))
    wb=ET.fromstring(z.read('xl/workbook.xml'))
    rels={r.get('Id'):r.get('Target') for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
    out={}
    for s in wb.find('m:sheets',NS):
        tgt=rels[s.get('{%s}id'%NS['r'])]
        tgt=tgt.lstrip('/'); tgt=tgt if tgt.startswith('xl/') else 'xl/'+tgt
        rows=[]
        for row in ET.fromstring(z.read(tgt)).iter('{%s}row'%NS['m']):
            d={}
            for c in row.findall('m:c',NS):
                ref=c.get('r'); col=re.match(r'[A-Z]+',ref).group()
                v=c.find('m:v',NS)
                if c.get('t')=='s' and v is not None: val=ss[int(v.text)]
                elif c.get('t')=='inlineStr': val=''.join(t.text or '' for t in c.iter('{%s}t'%NS['m']))
                else: val=v.text if v is not None else None
                d[col]=val
            rows.append(d)
        out[s.get('name')]=rows
    return out
if __name__=='__main__':
    wb=load(sys.argv[1])
    sub=sys.argv[2] if len(sys.argv)>2 else None
    mx=int(sys.argv[3]) if len(sys.argv)>3 else 30
    for n,rows in wb.items():
        if sub and sub not in n: continue
        print('=====',n,len(rows))
        for r in rows[:mx]: print(list(r.values())[:14])

"""Stdlib xlsx grep: print rows whose cells match a regex, with the sheet's header rows. Usage: xlsx_find_adv269.py FILE REGEX [MAXROWS]"""
import re, sys, zipfile
import xml.etree.ElementTree as ET
NS = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
def col(ref):
    s = re.match(r'[A-Z]+', ref).group(0); n = 0
    for ch in s: n = n*26 + ord(ch)-64
    return n
def main(path, rx, maxrows=40):
    z = zipfile.ZipFile(path)
    ss = []
    if 'xl/sharedStrings.xml' in z.namelist():
        for ev, el in ET.iterparse(z.open('xl/sharedStrings.xml')):
            if el.tag == NS+'si':
                ss.append(''.join(t.text or '' for t in el.iter(NS+'t'))); el.clear()
    wb = ET.parse(z.open('xl/workbook.xml')).getroot()
    names = [s.get('name') for s in wb.iter(NS+'sheet')]
    rels = ET.parse(z.open('xl/_rels/workbook.xml.rels')).getroot()
    pat = re.compile(rx)
    sheets = sorted(n for n in z.namelist() if re.match(r'xl/worksheets/sheet\d+\.xml$', n))
    for i, sp in enumerate(sheets):
        nm = names[i] if i < len(names) else sp
        hdr = []; shown = 0; nrows = 0; hits = 0
        for ev, el in ET.iterparse(z.open(sp)):
            if el.tag == NS+'row':
                nrows += 1
                vals = {}
                for c in el.iter(NS+'c'):
                    v = c.find(NS+'v'); t = c.get('t')
                    if t == 'inlineStr': x = ''.join(q.text or '' for q in c.iter(NS+'t'))
                    elif v is None: continue
                    elif t == 's': x = ss[int(v.text)]
                    else: x = v.text
                    vals[col(c.get('r'))] = x
                row = [vals.get(k, '') for k in range(1, (max(vals) if vals else 0)+1)]
                if nrows <= 4: hdr.append(row)
                if any(pat.search(x) for x in row):
                    hits += 1
                    if shown == 0:
                        for h in hdr: print(f'  [{nm}] HDR:', h[:14])
                    if shown < maxrows: print(f'  [{nm}] r{nrows}:', row[:14])
                    shown += 1
                el.clear()
        print(f'sheet {nm}: rows {nrows}, hits {hits}')
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 40)

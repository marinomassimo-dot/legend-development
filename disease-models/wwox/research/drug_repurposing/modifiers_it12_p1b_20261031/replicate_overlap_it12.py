"""IT12 P1-alt: overlap of same-sign FDR calls between screens of the same query gene (Data S4, sheet 'pairwise GI_Complete dataset').

Usage: python3 -I replicate_overlap_it12.py <path to File_S4.xlsx> <output json>
For each pair of screens of one query gene (rich/min and clones mixed): number of calls in each, shared same-sign calls,
sign conflicts, shared / min(n). Standard library only. Output is a list of [query, screenA, screenB, nA, nB, shared, conflicts, ratio].
"""
import sys, re, json, zipfile, collections, statistics
import xml.etree.ElementTree as ET
NS = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'

def main(path, out):
    z = zipfile.ZipFile(path); ss = []
    for ev, el in ET.iterparse(z.open('xl/sharedStrings.xml')):
        if el.tag == NS + 'si':
            ss.append(''.join(t.text or '' for t in el.iter(NS + 't'))); el.clear()
    S = collections.defaultdict(dict)
    for i, (ev, el) in enumerate(e for e in ET.iterparse(z.open('xl/worksheets/sheet5.xml')) if e[1].tag == NS + 'row'):
        r = {}
        for c in el.findall(NS + 'c'):
            v = c.find(NS + 'v'); r[re.match(r'[A-Z]+', c.get('r')).group(0)] = None if v is None else (ss[int(v.text)] if c.get('t') == 's' else v.text)
        el.clear()
        if i: S[r['C']][r['A']] = r['F']
    byq = collections.defaultdict(list)
    for s in S: byq[s.split('_')[0]].append(s)
    res = []
    for q, L in byq.items():
        for i in range(len(L)):
            for j in range(i + 1, len(L)):
                A, B = S[L[i]], S[L[j]]
                if not A or not B: continue
                same = sum(1 for g in A if g in B and A[g] == B[g]); conf = sum(1 for g in A if g in B and A[g] != B[g])
                res.append([q, L[i], L[j], len(A), len(B), same, conf, round(same / min(len(A), len(B)), 3)])
    json.dump(res, open(out, 'w'))
    sm = [t[7] for t in res if min(t[3], t[4]) <= 200]; bg = [t[7] for t in res if min(t[3], t[4]) > 200]
    print('pairs', len(res), 'min<=200:', len(sm), statistics.median(sm), '>200:', len(bg), statistics.median(bg))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(__doc__); sys.exit(0 if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help') else 2)
    main(sys.argv[1], sys.argv[2])

"""IT12 P1-alt extraction of the WWOX query screen (GIN352, WWOX_352_rich) from the authors' Data S4 / S8 / S1.

Usage: python3 -I gin352_extract_it12.py <GIN-v1.0.4 directory (unzipped Zenodo record 20734737)> <output directory>
Reads: Data Files/File_S1.xlsx, File_S4.xlsx (sheets wt_lfc, queries_lfc, qGI_scores, qGI_FDR, pairwise GI_Complete dataset),
       Data Files/File_S8.zip (qGI matrix, text). Writes the derived tables listed in the README. Standard library only.
The xlsx files are parsed as zipped XML (no openpyxl). Not the authors' code; no value is recomputed except counts and correlations.
"""
import sys, re, csv, json, math, zipfile, statistics, collections
import xml.etree.ElementTree as ET

NS = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
SCREEN = 'WWOX_352_rich'


def open_book(path):
    z = zipfile.ZipFile(path)
    ss = []
    for ev, el in ET.iterparse(z.open('xl/sharedStrings.xml')):
        if el.tag == NS + 'si':
            ss.append(''.join(t.text or '' for t in el.iter(NS + 't')))
            el.clear()
    names = re.findall(r'<sheet [^>]*name="([^"]+)"', z.read('xl/workbook.xml').decode())
    return z, ss, names


def rows(z, ss, idx):
    for ev, el in ET.iterparse(z.open('xl/worksheets/sheet%d.xml' % idx)):
        if el.tag == NS + 'row':
            r = {}
            for c in el.findall(NS + 'c'):
                col = re.match(r'[A-Z]+', c.get('r')).group(0)
                v = c.find(NS + 'v')
                r[col] = None if v is None else (ss[int(v.text)] if c.get('t') == 's' else v.text)
            yield r
            el.clear()


def fmt(x):
    return '' if x is None else '%.4g' % float(x)


def column(z, ss, idx, screen):
    out, ci = {}, None
    for i, r in enumerate(rows(z, ss, idx)):
        if i == 0:
            ci = [k for k, v in r.items() if v == screen][0]
            continue
        out[r['A']] = r.get(ci)
    return out


def main(base, outdir):
    d = base + '/Data Files/'
    # S1: query/screen information
    z, ss, _ = open_book(d + 'File_S1.xlsx')
    for r in rows(z, ss, 1):
        if r.get('C') == 'GIN352':
            json.dump(r, open(outdir + '/s1_gin352_row.json', 'w'), indent=1)
    # S4
    z, ss, names = open_book(d + 'File_S4.xlsx')
    q = column(z, ss, 3, SCREEN); f = column(z, ss, 4, SCREEN); lfc = column(z, ss, 2, SCREEN)
    cnt = collections.Counter(); pos = collections.Counter(); neg = collections.Counter(); W = []
    for i, r in enumerate(rows(z, ss, 5)):
        if i == 0:
            continue
        cnt[r['C']] += 1
        if r['F'] == 'positive': pos[r['A']] += 1
        elif r['F'] == 'negative': neg[r['A']] += 1
        if r['B'] == 'WWOX': W.append(r)
    v = sorted(cnt.values())
    summary = {'screens_with_calls': len(v), 'median_calls': v[len(v) // 2], 'min': v[0], 'max': v[-1],
               'wwox_calls': cnt[SCREEN], 'wwox_rank_ascending': v.index(cnt[SCREEN]) + 1,
               'wwox_negative': sum(1 for r in W if r['F'] == 'negative'), 'wwox_positive': sum(1 for r in W if r['F'] == 'positive'),
               'wwox_stringent': sum(1 for r in W if r.get('G') in ('negative', 'positive'))}
    # WT single-mutant LFC of WWOX guides (sheet 1, 39 WT screens)
    for i, r in enumerate(rows(z, ss, 1)):
        if i and r.get('A') == 'WWOX':
            x = [float(t) for k, t in r.items() if k != 'A' and t not in (None, 'NA')]
            summary['wwox_wt_lfc_mean'] = statistics.mean(x); summary['wwox_wt_lfc_sd'] = statistics.pstdev(x); summary['wwox_wt_n'] = len(x)
    # same-sign overlap of calls between screens of the same query gene
    S = collections.defaultdict(dict)
    json.dump(summary, open(outdir + '/summary.json', 'w'), indent=1)
    with open(outdir + '/wwox_gin352_significant_gis_with_hubs.tsv', 'w') as o:
        o.write('library_gene\tqGI\tFDR\tcall\tn_queries_with_same_sign_call_of_298\tstringent\tquery_lfc_in_wwox_screen\n')
        for r in sorted(W, key=lambda r: float(r['D'])):
            g = r['A']; n = (pos if r['F'] == 'positive' else neg)[g]
            o.write('%s\t%.3f\t%.3g\t%s\t%d\t%s\t%s\n' % (g, float(r['D']), float(r['E']), r['F'], n, r.get('G', ''), fmt(lfc.get(g))))
    # selected genes from existing cards (all genes, sign and FDR as reported)
    sel = ['WWOX', 'HIF1A', 'EGLN1', 'VHL', 'NFE2L2', 'KEAP1', 'MYC', 'GSK3A', 'GSK3B', 'EIF2AK1', 'EIF2AK3', 'PDK1', 'PDK2', 'PDK3', 'PDK4',
           'LDHA', 'LDHB', 'PDHA1', 'PDHB', 'DLD', 'CS', 'LIPT1', 'NDUFAF1', 'NDUFS4', 'SLC2A1', 'HK2', 'GOT1', 'ITCH', 'TNK2', 'SOD2', 'DPH2', 'EIF5AL1']
    with open(outdir + '/selected_genes_qgi_fdr.tsv', 'w') as o:
        o.write('gene\tqGI\tFDR\tquery_lfc\n')
        for g in sel:
            vals = ('absent', 'absent', 'absent') if g not in q else (fmt(q[g]), fmt(f[g]), fmt(lfc[g]))
            o.write('%s\t%s\t%s\t%s\n' % ((g,) + vals))
    # S8 matrix: profile correlation with the other 297 screens
    zz = zipfile.ZipFile(d + 'File_S8.zip')
    rd = csv.reader(zz.open('File_S8/File S8_HAP1 GI matrix_Clustered.txt').read().decode().splitlines(), delimiter='\t')
    h = next(rd); cols = [[] for _ in h]
    for row in rd:
        for j in range(1, len(h)):
            cols[j].append(float(row[j]) if row[j] not in ('', 'NA') else float('nan'))
    def corr(a, b):
        p = [(x, y) for x, y in zip(a, b) if x == x and y == y]
        mx = sum(x for x, y in p) / len(p); my = sum(y for x, y in p) / len(p)
        return sum((x - mx) * (y - my) for x, y in p) / math.sqrt(sum((x - mx) ** 2 for x, y in p) * sum((y - my) ** 2 for x, y in p))
    w = h.index(SCREEN)
    cs = sorted(((corr(cols[w], cols[j]), h[j]) for j in range(1, len(h)) if j != w), reverse=True)
    json.dump({'max_corr_with_any_other_screen': cs[0], 'median': statistics.median(a for a, b in cs), 'top5': cs[:5]},
              open(outdir + '/profile_correlation.json', 'w'), indent=1)


if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[1] in ('-h', '--help'):
        print(__doc__); sys.exit(0 if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help') else 2)
    main(sys.argv[1], sys.argv[2])

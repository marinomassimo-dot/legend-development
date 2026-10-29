#!/usr/bin/env python3
"""Apply the decision rule declared in prediction_declared_20261029.md to organoid_glial_panel_cpm.tsv.
Descriptive only: RAISED = all four KO libraries above the larger WT library AND mean-CPM ratio >= 1.5; LOWERED the mirror;
NOT INFORMATIVE = fewer than 20 raw counts in every library; otherwise NOT SEPARATED. No test, six libraries.
Usage: classify_panel.py <panel.tsv>   (read-only; prints a rectangular TSV to stdout and the per-set tally to stderr)"""
import csv, sys
SETS = {
 'microglia_presence': 'AIF1 P2RY12 TMEM119 CX3CR1 CSF1R PTPRC TREM2'.split(),
 'astroglial_lineage_homeostatic': 'GFAP AQP4 S100B ALDH1L1 SLC1A2 SLC1A3 GJA1 GLUL KCNJ10 ADK SOX9 NFIA HOPX FABP7'.split(),
 'reactive_pan': 'C3 SERPINA3 LCN2 CD44 CHI3L1 VIM TIMP1 CEBPD STAT3 SOCS3'.split(),
 'cytokine_inflammasome': 'IL1B IL6 TNF NLRP3 IL1R1 NFKB1 RELA CCL2 CXCL8 TGFB1'.split(),
 'reference': ['WWOX'],
}
if len(sys.argv) != 2 or sys.argv[1] in ('-h', '--help'):
    print(__doc__); sys.exit(0 if len(sys.argv) == 2 else 2)
rows = {r['gene']: r for r in csv.DictReader(open(sys.argv[1]), delimiter='\t')}
print('set\tgene\traw_ko(1-4)\traw_wt(1-2)\tcpm_ko_mean\tcpm_wt_mean\tratio\tclass')
tally = {}
for s, genes in SETS.items():
    for g in genes:
        r = rows.get(g)
        if r is None or r.get('raw_cko1') is None:
            print(f'{s}\t{g}\tABSENT\t\t\t\t\tNOT INFORMATIVE'); tally.setdefault(s, []).append('NI'); continue
        raw_ko = [float(r[f'raw_cko{i}']) for i in range(1, 5)]
        raw_wt = [float(r[f'raw_cwt{i}']) for i in range(1, 3)]
        c_ko = [float(r[f'cpm_cko{i}']) for i in range(1, 5)]
        c_wt = [float(r[f'cpm_cwt{i}']) for i in range(1, 3)]
        mk, mw = sum(c_ko) / 4, sum(c_wt) / 2
        ratio = mk / mw if mw else float('nan')
        if max(raw_ko + raw_wt) < 20: cls = 'NOT INFORMATIVE'
        elif min(c_ko) > max(c_wt) and ratio >= 1.5: cls = 'RAISED'
        elif max(c_ko) < min(c_wt) and ratio <= 1 / 1.5: cls = 'LOWERED'
        else: cls = 'NOT SEPARATED'
        tally.setdefault(s, []).append(cls)
        print(f"{s}\t{g}\t{'/'.join(f'{x:g}' for x in raw_ko)}\t{'/'.join(f'{x:g}' for x in raw_wt)}\t{mk:.2f}\t{mw:.2f}\t{ratio:.2f}\t{cls}")
for s, t in tally.items():
    print('#', s, {k: t.count(k) for k in sorted(set(t))}, file=sys.stderr)

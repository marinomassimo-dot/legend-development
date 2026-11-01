#!/usr/bin/env python3
"""Verifier item 5: re-run the imported grader on the producer's relations/assay tables for the four documents under
review and report the technique sets per assay, to find what actually triggered 'assay techniques differ'.
Read-only import of scout_it14_p6_20261101/selectivity_p6.py via importlib (not executed as main)."""
import csv, importlib.util, os, sys
D = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
spec = importlib.util.spec_from_file_location('sel', f'{D}/scout_it14_p6_20261101/selectivity_p6.py')
sel = importlib.util.module_from_spec(spec); spec.loader.exec_module(sel)
P = f'{D}/target_first_it15_qa_nmdar_20261101'
rows = list(csv.DictReader(open(f'{P}/relations_qa.tsv'), delimiter='\t'))
ctx = {r['assay_id']: r for r in csv.DictReader(open(f'{P}/assay_context_qa.tsv'), delimiter='\t')}
g = sel.collect(rows)
want = {'chembl:CHEMBL4308825', 'chembl:CHEMBL1146243', 'chembl:CHEMBL6115009', 'chembl:CHEMBL1759939'}
out = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'q5_regrade.tsv'), 'w')
out.write('compound\tdocument\tmeasure\tspecies\tgrade\tlimits\tassay_technique_sets\n')
for key, obs in sorted(g.items()):
    if key[1] not in want or key[0] not in ('CHEMBL305187', 'CHEMBL305195', 'CHEMBL807', 'CHEMBL742', 'CHEMBL284237'): continue
    grade, lim, by, comp, att = sel.grade_group(obs, ctx)
    assays = sorted({a for gname in att for a in by[gname]['assays']})
    ts = {a: sorted(sel.techniques(ctx[a]['description'])) if a in ctx else 'NO_CTX' for a in assays}
    out.write('\t'.join([key[0], key[1], key[2], key[3], grade, ' | '.join(lim), str(ts)]) + '\n')
out.close(); print(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'q5_regrade.tsv')).read())

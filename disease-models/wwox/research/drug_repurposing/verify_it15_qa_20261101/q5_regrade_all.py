"""Verifier item 5: regrade EVERY group of the producer's relations_qa.tsv with the unchanged imported grader and the producer's
assay_context_qa.tsv; compare with the shipped graded_comparisons_qa.tsv grade column. Writes q5_regrade_all_diff.tsv."""
import csv, importlib.util, os, collections, io
D = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
spec = importlib.util.spec_from_file_location('sel', f'{D}/scout_it14_p6_20261101/selectivity_p6.py')
sel = importlib.util.module_from_spec(spec); spec.loader.exec_module(sel)
P = f'{D}/target_first_it15_qa_nmdar_20261101'
rows = list(csv.DictReader(open(f'{P}/relations_qa.tsv'), delimiter='\t'))
ctx = {r['assay_id']: r for r in csv.DictReader(open(f'{P}/assay_context_qa.tsv'), delimiter='\t')}
groups = sel.collect(rows)
buf = io.StringIO(); 
for k, obs in sorted(groups.items()):
    if len({o[0] for o in obs}) < 2: continue
    fams = collections.defaultdict(list)
    for o in obs: fams[sel.family(o[0].split('|')[0])].append(o)
    parts = [(k, obs, '')]
    if len(fams) > 1:
        parts += [((k[0], k[1] + '#' + f, k[2], k[3]), fo, f) for f, fo in sorted(fams.items()) if len({o[0] for o in fo}) > 1]
    for kk, oo, fam in parts: sel.emit(buf, kk, oo, ctx, skip_if_undeterminable=bool(fam))
mine = list(csv.reader(io.StringIO(buf.getvalue()), delimiter='\t'))
shipped = list(csv.DictReader(open(f'{P}/graded_comparisons_qa.tsv'), delimiter='\t'))
print('regraded rows', len(mine), 'shipped rows', len(shipped))
print('regraded grades', collections.Counter(r[5] for r in mine))
print('shipped grades ', collections.Counter(r['grade'] for r in shipped))
sk = {(r['compound'], r['document'], r['measure'], r['species']): r['grade'] for r in shipped}
diff = [(r[0], r[1], r[2], r[3], sk.get((r[0], r[1], r[2], r[3])), r[5], r[6]) for r in mine if sk.get((r[0], r[1], r[2], r[3])) != r[5]]
print('rows whose grade differs', len(diff))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'q5_regrade_all_diff.tsv'), 'w') as f:
    f.write('compound\tdocument\tmeasure\tspecies\tshipped_grade\tregraded_grade\tregraded_limits\n')
    for d in diff: f.write('\t'.join(str(x) for x in d) + '\n')
print(collections.Counter((d[4], d[5]) for d in diff))

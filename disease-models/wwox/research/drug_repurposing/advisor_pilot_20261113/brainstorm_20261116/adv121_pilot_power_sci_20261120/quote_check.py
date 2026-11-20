"""ADV-121: verify each quoted sentence of the result verbatim (whitespace and quote marks normalised) in the held sources.
Usage: python3 -I quote_check.py <obeid_pmc.xml> <mmc2.txt>   (mmc2.txt = pdftotext -layout of mmc2.pdf)"""
import re, sys
def norm(t):
    t = re.sub(r'<[^>]+>', ' ', t)
    t = t.replace('’', "'").replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    return re.sub(r'\s+', ' ', t).strip().lower()
xml = norm(open(sys.argv[1], encoding='utf8').read())
sup = norm(open(sys.argv[2], encoding='utf8').read())
Q = [
 ('xml', 'Statistical analysis was performed using Student\'s t test (* p < 0.05; ** p < 0.01; ns, not significant). Error bars represent mean ± SD.'),
 ('xml', '(C) A graph representing body weight during the first postnatal month in KO + LD and KO + HD mice'),
 ('sup', 'Error bars represent mean ± SD'),
 ('sup', 'Graph represents percentage of Iba1 area in KO compared to WT shown in A'),
 ('sup', 'Graph represents percentage of GFAP area in KO compared to WT shown in C'),
 ('sup', 'Differential quantification of microglia (F) and astrocytes (H) in each treatment'),
 ('sup', 'A graph representing quantification of hindlimb clasping in wild-type (WT), Wwox-null (KO)'),
]
bad = 0
for where, q in Q:
    src = xml if where == 'xml' else sup
    # the XML legend renders the stars as separate glyphs; compare after removing asterisks and spaces around them
    nq = norm(q)
    ok = nq in src or nq.replace('* ', '∗ ') in src or nq.replace('*', '∗') in src or nq.replace('* ', '') in src.replace('∗ ', '')
    print('FOUND' if ok else 'MISSING', where, '|', q[:90])
    bad += 0 if ok else 1
print('quotes %d, found %d' % (len(Q), len(Q) - bad))
sys.exit(1 if bad else 0)

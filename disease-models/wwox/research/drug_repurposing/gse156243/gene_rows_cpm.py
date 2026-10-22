#!/usr/bin/env python3
"""Descriptive per-gene rows of the GSE156243 counts file: raw estimated counts and counts per million (library-size scaled
for display only; NO normalisation model, NO differential test). Usage: gene_rows_cpm.py <counts.gz> <out.tsv> GENE [GENE ...]"""
import gzip,csv,sys
src,out,genes=sys.argv[1],sys.argv[2],sys.argv[3:]
rows={}
with gzip.open(src,'rt') as f:
    r=csv.reader(f,delimiter='\t'); h=next(r)
    for x in r: rows[x[0]]=[float(v) for v in x[1:]]
sums=[sum(v[i] for v in rows.values()) for i in range(6)]
with open(out,'w') as o:
    o.write('gene\t'+'\t'.join('raw_'+c for c in h[1:])+'\t'+'\t'.join('cpm_'+c for c in h[1:])+'\tmeanKO_over_meanWT_cpm\n')
    for g in genes:
        v=rows.get(g)
        if v is None: o.write(g+'\tABSENT\n'); continue
        c=[v[i]/sums[i]*1e6 for i in range(6)]
        o.write(g+'\t'+'\t'.join(f'{x:g}' for x in v)+'\t'+'\t'.join(f'{x:.2f}' for x in c)+f'\t{(sum(c[:4])/4)/((sum(c[4:])/2) or float("nan")):.2f}\n')

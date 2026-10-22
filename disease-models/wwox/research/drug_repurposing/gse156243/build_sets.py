#!/usr/bin/env python3
"""Build S1/S2/S3/S0 gene sets exactly as declared in thresholds_and_query_declaration.md; annotate marker overlap.
Usage: build_sets.py <derived dir> <geo dir>"""
import csv,gzip,json,os,random,sys
der,geo=sys.argv[1:3]
val={}
for r in csv.DictReader(open(os.path.join(der,'symbol_validation.tsv')),delimiter='\t'):
    val[(r['ensg'])]=r
def hg(r):
    v=val[r['ensg']]
    if v['hgnc_symbol_for_ensg']: return v['hgnc_symbol_for_ensg'],v['symbol_status']
    if v['symbol_status']=='approved': return r['symbol'],'approved_ensg_unmapped'
    return None,v['symbol_status']
rows=[]
for fn in ('list_padj_le_0.05.tsv',):
    rows=list(csv.DictReader(open(os.path.join(der,fn)),delimiter='\t'))
markers={}
for r in csv.DictReader(open('marker_sets_declared.tsv'),delimiter='\t'):
    for g in r['genes'].split(','): markers.setdefault(g,[]).append(r['module'])
def sel(thr):
    s={'up':[],'down':[]};dropped=[]
    for r in rows:
        if float(r['padj'])<=thr and abs(float(r['log2FoldChange']))>=0.26:
            g,st=hg(r)
            if g is None: dropped.append((r['symbol'],st)); continue
            s[r['direction']].append(g)
    return s,dropped
S1,d1=sel(0.01);S2,d2=sel(0.05)
S3={k:[g for g in v if g not in markers] for k,v in S1.items()}
removed=sorted({g for v in S1.values() for g in v if g in markers})
universe=[l.strip() for l in open(os.path.join(der,'universe_counts_ge10_proxy.tsv'))][1:]
hs=set(); 
import json as j
docs=j.load(open(os.path.join(geo,'hgnc_complete_set_20261022.json')))['response']['docs']
appr={d['symbol'] for d in docs}
uni=sorted(g for g in universe if g in appr)
random.seed(20261022)
S0={'up':random.sample(uni,len(S1['up'])),'down':random.sample(uni,len(S1['down']))}
out={'S1':S1,'S2':S2,'S3':S3,'S0':S0}
json.dump(out,open(os.path.join(der,'query_sets.json'),'w'),indent=1)
# marker annotation across the full padj<=0.05 list
with open(os.path.join(der,'marker_annotation.tsv'),'w') as f:
    f.write('symbol\tdirection\tpadj\tlog2FoldChange\tmodules\n')
    for r in rows:
        g,_=hg(r)
        m=markers.get(g) or markers.get(r['symbol'])
        if m: f.write(f"{g or r['symbol']}\t{r['direction']}\t{r['padj']}\t{r['log2FoldChange']}\t{'|'.join(m)}\n")
print({k:{d:len(v) for d,v in s.items()} for k,s in out.items()})
print('dropped no-HGNC S1:',d1);print('S2 dropped',len(d2));print('markers removed from S1:',removed)
print('universe approved-symbol proxy',len(uni),'of',len(universe))

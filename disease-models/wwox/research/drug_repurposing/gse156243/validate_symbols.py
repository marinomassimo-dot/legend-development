#!/usr/bin/env python3
"""Validate list symbols and counts-file symbols against an HGNC complete-set JSON, keeping ENSG.
Usage: validate_symbols.py <hgnc json> <geo dir> <derived dir>"""
import json,gzip,csv,sys,os,collections
h,geo,der=sys.argv[1:4]
docs=json.load(open(h))['response']['docs']
approved={d['symbol']:d for d in docs}
prev=collections.defaultdict(list); alias=collections.defaultdict(list); ens={}
for d in docs:
    for p in d.get('prev_symbol',[]): prev[p].append(d['symbol'])
    for a in d.get('alias_symbol',[]): alias[a].append(d['symbol'])
    if 'ensembl_gene_id' in d: ens[d['ensembl_gene_id']]=d['symbol']
def cls(s):
    if s in approved: return 'approved'
    if s in prev: return 'previous_symbol->'+'|'.join(prev[s])
    if s in alias: return 'alias->'+'|'.join(alias[s])
    return 'not_in_HGNC'
out=[];cnt=collections.Counter()
for k in ('up','down'):
    fn={'up':'GSE156243_CKO_CWT_1246_upregulated_genes.txt.gz','down':'GSE156243_CKO_CWT_1021_downregulated_genes.txt.gz'}[k]
    for r in csv.DictReader(gzip.open(os.path.join(geo,fn),'rt'),delimiter='\t'):
        c=cls(r['symbol']); e=ens.get(r['ensg'])
        st='ensg_to_symbol_agrees' if e==r['symbol'] else ('ensg_not_in_HGNC' if e is None else 'ensg_maps_to_'+e)
        cnt[(c.split('->')[0],st.split('_maps')[0])]+=1
        out.append([r['ensg'],r['symbol'],k,c,e or '',st])
with open(os.path.join(der,'symbol_validation.tsv'),'w') as f:
    f.write('ensg\tlist_symbol\tdirection\tsymbol_status\thgnc_symbol_for_ensg\tensg_check\n')
    for o in out: f.write('\t'.join(o)+'\n')
# counts-file symbols
cc=collections.Counter(); notapp=[]
for r in csv.reader(gzip.open(os.path.join(geo,'GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz'),'rt'),delimiter='\t'):
    if r[0]=='gene': continue
    c=cls(r[0]).split('->')[0]; cc[c]+=1
    if c!='approved' and len(notapp)<0: pass
print('list symbols:',dict(cnt)); print('counts-file symbols:',dict(cc))

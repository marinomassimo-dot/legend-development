#!/usr/bin/env python3
"""Qualify the three GSE156243 supplementary files (read-only; no differential test is run).
Usage: qualify.py <dir with the 3 .gz files> <out dir>"""
import gzip, csv, math, sys, hashlib, json, os
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
F = {'counts':'GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz',
     'up':'GSE156243_CKO_CWT_1246_upregulated_genes.txt.gz',
     'down':'GSE156243_CKO_CWT_1021_downregulated_genes.txt.gz'}
def rows(k):
    with gzip.open(os.path.join(src,F[k]),'rt') as f: return list(csv.reader(f,delimiter='\t'))
R={}
# counts
c=rows('counts'); hdr=c[0]; body=c[1:]
ids=[r[0] for r in body]
vals=[[float(x) for x in r[1:]] for r in body]
flat=[v for r in vals for v in r]
R['counts']={'header':hdr,'rows':len(body),'unique_ids':len(set(ids)),'all_finite_nonneg':all(math.isfinite(v) and v>=0 for v in flat),
 'fractional_cells':sum(1 for v in flat if v!=int(v)),'cells':len(flat),
 'rows_total_ge10':sum(1 for r in vals if sum(r)>=10),'rows_total_zero':sum(1 for r in vals if sum(r)==0),
 'column_sums':[round(sum(r[i] for r in vals),1) for i in range(6)]}
# lists
L={}
for k in ('up','down'):
    t=rows(k); h=t[0]; d=[dict(zip(h,r)) for r in t[1:]]
    for x in d:
        for n in ('pvalue','padj','log2FoldChange'): x[n]=float(x[n])
    L[k]=d
    R[k]={'header':h,'rows':len(d),'unique_ensg':len({x['ensg'] for x in d}),'unique_symbol':len({x['symbol'] for x in d}),
      'max_pvalue':max(x['pvalue'] for x in d),'max_padj':max(x['padj'] for x in d),'min_padj':min(x['padj'] for x in d),
      'lfc_sign_ok':all((x['log2FoldChange']>0)==(k=='up') for x in d),
      'padj_le_0.01':sum(x['padj']<=0.01 for x in d),'padj_le_0.05':sum(x['padj']<=0.05 for x in d),
      'padj_gt_0.05':sum(x['padj']>0.05 for x in d),'abs_lfc_min':min(abs(x['log2FoldChange']) for x in d)}
both=L['up']+L['down']
R['union']={'rows':len(both),'unique_ensg':len({x['ensg'] for x in both}),
  'p_only_all_lt_0.01':all(x['pvalue']<0.01 for x in both),'max_padj':max(x['padj'] for x in both),
  'overlap_up_down_ensg':len({x['ensg'] for x in L['up']}&{x['ensg'] for x in L['down']})}
cs=set(ids)
R['universe']={'list_symbols_in_counts_rows':sum(x['symbol'] in cs for x in both),'list_symbols_not_in_counts':[x['symbol'] for x in both if x['symbol'] not in cs][:40],
  'n_list_symbols_not_in_counts':sum(x['symbol'] not in cs for x in both)}
def w(name,data,cols):
    with open(os.path.join(out,name),'w',newline='') as f:
        wr=csv.writer(f,delimiter='\t'); wr.writerow(cols+['direction'])
        for dr,x in data: wr.writerow([x[c] for c in cols]+[dr])
cols=['ensg','symbol','EntrezID','pvalue','padj','log2FoldChange','type']
for name,thr in (('padj_le_0.01',0.01),('padj_le_0.05',0.05)):
    w(f'list_{name}.tsv',[(dr,x) for dr in ('up','down') for x in L[dr] if x['padj']<=thr],cols)
w('list_pvalue_only_NOT_FDR_CONTROLLED.tsv',[(dr,x) for dr in ('up','down') for x in L[dr]],cols)
# tested-universe proxy: paper filter (overall count >=10 on six samples)
with open(os.path.join(out,'universe_counts_ge10_proxy.tsv'),'w') as f:
    f.write('gene\n'); [f.write(i+'\n') for i,r in zip(ids,vals) if sum(r)>=10]
json.dump(R,open(os.path.join(out,'qualification.json'),'w'),indent=1)
print(json.dumps(R,indent=1))

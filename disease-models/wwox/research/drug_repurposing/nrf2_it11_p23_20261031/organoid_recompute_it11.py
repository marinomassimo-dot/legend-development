"""IT11 P2.3 (scientist-c). Independent recomputation from the GEO deposit GSE156243 (not from the IT10 tsv). Usage: python3 -I %s <dir with the three GSE156243 supplementary .gz files>. Reads only; writes to stdout."""
import sys
if len(sys.argv)<2 or sys.argv[1] in ("-h","--help"):
    print(__doc__ % sys.argv[0]); sys.exit(0)
import gzip,sys,statistics as st,math
d=sys.argv[1]
rows={}
with gzip.open(d+'/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz','rt') as f:
    h=f.readline().rstrip('\n').split('\t'); 
    for l in f:
        p=l.rstrip('\n').split('\t'); rows[p[0]]=[float(x) for x in p[1:]]
print('header',h,'ngenes',len(rows))
lib=[sum(r[i] for r in rows.values()) for i in range(6)]
print('libsize',[round(x) for x in lib])
# DESeq2 median-of-ratios size factors (genes with all >0)
import math
lg=[]
for g,r in rows.items():
    if all(x>0 for x in r): lg.append((g,[math.log(x) for x in r]))
gm={g:sum(v)/6 for g,v in lg}
sf=[math.exp(st.median([v[i]-gm[g] for g,v in lg])) for i in range(6)]
print('sizefactors',[round(x,3) for x in sf],'n genes used',len(lg))
def ratio(vals): ko=sum(vals[:4])/4; wt=sum(vals[4:])/2; return ko/wt if wt>0 else float('nan')
print('gene\tCPMratio\tMoRratio\tlog2MoR\tKOcounts\tWTcounts\tKO_cpm_each\tWT_cpm_each')
for g in ['NFE2L2','NQO1','HMOX1','KEAP1','IL6','IL1B','TNF','IL1A','P2RY12','AIF1','TMEM119','WWOX','GFAP','CX3CR1','PTPRC']:
    r=rows.get(g)
    if r is None: print(g,'ABSENT');continue
    cpm=[r[i]/lib[i]*1e6 for i in range(6)]
    mor=[r[i]/sf[i] for i in range(6)]
    rm=ratio(mor)
    print(g,round(ratio(cpm),3) if ratio(cpm)==ratio(cpm) else 'nan',round(rm,3) if rm==rm else 'nan',round(math.log2(rm),2) if rm==rm and rm>0 else 'na',[round(x,1) for x in r[:4]],[round(x,1) for x in r[4:]],[round(x,2) for x in cpm[:4]],[round(x,2) for x in cpm[4:]],sep='\t')
# DE tables
for fn in ['upregulated','downregulated']:
    import glob
    p=glob.glob(d+'/*%s*'%fn)[0]
    with gzip.open(p,'rt') as f:
        hh=f.readline().split('\t'); n=0
        for l in f:
            n+=1; q=l.split('\t')
            if q[1] in ('NFE2L2','NQO1','HMOX1','KEAP1','IL6','IL1B','TNF','WWOX','TMEM119','AIF1'): print(fn,q[1],'p',q[3],'padj',q[4],'log2FC',q[5])
        print(fn,'rows',n)

"""IT11 P2.3 (scientist-c). Independent recomputation from the GEO deposit GSE156243 (not from the IT10 tsv). Usage: python3 -I %s <dir with the three GSE156243 supplementary .gz files>. Reads only; writes to stdout."""
import sys
if len(sys.argv)<2 or sys.argv[1] in ("-h","--help"):
    print(__doc__ % sys.argv[0]); sys.exit(0)
import gzip,math,statistics as st,sys
d=sys.argv[1]
rows={};
with gzip.open(d+'/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz','rt') as f:
    f.readline()
    for l in f:
        p=l.rstrip('\n').split('\t'); rows[p[0]]=[float(x) for x in p[1:]]
lib=[sum(r[i] for r in rows.values()) for i in range(6)]
def cpm(g): return [rows[g][i]/lib[i]*1e6 for i in range(6)]
def welch(a,b):
    ma,mb=st.mean(a),st.mean(b); va,vb=st.variance(a),st.variance(b)
    se=math.sqrt(va/len(a)+vb/len(b)); t=(ma-mb)/se
    df=(va/len(a)+vb/len(b))**2/((va/len(a))**2/(len(a)-1)+(vb/len(b))**2/(len(b)-1)); return t,df
# exact permutation test on log2(cpm+0.1) mean difference, C(6,4)=15 splits
import itertools
for g in ['NFE2L2','NQO1','HMOX1','KEAP1','SRXN1','GSR','G6PD','TMEM119']:
    x=[math.log2(v+0.1) for v in cpm(g)]; ko=x[:4]; wt=x[4:]
    t,df=welch(ko,wt)
    obs=abs(st.mean(ko)-st.mean(wt)); cnt=0; tot=0
    for c in itertools.combinations(range(6),4):
        a=[x[i] for i in c]; b=[x[i] for i in range(6) if i not in c]
        tot+=1; cnt+= abs(st.mean(a)-st.mean(b))>=obs-1e-12
    print(g,'KO cpm range',round(min(cpm(g)[:4]),2),round(max(cpm(g)[:4]),2),'WT',[round(v,2) for v in cpm(g)[4:]],'Welch t',round(t,2),'df',round(df,1),'exact perm p (15 splits, min 0.133)',round(cnt/tot,3))
# totals for cytokines & microglia genes
for g in ['IL6','IL1B','TNF','IL1A','IL18','CSF1R','P2RY12','CX3CR1','TMEM119','PTPRC','AIF1','ITGAM','CD68','GFAP','AQP4','S100B','SLC1A3','NLRP3','CASP1']:
    if g in rows: print(g,'counts',[round(v,1) for v in rows[g]],'sum',round(sum(rows[g]),1))
    else: print(g,'ABSENT from table')

import sys,json,re,gzip,numpy as np,collections
D=sys.argv[1]
f=gzip.open(D+'/data/rich.txt.gz','rt')
hdr=f.readline().rstrip('\n').split('\t')[1:]
ids=[];rows=[]
for ln in f:
    p=ln.rstrip('\n').split('\t'); ids.append(p[0]); rows.append(np.array([float(x) if x not in ('NA','') else 0.0 for x in p[1:]],dtype=np.float32))
X=np.vstack(rows); print(X.shape)
gene=np.array([i.split('_')[0] for i in ids])
cpm=X/X.sum(axis=0)*1e6
S=json.load(open(D+'/samples.json')); lib2={r[4]:r for r in S}
col={c:i for i,c in enumerate(hdr)}
scr=collections.defaultdict(lambda:{'T0':[],'late':[],'gt':''})
for c in hdr:
    r=lib2.get(c)
    if not r: continue
    m=re.match(r'(GIN\d+)_(T\d+)([A-C]?)',r[1])
    if not m: continue
    k='T0' if m.group(2)=='T0' else 'late'
    scr[m.group(1)][k].append(col[c]); scr[m.group(1)]['gt']=r[2]
ug,inv=np.unique(gene,return_inverse=True)
def genemedian(v):
    out=np.zeros(len(ug),dtype=np.float32)
    order=np.argsort(inv,kind='stable'); sv=v[order]; si=inv[order]
    b=np.flatnonzero(np.diff(si))+1; parts=np.split(sv,b)
    for i,p in enumerate(parts): out[i]=np.median(p)
    return out
L={}
for g,v in scr.items():
    if not v['T0'] or len(v['late'])<2: continue
    t0=np.log2(cpm[:,v['T0']].mean(axis=1)+0.5); late=np.log2(cpm[:,v['late']].mean(axis=1)+0.5)
    L[g]=genemedian(late-t0)
names=sorted(L); M=np.vstack([L[g] for g in names])  # screens x genes
ko='GIN352'
wt=[g for g in names if re.match(r'^(WT|Parental)',scr[g]['gt']) and 'del' not in scr[g]['gt']]
print('screens',len(names),'WT',len(wt),'KO present',ko in L,scr[ko]['gt'],'late reps',len(scr[ko]['late']))
gi={g:i for i,g in enumerate(ug)}
ess=[gi[g] for g in ug if re.match(r'^(RPL|RPS)\d',g)]
Mw=M[[names.index(g) for g in wt]]
kov=L[ko]
print('QC ribosomal median LFC KO',round(float(np.median(kov[ess])),2),'| WT screens median of medians',round(float(np.median(np.median(Mw[:,ess],axis=1))),2))
wm=Mw.mean(axis=0); ws=Mw.std(axis=0).clip(min=0.15)
z=(kov-wm)/ws
print('corr KO vs WT mean',round(float(np.corrcoef(kov,wm)[0,1]),3))
loo=[]
for i in range(len(wt)):
    o=np.delete(Mw,i,axis=0); m=o.mean(axis=0); s=o.std(axis=0).clip(min=0.15); zz=(Mw[i]-m)/s
    loo.append((int((zz<-4).sum()),int((zz>4).sum()), float(np.corrcoef(Mw[i],m)[0,1])))
print('LOO null per WT screen: median n(z<-4)',np.median([a for a,b,c in loo]),'median n(z>4)',np.median([b for a,b,c in loo]),'median corr',round(float(np.median([c for a,b,c in loo])),3))
print('WWOX-KO: n(z<-4)',int((z<-4).sum()),'n(z>4)',int((z>4).sum()))
o=np.argsort(z)
print('most negative z:',[(ug[i],round(float(z[i]),1),round(float(kov[i]),2),round(float(wm[i]),2)) for i in o[:20]])
pos=[i for i in o[::-1] if wm[i]>-1.0][:20]
print('most positive z (WT mean LFC>-1):',[(ug[i],round(float(z[i]),1),round(float(kov[i]),2),round(float(wm[i]),2)) for i in pos])
w=gi.get('WWOX'); print('WWOX own guides in KO: LFC',kov[w],'WT mean',wm[w],'z',z[w])
with open(D+'/wwox_ko_vs_wt_gene_lfc.tsv','w') as fo:
    fo.write('gene\tz\tko_lfc\twt_mean_lfc\twt_sd\n')
    for i in o: fo.write(f'{ug[i]}\t{z[i]:.3f}\t{kov[i]:.3f}\t{wm[i]:.3f}\t{ws[i]:.3f}\n')
# IT11 P5 note: run as `python3 -I gse298081_wwox_ko_screen_check.py <DIR>` where <DIR> holds data/rich.txt.gz (GSE298081_gin_read_counts_matrix_rich.txt.gz,
# GEO FTP, 83,673,734 bytes) and samples.json (library name -> GEO sample, parsed from the GEO brief SOFT text of GSE298081). Needs numpy only.
# Crude screen-level check, NOT the authors' genetic-interaction score: per gene median guide log2 fold change (late/T0, CPM, +0.5) for the WWOX query screen (GIN352,
# one clone, 3 late replicates) against the mean/sd of 15 parental-WT screens of other batches in the same matrix.

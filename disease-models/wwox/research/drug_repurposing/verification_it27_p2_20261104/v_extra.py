"""Verifier: 2-HG interaction, extra views. Usage: python3 -I v_extra.py <out_dir>
 * cell geometric means and fold changes (TIC-normalised areas)
 * additive-scale (linear area) interaction, pooled-MSE t test
 * residual-permutation test of the log2 interaction contrast under the additive null (20000 permutations, seed 1)
Metabolite 2-HG only (pre-declared question). Lactate shown alongside as the authors' own interaction hit (diagnostic)."""
import sys,os,csv,json
import numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import vstats as V
out=sys.argv[1]
rows=list(csv.DictReader(open(os.path.join(out,'v_areas_long.tsv')),delimiter='\t'))
CELL={('RNAi Control','LacZ'):(0,0),('Wwox RNAi','LacZ'):(1,0),('RNAi Control','AB42'):(0,1),('Wwox RNAi','AB42'):(1,1)}
files={r['file']:CELL[(r['group_wwox'],r['group_amyloid'])] for r in rows if r['assay_name'].endswith('_KDExp')}
tic={r['file']:float(r['tic']) for r in rows};fl=sorted(files);tm=np.median([tic[f] for f in fl])
res={}
for t in ('hydroxyglutarate','lactate'):
    a={r['file']:float(r['area'])/tic[r['file']]*tm for r in rows if r['target']==t and r['ppm']=='5' and r['file'] in files}
    X=np.array([[1,files[f][0],files[f][1],files[f][0]*files[f][1]] for f in fl],float)
    y=np.log2([a[f] for f in fl])
    cells={k:[a[f] for f in fl if files[f]==k] for k in set(files.values())}
    gm={str(k):float(2**np.mean(np.log2(v))) for k,v in cells.items()}
    # linear-scale interaction
    lin=V.twoway({k:np.array(v) for k,v in cells.items()})['interaction']
    # permutation (Freedman-Lane style): residuals of the additive model permuted, refit full model
    Xa=X[:,:3];beta=np.linalg.lstsq(Xa,y,rcond=None)[0];fit=Xa@beta;resid=y-fit
    def tint(yy):
        b,rss,_,_=np.linalg.lstsq(X,yy,rcond=None);r=yy-X@b;df=len(yy)-4;s2=(r@r)/df
        cov=s2*np.linalg.inv(X.T@X);return b[3]/np.sqrt(cov[3,3])
    t0=tint(y);rng=np.random.default_rng(1);cnt=0;N=20000
    for _ in range(N):
        cnt+= abs(tint(fit+rng.permutation(resid)))>=abs(t0)-1e-12
    res[t]=dict(cell_geometric_means_TIC={'C(ctrl,LacZ)':gm['(0, 0)'],'D(Wwox,LacZ)':gm['(1, 0)'],'G(ctrl,Abeta)':gm['(0, 1)'],'H(Wwox,Abeta)':gm['(1, 1)']},
       FC_KD_in_LacZ=gm['(1, 0)']/gm['(0, 0)'],FC_KD_in_Abeta=gm['(1, 1)']/gm['(0, 1)'],FC_Abeta_in_ctrl=gm['(0, 1)']/gm['(0, 0)'],
       ratio_of_ratios=(gm['(1, 1)']/gm['(0, 1)'])/(gm['(1, 0)']/gm['(0, 0)']),
       log2_interaction_t=float(t0),permutation_p_interaction=(cnt+1)/(N+1),linear_scale_interaction=dict(est=lin['est'],p=lin['p'],ci95=lin['ci95']))
json.dump(res,open(os.path.join(out,'v_extra.json'),'w'),indent=1,default=float)
print(json.dumps(res,indent=1,default=float))

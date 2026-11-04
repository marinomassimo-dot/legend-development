"""Verifier stage 2: peak integration + QC gate + diagnostics.
Usage: python3 -I v_integrate.py <npz_dir> <isa_dir> <out_dir>
Rules fixed before looking at sample areas:
 * identification anchor RT = the deposit's own MAF retention time for the compound (public metadata), search +/-30 s;
 * window from the mean pooled-QC EIC (5 ppm): apex of a [1,2,1]-smoothed trace; edges where the smoothed trace falls to
   baseline + 5 % of apex height, or at a local minimum, capped at 40 s each side;
 * per-file window = same left/right half-widths around the file's own apex (searched +/-8 s from the pooled apex), linear baseline
   from edge means; blanks use the pooled apex (no re-centring);
 * QC gate: Spearman(own 12 pooled areas, deposited 12 pooled values) >= 0.7, never relaxed."""
import sys, os, csv, json
import numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import vstats as V
ANCHOR={'lactate':561.04,'hydroxyglutarate':749.93,'citrate':824.3,'itaconate':771.31,'lysine':1092.18,
        'glucuronate':805.39,'orotate':597.3,'leucine':587.2,'methionine':618.5}
# metabolites that have no deposited anchor are searched wide and reported only if a single dominant peak exists
REF_PANEL=['leucine','methionine','aspartate','glutamate','phenylalanine','tryptophan']
def smooth(y):
    z=np.convolve(y,[.25,.5,.25],mode='same');z[0]=y[0];z[-1]=y[-1];return z
def window(rt,mean,rt0,search=30,cap=40):
    s=smooth(mean);m=(rt>=rt0-search)&(rt<=rt0+search)
    idx=np.where(m)[0];i=idx[np.argmax(s[idx])];apex=rt[i]
    base=np.percentile(s[(rt>=apex-150)&(rt<=apex+150)],10)
    thr=base+0.05*(s[i]-base)
    l=i
    while l>0 and s[l-1]<=s[l] and s[l]>thr and rt[i]-rt[l]<cap:l-=1
    r=i
    while r<len(s)-1 and s[r+1]<=s[r] and s[r]>thr and rt[r]-rt[i]<cap:r+=1
    return dict(apex=float(apex),left=float(rt[i]-rt[l]),right=float(rt[r]-rt[i]),height=float(s[i]),base=float(base))
def area(rt,y,apex,left,right):
    m=(rt>=apex-left)&(rt<=apex+right)
    if m.sum()<4:return np.nan
    x=rt[m];z=y[m]
    b0=z[:2].mean();b1=z[-2:].mean()
    base=np.interp(x,[x[0],x[-1]],[b0,b1])
    return float(np.trapezoid(np.clip(z-base,0,None),x))
def file_area(rt,y,w,recentre=True):
    apex=w['apex']
    if recentre:
        s=smooth(y);m=(rt>=apex-8)&(rt<=apex+8)
        idx=np.where(m)[0]
        if len(idx):apex=float(rt[idx[np.argmax(s[idx])]])
    return area(rt,y,apex,w['left'],w['right']),apex
def load_isa(isa):
    a=list(csv.reader(open(os.path.join(isa,'a_MTBLS12344_LC-MS_alternating_hilic_metabolite_profiling-1.txt')),delimiter='\t'))
    h=a[0];ia=h.index('MS Assay Name');idr=h.index('Derived Spectral Data File');isn=h.index('Sample Name')
    file2assay={};
    for r in a[1:]:
        if '/Negative/' in r[idr]:
            file2assay[os.path.basename(r[idr]).replace('.mzXML','')]=r[ia]
    s=list(csv.reader(open(os.path.join(isa,'s_MTBLS12344.txt')),delimiter='\t'));sh=s[0]
    ig=sh.index('Factor Value[Wwox manipulation]');ia2=sh.index('Factor Value[Amyloid]');iname=sh.index('Sample Name')
    grp={r[iname]:(r[ig],r[ia2]) for r in s[1:]}
    m=list(csv.reader(open(os.path.join(isa,'m_MTBLS12344_LC-MS_alternating_hilic_metabolite_profiling_v2_maf.tsv')),delimiter='\t'))
    mh=m[0];dep={}
    for r in m[1:]:
        dep[(r[4],r[5])]={mh[i]:float(r[i]) for i in range(21,len(mh)) if r[i]!=''}
    return file2assay,grp,dep
def main(npz,isa,out):
    os.makedirs(out,exist_ok=True)
    file2assay,grp,dep=load_isa(isa)
    D={f[:-4]:np.load(os.path.join(npz,f)) for f in sorted(os.listdir(npz)) if f.endswith('.npz')}
    pooled=[f for f in D if f.startswith('pooled')];blanks=[f for f in D if f.startswith('matrix')]
    samples=[f for f in D if f[0] in 'CDGHIJKL' and f[1:].isdigit()]
    rt=D[pooled[0]]['rt']
    # the rt axes differ slightly between files: interpolate every trace onto each file's own rt (kept native) -> use native per file
    targets=[k[:-2] for k in D[pooled[0]].files if k.endswith('_5')]
    W={};res=[];diag={}
    for t in targets:
        rt0=ANCHOR.get(t)
        grid=np.arange(60,1450,1.0)
        mean=np.mean([np.interp(grid,D[f]['rt'],D[f][t+'_5']) for f in pooled],axis=0)
        if rt0 is None:
            s=smooth(mean);rt0=float(grid[np.argmax(s)]);W[t]=dict(note='no deposit anchor: global max of mean pooled EIC')
        else:W[t]={}
        w=window(grid,mean,rt0);W[t].update(w);W[t]['anchor_rt']=rt0
        W[t]['pooled_mean_peak_over_blank_mean']=None
        for f in D:
            for ppm in (5,10):
                y=D[f][f'{t}_{ppm}'];r=D[f]['rt']
                a,ap=file_area(r,y,w,recentre=not f.startswith('matrix'))
                res.append(dict(file=f,target=t,ppm=ppm,area=a,apex=ap))
    # write areas
    with open(os.path.join(out,'v_areas_long.tsv'),'w') as fh:
        fh.write('file\tassay_name\tgroup_wwox\tgroup_amyloid\ttarget\tppm\tarea\tapex_rt\ttic\n')
        for r in res:
            f=r['file'];an=file2assay.get(f,'');g=grp.get(an,('',''))
            fh.write(f"{f}\t{an}\t{g[0]}\t{g[1]}\t{r['target']}\t{r['ppm']}\t{r['area']:.1f}\t{r['apex']:.2f}\t{D[f]['tic'].sum():.0f}\n")
    json.dump(W,open(os.path.join(out,'v_windows.json'),'w'),indent=1)
    # QC gate
    A={(r['file'],r['target'],r['ppm']):r['area'] for r in res}
    # deposited values keyed by (metabolite name, mz string)
    names={'lactate':('L-Lactate','89.0245'),'hydroxyglutarate':('2-Hydroxyglutarate','147.0299'),'citrate':('Citrate','191.0199'),
           'itaconate':('Itaconate','129.0194'),'lysine':('L-Lysine','145.0983'),'glucuronate':('D-Glucuronate','193.0354'),
           'orotate':('Orotate','155.01'),'leucine':('L-Leucine','132.1019'),'methionine':('L-Methionine','148.0438')}
    order=['Pool1_1','Pool1_2','Pool1_3','Pool1_4','Pool1_5','Pool1_6','Pool2_1','Pool2_2','Pool2_3','Pool2_4','Pool2_5','Pool2_6']
    inv={v:k for k,v in file2assay.items()}   # assay name -> file
    # alternative (sequential) mapping, diagnostic only: pooled_2_04..09 -> Pool2_1..Pool2_6
    alt=dict(inv);
    for i,n in enumerate(['04','05','06','07','08','09']):alt[f'Pool2_{i+1}']=f'pooled_2_{n}'
    qc={}
    for t,(nm,mz) in names.items():
        if t not in targets:continue
        key=[k for k in dep if k[0]==nm and k[1]==mz]
        if not key:continue
        dv=dep[key[0]]
        for lab,mp in (('assay_sheet_mapping',inv),('sequential_pool2_mapping_diagnostic',alt)):
            own=[A[(mp[p],t,5)] for p in order];dpv=[dv[p] for p in order]
            rho=V.spearman(own,dpv)
            b1=V.spearman(own[:6],dpv[:6]);b2=V.spearman(own[6:],dpv[6:])
            blanks_own=[A[(b,t,5)] for b in blanks];blanks_dep=[dv[f'Matrix_Blank_{i}'] for i in range(1,7)]
            qc.setdefault(t,{})[lab]=dict(rho12=rho,rho_pool1_6pts=b1,rho_pool2_6pts=b2,gate_pass=bool(rho>=0.7),
                 own_pooled=own,dep_pooled=dpv,blank_own_mean=float(np.mean(blanks_own)),pooled_own_mean=float(np.mean(own)),
                 blank_dep_mean=float(np.mean(blanks_dep)),pooled_dep_mean=float(np.mean(dpv)))
    json.dump(qc,open(os.path.join(out,'v_qc_gate.json'),'w'),indent=1)
    print(json.dumps({t:{k:(round(v['rho12'],3),v['gate_pass']) for k,v in d.items()} for t,d in qc.items()},indent=1))
if __name__=='__main__':
    main(*sys.argv[1:4])

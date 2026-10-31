#!/usr/bin/env python3
"""Verifier p1b analysis per plan.md. Usage: verify_analysis.py <dir with ctrl.npz ko.npz> <outdir>. --help safe."""
import sys, json, numpy as np
from collections import Counter
if len(sys.argv)<3 or sys.argv[1] in("-h","--help"):
    print(__doc__); sys.exit(0)
SD, OUT = sys.argv[1], sys.argv[2]
P = dict(
 gen=["Snap25","Syt1","Rbfox3","Stmn2","Rbfox1"],
 exc=["Slc17a7","Slc17a6","Camk2a","Satb2","Neurod6","Cux2"],
 inh=["Gad1","Gad2","Slc32a1"],
 olg=["Mog","Mobp","Mag","Cldn11","Opalin","St18"],
 opc=["Pdgfra","Cspg4","Vcan","Ptprz1"],
 ast=["Aqp4","Slc1a2","Slc1a3","Aldh1l1","Gja1","Gfap"],
 mic=["Csf1r","Cx3cr1","P2ry12","Tmem119","Inpp5d","Dock8"])
OLG_NAIVE = P["olg"]+["Mbp","Plp1"]
IMM=["Nnat","Sox11","Dcx","Sox4","Tubb3","Igfbpl1"]
def wilson(k,n):
    if n==0: return (float("nan"),)*2
    z=1.96;p=k/n;d=1+z*z/n;c=(p+z*z/(2*n))/d;h=z*np.sqrt(p*(1-p)/n+z*z/(4*n*n))/d
    return (c-h,c+h)
class Arm:
    def __init__(s,name,dup="first"):
        z=np.load(f"{SD}/{name}.npz"); s.name=name; s.X=z["X"].astype(np.int32); s.sym=z["sym"]; s.ids=z["ids"]
        s.idx={}
        for i,g in enumerate(s.sym): s.idx.setdefault(g,[]).append(i)
        s.dup=dup
    def g(s,gene,X=None):
        X=s.X if X is None else X
        ii=s.idx.get(gene)
        if ii is None: return np.zeros(X.shape[0],int)
        if s.dup=="first" or len(ii)==1: return X[:,ii[0]]
        if s.dup=="sum": return X[:,ii].sum(1)
        if s.dup=="last": return X[:,ii[-1]]
        if s.dup=="max":
            t=[X[:,i].sum() for i in ii]; return X[:,ii[int(np.argmax(t))]]
        if s.dup=="lowid":
            j=min(ii,key=lambda i:s.ids[i]); return X[:,j]
    def ndet(s,genes,X=None,thr=1):
        return sum((s.g(x,X)>=thr).astype(int) for x in genes)
def classify(a,X=None,rule="R1",strict=False,naive=False):
    thr=1
    G=lambda k:a.ndet(P[k],X)
    def pos(k,need=2):
        if strict:
            tot=sum(a.g(x,X) for x in P[k]); return (G(k)>=need)&(tot>=3)
        return G(k)>=need
    gen=G("gen");exc=pos("exc");inh=pos("inh")
    neu=(exc|inh)&(gen>=1)
    olgp=P["olg"] if not naive else OLG_NAIVE
    olg=(sum((a.g(x,X)>=1).astype(int) for x in olgp)>=2)
    opc=pos("opc");ast=pos("ast");mic=pos("mic")
    comp=np.vstack([neu,olg,opc,ast,mic]).T
    npos=comp.sum(1)
    n=len(npos); cls=np.array(["unassigned"]*n,dtype=object)
    names=["neuron","oligodendrocyte","OPC","astrocyte","microglia"]
    if rule=="R0":
        # highest detection fraction, ties unassigned
        fr=np.vstack([np.maximum(G("exc")/len(P["exc"]),G("inh")/len(P["inh"])),
                      sum((a.g(x,X)>=1).astype(int) for x in olgp)/len(olgp),
                      G("opc")/len(P["opc"]),G("ast")/len(P["ast"]),G("mic")/len(P["mic"])]).T
        mx=fr.max(1); top=(fr==mx[:,None]).sum(1)
        for i in range(n):
            if mx[i]>=2/6 and top[i]==1: cls[i]=names[int(fr[i].argmax())]
        excl=np.zeros(n,bool)
    else:
        for i in range(n):
            if npos[i]==1: cls[i]=names[int(np.argmax(comp[i]))]
        excl=npos>=2
        cls[excl]="ambiguous"
    sub=np.array([""]*n,dtype=object)
    for i in range(n):
        if cls[i]=="neuron":
            if exc[i] and inh[i]: sub[i]="EI_ambiguous"
            elif inh[i]: sub[i]="inh"
            else: sub[i]="exc"
    return cls,sub,excl,comp
def frac(k,n): lo,hi=wilson(k,n); return dict(k=int(k),n=int(n),p=(k/n if n else float("nan")),lo=lo,hi=hi)
def pv_defs(a,X,inh):
    g=lambda x:a.g(x,X)
    pvalb=g("Pvalb");sst=g("Sst");vip=g("Vip");lhx6=g("Lhx6");htr=g("Htr3a")
    co=(g("Kcnc1")>=1)|(g("Syt2")>=1)|(g("Kcna1")>=1)
    d=dict(
      PV_A=inh&(pvalb>=1), PV_A_strict=inh&(pvalb>=2),
      PV_A_co=inh&(pvalb>=1)&co&(sst==0)&(vip==0),
      PV_B=inh&(lhx6>=1)&(sst==0)&(vip==0)&(htr==0),
      PV_B_pvalb0=inh&(lhx6>=1)&(sst==0)&(vip==0)&(htr==0)&(pvalb==0),
      PV_B_pvalb1=inh&(lhx6>=1)&(sst==0)&(vip==0)&(htr==0)&(pvalb>=1),
      PV_A_notB=inh&(pvalb>=1)&~((lhx6>=1)&(sst==0)&(vip==0)&(htr==0)),
      SST=inh&(sst>=1), SST_pvalb0=inh&(sst>=1)&(pvalb==0), VIP=inh&(vip>=1),
      Lhx6_any=inh&(lhx6>=1), Pvalb_Sst_both=inh&(pvalb>=1)&(sst>=1), Pvalb_Vip_both=inh&(pvalb>=1)&(vip>=1))
    return d
def summarize(a,cls,sub,X=None,tag=""):
    n=len(cls); R={}
    R["n_all"]=n
    cnt=Counter(cls); R["class_counts"]=dict(cnt)
    neu=(cls=="neuron"); inh=neu&(sub=="inh"); exc=neu&(sub=="exc")
    R["neurons"]=int(neu.sum()); R["inh"]=int(inh.sum()); R["exc"]=int(exc.sum()); R["EI_amb"]=int((sub=="EI_ambiguous").sum())
    nonneu=np.isin(cls,["oligodendrocyte","OPC","astrocyte","microglia"])
    R["glia_total"]=int(nonneu.sum())
    for k in("oligodendrocyte","OPC","astrocyte","microglia"):
        R[f"{k}_of_all"]=frac(cnt[k],n)
        R[f"{k}_of_classified_nonamb"]=frac(cnt[k],n-cnt["ambiguous"]-cnt["unassigned"])
        R[f"{k}_of_nonneuronal"]=frac(cnt[k],int(nonneu.sum()))
    R["neuron_of_all"]=frac(neu.sum(),n)
    R["inh_of_neurons"]=frac(inh.sum(),neu.sum())
    pv=pv_defs(a,X,inh)
    R["pv"]={}
    for k,v in pv.items():
        R["pv"][k]=dict(n=int(v.sum()),of_inh=frac(v.sum(),inh.sum()),of_neurons=frac(v.sum(),neu.sum()),of_all=frac(v.sum(),n))
    R["inh_Pvalb_ge1"]=frac((inh&(a.g("Pvalb",X)>=1)).sum(),inh.sum())
    R["inh_Pvalb_ge1_UMI_total"]=int(a.g("Pvalb",X)[inh].sum())
    # immature
    imm={}
    for g in IMM: imm[g]=frac((a.g(g,X)[neu]>=1).sum(),neu.sum())
    nimm=sum((a.g(g,X)>=1).astype(int) for g in IMM)
    imm["ge2of6"]=frac((nimm[neu]>=2).sum(),neu.sum())
    R["immature_in_neurons"]=imm
    # Wwox by class
    w=a.g("Wwox",X); tot=(X if X is not None else a.X).sum(1)
    R["wwox"]={}
    for c in ["neuron","exc","inh","oligodendrocyte","OPC","astrocyte","microglia","ambiguous","unassigned"]:
        m=(sub==c) if c in("exc","inh") else (cls==c)
        if c in("exc","inh"): m=neu&(sub==c)
        if m.sum()==0: continue
        R["wwox"][c]=dict(n=int(m.sum()),umi=int(w[m].sum()),mean_umi=float(w[m].mean()),det=frac((w[m]>=1).sum(),m.sum()),per10k=float(w[m].sum()/tot[m].sum()*1e4))
    return R
LAB={}
def main():
    out={}
    for name in("ctrl","ko"):
        a=Arm(name); X=a.X
        r={}
        tot=X.sum(1); ngene=(X>0).sum(1)
        mt=np.array([s.startswith("mt-") for s in a.sym]); mtf=X[:,mt].sum(1)/tot
        r["qc"]=dict(n=int(len(tot)),median_umi=float(np.median(tot)),mean_umi=float(tot.mean()),median_genes=float(np.median(ngene)),mt_frac_median=float(np.median(mtf)),
                     umi_q10=float(np.quantile(tot,.1)),umi_q90=float(np.quantile(tot,.9)),total_umi=int(tot.sum()))
        # duplicates
        dups={g:c for g,c in Counter(a.sym).items() if c>1}
        r["n_dup_symbols"]=len(dups)
        for rule,kw in [("R0",dict(rule="R0")),("R1",dict(rule="R1")),("R2",dict(rule="R1",strict=True)),("NAIVE",dict(rule="R1",naive=True))]:
            cls,sub,excl,comp=classify(a,**kw)
            r[rule]=summarize(a,cls,sub)
            LAB[(name,rule)]=(cls.copy(),sub.copy())
            r[rule]["excluded_n"]=int(excl.sum()); r[rule]["excluded_frac"]=frac(excl.sum(),len(cls))
            if rule=="R1":
                cls1,sub1=cls,sub
                pairs=Counter()
                for i in np.where(excl)[0]:
                    pairs["+".join(n for n,b in zip(["neuron","olg","opc","ast","mic"],comp[i]) if b)]+=1
                r[rule]["ambiguous_composition"]=dict(pairs)
            if rule=="NAIVE":
                pairs=Counter()
                for i in np.where(excl)[0]:
                    pairs["+".join(n for n,b in zip(["neuron","olg","opc","ast","mic"],comp[i]) if b)]+=1
                r[rule]["ambiguous_composition"]=dict(pairs)
        # who changes between R1 and NAIVE
        clsN,_,_,_=classify(a,rule="R1",naive=True)
        r["R1_vs_NAIVE_transition"]={f"{x}->{y}":int(c) for (x,y),c in Counter(zip(cls1,clsN)).items() if x!=y}
        # ambient: neurons Mbp/Plp1 vs Wwox/other olg markers
        neu=(cls1=="neuron")
        myel=a.g("Mbp")+a.g("Plp1")
        r["ambient"]={}
        r["ambient"]["neurons_Mbp_or_Plp1_ge1"]=frac((myel[neu]>=1).sum(),neu.sum())
        r["ambient"]["neurons_Mbp_ge3"]=frac((a.g("Mbp")[neu]>=3).sum(),neu.sum())
        olgm=cls1=="oligodendrocyte"
        r["ambient"]["olg_median_Mbp"]=float(np.median(a.g("Mbp")[olgm])) if olgm.any() else None
        r["ambient"]["neuron_median_Mbp"]=float(np.median(a.g("Mbp")[neu]))
        r["ambient"]["neuron_mean_Mbp"]=float(a.g("Mbp")[neu].mean())
        r["ambient"]["olg_mean_Mbp"]=float(a.g("Mbp")[olgm].mean()) if olgm.any() else None
        w=a.g("Wwox")
        def corr(x,y):
            return float(np.corrcoef(x,y)[0,1]) if x.std()>0 and y.std()>0 else None
        lt=np.log1p(X.sum(1))
        r["ambient"]["neuron_corr_Wwox_vs_Mbp+Plp1"]=corr(w[neu],myel[neu])
        r["ambient"]["neuron_corr_Wwox_vs_logUMI"]=corr(w[neu],lt[neu])
        r["ambient"]["neuron_corr_Mbp+Plp1_vs_logUMI"]=corr(myel[neu],lt[neu])
        r["ambient"]["neuron_corr_Mog_vs_Mbp+Plp1"]=corr(a.g("Mog")[neu],myel[neu])
        # glia non-olg Wwox vs myelin
        # soup
        p=X.sum(0).astype(float); p/=p.sum()
        pm=p[a.idx["Mbp"][0]]+p[a.idx["Plp1"][0]]
        r["ambient"]["soup_myelin_fraction_of_pooled"]=float(pm)
        # R3 correct
        N=X.sum(1).astype(float)
        rho=np.clip(myel/(N*pm),0,0.5); rho[cls1=="oligodendrocyte"]=0
        # for non-OLG nuclei only
        r["ambient"]["rho_median_nonolg"]=float(np.median(rho[cls1!="oligodendrocyte"]))
        r["ambient"]["rho_mean_neurons"]=float(rho[neu].mean())
        exp=rho[:,None]*N[:,None]*p[None,:]
        Xc=np.floor(np.maximum(X-exp,0)+0.5).astype(np.int32)  # round to nearest
        cls3,sub3,excl3,comp3=classify(a,X=Xc,rule="R1")
        r["R3"]=summarize(a,cls3,sub3,X=Xc); r["R3"]["excluded_n"]=int(excl3.sum()); r["R3"]["excluded_frac"]=frac(excl3.sum(),len(cls3))
        r["R3"]["transition_vs_R1"]={f"{x}->{y}":int(c) for (x,y),c in Counter(zip(cls1,cls3)).items() if x!=y}
        # low-UMI quintile check
        q=tot<=np.quantile(tot,.2)
        r["lowUMI_q20"]=dict(n=int(q.sum()),class_counts=dict(Counter(cls1[q])),ambig_frac=float((cls1[q]=="ambiguous").mean()),ambig_frac_rest=float((cls1[~q]=="ambiguous").mean()),
                              olg_frac=float((cls1[q]=="oligodendrocyte").mean()),olg_frac_rest=float((cls1[~q]=="oligodendrocyte").mean()))
        # depth-matched downsample (binomial thinning to common target)
        r["_cls1"]=cls1; r["_sub1"]=sub1; r["_X"]=None
        out[name]=r
    # depth-matching downsample (POST-HOC, labelled): thin both arms to ctrl/ko common median UMI
    tgt=min(out["ctrl"]["qc"]["median_umi"],out["ko"]["qc"]["median_umi"])
    rng=np.random.default_rng(20261101)
    for name in("ctrl","ko"):
        a=Arm(name); X=a.X; N=X.sum(1)
        keep=np.minimum(1.0,tgt/np.median(N)*np.ones(len(N)))  # global thinning factor
        Xt=rng.binomial(X,keep[:,None]).astype(np.int32)
        cls,sub,excl,_=classify(a,X=Xt,rule="R1")
        s=summarize(a,cls,sub,X=Xt); s["excluded_frac"]=frac(excl.sum(),len(cls)); s["thin_factor"]=float(keep[0])
        out[name]["POSTHOC_thin"]=s
    for name in out:
        for k in("_cls1","_sub1","_X"): out[name].pop(k,None)
    json.dump(out,open(f"{OUT}/verify_results.json","w"),indent=1,default=lambda o:o.item() if hasattr(o,"item") else str(o))
    import pickle
    pickle.dump(LAB,open(f"{SD}/labels_verifier.pkl","wb"))
    print("done")
main()

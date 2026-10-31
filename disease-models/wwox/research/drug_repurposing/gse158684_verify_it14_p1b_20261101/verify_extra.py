#!/usr/bin/env python3
"""Verifier p1b: duplicates, pseudobulk, Wwox ambient, Fisher. Usage: verify_extra.py <npz dir> <outdir>. --help safe."""
import sys, json, numpy as np, math
from collections import Counter
if len(sys.argv)<3 or sys.argv[1] in("-h","--help"): print(__doc__); sys.exit(0)
SD,OUT=sys.argv[1],sys.argv[2]
sys.argv=[sys.argv[0],"--help"]  # not used further
import importlib.util
def fisher(a,b,c,d):
    # two-sided exact p via hypergeometric
    n=a+b+c+d; r1=a+b; c1=a+c
    def pm(x): return math.exp(math.lgamma(r1+1)+math.lgamma(n-r1+1)+math.lgamma(c1+1)+math.lgamma(n-c1+1)-math.lgamma(n+1)-math.lgamma(x+1)-math.lgamma(r1-x+1)-math.lgamma(c1-x+1)-math.lgamma(n-r1-c1+x+1))
    lo=max(0,r1+c1-n);hi=min(r1,c1);p0=pm(a)
    return min(1.0,sum(pm(x) for x in range(lo,hi+1) if pm(x)<=p0*(1+1e-9)))
DEC=["Pvalb","Sst","Vip","Htr3a","Lhx6","Kcnc1","Syt2","Kcna1","Gad1","Gad2","Slc32a1","Slc17a7","Slc17a6","Camk2a","Satb2","Neurod6","Cux2","Snap25","Syt1","Rbfox3","Stmn2","Rbfox1",
     "Mog","Mobp","Mag","Cldn11","Opalin","St18","Mbp","Plp1","Pdgfra","Cspg4","Vcan","Ptprz1","Aqp4","Slc1a2","Slc1a3","Aldh1l1","Gja1","Gfap","Csf1r","Cx3cr1","P2ry12","Tmem119","Inpp5d","Dock8",
     "Nnat","Sox11","Dcx","Sox4","Tubb3","Igfbpl1","Wwox"]
D={}
for arm in("ctrl","ko"):
    z=np.load(f"{SD}/{arm}.npz"); X=z["X"].astype(np.int64); sym=z["sym"]; ids=z["ids"]
    idx={}
    for i,g in enumerate(sym): idx.setdefault(g,[]).append(i)
    dups={g:v for g,v in idx.items() if len(v)>1}
    r={"n_dup_symbols":len(dups),"dups":{}}
    for g,v in dups.items():
        r["dups"][g]=dict(ids=[str(ids[i]) for i in v],umi=[int(X[:,i].sum()) for i in v],decisive=(g in DEC))
    r["decisive_dups"]=[g for g in dups if g in DEC]
    r["decisive_genes_absent"]=[g for g in DEC if g not in idx]
    r["decisive_idinfo"]={g:[str(ids[i]) for i in idx[g]] for g in DEC if g in idx and len(idx[g])>1}
    # id-level check: for decisive genes, do first-occurrence ids look like canonical? n total
    # pseudobulk per 10k UMI
    tot=X.sum()
    def pb(genes): return float(sum(X[:,idx[g][0]].sum() for g in genes if g in idx)/tot*1e4)
    r["pseudobulk_per10k"]={g:pb([g]) for g in ["Pvalb","Sst","Vip","Lhx6","Wwox","Mbp","Plp1","Pdgfra","Cspg4","Gad1","Gad2","Snap25","Slc17a7","Aqp4","Csf1r","Nnat","Dcx","Sox11"]}
    r["pseudobulk_per10k"]["OLG_panel_noMbpPlp1"]=pb(["Mog","Mobp","Mag","Cldn11","Opalin","St18"])
    r["pseudobulk_per10k"]["OPC_panel"]=pb(["Pdgfra","Cspg4","Vcan","Ptprz1"])
    r["pseudobulk_per10k"]["newOL_post_hoc"]=pb(["Enpp6","Bmp4","Tcf7l2","Itpr2","Fyn","Tmem2"])
    r["pseudobulk_per10k"]["matureOL_post_hoc"]=pb(["Mog","Mobp","Mag","Opalin","Klk6","Apod","Ctps"])
    # duplicate-sensitivity: Wwox & decisive genes under first/sum/max/last
    for mode in ("first","sum","last","max","lowid"):
        def get(g):
            ii=idx.get(g)
            if ii is None: return np.zeros(X.shape[0],int)
            if len(ii)==1 or mode=="first": return X[:,ii[0]]
            if mode=="sum": return X[:,ii].sum(1)
            if mode=="last": return X[:,ii[-1]]
            if mode=="max": return X[:,ii[int(np.argmax([X[:,i].sum() for i in ii]))]]
            if mode=="lowid": return X[:,min(ii,key=lambda i:ids[i])]
        r[f"sens_{mode}"]={g:int(get(g).sum()) for g in DEC if g in dups}
    D[arm]=r
# do decisive genes with duplicates include any? print
for arm in D: print(arm,D[arm]["n_dup_symbols"],"decisive dup:",D[arm]["decisive_dups"],"absent:",D[arm]["decisive_genes_absent"])
for arm in D: print(arm,"all dup symbols:",{g:(v["ids"],v["umi"]) for g,v in D[arm]["dups"].items()})
for arm in D: print(arm,"pb",{k:round(v,3) for k,v in D[arm]["pseudobulk_per10k"].items()})
json.dump(D,open(f"{OUT}/verify_extra.json","w"),indent=1)

#!/usr/bin/env python3
"""POST-HOC checks by verifier p1b (labelled post hoc): pan-neuronal-only nuclei, OLG within-class marker levels. Usage: verify_post_hoc.py <scratch dir>. --help safe."""
import sys, pickle, numpy as np
if len(sys.argv)<2 or sys.argv[1] in("-h","--help"): print(__doc__); sys.exit(0)
SD=sys.argv[1]; LAB=pickle.load(open(f"{SD}/labels_verifier.pkl","rb"))
for arm in("ctrl","ko"):
    z=np.load(f"{SD}/{arm}.npz"); X=z["X"].astype(int); sym=list(z["sym"]); g=lambda n:X[:,sym.index(n)]
    gen=sum((g(n)>=1).astype(int) for n in["Snap25","Syt1","Rbfox3","Stmn2","Rbfox1"])
    exc=sum((g(n)>=1).astype(int) for n in["Slc17a7","Slc17a6","Camk2a","Satb2","Neurod6","Cux2"])
    inh=sum((g(n)>=1).astype(int) for n in["Gad1","Gad2","Slc32a1"])
    cls,sub=LAB[(arm,"R1")]
    pan_only=(gen>=2)&(exc<2)&(inh<2)&np.isin(cls,["unassigned"])
    print(arm,"POSTHOC pan-neuronal(>=2 genes) w/o exc/inh call among R1-unassigned:",pan_only.sum(),"of",len(cls),round(pan_only.mean()*100,1),"% ; as % of (neurons + these):",round(pan_only.sum()/(pan_only.sum()+(cls=="neuron").sum())*100,1))
    o=cls=="oligodendrocyte"; N=X.sum(1)
    for n in["Mog","Mobp","Mag","Mbp","Plp1","Opalin","Cldn11"]:
        print("  OLG R1",n,"mean per 10k UMI",round(g(n)[o].sum()/N[o].sum()*1e4,1),"detected",round((g(n)[o]>=1).mean(),2))
    print("  OLG n",o.sum(),"median UMI",np.median(N[o]),"median genes",np.median((X[o]>0).sum(1)))

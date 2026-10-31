#!/usr/bin/env python3
"""Cell-by-cell comparison with producer labels (run only after own numbers were fixed). Usage: verify_compare.py <scratch dir> <producer results dir>. --help safe."""
import sys, pickle, numpy as np, csv
from collections import Counter
if len(sys.argv)<3 or sys.argv[1] in("-h","--help"): print(__doc__); sys.exit(0)
SD,PR=sys.argv[1],sys.argv[2]
LAB=pickle.load(open(f"{SD}/labels_verifier.pkl","rb"))
for arm in("ctrl","ko"):
    z=np.load(f"{SD}/{arm}.npz"); X=z["X"].astype(int); sym=list(z["sym"]); pv=X[:,sym.index("Pvalb")]; tot=X.sum(1)
    rows=list(csv.DictReader(open(f"{PR}/labels_{arm}.tsv"),delimiter="\t"))
    assert len(rows)==X.shape[0]
    idx=np.array([int(r["index"]) for r in rows]); assert (idx==np.arange(len(rows))).all()
    pc=np.array([r["class"] for r in rows]); psub=np.array([r["subclass"] for r in rows])
    ptot=np.array([int(r["total_UMI"]) for r in rows]); ppv=np.array([int(r["Pvalb_UMI"]) for r in rows]); pvb=np.array([int(r["PV_B"]) for r in rows])
    print(arm,"total_UMI identical:",(ptot==tot).all(),"Pvalb UMI identical:",(ppv==pv).all(),"sum Pvalb",pv.sum(),"PV_B flagged",pvb.sum())
    for rule in("R0","R1"):
        mc,ms=LAB[(arm,rule)]
        m={"neuron":None}
        ct=Counter(zip(pc,mc))
        print(" crosstab producer(rows) x mine",rule)
        P=sorted(set(pc));M=sorted(set(mc))
        print("   "+"\t".join(["prod\\mine"]+M))
        for p in P: print("   "+"\t".join([p]+[str(ct[(p,m_)]) for m_ in M]))
    # agreement on inhibitory
    mc,ms=LAB[(arm,"R0")]
    pin=(pc=="inhibitory"); min_=(mc=="neuron")&(ms=="inh")
    print(" inhibitory: producer",pin.sum(),"mine R0",min_.sum(),"both",(pin&min_).sum(),"only producer",(pin&~min_).sum(),"only mine",(~pin&min_).sum())
    print("  Pvalb>=1 in producer-inh",(pin&(pv>=1)).sum(),"in my R0 inh",(min_&(pv>=1)).sum(),"in union",((pin|min_)&(pv>=1)).sum())
    print("  producer doublets with Pvalb>=1:",((pc=="doublet")&(pv>=1)).sum()," what are my R0 classes of Pvalb>=1 nuclei:",Counter(mc[pv>=1]))
    # producer oligo vs mine
    po=(pc=="oligo"); mo=(mc=="oligodendrocyte")
    print("  OLG producer",po.sum(),"mine R0",mo.sum(),"both",(po&mo).sum())
    # producer doublet vs Mbp/Plp1
    mp=X[:,sym.index("Mbp")]+X[:,sym.index("Plp1")]
    print("  producer doublets: median Mbp+Plp1",np.median(mp[pc=="doublet"]),"nondoublet neurons",np.median(mp[np.isin(pc,["excitatory","inhibitory"])]))

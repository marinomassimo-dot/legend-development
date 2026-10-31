#!/usr/bin/env python3
"""Loader for GSE158684 10x filtered matrices (verifier p1b). numpy only. --help is safe."""
import gzip, sys, numpy as np
D = "/home/desktop/legend-development/files/geo/GSE158684/"
def load(arm):
    feats = [l.rstrip("\n").split("\t") for l in gzip.open(D+f"GSE158684_{arm}_filtered_features.tsv.gz","rt")]
    bcs = [l.strip() for l in gzip.open(D+f"GSE158684_{arm}_filtered_barcodes.tsv.gz","rt")]
    with gzip.open(D+f"GSE158684_{arm}_filtered_matrix.mtx.gz","rt") as f:
        for l in f:
            if not l.startswith("%"): break
        ng,nc,nnz = map(int,l.split())
        a = np.loadtxt(f, dtype=np.int64)
    assert a.shape[0]==nnz and ng==len(feats) and nc==len(bcs)
    X = np.zeros((nc,ng),dtype=np.uint16)
    X[a[:,1]-1,a[:,0]-1] = a[:,2]
    return feats,bcs,X
if __name__=="__main__":
    if len(sys.argv)>1 and sys.argv[1] in("-h","--help"):
        print(__doc__); sys.exit(0)
    import os
    out = sys.argv[1]
    for arm in("ctrl","ko"):
        f,b,X = load(arm)
        np.savez(os.path.join(out,f"{arm}.npz"),X=X,ids=np.array([x[0] for x in f]),sym=np.array([x[1] for x in f]),bc=np.array(b))
        print(arm,X.shape,int(X.sum()))

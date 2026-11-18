#!/usr/bin/env python3
"""ADV-052 (a): Cacna1g/h/i (and Wwox, Gad1, Slc17a7 as controls) by nucleus class in the held GSE158684 matrices (Synapsin-Cre Wwox deletion, hippocampus, one pool per genotype).
Class calls are the verifier's rule R1 (gse158684_verify_it14_p1b_20261101/verify_analysis.py: marker panels, two panel genes detected, one class only), reimplemented here unchanged.
Output: per arm and class, nuclei, nuclei with at least one UMI, UMI per 1e4 UMI of the pooled class. No statistic across libraries: one library per genotype (no replicate). --help is safe."""
import sys, gzip, numpy as np
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); sys.exit(0)
D = "/home/desktop/legend-development/files/geo/GSE158684/"
P = dict(gen=["Snap25", "Syt1", "Rbfox3", "Stmn2", "Rbfox1"], exc=["Slc17a7", "Slc17a6", "Camk2a", "Satb2", "Neurod6", "Cux2"], inh=["Gad1", "Gad2", "Slc32a1"],
         olg=["Mog", "Mobp", "Mag", "Cldn11", "Opalin", "St18"], opc=["Pdgfra", "Cspg4", "Vcan", "Ptprz1"], ast=["Aqp4", "Slc1a2", "Slc1a3", "Aldh1l1", "Gja1", "Gfap"],
         mic=["Csf1r", "Cx3cr1", "P2ry12", "Tmem119", "Inpp5d", "Dock8"])
GENES = ["Cacna1g", "Cacna1h", "Cacna1i", "Wwox", "Gad1", "Slc17a7"]

def load(arm):
    feats = [l.rstrip("\n").split("\t") for l in gzip.open(D + f"GSE158684_{arm}_filtered_features.tsv.gz", "rt")]
    with gzip.open(D + f"GSE158684_{arm}_filtered_matrix.mtx.gz", "rt") as f:
        for l in f:
            if not l.startswith("%"): break
        ng, nc, nnz = map(int, l.split())
        a = np.loadtxt(f, dtype=np.int64)
    X = np.zeros((nc, ng), dtype=np.int32); X[a[:, 1] - 1, a[:, 0] - 1] = a[:, 2]
    return [x[1] for x in feats], X

def run(arm):
    sym, X = load(arm); idx = {}
    for i, g in enumerate(sym): idx.setdefault(g, i)
    col = lambda g: X[:, idx[g]] if g in idx else np.zeros(X.shape[0], int)
    ndet = lambda gs: sum((col(g) >= 1).astype(int) for g in gs)
    gen = ndet(P["gen"]); exc = ndet(P["exc"]) >= 2; inh = ndet(P["inh"]) >= 2
    neu = (exc | inh) & (gen >= 1)
    comp = np.vstack([neu, ndet(P["olg"]) >= 2, ndet(P["opc"]) >= 2, ndet(P["ast"]) >= 2, ndet(P["mic"]) >= 2]).T
    names = ["neuron", "oligodendrocyte", "OPC", "astrocyte", "microglia"]
    cls = np.array(["unassigned"] * X.shape[0], dtype=object)
    one = comp.sum(1) == 1; cls[one] = [names[i] for i in comp[one].argmax(1)]; cls[comp.sum(1) >= 2] = "ambiguous"
    sub = np.array([""] * X.shape[0], dtype=object)
    sub[(cls == "neuron") & inh] = "neuron_inh"; sub[(cls == "neuron") & ~inh] = "neuron_exc"
    out = []
    for label, mask in [("all nuclei", np.ones(len(cls), bool)), ("neuron", cls == "neuron"), ("neuron_exc", sub == "neuron_exc"), ("neuron_inh", sub == "neuron_inh"),
                        ("oligodendrocyte", cls == "oligodendrocyte"), ("OPC", cls == "OPC"), ("astrocyte", cls == "astrocyte"), ("microglia", cls == "microglia")]:
        n = int(mask.sum()); tot = int(X[mask].sum())
        for g in GENES:
            c = col(g)[mask]
            out.append((arm, label, g, n, int((c >= 1).sum()), int(c.sum()), round(1e4 * c.sum() / tot, 2) if tot else float("nan")))
    return out

rows = run("ctrl") + run("ko")
with open(sys.argv[1], "w") as f:
    f.write("arm\tclass\tgene\tnuclei\tnuclei_with_umi\tumi\tumi_per_1e4\n")
    for r in rows: f.write("\t".join(map(str, r)) + "\n")
for g in GENES[:4]:
    print(g)
    for label in ("all nuclei", "neuron_exc", "neuron_inh", "oligodendrocyte", "OPC", "astrocyte"):
        a = [r for r in rows if r[2] == g and r[1] == label]
        print("  %-16s ctrl n=%4d det=%4d umi=%4d per1e4=%6.2f | ko n=%4d det=%4d umi=%4d per1e4=%6.2f" % (label, a[0][3], a[0][4], a[0][5], a[0][6], a[1][3], a[1][4], a[1][5], a[1][6]))

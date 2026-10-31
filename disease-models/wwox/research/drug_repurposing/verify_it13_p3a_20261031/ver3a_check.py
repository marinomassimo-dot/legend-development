#!/usr/bin/env python3
"""Independent check of P3a: gene-level TPM contrasts. Usage: ver3a_check.py HIPPO.gz CORTEX.gz FASTA.gz"""
import sys, gzip, re, math, collections
if len(sys.argv) != 4 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); sys.exit(0)
hip, ctx, fa = sys.argv[1:]
t2g = {}
for l in gzip.open(fa, "rt"):
    if l[0] == ">":
        m = re.search(r"gene_symbol:(\S+)", l)
        if m: t2g[l[1:].split()[0]] = m.group(1)
def load(p):
    f = gzip.open(p, "rt"); h = f.readline().rstrip("\n").split("\t")
    cols = h[3:]; g = collections.defaultdict(lambda: [0.0]*len(cols)); miss = 0
    for l in f:
        x = l.rstrip("\n").split("\t"); s = t2g.get(x[0])
        if not s: miss += 1; continue
        v = g[s]
        for i, y in enumerate(x[3:]): v[i] += float(y)
    return cols, g
GENES = "Pvalb Npy Gad2 Slc32a1 Dlx1 Dlx2 Dlx5 Lhx6 Cacna1g Cacna1h Kcnj6 Slc12a2 Slc12a5 Wwox Gad1 Sst Slc17a7 Camk2a".split()
def lfc(g, cols, gene, ko, ct):
    v = g[gene]; k = [v[cols.index(c)] for c in ko]; c = [v[cols.index(c)] for c in ct]
    return math.log2((sum(k)/len(k)+.5)/(sum(c)/len(c)+.5)), k, c
H = ["S_KO_1","S_KO_2","S_KO_3"]; SC = ["S_Ctrl_1","S_Ctrl_2"]; NK = ["N_KO_1","N_KO_2"]; NC = ["N_Ctrl_1","N_Ctrl_2"]
KO = ["KO_1","KO_2"]; WT = ["WT_1","WT_2","WT_3"]
contr = [("H_S",H,SC,"h"),("H_N",NK,NC,"h"),("H_null",KO,WT,"h"),("C_S",["CRTX_S_KO_1","CRTX_S_KO_2","CRTX_S_KO_3"],["CRTX_S_Ctrl_%d"%i for i in range(1,5)],"c"),
 ("bg_SC_v_WT",SC,WT,"h"),("bg_NC_v_WT",NC,WT,"h"),("bg_SC_v_NC",SC,NC,"h")]
D = {"h": load(hip), "c": load(ctx)}
print("gene\t"+"\t".join(c[0] for c in contr))
res = {}
for gn in GENES:
    row = []
    for n, a, b, t in contr:
        cols, g = D[t]; row.append(lfc(g, cols, gn, a, b)[0]); res[(gn,n)] = row[-1]
    print(gn+"\t"+"\t".join("%.2f"%r for r in row))
print("\nPAN panel mean (Gad2,Slc32a1,Dlx1,Dlx2,Dlx5,Lhx6) log2")
P = "Gad2 Slc32a1 Dlx1 Dlx2 Dlx5 Lhx6".split()
print("panel\t"+"\t".join("%.2f"%(sum(res[(g,n)] for g in P)/len(P)) for n,*_ in contr))
print("\nmean TPM per animal")
for gn in ["Pvalb","Npy","Slc12a2","Slc12a5","Cacna1g","Cacna1h","Kcnj6","Wwox"]:
    for t in "hc":
        cols, g = D[t]; print(gn, t, " ".join("%s=%.1f"%(c,v) for c,v in zip(cols,g[gn])))

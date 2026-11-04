"""IT27 verifier P1b extra: which genes carry the TPM mass shift (compositional check). Usage: python3 -I v_p1b_composition_check.py <hippo_TPM.gz> <cdna.fa.gz> <outfile>"""
import sys, gzip, re, numpy as np
hip, fa, out = sys.argv[1:4]
t2g, g2s = {}, {}
with gzip.open(fa, "rt") as f:
    for l in f:
        if l[0] == ">":
            t = l[1:].split()[0].split(".")[0]; m = re.search(r"gene:(ENSMUSG\d+)", l); s = re.search(r"gene_symbol:(\S+)", l)
            if m: t2g[t] = m.group(1)
            if m and s: g2s[m.group(1)] = s.group(1)
with gzip.open(hip, "rt") as f:
    h = f.readline().rstrip("\n").split("\t")[3:]; rows = [l.rstrip("\n").split("\t") for l in f]
G = {}
for r in rows:
    g = t2g.get(r[0].split(".")[0]);
    if g: G.setdefault(g, np.zeros(len(h))); G[g] += np.array(r[3:], float)
ids = sorted(G); M = np.array([G[g] for g in ids]); ix = {n: i for i, n in enumerate(h)}
arms = {"S_Ctrl": ["S_Ctrl_1", "S_Ctrl_2"], "S_KO": ["S_KO_1", "S_KO_2", "S_KO_3"], "WT": ["WT_1", "WT_2", "WT_3"], "null": ["KO_1", "KO_2"]}
A = {k: M[:, [ix[n] for n in v]].mean(1) for k, v in arms.items()}
with open(out, "w") as o:
    for a, b in [("S_Ctrl", "S_KO"), ("WT", "null")]:
        d = A[b] - A[a]; top = np.argsort(d)[::-1][:8]; bot = np.argsort(d)[:8]
        o.write(f"# {b} minus {a} mean TPM change; total absolute up = {d[d>0].sum():.0f}, down = {d[d<0].sum():.0f}\n")
        o.write("top gains: " + "; ".join(f"{g2s.get(ids[i],ids[i])} {A[a][i]:.0f}->{A[b][i]:.0f}" for i in top) + "\n")
        o.write("top losses: " + "; ".join(f"{g2s.get(ids[i],ids[i])} {A[a][i]:.0f}->{A[b][i]:.0f}" for i in bot) + "\n")
        top1k = np.argsort(A[a])[::-1][:20]
        o.write("share of TPM in top-20 genes of the reference arm: ref %.3f, pert %.3f\n" % (A[a][top1k].sum()/1e6, A[b][top1k].sum()/1e6))
print(open(out).read())

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "pylib"))
import csv, gzip, json, math, random, statistics, time
import numpy as np, h5py
D = "/home/desktop/legend-development/files/geo/GSE92742/"
G = "/home/desktop/legend-development/.claude/worktrees/it3-verify-lincs/disease-models/wwox/research/drug_repurposing/gse156243/"
def tab(fn): return list(csv.DictReader(gzip.open(D + fn, "rt"), delimiter="\t"))
si = tab("GSE92742_Broad_LINCS_sig_info.txt.gz"); gi_ = tab("GSE92742_Broad_LINCS_gene_info.txt.gz")
from collections import Counter
print("pert_type counts", Counter(r["pert_type"] for r in si).most_common(12))
print("n sig_info", len(si))
info = {r["sig_id"]: r for r in si}
f = h5py.File(D + "GSE92742_Broad_LINCS_Level5_COMPZ.MODZ_n473647x12328.gctx", "r")
m = f["0/DATA/0/matrix"]; col = [x.decode() for x in f["0/META/COL/id"][:]]; row = [x.decode() for x in f["0/META/ROW/id"][:]]
print("matrix", m.shape, "sig_ids in sig_info:", sum(c in info for c in col))
ptype = np.array([info[c]["pert_type"] for c in col]); cell = np.array([info[c]["cell_id"] for c in col]); iname = np.array([info[c]["pert_iname"] for c in col])
ptime = np.array([info[c]["pert_time"] for c in col])
cp = np.where(ptype == "trt_cp")[0]; cgs = np.where(ptype == "trt_sh.cgs")[0]
print("trt_cp in matrix", len(cp), "trt_sh.cgs", len(cgs), "trt_cp in sig_info (any)", sum(r["pert_type"]=="trt_cp" for r in si))
ww = [i for i in cgs if iname[i] == "WWOX"]; print("WWOX cgs", [col[i] for i in ww])
print("WWOX any pert_type in sig_info:", Counter((r["pert_type"], r["cell_id"]) for r in si if r["pert_iname"] == "WWOX"))
sym2id = {r["pr_gene_symbol"]: r["pr_gene_id"] for r in gi_}
gcol = {e: k for k, e in enumerate(row)}
q = {**json.load(open(G + "derived/query_sets.json")), **json.load(open(G + "derived/query_sets_it2_nulls.json"))}
def cols(sy): return [gcol[sym2id[s]] for s in sy if s in sym2id and sym2id[s] in gcol]
SETS = {k: (cols(q[k]["up"]), cols(q[k]["down"])) for k in ("S1", "K2")}
print({k: (len(v[0]), len(v[1])) for k, v in SETS.items()})
# expression deciles (own implementation)
cnt = {}
with gzip.open("/home/desktop/legend-development/files/geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz", "rt") as fh:
    fh.readline()
    for l in fh:
        x = l.rstrip("\n").split("\t"); cnt[x[0]] = np.array([float(v) for v in x[1:]])
lib = np.array([sum(v[i] for v in cnt.values()) for i in range(6)])
meanl = {g: float(np.mean(np.log2(v / lib * 1e6 + 1))) for g, v in cnt.items()}
sym_of = {gcol[e]: s for s, e in sym2id.items() if e in gcol}
ps = [s for s in sym_of.values() if s in meanl]; order = sorted(ps, key=lambda s: meanl[s]); dec = {s: min(9, i * 10 // len(order)) for i, s in enumerate(order)}
s1u, s1d = SETS["S1"]; s1all = set(s1u) | set(s1d); pool = {}
for c in sorted(sym_of):
    s = sym_of[c]
    if s in dec and c not in s1all: pool.setdefault(dec[s], []).append(c)
rnd = random.Random(777)  # own seed, not the producer's
NR = 1000
def matched():
    used, out = set(), []
    for arm in (s1u, s1d):
        a = []
        for c in arm:
            cand = [x for x in pool[dec.get(sym_of.get(c), 0)] if x not in used]; x = rnd.choice(cand); used.add(x); a.append(x)
        out.append(a)
    return out
MS = [matched() for _ in range(NR)]
ALL = [SETS["S1"], SETS["K2"]] + MS
W = np.zeros((len(row), len(ALL)), dtype="float32")
for j, (u, d) in enumerate(ALL): W[u, j] += 1 / len(u); W[d, j] -= 1 / len(d)
# CGS rows of three lines
want_cgs = set(int(i) for i in cgs)
want = np.sort(np.array(sorted(set(cp) | want_cgs)))
iscp = np.zeros(len(col), bool); iscp[cp] = True
rev = {"S1": 0, "K2": 0}; mim = {"S1": 0, "K2": 0}; ntot = 0
cgs_res = {}  # i -> (raw S1, zM S1)
t0 = time.time(); B = 4000
for a in range(0, len(col), B):
    sel = want[(want >= a) & (want < a + B)]
    if len(sel) == 0: continue
    blk = m[a:a + B, :][sel - a]
    S = blk @ W
    mu = S[:, 2:].mean(1); sd = S[:, 2:].std(1) + 1e-9
    zk2 = (S[:, 1] - mu) / sd
    for k, j in (("S1", 0), ("K2", 1)):
        z = (S[:, j] - mu) / sd
        if k=="K2": zk2=z
        c_ = iscp[sel]
        rev[k] += int((z[c_] <= -3).sum()); mim[k] += int((z[c_] >= 3).sum())
        if k == "S1":
            for t, i in enumerate(sel):
                if i in want_cgs: cgs_res[int(i)] = (float(S[t, 0]), float(z[t]), float(zk2[t]))
    ntot += int(iscp[sel].sum())
    if (a // B) % 20 == 0: print("block", a, round(time.time() - t0), flush=True)
print("compound signatures scored", ntot, "hits", rev, mim)
out = {"rev": rev, "mim": mim, "ntot": ntot}
rows = []
for i in ww:
    rows.append((col[i], cell[i], ptime[i], cgs_res[int(i)]))
res = {}
for i in ww:
    c = cell[i]
    if c not in ("HCC515", "MCF7", "PC3"):
        res[col[i]] = {"raw": round(cgs_res[int(i)][0], 3), "zM": round(cgs_res[int(i)][1], 2)}; continue
    pool_i = [j for j in cgs if cell[j] == c]
    zs = np.array([cgs_res[int(j)][1] for j in pool_i])
    pc = float((zs < cgs_res[int(i)][1]).mean())
    res[col[i]] = {"raw": round(cgs_res[int(i)][0], 3), "zM": round(cgs_res[int(i)][1], 2), "pct_same_line": round(pc, 3), "n_line": len(pool_i)} if c in ("HCC515", "MCF7", "PC3") else {"raw": round(cgs_res[int(i)][0], 3), "zM": round(cgs_res[int(i)][1], 2)}
out["wwox"] = res
z1=np.array([cgs_res[int(j)][1] for j in cgs]); z2=np.array([cgs_res[int(j)][2] for j in cgs])
out["bg"]={"S1_ge2":float((z1>=2).mean()),"S1_ge3":float((z1>=3).mean()),"K2_ge2":float((z2>=2).mean()),"K2_ge3":float((z2>=3).mean())}
json.dump(out, open("verify_out2.json", "w"), indent=1); print(json.dumps(out, indent=1))

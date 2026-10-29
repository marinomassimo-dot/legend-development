#!/usr/bin/env python3
"""IT7 P3 (scientist-a): bounded comparison of a reference overlap, a signed-network propagation and the six-gene signature route.
Pre-registered in PRE_REGISTRATION.md (committed before any evaluation value was opened). EXPLORATORY; not medical advice.

Usage:
  p3_run.py e2 --geo DIR --cache DIR [--out DIR]     compound-level comparison (needs numpy; reads LINCS level 5 extract read-only)
  p3_run.py e1 --counts FILE [--out DIR]            module transfer in GSE215425 (animals as unit)
  p3_run.py --help                                   this text; no work is done

  --geo    dir holding GSE92742_Broad_LINCS_{sig_info,gene_info}.txt.gz
  --cache  dir holding extract.npy, extract_rows.tsv, extract_genes.json (IT3 extract of GSE92742 level 5, float32, memory-mapped)
  Environment P3_SYNTH=1 replaces every z-score by seeded noise (development of the code without opening any outcome).
Deterministic: master seed 20261029; sub-seeds are master + k as declared in PRE_REGISTRATION.md. Stdlib + numpy only."""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help") or sys.argv[1] not in ("e1", "e2"):
    print(__doc__); raise SystemExit(0)
import csv, gzip, json, os, math, time, collections, hashlib
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
INP = os.path.join(HERE, "inputs")
SEED = 20261029
UP5 = ["SLC2A1", "HK2", "LDHA", "LDHB", "BNIP3"]; DOWN1 = "PDK1"; SIX = UP5 + [DOWN1]
BCELLS = {"NPC", "NPC.CAS9", "NPC.TAK"}; ECELLS = {"NEU", "NEU.KCL", "MNEU.E"}
EXCL_PREFIX = ("SLC2A", "HK", "LDH", "PDK", "PFK", "PGK", "ENO", "ALDO", "PKM", "PGAM", "TPI", "GAPDH", "PDH")
K, GAMMA = 3, 0.5

def arg(name, default=None):
    a = sys.argv
    return a[a.index(name) + 1] if name in a else default
def log(*a): print(time.strftime("%H:%M:%S"), *a, flush=True)
def tsv(path):
    op = gzip.open if path.endswith(".gz") else open
    return list(csv.DictReader(op(path, "rt"), delimiter="\t"))

def rankdata(a):
    u, inv, cnt = np.unique(a, return_inverse=True, return_counts=True)
    avg = np.cumsum(cnt) - (cnt - 1) / 2.0
    return avg[inv]
def pearson(x, y):
    x = x - x.mean(); y = y - y.mean(); d = math.sqrt((x * x).sum() * (y * y).sum())
    return float((x * y).sum() / d) if d > 0 else 0.0
def spearman(a, b): return pearson(rankdata(np.asarray(a, float)), rankdata(np.asarray(b, float)))
def rho_cols(score, M):
    """Spearman of one vector against every column of M (columns ranked with ties averaged)."""
    rs = rankdata(np.asarray(score, float)); rs = rs - rs.mean()
    R = np.column_stack([rankdata(M[:, j]) for j in range(M.shape[1])]); R = R - R.mean(0)
    d = np.sqrt((rs * rs).sum() * (R * R).sum(0))
    return np.where(d > 0, (rs[:, None] * R).sum(0) / np.where(d > 0, d, 1), 0.0)
def pct(x, q): return float(np.percentile(x, q))

# ============================================================================================ E2
def run_e2():
    geo, cache = arg("--geo"), arg("--cache")
    out = arg("--out", os.path.join(HERE, "results")); os.makedirs(out, exist_ok=True)
    synth = os.environ.get("P3_SYNTH") == "1"
    t0 = time.time()
    # ---- universe -------------------------------------------------------------------------
    sub = tsv(f"{INP}/pilot_subset.tsv")
    fam578 = [r["family_id"] for r in sub if r["usable_by_both_Mnet_and_Msig_neural"] == "yes"]
    cards = {r["family_id"]: r["card_ids"] for r in sub}; names = {r["family_id"]: r["name"] for r in sub}
    assert len(fam578) == 578, len(fam578)
    fam_perts = collections.defaultdict(set)
    for r in tsv(f"{INP}/pilot_lincs_contexts.tsv"):
        if r["family_id"] in set(fam578): fam_perts[r["family_id"]].add(r["pert_id"])
    pert2fam = collections.defaultdict(set)
    for f, ps in fam_perts.items():
        for p in ps: pert2fam[p].add(f)
    rowidx = {}
    for k, r in enumerate(tsv(f"{cache}/extract_rows.tsv")): rowidx[r["sig_id"]] = int(r["row"])
    sigs = []
    for r in tsv(f"{geo}/GSE92742_Broad_LINCS_sig_info.txt.gz"):
        if r["pert_type"] != "trt_cp" or r["pert_id"] not in pert2fam or r["sig_id"] not in rowidx: continue
        cls = "B" if r["cell_id"] in BCELLS else "E" if r["cell_id"] in ECELLS else None
        if cls: sigs.append(dict(sig_id=r["sig_id"], pert_id=r["pert_id"], cell=r["cell_id"], dose=r["pert_idose"], time=r["pert_itime"], cls=cls, row=rowidx[r["sig_id"]]))
    sigs.sort(key=lambda s: s["row"])
    famB = collections.defaultdict(list); famE = collections.defaultdict(list)
    for i, s in enumerate(sigs):
        for f in pert2fam[s["pert_id"]]: (famB if s["cls"] == "B" else famE)[f].append(i)
    U = sorted(f for f in fam578 if famB.get(f) and famE.get(f))
    log("signatures", len(sigs), "families with B", len(famB), "with E", len(famE), "|U|", len(U))
    # ---- z matrix -------------------------------------------------------------------------
    genes_entrez = json.load(open(f"{cache}/extract_genes.json"))["entrez_columns"]
    gi = {r["pr_gene_symbol"]: r["pr_gene_id"] for r in tsv(f"{geo}/GSE92742_Broad_LINCS_gene_info.txt.gz")}
    col_of = {g: i for i, g in enumerate(genes_entrez)}
    sym_col = {s: col_of[e] for s, e in gi.items() if e in col_of}
    col_sym = {c: s for s, c in sym_col.items()}
    G = len(genes_entrez)
    if synth:
        rng0 = np.random.default_rng(SEED); Z = rng0.standard_normal((len(sigs), G)).astype(np.float32)
    else:
        arr = np.load(f"{cache}/extract.npy", mmap_mode="r")
        Z = np.asarray(arr[[s["row"] for s in sigs], :], dtype=np.float32)
    mad = np.median(np.abs(Z - np.median(Z, axis=1, keepdims=True)), axis=1)
    scale = (1.4826 * mad).astype(np.float32); Zn = Z / scale[:, None]
    up_c = [sym_col[g] for g in UP5]; dn_c = sym_col[DOWN1]
    def os_real(up=up_c, dn=dn_c, arms="six"):
        v = -Zn[:, up].mean(1)
        return v + Zn[:, dn] if arms == "six" else v
    OS = os_real(); OS_up5 = os_real(arms="up5")
    def fam_med(vec, fams, table): return np.array([np.median(vec[table[f]]) for f in fams])
    OB, OE = fam_med(OS, U, famB), fam_med(OS, U, famE)
    nU = len(U)
    # ---- random readouts (C1) --------------------------------------------------------------
    sd = Z.std(0); dec = np.digitize(sd, np.quantile(sd, np.linspace(0.1, 0.9, 9)))
    excl = {c for c, s in col_sym.items() if s.startswith(EXCL_PREFIX)} | set(up_c) | {dn_c}
    rng = np.random.default_rng(SEED + 11)
    NR = 1000
    cand = {d: np.array([c for c in range(G) if dec[c] == d and c not in excl]) for d in range(10)}
    real_cols = up_c + [dn_c]
    RS = np.zeros((NR, 6), int)
    for k in range(NR):
        used = set()
        for j, rc in enumerate(real_cols):
            while True:
                c = int(rng.choice(cand[dec[rc]]))
                if c not in used: used.add(c); break
            RS[k, j] = c
    Rup, Rdn = RS[:, :5], RS[:, 5]
    def os_matrix(Zrows, scaled=True):
        # (n_sig, NR) opposition of each random readout
        A = np.empty((Zrows.shape[0], NR), np.float32)
        for k in range(NR): A[:, k] = -Zrows[:, Rup[k]].mean(1) + Zrows[:, Rdn[k]]
        return A
    OSr = os_matrix(Zn)
    def fam_med_mat(M, fams, table): return np.vstack([np.median(M[table[f]], axis=0) for f in fams])
    OBr, OEr = fam_med_mat(OSr, U, famB), fam_med_mat(OSr, U, famE)
    log("outcomes and random readouts done", round(time.time() - t0), "s")
    # ---- network ---------------------------------------------------------------------------
    def read_edges(files):
        E = {}
        for fn in files:
            for r in tsv(f"{INP}/{fn}"):
                srcs = r["source_symbol"].split("_") if "_" in r["source_symbol"] else [r["source_symbol"]]
                tgts = r["target_symbol"].split("_") if "_" in r["target_symbol"] else [r["target_symbol"]]
                for s in srcs:
                    for t in tgts:
                        if s == t: continue
                        sg = int(r["sign"]); k = (s, t)
                        E[k] = sg if (k not in E or E[k] == sg) else 0
        return [(s, t, sg) for (s, t), sg in E.items() if sg != 0]
    ext = read_edges(["signor_omnipath_edges.tsv.gz", "collectri_omnipath_edges.tsv.gz"])
    nodes_p1 = {r["node_id"]: r["symbol"] for r in tsv(f"{INP}/nodes.tsv")}
    wwox_add = []
    for r in tsv(f"{INP}/edges.tsv"):
        # P1 repaired commit 31446616: the four HIF1A -> gene inferred edges (ED077-ED080); selected by content, not by id
        if r["edge_type"] == "inferred" and r["source_node"].startswith("HGNC:") and r["target_node"].startswith("HGNC:") and r["sign"] in ("up", "down"):
            wwox_add.append((nodes_p1[r["source_node"]], nodes_p1[r["target_node"]], 1 if r["sign"] == "up" else -1))
    log("edges ext", len(ext), "wwox additions", wwox_add)
    class Graph:
        def __init__(s, edges):
            syms = sorted({e[0] for e in edges} | {e[1] for e in edges}); s.idx = {g: i for i, g in enumerate(syms)}; s.syms = syms; s.N = len(syms)
            src = np.array([s.idx[e[0]] for e in edges]); tgt = np.array([s.idx[e[1]] for e in edges]); sg = np.array([e[2] for e in edges], np.float32)
            od = np.bincount(src, minlength=s.N).astype(np.float32); w = sg / od[src]
            o = np.argsort(tgt, kind="stable"); s.src, s.tgt, s.w = src[o], tgt[o], w[o]
            s.ut, s.starts = np.unique(s.tgt, return_index=True)
            s.edges = edges
        def hop(s, X):
            c = X[:, s.src] * s.w
            out = np.zeros_like(X); out[:, s.ut] = np.add.reduceat(c, s.starts, axis=1); return out
        def prop(s, X, direct=False):
            y = X.copy() if direct else np.zeros_like(X); h = X
            for k in range(1, K + 1):
                h = s.hop(h); y += (GAMMA ** (k - 1)) * h
            return y
        def in_nb(s):
            d = collections.defaultdict(set)
            for a, b in zip(s.src, s.tgt): d[int(b)].add(int(a))
            return d
    # ---- compound target vectors -----------------------------------------------------------
    sgn = {"down": -1.0, "up": 1.0}
    fam_t = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in tsv(f"{INP}/pilot_net_actions.tsv"):
        if r["family_id"] not in set(fam578) or r["sign"] not in sgn: continue
        for t in r["target_symbol"].split(";"): fam_t[r["family_id"]][t].append(sgn[r["sign"]])
    famT = {f: {t: float(np.mean(v)) for t, v in fam_t[f].items()} for f in fam578}
    tcount = collections.Counter(t for f in fam578 for t in famT[f]); N578 = len(fam578)
    idf = {t: math.log((N578 + 1) / (n + 1)) for t, n in tcount.items()}
    ntar = np.array([len(famT[f]) for f in U], float)
    def x0_matrix(g):
        X = np.zeros((nU, g.N), np.float32)
        for i, f in enumerate(U):
            v = famT[f]; nrm = math.sqrt(sum(a * a for a in v.values()))
            if nrm == 0: continue
            for t, a in v.items():
                if t in g.idx: X[i, g.idx[t]] = a / nrm
        return X
    def readout_idx(g, up_syms, dn_sym):
        return [g.idx.get(s, g.N) for s in up_syms], g.idx.get(dn_sym, g.N)
    def net_score(y, upi, dni):
        yp = np.concatenate([y, np.zeros((y.shape[0], 1), np.float32)], 1)
        return -yp[:, upi].mean(1) + yp[:, dni]
    gx = Graph(ext); X0 = x0_matrix(gx); Y = gx.prop(X0)
    upi, dni = readout_idx(gx, UP5, DOWN1)
    NET = net_score(Y, upi, dni)
    NET_direct = net_score(gx.prop(X0, direct=True), upi, dni)
    NET_up5 = -np.concatenate([Y, np.zeros((nU, 1), np.float32)], 1)[:, upi].mean(1)
    gw = Graph(ext + wwox_add); Yw = gw.prop(x0_matrix(gw)); NETW = net_score(Yw, *readout_idx(gw, UP5, DOWN1))
    log("graph nodes", gx.N, "readouts in graph", {s: s in gx.idx for s in SIX}, "families with a target in graph", int((np.abs(X0).sum(1) > 0).sum()), "of", nU)
    # ---- REF ---------------------------------------------------------------------------------
    nb = gx.in_nb()
    def reg_vec(syms):
        r = np.zeros(gx.N, np.float32)
        for s in syms:
            if s in gx.idx:
                for a in nb[gx.idx[s]]: r[a] = 1
        return r
    Tm = np.zeros((nU, gx.N), np.float32)
    for i, f in enumerate(U):
        for t in famT[f]:
            if t in gx.idx: Tm[i, gx.idx[t]] = idf[t] / math.sqrt(len(famT[f]))
    REF1 = Tm @ reg_vec(SIX)
    mod20 = {r["symbol"] for r in tsv(f"{INP}/nodes.tsv") if r["node_type"] == "gene" and r["module"] == "glycolysis_pdh_lactate"}
    REF0_all = sum(1 for f in fam578 if mod20 & set(famT[f])); REF0 = np.array([len(mod20 & set(famT[f])) for f in U], float)
    BASE = ntar
    # ---- headline correlations -----------------------------------------------------------------
    M = {"SIG": OB, "NET-EXT": NET, "NET-WWOX": NETW, "REF-1": REF1, "BASE-promisc": BASE, "REF-0": REF0}
    rho = {k: spearman(v, OE) for k, v in M.items()}
    log("rho", rho)
    # ---- C1 nulls, C2 nulls ---------------------------------------------------------------------
    C1 = {k: rho_cols(M[k], OEr) for k in ["NET-EXT", "NET-WWOX", "REF-1", "BASE-promisc"]}
    C1["SIG"] = np.array([spearman(OBr[:, k], OEr[:, k]) for k in range(NR)])
    # random inputs (C2): same random readouts as the query
    def rand_scores_net(y, g):
        yp = np.concatenate([y, np.zeros((nU, 1), np.float32)], 1)
        out = np.empty((nU, NR), np.float32)
        for k in range(NR):
            ui = [g.idx.get(col_sym[c], g.N) for c in Rup[k]]; di = g.idx.get(col_sym[Rdn[k]], g.N)
            out[:, k] = -yp[:, ui].mean(1) + yp[:, di]
        return out
    NETr = rand_scores_net(Y, gx)
    REFr = np.empty((nU, NR), np.float32)
    for k in range(NR): REFr[:, k] = Tm @ reg_vec([col_sym[c] for c in RS[k]])
    def rho_inputs(Sm):  # real outcome, random-input scores
        return np.array([spearman(Sm[:, k], OE) for k in range(NR)])
    C2 = {"NET-EXT": rho_inputs(NETr), "REF-1": rho_inputs(REFr)}
    # C2b (added after registration, labelled): inputs matched on in-degree in G_ext instead of SD decile
    indeg = np.array([len(nb[gx.idx[col_sym[c]]]) if col_sym[c] in gx.idx else 0 for c in range(G)])
    rng2 = np.random.default_rng(SEED + 12)
    candb = {}
    for rc in real_cols:
        d0 = math.log1p(indeg[rc]); candb[rc] = np.array([c for c in range(G) if c not in excl and abs(math.log1p(indeg[c]) - d0) <= 0.3])
    NETb = np.empty((nU, NR), np.float32); REFb = np.empty((nU, NR), np.float32)
    ypad = np.concatenate([Y, np.zeros((nU, 1), np.float32)], 1)
    for k in range(NR):
        used = set(); cs = []
        for rc in real_cols:
            while True:
                c = int(rng2.choice(candb[rc]))
                if c not in used: used.add(c); cs.append(c); break
        ui = [gx.idx.get(col_sym[c], gx.N) for c in cs[:5]]; di = gx.idx.get(col_sym[cs[5]], gx.N)
        NETb[:, k] = -ypad[:, ui].mean(1) + ypad[:, di]; REFb[:, k] = Tm @ reg_vec([col_sym[c] for c in cs])
    C2b = {"NET-EXT": rho_inputs(NETb), "REF-1": rho_inputs(REFb)}
    log("nulls C1/C2 done", round(time.time() - t0), "s")
    # ---- matched family sets (control 3) ------------------------------------------------------------
    terc = np.digitize(ntar, np.quantile(ntar, [1 / 3, 2 / 3])); rk_OE = rankdata(OE); ntop = int(math.ceil(0.1 * nU))
    rngm = np.random.default_rng(SEED + 13)
    def matched_p(score):
        top = np.argsort(-rankdata(score), kind="stable")[:ntop]; obs = rk_OE[top].mean(); comp = collections.Counter(terc[top])
        sims = []
        for _ in range(1000):
            pick = np.concatenate([rngm.choice(np.where(terc == t)[0], n, replace=False) for t, n in comp.items()]); sims.append(rk_OE[pick].mean())
        return float(obs), float(np.mean(np.array(sims) >= obs))
    top_dec = lambda sc: (lambda a, b: len(set(a) & set(b)) / ntop)(np.argsort(-rankdata(sc), kind="stable")[:ntop], np.argsort(-rk_OE, kind="stable")[:ntop])
    matched = {k: matched_p(M[k]) for k in ["SIG", "NET-EXT", "NET-WWOX", "REF-1"]}
    tophit = {k: top_dec(M[k]) for k in M}
    # ---- direction-perturbed ------------------------------------------------------------------------
    rngs = np.random.default_rng(SEED + 21)
    signperm = []
    for _ in range(200):
        sg = np.array([e[2] for e in ext]); sg = rngs.permutation(sg)
        g = Graph([(e[0], e[1], int(s)) for e, s in zip(ext, sg)]); signperm.append(spearman(net_score(g.prop(x0_matrix(g)), *readout_idx(g, UP5, DOWN1)), OE))
    signperm = np.array(signperm)
    place = {}
    for j, gname in enumerate(SIX):
        upsyms = [s for s in SIX if s != gname]
        place[gname] = {"NET-EXT": spearman(net_score(Y, *readout_idx(gx, upsyms, gname)), OE),
                        "SIG": spearman(fam_med(os_real(up=[sym_col[s] for s in upsyms], dn=sym_col[gname]), U, famB), OE)}
    rho_flip = spearman(-NET, OE)
    log("direction-perturbed done", round(time.time() - t0), "s")
    # ---- structure sensitivity -------------------------------------------------------------------------
    rngd = np.random.default_rng(SEED + 22); drop = []
    for _ in range(100):
        keep = rngd.random(len(ext)) >= 0.2; g = Graph([e for e, kp in zip(ext, keep) if kp])
        drop.append(spearman(net_score(g.prop(x0_matrix(g)), *readout_idx(g, UP5, DOWN1)), OE))
    drop = np.array(drop)
    import random
    rw = []
    base_edges = list(ext); eset = set((e[0], e[1]) for e in base_edges)
    nsw = int(os.environ.get("P3_REWIRE_SWAPS_X", "50")) * len(base_edges); nrep = int(os.environ.get("P3_REWIRE_REPS", "100"))
    for rep in range(nrep):
        r = random.Random(SEED + 23 + rep); E = [list(e) for e in base_edges]; es = set(eset)
        for _ in range(nsw):
            i, j = r.randrange(len(E)), r.randrange(len(E)); a, b = E[i], E[j]
            if a[0] == b[0] or a[1] == b[1] or a[0] == b[1] or b[0] == a[1]: continue
            if (a[0], b[1]) in es or (b[0], a[1]) in es: continue
            es.discard((a[0], a[1])); es.discard((b[0], b[1])); a[1], b[1] = b[1], a[1]; es.add((a[0], a[1])); es.add((b[0], b[1]))
        g = Graph([tuple(e) for e in E]); rw.append(spearman(net_score(g.prop(x0_matrix(g)), *readout_idx(g, UP5, DOWN1)), OE))
    rw = np.array(rw)
    log("structure sensitivity done", round(time.time() - t0), "s")
    # ---- frequent hitters ---------------------------------------------------------------------------------
    def fh(score_mat):
        top = np.zeros(nU)
        for k in range(score_mat.shape[1]):
            top[np.argsort(-rankdata(score_mat[:, k]), kind="stable")[:ntop]] += 1
        return top / score_mat.shape[1]
    FH = {"SIG": fh(OBr), "NET-EXT": fh(NETr), "REF-1": fh(REFr)}
    flagged = {k: v >= 0.25 for k, v in FH.items()}
    flagged["NET-WWOX"] = flagged["NET-EXT"]
    rho_noFH = {k: (spearman(M[k][~flagged[k]], OE[~flagged[k]]) if k in flagged and (~flagged[k]).sum() > 20 else None) for k in ["SIG", "NET-EXT", "NET-WWOX", "REF-1"]}
    # ---- bootstrap -------------------------------------------------------------------------------------------
    rngb = np.random.default_rng(SEED + 24); BS = {k: [] for k in ["SIG", "NET-EXT", "NET-WWOX", "REF-1"]}
    for _ in range(1000):
        ii = rngb.integers(0, nU, nU); oe = OE[ii]
        for k in BS: BS[k].append(spearman(M[k][ii], oe))
    BS = {k: np.array(v) for k, v in BS.items()}
    ci = lambda a: [pct(a, 5), pct(a, 95)]
    # ---- swapped contexts and sensitivities ----------------------------------------------------------------------
    swap = {"SIG": spearman(OE, OB), "NET-EXT": spearman(NET, OB), "NET-WWOX": spearman(NETW, OB), "REF-1": spearman(REF1, OB)}
    sel1024 = np.array([s["dose"] == "10 uM" and s["time"] == "24 h" for s in sigs])
    def fam_med_sub(vec, fams, table, mask):
        o = []
        for f in fams:
            ids = [i for i in table[f] if mask[i]]; o.append(np.median(vec[ids]) if ids else np.nan)
        return np.array(o)
    OE_s, OB_s = fam_med_sub(OS, U, famE, sel1024), fam_med_sub(OS, U, famB, sel1024); ok = ~np.isnan(OE_s) & ~np.isnan(OB_s)
    sens = {"signatures_10uM_24h_only": {"n": int(ok.sum()), "SIG": spearman(OB_s[ok], OE_s[ok]) if ok.sum() > 10 else None,
            **{k: spearman(M[k][ok], OE_s[ok]) if ok.sum() > 10 else None for k in ["NET-EXT", "REF-1"]}}}
    OE5, OB5 = fam_med(OS_up5, U, famE), fam_med(OS_up5, U, famB)
    sens["up5_only_readout"] = {"SIG": spearman(OB5, OE5), "NET-EXT": spearman(NET_up5, OE5), "REF-1": spearman(REF1, OE5)}
    sens["NET_direct_k0_included"] = spearman(NET_direct, OE)
    # ---- known examples (descriptive, firewall item iii) -------------------------------------------------------------
    known = []
    for i, f in enumerate(U):
        if cards.get(f, "none") not in ("none", ""):
            known.append({"family": f, "name": names[f], "cards": cards[f], "pct_OE": float((rk_OE[i] - 0.5) / nU),
                          **{k: float((rankdata(M[k])[i] - 0.5) / nU) for k in ["SIG", "NET-EXT", "REF-1"]}})
    # ---- verdicts --------------------------------------------------------------------------------------------------------
    def signal(k):
        d = {"S1": rho[k] >= 0.15}
        c1 = pct(C1[k], 95); d["S2_C1"] = rho[k] > c1
        d["S2_C2"] = (rho[k] > pct(C2[k], 95)) if k in C2 else True
        d["S3"] = pct(BS[k], 5) > 0
        if k.startswith("NET"):
            d["S3"] = d["S3"] and float(np.median(drop)) >= 0.10 and float((drop > 0).mean()) >= 0.90
            d["S4"] = rho[k] > pct(signperm, 90)
        d["S5"] = rho_noFH.get(k) is not None and rho_noFH[k] >= 0.10
        return all(d.values()), d
    def verdict(k):
        sg, det = signal(k); diffs = BS[k] - BS["REF-1"]; dp = rho[k] - rho["REF-1"]
        if nU < 150: return "INCONCLUSIVE (|U|<150)", det, dp, ci(diffs)
        added = sg and dp >= 0.05 and pct(diffs, 5) > 0 and swap[k] >= 0.10 and swap[k] > swap["REF-1"]
        if added: return "ADDED VALUE", det, dp, ci(diffs)
        if not sg: return "NO ADDED VALUE (no signal)", det, dp, ci(diffs)
        if dp < 0.05 and pct(diffs, 95) <= 0.10: return "NO ADDED VALUE (signal, not above reference)", det, dp, ci(diffs)
        return "INCONCLUSIVE", det, dp, ci(diffs)
    V = {k: verdict(k) for k in ["NET-EXT", "SIG", "NET-WWOX"]}
    dW = BS["NET-WWOX"] - BS["NET-EXT"]
    wwox_added = (rho["NET-WWOX"] - rho["NET-EXT"] >= 0.03) and pct(dW, 5) > 0
    summary = dict(synthetic=synth, nU=nU, n_signatures=len(sigs), n_families_B=len(famB), n_families_E=len(famE), graph_nodes=gx.N, graph_edges=len(ext),
                   families_with_target_in_graph=int((np.abs(X0).sum(1) > 0).sum()), REF0_hits_in_578=REF0_all, REF1_nonzero=int((REF1 > 0).sum()),
                   readouts_in_graph={s: s in gx.idx for s in SIX}, rho=rho, tophit_decile=tophit, matched_set={k: {"mean_rank_OE": v[0], "p": v[1]} for k, v in matched.items()},
                   null_C1={k: {"p95": pct(v, 95), "p50": pct(v, 50), "emp_p": float((v >= rho[k]).mean())} for k, v in C1.items()},
                   null_C2={k: {"p95": pct(v, 95), "p50": pct(v, 50), "emp_p": float((v >= rho[k]).mean())} for k, v in C2.items()},
                   null_C2b_added_not_preregistered={k: {"p95": pct(v, 95), "p50": pct(v, 50), "emp_p": float((v >= rho[k]).mean())} for k, v in C2b.items()},
                   sign_permuted_networks={"p50": pct(signperm, 50), "p90": pct(signperm, 90), "emp_p": float((signperm >= rho["NET-EXT"]).mean())},
                   placement_of_down_gene=place, rho_global_flip=rho_flip,
                   edge_dropout20={"median": float(np.median(drop)), "p5": pct(drop, 5), "p95": pct(drop, 95), "share_positive": float((drop > 0).mean())},
                   rewiring={"reps": nrep, "median": float(np.median(rw)), "p5": pct(rw, 5), "p95": pct(rw, 95)},
                   frequent_hitters={k: {"flagged": int(flagged[k].sum()), "names_top5": [names[U[i]] for i in np.argsort(-FH[k])[:5]], "max_rate": float(FH[k].max())} for k in FH},
                   rho_without_frequent_hitters=rho_noFH, bootstrap90={k: ci(v) for k, v in BS.items()},
                   diff_vs_REF1_90={k: ci(BS[k] - BS["REF-1"]) for k in ["SIG", "NET-EXT", "NET-WWOX"]}, diff_WWOX_minus_EXT_90=ci(dW),
                   swapped_contexts=swap, sensitivities=sens, known_examples=known,
                   verdicts={k: {"verdict": v[0], "criteria": {a: bool(b) for a, b in v[1].items()}, "rho_diff_vs_REF1": v[2], "diff90": v[3]} for k, v in V.items()},
                   WWOX_edges_add_value=bool(wwox_added), wall_seconds=round(time.time() - t0))
    suffix = "_SYNTHETIC" if synth else ""
    json.dump(summary, open(f"{out}/results_summary{suffix}.json", "w"), indent=1, default=float)
    with open(f"{out}/family_scores{suffix}.tsv", "w") as o:
        o.write("family_id\tname\tcards\tn_targets\tO_E\tO_B_SIG\tNET_EXT\tNET_WWOX\tREF1\tREF0\tfreq_hit_rate_SIG\tfreq_hit_rate_NET\tfreq_hit_rate_REF1\n")
        for i, f in enumerate(U):
            o.write("\t".join([f, names[f], cards[f], str(int(ntar[i])), f"{OE[i]:.4f}", f"{OB[i]:.4f}", f"{NET[i]:.5g}", f"{NETW[i]:.5g}", f"{REF1[i]:.5g}", f"{REF0[i]:.0f}", f"{FH['SIG'][i]:.3f}", f"{FH['NET-EXT'][i]:.3f}", f"{FH['REF-1'][i]:.3f}"]) + "\n")
    with open(f"{out}/signature_scores{suffix}.tsv", "w") as o:
        o.write("sig_id\tpert_id\tcell_id\tdose\ttime\tcontext_class\topposition_score\n")
        for i, s in enumerate(sigs): o.write(f"{s['sig_id']}\t{s['pert_id']}\t{s['cell']}\t{s['dose']}\t{s['time']}\t{s['cls']}\t{OS[i]:.4f}\n")
    log("E2 done", suffix, json.dumps({k: v["verdict"] for k, v in summary["verdicts"].items()}))

# ============================================================================================ E1
def run_e1():
    counts = arg("--counts"); out = arg("--out", os.path.join(HERE, "results")); os.makedirs(out, exist_ok=True)
    op = gzip.open if counts.endswith(".gz") else open
    rows = list(csv.reader(op(counts, "rt")))
    hdr = rows[0]; body = rows[1:]
    gcol = int(os.environ.get("P3_GENE_COL", "0"))
    samples = [(i, h) for i, h in enumerate(hdr) if "_WT/WT_" in h or "_P47T/P47T_" in h]
    gene = [r[gcol] for r in body]
    X = np.array([[float(r[i]) for i, _ in samples] for r in body])
    lib = X.sum(0); cpm = X / lib * 1e6; L = np.log2(cpm + 1)
    sidx = collections.defaultdict(list)
    for j, (_, h) in enumerate(samples):
        reg, rest = h.split("_", 1); geno = "mut" if rest.startswith("P47T") else "wt"; animal = rest.split("_")[-1]
        sidx[reg].append((j, geno, animal))
    mouse = {"SLC2A1": "Slc2a1", "HK2": "Hk2", "LDHA": "Ldha", "LDHB": "Ldhb", "BNIP3": "Bnip3", "PDK1": "Pdk1"}
    gi = {}
    for i, g in enumerate(gene): gi.setdefault(g, i)
    up_i = [gi[mouse[g]] for g in UP5]; dn_i = gi[mouse[DOWN1]]
    rng = np.random.default_rng(SEED + 31); res = {}
    animals_all = {}
    from itertools import combinations
    def perm_p(score, lab):
        obs = score[lab].mean() - score[~lab].mean(); n = len(score); k = int(lab.sum()); cnt = tot = 0
        for c in combinations(range(n), k):
            m = np.zeros(n, bool); m[list(c)] = True; d = score[m].mean() - score[~m].mean(); tot += 1; cnt += d >= obs - 1e-12
        return float(obs), cnt / tot, tot
    for reg, lst in sidx.items():
        cols = [j for j, _, _ in lst]; lab = np.array([g == "mut" for _, g, _ in lst]); an = [a for _, _, a in lst]
        Lr = L[:, cols]; meanc = cpm[:, cols].mean(1)
        lfc = Lr[:, lab].mean(1) - Lr[:, ~lab].mean(1); ok = meanc >= 1
        cl = lfc - np.median(lfc[ok])
        D = cl[up_i].mean() - cl[dn_i]
        # matched null on mean-expression decile
        dec = np.digitize(meanc, np.quantile(meanc[ok], np.linspace(0.1, 0.9, 9)))
        real = up_i + [dn_i]; excl = set(real) | {i for i, g in enumerate(gene) if g.capitalize().startswith(("Slc2a", "Hk", "Ldh", "Pdk", "Pfk", "Pgk", "Eno", "Aldo", "Pkm", "Pgam", "Tpi", "Gapdh", "Pdh"))}
        cand = {d: np.array([i for i in range(len(gene)) if ok[i] and dec[i] == d and i not in excl]) for d in range(10)}
        nd = []
        for _ in range(1000):
            used = set(); s = []
            for r_ in real:
                while True:
                    c = int(rng.choice(cand[dec[r_]]))
                    if c not in used: used.add(c); s.append(c); break
            nd.append(cl[s[:5]].mean() - cl[s[5]])
        nd = np.array(nd)
        gm = Lr.mean(1)
        sa = (Lr[up_i] - gm[up_i, None]).mean(0) - (Lr[dn_i] - gm[dn_i])
        obs, p, tot = perm_p(sa, lab)
        conc = int(sum(cl[i] > 0 for i in up_i) + (cl[dn_i] < 0))
        res[reg] = dict(n_mut=int(lab.sum()), n_wt=int((~lab).sum()), D=float(D), null_p95=pct(nd, 95), null_p5=pct(nd, 5), above_p95=bool(D > pct(nd, 95)), exact_p_one_sided=p, n_assignments=tot,
                        genes_concordant_of_6=conc, up5_mean_cLFC=float(cl[up_i].mean()), per_gene_cLFC={g: float(cl[gi[mouse[g]]]) for g in SIX}, animal_scores=dict(zip(an, sa.round(4).tolist())), mut_animals=[a for a, l in zip(an, lab) if l])
        for a, s_, l in zip(an, sa, lab): animals_all.setdefault(a, {"mut": bool(l), "s": []})["s"].append(float(s_))
    r = res["HPC"]
    transfers = r["above_p95"] and r["exact_p_one_sided"] <= 0.05 and r["genes_concordant_of_6"] >= 4 and r["up5_mean_cLFC"] > 0
    nottr = (not r["above_p95"]) and r["exact_p_one_sided"] > 0.05 and r["genes_concordant_of_6"] <= 3
    ans = sorted(animals_all); sc = np.array([np.mean(animals_all[a]["s"]) for a in ans]); lab = np.array([animals_all[a]["mut"] for a in ans])
    obs, p, tot = perm_p(sc, lab)
    males = [i for i, a in enumerate(ans) if a.startswith("M")]; females = [i for i, a in enumerate(ans) if a.startswith("F")]
    def strat():
        obs_ = sc[lab].mean() - sc[~lab].mean(); cnt = tot_ = 0
        km, kf = int(lab[males].sum()), int(lab[females].sum())
        for cm in combinations(males, km):
            for cf in combinations(females, kf):
                m = np.zeros(len(ans), bool); m[list(cm) + list(cf)] = True; tot_ += 1; cnt += (sc[m].mean() - sc[~m].mean()) >= obs_ - 1e-12
        return cnt / tot_, tot_
    sp, st = strat()
    summary = dict(verdict="TRANSFERS" if transfers else "DOES NOT TRANSFER" if nottr else "INCONCLUSIVE", primary_region="HPC", regions=res,
                   animal_level_all_regions={"diff": float(obs), "exact_p": p, "n_assignments": tot, "animals": ans, "sex_stratified_p": sp, "sex_stratified_assignments": st})
    json.dump(summary, open(f"{out}/e1_p47t_summary.json", "w"), indent=1, default=float)
    log("E1 done", summary["verdict"])

run_e2() if sys.argv[1] == "e2" else run_e1()

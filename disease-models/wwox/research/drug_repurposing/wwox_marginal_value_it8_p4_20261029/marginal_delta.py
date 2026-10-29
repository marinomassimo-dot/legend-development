#!/usr/bin/env python3
"""IT8 P4 diagnosis: marginal contribution of WWOX inputs to the IT7 P3 network comparison.

Read-only toward IT7 P3 (inputs and results). Re-derives, from the committed IT7 tables only:
  A. the exact input delta between NET-EXT and NET-WWOX (nodes, edges, signs, families whose score changes);
  B. a power-only simulation: how large an edge delta would a paired comparison need to detect |d rho| >= 0.03
     (HYPOTHETICAL random edge sets; these are NOT WWOX relations and are never an arm of any comparison);
  C. non-outcome counts for LINCS signature quality (how many IT7 signatures pass conventional quality thresholds).
The held-out outcome O_E of IT7 is used ONLY in B to size a paired-difference standard error. It is already opened (IT7),
so nothing computed from it here can be a new test. No verdict is produced.

Usage: marginal_delta.py --p3 DIR --out DIR [--lincs DIR] ; --help answers without work. Needs numpy.
"""
import sys, os, csv, gzip, math, json, collections

if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) == 1:
    print(__doc__); sys.exit(0)

import numpy as np

def arg(n, d=None):
    return sys.argv[sys.argv.index(n) + 1] if n in sys.argv else d

P3 = arg("--p3"); OUT = arg("--out"); LINCS = arg("--lincs", "/home/desktop/legend-development/files/geo/GSE92742")
INP = f"{P3}/inputs"; RES = f"{P3}/results"
K, GAMMA = 3, 0.5
UP5 = ["SLC2A1", "HK2", "LDHA", "LDHB", "BNIP3"]; DOWN1 = "PDK1"

def tsv(p):
    op = gzip.open if p.endswith(".gz") else open
    with op(p, "rt", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def rankdata(a):
    a = np.asarray(a, float); o = np.argsort(a, kind="mergesort"); r = np.empty(len(a)); r[o] = np.arange(len(a))
    s = a[o]; i = 0
    while i < len(a):
        j = i
        while j + 1 < len(a) and s[j + 1] == s[i]: j += 1
        r[o[i:j + 1]] = (i + j) / 2; i = j + 1
    return r

def spearman(a, b):
    x = rankdata(a); y = rankdata(b); x = x - x.mean(); y = y - y.mean()
    d = math.sqrt((x * x).sum() * (y * y).sum()); return float((x * y).sum() / d) if d else 0.0

# ---- edges as in p3_run.py (same reading rule) ---------------------------------------------------
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
    return [(s, t, sg) for (s, t), sg in E.items() if sg != 0], E

ext, Eraw = read_edges(["signor_omnipath_edges.tsv.gz", "collectri_omnipath_edges.tsv.gz"])
nodes_p1 = {r["node_id"]: r["symbol"] for r in tsv(f"{INP}/nodes.tsv")}
p1_edges = tsv(f"{INP}/edges.tsv")
wwox_add = []
for r in p1_edges:
    if r["edge_type"] == "inferred" and r["source_node"].startswith("HGNC:") and r["target_node"].startswith("HGNC:") and r["sign"] in ("up", "down"):
        wwox_add.append((nodes_p1[r["source_node"]], nodes_p1[r["target_node"]], 1 if r["sign"] == "up" else -1))

extset = {(s, t): sg for s, t, sg in ext}
ext_nodes = {e[0] for e in ext} | {e[1] for e in ext}
A = {"external_edges": len(ext), "external_nodes": len(ext_nodes), "wwox_added_edges": len(wwox_add), "added_edges": []}
n_new_edges = n_new_nodes = n_sign_conflict = n_present_same = 0
for s, t, sg in wwox_add:
    status = ("absent_in_external" if (s, t) not in extset else ("present_same_sign" if extset[(s, t)] == sg else "present_opposite_sign"))
    if (s, t) in Eraw and Eraw[(s, t)] == 0: status = "present_conflicting_signs_dropped_in_external"
    A["added_edges"].append({"source": s, "target": t, "sign": sg, "status": status,
                              "source_in_ext": s in ext_nodes, "target_in_ext": t in ext_nodes})
    if status == "absent_in_external": n_new_edges += 1
    elif status == "present_same_sign": n_present_same += 1
    else: n_sign_conflict += 1
    n_new_nodes += (s not in ext_nodes) + (t not in ext_nodes)
A.update(new_edges=n_new_edges, already_present_same_sign=n_present_same, sign_conflicts=n_sign_conflict, new_nodes=n_new_nodes)
A["WWOX_node_in_external"] = "WWOX" in ext_nodes
A["WWOX_edges_in_external"] = [e for e in ext if e[0] == "WWOX" or e[1] == "WWOX"]
A["HIF1A_out_degree_external"] = sum(1 for e in ext if e[0] == "HIF1A")
A["HIF1A_to_six_readouts_in_external"] = {t: extset.get(("HIF1A", t)) for t in UP5 + [DOWN1]}
A["p1_edge_type_counts"] = {f"{a}|{b}": n for (a, b), n in collections.Counter((r["edge_type"], r["target_readout"]) for r in p1_edges).most_common()}
A["p1_gene_gene_edges"] = [(nodes_p1[r["source_node"]], nodes_p1[r["target_node"]], r["edge_type"], r["sign"]) for r in p1_edges
                           if r["source_node"].startswith("HGNC:") and r["target_node"].startswith("HGNC:") and r["source_node"] != "HGNC:12799"]

# ---- graph and propagation (same as p3_run.py) --------------------------------------------------
class Graph:
    def __init__(s, edges):
        syms = sorted({e[0] for e in edges} | {e[1] for e in edges}); s.idx = {g: i for i, g in enumerate(syms)}; s.N = len(syms)
        src = np.array([s.idx[e[0]] for e in edges]); tgt = np.array([s.idx[e[1]] for e in edges]); sg = np.array([e[2] for e in edges], np.float32)
        od = np.bincount(src, minlength=s.N).astype(np.float32); w = sg / od[src]
        o = np.argsort(tgt, kind="stable"); s.src, s.tgt, s.w = src[o], tgt[o], w[o]
        s.ut, s.starts = np.unique(s.tgt, return_index=True)
    def hop(s, X):
        c = X[:, s.src] * s.w; out = np.zeros_like(X); out[:, s.ut] = np.add.reduceat(c, s.starts, axis=1); return out
    def prop(s, X):
        y = np.zeros_like(X); h = X
        for k in range(1, K + 1):
            h = s.hop(h); y += (GAMMA ** (k - 1)) * h
        return y

fam_rows = tsv(f"{RES}/family_scores.tsv")
U = [r["family_id"] for r in fam_rows]; nU = len(U)
OE = np.array([float(r["O_E"]) for r in fam_rows]); NET_ref = np.array([float(r["NET_EXT"]) for r in fam_rows]); NETW_ref = np.array([float(r["NET_WWOX"]) for r in fam_rows])
sgn = {"down": -1.0, "up": 1.0}
fam_t = collections.defaultdict(lambda: collections.defaultdict(list))
Uset = set(U)
for r in tsv(f"{INP}/pilot_net_actions.tsv"):
    if r["family_id"] not in Uset or r["sign"] not in sgn: continue
    for t in r["target_symbol"].split(";"): fam_t[r["family_id"]][t].append(sgn[r["sign"]])
famT = {f: {t: float(np.mean(v)) for t, v in fam_t[f].items()} for f in U}

def x0(g):
    X = np.zeros((nU, g.N), np.float32)
    for i, f in enumerate(U):
        v = famT[f]; nrm = math.sqrt(sum(a * a for a in v.values()))
        if nrm == 0: continue
        for t, a in v.items():
            if t in g.idx: X[i, g.idx[t]] = a / nrm
    return X

def score(g):
    y = g.prop(x0(g)); yp = np.concatenate([y, np.zeros((nU, 1), np.float32)], 1)
    upi = [g.idx.get(s, g.N) for s in UP5]; dni = g.idx.get(DOWN1, g.N)
    return -yp[:, upi].mean(1) + yp[:, dni]

g0 = Graph(ext); S0 = score(g0)
gW = Graph(ext + wwox_add); SW = score(gW)
A["reproduction_max_abs_diff_NET_EXT"] = float(np.abs(S0 - NET_ref).max())
A["reproduction_max_abs_diff_NET_WWOX"] = float(np.abs(SW - NETW_ref).max())
d = SW - S0
A["families_total"] = nU
A["families_with_any_score_change"] = int((np.abs(d) > 1e-9).sum())
A["families_with_change_gt_1e-4"] = int((np.abs(d) > 1e-4).sum())
A["max_abs_score_change"] = float(np.abs(d).max())
A["sd_of_NET_EXT_scores"] = float(S0.std())
A["max_change_in_sd_units"] = float(np.abs(d).max() / S0.std()) if S0.std() else None
A["families_nonzero_NET_EXT"] = int((np.abs(S0) > 1e-12).sum())
A["rho_NETEXT_vs_NETWWOX_scores"] = spearman(S0, SW)
A["rho_EXT_vs_OE"] = spearman(S0, OE); A["rho_WWOX_vs_OE"] = spearman(SW, OE)
A["changed_families"] = [{"family": U[i], "name": fam_rows[i]["name"], "delta": float(d[i]), "NET_EXT": float(S0[i])} for i in np.argsort(-np.abs(d))[:10] if abs(d[i]) > 1e-9]
# in-silico: how many families can reach HIF1A within K hops at all (upper bound on who the 4 edges could touch)
reach = np.zeros(nU, bool)
if "HIF1A" in g0.idx:
    xh = np.zeros((nU, g0.N), np.float32)
    for i, f in enumerate(U):
        for t in famT[f]:
            if t in g0.idx: xh[i, g0.idx[t]] = 1.0
    # forward reachability within K hops from targets, count of families whose targets reach HIF1A
    h = np.abs(xh); acc = h.copy()
    gabs = Graph([(s, t, 1) for s, t, _ in ext])
    for _ in range(K):
        h = (gabs.hop(h) > 0).astype(np.float32); acc = np.maximum(acc, h)
    reach = acc[:, g0.idx["HIF1A"]] > 0
A["families_whose_targets_reach_HIF1A_within_K_hops_incl_direct"] = int(reach.sum())
A["families_with_direct_target_HIF1A"] = int(sum(1 for f in U if "HIF1A" in famT[f]))

# ---- B. power-only simulation -------------------------------------------------------------------
rng = np.random.default_rng(20261029 + 801)
B = {"note": "HYPOTHETICAL random edges between nodes of the external graph, signs random; sizes only; NOT WWOX relations; O_E is the IT7 opened outcome and is used only to size the paired-difference spread"}
def bootstrap_pair_diff(Sa, Sb, reps=400):
    r = np.random.default_rng(20261029 + 802); out = np.empty(reps)
    for b in range(reps):
        ix = r.integers(0, nU, nU); out[b] = spearman(Sb[ix], OE[ix]) - spearman(Sa[ix], OE[ix])
    return out
dW = bootstrap_pair_diff(S0, SW)
B["observed_paired_diff_rho"] = float(spearman(SW, OE) - spearman(S0, OE))
B["observed_paired_diff_boot_SE"] = float(dW.std()); B["observed_paired_diff_boot90"] = [float(np.percentile(dW, 5)), float(np.percentile(dW, 95))]
B["independent_rho_SE_at_nU"] = 1 / math.sqrt(nU - 3) * 1.0  # Fisher-z SE approx
B["MDE_independent_rho_80pct_power_one_sided_5pct"] = 2.4865 * (1 / math.sqrt(nU - 3))  # (1.645+0.84) * SE, SE in z units; ~= rho scale near 0
nodes_list = sorted(ext_nodes)
sizes = [4, 25, 100, 400, 1600, 6400]
rows = []
for k in sizes:
    diffs = []; nchg = []
    for rep in range(30 if k <= 1600 else 12):
        ia = rng.integers(0, len(nodes_list), k); ib = rng.integers(0, len(nodes_list), k)
        add = [(nodes_list[a], nodes_list[b], int(rng.choice([-1, 1]))) for a, b in zip(ia, ib) if a != b and (nodes_list[a], nodes_list[b]) not in extset]
        gk = Graph(ext + add); Sk = score(gk)
        diffs.append(spearman(Sk, OE) - spearman(S0, OE)); nchg.append(int((np.abs(Sk - S0) > 1e-9).sum()))
    rows.append({"edges_added": k, "pct_of_external_edges": round(100 * k / len(ext), 3), "families_changed_median": int(np.median(nchg)),
                 "abs_d_rho_median": float(np.median(np.abs(diffs))), "abs_d_rho_p95": float(np.percentile(np.abs(diffs), 95)), "reps": len(diffs)})
B["random_edge_additions"] = rows

# ---- C. LINCS quality counts (no outcome) --------------------------------------------------------
C = {}
try:
    sigs = tsv(f"{RES}/signature_scores.tsv")
    met = {}
    with gzip.open(f"{LINCS}/GSE92742_Broad_LINCS_sig_metrics.txt.gz", "rt") as f:
        rd = csv.DictReader(f, delimiter="\t")
        for r in rd: met[r["sig_id"]] = r
    C["signatures_in_IT7_scores"] = len(sigs); C["found_in_sig_metrics"] = sum(1 for s in sigs if s["sig_id"] in met)
    def passes(m, cc=0.2, sr=5.0):
        try: a = float(m["distil_cc_q75"]); b = float(m["pct_self_rank_q25"])
        except Exception: return False
        return a >= cc and 0 <= b <= sr
    def miss(m): return float(m["distil_cc_q75"]) == -666.0
    byc = collections.defaultdict(lambda: collections.Counter())
    pass_fam = {"B": collections.defaultdict(int), "E": collections.defaultdict(int)}
    pert2fam = collections.defaultdict(set)
    for r in tsv(f"{INP}/pilot_lincs_contexts.tsv"): pert2fam[r["pert_id"]].add(r["family_id"])
    for s in sigs:
        m = met.get(s["sig_id"]);
        if not m: continue
        c = s["context_class"]; byc[c]["n"] += 1
        byc[c]["cc_missing_(-666)"] += int(miss(m)); byc[c]["pass_cc>=0.2_&_selfrank<=5"] += int(passes(m))
        byc[c]["nsample>=3"] += int(float(m["distil_nsample"]) >= 3)
        if passes(m):
            for fam in pert2fam[s["pert_id"]]:
                if fam in Uset: pass_fam[c][fam] += 1
    C["by_context_class"] = {k: dict(v) for k, v in byc.items()}
    bothq = set(pass_fam["B"]) & set(pass_fam["E"])
    C["families_in_U"] = nU; C["families_with_passing_signature_in_B"] = len(set(pass_fam["B"]) & Uset)
    C["families_with_passing_signature_in_E"] = len(set(pass_fam["E"]) & Uset); C["families_with_passing_in_both_B_and_E"] = len(bothq)
    # gene_info landmark status of the six readouts (measured vs inferred)
    lm = {}
    with gzip.open(f"{LINCS}/GSE92742_Broad_LINCS_gene_info.txt.gz", "rt") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if r["pr_gene_symbol"] in UP5 + [DOWN1]: lm[r["pr_gene_symbol"]] = {"landmark_measured": r["pr_is_lm"], "bing_inferred_or_measured": r["pr_is_bing"]}
    C["six_readouts_L1000_status"] = lm
except FileNotFoundError as e:
    C["error"] = str(e)


# ---- D. what a WWOX out-edge could do (sizing only; scenarios are not proposals) -------------------------------------
D = {"note": "WWOX is a sink in the external graph (in-edges only). Scenario edges are the only gene-level relations the P1 table holds that involve WWOX; they are sized, not adopted. S_B encodes the readout answer in the network (circular by construction)."}
wwox_regs = sorted({e[0] for e in ext if e[1] == "WWOX"})
D["WWOX_regulators_in_external"] = wwox_regs
fam_with_reg = [f for f in U if any(r in famT[f] for r in wwox_regs)]
D["families_in_U_with_a_direct_target_among_WWOX_regulators"] = len(fam_with_reg)
D["those_families"] = [fam_rows[U.index(f)]["name"] for f in fam_with_reg]
D["families_in_U_with_WWOX_as_target"] = int(sum(1 for f in U if "WWOX" in famT[f]))
def scen(name, add):
    g = Graph(ext + add); S = score(g); dd = S - S0
    return {"scenario": name, "edges": [(a, b, c) for a, b, c in add], "families_changed(>1e-9)": int((np.abs(dd) > 1e-9).sum()),
            "families_changed(>1e-4)": int((np.abs(dd) > 1e-4).sum()), "max_abs_change": float(np.abs(dd).max()),
            "max_change_in_SD_of_NET_EXT": float(np.abs(dd).max() / S0.std()), "rho_with_O_E": spearman(S, OE),
            "paired_diff_rho_vs_EXT (descriptive, IT7-opened outcome)": float(spearman(S, OE) - spearman(S0, OE)),
            "spearman_scores_vs_EXT": spearman(S, S0)}
D["S_A_WWOX_to_HIF1A_loss_raises_protein_(MEF_and_cancer_cells,_non-neural)"] = scen("S_A", [("WWOX", "HIF1A", -1)])
D["S_B_WWOX_to_six_readouts_in_module_direction_(circular)"] = scen("S_B", [("WWOX", g_, -1) for g_ in UP5] + [("WWOX", DOWN1, 1)])
D["S_C_both"] = scen("S_C", [("WWOX", "HIF1A", -1)] + [("WWOX", g_, -1) for g_ in UP5] + [("WWOX", DOWN1, 1)])
# ---- E. card-linked (WWOX-system intervention) families: how many are even in the universe -----------------------------
sub = tsv(f"{INP}/pilot_subset.tsv")
cl = [r for r in sub if r["card_ids"] not in ("", "none", "NONE")]
E = {"card_linked_families_in_pilot": len(cl), "card_linked_usable_by_both_methods": sum(1 for r in cl if r["usable_by_both_Mnet_and_Msig_neural"] == "yes"),
     "card_linked_in_U": sum(1 for r in cl if r["family_id"] in Uset), "names_in_U": [r["name"] for r in cl if r["family_id"] in Uset]}
res = {"A_input_delta": A, "B_power": B, "C_signature_quality_counts": C, "D_WWOX_out_edge_scenarios": D, "E_card_linked_truth_availability": E}
os.makedirs(OUT, exist_ok=True)
json.dump(res, open(f"{OUT}/marginal_delta_results.json", "w"), indent=1, default=str)
print(json.dumps(res, indent=1, default=str)[:6000])

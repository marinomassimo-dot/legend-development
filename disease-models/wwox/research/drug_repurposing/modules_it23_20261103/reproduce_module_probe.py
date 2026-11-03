#!/usr/bin/env python3
"""IT23 module-discovery probe: first neighbours, RWR and a DIAMOnD-style connectivity test on small LEGEND seed sets.

Self-contained (numpy + scipy). Reads LEGEND seed tables, the LEGEND signed network (used UNSIGNED and undirected here),
STRING v12 human links (key-less download, CC BY 4.0), the engine proposals and the catalogue family actions.
Writes sensitivity.tsv, new_targets.tsv, run_facts.json next to this script.
Module membership gives no causal direction and no intervention benefit; nothing here ranks compounds.

  python3 reproduce_module_probe.py --string-dir DIR   (DIR holds 9606.protein.links.v12.0.txt.gz and 9606.protein.info.v12.0.txt.gz)
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)

import argparse, collections, csv, gzip, json, time
from pathlib import Path
import numpy as np
import scipy.sparse as sp
from scipy.stats import hypergeom

HERE = Path(__file__).resolve().parent
DRUG = HERE.parent
SEEDS = DRUG / "generation_it22_p1_20261103/inputs_it22/seeds_p1"
INPUTS = DRUG / "network_comparison_it7_p3_20261029/inputs"
PROPOSALS = DRUG / "generation_it22_p1_20261103/results_p1/proposals_it21.tsv"
ACTIONS = DRUG / "generation_it21_p2_20261103/results/actions"
TOPM = 50          # list length compared everywhere
DIAMOND_N = 100    # DIAMOnD iterations (pipeline default is 200; only the first TOPM are compared)
RWR_RESTART = 0.5
REPS = 20
HUB_N = 20         # top-degree non-seed nodes removed in the hub test
SEED0 = 20261103


def rd(path):
    op = gzip.open if str(path).endswith(".gz") else open
    with op(path, "rt", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


# ---------------------------------------------------------------- networks
def legend_edges():
    """Same edge reading as seed_engine.read_edges (complexes split, conflicting signs dropped), plus directed list for reach."""
    E = {}
    for fn in ("signor_omnipath_edges.tsv.gz", "collectri_omnipath_edges.tsv.gz"):
        for r in rd(INPUTS / fn):
            srcs = r["source_symbol"].split("_"); tgts = r["target_symbol"].split("_")
            for s in srcs:
                for t in tgts:
                    if s == t: continue
                    sg = int(r["sign"]); k = (s, t)
                    E[k] = sg if (k not in E or E[k] == sg) else 0
    return sorted((s, t) for (s, t), sg in E.items() if sg != 0)


def string_edges(sdir, cutoff):
    info = {}
    for ln in gzip.open(Path(sdir) / "9606.protein.info.v12.0.txt.gz", "rt"):
        if ln.startswith("#"): continue
        p = ln.split("\t"); info[p[0]] = p[1]
    E = set()
    for ln in gzip.open(Path(sdir) / "9606.protein.links.v12.0.txt.gz", "rt"):
        a, b, s = ln.split()
        if a == "protein1" or int(s) < cutoff: continue
        x, y = info.get(a), info.get(b)
        if x and y and x != y: E.add((x, y) if x < y else (y, x))
    return sorted(E)


class Graph:
    def __init__(self, edges):
        und = {(a, b) if a < b else (b, a) for a, b in edges if a != b}
        self.nodes = sorted({n for e in und for n in e}); self.idx = {n: i for i, n in enumerate(self.nodes)}
        self.edges = np.array([(self.idx[a], self.idx[b]) for a, b in sorted(und)], dtype=np.int64)
        self.N = len(self.nodes)

    def adj(self, edges=None, drop=None):
        e = self.edges if edges is None else edges
        if drop is not None and len(drop):
            m = np.ones(self.N, bool); m[list(drop)] = False
            e = e[m[e[:, 0]] & m[e[:, 1]]]
        A = sp.coo_matrix((np.ones(len(e)), (e[:, 0], e[:, 1])), shape=(self.N, self.N)); A = (A + A.T).tocsr(); A.data[:] = 1
        return A


# ---------------------------------------------------------------- the three components
def first_neighbours(A, seeds):
    s = np.zeros(A.shape[0]); s[seeds] = 1
    links = A @ s; links[seeds] = 0
    deg = np.asarray(A.sum(1)).ravel()
    order = sorted(np.flatnonzero(links > 0), key=lambda i: (-links[i], deg[i], i))
    return order, links


def rwr(A, seeds, restart=RWR_RESTART, correct_hub=False, iters=200):
    deg = np.asarray(A.sum(1)).ravel(); inv = np.where(deg > 0, 1 / np.maximum(deg, 1), 0)
    W = A.multiply(inv[None, :]).tocsr()          # column-normalised
    p0 = np.zeros(A.shape[0]); p0[seeds] = 1 / len(seeds); p = p0.copy()
    for _ in range(iters):
        q = (1 - restart) * (W @ p) + restart * p0
        if np.abs(q - p).sum() < 1e-10: p = q; break
        p = q
    sc = p.copy()
    if correct_hub:                                # divide by the degree-proportional steady state (hub control)
        sc = p / np.maximum(deg / max(deg.sum(), 1), 1e-12)
    sc[seeds] = -1; sc[deg == 0] = -1
    return list(np.argsort(-sc, kind="stable")[:TOPM + 0]), sc


def diamond(A, seeds, n=DIAMOND_N, alpha=1):
    """DIAMOnD-style connectivity significance (Ghiassian et al. 2015, MIT-licensed reference code): at each step add the non-module
    node whose number of links to the module is least likely under a hypergeometric null given its degree. Written from the algorithm
    description, not copied."""
    N = A.shape[0]; deg = np.asarray(A.sum(1)).ravel().astype(int)
    inm = np.zeros(N, bool); inm[seeds] = True
    ks = np.asarray(A @ inm.astype(float)).ravel().astype(int)
    added = []
    s0 = len(seeds)
    for _ in range(n):
        cand = np.flatnonzero(~inm & (deg > 0) & (ks > 0))
        if len(cand) == 0: break
        K = int(inm.sum()) + (alpha - 1) * s0
        kb = ks[cand] + (alpha - 1) * 0      # seed-link up-weighting omitted (alpha=1 default of the pipeline)
        p = hypergeom.sf(kb - 1, N, K, deg[cand])
        best = cand[np.lexsort((cand, deg[cand], p))[0]]
        added.append(int(best)); inm[best] = True
        ks += np.asarray(A[:, best].todense()).ravel().astype(int) if False else A[:, best].toarray().ravel().astype(int)
    return added


def run_method(name, A, seeds):
    if name == "first_neighbours":
        o, _ = first_neighbours(A, seeds); return o[:TOPM]
    if name == "rwr":
        return rwr(A, seeds)[0]
    if name == "rwr_hubcorr":
        return rwr(A, seeds, correct_hub=True)[0]
    if name == "diamond":
        return diamond(A, seeds)[:TOPM]
    raise KeyError(name)


METHODS = ["first_neighbours", "rwr", "rwr_hubcorr", "diamond"]


# ---------------------------------------------------------------- seeds, engine, catalogue
def read_seed_sets():
    def load(files):
        rows = []
        for f in files: rows += rd(SEEDS / f)
        return rows
    spec = {"Q2": ["Q2_expression_tiersAB.tsv"], "Q3": ["Q3_expression_tiersAB.tsv"],
            "Q4": ["Q4_expression_tiersAB.tsv", "Q4_protein_tiersAB.tsv"]}
    out = {}
    for q, files in spec.items():
        rows = load(files); g = [r["gene"] for r in rows if r["kind"] == "gene"]
        mem = [m for r in rows if r["kind"] == "process" for m in r["members"].split(";")]
        out[q + "_rows"] = sorted(set(g)); out[q + "_withprocess"] = sorted(set(g) | set(mem))
    return out


def engine_targets():
    by = collections.defaultdict(set)
    for r in rd(PROPOSALS):
        if r["main_target"]: by[r["question"]].add(r["main_target"])
    return by


def catalogue():
    signed = collections.defaultdict(lambda: [0, 0, 0])   # n families with signed action, n(+), n(-)
    for r in rd(ACTIONS / "family_actions.tsv.gz"):
        m = float(r["mean_sign"])
        if m != 0:
            c = signed[r["target_symbol"]]; c[0] += 1; c[1 if m > 0 else 2] += 1
    anyrows = collections.Counter()
    for r in rd(ACTIONS / "family_targets_any.tsv.gz"): anyrows[r["target_symbol"]] += 1
    return signed, anyrows


def engine_reach(dir_edges, seeds, hops=3):
    """Regulators of the seeds within `hops` directed steps in the LEGEND network: where the current engine can look."""
    up = collections.defaultdict(set)
    for s, t in dir_edges: up[t].add(s)
    seen = set(seeds); front = set(seeds)
    for _ in range(hops):
        nxt = set()
        for t in front: nxt |= up.get(t, set())
        nxt -= seen; seen |= nxt; front = nxt
    return seen - set(seeds)


def jac(a, b):
    a, b = set(a), set(b)
    return len(a & b) / len(a | b) if (a | b) else float("nan")


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--string-dir", required=True); ap.add_argument("--out", default=str(HERE))
    a = ap.parse_args(); out = Path(a.out)
    t0 = time.time(); rng = np.random.default_rng(SEED0)
    dedges = legend_edges()
    nets = {"LEGEND_signed_as_unsigned": Graph(dedges), "STRING_v12_min900": Graph(string_edges(a.string_dir, 900))}
    seedsets = read_seed_sets(); eng = engine_targets(); signed, anyrows = catalogue()
    facts = {"networks": {k: {"nodes": g.N, "edges": int(len(g.edges))} for k, g in nets.items()}, "seed_sets": {}, "topm": TOPM,
             "diamond_n": DIAMOND_N, "rwr_restart": RWR_RESTART, "reps": REPS, "hub_n": HUB_N}
    sens, newrows = [], []
    for sname, genes in seedsets.items():
        q = sname.split("_")[0]
        facts["seed_sets"][sname] = {"genes": genes, "n": len(genes)}
        for nname, G in nets.items():
            seeds = [G.idx[g] for g in genes if g in G.idx]; miss = [g for g in genes if g not in G.idx]
            facts["seed_sets"][sname][nname] = {"in_network": len(seeds), "missing": miss}
            if len(seeds) < 3: continue
            A0 = G.adj(); deg = np.asarray(A0.sum(1)).ravel()
            rank_pct = (np.argsort(np.argsort(deg)) + 1) / G.N
            hubs_all = set(np.flatnonzero(rank_pct >= 0.95).tolist())
            order = np.argsort(-deg, kind="stable"); hubs_rm = [int(i) for i in order if int(i) not in set(seeds)][:HUB_N]
            reach = engine_reach(dedges, genes) if nname.startswith("LEGEND") else engine_reach(dedges, genes)
            fn_all, _ = first_neighbours(A0, seeds)
            base = {m: run_method(m, A0, seeds) for m in METHODS}
            loo_freq = {m: collections.Counter() for m in METHODS}
            for m in METHODS:
                names = [G.nodes[i] for i in base[m]]
                hubfrac = np.mean([i in hubs_all for i in base[m]]); meanpct = float(np.mean(rank_pct[base[m]]))
                row = dict(seed_set=sname, network=nname, method=m, n_seeds_in_network=len(seeds), perturbation="baseline", n_runs=1,
                           mean_jaccard="", min_jaccard="", metric="hub_fraction_top5pct_degree", value=f"{hubfrac:.3f}",
                           extra=f"mean_degree_percentile={meanpct:.3f}; list_len={len(base[m])}")
                sens.append(row)
                # leave-one-out
                js, redisc = [], []
                for s in seeds:
                    rest = [x for x in seeds if x != s]
                    if len(rest) < 2: continue
                    L = run_method(m, A0, rest)
                    ref = [x for x in base[m] if x != s]; cur = [x for x in L if x != s]
                    js.append(jac(ref, cur)); redisc.append(s in L)
                    for x in L: loo_freq[m][x] += 1
                sens.append(dict(seed_set=sname, network=nname, method=m, n_seeds_in_network=len(seeds), perturbation="leave_one_seed_out",
                                 n_runs=len(js), mean_jaccard=f"{np.mean(js):.3f}", min_jaccard=f"{np.min(js):.3f}",
                                 metric="held_out_seed_in_top_list", value=f"{np.mean(redisc):.3f}", extra=""))
                # 10% edge removal
                js = []
                for _ in range(REPS):
                    keep = rng.random(len(G.edges)) >= 0.10
                    A = G.adj(edges=G.edges[keep]); L = run_method(m, A, seeds); js.append(jac(base[m], L))
                sens.append(dict(seed_set=sname, network=nname, method=m, n_seeds_in_network=len(seeds), perturbation="random_10pct_edges_removed",
                                 n_runs=REPS, mean_jaccard=f"{np.mean(js):.3f}", min_jaccard=f"{np.min(js):.3f}", metric="", value="", extra=""))
                # hubs
                A = G.adj(drop=hubs_rm); L = run_method(m, A, seeds)
                sens.append(dict(seed_set=sname, network=nname, method=m, n_seeds_in_network=len(seeds), perturbation=f"top{HUB_N}_degree_nodes_removed",
                                 n_runs=1, mean_jaccard=f"{jac(base[m], L):.3f}", min_jaccard="", metric="removed_nodes_in_baseline_list",
                                 value=str(len(set(hubs_rm) & set(base[m]))), extra="removed: " + ";".join(G.nodes[i] for i in hubs_rm[:5]) + ";..."))
            # target tables
            fn_set = set(fn_all)
            for m in METHODS:
                for rk, i in enumerate(base[m], 1):
                    t = G.nodes[i]
                    sg = signed.get(t, [0, 0, 0])
                    newrows.append(dict(seed_set=sname, network=nname, method=m, rank=rk, target=t, degree=int(deg[i]),
                        degree_percentile=f"{rank_pct[i]:.3f}", is_hub_top5pct=int(i in hubs_all),
                        also_direct_neighbour=int(i in fn_set), in_engine_main_targets=int(t in eng.get(q, set())),
                        in_engine_reach_3hop_regulators=int(t in reach), loo_frequency=f"{loo_freq[m][i]/max(len(seeds),1):.2f}",
                        new_vs_neighbours_and_engine=int(i not in fn_set and t not in eng.get(q, set()) and t not in reach),
                        catalogue_signed_families=sg[0], catalogue_families_plus=sg[1], catalogue_families_minus=sg[2],
                        catalogue_any_action_rows=anyrows.get(t, 0)))
    cols = ["seed_set", "network", "method", "n_seeds_in_network", "perturbation", "n_runs", "mean_jaccard", "min_jaccard", "metric", "value", "extra"]
    with open(out / "sensitivity.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, cols, delimiter="\t"); w.writeheader(); w.writerows(sens)
    with open(out / "new_targets.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, list(newrows[0]), delimiter="\t"); w.writeheader(); w.writerows(newrows)
    facts["seconds"] = round(time.time() - t0, 1)
    json.dump(facts, open(out / "run_facts.json", "w"), indent=1)
    print("done", facts["seconds"], "s")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""IT9 P2 seed-based generation engine: WWOX-loss seeds -> signed propagation -> compound "compatible action" proposals.

Represents the WWOX-deficient state as a signed seed vector over genes (direction x level; uncertain direction kept as conditional arms),
propagates it backward through the IT7 signed regulatory network (K = 3 hops, damping 0.5 per extra hop, 1/out-degree weights) and scores every
compound family by its signed target actions: Q > 0 means the compound's predicted effect on the seed genes OPPOSES the seed change,
Q < 0 means it MIMICS it ("compatible action", NOT predicted benefit; an unsigned proximity stays a proximity). Exploratory, computational,
not medical advice; proves function and sensitivity of a method, never therapeutic accuracy.

Subcommands (all deterministic; numpy only; `--help` does no work):
  build-actions --catalog PATH --out DIR [--cache DIR]   catalogue -> family_actions.tsv.gz + family_meta.tsv.gz (signed targets per family)
  run      --seeds FILE --actions DIR --label L --out DIR [--universe FILE] [--top N] [--nnull N] [--match total|indeg] [--allow-mixed-levels]
                                                     score a compound universe; writes proposals_L.tsv.gz, contributions_L.tsv, funnel_L.json
  tests    --seeds FILE --actions DIR --label L --out DIR [--decoy FILE] [--nnull N] [--match total|indeg]
                                                     T1-T5 of PRE_REGISTRATION.md (function, sensitivity, identity/leakage, added information, mutations)
  explain  --seeds FILE --actions DIR --family FAM:... [--family ...]   per-seed, per-target decomposition of the score of a family
  selftest                                           small synthetic graph with known answers (also run by test_seed_engine.py)

Seed table (TSV): seed_id, gene, kind(gene|process), members(; list for process), direction(up|down|uncertain), level(0-1],
direction_status(defined|uncertain), readout_level(transcript|protein|activity|phenotype), evidence_class, species, ortholog_map, source_ref, note.
Refused at load: evidence_class in {intervention_response, held_out, card}; non-human species without an ortholog_map; mixed readout levels unless --allow-mixed-levels.

Example, on a declared compound universe (family ids, one per line or a TSV with a family_id column):
  python3 seed_engine.py run --seeds seeds.tsv --actions results --label p3 --out results --universe universe.tsv
"""
import sys

if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

import argparse
import collections
import csv
import gzip
import importlib.util
import json
import math
import os
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
DRUG = HERE.parent
REPO = HERE.parents[4]
DEFAULT_INPUTS = DRUG / "network_comparison_it7_p3_20261029" / "inputs"
DEFAULT_CATALOG = DRUG / "catalog" / "catalog.jsonl.gz"
PILOT_SUBSET = DRUG / "usable_compounds_it7_p2_20261029" / "pilot_subset.tsv"
K, GAMMA = 3, 0.5
SEED0 = 20261030
FIREWALL_CLASSES = {"intervention_response", "held_out", "card"}
EVIDENCE_OK = {"transcript_contrast", "protein_state", "activity_state", "phenotype_state"}
MYELIN_DECOY = ["MBP", "PLP1", "MOG", "MAG", "MOBP", "CNP", "MAL", "UGT8", "MYRF", "SOX10"]  # engineer-assembled decoy, not a P1 set


# ------------------------------------------------------------------------------------------------ small helpers
def read_tsv(path):
    op = gzip.open if str(path).endswith(".gz") else open
    with op(path, "rt", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def rankdata(a):
    a = np.asarray(a, float)
    o = np.argsort(a, kind="mergesort")
    sa = a[o]
    flag = np.concatenate(([True], sa[1:] != sa[:-1]))
    idx = np.flatnonzero(flag)
    cnt = np.diff(np.append(idx, len(a)))
    r = np.empty(len(a))
    r[o] = np.repeat(idx + (cnt - 1) / 2.0, cnt)
    return r


def spearman(x, y):
    rx, ry = rankdata(x), rankdata(y)
    rx -= rx.mean(); ry -= ry.mean()
    d = math.sqrt(float((rx * rx).sum()) * float((ry * ry).sum()))
    return float((rx * ry).sum() / d) if d > 0 else float("nan")


def topk(q, k):
    """indices of the k largest q, ties by index (deterministic)."""
    o = np.lexsort((np.arange(len(q)), -np.asarray(q)))
    return o[:k]


# ------------------------------------------------------------------------------------------------ network
class Graph:
    """Signed directed graph; nodes = graph genes first, then `extras` (target/seed genes without edges)."""

    def __init__(self, edges, extras=()):
        syms = sorted({e[0] for e in edges} | {e[1] for e in edges})
        self.Ng = len(syms)
        ex = [x for x in sorted(set(extras)) if x not in set(syms)]
        self.syms = syms + ex
        self.N = len(self.syms)
        self.idx = {g: i for i, g in enumerate(self.syms)}
        src = np.array([self.idx[e[0]] for e in edges], dtype=np.int64)
        tgt = np.array([self.idx[e[1]] for e in edges], dtype=np.int64)
        sg = np.array([e[2] for e in edges], dtype=np.float64)
        od = np.bincount(src, minlength=self.N).astype(np.float64)
        w = sg / od[src]
        self.edges = edges
        self.src0, self.tgt0, self.sg0 = src, tgt, sg
        self.outdeg = od
        self.indeg = np.bincount(tgt, minlength=self.N).astype(np.float64)
        self._build(src, tgt, w)

    def _build(self, src, tgt, w):
        o = np.argsort(tgt, kind="stable")
        self.f_src, self.f_tgt, self.f_w = src[o], tgt[o], w[o]
        self.f_ut, self.f_starts = np.unique(self.f_tgt, return_index=True)
        o = np.argsort(src, kind="stable")
        self.b_src, self.b_tgt, self.b_w = src[o], tgt[o], w[o]
        self.b_us, self.b_starts = np.unique(self.b_src, return_index=True)

    def with_signs(self, sg):
        """same topology, other signs (weights keep 1/out-degree)."""
        g = object.__new__(Graph)
        g.__dict__.update(self.__dict__)
        w = np.asarray(sg, float) / self.outdeg[self.src0]
        g._build(self.src0, self.tgt0, w)
        return g

    def hop_fwd(self, X):
        c = X[:, self.f_src] * self.f_w
        out = np.zeros_like(X)
        out[:, self.f_ut] = np.add.reduceat(c, self.f_starts, axis=1)
        return out

    def hop_bwd(self, Z):
        c = Z[:, self.b_tgt] * self.b_w
        out = np.zeros_like(Z)
        out[:, self.b_us] = np.add.reduceat(c, self.b_starts, axis=1)
        return out

    def influence_ind(self, S, hops=K, gamma=GAMMA):
        """indirect influence (hops 1..K) of seed rows S (M x N): V = sum_k gamma^(k-1) (hop^T)^k S."""
        V = np.zeros_like(S)
        h = S
        for k in range(1, hops + 1):
            h = self.hop_bwd(h)
            V += (gamma ** (k - 1)) * h
        return V

    def dist_to_set(self, seed_idx, cap=6):
        """directed shortest path length from every node to the nearest seed (cap+1 = unreachable)."""
        radj = collections.defaultdict(list)
        for a, b in zip(self.src0, self.tgt0):
            radj[int(b)].append(int(a))
        d = np.full(self.N, cap + 1, dtype=np.int64)
        frontier = []
        for s in seed_idx:
            d[s] = 0
            frontier.append(int(s))
        k = 0
        while frontier and k < cap:
            k += 1
            nxt = []
            for n in frontier:
                for m in radj.get(n, ()):
                    if d[m] > k:
                        d[m] = k
                        nxt.append(m)
            frontier = nxt
        return d


def read_edges(inputs=DEFAULT_INPUTS):
    """IT7 P3 external network (SIGNOR + CollecTRI via OmniPath), complexes split into members, conflicting duplicates dropped."""
    E = {}
    for fn in ("signor_omnipath_edges.tsv.gz", "collectri_omnipath_edges.tsv.gz"):
        for r in read_tsv(Path(inputs) / fn):
            srcs = r["source_symbol"].split("_") if "_" in r["source_symbol"] else [r["source_symbol"]]
            tgts = r["target_symbol"].split("_") if "_" in r["target_symbol"] else [r["target_symbol"]]
            for s in srcs:
                for t in tgts:
                    if s == t:
                        continue
                    sg = int(r["sign"]); k = (s, t)
                    E[k] = sg if (k not in E or E[k] == sg) else 0
    return sorted((s, t, sg) for (s, t), sg in E.items() if sg != 0)


# ------------------------------------------------------------------------------------------------ seeds
class Seeds:
    """Seed units (one per gene per seed row; a process seed spreads level/sqrt(n) over its members).
    sign: +1/-1 for defined direction, 0 for uncertain (those carry level only)."""

    def __init__(self, units, notes=None):
        self.units = units  # list of dict(unit_id, seed_id, gene, sign, level, status, readout_level, evidence_class)
        self.notes = notes or {}

    def __len__(self):
        return len(self.units)

    @property
    def genes(self):
        return [u["gene"] for u in self.units]

    def vec(self, idx, N, which="defined", scale=1.0):
        """which: defined (sign*level for defined units), uncertain (+level for uncertain units), all_plus (every unit +level)."""
        v = np.zeros(N)
        for u in self.units:
            j = idx.get(u["gene"])
            if j is None:
                continue
            if which == "defined" and u["sign"] != 0:
                v[j] += u["sign"] * u["level"] * scale
            elif which == "uncertain" and u["sign"] == 0:
                v[j] += u["level"] * scale
        return v

    def unit_matrix(self, idx, N, unsigned_uncertain=True):
        """(M x N): unit j's row = sign*level (defined) or +level (uncertain, to be multiplied by +-1 for an arm)."""
        S = np.zeros((len(self.units), N))
        for i, u in enumerate(self.units):
            j = idx.get(u["gene"])
            if j is not None:
                S[i, j] = (u["sign"] if u["sign"] != 0 else 1.0) * u["level"]
        return S


def load_seeds(path, allow_mixed=False, human_only=True):
    rows = read_tsv(path)
    need = {"seed_id", "gene", "direction", "level", "direction_status", "readout_level", "evidence_class", "species"}
    if rows and not need <= set(rows[0]):
        raise SystemExit(f"seed table lacks columns {sorted(need - set(rows[0]))}")
    units, levels = [], set()
    for r in rows:
        cls = (r["evidence_class"] or "").strip()
        if cls in FIREWALL_CLASSES:
            raise SystemExit(f"firewall: seed {r['seed_id']} has evidence_class {cls!r} (intervention response / held-out / card data are never seeds)")
        if cls not in EVIDENCE_OK:
            raise SystemExit(f"seed {r['seed_id']}: evidence_class {cls!r} not in {sorted(EVIDENCE_OK)}")
        sp = (r["species"] or "").strip().lower()
        if sp not in ("human", "homo sapiens") and not (r.get("ortholog_map") or "").strip():
            raise SystemExit(f"seed {r['seed_id']}: species {sp!r} without ortholog_map (identity rule)")
        lvl = float(r["level"])
        if not (0 < lvl <= 1):
            raise SystemExit(f"seed {r['seed_id']}: level {lvl} outside (0,1]")
        d = (r["direction"] or "").strip().lower()
        st = (r["direction_status"] or "").strip().lower()
        sign = {"up": 1, "down": -1}.get(d, 0) if st == "defined" else 0
        if st == "defined" and d not in ("up", "down"):
            raise SystemExit(f"seed {r['seed_id']}: defined status needs direction up|down")
        kind = (r.get("kind") or "gene").strip() or "gene"
        genes = [x.strip().upper() for x in (r.get("members") or "").split(";") if x.strip()] if kind == "process" else [r["gene"].strip().upper()]
        if not genes:
            raise SystemExit(f"seed {r['seed_id']}: no gene")
        w = lvl / math.sqrt(len(genes)) if kind == "process" else lvl
        levels.add(r["readout_level"])
        for g in genes:
            units.append(dict(unit_id=f"{r['seed_id']}:{g}", seed_id=r["seed_id"], gene=g, sign=sign, level=w, status=st,
                              readout_level=r["readout_level"], evidence_class=cls))
    if len(levels) > 1 and not allow_mixed:
        raise SystemExit(f"mixed readout levels {sorted(levels)}: expression, protein and function are not merged; run per level or pass --allow-mixed-levels")
    return Seeds(units)


def seeds_replace(seeds, genes=None, signs=None, drop=None, scale=1.0):
    us = []
    for i, u in enumerate(seeds.units):
        if drop is not None and i in drop:
            continue
        v = dict(u)
        if genes is not None:
            v["gene"] = genes[i]
        if signs is not None and u["sign"] != 0:
            v["sign"] = signs[i]
        v["level"] = u["level"] * scale
        us.append(v)
    return Seeds(us)


# ------------------------------------------------------------------------------------------------ compounds
class Compounds:
    def __init__(self, rows, meta=None, space_idx=None):
        """rows: family_actions rows (family_id, target_symbol, mean_sign, ...)."""
        by = collections.defaultdict(dict)
        self.n_conflict = 0
        for r in rows:
            s = float(r["mean_sign"])
            if abs(s) < 1e-9:
                self.n_conflict += 1
                continue
            by[r["family_id"]][r["target_symbol"].upper()] = (s, r.get("groups", ""), r.get("scopes", ""))
        self.fams = sorted(by)
        self.fidx = {f: i for i, f in enumerate(self.fams)}
        self.targets = [by[f] for f in self.fams]
        self.meta = meta or {}

    def matrix(self, idx):
        fi, ci, va = [], [], []
        for i, t in enumerate(self.targets):
            nrm = math.sqrt(sum(v[0] ** 2 for v in t.values()))
            for g, (s, _, _) in t.items():
                if g in idx:
                    fi.append(i); ci.append(idx[g]); va.append(s / nrm)
        return np.array(fi, np.int64), np.array(ci, np.int64), np.array(va, float)


def score(A, V, F, chunk=128):
    """Q[f, m] = - sum_t A[f, t] V[m, t]; A = (fam_idx, col_idx, val)."""
    fi, ci, va = A
    o = np.argsort(fi, kind="stable")
    fi, ci, va = fi[o], ci[o], va[o]
    uf, starts = np.unique(fi, return_index=True)
    M = V.shape[0]
    Q = np.zeros((F, M))
    for a in range(0, M, chunk):
        sub = V[a:a + chunk]
        c = sub[:, ci] * va
        Q[uf, a:a + chunk] = -np.add.reduceat(c, starts, axis=1).T
    return Q


class Engine:
    def __init__(self, graph, comp, seeds):
        self.g, self.comp, self.seeds = graph, comp, seeds
        self.A = comp.matrix(graph.idx)
        self.F = len(comp.fams)
        self.in_graph = np.zeros(self.F, int)
        for f, c in zip(self.A[0], self.A[1]):
            if c < graph.Ng:
                self.in_graph[f] += 1

    def arms(self, seeds=None):
        """exact arms for a seed set: certain part, uncertain unit contributions, direct/indirect split."""
        seeds = seeds or self.seeds
        g = self.g
        S_def = seeds.vec(g.idx, g.N, "defined")[None, :]
        S_unc = seeds.vec(g.idx, g.N, "uncertain")[None, :]
        out = {}
        for nm, S in (("def", S_def), ("unc", S_unc)):
            out[nm + "_dir"] = score(self.A, S, self.F)[:, 0]
            out[nm + "_ind"] = score(self.A, g.influence_ind(S), self.F)[:, 0]
        # per-unit uncertain contributions (for the exact range)
        idxu = [i for i, u in enumerate(seeds.units) if u["sign"] == 0 and u["gene"] in g.idx]
        if idxu:
            SU = np.zeros((len(idxu), g.N))
            for r, i in enumerate(idxu):
                SU[r, g.idx[seeds.units[i]["gene"]]] = seeds.units[i]["level"]
            C = score(self.A, SU, self.F) + score(self.A, g.influence_ind(SU), self.F)
            out["unc_mass"] = np.abs(C).sum(1)
        else:
            out["unc_mass"] = np.zeros(self.F)
        out["ind"] = out["def_ind"]
        out["dir"] = out["def_dir"]
        out["full"] = out["def_dir"] + out["def_ind"]
        out["full_Uplus"] = out["full"] + out["unc_dir"] + out["unc_ind"]
        out["full_Uminus"] = out["full"] - out["unc_dir"] - out["unc_ind"]
        out["ind_Uplus"] = out["ind"] + out["unc_ind"]
        out["ind_Uminus"] = out["ind"] - out["unc_ind"]
        return out

    def quick(self, seeds):
        """NET-IND and NET-FULL for a seed set with only defined signs (nulls, mutations): returns (ind, dir)."""
        g = self.g
        S = seeds.vec(g.idx, g.N, "defined")[None, :] + seeds.vec(g.idx, g.N, "uncertain")[None, :]
        return score(self.A, g.influence_ind(S), self.F)[:, 0], score(self.A, S, self.F)[:, 0]

    def quick_many(self, S):
        """S: (M x N) full seed vectors -> (ind, dir) each F x M."""
        g = self.g
        ind = np.zeros((self.F, S.shape[0])); dr = np.zeros_like(ind)
        for a in range(0, S.shape[0], 200):
            sub = S[a:a + 200]
            ind[:, a:a + 200] = score(self.A, g.influence_ind(sub), self.F)
            dr[:, a:a + 200] = score(self.A, sub, self.F)
        return ind, dr


# ------------------------------------------------------------------------------------------------ catalogue -> actions
def build_actions(catalog, out, cache=None):
    sys.path.insert(0, str(REPO / "framework/scripts"))
    sys.path.insert(0, str(DRUG / "usable_compounds_it7_p2_20261029"))
    import compound_catalog as cc
    import repurposing_search as rs
    spec = importlib.util.spec_from_file_location("usable_census", DRUG / "usable_compounds_it7_p2_20261029" / "usable_census.py")
    uc = importlib.util.module_from_spec(spec); spec.loader.exec_module(uc)
    entries = cc.load(Path(catalog))
    idx = rs.Index(entries, rs.load_artefacts())
    fam = idx.family
    acts = collections.defaultdict(lambda: collections.defaultdict(lambda: dict(signs=[], groups=set(), scopes=set())))
    anyt = collections.defaultdict(collections.Counter)
    meta = {}
    for e in entries:
        f = fam[e["id"]]
        m = meta.setdefault(f, dict(family_id=f, name="", n_records=0, has_structure_key=0, has_chembl=0, mnet_usable=0))
        m["n_records"] += 1
        ids = e.get("ids") or {}
        if ids.get("skeleton_key"):
            m["has_structure_key"] = 1
        if ids.get("chembl"):
            m["has_chembl"] = 1
        if not m["name"] or "FAM:" + e["id"] == f:
            m["name"] = e.get("name") or m["name"]
        for t in e["targets"]:
            u = uc.row_usability(rs, idx, e, t)
            for sym in [x.strip().upper() for x in (u["symbol"] or "").split(";") if x.strip()]:
                anyt[f][sym] += 1
            if u["stated"] and not u["excluded"] and u["sign"] in ("up", "down") and u["stable"]:
                m["mnet_usable"] = 1
                for sym in [x.strip().upper() for x in (u["symbol"] or "").split(";") if x.strip()]:
                    a = acts[f][sym]
                    a["signs"].append(1.0 if u["sign"] == "up" else -1.0)
                    a["groups"].add(u["group"]); a["scopes"].add(u["scope"])
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    with gzip.open(out / "family_actions.tsv.gz", "wt", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["family_id", "target_symbol", "mean_sign", "n_rows", "groups", "scopes"])
        for f in sorted(acts):
            for sym in sorted(acts[f]):
                a = acts[f][sym]
                w.writerow([f, sym, f"{sum(a['signs']) / len(a['signs']):.4f}", len(a["signs"]), ";".join(sorted(a["groups"])), ";".join(sorted(a["scopes"]))])
    with gzip.open(out / "family_targets_any.tsv.gz", "wt", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["family_id", "target_symbol", "n_rows_any_action"])
        for f in sorted(anyt):
            for sym in sorted(anyt[f]):
                w.writerow([f, sym, anyt[f][sym]])
    with gzip.open(out / "family_meta.tsv.gz", "wt", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        cols = ["family_id", "name", "n_records", "has_structure_key", "has_chembl", "mnet_usable"]
        w.writerow(cols)
        for f in sorted(meta):
            w.writerow([meta[f][c] for c in cols])
    print(f"families {len(meta)}  with signed targets {len(acts)}  rows -> {out}")


def load_actions(adir):
    rows = read_tsv(Path(adir) / "family_actions.tsv.gz")
    meta = {r["family_id"]: r for r in read_tsv(Path(adir) / "family_meta.tsv.gz")}
    return rows, meta


# ------------------------------------------------------------------------------------------------ run
def make_engine(a, seeds_path=None, rows=None, meta=None, restrict=None):
    seeds = load_seeds(seeds_path or a.seeds, allow_mixed=getattr(a, "allow_mixed_levels", False))
    if rows is None:
        rows, meta = load_actions(a.actions)
    if restrict is not None:
        rows = [r for r in rows if r["family_id"] in restrict]
    edges = read_edges()
    extras = {r["target_symbol"].upper() for r in rows} | set(seeds.genes) | set(MYELIN_DECOY)
    g = Graph(edges, extras)
    comp = Compounds(rows, meta)
    return Engine(g, comp, seeds), rows, meta


def call_label(q, mass, tol=1e-9):
    if abs(q) <= tol:
        return "none"
    base = "opposes" if q > 0 else "mimics"
    return base if abs(q) > mass else base + "_conditional_on_uncertain_seeds"


def seed_contrib_table(eng, fam_ids, seeds=None):
    """per family, per seed unit: signed contribution (hop 0 / hops 1-3), and the target carrying most of it."""
    seeds = seeds or eng.seeds
    g = eng.g
    S = seeds.unit_matrix(g.idx, g.N)
    V0 = S
    Vi = g.influence_ind(S)
    rows = []
    tcache = {}
    for f in fam_ids:
        i = eng.comp.fidx[f]
        tg = [(gene, v[0]) for gene, v in eng.comp.targets[i].items()]
        nrm = math.sqrt(sum(s * s for _, s in tg))
        for ui, u in enumerate(seeds.units):
            sgn = 1.0
            best0 = bestk = None; c0 = ck = 0.0
            for gene, s in tg:
                j = g.idx.get(gene)
                if j is None:
                    continue
                a = s / nrm
                x0, xk = -a * V0[ui, j] * sgn, -a * Vi[ui, j] * sgn
                c0 += x0; ck += xk
                if best0 is None or abs(x0) > abs(best0[1]):
                    best0 = (gene, x0)
                if bestk is None or abs(xk) > abs(bestk[1]):
                    bestk = (gene, xk)
            if c0 == 0 and ck == 0:
                continue
            note = "uncertain_direction(+arm shown)" if u["sign"] == 0 else "defined"
            rows.append(dict(family_id=f, unit_id=u["unit_id"], seed_id=u["seed_id"], gene=u["gene"], seed_direction={1: "up", -1: "down", 0: "uncertain"}[u["sign"]],
                             level=f"{u['level']:.4f}", readout_level=u["readout_level"], direction_status=note, contrib_hop0=f"{c0:.6g}", contrib_hops1to3=f"{ck:.6g}",
                             contrib_total=f"{c0 + ck:.6g}", main_target_hop0=best0[0] if best0 and best0[1] else "", main_target_hops1to3=bestk[0] if bestk and bestk[1] else ""))
    return rows


def load_any_targets(adir):
    f = Path(adir) / "family_targets_any.tsv.gz"
    by = collections.defaultdict(set)
    if f.exists():
        for r in read_tsv(f):
            by[r["family_id"]].add(r["target_symbol"].upper())
    return by


def cmd_run(a):
    eng, rows, meta = make_engine(a)
    g, comp = eng.g, eng.comp
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    arms = eng.arms()
    mom = null_moments(eng, eng.seeds, a.nnull, SEED0 + 11, a.match)
    zi_p, zi_m, zi_r = arm_z(arms, mom, "ind")
    zf_p, zf_m, zf_r = arm_z(arms, mom, "full")
    # funnel
    allfam = len(meta)
    resolved = sum(1 for m in meta.values() if m["has_structure_key"] == "1" or m["has_chembl"] == "1")
    usable_meta = sum(1 for m in meta.values() if m["mnet_usable"] == "1")
    universe = None
    if a.universe:
        lines = read_tsv(a.universe) if a.universe.endswith((".tsv", ".tsv.gz")) else None
        universe = {r["family_id"] for r in lines} if lines is not None else {x.strip() for x in open(a.universe) if x.strip()}
    examined = (eng.in_graph > 0)
    examined_u = examined.copy()
    if universe is not None:
        for f, i in comp.fidx.items():
            if f not in universe:
                examined_u[i] = False
    anyt = load_any_targets(a.actions)
    seedset = set(eng.seeds.genes)
    direct_any = np.array([bool(anyt.get(f, set()) & seedset) for f in comp.fams])
    funnel = dict(catalogued_families=allfam, resolved_identity_families=resolved, mnet_usable_families=usable_meta,
                  mnet_usable_with_a_gene_symbol=len(comp.fams), mnet_usable_with_target_in_graph=int(examined.sum()),
                  declared_universe_families=(len(universe) if universe is not None else None),
                  declared_universe_in_mnet_usable_with_symbol=(sum(1 for f in universe if f in comp.fidx) if universe is not None else None),
                  examined=int(examined_u.sum()), examined_with_nonzero_net_full=int(((np.abs(arms["full"]) > 1e-12) & examined_u).sum()),
                  examined_with_nonzero_in_any_arm=int(((np.abs(arms["full"]) + np.abs(arms["full_Uplus"]) + np.abs(arms["full_Uminus"]) > 1e-12) & examined_u).sum()),
                  examined_hit_a_seed_gene_with_any_action=int((direct_any & examined_u).sum()),
                  conflicting_target_actions_dropped=comp.n_conflict,
                  seed_units=len(eng.seeds), seed_units_in_graph=sum(1 for u in eng.seeds.units if g.idx.get(u["gene"], 10**9) < g.Ng),
                  null_sets_for_z=a.nnull, z_sd_floor_full_Uplus=mom["p"]["full"][2],
                  units="families (catalogue records joined by parent/InChIKey block; NOT distinct drugs)")
    seed_nodes = [g.idx[x] for x in eng.seeds.genes if x in g.idx]
    dist = g.dist_to_set(seed_nodes)
    prox_mean, prox_z, prox_min = proximity(eng, dist, a.nprox)
    regs = {g.syms[s] for s, t in zip(g.src0, g.tgt0) if g.syms[t] == "WWOX"}
    inter = np.array([bool(regs & set(t)) for t in comp.targets])
    order = np.lexsort((np.arange(eng.F), -arms["full"], -zf_r, -zi_r))
    cols = ["family_id", "name", "n_signed_targets", "n_targets_in_graph", "Z_full_robust", "Z_ind_robust", "Q_net_full", "Q_net_ind", "Q_direct", "compatible_action",
            "Q_Uplus", "Q_Uminus", "Z_full_Uplus", "Z_full_Uminus", "uncertain_seed_mass", "direct_hit_any_action_on_seed_gene", "wwox_regulator_target",
            "prox_mean_dist", "prox_z_degree_matched", "prox_min_dist"]
    tmpl = "{:.6g}".format
    with gzip.open(out / f"proposals_{a.label}.tsv.gz", "wt", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(cols)
        keep = [i for i in order if examined_u[i] and (abs(arms["full"][i]) > 1e-12 or abs(arms["full_Uplus"][i]) > 1e-12 or abs(arms["full_Uminus"][i]) > 1e-12)]
        for i in keep:
            f = comp.fams[i]
            w.writerow([f, meta.get(f, {}).get("name", ""), len(comp.targets[i]), int(eng.in_graph[i]), tmpl(zf_r[i]), tmpl(zi_r[i]), tmpl(arms["full"][i]), tmpl(arms["ind"][i]),
                        tmpl(arms["dir"][i]), call_label(arms["full"][i], arms["unc_mass"][i]), tmpl(arms["full_Uplus"][i]), tmpl(arms["full_Uminus"][i]),
                        tmpl(zf_p[i]), tmpl(zf_m[i]), tmpl(arms["unc_mass"][i]), int(direct_any[i]), int(inter[i]),
                        tmpl(prox_mean[i]) if np.isfinite(prox_mean[i]) else "", tmpl(prox_z[i]) if np.isfinite(prox_z[i]) else "", prox_min[i] if prox_min[i] >= 0 else ""])
        top_fams = [comp.fams[i] for i in keep[:a.top]] + [comp.fams[i] for i in keep[-a.top:]]
        top_fams += [comp.fams[i] for i in keep if direct_any[i]][:a.top]
    ct = seed_contrib_table(eng, list(dict.fromkeys(top_fams)))
    with open(out / f"contributions_{a.label}.tsv", "w", encoding="utf-8", newline="") as fh:
        cols2 = ["family_id", "unit_id", "seed_id", "gene", "seed_direction", "level", "readout_level", "direction_status", "contrib_hop0", "contrib_hops1to3", "contrib_total",
                 "main_target_hop0", "main_target_hops1to3"]
        w = csv.DictWriter(fh, fieldnames=cols2, delimiter="\t", lineterminator="\n")
        w.writeheader()
        for r in ct:
            w.writerow(r)
    (out / f"funnel_{a.label}.json").write_text(json.dumps(funnel, indent=1) + "\n")
    print(json.dumps(funnel, indent=1))
    print(f"proposals_{a.label}.tsv.gz rows: {len(keep)}; contributions rows: {len(ct)}")
    return 0


def proximity(eng, dist, nnull, seed=SEED0 + 7):
    g, comp = eng.g, eng.comp
    deg = (g.indeg + g.outdeg)[:g.Ng]
    bins = np.digitize(deg, np.quantile(deg, np.linspace(0.1, 0.9, 9)))
    pools = [np.flatnonzero(bins == b) for b in range(10)]
    rng = np.random.default_rng(seed)
    F = eng.F
    pm = np.full(F, np.nan); pz = np.full(F, np.nan); pmin = np.full(F, -1)
    dd = dist[:g.Ng].astype(float)
    for i, t in enumerate(comp.targets):
        nodes = [g.idx[x] for x in t if x in g.idx and g.idx[x] < g.Ng]
        if not nodes:
            continue
        d = dd[nodes]
        pm[i] = d.mean(); pmin[i] = int(d.min())
        if len(nodes) > 400:
            nodes = list(rng.choice(nodes, 400, replace=False))
        b = bins[nodes]
        draws = np.empty((nnull, len(nodes)))
        for j, bb in enumerate(b):
            draws[:, j] = dd[pools[bb][rng.integers(0, len(pools[bb]), nnull)]]
        mu, sd = draws.mean(1).mean(), draws.mean(1).std()
        pz[i] = (pm[i] - mu) / sd if sd > 0 else 0.0
    return pm, pz, pmin


# ------------------------------------------------------------------------------------------------ tests
def match_bins(g, match):
    if match == "indeg":
        deg = g.indeg[:g.Ng]
    else:
        deg = (g.indeg + g.outdeg)[:g.Ng]
    edges = np.unique(np.quantile(deg, np.linspace(0.1, 0.9, 9)))
    bins = np.digitize(deg, edges)
    return bins, [np.flatnonzero(bins == b) for b in range(len(edges) + 1)]


def degree_matched_sets(eng, seeds, n, rng, match="total"):
    """n random seed sets: each seed gene replaced by a random gene of the same degree decile (match = total in+out degree [registered] or in-degree [M2]);
    real seed genes excluded; the signed levels are kept. Returns (S_plus, S_minus): uncertain-direction units enter with + (resp. -) their level."""
    g = eng.g
    bins, pools = match_bins(g, match)
    real = {g.idx[x] for x in seeds.genes if x in g.idx}
    extras = np.arange(g.Ng, g.N)
    Sp = np.zeros((n, g.N)); Sm = np.zeros((n, g.N))
    for k in range(n):
        used = set(real)
        for u in seeds.units:
            j = g.idx.get(u["gene"])
            pool = pools[bins[j]] if (j is not None and j < g.Ng) else extras
            while True:
                c = int(pool[rng.integers(0, len(pool))])
                if c not in used:
                    used.add(c); break
            Sp[k, c] += (u["sign"] if u["sign"] != 0 else 1.0) * u["level"]
            Sm[k, c] += (u["sign"] if u["sign"] != 0 else -1.0) * u["level"]
    return Sp, Sm


def null_moments(eng, seeds, n, seed, match="total"):
    """per-family mean and SD of Q (ind and full) under n degree-matched random seed sets, for the U+ and U- arms."""
    rng = np.random.default_rng(seed)
    Sp, Sm = degree_matched_sets(eng, seeds, n, rng, match)
    mom = {}
    for nm, S in (("p", Sp), ("m", Sm)):
        ind, dr = eng.quick_many(S)
        full = ind + dr
        mom[nm] = dict(ind=(ind.mean(1), ind.std(1)), full=(full.mean(1), full.std(1)))
    for nm in ("p", "m"):
        for t in ("ind", "full"):
            sd = mom[nm][t][1]
            pos = sd[sd > 0]
            floor = float(np.percentile(pos, 5)) if len(pos) else 1.0
            mom[nm][t] = (mom[nm][t][0], np.maximum(sd, floor), floor)
    return mom


def zscore(q, mu, sd):
    return (q - mu) / sd


def z_robust(zp, zm):
    out = np.zeros_like(zp)
    both_pos = (zp > 0) & (zm > 0)
    both_neg = (zp < 0) & (zm < 0)
    out[both_pos] = np.minimum(zp, zm)[both_pos]
    out[both_neg] = np.maximum(zp, zm)[both_neg]
    return out


def arm_z(arms, mom, kind):
    qp = arms[kind + "_Uplus"] if kind == "ind" else arms["full_Uplus"]
    qm = arms[kind + "_Uminus"] if kind == "ind" else arms["full_Uminus"]
    zp = zscore(qp, mom["p"][kind][0], mom["p"][kind][1])
    zm = zscore(qm, mom["m"][kind][0], mom["m"][kind][1])
    return zp, zm, z_robust(zp, zm)


def cmd_tests(a):
    eng, rows, meta = make_engine(a)
    g, comp, seeds = eng.g, eng.comp, eng.seeds
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    res = dict(label=a.label, seeds=str(a.seeds), n_seed_units=len(seeds), n_defined=sum(1 for u in seeds.units if u["sign"] != 0),
               n_uncertain=sum(1 for u in seeds.units if u["sign"] == 0))
    examined = eng.in_graph > 0
    E = np.flatnonzero(examined)
    NN = a.nnull
    res["examined_families"] = int(len(E))
    arms = eng.arms()
    real_ind, real_dir, real_full = arms["ind"], arms["dir"], arms["full"]
    defd = Seeds([u for u in seeds.units if u["sign"] != 0])
    i1, d1 = eng.quick(defd)
    # ---------------- T1
    t1 = {}
    z_ind, z_dir = eng.quick(Seeds([]))
    t1["a_zero_seeds_max_abs_Q"] = float(max(np.abs(z_ind).max(), np.abs(z_dir).max()))
    i2, d2 = eng.quick(seeds_replace(defd, scale=2.5))
    t1["b_scale_max_abs_err"] = float(max(np.abs(i2 - 2.5 * i1).max(), np.abs(d2 - 2.5 * d1).max()))
    S = defd.unit_matrix(g.idx, g.N)
    Cu = score(eng.A, S, eng.F) + score(eng.A, g.influence_ind(S), eng.F)
    t1["c_decomposition_max_abs_err"] = float(np.abs(Cu.sum(1) - (i1 + d1)).max()) if len(defd) else 0.0
    inert, moved = [], 0
    base = i1 + d1
    for k, u in enumerate(defd.units):
        ik, dk = eng.quick(seeds_replace(defd, drop={k}))
        if np.abs((ik + dk) - base).max() > 1e-6:
            moved += 1
        else:
            inert.append(u["unit_id"])
    allunits_inert = []
    for k, u in enumerate(seeds.units):
        if np.abs(sum(eng.quick(seeds_replace(seeds, drop={k}))) - sum(eng.quick(seeds))).max() <= 1e-6:
            allunits_inert.append(u["unit_id"])
    t1["d_defined_seeds_with_effect"] = moved
    t1["d_inert_defined_seeds"] = inert
    t1["d_inert_units_any_direction"] = allunits_inert
    t1["PASS"] = bool(t1["a_zero_seeds_max_abs_Q"] == 0 and t1["b_scale_max_abs_err"] < 1e-9 and t1["c_decomposition_max_abs_err"] < 1e-9 and (moved > 0 or len(defd) == 0))
    res["T1"] = t1
    # ---------------- T2 (nulls B, independent of the nulls used for the Z moments)
    rngB = np.random.default_rng(SEED0 + 1)
    Sp, Sm = degree_matched_sets(eng, seeds, NN, rngB, a.match)
    S_real = (seeds.vec(g.idx, g.N, "defined") + seeds.vec(g.idx, g.N, "uncertain"))[None, :]
    ri, rd = eng.quick_many(S_real)
    real_q = ri[:, 0] + rd[:, 0]
    ni, nd = eng.quick_many(Sp)
    nq = ni + nd
    def rank_stats(vreal, vnull):
        rr = rankdata(vreal[E]); rr -= rr.mean()
        rhos = np.empty(NN); ov = np.empty(NN)
        top_real = set(E[topk(vreal[E], 100)].tolist())
        for k in range(NN):
            rk = rankdata(vnull[E, k]); rk -= rk.mean()
            den = math.sqrt(float((rr * rr).sum()) * float((rk * rk).sum()))
            rhos[k] = float((rr * rk).sum() / den) if den > 0 else float("nan")
            ov[k] = len(top_real & set(E[topk(vnull[E, k], 100)].tolist()))
        return rhos, ov
    rhos, ov100 = rank_stats(real_q, nq)
    mu, sd = nq.mean(1), nq.std(1)
    zc = np.where(sd > 0, (real_q - mu) / np.where(sd > 0, sd, 1), 0.0)
    t2 = dict(a_n_null=NN, a_spearman_real_vs_null_median=float(np.nanmedian(rhos)), a_spearman_p5_p95=[float(np.nanpercentile(rhos, 5)), float(np.nanpercentile(rhos, 95))],
              a_top100_overlap_median=float(np.median(ov100)), a_top100_overlap_p5_p95=[float(np.percentile(ov100, 5)), float(np.percentile(ov100, 95))],
              a_effect_size_1_minus_rho_median=float(1 - np.nanmedian(rhos)),
              a_families_abs_z_gt3=int((np.abs(zc[E]) > 3).sum()), a_families_nonzero=int((np.abs(real_q[E]) > 1e-12).sum()))
    # NET-Z arm (A1.1): moments from nulls A (500 sets), evaluated against nulls B
    momA = null_moments(eng, seeds, 500, SEED0 + 11, a.match)
    zp = zscore(arms["full_Uplus"], momA["p"]["full"][0], momA["p"]["full"][1])
    zB = (nq - momA["p"]["full"][0][:, None]) / momA["p"]["full"][1][:, None]
    rz, ovz = rank_stats(zp, zB)
    t2["z_spearman_real_vs_null_median"] = float(np.nanmedian(rz)); t2["z_top100_overlap_median"] = float(np.median(ovz))
    t2["z_top100_overlap_p5_p95"] = [float(np.percentile(ovz, 5)), float(np.percentile(ovz, 95))]
    # b: sign shuffle among defined seeds
    dfi = [i for i, u in enumerate(seeds.units) if u["sign"] != 0]
    if len(dfi) >= 4:
        rng2 = np.random.default_rng(SEED0 + 2)
        signs0 = np.array([seeds.units[i]["sign"] for i in dfi])
        SS = np.zeros((NN, g.N))
        for k in range(NN):
            p = rng2.permutation(len(dfi))
            for pos, i in enumerate(dfi):
                j = g.idx.get(seeds.units[i]["gene"])
                if j is not None:
                    SS[k, j] += signs0[p[pos]] * seeds.units[i]["level"]
        SS += seeds.vec(g.idx, g.N, "uncertain")[None, :]
        si, sdr = eng.quick_many(SS)
        sq = si + sdr
        rho_s = np.array([spearman(real_q[E], sq[E, k]) for k in range(NN)])
        t2["b_sign_shuffle_median_spearman"] = float(np.nanmedian(rho_s))
        t2["b_sign_shuffle_p5_p95"] = [float(np.nanpercentile(rho_s, 5)), float(np.nanpercentile(rho_s, 95))]
        t2["b_sign_shuffle_identical_to_real"] = int((np.abs(sq - real_q[:, None]).max(0) < 1e-12).sum())
        n_pos, n_neg = int((signs0 > 0).sum()), int((signs0 < 0).sum())
        t2["b_defined_seed_signs_up_down"] = [n_pos, n_neg]
        if min(n_pos, n_neg) >= 1:
            mino = [i for i in dfi if seeds.units[i]["sign"] == (1 if n_pos < n_neg else -1)]
            sg = [u["sign"] for u in seeds.units]
            for i in mino:
                sg[i] = -sg[i]
            fi_, fd_ = eng.quick(seeds_replace(seeds, signs=sg))
            t2["b_flip_minority_sign_spearman_with_real"] = spearman(real_q[E], (fi_ + fd_)[E])
            t2["b_flip_minority_top100_overlap"] = len(set(E[topk(real_q[E], 100)].tolist()) & set(E[topk((fi_ + fd_)[E], 100)].tolist()))
    else:
        t2["b_sign_shuffle_median_spearman"] = None
        t2["b_note"] = "fewer than 4 defined-direction seeds: not testable"
    if a.decoy:
        dseeds = load_seeds(a.decoy)
    else:
        dseeds = Seeds([dict(unit_id=f"decoy:{x}", seed_id="decoy", gene=x, sign=-1, level=1.0, status="defined", readout_level="transcript", evidence_class="transcript_contrast") for x in MYELIN_DECOY])
    dq = sum(eng.quick(dseeds))
    top_real = set(E[topk(real_q[E], 100)].tolist())
    t2["c_decoy_n_genes"] = len(dseeds); t2["c_decoy_genes_in_graph"] = sum(1 for x in dseeds.genes if x in g.idx and g.idx[x] < g.Ng)
    t2["c_decoy_spearman_with_real"] = spearman(real_q[E], dq[E])
    t2["c_decoy_top100_overlap_with_real"] = len(top_real & set(E[topk(dq[E], 100)].tolist()))
    crit = [t2["a_spearman_real_vs_null_median"] <= 0.50, t2["a_top100_overlap_median"] <= 20,
            (t2["b_sign_shuffle_median_spearman"] is None) or t2["b_sign_shuffle_median_spearman"] <= 0.80, abs(t2["c_decoy_spearman_with_real"]) <= 0.50]
    t2["criteria_met_a_rho_a_top100_b_shuffle_c_decoy"] = [bool(x) for x in crit]
    t2["PASS"] = bool(all(crit))
    t2["z_arm_criteria_met_rho_top100"] = [bool(t2["z_spearman_real_vs_null_median"] <= 0.50), bool(t2["z_top100_overlap_median"] <= 20)]
    res["T2"] = t2
    # ---------------- T3
    t3 = {}
    t3["a_firewall"] = "seed classes checked at load (evidence_class in %s); none refused" % sorted(EVIDENCE_OK)
    probes_names = {r["family_id"]: r["name"] for r in read_tsv(PILOT_SUBSET) if r["card_ids"] not in ("none", "")}
    namehit = [f for f, n in probes_names.items() if n and n.upper() in set(seeds.genes)]
    t3["a_seed_gene_equals_probe_name"] = namehit
    t3["b_seed_units_total"] = len(seeds); t3["b_seed_units_in_graph"] = sum(1 for x in seeds.genes if x in g.idx and g.idx[x] < g.Ng)
    t3["b_seed_genes_missing_from_graph"] = sorted({x for x in seeds.genes if not (x in g.idx and g.idx[x] < g.Ng)})
    tsyms = {s for t in comp.targets for s in t}
    t3["b_distinct_signed_target_symbols"] = len(tsyms)
    t3["b_target_symbols_in_graph"] = sum(1 for s in tsyms if s in g.idx and g.idx[s] < g.Ng)
    t3["b_mnet_usable_families_without_gene_symbol"] = sum(1 for m in meta.values() if m["mnet_usable"] == "1") - len(comp.fams)
    allin = np.array([all((s in g.idx and g.idx[s] < g.Ng) for s in t) for t in comp.targets])
    R = np.flatnonzero(allin & examined)
    t3["b_restricted_universe_families"] = int(len(R))
    keepf = {comp.fams[i] for i in R}
    eng_r, _, _ = make_engine(a, rows=rows, meta=meta, restrict=keepf)
    rq = sum(eng_r.quick(seeds))
    posr = {f: i for i, f in enumerate(eng_r.comp.fams)}
    fl = [f for f in keepf if f in posr]
    t3["b_restricted_vs_all_spearman"] = spearman(np.array([real_q[comp.fidx[f]] for f in fl]), np.array([rq[posr[f]] for f in fl]))
    t3["b_restricted_check_note"] = "near-tautological by construction (a family whose every target is in the graph has the same score in any engine); the informative diagnostics are the next lines"
    # A1.3 (i) norm over in-graph targets only
    rows_ing = [r for r in rows if r["target_symbol"].upper() in g.idx and g.idx[r["target_symbol"].upper()] < g.Ng]
    e_ing = Engine(g, Compounds(rows_ing), seeds)
    q_ing = sum(e_ing.quick(seeds))
    sh = [f for f in e_ing.comp.fams if f in comp.fidx and examined[comp.fidx[f]]]
    t3["b_norm_all_targets_vs_ingraph_only_spearman"] = spearman(np.array([real_q[comp.fidx[f]] for f in sh]), np.array([q_ing[e_ing.comp.fidx[f]] for f in sh]))
    for nm, pred in (("chembl_only", lambda grp: grp == "ChEMBL"), ("nonchembl_only", lambda grp: grp != "ChEMBL")):
        sub = [r for r in rows if all(pred(x) for x in r["groups"].split(";"))]
        if sub:
            e2 = Engine(g, Compounds(sub), seeds)
            q2 = sum(e2.quick(seeds))
            shared = [f for f in e2.comp.fams if f in comp.fidx]
            t3[f"b_rows_{nm}_families"] = len(e2.comp.fams)
            t3[f"b_rows_{nm}_spearman_with_all_rows"] = spearman(np.array([q2[e2.comp.fidx[f]] for f in shared]), np.array([real_q[comp.fidx[f]] for f in shared]))
    unm = collections.Counter(s for t in comp.targets for s in t if not (s in g.idx and g.idx[s] < g.Ng))
    with open(out / f"unmapped_targets_{a.label}.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["target_symbol_not_in_graph", "n_families"])
        for sym, c in unm.most_common():
            w.writerow([sym, c])
    # leakage probes (defined-only arm and both conditional arms; mid-rank percentile)
    def pct(q, i):
        v = q[E]
        return float(((v < q[i]).sum() + 0.5 * (v == q[i]).sum()) / len(v))
    probes = []
    for f, nm in sorted(probes_names.items()):
        if f not in comp.fidx or not examined[comp.fidx[f]]:
            probes.append(dict(family_id=f, name=nm, status="not_examined (no signed target with a gene symbol in the graph)"))
            continue
        i = comp.fidx[f]
        own = sorted(x for x in comp.targets[i] if x in set(seeds.genes))
        ownidx = {k for k, u in enumerate(seeds.units) if u["gene"] in own}
        a_no = eng.arms(seeds_replace(seeds, drop=ownidx)) if ownidx else arms
        dnm = abs(arms["dir"][i]) + abs(arms["ind"][i])
        row = dict(family_id=f, name=nm, status="examined", Q_defined=float(arms["full"][i]), Q_Uplus=float(arms["full_Uplus"][i]), Q_Uminus=float(arms["full_Uminus"][i]),
                   percentile_defined_arm=pct(arms["full"], i), percentile_Uplus=pct(arms["full_Uplus"], i), percentile_Uminus=pct(arms["full_Uminus"], i),
                   own_target_seeds=own, hop0_share_of_abs_Q_defined=float(abs(arms["dir"][i]) / dnm) if dnm else 0.0)
        if ownidx:
            row.update(percentile_defined_after_leave_own_target_out=pct(a_no["full"], i), percentile_Uplus_after=pct(a_no["full_Uplus"], i), percentile_Uminus_after=pct(a_no["full_Uminus"], i))
            drop = max(row["percentile_defined_arm"] - row["percentile_defined_after_leave_own_target_out"], row["percentile_Uplus"] - row["percentile_Uplus_after"],
                       row["percentile_Uminus"] - row["percentile_Uminus_after"])
            row["flag"] = "RECOVERED_ONLY_VIA_OWN_TARGET" if drop > 0.20 else ""
        else:
            row["flag"] = ""
        probes.append(row)
    t3["c_probes"] = probes
    t3["c_probes_examined"] = sum(1 for p in probes if p["status"] == "examined")
    t3["c_probes_with_own_target_seed"] = sum(1 for p in probes if p.get("own_target_seeds"))
    t3["c_probes_flagged"] = sum(1 for p in probes if p.get("flag"))
    t3["PASS_identity"] = bool(t3["b_restricted_vs_all_spearman"] >= 0.90 and not namehit)
    res["T3"] = t3
    # ---------------- T4
    t4 = {}
    anyt = load_any_targets(a.actions)
    seedset = set(seeds.genes)
    direct_any = np.array([bool(anyt.get(f, set()) & seedset) for f in comp.fams])
    ref_dir = real_dir
    t4["spearman_NETIND_vs_DIRECT_examined"] = spearman(real_ind[E], ref_dir[E])
    t4["spearman_NETFULL_vs_DIRECT_examined"] = spearman(real_full[E], ref_dir[E])
    nz = E[np.abs(ref_dir[E]) > 1e-12]
    t4["n_direct_signed_nonzero_families"] = int(len(nz))
    t4["n_direct_any_action_families"] = int(direct_any[E].sum())
    t4["n_direct_any_action_that_also_have_nonzero_netind"] = int((direct_any[E] & (np.abs(real_ind[E]) > 1e-12)).sum())
    ti = E[topk(real_ind[E], 100)]
    t4["top50_overlap_NETIND_DIRECT"] = len(set(E[topk(real_ind[E], 50)].tolist()) & set(E[topk(ref_dir[E], 50)].tolist()))
    t4["top100_overlap_NETIND_DIRECT"] = len(set(ti.tolist()) & set(E[topk(ref_dir[E], 100)].tolist()))
    regs = {g.syms[s] for s, t in zip(g.src0, g.tgt0) if g.syms[t] == "WWOX"}
    inter = np.array([bool(regs & set(t)) for t in comp.targets])
    zI = zscore(arms["ind_Uplus"], momA["p"]["ind"][0], momA["p"]["ind"][1])
    zIr = arm_z(arms, momA, "ind")[2]
    def newcount(top, zz):
        new = [i for i in top if abs(ref_dir[i]) <= 1e-12 and not direct_any[i] and not inter[i] and real_ind[i] > 0]
        spec = [i for i in new if zz[i] > 3]
        return new, spec
    new, spec = newcount(ti, zIr)
    # registered raw-Q list, specificity by per-compound z against the independent nulls B (indirect part)
    muB, sdB = ni.mean(1), ni.std(1)
    zB_ind = np.where(sdB > 0, (real_ind - muB) / np.where(sdB > 0, sdB, 1), 0.0)
    new_rawq, spec_rawq = newcount(ti, zB_ind)
    t4.update(raw_Q_top100=dict(n_new=len(new_rawq), n_new_and_seed_specific_z_gt3=len(spec_rawq)))
    t4["raw_Q_outcome"] = "ADDS" if (len(new_rawq) >= 50 and len(spec_rawq) >= 25) else ("NONE" if len(spec_rawq) < 10 else "LIMITED")
    tz = E[topk(zIr[E], 100)]
    newz, specz = newcount(tz, zIr)
    t4["Z_top100"] = dict(n_new=len(newz), n_new_and_seed_specific_z_gt3=len(specz), n_with_positive_Z=int((zIr[tz] > 0).sum()))
    t4["Z_outcome"] = "ADDS" if (len(newz) >= 50 and len(specz) >= 25) else ("NONE" if len(specz) < 10 else "LIMITED")
    t4["Z_top100_overlap_with_raw_Q_top100"] = len(set(tz.tolist()) & set(ti.tolist()))
    t4["wwox_regulators_in_network"] = sorted(regs)
    t4["n_families_with_regulator_target"] = int(inter.sum())
    t4["note"] = "a top-k list of a method that fails T2 is not seed-specific whatever T4 says" if not t2["PASS"] else ""
    res["T4"] = t4
    # ---------------- T5
    t5 = {}
    zi, zd = eng.quick(Seeds([]))
    t5["a_empty_seeds_equal_zero_baseline_max_abs"] = float(max(np.abs(zi).max(), np.abs(zd).max()))
    flipi, flipd = eng.quick(seeds_replace(defd, signs=[-u["sign"] for u in defd.units]))
    t5["b_flip_all_max_abs_err"] = float(max(np.abs(flipi + i1).max(), np.abs(flipd + d1).max()))
    t5["b_flip_all_spearman_with_real"] = spearman((i1 + d1)[E], (flipi + flipd)[E])
    t5["b_flip_all_top100_overlap_real_vs_flipped"] = len(set(E[topk((i1 + d1)[E], 100)].tolist()) & set(E[topk((flipi + flipd)[E], 100)].tolist()))
    errs, sets_ok = [], True
    for k, u in enumerate(defd.units[:min(len(defd), 8)]):
        sg = [x["sign"] for x in defd.units]; sg[k] = -sg[k]
        fi, fd = eng.quick(seeds_replace(defd, signs=sg))
        S1 = np.zeros((1, g.N))
        if u["gene"] in g.idx:
            S1[0, g.idx[u["gene"]]] = u["sign"] * u["level"]
        contrib = score(eng.A, S1, eng.F)[:, 0] + score(eng.A, g.influence_ind(S1), eng.F)[:, 0]
        errs.append(float(np.abs((fi + fd) - ((i1 + d1) - 2 * contrib)).max()))
        changed = np.abs((fi + fd) - (i1 + d1)) > 1e-12
        sets_ok = sets_ok and (set(np.flatnonzero(changed).tolist()) == set(np.flatnonzero(np.abs(contrib) > 1e-12).tolist()))
    t5["c_one_sign_flip_max_abs_err"] = max(errs) if errs else 0.0
    t5["c_changed_set_equals_influenced_set"] = bool(sets_ok)
    if len(seeds) > len(defd):
        up_, um_ = arms["full_Uplus"], arms["full_Uminus"]
        t5["d_arm_difference_max_abs_err"] = float(np.abs((up_ - um_) - 2 * (arms["unc_dir"] + arms["unc_ind"])).max())
        t5["d_range_brackets_arms"] = bool(np.all(np.minimum(up_, um_) >= arms["full"] - arms["unc_mass"] - 1e-9) and np.all(np.maximum(up_, um_) <= arms["full"] + arms["unc_mass"] + 1e-9))
    else:
        t5["d_note"] = "no uncertain-direction seeds in this set"
    rng3 = np.random.default_rng(SEED0 + 3)
    rho_n = []
    S0 = (seeds.vec(g.idx, g.N, "defined") + seeds.vec(g.idx, g.N, "uncertain"))[None, :]
    for k in range(min(200, NN)):
        gm = g.with_signs(rng3.choice([-1.0, 1.0], len(g.sg0)))
        qm = score(eng.A, gm.influence_ind(S0), eng.F)[:, 0] + score(eng.A, S0, eng.F)[:, 0]
        rho_n.append(spearman(real_q[E], qm[E]))
    t5["e_network_sign_randomized_median_spearman"] = float(np.nanmedian(rho_n)); t5["e_n"] = len(rho_n)
    if len(defd):
        us = [dict(u) for u in defd.units]; us[0] = dict(us[0], level=0.0)
        t5["f_zero_level_equals_removal_max_abs"] = float(np.abs(sum(eng.quick(Seeds(us))) - sum(eng.quick(seeds_replace(defd, drop={0})))).max())
    t5["PASS"] = bool(t5["a_empty_seeds_equal_zero_baseline_max_abs"] == 0 and t5["b_flip_all_max_abs_err"] < 1e-9 and t5["c_one_sign_flip_max_abs_err"] < 1e-9
                      and t5["c_changed_set_equals_influenced_set"] and t5.get("d_arm_difference_max_abs_err", 0) < 1e-9 and t5.get("d_range_brackets_arms", True)
                      and t5["e_network_sign_randomized_median_spearman"] <= 0.9 and t5.get("f_zero_level_equals_removal_max_abs", 0) < 1e-12)
    ones = np.ones((1, g.N)); ones[0, g.Ng:] = 0
    reach = score(eng.A, g.influence_ind(ones), eng.F)[:, 0]
    t5["reach_baseline_spearman_abs_with_abs_real"] = spearman(np.abs(reach[E]), np.abs(real_q[E]))
    res["T5"] = t5
    (out / f"tests_{a.label}.json").write_text(json.dumps(res, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o)) + "\n")
    with open(out / f"tests_{a.label}_null_summary.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["null_index", "spearman_with_real_rawQ", "top100_overlap_rawQ", "spearman_with_real_Z", "top100_overlap_Z"])
        for k in range(NN):
            w.writerow([k, f"{rhos[k]:.5f}", int(ov100[k]), f"{rz[k]:.5f}", int(ovz[k])])
    print(json.dumps({k: (v if not isinstance(v, dict) else {kk: vv for kk, vv in v.items() if kk != "c_probes"}) for k, v in res.items()}, indent=1, default=str))
    return 0


# ------------------------------------------------------------------------------------------------ explain / selftest
def cmd_explain(a):
    eng, _, _ = make_engine(a)
    for r in seed_contrib_table(eng, [f for f in a.family if f in eng.comp.fidx]):
        print("\t".join(str(r[k]) for k in r))
    return 0


def selftest():
    """Synthetic graph with known answers: A -> B (+), B -> C (-), D -> C (+). Seed C up. Compound X inhibits A (down on A)."""
    edges = [("A", "B", 1), ("B", "C", -1), ("D", "C", 1)]
    g = Graph(edges, extras=["Z"])
    rows = [dict(family_id=f, target_symbol=t, mean_sign=str(s), groups="ChEMBL", scopes="single_protein") for f, t, s in
            [("X", "A", -1), ("Y", "A", 1), ("W", "D", -1), ("V", "C", -1), ("U", "Z", -1)]]
    comp = Compounds(rows)
    seeds = Seeds([dict(unit_id="s1:C", seed_id="s1", gene="C", sign=1, level=1.0, status="defined", readout_level="transcript", evidence_class="transcript_contrast")])
    eng = Engine(g, comp, seeds)
    ar = eng.arms()
    q = {f: (ar["ind"][comp.fidx[f]], ar["dir"][comp.fidx[f]]) for f in comp.fams}
    # X: A down -> B down -> C up (since B->C is -) : mimics C up -> Q_ind = -(+1) ... computed by hand below
    # effect of A(-1) on C: hop1 B = -1 * 1 (w=1/1) ; hop2 C = (-1)*(-1)*(1/1)... C gets B*(-1)*w(B->C: out-degree 1) => +1 ; damping 0.5 -> +0.5 ; seed C up => X mimics => Q = -0.5
    exp = {"X": (-0.5, 0.0), "Y": (0.5, 0.0), "W": (None, 0.0), "V": (0.0, 1.0), "U": (0.0, 0.0)}
    ok = abs(q["X"][0] + 0.5) < 1e-12 and abs(q["Y"][0] - 0.5) < 1e-12 and abs(q["V"][1] - 1.0) < 1e-12 and q["U"] == (0.0, 0.0)
    # W: D down; D->C (+) with out-degree 1, hop1 C = -1, seed up => Q_ind = +1 (opposes)
    ok = ok and abs(q["W"][0] - 1.0) < 1e-12
    return ok, q


def main():
    ap = argparse.ArgumentParser(description="IT9 P2 seed-based generation engine (see module docstring)")
    sp = ap.add_subparsers(dest="cmd", required=True)
    b = sp.add_parser("build-actions"); b.add_argument("--catalog", default=str(DEFAULT_CATALOG)); b.add_argument("--out", required=True); b.add_argument("--cache")
    r = sp.add_parser("run"); r.add_argument("--seeds", required=True); r.add_argument("--actions", required=True); r.add_argument("--label", required=True)
    r.add_argument("--out", required=True); r.add_argument("--universe"); r.add_argument("--top", type=int, default=100); r.add_argument("--nprox", type=int, default=500)
    r.add_argument("--allow-mixed-levels", action="store_true"); r.add_argument("--nnull", type=int, default=500); r.add_argument("--match", choices=["total", "indeg"], default="total")
    t = sp.add_parser("tests"); t.add_argument("--seeds", required=True); t.add_argument("--actions", required=True); t.add_argument("--label", required=True)
    t.add_argument("--out", required=True); t.add_argument("--decoy"); t.add_argument("--nnull", type=int, default=1000); t.add_argument("--match", choices=["total", "indeg"], default="total"); t.add_argument("--allow-mixed-levels", action="store_true")
    e = sp.add_parser("explain"); e.add_argument("--seeds", required=True); e.add_argument("--actions", required=True); e.add_argument("--family", action="append", required=True)
    e.add_argument("--allow-mixed-levels", action="store_true")
    sp.add_parser("selftest")
    a = ap.parse_args()
    if a.cmd == "build-actions":
        if a.cache:
            os.environ["LEGEND_CATALOG_CACHE"] = a.cache
        build_actions(a.catalog, a.out)
        return 0
    if a.cmd == "run":
        return cmd_run(a)
    if a.cmd == "tests":
        return cmd_tests(a)
    if a.cmd == "explain":
        return cmd_explain(a)
    ok, q = selftest()
    print("selftest", "PASS" if ok else "FAIL", q)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

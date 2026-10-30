#!/usr/bin/env python3
"""IT10 P1 v4 engine: the IT9 v3 engine (edge-mode typing, HGNC canonicalisation) plus ONE filter, F5 'member junction'.

Problem (disclosed in IT9 P4c-d for dimethyl fumarate, KEAP1 -P-> RBX1 -P-> NFKBIB -T-> TNF): the network splits every complex record ('ARNT_HIF1A',
'CUL3_RBX1') into its members, so a member inherits the edge of ANY complex that contains it, and two edges that name the same symbol are joined into a
chain although they may describe different complexes. F5 allows a chain a -> b -> c only if the junction node b is a SINGLETON in both records:
some record of edge a -> b has b alone as its target, and some record of edge b -> c has b alone as its source. The first and the last node of a chain
are not constrained (a compound target may be a complex member; a seed gene may sit in a complex target). One flag: --junction on|off (default on;
off reproduces v3 exactly).

Subcommands run, tests, explain, selftest as in v3 (the IT11 v3 selftest uses a typed toy graph with edge-type controls; network-report is not supported in v4), options --mode v3|all, --match adm. The admissible-in-degree null (--match adm) is still v3's degree and is not junction-aware.
Not a new engine: v3 is loaded and two names are replaced (read_edges, Graph). A compatible action is not a predicted benefit.
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import importlib.util, os
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
V3DIR = HERE.parents[1] / "generation_it9_p2_20261030" / "v3"
JUNCTION = True
for i, x in enumerate(list(sys.argv)):
    if x == "--junction" and i + 1 < len(sys.argv):
        JUNCTION = sys.argv[i + 1] != "off"; del sys.argv[i:i + 2]; break
MATCH_REACH = False                 # IT11: --match reach = null genes matched on the admissible reach (F5-aware), not on a degree
for i, x in enumerate(list(sys.argv)):
    if x == "--match" and i + 1 < len(sys.argv) and sys.argv[i + 1] == "reach":
        MATCH_REACH = True; sys.argv[i + 1] = "total"; break
spec = importlib.util.spec_from_file_location("seed_engine_v3", V3DIR / "seed_engine_v3.py")
m3 = importlib.util.module_from_spec(spec); sys.modules["seed_engine_v3"] = m3; spec.loader.exec_module(m3)
se = m3.se


def read_edges4(inputs=se.DEFAULT_INPUTS):
    """v3 typed edges plus two flags per (source, target, mode): some record has the SOURCE alone, some record has the TARGET alone."""
    h = m3.H(); E = {}; flags = {}; cache = {}; stats = dict(rows=0, symbols_unmapped=0)
    def cn(x):
        if x not in cache:
            c = h.canon(x); cache[x] = (c if c else x).upper()
            if not c: stats["symbols_unmapped"] += 1
        return cache[x]
    for fn in ("signor_omnipath_edges.tsv.gz", "collectri_omnipath_edges.tsv.gz"):
        for r in se.read_tsv(Path(inputs) / fn):
            srcs = r["source_symbol"].split("_") if "_" in r["source_symbol"] else [r["source_symbol"]]
            tgts = r["target_symbol"].split("_") if "_" in r["target_symbol"] else [r["target_symbol"]]
            ty = r["type"]; s_alone = len(srcs) == 1; t_alone = len(tgts) == 1
            for s0 in srcs:
                for t0 in tgts:
                    s, t = cn(s0), cn(t0)
                    if s == t:
                        continue
                    mode = "T" if ty == "transcriptional" else ("P" if ty == "post_translational" else "U")
                    if mode == "P" and m3.GPROT.match(t):
                        mode = "C"
                    sg = int(r["sign"]); k = (s, t, mode)
                    stats["rows"] += 1
                    E[k] = sg if (k not in E or E[k] == sg) else 0
                    f = flags.setdefault(k, [False, False]); f[0] |= s_alone; f[1] |= t_alone
                    m3.EDGE_SOURCES.setdefault(k, (r.get("sources") or "")[:120])
    out = sorted((s, t, sg, m, flags[(s, t, m)][0], flags[(s, t, m)][1]) for (s, t, m), sg in E.items() if sg != 0)
    read_edges4.stats = stats
    return out


class Graph4(m3.Graph3):
    def __init__(self, edges, extras=()):
        self._ss = np.array([bool(e[4]) if len(e) > 4 else True for e in edges])
        self._ts = np.array([bool(e[5]) if len(e) > 5 else True for e in edges])
        super().__init__(edges, extras)

    def _build(self, src, tgt, w):
        super()._build(src, tgt, w)
        self._t4 = {}
        for m in ("T", "P"):
            for ss in (True, False):
                for need in (False, True):
                    mask = (self._modes == m) & (self._ss == ss) & (self._ts | (not need))
                    s_, t_, w_ = src[mask], tgt[mask], w[mask]
                    o = np.argsort(s_, kind="stable"); s_, t_, w_ = s_[o], t_[o], w_[o]
                    us, starts = np.unique(s_, return_index=True)
                    self._t4[(m, ss, need)] = (t_, w_, us, starts)

    def with_signs(self, sg):
        g = object.__new__(type(self)); g.__dict__.update(self.__dict__)
        g._build(self.src0, self.tgt0, np.asarray(sg, float) / self.outdeg[self.src0])
        return g

    def _hop4(self, Z, m, ss, need):
        t_, w_, us, starts = self._t4[(m, ss, need)]
        out = np.zeros_like(Z)
        if len(t_):
            out[:, us] = np.add.reduceat(Z[:, t_] * w_, starts, axis=1)
        return out

    def influence_ind(self, S, hops=se.K, gamma=se.GAMMA):
        if m3.MODE == "all" or not JUNCTION:
            return super().influence_ind(S, hops, gamma)
        first = "T" if self.level == "expression" else "P"
        A = self._hop4(S, first, True, False); B = self._hop4(S, first, False, False)
        V = A + B
        for k in range(2, hops + 1):
            A, B = self._hop4(A, "P", True, True), self._hop4(A, "P", False, True)
            V += (gamma ** (k - 1)) * (A + B)
        return V

    def best_chain(self, target, seed, max_hops=se.K, gamma=se.GAMMA):
        """as v3, with F5: consecutive edges must meet at a singleton junction (unless --junction off)."""
        if target not in self.idx or seed not in self.idx:
            return None
        s_i, g_i = self.idx[target], self.idx[seed]
        succ = {}
        for a, b, w, mo, sg, ss, ts in zip(self.src0, self.tgt0, self.sg0 / self.outdeg[self.src0], self._modes, self.sg0, self._ss, self._ts):
            succ.setdefault(int(a), []).append((int(b), float(w), mo, int(sg), bool(ss), bool(ts)))
        best = [None, 0.0]
        def ok(seq):
            if m3.MODE == "all":
                return all(x in ("T", "P", "C", "U") for x in seq)
            if "C" in seq or "U" in seq:
                return False
            if self.level == "expression":
                return seq[-1] == "T" and all(x == "P" for x in seq[:-1])
            return all(x == "P" for x in seq)
        def dfs(node, path, modes, flags, wprod):
            if len(path) > max_hops:
                return
            if node == g_i and path:
                if ok(modes):
                    val = abs(wprod) * (gamma ** (len(path) - 1))
                    if val > best[1]:
                        best[0], best[1] = (list(path), list(modes), wprod), val
                return
            if len(path) == max_hops:
                return
            for b, w, mo, sg, ss, ts in succ.get(node, ()):
                if JUNCTION and m3.MODE != "all" and flags and not (flags[-1][1] and ss):
                    continue
                dfs(b, path + [(node, b, sg)], modes + [mo], flags + [(ss, ts)], wprod * w)
        dfs(s_i, [], [], [], 1.0)
        if not best[0]:
            return None
        path, modes, wprod = best[0]
        parts = []
        for (a, b, sg), mo in zip(path, modes):
            parts.append(f"{self.syms[a]} -{mo}({'+' if sg > 0 else '-'})-> {self.syms[b]} [{m3.EDGE_SOURCES.get((self.syms[a], self.syms[b], mo), '')}]")
        return "; ".join(parts)


_REACH = {}


def reach_counts(g, chunk=400):
    """admissible reach of every graph gene used as a seed: the number of nodes with a non-zero influence on it (same walks, same F5 rule, K hops).
    This is what the null seed's score depends on; the in-degree or total degree is a proxy for it."""
    key = (id(g), g.level, JUNCTION)
    if key in _REACH:
        return _REACH[key]
    out = np.zeros(g.Ng)
    for a in range(0, g.Ng, chunk):
        b = min(g.Ng, a + chunk)
        S = np.zeros((b - a, g.N)); S[np.arange(b - a), np.arange(a, b)] = 1.0
        out[a:b] = (np.abs(g.influence_ind(S)) > 0).sum(axis=1)
    _REACH[key] = out
    return out


_prev_match_bins = se.match_bins


def match_bins4(g, match):
    if MATCH_REACH:
        deg = reach_counts(g)
        edges = np.unique(np.quantile(deg, np.linspace(0.1, 0.9, 9)))
        bins = np.digitize(deg, edges)
        return bins, [np.flatnonzero(bins == b) for b in range(len(edges) + 1)]
    return _prev_match_bins(g, match)


se.match_bins = match_bins4


def __getattr__(name):     # every other v3 name (H, EDGE_SOURCES, MODE, GPROT, ...) is the v3 one
    return getattr(m3, name)


def _walks(self, target, seed, max_hops=se.K, gamma=se.GAMMA):
    """Every admissible walk (same mode and F5 rules as influence_ind) from a compound target to a seed gene, with its signed value |prod of weights| x gamma^(hops-1).
    The signed sum over these walks equals the influence the score uses for that (target, seed) pair (tested), so the shown chain can be placed in the real calculation:
    returns a list of (list of (a, b), value)."""
    if target not in self.idx or seed not in self.idx:
        return []
    s_i, g_i = self.idx[target], self.idx[seed]
    succ = {}
    for a, b, w, mo, ss, ts in zip(self.src0, self.tgt0, self.sg0 / self.outdeg[self.src0], self._modes, self._ss, self._ts):
        succ.setdefault(int(a), []).append((int(b), float(w), mo, bool(ss), bool(ts)))
    out = []
    def ok(seq):
        if m3.MODE == "all":
            return True
        if "C" in seq or "U" in seq:
            return False
        if self.level == "expression":
            return seq[-1] == "T" and all(x == "P" for x in seq[:-1])
        return all(x == "P" for x in seq)
    def dfs(node, path, modes, flags, wp):
        if node == g_i and path:
            if ok(modes):
                out.append((list(path), wp * (gamma ** (len(path) - 1))))
            return
        if len(path) == max_hops:
            return
        for b, w, mo, ss, ts in succ.get(node, ()):
            if JUNCTION and m3.MODE != "all" and flags and not (flags[-1][1] and ss):
                continue
            dfs(b, path + [(self.syms[node], self.syms[b])], modes + [mo], flags + [(ss, ts)], wp * w)
    dfs(s_i, [], [], [], 1.0)
    return out


Graph4.walks = _walks


def walk_summary(walks):
    """(n_walks, share of the pair's absolute walk mass carried by the strongest walk, share of the mass that opposes the net sign). Empty -> (0, None, None)."""
    if not walks:
        return 0, None, None
    gross = sum(abs(v) for _, v in walks)
    net = sum(v for _, v in walks)
    best = max(abs(v) for _, v in walks)
    opp = sum(abs(v) for _, v in walks if v * net < 0) if net else gross
    return len(walks), best / gross, opp / gross


Graph3 = Graph4            # names used by make_candidates_v3.py
read_edges3 = read_edges4
se.Graph = Graph4
se.read_edges = read_edges4

if __name__ == "__main__":
    raise SystemExit(se.main())

#!/usr/bin/env python3
"""IT9 P2 v3 engine: the v2 seed engine with the edge-mode filter F1 and HGNC-id canonicalisation of network and seed symbols (Amendment 5, PRE_REGISTRATION_V3.md).

Same subcommands and options as ../seed_engine.py (run, tests, explain, selftest) plus:
  --match adm          (v3 only) null genes matched on the admissible in-degree (Amendment 5c)
  --mode v3|all        v3 (default): edge typing by record mode and seed-level compatibility (expression seed: chains P* T, no coupling; protein/phospho seed: chains P+ only);
                       all: every edge usable at every level (the v2 behaviour; used for the filter-off halves of the mutation tests and the comparison)
  network-report --out FILE     edge counts by mode (T, P, C, U)
Use with the compound side from build_actions_v3.py (--actions results/actions). Edge sign/weight are unchanged (1/out-degree over all edges of the source).
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import importlib.util, json, os, re
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
V2DIR = HERE.parent
MODE = "v3"
for i, x in enumerate(list(sys.argv)):
    if x == "--mode" and i + 1 < len(sys.argv):
        MODE = sys.argv[i + 1]; del sys.argv[i:i + 2]; break
MATCH_ADM = False
for i, x in enumerate(list(sys.argv)):
    if x == "--match" and i + 1 < len(sys.argv) and sys.argv[i + 1] == "adm":
        MATCH_ADM = True; sys.argv[i + 1] = "total"; break     # v2's argparse only knows total|indeg; M3 is switched by this flag
_sv = list(sys.argv)
spec = importlib.util.spec_from_file_location("seed_engine_v2", V2DIR / "seed_engine.py")
se = importlib.util.module_from_spec(spec); sys.modules["seed_engine_v2"] = se; spec.loader.exec_module(se)
sys.argv = _sv
spec3 = importlib.util.spec_from_file_location("build_actions_v3", HERE / "build_actions_v3.py")
ba = importlib.util.module_from_spec(spec3); spec3.loader.exec_module(ba)
_H = None
GPROT = re.compile(r"^(GNA[0-9A-Z]{1,3}|GNB[0-9]+|GNG[0-9T]+)$")
EDGE_SOURCES = {}


def H():
    global _H
    if _H is None:
        _H = ba.Hgnc()
    return _H


def read_edges3(inputs=se.DEFAULT_INPUTS):
    """typed edges (source, target, sign, mode); symbols mapped to HGNC approved symbols; duplicates with conflicting sign inside one mode dropped."""
    h = H(); E = {}; stats = dict(rows=0, symbols_unmapped=0)
    cache = {}
    def cn(x):
        if x not in cache:
            c = h.canon(x)
            cache[x] = (c if c else x).upper()
            if not c: stats["symbols_unmapped"] += 1
        return cache[x]
    for fn in ("signor_omnipath_edges.tsv.gz", "collectri_omnipath_edges.tsv.gz"):
        for r in se.read_tsv(Path(inputs) / fn):
            srcs = r["source_symbol"].split("_") if "_" in r["source_symbol"] else [r["source_symbol"]]
            tgts = r["target_symbol"].split("_") if "_" in r["target_symbol"] else [r["target_symbol"]]
            ty = r["type"]
            for s0 in srcs:
                for t0 in tgts:
                    s, t = cn(s0), cn(t0)
                    if s == t:
                        continue
                    mode = "T" if ty == "transcriptional" else ("P" if ty == "post_translational" else "U")
                    if mode == "P" and GPROT.match(t):
                        mode = "C"
                    sg = int(r["sign"]); k = (s, t, mode)
                    stats["rows"] += 1
                    E[k] = sg if (k not in E or E[k] == sg) else 0
                    EDGE_SOURCES.setdefault(k, (r.get("sources") or "")[:120])
    out = sorted((s, t, sg, m) for (s, t, m), sg in E.items() if sg != 0)
    read_edges3.stats = stats
    return out


class Graph3(se.Graph):
    level = "expression"

    def __init__(self, edges, extras=()):
        self._modes = np.array([e[3] for e in edges])
        super().__init__(edges, extras)

    def _build(self, src, tgt, w):
        super()._build(src, tgt, w)
        self._typed = {}
        for m in ("T", "P"):
            mask = self._modes == m
            s_, t_, w_ = src[mask], tgt[mask], w[mask]
            o = np.argsort(s_, kind="stable")
            s_, t_, w_ = s_[o], t_[o], w_[o]
            us, starts = np.unique(s_, return_index=True)
            self._typed[m] = (t_, w_, us, starts)

    def adm_indeg(self):
        key = "T" if self.level == "expression" else "P"
        return np.bincount(self.tgt0[self._modes == key], minlength=self.N).astype(float)[:self.Ng]

    def hop_bwd_typed(self, Z, m):
        t_, w_, us, starts = self._typed[m]
        out = np.zeros_like(Z)
        if len(t_):
            out[:, us] = np.add.reduceat(Z[:, t_] * w_, starts, axis=1)
        return out

    def influence_ind(self, S, hops=se.K, gamma=se.GAMMA):
        if MODE == "all":
            return super().influence_ind(S, hops, gamma)
        if self.level == "expression":
            u = self.hop_bwd_typed(S, "T"); V = u.copy(); h = u
            for m in range(1, hops):
                h = self.hop_bwd_typed(h, "P"); V += (gamma ** m) * h
            return V
        V = np.zeros_like(S); h = S
        for k in range(1, hops + 1):
            h = self.hop_bwd_typed(h, "P"); V += (gamma ** (k - 1)) * h
        return V

    def best_chain(self, target, seed, max_hops=se.K, gamma=se.GAMMA):
        """strongest admissible chain (by |product of weights x gamma^(hops-1)|) from a compound target to a seed gene under the current level and mode."""
        if target not in self.idx or seed not in self.idx:
            return None
        s_i, g_i = self.idx[target], self.idx[seed]
        succ = {}
        for a, b, w, m, sg in zip(self.src0, self.tgt0, self.sg0 / self.outdeg[self.src0], self._modes, self.sg0):
            succ.setdefault(int(a), []).append((int(b), float(w), m, int(sg)))
        best = [None, 0.0]
        def ok(seq):
            if MODE == "all":
                return all(m in ("T", "P", "C", "U") for m in seq)
            if "C" in seq or "U" in seq:
                return False
            if self.level == "expression":
                return seq[-1] == "T" and all(m == "P" for m in seq[:-1])
            return all(m == "P" for m in seq)
        def dfs(node, path, modes, wprod):
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
            for b, w, m, sg in succ.get(node, ()):
                dfs(b, path + [(node, b, sg)], modes + [m], wprod * w)
        dfs(s_i, [], [], 1.0)
        if not best[0]:
            return None
        path, modes, wprod = best[0]
        parts = []
        for (a, b, sg), m in zip(path, modes):
            parts.append(f"{self.syms[a]} -{m}({'+' if sg > 0 else '-'})-> {self.syms[b]} [{EDGE_SOURCES.get((self.syms[a], self.syms[b], m), '')}]")
        return "; ".join(parts)


_orig_match_bins = se.match_bins
def match_bins3(g, match):
    if MATCH_ADM:
        deg = g.adm_indeg()
        edges = np.unique(np.quantile(deg, np.linspace(0.1, 0.9, 9)))
        bins = np.digitize(deg, edges)
        return bins, [np.flatnonzero(bins == b) for b in range(len(edges) + 1)]
    return _orig_match_bins(g, match)
se.match_bins = match_bins3
_orig_load = se.load_seeds
def load_seeds3(path, allow_mixed=False, human_only=True, ignore_guards=False):
    s = _orig_load(path, allow_mixed=allow_mixed, human_only=human_only, ignore_guards=ignore_guards)
    for u in s.units:
        c = H().canon(u["gene"])
        if c and c.upper() != u["gene"]:
            u["gene_input"] = u["gene"]; u["gene"] = c.upper()
    return s

_orig_make = se.make_engine
def make_engine3(a, seeds_path=None, rows=None, meta=None, restrict=None):
    eng, rows, meta = _orig_make(a, seeds_path, rows, meta, restrict)
    lv = {u["readout_level"] for u in eng.seeds.units}
    if len(lv) > 1:
        raise SystemExit(f"v3 needs one readout level per run, got {sorted(lv)}")
    lvl = next(iter(lv)) if lv else "expression"
    eng.g.level = "expression" if lvl == "expression" else "protein"
    return eng, rows, meta

se.Graph = Graph3
se.read_edges = read_edges3
se.load_seeds = load_seeds3
se.make_engine = make_engine3


def network_report(out):
    E = read_edges3()
    import collections
    c = collections.Counter(e[3] for e in E)
    info = dict(edges_by_mode=dict(c), edges_total=len(E), reading=read_edges3.stats,
                g_protein_coupling_edges=[(e[0], e[1]) for e in E if e[3] == "C"][:50], note="C = post-translational record whose target is a heterotrimeric G-protein subunit gene")
    Path(out).write_text(json.dumps(info, indent=1) + "\n")
    print(json.dumps(info, indent=1)[:600])


if __name__ == "__main__":
    if sys.argv[1] == "network-report":
        network_report(sys.argv[sys.argv.index("--out") + 1])
        raise SystemExit(0)
    raise SystemExit(se.main())

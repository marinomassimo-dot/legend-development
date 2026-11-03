#!/usr/bin/env python3
"""IT21 P5, arm 3: the SAME generator with the WWOX-specific contribution removed.

Three decoy designs, because the registered null matches on a COARSE covariate (the top degree decile spans very different hubs):
  coarse  a random gene of the same total-degree decile (what the engine's own null does, so a decoy is exchangeable with a null draw)
  deg     one of the 30 genes nearest in total degree (in + out) to the real seed gene: a hub is replaced by a hub of the same size
  reach   one of the 30 genes nearest in F5-admissible reach (the covariate of the IT11 reach-matched null) at the set's readout level

What is removed: the identity of the seed genes. Every seed gene (or process member) of a real WWOX seed set is replaced by a random gene of the same total-degree
decile of the same signed network; the direction, level, readout level, evidence class, guard tag and the number of units are kept. What is kept: the engine
(`engine_v4/seed_engine_v4.py`, unchanged), the refreshed compound side (`generation_it21_p2_20261103/results/actions`), the three IT10 nulls and the IT11 reach-matched
null, the seed-specific rule of `make_candidates_v3.py` (|z| > 3, same sign, in the three nulls, unflagged for active moiety) and the reach confirmation (H1 of P2).
What the difference measures: how much of the seed-specific output depends on WHICH genes were observed to change in WWOX-deficient systems, as opposed to the shape of
the network around a gene of that degree and the catalogue's coverage of its neighbours.

  decoy_arm.py make    --out DIR --k N               write the decoy seed files (deterministic; the real set is replicate 0 of the control)
  decoy_arm.py run     --work DIR --out FILE --k N [--workers 3] [--actions DIR] [--sets A,B]    run the engine on real (control) + N decoys, keep only the seed-specific rows
  decoy_arm.py control --rows FILE                           compare the control rows with the committed P2 seed-specific list

Reuses, does not copy: the engine and its nulls (IT10/IT11), the P2 action table, the seed tables of IT9. Zero spend, no network.
"""
import sys
if __name__ == "__main__" and (len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help")):
    print(__doc__)
    raise SystemExit(0)
import argparse, collections, csv, gzip, importlib.util, io, multiprocessing as mp, os, shutil, subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
IT10 = DR / "generation_it10_p1_20261031"
P2 = DR / "generation_it21_p2_20261103"
SEEDS = DR / "generation_it9_p2_20261030" / "seeds_p1"
ENGINE = IT10 / "engine_v4" / "seed_engine_v4.py"
SETS = ("Q2_expression_tiersAB", "Q4_expression_tiersAB", "Q5_expression_tiersAB", "Q6_expression_tiersAB", "Q6_protein_tiersAB")
NULLS = (("total", ""), ("indeg", "_indeg"), ("adm", "_adm"), ("reach", "_reach"))
SEED_BASE = 20261103
NEAREST = 30
VARIANTS = ("coarse", "deg", "reach")
OUT_COLS = ["seed_set", "variant", "rep", "family_id", "name", "sign", "z_total", "z_indeg", "z_adm", "z_reach", "reach_ok", "main_target", "hop", "direct_hit", "decoy_genes"]


def read_tsv(p):
    with (gzip.open(p, "rt", encoding="utf-8") if str(p).endswith(".gz") else open(p, encoding="utf-8")) as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def load_engine():
    """The v4 engine module, imported the way make_candidates_v3 does (its argv check needs a subcommand)."""
    spec = importlib.util.spec_from_file_location("seed_engine_v4", ENGINE)
    m = importlib.util.module_from_spec(spec)
    saved, sys.argv = sys.argv, ["seed_engine_v4.py", "selftest"]
    try:
        sys.modules["seed_engine_v4"] = m
        spec.loader.exec_module(m)
    finally:
        sys.argv = saved
    return m


class DecoyFactory:
    """Degree-matched replacement genes, deterministic in (replicate, unit index, bin)."""

    def __init__(self):
        import numpy as np
        self.np = np
        self.m = load_engine()
        self.H = self.m.H()
        self.G = self.m.Graph3(self.m.read_edges3(), extras=[])
        self.bins, self.pools = self.m.se.match_bins(self.G, "total")
        self.not_in_graph = 0
        self.m.m3.MODE = "v3"
        self.deg = (self.G.indeg + self.G.outdeg)[:self.G.Ng].astype(float)
        self._reach = {}

    def reach(self, level):
        if level not in self._reach:
            self.G.level = level
            self._reach[level] = self.m.reach_counts(self.G).astype(float)
        return self._reach[level]

    def covariate(self, variant, level):
        return self.deg if variant == "deg" else self.reach("expression" if level == "expression" else "protein")

    def canon(self, x):
        c = self.H.canon(x)
        return (c if c else x).upper()

    def unit_bin(self, gene):
        j = self.G.idx.get(self.canon(gene))
        return int(self.bins[j]) if (j is not None and j < self.G.Ng) else None

    def draw(self, rep, uidx, gene, used, variant="coarse", level="expression"):
        np = self.np
        b = self.unit_bin(gene)
        if b is None:
            self.not_in_graph += 1
            b = len(self.pools) // 2
        pool = self.pools[b]
        if variant != "coarse":
            j = self.G.idx.get(self.canon(gene))
            if j is not None and j < self.G.Ng:
                cov = self.covariate(variant, level)
                order = np.argsort(np.abs(cov - cov[j]) + 1e-9 * np.arange(self.G.Ng), kind="stable")
                pool = np.array([int(x) for x in order if int(x) != j and int(x) not in used][:NEAREST], dtype=int)
        rng = np.random.default_rng([SEED_BASE, rep, uidx, b, {"coarse": 0, "deg": 1, "reach": 2}[variant]])
        for _ in range(10000):
            c = int(pool[rng.integers(0, len(pool))])
            if c not in used:
                used.add(c)
                return self.G.syms[c]
        raise RuntimeError("no free decoy gene")

    def decoy_rows(self, rows, rep, variant="coarse"):
        """rows: seed table rows of one real set. Returns (new rows, the decoy gene list)."""
        real = set()
        for r in rows:
            for g in (r["members"].split(";") if r["kind"] == "process" else [r["gene"]]):
                if g.strip():
                    real.add(self.G.idx.get(self.canon(g)))
        used = {x for x in real if x is not None}
        out, genes, u = [], [], 0
        for r in rows:
            r2 = dict(r)
            if r["kind"] != "process" and self.unit_bin(r["gene"]) is None:
                continue        # a real seed gene that is not a node of the network contributes nothing; its decoy is omitted, so the decoy does not gain a unit the real set lacks
            if r["kind"] == "process":
                mem = []
                for g in [x for x in r["members"].split(";") if x.strip()]:
                    if self.unit_bin(g) is None:
                        continue
                    mem.append(self.draw(rep, u, g, used, variant, r["readout_level"])); u += 1
                r2["members"] = ";".join(mem)
                r2["gene"] = f"SET:DECOY_{rep:03d}"
                genes += mem
            else:
                g2 = self.draw(rep, u, r["gene"], used, variant, r["readout_level"]); u += 1
                r2["gene"] = g2
                genes.append(g2)
            r2["seed_id"] = f'{r["seed_id"].split(":")[0]}:decoy{rep:03d}:{r2["gene"]}'
            r2["note"] = f"IT21 P5 decoy {rep}: degree-matched replacement of {r['gene']}"
            out.append(r2)
        return out, genes


def write_seed_file(path, rows, cols):
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def cmd_make(a):
    fac = DecoyFactory()
    out = Path(a.out)
    for sn in SETS:
        rows = read_tsv(SEEDS / f"{sn}.tsv")
        cols = list(rows[0])
        for v in VARIANTS:
            d = out / v / sn
            d.mkdir(parents=True, exist_ok=True)
            for k in range(1, a.k + 1):
                new, genes = fac.decoy_rows(rows, k, v)
                write_seed_file(d / f"decoy{k:03d}.tsv", new, cols)
    print("decoy seed files written; seed genes outside the graph:", fac.not_in_graph)


# ---- the engine on one seed file --------------------------------------------------------------------------------------------------------------------
def run_engine(seed_file, label, wd, match, actions, nnull=500):
    env = dict(os.environ)
    env.setdefault("LEGEND_CATALOG_CACHE", str(DR / "catalog" / "cache"))
    cmd = [sys.executable, "-B", str(ENGINE), "run", "--seeds", str(seed_file), "--actions", str(actions), "--label", label, "--out", str(wd),
           "--match", match, "--mode", "v3", "--junction", "on", "--nnull", str(nnull), "--top", "3500"]
    r = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(f"engine failed for {label} {match}: {r.stderr[-400:]}")


def prop_path(wd, label):
    """The engine writes proposals as .tsv.gz (contributions as plain .tsv)."""
    p = Path(wd) / f"proposals_{label}.tsv.gz"
    return p if p.exists() else Path(wd) / f"proposals_{label}.tsv"


def zmap(path):
    return {r["family_id"]: float(r["Z_ind_robust"]) for r in read_tsv(path)}


def spec_from_runs(wd, label, flagged, genes):
    """The seed-specific rule of make_candidates_v3.py (allspec) on the four proposals files, plus the reach confirmation of P2 rule H1."""
    tot = read_tsv(prop_path(wd, label))
    zi, za = (zmap(prop_path(wd, label + s)) for s in ("_indeg", "_adm"))
    zr = zmap(prop_path(wd, label + "_reach")) if prop_path(wd, label + "_reach").exists() else {}
    contrib = collections.defaultdict(list)
    for c in read_tsv(Path(wd) / f"contributions_{label}.tsv"):
        contrib[c["family_id"]].append(c)
    rows = []
    for r in tot:
        fid = r["family_id"]
        z1 = float(r["Z_ind_robust"])
        if abs(z1) <= 3 or fid in flagged or fid not in zi or fid not in za:
            continue
        sg = 1 if z1 > 0 else -1
        if not (zi[fid] * sg > 3 and za[fid] * sg > 3):
            continue
        cs = sorted(contrib.get(fid, []), key=lambda c: -abs(float(c["contrib_total"])))
        main, hop = "", ""
        if cs:
            c = cs[0]
            h0, h1 = abs(float(c["contrib_hop0"])), abs(float(c["contrib_hops1to3"]))
            main, hop = (c["main_target_hop0"], "0") if h0 > h1 else (c["main_target_hops1to3"], "1-3")
        z4 = zr.get(fid)
        rows.append(dict(family_id=fid, name=r["name"], sign=sg, z_total=z1, z_indeg=zi[fid], z_adm=za[fid], z_reach="" if z4 is None else z4,
                         reach_ok=int(z4 is not None and z4 * sg > 3), main_target=main, hop=hop, direct_hit=r["direct_hit_any_action_on_seed_gene"],
                         decoy_genes=genes))
    return rows


def flagged_families(actions):
    out = set()
    for r in read_tsv(Path(actions) / "family_actions.tsv.gz"):
        if "UNCERTAIN_ACTIVE_MOIETY" in (r["flags"] or ""):
            out.add(r["family_id"])
    return out


def one(task):
    sn, variant, rep, work, actions = task
    wd = Path(work) / f"{sn}_{variant}_{rep:03d}"
    wd.mkdir(parents=True, exist_ok=True)
    try:
        if rep == 0:
            sf, genes = SEEDS / f"{sn}.tsv", "REAL"
        else:
            sf = Path(work) / "seeds" / variant / sn / f"decoy{rep:03d}.tsv"
            genes = ";".join(r["members"] if r["kind"] == "process" else r["gene"] for r in read_tsv(sf))
        label = f"p1_{sn}_{variant[0]}{rep:03d}"
        fl = flagged_families(actions)
        for match, suf in NULLS[:3]:
            run_engine(sf, label + suf, wd, match, actions)
        if spec_from_runs(wd, label, fl, genes):          # the reach null is only needed for a set that has a seed-specific row at all
            run_engine(sf, label + "_reach", wd, "reach", actions)
        rows = spec_from_runs(wd, label, fl, genes)
        for r in rows:
            r["seed_set"], r["rep"], r["variant"] = sn, rep, ("real" if rep == 0 else variant)
        return rows
    finally:
        shutil.rmtree(wd, ignore_errors=True)


def cmd_run(a):
    work = Path(a.work)
    (work / "seeds").mkdir(parents=True, exist_ok=True)
    sets = [s for s in SETS if not a.sets or s in a.sets.split(",")]
    variants = [v for v in VARIANTS if v in a.variants.split(",")]
    if not (work / "seeds" / "reach" / sets[0] / f"decoy{a.k:03d}.tsv").exists():
        cmd_make(argparse.Namespace(out=str(work / "seeds"), k=a.k))
    tasks = [(sn, "real", 0, str(work), a.actions) for sn in sets] + [(sn, v, rep, str(work), a.actions) for v in variants for rep in range(1, a.k + 1) for sn in sets]
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with gzip.open(out, "wt", encoding="utf-8", newline="") as fh, mp.Pool(a.workers) as pool:
        w = csv.DictWriter(fh, fieldnames=OUT_COLS, delimiter="\t", lineterminator="\n")
        w.writeheader()
        for rows in pool.imap_unordered(one, tasks):
            w.writerows(rows)
            n += 1
            if n % 25 == 0:
                print(f"{n}/{len(tasks)} runs", flush=True)
                fh.flush()
    print("done", n, "runs ->", out)


def cmd_control(a):
    """The replicate-0 rows (the real seed sets, through THIS code) against the committed P2 seed-specific list: same families, same reach-confirmed subset."""
    mine = collections.defaultdict(set)
    for r in read_tsv(a.rows):
        if r["rep"] == "0":
            mine[r["seed_set"]].add((r["family_id"], "opposes" if r["sign"] == "1" else "mimics"))
    ref = collections.defaultdict(set)
    for r in read_tsv(P2 / "results" / "engine" / "v3_seed_specific_all_nulls.tsv"):
        ref[r["seed_set"]].add((r["family_id"], r["arm"]))
    res = []
    for sn in SETS:
        res.append(dict(seed_set=sn, mine=len(mine[sn]), p2=len(ref[sn]), only_mine=len(mine[sn] - ref[sn]), only_p2=len(ref[sn] - mine[sn])))
    for r in res:
        print(r)
    return res


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("make"); m.add_argument("--out", required=True); m.add_argument("--k", type=int, default=100)
    r = sub.add_parser("run"); r.add_argument("--work", required=True); r.add_argument("--out", required=True); r.add_argument("--k", type=int, default=100)
    r.add_argument("--workers", type=int, default=3); r.add_argument("--actions", default=str(P2 / "results" / "actions")); r.add_argument("--sets", default=""); r.add_argument("--variants", default="coarse,deg,reach")
    c = sub.add_parser("control"); c.add_argument("--rows", required=True)
    a = ap.parse_args()
    {"make": cmd_make, "run": cmd_run, "control": cmd_control}[a.cmd](a)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""v3 candidate tables per question: arms opposes / mimics (robust, z against the degree-matched seed null), flagged_opposes / flagged_mimics (families carrying UNCERTAIN_ACTIVE_MOIETY, kept out of the
robust arms), direct_search. Each row gives the contributing seeds, the strongest admissible EDGE CHAIN from the main target to the seed with its record modes (T/P) and OmniPath source labels,
the family flags, and the status of the family in the v2 candidate tables.

  make_candidates_v3.py --seeds-dir ../seeds_p1 --results results --out results [--top-opposes 50] [--top-mimics 25] [--engine PATH]
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, collections, csv, glob, gzip, importlib.util, os
from pathlib import Path
HERE = Path(__file__).resolve().parent
_s = list(sys.argv); sys.argv = ["seed_engine_v3.py", "selftest"]
ENGINE = HERE / "seed_engine_v3.py"          # IT10: --engine PATH loads another engine with the same names (seed_engine_v4.py)
for _i, _x in enumerate(_s):
    if _x == "--engine" and _i + 1 < len(_s):
        ENGINE = Path(_s[_i + 1]).resolve(); del _s[_i:_i + 2]; break
spec = importlib.util.spec_from_file_location("seed_engine_v3", ENGINE)
m = importlib.util.module_from_spec(spec); sys.modules["seed_engine_v3"] = m; spec.loader.exec_module(m); sys.argv = _s
ap = argparse.ArgumentParser(); ap.add_argument("--seeds-dir", required=True); ap.add_argument("--results", required=True); ap.add_argument("--out", required=True)
ap.add_argument("--top-opposes", type=int, default=50); ap.add_argument("--top-mimics", type=int, default=25)
a = ap.parse_args()
rd = lambda p, gz=False: list(csv.DictReader((gzip.open(p, "rt", encoding="utf-8") if gz else open(p, encoding="utf-8")), delimiter="\t"))
R = Path(a.results); act = R / "actions"
anyt = collections.defaultdict(set)
for r in rd(act / "family_targets_any.tsv.gz", True): anyt[r["family_id"]].add(r["target_symbol"].upper())
meta = {r["family_id"]: r["name"] for r in rd(act / "family_meta.tsv.gz", True)}
fflags = collections.defaultdict(set)
for r in rd(act / "family_actions.tsv.gz", True):
    for x in filter(None, r["flags"].split(";")): fflags[r["family_id"]].add(x)
v2 = {}
for f in glob.glob(str(HERE.parent / "results" / "candidates_Q*.tsv")):
    for r in rd(f):
        if r["arm"] in ("opposes", "mimics") and r["seed_set"] == r["seed_set"]:
            v2[(r["seed_set"], r["family_id"])] = f"{r['arm']}#{r['rank']}" + ("(seed-specific v2)" if r["seed_specific_both_nulls"] == "1" else "")
edges = m.read_edges3(); G = m.Graph3(edges, extras=[])
COLS = ["question", "seed_set", "arm", "rank", "family_id", "name", "Z_ind_robust_total_null", "Z_ind_robust_indeg_null", "Z_ind_robust_adm_null", "seed_specific_all_three_nulls", "Q_net_ind", "compatible_action", "conditional_on_uncertain_seeds",
        "also_found_by_direct_search", "family_flags", "contributing_seed_1", "contributing_seed_2", "edge_chain_main_target_to_seed_1", "v2_status", "evaluation_forbidden_on"]
byq = collections.defaultdict(list); summary = []; allspec = []
for f in sorted(glob.glob(os.path.join(a.seeds_dir, "*.tsv"))):
    if f.endswith("manifest.tsv"): continue
    sn = os.path.basename(f)[:-4]; q = sn.split("_")[0]
    pt, pi = R / f"proposals_p1_{sn}.tsv.gz", R / f"proposals_p1_{sn}_indeg.tsv.gz"
    if not pt.exists(): continue
    prop = rd(pt, True); zi = {r["family_id"]: float(r["Z_ind_robust"]) for r in rd(pi, True)} if pi.exists() else {}
    pa = R / f"proposals_p1_{sn}_adm.tsv.gz"; za = {r["family_id"]: float(r["Z_ind_robust"]) for r in rd(pa, True)} if pa.exists() else {}
    ct = collections.defaultdict(list)
    for r in rd(R / f"contributions_p1_{sn}.tsv.gz", True): ct[r["family_id"]].append(r)
    seeds = rd(f); genes = set()
    for r in seeds: genes |= set(x for x in r["members"].split(";") if x) if r["kind"] == "process" else {r["gene"].upper()}
    genes = {m.H().canon(x).upper() if m.H().canon(x) else x for x in genes}
    lv = {r["readout_level"] for r in seeds}; G.level = "expression" if lv == {"expression"} else "protein"
    def seedtxt(fid):
        cs = sorted(ct.get(fid, []), key=lambda x: -abs(float(x["contrib_total"])))[:2]; out = []; chain = ""
        for k, c in enumerate(cs):
            h0, h1 = abs(float(c["contrib_hop0"])), abs(float(c["contrib_hops1to3"]))
            hop, tg = ("hop0", c["main_target_hop0"]) if h0 > h1 else ("hops1-3", c["main_target_hops1to3"])
            out.append(f"{c['seed_id'].split(':',1)[-1]}|{c['gene']}|{c['seed_direction']}|{hop}|{tg}|{float(c['contrib_total']):.3g}|{c['guard_tag']}")
            if k == 0:
                chain = "hop0 (target is the seed gene)" if hop == "hop0" else (G.best_chain(tg, c["gene"]) or "no admissible chain found for this target-seed pair (contribution rests on another pair)")
        return out + [""] * (2 - len(out)), chain
    def row(arm, rk, r):
        fid = r["family_id"]; z1 = float(r["Z_ind_robust"]); z2 = zi.get(fid); z3 = za.get(fid); s, ch = seedtxt(fid)
        sgn = 1 if z1 > 0 else -1
        spec3 = int(all(z is not None and z * sgn > 3 for z in (z1, z2, z3)))
        return [q, sn, arm, rk, fid, r["name"], f"{z1:.4g}", "" if z2 is None else f"{z2:.4g}", "" if z3 is None else f"{z3:.4g}", spec3, r["Q_net_ind"], r["compatible_action"],
                int("conditional" in r["compatible_action"]), r["direct_hit_any_action_on_seed_gene"], ";".join(sorted(fflags.get(fid, ()))) or "none", s[0], s[1], ch, v2.get((sn, fid), "not in v2 robust arms"), r["evaluation_forbidden_on"]]
    flagged = lambda r: "UNCERTAIN_ACTIVE_MOIETY" in fflags.get(r["family_id"], ())
    def zmin(r):
        z1 = float(r["Z_ind_robust"]); sgn = 1 if z1 > 0 else -1
        zs = [z1, zi.get(r["family_id"]), za.get(r["family_id"])]
        return min(sgn * z for z in zs if z is not None) if all(z is not None and z * sgn > 0 for z in zs) else 0.0
    for r in prop: r["_zmin"] = zmin(r)
    pos_all = sorted((r for r in prop if float(r["Z_ind_robust"]) > 0), key=lambda r: -r["_zmin"]); neg_all = sorted((r for r in prop if float(r["Z_ind_robust"]) < 0), key=lambda r: -r["_zmin"])
    pos = [r for r in pos_all if not flagged(r)][: a.top_opposes]; neg = [r for r in neg_all if not flagged(r)][: a.top_mimics]
    fpos = [r for r in pos_all if flagged(r)][:25]; fneg = [r for r in neg_all if flagged(r)][:15]
    rows = [row("opposes", i + 1, r) for i, r in enumerate(pos)] + [row("mimics", i + 1, r) for i, r in enumerate(neg)] + \
           [row("flagged_opposes", i + 1, r) for i, r in enumerate(fpos)] + [row("flagged_mimics", i + 1, r) for i, r in enumerate(fneg)]
    pr = {r["family_id"]: r for r in prop}
    dfam = sorted((fid for fid, t in anyt.items() if t & genes), key=lambda x: (-abs(float(pr[x]["Q_direct"])) if x in pr else 0, x))[:50]
    for i, fid in enumerate(dfam):
        r = pr.get(fid); hit = ",".join(sorted(anyt[fid] & genes))
        rows.append([q, sn, "direct_search", i + 1, fid, meta.get(fid, ""), "", "", "", "", r["Q_direct"] if r else "", (("opposes" if float(r["Q_direct"]) > 0 else "mimics") if r and float(r["Q_direct"]) else "unsigned_or_no_signed_direct_action"), "",
                     1, ";".join(sorted(fflags.get(fid, ()))) or "none", "targets:" + hit, "", "hop0 (target is the seed gene)", "n/a", r["evaluation_forbidden_on"] if r else ""])
    byq[q] += rows
    for rk, r in enumerate(sorted(prop, key=lambda r: -r["_zmin"])):
        z1 = float(r["Z_ind_robust"])
        if abs(z1) > 3 and not flagged(r) and zi.get(r["family_id"]) is not None and za.get(r["family_id"]) is not None:
            sgn = 1 if z1 > 0 else -1
            if zi[r["family_id"]] * sgn > 3 and za[r["family_id"]] * sgn > 3:
                x = row("opposes" if sgn > 0 else "mimics", rk + 1, r); allspec.append(x)
    summary.append((sn, len(pos), sum(1 for x in rows if x[2] == "opposes" and x[9] == 1), len(neg), sum(1 for x in rows if x[2] == "mimics" and x[9] == 1), len(fpos) + len(fneg), len(dfam)))
for q, rows in byq.items():
    with open(os.path.join(a.out, f"candidates_{q}.tsv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(COLS); w.writerows(rows)
with open(os.path.join(a.out, "v3_seed_specific_all_nulls.tsv"), "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(COLS); w.writerows(allspec)
for s in summary: print("set %s: opposes %d (seed-specific both nulls %d), mimics %d (%d), flagged rows %d, direct-search %d" % s)

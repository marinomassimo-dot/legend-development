#!/usr/bin/env python3
"""Candidate-proposal tables for P3: one TSV per question, arms opposes / mimics / direct_search, ranked by z against the degree-matched seed null (never by raw Q).

  make_candidates.py --seeds-dir seeds_p1 --results results --actions results --out results [--top-opposes 50] [--top-mimics 25]
Per row: contributing seeds (top two by |contribution|: seed id, gene, seed direction, hop, main target), compatible action (opposes/mimics = direction compatibility only, never predicted benefit),
conditional flag, z under both nulls (registered total-degree; in-degree) and seed_specific_both_nulls (z > 3 in both), whether the family is also found by the direct target search,
evaluation_forbidden_on (guard tags of the seed set). Opposes: top by Z_ind_robust with Z > 0; mimics: most negative; direct_search: families with any catalogue action on a seed gene, signed direct score where one exists.
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, collections, csv, glob, gzip, os
ap = argparse.ArgumentParser()
ap.add_argument("--seeds-dir", required=True); ap.add_argument("--results", required=True); ap.add_argument("--actions", required=True); ap.add_argument("--out", required=True)
ap.add_argument("--top-opposes", type=int, default=50); ap.add_argument("--top-mimics", type=int, default=25)
a = ap.parse_args()
rd = lambda p, gz=False: list(csv.DictReader((gzip.open(p, "rt", encoding="utf-8") if gz else open(p, encoding="utf-8")), delimiter="\t"))
anyt = collections.defaultdict(set)
for r in rd(os.path.join(a.actions, "family_targets_any.tsv.gz"), True): anyt[r["family_id"]].add(r["target_symbol"].upper())
meta = {r["family_id"]: r["name"] for r in rd(os.path.join(a.actions, "family_meta.tsv.gz"), True)}
COLS = ["question", "seed_set", "arm", "rank", "family_id", "name", "Z_ind_robust_total_null", "Z_ind_robust_indeg_null", "seed_specific_both_nulls", "Q_net_ind", "compatible_action", "conditional_on_uncertain_seeds",
        "also_found_by_direct_search", "contributing_seed_1", "contributing_seed_2", "evaluation_forbidden_on"]
byq = collections.defaultdict(list); summary = []
for f in sorted(glob.glob(os.path.join(a.seeds_dir, "*.tsv"))):
    if f.endswith("manifest.tsv"): continue
    sn = os.path.basename(f)[:-4]; q = sn.split("_")[0]
    pt = os.path.join(a.results, f"proposals_p1_{sn}.tsv.gz"); pi = os.path.join(a.results, f"proposals_p1_{sn}_indeg.tsv.gz")
    if not os.path.exists(pt): continue
    prop = rd(pt, True); zi = {r["family_id"]: float(r["Z_ind_robust"]) for r in rd(pi, True)} if os.path.exists(pi) else {}
    ct = collections.defaultdict(list)
    for r in rd(os.path.join(a.results, f"contributions_p1_{sn}.tsv")): ct[r["family_id"]].append(r)
    seeds = rd(f); genes = set()
    for r in seeds: genes |= set(x for x in r["members"].split(";") if x) if r["kind"] == "process" else {r["gene"].upper()}
    def seedtxt(fid):
        cs = sorted(ct.get(fid, []), key=lambda x: -abs(float(x["contrib_total"])))[:2]; out = []
        for c in cs:
            h0, h1 = abs(float(c["contrib_hop0"])), abs(float(c["contrib_hops1to3"]))
            hop, tg = ("hop0", c["main_target_hop0"]) if h0 > h1 else ("hops1-3", c["main_target_hops1to3"])
            out.append(f"{c['seed_id'].split(':',1)[-1]}|{c['gene']}|{c['seed_direction']}|{hop}|{tg}|{float(c['contrib_total']):.3g}")
        return out + [""] * (2 - len(out))
    def row(arm, rk, r):
        fid = r["family_id"]; z1 = float(r["Z_ind_robust"]); z2 = zi.get(fid)
        s = seedtxt(fid)
        return [q, sn, arm, rk, fid, r["name"], f"{z1:.4g}", "" if z2 is None else f"{z2:.4g}", int(z1 > 3 and z2 is not None and z2 > 3), r["Q_net_ind"], r["compatible_action"],
                int("conditional" in r["compatible_action"]), r["direct_hit_any_action_on_seed_gene"], s[0], s[1], r["evaluation_forbidden_on"]]
    pos = [r for r in prop if float(r["Z_ind_robust"]) > 0][: a.top_opposes]
    neg = [r for r in reversed(prop) if float(r["Z_ind_robust"]) < 0][: a.top_mimics]
    rows = [row("opposes", i + 1, r) for i, r in enumerate(pos)] + [row("mimics", i + 1, r) for i, r in enumerate(neg)]
    pr = {r["family_id"]: r for r in prop}
    dfam = sorted((fid for fid, t in anyt.items() if t & genes), key=lambda x: (-abs(float(pr[x]["Q_direct"])) if x in pr else 0, x))[:50]
    for i, fid in enumerate(dfam):
        r = pr.get(fid)
        hit = ",".join(sorted(anyt[fid] & genes))
        rows.append([q, sn, "direct_search", i + 1, fid, meta.get(fid, ""), "", "", "", r["Q_direct"] if r else "", (("opposes" if float(r["Q_direct"]) > 0 else "mimics") if r and float(r["Q_direct"]) else "unsigned_or_no_signed_direct_action"), "",
                     1, "targets:" + hit, "", r["evaluation_forbidden_on"] if r else ""])
    byq[q] += rows
    summary.append((sn, len(pos), sum(1 for x in rows if x[2] == "opposes" and x[8] == 1), len(neg), len(dfam)))
for q, rows in byq.items():
    with open(os.path.join(a.out, f"candidates_{q}.tsv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(COLS); w.writerows(rows)
for s in summary: print("set %s: opposes rows %d (seed-specific in both nulls %d), mimics rows %d, direct-search rows %d" % s)

#!/usr/bin/env python3
"""v2 vs v3 comparison (PRE_REGISTRATION_V3.md S1, S2, S5): per seed set counts, survivors of the v2 seed-specific list with the filter that removed each lost family, and the status of the
P3 proposals (P3-01 .. P3-20) in v3. Variants: v2 = committed v2 results; f1 = edge-mode filter only; f2 = identity + active-moiety flags only; p1 = full v3.

  compare_v2_v3.py --v3 results --out results
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, collections, csv, glob, gzip, json, os
from pathlib import Path
HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser(); ap.add_argument("--v3", required=True); ap.add_argument("--out", required=True); a = ap.parse_args()
V3, V2 = Path(a.v3), HERE.parent / "results"
rd = lambda p, gz=True: list(csv.DictReader((gzip.open(p, "rt", encoding="utf-8") if gz else open(p, encoding="utf-8")), delimiter="\t"))
def load(d, prefix, sn):
    out = {}
    for suf, key in (("", "t"), ("_indeg", "i"), ("_adm", "a")):
        p = Path(d) / f"proposals_{prefix}{sn}{suf}.tsv.gz"
        if not p.exists():
            if key == "a": continue
            return None
        for r in rd(p):
            out.setdefault(r["family_id"], {})[key] = float(r["Z_ind_robust"])
    return out
flags = collections.defaultdict(set)
for r in rd(V3 / "actions" / "family_actions.tsv.gz"):
    for x in filter(None, r["flags"].split(";")): flags[r["family_id"]].add(x)
spec = lambda z, sgn: z is not None and (z["t"] * sgn > 3 and z.get("i", 0) * sgn > 3)
strict = lambda z, sgn: spec(z, sgn) and z.get("a") is not None and z["a"] * sgn > 3
sets = sorted(os.path.basename(f)[:-4] for f in glob.glob(str(HERE.parent / "seeds_p1" / "Q*.tsv")))
rows = [["seed_set", "non_zero_v2", "non_zero_v3", "specific_opposes_v2", "specific_opposes_v3", "v2_opposes_surviving_in_v3", "lost_by_edge_mode_F1", "lost_by_identity_F2_only", "lost_other_or_both", "moved_to_flagged_F3", "specific_mimics_v2", "specific_mimics_v3", "v2_mimics_surviving_in_v3", "new_in_v3_opposes", "new_in_v3_mimics", "specific_opposes_v3_all_three_nulls", "specific_mimics_v3_all_three_nulls", "v2_opposes_surviving_all_three", "v2_mimics_surviving_all_three"]]
lostlist = []
for sn in sets:
    v2, v3, f1, f2 = load(V2, "p1_", sn), load(V3, "p1_", sn), load(V3, "f1_", sn), load(V3, "f2_", sn)
    if not v3: continue
    t2 = json.load(open(V2 / f"tests_p1_{sn}.json")); t3 = json.load(open(V3 / f"tests_p1_{sn}.json"))
    row = [sn, t2["T2"]["a_families_nonzero"], t3["T2"]["a_families_nonzero"]]
    for sgn, nm in ((1, "opposes"), (-1, "mimics")):
        s2 = {f for f, z in v2.items() if spec(z, sgn)}
        s3 = {f for f, z in v3.items() if spec(z, sgn) and "UNCERTAIN_ACTIVE_MOIETY" not in flags.get(f, ())}
        surv = s2 & s3; lost = s2 - s3; byF1 = byF2 = oth = flg = 0
        for f in lost:
            if "UNCERTAIN_ACTIVE_MOIETY" in flags.get(f, ()) and spec(v3.get(f), sgn): flg += 1; why = "F3_flagged"
            else:
                a1 = spec(f1.get(f), sgn) if f1 else True; a2 = spec(f2.get(f), sgn) if f2 else True
                if not a1 and a2: byF1 += 1; why = "F1_edge_mode"
                elif a1 and not a2: byF2 += 1; why = "F2_identity"
                else: oth += 1; why = "both_or_other"
            lostlist.append([sn, nm, f, why])
        new = s3 - s2
        if nm == "opposes": row += [len(s2), len(s3), len(surv), byF1, byF2, oth, flg]
        else: row += [len(s2), len(s3), len(surv)]
        row_new = len(new)
        if nm == "opposes": newo = row_new
        else: newm = row_new
    so3 = {f for f, z in v3.items() if strict(z, 1) and "UNCERTAIN_ACTIVE_MOIETY" not in flags.get(f, ())}; sm3 = {f for f, z in v3.items() if strict(z, -1) and "UNCERTAIN_ACTIVE_MOIETY" not in flags.get(f, ())}
    v2o = {f for f, z in v2.items() if spec(z, 1)}; v2m = {f for f, z in v2.items() if spec(z, -1)}
    row += [newo, newm, len(so3), len(sm3), len(v2o & so3), len(v2m & sm3)]
    rows.append(row)
with open(Path(a.out) / "v2_vs_v3_counts.tsv", "w", encoding="utf-8", newline="") as fh: csv.writer(fh, delimiter="\t", lineterminator="\n").writerows(rows)
with open(Path(a.out) / "v2_specific_families_lost_in_v3.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["seed_set", "arm", "family_id", "reason"]); w.writerows(lostlist)
# P3 proposals
P3 = HERE.parent.parent / "exploration_it9_p3_20261030"
fam_of = {r["parent"]: r["family_ids"].split(";") for r in rd(P3 / "candidates_consolidated.tsv", False)}
cand = {}
for q in "1234567":
    pth = V3 / f"candidates_Q{q}.tsv"
    if pth.exists():
        for r in rd(pth, False): cand.setdefault((r["seed_set"], r["family_id"]), []).append(r)
def prank(label, sn):
    p = V3 / f"proposals_{label}{sn}.tsv.gz"
    return {r["family_id"]: (i + 1, float(r["Z_ind_robust"])) for i, r in enumerate(rd(p))} if p.exists() else {}
out = [["cand_id", "name", "v2_seed_set", "v2_arm", "v3_sets_checked", "status_v3", "detail_per_family", "reason_if_not_robust", "chain_if_robust"]]
chains = {}
for r in rd(V3 / "v3_seed_specific_all_nulls.tsv", False): chains[(r["seed_set"], r["family_id"])] = r["edge_chain_main_target_to_seed_1"]
for r in rd(P3 / "selected.tsv", False):
    fams = fam_of.get(r["parent_chembl_id"], []); sn = r["seed_set"]; arm = r["arm_direction"]
    sg = 1 if arm == "opposes" else (-1 if arm == "mimics" else 0)
    sets_here = [sn] + ([sn.replace("expression", "protein")] if sn.startswith("Q6_expression") else [])
    sets_here = [x for x in sets_here if (V3 / f"proposals_p1_{x}.tsv.gz").exists()]
    detail, status, chain, why = [], "ABSENT_FROM_V3_PROPOSALS", "", []
    best = None
    for s_ in sets_here:
        P, PI, PA = prank("p1_", s_), prank("p1_", s_ + "_indeg"), prank("p1_", s_ + "_adm")
        for f in fams:
            if f in P:
                zt, zi_, za_ = P[f][1], PI.get(f, (0, 0))[1], PA.get(f, (0, 0))[1]
                strictv = all(z * (1 if zt > 0 else -1) > 3 for z in (zt, zi_, za_))
                fl = "UNCERTAIN_ACTIVE_MOIETY" in flags.get(f, ())
                detail.append(f"{s_}:{f}: Z total/indeg/adm {zt:.2f}/{zi_:.2f}/{za_:.2f} rank {P[f][0]}{' FLAGGED_ACTIVE_MOIETY' if fl else ''}")
                two = all(z * (1 if zt > 0 else -1) > 3 for z in (zt, zi_))
                st = "FLAGGED_UNCERTAIN_ACTIVE_MOIETY" if fl else ("ROBUST_ALL_THREE_NULLS" if strictv else ("SPECIFIC_IN_TWO_NULLS_NOT_ADM" if two else "NOT_SEED_SPECIFIC_IN_V3"))
                order = ["ROBUST_ALL_THREE_NULLS", "SPECIFIC_IN_TWO_NULLS_NOT_ADM", "FLAGGED_UNCERTAIN_ACTIVE_MOIETY", "NOT_SEED_SPECIFIC_IN_V3", "ABSENT_FROM_V3_PROPOSALS"]
                if order.index(st) < order.index(status): status = st
                if strictv and not fl: chain = chain or chains.get((s_, f), "")
    if sg == 0:
        ds = [c for s_ in [sn.split(":")[0]] for (ss, f), cs in cand.items() if ss.startswith(s_) for c in cs if c["arm"] == "direct_search" and f in fams]
        status = "IN_DIRECT_SEARCH_ARM" if ds else "ABSENT_FROM_DIRECT_SEARCH_ARM"
        detail = [f"{c['seed_set']}:{c['family_id']} direct rank {c['rank']} targets {c['contributing_seed_1']}" for c in ds[:3]]
    if status in ("ABSENT_FROM_V3_PROPOSALS", "NOT_SEED_SPECIFIC_IN_V3", "SPECIFIC_IN_TWO_NULLS_NOT_ADM"):
        z1, z2, z0 = load(V3, "f1_", sn), load(V3, "f2_", sn), load(V2, "p1_", sn)
        for f in fams:
            if z0 and sg and spec(z0.get(f), sg):
                a1 = spec(z1.get(f), sg) if z1 else None; a2 = spec(z2.get(f), sg) if z2 else None
                why.append(f"{f}: seed-specific in v2; edge-mode filter alone {'keeps' if a1 else 'removes'}; identity/flags alone {'keeps' if a2 else 'removes'}")
    out.append([r["cand_id"], r["name"], sn, arm, ";".join(sets_here), status, " | ".join(detail)[:500], " | ".join(why)[:400], chain[:300]])
with open(Path(a.out) / "p3_proposals_status_v3.tsv", "w", encoding="utf-8", newline="") as fh: csv.writer(fh, delimiter="\t", lineterminator="\n").writerows(out)
for r in rows: print("\t".join(map(str, r)))

#!/usr/bin/env python3
"""IT16 P2: score the module's frozen intervention selection against trivial baselines.

Offline, stdlib only, no clock, writes nothing unless --out is given. Reads the ranking tables
of ranking_it8_p9_20261029 (selections.tsv, units.tsv, member_evidence.tsv) and a dated outcomes table.

  report    [--out FILE]      measures 1-4 of PRE_REGISTRATION.md
  evaluate  --outcomes TSV    score the frozen general selection against B0/B1 on outcomes dated after the freeze

Exit 0 always for report; evaluate exits 2 when fewer than 5 independent post-freeze outcomes exist (no claim).
"""
import argparse
import csv
import hashlib
import json
import sys
from itertools import combinations
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
RANK = HERE.parent / "ranking_it8_p9_20261029"
FREEZE = "2026-10-29"
MIN_OUTCOMES = 5
TOPN = 8


def tsv(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def num(x):
    try:
        return int(x)
    except (TypeError, ValueError):
        return 0


def hyper_ge(k, n_pool, n_good, n_draw):
    """P(X >= k) drawing n_draw from n_pool containing n_good."""
    tot = comb(n_pool, n_draw)
    return sum(comb(n_good, i) * comb(n_pool - n_good, n_draw - i) for i in range(k, min(n_good, n_draw) + 1)) / tot


def kendall(a, b):
    """tau over items present in both orderings."""
    common = [x for x in a if x in b]
    if len(common) < 2:
        return None
    c = d = 0
    for x, y in combinations(common, 2):
        s = (a.index(x) - a.index(y)) * (b.index(x) - b.index(y))
        c += s > 0
        d += s < 0
    return (c - d) / (c + d) if c + d else None


def load():
    units = tsv(RANK / "units.tsv")
    mem = tsv(RANK / "member_evidence.tsv")
    sel = [r for r in tsv(RANK / "selections.tsv") if r["view"] == "general"]
    sel.sort(key=lambda r: int(r["position_in_list"]))
    return units, mem, sel


def per_unit(mem):
    w, o, tested, classonly = {}, {}, {}, {}
    for m in mem:
        u = m["unit_id"]
        w[u] = w.get(u, 0) + num(m["wwox_assertions"])
        o[u] = o.get(u, 0) + num(m["outside_wwox_assertions"])
        tested[u] = tested.get(u, False) or m["tested_in_wwox_system"] == "yes"
        classonly.setdefault(u, True)
        if m["member_type"] != "class_level":
            classonly[u] = False
    return w, o, tested, classonly


def baselines(units, w, o):
    ids = [u["unit_id"] for u in units]
    b1 = sorted(ids, key=lambda u: (-w.get(u, 0), u))
    b2 = sorted(ids, key=lambda u: (-o.get(u, 0), u))
    return ids, b1, b2


def report():
    units, mem, sel = load()
    w, o, tested, classonly = per_unit(mem)
    ids, b1, b2 = baselines(units, w, o)
    mod = [r["unit_id"] for r in sel]
    top = mod[:TOPN]
    tset = {u for u, t in tested.items() if t}
    names = {u["unit_id"]: u["label"] for u in units}
    out = {
        "inputs_sha256": {f: sha(RANK / f) for f in ("units.tsv", "selections.tsv", "member_evidence.tsv")},
        "pool_units": len(ids),
        "units_with_member_rows": len({m["unit_id"] for m in mem}),
        "module_top": top,
        "tested_units": sorted(tset),
        "m1_top_in_tested": f"{len(set(top) & tset)}/{len(top)}",
        "m1_hypergeom_p_ge": hyper_ge(len(set(top) & tset), len(ids), len(tset), len(top)),
        "m1_b1_top": b1[:TOPN],
        "m1_overlap_module_b1": len(set(top) & set(b1[:TOPN])),
        "m1_kendall_module_vs_b1": kendall(top, b1),
        "m1_b2_top": b2[:TOPN],
        "m1_overlap_module_b2": len(set(top) & set(b2[:TOPN])),
        "m1_module_not_in_b1": [(u, names[u]) for u in top if u not in b1[:TOPN]],
        "m1_b1_not_in_module": [(u, names[u]) for u in b1[:TOPN] if u not in top],
        "m1_b1_ties_at_cut": sum(1 for u in ids if w.get(u, 0) == w.get(b1[TOPN - 1], 0)),
    }
    # measure 3: how many tested units have the outcome paper as their only WWOX-system evidence
    out["m3_tested_units"] = len(tset)
    out["m3_pool_defined_by_outcomes"] = True if tset else False
    # measure 4
    out["m4_untested_units"] = len(ids) - len(tset)
    out["m4_class_level_only_units"] = sum(1 for u in ids if classonly.get(u, False))
    out["m4_units_without_member_rows"] = len(ids) - len({m["unit_id"] for m in mem})
    out["m4_units_with_wwox_null_harm"] = sum(1 for u in units if not u["X_counter_evidence"].startswith("WWOX-system null/harm/mixed assertions 0"))
    gen = {u["unit_id"] for u in units if u["M_mechanism"].startswith("generated proposal")}
    out["m5_generated_proposal_units"] = len(gen)
    out["m5_generated_in_top"] = len(gen & set(top))
    out["m5_generated_with_wwox_system_result"] = len(gen & tset)
    # outcomes
    oc = tsv(HERE / "outcomes_it16.tsv")
    origins = {r["pmid"] for r in oc}
    controlled = {r["pmid"] for r in oc if r["kind_of_result"] == "controlled perturbation"}
    out["m2_outcome_rows"] = len(oc)
    out["m2_distinct_origins"] = len(origins)
    out["m2_controlled_origins"] = len(controlled)
    out["m2_after_freeze"] = sum(1 for r in oc if r["pub_date"] > FREEZE)
    out["m2_dates"] = sorted(r["pub_date"] for r in oc)
    # retrospective split at 2022-01-01 (invalid for prediction when the pool is defined by outcomes)
    dev = [r for r in oc if r["pub_date"] < "2022-01-01"]
    ev = [r for r in oc if r["pub_date"] >= "2022-01-01"]
    out["retro_dev_units"] = sorted({r["unit_id"] for r in dev})
    out["retro_eval_units"] = sorted({r["unit_id"] for r in ev})
    out["retro_eval_controlled_origins"] = len({r["pmid"] for r in ev if r["kind_of_result"] == "controlled perturbation"})
    return out


def evaluate(path):
    units, mem, sel = load()
    w, o, tested, _ = per_unit(mem)
    ids, b1, _ = baselines(units, w, o)
    top = [r["unit_id"] for r in sel][:TOPN]
    rows = [r for r in tsv(path) if r["pub_date"] > FREEZE and r["kind_of_result"] == "controlled perturbation"]
    origins = {r["pmid"] for r in rows}
    hit_units = {r["unit_id"] for r in rows}
    res = {"independent_post_freeze_origins": len(origins), "units_hit": sorted(hit_units),
           "module_hits": len(hit_units & set(top)), "b1_hits": len(hit_units & set(b1[:TOPN])),
           "b0_p_ge_module_hits": hyper_ge(len(hit_units & set(top)), len(ids), len(hit_units), TOPN) if hit_units else None}
    res["claim"] = "none: fewer than %d independent post-freeze outcomes" % MIN_OUTCOMES if len(origins) < MIN_OUTCOMES else "scored; interpret against B1 first"
    return res, len(origins) >= MIN_OUTCOMES


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    r = sub.add_parser("report")
    r.add_argument("--out")
    e = sub.add_parser("evaluate")
    e.add_argument("--outcomes", required=True)
    a = ap.parse_args(argv)
    if a.cmd == "report":
        text = json.dumps(report(), indent=1, ensure_ascii=False, sort_keys=True)
        if a.out:
            Path(a.out).write_text(text + "\n", encoding="utf-8")
        print(text)
        return 0
    if a.cmd == "evaluate":
        res, ok = evaluate(a.outcomes)
        print(json.dumps(res, indent=1, sort_keys=True))
        return 0 if ok else 2
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())

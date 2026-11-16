#!/usr/bin/env python3
"""Mechanism-class matching matrix: score classes by a rule fixed beforehand, reproducibly.

    python3 framework/scripts/aed_matrix.py score CELLS.tsv RULE.json [--out FILE] [--expect-rule-sha256 HEX]

WHY
---
The question is which antiseizure mechanism class matches the repository's WWOX threads, asked
without repeating the contrasting literature (MEETING f4lqagml, item 3). A hand-built table can
be re-ranked at will; this tool makes the ranking a function of two committed files. It is a
matching exercise on mechanism labels: it nominates no agent, gives no dose, and clears nothing
through BLOCK-1.

INPUTS
------
CELLS.tsv, one row per (thread, class, optional agent) with columns
  cell_id, thread_id, class_id, agent_id, endpoint, age, sign, evidence_tier, link_directness,
  axis, origin_id, has_genotype_contrast, has_drug_by_genotype, unit, source_locator
  sign in {match, neutral, aggravation, unknown}; tier and directness are integers 0-3;
  endpoint, age and class_id in the rule's closed lists; has_* in {yes, no}. The thread set is DATA:
  any thread_id is accepted, but every cell needs a source_locator, an axis and an origin_id, and
  the run prints the final thread list's sha256 so a freeze can record it.
  A thread in the rule's never_specific_threads is scored as generic whatever its cell says;
  a thread in zero_directness_threads must carry directness 0 or the run is refused.
RULE.json holds the formula's parameters and the written rubric (see check_rule). Its sha256 is
printed on every run and may be pinned with --expect-rule-sha256. When both files are tracked
by git, the rule's first commit must be an ancestor of the cells' first commit.

WHAT IT COMPUTES, per endpoint (never summed across endpoints) and per age window next to the pooled one
  - cell value = evidence_tier x link_directness;
  - a class's score sums, over DISTINCT (axis, origin_id) keys, the largest value of its `match`
    cells under that key: one origin counts once, however many threads cite it;
  - three scores: all cells, only cells with has_genotype_contrast=yes, only has_drug_by_genotype=yes;
  - aggravation scored the same way and reported in its OWN column, never netted against a match;
  - `unknown` and `neutral` are counted, never scored, and never merged with each other;
  - a degree-preserving permutation null (the class labels of the match cells are permuted among
    the match cells of the endpoint, so every class keeps its number of cells; the permutation is
    a function of the seed and the cell ids, identical on every run and Python version);
  - rank stability: the top class under every single-cell tier +-1 change and the all +-1 change,
    and under every PAIR of match cells moved by +-1 (bounded two-cell enumeration, capped at a fixed
    number of runs and reported as not run above it); full 3^n enumeration is not feasible;
  - the top set, its size k out of the rule's classes, informativeness 1 - k/N and a label:
    `discriminating` (k = 1), `tie_set_weak` (k above 1 and within the rule's share of the classes),
    `not_discriminating` (above it), `no_scored_class`; a window with no match cell is emitted as a
    frozen null ordering (`not_scorable_null_ordering`, all classes tied), never as a neutral;
  - `null undefined` instead of a p-value when the null is degenerate (equal tiers, no match cell,
    zero variance across permutations);
  - the stability of the top SET (a class-level 'top class' out of a tie is a tie-break artefact): the share of
    single-cell and all +-1 tier changes under which the same set stays on top, the share under which each
    class is inside the top set, and the range of the set's size;
  - `score_origin_collapsed`: the sum over origins of the best cell of that origin whatever its axis, printed
    beside score_all, which collapses by (axis, origin) key; neither changes rank_by, a note names a change of the top set;
  - the per-thread sum (every match cell, no origin collapse) with its rank next to the origin-collapsed
    score, and a note when collapsing changes the top set or one origin carries every match cell.
An agent ranking is printed only for the top class and only when some (axis, origin) key carries
a match for one agent of that class and not for another.

RULES R1-R3 (rule v2, declared together by r1_min_link, r2_scorable_denominator and r3_splits; a rule without them runs exactly as v1)
  R1  a class is scored in a group only with a match or aggravation link at the rule's minimum tier and directness;
  R2  informativeness and the tie-share limit use the scorable classes of the group, so empty columns never raise informativeness;
  R3  the children of a declared split need two representative agent ids each and a distinguishing thread, else they are unscorable.
An unscorable class is printed (rank `unscorable`, its aggravation still shown) and named in a note; it is never neutral.

Exit codes: 0 scored (or no cells) · 2 invalid invocation, rule, cells or pinned digest.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import prediction_ledger as pl  # noqa: E402  (the git helpers live there)

CELL_COLUMNS = ["cell_id", "thread_id", "class_id", "agent_id", "endpoint", "age", "sign",
                "evidence_tier", "link_directness", "axis", "origin_id", "has_genotype_contrast",
                "has_drug_by_genotype", "unit", "source_locator"]
SIGNS = ("match", "neutral", "aggravation", "unknown")
YESNO = ("yes", "no")
SCORES = ("score_all", "score_specific", "score_drug_by_genotype")
OUT_COLUMNS = ["endpoint", "window", "class_id", "rank", "score_all", "score_specific",
               "score_drug_by_genotype", "aggravation_score", "match_keys", "score_per_thread_sum",
               "rank_per_thread_sum", "neutral_cells", "unknown_cells", "null_mean", "excess",
               "null_ge_fraction", "top_set_size", "informativeness", "top_set_label", "tied_with",
               "score_origin_collapsed", "rank_origin_collapsed", "top_set_same_share",
               "top_set_membership_share"]
OUT_COLUMNS_V2 = OUT_COLUMNS + ["scorable", "scorable_classes"]   # only a rule with R1-R3 adds them: a v1 run keeps its bytes
POOLED = "pooled"


def r_rules(rule: dict) -> bool:
    """True when the rule declares R1-R3 (rule v2): scored only with a link, informativeness over the scorable classes, splits checked."""
    return "r1_min_link" in rule


def out_columns(rule: dict) -> list[str]:
    return OUT_COLUMNS_V2 if r_rules(rule) else OUT_COLUMNS


class Invalid(Exception):
    pass


def check_rule(rule: dict) -> None:
    for key in ("rule_version", "tier_rubric", "directness_rubric", "endpoints", "age_windows", "classes",
                "never_specific_threads", "zero_directness_threads", "discriminating_top_set_max_share",
                "rank_by", "permutations", "seed"):
        if key not in rule:
            raise Invalid(f"rule lacks {key!r}")
    for rubric in ("tier_rubric", "directness_rubric"):
        if sorted(rule[rubric]) != ["0", "1", "2", "3"] or not all(str(v).strip() for v in rule[rubric].values()):
            raise Invalid(f"{rubric} must describe 0, 1, 2 and 3 in words")
    if not rule["endpoints"] or not all(isinstance(e, str) and e for e in rule["endpoints"]):
        raise Invalid("endpoints must be a non-empty list of names")
    for key in ("endpoints", "age_windows", "classes"):
        if not rule[key] or len(set(rule[key])) != len(rule[key]):
            raise Invalid(f"{key} must be a non-empty list without repeats")
    for key in ("never_specific_threads", "zero_directness_threads"):
        if not isinstance(rule[key], list) or not all(isinstance(t, str) and t for t in rule[key]):
            raise Invalid(f"{key} must be a list of thread ids")
    share = rule["discriminating_top_set_max_share"]
    if not (isinstance(share, list) and len(share) == 2 and all(isinstance(n, int) and n > 0 for n in share)):
        raise Invalid("discriminating_top_set_max_share must be [numerator, denominator], positive integers")
    if any(k in rule for k in ("r1_min_link", "r2_scorable_denominator", "r3_splits")):
        if not all(k in rule for k in ("r1_min_link", "r2_scorable_denominator", "r3_splits")):
            raise Invalid("R1, R2 and R3 are declared together: r1_min_link, r2_scorable_denominator and r3_splits")
        lo = rule["r1_min_link"]
        if not (isinstance(lo, list) and len(lo) == 2 and all(isinstance(n, int) and 1 <= n <= 3 for n in lo)):
            raise Invalid("r1_min_link must be [minimum tier, minimum directness], integers 1-3")
        if rule["r2_scorable_denominator"] is not True:
            raise Invalid("r2_scorable_denominator must be true when R1-R3 are declared")
        for sp in rule["r3_splits"]:
            kids = sp.get("children") if isinstance(sp, dict) else None
            if not (isinstance(sp, dict) and sp.get("parent") and isinstance(kids, list) and len(kids) >= 2
                    and set(kids) <= set(rule["classes"]) and isinstance(sp.get("min_representatives", 2), int)):
                raise Invalid("each r3_splits entry needs a parent, two or more children that are rule classes, and an integer min_representatives")
    if rule["rank_by"] not in SCORES:
        raise Invalid(f"rank_by must be one of {SCORES}")
    if not (isinstance(rule["permutations"], int) and 0 <= rule["permutations"] <= 10000):
        raise Invalid("permutations must be an integer 0-10000")
    if not isinstance(rule["seed"], int):
        raise Invalid("seed must be an integer")


def read_cells(path: Path, rule: dict) -> list[dict]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        missing = [c for c in CELL_COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            raise Invalid(f"cells lack columns: {', '.join(missing)}")
        rows = [{c: (r.get(c) or "").strip() for c in CELL_COLUMNS} for r in reader]
    seen = set()
    for n, row in enumerate(rows, 2):
        where = f"row {n} ({row['cell_id'] or 'no cell_id'})"
        for req in ("cell_id", "thread_id", "class_id", "endpoint", "age", "axis", "origin_id", "source_locator"):
            if not row[req]:
                raise Invalid(f"{where}: {req} is required")
        if row["cell_id"] in seen:
            raise Invalid(f"{where}: duplicate cell_id")
        seen.add(row["cell_id"])
        if row["sign"] not in SIGNS:
            raise Invalid(f"{where}: sign {row['sign']!r} not in {SIGNS}")
        for col, key in (("endpoint", "endpoints"), ("age", "age_windows"), ("class_id", "classes")):
            if row[col] not in rule[key]:
                raise Invalid(f"{where}: {col} {row[col]!r} not in the rule's {key}")
        if row["thread_id"] in rule["zero_directness_threads"] and row["link_directness"] != "0":
            raise Invalid(f"{where}: the rule fixes directness 0 for thread {row['thread_id']}")
        generic = row["thread_id"] in rule["never_specific_threads"]
        for col in ("has_genotype_contrast", "has_drug_by_genotype"):
            if row[col] not in YESNO:
                raise Invalid(f"{where}: {col} must be yes or no")
        if row["has_drug_by_genotype"] == "yes" and row["has_genotype_contrast"] != "yes":
            raise Invalid(f"{where}: a drug-by-genotype test is a genotype contrast; set both to yes")
        for col in ("evidence_tier", "link_directness"):
            if row[col] not in ("0", "1", "2", "3"):
                raise Invalid(f"{where}: {col} must be an integer 0-3")
        if generic:  # generic by rule, whatever the cell says
            row["has_genotype_contrast"] = row["has_drug_by_genotype"] = "no"
    return rows


def value(row: dict, shift: int = 0) -> int:
    tier = min(3, max(0, int(row["evidence_tier"]) + shift))
    return tier * int(row["link_directness"])


def class_scores(rows: list[dict], sign: str, shift_all: int = 0, shifts: dict[str, int] | None = None):
    """class_id -> {score name -> sum over distinct (axis, origin) of the largest cell value}."""
    best: dict[str, dict[str, dict[tuple, int]]] = {}
    for row in rows:
        if row["sign"] != sign:
            continue
        val = value(row, shift_all + (shifts or {}).get(row["cell_id"], 0))
        key = (row["axis"], row["origin_id"])
        for name, ok in (("score_all", True), ("score_specific", row["has_genotype_contrast"] == "yes"),
                         ("score_drug_by_genotype", row["has_drug_by_genotype"] == "yes")):
            if ok:
                slot = best.setdefault(row["class_id"], {}).setdefault(name, {})
                slot[key] = max(slot.get(key, 0), val)
    return {c: {n: sum(v.values()) for n, v in names.items()} for c, names in best.items()}


def per_thread_sums(rows: list[dict]) -> dict[str, int]:
    """class_id -> sum of tier x directness over EVERY match cell (no origin collapse)."""
    sums: dict[str, int] = {}
    for row in rows:
        if row["sign"] == "match":
            sums[row["class_id"]] = sums.get(row["class_id"], 0) + value(row)
    return sums


def origin_collapsed_sums(rows: list[dict]) -> dict[str, int]:
    """class_id -> sum over ORIGINS of the largest cell value of that origin, whatever its axis (best axis per origin)."""
    best: dict[str, dict[str, int]] = {}
    for row in rows:
        if row["sign"] == "match":
            slot = best.setdefault(row["class_id"], {})
            slot[row["origin_id"]] = max(slot.get(row["origin_id"], 0), value(row))
    return {c: sum(v.values()) for c, v in best.items()}


def ranked(classes: list[str], scores: dict, by: str) -> list[tuple[str, int]]:
    return sorted(((c, scores.get(c, {}).get(by, 0)) for c in classes), key=lambda t: (-t[1], t[0]))


def permuted(rows: list[dict], seed: int, index: int) -> list[dict]:
    """The match cells with their class labels permuted among themselves (degree preserving)."""
    match = sorted((r for r in rows if r["sign"] == "match"), key=lambda r: r["cell_id"])
    order = sorted(match, key=lambda r: hashlib.sha256(f"{seed}:{index}:{r['cell_id']}".encode()).hexdigest())
    labels = [r["class_id"] for r in match]
    moved = {r["cell_id"]: labels[k] for k, r in enumerate(order)}
    return [dict(r, class_id=moved[r["cell_id"]]) if r["cell_id"] in moved else r for r in rows]


def null_for(rows: list[dict], classes: list[str], rule: dict):
    """-> ({class: (null mean, fraction of permutations >= observed)}, reason the null is undefined or '')."""
    n = rule["permutations"]
    match = [r for r in rows if r["sign"] == "match"]
    if n == 0:
        return {}, "no permutations requested"
    if not match:
        return {}, "no match cell"
    if len({r["evidence_tier"] for r in match}) == 1:
        return {}, "equal tiers: the ordering rests on the declared directness judgements"
    observed = class_scores(rows, "match")
    sims = [class_scores(permuted(rows, rule["seed"], k), "match") for k in range(n)]
    out, spread = {}, False
    for c in classes:
        values = [sim.get(c, {}).get("score_all", 0) for sim in sims]
        spread = spread or len(set(values)) > 1
        out[c] = (sum(values) / n, sum(v >= observed.get(c, {}).get("score_all", 0) for v in values) / n)
    return (out, "") if spread else ({}, "zero variance across permutations")


def stability(rows: list[dict], classes: list[str], rule: dict) -> tuple[str, int, int, list[str]]:
    by = rule["rank_by"]
    base = ranked(classes, class_scores(rows, "match"), by)
    top = base[0][0]
    tied = [c for c, s in base if s == base[0][1]]
    runs = [("all+1", dict(shift_all=1)), ("all-1", dict(shift_all=-1))]
    runs += [(f"{r['cell_id']}{s:+d}", dict(shifts={r["cell_id"]: s}))
             for r in sorted(rows, key=lambda r: r["cell_id"]) if r["sign"] == "match" for s in (1, -1)]
    keep, moved = 0, []
    for label, kw in runs:
        winner = ranked(classes, class_scores(rows, "match", **kw), by)
        if winner[0][0] == top and (len(winner) < 2 or winner[0][1] > winner[1][1]):
            keep += 1
        else:
            moved.append(label)
    return top, keep, len(runs), moved if len(tied) == 1 else moved + [f"tie at baseline: {','.join(tied)}"]


def set_stability(rows: list[dict], classes: list[str], rule: dict) -> dict:
    """Stability of the top SET (a tie-break picks one 'top class' out of a tie, so a class-level count is an artefact):
    how often the original top set stays the top set under every single-cell tier +-1 change and the all +-1 change,
    how often each class is inside the top set, and the range of the set's size."""
    by = rule["rank_by"]
    base = set(top_set(ranked(classes, class_scores(rows, "match"), by)))
    runs = [dict(shift_all=1), dict(shift_all=-1)]
    runs += [dict(shifts={r["cell_id"]: s}) for r in sorted(rows, key=lambda r: r["cell_id"]) if r["sign"] == "match" for s in (1, -1)]
    same, inside, sizes = 0, {c: 0 for c in classes}, []
    for kw in runs:
        now = set(top_set(ranked(classes, class_scores(rows, "match", **kw), by)))
        same += now == base
        sizes.append(len(now))
        for c in now:
            inside[c] += 1
    return {"base": base, "runs": len(runs), "same": same, "inside": inside, "kmin": min(sizes), "kmax": max(sizes)}


PAIR_RUN_CAP = 200000


def stability_pairs(rows: list[dict], classes: list[str], rule: dict) -> str:
    """Every PAIR of match cells moved by (+-1, +-1): a bounded two-cell enumeration (deterministic cap)."""
    cells = sorted(r["cell_id"] for r in rows if r["sign"] == "match")
    total = len(cells) * (len(cells) - 1) // 2 * 4
    if total == 0:
        return "two-cell tier enumeration: fewer than two match cells"
    if total > PAIR_RUN_CAP:
        return f"two-cell tier enumeration not run: {total} runs exceed the cap {PAIR_RUN_CAP}"
    by = rule["rank_by"]
    base = ranked(classes, class_scores(rows, "match"), by)
    top, keep = base[0][0], 0
    for i, a in enumerate(cells):
        for b in cells[i + 1:]:
            for sa in (1, -1):
                for sb in (1, -1):
                    w = ranked(classes, class_scores(rows, "match", shifts={a: sa, b: sb}), by)
                    keep += w[0][0] == top and w[0][1] > w[1][1]
    return f"two-cell tier enumeration: top class kept in {keep} of {total} runs"


def agent_ranking(rows: list[dict], top: str, by: str) -> str:
    cells = [r for r in rows if r["class_id"] == top and r["sign"] == "match"]
    agents = sorted({r["agent_id"] for r in cells if r["agent_id"]})
    if len(agents) < 2:
        return "agent ranking not licensed: fewer than two agents carry a match in the top class"
    keys = {a: {(r["axis"], r["origin_id"]) for r in cells if r["agent_id"] == a} for a in agents}
    shared = {(r["axis"], r["origin_id"]) for r in cells if not r["agent_id"]}
    if all(keys[a] | shared == keys[agents[0]] | shared for a in agents):
        return "agent ranking not licensed: no (axis, origin) key separates two agents of the top class"
    pairs = []
    for a in agents:
        mine = [r for r in rows if r["class_id"] == top and (r["agent_id"] in ("", a))]
        pairs.append((a, class_scores(mine, "match").get(top, {}).get(by, 0)))
    pairs.sort(key=lambda t: (-t[1], t[0]))
    return "agent scores inside the top class: " + "; ".join(f"{a}={s}" for a, s in pairs)


def top_set(order: list[tuple[str, int]]) -> list[str]:
    best = order[0][1]
    return [c for c, s in order if s == best] if best > 0 else []


def tie_label(k: int, n_classes: int, share: list[int]) -> str:
    if k == 0:
        return "no_scored_class"
    if k == 1:
        return "discriminating"
    return "tie_set_weak" if k * share[1] <= n_classes * share[0] else "not_discriminating"


def has_link(row: dict, rule: dict) -> bool:
    """R1: a cell links its class to a thread at the rule's minimum tier and directness (a match or an aggravation link; unknown and neutral are not links)."""
    lo_t, lo_d = rule["r1_min_link"]
    return row["sign"] in ("match", "aggravation") and int(row["evidence_tier"]) >= lo_t and int(row["link_directness"]) >= lo_d


def split_failures(rows: list[dict], rule: dict) -> dict[str, str]:
    """R3: child class -> reason, for the children of a split the cells do not justify. A split needs two representatives (agent ids) in EACH
    child and a distinguishing thread: one linked to some children of the split and not to others."""
    out = {}
    for sp in rule.get("r3_splits", []):
        kids = sp["children"]
        need = sp.get("min_representatives", 2)
        reasons = []
        for kid in kids:
            agents = {r["agent_id"] for r in rows if r["class_id"] == kid and r["agent_id"]}
            if len(agents) < need:
                reasons.append(f"{kid} has {len(agents)} representative agent id(s) in the cells, needs {need}")
        threads = {t for t in {r["thread_id"] for r in rows if r["class_id"] in kids}
                   if 0 < len({r["class_id"] for r in rows if r["thread_id"] == t and r["class_id"] in kids and has_link(r, rule)}) < len(kids)}
        if not threads:
            reasons.append("no thread links some children of the split and not others")
        if reasons:
            for kid in kids:
                out[kid] = f"R3 split {sp['parent']}: " + "; ".join(reasons)
    return out


def unscorable_note(endpoint: str, all_classes: list[str], classes: list[str], failed: dict[str, str]) -> str:
    dropped = [c for c in all_classes if c not in classes]
    return (f"[{endpoint}] not scorable ({len(dropped)} of {len(all_classes)} classes; excluded from every denominator): "
            + ", ".join(f"{c} ({failed[c] if c in failed else 'R1 no link at the minimum tier and directness'})" for c in dropped))


def score_endpoint(rows: list[dict], endpoint: str, rule: dict):
    mine = [r for r in rows if r["endpoint"] == endpoint]
    all_classes = list(rule["classes"])
    v2 = r_rules(rule)
    failed = split_failures(rows, rule) if v2 else {}
    table, notes = [], []
    for window in [POOLED] + list(rule["age_windows"]):
        part = mine if window == POOLED else [r for r in mine if r["age"] == window]
        tag = f"[{endpoint} {window}]"
        classes = all_classes
        part_all = part
        if v2:   # R1 and R3: only classes with a qualifying link (and an unfailed split) are scored, and only they count in the denominators (R2)
            linked = {r["class_id"] for r in part if has_link(r, rule)}
            classes = [c for c in all_classes if c in linked and c not in failed]
            part = [r for r in part if r["class_id"] in classes]
        if not any(r["sign"] == "match" for r in part):
            agg_only = class_scores(part_all, "aggravation")  # aggravation is its own column even where no match exists
            for c in all_classes:
                table.append({"endpoint": endpoint, "window": window, "class_id": c, "rank": "null",
                              **{k: "0" for k in ("score_all", "score_specific", "score_drug_by_genotype",
                                                  "match_keys", "score_per_thread_sum")},
                              "aggravation_score": str(agg_only.get(c, {}).get("score_all", 0)),
                              "rank_per_thread_sum": "null",
                              "neutral_cells": str(sum(r["class_id"] == c and r["sign"] == "neutral" for r in part_all)),
                              "unknown_cells": str(sum(r["class_id"] == c and r["sign"] == "unknown" for r in part_all)),
                              "null_mean": "undefined", "excess": "undefined", "null_ge_fraction": "undefined",
                              "top_set_size": str(len(all_classes)), "informativeness": "0.000",
                              "top_set_label": "not_scorable_null_ordering", "tied_with": "",
                              "score_origin_collapsed": "0", "rank_origin_collapsed": "null",
                              "top_set_same_share": "", "top_set_membership_share": "",
                              **({"scorable": "yes" if c in classes else "no", "scorable_classes": str(len(classes))} if v2 else {})})
            notes.append(f"{tag} not scorable: no class links to any thread here; frozen as a null ordering "
                         f"(all {len(all_classes)} classes tied, informativeness 0)")
            if v2 and window == POOLED and len(classes) < len(all_classes):
                notes.append(unscorable_note(endpoint, all_classes, classes, failed))
            if agg_only:
                notes.append(f"{tag} aggravation-only window: aggravation is printed in its own column "
                             "for " + ",".join(sorted(agg_only)) + "; the match columns stay null and nothing is netted")
            continue
        match, agg, sums = class_scores(part, "match"), class_scores(part, "aggravation"), per_thread_sums(part)
        null, why = null_for(part, classes, rule)
        order = ranked(classes, match, rule["rank_by"])
        rank_sum = {c: i for i, (c, _) in enumerate(sorted(((c, sums.get(c, 0)) for c in classes),
                                                           key=lambda t: (-t[1], t[0])), 1)}
        top = top_set(order)
        k = len(top)
        oc = origin_collapsed_sums(part)
        rank_oc = {c: i for i, (c, _) in enumerate(sorted(((c, oc.get(c, 0)) for c in classes), key=lambda t: (-t[1], t[0])), 1)}
        st = set_stability(part, classes, rule) if k else None
        label = tie_label(k, len(classes), rule["discriminating_top_set_max_share"])
        info = f"{1 - k / len(classes):.3f}" if k else "0.000"
        keys = {c: len({(r["axis"], r["origin_id"]) for r in part if r["class_id"] == c and r["sign"] == "match"})
                for c in classes}
        for place, (cls, score) in enumerate(order, 1):
            tied = [c for c, sc in order if sc == score and c != cls]
            table.append({"endpoint": endpoint, "window": window, "class_id": cls, "rank": str(place),
                          "score_all": str(match.get(cls, {}).get("score_all", 0)),
                          "score_specific": str(match.get(cls, {}).get("score_specific", 0)),
                          "score_drug_by_genotype": str(match.get(cls, {}).get("score_drug_by_genotype", 0)),
                          "aggravation_score": str(agg.get(cls, {}).get("score_all", 0)),
                          "match_keys": str(keys[cls]), "score_per_thread_sum": str(sums.get(cls, 0)),
                          "rank_per_thread_sum": str(rank_sum[cls]),
                          "neutral_cells": str(sum(r["class_id"] == cls and r["sign"] == "neutral" for r in part)),
                          "unknown_cells": str(sum(r["class_id"] == cls and r["sign"] == "unknown" for r in part)),
                          "null_mean": f"{null[cls][0]:.3f}" if null else "undefined",
                          "excess": f"{match.get(cls, {}).get('score_all', 0) - null[cls][0]:.3f}" if null else "undefined",
                          "null_ge_fraction": f"{null[cls][1]:.3f}" if null else "undefined",
                          "top_set_size": str(k), "informativeness": info, "top_set_label": label,
                          "tied_with": ",".join(tied),
                          "score_origin_collapsed": str(oc.get(cls, 0)), "rank_origin_collapsed": str(rank_oc[cls]),
                          "top_set_same_share": f"{st['same'] / st['runs']:.3f}" if st else "",
                          "top_set_membership_share": f"{st['inside'][cls] / st['runs']:.3f}" if st else "",
                          **({"scorable": "yes", "scorable_classes": str(len(classes))} if v2 else {})})
        if v2:
            agg_all = class_scores(part_all, "aggravation")
            for c in all_classes:
                if c not in classes:
                    table.append({"endpoint": endpoint, "window": window, "class_id": c, "rank": "unscorable",
                                  **{k: "0" for k in ("score_all", "score_specific", "score_drug_by_genotype", "match_keys",
                                                      "score_per_thread_sum", "score_origin_collapsed")},
                                  "aggravation_score": str(agg_all.get(c, {}).get("score_all", 0)),
                                  "rank_per_thread_sum": "unscorable", "rank_origin_collapsed": "unscorable",
                                  "neutral_cells": str(sum(r["class_id"] == c and r["sign"] == "neutral" for r in part_all)),
                                  "unknown_cells": str(sum(r["class_id"] == c and r["sign"] == "unknown" for r in part_all)),
                                  "null_mean": "undefined", "excess": "undefined", "null_ge_fraction": "undefined",
                                  "top_set_size": str(k), "informativeness": info, "top_set_label": "unscorable",
                                  "tied_with": "", "top_set_same_share": "", "top_set_membership_share": "",
                                  "scorable": "no", "scorable_classes": str(len(classes))})
            if window == POOLED and len(classes) < len(all_classes):
                notes.append(unscorable_note(endpoint, all_classes, classes, failed))
        notes.append(f"{tag} top set {{{','.join(top)}}} size {k} of {len(classes)}, informativeness {info}: {label}")
        if st:
            members = ", ".join(f"{c} {st['inside'][c] / st['runs']:.0%}" for c in sorted(classes, key=lambda c: (-st["inside"][c], c))
                                if st["inside"][c])
            notes.append(f"{tag} top SET {{{','.join(sorted(st['base']))}}} stays the top set in {st['same']} of {st['runs']} "
                         f"single-cell or all tier +-1 changes; size {st['kmin']}-{st['kmax']}; share of changes with the class inside the top set: {members}")
        oc_top = [c for c, v in sorted(((c, oc.get(c, 0)) for c in classes), key=lambda t: (-t[1], t[0])) if v and v == max(oc.values())]
        if oc and set(oc_top) != set(top):
            notes.append(f"{tag} best axis per origin changes the top set: score_all {{{','.join(top)}}} -> "
                         f"score_origin_collapsed {{{','.join(oc_top)}}}")
        if not null:
            notes.append(f"{tag} null undefined ({why}); no p-value is reported")
        by_sum = [c for c, _ in sorted(((c, sums.get(c, 0)) for c in classes), key=lambda t: (-t[1], t[0]))
                  if sums.get(c, 0) == max(sums.values())]
        if set(by_sum) != set(top):
            notes.append(f"{tag} origin collapse changes the top set: per-thread sum {{{','.join(by_sum)}}} "
                         f"-> origin-collapsed {{{','.join(top)}}}")
        origins = {(r["axis"], r["origin_id"]) for r in part if r["sign"] == "match"}
        if len(origins) == 1:
            notes.append(f"{tag} single origin {sorted(origins)[0][1]} carries every match cell: "
                         "the per-thread sum and the collapsed ranking must both be read")
        if window == POOLED:
            t, keep, total, moved = stability(part, classes, rule)
            notes.append(f"[{endpoint}] top class {t}; kept in {keep} of {total} tier perturbations"
                         + (f"; moved or tied under: {', '.join(moved)}" if moved else "")
                         + ("; secondary: with several classes tied on top this 'top class' is a tie-break artefact, read the top SET lines" if k > 1 else ""))
            notes.append(f"[{endpoint}] {stability_pairs(part, classes, rule)}")
            notes.append(f"[{endpoint}] {agent_ranking(part, t, rule['rank_by'])}")
    return table, notes


def rule_order(root: Path, rule_path: Path, cells_path: Path) -> str:
    """rule committed before the cells: yes | same_commit | not_ancestor | untracked."""
    try:
        rel = [str(p.resolve().relative_to(root)) for p in (rule_path, cells_path)]
        adds = pl.first_adds(root, ".")
        a, b = (adds.get(p) for p in rel)
        if not a or not b:
            return "untracked"
        if a[0] == b[0]:
            return "same_commit"
        return "yes" if pl.git_ok(root, "merge-base", "--is-ancestor", a[0], b[0]) else "not_ancestor"
    except (ValueError, RuntimeError):
        return "untracked"


def run(cells_path: Path, rule_path: Path, out: Path | None, pin: str | None, root: Path) -> int:
    try:
        raw = rule_path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        if pin and pin.lower() != digest:
            raise Invalid(f"rule sha256 {digest} is not the pinned {pin.lower()}")
        rule = json.loads(raw)
        check_rule(rule)
        rows = read_cells(cells_path, rule)
        order = rule_order(root, rule_path, cells_path)
        if order == "not_ancestor":
            raise Invalid("the rule's first commit is not an ancestor of the cells' first commit")
    except (Invalid, OSError, ValueError, csv.Error) as exc:
        print(f"invalid: {exc}", file=sys.stderr)
        return 2
    threads = sorted({r["thread_id"] for r in rows})
    if r_rules(rule):
        print(f"R1 minimum link tier {rule['r1_min_link'][0]} directness {rule['r1_min_link'][1]}; R2 informativeness over the scorable classes; "
              f"R3 splits {len(rule['r3_splits'])}: " + (", ".join(f"{sp['parent']} {'NOT MET' if any(c in split_failures(rows, rule) for c in sp['children']) else 'met'}"
                                                              for sp in rule["r3_splits"]) or "none declared"))
    print(f"rule {rule['rule_version']} sha256 {digest}; rule committed before cells: {order}; "
          f"cells {len(rows)}; rank_by {rule['rank_by']}; permutations {rule['permutations']} seed {rule['seed']}")
    print(f"threads {len(threads)} sha256 {hashlib.sha256(chr(10).join(threads).encode()).hexdigest()}: "
          + ",".join(threads))
    if not rows:
        print("no cells: nothing to score")
        return 0
    table, notes = [], []
    for endpoint in rule["endpoints"]:
        t, n = score_endpoint(rows, endpoint, rule)
        table += t
        notes += n
    cols = out_columns(rule)
    lines = ["\t".join(cols)] + ["\t".join(r[c] for c in cols) for r in table]
    text = "\n".join(lines) + "\n"
    if out:
        out.write_text(text)
        print(f"scores written: {len(table)} rows; endpoints are never summed")
    else:
        sys.stdout.write(text)
    for note in notes:
        print(note)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", default=".", help="repository root (default: current directory)")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sc = sub.add_parser("score", help="score the classes of a cells table under a rule file")
    sc.add_argument("cells")
    sc.add_argument("rule")
    sc.add_argument("--out", help="write the score table here (default: standard output)")
    sc.add_argument("--expect-rule-sha256", help="refuse unless the rule file has exactly this digest")
    args = parser.parse_args(argv)
    return run(Path(args.cells), Path(args.rule), Path(args.out) if args.out else None,
               args.expect_rule_sha256, Path(args.root).resolve())


if __name__ == "__main__":
    sys.exit(main())

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
  endpoint, age, class_id and thread_id in the rule's closed lists; has_* in {yes, no}.
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
  - rank stability: the top class under every single-cell tier +-1 change and the all +-1 change.
An agent ranking is printed only for the top class and only when some (axis, origin) key carries
a match for one agent of that class and not for another.

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
               "score_drug_by_genotype", "aggravation_score", "match_keys", "neutral_cells",
               "unknown_cells", "null_mean", "excess", "null_ge_fraction", "tied_with"]
POOLED = "pooled"


class Invalid(Exception):
    pass


def check_rule(rule: dict) -> None:
    for key in ("rule_version", "tier_rubric", "directness_rubric", "endpoints", "age_windows", "classes",
                "threads", "never_specific_threads", "zero_directness_threads", "rank_by",
                "permutations", "seed"):
        if key not in rule:
            raise Invalid(f"rule lacks {key!r}")
    for rubric in ("tier_rubric", "directness_rubric"):
        if sorted(rule[rubric]) != ["0", "1", "2", "3"] or not all(str(v).strip() for v in rule[rubric].values()):
            raise Invalid(f"{rubric} must describe 0, 1, 2 and 3 in words")
    if not rule["endpoints"] or not all(isinstance(e, str) and e for e in rule["endpoints"]):
        raise Invalid("endpoints must be a non-empty list of names")
    for key in ("endpoints", "age_windows", "classes", "threads"):
        if not rule[key] or len(set(rule[key])) != len(rule[key]):
            raise Invalid(f"{key} must be a non-empty list without repeats")
    for key in ("never_specific_threads", "zero_directness_threads"):
        if not set(rule[key]) <= set(rule["threads"]):
            raise Invalid(f"{key} names a thread that is not in threads")
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
        for req in ("cell_id", "thread_id", "class_id", "endpoint", "age", "axis", "origin_id"):
            if not row[req]:
                raise Invalid(f"{where}: {req} is required")
        if row["cell_id"] in seen:
            raise Invalid(f"{where}: duplicate cell_id")
        seen.add(row["cell_id"])
        if row["sign"] not in SIGNS:
            raise Invalid(f"{where}: sign {row['sign']!r} not in {SIGNS}")
        for col, key in (("endpoint", "endpoints"), ("age", "age_windows"), ("class_id", "classes"),
                         ("thread_id", "threads")):
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


def class_scores(rows: list[dict], sign: str, shift_all: int = 0, shift_cell: tuple[str, int] | None = None):
    """class_id -> {score name -> sum over distinct (axis, origin) of the largest cell value}."""
    best: dict[str, dict[str, dict[tuple, int]]] = {}
    for row in rows:
        if row["sign"] != sign:
            continue
        shift = shift_all + (shift_cell[1] if shift_cell and shift_cell[0] == row["cell_id"] else 0)
        val = value(row, shift)
        key = (row["axis"], row["origin_id"])
        for name, ok in (("score_all", True), ("score_specific", row["has_genotype_contrast"] == "yes"),
                         ("score_drug_by_genotype", row["has_drug_by_genotype"] == "yes")):
            if ok:
                slot = best.setdefault(row["class_id"], {}).setdefault(name, {})
                slot[key] = max(slot.get(key, 0), val)
    return {c: {n: sum(v.values()) for n, v in names.items()} for c, names in best.items()}


def ranked(classes: list[str], scores: dict, by: str) -> list[tuple[str, int]]:
    return sorted(((c, scores.get(c, {}).get(by, 0)) for c in classes), key=lambda t: (-t[1], t[0]))


def permuted(rows: list[dict], seed: int, index: int) -> list[dict]:
    """The match cells with their class labels permuted among themselves (degree preserving)."""
    match = sorted((r for r in rows if r["sign"] == "match"), key=lambda r: r["cell_id"])
    order = sorted(match, key=lambda r: hashlib.sha256(f"{seed}:{index}:{r['cell_id']}".encode()).hexdigest())
    labels = [r["class_id"] for r in match]
    moved = {r["cell_id"]: labels[k] for k, r in enumerate(order)}
    return [dict(r, class_id=moved[r["cell_id"]]) if r["cell_id"] in moved else r for r in rows]


def null_for(rows: list[dict], classes: list[str], rule: dict) -> dict[str, tuple[float, float]]:
    n = rule["permutations"]
    if n == 0 or not any(r["sign"] == "match" for r in rows):
        return {c: (0.0, 0.0) for c in classes}
    observed = class_scores(rows, "match")
    total = {c: 0 for c in classes}
    ge = {c: 0 for c in classes}
    for k in range(n):
        sim = class_scores(permuted(rows, rule["seed"], k), "match")
        for c in classes:
            s = sim.get(c, {}).get("score_all", 0)
            total[c] += s
            ge[c] += s >= observed.get(c, {}).get("score_all", 0)
    return {c: (total[c] / n, ge[c] / n) for c in classes}


def stability(rows: list[dict], classes: list[str], rule: dict) -> tuple[str, int, int, list[str]]:
    by = rule["rank_by"]
    base = ranked(classes, class_scores(rows, "match"), by)
    top = base[0][0]
    tied = [c for c, s in base if s == base[0][1]]
    runs = [("all+1", dict(shift_all=1)), ("all-1", dict(shift_all=-1))]
    runs += [(f"{r['cell_id']}{s:+d}", dict(shift_cell=(r["cell_id"], s)))
             for r in sorted(rows, key=lambda r: r["cell_id"]) if r["sign"] == "match" for s in (1, -1)]
    keep, moved = 0, []
    for label, kw in runs:
        winner = ranked(classes, class_scores(rows, "match", **kw), by)
        if winner[0][0] == top and (len(winner) < 2 or winner[0][1] > winner[1][1]):
            keep += 1
        else:
            moved.append(label)
    return top, keep, len(runs), moved if len(tied) == 1 else moved + [f"tie at baseline: {','.join(tied)}"]


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


def windows_of(rows: list[dict]) -> list[str]:
    return [POOLED] + sorted({r["age"] for r in rows})


def score_endpoint(rows: list[dict], endpoint: str, rule: dict):
    mine = [r for r in rows if r["endpoint"] == endpoint]
    classes = sorted({r["class_id"] for r in mine})
    table, notes = [], []
    for window in windows_of(mine):
        part = mine if window == POOLED else [r for r in mine if r["age"] == window]
        match, agg = class_scores(part, "match"), class_scores(part, "aggravation")
        null = null_for(part, classes, rule)
        keys = {c: len({(r["axis"], r["origin_id"]) for r in part if r["class_id"] == c and r["sign"] == "match"})
                for c in classes}
        order = ranked(classes, match, rule["rank_by"])
        for place, (cls, score) in enumerate(order, 1):
            tied = [c for c, s in order if s == score and c != cls]
            table.append({"endpoint": endpoint, "window": window, "class_id": cls, "rank": str(place),
                          "score_all": str(match.get(cls, {}).get("score_all", 0)),
                          "score_specific": str(match.get(cls, {}).get("score_specific", 0)),
                          "score_drug_by_genotype": str(match.get(cls, {}).get("score_drug_by_genotype", 0)),
                          "aggravation_score": str(agg.get(cls, {}).get("score_all", 0)),
                          "match_keys": str(keys[cls]),
                          "neutral_cells": str(sum(r["class_id"] == cls and r["sign"] == "neutral" for r in part)),
                          "unknown_cells": str(sum(r["class_id"] == cls and r["sign"] == "unknown" for r in part)),
                          "null_mean": f"{null[cls][0]:.3f}",
                          "excess": f"{match.get(cls, {}).get('score_all', 0) - null[cls][0]:.3f}",
                          "null_ge_fraction": f"{null[cls][1]:.3f}", "tied_with": ",".join(tied)})
        if window == POOLED and any(r["sign"] == "match" for r in part):
            top, keep, total, moved = stability(part, classes, rule)
            notes.append(f"[{endpoint}] top class {top}; kept in {keep} of {total} tier perturbations"
                         + (f"; moved or tied under: {', '.join(moved)}" if moved else ""))
            notes.append(f"[{endpoint}] {agent_ranking(part, top, rule['rank_by'])}")
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
    print(f"rule {rule['rule_version']} sha256 {digest}; rule committed before cells: {order}; "
          f"cells {len(rows)}; rank_by {rule['rank_by']}; permutations {rule['permutations']} seed {rule['seed']}")
    if not rows:
        print("no cells: nothing to score")
        return 0
    table, notes = [], []
    for endpoint in rule["endpoints"]:
        if any(r["endpoint"] == endpoint for r in rows):
            t, n = score_endpoint(rows, endpoint, rule)
            table += t
            notes += n
    lines = ["\t".join(OUT_COLUMNS)] + ["\t".join(r[c] for c in OUT_COLUMNS) for r in table]
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

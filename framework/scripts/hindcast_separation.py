#!/usr/bin/env python3
"""Hindcast component separation: AUC, exact permutation p and an interval per component at small n. Numbers only: it never says pass or fail.

    python3 framework/scripts/hindcast_separation.py SCORES.tsv LABELS.tsv [--identified IDENT.tsv]

SCORES.tsv: id, c1..c4 (0, 1, 2 or `unknown`, which is scored 0 as the scorer sheet says), saved by the blind scorer BEFORE the labels are opened.
LABELS.tsv: id, label (POS or NEG), the analyst's file; this tool never opens the key. IDENT.tsv (optional): id, answer (identified, partly, not).
Per component and for the unweighted sum: AUC (POS against NEG, ties one half), exact one-sided permutation p over every arrangement of the labels,
a seeded percentile bootstrap interval within each label (10,000 resamples, seed 20261119; too narrow at 6 against 6) and the leave-one-pair-out AUC range.
Reading rule (ADV-093, scorer sheet section 8): "no separation shown" is not "does not separate". Not medical advice; not a probability of benefit; no weights, no threshold search.
Exit codes: 0 printed, 2 invalid input.
"""
from __future__ import annotations
import csv, itertools, random, re, sys
from pathlib import Path

SEED, RESAMPLES, MAX_N = 20261119, 10000, 20


def read(path: str) -> list[dict[str, str]]:
    with open(path, newline="") as handle:
        return [{k: (v or "").strip() for k, v in row.items()} for row in csv.DictReader(handle, delimiter="\t")]


def auc(pos: list[float], neg: list[float]) -> float:
    return sum(1.0 if p > q else 0.5 if p == q else 0.0 for p in pos for q in neg) / (len(pos) * len(neg))


def exact_p(values: list[float], k: int, observed: float) -> float:
    """One-sided: the share of the C(n, k) label arrangements whose AUC is at least the observed one."""
    n, hits, total = len(values), 0, 0
    for chosen in itertools.combinations(range(n), k):
        picked = set(chosen)
        a = auc([values[i] for i in picked], [values[i] for i in range(n) if i not in picked])
        hits += a >= observed - 1e-12
        total += 1
    return hits / total


def interval(pos: list[float], neg: list[float]) -> tuple[float, float]:
    rng = random.Random(SEED)
    draws = sorted(auc([rng.choice(pos) for _ in pos], [rng.choice(neg) for _ in neg]) for _ in range(RESAMPLES))
    return draws[int(0.025 * RESAMPLES)], draws[int(0.975 * RESAMPLES) - 1]


def report(name: str, pos: list[float], neg: list[float]) -> str:
    a = auc(pos, neg)
    lo, hi = interval(pos, neg)
    loo = [auc(pos[:i] + pos[i + 1:], neg) for i in range(len(pos))] + [auc(pos, neg[:j] + neg[j + 1:]) for j in range(len(neg))]
    return (f"{name}: AUC {a:.3f} ({len(pos)} POS, {len(neg)} NEG); exact one-sided permutation p {exact_p(pos + neg, len(pos), a):.4f}; "
            f"bootstrap interval [{lo:.3f}, {hi:.3f}] (too narrow at this n); leave-one-pair-out range [{min(loo):.3f}, {max(loo):.3f}]")


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[0] in ("-h", "--help") or (len(argv) > 2 and argv[2] != "--identified"):
        print(__doc__)
        return 0 if argv and argv[0] in ("-h", "--help") else 2
    try:
        scores = {r["id"]: r for r in read(argv[0])}
        labels = {r["id"]: r["label"].upper() for r in read(argv[1])}
        cols = sorted(c for c in next(iter(scores.values())) if re.fullmatch(r"c\d+", c))
        assert cols and set(scores) == set(labels) and set(labels.values()) <= {"POS", "NEG"} and len(labels) <= MAX_N, "ids differ, a label is not POS/NEG, no cN column or n above %d" % MAX_N
        val = {i: [0 if scores[i][c].lower() == "unknown" else int(scores[i][c]) for c in cols] for i in scores}
        assert all(0 <= v <= 2 for row in val.values() for v in row), "a component value is outside 0 to 2"
        ids_pos = [i for i in labels if labels[i] == "POS"]
        ids_neg = [i for i in labels if labels[i] == "NEG"]
        assert ids_pos and ids_neg, "both labels are needed"
    except (OSError, KeyError, ValueError, AssertionError, StopIteration) as exc:
        print(f"invalid input: {exc}", file=sys.stderr)
        return 2
    for j, c in enumerate(cols):
        print(report(c.upper(), [val[i][j] for i in ids_pos], [val[i][j] for i in ids_neg]))
    print(report("SUM (unweighted)", [sum(val[i]) for i in ids_pos], [sum(val[i]) for i in ids_neg]))
    if len(argv) == 4:
        ans = [r["answer"].lower() for r in read(argv[3])]
        n_id = sum(a == "identified" for a in ans)
        print(f"identification probe: {n_id} identified, {sum(a == 'partly' for a in ans)} partly, of {len(ans)}" + ("; AT LEAST HALF IDENTIFIED: contaminated, read the separation as recall" if len(ans) and 2 * n_id >= len(ans) else ""))
    print("No pass or fail. 'No separation shown' is not 'does not separate'. A convenience set with skew and a model scorer that may remember outcomes; a component added after the freeze is post hoc.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

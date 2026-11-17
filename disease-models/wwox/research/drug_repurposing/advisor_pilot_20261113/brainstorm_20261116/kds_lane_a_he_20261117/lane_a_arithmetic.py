#!/usr/bin/env python3
"""Lane A (ADV-031): reproduce the arithmetic of the operator's ketamine input. Standard library only; prints each figure next to the value the input states."""
from __future__ import annotations

import argparse
from math import comb, exp, log, sqrt

Z = 1.959963984540054


def wilson(k: int, n: int) -> tuple[float, float]:
    p = k / n
    den = 1 + Z * Z / n
    centre = (p + Z * Z / (2 * n)) / den
    half = Z * sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / den
    return 100 * (centre - half), 100 * (centre + half)


def fisher_two_sided(a: int, b: int, c: int, d: int) -> float:
    n, r1, c1 = a + b + c + d, a + b, a + c
    prob = lambda x: comb(r1, x) * comb(n - r1, c1 - x) / comb(n, c1)  # noqa: E731
    p0 = prob(a)
    return sum(prob(x) for x in range(max(0, c1 - (n - r1)), min(r1, c1) + 1) if prob(x) <= p0 * (1 + 1e-9))


def main() -> int:
    argparse.ArgumentParser(description=__doc__).parse_args()
    lo, hi = wilson(24, 30)
    print(f"Wilson 95% CI 24/30: {lo:.1f} to {hi:.1f} percent (input: 62.7 to 90.5)")
    lo, hi = wilson(21, 27)
    print(f"Wilson 95% CI 21/27 (Kuki 15/18 plus Rosati 6/9, the two series whose abstracts state a response): {lo:.1f} to {hi:.1f} percent, point {100 * 21 / 27:.1f}")
    print(f"Fisher exact 6/6 versus 0/3 (two-sided): p = {fisher_two_sided(6, 0, 0, 3):.4f} (input: 0.0119)")
    a, n1, c, n2 = 9, 27, 2, 27
    p1, p2 = a / n1, c / n2
    rd = p1 - p2
    se = sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    print(f"memantine 9/27 versus 2/27: risk difference {100 * rd:.2f} percent, Wald 95% CI {100 * (rd - Z * se):.2f} to {100 * (rd + Z * se):.2f} (input: +25.9, +5.6 to +46.3)")
    l1, u1 = wilson(a, n1)
    l2, u2 = wilson(c, n2)
    p1c, p2c = 100 * p1, 100 * p2
    print(f"  Newcombe hybrid-score CI: {100 * rd - sqrt((p1c - l1) ** 2 + (u2 - p2c) ** 2):.2f} to {100 * rd + sqrt((u1 - p1c) ** 2 + (p2c - l2) ** 2):.2f}")
    odds = a * (n2 - c) / ((n1 - a) * c)
    se_l = sqrt(1 / a + 1 / (n1 - a) + 1 / c + 1 / (n2 - c))
    print(f"  odds ratio {odds:.2f}, Woolf 95% CI {exp(log(odds) - Z * se_l):.2f} to {exp(log(odds) + Z * se_l):.2f} (input: 6.25)")
    print(f"  NNT {1 / rd:.2f} (input: 3.9); from the Wald CI limits: {1 / (rd + Z * se):.1f} to {1 / (rd - Z * se):.1f}")
    print(f"  unpaired Fisher exact two-sided p = {fisher_two_sided(9, 18, 2, 25):.4f} (input: 0.0394)")
    print("  paired analysis: only the margins are known (9 responders on memantine, 2 on placebo, 27 patients); the exact McNemar two-sided p over the three possible tables:")
    for both in (0, 1, 2):
        b, cc = 9 - both, 2 - both
        m = b + cc
        p = min(1.0, 2 * sum(comb(m, k) for k in range(min(b, cc) + 1)) / 2 ** m)
        print(f"    responders on both arms {both}: memantine-only {b}, placebo-only {cc}, p = {p:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

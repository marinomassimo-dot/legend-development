#!/usr/bin/env python3
"""Exact arithmetic for the discriminating design. (1) Fisher exact (two-sided) on the published
burst counts (Breton 2021: KO 36/42, HT 4/23, WT 0/11; slices as units, as published: animals not
separable). (2) Exact power of a one-sided Fisher test for two proportions p1 > p2 at n per arm
(slices as units; with clustering by animal the true power is lower: a design assumption, stated).
Pure python, deterministic. Usage: design_counts.py <out.txt>"""
import sys
from math import comb
def hyp_p(a, n1, n2, k):
    # P(X=a) hypergeometric: choose k successes among n1+n2, a in group 1
    return comb(n1, a) * comb(n2, k - a) / comb(n1 + n2, k)
def fisher_two_sided(a, n1, c, n2):
    k = a + c; p0 = hyp_p(a, n1, n2, k); s = 0.0
    for x in range(max(0, k - n2), min(n1, k) + 1):
        p = hyp_p(x, n1, n2, k)
        if p <= p0 * (1 + 1e-12): s += p
    return s
def fisher_one_sided_greater(a, n1, c, n2):
    k = a + c
    return sum(hyp_p(x, n1, n2, k) for x in range(a, min(n1, k) + 1))
def binom_pmf(n, p, x): return comb(n, x) * p**x * (1 - p)**(n - x)
def power(n, p1, p2, alpha=0.05):
    pw = 0.0
    for a in range(n + 1):
        for c in range(n + 1):
            if fisher_one_sided_greater(a, n, c, n) <= alpha:
                pw += binom_pmf(n, p1, a) * binom_pmf(n, p2, c)
    return pw
def main():
    if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__); return 0 if len(sys.argv) > 1 else 2
    L = []
    L.append("published counts (slices): KO 36/42, HT 4/23, WT 0/11")
    L.append(f"Fisher two-sided KO vs HT: p = {fisher_two_sided(36,42,4,23):.3g}")
    L.append(f"Fisher two-sided HT vs WT: p = {fisher_two_sided(4,23,0,11):.3g}")
    L.append("exact power, one-sided Fisher alpha 0.05, n slices per arm (independent slices assumed):")
    for (p1, p2) in [(0.60, 0.17), (0.80, 0.17), (0.60, 0.05), (0.86, 0.17)]:
        row = [f"n={n}:{power(n,p1,p2):.2f}" for n in (6, 8, 10, 12, 16, 20)]
        L.append(f"  p1={p1} vs p2={p2}  " + "  ".join(row))
    open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L)); return 0
if __name__ == "__main__": sys.exit(main())

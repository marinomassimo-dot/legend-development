#!/usr/bin/env python3
"""Dated addendum 2026-11-11 (after V5), NOT part of the preregistered grid: pool sizes taken from native knock-out data held in the verified tables.
TASK-1/3 pool: Yao 2017 (28276488), holding current at -60 mV 58.4 -> 43.3 pA in TASK-1/3 double knock-out, so a 0.26 share of the holding current (INFERENZA: current at -60 mV, not conductance; layer V, P9-15, room temperature; compensation possible).
TREK-1 pool: Labbaf 2025 (40998695), Rin of persistent-firing S1 layers 2-4 pyramidal neurons 121.4 (WT, n 16) -> 257.2 MOhm (knock-out, n 33); conductance share removed = 1 - 121.4/257.2 = 0.53 (INFERENZA: adult, selected firing class, constitutive knock-out, compensation possible).
Writes size_check_pools.tsv: loss L = pool * closure(pH50, n, pH0, d) against the Wwox 0.28."""
import csv, pathlib
HERE = pathlib.Path(__file__).resolve().parent
def o(ph, p50, n): return 1 / (1 + 10 ** (n * (p50 - ph)))
def f(ph0, d, p50, n): return 1 - o(ph0 - d, p50, n) / o(ph0, p50, n)
POOLS = [("TASK-1/3 (Yao KO, holding current)", 0.26, [("TASK-1", 7.3), ("TASK-1", 7.4), ("TASK-1", 6.6), ("TASK-3", 6.47), ("TASK-3", 6.9)]),
         ("TREK-1 (Labbaf KO, Rin)", round(1 - 121.4 / 257.2, 2), [("TREK-1", 7.5)])]
rows = []
for name, pool, chans in POOLS:
    for ch, p50 in chans:
        for ph0 in (7.2, 7.4):
            for n in (0.7, 1, 2):
                for d in (0.1, 0.2, 0.3):
                    fc = f(ph0, d, p50, n); rows.append([name, pool, ch, p50, ph0, n, d, round(fc, 3), round(pool * fc, 3), "yes" if pool * fc >= 0.28 else "no"])
with open(HERE / "size_check_pools.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["pool_source", "pool_share", "channel", "pH50", "pH0", "hill_n", "delta_pH", "closure_f", "loss_L", "reaches_0.28"]); w.writerows(rows)
for r in rows:
    if r[2] == "TREK-1" and r[6] in (0.2, 0.3): print(r)
print("max L TASK pool:", max(r[8] for r in rows if r[0].startswith("TASK")), " max L TREK pool:", max(r[8] for r in rows if r[0].startswith("TREK")))
print("min d reaching 0.28, TREK-1:", sorted({(r[4], r[5], r[6]) for r in rows if r[2] == "TREK-1" and r[9] == "yes"}))

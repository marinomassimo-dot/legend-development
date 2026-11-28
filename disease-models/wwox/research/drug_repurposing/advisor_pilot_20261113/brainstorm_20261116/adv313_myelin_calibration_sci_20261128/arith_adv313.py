#!/usr/bin/env python3
"""ADV-313 arithmetic: natural-log ratios (treated or mutant over control) and Spearman rank agreement.
Inputs are the numbers listed in CALIBRATION_TABLE_ADV313; labels carry paper, figure or table, panel and row."""
from math import log
from itertools import product

def ln(a, b):  # treated, control
    return log(a / b)

# (structure_treated, structure_control, conduction_treated, conduction_control); speed form, slower = negative
V = {
 # ADV-312 rows, unchanged
 'Palma axon-count': (249, 287, 0.425, 0.504), 'Palma g small': (0.787, 0.768, 0.425, 0.504),
 'Crawford10 thick EAE/normal': (0.027, 0.060, 1.69, 1.82), 'Crawford10 g EAE/normal': (0.94, 0.87, 1.69, 1.82),
 'Crawford10 thick ligand/EAE': (0.065, 0.027, 1.92, 1.69), 'Crawford10 g ligand/EAE': (0.85, 0.94, 1.92, 1.69),
 'Nr2f1 g': (0.63, 0.74, 12.38, 15.79),  # latency ratio inverted: speed = 1/latency
 # new, ADV-313
 'STZ thick lumbar': (0.33, 0.42, 12.9, 16.7), 'STZ g lumbar': (0.72, 0.62, 12.9, 16.7),
 'STZ thick cervical': (0.38, 0.54, 14.3, 14.7), 'STZ g cervical': (0.66, 0.65, 14.3, 14.7),
 'CPZ pct-myelinated +0.16': (10.4, 37.3, 0.507, 0.489), 'CPZ pct-myelinated -1.59': (3.4, 29.7, 0.517, 0.511),
 'CPZ g -1.59': (0.85, 0.73, 0.517, 0.511),
 'L-NIO myelinated-number': (67, 101, 0.43, 0.49),
 'Dutta g': (0.764, 0.717, 0.796, 1.0),  # CV reduced 20.4 percent
 'Fig4 pct-myelinated Olig2Cre': (12, 79, 0.6, 1.9), 'Fig4 pct-myelinated SynCre': (9, 79, 0.7, 1.9),
 'Fig4 g Olig2Cre': (0.868, 0.815, 0.6, 1.9), 'Fig4 g SynCre': (0.855, 0.815, 0.7, 1.9),
}
print('contrast | ln structure | ln speed | |s|/|c|')
for k, (st, sc, ct, cc) in V.items():
    s, c = ln(st, sc), ln(ct, cc)
    print(f'{k} | {s:+.3f} | {c:+.3f} | {abs(s)/abs(c):.2f}')

def rank(x):
    o = sorted(range(len(x)), key=lambda i: x[i]); r = [0.0] * len(x); i = 0
    while i < len(o):
        j = i
        while j + 1 < len(o) and x[o[j + 1]] == x[o[i]]: j += 1
        for k in range(i, j + 1): r[o[k]] = (i + j) / 2 + 1
        i = j + 1
    return r

def rho(keys):
    a = rank([abs(ln(V[k][0], V[k][1])) for k in keys]); b = rank([abs(ln(V[k][2], V[k][3])) for k in keys])
    n = len(a); ma = sum(a) / n; mb = sum(b) / n
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    return num / (sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b)) ** 0.5

def spread(name, choices, drop=None):
    out = [rho(list(c)) for c in product(*choices) if True]
    print(f'{name}: combinations {len(out)}, rho min {min(out):+.2f}, max {max(out):+.2f}, '
          f'rho>=0.7 in {sum(r >= 0.7 for r in out)}, |rho|<0.5 in {sum(abs(r) < 0.5 for r in out)}')

HEAD = [['Palma axon-count'], ['Crawford10 thick EAE/normal', 'Crawford10 thick ligand/EAE'], ['Nr2f1 g'],
        ['STZ thick lumbar', 'STZ g lumbar', 'STZ thick cervical'],
        ['CPZ pct-myelinated +0.16', 'CPZ pct-myelinated -1.59', 'L-NIO myelinated-number'], ['Dutta g'], ['Fig4 pct-myelinated Olig2Cre', 'Fig4 pct-myelinated SynCre']]
GRAT = [['Palma g small'], ['Crawford10 g EAE/normal', 'Crawford10 g ligand/EAE'], ['Nr2f1 g'],
        ['STZ g lumbar', 'STZ g cervical'], ['CPZ g -1.59'], ['Dutta g'], ['Fig4 g Olig2Cre', 'Fig4 g SynCre']]
spread('headline-variable set (7 sources)', HEAD)
spread('g-ratio class (7 sources)', GRAT)
print('\nfirst-listed choices:')
for n, ch in (('headline', HEAD), ('g-ratio', GRAT)):
    keys = [c[0] for c in ch]; print(n, f'{rho(keys):+.2f}')
    for i in range(len(keys)): print('  leave out', keys[i], f'{rho(keys[:i] + keys[i+1:]):+.2f}')

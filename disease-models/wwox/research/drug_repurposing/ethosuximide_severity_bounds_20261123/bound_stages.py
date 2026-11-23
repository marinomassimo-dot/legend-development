"""Partial identification of measured minutes using integer Racine scores and group moments."""
import csv
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations_with_replacement
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / 'fig7_quant_ethosuximide_lithium_sci_20261115' / 'output'
OUT = HERE / 'results'
ARMS = ('PTZ', 'PTZ+ETS')
ENDPOINTS = ('clonic_or_death', 'generalized_or_death', 'clonic_excluding_death')
WINDOWS = ((1,10), (11,30), (31,60))
SCENARIOS = {
    'primary': ((6,), .085, .10, True),
    'mean_only': ((6,), .085, .10, False),
    'wider': ((6,), .17, .20, True),
    'among_scored_n3_to_6': ((3,4,5,6), .085, .10, True),
}


def read(name):
    with (DATA/name).open() as stream:
        return list(csv.DictReader(stream, delimiter='\t'))


def write(name, header, rows):
    with (OUT/name).open('w', newline='') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(header)
        writer.writerows(rows)


@lru_cache(maxsize=None)
def catalogue(sizes):
    arms = []
    for n in sizes:
        x = np.asarray(list(combinations_with_replacement(range(7), n)))
        arms.append(np.column_stack([x.mean(axis=1), x.std(axis=1, ddof=1)/np.sqrt(n),
                                     (x>=3).mean(axis=1), (x>=5).mean(axis=1),
                                     ((x>=3)&(x<=5)).mean(axis=1)]))
    return np.concatenate(arms)


def compatible(readings, sizes, mean_tol, sem_tol, use_sem=True):
    full = catalogue(sizes)
    if not readings:
        return 'missing', full
    means = [m for m, _ in readings]
    rows = full[(full[:,0] >= min(means)-mean_tol) & (full[:,0] <= max(means)+mean_tol)]
    if not len(rows):
        return 'no_integer_mean', full
    if not use_sem:
        return 'mean_only', rows
    lo = min(sem for _, sem in readings) - sem_tol
    hi = max(sem if sem > 0 else .2 for _, sem in readings) + sem_tol
    active = rows[(rows[:,1] >= lo) & (rows[:,1] <= hi)]
    return ('joint', active) if len(active) else ('no_joint_use_mean', rows)


def main():
    OUT.mkdir(exist_ok=True)
    inputs = defaultdict(list)
    for rendering in ('pdf','png'):
        for row in read(f'fig7b_raster_{rendering}.tsv'):
            if row['genotype']=='-/-' and row['arm'] in ARMS and row['flag']=='ok':
                inputs[row['arm'], float(row['minute'])].append((float(row['mean_stage_raw']), float(row['sem_up_stage'])))
    minute_rows, window_rows = [], []
    for scenario, settings in SCENARIOS.items():
        bounds, methods = {}, {}
        for minute in range(1,61):
            for arm in ARMS:
                method, possible = compatible(inputs[arm, minute], *settings)
                methods[arm,minute] = method
                bounds[arm,minute] = possible[:,2:].min(axis=0), possible[:,2:].max(axis=0)
                for j, endpoint in enumerate(ENDPOINTS):
                    lo, hi = bounds[arm,minute]
                    minute_rows.append((scenario, minute, arm, endpoint, method, len(possible), lo[j], hi[j]))
        for first,last in WINDOWS:
            minutes = range(first,last+1)
            statuses = Counter(methods[a,m] for a in ARMS for m in minutes)
            # Arms and minutes can vary independently; longitudinal constraints could tighten these bounds.
            gap_lo = np.mean([bounds[ARMS[0],m][0]-bounds[ARMS[1],m][1] for m in minutes], axis=0)
            gap_hi = np.mean([bounds[ARMS[0],m][1]-bounds[ARMS[1],m][0] for m in minutes], axis=0)
            for j, endpoint in enumerate(ENDPOINTS):
                window_rows.append((scenario, first, last, endpoint, gap_lo[j], gap_hi[j],
                                    *[statuses[k] for k in ('joint','no_joint_use_mean','mean_only','missing','no_integer_mean')]))
    controls = defaultdict(Counter)
    for r in read('fig7d_vector_points.tsv'):
        if r['genotype']!='-/-' or r['arm'] not in ('PTZ','PTZ+LiCl'):
            continue
        n = 6 if r['arm']=='PTZ' else 7
        status,_ = compatible([(float(r['mean_stage']),float(r['bar_up_stage']))],(n,),.02,.02)
        controls[r['arm']][status] += 1
    write('minute_bounds.tsv', 'scenario minute arm outcome constraint feasible_histograms min_fraction max_fraction'.split(), minute_rows)
    write('window_bounds.tsv', 'scenario first_min last_min outcome lower_gap upper_gap joint_arm_minutes dropped_sem mean_only missing no_integer_mean'.split(), window_rows)
    write('vector_check.tsv', ['arm','constraint','points'], [(a,k,v) for a,by in controls.items() for k,v in by.items()])


if __name__ == '__main__':
    main()

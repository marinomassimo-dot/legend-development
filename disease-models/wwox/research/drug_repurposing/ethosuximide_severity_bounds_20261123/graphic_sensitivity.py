"""Audit tolerances on a separate vector/raster panel and bound late-phase reading errors."""
import csv
from collections import defaultdict
import numpy as np
from bound_stages import ARMS, OUT, read, write


def compare_renderings():
    def key(r):
        return r['arm'], round(float(r['minute'])*2)/2
    exact = {key(r): (float(r['mean_stage']), float(r['bar_up_stage']))
             for r in read('fig7d_vector_points.tsv') if r['genotype']=='-/-'}
    errors = defaultdict(list)
    for r in read('fig7d_raster_png.tsv'):
        if r['genotype'] != '-/-' or r['flag'] != 'ok' or key(r) not in exact:
            continue
        mu, se = exact[key(r)]
        reported = float(r['sem_up_stage'])
        sem_error = abs(se-reported) if reported else max(0, se-.20)
        errors[r['arm']].append((abs(mu-float(r['mean_stage_raw'])),sem_error))
    rows = []
    for arm, pairs in sorted(errors.items()):
        mean_err, sem_err = np.array(pairs).T
        for label, mean_tol, sem_tol in [('primary',.085,.10), ('wider',.17,.20)]:
            means, sems = mean_err <= mean_tol, sem_err <= sem_tol
            rows.append((arm,label,len(pairs),sum(means),sum(sems),sum(means&sems),
                         np.median(mean_err), np.median(sem_err), max(mean_err), max(sem_err)))
    return rows


def contamination():
    with (OUT/'minute_bounds.tsv').open() as stream:
        rows = [r for r in csv.DictReader(stream,delimiter='\t') if r['scenario']=='primary' and int(r['minute'])>=31]
    results = []
    for endpoint in sorted({r['outcome'] for r in rows}):
        relevant = [r for r in rows if r['outcome']==endpoint]
        losses, net = [], 0
        for r in relevant:
            if r['arm']==ARMS[0]:
                lower = float(r['min_fraction'])
                net += lower
                losses.append(lower)
            else:
                upper = float(r['max_fraction'])
                net -= upper
                losses.append(1-upper)
        losses.sort(reverse=True)
        for k in range(len(losses)+1):
            results.append((endpoint,k,(net-sum(losses[:k]))/30))
    return results


if __name__ == '__main__':
    write('cross_panel_errors.tsv','arm scenario readable mean_covered sem_covered both_covered '
          'median_abs_mean_err median_sem_interval_err max_abs_mean_err max_sem_interval_err'.split(), compare_renderings())
    write('late_error_budget.tsv',['outcome','extra_unconstrained_arm_minutes','worst_case_lower_gap'], contamination())

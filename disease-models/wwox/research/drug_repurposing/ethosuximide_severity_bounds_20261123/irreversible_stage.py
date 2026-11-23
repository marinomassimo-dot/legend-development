"""Sharp bounds for a fixed cohort when stage 6 persists after death."""
from collections import defaultdict
import numpy as np
from bound_stages import ARMS, ENDPOINTS, SCENARIOS, compatible, read, write


def arm_bounds(readings, arm, settings, first):
    # The state is the number dead; every other stage may change arbitrarily.
    lower = np.full((7,len(ENDPOINTS)),np.inf)
    upper = np.full_like(lower,-np.inf)
    lower[0] = upper[0] = 0
    for t in range(first,61):
        _, feasible = compatible(readings[arm,t], *settings)
        dead = np.rint(6*(feasible[:,2]-feasible[:,4])).astype(int)
        low_next = np.full_like(lower,np.inf)
        high_next = np.full_like(upper,-np.inf)
        for d in np.unique(dead):
            local = np.rint(6*feasible[dead==d,2:]) if t>=31 else np.zeros((1,3))
            low_next[d] = lower[:d+1].min(axis=0) + local.min(axis=0)
            high_next[d] = upper[:d+1].max(axis=0) + local.max(axis=0)
        lower,upper = low_next,high_next
    lo, hi = lower.min(axis=0), upper.max(axis=0)
    return (lo,hi) if np.isfinite(lo).all() else None


def main():
    readings = defaultdict(list)
    for rendering in ('pdf','png'):
        for r in read(f'fig7b_raster_{rendering}.tsv'):
            if r['genotype']=='-/-' and r['arm'] in ARMS and r['flag']=='ok':
                readings[r['arm'],float(r['minute'])].append((float(r['mean_stage_raw']),float(r['sem_up_stage'])))
    rows=[]
    for scenario in ('primary','wider','mean_only'):
        for first in (31,1):
            arms = [arm_bounds(readings, a, SCENARIOS[scenario], first) for a in ARMS]
            for j, endpoint in enumerate(ENDPOINTS):
                if any(a is None for a in arms):
                    rows.append((scenario, first, endpoint, 'no_compatible_path', *(['NA']*6)))
                    continue
                (pl,ph),(tl,th) = arms
                rows.append((scenario,first,endpoint,'feasible',pl[j],ph[j],tl[j],th[j],
                             (pl[j]-th[j])/180,(ph[j]-tl[j])/180))
    write('irreversible_stage.tsv', 'scenario start_constraints_minute outcome status PTZ_low_count PTZ_high_count '
          'treated_low_count treated_high_count lower_gap upper_gap'.split(), rows)


if __name__ == '__main__':
    main()

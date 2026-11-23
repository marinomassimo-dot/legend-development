"""Reimplementation of Phillips et al. (2026) Fig. 3A with final Table 2 rates.
Topology checked against CaPlaneNMDARwMem.mod in Zenodo 18262690 (CC BY 4.0).
Rates are in seconds and micromolar. The last augmented coordinate integrates open time.
"""
import csv
from functools import lru_cache
import sys

import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq


@lru_cache(maxsize=256)
def generator(glutamate, memantine, calcium):
    states = [(ca, drug, name) for ca in ([0, 1] if calcium else [0])
              for drug in ([0, 1] if memantine else [0])
              for name in (["R", "AR", "A2R", "O", "D", "CDD"] if ca else ["R", "AR", "A2R", "O", "D"])]
    index = {state: n for n, state in enumerate(states)}
    matrix = np.zeros((len(states)+1, len(states)+1))
    def pair(src, dest, forward, reverse):
        i, j = index[src], index[dest]
        matrix[j,i] += forward
        matrix[i,i] -= forward
        matrix[i,j] += reverse
        matrix[j,j] -= reverse
    for ca, drug, name in states:
        if name == "R":
            pair((ca,drug,"R"), (ca,drug,"AR"), 10 * glutamate, 25)
            pair((ca,drug,"AR"), (ca,drug,"A2R"), 5 * glutamate, 50)
            pair((ca,drug,"A2R"), (ca,drug,"O"), 71, 305)
            pair((ca,drug,"A2R"), (ca,drug,"D"), 0.520 if drug else 0.135, 0.243)
            if ca:
                pair((ca,drug,"A2R"), (ca,drug,"CDD"), 1.75 if drug else 0.737, 0.304 if drug else 0.692)
            if not drug and memantine:
                pair((ca,0,"O"), (ca,1,"O"), 30 * memantine, 143)
            if not drug:
                matrix[-1, index[ca,drug,"O"]] = 1
        if not ca and calcium:
            pair((0,drug,name), (1,drug,name), 1e6*calcium, 82000)
    assert np.max(np.abs(matrix[:-1,:].sum(axis=0))) < 1e-8
    return matrix, states


@lru_cache(maxsize=700)
def evolution(glutamate, drug, calcium, seconds):
    return expm(generator(glutamate, drug, calcium)[0] * seconds)


def stationary(matrix, discrete=False):
    a = matrix.copy()
    if discrete:
        a -= np.eye(len(a))
    a[-1] = 1
    target = np.zeros(len(a))
    target[-1] = 1
    probability = np.linalg.solve(a, target)
    if probability.min() < -1e-7:
        raise ValueError("Invalid probability")
    return probability


def charge(period, span, pulses, drug, calcium, even, width=.002, pulse_glu=1000., baseline_glu=0.):
    on = evolution(pulse_glu, drug, calcium, width)
    gap = period/pulses if even else (span-width)/(pulses-1)
    if gap < width:
        raise ValueError("Pulses overlap")
    between = evolution(baseline_glu, drug, calcium, gap-width)
    last_gap = period - ((pulses-1)*gap+width)
    cycle = evolution(baseline_glu, drug, calcium, last_gap) @ on @ np.linalg.matrix_power(between@on, pulses-1)
    assert np.max(np.abs(cycle[:-1,:-1].sum(axis=0) - 1)) < 3e-7
    steady = stationary(cycle[:-1,:-1], True)
    q_cycle = cycle[-1,:-1]
    _, states = generator(0.,drug,calcium)
    initial = np.zeros(len(states))
    bound = calcium/(calcium+.082)
    initial[states.index((0,0,"R"))] = 1-bound
    if calcium:
        initial[states.index((1,0,"R"))] = bound
    return np.array([q_cycle @ initial, q_cycle @ steady])


def constant_rate(drug, calcium):
    m, _ = generator(1000., drug, calcium)
    return m[-1,:-1] @ stationary(m[:-1,:-1])


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(["period_s","cluster_span_s","pulses","drug_uM","cytosolic_Ca_uM",
                     "cluster_first_pct","even_first_pct","cluster_minus_even_first_pp",
                     "cluster_periodic_pct","even_periodic_pct","cluster_minus_even_periodic_pp"])
    settings = [(26.2,0.66,5),(26.2,0.53,5),(26.2,1.06,5),(60/0.84,0.66,5),
                (26.2,0.66,15),(26.2,0.66,33)]
    for period,span,pulses in settings:
        for calcium in (0.,0.1,10.):
            for drug in (.36,1.,10.):
                blocks = []
                for even in (False,True):
                    q0 = charge(period,span,pulses,0.,calcium,even)
                    q = charge(period,span,pulses,drug,calcium,even)
                    blocks.append(100*(1-q/q0))
                cluster,even = blocks
                values = np.column_stack((cluster,even,cluster-even)).ravel()
                writer.writerow([round(period,4),span,pulses,drug,calcium,*np.round(values,5)])
    for ca in (0.,0.1,10.):
        ref = constant_rate(0.,ca)
        half = brentq(lambda m: constant_rate(m,ca)/ref-.5, .001,50.)
        print(f"# steady 1mM glutamate, Ca={ca} uM: model IC50={half:.4f} uM")


if __name__ == "__main__":
    main()

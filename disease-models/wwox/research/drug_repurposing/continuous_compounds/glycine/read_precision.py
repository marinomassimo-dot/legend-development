"""Exact technical sampling distribution for a hypothetical equal-depth 2 vs 4 experiment."""
import csv
from collections import defaultdict
from math import comb, isclose
import sys

def binomial(n,p):
    return [comb(n,k)*p**k*(1-p)**(n-k) for k in range(n+1)]

def quantile(masses, probability):
    cumulative = 0.0
    for value, mass in sorted(masses.items()):
        cumulative += mass
        if cumulative >= probability:
            return value
    raise ValueError("Incomplete distribution")

writer=csv.writer(sys.stdout,delimiter="\t",lineterminator="\n")
writer.writerow(("scenario","reads_per_library","control_fraction","KO_fraction",
                 "technical_delta_pp_q025","technical_delta_pp_q975","probability_nonpositive"))
for scenario, pc, pk in (("mouse_sized_shift",0.2209,0.3223),("equal_fractions",0.2209,0.2209)):
    for depth in (20,50,100):
        masses=defaultdict(float)
        # With equal library depths, the KO minus control mean is (k - 2*c)/(4*depth).
        control=binomial(2*depth,pc)
        knockout=binomial(4*depth,pk)
        for c,mc in enumerate(control):
            for k,mk in enumerate(knockout):
                masses[k-2*c] += mc*mk
        assert isclose(sum(masses.values()),1.0,abs_tol=1e-10)
        unit=100/(4*depth)
        writer.writerow((scenario,depth,pc,pk,quantile(masses,0.025)*unit,
                         quantile(masses,0.975)*unit,f"{sum(m for v,m in masses.items() if v<=0):.5f}"))

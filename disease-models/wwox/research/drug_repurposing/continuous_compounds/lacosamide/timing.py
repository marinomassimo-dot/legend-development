"""Reconstruct the mean-parameter Fig. 6 clamp and compare two labelled timescales."""
import csv
from math import expm1
from pathlib import Path

def phases(time_s, fast_fraction, fast_tau, slow_fraction, slow_tau):
    return [-fast_fraction * expm1(-time_s / fast_tau), -slow_fraction * expm1(-time_s / slow_tau)]

with Path(__file__).with_name('timing.tsv').open('w') as stream:
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(['step_s','control_unavailable','lcm_unavailable','drug_minus_vehicle_pp','slow_contribution_pp'])
    for time in (0.025,0.10,0.66,2.,10.):
        control = phases(time,0.33,0.063,0.09,3.003)
        drug = phases(time,0.44,0.056,0.19,4.403)
        values = [sum(control),sum(drug),100*(sum(drug)-sum(control)),100*(drug[1]-control[1])]
        writer.writerow([time]+[round(value,5) for value in values])

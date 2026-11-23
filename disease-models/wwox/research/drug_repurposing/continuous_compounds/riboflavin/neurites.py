"""Digitize mean neurite length in Niceforo et al., Fig. 6C (CC BY 4.0)."""
from pathlib import Path
import csv
import hashlib
from statistics import median
import subprocess
import sys
import numpy as np

EXPECTED = '30194a5d6ce9f7fbe3c52e2885a02e6d5b442c345b543805d6e37fc912ac7f0f'
BARS = [('control', 'untreated', 89), ('P1', 'untreated', 120), ('P1', 'RF', 148),
        ('P1', 'NACA', 177), ('P1', 'combined', 207), ('P2', 'untreated', 236),
        ('P2', 'RF', 265), ('P2', 'NACA', 294), ('P2', 'combined', 323)]

def calculate(source, output):
    assert hashlib.sha256(source.read_bytes()).hexdigest() == EXPECTED
    rgb = subprocess.check_output(['convert', str(source), '-depth', '8', 'rgb:-'])
    pixels = np.frombuffer(rgb, dtype=np.uint8).reshape(1110, 718, 3).astype(int)
    ink = (np.ptp(pixels, axis=2) > 45) | (pixels.max(axis=2) < 210)
    tops = {}
    for line, treatment, center in BARS:
        edges = []
        for x in [center - 5, center - 4, center + 4, center + 5]:
            # Walk upward within the bar, away from central error bars and brackets.
            background = np.flatnonzero(~ink[795:965, x])
            edges.append(795 + int(background[-1]) + 1)
        assert max(edges) - min(edges) <= 2
        tops[line, treatment] = median(edges)
    # Zero and 200 µm tick centres are y=969.5 and 794.5 respectively.
    with output.open('w') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(['line', 'arm', 'bar_center_x', 'bar_top_y', 'approx_um', 'baseline_gap_closed_percent'])
        for line, treatment, x in BARS:
            top = tops[line, treatment]
            um = (969.5 - top) * 200 / 175
            fraction = 'NA'
            if line != 'control':
                baseline = tops[line, 'untreated']
                fraction = round(100 * (baseline - top) / (baseline - tops['control', 'untreated']), 1)
            writer.writerow([line, treatment, x, top, round(um, 1), fraction])

if __name__ == '__main__':
    calculate(Path(sys.argv[1]), Path(__file__).with_name('neurites.tsv'))

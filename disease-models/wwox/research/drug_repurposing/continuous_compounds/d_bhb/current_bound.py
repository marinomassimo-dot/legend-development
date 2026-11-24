"""Initial BHB compatible with a specified relative growth in modeled current at saturation."""
import csv
from pathlib import Path

def maximum_baseline(ec50, maximal_current, minimum_relative_growth, slope):
    # Solve I(C) = I(infinity) / (1 + growth) with I(0) = 1.
    initial_current = maximal_current / (1 + minimum_relative_growth)
    response_ratio = (initial_current - 1) / (maximal_current - initial_current)
    return ec50 * response_ratio ** (1 / slope)

with Path(__file__).with_suffix('.tsv').open('w', newline='') as stream:
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(['assumed_Hill_slope', 'required_relative_increment', 'highest_possible_baseline_uM'])
    for slope in [0.7, 1, 1.5]:
        for growth in [0.05, 0.1, 0.2]:
            writer.writerow([slope, growth, round(maximum_baseline(0.7, 3.5, growth, slope), 4)])

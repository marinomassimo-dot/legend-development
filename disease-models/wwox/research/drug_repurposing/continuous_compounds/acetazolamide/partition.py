"""Sensitivity calculation using Chapron Table 2 and a pediatric abstract-level total."""
from pathlib import Path
import csv

HERE = Path(__file__).resolve().parent
total_micromolar = 6.2 * 1000 / 222.25
bath_micromolar = 10
with (HERE / 'partition.tsv').open('w') as stream:
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(['adult_fraction_scenario', 'fraction_unbound', 'estimated_plasma_free_uM', 'required_unbound_brain_to_plasma_ratio'])
    for label, fraction in [('minimum', 0.032), ('reported_mean', 0.040), ('maximum', 0.057)]:
        free_micromolar = fraction * total_micromolar
        writer.writerow([label, fraction, round(free_micromolar, 3), round(bath_micromolar / free_micromolar, 3)])

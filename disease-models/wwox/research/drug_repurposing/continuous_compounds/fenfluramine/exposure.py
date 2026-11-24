"""Sensitivity of the free brain/plasma ratio required to match the BiP assay level."""
import csv
from pathlib import Path
import sys

parent_mw = 231.26  # g/mol, free base C12H16F3N
peak_total = 68.0 / parent_mw  # ng/mL divided by g/mol gives micromolar
peak_free = 0.5 * peak_total
with Path(sys.argv[1]).open('w') as stream:
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(['parent_plasma_peak_total_uM', 'parent_plasma_peak_free_uM',
                     'nominal_assay_uM', 'assumed_assay_free_fraction', 'implied_free_ratio'])
    for fraction in [0.1, 0.5, 1.0]:
        writer.writerow([round(peak_total, 4), round(peak_free, 4), 1.0, fraction,
                         round(1.0 * fraction / peak_free, 3)])

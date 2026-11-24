"""Reproduce the compartment-specific comparisons in exposure.md (stdout TSV)."""
import csv
import sys

MOLECULAR_WEIGHT = 171.24  # g/mol, gabapentin free compound, US label section 11
# PMDA dossier, Table 2.7.2.2 pp. 172–173, direct transcription of
# range endpoints from the original scan. Finnish footnote d separately identified.
rows = [
    ('Sweden_single_6h', 'CSF', 5, 0.14, 0.44),
    ('Sweden_12_weeks', 'CSF', 19, 0.22, 0.98),
    ('Finland_12_weeks_all', 'CSF', 9, 0.22, 0.78),
    ('Finland_excluding_two_deferred_CSF', 'CSF', 7, 0.22, 0.56),
]
writer = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')
writer.writerow(['source_group', 'compartment', 'n_values', 'low_ug_mL', 'high_ug_mL',
                 'low_uM', 'high_uM', 'retinal_32uM_over_high', 'high_over_spinal_0.1uM'])
for group, compartment, n, low, high in rows:
    a, b = [v * 1000 / MOLECULAR_WEIGHT for v in (low, high)]
    writer.writerow([group, compartment, n, low, high, f'{a:.3f}', f'{b:.3f}',
                     f'{32/b:.2f}', f'{b/.1:.2f}'])

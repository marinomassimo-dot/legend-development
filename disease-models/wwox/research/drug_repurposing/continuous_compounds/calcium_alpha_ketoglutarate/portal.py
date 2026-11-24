"""Descriptive contrasts from Lambert et al. Table 1, juvenile pig sodium-AKG study."""
import csv
import sys

enteral_rate = 930.0  # micromol/kg/h
baseline_balance, infused_balance = 19.7, 95.2  # micromol/kg/h
rows = [
    ('net_portal_appearance_over_enteral_input', 100 * infused_balance / enteral_rate, 'percent'),
    ('increment_over_saline_per_enteral_input', 100 * (infused_balance - baseline_balance) / enteral_rate, 'percent'),
    ('arterial_increment', 27.4 - 13.8, 'micromol/L'),
    ('portal_increment', 64.6 - 22.0, 'micromol/L'),
]
out = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')
out.writerow(['study_1_contrast', 'value', 'unit'])
for name, value, unit in rows:
    out.writerow([name, f'{value:.4f}', unit])

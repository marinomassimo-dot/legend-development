"""Recompute group plasma exposure and the conditional post-wash protein bound."""
from pathlib import Path
import csv
import sys

out = Path(sys.argv[1])
rows = []
for analyte, mass, peak, auc in [
    ('fenfluramine', 231.26, 68.6, 1400),
    ('norfenfluramine', 203.20, 37.8, 872),
]:
    for label, total in [('peak', peak), ('24h_time_average', auc / 24)]:
        rows.append([analyte, label, 'estimated_free_plasma_uM', 0.5 * total / mass])

# The input protein is added before washing. The retained amount is unknown.
sigma_added_pmol = 100 * 200 / 1000  # nM x µL / 1000
for analyte, ed50_pm in [('positive_parent', 170), ('positive_metabolite', 50)]:
    ligand_pmol = ed50_pm * 300 / 1e6
    rows.append([analyte, 'washed_assay_ED50', 'ligand_added_pmol', ligand_pmol])
    rows.append([analyte, 'linear_1to1_no_reuse', 'max_retained_pct_input',
                 100 * 2 * ligand_pmol / sigma_added_pmol])
rows.append(['parent_over_metabolite', 'FDA_population_DDI',
             'fold_change_24h_AUC_ratio', (1 + 1.66) / (1 - 0.38)])
with out.open('w') as stream:
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(['analyte', 'comparison', 'quantity', 'value'])
    for analyte, comparison, quantity, value in rows:
        writer.writerow([analyte, comparison, quantity, f'{value:.6g}'])

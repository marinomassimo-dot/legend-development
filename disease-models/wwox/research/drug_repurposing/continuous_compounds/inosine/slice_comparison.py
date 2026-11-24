"""Summarize within-mouse contrasts from three published inosine workbooks."""
import csv
from pathlib import Path
from statistics import median
import sys
import openpyxl

root = Path(sys.argv[1])
writer = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')
writer.writerow(['panel', 'contrast', 'units', 'complete_mice', 'positive',
                 'median_difference', 'min_difference', 'max_difference'])

def compare(book, tab, panel, description, units, rows, columns, coefficients):
    workbook = openpyxl.load_workbook(root / book, data_only=True)
    sheet = workbook[tab]
    differences = []
    for row in rows:
        assert str(sheet[f'A{row}'].value).startswith('M')
        values = [sheet[f'{column}{row}'].value for column in columns]
        if all(isinstance(value, (float, int)) for value in values):
            differences.append(sum(c * v for c, v in zip(coefficients, values)))
    writer.writerow([panel, description, units, len(differences), sum(d > 0 for d in differences),
                     *[f'{v:.4f}' for v in (median(differences), min(differences), max(differences))]])
    workbook.close()

for book, tab, panel, exposure, rows in [
    ('MOESM5.xlsx', 'Fig. 4', '4a', 'KCl', range(4, 10)),
    ('MOESM10.xlsx', 'Extended Data Fig. 4', 'ED4b', 'added_inosine', range(12, 18))
]:
    compare(book, tab, panel, f'pentoseP_{exposure}_minus_baseline', 'normalized_signal', rows, 'KJ', [1,-1])
    compare(book, tab, panel, f'pentoseP_{exposure}_8MDP_interaction', 'normalized_signal', rows, 'MLKJ', [1,-1,-1,1])

for analyte, columns in [('M+0','CB'), ('M+5','ED')]:
    compare('MOESM5.xlsx','Fig. 4','4e',f'pentoseP_{analyte}_KCl_minus_rest',
            'normalized_signal',range(23,29),columns,[1,-1])
for analyte, columns in [('pentoseP','DC'), ('phosphoenolpyruvate','SR')]:
    compare('MOESM5.xlsx','Fig. 4','4f',f'{analyte}_KCl_minus_rest',
            'atom_percent_points',range(34,40),columns,[1,-1])
compare('MOESM6.xlsx','Fig. 5','5i','phosphocreatine_PNP_inhibitor_minus_vehicle',
        'normalized_signal',range(86,95),'DC',[1,-1])

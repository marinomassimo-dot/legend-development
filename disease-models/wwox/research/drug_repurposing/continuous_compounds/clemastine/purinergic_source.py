"""Recalculate the clemastine-by-ATP interaction from Kocot et al. SD5."""
from pathlib import Path
from statistics import mean
import csv
import sys
import openpyxl


def read_effect(sheet, rows, columns):
    def group(column):
        values = [sheet[f'{column}{row}'].value for row in rows]
        return mean(value for value in values if isinstance(value, (int, float)))

    ctrl, drug, atp, both = map(group, columns[:4])
    interaction = (both - atp) - (drug - ctrl)
    blocked = group(columns[4]) if len(columns) == 5 else None
    return ctrl, drug, atp, both, blocked, interaction


if __name__ == '__main__':
    book = openpyxl.load_workbook(Path(sys.argv[1]), data_only=True)
    writer = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')
    writer.writerow('sheet experiment control clemastine ATP combined antagonist_plus_combined additive_interaction_pp'.split())
    for name, run, rows, columns in [
        ('Figure 3F', 'donor1', range(4, 8), 'ABCD'),
        ('Figure 3G', 'experiment1', range(4, 8), 'ABDEF'),
        ('Figure 3G', 'experiment2', range(8, 12), 'ABDEF'),
    ]:
        sheet = book[name]
        assert 'oligodendrocyte' in sheet['A1'].value
        assert sheet['A3'].value == 'Ctrl' and sheet['B3'].value == 'CLM'
        assert sheet[columns[2] + '3'].value == 'ATP'
        assert sheet[columns[3] + '3'].value in ('ATP+CLM', 'CLM+ATP')
        if len(columns) == 5:
            assert sheet[columns[4] + '3'].value == 'ATP+CLM+JNJ'
        writer.writerow([name, run, *read_effect(sheet, rows, columns)])

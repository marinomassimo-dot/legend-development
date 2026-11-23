"""Recalculate the Table 5 same-clock C4 comparisons under the published group labels."""
from decimal import Decimal
from pathlib import Path
import csv
import sys
import xml.etree.ElementTree as ET

def run(source, output):
    paper = ET.parse(source)
    table, = [t for t in paper.findall('.//table-wrap') if t.findtext('label') == 'Table 5']
    rows = []
    for row in table.findall('.//tbody/tr'):
        cells = [' '.join(''.join(cell.itertext()).split()) for cell in row]
        if len(cells) < 9:
            continue
        label = cells[0]
        identifier = int(label.split('*')[0])
        before, after = Decimal(cells[1]), Decimal(cells[4])
        group = 'below_baseline_criterion'
        if before > 2:
            group = 'poor' if '**' in label else 'compatible'
        eeg = cells[-1].split(' on C7')[0].lower()
        fall = (1 - after / before) * 100
        rows.append([identifier, group, before, after, round(fall, 1), eeg])
    assert len(rows) == 10 and len(set(row[0] for row in rows)) == 10
    with output.open('w') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(['study_row','authors_group','C4_day1_am_mM','C4_day3_am_mM','decrease_percent','EEG_on_C7'])
        writer.writerows(rows)

if __name__ == '__main__':
    run(Path(sys.argv[1]), Path(__file__).with_name('ketones.tsv'))

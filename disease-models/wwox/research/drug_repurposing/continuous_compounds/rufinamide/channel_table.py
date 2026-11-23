"""Recompute parent-drug minus vehicle contrasts in the first table of Gilchrist et al."""
import csv
from html.parser import HTMLParser
from pathlib import Path
import sys


class ParentTable(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows = []
        self.table_count = 0
        self.in_table = False
        self.cell = None

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.table_count += 1
            self.in_table = self.table_count == 1
        if self.in_table and tag == 'tr':
            self.row = []
        if self.in_table and tag in {'th', 'td'}:
            self.cell = []

    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)

    def handle_endtag(self, tag):
        if tag in {'th', 'td'} and self.cell is not None:
            self.row.append(''.join(self.cell).strip())
            self.cell = None
        if tag == 'tr' and self.in_table:
            self.rows.append(self.row)
        if tag == 'table':
            self.in_table = False


def compare(source, target):
    parser = ParentTable()
    parser.feed(source.read_text())
    values = {}
    for row in parser.rows:
        if len(row) != 6:
            continue
        treatment, measure, *cells = row
        if treatment:
            group = treatment
        if measure.startswith(('activation', 'inactivation', 'recovery')) and group in {'DMSO', 'rufinamide'}:
            numbers = [float(v.split('±')[0].strip().replace('–','-').replace('−','-')) for v in cells]
            values[group, measure.split()[0]] = numbers
    with target.open('w') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(['measurement','unit','isoform','DMSO','rufinamide_100uM','difference','ratio_for_tau'])
        for measure in ['activation','inactivation','recovery']:
            vehicle = values['DMSO',measure]
            drug = values['rufinamide',measure]
            for isoform, a, b in zip(['NaV1.1','NaV1.2','NaV1.3','NaV1.6'],vehicle,drug,strict=True):
                writer.writerow([measure,'ms' if measure=='recovery' else 'mV',isoform,a,b,round(b-a,2),round(b/a,3) if measure=='recovery' else 'NA'])


if __name__ == '__main__':
    compare(Path(sys.argv[1]), Path(__file__).with_name('channels.tsv'))

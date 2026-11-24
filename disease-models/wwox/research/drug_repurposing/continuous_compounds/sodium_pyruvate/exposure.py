"""Reproduce formulation, diagnostic and crossover contrasts from the cited sources."""
import csv
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

article = ET.parse(Path(sys.argv[1]))
assert article.findtext('.//article-id[@pub-id-type="pmid"]') == '24841105'
table = article.find('.//table-wrap/table')
rows = [[''.join(cell.itertext()).strip() for cell in row] for row in table.findall('.//tr')]
assert rows[0][1:] == ['Placebo', 'NaP']
start = next(i for i, row in enumerate(rows) if row[0].startswith('PYR'))
baseline, after = rows[start + 1:start + 3]
assert baseline[0] == 'Rest' and after[0] == '60 min after ingestion'
placebo, sodium = (float(after[i].split()[0]) - float(baseline[i].split()[0]) for i in [1, 2])
out = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')
out.writerow(['source', 'matrix', 'measure', 'value', 'unit'])
for source, matrix, measure, value, unit in [
    ('Gibco 21331/Neurobasal', 'fresh basal mixture', 'equal-volume recipe', (55+25)/2/110, 'mM'),
    ('Komaki p314', 'CSF', 'pretreatment', 1.21*10/88.06, 'mM'),
    ('Komaki p314', 'blood', 'pretreatment', 1.13*10/88.06, 'mM'),
    ('Komaki p314', 'blood', 'on treatment', 0.88*10/88.06, 'mM'),
    ('Fujii p136 patient 3', 'CSF', 'derived pretreatment from lactate and ratio', 5.2/20, 'mM'),
    ('Olek Table 1', 'capillary blood', '60 min minus rest, placebo', placebo, 'uM'),
    ('Olek Table 1', 'capillary blood', '60 min minus rest, sodium pyruvate', sodium, 'uM'),
    ('Olek Table 1', 'capillary blood', 'between-period difference of mean changes', sodium-placebo, 'uM')
]:
    out.writerow([source, matrix, measure, f'{value:.4f}', unit])

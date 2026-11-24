"""Reproduce the timing contrasts and cross-system exposure comparison."""
import csv
import sys
import xml.etree.ElementTree as ET

r = ET.parse(sys.argv[1])
assert r.findtext('.//article-id[@pub-id-type="pmid"]') == '26133962'
table = r.find('.//table-wrap[@id="T2"]')
rows = [[' '.join(''.join(c.itertext()).split()) for c in tr] for tr in table.findall('.//tr')]
assert 'Healthy Comparison Group' in rows[0][2]
plasma_row, = [row for row in rows if row[0].startswith('Plasma level')]
total = float(plasma_row[7]) / 375.56  # ng/mL to µM, using active-moiety mass
free = total * 0.04
out = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')
out.writerow(['quantity', 'value', 'unit'])
for name, value, unit in [
    ('TMS conditioned response at 3 ms, post minus pre', 50.4 - 37.1, 'percentage points'),
    ('TMS cortical silent period, post minus pre', 180 - 158, 'ms'),
    ('CA1 conditioned population amplitude at 200 ms, drug minus control', 7.8 - 35.4, 'percentage points'),
    ('CA1 conditioned population amplitude at 800 ms, drug minus control', 34.4 - 98.8, 'percentage points'),
    ('adult healthy comparator total plasma mean', total, 'uM'),
    ('adult free plasma mean estimated from label', free, 'uM'),
    ('2 uM slice bath / estimated human free plasma', 2/free, 'fold'),
    ('20 uM slice bath / estimated human free plasma', 20/free, 'fold'),
]:
    out.writerow([name, f'{value:.4f}', unit])

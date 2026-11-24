"""Reproduce the chiral plasma comparison in Hermann et al., Tables 1 and 2."""
import csv
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

source, output = map(Path, sys.argv[1:])
root = ET.parse(source)
assert root.findtext('.//article-id[@pub-id-type="pmid"]') == '25506250'
def geometric_means(label):
    table, = [t for t in root.findall('.//table-wrap') if t.findtext('label') == label]
    values = {}
    for row in table.findall('.//tbody/tr'):
        cells = [''.join(c.itertext()).strip() for c in row.findall('td')]
        values[cells[0]] = float(cells[1].replace(',', ''))
    return values

peaks, areas = geometric_means('Table 1'), geometric_means('Table 2')
assert peaks.keys() == areas.keys() and len(peaks) == 4
with output.open('w') as stream:
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(['form', 'R_plasma_peak_uM', 'R_plasma_AUC0t_uM_h',
                     'AUC_over_5uM_hours', 'fraction_of_constant_5uM_24h_area'])
    for form, peak in peaks.items():
        area = areas[form] / 206.33
        writer.writerow([form, round(peak/206.33, 3), round(area, 3),
                         round(area/5, 3), round(area/(5*24), 4)])

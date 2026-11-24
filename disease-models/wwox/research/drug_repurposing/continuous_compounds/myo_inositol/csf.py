"""Recalculate the control distributions and repeated patient observations in Vos Tables S1/S2."""
import csv
from pathlib import Path
import statistics
import sys
import xml.etree.ElementTree as ET
from zipfile import ZipFile

with ZipFile(sys.argv[1]) as archive:
    document = ET.fromstring(archive.read('word/document.xml'))
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
tables = document.findall('.//w:tbl', ns)
with Path(sys.argv[2]).open('w') as stream:
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(['matrix', 'group', 'n_observations', 'mean_uM', 'sample_sd_uM', 'min', 'max'])
    for matrix, table in zip(['plasma', 'CSF'], tables[:2]):
        rows = [[''.join(cell.itertext()).strip() for cell in row.findall('w:tc', ns)]
                for row in table.findall('w:tr', ns)]
        assert 'Control patients' in rows[0] and 'Myo-Inositol' in rows[1][1]
        data_rows = [r for r in rows if r[0].isdigit()]
        for group, col in [('control', 1), ('one_treated_child', 3)]:
            values = [float(r[col]) for r in data_rows if r[col] not in {'NA', ''}]
            writer.writerow([matrix, group, len(values), round(statistics.mean(values), 3),
                             round(statistics.stdev(values), 3), min(values), max(values)])

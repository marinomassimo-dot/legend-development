"""Calculate descriptive CSF concentrations from Vos supplement S3–S5, without assuming independent litters."""
import csv
from pathlib import Path
from statistics import mean
import sys
import xml.etree.ElementTree as ET
from zipfile import ZipFile

with ZipFile(sys.argv[1]) as archive:
    document = ET.fromstring(archive.read('word/document.xml'))
tables = document.findall('.//{*}tbl')
assert len(tables) == 5
with Path(sys.argv[2]).open('w') as stream:
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(['genotype', 'embryonic_day', 'n_unsupplemented', 'n_supplemented',
                     'control_mean_uM', 'supplemented_mean_uM', 'increment_uM', 'fold'])
    for table in tables[2:]:
        rows = [[''.join(c.itertext()).strip() for c in r.findall('{*}tc')] for r in table.findall('{*}tr')]
        label = rows[0][1]
        assert rows[2][1:] == ['10.5', '14.5', '18.5'] * 2
        samples = [r for r in rows if r[0].startswith('Sample ')]
        for col in (1, 2, 3):
            def values(index):
                return [float(r[index]) for r in samples if r[index]]
            a, b = values(col), values(col + 3)
            ca, cb = mean(a), mean(b)
            writer.writerow([label, rows[2][col], len(a), len(b), round(ca, 2),
                             round(cb, 2), round(cb - ca, 2), round(cb / ca, 3)])

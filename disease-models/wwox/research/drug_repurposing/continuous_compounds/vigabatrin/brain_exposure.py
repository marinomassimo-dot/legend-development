"""Recompute published brain-dialysate summaries from Shannon et al. S2–S3."""
import csv
from collections import defaultdict
from pathlib import Path
from statistics import median
import sys
import xml.etree.ElementTree as ET
from zipfile import ZipFile

word = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
def patient_rows(path):
    with ZipFile(path) as archive:
        root = ET.fromstring(archive.read('word/document.xml'))
    rows = {}
    patient = None
    for row in root.iter(word + 'tr'):
        cells = [''.join(cell.itertext()).strip() for cell in row.findall(word + 'tc')]
        if cells[0].isdigit():
            patient = int(cells[0])
        elif not (cells[0] == '' and cells[1] == 'B'):
            continue
        catheter = cells[1] if cells[1] in ('A','B') else 'single'
        key = (patient, catheter)
        assert key not in rows
        rows[key] = cells[2:] if catheter != 'single' else cells[1:]
    return rows

inputs, output = map(Path, sys.argv[1:])
pk = patient_rows(inputs/'sd4.docx')
dial = patient_rows(inputs/'sd5.docx')
assert set(pk) == set(dial) and len(dial) == 11
for key, data in dial.items():
    assert abs(float(pk[key][3]) - float(data[1])) < 0.011
with output.open('w') as stream:
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(['dose', 'background_subtracted_fraction', 'sampling_unit',
                     'included_units', 'median_peak_uM', 'median_time_avg_uM', 'max_peak_uM'])
    for dose, idx in [(1,1),(3,3)]:
        for fraction in (0, 1):
            pairs = [(person, float(row[idx])-fraction*float(row[0]),
                      float(row[idx+1])-fraction*float(row[0]))
                     for (person, _), row in dial.items() if row[idx] != '--']
            by_person = defaultdict(list)
            for person, peak, mean in pairs:
                by_person[person].append((peak, mean))
            individuals = [(p, median(v[0] for v in group), median(v[1] for v in group))
                           for p, group in by_person.items()]
            for unit, values in [('catheter',pairs),('person',individuals),
                                 ('person_excluding_P6',[v for v in individuals if v[0] != 6])]:
                writer.writerow([dose, fraction, unit, len(values),
                                 round(median(v[1] for v in values),3),
                                 round(median(v[2] for v in values),3),
                                 round(max(v[1] for v in values),3)])

# Within-catheter change cancels a constant additive background. Aggregate the two
# dual-catheter participants before computing the group median and sign count.
changes = defaultdict(list)
for (person, _), row in dial.items():
    if row[3] != '--':
        changes[person].append((float(row[3])-float(row[1]),
                                float(row[4])-float(row[2])))
with output.with_name('paired_change.tsv').open('w') as stream:
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(['measure','people','increased','median_change_dose3_minus_dose1_uM'])
    for idx, label in enumerate(['peak', 'time_average']):
        values = [median(v[idx] for v in group) for group in changes.values()]
        writer.writerow([label, len(values), sum(v > 0 for v in values), round(median(values),3)])

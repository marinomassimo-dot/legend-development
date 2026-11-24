"""Align the eight Kearns-Sayre observations across the two published tables."""
import csv
from pathlib import Path
import sys
import xml.etree.ElementTree as ET


def patient_rows(article, label):
    table, = [t for t in article.findall('.//table-wrap') if t.findtext('label') == label]
    rows = {}
    for tr in table.findall('.//tr'):
        cells = [' '.join(''.join(cell.itertext()).split()) for cell in tr if cell.tag in ('th', 'td')]
        if cells and cells[0].strip('*').isdigit():
            rows[cells[0].strip('*')] = cells
    return rows


article = ET.parse(sys.argv[1])
biochemistry = patient_rows(article, 'Table 2')
clinical = patient_rows(article, 'Table 3')
assert set(biochemistry) == set(clinical) == set('12345678')
with Path(sys.argv[2]).open('w') as stream:
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(['case', 'age_start_y', 'repeat_interval_y', 'plasma_folate_ng_mL',
                     'csf_pre_nmol_L', 'csf_post_nmol_L', 'NPMDS_pre', 'NPMDS_post'])
    for case, row in biochemistry.items():
        folate = row[6].split('➔')
        scores = clinical[case][-1].strip('*').split('/')
        writer.writerow([case, row[1], row[3], row[4], folate[0],
                         folate[1] if len(folate) == 2 else 'NA',
                         *(scores if len(scores) == 2 else ['NA', 'NA'])])

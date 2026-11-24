"""Combine published buffer rates and adult incremental plasma exposures.

Run: python kinetics.py /path/to/l_carnosine_loop_20261124 > kinetics.tsv
The calculation describes a hypothetical bolus of aldehyde in a single compartment.
"""
import csv
from math import expm1, log
from pathlib import Path
import sys
import xml.etree.ElementTree as ET


def table_rows(path, pmid, label):
    root = ET.parse(path)
    assert root.findtext('.//article-id[@pub-id-type="pmid"]') == pmid
    table, = [t for t in root.findall('.//table-wrap') if t.findtext('label') == label]
    return [[' '.join(''.join(cell.itertext()).split()) for cell in row]
            for row in table.findall('.//tr')]


source = Path(sys.argv[1])
rates = table_rows(source / 'pmid_23559625.xml', '23559625', 'Table 1')
plasma = table_rows(source / 'oral.xml', '40647235', 'Table 4')
assert rates[0][1].startswith('Carnosine') and rates[0][4].startswith('Histidine')
assert 'Carnosine' in plasma[0][0] and 'Histidine' in plasma[6][0]
assert 'AUC' in plasma[1][1] and 'AUC' in plasma[7][1]
writer = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')
writer.writerow(['adult_arm', 'reactant', 'aldehyde', 'k_per_M_s', 'incremental_AUC_uM_h',
                 'k_times_AUC', 'model_incremental_loss_percent', 'half_time_at_1mM_min'])
for label, column, section in [('carnosine', 1, plasma[2:6]), ('histidine', 4, plasma[8:12])]:
    for arm, area, *_ in section:
        auc = float(area.split('±')[0])
        for row in rates[1:]:
            if row[0] not in ('4-HNE', 'Acrolein'):
                continue
            rate = float(row[column].split('±')[0])
            hazard = rate * auc * 0.0036  # micromolar-hours to molar-seconds
            writer.writerow([arm, label, row[0], rate, auc, f'{hazard:.6f}',
                             f'{-100 * expm1(-hazard):.3f}', f'{log(2)/(rate*.001*60):.2f}'])

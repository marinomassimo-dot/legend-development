"""Recompute the magnesium-only concentration shifts from Yi et al. Table 3."""
import csv
import hashlib
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

SOURCE_SHA = '87ee420f6086fb5a93fe88a7fadb5a5462de32bcf213494f9986d422ee5be011'
# mM. The original slice value is nominal and the adult CSF value is ionized.
SCENARIOS = [('adult_ventricular', 0.80, 0.89), ('nominal_spheroid_sensitivity', 1.50, 1.59),
             ('restoring_from_zero', 0.00, 0.80)]


def current(mg_mm, ic50_um, slope):
    return 100 / (1 + (1000 * mg_mm / ic50_um) ** slope)


def calculate(source, output):
    if hashlib.sha256(source.read_bytes()).hexdigest() != SOURCE_SHA:
        raise ValueError('Use the archived Yi Table 3 XML identified in the dossier')
    table, = [t for t in ET.parse(source).findall('.//table-wrap')
              if t.findtext('label', '').rstrip('.') == 'Table 3']
    with output.open('w') as stream:
        out = csv.writer(stream, delimiter='\t', lineterminator='\n')
        out.writerow('scenario Mg_start_mM Mg_end_mM mV subtype oocytes IC50_uM IC50_SEM_uM Hill start_pct end_pct loss_points loss_pct_of_start loss_points_lowIC50 loss_points_highIC50'.split())
        for row in table.findall('.//tbody/tr'):
            cells = [''.join(cell.itertext()).strip() for cell in row]
            if cells[0] != 'Mg2+':
                continue
            voltage = int(cells[1].replace('−', '-'))
            for i, subtype in enumerate(('BB', 'BD', 'DD')):
                offset = 2 + 3*i
                ic50, sem = map(float, re.findall(r'[0-9]+(?:\.[0-9]+)?', cells[offset])[:2])
                slope = float(cells[offset+1])
                n = int(cells[offset+2])
                for name, start, end in SCENARIOS:
                    before = current(start, ic50, slope)
                    after = current(end, ic50, slope)
                    loss = before - after
                    sens = [current(start, k, slope) - current(end, k, slope) for k in (ic50-sem, ic50+sem)]
                    out.writerow([name, start, end, voltage, subtype, n, ic50, sem, slope,
                                  *(f'{x:.6f}' for x in [before, after, loss, 100*loss/before, *sens])])


if __name__ == '__main__':
    calculate(*map(Path, sys.argv[1:]))

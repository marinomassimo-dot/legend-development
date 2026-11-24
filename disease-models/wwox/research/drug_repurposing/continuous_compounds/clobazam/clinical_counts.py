"""Aggregate Oliver et al. Table 2 without exporting participant-level data."""
import argparse
from xml.etree import ElementTree
import re

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("article_xml")
root = ElementTree.parse(parser.parse_args().article_xml)
def mentions(cell, current):
    nodes = cell.iter('underline') if current else (cell,)
    return set(re.findall(r'\b[A-Z]+\b', ' '.join(''.join(n.itertext()) for n in nodes)))

rows = [list(row)[1:] for table in root.findall('.//table-wrap')
        if table.findtext('label', '').strip().lower() == 'table 2'
        for row in table.findall('.//tr') if 'ASMs trialed' in ''.join(list(row)[0].itertext())]
if len(rows) != 1 or len(rows[0]) != 13:
    raise ValueError('Expected one treatment row with 13 clinical histories')
print('status\thistories\tCLB\tCBD\tboth')
for current in (False, True):
    sets = [mentions(cell, current) for cell in rows[0]]
    print('current' if current else 'ever', len(sets), sum('CLB' in s for s in sets),
          sum('CBD' in s for s in sets), sum({'CLB', 'CBD'} <= s for s in sets), sep='\t')

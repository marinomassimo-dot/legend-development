"""Extract the prespecified sulfur genes from Table S2 (PMID 40175519)."""
import csv
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

GENES = 'NFE2L2 KEAP1 NQO1 GCLC GCLM GSS SLC7A11 CBS CTH SLC1A1 ABCC1'.split()
SHEETS = ('SFN-control DEGs', 'VPA-control DEGs', 'VPA+SFN-control DEGs', 'VPA+SFN-VPA DEGs')


def extract(workbook, output):
    with zipfile.ZipFile(workbook) as archive, output.open('w') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(['contrast', 'listed_rows', 'gene', 'listed', 'log2FC', 'adjusted_p'])
        book = ET.fromstring(archive.read('xl/workbook.xml'))
        names = [e.get('name') for e in book.findall('.//{*}sheet')]
        if tuple(names[:4]) != SHEETS:
            raise ValueError('Unexpected worksheet layout for the published Table S2')
        strings = [''.join(n.itertext()) for n in ET.fromstring(archive.read('xl/sharedStrings.xml'))]
        for number, name in enumerate(SHEETS, 1):
            root = ET.fromstring(archive.read(f'xl/worksheets/sheet{number}.xml'))
            rows = root.findall('.//{*}row')
            entries = {}
            count = 0
            for row in rows[1:]:
                values = {}
                for cell in row:
                    column = re.sub(r'[0-9]+', '', cell.get('r'))
                    if column not in ('A', 'B', 'C', 'D'):
                        continue
                    value = cell.findtext('{*}v')
                    if value is not None:
                        values[column] = strings[int(value)] if cell.get('t') == 's' else value
                if row.get('r') == '2':
                    if list(values.values()) != ['Ensembl gene ID','external_gene_name','log2FoldChange','padj']:
                        raise ValueError(f'Unexpected header in {name}')
                    continue
                if not all(key in values for key in ('A', 'B', 'C', 'D')):
                    continue
                count += 1
                gene = values['B']
                if gene in GENES:
                    if gene in entries:
                        raise ValueError(f'Duplicate {gene} in {name}')
                    entries[gene] = (values['C'], values['D'])
            for gene in GENES:
                writer.writerow([name, count, gene, int(gene in entries), *entries.get(gene, ('NA', 'NA'))])


if __name__ == '__main__':
    extract(*map(Path, sys.argv[1:]))

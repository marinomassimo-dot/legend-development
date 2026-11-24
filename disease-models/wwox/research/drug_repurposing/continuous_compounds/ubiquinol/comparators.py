"""Extract preselected proteins and pediatric crossover endpoints from held primary records."""
import csv
import hashlib
import json
from pathlib import Path
import sys


def extract(files, output):
    study = json.loads((files / 'deepening_downloads/ubiquinol_loop_20261124/NCT00432744.json').read_bytes())
    protocol = study['protocolSection']
    assert protocol['identificationModule']['nctId'] == 'NCT00432744'
    enrolled = protocol['designModule']['enrollmentInfo']['count']
    measures = study['resultsSection']['outcomeMeasuresModule']['outcomeMeasures']
    with (output / 'clinical.tsv').open('w') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(['endpoint', 'enrolled', 'n_analyzed', 'method', 'estimate', 'ci95_low', 'ci95_high', 'p'])
        for m in measures:
            analysis, = m['analyses']
            denominators, = m['denoms']
            n = sum(int(c['value']) for c in denominators['counts'])
            writer.writerow([m['title'], enrolled, n, analysis['statisticalMethod'],
                             analysis.get('paramValue', 'NA'), analysis.get('ciLowerLimit', 'NA'),
                             analysis.get('ciUpperLimit', 'NA'), analysis['pValue']])

    table = files / 'i18_proteome/zeng2024_table_s1_parsed.tsv'
    manifest = json.loads((table.parent / 'MANIFEST.json').read_bytes())
    assert hashlib.sha256(table.read_bytes()).hexdigest() == manifest['table_sha256']
    with table.open() as stream:
        proteins = list(csv.DictReader(stream, delimiter='\t'))
    with (output / 'protein.tsv').open('w') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(['symbol', 'matching_rows', 'log2FC', 'BH_adjusted_p'])
        for symbol in 'COQ2 COQ4 COQ7 COQ9 AIFM2 GPX4 NQO1'.split():
            aliases = {symbol, 'FSP1'} if symbol == 'AIFM2' else {symbol}
            matches = [p for p in proteins if p['symbol'] in aliases]
            assert len(matches) <= 1
            row = matches[0] if matches else {}
            writer.writerow([symbol, len(matches), row.get('log2fc', 'NA'), row.get('bh_adj_p', 'NA')])


if __name__ == '__main__':
    extract(Path(sys.argv[1]), Path(sys.argv[2]))

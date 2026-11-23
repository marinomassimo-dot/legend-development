"""Sample-level detectability in the author-linked UCSC cortex-dev atlas."""
import argparse
import csv
import gzip
import hashlib
import json
from collections import defaultdict
from pathlib import Path
import numpy as np


def write(path, header, rows):
    with path.open('w', newline='') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(header)
        writer.writerows(rows)


def load_atlas(matrix, metadata, config):
    assert json.loads(config.read_text())['unit'] == 'TPM'
    with metadata.open() as stream:
        meta = {r['Cell']: r for r in csv.DictReader(stream, delimiter='\t')}
    targets = {'PAQR6', 'PAQR7', 'PAQR8', 'SOX2', 'PROM1', 'DCX', 'WWOX'}
    genes = {}
    with gzip.open(matrix, 'rt') as stream:
        cells = stream.readline().rstrip().split('\t')[1:]
        assert len(cells) == len(meta) == len(set(cells)) and set(cells) == set(meta)
        for line in stream:
            key, rest = line.rstrip().split('\t', 1)
            symbol = key.split('|')[-1]
            if symbol in targets:
                assert symbol not in genes
                values = np.fromstring(rest, sep='\t')
                assert len(values) == len(cells) and np.all(values >= 0)
                genes[symbol] = values
    assert set(genes) == targets
    return cells, meta, genes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('matrix', 'meta', 'config', 'out'):
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    cells, meta, genes = load_atlas(args.matrix, args.meta, args.config)
    groups = defaultdict(list)
    for i, cell in enumerate(cells):
        row = meta[cell]
        if row['RegionName'] != 'Cortex':
            continue
        cluster = row['WGCNAcluster']
        if cluster in ('RG-div1', 'RG-div2'):
            cluster = 'dividing_RG'
        if cluster not in ('vRG', 'dividing_RG'):
            continue
        age = float(row['Age_in_Weeks'])
        for lo, hi in [(10, 20), (13, 16)]:
            if lo <= age <= hi:
                groups[(f'{lo}-{hi}', cluster, row['Name'])].append(i)
    samples, summary = [], defaultdict(list)
    for (ages, cluster, name), idx in sorted(groups.items()):
        for symbol in sorted(genes):
            values = genes[symbol][idx]
            for floor, present in [('positive', values > 0), ('at_least_1_TPM', values >= 1)]:
                proportion = present.mean()
                samples.append([ages, cluster, name, len(idx), symbol, floor, int(present.sum()), proportion])
                if len(idx) >= 5:
                    summary[ages, cluster, symbol, floor].append((len(idx), int(present.sum()), proportion))
    rows = []
    for key, counts in sorted(summary.items()):
        n, detected, fractions = np.asarray(counts).T
        rows.append([*key, len(counts), int(n.sum()), int(detected.sum()), np.median(fractions),
                     *[int(sum(fractions >= cutoff)) for cutoff in (.01, .10, .25)]])
    write(args.out/'single_cell_samples.tsv', 'weeks class sample cells gene expression_floor detected fraction'.split(), samples)
    write(args.out/'single_cell_summary.tsv', 'weeks class gene floor samples_ge5 cells detected median_sample_fraction samples_ge1pct samples_ge10pct samples_ge25pct'.split(), rows)
    write(args.out/'single_cell_inputs.tsv', ['input', 'sha256'], ([p.name, hashlib.sha256(p.read_bytes()).hexdigest()] for p in (args.matrix, args.meta, args.config)))


if __name__ == '__main__':
    main()

"""Calculate conditional residual transport and human comparator contrasts."""
from pathlib import Path
import argparse
import csv


def carrier_rows(screen):
    rows = []
    with screen.open() as stream:
        for record in csv.DictReader(stream, delimiter='\t'):
            if record['gene'] != 'SLC25A19':
                continue
            r = float(record['ko_mean']) / float(record['wt_mean'])
            assert 0 < r < 1
            ceiling = r / (1 - r)
            for s in (0.25, 1, 3, 10):
                margin = r - (1 - r) * s
                rows.append([record['model'], r, s, ceiling,
                             1 / margin if margin > 0 else 'no_finite_solution'])
    return rows

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('screen', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    with args.output.open('w') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(['model','capacity_proxy','baseline_substrate_over_Km','critical_s','required_fold_in_cytosolic_ThDP'])
        writer.writerows(carrier_rows(args.screen))

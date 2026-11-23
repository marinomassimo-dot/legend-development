"""Estimate captured-cell transcript contributions in explicitly dissected ventricular zone."""
import argparse
from collections import defaultdict
from pathlib import Path
import numpy as np
from single_cells import load_atlas, write

RADIAL = {
    "vRG": {"vRG"},
    "with_dividing": {"vRG", "RG-div1", "RG-div2"},
    "all_radial": {"vRG", "RG-div1", "RG-div2", "tRG", "oRG", "RG-early"},
}


def share(inside, outside, weight=1):
    total = weight * inside + outside
    return weight * inside / total if total else float('nan')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for item in ('matrix', 'meta', 'config', 'out'):
        parser.add_argument(item, type=Path)
    args = parser.parse_args()
    cells, meta, genes = load_atlas(args.matrix, args.meta, args.config)
    samples = defaultdict(list)
    for i, cell in enumerate(cells):
        row = meta[cell]
        if (row['RegionName'] == 'Cortex' and row['Laminae'] == 'VZ'
                and 10 <= float(row['Age_in_Weeks']) <= 20):
            samples[row['Name']].append(i)
    class_rows, sample_rows, summary = [], [], defaultdict(list)
    for sample, idx in sorted(samples.items()):
        classes = np.array([meta[cells[i]]['WGCNAcluster'] for i in idx])
        for gene in sorted(genes):
            levels = genes[gene][idx]
            for label in sorted(set(classes)):
                values = levels[classes == label]
                class_rows.append([sample, label or 'unassigned', gene, len(values),
                                   np.count_nonzero(values), sum(values), max(values)])
            for name, labels in RADIAL.items():
                target = np.isin(classes, list(labels))
                inside, outside = levels[target].sum(), levels[~target].sum()
                rates = [share(inside, outside, w) for w in (.25, 1, 4)]
                sample_rows.append([sample, name, gene, int(sum(target)), len(levels),
                                    inside, outside, *rates])
                if target.any() and inside + outside > 0:
                    summary[gene, name].append((inside, outside))
    summary_rows = []
    for key, values in sorted(summary.items()):
        a, b = np.array(values).T
        for weight in (.25, 1, 4):
            fractions = [share(x,y,weight) for x,y in values]
            pooled = share(sum(a), sum(b), weight)
            leave_out = [share(sum(a)-x, sum(b)-y, weight) for x,y in values]
            summary_rows.append([*key, weight, len(a), sum(v > .5 for v in fractions),
                                 np.mean(fractions), pooled, np.nanmin(leave_out), np.nanmax(leave_out)])
    write(args.out/'vz_classes.tsv', 'sample atlas_class gene cells positive sum_TPM max_TPM'.split(), class_rows)
    write(args.out/'vz_sample_shares.tsv', 'sample radial_classes gene radial_cells all_cells radial_TPM other_TPM share_w025 share_w1 share_w4'.split(), sample_rows)
    write(args.out/'vz_summary.tsv', 'gene radial_classes weight informative_samples samples_majority equal_sample_mean pooled_informative leave_one_min leave_one_max'.split(), summary_rows)


if __name__ == '__main__':
    main()

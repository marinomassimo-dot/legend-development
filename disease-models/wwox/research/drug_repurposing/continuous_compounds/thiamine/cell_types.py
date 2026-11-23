"""Recompute the compartment-relevant transcript counts in WWOX hippocampal nuclei."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / 'ganaxolone_20261123'))
from analyze import assigned_nuclei, tsv

GENES = ['Slc19a2', 'Slc19a3', 'Slc25a19', 'Tpk1', 'Pdha1', 'Ogdh', 'Tkt']
def run(files, genes=GENES, output_dir=HERE):
    rows = []
    summaries = {}
    for arm, cell, depth, counts in assigned_nuclei(files, [], [], genes):
        total = int(depth.sum())
        for gene in genes:
            umi = int(counts[gene].sum())
            rows.append([arm, cell, gene, len(depth), total, umi, int((counts[gene] > 0).sum()), 1e6*umi/total])
            summaries[arm, cell, gene] = (total, umi)
    tsv(output_dir/'cell_types.tsv', 'pool class gene nuclei total_UMI gene_UMI positive CPM'.split(), rows)
    cells = sorted({cell for arm, cell, gene in summaries})
    effects = []
    for gene in genes:
        within = mixture = 0.0
        totals = {arm:sum(summaries[arm,c,gene][0] for c in cells) for arm in ['ctrl','ko']}
        means = {}
        for arm in totals:
            means[arm] = 1e6*sum(summaries[arm,c,gene][1] for c in cells)/totals[arm]
        for c in cells:
            rates, weights = {}, {}
            for arm in totals:
                depth, umi = summaries[arm,c,gene]
                rates[arm] = 1e6*umi/depth
                weights[arm] = depth/totals[arm]
            within += (rates['ko']-rates['ctrl'])*(weights['ko']+weights['ctrl'])/2
            mixture += (weights['ko']-weights['ctrl'])*(rates['ko']+rates['ctrl'])/2
        diff = means['ko']-means['ctrl']
        assert abs(diff-within-mixture) < 1e-8
        effects.append([gene, means['ctrl'], means['ko'], diff, within, mixture])
    tsv(output_dir/'mixture.tsv', 'gene ctrl_CPM ko_CPM difference within_class class_weights'.split(), effects)

if __name__ == '__main__':
    run(Path(sys.argv[1]))

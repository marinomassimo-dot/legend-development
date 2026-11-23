"""Describe purinergic receptor and gasdermin machinery in pooled WWOX hippocampus."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / 'ganaxolone_20261123'))
from analyze import assigned_nuclei, tsv

GENES = ['P2rx7', 'Gsdmd', 'Casp1']
if __name__ == '__main__':
    rows = []
    for arm, cell, depth, counts in assigned_nuclei(Path(sys.argv[1]), [], [], GENES):
        if cell in {'microglia', 'OPC', 'COP', 'NFOL', 'MFOL', 'MOL'}:
            for gene in GENES:
                values = counts[gene]
                rows.append([arm, cell, gene, len(depth), int(depth.sum()), int(values.sum()),
                             int((values > 0).sum()), values.sum() * 1e6 / depth.sum()])
    tsv(HERE / 'purinergic_nuclei.tsv', 'pool class gene nuclei total_UMI gene_UMI positive CPM'.split(), rows)

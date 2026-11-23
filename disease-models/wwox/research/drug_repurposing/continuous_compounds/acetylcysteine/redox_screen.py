"""Reproduce the bulk expression and pooled hippocampal nuclear counts."""
import argparse
import gzip
from pathlib import Path
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'creatine'))
from assess import MODELS, assigned_nuclei, load_target, reference, tsv

GENES = 'Gclc Gclm Gss Gsr Slc7a11 Slc3a2 Slc1a1 Slc1a2 Slc1a3'.split()

def bulk(files):
    gene_map, _ = reference(files)
    rows, library_rows = [], []
    for model, accession, wt_prefix, ko_prefix in MODELS:
        human = model == 'human_organoid'
        genes = [g.upper() if human else g for g in GENES]
        source, = (files/'geo'/accession).glob('*count_table.txt.gz' if human else '*TPM_Table.txt.gz')
        names, measured = load_target(source, genes, None if human else gene_map)
        assert set(genes) == set(measured)
        wt = [i for i,n in enumerate(names) if n.startswith(wt_prefix)]
        ko = [i for i,n in enumerate(names) if n.startswith(ko_prefix)]
        assert len(wt)>1 and len(ko)>1
        for gene in genes:
            expr = measured[gene]
            x = np.log2(1 + expr)
            def delta(omitted=None):
                return np.mean([x[i] for i in ko if i!=omitted]) - np.mean([x[i] for i in wt if i!=omitted])
            omissions = [delta(i) for i in wt+ko]
            rows.append([model,gene.upper(),len(wt),len(ko),np.mean(expr[wt]),np.mean(expr[ko]),delta(),min(omissions),max(omissions)])
            library_rows.extend([model,gene.upper(),names[i],'KO' if i in ko else 'WT',expr[i]] for i in wt+ko)
    tsv(HERE/'bulk.tsv','model gene wt_n ko_n wt_mean ko_mean log_delta omit_min omit_max'.split(),rows)
    tsv(HERE/'libraries.tsv','model gene library arm expression'.split(),library_rows)

def nuclei(files):
    rows = []
    def add(arm, group, depth, counts):
        assert len(depth)>0 and depth.sum()>0
        for gene in GENES:
            obs = counts[gene]
            rows.append([arm,group,len(depth),int(depth.sum()),gene,int(obs.sum()),int(np.count_nonzero(obs)),1e6*obs.sum()/depth.sum()])
    for arm,group,depth,counts in assigned_nuclei(files,[],[],GENES):
        add(arm, group, depth, counts)
    for arm in ('ctrl','ko'):
        root = files/'geo/GSE158684'
        prefix = 'GSE158684_'+arm+'_filtered_'
        with gzip.open(root/(prefix+'features.tsv.gz'),'rt') as f:
            symbols = [line.split('\t')[1] for line in f]
        with gzip.open(root/(prefix+'matrix.mtx.gz'),'rt') as f:
            dimensions = next(line for line in f if not line.startswith('%'))
            n = int(dimensions.split()[1])
            matrix = np.fromstring(f.read(),dtype=np.int64,sep=' ').reshape(-1,3)
        depth = np.bincount(matrix[:,1]-1,weights=matrix[:,2],minlength=n)
        wanted = set(GENES+['Aqp4','Aldh1l1'])
        keep_ids = [i for i,g in enumerate(symbols,1) if g in wanted]
        subset = matrix[np.isin(matrix[:,0],keep_ids)]
        counts = {}
        for i in keep_ids:
            entries = subset[subset[:,0]==i]
            gene = symbols[i-1]
            counts[gene] = counts.get(gene,0) + np.bincount(entries[:,1]-1,weights=entries[:,2],minlength=n)
        both = (depth>=500)&(counts['Aqp4']>0)&(counts['Aldh1l1']>0)
        add(arm,'Aqp4_and_Aldh1l1',depth[both],{g:counts[g][both] for g in GENES})
    tsv(HERE/'nuclei.tsv','pool subset n_nuclei total_UMI gene gene_UMI positive_nuclei CPM'.split(),rows)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('files',type=Path)
    args = parser.parse_args()
    bulk(args.files)
    nuclei(args.files)

"""Descriptive expression-matched backgrounds for the three prespecified flavin steps."""
from pathlib import Path
import sys
import csv
import gzip
from collections import defaultdict
import numpy as np

def load_all(files, accession, wt_prefix, ko_prefix, transcript_map):
    human = accession == 'GSE156243'
    pattern = '*count_table.txt.gz' if human else '*TPM_Table.txt.gz'
    source, = (files/'geo'/accession).glob(pattern)
    offset = 1 if human else 3
    by_name = {}
    folded = defaultdict(set)
    with gzip.open(source, 'rt') as stream:
        rows = csv.reader(stream, delimiter='\t')
        names = next(rows)[offset:]
        library = np.zeros(len(names))
        for row in rows:
            symbol = row[0] if human else transcript_map.get(row[0].split('.')[0])
            values = np.array(row[offset:], float)
            if human:
                library += values
            if symbol:
                folded[symbol.upper()].add(symbol)
                by_name[symbol] = by_name.get(symbol, 0) + values
    w = [i for i,n in enumerate(names) if n.startswith(wt_prefix)]
    k = [i for i,n in enumerate(names) if n.startswith(ko_prefix)]
    summary = {}
    for symbol, values in by_name.items():
        key = symbol.upper()
        if len(folded[key]) != 1:
            continue
        if human:
            values = values * 1e6 / library
        wt = np.log2(1 + values[w])
        ko = np.log2(1 + values[k])
        if wt.mean() <= 0:
            continue
        # Max difference when each WT or KO is removed individually.
        omit_worst = max(ko.mean() - (wt.sum()-wt.max())/(len(wt)-1),
                         (ko.sum()-ko.min())/(len(ko)-1) - wt.mean())
        summary[key] = (wt.mean(), ko.mean()-wt.mean(), omit_worst)
    return summary

def run(files, base, out):
    sys.path.insert(0,str(base/'ganaxolone_20261123'))
    from analyze import reference
    transcript_map,_ = reference(files)
    models=[('GSE158682','CRTX_S_Ctrl_','CRTX_S_KO_'),('GSE156243','cwt','cko'),('GSE158681','S_Ctrl_','S_KO_')]
    studies=[load_all(files,*model,transcript_map) for model in models]
    common=sorted(set.intersection(*(set(s) for s in studies)))
    data=np.array([[s[g] for s in studies] for g in common])
    scaled=data[:,:,0]/data[:,:,0].std(axis=0)
    targets=['SLC52A2','RFK','FLAD1']
    # Require exact agreement with the separate targeted implementation.
    panel = base/'continuous_compounds/riboflavin/screen.tsv'
    with panel.open() as stream:
        measured = {(row['accession'],row['gene']): row for row in csv.DictReader(stream,delimiter='\t')}
    for gene in targets:
        for i, (accession, _, _) in enumerate(models):
            row = measured[accession,gene]
            assert np.allclose(data[common.index(gene),i,1:], [float(row['delta']),float(row['omit_max'])], atol=1e-10)
    pool=np.array([i for i,g in enumerate(common) if g not in targets])
    with out.open('w') as stream:
        writer=csv.writer(stream,delimiter='\t',lineterminator='\n')
        writer.writerow(['target','same_symbol_universe','neighbors','down_all_three','omit_negative_all_three','max_distance'])
        for gene in targets:
            distance=np.linalg.norm(scaled-scaled[common.index(gene)],axis=1)
            near=pool[np.argsort(distance[pool],kind='stable')]
            for n in (100,200,500):
                subset=near[:n]
                writer.writerow([gene,len(common),n,int((data[subset,:,1]<0).all(axis=1).sum()),int((data[subset,:,2]<0).all(axis=1).sum()),round(distance[subset[-1]],5)])
if __name__=='__main__':
    run(Path(sys.argv[1]),Path(sys.argv[2]),Path(__file__).with_name('background.tsv'))

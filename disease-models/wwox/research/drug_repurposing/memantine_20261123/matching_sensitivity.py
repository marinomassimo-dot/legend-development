"""Ask whether arbitrary greedy matching order determined the murine tissue verdict."""
import argparse
import csv
from pathlib import Path

import numpy as np

from learn_signature import study, write
from test_wwox import references, load


def read_tsv(path):
    with path.open() as f:
        return list(csv.DictReader(f, delimiter="\t"))


def contrasts(values, names, case, control):
    c = [i for i,n in enumerate(names) if n.startswith(case)]
    k = [i for i,n in enumerate(names) if n.startswith(control)]
    changes = []
    for omit in [None, *c, *k]:
        changes.append(values[:, [i for i in c if i!=omit]].mean(axis=1)
                       - values[:, [i for i in k if i!=omit]].mean(axis=1))
    return np.array(changes)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("counts","soft","files","gene_info","out"):
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    pairs = read_tsv(args.out/"pairs.tsv")
    hits = [r for r in pairs if r["arm"]=="hit"]
    controls = read_tsv(args.out/"candidate_pool.tsv")
    scale = np.array([float(r["eligible_sd"]) for r in read_tsv(args.out/"matching.tsv")])
    labels = [r["ensembl"] for r in hits+controls]
    columns = ["basal_logCPM","induction","passive"]
    descriptors = np.array([[float(r[c]) for c in columns] for r in hits+controls])
    nh = len(hits)
    distance = np.linalg.norm((descriptors[:nh,None,:]-descriptors[None,nh:,:])/scale,axis=2)
    order = np.argsort(distance,axis=1,kind="stable")
    refs,_,_=references(args.files/"reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz",
                        args.files/"geo/GSE156243/hgnc_complete_set_20261022.json", args.gene_info,set(labels))
    mouse_d = []
    for cohort,case,ctrl in [("GSE158681","S_KO_","S_Ctrl_"),("GSE158682","CRTX_S_KO_","CRTX_S_Ctrl_")]:
        path, = (args.files/"geo"/cohort).glob("*TPM_Table.txt.gz")
        names,v = load(path,refs,True)
        mouse_d.append(contrasts(np.array([v[g] for g in labels]),names,case,ctrl))
    source,_,x,metadata = study(args.counts,args.soft)
    ix = [source.index(g) for g in labels]
    validation = np.array([x[ix,metadata[p,"1h Bic + 1h TTX & NMDA"]] - x[ix,metadata[p,"1h Bic + 1h TTX"]] for p in (7,8)])
    rng = np.random.default_rng(20261123)
    records = []
    for draw in range(501):
        sequence = range(nh) if draw == 0 else rng.permutation(nh)
        selected = set()
        for h in sequence:
            c = next(j for j in order[h] if j not in selected)
            selected.add(c)
        idx = [j+nh for j in sorted(selected)]
        def score(matrix):
            return matrix[:,:nh].mean(axis=1)-matrix[:,idx].mean(axis=1)
        if draw == 0:
            assert {labels[j] for j in idx} == {r["ensembl"] for r in pairs if r["arm"]=="control"}
        held = score(validation)
        hipp,ctx = (score(m) for m in mouse_d)
        records.append([draw, *held, hipp[0], hipp[1:].max(), ctx[0],ctx[1:].max(),
                       int(max(held)<0 and max(hipp)<0 and max(ctx)<0)])
    write(args.out/"rematching.tsv","draw held7 held8 hippo hippo_loo_max cortex cortex_loo_max all_gates",records)


if __name__=="__main__":
    main()

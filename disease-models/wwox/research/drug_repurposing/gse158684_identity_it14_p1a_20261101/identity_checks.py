#!/usr/bin/env python3
"""IT14 p1a: what the GSE158684 matrices themselves say about pre-deposit filtering, sex composition
(a partial animal-identity handle) and Wwox in glia vs neurons (ambient test). numpy only.
usage: identity_checks.py [--help] [DATA_DIR] [LABEL_DIR] [OUT_DIR]"""
import sys, gzip, os
import numpy as np
if '--help' in sys.argv or '-h' in sys.argv:
    print(__doc__); sys.exit(0)
D = sys.argv[1] if len(sys.argv) > 1 else '/home/desktop/legend-development/files/geo/GSE158684'
L = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'snrna_it13b_pv_20261031', 'results')
O = sys.argv[3] if len(sys.argv) > 3 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results')
os.makedirs(O, exist_ok=True)
SEX = ['Xist', 'Tsix', 'Ddx3y', 'Uty', 'Kdm5d', 'Eif2s3y']
def load(arm):
    feats = [l.split('\t')[1] for l in gzip.open(f'{D}/GSE158684_{arm}_filtered_features.tsv.gz', 'rt').read().splitlines()]
    with gzip.open(f'{D}/GSE158684_{arm}_filtered_matrix.mtx.gz', 'rt') as fh:
        for _ in range(2): fh.readline()
        ng, nc, nnz = map(int, fh.readline().split())
        a = np.fromstring(fh.read(), dtype=np.int64, sep=' ').reshape(-1, 3)
    return feats, nc, a[:, 0] - 1, a[:, 1] - 1, a[:, 2]
rows_qc, rows_sex, rows_w = [], [], []
for arm in ('ctrl', 'ko'):
    feats, nc, r, c, v = load(arm)
    idx = {}
    for i, g in enumerate(feats): idx.setdefault(g, i)
    tot = np.bincount(c, weights=v, minlength=nc); ng = np.bincount(c, minlength=nc)
    mt = np.array([f.startswith('mt-') for f in feats])
    mtu = np.bincount(c[mt[r]], weights=v[mt[r]], minlength=nc)
    def q(x, p): return float(np.percentile(x, p))
    rows_qc.append([arm, nc, f'{q(ng,0):.0f}', f'{q(ng,50):.0f}', f'{q(ng,100):.0f}', int((ng < 200).sum()), int((ng > 2500).sum()),
                    f'{q(tot,0):.0f}', f'{q(tot,50):.0f}', f'{q(tot,100):.0f}', int((tot > 15000).sum()), f'{q(mtu/tot,100):.4f}', int(((mtu/tot) > 0.03).sum())])
    def g(name):
        m = r == idx[name]
        return np.bincount(c[m], weights=v[m], minlength=nc)
    X = {s: g(s) for s in SEX if s in idx}
    ysum = sum(X[s] for s in ('Ddx3y', 'Uty', 'Kdm5d', 'Eif2s3y') if s in X)
    xi = X['Xist']
    for lab, m in (('all', np.ones(nc, bool)),):
        rows_sex.append([arm, nc, int((xi > 0).sum()), int((ysum > 0).sum()), int(((xi > 0) & (ysum > 0)).sum()),
                         int((xi >= 2).sum()), int((ysum >= 2).sum()), int(((xi >= 2) & (ysum >= 2)).sum()),
                         int(xi.sum()), int(ysum.sum())])
    lab = [l.rstrip('\n').split('\t') for l in open(f'{L}/labels_{arm}.tsv')][1:]
    cls = np.array([x[1] for x in lab]); assert len(cls) == nc
    w = g('Wwox'); sn = g('Snap25'); gm = g('Mbp')
    for k in ('excitatory', 'inhibitory', 'oligo', 'astro', 'doublet'):
        m = cls == k
        if m.sum() == 0: continue
        rows_w.append([arm, k, int(m.sum()), int(w[m].sum()), f'{(w[m] > 0).mean():.3f}', f'{np.median(tot[m]):.0f}',
                       f'{sn[m].sum()/tot[m].sum()*1e4:.2f}', f'{w[m].sum()/tot[m].sum()*1e4:.2f}'])
    if arm == 'ctrl':   # ambient test: do Wwox-positive oligo/astro nuclei carry more neuronal Snap25 ambient?
        for k in ('oligo', 'astro'):
            m = cls == k; pos = m & (w > 0); neg = m & (w == 0)
            rows_w.append([arm, f'AMBTEST_{k}_Wwoxpos_vs_neg_Snap25_per1e4', int(pos.sum()), int(neg.sum()),
                           f'{sn[pos].sum()/tot[pos].sum()*1e4:.2f}', f'{sn[neg].sum()/tot[neg].sum()*1e4:.2f}',
                           f'{np.median(tot[pos]):.0f}', f'{np.median(tot[neg]):.0f}'])
def wr(name, hdr, rows):
    with open(f'{O}/{name}', 'w') as f:
        f.write('\t'.join(hdr) + '\n')
        for x in rows: f.write('\t'.join(map(str, x)) + '\n')
wr('deposit_prefilter_qc.tsv', ['arm','nuclei','genes_min','genes_median','genes_max','n_genes_lt200','n_genes_gt2500','umi_min','umi_median','umi_max','n_umi_gt15000','mt_frac_max','n_mt_gt3pct'], rows_qc)
wr('sex_genes_by_arm.tsv', ['arm','nuclei','Xist_pos','Y_pos','both_pos','Xist_ge2','Y_ge2','both_ge2','Xist_UMI','Y_UMI'], rows_sex)
wr('wwox_glia_ambient.tsv', ['arm','class_or_test','n1','n2_or_Wwox_UMI','a','b','c','d'], rows_w)
print('done')

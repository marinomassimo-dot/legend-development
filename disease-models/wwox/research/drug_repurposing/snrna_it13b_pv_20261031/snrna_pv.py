#!/usr/bin/env python3
"""IT13b: nucleus-resolved PV composition from GSE158684 (numpy only). Rules fixed in PRE_ANALYSIS.md.
usage: snrna_pv.py [--help] [DATA_DIR] [OUT_DIR]"""
import sys, gzip, io, os
import numpy as np
if '--help' in sys.argv or '-h' in sys.argv:
    print(__doc__); sys.exit(0)
D = sys.argv[1] if len(sys.argv) > 1 else '/home/desktop/legend-development/files/geo/GSE158684'
O = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results')
os.makedirs(O, exist_ok=True)
rng = np.random.default_rng(20261031)
G = {'EXC': ['Slc17a7','Slc17a6','Camk2a','Neurod6','Satb2'], 'INH': ['Gad1','Gad2','Slc32a1'],
     'PAN': ['Snap25','Syt1','Rbfox3','Stmn2'], 'OLIGO': ['Mbp','Plp1','Mog','Mobp'],
     'ASTRO': ['Aqp4','Gja1','Slc1a2','Aldh1l1'], 'OPC': ['Pdgfra','Vcan','Cspg4'],
     'MICRO': ['Csf1r','Cx3cr1','P2ry12','Hexb']}
EXTRA = ['Pvalb','Sst','Vip','Lhx6','Htr3a','Npy','Kcnc1','Kcnc2','Dcx','Sox11','Sox4','Igfbpl1','Nnat','Atp1a3','Cck','Enpp6','Bmp4','Wwox','Tubb3','Gad1','Gad2']
need = sorted({g for v in G.values() for g in v} | set(EXTRA))

def load(arm):
    feats = [l.split('\t')[1] for l in gzip.open(f'{D}/GSE158684_{arm}_filtered_features.tsv.gz','rt').read().splitlines()]
    nb = len(gzip.open(f'{D}/GSE158684_{arm}_filtered_barcodes.tsv.gz','rt').read().splitlines())
    idx = {}
    for i, g in enumerate(feats):
        idx.setdefault(g, i)  # first occurrence; duplicates reported
    dup = len(feats) - len(set(feats))
    with gzip.open(f'{D}/GSE158684_{arm}_filtered_matrix.mtx.gz','rt') as fh:
        for _ in range(2): fh.readline()
        ng, nc, nnz = map(int, fh.readline().split())
        a = np.loadtxt(fh, dtype=np.int64) if False else np.fromstring(fh.read(), dtype=np.int64, sep=' ').reshape(-1, 3)
    assert a.shape[0] == nnz and nc == nb
    r, c, v = a[:,0]-1, a[:,1]-1, a[:,2]
    tot = np.bincount(c, weights=v, minlength=nc)
    ngenes = np.bincount(c, minlength=nc)
    X = {}
    for g in need:
        if g not in idx: X[g] = None; continue
        m = r == idx[g]
        X[g] = np.bincount(c[m], weights=v[m], minlength=nc)
    return X, tot, ngenes, dup

def gsum(X, names, nc):
    s = np.zeros(nc)
    for g in names:
        if X[g] is not None: s += X[g]
    return s

def classify(X, tot):
    nc = len(tot)
    exc, inh, pan = (gsum(X, G[k], nc) for k in ('EXC','INH','PAN'))
    gl = np.stack([gsum(X, G[k], nc) for k in ('OLIGO','ASTRO','OPC','MICRO')])
    glmax = gl.max(0); glarg = gl.argmax(0)
    dbl = ((exc >= 3) & (inh >= 3)) | ((glmax >= 3) & ((exc >= 3) | (inh >= 3)))
    lab = np.full(nc, 'other', dtype=object)
    lab[(pan >= 2)] = 'unassigned_neuron'
    glia = (glmax >= 3) & (glmax > pan)
    names = np.array(['oligo','astro','opc','micro'])
    lab[glia] = names[glarg[glia]]
    lab[(exc >= 2) & (exc > inh)] = 'excitatory'
    lab[(inh >= 2) & (inh > exc)] = 'inhibitory'
    lab[dbl] = 'doublet'
    # glia rule 4 must not override 2/3: reapply order properly
    lab2 = np.full(nc, 'other', dtype=object)
    lab2[(pan >= 2)] = 'unassigned_neuron'
    lab2[glia] = names[glarg[glia]]
    m3 = (exc >= 2) & (exc > inh); lab2[m3] = 'excitatory'
    m2 = (inh >= 2) & (inh > exc); lab2[m2] = 'inhibitory'
    lab2[dbl] = 'doublet'
    # rules order is 1,2,3,4,5 with first match winning: inhibitory beats excitatory beats glia beats unassigned
    out = np.full(nc, 'other', dtype=object)
    out[(pan >= 2)] = 'unassigned_neuron'
    out[glia] = names[glarg[glia]]
    out[m3] = 'excitatory'
    out[m2] = 'inhibitory'
    out[dbl] = 'doublet'
    return out

def sub(X, lab):
    nc = len(lab); s = np.full(nc, '', dtype=object)
    g = lambda n: (X[n] if X[n] is not None else np.zeros(nc))
    inh = lab == 'inhibitory'
    sst = inh & (g('Sst') >= 1); vip = inh & ~sst & (g('Vip') >= 1)
    pva = inh & ~sst & ~vip & (g('Pvalb') >= 1)
    oth = inh & ~sst & ~vip & ~pva
    s[sst] = 'SST'; s[vip] = 'VIP'; s[pva] = 'PV_A'; s[oth] = 'otherINH'
    pvb = inh & (g('Lhx6') >= 1) & (g('Sst') == 0) & (g('Vip') == 0) & (g('Htr3a') == 0)
    return s, pvb

def cp(k, n, a=0.05):
    # Clopper-Pearson via bisection on binomial tail (numpy only)
    from math import lgamma, log, exp
    def cdf(x, p):  # P(X<=x), log-space
        if p <= 0: return 1.0
        if p >= 1: return 1.0 if x >= n else 0.0
        return min(1.0, sum(exp(lgamma(n+1)-lgamma(i+1)-lgamma(n-i+1)+i*log(p)+(n-i)*log(1-p)) for i in range(0, x+1)))
    def bis(f, lo=0.0, hi=1.0):
        for _ in range(60):
            mid = (lo+hi)/2
            if f(mid): hi = mid
            else: lo = mid
        return (lo+hi)/2
    if n == 0: return (float('nan'), float('nan'))
    lo = 0.0 if k == 0 else bis(lambda p: 1 - cdf(k-1, p) >= a/2)
    hi = 1.0 if k == n else bis(lambda p: cdf(k, p) <= a/2, 0.0, 1.0)
    return lo, hi

def fisher(a, b, c, d):
    # two-sided exact: sum of probs <= observed; table [[a,b],[c,d]]
    from math import lgamma, exp
    lf = lambda n: lgamma(n+1)
    n1, n2, m1 = a+b, c+d, a+c
    N = n1+n2
    def lp(x): return lf(n1)+lf(n2)+lf(m1)+lf(N-m1)-lf(N)-lf(x)-lf(n1-x)-lf(m1-x)-lf(n2-m1+x)
    lo, hi = max(0, m1-n2), min(n1, m1)
    po = exp(lp(a)); tot = 0.0
    for x in range(lo, hi+1):
        p = exp(lp(x))
        if p <= po*(1+1e-9): tot += p
    return min(1.0, tot)

def frac_row(name, k0, n0, k1, n1, rows):
    f0, f1 = k0/n0 if n0 else float('nan'), k1/n1 if n1 else float('nan')
    c0, c1 = cp(k0, n0), cp(k1, n1)
    ratio = f1/f0 if f0 > 0 else float('nan')
    p = fisher(k1, n1-k1, k0, n0-k0) if n0 and n1 else float('nan')
    rows.append([name, k0, n0, f'{f0:.4f}', f'{c0[0]:.4f}', f'{c0[1]:.4f}', k1, n1, f'{f1:.4f}', f'{c1[0]:.4f}', f'{c1[1]:.4f}', f'{ratio:.3f}', f'{p:.3g}'])

def wtsv(path, hdr, rows):
    with open(path, 'w') as f:
        f.write('\t'.join(hdr)+'\n')
        for r in rows: f.write('\t'.join(str(x) for x in r)+'\n')

arms = {}
for arm in ('ctrl', 'ko'):
    X, tot, ng, dup = load(arm)
    lab = classify(X, tot); s, pvb = sub(X, lab)
    arms[arm] = dict(X=X, tot=tot, ng=ng, lab=lab, sub=s, pvb=pvb, dup=dup)

FH = ['quantity','ctrl_k','ctrl_n','ctrl_frac','ctrl_lo','ctrl_hi','ko_k','ko_n','ko_frac','ko_lo','ko_hi','ratio_ko_over_ctrl','fisher_p_descriptive']
def fractions(excl_dbl=True):
    rows = []
    A, B = arms['ctrl'], arms['ko']
    for tag, f in (('all_nuclei', lambda a: np.ones(len(a['lab']), bool)),):
        pass
    def cnt(a, mask): return int(mask.sum())
    classes = ['excitatory','inhibitory','oligo','astro','opc','micro','unassigned_neuron','other','doublet']
    tot0, tot1 = len(A['lab']), len(B['lab'])
    nd0, nd1 = int((A['lab']!='doublet').sum()), int((B['lab']!='doublet').sum())
    for c in classes:
        k0, k1 = int((A['lab']==c).sum()), int((B['lab']==c).sum())
        frac_row(f'{c}/all_nuclei', k0, tot0, k1, tot1, rows)
        if c != 'doublet': frac_row(f'{c}/nondoublet', k0, nd0, k1, nd1, rows)
    neu = lambda a: np.isin(a['lab'], ['excitatory','inhibitory','unassigned_neuron'])
    n0, n1 = int(neu(A).sum()), int(neu(B).sum())
    for c in ('inhibitory','excitatory'):
        frac_row(f'{c}/neurons', int((A['lab']==c).sum()), n0, int((B['lab']==c).sum()), n1, rows)
    i0, i1 = int((A['lab']=='inhibitory').sum()), int((B['lab']=='inhibitory').sum())
    for c in ('PV_A','SST','VIP','otherINH'):
        frac_row(f'{c}/inhibitory', int((A['sub']==c).sum()), i0, int((B['sub']==c).sum()), i1, rows)
    frac_row('PV_B/inhibitory', int(A['pvb'].sum()), i0, int(B['pvb'].sum()), i1, rows)
    frac_row('PV_A/all_nuclei', int((A['sub']=='PV_A').sum()), tot0, int((B['sub']=='PV_A').sum()), tot1, rows)
    frac_row('PV_B/nondoublet', int(A['pvb'].sum()), nd0, int(B['pvb'].sum()), nd1, rows)
    # sensitivity: Pvalb>=1 among all inhibitory regardless of Sst/Vip
    for nm, a in (('x',A),('y',B)): pass
    k0 = int(((A['lab']=='inhibitory') & (A['X']['Pvalb']>=1)).sum()); k1 = int(((B['lab']=='inhibitory') & (B['X']['Pvalb']>=1)).sum())
    frac_row('Pvalb_detected/inhibitory', k0, i0, k1, i1, rows)
    k0 = int((A['X']['Pvalb']>=1).sum()); k1 = int((B['X']['Pvalb']>=1).sum())
    frac_row('Pvalb_detected/all_nuclei', k0, tot0, k1, tot1, rows)
    return rows
wtsv(f'{O}/class_fractions.tsv', FH, fractions())

# Pvalb per nucleus and marker means per class
def norm(a, g):
    x = a['X'][g]
    return None if x is None else x / a['tot'] * 1e4
def boot_diff(x0, x1, B=2000):
    if len(x0) == 0 or len(x1) == 0: return (float('nan'),)*3
    d = x1.mean() - x0.mean()
    bs = np.array([rng.choice(x1, len(x1)).mean() - rng.choice(x0, len(x0)).mean() for _ in range(B)])
    return d, np.percentile(bs, 2.5), np.percentile(bs, 97.5)
rows = []
sets = {'PV_B': lambda a: a['pvb'], 'PV_A': lambda a: a['sub']=='PV_A', 'inhibitory': lambda a: a['lab']=='inhibitory',
        'SST': lambda a: a['sub']=='SST', 'VIP': lambda a: a['sub']=='VIP', 'excitatory': lambda a: a['lab']=='excitatory',
        'oligo': lambda a: a['lab']=='oligo', 'astro': lambda a: a['lab']=='astro', 'opc': lambda a: a['lab']=='opc',
        'micro': lambda a: a['lab']=='micro', 'neurons': lambda a: np.isin(a['lab'],['excitatory','inhibitory','unassigned_neuron'])}
genes = ['Pvalb','Kcnc1','Kcnc2','Lhx6','Gad1','Gad2','Npy','Sst','Vip','Cck','Dcx','Sox11','Sox4','Igfbpl1','Nnat','Atp1a3','Wwox','Enpp6','Bmp4']
for sname, fn in sets.items():
    m0, m1 = fn(arms['ctrl']), fn(arms['ko'])
    for g in genes:
        if arms['ctrl']['X'][g] is None: continue
        x0, x1 = norm(arms['ctrl'], g)[m0], norm(arms['ko'], g)[m1]
        d, lo, hi = boot_diff(x0, x1, 1000)
        r0 = arms['ctrl']['X'][g][m0]; r1 = arms['ko']['X'][g][m1]
        rows.append([sname, g, int(m0.sum()), int(m1.sum()), f'{x0.mean():.3f}' if len(x0) else 'NA', f'{x1.mean():.3f}' if len(x1) else 'NA',
                     f'{d:.3f}', f'{lo:.3f}', f'{hi:.3f}', f'{(r0>=1).mean():.3f}' if len(r0) else 'NA', f'{(r1>=1).mean():.3f}' if len(r1) else 'NA', int(r0.sum()), int(r1.sum())])
wtsv(f'{O}/class_gene_means.tsv', ['class','gene','n_ctrl','n_ko','mean_norm_ctrl','mean_norm_ko','diff_ko_minus_ctrl','boot_lo','boot_hi','detect_frac_ctrl','detect_frac_ko','umi_sum_ctrl','umi_sum_ko'], rows)

# totals and ambient
rows = []
for arm, a in arms.items():
    for sname in ('inhibitory','excitatory','oligo','astro','opc','micro','PV_B','doublet'):
        m = (a['lab']==sname) if sname not in ('PV_B',) else a['pvb']
        if m.sum() == 0: continue
        t = a['tot'][m]
        rows.append([arm, sname, int(m.sum()), f'{np.median(t):.0f}', f'{t.mean():.0f}', f'{np.median(a["ng"][m]):.0f}'])
wtsv(f'{O}/depth.tsv', ['arm','class','n','median_UMI','mean_UMI','median_genes'], rows)
rows = []
for arm, a in arms.items():
    for gl in ('oligo','astro','micro','opc','excitatory'):
        m = a['lab']==gl
        if m.sum() == 0: continue
        u = a['tot'][m].sum()
        for g in ('Pvalb','Gad1','Snap25','Sst','Npy'):
            if a['X'][g] is None: continue
            rows.append([arm, gl, int(m.sum()), g, int(a['X'][g][m].sum()), f'{a["X"][g][m].sum()/u*1e4:.3f}'])
wtsv(f'{O}/ambient_indicator.tsv', ['arm','nonINH_class','n_nuclei','gene','umi','umi_per_1e4_umi'], rows)
rows = []
for arm, a in arms.items():
    t = a['tot']; rows.append([arm, len(t), int(a['dup']), f'{np.median(t):.0f}', f'{t.mean():.0f}', f'{np.median(a["ng"]):.0f}', int((a['lab']=='doublet').sum()),
        int((a['lab']=='other').sum()), f'{a["X"]["Wwox"].sum() if a["X"]["Wwox"] is not None else -1:.0f}'])
wtsv(f'{O}/arm_qc.tsv', ['arm','nuclei','duplicate_feature_names','median_UMI','mean_UMI','median_genes','doublet_flagged','other_unclassified','Wwox_UMI_total'], rows)
# Wwox by class (is Wwox deleted in neurons only?)
rows = []
for arm, a in arms.items():
    for sname in ('excitatory','inhibitory','oligo','astro'):
        m = a['lab']==sname
        if m.sum() and a['X']['Wwox'] is not None:
            rows.append([arm, sname, int(m.sum()), int(a['X']['Wwox'][m].sum()), f'{(a["X"]["Wwox"][m]>=1).mean():.3f}', f'{(a["X"]["Wwox"][m]/a["tot"][m]*1e4).mean():.3f}'])
wtsv(f'{O}/wwox_by_class.tsv', ['arm','class','n','Wwox_UMI','detect_frac','mean_norm'], rows)
# permutation (descriptive only): PV_A/inh fraction, nuclei-label shuffle among inhibitory nuclei
inh0, inh1 = (arms['ctrl']['lab']=='inhibitory'), (arms['ko']['lab']=='inhibitory')
isP = np.concatenate([(arms['ctrl']['sub']=='PV_A')[inh0], (arms['ko']['sub']=='PV_A')[inh1]]).astype(int)
obs = isP[inh0.sum():].mean() - isP[:inh0.sum()].mean()
cnt = 0
for _ in range(10000):
    p = rng.permutation(isP); d = p[inh0.sum():].mean() - p[:inh0.sum()].mean()
    cnt += abs(d) >= abs(obs) - 1e-12
wtsv(f'{O}/permutation_descriptive.tsv', ['statistic','observed','n_perm','p_nuclei_label_shuffle_NOT_a_replicate_test'], [['PV_A_frac_of_inhibitory_KO_minus_ctrl', f'{obs:.4f}', 10000, f'{cnt/10000:.4f}']])
# per-nucleus labels for the verifier
for arm, a in arms.items():
    with open(f'{O}/labels_{arm}.tsv', 'w') as f:
        f.write('index\tclass\tsubclass\tPV_B\tPvalb_UMI\ttotal_UMI\n')
        for i in range(len(a['lab'])):
            f.write(f'{i}\t{a["lab"][i]}\t{a["sub"][i]}\t{int(a["pvb"][i])}\t{int(a["X"]["Pvalb"][i])}\t{int(a["tot"][i])}\n')
print('done', {k: {c: int((v['lab']==c).sum()) for c in set(v['lab'])} for k, v in arms.items()})

# Added after first look (post hoc, labelled as such in README): pseudo-bulk and Pvalb-by-class including doublets
rows = []
for arm, a in arms.items():
    T = a['tot'].sum()
    for g in ('Pvalb','Kcnc1','Kcnc2','Gad1','Gad2','Slc32a1','Sst','Npy','Vip','Snap25','Slc17a7','Mbp','Plp1','Wwox'):
        if a['X'][g] is not None:
            rows.append([arm, g, int(a['X'][g].sum()), f'{a["X"][g].sum()/T*1e6:.2f}', int((a['X'][g]>=1).sum())])
wtsv(f'{O}/pseudobulk.tsv', ['arm','gene','umi_total','cpm_of_total_umi','nuclei_detected'], rows)
rows = []
for arm, a in arms.items():
    pv = a['X']['Pvalb']
    for c in sorted(set(a['lab'])):
        m = a['lab']==c
        rows.append([arm, c, int(m.sum()), int(pv[m].sum()), int((pv[m]>=1).sum())])
wtsv(f'{O}/pvalb_by_class_incl_doublets.tsv', ['arm','class','n','Pvalb_UMI','nuclei_Pvalb_detected'], rows)

# Pseudo-bulk rate ratio (KO/ctrl) of UMI share, exact conditional binomial interval (nuclei pooled; descriptive)
rows = []
T0, T1 = arms['ctrl']['tot'].sum(), arms['ko']['tot'].sum()
for g in ('Pvalb','Kcnc1','Gad1','Gad2','Sst','Npy','Vip','Mbp','Wwox'):
    k0, k1 = int(arms['ctrl']['X'][g].sum()), int(arms['ko']['X'][g].sum())
    lo, hi = cp(k1, k0+k1)
    f = lambda p: (p/(1-p)) * (T0/T1)   # share odds -> rate ratio
    rows.append([g, k0, k1, f'{(k1/T1)/(k0/T0):.3f}', f'{np.log2((k1/T1)/(k0/T0)):.2f}', f'{f(lo):.3f}' if lo > 0 else '0', f'{f(hi):.3f}' if hi < 1 else 'inf'])
wtsv(f'{O}/pseudobulk_rate_ratio.tsv', ['gene','umi_ctrl','umi_ko','rate_ratio_ko_over_ctrl','log2','exact_lo','exact_hi'], rows)

# POST HOC sensitivity S2 (not in PRE_ANALYSIS): doublet only = exc>=3 and inh>=3 (glia+neuron co-detection no longer excluded, because
# abundant Mbp/Plp1 ambient RNA flags many real neurons); inhibitory per original rule; PV-class and Pvalb per nucleus recomputed.
rows = []
tmp = {}
for arm, a in arms.items():
    X = a['X']; nc = len(a['tot'])
    exc, inh = gsum(X, G['EXC'], nc), gsum(X, G['INH'], nc)
    dbl = (exc >= 3) & (inh >= 3)
    ih = (inh >= 2) & (inh > exc) & ~dbl
    ex = (exc >= 2) & (exc > inh) & ~dbl
    pv = X['Pvalb']; sst = X['Sst']; vip = X['Vip']
    pva = ih & (sst == 0) & (vip == 0) & (pv >= 1)
    pvb = ih & (X['Lhx6'] >= 1) & (sst == 0) & (vip == 0) & (X['Htr3a'] == 0)
    tmp[arm] = dict(n=nc, dbl=int(dbl.sum()), inh=int(ih.sum()), exc=int(ex.sum()), pva=int(pva.sum()), pvb=int(pvb.sum()),
                    pvu_inh=int(pv[ih].sum()), pvdet_inh=int((pv[ih]>=1).sum()), pvu_exc=int(pv[ex].sum()), pvu_all=int(pv.sum()), snap=int(X['Snap25'].sum()), gad1=int(X['Gad1'].sum()), gad2=int(X['Gad2'].sum()))
for k in tmp['ctrl']:
    rows.append([k, tmp['ctrl'][k], tmp['ko'][k]])
wtsv(f'{O}/sensitivity_S2_posthoc.tsv', ['quantity','ctrl','ko'], rows)
c, k = tmp['ctrl'], tmp['ko']
rows = []
frac_row('S2 inhibitory/nondoublet', c['inh'], c['n']-c['dbl'], k['inh'], k['n']-k['dbl'], rows)
frac_row('S2 PV_A/inhibitory', c['pva'], c['inh'], k['pva'], k['inh'], rows)
frac_row('S2 PV_B/inhibitory', c['pvb'], c['inh'], k['pvb'], k['inh'], rows)
frac_row('S2 Pvalb_detected/inhibitory', c['pvdet_inh'], c['inh'], k['pvdet_inh'], k['inh'], rows)
wtsv(f'{O}/sensitivity_S2_fractions_posthoc.tsv', FH, rows)
# Pvalb UMI relative to neuronal content (post hoc): per Snap25 UMI and per (Gad1+Gad2) UMI, exact conditional interval
rows = []
for nm, den in (('Snap25', 'snap'), ('Gad1+Gad2', None)):
    d0 = c['snap'] if den else c['gad1'] + c['gad2']; d1 = k['snap'] if den else k['gad1'] + k['gad2']
    k0, k1 = c['pvu_all'], k['pvu_all']
    ratio = (k1/d1)/(k0/d0); lo, hi = cp(k1, k0+k1)
    f = lambda p: (p/(1-p)) * (d0/d1)
    rows.append([nm, k0, k1, d0, d1, f'{ratio:.3f}', f'{np.log2(ratio):.2f}', f'{f(lo):.3f}', f'{f(hi):.3f}'])
wtsv(f'{O}/pvalb_relative_to_neuronal_posthoc.tsv', ['denominator','pvalb_ctrl','pvalb_ko','den_ctrl','den_ko','ratio','log2','exact_lo','exact_hi'], rows)

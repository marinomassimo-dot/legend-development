"""ADV-116: P14 set scores for GSE112627, exactly as pre-registered (f672781f3). Reads only P14 columns."""
import gzip, sys, random, statistics as st, math
path = sys.argv[1]
rows = gzip.open(path, 'rt').read().split('\n')
hdr = rows[0].split('\t')[1:]
cols = {h.split(': ')[1]: [] for h in hdr}
idx = {}
for i, h in enumerate(hdr):
    n, lab = h.split(': ')
    idx.setdefault(lab, []).append(i)
P14 = {'F1_KO': idx['P14_F1_KO'], 'F1_WT': idx['P14_F1_WT'], '129_KO': idx['P14_129_KO'], '129_WT': idx['P14_129_WT']}
assert [len(v) for v in P14.values()] == [3, 3, 3, 2], P14
data = {}
for r in rows[1:]:
    if not r.strip(): continue
    f = r.split('\t'); g = f[0]
    v = f[1:]
    try:
        data[g] = {k: [math.log2(float(v[i]) + 1) for i in ix] for k, ix in P14.items()}
    except ValueError:
        pass
SETS = {
 'ASTRO_REACTIVE': ['Gfap','Vim','C3','Lcn2','Cd44','Serpina3n','Stat3'],
 'MICRO_ID': ['Cx3cr1','P2ry12','Csf1r'],
 'MICRO_ACT': ['Aif1','Cd68','Trem2','Tyrobp','Lyz2','Itgax'],
 'ENERGY_GLYC': ['Pdk1','Pdk2','Pdk3','Pdk4','Ldha','Slc16a1','Hk2','Pfkp','Pkm','Slc2a1'],
 'ENERGY_OXPHOS': ['Cox4i1','Ndufa4','Atp5f1a','Uqcrc1','Sdha','Cs'],
 'ASTRO_ID(control)': ['Aqp4','Aldh1l1','Slc1a2'],
}
ALIAS = {'Atp5f1a': 'Atp5a1'}
def d_gene(g, ko, wt, drop_sample=None):
    a = data[g][ko]; b = data[g][wt]
    if drop_sample is not None:
        which, i = drop_sample
        if which == ko: a = [x for j, x in enumerate(a) if j != i]
        else: b = [x for j, x in enumerate(b) if j != i]
    return st.mean(a) - st.mean(b)
def present(genes):
    out = []; miss = []
    for g in genes:
        if g in data: out.append(g)
        elif ALIAS.get(g) in data: out.append(ALIAS[g])
        else: miss.append(g)
    return out, miss
random.seed(20261120)
def run(ko, wt, label):
    print(f'\n##### CONTRAST {label}: {ko} vs {wt}  (n {len(P14[ko])} vs {len(P14[wt])})')
    # expression deciles from the six primary-contrast samples (fixed to F1 per pre-registration)
    means = {g: st.mean(data[g]['F1_KO'] + data[g]['F1_WT']) for g in data}
    gs = sorted(means, key=lambda g: means[g]); n = len(gs)
    dec = {g: min(9, int(10 * i / n)) for i, g in enumerate(gs)}
    bydec = {k: [g for g in gs if dec[g] == k] for k in range(10)}
    allset = set(sum(([*present(v)[0]] for v in SETS.values()), []))
    res = []
    for name, genes in SETS.items():
        pg, miss = present(genes)
        if len(pg) < 4:
            print(f'{name}: NOT SCORED (present {len(pg)}; missing {miss})'); continue
        dg = {g: d_gene(g, ko, wt) for g in pg}
        D = st.mean(dg.values())
        # null
        cnt = 0; N = 10000
        pools = {k: [g for g in bydec[k] if g not in allset] for k in bydec}
        for _ in range(N):
            s = st.mean(d_gene(random.choice(pools[dec[g]]), ko, wt) for g in pg)
            if abs(s) >= abs(D): cnt += 1
        p = (cnt + 1) / (N + 1)
        # leave-one-gene-out
        logo = [st.mean(v for k, v in dg.items() if k != g) for g in pg]
        logo_ok = all((x > 0) == (D > 0) and abs(x) >= 0.07 for x in logo)
        # leave-one-sample-out
        loso = []
        for which in (ko, wt):
            for i in range(len(P14[which])):
                loso.append(st.mean(d_gene(g, ko, wt, (which, i)) for g in pg))
        loso_ok = all((x > 0) == (D > 0) for x in loso)
        res.append((name, pg, miss, D, p, logo, logo_ok, loso, loso_ok, dg))
    # Holm across scored sets excluding the control
    main = [r for r in res if not r[0].endswith('(control)')]
    order = sorted(range(len(main)), key=lambda i: main[i][4]); holm = {}
    m = len(main); run_max = 0
    for rank, i in enumerate(order):
        run_max = max(run_max, min(1, main[i][4] * (m - rank))); holm[main[i][0]] = run_max
    for (name, pg, miss, D, p, logo, logo_ok, loso, loso_ok, dg) in res:
        c1 = abs(D) >= 0.10; c2 = p <= 0.05
        fails = sum(not c for c in (c1, c2, logo_ok, loso_ok))
        verdict = 'DIFFERENT' if fails == 0 else ('NOT DIFFERENT' if (not c1 and not c2) else ('BOUNDARY' if fails == 1 else 'NOT DIFFERENT (>=2 criteria fail)'))
        print(f'{name}: genes {len(pg)} (missing {miss}) D={D:+.3f} log2  p_raw={p:.4f} Holm={holm.get(name,float("nan")):.3f}  |D|>=0.10:{c1} p<=0.05:{c2} LOGO_ok:{logo_ok} (min|x|={min(abs(x) for x in logo):.3f}) LOSO_ok:{loso_ok} (range {min(loso):+.3f}..{max(loso):+.3f})  => {verdict}')
        print('    per gene d:', ', '.join(f'{k}={v:+.2f}' for k, v in dg.items()))
run('F1_KO', 'F1_WT', 'PRIMARY')
run('129_KO', '129_WT', 'SECONDARY (descriptive)')

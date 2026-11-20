"""ADV-121: the pilot power table, computed under PREREGISTRATION_ADV121_SCI_20261120.md.

Reads the ADV-120 measurements (benchmark_card_adv120_sci_20261120/measurements) and this folder's
measurements_adv121/ (Fig 3C error bars; optionally figS7B_D.json). Prints the table; with --tsv writes
OUTPUT_power_table.tsv. No numbers are typed here except the spike-wave per-animal values of the SWD note
(panel 7E, measured on the raster in an earlier window) and the bar closures of section 4 of the ADV-120 result.
Usage: python3 -I compute_power_table.py [--tsv]
"""
import os, sys, json, math
from statistics import NormalDist

HERE = os.path.dirname(os.path.abspath(__file__))
M120 = os.path.join(os.path.dirname(HERE), 'benchmark_card_adv120_sci_20261120', 'measurements')
M121 = os.path.join(HERE, 'measurements_adv121')
ND = NormalDist()
Z_POWER = ND.inv_cdf(0.80)
ALPHAS = {'0.05': 0.05, '0.0125': 0.05 / 4}   # uncorrected; Holm worst case over four treated arms
BAR_C = {'weight': 0.5, 'clasp': 0.80, 'swd': 0.63}   # section 4 of the ADV-120 result
GLU_P20_BAR = 0.92      # times WT, section 4
GLIA_BAR = 1.2          # times WT (upper bound), section 4
DESIGN_N = 14           # v3.1 6.8: 13 to 14 per arm at the observed SD
REF_N = 50              # v3.1 6.8: about 50 at the SD upper bound


def jl(d, name):
    return json.load(open(os.path.join(d, name)))


def chi2_lower_quantile(p, df):
    """Quantile of chi-square(df) at lower tail p, by bisection on the regularised lower incomplete gamma."""
    def gammainc(a, x):
        if x <= 0:
            return 0.0
        if x < a + 1:
            s = t = 1.0 / a
            n = a
            while abs(t) > 1e-14 * abs(s):
                n += 1
                t *= x / n
                s += t
            return s * math.exp(-x + a * math.log(x) - math.lgamma(a))
        b = x + 1 - a
        c = 1e300
        d = 1 / b
        h = d
        for i in range(1, 500):
            an = -i * (i - a)
            b += 2
            d = an * d + b
            d = 1e-300 if abs(d) < 1e-300 else d
            c = b + an / c
            c = 1e-300 if abs(c) < 1e-300 else c
            d = 1 / d
            h *= d * c
        return 1 - math.exp(-x + a * math.log(x) - math.lgamma(a)) * h
    lo, hi = 1e-9, 200.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if gammainc(df / 2.0, mid / 2.0) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def sd_upper_factor(df, tail=0.05):
    """One-sided 95 percent upper bound of an SD from df degrees of freedom, as a multiple of the observed SD."""
    return math.sqrt(df / chi2_lower_quantile(tail, df))


def n_per_arm(delta, sd, alpha):
    z = ND.inv_cdf(1 - alpha / 2)
    return 2 * (z + Z_POWER) ** 2 * (sd / abs(delta)) ** 2 + 2


def klass(n):
    return 'fits' if n <= DESIGN_N else ('exceeds' if n <= REF_N else 'beyond')


def pool(a, b):
    return math.sqrt((a * a + b * b) / 2.0)


def main():
    tsv = '--tsv' in sys.argv
    F5 = sd_upper_factor(5)
    rows = []

    def add(family, age, kind, delta, sd, sdflag, note, dA=None, sdA=None):
        """kind: 'bar' (candidate at the bar vs LD level) or 'HD' (candidate as strong as HD vs LD) or 'vehicle'."""
        r = {'family': family, 'age': age, 'delta_kind': kind, 'delta': delta, 'sd_pool': sd, 'sd_flag': sdflag,
             'note': note}
        if sd is None or delta is None:
            r.update({k: None for k in ('n_obs_a05', 'n_ub_a05', 'n_obs_a0125', 'n_ub_a0125', 'cls_obs_holm', 'cls_ub_holm', 'd')})
        else:
            r['d'] = abs(delta) / sd
            r['n_obs_a05'] = n_per_arm(delta, sd, 0.05)
            r['n_ub_a05'] = n_per_arm(delta, sd * F5, 0.05)
            r['n_obs_a0125'] = n_per_arm(delta, sd, 0.0125)
            r['n_ub_a0125'] = n_per_arm(delta, sd * F5, 0.0125)
            r['cls_obs_holm'] = klass(r['n_obs_a0125'])
            r['cls_ub_holm'] = klass(r['n_ub_a0125'])
        # pixel spread: the same n with calibration B (offset-only differences give the same delta)
        if dA is not None and sdA is not None and delta is not None and sd:
            r['pixel_rel_change'] = abs(n_per_arm(dA, sdA, 0.0125) - r['n_obs_a0125']) / r['n_obs_a0125']
        else:
            r['pixel_rel_change'] = None
        rows.append(r)

    # ---- weight (g), Fig 3C: values A and B, bars from measurements_adv121/fig3C_bars.json
    w = jl(M120, 'fig3C.json')
    bars = jl(M121, 'fig3C_bars.json')['series']

    def wv(series, age, key='value_A'):
        for x in w['series'][series]:
            if x['age'] == age and key in x:
                return x[key]
        return None

    def bar(series, age):
        for x in bars[series]:
            if x['age'] == age:
                if x.get('status') == 'bar protrudes':
                    return x['sd_units_A'], 'value'
                if x.get('status') == 'hidden within marker':
                    return x['sd_ceiling_units_A'], 'ceiling'
                return None, 'unresolved'
        return None, 'unresolved'

    for age in (5, 10, 15):
        WT, KO, LD, HD = (wv(s, age) for s in ('WT', 'KO', 'LD', 'HD'))
        WTb, KOb, LDb, HDb = (wv(s, age, 'value_B') for s in ('WT', 'KO', 'LD', 'HD'))
        if LD is None and age == 5:
            # LD marker hidden behind HD at P5: candidates 3.16 (upper edge) to 3.55 (lower edge) in fig3C_occluded_LD_P5_P30.json
            occ = jl(M120, 'fig3C_occluded_LD_P5_P30.json')['series']['LD'][0]
            LD, LDb = occ['value_if_lower_edge_visible'], occ['value_if_lower_edge_visible'] - 0.07
        sdL, fL = bar('LD', age)
        sdH, fH = bar('HD', age)
        if sdL is None or sdH is None:
            sd, flag = None, 'LD bar unresolved (marker occluded by HD marker at P5)' if sdL is None else 'HD bar unresolved'
        else:
            sd = pool(sdL, sdH)
            flag = 'value' if (fL == 'value' and fH == 'value') else 'ceiling (<=)'
        if age in (10, 15):
            lvl = KO + BAR_C['weight'] * (WT - KO)
            lvlb = KOb + BAR_C['weight'] * (WTb - KOb)
            add('weight g', 'P%d' % age, 'bar', lvl - LD, sd, flag,
                'LD SD %s (%s), HD SD %s (%s)' % (sdL, fL, sdH, fH), lvlb - LDb, sd)
        add('weight g', 'P%d' % age, 'HD', HD - LD, sd, flag,
            'LD SD %s (%s), HD SD %s (%s)' % (sdL, fL, sdH, fH), HDb - LDb, sd)

    # ---- clasping S4A at P18
    c = jl(M120, 'figS4A.json')['series']
    def half(s):
        return max(c[s][0]['upper_end_A'] - c[s][0]['mean_A'], c[s][0]['mean_A'] - c[s][0]['lower_end_A'])
    WTc, KOc, LDc, HDc = (c[s][0]['mean_A'] for s in ('WT', 'KO', 'LD', 'HD'))
    WTcb, KOcb, LDcb, HDcb = (c[s][0]['mean_B'] for s in ('WT', 'KO', 'LD', 'HD'))
    sdc = pool(half('LD'), half('HD'))
    lvl = KOc - BAR_C['clasp'] * (KOc - WTc)
    lvlb = KOcb - BAR_C['clasp'] * (KOcb - WTcb)
    note = 'whisker half-lengths LD %.2f (larger of upper %.2f and lower %.2f), HD %.2f; n and scale not printed' % (
        half('LD'), c['LD'][0]['upper_end_A'] - LDc, LDc - c['LD'][0]['lower_end_A'], half('HD'))
    add('clasping score', 'P18', 'bar', LDc - lvl, sdc, 'value', note, LDcb - lvlb, sdc)
    add('clasping score', 'P18', 'HD', LDc - HDc, sdc, 'value', note, LDcb - HDcb, sdc)

    # ---- glucose mg/dL, Fig 3E (P10), 3F (P20), 3G (P30); dots counted
    glu_df = {}
    for fig, age in (('fig3E', 10), ('fig3F', 20), ('fig3G', 30)):
        g = jl(M120, fig + '.json')
        G = g['groups']
        WT, LD, HD = G['WT']['dot_mean_A'], G['LD']['dot_mean_A'], G['HD']['dot_mean_A']
        sdl, sdh = G['LD']['dot_sd_A'], G['HD']['dot_sd_A']
        nl, nh = G['LD']['dots_cores'], G['HD']['dots_cores']
        glu_df[age] = (nl - 1) + (nh - 1)
        sd = pool(sdl, sdh)
        note = 'dots LD %d (SD %.2f), HD %d (SD %.2f); df of the benchmark SD %d, own factor %.2f' % (
            nl, sdl, nh, sdh, glu_df[age], sd_upper_factor(glu_df[age]))
        # calibration B: scale ratio from label centres against tick marks (offset cancels in differences)
        tk, lc = g['y_ticks_px_found'], g['y_label_centres_px']
        ratio = 1.0
        if len(tk) == len(lc) and len(tk) > 1:
            ratio = ((lc[-1] - lc[0]) / (tk[-1] - tk[0]))
        if age == 20:
            add('glucose mg/dL', 'P20', 'bar', GLU_P20_BAR * WT - LD, sd, 'value', note, (GLU_P20_BAR * WT - LD) * ratio, sd * ratio)
        add('glucose mg/dL', 'P%d' % age, 'HD', HD - LD, sd, 'value',
            note + ('; no bar in gap units at this age' if age != 20 else ''), (HD - LD) * ratio, sd * ratio)

    # ---- glia percent area, S7F (Iba1) and S7H (GFAP); caps are SD
    for fig, nm in (('figS7F', 'Iba1 percent area'), ('figS7H', 'GFAP percent area')):
        b = jl(M120, fig + '.json')['bars_left_to_right']
        WT, LD, HD = b[0]['value_A'], b[1]['value_A'], b[2]['value_A']
        WTb, LDb, HDb = b[0]['value_B'], b[1]['value_B'], b[2]['value_B']
        sdl, sdh = b[1]['cap_minus_top_A'], b[2]['cap_minus_top_A']
        sd = pool(sdl, sdh)
        note = 'cap minus top LD %.2f, HD %.2f; n and age not printed; unit of analysis (animal or section) not stated' % (sdl, sdh)
        add(nm, 'age not printed', 'bar', LD - GLIA_BAR * WT, sd, 'value', note, LDb - GLIA_BAR * WTb, sd)
        add(nm, 'age not printed', 'HD', LD - HD, sd, 'value', note, LDb - HDb, sd)

    # ---- spike-wave per hour: per-animal values of the SWD note (panel 7E); no LD arm
    KO = [0.33, 0.61, 0.69, 0.73, 0.80]
    HDv = [0.00, 0.09, 0.11, 0.18, 0.25]
    WTm = 0.03
    def sd_of(v):
        m = sum(v) / len(v)
        return math.sqrt(sum((x - m) ** 2 for x in v) / (len(v) - 1))
    mk, mh = sum(KO) / 5, sum(HDv) / 5
    lvl = mk - BAR_C['swd'] * (mk - WTm)
    sd = pool(sd_of(KO), sd_of(HDv))
    note = 'KO SD %.3f, HD SD %.3f (5 pups each); no LD arm: contrast is candidate against the knockout vehicle arm, not partial against broad' % (sd_of(KO), sd_of(HDv))
    add('spike-wave per hour', 'P14 to P21 pooled', 'vehicle (bar level)', mk - lvl, sd, 'value', note)
    add('spike-wave per hour', 'P14 to P21 pooled', 'vehicle (as HD)', mk - mh, sd, 'value', note)

    # S7B/S7D glia knockout baseline (measured under the pre-registered rule of section 4): WT-ratio units, cross-experiment
    p = os.path.join(M121, 'figS7B_D.json')
    extra = jl(M121, 'figS7B_D.json') if os.path.exists(p) else None
    closures = []
    if extra:
        for fig, key, nm in (('figS7F', 'S7B_Iba1', 'Iba1'), ('figS7H', 'S7D_GFAP', 'GFAP')):
            b = jl(M120, fig + '.json')['bars_left_to_right']
            wtF, ldF, hdF = b[0]['value_A'], b[1]['value_A'], b[2]['value_A']
            sdHDr = b[2]['cap_minus_top_A'] / wtF
            ldr, hdr = ldF / wtF, hdF / wtF
            bw, bk = extra[key]['bars'][0], extra[key]['bars'][1]
            wtB, koB = bw['value_A'], bk['value_A']
            kor = koB / wtB
            sdKOr = bk['cap_minus_top_A'] / wtB
            sdp = pool(sdKOr, sdHDr)
            note = ('S7B/S7D (P20, n not printed) KO/WT %.2f (SD %.2f of WT); S7F/H arms in their own WT units (LD %.2f, HD %.2f); '
                    'different experiments and WT baselines (%s WT %.2f in S7B/D against %.2f in S7F/H), indicative only') % (
                    kor, sdKOr, ldr, hdr, nm, wtB, wtF)
            add(nm + ' (WT-ratio)', 'KO at P20; arms age not printed', 'vehicle (bar level)', kor - GLIA_BAR, sdp, 'value', note)
            add(nm + ' (WT-ratio)', 'KO at P20; arms age not printed', 'vehicle (as HD)', kor - hdr, sdp, 'value', note)
            closures.append((nm, kor, (kor - ldr) / (kor - 1), (kor - hdr) / (kor - 1), 'KO/WT in S7B/D vs arm/WT in S7F/H'))

    cols = ['family', 'age', 'delta_kind', 'delta', 'sd_pool', 'sd_flag', 'd', 'n_obs_a0125', 'n_ub_a0125', 'n_obs_a05', 'n_ub_a05',
            'cls_obs_holm', 'cls_ub_holm', 'pixel_rel_change', 'note']
    def fmt(v):
        if v is None:
            return 'NA'
        if isinstance(v, float):
            return '%.2f' % v if abs(v) >= 0.1 else '%.3f' % v
        return str(v)
    lines = ['\t'.join(cols)]
    for r in rows:
        lines.append('\t'.join(fmt(r.get(k)) for k in cols))
    out = '\n'.join(lines)
    print('# factor of the SD upper bound at 5 df (one-sided 95 percent): %.3f; z_power %.4f; Holm alpha %.4f' % (F5, Z_POWER, 0.0125))
    print('# check of the method against v3.1 6.8: n(delta 0.4475, SD 0.32): %.1f uncorrected, %.1f Holm-4, upper bound %.1f and %.1f' % (
        n_per_arm(0.4475, 0.32, 0.05), n_per_arm(0.4475, 0.32, 0.0125), n_per_arm(0.4475, 0.32 * F5, 0.05), n_per_arm(0.4475, 0.32 * F5, 0.0125)))
    print(out)
    # reading ages
    print('\n# reading-age ranking by d = |HD - LD| / SD_pool (observed means; ceilings make d a floor)')
    for fam in ('weight g', 'glucose mg/dL'):
        rr = [r for r in rows if r['family'] == fam and r['delta_kind'] == 'HD']
        for r in sorted(rr, key=lambda r: -(r['d'] if r['d'] is not None else -1)):
            print('%s %s d=%s (%s)' % (fam, r['age'], fmt(r['d']), r['sd_flag']))
    if tsv:
        open(os.path.join(HERE, 'OUTPUT_power_table.tsv'), 'w').write(out + '\n')
    for nm, kor, cl, ch, why in closures:
        print('\n# glia closure in WT-ratio units (%s): %s KO/WT %.2f; LD closes %.2f, HD closes %.2f' % (why, nm, kor, cl, ch))


if __name__ == '__main__':
    main()

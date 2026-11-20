"""ADV-120 sitting 2: every number of the card, derived from the saved measurement files (measurements/*.json).

Reads only the JSON written by measure_fig3B.py, measure_xy_panel.py, measure_dots.py, measure_bars.py and
measure_errorbar_points.py. Gap closed = (arm - untreated knockout) / (wild type - untreated knockout).
The only typed numbers are the three SWD means from the earlier note (marked) and the printed n of Fig 3B.
Usage: compute_card_numbers.py [measurements_dir]
"""
import json, os, sys
import numpy as np

D = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'measurements')
J = lambda n: json.load(open(os.path.join(D, n)))
closure = lambda arm, ko, wt: (arm - ko) / (wt - ko)
P = lambda *a: print(*a)

# ---------------- R1 survival, Fig 3B ----------------
b = J('fig3B.json')
sq = {k: v['pass2_squares'] for k, v in b['series'].items()}
prof = b['pass3_profile_at_ages']
P('== R1 survival (Fig 3B; two calibrations: y labels A, axis row B; passes: squares, segments, profile)')
spread = max(abs(s['pct_A'] - s['pct_B']) for k in sq for s in sq[k])
P('max calibration A vs B difference over all squares (percentage points): %.2f' % spread)
def level(name, t):
    last = [s for s in sq[name] if s['day'] <= t]
    return min(100.0, max(0.0, last[-1]['pct_A'])) if last else 100.0
for name, n_leg in (('KO', 10), ('LD', 20), ('WT', 20), ('HD', 30)):
    ev = sq[name]
    P('%s legend n=%d: squares (day, %%) %s' % (name, n_leg, [(s['day'], round(s['pct_A'], 1)) for s in ev]))
# first steps (percentage points) -> implied number at risk at the first event
first = {'KO': 100 - sq['KO'][0]['pct_A'], 'LD': 100 - sq['LD'][0]['pct_A'], 'WT': 100 - sq['WT'][0]['pct_A']}
hd_levels = sorted({round(x['pct_A'], 1) for k in ('pass3_profile_at_ages',) for a, f in prof['HD'].items() for x in f if 60 <= int(a) <= 90})
first['HD'] = 100 - max(l for l in hd_levels if l < 97)
for k, v in first.items():
    P('%s first step %.1f points -> implied at-risk count %.1f' % (k, v, 100.0 / v))
P('HD profile levels seen at ages 60..90 d: %s (steps %s)' % (hd_levels, [round(100 - hd_levels[-1], 1)]))
P('first event days: KO %.1f, LD %.1f, WT %.1f; HD between the 45 d profile (no visible HD line: hidden behind the WT line at 100) and the 60 d profile (%.1f)'
  % (sq['KO'][0]['day'], sq['LD'][0]['day'], sq['WT'][0]['day'], [x['pct_A'] for x in prof['HD']['60']][0]))
def median_day(name):
    below = [s for s in sq[name] if s['pct_A'] <= 50.5]
    return below[0]['day'] if below else None
P('median (first square at or below 50%%): KO %.1f d, LD %.1f d; WT and HD never reach 50%%' % (median_day('KO'), median_day('LD')))
P('last event: KO %.1f d, LD %.1f d (percent at zero)' % (sq['KO'][-1]['day'], sq['LD'][-1]['day']))
def hd_level(t):
    f = prof['HD'].get(str(t), [])
    v = [x['pct_A'] for x in f if x['pct_A'] < 97]   # runs at 97 or more are the halves of a mark sitting at 100
    return v[0] if v else 100.0
P('survival %  at age (WT | LD | HD ; KO=0 after 17 d); WT is the reference, and HD = hidden-at-100 means 100 by continuity')
for t in (20, 30, 45, 60, 75, 90, 100, 150, 295):
    wt = level('WT', t) if t not in prof['WT'] else level('WT', t)
    ld = level('LD', t)
    hd = hd_level(t) if str(t) in prof['HD'] else None
    row = 'age %3d: WT %.1f LD %.1f HD %s' % (t, wt, ld, ('%.1f' % hd) if hd is not None else 'n/a')
    if hd is not None:
        row += ' | closed: LD %.2f HD %.2f' % (closure(ld, 0.0, wt), closure(hd, 0.0, wt))
    P(row)
wt_end = level('WT', 300)
P('WT final plateau %.1f%% (a wild type that is not 100%%); HD final %.1f%%; HD/WT at 300 d %.2f' % (wt_end, level('HD', 300) if sq['HD'] else 0, hd_level(295) / wt_end))

# ---------------- R2 weight, Fig 3C ----------------
c = J('fig3C.json')['series']; co = J('fig3C_occluded_LD_P5_P30.json')['series']
val = lambda s, age: next((r['value_A'] for r in c[s] if r['age'] == age and 'value_A' in r), None)
P('\n== R2 weight (g), Fig 3C; calibrations A ticks, B labels (difference %.2f g)' % max(abs(r['value_A'] - r['value_B']) for s in c for r in c[s] if 'value_A' in r))
ld5 = [r for r in co['LD'] if r['age'] == 5.0][0]; ld30 = [r for r in co['LD'] if r['age'] == 30.0][0]
P('LD at P5 occluded by the HD marker: candidates %.2f (upper edge) to %.2f (lower edge); LD at P30 occluded: %.2f to %.2f' %
  (ld5['value_if_upper_edge_visible'], ld5['value_if_lower_edge_visible'], ld30['value_if_upper_edge_visible'], ld30['value_if_lower_edge_visible']))
for age in (5, 10, 15, 20, 25, 30):
    row = {s: val(s, float(age)) for s in ('WT', 'KO', 'LD', 'HD')}
    if age == 5: row['LD'] = ld5['value_if_lower_edge_visible']
    if age == 30: row['LD'] = ld30['value_if_lower_edge_visible']
    txt = 'P%-2d WT %s KO %s LD %s HD %s' % (age, row['WT'], row['KO'], row['LD'], row['HD'])
    if row['KO'] is not None:
        txt += ' | closed: LD %.2f HD %.2f' % (closure(row['LD'], row['KO'], row['WT']), closure(row['HD'], row['KO'], row['WT']))
    else:
        txt += ' | no untreated KO after P15; HD/WT %.2f LD/WT %.2f' % (row['HD'] / row['WT'], row['LD'] / row['WT'])
    P(txt)
d = J('fig3D.json')['series']
P('Fig 3D (to P180): WT readable %s; the KO, LD and HD marker cores are not separable from the WT markers except LD at P30 (%.2f g)' %
  ([(r['age'], r['value_A']) for r in d['WT'] if 'value_A' in r], d['LD'][0]['value_A']))
P('Fig 3D WT at the marker nearest P30 (window +/- 2.3 d at 4.3 px/d) = %.2f g against Fig 3C WT at P30 = %.2f g; 3C slope near P30 is %.2f g/day, so a few days of offset would account for it: not claimed as a discrepancy' % (d['WT'][0]['value_A'], val('WT', 30.0), (val('WT', 30.0) - val('WT', 25.0)) / 5))

# ---------------- R3 glucose, Fig 3E-3H ----------------
P('\n== R3 glucose (mg/dL), dots per group, mean of the dots, SD of the dots (calibrations A, B listed in the JSON)')
rng = np.random.default_rng(0)
def gl(name):
    g = J(name)['groups']
    return {k: {'n': v['dots_cores'], 'n_area': v['dots_estimated_n_by_area'], 'mean': v['dot_mean_A'], 'sd': v['dot_sd_A']} for k, v in g.items() if v.get('dot_mean_A') is not None}
for pan, nm in (('P10', 'fig3E.json'), ('P20', 'fig3F.json'), ('P30', 'fig3G.json')):
    g = gl(nm)
    P(pan, {k: (v['n'], v['mean'], v['sd']) for k, v in g.items()})
g10 = gl('fig3E.json')
w, k_, l_, h_ = g10['WT'], g10['KO'], g10['LD'], g10['HD']
P('P10 gap closed: LD %.2f HD %.2f' % (closure(l_['mean'], k_['mean'], w['mean']), closure(h_['mean'], k_['mean'], w['mean'])))
def mc(arm):
    xs = []
    for _ in range(20000):
        m = {n: rng.normal(v['mean'], v['sd'] / np.sqrt(v['n'])) for n, v in (('W', w), ('K', k_), ('A', arm))}
        xs.append((m['A'] - m['K']) / (m['W'] - m['K']))
    return np.percentile(xs, [5, 50, 95])
P('P10 closure 5-50-95 percentile from the group SEMs (dots, Monte Carlo): LD %s HD %s' % (np.round(mc(l_), 2), np.round(mc(h_), 2)))
g20 = gl('fig3F.json')
P('P20: no untreated KO in the panel; LD - WT = %.1f, HD - WT = %.1f mg/dL; LD/WT %.2f HD/WT %.2f' %
  (g20['LD']['mean'] - g20['WT']['mean'], g20['HD']['mean'] - g20['WT']['mean'], g20['LD']['mean'] / g20['WT']['mean'], g20['HD']['mean'] / g20['WT']['mean']))
h = J('fig3H.json')['groups']
P('P180 (bars): WT %.1f, HD %.1f mg/dL, HD/WT %.2f; n not printed' % (h['WT']['bar_value_A'], h['HD']['bar_value_A'], h['HD']['bar_value_A'] / h['WT']['bar_value_A']))

# ---------------- R5 myelination ----------------
P('\n== R5 myelination')
c6 = J('fig6C.json')['bars_left_to_right']; d6 = J('fig6D.json')['bars_left_to_right']; e6 = J('fig6E.json')['bars_left_to_right']
P('Fig 6C brain weight mg: WT %.0f KO %.0f (KO/WT %.2f); Fig 6D CC thickness (unit not printed on the axis): WT %.0f KO %.0f (KO/WT %.2f)' %
  (c6[0]['value_A'], c6[1]['value_A'], c6[1]['value_A'] / c6[0]['value_A'], d6[0]['value_A'], d6[1]['value_A'], d6[1]['value_A'] / d6[0]['value_A']))
printed = {'cc': 48, 'cortex': 30, 'striatum': 50, 'AC': 70}
for i, reg in enumerate(printed):
    wv, kv = e6[2 * i]['value_A'], e6[2 * i + 1]['value_A']
    P('Fig 6E %-8s WT %.1f KO %.1f: KO/WT %.0f%%, reduction %.0f%%; printed %d%%' % (reg, wv, kv, 100 * kv / wv, 100 * (1 - kv / wv), printed[reg]))
P('(Fig 6E calibration B, by label centres, is invalid for this panel: the labels merged with annotations; A only)')
m17 = J('repudi2021_fig5_myelinated_P17.json')['bars_left_to_right']; um = J('repudi2021_fig5_unmyelinated_6mo.json')['bars_left_to_right']
wt17, ko17, aav17 = m17[0], m17[1], m17[2]
P('2021 Fig 5 CC myelinated axons per FOV at P17 (n=3 each): WT %.1f KO %.1f KO+AAV %.1f (B: %.1f %.1f %.1f); gap closed %.2f' %
  (wt17['value_A'], ko17['value_A'], aav17['value_A'], wt17['value_B'], ko17['value_B'], aav17['value_B'], closure(aav17['value_A'], ko17['value_A'], wt17['value_A'])))
P('2021 Fig 5 CC unmyelinated axons per FOV at 6 months (n=3 each): WT %.1f KO+AAV %.1f (B: %.1f %.1f); treated/WT %.2f' %
  (um[0]['value_A'], um[1]['value_A'], um[0]['value_B'], um[1]['value_B'], um[1]['value_A'] / um[0]['value_A']))

# ---------------- R4 glia ----------------
P('\n== R4 glia (percent area, treated-arm panels; no untreated KO in these panels)')
f7 = J('figS7F.json')['bars_left_to_right']; h7 = J('figS7H.json')['bars_left_to_right']
P('S7F Iba1: WT %.2f LD %.2f HD %.2f (LD/WT %.2f HD/WT %.2f)' % (f7[0]['value_A'], f7[1]['value_A'], f7[2]['value_A'], f7[1]['value_A'] / f7[0]['value_A'], f7[2]['value_A'] / f7[0]['value_A']))
P('S7H GFAP: WT %.2f LD %.2f HD %.2f (LD/WT %.2f HD/WT %.2f)' % (h7[0]['value_A'], h7[1]['value_A'], h7[2]['value_A'], h7[1]['value_A'] / h7[0]['value_A'], h7[2]['value_A'] / h7[0]['value_A']))

# ---------------- R6 motor ----------------
P('\n== R6 hindlimb clasping score (S4A, P18; scale 0 to 5 as drawn; n not printed)')
s4 = J('figS4A.json')['series']
m = {k: v[0]['mean_A'] for k, v in s4.items()}
mb = {k: v[0]['mean_B'] for k, v in s4.items()}
P('WT %.2f KO %.2f LD %.2f HD %.2f (B: %s); gap closed LD %.2f HD %.2f; SD from the lower whisker: LD %.2f HD %.2f KO %.2f WT %.2f' %
  (m['WT'], m['KO'], m['LD'], m['HD'], [mb[k] for k in ('WT', 'KO', 'LD', 'HD')], closure(m['LD'], m['KO'], m['WT']), closure(m['HD'], m['KO'], m['WT']),
   s4['LD'][0]['half_range_A'] if False else m['LD'] - s4['LD'][0]['lower_end_A'], m['HD'] - s4['HD'][0]['lower_end_A'], m['KO'] - s4['KO'][0]['lower_end_A'], m['WT'] - s4['WT'][0]['lower_end_A']))

# ---------------- R7 spike-wave (typed from SWD_READOUT_FIG7_OBEID2026_SCI_20261120.md) ----------------
ko, wt, hd = 0.63, 0.03, 0.13   # per hour, means of the per-animal values in that note (typed, not re-measured)
P('\n== R7 spike-wave per hour (typed from the earlier note): KO %.2f WT %.2f KO+HD %.2f; gap closed HD %.2f' % (ko, wt, hd, closure(hd, ko, wt)))

# ---------------- sampling spread (what the bar rule's "measured spread" means beyond the pixel calibration) ----------------
P('\n== sampling spread')
def binom_se(p, n):
    return float(np.sqrt(p * (1 - p) / n))
wt90 = level('WT', 90) / 100.0
for lbl, p, n in (('HD at 90 d', hd_level(90) / 100, first['HD'] and 100.0 / first['HD']), ('LD at 60 d', level('LD', 60) / 100, 100.0 / first['LD'])):
    P('%s: fraction alive %.2f, implied at-risk n %.0f, binomial SE %.2f points of fraction, SE of the gap closed (divided by WT %.2f) %.2f' % (lbl, p, n, binom_se(p, n), wt90, binom_se(p, n) / wt90))
P('(the legend n would give a smaller SE: HD n=30 -> %.2f; LD n=20 -> %.2f; reported as the lower bound of spread)' % (binom_se(hd_level(90) / 100, 30), binom_se(level('LD', 60) / 100, 20)))
P('SWD (per-animal ranges typed from the earlier note): KO+HD 0.00 to 0.25 per hour against KO mean 0.63, WT mean 0.03 -> closure %.2f to %.2f' % (closure(0.25, 0.63, 0.03), closure(0.0, 0.63, 0.03)))
for nm, arm_sd, arm_mean in (('clasp HD', s4['HD'][0]['mean_A'] - s4['HD'][0]['lower_end_A'], s4['HD'][0]['mean_A']), ('clasp LD', s4['LD'][0]['mean_A'] - s4['LD'][0]['lower_end_A'], s4['LD'][0]['mean_A'])):
    P('%s: one SD of the arm changes the closure by %.2f (n not printed, so the SE is not computed)' % (nm, arm_sd / (m['KO'] - m['WT'])))

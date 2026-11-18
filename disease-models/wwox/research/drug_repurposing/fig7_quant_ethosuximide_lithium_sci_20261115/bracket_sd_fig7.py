"""ADV-061: bracket of the SD of the per-animal summary S for Cheng 2020 Fig. 7b and 7d from means and upward SEM bars.
S = mean stage over minutes 1 to 60. Per-bin SD = SEM x sqrt(N) (N from the figure legends, assumed constant over the hour:
the legends give one N per arm and the figure does not say whether animals that die keep stage 6 or leave the mean).
Bounds: minutes independent (lower) and minutes fully correlated within animal (upper); intermediate rho shown.
Inputs are the held extraction outputs of fig7_quant_ethosuximide_lithium_sci_20261115 (read only). Offline."""
import csv, math, sys
OUT = sys.argv[1]            # directory with the extraction outputs
N = {('7b','+/+','PTZ'):20, ('7b','+/+','PTZ+ETS'):16, ('7b','+/-','PTZ'):18, ('7b','+/-','PTZ+ETS'):12,
     ('7b','-/-','PTZ'):6, ('7b','-/-','PTZ+ETS'):6,
     ('7d','+/+','PTZ'):12, ('7d','+/+','PTZ+LiCl'):8, ('7d','+/-','PTZ'):12, ('7d','+/-','PTZ+LiCl'):12,
     ('7d','-/-','PTZ'):6, ('7d','-/-','PTZ+LiCl'):7}
HID_LO, HID_HI = 0.055, 0.11      # an upward bar shorter than the marker half height is hidden: bounds as in the earlier README
Z = 2.802                          # (1.96 + 0.84), as in the brief's sizing
DELTA = abs(math.log(0.7))
def curves():
    out = {}
    for r in csv.DictReader(open(OUT + '/fig7b_raster_pdf.tsv'), delimiter='\t'):
        if r['arm'] == 'control' or r['minute'] in ('', '0.0'): continue
        key = ('7b', r['genotype'], r['arm'])
        mm = r['mean_stage_lattice'] or r['mean_stage_raw']
        if mm == '': continue   # no usable body for that minute (marker hidden): the minute is omitted
        m = float(mm); s = r['sem_up_stage']
        hidden = r['flag'] in ('short_run', 'no_body')
        out.setdefault(key, []).append((int(float(r['minute'])), m, (float(s) if s not in ('',) else 0.0), hidden))
    best = {}
    for r in csv.DictReader(open(OUT + '/fig7d_vector_points.tsv'), delimiter='\t'):
        mn = float(r['minute']); k = round(mn)
        if k < 1 or k > 60 or abs(mn - k) > 0.26: continue
        key = ('7d', r['genotype'], r['arm'])
        d = abs(mn - k)
        if (key, k) not in best or d < best[(key, k)][0]:
            best[(key, k)] = (d, float(r['mean_stage']), float(r['bar_up_stage']))
    for (key, k), (d, m, s) in best.items():
        out.setdefault(key, []).append((k, m, s, s < HID_HI))
    return out
def stats(pts, hid):
    pts = sorted(pts); n = N_KEY
    sds = []; ms = []
    for k, m, s, h in pts:
        sem = (HID_HI if hid == 'hi' else HID_LO) if h and s < HID_HI else s
        sds.append(sem * math.sqrt(n)); ms.append(m)
    T = len(pts)
    mean = sum(ms) / T
    sq = math.sqrt(sum(x * x for x in sds)); lin = sum(sds)
    return T, mean, sq / T, lin / T
rows = []
for key, pts in sorted(curves().items()):
    N_KEY = N[key]
    nh = sum(1 for p in pts if p[3] and p[2] < HID_HI)
    for hid in ('lo', 'hi'):
        T, mean, sd_ind, sd_cor = stats(pts, hid)
        for rho in (0.0, 0.3, 0.6, 0.9, 1.0):
            sd = math.sqrt((1 - rho) * sd_ind ** 2 + rho * sd_cor ** 2)
            cv = sd / mean if mean > 0 else float('nan')
            sig = math.sqrt(math.log(1 + cv * cv)) if cv == cv else float('nan')
            n_arm = 2 * (Z * sig / DELTA) ** 2 if sig == sig else float('nan')
            rows.append((key[0], key[1], key[2], N_KEY, T, nh, hid, rho, round(mean, 3), round(sd, 3), round(cv, 2), round(sig, 2), round(n_arm)))
hdr = ('panel', 'genotype', 'arm', 'N', 'bins', 'hidden_bins', 'hidden_rule', 'rho', 'mean_S', 'SD_S', 'CV', 'sigma_log_lognormal', 'n_per_arm_ratio0.7')
with open(sys.argv[2], 'w') as f:
    f.write('\t'.join(hdr) + '\n')
    for r in rows: f.write('\t'.join(str(x) for x in r) + '\n')
print('\t'.join(hdr))
for r in rows:
    if r[6] == 'hi' and r[7] in (0.0, 0.6, 1.0) and r[2] in ('PTZ',):
        print('\t'.join(str(x) for x in r))

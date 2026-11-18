#!/usr/bin/env python3
"""Post-hoc dispersion check on HE's I18 table (an attack, not HE's preregistered test): are the 118 primary PPxY carriers MORE SPREAD in log2 fold change than intensity-matched
non-carriers? A pooled median difference cancels opposite-signed effects and is insensitive to a minority of true targets. Prediction written first: PREDICTION_I18_DISPERSION_BEFORE_RUN.md.
    python3 i18_dispersion_check.py --help
    python3 i18_dispersion_check.py run <parsed_table.tsv> <uniprot_sequences.tsv> <carriers_primary.tsv>
Inputs are HE's files (third-party table kept outside git under files/i18_proteome/; carriers list from HE's results/). Reports Rd (carrier-count-weighted ratio of the median absolute
deviation of log2 fold change, carriers over non-carriers, within intensity deciles) and a one-sided permutation p (3,000 draws, seed 1). Non-carriers: no PP.Y, LP.Y, PP.F or PP.A anywhere."""
import sys
if len(sys.argv) != 5 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv, random, re, statistics as st
fc = {}
for r in csv.DictReader(open(sys.argv[2]), delimiter="\t"):
    try: fc[r["uniprot"]] = (float(r["log2fc"]), (float(r["log2_int_control"]) + float(r["log2_int_silenced"])) / 2)
    except ValueError: pass
seq = {r["Entry"]: r["Sequence"] for r in csv.DictReader(open(sys.argv[3]), delimiter="\t")}
car = [u for u in set(r["uniprot"] for r in csv.DictReader(open(sys.argv[4]), delimiter="\t")) if u in fc]
pat = re.compile(r"(?=(PP.Y|LP.Y|PP.F|PP.A))")
non = [u for u in fc if u in seq and not pat.search(seq[u])]
ints = sorted(v[1] for v in fc.values())
dec = lambda x: min(9, int(10 * sum(1 for y in ints if y < x) / len(ints)))
strata = {}
for u in car + non: strata.setdefault(dec(fc[u][1]), []).append(u)
mad = lambda v: st.median(abs(x - st.median(v)) for x in v)
def Rd(lab):
    num = den = 0
    for us in strata.values():
        c = [fc[u][0] for u in us if lab[u]]; n = [fc[u][0] for u in us if not lab[u]]
        if len(c) < 3 or len(n) < 3 or mad(n) == 0: continue
        num += len(c) * mad(c) / mad(n); den += len(c)
    return num / den
cs = set(car); lab = {u: (u in cs) for u in car + non}; obs = Rd(lab); random.seed(1); ge = 0; N = 3000
for _ in range(N):
    l2 = {}
    for us in strata.values():
        fl = [lab[u] for u in us]; random.shuffle(fl)
        for u, f in zip(us, fl): l2[u] = f
    if Rd(l2) >= obs: ge += 1
print(f"carriers {len(car)}, non-carriers {len(non)}; Rd = {obs:.3f}; one-sided permutation p = {(ge + 1) / (N + 1):.3f}")

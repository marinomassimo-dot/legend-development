#!/usr/bin/env python3
"""ADV-122 chain: adult anchor to a P12-P17 range at the Cheng regimen (arithmetic only).

Usage: python3 -I chain_prior_bound.py FACTORS.tsv OUTDIR
Model (pre-registration section 2): one-compartment, first-order absorption ka, first-order
elimination k.  Adult reference: C0 at t=45 min after 72.3 mg/kg.  Pup relative to adult at the
same mg/kg and time:
    ratio = r_A * r_BP / r_V * shape(k_pup, ka_pup) / shape(k_ad, ka_ad)
    shape(k, ka) = ka (exp(-k t) - exp(-ka t)) / (ka - k)
    k_pup = k_ad * r_CL / r_V          (CL = k V: lower clearance, or larger V, changes k)
    C_pup = C0 * (150/72.3)**lin * ratio
Factors (rows of FACTORS.tsv, columns: factor, label, low, central, high, source, access,
competing, weakening):  t_half_ad (h), ka_ad (1/h), ka_pup (1/h), lin (exponent, 1 = linear),
r_CL, r_V, r_BP, r_A.  low/high are the two ends of the range, not ordered by effect.
"""
import csv, itertools, math, os, sys

# ug/g -> mM at density 1 g/mL: (ug/g * 1000 g/L / 1e6) / (g/mol) * 1000 -> mM = ug/g / MW
MW = 141.17
C0 = {"A_per_g_tissue": 134.9 / MW, "B_per_g_homogenate_1to2": 3 * 134.9 / MW}  # mM
DOSE_RATIO = 150.0 / 72.3
T = 0.75  # h
THRESH = [("0.6 mM (persistent T-current IC50)", 0.6),
          ("2 mM (linear scaling of the anchor, as held)", 2.0),
          ("5 mM (CACNA1I FLIPR, reported above)", 5.0)]
NAMES = ["t_half_ad", "ka_ad", "ka_pup", "lin", "r_CL", "r_V", "r_BP", "r_A"]


def shape(k, ka, t=T):
    if abs(ka - k) < 1e-9:
        return ka * t * math.exp(-k * t)
    return ka * (math.exp(-k * t) - math.exp(-ka * t)) / (ka - k)


def conc(c0, f):
    k_ad = math.log(2) / f["t_half_ad"]
    k_pup = k_ad * f["r_CL"] / f["r_V"]
    ratio = f["r_A"] * f["r_BP"] / f["r_V"] * shape(k_pup, f["ka_pup"]) / shape(k_ad, f["ka_ad"])
    return c0 * DOSE_RATIO ** f["lin"] * ratio


def classify(lo, hi):
    if hi < 0.6:
        return "entirely below 0.6 mM"
    if lo < 0.6 <= hi:
        return "straddles 0.6 mM"
    if hi < 5.0 and lo >= 0.6:
        return "between 0.6 and 5 mM"
    if lo < 5.0 <= hi:
        return "straddles 5 mM"
    return "entirely above 5 mM"


def main(path, outdir):
    rows = list(csv.DictReader(open(path), delimiter="\t"))
    fac = {r["factor"]: r for r in rows}
    miss = [n for n in NAMES if n not in fac]
    if miss:
        sys.exit("missing factors: %s" % miss)
    val = {n: tuple(float(fac[n][c]) for c in ("low", "central", "high")) for n in NAMES}
    os.makedirs(outdir, exist_ok=True)
    out_rows, tor = [], []
    for bname, c0 in C0.items():
        cen = {n: val[n][1] for n in NAMES}
        ccen = conc(c0, cen)
        vals = []
        for combo in itertools.product(*[(val[n][0], val[n][2]) for n in NAMES]):
            vals.append(conc(c0, dict(zip(NAMES, combo))))
        lo, hi = min(vals), max(vals)
        out_rows.append((bname, round(c0, 4), round(lo, 4), round(ccen, 4), round(hi, 4), classify(lo, hi)))
        for n in NAMES:
            a = dict(cen); a[n] = val[n][0]
            b = dict(cen); b[n] = val[n][2]
            ca, cb = conc(c0, a), conc(c0, b)
            tor.append((bname, n, fac[n]["label"], round(ca, 4), round(cb, 4), round(abs(cb - ca), 4)))
    with open(os.path.join(outdir, "OUTPUT_chain.tsv"), "w") as f:
        f.write("branch\tC0_adult_mM\tC_pup_low_mM\tC_pup_central_mM\tC_pup_high_mM\tposition_vs_thresholds\n")
        for r in out_rows:
            f.write("\t".join(map(str, r)) + "\n")
    with open(os.path.join(outdir, "OUTPUT_tornado.txt"), "w") as f:
        for bname in C0:
            f.write("branch %s: one-at-a-time swing of C_pup (mM), others at central, sorted\n" % bname)
            for r in sorted([t for t in tor if t[0] == bname], key=lambda t: -t[5]):
                f.write("  %-10s %-11s low-end %.4f  high-end %.4f  swing %.4f\n" % (r[1], r[2], r[3], r[4], r[5]))
        f.write("thresholds: " + "; ".join("%s = %s" % t for t in THRESH) + "\n")
    print(open(os.path.join(outdir, "OUTPUT_chain.tsv")).read())


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])

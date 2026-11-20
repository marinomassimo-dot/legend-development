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
# Bottom-up route (added after the freeze, recorded in the result): independent of the anchor.
BU_NAMES = ["V_ad", "F_ip"]  # adult apparent volume (L/kg), i.p. bioavailability fraction
DOSE_MMOL = 150.0 / MW  # mmol/kg at the Cheng regimen
DOSE_ANCHOR_MMOL = 72.3 / MW


def shape(k, ka, t=T):
    if abs(ka - k) < 1e-9:
        return ka * t * math.exp(-k * t)
    return ka * (math.exp(-k * t) - math.exp(-ka * t)) / (ka - k)


def conc(c0, f):
    k_ad = math.log(2) / f["t_half_ad"]
    k_pup = k_ad * f["r_CL"] / f["r_V"]
    ratio = f["r_A"] * f["r_BP"] / f["r_V"] * shape(k_pup, f["ka_pup"]) / shape(k_ad, f["ka_ad"])
    return c0 * DOSE_RATIO ** f["lin"] * ratio


def bottom_up(f, v, dose=DOSE_MMOL, pup=True):
    """Total brain conc at 45 min from dose/V only (no anchor): F * dose / V * shape * r_BP."""
    k_ad = math.log(2) / f["t_half_ad"]
    rv = f["r_V"] if pup else 1.0
    rcl = f["r_CL"] if pup else 1.0
    k = k_ad * rcl / rv
    ka = f["ka_pup"] if pup else f["ka_ad"]
    F = min(1.0, v["F_ip"] * (f["r_A"] if pup else 1.0))
    bp = f["r_BP"] if pup else 1.0
    return F * dose / (v["V_ad"] * rv) * shape(k, ka) * bp


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
    miss2 = [n for n in BU_NAMES if n not in fac]
    if miss2:
        sys.exit("missing factors: %s" % miss2)
    val = {n: tuple(float(fac[n][c]) for c in ("low", "central", "high")) for n in NAMES + BU_NAMES}
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
    # bottom-up route and anchor coherence
    allf = NAMES + BU_NAMES
    cen = {n: val[n][1] for n in allf}
    lines = []
    bu_vals = [bottom_up(dict(zip(allf, c)), dict(zip(allf, c)))
               for c in itertools.product(*[(val[n][0], val[n][2]) for n in allf])]
    bu_c = bottom_up(cen, cen)
    ad_c72 = bottom_up(cen, cen, DOSE_ANCHOR_MMOL, pup=False)
    ad_c150 = bottom_up(cen, cen, DOSE_MMOL, pup=False)
    ceil_ad72 = DOSE_ANCHOR_MMOL / val["V_ad"][2]  # no elimination, F=1, largest V -> lowest ceiling
    ceil_ad72_hi = DOSE_ANCHOR_MMOL / val["V_ad"][0]
    lines.append("bottom-up pup at the Cheng regimen (mM, total brain, no anchor used): low %.3f central %.3f high %.3f; position: %s" % (min(bu_vals), bu_c, max(bu_vals), classify(min(bu_vals), max(bu_vals))))
    lines.append("bottom-up adult at 72.3 mg/kg, central: %.3f mM; at 150 mg/kg central: %.3f mM" % (ad_c72, ad_c150))
    for bname, c0 in C0.items():
        lines.append("anchor %s = %.3f mM; measured over bottom-up adult central = %.2f" % (bname, c0, c0 / ad_c72))
    lines.append("no-elimination ceiling at the anchor dose: F=1, dose/V = %.3f mM (V %.2f L/kg) to %.3f mM (V %.2f L/kg); a brain-to-plasma ratio of 1 assumed" % (ceil_ad72, val["V_ad"][2], ceil_ad72_hi, val["V_ad"][0]))
    for bname, c0 in C0.items():
        lines.append("anchor %s needs brain-to-plasma ratio at least %.2f at V=%.2f L/kg, F=1, zero elimination" % (bname, c0 / ceil_ad72_hi, val["V_ad"][0]))
    with open(os.path.join(outdir, "OUTPUT_bottom_up.txt"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print(open(os.path.join(outdir, "OUTPUT_chain.tsv")).read())
    print("\n".join(lines))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])

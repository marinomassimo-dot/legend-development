"""ADV-122 verification (part A of the night mandate): what does dose over volume bound? EXPLORATORY, after the freeze.

One-compartment model with first-order absorption ka and elimination k (same shape as chain_prior_bound.py):
    C_p(t) = F * D * ka / (V * (ka - k)) * (exp(-k t) - exp(-ka t))          [mM = mmol/L]
    C_brain,total(t) = Kp * C_p(t)                                            [Kp = total brain / total plasma, dimensionless]
    D = dose_mg_per_kg / 141.17                                               [mmol/kg]; V in L/kg; 1 ug/g of tissue = 1 mg/kg tissue = 1/141.17 mM at 1.00 g/mL
Question: which Kp does each measured or scaled brain value REQUIRE, given settings of V, t_half, F? The corner of the
settings that gives the lowest required Kp is the zero-elimination, F = 1, smallest-V corner (dose / V). Nothing here is a probability.
Usage: python3 -I coherence_check_partA.py OUTFILE
"""
import itertools, math, sys

MW = 141.17
T = 0.75  # h, 45 min
KA = 6.0  # per h (serum-brain equilibration within 10 min bounds it from below)


def shape(k, ka=KA, t=T):
    if abs(ka - k) < 1e-9:
        return ka * t * math.exp(-k * t)
    return ka * (math.exp(-k * t) - math.exp(-ka * t)) / (ka - k)


def kp_required(c_mM, dose_mg, V, t_half, F):
    k = 0.0 if t_half is None else math.log(2) / t_half
    cp = F * (dose_mg / MW) / V * shape(k)
    return c_mM / cp


def main(out):
    L = []
    anchors = [("anchor A (printed ug/g read as per g tissue): 134.9 ug/g -> %.3f mM" % (134.9 / MW), 134.9 / MW, 72.3),
               ("anchor B (printed ug/g read as per g of 1:2 homogenate, x3): %.3f mM" % (3 * 134.9 / MW), 3 * 134.9 / MW, 72.3),
               ("scaled to 150 mg/kg, branch A (x2.0747): %.3f mM" % (134.9 / MW * 150 / 72.3), 134.9 / MW * 150 / 72.3, 150.0),
               ("scaled to 150 mg/kg, branch B: %.3f mM" % (3 * 134.9 / MW * 150 / 72.3), 3 * 134.9 / MW * 150 / 72.3, 150.0),
               ("the unsourced 'band' lower end 2 mM at 150 mg/kg", 2.0, 150.0),
               ("the unsourced 'band' 4 mM at 150 mg/kg", 4.0, 150.0),
               ("the unsourced 'band' upper end 6 mM at 150 mg/kg", 6.0, 150.0)]
    Vs = [0.40, 0.45, 0.55, 0.65, 0.75]
    ths = [("none", None), ("4 h", 4.0), ("2 h", 2.0), ("1 h", 1.0)]
    Fs = [1.0, 0.9]
    L.append("Required Kp (total brain / total plasma) so that the model reproduces the value at 45 min; F = 1 and 0.9; ka = %.0f per h" % KA)
    L.append("Reference Kp for an unbound, passively distributed small polar drug = brain water fraction / plasma water fraction = about 0.79/0.93 = %.2f (inputs: brain water 76.6 to 85.6 percent in rat by age, producer D; plasma water 0.93 is a textbook assumption, not sourced here); rat steady-state ethosuximide brain/plasma 0.90 to 0.94 (abstract, PMID 590227); early rat cortex 2.04 at 5 min falling to 0.14 at 2 h (abstract, PMID 2047576)." % (0.79 / 0.93))
    for name, c, dose in anchors:
        L.append("")
        L.append(name + "  (dose %.1f mg/kg = %.3f mmol/kg)" % (dose, dose / MW))
        L.append("  V (L/kg)   " + "   ".join("t1/2 %-4s" % n for n, _ in ths))
        for F in Fs:
            L.append("  F = %.1f" % F)
            for V in Vs:
                L.append("   %.2f      " % V + "   ".join("%8.2f" % kp_required(c, dose, V, th, F) for _, th in ths))
    # corner summary
    L.append("")
    L.append("Lowest required Kp (V = 0.40, F = 1, no elimination) and at the labelled central settings (V = 0.65, F = 0.9, t1/2 = 1 h):")
    for name, c, dose in anchors:
        lo = kp_required(c, dose, 0.40, None, 1.0)
        lo55 = kp_required(c, dose, 0.55, None, 1.0)
        cen = kp_required(c, dose, 0.65, 1.0, 0.9)
        L.append("  %-78s best corner %.2f (V 0.55: %.2f)   central %.2f" % (name[:78], lo, lo55, cen))
    # settings that make anchor A coherent with Kp = 0.85 and Kp = 1.0
    L.append("")
    L.append("Settings (V, t1/2, F; ka = 6 per h) for which anchor A needs Kp <= 1.0 / <= 0.85 (grid):")
    for kp_ref in (1.0, 0.85):
        ok = [(V, th, F) for V, (n, th), F in itertools.product([0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.65, 0.75], ths, Fs)
              if kp_required(134.9 / MW, 72.3, V, th, F) <= kp_ref]
        L.append("  Kp <= %.2f: %s" % (kp_ref, "; ".join("V %.2f, t1/2 %s, F %.1f" % (V, "none" if th is None else "%g h" % th, F) for V, th, F in ok) or "none on the grid"))
    open(out, "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main(sys.argv[1])

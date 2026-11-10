"""SCI43: the reversal potential of the conductance that must have changed, implied by a printed (Rin, Vrest) pair.
Single-conductance steady-state arithmetic: G = 1/Rin; V_new = (G_old*V_old + dG*E_x)/G_new with dG = G_new - G_old (negative for a loss).
  E_x = V_old + dV * G_new / (G_new - G_old)
Assumptions (all can fail): one conductance changed, the rest of the cell unchanged, steady state, point means of cells treated as units, no variance carried.
Labelled INFERENZA; computed once by the Orchestrator at S3 (NOT preregistered; the preregistered uncertainty analysis is S7). After verification the arithmetic is a CONSTRAINT on explanations, not a discriminator between a K+ loss and a smaller cell plus a shunt.
  python3 implied_reversal.py -> output/implied_reversal_points.tsv"""
import csv
from pathlib import Path
HERE = Path(__file__).resolve().parent
# case, source, Rin_old, Rin_new (MOhm), V_old, V_new (mV, recorded scale as printed), kind of change, note
CASES = [
 ("Wwox WT->KO (P13-P17 L2/3, 35 C)", "34634460 Table 1", 102.88, 143.03, -79.25, -73.62, "net loss", "tau 18.55 -> 21.25 ms"),
 ("Wwox WT->HT", "34634460 Table 1", 102.88, 143.26, -79.25, -75.51, "net loss", "HT vs KO untested in the paper"),
 ("Fmr1 WT->KO (P28-42 L2/3 auditory, 34 C)", "10.64898/2026.02.03.703439 Fig 1", 172.7, 124.5, -78.3, -82.0, "net gain", "Ba2+-sensitive current larger in KO (measured); K+ gain of known sign"),
 ("Ba2+ 60 uM on WT (same preparation)", "10.64898/2026.02.03.703439 Fig 1", 172.7, 223.8, -78.3, -76.8, "loss by block", "Rin_new derived from printed delta; rest +1.5 mV; measured Ba2+ reversal -89.6 +/- 2.4 mV (voltage clamp)"),
 ("Kcnq2 cKO vs control (P15-20 L2/3, RT)", "28100740 Fig 2", 239.0, 299.0, -67.3, -65.7, "net loss", "rest change not significant (p 0.2); corrected scale; order of the two values to be checked by the verifier"),
 ("Development L3 P7->P14 (prelimbic, 31 C)", "30911152 Table 2", 405.85, 213.42, -61.63, -69.96, "net gain", "tau 40.2 at P14; no tool"),
 ("Development L3 P14->P28", "30911152 Table 2", 213.42, 110.28, -69.96, -73.02, "net gain", ""),
 ("Development L5 P7->P14", "30911152 Table 2", 161.83, 78.33, -61.30, -67.08, "net gain", ""),
 ("Development L5 P14->P28", "30911152 Table 2", 78.33, 52.60, -67.08, -69.62, "net gain", ""),
 ("ZD7288 10 uM on WT (Ih block)", "10.64898/2026.02.03.703439 Fig 5", 130.0, 138.0, -78.3, -83.0, "loss by block", "ILL-CONDITIONED (verifier): baseline Rin read off Fig 5C (about 130, +8 printed); halving the +8 MOhm difference moves E_x from about -2 to about +74 mV; kept only to show that the arithmetic is unstable for a small share; V_old = preprint WT mean; rest -4.7 mV"),
]
OFFSETS = [0, 8, 13, 16]  # recorded = true + delta (candidate junction offsets, mV); E_K true about -97.5 mV for the Wwox solutions
def main():
    rows = []
    for name, src, r0, r1, v0, v1, kind, note in CASES:
        g0, g1 = 1000 / r0, 1000 / r1
        dG, dV = g1 - g0, v1 - v0
        ex = v0 + dV * g1 / dG
        rows.append([name, src, r0, r1, v0, v1, f"{g0:.2f}", f"{g1:.2f}", f"{dG:+.2f}", f"{100*dG/g0:+.0f}", f"{dV:+.2f}", f"{ex:.1f}", kind, note])
    # degenerate reproduction (verifier): a membrane scaled down plus a fixed shunt at 0 mV reproduces the Wwox WT->KO pair exactly,
    # and its implied reversal is the native rest of the membrane, so a K+-like value does not identify a K+ conductance.
    gs = 1.5; g0, g1 = 1000 / 102.88, 1000 / 143.03
    vn = -79.25 * g0 / (g0 - gs); s = (g1 - gs) / (g0 - gs); vko = vn * (g1 - gs) / g1
    rows.append([f"Size plus shunt: membrane scaled to {s:.2f} with a fixed {gs} nS shunt at 0 mV (reproduces Wwox WT->KO)", "verifier construction", 102.88, 143.03, -79.25, round(vko, 2), f"{g0:.2f}", f"{g1:.2f}", f"{g1-g0:+.2f}", f"{100*(g1-g0)/g0:+.0f}", f"{vko+79.25:+.2f}", f"{vn:.1f}", "net loss", "implied reversal = native rest of the scaled membrane: the arithmetic cannot tell this from a K+ conductance loss"])
    with open(HERE / "output/implied_reversal_points.tsv", "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["case", "source", "Rin_old_MOhm", "Rin_new_MOhm", "V_old_mV", "V_new_mV", "G_old_nS", "G_new_nS", "dG_nS", "dG_percent", "dV_mV", "implied_E_x_recorded_scale_mV", "kind", "note"])
        w.writerows(rows)
    for r in rows: print(r[0], "| dG %s nS (%s%%) dV %s -> E_x %s" % (r[8], r[9], r[10], r[11]))
    print("Wwox E_K on the recorded scale if recorded = true + delta, E_K true -97.5:", {d: round(-97.5 + d, 1) for d in OFFSETS})
main()

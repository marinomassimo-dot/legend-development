#!/usr/bin/env python3
"""I4: what the two held adenosine-axis changes do to A1 tone, as arithmetic (a hypothesis generator, not a measurement).

    python3 i4_tone_arithmetic.py [--out FILE]      (deterministic; no randomness, no files read)

Held numbers (hippocampal nuclei pool, one pool per arm, no variance; SCI's and IT's recounts agree): neuron-like Adk 156.8 -> 126.7 CPM (x0.808), Adora1 39.6 -> 19.3 (x0.487), Kcnj3 617 -> 451 (x0.731);
astrocyte-like Adk 609 -> 534 (x0.877), Adora1 42.5 -> 28.3 (x0.666). Bulk (P17 neuron-deletion rows and the P47T line) shows Adora1 inside the 1.5-fold band, so each scenario states which Adora1 value it uses.
Model (ASSUMED, the simplest that has the right sign structure): extracellular adenosine at steady state ~ production / (clearance), clearance ~ Adk_level^s (s from 0.5 to 1.5, saturation and the other
clearance routes make s < 1 plausible); A1 occupancy ~ adenosine * Adora1_level^r (r 0.5 to 1; linear in the low-adenosine range); an effector factor Kcnj3_level^g (g 0 or 1). tone = adenosine * receptor^r * effector^g, relative to wild type.
RNA is used as a proxy for protein level and for capacity: that is a further assumption. Not medical advice.
"""
import argparse, itertools

ADK, ADORA1, KCNJ3 = 126.7 / 156.8, 19.3 / 39.6, 451 / 617
ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter); ap.add_argument("--out"); a = ap.parse_args()
rows = [["scenario", "adk_exponent_s", "receptor_exponent_r", "girk_exponent_g", "adenosine_ratio", "tone_ratio_null_over_wt"]]
for scen, a1, kc in (("snRNA pool values (Adora1 x0.487, Kcnj3 x0.731)", ADORA1, KCNJ3), ("Adora1 and Kcnj3 unchanged (the bulk reading)", 1.0, 1.0), ("only Adk changes (same as above, listed for the sign)", 1.0, 1.0)):
    if scen.startswith("only"): continue
    for s, r, g in itertools.product((0.5, 1.0, 1.5), (0.5, 1.0), (0.0, 1.0)):
        ado = ADK ** (-s); rows.append([scen, f"{s}", f"{r}", f"{g}", f"{ado:.3f}", f"{ado * a1 ** r * kc ** g:.3f}"])
table = "\n".join("\t".join(r) for r in rows) + "\n"
vals = {k: [float(r[-1]) for r in rows[1:] if r[0].startswith(k)] for k in ("snRNA", "Adora1 and Kcnj3")}
text = f"# snRNA scenario: tone ratio from {min(vals['snRNA']):.2f} to {max(vals['snRNA']):.2f} (below 1 in {sum(v < 1 for v in vals['snRNA'])} of {len(vals['snRNA'])} cells)\n"
text += f"# bulk scenario: tone ratio from {min(vals['Adora1 and Kcnj3']):.2f} to {max(vals['Adora1 and Kcnj3']):.2f} (above 1 in every cell: lower Adk alone raises adenosine)\n"
if a.out:
    open(a.out, "w").write(table); open(str(a.out).rsplit(".", 1)[0] + "_summary.txt", "w").write(text)    # comment lines never go inside a TSV
print(table + text)

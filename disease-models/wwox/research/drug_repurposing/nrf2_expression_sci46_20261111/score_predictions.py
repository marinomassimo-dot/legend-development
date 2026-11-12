"""SCI46 queue item: scores the predictions of PREREGISTRATION.md (committed before the run) from nrf2_expression_mouse.tsv and nrf2_expression_human.tsv, by the rules written there, and writes
predictions_scored.tsv and neuron_readability.tsv (genes by mouse neuron and astrocyte class mean against the 1 and 5 FPKM lines). No prediction is changed.
  python3 score_predictions.py"""
import csv, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
if "--help" in sys.argv or "-h" in sys.argv: print(__doc__); sys.exit(0)
M, H = {}, {}
for r in csv.DictReader(open(HERE / "nrf2_expression_mouse.tsv", encoding="utf-8"), delimiter="\t"): M[(r["gene"], r["cell_class"])] = float(r["mean_fpkm"])
for r in csv.DictReader(open(HERE / "nrf2_expression_human.tsv", encoding="utf-8"), delimiter="\t"): H[(r["gene"], r["group"])] = float(r["mean_fpkm"])
N, A, MG, OPC = "neurons (P7)", "astrocytes (P7)", "microglia", "OPC (P17)"
ALL = sorted({c for _, c in M})
m = lambda g, c: M[(g, c)]
f = lambda x: f"{x:.2f}"
rows = []
def add(pid, text, verdict, basis): rows.append([pid, text, verdict, basis])
det = lambda g, cs: all(m(g, c) >= 1 for c in cs)
add("NP1", "Nfe2l2 and Keap1 detected in mouse neurons, astrocytes, microglia and OPC", "HELD" if det("Nfe2l2", [N, A, MG, OPC]) and det("Keap1", [N, A, MG, OPC]) else "FAILED",
    "Nfe2l2 " + "; ".join(f"{c.split(' (')[0]} {f(m('Nfe2l2', c))}" for c in [N, A, MG, OPC]) + " | Keap1 " + "; ".join(f"{c.split(' (')[0]} {f(m('Keap1', c))}" for c in [N, A, MG, OPC]))
r = m("Nqo1", A) / m("Nqo1", N)
add("NP2", "Nqo1 at least twice as high in mouse astrocytes as in neurons", "HELD" if r >= 2 else "FAILED", f"astrocytes {f(m('Nqo1', A))}, neurons {f(m('Nqo1', N))}, ratio {r:.1f}")
top = max(ALL, key=lambda c: m("Hmox1", c))
add("NP3", "Hmox1 highest in mouse microglia among the seven classes", "HELD" if top == MG else "FAILED", f"highest {top} {f(m('Hmox1', top))}; microglia {f(m('Hmox1', MG))}; neurons {f(m('Hmox1', N))}; astrocytes {f(m('Hmox1', A))}")
ok = m("Niacr1", MG) >= 1 and m("Niacr1", N) < 1 and m("Niacr1", A) < 1
add("NP4", "Hcar2 detected in microglia, below 1 FPKM in neurons and astrocytes", "HELD" if ok else "FAILED",
    f"scored on the table symbol Niacr1 (UniProt lists Hcar2 Gpr109a Niacr1 as one mouse protein; Hcar2 is absent from the table under its current symbol: a deviation from the preregistration, stated): microglia {f(m('Niacr1', MG))}, neurons {f(m('Niacr1', N))}, astrocytes {f(m('Niacr1', A))}; human HCAR2 absent from the human table")
ok = m("Nqo1", N) < 5 and m("Nqo1", A) > 20
add("NP5", "Nqo1 below 5 FPKM in mouse neurons and above 20 in astrocytes", "FAILED" if not ok else "HELD",
    f"neurons {f(m('Nqo1', N))} (below 5: yes); astrocytes {f(m('Nqo1', A))} (above 20: no). Nqo1 is at or below about 3 FPKM in every mouse class (maximum {f(max(m('Nqo1', c) for c in ALL))}); in the human table the highest group is endothelium {f(H[('NQO1','endo_ctx')])} and mature cortical astrocytes {f(H[('NQO1','astro_mature_ctx')])}")
rk, rn = max(m("Keap1", N), m("Keap1", A)) / min(m("Keap1", N), m("Keap1", A)), max(m("Nfe2l2", N), m("Nfe2l2", A)) / min(m("Nfe2l2", N), m("Nfe2l2", A))
add("NP6", "Keap1 and Nfe2l2 differ by less than a factor of two between mouse neurons and astrocytes", "FAILED" if (rk >= 2 or rn >= 2) else "HELD",
    f"Keap1 neurons {f(m('Keap1', N))}, astrocytes {f(m('Keap1', A))} (x{rk:.2f}); Nfe2l2 neurons {f(m('Nfe2l2', N))}, astrocytes {f(m('Nfe2l2', A))} (x{rn:.1f}, astrocytes higher); human single neuron sample NFE2L2 {f(H[('NFE2L2','neuron_ctx')])} against mature cortical astrocytes {f(H[('NFE2L2','astro_mature_ctx')])}")
ast = ["astro_fetal_ctx", "astro_hippocampus_epilepsy_region", "astro_mature_ctx", "astro_tumor"]
below = [a for a in ast if H[("NQO1", "neuron_ctx")] < H[("NQO1", a)]]
add("NP7", "Human single neuron sample NQO1 below the astrocyte classes", "FAILED" if len(below) < len(ast) else "HELD",
    f"neuron {f(H[('NQO1','neuron_ctx')])} (one sample); below " + ", ".join(f"{a} {f(H[('NQO1', a)])}" for a in below) + "; not below " + ", ".join(f"{a} {f(H[('NQO1', a)])}" for a in ast if a not in below))
rw = m("Wwox", N) / m("Wwox", A)
add("NP8", "Wwox detected in mouse neurons and astrocytes and higher in neurons than in astrocytes (rule: at least twice)", "PARTLY: detected in both; the ratio is below the preregistered factor of two" if (m("Wwox", N) >= 1 and m("Wwox", A) >= 1 and rw < 2) else ("HELD" if rw >= 2 else "FAILED"),
    f"neurons {f(m('Wwox', N))}, astrocytes {f(m('Wwox', A))}, ratio {rw:.2f}; human single neuron {f(H[('WWOX','neuron_ctx')])} against mature cortical astrocytes {f(H[('WWOX','astro_mature_ctx')])}")
add("NP9", "descriptive: G6pdx and Gclm detected in the four main mouse classes", "HELD (descriptive)" if det("G6pdx", [N, A, MG, OPC]) and det("Gclm", [N, A, MG, OPC]) else "NOT HELD",
    "G6pdx " + "; ".join(f"{c.split(' (')[0]} {f(m('G6pdx', c))}" for c in [N, A, MG, OPC]) + " | Gclm " + "; ".join(f"{c.split(' (')[0]} {f(m('Gclm', c))}" for c in [N, A, MG, OPC]))
with open(HERE / "predictions_scored.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["prediction", "statement", "verdict", "values_fpkm_class_means"]); w.writerows(rows)
genes = sorted({g for g, _ in M})
out = []
for g in genes:
    n, a = m(g, N), m(g, A)
    line = "above 5 in neurons" if n >= 5 else ("1 to 5 in neurons" if n >= 1 else "below 1 in neurons")
    out.append([g, f(n), f(a), f(m(g, MG)), f(m(g, OPC)), f"{(a / n):.2f}" if n else "NA", line])
with open(HERE / "neuron_readability.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["gene", "neurons_P7", "astrocytes_P7", "microglia", "OPC_P17", "astro_over_neuron", "neuron_line"]); w.writerows(out)
for r in rows: print(r[0], "|", r[2])

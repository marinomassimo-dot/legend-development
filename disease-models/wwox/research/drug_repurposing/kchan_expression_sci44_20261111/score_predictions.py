"""SCI44 coda: score the preregistered predictions P1-P6 from kchan_expression_mouse.tsv and kchan_expression_human.tsv (floor 0.1 FPKM for ratios). Writes predictions_scored.tsv.
  python3 score_predictions.py"""
import csv, sys
from pathlib import Path
H = Path(__file__).resolve().parent
if "--help" in sys.argv: print(__doc__); sys.exit(0)
def load(fn, k1, k2):
    d = {}
    for r in csv.DictReader(open(H / fn, encoding="utf-8"), delimiter="\t"): d[(r["gene"].upper(), r[k2])] = float(r["mean_fpkm"])
    return d
M = load("kchan_expression_mouse.tsv", "gene", "cell_class"); Hu = load("kchan_expression_human.tsv", "gene", "group")
mn, ma, me, mm = "neurons (P7)", "astrocytes (P7)", "endothelium", "microglia"
def m(g, c): return M.get((g.upper(), c), 0.0)
def h(g, c): return Hu.get((g.upper(), c), 0.0)
fl = lambda x: max(x, 0.1)
ha = "astro_mature_ctx"; hn = "neuron_ctx"
out = []
def add(pid, text, ok, detail): out.append([pid, text, "held" if ok else "failed", detail])
add("P1a", "Kcnj11 >= 1 FPKM in mouse neurons", m("Kcnj11", mn) >= 1, f"Kcnj11 neuron {m('Kcnj11', mn):.2f}, astro {m('Kcnj11', ma):.2f}")
add("P1b", "Abcc8 >= 1 FPKM in mouse neurons and neuron >= astrocyte", m("Abcc8", mn) >= 1 and m("Abcc8", mn) >= m("Abcc8", ma), f"Abcc8 neuron {m('Abcc8', mn):.2f}, astro {m('Abcc8', ma):.2f}")
add("P2m", "Kcnj10 astro >= 10 x neuron, mouse", fl(m("Kcnj10", ma)) >= 10 * fl(m("Kcnj10", mn)), f"Kcnj10 astro {m('Kcnj10', ma):.2f}, neuron {m('Kcnj10', mn):.2f}")
add("P2h", "KCNJ10 astro >= 10 x neuron, human", fl(h("KCNJ10", ha)) >= 10 * fl(h("KCNJ10", hn)), f"KCNJ10 astro {h('KCNJ10', ha):.2f}, neuron {h('KCNJ10', hn):.2f} (neuron n=1)")
for g in ("Kcnj8", "Abcc9"):
    add("P3_" + g, f"{g} neuron < max(endothelium, astrocyte), mouse", m(g, mn) < max(m(g, me), m(g, ma)), f"{g} neuron {m(g, mn):.2f}, astro {m(g, ma):.2f}, endo {m(g, me):.2f}")
add("P4a_m", "Kcnk1 astro > neuron, mouse", m("Kcnk1", ma) > m("Kcnk1", mn), f"Kcnk1 astro {m('Kcnk1', ma):.2f}, neuron {m('Kcnk1', mn):.2f}")
add("P4a_h", "KCNK1 astro > neuron, human", h("KCNK1", ha) > h("KCNK1", hn), f"KCNK1 astro {h('KCNK1', ha):.2f}, neuron {h('KCNK1', hn):.2f} (neuron n=1)")
for g in ("Kcnk2", "Kcnk3", "Kcnk9"):
    add("P4b_" + g, f"{g} >= 1 FPKM in mouse neurons", m(g, mn) >= 1, f"{g} neuron {m(g, mn):.2f}")
add("P5", "Kcnj2 neuron >= astrocyte, mouse", m("Kcnj2", mn) >= m("Kcnj2", ma), f"Kcnj2 neuron {m('Kcnj2', mn):.2f}, astro {m('Kcnj2', ma):.2f}")
for g in ("Kcnq2", "Kcnq3", "Hcn1"):
    add("P6_" + g, f"{g} neuron >= 3 x astrocyte, mouse", fl(m(g, mn)) >= 3 * fl(m(g, ma)), f"{g} neuron {m(g, mn):.2f}, astro {m(g, ma):.2f}")
with open(H / "predictions_scored.tsv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["prediction", "statement", "result", "values"]); w.writerows(out)
for r in out: print(r[0], r[2], "|", r[3])

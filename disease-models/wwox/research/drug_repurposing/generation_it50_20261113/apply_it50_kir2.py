"""IT50: the Kir-gene cell-class states already computed by cell_context (cell_context_it46.tsv) carried into the INV-18 Ba2+/Kir2 arm (dated clause; idempotent; no new scientific proposition)."""
import csv, sys
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
TXT = ("[IT50 cell class] In the held RNA class tables no Kir2-family subunit gene is neuron-enriched: KCNJ2 is enriched in other classes in both tables (mouse neurons P7 0.74 FPKM against an endothelial class 41.80; the one human neuron sample 1.40 against an oligodendrocyte-class sample 6.64, n=1); "
       "KCNJ4 and KCNJ12 are shared in the mouse table and not detected in the human one; KCNJ14 is in no held table (unknown, not low). The astrocytic Kir gene KCNJ10 is enriched in astrocytes in both tables (mouse 184.76 against 8.12 in neurons; human 126.02 against 9.00). "
       "So a Ba2+- or Kir2-directed effect cannot be assigned to neurons from these tables: the glial (Kir4.1) arm is required for the statement that a Ba2+ share is neuronal, and a native-cell positive control for a Kir2 probe is not identifiable from them (a heterologous control is the default). RNA class means of different ages; not protein, current or subunit composition.")
EV = " [IT50] cell-class RNA states of the Kir genes are held (INV-18 clause): none neuron-enriched; composition still unread."
def main(check=False):
    csv.field_size_limit(10**9); n = 0
    for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"):
        p = DR / f; rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; i, c = h.index("inv_id"), h.index("feasibility")
        for r in rows[1:]:
            if r[i] == "INV-18" and "[IT50 cell class]" not in r[c]: r[c] = (r[c] + " " + TXT).strip(); n += 1
        if not check and n: csv.writer(open(p, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    qm = DR / "batch_sci_20261105/map/open_questions_map.tsv"
    rows = list(csv.reader(open(qm, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; m = 0
    for r in rows[1:]:
        if r[0] in ("IT49-Q07", "IT49-Q09") and "[IT50]" not in r[h.index("status_evidence")]:
            r[h.index("status_evidence")] += EV; m += 1
    if not check and m: csv.writer(open(qm, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    print(("would change " if check else "changed ") + str(n + m))
if __name__ == "__main__":
    main("--check" in sys.argv)

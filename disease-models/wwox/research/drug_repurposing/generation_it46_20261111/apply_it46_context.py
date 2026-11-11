#!/usr/bin/env python3
"""IT46 P1: the cell-context join reaches the two consumers that carried the IT45 sentence "the Kv7 genes are neuron-enriched"
(compound_view V10 next_test; investigations INV-18 feasibility). The correction text is built from cell_context.py rows, not typed.
Idempotent: a row that already holds the marker is left alone.  python3 apply_it46_context.py [--check]"""
import csv, sys
from pathlib import Path
import cell_context as cc

HERE = Path(__file__).resolve().parent; DR = HERE.parent
MARK = "[IT46 cell context]"
TARGETS = [(DR / "generation_it41_20261109/compound_view.tsv", "item_id", "V10", "next_test"),
           (DR / "ranking_it8_p9_20261029/investigations_it20.tsv", "inv_id", "INV-18", "feasibility"),
           (DR / "ranking_it8_p9_20261029/investigations.tsv", "inv_id", "INV-18", "feasibility")]


def clause():
    rel = cc.relations()
    r5 = cc.join(rel["R5"], "R5")
    by = {(r["gene"], r["table"]): r for r in r5}
    q2, q3 = by[("KCNQ2", "mouse")], by[("KCNQ3", "mouse")]
    h2 = by[("KCNQ2", "human")]
    _, cons = cc.context_for(rel["R5"], "R5")
    return (f"{MARK} The IT45 join compared neurons with astrocytes only. Against every class of the held tables the Kv7 genes are not cleanly neuronal: "
            f"KCNQ2 is highest in P7 mouse neurons ({q2['neuron_fpkm']} FPKM) but {q2['best_other_class']} reaches {q2['best_other_fpkm']} (under the 3-fold convention, so 'shared'); "
            f"KCNQ3 is {q3['neuron_fpkm']} in neurons against {q3['best_other_fpkm']} in {q3['best_other_class']} (shared); "
            f"the one human neuron sample reads KCNQ2 at {h2['neuron_fpkm']} against {h2['best_other_fpkm']} in {h2['best_other_class']}; KCNQ4 and KCNQ5 were not queried (unknown). "
            f"A Kv7-blocker-sensitive difference current therefore needs a cell-specific control too, as a Ba2+-sensitive one does; RNA class means, P7, not current. Machine reading (cell_context.py): {cons}.")


def main(check=False):
    text = clause(); changed = 0
    for f, idc, idv, col in TARGETS:
        rows = list(csv.reader(open(f, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]
        i, c = h.index(idc), h.index(col)
        for r in rows[1:]:
            if r[i] == idv and MARK not in r[c]:
                r[c] = (r[c] + " " + text).strip(); changed += 1
        if not check:
            csv.writer(open(f, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    print(("would change " if check else "changed ") + str(changed) + " cell(s)")
    return changed


if __name__ == "__main__":
    csv.field_size_limit(10**9)
    main("--check" in sys.argv)

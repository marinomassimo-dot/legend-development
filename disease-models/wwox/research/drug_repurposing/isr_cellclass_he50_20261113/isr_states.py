#!/usr/bin/env python3
"""HE50 item 5 (IT49-Q02): the ISR gene list from the case, its count checked, and the held-table state of each gene by the existing cell_context join.

  python3 -I isr_states.py            -> writes isr_cell_class_states.tsv and prints the list check

The list is read from the question text of IT49-Q02 (not typed here): "EIF2AK1-4, EIF2B1-5, PPP1R15A/B, EIF2S1" expands to twelve symbols. The case's result note says "all 11 ISR genes": the printed check shows that
count and the effective one apart. The two RNA tables are written by `generation_it47_20261112/b1_cellclass/targets_expression.py --genes ... --prefix isr_expression` from the registered inputs (digests in
`input_digests.tsv`); the join, the 1.0 FPKM floor and the 3-fold rule are `generation_it46_20261111/cell_context.py` unchanged, with the two tables added in this process only. RNA says nothing about the protein-level
direction of the ISR in a WWOX-deficient cell."""
import csv, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
DR = HERE.parent
sys.path.insert(0, str(DR / "generation_it46_20261111"))
import cell_context as cc  # noqa: E402

def case_symbols():
    row = next(r for r in csv.DictReader(open(DR / "batch_sci_20261105/map/open_questions_map.tsv", encoding="utf-8"), delimiter="\t") if r["qid"] == "IT49-Q02")
    inside = re.search(r"\((.*)\)", row["question_text_max300"]).group(1)
    out = []
    for tok in [t.strip() for t in inside.split(",")]:
        m = re.fullmatch(r"([A-Z0-9]*?[A-Z])(\d+)-(\d+)", tok)            # EIF2AK1-4: a numbered family
        n = re.fullmatch(r"([A-Z0-9]+?\d)([A-Z])/([A-Z])", tok)             # PPP1R15A/B: two letter suffixes
        if m and "-" in tok:
            out += [f"{m.group(1)}{i}" for i in range(int(m.group(2)), int(m.group(3)) + 1)]
        elif n:
            out += [f"{n.group(1)}{n.group(2)}", f"{n.group(1)}{n.group(3)}"]
        else:
            out.append(tok)
    return out, row["question_text_max300"]

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__); sys.exit(0)
    syms, text = case_symbols()
    declared = re.search(r"all (\d+) ISR genes", (DR / "generation_it49_20261112/p5_case_inv02/result_it49.md").read_text(encoding="utf-8")).group(1)
    print(f"symbols from the question text: {len(syms)} ({', '.join(syms)}); the result note of the case declares {declared}: the counts differ, and which symbol a shorter list drops is not told by the count (compare the list used by any consumer)")
    for k, sp, f, cls, val, n, neuron, skip in (("mouse_isr", "mouse", "isr_expression_mouse.tsv", "cell_class", "mean_fpkm", "n_samples", r"^neurons?\b", r"^$"),
                                               ("human_isr", "human", "isr_expression_human.tsv", "group", "mean_fpkm", "n_columns", r"^neuron_", r"^(whole_cortex|mouse_astro)$")):
        cc.TABLES.append(dict(key=k, species=sp, path=HERE / f, cls=cls, val=val, n=n, neuron=neuron, skip=skip))
    keep = {"mouse_isr", "human_isr"}
    rows = [r for r in cc.join(syms, "IT49-Q02") if r["table"] in keep]
    with open(HERE / "isr_cell_class_states.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, cc.FIELDS, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
    from collections import Counter
    print(len(rows), "rows;", dict(Counter((r["species"], r["state"]) for r in rows)))

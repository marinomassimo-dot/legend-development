#!/usr/bin/env python3
"""Apply the V10 recheck corrections (SCI48) to the producer's tables, cell by cell.

Idempotent: a cell already equal to the new value is left alone. Every change is
appended to CORRECTIONS.tsv (file, row_id, field, before, after, reason, source).
Run from this folder: python3 apply_v10_corrections.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

EDITS = [
    ("sfn_table.tsv", "S25", "sfn_conc",
     "5 mg/kg intraperitoneal (abstract; source fact)",
     "5 mg/kg intraperitoneal is the RAT dose in the abstract; no mouse dose was recorded (V10 recheck)",
     "the dose belongs to the rat part", "verdicts R, TBI row"),
    ("sfn_table.tsv", "S25", "endpoint",
     "neurologic score at 7 d; oxidative markers at 24 h; neuronal death and contusion volume",
     "null contrast: neurologic score at 7 d and oxidative markers at 24 h only; neuronal death, contusion volume and HO-1/NQO1 were measured in rats, which had no loss arm",
     "the loss contrast has two endpoints", "verdicts R, TBI row"),
    ("matrix.tsv", "M31", "cell_class_and_system",
     "in vivo mouse brain (controlled cortical impact), Nrf2+/+ versus -/-; function (neurologic score 7 d), molecular (oxidative markers 24 h), viability (neuronal death, per abstract)",
     "in vivo mouse brain (controlled cortical impact), Nrf2+/+ versus -/-; function (neurologic score 7 d) and molecular (oxidative markers 24 h); neuronal death and contusion volume were measured in rats without a loss arm",
     "viability was not measured under loss", "verdicts R, TBI row"),
    ("sfn_table.tsv", "S26", "endpoint_class",
     "function",
     "tissue_biochemical (residual haemoglobin); not function in the brief's sense",
     "a tissue readout, not a functional one", "verdicts R, Zhao row"),
    ("sfn_table.tsv", "S26", "neural_class",
     "in vivo mouse and rat brain (striatal autologous-blood ICH): hematoma clearance by microglia/macrophages; function of the phagocytic system (haemoglobin remaining), molecular/cellular",
     "in vivo mouse and rat brain (striatal autologous-blood ICH): hematoma clearance, read as residual haemoglobin; 'microglia-linked' is the authors' attribution in a global knock-out",
     "attribution to microglia is not shown by a global knock-out", "verdicts R, Zhao row"),
    ("sfn_table.tsv", "S27", "species_age_prep",
     "mouse neonatal primary microglia",
     "primary neonatal microglia; the source is inconsistent on species (Methods: mouse p1-p2 pups; Fig. 1-3 legends: rat microglia)",
     "species inconsistency inside the source", "verdicts R, Zhao row"),
    ("matrix.tsv", "M32", "cell_class_and_system",
     "in vivo mouse ICH (and rat), WT versus Nrf2-KO; function of microglia/macrophage clearance (hematoma haemoglobin at 7 d)",
     "in vivo mouse ICH (and rat), WT versus Nrf2-KO; tissue readout: residual hematoma haemoglobin at 7 d (not a functional endpoint; the microglial attribution is the authors', in a global knock-out)",
     "endpoint class corrected", "verdicts R, Zhao row"),
    ("matrix.tsv", "M32", "explanation_supported",
     "H1/H3-direction for a microglia-linked clearance endpoint",
     "H1/H3-direction for a tissue haemoglobin-clearance endpoint",
     "endpoint class corrected", "verdicts R, Zhao row"),
    ("sfn_table.tsv", "S32", "authors_year",
     "Innamorato NG et al. 2008 (kainate slices; Mol Cell Neurosci)",
     "Rojo AI et al. 2008 (kainate slices; Mol Cell Neurosci)",
     "first author mislabelled by V10 and repeated; only the senior author is shared with S14", "audit section 10"),
    ("sfn_table.tsv", "S32", "independence_note",
     "found by V10 (verifier strings); same first author as S14 (a different paper)",
     "found by V10 (verifier strings); shares the senior author, not the first author, with S14 (a different paper)",
     "first-author claim withdrawn", "audit section 10"),
    ("matrix.tsv", "M38", "source",
     "Innamorato 2008 slices (18619545), abstract; no PMC id",
     "Rojo 2008 slices (18619545), abstract; no PMC id",
     "first author corrected", "audit section 10"),
]


def split(line):
    return line.rstrip("\n").split("\t")


def apply(path, edits, log):
    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()
    head = split(lines[0])
    changed = 0
    for fname, row_id, field, before, after, reason, source in edits:
        if field not in head:
            sys.exit(f"{path}: no column {field}")
        col = head.index(field)
        for i, line in enumerate(lines[1:], 1):
            cells = split(line)
            if cells[0] != row_id:
                continue
            if cells[col] == after:
                break
            if cells[col] != before:
                sys.exit(f"{fname} {row_id} {field}: cell is not the expected before-value")
            cells[col] = after
            lines[i] = "\t".join(cells) + "\n"
            log.append((fname, row_id, field, before, after, reason, source))
            changed += 1
            break
        else:
            sys.exit(f"{fname}: row {row_id} not found")
    with open(path, "w", encoding="utf-8") as fh:
        fh.writelines(lines)
    return changed


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        return
    log = []
    n = 0
    for fname in sorted({e[0] for e in EDITS}):
        n += apply(os.path.join(HERE, fname), [e for e in EDITS if e[0] == fname], log)
    if log:
        with open(os.path.join(HERE, "CORRECTIONS.tsv"), "a", encoding="utf-8") as fh:
            for row in log:
                fh.write("\t".join(c.replace("\t", " ") for c in row) + "\n")
    print(f"{n} cell(s) changed")


if __name__ == "__main__":
    main()

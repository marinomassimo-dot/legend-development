"""IT47 P7 (DREAM): across all relations of the IT41-IT44 tables and the IT40 search, how many target genes can a held cell-class table assign to neurons?
Counts per relation: genes neuron-enriched in every table that carries them / not assignable (shared, enriched elsewhere, not detected, tables disagree) / not in any table.
python3 relation_context_summary.py -> relation_context_summary_it47.tsv"""
import csv, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "generation_it46_20261111"))
import cell_context as cc  # noqa: E402
rel = cc.relations(); rows = []
for rid in sorted(rel, key=lambda s: (s[0], int(''.join(c for c in s if c.isdigit()) or 0))):
    by = {}
    for r in cc.join(rel[rid], rid):
        by.setdefault(r["gene"], []).append(r)
    clean = notassign = unknown = 0
    for g, v in by.items():
        seen = [x for x in v if x["state"] != "NOT_IN_TABLE"]
        if not seen: unknown += 1
        elif all(x["state"] == "NEURON_ENRICHED" for x in seen): clean += 1
        else: notassign += 1
    rows.append([rid, len(by), clean, notassign, unknown])
with open(HERE / "relation_context_summary_it47.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["relation_id", "genes", "neuron_attributable", "not_assignable_to_neurons", "not_in_any_table"]); w.writerows(rows)
tot = [sum(r[i] for r in rows) for i in (1, 2, 3, 4)]
print(len(rows), "relations; genes", tot[0], "| attributable", tot[1], "| not assignable", tot[2], "| unknown", tot[3])
print("relations with at least one gene not assignable:", sum(1 for r in rows if r[3] > 0), "| relations with every gene attributable:", sum(1 for r in rows if r[2] == r[1] and r[1] > 0))

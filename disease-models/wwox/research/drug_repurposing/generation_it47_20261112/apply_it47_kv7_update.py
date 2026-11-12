"""IT47 B1: the IT46 context clause on compound view V10 and investigation INV-18 said "KCNQ4 and KCNQ5 were not queried (unknown)"; the B1 extraction queried them. A dated update is appended (the earlier text is kept). Idempotent.  python3 apply_it47_kv7_update.py [--check]"""
import csv, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
TXT = ("[IT47 update] KCNQ4 and KCNQ5 are now queried (RNA class means, same inputs): KCNQ5 is neuron-enriched in both tables (mouse 9.40 against 0.98 in the oligodendrocyte lineage; human sample 15.00), KCNQ4 is shared in mouse and not detected in the human sample. "
       "Of the four Kv7 genes only KCNQ5 is neuron-enriched in every table that carries it; the statement that a Kv7-blocker-sensitive current needs a cell-specific control stands for KCNQ2 and KCNQ3. RNA is not current. Source: generation_it47_20261112/b1_cellclass/scored_it47.md.")
TXT2 = ("[IT47 update 2] The held human KCNQ2 value (0.1 in one neuron sample, 0.2-1.5 in whole cortex) is low across that table and its cause is unknown: it is not a species difference. A second human nuclei table (source dataset not verified) gives neuronal KCNQ2 with OPC at 0.73 of the neuronal maximum, so an OPC contribution to a bath-applied opener is a plausible alternative to control, not shown. RNA is not current.")
EDITS = [(DR / "generation_it41_20261109/compound_view.tsv", "item_id", "V10", "next_test"), (DR / "ranking_it8_p9_20261029/investigations_it20.tsv", "inv_id", "INV-18", "feasibility"), (DR / "ranking_it8_p9_20261029/investigations.tsv", "inv_id", "INV-18", "feasibility")]


def main(check=False):
    csv.field_size_limit(10**9); changed = 0
    for f in sorted({e[0] for e in EDITS}):
        rows = list(csv.reader(open(f, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]
        for ff, idc, idv, col in EDITS:
            if ff != f: continue
            i, c = h.index(idc), h.index(col)
            for r in rows[1:]:
                if r[i] == idv:
                    if "[IT47 update]" not in r[c]:
                        r[c] = (r[c] + " " + TXT).strip(); changed += 1
                    if "[IT47 update 2]" not in r[c]:
                        r[c] = (r[c] + " " + TXT2).strip(); changed += 1
        if not check:
            csv.writer(open(f, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    print(("would change " if check else "changed ") + str(changed))


if __name__ == "__main__":
    main("--check" in sys.argv)

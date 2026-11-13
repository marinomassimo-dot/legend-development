"""IT49: SCI49 package A consumer rows 2-6 and 8 as dated clauses / question edits (idempotent; the original text stays)."""
import csv, sys
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
U3 = ("[SCI49 update 3] Verified by an independent reader: the second human table is the HPA single-nuclei brain table, which the HPA documentation attributes to Siletti et al. 2023 (about 2.6 million nuclei, 11 regions, 48 cell types; the paper itself was not reached). "
      "OPC KCNQ2 RNA is 0.73 of forebrain projection neurons (0.68 of the highest neuronal cluster; 8th of 48 clusters; mouse P17 OPC 0.35 of P7 neurons). The held human 0.1 is a reporting floor, not a measured level. "
      "A Kv7-blocker-sensitive current in OPC is reported in one study in cultured rat cells; nothing is known in slice or at P13-P17. "
      "An OPC control is required only to state that a bath-applied opener acts through neurons (identified NG2-cell recordings in the same slices; a cell-restricted Kcnq2 manipulation if a current exists), not to report the bath effect, its Kv7 dependence or a genotype-by-drug component. RNA is not protein or current.")
QS = {"IT47-Q04": dict(question_text_max300="Does OPC contribute to a bath Kv7 opener or GABA-A modulator effect in Wwox slices (KCNQ2 RNA in OPC 0.73 of forebrain projection neurons in one human nuclei table; functional GABA-A in mouse OPC at abstract level)?",
                        decision_at_stake_max200="Decides whether a slice result may be called neuronal: the OPC control is required for that statement only.",
                        status_evidence="inferences verified by an independent reader (SCI49 A); the OPC GABA-A premise rests on abstracts",
                        blocking_reason="Needs identified NG2-cell recordings at P13-P17 and a cell-restricted Kcnq2 manipulation; Kv7 in OPC rests on one culture study.")}
NEWQ = ["IT49-Q04", "cell_context_verify_sci49_20261112/consumer_delta.md", "Is KCNQ3 RNA in human microglia a measurement of protein or current, and does a Kv7 opener act on microglia in slice?", "Matters only if an opener acts on KCNQ3-containing channels (low priority).", "literature_executable", "OPEN", "", "cell_context_verify_sci49_20261112/consumer_delta.md row 6 (RNA only; floor in mouse microglia, highest in the HPA table)", "2026-11-12", "RNA only; unresolved species or technical difference.", "yes", ""]
IT46_NOTE = ("\n## Update 2026-11-12 (IT49, from SCI49 package A; the text above is kept)\nThe held human KCNQ2 value 0.1 is the table's reporting floor (the same laboratory sets values below 0.1 to 0.1); human whole cortex is also low (KCNQ2/SNAP25 0.001-0.009 against 0.122 in HPA forebrain projection neurons); one patient was selected with anti-Thy1; the cause is not determinable, so \"human neurons lack KCNQ2\" is not permitted. "
             "KCNQ3 RNA in human microglia is the highest in the HPA table and echoed by Zhang 2016 myeloid samples, while mouse microglia Kcnq3 sits at the floor (unresolved; IT49-Q04). The OPC control is needed only for the statement that an effect is neuronal.\n")
DREAM_NOTE = ("\n## Update 2026-11-12 (IT49)\nThe row \"one shared OPC-aware specificity control for both bath levers\" is restated as a conditional addition tied to the attribution (SCI49 A, A5): required only to say that the effect is neuronal; an identified NG2-cell recording in the same slices is the cheapest first step; the GABA-A lever's OPC premise rests on abstracts.\n")

def clause(path, idcol, idval, col, txt, tag, check):
    rows = list(csv.reader(open(path, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; n = 0
    i, c = h.index(idcol), h.index(col)
    for r in rows[1:]:
        if r[i] == idval and tag not in r[c]:
            r[c] = (r[c] + " " + txt).strip(); n += 1
    if not check and n: csv.writer(open(path, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    return n

def main(check=False):
    csv.field_size_limit(10**9); n = 0
    n += clause(DR / "generation_it41_20261109/compound_view.tsv", "item_id", "V10", "next_test", U3, "[SCI49 update 3]", check)
    for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"):
        n += clause(DR / f, "inv_id", "INV-18", "feasibility", U3, "[SCI49 update 3]", check)
    qm = DR / "batch_sci_20261105/map/open_questions_map.tsv"
    rows = list(csv.reader(open(qm, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]
    for r in rows[1:]:
        if r[0] in QS and "verified by an independent reader (SCI49 A)" not in r[h.index("status_evidence")]:
            for col, v in QS[r[0]].items(): r[h.index(col)] = v
            r[h.index("last_touched")] = "2026-11-12"; n += 1
    if "IT49-Q04" not in {r[0] for r in rows}: rows.append(NEWQ); n += 1
    if not check and n: csv.writer(open(qm, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    for f, note, tag in ((DR / "generation_it46_20261111/README.md", IT46_NOTE, "Update 2026-11-12 (IT49, from SCI49"), (DR / "generation_it47_20261112/dream_it47.md", DREAM_NOTE, "Update 2026-11-12 (IT49)")):
        if tag not in f.read_text(encoding="utf-8") and not check:
            open(f, "a", encoding="utf-8").write(note); n += 1
    print(("would change " if check else "changed ") + str(n))
if __name__ == "__main__":
    main("--check" in sys.argv)

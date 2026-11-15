"""IT55: operator-directed wording (roadmap 2026-11-15 items 2 and 3): INV-06 CTGF clause, INV-03 narrowed question, WO-25 blocking_reason (idempotent; --check)."""
import csv, sys
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
OLD6 = "IPOTESI; the Wwox-CTGF link is unsupported."
NEW6 = ("IPOTESI; [ADV-007] the held Wwox expression data neither support nor reverse a Wwox-CTGF link, and they do not separate it from cell composition: "
        "the one human knockout-organoid rise (log2 fold change 1.32, 4 against 2 libraries) is of the size a progenitor-state shift alone would carry, and the mouse bulk tables disagree in sign; expression is not secretion. "
        "The CTGF expression check is closed and is not repeated; CTGF does not become a demonstrated neuronal WWOX product; the conditioned-medium comparison (X1) stays a conditional design, reopened only with a pertinent measured premise (OQ11).")
C3 = " [ADV-009] The qualified proposal stands and the question narrows to the values and conditions still missing (the pair has one agent measured on the three isoforms and one measured on Cav3.2 only): for the Cav3.2-only agent, Cav3.1 and Cav3.3 (three-isoform profile only at abstract level, in oocytes); a same-condition comparison of the two agents; and hERG or QT values (none for the Cav3.2-only agent; for the other agent hERG differs about 100-fold between one patch-clamp abstract and binding or screening values, not reconciled). The three-isoform agent's values (Kd 530, 3552 and 837 nM on Cav3.1, 3.2 and 3.3) come from rat channels in HEK cells; the Cav3.2-only agent's values (IC50 2.9 uM racemate on Cav3.2) from human Cav3.2a in a Fluo-4 influx assay; no margin of any kind is computed across different assays."
WO25 = ("Narrowed 2026-11-15 (ADV-009): the flunarizine values on the three isoforms and the efonidipine values on Cav3.2 are read in full text. Still missing: efonidipine on Cav3.1 and Cav3.3 (full text of PMID 19401195 not reached; abstract level only), "
        "a same-condition comparison of the two agents, and any efonidipine hERG or QT value. Route facts in cav3_pair_adv009_20261115/access.tsv; revival: the full text of PMID 19401195, or one laboratory report with both agents on the three isoforms.")
def w(p, rows): csv.writer(open(p, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
def main(check=False):
    csv.field_size_limit(10**9); n = 0
    for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"):
        p = DR / f; rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; k = 0
        i = h.index("inv_id")
        for r in rows[1:]:
            if r[i] == "INV-06" and OLD6 in r[h.index("next_test")]:
                r[h.index("next_test")] = r[h.index("next_test")].replace(OLD6, NEW6); k += 1
            if r[i] == "INV-03" and "[ADV-009]" not in r[h.index("decisive_uncertainty")]:
                r[h.index("decisive_uncertainty")] += C3; k += 1
        if not check and k: w(p, rows)
        n += k
    p = DR / "batch_sci_20261105/map/open_questions_map.tsv"; rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]
    for r in rows[1:]:
        if r[0] == "WO-25" and r[h.index("blocking_reason")] != WO25:
            r[h.index("blocking_reason")] = WO25; n += 1
    if not check and n: w(p, rows)
    print(("would change " if check else "changed ") + str(n))
if __name__ == "__main__":
    main("--check" in sys.argv)

"""IT46 P4: the corrected designs of the two audited comparisons reach their consumers (idempotent; marker "[IT46 audit]").
Kv7 (R5 -> R5a/R5b, with the reviewer's additions): investigations INV-18 next_test, compound view V10 next_test, open question IT45-Q01.
KEAP1 reagent pair (S10): investigations INV-08 next_test, compound view V19 next_test.
Dated lines at the foot of the two IT45 notes. python3 apply_it46_audit.py [--check]"""
import csv, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
MARK = "[IT46 audit]"
KV7 = (MARK + " The IT45 comparison of an opener in the bath with an equal injected current does not hold on burst incidence (a slice-level event that one injected cell cannot change; a direct current also leaves input resistance unchanged while an opener lowers it). "
       "Corrected: R5a, the opener lowers the burst rate within each slice against a vehicle time control and the effect is reversed or occluded by a Kv7 blocker (or reproduced by a second opener of another chemotype); "
       "R5b, a non-Kv7 hyperpolarising manipulation of the slice is compared at matched shift of the recorded cells' membrane potential and matched input-resistance change, at three or more levels; "
       "single-cell comparisons use dynamic clamp on cell-level endpoints only; the animal is the statistical unit. A Kv7-blocker-sensitive current that is not smaller in the knockout does not refute an opener lever (it tests a deficit, not the lever). "
       "Useful in general and specific to the Wwox lesion are separate tests: the second needs a genotype-by-drug interaction against a non-Wwox hyperexcitable preparation matched on baseline burst rate. Source: generation_it46_20261111/p4_audit_it46.md; verify_p4/VERDICTS.md.")
KEAP = (MARK + " The covalent and the non-covalent compound are not compared at equal concentration and time (the electrophile is consumed by thiols and persists after washout): a phase 0 matches exposure on a proximal NRF2 reading (concentration-response, time-course, cytotoxicity, glutathione, washout) first; "
        "at least two independent NFE2L2-knockdown reagents with measured efficiency; an NRF2-independent control gene set beside the target set; a WWOX genotype factor, since the pair speaks to the NRF2 pathway and not yet to the WWOX hypotheses; neuron and astrocyte cultures have no network, so a network outcome is a second phase. Source: generation_it46_20261111/p4_audit_it46.md; verify_p4/VERDICTS.md.")
OQ = (" " + MARK + " The 'equal current-injection' arm is replaced by R5a/R5b (see INV-18 next test): the injection arm has no burst endpoint.")
EDITS = [(DR / "generation_it41_20261109/compound_view.tsv", "item_id", "V10", "next_test", KV7), (DR / "ranking_it8_p9_20261029/investigations_it20.tsv", "inv_id", "INV-18", "next_test", KV7),
         (DR / "ranking_it8_p9_20261029/investigations.tsv", "inv_id", "INV-18", "next_test", KV7),
         (DR / "generation_it41_20261109/compound_view.tsv", "item_id", "V19", "next_test", KEAP), (DR / "ranking_it8_p9_20261029/investigations_it20.tsv", "inv_id", "INV-08", "next_test", KEAP),
         (DR / "ranking_it8_p9_20261029/investigations.tsv", "inv_id", "INV-08", "next_test", KEAP),
         (DR / "batch_sci_20261105/map/open_questions_map.tsv", "qid", "IT45-Q01", "blocking_reason", OQ)]
NOTES = [(DR / "generation_it45_20261111/p3_lever_it45.md", "\n**Update 2026-11-11 (IT46 P4).** Section 1 row R5 and section 4 do not hold on burst incidence: the injection arm has no burst endpoint. The corrected design (R5a mediation with a Kv7 blocker or a second chemotype, R5b a non-Kv7 hyperpolarisation matched on membrane-potential shift and input-resistance change, dynamic clamp for single cells, the animal as unit, a genotype-by-drug test for Wwox specificity) is in `../generation_it46_20261111/p4_audit_it46.md`. The IT45 text above is left as written.\n"),
         (DR / "next_batch_it45_20261111/BRIEFS.md", "\n**Update 2026-11-11 (IT46 P4).** B2: the 'equal current-injection hyperpolarisation' arm is replaced (see `../generation_it46_20261111/p4_audit_it46.md`). B1: add an exposure-matching phase 0, a second knockdown reagent, an NRF2-independent control gene set and a WWOX genotype factor to the SCI46 comparison rows.\n")]


def main(check=False):
    csv.field_size_limit(10**9); changed = 0
    for f in sorted({e[0] for e in EDITS}):
        rows = list(csv.reader(open(f, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]
        for ff, idc, idv, col, txt in EDITS:
            if ff != f:
                continue
            i, c = h.index(idc), h.index(col)
            for r in rows[1:]:
                if r[i] == idv and MARK not in r[c]:
                    r[c] = (r[c] + (txt if txt.startswith(" ") else " " + txt)).strip(); changed += 1
        if not check:
            csv.writer(open(f, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    for f, line in NOTES:
        t = f.read_text(encoding="utf-8")
        if "Update 2026-11-11 (IT46 P4)" not in t:
            changed += 1
            if not check:
                f.write_text(t.rstrip("\n") + "\n" + line, encoding="utf-8")
    print(("would change " if check else "changed ") + str(changed))


if __name__ == "__main__":
    main("--check" in sys.argv)

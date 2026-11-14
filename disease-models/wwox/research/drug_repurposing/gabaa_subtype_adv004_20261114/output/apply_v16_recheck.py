#!/usr/bin/env python3
"""Apply the V16 recheck corrections C1-C10 (verify/recheck_readme.md) to README.md, consumer_delta.md and the SCI47 update block; idempotent.

Run from this folder: python3 output/apply_v16_recheck.py. Prints applied, already-applied and missing anchors.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SCI47 = os.path.join(os.path.dirname(ROOT), "inhibitory_defect_sci47_20261112", "README.md")

README = [
    ("read at full text (2026-11-14)", "read as text and tables (2026-11-14)"),
    ("They were read as complete originals through the Europe PMC XML (text, Methods, every table and legend; figures only partly: see Limits)",
     "They were read as text, Methods and every table through the Europe PMC XML; figures largely not opened (partial_fulltext_read; see Limits)"),
    ("**All 38 numbers of the IT14 table match the sources**; IT14 is a subset and omits what changes a reading: SD and n",
     "**All 38 checked rows of the IT14 table hold (37 value rows; the 38th lists omissions)**; IT14 is a subset and omits what changes a reading (list not exhaustive): SD and n"),
    ("there is **no independent replication** (the 2026 Phase IIa paper, PMID 42886059, rests its α2 preference on Ralvenius alone and cites neither Hammer nor Jensen; its primary-outcome difference is 0.46 points, p = 0.47)",
     "there is **no independent same-design replication with diazepam** (Hammer, an independent human-oocyte series without a diazepam series, points the same way for NDMC; the 2026 Phase IIa paper, PMID 42886059, cites Ralvenius 2016 alone, in its Introduction, for the in vitro α2 preference; Hammer and Jensen do not appear in its body text, the reference list was not checked; primary-outcome difference 0.46 points, p = 0.47, underpowered, 33 of 76 planned)"),
    ("clobazam is at or below 1 in both (0.78 and 1.02); potency shows no α-selectivity in either paper;",
     "clobazam is about 1 or below (0.78 Ralvenius; 1.02 Hammer); α1, α2 and α5 EC50 lie within about 1.6-fold in both papers and α3 is the least potent (clobazam 1.10 vs 0.39–0.61 µM in Ralvenius, 240 vs 132–174 nM in Hammer, P < 0.05; NDMC 0.81 vs 0.49–0.58 µM, 282 vs 98–151 nM, P < 0.01 vs α2 in Hammer);"),
    ("NDMC is α2 = α3 > α1 in both", "NDMC α2 is about equal to α3 and above α1 in both"),
    ("Hammer's \"non-selective\" is relative to clonazepam, whose own α2/α1 (1.21 total, 1.40 increment) is not flat, and its Table 3 shows",
     "Hammer calls NDMC non-selective, like clonazepam, whose α2/α1 is 1.21 (total) or 1.40 (increment), α1 against α2 not significant in its Table 3, so the non-selective benchmark is itself above 1.0 and imprecisely known; its Table 3 shows"),
    ("reports diazepam at 508 ± 28% (N = 5) at the subunit set where Ralvenius reports 227 ± 15% (text 237%), while the diazepam EC50 agrees (59 versus 71 nM): a roughly twofold efficacy difference between two laboratories in one nominal system, larger than the NDMC α2/α1 effect: efficacy values in this field are laboratory-dependent for reasons the three papers do not isolate (INFERENZA).",
     "reports diazepam at 508 ± 28% (N = 5) at the nominal subunit set where Ralvenius reports 227 ± 15% (text 237%), while the diazepam EC50 agrees (59 versus 71 nM). In this one pair of laboratories (Fisher: rat α3β3γ2L, HEK-293T, about 3 µM GABA; Ralvenius: rat α3β3γ2, EC10 8 µM) diazepam efficacy differs about twofold (about 1.8 if the bases differ), so efficacy values may vary between laboratories for reasons these papers do not isolate (INFERENZA from one comparison). Fisher 2011 was read as text; its tables and figures were not returned."),
    ("read at full text by the verifier)", "read as text by the verifier)"),
    ("potency shows no α-selectivity; no independent replication exists.",
     "potency differs little among α1, α2 and α5 and α3 is least potent; no independent same-design replication with diazepam exists (Hammer, an independent human-oocyte series without a diazepam series, points the same way for NDMC)."),
    ("and is not reproduced as a contrast by Hammer: 1.02 against 1.33)",
     "and is smaller and untested in Hammer: 1.02 against 1.33 total, 1.03 against 1.65 increment, both called non-selective)"),
    ("the producer's readings of Hammer's diazepam bars (about 254, 241, 335 and 225 at α1, α2, α3, α5, `output/numbers.tsv` N072–N076) **conflict",
     "the producer's diazepam bar readings at α1 and α2 (about 254 and 241; `output/numbers.tsv` N072, N073) **conflict"),
    ("the verifier could not open the figure; the derived",
     "the α3 and α5 readings (335, 225) are within the text's 2.3–3.4-fold bound and N076 is a clobazam bar (about 253); the verifier opened no figure; the derived"),
    ("with Hammer's non-selective clonazepam ratio (1.21 total, 1.40 increment) as the benchmark for \"non-selective\", not 1.0;",
     "with the clonazepam (or diazepam) ratio measured in the same new series as the benchmark for \"non-selective\" (Hammer's 1.21 / 1.40 is one small-n dataset, α1 n = 4, α2 n = 5, and only indicates that the benchmark is not 1.0);"),
    ("IT14 transcription 38 of 38;", "IT14 transcription 38 of 38 rows (37 value rows plus the omissions row);"),
    ("conditions and trigger 5 of 6 rows correct (the producer's design position judged correct with overstatements, **corrected above**); absence: 15 searches in PubMed and Europe PMC, no other primary paper",
     "conditions and trigger: 3 rows correct, 1 correct with additions, 1 incomplete, 1 (the design position) correct with overstatements, **corrected above**; absence: 9 logged search strings plus 6 unlogged exploratory PubMed strings (PubMed and Europe PMC), no other primary paper"),
    ("Ralvenius Fig 1 and Figs S1–S2, Jensen Figs 1–2 and Hammer Figs 3 and 4 were not opened by the verifier;",
     "the verifier opened no figure of any paper and the producer opened Hammer Figs 3 and 4 only; Hammer Figs 1, 2, 5, 6, Ralvenius Fig 1 and Figs S1–S2, Jensen Figs 1–2 and the tables and figures of Fisher 2011 and of the Phase IIa paper were not opened (the Phase IIa clinical results were not read);"),
    ("two engines, 15 strings, not a census;", "two engines, 9 logged plus 6 unlogged exploratory strings, not a census;"),
]
DELTA = [
    ("\"data exist, selectivity basis- and laboratory-dependent, alpha2-preferring not established\"",
     "\"data exist, selectivity basis-dependent and not shown to reproduce across laboratories, alpha2-preferring not established\""),
    ("with Hammer's clonazepam ratio as the \"non-selective\" benchmark", "with the clonazepam ratio measured in the same new series as the \"non-selective\" benchmark"),
    ("all 38 numbers match;", "all 38 checked rows hold (37 value rows plus the omissions row);"),
    ("the Phase IIa paper rests the preference on Ralvenius alone (primary outcome difference 0.46 points, p = 0.47)",
     "the Phase IIa paper cites Ralvenius alone for the in vitro preference (reference list not checked; primary outcome difference 0.46 points, p = 0.47)"),
    ("replaced by \"rests on Ralvenius 2016 alone\"", "replaced by \"cites Ralvenius 2016 alone in its Introduction\""),
]
SCI = [
    ("potency shows no alpha-selectivity; there is no independent replication.",
     "potency differs little among alpha1, alpha2 and alpha5 and alpha3 is least potent; there is no independent same-design replication with diazepam (Hammer's independent human-oocyte series, without diazepam, points the same way)."),
]


def apply(path, pairs):
    body = open(path, encoding="utf-8").read()
    for old, new in pairs:
        if new in body:
            print("already  ", old[:60])
        elif old in body:
            body = body.replace(old, new)
            print("applied  ", old[:60])
        else:
            print("MISSING  ", old[:60])
    open(path, "w", encoding="utf-8").write(body)


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        return
    apply(os.path.join(ROOT, "README.md"), README)
    apply(os.path.join(ROOT, "consumer_delta.md"), DELTA)
    apply(SCI47, SCI)


if __name__ == "__main__":
    main()

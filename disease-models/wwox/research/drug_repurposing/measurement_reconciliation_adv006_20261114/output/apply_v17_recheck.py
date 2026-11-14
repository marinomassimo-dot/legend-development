#!/usr/bin/env python3
"""Apply the V17 recheck corrections (verify/recheck_readme.md) to README.md, consumer_delta.md and the type cells of conflicts.tsv; idempotent.

Run from this folder: python3 output/apply_v17_recheck.py. Prints applied, already-applied and missing anchors; type changes are appended to output/CORRECTIONS.tsv.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

README = [
    ("and **no file consolidates** the SCI42 and SCI47 requests.", "and **no file was found** that consolidates the SCI42 and SCI47 requests (two bounded searches, not the whole repository)."),
    ("There is **no** earlier specification of the sIPSC re-record with glutamate block, of the evoked IPSC or of the agonist response (the August design gives sIPSC and mIPSC only after rupture)",
     "There is **no** earlier specification of the sIPSC re-record with glutamate block or of the evoked IPSC in the August candidates, and none of an agonist-response amplitude measurement (the August design applies isoguvacine by puff only for the reversal potential and the firing sign, and gives sIPSC and mIPSC only after rupture)"),
    ("who had missed CLAIM002 in his own first search and confirmed it in the second", "who missed CLAIM002 in the first search and confirmed it in the second"),
    ("103 table rows were read (87 in the thread, 16 outside it); 20 of them are pointer rows of `explanations.tsv` and `conditional_prediction.tsv`, so by the S0 definition about 83 requests (about 67 in the thread); they reduce to **28 measurement rows, of which about nine are slice recordings** (the rest are drug arms, a heterologous receptor series, a pH measurement, histology, re-analyses, rescue and human arms)",
     "104 table rows (103 read, plus IT45-Q05 added: 88 in the thread, 16 outside it); 20 of them are pointer rows of `explanations.tsv` and `conditional_prediction.tsv`, so by the S0 definition about 84 requests (about 68 in the thread); they reduce to **28 measurement rows, of which about nine are core Synapsin-Cre layer II/III recordings** (the rest include other recordings (M10, M12, M13, M19, M25), drug arms, a heterologous receptor series, a pH measurement, histology, re-analyses, rescue and human arms)"),
    ("CF06 global allele against Synapsin-Cre and CF07 CA3 against layer II/III are different preparations (the August design also lists layer 2/3 as secondary: the CF07 quote is verbatim but selective);",
     "CF06 global allele against Synapsin-Cre is a different preparation and CF07 CA3 against layer II/III is a priority difference inside the August design (which also lists layer 2/3 as secondary: the CF07 quote is verbatim but selective);"),
    ("**None of the conflicts can be adjudicated from the packages**, because none of them holds a recording;",
     "**None of the six genuine conflicts is decided by the packages**, since none holds a recording (CF23 and CF03 are resolvable by a design choice);"),
    ("the four candidate tables (`new_measurements.tsv`, `levers.tsv`, `matrix.tsv`, `conditional_prediction.tsv`) differ in which of the seven design slots they have; `conditional_prediction.tsv` has no unique key;",
     "the four candidate tables (`new_measurements.tsv`, `levers.tsv`, `matrix.tsv` and IT14's `reopen_searches_it14_p3.tsv`) differ in which of the seven design slots they have; `conditional_prediction.tsv` is a fifth table with no unique key;"),
    ("while the `pharmacological_comparison` role reads `new_measurements.tsv`, so the table list is not the only registration route.",
     "while the `pharmacological_comparison` role reads `new_measurements.tsv` only together with a `comparison.tsv`, which neither package has, so a registration needs either new design-table names or a comparison table authored by the owners."),
    ("(about 40 of 103 rows re-derived and agreed;", "(about 40 of 104 rows re-derived and agreed;"),
    ("the conflicts sit in configuration, cohort and cell class, not in antagonist identity, unit or age bin",
     "the conflicts sit in configuration, cohort structure, burst state against glutamate block and the matching variable, not in antagonist identity, unit or age bin"),
    ("overstated in five places", "overstated in six places"),
    ("One launch each at this point.", "One launch each, then V17 resumed twice (the blind check was the first; a narrow recheck of this README and the delta the second: 10 tool uses, 266,708 subagent tokens)."),
]
DELTA = [
    ("the mIPSC half is already specified (SCI42 M04 = SCI47 Phase 0 (ii))", "the mIPSC half is requested in SCI42 M04 and SCI47 Phase 0 (ii), with the internal solution unstated or different from NP3P2's"),
    ("L3 kept as a measurement (E_GABA) and dropped as a drug arm in SCI47 against kept in SCI42 (CF15, a prediction versus a lever status)",
     "SCI42 lists chloride-gradient manipulations only as conditional prediction rows; SCI47 L3 is dropped as a drug arm now (a gap, not a conflict: CF15)"),
    ("the `pharmacological_comparison` role reads `new_measurements.tsv`", "the `pharmacological_comparison` role reads `new_measurements.tsv` only with a `comparison.tsv` that neither package has"),
    ("overstated in five places", "overstated in six places"),
    ("about 40 of 103 relation labels re-derived", "about 40 of 104 relation labels re-derived"),
]
TYPES = {"CF06": "gap", "CF07": "gap", "CF09": "gap", "CF15": "gap", "CF23": "genuine"}


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


def conflicts():
    p = os.path.join(HERE, "conflicts.tsv")
    rows = [l.split("\t") for l in open(p, encoding="utf-8").read().rstrip("\n").split("\n")]
    ti, wi = rows[0].index("type"), rows[0].index("why_both_cannot_be_met_in_one_recording")
    log = []
    for r in rows[1:]:
        if r[0] in TYPES and r[ti] != TYPES[r[0]]:
            note = r[ti]
            log.append([r[0], r[ti], TYPES[r[0]]])
            r[wi] = "V17 note: " + note + " || " + r[wi]
            r[ti] = TYPES[r[0]]
    open(p, "w", encoding="utf-8").write("\n".join("\t".join(r) for r in rows) + "\n")
    if log:
        with open(os.path.join(HERE, "CORRECTIONS.tsv"), "a", encoding="utf-8") as f:
            for k, b, a in log:
                f.write("\t".join(["conflicts.tsv", k, "type", b, a, "keep type to the enum; the note moved to the why cell (V17 recheck)", "verify/recheck_readme.md item 7"]) + "\n")
    print(len(log), "type cell(s) restored to the enum")


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        return
    apply(os.path.join(ROOT, "README.md"), README)
    apply(os.path.join(ROOT, "consumer_delta.md"), DELTA)
    conflicts()


if __name__ == "__main__":
    main()

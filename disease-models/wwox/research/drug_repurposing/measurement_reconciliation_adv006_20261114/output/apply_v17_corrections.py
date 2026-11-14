#!/usr/bin/env python3
"""Apply the V17 verifier corrections (ADV-006) to the producer's tables; idempotent.

Run from this folder: python3 apply_v17_corrections.py. Reads two source cells verbatim for the added conflict, writes the changes
to crosswalk.tsv, conflicts.tsv, closes.tsv, measurements.tsv and phase_note.md, and appends each change to CORRECTIONS.tsv.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DR = os.path.abspath(os.path.join(HERE, "..", ".."))
SRC = "verify/audit.md; verify/verdicts.tsv"
MAP = os.path.join(DR, "batch_sci_20261105", "map", "open_questions_map.tsv")
S42 = "chloride_gradient_sci42_20261110/output/new_measurements.tsv"
S47 = "inhibitory_defect_sci47_20261112/output/levers.tsv"
PFX = "disease-models/wwox/research/drug_repurposing/"
CLOG = []


def read(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return [l.split("\t") for l in f.read().rstrip("\n").split("\n")]


def write(name, rows):
    with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
        f.write("\n".join("\t".join(r) for r in rows) + "\n")


def table(path):
    with open(path, encoding="utf-8") as f:
        rows = [l.split("\t") for l in f.read().rstrip("\n").split("\n")]
    return rows[0], rows[1:]


def log(f, rid, field, before, after, reason):
    CLOG.append([f, rid, field, before, after, reason, SRC])


def set_cell(name, key, col, new, reason, key_col=0, append=False):
    rows = read(name)
    ci = rows[0].index(col)
    for r in rows[1:]:
        if r[key_col] == key:
            after = (r[ci] + " | " + new) if append else new
            if new in r[ci] or r[ci] == after:
                return
            log(name, key, col, r[ci], after, reason)
            r[ci] = after
    write(name, rows)


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        return
    # 1. missed request IT45-Q05
    cw = read("crosswalk.tsv")
    rid = "map#open_questions_map:IT45-Q05"
    if not any(r[0] == rid for r in cw):
        h, body = table(MAP)
        row = [r for r in body if r[0] == "IT45-Q05"][0]
        q = row[h.index("question_text_max300")]
        assert q.startswith("What is the interstitial pHo at the recording depth in the Wwox slice by genotype")
        new = [rid, PFX + "batch_sci_20261105/map/open_questions_map.tsv", "IT45-Q05, column question_text_max300", q,
               "Wwox slice (question text)", "not stated by the source", "interstitial pHo at the recording depth", "30-37 C for the TREK-1 half",
               "not stated by the source", "by genotype", row[h.index("decision_at_stake_max200")], "no (No genotype-resolved tissue pH measurement exists)",
               "M22", "partly_overlapping",
               "V17 (missed request): the pHo-by-genotype half is the same quantity as glun2b M01 (M22); the TREK-1 Hill-slope half at 30-37 C is another measurement (a pHo response of a channel, no recording of this slice)."]
        assert len(new) == len(cw[0])
        cw.append(new)
        write("crosswalk.tsv", cw)
        log("crosswalk.tsv", rid, "(row added)", "", "request row", "missed request: IT45-Q05 is the same slice-pH quantity as glun2b M01")
    # 2. missed conflict CF23, quotes copied from the two source cells
    cf = read("conflicts.tsv")
    if not any(r[0] == "CF23" for r in cf):
        h42, b42 = table(os.path.join(DR, S42))
        a = [r for r in b42 if r[0] == "M10"][0][h42.index("measurement")]
        qa = "Matched non-GABAergic suppression of bursts titrated to the same percent of evoked synaptic charge removed"
        h47, b47 = table(os.path.join(DR, S47))
        b = [r for r in b47 if r[0] == "L1"][0][h47.index("functional_comparator")]
        qb = "a submaximal NMDAR block (d-APV) or a hyperpolarising manipulation matched on the recorded cells' membrane potential and input resistance"
        assert qa in a and qb in b
        new = ["CF23", "M15", "other (matching variable of the matched arm)", PFX + S42 + "#M10:measurement", qa, PFX + S47 + "#L1:functional_comparator", qb,
               "genuine (V17: missed by the producer)",
               "the same arm and the same burst endpoint, but the titration target differs (percent of evoked synaptic charge removed versus membrane potential and input resistance of the recorded cells); one titration cannot be set to both in the same cell.",
               "yes: SCI42's own design_choice_not_finding cell calls the metric a design choice; SCI47 does not give a reason",
               "whether a non-GABAergic comparator that removes the same synaptic charge also matches the cells' membrane potential and input resistance decides how a drug arm is read against it"]
        assert len(new) == len(cf[0])
        cf.append(new)
        write("conflicts.tsv", cf)
        log("conflicts.tsv", "CF23", "(row added)", "", "conflict row", "missed genuine conflict hidden inside merge M15")
    # 3. reclassify conflicts
    for k, t, why in [
        ("CF06", "distinct preparations (V17: not a conflict inside one preparation; the producer keeps M05 and M14 apart itself)", "different preparation"),
        ("CF07", "gap (V17: the quote is verbatim but selective; the same CELL_TYPE list names layer 2/3 pyramidal neurons, dorsal cortex, as secondary)", "selective quote"),
        ("CF09", "gap (V17: an interpretive standard; both can be recorded together)", "interpretive standard, not a recording condition"),
        ("CF15", "gap (V17: one side is a prediction in conditional_prediction.tsv, the other a lever status in levers.tsv)", "prediction versus lever status")]:
        set_cell("conflicts.tsv", k, "type", t, why)
    # 4. closes counted on the conservative reading, basis kept
    set_cell("closes.tsv", "WO-15", "closes", "partly (conservative; fully against the map wording once M02 and M04 are done)", "V17: the producer's own basis cell says fully against the map text")
    set_cell("closes.tsv", "IT46-Q10", "closes", "partly (conservative; fully if two nested cohorts are accepted)", "V17: the producer's own basis cell says fully under two nested cohorts")
    # 5. measurements
    set_cell("measurements.tsv", "M15", "mode_and_configuration", "V17: the matching variable differs between sources (SCI47 L1 functional_comparator: membrane potential and input resistance); conflict CF23", "missed conflict inside a merge", key_col=0, append=True)
    set_cell("measurements.tsv", "M22", "requests_merged", "map#open_questions_map:IT45-Q05 (V17: missed request)", "missed request", append=True)
    set_cell("measurements.tsv", "M22", "source_names", "map IT45-Q05 (pHo half)", "missed request", append=True)
    for k, why in [("M01", "NP3P2, WO-17, Phase 0 (vii) and the rescue item"), ("M05", "IT46-Q04 and the human-organoid E_GABA item")]:
        set_cell("measurements.tsv", k, "requests_merged", "V17: not one session: the list mixes members that need a changed cell (" + why + ")", "list wider than one session", append=True)
    # 6. phase_note stale sentence
    p = os.path.join(HERE, "phase_note.md")
    t = open(p, encoding="utf-8").read()
    i = t.find("Copies of the table generators are in `build_scripts/`")
    if i >= 0:
        j = t.find("\n", i)
        old = t[i:j]
        t = t[:i] + "The table generators are not in the tree (V17: `build_scripts/` was removed; the tables are not regenerable from the folder, `quote_check.py` is)." + t[j:]
        open(p, "w", encoding="utf-8").write(t)
        log("phase_note.md", "line 7", "text", old[:120] + "...", "generators not in the tree", "stale sentence")
    if CLOG:
        pth = os.path.join(HERE, "CORRECTIONS.tsv")
        new = not os.path.exists(pth)
        with open(pth, "a", encoding="utf-8") as f:
            if new:
                f.write("file\trow_id\tfield\tbefore\tafter\treason\tsource\n")
            for r in CLOG:
                f.write("\t".join(c.replace("\t", " ").replace("\n", " ") for c in r) + "\n")
    print(len(CLOG), "change(s)")


if __name__ == "__main__":
    main()

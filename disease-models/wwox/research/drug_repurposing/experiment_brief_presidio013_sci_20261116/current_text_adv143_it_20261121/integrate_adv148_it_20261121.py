"""ADV-148 integration (IT, 2026-11-21). Applies the design team's replacements S01 to S14
(REPLACEMENTS_FOR_IT_ADV148_SCI_20261121.tsv) to the current text, by script.
- A marker named by a replacement is replaced by the answer note (plus an OPEN-GAP marker for the laboratory question, when the row has one);
  the old marker goes to the History.
- A sentence the replacement says to change is replaced in place; the old sentence goes to the History.
- Every numeric token of an inserted text must be in the row's numeric_tokens column, in another row's column, in the older texts or in the current text;
  otherwise the run stops (nothing is written).
Usage: python3 integrate_adv148_it_20261121.py TEXT.md REPLACEMENTS.tsv OLD_A.md OLD_B.md [--dry-run]   (idempotent)"""
import csv
import re
import sys

TOK = re.compile(r"(?<![A-Za-z0-9.])\d+(?:[.,]\d+)?")
IDS = re.compile(r"\b(?:Q|C|T|E|L|R|P|S|M|H|N)\d{1,3}\b|\bQA\d\b|\bADV-\d+\b|\b\d{4}-\d{2}-\d{2}\b|\bPMID\s*\d+\b|\bFTR-[\w-]+\b")
STATUS = {
    "REAL_RULE_INFERENCE": "INFERENCE: a rule proposed by the design team, not a source value",
    "WORDING_DEFECT": "corrected by the design team",
    "WORDING_DEFECT_MINE": "corrected by the design team",
    "ANSWERED_BY_DOCUMENTS": "stated in a source text",
    "ANSWERED_BY_DOCUMENTS_PLUS_RULE_INFERENCE": "stated in a source text; the latency rule is an INFERENCE, to be fixed before data",
    "ANSWERED_BY_DOCUMENTS_PLUS_WORDING_DEFECT": "stated in a source text; the wording of the earlier row is corrected",
    "REAL_LABORATORY_PLUS_RANGE": "INFERENCE: an illustrative range with its basis, not a source value; the figure itself is the laboratory's",
}


def toks(s):
    return set(TOK.findall(IDS.sub(" ", s)))


def main(a):
    dry = "--dry-run" in a
    a = [x for x in a if x != "--dry-run"]
    text_p, tsv_p, a_p, b_p = a[1:5]
    t = open(text_p, encoding="utf-8").read()
    if "Design-team answer S03" in t:
        print("already integrated")
        return 0
    old_tok = toks(open(a_p, encoding="utf-8").read() + open(b_p, encoding="utf-8").read())
    rows = {r["repl_no"]: r for r in csv.DictReader(open(tsv_p, encoding="utf-8", newline=""), delimiter="\t")}
    glob = set(x for r in rows.values() for x in r["numeric_tokens"].split(";") if x)
    cur_tok = toks(t)
    removed = []
    unlisted = []
    inserted = []

    def note(rid, gid, body, lab_q=None, owner="laboratory", status=None):
        r = rows[rid]
        miss = sorted(toks(body) - (old_tok | glob | cur_tok))
        if miss:
            unlisted.append((rid, miss))
        st = status or STATUS[r["class"]]
        s = f"[Design-team answer {gid}, 2026-11-21; status: {st}. {body}]"
        inserted.append(s)
        if lab_q:
            s += f"\n\n**OPEN-GAP {rid} (owner {owner}): {lab_q}**"
        return s

    def rep(old, new, label, keep=True):
        nonlocal t
        assert t.count(old) == 1, ("anchor not unique or absent", label, old[:80], t.count(old))
        t = t.replace(old, new)
        if keep:
            removed.append((label, old))

    def marker(mid, new):
        nonlocal t
        pat = re.compile(r"\*\*(?:OPEN-GAP|CONFLICT-OPEN) " + re.escape(mid) + r" \(owner \w+\):.*?\*\*", re.S)
        ms = pat.findall(t)
        assert len(ms) == 1, ("marker", mid, len(ms))
        removed.append(("Marker " + mid, ms[0]))
        t = pat.sub(lambda m: new, t, count=1)

    def sub_in_notes(old, new, label, count=None):
        """Replace a phrase only on lines that are design-team notes (before the History)."""
        nonlocal t
        k = t.index("\n## History")
        head, tail = t[:k], t[k:]
        lines = head.split("\n")
        n = 0
        for i, l in enumerate(lines):
            if l.startswith("[Design-team answer") and old in l:
                n += l.count(old)
                lines[i] = l.replace(old, new)
        assert n and (count is None or n == count), ("phrase in notes", label, old, n)
        removed.append((label, f"'{old}' replaced by '{new}' on {n} note line(s)"))
        t = "\n".join(lines) + tail

    # ---- S01 (C002, R3C02): the rule sentence in Ages, the CLAR-SERIES note, the marker
    s = rows["S01"]
    rep("Which ages the series contains is fixed by this rule (the assay age and at least two older ages); the earlier remark that the series \"straddles P11 and P14\" is not a further requirement (it is in the History).",
        "Which ages the series contains is fixed by this rule (the assay age and at least two older ages). A series that also straddles P11 and P14 is required only if the chloride-window read is wanted; when the assay age is P14 or later that read needs P11 as one further age (seven more wild-type cells); otherwise the series is as defined and no further age is added.",
        "Ages, rule sentence of the wild-type series")
    m = re.search(r"\[Design-team answer CLAR-SERIES, 2026-11-21;.*?\]", t, re.S)
    assert m
    removed.append(("Note CLAR-SERIES (superseded)", m.group(0)))
    t = t[:m.start()] + note("S01", "C002/CLAR-SERIES",
                             "The wild-type series is the assay age plus at least two older ages inside the window to about P28. A series that also straddles P11 and P14 is required only if the chloride-window read is wanted; when the assay age is P14 or later that read needs P11 as one further age (seven more wild-type cells); otherwise the series is as defined and no further age is added. This note replaces the earlier note on the series: it describes the optional straddle, not a further requirement for the primary contrast.") + t[m.end():]
    marker("R3C02", f"**OPEN-GAP S01 (owner laboratory): {s['question_for_laboratory_or_operator'].split(': ', 1)[1]}**")

    # ---- S03 (C004, R3C04): the pilot ages in the Q19 note
    rep("and uses the ages the brief already names: P11 and P14; knockout feasible ages are bounded above by the earlier of the two documented death statements. A third later age depends on the laboratory's colony survival.",
        "and the pilot's candidate assay ages are two ages chosen by the laboratory inside the working window P12 to P17 (one near each end, from its colony's survival and the age at which knockout vehicle pups reliably seize); P11 and P14 are named in the brief only as chloride-window ages and enter the wild-type series only if that read is wanted; they are not the pilot assay ages. The pilot arithmetic (2 ages, 6 to 8 per cell) is unchanged. The window itself is an inference from documented ages: spontaneous seizures after P12 (Cheng 2020), ECoG spikes from about P14, slice bursting P13 to P17, death at about three to four weeks; the laboratory confirms from its colony. (This corrects the earlier answer, which took the pilot ages to be P11 and P14.)",
        "Note Q19, pilot ages")
    marker("R3C04", f"**OPEN-GAP S03 (owner laboratory): {rows['S03']['question_for_laboratory_or_operator'].split(': ', 1)[1]}**")

    # ---- S04: the status box
    rep("no number in this text is new. Each number appears as in the older texts;",
        "no number of the older texts was changed. Figures computed by the design team after the cold read (for example the doubled-vehicle total, the litter counts for wild-type supply, the inflation of the SD by one relative standard error, the pilot arithmetic) are labelled computed or inference where they stand; their derivations are in the design team's register of numeric tokens. Each number appears as in the older texts;",
        "Status box, sentence on numbers")

    # ---- S05: the Cheng regimen specifics in the Q15 note
    rep("The two Cheng regimens differ in schedule (lithium three injections within one hour; ethosuximide one injection 45 minutes before PTZ, both in saline, Methods), so a single vehicle group",
        "The replication condition is the regimen printed in the Methods of Cheng 2020 (agent, route, interval and number of injections are read there; this text copies none of its doses); only its differing schedules matter here: the two agents are given on different schedules, so a single vehicle group",
        "Note Q15, Cheng regimen specifics")

    # ---- S06: P5 and P8
    marker("Q84", note("S06", "C011/Q84",
                       "'P5' and 'P8' are labels of predictions in the in vivo priors file (P5: the lithium interaction ratio lies between 0.7 and 1.43; P8: at least one test or panel agent raises minimal-seizure incidence by at least 1.3 times vehicle while lowering generalised-seizure incidence); they are not postnatal days. A separate earlier priors file has its own P5 (a different prediction, the d-APV class), so every use in this text says 'of the in vivo priors file'. Where the text named a numbered line of an older text or 'set P5', it now names the section or the prediction's own words."))
    rep("as the predictions file defines \"generalised\" for P8", "as the in vivo priors file defines \"generalised\" for its prediction P8", "Table of seizure types, P8")
    rep("(as in the predictions file, E1, E3 and P5)", "(as in the in vivo priors file, E1, E3 and its prediction P5)", "Table of outcomes, P5")
    rep("(set P5 of the predictions file:", "(prediction P5 of the in vivo priors file:", "Condition for the development cohort, P5")

    # ---- S07: Cheng 2020 group sizes
    rep("Cheng 2020 used 6 to 7 knockout and 12 to 20 wild-type or heterozygous pups per group;",
        "In Cheng 2020 Fig. 7 the group sizes are printed in the figure legends as N: PTZ-alone knockout 6, knockout with ethosuximide 6, knockout with lithium 7 (6 to 7 knockouts per group); wild type and heterozygous groups 8 to 20 (7b: +/+ 20 and 16, +/- 18 and 12; 7d: +/+ 12 and 8, +/- 12 and 12); they are read from the figure legend, not stated in the Methods text;",
        "Planning, Cheng group sizes")
    rep("(n of 6 to 8 per cell is the Cheng 2020 scale)", "(6 to 8 per cell for the pilot is of the order of the Cheng knockout groups (6 to 7))", "Stage 1 row, Cheng scale")

    # ---- S08: grade and stage in the design-team notes
    sub_in_notes("area under the stage against time", "area under the grade against time", "S08 area under the stage")
    sub_in_notes("stage 6 IS death", "grade 6 IS death", "S08 stage 6")
    sub_in_notes("stage units", "grade units", "S08 stage units")
    sub_in_notes("stage-matched wild-type response", "wild-type response that is not at the floor", "S08 stage-matched response (notes)")
    rep("cannot be tested at a stage-matched wild-type response", "cannot be tested at a wild-type response that is not at the floor", "Stage 1 row, stage-matched response")

    # ---- S09: latency
    s9 = rows["S09"]["replacement_text"].replace("(V2 line 30: 60-minute window, grade per 1-minute bin as the maximum in the bin)", "(as in this text: 60-minute window, grade per 1-minute bin as the maximum in the bin)")
    assert "V2" not in s9
    s9 = s9.replace("Latency rule (INFERENCE, to be fixed before data):", "Latency rule (INFERENCE, to be fixed before data):")
    marker("Q51", note("S09", "Q51", s9, rows["S09"]["question_for_laboratory_or_operator"].split(": ", 1)[1]))

    # ---- S10: which stimulus governs which cell
    s10 = rows["S10"]
    marker("R3C01", note("S10", "R3C01", s10["replacement_text"].replace("State which stimulus governs which cell: ", "Which stimulus governs which cell: ", 1),
                         s10["question_for_laboratory_or_operator"].split(": ", 1)[1]))

    # ---- S11: E2
    s11 = rows["S11"]["replacement_text"].replace("The frozen in vivo priors already settle it:", "The frozen in vivo priors settle it:")
    s11 = re.sub(r"\s*\(My first draft.*?withdrawn\.\)", "", s11)
    assert "My first" not in s11
    marker("R3C05", note("S11", "R3C05", s11))
    rep("- (E2) age-limited, with a wild-type floor (", "- (E2) age-limited: a small wild-type drug effect at the assay age while wild-type vehicle S is above the pilot-fixed floor, not a floor-bound arm (", "Outcomes list, E2")
    rep("| Ethosuximide | R(+/+) null at the assay age, an effect at the older age (E2) | age-limited with a wild-type floor; the Cheng 2020 pattern is not knockout selectivity |",
        "| Ethosuximide | R(+/+) a null at the assay age and an effect at the older age, with the panel valid and wild-type vehicle S above the floor (E2); if wild-type vehicle S is at or below the floor, R(+/+) is not computed and the reading is E5 | an age-limited wild-type non-response, not a floor-bound arm; the Cheng 2020 pattern is not knockout selectivity |",
        "Outcomes table, E2 row")

    # ---- S12: 75 litters
    marker("R3C09", note("S12", "R3C09",
                         "The text's references to '75 litters' as a figure of the sections above are replaced by the current figures of the planning table: at the optimistic log SD 0.3 (not credible) three knockout arms need 19 litters (11 per arm) and one drug-by-genotype interaction 25 litters; at the credible scale three knockout arms need 62 to 187 litters (36 to 109 per arm). '75 litters' (3 x 44) is a superseded figure and stays in the History only."))
    rep("(19 and 53 litters; 75 litters; the dose-check totals) are the optimistic scale and should be read with the 36 to 109 bracket.",
        "(19 and 53 litters; 25 litters for one drug-by-genotype interaction; the dose-check totals) are the optimistic scale and should be read with the 36 to 109 bracket, at which three knockout arms need 62 to 187 litters.",
        "Planning scale paragraph, 75 litters")

    # ---- S13: unresolved panel age
    marker("R3C10", note("S13", "R3C10", rows["S13"]["replacement_text"].replace(" (V2 line 42: do not read the null)", " (do not read the null)"), rows["S13"]["question_for_laboratory_or_operator"].split(": ", 1)[1]))

    # ---- S02 and S14 at the R3Q37 marker (S02 first)
    s2 = rows["S02"]["replacement_text"].replace("State both totals in the sample-size section: ", "Both totals: ", 1).replace("(S01)", "(see the note on the age series)")
    assert "S01" not in s2
    s14 = rows["S14"]["replacement_text"].replace("A single figure cannot be fixed", "No single figure can be fixed", 1).replace("If one must be written, write a range with its basis, not one number:", "If one must be written, it is a range with its basis, not one number:", 1).replace("Say 'illustrative until the pilot gives the SD'.", "All of it is illustrative until the pilot gives the SD.")
    assert "Say " not in s14
    marker("R3Q37", note("S02", "C003", s2) + "\n\n" + note("S14", "R3Q37", s14, rows["S14"]["question_for_laboratory_or_operator"].split(": ", 1)[1]))

    # ---- History
    hist = ("\n### Markers and sentences replaced on 2026-11-21 (design-team group C)\n\n"
            "The lines below were the open markers, notes and sentences of this text before the design team's second set of answers was integrated; they are kept as they stood.\n\n" +
            "\n".join(f"- {lab}: {old}" for lab, old in removed) + "\n")
    k = t.index("\n## Out of scope for this laboratory")
    t = t[:k] + "\n" + hist + t[k:]
    print("unlisted tokens (in no column, no older text, not in the current text):", unlisted)
    left = [w for w in ("V2", "ADV", "SCI", "Held", "held ", " R0", "my ", "My ") if any(w in x for x in inserted)]
    print("leftover programme words in the body from the first inserted note on:", left)
    for lab, _ in removed:
        print("replaced:", lab)
    if unlisted:
        print("STOP: unlisted tokens")
        return 1
    if not dry:
        open(text_p, "w", encoding="utf-8").write(t)
    print("done" if not dry else "dry run, nothing written")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

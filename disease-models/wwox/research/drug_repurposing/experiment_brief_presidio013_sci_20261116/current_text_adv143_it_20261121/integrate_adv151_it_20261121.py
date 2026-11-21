"""ADV-151 integration (IT, 2026-11-21). Applies the design team's seven decisions D01 to D07
(REPLACEMENTS_FOR_IT_ADV151_SCI_20261121.tsv) to the current text, by script.
- Each named decision (OPEN-GAP C09, C30, C31, C35, R2C01, R2C09, R2C10) is replaced by the answer note, plus an OPEN-GAP marker for a laboratory question
  where the row has one; the old markers go to the History.
- The sentences the decisions change (stage 1 row, multiplicity bullet, threshold rows, outcomes row, cohort condition, order of hypotheses) are replaced in place;
  the old sentences go to the History.
- Two notes of D05 are NOT decided (the frozen priors file is silent): they become OPEN-GAP markers with their options, owner the design team with the laboratory,
  before data, as a pre-registration amendment. No deviation from the frozen file is adopted.
- Every numeric token of an inserted text must be in the row's numeric_tokens column, another row's column, the older texts or the current text (one extra: 1.4286, the reciprocal named in D05).
Usage: python3 integrate_adv151_it_20261121.py TEXT.md REPLACEMENTS.tsv OLD_A.md OLD_B.md [--dry-run]   (idempotent)"""
import csv
import re
import sys

TOK = re.compile(r"(?<![A-Za-z0-9.])\d+(?:[.,]\d+)?")
IDS = re.compile(r"\b(?:Q|C|T|E|L|R|P|S|M|H|N|D)\d{1,3}\b|\bQA\d\b|\bADV-\d+\b|\b\d{4}-\d{2}-\d{2}\b|\bPMID\s*\d+\b|\bFTR-[\w-]+\b")
EXTRA = {"1.4286"}
INF = "INFERENCE: a rule proposed by the design team, not a source value"


def toks(s):
    return set(TOK.findall(IDS.sub(" ", s)))


def main(a):
    dry = "--dry-run" in a
    a = [x for x in a if x != "--dry-run"]
    text_p, tsv_p, a_p, b_p = a[1:5]
    t = open(text_p, encoding="utf-8").read()
    if "Design-team answer D01" in t:
        print("already integrated")
        return 0
    rows = {r["repl_no"]: r for r in csv.DictReader(open(tsv_p, encoding="utf-8", newline=""), delimiter="\t")}
    allowed = toks(open(a_p, encoding="utf-8").read() + open(b_p, encoding="utf-8").read()) | toks(t) | EXTRA | set(x for r in rows.values() for x in r["numeric_tokens"].split(";") if x)
    removed, inserted, unlisted = [], [], []

    def check(s, label):
        miss = sorted(toks(s) - allowed)
        if miss:
            unlisted.append((label, miss))
        inserted.append(s)

    def rep(old, new, label):
        nonlocal t
        assert t.count(old) == 1, ("anchor", label, old[:80], t.count(old))
        check(new, label)
        t = t.replace(old, new)
        removed.append((f"Sentence ({label})", old))

    def marker(mid, new, label, kind="OPEN-GAP"):
        nonlocal t
        pat = re.compile(r"\*\*" + kind + " " + re.escape(mid) + r" \(owner \w+\):.*?\*\*", re.S)
        ms = pat.findall(t)
        assert len(ms) == 1, ("marker", mid, len(ms))
        removed.append(("Marker " + mid, ms[0]))
        check(new, label)
        t = pat.sub(lambda m: new, t, count=1)

    def note(rid, gid, body, status=INF):
        s = f"[Design-team answer {gid}, 2026-11-21; status: {status}. {body}]"
        check(s, rid)
        return s

    def lab(rid, q, owner="laboratory"):
        return f"\n\n**OPEN-GAP {rid} (owner {owner}): {q}**"

    def lq(rid):
        q = rows[rid]["question_for_laboratory_or_operator"]
        return q.split(": ", 1)[1]

    # ---- D01 (C09)
    d = rows["D01"]["replacement_text"]
    body = ("The pilot carries, at each of its two ages, knockout vehicle, wild-type vehicle and the wild-type flat-profile panel agent at ONE exposure (n 6 to 8 per cell; 36 to 48 animals, as already counted). "
            "The stage 1 row lists the panel cell, so its stop rule (\"the panel agent has no effect at any age\") can be read in stage 1. The dose check (\"if the lower exposure is effective in the panel agent at an age\") belongs to stage 2, where the panel agents are already run at two exposures; "
            "an age left unresolved in stage 1 is handled by the rule for an unresolved panel age (re-read at the second exposure in stage 2). Not adopted: vehicle pups only (it would move the pilot's stop rule out of stage 1) and the panel agent at two exposures in the pilot (it adds wild-type cells beyond the pilot note's count).")
    assert "ONE exposure" in d
    marker("C09", note("D01", "C09", body), "C09")
    rep("| 1 pilot | knockout and wild-type vehicle pups at candidate assay ages;",
        "| 1 pilot | knockout and wild-type vehicle pups and wild-type pups given the flat-profile panel agent at one exposure, at candidate assay ages;", "Stage 1 row, panel cell")

    # ---- D02 (C30)
    marker("C30", note("D02", "C30", rows["D02"]["replacement_text"]) + lab("D02", lq("D02")), "C30")

    # ---- D03 (C31) and Q57
    d3 = rows["D03"]["replacement_text"].replace("split into two add-ons with their own lists and ages (option 2)", "split into two add-ons with their own lists and ages").replace("The same answer settles the open question Q57 (one or two add-ons; serial in the same pups or separate cohorts):", "This also settles the open question on one or two add-ons and on serial or separate cohorts:")
    assert "Q57" not in d3 and "option" not in d3
    marker("C31", note("D03", "C31/Q57", d3) + lab("D03", lq("D03")), "C31")
    marker("Q57", "(see the design-team answer D03 above)", "Q57")

    # ---- D04 (C35) and Q70
    d4 = rows["D04"]["replacement_text"]
    m = re.search(r"Replace the multiplicity sentence by: '(.*?)' The earlier statement", d4, re.S)
    assert m
    bullet = m.group(1).replace("(D06)", "(see the primary comparison below)")
    tail = d4[m.end() - len("The earlier statement"):].strip()
    tail = tail.replace("as V2's cell total does", "as the cell total of the sample-size section does")
    assert "V2" not in tail and "D06" not in bullet
    old_b = re.search(r"- \*\*Shared vehicle and multiplicity\.\*\* .*", t).group(0)
    rep(old_b, "- **Shared vehicle and multiplicity.** " + bullet, "Multiplicity bullet")
    marker("C35", note("D04", "C35", tail), "C35")
    marker("Q70", "(see the design-team answer D04 above)", "Q70")

    # ---- D05 (R2C01): endpoints; two notes stay open
    d5 = ("The endpoints belong to the genotype-specific class, as the frozen priors file already has them (an effect is a ratio at most 0.7; E1 \"at most 0.7\"; E3 is rejected if the interaction ratio is \"at most 0.7 or at least 1.43\"). "
          "The no-specificity band of prediction P5 is therefore the open interval: an interaction ratio above 0.7 and below 1.43. Wherever this text restated the complement of that band as \"outside 0.7 to 1.43\", it now says \"at most 0.7 or at least 1.43\". No number changes; only the classification of a ratio of exactly 0.7 or 1.43 is fixed.")
    gap_a = ("**OPEN-GAP D05a (owner SCI): Is 1.43 kept as the upper edge of the no-specificity band although it is the rounded reciprocal of 0.7 (1/0.7 = 1.4286), so that a ratio between 1.4286 and 1.43 sits in the band while its reciprocal is below 0.7? Owner: the design team with the laboratory, before data, as a pre-registration amendment. Options: (1) keep the frozen band as it is; (2) amend before data to the exact reciprocal. The frozen priors file is not edited.**")
    gap_b = ("**OPEN-GAP D05b (owner SCI): Are the interaction thresholds (P5 and the classes E1 and E3) scored on the point ratio or on its interval? The frozen priors file is silent. Owner: the design team with the laboratory, before data, as a pre-registration amendment. Options: (1) class by the point ratio, with the point ratio and its interval both reported; (2) class by the interval (the class holds only if the whole interval lies in it). No deviation from the frozen file is adopted here.**")
    marker("R2C01", note("D05", "R2C01", d5) + "\n\n" + gap_a + "\n\n" + gap_b, "R2C01")
    rep("| no genotype specificity (interaction ratio) | 0.7 to 1.43 (as in the in vivo priors file, E1, E3 and its prediction P5) |",
        "| no genotype specificity (interaction ratio) | above 0.7 and below 1.43 (the open band of prediction P5 of the in vivo priors file) |", "Thresholds table, no-specificity row")
    rep("lithium effect in all genotypes (interaction between 0.7 and 1.43); second GSK-3 inhibitor effect;", "lithium effect in all genotypes (interaction above 0.7 and below 1.43); second GSK-3 inhibitor effect;", "Outcomes table, L1 row")
    rep("the row 'lithium effect in all genotypes (interaction 0.7 to 1.43); second GSK-3 inhibitor effect;", "the row 'lithium effect in all genotypes (interaction above 0.7 and below 1.43); second GSK-3 inhibitor effect;", "Note Q82, quoted row")
    rep("the point estimate of the interaction ratio lies in 0.7 to 1.43.", "the point estimate of the interaction ratio lies above 0.7 and below 1.43.", "Note Q73, band")

    # ---- D06 (R2C09)
    d6 = rows["D06"]["replacement_text"].replace("The single pre-specified primary is option (1): the knockout", "The single pre-specified primary is the knockout", 1)
    assert "option" not in d6
    marker("R2C09", note("D06", "R2C09", d6) + lab("D06", lq("D06")), "R2C09")
    rep("as descriptive ratios with their intervals; (iii)", "as descriptive ratios with their intervals (the primary, the knockout ratio at the assay age, is judged at 95%; every other ratio is descriptive); (iii)", "Order of hypotheses, (ii)")

    # ---- D07 (R2C10)
    d7 = rows["D07"]["replacement_text"].replace("Option (1): keep prediction P5 as written (two-sided; the priors file is frozen) and state what a smaller knockout effect means for the optional development cohort:", "Prediction P5 is kept as written (two-sided; the priors file is frozen). What a smaller knockout effect means for the optional development cohort:", 1)
    assert "Option" not in d7
    marker("R2C10", note("D07", "R2C10", d7), "R2C10")
    rep("(prediction P5 of the in vivo priors file: interaction outside 0.7 to 1.43, and the second GSK-3 inhibitor reproducing it while the non-GSK-3 comparator drug does not)",
        "(prediction P5 of the in vivo priors file rejected on the side of an interaction ratio at most 0.7, and the second GSK-3 inhibitor reproducing it while the non-GSK-3 comparator drug does not)", "Cohort condition")

    hist = ("\n### Decision markers and sentences replaced on 2026-11-21 (design-team decisions D01 to D07)\n\n"
            "The lines below were the named decisions and sentences of this text before the design team's seven decisions were integrated; they are kept as they stood.\n\n" +
            "\n".join(f"- {lab_}: {old}" for lab_, old in removed) + "\n")
    k = t.index("\n## Out of scope for this laboratory")
    t = t[:k] + "\n" + hist + t[k:]
    print("unlisted tokens:", unlisted)
    print("leftover programme words in inserted text:", [w for w in ("V2", "ADV", "Held", "held ", "D0", "R0") if any(w in x for x in inserted)])
    if unlisted:
        print("STOP")
        return 1
    if not dry:
        open(text_p, "w", encoding="utf-8").write(t)
    print("done" if not dry else "dry run")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

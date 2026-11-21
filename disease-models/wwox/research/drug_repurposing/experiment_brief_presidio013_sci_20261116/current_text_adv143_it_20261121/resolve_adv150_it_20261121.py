"""ADV-150 (IT, 2026-11-21): classification of the 13 conflicts that ADV-148 did not answer, applied by script.
(a) six are text-only repairs (the documents resolve them by scope or wording); each replaced sentence and each removed marker is kept in the History.
(b) seven are decisions for design science: the CONFLICT-OPEN marker becomes a named decision with the options of the documents (nothing is decided here).
No number is invented: every numeric token of an inserted text must be in the older texts or in the current text, except the two PMIDs listed in EXTRA
(both are in the design team's regimen table, advisor_pilot_20261113/brainstorm_20261116/adv067_lithium_regimen_sci_20261118/).
Usage: python3 resolve_adv150_it_20261121.py TEXT.md OLD_A.md OLD_B.md [--dry-run]   (idempotent)"""
import re
import sys

TOK = re.compile(r"(?<![A-Za-z0-9.])\d+(?:[.,]\d+)?")
IDS = re.compile(r"\b(?:Q|C|T|E|L|R|P|S|M|H|N)\d{1,3}\b|\bQA\d\b|\bADV-\d+\b|\b\d{4}-\d{2}-\d{2}\b|\bPMID\s*\d+\b|\bFTR-[\w-]+\b")
EXTRA = {"31238129", "29102713"}


def toks(s):
    return set(TOK.findall(IDS.sub(" ", s)))


def main(a):
    dry = "--dry-run" in a
    a = [x for x in a if x != "--dry-run"]
    text_p, a_p, b_p = a[1:4]
    t = open(text_p, encoding="utf-8").read()
    if "Conflict markers and sentences replaced on 2026-11-21" in t:
        print("already applied")
        return 0
    allowed = toks(open(a_p, encoding="utf-8").read() + open(b_p, encoding="utf-8").read()) | toks(t) | EXTRA
    removed = []
    inserted = []
    unlisted = []

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

    def marker(mid, new, label):
        nonlocal t
        pat = re.compile(r"\*\*CONFLICT-OPEN " + re.escape(mid) + r" \(owner \w+\):.*?\*\*", re.S)
        ms = pat.findall(t)
        assert len(ms) == 1, ("marker", mid, len(ms))
        removed.append((f"Marker {mid}", ms[0]))
        if new:
            check(new, label)
        t = pat.sub(lambda m: new, t, count=1) if new else pat.sub("", t, count=1)

    # ---------------- (a) text-only repairs ----------------
    # C23: the two quantities differ
    rep("wild-type grade is about 1 on 0 to 6, close to the floor, that is, so low that a reduction cannot be seen)",
        "wild-type grade is about 1 on 0 to 6, close to the floor, that is, so low that a reduction cannot be seen; \"about 1\" is an eye reading of the published curves, and the older texts do not say whether it is a peak value or a mean; it is not the 60-minute mean grade of the floor bracket used below (mean S 0.27 to 0.41 in grade units), which is a different quantity and is not to be compared with it)",
        "C23, wild-type grade about 1")
    marker("C23", "", "C23")
    # C03: the same abstract is named in both sentences
    rep("The design team's literature table holds acute pro-convulsant and chronic threshold-raising results in one mouse PTZ paper family.",
        "The pro-convulsant abstract is the same one: in that report (PMID 29102713, abstract level, male mice by its record) the acute arm was pro-convulsive and the chronic arm raised the threshold; the interval and the PTZ method of the acute arm are not stated and the full text is closed, which is why it is not counted as a clear sign flip.",
        "C03, one family")
    marker("C03", "", "C03")
    # C02: the second regimen is a literature schedule, not a schedule of our own
    rep("A second regimen is an optional comparator arm (a single injection, PTZ about 30 minutes later), not a design variable of the main contrast.",
        "A second regimen is an optional comparator arm (a single injection, PTZ about 30 minutes later: the schedule of one published mouse report, PMID 31238129, read at abstract level, not a schedule of our own), not a design variable of the main contrast.",
        "C02, second regimen")
    marker("C02", "", "C02")
    # C16: the sentence pointed to a value neither text states
    rep("This brief carries only the heterozygote bursting incidence.",
        "This text carries no heterozygote bursting incidence: an earlier sentence said it carried only that value, and no such value is stated in either of the older texts.",
        "C16, heterozygote bursting incidence")
    marker("C16", "", "C16")
    # R2C05: grade 4 and the tonic phase
    marker("R2C05",
           "[Text repair 2026-11-21 conflict R2C05: a grade 4 counts as generalised only if a tonic phase is seen; a grade 4 without one does not count as generalised and has its own line; a grade 5 is a generalised tonic-clonic seizure in the printed scale of Cheng 2020 (see the note on the scale) and counts.]",
           "R2C05")
    # C32: GFAP and Iba1 scoring is not planned in the provoked assay
    marker("C32",
           "[Text repair 2026-11-21 conflict C32: no GFAP or Iba1 scoring is planned in the provoked assay; GFAP scoring appears only in the optional development cohort. The words \"alongside any GFAP and Iba1 scoring at P5 to P9\" in the add-on (e2) therefore apply only if the laboratory adds such scoring or runs that cohort; the measures of the add-on and the ages P7, P9, P11 and P14 are as listed there.]",
           "C32")

    # ---------------- (b) decisions for design science ----------------
    D = {
        "C09": "DECISION (design science): which pups the pilot carries. The pilot note gives two ages of knockout vehicle, wild-type vehicle and the flat-profile panel agent at one exposure (36 to 48 animals); the stage 1 row lists vehicle pups only; the pilot's stop rule needs the panel agent; the dose-check decision (\"if the lower exposure is effective in the panel agent at an age\") needs the panel agent at two exposures. Options in the documents: (1) the panel agent at one exposure in the pilot, and the dose check in stage 2; (2) the panel agent at two exposures in the pilot (more wild-type cells than the pilot note counts); (3) vehicle pups only, as the stage 1 row says, with the panel stop rule and the dose check moved to stage 2.",
        "C30": "DECISION (design science): whether the add-on (e2) also measures parathyroid hormone and lipids. The human-side line (e4) says that neither is named in any human report read and that this strengthens the add-on measurement; the list of (e2) is serum total calcium with albumin (or ionised calcium), glucose, body weight and a milk-spot score. Options: (1) add parathyroid hormone and a lipid measure to (e2), with the blood volume of a P7 pup addressed (the open question on the add-ons); (2) keep the list of (e2) as written and read (e4) as context only.",
        "C31": "DECISION (design science): whether the glucose series (e) and the calcium add-on (e2) are one add-on or two. (e) lists glucose, ketone and lactate by age, and milk intake or stomach filling, at P7 to P14; (e2) lists serum total calcium with albumin (or ionised calcium), glucose, body weight and a milk-spot score at P7, P9, P11 and P14. Options: (1) one combined add-on with the union of the lists at P7, P9, P11 and P14; (2) two add-ons, each with its own list and ages, with glucose and the feeding read taken once. This is the same decision as the open question on serial or separate cohorts.",
        "C35": "DECISION (design science): how many comparisons the multiplicity statement counts. It counts five test arms sharing one vehicle group per genotype (95% and 99%, Bonferroni for five; vehicle about twice a test arm). The text later adds a lithium-alone arm, an optional second regimen, the optional T-type arm, a second GSK-3 inhibitor, a comparator drug and panel agents at two exposures each. Options: (1) keep five and treat every added arm as outside the family (exploratory, reported at 95% only); (2) recount the family over the arms that share a vehicle group in a session, and state the count and the Bonferroni divisor before data.",
        "R2C01": "DECISION (design science): the boundary rule for an interaction ratio of exactly 0.7 or 1.43. The thresholds table says \"genotype specificity: at most 0.7 or at least 1.43\" and \"no genotype specificity: 0.7 to 1.43\"; prediction P5 of the in vivo priors file and the cohort condition say \"outside 0.7 to 1.43\" (the endpoints inside the null band). Options: (1) the endpoints belong to the specificity class (as \"at most\" and \"at least\"); (2) the endpoints belong to the no-specificity band (as \"outside 0.7 to 1.43\").",
        "R2C09": "DECISION (design science): which comparison is the single pre-specified primary. One passage says the ethosuximide comparison is the pre-specified primary, judged at 95%; the order of hypotheses lists the ethosuximide effect ratios in the knockout and in the wild type, at the assay age and at the older ages, as descriptive ratios with their intervals, and the interaction as exploratory unless sized. Options (readings of those lists): (1) the knockout ethosuximide ratio at the assay age is the primary, judged at 95%, and every other ratio is descriptive; (2) the knockout and wild-type ratios at the assay age are the primary, the older ages descriptive; (3) no comparison is a confirmatory primary: all ratios are descriptive and the multiplicity statement says so.",
        "R2C10": "DECISION (design science): whether the condition for the optional development cohort is one-sided. As written it is \"interaction outside 0.7 to 1.43\" (prediction P5 of the in vivo priors file), which admits a larger knockout effect (ratio at most 0.7) and a smaller one (ratio at least 1.43); the outcomes table calls only the larger one knockout-enhanced. Options: (1) keep P5 as written (two-sided; the priors file is frozen) and state what a smaller knockout effect means for the cohort; (2) make the cohort condition one-sided (ratio at most 0.7, reproduced by the second GSK-3 inhibitor of another class) and say that P5 is then wider than the condition.",
    }
    for k, v in D.items():
        marker(k, f"**OPEN-GAP {k} (owner SCI): {v}**", k)

    hist = ("\n### Conflict markers and sentences replaced on 2026-11-21 (classification of the 13 open conflicts)\n\n"
            "The lines below were the conflict markers and sentences of this text before the 13 conflicts left open by the design team's second set of answers were classified: six were repaired in the text, seven became named decisions. They are kept as they stood.\n\n" +
            "\n".join(f"- {lab}: {old}" for lab, old in removed) + "\n")
    k = t.index("\n## Out of scope for this laboratory")
    t = t[:k] + "\n" + hist + t[k:]
    print("unlisted tokens:", unlisted)
    print("leftover programme words in inserted text:", [w for w in ("V2", "Held", "held ") if any(w in x for x in inserted)])
    if unlisted:
        print("STOP")
        return 1
    if not dry:
        open(text_p, "w", encoding="utf-8").write(t)
    print("done" if not dry else "dry run")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

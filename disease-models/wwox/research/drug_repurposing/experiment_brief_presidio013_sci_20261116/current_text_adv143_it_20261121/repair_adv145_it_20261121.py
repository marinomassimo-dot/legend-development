"""ADV-145 repair after the round-2 cold read (IT, 2026-11-21). Idempotent. Run from this folder.
Edits PUP_BRIEF_CURRENT_IT_20261121.md only: (1) two sentences where the fold-in introduced an error, restored
to the wording of the older text; (2) markers for gaps and conflicts the round-2 reader found unmarked. No number is
added: every numeric token is one the older texts carry (check_current_text.py is rerun after)."""
from pathlib import Path

P = Path(__file__).resolve().parent / "PUP_BRIEF_CURRENT_IT_20261121.md"
t = P.read_text(encoding="utf-8")
if "R2C01" in t:
    raise SystemExit("already applied")


def rep(old, new):
    global t
    assert t.count(old) == 1, ("anchor not unique or absent", old[:70], t.count(old))
    t = t.replace(old, new)


def after_line(substr, text, after_table=False):
    global t
    lines = t.split("\n")
    idx = [i for i, l in enumerate(lines) if substr in l]
    assert len(idx) == 1, ("anchor not unique or absent", substr[:70], len(idx))
    i = idx[0]
    if after_table:
        while i + 1 < len(lines) and lines[i + 1].startswith("|"):
            i += 1
    lines[i + 1:i + 1] = ["", text]
    t = "\n".join(lines)


# (1) repairs of fold-in errors (the older wording is restored)
rep("The litter and animal totals at 11 per cell (19 and 53 litters; the dose-check totals) are the optimistic scale",
    "The litter and animal totals of the sections above (19 and 53 litters; 75 litters; the dose-check totals) are the optimistic scale")
rep("against 11.4 to 71.5 and 9.2 to 56.9 in the quantification above)",
    "against 11.4 to 71.5 and 9.2 to 56.9 for the first reading, whose values are given only here)")

# (2) conflicts the round-2 reader found unmarked (inherited from the older texts; both statements stay)
after_line("| no genotype specificity (interaction ratio) | 0.7 to 1.43",
           "**CONFLICT-OPEN R2C01 (owner SCI): The values 0.7 and 1.43 belong to both classes of the thresholds table (genotype specificity: at most 0.7 or at least 1.43; no genotype specificity: 0.7 to 1.43), so a ratio of exactly 0.7 or 1.43 is not classified.**",
           after_table=True)
after_line("generalised seizures (**grades 4 to 5 with a tonic phase",
           "**CONFLICT-OPEN R2C05 (owner SCI): Grade 4 is described without a tonic phase while generalised seizures are grades 4 to 5 with a tonic phase; which grade 4 counts as generalised is not stated.**")
after_line("as descriptive ratios with their intervals",
           "**CONFLICT-OPEN R2C09 (owner SCI): The ethosuximide comparison is listed as primary in one place and as descriptive ratios with intervals in another; whether it is tested at the stated confidence level is not stated.**")
after_line("interaction outside 0.7 to 1.43, and the second GSK-3 inhibitor",
           "**CONFLICT-OPEN R2C10 (owner SCI): The condition for the optional cohort, an interaction outside 0.7 to 1.43, also admits a smaller knockout effect, which the outcomes table does not call knockout-enhanced.**")

# (3) gaps the round-2 reader found unmarked
after_line("- **Cluster and sex.**",
           "**OPEN-GAP R2Q16 (owner laboratory): Is sex balanced or stratified across arms, and are both sexes used?**")
after_line("- **Blinding.**",
           "**OPEN-GAP R2Q81 (owner laboratory): Is scorer training or inter-scorer agreement required, and how many scorers are assumed?**")
after_line("| 3 lithium (optional) | lithium against vehicle in all genotypes **in the same session**",
           "**OPEN-GAP R2Q43 (owner SCI): For stage 3, in the same session as what, and at the assay age only or across the whole age series?**")
after_line("- **(c) A Cav3 transcript or protein readout**",
           "**OPEN-GAP R2Q80 (owner SCI): Which Cav3 transcript or protein readout, region and age is meant by add-on (c)?**")
after_line("- **(e3) Inhibitory currents and phospho-ErbB4**",
           "**OPEN-GAP R2Q79 (owner SCI): How are the inhibitory currents and phospho-ErbB4 to be measured (region, age, method, tissue plan) in animals of the same cohort as the calcium and serum add-on?**")
after_line("Predictions for the outcome classes were fixed in a predictions file",
           "**OPEN-GAP R2Q82 (owner operator): Does the laboratory receive the older texts, the operator note and the predictions file, and where are they kept?**")

# (4) two plain notes in the History introduction (no gap: a reading aid)
rep("The older texts themselves are also kept unchanged in the repository.",
    "The older texts themselves are also kept unchanged in the repository. Some quoted lines stop in the middle of a sentence on purpose: each is one verbatim passage of an older text, cut where the superseded statement ends. Names such as ADV, IT, HE and SCI in the quoted lines are roles of the design team and its coordinators in the older texts, kept as written. Repair of 2026-11-21 after the second cold read: two sentences of the Sample size section were restored to the wording of the older texts (the litter totals and the first reading's SD values), and four conflicts and six gaps that the second reader found unmarked received markers, all labelled R2 (the other two of its unmarked questions are answered by the two notes in this paragraph).")
P.write_text(t, encoding="utf-8")
print("applied")

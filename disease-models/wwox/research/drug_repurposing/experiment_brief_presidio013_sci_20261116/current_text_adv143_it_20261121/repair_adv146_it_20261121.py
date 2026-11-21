"""Round-3 cold read repair (IT, 2026-11-21). Idempotent. Run from this folder.
Edits PUP_BRIEF_CURRENT_IT_20261121.md: (1) the status box says what the bracketed design-team notes are, that their figures carry their own status,
how 'stage' in a quoted note relates to 'grade', and what a body reference to an older numbered line is; (2) one marker moved out of a table;
(3) markers for conflicts that the integration of the design team's answers placed next to older sentences, and for one gap, which the round-3 reader
found unmarked. No number is added; every number in a new marker is one the text already carries."""
from pathlib import Path

P = Path(__file__).resolve().parent / "PUP_BRIEF_CURRENT_IT_20261121.md"
t = P.read_text(encoding="utf-8")
if "R3C01" in t:
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


# (1) status box
rep("- No number in this text is new. Each number appears as in the older texts;",
    "- Design-team notes. The bracketed notes \"[Design-team answer ...; status: ...]\" are the design team's answers of 2026-11-21 to the open questions of the earlier readings. The status after the semicolon says what a note is: computed from stated inputs; stated in a source text; confirmed or corrected; INFERENCE (a rule proposed by the design team, not a source value); or partly closed (the rest is a marked open item). A note is later and more specific than the sentence beside it: where they differ, follow the note; the sentence stays, and where both cannot hold a CONFLICT-OPEN marker says so.\n- Apart from the design-team notes (each figure in a note carries the status that its note states), no number in this text is new. Each number appears as in the older texts;")
rep("\"stage\" always means a step of the experimental plan (stages 0 to 4).",
    "\"stage\" always means a step of the experimental plan (stages 0 to 4). The design-team notes quote source papers that also say \"stage\" for a step of the seizure scale (\"stage 6 is death\"); in a note, a \"stage\" with a seizure meaning is a grade, and \"stage units\" are grade units. A reference in the body to a numbered line of an older text (for example \"line 9.14\") or to a set of the predictions file points to a text kept in the repository, not to a section of this one.")

# (2) the stage-3 marker was inserted inside the stage table; it moves to below the table
mk = "**OPEN-GAP R2Q43 (owner SCI): For stage 3, in the same session as what, and at the assay age only or across the whole age series?**"
assert t.count("\n\n" + mk) == 1
t = t.replace("\n\n" + mk, "", 1)
after_line("| 3 lithium (optional) | lithium against vehicle in all genotypes **in the same session**", mk, after_table=True)

# (3) markers
after_line("| wild-type and heterozygous pups at that published stimulus",
           "**CONFLICT-OPEN R3C01 (owner SCI): The replication condition is the published low-dose stimulus, at which wild type sat near the floor, while a stimulus with a non-floor wild-type response is required for the contrast; the text does not say which wins.**",
           after_table=True)
after_line("[Design-team answer CLAR-SERIES, 2026-11-21;",
           "**CONFLICT-OPEN R3C02 (owner SCI): The note above adds P11 as a further series age when the assay age is P14 or later, while the rule sentence in Ages says the straddle of P11 and P14 is not a further requirement; the rule sentence was not changed.**")
after_line("[Design-team answer Q19, 2026-11-21;",
           "**CONFLICT-OPEN R3C04 (owner SCI): The note above takes the pilot ages to be P11 and P14, while another note takes the working window to be P12 to P17 with P11 only as the chloride-window probe; the pilot ages are not fixed.**")
after_line("[Design-team answer Q67, 2026-11-21;",
           "**CONFLICT-OPEN R3C10 (owner SCI): A panel that fails is an assay failure, but the rule above also leaves an age unresolved when the flat-profile agent gives neither a null nor an effect; what is done with an unresolved panel age is not stated.**")
after_line("| Ethosuximide | R(+/+) null at the assay age, an effect at the older age (E2)",
           "**CONFLICT-OPEN R3C05 (owner SCI): Outcome E2 is defined by a wild-type floor, while the floor rule says R is not computed and the arm is not interpretable at the floor.**",
           after_table=True)
after_line("The litter and animal totals of the sections above (19 and 53 litters; 75 litters;",
           "**CONFLICT-OPEN R3C09 (owner SCI): The sentence above cites 75 litters as a figure of the sections above, but the sample-size table carries 75 only as a derived figure (3 x 44) and, in the History, as a superseded one.**")
after_line("| planning total for the required stages with the dose check",
           "**OPEN-GAP R3Q37 (owner SCI): Which single figure of animals and litters is to go into an application, given the planning totals of this section?**",
           after_table=True)
P.write_text(t, encoding="utf-8")
print("applied")

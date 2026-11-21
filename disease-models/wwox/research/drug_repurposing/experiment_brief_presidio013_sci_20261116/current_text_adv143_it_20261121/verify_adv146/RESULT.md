# Cold read, round 3 - can a laboratory work from this text without a call?

Source: DOCUMENT_CURRENT_pup_brief.md only (read completely, 692 lines). Settings stated for this read: model sonnet, effort high.

**(A) Can the laboratory start without a call?** Only with named gaps closed. QUESTIONS.tsv holds 86 questions; I mark 16 as blocking a start (Q001, Q002, Q007, Q008, Q015, Q016, Q017, Q020, Q022, Q025, Q026, Q037, Q038, Q039, Q046, Q047). "Blocking" here means an answer that only the document's owners can give, or an internal contradiction that changes what I would run, before the stage 1 pilot can be run or the whole plan accepted. The other 70 are decisions or facts that belong to my own laboratory (colony, ethics, standards, staffing) or concern optional arms and add-ons; they are marked "no" with the reason. Several lab-internal items (document marker ids: Q42 line, Q22 supply, Q61 status procedure) are also go/no-go for me, but I can answer them without a call. I could prepare the pilot and the ethics application from the document, but not execute the required ethosuximide arm: the replication doses are not in the text and the open items owned by "SCI" or "operator" have no route to an answer (no contact is named).

**(B) UNAIDED: which text governs, what it replaces, where the earlier lines went.**
- Governs: "STATUS: THIS TEXT GOVERNS. Version and date: 2026-11-21." and "This is the one current text of this experiment brief."
- Replaces: "It replaces, for reading, the two older texts: the consolidated brief dated 2026-11-19 and the original brief dated 2026-11-18 with the dated lines appended to it (the last dated 2026-11-21)." Rule of precedence: "Where this text and an older text differ, this text is the one to follow."
- Where the earlier statements went: "Every statement that this text supersedes is kept, word for word, in the section 'History (old text kept)' at the end, with its date and the statement that replaced it." The older texts themselves: "kept unchanged in the repository" (not available to me). The History also says "Some quoted lines stop in the middle of a sentence on purpose" and that some dated lines were "dropped, the body carries them". The operator-facing content "is kept in a separate operator note and is not in this text" (not available to me).
- What the document does not say: it does not define the bracketed "[Design-team answer ...; status: ...]" notes (39 of them), although they carry many operative rules; it says the predictions file "governs any conflict" on definitions while the status box says this text governs (see C019); it does not say that the History is a complete list of what changed.

**(C) The ten items that would most block a start, ranked**
1. Q001 - status of the "[Design-team answer ...]" notes: many rules I would execute (same injection schedule for every pup, panel validity rule, floor threshold, stimulus rule, grade 6 = death) exist only in them, and the status box does not define them.
2. Q007 and Q002 - no contact route, and the predictions file that "governs any conflict" may not be sent; about 40 open items are owned by SCI or operator and cannot be closed without asking.
3. Q016 - the replication condition (Cheng's low-dose PTZ, wild type near the floor) conflicts with the requirement of a non-floor wild-type stimulus (C001); I cannot tell which wins.
4. Q015, Q017 (and Q018 for lithium) - PTZ, ethosuximide and lithium doses and volumes are not in the document; it points to a paper I do not hold.
5. Q046 and Q047 - pilot ages (P11 and P14, or P12 to P17) and the number of wild-type series ages (three or four) disagree (C002 to C004); the cell count and animal totals change.
6. Q037 and Q038 - no single animal and litter figure to apply for (about 300, 354, 1,350; 36 to 109 per knockout arm, 60 to 181 after pilot) and no rule for the smallest informative stage 2 if knockouts are scarce.
7. Q039 - wild-type source: the body says wild-type animals "are not limiting", the note says 132 versus 33 litters depending on breeding; littermate control undecided.
8. Q022 and Q020 - whether every pup gets the same number of injections (shared vehicle) and what "two exposures per agent" means; both fix the vehicle design and cell count.
9. Q025 and Q026 - how three tonic-clonic seizures are counted (the status and rescue trigger) and which grade 4 counts as generalised.
10. Q008 - funding, data ownership, authorship and agreement are not offered.

**(D) Conflicts between sections not marked by the document as conflicts** (details in CONFLICTS.tsv, no CONFLICT-OPEN line covers them)
- C001 replication stimulus (low-dose PTZ, wild type near floor) vs required non-floor wild-type stimulus.
- C002 age series "straddling P11 and P14 is not a further requirement" vs "P11 ... is added as a further age".
- C004 pilot ages P11 and P14 vs working window P12 to P17.
- C005 outcome E2 defined by a wild-type floor vs the floor rule (R not computed) and the table header "wild type above floor".
- C007 "No number in this text is new" vs computed new numbers in notes (354, 132, 33, 60, 181).
- C008 no-number policy vs the 45 minutes given in a note while no doses are given.
- C009 "75 litters" cited as a figure of the sections above; it only exists as a superseded figure.
- C010 panel states: "a panel that fails is an assay failure" vs "invalid when ... a null, unresolved otherwise".
- C011 status box "Sections are named, not numbered" vs "line 9.14 ... 9.16" and "set P5" in the body.
- C012 group sizes of Cheng: 6 to 8, 6 to 7, N = 6.
- C013 "stage" defined as a plan step, then used for seizure scale steps in notes.
Partly marked, so not fully unmarked: C003 (21 wild-type cells assume three ages while the working window implies four), C014 (36 to 109 vs 60 to 181 per arm), C015 (two definitions of "general"), C016 ("none changes ... a size" vs add-on burden).
Resolved inside the document by a note, though the text above it was not edited: C006 (grade table vs Q18 note), C017 ("twice" vs 180 to 320, answer C06), C018 (about 300 vs about 354, answers C08/Q32), C019 (this text governs vs predictions file governs, answer Q06).

**Marked by the document (listed separately, CONFLICTS.tsv C020 to C036):** CONFLICT-OPEN C23, R2C05, C09, C03, C02, R2C01, R2C09, C35, C31, C32, C30, C16, R2C10 (13 in the body), plus OPEN-GAP Q81, OPEN-GAP C25/Q45 and History CONFLICT-OPEN C18 and C17.

Files: QUESTIONS.tsv (86), CONFLICTS.tsv (36), TERMS.tsv (31), SEARCH_NOTES.md, all in this folder.

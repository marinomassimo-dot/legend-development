# RESULT: cold reading (round 2) of the current pup brief

Source: only DOCUMENT_CURRENT_pup_brief.md. "Start" means beginning the first step the text describes (the stage 1 pilot) and being able to commit to the experiment. A question is marked blocking if it stops that.

**(A) Can the laboratory start without a call?** Only with named gaps closed. QUESTIONS.tsv has 84 questions; 15 are marked as blocking a start (q01, q02, q03, q08, q09, q17, q19, q20, q21, q32, q35, q37, q59, q62, q63), and the other 69 do not block the pilot (several block stage 2 or 3 or the optional parts). The document itself carries 72 OPEN-GAP markers (all 72 are mapped to a row) and 14 CONFLICT-OPEN markers; 11 of my 84 questions have no marker of the document (nearest_marker "none") and two more are only partly covered (Q84 for P5 and P8, Q51 for latency but not the window start). The most serious point is that the document names no contact, no terms and no line or allele, so a laboratory cannot close any other gap without a call.

**(B) UNAIDED: which text governs and what it replaces.** The document says: "STATUS: THIS TEXT GOVERNS. Version and date: 2026-11-21." and "This is the one current text of this experiment brief. It replaces, for reading, the two older texts: the consolidated brief dated 2026-11-19 and the original brief dated 2026-11-18 with the dated lines appended to it (the last dated 2026-11-21)." Where texts differ: "Where this text and an older text differ, this text is the one to follow." Where the earlier statements went: "Every statement that this text supersedes is kept, word for word, in the section 'History (old text kept)' at the end, with its date and the statement that replaced it." Dated lines that changed nothing are listed in the History section "Dated lines folded without a superseded statement, with their dates" (lines 9.1 to 9.17, each with where it was folded); the gene-addition lines 9.14 to 9.16 are in "Out of scope for this laboratory" and the History entry above it; the two different "9.12" lines are named apart in the History. Operator-facing content: "The operator-facing content is kept in a separate operator note and is not in this text." The document does not say: where the operator note, the older texts ("kept unchanged in the repository") or the predictions file can be obtained, or whether the laboratory is allowed to see them; and whether the History is complete (several quoted lines end mid-sentence). One gap in the statement of precedence: the Scope says "the predictions file governs any conflict" with this text, so the status box is not the last word.

**(C) The ten items that would most block a start, ranked.**
1. No contact route, no funding, data ownership, credit or authorship terms, no deliverables (Q75, Q74, Q76).
2. The mouse line: allele, background and source are unnamed, and whether the laboratory can obtain the global knockout is "open" (Q42); the wild-type source and breeding plan are also not stated (Q45, Q80, C25).
3. The provoking stimulus and the scale: PTZ is anchored for lithium but the stimulus is also the laboratory's choice; grades 0, 1, 2 and 6 are undefined; grade 4 is described both without and with a tonic phase (Q12, QA3, Q18).
4. The predictions file is said to govern conflicts and to define "generalised" and sets "P5"/"P8", but it is only cited by checksum (Q06, Q84).
5. The pilot is not defined: which ages, whether the panel agent is in it (its own stop rule needs it), how many animals and litters (Q19, Q37, Q34, Q23, C09).
6. Welfare: a status stopping rule "written before the first animal" is required, but the trigger, rescue procedure, whether death is accepted, and the expected death rate are missing (Q61, Q62, Q52).
7. Genotyping before the test and allocation: method, age, turnaround and the allocation rule for about 1.75 knockouts per litter (Q43, Q46, Q44).
8. The required stage 2: the ethosuximide regimen, what "two exposures per agent" means, and whether one shared vehicle is valid (Q14, Q16, Q15).
9. No single n per cell or breeding figure: 11, 22, 31, 36 to 109, 44, 50, 180 to 320 are stated on different bases; the planning, vehicle-size and multiplicity statements disagree (Q31, Q32, Q33, C06, C08, C35, Q70).
10. The primary outcome and analysis rules: S units and primary summary, latency and window start, the numerical rules for "floor" and for panel validity, the boundary of the interaction thresholds (Q49, Q50, Q51, Q22, Q68, Q67).

**(D) Conflicts between sections that the document does not itself mark.** Seventeen are in CONFLICTS.tsv (c01 to c17); the column flagged_in_document says where a marker only partly covers one. In short:
- c01 thresholds: interaction ratio "at most 0.7 or at least 1.43" is specific; "0.7 to 1.43" is not specific; the end values are in both.
- c02 E2 is "age-limited with a wild-type floor", but the table requires "wild type above floor" and the floor rule makes a floor arm "not interpretable".
- c03 the status stopping rule is "fixed" in one list, written and decided by the laboratory in others (Q61 asks only for its content).
- c04 doses, route and stimulus are "decided by the laboratory" while Q14 and Q12 ask the design team for them.
- c05 grade 4 is "without a tonic phase" but generalised is "4 to 5 with a tonic phase".
- c06 "19 and 53 litters" are said to be "at 11 per cell"; 53 belongs to 31 per arm.
- c07 the base design "cannot show how a drug works", but the title promises a GSK-3 reading (partly covered: "needs the add-on").
- c08 stage 2 is "the only arm whose outcome decides between selective, age-limited or general" while the genotype contrast that separates them is "not attemptable" (partly Q73).
- c09 the ethosuximide comparison is "primary" and also "descriptive ratios".
- c10 the cohort condition "interaction outside 0.7 to 1.43" accepts a smaller knockout effect, not only knockout-enhanced.
- c11 Cheng group sizes: 6 to 7 knockout (sample size) against "6 to 8 per cell is the Cheng 2020 scale" (stage 1).
- c12 death ages: four weeks, three to four weeks, day 17 (flagged by Q37).
- c13 "P5" is a prediction set in one place and postnatal day 5 in add-on e2 (partly Q84).
- c14 SD figures said to be "in the quantification above" are not there.
- c15 Q33 cites 75 litters, a figure only in the History.
- c16 the Scope ("predictions file governs any conflict") and the status box ("this text is the one to follow") answer differently (flagged by Q06).
- c17 the body quotes old line numbers (9.14 to 9.16) although the box says references are by name; no effect on execution.

**Marked by the document (not counted above), by id:** C23 (wild-type grade about 1 against S of 0.27 to 0.41); C09 (stage 1 row lists vehicle pups only but its stop rule needs the panel agent); C03 (regimen sign flip); C02 (second lithium regimen); C35 (multiplicity counts five comparisons); C25 (wild-type and heterozygous animals "not limiting"); C06 (twice the simple-effect number against the stated 180 to 320 per cell; I checked: twice 36 to 109 gives 72 to 218, so this one is a true arithmetic mismatch); C08 (vehicle twice a test arm against equal n); C31 (glucose series against calcium add-on); C32 (GFAP and Iba1 scoring not planned); C30 (parathyroid hormone and lipid not in the add-on list); C16 (heterozygote bursting incidence absent); C18 (what changed between original and consolidated text); C17 (two texts both numbered 9.12).

I checked the arithmetic of the sample-size table (simple effect 11, 31, 79 for SD 0.3, 0.5, 0.8; 22 per cell; 27 cells; 33 to 150 knockouts; 62 to 187 litters) and found it consistent with its stated inputs, except the marked C06.

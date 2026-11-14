# IT52 result: SCI47 levers L1 and L2 read by the generator through declared keys (revision ba0283130)

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Nothing here nominates a compound or changes a ranking, sign or need. Targeted check of one known limit, not a benchmark. Criteria: `prereg_it52.md` (fixed before HE's change). Independent reader: `verify/READER_REPORT.md` (sonnet, effort high read back x18 by `session_model_census.py`; 18 turns; output 43,085 tokens; cache written 132,685; cache read 1,254,144; the reader's own sentence "effort low" is its self-report and is contradicted by the census). Cost apart from mine.

## What moved / what could not be held
Moved: generator revision (6d6fabf88 -> ba0283130) with one manifest row (`inhibitory_defect_sci47_20261112`, hypotheses_only, INV-05), levers.tsv accepted as a table, six rows CP-inhibitory_defect_sci47_20261112::L1..L6 and the column `design_join`. The PKG_MAP is HE's draft, not confirmed by the owners. Held: levers.tsv, ADV-006 tables, criteria.

## Against the criteria
| Criterion | Result |
|---|---|
| (a) rows for L1, L2 carrying the lever's own status, risk, counter-evidence, rejection result; L3, L6 as dropped | met for L1, L2 (every BEFORE cell appears verbatim). L3 and L6 read dropped in the cells that count, but all four dropped/active rows share kind `conditional_hypothesis_from_package`, nomination CONDITIONAL and the same 53-row list: they look more active than the package says |
| (b) E_GABA-first order as the sources' conditional reading, quoted, not an observation | met: M16 and M17 `interpretable_after` (M02, M04, M05) quoted and labelled; L2's quotation names only "the Phase-0 measurements" in general (reader R2, partly) |
| (c) M15 co-requirement; both matching variables of CF23 unresolved | M15 as co-requirement of every drug arm: met. CF23 appears as an id only; its two variables were already in BEFORE (my dated note in levers.tsv), so nothing new |
| (d) conflicts that change how an arm is read, both quotes | NOT met: CF04, CF05a, CF05b, CF23 are listed by id and type, with no content; CF01 and CF03 are not reached by one hop (second-hop rows listed and not followed, as HE disclosed) |
| (e) independent reader finds it actionable | NOT met: "mostly adds a map to the ADV-006 package"; the only new ordering (mIPSC, agonist response and E_GABA before an L1/L2 arm) was already implied by BEFORE |
| Harms | none of the WORSE list: no side chosen, no order of cost read as dependency, no id read in the wrong space, no subunit wording added, no preparation moved silently by the output's own text. Reader hazards: M01 means two things inside the L3 row's quoted cells with no crosswalk; contexts (preparation, age) of joined rows are never stated |

## Reader verdicts (R1-R12, reproduced from the report)
SUPPORTED: R1, R3, R7, R11. PARTLY: R2, R4, R5, R6, R8, R10, R12. NOT SUPPORTED: R9 (the generator's sentence that the package does not classify the other levers is false for this package: SCI47 levers_notes.md and README answer 3 treat L1 and L2 as alternatives chosen by the Phase-0 outcome, L4 as generic comparator). R10: "expected result not stated" is true of the levers.tsv row only; SCI47 matrix O01 and levers_notes.md state what each outcome would favour. I checked CF04 and CF05a against conflicts.tsv: they are genuine, typed pipette/solution and cohort structure, against the August design; the output does not carry their content.

## Verdict
NO DIFFERENCE in what an independent reader finds actionable; an observed change in the generator output exists (six lever rows and a 53-row map, accurately quoted). Kept apart: (1) observed change in output: yes; (2) better formulation of an experiment: not shown (the reader names items the experiment needs that neither BEFORE nor AFTER reach: the evoked IPSC M03 tied to the L1-versus-L2 choice, the outcome-to-lever table, M06 for L1, the non-Wwox comparator arms, burst reduction is not correction of the defect, L2's third ADV-004 "may not"); (3) predictive capacity: none, none claimed.

## Missing steps (no consumer updated, since not improved)
1. The join carries conflict ids, not their content (type, cell, both quotes): mechanical, in the generator (HE), as the conflict rows of the design file already do.
2. CF01 and CF03 sit behind M01 (second hop): a decision on whether a declared-key join may follow one more hop where the gating row's own list names it (HE with the package owners).
3. The slot "expected result: not stated" and the sentence "the package does not classify the other rows" contradict SCI47's own outcome table: mapping gap, needs the owner (SCI) to confirm the mapping.
4. Dropped levers L3 and L6 are labelled like active ones: a label (HE).
5. Preparation and age of each joined row are absent: a column (HE).
Residual disposition: ADV decides whether the thread continues (L3-L6, SCI42 explanations) on this result: the answer to its question is that the join as built is not yet actionable; steps 1, 3 and 5 are the ones the reader's list points to.

## Not shown
A better experiment, a better prediction, or generality; one case chosen by ADV from my proposal, criteria by me, scored by an independent reader on one pass.

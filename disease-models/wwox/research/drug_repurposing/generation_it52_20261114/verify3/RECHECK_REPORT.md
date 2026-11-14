# RECHECK_REPORT: bounded recheck of verify3 (after3) against the originals

Non-canonical research material. Not medical advice. Reference genotype class only. No ranking changed.

D = `disease-models/wwox/research/drug_repurposing`. Checked: `D/generation_it52_20261114/verify3/after3_rows_L1_L2_L3_L6.tsv` against ADV-006 `output/measurements.tsv`, `conflicts.tsv`, `README.md`, SCI47 `levers.tsv`, and my earlier `verify2/READER_REPORT2.md`. Only the points the coordinator listed. The checks were done with scripts: substring equality of every printed conflict cell against `conflicts.tsv`, and of every printed "M..: preparation '...'; age_bin '...'" against `measurements.tsv` (129 occurrences in L1, L2 and L3, 0 mismatches).

## Point 1. Preparation and age on every conflict side in the L1 and L2 design_join: PARTLY

What is closed:
- Each genuine conflict printed in full (CF04, CF05a, CF05b, CF23 in L1 and L2) now has, per side, a "context: the preparation of the ADV-006 row(s) it is reconciled into" cell. All contexts are verbatim from `measurements.tsv` (checked).
- The August-candidate sides of CF04 (side B) and CF05a (side A) carry: "the August candidate's preparation, ADV-006 M14 verbatim: preparation 'Wwox-/- (Aqeilan allele), Wwox+/-, P47T/P47T; CA3 pyramidal (primary) and dorsal-cortex layer 2/3 (secondary)'; age_bin 'P5-P7, P10-P12, P14-P16 (primary), P18-P21; adults for P47T only'". This equals `measurements.tsv` M14 `preparation` and `age_bin` exactly. It agrees with ADV-006 README answer 3: "Across the August design's preparation (2): CF04 ... CF05a ...".
- The SCI47 sides sit on M01/M02/M05 or M03 contexts, which state Synapsin-Cre layer II/III, P13-P17 (M01 'mouse neuron-deleted (Synapsin-Cre) neocortical slice, layer II/III pyramidal cells (SCI47 Phase 0); the SCI42 row does not state it'; M05 'mouse Synapsin-Cre knockout ... layer II/III ...').
- L2's inherited context is marked once, at the head: "preparation: 'Synapsin-Cre slice, layer II/III, P13-17' [inherited context: this preparation or age is ADV-006's for the row; L2's own cells in levers.tsv do not state it (the Synapsin-Cre layer II/III P13-17 context is written in L1's cells)]". This is correct: L1's `action_required_and_context` says "context: Synapsin-Cre slice, layer II/III, P13-17, burst endpoint as LFP", and L2's cells say only "functional_comparator: as L1".
- No printed conflict side now carries a wrong preparation. CF23 sides carry M15's "burst slice preparation" with age "not stated by the source" (verbatim).

What stays partly open:
- (a) The August side is mapped to M14 by the generator. `conflicts.tsv` gives `m_id` M02 for CF04 and M01;M02;M05 for CF05a, and ADV-006's M01 and M02 `source_names` also list "CC-EXPERIMENT endpoint 4". The M14 mapping is supported by the README sentence above and by M14's `source_names`, but it is not derivable from `conflicts.tsv` alone. The words "global allele" are not printed (M14's `name` has them); the reader gets "Wwox-/- (Aqeilan allele)" and "CA3" and must infer that it is another line.
- (b) CF04 side A prints its context as M02: preparation 'as M01'; age_bin 'P13-P17'. This is verbatim but unresolved: M01's cell is not printed in CF04, so that side never says Synapsin-Cre in that conflict.
- (c) In L2, the inherited mark appears once (head). The same M17 string "Synapsin-Cre slice, layer II/III, P13-17" is printed unmarked four more times inside the CF11 and CF16 side contexts. These are citations of the same row cell, but the "inherited" label does not travel with them.
- (d) Thirteen other-typed conflicts are still ids only ("CF06 (gap)" ... "CF22 (gap)"); no sides, so no preparation. CF06, CF07 and CF09 (M05;M14) are the ones about the August line (CF06 vs the global allele); they are marked only "(gap)".

## Point 2. M01: one hop label per lever in both columns: L1 CLOSED, L2 OPEN

- L1: `design_join`: "first hop through the attachments (see lever_attachments), not second hop: M01, M02, M04". `lever_attachments`: "ADV-006 rows whose requests_merged names an attached matrix row (first hop, also for M01 and M03 where listed): M01, M02, M03, M04". The two agree. No second-hop list remains in L1.
- L2: `design_join`: "second-hop rows named by the gating rows and not reached by the attachments, listed and NOT followed (an order of cost or priority may sit there): M01". `lever_attachments`: "ADV-006 row M01 (...): owners' reading: first hop for the lever; no declared key of this row reaches it (owner-stated, SCI PRESIDIO-001)". M01 is a second-hop row "not reached by the attachments" in one column and an attached first-hop row in the other. The new phrase "not reached by the attachments" is false for L2 M01. M01 also appears in L2's own list of rows whose `lever_or_comparison_gated` names L2 ("M01 'E-artefact versus supply/response; L1 and L2 premise ...'"). So the contradiction I reported in READER_REPORT2 (R3) is still there in L2, now with a new false clause.

## Point 3. Each printed conflict carries the three cells verbatim: CLOSED for conflicts printed in full; two exceptions by design

- For every conflict printed in full in L1, L2 and L3 (design_join and lever_attachments), the strings "why_both_cannot_be_met_in_one_recording: <value>", "which_would_change_the_interpretation: <value>" and "adjudicable_from_the_packages: <value>" are equal to `conflicts.tsv` in full. The character after each value is the expected delimiter, so nothing is cut or appended. `type` and `cell_type` also match.
- Exceptions: CF01 is not printed with the three cells (point 4). The thirteen gap/synonym rows in L1 and L2 are ids only.
- What was added around the cells: the `side A (path; context: ...)` and `side B (...)` wrappers, with the context cells described in point 1. These are marks and verbatim cells from `measurements.tsv`.

## Point 4. L2 CF01 text same as L1: CLOSED

L2 `design_join` and `lever_attachments` both carry: "CF01 NOT attached: SCI47 is not consistent on the sIPSC configuration (its Phase 0 item (i) asks a pipette-set chloride, its cohort sentence names perforated native chloride): stating the conflict for a lever needs a choice that is the owners'". It is the same sentence as in L1. No bare id remains for CF01 outside the 53-row id list. The sentence is supported by SCI47 `design_review.md` Phase 0 ("the minimum that survives is a perforated-patch cohort for native-chloride sIPSC ..." and "(i) sIPSC with a physiological-chloride pipette and with the high-chloride pipette in different cells") and by the ADV-006 README update, point (1). One awkwardness: in L2 the sentence sits under "genuine conflicts on them, for the reader to weigh".

## Point 5. "The same rows reach the other GABA lever": CLOSED

- The sentence no longer appears (0 occurrences in L1, L2 and L3).
- Replacement, for every route-E row: "its outcome cell names E2 [E5 / E1, E3 / E4], an E-id this lever names; the other levers whose own cells name the same E-id: none". Checked against `levers.tsv`: the E-ids in each lever's own cells are L1 E2 and E5, L2 E1, E3 and E4, L5 E6, and none for L3, L4 and L6. So "none" is correct for O10 and O14 via E5 (L1), and for O02 and O05 via E2 (L1) and O01, O02, O03, O05, O14 via E1/E3/E4 (L2). The wrong O10 statement is gone.
- Caveat: because the test is per E-id, O02 and O05 are now each printed in both L1 and L2 with "none" and no word that the same row is attached to both levers. The true part of the old sentence (O01/O02/O05 do not separate L1 from L2) is no longer printed. Not an error.

## L3 tags

- O03 and O14 on L3 now read "named in requests_merged of M05 (rows declared for this lever)". M20 is gone. This is correct: M05's `requests_merged` names both and `levers:L3`; M20 names only `levers:L3`.
- CF15 on L3 is printed in full. Cells checked verbatim: `adjudicable_from_the_packages` "partly (SCI47 states its reason in the L3 row ...)", `which_would_change_the_interpretation` "Whether a chloride-transport arm is a stated step after E_GABA or a closed branch.", `why_both_cannot_be_met_in_one_recording` "V17 note: gap ... An arm is in the design or it is not." M20's own cell "arm conditional; dropped by SCI47: CF15" is not printed, but CF15 now carries the drop (side B "dropped as a drug arm now; ...").

## M06 for L1: printed with its own words, conflicts not followed: CLOSED

L1 now prints "M06 'the extrasynaptic modulator class of M17 (SCI42 conditional_prediction row 9); L1 readout'". This is verbatim from `measurements.tsv` M06 `lever_or_comparison_gated`. The list header says "(their words; their conflicts are not followed)". M06 appears in no `m_id` of `conflicts.tsv`, so there are no conflicts to follow.

---

## Beyond the five points

(a) M06 on L1. It is verbatim, but it is new content, not a mark. The reason it is attached is the text token "L1" in a `lever_or_comparison_gated` cell, not a declared key: M06's `requests_merged` ("sci42_chloride#new_measurements:M07 ; sci42_chloride#explanations:E-compensation") names no lever. The same text-match rule adds M01, M02, M03, M05, M12 and M18 to L1 and M01, M02, M03, M04, M05, M12 and M18 to L2, all verbatim from `measurements.tsv`. M06's phrase talks about M17 (an L2 arm) and does not say so for the L1 reader.

(b) CF15 on L3. Verbatim from `conflicts.tsv` and a consequence of a declared key: CF15's `m_id` is "M20;M05" and both M05 and M20 declare `sci47_inhibitory#levers:L3` in `requests_merged`. It is new content in the L3 join. L3 now prints fifteen conflicts in full (CF05a, CF05b, CF06 to CF10, CF13, CF14, CF15, CF21, CF23 and others), where L1 prints five and L2 seven. The dropped lever's join is the longest.

(c) Observation, not part of the pass. `design_join` length in characters: L1 10,810; L2 14,716; L3 28,985. `lever_attachments`: L1 20,662; L2 12,178; L3 22,920. In every row, 31 to 35% of the join is the repeated "context: the preparation of the ADV-006 row(s) it is reconciled into" blocks (L1 3,750 of 10,810; L2 4,742 of 14,716; L3 9,129 of 28,985). In L3 the M05 preparation string is printed 18 times. As a reader: the gate sentence and the hop labels sit at the start and end of the cell and are easy to find in L1. In L2 and L3 the decisive items (gate, hop labels, "no side is chosen on any conflict; no order here is a result", the CF23 owner note) are separated by several thousand characters of conflict contexts, and the L2 M01 contradiction is hard to see because the two statements are 6,000 characters apart in different columns. The length hinders more in L3 (a dropped lever) than in L1 and L2.

---

## Did the correction add, introduce, or leave open?

- Added beyond marks and verbatim cells: (i) the choice of M14 as the context for the August sides (a mapping, supported by the README); (ii) the list of rows that name L1 or L2 in `lever_or_comparison_gated`, including M06 (verbatim, by text match, not by a declared key); (iii) CF11 and CF16 in full for L1 and L2, and about ten gap/synonym rows in full for L3 (verbatim); (iv) the E-id "other levers: none" clause; (v) the hop labels. Everything I checked is verbatim from the originals except the labels and mapping choices named here.
- New error introduced: yes, one. L2 `design_join` states that M01 is "not reached by the attachments", which is false against L2's own `lever_attachments`.
- The harm (an unsaid move of context between preparations): the August sides of CF04 and CF05a now carry their own preparation and age verbatim, L2's inherited context is marked, and no printed conflict side sits on the Synapsin-Cre arm with a wrong preparation. The remaining items under point 1 are residual: "as M01" unresolved on CF04 side A, the unmarked repeats of the inherited L2 string in CF11 and CF16, the "global allele" wording not printed, and the thirteen ids-only rows.

Per-point verdicts: point 1 PARTLY; point 2 PARTLY (L1 CLOSED, L2 OPEN); point 3 CLOSED; point 4 CLOSED; point 5 CLOSED; L3 tags CLOSED; M06 on L1 CLOSED.

Harm closed: yes (for the unsaid move of context between preparations on printed conflict sides; the L2 M01 contradiction is a separate open defect).

Model, effort, turns for this recheck: Sonnet 5.5 (claude-sonnet-5-5); reasoning effort 10 (low); about 9 further tool-calling turns plus this write-up.

# Independent verification of the revised priority rules (P11), 2026-10-29

Producer: scientist-d. Verifier: independent; 16 sampled card x need positions derived by hand from the rule text: 16/16 match the code; five defects (tool compound F1, outside-WWOX counter-evidence silent, wild-type-only row counted favourable, 'firm' overstates, F2 criteria bundle) fixed by the producer in task/it5-p11fix.

# P11 verification (scientist-b), commit 12affd39, read-only
Derivation from rule text + pertinence rows; code run: `repurposing_view.py positions` (45 lines, 43 links + 1 unlinked card).
| link | my derivation | code |
|---|---|---|
| C01 gene addition | F1 (1 fav row, untreated same genotype, no weak flag; high_dose_only/n=5 not weakening flags) | F1 |
| C04 gene addition | F1 (GFAP-P5HD untreated KO+WT, no weak flag; LD partial; MBP unquantified) | F1 |
| C04 glycaemia/growth | C2 (fav + 2 null + mixed) | C2 |
| D01 MYC | C2 (normalised-vs-WT + null) | C2 |
| D01 Wnt | P3 (no row) | P3 |
| EB-ETX-01 seizure / T-type | F2 (one_experiment, graphical) | F2 / F2 |
| G01 seizure | F2 (nonspecific_also_in_wild_type); WT-arm rows not WWOX kinds | F2 |
| G01 GSK3 | P3 | P3 |
| EB-KD-01 seizure / pyruvate | F2 (uncontrolled case) / P3 | F2 / P3 |
| EB-VGB-01 seizure | C2 (3 benefit+partial vs 3 null) | C2 |
| EB-VGB-01 inhibitory, myelination | P3, P3 | P3, P3 |
| H01 T-type / seizure | F3 (2 other-disease benefit, need has WWOX obs) / P3 | F3 / P3 |
| H02 myelination / seizure / inhibitory | C3 (7 harm, no benefit) / F3 / P3 | C3 / F3 / P3 |
| A01 PBA | F3 | F3 |
| B02 | P1 (abstention) | P1 |
| F01 d-APV | F1 by letter (before/after washout, no weak flag) | F1 |
Also B01 (P3: favourable other-gene precedent but no WWOX obs on need) matches. 16/16 sampled links agree; no code/rule disagreement found. Hand check of the remaining table lines was by spot-reading only.

## (1) Code implements written rules: yes
classify_rows/assign_need_position match section 2 (order, "mixed" row alone also -> C2, not_normalised and unresolved/unquantified counted neither way, F1 needs control + depth + no WEAK_FLAGS).

## (2) Scientific defensibility
- F1 for one favourable readout with untreated comparator, full/partial text, one clean row: acceptable as a "reading-quality screen" only. C01 is a single high-dose arm, n=5: F1 label "firm WWOX readout" overstates; the page prints n=5/high-dose caveat, so honest but label is strong. Suggest renaming F1 to "controlled WWOX readout" or requiring >=2 independent rows/endpoints for "firm" (smallest: rename). Severity LOW-MED.
- C04 gene addition F1 rests on one firm row (GFAP cell count, a glial marker) while survival/motor rows have comparator "not stated". Rule is satisfied literally; the F1 is carried by the least clinically weighty endpoint. LOW-MED (same fix: F1 should name the firm row; check the page shows it).
- D01 MYC C2: DR-D01-001 is counted "favourable" although its own row says "not_a_recovery_comparison; not counted as recovery" and comparison_with_wild_type_only. Rule 3 counts "normalised vs WT" as favourable. Honest outcome would be C1 (only real signed result = null). Direction is safe (counter-evidence family either way) but the Criteria line says "mixed". LOW-MED. Fix: a genotype_comparison row flagged not_a_recovery_comparison counts neither way (listed).
- C3 for H02 myelination: defensible (vigabatrin-class myelin vacuolation in rodent/dog; safety question), and the label "study = does it apply" is right. Note it is a safety question, not a benefit hypothesis; C3 wording is adequate.
- F01 d-APV F1: MISLEADING. The row itself carries flags tool_compound_d-APV;full_competitive_block_only;AMPAR_untested and basis "NOT attached to memantine or perampanel", yet is F1 "firm" for a candidate list. Severity MEDIUM-HIGH (the strongest label on a non-drug / non-candidate intervention). Smallest honest fix: add "tool_compound" and "NOT attached" to WEAK_FLAGS-style cap (F1 -> F2), or at minimum a visible "tool compound" tag on the link driven by the existing flag (no new data needed). Also F01 has outside null+harm rows (counter_in_rows True) beside an F1; F1 text says "no counter-result beside it" but the test ignores outside rows. LOW-MED: print "outside-WWOX counter-evidence exists" on F1 criteria, or state in the F1 definition that it concerns WWOX-system rows only.

## (3) Hiding/promotion
- No WWOX-side null/harm hidden by a favourable one (C2 triggers). Null or unfavourable only never reaches F. OK.
- Residual: (a) F3 ignores outside harm/null when any outside favourable exists (H01 T-type: 2 benefit vs null + harm -> F3; A01: 3 vs 2 null; E01). Flag shows counter_in_rows but the position label says nothing. LOW-MED: tag F3 "with outside counter-evidence" (data field already exists). (b) "not_normalised_vs_wild_type" low-dose arms (C04 GFAP area LD) count neither way, so an F1 can sit beside a not-normalised arm; listed on the page, not in the position. LOW. (c) the wild-type-arm lithium effects are kept out, consistent.
- No null/unfavourable promoted as favourable in sampled links.

## (4) Criteria lines
Printed "criteria not met" are the tested statements, correct. Weakness: the F1 criterion is one compound sentence (controlled AND full/partial text AND no weak flag), so for F2 the line does not say WHICH part failed (ETX: comparator ok, flags failed). LOW; split into three statements or append the failing flag names. Wording "no null... in a WWOX system" listed as not met for C2 correctly. P3 label ("nothing favourable ... or no WWOX observation") merges two reasons (B01), but the Criteria line disambiguates.

## (5) Global presentation
Honest: card shows the set of need positions (`F1 + C2`), tiles count links, `group` removed from cards. No best-of-needs found.

## (6) Tests
`python3 -B framework/scripts/test_repurposing_view.py` in worktree: Ran 48, OK (stdout includes expected "STALE" lines from the negative tests). Mutation in a scratch copy (git archive, scratchpad/mut): overview_positions truncated to the first (best) position -> 3 failures incl. test_overview_position_is_the_set_of_need_positions_never_best_of. Test is effective. Repo untouched.

## Defects by severity
1. MED-HIGH: F01 d-APV is F1 despite tool-compound/not-attached flags (admitted limit, but fixable now from existing flags).
2. LOW-MED: F3 hides outside counter-evidence in label; F1 criterion silent on outside counter rows (F01).
3. LOW-MED: D01-001 counted favourable though row says not a recovery comparison (C2 should be C1).
4. LOW-MED: "firm" wording vs single-row/n=5 (C01, C04 carried by GFAP row).
5. LOW: F2 criteria line does not name the failing component.

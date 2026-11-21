# ADV-148 integration: what was applied, where, and the marker totals (IT, 2026-11-21)

Source: the design team's replacements S01 to S14 (`../../../advisor_pilot_20261113/brainstorm_20261116/adv148_residual_conflicts_sci_20261121/REPLACEMENTS_FOR_IT_ADV148_SCI_20261121.tsv`, main 6bc80371b), applied by `../integrate_adv148_it_20261121.py` (idempotent; every numeric token of an inserted text is traced to the row's column, to the older texts or to the current text, otherwise the run stops; a run with tokens in none of them printed `[]`). Every replaced marker, note and sentence is kept as it stood in the History section "Markers and sentences replaced on 2026-11-21 (design-team group C)". Public, disease-level; no new dose; not medical advice.

## Where each replacement went
| Row | Items | Applied as |
|---|---|---|
| S01 | C002, R3C02 | rule sentence of the wild-type series rewritten (straddle of P11 and P14 required only if the chloride-window read is wanted); the earlier series note is replaced by the S01 note (it is superseded); marker R3C02 replaced by a laboratory question |
| S02 | C003 | both totals (3 ages: 21 wild-type cells, 27 in all; 4 ages: 28 and 34, +77 animals) as a note in the sample-size section, before the S14 note |
| S03 | C004, R3C04 | the Q19 note's pilot-ages clause replaced (two laboratory-chosen ages inside P12 to P17; P11 and P14 are not the pilot ages; this corrects the earlier answer); marker R3C04 replaced by a laboratory question |
| S04 | C007 | status box sentence on numbers rewritten |
| S05 | C008 | the Cheng regimen specifics in the Q15 note replaced by a pointer to the Methods of Cheng 2020 |
| S06 | C011, Q84 | marker Q84 replaced by the note (P5 and P8 are labels of the in vivo priors file); three body mentions now say "of the in vivo priors file" |
| S07 | C012 | the two group-size statements in the body replaced by one, labelled as read from the figure legends; plus ADV's line: the sizes rest on a single origin, the supplement is held and holds no seizure methods or N, no second source by three routes, only the authors could add one |
| S08 | C013 | "grade" for the 0 to 6 scale in the design-team notes (area under the grade; grade 6 is death; grade units; a wild-type response that is not at the floor); the stage 1 row says the same |
| S09 | Q51 | marker replaced by the latency rule (window starts at the PTZ injection; INFERENCE to be fixed before data) plus a laboratory question |
| S10 | R3C01 | marker replaced by the rule on which stimulus governs which cell, plus a laboratory question |
| S11 | R3C05 | marker replaced by the note; the E2 line and the E2 row of the outcomes table corrected (age-limited wild-type non-response, not a floor-bound arm; at the floor the reading is E5) |
| S12 | R3C09 | marker replaced by the note; the "75 litters" in the planning-scale paragraph replaced by the current figures |
| S13 | R3C10 | marker replaced by the rule for an unresolved panel age (validity-indeterminate, not an assay failure), plus a laboratory question |
| S14 | R3Q37 | marker replaced by an illustrative range with its basis, plus a laboratory question |

Two corrections to what was integrated from ADV-144 (carried by SCI): the pilot ages (Q19 note, S03) and the CLAR-SERIES note (S01, straddle optional).

## Marker totals in the governing text (before the History)
| Marker | Before | After |
|---|---|---|
| OPEN-GAP, owner design team (SCI) | 30 | 27 |
| OPEN-GAP, owner laboratory | 31 | 37 (new: S01, S03, S09, S10, S13, S14) |
| OPEN-GAP, owner operator | 8 | 8 |
| OPEN-GAP, all | 69 | 72 |
| CONFLICT-OPEN (all design team) | 19 | 13 (R3C01, R3C02, R3C04, R3C05, R3C09, R3C10 resolved; R2 and C-series markers outside ADV-148 remain: C02, C03, C09, C16, C23, C30, C31, C32, C35, R2C01, R2C05, R2C09, R2C10) |

Not applied, because ADV-148 did not answer them: the other 13 conflict markers and the owner-SCI OPEN-GAP markers outside the 15 items. The laboratory question of R3Q37 stays a laboratory question (pups per month and breeding scheme).

## Checker (`../check_current_text.py` with both token registers)
Part 1: three lines, all notes of the earlier ADV-144 integration (Q22, Q34, Q31) with tokens SCI listed elsewhere in its register (already reconciled in `../verify_adv146/RECONCILIATION_ADV144_IT_20261121.md`); none of the ADV-148 notes. Part 2: 0 non-verbatim History lines.

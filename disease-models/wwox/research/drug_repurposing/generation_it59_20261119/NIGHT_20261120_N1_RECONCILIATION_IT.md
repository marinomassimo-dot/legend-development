# N1 reconciliation, IT Orchestrator window N, 2026-11-20 (night continuation; mandate ORCH-ROADMAP-IT59-20261119)

Reference-genotype class only; nothing here is a result or medical advice; no personal data. Written so that a later window does not repeat a closed integration. Reply language to the operator: Italian; files: English.

## 1. What is already consumed (do not repeat)

| Delivery | Consumer and landing | State |
|---|---|---|
| ADV-122 result (SCI, `0324dbeac`, merge `13efa8e80`): prior 0.2 to 4.2 mM total brain at the Cheng regimen by two routes, anchor sits at the upper edge of a model-conditional coherence check (wording corrected after SCI part A, 2026-11-20) | SCI v3.1 dated lines 6.28 and 6.29 (`7eae5603f`); ADV correction and DREAM line (`f3b07303d`); HE ethosuximide sheet dated addition (`787d90705`, origin SCI, not re-read by HE); IT dated notes on the ADV-097 consumption record and the V3 review, dated line on map row WO-24 (`5600101a2`, landed `2d3e72b67`) | consumed; WO-24 stays OPEN |
| The 'adult effective band about 2 to 6 mM' | withdrawn as a sourced band in four places (SCI 6.29, ADV, the two IT files); H01, G01, WO-24 and IT46-Q04 never carried it | closed |
| WM103 part 1 (three dated notes, `BATCH_20261120_002`) and the second blind check | landed `9b8aad555`; part 2 (MAJOR) is the operator's item 18 | part 1 closed; part 2 reserved |
| EB-ETX-01 packet (unit B packet change, earlier) | card and packet already carry the anchor with its cautions (homogenate 1 to 2, no dilution correction, saline arm, 'about half the dose of the one Wwox experiment') | consumed up to the ADV-122 limit |

## 2. What is owed and what it waits for

| Owed | Event it waits for | Independent of the wait |
|---|---|---|
| EB-ETX-01 card and packet text: add the coherence-check limit (model-conditional, not a conservation law) and the ADV-122 prior (wording in the checkpoint addendum of 2026-11-20) | the package: `package` then `package --check` on the final tip, after item 17 | no |
| the other card-text folds (EB-ETX-01 harm field, I01 and G01 harm text, F02, the TMP195 line, WO-24 / Kv7 / lithium / vigabatrin pup-exposure lines) | the same package | no |
| package pages online (the 2026-11-19 ones) | item 17 (guard names `tiratricol`, `tta-a2`: nobody rewords or loosens the guard) | no |
| WM103 part 2 and the coordinated CLAIM 011 Title and BLOCK 2 row | item 18 | part 1 done |
| CI | HE's tick line; the red is exactly three repository-side failures in `test_repurposing_view.py` (package-current, two shareable-page name tests), the same on #1638 and #1649 (HE addendum B1, GitHub job steps read from the API) | no full battery is repeated for this unchanged block |

Reserved items 17 and 18 stay with the operator. They block the package and the card-text folds only; analysis, integration, delegations and the open-question map continue.

## 3. State of the mandate record

Before this window's additions the record had one IN_PROGRESS step (6, operational continuation) and one BLOCKED step (4, the generation comparison, deferred by its own rule because no decision rode on it on 2026-11-20). Step 6 is the standing operational step and now corresponds to real work: the night mandate steps N1 to N5 added to the same record by `mandate_continuity.py accept`. Step 4's deferral is superseded in scope, not in kind, by N3 (a gain evaluation when the case allows, with criteria fixed first); it stays BLOCKED until N3 names a case and its criteria. No other record of the orchestrator actor carries an open step (checked over `ledger/tasks/orchestrator/*.json`).

## 4. Independent work that continues during the waits
Choosing and carrying a new case (N2), the gain evaluation on it (N3), consumption (N4), delivery (N5). No frozen candidate is touched.

## 5. Addendum, 2026-11-20 night: wording corrected after SCI part A
SCI's `CORRECTION_ADV122_PART_A_COHERENCE_CHECK_SCI_20261120.md` (landed 9c01c2be58f9) shows that dose over volume is a model-conditional coherence check, not a conservation law; IT's dated notes on the ADV-097 consumption record and the V3 review now carry the replacement paragraph (originals unchanged), and the two table rows above use it. The EB-ETX-01 card fold wording in checkpoint 3's addendum says 'at or above ... uncertain by about 2 to 3 times' and is not changed. The consumer list is SCI's section 4; the ADV lines (SELECTION_NOTE line 106, assignments line 295) are ADV's to correct.

## 6. Addendum, 2026-11-20 late: ADV-123 consumer_delta received (SCI, main fc7564717a73; peer content, not an order)
Source: `brainstorm_20261116/adv123_myelin_function_map_sci_20261120/RESULT_ADV123_SCI_20261120.md` section 6. Owed to IT, folded with the package after item 17 (card-text change, no exposure row moves, no rank moves): (a) cards F02 and J01: add 'OL class: myelin contribution untested, drug effects not separated from direct action'; (b) the thyromimetic row text: 'late start (Triac P22-P42) did not improve myelination, function not measured; no human post-thyromimetic myelin imaging reached'; (c) wherever the Wwox P17 electron-microscopy counts are printed, label the pair: myelinated axons per field of view WT 130.3, KO 45.7, treated 104.9 at P17; the 51.5 and 26.4 pair is the corpus callosum at 6 months. Not yet checked by IT: SCI's adjudications (B5 density claim withdrawn; A06 legend p duplicated) and the four decisive points; IT re-ran nothing and takes the text as SCI-level, verified on 14 triples only. HE sheet BATCH6 and the broad-comparison OL row are ADV's and HE's to apply. The painted-page statement of N4 is unchanged.

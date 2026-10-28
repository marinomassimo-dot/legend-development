# Final check of the round-3 coverage corrections (actor scientist-c)

Subject: main dcea7f1d. Re-run of `2026-10-28_it3_coverage_reverification.py` (unchanged, reads raw files) plus a detector test run inline (below). Not medical advice.

## Verdict: PASS, with three minor residuals

## 1. The 21 rows added to assertion_pertinence.tsv (52 to 73 lines; 71 data rows; 0 assertions now unlisted)
Opened each against its packet (direction, bridge comparison, reading depth, context, measured-result note).

* AAV9 glucose day 20 HD/LD (need SYSTEMIC-GLYCAEMIA-GROWTH): pertinent (glycaemia part of the need). Sign `normalised_vs_wild_type` (HD about 147, not different from wild type) and `not_normalised_vs_wild_type` (LD about 128, one star below). Packet direction UNKNOWN, no untreated-knockout arm; the file states this and writes no direction, L4 no. Correct.
* AAV9 GFAP area HD/LD (GENE-ADDITION): same pattern. LD is two stars worse than wild type and is kept visible. Correct.
* AAV9 MBP HD/LD: `unquantified`, `counts_L3=no`, micrographs only, authors' interpretation. Correct and conservative.
* D01-002 (MYC need): measured no recovery, CTIP2 far below wild type, reading depth UNKNOWN. Sign null, L3 yes, L4 no. The A51 cell is now `observed_depth_unknown` with signs {benefit 1, null 1} listed under `signs_depth_unknown_not_counted_as_observed`. The split that DR-D01-001 hid is now visible. Correct.
* Vigabatrin A-VGB-4 (clinical, not the electrographic endpoint it names; unresolved, L3 no), A-VGB-5 and A-VGB-6 (reported nulls, case level, L3 yes, L4 no), A-VGB-9 (developmental outcome, `out_of_scope_endpoint`), A-VGB-11 (combined with the ketogenic diet, `case_report_uninformative`). All correct; the two nulls now balance the two benefit reports.
* Ketogenic diet A-KD-2 (`case_report_uninformative`, unmeasured) and A-KD-3 (developmental label at one timepoint, out of scope). Correct.
* A-ETX-3 and DR-H01-004: research T-type blockers lowered progenitor viability in vitro, not ethosuximide and not apinocaltamide; sign harm, subject `tool_no_catalogue_identity`, L3 no. Correct and correctly not attached to a catalogued drug.
* DR-H01-001/-002/-003 (apinocaltamide in rat/mouse models, abstract-only; benefit, benefit, null): other-disease precedent, L3 no. The kindling null is kept. Correct.
* DR-A02-003: activity not measured (not a measured null), sign `unresolved`. Correct.

No defect in need, subject, sign, kind or flags. One presentation note: the GENE-ADDITION and GLYCAEMIA cells keep the state word `observed_wwox_system` although several of their signs are comparisons against wild type with no knockout arm; the signs and `no_knockout_arm` flag are listed in the cell, so I count this as disclosed, not an over-claim.

## 2. Recount
* Per-need and union figures unchanged and reproduced: 1,026 records (2.3% of 44,211; 4.2% of 24,423), 998 families on my key vs 997 reported (the producer's InChIKey-block merge), 1,337 with pathway members, exclusions 77+2+1 records.
* Matrix: L3 `observed_wwox_system` 7, `observed_case_level_only` 2, `observed_depth_unknown` 1, precedent-only 9, target-engagement-only 3; L4 `observed_experimental` 3 and `observed_case_level` 2. As expected.
* `interventions_with_a_listed_pertinent_readout_assertion` = 7 (perampanel is out, as I asked). Consistent cells 125 = 103 families; 0 favourable or opposed label on any `uncertain` need.

## 3. Generic artefact detector (rule: Guide-to-Pharmacology record with 3 or more symbols from the first 8 percent of the DGIdb alphabetical symbol list)
Reimplemented independently: 5,012 distinct DGIdb symbols, first 400 (to ARSD); 518 GtoP records trigger. Among the need symbols the only one in that block is ABAT (55 records flagged by the run rule; the explicit ABAT/ABCA rows cover the other 22 that carry fewer than 3 early symbols). ABAT outcome: 89 ABAT-linked records, 77 dropped (no second source), 12 kept. As stated. No other need gene is touched, so no false positive on a need gene today.
Evidence that the pattern is general and not only adenosine: flagged records include vasopressin analogues (ABCC6, AQP9, AR, ARAF), tetramethylammonium (ARF5, ARF6, ARG1), suramin, glutamic acid, brl-37344.
Residuals: (a) the 8 percent cut is arbitrary: any future need on a symbol up to ARSD (for example ADORA*, ADRA*, AKT1, APP, AR) will have its GtoP-only rows with 3 or more early symbols dropped; a genuine multi-target ligand with three real early-alphabet targets would also be dropped, so the rule should be reported per need with the dropped count (the summary reports it globally only); (b) the rule needs "second source", so genuine rows survive (valproate, tiagabine, vigabatrin, CPP-115 kept); (c) the 22 ABAT rows rely on the explicit list, not the detector.

## 4. plain_statement and the growth note
`plain_statement` is accurate: no catalogued repurposing candidate with a controlled WWOX-system recovery; the only experimental L4 cells are AAV9 (spike-wave high dose n 5; growth body weight only, glucose unchanged); the other L4 cells are uncontrolled vigabatrin and ketogenic-diet reports; ethosuximide, lithium and d-APV have single WWOX-system readouts without recovery status. The AAV9 note `growth = body weight only (blood glucose was not changed)` is present in the L4 cell (`endpoint_note`), the L3 flags (`growth=body_weight_only`) and the README. Confirmed.

## Concrete corrections (all minor)
1. Report artefact-detector drops per need in the summary (currently global), so a future need on an early-alphabet symbol is visible at once.
2. Consider a state word for L3 cells whose only comparisons are against wild type (`observed_vs_wild_type_only`) instead of `observed_wwox_system`; disclosed today by flags, not by name.
3. Replace the explicit ABAT/ABCA list by a test that fails if a need symbol enters the early block without a reviewer decision.

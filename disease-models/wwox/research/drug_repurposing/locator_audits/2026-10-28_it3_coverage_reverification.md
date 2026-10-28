# Re-verification of the revised it3 coverage layer (actor scientist-c)

Subject: main cb456e3c (merge of task/it3-search2). Script: `2026-10-28_it3_coverage_reverification.py` (same folder; offline; reads catalogue, needs, coverage outputs and cards directly; no producer module). Follows the first audit `2026-10-28_it3_coverage_independent_verification.md`. Not medical advice.

## Verdict

The numbers are reproduced exactly and six of my seven corrections are truly resolved in the computation. Remaining: a handful of curation inconsistencies in `assertion_pertinence.tsv`, selective listing (20 unlisted assertions, no per-cell indicator), and a few labels that still read stronger than their content. Nothing found that hides a stale or failed source.

## 1. Recount (script)

Independent rule: headline link = `intervention_target` or `disease_gene_product`, human ChEMBL rows by component symbol and DGIdb by HGNC symbol; excluded = the "Null" placeholder, Guide-to-Pharmacology ABAT/ABCA1-3 rows without a second source, and PDK1 rows from TdgClinicalTrial/PharmGKB on records that carry PDPK1 and no ChEMBL PDK1 mechanism.

* Per need, all 22: records identical to the summary; families identical except glutamate 192 vs 191 (my parent-key vs the producer's extra InChIKey-block merge, as before).
* Union: 1,026 records (identical), 998 families on my key vs 997 reported (same cause). 1,026/44,211 = 2.32% (2.3); 1,026/24,423 = 4.20% (4.2). Including pathway members: 1,337 (identical, 3.0%).
* Excluded records: 77 artefact + 2 alias + 1 placeholder = 80 (identical; the summary's 154/33/2 are row counts, its 80 is records). Touch distribution 910/78/7/0/0 ... (1/2/3/5/6 needs) matches within the one-family key difference; the 17-need "Null" pseudo-family is gone.
* GSK3B 51 (the one MAPT record in it also hits GSK3B), INHIBITORY-HYPOFUNCTION 11 (vigabatrin x2, CPP-115, valproate, divalproex, DP-VPA, tiagabine, pyridoxal phosphate, alanine, pyruvic acid, 4-hydroxybenzaldehyde). All as expected.
* Priorities: 125 consistent cells = 103 distinct families (66 glutamate, 35 T-type, 24 seizure). 0 favourable or opposed labels on `uncertain` needs. Only 2 `opposite_mechanism` (aspartic acid, glycine at GRIN2A/2B), both mechanically true and not candidates.

### Status of my seven corrections

| # | Correction | Status |
|---|---|---|
| 1 | Exclude GtoP ABAT artefact rows | RESOLVED in counts (77 records out). The rows remain in `associations.jsonl.gz` as `not_evaluable`, which does not say "excluded as source artefact"; add an explicit `excluded_reason` field so a reader of the association file is not left to infer it |
| 2 | MAPT effector constraint is not a link | RESOLVED (GSK3B 498 to 51; 710 records touch only effector/readout markers) |
| 3 | Link counts by target kind | RESOLVED (headline vs "incl pathway members" 1,337; per-cell `pathway_member_only` state, 383 cells) |
| 4 | Role rows: GRIA1-4 demoted, qualifiers, seizure label | RESOLVED for GRIA (unresolved), qualifiers carried in a new column and in `limits`. The qualifier text is in the file and the summary limits, but a `consistent_mechanism_candidate` priority record does not itself repeat "inferred from ONE d-APV block"; check that the 24 seizure and 66 glutamate records carry the `certainty_qualifiers` field (the matrix cell does) |
| 5 | L3/L4 endpoint pertinence, dose arms, sign, engagement vs readout, no d-APV on memantine | MOSTLY RESOLVED, see section 2 for residual defects |
| 6 | 201 cells vs 179 families; "Null" out | RESOLVED (125 / 103 reported separately; Null excluded) |
| 7 | Stale as a state; rename `not_relevant`; list PDK1 suspects | RESOLVED, see section 3 |

## 2. Hand-curated inputs

### source_artefacts.tsv (5 rows) and alias list
Sound. The GtoP rule is "require a second source", which my independent implementation reproduces exactly. The two alias-risk records (Osu-03012, celecoxib) are held out of the headline and listed in the summary as unresolved. Gap: the rule is keyed on `ABAT, ABCA1-3` only. The artefact is an alphabetical-prefix expansion, so other symbols from the same GtoP expansion (FTH1P4 was seen beside ABAT in adenosine rows; other receptors' expansions may exist) are not tested. None of those is a need symbol, so no headline impact now, but a new need with an A-prefixed symbol would be exposed. Suggest a generic detector: a GtoP record whose gene list contains 3 or more alphabetically consecutive symbols with an unrelated family.

### target_roles.tsv (17 rows)
Qualifier column added and honest. GRIA1-4 unresolved (correct); GRIN rows say "ONE full competitive block (d-APV)"; T-type rows say "ONE ethosuximide experiment, no drug-by-genotype test, lithium also acted in wild type"; seizure rows say "symptom-level inference". Residual: GRIN1 coupling `same` is applied to GRIN1, GRIN2A and GRIN2B alike although d-APV is non-subunit-selective and the GRIN-variant series split by variant class; the qualifier mentions the first, not the second. T-type: CACNA1H/I carry the same qualifier "no isoform-level" (good). No further change needed beyond adding "sign depends on variant class (GRIN series)" to the GRIN qualifier.

### assertion_pertinence.tsv (52 rows)
I opened all 52 against the packet and card (assertion text, direction, bridge comparison, reading depth, context) and checked pertinent need, subject, sign, evidence kind and the L3/L4 flags. Detail:

Correct (about 40 rows): all AAV9 rows (SWD, survival, motor, GFAP at high dose = L3+L4; low dose = mixed, L4 no; body weight HD = L4 for the growth need, glucose day 10 = null, no L4); vigabatrin A-VGB-1/-3 (case-level L4 flagged `queried_not_full_read`), A-VGB-2 partial, A-VGB-10 null, A-VGB-7/-8 harm kept apart with L3 no; ketogenic diet A-KD-1 now listed for seizure only (not PDH); ethosuximide A-ETX-1 for T-type and seizure (L3 yes, L4 no, one experiment); lithium DR-LI-001 (L3 yes, L4 no, `nonspecific_also_in_wild_type`); all enzyme assays (E02, E03, W2-005) as target engagement with no L3; d-APV DR-W2-001 as `tool_no_catalogue_identity`, L3 yes, "NOT attached to memantine or perampanel"; memantine GRIN series, harm datum DR-W2-004 kept as harm; all A01/A02/B01/E01 as other-disease with no L3; DR-E02-GEN-001 as a genetic (Ldh RNAi) precedent, not a compound result.

Defects found:
1. **DR-W2-007** (adult, seven drugs, `counts_L3=yes`, kind `case_report_wwox_clinical`, sign null). The row's own basis says it "supports no statement about the drug", yet it counts for L3 and puts perampanel in the cell state `measured_null_only`, and perampanel is one of the "9 interventions with a pertinent WWOX-system readout". An uninterpretable n=1 polytherapy is not a measured null for perampanel. Set `counts_L3=no` (kind `case_report_uninformative`) and drop perampanel from the 9 (then 8).
2. **DR-LI-002 / DR-LI-003** are the wild-type and heterozygous arms of the Wwox-null experiment, labelled `readout_other_disease`; the lithium cell then reports `signs_other_disease_precedent_not_observed_here: benefit 2`. They are control-genotype arms of a WWOX experiment, not other-disease precedent. Use kind `control_arm_same_experiment`. The effect is only a mislabel, but it feeds the very text meant to show the non-specificity of lithium.
3. **DR-D01-001** (A51): `counts_L3=yes` with reading depth UNKNOWN (flagged, and L4 no). L3 `observed_wwox_system` should not be reached when depth is UNKNOWN; downgrade to a state such as `observed_depth_unknown`.
4. **DR-AAV-SURV-LD / MOTOR-LD / WT-LD** sign `mixed` while the first (survival) is, per the need's observation O1, a fall to 0 percent by about day 77; `mixed` is acceptable, and L4 no is right. Fine, but `counts_L3=yes` makes the L3 cell for GENE-ADDITION include a low-dose arm that ends in extinction under the same state word as the high-dose arm; the signs are listed, so this is presentation only.
5. **Selective listing.** 20 DATO assertions are not listed and therefore not counted, including WWOX-system ones that could carry a null or contrary sign: D01 DR-D01-002 (NO_CHANGE in layer neurons, same organoid experiment as the counted decrease in progenitors), C04 glucose day 20 (HD/LD), GFAP area (HD/LD), MBP (HD/LD), vigabatrin A-VGB-4/-5/-6/-9/-11, ketogenic diet A-KD-2/-3, and the apinocaltamide card H01-001..004 (other-disease). The summary gives only the global figure (20). A cell can therefore read `observed` while a null or contrary assertion of the same experiment sits unlisted. Add per-cell `unassessed_assertions_on_the_same_card` and judge at least the WWOX-system ones (DR-D01-002, GLU20, A-VGB-4, A-KD-2, MBP).

## 3. Source-state logic

* Vocabulary in code: OK, STALE_EXPORT, STALE_AFTER_FAILED_REFRESH, PARTIAL, FAILED, INCOMPLETE, NOT_FETCHED; hard problems (FAILED, INCOMPLETE, NOT_FETCHED) of any source turn dispositions into `incomplete_or_failed_query`; stale states append a caveat to every absence-type result. Real state: dgidb `STALE_EXPORT`, dsld `PARTIAL` (981 of 4,697 names probed), others OK.
* All 679 priority records carry the stale caveat in their reason text; L1 `none_found` cells carry `source_caveat_stale`; `no_catalogue_link_found` (7) and `source_queried_without_result` (2) both say "absence holds for a STALE source". No disposition silently hides a stale source. Pass.
* Gap A: `PARTIAL` (DSLD) is reported as "affects access categories only" but nothing in the access fields of catalogue entries or priorities states that supplement status is name-only and incomplete for 3,700 of 4,697 names; `unknown/unverified` access for supplements is therefore not a negative but not flagged as partial in the record either. Add a caveat to the access field of priorities.
* Gap B: failure paths are exercised only by synthetic tests (as before); the real outputs contain no hard state. Acceptable, but the check should confirm it with a negative test on the real files (set a source FAILED in a scratch copy and assert all 679 priorities flip); I did not run that.
* STALE_AFTER_FAILED_REFRESH has no producer path visible in the real files (no refresh logic ran); it is reserved vocabulary.

## 4. The 9 interventions with a pertinent WWOX-system readout

Rows: AAV9 WWOX (SWD), AAV9 endpoint families, vigabatrin, ketogenic diet, ethosuximide, lithium, A51, glutamate node (d-APV), perampanel.

| Intervention | Reading |
|---|---|
| AAV9 WWOX, SWD (L3+L4 experimental) | Sound. Objective, high dose only, n 5 |
| AAV9 endpoint families, gene addition (L3; L4 only on high-dose arms) | Sound; low-dose arms correctly excluded from L4 |
| AAV9, glycaemia/growth (L3+L4 on body weight; glucose null) | Defensible: L4 rests on body weight alone and glucose is null. The state word should say "growth only" so that the need name is not read as glycaemia recovered |
| Vigabatrin, seizure (L3 and L4 case level) | Marginal but honestly labelled `observed_case_level`; reading depth `queried_not_full_read` and no comparator. Keep as case level; should not appear in any count of "recovery" |
| Ketogenic diet, seizure (case level) | Same; clinician-reported, no instrument |
| Ethosuximide, T-type and seizure (L3 only) | One experiment, graphical, no interaction test; correctly no L4 |
| Lithium, seizure (L3 only) | Non-specific, flagged; correctly no L4 and L1 `none_found` for seizure. Remaining wart: control arms mislabelled (defect 2) |
| A51, MYC (L3 only) | Depth UNKNOWN; downgrade (defect 3). "SOX2 is a readout marker" flag is present |
| Perampanel (L3 `measured_null_only`) | Over-claim (defect 1); should not count |

After defects 1-3, the honest statement is: 8 interventions with a WWOX-system readout or case report, of which 3 carry L4 (2 experimental, 1 case-level) in the cell-level counts, plus 2 case-level; none of them is a catalogued repurposing candidate with a controlled WWOX-system recovery. This is worth stating in the summary text because the AAV9 rows are a gene therapy, not a repurposing candidate, and the others are uncontrolled or non-specific.

## Concrete corrections (ranked)

1. DR-W2-007: `counts_L3=no`; remove perampanel from the "interventions with a pertinent readout" count (9 to 8).
2. DR-LI-002/-003: evidence kind `control_arm_same_experiment`, not `readout_other_disease`.
3. DR-D01-001: no `observed_wwox_system` when reading depth is UNKNOWN.
4. Per-cell indicator of unassessed assertions of the same card; judge the WWOX-system ones among the 20 (DR-D01-002, glucose day 20, GFAP area, MBP, A-VGB-4, A-KD-2).
5. `excluded_reason` field on artefact, alias and placeholder rows in `associations.jsonl.gz`.
6. Carry the DSLD PARTIAL caveat into access fields; negative test of a hard-failed source on the real files.
7. Generic detector for alphabetical-prefix GtoP expansions instead of a four-symbol list; add "sign depends on variant class" to the GRIN role qualifier.

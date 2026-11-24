# COMMIT CANDIDATE — CC-20261124-ORCHESTRATOR-ADV216-CONSUMERS-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (consumers of ADV-216, SCI) · **Date:** 2026-11-24 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin of the findings:** `advisor_pilot_20261113/brainstorm_20261116/adv216_reading_debt_three_partials_sci_20261124/RESULT_ADV216_READING_DEBT_THREE_PARTIALS_SCI_20261124.md` (SCI) and its three receipts (`FTR-20261124-29940337-01`, `FTR-20261124-24002024-01`, `FTR-20261124-PPR1124524-01`, all in the ledger on main). Directed by ADV on 2026-11-24 as ordinary candidates for the next `BATCH_COMMIT`.
**Status:** PROPOSED. No registry file is edited by this act.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice.

## 1 · CHANGE CLASS (stated before any apply)
**PATCH (depth lines and one wording qualifier).** Two `Evidence depth` lines are behind the ledger, one gets a dated update line, and one conditional-question cell gets a qualifier. No claim, status, grade, ranking row or working-model sentence changes.

## 2 · Proposed wording
**A. `PAPER 495` (Dohare 2018, GSK3beta inhibitor and myelination; not WWOX evidence), field `Evidence depth`.**
Old (verbatim fragments): `(the receipt that produced the manifest; no later reading has extended it)` and `unread or absent (receipt): figures `captions_only`, limitations `not_present`, supplementary `not_present`, tables `not_present``
New: `(the receipt that produced the manifest; a later receipt, `FTR-20261124-29940337-01` (SCI, ADV-216, reason `new_question_outside_prior_coverage`), read results, discussion and the two tables; abstract, introduction, methods and references not re-read)` and `unread or absent (latest receipt): figures `captions_only` (image routes returned HTTP 403 and a challenge page, nothing bypassed), limitations `not_present`, supplementary `not_present`; the earlier label `tables not_present` was wrong (Tables 1 and 2 are in the article)`.
Quote from SCI's result for the blind check: "the TABLES, wrongly marked `not_present` in the earlier receipt, are in the article and were read: Table 1 (twelve infants, six with and six without haemorrhage) and Table 2 (neurobehavioural scores, n = 10 / 10 / 9). The body has no Tau readout (zero occurrences) and tests one GSK3 inhibitor only".

**B. `PAPER 447` (Baraban 2013, scn1Lab zebrafish drug screen; not WWOX evidence), field `Evidence depth`.**
Old (verbatim fragments): `(the receipt that produced the manifest; no later reading has extended it)` and `unread or absent (receipt): figures `captions_only`, supplementary `not_read`, tables `not_present``
New: `(the receipt that produced the manifest; later receipts, the latest `FTR-20261124-24002024-01` (SCI, ADV-216, reason `new_question_outside_prior_coverage`), read results, discussion, the table and the supplementary PDF; Figures 5 and 6 were opened as images)` and `unread or absent (latest receipt): figures `captions_only` (Figures 1 to 4 not re-opened, an understatement on purpose), limitations `not_present`; the earlier labels `tables not_present` and `supplementary not_read` were wrong or superseded (Table I is a microarray of thirteen sodium-channel subunit probes; the supplementary spreadsheet was identified, not parsed)`.
Quote for the blind check: "Vigabatrin raised electrographic burst frequency in 6 of 7 fish (no group test reported), while the same paper's locomotion assay shows a fall of about 30 percent (not significant): the two assays disagree in sign for the same drug."

**C. `PAPER 157` (Abudiab 2025 preprint, oligodendroglial Wwox; preprint, not peer reviewed), dated update line at the foot of `Evidence depth`.**
Add (nothing replaced): `**Update 2026-11-24 (`FTR-20261124-PPR1124524-01`, SCI, ADV-216, reason `inadequate_prior_coverage`):** Supplementary Figures 1 to 6 are inside the held PDF (pages 17 to 22) and were read from rendered pages; the earlier map called them `captions_only`. They do not resolve the 59.1 versus 36.1 mismatch; the remyelination readout of Supplementary Figure 4 is qualitative and "per FOV" is undefined. Depth stays partial (introduction and methods not re-read).`

**D. Vigabatrin conditional question (the map row `IT30-CQ5` cites `#CQ-IT30-05`; in `context_it30_20261105/results/conditional_questions_it30.tsv` the vigabatrin row is `CQ-IT30-06` and `CQ-IT30-05` is rapamycin: an identifier mismatch to settle before the edit).**
Old (verbatim fragment of the `question` cell): `adverse: scn1lab larval zebrafish (LoF) | spontaneous seizures | endpoint: epileptiform event frequency, same assay`
New: `adverse (qualified): scn1lab larval zebrafish (LoF) | spontaneous seizures | endpoint: epileptiform event frequency, same assay; higher burst frequency in 6 of 7 fish at one bath concentration, no group test reported; the same paper's locomotion assay is opposite in sign (about -30 percent, not significant): aggravation untested, not shown`
Quote: "the scn1Lab cell reads 'adverse' without a qualifier; the paper supports 'higher burst frequency in 6 of 7 fish at one 1 mM bath concentration, no group test reported ...; locomotion assay opposite in sign and not significant'. It does not support a graded or tested aggravation. No WWOX content."
Not part of this candidate (SCI's map consumers, for the map owner): the WO-23 "nearest neighbour" line and the RS-NP4G1 "supplement read" line.

## 3 · What this does NOT do
* No claim, `PAPER` status, grade, ranking, compound card or portfolio row; no record reaches complete depth; no WWOX content is added (zero occurrences of the gene in the two non-WWOX papers).
* The coverage and reading-state surfaces already show the SCI receipts; regenerate after the batch only if the batch changes inputs.

## 4 · Statements for the blind check at propagation time
1. The three receipts exist in the ledger with the event ids, reasons and coverage maps stated above — surface: receipt ledger.
2. Table 1 and Table 2 are in the Dohare article, and "Tau" occurs zero times in its body — surface: article text (held artefact of the earlier receipt).
3. The Baraban supplementary PDF does not mention vigabatrin and Figure 6B shows the vigabatrin locomotion bar near -30 percent, not significant — surface: article figure and supplement (open-data bucket).


## BATCH DISPOSITION — `BATCH_20261124_003` (2026-11-24, ACTOR_ID `orchestrator`, MANUAL, mandate IT59), append-only

**Status:** PROPAGATED

5 record-scoped `replace-within` ops on `paper_registry_current.md` (PAPER 495 and PAPER 447 Evidence depth, two ops each; PAPER 157 dated update line), items A to C as proposed. Item D (vigabatrin cell of the conditional-question row) is NOT a registry edit: it goes by the ordinary route in the research map, with the identifier corrected to CQ-IT30-06 (the map row IT30-CQ5 cites CQ-IT30-05, which is rapamycin in the TSV).

# Proposed registry changes (candidate in the repository's vocabulary; nothing applied)

- **Status:** PROPOSED, NOT PROPAGATED. Non-canonical research note, not medical advice. Public edition, WWOX-DEE reference genotype class; only published literature, no individual-level record.
- **Author:** ACTOR_ID `orchestrator` (stated assumption), task `ORCH-SCIBATCH-DR-20261105`, branch `task/dr-parallel-20261105`.
- **Class:** MINOR as drafted (claim wording narrowed or extended, paper-record annotations; no baseline reversed, no block redefined). `target_wm_version` would be the next MINOR after the working-model version current at propagation. The class and version are the `BATCH_COMMIT` author's to confirm; the integrator decides whether CLAIM 031 and 042 changes reach MAJOR on reading.
- **Source material:** the five packages under `batch_sci_20261105/` with their `verify/` verdicts; `integration/VERIFICATION.md`. Locator audit: every row behind these proposals was blind-audited at least once; the narrowing edits listed there were not re-audited. The three claims touched are not `consolidated baseline` (CLAIM 001 `conflicting evidence`, CLAIM 031 and 042 `in observation`), so the audit trigger of the locator-audit skill is not mandatory, but it was done.

## 1 · Claims

**CLAIM 001** (vigabatrin and the MRI abnormality in WWOX-DEE; status stays `conflicting evidence`). Items from `a1_wwox_reports/module_inputs.md` section "proposed_registry_changes" item 1 (narrow the Chong 2023 sentence to the printed text; add Table 1 response codes for the Shaukat children; narrow the Riva wording to the printed phrases; add efficacy observations of three further reports; add the imaging boundary: brainstem or tegmental signal occurs in two WWOX children with no documented vigabatrin and is not the exposed pair's globus pallidus and thalamus pattern). From `b1_whitematter/module_inputs.md` section 5: three independent centres put the abnormality in imaged infants at 22.1 to 44.7 percent, about 26 percent per exposed child where the exposed denominator is given, and it occurs in children never exposed (7 of 52 in one cohort; 4 percent of naive infants in a controlled study), so a WWOX count without a denominator is not an excess; a hormonal co-therapy association is split (symptomatic form yes; imaging finding absent in two cohorts, present univariably in a third); no change of sign.

**CLAIM 031** (seizure control does not rescue development; status stays `in observation`). Narrow the title's universal to the record: in the published WWOX-DEE reports read, partial or transient seizure improvement was not followed by developmental gain in any of 4 children with both endpoints (null or splice classes, clinical narratives, short or undated follow-up); no sustained, instrumented response is recorded. Narrow `Genotype/model relevance` ("principle expected independent of genotype"): decoupling holds in genetic and structural strata and not in unknown aetiology, where a randomised developmental effect exists (A2 module inputs section 3, the strongest single proposal of the batch). Replace "the qualifier's scope is ambiguous and not resolved" with the better-supported of two readings and its residual ambiguity (A1 item 2). Add at abstract level that developmental delay was evident from birth in a seven-child series (PMID 42721537).

**CLAIM 042** (ketogenic diet in one five-patient series). Replace "two of the three diet responders are previously published individuals" with the finding of A1 item 3 (patient 4 stated; patient 2's credit variant-level and refuted cell-wise; the second previously published child most likely a non-responder: INFERENZA); replace "the developmental endpoint did not move in any column" with "the developmental row is a single status label in every column; no course is recorded"; the `REVIVAL_TRIGGER` (a Q230P carrier exposed to the diet) is met by two homozygous exposures with no attributable response, while the claim's own carrier is compound heterozygous and its statement about that carrier is unchanged; the exposed denominator remains not stated (minimum 3).

## 2 · Paper and corpus records (A1 items 4 to 13; A2 items 1 to 6)

Overlap and detail annotations on PAPER 017, 045, 143, 171, 018, 189 and 003 (and FT-114); new abstract-level records for PMID 42735667 (64-child vigabatrin cohort), 30061856, 42190144, and identity records for the other sources read beyond the abstract by A2 (all `partial_fulltext_read` or abstract, none complete); CORPUS P225 depth to abstract-only; full-text queue entries FT-110 (seven-child series, PMID 42721537; narrow its "five homozygous patients" wording: zygosity is not stated in the abstract), FT-114, and the two ICISS papers as queue candidates. No paper is registered as a completed reading: no staged receipt is a complete read. The R1, R2, B1 other-disease sources are not proposed as registry readings (they would inflate coverage counters without a WWOX claim); they live as rows and staged receipts.

## 3 · Discovery ledger leads (staged with the official tool)

`disease-models/wwox/research/lead_staging/orchestrator/lead_scibatch_postonset_white_matter.json` and `lead_scibatch_ube3a_mode_split.json` (both `IPOTESI`, validated by `discovery_lead.py check`); on `main`, `python3 framework/scripts/discovery_lead.py append --staged` numbers and appends them (dry run first).

## 4 · Negative findings with their reopening triggers (for the dismissal ledger, if the integrator keeps one entry per bounded null)

* "No post-onset sheath-morphometry precedent in a neuron-driven lesion", bounded searches R1 (34 queries) and R2 (32 queries) plus three reviewer searches, 2026-11-05/06; reopen when a post-onset arm with electron microscopy or g-ratio is published in a neuron-restricted lesion.
* "No post-onset interneuron count after gene restoration", same searches; reopen on such a study.
* "No sibling (CPP-115, OV329) white-matter measurement reachable", with the toxicology reports subscription-only; reopen when those reports are read.
* "No inactivator of this class given to a myelin-deficient or WWOX system" (B1 attestations B1-37, B1-38, queries in `b1_whitematter/queries.tsv`).

## 5 · Working model

No working-model sentence is contradicted by this batch. B1 proposes one added clause to the working-model sentence on the vigabatrin imaging abnormality (the same pattern occurs in other genetic encephalopathies, including one with a delayed-myelination baseline, so the co-occurrence with a hypomyelinating baseline is not WWOX-specific; the cohort that reports it may contain the two WWOX children and is not independent corroboration); apply only through `BATCH_COMMIT`.

## What was deliberately NOT done

No registry, ledger, claim, working-model or current-file edit; no receipt recorded; no PAPER record created; no dismissal entry written.

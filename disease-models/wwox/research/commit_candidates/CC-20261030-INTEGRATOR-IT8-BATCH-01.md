# CC-20261030-INTEGRATOR-IT8-BATCH-01
- **Class:** MINOR, wording and research-layer notes (ORDINARY). **No working-model statement is contradicted by the iteration-8 results, so no version bump: `target_wm_version` is `WM_v7.29` (preserved).** No claim created, reversed or promoted; no `Status`, `Type`, `Title` or `Summary` of any registry record changed; no hypothesis status or ranking changed, no support added. No individual-level data. Not medical advice; nothing here is a clinical recommendation.
- **Author:** ACTOR_ID `integrator` (Integrator worker for the orchestrator), mandate IT8, batch path, task branch `task/it8-batch`.
- **Source material (already in `main`, not re-enumerated):** `drug_repurposing/wwox_marginal_value_it8_p4_20261029/README.md` with `locator_audits/2026-10-30_it8_p4_verifier.md` (P4); `drug_repurposing/pharmacological_qualification_it8_p3_20261029/README.md` (P3); `drug_repurposing/advance_it8_p5_20261029/README.md` and its two loop READMEs (P5), with the five receipts `FTR-20261029-37804316-01`, `-41706892-01`, `-42587157-01`, `-42190665-01`, `-34253921-01`, already recorded in the receipt ledger.

## What changes and why
1. **The IT7 label 'WWOX-enriched' is a misnomer and is narrowed where it over-extends (P4).** The IT7 S3 condition added four HIF1A edges that were all already in the external network with the same sign (0 edges, 0 nodes, 0 signs); its 'no added value' says nothing about WWOX knowledge. Wording only, in `DL-MECH-174` (heading, causal statement, plus a dated CORRECTION bullet), `HYP-20260709-05` and `HYP-20261026-11` (the UPDATE bullets of 2026-10-29), the IT7 P6 results table and the IT7 P5 comparison README. Results, criteria, the pre-registration, the verdict words and the pilot history are untouched.
2. **IT8 P3 pharmacological qualification, as non-canonical dated NOTE bullets (no claim promotion):** stiripentol and LDH (no enzyme-level support, not proven absent) in `DL-REPO-004` and `HYP-20261026-11`; dichloroacetate and the PDK probe in `HYP-20260709-05`; phenylbutyrate salt against parent acid in `HYP-20260709-08`; memantine voltage pair in `HYP-20261027-01`; ethosuximide and apinocaltamide in `DL-MECH-170`. Bumetanide is carried by neither ledger (only the analysis map), so no ledger note was written for it.
3. **IT8 P5:** three discovery-ledger leads (`DL-MECH-175` ISR sign depends on the lesion; `DL-MECH-176` ATF4 protein rises with mGluR activity without an mRNA change, an activity control is required; `DL-MECH-177` post-onset restoration of circuit endpoints in Shank3 and Meis2, endpoint-class hypothesis), appended by `discovery_lead.py`; an UPDATE bullet on `HYP-20261026-10` adding the activity control and the potentiation arm to Stage 1, no status change (`HYP-20261026-11` is the LDH hypothesis, not an ISR one, and is not touched on this point); five new corpus stubs `CORPUS-STUB-190` to `-194` and literature-log rows `LIT-0840` to `LIT-0844`, each `partial_fulltext_read`, registry role OTHER_DISEASE_PRECEDENT, not WWOX evidence.
4. **Scout annotation:** the PMID 37804316 row of `drug_repurposing/scout_it7_20261029.md` carries the disputed Sephin-1 target (PMID 28447936, abstract level).

## What was deliberately NOT done, and why
- **P9 ranking note:** skipped. `drug_repurposing/ranking_it8_p9_20261029` is not in `main` yet (it lives on `task/it8-p9`); a pointer to an absent folder would be a dangling reference. To be added after P9 lands.
- **No working-model change, no claim registry change, receipt ledger untouched** (the five receipts were recorded earlier). `drug_repurposing/cards`, `needs`, `view` and `README.md` untouched (the `it8-p0b` task owns them).
- **No registry record for the compounds**, no ranking line, no card or need edit.

## Version rule (prompt_batch_commit section 7)
No statement in `working_model_current.md` changes, so no bump: `WM_v7.29` is preserved, the working-model history gets no row.

## Op lists
Record-scoped, dry run then `--apply`; refusals: none; `FULL_FALLBACK`: none. Paper registry 1 op (`append` of five stubs) and literature log 1 op (`append` of five rows), through `batch_commit.py propagate`; discovery ledger 6 `replace-within` ops and hypotheses ledger 7 `replace-within` ops, through `record_scoped_edit.py apply` (`propagate` accepts only the four current files); the three new leads through `discovery_lead.py append`. Working model 0 ops, claim registry 0 ops.

## BATCH DISPOSITION

**Verdict:** PROPAGATED (wording and research-layer notes; working model `WM_v7.29` preserved, no bump)
**Batch:** `BATCH_20261019_030` (2026-10-30, MANUAL, ACTOR_ID `integrator`, task `INT-IT8-BATCH-20261030`)

- **Misnomer narrowed:** `DL-MECH-174`, `HYP-20260709-05`, `HYP-20261026-11`, the IT7 P6 results table, the IT7 P5 comparison README.
- **P3 notes (non-canonical):** `DL-REPO-004`, `HYP-20261026-11`, `HYP-20260709-05`, `HYP-20260709-08`, `HYP-20261027-01`, `DL-MECH-170`.
- **P5:** `DL-MECH-175`, `DL-MECH-176`, `DL-MECH-177`; UPDATE on `HYP-20261026-10`; `CORPUS-STUB-190` to `CORPUS-STUB-194`; `LIT-0840` to `LIT-0844`.
- **Scout annotation:** `scout_it7_20261029.md`.
- **Skipped:** P9 pointer (target not in `main`); bumetanide ledger note (no ledger record carries it).
- **Unchanged:** every `Status`, `Type`, `Title` and `Summary`; the working model; the claim registry; the receipt ledger; the Status and ranking of every hypothesis touched.

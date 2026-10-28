# CC-20261027-SCIENTIST-C-ISR-01
- **Class:** ORDINARY (research layer; no consolidated baseline claim; no working-model change). **target_wm_version:** none. NOT WWOX EVIDENCE.
- **Source:** PMID 41380592, complete read, staged receipt `research/receipt_staging/scientist-c/FTR-20261027-41380592-01.json` (references not_read in the manifest; the optional key is omitted from the receipt coverage because a complete read may not carry not_read), manifest `deepdive_manifests/PMID41380592.json`, notes `drug_repurposing/isr_pars2_reading_it3_20261027.md` and `complex_i_ldh_pdh_it3_20261027.md`.
## Proposals for the integrator (in order)
1. Record the staged receipt (trial in a throwaway clone succeeded), then rebuild cards (`lucas_clarke_followup_20261026/build_cards.py` adds the PARS2 text and the E02 row only once the ledger holds the event), `check_cards.py`, `repurposing_join.py run`.
2. Apply `drug_repurposing/hypcurrent_it3_isr_20261027/ledger_edits.json` to the hypotheses ledger with `hypcurrent_20261027/apply_ledger_edits.py` (dry run: both edits apply once): HYP-20261026-10 precedent and Stage 1/2 design; HYP-20261026-11 readout addition. No status, ranking or direction change.
3. DL-MECH-173: append one sentence citing the precedent (genetic, partial, non-WWOX). Unchanged: R-10, R-11, DL-REPO-004, HYP-20260709-01/-05, E03, E04.
## Needs a verifier
Blind locator audit of the 19 figure attestations (plot readings, one reader); the Fig 6B key inconsistency.

## BATCH DISPOSITION

**Verdict:** PROPAGATED (research layer; `WM_v7.27` preserved)
**Batch:** `BATCH_20261019_024` (2026-10-28, MINOR, MANUAL, ACTOR_ID `integrator`, task `INT-IT3-BATCH-20261028`)

- **Proposal 1:** receipt `FTR-20261027-41380592-01` recorded by the orchestrator on 2026-10-28 (ledger 880 events, chain verified); cards rebuilt, `check_cards.py` and `repurposing_join.py run` re-run.
- **Proposal 2:** `hypcurrent_it3_isr_20261027/ledger_edits.json` applied to `HYP-20261026-10` and `HYP-20261026-11` after the blind locator audit (`locator_audits/2026-10-28_it3_pars2_blind_audit.md`: 29 of 30 body locators SUPPORTED, one wording OVERSHOOT, 19 figure readings agreeing). No status, ranking or direction change.
- **Proposal 3:** one UPDATE bullet on `DL-MECH-173` (genetic, partial, non-WWOX precedent), applied with `record_scoped_edit.py replace-within` because `batch_commit.py propagate` accepts only the four scientific current files.
- **Unchanged:** `R-10`, `R-11`, `DL-REPO-004`, `HYP-20260709-01/-05`, `E03`, `E04`.

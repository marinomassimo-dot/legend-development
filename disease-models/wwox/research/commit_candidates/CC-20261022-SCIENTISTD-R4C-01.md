# COMMIT CANDIDATE — CC-20261022-SCIENTISTD-R4C-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-d` (stated assumption of the Orchestrator), task `REPURP-R4C-D-20261022`, branch `task/R4-D-20261022`, 2026-10-22.
**context_policy:** `QUESTION_DRIVEN` (the group's five questions in `repurposing_batch_selection_20261021.md`). **Not medical advice.** Class-level statements only; no individual-level record.
**target_wm_version:** `WM_v7.24` · **Change class:** MINOR (registry presence for three precedent papers and completing receipts for six; one non-canonical card rewritten; no claim status, baseline claim or working-model block is touched).

## 0 · Why

The coordinator asked for (1) the card D01 exposure statement replaced by the audited recomputation, (2) the R4 HELD-partial rows closed where possible, (3) at most three new R4 precedent or design reports not in the registry. Details in `repurposing_r4c_scientist-d_20261022.md`.

## 1 · Ops

None. The card D01 is a file under `drug_repurposing/cards/` rebuilt from its packet by `repurposing_bridge.py` and checked by `check_cards.py` (12 packets, 0 problems); it is committed on this branch and is not a registry record.

## 2 · Registry presence proposed (placeholders; the integrator mints ids)

| Placeholder | PMID | Short title | Depth | Registry state found |
|---|---|---|---|---|
| R01 | 42542632 | Thiel 2026, oral zinc in GNAO1-related disorders, open-label pilot (substitute, precedent) | partial (protocol read in part) | no record |
| R02 | 42594875 | Aartsma-Rus 2026, eligibility for individualised antisense in neurodevelopmental disease, consensus (substitute, precedent) | complete | no record |
| R03 | 42494992 | Acosta 2026, outcome strategies for neuropaediatric rare disease trials, expert opinion (substitute, precedent) | partial (poster read in part) | no record |

Completing receipts (staged under `receipt_staging/scientist-d/`, each names its prior receipt, `reread_reason: inadequate_prior_coverage`): `FTR-20261022-38015929-02`, `-40162009-02`, `-41531035-02`, `-42446932-02`, `-42481851-02`, `-42286026-02`. New first receipts: `FTR-20261022-42542632-01`, `-42594875-01`, `-42494992-01`. All nine pass `staged_receipt_check.py` and their manifests pass `deepdive_manifest.py` strict with `--artifact-workspace` on the shared checkout.

## 3 · Claim-level observations (all MINOR; none narrows or reverses a baseline claim)

- Nothing here concerns WWOX; no claim in the registry carries a GNAO1, STXBP1, CLN2, CDKL5, KCNQ2 or SCN2A statement.
- Reading-queue entry for `36537114` (Chong 2023, FT-125): retried 2026-10-22, still closed (no open copy; publisher challenge not circumvented); the operator PDF wishlist item stands.
- Still owed, listed for the queue (supplements on disk, not read end to end): `35499850`, `39093319`, `41250984`, `39439575`, and the long protocols behind `39625912`, `39762914` and `41999155`.

## 4 · Staged leads (not appended to the discovery ledger); all `IPOTESI`

1. **Headline versus paired change in single-arm pilots.** In the GNAO1 zinc pilot the Summary's GMFM-66 and disability changes are differences of means over 12, 11 and 10 patients; the paired changes are about half. A repurposed-drug card should carry paired changes. Falsifier: a pilot whose Summary and paired values agree.
2. **A non-disease external comparator moves the effect size.** The cerebral palsy comparator cohorts of that pilot come from an active rehabilitation programme; the main text restricts to 8 treated children where the appendix uses 10. Falsifier: a disease-specific natural-history comparator showing the same direction.
3. **The N-of-1 framework's nanorare cut (under 30 patients) fits private alleles, not the WWOX class.** Falsifier: a WWOX allele class with fewer than 30 known carriers for whom the consensus statements would apply.

## 5 · Shared surfaces left to the Orchestrator

`pathograph`, `batch_queue`, `coverage_report` and `reading_state` not regenerated (commits carry `LEGEND_STALE_SURFACES_BECAUSE`). The four scientific current files, `full_text_queue_current.md` and the ledger are untouched. `drug_repurposing/p5/` carries its own copy of the A51 "supralinear" wording (another actor's directory), named for the Orchestrator.

### LOCATOR TRIPLES FOR BLIND AUDIT
49 triples audited blind by a separate agent: 45 SUPPORTED, 4 not (1 NOT_IN_SOURCE, 3 OVERSHOOT); all narrowed before landing, `contradicts_locator` on the three already-committed entries; record in `page_adjudications/locator_audit_R4c_20261022.md`.

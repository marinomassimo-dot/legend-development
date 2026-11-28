# COMMIT CANDIDATE — CC-20261128-ORCHESTRATOR-ADV302-309-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (SCI ADV-302 J1 to J8, closed records C1 and C2, retraction ADD for PMID 26041563; SCI ADV-309 W1 to W4) · **Date:** 2026-11-28 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin:** SCI's `SENTENCES_FOR_IT_ADV302_SCI_20261128.md`, `SENTENCES_FOR_IT_CLOSED_ADV302.md`, `SENTENCES_FOR_IT_ADV309_SCI_20261128.md`. **Checks:** two blind rounds by `legend-delegate` (sonnet, effort high stated), packets and reports in `adv302_309_consumers_it30_20261128/`. **Status:** PROPAGATED in `BATCH_20261128_005`.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice. Reference genotype class only.

## 1 · CHANGE CLASS
**MINOR, no version bump.** Wording narrowed to what the held sources print: DL-MECH-049 (J1 to J8; title now hedged), DL-MECH-027 (title and body: neurons not "intact"; rescue is a hypothesis), CLAIM 036 (three fields: chemistry is P18 only, EIIA-Cre), CLAIM 014 (ages and tissues sampled), CLAIM 005 (hippocampus, two weeks, one study), DL-MECH-008 and DL-MOL-004 (abstract-level notes), and the retraction of 26041563 (Mol Cancer 19:126, 15 August 2020, Figs 2 and 3, vinculin loading controls) in DL-MECH-025, FM-006, `disease_model.md` and `working_model_current.md`. Zero scientific delta for the working model: the cluster was already declared retracted and not baseline-supporting; no claim created, reversed or promoted; no status or grade changed.

## 2 · Where the full text is
`ops_claims_w309_it30.json` (claim registry, 5 ops), `ops_working_model_current_it30.json` (1 op), `ops_disease_model_it30.json` (one fragment), `edits_302_it30.py` and `edits_ledger_w309_it30.py` (exact-once fragments), `apply_it30.py`.

## 3 · Checks and what they changed
Round 1 rates with denominators: ADV-309 sentences 2 of 8 MUST CHANGE; ADV-302 items 6 of 11 (5 substantive). Round 2 on the repairs: 0 of 11 and 0 of 3 MUST CHANGE. See `BLIND_REPORTS_AS_DELIVERED_ADV302_309_IT30.md`. Not applied by design: the producer's findings outside the four W (`meta_gaba_paradox_current.md` line 23 "P14-P18", DL-MECH-027 "Wwox non serve a ... migrazione" against Iacomino's P1 migration defect, DL-MECH-049 "Conferma e meccanizza DL-MECH-017", ledger line 566 D-04, the first quotation in the DL-MECH-049 head block, the generated join files): listed for a later increment.

## BATCH DISPOSITION — `BATCH_20261128_005`, append-only
**Status:** PROPAGATED (claim registry and working model by `batch_commit.py propagate`; the rest by exact-once fragment replacement, `apply_it30.py`). MINOR.

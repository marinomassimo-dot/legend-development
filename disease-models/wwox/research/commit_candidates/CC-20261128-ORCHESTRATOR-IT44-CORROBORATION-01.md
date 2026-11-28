# COMMIT CANDIDATE — CC-20261128-ORCHESTRATOR-IT44-CORROBORATION-01

**Actor:** `orchestrator` (IT, successor 44) · **Task:** ORCH-ROADMAP-IT59-20261119 (corroboration-independence batch, ADV decision of 2026-11-28) · **Date:** 2026-11-28

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice.

## 1 · CHANGE CLASS
**MINOR, no version bump.** Records `CLAIM 014`, `025`, `028`, `030`, `036`, `038`; seven record-scoped operations (`ops_corroboration_it44.json`). No status, direction or working-model statement changes; `target_wm_version` stays `WM_v7.29`; no ranking, need or candidate-state change.

| Record | Change | Kind |
|---|---|---|
| `CLAIM 014`, Evidence boundary | «multi-paper convergence» is the convergence of one collaboration; only PMID 32581702 observes development before birth in its own material | **edit** (SCI second reader FAILS, judgement call; SCI HOLDS under the frozen rule) |
| `CLAIM 030`, severity sentence | Steinberg poses a question; family identity with PMID 24369382 not stated; «(null)» is read from the genotype (no patient protein measurement in PMID 24456803) | **edit** (additions; sentence kept) |
| `CLAIM 036`, qualification | PAPER 075, 076, 078 are one laboratory line; the independent pair is with PAPER 057 | **edit** |
| `CLAIM 025` | «confirmed in vivo» names no first source (`CORPUS P191`, `Identifier: PENDING`) | dated pointer, sentence unchanged (UNSETTLED) |
| `CLAIM 028` | three of four papers of the «convergence» are `Identifier: PENDING` placeholders | dated pointer, sentence unchanged (UNSETTLED) |
| `CLAIM 036` rat half, `CLAIM 038` | rat texts (PMID 19500159, 17803050) not held; independence of the rat half not re-checkable | dated pointers (UNSETTLED) |

Already repaired, not edited again: `CLAIM 030` corroboration paragraph (`BATCH_20261128_013`).

## 2 · Sources
`drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/corroboration_independence_sci_20261128/` (SCI BI) and `…/corroboration_independence_it_20261128/` (`RESULT_CORROBORATION_BATCH_IT44_20261128.md`, nine receipts). Operation list `ops_corroboration_it44.json`.

## 3 · Blind reader on the composed text
Sixteen atoms: 13 supported, 1 not supported as first worded (A7, reworded), 2 unsettled (C2, D2, written as pointers). See the RESULT. The reworded sentences were not sent a second time.

## 4 · Cards
`copied_card_sentences.py --base <old tip>` is run before landing (result in the landing note). RP rows `RP-017` and `RP-019` name `CLAIM 030` or `CLAIM 036`; not edited (ADV owns the rows).

## BATCH DISPOSITION — `BATCH_20261128_014`, append-only
**Verdict:** PROPAGATED (six claim records; working model `WM_v7.29` preserved)
**Status:** PROPAGATED by `batch_commit.py propagate`. MINOR.

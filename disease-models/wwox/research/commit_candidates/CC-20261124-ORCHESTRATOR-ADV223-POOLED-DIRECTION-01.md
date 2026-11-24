# COMMIT CANDIDATE — CC-20261124-ORCHESTRATOR-ADV223-POOLED-DIRECTION-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (ADV-223, pooled-direction sweep) · **Date:** 2026-11-24 · **target_wm_version:** `WM_v7.29` (a patch-level wording change, no claim, status, grade or ranking changes)
**Origin of the findings:** `advisor_pilot_20261113/brainstorm_20261116/it_adv223_20261124/RESULT_ADV223_IT_20261124.md`, section 3, rows 5, 6 and 7 (sentence-level sweep of the claim registry, the working model and the paper registry, pre-registered in `PREREG_ADV223_IT_20261124.md`).
**Status:** PROPOSED, for the next `BATCH_COMMIT` that the queue triggers. No registry or working-model file is edited by this act.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice.

## 1 · CHANGE CLASS (stated before any apply)
**PATCH (wording only).** Three working-model lines gain a qualifier that the claim record they cite already carries. No claim, working-model sentence of the baseline, status, type, grade, ranking row or compound card changes meaning; the guards on `CLAIM 002` (pooled-only clause) and `RP-043` are not touched.

## 2 · What and why
The sweep found three working-model lines that join mechanisms or systems under one word while the claim record behind each states the direction or the system limit. Each is a **mirror or prose line** whose own record omits the caveat, so a reader of the working model alone gets the pooled sentence.

## 3 · Proposed wording (old verbatim, new)
**A. `working_model_current.md`, BLOCK 2 row 025.**
Old (verbatim): `| 025 | WWOX/HIF1A ratio as a systems-level state marker linking glycolysis, inflammation and Wnt-adjacent signalling | DATO+INF | P5 / state transition | T2 conceptual | in observation | paper 191 |`
New: `| 025 | WWOX/HIF1A ratio as a systems-level state marker linking glycolysis, inflammation and Wnt-adjacent signalling — ⚠️ the direction is context-dependent, not a property of the marker (CLAIM 025) | DATO+INF | P5 / state transition | T2 conceptual | in observation | paper 191 |`
Pattern: the same marker row 009 already carries (`⚠️ counter-directional evidence recorded (CLAIM 034)`).

**B. `working_model_current.md`, section "Metabolic branch refinement".**
Old (verbatim sentence): `The WWOX/HIF1A axis appears to act as a broader **state indicator** linked to glycolysis, inflammatory tone, Wnt-related signalling and possibly state-transition biology.`
New: the same sentence followed by: `The direction is context-dependent (a low ratio is the maladaptive state in gestational-diabetes leukocytes; in the cancer-subtype survival data the association runs both ways and is descriptive only), so it is a state indicator, not a severity scale (CLAIM 025).`

**C. `working_model_current.md`, BLOCK 3, `TX-007` line.**
Old (verbatim fragment): `on a tumour suppressor whose induction is pro-apoptotic,`
New: `on a tumour suppressor whose overexpression is pro-apoptotic in cancer cell lines and whose direction in stressed neurons is unresolved (CLAIM 044),`

## 4 · What this does NOT do
* No claim, `PAPER` record or ranking row changes; `CLAIM 009`, `CLAIM 025`, `CLAIM 034` and `CLAIM 044` are not edited (they already carry the caveats).
* The three ADV-218 stubs and records are not touched here; when they become records each should carry its system and direction in the first line (RESULT section 4).
* Nothing imported over a held quantified reading (no review-level compression).

## 5 · Statements for the blind check at propagation time
1. The claim record `CLAIM 025` states that directionality is not a property of the marker (low ratio maladaptive in gestational-diabetes leukocytes; cancer-subtype survival association in both directions, described by the authors as descriptive and hypothesis-generating) — surface: claim registry, Summary.
2. The record `CLAIM 044` states that the direction of WWOX activity in stressed neurons is unresolved and that the measurement is of activated WWOX gain under stress, transferability T3 — surface: claim registry, title and Summary.
3. The proposed fragment "overexpression is pro-apoptotic in cancer cell lines" is supported by a held record that reports cell-line overexpression with apoptosis readouts (for example the A549 overexpression record) — surface: paper registry, Role field.

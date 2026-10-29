# CC-20261029-INTEGRATOR-IT6-WM-01
- **Class:** MINOR, working-model wording. **`target_wm_version` is `WM_v7.29`** (bump from `WM_v7.28`). No claim created or reversed, no `Status`, `Type` or `Summary` changed; no individual-level data. Not medical advice.
- **Author:** ACTOR_ID `integrator` (Integrator worker for the orchestrator), mandate IT6, task branch `task/it6-batch`.
- **Source:** finding D1 and section R8 of the adversarial review of `BATCH_20261019_027` (`research/locator_audits/2026-10-29_it6_batch_review.md`), each statement re-checked against the cycle verifier reports (`2026-10-29_it6_p7_verifier.md`, D1 and D2; statement 2 and 3) and the claim wave notes already registered.

## What changes and why
1. **Line 'critical early postnatal window (P0-P5 in mouse)' (Design principles, gene therapy context).** It turns the ages tested into a measured window. The main cohorts were injected at P0-P1 and the timing arms at P1-P5 (no P0 arm, no P4 survival curve, a P3 arm at about 67 percent and a P5 arm at 75 percent), and the authors write that later intervention was not explored and that this is not 'a definitive boundary for therapeutic responsiveness' (`CLAIM 011`, `DL-MECH-011`, `DIS-033`). New text: 'early postnatal window tested (P0-P5 in mouse: ages tested, not a measured boundary)'.
2. **Three 'durable rescue' lines on AAV9-hSynI-hWWOX** (DATA, section 4, gene therapy context) gain '(early-window prevention in the null mouse; no after-onset mouse arm)'. They sat beside 'early postnatal' wording but the qualifier of the claim wave notes did not reach the model.
3. **'The therapeutic window is generally considered still open in early childhood; plasticity at age ~3 is plausible, not guaranteed'** gains an explicit premise tag (`PREMISE_TAG: DEFAULT_FROM_TEXTBOOK`; unsourced, outside the mouse evidence). The sentence is not changed.
4. The narrative view `disease_model.md` is aligned (its three matching lines).

## Version rule (prompt_batch_commit section 7)
MINOR: a block update without a policy change; no baseline claim reversed, no `Status`, `Type` or `Summary` touched. `Version` becomes `WM_v7.29_2026-10-29`, the single `Last update` line of the hot file is replaced by this batch's, the previous note stays in `working_model_history.md`, which gains the new `Last update` note and a Changelog row; the state manifest `working_model_version` and `target_wm_version` become `WM_v7.29`.

## Op lists
7 record-scoped ops on the working model through `batch_commit.py propagate` (dry run, then `--apply`); the history file takes 2 further ops through `record_scoped_edit.py` (a `Last update` note and a Changelog row, text in the file); claim registry, paper registry, literature log, ledgers: none.

### working_model_current.md (7 ops)
```json
[
 {
  "op": "replace-within",
  "heading": "WWOX loss-of-function (WOREE / WWOX-DEE) — disease-level working model",
  "old": "**Version:** WM_v7.28_2026-10-29",
  "new": "**Version:** WM_v7.29_2026-10-29"
 },
 {
  "op": "replace-within",
  "heading": "WWOX loss-of-function (WOREE / WWOX-DEE) — disease-level working model",
  "old": "**Last update:** 2026-10-29 — `BATCH_20261019_025` (**MINOR** — MANUAL, ACTOR_ID `orchestrator` by stated assumption, operator authorisation): one candidate pro [... the whole previous Last update line, replaced; its text is kept in working_model_history.md]",
  "new": "**Last update:** 2026-10-29 — `BATCH_20261019_028` (**MINOR** — MANUAL, ACTOR_ID `integrator`, task INT-IT6-WM-20261029): one candidate propagated (`CC-20261029-INTEGRATOR-IT6-WM-01`), from finding D1 and the R8 section of the adversarial review of `BATCH_20261019_027` (`research/locator_audits/2026-10-29_it6_batch_review.md`). **No claim created or reversed, and no `Status`, `Type` or `Summary` changed anywhere.** (1) **The 'Design principles' bullet of the gene therapy context no longer calls P0-P5 a 'critical early postnatal window'.** It now reads 'early postnatal window tested (P0-P5 in mouse: ages tested, not a measured boundary)': the main cohorts were injected at P0-P1 and the timing arms at P1-P5, the P3 and P5 arms lost animals, there is no P4 survival curve, and the authors write that later intervention was not explored and that this is not 'a definitive boundary for therapeutic responsiveness' (`CLAIM 011` wave note, `DL-MECH-011`, `DIS-033`). (2) **The three 'durable rescue' lines on AAV9-hSynI-hWWOX** (DATA, section 4, gene therapy context) now carry '(early-window prevention in the null mouse; no after-onset mouse arm)': every endpoint is measured after neonatal treatment of animals never measured before it, and the only after-onset add-back read in the corpus is organoid. (3) **The sentence that the therapeutic window is 'generally considered still open in early childhood; plasticity at age ~3' carries an explicit premise tag** (`PREMISE_TAG: DEFAULT_FROM_TEXTBOOK`, unsourced in this model; the sentence itself is unchanged). The narrative view `disease_model.md` is aligned. The iteration-6 research-layer results stay in the claim wave notes and ledgers of `BATCH_20261019_027`. Not medical advice."
 },
 {
  "op": "replace-within",
  "heading": "DATA (WWOX literature)",
  "old": "including ECoG/SWD reduction (Obeid 2026). 🔴 **Not a graded continuum",
  "new": "including ECoG/SWD reduction (Obeid 2026) (early-window prevention in the null mouse; no after-onset mouse arm). 🔴 **Not a graded continuum"
 },
 {
  "op": "replace-within",
  "heading": "4) Note on missense alleles and gene therapy",
  "old": "myelination, gliosis, SWD/ECoG. 🔴 **\"Dose calibration\" here",
  "new": "myelination, gliosis, SWD/ECoG (early-window prevention in the null mouse; no after-onset mouse arm). 🔴 **\"Dose calibration\" here"
 },
 {
  "op": "replace-within",
  "heading": "Gene therapy context",
  "old": "neuron-specific targeting; early postnatal ICV delivery. P7 design principles",
  "new": "neuron-specific targeting; early postnatal ICV delivery (early-window prevention in the null mouse; no after-onset mouse arm). P7 design principles"
 },
 {
  "op": "replace-within",
  "heading": "Gene therapy context",
  "old": "plasticity at age ~3 is plausible, not guaranteed.",
  "new": "plasticity at age ~3 is plausible, not guaranteed. `PREMISE_TAG: DEFAULT_FROM_TEXTBOOK` — an unsourced expert-sentiment sentence outside the mouse evidence; this model holds no source for plasticity at age ~3."
 },
 {
  "op": "replace-within",
  "heading": "Gene therapy context",
  "old": "controlled dose; critical early postnatal window (P0–P5 in mouse).",
  "new": "controlled dose; early postnatal window tested (P0–P5 in mouse: ages tested, not a measured boundary)."
 }
]
```

## Proof
`framework/scripts/test_repurposing_join.py::SupersededWordingGoneIT6` (extended): the working model no longer contains 'critical early postnatal window', carries the tested-ages wording, the three early-window-prevention qualifiers and the premise tag, keeps its Status lines, and its version equals the one the state manifest declares.

## BATCH DISPOSITION

**Verdict:** PROPAGATED (working-model wording; MINOR, `WM_v7.29`)
**Batch:** `BATCH_20261019_028` (2026-10-29, MANUAL, ACTOR_ID `integrator`, task `INT-IT6-WM-20261029`)

- **Window wording and early-window qualifiers:** propagated to `working_model_current.md` (Design principles, the three durable-rescue lines), `working_model_history.md` and `disease_model.md`.
- **Premise tag:** propagated to the therapeutic-window sentence.
- **Unchanged:** every `Status`, `Type` and `Summary`; every claim; the ledgers; the receipt ledger.

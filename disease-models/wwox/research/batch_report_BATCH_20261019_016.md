# BATCH COMMIT REPORT — BATCH_20261019_016

## Summary

- **Type:** MANUAL (ACTOR_ID `integrator`, assigned by the Orchestrator). One job.
- **WM version:** `WM_v7.27` → `WM_v7.27` — **preserved**, as in batches 009 to 015. No disease-model
  change: no claim was created, reversed or narrowed, no `consolidated baseline` record was touched,
  and no `Status`, `Type`, `Summary`, block or baseline changed anywhere.
- **Commit candidates propagated:** 1 — `CC-20261021-SCIENTIST-C-R3-A51-ATTRIBUTION-01`, MINOR additive.
- **Change class:** MINOR, additive, in one record of one append-only ledger.
- **Snapshot:** `backup/20261024_batch016` · **pre-batch commit:** `8050597d962f5881d4c16c0d7ff1d6f8fcc63d81`
- Not medical advice. No dose, administration route, schedule or suitability statement was written.

## Why the candidate moved, and how that was verified

The candidate had been `DEFERRED` since 2026-10-22 under **one** condition, written in its own header:
*HELD from propagation until the repaired manifests are audited by someone other than the producer.*
Nothing else about it had changed. The integrator verified the condition **first-hand against both
audit files** rather than on the assigning actor's word:

| Proposed addition | Sources | Audit file, by a different auditor | Result |
|---|---|---|---|
| 1 (attribution) · 2 (CK1-alpha direction) | 38147624, 40156289 (and 40665325, from which nothing is carried) | `page_adjudications/locator_audit_R3_repairs_R3b_20261022.md` | all **11 of 11** repaired entries of 40156289 held; **7 of 8** repaired entries of 38147624 held; the eighth (`entry 21`, lane reading) a **minor `OVERSHOOT`** |
| 3 (BLOCK-1, second and third reason) | 42154236, 42401046 | `page_adjudications/locator_audit_block1_sources_20261024.md` | **exhaustive over both manifests: 43 triples judged, 43 `SUPPORTED`, 0 adverse, 0 `UNVERIFIABLE`**; both named propositions `SUPPORTED AS WRITTEN`; **2 anchor-level defects** (a supplementary-figure numbering mix-up; a wrong ppi note), every content statement verified against the files named |
| 4 (missing measurements) | — | not an evidential claim | landed as **unblocking items, not novelty claims** |

**The one adverse verdict and how it was handled.** `38147624` entry 21 is a minor `OVERSHOOT`: the
auditor confirmed the absence of a Myc band at the highest-burden lane and the bands at the four lanes
the entry names, and flagged only that *"none visible"* at **two intermediate lanes** was slightly too
strong. Proposed addition 1 uses the confirmed part; the entry's later restatement of those two lanes is
the producer's own and is **unaudited**, so **no statement about them was carried**. The landed block
says so inside itself.

## Files modified

| File | What |
|---|---|
| `disease-models/wwox/research/discovery_ledger_current.md` | **one dated additive block inside `DL-THER-089`** — attribution and BLOCK-1 notes only. `record_scoped_edit.py replace --id "DL-THER-089"`, **14 insertions, 0 deletions**, no `FULL_FALLBACK`; every byte outside the addressed record provably unchanged |
| `disease-models/wwox/research/discovery_ledger_history.md` | one change-log row (append only) |
| `disease-models/wwox/research/commit_candidates/CC-20261021-SCIENTIST-C-R3-A51-ATTRIBUTION-01.md` | `## BATCH DISPOSITION` rewritten to `PROPAGATED` with the earlier `DEFERRED` disposition kept below it; header `STATUS` corrected with the superseded wording quoted in the line (`prompt_batch_commit.md` § 7.2) |
| `framework/state/state_manifest_current.md` | § 4 last-batch block, § 5 LINT block. `working_model_version`, `last_wm_update` and `last_wm_batch_commit_id` **preserved** |
| `framework/state/state_history.md` | `batch_20261019_016_scope` and `_candidates` at the top of § 4 |

## Files unchanged

All four scientific current files (`working_model_current.md`, `claim_registry_current.md`,
`paper_registry_current.md`, `literature_tracking_log_current.md`), `working_model_history.md`,
`disease_model.md`, the `meta_*` files, the research lines and candidates, the biomarker and endpoint
files, `therapeutic_strategies_current.md`, the dismissal ledger, the therapeutic-hypotheses ledger, the
full-text queue, the receipt ledger (**no receipt recorded, none re-pointed: this batch propagated no
reading and created no staging draft**), every deep-dive manifest (they were correct; nothing was
edited), the DisMech sidecar and its seal (**no sealed claim touched**), and every `PAPER`, `LIT` and
`CORPUS` record (**none created**).

## What landed in `DL-THER-089`, and the caveats that travel with it

- **(a)** The **Wnt-versus-MYC-versus-CDK attribution stays unresolved**, and the `Csnk1a1` leukaemia
  system does not resolve it. `INFERENZA` that the A51 effect there is Myc-mediated is **not supported**;
  `IPOTESI` at most. This is the candidate's own first proposed addition, landed as written.
- **(b)** Direction of the CK1-alpha arm, as a **premise to test**: `IPOTESI`, with
  `PREMISE: INFERENZA` on the HEK-293T result and `PREMISE: DEFAULT_FROM_TEXTBOOK` on reading A51 as a
  Wnt suppressor. Its three audited limits travel with it (authors' expectation, not a measured
  loss of function; endogenous status not stated and no empty-vector arm; the variant-to-family
  assignment an unresolved conflict inside the source).
- **(c)** BLOCK-1 gains a second and a third reason, **with the caveats attached to the claims and not
  to a footnote**, so a reader of the entry cannot miss them: the Cdk7 morphology result is written with
  **n = 3 per genotype under a one-sided Mann-Whitney whose smallest attainable value is P = 0.05** and
  with the **one-sample-per-age-and-genotype** blots, and with **no EEG** (those strings do not occur in
  that article at all); the GSK3 arm is written as **histology and immunohistochemistry at day 14 only,
  one dose level, adult mice, no EEG and no spontaneous-seizure or seizure-burden endpoint**.
- **(d)** The missing measurements are recorded as **unblocking items**, with no assertion that any of
  them is absent from the literature at large.
- The candidate's **`REVIVAL_TRIGGER`** is recorded verbatim: a measurement of A51 in a **neural** system
  with an **attribution control** (a CDK7/9-selective arm and a CK1-alpha-selective arm).
- 🔴 **Every source in the block is labelled `NOT WWOX EVIDENCE`.** None is a WWOX experiment and none is
  an A51 experiment in neural tissue. The BLOCK-1 therapeutic-window question of the entry — a
  dose-response with a treated wild-type arm — stays **open and unanswered**.

## Two counts of the candidate were not reproduced

Both divergences are written inside the landed block, so a reader of the ledger sees them without
opening the candidate:

| Candidate wrote | Audited entries carry | What was written |
|---|---|---|
| addition 1: *"one of five concentrations"* | the entry names **four** concentrations | *"only one of the four concentrations the audited entry names, the highest of them"* |
| addition 3: *"two of four remodelling markers"* in the unilateral model | **three of four** — dispersion, migration and the contralateral cell-count increase, the ipsilateral count unchanged | the audited enumeration |

Neither is adverse to the candidate: the first is a miscount, the second is conservative. Neither was
reproduced.

## Held, and still held

- 🔴 **Nothing whatsoever is carried from `40665325`** (adult phase 1). Its **dose-proportionality table**
  entry is the one entry of that manifest the blind audit left `OVERSHOOT`, and **no dose-proportionality
  sentence, and no dose, route, schedule or suitability sentence of any kind, exists in anything this
  batch wrote** — in the ledger, the candidate disposition, the manifest, the history or this report.
- **`CC-20261021-SCIENTIST-A-R1-PROTEOSTASIS-01` stays deferred**, evidence unchanged. It is named here,
  in the batch report, and **deliberately nowhere in the manifest or its history**, because naming a
  candidate in a batch scope closes it whatever the sentence around the id says
  (`prompt_batch_commit.md` § 7).

## Conflicts resolved

None. One candidate, one target record, no other candidate addressing `DL-THER-089`.

## Gates

`legend_lint.py` WARN with **no BLOCK** before and after · `growth_anchors.py check` · `fulltext_receipts.py verify`
· `public_release_gate.py` PASS · derived surfaces regenerated and fresh · the locator-count suite re-run
**last**, because `main` moves under a batch. Figures are in the task ledger
`ledger/tasks/integrator/BATCH_20261019_016.json`.

## Recommended next actions

1. The `REVIVAL_TRIGGER` above is now a recorded, checkable condition on this lead — a literature sweep
   for an A51 experiment in a neural system with an attribution control is the cheapest next move.
2. `CC-20261021-SCIENTIST-A-R1-PROTEOSTASIS-01` is still held on **unaudited producer repairs**: the same
   discharge route that moved this candidate applies to it the moment a non-producer audit exists.
3. The discovery-ledger change-log carried **no row between 2026-07-05 and this batch** while the ledger
   itself grew by 24 run sections. That gap is pre-existing, was not repaired here, and is worth a
   harness decision: either the header's append rule binds every writer, or it should stop claiming to.

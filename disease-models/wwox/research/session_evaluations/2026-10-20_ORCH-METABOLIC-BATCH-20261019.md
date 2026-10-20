# Orchestrator self-evaluation — metabolic batch ORCH-METABOLIC-BATCH-20261019

Identity: `orchestrator`, a stated assumption recorded in the task record. Not medical advice.
Public edition, class level. Scope: coordination of four waves of reading by up to four Scientists
(about 170 full-text readings), seven batch commits (BATCH_20261019_001 to _007, WM_v7.20 to
WM_v7.26), three Mirror reviews, one push to the development repository.

## Part 1 — executable verdict

| Check | Result (2026-10-20, main after batch 007) |
|---|---|
| `session_self_eval.py --workspace . --disease wwox` | PASS — every complete read landed, every declared output resolves; unread premises 0/0 |
| `fulltext_receipts.py verify` | OK, 680 chained, tail anchored |
| `legend_lint.py .` | WARN, 0 BLOCK (pre-existing UNLINKED_SUPPORT warnings only) |
| `public_release_gate.py` | PASS, 0 blocks |
| Release battery on a fresh clone of the pushed ancestor | 143 of 144 suites green; the one red (verbosity of a new test) fixed and re-verified before the push; the final battery on the very last SHA was not re-run in full |

Declared gaps listed by `session_self_eval.py` belong to older manifests (waived slots, ratchets);
none names a reading of this batch.

## Part 2 — judgement

| Dimension | Answer, with anchor | Grade |
|---|---|---|
| Did the batch answer the operator's question? | For every requested theme and intervention the answer is a measured negative: no study measures the theme in a WWOX-deficient system. The negative is specific and carries the missing assay (batch reports; Scientist notes `metabolic_wave_*`, `interventions_wave_*`, `wave4_*`). | strong |
| Source parity and lawful bodies | Paywalled targets were parked with the cascade run, never circumvented; the operator's PDF wishlist is in the closing report. | strong |
| Substitutes labelled | Every non-WWOX record carries NOT WWOX EVIDENCE; Mirror sampled and confirmed (reviews 003–005 and 006). | strong |
| Delegation discipline | Selectors read-only, Scientists on branches, receipts staged and recorded by me in event-ID order after a scratch-clone trial (seven times); integrators ran under the legend-commit procedure. | strong |
| Own errors | See attribution below. | partial |
| Persistence | Task record `ORCH-METABOLIC-BATCH-20261019` carries the queue, DEFAULTS_TAKEN and DECISIONS_TAKEN; mandate verdict reconciled before ending. | strong |

## Attribution — who caught what

| Incident | Caught by |
|---|---|
| Staged receipts with future `analysis_at` (eleven in the first set, thirteen in the last) | machine — the writer refused in the scratch-clone trial |
| Stray state-manifest anchor (543 events, ledger 542) blocking LINT and landings | machine (LINT) and a subagent; classifier refused my own restore until the operator authorised it |
| Battery reds after landing new tools (missing `verbosity=2`, missing executable bit, a registry depth line) | machine — release battery and `test_batch_queue` |
| Provenance ceiling exceeded by re-read manifests | machine — `test_manifest_receipt_provenance`; the root cause (re-acquired bytes) was found by the harness agent, not by me |
| Sathe/Stevering "disagree" sentence in a claim note and a lead | Mirror (BLOCK-class repair B1), confirmed against source by the repair agent |
| My own harness brief asked for a narrow fix; the agent's rule also reclassified five older cases and lowered the ceiling 15 → 9 | caught at hand-back by me, then reviewed by Mirror (finding B2); disclosed to the operator |
| Two wording fragments tripped the public gate (a parent-side term in a dossier, the phrase "parent-of-origin" in a review) | machine — `public_release_gate` |

`undetected_known`: 0 is the limit of this census, not a clean bill: no blind audit ran on the
orchestrator's own decisions.

## Weakest answers, and the upgrade that answers them

1. **The receipt-recording procedure was done by hand seven times** — list the unrecorded staged
   receipts, repair future timestamps, trial in a clone with a hard-linked evidence tree, record in
   order, copy back, regenerate surfaces. The first trial used a symlink and failed for a reason
   that was not the receipts. **Upgrade shipped:** `framework/scripts/record_staged_receipts.py`
   with `test_record_staged_receipts.py` (4 offline tests), a routing row in
   `framework/scripts/README.md`, and enrolment in `scripts/run_release_regressions.py`.
2. **I briefed the harness agent narrowly and did not forbid reclassifying older cases**; the
   result was sound but wider than I asked. Next brief states what must not change, not only what
   to change. (Process note, no code.)
3. **I did not run the whole battery on the very last SHA before the push**; I ran it on the
   ancestor and re-ran the one failing suite. Stated here rather than hidden.

## Open items for the operator

- Papers registry about 1.54 MB, past the +25 percent re-raise point; sharding or an event store
  is the operator's decision; a third deferral is refused.
- PDF wishlist (closing report).
- Harness decision `SUPERSEDED_ARTIFACTS` (ceiling 15 → 9 by reclassification) — reversible,
  recorded in the provenance docstring and protocol amendment.

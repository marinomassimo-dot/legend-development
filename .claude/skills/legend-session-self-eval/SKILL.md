---
name: legend-session-self-eval
description: Mandatory post-batch self-diagnosis for LEGEND. Runs the executable gate (session_self_eval.py, deepdive_manifest.py, fulltext_receipts.py verify, legend_lint.py), then forces the written judgement diagnosis using the batch template, and turns every weak answer into a proportional micro-upgrade. Use after the analytical work and BEFORE legend-capability-scout and legend-session-takeaways — takeaways written first will describe a session that went well. Trigger it for "autovalutazione", "self-evaluation", "how did the process run", "diagnosi di sessione", "valuta il batch", or at the close of any batch or completed full-text read.
---

# LEGEND — session / batch self-evaluation

This skill is a **dispatcher, not a second source of truth.** The questions, the rationale and
the rule all live in [`framework/protocols/session_self_evaluation.md`](../../../framework/protocols/session_self_evaluation.md);
the written answers go in [`framework/protocols/batch_self_evaluation_template.md`](../../../framework/protocols/batch_self_evaluation_template.md).
Read the protocol — do not paraphrase it from here.

## Why a skill on top of a protocol

Because the protocol already existed and was **not run**. On 2026-07-26 a session completed a
full-text deep dive, wrote a tidy summary reporting that the process had gone well, and never
executed `session_self_eval.py` — which was in the repository, with tests, and which **failed
that session on two blocking checks** the moment it was finally run. A protocol nobody invokes
is documentation. This skill exists so the diagnosis has a name the operator can say.

## Order of operations — this order, not another

1. **Executable first.** Run Part 1. You may not write the judgement section before you have
   the machine verdict, because knowing the verdict changes what you are willing to claim.
2. **Judgement second**, in writing, against the template.
3. **Micro-upgrade third**, derived from the weakest answer.
4. *Then* `legend-capability-scout`, *then* `legend-session-takeaways`.

## Part 1 — run these; do not answer them

```bash
python3 framework/scripts/session_self_eval.py --workspace . --disease <disease>
python3 framework/scripts/deepdive_manifest.py --workspace . --disease <disease> --pmid <PMID>
python3 framework/scripts/fulltext_receipts.py verify
python3 framework/scripts/legend_lint.py .
```

Read the output literally. `[DECLARED GAP]`, `[UNREAD PREMISE]` and `[WARN_BUT_PROCEED]` lines
are findings even when the verdict is `PASS` — they are the debts that accumulate visibly until
someone closes them. A `FAIL` is not a formatting problem: fix the state, never the check, and
if the check was wrong, **strengthen it and add the regression** rather than relaxing it.

## Part 2 — answer in writing, with anchors

All 27 questions are in the protocol. `Yes` without a section, figure, file path or record ID is
not an answer. Store the completed diagnosis in a **durable** path —
`disease-models/<disease>/research/session_evaluations/<YYYY-MM-DD>_<key>.md` — never only in
`staging/`.

Three failure modes to watch for in your own answers:

- **Answering yes to everything.** Every question in the protocol carries a *"what a bad answer
  looks like"* clause precisely because this is the default failure.
- **Grading the outcome instead of the process.** A valuable finding does not make the process
  sound. The two get separate grades: on 2026-07-26 the content held and the process did not.
- **Writing the diagnosis yourself and calling it evidence.** Self-assessment by the agent that
  did the work is the weakest form. Where a parallel session, a check or the operator caught
  something you missed, **say who caught it** — that attribution is the useful signal.

## The rule

A session is not closed by having produced output. It is closed when **Part 1 returns `PASS`**
and **Part 2 is answered in writing**. Where an answer is weak, the session owes a proportional
micro-upgrade — **and the upgrade is the answer, not the promise of one.** A proposal parked in
`staging/` is not a capability the system has gained.

## Scope

Read-only toward the four canonical current files. This skill may append to the designated
append-only carve-outs (the ledgers, the queue, the receipt ledger through its validated
writer) and may ship framework/script upgrades with their regressions. Canonical promotion
stays a separate `BATCH_COMMIT` decision. Not medical advice.

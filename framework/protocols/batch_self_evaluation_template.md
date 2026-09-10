# Batch/full-text self-evaluation — durable template

> Complete after analysis and before capability growth or takeaways. Replace every prompt
> with evidence. `Yes` without an anchor is not an answer.

## Scope and executable verdict

- Batch/session:
- Studies and complete-read receipt IDs:
- `session_self_eval.py`:
- Per-study manifest(s):
- Receipt verification:
- Structural LINT:
- Local verdict:
- Workspace/global verdict and concurrent conditions:

## Content diagnosis

| Dimension | Evidence-backed answer | Grade (`strong`/`partial`/`failed`) | Debt or correction |
|---|---|---|---|
| Sequential full-text, figures, tables, supplements |  |  |  |
| Main message and original contribution |  |  |  |
| Hidden gold beyond keywords/abstract |  |  |  |
| Source parity: context, type and recency |  |  |  |
| Team type, field density, observation vs interpretation |  |  |  |
| DATO / INFERENZA / IPOTESI / ESPANSIONE separation |  |  |  |
| Existing claims touched; conflicts/revival triggers |  |  |  |
| Multi-hop and corpus cross-query |  |  |  |

## Persistence diagnosis

- Durable ledger/registry IDs and wikilinks:
- Reading queue/debt:
- Dossier and commit candidate:
- Receipt source fingerprint, coverage and supplement state:
- Can a future run distinguish full text from abstract only? How:

## Process and capability diagnosis

- Skills/gates/patterns used:
- Plausible skills deliberately declined, with reasons:
- Failures, retries, extraction mismatches or concurrency events:
- What caught each failure before an overclaim:
- Disease-agnostic micro-upgrade shipped:
- Regression/evidence that makes the upgrade persistent:
- Residual risk and next decisive action:

## Attribution census — required, fixed, parseable

Fill it from the failures enumerated above. The counting rule and the reason each line exists
are in [`session_self_evaluation.md`](session_self_evaluation.md) Part 3. In short: one incident
per defect or near-error, repeated instances of one rejection class counted once, and
`severity_high` reserved for the incidents that would have **reached the record** rather than
been refused by a writer.

```
ATTRIBUTION_CENSUS
incidents: <n>
machine: <n>   blind_auditor: <n>   peer: <n>   self: <n>
severity_high: <n>   of which self: <n>
undetected_known: <n>
```

`undetected_known` counts defects found **later** and attributed back to this wave. It is the one
line that pushes back on this diagnosis being written by the actor whose work it grades: an error
nobody caught appears in no list, so a corpus where this line is always `0` is reporting the limit
of the census, not the absence of the defects.

## §21c output — written to the task contract, not only here

`DEFAULTS_TAKEN` and `STOP_LOG` belong in this wave's `WAVE_n_RESULT` in the task contract JSON
(Annex A.1b), **both, even when empty**. A default recorded only in a message to the coordinator
is a transcript: after the ten unattended hours of 2026-09-09, a repository-wide grep found
`DEFAULTS_TAKEN` in two files.

---
name: legend-research-loop
description: Runs controlled micro-experiments on LEGEND scripts, lint, rankings, heuristics and procedures using a baseline, a single variable, a predefined success criterion, verification and a KEEP/DISCARD/INCONCLUSIVE decision. Use it when proposing or testing a non-trivial operational change, comparing two methods, validating an internal heuristic, or to avoid adopting an improvement on plausibility alone. Do not use it to replace full reading of studies, produce scientific proof, or directly modify the canonical current files.
---

# Legend Research Loop

Apply a small, verifiable, reversible experimental cycle. Change one variable at a time and keep the negative outcomes too.

## Initial gate

1. Confirm the object is operational or methodological: a script, lint, ranking, heuristic, procedure or repeatable transformation.
2. Do not use an automatic metric as a substitute for full text, scientific judgement, safety or clinical decision.
3. Do not write to the canonical current files. Any scientifically relevant result re-enters the ordinary pipeline.
4. If there is no observable, non-arbitrary criterion, classify the attempt as `INCONCLUSIVE` or run an explicit qualitative audit.

## Protocol

### 1. Question

State a falsifiable question:

`Does change X improve Y relative to baseline Z without degrading guardrail G?`

### 2. Baseline

Record before the change:

- identical input or fixture;
- current behaviour and result;
- primary metric;
- guardrail not to degrade;
- relevant environment or version.

If the baseline is missing, do not declare an improvement.

### 3. Success criterion

Define before execution:

- threshold or expected outcome;
- negative control or known case when available;
- crash/failure conditions;
- acceptable complexity cost.

Prefer lossless criteria: accuracy without record loss, coverage without false blocks, simplification at equivalent performance.

### 4. Minimal change

Change a single conceptual variable. Avoid adjacent refactors, new dependencies and unnecessary configurability. Make rollback easy.

### 5. Verification

Run the same check on the baseline and on the variant. Inspect the errors, not only the aggregate metric. For bug fixes, include at least the case that reproduces the defect and a control that must not change.

### 6. Decision

Use exactly one state:

- `KEEP`: passes the criterion and the guardrails; the complexity cost is proportionate.
- `DISCARD`: does not improve, degrades a guardrail, or adds disproportionate complexity.
- `INCONCLUSIVE`: insufficient evidence, invalid metric or ambiguous result.
- `CRASH`: invalid execution; do not count it as evidence against the idea until it is clear whether the crash is accidental or structural.

Do not retroactively change the criterion to save a result.

## Minimal record

Report in chat or in an appropriate operational artifact:

```text
experiment_id:
question:
baseline:
single_change:
success_criterion:
result:
guardrails:
decision: KEEP | DISCARD | INCONCLUSIVE | CRASH
next_step:
```

Do not create a new permanent log if an existing operational log suffices. Record in the capability scout log only when the test produces a micro-upgrade or a reusable failure mode.

## LEGEND guardrails

- Popularity, elegance and consensus among LLMs are not metrics of scientific truth.
- A `KEEP` result validates the procedure within the tested scope, not a biomedical claim.
- An LLM council can widen the alternatives, but does not replace primary sources or a treating team.
- Preserve privacy: no sensitive data in remote services without sanitization and explicit authorization.
- Nothing is medical advice; clinical-strategic outputs serve discussion with a treating team.

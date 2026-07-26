# Failure-Aware Evaluation

**The distinctive contribution of LEGEND: not just extracting mechanism from literature, but measuring where AI reasoning quietly fails — and correcting it.**

> Public method. The gold cases are drawn from *real, observed* reasoning failures encountered during genuine rare-disease research, using public-literature examples.

## Why a failure-aware eval

A knowledge system that accumulates for months is endangered less by what it asserts than by what it **discards**. A **false positive** gets tested and dies; a **false negative** is **silent, permanent, and self-reinforcing** — once discarded, nobody looks again. In a compounding system, false positives are a cost; **false negatives are a compounding loss.** Existing pipelines can retrieve and connect literature, but do not systematically measure their own compounding failures. This eval does.

## What it measures (metrics)

Not "% correct answers", but:

1. **source actually supports the claim** — in the declared variant / species / tissue (beyond "the quote exists in the abstract");
2. **correct causal direction** (no substrate/regulator inversion);
3. **measured-vs-inferred distinction** (no surrogate promoted to endpoint);
4. **correct species / tissue / model attribution**;
5. **improper cross-context transfer rate**;
6. **uncertainty calibration / appropriate abstention**;
7. **contradiction detection**;
8. **false-negative rate**;
9. **ability to reopen a superseded conclusion after new evidence** (temporal, see below);
10. **expert review time required**.

A dedicated **biomarker/endpoint epistemic-calibration** family checks whether the system keeps molecular biomarker vs distal clinical endpoint separate, refuses "validated" without a validation study, and defines an endpoint before observing the outcome.

## The experimental design

### Cumulative controlled arms

| Arm | Configuration |
|---|---|
| **A** | model + unstructured prompt |
| **B** | same model + interoperable schema (DisMech / LinkML) + validators |
| **C** | same model + schema + LEGEND guardrails (`PREMISE_TAG`, dismissal ledger, `REVIVAL_TRIGGER`) |

**Held identical across arms:** corpus · model/version · available tools · token budget · retrieval · replicates · scoring. So any gain is attributable to the guardrails, not to extra context or resources.

### Sequential (temporal) evaluation — the core innovation

Static accuracy is not enough. The distinctive test is **temporal**:

```
T0: incomplete evidence → the model accepts / rejects / suspends a hypothesis,
    recording its PREMISE and a REVIVAL_TRIGGER.
T1: new evidence arrives → the system must identify which past rejection to
    reopen, update the conclusion, and preserve the history (no silent overwrite).
```

This measures **permanent false negatives**, `REVIVAL_TRIGGER` quality, re-audit capability, and correction-without-drift — i.e. the difference between a *self-correcting* and a *self-improving* system.

### Benchmark construction (discipline)

Real observed errors are organized as **error families** (see `failure_taxonomy.md`), each with **multiple public instances**, **positive cases and negative controls**, a **development set** and a **held-out test set**, **independent adjudication** on at least a subset, and **no final tuning on the test set** — so guardrails cannot "win" by having been written on the eval examples.

### Reproducibility

Every run logs model version · prompt · schema · corpus · seed/replicate · tokens · cost (**run/cost ledger**), so A/B/C differences are attributable and the budget is auditable. The eval runs **lean first** (few replicates) and scales only where the signal justifies it.

## Interoperability with DisMech

Monarch's DisMech already models supporting/refuting/partial evidence and hypothetical/deprecated mechanism status. Its evidence and status enums become the **label space** of this benchmark: the eval measures whether a model assigns those labels correctly — including over time. LEGEND's original additions are the **reopening dynamic** (`REVIVAL_TRIGGER` + re-audit) and **premise tagging**, which the failure-aware eval is designed to measure. In this sense the eval directly serves DisMech's own curation quality control.

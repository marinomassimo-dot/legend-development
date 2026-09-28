# Benchmark J · J5 — RESULTS and decision

> Harness evidence, non-scientific. Rule fixed in [`PREREGISTRATION_J5.md`](PREREGISTRATION_J5.md),
> committed before the instrument change and before this replay. Raw rows:
> [`j5_results.json`](j5_results.json), produced by
> `python3 framework/scripts/record_edit_bench.py j5 --repo .` (≈22 s). Nothing here changes a
> claim, the working model, an evidence grade or a disease-model conclusion.

## Decision

**The paper-registry family is SUPPORTED as evidence.** With J2's three supported families, all
four current files now meet J3's family rule; the Benchmark J verdict *as evidence* becomes
**SUPPORTED**. Per the pre-registration, `BATCH_COMMIT` Phase 4.0 is **not** changed here:
`batch_commit.py propagate` still refuses `paper_registry_current` by name and the paper registry
keeps its FULL rewrite until that separate step is taken.

| Condition (PREREGISTRATION_J5 § 3) | Required | Measured | Met |
|---|---|---|---|
| lost legitimate edits, record granularity | L = 0 of 328 | **0** — `INTENDED` 318 / 318, `LEGITIMATE_COLLATERAL` 10 / 10 | ✅ |
| silent corruption, both granularities | S = 0 | **0** record · **0** range | ✅ |
| untouched units byte-equal | every event | **24 / 24** event rows (22 unique + 2 duplicate patches), both granularities | ✅ |
| instrument control | ≥ 95 % | **22 / 22** plants detected (100 %) | ✅ |
| refusals of any code (counted as losses) | — | **0** in both granularities, `UNBOUNDED_SPAN` included | — |

R = X in 22 / 22 unique events; R = child in 21 / 22 (the one `VERBATIM_COPY_DRIFT` hunk is not an
edit, and the editor prevented it, as in J2).

## The one former miss

`56c1881`, `## Purpose` of the paper registry, gets the op
`{"op": "replace", "heading": "Purpose", "under": "Paper Registry Current"}` and reproduces the
added `### Pathway-code legend` sub-block byte for byte; the second `## Purpose`, under
`# FASE 1 TRIAGE CORPUS`, is byte-equal. The deriver adds `under` only where the parent carries
the heading text more than once — on this corpus, that one op.

## Out of sample — reported, not decided

The seven post-J4 `BATCH_COMMIT` propagations that touched the paper registry, labelled by the same
cascade, replayed with today's editor and the J5 deriver (record granularity):

| Commit | E hunks + other | Ops | Refused | Lost | Silent | R = X | untouched equal |
|---|---|---:|---:|---:|---:|---|---|
| `c99dfe5` | 19 (some `UNRESOLVED`) | 5 | 0 | 0 | 0 | ✅ | ✅ |
| `1cdb1a4` | 2 | 2 | 0 | 0 | 0 | ✅ | ✅ |
| `95bd885` | 15 | 6 | 0 | 0 | 0 | ✅ | ✅ |
| `bc09bc9` | 3 | 3 | 0 | 0 | 0 | ✅ | ✅ |
| `da8b08b` | 11 | 9 | 0 | 0 | 0 | ✅ | ✅ |
| `c5eec22` | 2 | 2 | 0 | 0 | 0 | ✅ | ✅ |
| `67ac5ec` | 2 | 2 | 0 | 0 | 0 | ✅ | ✅ |

In those seven batches the FULL path passed ≈8.3 MB of paper registry through the model (file in
and out); the record-scoped path would have needed ≈151 KB — see
[`harness_cost_20260928.md`](../../../../governance/design_records/harness_cost_20260928.md) § 3.

## What changed in the tools

- `record_scoped_edit.py`: optional `under` (`--under`, `"under"` in an ops file) — valid only with
  `heading`; keeps the heading hits whose enclosing-heading chain contains that exact text; none →
  `ANCHOR_MISSING`, several → `ANCHOR_AMBIGUOUS`; `under` without `heading` → `ANCHOR_MISSING`. An
  op without `under` resolves exactly as before. Seven new unit tests.
- `record_edit_bench.py`: `j5` = J2's replay restricted to the paper-registry family with the
  qualifier switch on. `j2` is unchanged (the switch defaults off).

## Known limits

- The corpus is the frozen J0 slice (22 events, mostly additive) plus seven recent batches;
  renames, splits and deletions in the paper registry are exercised only by the unit suite.
- The J2 deriver anchors working-model edits by `id: BLOCK 3`, which the editor has refused since
  `e9c9172` (`UNBOUNDED_SPAN`); production anchors those edits by `--heading`. A J2 re-run with
  today's editor would therefore misreport the working-model family; J5 does not touch that family.

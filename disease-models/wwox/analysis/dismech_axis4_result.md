# Axis 4 — deduplication, measured

> **Non-canonical.** The first run of axis 4 with a non-empty correspondence set, and the
> reason it will stay uninformative at any scale. It changes no canonical file.
>
> Public, disease-level, de-identified. Nothing here is medical advice.

**Date:** 2026-08-04 · **Inputs:** reference sidecar after the precision repairs (22 occurrences) vs realigned independent derivation (27)

---

## The measurement

| | occurrences | dedup groups | groups spanning more than one claim |
|---|---:|---:|---:|
| Reference | 22 | 21 | **1** |
| Independent | 27 | 27 | **0** |

The single merge is `DK-c46285700983`, joining CLAIM 016 and CLAIM 035 on the WWOX 388–407
requirement — the merge predicted by inspection in the specification and reproduced by
computation ever since.

Comparing the two partitions is therefore comparing one merge against none. **Axis 4 runs, and
says almost nothing.**

## Why it is structural, not a shortage of data

The production dedup key hashes the proposition text, the context, the locator fingerprint,
the epistemic type and the evidence relation. Two occurrences merge only when an author wrote
the *same sentence twice*.

Measured: **0 of 21 reference propositions are byte-identical to any of the 27 independent
ones.** Under the canonical key, still zero merges on the independent side.

That is not a defect of these two derivations. Two readers decomposing the same material in
their own words will essentially never produce identical strings, so:

- **within a run**, dedup works and is meaningful — it catches an author restating the same
  fact at two anchors, which is exactly what the reference did once;
- **across runs**, an exact-text key can only ever report near-total disagreement, and the
  canonical key does not close the gap because it deliberately refuses to fold word order,
  qualifiers or added context.

Cross-run partition comparison would require correspondence established by *judgement* —
axis 3's human step — and then it measures whether two readers grouped the same *facts*, not
the same *strings*. That is a different and much more expensive measurement than the axis
was designed for.

## Verdict

**Axis 4 is well-formed and uninformative.** It should keep running — a within-run merge is
worth catching, and a partition that suddenly changes is a signal — but the cross-run
comparison it was designed for cannot be made to work with a text-derived key, and widening
the key until it does would destroy the property that makes the rest of the instrument
honest.

This closes the four axes. The scoreboard:

| Axis | Status | What it measures reliably |
|---|---|---|
| 1 — anchor selection | works | shared anchors, once the ordinal base is declared |
| 2 — atomisation | works | **split agreement, confirmed exactly by two blind reviewers** |
| 3 — proposition correspondence | works only with a human step | equivalence, at ~68 % inter-rater agreement |
| 4 — deduplication | runs, near-empty | within-run restatement; **not** cross-run partitions |

## Related

[`dismech_axis3_review_result_round2.md`](dismech_axis3_review_result_round2.md) · [`dismech_independent_derivation_design.md`](dismech_independent_derivation_design.md) · [`dismech_export_spec.md`](dismech_export_spec.md)

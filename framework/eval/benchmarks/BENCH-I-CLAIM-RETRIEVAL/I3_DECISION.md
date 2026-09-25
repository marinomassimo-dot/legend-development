# Benchmark I · I3 — architecture decision

> Harness evidence and a routing decision; non-scientific. Nothing here changes a claim, the
> working model, an evidence grade or a disease-model conclusion.

## Decision

**TARGETED RETRIEVAL NOT SUPPORTED.** The full claim-registry preload stays on every route
that has it. Pre-registered rule ([`PREREGISTRATION.md`](PREREGISTRATION.md) § 5): *NOT SUPPORTED
⇔ I1 not acceptable, or …* — and I1 is not acceptable.

## Why, in the order the evidence arrived

1. **Retrieval misses real targets.** On 22 STRONG historical events (29 affected claims), the
   route the comparison already runs (`registry_records.py get --pmid --hops 1`) reaches
   **13 / 29**, and the progressive literal route reaches **25 / 29**. The four misses are all
   diagnosed and none is an implementation defect: links followed outward only (I03), a
   discriminating concept that is common vocabulary in a one-gene registry (I06), an acronym the
   pre-registered token rule drops (I09), and a trigger the first pass never recorded (I24)
   ([`I1_RESULTS.md`](I1_RESULTS.md)).
2. **The context reduction is not material.** The progressive route's candidate set is **83 %**
   of the registry at the median; the only setting that reaches every target returns **91 %**. The
   only small route (2.6 %) is the one that reaches 45 %. Recall and bytes trade almost
   one-for-one: a paper's first-pass text shares some distinctive word with most of 40 claims
   about one gene.
3. **Attention is not the problem.** Where the target was in context, the model found it as
   reliably from the progressive records as from the whole registry: 73 vs 68 of 84, no fixture
   favouring either arm, the same two fixtures missed identically in both
   ([`I2_RESULTS.md`](I2_RESULTS.md)). This does not rescue the optimisation — Arm C was 0.87 of
   Arm A — but it locates the failure: **the bottleneck is candidate generation, not reading.**

## Context, full registry vs targeted (measured)

| | Whole registry | CURRENT | PROGRESSIVE (primary) | PROGRESSIVE (cap 0.20) |
|---|---:|---:|---:|---:|
| claim bytes (median over fixtures) | 100 % (70,978–119,152 B at the events' parents; **127,862 B** at `main` today) | 2.6 % | 83.3 % | 91.1 % |
| claim records (median) | 35–39 (40 today) | 1 | 31 | 36 |
| STRONG targets reached | 29 / 29 | 13 / 29 | 25 / 29 | 29 / 29 |
| native input tokens per I2 call (median) | 44,079 (Arm A) | — | 40,428 (Arm C) | — |

Percentage reduction of the progressive route against the whole registry: **16.7 %** of claim
bytes at the median; **8 %** of native input tokens per call in I2.

## Routing change

**None.** The preload is retained on the nine routes that load the claim registry whole
(`operator_manual.md` § 1.1, § 1.2, § 2 · `deep_dive_manual.md` · `legend-start` · `legend` step 3 ·
`legend-deepdive` skill and agent · `legend-discovery` 2b · `legend-hypothesis-forge` 0). The only
edit is an evidence pointer beside the manual's own rationale in § 1.1, so the next reader of
*"un recupero selettivo non può garantirlo"* finds the measurement instead of re-opening the
question. The paper registry and literature log remain by record, as before: this benchmark says
nothing against that route, which is about identity lookup, not impact discovery.

## What would reopen this

The smallest evidence that could change the decision: a deterministic candidate route that
reaches **all 29** STRONG targets of this fixture set (and new events since) at a **material**
reduction, for example under half the registry. The post-hoc backlink-as-mention measurement
(CURRENT 13 → 17 / 29, 3.5 %) shows that link-graph completeness moves recall cheaply, and that
it is far from sufficient on its own; I06, I09 and I24 need either a richer first pass or
matching the D-layer deliberately does not do.

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

## K1 · after "a citation by record link is a citation" (2026-09-26)

K1 made, deliberately, the change this benchmark reverted: a record that wikilinks to an
identity record of the queried PMID/DOI is a `mention (links to …)` hit
([design record](../../../../governance/design_records/k1_citation_by_record_link_20260926.md)).
Re-run of I1 with the frozen fixtures, primary configuration, no sensitivity, written to
[`i1_results_after_K1.json`](i1_results_after_K1.json); the frozen files above were not touched.

| STRONG (22 fixtures, 29 targets) | CURRENT before | CURRENT after K1 | PROGRESSIVE before | PROGRESSIVE after K1 |
|---|---:|---:|---:|---:|
| targets retrieved | 13 / 29 | **17 / 29** | 25 / 29 | **26 / 29** |
| fixtures fully retrieved | 9 / 22 | 11 / 22 | 18 / 22 | 19 / 22 |
| median candidates | 1 | 1 | 31 | 31 |
| median registry fraction | 2.6 % | **3.5 %** | 83.3 % | 83.3 % |

The after-K1 run matches the post-hoc measurement row for row (all 78 fixture × strategy rows
identical), with a different implementation (`registry_records.py` sha256 `755bc3bd…`
against the post-hoc `1bbadaa9…`). Gained targets: I03 (both), I07, I16 — as predicted. I06,
I09 and I24 are still missed at the events' parents.

**The decision stands: TARGETED RETRIEVAL NOT SUPPORTED, preload retained.** The pre-registered
SUPPORTED rule needs all 29 STRONG targets at a material reduction; K1 gives 17 / 29 on the small
route and 26 / 29 at 83 % of the registry. K1 alone was never going to meet it, and does not.

**Size guard** — `get --pmid <P> --hops 1` on today's `main` registries, for the 23 PMIDs of the
fixtures, rendered bytes and records returned, before → after K1. Total: 1,814,650 → 2,080,228 B (1.15×).

| PMID | bytes before | bytes after | ratio | records before → after |
|---|---:|---:|---:|---:|
| 21075834 | 18,864 | 38,338 | 2.03× | 5 → 13 |
| 18974271 | 26,585 | 49,062 | 1.85× | 6 → 13 |
| 17575124 | 43,572 | 70,402 | 1.62× | 8 → 17 |
| 31340538 | 109,153 | 144,363 | 1.32× | 26 → 39 |
| 42422765 | 143,767 | 188,309 | 1.31× | 25 → 36 |
| 17360458 | 106,126 | 134,221 | 1.26× | 22 → 33 |
| 32581702 | 60,799 | 72,039 | 1.18× | 11 → 17 |
| 32000863 | 127,236 | 148,405 | 1.17× | 30 → 38 |
| 33916893 | 75,139 | 83,580 | 1.11× | 18 → 21 |
| 34747138 | 100,667 | 110,455 | 1.10× | 21 → 24 |
| 34268881 | 157,101 | 171,585 | 1.09× | 33 → 39 |
| 19500159 | 150,985 | 162,920 | 1.08× | 31 → 36 |
| 15070730 | 64,566 | 69,643 | 1.08× | 11 → 15 |
| 30755385 | 61,645 | 63,472 | 1.03× | 18 → 18 |
| 23254685 | 46,349 | 47,233 | 1.02× | 13 → 13 |
| 34831305 | 69,478 | 70,623 | 1.02× | 17 → 17 |
| 41562193 | 24,730 | 25,077 | 1.01× | 10 → 10 |
| 29724996 | 52,007 | 52,717 | 1.01× | 16 → 16 |
| 26499798 | 64,379 | 65,203 | 1.01× | 14 → 14 |
| 21115974 | 60,913 | 61,526 | 1.01× | 15 → 15 |
| 30290271 | 129,456 | 129,922 | 1.00× | 30 → 30 |
| 20530675 | 79,500 | 79,500 | 1.00× | 21 → 21 |
| 21731849 | 41,633 | 41,633 | 1.00× | 12 → 12 |

One answer grows by more than 2×: **PMID 21075834, 2.03×** (18,864 → 38,338 B, 5 → 13 records).
Cause: CLAIM 009 and CLAIM 034 cite it as `[[paper_registry_current#PAPER 071]]`, now hits at hop 0 —
they are I09's two STRONG targets, reached on today's registries because PAPER 071 now exists
(at the event's parent the paper was only `CORPUS P358`). The added bytes are their own text plus
the one outward hop from them (PAPER 054, 002, 023, 017, 061, CLAIM 028, DIS-008). Nothing is capped.

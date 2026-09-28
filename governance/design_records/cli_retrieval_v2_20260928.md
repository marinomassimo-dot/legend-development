# CLI Retrieval v2 — measured before built, 2026-09-28

> **Non-normative design record**, harness only. Actor: Harness Engineering (`plan`), autonomous
> micro-roadmap *CLI Retrieval v2* (R2.0–R2.9), queued behind the harness-cost queue of the same
> day. Nothing here changes a claim, a registry, `registry_records.py` or any routing rule; the
> claim-registry preload stays canonical. Measured at `main` = `e946f79`.

**Verdict: V2 DOES NOT MATERIALLY IMPROVE CURRENT RETRIEVAL.** No deterministic admission rule over
the frozen Benchmark I candidates reaches the STRONG targets at a material reduction, and the two
features that do not need that (batch mode, renderer compaction) buy too little to ship.

## R2.0 · Baseline

- `python3 framework/scripts/claim_retrieval_bench.py i1` at `e946f79` reproduces
  [`i1_results_after_K1.json`](../../framework/eval/benchmarks/BENCH-I-CLAIM-RETRIEVAL/i1_results_after_K1.json)
  exactly — identical candidate sets in every fixture. STRONG: CURRENT **17 / 29 at 3.5 %**,
  PROGRESSIVE **26 / 29 at 83.3 %**; sensitivity 0.05 → 24 / 29, **0.20 → 29 / 29 at 91.1 %**.
  53 s for the whole run.
- CLI cost: one `get` 0.2–0.5 s wall; importing the module 0.04 s; parsing all seven surfaces
  (1,462 records) 0.26 s.

## Per feature

| Block | Outcome | Evidence |
|---|---|---|
| R2.1 explicit backlinks | **NOT NEEDED** | K1 (`4c1d250`) already returns, as default semantics and with its reason (`mention (links to …)`), every record that links to the query's identity record; the broader inbound hop was measured by I4 at +1 / 29 for 2.3× the bytes ([`g1_i4_residual_decisions_20260926.md`](g1_i4_residual_decisions_20260926.md) § B) |
| R2.2 batch / parse once | **NOT NEEDED** | a whole parse is 0.26 s; post-M1 transcripts make ≈8 `registry_records.py` calls each (207 `get` over 26 transcripts) → ≤ 3 s per session |
| R2.3 selection tiers | **REFUTED** for preload replacement | table below |
| R2.4 `--explain-selection` | **NOT NEEDED** | every returned record already carries its deterministic reason (`identity`, `identity (doi)`, `mention`, `mention (links to X)`, `theme`, `field`, `linked from X (hop n)`), in text and JSON |
| R2.5 Benchmark I replay | **run** (R2.0 + the tier replay) | — |
| R2.6 context budget | **REFUTED** | table below |
| R2.7 renderer metadata | **NOT NEEDED** | `get --pmid 30290271 --hops 1` today: 237,430 B out, 224,603 B of it whole records; shared metadata 12,827 B (**5.4 %**) |
| R2.8 model attention | **NOT RUN** | retrieval failed its deterministic arm |
| R2.9 routing | **NO CHANGE** | — |

## Tiers and budgets on the frozen fixtures (R2.3 / R2.6)

[`r2_posthoc_tiers.py`](../../framework/eval/benchmarks/BENCH-I-CLAIM-RETRIEVAL/r2_posthoc_tiers.py) →
[`r2_posthoc_tiers.json`](../../framework/eval/benchmarks/BENCH-I-CLAIM-RETRIEVAL/r2_posthoc_tiers.json);
post-hoc, candidate sets unchanged, fractions of the claim registry's bytes at each fixture's
`commit_read`, STRONG (22 fixtures, 29 targets).

| Admission rule | df_cap 0.10 (primary) | df_cap 0.20 (sensitivity) |
|---|---|---|
| everything PROGRESSIVE returns | 26 / 29 at median 84.9 % (p90 96.3 %) | 29 / 29 at 93.1 % (p90 100 %) |
| tier ≤ 2 (CURRENT + ≥ 2 literal terms) | 23 / 29 at 71.4 % (p90 84.7 %) | 28 / 29 at 86.3 % (p90 95.6 %) |
| tier order, whole records, budget 40 % | 13 / 22 fixtures complete | 15 / 22 |
| exploratory: literal hits by term count, budget 40 % | 18 / 22 | 17 / 22 |
| byte fraction needed to reach every found target, tier order | median 6.8 %, **p90 72 %, max 78 %** | median 9.0 %, p90 81 %, max 99 % |

The median is small because most targets are CURRENT hits; the tail is what decides, and a fixed
budget cannot know in advance which fixture is in the tail. The brief's own line holds: 29 / 29
only at 80–90 % of the registry is **not enough improvement**.

## What now prevents a smaller context (R2 § I)

1. **A comparison asks about a relation the registry does not yet record.** Seven STRONG
   fixtures have no link path at all to their target (I4 § B3); only literal overlap finds them,
   and literal overlap of scientific vocabulary is broad.
2. **The working model's BLOCK 3 is one record from its heading to end of file**, `## Changelog`
   and the batch sections included. In the 237 KB answer above, BLOCK 3 is 54,816 B returned
   because the PMID is named once in that history, and its hop-1 links bring CLAIM 002 and more.
   Selecting fewer records cannot fix a record that is 50 % history; it is the G1 structure
   question, now HUMAN_REQUIRED in [`harness_cost_20260928.md`](harness_cost_20260928.md) § 9.

## Next action

Revisit only after the working model's history leaves BLOCK 3 (G1 option A): then re-run
`claim_retrieval_bench.py i1` and this script unchanged. That changes what a `mention` of a paper
in the WM costs; it does not by itself change the claim-registry verdict.

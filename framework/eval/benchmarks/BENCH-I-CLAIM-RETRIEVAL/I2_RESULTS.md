# Benchmark I · I2 — model attention, Arm A (whole registry) vs Arm C (retrieved records) · RESULTS

> Harness evidence, non-scientific. 132 independent `claude -p` calls (`claude-opus-5-5`), run
> 2026-09-25 06:17–06:28 UTC under [`I2_PROTOCOL_FREEZE.md`](I2_PROTOCOL_FREEZE.md): 22 fixtures ×
> 2 arms × 3 repetitions, 0 failed calls, 0 retries. Compact per-run records (job id, arm, prompt
> hash, bytes, native token usage, the model's answer) in [`i2_runs.jsonl`](i2_runs.jsonl); blind
> scores and the unblinded table in [`i2_grades.json`](i2_grades.json). Raw CLI payloads were kept
> out of the repository.

## Paired raw results

✓ every target named · ½ some · ✗ none · ∅ the runner returned an **empty final answer**
(finished normally with thinking tokens but no text; graded `OTHER` as pre-registered).
"rel ok" = identified targets whose relationship matched the historical label. "extras/run" =
non-target claim IDs named per run (unlabelled, not judged wrong: history labels what changed, not
everything a paper touches).

| Fixture | Class | Targets | Relationship | PMID route? | A outcomes | A ident | A rel ok | A extras/run | C outcomes | C ident | C rel ok | C extras/run | C/A bytes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I00 | NO_CHA | — (none) | no affected existing claim | — | ✓✓✓ | — | 0 | 0/0/0 | ✓✓✓ | — | 0 | 0/0/0 | 0.20 |
| I01 | STRONG | 005 | narrows / qualifies | no | ✓✓✓ | 3/3 | 0 | 8/5/7 | ✓✓✓ | 3/3 | 2 | 3/5/6 | 0.81 |
| I02 | STRONG | 005 | contradicts / weakens | no | ✓✓✓ | 3/3 | 0 | 6/7/5 | ✓✓✓ | 3/3 | 0 | 4/4/4 | 0.89 |
| I04 | STRONG | 004 | requires review | yes | ✓✓✓ | 3/3 | 0 | 2/4/5 | ✓✓✓ | 3/3 | 0 | 6/5/5 | 0.67 |
| I05 | STRONG | 009 | supports / strengthens | no | ✓✓∅ | 2/3 | 0 | 5/7/0 | ✓✓✓ | 3/3 | 1 | 4/4/4 | 0.68 |
| I07 | STRONG | 016 | narrows / qualifies | no | ✓✓✓ | 3/3 | 0 | 11/10/11 | ✓✓✓ | 3/3 | 0 | 10/9/11 | 0.97 |
| I08 | USABLE | 003, 004, 016 | narrows / qualifies | no | ½½½ | 6/9 | 2 | 8/7/9 | ½½½ | 6/9 | 1 | 8/8/7 | 0.80 |
| I10 | STRONG | 032 | narrows / qualifies | yes | ✓∅✓ | 2/3 | 2 | 1/0/2 | ✓✓✓ | 3/3 | 3 | 3/0/1 | 0.41 |
| I11 | STRONG | 032, 036 | narrows / qualifies | yes | ∅✓✓ | 4/6 | 2 | 0/2/2 | ✓✓½ | 5/6 | 0 | 2/2/2 | 0.51 |
| I12 | STRONG | 036 | narrows / qualifies | yes | ✓∅✓ | 2/3 | 0 | 2/0/3 | ✓✓✓ | 3/3 | 0 | 4/2/2 | 0.65 |
| I13 | STRONG | 036 | narrows / qualifies | yes | ✓✓∅ | 2/3 | 0 | 4/1/0 | ✓✓✓ | 3/3 | 0 | 2/1/3 | 0.60 |
| I14 | STRONG | 011 | narrows / qualifies | yes | ✓✓✓ | 3/3 | 0 | 5/6/3 | ✓✓✓ | 3/3 | 0 | 3/3/4 | 0.87 |
| I15 | USABLE | 002 | narrows / qualifies | yes | ✓✓✓ | 3/3 | 3 | 7/8/6 | ✓✓✓ | 3/3 | 3 | 5/9/5 | 0.92 |
| I16 | STRONG | 017, 019, 030, 033 | narrows / qualifies | no | ✓✓✓ | 12/12 | 1 | 2/3/3 | ✓✓✓ | 12/12 | 3 | 5/8/3 | 0.93 |
| I17 | STRONG | 023 | narrows / qualifies | no | ✓✓✓ | 3/3 | 0 | 2/2/1 | ✓✓✓ | 3/3 | 0 | 4/2/2 | 0.90 |
| I18 | STRONG | 023 | supports / strengthens | yes | ✓∅✓ | 2/3 | 2 | 5/0/4 | ✓✓✓ | 3/3 | 3 | 4/4/4 | 0.91 |
| I19 | STRONG | 025 | narrows / qualifies | yes | ✓✓✓ | 3/3 | 3 | 6/5/5 | ✓✓✓ | 3/3 | 3 | 4/4/4 | 0.83 |
| I20 | STRONG | 029 | narrows / qualifies | yes | ✓✓✓ | 3/3 | 2 | 1/3/2 | ✓✓✓ | 3/3 | 3 | 1/1/1 | 0.91 |
| I21 | STRONG | 030 | supports / strengthens | no | ✓✓✓ | 3/3 | 3 | 10/11/11 | ✓✓✓ | 3/3 | 3 | 9/11/10 | 0.95 |
| I22 | STRONG | 036 | narrows / qualifies | no | ✓✓✓ | 3/3 | 0 | 3/5/3 | ✓∅✓ | 2/3 | 0 | 3/0/1 | 0.96 |
| I23 | STRONG | 036 | narrows / qualifies | no | ✓✓✓ | 3/3 | 0 | 2/2/2 | ✓✓✓ | 3/3 | 0 | 2/2/1 | 0.90 |
| I25 | USABLE | 005, 037 | contradicts / weakens | no | ✗✗✗ | 0/6 | 0 | 5/6/7 | ✗✗✗ | 0/6 | 0 | 3/5/4 | 0.84 |
A {'correct': 51, 'partial': 3, 'incorrect': 3, 'OTHER': 6} relok 20 extras total 280

## Aggregates (target fixtures only; 21 fixtures, 63 runs per arm)

| | Arm A (whole registry) | Arm C (progressive records) |
|---|---:|---:|
| runs correct / partial / incorrect / empty | 51 / 3 / 3 / **6** | 55 / 4 / 3 / **1** |
| **targets identified (pooled)** | **68 / 84** | **73 / 84** |
| targets identified, excluding empty-answer runs | 68 / 77 (88.3 %) | 73 / 83 (88.0 %) |
| fixtures favouring this arm (score gap ≥ 0.5) | 0 | 0 |
| fixtures where the arms differ at all | 7, each by one repetition (6 of them an A run with an empty answer; I22 is a C empty answer) | |
| relationship matches on identified targets | 20 / 68 | 25 / 73 |
| extra (unlabelled) claim IDs, total | 280 | 262 |
| no-change control I00 | 3 / 3 correct (empty list) | 3 / 3 correct |
| claim-context bytes, median | 97,830 | 83,704 (0.87 × A) |
| claim records, median | 39 | 33 |
| native input tokens per call, median (main model; input + cache read + cache write) | 44,079 | 40,428 |

The token medians are the runner's own `modelUsage` counts, not estimates. The per-call range is
wider than the byte range because a run the CLI took in two turns counts its context twice; the
median is robust to that and is the number reported.

## Error decomposition (per missed target / per run, as pre-registered)

| Class | Meaning | Arm A | Arm C |
|---|---|---:|---:|
| `TARGET_NOT_IN_CONTEXT` | retrieval | 0 | 0 |
| `TARGET_IN_CONTEXT_NOT_SELECTED` | attention | 0 | 0 |
| `WRONG_NEARBY_CLAIM` | discrimination (target missed while other claims were named) | 9 | 10 |
| `EXTRA_UNSUPPORTED_CLAIMS` | precision (runs naming ≥ 1 unlabelled claim) | 57 | 61 |
| `RELATIONSHIP_WRONG` | interpretation (identified target, label differs) | 48 | 48 |
| `OTHER` | empty or unparseable answer | 6 | 1 |

Where the misses are: **I25** (0 / 6 in both arms — the seizure-batch synthesis: the model links
the AAV paper's observations to other claims and never to CLAIM 005 / CLAIM 037) and **I08**
(6 / 9 in both arms — the review's secondary link to CLAIM 003 / 004). Both are
USABLE_WITH_LIMITATION fixtures, and both fail **identically in both arms**: an attention and
discrimination limit of the comparison step itself, not a consequence of the smaller context.
Relationship agreement is low in both arms (~30 %): the model says *supports* where history
wrote *narrows*, the known softness of a four-way label, and not arm-dependent.

## I2 verdict

On the fixtures where retrieval succeeded, **Arm C shows no loss of target identification
relative to Arm A**: no fixture favours A, pooled C ≥ pooled A, and every per-fixture difference is
one repetition, six of seven being empty A answers. The attention half of the question is
answered in C's favour. **But the context Arm C carried was 0.87 of Arm A's**: I2 compared the
whole registry with most of it, because that is what PROGRESSIVE returns. It does not show that a
*small* context preserves attention, because no small context reached the targets in I1.

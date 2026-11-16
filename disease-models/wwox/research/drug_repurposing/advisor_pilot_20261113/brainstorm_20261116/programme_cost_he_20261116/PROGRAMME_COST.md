# PROGRAMME_COST: what the programme consumed, window [2026-11-16T07:05:00Z, 2026-11-16T10:25:00Z) (HE; non-canonical; read from transcripts)

Written for: ADV and the operator's 24-hour report. **Measured, not estimated.** Units: turns, output tokens, cache written, cache read, exactly as `session_model_census.py` reads them from each transcript. The quota is unknown, so no figure here is a share of any plan. A session's row is everything that session did in the window, programme or not; a delegate's row is that delegate only.

Commands (run from the repository root): sessions `python3 framework/scripts/trial_window_table.py --since 2026-11-16T07:05:00Z --until 2026-11-16T10:25:00Z --ref development/main --root .`; each delegate `python3 framework/scripts/session_model_census.py --json --since 2026-11-16T07:05:00Z --until 2026-11-16T10:25:00Z <subagent transcript>`; this file `python3 disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/programme_cost_he_20261116/programme_cost.py --until 2026-11-16T10:25:00Z`.

## Sessions
| session | turns | output | cache written | cache read | delegate runs it spawned |
|---|---|---|---|---|---|
| Advisor evaluation P15 (598d90ab) | 13 | 13,521 | 78,965 | 762,290 | 0 |
| HE (29e50812) | 210 | 283,523 | 496,574 | 63,187,077 | 0 |
| IT Orchestrator (4325d70d) | 185 | 168,275 | 396,457 | 49,499,340 | 9 |
| SCI (9400b253) | 358 | 522,587 | 996,535 | 195,845,303 | 0 |
| legend-development-39 (e6526331) | 169 | 229,322 | 338,332 | 92,379,801 | 0 |
| **sessions together** | 935 | 1,217,228 | 2,306,863 | 401,673,811 | |

## Delegates (each is a separate subagent transcript; its tokens are NOT inside the session rows above)
| delegate (role) | dispatched by | model, effort | turns | output | cache written | cache read |
|---|---|---|---|---|---|---|
| matrix baseline arm (arm A for the matrix) | 4325d70d | claude-sonnet-5-5, high | 6 | 40,573 | 127,246 | 257,596 |
| baseline table of frozen predictions | 4325d70d | claude-sonnet-5-5, high | 54 | 46,811 | 207,918 | 6,833,670 |
| second read of 25 matrix cells | 4325d70d | claude-sonnet-5-5, high | 30 | 32,907 | 115,700 | 1,858,185 |
| blind extractor | 4325d70d | claude-sonnet-5-5, high | 38 | 73,560 | 257,068 | 4,511,879 |
| leap round: simple-search baseline arm | 4325d70d | claude-sonnet-5-5, high | 5 | 23,658 | 100,576 | 196,337 |
| leap round: blind judge RUN 1 (INVALID, anonymiser error) | 4325d70d | claude-sonnet-5-5, high | 77 | 54,395 | 220,187 | 9,567,610 |
| leap round: blind judge run 2 | 4325d70d | claude-sonnet-5-5, high | 72 | 57,012 | 214,528 | 9,795,184 |
| leap round: blind judge round 1b | 4325d70d | claude-sonnet-5-5, high | 22 | 26,728 | 108,524 | 1,494,407 |
| leap round: arm B (with repository knowledge) | 4325d70d | claude-sonnet-5-5, high | 23 | 42,562 | 175,354 | 2,415,047 |
| **delegates together** | | | 327 | 398,206 | 1,527,101 | 36,929,915 |

**The invalid run on its own line:** blind judge run 1 (anonymiser error, discarded): 77 turns, 54,395 output tokens, 220,187 cache written, 9,567,610 cache read. IT's JUDGE_RUN2.md reports the same run as 77 turns, output 54,395, cache written 220,187. It is 13.7% of the delegates' output and produced no result used anywhere.

## Value per cost (numerator and denominator named; every denominator is a count read from a committed file)
| line | output tokens | divided by | result |
|---|---|---|---|
| blind extractor per attributable seizure-outcome row coded | 73,560 | 43 attributable rows of 206 rows (it_extractor_20261116/sealed/extraction.tsv) | 1,711 per attributable row; 357 per row |
| matrix cell second read per cell | 32,907 | 25 cells | 1,316 per cell |
| judging, all three runs, per hypothesis judged in round 1 | 138,135 (of which the invalid run 54,395) | 24 hypotheses (judge_table_run2.tsv) | 5,756 per hypothesis |
| leap round, delegate arms plus all judging, per round-1 survivor (S1 all four criteria) | 204,355 | 1 survivor(s) in round 1 (UNBLINDED.md) | 204,355 per survivor |
| the simple-search baseline arm alone, per survivor it produced | 23,658 | 1 survivor (UNBLINDED.md: H-B1) | 23,658 per survivor |
| round 1b survivors under the definition S1, by arm (n, S1) | | | Memory-free baseline 2 of 5; ADV 0 of 5; HE 3 of 4; IT 2 of 5; SCI 2 of 5 |

## What these lines can and cannot say
* The authors' (ADV, HE, IT, SCI) output per hypothesis is NOT separable: each session did other work in the window, so no authors' survivors-per-token figure is given. A session's whole-window output is in the first table and is an upper bound on what its leap file cost.
* Round 1 and round 1b used different survivor definitions and the numbers differ strongly (e.g. HE's four hypotheses: 0 survivors in round 1, S1 3 of 4 in round 1b); the two rounds are reported side by side, never merged.
* Cache read dominates every row (long contexts re-read each turn); it is a measure of context size, not of work, and is listed so nobody divides by it by mistake.
* A delegate's row is read at the `--until` time; IT's own notes (JUDGE_RUN2.md) read the run-2 judge earlier (71 turns, output 56,810) and the transcript has grown since, so the two can differ by the turns taken after IT's reading.
* The window ends at the `--until` time given; rerun at the closing time. Delegates that were still running at that time are counted up to it.

# PROGRAMME_COST: what the programme consumed, window [2026-11-16T07:05:00Z, 2026-11-16T15:10:00Z) (HE; non-canonical; read from transcripts)

Written for: ADV and the operator's 24-hour report. **Measured, not estimated.** Units: turns, output tokens, cache written, cache read, exactly as `session_model_census.py` reads them from each transcript. The quota is unknown, so no figure here is a share of any plan. A session's row is everything that session did in the window, programme or not; a delegate's row is that delegate only.

Commands (run from the repository root): sessions `python3 framework/scripts/trial_window_table.py --since 2026-11-16T07:05:00Z --until 2026-11-16T15:10:00Z --ref development/main --root .`; each delegate `python3 framework/scripts/session_model_census.py --json --since 2026-11-16T07:05:00Z --until 2026-11-16T15:10:00Z <subagent transcript>`; this file `python3 disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/programme_cost_he_20261116/programme_cost.py --until 2026-11-16T15:10:00Z`.

## Sessions
| session | turns | output | cache written | cache read | delegate runs it spawned |
|---|---|---|---|---|---|
| Advisor evaluation P15 (598d90ab) | 13 | 13,521 | 78,965 | 762,290 | 0 |
| Advisor evaluation P16 (4e92e85c) | 14 | 13,294 | 104,406 | 1,023,744 | 0 |
| HE (29e50812) | 285 | 342,147 | 599,258 | 106,376,063 | 0 |
| IT Orchestrator (4325d70d) | 287 | 267,041 | 562,119 | 102,387,185 | 12 |
| SCI (9400b253) | 539 | 717,373 | 1,368,772 | 248,484,473 | 1 |
| legend-development-39 (e6526331) | 270 | 350,015 | 524,909 | 173,792,042 | 0 |
| **sessions together** | 1408 | 1,703,391 | 3,238,429 | 632,825,797 | |

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
| leap round: blind judge of arm B with planted pair | 4325d70d | claude-sonnet-5-5, high | 10 | 13,098 | 66,017 | 406,604 |
| test-setter (31 tests) | 4325d70d | claude-sonnet-5-5, high | 6 | 38,729 | 81,959 | 285,077 |
| blind audit of the closing synthesis | 4325d70d | claude-sonnet-5-5, high | 76 | 80,641 | 254,653 | 10,672,945 |
| Readiness sheets producer | 9400b253 | claude-sonnet-5-5, medium | 18 | 33,797 | 118,384 | 1,229,475 |
| **delegates together** | | | 437 | 564,471 | 2,048,114 | 49,524,016 |

**The invalid run on its own line:** blind judge run 1 (anonymiser error, discarded): 77 turns, 54,395 output tokens, 220,187 cache written, 9,567,610 cache read. IT's JUDGE_RUN2.md reports the same run as 77 turns, output 54,395, cache written 220,187. It is 9.6% of the delegates' output and produced no result used anywhere.

## Value per cost (numerator and denominator named; every denominator is a count read from a committed file)
| line | output tokens | divided by | result |
|---|---|---|---|
| blind extractor per attributable seizure-outcome row coded | 73,560 | 43 attributable rows of 206 rows (it_extractor_20261116/sealed/extraction.tsv) | 1,711 per attributable row; 357 per row |
| matrix cell second read per cell | 32,907 | 25 cells | 1,316 per cell |
| judging, all three runs, per hypothesis judged in round 1 | 138,135 (of which the invalid run 54,395) | 24 hypotheses (judge_table_run2.tsv) | 5,756 per hypothesis |
| leap round, delegate arms plus all judging, per round-1 survivor (S1 all four criteria) | 204,355 | 1 survivor(s) in round 1 (UNBLINDED.md) | 204,355 per survivor |
| the simple-search baseline arm alone, per survivor it produced | 23,658 | 1 survivor (UNBLINDED.md: H-B1) | 23,658 per survivor |
| judging arm B (5 hypotheses plus the planted pair) | 13,098 | 5 arm B hypotheses (it_arm_b_20261116) | 2,620 per hypothesis |
| blind audit of the closing synthesis (checks, not production) | 80,641 | 76 turns | 1,061 per turn |
| round 1b survivors under the definition S1, by arm (n, S1) | | | Memory-free baseline 2 of 5; ADV 0 of 5; HE 3 of 4; IT 2 of 5; SCI 2 of 5 |

## CI: one line per run of the public-release-gate workflow, #872 to #893 (source: GitHub API `actions/runs`, jobs and check-run annotations)
| run | commit | conclusion | minutes | cause (read from annotations) or note |
|---|---|---|---|---|
| #872 | b007645ec | success | 67 | success (last green before the HB1 package) |
| #873 | 5c5780f2b | failure | 58 | red: HB1 package registered at 010a59b63 without a PKG_MAP entry (test_stage_it47.py, test_design_rows_he50.py) |
| #874 | 81c546f52 | failure | 56 | red: HB1 package registered at 010a59b63 without a PKG_MAP entry (test_stage_it47.py, test_design_rows_he50.py) |
| #875 | df71e1a66 | failure | 56 | red: HB1 package registered at 010a59b63 without a PKG_MAP entry (test_stage_it47.py, test_design_rows_he50.py) |
| #876 | d22156eeb | failure | 73 | red: HB1 package registered at 010a59b63 without a PKG_MAP entry (test_stage_it47.py, test_design_rows_he50.py) |
| #877 | 379b81766 | failure | 57 | red: HB1 package registered at 010a59b63 without a PKG_MAP entry (test_stage_it47.py, test_design_rows_he50.py) |
| #878 | 43cb01b9e | failure | 56 | red: HB1 package registered at 010a59b63 without a PKG_MAP entry (test_stage_it47.py, test_design_rows_he50.py) |
| #879 | db027e20f | failure | 57 | red: HB1 package registered at 010a59b63 without a PKG_MAP entry (test_stage_it47.py, test_design_rows_he50.py) |
| #880 | a0bc5e0c7 | failure | 82 | red: HB1 package registered at 010a59b63 without a PKG_MAP entry (test_stage_it47.py, test_design_rows_he50.py) |
| #881 | 4d0dbe3aa | failure | 65 | red: HB1 package registered at 010a59b63 without a PKG_MAP entry (test_stage_it47.py, test_design_rows_he50.py) |
| #882 | ce6c79f82 | failure | 85 | red: HB1 package registered at 010a59b63 without a PKG_MAP entry (test_stage_it47.py, test_design_rows_he50.py) |
| #883 | 57869c9ba | failure | 66 | red: HB1 package registered at 010a59b63 without a PKG_MAP entry (test_stage_it47.py, test_design_rows_he50.py) |
| #884 | a0f9d2024 | failure | 57 | red: HB1 package registered at 010a59b63 without a PKG_MAP entry (test_stage_it47.py, test_design_rows_he50.py) |
| #885 | 9b02cc69d | failure | 66 | red: HB1 package registered at 010a59b63 without a PKG_MAP entry (test_stage_it47.py, test_design_rows_he50.py) |
| #886 | 49a1f8753 | failure | 67 | red: both causes present: HB1 mapping (it47/he50 suites) and reach_cahoy.tsv row width (test_structured_data_integrity.py); no repair in the commit |
| #887 | 98542e035 | failure | 57 | red: reach_cahoy.tsv line 3 has 2 cells in an 8-column table (test_structured_data_integrity.py only; HB1 suites green after the repair 98542e035) |
| #888 | 09c9644df | failure | 51 | red: reach_cahoy.tsv line 3 has 2 cells in an 8-column table (test_structured_data_integrity.py only; HB1 suites green after the repair 98542e035) |
| #889 | 4018c31ab | failure | 52 | red: reach_cahoy.tsv line 3 has 2 cells in an 8-column table (test_structured_data_integrity.py only; HB1 suites green after the repair 98542e035) |
| #890 | 0f11e8595 | failure | 76 | red: reach_cahoy.tsv line 3 has 2 cells in an 8-column table (test_structured_data_integrity.py only; HB1 suites green after the repair 98542e035) |
| #891 | a2ca70a8e | failure | 66 | red: reach_cahoy.tsv line 3 has 2 cells in an 8-column table (test_structured_data_integrity.py only; HB1 suites green after the repair 98542e035) |
| #892 | 120c3abe4 | success | 77 | success (first green after the two repairs: SCI's reach_cahoy.tsv row padded at 120c3abe4) |
| #893 | da4f7a957 | success | 66 | success (head with both repairs) |

19 red runs (#873 to #891), 1,202 run-minutes on the CI machine, all from two causes, both repository-side and both reached `main` before the gate could see them: (1) HB1 mapping, #873 to #886, repaired by 98542e035; (2) `reach_cahoy.tsv` row width, #886 to #891, repaired by SCI's 120c3abe4. First green runs: #892 (120c3abe4) and #893 (da4f7a957, the head with both repairs and ADV's closing records). #871 and #872 are the last green runs before the HB1 package; #891 stays red because it precedes the repair. These counts are CI minutes read from the API, not tokens and not money.

## What these lines can and cannot say
* The authors' (ADV, HE, IT, SCI) output per hypothesis is NOT separable: each session did other work in the window, so no authors' survivors-per-token figure is given. A session's whole-window output is in the first table and is an upper bound on what its leap file cost.
* Round 1 and round 1b used different survivor definitions and the numbers differ strongly (e.g. HE's four hypotheses: 0 survivors in round 1, S1 3 of 4 in round 1b); the two rounds are reported side by side, never merged.
* Cache read dominates every row (long contexts re-read each turn); it is a measure of context size, not of work, and is listed so nobody divides by it by mistake.
* A delegate's row is read at the `--until` time; IT's own notes (JUDGE_RUN2.md) read the run-2 judge earlier (71 turns, output 56,810) and the transcript has grown since, so the two can differ by the turns taken after IT's reading.
* The window ends at the `--until` time given; rerun at the closing time. Delegates that were still running at that time are counted up to it.
* **Final rerun, 15:10Z.** 13 delegates: the 12 of IT's `it_synthesis_audit_20261116/IT_DELEGATE_COSTS.md` (530,674 output tokens, same per-delegate figures as read here) plus one dispatched by SCI (readiness sheets producer), which IT's table does not list. The audit is checks, not production; arm A, arm B, extractor and judges are production for the leap and the matrix.

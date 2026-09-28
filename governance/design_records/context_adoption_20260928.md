# Context reduction and full record-scoped adoption — 2026-09-28 (second harness run)

> **Non-normative design record**, harness only. Actor: Harness Engineering (`plan`), autonomous
> queue of 2026-09-28 carrying the operator's decisions **A** (working model: Option A) and **B**
> (paper registry: Option A). Figures are bytes unless stated; token figures are bytes / 4,
> **estimates** (no tokenizer is installed). Follows [`harness_cost_20260928.md`](harness_cost_20260928.md).

## Landed

| Block | Commit(s) on `main` | What |
|---|---|---|
| Paper registry record-scoped (B) | `84b57cd` | `batch_commit.py propagate` covers all four current files; a refusal writes nothing and prints `FULL_FALLBACK <file> <code>`; Phase 4.0 states the never-force rule and the J3 + J5 evidence |
| Replay tool on today's editor | `77b4548` | `record_edit_bench.production_anchor`: nested-section `--heading` (+`under`) or `to_eof` when the record really is last — the two ways past `UNBOUNDED_SPAN` production uses |
| Waiting by identity | `b5bf8fc` | `CLAUDE.md` routes "waiting for a job you started" to `process_wait.py` |
| Remote-first landing | `b61fbac` | `task_close` deletes a branch cut from `origin/main` (upstream dropped only after ancestry is verified) and prints a `PUSH_NOTE` naming unpublished foreign commits on main |
| Working model split (A) | `c5eb296`, `001b1ea`, `0bfe4c2`, `afbaa15` | `BATCH_20260928_004` (structural): see [its report](../../disease-models/wwox/research/session_evaluations/2026-09-28_BATCH_20260928_004.md) |

## Measured

**Replays with today's editor.** Frozen J2 corpus: every family's figures identical to
`j2_results.json` (working model 41 / 41 in both modes; paper registry its one J2 miss, as frozen);
control 69 / 69. J5: identical to `j5_results.json` (328 / 328). Seven post-J4 batches, all four
files, production path: 27 events, 0 refused, 0 lost, 0 silent, R = X 27 / 27. The earlier
misreport was the benchmark's id anchor, not production.

**Paper-registry write surface, seven real batches (record granularity, `under` on).**

| Per batch | Mean | Median | Max |
|---|---:|---:|---:|
| FULL path (file in + out) | 1,182,761 | 1,181,388 | 1,215,272 |
| record-scoped: records read | 16,271 | 9,175 | 41,439 |
| record-scoped: ops written | 16,546 | 11,699 | 33,561 |
| record-scoped total | 32,817 | 20,874 | 58,711 |

Reduction per event 95.1–98.8 %; apply 0.10–0.34 s, verification ≈ 0.01 s; fallback frequency in
replay **0 / 7**.

**Hot scientific context** (routes that load the working model and claim registry whole):
316,834 → **244,383** B (−72,451 B, −22.9 %, ≈ −18 k tokens est.). The cold history
(76,266 B) is loaded by no route. Startup bootstrap (`CLAUDE.md`, manifest, `LEGEND_CORE`, role,
start/close skills, ≈ 87 KB) unchanged but for one router row.

**Retrieval after the split.** Frozen Benchmark I: identical (reads are bound to historical
parents). Today's history-inflated query: 224,603 → 148,251 B (−34 %); largest record
54,816 → 15,170 B. Preload decision unchanged.

**Runtime.** Battery sums 474.6 / 476.1 / 510.7 s across this run's three full batteries (135
suites, 0 red), within load noise (load average 1.1 → 2.2); no runtime change was attempted.

## Scratch census (`/tmp`)

| Class | What | Size | Action |
|---|---|---:|---|
| DEAD_OWNER_REAPABLE | `legend-selftest-tracer-*` — residue of the leak fixed in `42770a3`; each holds only a copy of a tool constant | 3,460 dirs (≈ 26 MB of files) | **reaped** after byte-matching the content against every historical `_TRACER` and checking no live process's environment named it; 48 whose content matched no version kept |
| UNATTRIBUTED | ~20 hand-named verify clones (`legend-aqp-*`, `legend-weekly-*`, `legend-b*-verify`, `legend-he-*`), 32–53 h old; all clean, no commit absent from the repository | ≈ 2.4 GB | **kept** — no owner recorded; destructive cleanup of unattributed scratch is the operator's |
| UNATTRIBUTED | `/tmp/legend-startup-context-audit`: a worktree directory whose registration is gone, 457 h | 35 MB | kept, same reason |
| LIVE_OWNED | five registered `/tmp/legend-orch-*` / `legend-scientist-r7` worktrees | ≈ 260 MB | kept |

No defect in `owned_scratch`: none of these was created through it. The clones' absence of owner
metadata is the gap; using `owned_scratch.make` for verify clones would make them reapable.

## Why `pgrep -f` happened

A HARNESS session loads the router, the manifest, `LEGEND_CORE` and its role — none named
`process_wait.py`; the rule lived in `parallel_legend_protocol.md` and the scripts README. A
routing defect, fixed by one router row; the runtime's own completion notification remains the
first choice (`process_wait.py`'s docstring).

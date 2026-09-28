# Harness cost — baseline, census and measured reductions, 2026-09-28

> **Non-normative design record**, harness only. Actor: Harness Engineering (`plan`), autonomous
> queue *measure and reduce real harness cost*, operator absent. Nothing here changes a claim, the
> working model, an evidence grade, a registry, a ledger or a routing rule. Every figure names the
> command or script that produced it; the scripts used for the transcript and replay figures were
> run read-only from a session scratchpad and are described well enough to re-run.

- **Tree measured:** `main` = `c38da96` (= `origin/main` after the concurrent actor pushed),
  clean task worktree, 4 CPUs, load ≈ 1.1 from one other live actor.
- **Comparability.** Only same-machine, back-to-back figures are compared below. The 2026-09-24
  figures in [`harness_baseline_20260924.md`](harness_baseline_20260924.md) are context only
  (different container, 114 suites then, 135 now).

## 1 · Baseline (P0)

| Command | Result |
|---|---|
| `python3 scripts/run_release_regressions.py` | **578 s wall** (`/usr/bin/time`), 558.8 s summed over **135** suites, **0 failing**, verdict `PASS WITH SKIPS` (33 skips: `files/` is gitignored in a fresh worktree) |
| `python3 scripts/public_release_gate.py` | **25.7–28.9 s**, `VERDICT: PASS`, `BLOCKS: 0` |
| `python3 framework/scripts/batch_queue.py --root . --check …/batch_queue.md` | **45–50 s**, exit 0 (116 s under `cProfile`) |

Top suites (seconds): `test_repository_surface_determinism` 145.4 · `test_batch_queue` 102.2 ·
`test_self_test_coverage` 35.5 · `test_registry_records` 27.4 · `test_phase_handoff` 20.9 ·
`test_scientific_consistency` 18.5 · `test_paper_packet` 14.8 · `test_pathograph` 13.7 ·
`test_structural_analysis` 13.7 · `test_regenerate_adjudications_fails_closed` 12.4 ·
`test_documented_commands` 11.2 · `test_benchmark_input_surface` 10.8 · `test_repo_root` 10.4 ·
`test_session_self_eval` 9.6 · `test_legend_handoff` 8.1. **The first two are 44 % of the sum.**

Where the time goes (per-test timing, `unittest` cases run one by one):

- **`test_repository_surface_determinism` (≈124 s):** one test runs the full release gate twice
  (53 s); six tests each spawn `test_documented_commands.py` (≈9–10 s each). `git worktree add`
  costs 0.3 s. Both are intentional end-to-end arms — **not optimised**.
- **`test_batch_queue` (≈92 s):** two tests each paid one full classification of the seed
  (44 s + 40 s) — one in-process through the memoised `build(ROOT)`, one in a **subprocess**
  that rebuilt the same report from scratch. **Duplicated work — fixed, § 5.**
- **`batch_queue` itself:** ≈92 % of its profile is `difflib.SequenceMatcher.ratio` inside
  `study_dedup_triage.match_row` — 706 unmatched seed titles × ≈270 full ratios against 1,052
  records.
- **Release gate:** `scan_privacy_and_secrets` ≈ 22 s of ≈ 29 s over 1,633 text files / 48 MB.

## 2 · Context census (P1)

No tokenizer is installed (`tiktoken`, `anthropic` absent); token figures are **bytes / 4,
estimates**.

**Documented hot load, per route** (what each route's own SKILL / manual says to load whole):

| Surface | Bytes | Routes that load it whole |
|---|---:|---|
| bootstrap: `CLAUDE.md` 9,985 · `AGENTS.md` 5,486 · state manifest 18,620 · `LEGEND_CORE.md` 33,605 · `legend-start` 4,957 · capability-scout 9,908 · takeaways 4,824 | **87,385** (~22 k tok est.) | every route |
| role contract | 5,165–18,342 | every route |
| `working_model_current.md` | **109,924** | MINIMAL / STANDARD / FULL, `legend`, `legend-deepdive`, `legend-discovery`, forge, aso-designer (at comparison, after the first pass, under `SOURCE_FIRST`) |
| `claim_registry_current.md` | **206,910** | same |
| WM + claims pair | **316,834** (~79 k tok est.) | same — was 193,566 at G1 (2026-09-26): **+64 % in two days** |
| `paper_registry_current.md` / literature log | 610,302 / 525,964 | FULL only; every other profile reads records via `registry_records.py` |
| `fulltext_read_receipt.md` | 59,906 | every full-text route (on demand) |
| `prompt_batch_commit.md` | 32,631 | batch commit |
| `scientist_standing_brief.md` | 21,008 | scientist dispatch |

**What the growth is.** Working model: `Last update` stack 23,858 B + `## Changelog` 39,797 B +
three batch sections 11,467 B ≈ **75 KB history-shaped (≈68 %)** against ≈35 KB live model.
**Both G1 revival triggers have fired** (> 80 KB; history > 60 %) — see § 8. Claim registry:
+71,811 B since the M1 cut, all inside claim bodies (CLAIM 011 +9.8 KB, 037 +8.5 KB, 002 +8.1 KB,
030 +8.0 KB …) — scientific content, not harness material.

**What sessions actually load** (52 post-M1 transcripts, bytes of tool results that touched a
LEGEND surface, classified read-only):

| Actor class | n | LEGEND-surface bytes median / p90 | of which registries median / p90 | claims median | WM median |
|---|---:|---:|---:|---:|---:|
| scientist (batch / adjudication) | 13 | 114,871 / 187,637 | 58,117 / 100,463 | 15,449 | 9,772 |
| mirror | 6 | 76,763 / 121,311 | 55,721 / 110,977 | 15,512 | 27,424 |
| workflow agents | 16 | 73,460 / 104,568 | 26,022 / 76,388 | 4,834 | 0 |
| harness | 12 | 57,332 / 121,060 | 4,740 / 32,644 | 179 | 0 |

`Read` calls on the WM: **0**; on the claim registry: 5 (all ranged). The adjudication and batch
routes do **not** follow the documented whole-file preload — they reach records by `sed`/`grep`
and `registry_records.py`. That is consistent with Benchmark I (the preload binds the comparison
step of a *reading*), and it is recorded, not changed: no post-M1 transcript was a comparison
after a `SOURCE_FIRST` first pass.

## 3 · J4 in production (P2)

Seven post-J4 propagation commits (`c99dfe5`, `1cdb1a4`, `95bd885`, `bc09bc9`, `da8b08b`,
`c5eec22`, `67ac5ec`) replayed deterministically, no model calls: hunks labelled with the J0
cascade (`record_edit_bench.label_file`), range ops derived and applied in memory by
`record_scoped_edit.py` to the parent's bytes, compared with the child. Batch reports of
0927_003, 0928_001, 0928_002 and 0928_003 record production use of the editor with **0
refusals**; the ops files themselves were not persisted, so the replay re-derives them.

| Family | Events | Full path (file in + out) | Record-scoped (records read + ops written) | Reduction | Apply / verify |
|---|---:|---:|---:|---:|---|
| claim registry | 7 | 2,376,994 B | 340,459 B | **85.7 %** | 0.58 s / 0.02 s total |
| literature log | 6 | 6,264,756 B | 20,872 B | **99.7 %** | 1.13 s / 0.11 s |
| working model | 7 | 1,138,018 B | 562,083 B | **50.6 %** (upper bound: whole BLOCK read) | 0.19 s / 0.02 s |
| paper registry (still FULL) | 7 | 8,279,328 B | 150,796 B | 98.2 % *if it were scoped* | 2.57 s / 0.12 s |

- **Correctness:** silent corruption **0** in every event; every accepted op reproduced its
  intended hunks; untouched units byte-equal in every event. Where the replay result differs from
  the child it is only on hunks the labeller marks `UNRESOLVED`, as in J2.
- **Instrument gap found:** with today's editor every WM event is **refused** with
  `UNBOUNDED_SPAN` — the safety rule of `e9c9172` (2026-09-28) refuses an `id: BLOCK 3` op whose
  assumed span swallows `## Changelog`. The J2 deriver anchors by `id`. Against the frozen J1
  editor (`50d9d39`) the same WM events replay **7/7 with 0 refusals, 0 silent**. Production uses
  `--heading` anchors and is unaffected; the benchmark deriver is what needs a heading anchor
  before J2 can be re-run on the current editor.
- **Verification cost does not offset the gain:** apply + post-condition ≤ 0.9 s per event against
  a model-visible saving of 0.3–1.0 MB per paper-registry-sized file.
- The **largest remaining rewrite surface is the paper registry**: ≈1.2 MB in + out per batch.

## 4 · Adoption after M1 (P3)

Same classifier and cut as M1 (`e30b8ec`, 2026-09-26T20:39Z), 52 transcripts (2 main, 50
subagents / workflow agents), plus the receipt ledger.

| Measure | M1 (2026-09-26) | Now |
|---|---:|---:|
| readings (receipts authored after the cut) declaring `context_policy` | 0 / 29 | **22 / 22** (all `QUESTION_DRIVEN`; the 2 non-readings — a correction, an adversarial re-analysis — excluded) |
| transcripts declaring a policy | 0 / 42 | 16 / 52 |
| transcripts retrieving from the large surfaces that used `registry_records.py` | 1 / 12 | **26 / 36** |
| targeted retrieval acts / manual lookups (id + theme) | 2 / 103 | **102 / 386** |
| dispatches sending an agent to LEGEND records that name the tool | 0 / 10 | **21 / 23** |
| `SOURCE_FIRST` readings | 0 | 0 — every post-cut reading held a prior and said so |

Misses, classified: the manual lookups concentrate in batch actors (an `old` string for
`replace-within` needs the exact bytes and line — **legitimate exception**) and in Mirror reviews
(**agent non-adoption**, no routing defect found: the Mirror role contract is not a retrieval
route). Full-text dispatches without a policy line (21 / 27) are Orchestrator dispatches of
scientist packages whose receipts then declare it (**legitimate: the brief carries it**).
**Adoption is materially improved; no new enforcement added.**

## 5 · Changes landed

| # | Problem | Evidence | Change | Effect | Commit |
|---|---|---|---|---|---|
| C1 | `self_test_coverage._tracer_dir()` never removed its `/tmp` directory | 3,474 `legend-selftest-tracer-*` dirs on this host, 883 in 24 h, **17 per suite run** (counted before/after one run) | `guarded_run` and `survey` remove it in `finally`; test setUps register cleanup; new test pins the exact directory | 0 per run; new test fails on the old code | `42770a3` |
| C2 | `test_committed_queue_is_current` rebuilt the batch queue in a subprocess although the same process already builds it | 44.2 s + 40.0 s for two tests over one identical report | calls `bq.main()` in-process with the same argv; same `--check` branch, message, exit code | `test_batch_queue` **92.5 s → 52.9 s**; planted drift still fails with `DRIFT:` | `5d19719` |

## 6 · Refuted / not adopted

| Candidate | Result | Why not |
|---|---|---|
| Visit `match_row` fuzzy candidates in descending exact `quick_ratio` bound | **exact** — 0 differences over 2,812 calls (706 real, 400 perturbed, 300 tie cases) | 191 k of 196 k `ratio()` calls remain: the character-multiset bound is far above the best ratio of an unmatched title. 45.5 → 43 s, inside noise |
| Release gate: ask distinct words (`set(findall)`) before the per-token loop | **exact** — byte-identical gate output; identical 81-finding set on a tree with planted fixtures | 41 files / 9 MB still contain a three-letter sensitive token inside digests and run the loop; ≈2 s of ≈26 s. Not worth touching a privacy control for <10 % |
| Faster `git worktree add` in the determinism suite | — | 0.3 s; the suite's cost is its intended guard subprocesses |
| Working-model / claim-registry retrieval change | — | not attempted (P6): decisions stand without a new benchmark |

## 7 · Process and worktree hygiene (P9)

- Orphan LEGEND processes (PPID 1): **none**. `process_wait` timeouts in transcripts: none seen.
- `git worktree list`: 26 entries, all clean (`branch_hygiene.py`); `prunable`: 0. Five `/tmp`
  task worktrees and 20 `.claude/worktrees/*` belong to other actors — listed, not removed.
- `/tmp/legend-*`: 3,601 entries, ≈2.4 GB. The count was the tracer leak (fixed, C1); the bytes are
  verify clones of other actors (`legend-weekly-*-verify`, `legend-aqp-*`, ≈150 MB each) — not
  task-owned, not removed. **One mechanism recurred and is fixed; nothing else recurred.**

## 8 · Ranked remaining bottlenecks

| Bottleneck | Frequency | Measured cost | Avoidable | Confidence | Action |
|---|---|---|---:|---|---|
| WM history in every scientific preload | every reading comparison, forge, deep dive | ≈75 KB of 110 KB (~19 k tok est.) per load | ≈68 % of the WM | high (bytes), medium (loads — § 2 shows adjudication routes don't load it whole) | **HUMAN_REQUIRED** — G1 triggers fired |
| Paper-registry FULL rewrite in `BATCH_COMMIT` | every batch that touches it (6 of 7 recent) | ≈1.2 MB in + out per batch | ≈98 % | high | J5 only if a heading-path anchor passes a new pre-registered replay |
| `batch_queue` fuzzy classification | every build: Phase 4.7, freshness checks, the suite (once now) | ≈40 s | unknown without a tighter exact bound | medium | a real upper bound on `ratio()` (e.g. per-row LCS on the top-k) is research, not a micro-fix |
| Release gate privacy scan | every landing, the battery twice | ≈22 s | ≈2 s exact | high | no change |
| Determinism suite's gate + guard arms | every battery | ≈120 s | 0 (intentional) | high | no change |

## 9 · HUMAN_REQUIRED

**WM size (G1 revival).** 109,924 B, history-shaped ≈68 %. *Option A:* the Scientist writes the G1
A3 qualifications into live sections through a `BATCH_COMMIT`, after which the history can move to
a cold file and every scientific route sheds ≈75 KB. *Option B:* keep the whole-file preload and
raise the trigger. The harness can measure either, but choosing is a scientific-canon decision.

## 10 · Re-running

- Battery / gate / batch_queue: commands in § 1, timed with a Python `perf_counter` wrapper.
- Per-test timing: load the suite module, run each `TestCase` alone, time it.
- J4 replay: for each commit and current file, `record_edit_bench.commit_context` +
  `label_file` + `resolve_commit`, then `replay_event(…, sha[:12], labels, "range")` (the 12-char
  prefix matters: hunk ids are keyed on it); WM rows also against `50d9d39`'s editor.
- Transcripts: every JSONL event after the cut, `tool_use` inputs classified as in M1 § 2 and
  each `tool_result` sized against the surface its call touched.

# Generated-tree H2 — freshness verified on the exact candidate tree

> **Non-normative design record.** Harness Engineering roadmap v1.1, Wave 4, item
> "generated-tree H2" (distinct from `safe_push` H2). It follows
> [H0](h0_generated_surface_drift_20260924.md), which found one cause with three entry points:
> regeneration of the committed derived surfaces exists only in BATCH_COMMIT Phase 4.7, while
> direct landings also write their inputs. The operating rule lives where it applies —
> `parallel_legend_protocol.md` rule 2, `prompt_batch_commit.md` Phase 4.7,
> `fulltext_read_receipt.md` — and the routing in `framework/scripts/README.md` § 7.

## Measured first (2026-09-26)

Each generator's own check, run on a clean checkout:

| Surface | `main` = `990b6f6` | `main` = `e30b8ec` (candidate-tree run, `--all`) |
|---|---|---|
| coverage_report | OK, 0.8 s | FRESH, 0.6 s |
| reading_state | CURRENT, 0.4 s | FRESH, 0.2 s |
| batch_queue | OK, 48.1 s | FRESH, 95.1 s (host under load) |
| pathograph inventory + export | CURRENT, 3.7 s | FRESH, 3.1 s |
| surface_census | no check by design | NO_CHECK |

`main` was fresh: A3d's regeneration had held. The defect H0 describes is latent, not present.

## What was built

`framework/scripts/candidate_tree_freshness.py` materializes the candidate tree from git objects
into a private temporary directory (a temporary index, `read-tree` + `checkout-index`; no
worktree is registered), discovers the surfaces with the release suite's own
`generated_surfaces()` (now taking a `root`), runs only the checks whose inputs the candidate
changes relative to its base, and reports `FRESH · STALE · NOT_AFFECTED · CHECK_ERROR` (plus
`NO_CHECK` for the census). Exit 0 / 1 / 2.

- **Candidate shapes.** `--merge TIP --base main` (the ort merge `task_close` performs, via
  `git merge-tree --write-tree`); `--staged`; `--paths` (HEAD + exactly the named files, what
  `legend_commit.sh` commits); `--candidate REV` (audit a landed commit against its parent).
- **Inputs.** Declared per generator from its own `derived_inputs` call and widened where the
  generator reads more (batch_queue scans every `*_current.md`; coverage_report reaches
  `research/` through `growth_anchors`), plus the surface and its companion outputs, plus the
  transitive closure of the generator's local imports computed in the candidate tree. A
  discovered surface with no declaration is `CHECK_ERROR`: unknown is never a pass.
- **Replay of H0's transitions** with the new tool: `--candidate c9914f9` → coverage_report and
  reading_state STALE; `--candidate 3bd71c8` → pathograph STALE. The tool would have refused
  both landings H0 names.

## Wiring

| Landing path | What it checks | On STALE / CHECK_ERROR | Override |
|---|---|---|---|
| `task_close.py` | the merge result of the task tip into the current `main`, before the lock; re-checked under the lock if `main` moved | refuse, main untouched, regeneration commands printed | `--stale-surfaces-because "<reason>"`, printed |
| `scripts/legend_commit.sh` | HEAD + the named files, under the commit lock, before `git add` | exit 5, nothing staged | `LEGEND_STALE_SURFACES_BECAUSE="<reason>"`, recorded as a `Stale-surfaces-because:` trailer |
| `fulltext_receipts.py record` | — (flag, not gate) | prints the two regeneration commands and the candidate check | — |

`record` flags rather than regenerates: `coverage_report` reads the whole registries directory,
and regenerating it inside `record` would bake in a peer's in-flight registry edit (C22, 2026-09-09).
The gate that makes the flag binding is the commit wrapper.

**Not covered, stated so nobody over-reads it:** a plain `git commit` that bypasses both tools.
No hook is installed — the runtime guard and its hooks were retired by operator decision on
2026-09-07 (`4341ef9`). The per-surface drift suites still catch it after the fact.

## Latency

| Candidate | Checks run | Wall time |
|---|---|---|
| harness-only (`5e5f160`, a `framework/scripts` change outside every closure; `--paths README.md`) | 0 | 0.9 s |
| registry change (`752ae4a`, literature log) | 3 (batch_queue dominant) | 47.8 s |
| receipt append (`c9914f9`) | 4 | 86.3 s (batch_queue 84.5 s, host under load) |
| test fixtures (`test_task_close.py`, 17 prior tests) | 0 | suite 6.2 s → 6.2 s |

Checks run in parallel, so wall time is the slowest affected check. `batch_queue.py` is the
whole cost of a scientific landing; it reads the receipt ledger, so a receipt landing
legitimately pays it.

## The leaked worktrees

`/tmp/tmpwea7wqn_/tree` (2026-09-14, planted `[[a-target-that-does-not-exist-xyz]]` in
`governance/ANNEX_INDEX.md`) and `/tmp/tmp37jhblwn/tree` (2026-09-26, planted
`vendored_untracked/.git`) were disposable checkouts of `scripts/test_repository_surface_determinism.py`,
identified by their planted edits. Their cleanup was correct but ran only via `addCleanup`: a
process killed mid-test never reached it — reproduced with SIGKILL, which leaves the worktree
registered. Repair: `framework/scripts/owned_scratch.py` stamps a box with `PID:START`
(`process_wait.py`'s identity) and reaps dead owners' boxes together with the worktrees
registered inside them. Applied to that suite and to the three siblings that register
worktrees on the real repository (`test_repo_root.py`, `integration_matrix.py`,
`claim_retrieval_bench.py`). Both leaked worktrees were removed; six other `/tmp/tmp*/tree`
directories belong to other actors' temporary clones, not to this repository, and were left.

## H3 — further refinements, re-evaluated

- **`reading_state.md` on demand (H0's H1): not implemented.** The drift it would remove is now
  refused at landing, and 85 tracked files name `reading_state` — a reference migration with
  no remaining staleness to buy.
- **Faster `batch_queue` check: not implemented.** It is the only cost above a second; it is
  paid only by landings that change its inputs, and a narrower input map would trade
  correctness for time without evidence that the time is harmful. Revisit when a measured
  landing is refused or abandoned for latency.

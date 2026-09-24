# H0 — why four generated surfaces went stale together

> **Non-normative design record.** Harness Engineering roadmap v1.1, Wave 1, block H0: a
> read-only diagnosis, made **before** any surface is regenerated (A3d), so the cause is
> established on the state in which the defect was found. Nothing is repaired here.

## Question

At `main` = `3501f19` the drift checks of `coverage_report.md`, `batch_queue.md`,
`reading_state.md` and the pathograph inventory/export all fail. Did one cause or four?

## Method (reproducible)

- A full, non-shallow clone of `main` (1103 commits). The working clone of the session was
  shallow (50 commits), and the first replay could only show that all four surfaces were
  already stale at `62218b6`, its oldest commit.
- For each surface: `R` = the last first-parent `main` commit that modified it (its last
  regeneration). Its own check is then run at **every** first-parent commit after `R`
  (142 commits); `batch_queue` (~64 s per check) is run at every commit after `R` that
  touched its inputs or generators (`disease-models/wwox/registries`, `…/research`,
  `framework/scripts/batch_queue.py`, `study_dedup_triage.py`) plus the tip — 68 commits.
- The checks are each generator's own, run with the generator code of that commit:

  | Surface | Check |
  |---|---|
  | coverage_report | `python3 framework/scripts/coverage_report.py --root . --check disease-models/wwox/registries/coverage_report.md` |
  | reading_state | `python3 framework/scripts/reading_state.py --root . --check disease-models/wwox/registries/reading_state.md` |
  | batch_queue | `python3 framework/scripts/batch_queue.py --root . --check disease-models/wwox/registries/batch_queue.md` |
  | pathograph | `python3 framework/scripts/pathograph.py --disease wwox --verify --out …/pathograph_inventory.md --export …/data/pathograph_export.jsonl` |

- Every check kept its command, stdout, stderr, exit code and elapsed time, and was
  classified `PASS · REAL_DRIFT · GENERATOR_ERROR · HISTORICAL_INCOMPATIBILITY ·
  NOT_APPLICABLE`. A non-zero exit is `REAL_DRIFT` only when there is no traceback and no
  usage error; the drift outputs were also read (each says the surface "no longer matches"
  or "has drifted from its sources").

## Result — 494 checks

| Surface | Last regeneration | Checks | PASS | REAL_DRIFT | Other | Only transition (PASS → REAL_DRIFT) |
|---|---|---:|---:|---:|---:|---|
| coverage_report | `094c9ba` (2026-09-21 15:07) | 142 | 28 | 114 | 0 | `c2d45d2` → **`c9914f9`** |
| reading_state | `094c9ba` | 142 | 28 | 114 | 0 | `c2d45d2` → **`c9914f9`** |
| pathograph | `094c9ba` | 142 | 38 | 104 | 0 | `aa7a81c` → **`3bd71c8`** |
| batch_queue | `bbf2c6c` (2026-09-21 23:30) | 68 | 34 | 34 | 0 | `0e13f9e` → **`817a0d0`** |

- Every regeneration was fresh at its own commit; each surface has exactly **one** transition
  and never recovers; no `GENERATOR_ERROR`, no `HISTORICAL_INCOMPATIBILITY`.
- The three transition commits (all 2026-09-22, all **single-parent direct commits on
  `main`**, none a `BATCH_COMMIT`, none a merge through `task_close.py`):
  - `c9914f9` *The receipt I owed…* — appended one event to `fulltext_read_receipts.jsonl`
    (the receipt writer also re-anchors the state manifest). Inputs of `coverage_report` and
    `reading_state`.
  - `3bd71c8` *PROPAGATED under operator authorization…* — edited `claim_registry_current.md`
    and `working_model_current.md` outside a batch commit. Input of the pathograph.
  - `817a0d0` *The predictor we were leaning on is inverted…* — edited
    `full_text_queue_current.md`. Input of `batch_queue`.

## Diagnosis

**One cause, three entry points.** Regeneration of the committed derived surfaces exists in
exactly one place — `prompt_batch_commit.md` Phase 4.7 — while their inputs are also written by
direct landings that never pass through it: a receipt recording, an operator-authorized direct
propagation, and an analysis commit touching the full-text queue. LEGEND_CORE §21e makes such
landings legitimate and requires only LINT for scientific-file changes, so nothing on those
paths runs the drift checks. The surfaces then stay stale until the next batch commit.

This supports the roadmap's H2 direction (freshness evaluated on the fast landing path, against
the exact candidate tree) and H1 (`reading_state.md` on demand: it went stale on the very first
receipt after its regeneration). Neither is implemented here.

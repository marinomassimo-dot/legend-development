# Harness baseline — 2026-09-24

> **Non-normative design record.** The before-state for the Harness Engineering roadmap v1.1
> (Wave 0, block B0). Every figure names the command that produced it, so a later wave can
> re-run the same command and compare. Nothing here is a rule, a gate or a target.

- **Repository state measured:** `main` at `3501f19f80fbda9b6f7ee32da117683f0bfcfdbb`, clean detached worktree, 4 CPUs.
- **Timings are wall-clock seconds on one container run.** Treat differences under ~10 % as
  noise; the container is shared with other processes.
- **Machine speed is not stable across containers.** The same battery at the parent commit
  `f3d890c` summed to ~512 s earlier the same day on a different container; here it sums to
  ~1032 s. A before/after comparison is therefore only valid when both trees are timed back to
  back on one machine — which is how the end-of-wave comparison is made.

## 1 · Regression battery

Command (sequential, one process per suite — the runner's own execution model, timed
outside it because the runner printed no per-suite time before block B0b):

```bash
python3 scripts/run_release_regressions.py --list > list.txt
while read -r t; do s=$(date +%s.%N); timeout 900 python3 "$t" >/dev/null 2>&1; rc=$?; \
  printf '%.2f\t%s\t%s\n' "$(echo "$(date +%s.%N) - $s" | bc)" "$rc" "$t"; done < list.txt
```

- **Suites:** 114 · **summed suite time:** 1032.4 s · **wall:** 1033.5 s
- **Failing suites:** 12
- **Tracked files changed by the battery:** none

| Seconds | Exit | Suite |
|---:|---:|---|
| 428.7 | 1 | `scripts/test_repository_surface_determinism.py` |
| 214.3 | 1 | `framework/scripts/test_batch_queue.py` |
| 55.3 | 0 | `framework/scripts/test_self_test_coverage.py` |
| 25.0 | 0 | `framework/scripts/test_legend_handoff.py` |
| 21.1 | 0 | `framework/scripts/test_repo_root.py` |
| 20.5 | 0 | `framework/scripts/test_registry_records.py` |
| 20.1 | 1 | `framework/scripts/test_pathograph.py` |
| 18.3 | 0 | `framework/scripts/test_benchmark_input_surface.py` |
| 17.3 | 0 | `framework/scripts/test_artifact_index.py` |
| 16.5 | 0 | `framework/scripts/test_integration_matrix.py` |

Failing suites at baseline:

- `framework/scripts/test_batch_queue.py`
- `framework/scripts/test_coverage_report.py`
- `framework/scripts/test_pathograph.py`
- `framework/scripts/test_reading_state.py`
- `scripts/test_documented_commands.py`
- `scripts/test_fresh_clone_reader_journey.py`
- `scripts/test_link_targets.py`
- `scripts/test_locator_obligation_reaches_every_route.py`
- `scripts/test_release_surface.py`
- `scripts/test_repository_surface_determinism.py`
- `scripts/test_scientific_consistency.py`
- `scripts/test_skill_packages.py`

## 2 · Single-command timings

| Command | Result |
|---|---|
| `python3 scripts/public_release_gate.py` | 150.6 s (exit 2) |
| `python3 framework/scripts/batch_queue.py --root . --check disease-models/wwox/registries/batch_queue.md` | 95.2 s (exit 1) |

## 3 · Generated-surface drift (each surface's own check; exit 0 = fresh)

| Command | Result |
|---|---|
| `python3 framework/scripts/coverage_report.py --root . --check disease-models/wwox/registries/coverage_report.md` | 0.7 s (exit 1) |
| `python3 framework/scripts/reading_state.py --root . --check disease-models/wwox/registries/reading_state.md` | 0.3 s (exit 1) |
| `python3 framework/scripts/pathograph.py --disease wwox --verify --out …/pathograph_inventory.md --export …/pathograph_export.jsonl` | 3.5 s (exit 1) |
| batch_queue `--check` (above) | see §2 |

## 4 · Release gate verdict at baseline

`python3 scripts/public_release_gate.py` → **`VERDICT: BLOCK_PUBLICATION`, `BLOCKS: 1`**:
`PARENT_OF_ORIGIN_VARIANT_LINKAGE` in `disease-models/wwox/handoff/Q230P_HANDOFF_TO_TOOLED_INSTANCE_20260924.md:8`,
introduced by `3501f19` (the tip of `main` when this baseline was taken). It is privacy-relevant
content outside the harness programme and is **not** repaired by any Wave 0/1 block. The
acceptance criterion used by those blocks is therefore *an identical finding set before and
after the block* — no finding added, none hidden — rather than a green verdict.

## Static measurements

```text
## sizes (wc -c)
   77352  framework/state/state_manifest_current.md
   53902  disease-models/wwox/registries/working_model_current.md
  127862  disease-models/wwox/registries/claim_registry_current.md
    9916  CLAUDE.md
## routing coverage: files naming the tool among .claude roles framework/manuals framework/protocols framework/instruction CLAUDE.md AGENTS.md
registry_records: 5 files
paper_packet: 1 files
## retrieval failures (registry_records.py get ...; exit 1 = NO RECORD MATCHED)
get --id DL-BIO-001 --source discovery_ledger_current: exit 1
get --id DIS-001 --source dismissal_ledger_current: exit 1
get --theme myelin --source discovery_ledger_current: exit 1 (term occurs 7 times in the file)
## forced-output wording locations (file:line)
.claude/skills/legend-capability-scout/SKILL.md:3
.claude/skills/legend-capability-scout/SKILL.md:23
.claude/skills/legend-capability-scout/SKILL.md:25
.claude/skills/legend-capability-scout/SKILL.md:159
.claude/skills/legend-discovery/SKILL.md:22
.claude/skills/legend-hypothesis-forge/SKILL.md:3
.claude/skills/legend-hypothesis-forge/SKILL.md:63
.claude/skills/legend-session-takeaways/SKILL.md:114
.claude/skills/legend-start/SKILL.md:12
.claude/skills/legend/SKILL.md:70
.claude/skills/legend/SKILL.md:83
.claude/skills/legend/SKILL.md:129
framework/protocols/session_self_evaluation.md:164
## worktrees / processes
prunable worktree entries (git worktree list --porcelain | grep -c prunable): 0
live self-matchable waiters (ps -eo args | grep -c -E '[p]grep -f'): 0
```


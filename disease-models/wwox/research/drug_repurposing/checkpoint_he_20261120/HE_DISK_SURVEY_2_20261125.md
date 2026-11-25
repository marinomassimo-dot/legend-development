# Disk survey 2: growth, and what can be removed (HE 02915fa6, 2026-11-25 15:45 to 15:56Z)

Report only. **Nothing was deleted by this survey; ADV decides the cleanup.** Read after `HE_DISK_SURVEY_20261125.md` (survey 1, 15:29Z). Sizes are allocated blocks counted once per inode ("freed if removed": all hard links inside the item). Scripts and raw data, outside git: `files/coordination/he_disk_survey_20261125/` (`disk_survey.py`, `disk_growth.py`, `classify_worktrees.py`, `tmp_signatures.py`, `*.json`).

## 1 Where we are

- Free: 20.28 GB at 15:45:50Z (trigger: 15 GB). Earlier readings: about 24 GB at 12:30Z, 19 GB at 15:15Z, 20.01 GB at 15:29Z (before HE removed its own 1.2 GB clone).
- Net rate 12:30Z to 15:15Z: about 1.8 GB per hour. At that rate the 5.3 GB margin lasts about 3 hours; at the 24 h average of surviving new bytes below (0.65 GB per hour), about 8 hours. Sizes here are in 10^9 bytes; `df -h` shows 19G.

## 2 Growth per area

Bytes of **surviving** inodes by birth time (`statx`), at 15:47Z. Files created and already deleted are invisible; so this is what stayed on disk, which is what fills it.

| area | last 1 h GB | last 3 h | last 6 h | last 24 h |
|---|---|---|---|---|
| worktrees | 0.96 | 2.00 | 4.66 | 7.83 |
| home (outside the repo) | 0.11 | 1.01 | 1.41 | 3.04 |
| job folders | 0.04 | 0.18 | 1.44 | 2.28 |
| repo root (`files/`, `.git`) | 0.06 | 0.62 | 0.96 | 1.26 |
| transcripts and `~/.claude` | 0.03 | 0.11 | 0.16 | 0.43 |
| `~/.local/share` | 0.00 | 0.00 | 0.00 | 0.40 |
| `/tmp` | 0.08 | 0.13 | 0.15 | 0.25 |
| total | 1.29 | 4.05 | 8.79 | 15.51 |

**Half of the growth is worktrees**: each new one costs about 0.5 GB (0.46 GB for the three born in the last hour), and one is made per window rollover. 15 worktrees were born in 24 h. Survey 1 to survey 2 (16 min): worktrees 17 to 19.

## 3 Safe to remove now

| item | GB | rule it passes |
|---|---|---|
| worktree `sci_ah_land` | 0.53 | HEAD in main, clean, no ignored file, no process, no session launched there. **But it is SCI's second landing worktree (named in SCI 0d0c6dc3's transcript): ask SCI first.** |

No `/tmp` clone is REMOVABLE by `tmp_clone_report.py` (106 candidates, 0). No other worktree passes all the rules today.

## 4 Becomes removable on a stated condition

| items | GB | condition and rule |
|---|---|---|
| worktrees `he_o_20261125`, `it_17_20261125`, `it_18_20261125`, `sci_ag_20261125` | 2.12 | pass everything except "transcript newer than 24 h" (quiet 5.2, 5.2, 3.2, 2.2 h at 15:48Z): eligible on 2026-11-26 from about 10:40Z, 10:40Z, 12:40Z, 13:40Z, if re-run `classify_worktrees.py` still says so |
| worktrees `he_n`, `he_p`, `he_q`, `sci_aj` and the other windows of 2026-11-25 | about 0.5 each | their window must be retired (a live process today), then 24 h |
| `he_s_20261125` | 0.53 | previous HE window: 24 h after retirement |
| worktrees `it_19`, `it_fu_20261124`, `it_successor_n_20261120` | 1.51 | an ignored `backup/` folder each (20 files, about 4.5 MB: BATCH_COMMIT snapshots). `git worktree remove` deletes ignored files **without asking**: copy `backup/<stamp>/` to the root `backup/` first (or confirm it is not needed). `it_successor_n` also holds 6 orphan browser processes |
| `adv_successor_a_20261120` | 0.53 | ADV's own live window: no |
| `he_g_20261123`, `p022b` | 1.01 | held by orphan browser processes (operator's list); `p022b` also has ignored `.log` analysis outputs that may be the only copy |
| `/tmp/legend-meeting-cross-runtime-20261123` | 0.45 | `codex/*` branch not in main: waits for the operator's backup-push answer |

**Rule used for a worktree:** HEAD an ancestor of `development/main`; no tracked or untracked change; no ignored file except regenerable caches; no process working in it or naming it; no CURRENT window and no live session launched there; newest transcript of its project folder older than 24 h. A window that works in a worktree it was not launched in is NOT detected (see `sci_ah_land`): ask the owner.

## 5 Large items that need an owner's or the operator's decision (not on any safe list)

| item | GB | what it is, read only |
|---|---|---|
| `/tmp/claude-1000` | 20.85 | excluded by the standing rule. 20.78 GB are the scratchpads of the root-project sessions, 18.96 GB of them of session `4325d70d` (last transcript 2026-11-19, not listed, no process): downloaded public data (JUMP parquet 1.0 GB, ecKG edges 0.85 GB, GIN zip 0.69 GB, DepMap CSVs), a venv, history blobs. 10 tracked files name paths under it (task files and a verification note; no full-text receipt). Largest single recovery on the machine; **operator's rule, operator's call** |
| `/tmp/tmp*/repo` (805 folders) | 5.47 | **leaked by one test**, see section 6. Content is a copy of `framework/scripts` plus a synthetic PDF. Rule: folder `tmp*` whose only entry is `repo`, which holds exactly `disease-models`, `files`, `framework`; older than 1 day; no process names it. No tool removes these today (`tmp_clone_report.py` never lists them: no `.git`) |
| `/tmp/tmp*` browser profiles | 2.5 | 6 of `chromium-stderr.log,profile` (1.28 GB, 0.5 to 17 days) and 10 older full profiles (1.2 GB, 23 to 27 days); no process names them |
| `/tmp/tmpr1z1_3h6` | 0.51 | one folder of full-text receipt JSONs, 17 days |
| `/tmp/legend-ethosuximide-inputs`, `legend-wwox-qr-inputs`, two dashboard release folders, others without `.git` | 4.0 | "only their owner can judge" (tool's words) |
| `~/legend_browser_tmp` (312 entries) | 1.67 | browser temporary folders (the largest are 160 to 200 MB profiles), 0.73 GB born in 24 h |
| job folders | 4.25 | `5fef7cc4` 1.18 GB (1.1 GB `adv275` download, IT PREVIOUS, born 6 h ago), `3b826442` 0.53, `961aabbb` 0.36, `b3e65c69` 0.28. Rule: job of a PREVIOUS window retired more than 24 h ago; ADV or the owner confirms nothing there is the only copy |
| `~/.vscode`, `~/.config`, `~/.vscode-server`, `~/.codex`, `uv` cache, `~/.local/share` | 21 | the operator's tools, not the laboratory's |

## 6 One producer found: a test that leaks 27 MB per run

`framework/scripts/test_regenerate_adjudications_fails_closed.py`, inner function `fresh()` (about line 287): `build(Path(tempfile.mkdtemp()) / "repo")` four times, never removed. Each copy holds all of `framework/scripts`. 805 such folders since 2026-10-28, 5.47 GB, 12 of them today. **Reproduced** with `TMPDIR` pointed at an empty folder: one run of the suite left 4 folders, 37 MB. **Fixed in this landing** (`dir=self.tmp`, which `setUp` already removes): the same run leaves 0, 27 tests pass. The folders already there are not touched.

## 7 Recommendation

1. The leaking test is fixed (section 6). Whether the other suites leave anything material is read from the `/tmp` listings around the 4-worker battery of the same day.
2. Put to the operator, once: may the 19.4 GB scratchpad of the closed session `4325d70d` and the 5.47 GB of leaked test folders be removed? Together about 24 GB, which ends the pressure.
3. Until then: remove `sci_ah_land` if SCI agrees (0.5 GB), and the four worktrees of section 4 row 1 on 2026-11-26.
4. Standing cost to lower next: 0.5 GB per window worktree. A window that reuses its predecessor's worktree, or a retirement step that removes the predecessor's worktree after 24 h, are the two options; not measured further here.

## 8 Done after the report (16:13 to 16:29Z)

- **ADV's decision: remove the leaked sandboxes, bounded** (exact form `/tmp/tmp<8>/repo`, own user, unchanged for 6 h, no process with a working directory, open or mapped file inside, listed first, exact-path loop, parent removed only if empty). HE added one condition: `repo` holds exactly the test's three folders. List rebuilt just before: 793 pass, 16 modified in the last 6 h. **Removed 793 folders and their 793 empty parents; free space 18,847 to 23,918 MiB (+5.0 GiB)**; 16 `repo` folders remain. Own processes whose descriptor tables could not be read at the final listing: 4. List and removed list: `files/coordination/he_disk_survey_20261125/leaked_repo_{list,removed}.txt`.
- **Ignored `backup/` folders** (it_19, it_fu, it_successor_n): one batch snapshot of 20 files each; 19 are byte-identical to blobs reachable from `development/main`, the 20th is a note naming the base commit (that commit is in main, nothing was dirty). ADV will not copy them.
- **Correction to section 4:** `it_19` has an ignored `backup/` and a window that wrote on 2026-11-25 about 15:35Z, so it is eligible after about 15:40Z on 2026-11-26, not in the morning.
- **The check is now a tracked tool:** `python3 framework/scripts/branch_hygiene.py --removal --main development/main` (report only).
- **Browser profile folders** (`~/legend_browser_tmp`, 7 of 1.36 GB; those of section 5 in `/tmp`): the youngest seen dates from 2026-11-25 12:46Z, before the producer fix of 13:30Z (a2b46d713). None newer was seen. Not removed; not in ADV's decision.

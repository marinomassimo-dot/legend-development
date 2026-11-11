# Disk pressure on the VPS — measured 2026-11-11 (read-only analysis, nothing deleted)

Filesystem `/`: 193 GB, 174 GB used, 20 GB free (90%). All sizes below are **unique blocks** (`du` run once over several paths, so a hard link counts once). Earlier per-directory figures that were measured one directory at a time over-count shared files.

## Where the 174 GB is

| Area | GB | Static or growing |
|---|---|---|
| `legend-development/files/` (gitignored corpus) | 61 | **static since 2026-10-28/31** (`files/geo` 55: GSE92742 43.7 + other series) |
| `legend-development/.claude/worktrees/` (33 worktrees) | 12 | slow |
| `legend-development/.git` | 0.5 | slow |
| `/home/desktop` other (`.cache` 8.4, `.claude` 5.1, `.vscode` 4.3, `.config` 2.2, `.local` 1.5, `q230p-tooluniverse-blind/.venv` 5.8) | ~27 | slow |
| **`/tmp`** | **~63** | **growing: this is the fast part** |
| `/root` 7.5, `/var/lib/snapd` 3.5, logs 0.1 | ~11 | static |

`/tmp` was not in the first breakdown. Measured file by file (st_blocks, files with a single link; files hard-linked into `files/` count zero), without per-directory rounding:

| `/tmp` part | GB | What it is |
|---|---|---|
| Battery / publication / landing clones (103 directories: `it44_batt_*`, `bat_it4*`, `pub*_it4*`, `legend_batt_*`, `it44_land`, `it43_pub`, `headcopy`, `legend-ci-*-verify`) | 33.7 | one `git clone --no-hardlinks` per battery or publication check, about 1 GB each; `files/` inside them is hard-linked and costs nothing; none has a live process inside (checked through `/proc/*/cwd` and open file descriptors) |
| `/tmp/claude-1000/...` session scratchpads (169 sessions) | 23.1 | one old session (`4325d70d`, 2026-10-26/27) holds 21.5 GB of its own scratch (`dl` 2.1, `v20` 2.0, `hist_blobs` 1.9, `ecKG` 1.35, `it12b` 1.0, `raw` 0.9 ...) |
| `tmp*` directories from tests (4,966; 4,188 older than 12 h) | 6.2 | test scratch, several 0.3-0.4 GB ledger clones (`FTR-*.json` receipts) and headless-Chromium profiles |
| 16,665 `org.chromium.Chromium.*` directories | 0.1 | many, but tiny: not a space problem (a first estimate of 17 GB was an artefact of rounding every small directory up to 1 MB) |
| deleted-but-still-open files held by live processes | 0.1 | negligible |

Growth per day, new `/tmp` data by modification date (excluding the session scratchpads): about 0.2-0.3 GB/day until 2026-11-05, 1.6 / 0.3 / 1.7 / 4.0 GB on 11-06..09, **20.1 GB on 11-10 (19.0 of it battery clones)** and **9.7 GB so far on 11-11 (8.9 clones)**. The rise follows the number of parallel sessions each running a battery or a publication check. `files/geo/GSE92742` has not changed since 2026-10-28: it is the largest single item but it is not what is growing.

## GSE92742 (LINCS level 5), 55 GB in `files/geo`

| File | GB | Role | Last read |
|---|---|---|---|
| `...Level5...n473647x12328.gctx.gz` | 21.3 | the downloaded original (checksum in `GSE92742_SHA512SUMS.txt.gz`) | 2026-10-28 |
| `...Level5...gctx` | 23.4 | `gunzip -k` copy of the file above; read only by `lincs_it3_local_level5.py extract` (its docstring says so) | atime 2026-10-28 07:37 |
| `cache_it3/extract.npy` | 11.9 | extract of trt_cp / trt_sh.cgs signatures; read by `score`, `report` and by `generation_it9_p2.../seed_sig_arm.py` | |
| `cache_it3/scores.npy` + small files | 1.9 | scratch, "git-ignored" per the script | |

The `.gctx` is a regenerable decompressed copy (`gunzip -k`, minutes); the cache is regenerable from it. Nothing after 2026-10-28 read the `.gctx`. **Link count is 48**: the `.gctx`, the `.gz` and the cache files are hard-linked into the `files/` of many battery clones, so deleting the name in the repository frees nothing until the clones are gone. Order matters: clones first, then the file.

## Recoverable space and what each step needs

| Step | GB freed | Risk | Needs |
|---|---|---|---|
| 1. Remove finished battery / publication / landing clones in `/tmp` (103 directories, none with a live process inside) | ~34 | none for the repository: clones of committed SHAs; logs are kept in `*_keep` folders | most belong to other sessions (IT/SCI): the Orchestrator or the operator decides, owner by owner |
| 2. Remove the old scratchpad of session `4325d70d` (15 days old) and scratchpads of other ended sessions | ~22 | scratch of a closed session; anything cited in a record was copied into the repository | operator decision (not mine) |
| 3. Remove `tmp*` directories older than 12 h with no live process inside | ~5 (unique) | none expected: test scratch | same |
| 4. After step 1, remove the `.gctx` (its link count must read 1) | 23.4 | rebuild = `gunzip -k` of the kept `.gz` (22 GB written once, minutes) only if `extract` is ever rerun; the cache `extract.npy` serves the later stages | operator decision |
| 5. Optional: `cache_it3` | 13.8 | rebuild = gunzip + `extract` + `score` (hours) | not recommended now |
| 6. `q230p-tooluniverse-blind/.venv` (5.8: NVIDIA/CUDA 3.2, torch 1.2, triton 0.9) | 5.8 | an environment, not data; recreate from a requirements file if one exists | only when that project is idle; not needed |

Steps 1-4 together free about 85 GB (disk from 90% to about 46%), with no scientific information lost.

## Why it will keep growing, and the smallest fix

Each battery creates its own ~1 GB clone and no step removes it; test suites create `tmp*` directories. The ledger clones that receipts trials use are 0.3-0.4 GB each. A closing step in the battery procedure ("copy the log to `*_keep`, remove the clone with a literal path") costs one command per battery and stops the accumulation; the same for the scratch clone of a receipts trial. A read-only lister (what is in `/tmp`, how old, whether a live process is inside, unique size, hard-link aware) would let the Orchestrator apply step 1-3 without guessing; it removes nothing.

Removal of other sessions' directories is not done here: the classifier and the standing rule require authorisation, and the directories are not mine. My own clones (`he42..he45` batteries) were removed after each battery.

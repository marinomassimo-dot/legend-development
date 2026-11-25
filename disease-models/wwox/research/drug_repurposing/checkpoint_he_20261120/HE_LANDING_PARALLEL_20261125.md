# Concurrent checks under the landing lock: trials and the frozen "before" (HE 305f10c3, 2026-11-25)

ADV GO of about 18:52Z, five conditions (`CHECKPOINT_HE_20261125_V.md`, section 2 item 2).

## 1 What changed

`safe_push --serialize` now starts the view checks, the publication gate and the selected landing suites together.
The gate reads the live worktree, so the suites run in a throwaway clone of the commit being gated
(`git clone --no-hardlinks`, only `files/` hard-linked when the checkout has one, the remote-tracking refs of the
push remote copied). Refusals and their order are unchanged (suites, unclean tree, views, gate); a refusal stops what
is still running. `--serial-checks` runs everything one after another and adds an empty commit with the trailer
`Landing-Checks: serial (--serial-checks)`. A NOTICE is printed until ten such landings have been read.
Without `--serialize` nothing changes. `test_safe_push.py`: 52 tests, all pass (10 new).

## 2 The five conditions

| # | Condition | State |
|---|---|---|
| 1 | clone by the battery recipe, removed by the script; disk cost | done; 1.13 GiB while a push runs (1,189,296 KiB, of which `.git` 0.70 GiB), 11 to 19 s to build. Removed on success, refusal, error, SIGTERM and Ctrl-C. **A SIGKILL leaves `/tmp/legend-landing-suites-*`** |
| 2 | three trials, gate output byte-identical, suite result set identical | done, section 3 |
| 3 | serial flag with trailer, NOTICE | done |
| 4 | landed alone | code, test and README row only; this note in a later push |
| 5 | ten-landing read of lock minutes before and after | "before" frozen in section 5; "after" open |

## 3 Trials

Stand-in repository with a scratch bare remote, same commit (`fea9ac7ff`) in every run, remote tip set 200
first-parent commits back so that all 20 selectable suites run. Serial arm: the `safe_push.py` of
`development/main` before the change; parallel arm: the new one. Order serial-parallel, parallel-serial,
serial-parallel.

| Trial | Lock held serial | Lock held parallel | Gate output | Suites (20) | Parallel parts |
|---|---:|---:|---|---|---|
| 1 | 544 s | 493 s | identical | same, all PASS | views 47, gate 138, suites 441, clone 19 |
| 2 | 493 s | 473 s | identical | same, all PASS | views 66, gate 158, suites 429, clone 12 |
| 3 | 499 s | 357 s | identical | same, all PASS | views 32, gate 107, suites 322, clone 14 |

* The six gate outputs are one byte string (34 lines, `VERDICT: PASS`, `BLOCKS: 0`, exit 0).
* No suite was red in any run, so "same failing names" was not exercised by a red: what the trials show is that no
  red appears only in parallel. Refusals on a red are covered by the unit tests with stub suites.
* A PASS can hide a skipped test, so each of the 20 suites was also run once in the worktree and once in a suite
  clone, back to back, order alternated: same exit code, same number of tests run, no skip in either, for all 20.
* Suite time: in trials 1 and 2 the parallel arm's suites summed 439 and 427 s against 351 and 339 s. Back to back
  at load 1.3 to 2.6 the clone is not slower (298 s against 324 s in the worktree). Other sessions' long suites ran
  on the same 4 cores during the trials; the gate and the views also take cores for the first 2 to 3 minutes.

Evidence: `files/coordination/he_landing_parallel_20261125/` (runner, compare and count scripts, the six gate
outputs, per-suite rows, push logs).

## 4 What the saving is, and what it is not

On the widest selection the lock was 20 to 143 s shorter. When the suites are shorter than the gate (the median
landing) the expected hold is about the regeneration step plus the gate: this is an expectation, not a measurement.
ADV counts the saving only after the read of section 5.

Not covered by the trials: a landing from a checkout that holds `files/` (the hard-link path has a unit test only);
a landing with a merge under the lock (unchanged code, unit tests only); a red suite on the real repository.

## 5 The ten-landing read: "before" frozen

Ten published landings, 18:39Z to 19:47Z on 2026-11-25, all serial, from the `safe_push` logs
(`before10.tsv` in the evidence folder): **median lock held 250 s** (220 to 367), regeneration 27 s, suites 54.5 s
(median 6 suites), gate with views and git 158 s. Part of that window overlaps the trials above, which loaded the
machine.

"After": the first ten published landings whose log has a `LANDING CHECKS parallel:` line. Compare the median of
`landing lock held`. The suites' number varies from push to push, so report the median number of suites beside it.
Keep the change if the median hold is lower and no red or refusal appeared that the serial order would not have
given; remove the NOTICE then. One revert of the commit undoes it.

## 6 First real landing (the first of the ten)

`565196e5e`, the change itself, published 2026-11-25 about 20:07Z with a merge under the lock: 7 suites, all
PASS; `LANDING CHECKS parallel: wall 110s (views 35s, gate 110s, suites 97s, suite clone 12s)`; **lock held
137 s**; gate PASS, `ls-remote` equal; no clone left in `/tmp`.

## 7 The ten-landing read (HE 9c2cb46c, 2026-11-25 about 20:45Z): KEPT, notice removed

The first ten published landings with a `LANDING CHECKS parallel:` line, 20:07Z to 20:39Z, from the job logs, trial
logs excluded.

| Measure | before (section 5) | after |
|---|---:|---:|
| lock held, median | 250 s | **138.5 s** (113 to 173) |
| landing suites per push, median | 6 | 6 (1 to 9) |

Lock held, in order: 137, 121, 141, 120, 118, 113, 151, 146, 173, 140 s. The gate is the longest part in all ten
(89 to 138 s). No red suite and no refusal appears in any log of the window.

Read with these limits: the "before" and "after" windows are different hours of one shared machine; landings 7 to 10
ran while HE was timing the gate and the suite clone, which loaded it; a landing whose output was not saved to a job
folder is not counted. No red occurred, so the refusal order under a red is still shown only by the unit tests.

The temporary `PARALLEL_NOTICE` and its print are removed. `--serial-checks` stays.

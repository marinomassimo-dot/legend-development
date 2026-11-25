# Which suites hold the gate's minutes, and one change (HE, 2026-11-25)

ADV's item: name the suites that hold the release gate's 50 to 88 minutes and propose the one change with the best minutes per risk. ADV accepted the change below on one condition: a warm gate cache must be shown unable to hide a real block. No workflow file is touched.

## 1. Where the minutes are

First CI run with per-suite times, #2428 (commit f093ab03), read from the public annotations:

| part | seconds |
|---|---|
| regression step | 3,750 |
| publication gate step | 510 |
| sum over 276 suites | 3,385 |
| `test_repurposing_view.py` | 996 |
| `test_repository_surface_determinism.py` | 758 |

Those two suites are 52% of the suite time. Locally, one test of the second, `test_a_stray_git_file_cannot_suppress_a_real_block`, took 503 of about 760 seconds inside a full run of the suite: it runs the whole publication gate twice.

## 2. The change

The two gate runs of that one test now use `--cache` with a private cache file in the test's own scratch box, outside the tree under test and empty at the start. The first run scans everything; the second answers unchanged files from the first. Nothing else uses it, and the gate itself is unchanged.

Why the cache cannot hide what the test looks for: it stores the privacy findings of one file under the gate's own bytes, the path and the content. Which files are walked is decided again on every run, and the link scan that the test asserts is never cached.

## 3. ADV's condition, shown

Scratch checkout, one shared host, 2026-11-25 about 11:07 to 11:26Z.

| step | result |
|---|---|
| cold gate on the clean tree | PASS, 216 s, 15,400 misses |
| a broken wikilink planted after it, warm run | **BLOCK** (`BROKEN_WIKILINK`), 33 s, 15,399 hits and 1 miss |
| the same plus the stray `governance/.git` marker, warm run | **BLOCK**, 33 s, 15,400 hits |
| mutation: the old name-only nested-checkout predicate put back, then the changed test | **the test FAILS** ("a one-line untracked file turned a BLOCK into a PASS"), 234 s |

A planted change in a file the privacy scan reads is a different content, so a different key; `test_public_release_gate_cache.py` already holds that case.

## 4. Before and after

The one test, back to back, same host, load average about 3 to 4:

| form | wall seconds |
|---|---|
| before (commit b0c73b89) | 396 |
| after | 251 |

**145 s saved, 37% of that test.** The same test took 503 s in an earlier full run of its suite, so the host's load moves the figure. The CI effect is not measured; read it from the per-suite time of `test_repository_surface_determinism.py` in a run holding this change, against 758 s in #2428 (one run each, so a difference under about 100 s says nothing).

## 5. Not done

`test_repurposing_view.py` is the larger consumer (996 s). Its per-test times were not collected here.

## 6. Baseline for the landing refusal (frozen before any later read)

`safe_push --serialize` has refused a push that turns a selected landing suite red since d3d1f94b (published about 11:21Z). Read at about 11:09Z, before it: over the gate's last 95 runs (7 h 33 min), 44 completed `failure` and 41 `success`, so 52% of the 85 concluded runs failed.

Prediction, to be read after 2026-11-26 11:21Z over runs of commits after d3d1f94b: no red caused by a suite the selection named for that landing, from a publisher whose worktree held the new script. Rejected by one such red. A red from a suite the selection did not name is a selector gap and counts against the selector, not the refusal. The failed share is reported beside it and is not the test: one cause can hold many runs red.

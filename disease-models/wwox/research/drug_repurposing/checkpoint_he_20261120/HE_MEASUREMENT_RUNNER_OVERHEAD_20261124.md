# Measurement, 2026-11-24 (HE, ADV-220): where the runner's 336 s between suites goes

Read-only measurement; no change to the runner. Source: the serial profile run of `scripts/run_release_regressions.py` on main `6dcf2b67d` (wall 5,633 s, suite time 5,297 s over 271 suites, so 336 s outside the `TIME` lines) and a direct timing of the runner's own post-suite step in the same battery clone.

## What the step is
After every suite the runner calls `tracked_state(GUARDED_TREES)` (`scripts/run_release_regressions.py`, once before the battery and once after each suite): `git ls-files -z --cached --others --exclude-standard` over eight trees (disease-models, governance, roles, framework/protocols, framework/instruction, framework/state, learning, ledger), then `git hash-object --stdin-paths` over every file listed. It compares the result with the previous state; a difference names the suite that wrote under a guarded tree and fails the verdict whatever its exit code.

## Numbers (warm file cache, five repetitions each)
| Part | Time |
|---|---|
| files listed under the guarded trees | 14,861 files, 397.9 MB |
| `git ls-files` | 0.03 s |
| `git hash-object` over those files | 0.94 to 1.01 s (the first, cold call: 6.2 s) |
| `tracked_state` in all | median 1.04 s |
| a bare Python start | 0.012 s |
| `os.stat` of the same 14,861 files | 0.03 s |

272 calls (271 suites plus the baseline) at 1.04 s is about 283 s, which is 84 percent of the 336 s. The remaining 53 s (about 0.2 s per suite) was not decomposed: it is the runner's own output handling and the slower, colder reads of a run shared with live sessions.

## What it protects
The 2026-09-10 incident: 54 tracked dossiers under disease-models were overwritten with the seven bytes "touched" during an unattended run and nothing could say which suite did it. The comment above `GUARDED_TREES` still says "one `git ls-files -s` per suite, no content read"; that was true of the first version and is no longer true, because the index blob does not move when the working tree is written, so the state now hashes the working tree.

## Reading, not a change
The cost is the content hash, not the file listing or process start. A cheaper guard would compare `os.stat` (size and mtime) and hash only what changed, about 0.03 s against 1.04 s per suite, and would save roughly 270 s of a 94-minute run (about 5 percent). It would also change what the guard can see (a write that restores size and mtime), so it is a decision for a gate owner, not made here. The stale comment is the only thing wrong today.

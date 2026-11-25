# Design note for the operator: an opt-in cache for the publication gate's per-file privacy scan (ADV-057; HE, 2026-11-18)

Written for: the operator (through ADV's decision page). Non-canonical. Labels: MEASURED, ESTIMATED, ASSUMED. Nothing here is turned on: the cache is OFF by default and no push uses it unless you say so.

## The decision in one sentence
**Whether a push may use a stored result of the gate's per-file privacy scan for files whose bytes and for a gate script that have not changed, instead of re-reading all 11,686 files at every landing.** The gate still runs on the exact commit being pushed, under the landing lock, before every push (section 21d unchanged); only how its answer for unchanged files is obtained changes.

## What changes, and what does not
| Changes | Does not change |
|---|---|
| `scripts/public_release_gate.py` gains `--cache`, `--no-cache`, `--cache-verify` and the environment switch `LEGEND_GATE_CACHE=1`. With any of them on, the privacy scan of a file whose key is in the cache returns the stored findings instead of scanning | The default: no flag and no variable means today's behaviour, byte for byte, and **nothing is written** (tested) |
| A cache file `<git dir>/legend_gate_cache/privacy_v1.json` (sealed, rewritten atomically, holds only the current run's files) | `safe_push.py` (not edited; it would pass the environment variable through to the gate if you choose to set it) |
| 12 new tests in `scripts/test_public_release_gate_cache.py` | Every detector pattern and digest list; which files are scanned (decided afresh each run); the link, README-consistency and provenance scans (cross-file, always run in full); the pre-check (never uses the cache); the clean clone |
Key of one entry = sha256(gate script bytes, Python version, relative path, bytes of the file). **Any edit of the script, of any pattern or digest in it, or of the interpreter, changes every key: the next run scans everything.** The bytes that are hashed are the bytes that are scanned (one read serves both), so a file that changes during a run cannot be filed under another file's hash.

## Evidence (MEASURED)
* 111 scans of the 66 fixtures of the existing gate suite (87 of them with BLOCK findings, including case linkage, parent-of-origin, identifiers, secrets, e-mail): no cache, cold cache, warm cache and `--cache-verify` give identical findings to the field; all 222 file lookups of the warm runs were hits.
* The whole existing suite passes again with the cache switched on for every gate it starts.
* On this repository (11,686 scanned files), three command-line runs, uncached, cold and warm, print **byte-identical output**: first on a tree that carried one real BLOCK (an e-mail in my own new test file, since fixed) and many REVIEW findings, all reproduced; then, on the final code, on the passing tree.
* Mutation: changing one detector pattern invalidates every entry; the file that was clean under the old script is rescanned and flagged (tested on a copy of the gate; the real detectors were not touched).
* A damaged, truncated, wrongly sealed, other-format or other-script cache gives a full scan with the same findings. A file whose name is not valid UTF-8 gives the same output cached and uncached.
* One independent reader (sonnet, medium; code and fixtures only) tried 15 attacks. Two broke the first version: an A-to-B-to-A edit during the scan (**fixed**: single read, with a test) and a non-UTF-8 file name (**fixed**). The third, below, remains.

## Saving (ESTIMATED from the measurements; log-based queue replays did not reproduce observed waits, so figures scale observed waits)
Whole gate on this tree, load average about 5 on 4 cores: uncached **237 s**, cold cache **222 s** (no slower; the first version measured 243 s against 240 s), warm cache **31.7 s** (-87%). The lock hold of a landing (median 3.5 min, of which the gate is about 3.2) would fall to about 0.9 min if the merge and push overhead is 20 s (ASSUMED); waits scale with it: median 2.8 to about 0.7 min and p90 10 to about 2.6 min (upper bounds). It also removes about 85% of the gate's CPU from a machine that already runs near load 5.

## Failure modes (what could go wrong, and what catches it)
1. **A cache whose entries were edited by someone who can write the repository's git directory, with the seal recomputed, would hide a finding.** The seal detects damage, not forgery (it is a plain digest; a secret key would sit in the same directory). The writer already has the power to edit hooks or the gate itself, so this is the same trust as the repository's own control files, but it is a new place to hide a finding. Catch: `public_release_gate.py --cache-verify` scans everything, compares with the stored entries, exits 3 on any difference and rewrites the cache; tested. Run it daily and before every release (one full scan, about 4 minutes, no new scheduler: ADV's recall can carry it).
2. A different Python version or a changed script: full rescan on the next run (a cost, not a risk).
3. Two gates on one cache file: atomic replace, the last writer wins; a torn file fails the seal and is ignored (tested with six simultaneous runs by the reviewer).
4. The cache cannot see cross-file effects: the three other scans run in full every time, as today.
5. Unreadable or vanished files, findings tied to no file: those runs store nothing and behave as today.

## The switch
Turn on for one run: `python3 scripts/public_release_gate.py --cache`; for pushes, the environment variable set by whoever pushes: `LEGEND_GATE_CACHE=1 python3 framework/scripts/safe_push.py development main --expect-sha <sha> --serialize` (the gate subprocess inherits it). **Turn off:** unset the variable, pass `--no-cache` (it wins over everything), or delete `<git dir>/legend_gate_cache/`. Audit: `--cache-verify`.

## The sentence to approve (or not)
"I approve pushes using the publication gate's opt-in per-file privacy cache (`LEGEND_GATE_CACHE=1`), on the understanding that it stores gate results inside the repository's git directory and is trusted like the repository's own hooks, that the gate still runs on the exact commit before every push, and that `--cache-verify` is run daily and before every release; I can switch it off by unsetting the variable."

## Update 2026-11-18 (HE, after the continuity mandate): the 20 s landing overhead, measured
The saving section above says the lock hold would fall to about 0.9 min "if the merge and push overhead is 20 s (ASSUMED)". That figure is now measured in part. Scratch clone of this repository (`--no-hardlinks`) against a local bare remote, the real `safe_push.py --serialize` with an empty commit each time, load average 2.6 to 5.3 on 4 cores (the job ran under `mandate_watch.py job run --memory-max 5G`):

| Landing (whole `safe_push.py`) | Wall time | Load |
|---|---|---|
| fast-forward, gate uncached | 314.4 s | 5.3 |
| remote moved, merge under the lock, gate uncached | 227.7 s | 4.1 |
| fast-forward, `LEGEND_GATE_CACHE=1`, cold | 217.7 s | 2.7 |
| fast-forward, cache warm | 30.9 s | 3.2 |
| remote moved, merge, cache warm | 25.9 s | 2.9 |
| same, with `GIT_TRACE2_EVENT` | 22.4 s | about 3 |

* **Git steps of a landing, MEASURED** (trace of the 22.4 s landing, against the local bare remote): fetch 0.04 s, merge 0.07 s, push 0.03 s, ls-remote about 0 s, three `status` 0.09 s in all: about **0.25 s** together.
* **The gate alone, cache warm, MEASURED** three times in the same clone: 28.5, 28.1 and 30.3 s. The whole landing (22.4 to 30.9 s) is not distinguishable from the gate alone at this noise: the non-gate part is within a few seconds, not 20.
* **Network to the real remote, MEASURED read-only** (five runs each): `git ls-remote` 1.2 to 1.9 s; a no-op `git fetch` 1.3 to 1.9 s with one 5.9 s outlier. The push of a small commit to the real remote was **not** measured (a test commit cannot be pushed there); the two real landings of today took 235 s and 277 s uncached, in the range of the uncached scratch landings (228 to 314 s), so they carry no separable overhead either.
* **Reading, ESTIMATED:** overhead outside the gate is about 0.25 s local plus fetch, push and ls-remote round trips, so roughly **3 to 8 s** at the real remote, not 20 s. With the cache warm a landing would hold the lock about 25 to 40 s instead of the estimated 0.9 min. The unexplained difference between the median hold (3.5 min) and the gate (3.2 min) in the queue logs is therefore probably queue and start-up time, or the longer gate under load, and was not located. Cache cold is no slower than uncached (217.7 s against 227.7 s and 314.4 s; the spread is load, not cache).
* Limits: one clone, empty commits (the cache-warm gate sees an identical tree; a real change adds re-scanning of the changed files only), a local remote, five network samples, load that varied between runs. Raw timings: scratch log of the run, summarised here; the scratch clone is not kept.

## Update 2026-11-18 (HE, battery on 6320348db5): the differential proof's base-suite size
The release battery on 6320348db5 failed `scripts/test_public_release_gate_cache.py` (`DifferentialSuite`): the proof pins the size of the base gate suite (`result.testsRun`, 70), and my pre-check REMINDER change (16e1468bb) added two tests to `scripts/test_public_release_gate.py`, so the base suite ran 72. The proof itself (identical findings cold, warm, verify and uncached for every fixture) was not what failed; the pinned count is now 72. The two new tests are fixtures of the pre-check output and use no cache. I ran `test_public_release_gate.py` after that change but not this suite, which is why the count was found by the battery and not before it.

## Update 2026-11-19 (HE): the pinned base-suite size is now 73
A third test in `scripts/test_public_release_gate.py` (the receipts-ledger reminder) raised the base gate suite from 72 to 73; the pinned count in `test_public_release_gate_cache.py` was updated in the same change, found by the lookup of suites that name the changed test file (README section 13), this time before the push.

## Update 2026-11-25 (HE): search guards in the privacy scan; pinned base-suite size now 76
The privacy scan now skips a search for a file that cannot match it: each guard names, for every alternative of its pattern, a literal that any match contains. Patterns, scope, allow-lists and verdicts did not change; the cache is as it was (off by default).

**Rule.** A differential over today's tree cannot see a pattern added tomorrow. A short-cut or cache in a privacy gate therefore keys on a digest of its own source and patterns and falls back to the full search on any change. Here: guards run only while `scan_source_digest() == GUARDS_WRITTEN_FOR`; `test_search_guards_are_in_force` fails until someone has re-read the guards and updated the digest. The first version lacked this and failed the pattern-mutation test of the cache suite.

**Proof, MEASURED on base 6af888dc5** (old script sha256 235e2854d11444b5…, new 81add1dcf1451910…):
* Findings identical, field by field and in order: the whole tree (31 and 31), the added or changed files of the last 50 first-parent commits (34 and 34), 121 planted trees (127 and 127). Whole gate output and exit code identical on the clean tree (PASS) and with the planted files in it (122 BLOCKs).
* One planted positive per guarded alternative, found by the old scan and the new. Each of 53 guard literals broken in turn: 53 detected.
* Cache present: a new alternative added to a pattern in a throwaway copy (private key form, AWS prefix, maternal word, person noun, country), a matching file cached clean by the unchanged gate: the mutated copy reports it with 0 cache hits; the same copy with the fall-back forced off misses it, in all five.
* Time, one run each on a shared host: whole gate 217 s to 118 s (clean tree), 242 s to 112 s (planted); privacy scan alone 201 s to 68 s. The cache suite's exact-tree comparison (`GATE_CACHE_FULL_TREE=1`) was not run.

**Open (ADV condition 5):** on each of the first three real landings after this one, read the findings count of the old and the new script on the landed commit and report.

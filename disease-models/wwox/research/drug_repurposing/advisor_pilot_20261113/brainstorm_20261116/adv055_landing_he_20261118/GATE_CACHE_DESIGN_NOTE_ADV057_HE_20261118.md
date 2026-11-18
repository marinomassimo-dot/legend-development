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

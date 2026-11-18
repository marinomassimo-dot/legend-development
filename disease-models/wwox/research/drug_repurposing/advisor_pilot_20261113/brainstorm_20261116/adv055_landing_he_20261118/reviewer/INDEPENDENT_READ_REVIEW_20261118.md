# Independent read: can the cached privacy scan PASS where the uncached one BLOCKs?
Non-canonical. Python 3.12.3. Experiments in this folder (t1..t6, g1, aba.py, h.sh, copies of gate_old.py and gate_new.py).
Comparison method: printed lines starting with '[' minus ' MISSING_' lines, old vs `--cache` cold and warm, LEGEND_GATE_CACHE_FILE in this folder.

## (a) Attack ideas

1. Poisoned or forged cache entry. Seal is a plain sha256 over the content, not a MAC and not keyed. Anyone who can write the cache file (or the `<git common dir>/legend_gate_cache/` dir, or set LEGEND_GATE_CACHE_FILE) can set an entry to [] and recompute the seal.
   Tried: tree t4 (a.md with an e-mail); cold run `--cache`; python rewrote the entry for key(a.md) to [] and called `gate.cache_seal`; warm run.
   Old: `[BLOCK] EMAIL_ADDRESS a.md:1`. New warm: no EMAIL line (hits=2, misses=0), the cache rewrote itself with the poison (stored=True). `--cache-verify`: exit 3 CACHE_MISMATCH, as designed.
   Verdict: BREAKS (needs write access to the cache; the test file `test_verify_mode_catches_an_entry_that_was_edited_and_resealed` already records it as "the stated limit"). The warm run does not even print that the cache is unauthenticated.

2. ABA race between scan and the post-scan re-hash. Code: after the scan, each miss is re-hashed and stored if `again == keys[rel]`. If the file is A at hash time, B (clean) while scanned, and A again at re-hash, the findings of B are stored under key(A).
   Tried: `aba.py` (monkeypatches `read_text` to write clean content once just before the first read of a.md, and restores the original bytes right after `scan_privacy_and_secrets` returns), tree t5, `LEGEND_GATE_CACHE_FILE=c5.json python3 aba.py`, then a plain warm run.
   Old (uncached, file = A): `[BLOCK] EMAIL_ADDRESS a.md:1`. New warm run after the raced cold run: hits=2, no EMAIL line. The poisoned entry is persistent: every later run with the same bytes passes that file, until the gate script changes or the file changes.
   Verdict: BREAKS, but only against a concurrent writer that toggles a file during the scan (the raced run itself is no worse than the old gate under the same race; the damage is that the wrong answer is persisted and reused). Simple edit A->B during the scan is handled correctly (re-hash differs, not stored; the recheck in RaceGuard covers that).

3. Non-UTF-8 file name (surrogateescape). Key construction does `f"...{rel}..."`.encode("utf-8").
   Tried: t3: file named b'bad\xff.md' containing an e-mail, `gate_old.py` vs `gate_new.py --cache`.
   Old: exit 2, the finding printed with a replacement character. New: exit 3, `GATE_ERROR: UnicodeEncodeError ... '\udcff'`, no cache file written, no findings listed.
   Verdict: HOLDS for the question (not a PASS, fail closed), but the output is NOT identical (exit 3 vs 2, no finding lines). Anyone who commits such a name can no longer use `--cache` at all; the cache silently degrades the report. Fix idea: encode with errors="surrogateescape" in the key and open the cache with the same.

4. Unicode / odd names: NFC vs NFD names, a name with newline and U+2028, upper-case `UP.MD`, `sub/x.JSONL`, invalid UTF-8 inside a file (read_text errors="replace"), `\r\n` and bare `\r` line ends (read_text translates newlines, the key hashes raw bytes).
   Tried: t2 and t1 (cold and warm).
   Old vs new cold vs new warm: identical (7 findings in t2, 8 in t1). HOLDS. Raw-byte hashing is strictly finer than the text, so it can only miss, never conflate.

5. GATE_INTERNAL_FILES skip. `scripts/public_release_gate.py` and `scripts/test_public_release_gate.py` containing e-mails, plus a Markdown file (named other, in the same folder as the two internal files).
   Tried: t2. The two internal files give [] in both runs; other.md is reported in both. Cached [] is keyed by rel, so the same bytes under a different name are not answered by it. HOLDS.

6. Same relative path twice / case-insensitive paths / symlinks. os.walk yields each rel once; rel is part of the key; symlinked directories are not followed; broken or directory symlinks fail `is_file()` before both paths. Case variants (`UP.MD`) are distinct strings. HOLDS by reading; only the Unicode/case names in item 4 were run (NOT TESTED on a case-insensitive filesystem).

7. Unreadable file. Code: hash step catches OSError, marks key None, passes the file as a miss; the scan then raises as the old one does. NOT TESTABLE HERE as root-like permission setup was not tried; by reading the result is the same exit 3 (`GATE_ERROR`) in both, no PASS. HOLDS (by reading).

8. Finding whose path is not a scanned file. Within the loop every finding carries `rel` (add_matches uses `path.relative_to(root)`, the same string). So `cacheable` is always true in practice; if it were false the findings are still returned, only the store is skipped. HOLDS.

9. Order of findings. Cached files' findings are appended before the fresh ones, whereas the old loop appends in walk order. `deduplicate` sorts by (path, line, code) with a stable dict, so the only observable difference is the order of findings with equal (path, line, code) from different files (impossible, path differs) or same file (same relative order stored). HOLDS; verdict (BLOCK/PASS) is order independent.

10. Two gates at once on one cache file. Tried: six simultaneous `--cache` runs on 301 files (t6), cold start. All six outputs equal the old output; two runs found no cache (misses=301) and four hit; the file stayed valid (tmp named by pid, `os.replace`). HOLDS. Caveat: two processes with the same pid in different pid namespaces sharing one cache directory would write the same tmp name; the result would be a bad seal, i.e. no cache, not a wrong answer (by reading, not run).

11. Cache written by a different checkout / worktree. The key has no root in it, only script digest, rel and bytes, which is exactly the function's input. Tried: git repo g1 and worktree g1wt share `g1/.git/legend_gate_cache/privacy_v1.json`; hits across the two roots, a changed file in the worktree is a miss, the other root still BLOCKs. HOLDS. Side effect: roots with different trees evict each other (the cache keeps only the current run's files).

12. Flags and environment. `LEGEND_GATE_CACHE=1`, `=true` (ignored: only "1" enables), `--no-cache` with env 1 (off), `LEGEND_GATE_CACHE_FILE` pointing to a directory, to garbage JSON, to a missing file. `--paths`/`--changed-since` with `--cache` (cache is disabled in pre-check, confirmed: no GATE_CACHE line). All give the same finding count as old (1). HOLDS.

13. Script digest. `gate_digest()` reads `__file__` bytes. The gate imports only stdlib, reads no config file, and no os.environ key besides the two cache variables, so every detector input is in those bytes. Not covered by the key: the Python version and its Unicode database / `re` behaviour (`casefold`, `\b`, `isdigit`), and runtime monkeypatching of module constants by a caller that imports the module. NOT TESTABLE HERE (one interpreter). Low risk.

14. `lru_cache` `is_sensitive` is local to each call, pure in its argument. HOLDS. PRIVACY_FILES = [] (all hits) yields no files (`is not None`), confirmed by the warm runs with misses=0.

15. File hash vs scan time-of-check on hits. A hit never re-reads the file, so a file edited right after the hash would be answered with the old bytes' findings; the uncached gate has the same window (scan reads later), so this is equal exposure, not a difference. HOLDS.

## (b) Inputs the loop body reads besides (text, relative path)
- `in_scope(root, path)` -> global `ONLY_PATHS` (None in full gate; the cache is disabled when it is set via main, but `scan_privacy_cached` called as a library with ONLY_PATHS set would hash and cache only the scoped files, consistently).
- `read_text(path)` (the bytes of the file; newline translation, errors="replace").
- `GATE_INTERNAL_FILES` (module constant, in the script bytes).
- `path.relative_to(root)` in `add_matches` (the same rel string).
- Module constants and helpers, all in the script bytes: `PARENT_ORIGIN`, `MATERNAL_ORIGIN`, `PATERNAL_ORIGIN`, `PARENT_OF_ORIGIN_WORDS`, `MATERNAL_WORDS`, `PATERNAL_WORDS`, `PLACEHOLDER_TOKENS`, `STUDY_IDENTIFIER`, `PRIVACY_EXTRA_SUFFIXES`, `EXTRA_WINDOW`, `record_blocks`, `attribution_window`, `semantic_blocks`, `parent_origin_is_explicitly_negated`, `person_context_is_explicitly_negated`.
- Interpreter: `re`, `str.casefold`, `hashlib`, `functools.lru_cache` (call-local, so not persisted across calls).
- Not read: environment (besides the cache variables), clock, randomness, other files, file metadata (mtime, mode, size). The file LIST (walk, git ls-files via `unpublishable_paths`/`tracked_paths`) decides which files are scanned and is computed fresh each run in both gates; the cache never decides membership.

## (c) Gaps in the tests (test_public_release_gate_cache.py)
- Resealed forged entry is tested only as an accepted limit; nothing checks a stored-entry sanity (e.g. the path field equals the key's rel, line numbers plausible) nor any warning on a warm run.
- No test of an edit that reverts between scan and re-hash (item 2). RaceGuard covers A->B only.
- No non-UTF-8 file name, no surrogate in a path (item 3), no NFC/NFD, no newline in a name.
- No concurrency test (several processes, or the same pid tmp name).
- No worktree / shared git-common-dir test, no `rev-parse` failure test (root not in a git repo gives path None, i.e. silently no cache).
- Unreadable file (permission) not tested with the cache.
- No cache written under another Python version.
- The tree-level differential uses the existing 66 fixtures and an optional ten-minute exact-tree run (GATE_CACHE_FULL_TREE=1) that is skipped by default.
- No test that `scan_privacy_cached` leaves PRIVACY_FILES None after an exception in a detector (the code has `finally`, by reading fine).

## (d) Overall answer
The claim "findings and verdict are identical for every input" does not hold in general. For ordinary inputs (files, names, encodings, line endings, flags, env, concurrency, worktrees) the cached run was identical cold and warm in every experiment I ran. Two inputs make the cached run PASS a file the uncached gate BLOCKs: (1) a cache file whose entry was rewritten and resealed (the seal is unkeyed, so it detects damage, not forgery), and (2) a file that is toggled A->B->A during the scan, which stores B's findings under A's key and persists them. Both need a write-capable adversary (cache dir or the working tree during the gate), so against an honest user the cache looks safe, but its stated guarantee for "every input" is too strong; the warm run also gives no sign that its answer was not recomputed. A third difference is not a PASS: a non-UTF-8 file name makes `--cache` exit 3 with no findings where the old gate exits 2 with the finding. Cheap hardening: re-scan at least one-third of hits, or always verify in the landing gate, key the seal with something not stored beside the cache, store text hash computed from the very bytes the scan read (read once, scan from that string) to close item 2, and encode keys with surrogateescape. I could not check: other Python versions, case-insensitive filesystems, permission-denied files, pid-namespace tmp collisions, and the full-tree exact comparison.


---
Dated edit 2026-11-18 (HE, ADV-060): the reviewer's fixture file name in item 5 was a path-shaped string that the reader-journey suite read as a missing repository path; reworded to a description. Nothing else in this report was edited.

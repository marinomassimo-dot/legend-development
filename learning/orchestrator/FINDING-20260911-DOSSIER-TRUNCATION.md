# Finding — 54 tracked dossiers overwritten with the word `touched` during an unattended run

**Recorded by:** `orchestrator`, 2026-09-11 · **Status:** RESTORED, culprit UNATTRIBUTED, guard SHIPPED
· **Severity:** high — scientific artefacts, other actors' readings, and `git` was the only reason
nothing was lost

## What happened

At **2026-09-10 22:26:40–41 UTC**, in a 0.6-second loop, every `PMID*.md` under
`disease-models/wwox/research/fulltext_dossiers/` — **54 files, 10,823 lines** — was overwritten
with the seven bytes `touched`. One manifest, `PMID15070730.json`, had three locator snippets
whitespace-normalised in the same window (`( Fig. 4 )` → `(Fig. 4)`), the signature of
`recapture_snippets.py --write` run against the real root. All changes were **unstaged working-tree
writes**: no commit, no stash, no reflog entry, no merge state.

Three harness sessions were running in the checkout at the time (`HARNESS-ACQREC-001`,
`HARNESS-HANDOFF-001`, `HARNESS-SELFTEST-001`). All three were killed by a rate limit shortly
after and never reported. None had write authority under `disease-models/`.

## Blast radius, measured

| Tree | Result |
|---|---|
| `fulltext_dossiers/` | 54 of 54 modified files contained exactly `touched` |
| `deepdive_manifests/` | 1 file, snippet normalisation only |
| `registries/` (the four current files, the receipt ledger) | **untouched** |
| `files/` (gitignored evidence; git could not have shown it) | **0** files modified in the window; no 7-byte files outside a JSON cache |
| anything else containing `touched` as whole content | none |

## What was excluded, and how

- **git operations**: reflog, stash, `MERGE_HEAD`, `ORIG_HEAD`, `rebase-*` — nothing at 22:26.
- **The literal `touched` in code**: absent from every `.py` in the repository, tracked or in
  flight, and from all three session transcripts except as prose (`not_touched`, `untouched`).
- **The meta-test's tracer** (`self_test_coverage.py`): it *notes* opened paths and writes only
  its own dump into a temp directory.
- **`test_dossier_quote_audit.py`** (in flight): its real-corpus case reads every dossier and
  asserts, byte for byte, that the audit wrote nothing.
- **`test_benchmark_input_surface.py`** (14 writers, names the dossier tree): every write goes to
  `self.surfaces/FIX-001/…` under a temp root.
- **`test_legend_handoff.py`** (in flight): destinations are temp dirs; the session's real-repo
  commands were reads and `classify --root .`.

What remains: `HARNESS-ACQREC-001` and `HARNESS-HANDOFF-001` **both launched the full release
battery within a minute of each other** as their "baseline before change", so two batteries ran
concurrently over one working tree at ~22:26; `HARNESS-SELFTEST-001` ran a loop over ten suites
from `framework/scripts/` in the same window. Some suite, under some of those conditions, wrote
the dossiers. The forensic trail is exhausted at the point where the next step is cheaper as a
guard than as an autopsy.

## What was done

1. **Restored** the 54 dossiers and the manifest from `HEAD` (`git checkout --`). Nothing unique
   was lost: the committed versions are the readings; the in-flight bytes were `touched`.
2. **Guard shipped** in `scripts/run_release_regressions.py`: the runner hashes every tracked file
   under the guarded trees (`disease-models`, `governance`, `roles`, `framework/protocols`,
   `framework/instruction`, `framework/state`, `learning`, `ledger`) before the battery and
   **after each suite**; a suite that changed one is printed as
   `TRACKED_FILES_WRITTEN_BY_SUITE <suite>` with the paths, and **fails the verdict on its own**,
   whatever its exit code. `scripts/test_release_runner_guard.py` pins it.
3. The three sessions were resumed with an instruction to run the battery under an exclusive
   lock, so two batteries never again share a working tree, and to stop and report — not
   restore, not commit — if `git status --short disease-models/` is non-empty before a commit.

## Residual, stated

- **The culprit is unattributed.** The guard attributes on the next run; if the write only
  happens under concurrency, the lock removes the condition and the attribution may never come.
  That is acceptable: the class is closed either way.
- **Concurrent batteries defeat the attribution**, not the detection — a suite may be blamed for a
  peer's write. The lock serialises batteries. **It does not serialise editors**: within the hour
  of shipping, the guard attributed a change to `fulltext_read_receipt.md` to
  `test_repository_surface_determinism.py`, whose fixtures work on a `mkdtemp` copy; the file had
  been edited by a peer session at 06:04:35, inside that suite's slot. A worktree-hash guard in a
  shared checkout separates a suite's write from a concurrent peer edit only when the tree is
  quiet. Refinement built the same morning: the runner records each suite's start/end and prints
  each changed path's mtime against that window — `WRITTEN BEFORE/AFTER THE SUITE` exonerates by
  arithmetic; `INSIDE the window` stays ambiguous and says so (`mtime_verdict`).
- **This is the `real_artifact_case` hazard the dispatch did not name.** The self-test meta-test
  asks every suite to touch a real corpus artefact; the dispatch said *never a false green* and
  did not say *never a write*. `INVISIBLE_COMPLIANCE_GATE`'s sibling: a criterion that rewards
  reading real artefacts must forbid writing them in the same sentence, or it trains exactly this.

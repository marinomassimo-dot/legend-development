---
record_type: SESSION_LEARNING_REVIEW
actor_id: plan
runtime: Codex
date: 2026-09-06
status: LANDED_ON_MAIN
base_head: ed7078272d4bad0bdef7118e4901a6e61d8ebc69
landed_by: the commit that carries this file (Claude Code continuation, same actor, same day)
---

# Agile task closure and session-start scouting

## Implemented

- `framework/scripts/task_close.py`: from a committed, verified task worktree, merge into
  the checkout holding main, verify ancestry, detach at the same commit, then safely delete
  the task branch. Default retains the worktree; `--remove-worktree` removes it only when
  clean, unlocked and free of ignored material. `--dry-run` is read-only. `--branch` permits
  resumption after detachment only at the same branch tip. Conflicts retain task material.
- Guard: ordinary worktree creation remains allowed. Force, abbreviations and bundled
  flags are distinguished from branch-name values; reset through `-B` is refused. Only
  `git switch --detach HEAD` in the assigned checkout is admitted for detachment.
- `runtime_parity.py`: resolve complete actor identifiers before instance suffixes;
  `junior-harness` reaches its contract and governance fingerprint.
- `branch_hygiene.py`: elapsed seconds determine overdue status; 24 hours exactly is
  within the limit, 24 hours plus one second and 25 hours are overdue.
- `scripts/run_release_regressions.py`: discover tracked and untracked test suites,
  respecting Git exclusions; source archives use filesystem discovery. Preserve the
  established ordering and append newly discovered suites. The inventory now has 93 targets.
- `harness_session_start.py`: derive the ISO week's expected scout report and distinguish
  missing, invalid, pending-triage and current reports. Wired into legend-start and Codex
  bootstrap for Plan and Junior. Plan also receives a fresh branch-hygiene count.
- Operational pointers and closure recipe repaired; scientific reading obligations again
  reachable from the shared router. Harness scout classified as non-scientific in the route
  registry. Broken deployment link repaired. Existing lost executable bits restored.
- Regression repairs: document scans prune peer checkouts; local runtime configuration
  has explicit privacy exclusions checked against the index; handoff CLI documents all
  its supported modes; historical guard comparison pins the actual pre-migration blob;
  relative peer-path verification checks topology instead of assuming a sibling directory.

## Validation

The initial full regression run reported failures in ten suites. The run overlapped edits;
its later suites are not an immutable baseline. The eight-suite focused repair run passed.
Final complete regression run: PASS WITH SKIPS, 93 targets, three skips. All three are
topology-dependent checks for a shared checkout different from the assigned worktree;
this session runs in the primary checkout. The runner could not extract one subtest's
reason, but the captured suite output names it explicitly: git run in the shared checkout.
Final LINT PASS; publication gate PASS with zero blocks; receipt chain PASS (128 events);
diff whitespace check PASS. The final standalone closure suite passed all 16 tests.
No publication was performed.

Real-Git tests cover closure, conflicts and retry, detached resumption, dirty/ignored/locked
worktrees, peer ownership, concurrent closure, dry-run, optional removal and guard decisions.
The force/reset test actually reproduces branch reset and duplicate branch checkout in
disposable repositories before asserting the guard rejects those commands.
An additional negative test showed that Git's no-overwrite-ignore option alone did not
protect ignored material during a non-fast-forward merge. The closure command now checks
incoming paths against ignored files/directories before merging, including directory/file
collisions; unrelated ignored caches remain allowed. The reproducer now passes.

## Registration and boundaries

The operator explicitly assigned ACTOR_ID `plan` and authorized workspace implementation.
Read-only parity passes. Write-enabled parity remains FAIL: hook status is TRUST_PENDING,
not DEMONSTRATED. No probe receipt was fabricated and no runtime control was claimed proven.
Claude launch/agent discovery and Claude-side cross-session transport are unavailable here;
no external spend, publication, scientific propagation or peer-branch integration occurred.

The Git staging attempt failed with `Operation not permitted` creating `.git/index.lock`.
The managed sandbox permits workspace files but protects repository metadata. Changes are
therefore present in the workspace, not committed or landed by this session.

## DEFAULTS_TAKEN / DECISIONS_TAKEN

- Keep the task worktree after closure by default; removal is explicit and refuses even
  ignored material. This preserves reusable chats and local data.
- Use session-start reminders, not an unattended scheduler. No background execution is
  claimed when no session is open; an absent weekly report is never treated as completed.
- Repair test assumptions against their real subjects, without skipping failing suites or
  weakening the tested scientific obligations. Existing peer work remains untouched.
- Use the explicitly authorized root workspace. Git metadata isolation prevents creating a
  task branch or committing; changing the sandbox or bypassing it is outside this session.

## STOP_LOG

- Missing identity was resolved by the operator assigning `plan`.
- Runtime filesystem denial: named `git add` cannot create the index lock. No permission
  re-request; finish every permitted edit and validation and report the remaining commit.

## Learning and micro-upgrade

An operation is not safe merely because its verb is normally additive: option values,
force/reset options and the checkout lifecycle must be tested together against real Git.
Automatic suite discovery closes the recurring gap between writing a test and running it.
The weekly scout is now observable at startup instead of depending on a remembered Monday.

Snapshot from the startup report: 89 branches, 59 LAND_OVERDUE, 28 DELETE_READY; these are
observations, not authorization to integrate another actor's scientific work or retire it.
The current week's scout is SCOUT_DUE. Next operational steps are the local commit in a
session with writable Git metadata, then Junior's weekly scout and Plan's triage.

---

## Continuation, 2026-09-06 (Claude Code, ACTOR_ID `plan` re-assigned by the operator)

The Codex session above could not create `.git/index.lock`. This continuation, in the same
root checkout, re-ran every check on the actual bytes instead of reading the report, then
put the diff through a blind hostile review before landing it.

### Re-verified before any repair

LINT PASS; receipt chain OK (128 events, tail anchored); `public_release_gate` PASS with
zero blocks; `run_release_regressions` PASS WITH SKIPS, 93 targets, 3 skips (all in
`test_runtime_parity.py`, all "this surface IS its own shared checkout"). Bootstrap as
`plan` now carries `HARNESS_SCOUT 2026-W36 SCOUT_DUE` and the branch-hygiene line;
`junior-harness` resolves to `roles/junior_harness.md`. A `git update-index --refresh`
probe was refused by the guard as UNKNOWN_EFFECT and was not retried by another route.

### Blind review (fresh Opus instance, diff only, no authorship, no history): BLOCK

Thirteen findings, one BLOCK. Each was REPAIRED or ACCEPTED, never discussed.

| # | Finding | Outcome |
|---|---|---|
| 1 | A conflicting merge left `MERGE_HEAD` in the checkout holding `main`, refusing every other actor's closure until a human resolved it | REPAIRED: `task_close.py` aborts the conflicted merge, `main` is byte-identical to before, the branch and worktree are kept; the test now proves a second actor lands while the conflict is unrepaired, and that the repair is made on the task side |
| 2 | `GitError` reported stderr only; `git merge` writes the conflict to stdout, so the cause was empty | REPAIRED: both streams; the test asserts the conflicted path is named |
| 3 | `DETACH_CURRENT_HEAD` drops the effect, so `post_effect_verify` would report `WRITE_RESULT_INVALID` for `git switch --detach HEAD` | ACCEPTED: `post_effect_verify` is not wired into the shipped hook (`scripts/guard_bash_command.py` imports `pre_tool_use_guard` and `guard_policy.verdict` only); `switch -c` and `branch -d` already belong to the same class. Open as a named debt for the day that module is wired, not silenced |
| 4 | The enrollment invariant became tautological: same `git ls-files` call on both sides | REPAIRED: `NOT_RUN_BY_DESIGN` moved into the runner and honoured by `battery()`; the test asserts battery = priority ∪ discovery − exclusions, that every exclusion and priority entry exists on disk, and carries a positive control on `battery()` |
| 5 | Expected verdicts keyed on free-text labels in two corpora, spelled differently in each | REPAIRED: the verdict is corpus data beside the spelling in both files |
| 6 | Comment claimed the pinned blob is "the pre-migration object"; it is the discriminator-carrying revision, not the last one | REPAIRED: comment states which blob and why, and names the unexamined one |
| 7 | Report prints `age_days` while classifying on seconds | ACCEPTED: the class column is the verdict; the day column is a display |
| 8 | The scout template's `status: PROPOSED → TRIAGED (...)` can never satisfy the parser | REPAIRED: template says `PROPOSED`; the skill states the two literal values and the `\|`-in-cell hazard |
| 9 | Recipe text did not match the flags `task_close.py` runs; `--remove-worktree` also refuses ignored files, undocumented | REPAIRED in `branch_hygiene.landing_recipe`, the script docstring and `--help`. §21e's prose ("a clean closed-chat worktree") is left as is: the sentence is true and the section is reserved |
| 10 | A SIGKILLed run leaves the lock file forever, with no path in the message | REPAIRED for the message (names the path and when it may be removed); the stale-lock age check is not added: a lock that is removed on a heuristic is not a lock |
| 11 | Only the exact argv `git switch --detach HEAD` is admitted; `-d`, `--deta`, `checkout --detach` are refused | ACCEPTED: over-refusal only; the recipe uses the one spelling |
| 12 | Both markdown scans now prune peer checkouts and caches | ACCEPTED: `.claude/worktrees/` is gitignored and nothing tracked lives under `backup/`; the population of tracked documents is unchanged |
| 13 | `deployment/local_instance.md` was already gitignored, so its allowlisting is either redundant or masked a failure | ACCEPTED as redundant-by-design: the assertion is positive (explicitly ignored AND never tracked) and covers both files |

After the repairs: the eight touched suites green; `run_release_regressions` re-run in full
before the commit (result recorded in the commit message and in the manifest note).

### DECISIONS_TAKEN (this continuation)

- ACTOR_ID `plan` assumed from the operator's assignment in the pasted transcript; the work
  is the same task's closure. Reversible: nothing here depends on the identity.
- Committed on `main` directly from the root checkout, as §21e item 1 allows for work that is
  finished when written; the edits already lived in this checkout and no other session was
  writing to it (every open chat has its own worktree). Alternative rejected: moving 28 paths
  to a task branch through stash, which the guard does not admit.
- §21e item 2 was edited (the closure recipe) in the Codex session. A change to §21e is on
  the RESERVED list. The operator saw the file list including `LEGEND_CORE.md` and answered
  "vai avanti, fai tutti i miglioramenti necessari"; that is taken as the operator's
  authorisation for exactly that edit, and it is recorded here so Mirror can find it. If the
  operator disagrees, the revert is one hunk.
- Mirror-style review used before landing although §21e requires none for harness changes:
  it cost one dispatch and found the BLOCK above. Ex-post review remains open to Mirror.

### STOP_LOG (this continuation)

- Class 1 · `git update-index --refresh` refused (UNKNOWN_EFFECT) · 0 waited · not retried
  by another tool; writability was established by the named `git add` at commit time.

### Still open after this landing

- Codex hook `TRUST_PENDING` → `DEMONSTRATED` needs a session probe that records a refusal,
  run from a Codex session; it is a spend under Annex J.4 and is the operator's to open.
- The three `test_runtime_parity.py` skips need a peer worktree whose shared checkout is
  this root. CLOSED: run from a detached scratch worktree at `30fa785` (`git worktree add
  --detach`, admitted by the guard as ordinary creation), the whole
  `ThePeerPlaceholdersAreDerivedAndNotThisMachinesLayout` class passed 7/7 with no skip,
  the three formerly skipped tests included; the scratch worktree was then removed clean.
- 59 LAND_OVERDUE branches: authors land or record abandonment; retiring is reserved.
- `HARNESS-SCOUT-2026-W36.md`: Junior scouts, Plan triages.

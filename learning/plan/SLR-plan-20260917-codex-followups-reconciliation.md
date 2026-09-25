# Reconciling the Codex harness follow-ups — 2026-09-17

Actor: plan (Harness Engineering), Claude Opus 5, on operator instruction to reconcile the
Codex work before implementing anything else, and explicitly not to implement the versioning
conflict a second time.

## 1 · What was actually there

Not what the names suggested. The branch existed, the worktree existed, the task record was
named in the instruction — and none of it was committed.

| Asked about | Found |
|---|---|
| worktree `/tmp/legend-harness-followups` | 19 files **staged in the index**, uncommitted since 2026-09-14 |
| branch `task/plan-harness-followups-20260914` | at `cb181dd`, **0 commits ahead** of main, 76 behind |
| task `HARNESS-FOLLOWUPS-20260914-CODEX` | existed **only in that index**, absent from every commit |

Its own record said `CURRENT_STATE: IN_PROGRESS`, its report said the release comparison and
the final-state gate run were *pending*, and its review requirement claimed no independent
review. So nothing here could be treated as verified, and the instruction not to presume it
was right.

**Preserved before anything else** (`a97be99`): a worktree index is lost by any checkout, and
three days of another runtime's work were one command away from disappearing.

## 2 · Overlap, measured rather than assumed

Main moved 96 files in those 76 commits; this work touches 19; the intersection is **one**,
`governance/annex_a_task_contract.md`. It merged with no conflict: Codex's `A.1a` sits before
`A.1b`, and the `A.1c` block that landed since sits after. **Nothing was superseded**, so the
instruction to preserve superseded work as history without reintroducing it had nothing to
apply to, which is worth saying plainly rather than implying a judgement was made.

## 3 · The verification it left pending

Its own new suite green, and support_linkage, semantic graph, foundation trace, task close,
commit subjects, the commit wrapper and the collision check all green. LINT `WARN`, carrying
the new `POSSIBLE_CONTRAST` advisory that is the intended behaviour. Publication gate PASS,
0 blocks.

**And a consequence it had not carried.** The shared Claim-links parser changed what the
pathograph reads, so the committed derived surfaces drifted and `test_pathograph` went red.
Attributed with a control worktree at plain main, where the same suite is green. Before
regenerating a surface that encodes a different reading of the registry, the parser was checked
against the registry text on all six records where old and new disagree:

| Record | The field says | Old whole-field digit scan | New |
|---|---|---|---|
| `CORPUS P261`, `P268` | "none — adds qualification notes to CLAIM 036 and creates no link" | `036` | none |
| `CORPUS P207` | "CLAIM 028 (source pointer normalized to 207/218/206/214 by BATCH_20260725_001)" | seven, including a batch id | `CLAIM 028` |
| `PAPER 082`, `083` | "deliberately none. CLAIM 002 and CLAIM 004 must NOT be linked" | `002`, `004` | none |
| `PAPER 094` | "none proposed by the reading … referenced by DL-MECH-012" | `012` | none |

The old instrument was inventing links out of a batch identifier, out of a ledger entry's own
name, and — twice — out of the very claims a record explicitly forbids linking. Regenerating
was therefore the correct resolution and reverting would have preserved a defect.

## 4 · The metadata correction

`ledger/tasks/scientist-a/ALDAZ-REPAIR-A-20260913.json` carried `started_at_head: "1104c68"`.
Verified before writing that `git rev-parse --disambiguate` returns exactly one object, then
expanded to the full 40-character name. **Both** occurrences: the guard reads only top-level
`HASH_FIELDS` and would have gone green with the same field left abbreviated three lines below.
Metadata only; no scientific judgement of that task is reopened.

## 5 · Corrections against my own work in this session

- **I reported that Codex's new suite was "not enrolled" in the release battery. That was
  wrong.** I grepped the explicit inventory list and stopped there. The runner also calls
  `discover_tests()`, which walks the tree, so the suite runs: the reconciled battery counted
  120 suites against main's 119, and the extra one is exactly `test_harness_followups.py`. The
  explicit list is a priority order, not the whole battery. A grep is not a measurement of
  behaviour.
- `paper_packet` red in the reconciled tree is **not** this work: it fails identically on a
  control worktree at plain main, because it is local-corpus scoped and `files/fulltext/` is
  gitignored and exists only in the root checkout.

## 6 · Limits

No push. No scientific current file changed. The pathograph is a derived analysis surface and
its regeneration carries no claim, no status and no working-model text. The parser was verified
on the six records where the two readings differ, not on all 442; a full re-audit of declared
links is a separate task and is not claimed here.

## 7 · Final measurement, on main, in the checkout that has the corpus

`df3abfe`, root checkout, `files/fulltext/` present: **120 suites, 2 red.**

| Red | Attribution |
|---|---|
| `scripts/test_link_targets.py` | pre-existing; identical on a control worktree at plain main |
| `framework/scripts/test_batch_queue.py` | red by design, 105 against 69, until populations I1 and I3 are dispositioned |

`paper_packet` is **green here**, which confirms the reading taken in the branch: its redness
there was the absent gitignored corpus, not this work. `pathograph` is green after the
regeneration. `task_record_commit_hashes` is green, closed by the hash expansion.

Net effect against the baseline main carried into this task, three red: **one fewer, none
added.** The suite count rises 119 to 120 because `discover_tests()` picks up the new suite.

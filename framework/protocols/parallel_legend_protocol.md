# PARALLEL LEGEND PROTOCOL

> **Protocol for running parallel deep dives on separate LEGEND instances without corrupting shared state.**
> Version: v3.3.1
> Invoke with `MODE: PARALLEL_BRANCH` to create branches, `MODE: PARALLEL_MERGE` to merge them.

---

## 0. PURPOSE

Enable parallel work on different sets of papers (e.g. two distinct LEGEND chats, or a developer + assistant) without:

- corrupting the current files
- creating incoherent concurrent commits
- silently losing conflicts

> **Central rule:** *parallel deep dive yes, parallel commit no.*
> Branches work in isolation. The merge is single and sequential.

---

## 1. CORE PRINCIPLES

### 1.1 Isolation
Each branch has:
- its own `session_commit_log_branch_X.md`
- its own declared scope (set of papers, time range, domain)
- no write access to the current files
- read access to the same snapshot of the current files

### 1.2 Convergence
All branches converge into:
- a single merge event
- a single post-merge BATCH_COMMIT
- a single update of the current files

### 1.3 Conflict transparency
Conflicts between branches:
- never resolved silently
- never resolved automatically
- always produced as `merge_conflict_report.md`
- always authorized by the operator before proceeding

### 1.4 Append-only logs
- Branch commit candidates never overwrite each other
- Branch logs remain after the merge as an audit trail

---

## 2. WHEN TO USE PARALLEL BRANCHES

### Legitimate use cases

- The operator opens two LEGEND chats to work simultaneously on different sets of papers
- A weekly query produces a batch of N papers too large for a single session
- Deep dives on different domains (e.g. branch A = oncology bridge, branch B = gene therapy)
- Recovery from context-window saturation: the work is split

### Inappropriate use cases

- Branches on the same scope (duplicate work)
- Branches on different working_model_versions (no — they must start from the same snapshot)
- Branches to "try WM changes" (BATCH_COMMIT with rollback exists for that)
- Branches living beyond 7 days (drift too high)

---

## 3. BRANCH LIFECYCLE

```
[Pre-flight check]
       ↓
[Branch creation]  ← MODE: PARALLEL_BRANCH
       ↓
[Branch active work]
       ↓
[Branch lock-in]
       ↓
[Pre-merge check]
       ↓
[Merge]            ← MODE: PARALLEL_MERGE
       ↓
[Post-merge BATCH_COMMIT]
       ↓
[Branch closure]
```

---

### 3.1 Pre-flight check (before branch creation)

| Check | If it fails → |
|---|---|
| `current_state` in manifest = `READY` | ABORT — resolve the block |
| No BATCH_COMMIT in progress | ABORT — complete it first |
| Current snapshot of the current files readable | ABORT — recovery |
| Branch scope declared (set of papers, domain) | ABORT — request scope |
| Branch scope does not overlap with already-active branches | ABORT — resolve the overlap |

---

### 3.2 Branch creation

`MODE: PARALLEL_BRANCH` with parameters:

```yaml
branch_id: BRANCH_X_YYYYMMDD
scope: "paper 221-230" | "RL-GT-001 deep dive" | "biomarker discovery batch"
created_at: YYYY-MM-DD
created_by: [operator / chat_id]
base_snapshot_wm_version: WM_vX.Y_YYYY-MM-DD
expected_duration: [days]
commit_log_file: session_commit_log_branch_X.md
```

Action:
1. Update `state_manifest_current.md` (Parallel branches section): append entry
2. Change `current_state` to `IN_PARALLEL_BRANCH`
3. Create the `session_commit_log_branch_X.md` file (empty, with a header)
4. Append a branch-creation event to `legend_activity_log.md`

> **Scope rule:** once declared, a branch's scope does not change. To add out-of-scope papers, close the branch and create a new one.

---

### 3.3 Branch active work

During the branch's life:

- All branch deep dives produce commit candidates in `session_commit_log_branch_X.md`
- The current files stay read-only
- The branch can run LINT_AUTOMATIC locally to validate its own commit candidates
- The branch **cannot** run BATCH_COMMIT
- The branch **cannot** run an ingest that requires changes to `inbox_current.md` if the file is locked by another branch's merge (see section 7)

> **Working_model_version reference:** each branch commit candidate declares `target_wm_version` relative to `base_snapshot_wm_version`. At merge, this allows detecting whether other branches have already modified the object.

---

### 3.4 Branch lock-in

When the branch is "ready" to merge:

```yaml
branch_status: LOCKED_IN
locked_at: YYYY-MM-DD
final_commit_count: N
```

From this moment:
- no new commit candidates for the branch
- the branch can still answer queries, but does not generate commits
- the merge can begin

---

### 3.5 Pre-merge check

Before starting the merge, verify:

| Check | If it fails → |
|---|---|
| All active branches are in `LOCKED_IN` state | ABORT — wait for the missing lock-ins |
| All `session_commit_log_branch_X.md` readable | ABORT — branch recovery |
| Snapshot of the current files unaltered since branch creation | WARN or ABORT (see section 5) |
| No authorized URGENT_COMMIT executed during the branch's life | ABORT — obsolete branch, recreate |
| LINT_AUTOMATIC run on each branch_commit_log individually, outcome ≤ WARN | ABORT — resolve first |

---

### 3.6 Merge

`MODE: PARALLEL_MERGE` with all branches locked in.

#### Step 1: Global inventory
Build a unified inventory of all commit candidates from all branches.

#### Step 2: Conflict detection
For each object (claim, paper, meta, biomarker, endpoint), check:

- Is it modified by more than one branch?
- Are the changes compatible (non-overlapping) or incompatible (overlapping/contradictory)?

| Conflict type | Handling |
|---|---|
| Same object, identical changes | Automatic merge (deduplication) |
| Same object, complementary changes (e.g. branch A adds a supporting paper, branch B updates status) | Automatic merge with sequencing |
| Same object, overlapping changes (e.g. two branches propose a different status for the same claim) | STOP → produce `merge_conflict_report.md` |
| Same object, contradictory changes (e.g. branch A adds a claim, branch B archives the same claim) | STOP → produce `merge_conflict_report.md` |

#### Step 3: Conflict report (if needed)
If conflicts are detected:
1. Create/populate `merge_conflict_report.md`
2. STOP the merge
3. Notify the operator
4. Wait for explicit resolution decisions

#### Step 4: Merge execution (if no conflicts or conflicts resolved)
1. Combine the commit candidates of all branches into a single consolidated `session_commit_log.md` (preserving branch attribution)
2. Mark the `session_commit_log_branch_X.md` files as `MERGED` (do not delete)
3. Ready for BATCH_COMMIT

---

### 3.7 Post-merge BATCH_COMMIT

Run standard `MODE: BATCH_COMMIT` on the consolidated queue.

> The post-merge BATCH_COMMIT always has `last_batch_commit_type: PARALLEL_MERGE` in the manifest.

---

### 3.8 Branch closure

After the BATCH_COMMIT completes:

1. Update the manifest (Parallel branches section): remove active branches
2. Change `current_state` from `IN_PARALLEL_BRANCH` to `READY`
3. Mark `merge_conflict_report.md` as `RESOLVED_AND_ARCHIVED` if it had been active
4. Append a branch-closure event with summary to `legend_activity_log.md`
5. The `session_commit_log_branch_X.md` files remain as an audit trail (never deleted)

---

## 4. CONFLICT DETECTION CRITERIA

Operational definitions of conflict.

### 4.1 Object-level conflicts

For each identifiable object (PAPER-NNN, CLAIM-NNN, BC-NNN, CME-NNN, RL-XXX-NNN):

- **Modification overlap**: ≥ 2 branches modify the same object
- **Status divergence**: branches propose different statuses for the same claim
- **Evidence divergence**: branches propose different evidence support
- **Wikilink divergence**: branches propose different wikilinks for the same object

### 4.2 Working-Model conflicts

- **WM section overlap**: ≥ 2 branches modify the same WM section
- **Direct-clinical contention**: ≥ 2 branches propose changes to the direct-clinical tier (always flagged as critical)
- **Version target conflict**: branches declare incompatible target_wm_versions

### 4.3 Cross-object conflicts

- **Claim-paper inconsistency**: branch A archives claim X, branch B adds a supporting paper to claim X
- **Meta-claim inconsistency**: branch A updates a meta citing claim X, branch B modifies claim X incompatibly

### 4.4 Auto-resolvable

- **Pure additions** that do not overlap (new PAPER, CLAIM with distinct IDs)
- **Identical modifications** (deduplication)
- **Sequenced modifications** where order is inferable (e.g. paper added, then cited by a claim)

---

## 5. SNAPSHOT DRIFT HANDLING

Critical case: during the branch's life, the current files are modified by an external event (authorized URGENT_COMMIT, recovery, manual intervention).

| Drift type | Severity | Action |
|---|---|---|
| No drift (currents unchanged from base_snapshot) | OK | Proceed with merge |
| Drift on files not touched by the branch | WARN_BUT_PROCEED | Proceed with review |
| Drift on files touched by the branch | BLOCK | Obsolete branch → re-base or recreate |
| Drift on the Working Model with a MAJOR bump | BLOCK | Obsolete branch → mandatory recreation |

**Re-base option** (advanced, requires attention):
- The operator explicitly authorizes it
- The branch is "replayed" against the new snapshot
- Conflicts resolved one by one
- If too much drift, better to discard the branch and recreate

---

## 6. ANTI-PATTERNS

- Never a parallel commit (BATCH_COMMIT in separate branches)
- Never branches on the same scope
- Never self-resolve conflicts (always the operator)
- Never delete `session_commit_log_branch_X.md` post-merge
- Never ignore snapshot drift
- Never change the scope of an active branch
- Never merge without a complete pre-merge check
- Never merge without a pre-merge LINT on each branch
- Never assume "no conflict" without an explicit Step 2

---

## 7. INBOX DURING PARALLEL

When branches are active, `inbox_current.md` can be touched:

- By the main branch (default): may run ingest, classification
- By secondary branches: only staged appends

To avoid race conditions:
- New inbox items during parallel are marked `PARALLEL_PENDING`
- They are processed at merge (together with the commit candidates)
- Never processed independently in multiple branches

---

## 8. PRACTICAL EXAMPLE

```
Day 1:
  - operator creates BRANCH_A (scope: paper 221-225)
  - operator creates BRANCH_B (scope: paper 226-230)
  - manifest.current_state: IN_PARALLEL_BRANCH

Day 2-3:
  - Branch A: 4 deep dives → 4 commit candidates in session_commit_log_branch_A.md
  - Branch B: 5 deep dives → 5 commit candidates in session_commit_log_branch_B.md
  - Current files unchanged

Day 4:
  - Lock-in BRANCH_A
  - Lock-in BRANCH_B
  - MODE: PARALLEL_MERGE
  - Step 2 conflict detection:
    - Branch A proposes a change to CLAIM 028 (status → "in observation")
    - Branch B proposes a change to CLAIM 028 (status → "conflicting evidence")
    - CONFLICT detected
  - Step 3: produce merge_conflict_report.md
  - STOP merge
  - Notify the operator

Day 4 (later):
  - operator decides: status = "conflicting evidence" (Branch B)
  - Re-run Step 4 with the decision applied
  - Merge completed
  - Post-merge BATCH_COMMIT
  - Branch closure
  - manifest.current_state: READY
```

---

## 9. CHANGE LOG (this protocol)

| Date | Event |
|---|---|
| — | Created v3.3.1 — branch lifecycle, conflict detection criteria, snapshot drift handling |

---

## 10. WIKILINKS

- Framework: [[LEGEND_CORE]]
- Conflict report: `merge_conflict_report`
- Batch commit prompt: [[prompt_batch_commit]]
- Lint prompt: [[prompt_lint_integrity_check]]
- State manifest: [[state_manifest_current]]
- Activity log: `legend_activity_log`

---

## 🔴 One actor, one worktree, one task branch — author-owned landing

Everything above governs parallelism **logically**: disjoint scopes, merge before commit. It says
nothing about where the work physically lives, because it was written for a system with one actor
at a time. On **2026-08-09/10** several sessions ran against a single checkout — one HEAD, one
index, one working tree — and it broke four times in two days, three different ways:

- a branch created by one session **silently redirected another session's commit**: the author
  reported work "on `main`" that was on a branch it had never chosen, twice;
- `git checkout -- <path>` **destroyed another actor's uncommitted work** — specifically the
  receipt-ledger tail anchor written moments earlier by `fulltext_receipts.py record`, turning a
  healthy ledger into `BLOCK_SYSTEM`. The reverting actor had read the first twenty lines of the
  diff and concluded the file held only its own change;
- one session **committed another's in-flight files** because they looked finished.

Nothing was lost, and that is luck rather than design. The binding rules:

1. **Every simultaneously open chat works in its own `git worktree`, on a task-scoped branch.**
   Not a convention — the shared checkout is what makes the other three failures possible
   when two sessions share it *at the same time*. The worktree is concurrency hygiene, not a
   rank, and not a place to keep work.
2. **The author lands its own branch on `main` at task end** —
   from its clean task worktree with `python3 framework/scripts/task_close.py` after
   committing and running the required checks. It merges, verifies ancestry, detaches at
   the same commit and safely deletes the branch. `--remove-worktree` also removes the
   clean worktree when its chat is closed. A failed merge preserves the task branch.
   There is no integrating session and no monopoly on merging; nothing stays unmerged at
   rest. Rule and recipe: [`LEGEND_CORE.md` §21e](../instruction/LEGEND_CORE.md#21e-agile-operating-mode)
   (operator decision 2026-09-05, `DEC-20260905-AGILE-HARNESS-MODE`), which replaced the
   earlier "only the integrating session merges to `main`".
3. **Never commit, revert or stage a file another actor is holding** unless that actor has
   declared it finished. If you do it anyway because the work would otherwise be lost, say so in
   the commit message and name the author.
4. **Read the whole diff before reverting.** `git checkout -- <path>` is a destructive write with
   no confirmation, and — unlike blanket staging and heredoc writes — the `PreToolUse` Bash guard
   does not cover it. `git diff <path>` in full, or not at all.
5. **A `BATCH_COMMIT` owns the shared checkout for its duration.** It snapshots, propagates and
   restores on failure; a foreign commit inside that window corrupts the snapshot it would
   restore from.
6. 🔴 **A branch carries the manifest; it does not carry the evidence.** The five rules above are
   about *who may write*. This one is about *what a write can still not reach*. `files/` is
   gitignored for copyright — this repository publishes the derivation and never the derived — so
   a branch, a worktree and a temporary workspace all carry the **manifest**, and none of them
   carries the artifacts the manifest names. Two actors on two worktrees read the same
   `source_artifacts` block off two different filesystems, only one of which has the file in it.

   So **every evidentiary artifact is written into the `files/` of the shared checkout**, and
   **the validation that counts is the one re-run there**. `_safe_repo_path` already refuses to
   resolve an artifact outside its workspace, which is the right refusal: it is what stops a
   reading from being certified against a copy that will not exist tomorrow. Where the manifest is
   authored elsewhere, validate it with the shared checkout as artifact root —
   `deepdive_manifest.py --artifact-workspace` exists for exactly that — and say so.

   `PMID 34831305` was validated `MANIFEST STRICT PASS` in a temporary workspace that then
   evaporated: the manifest survived on its branch, the two figure files did not travel with it,
   and two visual locators spent a day being unverifiable by anyone — **including the actor that
   had verified them.** A green verdict whose inputs are gone is not a verification, it is a
   memory of one. Operational detail: [[fulltext_read_receipt]] § *Evidence locality across
   branches*.

The private working material a `BATCH_COMMIT` consumes — the commit candidates in `staging/` — is
gitignored, so it exists in **exactly one checkout** and does not propagate to worktrees. That is
why the integrator's step is not interchangeable with anyone else's.

---

**End of `parallel_legend_protocol.md`**

> Parallel deep dive yes; parallel commit no.
> Conflicts are surfaced, never silently resolved.

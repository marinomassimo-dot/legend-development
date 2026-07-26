# PROMPT — BATCH COMMIT

> **Operational protocol for propagating commit candidates into the current files.**
> Version: v3.3.1
> Invoke with `MODE: BATCH_COMMIT` or `MODE: URGENT_COMMIT`.

---

## 0. PURPOSE

Deterministically turn the commit candidates accumulated in `session_commit_log.md` into actual updates to the current files, with:

- a Working-Model version bump
- a complete change log
- conflict detection and resolution
- propagation tracking
- manifest and activity-log update

> **BATCH_COMMIT is the only moment when the 4 scientific current files are modified.**
> Outside BATCH_COMMIT, the current files are read-only.

---

## 1. INVOCATION

### 1.1 BATCH_COMMIT (standard)

Triggered by:
- **Temporal**: weekly (fixed day)
- **Threshold**: ≥ 5 accumulated commit candidates
- **Manual**: explicit operator request

The **first trigger to fire** wins.

### 1.2 URGENT_COMMIT (exception)

Triggered by an `URGENT_COMMIT_REQUEST` authorized by the operator, in the 5 admissible categories:
1. Direct safety signal
2. Grave error in the WM
3. Paper decisive for a direct clinical decision
4. Explicit operator request
5. Retraction / invalidation

Operational differences from standard BATCH_COMMIT:
- Accelerated subset (may skip phases 4 and 7 if not relevant)
- Triggers a MAJOR bump of `working_model_version`
- Requires explicit authorization before starting
- May propagate a single isolated commit candidate

---

## 2. PRE-FLIGHT CHECK (MANDATORY)

Before starting the BATCH_COMMIT, verify in order:

| Check | If it fails → |
|---|---|
| `state_manifest_current.md` readable | ABORT — recovery |
| `current_state` in manifest = `READY` | ABORT — resolve the block |
| LINT_AUTOMATIC run recently (< 24h) with outcome ≤ WARN_BUT_PROCEED | Run LINT_AUTOMATIC now |
| No pending `BLOCK_BATCH_COMMIT` or `BLOCK_SYSTEM` | ABORT — resolve first |
| No unmerged active parallel branch | ABORT — complete the merge first |
| `session_commit_log.md` contains at least 1 commit candidate | ABORT (nothing to commit) |
| Backup of the current files available | ABORT — create a backup first |

If all checks pass → set `current_state: IN_BATCH_COMMIT` in the manifest and proceed.

---

## 3. PROTOCOL — 8 PHASES

### Phase 1 — Inventory

Build an inventory of the commit candidates to process.

```
For each commit candidate in session_commit_log.md:
  - ID
  - creation timestamp
  - declared target_wm_version
  - type (paper / claim / meta / research / biomarker / endpoint / framework)
  - impacted files
  - urgent flag (yes/no)
```

Output: `batch_inventory.tmp` (ordered list).

**Ordering rule:** process in the order
1. URGENT (if present and authorized)
2. Paper additions
3. Claim updates
4. Meta updates
5. Research-line updates
6. Biomarker / endpoint updates
7. Working-Model updates (always last)

This order guarantees that upstream dependencies are already propagated.

---

### Phase 2 — Conflict detection

For each commit candidate, check conflicts with:

- other commit candidates in the same batch (e.g. two commits propose different changes to CLAIM 028)
- the current state of the current files (e.g. a claim modified after the candidate was created)
- the current Working-Model state

| Conflict type | Resolution |
|---|---|
| Two CCs modify the same claim compatibly | Automatic merge |
| Two CCs modify the same claim incompatibly | STOP → request an operator decision |
| Obsolete CC (claim modified by another already-propagated CC) | Mark the CC as `SUPERSEDED` |
| CC depending on a claim that does not yet exist | STOP → reorder or request a new CC |

If conflicts are unresolved → ABORT the batch + produce a `conflict_report.md` for the operator.

---

### Phase 3 — Backup and snapshot

Before touching any current file:

```
Create a snapshot in /backup/YYYYMMDD_HHMM/:
  - working_model_current.md
  - claim_registry_current.md
  - paper_registry_current.md
  - literature_tracking_log_current.md
  - meta_*_current.md
  - research_*_current.md
  - biomarker_candidates_current.md
  - clinical_monitoring_endpoints_current.md
  - state_manifest_current.md (pre-batch snapshot)
```

Record the snapshot path in `legend_activity_log.md`.

> **Without a complete snapshot: ABORT.**

---

### Phase 4 — Propagation

For each commit candidate (in the order fixed in Phase 1), apply the changes.

#### 4.1 Paper additions
Append to `paper_registry_current.md`. Update `literature_tracking_log_current.md`.

#### 4.2 Claim updates
Modify `claim_registry_current.md`. Verify:
- valid status
- at least 1 supporting paper
- a change-log entry for every modification

#### 4.3 Meta updates
Modify `meta_*_current.md`. Update `meta_index_current.md` if a new meta.

#### 4.4 Research-line updates
Modify `research_lines_current.md` or `research_candidates_current.md`.

#### 4.5 Biomarker / endpoint updates
Modify `biomarker_candidates_current.md` or `clinical_monitoring_endpoints_current.md`.

**Discipline check** (rerun of the biomarker section of the LINT):
- Tier 3 endpoint in the biomarker file → ABORT
- Biochemical biomarker in the endpoint file → ABORT
- Biomarker promoted to "validated" without a validation paper → ABORT

#### 4.6 Working-Model update (last)
Modify `working_model_current.md`.
- Bump `working_model_version`:
  - MINOR for normal changes
  - MAJOR for baseline reversals / authorized URGENT
- Update the WM change log
- Verify that every cited claim exists and has a compatible status

> **If even a single change fails: ABORT + restore from the Phase 3 snapshot.**

---

### Phase 5 — Post-propagation LINT

Run `LINT_AUTOMATIC` on the post-propagation state.

| Outcome | Action |
|---|---|
| `PASS` or `INFO` | Proceed to Phase 6 |
| `WARN_BUT_PROCEED` | Proceed to Phase 6, record the warning |
| `BLOCK_BATCH_COMMIT` | ABORT + restore from snapshot |
| `BLOCK_SYSTEM` | ABORT + restore + escalate to the operator |

Logic: the pre-flight LINT verifies that you may start; the post-propagation LINT verifies that the result is coherent.

---

### Phase 6 — Manifest update

Update `state_manifest_current.md`:

```yaml
working_model_version: WM_vX.Y_YYYY-MM-DD  # new
last_wm_update: YYYY-MM-DD
last_wm_batch_commit_id: BATCH_YYYYMMDD_NNN
last_batch_commit_id: BATCH_YYYYMMDD_NNN
last_batch_commit_date: YYYY-MM-DD
last_batch_commit_type: WEEKLY | THRESHOLD | MANUAL | URGENT
commit_candidates_propagated: N
target_wm_version: [achieved version]
trigger: [trigger type]
current_state: READY  # restore from IN_BATCH_COMMIT
```

Also update the 3.x sections of the manifest with the timestamps of the modified files.

If an URGENT_COMMIT was authorized: remove the entry from `pending_urgent_requests` and mark it `AUTHORIZED_AND_EXECUTED`.

---

### Phase 7 — Commit-candidate cleanup

In `session_commit_log.md`:
- Mark the processed commit candidates as `PROPAGATED` with a reference to `BATCH_YYYYMMDD_NNN`
- Mark any `SUPERSEDED` with a rationale
- Do not remove from the queue — the queue is append-only

> **Never delete commit candidates from the queue.** Only mark them.

### 7.1 Re-point the receipts of everything this batch propagated

A deep-dive receipt names the artifacts the reading produced — which, before the commit, are
**staging drafts**. After propagation those drafts are no longer where the reading lives: it
lives in the canonical registries. Leave the receipt as it is and it keeps pointing at a
working file that the public edition never ships, so a fresh clone opens with
`UNRESOLVED_OUTPUT_FILE` and the reading history published to the world points at nothing.

For every receipt whose outputs name a path under a private root (`staging/`, `files/`,
`backup/`, `tmp/`, `overlay/`, `_qa/`):

```bash
# append a correction event; never edit the ledger by hand
python3 framework/scripts/fulltext_receipts.py record --receipt <correction.json>
```

The correction receipt carries `reread_reason: receipt_correction`, `prior_receipt` set to the
event it retires, and outputs re-pointed to the canonical landing (`paper_registry_current.md#PAPER NNN`,
`literature_tracking_log_current.md#LIT-NNNN`, plus the ledger/queue entries already durable).
Coverage, depth, analysis time, source locator and fingerprint are **carried over unchanged** —
this corrects where the output went, never what was read. History is not rewritten: the original
event stays visible in the chain and is simply superseded.

Enforced by `test_active_receipts_never_name_an_output_that_cannot_ship` in
`scripts/test_fulltext_trace_contract.py`.

Final batch output:
- N commit candidates `PROPAGATED`
- M commit candidates `SUPERSEDED`
- K commit candidates `DEFERRED` (left in the queue for the next batch)

---

### Phase 8 — Activity log + change report

#### 8.1 Append to `legend_activity_log.md`

```markdown
## YYYY-MM-DD HH:MM — BATCH_COMMIT BATCH_YYYYMMDD_NNN

- type: WEEKLY | THRESHOLD | MANUAL | URGENT
- trigger: [...]
- pre-flight LINT: [outcome]
- commit candidates processed: N
- propagated: N
- superseded: M
- deferred: K
- working_model_version: [old] → [new]
- conflicts encountered: N (resolved: N, escalated: 0)
- post-propagation LINT: [outcome]
- snapshot path: /backup/YYYYMMDD_HHMM/
- duration: HH:MM
- outcome: SUCCESS | ABORTED | PARTIAL_RECOVERY
```

#### 8.2 Produce a change report

Structured output for the operator:

```markdown
# BATCH COMMIT REPORT — BATCH_YYYYMMDD_NNN

## Summary
- Type: [...]
- WM version: WM_vX.Y → WM_vX.(Y+1)
- Commit candidates propagated: N

## Files modified
- working_model_current.md (MAJOR/MINOR bump)
- claim_registry_current.md (N claims modified)
- paper_registry_current.md (N papers added)
- [...]

## Files unchanged
- [...]

## Key changes (clinically relevant)
[Narrative list of the operationally relevant changes]

## Conflicts resolved
[If any]

## Deferred to next batch
[If any]

## Recommended next actions
- [e.g. "review the research tier in light of new CLAIM 029"]
```

---

## 4. URGENT_COMMIT — VARIATIONS

When `MODE: URGENT_COMMIT`, the protocol is abbreviated but stricter on the critical checks.

### Phase modifications

| Phase | Standard | Urgent |
|---|---|---|
| 1 (Inventory) | All CCs | Only URGENT-marked CCs |
| 2 (Conflict) | Among all CCs | Between URGENT CCs and current state |
| 3 (Backup) | Mandatory | Mandatory (no skip) |
| 4 (Propagation) | All types | Only impacted files |
| 5 (Post-LINT) | Full LINT_AUTOMATIC | Full LINT_AUTOMATIC (no skip) |
| 6 (Manifest) | MINOR bump default | MAJOR bump default |
| 7 (Cleanup) | Standard | Standard |
| 8 (Log) | Standard report | Report with a visible URGENT flag |

### Authorization gate

> Before Phase 1, LEGEND must have explicit operator confirmation:
> *"I authorize URGENT_COMMIT [URGENT_ID] for category [N]"*

Without clear textual authorization → ABORT.

---

## 5. ABORT PROTOCOL

If at any phase the batch must be aborted:

1. **Immediate stop** of execution
2. **Restore from the Phase 3 snapshot** (all files to pre-batch values)
3. **Update the manifest**: `current_state: BLOCKED_BY_LINT` or `BLOCKED_SYSTEM` depending on the reason
4. **Append to the activity log**:
   ```
   YYYY-MM-DD HH:MM — BATCH_COMMIT BATCH_YYYYMMDD_NNN ABORTED
   - phase reached: N
   - reason: [...]
   - snapshot restored from: [path]
   - commit candidates left in queue: K
   ```
5. **Notify the operator** with an explicit ABORT report
6. The commit candidates **stay in the queue** unmodified for the next batch

> **Never a partial commit. All or nothing.**

---

## 6. ANTI-PATTERNS

What BATCH_COMMIT must never do:

- Never propagate a CC without a target_wm_version
- Never bump the version without a change log
- Never skip Phase 3 (backup) to "save time"
- Never skip Phase 5 (post-LINT) because "the pre-flight LINT passed"
- Never self-authorize an URGENT_COMMIT
- Never delete CCs from the queue (only mark them)
- Never a partial commit on error
- Never propagate a CC with an unresolved conflict
- Never promote a biomarker to "validated" without a validation paper
- Never put a Tier 3 endpoint in biomarker_candidates

---

## 7. WORKING_MODEL_VERSION RULES

### MINOR bump
- Addition of a new claim (in observation)
- Status update of a non-baseline claim
- Block update without a policy change
- Addition of a supporting paper to an existing claim
- Addition of a candidate biomarker / endpoint

### MAJOR bump
- Reversal of a baseline claim
- Policy change in the direct-clinical tier
- Authorized URGENT_COMMIT (category 1, 2, 3, 5)
- Retraction of a baseline paper
- Structural change to the Working Model

### Format
`WM_vMAJOR.MINOR_YYYY-MM-DD`

Example:
- `WM_v0.07_...` → `WM_v0.08_...` (MINOR)
- `WM_v0.08_...` → `WM_v1.00_...` (MAJOR for a reversal)

---

## 8. CHANGE LOG (this prompt)

| Date | Event |
|---|---|
| — | Created v3.3.1 — 8-phase protocol, URGENT variation, version-bump rules |

---

## 9. WIKILINKS

- Framework: [[LEGEND_CORE]]
- Lint prompt: [[prompt_lint_integrity_check]]
- State manifest: [[state_manifest_current]]
- Activity log: `legend_activity_log`
- Session commit log: `session_commit_log`
- Parallel protocol: [[parallel_legend_protocol]]

---

**End of `prompt_batch_commit.md`**

> BATCH_COMMIT is the write point. Everything else is preparation.
> All or nothing. Never a partial commit.

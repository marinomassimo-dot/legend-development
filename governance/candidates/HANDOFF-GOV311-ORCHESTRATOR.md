---
artifact: HANDOFF — CAND-20260816-GOV311 → the session that executes the canonical commit
candidate_id: CAND-20260816-GOV311
candidate_content_hash: c39ecae89677363802c8c7d24b704da185fc568fed360b08ad01adb39730c239
base_head: 749a9a9b8f29c855f803a43b979c591532557561
source_branch: evidence-index
domain: CONTROL PLANE — outside the candidate content domain (P5.1); writing it does not alter the hash
prepared_by: plan
prepared_on: 2026-08-16
authority: none — this document records verified state and routes to the governing procedure.
  It issues no instruction and confers no permission.
---

# Handoff — what is ready, what must still be checked, and by whom

You are reading this because a candidate has passed review and approval and is waiting for the
one step Plan may not perform. **This file confers nothing.** It records what has been verified,
names where each rule lives, and lists what remains — so that the executing session does not have
to reconstruct a day's work from a chat log.

## What this candidate is

The single introduction of **Governance v3.1.1** — body, ten annexes, role contracts,
`BOOTSTRAP.md`, deployment profile, the Plan-defined parameters, two executable scripts, the
prior-art design record, and the migration of the root `CLAUDE.md` into a router with every rule
it carried relocated to a canonical home.

`CHANGE_CLASS: MAJOR`, by definition rather than by judgement: it is governance, authority and
gate changes at once.

## State, verified

| | |
|---|---|
| `CANDIDATE_CONTENT_HASH` | `c39ecae89677363802c8c7d24b704da185fc568fed360b08ad01adb39730c239` |
| `BASE_HEAD` | `749a9a9b8f29c855f803a43b979c591532557561` — equals `main`; branch **0 behind** |
| Mirror | `PASS_WITH_NOTES` — `REV-GOV311-MIRROR-002`, commit `2d7c4ab8`, bound to this hash |
| Human approval | `APPROVED` — `RES-20260816-GOV311-001`, bound to this hash + base |
| Deviations | PID-09 and PID-10 **ACCEPTED** by the operator |
| LINT · publication gate | `PASS` · `PASS`, `BLOCKS: 0` |

Reproduce the hash yourself before trusting any of the above — one command, from the repository
root:

```bash
python3 governance/scripts/candidate_content_hash.py \
  --base 749a9a9b8f29c855f803a43b979c591532557561 \
  --tip  9720a0cd1dddfe457f8e4eec1ebe47bd627512cc --show-domain
```

## Before executing: what is NOT inherited from this branch

GATE 0 is about the **root checkout**, and nothing verified on `evidence-index` transfers to it.
Re-verify there, at execution time:

- **root clean** — a dirty root is `NO BATCH`, and this is the condition most likely to have
  changed since;
- **`BASE_HEAD` still equals the root's `main`** — if `main` moved, the candidate needs
  re-alignment and a new hash, and the approval bound to the old hash no longer applies (gate 5);
- **`ONE_WRITER`** — no other session holding the root;
- **`GOVERNANCE_VERSION` correct**.

**The lease condition is `NOT_YET_APPLICABLE` for this one commit**, by operator ruling
`RES-20260816-GOV311-002` (ACCEPT INTERPRETATION 1). It binds again from the next canonical batch.
No frozen text was amended and the ruling does not generalise.

## The procedure is not restated here

`framework/protocols/prompt_batch_commit.md` holds the 8-phase procedure; Annex D.4 holds the
transaction shape — snapshot, apply the exact candidate, post-commit validate, and on failure
restore and record rather than repair. Manual repair in the root is forbidden. Follow those, not
a summary of them.

Two things worth naming because they are easy to get wrong under time pressure: **snapshot before
applying**, and **apply the exact candidate** — the tree at `9720a0cd…`, whose identity is the
hash above. A commit whose content hash does not match is precisely what gate 5 exists to catch.

## What becomes due immediately after the commit

Not instructions — a list so nothing is lost in the transition.

| Item | Why it is next |
|---|---|
| Bootstrap §47 from step 1 | `BOOTSTRAP.md` guides it; the worktree `lettore-c` does not exist yet |
| `LEARNING_INDEX` | eleven session-learning records (MAT-001…011) exist and none is filed; the schema is Annex E.2 |
| MAT-012 | the log entry for the RC-6…RC-10 correction was deliberately deferred: `governance/design_records/` is inside the content domain, so writing it would have changed the approved hash |
| Event ledger writer | design chosen (P7); must reuse the existing append-only receipt-ledger machinery, not a second mechanism |
| `HUMAN_APPROVAL_QUEUE` general implementation | the minimal conformant instance exists; `REVISION_REQUESTED` handling, `APPROVED_WITH_MODIFICATION` and the DAILY_BRIEF view do not |
| `OPERATOR_DAILY_BRIEF` | due at the first worked day with laboratory activity to report |
| Runtime inventory / Agent Card | populated by registration and L2, not before |

## Carried unresolved

`ESC-3` — the `MIRROR_RETROSPECTIVE` cadence `N` remains unset by explicit operator decision. Two
actors declined it citing G.2. It blocks nothing: retrospectives cannot run before there are
batches to retrospect.

The remaining `UNRESOLVED` items are in the manifest §5, each with its authority and whether it
blocks. None blocks this commit.

## What Plan did not do, and will not

Plan does not execute `CANONICAL_BATCH_COMMIT` (H.1 — Orchestrator alone), does not touch `main`
or the root checkout, does not acquire a lease, does not start the bootstrap, and does not message
Mirror directly. The approval removes a precondition; it transfers no authority.

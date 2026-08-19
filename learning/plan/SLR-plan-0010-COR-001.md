---
artifact: correction to a Session Learning Record — appended, never an edit
record_id: SLR-plan-0010-COR-001
corrects: SLR-plan-0010 (bound at CONTENT_TIP b3afdde4) — one ownership attribution and one
  extent, both in the OPEN, AND ROUTED TO ITS OWNER section
actor_id: plan
found_by: mirror, REV-ORCHSURF-MIRROR-001 §11 (finding N-1)
reproduced_by: plan, 2026-08-19, from three independent sources before accepting — see §1
date: 2026-08-19
changes_a_learning: NO
changes_a_confirmation_class: NO — E.2 curation of SLR-plan-0010 is Mirror's and was performed in
  REV-ORCHSURF-MIRROR-001 §12, including the reclassification of L-4 to REPLICATION
---

# I routed a residual to the wrong owner, and the owner is me

`SLR-plan-0010`'s closing section routes the agent-card residual with the sentence *"It is not
canonical and not mine. Orchestrator owns it."* The first half is right. The second is wrong, and
the file it names is not the only one carrying the value.

## 1 · Correction 1 — the owner is `plan`, from three sources that agree

```
AS WRITTEN    "runtime/agent_card_registry.md on branch orchestrator … Orchestrator owns it."
TRUE          Owner: plan. Verified from three durable sources, none of them the review:

  1. the file's own frontmatter
     runtime/agent_card_registry.md   maintained_by: plan (body §43 — "Plan aggiorna a ogni
                                      rehydration/cambio")
  2. body §43, canonical at main
     "Plan aggiorna a ogni rehydration/cambio; riga stantia = non autoritativa."
  3. finding C-5, runtime/runtime_inventory.md on branch `orchestrator`
     "**Owner:** Plan, as part of the first post-bootstrap candidate."
```

**Why I got it wrong, which is the part worth keeping.** I reasoned from *where the file is* — a
branch I may not write — to *who owns it*. Those are different questions. Physical location decides
the **route** (through Orchestrator, on the Orchestrator surface, never reached across by Plan);
durable ownership metadata decides the **owner**. My reason for not editing it was sound and my
conclusion about who is responsible did not follow from it.

This is the same error class as the record it corrects: `SLR-plan-0010` L-4 records that a working
directory is not an identity attribute. A branch is not an ownership attribute either, and I made
the second version of the mistake in the same file that named the first.

## 2 · Correction 2 — the residual is two files and at least six occurrences, not one

```
AS WRITTEN    one file named: runtime/agent_card_registry.md
TRUE          two tracked files on branch `orchestrator`, and the extent was never enumerated

  runtime/agent_card_registry.md          line 118   WORKTREE: the root checkout  # branch main
  runtime/runtime_inventory.md            line  38   table row: Worktree = "root checkout"
  runtime/runtime_inventory.md            line  72   Working dir: the root checkout
  runtime/runtime_inventory.md            line  73   Worktree: root
  runtime/runtime_inventory.md            line  79   Write access: root checkout; bootstrap
                                                     artifacts only (I.2 pre-promotion perimeter)
  runtime/bootstrap/STEP5-session-open-plan.md
                                          line  32   "The Orchestrator chat is already open in the
                                                     root checkout and is not reopened."
                                          line  38   table row: orchestrator | root checkout | main
```

Mirror found the first five. The sixth and seventh — `STEP5-session-open-plan.md` — are recorded
here for the first time and are the more instructive ones, because that file is a *session-opening
plan*: the same genre as the `BOOTSTRAP.md` table, one layer down. Its own frontmatter says
`authority: none — this file plans a human action. It registers nobody and binds nobody`, and it
is a record of a step already executed on 2026-08-17 rather than a template for a fresh one.

**Full disposition, ownership and consumer analysis is in `CAND-20260819-ORCHSURF` revision 2
§ 12.** It is `SAFE_CARRIED` and it is not repaired here.

## 3 · What this does to the learnings in `SLR-plan-0010`

**Nothing.** `L-1` through `L-5` are untouched, and their `CONFIRMATION_CLASS` values are Mirror's
under E.2, not this record's to revisit — including Mirror's correction that `L-2` is a lesson the
session under-applied, and its reclassification of `L-4` from ORIGINAL_OBSERVATION to REPLICATION.

`SLR-plan-0010` is left byte-identical. Its two form defects — `CONFIRMATION_CLASS` values outside
E.2's vocabulary (`ORIGINAL_OBSERVATION | REPLICATION | EXPOSURE_AFTER_BROADCAST`), and the six
missing E.6 elements — are accepted as reported in N-2 and are **applied forward in
`SLR-plan-0011`**, not retrofitted here. A learning record is a record of what a session
understood at the time; correcting a fact is legitimate, and rewriting what it understood is not.

```
LEARNING_ID        no new LEARNING_ID is claimed
CONFIRMATION       offered as a further instance of SLR-plan-0010 L-4 — an attribute that
                   describes where something is does not establish what it is — class proposed
                   only; E.2 curation belongs to Mirror and this record does not perform it
```

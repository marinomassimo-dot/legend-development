---
artifact: HANDOFF — role contract repair preparation
handoff_id: HANDOFF-20260822-ROLE-CONTRACT-REPAIR
task_id: PLAN_ROLE_CONTRACT_REPAIR_PREPARATION_v2
iteration: 2/3
author: plan
authored_on: 2026-08-22
dispatcher: operator
governance_version: 3.1.1

STATUS: PREPARATION_ONLY
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED

accompanies: governance/candidates/PREP-20260822-ROLE-CONTRACT-REPAIR.md
recipient: NOT ASSIGNED — no actor is named as recipient and none is elected here. Routing is
  unresolved repository-wide (APR-20260819-XPORT-001 SESSION_ROUTING_DEBT), and this document
  does not invent a destination.
naming_note: learning/plan/ contains SLR-plan-NNNN records by convention. This is a handoff, not
  a Session Learning Record, and is named accordingly rather than taking an SLR number it has not
  earned. The location is the one the dispatch specifies.
---

# HANDOFF — ROLE CONTRACT REPAIR PREPARATION

> **Nothing is delivered for execution.** This handoff transmits a preparation document and the
> open questions it could not answer. It requests no approval and confers no authority.

---

## 1 · WHAT WAS DONE

`PREP-20260822-ROLE-CONTRACT-REPAIR.md` was prepared under `governance/candidates/`, responding to
the findings of `REV-ROLES-MIRROR-001` against the four role contracts, and reading
`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` as the operator determination of their activation
state.

**No file under `roles/`, `governance/decisions/`, `framework/` or `ledger/` was modified.** No
`status:` line was changed. No `DEC` and no `HUMAN_APPROVAL` record was created.

---

## 2 · THE THREE THINGS A READER SHOULD KNOW FIRST

### 🔴 2.1 · Plan acted without contract authority, and says so

`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` (`OPTION B — ACTIVATION_NOT_CONFIRMED`) holds all
four contracts **non-binding**. `roles/plan.md` is therefore not a source of authority for this
session. Every structural act in the preparation traces to a named instrument instead — Annex D.1
for the `WORK_COMMIT`, P5.1 for the control-plane domain, Annex C.2 for the review format. The
dispatch grants nothing and was not treated as granting anything.

### 🔴 2.2 · Neither input object was on this checkout, and both exist

| Object | Present on | Refs of 45 |
|---|---|---|
| `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` | `refs/heads/main` | **1** |
| `REV-ROLES-MIRROR-001.md` | `refs/heads/mirror` | **1** |

Both were located by sweeping every ref before any statement was made about them. `NOT_FOUND` here
was never converted into `NOT_EXIST`.

### 🔴 2.3 · This checkout carries the repair Mirror said was elsewhere

`roles/orchestrator.md` at my HEAD is blob `24663eec77` — the ORCHSURF revision-4 text. Mirror
reviewed `2bbb214143` and recorded *"That revision is on neither ref under review."* **I am standing
on one of the two refs that carry it.** Every statement about that contract in the preparation names
which blob it concerns.

---

## 3 · FINDINGS CONSUMED — and what came back changed

Four findings were re-measured rather than accepted. Three survived; one did not survive in the form
transmitted.

### MAJOR-1 — survived, and is now stronger

Mirror's C.2 falsifier (*"a full hand-composition would settle it"*) was **executed**. A separate
implementation of P2.2, importing nothing from the repository script, produced
`0d6987bd79e5…faec1429` for `plan` — **identical to the script's output**, input for input across
all 13. The row in `roles/plan.md`:73 declaring fingerprint composition *"blocked: the composition
is prose, not a script"* denies a capability the repository demonstrably has.

### MAJOR-2 — survived, with corroboration three days older than the review

`APR-20260819-XPORT-001` (operator-approved, 2026-08-19, on `refs/heads/orchestrator`) already
carried this defect by name as `ORCHESTRATOR_WORKTREE_CONTRADICTION` … `NOT repaired here`. Two
instruments reached it independently.

### MAJOR-3 — survived, but its character changed

All three conditions in `scientist_reading_modes.md`'s status line are **independently evidenced**:
canonical execution (`4454fea`, ancestor of `main`), Mirror review (`REV-SCIAB-MIRROR-006` ACCEPT,
on `mirror` only), and `HUMAN_APPROVAL` (`APR-20260819-SCIAB-001`, on `orchestrator` only) — in the
required order, approval six minutes before execution. **The review reached the execution but not
the approval**, and its own § 2 names the mechanism: the branch-authority trap.

**Mirror's falsifier still is not discharged**: no object anywhere records the status line as
superseded, and the protocol is one blob on all 8 refs carrying it. The finding is a **staleness
defect with all three conditions evidenced**, not an unresolvable contradiction.

### 🔴 MINOR-3 — did NOT survive in the form transmitted

Transmitted: all three Scientist worktrees sit on refs carrying the superseded blob.

Measured: `lettore` and `lettore-b` carry **no `roles/` and no `governance/` at all** — neither has
`a8cd125` (the materialization commit) as an ancestor. Only `lettore-c` matches the finding.

The true state is worse than the reported one: two of three Scientist worktrees offer **no contract
and no constitution to rehydrate from**, which the check that finds a stale blob cannot detect. This
is a ref-topology defect, not a contract defect, and **no contract repair addresses it**.

Restating a finding is Mirror's act under C.2. The evidence is transmitted; the verdict is not
rewritten here.

---

## 4 · UNRESOLVED DECISIONS — none of them taken

| # | Question | Why Plan did not answer it |
|---|---|---|
| U-1 | Annex H.1 row 40 assigns lifecycle-learning authority to **nobody** — the only such row in the table (measured, 17 rows). | Filling it is a governance change; H.1 and body §4/§10 assign it to the operator. The dispatch independently forbids assigning unresolved authority. |
| U-2 | MINOR-1: does Plan or Mirror maintain the `ACTIVE_LESSONS` subsets? | Repairing either contract first **silently fills U-1** by making one document's verb the survivor. The ordering is the decision, and it is not Plan's. |
| U-3 | MAJOR-1: blocker phrase only, or blocker + `UNVERIFIED → VERIFIED`? | Different changes, different review levels. Capability promotion is an Annex I.4 L2 act; a self-declared `VERIFIED` is what `CONFIGURED != PROVEN` forbids. |
| U-4 | MAJOR-2: adopt `CAND-20260819-ORCHSURF` rev 4 whole, or a narrow edit? | The candidate carries more than MAJOR-2's three clauses. **And it is unapproved** — zero ORCHSURF approvals across all 19 refs carrying the queue. |
| U-5 | MAJOR-2: does `DEC-20260820-ORCH-SESSION-HOME` settle the repair *direction* while the *text* stays unapproved? | The candidate's own `revision_4` field asserts it does. **Plan does not adjudicate its own candidate's claim about an operator decision.** |
| U-6 | MAJOR-3: does a satisfied-but-unrecorded condition bind the protocol? | This is `DEC-20260822`'s question, answered `NOT_CONFIRMED` for `roles/` — on reasoning that **cites this protocol** as the repository's gloss on the grammar. Extending it by analogy is a governance interpretation, prohibited here. |
| U-7 | MAJOR-3: which document is defective — the contract for over-claiming, or the protocol for a stale line? | The repair differs completely. **Plan authored both**, so its reading carries no independence under C.2. |
| U-8 | Are `lettore` / `lettore-b` meant to carry governance at all? | Requires operator or runtime authority. Intent is not inferred from topology. |
| U-9 | May a repair be prepared against a contract `DEC-20260822` holds non-binding — does repair precede or follow the activation act its consequence 3 requires? | A sequencing question for the operator. Preparation proceeded because the dispatch ordered it; the question is recorded rather than resolved. |

**`MIRROR_RETROSPECTIVE` cadence `N` (ESC-3) was not resolved**, as the dispatch requires.

---

## 5 · AFFECTED OBJECTS

**Read, not modified:**

```
governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md   @ refs/heads/main    2bb2700
reviews/mirror/REV-ROLES-MIRROR-001.md                                @ refs/heads/mirror  1350477
roles/plan.md · roles/orchestrator.md · roles/scientist.md · roles/mirror.md
framework/protocols/scientist_reading_modes.md
governance/annex_e_learning_lifecycle.md § E.5 · governance/annex_h_authority_matrix.md § H.1
governance/plan_defined_parameters.md § P2 · governance/candidates/CAND-20260819-ORCHSURF.md
ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl   (this ref, and @ refs/heads/orchestrator)
```

**Created — the only two paths written:**

```
governance/candidates/PREP-20260822-ROLE-CONTRACT-REPAIR.md
learning/plan/HANDOFF-20260822-ROLE-CONTRACT-REPAIR.md
```

Both are under declared `CONTROL_PLANE_ROOT`s or outside the canonical scientific state; neither
moves any candidate content hash.

---

## 6 · REQUIRED FUTURE REVIEW

1. **`AUTHOR_RESPONSE` to `REV-ROLES-MIRROR-001` — required and outstanding.** Neither the
   preparation nor this handoff is that response (Annex C.2: silence is not acceptance;
   `DEC-20260822` § IMMEDIATE_CONSEQUENCES 5 records the same).
2. **Independent review of `roles/mirror.md`** — **suppliable by neither Mirror nor Plan**: Mirror
   is barred by G.2/H.1 from self-review, and Plan authored all four contracts, so its review would
   be an author review. 🔴 The G.2 route currently has **no available executor**: 0 `ACTIVE` leases
   by derivation → no `ACTIVE_ORCHESTRATOR` to choose a reviewer, and 0 `VERIFIED` capabilities in
   any actor of any role.
3. **C.2 review at floor R4 (`MIRROR_REQUIRED`, Annex G.1)** for any repair candidate that follows.
4. **Re-measurement of MINOR-3** before anything is built on it.
5. **Operator determination on U-1 and U-6** — the two questions this task is barred from answering.

---

## 7 · WHAT THIS HANDOFF DOES NOT DO

Does not: name or elect a recipient · request approval · schedule a repair · activate or ratify
anything · change any `status:` line · assign a reviewer (Orchestrator's act under G.2) · resolve
any finding · resolve cadence `N` · advance `main` · claim that routing is solved.

`SESSION_ROUTING_DEBT` remains real and out of scope, exactly as `APR-20260819-XPORT-001` records
it. No recipient was invented to make this handoff look delivered.

---

**Prepared by:** `plan`, worktree `evidence-index`, branch `plan-orchsurf-r4-transcription`,
2026-08-22 — under the operator's dispatch, **not** under the authority of `roles/plan.md`.

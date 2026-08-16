---
artifact: DECLARED DEVIATION RECORD — for HUMAN_APPROVAL
candidate_id: CAND-20260816-GOV311
candidate_content_hash: c39ecae89677363802c8c7d24b704da185fc568fed360b08ad01adb39730c239
base_head: 749a9a9b8f29c855f803a43b979c591532557561
governance_version: 3.1.1 (FROZEN)
mirror_review: PASS_WITH_NOTES — REV-GOV311-MIRROR-002 (2d7c4ab8), ESC-2 raised
domain: CONTROL PLANE — this file lives under governance/candidates/ and is outside the
  candidate content domain (P5.1). Writing it does not alter the hash above.
prepared_by: plan
prepared_on: 2026-08-16
state: AWAITING_HUMAN_APPROVAL — no approval is exercised in this document
---

# Declared deviations from Governance v3.1.1 FROZEN — PID-09 and PID-10

Two deviations from the frozen text were declared by Plan when made, and Mirror recommends
accepting both while explicitly refusing to ratify them: a deviation from frozen text is
governance, and Annex H.1 assigns governance to the operator. Ratifying them through a reviewer's
PASS would be the reviewer taking an authority it does not hold.

**This is not an implementation detail presented as one.** Each deviation is stated as a
departure from a specific clause, with the reason, the residual risk, the mitigation and a
recommendation the operator is free to reject.

Rejecting either deviation changes files inside the content domain and therefore produces a new
`CANDIDATE_CONTENT_HASH` and a new full review. Accepting both leaves the candidate as reviewed.

---

## PID-09 — Shared Scientist Role Contract replacing duplicated per-actor role files

### FROZEN_REQUIREMENT

Annex I.2 step 7: *"ogni attore legge `/roles/<suo>.md`"* — each actor reads its own role file.
Read literally for three scientists, this yields three files:

```
roles/
├── scientist-A.md
├── scientist-B.md
└── scientist-C.md
```

### MATERIALIZED_IMPLEMENTATION

```
roles/
└── scientist.md          ← one ROLE CONTRACT, shared by scientist-a / -b / -c
```

The file declares in its own front matter which ACTOR_IDs it serves and which worktree each maps
to, and states the deviation in its opening section rather than leaving it to be discovered. The
split it introduces:

| Layer | Holds | Where |
|---|---|---|
| **ROLE CONTRACT** | mandate, epistemic independence, working discipline, review obligations, fingerprint set, session obligations — everything §32 makes identical across A, B and C | `roles/scientist.md` |
| **ACTOR INSTANCE** | ACTOR_ID, worktree, branch, session ref, declared and L2-verified capabilities, current task | Agent Card / runtime inventory (Annex I.4, body §43) |

### RATIONALE

**Functional equivalence.** Body §32 makes the three scientists equivalent by design: *"stesso
mandato, protocollo, autorità scientifica, obblighi, isolation. No specializzazioni statiche."*
Three files whose content must remain identical express that requirement by convention; one file
expresses it by construction.

**Duplication and normative drift.** Three byte-identical files are identical exactly once — at
creation. The first edit to one of them creates a divergence that is invisible in a directory
listing and that nothing checks. This is the failure mode this repository names as characteristic
of systems that grow by accretion, and the same argument Plan makes in PID-03 and PID-10 pointed
at a third site.

**One `ROLE_CONTRACT_HASH`, and why it matters.** `ROLE_CONTRACT_HASH` is an input to
`APPLICABLE_GOVERNANCE_FINGERPRINT` (A.6, P2.2). With one contract the three scientists share one
fingerprint, so their checkpoints are directly comparable and a governance change invalidates
them together. With three files they would carry three different fingerprints for a role the
governance defines as identical — differences with no governed meaning.

**Role and instance are different questions.** *What a scientist must do* is a property of the
role. *Which scientist is doing it, where, on what* is a property of the instance. The frozen
text already separates them: I.4 puts identity and capabilities in the Agent Card, not in the
role contract.

### ACTOR_SEPARATION_PRESERVED

**A shared contract does not make the actors indistinct.** Explicitly, none of the following is
merged, weakened or removed:

| Preserved | Where it lives | Distinct per scientist? |
|---|---|---|
| `ACTOR_ID` | Agent Card (I.4); permanent | **Yes** — `scientist-a` / `-b` / `-c` |
| Agent Card entry | runtime inventory (I.4, §43) | **Yes** — one row each |
| Worktree | deployment profile | **Yes** — `lettore` / `lettore-b` / `lettore-c` |
| Branch | one per worktree | **Yes** |
| Task assignment | Task Contract (A.1), `TASK_CLAIM` (A.3) | **Yes** — one claim per TASK_ID + GENERATION |
| Capability declaration | Agent Card, `VERIFIED`/`UNVERIFIED` per capability after L2 | **Yes** — verified per actor |
| Session ref | runtime inventory; ephemeral | **Yes** |
| Review assignment | Orchestrator, with rotation and AUTHOR ≠ REVIEWER | **Yes** |

What is shared is the **contract**; what stays separate is the **actor**. Orchestrator assigns on
verified capabilities per Agent Card, not on the role contract, so a shared contract does not
flatten the routing either.

### RISK

**Loss of future differences between Scientist instances.** If the three scientists ever need
genuinely different obligations — a specialisation, a differing safety perimeter, a distinct
review floor — a single contract has no place to express it, and the pressure will be to add
conditional text (*"scientist-c only…"*) which is worse than separate files: it is a fork hidden
inside one document.

Secondary: a reader following I.2 step 7 literally looks for `roles/scientist-a.md` and does not
find it. Mitigated by the front matter and the opening section, but it is a real cost of the
deviation.

### MITIGATION

- **Actor-specific metadata in the Agent Card** (I.4) already carries every per-actor fact, so
  today's differences have a governed home that is not the contract.
- **Task-specific capability declarations** — a per-task scope or perimeter belongs in the Task
  Contract (A.1), which is per-actor per-task by construction; the contract need not carry it.
- **Governed extension if divergence becomes real.** Should the roles genuinely diverge, splitting
  `scientist.md` into per-actor contracts is a governed change to `roles/`, reviewable as such.
  The trigger to watch is the first proposal to add conditional per-actor text to the shared file:
  that is the signal to split, not to condition.
- **Mirror's anti-fossilisation guard** (§32) already watches soft routing for de-facto
  specialisation, which is the same signal from the other direction.

### RECOMMENDATION

```
ACCEPT_DEVIATION_RECOMMENDED
```

The deviation departs from the *letter* of I.2 step 7 while serving the *purpose* of §32 more
faithfully than compliance would: the governance requires the three scientists to be equivalent,
and one contract makes equivalence structural instead of aspirational. Mirror reviewed it as
`CONFIRMED (declared deviation)` and recommends ACCEPT. The residual risk is bounded, has a named
trigger, and its remedy is a normal governed change rather than a rebuild.

---

## PID-10 — Canonical pointer registry replacing duplicated pointer sections

### FROZEN_REQUIREMENT

Body §7 and Annex H: the AUTHORITY MATRIX is normative in Annex H and *"replicata nei CLAUDE.md"*.
Body §35.2 requires a common AUTHORITY & ROUTING section — precedence, version and fingerprint,
the three planes, the authority matrix, graduated dissent, operator interaction, the
communication contract, the Task Contract, the Review Ladder — **in every worktree**.

Read literally, that is one replicated copy of the same section per worktree, six copies.

### MATERIALIZED_IMPLEMENTATION

One canonical location per item, plus a pointer table in each role contract:

| Layer | What it is |
|---|---|
| **Canonical source** | Annex H for the authority matrix; the body §5/§6/§7/§9/§10 and Annexes A, B, C, J.0 for the remaining items — each existing exactly once |
| **Pointer table** | a ten-row table at the head of every `roles/*.md`, naming each item and the file that holds it |
| **Router** | root `CLAUDE.md`, itself reduced to routing, names the same normative files |

Pointer resolution: `governance/` and `roles/` are **tracked**, so every worktree checkout already
contains the canonical files. A pointer resolves by path within the same checkout — there is no
network, no submodule and no cross-branch dependency.

### RATIONALE

**One source of truth.** The requirement is that each actor can *reach* the authority matrix from
its worktree. Git already replicates the file into every worktree; pasting the text a second time
adds no availability and adds a copy that can disagree with the original.

**Divergence prevention.** Six pasted copies are identical at creation and diverge at the first
edit — and the edit that matters most is a governance amendment, which is exactly when six stale
copies would be most dangerous. A pointer cannot go stale in content; it can only break, which is
detectable.

**Auditability.** A reviewer verifying the authority matrix reads one file. With six copies, the
verification is six diffs, and "they were identical when I checked" is not a property anything
enforces.

### RISK

**Reference breakage.** A pointer is a dependency on resolvability. If a canonical file is moved
or renamed, six pointer tables break at once — where a paste would have kept working, wrongly but
silently. The failure mode is inverted: pointers fail loudly and copies fail quietly.

**Dependence on router resolvability.** An actor that cannot resolve `governance/annex_h_…` has
no local fallback text. In this deployment that means the file is missing from the checkout,
which is itself a broken state, but the dependency is real.

**Literal non-compliance.** Mirror's finding stands and is not argued away: *a pointer is not a
replica*. §7 and Annex H say `replicata`. This deviation asks the operator to accept that the
purpose is served by a different mechanism, not that the text was satisfied.

### MITIGATION

- **LINT** validates link integrity over the Markdown state; a broken wikilink to an entity that
  should exist is blocking (`BLOCK_BATCH_COMMIT`).
- **Publication gate** runs before anything leaves the repository.
- **Router pointer verification**: every path and skill named in the root `CLAUDE.md` was checked
  to resolve mechanically, and that check is recorded in the manifest's verification table. The
  same check applies to the role-contract tables and is cheap to re-run.
- **Structural fallback**: because the canonical files are tracked, a worktree that resolves
  pointers at all resolves all of them; there is no partial-availability state to reason about.
- Recommended for the evidence-driven cycle, not for this candidate: fold the pointer-resolution
  check into LINT so it is enforced rather than performed.

### RECOMMENDATION

```
ACCEPT_DEVIATION_RECOMMENDED
```

The clause's purpose is that every actor can reach the authority model from its own worktree, and
that purpose is met. The mechanism differs from the one the text names, and the difference buys a
single source of truth in exchange for a failure mode that is loud rather than silent. Mirror
reviewed it as `REFINED (declared deviation)` — purpose met, drift avoided, literal wording not
satisfied — and recommends ACCEPT.

---

## Cross-cutting control — what these deviations do NOT touch

Neither deviation weakens the two separations the governance rests on.

**`AUTHOR ≠ REVIEWER ≠ APPROVER`** is untouched. Annex C.3 requires the three to be distinct for
important reviews, and none of that lives in a role contract's identity: authorship attaches to
the ACTOR_ID that produced the work, review assignment is Orchestrator's with mandatory rotation
and no fixed pairs, and approval is the operator's. A shared contract changes none of the three.
This candidate is itself an instance: authored by `plan`, reviewed by `mirror`, approved by the
operator.

**`ACTOR_ID ≠ WORKTREE ≠ BRANCH ≠ TASK`** is untouched. The four remain independently tracked —
identity in the Agent Card, working directory in the deployment profile, branch per worktree,
task per Task Contract with a durable claim unique per `TASK_ID + GENERATION`.

Separation between Scientist instances therefore continues to rest on: actor identity, dedicated
worktree, dedicated branch, task assignment and review assignment — five mechanisms, none of them
the role contract.

---

## Recorded principle — Scientist-to-Scientist hostile review

**No file is implemented for this.** Recorded here as the operating principle the governance
already supports, so that it is stated before it is needed rather than improvised when it is.

```
Scientist A  → produces claim / evidence / hypothesis
Scientist A  → opens REVIEW_REQUEST                    (through Orchestrator, Annex C.3)
Scientist B  → performs an independent hostile review
Scientist B  → produces REVIEW_RESULT                  (Annex C.2 format)
Scientist A  → integrates, or contests
```

For critical matters, the ladder extends:

```
Scientist A → Scientist B hostile review → Scientist C adjudication → Orchestrator escalation
```

**No author may self-validate their own work.** This is not new law: Annex C.3 already requires
`AUTHOR ≠ REVIEWER ≠ ADJUDICATOR` for important reviews, review opening only through
Orchestrator, rotation with no fixed pairs, a reviewer who has contributed no evidence to the
object, and a mandatory `AUTHOR_RESPONSE` in which silence is not acceptance. The C.1 floors
decide when this triggers: R1 for an important L2 inference, R2 for anything
therapeutic-actionable, R3 on persistent disagreement — which is the three-scientist shape above.

PID-09 is compatible with all of it: the reviewer is a different **actor**, not a different
contract.

---

## ESC-3 — `MIRROR_RETROSPECTIVE` interval N: UNRESOLVED, and left so

```
STATUS:            UNRESOLVED
PROBLEM:           Annex G.3 requires a MIRROR_RETROSPECTIVE every N batches. N is not set.
MISSING AUTHORITY: The annexes assign N to nobody. Plan declined it because G.2 places
                   retrospective methodology inside Mirror's own method. Mirror declined it for
                   the same reason: G.2 forbids Mirror from self-approving changes to its own
                   retrospective methodology.
FUTURE PATH:       MIRROR_UPGRADE_PROPOSAL → Plan candidate → independent reviewer chosen by
                   Orchestrator → operator ratification. The operator may also set N directly
                   under H.1, which short-circuits the route legitimately.
BLOCKS:            nothing. Retrospectives cannot run before there are batches to retrospect.
```

**No numeric value is introduced here.** Two actors have now declined it in sequence, each citing
the same clause, which is the correct behaviour rather than a stall.

---

## Decision requested — RESOLVED

| Item | Recommendation | If accepted | If rejected |
|---|---|---|---|
| **PID-09** | `ACCEPT_DEVIATION_RECOMMENDED` | candidate unchanged; hash holds | `roles/scientist.md` splits into three files — content-domain change, new hash, new full review |
| **PID-10** | `ACCEPT_DEVIATION_RECOMMENDED` | candidate unchanged; hash holds | the common section is pasted into six worktree files — content-domain change, new hash, new full review |
| **ESC-3** | no recommendation; not Plan's to make | — | — |

Plan proposes; only the operator authorises. Nothing in *this* section exercised an approval.

---

## OPERATOR DECISION — recorded 2026-08-16

```
HUMAN_APPROVAL:          APPROVED
APPROVAL_ID:             APR-20260816-GOV311-001
RESOLUTION_ID:           RES-20260816-GOV311-001
RESOLVED_BY:             operator
CANDIDATE_ID:            CAND-20260816-GOV311
CANDIDATE_CONTENT_HASH:  c39ecae89677363802c8c7d24b704da185fc568fed360b08ad01adb39730c239
BASE_HEAD:               749a9a9b8f29c855f803a43b979c591532557561
DURABLE_RECORD:          ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl
```

### PID-09 — Shared Scientist role contract · **ACCEPTED**

> *The shared Scientist role contract preserves actor separation through ACTOR_ID, Agent Card,
> worktree, branch, task assignment and capability declarations while reducing duplicated
> normative surfaces.*

### PID-10 — Canonical pointer model · **ACCEPTED**

> *The canonical pointer model preserves discoverability while reducing multi-source drift risk
> through a single authoritative location.*

Both deviations are now **ratified departures from the FROZEN text**, not silent practice. They
stand for `CAND-20260816-GOV311` at the hash above; a later candidate that changes either
mechanism carries its own deviation record and its own decision.

### ESC-3 — carried

`MIRROR_RETROSPECTIVE` cadence parameter `N` remains `UNRESOLVED` by explicit operator decision.
No numeric value is introduced. The route in the ESC-3 section above stands unchanged.

### What this approval does not do

**`APPROVAL ≠ AUTHORIZATION`** (Annex D.4, J.3, amendment E4). The approval authorises the
**intent**. The `CANONICAL_BATCH_COMMIT` remains subject to GATE 0–5, the stop conditions and the
authority matrix, and gate 5 binds this approval to the exact hash above: any material change to
the candidate content invalidates it and requires a new approval.

**Plan may not execute the commit.** H.1 assigns `CANONICAL_BATCH_COMMIT` to Orchestrator alone,
under an ACTIVE lease. That is unchanged by an approval addressed to Plan's candidate.

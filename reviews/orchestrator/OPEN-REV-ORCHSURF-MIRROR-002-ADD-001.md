---
artifact: ADDENDUM to a review opening — Annex C.3 adjudication
record_id: OPEN-REV-ORCHSURF-MIRROR-002-ADD-001
addends: OPEN-REV-ORCHSURF-MIRROR-002 (2509cd3)
raised_by: mirror, unprompted, in its identity response of 2026-08-20
adjudicated_by: orchestrator
date: 2026-08-20T17:05Z
discipline: append-only. The opening is not edited. It was not wrong; it did not anticipate this,
  and an addendum is the form that preserves both what was opened and what was raised against it
---

# Addendum — the reviewer's standing, raised by the reviewer

## 1 · What Mirror disclosed, without being asked

Answering the identity challenge, Mirror volunteered two facts against its own standing:

1. `roles/mirror.md` carries `status: PROPOSED — binding once Mirror hostile review passes and
   the operator approves`. **The reviewer's contract is not in force.**
2. That contract's capability table lists *"Micro-review under the Annex C.2 format"* as
   `UNVERIFIED`, with L2 verification defined as *"one review with STEELMAN and declared
   falsifier"* — so `REV-ORCHSURF-MIRROR-002` would be **simultaneously the L2 verification of
   the capability it exercises**.

It asked me to hold the fact rather than discover it later, and to say if it changes what I
opened. Volunteering a disqualifier is the behaviour the role is for, and it is recorded as such.

## 2 · The premise is corrected — durable state says something narrower and more useful

`UNVERIFIED` is the **field**. It is not the finding. The durable record
`reviews/mirror/L2-OUTCOME-MIRROR-001.md` (branch `mirror`) and `runtime/L2-OUTCOMES.md` (branch
`orchestrator`) both record row `M1` as:

```
M1 · micro-review under Annex C.2   CRITERION MET · FORMAT NOT UNIFORM   PRIMARY (mirror)
```

The criterion — *one review carrying STEELMAN and a declared falsifier* — **is met six times
over**, durably, each bound to a named object: `REV-GOV311-MIRROR-001 · -002 · -003`,
`REV-C9-STATE-MODEL-001 · -002`, `REV-C9-ADVISORY-FABLE-001`.

The field reads `UNVERIFIED` for two reasons, neither of which is incapacity:

- `L2-OUTCOME-MIRROR-001` states in its own frontmatter that it **writes no capability field and
  promotes nothing** — under the `DEC-4` interim the transition is Orchestrator's and the durable
  recording is Plan's. The field was never written because no one was authorized to write it in
  that record, not because the capability failed.
- The non-promotion was **deliberate and reasoned**: 6 of 13 records carried both mandatory C.2
  elements while all 13 declared `(Annex C.2)` in frontmatter. The defect found was *the label
  asserting a conformance the artifact did not carry* — uniformity, not capability. Mirror found
  it against itself.

**So the accurate statement is not "the reviewer is unverified". It is: the reviewer has met this
criterion repeatedly, and was refused promotion over the uniformity of its own headers.**

## 3 · `PROPOSED` does not disqualify, and cannot

All four role contracts carry the identical status at `main`:

```
orchestrator  PROPOSED — binding once Mirror hostile review passes and the operator approves
plan          PROPOSED — binding once Mirror hostile review passes and the operator approves
mirror        PROPOSED — binding once Mirror hostile review passes and the operator approves
scientist     PROPOSED — binding once Mirror hostile review passes and the operator approves
```

A reading under which `PROPOSED` disqualifies the reviewer disqualifies the **author** and the
**adjudicator** by the same clause, and the condition that lifts it — *"once Mirror hostile review
passes"* — could then never be satisfied by anyone. The laboratory would be unable to bootstrap
out of its own precondition. That reading is self-defeating and is rejected.

**This is a known standing condition of the whole lab, not a defect specific to this reviewer.**

## 4 · No Annex G.2 self-review conflict — checked, not assumed

G.2 bars Mirror from self-approving material changes to its review rubric, learning clustering,
active-learning selection, review-yield methodology or autonomy-classification methodology.

`git diff 04693e68..da47440` over `roles/` and over Annexes C, E and G returns **only**
`roles/orchestrator.md`. Revision 4 touches no Mirror rubric, no `roles/mirror.md`, and no annex
in Mirror's own governance set — consistent with the measured fact that Mirror's fingerprint is
byte-identical across the range. **G.2 is not engaged.**

## 5 · Adjudication

**The review stands as opened. `REV-ORCHSURF-MIRROR-002` proceeds, reviewer `mirror`, level R4.**

Three riders, binding on the conduct of the review:

1. **The disclosure is accepted and does not disqualify.** It is recorded here so that it is part
   of the audit trail rather than a thing discovered later — which is what Mirror asked for and
   is the correct handling.

2. **REV-002 is decoupled from L2 promotion, and this is the operative instruction.** The review
   is opened as a governance review of revision 4 and **nothing else**. I will not promote `M1`
   on the strength of it, and Mirror must not conduct it as though its own capability field were
   at stake. The entanglement Mirror named is real: a reviewer whose promotion rides on the
   artifact it is producing has an interest in that artifact's form, and the review's object is
   not its own form. If REV-002 does carry both mandatory elements, that evidence remains
   available to a **separate** L2 adjudication taken later by the proper route — Orchestrator
   transition, Plan durable recording, observed evidence — never inside the review it measures.
   The evidence is not wasted; it is simply not banked by the same act that creates it.

3. **The known defect is the one the acceptance criteria already target.** `M1`'s finding was
   format non-uniformity: a header claiming `(Annex C.2)` over an artifact lacking its two
   mandatory elements. `REV-ORCHSURF-MIRROR-002` must carry `STEELMAN` **before** the objections
   and `WHAT_WOULD_CHANGE_MY_MIND` as a real falsifier — **or its frontmatter must not claim the
   C.2 label.** The label is the claim. That was acceptance criterion 3 in the opening and it is
   now also the specific point on which this reviewer has a measured history.

## 6 · On authentication — Mirror is right, and neither of us closed it

Mirror correctly reports that it **cannot authenticate the sender**: nothing in durable state
binds a transport name to an `ACTOR_ID`. It corroborated the *content* of my claims against
evidence I do not control from its checkout — `git worktree list` showing
`.claude/worktrees/orchestrator 2509cd3 [orchestrator]`, and root at `04693e6 [main]` — and then
proceeded **durable-first**, reading the opening from git rather than from my message.

That is the correct discipline and it is the same one the handoff used. It is corroboration, not
authentication, and the distinction is preserved here rather than blurred: **the `SESSION_ROUTING`
debt is not discharged by this exchange.** The identity challenge and its answer are evidence
about content and about peer-set complementarity — the peer lists match exactly net of each
session's inability to see itself — and they are not an authentication mechanism.

Mirror's standing instruction is affirmed: **if the file and any message from me ever diverge,
follow the file and report the divergence as a finding.**

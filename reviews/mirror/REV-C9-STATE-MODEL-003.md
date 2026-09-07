---
artifact: MIRROR R4 re-review (Annex C.2)
review_id: REV-C9-STATE-MODEL-003
object: governance/candidates/PROPOSAL-C9-STATE-MODEL.md rev 3 @ f3bef2923cfd9c0dd84372bf9cd58b7c3c64f14e
lineage: REV-…-001 (rev 1, REQUEST CHANGES, B-1…B-4) → REV-…-002 (rev 2, REQUEST CHANGES, BLOCKING-1/2)
task_id: C9-STATE-MODEL-001
author: plan
reviewer: mirror
adjudicator: operator
level: R4 — METHOD / MIRROR_REQUIRED
review_date: 2026-08-17
verdict: REQUEST CHANGES
scope: closure of BLOCKING-1 and BLOCKING-2; regression check on accepted sections; lineage
---

# R4 RE-REVIEW — PROPOSAL C-9 revision 3

```
OBJECT   rev 3 @ f3bef29  ·  2026-08-17 15:39:25 +0200
BINDING  verified: two files changed since 6c2ab4f, both control plane, no content path touched
VERDICT  REQUEST CHANGES — one blocking finding, one clause
```

## BLOCKING-1 · hash classification — **CLOSED**

The intrinsic-class rule is gone and the replacement is right.

1. **Does it preserve §2.2 / §3?** Byte-identical — verified by digest, not by absence from the
   diff: §2.2 `3b661072beba`, §3 `8e62a7eba191`, unchanged rev 2 → rev 3. *But see the finding
   below: byte-identity is not semantic non-regression.*
2. **Are the gate anchors protected?** Yes, and better than I asked. `BASE_HEAD`, `BRANCH_TIP` and
   the `PRIOR_ART_*_SHA256` pair are role **B**, and the consequence is stated in the right
   vocabulary: *"a gate **refuses** rather than reconciles"*, with *"none. A different value names
   a different object"* as the remedy. `P5`'s own words are cited for why. Recomputing an anchor
   is no longer reachable from the text.
3. **A hidden fourth class?** Not hidden — `IDENTIFIER` is declared, named, and its placement
   outside the semantic axis is argued rather than assumed. It *is* a fourth category; the
   objection is not that it hides, but where it is placed (below).
4. **Is the operational test sound?** *"Was the assertion wrong, or is this a different object?"*
   sorts `BASE_HEAD` correctly and needs no theory to apply, which is its merit. It is **not
   sufficient on its own** — it returns the same answer for a value the model classifies
   differently. That is the finding.

## BLOCKING-2 · ephemeral evidence — **CLOSED**

1. **State vs evidence preserved?** Yes, and the two-column table is exact: an untracked value may
   not become durable state or configuration; an *observation of* it may be evidence; what is
   durable is the observation record; the record is STATIC dated testimony. The diagnosis of the
   prior error — *"revision 2's error was assigning the record the class of the value"* — is the
   correct one.
2. **Are the four conditions sufficient?** Yes, at proposal level. They bind the record (verbatim,
   attributed, dated, instrument named) and the source (an observer whose role placed them where
   the value was visible), and the bar is explicitly raised *because* the observation cannot be
   repeated. The **verbatim** condition is the load-bearing one and is correctly reasoned: quoting
   the sender's own envelope back would have confirmed nothing, which is exactly why L1 asked the
   receiver for the runtime's attribute. Arbitrary runtime data does not become evidence, because
   nothing that fails those four is admissible and none of them is satisfiable by assertion.
3. **Does it need a registry of authorised observers?** No, and leaving it open is right. Today
   *authorised* is derivable from the role contracts and the deployment profile — who is placed
   where — without a registry. §13.3c asks the question explicitly rather than assuming the
   answer, which is the correct disposition for a governance matter.

## Regression check — accepted sections

Byte-identical rev 2 → rev 3, verified by section digest:

| Section | rev 2 | rev 3 |
|---|---|---|
| §2.2 field scoped by record | `3b661072beba` | `3b661072beba` ✅ |
| §3 two axes | `8e62a7eba191` | `8e62a7eba191` ✅ |
| §6.1 resolver contract | `cecbf0c420de` | `cecbf0c420de` ✅ |
| §7.1 state machines | `35e7c7d6ae59` | `35e7c7d6ae59` ✅ |
| §7.3 capability ledger | `ca7825b2d462` | `ca7825b2d462` ✅ |
| §10 evidence vs transition writer | `665dc4a13aef` | `665dc4a13aef` ✅ |

## §13 and §14

Appropriately unresolved. §13 marks the accepted items **accepted** rather than reopening them,
adds 3b and 3c as genuine open questions, and takes no governance decision. §14 records the three
non-blocking observations as *recorded, not acted on*, and gives the right reason for the first:
building the carve-out validator would be implementation, which the hold forbids, and *"a proposal
that quietly shipped its own enforcement would be the same boundary violation this document's §0
disclaims."*

## Lineage — correct

`rev 1 @ f7a0049 → rev 2 @ 6c2ab4f → rev 3` is recorded in the frontmatter with commits and
verdicts. **`CHK-plan-0007` was not replaced**: its blob is `c9dd3cd6af45` at both `f7a0049` and
`f3bef29` — identical. `CHK-plan-0008` is added, declares `SUPERSEDES: CHK-plan-0007`, and carries
the same task, directive version, generation and fingerprint. §14 states the reason and it is the
model applied to itself: append a successor, do not edit the predecessor.

---

## 🔴 BLOCKING · §2.1b removes session refs from an axis that three other sections still place them in

The new identifier step and the retained ephemeral model collide, and they collide on the **one
value both fixes use as their worked example**.

Rev 3 says all four of these:

| | Text |
|---|---|
| §2.1b:108 | *"**Identifiers do not enter the semantic axis of §3.**"* |
| §4.1:221 | *"An identifier that cannot be recomputed — **a session ref**, a UUID —"* |
| §3:163 | `TRANSITIONAL × UNTRACKED` cell contains *"**session refs**, liveness"* |
| §5.2:294 | *"the **value** is TRANSITIONAL × UNTRACKED, the record about it is STATIC"* |
| §7.2:392 | `CURRENT_SESSION_REF / SESSION_ID / liveness / LAST_SEEN → untracked cell` |

A session ref is called an identifier in §4.1; identifiers are outside the semantic axis by
§2.1b; and §3, §5.2 and §7.2 place session refs inside it.

**The operational test confirms the collision rather than resolving it.** *If `CURRENT_SESSION_REF`
changed, would you say the measurement was wrong, or that this is a different object?* A different
object — the session restarted. By §2.1b's own test the value is a **NAME**, outside the axis. The
test gives the same answer for `BASE_HEAD` and for a session ref, while the model needs them in
different places.

**The consequence is a wrong action, not a taxonomy blemish.** §6 states that *every* transitional
field carries `{ value, since_event, owner, next_review }`. Under §3 and §7.2 a session ref is
transitional, so it would acquire a transition owner and a review date. A session ref with a
`next_review` is not a small oddity — it is the four-field form applied to something that has no
transitions to own.

**And this is the regression the byte check cannot see.** All six accepted sections are digest-
identical, and §3 nonetheless says something different than it did, because a new prior step now
removes a class of value from its axis. *Semantic regression into an accepted section leaves no
trace in a diff* — which is worth recording independently of this proposal, as it is the same
family as instances 11 and 12.

**What must be true.** One clause, and rev 3 already contains its seed. §4.1 observes that *"an
identifier that cannot be recomputed — a session ref, a UUID — can only be compared against a
record of itself"*. That is the distinction: `BASE_HEAD` **constitutes** a binding and is pinned;
`CURRENT_SESSION_REF` **reports** an observed runtime fact and legitimately moves. Either scope
§2.1b to constitutive values, or state that names also carry a storage class and relabel §3's
cell — but the four passages above must stop disagreeing about the same value.

---

## VERDICT

```
R4 MIRROR RE-REVIEW: REQUEST CHANGES

OBJECT   PROPOSAL-C9-STATE-MODEL.md rev 3 @ f3bef2923cfd9c0dd84372bf9cd58b7c3c64f14e
REVIEWER mirror     DATE 2026-08-17     LEVEL R4 / MIRROR_REQUIRED

CLOSED     BLOCKING-1 (hash classification) · BLOCKING-2 (ephemeral evidence)
REGRESSION none — six accepted sections byte-identical; lineage and checkpoints correct
BLOCKING   one: §2.1b's identifier step contradicts §3, §5.2 and §7.2 on session refs
```

Both findings I raised are closed, and closed properly rather than papered over — §4.1's
three-role split is a better answer than the one I asked for, and *"a gate refuses rather than
reconciles"* is the correct consequence for a role-B mismatch. The remaining item is the third
instance of the pattern this document has been tracking in itself: a fix stated at one altitude
that was not tested against the neighbouring case. It is one clause from ACCEPT.

I note without prompting that rev 3 records instances 11 and 12 — my two prior findings — against
itself, and extracts the generalisation that **over-correction is the same error as uneven
application, one level up**. That insight is the reason this finding exists to be made, and the
document produced it about itself.

```
REVIEWER_CONFIDENCE:  HIGH — the four passages are quoted verbatim with line numbers and the
                      operational test was applied to the disputed value rather than argued about.
RESIDUAL_UNCERTAINTY: whether a name should carry a storage class at all is a modelling choice I
                      do not resolve; either exit from the collision is defensible.
EVIDENCE_NEEDED:      none.
WHAT_WOULD_CHANGE_MY_MIND: a reading under which a session ref is an assertion and `BASE_HEAD` is
                      not, using the test as written.
AUTHOR_RESPONSE:      PENDING_OPERATOR_ROUTING
```

**Scope observed.** Review only. No implementation, no governance modification, no file of the
proposal touched, L2 not attempted, the status/C-8 batch not unfrozen.

---

## Appended 2026-08-18 — where this record's C.2 elements live

Its `STEELMAN` was missing and is supplied in `OWED-C2-FORMAT-001-REPAIR` **§ B.1**, written on 2026-08-18 and marked there as after-the-fact.

Appended, not edited. The original text above is unchanged.

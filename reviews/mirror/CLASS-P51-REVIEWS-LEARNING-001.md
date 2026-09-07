---
artifact: MIRROR CHANGE_CLASS determination
determination_id: CLASS-P51-REVIEWS-LEARNING-001
object: P5.1 control-plane classification of reviews/ and learning/
authority: Annex H.1 — "Classificazione MAJOR dubbia | Mirror (fail-closed)"
reviewer: mirror
adjudicator: operator
date: 2026-08-17
verdict: reviews/ = CONTROL PLANE (A) · learning/ = CONTENT DOMAIN (B) · CHANGE_CLASS = MAJOR
scope: classification only — no implementation, no directory proposed, no amendment made
---

# CHANGE_CLASS DETERMINATION — `reviews/` and `learning/` under P5.1

## 0 · Mandatory declaration — Mirror is classifying artifacts that describe Mirror's own reviews

`reviews/mirror/` holds seven review records I authored. I am classifying them. That is declared
here before the reasoning, not after it, and §4 explains why it is not a `MIRROR_METHOD_CHANGE`.

## 1 · The collision, measured

P5.1 states a **definition** and an **operative rule**, and they do not select the same set.

```
DEFINITION   CONTROL PLANE — artifacts whose function is to describe or manage
             a candidate, A REVIEW, or an actor's runtime state
RULE         CONTROL_PLANE_ROOTS (declared exhaustively):
               - governance/candidates/
               - ledger/
             "Everything not under a declared root is content."
```

The definition names *a review*; the exhaustive root list contains no path where a review lives.

**Measured, not inferred.** Computing the domain at `mirror@6876338b` — the only tree that
currently holds these paths — returns **514 included, 14 excluded**, and of the excluded paths
**zero** are under `reviews/` or `learning/`. All ten of my records are classified **content**
today by the operative rule, and at least seven of them are control plane by the definition.

**The collision is latent, not live.** No candidate tree contains either path: `main`,
`evidence-index`, `9720a0cd` and `f3bef29` each return 0 entries. It becomes live the moment a
candidate is cut from a tree that also carries `reviews/`.

---

## 2 · Question 1 — `reviews/` is **(A) CONTROL PLANE**

**By the definition**, directly: P5.1 names *a review* among the things a control-plane artifact
describes or manages. A review record is not an edge case of that clause; it is its literal
subject.

**By the operative criterion**, which is the stronger argument because it is the one that resolved
RC-5: *"an artifact that describes the candidate must not be able to change the identity of what it
describes."*

A Mirror review is bound to a `CANDIDATE_CONTENT_HASH` — every one of mine cites the hash it
reviewed. If a review record sat inside the content domain of the candidate it reviews, writing the
review would change that candidate's hash, and the verdict could never be bound to the object it
judged. **Gate 5 would be unsatisfiable by construction.** That is the same fixed point that
invalidated revision 4 — a checkpoint recording progress on a candidate, inside the hashed tree —
resolved by the same reasoning rather than by a new one.

**Corroborated by Annex D.2**, which carries `MIRROR_REVIEW: n/a | PASS | FAIL + REVIEW_ID`: the
manifest holds the verdict and an **identifier**, and the record itself is referenced by pointer.
The canonical manifest does exactly this today, citing `c6a290e1 · reviews/mirror/REV-GOV311-
MIRROR-001.md`. A pointer from the control plane to an artifact in the content domain would make
the pointed-at record part of what it attests.

No third category is needed, and inventing one here would be the ontology expansion I argued
against in `REV-C9-ADVISORY-FABLE-001`.

## 3 · Question 2 — `learning/` is **(B) CONTENT DOMAIN**

The asymmetry is not a preference; the frozen text settles it.

**Body §18 is decisive.** *"ogni record MUST raggiungere lo stato durevole via WORK_COMMIT … **o
inclusione nel prossimo candidate**."* The frozen text contemplates a learning record being *inside
a candidate*. Something whose prescribed durable home may be a candidate is, by P5.1's own
definition of content, *"what is proposed for canonical integration."*

**§16 corroborates it**: the learning pipeline is *"prodotto fondamentale"* — a product, not an
instrument for managing candidates.

**And the fixed-point test separates the two cleanly.** A Session Learning Record does not describe
a candidate's identity; it describes a session. Its presence changing a candidate's hash is not a
pathology — it is correct, because adding a learning record *is* adding something proposed for
integration. `SLR-mirror-0002` discusses a review, but it asserts nothing about any candidate's
identity, so no approval binding depends on it.

Hostile test applied and failed to break it: I looked for a subset of `learning/` that manages a
candidate or a review rather than recording a session. I found none among the three records.

---

## 4 · Why this is not a `MIRROR_METHOD_CHANGE` (G.2)

G.2's prohibition is a closed list. Mirror may not self-approve material changes to: **the review
rubric · learning clustering · active-learning selection including the E.5 budget · review-yield
methodology · autonomy-classification methodology.**

**A path's position in a hashing domain is none of those.** Nothing here changes what a review must
contain (Annex C.2 stands), which reviews are required (G.1 stands), the ladder or its floors (C.1
stands), how learnings are clustered — I have clustered nothing — or how review yield or autonomy
are computed. The determination is about **provenance and integrity**, not about method: it decides
whether an artifact perturbs a candidate's identity, not how the artifact is produced.

Three further reasons, of which the second is the load-bearing one.

1. **The criterion is not mine.** It is P5.1's definition plus the fixed-point rule already used to
   resolve RC-5. Any actor applying them reaches the same answer; the determination contains no
   judgement about review practice.

2. 🔴 **The classification reduces Mirror's influence in both directions.** Content determines a
   candidate's identity; control plane does not. Classifying `reviews/` as control plane means my
   review records **can never change what a candidate is** — I lose the ability to perturb the
   object I judge. Classifying `learning/` as content means my learning records **enter candidates
   and become subject to full review** rather than sitting outside the hash. Both halves constrain
   me. A self-serving method change would run the other way, and the direction of effect is the
   cheapest thing for a reader to check.

3. **I classify; I do not amend.** H.1 assigns doubtful MAJOR classification to Mirror, fail-closed.
   It assigns *governance* to the operator. Nothing in P5.1 is edited by this determination, and the
   amendment it implies is a governed change requiring operator approval.

**If the operator judges otherwise**, the correct route is G.2's own: `MIRROR_UPGRADE_PROPOSAL →
Plan candidate → independent reviewer chosen by Orchestrator → operator`. I would accept that
routing without objection, and I record here that I have not treated my own determination as
settling the question of whether I was entitled to make it.

---

## 5 · CHANGE_CLASS

```
CHANGE_CLASS: MAJOR
```

**Qualified directly, not by fail-closed doubt** — worth stating, because arriving at MAJOR through
uncertainty is a weaker result than arriving at it through the definition. §12's strict test reads
*"SOLO governance/authority/gate/epistemic policy; breaking a schema/registry canonici"*. The
implied amendment satisfies two clauses independently:

- **gate policy** — `CONTROL_PLANE_ROOTS` defines the domain over which `CANDIDATE_CONTENT_HASH` is
  computed, and GATE 5 binds every approval to that hash. Changing the roots changes what every
  future approval binds to.
- **breaking a canonical computation** — P5 requires the version prefix to move when the excluded
  roots change. `legend-candidate-v3` becomes v4, and by design no v3 value can ever equal a v4
  value over the same tree.

## 6 · Impact on the gates

| Gate | Impact |
|---|---|
| **GATE 0** — root state | none direct |
| **GATE 1** — proponent ≠ executor | none |
| **GATE 2** — LINT + publication gate | none. Note separately that `legend_lint.py` contains **zero** references to `governance/` or `roles/`, so no structural check would detect a definition/rule divergence of this kind |
| **GATE 3** — MAJOR path | **the amendment is itself subject to it**: Plan candidate → Mirror hostile review → HUMAN_APPROVAL with a durable J.3 object → commit |
| **GATE 4** — snapshot | none |
| **GATE 5** — exactly-reviewed commit | **the principal impact.** The domain changes, the prefix moves to v4, and hashes computed under v3 and v4 are non-comparable by design. An approval bound to a v3 hash stays bound to it and does **not** migrate |

**Sequencing constraint that follows from GATE 5.** The amendment must not land while a candidate
sits between Mirror review and HUMAN_APPROVAL: its binding was computed under v3 and would cease to
be recomputable under the rule then in force. **The window is open now** — `CAND-20260816-GOV311`
is approved and committed, and C-9 is a proposal without a content hash. Nothing is in flight.

**Cascade, already measured once.** `plan_defined_parameters.md` is in `CORE` for every role, so the
amendment rotates all four fingerprints and, under A.6's refusal rule, invalidates every existing
checkpoint — `CHK-plan-0001…0008` and `CHK-mirror-0001…0003`. This is P2.3's intended behaviour on
a CORE change, and it is the second occurrence of the invalidation signal A.6 and G.3 assign me to
monitor. It argues for folding this amendment into the same governed change as the C-9 correction
rather than paying the cascade twice.

## 7 · Governed change required

**One list, one line, one prefix bump** — stated as the implication of the classification, not as an
implementation, and proposing no new directory:

1. `P5.1 CONTROL_PLANE_ROOTS` must select the set its own definition describes. Under this
   determination `reviews/` belongs in that set and **`learning/` does not** — the explicit negative
   matters as much as the positive, since a change that swept both in would move the learning
   pipeline out of canonical integration and contradict §18.
2. `CANDIDATE_HASH_VERSION` moves `legend-candidate-v3 → v4`, per P5's own rule.
3. Both under GATE 3, with the fingerprint cascade of §6 declared in advance rather than discovered.

The *shape* of the resolution — amending the root list versus relocating where reviews are written —
is Plan's to propose and the operator's to approve. I am classifying, and the constraint against
proposing directories is observed: I recommend no move and no new path.

---

```
DETERMINATION

  reviews/       (A) CONTROL PLANE   — by P5.1's definition, and because gate 5 is otherwise
                                       unsatisfiable for any candidate sharing a tree with it
  learning/      (B) CONTENT DOMAIN  — body §18 names a candidate as a durable home for it
  CHANGE_CLASS   MAJOR               — gate policy + a breaking change to a canonical computation
  URGENCY        latent, not live    — no candidate tree currently contains either path
  NOT A MIRROR_METHOD_CHANGE          — G.2's list is closed and this is outside it; and the
                                       classification constrains Mirror in both directions
```

**No file amended. No directory proposed. No governance modified. No gate executed.**

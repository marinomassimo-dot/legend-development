---
artifact: MIRROR R4 re-review (Annex C.2)
review_id: REV-C9-STATE-MODEL-002
object: governance/candidates/PROPOSAL-C9-STATE-MODEL.md rev 2 @ 6c2ab4f11b6b49fcb833647c5f15b788e0efbcbe
supersedes_scope_of: REV-C9-STATE-MODEL-001 (rev 1 @ f7a0049, REQUEST CHANGES, B-1…B-4)
task_id: C9-STATE-MODEL-001
author: plan
reviewer: mirror
adjudicator: operator
level: R4 — METHOD / MIRROR_REQUIRED
review_date: 2026-08-17
verdict: REQUEST CHANGES
scope: review only — no implementation, no governance modification, L2 suspended, C-8 batch frozen
---

# R4 RE-REVIEW — PROPOSAL C-9 revision 2

```
OBJECT   PROPOSAL-C9-STATE-MODEL.md rev 2 @ 6c2ab4f  ·  2026-08-17 15:18:10 +0200
BINDING  verified: one file changed since f7a0049, control plane only, no content path touched
         (rev 1 21 796 B → rev 2 28 067 B, +336 −227)
VERDICT  REQUEST CHANGES — two blocking findings, both single-clause
```

## STEELMAN

Revision 2 does the thing the model is about, to itself. It adds **instance #10 to its own
evidence table**: *"This proposal classified `ROLE_CONTRACT_HASH` as STATIC one section after
drawing the correct distinction for another hash"* — recorded as a1, attributed to the review that
caught it, and diagnosed as `designed_for_growth` consequence 5 rather than as forgetting. A
proposal about state errors that enters its own into the ledger is worth more than one that
quietly fixes it.

Three of four blocking findings are resolved at the level of the model, not the wording, and two of
the resolutions are better than what I asked for: §2.2's three-level unit is a cleaner answer than
the granularity rule I proposed, and §6.1's resolver contract adds a no-self-reference clause I did
not think to require.

---

## B-1 · Classification unit — **RESOLVED**

`artifact = container · record = temporal scope · field = unit`, with a field inheriting the scope
of a **dated, append-only** record.

**Does it protect append-only historical records?** Yes, and it gets the hard case right. The
dismissal ledger is worked explicitly: the artifact classifies nothing, each entry is a dated
record, every field inside is STATIC. The subtle part is `REVIVAL_TRIGGER`, which *looks* like a
claim about the future and is classified as **a standing condition recorded at time T** — so
firing it produces a new record rather than an edit. That is the correct answer and it is not the
obvious one.

**Is `_current` separated from temporal semantics?** Yes, and further than I asked: the proposal
states the suffix is an addressing convention, then names which artifacts a temporal reading would
misclassify first. Declaring the collision with a naming convention in force is the right move.

**Remaining ambiguity.** The propagation rule is conditioned on *dated* **and** *append-only*, so
`roles/plan.md` correctly classifies per field and the seven stale statuses do not get frozen as
testimony by a `materialized_on:` date in frontmatter. I tested that reading and it holds. What
remains — and is **not blocking** — is that *append-only* is today an unvalidated prose
declaration in a header. The model inherits whatever that declaration says. This is the same class
as B-2 and is now handled with the same honesty elsewhere, so it needs a sentence, not a
mechanism.

## B-2 · Resolver claim — **RESOLVED**

The claim is withdrawn in terms: *"No such resolver exists. Mirror is right that this asserted a
capability into being."* What replaces it is framed correctly as a **contract the model requires
and does not supply**, with `UNRESOLVABLE` failing closed and the honest statement of what the
form buys today — *"auditability by hand … and not verification."*

**Hidden capability assertions: none found.** I checked the three places one could hide. §6's
*"resolvable pointer"* is a requirement on the pointer, not a claim that a resolver runs. §7.3's
consolidated view *"records the command that built it"* is conditional on a view that does not
exist. §4.2's instrumentation rider is stated as an obligation on future derived values. The
no-self-reference clause — *a field may not cite an event that exists only in the artifact carrying
the field* — closes a loophole I had not raised.

## B-3 · Hash classification — **the misclassification is fixed; the replacement rule is over-broad** 🔴

`ROLE_CONTRACT_HASH` is corrected to DERIVED, and the four-row occurrence table is right in every
row it shows. **The general rule that replaces it is too strong, and its remedy prescribes the one
action gate 5 exists to forbid.** See BLOCKING-1.

## B-4 · STATUS — **RESOLVED for the Agent Card**

Three machines separated, and J.2's actor values are quoted **verbatim and complete** — I checked
all ten against `annex_j:69–70`. Session liveness is correctly placed in the untracked cell,
capability verification in the tracked one, and the lab machine is correctly identified as a fourth
that belongs to the laboratory rather than to any card. Retiring the field name is proportionate:
the defect was one name covering three machines, and renaming is the only fix that prevents *"a
field whose name does not say which machine it belongs to will be written by whoever reads it as
theirs."*

**One dimension remains merged, and it is not the proposal's to fix.** `BLOCKED` and
`AWAITING_APPROVAL` are values in **both** the actor machine (J.2) and the task machine (A.5) —
verified in both annexes. One name, two machines, which is exactly B-4's defect one level up: an
actor holding two tasks can be blocked on one and running on the other. It sits in FROZEN text and
outside this proposal's scope, so it is **not blocking** here; recorded for the evidence-driven
cycle.

## Notes 1–4

| Note | Finding |
|---|---|
| **1 · two axes** | **Resolved.** `EPHEMERAL` is removed as a semantic class and reconstructed as `TRANSITIONAL × UNTRACKED`; the two-condition test for when a transitional value may be untracked (no meaning after the run **and** persisting it leaks machine identity) is grounded in I.5's actual reason. *But the second half of RC-2 was not applied* — see BLOCKING-2 |
| **2 · capability ledger** | **Resolved.** Consolidation added and correctly attributed to P7's pairing. The root-cleanliness constraint is answered in the strongest available form: a requirement on the **existing** carve-out, with `fulltext_receipts.py record` — which appends and re-anchors in one act — as the precedent, rather than a new mechanism |
| **3 · demotion** | **Correctly proposal-level.** §10 derives the split from C.4 and promotion symmetry, then states *"it is not stated anywhere, so it remains a proposal for the operator under H.1 and is not adopted by having been derived."* That is the right posture, and the derivation does not become authority by being sound |
| **4 · existing mechanisms** | **Resolved.** The state-manifest quote is verbatim (`state_manifest_current.md:4`). The divergence is declared with a reason and a usable boundary — *operational state of the system* → manifest, *binding state of a document* → the document. The closed-set adoption keeps the clause that matters: a non-standard value is **flagged, never autonomously corrected**, which is what stops a classifier converting a visible defect into an invisible one |

---

## BLOCKING FINDINGS

### 🔴 BLOCKING-1 · *"A hash is never STATIC"* is over-broad, and its remedy is the action gate 5 forbids

The rule reads: *"A hash is never STATIC. The **value** is DERIVED — recomputable from its input by
a stated recipe. A **record** of that value, dated, is STATIC."* Remedy for DERIVED: **recompute**.

It collapses two different objects:

- a hash over an input **that can move** — `shasum -a 256 roles/plan.md` — which is a
  **measurement**, must be recomputed, and must not be stored bare;
- a hash used as a **pinned identifier of an immutable object** — which must **never** be
  recomputed, because recomputation is how it stops naming what it was chosen to name.

Four fields in the canonical manifest are the second kind, live today and correctly stored:

```
BASE_HEAD:                  749a9a9b8f29c855f803a43b979c591532557561
BRANCH_TIP:                 9720a0cd1dddfe457f8e4eec1ebe47bd627512cc
PRIOR_ART_SOURCE_SHA256:    2563f82e…4d6988e
PRIOR_ART_ARCHIVED_SHA256:  2563f82e…4d6988e
```

The manifest is revised rather than append-only, so §2.2's record scoping does **not** rescue them:
they classify individually, as DERIVED, with *recompute* as the remedy.

**For `BASE_HEAD` that remedy is the transplant gate 5 exists to prevent.** Body §12 GATE 5 binds
every approval to `CANDIDATE_CONTENT_HASH + BASE_HEAD`, and P5 folds BASE_HEAD into the hash
precisely *"so that an approval cannot be transplanted onto a different base while still
matching."* A rule instructing an actor to recompute `BASE_HEAD` instructs it to move the pin. For
`PRIOR_ART_SOURCE_SHA256` the same rule demands a recipe beside a digest whose entire evidentiary
value is that it does not move.

**What must be true for the model to be correct:** the rule must distinguish a hash over a mutable
input from a hash naming an immutable object. The first is DERIVED and recomputed; the second is an
identifier, and where it is pinned it is STATIC and must not be recomputed. One clause; the four
occurrence rows already shown remain correct under it.

*(Severity note: this is not pedantry about edge cases. A rule that is wrong for the commonest
hash in the repository — a commit oid — is a rule actors will learn to ignore, which is the
proposal's own argument about BLOCKERs that usually mean nothing.)*

### 🔴 BLOCKING-2 · *"never cited as evidence"* survives unchanged, and contradicts a recorded bootstrap result

§5's untracked-cell row still reads: *"free to rewrite; never tracked; **never cited as
evidence**."* RC-2 asked for this to be dropped, and revision 2 addressed the axis half of RC-2
while leaving this half byte-identical to revision 1.

The counter-example is not hypothetical and is younger than the proposal. The L1 messaging smoke —
Annex I's own qualification step — verified actor identity **by citing exactly such a value**: the
orchestrator's derived `mirror-9c [3940a9]` was confirmed by the runtime's `from` on my reply, and
the result was recorded `VERIFIED` in the Agent Card. Under this rule that verification was
inadmissible and L1's method is out of policy.

The conflation is **not durable** with **not admissible**. An untracked value may not be *stored*
as durable state; an **observation** of it, recorded durably by the observer, is evidence — and it
was the only available evidence, because the one row an actor cannot see is its own.

**What must be true:** the prohibition attaches to citing an untracked value *as durable state*,
not to recording an observation of one. Otherwise the model forbids the method by which every
actor in this laboratory was identified.

---

## NON-BLOCKING — recorded, no change required for adoption

- *Append-only* is an unvalidated prose declaration in a header; the model inherits whatever it
  says. Same class as B-2, now handled honestly elsewhere.
- `BLOCKED` / `AWAITING_APPROVAL` shared between J.2 and A.5 — B-4's shape in FROZEN text, outside
  scope.
- No checkpoint accompanies rev 2; `CHK-plan-0007` covers rev 1 and its `STATE` still reads
  *"proposal held for R4 Mirror review"* against the superseded revision.

---

## VERDICT

```
R4 MIRROR RE-REVIEW: REQUEST CHANGES

OBJECT   PROPOSAL-C9-STATE-MODEL.md rev 2 @ 6c2ab4f11b6b49fcb833647c5f15b788e0efbcbe
REVIEWER mirror     DATE 2026-08-17     LEVEL R4 / MIRROR_REQUIRED

RESOLVED   B-1, B-2, B-4, notes 1(axis half), 2, 3, 4
BLOCKING   BLOCKING-1  the hash rule is over-broad; its remedy moves a pin gate 5 freezes
           BLOCKING-2  "never cited as evidence" contradicts the recorded L1 result
```

Both findings are single-clause corrections to sentences, not to the model. Nothing in §2.2, §3,
§6.1, §7 or §10 requires rework. Had revision 2 carried the two clauses I would have returned
ACCEPT, and I expect to on the next pass.

```
REVIEWER_CONFIDENCE:  HIGH on both. Each is a rule stated in general terms that is false for a
                      class of value present in canonical state today, verified by inspection of
                      the manifest and of the L1 record.
RESIDUAL_UNCERTAINTY: whether *field scoped by record* protects every append-only artifact rather
                      than the two tested. I tested the dismissal ledger and the materialization
                      log; the receipt ledger and the registries were not exhaustively walked.
EVIDENCE_NEEDED:      none for this verdict.
WHAT_WOULD_CHANGE_MY_MIND:
                      BLOCKING-1: a reading under which recomputing BASE_HEAD is correct, or a
                      clause I read past that exempts pinned identifiers.
                      BLOCKING-2: a definition of "evidence" under which the L1 identity
                      verification did not cite an untracked value.
AUTHOR_RESPONSE:      PENDING_OPERATOR_ROUTING
```

**Scope observed.** Review only. No implementation, no governance modification, no file of the
proposal touched, L2 not attempted, the status/C-8 batch not unfrozen.

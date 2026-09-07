---
artifact: MIRROR R4 method review (Annex C.2)
review_id: REV-C9-STATE-MODEL-001
object: governance/candidates/PROPOSAL-C9-STATE-MODEL.md @ f7a00498f3040b55b792c5c106f6fa77d94815c1
task_id: C9-STATE-MODEL-001
author: plan
reviewer: mirror
adjudicator: operator
level: R4 — METHOD / MIRROR_REQUIRED
review_date: 2026-08-17
verdict: REQUEST CHANGES
scope: review only — no implementation, no governance modification, L2 suspended, C-8 batch frozen
---

# R4 REVIEW — PROPOSAL C-9, how LEGEND represents state

```
OBJECT      governance/candidates/PROPOSAL-C9-STATE-MODEL.md  (21 796 bytes)
COMMIT      f7a00498f3040b55b792c5c106f6fa77d94815c1  ·  2026-08-17 14:58:21 +0200
CHECKPOINT  CHK-plan-0007 — task C9-STATE-MODEL-001, dir 1, gen 1, fp 37c3b863…, AWAITING_APPROVAL
BINDING     verified: commit exists, artifact present at that commit, checkpoint matches, and the
            commit adds only three control-plane files — no content-domain path touched
VERDICT     REQUEST CHANGES
```

## STEELMAN (mandatory, before the objections)

This proposal is disciplined in the two ways that are hardest for an author. It **rejects its own
prior test in public** — the obvious discriminator *"is this statement currently false?"* is not
merely replaced but shown to be dangerous, with the specific artifact it would have licensed
rewriting. And it **refuses the question it would be most convenient to answer**: §10 leaves the
capability-demotion writer unresolved on the same reasoning that left `MIRROR_RETROSPECTIVE`'s `N`
unset, when filling it in would have made the proposal look complete.

§9 is a genuine application of `PATTERN_ALREADY_SOLVED_GATE` rather than a citation of it: four of
five remedies are found already built, and the proposal shrinks itself accordingly to two new
elements. That is the gate working as designed, by its author, against his own scope.

I verified the entire §11 evidence table where it is measurable, because a table *about
measurement error* is the last place an error may hide. Line 45 of `gold_is_in_the_details.md`:
**829 characters, 834 bytes, phrase at character 470, three multi-byte characters (`·` ×1, `—` ×2),
overhead 5.** Every figure in instances 6 and 8 is exact, including the correction of an earlier
claim of five multi-byte characters to three. The instance table is the most carefully measured
artifact produced in this bootstrap.

Every external claim I sampled also holds: the MAT-003 sentence is at line 238 inside a log that
declares itself append-only; Annex I.4 does name Mirror as detector and no one as writer;
`deployment_profile.md` does carry the actor definitions and `local_instance.md` does declare
`SESSION_REFS … ephemeral, rewritten freely`.

---

## 1 · Is the discriminator correct?

> **Does this artifact claim to describe the present?**

**Verdict: REFINED — correct in substance, under-specified in a way that makes it undecidable for
the artifacts this repository actually holds.**

It is right, and it is a real improvement over the test it replaces. On the case the review
question names it works exactly as claimed: `materialization_log.md:238` sits inside MAT-003 in a
log whose header reads *"Append-only. A record already written is never modified"*, so the artifact
describes a moment, the sentence is dated testimony, and the model protects it. Confirmed.

**The defect is that the question names no granularity, and the proposal answers it at two
different granularities in two different sections.**

- §2 asks it of the **artifact**: *"does this artifact claim to describe the present?"*
- §7 answers it per **field**, splitting one Agent Card into three classes — which is only
  possible if the question is asked of fields, not artifacts.

If the unit is the artifact, §7's split is out of model. If the unit is the field, §2's protection
of MAT-003 does not follow from the artifact being append-only — it has to be re-derived
sentence by sentence, and *"All are marked `status: PROPOSED`"* is written in the present tense and
would be at risk again.

This is not hypothetical. This repository holds artifacts that answer both ways at once:

| Artifact | As an artifact | Per entry |
|---|---|---|
| `dismissal_ledger_current.md` | header: *"non-canonical, **append-only**"*; name says `_current` | each dismissal is dated testimony with a `REVIVAL_TRIGGER` |
| `discovery_ledger_current.md`, `literature_tracking_log_current.md` | same shape | same |
| the receipt ledger | append-only, hash-chained | each receipt is testimony |
| the Agent Card | one file | three classes, per §7 |

An append-only ledger named `_current` is precisely the collision: the *set* is a present-tense
claim, each *entry* is testimony. Asked of the artifact, "does it describe the present?" returns
yes — and yes routes to TRANSITIONAL or DERIVED, whose remedies are *update in place* and
*recompute*. Applied to a dismissal ledger that is the worked example of the negatives discipline,
that licenses exactly the rewriting §2 exists to forbid, and it arrives through the front door
rather than through the test that was rejected.

**REQUIRED CHANGE 1.** Declare the unit the question is asked of, and state the rule for artifacts
that answer differently across their parts. The rule §7 already uses in practice is a good
candidate — *ask it of the smallest independently-writable unit; where one artifact yields more
than one answer, that is a signal to split it* — but it must be written, because it is the step
that decides whether testimony is protected.

```
VERDICT: REFINED
REFINED_FORMULATION: The discriminator is correct and its granularity is undeclared. It protects
                     dated testimony when asked of an append-only artifact, and does not
                     self-evidently do so for a present-tense sentence inside one, nor for a
                     ledger whose name claims the present.
WHAT_WOULD_CHANGE_MY_MIND: a granularity rule in §2 that classifies `dismissal_ledger_current.md`
                     as protected without relying on the reader knowing it is append-only.
```

---

## 2 · Are the four classes valid?

**Verdict: REFINED. No fifth class is required. The four are not a partition, because one of them
is defined on the other axis — which the proposal declares and then does not resolve.**

§3 states plainly that two axes are in play and that composing them yields four classes. It is
honest about the seam. But the resulting set mixes predicates:

- **STATIC** and **TRANSITIONAL** are defined semantically — by what the value claims.
- **DERIVED** is semantic *and* has a storage consequence (not stored).
- **EPHEMERAL** is defined by **storage** — *"untracked / gitignored"*, *"for this run only"*.

So a value can satisfy two classes at once. `CURRENT_SESSION_REF` claims to describe the present
and moves through states as sessions restart — semantically **transitional** — while being
untracked, hence **ephemeral**. The proposal classes it ephemeral and thereby drops the semantic
fact that it transitions.

The cost is visible in §5's rule for the class: *EPHEMERAL … "never cited as evidence."* That rule
was falsified during this bootstrap, four hours before the proposal was written. The L1 messaging
smoke verified my identity **by citing an ephemeral value**: the orchestrator's derived
`mirror-9c [3940a9]` was confirmed by the runtime's `from` on my reply, and the whole method
turned on treating that ephemeral observation as evidence — correctly, because it was an
observation of the runtime rather than an assertion by me.

**A fifth class is not the fix.** The fix is to stop treating the four as mutually exclusive:
declare the two axes independent, classify on the semantic axis, and let storage be a second
attribute. `SESSION_REF` is then *transitional · ephemeral*, which is both true statements instead
of one true and one lost.

**REQUIRED CHANGE 2.** Either state that the four classes are a partition and justify why
`SESSION_REF` is not transitional, or present the model as two attributes and drop the
"never cited as evidence" absolute, which is already contradicted by the L1 record.

---

## 3 · The transitional state model

`{ value, since_event, owner, next_review }`

**Verdict: REFINED. The shape is right and it is missing three things, one of which is the
mechanism that makes its own central claim true.**

**(3a) The checker is absent, and the proposal supplies the rule that condemns this.** §6 argues
the form's advantage is that it *"cannot go silently stale: the event pointer either resolves … or
it does not, and that is checkable by a script rather than by a reader's memory."* No such script
is proposed, and no existing validator resolves `since_event`. §7 states the governing principle
one page later, about carve-outs: **"a carve-out without its validator is an exemption wearing a
carve-out's name."** Applied to §6: a form whose value is checkability, shipped without the
checker, is a convention wearing a mechanism's name. Until a resolver exists, the four-field form
is better documentation with the same failure mode — a human must still notice.

**(3b) The closed set is asserted but never located.** *"value — the current state, from a closed
set."* Which set, declared where, and enforced by what? The repository already does this properly
one layer down: `LEGEND_CORE.md` fixes claim states as **exact strings** and the LINT blocks a
non-standard status. §6 neither cites that pattern nor says where a governance status's closed set
lives.

**(3c) `next_review` drops the forcing function of the ancestor it names.** §6 derives the field
from `PROVISIONAL_OPERATIONAL_PRACTICE` (E.3) — but E.3's expiry compels an explicit
`PROMOTE | REJECT | EXTEND_WITH_REASON`, and *"mai provisional per sempre."* §6's `next_review` is
only *"when the value must be re-examined"*, with no mandated act on arrival and no state for a
review that comes due and is not performed. That is a weakening of the mechanism it generalises,
and it reintroduces the exact failure the proposal is about: a date nobody is delinquent for
missing.

**Not missing, contrary to the review question:** ownership is handled well (§5's insight that the
seven statuses went stale because *no role was named, so no actor was late* is the strongest
paragraph in the document), and conflict resolution is arguably out of scope until a resolver
exists. Transition *rules* — the legal moves between values — are absent, and follow from (3b).

**REQUIRED CHANGE 3.** Name the validator that resolves `since_event` and the artifact that
declares each field's closed set, or state plainly that the form is documentation-only until both
exist. Restore E.3's forced action at `next_review`.

---

## 4 · The Agent Card split

**Verdict: REFINED — the split resolves C-9's *homelessness*, and two of its assignments are wrong
by the proposal's own definitions.**

The core insight is correct and is the proposal's best structural finding: the capability record
"kept finding new ground" because *"permanent or ephemeral?"* is a question it cannot answer. Two
of the three parts already have approved homes; I verified both.

**(4a) `ROLE_CONTRACT_HASH` is classed permanent/static. It is DERIVED.** It is computed from
`roles/<actor>.md`; when the contract legitimately changes, the hash must change. Under STATIC
rules the remedy is *"re-measure, then append a correction — never edit"*, which is the wrong
instrument: the right one is *recompute*. This session watched all four fingerprints move when a
single CORE artifact changed; a stored contract hash behaves the same way. Storing a derived value
under static handling is the precise defect the proposal was written to name.

**(4b) `STATUS` is classed EPHEMERAL in §7 and TRANSITIONAL in §5.** §7's field list ends
`CURRENT_SESSION_REF / CURRENT_SESSION_ID / STATUS / LAST_SEEN → ephemeral`. §5's transition-owner
table contains `ACTIVE ↔ DOWN in the roster | heartbeat timeout | orchestrator`. Both cannot hold:
either the roster status is ephemeral and has no transition owner, or it is transitional and
§7 misfiles it. J.2 makes the actor state machine normative, which settles it toward §5 — §7 is
the error.

**REQUIRED CHANGE 4.** Reclassify `ROLE_CONTRACT_HASH` as DERIVED (cacheable with its input
digest) and `STATUS` as TRANSITIONAL with the owner §5 already names.

---

## 5 · The capability ledger

`ledger/capabilities/<WRITER_ACTOR_ID>.jsonl`

**Verdict: writer-based naming is CONFIRMED and correctly derived from P7. Two consequences of the
path are unexamined.**

**Writer ownership is right, and the derivation is exact.** P7 reads: *"per-actor append-only event
file inside each actor's own worktree … PATH: `ledger/events/<ACTOR_ID>.jsonl` (in the actor's own
worktree)."* The one-writer property there is not produced by the filename — it is produced by the
file living in the tree of the actor that writes it, where the name and the writer coincide. A
file named for its *subject* keeps the shape and loses the precondition. Naming by writer restores
it, and the proposal's reason — that the filename should answer *who may write here* — is the
correct reading. Confirmed.

**(5a) For the orchestrator, "its own worktree" is the root checkout.** Capability promotion at L2
is the orchestrator's act, so `ledger/capabilities/orchestrator.jsonl` lives in root. `ledger/` is
tracked, so every append dirties the one tree GATE 0 requires clean. That is C-5's shape as a
standing condition rather than an incident: the mechanism would make root permanently dirty
between batches, in the tree where §14 calls one-writer critical and where C-7 is open. Not fatal —
appends can be committed with the batch — but the interaction is not addressed and it should be
before the path is fixed.

**(5b) No consolidator is named.** P7 pairs per-actor files with *"consolidated by Plan into a
derived canonical view"*, because N append-only files do not answer *what is this capability's
status now*. §7 proposes the writers and omits the reader. The Agent Card needs one answer per
capability; nothing produces it.

**(5c) The existing state-control home is not evaluated.** `framework/state/state_manifest_current.md`
is declared the single source of truth for state control and already carries live transitional
fields (`current_state: READY`, `batch_commit_gate: OPEN`). The gate the proposal invokes requires
*"adopt it or write down why you are diverging"*; the manifest is not mentioned. I do not think the
manifest is the right home — per-actor capability history wants an append-only ledger, not a
status file — but the divergence is exactly what §9's own standard says must be written down.

---

## 6 · Who writes a capability demotion

**Verdict: correctly left UNRESOLVED. The two options are not alternatives, and that is why it
looks unresolvable.**

I confirmed the gap in the source: Annex I.4 says *"una capability con fallimenti ripetuti torna
UNVERIFIED"* — intransitive, no writer — with `DETECTION: … → Mirror coordination review` and
`RECOVERY: retrocessione a UNVERIFIED`. Mirror is named as detector; the writer is named by nobody
in I.4, H.1 or G.2. The proposal's reading is exact.

**The authority implications, which the options as written obscure:**

Option A (*Orchestrator writes on Mirror's finding*) and Option B (*Mirror writes evidence,
Orchestrator consumes*) answer **different questions**. A answers *who writes the status*; B
answers *who writes the evidence*. Both records are needed, so the real choice is not A-or-B but
whether they are one record or two.

Taking A alone has a governance cost that is not visible in the framing: **Mirror's detection
would have no durable existence until another actor chose to write it.** By §18, what is not in
durable state did not happen — so under A, the evidentiary basis of Mirror's own metrics (G.3's
autonomy ledger and review yield derive from durable records) passes through the hands of the actor
whose patterns Mirror audits ex post. That is not an accusation of bad faith; it is the structural
reason AUTHOR ≠ REVIEWER exists, applied to the record rather than to the review.

Taking B alone has the cost the proposal names — a second writer, hence a second file — plus one it
does not: a demotion that exists only as Mirror evidence is not a status change, so an actor could
continue to be assigned on a capability Mirror has recorded as failing.

**Annex C.4 already partitions this**: `EVIDENCE → Scientist + Plan/provenance · INFERENCE → peer ·
SYSTEM → Mirror`. A capability failure is a SYSTEM observation, which is Mirror's. A capability
*status* is an assignment input, which is the orchestrator's, symmetric with promotion at L2. The
partition points to two records with one writer each — the shape §7's naming rule already supports.

**I do not resolve it, and the reason is not deference.** Deciding who may write a record that
constrains actors is governance, and H.1 gives governance to the operator. I record the analysis;
the decision is not mine, and an actor choosing it — including this one — would be the convenient
interpretation the proposal correctly refused.

---

## 7 · Does the proposal introduce unnecessary mechanisms?

**Verdict: CONFIRMED, with one gate omission.**

The proposal is unusually restrained. §9 finds four of five remedies already built and reduces its
own novelty to two elements. I checked the claim rather than accepting it: append-corrections,
`REVIVAL_TRIGGER` + re-audit, E.3 expiry, the tool-re-anchors rule, and variant 3 of
`PATTERN_ALREADY_SOLVED_GATE` all exist as cited. Nothing in §6 or §7 duplicates a mechanism that
is already present.

Two existing mechanisms are **not** cited, and under the gate's own wording each needs an adopt-or-
diverge line: the **state manifest** as the declared state-control home (§5c above), and
`LEGEND_CORE`'s **closed-set-of-exact-strings + LINT enforcement** as the existing answer to §6's
"from a closed set" (§3b above). Both are omissions of the shape the gate exists to catch —
a solution present in the repository, applied at one site, not carried to the second.

---

## VERDICT

```
R4 MIRROR REVIEW: REQUEST CHANGES

OBJECT   PROPOSAL-C9-STATE-MODEL.md @ f7a0049
REVIEWER mirror     DATE 2026-08-17     LEVEL R4 / MIRROR_REQUIRED
```

**BLOCKING FINDINGS**

| # | Finding | Where |
|---|---|---|
| **B-1** | The discriminator declares no granularity and is applied at artifact level in §2 and field level in §7. Append-only ledgers named `_current` answer both ways, and the artifact-level answer routes testimony to *update in place* | §2 / §7 |
| **B-2** | §6's central claim — that the form is script-checkable — ships without any resolver for `since_event`. The proposal's own rule applies: a mechanism without its validator is a convention wearing a mechanism's name | §6 |
| **B-3** | `ROLE_CONTRACT_HASH` classed permanent/static; it is DERIVED, and the classification prescribes the wrong remedy (append a correction, rather than recompute) | §7 |
| **B-4** | `STATUS` classed EPHEMERAL in §7 and TRANSITIONAL with owner in §5; J.2 settles it toward §5 | §5 / §7 |

**REQUIRED CHANGES** — RC-1 (granularity rule), RC-2 (partition or two attributes; drop the
"never cited as evidence" absolute), RC-3 (name the resolver and the closed-set home; restore
E.3's forced action at `next_review`), RC-4 (reclassify `ROLE_CONTRACT_HASH` and `STATUS`).

**NON-BLOCKING OBSERVATIONS**

- **N-1** The capability ledger for the orchestrator lands in the root checkout, making root
  dirty between batches — GATE 0's condition, C-5's shape as a standing state. Address before the
  path is fixed.
- **N-2** No consolidator is named for the per-actor capability files; P7 pairs writers with a
  Plan-built derived view.
- **N-3** Gate omission: the state manifest and `LEGEND_CORE`'s closed-set mechanism are not given
  adopt-or-diverge lines.
- **N-4** §6's four-field form is sound as documentation today; its advantage over prose is
  contingent on B-2.
- **N-5** §11 is verified exact in every measurable figure. Recorded as a positive: it is the
  first artifact in this bootstrap whose numbers survived independent re-measurement unchanged.

**WHAT THIS VERDICT IS NOT.** `REQUEST CHANGES` is not a judgement that the model is wrong. The
discriminator is right, the ownership insight of §5 is the sharpest thing in the document, the
writer-named ledger is correctly derived, and §10 is correctly refused. Four corrections are
needed, all local, and none of them touches the model's foundation. The proposal is closer to
adoption than a first draft of a state model has any right to be.

```
REVIEWER_CONFIDENCE:  HIGH on B-3 and B-4 (internal contradictions, mechanically checkable).
                      HIGH on B-2. MEDIUM-HIGH on B-1 — the granularity gap is certain, the
                      severity depends on whether an implementer would reach for the artifact or
                      the field, and both readings are in the document.
RESIDUAL_UNCERTAINTY: whether a fifth class is required cannot be settled from four worked cases;
                      I found none needed, which is weaker than none existing.
EVIDENCE_NEEDED:      for RC-3, the resolver's cost — if `since_event` can only be resolved by a
                      human following a pointer, the form should say so rather than claim
                      checkability.
WHAT_WOULD_CHANGE_MY_MIND:
                      B-1: a granularity rule already in the text that I read past.
                      B-3/B-4: a definition under which a stored hash is static, or under which
                      roster STATUS has no transition owner.
AUTHOR_RESPONSE:      PENDING_OPERATOR_ROUTING
```

**Scope observed.** Review only. No implementation, no governance modification, no file of the
proposal touched, L2 not attempted, the status/C-8 batch not unfrozen. No recommendation above is
an instruction to implement; RC-1…RC-4 identify what must be true for the model to be correct, not
how to build it.

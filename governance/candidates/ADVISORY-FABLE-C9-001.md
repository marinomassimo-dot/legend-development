---
artifact: ADVISORY REGISTER ENTRY
advisory_id: ADVISORY-FABLE-C9-001
object: Fable advisory on the C-9 identifier collision — binding-contract abstraction
origin: Fable, on the C-9 collision raised at REV-C9-STATE-MODEL-003
status: REVIEWED
outcome: MACRO_UPGRADE_CANDIDATE
reviewed_by: mirror — REV-C9-ADVISORY-FABLE-001, R4 / MIRROR_REQUIRED, verdict REQUEST CHANGES
registered_by: plan
registered_on: 2026-08-17
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1)
implementation: NONE — no trajectory below is built, scheduled or adopted
---

# ADVISORY-FABLE-C9-001 — register entry

Registered **separately from C-9** on the operator's direction. C-9 closed at revision 4 with a
one-clause patch (§2.1c); nothing from this advisory was folded into it beyond that clause, which
the C-9 review had prescribed independently.

**Why separate.** The binding-contract abstraction changes the unit of classification, adds a
declaration to every identifier and requires an enforcement layer. Folding it into a proposal four
revisions deep would have replaced a one-clause fix with a redesign, inside a document whose §0
disclaims exactly that. Under §17 a macro-upgrade is governed and typically MAJOR; this is one.

**Review status.** Mirror reviewed the advisory at R4 and returned `REQUEST CHANGES` with four
blocking findings (F-1…F-4) against the three contracts as written. `REVIEWED` here records that
the review happened and its disposition — **not** that the advisory's content is accepted. The
trajectories below carry the findings with them; none is cleared.

---

## Trajectory A — Binding Contract Model

```
origin:    evidence-driven
trigger:   C-9 collision
maturity:  candidate upgrade
```

**What it proposes.** That a role does not merely label a value but *constrains its admissible
behaviour* — C-9's §3 is a matrix whose empty cells read as *no normal case* rather than
*forbidden*, and the advisory names the difference. Its sharpest contribution is a reformulation
of what a violation is:

> *The violation is not the change itself. The violation is a transition without an event.*

That improves on C-9 §5 in a way worth preserving: C-9 makes staleness **attributable** by naming
a transition owner, so someone is delinquent. This makes it **detectable** — a state that moved
without a corresponding event is a machine-checkable condition — and detection beats attribution
because it does not depend on anyone noticing.

**Open findings, carried, not cleared.**

- **F-1** — `DERIVED` has no contract, and it is the one class with running enforcement. The scope
  against C-9's accepted §2.2 is undecidable from the advisory's text.
- **F-2** — *"each identifier declares its contract once"* is a pinned value that nothing
  validates, which `designed_for_growth.md` consequence 1 forbids by name.
- **F-3** — `TRACKED_TRANSITION`'s enforcement names a mechanism that does not exist, and its
  `LAST_SEEN` example reverses C-9 §7.2 and fails the thousandth-batch test.
- **F-4** — contracts 1 and 3 are not separated by the criterion said to generate them.

**What would move it forward**, from the review's `WHAT_WOULD_CHANGE_MY_MIND`: a fourth contract
for recomputed values or an explicit identifier-only scope (F-1); an event writer, or `LAST_SEEN`
removed from the examples (F-3); a criterion separating read-time refusal from write-once (F-4).

**Eligibility.** Not before the evidence-driven cycle has data. The freeze is explicit that an
upgrade must be fed by the autonomy ledger, review yield, dissent lifecycle and recovery events —
*"mai da ulteriore brainstorming architetturale"* — and an ontology project is precisely the
failure that clause exists to prevent.

---

## Trajectory B — Semantic Regression Detection

```
origin:    observed finding
trigger:   regression without diff
maturity:  research candidate
```

**What it observes.** That a change can invalidate an assertion in a file it never touched, so a
diff-scoped check cannot see it. This is the (B) shape of C-9 §1 with a detection question
attached, and the seven stale statuses are its worked example: no diff touched them, and every one
became false.

**🔴 The correction that changes what this trajectory is.** The advisory presents its mitigation —
*declared invariants at assertion level, verified globally at the commit gate, independent of
touched files* — as new. **The mechanism already exists and runs.** `legend_lint.py` is exactly a
whole-state structural validator: independent of which files a batch touched, consumed at the
commit gate, and already enforcing cross-artifact invariants — a claim in the working model absent
from the registry blocks the batch.

What does not exist is **coverage**. Verified independently at this registration:

```
grep -c "governance/"  framework/scripts/legend_lint.py   →  0
grep -c "roles/"       framework/scripts/legend_lint.py   →  0
```

So the gap is that the **governance corpus has no structural validator**, not that the shape must
be invented. Under `PATTERN_ALREADY_SOLVED_GATE` this is an *adopt-and-extend*, and framing it as
a new class of validation would build a second mechanism beside one that already works.

**That reframing shrinks the trajectory and raises its value**: extending an existing, gate-
consumed validator to `governance/` and `roles/` is a smaller change than a new validation layer,
and it would have caught the seven stale statuses, C-8, and the six false `pending` rows without
any of C-9's machinery.

**Eligibility.** After C-9's clauses are adopted, since the invariants a governance validator
would check are the ones C-9 defines. Building the checker before the rules exist would pin the
rules in code — F-2's own objection, one level up.

---

## Trajectory C — Agent-to-Agent Collaboration Protocol

```
origin:    operator direction
trigger:   multi-agent collaboration prototype
maturity:  design exploration
```

**What it addresses.** How agents collaborate when one may legitimately widen a problem beyond
what was asked. The v3.1.1 governance covers assignment, review, dissent and adjudication; it does
not describe an actor *contributing an unrequested reframing*, which is what produced this
advisory.

**Status.** Design exploration — the least mature of the three, and the one most exposed to the
freeze. It is registered because the operator directed it, and because the material it would
formalise was generated in the process of closing C-9 rather than by imagining requirements.

**Evidence it already has**, from this cycle: the process correction in Mirror's review inserting
operator ratification before materialization; the addressee guardrail carried inside the L1 ping;
and the practice, applied by three actors here, of verifying a peer's quotation rather than
accepting it.

---

## Governance note — this cycle as an instance

Recorded at the operator's direction, in the operator's formulation:

> *This Fable → Mirror → Fable cycle constitutes an operational example of the agent-collaboration
> principle: agents may widen the problem beyond the initial request, provided they clearly
> separate exploratory contributions, evidence, and binding decisions.*

The separation held here, and the artifacts show where each part landed. The **exploratory
contribution** is this advisory, registered as a candidate and adopted nowhere. The **evidence** is
in the reviews and in the two checks re-run at this registration — the collision reproduced by
C-9's own operational test, and the lint-coverage grep returning zero. The **binding decision** is
one clause, §2.1c, prescribed by a review and applied by the operator's closure directive.

The failure mode the separation prevents is visible in what did *not* happen: the advisory's two
best formulations were kept out of C-9 even though they would have improved it, because improving
a document is not the same as being in scope for it. Widening the problem is permitted; widening
the artifact under review is not.

---

## Disposition

```
ADVISORY-FABLE-C9-001
  status   REVIEWED
  outcome  MACRO_UPGRADE_CANDIDATE
  A · Binding Contract Model            evidence-driven   · C-9 collision                  · candidate upgrade
  B · Semantic Regression Detection     observed finding  · regression without diff        · research candidate
  C · Agent-to-Agent Collaboration      operator direction· multi-agent collab. prototype  · design exploration

IMPLEMENTATION  none
ADOPTED         nothing
F-1…F-4         open, carried with trajectory A
NEXT            evidence-driven cycle; no trajectory is scheduled by this registration
```

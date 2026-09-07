---
artifact: MIRROR hostile review of an advisory (Annex C.2)
review_id: REV-C9-ADVISORY-FABLE-001
object: Fable advisory on the C-9 identifier collision — binding-contract abstraction
origin: operator + Fable advisory
related: REV-C9-STATE-MODEL-003 (rev 3 @ f3bef29, REQUEST CHANGES, identifier collision)
reviewer: mirror
adjudicator: operator
level: R4 — METHOD / MIRROR_REQUIRED
review_date: 2026-08-17
verdict: REQUEST CHANGES
scope: conceptual review only — no implementation, no governance modification
---

# HOSTILE REVIEW — Fable advisory on the identifier collision

## STEELMAN

The advisory opens by declaring what it could not see — *"I am reasoning from the provided
extract, not from the complete §3 text"* — and asks to be recalibrated if the extract misled it.
It did, in one place, and in the advisory's favour: `BASE_HEAD × transitional` is **not**
expressible in rev 3, because §2.1b puts identifiers outside the semantic axis. But rev 3 *also*
places session refs inside that axis, which is precisely the collision I raised. So the critique
lands on the ambiguity rather than on the model as stated — it reached the right target from a
partial view, which is what the honesty premise was for.

Two contributions are real and better than what C-9 currently has.

**"The role constrains the admissible behaviour: it is not a free matrix, it is a constraint
function."** C-9's §3 is a matrix with `—` in the unpopulated cells, and `—` reads as *no normal
case*, not as *forbidden*. The advisory names something C-9 leaves implicit, and naming it is
worth more than the three contracts that follow.

**"The violation is not the change itself. The violation is a transition without an event."** This
is the sharpest sentence in the advisory and it improves on C-9's §5. C-9 makes staleness
*attributable* — a transition owner is named so someone is delinquent. The advisory makes it
**detectable** — a state that moved without a corresponding event is a machine-checkable
condition, and detection beats attribution because it does not depend on anyone noticing.

The scope warning is correct and important, and it is the same instruction the frozen text gives
itself: *"ogni upgrade di governance MUST essere evidence-driven … mai da ulteriore brainstorming
architetturale."* An ontology project is exactly the failure the freeze exists to prevent.

---

## 1 · Is the proposed abstraction correct?

**Direction: yes. Form as stated: no — four defects, three of which C-9 has already been through.**

Classifying the *binding* rather than the field is a genuine reframe and it dissolves the
"is a session ref a name or an assertion?" question I raised, by making the question *what
contract governs this binding?* — which is answerable without theory. That much is right.

The three contracts as written do not carry it.

---

## 2 · Does it introduce hidden complexity?

**Yes — and it is the opposite of the advertised property.** The pitch is *"the validator knows
three behaviours, not n×m combinations."* But the same paragraph says **"Each identifier declares
its contract once."**

The complexity is not removed. It is **relocated into n hand-written declarations**, one per
identifier, and nothing checks a declaration against the behaviour it claims. A matrix with
forbidden cells is at least derivable by a rule; a per-identifier declaration is an assertion, and
an assertion nobody validates is where this bootstrap has spent two days.

See F-2: this is not a stylistic objection, it is a rule this repository already has.

---

## 3 · Does it preserve the principles accepted in C-9?

**No, in two specific ways.**

- *"Do not classify the field"* directly displaces **§2.2 — the unit is the FIELD, scoped by its
  RECORD** — which was accepted at the R4 re-review and is byte-identical across rev 2 → rev 3.
  The advisory may intend to supplement §2.2 for identifier-valued fields only, but it is written
  as a replacement instruction, and the difference is not decidable from the text.
- The three contracts have **no home for DERIVED** (F-1), which is C-9's only class with running
  executable enforcement today.

---

## 4 · C-9 correction, or separate MACRO_UPGRADE candidate?

**Separate MACRO_UPGRADE candidate. It must not become the C-9 correction.**

The C-9 collision needs **one clause** — as REV-C9-STATE-MODEL-003 states: scope §2.1b to values
that *constitute* a binding, or say that names carry a storage class and relabel §3's cell. That
is a sentence in a proposal already three revisions deep and one finding from ACCEPT.

The binding-contract abstraction is a different and larger object: it changes the unit of
classification, adds a declaration to every identifier, and requires an enforcement layer. Folding
it into C-9 would replace a one-clause fix with a redesign, and would do so *inside* a proposal
whose §0 disclaims exactly that. Under §17 a macro-upgrade is governed, typically MAJOR, and this
is one.

**The semantic-regression finding is also a separate candidate — with a correction.** The advisory
says the mitigation is *"declared invariants at assertion level, verified globally at commit gate,
independent of touched files"*, and presents it as new. **The mechanism already exists and is
running**: `legend_lint.py` is precisely a whole-state structural validator, independent of which
files a batch touched, consumed at the commit gate, and it already enforces cross-artifact
invariants (a claim in the working model absent from the registry blocks the batch).

What does not exist is **coverage**: `legend_lint.py` contains **zero** references to `governance/`
or `roles/` — verified by grep. So the gap is that the governance corpus has no structural
validator, not that the shape has to be invented. Under `PATTERN_ALREADY_SOLVED_GATE` this is an
adopt-and-extend, and framing it as a new class of validation would build a second mechanism
beside one that already works.

---

## BLOCKING FINDINGS

### 🔴 F-1 · DERIVED has no contract, and it is the one class with running enforcement

Three contracts are offered as sufficient. A value that is **recomputed on demand** fits none of
them: it is not frozen, it emits no transition event, and it is not testimony. The four role
fingerprints, `candidate_content_hash` as computed by the script, `growth_anchors.py`'s counts and
every LINT verdict are exactly this.

This matters more than a taxonomy gap because DERIVED is where C-9's discipline is *already
executable*: `governance_fingerprint.py`, `candidate_content_hash.py` and `growth_anchors.py` run
today and enforce *never store what can be computed / the tool that causes the change re-anchors
it*. An abstraction that supersedes C-9's classification and omits DERIVED loses the only part of
the model that currently bites.

**What must be true:** either a fourth contract for recomputed values, or an explicit statement
that the three contracts govern **identifier bindings only** and leave C-9's semantic axis intact
for everything else. The second is smaller and I expect it is what was meant — but it is not what
is written, and §3's answer above depends on which it is.

### 🔴 F-2 · "Each identifier declares its contract once" is a pinned value, which this repository forbids by name

`designed_for_growth.md` consequence 1: *"Never pin a number a human must remember to update. The
change must be re-anchored by the tool that causes it … updating a constraint must cost at least
as much as complying with it."*

A declared contract is that pin, in a worse form than a number: if an identifier's real behaviour
changes — a value that was frozen becomes recomputed, a runtime relationship becomes persistent —
the declaration does not move, and **nothing compares the declaration to the behaviour.** The
system would hold a corpus of contract declarations that are true when written and silently
falsified by later change.

That is branch (B) of C-9's own problem statement, reintroduced by the mechanism proposed to close
branch (A). The advisory's enforcement column is where this shows: `FROZEN_BINDING` cites *"already
existing"* gates, which is right; the other two cite mechanisms that must be built, and neither
cites anything that validates the declaration itself.

**What must be true:** the contract must be derivable from something observable, or the declaration
must be checked against behaviour by a validator that exists. A third option — accept that it is a
declaration and say so — is honest but forfeits the pitch of F-2's own paragraph.

### 🔴 F-3 · TRACKED_TRANSITION's enforcement names a mechanism that does not exist, and its examples reverse an accepted C-9 decision

*"Change means: a legal transition, but it must generate an event (Annex J) with previous value
preserved. … The violation is a transition without an event."*

**The Annex J event writer does not exist.** `ledger/events/` is not present in the tree, and P7
records it as *"design chosen; writer and validator not yet built"* — it is listed in
`PENDING_IMPLEMENTATION`. Under this contract every session-ref change is a violation from day
zero, because no event can be emitted. This is the same class as C-9 rev 1's B-2 — a capability
asserted into existence — which was blocked, and it should be blocked here for the same reason.

**Two further consequences of the examples given.**

`LAST_SEEN` is offered as a `TRACKED_TRANSITION`. C-9's accepted §7.2 places it in the **untracked
cell**, in the gitignored `local_instance.md`, and I.5's reason is not convenience — it is that the
tracked half must survive the clone-and-run test and must not carry machine identity. Promoting
`LAST_SEEN` to a tracked, event-emitting binding reverses an accepted decision and re-imports what
I.5 excluded.

And it fails the growth test the repository requires every control to answer. `LAST_SEEN` moves at
`HEARTBEAT_CADENCE: 30 minutes`, per actor. Six actors produce roughly 288 events a day whose
entire content is *an actor was still alive*. At the thousandth batch the event ledger — Mirror's
declared primary analysis surface under G.3 — is majority heartbeat noise. *Will this still be
informative at the thousandth batch?* For this binding, no.

### 🔴 F-4 · Contracts 1 and 3 are not separated by the criterion that is said to generate them

The stated classifier is *"the mutability contract of its binding"*. Test it:

| | Binding | Mutable? |
|---|---|---|
| `FROZEN_BINDING` — `BASE_HEAD` → a commit | immutable for the declaring object's lifetime | **no** |
| `APPEND_ONLY_RECORD` — `CHK-plan-0008` → a checkpoint | immutable, permanently | **no** |

Both are immutable, so the stated criterion cannot tell them apart. What actually separates them is
**where enforcement sits** — a precondition check at *read* time versus write-once at *write* time
— and that is a property of how the value is consulted, not of the binding's mutability.

The distinction is real and operationally useful; the rule offered does not produce it. A validator
built from the stated criterion would have to fall back on the examples, which is the per-case
judgement the abstraction was introduced to remove.

---

## ON THE PROCESS RECOMMENDATION — an authority correction

The sequence reads: `Fable advisory → Mirror hostile review → **If accepted** → Plan materializes`.

**Mirror's acceptance is not an authorization to materialize.** H.1 gives governance to the
operator; a C-9 correction touching `plan_defined_parameters.md` or a role contract is MAJOR under
body §12 and requires `HUMAN_APPROVAL` with a durable queue object under J.3. My verdict on an
advisory is an input to that decision and never a substitute for it. The sequence should read
`… → Mirror hostile review → operator ratification → Plan materializes`.

I raise this even though nothing here is being materialized, because a process diagram is the
artifact people follow when they are not reading the annexes.

---

## VERDICT

```
MIRROR HOSTILE REVIEW (advisory): REQUEST CHANGES

OBJECT    Fable advisory — binding-contract abstraction for the C-9 identifier collision
REVIEWER  mirror     DATE 2026-08-17     LEVEL R4 / MIRROR_REQUIRED

BLOCKING  F-1  DERIVED has no contract; scope vs accepted §2.2 undecidable from the text
          F-2  "declares its contract once" is a pin that nothing validates — consequence 1
          F-3  TRACKED_TRANSITION's enforcement does not exist; LAST_SEEN reverses §7.2 and
               fails the thousandth-batch test
          F-4  contracts 1 and 3 are not separated by the stated criterion

DISPOSITION OF THE PARTS
  · the C-9 correction stays ONE CLAUSE — do not fold this abstraction into it
  · binding contracts → separate MACRO_UPGRADE candidate, governed, evidence-driven
  · semantic-regression validation → separate MACRO_UPGRADE candidate, corrected: the
    mechanism exists (legend_lint.py, whole-state, gate-consumed); the gap is that it has
    zero coverage of governance/ and roles/
  · process sequence → insert operator ratification before materialization
```

Two things in the advisory should survive whatever happens to the three contracts: *the role
constrains admissible behaviour rather than composing freely*, and *the violation is a transition
without an event*. The second is a better formulation than C-9 currently carries and belongs in
the macro-upgrade candidate on its own merits.

```
REVIEWER_CONFIDENCE:  HIGH on F-1, F-3, F-4 — each verified against the tree or against accepted
                      C-9 text. HIGH on F-2 as a rule citation; MEDIUM on how much it bites, since
                      a declaration checked at review time is weaker than a pin but not nothing.
RESIDUAL_UNCERTAINTY: whether the advisory intends to supplement C-9 or replace its unit. My
                      findings are stated for the replacement reading, which is what the text says;
                      under the supplement reading F-1 and part of §3 above soften considerably.
EVIDENCE_NEEDED:      a scope statement from the author would resolve more of this than any
                      further analysis by me.
WHAT_WOULD_CHANGE_MY_MIND:
                      F-1: a fourth contract for recomputed values, or an explicit identifier-only
                      scope. F-3: an event writer, or LAST_SEEN removed from the examples.
                      F-4: a criterion that separates read-time refusal from write-once.
AUTHOR_RESPONSE:      PENDING_OPERATOR_ROUTING
```

**Scope observed.** Conceptual review only. No implementation, no governance modification, no C-9
file touched, no decision taken on any part — every disposition above is a recommendation to the
operator under H.1.

---
artifact: PROPOSAL C-9 — how LEGEND represents state
proposal_id: C9-STATE-MODEL
revision: 3
task_id: C9-STATE-MODEL-001
author: plan
authored_on: 2026-08-17
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1), so this
  file modifies no content-domain artifact, no candidate content hash and no role fingerprint
lineage:
  - rev 1 @ f7a0049 — R4 returned REQUEST CHANGES (B-1…B-4, notes 1–4)
  - rev 2 @ 6c2ab4f — R4 re-review returned REQUEST CHANGES; §2.2, §3, §6.1, §7 and §10 ACCEPTED;
    two clauses blocking (hash rule too strong; "never cited as evidence" incorrect)
  - rev 3 @ f3bef29 — revised the two blocking clauses; R4 returned REQUEST CHANGES on one
    finding, the identifier collision (REV-C9-STATE-MODEL-003)
  - rev 4 @ this commit — CLOSING PATCH: §2.1c, one clause, per that review's first exit
status: ACCEPTED
status_since_event: operator closure directive, 2026-08-17
status_transition_owner: operator
status_next_review: at the first governed change that adopts any clause of this proposal
acceptance_is_not_adoption: true
hold: no implementation and no governance modification until that review completes; L2 suspended;
  the status/C-8 batch frozen pending a later operator decision
---

# PROPOSAL C-9 — static, derived and transitional state · revision 3

> **Lineage note.** Revision 1 returned `REQUEST CHANGES` with four blocking findings; revision 2
> answered them and returned `REQUEST CHANGES` with two. The review states the model does not
> require redesign and accepts §2.2, §3, §6.1, §7 and §10. **This revision touches only the two
> blocking clauses and the sections they force.** Accepted text is preserved verbatim.
>
> Both remaining findings are the same failure at one more level of generality: revision 2 fixed
> a per-field judgement by promoting it to a universal rule, and each universal rule turned out to
> have a counterexample sitting in this repository. **A rule stated more strongly than its
> evidence is an (a1) assertion — untested — wearing the clothes of a principle.** That is
> recorded as instances 11 and 12 rather than smoothed over.

## 0 · What this proposes, and what it does not

It proposes **a classification, a unit of classification, and an ownership map**: a question that
sorts any recorded value, an explicit statement of *what* gets sorted, and a rule naming who may
write each class. It proposes almost no new machinery — three of the four remedies already exist
in this repository.

It does **not** implement anything, does not modify governance, does not adopt itself, and does
not repair the live defects it uses as examples. Adoption requires a governed change to
content-domain artifacts and, for the parts touching `plan_defined_parameters.md` or a role
contract, a fingerprint rotation.

---

## 1 · The problem, as observed

Two shapes were measured during the v3.1.1 bootstrap. They look identical in a diff and have
opposite remedies.

**(A) STATE ERROR — the value was wrong when written.** Remedy: verification before assertion.
Mirror split this, and the halves differ:

- **(a1)** the assertion was never tested → test before asserting.
- **(a2)** a test ran, passed, and could not discriminate → show the test can fail.

(a2) is the worse half: it leaves a green result behind.

**(B) STALE TRANSITION STATE — the value was correct when written and was invalidated by a
transition the system itself performed.** Remedy: the transition carries the update. Human memory
is not a mechanism.

---

## 2 · The discriminator, and the unit it applies to · **[B-1]**

### 2.1 · The question

The obvious test is *"is this statement currently false?"* **That test is wrong.** It flags
`governance/design_records/materialization_log.md:238` — a sentence inside MAT-003 reading *"All
are marked `status: PROPOSED`…"* — which was **true on 2026-08-16 when written**, sits in an
append-only log, and is dated testimony. A model that cannot tell that from a stale status field
licenses rewriting history, which is more expensive than any stale field.

The question one step earlier:

> ### Does this assertion claim to describe the present?

*(The question is the orchestrator's. The test it replaced was mine.)*

### 2.1b · A prior question — is this an assertion at all? · **[BLOCKING-1]**

The question above presupposes the value **asserts** something about state. Not every recorded
value does. `BASE_HEAD: 749a9a9b…` does not claim that something *is* or *was* the case: it
**names an object**. A name is not an assertion, and asking a name whether it describes the
present is a category error — which is how revision 2 produced a rule that swallowed the
identifiers the gates depend on.

So the classifier begins one step further back:

> ### 1. Is this a NAME or an ASSERTION?
> ### 2. If an assertion — does it claim to describe the present?

**The operational test**, which needs no theory: *if this value changed, would you say "the
measurement was wrong" or "that is a different object"?*

- *the measurement was wrong* → an **assertion**; continue to question 2
- *that is a different object* → a **NAME**; continue to the scoping clause below

### 2.1c · A name leaves the axis only if something is BOUND to it · **[the one clause]**

The test above is necessary and not sufficient. It returns *"a different object"* for both
`BASE_HEAD` and `CURRENT_SESSION_REF` — a session restart genuinely produces a different session —
while the model needs the two in different places. Revision 3 put every name outside the semantic
axis, which would have given a session ref a transition owner and a review date. That is not a
taxonomy blemish; it is a wrong action.

> **A name sits outside the axis only when something is bound to it.**
>
> A **binding name** is one that an approval, a gate or a freeze cites, such that a different
> value produces **refusal rather than update**. It is an `IDENTIFIER` (§4.1, role B).
>
> A name that binds nothing is not an identifier in this sense. When it changes, nothing refuses —
> the new value is simply the current one — so it remains an assertion about the present and is
> classified by §3 like any other.

The second half of the test, therefore: *and does anything refuse when it changes?*

| Value | Different object? | Anything refuses? | Result |
|---|---|---|---|
| `BASE_HEAD` | yes | yes — gate 5 | **IDENTIFIER**, outside the axis |
| `CANDIDATE_CONTENT_HASH` bound in an approval | yes | yes — gate 5 | **IDENTIFIER** |
| `PRIOR_ART_*_SHA256` | yes | yes — `BYTE_IDENTITY` | **IDENTIFIER** |
| `CURRENT_SESSION_REF` | yes | **no** | assertion → `TRANSITIONAL × UNTRACKED` (§3), **no owner, no review date** |

*(The collision, the operational test that exposes it, and the wrong-action consequence are
Mirror's, at the R4 review of revision 3. The scoping clause is the first of the two exits that
review offered.)*

`BASE_HEAD` fails the first and passes the second: a different value there does not mean the base
was mis-measured, it means the candidate is bound to a different commit. That is precisely what
GATE 5 exists to detect, and it is why identifiers must be immutable rather than correctable.

**Identifiers do not enter the semantic axis of §3.** That axis classifies assertions about state;
a name has no temporal claim to classify. This is stated as an addition *before* §3 rather than as
a fourth class *inside* it, so the section the review accepted stands unamended.

### 2.2 · The unit is the FIELD, scoped by its RECORD · **[B-1]**

Revision 1 asked the question of an *artifact* in §2 and of *fields* in §7. Mirror is right that
this is ambiguous, and right about the example that breaks it.

**The unit of classification is the field** — the smallest recorded assertion. **A field inherits
the temporal scope of the record that encloses it.** Three levels, and only two of them classify:

| Level | Role in classification |
|---|---|
| **Artifact** | **none.** A container. Its name is not evidence about its contents |
| **Record** | supplies **temporal scope**. A dated, append-only record binds every field inside it to that date |
| **Field** | **the unit.** Each field is classified individually |

So a field that reads as live is STATIC when its record is dated, because the record says *at time
T* over everything it contains.

**The worked case Mirror supplied.** `disease-models/wwox/research/dismissal_ledger_current.md`
carries `_current` in its name and holds eleven dated `REVIVAL_TRIGGER` entries. Under revision 1
the artifact-level question gave the wrong answer twice over: the name claims the present, the
entries do not. Under this revision the artifact classifies nothing, each entry is a dated record,
and every field inside an entry is STATIC — protected, unrewritable, exactly as the append-only
discipline requires. The `REVIVAL_TRIGGER` itself is not an exception: it is a **standing
condition recorded at time T**, not a claim about now, which is why firing it produces a *new*
record rather than an edit to the old one.

**A consequence worth stating because it contradicts a naming convention in force.** The `_current`
suffix marks the canonical file of a kind; it does **not** assert that every field inside claims
the present. `dismissal_ledger_current.md` and `claim_registry_current.md` are living containers
of dated records. The suffix is an addressing convention, not a temporal one, and any classifier —
human or scripted — that reads it as temporal will misclassify the ledgers first.

**Artifact-level shorthand** remains legitimate in exactly one case: when every field in an
artifact shares a class, the artifact may be labelled for convenience. `roles/plan.md` is not such
a case — it carries a STATIC role definition and a TRANSITIONAL status field, which is why C-8
could go stale inside an otherwise stable document.

---

## 3 · Two axes, not one partition · **[note 1]**

Revision 1 presented four classes as a single partition, which hid that they sit on different
axes. Mirror is right, and the reconciliation removes the fourth class rather than adding a fifth.

**Semantic axis** — what the assertion claims: `STATIC` · `DERIVED` · `TRANSITIONAL`.
**Storage axis** — where it may live: `TRACKED` · `COMPUTED` · `UNTRACKED`.

|  | TRACKED | COMPUTED | UNTRACKED |
|---|---|---|---|
| **STATIC** | dated records, ledgers, commits — *the normal case* | — | — |
| **DERIVED** | cached **with its input digest** — rare, and a smell | on demand — *the normal case* | — |
| **TRANSITIONAL** | governed statuses, the roster, capability status — *the normal case* | — | session refs, liveness — *the "ephemeral" cell* |

**`EPHEMERAL` is not a semantic class.** It is `TRANSITIONAL × UNTRACKED` — a storage decision
applied to a transitional value. That is why revision 1 could not place the capability record:
*"permanent or ephemeral?"* is a malformed question, mixing one axis's value with the other's.

**When is a transitional value untracked?** Both conditions, together: it has no meaning after the
run that produced it, **and** persisting it would leak machine or session identity. That second
condition is not incidental — it is `I.5`'s stated reason for `deployment/local_instance.md` being
gitignored, and it is why a session ref is untracked while a roster state is not.

---

## 4 · Historical event vs current derived state · **[requirement 1, B-3]**

Both are true; they differ in what they are true **about**.

| | Historical event | Current derived state |
|---|---|---|
| Asserts | this happened, then | this holds, now, by rule |
| Record carries | a **timestamp of assertion** | a **recipe** |
| Goes stale? | never — the moment does not move | never — it is recomputed |
| Remedy when wrong | re-measure, then **append** a correction | recompute |

### 4.1 · A hash is not a class. The semantic ROLE decides. · **[B-3, BLOCKING-1]**

Revision 1 classified `ROLE_CONTRACT_HASH` as STATIC, which was wrong. Revision 2 corrected it
with *"a hash is never STATIC; the value is DERIVED"* — **which is also wrong, and more
dangerously**, because it is general enough to swallow the anchors the gates depend on.
`BASE_HEAD`, `BRANCH_TIP` and the `PRIOR_ART_*_SHA256` pair are not measurements awaiting
recomputation. They are identities, and `P5` says why in its own words: BASE_HEAD is folded in
*"so an approval cannot be transplanted onto a different base"*.

**A hash has no class of its own.** The same 64 hex characters carry three different roles, and
the role decides:

| Role | The question it answers | Class | If the value differs |
|---|---|---|---|
| **A · DERIVED MEASUREMENT** | *what does this mutable input hash to now?* | DERIVED | the measurement was wrong or the input moved → **recompute** |
| **B · IMMUTABLE IDENTIFIER** | *which object?* | **IDENTIFIER** — outside the temporal axis (§2.1b) | you are naming a **different object**. There is nothing to correct; a gate must **refuse**, not reconcile |
| **C · HISTORICAL RECORD of either** | *what was it, then?* | STATIC | append a correction; never edit |

Applied to the values in force:

| Value | Role | Why |
|---|---|---|
| `shasum -a 256 roles/plan.md` run today | A | asks what a mutable file hashes to now |
| `ROLE_CONTRACT_HASH` inside `CHK-plan-0006` | B, and C by being recorded | names which contract version the checkpoint was taken under; a different value means a different contract, not a mis-measurement |
| `BASE_HEAD 749a9a9b…` | **B** | GATE 5 binds to it precisely so it cannot move |
| `BRANCH_TIP 9720a0cd…` | **B** | names the tree the domain was taken over |
| `PRIOR_ART_SOURCE_SHA256` / `..._ARCHIVED_SHA256` | **B** | their whole purpose is an identity comparison — `BYTE_IDENTITY: PASS` asserts the two names denote the same bytes |
| `CANDIDATE_CONTENT_HASH` as computed by the script | A | a measurement over a tree, by a published recipe |
| `CANDIDATE_CONTENT_HASH` as bound in an approval | **B** | the approval names *that* content; a different value is a different candidate, which is what gate 5 detects |
| any of the above inside a commit message or checkpoint | C | dated testimony |

**The strongest kind of identifier is one that is also derivable**, and this is not a curiosity —
it is why RC-1 mattered. `CANDIDATE_CONTENT_HASH` is role B when a gate binds to it and role A
when the script computes it, so the binding can be **re-verified** rather than merely compared.
An identifier that cannot be recomputed — a session ref, a UUID — can only be compared against a
record of itself, which is why §5.2's observation rule exists.

**Storage rule that follows:** a role-A value must not be stored without its recipe beside it.
That is why the manifest publishes the reproduction command and why the entry count was removed
rather than corrected (RC-3). A role-B value *must* be stored — that is what an anchor is for.

**What revision 2 got right and should be kept:** the failure that produced it. §4 of revision 1
drew the historical-versus-current distinction for one hash and failed to carry it one section
later to another. Uneven application inside the document proposing to cure uneven application —
not by forgetting the rule, but by recognising the shape and stopping there
(`designed_for_growth.md` consequence 5). Revision 2 then over-corrected into a universal, which
is the same error with the sign flipped: a per-case judgement replaced by a rule that was never
tested against `BASE_HEAD`.

### 4.2 · Instrumentation rider

A derived value is only as good as the observation that produced it, and observation is where this
bootstrap failed nine times (§11). **A derived value must record the command that produced it, in
a form a reader can re-run without reconstructing a pipeline** — the command, not its output.

---

## 5 · Ownership of the writer, per class · **[requirement 2]**

**A transitional field with no named transition owner has nobody who is delinquent when it stops
being true.** The seven stale statuses went stale because no role was named, not because no
mechanism existed.

| Class | Writer | Constraint |
|---|---|---|
| **STATIC** | the actor that witnessed it | never edited by anyone, its author included. A correction is a **new record** naming what it supersedes |
| **DERIVED** | the tool | *the tool that causes the change re-anchors it.* No hand-written derived values; a cache is written by the computing tool and carries its input digest |
| **TRANSITIONAL** | the actor whose act causes the transition | named **in the field itself** |
| *(untracked cell)* | whoever holds the runtime | free to rewrite; never tracked; never **stored** as durable state — but see §5.2, an *observation of* it may be evidence |

### 5.2 · Durability of a value ≠ admissibility of an observation · **[BLOCKING-2]**

Revision 2 said an untracked value is *"never cited as evidence"*. **That is wrong**, and the
counterexample is this bootstrap's own L1 smoke test.

The load-bearing item in L1 was the `from` attribute the runtime placed on an incoming message —
untracked, ephemeral, gone when the session ends. It was nevertheless **valid evidence**, and it
was the only thing that could confirm a derived `SESSION_REF` by observation rather than by
inference. Under revision 2's clause, the one test that closed L1 would have been inadmissible.

The clause conflated two different properties:

| | Untracked **value** | **Observation of** an untracked value |
|---|---|---|
| may become durable state | **no** | — |
| may be persistent configuration | **no** | — |
| may be evidence | — | **yes**, under the conditions below |
| what is durable | nothing | the **observation record** |
| its class | TRANSITIONAL × UNTRACKED | **STATIC** — dated testimony (§2.2) |

**The boundary.** An untracked value cannot become durable state or be treated as configuration.
An *observation* of it becomes durable through the observation record, and that record is STATIC:
it asserts *at time T, observer O saw V*, which remains true forever regardless of what the value
does next.

**Conditions on the observation**, higher than for a re-checkable value, because nobody can go
back and look:

- **an authorised observer** — someone whose role places them where the value was visible. In L1
  the receiving actor was the only party who could see the `from` the runtime supplied;
- **verbatim** — the value as received, not as paraphrased or as the sender's envelope claimed it.
  Quoting the sender's own assertion back would have confirmed nothing, which is why the protocol
  asked the receiver to quote the runtime's attribute;
- **attributed and dated** — observer and moment, since the observation cannot be repeated;
- **the instrument named** — §4.2's rider applies with more force here: an unrepeatable
  observation taken through an unnamed pipeline cannot be distinguished later from instance 7.

**This is the model classifying its own machinery correctly:** the value is
TRANSITIONAL × UNTRACKED, the record about it is STATIC, and revision 2's error was assigning the
record the class of the value.

### 5.1 · Transition owners in force today

| Field | Transition | Owner |
|---|---|---|
| `status: PROPOSED → BINDING` on a governed artifact | Mirror review passes **and** operator approves | **operator**; Plan transcribes on the event |
| `STATE: PENDING → APPROVED` in the approval queue | operator resolves | **operator** |
| actor lifecycle state (J.2) | heartbeat, timeout, rotation, operator pause | **orchestrator** |
| capability `UNVERIFIED → VERIFIED` | L2 smoke passes | **orchestrator** |
| capability `VERIFIED → UNVERIFIED` | repeated failures | **two writers — see §10** |
| a governance rejection whose premise expires | the premise is falsified | the actor producing the datum, via re-audit |

---

## 6 · Lifecycle of transitional statuses · **[requirement 3, B-2]**

Every transitional field carries four things:

```
{ value, since_event, owner, next_review }
```

- **value** — from a **declared closed set** (§9.2)
- **since_event** — the durable event that set it; a resolvable pointer, never prose
- **owner** — who performs the next transition (§5)
- **next_review** — when the value is re-examined even if no event fires

`next_review` is what stops a transitional value becoming permanent by neglect, and it is not new:
`PROVISIONAL_OPERATIONAL_PRACTICE` (Annex E.3) already carries expiry with a forced
`PROMOTE | REJECT | EXTEND_WITH_REASON`, and the four PROVISIONAL parameters in
`plan_defined_parameters.md` already use it.

### 6.1 · The resolver contract — a requirement, not an existing capability · **[B-2]**

Revision 1 claimed `since_event` made a status *"checkable by a script rather than by a reader's
memory"*. **No such resolver exists.** Mirror is right that this asserted a capability into being.
The claim is withdrawn and replaced by a contract the model requires and does not supply:

```
RESOLVER CONTRACT — minimum

  input    (artifact, field, value, since_event)
  locate   since_event by identifier, in a declared durable location
  return   CONFIRMS | CONTRADICTS | UNRESOLVABLE

  fail-closed : UNRESOLVABLE is a failure, never a pass
  no prose    : an event is a record with an identifier, not a sentence describing one
  no self-ref : a field may not cite itself, nor an event that exists only in the artifact
                carrying the field
```

Until such a resolver exists, the four-field form buys **auditability by hand** — a reader can
follow the pointer — and not verification. That is still an improvement over prose, and it is a
smaller claim than revision 1 made.

**Worked example**, current form and proposed form:

```
status: PROPOSED — binding once Mirror hostile review passes and the operator approves

status: BINDING
status_since_event: RES-20260816-GOV311-001
status_transition_owner: operator
status_next_review: on the next MAJOR governance change
```

---

## 7 · Permanent / derived / ephemeral, applied · **[requirement 4, B-4, note 2]**

### 7.1 · The Agent Card is three state machines, and `STATUS` named none of them · **[B-4]**

Revision 1 put `STATUS` in the transitional list in §5 and in the ephemeral list in §7. Mirror is
right: that is a contradiction, and it comes from one field name covering three different state
machines. **They must not be merged.**

| Machine | Values | Class | Owner |
|---|---|---|---|
| **actor lifecycle** | `BOOTSTRAPPING · ACTIVE · IDLE · RUNNING · BLOCKED · AWAITING_APPROVAL · DEGRADED · DOWN · PAUSED · RETIRED` (J.2, verbatim) | TRANSITIONAL × TRACKED | orchestrator |
| **session liveness** | whether *this* session is reachable now | TRANSITIONAL × UNTRACKED | the runtime holder |
| **capability verification** | `VERIFIED · UNVERIFIED` per capability (I.4) | TRANSITIONAL × TRACKED | orchestrator at L2; demotion §10 |

Proposed: `STATUS` is retired as a field name and replaced by `lifecycle_state`,
`session_liveness` and per-capability `status`. A field whose name does not say which machine it
belongs to will be written by whoever reads it as theirs.

The lab machine (`BOOTSTRAP · OPERATIONAL · ORPHAN · SUSPENDED`) is a fourth, and it belongs to
the laboratory rather than to any actor's card.

### 7.2 · Two of the three halves already have homes

```
ACTOR_ID / ROLE / WORKTREE / ROLE_CONTRACT              → STATIC, tracked  → deployment_profile.md
ROLE_CONTRACT_HASH                                       → DERIVED (§4.1)  → computed, not stored
CAPABILITIES [{capability, status, last_verified}]       → TRANSITIONAL    → §7.3
CURRENT_SESSION_REF / SESSION_ID / liveness / LAST_SEEN  → untracked cell  → local_instance.md
```

`deployment/deployment_profile.md` already states its portable half carries *"the actor
definitions"* and tabulates ACTOR_ID → worktree → contract for all six actors; its local half
already declares `SESSION_REFS ... ephemeral, rewritten freely`. **The third home was not one
artifact needing relocation. It was one artifact that should never have been single** — which is
why it kept finding new ground: nothing owned it because two things already did.

### 7.3 · The capability ledger — writer-named, with consolidation · **[note 2]**

```
ledger/capabilities/<WRITER_ACTOR_ID>.jsonl     append-only, one writer per file
  { subject_actor_id, capability, status, evidence, since_event, at }

ledger/capabilities/consolidated/               derived view, rebuilt by replay, never hand-edited
                                                consolidated by Plan
```

Named by its **writer**, not its subject: P7's one-writer property comes from *an actor owning the
file in its own worktree*, and a file named `<subject>.jsonl` written by neither the subject nor
the tree's owner borrows the shape and drops the precondition.

**Consolidation was missing in revision 1 and Mirror is right that P7 pairs the two.** A per-writer
set without a consolidated view answers *what did this writer attest* and never *what is this
actor's current capability* — which is the question Orchestrator must answer before assigning. The
view is derived (§3): rebuilt by replay, never edited, and by §4.2 it records the command that
built it.

**The root-cleanliness constraint, which revision 1 did not consider** — Mirror's note. The
Orchestrator's working directory *is* the root checkout, and GATE 0 requires **root clean**. An
uncommitted append to `ledger/capabilities/orchestrator.jsonl` therefore makes the root dirty and
blocks every canonical batch until it is committed. So the append-only carve-out must permit
**committing that path immediately, outside a `BATCH_COMMIT`** — which is exactly the existing
shape: `fulltext_receipts.py record` appends *and* re-anchors in one act, and the state manifest
already designates such ledgers as carve-outs. This is a requirement on the carve-out, not a new
mechanism, and it is the reason the carve-out must be **validated**: the receipt ledger's is a
permission *plus* a validator the LINT consumes. A carve-out without its validator is an exemption
wearing a carve-out's name.

Freeze policy: `FREEZE_SCOPE_GATE` tier 2 — prefix length + prefix digest, so growth is legal and
only rewriting the frozen prefix is a violation.

---

## 8 · Applied to every live case

| Case | Class | Remedy | Held? |
|---|---|---|---|
| Seven `status: PROPOSED` on governed artifacts | TRANSITIONAL × TRACKED | §6 four-field form; owner operator; event `RES-20260816-GOV311-001` | yes |
| `claude_md_migration_map.md` front matter | same | same | yes |
| Six of ten `pending` rows in `ANNEX_INDEX` | should be **DERIVED** | *does this artifact exist?* is a question a script answers | yes |
| The `held` row in `ANNEX_INDEX` | a **rejection with an expired premise** | `epistemic_discipline` §2 — `REVIVAL_TRIGGER` + re-audit, never carried to a governance rejection | yes |
| `materialization_log.md:238` | **STATIC** — dated testimony, field scoped by its record (§2.2) | 🔴 **none. Do not touch.** A new record, never an edit | must remain |
| Every `REVIVAL_TRIGGER` in the dismissal ledger | **STATIC** — standing condition recorded at time T | firing it produces a new record | must remain |
| C-8, the stale capability line in `roles/plan.md` | TRANSITIONAL | §6 form; owner orchestrator at L2 | yes |
| `ROLE_CONTRACT_HASH` computed today | **role A — DERIVED** (§4.1) | recompute | yes |
| `BASE_HEAD`, `BRANCH_TIP`, `PRIOR_ART_*_SHA256`, an approval's bound hash | **role B — IDENTIFIER** | none. A different value names a different object; a gate **refuses** rather than reconciles | n/a — must not move |
| The `from` attribute observed in L1 | value: TRANSITIONAL × UNTRACKED · record: **STATIC** (§5.2) | the observation record is the durable artifact | n/a |
| Agent Card `STATUS` | three machines (§7.1) | split into named fields | yes |

---

## 9 · Existing mechanisms — adoption and divergence · **[note 4]**

### 9.1 · Adopted

| Need | Existing mechanism | Site |
|---|---|---|
| Correct a STATIC error without erasing history | append a correction record | `COR-20260816-GOV311-001`; superseded checkpoints; receipt-ledger chain |
| Never store what can be computed | *the tool that causes the change re-anchors it* | `designed_for_growth.md` consequence 1; `growth_anchors.py` |
| Reopen a rejection whose premise expired | `REVIVAL_TRIGGER` + re-audit on every new mechanistic DATO | `epistemic_discipline.md` §2; eleven ledger entries |
| Show a passing test could have failed — the (a2) remedy | *a green suite is evidence only if the environment it ran in is capable of exhibiting the defect* | `PATTERN_ALREADY_SOLVED_GATE` variant 3 |
| Force re-examination of a transitional value | expiry with `PROMOTE / REJECT / EXTEND_WITH_REASON` | `PROVISIONAL_OPERATIONAL_PRACTICE`, Annex E.3 |
| Append-only ledger writable outside a batch | designated **validated** carve-out | state manifest preamble; `LEGEND_CORE.md`; `fulltext_receipts.py` |
| Freeze an append-only ledger without false alarms | tier 2, prefix length + prefix digest | `FREEZE_SCOPE_GATE` |

### 9.2 · Closed-set discipline — adopted verbatim · **[note 4b]**

`LEGEND_CORE.md` already governs closed-set state values, for claims:

> *Valid states: `consolidated baseline | in observation | conflicting evidence | flagged for
> review | background only | archived`. Never invent states. Every change → change log.
> Non-standard states → flag, do not autonomously correct.*

**Adopted unchanged for every transitional field**: the `value` comes from a declared closed set;
inventing a value is forbidden; a value outside the set is **flagged, never silently corrected**.
The last clause matters most here — a classifier that autocorrects an unexpected status would
convert a visible defect into an invisible one.

Closed sets already declared and to be reused verbatim rather than restated: J.2's actor and lab
machines (§7.1), `I.4`'s `VERIFIED | UNVERIFIED`, `J.3`'s
`PENDING | APPROVED | APPROVED_WITH_MODIFICATION | DENIED | REVISION_REQUESTED`, `A.5`'s task
states, `E.1`'s learning lifecycle.

### 9.3 · The state manifest is the existing home for operational transitional state · **[note 4a]**

`framework/state/state_manifest_current.md` already is what §6 describes, for one domain:

> *This is the only **state-control** file updatable outside a `BATCH_COMMIT`. … Every
> operational event (ingest, lint, commit candidate, batch commit, branch) must update it.*

It carries `current_state`, `deep_dive_gate`, `ingest_gate`, `batch_commit_gate` — transitional
fields with an existing update rule that is precisely *the event carries the update*, and an
existing carve-out permitting the write.

**Adoption:** operational transitional state stays there. §6 does not create a second home for it
and must not.

**Declared divergence:** an artifact's own binding status stays **on the artifact**, not in the
manifest. Reason: a reader of `roles/plan.md` must be able to see whether it binds without loading
a second file, and the manifest tracks the laboratory's operational state rather than the
lifecycle of every governed document. The cost of the divergence is two homes for two kinds of
transitional state, and the boundary is: *operational state of the system* → manifest; *binding
state of a document* → the document. Stated so the next actor does not have to infer it, per the
gate's own instruction to adopt or write down why you diverge.

---

## 10 · Capability demotion — two questions, not two options · **[note 3]**

Revision 1 offered two alternatives. **Mirror is right that they are not alternatives**, and the
separation dissolves the dilemma rather than resolving it by convenience.

| Question | Answer | Basis |
|---|---|---|
| **(B) who writes the evidence event** — repeated failures observed | **Mirror** | Annex C.4: `SYSTEM → Mirror`. Repeated failure across tasks is a system observation, and G.3 already assigns Mirror the coordination review that detects it |
| **(A) who writes the state transition** `VERIFIED → UNVERIFIED` | **orchestrator** | promotion symmetry: I.4 gives promotion to Orchestrator at L2, and a state machine whose two directions have different owners has no single authority over its values |

Two records, two writers, two files — which the §7.3 writer-named scheme supports natively and
which a subject-named scheme could not have expressed at all.

**Still requiring ratification.** The frozen text names neither writer: I.4 names Mirror only as
*detector*. The assignment above **follows from** C.4 and promotion symmetry; it is not stated
anywhere, so it remains a proposal for the operator under H.1 and is not adopted by having been
derived.

---

## 11 · Evidence — the instances this model was built from

All measured during the v3.1.1 bootstrap and its reviews. Each is (A); each was remedied by
**re-measuring**, never by anyone remembering better.

| # | Instance | Branch | Found by |
|---|---|---|---|
| 1 | Candidate hash irreproducible: `$(...)` strips a trailing newline | a1 | mirror |
| 2 | The same byte made `wc -l` report 507 where the listing held 508 | a1 | mirror |
| 3 | `ONE_WRITER` argued from a reflog that could not have shown the contrary | a2 | mirror |
| 4 | A literal-presence check returning PASS while missing the true destination | a2 | mirror |
| 5 | Case-sensitive grep returned 0; the text is at `gold_is_in_the_details.md:45` with a capital **P**. Rule 5e preserved | a2 | orchestrator |
| 6 | Truncated display: phrase at character 470 of an 829-character line, so `cut -c1-400` returns 0 | a2 | mirror |
| 7 | `sed -n "${VAR}p"` with an empty variable printed the whole file; "line length 9087" was coherent and wrong | a2 | plan, on itself |
| 8 | 834 bytes published as characters; delta of 5 comes from **3** multi-byte characters | a2 | orchestrator, refined by plan |
| 9 | Both actors reconciled #8 by assuming an unchecked explanation, which was wrong | a1 | orchestrator |
| 10 | **This proposal classified `ROLE_CONTRACT_HASH` as STATIC one section after drawing the correct distinction for another hash** | a1 | mirror, at R4 |
| 11 | **The fix for #10 — *"a hash is never STATIC"* — was never tested against `BASE_HEAD`, and would have reclassified every gate anchor as a recomputable measurement** | a1 | mirror, at R4 re-review |
| 12 | **"Untracked values are never cited as evidence" would have made the observation that closed L1 inadmissible** | a1 | mirror, at R4 re-review |

Twelve instances; six are (a2). Every correction in the chain was right about the thing it
corrected while carrying a smaller instance of the same family.

**Instances 10, 11 and 12 form one chain and are the most useful rows in this table**, because
they are this document failing three times in the same place: a per-field misclassification, then
a universal rule that over-corrected it, then a second universal rule with the same defect. The
first was uneven application; the second and third were its mirror image — **a rule stated more
strongly than the evidence that produced it.** Both are (a1): an assertion made without testing it
against the cases it would govern, and in both cases the counterexample was already in the
repository, load-bearing, and two files away.

The generalisation worth keeping: **over-correction is not the opposite of uneven application, it
is the same error at a higher altitude.** Fixing a case by promoting it to a universal skips the
same step — checking the rule against the instances it now covers.

The sharpest statement of the class came out of #7: **a mis-scoped pattern leaves a suspicious
silence; a broken pipeline hands you a number.**

---

## 12 · Attribution

- The discriminator (§2.1) is the **orchestrator's**; it replaced a test of mine that would have
  licensed rewriting the log.
- The (a1)/(a2) split and instances 1–4, 6 are **Mirror's**.
- Instances 5, 8, 9, and the objection correcting the ledger path to writer-named, are the
  **orchestrator's**.
- B-1 through B-4 and notes 1–4 are **Mirror's**, at R4. B-3 and B-4 were defects in the model;
  B-1 was an ambiguity that would have misclassified the dismissal ledger; B-2 was a capability
  asserted into existence.
- BLOCKING-1 and BLOCKING-2 are **Mirror's**, at the R4 re-review, together with the framing that
  resolves the first — *hash is not a class by itself; classification depends on semantic role* —
  and the distinction that resolves the second, between the durability of a value and the
  admissibility of an observation. Both caught rules this document had stated more strongly than
  its evidence.
- The two-axis composition, the transitional-owner rule, the four-field form, the Agent Card
  split, the field-scoped-by-record unit, and instance 7 are **Plan's**.

---

## 13 · What the next review must decide

*(Items 1, 2 and the §6.1, §7, §10 questions were accepted at the R4 re-review and are retained
for the record rather than reopened.)*

1. §2.2 — ✅ accepted at re-review.
2. §3 — ✅ accepted at re-review. Note that §2.1b adds a step **before** this axis rather than a
   class inside it, precisely so the accepted section stands unamended; confirm that placement is
   right.
3. §4.1 — is the three-role split (measurement / identifier / historical record) correct, and is
   *"a gate refuses rather than reconciles"* the right consequence for a role-B mismatch?
3b. §2.1b — is the operational test — *"the measurement was wrong" versus "that is a different
   object"* — sufficient to sort a value without appeal to theory?
3c. §5.2 — are the four conditions on an observation of an untracked value the right ones, and is
   *authorised observer* definable without a registry that does not yet exist?
4. §6.1 — is the resolver contract a model requirement or an implementation smuggled into a
   proposal? It was written to be the former.
5. §7.1 — is retiring the field name `STATUS` proportionate to the confusion it caused?
6. §7.3 — is the carve-out plus validator plus tier-2 freeze plus consolidated view the right
   cost, or is the capability record better left uncommitted until a lease exists?
7. §9.3 — is the divergence from the state manifest justified, or should artifact status live
   there too?
8. §10 — does the (A)/(B) separation hold, and is the derived assignment acceptable as a proposal?
9. Ordering: the status/C-8 batch is frozen behind this review. If adopted, the batch should apply
   the new form rather than the old value — one change rather than two.

---

## 14 · Non-blocking observations from the R4 re-review — recorded, not acted on

**The append-only carve-out remains a prose declaration unless a validator exists.** Correct, and
kept at proposal level deliberately. §7.3 states the requirement — a carve-out is a permission
*plus* a validator the LINT consumes — and does not build one. Writing the validator would be
implementation, which the hold forbids, and a proposal that quietly shipped its own enforcement
would be the same boundary violation this document's §0 disclaims.

**`BLOCKED` / `AWAITING_APPROVAL` overlap between J.2 and A.5.** Noted and left outside scope. J.2
lists them among actor states; A.5 lists them among task states. Whether one actor blocked on one
task is the same fact recorded twice, or two facts that can legitimately disagree, is a question
about the frozen text rather than about this model. Recorded here so it is not rediscovered.

**Checkpoint lineage.** `CHK-plan-0007` recorded the hand-off at revision 1. Revisions 2 and 3
each changed what a resumer would need to know, so a successor checkpoint accompanies this
revision rather than an edit to `0007` — the same append-not-edit rule the model proposes, applied
to the model's own process artifacts.

---

---

## 15 · Closure

C-9 closes at revision 4 on the operator's directive, with the minimal patch its last review
prescribed: **one clause**, §2.1c, scoping the identifier exit to names something is bound to.

**Accepted is not adopted.** The status above records that the proposal is settled as a
*document*; it changes no governed artifact. Every remedy in §8 remains frozen, L2 remains
suspended, and the status/C-8 batch remains frozen. Adoption of any clause is a governed change
with its own review, and for the clauses touching `plan_defined_parameters.md` or a role contract
it carries a fingerprint rotation.

**What was deliberately kept out.** The Fable advisory produced two formulations better than
anything this document carries — *the role constrains admissible behaviour rather than composing
freely*, and *the violation is not the change, it is a transition without an event*. Neither is
folded in here. The second in particular would improve §5: C-9 makes staleness **attributable**
by naming an owner, while that formulation makes it **detectable**, and detection beats
attribution because it does not depend on anyone noticing.

They are held out on purpose. Folding a binding-contract abstraction into a proposal four
revisions deep and one clause from closure would replace a one-clause fix with a redesign, inside
a document whose §0 disclaims exactly that. They are registered separately as
[`ADVISORY-FABLE-C9-001.md`](ADVISORY-FABLE-C9-001.md), outcome `MACRO_UPGRADE_CANDIDATE`, where
they can be argued on their own merits under §17's governed path.

**Nothing here is adopted by having been written.** No implementation, no governance modification,
L2 suspended, batch frozen — as directed.

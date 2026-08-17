---
artifact: PROPOSAL C-9 — how LEGEND represents state
proposal_id: C9-STATE-MODEL
revision: 2
task_id: C9-STATE-MODEL-001
author: plan
authored_on: 2026-08-17
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1), so this
  file modifies no content-domain artifact, no candidate content hash and no role fingerprint
lineage:
  - rev 1 @ f7a0049 — R4 Mirror review returned REQUEST CHANGES (B-1…B-4, notes 1–4)
  - rev 2 @ this commit — revises rev 1 in response; supersedes nothing, corrects itself
status: PROPOSED
status_since_event: R4 REQUEST CHANGES on rev 1, relayed by the operator 2026-08-17
status_transition_owner: operator, on the outcome of the next R4 Mirror review
status_next_review: R4 — MIRROR_REQUIRED, before anything proposed here is implemented
hold: no implementation and no governance modification until that review completes; L2 suspended;
  the status/C-8 batch frozen pending a later operator decision
---

# PROPOSAL C-9 — static, derived and transitional state · revision 2

> **Lineage note.** Revision 1 was reviewed at R4 and returned `REQUEST CHANGES` with four
> blocking findings. This revision answers them. Three of the four were defects *in the model*,
> not in its presentation, and one — B-3 — was the proposal committing, inside itself, the exact
> failure it proposes to fix. That is recorded rather than smoothed over, because a proposal about
> state errors that hides its own is worth less than the model it carries.

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

### 4.1 · Every hash is DERIVED. A recorded hash is a STATIC record of a derivation. · **[B-3]**

Revision 1 classified `ROLE_CONTRACT_HASH` as STATIC. **Mirror is right that this is wrong**, and
the error is instructive: §4 of revision 1 drew exactly this distinction for
`CANDIDATE_CONTENT_HASH` — *recorded in a commit message it is historical; emitted by the script
today it is derived* — and then failed to carry it one section later to a hash of the same kind.

**Uneven application, inside the document proposing to fix uneven application.** Not by forgetting
the rule: by recognising the shape and stopping there, which is the mechanism this repository
names in `designed_for_growth.md` consequence 5.

The corrected rule is general and removes the per-field judgement:

> **A hash is never STATIC. The *value* is DERIVED — recomputable from its input by a stated
> recipe. A *record* of that value, dated, is STATIC.**

| Occurrence | Class | Remedy if wrong |
|---|---|---|
| `shasum -a 256 roles/plan.md` today | DERIVED | recompute |
| `ROLE_CONTRACT_HASH` inside `CHK-plan-0006` | STATIC — what it hashed to at that checkpoint | append a correction |
| `CANDIDATE_CONTENT_HASH` in commit `908197b` | STATIC | append a correction |
| `CANDIDATE_CONTENT_HASH` in a live manifest field | **DERIVED, and must not be stored** without its recipe beside it | recompute |

The last row is the one with teeth: it is why the manifest publishes the reproduction command and
why the entry count was removed rather than corrected (RC-3). A stored derived value without its
recipe is a state error waiting for its input to move.

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
| *(untracked cell)* | whoever holds the runtime | free to rewrite; never tracked; never cited as evidence |

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
| `ROLE_CONTRACT_HASH` wherever stored live | **DERIVED** (§4.1) | recompute; store only inside dated records | yes |
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

Six of ten are (a2), and every correction in the chain was right about the thing it corrected while
carrying a smaller instance of the same family — #10 included, which is this document.

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
- The two-axis composition, the transitional-owner rule, the four-field form, the Agent Card
  split, the field-scoped-by-record unit, and instance 7 are **Plan's**.

---

## 13 · What the next review must decide

1. §2.2 — is *field, scoped by record* the right unit, and does it protect every append-only
   artifact rather than only the two tested?
2. §3 — are two axes stated correctly, and is `TRANSITIONAL × UNTRACKED` the whole of what
   "ephemeral" meant?
3. §4.1 — is *no hash is ever STATIC* too strong?
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

**Nothing here is adopted by having been written.** No implementation, no governance modification,
L2 suspended, batch frozen — as directed.

---
artifact: PROPOSAL C-9 — how LEGEND represents state
proposal_id: C9-STATE-MODEL
task_id: C9-STATE-MODEL-001
author: plan
authored_on: 2026-08-17
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1), so this
  file modifies no content-domain artifact, no candidate content hash and no role fingerprint
status: PROPOSED
status_since_event: operator directive of 2026-08-17, confirmed directly after two relays
status_transition_owner: operator, on the outcome of an R4 Mirror review
status_next_review: R4 — MIRROR_REQUIRED, before anything proposed here is implemented
hold: no implementation and no governance modification until that review completes; L2 suspended;
  the status/C-8 batch frozen pending a later operator decision
---

# PROPOSAL C-9 — static, derived and transitional state

> The four status fields above are written in the form this document proposes. They are the
> smallest available demonstration: a transitional value that names the event that set it, the
> actor who owns its next transition, and when that transition is due. If the proposal is
> rejected, this header is the first thing to revert.

## 0 · What this proposes, and what it does not

It proposes **a classification and an ownership map**: a question that sorts any recorded value
into one of four classes, and a rule naming who may write each class. It proposes almost no new
machinery, because three of the four remedies already exist in this repository and the fourth is a
field convention.

It does **not** implement anything, does not modify governance, does not adopt itself, and does
not repair the live defects it uses as examples. Those repairs are frozen by the hold, which is
correct: a correction that pre-empts the model meant to govern corrections is the thing being
guarded against.

Adopting any part of this requires a governed change to content-domain artifacts and, for the
parts touching `plan_defined_parameters.md` or a role contract, a fingerprint rotation. That cost
is stated here so review can weigh it, not discovered afterwards.

---

## 1 · The problem, as observed

Two shapes were measured during the v3.1.1 bootstrap. They look identical in a diff and have
opposite remedies.

**(A) STATE ERROR — the value was wrong when written.**
Remedy: verification before assertion. Mirror split this, and the halves differ:

- **(a1)** the assertion was never tested. Remedy: test before asserting.
- **(a2)** a test ran, passed, and could not discriminate. Remedy: show the test can fail.

(a2) is the worse half, because it leaves a green result behind. A wrong (a1) looks like an
untested claim; a wrong (a2) looks like a verified one.

**(B) STALE TRANSITION STATE — the value was correct when written and was invalidated by a
transition the system itself performed.**
Remedy: the transition must carry the update. Human memory is not a mechanism.

Seven governed artifacts still read `status: PROPOSED — binding once Mirror hostile review passes
and the operator approves` with both conditions satisfied since `84407c1` and
`RES-20260816-GOV311-001`. Nothing was wrong when written. The system's own success invalidated
them.

---

## 2 · The discriminator — one question, asked before any other

The obvious test is *"is this statement currently false?"* **That test is wrong, and its failure
is the most important constraint in this proposal.**

It flags `governance/design_records/materialization_log.md:238` — a sentence inside MAT-003
reading *"All are marked `status: PROPOSED`. They become binding when Mirror's hostile review
passes and the operator approves"* — which was **true on 2026-08-16 when written**, sits in an
append-only log, and is dated testimony. A model that cannot tell that from a stale status field
licenses rewriting history, which is a more expensive failure than any stale field.

The question that must be asked first is one step earlier:

> ### Does this artifact claim to describe the present?

If it claims to describe *a moment*, it is historical and immutable. If it claims to describe
*now*, it is live and must either be computed or be bound to the event that changes it.

*(This question is the orchestrator's, from the exchange of 2026-08-17. The test it replaces was
mine, and it was the wrong one.)*

---

## 3 · Four classes, on two axes

The operator's addendum asks for **permanent / derived / ephemeral**. That is a *storage* axis.
The distinction above is a *semantic* axis: **static / derived / transitional**. They are not the
same axis, and composing them yields four classes, not three.

| Class | Claims to describe | Where it lives | Who writes it | Remedy when wrong |
|---|---|---|---|---|
| **STATIC** | a moment, dated | tracked, append-only | the witness; corrections **appended**, attributed | re-measure, then append a correction — never edit |
| **DERIVED** | now, by a stated rule | not stored; or cached with its input digest | the tool that computes it — never a hand | recompute |
| **TRANSITIONAL** | now | tracked, event-linked | the **transition owner** | the event carries the update |
| **EPHEMERAL** | now, for this run only | untracked / gitignored | whoever holds the runtime | discard; it is rewritten freely |

The two axes map onto each other imperfectly, and the gap is where the confusion lived:
*permanent ≈ static*, *derived ≈ derived*, but **ephemeral ≠ transitional**. Ephemeral means
short-lived and disposable; transitional means it moves through defined states and must be
maintained. A value can be long-lived and transitional (a status), or short-lived and static (a
measurement taken once).

**The general rule that falls out** is `designed_for_growth.md` consequence 1 in different
clothes: *a transitional value that a human must remember to update is a defect by construction.*
Either derive it, or bind it to the event.

---

## 4 · Requirement 1 — historical event vs current derived state

Both are *true*; they differ in what they are true **about**.

| | Historical event | Current derived state |
|---|---|---|
| Asserts | this happened, then | this holds, now, by rule |
| Record carries | a **timestamp of assertion** | a **recipe** |
| Goes stale? | never — the moment does not move | never — it is recomputed |
| Instrument | append a correction if mis-measured | run the command |
| Examples | MAT-003's sentence; `CANDIDATE_CONTENT_HASH c39ecae8…` as recorded in commit `908197b`; `RES-20260816-GOV311-001` | the four role fingerprints; the candidate content hash **as computed now**; the domain entry count; LINT and publication-gate verdicts |

The same hash appears in both columns, which is not a contradiction and is worth stating plainly:
`c39ecae8…` recorded in a commit message is a historical event — *this is what the tree hashed to
then*. The same value emitted by `candidate_content_hash.py` today is derived. The first is never
corrected; the second is never stored.

**The instrumentation caveat this requirement needs.** A derived value is only as good as the
observation that produced it, and observation is where this bootstrap failed repeatedly (§11). The
requirement therefore carries a rider: *a derived value must record the command that produced it,
in a form a reader can re-run without reconstructing a pipeline.* Not the output of the command —
the command.

---

## 5 · Requirement 2 — ownership of the writer, per class

This is the requirement that explains the seven stale statuses better than any mechanism does.

**A transitional field with no named transition owner has nobody who is delinquent when it stops
being true.** The seven did not go stale because a mechanism was missing. They went stale because
no role was named, so no actor was late.

| Class | Writer | Constraint |
|---|---|---|
| **STATIC** | the actor that witnessed it | never edited by anyone, including its author. A correction is a **new record** naming what it supersedes, as `COR-20260816-GOV311-001` supersedes a citation without touching the line that carried it |
| **DERIVED** | the tool | *the tool that causes the change re-anchors it.* No actor writes a derived value by hand; if a value is cached, the cache is written by the computing tool and carries its input digest |
| **TRANSITIONAL** | the actor whose act causes the transition | named **in the field itself**, so staleness has an owner |
| **EPHEMERAL** | whoever holds the runtime | free to rewrite; never tracked; never cited as evidence |

**Transition owners, for the classes in play today:**

| Field | Transition | Owner |
|---|---|---|
| `status: PROPOSED → BINDING` on a governed artifact | Mirror review passes **and** operator approves | **operator** — Plan transcribes on the event |
| `STATE: PENDING → APPROVED` in the approval queue | operator resolves | **operator** |
| capability `UNVERIFIED → VERIFIED` | L2 smoke passes | **orchestrator** |
| capability `VERIFIED → UNVERIFIED` | repeated failures, detected by Mirror | 🔴 **UNRESOLVED** — see §10 |
| `ACTIVE ↔ DOWN` in the roster | heartbeat timeout | **orchestrator** |
| a governance rejection whose premise expires | the premise is falsified | **the actor that produced the datum**, via re-audit (§9) |

---

## 6 · Requirement 3 — lifecycle of transitional statuses

Every transitional field carries four things, not one:

```
{ value, since_event, owner, next_review }
```

- **value** — the current state, from a closed set
- **since_event** — the durable event that set it. A pointer, not prose: a reader verifies by
  following it, and a value with no event behind it is unfalsifiable
- **owner** — who performs the next transition (§5)
- **next_review** — when the value must be re-examined even if no event fires

The last field is what stops a transitional value from becoming permanent by neglect. It is not a
new invention: `PROVISIONAL_OPERATIONAL_PRACTICE` (Annex E.3) already carries expiry with a forced
`PROMOTE | REJECT | EXTEND_WITH_REASON`, and the four PROVISIONAL parameters in
`plan_defined_parameters.md` already use it. The proposal is to generalise that shape from
learning practices to every transitional field.

**Worked example**, using the seven live cases. Current form:

```
status: PROPOSED — binding once Mirror hostile review passes and the operator approves
```

Proposed form:

```
status: BINDING
status_since_event: RES-20260816-GOV311-001
status_transition_owner: operator
status_next_review: on the next MAJOR governance change
```

The difference that matters is not the value. It is that the second form **cannot go silently
stale**: the event pointer either resolves to a resolution that says BINDING or it does not, and
that is checkable by a script rather than by a reader's memory.

---

## 7 · Requirement 4 — permanent / derived / ephemeral separation

The Agent Card is the worked case, and it is not one artifact. Annex I.4's own field list splits
along the seam:

```
ACTOR_ID / ROLE / WORKTREE / ROLE_CONTRACT / ROLE_CONTRACT_HASH     → permanent (static)
CAPABILITIES [{capability, status VERIFIED|UNVERIFIED, last_verified}] → TRANSITIONAL
CURRENT_SESSION_REF / CURRENT_SESSION_ID / STATUS / LAST_SEEN       → ephemeral
```

Two of the three already have declared homes in `deployment/deployment_profile.md`, approved with
the v3.1.1 candidate: the portable half states it carries *"the actor definitions"* and tabulates
ACTOR_ID → worktree → contract for all six actors; the local half declares
`SESSION_REFS: ACTOR_ID -> current session reference; ephemeral, rewritten freely`, in the
gitignored `deployment/local_instance.md`.

**So the third home was not one artifact needing relocation. It was one artifact that should never
have been single** — which is precisely why it kept finding new ground: nothing owned it because
two things already did.

The capability record is the third part, and it is **transitional**, not homeless. It looked
homeless because *"permanent or ephemeral?"* is a question it cannot answer, being neither. Under
§5 it needs a writer-owned home:

```
proposed:  ledger/capabilities/<WRITER_ACTOR_ID>.jsonl
           append-only; the SUBJECT is a field, not the filename
           { subject_actor_id, capability, status, evidence, since_event, at }
```

Named by its **writer**, not its subject. P7's one-writer property comes from *an actor owning
the file in its own worktree*; a file named `<ACTOR_ID>.jsonl` written by neither the actor it
names nor the actor whose tree holds it borrows the shape and drops the precondition. Naming by
writer restores it and makes the filename answer *who may write here* rather than *who is being
described* — so the confusion cannot recur for an actor who has never read P7.

Two mechanisms this needs, **both already existing**, per `PATTERN_ALREADY_SOLVED_GATE`:

- **the append-only carve-out.** `LEGEND_CORE.md` and the state manifest already designate
  non-canonical append-only ledgers as explicit, *validated* carve-outs writable outside a
  `BATCH_COMMIT`. The load-bearing word is **validated**: the receipt ledger's carve-out is a
  permission *plus* a validator the LINT consumes, so a rewritten history halts the system. A
  carve-out without its validator is an exemption wearing a carve-out's name;
- **freeze tier 2.** `FREEZE_SCOPE_GATE` pins append-only ledgers by *prefix length + prefix
  digest*, so growth is legal and only rewriting the frozen prefix is a violation. Whole-file
  pinning would fire on every legitimate append.

---

## 8 · Applied to every live case

| Case | Class | Remedy | Frozen by the hold? |
|---|---|---|---|
| Seven `status: PROPOSED` on governed artifacts | TRANSITIONAL | §6 four-field form; owner = operator; event = `RES-20260816-GOV311-001` | **yes** |
| `claude_md_migration_map.md` front matter | TRANSITIONAL (non-normative artifact) | same | **yes** |
| Six of ten `pending` rows in `ANNEX_INDEX` | should be **DERIVED** | *does this artifact exist?* is a question a script answers; stop storing the answer | **yes** |
| The `held` row in `ANNEX_INDEX` | a **rejection with an expired premise** | `epistemic_discipline` §2 — `REVIVAL_TRIGGER` + the re-audit rule, already governing exactly this in the dismissal ledger and never carried to a governance rejection | **yes** |
| `materialization_log.md:238` | **STATIC** — dated testimony | 🔴 **none. Do not touch.** If the log must reflect the change, it takes a *new record* | n/a — must remain |
| C-8, the stale capability line in `roles/plan.md` | TRANSITIONAL | §6 form; owner = orchestrator at L2 | **yes** |
| Agent Card / `runtime/agent_card_registry.md` | three classes in one file | §7 split | **yes** |
| Capability verification status | TRANSITIONAL | §7 writer-named ledger | **yes** |

Every remedy above is held. The proposal's purpose is to be reviewed, not to license the repairs.

---

## 9 · What already exists — three of four remedies

This is the smallest and most defensible form of the proposal, and it follows the gate's own
prescription: *search this repository for the same concept before writing it, and if it exists,
adopt it or write down why you are diverging.*

| Need | Existing mechanism | Site |
|---|---|---|
| Correct a STATIC error without erasing history | append a correction record | `COR-20260816-GOV311-001`; the superseded checkpoints; the receipt-ledger chain |
| Never store what can be computed | *the tool that causes the change re-anchors it* | `designed_for_growth.md` consequence 1; `growth_anchors.py`; `candidate_content_hash.py --show-domain` |
| Reopen a rejection whose premise expired | `REVIVAL_TRIGGER` + re-audit on every new mechanistic DATO | `epistemic_discipline.md` §2; eleven entries in the dismissal ledger |
| Show that a passing test could have failed — the (a2) remedy | *a green suite is evidence only if the environment it ran in is capable of exhibiting the defect*; the test mounts the condition, plus a companion assertion that the fixture would fail without the fix | `PATTERN_ALREADY_SOLVED_GATE` variant 3, 2026-08-10 |
| Force a transitional value to be re-examined | expiry with `PROMOTE / REJECT / EXTEND_WITH_REASON` | `PROVISIONAL_OPERATIONAL_PRACTICE`, Annex E.3 |

**The only genuinely new element is the four-field transitional form** of §6 and the writer-named
ledger path of §7. Everything else is an existing remedy reached by a new question.

---

## 10 · UNRESOLVED — deliberately not filled

**Who writes a capability demotion.** Annex I.4 reads:

```
DETECTION:  fallimenti ripetuti sullo stesso tipo di task → Mirror coordination review
RECOVERY:   retrocessione a UNVERIFIED → nuovo smoke → riabilitazione
```

Mirror is named as the **detector**. The writer is named by nobody — not I.4, not H.1, not G.2.
Two candidates, both defensible:

1. **Orchestrator writes on Mirror's finding.** Symmetric with promotion at L2; keeps one writer
   for the capability ledger; makes Mirror purely diagnostic, consistent with *no command over
   actors*.
2. **Mirror writes, Orchestrator consumes.** Puts the record where the evidence is; costs a second
   writer, hence a second file under the §7 naming rule, which the shape supports.

Not filled here, for the same reason `MIRROR_RETROSPECTIVE`'s `N` was left unset: an actor
choosing who may write a record that constrains actors is the convenient interpretation. This is
the operator's under H.1.

---

## 11 · Evidence — the instances this model was built from

Requirement 1's instrumentation rider (§4) exists because of these. All were measured during the
v3.1.1 bootstrap and its reviews; each is (A), and each was remedied by **re-measuring**, never by
anyone remembering better.

| # | Instance | Branch | Found by |
|---|---|---|---|
| 1 | Candidate hash irreproducible: `$(...)` strips a trailing newline, so the computed and published values differed by one byte | a1 | mirror |
| 2 | The same stripped byte made `wc -l` report 507 where the listing held 508 | a1 | mirror |
| 3 | `ONE_WRITER` argued from a reflog that could not have shown the contrary | a2 | mirror |
| 4 | A literal-presence check that returned PASS while missing the true destination | a2 | mirror |
| 5 | Case-sensitive grep for *"publish the derivation…"* returned 0; the text is at `gold_is_in_the_details.md:45` with a capital **P**. Rule 5e preserved | a2 | orchestrator |
| 6 | A truncated display: the phrase begins at character 470 of an 829-character line, so `cut -c1-400` returns 0 while the full line returns 1 | a2 | mirror |
| 7 | `sed -n "${VAR}p"` with an empty variable printed the whole file; the resulting "line length 9087, phrase at char 8363" was coherent and wrong | a2 | plan, on itself |
| 8 | 834 bytes published as 834 characters; the line is 829 characters and 834 bytes, and the delta of 5 comes from **3** multi-byte characters, not 5 | a2 | orchestrator, then refined by plan |
| 9 | The two actors reconciled #8's discrepancy by assuming an explanation ("table-prefix accounting") that neither had checked, and which was wrong | a1 | orchestrator |

**The pattern the table shows** is the finding, not the individual rows: six of nine are (a2), and
every correction in the chain was right about the thing it corrected while carrying a smaller
instance of the same family. That is not carelessness compounding. It is what this class looks
like when it is actually being hunted — each pass measures at finer resolution than the last, and
the instrument does not become more careful on its own.

The sharpest statement of the class came out of #7: **a mis-scoped pattern leaves a suspicious
silence; a broken pipeline hands you a number.** Silence invites a second look; content reads as
an answer.

---

## 12 · Attribution

- The discriminator of §2 — *does this artifact claim to describe the present* — is the
  **orchestrator's**. It replaced a test of mine that would have licensed rewriting the log.
- The (a1)/(a2) split of §1 and instances 1–4 and 6 are **Mirror's**.
- Instances 5, 8 and 9, and the objection that corrected the §7 ledger path from subject-named to
  writer-named, are the **orchestrator's**.
- The four-class composition, the transitional-owner rule of §5, the four-field form of §6, the
  Agent Card split of §7, and instance 7 are **Plan's**.
- The reason `materialization_log.md:238` must survive was raised by Plan and adopted by the
  orchestrator as the constraint the model has to answer.

Recorded because a proposal that erases who found what is itself a state error about its own
provenance.

---

## 13 · What the review must decide

1. Is the discriminator of §2 correct, and does it protect dated testimony in every case, not
   just the one that prompted it?
2. Are four classes right, or does the two-axis composition hide a fifth?
3. Is the four-field transitional form (§6) worth its cost? It touches every governed artifact
   carrying a status, and two of those are in `CORE`, so adoption rotates fingerprints.
4. Should `ANNEX_INDEX`'s existence rows become derived — i.e. should the index stop storing
   answers a script can produce?
5. §7's writer-named capability ledger: is the carve-out plus validator plus tier-2 freeze the
   right cost, or is the record better left uncommitted until a lease exists?
6. §10: who writes a capability demotion.
7. Ordering: the status/C-8 batch is frozen behind this review. If the proposal is adopted, the
   batch should apply the new form rather than the old value, which makes it one change rather
   than two.

**Nothing here is adopted by having been written.** No implementation, no governance modification,
L2 suspended, batch frozen — as directed.

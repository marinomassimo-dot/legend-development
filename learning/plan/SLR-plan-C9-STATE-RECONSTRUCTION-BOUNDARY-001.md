---
artifact: SESSION LEARNING RECORD (Annex E.6) — boundary analysis
record_id: SLR-plan-C9-STATE-RECONSTRUCTION-BOUNDARY-001
actor_id: plan
role: Plan — identity established from `deployment/deployment_profile.md`, not from a contract
date: 2026-08-22
task_id: PLAN_BOUNDARY_ANALYSIS_C9_STATE_RECONSTRUCTION_v1
mode: READ_ONLY_ANALYSIS → CREATE_ANALYSIS_ARTIFACT_ONLY
objects_analysed:
  - governance/candidates/PROPOSAL-C9-STATE-MODEL.md @ blob d2ada5bc (identical on `main` and HEAD)
  - governance/candidates/PROPOSAL-ORCH-STATE-RECONSTRUCTION.md @ ref orch-state-reconstruction,
    blob e6af7e3d — present on that ref only; absent at this HEAD
authority: none. This record decides nothing, merges nothing, sequences nothing and modifies
  neither proposal. It is analysis offered for review. Q-10 is left exactly as open as it was.
normative: no
adjacent_and_binding:
  - DEC-20260822-ORCH-STATE-RECONSTRUCTION-CANDIDATE (OPTION B — HELD_AS_CANDIDATE). Its
    BOUNDARIES explicitly do NOT resolve the C-9 relationship; its NEXT_ALLOWED_ACTION lists
    "Plan's determination on Q-2 and on C-9 sequencing, being that role's row, subject to
    review" among what may occur without that record authorizing it. **This dispatch said
    `Do not decide.` No determination is made here.** Analysis only.
  - DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE — all four role contracts are PROPOSED. No
    authority is read from `roles/plan.md` anywhere in this record.
  - REV-ORCH-STATE-RECONSTRUCTION-001 § F-13 @ ref mirror — the only prior measurement of this
    overlap. Its two rows were reproduced here and both hold. This record extends it; it does
    not restate it.
curation: PENDING — E.2 gives epistemic curation to Mirror. Every finding below is proposed.
---

# C-9 × ORCH-STATE-RECONSTRUCTION — boundary analysis

> **This record does not answer the question it was given.** The dispatch asked whether the two
> proposals are duplicates, complementary layers, subsuming, or unrelated — and then said
> `Do not decide.` What follows is the evidence each answer would have to be built from, plus
> one coupling that was not previously on the record. **Selecting among A/B/C/D is a governance
> act this record does not perform.**

---

## IDENTITY

Established from repository evidence, not from the dispatch's assertion and not from a contract.

| Field | Value | How established |
|---|---|---|
| `actor_id` | `plan` | `deployment/deployment_profile.md` line 34 maps `plan` → worktree `evidence-index`; this session is standing in that worktree. **The profile's own caveat is carried:** *"Neither column is an ACTOR_ID oracle and neither is a write-authority oracle."* The mapping locates; it does not authorize |
| worktree | `/Users/massimo/Desktop/legend-public/.claude/worktrees/evidence-index` | `git worktree list` |
| branch | `plan-orchsurf-r4-transcription` | `git rev-parse --abbrev-ref HEAD` |
| HEAD | `2e22c4836a85c21ccced94af91ca40529b5de09b` | `git rev-parse HEAD` |
| working tree | clean before this file | `git status --porcelain` empty |
| authority claimed | **none** | `roles/plan.md` carries `status: PROPOSED`; per `DEC-20260822` consequence 2 no authority is read from it. This record needs none: it creates one file under `learning/`, which H.1 gives to *"ogni attore, solo proprio branch"* as a `WORK_COMMIT` |

🔴 **One divergence from the profile, recorded rather than smoothed.** The profile gives `plan`
the work surface *"worktree `evidence-index`, branch `evidence-index`"*. This session is in that
worktree but on branch `plan-orchsurf-r4-transcription`, which is **not** a descendant of
`refs/heads/evidence-index` (`git merge-base --is-ancestor` returned false). It is a topic branch
sharing the worktree. Whether the profile's `Work surface` column names a branch exactly or a
branch family is not resolved here; it is noted because an identity claim built on that column
should not silently absorb the difference.

---

## SURFACE MAP

Every negative claim below is scoped by this surface and by nothing wider.

```
MEASURED_FROM     worktree  evidence-index
                  branch    plan-orchsurf-r4-transcription
                  HEAD      2e22c4836a85c21ccced94af91ca40529b5de09b
                  tree      clean at measurement time
                  date      2026-08-22

REFS SURVEYED     48 total via git for-each-ref
                  Repository-wide sweeps iterate refs/heads + refs/tags + refs/remotes
                  = 43 refs. Sweeps are labelled REPOSITORY-WIDE(43) below.
WORKTREES         16 via git worktree list

RELATION TO main  🔴 main tip is 2bb27005 and is NOT an ancestor of this HEAD.
                  merge-base(HEAD, main) = 04693e68; 35 commits on HEAD not on main.
                  This surface is therefore NOT the surface DEC-20260822 measured from
                  (main @ 2bb27005, 47 refs / 15 worktrees). The count differs by the
                  branch and worktree this session added.

OBJECT PARITY     Both analysed blobs were pinned and compared against the surface the
                  operator decision used, so the divergence above does not reach them:
                    C-9   blob d2ada5bc — IDENTICAL on refs/heads/main and on this HEAD
                          sha-256 f162d356adbc2836b4001500ed9f094b4805d0cfe5515d0518cc8b9dd4fd6c55
                    ORCH  blob e6af7e3d @ refs/heads/orch-state-reconstruction
                          sha-256 f491d5247dc1cfffbee3aae66eb646e3114d764e9f18930f9082c34a3ea072ba
                                  — matches the sha-256 recorded in DEC-20260822 exactly
                  Both objects are byte-identical to what the operator decided on.

VALIDITY          NOT_FOUND on 43 refs is not NOT_EXIST. Clones, unpushed worktrees and
                  unreferenced objects lie outside this surface.
```

🔴 **`PROPOSAL-ORCH-STATE-RECONSTRUCTION.md` does not exist at this HEAD.** It was read via
`git show refs/heads/orch-state-reconstruction:…`. A REPOSITORY-WIDE(43) sweep places it on
exactly one ref. **This record is itself a ninth fragmented object** — written on a branch that
carries neither proposal-under-analysis at the location the other one lives. The pattern the
object diagnoses was paid again to analyse the object.

---

## ANALYSIS

### 1 · Purpose comparison

| | **C-9 STATE MODEL** | **ORCH STATE RECONSTRUCTION** |
|---|---|---|
| **Problem addressed** | A value that was **correct when written** and was invalidated by a transition the system performed — indistinguishable in a diff from a value that was **wrong when written**. Seven stale `status:` fields (§1, §8) | A **dispatch that cannot be safely made**: required objects on other refs, actor authority unclear, negatives lacking a measurement surface (§1.1–1.4) |
| **Input objects** | **Recorded fields**, scoped by the record enclosing them (§2.2 — *"the unit of classification is the field"*) | **Four state groups read across refs** — `ARTIFACT_STATE`, `ACTOR_STATE`, `AUTHORITY_STATE`, `DEPENDENCY_STATE` (§2) |
| **Output objects** | A classification (2 axes), a four-field form `{value, since_event, owner, next_review}`, an ownership map (§5.1, 6 rows), a resolver contract (§6.1), a capability ledger design (§7.3) | **Questions only.** §3 is 6 named check-groups, §4 a block-record shape *"if blocks were adopted"*, §6 ten open questions. It states: *"Where it names a check, the check does not exist. Where it names a field, no writer for that field is proposed."* |
| **Lifecycle stage** | 🔴 **POST-transition — the residue.** What was left behind, what class it is, who owes its next move | 🔴 **PRE-transition — the precondition.** Whether an act may begin at all |
| **Owner assumptions** | **Assumes owners are assignable** and assigns six (§5.1), deriving two more (§10) | **Assumes nothing.** Measures that 3 of 5 `ACTOR_STATE` rows *"have no observing writer"* and are declared by the actor being described |
| **Status** | `ACCEPTED`, `acceptance_is_not_adoption: true`, held | `PROPOSED`, `normative: no`, `authority: none`; held as candidate by DEC-20260822 Option B |

**The stage row is the load-bearing difference.** C-9 governs what a transition *leaves*; the
reconstruction governs what must be legible *before* one is attempted. Neither reads the other's
artifacts in the ordinary case.

---

### 2 · Concept overlap

A coarse signal first — occurrence counts, `grep -ci`, over both full texts. **Frequency is not
treatment**, so each row is adjudicated qualitatively below the table.

| Concept | C-9 | ORCH | Signal |
|---|---|---|---|
| `state` | 51 | 38 | both — different referents |
| `transition` | 41 | 9 | **C-9 dominant** |
| `field` | 33 | 7 | **C-9 dominant** |
| `identity` / `identifier` | 19 | 4 | C-9 dominant, but the sharpest true intersection |
| `owner` / `writer` | 18 / 12 | 11 / 7 | both |
| `ledger` | 17 | 9 | both — different ledgers |
| `event` | 19 | 11 | both — different resolvability (see below) |
| `roster` | 4 | 3 | both, lightly |
| `actor` | 19 | 37 | ORCH dominant |
| `authority` | **1** | **20** | 🔴 **near-total separation** |
| `H.1` | **1** | **25** | 🔴 **near-total separation** |
| `dispatch` | **0** | **30** | 🔴 **disjoint** |
| `routing` / `route` | **0** | **5** | 🔴 **disjoint** |

**Per-concept adjudication.**

- **state — overlapping word, disjoint referent.** C-9's `state` is the *semantic class of one
  recorded assertion* (STATIC / DERIVED / TRANSITIONAL × TRACKED / COMPUTED / UNTRACKED). ORCH's
  `*_STATE` groups are *subject-matter groupings of things a dispatcher must read*. These are
  **orthogonal partitions of overlapping material**, not competing ones: a field inside
  `ACTOR_STATE` may be STATIC, DERIVED or TRANSITIONAL under C-9. They do not contradict; a
  reader would have to hold both, and could mistake `ACTOR_STATE` for a C-9 class.
- **object identity — the sharpest real intersection, and it is not merely adjacent.** C-9 §2.1c
  defines an `IDENTIFIER` by a **refusal test**: *"a binding name is one that an approval, a gate
  or a freeze cites, such that a different value produces refusal rather than update."* ORCH §2.1
  and Q-2 ask what identifies a **dispatched** object. See finding **B-1** below — these are
  coupled by construction, not by topic.
- **transitions — 🔴 three senses of one word now in play.** A.5 and J.2 define *transizione* as
  *evento (J.1) + roster durevole*. C-9 uses *transition* for a **state change of a field** and
  builds §5–§6 on it. ORCH names a `TRANSITION_CHECK` that checks **dispatch preconditions** and
  performs no transition in J.2's sense at all. ORCH §0.1 already flags *transition* as external
  vocabulary — but flags it against the **annexes**, not against C-9. **The collision between the
  two candidates' usages is recorded in neither document.**
- **events — 🔴 not blocked by the same absence, contrary to the natural reading.** Measured this
  session: `ledger/events/` exists on **0 of 43 refs** (REPOSITORY-WIDE, re-measured, reproducing
  ORCH §2.4). But C-9 §6.1's resolver requires only *"a declared durable location"*, and its own
  worked example resolves **today**: `RES-20260816-GOV311-001` is line 3 of
  `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` on `main`, carrying `RESOLUTION_ID`, `STATE`,
  `RESOLVED_BY`, `RESOLVED_AT`. **C-9's resolver is satisfiable now for the governance-status
  class of events. ORCH's `what closed what?` is not satisfiable at all.** Scope of that claim,
  stated so it is not over-read: satisfiability was verified for **one** event id in **one**
  class. For capability and actor-lifecycle events C-9 §7.3 *proposes* `ledger/capabilities/`,
  which this session measured on **0 of 43 refs** — so for those classes C-9's resolver is as
  unsatisfiable as ORCH's.
- **roster — complementary, same object.** C-9 §7.2 *classifies* the roster and records that
  `runtime/` is untracked at standing cost C-5b. ORCH §2.2 *measures* that the roster's readiness
  rows are self-declared. Classification and audit of one object, from two sides.
- **authority — 🔴 no overlap.** 1 mention against 20; 1 `H.1` against 25. C-9 assigns *writers by
  class*; it never allocates decision authority. ORCH routes *decisions by H.1 row* and classifies
  nothing. **Different keys into different tables.**
- **routing — disjoint.** C-9: zero occurrences. Not a shared concern in any degree.
- **ledger — overlap of kind, not of object.** C-9 §7.3 proposes `ledger/capabilities/`,
  writer-named + consolidated, tier-2 freeze. ORCH §2.4 measures `ledger/events/` absent and
  `OWED NOT BARRED`. Two different ledgers, both under `ledger/`, only one of which has a stated
  naming discipline. Collision candidate, §4 below.

---

### 3 · Architectural layers

The dispatch offered an example and instructed that it not be assumed correct. **It was tested,
and it is approximately right with one misleading implication.**

> Offered: C-9 = *what is the durable state model?* · Reconstruction = *how is current state
> reconstructed and evaluated?*

The implication that misleads is that **the reconstruction reads the state C-9 models**. It
largely does not. Of ORCH's four groups, `AUTHORITY_STATE` is read from **H.1 — a frozen matrix
C-9 never classifies and mentions once**; `DEPENDENCY_STATE` is read from queues, reviews and a
non-existent event ledger. Only `ARTIFACT_STATE` and parts of `ACTOR_STATE` are populated by the
kind of recorded field C-9 sorts. **A reader taking the example literally would expect a
writer/reader pair over one model. The measured relation is two models that touch on one surface.**

The layering the evidence supports instead:

```
C-9      ── WRITE-SIDE DISCIPLINE ──   a value is being recorded.
                                       What class is it? Who owns its next move?
                                       When is it re-examined even if nothing fires?
                                       UNIT: the field, scoped by its record.

ORCH     ── READ-SIDE PRECONDITION ──  an act is about to be attempted.
                                       Is every input legible, addressable, authorized?
                                       UNIT: the dispatch — an act, not a value.

SEAM     ── one surface only ──────    the ADDRESS of an object.
```

Different units (field vs act), different temporal relation to a transition (after vs before),
different keys (class vs H.1 row). **That is a layer separation, not a topical one** — and it is
what makes the single seam worth stating precisely rather than waving at.

---

### 4 · Collision analysis

Assessed against the four risks named in the dispatch. Verdicts are **measurements**, not
recommendations.

**Risk 1 · Two competing state models — NOT FOUND as competition; FOUND as vocabulary.**
ORCH proposes no classification of values and cannot compete with C-9's axes. What exists is a
second use of the word `state` on an orthogonal key (§2 above). The failure mode is a reader
misreading `ACTOR_STATE` as a C-9 class, not two models issuing contradictory verdicts on one
field. **No field was found that the two would classify differently — because ORCH classifies no
field at all.**

**Risk 2 · Two ownership models — NOT FOUND as contradiction; FOUND as an unmet precondition.**
F-13 correctly records that C-9 §5.1 answers much of Q-4. The refinement this record adds:
C-9 §5.1 assigns *actor lifecycle state (J.2) → orchestrator*, and ORCH §2.2 measures that
**readiness has no observing writer** — `LAST_SEEN` is actor-declared, `HEARTBEAT_CADENCE` is
PROVISIONAL and *"no heartbeat mechanism has ever run"*. So C-9 **names an owner for a field
nobody can currently observe**. That is not a conflict between the two documents; it is ORCH
supplying a measured precondition that C-9 §5.1 assumes and does not check. The two ownership
schemes key differently (class vs H.1 row) and were not found to collide.

**Risk 3 · Duplicate indexes — FOUND, as a live risk rather than a present fact.**
Both documents want an append-only ledger under `ledger/`; neither wants the same one. C-9 §7.3
sets a discipline for its own — writer-named files, a consolidated replay view, tier-2 freeze,
and a carve-out that must ship *"a permission **plus** a validator the LINT consumes"*.
`ledger/events/` is owed under J.1 and carries **no such discipline on the surveyed surface**.
Measured: `ledger/capabilities/` 0 of 43 refs; `ledger/events/` 0 of 43 refs; `ledger/` on `main`
holds `approvals`, `checkpoints`, `retirements`, `tasks`. **Neither exists, so nothing has
diverged yet.** The risk is that whichever is built first sets a convention the second inherits or
contradicts, and the two documents are held separately with no record that they share a parent
directory.

**Risk 4 · Conflicting lifecycle definitions — FOUND, and it is convergent, which strengthens it.**
Two instances:
1. **Three senses of `transition`** (§2 above), one of them introduced by each candidate.
2. 🔴 **Both documents independently arrive at the same unresolved `BLOCKED` question.** C-9 §14
   records the J.2/A.5 overlap as a non-blocking observation and **puts it out of scope**:
   *"Whether one actor blocked on one task is the same fact recorded twice, or two facts that can
   legitimately disagree, is a question about the frozen text rather than about this model."*
   ORCH reaches the same gap from the other side at Q-3: *"Does a dispatch block map onto A.5
   `BLOCKED`, or is it a pre-task state?"* **Two authors, two directions, one gap, and each
   declines it as belonging to the other's territory or to the frozen text.** Convergence from
   independent starting points is stronger evidence that the gap is real than either mention
   alone — and it is currently owned by nobody.

---

### 5 · Complementarity test

**Could both coexist? On the measured evidence: yes — and the coexistence is not free, because
they are coupled at one point in a way not previously recorded.**

The boundary that the evidence supports, offered **as a description, not as a rule**:

```
C-9    classifies any value ALREADY RECORDED: class, owner, next_review.
         Supplies: no dispatch check, no authority allocation, no routing.
ORCH   establishes whether an ACT NOT YET PERFORMED has legible inputs.
         Supplies: no field class, no writer assignment, no ledger schema.
SEAM   the address of an object — bidirectional, and NOT a two-body problem:
         framework/protocols/cross_session_transport.md § 8 already refuses on
         "exists at the named commit", procedurally, in force, cited by neither.
```

#### 🔴 B-1 · The coupling at the seam — a mechanical dependency, in both directions

This is the finding this record adds to F-13, which measured the overlap as *near-neighbours* and
stopped there.

**Direction 1 — C-9's refusal test does not return a single answer for a dispatch address.**
C-9 §2.1c admits a name to `IDENTIFIER` status **only if something refuses when it changes**.
Applied to a dispatch address, that test splits, because the repository contains a refusal of one
kind and not of the other.

> **A correction to this record's own first pass, kept rather than smoothed.** The measurement
> was first run over executables alone and returned *nothing refuses on a dispatch address*. That
> statement is **false as written**, and the falsifier this record declared for itself is what
> caught it — the third one, *"a normative document that makes a dispatch address binding without
> any executable enforcing it"*. It fired on the first test. The corrected finding is below and is
> stronger than the one it replaces.

| | Executable refusal | Procedural refusal |
|---|---|---|
| **Exists for a dispatch address?** | 🔴 **no** | ✅ **yes** |
| **Evidence** | Swept every `.py` / `.sh` / `.js` / `.yaml` / `.yml` / `.json` / `.toml` file on `main`. Complete `handoff` hit list: `framework/scripts/surface_census.py` (a comment classifying corpus material, line 140), its test, `scripts/test_fresh_clone_reader_journey.py`, and five `ledger/` + `release/` **records** — no validator among them. `candidate_content_hash.py` binds *candidates*; `legend_lint.py` does not mention `handoff` or `dispatch` at all | `framework/protocols/cross_session_transport.md` § 8: `HANDOFF ESTABLISHED` is a six-term conjunction whose **term 1 is *"the DURABLE ARTIFACT exists at the named commit"*** and term 2 *"its binding (hash / digest) is valid where one exists"*, with *"If any term is absent: `HANDOFF NOT ESTABLISHED`"*. § 9 adds *"IF no unique target → ROUTING: BLOCKED. Fail closed."* |
| **Character** | — | The protocol declares `ENFORCEMENT MODE: PROCEDURAL`, *"no validator runs at send time"*, and 🔴 *"This is procedural discipline and it is not an enforced invariant."* It nevertheless asserts the refusals bind: **_"Those five lines bind now, because they are refusals and a refusal needs no mechanism."_** |

**So the answer turns on a question C-9 does not settle: does §2.1c's refusal test require a
mechanism, or does a procedural refusal qualify?** C-9's three worked examples are *all*
executable — `BASE_HEAD` → gate 5, `CANDIDATE_CONTENT_HASH` → gate 5, `PRIOR_ART_*_SHA256` →
`BYTE_IDENTITY`. **The clause was written against enforced gates and never tested against a
protocol that claims a refusal needs no mechanism.** Read narrowly (mechanism required), a
dispatch address binds nothing → assertion → `TRANSITIONAL`, needing an owner and a review date.
Read broadly (procedure suffices), `cross_session_transport` § 8 term 1 already makes it an
`IDENTIFIER` → immutable, outside the semantic axis, **and C-9's §6 four-field form must not be
applied to it.** Opposite remedies, again.

**Direction 2 — ORCH's Q-1 determines what C-9's test returns.**
ORCH Q-1 asks whether a `TRANSITION_CHECK` is *a gate, an advisory, or a report*. That is exactly
the refusal criterion C-9 §2.1c depends on:

| If Q-1 resolves to… | Does anything refuse? | C-9 class of a dispatch address |
|---|---|---|
| **a gate** | yes, **executably** — satisfies §2.1c on either reading | **`IDENTIFIER`** — outside the semantic axis, immutable, *"a gate refuses rather than reconciles"* (§4.1 role B) |
| **an advisory or a report** | no new refusal; only the **procedural** one already in `cross_session_transport` § 8 | 🔴 **undetermined** — `IDENTIFIER` on the broad reading of §2.1c, `TRANSITIONAL` on the narrow one |

**So the same value lands in two different C-9 classes depending on the answer to an ORCH open
question — and the two classes have opposite remedies.** One is immutable and refuses on
mismatch; the other is mutable, needs a named owner and goes stale by neglect, which is the
precise failure C-9 §1 exists to prevent.

**Consequence, stated as an observation and not as a recommendation:** adopting ORCH §3
`TARGET_EXISTS` as a **gate** would change the C-9 class of every dispatch address in the
repository, and neither document says so. This is a stronger statement than *near-neighbours*:
the two are not merely adjacent contracts over a shared location, they are **a test and its own
missing input**. Q-1 belongs to the operator (ORCH says so); Q-2 belongs to Plan (H.1
`Integrazione strutturale`, per DEC-20260822). **Neither can be answered correctly without the
other's answer**, which is a sequencing fact — and sequencing is not performed here.

🔴 **And the coupling has a third leg neither proposal reaches: `cross_session_transport` § 8.**
That protocol already refuses on *"the DURABLE ARTIFACT exists at the named commit"* — which is
ORCH's `TARGET_EXISTS` question, **already asked, already fail-closed, already in force, and
procedural.** Neither candidate cites it: `cross_session_transport` appears nowhere in either
document's text. So the seam is not a two-body problem between two held candidates. It is a
three-body problem in which **the third body is already binding**, and a `TARGET_EXISTS` gate
designed without reference to it would be the second fail-closed check over the same fact.

#### What the complementarity test does *not* establish

- It does **not** establish that both *should* coexist. Coexistence being possible is not
  coexistence being right, and the choice among A/B/C/D is not made here.
- It does **not** establish that the boundary above is the correct one. It is the boundary the
  measured evidence supports; it has had no review.
- It does **not** dissolve F-13's warning. *"Resolving either without the other would create the
  divergence both are trying to prevent"* is **strengthened** by B-1, not weakened: B-1 exhibits
  the mechanism by which the divergence would occur.

---

### 6 · Open questions

Listed. **Not answered** — several are governance questions this record has no authority over,
and the dispatch forbade deciding in any case.

**Carried forward unchanged from the objects themselves**

- **Q-10** (ORCH) — *what is the relationship between these two files?* Open. This record supplies
  evidence toward it and selects nothing.
- **Q-1** (ORCH) — gate / advisory / report. *Owner: operator.* 🔴 **B-1 raises its cost**: it is
  not only a normative fork, it silently determines a C-9 class.
- **Q-2** (ORCH) — what identifies a dispatched object. *Owner: Plan, subject to review.*
  🔴 **B-1 shows it is not independently answerable**: C-9 §2.1c answers it only once Q-1 is known.
- **Q-4** (ORCH) — who writes actor readiness. Partly answered by C-9 §5.1 (F-13); **the instrument
  the answer presupposes does not exist** (§4 risk 2).

**Newly registered by this analysis**

- **N-1** — Which sense of `transition` governs, given three now in play (A.5/J.2 *transizione*,
  C-9's field-state change, ORCH's `TRANSITION_CHECK`)? Recorded in neither candidate.
- **N-2** — Does `ledger/` need a stated convention **before** either `ledger/capabilities/` or
  `ledger/events/` is built? Both are absent on 43 refs; the first built sets the precedent.
  C-9 §7.3 states a discipline for one; J.1 states none for the other.
- **N-3** — Who owns the J.2/A.5 `BLOCKED` overlap? C-9 §14 declines it as *"about the frozen
  text"*; ORCH Q-3 declines it as unanswered. **Convergently identified, unowned.**
- **N-5** — 🔴 **A measured negative in ORCH § 0.1 may not hold, and the object is held where it
  cannot be repaired.** ORCH § 0.1 states of `handoff`: *"no schema, no required fields and **no
  state effect** are specified for it anywhere on the surveyed surface"*, and Q-6 states *"B.2
  names it and specifies nothing."* But `framework/protocols/cross_session_transport.md` § 8 — on
  `main`, inside ORCH's own declared surface (`base_head 2bb27005`) — specifies exactly a state
  effect: a six-term conjunction yielding `HANDOFF ESTABLISHED` / `HANDOFF NOT ESTABLISHED`, with
  required terms and a fail-closed routing rule. Verified this session: the string
  `cross_session_transport` appears **0 times in ORCH and 0 times in C-9**.
  **The distinction that could rescue the claim, stated fairly:** ORCH's subject is Annex B.2's
  *message type*, and § 8 governs the *act* of handoff rather than a message schema — so
  *"no schema"* may stand while *"no state effect"* does not. 🔴 **This record does not adjudicate
  that.** Plan is not the reviewer of this object, the object is held under Option B, and
  `REV-ORCH-STATE-RECONSTRUCTION-001` is closed with an `AUTHOR_RESPONSE` still outstanding.
  Registered here so it reaches the author, not resolved here. *Owner: the author, via the
  outstanding `AUTHOR_RESPONSE`; adjudication is Mirror's row, not Plan's.*
- **N-4** — 🔴 **C-9's own revision number is ambiguous inside the object.** Frontmatter reads
  `revision: 3` (line 4) and the title reads *"revision 3"* (line 26), while the lineage reads
  *"rev 4 @ this commit — CLOSING PATCH"* (line 16) and §15 reads *"C-9 closes at revision 4"*
  (line 687). **C-9 cannot currently be cited by revision without ambiguity.** Registered because
  it bears directly on this record's dimension 2 (object identity) and because it is, precisely,
  a transitional field that a transition failed to carry — the defect C-9 models, in C-9. Not
  repaired here: C-9 is held, and editing a held candidate is not analysis.

---

## ARTIFACT

```
CREATED   learning/plan/SLR-plan-C9-STATE-RECONSTRUCTION-BOUNDARY-001.md   (this file, 1 file)
MODIFIED  none
DELETED   none
```

**Naming deviation, recorded.** `learning/plan/` holds 19 records on the pattern
`SLR-plan-NNNN[-COR-NNN].md`. The dispatch specified this filename literally, so it was followed
rather than renumbered to `SLR-plan-0015`. Flagged so the sequence is not later read as having a
gap or a stray.

---

## VALIDATION

| Constraint | Result | How verified |
|---|---|---|
| Only `learning/plan` changed | ✅ | one new untracked file; `git status --porcelain` shows nothing else |
| No governance change | ✅ | `governance/` untouched; both proposals read via `git show` / `sed`, never opened for write |
| No roles change | ✅ | `roles/` untouched and not read as authority |
| No framework change | ✅ | `framework/` untouched |
| No ledger change | ✅ | `ledger/` read-only; the approvals queue was read to verify one event id resolves, never appended to |
| Neither proposal modified | ✅ | C-9 blob `d2ada5bc` unchanged at HEAD; ORCH blob `e6af7e3d` on its own ref, never checked out |
| No decision taken | ✅ | no A/B/C/D selection; Q-10 open; nothing merged, sequenced or released from hold |
| `main` unchanged | ✅ | `main` @ `2bb27005`, not written to and not an ancestor of this branch |

---

## WHAT THIS RECORD DID NOT DO

- It did not decide whether the proposals are duplicates, layers, subsuming or unrelated.
- It did not merge, sequence, adopt, reject or release either proposal from hold.
- It did not resolve Q-1, Q-2, Q-4 or Q-10, and did not answer N-1…N-5.
- It did not repair N-4, the C-9 revision ambiguity, though the defect is in a file at this HEAD.
- It did not adjudicate N-5. Finding a possible defect in a held object under review by someone
  else is not a licence to rule on it; it is registered for the author's outstanding
  `AUTHOR_RESPONSE` and for Mirror's row.
- It did not discharge the outstanding `AUTHOR_RESPONSE` to `REV-ORCH-STATE-RECONSTRUCTION-001`,
  which remains absent and which C.2 makes obligatory on the author, not on Plan.
- It did not ratify or contest any finding of that review; F-13's two rows were reproduced and
  extended, and F-7 through F-12 were not examined.
- 🔴 **It did not have its own central finding reviewed.** B-1 is one session's derivation from
  two held documents, and it has already been wrong once inside this record.

  **The falsifier that fired.** Three falsifiers were declared against B-1's first form: a refusal
  on a ref other than `main`; a refusal in a file type outside the swept extension set; or a
  normative document binding a dispatch address with no executable enforcing it — since C-9 §2.1c
  admits *"an approval, a gate **or a freeze**"*, and a freeze can be textual. **The third fired
  on the first test**, and B-1's flat negative was replaced by the two-reading split now in § 5.
  The finding survived because the falsifier was written down and then actually run — not because
  the first measurement was sound. **This is the third instance in this review chain of a negative
  that dissolved on re-measurement**, after the object's `\b` regex (ORCH § 0), the reviewer's
  working-directory sweep (REV § C-3) and the operator's heading-anchor miscount (DEC), and it is
  further corroboration of ORCH § 1.4 rather than an exception to it.

  **Falsifiers still standing against B-1 in its corrected form:** an executable refusal on a
  dispatch address existing on a ref other than `main`; or a governed reading of C-9 §2.1c that
  settles the mechanism-vs-procedure question one way, which would collapse the split back to a
  single answer and make the coupling one-directional rather than mutual.

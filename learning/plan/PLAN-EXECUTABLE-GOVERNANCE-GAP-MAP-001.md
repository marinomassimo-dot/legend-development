---
record_type: WORK_ANALYSIS
record_id: PLAN-EXECUTABLE-GOVERNANCE-GAP-MAP-001
task_id: PLAN_EXECUTABLE_GOVERNANCE_GAP_MAP_v1
title: What LEGEND declares, what it specifies, and what actually runs — a gap map, a roadmap
  re-baseline, and a queue nobody has to re-derive
author: plan
session_ref: evidence-index-cb [abbbc5]
authored_on: 2026-08-25
dispatcher: operator
governance_version: 3.1.1 — read and cited, NOT exercised and NOT modified
mode: ANALYSIS / PREPARATION ONLY

STATUS: ANALYSIS_COMPLETE
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none

classification:
  - EXECUTABLE-GOVERNANCE GAP MAP + ROADMAP RE-BASELINE + READY QUEUE
  - NOT GOVERNANCE · NOT A PROTOCOL · NOT A DECISION · NOT A CANDIDATE
  - NOT AN ACTIVATION — no `status:` line is changed by this record
  - NOT A DISPATCH — no actor is assigned work here
  - DECISION-NEUTRAL on §P7 and on cross_session_transport.md normativity

relation_to_prior: >
  CONSUMES and does not re-derive: PLAN-MIRROR-V3-MINIMUM-REPAIR-CONSOLIDATION-001 (M3-1…M3-15),
  PLAN-J3-QUEUE-RECONCILIATION-001 (queue lineages), PLAN-EXECUTION-TRANSITION-001 (M1–M4, D-1…D-6),
  PLAN-SURFACE-MAP-QUEUE-CLOSURE-001, legend_operating_convention_v1.md (B.2.2, B.10),
  PLAN-WRITER-STATE-AND-COMMIT-PROVENANCE-001 (43cf690 authority),
  and, from `main`, DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE and
  SCIENTIFIC-PIPELINE-PREPARATION-001. SUPERSEDES NONE OF THEM.

domain: >
  CONTENT. `learning/` matches no declared CONTROL_PLANE_ROOT prefix (plan_defined_parameters.md
  § P5.1 — `governance/candidates/`, `ledger/`, `reviews/`), and P5.1 states `learning/` is content
  BY INTENT. This file therefore moves the CANDIDATE_CONTENT_HASH of any future candidate rebased
  onto it. Disclosed.

personal_data: none introduced. The human role is `the Operator` throughout.
---

# The gates that run are the ones nobody had to be told to run

> **Nothing here is medical advice.** Disease-level only; no individual-level record.
> **Nothing here is canonical.** This is Plan work-analysis. It originates no actor, no control
> plane, no schema, no annex and no threshold. It answers **no** H.1 question and **selects no
> option** on any open determination.

---

## 0 · OBSERVATION_SCOPE

Every negative in this record is scoped to this table. **A local NOT_FOUND is not a repo-wide
NOT_EXIST, and a worktree negative is not a repository negative.** Every ref-level negative below
is paired with a positive control that fires; where a control failed, that is recorded too.

### 0.1 · Derivation surface

| Fact | Value | How established |
|---|---|---|
| Derivation instant | measurement phase `2026-08-25T20:54Z → 21:10:37Z`; re-verification `21:20:57Z` | `datetime.now(timezone.utc)` |
| Worktree | `.claude/worktrees/evidence-index` | `pwd` |
| Branch / MEASURED_AT | `plan-orchsurf-r4-transcription` @ **`4be5a37`** for every measurement below | `git rev-parse` |
| HEAD at authoring close | **`eac6737`** — the branch advanced by 3 commits while this record was written | `git rev-parse` |
| 🔴 What moved in between | **exactly one path**: `learning/plan/PLAN-WRITER-STATE-AND-COMMIT-PROVENANCE-001.md`, in `addd7f1`, `6c8f70f`, `eac6737`, all another session's | `git diff --name-only 4be5a37 eac6737` |
| Re-verification at `eac6737` | LINT **PASS** · receipts **OK 128 chained** · anchors **PASS** · release gate **BLOCK ×5** → § 2.5 | the four scripts, re-run |
| Divergence vs `main` | **2 behind, 59 ahead** at `4be5a37` | `git rev-list --left-right --count main...HEAD` |
| The 2 commits I lack | `2bb2700`, `788c357` — two files, both read in full below | `git diff --name-only HEAD...main` |
| Ref population swept | **44 `refs/heads` + 6 `refs/remotes`**; **55 refs total** with the 5 `refs/tags` | `git for-each-ref` |
| Worktree population | **27** entries | `git worktree list` |
| Sweep positive control | `CLAUDE.md` present on **44 of 44** heads | required before any ref-level negative |
| Peer refs at this instant | `main 788c357` · `mirror 30b6f7b` · `orchestrator 1e2fabd` · `lettore 605fc5d` · `lettore-b 9a09590` · `lettore-c 5b1d6c2` · `legend-operating-convention-v1 9a13c49` · `orchestrator-surface f3cdc78` | `git rev-parse` |
| `legend_lint.py .` | **PASS** (1 `[INFO]`, CLAIM 010 background-only) | run on this tree |
| `fulltext_receipts.py verify` | **OK — 128 chained, tail anchored** | run on this tree |
| `growth_anchors.py check` | **PASS** — claims 39 · papers 70 · corpus 356 · literature 390 | run on this tree |
| `lease_state.py` | **ACTIVE by derivation: 0** — 5 records visible from this ref | run on this tree |
| `public_release_gate.py` | 🔴 **BLOCK_PUBLICATION · BLOCKS 1 · exit 2** at `4be5a37`; **BLOCKS 5** once this record's own first draft was on disk — § 2.5 | run on this tree, and on three clean `git archive` extractions (EG-15, § 4.4) |
| Working tree during measurement | **1 dirty entry**, another session's file, not touched here | `git status --porcelain` |

**Two peer refs moved during this session** — `mirror` `77be2f4 → 30b6f7b` and
`legend-operating-convention-v1` `a58af46 → 9a13c49`. No finding below is drawn from either ref's
current tip. Where a `mirror` fact is cited it is cited from an artifact already consumed at
`77be2f4`, and attributed.

### 0.2 · What I could NOT reach — declared, not inferred

- **The 55-PDF corpus.** `files/` is git-ignored and per-worktree. Nothing in this record depends
  on it.
- **`main` @ `788c357`'s two extra commits** were read out-of-tree via `git show main:<path>`, in
  full, not skimmed. They are `governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md`
  and `learning/orchestrator/SCIENTIFIC-PIPELINE-PREPARATION-001.md`. **The measurement surface of
  this record is therefore `HEAD` ∪ those two objects**, and that union is stated rather than
  implied because neither tree exists as a single ref.
- **Any biological proposition.** Nothing scientific was adjudicated, no current file was opened
  for writing, no receipt was written, no PMID was read.

### 0.3 · One instrument error, caught by its own control, recorded because it would have produced a false negative

The scientific-idleness measurement of § 3.6 was first run as `git log --all -- $C4`, with the four
current-file paths in a shell variable. **zsh does not word-split an unquoted parameter expansion**,
so all four paths arrived as one argument and the query returned `0` — the answer I expected. The
positive control (`same paths, no range`) also returned `0`, which is impossible, and that is what
exposed it. Re-run with `set --` and `"$@"`, the control returns **9** and the negative still
returns **0**. **The negative survived; the first run of it was worthless.** This is the same
family as the `"$r:path"` `:r`-modifier failure, and the rule that caught both is the same one: a
ref- or path-scoped negative is not reportable until a control over the same instrument fires
non-zero.

### 0.4 · What this pass mutated

**One act: this file was created.** No canonical file was opened for writing. No tracked file on
any other actor's branch was touched. No `status:` line anywhere was changed. No `ledger/`,
`runtime/`, `governance/` or `roles/` path was written. No lease was acquired. Write-seat
deconfliction for this working directory is recorded at § 6.3.

---

## 1 · METHOD

### 1.1 · The seven classes, and the one question that separates them

The classification does not ask *is this good*. It asks **what would happen if the rule were
violated right now**, and the answer partitions cleanly:

```
E1  NORMATIVE + EXECUTABLE + ENFORCED    a mechanism runs and refuses
E2  NORMATIVE + EXECUTABLE, NOT ENFORCED a mechanism exists; nothing guarantees it is invoked
E3  NORMATIVE ONLY                       the rule is specified; no mechanism exists
E4  EXECUTION PATH UNREACHABLE           rule and mechanism exist; the actor/lease/route does not
E5  NORMATIVE CONTRADICTION              two applicable obligations cannot both be satisfied
E6  IMPLEMENTED WITHOUT A NORMATIVE OWNER  behaviour runs; no surface governs it
E7  NO GAP                               a suspected gap, falsified, with the falsifier recorded
```

**E2 and E4 are the two that get conflated, and the difference decides the owner.** E2 is a wiring
job — someone builds a gate. E4 is not: the mechanism is finished and the *route to it* is closed,
so building more mechanism does nothing. Every E4 below terminates at an actor, a lease or a
determination, never at a missing script.

### 1.2 · Admission test — what makes a finding a repair rather than an improvement

A gap enters `MINIMUM_BACKLOG` only on a demonstrated instance of one of:

```
C1  violates a property LEGEND already declares or promises
C2  renders a foreseen transition non-executable
C3  permits a false PASS
C4  prevents a recovery, audit or provenance property already required
C5  creates a real normative contradiction
```

Everything else is `OPTIONAL / FUTURE` and is listed as such at § 2.4. **The point of the test is
to keep improvable things out**, and it excluded more than it admitted: § 2.4 holds five classes of
finding that are real and are not repairs.

---

## 2 · EXECUTABLE_GOVERNANCE_GAPS

### 2.1 · E1 — the properties that actually run, listed first so the map is not read as an indictment

These are the exemplars. Each is normative, executable, invoked by a gate, and covered by a test
that a CI runner actually runs (`scripts/run_release_regressions.py`, **56 suites**, with
`test_release_runner_verdict.py` checking that every tracked suite is in fact run).

| Property | Executable surface | Enforced at | Test in the runner | Verdict here |
|---|---|---|:--:|---|
| Structural registry integrity | `framework/scripts/legend_lint.py` | GATE 2; `BLOCK_BATCH_COMMIT` | ✅ | **PASS** |
| Full-text reading is a ledger fact, not a claim | `fulltext_receipts.py verify` — SHA-256 chain + tail anchor in the state manifest | consumed by the LINT | ✅ | **OK, 128 chained** |
| Growth anchors match what the tool measures | `growth_anchors.py check` — re-derives its own denominators | LINT-adjacent | ✅ | **PASS** |
| Candidate identity is a content hash, not a commit hash | `governance/scripts/candidate_content_hash.py` — **parses P5.1 rather than copying it** | GATE 5 | ✅ | reproducible |
| Nothing publishes with an identifier or a broken link | `scripts/public_release_gate.py` — fail-closed, **exit 2** on BLOCK | GATE 2 | ✅ | **BLOCK ×1** — see EG-15 |
| The lease singleton | `lease_state.py` — invariant, fatal in every mode | GATE 0 | ❌ | see EG-05, EG-06 |

🔴 **The pattern in the E1 column is worth naming, because it is the repository's own best
result.** Every property in that table became enforceable the moment someone wrote *a script that
derives the answer instead of a sentence asking a future reader to check*. `candidate_content_hash.py`
parsing P5.1 rather than restating it is the strongest instance: the executable form and the
governed form **cannot** disagree. Every E3 below is a place where that step was not taken.

### 2.2 · MINIMUM_BACKLOG — gaps that pass the admission test

Seventeen findings survived. Full records follow the summary.

| ID | Property | Class | Admits on | Blocks a promised property today? | Authority to fix |
|---|---|:--:|:--:|:--:|---|
| **EG-01** | Role-contract activation act | **E3** | C1 C2 C5 | ✅ all four contracts | Operator (H.1) |
| **EG-02** | Satisfied conditions, stale `status:` | **E5** | C3 C5 | ✅ P5.1 binds every candidate hash | Operator (H.1) |
| **EG-03** | `MIRROR_REVIEW` vocabulary vs GATE 3 | **E2** | C3 | ✅ GATE 3 | Operator, via P-8 |
| **EG-04** | `ONE_WRITER` has no executable form | **E3** | C3 | ✅ GATE 0 — **failed in production this session** | Plan (build) + Operator (gate) |
| **EG-05** | Lease population is ref-dependent | **E2** | C3 C4 | ✅ GATE 0 singleton | Operator (writer/route) |
| **EG-06** | Two governance tools have no test and no CI | **E2** | C3 C4 | ⚠️ silently | **Plan — today** |
| **EG-07** | §P7 event ledger specified, never built | **E3** | C1 C2 C4 | ✅ Mirror's primary surface | Plan builds; Operator decides emission |
| **EG-08** | The declared v3.2 path is unreachable | **E4** | C1 C2 | ✅ governance evolution | Operator |
| **EG-09** | `HUMAN_APPROVAL_QUEUE` — 3 lineages, no writer | **E6**+E2 | C3 C4 | ✅ approval provenance | Operator (D-1 / P-2) |
| **EG-10** | Control-plane artifacts have no route to canonical state | **E4** | C2 C4 | ✅ Annex C.2 author response | Operator |
| **EG-11** | Runtime inventory / Agent Card on 1 of 44 heads | **E4** | C2 | ✅ CLAUDE.md § 0 | Operator |
| **EG-12** | 0 VERIFIED capabilities; L2 suspended | **E4** | C2 | ✅ every Task Contract | Operator (lift C-9 hold) |
| **EG-13** | Review ladder unreachable at **both** ends | **E4** | C2 C5 | ✅ Annex C entirely | Operator |
| **EG-14** | A.6 checkpoint refusal has no reachable recovery | **E4**+E2 | C2 C4 | ✅ 19 of 19 Plan checkpoints | Operator; schema by Plan |
| **EG-15** | Two release suites red at HEAD, one file, one commit | **E1**⚠ | C2 | ✅ **GATE 2, from this branch, today** | **Plan — today** |
| **EG-16** | `roles/plan.md` contradicts a tracked script | **E5** | C5 | ⚠️ record only | folded into EG-01 |
| **EG-17** | The MAJOR-2 repair exists on 2 of 44 heads | **E4** | C5 | ✅ on `main` | Operator |

---

### EG-01 · The activation act is required, has no form, and has never been performed

```
PROPERTY_ID          ROLE_CONTRACT_ACTIVATION
NORMATIVE SURFACE    roles/{plan,orchestrator,scientist,mirror}.md line 7 (line 12 for scientist);
                     DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE, consequence 3
EXECUTABLE SURFACE   none
ACTOR / PRODUCER     Operator (H.1 — governance → Operatore)
RECEIVER / CONSUMER  all four actors, at every rehydration
GATE                 none. No gate reads a role contract's status
CLASS                E3 — NORMATIVE ONLY
```

**Positive evidence.** All four contracts carry, byte-identically in the operative clause,
`status: PROPOSED — binding once Mirror hostile review passes and the operator approves`.
`DEC-20260822` decided `OPTION B — ACTIVATION_NOT_CONFIRMED` and states in consequence 3 that *"a
new, explicit activation act is required … This record does not perform it, does not schedule it,
and does not specify its form."*

**Negative control, with its denominator.** Across **all 50 refs**:
`git log --all -S'status: ACTIVE' -- roles/` → **0**; `-S'status: BINDING' -- roles/` → **0**;
the same over `framework/protocols/` for `ACTIVE`, `BINDING`, `CANONICAL` → **0, 0, 0**.
**Positive control:** `-S'status: FROZEN' -- governance/` → **7**;
`-S'status: PROPOSED' -- framework/protocols/` → **3**. The search fires.

**Failure mode.** An actor rehydrates, reads its contract, and either (a) relies on it — which
`DEC-20260822` consequence 2 forbids — or (b) does not, in which case the `Plan may / must not`
clauses that define its perimeter are decorative and its perimeter comes only from H.1's
seventeen rows.

**Impact.** Measured, not asserted: every Plan record produced since 2026-08-22, this one included,
carries some form of *"no role contract relied upon."* That is the correct behaviour and it is also
the measurement — **the contracts have been routed around, in writing, by their own author.**

**Minimum repair surface.** One artifact under `governance/decisions/`, written by the Operator,
naming the four objects and the form of the act. **It is not a document Plan may draft on its own
behalf**: `roles/plan.md` is inside the set, and an actor preparing the instrument that makes its
own contract binding is precisely the move `REV-ROLES-MIRROR-001` § 8 declined to make.

🔴 **The condition, as written, has a measured obstacle nobody has removed.** The clause names *a
passing Mirror hostile review*. The only hostile review of these four objects as a set returned
**CHANGES_REQUIRED on three** and **no verdict on the fourth** (self-review prohibition). So the
named condition is not merely unmet — it is **failed on three and structurally untestable on one**.
Whoever prepares the act inherits both facts.

---

### EG-02 · Four objects whose activation conditions are satisfied still declare themselves non-binding — and one of them binds every candidate in the repository

```
PROPERTY_ID          SATISFIED_CONDITION_STALE_STATUS
NORMATIVE SURFACE    the four objects' own frontmatter status lines
EXECUTABLE SURFACE   for P5.1 only: governance/scripts/candidate_content_hash.py, which PARSES it
ACTOR / PRODUCER     Operator (H.1)
RECEIVER / CONSUMER  GATE 5 (P5.1) · every cross-session sender (XPORT) · every Scientist (modes)
GATE                 GATE 5 reads a hash computed under a rule whose file says it binds nobody
CLASS                E5 — NORMATIVE CONTRADICTION
```

| Object | Its own condition | Measured | `status:` today |
|---|---|:--:|---|
| `governance/plan_defined_parameters.md` | Mirror review passes · operator approves | ✅ `REV-P5DOMAIN-MIRROR-001` ACCEPT · `APR-20260819-P5DOMAIN-001` APPROVED · canonically executed at `04693e6` | `PROPOSED` |
| `framework/protocols/cross_session_transport.md` | canonical execution · Mirror ACCEPT · approval | ✅ `f70878d` — *"Cross-session transport becomes canonical"* · `APR-20260819-XPORT-001` APPROVED | `PROPOSED` |
| `framework/protocols/scientist_reading_modes.md` | canonical execution of SCIAB · Mirror · approval | ✅ all three, measured clause-by-clause in `SCIENTIFIC-PIPELINE-PREPARATION-001` § 3.3 | `PROPOSED` |
| `framework/protocols/controlled_benchmark_ab.md` | canonical execution of SCIAB | ✅ `4454fea` | `PROPOSED` |

**Why this is E5 and not merely E3, and the argument turns on exactly one file.** For the three
protocols, a stale status line is an inconsistency with no live consumer — nobody is currently
reading under them. `plan_defined_parameters.md` is different, and the difference is measurable:

- its own status line says it is *"normative once Mirror hostile review passes and the operator
  approves"* — i.e. **it binds nobody**;
- § P5.1 declares itself *"the single authoritative definition"* of the candidate content domain;
- `candidate_content_hash.py` **parses that section** rather than carrying a copy, so every
  `CANDIDATE_CONTENT_HASH` in the repository is computed under it;
- `DEC-20260822` — a binding operator determination — cites P5.1 as the authority for the domain
  classification of its own record;
- **eight canonical batch commits** bound their approvals to hashes computed under it.

Those obligations cannot both hold. Either P5.1 binds — and the status line is false — or it does
not, and eight approvals are bound to hashes computed under a rule that binds nobody. **The doubt
rule (§ 250, `dubbio persistente → MAJOR, fail-closed`) does not dissolve it: it says which way to
route it, not which limb is true.**

**Admission.** C5 directly; C3 because an approval bound under a non-binding hash rule is an
approval whose scope cannot be re-derived.

🔴 **What Plan may not do here, and this is the load-bearing constraint on the whole record.**
`DEC-20260822` refused to extend an approval into an activation *by analogy* and *"adopts no
general interpretation."* Ruling that a satisfied condition self-executes is exactly that move, on
a file Plan authored. **Plan measures the clauses. Plan does not rule on them.** § 5's `activation_state`
tool exists precisely so the Operator decides once, on printed facts, instead of a fourth record
deriving the same table by hand.

**Minimum repair surface.** One determination covering all four objects at once, plus a mechanism
(§ 5, M1.2) that prevents the class recurring. Repairing them one at a time reproduces the defect.

---

### EG-03 · GATE 3 reads a field whose declared vocabulary nothing conforms to

```
PROPERTY_ID          MIRROR_REVIEW_VOCABULARY
NORMATIVE SURFACE    annex_d_commit_batch.md line 38 (FROZEN): `MIRROR_REVIEW: n/a | PASS | FAIL + REVIEW_ID`
                     body GATE 3: "Plan candidate → Mirror hostile review → MIRROR PASS → HUMAN_APPROVAL"
EXECUTABLE SURFACE   framework/scripts/artifact_index.py — REPORTS, gates nothing, exit 0 always
ACTOR / PRODUCER     Plan (writes the manifest) · Mirror (produces the verdict)
RECEIVER / CONSUMER  Orchestrator at GATE 3
GATE                 GATE 3 — asserted by hand
CLASS                E2 — EXECUTABLE, NOT ENFORCED
```

**Re-derived independently this session**, by running the tool rather than reading the prior
finding: `artifact_index.py` reports `conforming: 0 of 10 carrying the field (14 in the class)`.
Values in the population include `PENDING`, `REQUIRED · NOT PERFORMED · NOT ASSUMED`,
`PASS_WITH_NOTES`, `REQUEST CHANGES`, and one full narrative sentence about the review *process*.
**`PENDING` and `REQUIRED` are scheduling states, not review outcomes.** The legal value `n/a` is
unused.

**Prior art, credited and not re-opened.** `legend_operating_convention_v1.md` § B.2.2.1 established
this at `0 of 9` (filename-scoped) and explained why 9 and 10 are both correct — the delta is
`APPROVAL-GOV311-DEVIATIONS.md`, which sits in `governance/candidates/` and derives to the CAND
class by path. **Conformance is 0 under every denominator I can construct.** My figure differs from
that record's because the population has grown, which is what a population-derived figure does; the
conclusion has not moved. Registered as **P-8** in that document's B.10 register.

**Failure mode — and it is not hypothetical.** `PASS_WITH_NOTES` **already carried a completed
canonical GATE 3**. A value outside the frozen vocabulary was read as satisfying *"MIRROR PASS"* by
a human, once, successfully. Nothing distinguishes that from the next reader treating
`REQUEST CHANGES` or `PENDING` as adequate, because **no validator looks at the field at all** —
`artifact_index.py` reports it and gates nothing, by design.

**Admission.** C3 — a false PASS at GATE 3 is available today and has a precedent.

**Minimum repair surface.** Not code first. The four options are already enumerated at P-8 (extend
the vocabulary · declare a mapping · declare that no disposition implies PASS · generalize the
existing scoped ruling), and **any mapping retroactively characterises a completed GATE 3**, which
is why the decision precedes the validator and not the reverse.

---

### EG-04 · `ONE_WRITER` is a GATE 0 condition with no executable form, and it failed in this working directory during this session

```
PROPERTY_ID          ONE_WRITER_PER_WORKING_DIRECTORY
NORMATIVE SURFACE    body § 258; GATE 0 (body line 238); Annex D.3
EXECUTABLE SURFACE   NONE
ACTOR / PRODUCER     every actor
RECEIVER / CONSUMER  Orchestrator at GATE 0; Plan at reconciliation
GATE                 GATE 0 — one of five conditions, and this is the one nothing derives
CLASS                E3 — NORMATIVE ONLY
```

**Negative control, with its denominator.** `grep -rln 'ONE_WRITER' --include='*.py' .` → **0 files**.
**Positive control:** the same grep for `CONTROL_PLANE_ROOTS` → **3 files**
(`artifact_index.py`, `candidate_content_hash.py`, `test_candidate_content_hash.py`). The grep fires.

**Failure mode, observed — not modelled.** Three sessions named `evidence-index-*` held the same
working directory during this session. The conflict was detected by one of them **sending a chat
message**, and resolved by agreement in chat. Before that agreement was reached, one session had
already committed three files belonging to another session's uncommitted work, under a preservation
blocker that existed only in a third session's messages — measured by that session across all refs,
with a positive control, as present in **zero refs and zero files**. The full account is
`learning/plan/PLAN-WRITER-STATE-AND-COMMIT-PROVENANCE-001.md` § 4, and its conclusion is the exact
statement of this gap: *"every control governing the situation lived in prose."*

**Impact.** GATE 0 can be asserted `PASS` in a root that has two writers, because nothing in the
repository can see the second one. J.0 already declares the compensating protocol for the *lock*
LEGEND does not have; it declares no compensation for **ONE_WRITER**, which is listed as a GATE 0
condition and not as a missing guarantee.

**Minimum repair surface.** A durable per-working-directory writer record plus a check that reads it
— the shape `PLAN-WRITER-STATE-AND-COMMIT-PROVENANCE-001` § 4 names. **Buildable by Plan without any
determination**, as a report. Wiring it into GATE 0 is a gate change and is not.

---

### EG-05 · The lease singleton is derived over a population that differs by ref

```
PROPERTY_ID          LEASE_POPULATION_REF_DEPENDENT
NORMATIVE SURFACE    Annex I.3; GATE 0 (`ORCHESTRATOR_LEASE ACTIVE singleton`); Annex D.3
EXECUTABLE SURFACE   framework/scripts/lease_state.py — reads exactly ONE file, the checkout's
ACTOR / PRODUCER     orchestrator ONLY, from the orchestrator worktree (the record's own writer rule)
RECEIVER / CONSUMER  every actor, from every checkout
GATE                 GATE 0 — this is its one MECHANIZED clause
CLASS                E2 — EXECUTABLE, NOT ENFORCED (over the right population)
```

**Measured.** `runtime/orchestrator_lease.md` resolves to exactly **two distinct blobs** across the
44 heads: `c34f4866…` on **22 heads including `main`**, and `d8a2b47b…` on **1 head, `orchestrator`**.
Counting `ACTIVATED_AT` occurrences: **6 vs 10** (5 lease records vs 9, plus one template each).
Running the derivation over each:

```
this ref (5 records)          ACTIVE by derivation: 0   + 2 findings on lease #3
orchestrator (9 records)      ACTIVE by derivation: 0   + the same 2 findings, exit 1
```

The most recent canonical batch on `main` (`04693e6`) declares in its GATE 0 block that it acquired
and used **lease #9**. **That row does not exist on `main`.**

**Failure mode.** The derivation is correct and the population is not. An actor consulting the lease
from any of the 22 heads carrying the short lineage sees five terminal records and derives
`ACTIVE: 0` — which is the same answer it would derive if lease #10 were ACTIVE and recorded where
lease #6…#9 are. **The invariant the tool enforces fatally is computed over whatever the current ref
happens to contain.**

**This is not a new discovery and it is not a surprise to the governance.** P5.1 states it
explicitly: *"the row recording a lease can therefore never sit inside the batch that lease
authorized, so `main`'s copy of this record lags by at least the current lease, permanently"*, and
concludes that Annex I.3's `DETECTION` — *"doppio record sulla stessa successione"* — *"is therefore
weaker than a tracked home suggests."* **What is new here is the number: the lag is not one lease.
It is four.**

**Admission.** C3 and C4.

**Minimum repair surface.** Not a script. The lease needs either a single declared canonical ref
that every actor reads, or a consolidation route — and both are the same question EG-09 and EG-10
ask about `ledger/`. **The three should be decided together or the fix will fork again.**

---

### EG-06 · The two tools that mechanize GATE 0 and A.6 have no test and are in no CI suite

```
PROPERTY_ID          UNTESTED_GOVERNANCE_TOOLS
NORMATIVE SURFACE    GATE 0 (lease singleton) · Annex A.6 (fingerprint = resume compatibility) · H.2
EXECUTABLE SURFACE   framework/scripts/lease_state.py · governance/scripts/governance_fingerprint.py
GATE                 GATE 0; A.6's refusal rule
CLASS                E2 — EXECUTABLE, NOT ENFORCED (no regression protects it)
```

**Measured over an enumerated population of 8 governance-relevant tools**, each asked two questions
— does a `test_*.py` exist, and is it listed in `scripts/run_release_regressions.py`:

| Tool | test exists | in the release runner |
|---|:--:|:--:|
| `candidate_content_hash.py` | ✅ | ✅ |
| `artifact_index.py` | ✅ | ✅ |
| `legend_lint.py` | ✅ | ✅ |
| `fulltext_receipts.py` | ✅ | ✅ |
| `growth_anchors.py` | ✅ | ✅ |
| `public_release_gate.py` | ✅ | ✅ |
| 🔴 `lease_state.py` | **NONE** | **0** |
| 🔴 `governance_fingerprint.py` | **NONE** | **0** |

**6 of 8 are covered. The 2 that are not are exactly the two whose output a FROZEN gate consumes as
a boolean.** `lease_state.py`'s own docstring declares the singleton *"an invariant, not a finding …
checked in EVERY mode and always exits non-zero"*, on Mirror's blocking instruction. Nothing
re-verifies that claim after any edit.

**Falsification attempted, and it failed — recorded because it changes the finding's size.** I
probed for fail-open behaviour: `lease_state.py --home <nonexistent>` exits **2**, and
`public_release_gate.py` on a blocking tree exits **2**. Both are correctly fail-closed. My first two
readings said `exit=0` and were wrong — I was reading `$?` after a pipe, so I measured `tail` and
`grep`. **The tools are sound; what is missing is the regression that keeps them sound.**

**Admission.** C3 and C4 — a regression in either is invisible until a batch relies on it.

**Minimum repair surface.** Two test files, no governance, no determination. **This is the cheapest
item in the entire backlog and Plan can do it today** (§ 7, action 2).

---

### EG-07 · §P7 · The event ledger is fully specified, has 23 named types, and has never existed

```
PROPERTY_ID          EVENT_LEDGER_P7
NORMATIVE SURFACE    Annex J.1 (FROZEN) — schema, 23 minimum types, append-only-strict,
                     CLOSES_EVENT_ID, sovereignty clause;
                     plan_defined_parameters.md § P7 — option (a), path, format, view
EXECUTABLE SURFACE   NONE
ACTOR / PRODUCER     each actor, into its own file (option (a): one writer by construction)
RECEIVER / CONSUMER  Plan (consolidation, J.1 + roles/plan.md) · Mirror (G.3, primary surface)
GATE                 none today. J.1's DETECTION is "incrocio ledger ↔ stato durevole"
CLASS                E3 — NORMATIVE ONLY
```

**Negative, with its denominator and control.** `ledger/events/` and `ledger/consolidated/` are
present on **0 of 44 heads**. **Positive control:** `ledger/approvals/` resolves on **29 of 44** and
on `main`, `mirror` and `orchestrator` individually. Searched again in code:
`grep -rln 'ledger/events|ledger/consolidated|EVENT_LEDGER|EVENT_ID' --include='*.py'` → **0 files**;
the same strings in `*.md` → **14 files**, all of them specification or analysis. **23 event types
decided, 0 lines of code, 0 events emitted, on any ref, ever.**

**§ P7 already answered every design question.** Option (a) over option (b), with the reason
recorded: *"several event types in J.1's own minimum list leave neither [a commit nor an ACKed
message]: `CHECKPOINT_WRITTEN`, `ACTOR_DOWN`, `LEASE_STALE`, `HUMAN_REQUIRED_OPENED`,
`RESUMED_FROM_MILESTONE`. A ledger that structurally cannot record its own recovery events is
exactly the wrong instrument for Mirror."* Path, format and view are fixed. **This is not a design
gap. It is an unbuilt build.**

**And the debt is already declared eligible.** `CAND-20260816-GOV311` § 4 `PENDING_IMPLEMENTATION`
carries the row *"EVENT LEDGER writer + validator"* with the eligibility condition *"After canonical
commit, before the first scientific batch"* — canonical commit done (2026-08-16), first scientific
batch not started (§ 3.6). **Building it discharges a declared debt at its own stated threshold and
requires no new authorization. Emitting under it is a different act and does.**

**Admission.** C1 (Annex G.3 promises Mirror this surface), C2, C4.

**Minimum repair surface.** § 5 of this record — the decision-neutral readiness package.

---

### EG-08 · The declared route to governance v3.2 terminates in a surface that does not exist

```
PROPERTY_ID          V3_2_EVOLUTION_PATH
NORMATIVE SURFACE    Annex G.3 (FROZEN)
EXECUTABLE SURFACE   none — depends entirely on EG-07
CLASS                E4 — EXECUTION PATH UNREACHABLE
```

Annex G.3, verbatim: `MIRROR_RETROSPECTIVE ogni N batch — [v3.1.1] condotta primariamente
sull'EVENT LEDGER consolidato (J.1)`, and, closing the section:
**`Queste metriche sono la fonte esclusiva della futura v3.2 (freeze).`**

Three things follow, and the third is why this is carried separately from EG-07:

1. **AUTONOMY LEDGER** (`HUMAN_REQUIRED PREVENTABLE vs UNAVOIDABLE`, hours blocked, work continued
   during HITL, false escalations) derives from the ledger. Not computable.
2. **REVIEW YIELD** per ladder level, whose stated purpose is to *demote* a level whose yield is
   persistently null, derives from the ledger. Not computable — so no ladder level can ever be
   retired on evidence.
3. **`fonte esclusiva` is exclusive.** The one input the governance names for its own next version
   is absent, and no substitute is authorized. **LEGEND's declared evolution path is closed, and
   nothing in the repository says so.**

**Attempted refutation, and it held.** I put the third link to an independent Plan session as
possible over-reach. It reproduced all three measurements in its own hand and declined to break it:
*"'fonte esclusiva' is exclusive, the surface it names is absent, and nothing bridges them."*

**Admission.** C1, C2.

**Minimum repair surface.** None available below the Operator: either the ledger is built and
emitted (EG-07 + D-3), or G.3's exclusivity clause is amended, which is an amendment to a FROZEN
annex. **The honest interim is to record that v3.2 is not scheduled, rather than to treat it as
pending.**

---

### EG-09 · The approval queue has three lineages, no declared writer, and three out-of-enum states

```
PROPERTY_ID          HUMAN_APPROVAL_QUEUE_WRITER
NORMATIVE SURFACE    Annex J.3 — schema, STATE enum, "ogni HUMAN_REQUIRED crea un oggetto in coda"
EXECUTABLE SURFACE   none. § P7's one-writer decision covers ledger/events/, NOT ledger/approvals/
ACTOR / PRODUCER     🔴 UNDECLARED — J.3 names a requester and a resolver, and allocates no file writer
RECEIVER / CONSUMER  GATE 3; the DAILY_BRIEF's PENDING HUMAN DECISIONS
CLASS                E6 (writer) + E2 (enum)
```

**Re-derived independently this session**, by blob rather than by report:

| Blob | Lines | Refs | Contents beyond the shared prefix |
|---|:--:|---|---|
| `20c24a2b…` | 6 | **26 heads incl. `main`, `mirror`, this branch** | — (the prefix itself) |
| `bb603d9a…` | 10 | **1 — `orchestrator`** | SUNSET-DEC3 · SCIAB · XPORT · P5DOMAIN, dated 08-18/08-19 |
| `95fc8163…` | 14 | **2 — `evidence-index`, `p51c9-rebased-onto-c89c2217`** | HA-1…HA-4 + four resolutions, dated **08-17** |

**The two extensions are disjoint.** Both extend the same byte-identical 6-line prefix; neither
contains the other; **`main` carries neither.** The longer lineage is the *older* one — 14 lines
dated 08-17 against 10 lines dated 08-18/19 — so line count inverts chronology, and any reconciler
ordering by length would order it backwards. This confirms `PLAN-J3-QUEUE-RECONCILIATION-001` in an
independent hand, including its `0 key collisions`.

**Impact, stated as a number.** **12 operator approval records are invisible from `main`.** Among
them are the three approvals on which `PLAN-EXECUTION-TRANSITION-001` § 1(b) and
`SCIENTIFIC-PIPELINE-PREPARATION-001` § 3.3 rest their measurement that EG-02's conditions are
satisfied. **A reader who checks those claims against `main` alone will conclude they are false.**
`SCIENTIFIC-PIPELINE-PREPARATION-001` § 2.3 records making exactly that error mid-survey.

**The enum, separately.** J.3 declares `STATE: PENDING | APPROVED | APPROVED_WITH_MODIFICATION |
DENIED | REVISION_REQUESTED`. The 14-line lineage carries `DEFERRED` ×2 and `RESOLVED` ×1.
**Nothing validates the file** — its own `_schema` line concedes it *"is NOT the general queue
implementation, which remains PENDING_IMPLEMENTATION in the candidate manifest."*

**Failure mode.** A fourth lineage. Any reconciliation performed from a branch that is not the
destination creates one, which is the defect being repaired — the structural blocker
`PLAN-EXECUTION-TRANSITION-001` § 3.2 already names.

**Admission.** C3, C4. **Registered as P-2, and P-2 is the root of the B.10 dependency graph.**

---

### EG-10 · A control-plane artifact has no route to canonical state, and the Annex C.2 author response is sitting on one ref

```
PROPERTY_ID          CONTROL_PLANE_TRANSPORT
NORMATIVE SURFACE    P5.1 CONTROL_PLANE_ROOTS (governance/candidates/, ledger/, reviews/);
                     Annex C.2 "AUTHOR_RESPONSE (obbligatoria; il silenzio non è accettazione)"
EXECUTABLE SURFACE   none — a candidate structurally CANNOT carry these paths
CLASS                E4 — EXECUTION PATH UNREACHABLE
```

**The mechanism is a consequence of a correct rule.** `reviews/` and `ledger/` are control-plane
roots precisely so a reviewer's verdict cannot alter the identity of the object under review. The
correct rule has an uncorrected consequence: **`INTEGRATION_CANDIDATE` is the only route into
canonical state, and it excludes these paths by construction.** No second route is implemented.

**Measured instance, and it is the obligation the roadmap lists as outstanding.**
`reviews/plan/AUTHOR-RESPONSE-ROLES-MIRROR-001.md` **exists, is complete**, and disposes of all six
transmitted findings (`MAJOR-1 ACCEPTED, falsifier discharged · MINOR-1 ACCEPTED · MAJOR-2 ACCEPTED,
stands on main · MINOR-2 ACCEPTED · MAJOR-3 ACCEPTED with changed character · MINOR-3 CONTESTED IN
THE FORM TRANSMITTED, with evidence, and the true state is worse`).

It is tracked on **1 of 44 heads** — this one. **Positive control:** `reviews/plan/` is present on
**20 of 44**. It is not on `main`. It is not on `mirror`, where the reviewer reads.

**So the C.2 obligation is discharged in substance and undelivered in fact**, and both
`PLAN-EXECUTION-TRANSITION-001` § 6 (P2) and `DEC-20260822` consequence 5 still describe it as
outstanding — correctly, from where they were measuring.

**The route is named and has never run.** Commit `005888b`'s message says the approvals *"enter
canonical state by their own route, as a control-plane candidate, and not silently with this
commit."* Measured: `main`'s approval queue is still the 6-line prefix. **The control-plane candidate
route has been named at least once and executed zero times.**

**Admission.** C2, C4.

---

### EG-11 · CLAUDE.md § 0's first bootstrap condition is true on 43 of 44 heads by construction

```
PROPERTY_ID          RUNTIME_INVENTORY_REACHABILITY
NORMATIVE SURFACE    CLAUDE.md § 0; Annex I.2 step 5; Annex I.4 (Agent Card registry)
EXECUTABLE SURFACE   none
CLASS                E4 — EXECUTION PATH UNREACHABLE
```

CLAUDE.md § 0 is unconditional: `IF no valid runtime inventory / no ACTIVE ORCHESTRATOR_LEASE:
ENTER BOOTSTRAP_MODE.`

**Measured — every head carrying anything under `runtime/`:** 24 heads carry `runtime/` at all, and
**23 of them carry exactly one file**, `orchestrator_lease.md`. **One head — `orchestrator` — carries
the rest**: `runtime_inventory.md`, `agent_card_registry.md`, `L2-OUTCOMES.md`, three
`runtime/bootstrap/` records and the C-2 handoff. **Positive control:** `governance/` present on
**29 of 44**.

**Consequence.** The runtime inventory does not exist on `main`, on `mirror`, on any `lettore*`, or
on this branch. **Every session outside the `orchestrator` worktree satisfies § 0's first antecedent
by construction and is therefore in `BOOTSTRAP_MODE` permanently**, regardless of the lab's actual
state. That is not a description of an unhealthy lab — it is a measurement of where a file is.

**Admission.** C2 — every promotion path in Annex I.2 runs through an inventory nobody but one
worktree can read.

---

### EG-12 · No capability is VERIFIED anywhere, and the verification is under an operator hold

```
PROPERTY_ID          CAPABILITY_VERIFICATION
NORMATIVE SURFACE    Annex I.4 + body § 8 — "Orchestrator assegna sulle capabilities VERIFIED";
                     "CONFIGURED != PROVEN"
EXECUTABLE SURFACE   runtime/agent_card_registry.md (a record, not a mechanism)
CLASS                E4 — EXECUTION PATH UNREACHABLE
```

**Measured on `orchestrator:runtime/agent_card_registry.md`:** **21 capability rows. 21
`status: UNVERIFIED`. 0 `status: VERIFIED`.** `last_verified: NONE` on every row. Registry header:
`status: PARTIALLY REGISTERED — 3 of 6 cards raised from skeleton`.

`controlled_benchmark_ab.md` P-3 states the blocker in its own words: *"all UNVERIFIED; L2
**SUSPENDED** by the C-9 hold (operator, 2026-08-17) — this protocol does not lift it."*

**Consequence, stated plainly.** Annex I.4 makes VERIFIED capabilities the precondition for
assignment. Zero exist. **No Task Contract can be legitimately assigned to any actor today**, which
means M4's pilot, the first scientific batch, and every downstream milestone are blocked on a hold
that predates all of them by eight days.

**Admission.** C2.

**Minimum repair surface.** Lifting the C-9 hold, then one L2 session. **Neither is Plan's, and
neither is available to any actor: the hold is the Operator's and L2 requires an Orchestrator to
run the smoke.**

---

### EG-13 · The review ladder is unreachable at both ends, not just the exit

```
PROPERTY_ID          REVIEW_LADDER_REACHABILITY
NORMATIVE SURFACE    Annex C.3 — "Apertura solo via Orchestrator"; "max 2 round → adjudication";
                     H.1 — "Aggiudicazione challenge | Orchestrator"; C.1 floors
EXECUTABLE SURFACE   none required — the gap is the actor
CLASS                E4 — EXECUTION PATH UNREACHABLE
```

**Attribution, because this finding has two halves with two authors.** The **exit** half — *a cap
terminating in "→ adjudication" cannot bind when adjudication is unreachable* — is
`PLAN-MIRROR-V3-MINIMUM-REPAIR-CONSOLIDATION-001` § 3.2's surviving residue of M3-14, and is cited,
not re-derived. The **entry** half is derived here: C.3's first clause, `Apertura solo via
Orchestrator`, has the *same* unreachable actor. **The ladder cannot be opened either.**

**The unreachability, measured.** `lease_state.py` → `ACTIVE by derivation: 0`, five terminal
records, the most recent released `2026-08-18T14:05:20Z`. `roles/orchestrator.md` is `PROPOSED`
(EG-01), and per `DEC-20260822` consequence 2 no authority may be read from it. Annex I.2 gives
promotion to Orchestrator only through the bootstrap protocol, which runs through the runtime
inventory of EG-11 and the capability verification of EG-12.

**Impact.** Annex C is FROZEN and normative and binds independently of any role contract — and its
first procedural clause and its terminal clause both name an actor that no route currently reaches.
Every review conducted in the interim has been opened by something other than the mechanism C.3
names.

**Admission.** C2, C5.

---

### EG-14 · Every Plan checkpoint refuses to resume, and A.6's prescribed recovery terminates at EG-13

```
PROPERTY_ID          CHECKPOINT_RESUME_COMPATIBILITY
NORMATIVE SURFACE    Annex A.6 — "la rehydration che trova ... fingerprint incompatibili NON riprende
                     — segnala e chiede stato a Orchestrator" (pattern MAF)
EXECUTABLE SURFACE   governance/scripts/governance_fingerprint.py (E2 — see EG-06)
CLASS                E4 (recovery route) + E2 (no schema validator)
```

**Measured.** `governance_fingerprint.py compose --role plan` → `0d6987bd…` today. The 19 Plan
checkpoints in `ledger/checkpoints/plan/` carry:

```
c1d1a9cf…   CHK-0001 … 0005     (5)
37c3b863…   CHK-0006 … 0008     (3)
9c0c13fb…   CHK-0009 … 0014, 0017 … 0019  (9)
🔴 prose    CHK-0015, CHK-0016  (2) — "composed at session open over CORE + Annex D + E + I + J.1
                                       per plan_defined_parameters.md P2.2"
```

**19 of 19 are fingerprint-incompatible with the current composition. 2 of 19 are not even
evaluable**, because the field required by A.6 to be a hash contains a description of how a hash
would be produced.

**What is NOT the defect, stated so the finding is not inflated.** The drift itself is A.6 working
correctly: the composition inputs include `plan_defined_parameters.md` and `roles/plan.md`, both in
CORE, and P5DOMAIN legitimately amended the first. **A fingerprint that moves when pertinent
governance moves is the mechanism succeeding.**

**What IS the defect, in two parts.** (a) A.6's refusal rule is unconditional and its only
prescribed recovery is *"chiede stato a Orchestrator"* — the actor of EG-13. There is therefore
**no path from an incompatible checkpoint back to work**, and 19 of 19 are incompatible. (b) The
checkpoint schema is validated by nothing, which is how two records came to carry prose in a hash
field without anything noticing.

**Admission.** C2, C4.

---

### EG-15 · Two release suites are red at HEAD, both from one file, both since one commit — and one of them blocks GATE 2

```
PROPERTY_ID          RELEASE_SURFACE_REGRESSION_AT_702df73
NORMATIVE SURFACE    GATE 2 — "LINT PASS + publication gate PASS/0 nella stessa finestra"
EXECUTABLE SURFACE   scripts/public_release_gate.py:651 (pattern), :697–709 (scan loop)
                     scripts/test_documented_commands.py — in run_release_regressions.py:18
CLASS                E1 with two defects — both gates are correct, fail-closed and tested.
                     What is missing is that nothing ran them over the change that broke them
```

**Measured with a before/after control, on clean `git archive` extractions so no untracked file can
confound it — and the sweep found a second red suite I was not looking for:**

| Clean tree | `public_release_gate.py` | `scripts/test_documented_commands.py` |
|---|---|---|
| `43cf690~2` — before `702df73` | **PASS · BLOCKS 0 · exit 0** | **OK · exit 0** |
| `43cf690` | 🔴 **BLOCK_PUBLICATION · BLOCKS 1 · exit 2** | 🔴 **FAILED · exit 1** |
| `eac6737` — HEAD | 🔴 **BLOCK · BLOCKS 1 · exit 2** | 🔴 **FAILED · exit 1** |

**Two release suites went red at the same commit, and both findings are in the same file** —
`learning/plan/PATHOGRAPH-TRANSPORT-CONSOLIDATION-001.md`, one of the twelve Plan records that
V3 Action 7 tracked:

```
public_release_gate.py         :222   BROKEN_WIKILINK — the wikilink token, shown inline
test_documented_commands.py    :57    a pathograph script under framework/scripts — does not exist
                               :64    the same script named again                  — does not exist
                               :65    its companion test, same directory           — does not exist
```

> **The three names are described, not written.** Writing them would make *this* record the fourth
> and fifth findings of the same suite — which is exactly what the first draft did (§ 2.5, second
> instance). Reproduce with:
> `python3 scripts/test_documented_commands.py` — the failure output names all three in full.

🔴 **`test_documented_commands.py` is in the release runner at line 18. `run_release_regressions.py`
is therefore red at HEAD**, and has been since `702df73`.

**The second mechanism is a different defect from the first and shares its cause.** The wikilink
block is a scanner that cannot see code spans. The documented-commands failure is a record naming
three scripts that do not exist — the same guard, and the same shape, that commit `c964324`'s own
message records catching *"my own appendix naming seven scripts that do not exist."* **The guard
worked both times. What did not happen at `702df73` is that nobody ran it over the result.**

**Scope note, stated because it changes who this is about.** Action 7's brief was to track
previously-untracked Plan records, and it discharged that brief — including scrubbing 11 identifier
occurrences first, verified by an external sweep with a positive control. **Making a file tracked
makes it subject to gates it was never subject to before.** Neither suite was in that action's
acceptance criteria, and neither is a criticism of the scrub. It is a missing step: *tracking a
document is a change to the release surface.*

**Mechanism, read rather than guessed.** `public_release_gate.py:651` compiles a doubled-opening-
bracket pattern and `:697` runs `wikilink.finditer(text)` over the **raw file text**, with no
inline-code stripping. Line 222 of that record is prose *about* wikilink materialization: it states
that a registry mention carries no wikilink token, and it shows that token inline, inside backticks,
with an ellipsis as the placeholder target. **The scanner has no notion of a code span**, so it reads
the illustration as a live link to a page named `…`, which does not exist. There is a
`WIKILINK_EXAMPLES` allowlist at `:44` for illustrative targets — `file`, `DEEP_DIVE` and three
others — and the ellipsis placeholder is not among them.

> **Reproduce without reproducing the defect:**
> `sed -n '222p' learning/plan/PATHOGRAPH-TRANSPORT-CONSOLIDATION-001.md`
> This record deliberately does **not** quote that line verbatim. § 2.5 explains why it cannot.

**Why this matters more than one broken line.** The three publication blocks
`PLAN-EXECUTION-TRANSITION-001` § 0 recorded were `DIRECT_IDENTIFIER` findings **in an untracked
file** — a working-tree-only block that a clean checkout passed. Those are gone. **These are
tracked**, so they are present in a clean extraction, therefore inside the candidate content domain,
therefore **GATE 2 fails for any candidate cut from this branch.** The block's *class* changed, not
just its identity.

**It is also a recurring shape, not an accident.** A checker for syntax X blocks on any document
that discusses syntax X. The next Plan or Mirror record explaining wikilink materialization will
trip it again.

**Admission.** C2 — no candidate can be prepared from this branch until it clears.

**Minimum repair surface — three options, and they are not equivalent:**

| # | Repair | Class | Cost | Leaves the class open? |
|---|---|---|---|:--:|
| **a** | rewrite the prose so the token is described rather than shown | ordinary, Plan's own file | one line | **yes** |
| b | add the ellipsis placeholder to `WIKILINK_EXAMPLES` | gate allowlist | one line | yes, and it blinds the gate to a genuinely broken token of that exact shape |
| c | strip inline code spans before extraction | **MAJOR (fail-closed, § 250 doubt rule)** — it changes what a BLOCK-severity gate blocks on | ~10 lines + fixtures | no |

**Recommended: (a) now, (c) registered as a separate proposal.** (a) unblocks GATE 2 today at zero
governance cost; (c) is the only one that closes the class, and it routes through GATE 3 because
Plan does not self-adjudicate a change to what a gate blocks on. **(b) is rejected**: it converts a
correct block into a permanent blind spot.

🔴 **Routing note.** The blocking line is in a file committed at `702df73` by a different Plan
session. This record does not edit it. It is reported at § 7 and to that session.

### 2.5 · 🔴 EG-15's predicted recurrence fired inside this record, in the same session, against its author

§ 2.2's EG-15 entry closes with: *"The next Plan or Mirror record explaining wikilink
materialization will trip it again."* **The next such record was this one, and it did.**

The first draft of this file discussed the defect by showing the token inline, inside backticks,
exactly as the record it was describing had. Run against the working tree:

```
BLOCKS: 5
  learning/plan/PATHOGRAPH-TRANSPORT-CONSOLIDATION-001.md:222    ← the finding
  learning/plan/PLAN-EXECUTABLE-GOVERNANCE-GAP-MAP-001.md:781    ← this record, quoting the finding
  …:803  …:1053  …:1398                                          ← this record, discussing the repair
```

**One document about the defect added four instances of it.** The occurrences are removed above and
the prose now describes the token instead of showing it.

**This changes the sizing of option (a), and the correction is the point.** I had classed (a) as *"one
line, leaves the class open."* Trying it establishes something stronger: **there is no way to display
the syntax at all.** Every construction that puts the doubled opening bracket and the doubled closing
bracket in one text run matches the pattern — inside backticks, inside a fenced block, split across a
line break, or separated by a hyphen — because the extractor sees raw bytes and the character class
between the brackets excludes only `]`, `#` and `|`. The only compliant form is not to write it.

**So (a) is not "cheap but incomplete." It is a documentation prohibition**: the repository cannot
document its own wikilink convention inside the surface the gate scans. That is a real cost, it was
invisible until someone tried the repair, and it moves (c) from *nice-to-have* to *the only option
that restores the ability to describe the system*. **(a) still goes first — GATE 2 is blocked today —
but the proposal for (c) should carry this paragraph as its motivation, not a tidiness argument.**

**It fired a second time, against a different gate, in the same file, an hour later.** Having removed
the four wikilink instances, I wrote out the three non-existent script names that
`test_documented_commands.py` reports — in order to report them. The guard then named **this record**
as the source of three further findings. Same shape, different checker:

```
draft 1   4 findings   public_release_gate.py         — showing a wikilink token
draft 2   3 findings   test_documented_commands.py    — naming a script that does not exist,
                                                         in a sentence saying it does not exist
final     0 findings   both                           — every offending token described, not written
```

**So the class is wider than one scanner.** It is: *any guard that matches a literal pattern over
raw bytes fires on the document that reports its own findings.* Both guards here are correct and
both are load-bearing; neither has a notion of quotation. **The general rule the repository already
holds — exclude the record from its own reproduction command — is the mitigation, and it is
procedural.** Option (c) mechanizes it for one of the two.

*Recorded rather than quietly fixed, because a predicted recurrence that fires twice against its own
predictor, on two independent instruments, is the strongest available evidence that the class is
real. Verified at the close: this record contributes **0** findings to either suite.*

---

### EG-16 · `roles/plan.md` says a capability is blocked by a missing script, and the script runs

```
CLASS  E5 — NORMATIVE CONTRADICTION.  Re-derived, already ACCEPTED, remedy blocked upstream.
```

`roles/plan.md:73`: `| Fingerprint composition | emit a fingerprint for a named role — **blocked:
the composition is prose, not a script** | UNVERIFIED |`.
`python3 governance/scripts/governance_fingerprint.py compose --all` → four fingerprints, **exit 0**.

This is `REV-ROLES-MIRROR-001`'s MAJOR-1, spot-verified in `DEC-20260822` E-11, and already
**ACCEPTED with its falsifier discharged** in `AUTHOR-RESPONSE-ROLES-MIRROR-001`. It is carried here
only to record that the remedy — editing the contract — is inside EG-01's blocked perimeter, and that
the author response saying so is inside EG-10's undelivered one. **Two gaps stand between an accepted
finding and its one-line fix.**

---

### EG-17 · The MAJOR-2 repair exists on 2 of 44 heads; the contradiction stands on `main`

```
CLASS  E4 — EXECUTION PATH UNREACHABLE
```

**Measured with a braced per-ref sweep** (the unbraced form silently returns ABSENT on every ref in
zsh — recorded at § 0.3's family):

- `worktree: the repository root checkout` → **27 heads, including `main`**
- `worktree: orchestrator` → **2 heads: `orchestrator-surface`, `plan-orchsurf-r4-transcription`**
- `roles/orchestrator.md` present on **29 of 44** (positive control)

On `main`, line 5 still reads `worktree: the repository root checkout` and line 46 still reads
`**Orchestrator must not:** commit its own work;` — without the `to the canonical surface`
qualifier that resolves it. The repaired revision adds `session_home`, `canonical_batch_surface` and
the four-concepts section, and quotes the operator's adjudication of 2026-08-20 verbatim.

**Why it is stuck.** The repair travels in `CAND-20260819-ORCHSURF`, which is **not on `main`**, and
whose `MIRROR_REVIEW` field is the one manifest in the population that **disagrees with itself across
refs** — `REV-ORCHSURF-MIRROR-001 → REQUEST CHANGES` on one ref, `REV-ORCHSURF-MIRROR-002 — revision
4 WAS reviewed` on another. So the candidate carrying the fix is itself an instance of EG-03.

**Admission.** C5 — three clauses in tension on the canonical surface, with the repair prepared and
unreachable.

---

### 2.3 · E7 — suspected gaps, falsified, with the falsifier recorded

**These are here because a gap map that reports only confirmations is an instrument nobody can
calibrate.** Each was a real suspicion I held and tested.

| # | Suspicion | Falsifier | Verdict |
|---|---|---|---|
| **E7-a** | `public_release_gate.py` prints BLOCK and exits 0 — a false PASS for any CI caller | run without a pipe: **exit 2**. My `exit=0` readings were `$?` after `tail`/`grep` | **NO GAP.** Correctly fail-closed |
| **E7-b** | `lease_state.py` fails open when it cannot read the lease | `--home <nonexistent>` → **exit 2** | **NO GAP.** Correctly fail-closed |
| **E7-c** | LINT / receipts / growth anchors are ceremonial — they pass because they measure nothing | all three run, all three PASS, all three have tests **in** the release runner, and `growth_anchors` re-derives its own denominators rather than reading declared ones | **NO GAP.** These are the E1 exemplars |
| **E7-d** | The three approval-queue lineages contradict each other | all three share a **byte-identical 6-line prefix**; the two extensions are **disjoint**; 0 key collisions. Independently re-derived, confirming `PLAN-J3-QUEUE-RECONCILIATION-001` | **NO GAP** in *content*. The gap is the writer (EG-09), not a conflict |
| **E7-e** | `artifact_index.py`'s 120 findings are 120 gaps | it declares itself discovery-only, exits 0 always, gates nothing by design; `UNATTRIBUTED` (45) and `NO_SESSION_REF` (69) are aspirations of a **DRAFTED, non-binding** convention | **NO GAP.** OPTIONAL/FUTURE — § 2.4 |
| **E7-f** | The fingerprint drift across checkpoints is a defect | the composition inputs include two CORE files that P5DOMAIN legitimately amended; drift on pertinent change is A.6 **succeeding** | **NO GAP** in the drift. The gap is the recovery route (EG-14) |

### 2.4 · OPTIONAL / FUTURE — real, improvable, and not repairs

Admitted by none of C1–C5. Listed so they are not rediscovered as urgent.

1. **`artifact_index.py`'s 120 convention findings** — 6 `IN_A_CLASS_DIRECTORY_IT_IS_NOT`, 45
   `UNATTRIBUTED`, 69 `NO_SESSION_REF`. Under a non-binding convention, non-conformance is not
   violation.
2. **`PROPOSAL` and `HANDOFF` are UNANCHORED classes** — the convention itself says they have no
   correct home today (P-1, P-7). Deciding it changes nothing that currently runs.
3. **`MIRROR_RETROSPECTIVE ogni N batch` — `N` is `UNASSIGNED_PARAMETER`.** § P7's closing note
   flags it and declines to fill it in, correctly: G.2 puts retrospective methodology beyond
   Mirror's unilateral change. It blocks nothing that is otherwise reachable (EG-08 already blocks
   it).
4. **The `runtime/` domain classification** — open, routed to C-9 § 7.2 under an operator-owned
   hold, with a `PROCEDURAL` mitigation declared as such. Re-deriving it here is the
   self-authorization the hold exists to prevent.
5. **Approval bindings do not record which `CANDIDATE_HASH_VERSION` they were computed under** —
   `legend_operating_convention_v1.md` § S.12, measured 0/0/3 across the three queue lineages
   against 8 of 8 on the CAND manifests. Real, and it becomes urgent only when the hash rule next
   moves.

---

## 3 · ROADMAP_REBASELINE

### 3.1 · The five axes, kept apart on purpose

A feature is not `DONE` because it is written down. Every row below is scored on all five, and the
gap between columns 1 and 5 is the entire content of this section.

```
DOCUMENTED  a normative or design surface says it exists
IMPLEMENTED an artifact or script exists
EXECUTABLE  it runs, today, from a checkout
ENFORCED    something refuses when it is violated
VALIDATED   a test in scripts/run_release_regressions.py protects it
```

### 3.2 · M1 · ARTIFACT CONVENTION v1.0

| Item | Status | DOC | IMPL | EXEC | ENF | VAL | Note |
|---|---|:--:|:--:|:--:|:--:|:--:|---|
| M1.1 class map | **DONE** | ✅ | ✅ | ✅ | ➖ | ✅ | delivered as `framework/scripts/artifact_index.py`; test at `run_release_regressions.py:59`. `ENF` is ➖ **by design** — exit 0 always |
| M1.2 `activation_state` | **NOT_STARTED** | ✅ | ❌ | ❌ | ❌ | ❌ | no file on any ref. **Highest-value buildable item in the whole plan** — § 3.7 |
| M1.3 convention document | **DONE (as DRAFTED)** | ✅ | ✅ | ➖ | ❌ | ➖ | `legend_operating_convention_v1.md`, 1360 lines, `binding: NO`, indexed at `protocols/index.md:95` |
| M1.4 relocate 3 `DEC-*` + 1 `APPROVAL-*` | **BLOCKED_AUTHORITY** + **BLOCKED_DEPENDENCY** | ✅ | ❌ | — | — | — | needs D-6; and B.10 orders it **after P-7** — do not relocate a class whose existence is escalated |

**M1 is the milestone the multi-agent work actually moved.** Two of four delivered, both since
2026-08-23.

### 3.3 · M2 · HUMAN_APPROVAL_QUEUE RECONCILIATION

| Item | Status | Note |
|---|---|---|
| Analysis / divergence report | **DONE** | `PLAN-J3-QUEUE-RECONCILIATION-001` — independently re-derived here (EG-09), unchanged |
| M2.1 reconciler `--report` | **NOT_STARTED** | pure function, writes nothing to `ledger/`. Buildable now |
| M2.2 declare the writer | **BLOCKED_AUTHORITY** | D-1 / **P-2, the root of the B.10 graph** |
| M2.3 out-of-vocabulary states | **BLOCKED_AUTHORITY** + dep P-2 | D-2 / P-3 |
| M2.4 the single reconciling write | **BLOCKED_AUTHORITY** + **BLOCKED_DEPENDENCY** | D-1 ∧ D-2 ∧ (a lease, if D-1 elects Orchestrator) |
| M2.5 currency of HA-2 / HA-4 | **BLOCKED_AUTHORITY** | D-5. HA-4's tip is measurably not an ancestor of `main`; HA-2 declares no tip at all, so its status is `NOT MEASURABLE` |

### 3.4 · M3 · EVENT LEDGER / §P7

| Item | Status | Note |
|---|---|---|
| Architecture | **DONE** | § P7 option (a), path, format, view. Byte-identical across every ref carrying it. **Not reopened here** |
| M3.1 writer + validator | **NOT_STARTED** | debt row **eligible now** by its own declared threshold (`CAND-20260816-GOV311` § 4) |
| M3.2 consolidator + replay view | **NOT_STARTED** | depends on M3.1. `fulltext_receipts.py rechain` is the consolidator primitive and is already written and tested |
| M3.3 LINT wiring at INFO | **NOT_STARTED** | depends on M3.1/M3.2. INFO is not a gate |
| M3.4 first emission | **BLOCKED_AUTHORITY** | D-3 ∧ a lease. **Build ≠ emit** — § 5.9 |

### 3.5 · M4 · FIRST PRODUCTIVE LEGEND CYCLE

| Item | Status | Note |
|---|---|---|
| M4.1 pilot selection | **BLOCKED_AUTHORITY** + **BLOCKED_DEPENDENCY** | D-4; and **EG-12** — 0 VERIFIED capabilities, L2 suspended |
| M4.2 pre-declared measurement sheet | **NOT_STARTED** | buildable now, and **quantity #2 (hand-edits to close a cycle) has no baseline and cannot be reconstructed after the run** |
| M4.3 the run | **BLOCKED_AUTHORITY** + **BLOCKED_DEPENDENCY** | D-4 ∧ M3.1 (else no event evidence) ∧ **EG-15** (GATE 2) |
| M4.4 comparison + KEEP/DISCARD | **BLOCKED_DEPENDENCY** | after M4.3. `legend-research-loop` is the existing instrument |

### 3.6 · 🔴 The workstream the roadmap does not name, and the one this section exists to surface

**What risks being neglected because attention is on governance is the science, and it is
measurable, not a worry.**

```
Last commit touching any of the four canonical current files, on ANY of 50 refs:
    749a9a9   2026-08-15 00:14:55 +0200   "Propagate the integrated reading backlog as WM v4.3"

Commits on main since:                                        87
Commits since, on ANY ref, touching any of the four:            0
Positive control (total commits ever touching them, all refs):  9   ← the query fires
Commit candidates queued at HEAD:                              19   (CC-*.md, object-derived)
BATCH_COMMIT trigger:                                          ≥5
```

🔴 **`749a9a9` is not an arbitrary boundary. It is `RES-20260816-GOV311-001`'s `base_head` —
literally the commit the entire governance layer was approved against.** Everything after it is
governance about a pipeline that has not moved since.

**The honest reading, and the honest counter-reading, both stated.**
The counter-reading is real: the governance was installed *because* the pipeline needed gates, the
scientific state is **healthy and green** (LINT PASS, 128 receipts chained and anchored, growth
anchors PASS, four current files untouched by any of the 87 commits), and a frozen-and-correct
registry is a legitimate state to be in while its safety apparatus is built.
The reading I hold anyway: **a backlog at ~4× its own trigger, idle for ten days, is a measurement
of cost, and no artifact in this repository states it.** Every roadmap document tracks M1–M4 and
D-1…D-6. **None tracks the 19.** That absence is the finding.

**This is not a proposal to run a batch.** Running one requires D-4, EG-12 and EG-15, none of which
are Plan's. It is a proposal that **the queue depth belongs in the roadmap as a tracked quantity**,
so that the cost of each additional governance week is visible rather than inferred.

### 3.7 · What the recent multi-agent work accelerated, and what it revealed to be less mature

**Accelerated** — all since 2026-08-22, all verifiable in durable state:

- M1.1 and M1.3 delivered and, for M1.1, wired into CI;
- `DEC-20260822` settled activation as a **fact** rather than leaving it ambient;
- the entire B.2.2 measurement — three verdict axes, and the discovery that the only one a FROZEN
  gate reads is unpopulated — a defect nobody had named in six days of using the gate;
- `PLAN-J3-QUEUE-RECONCILIATION-001`, and the chronology inversion inside it;
- Mirror v3's fifteen findings and their independent re-measurement, three of which **moved**;
- 12 previously-untracked Plan records tracked, with 11 identifier occurrences scrubbed first;
- the Annex C.2 author response written.

**Revealed to be less mature than it looked** — each is a thing that read as working:

| Looked like | Is |
|---|---|
| GATE 3 gates on Mirror PASS | the gating field is free text; **0 of 10 conform**; a non-conforming value already carried a canonical GATE 3 |
| The lease has a tracked home, so it is observable | tracked ≠ enforced; the population is **ref-dependent, 5 vs 9**, and the lag is structural |
| The role contracts define the actors | **4 of 4 non-binding**, and the activation condition **fails on 3** |
| §P7 is decided | 23 types, **0 code, 0 events**, and Mirror's primary surface depends on it |
| Actors have declared capabilities | **21 rows, 21 UNVERIFIED, 0 VERIFIED**, verification under an operator hold |
| The approval queue is append-only and single | **3 lineages, no declared writer**, 12 approvals invisible from `main` |
| ONE_WRITER protects the root | **0 executable form** — and it failed here, this session |
| The publication gate protects `main` | it does, correctly and fail-closed — **and it now blocks GATE 2 from this branch** |

**The pattern, stated once.** Every item in the right-hand column was *documented* and *not
validated*. The five-axis scoring in § 3.1 exists because a single `DONE` column would have shown
green for all eight.

---

## 4 · MIRROR_V3_READY_QUEUE

### 4.1 · Basis, and what is deliberately not re-derived

`PLAN-MIRROR-V3-MINIMUM-REPAIR-CONSOLIDATION-001` (@ `43cf690`, actions 1–7, routing R-1…R-7) is
**consumed, not re-measured**. M3-1…M3-15, the three moved findings (M3-10 discriminant is CASE not
PATH; M3-14 partly falsified; M3-15 is 14 dirty not 15) and Action 7's execution are taken as given,
with attribution. **What this section adds is what that record's R-table does not carry**: obsolete
and no-op actions, actions whose *content* changed under the three moved findings, reviewer, Human
Gate y/n, Orchestrator-required y/n, and what Plan can prepare **today**.

### 4.2 · Residual actions after the three moved findings

| Action | Still live? | Changed by | What changed |
|---|---|---|---|
| **1** privacy digest | ✅ live | **M3-10** | **The patch is one enrolled casefold digest, NOT a path pattern.** `independent_privacy_scan.py:239` already checks `CASEFOLD_IDENTIFIER_DIGESTS`; the name is simply not enrolled. Mirror's proposed pattern would leave the lowercase-standalone form uncaught |
| **2** wire `verify` + one real recipe | ✅ live | — | Unchanged. Sized "one line" and **is not one line**: `verify` is a property of which directory you stand in, so the wiring must declare an artifact workspace or it converts a correct fail-closed into a permanent red |
| **3** gates print their population | ✅ live | — | Unchanged. **Cheapest, highest leverage** — the only repair that would have made M3-9, M3-8 and M3-3 visible on day one without a reviewer |
| **4** `stated commit` in the evidence standard | ✅ live | — | Unchanged, and **strictly after Action 3** |
| **5** supersession / closing-artifact check | ✅ live | **M3-15** | Its owning object is now **tracked** (Action 7 discharged the blocker). Routable |
| **6 · A′** run-level authority aggregation | ✅ live | **M3-14** | Survives as Plan plumbing, folded into Action 5 |
| **6 · B** Annex C.3 cap fitness | ✅ live | **M3-14** | **Reframed.** Question A as Mirror framed it is satisfied; the surviving question is the one this record widens at **EG-13** |
| **7** Plan untracked state | ✅ **DONE** | — | Executed at `702df73`. **No longer a queue item** |
| **6 · Question A patch** | 🔴 **OBSOLETE — NO-OP** | **M3-14** | Annex C is already in both P2.2 pertinence sets; `roles/scientist.md` already states the cap; three Orchestrator artifacts cite it mid-run. **Do not queue it** |

### 4.3 · READY_QUEUE — ordered for consumption without re-analysis

Ordering rule: **anything Plan can finish alone comes first**, then anything a tool implementer can
finish alone, then anything gated. **No later row implies authority for an earlier unresolved gate.**

| # | Action | Actor | Reviewer | Human Gate | Orch. required | Depends on | Preparable by Plan today |
|:--:|---|---|---|:--:|:--:|---|---|
| **Q-1** | **EG-15** — clear **both** red suites in `PATHOGRAPH-TRANSPORT-CONSOLIDATION-001`: the wikilink block at `:222` (option **a**) and the three non-existent script names at `:57 :64 :65` | **Plan** — the file's author, or with their consent | none (ordinary) | ❌ | ❌ | — | ✅ **the whole action.** Turns `run_release_regressions.py` green and unblocks GATE 2 for every candidate from this branch |
| **Q-2** | **EG-06** — `test_lease_state.py`, `test_governance_fingerprint.py`, both into the release runner | **Plan** | ordinary | ❌ | ❌ | — | ✅ the whole action |
| **Q-3** | **A-3** — three gate verdicts print their population | tool implementer | ordinary | ❌ | ❌ | — | ✅ the exact per-gate diff (§ 6.3 of the V3 record specifies it verbatim) |
| **Q-4** | **A-5 + A-6·A′** — supersession check + run-level authority aggregation | **Plan**, into `PATHOGRAPH-TRANSPORT-CONSOLIDATION-001` | ordinary | ❌ | ❌ | Action 7 ✅ discharged | ✅ the whole action |
| **Q-5** | **A-2** — wire `regenerate_adjudications.py verify` + one real-recipe test, **with a declared artifact workspace** | tool implementer | **Mirror** — to class it MAJOR or not (§ 250 doubt rule) | ❌ | ❌ | — | ✅ the workspace design + the fixture; **not** the classification |
| **Q-6** | **A-4** — `stated commit` field in the evidence standard | owner of `scientist_evidence_standard.md` (Scientist A) | ordinary | ❌ | ❌ | **Q-3** | ⚠️ Plan may draft the field spec; the object is on `lettore` only, **201 behind `main`** |
| **Q-7** | **A-1** — enrol the folded digest + the 5-fixture matrix | Operator → implementer | Mirror | ✅ **D-1/D-2/D-3 of § 11.1** | ❌ | — | ✅ the fixture matrix and the enumeration of affected tracked surfaces, **without printing identifiers** |
| **Q-8** | **A-6·B** — Annex C.3 cap fitness, widened by **EG-13** | **Operator** | — | ✅ **amending a FROZEN annex** | ❌ | — | ✅ the packet, **with the prior question stated and no threshold recommended** |
| **Q-9** | **R-7** — Mirror tests the landed patches | **Mirror** | — | ❌ | ⚠️ C.3 says opening is Orchestrator's — **EG-13** | Q-1…Q-7 | ✅ nothing; it is Mirror's |

### 4.4 · 🔴 One row carries UNRESOLVED AUTHORITY, which is not the same as an unmet dependency

Commit `43cf690` — the commit carrying the V3 consolidation itself — committed three coupled files
that a session acting as Orchestrator had determined were **BLOCKED from preservation**, because the
Operator dispatch makes provenance a precondition and the crosswalk's original authorship is
unrecoverable. **That determination existed only in messages and in a report to the Operator**;
measured across every ref with a positive control, it was present in **zero refs and zero files**.
It could not have been seen from this working directory and was not bypassed.

The coupling is real: **every proper subset of the three files leaves a gate unsatisfied.**

🔴 **Both terminal arms are gate-valid, and I re-derived that here rather than inheriting it.**
Three clean `git archive` extractions into scratch, gates run in place, nothing done to the working
tree:

| Arm | Tree | `legend_lint.py .` | `growth_anchors.py check` |
|---|---|---|---|
| **KEEP all three** | `43cf690` | **PASS**, exit 0 | **PASS**, exit 0 — `unread_premises 4` |
| **REVERT all three** | `43cf690~1` | **PASS**, exit 0 | **PASS**, exit 0 — `unread_premises 4` |
| **REVERT half** — keep the crosswalk, revert FT-073 | `43cf690` + one file reset | 🔴 `BLOCK_BATCH_COMMIT` — *"5 reasoning-layer citations lack any read receipt … above the baseline of 4"* | 🔴 `BLOCK` — `RATCHET_VIOLATION: 1 new unread premises (27845895)` |

**The gates discriminate, and that is what makes the PASS mean something.** A pair of arms that both
passed would be consistent with a gate that never fails; the third arm proves the instrument fires.
**Reverting all three is safe. Reverting half manufactures the failure.**

⚠️ **A correction to what I first wrote here, and it changed the row.** My initial draft carried
*"do not revert — it would destroy the object the decision is about"* as a standing position. That
overstated it in two ways, and a peer session caught the first while my own re-derivation confirmed
the second. **A full revert is valid and lands in a passing state**; the crosswalk is absent at
`43cf690~1` and lives in exactly one commit, so a revert removes a file rather than un-tracking one.
**The whole cost of reverting is that an 834-line analysis with no identifiable author ceases to
exist** — a real cost, and not a gate failure. Saying "unsafe" when the true statement is "expensive"
would have pre-empted the Operator's decision by mislabelling one of its options.

**The question before the Operator is "does `43cf690` stand"** — not "preserve these or not", and
both answers are executable.

**Consequence for this queue, and it is the reason the row exists.** Every row Q-1…Q-9 rests on the
V3 consolidation, which is inside `43cf690`. **If `43cf690` does not stand, the queue's basis moves.**
That is `UNRESOLVED_AUTHORITY`, and a consumer must not treat it as a dependency that will clear on
its own. Detail: `PLAN-WRITER-STATE-AND-COMMIT-PROVENANCE-001` § 3.

### 4.5 · What must NOT change

The sixteen items of `PLAN-MIRROR-V3-MINIMUM-REPAIR-CONSOLIDATION-001` § 8 stand unmodified. **This
record adds nothing to that list and removes nothing from it.** In particular: no new actor, no new
control plane, no new graph schema, no new annex, no numerical threshold, no rewrite of
`regenerate_adjudications.py`, and M3-7a must not enter a design argument.

---

## 5 · §P7 · IMPLEMENTATION-READINESS PACKAGE — decision-neutral

> **This section selects no option.** It does not decide whether § P7 or
> `cross_session_transport.md` become normative; that is EG-02 / D-3, and it is the Operator's.
> Every element below stops at the frontier where a determination begins, and the frontier is
> marked 🛑 rather than crossed.

### 5.1 · Event inventory — the 23 types, with producer and consumer derived from the annexes

Producers are derived from H.1 and the annex that owns each act, **never from a role contract**
(`DEC-20260822` consequence 2).

| # | EVENT_TYPE | Producer (annex basis) | Primary consumer |
|---|---|---|---|
| 1 | `TASK_ASSIGNED` | Orchestrator — H.1 row 1 | Plan reconciliation; Mirror autonomy ledger |
| 2 | `TASK_ACKED` | the assignee — A.2 | Orchestrator (B.3 timeout) |
| 3 | `TASK_CLAIMED` | the assignee — A.3 | Plan (`CLAIM_CONFLICT` detection) |
| 4 | `TASK_COMPLETE` | the assignee — A.5 | Orchestrator; Plan |
| 5 | `TASK_CANCELLED` | Orchestrator — A.5 | the assignee |
| 6 | `CHECKPOINT_WRITTEN` | the actor — A.6 | Mirror (invalidation rate) |
| 7 | `RESUMED_FROM_MILESTONE` | the actor — A.7 | Mirror (work-redone ratio) |
| 8 | `REVIEW_OPENED` | Orchestrator — C.3 🛑 **EG-13** | Mirror (review yield) |
| 9 | `REVIEW_CLOSED` | the reviewer — C.2 | Mirror; Plan |
| 10 | `WORK_COMMIT` | every actor — D.1 | Plan |
| 11 | `CANDIDATE_CREATED` | Plan — D.1 | Orchestrator |
| 12 | `BATCH_COMMITTED` | Orchestrator — D.1, under lease | Plan; Mirror |
| 13 | `BATCH_ABORTED` | Orchestrator — D.4 | Plan (restore path) |
| 14 | `ACTOR_DOWN` | Orchestrator — body § 36 (heartbeat timeout) | the lab roster (J.2) |
| 15 | `ACTOR_ACTIVE` | the actor — J.2 | roster |
| 16 | `LEASE_ACQUIRED` | Orchestrator — I.3 | **the singleton check — EG-05** |
| 17 | `LEASE_STALE` | derivation, not an actor — I.3 | GATE 0 |
| 18 | `HUMAN_REQUIRED_OPENED` | Orchestrator (ordinary) / any actor — H.1, J.3 | the approval queue — 🛑 **EG-09/P-2** |
| 19 | `APPROVAL_RESOLVED` | Operator — J.3 | the requesting actor |
| 20 | `LEARNING_PROMOTED` | Mirror (epistemic) + Plan (durability) — H.1, E | `LEARNING_INDEX` |
| 21 | `GOVERNANCE_UPDATED` | Plan — H.1 | every actor (fingerprint invalidation, A.6) |
| 22 | `DISSENT_OPENED` | any actor — F | Orchestrator |
| 23 | `CHALLENGE_ADJUDICATED` | Orchestrator — H.1 🛑 **EG-13** | the challenger |

**Two rows are structurally different and must not be modelled as actor events.** `LEASE_STALE`
(#17) has no producer — it is a *derivation over a clock*, which is why `lease_state.py` computes it
rather than reading it. `ACTOR_DOWN` (#14) is produced by the *observer*, not the subject, because a
down actor cannot append. **Both are the reason § P7 chose option (a) over option (b)**, and both
are the reason a naive one-writer-per-actor implementation needs an explicit rule for events
*about* an actor written *by* another.

### 5.2 · Storage target — fixed by § P7, restated not re-decided

```
SOURCE   ledger/events/<ACTOR_ID>.jsonl     one writer per file, by construction
VIEW     ledger/consolidated/               derived, rebuilt by replay, never hand-edited
FORMAT   JSON Lines, one event per line, append-only
DOMAIN   ledger/ is a CONTROL_PLANE_ROOT (P5.1) — outside CANDIDATE_CONTENT_HASH
```

🛑 **The domain line is a dependency, not a detail.** Because `ledger/` is control plane, the event
ledger **cannot travel to canonical state inside a candidate** — **EG-10**. Whether the consolidated
view lives on one ref or is rebuilt per-checkout is therefore coupled to the same question as
EG-05's lease and EG-09's approval queue. **Not decided here.**

### 5.3 · Ordering requirements

1. **Per-file total order** — append position. Guaranteed by construction (one writer).
2. **No global total order across files, and none is required.** J.1's `GUARANTEE` names
   attribution and traceability, not global ordering. **Do not invent a global sequence number**;
   it would need a shared writer, which option (a) exists to avoid.
3. **Causal order via `CLOSES_EVENT_ID` only.** J.1 is strict: *"un evento già scritto NON viene MAI
   aggiornato — nemmeno per collegarlo alla sua chiusura."* The open→outcome link lives in the
   **closing** event.
4. **`closed_by` may exist ONLY in the derived view.** Never in a source line. This is the single
   rule most likely to be violated by a convenient implementation, and it is why the view must be
   *rebuildable* rather than *maintained*.

### 5.4 · Idempotency requirements

| Requirement | Rationale |
|---|---|
| `EVENT_ID` unique within its file; re-append of an identical event is a **no-op, not an error** | A.7's resume path replays steps; a resume that crashes mid-append must be safe to retry |
| Replay of the whole consolidation is deterministic and total — same inputs, byte-identical view | the view is evidence; a non-deterministic view cannot be diffed in review |
| `RESUMED_FROM_MILESTONE` is itself an event | A.7 requires the skip to be *recorded*, not silent |
| A consolidator run over an unchanged input set produces an unchanged output | otherwise every run shows as a diff and reviewers stop reading it |

### 5.5 · Recovery requirements — J.1's own clause, made concrete

J.1: `RECOVERY: Plan ricostruisce dallo stato durevole marcando RECONSTRUCTED; le chiusure
ricostruite portano anch'esse CLOSES_EVENT_ID`.

```
R1  a reconstructed event is MARKED RECONSTRUCTED and is never indistinguishable from an observed one
R2  reconstruction reads durable state (commits, receipts, manifests, checkpoints) — never a chat
R3  reconstructed closures still carry CLOSES_EVENT_ID; a closure without an opening is a FINDING,
    not an event to invent
R4  🔴 SOVEREIGNTY: "lo stato repo resta sovrano — in conflitto vince il repo; il ledger è audit
    e analisi, MAI seconda fonte di verità." A reconstruction that contradicts durable state is
    a defect in the reconstruction
```

### 5.6 · Failure semantics — from J.1, each paired with what would detect it

| Failure (J.1) | Detection | Implementable today? |
|---|---|---|
| events missing (actor died before append) | cross-check ledger ↔ durable state; a gap = a missing event | ✅ mechanical |
| consolidation lagging | view tail vs source tails | ✅ mechanical |
| opening without closing beyond a threshold | age of unclosed openings | ⚠️ **the threshold is a parameter nobody owns** — same class as `MIRROR_RETROSPECTIVE ogni N` |
| chain break / truncation | `ledger_prev_hash` + tail anchor, the receipts pattern | ✅ **already implemented, in `fulltext_receipts.py`** |

### 5.7 · The reuse target, measured

§ P7 names `fulltext_receipts.py` and instructs that the writer *"should reuse the existing
append-only machinery, not invent a second one."* Measured: **1444 lines of implementation, 1207
lines of test**, subcommands `validate · verify · anchor · status · record · rechain`.

| J.1 requirement | Already present |
|---|---|
| append-only **enforced**, not asserted | `ledger_prev_hash` = SHA-256 of the canonical serialization of the previous event |
| truncation detectable | tail anchor (count + head digest) in the state manifest |
| validate / verify / append / query | four subcommands |
| **consolidate two divergent histories** | `rechain --onto` — *"rebase this ledger's divergent events onto another ledger's history"*, with `--dry-run` and a refusal on orphaned citations |

**`rechain` is the consolidator primitive, already written and already tested.** It is also the
primitive M2.1 needs, which is the strongest argument that the approval queue should be a
*specialization* of this mechanism rather than a second one — and that argument is recorded, not
adopted: **it is D-1 option (b), and D-1 is the Operator's.** 🛑

### 5.8 · Tests — positive and negative, specified so an implementer does not invent them

**Positive**
1. Round-trip: append one event of **each of the 23 types**, `validate` → OK, chain intact.
2. `CLOSES_EVENT_ID` on a closure type resolves to an existing opening in the same or another file.
3. Consolidation over a synthetic multi-actor fixture is **deterministic**: two runs, byte-identical.
4. `closed_by` appears in the view and in **no** source line — asserted over the source bytes.
5. Re-append of an identical `EVENT_ID` is a no-op; the file does not grow.
6. A `RECONSTRUCTED` event round-trips with its marking preserved.

**Negative** — each must FAIL, and the test asserts the failure
7. An event type outside the 23-member enum → **rejected**. The enum is closed.
8. `CLOSES_EVENT_ID` on a **non-closure** type → rejected.
9. A write to `ledger/events/<any ACTOR_ID but the writer's own>.jsonl` → **refused**. This is the
   one-writer property, and it must be enforced by the writer, not by discipline.
10. Mutating a historical line → chain break detected by `validate`.
11. Truncating the tail → detected by the anchor, **not** by the chain. Both must be exercised
    separately; a chain-only test passes on a truncated ledger.
12. A closure whose opening does not exist → **FINDING**, not a silent accept.
13. A consolidator run over a source set containing two files claiming the same `EVENT_ID` →
    reported, not silently deduplicated.

🔴 **Test 11 is the one most likely to be skipped**, because a chain check *looks* like it covers
truncation and does not. `fulltext_receipts.py`'s docstring already states this in its own words and
also states the residual limit honestly: *"an editor who rewrites the ledger and the manifest anchor
in the same breath is not caught by arithmetic."*

### 5.9 · Dependencies, and the frontiers this package does not cross

```
NO DEPENDENCY — buildable today
  the writer, the validator, the closed 23-type enum, the one-writer path refusal,
  the consolidator, the replay view, every test above, LINT wiring at INFO severity

🛑 FRONTIER — stop here
  D-3   is §P7 normative?                          → EG-02, Operator (H.1)
  D-4   who may emit, and from when?               → EG-12/EG-13, Operator + a lease
  P-2   the ledger/approvals writer                → EG-09; decides whether the queue reuses
                                                      this mechanism or stays separate
  P-1   PROPOSAL's domain                          → touches CONTROL_PLANE_ROOTS, which decides
                                                      where the consolidated view may live
  ---   the "opening without closing" threshold    → an UNASSIGNED_PARAMETER, § 2.4 item 3
```

🔴 **BUILD ≠ EMIT, and the reason is not caution.** A ledger written under a design whose normative
standing is undetermined, **by the only actor who could also declare it normative**, is the
self-written-record defect one layer up. Writing the *code* is not writing the *record*. The debt row
is eligible; the emission is not.

### 5.10 · Smallest coherent implementation slices

| Slice | Contents | Depends on | Gated? |
|:--:|---|---|:--:|
| **S1** | schema + closed enum + `validate`, no writer | — | no |
| **S2** | writer with the own-`ACTOR_ID`-path refusal + tests 1, 5, 9, 10 | S1 | no |
| **S3** | tail anchor + truncation test 11 | S2 | no |
| **S4** | consolidator via `rechain` + view + tests 3, 4, 13 | S2 | no |
| **S5** | `CLOSES_EVENT_ID` resolution + reconstruction marking + tests 2, 6, 12 | S4 | no |
| **S6** | LINT wiring at **INFO** (ledger ↔ durable-state gap) | S5 | no — INFO is not a gate |
| **S7** | **first emission** | S6 | 🛑 **D-3 ∧ D-4 ∧ a lease** |

**S1–S6 are one working session and cross no frontier.** S7 is a different kind of act and is the
only slice that is.

---

## 6 · CLOSING SECTIONS

### 6.1 · EXECUTABLE_GOVERNANCE_GAPS — summary

**17 gaps admitted**, over a population of every normative surface in `governance/`, `roles/`,
`framework/protocols/`, `runtime/` and `ledger/` that I could reach from this ref plus `main`'s two
extra objects. **6 falsified (E7)**, **5 classed OPTIONAL/FUTURE**.

```
E1  1 exemplar class, 6 properties          the gates that run, and the pattern that made them run
E2  4   EG-03 EG-05 EG-06 EG-09(enum)       a mechanism exists; nothing guarantees it is invoked
E3  3   EG-01 EG-04 EG-07                   specified, no mechanism
E4  7   EG-08 EG-10 EG-11 EG-12 EG-13 EG-14 EG-17    the actor, lease or route is closed
E5  3   EG-02 EG-16 (+EG-13 secondarily)    two obligations that cannot both hold
E6  1   EG-09(writer)                       behaviour with no normative owner
E7  6   falsified, falsifiers recorded
```

**The single most consequential number: 7 of 17 are E4.** They are not fixed by building anything.
**Six of the seven terminate at the same two facts** — no reachable Orchestrator (EG-13) and no
activated contract (EG-01) — and those two are one operator session apart.

### 6.2 · ROADMAP_REBASELINE — summary

```
DONE                 M1.1 · M1.3 · M2-analysis · M3-architecture · V3 Action 7 · the C.2 author
                     response (written; UNDELIVERED — EG-10)
NOT_STARTED          M1.2 · M2.1 · M3.1 · M3.2 · M3.3 · M4.2      ← all six need no authority
BLOCKED_AUTHORITY    M1.4 · M2.2 · M2.3 · M2.5 · M3.4 · M4.1 · M4.3 · role activation
BLOCKED_DEPENDENCY   M2.4 · M4.4 · M1.4 (also, on P-7)
SUPERSEDED           V3 Action 6 Question A — measured NO-OP, do not queue
OPTIONAL_FUTURE      the five classes at § 2.4
UNTRACKED WORKSTREAM 19 commit candidates · 0 propagations in 87 commits · trigger ≥5   (§ 3.6)
```

### 6.3 · MIRROR_V3_READY_QUEUE — summary

**9 rows, ordered.** Q-1…Q-4 need **no** Human Gate, **no** Orchestrator and **no** determination —
they are four actions Plan or a tool implementer can finish alone. Q-5 needs a Mirror
classification, not an approval. Q-7 and Q-8 are the two Human Gates, both prepared, **neither
pre-empted**. Q-9 is Mirror's and inherits EG-13.

🔴 **Q-1 first, and not for tidiness: it is the only row that unblocks a gate.** Until EG-15 clears,
GATE 2 fails for every candidate cut from this branch, so no work in this queue can become a
candidate at all.

**One row carries `UNRESOLVED_AUTHORITY`, not an unmet dependency** — § 4.4, `43cf690`.

**Write-seat disclosure for this working directory** — recorded in durable state precisely because
EG-04 says an arrangement like this one should not live in chat.

Three sessions named `evidence-index-*` held this directory concurrently. Sole-writer was
established by explicit exchange, not by assumption:

- `evidence-index-a7 [83eedd]` opened a `ONE_WRITER` check, held the seat, and wrote `702df73`,
  `43cf690`, `4be5a37`, `addd7f1`, `6c8f70f`, `eac6737`;
- `evidence-index-a6 [446782]` stood down as writer with **zero commits**, and attested authorship
  of five files inside `702df73`;
- this session, `evidence-index-cb [abbbc5]`, held **read-only** throughout the measurement phase
  and then wrote **this file only**.

🔴 **The handover itself demonstrated the gap it documents.** The release of the seat was first sent
to `legend-public-cb` — a different session whose name differs from this one's by prefix — which
correctly declined to act on an agreement it was not party to. **A routing slip of one label left the
seat unclaimed and both parties waiting**, and nothing in the repository could have detected it,
because the arrangement had no durable form. Identity was ultimately established the only way
available: each session's name is **absent from its own `ListAgents` output and present in the
other's**, and delivery closes the pair. That is a workable protocol and it is a chat protocol.
`started Xh ago` was explicitly not used, by either party: it measures runtime incarnation, not
paternity of the work on a branch.

### 6.4 · DECISION_NEUTRAL_WORK_AVAILABLE_NOW

Work that reduces uncertainty, prepares an already-foreseen implementation, or verifies a promised
property — **and crosses no frontier**. Ordered by value.

| # | Work | Owner | Authority it rests on | Closes / prepares |
|:--:|---|---|---|---|
| 1 | Clear both EG-15 suites (option **a** + three script names) | Plan | none — a Plan working record, ordinary change | **turns CI green; unblocks GATE 2** |
| 2 | `test_lease_state.py` + `test_governance_fingerprint.py`, both into the release runner | Plan | none — adding a test gates nothing new | **EG-06** |
| 3 | `activation_state` — resolve every conditional `status:` line to `SATISFIED / UNSATISFIED / UNMEASURABLE` | Plan | none — **it asserts no activation**, it prints facts | **EG-02**, and stops the class recurring |
| 4 | §P7 slices **S1–S6** | Plan | `CAND-20260816-GOV311` § 4 — debt eligible at its own threshold | **EG-07**; unblocks EG-08's precondition |
| 5 | `approval_queue_reconcile --report` — pure function, writes nothing to `ledger/` | Plan | none | **EG-09** analysis half |
| 6 | Q-4 — supersession check + run-level authority aggregation | Plan | ordinary; owning object now tracked | V3 Actions 5 + 6·A′ |
| 7 | M4.2 — the pilot measurement sheet, **pre-declared** | Plan | none — a declaration made before a run | **quantity #2 is unrecoverable after the run** |
| 8 | A `ONE_WRITER` durable record + a report-only check | Plan | none as a report | **EG-04** |

**Total: roughly one to two working sessions, zero governed objects touched, zero authority claimed,
and every item reversible by `git revert`.**

### 6.5 · TRUE_HUMAN_OR_ORCHESTRATOR_BLOCKERS

**Everything else in this record is downstream of these nine.** Six of the nine are **one-time**
unblocking decisions, not recurring costs.

| # | Blocker | Whose | One-time? | Unblocks |
|:--:|---|---|:--:|---|
| **H-1** | **The role-contract activation act** — its form, its content, its performance | Operator (H.1) | ✅ | EG-01, EG-16, EG-17, every `OWNER` column in every plan |
| **H-2** | **A determination on satisfied-condition/stale-status**, covering all four objects at once | Operator (H.1) | ✅ | **EG-02** — and P5.1, which binds every candidate hash |
| **H-3** | **Lift the C-9 hold on L2** capability verification | Operator | ✅ | **EG-12** → every Task Contract, M4 entirely |
| **H-4** | **A reachable Orchestrator** — a lease, by the Annex I.2 route, never by self-assumption | Operator (I.2 step 9–10) | ✅ | **EG-13** → Annex C at both ends; EG-14's recovery; M3.4; M4.3 |
| **H-5** | **D-1 / P-2 — declare the writer for `ledger/approvals/`** | Operator | ✅ | **EG-09**, and it is the **root** of the B.10 graph |
| **H-6** | **A route for control-plane artifacts into canonical state** | Operator | ✅ | **EG-10**, EG-05, EG-11 — and they should be decided together |
| **H-7** | **P-8 — the `MIRROR_REVIEW` vocabulary** | Operator, on Mirror's input | ✅ | **EG-03** → GATE 3 stops accepting free text |
| **H-8** | **Does `43cf690` stand?** | Operator | ✅ | the **basis** of the entire Mirror-V3 queue — § 4.4 |
| **H-9** | **The two prepared Human Gates** — V3 § 11.1 (privacy digest) and § 11.2 (Annex C.3 cap, widened by EG-13) | Operator | ✅ | Q-7, Q-8 |

🔴 **H-4 is the keystone.** It appears in the dependency chain of five of the seven E4 gaps. It is
also the one blocker that **no actor may resolve on its own behalf** — I.2 makes promotion a
protocol and body § 9.4 forbids self-promotion — so it cannot be worked around by any amount of
preparation, including this record.

**And there is a real order among them.** H-2 before H-1: the four contracts' activation runs
through `plan_defined_parameters.md`, which is itself in the EG-02 set, and activating contracts
under a hash rule whose own status is unsettled reproduces the defect one layer up. **H-5 before
H-6**, because a route for control-plane artifacts that does not know who writes the queue will fork
it a fourth time.

---

## 7 · NEXT_5_PLAN_ACTIONS

Five, maximum, ordered by value to the roadmap as a whole. **Each either reduces uncertainty,
prepares an already-foreseen implementation, or verifies a promised property.** Anything that did
only one of "keeps Plan busy" was discarded — including a sixth candidate (a validator for the
convention's 120 findings), which fails the admission test at § 1.2 and is left at § 2.4.

| # | Action | Why it is here | Type | Done when |
|:--:|---|---|---|---|
| **1** | **Clear EG-15** — repair **both** red suites in `PATHOGRAPH-TRANSPORT-CONSOLIDATION-001` (`:222` wikilink, option **a**; `:57 :64 :65` non-existent script names), and register option **c** as a separate proposal **carrying § 2.5 as its motivation** | `run_release_regressions.py` is **red at HEAD** and has been since `702df73`, and until the publication block clears **no candidate can be cut from this branch** — GATE 2 requires publication gate PASS/0. § 2.5 raises the stakes on (c): the repository currently cannot document its own wikilink convention at all | verifies a promised property | `git archive HEAD` extraction → release gate `PASS · BLOCKS 0 · exit 0` **and** `test_documented_commands.py` exit 0, both matching the `43cf690~2` control |
| **2** | **Build `activation_state`** — resolve every conditional `status:` line to `SATISFIED / UNSATISFIED / UNMEASURABLE`, printing the condition, the measurement and the command | **Four records have now derived the EG-02 table by hand** (`PLAN-EXECUTION-TRANSITION` § 1b, `SCIENTIFIC-PIPELINE-PREPARATION` § 3.3, this record § 2, and the four `roles/` rows in `DEC-20260822`). It asserts no activation; it makes H-2 decidable on printed facts in one sitting instead of a fifth re-derivation | reduces uncertainty | it reproduces § 2's EG-02 table and the four `roles/` rows without a human re-deriving them, with a test in the release runner |
| **3** | **`test_lease_state.py` + `test_governance_fingerprint.py`**, both wired into `run_release_regressions.py` | **6 of 8 governance tools are covered; the 2 that are not are exactly the two a FROZEN gate consumes as a boolean** — GATE 0's singleton and A.6's resume predicate. Cheapest item in the backlog, and it protects the two properties whose silent regression would be least visible | verifies a promised property | both run green in the runner; the singleton test asserts a **non-zero exit** on a two-ACTIVE fixture |
| **4** | **§P7 slices S1–S6** — schema, closed 23-type enum, writer with own-path refusal, tail anchor, consolidator via `rechain`, LINT at INFO. **Emit nothing** | The debt is **eligible at its own declared threshold** and needs no authorization; it is the precondition of Mirror's primary surface (EG-07) and of the declared v3.2 path (EG-08). Reuses 2,651 lines of already-tested machinery rather than inventing a second ledger | prepares a foreseen implementation | all 13 tests of § 5.8 pass on a synthetic 23-type fixture; `ledger/events/` still contains **zero real events** |
| **5** | **Q-4** — the supersession / closing-artifact check plus run-level authority aggregation, into `PATHOGRAPH-TRANSPORT-CONSOLIDATION-001` | Its owning object became routable when Action 7 tracked it, so the edge that blocked it is discharged; it closes V3 Actions 5 and 6·A′ together; and the class it repairs — a closing artifact bound to a mid-run snapshot, measured at **8·7·9 commits of drift** — is a merge-base check, not another reviewer | prepares a foreseen implementation | the check reports incorporated/superseded/rejected/missed per peer artifact and binds a handoff to actual current tips |

**Deliberately NOT in this list, and why**, because an omission with a reason is information:

- **`approval_queue_reconcile --report`** — buildable and harmless, but its output changes nothing
  until H-5 declares a writer, and `PLAN-J3-QUEUE-RECONCILIATION-001` already carries the analysis a
  human needs to decide. It would produce a machine-readable twin of a conclusion already reached.
- **M4.2, the pilot measurement sheet** — genuinely valuable and genuinely time-sensitive (quantity
  #2 cannot be reconstructed after a run), but it is six blockers away from a run. It belongs
  immediately after H-3 and H-4 clear, not before.
- **Anything touching `roles/`, `governance/`, `ledger/` or `runtime/`** — all four are inside
  EG-01, EG-09, EG-10 or a hold. Preparing text for them is available; writing it is not.

---

## 8 · WHAT THIS RECORD DOES NOT DO

Does not activate any role contract, protocol or parameter file · does not change any `status:` line
on any ref · does not select an option on D-1…D-6 or on P-1…P-8 · does not decide whether §P7 or
`cross_session_transport.md` are normative · does not rule on EG-02's contradiction · does not
declare an `ACCEPT → PASS` mapping for `MIRROR_REVIEW` · does not open a `CAND`, write a `DEC`,
create an `APPROVAL` or append to any `.jsonl` · does not write to `ledger/`, `runtime/`,
`governance/` or `roles/` on any ref · does not assign work to any actor · does not dispatch, and
sent no `TASK_ASSIGNMENT` · does not acquire or renew a lease · does not verify or declare a
capability · does not lift the C-9 hold · does not re-review any commit candidate · does not
adjudicate any scientific proposition, type any edge, or open a current file for writing · does not
constitute an `AUTHOR_RESPONSE` to anything · is **not** a `WORK_COMMIT`'s justification and **not**
a `CANONICAL_BATCH_COMMIT`.

---

## 9 · VERIFICATION TRAIL

Every figure above, with the command that produced it and its figure class. **Population-derived
figures decay as branches are created; object-derived figures do not.** A reader who gets a
different number must be able to tell which happened.

| # | Claim | Command | Class |
|:--:|---|---|---|
| 1 | HEAD `4be5a37`, 2 behind / 59 ahead of `main` | `git rev-list --left-right --count main...HEAD` | population |
| 2 | 44 heads + 6 remotes; 27 worktrees | `git for-each-ref` · `git worktree list` | population |
| 3 | Sweep control: `CLAUDE.md` on 44 of 44 | per-ref `git cat-file -e "${r}:CLAUDE.md"` | population |
| 4 | LINT PASS · receipts OK 128 · anchors PASS · lease ACTIVE 0 | the four scripts, run here | object |
| 5 | `status: ACTIVE|BINDING` never in `roles/`; controls fire at 7 and 3 | `git log --all -S… --` ×6 | object |
| 6 | 11 objects carry `PROPOSED` on `main` | per-file `git show main:<p> \| sed -n '/^status:/p'` | object |
| 7 | `worktree: orchestrator` on 2 of 44; file present on 29 of 44 | **braced** per-ref sweep + presence control | population |
| 8 | Approval queue: 3 blobs — 6/26 refs · 10/1 ref · 14/2 refs | `git rev-parse "${r}:ledger/approvals/…"` then `git cat-file -p` | population |
| 9 | Lease: 2 blobs; `ACTIVATED_AT` ×6 vs ×10 → 5 vs 9 records | `git rev-parse` per ref; `grep -c ACTIVATED_AT` | object |
| 10 | `ledger/events/` and `ledger/consolidated/` on 0 of 44; control `ledger/approvals/` on 29 of 44 | `git ls-tree -r --name-only "$r" \| grep -E …` | population |
| 11 | 0 Python files reference the event ledger; 14 `.md` do | `grep -rln … --include='*.py'` / `'*.md'` | object |
| 12 | `ONE_WRITER` in 0 `.py`; control `CONTROL_PLANE_ROOTS` in 3 | `grep -rln … --include='*.py'` | object |
| 13 | `MIRROR_REVIEW` conforming 0 of 10 (14 in class) | `python3 framework/scripts/artifact_index.py` | population |
| 14 | Fingerprint tool emits 4, exit 0; `roles/plan.md:73` says blocked | `governance_fingerprint.py compose --all` · `grep -n` | object |
| 15 | 19 Plan checkpoints; 3 distinct hashes + 2 prose; today `0d6987bd…` | JSON parse of `ledger/checkpoints/plan/*` · `compose --role plan` | object |
| 16 | Release gate **and** `test_documented_commands.py`: clean `43cf690~2` → 0/OK; clean `43cf690` and `eac6737` → BLOCK 1 / FAILED | `git archive <ref> \| tar -x -C <scratch>` then both run in place | object |
| 17 | Wikilink regex at `:651`, scan loop `:697`, allowlist `:44`, no code-span stripping | `sed -n` over `scripts/public_release_gate.py` | object |
| 18 | 6 of 8 governance tools tested and in the runner; `lease_state`/`governance_fingerprint` neither | `git ls-files \| grep test_<t>.py` + `grep -c` in the runner | object |
| 19 | 56 suites in the release runner | `sed -n '1,90p' scripts/run_release_regressions.py` | object |
| 20 | Agent card: 21 capability rows, 21 UNVERIFIED, 0 VERIFIED | `git show orchestrator:runtime/agent_card_registry.md \| grep -cE '\{capability:'` | object |
| 21 | `runtime/` beyond the lease on 1 of 44; control `governance/` on 29 of 44 | per-ref `git ls-tree -r --name-only "$r" -- runtime/` | population |
| 22 | AUTHOR-RESPONSE-ROLES-MIRROR-001 on 1 of 44; control `reviews/plan/` on 20 of 44 | per-ref `git cat-file -e` + directory control | population |
| 23 | Last current-file commit `749a9a9` 2026-08-15; **0** after it on any ref; control **9** total | `git log --all --oneline [749a9a9..] -- "$@"` with `set --` | object |
| 24 | 87 commits on `main` since `749a9a9`; 19 `CC-*.md` queued | `git rev-list --count` · `ls -1 … \| wc -l` | population / object |
| 25 | `fulltext_receipts.py` 1444 + 1207 lines; 6 subcommands incl. `rechain` | `wc -l` · `--help` | object |
| 26 | § 4.4 three arms: KEEP PASS/PASS · REVERT-ALL PASS/PASS · REVERT-HALF `BLOCK_BATCH_COMMIT` + `RATCHET_VIOLATION (27845895)` | three `git archive` extractions into scratch; `legend_lint.py .` and `growth_anchors.py check` run in place | object |
| 27 | The crosswalk is absent at `43cf690~1` and lives in exactly one commit | `git cat-file -e '43cf690~1:disease-models/wwox/analysis/dismech_legend_evidence_crosswalk_v2.md'` | object |
| 28 | § 2.5: this record's first draft added **4** publication blocks; after the rewrite it adds **0** | `public_release_gate.py` before and after, working tree | object |
| 29 | Only one path moved between `4be5a37` and `eac6737` | `git diff --name-only 4be5a37 eac6737` | object |

**Four things in this record were wrong on first execution and are reported as corrected, with the
mechanism.** Three were caught by controls rather than by rereading; one was caught by a peer.

| What | Mechanism | Caught by | Changed a conclusion? |
|---|---|---|---|
| Row 23 — the scientific-idleness query | zsh does not word-split an unquoted parameter expansion, so four paths arrived as one argument | **its own positive control returning an impossible 0** (§ 0.3) | no — the negative survived re-execution |
| E7-a / E7-b exit codes | `$?` read after a pipe measures the last command in the pipeline, not `python3` | probing deliberately for fail-open | **yes** — it would have reported two sound gates as broken |
| Row 27 — the crosswalk's history | I searched `…/research/…` where the path is `…/analysis/…` | a `0` that was implausible against a commit I could see | no |
| § 4.4 — "do not revert" | I asserted a revert was unsafe; the true statement is that it is expensive | **a peer session**, then confirmed by my own three-arm re-derivation | **yes** — it mislabelled one of the Operator's two options |

**The pattern is worth more than the four corrections.** Every one of them was a *confident* number
or claim, and none was caught by re-reading what I had written. Three fell to a control that fired
where it should not have, and the fourth to someone who was not persuaded. **A figure without a
control is not a measurement, and a judgement made alone is not a finding until someone else can
see it.**

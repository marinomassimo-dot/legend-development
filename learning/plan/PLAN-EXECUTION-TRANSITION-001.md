---
artifact: EXECUTION TRANSITION — the minimum path from governance bootstrap to a running laboratory
record_id: PLAN-EXECUTION-TRANSITION-001
task_id: PLAN_EXECUTION_TRANSITION_v1
author: plan
authored_on: 2026-08-23
dispatcher: operator
governance_version: 3.1.1 (read, not exercised)
mode: PLANNING_ONLY

STATUS: PLAN_DELIVERED
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none

classification:
  - EXECUTABLE PLAN — milestones, dependencies, owners, deliverables
  - NOT A GOVERNANCE CHANGE
  - NOT A DEC — § 5 prepares six determinations; it makes none
  - NOT AN ACTIVATION — no `status:` line is changed by this record
  - NOT A MERGE AUTHORIZATION
  - NO NEW VOCABULARY, NO NEW HIERARCHY LEVEL

scope_source: >
  Operator dispatch, in-session, 2026-08-23: "TRANSITION FROM ANALYSIS TO EXECUTION", four
  priorities M1–M4, four required outputs. The dispatch closes SURFACE MAP and forbids opening
  new general governance analyses. This record opens none: every finding below was already
  measured by a prior record or is re-measured here with the command shown.

domain: >
  CONTENT. `learning/` is content by explicit intent (`plan_defined_parameters.md` § P5.1), so
  this file sits inside the `CANDIDATE_CONTENT_HASH` of any future candidate spanning this branch
  and moves it. Disclosed, not worked around.

owner_caveat: >
  🔴 The `OWNER` column names SEATS, not authorities. No role contract is binding:
  `roles/plan.md`, `roles/orchestrator.md`, `roles/scientist.md` and `roles/mirror.md` all carry
  `status: PROPOSED — binding once Mirror hostile review passes and the operator approves`, and
  `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` returned `ACTIVATION_NOT_CONFIRMED`. The only
  binding authority in force is Annex H.1 (FROZEN), which names the operator. Every non-operator
  seat below therefore acts under operator-transmitted scope, exactly as this record does.
---

# EXECUTION TRANSITION — M1 · M2 · M3 · M4

> **Nothing here executes.** This record orders work, names what blocks it, and specifies the
> first commit down to the command. It writes no governance object, opens no candidate, changes
> no status line and claims no authority.

---

## 0 · BASELINE — measured at this HEAD, this session

```
BRANCH            plan-orchsurf-r4-transcription   HEAD e995edd
WORKTREE          .claude/worktrees/evidence-index
CANONICAL main    788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5     OBSERVED, NOT MOVED
CONTENT REFS      52  (43 refs/heads · 4 refs/remotes · 5 refs/tags; 4 codex turn-diffs and
                      refs/stash excluded as non-content)
TRACKED PATHS     764 distinct, union over all 52 refs
```

| # | check | command | result |
|---|---|---|---|
| 1 | structural LINT | `python3 framework/scripts/legend_lint.py .` | **PASS** (1 INFO, pre-existing) |
| 2 | receipt ledger | `fulltext_receipts.py verify` | **OK** — 128 chained, tail anchored |
| 3 | publication gate | `python3 scripts/public_release_gate.py` | 🔴 **BLOCK_PUBLICATION** — 3 blocks |
| 4 | lease | `framework/scripts/lease_state.py` | **ACTIVE by derivation: 0** |
| 5 | `ledger/events/` | `git ls-tree` over 52 refs | **absent on every ref** |
| 6 | role contracts | `grep '^status:' roles/*.md` | **4 of 4 PROPOSED** |

**All three publication blocks are `DIRECT_IDENTIFIER` in ONE untracked file** —
`learning/plan/FIRST-SCIENTIST-PILOT-READINESS-AUDIT-001.md`, lines 582, 629, 673: the operator's
given name written into public material. The file belongs to another session and is not touched
here. It is a working-tree-only block: a clean checkout of this HEAD passes. It blocks GATE 2
(*"LINT PASS + publication gate PASS/0 nella stessa finestra"*), therefore it blocks any
**candidate** evidenced from this tree — and it does **not** block a `WORK_COMMIT`.

---

## 1 · THE ONE IDEA THAT ORDERS EVERYTHING: **BUILD ≠ ACTIVATE**

The dispatch's own finding — *plumbing gap, not design gap* — has a corollary that decides the
sequence. Every M1–M3 item splits cleanly in two:

```
MECHANISM   a script, a schema, a report, a test.  Content. Measurable. Reversible.
            Requires NO human determination and NO lease. Buildable today.
NORMATIVITY the sentence that says "and from now on this binds."  Governance.
            Requires the operator (H.1). Not buildable, only decidable.
```

Everything that has stalled has stalled because the two were bundled. Unbundled, **M1, M2.1, M3.1
and M3.2 are buildable now**, and the human gate shrinks to **one decision session** covering six
determinations (§ 5), all of the same class.

Two corollaries, both measured:

**(a) The debts are already declared and already eligible.** `CAND-20260816-GOV311` § 4
`PENDING_IMPLEMENTATION` already carries M3 and M2 with their own eligibility thresholds:

| debt row | eligible when (verbatim) | status now |
|---|---|---|
| EVENT LEDGER writer + validator | *"After canonical commit, before the first scientific batch"* | ✅ **ELIGIBLE** — canonical commit done; first scientific batch not started |
| Consolidated event view | *"With the writer"* | ✅ **ELIGIBLE** with M3.1 |
| `HUMAN_APPROVAL_QUEUE` — general implementation | *"With the brief, after canonical commit"* | ⚠️ eligible; the brief is a separate debt |

M3 is therefore **not new development requiring authorization** — it is the discharge of a debt
whose own threshold is met. Building it needs no DEC. *Emitting* under it does (§ 5, D-3).

**(b) Two "PROPOSED" files are stale, not undecided — and they are the same defect.**

| file | its own activation conditions | measured |
|---|---|---|
| `governance/plan_defined_parameters.md` (holds § P7) | Mirror hostile review passes · operator approves | `REV-P5DOMAIN-MIRROR-001` **verdict: ACCEPT** · `APR-20260819-P5DOMAIN-001` **APPROVED** · content tip `ceefaa286115` **ancestor of `main`** ✅ |
| `framework/protocols/cross_session_transport.md` (holds § 8 closure) | canonical execution · Mirror ACCEPT · operator approval | `e839db383827` **ancestor of `main`** · `REV-XPORT-MIRROR-002` ACCEPT · `APR-20260819-XPORT-001` **APPROVED** ✅ |

Both status lines still read `PROPOSED`. Three conditions satisfied, verified at source, never
recorded. `roles/*.md` are **not** in this class — `REV-ROLES-MIRROR-001` returned
`CHANGES_REQUIRED` on three of four contracts and the `AUTHOR_RESPONSE` Annex C.2 requires is
still outstanding.

🔴 **Whether a satisfied condition activates a file is a governance interpretation, and Plan may
not make it** — `DEC-20260822` refused exactly that move by analogy and *"adopts no general
interpretation."* So the plan does not activate them. It **mechanizes the measurement** (M1.2) so
the operator decides once, on facts, instead of re-deriving them per file.

---

## 2 · M1 — ARTIFACT CONVENTION v1.0

**Principle, as agreed and not extended:**

```
Path defines artifact class.
Status defines lifecycle validity.
Presence of an artifact does not imply authority.
```

### 2.1 · The convention — four classes, nothing else

| CLASS | CANONICAL PATH | ID | WRITER | LIFECYCLE FIELD (existing vocabulary) |
|---|---|---|---|---|
| **DEC** | `governance/decisions/DEC-<YYYYMMDD>-<SLUG>.md` | `DEC-…` | operator (`record_type: OPERATOR_DECISION`) | `OPTION_SELECTED` + `SCOPE_LIMITATION` |
| **CAND** | `governance/candidates/CAND-<YYYYMMDD>-<SLUG>.md` | `CAND-…` | plan (H.1 — *integrazione strutturale / candidate*) | `state` + `CANDIDATE_CONTENT_HASH` + `BASE_HEAD` (D.2, P5) |
| **REVIEW** | `reviews/<ACTOR_ID>/REV-<OBJECT>-<REVIEWER>-<NNN>.md` | `REV-…` | that reviewer, that directory, nobody else | `verdict:` — C.2 vocabulary only (`CONFIRMED · WEAKENED · REFINED · REFUTED`) |
| **APPROVAL** | `ledger/approvals/…` (shape decided by **D-1**, § 5) | `APR-…` / `RES-…` | 🔴 **UNDECLARED TODAY** — this is M2's blocker | `STATE` — J.3 vocabulary only |

No fifth class is created. `HANDOFF`, `PROPOSAL`, `PREP`, `ADVISORY`, `DELTA`, `AUTHOR-RESPONSE`
are **not** promoted to classes: they are working artifacts, and the convention's rule about them
is one line — *a working artifact lives beside its author's other work and never inside a class
directory it does not belong to.*

### 2.2 · What the convention costs today — measured over 764 paths / 52 refs

| finding | count | detail |
|---|---|---|
| 🔴 `DEC-*` files **outside** `governance/decisions/` | **3** | all under `governance/candidates/`: `DEC-20260817-006-GOV-SCOPE-RESOLUTION`, `DEC-20260817-006-L2-SCOPE`, `DEC-20260818-007-LAB-REACTIVATION` |
| `DEC-*` correctly placed | 4 | `governance/decisions/` |
| 🔴 `APPROVAL-*` file under `governance/candidates/` | **1** | `APPROVAL-GOV311-DEVIATIONS.md` — an approval-class name in the candidate directory |
| ✅ `REV-*` outside `reviews/` | **0** of 40 | **REVIEW is the one class where the convention already holds by construction** |
| ⚠️ `HANDOFF-*` roots | **5** for 12 files | `governance/candidates` · `learning/mirror` · `learning/plan` · `reviews/mirror` · `runtime/handoff/C-2` |
| ⚠️ `PROPOSAL-*` roots | 2 for 3 files | one of them in the scientific `commit_candidates/` — a different domain entirely |

Seven misplacements out of 764 paths is not a crisis; it is exactly the size of gap that a
report-only validator closes in one pass and then keeps closed for free.

### 2.3 · The third clause is the one that needs a mechanism

*"Presence of an artifact does not imply authority"* has one measurable form: **for every file
whose `status:` names its own activation conditions, resolve each condition against the
repository and print `SATISFIED | UNSATISFIED | UNMEASURABLE`.** That is what nothing does today,
and it is why § 1(b) had to be derived by hand three times in three records.

### 2.4 · M1 deliverables

| id | deliverable | kind | DEC? |
|---|---|---|---|
| **M1.1** | `framework/scripts/artifact_class_map.py` — path ⇄ class ⇄ ID-prefix consistency report over the whole tree; `--report` (default, exit 0) and `--strict` (exit 1 on mismatch, unused until D-6) | script + test | **no** |
| **M1.2** | `framework/scripts/activation_state.py` — for every file with a conditional `status:` line, resolve each named condition to a measured fact and print the table of § 1(b) | script + test | **no** |
| **M1.3** | `framework/protocols/artifact_conventions.md` — the table of § 2.1, `status: PROPOSED`, deliberately | document | **for its normativity only (D-6)** |
| **M1.4** | relocation of the 3 `DEC-*` and 1 `APPROVAL-*` misplaced files | git mv | **yes — D-6** (moving a governance artifact is a governance act) |

**Owner:** plan (M1.1–M1.3) · operator (M1.4 authorization).
**Dependencies:** none. M1.1 and M1.2 depend on nothing and block M2.2, M3.4 and D-1…D-6.
**Done when:** both scripts run green in CI (`run_release_regressions.py`) and `activation_state.py`
reproduces § 1(b) without a human re-deriving it.

---

## 3 · M2 — HUMAN_APPROVAL_QUEUE RECONCILIATION

**Prior work, not repeated here:** `learning/plan/PLAN-J3-QUEUE-RECONCILIATION-001.md` is the
keyed comparison and the divergence report the dispatch asks to keep separate. It is already
separate, already written, and this plan does not restate its tables.

Its load-bearing results, carried forward as *its* measurements:

```
3 lineages         20c24a2ba478 (6 lines, 27 refs, incl. main) · bb603d9a270b (10 lines, 1 ref)
                   95fc81639014 (14 lines, 2 refs)
0 key collisions   0 byte conflicts on the 6-line shared base
union              18 lines · 0 edited · 0 deleted
chronology         🔴 INVERTED vs line count — the 14-line lineage is 2026-08-17, the 10-line one is -18/-19
out-of-vocabulary  3 states — DEFERRED ×2, RESOLVED ×1
invisible from main 8 operator approvals
declared writer    🔴 none
```

Re-verified here at this HEAD: the working-tree copy is the 6-line lineage; the `orchestrator`
ref's tail carries `SUNSET-DEC3-001 · SCIAB-001 · XPORT-001 · P5DOMAIN-001`, all `APPROVED`,
`DECIDED_BY: operator`.

### 3.1 · The four constraints, and what each forbids in code

| constraint | mechanized as |
|---|---|
| no record loss | the reconciler is a **pure function**: union by key, never a rewrite. `assert len(out) == len(union_of_inputs)` |
| no silent retroactive modification | source lines are copied **byte-identical**; the reconciler diffs its own output against each input and refuses to emit if any shared line changed |
| no automatic interpretation of ambiguous states | `DEFERRED`/`RESOLVED` are **carried through verbatim** and surfaced as `LEGACY_STATE` **in the derived view only** — never normalised in a source line |
| divergence report separate | already separate: `PLAN-J3-QUEUE-RECONCILIATION-001.md`; the reconciler regenerates a machine-readable twin, it does not replace the record |

### 3.2 · The blocker is structural, and it is a decision, not a task

A reconciliation performed from any branch that is not the destination **creates a fourth
lineage** — which is the defect being repaired. So the act needs: **one declared writer, writing
once, onto the destination ref.** `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` has **no declared
writer**: J.3 names a requester and a resolver and allocates no file writer, and § P7's one-writer
decision covers `ledger/events/`, not `ledger/approvals/`. There are also **0 ACTIVE leases**, so
there is no `ACTIVE_ORCHESTRATOR` to write onto `main` under GATE 0.

### 3.3 · M2 deliverables

| id | deliverable | kind | DEC? |
|---|---|---|---|
| **M2.1** | `framework/scripts/approval_queue_reconcile.py --report` — keyed union + machine-readable divergence report, **writes nothing to `ledger/`** | script + test | **no** |
| **M2.2** | declare the writer for the J.3 surface | governance | **yes — D-1** |
| **M2.3** | rule for the 3 out-of-vocabulary states | governance | **yes — D-2** |
| **M2.4** | the single reconciling write, on the destination ref, by the declared writer | execution | **after D-1, D-2** |
| **M2.5** | currency of `HA-2` / `HA-4` (`DEFERRED`) | governance | **yes — D-5** |

**Owner:** plan (M2.1) · operator (D-1, D-2, D-5) · the writer D-1 declares (M2.4).
**Dependencies:** M2.1 → nothing. M2.4 → D-1 ∧ D-2 ∧ (lease, if D-1 elects Orchestrator).
**Done when:** the reconciled file exists on exactly one ref, `--report` shows 1 lineage, and no
source line differs from its original by one byte.

---

## 4 · M3 — EVENT LEDGER / P7

**The architecture is not reopened.** § P7 decided option (a) and § P7 is byte-identical on all
30 refs carrying it. `PID-13` fixed the path. What follows is implementation only.

```
DECISION (a)   per-actor append-only JSONL, one writer per file, consolidated by replay
PATH           ledger/events/<ACTOR_ID>.jsonl            ← absent on all 52 refs
VIEW           ledger/consolidated/                       ← derived, rebuilt by replay, never hand-edited
EVENT          EVENT_ID · timestamp · ACTOR_ID · TASK_ID · EVENT_TYPE · OBJECT · DURABLE_POINTER
               CLOSES_EVENT_ID  (closure events only)
TYPES          23, enumerated in J.1 · 0 ever emitted
REUSE TARGET   framework/scripts/fulltext_receipts.py — named by § P7 itself
```

### 4.1 · The reuse target is a closer fit than § P7 claims

`fulltext_receipts.py` (1444 lines, 128 live records, its `verify` already consumed by the LINT)
already implements every primitive J.1 requires, and one J.1 does not name but the consolidator
needs:

| J.1 requirement | already in `fulltext_receipts.py` |
|---|---|
| append-only, enforced not asserted | `ledger_prev_hash` = SHA-256 of the canonical serialization of the previous event |
| truncation detectable | tail anchor (count + head digest) in the state manifest |
| validate / verify / append | `validate` · `verify` · `record` · `status` · `anchor` |
| **consolidate two divergent histories** | 🔴 **`rechain`** — *"rebase this ledger's divergent events onto another ledger's history"*, identity judged **modulo `ledger_prev_hash`**, refusing any change beyond that field |

`rechain` is the consolidator primitive, already written and already tested. **It is also the
primitive M2.1 needs** — which is the argument that the approval queue should be a specialization
of this mechanism rather than a second one (see D-1, option (b)).

### 4.2 · M3 deliverables

| id | deliverable | kind | DEC? |
|---|---|---|---|
| **M3.1** | `framework/scripts/legend_events.py` — writer + validator on the receipts pattern: J.1 schema, the 23-type enum closed, `CLOSES_EVENT_ID` accepted only on closure types, **writer refuses any path but `ledger/events/<its own ACTOR_ID>.jsonl`** | script + test | **no** |
| **M3.2** | consolidator → `ledger/consolidated/events.jsonl`, rebuilt by replay via `rechain`; `closed_by` computed **in the view only**, never in a source line | script + test | **no** |
| **M3.3** | LINT wiring at **INFO** severity first (gap between ledger and durable state = missing event), ratcheted to WARN/BLOCK only after one full cycle of real data | edit to `legend_lint.py` | **no** (INFO is not a gate) |
| **M3.4** | first emission — who emits, from when, and is § P7 normative | governance + activation | **yes — D-3, D-4** |

**Owner:** plan (M3.1–M3.3) · operator (D-3) · orchestrator-seat (D-4, activation).
**Dependencies:** M3.2 → M3.1. M3.4 → D-3 ∧ a lease. **M3.1–M3.3 depend on nothing.**
**Done when:** `legend_events.py validate` and `verify` pass on a synthetic 23-type fixture, the
consolidated view round-trips by replay, and the LINT reports the ledger↔state gap as INFO.

🔴 **Build the mechanism, emit nothing, until D-3.** A ledger written under a design whose
normative standing is undetermined, by the only actor who could also declare it normative, is the
self-written-record defect one layer up. Writing the *code* is not writing the *record*.

---

## 5 · M4 — FIRST PRODUCTIVE LEGEND CYCLE

**The old to-dos are the test fixture, and they are large enough to be a real test.** Measured
this session:

```
batch_queue.md            415 unprocessed · 233 with free full text · 73 NEW · 25 IN_PIPELINE
full_text_queue_current   72 FT entries · 11 HIGH
commit_candidates/        17
deepdive_manifests/       64
receipts                  128 chained
```

A pilot design already exists and is not rewritten here:
`learning/plan/FIRST-WWOX-PAPER-PILOT-DESIGN-001.md` (untracked, another session's), with
`SCIENTIST-FIRST-REAL-PAPER-PILOT-001` and `SCIENTIST-ACTIVATION-READINESS-001` behind it.

### 5.1 · What makes it a test of the plumbing rather than a paper read

One paper, end to end, with **the measurement declared before the run** — otherwise the run
produces a paper and no evidence about the pipeline:

| # | measured quantity | instrument | baseline (pre-plumbing) |
|---|---|---|---|
| 1 | events emitted vs events expected for the task shape | `legend_events.py` + J.1's 23 types | **0 emitted** — every value is an improvement, so #1 alone proves nothing |
| 2 | state files requiring a **hand** edit to close the cycle | `git diff --stat` over the run, partitioned by generated-vs-authored | ⚠️ unmeasured — **capture it on the pilot run or the comparison is lost** |
| 3 | receipts vs readings | `fulltext_receipts.py status` | 128 chained; `FT-001`'s six-day lag is the known failure shape |
| 4 | time from full text acquired → commit candidate | run clock | unmeasured |
| 5 | LINT/gate failures discovered **after** the work rather than before | LINT + `public_release_gate.py` | GATE 2 blocked today by an untracked file (§ 0) |

🔴 **#2 is the one that answers the dispatch's question,** and it has no baseline. It must be
captured during the pilot run itself; reconstructing it afterwards is not possible.

### 5.2 · M4 deliverables

| id | deliverable | kind | DEC? |
|---|---|---|---|
| **M4.1** | pilot selection from the existing queue — one paper, from `full_text_queue_current.md` HIGH or `batch_queue.md` NEW, chosen by the existing `legend-proband-priority-matrix`, not invented | selection | **no** — but see D-4 for who runs it |
| **M4.2** | the pre-declared measurement sheet of § 5.1, written **before** the run | document | **no** |
| **M4.3** | the run itself: intake → acquire → deep dive → commit candidate | execution | **D-4** (a Scientist seat running work is an activation) |
| **M4.4** | the comparison, and the KEEP/DISCARD verdict on each plumbing piece — `legend-research-loop` is the existing instrument for exactly this and is not re-invented | document | **no** |

**Owner:** operator (D-4) · scientist-seat (M4.3) · plan (M4.2, M4.4).
**Dependencies:** M4.3 → D-4 ∧ M3.1 (or the run produces no event evidence) ∧ § 0's GATE 2 block
cleared if the cycle is to end in a candidate.
**Done when:** one paper closes with a commit candidate, and § 5.1's five rows have values.

---

## 6 · OUTPUT 1 — ORDER OF ACTIONS

Three tracks. Track A needs nobody, and everything else waits on Track B's single session.

```
TRACK A — BUILDABLE NOW, NO DEC, NO LEASE, NO ACTIVATION       (plan seat, own branch)
  A1  M1.1  artifact_class_map.py            + test        ─┐
  A2  M1.2  activation_state.py              + test         │  ← COMMIT 1 (§ 9)
  A3  M1.3  artifact_conventions.md  (PROPOSED)            ─┘
  A4  M3.1  legend_events.py  writer + validator + test        ← COMMIT 2
  A5  M3.2  consolidator + replay view + test                  ← COMMIT 2
  A6  M2.1  approval_queue_reconcile.py --report + test        ← COMMIT 3
  A7  M3.3  LINT wiring at INFO                                ← COMMIT 3
  A8  M4.2  pilot measurement sheet, pre-declared              ← COMMIT 4

TRACK B — ONE OPERATOR SESSION, SIX DETERMINATIONS             (operator)
  B1  D-1 … D-6  (§ 7).  Input: the reports A1, A2 and A6 produce.
      🔴 Run Track A FIRST — the six determinations are decided on measured facts,
         and A1/A2/A6 are what measures them.

TRACK C — UNBLOCKED BY B, IN THIS ORDER                        (mixed seats)
  C1  M1.4   relocate 3 DEC-* + 1 APPROVAL-*        after D-6
  C2  M2.4   the single reconciling write            after D-1 ∧ D-2
  C3  M3.4   first emission                          after D-3 ∧ a lease
  C4  M4.1   pilot selection                         after D-4
  C5  M4.3   the pilot run                           after C3 (else no event evidence)
  C6  M4.4   comparison + KEEP/DISCARD verdict       after C5

PARALLEL, OWNED ELSEWHERE, BLOCKING ONLY PUBLICATION
  P1  clear the 3 DIRECT_IDENTIFIER blocks in the untracked audit file (§ 0)
      → owner: the authoring session, or the operator. Fix: the given name → "the operator".
      Blocks: GATE 2, therefore every CAND. Does NOT block Track A.
  P2  AUTHOR_RESPONSE to REV-ROLES-MIRROR-001 — required by C.2, outstanding
      → owner: plan. Blocks: role-contract activation, therefore every binding OWNER column.
```

**Critical path:** `A1+A2 → B1 → C2/C3 → C5 → C6`. Track A is one working session. Track B is one
operator session. Nothing else is serialized.

---

## 7 · OUTPUT 2 — WHAT REQUIRES A HUMAN DEC

Six determinations, all Annex H.1 → operator, all decidable in one session. Each carries options
and a recommendation the operator is free to reject; **none is decided here.**

| # | determination | why only the operator | options | Plan's recommendation |
|---|---|---|---|---|
| **D-1** | **Who writes `ledger/approvals/`?** J.3 allocates no file writer; the surface has forked into 3 lineages precisely because of it | allocating a writer is a governance act (H.1 — *governance → operatore*) | **(a)** Orchestrator sole writer under ACTIVE lease · **(b)** per-actor `ledger/approvals/requests/<ACTOR_ID>.jsonl` + `resolutions/operator.jsonl`, consolidated by replay · **(c)** operator-only | 🔵 **(b)** — same one-writer topology as § P7, same consolidator (`rechain`), and it dissolves the fork by construction instead of by discipline. It is the smallest change that cannot re-fork |
| **D-2** | **The 3 out-of-vocabulary states** (`DEFERRED` ×2, `RESOLVED` ×1) | changing J.3's vocabulary, or reinterpreting a recorded operator decision, is governance | **(a)** extend J.3's enum · **(b)** map them to J.3 values with a recorded mapping · **(c)** carry verbatim, surface as `LEGACY_STATE` in the derived view only | 🔵 **(c)** — it is the only option that satisfies the dispatch's own "no silent retroactive modification" and "no automatic interpretation". (a) and (b) both edit the past |
| **D-3** | **Is § P7 normative?** `plan_defined_parameters.md` reads `PROPOSED`; its two conditions are measured satisfied (§ 1b) and the file is Plan's own | extending `DEC-20260822` by analogy is a governance interpretation, and Plan may not rule on its own file | **(a)** confirm normative, correct the stale status line · **(b)** require a fresh Mirror review · **(c)** leave PROPOSED and forbid emission | 🔵 **(a)**, with the same ruling extended to `cross_session_transport.md`. They are one defect class, and D-6 mechanizes the check that stops it recurring |
| **D-4** | **Activation:** may a Scientist seat run the M4 pilot, and does an Orchestrator lease open? | `TASK_ASSIGNED` has exactly one authorized writer (H.1 row 1) and nobody holds it; 0 ACTIVE leases | **(a)** open a lease and activate one Scientist seat for the pilot only · **(b)** the operator runs the pilot under transmitted scope, no activation · **(c)** defer | 🔵 **(a) scoped to the pilot** — (b) works but produces no evidence about the *laboratory*, which is what M4 is for |
| **D-5** | **Are `HA-2` and `HA-4` (`DEFERRED`) still live?** `HA-4`'s candidate tip `ab4856b1d90c` is 🔴 **NOT an ancestor of `main`**; `HA-2`'s candidate declares **no content tip at all**, so its status is `NOT MEASURABLE` | ruling on the currency of an operator's own deferral is the operator's | **(a)** both lapsed · **(b)** both live · **(c)** per-item | 🔵 **(c)** — they differ in kind: one is measurably un-canonicalized, the other is unmeasurable because the candidate never declared a tip. One ruling for both would hide that |
| **D-6** | **Does the artifact convention (M1.3) bind, and may `artifact_class_map.py --strict` gate?** | making a convention normative, and moving governance artifacts (M1.4), are governance acts | **(a)** bind + `--strict` in CI + relocate the 4 files · **(b)** bind, report-only, relocate · **(c)** leave PROPOSED, report-only | 🔵 **(b)** first, **(a)** after one clean cycle — a gate switched on the same day as its first measurement blocks on its own novelty |

**Not requiring a DEC, and worth saying so explicitly:** building any Track A script; running any
report; writing this plan; selecting a pilot paper from an existing queue; wiring a LINT check at
INFO. None of them changes a governed object.

---

## 8 · OUTPUT 3 — WHAT CAN BE IMPLEMENTED IMMEDIATELY

Everything in Track A. Concretely, in dependency order, with the authority each rests on:

| # | file | ~size | authority it rests on |
|---|---|---|---|
| 1 | `framework/scripts/artifact_class_map.py` + `test_artifact_class_map.py` | ~150 + ~120 | none needed — a report over `git ls-tree`. Writes nothing but stdout |
| 2 | `framework/scripts/activation_state.py` + test | ~180 + ~140 | none needed — resolves declared conditions to measured facts; **asserts no activation** |
| 3 | `framework/protocols/artifact_conventions.md`, `status: PROPOSED` | ~80 lines | none — a PROPOSED document binds nobody, which is clause 3 of the convention applied to itself |
| 4 | `framework/scripts/legend_events.py` + test | ~300 + ~250 | `CAND-20260816-GOV311` § 4: the debt row is **eligible now**. Emits nothing |
| 5 | consolidator + replay view + test (may live in #4) | ~150 + ~120 | same row, *"with the writer"* |
| 6 | `framework/scripts/approval_queue_reconcile.py --report` + test | ~200 + ~150 | none — pure function, `ledger/` untouched |
| 7 | LINT wiring at INFO | ~30 | INFO is not a gate; the LINT already carries pre-existing INFO |
| 8 | M4.2 measurement sheet | ~60 lines | none — a declaration made before a run |

**Total: ~2,100 lines, one working session, zero governed objects touched, zero authority
claimed.** Every one of them is reversible by `git revert` and none of them can move a
`CANDIDATE_CONTENT_HASH` in a way a reviewer cannot see.

---

## 9 · OUTPUT 4 — THE FIRST CONCRETE COMMIT

**`COMMIT 1` — M1's two scripts and the PROPOSED convention.** It is first because D-1 … D-6 are
decided on what `activation_state.py` and `artifact_class_map.py` print, and because it is the
only milestone with no dependency of any kind.

```
BRANCH        plan-orchsurf-r4-transcription        (WORK_COMMIT — H.1: own branch, milestone granularity)
CLASS         WORK_COMMIT, not CANONICAL_BATCH_COMMIT.  GATE 0 not invoked; no lease required
GATE 2        not applicable to a WORK_COMMIT — and it would fail from this tree today (§ 0)
DOMAIN        CONTENT (framework/) — moves a future candidate hash. Disclosed, correct, and
              exactly what P5.1 intends for framework/
```

**Files — named individually; blanket staging is blocked in this repository:**

```
learning/plan/PLAN-EXECUTION-TRANSITION-001.md          this record
framework/scripts/artifact_class_map.py                 M1.1
framework/scripts/test_artifact_class_map.py
framework/scripts/activation_state.py                   M1.2
framework/scripts/test_activation_state.py
framework/protocols/artifact_conventions.md             M1.3   status: PROPOSED
framework/protocols/index.md                            one pointer line added
```

**Acceptance, run before staging — all four must pass:**

```bash
python3 framework/scripts/test_artifact_class_map.py
python3 framework/scripts/test_activation_state.py
python3 framework/scripts/legend_lint.py .                     # expect PASS
python3 framework/scripts/artifact_class_map.py --report       # expect exit 0, 7 findings listed
python3 framework/scripts/activation_state.py                  # expect the § 1(b) table, reproduced
```

**Commit:**

```bash
git add learning/plan/PLAN-EXECUTION-TRANSITION-001.md \
        framework/scripts/artifact_class_map.py \
        framework/scripts/test_artifact_class_map.py \
        framework/scripts/activation_state.py \
        framework/scripts/test_activation_state.py \
        framework/protocols/artifact_conventions.md \
        framework/protocols/index.md
git commit -m "The convention was already true of forty reviews and false of four governance files, and nothing measured which"
```

**What COMMIT 1 must NOT contain**, so the commit stays inside the authority it claims:

```
no change to any status: line                    no ledger/events/ file
no file under governance/decisions/              no ledger/approvals/ write
no file moved out of governance/candidates/      no CAND, no DEC, no APPROVAL
no --strict wiring in CI                         no lease row, no roster row
```

**Then COMMIT 2** (`legend_events.py` writer + validator + consolidator + tests) and **COMMIT 3**
(`approval_queue_reconcile.py --report` + LINT INFO wiring). Both are Track A; neither needs
Track B. **COMMIT 4 is the first one that does**, and it is `M2.4` — the single reconciling write,
by the writer `D-1` declares, on the ref `D-1` implies.

---

## 10 · WHAT THIS RECORD DOES NOT DO

Does not decide D-1 … D-6 · does not activate `plan_defined_parameters.md`,
`cross_session_transport.md` or any `roles/*.md` · does not change any `status:` line · does not
open a `CAND` · does not write a `DEC` · does not write to `ledger/` on any ref · does not merge
or authorize merging the approval queue · does not normalise `DEFERRED` or `RESOLVED` · does not
relocate any file · does not assign a task · does not acquire or renew a lease · does not select
the pilot paper · does not touch the five untracked artifacts of another session · does not
advance `main` · does not introduce vocabulary or a new hierarchy level · is not the
`AUTHOR_RESPONSE` that `REV-ROLES-MIRROR-001` still requires.

---

## 11 · VERIFICATION TRAIL — every number above, and the command that produced it

| # | claim | command | result |
|---|---|---|---|
| 1 | LINT | `legend_lint.py .` | PASS, 1 INFO |
| 2 | receipts | `fulltext_receipts.py verify` | OK, 128 chained, anchored |
| 3 | publication gate | `public_release_gate.py` | BLOCK_PUBLICATION, 3 blocks, all in one **untracked** file |
| 4 | leases | `lease_state.py` | ACTIVE by derivation: **0** (5 rows: 2 STALE, 3 RELEASED) |
| 5 | `ledger/events/` | `git ls-tree -r` × 52 refs | **absent on every ref** |
| 6 | role contracts | `grep '^status:' roles/*.md` | 4 of 4 `PROPOSED` |
| 7 | `DEC-*` placement | union of `ls-tree` over 52 refs | 4 in `decisions/`, **3 in `candidates/`** |
| 8 | `APPROVAL-*` placement | same | **1**, in `candidates/` |
| 9 | `REV-*` placement | same | 40 files, **0 outside `reviews/`** |
| 10 | `HANDOFF-*` roots | same | 12 files across **5** roots |
| 11 | tracked paths | same | **764** distinct |
| 12 | P5DOMAIN review verdict | `git show refs/heads/mirror:reviews/mirror/REV-P5DOMAIN-MIRROR-001.md` | `verdict: ACCEPT` |
| 13 | P5DOMAIN approval | `git show refs/heads/orchestrator:…/HUMAN_APPROVAL_QUEUE.jsonl` | `APR-20260819-P5DOMAIN-001` `APPROVED`, `DECIDED_BY: operator` |
| 14 | candidate tips vs `main` | `git merge-base --is-ancestor <tip> main` | `ceefaa286115` ✅ · `e839db383827` ✅ · `234c8bae2a33` ✅ · `4454feab72b7` ✅ · `b9af54ebe2fd` ✅ · 🔴 `ab4856b1d90c` **NOT** |
| 15 | receipts CLI surface | `fulltext_receipts.py --help` | `validate · verify · anchor · status · record · **rechain**` |
| 16 | debt rows | `CAND-20260816-GOV311.md` § 4 | EVENT LEDGER writer *"after canonical commit, before the first scientific batch"* |
| 17 | queue fixture sizes | `grep -c`, `ls \| wc -l` | 72 FT entries (11 HIGH) · 17 commit candidates · 64 deepdive manifests · 415 unprocessed / 233 free full text / 73 NEW / 25 IN_PIPELINE |
| 18 | `main` | `git rev-parse main` | `788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5` — unchanged |

Carried from `PLAN-J3-QUEUE-RECONCILIATION-001` and **not** re-measured here, attributed as its
measurement: the 3 lineages, the 0 key collisions, the 18-line union, the inverted chronology, the
3 out-of-vocabulary states, the 8 approvals invisible from `main`.

---

**Prepared by:** `plan`, worktree `evidence-index`, branch `plan-orchsurf-r4-transcription`,
2026-08-23 — under the operator's transmitted scope for the execution transition, **not** under
the authority of `roles/plan.md`, which is `PROPOSED` and not binding.

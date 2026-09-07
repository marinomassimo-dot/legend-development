---
artifact: ARCHITECTURAL ANALYSIS — the operating model of Orchestrator as Laboratory Director
record_id: LAB-DIRECTOR-OPERATING-MODEL-001
task_id: LAB_DIRECTOR_OPERATING_MODEL_v1
dispatcher: operator
author_session: worktree cut from `main` @ `788c357`, branch `orch-lab-director-operating-model`,
  no ACTIVE lease
actor_id: NOT ESTABLISHED — see § 1. This record is not authored under a role contract.
date: 2026-08-22
governance_version: 3.1.1 (read, not exercised)
classification:
  - ARCHITECTURAL ANALYSIS ONLY
  - NOT AN IMPLEMENTATION
  - NOT AN ACTIVATION OF THE ORCHESTRATOR ROLE
  - NOT A GOVERNANCE CHANGE
normative_sources_used: >
  The governance body (`GOVERNANCE_v3.1.1.md`) and annexes A–J only, plus
  `plan_defined_parameters.md` for the seven values the annexes delegate by name. Per the
  operator's constraint and independently per `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE`
  consequence 2, NO clause of any file under `roles/` is used as the source of a rule. All four
  role contracts are treated as PROPOSED throughout. Where a role contract agrees with an annex
  it is cited as agreement, never as authority.
domain: >
  CONTENT. `learning/` is not a CONTROL_PLANE_ROOT — P5.1 lists exhaustively
  `governance/candidates/`, `ledger/`, `reviews/`. This record therefore sits inside the
  CANDIDATE_CONTENT_HASH of any future candidate that re-aligns onto `main`.
not_an_slr: >
  This is NOT a Session Learning Record (Annex E.6). The name is deliberately not `SLR-` so the
  two are not conflated.
authority_claimed: none
writes_performed: one file, on this branch, in this worktree. `main` unchanged at `788c357`.
---

# LABORATORY DIRECTOR — OPERATING MODEL 001

> **ANALYSIS ONLY · NOT AN IMPLEMENTATION · NOT AN ACTIVATION · NOT A GOVERNANCE CHANGE**
>
> Nothing here creates a queue, a schema, a field, an event, a validator or a registry. Nothing
> assigns work, opens a review, requests an approval, acquires a lease or activates a contract.
> It answers one question with measurements: **if the human operator disappears for 12 hours,
> what can LEGEND continue doing safely, and what must stop?**

---

## 0 · TASK_STATUS

The dispatch asks for six components analysed and one number produced. All six are analysed
below and the number is given in § 11, with its denominator named and its limits stated.

**Two conditions constrain what this record may claim, and both are measured, not assumed.**

1. **No role contract is binding.** `governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md`
   is an operator determination under H.1: `OPTION B — ACTIVATION_NOT_CONFIRMED`. Its consequence
   2 is in force in every section below — *"Any authority an actor exercises must be traced to
   the governance body or to a named annex … never to a role contract clause standing alone."*
   The operator's constraint and the repository's own determination agree, and the analysis is
   written to satisfy the stricter reading of both.
2. **This record is one of six on six branches.** Five sibling analyses exist, none on `main`
   (§ 2.3). Three of them overlap this dispatch's components substantially. **Where a sibling
   reached a finding first, it is credited by name and the measurement is re-run here rather
   than inherited** — twice with a different result (§ 2.4). Where this record adds something,
   § 2.5 says what and why.

---

## 1 · IDENTITY — established from repository evidence, not from the dispatch

The dispatch addresses this session as Orchestrator. **Identity is not conferred by a dispatch**,
and the repository's evidence does not support the claim.

| Fact | Measured value | How |
|---|---|---|
| Repository | `<REPO_ROOT>` | `git rev-parse --show-toplevel` |
| Working tree for this record | a worktree cut for this session, outside the root checkout | `git worktree add -b orch-lab-director-operating-model … 788c357` |
| Branch | `orch-lab-director-operating-model` | `git rev-parse --abbrev-ref HEAD` |
| Base | `788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5` (`main`) | `git rev-parse HEAD` |
| Tree at open | **clean** — 0 porcelain entries | `git status --porcelain` |
| Lease | **`ACTIVE by derivation: 0`** — 5 records, all `STALE` or `RELEASED`; most recent released `2026-08-18T14:05:20Z` | `python3 framework/scripts/lease_state.py` |
| Runtime inventory | **absent on `main`**; exists at `runtime/runtime_inventory.md` on branch `orchestrator` | `git ls-tree` |
| `ACTOR_ID` | **not established** — no registration record exists for this session | — |
| `SESSION_REF` | **not observable** and not invented — `ListAgents` shows peers, never self | — |

### 1.1 · The consequence

`CLAUDE.md` § 0 is unconditional, and both of its antecedents hold:

```
IF no valid runtime inventory / no ACTIVE ORCHESTRATOR_LEASE:
    ENTER BOOTSTRAP_MODE.
    Do NOT assume Orchestrator authority merely because you are in root.
```

**This session is in `BOOTSTRAP_MODE` and is not Orchestrator.** That is not an obstacle to the
task: the dispatch asks how the Director's office *could* work, and describing an office is not
occupying it. It does mean that every statement below about what Orchestrator may do is a
statement about **Annex H.1 and the body**, never about this session.

### 1.2 · Why the root checkout was not used

Body § 14 — `ONE_WRITER_PER_WORKING_DIRECTORY`, *"Critico nella root"* — and § 12 GATE 0, which
requires `root clean` for any future canonical batch. Writing this record in the root checkout
would have made the root dirty for the duration and put a branch other than `main` on the shared
checkout. A session-local worktree costs nothing and removes the hazard. The five sibling
sessions did the same, each in its own scratchpad (`git worktree list`, measured).

---

## 2 · SURFACE_MAP

### 2.1 · Ref surface

`git for-each-ref refs/heads refs/tags refs/remotes` → **49 refs** (40 heads · 5 tags · 4
remotes). Every sweep below iterates all 49 and was run **with a positive control in the same
invocation**, for a specific reason recorded here: the first sweep attempted in this session
returned `0` for the target *and* `0` for the control, because in `zsh` an unquoted variable does
not word-split and the loop ran once against an invalid ref. A sweep that returns zero on a
broken loop is indistinguishable from a sweep that returns zero on an empty repository. **Every
count in this record survived a control that returned non-zero.**

### 2.2 · Normative sources read in full

`GOVERNANCE_v3.1.1.md` (body, 50 sections) · Annexes A, B, C, D, E, F, G, H, I, J ·
`plan_defined_parameters.md` (P1–P7 and the tail note) ·
`governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md`.

Read descriptively, never as authority: `roles/orchestrator.md`, `roles/plan.md`,
`roles/scientist.md`, `roles/mirror.md` — all four carry
`status: PROPOSED — binding once Mirror hostile review passes and the operator approves`, and
`git log --all -S` confirms that line has been **written twice and changed never**.

### 2.3 · The sibling analyses — five, on five branches, none on `main`

| Record | Branch | Lines |
|---|---|---|
| `SCIENTIFIC-PIPELINE-PREPARATION-001` | on `main` **and** carried on five others | 585 |
| `AUTONOMOUS-DISPATCH-LOOP-MODEL-001` | `orch-autonomous-dispatch-loop` | 934 |
| `LEGEND-AGENT-COORDINATION-PROTOCOL-001` | `orch-agent-coordination-protocol` | 943 |
| `CONTROL-PLANE-RECONCILIATION-ANALYSIS-001` | `orch-control-plane-reconciliation` | 745 |
| `SCIENTIFIC_PIPELINE_LIFECYCLE-MODEL-001` | `orch-scientific-pipeline-lifecycle-model` | 862 |
| `ORCHESTRATOR-SCIENTIFIC-PIPELINE-AND-LOOP-ARCHITECTURE-ANALYSIS-001` | `orch-pipeline-loop-architecture` | 1189 |

🔴 **`AUTONOMOUS-DISPATCH-LOOP-MODEL-001` analyses the same six components this dispatch names**,
including a 24-hour version of the 12-hour question. It was read in full before this record was
written. **Re-deriving its conclusions and presenting them as new would be the failure this
laboratory calls a second noun for one object.** What this record does instead is in § 2.5.

### 2.4 · Two measurements re-run, with a different result

Both siblings' figures are defensible under their own predicate; the difference is the predicate,
and it is recorded so a later reader is not left with two numbers and no explanation.

| Quantity | Sibling figure | Measured here | Why they differ |
|---|---|---|---|
| Review artifacts | 54 (`AUTONOMOUS-DISPATCH-LOOP`) · 40 (`CONTROL-PLANE-RECONCILIATION`) | **40 distinct paths whose *basename* begins `REV-`**; **54 distinct paths *containing* the substring `REV-`** anywhere | Both numbers are right for their predicate. The count that matters for review closure is the **object** count, 40 |
| Author responses | 8 | **7 files named `AUTHOR-RESPONSE-*`**, plus 1 named `REV-AUTHOR-RESPONSE-*` — which is a **review of** an author response, not a response | The eighth is on the other side of the join |
| Control-plane validators | *"0 of 831 python files"* for nine control-plane tokens | **1 of 831** — `governance/scripts/governance_fingerprint.py` reads `APPLICABLE_GOVERNANCE_FINGERPRINT`. The other eight tokens measure **0**. Control: `framework/state` → **14** | The fingerprint is the one control-plane object with an executable |

**Closure ratio, restated with the corrected predicate: 7 author responses against 40 reviews.**
C.2: *"AUTHOR_RESPONSE obbligatoria; il silenzio non è accettazione."*

### 2.5 · What this record adds, stated before it is claimed

1. **The office, not the loop.** The siblings model the *machinery* a Director would operate — an
   event stream, a dispatch loop, a lifecycle, a control plane. This record models the **job**:
   what a Laboratory Director is *for* under this constitution, decomposed into the six
   components, and which parts of it the constitution has already given away (§ 3).
2. **The clock inventory** (§ 10). The 12-hour question has a time axis, and nobody has measured
   what LEGEND's own clocks do along it. Every governance clock in this system fires inside the
   **first 90 minutes**. The finding is that the horizon is not a variable.
3. **The two-layer asymmetry, quantified** (§ 4.3). A working, derived, non-hand-maintained task
   queue with a readiness predicate **already runs in this repository** — on the scientific layer.
   `AUTONOMOUS-DISPATCH-LOOP-MODEL-001` T-2 credits the receipt ledger for the append-only
   pattern; this record measures the *queue* itself, which is a closer match to the missing
   object than the ledger is.
4. **The number, on a named denominator** (§ 11). The dispatch requires a percentage. No sibling
   gives one, and each is right that "percentage of work" is unmeasurable today. This record
   answers on a **closed, countable, normative population** — the rows of body § 4 and Annex H.1
   — and says exactly what that measures and what it does not.

---

## 3 · THE OFFICE OF LABORATORY DIRECTOR — decomposed from frozen text

Before asking what can be automated, it is worth asking what the job *is*, because the
constitution already answers and the answer is narrower than "running the lab".

### 3.1 · What the body allocates to Orchestrator

Body § 8, enumerated: *who works on what; priorities; suspensions and reassignments; Ladder level
(≥ floor) and reviewer; opening, ownership and closing of direct interactions (§ 20.3);
readiness of candidates; `CANONICAL_BATCH_COMMIT` under gates; classification of
`HUMAN_REQUIRED`.* Plus routine recovery, receiving learning, distributing PROVISIONAL practice,
maintaining the `DAILY_BRIEF`, and assigning via Task Contract (Annex A).

And, in the same section, the two limits: **it does not produce scientific work destined for the
canon, and it does not decide scientific conclusions.**

### 3.2 · The principle that shapes the whole office

Body § 2 is the sentence the rest of this analysis keeps returning to:

> **Orchestrator controls what work is done, by whom and in which order. It does not control what
> scientific conclusion an agent must reach.**

```
OPERATIONAL AUTHORITY  → Orchestrator: WHO / WHAT / WHEN / PRIORITY / REVIEW / RECOVERY
EPISTEMIC INDEPENDENCE → the responsible Scientist: WHAT THE EVIDENCE SUPPORTS
                         (subject to review, never to an order)
```

🔴 **This is why "Laboratory Director" is a better name than "manager", and why the autonomy
question is tractable at all.** The Director's office is **entirely coordination**. Not one of
its powers is a scientific judgement. A coordination function is exactly the class of work that
can be mechanized without touching rigor — because rigor lives in the other column, and the
constitution has already put a wall between them.

### 3.3 · The office, decomposed into the dispatch's six components

| # | Component | H.1 row that allocates it | Is it a judgement about evidence? |
|---|---|---|---|
| 1 | **Task queue** — what work exists | *Task / priorità / riassegnazione / generation* → Orchestrator | no |
| 2 | **Dependency checking** — what is ready | not allocated by any H.1 row 🔴 | no |
| 3 | **Role resolution** — who does it | *Task…* + *Livello Ladder (≥ floor) e reviewer* → Orchestrator | no |
| 4 | **Handoff** — transferring it | not allocated by any H.1 row 🔴 | no |
| 5 | **Escalation** — what the human must decide | *Classificazione HUMAN_REQUIRED ordinaria* → Orchestrator | no |
| 6 | **Autonomy measurement** — how well it is going | `AUTONOMY LEDGER` → Mirror (G.3) | no |

🔴 **Two of the six components the dispatch names have no authority row anywhere in H.1.**
Dependency satisfaction and handoff are things the governance describes (A.1 declares a
`DEPENDENCIES` field; B.2 lists a `HANDOFF` message type) without ever saying **who decides a
dependency is met** or **who owns a handoff**. This is not a gap in the analysis; it is a gap in
the constitution, and it reappears concretely in § 5 and § 7.

---

## 4 · TASK QUEUE

### 4.1 · What an open task is, in frozen text

A task's life is Annex A.5, and it is a closed vocabulary:

```
ASSIGNED → ACKED → CLAIMED → IN_PROGRESS → (BLOCKED | AWAITING_APPROVAL) → IN_PROGRESS
        → COMPLETE | CANCELLED | REASSIGNED(gen+1) | PARKED
```

**An open task is one whose opening record has no closing record.** That phrasing is forced, not
chosen: J.1 forbids the alternative in terms.

> **Append-only rigoroso:** un evento già scritto NON viene MAI aggiornato — nemmeno per
> collegarlo alla sua chiusura. … Un campo `closed_by` può esistere SOLTANTO nella **vista
> derivata/replayed** costruita da Plan, mai nel ledger sorgente.

So "open" is a **derivation over an append-only stream**, never a field anyone maintains. And
J.1's sovereignty clause adds the second constraint: *"lo stato repo resta sovrano — in conflitto
vince il repo; il ledger è audit e analisi, mai seconda fonte di verità."* The queue reports; the
repository decides.

### 4.2 · How it is represented today — measured

| Object | Specified in | Instances measured |
|---|---|---|
| Task record | A.1, 15 fields | **5**, all under `ledger/tasks/plan/`, all authored by `plan` about `plan` |
| Checkpoint | A.6 | **27** — 19 `plan`, 8 `mirror` |
| Event | J.1, 23 minimum types | 🔴 **0 paths under `ledger/events/` on 49 refs** (control `^roles/`: 108 paths on 27 refs) |
| Consolidated view | J.1 / P7 | 🔴 **0 on 49 refs** |

The five task records' own `STATE` fields, parsed:

```
C9-STATE-MODEL-001            'CLAIMED → IN_PROGRESS'
GOV311-PLAN-REMEDIATION-001   'CLAIMED → IN_PROGRESS'
SCIENTIST-AB-SPEC-001         'CLAIMED → IN_PROGRESS → AWAITING_REVIEW → CHANGES_REQUESTED → …'  (≈300 chars)
P5DOMAIN-001                  ABSENT
XPORT-ROUTING-001             ABSENT
```

🔴 **Not one of the five carries a bare A.5 token, and two carry no `STATE` at all.**
`AWAITING_REVIEW` and `CHANGES_REQUESTED` are not A.5 states. The 300-character chain in
`SCIENTIST-AB-SPEC-001` is a mutable field doing an append-only job — it accumulated its own
history because there was nowhere else to put it. `AUTONOMOUS-DISPATCH-LOOP-MODEL-001` D-1.1
reached this first and its reading is correct: **the cheap retrofit — adding a maintained
`status:` field — is precisely the mutation J.1 bans.**

### 4.3 · 🔴 The queue the Director needs already exists, one layer down

This is the measurement this record contributes, and it changes the shape of the problem.

`framework/scripts/batch_queue.py`, run this session:

```
415 records have not been processed. 233 of them have a free full text
    and can be worked immediately.

NEW                   73   never seen by the system — the front of the queue
CORPUS_CATALOGUED    342   catalogued and deduplicated, never analytically processed
OUT_OF_SCOPE_LIKELY  224   no scope signal in the title — later, never discarded
AMBIGUOUS              7   identifiers must be resolved before ingest
IN_PIPELINE           25   already in flight
KNOWN_INTEGRATED      35   done
```

Its own docstring states the design rule, and it is the rule the control plane needs:

> **Status** — derived here, every run, by joining the seed against the registries on PMID and
> DOI. **Nothing about status is hand-maintained**, so the queue cannot drift into disagreeing
> with the canonical state.

| Property an open-task queue requires | Present in `batch_queue.py`? |
|---|---|
| status derived, never maintained | ✅ every run, from the registries |
| an explicit *ready to work now* predicate | ✅ `233 … can be worked immediately` |
| a not-ready class that is not a discard | ✅ `OUT_OF_SCOPE_LIKELY` — *"never discarded"* |
| an in-flight class distinct from open | ✅ `IN_PIPELINE` |
| an *ambiguous, resolve before ingest* class | ✅ `AMBIGUOUS` — the honest "run the gate on this" |
| never authoritative over canonical state | ✅ read-only toward every registry |
| a dated, inert input that never claims currency | ✅ `corpus_seed_*.tsv`, carries its date |

🔴 **The asymmetry, stated plainly.** On the scientific layer this laboratory has a derived queue
over 415 items with six status classes and a readiness predicate, a chained 128-receipt ledger
that is tail-anchored outside itself, and five runnable gates that all returned PASS this
session. On the control plane it has **five hand-written JSON files, three of which describe
their state in prose and two of which do not describe it at all.**

The Director's task-queue problem is not unsolved in this repository. **It is solved on the other
layer, on the correct principle, by an instrument that already runs.** P7 says the same thing
about the ledger — *"This should reuse the existing append-only machinery, not invent a second
one … Before building a guard, look for it — it is probably already here."* The observation
extends: the *queue* pattern is also already here.

**This record does not propose building it.** It records that the pattern exists, works, and is
governed by a rule (`nothing hand-maintained`) that happens to be J.1's rule arrived at
independently.

### 4.4 · How priorities are represented

| Carrier | Source | State |
|---|---|---|
| `PRIORITY` field on the Task Contract | A.1 | field declared; **no vocabulary, no ordering, no comparator defined anywhere** |
| Ladder floor as an implicit priority | C.1 | ✅ fully specified and ordinal — R0 < R1 < R2 < R3 < R4 < R5 |
| Scientific priority | body § 41 (*first batch PICCOLO, 1–2 PMID each*) | ✅ specified for the first cycle only |
| Strategic priority | H.1 *Strategia complessiva → Operatore* | 🔴 **human by allocation, and correctly so** |

🔴 **`PRIORITY` is the one A.1 field with no defined range.** Every other field in A.1 either
names its vocabulary (`INTERACTION_MODE: AUTONOMOUS_COMPLETE | QUESTIONS_ALLOWED | SINGLE_TURN`),
points at a schema (`REVIEW_REQUIREMENT` → C.1's floors), or is free-form by intent (`OBJECTIVE`).
A queue cannot order itself on a field with no order.

### 4.5 · Executable versus blocked — the four buckets, and their single blocker

| Bucket | Predicate from frozen text | Answerable today? |
|---|---|---|
| **OPEN** | opening event with no `CLOSES_EVENT_ID` pointing at it (J.1) | 🔴 no — 0 events on 49 refs |
| **BLOCKED** | A.5 `BLOCKED`, or `AWAITING_APPROVAL` joined to an unresolved J.3 `APPROVAL_ID` | 🔴 no — 0 records carry either state, and the queue that answers the join is forked (§ 5.4) |
| **READY** | ACKed + claimed + every `DEPENDENCIES` entry closed + owner not `DOWN` | 🔴 no — no row of H.1 says who closes a dependency; `DOWN` needs a heartbeat that has never run |
| **FAILED** | attempts ≥ `RETRY_POLICY.max_attempts`, `on_exhaust` applied and recorded; A.5 `PARKED` | 🔴 no — 0 records carry `PARKED`, and F.4 `DIAGNOSE` must run first and is a judgement, not a predicate |

All four reduce to *does a closing record exist*, and none of the four can be answered.
Corroborates `AUTONOMOUS-DISPATCH-LOOP-MODEL-001` D-1 independently.

---

## 5 · DEPENDENCY CHECKER

### 5.1 · The question, and the row that does not exist

A.1 declares a `DEPENDENCIES` field on every Task Contract. **H.1 has 17 rows and none of them
allocates the act of declaring a dependency satisfied.** That is not a small omission: it is the
difference between a queue that can compute readiness and a queue that must ask someone.

### 5.2 · Which dependencies are machine-checkable

Derived from frozen text only, then measured. The classification is by **what kind of thing the
check is**, not by whether a script happens to exist.

| Class | Dependency | Machine-checkable in principle? | Instrument today |
|---|---|---|---|
| **D-1** | root clean · `BASE_HEAD` as expected · `ONE_WRITER` (GATE 0) | ✅ fully — git primitives | ⚠️ asserted by hand; `batch_commit.py` is snapshot/restore only |
| **D-2** | `ORCHESTRATOR_LEASE ACTIVE` singleton (GATE 0, I.3) | ✅ fully | ✅ **`lease_state.py`** — derives from `EXPIRES_AT`/`RELEASED_AT` and the clock, not from a stored field |
| **D-3** | `CANDIDATE_CONTENT_HASH` + `BASE_HEAD` unchanged (GATE 5, D.2) | ✅ fully — deterministic by P5 | ✅ **`candidate_content_hash.py`**, independently reproducible |
| **D-4** | `LINT PASS` + `publication gate PASS/0` in the same window (GATE 2) | ✅ fully | ✅ **`legend_lint.py`**, **`public_release_gate.py`** — both PASS this session |
| **D-5** | checkpoint compatibility: `directive_version` + `generation` + fingerprint (A.6) | ✅ fully | ⚠️ **half** — `governance_fingerprint.py compose` exists; nothing compares a checkpoint against it |
| **D-6** | governance fingerprint pertinence (A.6, P2) | ✅ fully | ✅ `governance_fingerprint.py` |
| **D-7** | artifact resolves at a pinned blob (C.2 `OBJECT`) | ⚠️ **only if the ref is carried** — a path without a ref is not an address | 🔴 no schema requires a ref field |
| **D-8** | reviewer availability: `VERIFIED` capability (I.4, body § 8) + C.3's cap of one active review per Scientist | ⚠️ in principle | 🔴 **the input surface disagrees with itself** — § 5.5 |
| **D-9** | independence: `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR`, rotation, no contributed evidence (C.3) | ⚠️ in principle, given a durable record of who did what | 🔴 no such record exists |
| **D-10** | actor liveness — `DOWN` after 3 missed heartbeats (B.3, P4) | ✅ fully | 🔴 no heartbeat has ever run |
| **D-11** | cost envelope — `DEFAULT_EXTERNAL_SPEND = 0` (J.4) | ✅ by construction | ✅ **satisfied with no instrument at all** |

### 5.3 · 🔴 The property that separates D-11 from all the others

D-11 needs no registry, no event and no script, and it is the only precondition in the table that
is reliable today. The reason generalises:

> **Its default is "no".** A missing record produces a refusal. Every other precondition in the
> table fails **open** when its record is missing — an independence check with no data to check
> against does not block the review, it simply does not happen.

**The preconditions that need instruments are exactly the ones whose default is "yes".** This is
the design lesson the cost policy already embodies and nothing else does. It also explains why the
laboratory's *safety* properties have held while its *coordination* properties have not: the
safety rules were written fail-closed and the coordination rules were written fail-open.

### 5.4 · The three-state split the dispatch asks for

```
READY                      every dependency of the task is closed, the owner is live,
                           the object resolves at its pinned blob, and no gate refuses
                           → COMPUTABLE for D-1…D-6, D-11.  NOT computable for D-7…D-10.

BLOCKED_BY_SYSTEM          a precondition is unmet for a reason a machine could establish
                           → today this class is INDISTINGUISHABLE from the next one,
                             because the records that would separate them do not exist

BLOCKED_BY_HUMAN_DECISION  an object sits in J.3's HUMAN_APPROVAL_QUEUE unresolved,
                           or the act is allocated to the operator by H.1
                           → the queue EXISTS.  Measured state below.
```

**The `HUMAN_APPROVAL_QUEUE`, measured across all 49 refs this session:**

| Ref group | Distinct `APPROVAL_ID` + `RESOLUTION_ID` | States present |
|---|---|---|
| `main` and 20 other refs | **4** | `PENDING`, `APPROVED` |
| `orchestrator` | **12** — adds SUNSET-DEC3, P5DOMAIN, SCIAB, XPORT | `PENDING`, `APPROVED` |
| `evidence-index`, `p51c9-rebased-onto-c89c2217` | **12** — adds HA-1…HA-4 | `PENDING`, `APPROVED`, 🔴 `DEFERRED`, 🔴 `RESOLVED` |

🔴 **The union is 20 identifiers (10 approval objects and their resolutions). No single ref
carries it.** `orchestrator`'s twelve and `evidence-index`'s twelve are different twelves —
neither is a subset of the other — and `main` carries four. A Director standing on `main` and
asking *"what is waiting for the human?"* gets an answer that is wrong by sixteen identifiers, and
nothing tells it so.

🔴 **`DEFERRED` and `RESOLVED` are not in J.3's vocabulary**, which is
`PENDING | APPROVED | APPROVED_WITH_MODIFICATION | DENIED | REVISION_REQUESTED`. The same drift
the lease record documents about its own `EXPIRED` value. Nothing detects either.
Independently reproduces `AUTONOMOUS-DISPATCH-LOOP-MODEL-001` B-7 and B-8 at a different
granularity — that record counted approval objects, this one counted every identifier.

### 5.5 · 🔴 The dependency checker's input surface contradicts itself

Both files are on branch `orchestrator`, committed the same day:

```
runtime/agent_card_registry.md   23 occurrences of UNVERIFIED, 0 capability rows VERIFIED
runtime/L2-OUTCOMES.md           "3 VERIFIED of 12 attempted"
                                 O4  lease acquire · renew · observe expiry     VERIFIED
                                 S2  scientist worktree confinement             VERIFIED
                                 S4  scientist capability per plan              VERIFIED
                                 — ratified by "operator decision of 2026-08-18 §1"
```

Body § 8 and I.4 make this consequential rather than cosmetic: *"Orchestrator assegna sulle
capabilities **verificate**, non sul ruolo presunto."* Body § 43 says which is authoritative —
*"riga stantia = non autoritativa"* — but **no rule says who reconciles them**, and until someone
does, the readiness predicate for D-8 reads one of two contradictory inputs depending on which
file it opens.

---

## 6 · ROLE RESOLUTION

### 6.1 · The four questions the dispatch asks, answered against frozen text

**(a) Who should execute this task?** — Fully specified and fully mechanical.

```
C.4 / body § 23   EVIDENCE   → Scientist + Plan (provenance)
                  INFERENCE  → peer Scientist
                  SYSTEM     → Mirror

C.1               L1 ordinary observation          → floor R0
                  L2 important inference           → floor R1
                  therapeutic-actionable inference → floor R2
                  persistent scientific disagreement → floor R3
                  methodology-changing process     → floor R4
                  specified cross-model cases      → floor R5
                  derogable only UPWARD; below the floor only with recorded rationale
```

🔴 **These two mappings contain no discretion.** Object class → reviewer class is three-way and
total. Claim class → floor is six-way, ordinal and total. Both are frozen, both are unambiguous,
and a function implementing them would have no parameters to tune. **The hard part of role
resolution is already written down.**

**(b) Does the actor exist?** — I.4 defines the Agent Card: `ACTOR_ID` (permanent), `ROLE`,
`WORKTREE`, `ROLE_CONTRACT_HASH`, `CAPABILITIES[]`, `CURRENT_SESSION_REF` (ephemeral), `STATUS`,
`LAST_SEEN`. A registry instance exists on branch `orchestrator`, self-described as
`PARTIALLY REGISTERED — 3 of 6 cards`. Two Scientists remain unregistered.

**The dispatch says: do not invent a registry. It is not invented, and it is not needed to be —
one exists.** Its problems are staleness (§ 5.5) and reachability (it is on one ref), not absence.

**(c) Is the capability verified?** — I.4 is explicit and fail-closed: a declared capability is
`UNVERIFIED` until L2 smoke-tests it, *"CONFIGURED != PROVEN applicato alle capacità"*, and
*"una capability con fallimenti ripetuti torna UNVERIFIED"*. The rule is sound. Its input is the
contradiction in § 5.5.

**(d) Is the actor available?** — Three separate conditions, and this is where the office breaks:

| Condition | Source | State |
|---|---|---|
| not `DOWN` | J.2 state machine, fed by B.3 heartbeat | 🔴 **never derivable — no heartbeat has ever run** |
| not at C.3's cap of one active review | C.3 | 🔴 no durable record of open reviews per actor |
| **reachable** | B.1 `TO (ref)` | 🔴 **`ACTOR_ID` is identity, not a route; `SESSION_REF` is a route and is not observable by its own holder** |

### 6.2 · 🔴 The gap, named precisely

> **Role resolution is not blocked on judgement. It is blocked on an address.**

Steps (a) and the *rules* of (d) are deterministic functions over frozen text. Step (b) has a
registry. Step (c) has a rule with a contradictory input. **Step (d)'s last row is the one that
has no answer at all**: the governance distinguishes stable identity (`ACTOR_ID`) from ephemeral
routing (`SESSION_REF`) correctly — body § 21, *"Il `from` è routing; l'identità è l'ACTOR_ID"* —
and then provides no mechanism by which an actor learns its own `SESSION_REF` or by which a
Director resolves an `ACTOR_ID` to one.

Every actor that has faced this declined to invent a value. The Plan checkpoints record the
refusal in almost identical language across four generations: *"NOT DECLARED — an actor cannot
observe its own routing reference (ListAgents shows peers only)."* **That refusal is correct and
it is why the problem is still visible rather than papered over with a guess.**

### 6.3 · Fallback when no eligible actor resolves

The governance defines no fallback. The **observed** fallback is consistent and correct:
escalation to the operator, under F.2's `ESCALATE` and H.1's operator rows. The measured instance
is `REV-ROLES-MIRROR-001`, which emitted **no verdict** on `roles/mirror.md` because the only
eligible reviewer was the author, and referred it upward rather than resolving it conveniently.

🔴 That is a role-resolution *failure* handled exactly as a Director should handle one, by an
actor with no Director. It is evidence that the escalation discipline works without the
infrastructure — and evidence that the infrastructure is what is missing, not the discipline.

---

## 7 · HANDOFF GENERATION

### 7.1 · The minimum information for an autonomous transfer

Each field below is derived from an annex that already requires it, or from an existing artifact
that already carries it. **Nothing is newly required here**: requiring anything of a B.2 `HANDOFF`
would be a change to a FROZEN annex, which this record does not propose.

| Dispatch field | Minimum carrier | Frozen source | Carried by an existing artifact? |
|---|---|---|---|
| **source artifact** | `(ref, path, blob)` — a path alone is not an address | C.2 `OBJECT`; D.2 binds hash **+** `BASE_HEAD` | ⚠️ **by choice, not by schema.** `HANDOFF-SCIENTIST-AB-SPEC` carries `carried_from: branch … commits …` and a sha-256 of the body; `HANDOFF-XPORT-MIRROR` distinguishes `BASE_HEAD` / `CONTENT_TIP` / `MANIFEST_TIP` as three separate oids |
| **destination actor** | `ACTOR_ID` (identity) **and** a route | B.1 `ACTOR_ID` / `TO`; I.4 | 🔴 identity yes, route no. `HANDOFF-XPORT-MIRROR` states it outright: *"to: mirror — **DELIVERY IS THE OPERATOR'S**, deliberately"* |
| **expected output** | `DELIVERABLE` + `MILESTONE_PLAN` with the durable evidence each milestone must leave | A.1 (E2) | ✅ `SCIENTIST-AB-SPEC-001` carries an 8-entry `MILESTONE_PLAN`, each with `durable_evidence` |
| **validation criteria** | `ACCEPTANCE_CRITERIA` (verifiable) + `REVIEW_REQUIREMENT` (C.1 floor) | A.1; C.1 | ✅ present in the task records |
| **dependency state** | `DEPENDENCIES` + `CURRENT_STATE (durable pointer)` + `APPLICABLE_GOVERNANCE_FINGERPRINT` | A.1; A.6 | ⚠️ fingerprint yes (computable today); `DEPENDENCIES` as a **closed/open** state, no |

### 7.2 · Comparison with the existing HANDOFF artifacts

**14 distinct handoff paths across 49 refs**, in six namespaces (`governance/candidates/`,
`runtime/handoff/`, `release/`, `framework/protocols/`, `.claude/skills/`, and inline references).
No two share a schema. Read closely, the best of them are *better* than anything the governance
requires — and that is the finding.

| Practice observed | Where | Required by any annex? |
|---|---|---|
| source ref + commit oids + sha-256 of the body, with the discrepancy between file-hash and body-hash **explained in advance** | `HANDOFF-SCIENTIST-AB-SPEC` frontmatter | ❌ no |
| three distinct oids named separately (`BASE_HEAD`, `CONTENT_TIP`, `MANIFEST_TIP`) with the invariant that must hold across them | `HANDOFF-XPORT-MIRROR` § -R2 | ❌ no |
| runnable commands the receiver executes to verify the object **without merging** | `HANDOFF-XPORT-MIRROR` | ❌ no |
| `scope_rule: SCOPE MUST NOT BE REDUCED` | `HANDOFF-SCIENTIST-AB-SPEC` | ❌ no |
| an explicit statement of who has **not** opened the review — *"opened_by: nobody yet. Annex C.3: a review is opened only through Orchestrator"* | `HANDOFF-XPORT-MIRROR` | ❌ no |
| preconditions **independently verified, not relayed** | `HANDOFF-SCIENTIST-AB-SPEC` § 2 | ❌ no |

🔴 **The senders are already writing a better handoff than the constitution asks for.** B.2 lists
`HANDOFF` in an enumeration of message types and says nothing further — no envelope beyond B.1,
no required field, no state effect, no closure. Every good practice in the table above is an
individual author's discipline, reinvented each time, and therefore available on the day the
author is careful and absent on the day they are not.

### 7.3 · 🔴 The missing half is the receiver

**14 handoff artifacts. Zero receiver-side records.** No counterparty `TASK_ACK` exists for any
task: three of the five task records carry a `TASK_ACK` block and all three are **self-written**;
all five carry a `TASK_CLAIM` with `claimed_by == OWNER == plan`.

This matters because J.0 names the compensating protocol for the guarantee LEGEND does not have:

```
J.0   Exactly-once / delivery garantita  →  ACK + dedup MESSAGE_ID + reinvio + DIAGNOSE (B.3, F.4)
```

**The compensator is specified and has never engaged.** Without a receiver record, *"handed off"*
and *"received"* are the same durable state, and body § 18's rule decides the question from the
other side: *"Ciò che non è nello stato durevole non è accaduto."*

Reproduces `AUTONOMOUS-DISPATCH-LOOP-MODEL-001` D-4.1. The count differs (14 here, 15 there) and
the difference is the predicate: this sweep counts distinct paths whose basename or directory
matches `HANDOFF`, deduplicated across refs.

### 7.4 · The field with no name

The most consistently written field in this laboratory's practice appears in four artifacts under
four different names, and in **no normative text at all**:

```
NOT_DONE_DELIBERATELY            ledger/checkpoints/plan/CHK-plan-0019.json
OUT_OF_SCOPE                     governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md
deliberately_not_touched         ledger/tasks/plan/SCIENTIST-AB-SPEC-001.json
"What this record does NOT do"   four sibling analyses, and § 13 of this one
```

🔴 A field every careful author writes, that no schema names, is a field the next author will
invent again — or omit. Naming it is a governed change and is not proposed here. Recorded as
`L-3` (§ 12), and credited: `AUTONOMOUS-DISPATCH-LOOP-MODEL-001` D-3 raised it first, from three
of the same four instances.

---

## 8 · HUMAN ESCALATION — the taxonomy

Built directly from body § 4, Annex H.1 and Annex J.3 — **not** from a sibling's map, so the two
can be compared as independent derivations.

### 8.1 · Body § 4's taxonomy, classified row by row

The body's own `TASSONOMIA HUMAN_REQUIRED` has **12 rows**. Every one is reproduced and assigned
to exactly one class.

| # | Event (§ 4) | System continues? | Human? | Class |
|---|---|---|---|---|
| 1 | Difficult paper / unreadable PDF / validator FAIL | yes — retry per A.1 | no | **B** |
| 2 | Scientist disagrees with Orchestrator | yes (§ 9) | no | **B** |
| 3 | Slow Scientist | yes — rebalancing | no | **B** |
| 4 | Scientist crashed | others continue | yes — *only to reopen the UI* | **C-runtime** |
| 5 | Chat/window closed | others continue | yes — rebootstrap if needed | **C-runtime** |
| 6 | Ambiguous scientific problem | yes — Review Ladder | *normally no* | **B** |
| 7 | **Any spend** (J.4, `DEFAULT_EXTERNAL_SPEND = 0`) | **NO, before the spend** | yes | **A** |
| 8 | **MAJOR batch** (§ 12) | the rest continues; the MAJOR waits | yes, asynchronous | **A** |
| 9 | **Significant destructive/irreversible operation** | waits | yes | **A** |
| 10 | **Governance / authority model change** | waits | yes | **A** |
| 11 | **Strategic conflict unresolvable by the rules** | independent work continues | yes | **A** |
| 12 | Orchestrator DOWN → `LAB_STATE = ORPHAN` | — | yes — *to reopen it* | **C-runtime** |

```
A  · must always remain human        5 of 12   (42%)
B  · already delegated by the text    4 of 12   (33%)
C-runtime · human hands, not human judgement   3 of 12   (25%)
```

### 8.2 · Class A — decisions that must always remain human

Five § 4 rows, plus what H.1 and the body add. **This list should not shrink, and the analysis
does not try to shrink it.**

| # | Decision | Why it is not delegable | Source |
|---|---|---|---|
| **A-1** | **Any external spend** | `DEFAULT_EXTERNAL_SPEND = 0`; spend requires an approved `BUDGET_ENVELOPE`; § 48 makes cost without approval a stop condition | J.4; § 4; § 48 |
| **A-2** | **MAJOR approval** | GATE 3: `Plan candidate → Mirror hostile review → MIRROR PASS → HUMAN_APPROVAL → commit`. And `APPROVAL ≠ AUTHORIZATION` (E4) — approval authorizes the intent, never execution outside the gates | § 12; D.4; J.3 |
| **A-3** | **Governance / authority-model change** | H.1 is itself marked `[MAJOR]`; changing it needs the full gate 3 | H.1; § 12 |
| **A-4** | **Overall strategy and scientific scope** | *Strategia complessiva → Operatore.* Orchestrator orders work **within** a scope; it does not set the scope | H.1 |
| **A-5** | **Significant destructive or irreversible operations** | § 4; and § 48 forbids proceeding past any point that could lose dirty work, overwrite state, delete an uncensused worktree or compromise provenance | § 4; § 48 |
| **A-6** | **Strategic conflict the rules cannot resolve** | § 4 — and note the design: *independent work continues* while it waits | § 4 |
| **A-7** | **Persistent scientific disagreement** | Floor `R3 TRIADIC`, derogable only upward. And `DISAGREEMENT_UNRESOLVED` with explanation is a **legitimate outcome** — forced synthesis is an error | C.1; § 27 |
| **A-8** | **Anything therapeutic** | Not medical advice; supports discussion with a treating clinical team, never substitutes for one | root `CLAUDE.md` |

🔴 **A-7 is the one that most directly protects rigor, and it protects it by refusing to
converge.** Body § 27 makes an unresolved disagreement a legitimate output. Any autonomy design
that treats disagreement as a queue item to be cleared would be optimizing against the
constitution.

### 8.3 · Class B — decisions the frozen text already delegates

These require no change of any kind. They are already allocated away from the human and, on the
scientific layer, already exercised.

| # | Decision | Delegated to | Source |
|---|---|---|---|
| **B-1** | Retry after a failed read, unreadable PDF or validator FAIL | the actor, per `RETRY_POLICY`; `on_exhaust` default `PARK` | A.1; P1; § 4 |
| **B-2** | Disagreement with an operational directive | graduated — ADVISORY comply+record; MATERIAL communicate-then-proceed on timeout | § 9.1; F.1 |
| **B-3** | Rebalancing a slow actor | Orchestrator — task/priority/reassignment | H.1; § 4 |
| **B-4** | An ambiguous scientific problem | the Review Ladder — *normally no human* | § 4; C.1 |
| **B-5** | Which reviewer, at which Ladder level (≥ floor) | Orchestrator | H.1; C.1 |
| **B-6** | Scientific conclusions | the responsible Scientist — *subject to review, never to an order* | H.1; § 2 |
| **B-7** | Structural integration, and refusal on provenance/schema grounds | Plan (`INTEGRATION_BLOCK`) | H.1; § 28 |
| **B-8** | Epistemic/method review; MAJOR classification when doubtful | Mirror (fail-closed) | H.1 |
| **B-9** | Ordinary `HUMAN_REQUIRED` classification | Orchestrator | H.1 |
| **B-10** | Challenge adjudication, with recorded rationale | Orchestrator — `ACCEPT \| MODIFY \| OVERRIDE_WITH_RATIONALE \| ESCALATE` | H.1; F.2 |
| **B-11** | `WORK_COMMIT` at milestone granularity | every actor, own branch | H.1; D.1 |

### 8.4 · Class C — blocked today *only* because infrastructure is missing

**The dispatch's third category, and the largest.** Each row is coordination the constitution
already permits a non-human actor to perform, that a human performs today because a record, an
address or an instrument is absent.

| # | Currently human | What makes it infrastructure and not judgement | Blocked on |
|---|---|---|---|
| **C-1** | **Being the transport between actors** — relaying handoffs, review requests, completions | B.1 already defines the envelope; § 21 already says *"messaggi = pointer, stato durevole decide"*. `HANDOFF-XPORT-MIRROR` records the operator as transport **by design decision, for want of an alternative** | no route from `ACTOR_ID` (§ 6.2) |
| **C-2** | **Knowing what is awaiting a human decision** | J.3 fully specifies the queue object and it exists | the queue is forked across refs; no ref carries the union (§ 5.4) |
| **C-3** | **Finding which ref carries an artifact** | a 49-ref sweep is a loop; performed by hand repeatedly this session | no ref field in any address (§ 7.1) |
| **C-4** | **Noticing an unanswered review** | a join over two file sets — measured 7 against 40 | no instrument reads `reviews/` |
| **C-5** | **Detecting a dead or absent actor** | B.3 + P4 specify it completely: 30-minute cadence, `DOWN` after 3 misses | no heartbeat has ever run |
| **C-6** | **Detecting a duplicated claim on one task** | A.3's uniqueness is *"by organizational construction"*; detection is a scan for two claims on one `TASK_ID + GENERATION` | no event stream |
| **C-7** | **Assembling the `OPERATOR_DAILY_BRIEF`** | § 10.4 enumerates its contents exactly, and every input is a durable file | 0 instances on 49 refs |
| **C-8** | **Reconciling the Agent Card registry against L2 outcomes** | body § 43 already says the stale row is not authoritative | no rule says who reconciles (§ 5.5) |
| **C-9** | **Answering "what is open, ready, blocked or failed"** | the four predicates are frozen and unambiguous | 0 events on 49 refs (§ 4.5) |
| **C-10** | **Watching the lease window between turns** | `lease_state.py` derives the state correctly whenever it is run | nothing runs when no actor is running (§ 10.2) |

```
A  · irreducible human judgement       8   recurring per decision
B  · already delegated by frozen text 11   no change required
C  · blocked on infrastructure only   10   each blocked on an absent record, address or instrument
```

🔴 **The accounting is the finding.** The human's load in this laboratory is not dominated by
strategy. It is dominated by **transport and reconciliation** — ten mechanical steps, of which
none is a judgement about evidence and none requires an authority the human holds. The eight
strategic gates are genuinely irreducible and are not where the cost is.

This corroborates `CONTROL-PLANE-RECONCILIATION-ANALYSIS-001`'s G-D (6 / 8 / 9) from an
independent derivation: that record built its map from measured interventions, this one from the
rows of § 4 and H.1. The two populations are constructed differently and land in the same place.

**This record does not recommend building any C row.** Each is reported with what it is blocked
on, and the authority to build any of them is allocated to nobody today.

---

## 9 · AUTONOMY METRIC

### 9.1 · What the governance already specifies

```
AUTONOMY LEDGER (G.3, body § 3)
    HUMAN_REQUIRED  PREVENTABLE vs UNAVOIDABLE
    ore bloccate · lavoro proseguito durante HITL · false escalation
    voluntary supervision EXCLUDED — it does not count as HITL
GOAL     § 3 — reduce PREVENTABLE.  Weekly synthesis in the DAILY_BRIEF.
OWNER    Mirror (G.3), whose designated primary analysis surface is the
         consolidated EVENT LEDGER (J.1) — "non leggendo le chat"
```

Measured across 49 refs, each with a positive control:

```
AUTONOMY LEDGER instances                       0
OPERATOR_DAILY_BRIEF (its weekly carrier)       0    — § 10.4 requires it once per working day
consolidated event ledger (its input surface)   0
active_lessons/                                 0
LEARNING_INDEX                                  0    — § 15 makes consulting it MANDATORY
control:  ^roles/                             108 paths on 27 refs
```

🔴 **Every claim that any change raised or lowered human load — including every claim in this
record — is currently unfalsifiable.** Independently reproduces
`SCIENTIFIC_PIPELINE_LIFECYCLE-MODEL-001` T-5 and `AUTONOMOUS-DISPATCH-LOOP-MODEL-001` A-1.

### 9.2 · The dispatch asks for four causes; G.3 defines two

The dispatch requires human effort to be attributed to **scientific judgement / governance /
missing infrastructure / missing automation**. G.3's vocabulary is `PREVENTABLE` / `UNAVOIDABLE`.

```
scientific judgement    ≈  UNAVOIDABLE   § 8.2 rows A-7, A-8.  Structural. Should never fall.
governance              ≈  UNAVOIDABLE   § 8.2 rows A-1…A-6.   Structural. Should never fall.
missing infrastructure  ≈  🔴 NO CLASS   § 8.4 C-1…C-10.  Not structural; falls when a record,
                                          an address or an instrument exists — not when anyone
                                          classifies better.
missing automation      ≈  🔴 NO CLASS   the subset of the above where the specification is
                                          complete and only the code is absent (C-5, C-7, C-9)
```

🔴 **Under G.3 as written, the two right-hand causes must both be booked as `PREVENTABLE`.**
Technically correct — they *are* preventable, by building the thing — and operationally
destructive, because it merges *"the classifier made a bad call"* with *"the laboratory has not
built the instrument yet."* Those have different owners, different remedies, and opposite
implications for whether the classification process is working.

**This record does not adopt a third or fourth class and may not.** G.2 places
*autonomy-classification methodology* among the things **Mirror may not change alone**; the flow
is `proposal → Plan candidate → independent reviewer chosen by Orchestrator → validation; if
governance → operator`. Recorded as `L-1` (§ 12). Nothing is renamed.
`AUTONOMOUS-DISPATCH-LOOP-MODEL-001` D-1 raised the three-class version of this first; the
dispatch's fourth cause (*missing automation* as distinct from *missing infrastructure*) is a
further split and is recorded, not adopted.

### 9.3 · What a meter would need, given what exists

```
INPUT     J.1's HUMAN_REQUIRED_OPENED + APPROVAL_RESOLVED, joined by APPROVAL_ID
          to the J.3 queue object every HUMAN_REQUIRED is required to create (§ 4, J.3)
DERIVED   ore bloccate      = APPROVAL_RESOLVED.ts − HUMAN_REQUIRED_OPENED.ts
          lavoro proseguito = events by other actors inside that interval
          false escalation  = a HUMAN_REQUIRED whose resolution cites a rule that
                              already answered it
EXCLUDED  voluntary supervision — § 3, explicitly not HITL
```

Two of the three inputs are event types that have never been emitted. The third — the J.3 queue —
exists and is forked with two out-of-vocabulary states in it. **A meter built on today's
substrate would measure the substrate, not the laboratory.**

🔴 **One measurable proxy does exist and is worth naming**, because it needs no new instrument:
`ore bloccate` for the approvals that *have* been resolved is computable today from the queue's
own `REQUESTED_AT` and `RESOLVED` fields, on any ref that carries the object — **and it would be
wrong**, because the union of the queue is not on any ref. The proxy is blocked by a
reconciliation, not by an absence. That is a C-class blocker (§ 8.4, C-2), not an A-class one.

---

## 10 · THE 12-HOUR QUESTION

### 10.1 · The literal question asks for something § 34 forbids

> *"Niente job invisibili: **autonomia ≠ invisibilità**."* — body § 34, with
> `INTERACTION_PROFILE: VISIBLE_VSCODE` and *"persistent, visible, inspectable, interactive
> actors"* named as a **core property**.

Unattended execution is not an unbuilt feature in LEGEND; it is outside the design. So the
question has two forms and both are answered:

- **literal form** — *what executes with nobody present?* → § 10.2
- **answerable form** — *with the actors' sessions open and the human not answering, what
  proceeds and what halts?* → § 10.4

The distinction matters: a model built to satisfy the literal form would be designing against
§ 34. `AUTONOMOUS-DISPATCH-LOOP-MODEL-001` H-2 makes the same split for a 24-hour horizon and it
is right.

### 10.2 · Literal form — measured

| Mechanism | Measured |
|---|---|
| Hooks | **1** — `PreToolUse` / `Bash` → `scripts/guard_bash_command.py`. Fires only **inside** an actor's turn |
| `SessionStart` hook | none |
| Scheduler / cron | none — no `schedule:` key anywhere in `.github/` or `.claude/` |
| CI | 1 workflow, `public-release-gate.yml`, triggered by `push` · `pull_request` · `workflow_dispatch` — **all human-initiated** |

**In 12 hours with no human, the number of processes that execute is zero.** Not "few". Zero.
Every gate, validator and derivation in this repository — including the five that returned PASS
this session — runs only when someone opens a turn.

### 10.3 · 🔴 The clock inventory — and why 12 hours is not a meaningful horizon

This is the measurement that decides the question, and it has not been made before. LEGEND has
exactly four time-dependent mechanisms. Every one of them completes inside the **first 90
minutes**.

| Clock | Value | Source | Fires at |
|---|---|---|---|
| `ACK_TIMEOUT` | 30 min → resend; 2nd miss → `BLOCKER` | P3 `[PROVISIONAL]` | **T+30 / T+60** |
| `HEARTBEAT_CADENCE` | 30 min; `DOWN` after 3 consecutive misses | P4 `[PROVISIONAL]` | **T+90** |
| `ORCHESTRATOR_LEASE` TTL | computed from all five records as `EXPIRES_AT − LAST_RENEWED`: **2 min** (#1, the only lease ever renewed), **40 min** (#2, #3), **60 min** (#4, #5). Longest = 60 | I.3; `runtime/orchestrator_lease.md` | **T+2 … T+60** |
| PROVISIONAL practice expiry | *"after the third scientific batch"* | P3.1, P4.1; E.3 | **never — see below** |

```
T+0        the human stops answering
T+2..60    any ACTIVE lease expires → STALE.  GATE 0's singleton precondition unsatisfiable.
           (2 min if it was being renewed, 60 min at the longest TTL ever issued)
T+30       first unACKed state-changing message resends
T+60       second miss → BLOCKER raised
T+90       every silent actor is DOWN → tasks PARKED or reassigned at generation+1
─────────  ▲ every governance clock in the system has now fired
T+90 … T+12h    NOTHING FURTHER CHANGES BY THE PASSAGE OF TIME
```

🔴 **The 12-hour horizon is eight times longer than the longest clock LEGEND owns.** Hour 2 and
hour 12 are structurally identical states. The dispatch could have asked about 2 hours, 12 hours
or 12 days and the answer would be the same list — which means **the horizon is not a variable in
this system**, and any model that treats it as one is modelling something LEGEND does not have.

🔴 **And the fourth clock can never fire.** Both P3 and P4 are registered `PROVISIONAL` under
E.3 with the expiry *"after the third scientific batch — PROMOTE | REJECT | EXTEND_WITH_REASON"*.
Measured:

```
governance/GOVERNANCE_v3.1.1.md   materialized_on:          2026-08-16
framework/state/…manifest         last_batch_commit_date:   2026-08-15   (BATCH_20260815_001)
```

**The last scientific batch predates this governance by one day. Zero of the three have occurred.**
E.3 is explicit — *"Mai provisional per sempre"* — and the two parameters that govern LEGEND's
only two time-based failure detectors are provisional against a counter that has never advanced.
Neither can be promoted, rejected or extended, because the condition that would trigger the review
has not happened once.

### 10.4 · Answerable form — what continues and what stops

```
CONTINUES ─ each actor finishes the task it holds under a valid contract, then parks     § 9.4
          ─ WORK_COMMIT on the actor's own branch                          H.1, "ogni attore"
          ─ Plan continues preparation                                                   § 9.4
          ─ Mirror continues reviews already open                                        § 9.4
          ─ every mechanical validator and gate, ON DEMAND inside a turn             measured
          ─ LAB_STATE = ORPHAN; nobody promotes themselves                          § 9.4, I.3

STOPS — because the governance decided it should.  This list is correct and should NOT shrink.
          ─ CANONICAL_BATCH_COMMIT      GATE 0 needs an ACTIVE lease singleton; measured 0,
                                        and I.3 forbids self-promotion to obtain one
          ─ any spend                   J.4 DEFAULT_EXTERNAL_SPEND = 0
          ─ any MAJOR                   GATE 3: Mirror PASS *and* HUMAN_APPROVAL
          ─ any destructive/irreversible operation                             § 4; § 48
          ─ persistent scientific disagreement    C.1 floor R3, derogable only upward
          ─ public push                 a human reading the diff before it is published
          ─ anything therapeutic        never a substitute for a treating clinical team

STOPS — because a record is missing or an address does not resolve.  NOT a decision.
          ─ new task assignment         needs VERIFIED capabilities; the registry says 0
                                        while L2-OUTCOMES ratifies 3            § 5.5
          ─ review opening              Orchestrator-only (C.3), and there is no ACTIVE one
          ─ every cross-actor handoff   no route from ACTOR_ID; the human is the transport § 6.2
          ─ any open/ready/blocked/failed question    0 events on 49 refs        § 4.5
          ─ knowing what is pending     the approval queue is forked; no ref carries the union
```

🔴 **The two lists look identical from outside.** Both present as *"waiting for the human."*
Neither the operator nor any actor can currently tell them apart, because the instrument that
distinguishes them — the `AUTONOMY LEDGER`'s `PREVENTABLE` / `UNAVOIDABLE` split — has never been
instantiated (§ 9.1).

**That is the honest answer to the dispatch's question.** What LEGEND can safely continue doing
for 12 hours is: finish held work, commit it durably, park cleanly, and refuse everything that
touches the canon, the money or the public surface. What must stop, stops correctly. **What
should not stop — but does — is every act of coordination**, and it stops for want of an address,
not for want of a decision.

---

## 11 · THE PERCENTAGE ANSWER

> *"What percentage of future LEGEND work can become autonomous without reducing scientific
> rigor?"*

### 11.1 · The denominator problem, stated before the number

"Work" is not a measurable unit in this repository today. § 9.1 measures why: the autonomy ledger
has **0 instances on 49 refs**, so hours-per-decision, decisions-per-batch and work-blocked-per-
escalation are all unobserved. **Any percentage of *work* would be a fabricated ratio.**

What *is* countable is a closed, frozen, auditable population: **the decision points the
constitution enumerates.** Body § 4 has exactly 12 rows. Annex H.1 has exactly 17. Section 48 has
exactly 10 stop conditions. These are not samples and not estimates — they are the whole
population, and anyone can recount them.

**The number below is a percentage of enumerated decision points, not of work.** Stated that way
it is verifiable; stated any other way it would not be.

### 11.2 · Three measurements over three named populations

**(a) Annex H.1 — 17 authority rows, by holder**

```
Orchestrator                                   5   task/priority/generation · Ladder+reviewer ·
                                                   CANONICAL_BATCH_COMMIT · HUMAN_REQUIRED
                                                   classification · challenge adjudication
Plan                                           3   integration/candidate · INTEGRATION_BLOCK ·
                                                   fingerprint composition
Mirror                                         2   epistemic/method review · doubtful MAJOR
Scientist responsabile                         1   scientific conclusion
ogni attore                                    1   WORK_COMMIT
split / procedural (no single holder)          3   learning lifecycle (authority column is "—") ·
                                                   Mirror method change ("mai Mirror da solo") ·
                                                   BOOTSTRAP→Orchestrator promotion (Annex I)
Operatore                                      2   spend / MAJOR approval / governance ·
                                                   overall strategy
─────────────────────────────────────────────────
allocated to a NON-HUMAN actor                15 / 17  =  88%
```

**(b) Body § 4 — 12 taxonomy rows** (§ 8.1)

```
no human required at all                       4 / 12  =  33%
human required, but as HANDS not judgement     3 / 12  =  25%    (reopen a UI, rebootstrap)
human judgement required                       5 / 12  =  42%
```

**(c) Section 48 — 10 stop conditions, by checkability**

```
machine-checkable in principle                 8 / 10   (all but "macro-upgrade without governance"
                                                         and "cost without HUMAN_APPROVAL")
has a real instrument TODAY                    3 / 10   lease singleton (lease_state.py) ·
                                                         checkpoint fingerprint
                                                         (governance_fingerprint.py) ·
                                                         hash mismatch (candidate_content_hash.py)
```

### 11.3 · The answer

**≈ 85–90 % of LEGEND's enumerated coordination decision points can become autonomous without
reducing scientific rigor. Approximately 10–15 % must remain human permanently. Today, the
realized figure on the control plane is 0 %.**

The three figures decompose cleanly, and the decomposition is the actual answer:

| | Share | What it is | What moves it |
|---|---|---|---|
| **Ceiling set by the constitution** | **88 %** (15/17 H.1 rows) | authority already allocated to non-human actors | nothing — it is already delegated |
| **Floor set by rigor** | **≈ 12 %** | the 2 operator rows of H.1; the 5 judgement rows of § 4; A-7's R3 floor and A-8's clinical boundary | **nothing should move it.** Shrinking this is how rigor is lost |
| **Realized today, control plane** | **0 %** | no task assigned, no review opened, no handoff delivered without a human | records, addresses, instruments — § 8.4's ten C rows |
| **Realized today, scientific layer** | **high, and unquantified** | a derived 415-item queue, 128 chained receipts, 64 deep-dive manifests, five gates at PASS | already working |

### 11.4 · Why the gap is 88 → 0 and what that means

**The distance between the ceiling and the realized figure is entirely category C.** Not one of
the ten C rows in § 8.4 is blocked by an authority the operator holds; each is blocked by a
missing record, a missing address or a missing instrument. And not one of them is a judgement
about evidence — § 3.2's wall guarantees that, because the Director's whole office is on the
coordination side of it.

🔴 **This is the reason "trustworthy autonomy" and "maximum autonomy" point the same way here,
which is unusual and worth stating.** In most systems, raising autonomy means moving decisions
across the judgement boundary and accepting risk. In LEGEND it does not: the 88 % is already on
the far side of that boundary by the constitution's own allocation. Building the C-class
instruments would not transfer a single scientific judgement to a machine. **It would transfer
transport and bookkeeping** — and it would, for the first time, make the two kinds of waiting
distinguishable (§ 10.4), which is itself a rigor property rather than a convenience one.

### 11.5 · What this number is not

- **It is not a percentage of work, effort or time.** The instrument that would measure those has
  0 instances (§ 9.1). A reader who converts 88 % into "the operator's day shrinks by 88 %" has
  made a claim this record does not support and cannot.
- **It is not a target.** § 3's `95/5` is the body's own goal and this record neither endorses,
  revises nor operationalizes it.
- **It is not a recommendation to build anything.** § 8.4's C rows are reported with what each is
  blocked on; the authority to build any of them is allocated to nobody today, and
  `AUTONOMOUS-DISPATCH-LOOP-MODEL-001` B-9 measured that the L2 record says so in terms.
- **It rests on a population that could be recounted differently.** H.1's three "split /
  procedural" rows could defensibly be counted as partly-operator, which would move 88 % to
  71 %. Both counts are shown so the choice is visible rather than buried.

---

## 12 · OPEN QUESTIONS

Carried questions keep the identifiers their originating record gave them. New ones use the `L-`
prefix. **None is resolved here and none is assigned to anyone.**

| # | Question | Owner per the governance | State |
|---|---|---|---|
| **Q-1** | Reading, analysis and handoff have no J.1 event type | operator (governance) / Plan (design) | **OPEN** — carried |
| **Q-2** | What identifies a dispatched object — ref, tip oid, content hash, or all three? | Plan, subject to review | **OPEN** — carried; § 7.1 measures the practice without proposing a requirement |
| **Q-6** | Does Annex B's `HANDOFF` need a schema? Annex B is FROZEN | unclear | **OPEN** — carried |
| **Q-8** | What resolves a session seen by four actors and claimed by none? | operator | **OPEN** since 2026-08-16 |
| **O-1** | `scientist_reading_modes.md`'s three activation clauses measure SATISFIED; its status line still reads `PROPOSED` | operator | **OPEN** — carried |
| **D-1** | The `temporaneo` autonomy class has no home in G.3's two-value vocabulary | G.2 flow → operator if governance | **OPEN** — carried |
| **D-2** | Who reconciles the Agent Card registry against `L2-OUTCOMES.md`? | body § 43 → Plan; operator if normative | **OPEN** — carried |
| **L-1** | 🔴 **NEW.** The dispatch asks autonomy to be attributed to **four** causes; G.3 defines **two**, and the dispatch's third and fourth (*missing infrastructure*, *missing automation*) are distinct from each other — the first needs a record or an address, the second needs only code against a complete spec. Splitting them is a change to autonomy-classification methodology, which G.2 bars Mirror from making alone | G.2 flow | **OPEN** |
| **L-2** | 🔴 **NEW.** P3 and P4 are `PROVISIONAL` with expiry *"after the third scientific batch"*. Zero batches have occurred under governance 3.1.1 — the last is `BATCH_20260815_001`, dated one day **before** the governance was materialized. E.3 forbids provisional-forever, and the counter that would end it has never advanced. Is the remedy a different expiry condition, an `EXTEND_WITH_REASON`, or a ruling that the pre-3.1.1 batches count? | Plan (P3/P4 are Plan-defined); E.3 review | **OPEN** |
| **L-3** | 🔴 **NEW (corroborating).** `PRIORITY` is the only A.1 field with a declared name and no declared range. A queue cannot order itself on a field with no order, and § 4.4 measures that every other A.1 field either names its vocabulary or is free-form by intent | Plan (schema) / operator if normative | **OPEN** |
| **L-4** | 🔴 **NEW.** The dispatch's six components include two — dependency satisfaction and handoff ownership — that **no row of H.1 allocates to anyone** (§ 3.3). A Director cannot delegate an authority the matrix does not grant, and cannot exercise one either | operator (H.1 is `[MAJOR]`) | **OPEN** |

---

## 13 · What this record does NOT do

- it does **not** create, propose or adopt a queue, an event writer, a schema, a field, a check, a
  gate, a validator or a registry;
- it does **not** emit an event, issue a task, open a review, request an approval, acquire a
  lease, or perform any commit other than the one that makes this file durable on its own branch;
- it does **not** activate, amend or read as binding any role contract — `DEC-20260822`
  consequence 2 and the operator's constraint are both in force throughout, and **no rule in this
  record is sourced from `roles/`**;
- it does **not** modify `governance/`, `roles/`, `framework/` or `ledger/` — nothing under any of
  the four was touched, and the branch diff is one added file;
- it does **not** resolve Q-1, Q-2, Q-6, Q-8, O-1, D-1, D-2 or any of L-1…L-4;
- it does **not** adopt a third or fourth autonomy class, rename G.3's two, or touch Mirror's
  methodology (G.2);
- it does **not** repair the forked approval queue, the out-of-vocabulary approval states, or the
  contradiction between the Agent Card registry and `L2-OUTCOMES.md` — each is reported with its
  evidence and left exactly as written, **because a record edited to agree with its own schema has
  stopped being evidence**;
- it does **not** recommend building any item in § 8.4, and does not assign ownership of any
  finding;
- it does **not** edit any sibling analysis, any decision record, or `main`;
- it does **not** merge any branch, and `main` is unchanged at `788c357`.

---

## 14 · VERIFICATION TRAIL

Every command was executed in this session. Sweeps labelled *49 refs* iterate
`refs/heads` + `refs/tags` + `refs/remotes` and were each run **with a positive control in the
same invocation** — see § 2.1 for why that is not a formality.

| Check | Command | Result |
|---|---|---|
| Identity — branch / base / tree | `git rev-parse --abbrev-ref HEAD`; `git rev-parse HEAD`; `git status --porcelain` | `orch-lab-director-operating-model`; `788c357d…`; empty |
| Worktree isolation | `git worktree add -b … 788c357`; `git worktree list` | own worktree; root checkout left on `main`, clean |
| Lease | `python3 framework/scripts/lease_state.py` | `ACTIVE by derivation: 0`; 5 records, all STALE/RELEASED |
| Ref surface | `git for-each-ref refs/heads refs/tags refs/remotes` | 40 · 5 · 4 = **49** |
| Event ledger | `git ls-tree -r <ref> \| grep '^ledger/events/'` over 49 refs | **0 paths on 0 refs**; control `^roles/` → **108 paths on 27 refs** |
| `ledger/consolidated/` · `active_lessons/` · `DAILY_BRIEF` · `autonomy_ledger` · `LEARNING_INDEX` | same sweep, same control | **0 each** |
| Task / checkpoint population | `git ls-tree -r <ref> -- ledger/tasks ledger/checkpoints` over 49 refs | `tasks/plan` **5**; `checkpoints/plan` **19**; `checkpoints/mirror` **8**; **nothing for orchestrator or any scientist** |
| Task `STATE` fields | `python3` over `ledger/tasks/plan/*.json` | 3 of 5 free-text arrow strings; **2 absent**; **0 bare A.5 tokens** |
| Approval queue fork | `git show "${r}:ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl"` parsed on every carrier; **ID sets compared, not line counts** | 4 / 12 / 12 variants; **20 distinct identifiers**; `main` carries 4; `orchestrator` ⊄ `evidence-index` ⊄ `orchestrator` |
| Out-of-vocabulary approval states | same parse | `DEFERRED`, `RESOLVED` on `evidence-index` and `p51c9-rebased-onto-c89c2217` |
| Capability rows | `git show orchestrator:runtime/agent_card_registry.md` | **23 `UNVERIFIED`**, 0 capability rows VERIFIED |
| L2 ratified rows | `git show orchestrator:runtime/L2-OUTCOMES.md` | *"3 VERIFIED of 12 attempted"* — `O4`, `S2`, `S4`, ratified by operator decision 2026-08-18 |
| Review objects | basename sweep over 49 refs | **40** basenames beginning `REV-`; 54 paths *containing* `REV-` |
| Author responses | same sweep | **7** `AUTHOR-RESPONSE-*`, plus 1 `REV-AUTHOR-RESPONSE-*` which is a review |
| Handoff artifacts | path sweep over 49 refs | **14 distinct paths**, six namespaces |
| Control-plane validators | `grep -rl --include='*.py'` for 9 control-plane tokens, excl. `_external_repos` | **1 of 831** (`governance_fingerprint.py` ← `APPLICABLE_GOVERNANCE_FINGERPRINT`); other 8 tokens **0**; control `framework/state` → **14** |
| H.1 authority rows | `awk` over `annex_h_authority_matrix.md` | **17 data rows**; 2 held by the operator |
| Body § 4 taxonomy rows | `awk` over `GOVERNANCE_v3.1.1.md` | **12 data rows**; split 4 / 3 / 5 as in § 8.1 |
| § 48 stop conditions | read in full | **10 clauses** |
| Hooks / scheduler / CI | `python3` over `.claude/settings.json`; `ls .github/workflows`; grep `schedule\|cron` | 1 `PreToolUse`/`Bash` hook; **no `SessionStart`**; CI `on: push · pull_request · workflow_dispatch`; **no schedule anywhere** |
| Clock values | `plan_defined_parameters.md` P3, P4; `runtime/orchestrator_lease.md` | ACK 30 min / BLOCKER at 2nd miss; heartbeat 30 min / DOWN at 3 misses ≈ 90 min; lease TTL **40 min** (#2,#3) and **60 min** (#4,#5) |
| PROVISIONAL expiry reachability | `grep materialized_on` vs `grep last_batch_commit_date` | governance **2026-08-16**; last batch **2026-08-15** → **0 of 3 batches under 3.1.1** |
| Scientific queue | `python3 framework/scripts/batch_queue.py --limit 3` | **415 unprocessed · 233 workable now**; 6 verdict classes |
| Scientific layer health | `legend_lint.py`; `public_release_gate.py`; `fulltext_receipts.py verify`; `growth_anchors.py check` | LINT **PASS** (1 pre-existing INFO) · gate **PASS / BLOCKS: 0** (4 pre-existing `[REVIEW]` lines under `disease-models/`, untouched) · **128 chained receipts, tail anchored** · anchors **PASS** |
| Corpus size | `ls` over research artifacts | 64 deep-dive manifests · 33 dossier artifacts |
| Candidate canonicality | `git merge-base --is-ancestor <content_tip> main` | SCIENTIST-AB-SPEC, P5DOMAIN, XPORT — all **CANONICAL** |
| Role contract status | `git grep -n "^status:" main -- roles/`; `git log --all -S'status: ACTIVE' -- roles/` | 4 × `PROPOSED …`; `ACTIVE` and `BINDING` **never present on any ref** |

---

**Recorded by:** a session in `BOOTSTRAP_MODE`, no lease, no `ACTOR_ID`, in a session-local
worktree on branch `orch-lab-director-operating-model` cut from `main` @ `788c357`.
**This is not a `WORK_COMMIT` under a task contract and not a `CANONICAL_BATCH_COMMIT`.** It is an
architectural analysis that claims no authority. `main` is unchanged.

🔴 **This record is itself the sixth analysis of this laboratory's coordination that a reader
standing on `main` will not find** — five siblings measured in § 2.3, plus this one. That is
§ 8.4's C-3 applied to the record that measures it: stated here rather than left for the next
reader to discover, who will, as every session in this chain has, be told the ref by the
operator.

---
artifact: AUTONOMOUS DISPATCH LOOP — minimal coordination model, v0.1, described not built
record_id: AUTONOMOUS-DISPATCH-LOOP-MODEL-001
task_id: AUTONOMOUS_DISPATCH_LOOP_MODEL_v1
dispatcher: operator
author_session: root checkout at `main` @ 788c357, no ACTIVE lease; written on branch
  `orch-autonomous-dispatch-loop`, cut from `main` @ 788c357
actor_id: NOT ESTABLISHED — see IDENTITY. This record is not authored under a role contract.
date: 2026-08-22
governance_version: 3.1.1 (read, not exercised)
classification:
  - DESIGN ANALYSIS ONLY
  - NOT GOVERNANCE
  - NOT A SPECIFICATION
  - NOT EXECUTION AUTHORIZATION
domain: >
  CONTENT. `CONTROL_PLANE_ROOTS` (plan_defined_parameters.md § P5.1) are exhaustively
  `governance/candidates/`, `ledger/`, `reviews/`. `learning/` is CONTENT by explicit intent,
  stated in that same section. This record therefore moves the candidate hash of any future
  candidate that re-aligns onto its branch, exactly as the declaration says it must.
not_an_slr: >
  This is NOT a Session Learning Record. Annex E.6 governs `SLR-*`; it does not govern this.
  The name is deliberately not `SLR-` so the two are not conflated.
authority_claimed: none
---

# AUTONOMOUS DISPATCH LOOP — MODEL 001

> **DESIGN ANALYSIS ONLY · NOT GOVERNANCE · NOT A SPECIFICATION · NOT EXECUTION AUTHORIZATION**
>
> Nothing here assigns work, activates a contract, confers authority, adopts a field, resolves a
> finding, builds a queue, or authorizes any session to open. Every rule cited is cited from the
> governance body or a named annex. Every number was measured in this session.

---

## TASK_STATUS

**Dispatch received:** define the minimal model of a LEGEND Autonomous Dispatch Loop v0.1,
answering *"if the human director disappears for 24 hours, which parts of the laboratory can
continue autonomously and which must necessarily stop?"* — analysing seven areas: event model,
task queue model, dependency checker, role resolver, handoff generator, human escalation,
autonomy ledger.

**Mode:** `READ_ONLY_MEASUREMENT → CREATE_ANALYSIS_RECORD_ONLY`. One file written, on a branch
of its own. `main` is untouched and unchanged at `788c357`.

**What the dispatch itself constrains.** It says *"Non creare una queue. Descrivere il modello"*
and *"NON progettare un Orchestrator più intelligente. Progettare un sistema di coordinamento."*
Both are followed literally: nothing is constructed, and no capability is proposed for the
Orchestrator that the governance does not already allocate to it.

### 🔴 One governance hold applies to this subject matter, and its reach is open

`DEC-20260822-ORCH-STATE-RECONSTRUCTION-CANDIDATE` (branch
`operator-decision-orch-state-reconstruction`) selects `OPTION B — HELD_AS_CANDIDATE` and states:

```
NEXT_ALLOWED_ACTION: none — no work is authorized by this record.
Not authorized: no design phase, no specification work, no prototype, no writer, no adoption
of any § 3 check or § 4 field, and no consultation of any § 3 check at a real dispatch.
```

Its `applies_to` names **exactly one object**: `PROPOSAL-ORCH-STATE-RECONSTRUCTION.md @
orch-state-reconstruction`. Whether the prohibition reaches dispatches other than that candidate
is recorded as an **open question by a sibling analysis** (`LEGEND-AGENT-COORDINATION-PROTOCOL-001`,
C-4) and is **not resolved here**.

**How this record handles it, so the handling is attackable rather than convenient:**

- the hold is treated as binding on its named object, in full;
- **no** § 3 reconstruction check is proposed, adopted, consulted, or relied on anywhere below;
- nothing here is a specification: every field named in `DISPATCH_MODEL` is **derived from text
  already frozen in an annex**, and the two places where the derivation would require a new
  requirement are named as governed changes that this record does not propose (Q-6, D-3);
- a reader who takes the hold broadly should treat `TARGET_MODEL` and `DISPATCH_MODEL` as
  **blocked pending the operator's determination of reach**, and should read the rest —
  `SURFACE_MAP`, `CURRENT_FAILURE_MODE`, `EVENT_MODEL`, `AUTONOMY_MEASUREMENT` — as measurement,
  which no hold bars.

**Produced:** this file. **Not produced:** a queue, a writer, a schema, an event, a task, an
assignment, a lease, a review, an approval, a merge.

---

## IDENTITY

**Identity is not inherited from a dispatch.** The dispatch addressed this session as
Orchestrator in design-analysis mode and instructed that no authority be taken from the role
contract. Both instructions are followed; the repository's own evidence is the source.

| Fact | Measured value | How |
|---|---|---|
| Repository | `<REPO_ROOT>` | `git rev-parse --show-toplevel` |
| Branch at session open | `main` | `git rev-parse --abbrev-ref HEAD` |
| HEAD at session open | `788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5` | `git rev-parse HEAD` |
| Working tree at open | **clean** — 0 porcelain entries | `git status --porcelain` |
| Lease | 🔴 **`ACTIVE by derivation: 0`** — 5 records, all `STALE` or `RELEASED`; most recent released `2026-08-18T14:05:20Z` | `python3 framework/scripts/lease_state.py` |
| Runtime inventory on this ref | **absent** — exists only at `runtime/runtime_inventory.md` on branch `orchestrator` | ref sweep, 49 refs |
| `ACTOR_ID` | **not established** — no registration record exists for this session | — |
| `SESSION_REF` | **not observable, and not invented** — no actor observes its own routing reference | `scientist_reading_modes.md` § 1.2 |
| Branch this record is written on | `orch-autonomous-dispatch-loop`, cut from `main` @ `788c357` | `git worktree add -b … main` |

### The consequence, stated plainly

`CLAUDE.md` § 0 is unconditional and both of its antecedents hold:

```
IF no valid runtime inventory / no ACTIVE ORCHESTRATOR_LEASE:
    ENTER BOOTSTRAP_MODE.
    Do NOT assume Orchestrator authority merely because you are in root.
```

**This session is in `BOOTSTRAP_MODE` and is not Orchestrator.** It holds no lease, has issued no
task, and has opened no review.

### Authority is derived from the body and the annexes only

`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` (on `main`) determines
**`ACTIVATION_NOT_CONFIRMED`**: the four role contracts remain `PROPOSED`. Its consequence 2 binds
how this record may be written:

> **No actor authority may be assumed from these contracts.** Any authority an actor exercises
> must be traced to the governance body or to a named annex — H.1 for the authority matrix, D for
> the commit path, C for the review ladder, I.3 for the lease — never to a role contract clause
> standing alone.

Every rule cited below is cited from `GOVERNANCE_v3.1.1.md` or from an annex.
`roles/orchestrator.md`, `roles/plan.md`, `roles/mirror.md` and `roles/scientist.md` are quoted
**descriptively only**, and each such quotation is marked.

---

## SURFACE_MAP

```
MEASURED_AT          ref     main
                     HEAD    788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5
                     date    2026-08-22, this session (UTC stamps below from the runtime)
                     tree    clean at session open

REFS SWEPT           49 total — 40 refs/heads · 5 refs/tags · 4 refs/remotes
                     (one of the 40 heads is this record's own branch, created this session)
WORKTREES            22, via `git worktree list` — one of them is this session's, created to
                     write this file; 21 existed at session open

VALIDITY             Every absence claim below is REPOSITORY-WIDE over those 49 refs and over
                     no wider surface. NOT_FOUND on 49 refs is NOT NOT_EXIST: other clones,
                     unpushed worktrees and unreferenced objects lie outside it. Claims scoped
                     to `main` alone are labelled LOCAL.
POSITIVE CONTROLS    Every negative sweep below was run with a positive control in the same
                     invocation. Two are recorded: `^roles/` returns 4 paths on 27 refs;
                     `framework/state` returns 94 of 831 Python files.
```

### Four sibling analyses exist, on four branches, none of them `main`

This dispatch is the fifth of a set issued the same day. The other four were located by ref
sweep, read by `git show <ref>:<path>`, and are cited by identifier below rather than restated.

| Branch | Record | Overlap with this dispatch |
|---|---|---|
| `orch-pipeline-loop-architecture` | `ORCHESTRATOR-SCIENTIFIC-PIPELINE-AND-LOOP-ARCHITECTURE-ANALYSIS-001` | pipeline + loop architecture, automation candidates, human gates |
| `orch-agent-coordination-protocol` | `LEGEND-AGENT-COORDINATION-PROTOCOL-001` | 8-stage task lifecycle, object addressing, role boundary, human gate map |
| `orch-scientific-pipeline-lifecycle-model` | `SCIENTIFIC_PIPELINE_LIFECYCLE-MODEL-001` | 9-state lifecycle vs J.1's 23 event types |
| `orch-control-plane-reconciliation` | `CONTROL-PLANE-RECONCILIATION-ANALYSIS-001` | control-plane reconciliation, human gate map |

> 🔴 **Sibling reports are treated as claims, not as findings.** Every number this record states
> was re-measured in this session. Where a sibling's measurement reproduced, that is said. Where
> one did not, the correction is below and the sibling record is **not edited**.

### Two corrections to sibling measurements, both re-measured here

**(a) `0 of 21 capabilities VERIFIED` is true of the registry and false of the laboratory.**

`LEGEND-AGENT-COORDINATION-PROTOCOL-001` (F-5.1, HG-8) and
`ORCHESTRATOR-SCIENTIFIC-PIPELINE-AND-LOOP-ARCHITECTURE-ANALYSIS-001` both argue from
*"0 of 21 rows are VERIFIED"*. Measured on branch `orchestrator`:

```
runtime/agent_card_registry.md   `status: UNVERIFIED`  × 21     `status: VERIFIED`  × 0
runtime/L2-OUTCOMES.md           "3 VERIFIED of 12 attempted", ratified by
                                 "operator decision of 2026-08-18 §1":
                                   O4  lease acquire · renew · observe expiry   VERIFIED
                                   S2  scientist worktree confinement           VERIFIED
                                   S4  scientist capability per plan            VERIFIED
```

Both files are on the **same branch**. Commit timestamps, this session:

```
632ad22  2026-08-18 16:05:46 +0200   runtime/agent_card_registry.md   (its only commit)
68d3528  2026-08-18 16:20:16 +0200   runtime/L2-OUTCOMES.md           (created)
600a0df  2026-08-18 16:30:18 +0200   runtime/L2-OUTCOMES.md           (tip)
git merge-base --is-ancestor 632ad22 600a0df  →  true
```

🔴 **The registry is the surface body § 8 says assignment is made from — and it was written
twenty-five minutes before the L2 round it does not record, and never updated.** Two of the three
ratified rows map verbatim onto a registry row that still reads `UNVERIFIED` (`O4` ↔ *"Lease
acquisition and renewal"*; `S2` ↔ *"Worktree confinement"*). The registry's own frontmatter reads
`updated_on: 2026-08-17`, and body § 43 already supplies the rule for this: *"riga stantia = non
autoritativa."*

**Why this matters here and not only as bookkeeping.** The sibling conclusion — that assignment is
blocked because nothing is VERIFIED — survives in substance: 18 of 21 rows are genuinely
unverified and L2 is under an operator hold. But the *mechanism* is different, and it is the one
that bears on a dispatch loop: **the resolver's declared input surface disagrees with the
ratified record beside it.** A resolver reading the registry would refuse a lease renewal that the
operator has already verified. That is not a capability gap; it is a reconciliation gap, and it is
`B-6` below.

**(b) One instrument error of my own, recorded rather than silently corrected.**

My first measurement of control-plane coupling returned *"13 Python files reference
`ledger/tasks`"*. The command was `grep -rl -- "$p" --include='*.py' .` — where `--` ends option
parsing, so `--include='*.py'` became a **file argument** and the search ran over every file type.
Re-measured correctly, with a positive control in the same invocation:

```
python files in scope (excl. _external_repos)                  831
  reference ledger/tasks · ledger/checkpoints · ledger/approvals
  · ledger/events · HUMAN_APPROVAL · TASK_ASSIGNMENT
  · AUTONOMY_LEDGER · learning/ · reviews/                       0   each
POSITIVE CONTROL — reference framework/state                    94   ✅ instrument working
```

This is the third instance in this analysis chain of a query returning a clean, wrong answer —
after a sibling's `^## H\.1` anchor against a `### H.1` heading, and a sibling's line-250 anchor
against a fence beginning at line 255. **The failure class is not rare enough to treat as
incidental**, and every negative in this record was therefore run with a control.

### Objects located, and the ref each lives on

| Object | On `main`? | Lives at |
|---|---|---|
| `ledger/events/` · `ledger/consolidated/` | ❌ | 🔴 **0 of 49 refs** |
| `active_lessons/` | ❌ | 🔴 **0 of 49 refs** |
| `LEARNING_INDEX` (any path) | ❌ | 🔴 **0 of 49 refs** |
| a durable roster (J.2) | ❌ | 🔴 **0 of 49 refs** |
| `OPERATOR_DAILY_BRIEF` (§ 10.4) | ❌ | 🔴 **0 of 49 refs** |
| `frozen/RECEIPT-<ACTOR_ID>.json` (benchmark freeze) | ❌ | 🔴 **0 of 49 refs** — BENCH-AB-001 not started |
| `runtime/agent_card_registry.md` | ❌ | branch `orchestrator` only |
| `runtime/runtime_inventory.md` | ❌ | branch `orchestrator` only |
| `runtime/L2-OUTCOMES.md` | ❌ | branch `orchestrator` only |
| `runtime/orchestrator_lease.md` | ✅ | `main` + 14 other refs |
| `ledger/tasks/` | ✅ | **`plan` only**, on every one of the 23 refs that carry it |
| `ledger/checkpoints/` | ✅ | `plan` on 23 refs; **`mirror` on branch `mirror` only** |
| `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` | ✅ | **forked — see below** |

### 🔴 The HUMAN_APPROVAL_QUEUE has forked, and no ref carries the union

J.3 makes this file the durable object every `HUMAN_REQUIRED` creates. Measured by parsing the
blob on every ref that carries it, comparing **contents, not line counts**:

| Depth | Refs | `APPROVAL_ID`s carried |
|---|---|---|
| 6 lines | 20 refs incl. `main`, `mirror`, `lettore-c` | `GOV311-001`, `GOV311-002` |
| 10 lines | 1 ref — `orchestrator` | + `SUNSET-DEC3-001`, `SCIAB-001`, `XPORT-001`, `P5DOMAIN-001` |
| 14 lines | 2 refs — `evidence-index`, `p51c9-rebased-onto-c89c2217` | + `HA-1`, `HA-2`, `HA-3`, `HA-4` |

```
orchestrator  ⊄  evidence-index          the four 2026-08-17 HA-* approvals are absent from it
evidence-index ⊄  orchestrator           the four 2026-08-18/19 approvals are absent from it
main carries 2 of the 10 distinct APPROVAL_IDs
```

This reproduces a sibling finding (`LEGEND-AGENT-COORDINATION-PROTOCOL-001` F-5.3, N-1)
independently and by a different route — that record measured by blob oid, this one by parsing
and comparing the `APPROVAL_ID` sets. **The counts agreeing is not the corroboration; the sets
agreeing is.**

🔴 **A second defect in the same file, not previously recorded.** J.3 declares the state
vocabulary `PENDING | APPROVED | APPROVED_WITH_MODIFICATION | DENIED | REVISION_REQUESTED`.
Measured on `evidence-index`:

```
RES-20260817-HA-2   STATE: DEFERRED     ← not in J.3's vocabulary
RES-20260817-HA-4   STATE: DEFERRED     ← not in J.3's vocabulary
RES-20260817-HA-3   STATE: RESOLVED     ← not in J.3's vocabulary
```

This is the same failure class the lease record already documents about itself — *"`EXPIRED` is
not in I.3's vocabulary … A terminal state was written by hand in a value the governance does not
define."* **Two independent hand-written control-plane records have drifted from their own frozen
vocabulary, in the same way, and nothing detects either.** Neither is repaired here: a record
edited to agree with its own schema has stopped being evidence.

---

## CURRENT_FAILURE_MODE

### What actually moves work today

```
operator
   │  reads a durable artifact on ref X, by hand
   │  composes a dispatch naming the role, the mode, the scope — and the ref
   ▼
session (some checkout)  ── establishes identity from the repository, not from the dispatch
   │  works inside one worktree
   │  WORK_COMMIT on its own branch                    (H.1 — "ogni attore, solo proprio branch")
   ▼
durable artifact on branch B
   │
   └── 🔴 no return edge. Nothing carries (ref, path) forward to the next actor.
```

On 2026-08-22 this produced five analysis records on five branches, plus the decisions and
reviews they depend on. Measured exactly: **of the 11 evidence artifacts this record cites, 2 are
on `main`** — `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` and
`SCIENTIFIC-PIPELINE-PREPARATION-001`. The other 9 — including the second decision, the Mirror
review of the role contracts, the Agent Card registry, `L2-OUTCOMES.md` and all four sibling
analyses — are each reachable from one branch only. Every session in the chain,
including this one, read its predecessors by `git show <ref>:<path>`, and every one was told the
ref **by the dispatch**. The operator is the transport layer. That diagnosis was reached by a
proposal author, `CONFIRMED` by Mirror at R4, reproduced by an operator decision, and reproduced
again by two sibling analyses; this record reproduces it a sixth time, mechanically, by having
had to do it.

### The three measurements that name the failure precisely

**1 · Nothing in this repository executes unless a human opens a session.**

```
.claude/settings.json           1 hook, total:  PreToolUse / matcher "Bash"
                                → scripts/guard_bash_command.py
                                It fires INSIDE an actor's turn. It cannot start one.
SessionStart / Stop hooks       none
scheduler (cron, launchd)       none in the repository
CI                              .github/workflows/public-release-gate.yml
                                on: push · pull_request · workflow_dispatch
                                — all three human-initiated; and a push is itself a human gate
```

**In the 24 hours the dispatch asks about, the number of processes that would run is zero.**
The lease record already says this about its own weakest layer: *"`PROCEDURAL` … Nothing compels
the Orchestrator to record an acquisition, and **nothing runs between turns**."*

**2 · The control plane has no readers.** 0 of 831 Python files read `ledger/tasks`,
`ledger/checkpoints`, `ledger/approvals`, `ledger/events`, `HUMAN_APPROVAL`, `TASK_ASSIGNMENT`
or `AUTONOMY_LEDGER`; 94 of 831 read `framework/state`. Every instrument this laboratory owns
points at the **scientific** layer. The coordination layer is text that only humans and agents
read.

**3 · The two layers are at incomparable maturities.** The scientific pipeline runs: 128
hash-chained receipts with `verify` OK and a tail anchor the LINT consumes; 66 deep-dive
manifests; a locator audit; a build/verify/freeze instrument for blind reading surfaces. The
coordination layer's entire installed base is 5 task records (one actor, self-assigned,
self-claimed), 27 checkpoints (two actors), one lease script, and a forked approval queue.

### The name for it

> **The loop is not blocked by authority. It is blocked by observability and addressing — and
> the two are one problem seen at two distances.** H.1 allocates every edge of
> `Orchestrator → Plan → Mirror → Scientist` without a gap that C.3, body § 28 and G.2 do not
> already separate. What is missing is that **no actor can see that another actor's stage ended,
> and no record says where to look.**

This record's own contribution to the diagnosis is narrower and is in `EVENT_MODEL`: of the ten
events the dispatch names, **the ones with a defined writer outnumber the ones with a defined
reader**, and a dispatch loop is a reader.

---

## TARGET_MODEL

> Described. Not proposed, not adopted, not scheduled, not assigned. Every element below is
> either already in frozen text or is named as a governed change that this record does not make.

### T-1 · The dispatch loop is a derivation, not a daemon

Three frozen constraints decide the shape before any design choice is available:

| Constraint | Source | Consequence for the loop |
|---|---|---|
| *"Niente job invisibili: autonomia ≠ invisibilità."* Actors are `persistent, visible, inspectable, interactive`; `INTERACTION_PROFILE: VISIBLE_VSCODE` | body § 34 | **the loop may not be a background process.** Unattended execution is not merely unbuilt here — it is not the thing this governance is trying to build |
| *"State changes by appending events, never by mutating."* `closed_by` may exist **only** in the derived view, never in the source ledger | J.1 | **the loop's state may not be a mutable status field.** It is rebuilt by replay |
| *"lo stato repo resta sovrano — in conflitto vince il repo; il ledger è audit e analisi, mai seconda fonte di verità"* | J.1 | **the loop is never authoritative.** It reports; the repository decides |

```
DISPATCH LOOP  =  a QUERY over per-actor append-only durable state,
                  run by an actor inside a visible turn,
                  producing a VIEW that is never a second source of truth.

NOT            =  a scheduler, a daemon, a shared mutable queue file, or a status field
                  that anyone edits.
```

**This is not a design preference. It is what remains after § 34, J.1 and P7 have each removed an
option.** P7 already chose the substrate for exactly these reasons: per-actor append-only JSONL
at `ledger/events/<ACTOR_ID>.jsonl`, consolidated by Plan into a derived view, *"append-only,
nessun file condiviso multi-writer"*.

### T-2 · The pattern already runs in this repository, on the other layer

The receipt ledger is the same shape, working, at 128 events:

| Property the loop needs | How the receipt ledger already does it |
|---|---|
| append-only, never mutated | one line per event; `record_kind` distinguishes contemporaneous from reconstruction |
| closure without rewriting the opening record | `invalidates_receipt` + `invalidation_reason` are carried by the **closing** record — J.1's `CLOSES_EVENT_ID` rule, already implemented |
| chain integrity | `ledger_prev_hash` per record; `fulltext_receipts.py verify` → `OK: 128 chained receipt(s)` |
| an anchor outside the file | tail anchored in `framework/state/state_manifest_current.md`; hand-editing breaks the chain and halts LEGEND |
| a consumer | the LINT consumes `verify`; `reading_state.py --check` re-derives a committed page and exits non-zero on drift |

P7 says the same thing in its own words — *"This should reuse the existing append-only machinery,
not invent a second one … Before building a guard, look for it — it is probably already here."*
**The dispatch loop's substrate is not novel engineering. It is one existing pattern applied to a
second class of object, and P7 has already recorded that decision and its reason.**

### T-3 · What the model is minimally made of

```
                 ┌──────────────────────────────────────────────────┐
                 │  per-actor append-only event files (P7 design a) │  ← does not exist
                 └───────────────────────┬──────────────────────────┘
                                         │  replay
                 ┌───────────────────────▼──────────────────────────┐
                 │  DERIVED VIEW — never authoritative, rebuilt      │
                 │  ┌────────────┬──────────────┬────────────────┐  │
                 │  │ TASK QUEUE │ DEPENDENCIES │ ROLE RESOLVER  │  │
                 │  └────────────┴──────────────┴────────────────┘  │
                 └───────────────────────┬──────────────────────────┘
                                         │  produces
                 ┌───────────────────────▼──────────────────────────┐
                 │  HANDOFF PACKAGE — an address, not a message     │
                 └───────────────────────┬──────────────────────────┘
                                         │  what it cannot resolve
                 ┌───────────────────────▼──────────────────────────┐
                 │  HUMAN_APPROVAL_QUEUE (J.3) + DAILY_BRIEF (§10.4)│  ← queue forked; brief absent
                 └──────────────────────────────────────────────────┘
```

Four components. **One of them exists** (the approval queue, forked). **One is designed and
unbuilt** (the event files). **Two are derivations that cannot be computed until the first one
exists.**

---

## EVENT_MODEL

The dispatch names ten events. Each is assessed on the five questions it asks — *does it exist?
is it missing? who writes it? who reads it? automatic or human?* — plus the J.1 minimum type that
would carry it. Authority is cited from H.1 and the annexes.

> **`writer` = who is authorised to bring the record into being. `reader` = who, other than the
> writer, can observe it happen without being told where to look.** The second column is the one
> a dispatch loop actually consumes, and it is the one the repository allocates least.

| # | Event | J.1 type | Exists? | Writer (authority) | Reader | Auto / human |
|---|---|---|---|---|---|---|
| **1** | **task creation** | `TASK_ASSIGNED` | ⚠️ **schema yes, instances degenerate.** A.1 fully specifies 15 fields. **5 records repository-wide, all `ledger/tasks/plan/`, all written by `plan` about `plan`.** `XPORT-ROUTING-001`'s own `_note`: *"No `TASK_ASSIGNMENT` message was received."* **0 events emitted** | **Orchestrator** — H.1 row 1 (*Task / priorità / riassegnazione / generation*); **not** conditioned on a lease | the assignee, via A.2 `TASK_ACK`; Plan at reconciliation | **HUMAN.** Hand-authored JSON; **no validator for A.1 exists** (0 of 831 py files) |
| **2** | **assignment** | `TASK_ACKED`, `TASK_CLAIMED` | 🔴 **no counterparty ACK exists for any task.** 3 of 5 records carry a `TASK_ACK` block — **all self-written**. 5 of 5 carry a `TASK_CLAIM` — all with `claimed_by == OWNER == plan` | ACK: the assignee (A.2). CLAIM: the claimant (A.3) | Orchestrator, for A.3 uniqueness; Plan, for `CLAIM_CONFLICT` at reconciliation | **HUMAN** |
| **3** | **reading start** | 🔴 **none of the 23** | 🔴 **no object of any kind.** The receipt ledger's 19 distinct keys were enumerated this session: `event_at`, `analysis_at`, `analysis_time_precision`, … — **no start field**. A receipt records a *completed* read | — | — | — |
| **4** | **reading freeze** | 🔴 **none of the 23** | ✅ **specified and mechanized, never exercised.** `benchmark_input_surface.py` has `freeze` and `verify-freeze` subcommands; protocol § 7 step 5. **0 `frozen/RECEIPT-*` on 49 refs** | 🔴 **Plan** — *"FREEZE each reading the moment its completion is declared — **before reading its content**"* (`controlled_benchmark_ab.md` step 5) | **any actor** — tree digest + per-file digests + commit sha, verifiable from the receipt alone | ✅ **AUTOMATIC once invoked** |
| **5** | **analysis complete** | 🔴 **none of the 23** | ⚠️ **partial.** `scientist_reading_modes.md` §§ 3.6/3.8 specify a five-step acceptance test; 66 deep-dive manifests exist; `deepdive_manifest.py --verify-artifacts` and `locator_audit.py` run | the owning actor declares | the validators (steps 1–4) | ⚠️ **MIXED.** Steps 1–4 mechanical. 🔴 **Step 5 — the blind locator audit — is agent-conducted and has no scripted form.** `locator_audit.py` answers *does the quote occur in its artifact*, not *does the quote support the proposition* |
| **6** | **handoff** | 🔴 **none of the 23** | 🔴 **named and unspecified.** B.2 lists `HANDOFF` in an enumeration and says nothing further: no envelope beyond B.1, no required field, no state effect, no closure. **15 paths, 6 namespaces, no two alike** | 🔴 **unallocated** — anyone, in practice | 🔴 **nobody.** No receiver-side record exists in any of the 15 | **HUMAN** — the operator is the transport |
| **7** | **review request** | `REVIEW_OPENED` | ⚠️ **rule is the strongest in the set; instances bypass it.** C.3 and body § 25: *"Apertura solo via Orchestrator"* — no other actor may open a review, Mirror included. **0 events.** In practice reviews are opened by `HANDOFF-*` artifacts written by the reviewed party | **Orchestrator, exclusively** (C.3; H.1 *Livello Ladder e reviewer*) | the reviewer | **HUMAN** |
| **8** | **review complete** | `REVIEW_CLOSED` | 🔴 **closure is allocated — to the author, not the reviewer.** C.2: *"AUTHOR_RESPONSE obbligatoria; il silenzio non è accettazione."* Measured over 49 refs: **54 `REV-*` artifacts, 8 `AUTHOR-RESPONSE-*`** | 🔴 **the AUTHOR of the reviewed object** — the only closure H.1 or an annex allocates to anyone | Orchestrator (adjudication); Mirror (review yield, G.3) | **HUMAN** |
| **9** | **adjudication** | `CHALLENGE_ADJUDICATED` — ⚠️ **challenges only.** C.1's `R3 TRIADIC` floor for persistent scientific disagreement has **no event type** | 🔴 **zero records of either kind.** 14 paths match `/adjud/i` over 49 refs and **every one is the scientific page-adjudication instrument** (`page_adjudications/…/adjudications.json` + `regenerate_adjudications.py`) — a different object that shares the word | **Orchestrator, with recorded rationale** (H.1); verdicts `ACCEPT \| MODIFY \| OVERRIDE_WITH_RATIONALE \| ESCALATE` (F.2). 🔴 Escalates to the operator when `AUTHOR == ADJUDICATOR` (C.3) | Mirror, **ex post and pattern-based only** (F.3: *"mai veto ex ante"*) | **HUMAN** |
| **10** | **learning creation** | `LEARNING_PROMOTED` — ⚠️ **promotion only.** E.1's `OBSERVED → LOCAL → PROVISIONAL → VALIDATING` transitions have no type, and **retrieval has none** | ⚠️ **records yes, loop no.** E.6's 12-field record is instantiated widely. `LEARNING_INDEX` **0 of 49**; `active_lessons/` **0 of 49** — while body § 15 makes consulting the index **mandatory** before filing | any actor writes the record. Index: **durability → Plan, epistemic curation → Mirror** — H.1's **only row whose authority column is `—`** | 🔴 **nobody.** 0 executables read `learning/` or `reviews/`; `CLAUDE.md`'s single pointer targets `active_lessons/`, which exists on 0 refs | **HUMAN** |

### E-1 · The shape of the result

```
events with a WRITER named in normative text        8 / 10   (missing: reading start, handoff)
events with a READER other than the writer          3 / 10   (reading freeze, analysis complete,
                                                              review complete — the last partly)
events covered by a J.1 minimum type                4 / 10   fully
                                                    2 / 10   partially (adjudication: challenges
                                                              only; learning: promotion only)
                                                    4 / 10   🔴 not at all — reading start,
                                                              reading freeze, analysis complete,
                                                              handoff
events EVER EMITTED as a J.1 event                  0 / 10
```

### E-2 · 🔴 The three findings that do not sit in any one cell

**1 · J.1's vocabulary is a control-plane vocabulary, and the loop needs a work vocabulary.**
The four events with no J.1 type at all are the four where the scientific work happens or is
handed over. Two of them (reading, analysis) are covered by a *different* ledger that J.1 does
not reference and P7's design does not subsume. **Building the event ledger exactly to
specification would leave events 3, 4, 5 and 6 unobservable.** Whether to extend J.1's minimum
list (a governance change), keep two ledgers with a declared join, or treat reading and analysis
as sovereign durable state queried rather than mirrored, is the sibling record's Q-1 and is
**not decided here**. J.1's own sovereignty clause supports the third.

**2 · Writers outnumber readers, and a dispatch loop is a reader.** Eight of ten events have a
writer the governance names. Three have an observer who is not the writer. **For five of the ten,
the only party who can tell that the event happened is the party who caused it** — and body § 18
supplies the consequence from the other side: *"Ciò che non è nello stato durevole non è
accaduto."* An event that only its author can see is, for coordination purposes, an event that
did not happen.

**3 · Event 4 is the counter-example, and it is worth more than its instance count.**
The reading freeze is the **only one of the ten** whose closer is (i) mechanized, (ii) owned by a
party other than the worker, and (iii) verifiable by a third party from the artifact alone. It
was designed that way on purpose — the freeze runs *before anyone reads the content*, so the
record cannot be adjusted to fit what the content turned out to be. **It has never run.** Its
protocol's frontmatter reads `status: PROPOSED — binding on canonical execution of
CAND-20260818-SCIENTIST-AB-SPEC`, and `git merge-base --is-ancestor 4454feab main` returns
**true** — the candidate is canonical. Whether that clause is therefore satisfied is a
`STATE_DETERMINATION` of the kind `DEC-20260822` performed for `roles/`, it sits with the
operator under H.1, and **this record measures it without ruling on it.**

---

## DISPATCH_MODEL

> Sections 2–5 of the dispatch: task queue, dependency checker, role resolver, handoff generator.
> **Described as models. Nothing is created.**

### D-1 · TASK QUEUE MODEL — four buckets that reduce to one predicate

**How the Orchestrator would know, and what it can know today.**

| Bucket | Predicate, derived from frozen text | What answers it today |
|---|---|---|
| **OPEN** | a `TASK_ASSIGNED` event with **no closing event carrying `CLOSES_EVENT_ID` pointing at it** (J.1) | 🔴 nothing. `STATE` is a free-text arrow string in 3 of 5 records (*"CLAIMED → IN_PROGRESS"*; one is a 300-character chain) and **absent in 2 of 5**. **No record's `STATE` value is a single A.5 token** |
| **BLOCKED** | A.5 `BLOCKED` or `AWAITING_APPROVAL`, the latter joined to an unresolved `APPROVAL_ID` in J.3's queue | 🔴 **0 records carry either state**, and the queue that would answer the join is **forked across refs**, so *"what is awaiting approval"* has no single-ref answer |
| **READY** | ACKed + claimed + **every `DEPENDENCIES` entry closed** + owner not `DOWN` (A.1, A.3, J.2) | 🔴 A.1 declares a `DEPENDENCIES` field; **H.1 has no row for who declares a dependency satisfied.** `DOWN` requires HEARTBEAT (B.3, P4 = 30 min / 3 misses), which has never run |
| **FAILED** | attempts ≥ `RETRY_POLICY.max_attempts`, with `on_exhaust ∈ {REASSIGN, PARK, ESCALATE}` applied and recorded (A.1, P1); A.5 `PARKED` | 🔴 **0 records carry `PARKED`**, and F.4 `DIAGNOSE` must run first — it is a judgement (*delivery failure? context failure? contract ambiguity? actual refusal?*), not a predicate |

#### 🔴 D-1.1 · The four buckets are one question, and the obvious retrofit is the one J.1 forbids

Every row above resolves to **"does a closing record exist for this task?"** — and J.1 states, in
terms, how that question may *not* be answered:

> **Append-only rigoroso:** un evento già scritto NON viene MAI aggiornato — nemmeno per
> collegarlo alla sua chiusura. … Un campo `closed_by` può esistere SOLTANTO nella **vista
> derivata/replayed**, mai nel ledger sorgente.

**So the queue cannot be retrofitted by adding or maintaining a `status:` field on the five task
records.** That is precisely the mutation J.1 bans, and it is the cheapest-looking fix. The five
existing records already show why the ban is right: `SCIENTIST-AB-SPEC-001`'s `STATE` field has
been rewritten repeatedly into a 300-character prose chain that records its own history because
it had nowhere else to put it — a mutable field doing an append-only job, badly, and readable by
no instrument.

The queue is therefore **a derivation or it is nothing**, and its input is the one artifact that
does not exist. This is not an argument that the ledger should be built; it is the measurement
that the four buckets have exactly one blocker between them.

#### D-1.2 · What the queue is *not* allowed to be

- **not a shared file** — body § 14 `ONE_WRITER_PER_WORKING_DIRECTORY`, and J.1's *"nessun file
  condiviso multi-writer"*. The approval queue is the measured demonstration of what happens
  otherwise: an append-only object appended concurrently on two branches, now forked;
- **not authoritative** — J.1: *"in conflitto vince il repo"*. A task the view calls `READY` and
  the repository shows claimed is claimed;
- **not a scheduler** — body § 34.

### D-2 · DEPENDENCY CHECKER — five precondition classes, four unverifiable

The dispatch's worked example is a Mirror review. Taken clause by clause, then generalised.

| Dispatch's precondition | The governance's actual requirement | Verifiable today? |
|---|---|---|
| artifact present | C.2 `OBJECT (claim id / CANDIDATE_CONTENT_HASH / directive id)`. An object here is addressed by `(ref, path, blob)`; a path alone does not address it, and a branch name addresses a **location, not a state** | ⚠️ **yes, by git — if the ref is known.** Which is the addressing problem, not a solution to it |
| author response present | ⚠️ **precise correction.** The `AUTHOR_RESPONSE` is the **closer of the previous review** (C.2), not a precondition of the next one. A revised object gets a new hash, and D.2 binds every approval to `CANDIDATE_CONTENT_HASH + BASE_HEAD`, so a new review is a new object. The outstanding response is a **governance** condition — `DEC-20260822-…-CANDIDATE` rationale § 2 declined to authorize work on exactly this ground: *"Authorizing a design phase on a review whose author response is unwritten would read silence as acceptance — which C.2 forbids in those words"* | ✅ yes — count `REV-*` against `AUTHOR-RESPONSE-*`. **Measured: 54 against 8** |
| reviewer available | body § 8: *"Orchestrator assegna sulle capabilities **verificate**, non sul ruolo presunto"*; I.4. Plus C.3's cap: **one active review per Scientist** | 🔴 **no.** The registry says 21/21 `UNVERIFIED`; `L2-OUTCOMES.md` on the same branch says 3 ratified `VERIFIED`. **The input disagrees with itself** |
| independence respected | C.3: `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR` for important reviews; rotation, never fixed pairs; reviewer without contributed evidence; semi-blind = *"independence by task framing, not by information barrier"* | 🔴 **no** — there is no durable record of who authored, reviewed or adjudicated what, to check a candidate assignment against |

**Generalised: five precondition classes, derived from frozen text only.**

```
P-A  OBJECT RESOLVES        (ref, path, blob) resolves and the blob is the pinned one
                            → C.2 OBJECT; D.2 hash+base binding
                            STATUS: unverifiable without a ref field — Q-2, open

P-B  AUTHORITY EXISTS       an H.1 row allocates the act; for CANONICAL_BATCH_COMMIT also
                            GATE 0's ACTIVE lease singleton
                            STATUS: measurable — and measures 0 ACTIVE leases

P-C  CAPABILITY VERIFIED    the act is on the actor's VERIFIED capability list (I.4, body §8)
                            STATUS: input surface stale by one ratified round — B-6

P-D  CONFLICT-FREE          C.3 exclusions; G.2's bar on Mirror reviewing its own method
                            STATUS: no durable record to check against

P-E  COST ENVELOPE          J.4 DEFAULT_EXTERNAL_SPEND = 0; any spend needs an approval object
                            STATUS: ✅ SATISFIED BY CONSTRUCTION
```

> 🔴 **P-E is the only precondition that works today, and the reason is worth stating: its
> default is "no".** It needs no instrument, no registry and no event, because a missing record
> produces a refusal rather than a false permission. Every other precondition fails **open** when
> its record is missing — an unverifiable independence check does not block a review, it simply
> does not happen. **The four that need instruments are the four whose default is "yes".**

### D-3 · ROLE RESOLVER — from *"a review is needed"* to *"which actor"*

Six steps. Steps 1–2 are already fully mechanical; the failure is entirely in 3–5.

| # | Step | Source | Status |
|---|---|---|---|
| **1** | **object class → reviewer class.** `EVIDENCE → Scientist + Plan/provenance` · `INFERENCE → peer Scientist` · `SYSTEM → Mirror` | C.4 / body § 23 | ✅ **mechanical, and it exists.** A three-way mapping with no discretion in it |
| **2** | **claim class → Ladder floor.** L1 ordinary → R0 · L2 important → R1 · therapeutic-actionable → R2 · persistent disagreement → R3 · methodology-changing → R4 · specified cross-model → R5. Derogable **only upward**; below the floor only with recorded rationale | C.1; H.1 gives the level (≥ floor) to Orchestrator | ✅ **mechanical, and it exists** |
| **3** | **candidate actors.** Only `VERIFIED` capabilities | I.4; body § 8 | 🔴 **input stale** — B-6 |
| **4** | **exclusions.** `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR`; rotation; no contributed evidence; cap 1 active review per Scientist; G.2's bar on Mirror's own method | C.3; G.2 | 🔴 **no record to compute against.** ⚠️ *Measured instance that the rule does work when a human applies it:* `REV-ROLES-MIRROR-001` emitted **no verdict** on `roles/mirror.md`, on the self-review prohibition |
| **5** | **routing.** Deliver to the chosen actor | B.1; I.4 | 🔴 **not exercisable.** `ACTOR_ID` is identity and is not a route; `SESSION_REF` is a route and is **not observable by its own holder**; the transport recorded by `CAND-20260819-XPORT` is a uds socket that dies with its process. C-7 — one session seen by four actors and claimed by none — open since 2026-08-16 |
| **6** | **fallback.** What happens when no eligible actor resolves | 🔴 **the governance defines none** | ⚠️ **but the measured fallback is consistent and correct: escalation to the operator.** F.2's `ESCALATE`; H.1's operator rows. When `REV-ROLES-MIRROR-001` found the only eligible reviewer was the author, it declined to resolve and referred to the operator — *"an actor choosing the reading that makes its own contract binding would be exactly the convenient interpretation the gate exists to prevent"* |

> 🔴 **The resolver is not the hard part.** Steps 1, 2 and 4's rule set are a small deterministic
> function over C.4, C.1 and C.3 — already written, already frozen, already unambiguous. **Its
> inputs are stale and its output is not deliverable.** Reallocating authority would not move
> this; a current registry and a routable address would move all of it.

### D-4 · HANDOFF GENERATOR — the minimum package, derived not invented

Every field below is taken from text **already frozen in an annex or already carried by an
existing artifact**. Nothing is newly required, because requiring anything of a B.2 `HANDOFF` is a
change to a FROZEN annex — the sibling record's Q-6, open.

| Dispatch field | Derived carrier | Source | Precedent measured |
|---|---|---|---|
| **origine** | `ACTOR_ID` — **identity**, never the routing `from` | B.1; I.4; body § 21 | present in every task record |
| **obiettivo** | `TASK_ID` + `DIRECTIVE_VERSION` + `GENERATION` | A.1; A.4; B.1 | present in all 5 task records |
| **artifact** | `(ref, path)` — the ref is the field without which a path is not an address | — | 🔴 **no schema requires it.** `HANDOFF-GOV311-ORCHESTRATOR` carries `source_branch` as a **structured frontmatter key**, on `main` |
| **hash** | blob oid **+** sha-256 of content; for a candidate, `CANDIDATE_CONTENT_HASH` **+** `BASE_HEAD` | D.2; GATE 5 | `HANDOFF-P5DOMAIN-MIRROR` distinguishes `BASE_HEAD` / `CONTENT_TIP` / `MANIFEST_TIP` as three separate oids |
| **stato** | an A.5 token **+** A.1's `CURRENT_STATE (durable pointer)` | A.5; A.1 | 🔴 no existing record carries a bare A.5 token |
| **vincoli** | `REVIEW_REQUIREMENT` (C.1 floor) · `INTERACTION_MODE` · `RETRY_POLICY` · `APPLICABLE_GOVERNANCE_FINGERPRINT` | A.1; A.6; C.1 | the fingerprint is computable today: `governance_fingerprint.py compose --all` emits four |
| **cosa non fare** | 🔴 **the strongest field in practice and the only one with no name anywhere in the governance** | — | measured under **four different names** in four artifacts: `NOT_DONE_DELIBERATELY` (`CHK-plan-0019`), `OUT_OF_SCOPE` (`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE`), `BOUNDARIES` (`DEC-20260822-…-CANDIDATE`), *"What this record does NOT do"* (three sibling analyses) |

#### 🔴 D-4.1 · The missing half is the receiver, not the sender

Fifteen handoff artifacts exist across six namespaces. **None carries a receiver-side record.**
Without one, *"handed off"* and *"received"* are the same durable state, and B.3's compensating
protocol — the one J.0 names for the absent exactly-once guarantee — cannot engage:

```
J.0   Exactly-once / delivery garantita  →  ACK + dedup MESSAGE_ID + reinvio + DIAGNOSE (B.3, F.4)
```

**The compensator is specified and has never been instantiated: 0 counterparty ACKs exist for any
task.** A handoff package with all seven fields above and no receipt is a better-addressed letter,
not a closed transfer.

#### D-4.2 · What is a governed change and what is not

- **Not** a governed change: an author *choosing* to carry ref, blob and sha-256 in a handoff it
  writes. `HANDOFF-GOV311-ORCHESTRATOR` already does, on `main`.
- **Is** a governed change: *requiring* it of every B.2 `HANDOFF` (Annex B is FROZEN) — Q-6; and
  giving `cosa non fare` a name in normative text — **D-3**, new below.

---

## HUMAN_ESCALATION

### H-1 · The dispatch's split, tested against the repository

The dispatch proposes: **automatic** = routing, verification, handoff, validations;
**human** = governance, scientific priority, architectural change, strategic conflict.

| Proposed automatic | Verdict | Evidence |
|---|---|---|
| **routing** | 🔴 **cannot be automated today.** H.1 allocates it to Orchestrator; no actor is routable (D-3 step 5) | I.4; C-7 |
| **verification** | ✅ **already automatic, and it is the one that is.** 7 runnable gates named in `CLAUDE.md` § 3 plus `deepdive_manifest.py`, `locator_audit.py`, `benchmark_input_surface.py verify/freeze`, `batch_queue.py --check`, `reading_state.py --check` | measured: all read `framework/state` / `disease-models` |
| **handoff** | 🔴 **cannot be automated today.** No schema, no receiver record (D-4.1) | B.2; 15 artifacts |
| **validations** | ⚠️ **split.** Automatic for the scientific layer. 🔴 **Zero validators exist for any A.1, A.6, B.1, C.2 or J.3 object** — 0 of 831 Python files, positive control 94 | measured |

| Proposed human | Verdict |
|---|---|
| **governance** | ✅ H.1 *Spese / MAJOR approval / governance → Operatore*; GATE 3; H.2 |
| **scientific priority** | ✅ H.1 *Strategia complessiva → Operatore*; body § 4 |
| **architectural change** | ✅ H.1 is `[MAJOR]` and FROZEN; body § 12's strict MAJOR definition |
| **strategic conflict** | ✅ body § 4 — *"Conflitto strategico non risolvibile dalle regole"* → human, while independent work continues |

**All four human classes are correctly identified and all four are already normative.** The
dispatch's split is right about what should stay human. It is wrong — or rather, optimistic —
about three of the four it calls automatic.

### H-2 · The 24-hour question, answered in three layers

**Layer 1 — mechanical. Nothing runs.**

Measured: one hook (`PreToolUse` / `Bash`), which fires only *inside* an actor's turn; no
`SessionStart` hook; no scheduler; one CI workflow triggered by `push`, `pull_request` or
`workflow_dispatch`, all human-initiated. **In 24 hours with no human, the number of processes
that execute is zero.** Every "autonomous" step in this laboratory still requires a human to open
a turn.

**Layer 2 — normative. The literal question asks for something § 34 forbids.**

> *"Niente job invisibili: **autonomia ≠ invisibilità**."* — body § 34, with
> `INTERACTION_PROFILE: VISIBLE_VSCODE` and *"persistent, visible, inspectable, interactive
> actors"* as a **core property**.

Unattended execution is not an unbuilt feature here; it is outside the design. **The answerable
form of the dispatch's question is therefore:** *with the actors' sessions open and the human not
answering, what proceeds and what halts?* Everything below answers that form. The distinction is
not pedantry — a model built to answer the literal question would be designing against § 34.

**Layer 3 — under the answerable form.**

```
CONTINUES  ── each actor finishes the task it holds under a valid contract, then parks   §9.4
           ── WORK_COMMIT on the actor's own branch                     H.1 "ogni attore"
           ── Plan continues preparation                                            §9.4
           ── Mirror continues reviews already open                                 §9.4
           ── every mechanical validator and gate, on demand                    measured
           ── LAB_STATE = ORPHAN; nobody promotes themselves                        §9.4

STOPS — because the governance decided it should (correct, and should not change)
           ── CANONICAL_BATCH_COMMIT     GATE 0: ACTIVE lease singleton — measured 0,
                                         and I.3 forbids self-promotion to obtain one
           ── any spend                  J.4 DEFAULT_EXTERNAL_SPEND = 0
           ── any MAJOR                  GATE 3: Mirror PASS *and* HUMAN_APPROVAL
           ── public push                a human reading the diff
           ── anything therapeutic       CLAUDE.md — never a substitute for a clinical team
           ── persistent scientific disagreement   C.1 floor R3, derogable only upward

STOPS — because an instrument is missing or an address cannot be resolved (NOT a decision)
           ── new task assignment        needs VERIFIED capabilities; the registry says 0/21
                                         while L2-OUTCOMES records 3 ratified          B-6
           ── review opening             Orchestrator-only (C.3), and there is no ACTIVE one
           ── every cross-actor handoff  no ref in the address; the operator is the transport
           ── any queue/dependency/readiness question   the event ledger is 0 of 49 refs
           ── knowing what is pending    the approval queue is forked; no ref carries the union
```

> 🔴 **The third bucket is the finding, and it is the whole answer to the dispatch's question.**
> The work that halts in 24 hours divides into two kinds. The first kind halts because someone
> decided it should, wrote the decision down, and the decision is right — that list is short,
> and shortening it further would be the wrong project. The second kind halts because a record
> is missing, an address does not resolve, or two files on one branch disagree.
>
> **Both look identical from outside: "waiting for the human."** Neither the operator nor any
> actor can currently tell them apart, because the instrument that would distinguish them — the
> `AUTONOMY LEDGER`'s `PREVENTABLE` vs `UNAVOIDABLE` classification — has never been
> instantiated. **The dispatch loop's first job is not to reduce the human's load. It is to make
> the two kinds of waiting distinguishable.**

---

## AUTONOMY_MEASUREMENT

### A-1 · The meter is specified and has never been built

Annex G.3 and body § 3 define it:

```
AUTONOMY LEDGER   HUMAN_REQUIRED  PREVENTABLE vs UNAVOIDABLE
                  ore bloccate · lavoro proseguito durante HITL · false escalation
                  supervisione volontaria ESCLUSA — non conta come HITL
GOAL              §3 — reduce PREVENTABLE. Weekly synthesis in the DAILY_BRIEF.
OWNER             Mirror (G.3), whose designated primary analysis surface is the
                  consolidated EVENT LEDGER (J.1) — "non leggendo le chat"
```

Measured over 49 refs:

```
AUTONOMY LEDGER instances                       0
OPERATOR_DAILY_BRIEF (its weekly carrier)       0        — §10.4 requires it once per working day
consolidated event ledger (its input surface)   0
MIRROR_RETROSPECTIVE artifacts                  0        — cadence N is UNASSIGNED by the annexes
                                                           to anyone, and G.2 bars Mirror from
                                                           setting it alone
```

**Every claim that any change raised or lowered human load — including every claim in this
record — is currently unfalsifiable.** This reproduces `SCIENTIFIC_PIPELINE_LIFECYCLE-MODEL-001`
T-5 independently and the reproduction is worth recording: two sessions reached it from different
directions.

### A-2 · 🔴 The dispatch asks for three classes; G.3 defines two

The dispatch asks that human effort be measured as **necessario / prevenibile / temporaneo**.
G.3's vocabulary is **`PREVENTABLE` / `UNAVOIDABLE`**. The third class has no home.

```
necessario   ≈  UNAVOIDABLE   structural: the six gates in H-2 bucket 2. Should never fall.
prevenibile  ≈  PREVENTABLE   a classification the Orchestrator should not have made, or an
                              escalation that the rules already answered. Should fall to zero.
temporaneo   ≈  🔴 NO CLASS   unavoidable TODAY because an instrument is absent; not structural;
                              falls when the instrument is built, not when anyone decides better.
```

**Under G.3 as written, `temporaneo` must be booked as `PREVENTABLE`** — which is technically
correct (it *is* preventable, by building the thing) and operationally destructive: it merges
*"the classifier made a bad call"* with *"the laboratory has not built the instrument yet."*
Those have different owners, different fixes and opposite implications for whether the
classification process is working.

**H-2's third bucket is exactly this class, and it is the larger one.**

🔴 **This record does not adopt a third class, and may not.** G.2 places
*autonomy-classification methodology* among the things **Mirror may not change alone**, and a
change to it flows `proposal → Plan candidate → independent reviewer chosen by Orchestrator →
validation; if governance → operator`. Introducing a third class is that kind of change.
Recorded as an observation and as **D-1** below. Nothing is renamed.

### A-3 · What a meter would need, given what exists

```
INPUT       J.1's HUMAN_REQUIRED_OPENED  +  APPROVAL_RESOLVED, joined by APPROVAL_ID
            to the J.3 queue object each HUMAN_REQUIRED is required to create
DERIVED     ore bloccate            = APPROVAL_RESOLVED.ts − HUMAN_REQUIRED_OPENED.ts
            lavoro proseguito       = events by other actors inside that interval
            false escalation        = a HUMAN_REQUIRED whose resolution cites a rule that
                                      already answered it
EXCLUDED    voluntary supervision — §3, explicitly not HITL
```

Two of the three inputs are the event types that have never been emitted. The third — the J.3
queue — exists and is **forked across refs with two out-of-vocabulary states in it**. So even the
one input that exists would need reconciling before it could be joined against anything.

**A meter built on today's substrate would measure the substrate, not the laboratory.**

---

## BLOCKERS

Measured conditions between the current system and the loop the dispatch describes. **Listed,
not solved. Not assigned.** Ownership is named only where the repository names it.

| # | Blocker | Evidence measured this session | Owner per repository |
|---|---|---|---|
| **B-1** | 🔴 **No event stream.** `ledger/events/` and `ledger/consolidated/` on **0 of 49 refs**; 0 of the 10 dispatch events ever emitted | SURFACE_MAP; EVENT_MODEL | design → Plan (**done**, P7). **Writer → nobody** |
| **B-2** | 🔴 **Four of the ten dispatch events have no J.1 type at all** — reading start, reading freeze, analysis complete, handoff. Building J.1 as specified does not close them | E-2.1 | unassigned — Q-1 |
| **B-3** | 🔴 **The queue's four buckets reduce to one predicate, and the cheap retrofit is the one J.1 bans.** A `status:` field on the task records is the mutation *"State changes by appending events, never by mutating"* forbids | D-1.1 | — |
| **B-4** | 🔴 **A path without a ref is not an address.** Every object used as evidence here was fetched by `git show <ref>:<path>`; **2 of the 11 cited evidence artifacts are on `main`** | CURRENT_FAILURE_MODE | Q-2 — Plan, subject to review |
| **B-5** | 🔴 **Handoff has no receiver record.** 15 artifacts, 6 namespaces, 0 receiver traces; 0 counterparty `TASK_ACK`s for any task, so J.0's compensator for absent delivery guarantees has never engaged | D-4.1 | B.3; Q-6 |
| **B-6** | 🔴 **NEW — the resolver's input surface disagrees with the ratified record beside it.** `agent_card_registry.md` (21/21 `UNVERIFIED`, single commit `632ad22` @ 16:05:46) vs `L2-OUTCOMES.md` (3 `VERIFIED`, ratified by operator decision, commits 16:20:16–16:30:18) — **same branch, same day, never reconciled.** Body § 43: *"riga stantia = non autoritativa"* | SURFACE_MAP (a) | body § 43 → Plan (*"Plan aggiorna a ogni rehydration/cambio"*) |
| **B-7** | 🔴 **NEW — J.3's queue carries states J.3 does not define.** `DEFERRED` ×2 and `RESOLVED` ×1 on `evidence-index`, against the declared `PENDING \| APPROVED \| APPROVED_WITH_MODIFICATION \| DENIED \| REVISION_REQUESTED`. Same failure class as the lease record's self-documented `EXPIRED`; **nothing detects either** | SURFACE_MAP | Plan (durability) / operator |
| **B-8** | 🔴 **The approval queue is forked and no ref carries the union.** 10 distinct `APPROVAL_ID`s; max 6 on any ref; `main` carries 2; `orchestrator ⊄ evidence-index ⊄ orchestrator` | SURFACE_MAP | Plan (durability) / operator |
| **B-9** | 🔴 **No control-plane validator of any kind.** 0 of 831 Python files read an A.1, A.6, B.1, C.2 or J.3 object; positive control 94 | SURFACE_MAP (b) | L2 record: *"not authorized to anyone"* |
| **B-10** | 🔴 **The meter for the dispatch's own success criterion does not exist.** AUTONOMY LEDGER 0/49; DAILY_BRIEF 0/49; Mirror's designated input surface 0/49; retrospective cadence `N` UNASSIGNED | AUTONOMY_MEASUREMENT | G.3 → Mirror; cadence unassigned to anyone |
| **B-11** | ⚠️ **Review closure at 8 of 54.** C.2: silence is not acceptance. The closer is the **author**, and it is the only closure any annex allocates | EVENT_MODEL #8 | the author of each reviewed object |
| **B-12** | ⚠️ **No heartbeat has ever run**, so `DOWN` — the input to J.2's actor state machine and to the queue's `READY` predicate — has never been derivable. P3/P4 are `PROVISIONAL` and expire on evidence *"from the event ledger"*, an event that cannot occur | B.3; P3/P4 | B.3; P3/P4 |
| **B-13** | 🔴 **The role contracts are non-binding.** `DEC-20260822`: `ACTIVATION_NOT_CONFIRMED`; a new explicit activation act is required and this record does not perform, schedule or specify it | `DEC-20260822` | operator (H.1) |
| **B-14** | 🔴 **The reach of `DEC-20260822-…-CANDIDATE`'s prohibition is undetermined**, and this record's `TARGET_MODEL` and `DISPATCH_MODEL` sit inside the uncertainty | TASK_STATUS | operator |

**B-1 through B-5 are one absence observed at five points.** Without events nothing closes;
without closure the queue has no predicate; without a ref durable state is not reachable; the
queue fork and the handoff gap are that same absence operating on replicated files. **This record
does not propose which of them, if any, is the right place to intervene.**

---

## OPEN_QUESTIONS

Carried questions keep the identifiers their originating record gave them, so they are not
renumbered into new objects. New questions use the `D-` prefix. **None is resolved here and none
is assigned to anyone.**

| # | Question | Owner per H.1 | State |
|---|---|---|---|
| **Q-1** | Reading, analysis and handoff have no J.1 event type. Extend J.1's minimum list (MAJOR under H.2), keep two ledgers with a declared join, or treat reading/analysis as sovereign durable state queried rather than mirrored? | operator (governance) / Plan (design) | **OPEN** — carried, corroborated at event granularity here |
| **Q-2** | What identifies a dispatched object — ref, tip oid, content hash, or all three? | Plan, subject to review | **OPEN** — carried |
| **Q-6** | Does Annex B's `HANDOFF` need a schema? Annex B is FROZEN | unclear | **OPEN** — carried; D-4 derives what the package would contain **without proposing the requirement** |
| **Q-8** | What resolves C-7 — a session seen by four actors and claimed by none? | operator | **OPEN** since 2026-08-16 |
| **C-4** | Does `DEC-20260822-…-CANDIDATE`'s prohibition on *"design phase, specification work"* reach dispatches other than the one candidate it `applies_to`? | operator | **OPEN** — carried; **this record's own admissibility turns on it** (TASK_STATUS) |
| **O-1** | `scientist_reading_modes.md`'s three activation clauses measure SATISFIED; its status line still reads `PROPOSED` | operator | **OPEN** — carried. `controlled_benchmark_ab.md` carries the same construction, and `4454feab` **is** an ancestor of `main` (measured) |
| **D-1** | 🔴 **NEW.** The dispatch's `temporaneo` class has no home in G.3's `PREVENTABLE / UNAVOIDABLE` vocabulary, and it is the class H-2's third bucket falls in. Adding it is a change to *autonomy-classification methodology*, which **G.2 bars Mirror from making alone** | proposal → Plan candidate → independent reviewer chosen by Orchestrator; if governance → operator (G.2) | **OPEN** |
| **D-2** | 🔴 **NEW.** Which record is authoritative when the Agent Card registry and `L2-OUTCOMES.md` disagree on the same branch? Body § 43's *"riga stantia = non autoritativa"* answers *which is stale*; it does not say **who reconciles**, nor whether an assignment made from the stale surface is void | body § 43 → Plan (maintenance); operator (if the answer is normative) | **OPEN** |
| **D-3** | 🔴 **NEW.** *"Cosa non fare"* is the most consistently written field in this laboratory's practice and has **no name in any normative text.** Measured under four different names in four artifacts. Naming it is a governed change; leaving it unnamed means every handoff invents it again | unallocated | **OPEN** |
| **D-4** | 🔴 **NEW.** J.3's queue carries `DEFERRED` and `RESOLVED`, which its own frozen vocabulary does not define — the same drift the lease record documents about `EXPIRED`. Is the repair a normalisation of the records, an extension of the vocabulary, or a validator that reports without repairing? All three are defensible and **normalising first would destroy the evidence** | Plan (schema) / operator | **OPEN** |
| **D-5** | 🔴 **NEW.** § 34 forbids invisible jobs; the dispatch's literal question presumes unattended execution. Is *"autonomy"* in this laboratory defined as **fewer human decisions per unit of work** (compatible with § 34) or as **work proceeding without a human present** (not compatible)? Every autonomy target depends on which, and body § 3's `95/5` does not say | operator (strategy) | **OPEN** |

---

## What this record does NOT do

- it does **not** create, propose or adopt a queue, an event writer, a schema, a field, a check,
  a gate or a validator;
- it does **not** emit an event, issue a task, open a review, request an approval, acquire a
  lease or perform any commit other than the one that makes this file durable on its own branch;
- it does **not** activate, amend or read as binding any role contract — `DEC-20260822`
  consequence 2 is in force throughout;
- it does **not** resolve Q-1, Q-2, Q-6, Q-8, C-4, O-1 or any of D-1…D-5;
- it does **not** propose, consult or rely on the § 3 reconstruction check held by
  `DEC-20260822-…-CANDIDATE`, and it does **not** determine that decision's reach;
- it does **not** repair the forked approval queue, the out-of-vocabulary states, or the stale
  registry — each is reported with its evidence and left exactly as written, because a record
  edited to agree with its own schema has stopped being evidence;
- it does **not** adopt a third autonomy class, rename G.3's two, or touch Mirror's methodology;
- it does **not** edit any sibling analysis, any decision record, or `main`;
- it does **not** merge any branch or modify any candidate, annex, ledger, framework, runtime or
  scientific file.

---

## VERIFICATION TRAIL

Every command was executed in this session. Sweeps labelled *49 refs* iterate
`refs/heads` + `refs/tags` + `refs/remotes` and were each run with a positive control in the same
invocation.

| Check | Command | Result |
|---|---|---|
| Identity — branch / HEAD / tree | `git rev-parse --abbrev-ref HEAD`; `git rev-parse HEAD`; `git status --porcelain` | `main`; `788c357d…`; empty |
| Lease | `python3 framework/scripts/lease_state.py` | `ACTIVE by derivation: 0`; 5 records, all STALE/RELEASED |
| Ref surface | `git for-each-ref --format=x refs/heads`, `refs/tags`, `refs/remotes` | 40 · 5 · 4 = **49** |
| Worktrees | `git worktree list` | 22 (21 at session open) |
| Cited evidence on `main` | `git cat-file -e main:<path>` over the 11 cited artifacts | **2 on `main`, 9 elsewhere** |
| Gates, run in this worktree | `python3 framework/scripts/legend_lint.py .`; `python3 scripts/public_release_gate.py` | LINT **PASS** (1 pre-existing INFO); publication gate **PASS / BLOCKS: 0** (4 pre-existing `[REVIEW]` lines, all under `disease-models/`, untouched here) |
| Event ledger | `git ls-tree -r <ref> \| grep '^ledger/events/'` over 49 refs | **0**; control `^roles/` → 4 paths on 27 refs |
| `ledger/consolidated/` · `active_lessons/` · `LEARNING_INDEX` · roster · `DAILY_BRIEF` · `frozen/RECEIPT-` | same sweep | **0 each**, same control |
| Task ledger population | `git ls-tree -r <ref> -- ledger/tasks` over 49 refs | **`plan` only**, on all 23 refs that carry it |
| Checkpoint population | same, `-- ledger/checkpoints` | `plan` on 23 refs; `mirror` on `mirror` only |
| Task record state fields | `python3` over `ledger/tasks/plan/*.json` | 3 of 5 carry free-text `STATE`; 2 carry none; 0 carry a bare A.5 token; 5 of 5 self-claimed (`claimed_by == OWNER == plan`) |
| Approval queue fork | `git show <ref>:ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` parsed on every carrier; **`APPROVAL_ID` sets compared, not line counts** | 6/10/14-line variants; 10 distinct IDs; `main` carries 2; `orchestrator ⊄ evidence-index ⊄ orchestrator` |
| Out-of-vocabulary approval states | same parse | `DEFERRED` ×2, `RESOLVED` ×1 on `evidence-index` |
| Capability rows | `git show orchestrator:runtime/agent_card_registry.md \| grep -c 'status: UNVERIFIED'` / `'status: VERIFIED'` | **21 / 0** |
| L2 ratified rows | `git show orchestrator:runtime/L2-OUTCOMES.md` | `O4`, `S2`, `S4` **VERIFIED**, *"operator decision of 2026-08-18 §1"* |
| Registry staleness | `git log --format='%h %ci' orchestrator -- <both paths>`; `git merge-base --is-ancestor 632ad22 600a0df` | registry `16:05:46`, L2 tip `16:30:18`, same day; ancestor **true** |
| Control-plane coupling | `grep -rl --include='*.py' -F <path> .` excl. `_external_repos` | **0 of 831** for 9 control-plane tokens; control `framework/state` → **94** |
| Receipt chain | `python3 framework/scripts/fulltext_receipts.py verify` | `OK: 128 chained receipt(s), tail anchored` |
| Receipt schema keys | `python3` over `fulltext_read_receipts.jsonl` | 19 distinct keys; **no start field** |
| Freeze instrument | `python3 framework/scripts/benchmark_input_surface.py --help` | subcommands `build, verify, freeze, verify-freeze, population, locators, tree-digest` |
| Review closure ratio | path sweep over 49 refs | `REV-*` **54** · `AUTHOR-RESPONSE-*` **8** |
| Handoff population | path sweep over 49 refs | **15** |
| Deep-dive manifests | path sweep over 49 refs | **66** |
| Adjudication records | `grep -Ei adjud` over all paths, 49 refs | **14 paths, all scientific page-adjudication**; 0 governance adjudications |
| Hooks / scheduler | `python3` over `.claude/settings.json`; `ls .github/workflows`; grep for `schedule\|cron` | 1 `PreToolUse`/`Bash` hook; no `SessionStart`; CI `on: push · pull_request · workflow_dispatch`; **no schedule** |
| Benchmark candidate canonical | `git merge-base --is-ancestor 4454feab main` | **true** |
| Fingerprint tool | `python3 governance/scripts/governance_fingerprint.py compose --all` | 4 fingerprints emitted (run by the decision record of 2026-08-22; not re-run here) |

---

**Recorded by:** a session in `BOOTSTRAP_MODE`, no lease, no `ACTOR_ID`, on branch
`orch-autonomous-dispatch-loop` cut from `main` @ `788c357`.
**This is not a `WORK_COMMIT` under a task contract and not a `CANONICAL_BATCH_COMMIT`.** It is a
design analysis that claims no authority, and `main` is unchanged.

🔴 **This record is itself a ninth fragmented object.** A reader standing on `main` will not find
it. That is the diagnosis in `CURRENT_FAILURE_MODE` applied to the record that makes it, and it is
stated here rather than left for the next reader to discover — who will, as every session in this
chain has, be told the ref by the operator.

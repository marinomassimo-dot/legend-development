---
artifact: COORDINATION PLAN — first Scientist A/B/Mirror run, sequence defined not executed
record_id: FIRST_SCIENTIFIC_RUN_COORDINATION-PLAN-001
task_id: FIRST_SCIENTIFIC_RUN_COORDINATION_v1
dispatcher: operator
author_session: root checkout, branch `main`, no ACTIVE lease
actor_id: NOT ESTABLISHED — same condition as SCIENTIFIC-PIPELINE-PREPARATION-001 § 1
date: 2026-08-22
mode: READ-ONLY ANALYSIS
governance_version: 3.1.1 (read, not exercised)
classification:
  - COORDINATION SEQUENCE ONLY
  - NOT GOVERNANCE
  - NOT AN ACTIVATION
  - NOT AN EXECUTION AUTHORIZATION
measured_at: main @ 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5, 2026-08-22
predecessor: learning/orchestrator/SCIENTIFIC-PIPELINE-PREPARATION-001.md
domain: >
  CONTENT. `learning/` is not among the exhaustive CONTROL_PLANE_ROOTS of P5.1
  (`governance/candidates/`, `ledger/`, `reviews/`). This record therefore sits inside the
  CANDIDATE_CONTENT_HASH of any future candidate that re-aligns onto `main`.
not_an_slr: >
  Not a Session Learning Record. Annex E.6 governs `SLR-*`; the name is deliberately not `SLR-`
  so the two are not conflated. Same convention as the predecessor.
authority_claimed: none
---

# FIRST SCIENTIFIC RUN — COORDINATION PLAN 001

> **READ-ONLY ANALYSIS · NOT GOVERNANCE · NOT AN ACTIVATION · NOT AN EXECUTION AUTHORIZATION**
>
> This record defines a sequence. It dispatches nobody, activates nothing, assigns no paper,
> creates no Task Contract, and lifts no hold. Every blocker named below is disposed of by
> someone else.

---

## 0 · What this record is, and the one thing it adds

The predecessor established the *model* — what a Scientist reading is, what it must produce, who
may not see what. This record establishes the **sequence**: what is checked before anything
starts, in what order the actors move, what state each object is in at each moment, where a human
must decide, and what cannot be automated today.

Its single substantive finding is stated up front, because everything else depends on it:

> 🔴 **The requested dispatch order — Orchestrator → Scientist A → Scientist B → Mirror — omits
> the actor that does most of the work and holds the experiment's integrity guarantee.**
> `controlled_benchmark_ab.md` § 5 assigns **Plan** to five of eleven steps, including the
> **FREEZE**. Without Plan there is no freeze; without a freeze the A/B comparison is not blind;
> an unblinded A/B comparison is not the experiment. See § 2.2.

---

## 1 · PRE-FLIGHT CHECK

Five classes, as dispatched. Every row carries the route that measures it, and the value that
route returned today. **A value in this table is a photograph and it decays** (body § 43); each
row names how to re-derive it rather than asking a later reader to trust the cell.

**MEASURED_AT: `main` @ `788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5`, 2026-08-22**

### 1.1 · Summary — two of five are green

| # | Class | Route | Measured today | Verdict |
|---|---|---|---|---|
| **PF-1** | agent availability | Agent Card registry, branch `orchestrator` | 3 of 6 registered — **`scientist-a` and `scientist-b` are `NOT_REGISTERED`, `ACTOR_ID: UNRESOLVED`** | 🔴 **BLOCKED** |
| **PF-2** | worktree validity | `git worktree list` | 25 worktrees; all five role worktrees present; **four tips moved since the predecessor measured** | 🟡 **PRESENT, RE-DERIVE** |
| **PF-3** | capability status | `roles/scientist.md` × Annex I.4 | **all six `UNVERIFIED`**; L2 **SUSPENDED** by the C-9 hold | 🔴 **BLOCKED** |
| **PF-4** | paper availability | `benchmark_manifest.json` `SOURCE_FILES[]` + `shasum -a 256` | **7 of 7 present, all digests match** | ✅ **GREEN** |
| **PF-5** | required tools | presence + `--help` | **7 of 7 present**, `benchmark_input_surface.py` exposes all seven subcommands | ✅ **GREEN** |

The two green rows are the two that are usually assumed and rarely checked. The three that block
are all **authority and registration**, not capability of the machine.

### 1.2 · PF-1 · Agent availability

`git show orchestrator:runtime/agent_card_registry.md` — `status: PARTIALLY REGISTERED — 3 of 6`.

| Actor | Registration | Note |
|---|---|---|
| `plan` | ✅ registered 2026-08-17 | verified against durable state; fingerprint recomputed in-worktree |
| `mirror` | ✅ registered 2026-08-17 | same |
| `scientist-c` | ✅ registered 2026-08-17 | **not required by an A/B/Mirror run** — see § 4.4 |
| `scientist-a` | 🔴 `STATUS: NOT_REGISTERED`, `ACTOR_ID: UNRESOLVED # proposed: scientist-a` | required |
| `scientist-b` | 🔴 `STATUS: NOT_REGISTERED`, `ACTOR_ID: UNRESOLVED # proposed: scientist-b` | required |
| `orchestrator` | — no ACTIVE lease (§ 1.6) | required |

> **The shape of this is worth naming.** The three actors that *are* registered include both
> non-Scientist actors this run needs — Plan and Mirror. The two that are not are exactly the two
> readers. The registry also records that the Scientist `ACTOR_ID`s are `UNRESOLVED`
> **by governed decision**, so resolving them is not a clerical act.

Registration is **I.2 step 7**; the L2 capability smoke is **I.2 step 8**. They are separable,
and that separation is the whole unblocking order of § 4.5.

### 1.3 · PF-2 · Worktree validity

`git worktree list` → **25** worktrees (the predecessor measured 16; the delta is
session-scratchpad worktrees under `/private/tmp/claude-501/…`, which are ephemeral and are not
role seats).

| Seat | Branch | Tip today | Predecessor's value @ `2bb2700` |
|---|---|---|---|
| root | `main` | `788c357` | `2bb2700` — moved |
| `.claude/worktrees/lettore` | `lettore` | `9b0cf47` | `9b0cf47` — unchanged |
| `.claude/worktrees/lettore-b` | `lettore-b` | `cb50e17` | `cb50e17` — unchanged |
| `.claude/worktrees/lettore-c` | `lettore-c` | `908197b` | `908197b` — unchanged |
| `.claude/worktrees/mirror` | `mirror` | `da52ee5` | `1892071` — **moved** |
| `.claude/worktrees/orchestrator` | `orchestrator` | `1e2fabd` | `1e2fabd` — unchanged |
| `.claude/worktrees/evidence-index` | `plan-orchsurf-r4-transcription` | `b72af2f` | `2e22c48` — **moved** |

**Validity is not existence.** A seat is valid for this run when it exists, is on its branch of
record, and is clean at handover. The manifest fixes the branch of record for the two readers:
`lettore` for `scientist-a`, `lettore-b` for `scientist-b`. Both hold. The reading itself does
**not** happen in these worktrees — it happens in the benchmark surface (§ 2.3 below), and this
is the declared deviation of `controlled_benchmark_ab.md` § 2.2.

> ⚠️ **Two tips moved and nothing detected it.** `mirror` and `evidence-index` advanced between
> the predecessor's measurement and this one. Neither move is wrong; the point is that no
> instrument reported it, and a pre-flight that reads the predecessor's table instead of
> re-deriving would have been wrong on two rows.

### 1.4 · PF-3 · Capability status

`framework/protocols/scientist_reading_modes.md` line 119 — *"the six of `roles/scientist.md`,
each `status: UNVERIFIED`"*. Line 146 makes the consequence explicit: *"A registered
`scientist-a` with six `UNVERIFIED` capabilities can be [registered and still not assignable]."*

`controlled_benchmark_ab.md` P-3 requires `VERIFIED` at L2 for at minimum: full-text read
producing a receipt · work manifest with verbatim locators · worktree confinement · Auto Mode
actually active. Measured: **all UNVERIFIED**.

The suspension is not incidental. `governance/candidates/PROPOSAL-C9-STATE-MODEL.md` frontmatter:

```
status: ACCEPTED
acceptance_is_not_adoption: true
hold: no implementation and no governance modification until that review completes;
      L2 suspended; the status/C-8 batch frozen pending a later operator decision
```

**L2 is I.2 step 8.** Steps 9 (lease acquisition) and 10 (`ACTIVE_ORCHESTRATOR`) are downstream
of it in the bootstrap sequence. This is the critical path of § 4.5 and § 5.3.

### 1.5 · PF-4 · Paper availability — the one row that is fully green

`BENCH-AB-001` fixes the paper: **PMID 42397075**, DOI `10.1093/brain/awag239`, Aqeilan et al.,
*Brain* 2026 — patient-derived neural organoids.

The packet lives under `files/fulltext/`, which is **git-ignored** — present in a checkout, never
in a commit. So its availability is a genuine per-instance pre-flight check and not a property of
the ref. Re-derive with `shasum -a 256` against `benchmark_manifest.json` `SOURCE_FILES[]`:

| Surface path | Manifest digest (16) | Measured (16) | |
|---|---|---|---|
| `PMID42397075_Aqeilan2026.pdf` | `b6b44816bb5a029a` | `b6b44816bb5a029a` | ✅ |
| `PMID42397075_Aqeilan2026_fitz.txt` | `9c48aa0934648f58` | `9c48aa0934648f58` | ✅ |
| `…File008.pdf` (author contributions) | `8a91fd6c5bf78d86` | `8a91fd6c5bf78d86` | ✅ |
| `…File009.pdf` (methods, 14 pp.) | `19d1b1d730531515` | `19d1b1d730531515` | ✅ |
| `…File010.pdf` (suppl. figs 1–10) | `aa86f300c7f5333d` | `aa86f300c7f5333d` | ✅ |
| `…File011.pdf` (resource table) | `7c8d7fdd1c65dbc9` | `7c8d7fdd1c65dbc9` | ✅ |
| `…File012.pdf` (uncropped blots) | `18864bfbdd8329a8` | `18864bfbdd8329a8` | ✅ |

**7 of 7 present, 7 of 7 digests match.** The evaluation population is already enumerated ex ante
and is itself a fixed denominator: **65 units / 109 panels** (revision 2), derived by
`benchmark_input_surface.py population`, deterministic across two consecutive runs.

> One caveat carried rather than smoothed: `_fitz.txt` is marked `NOT_REPRODUCIBLE —
> identity by digest`. Its declared extraction recipe does not regenerate its bytes. The artifact
> is intact and its recipe is not runnable, so the digest **is** its identity. A pre-flight can
> confirm the bytes; it cannot re-derive them.

### 1.6 · PF-5 · Required tools, and the lease

All present at `main` @ `788c357`:

| Tool | Role in this run |
|---|---|
| `framework/scripts/benchmark_input_surface.py` | `build · verify · freeze · verify-freeze · population · locators · tree-digest` — the experiment's spine |
| `framework/scripts/deepdive_manifest.py` | work manifest, `--verify-artifacts --require-current-schema` (schema 2) |
| `framework/scripts/lease_state.py` | lease derivation — *derive at the moment, never assume* (P-4) |
| `framework/scripts/fulltext_receipts.py` | receipt chain + manifest tail anchor |
| `framework/scripts/legend_lint.py` | structural LINT |
| `framework/scripts/corpus_firewall.py` | corpus containment |
| `scripts/public_release_gate.py` | publication gate (only if anything is pushed) |

**Lease, derived now** — `python3 framework/scripts/lease_state.py`:

```
lease #1  derived=STALE     stored=STALE      lease #2  derived=RELEASED  stored=RELEASED
lease #3  derived=STALE     stored=EXPIRED    lease #4  derived=RELEASED  stored=RELEASED
lease #5  derived=RELEASED  stored=RELEASED
ACTIVE by derivation: 0
```

**Zero ACTIVE leases.** Note lease #3: `derived=STALE` vs `stored=EXPIRED` — derivation and
stored value disagree, which is why P-4 says derive and never read.

### 1.7 · The pre-flight gate, stated as one line

```
BLIND FIRST PASS is authorized only when every row of controlled_benchmark_ab.md §1
reads satisfied AT THE MOMENT OF HANDOVER, by the route each row names.

Today: P-1 satisfied (both protocols canonical) · P-2 FAILS · P-3 FAILS ·
       P-4 FAILS · P-5 pending registration · P-6 FAILS (no contract exists) ·
       P-7 FAILS (surfaces not built; manifest _state: "PREPARED — NOT FROZEN",
                  FROZEN_SHA256: null, both HANDOVER blocks null)
```

---

## 2 · DISPATCH ORDER

### 2.1 · The order as dispatched

```
Orchestrator → Scientist A → Scientist B → Mirror
```

### 2.2 · 🔴 Three defects, measured against `controlled_benchmark_ab.md` § 5

**Defect 1 — Plan is missing, and Plan holds the integrity guarantee.**
§ 5 assigns Plan steps **1, 3, 5, 6, 9** of 11. Step 5 is the FREEZE, and § 7 fixes its timing:
*"Plan freezes **on the completion declaration and before reading the content**. The order
matters: a freeze taken after Plan has read the content is a freeze whose timing cannot be
shown."* A sequence without Plan has no step that makes a first pass immutable, and the
comparison at step 6 then runs over trees that could still move.

**Defect 2 — `A → B` is not a sequence.**
A and B are dispatched **together** at step 2, under one shared `PARALLEL_READ_GROUP:
BENCH-AB-001`, and they read **concurrently and mutually blind**. An arrow from A to B implies a
dependency that the protocol forbids: § 7 requires that *"neither actor sees the other's first
pass until **both** are frozen."* The correct notation is a fork, not a chain.

**Defect 3 — the blind locator audit is omitted.**
§ 5 step 7 spawns **fresh blind agents** over every `(proposition, snippet, anchor)` triple of
both readings, reader identity withheld. The predecessor already flagged why this matters:
*"Step 5 is the one that catches a careful reading that says more than its source — and it is the
step that is skipped first under time pressure."* A four-position chain drops it silently.

### 2.3 · The order the protocol actually defines

`controlled_benchmark_ab.md` § 5, reproduced structurally — **not restated in new vocabulary**:

```
 0  operator / Orchestrator   preconditions P-1…P-5 satisfied by their own routes
 1  Plan                      build both surfaces · verify · enumerate population · FREEZE manifest
 2  Orchestrator (lease)      issue TWO Task Contracts, one PARALLEL_READ_GROUP
                                 BENCH-AB-001-A  OWNER scientist-a  MODE A
                                 BENCH-AB-001-B  OWNER scientist-b  MODE B
 3  Plan → each actor         HANDOVER: writer transfer + memory-scope check recorded
                                    ┌──────────────────────────────┐
 4  scientist-a  ─────────────┤  blind first pass, concurrent  ├───────────── scientist-b
                                    └──────────────────────────────┘
                              no contact · no sight of the other · no prior LEGEND output
 5  Plan                      FREEZE each reading ON its completion declaration,
                              BEFORE reading content → receipt → byte-identical IMPORT
 6  Plan                      mechanical checks · comparison matrix · unresolved-disagreement list
                              (listed, NEVER resolved by Plan — body §28)
 7  fresh blind agents        locator audit of every triple, both readings, identity withheld
 8  Mirror                    R4 adjudication OF THE PROCESS (not of the paper)
 9  Plan                      outcome summary — dimensions separately, no composite
10  Orchestrator              scientific disagreement → Annex C R2/R3, OUTSIDE the benchmark
```

### 2.4 · Reconciling the two

The dispatched order is not wrong about **authority** — it is incomplete about **actors**.
Orchestrator does open and close the run; Mirror does adjudicate last. Corrected minimally, and
keeping the dispatched vocabulary:

```
Orchestrator ──▶ Plan ──▶ ┬─▶ Scientist A ─┬─▶ Plan(FREEZE) ─▶ blind audit ─▶ Mirror ─▶ Orchestrator
                          └─▶ Scientist B ─┘
```

Three constraints ride on that diagram and none is decorative:

| Constraint | Source | If violated |
|---|---|---|
| A and B never see each other pre-freeze | § 7 | benchmark **void for the second reader**; the outcome says so |
| Plan freezes before reading content | § 7 | freeze timing cannot be shown |
| Mirror's object is the **process**, not the paper | Annex G; § 5 step 8 | Mirror becomes a third reader; R4 is not a reading |

### 2.5 · One honest note on the A↔B barrier

`controlled_benchmark_ab.md` § 7 labels its own guarantee, in the Annex J.0 style:

```
GUARANTEE_PROVIDED:            none by mechanism — discipline only
FAILURE_MODE_STILL_POSSIBLE:   Plan reads or relays A's first pass to B before B freezes
DETECTION:                     receipts carry FREEZE_TIMESTAMP_UTC and SURFACE_COMMIT;
                               inspection makes a violation VISIBLE AFTER THE FACT, never prevented
RECOVERY:                      the benchmark is void for the second reader; the outcome says so
```

The blinding of the *surface* is mechanized (allowlist, parity, content scan, forbidden-path
check). The blinding **between the two actors** is not. That asymmetry is the honest state and it
is not softened here.

---

## 3 · STATE TRANSITIONS

### 3.1 · The finding: six requested names span three machines, and two do not exist

The dispatch asks for `READY · RUNNING · FROZEN · WAITING_REVIEW · COMPLETE · FAILED` and says to
use existing vocabulary where possible. Measured across `governance/`, `framework/`, `roles/`,
`ledger/`:

| Requested | Occurrences | Exists as | Verdict |
|---|---|---|---|
| `READY` | 30 | **system state** (`state_manifest_current.md` `current_state: READY`); also candidate review states | ⚠️ **exists, different machine** |
| `RUNNING` | 2 | **actor lifecycle** (J.2, verbatim) | ⚠️ **exists, actor machine only** |
| `FROZEN` | 39 | **document status** in frontmatter; and an **act by Plan on an artifact** | ⚠️ **not a lifecycle state at all** |
| `WAITING_REVIEW` | **0** | — | 🔴 **does not exist on any surveyed path** |
| `COMPLETE` | 91 | **task lifecycle terminal** (A.5, verbatim) | ✅ **exact match** |
| `FAILED` | 7 | mostly **script exit text**; Annex B nominal map `failure→failed` | 🔴 **not an A.5 terminal** |

`PROPOSAL-C9-STATE-MODEL.md` § 7.1 already diagnosed exactly this error class, and its ruling is
the reason the table above does not simply rename things:

> *"one field name covering three different state machines. **They must not be merged.** … A
> field whose name does not say which machine it belongs to will be written by whoever reads it
> as theirs."*

### 3.2 · The machines that exist, verbatim

```
TASK        (A.5)   ASSIGNED → ACKED → CLAIMED → IN_PROGRESS → (BLOCKED | AWAITING_APPROVAL)
                    → IN_PROGRESS → COMPLETE | CANCELLED | REASSIGNED(gen+1) | PARKED

ACTOR       (J.2)   BOOTSTRAPPING → ACTIVE ⇄ (IDLE | RUNNING)
                    RUNNING → BLOCKED | AWAITING_APPROVAL → ACTIVE
                    ACTIVE → DEGRADED (rotation) | DOWN (timeout) | PAUSED (operator) | RETIRED

LAB         (J.2)   BOOTSTRAP | OPERATIONAL | ORPHAN (orchestrator DOWN) | SUSPENDED

APPROVAL    (J.3)   PENDING | APPROVED | APPROVED_WITH_MODIFICATION | DENIED | REVISION_REQUESTED

CAPABILITY  (I.4)   VERIFIED | UNVERIFIED                          (per capability)

FIRST PASS  (bench §7 receipt)
                    COMPLETE_DECLARED_BY_ACTOR | ABANDONED | TIMED_OUT

REVIEW      (C.2 verdict)  CONFIRMED | WEAKENED | REFINED | REFUTED
            (J.1 events)   REVIEW_OPENED → REVIEW_CLOSED
```

### 3.3 · The mapping — requested name → existing vocabulary

| Requested | Say instead | Machine | Why |
|---|---|---|---|
| **READY** | `current_state: READY` for the system; `OPERATIONAL` for the lab; **P-1…P-7 satisfied** for this run | system / LAB | `READY` is a property of the *system*, never of a task or an actor. A task is never `READY` — it is `ASSIGNED`, then `ACKED`, then `CLAIMED`. |
| **RUNNING** | `RUNNING` for the **actor**; `IN_PROGRESS` for the **task** | ACTOR / TASK | Both exist; they are different machines and C-9 § 7.1 forbids merging them. During step 4: actor `RUNNING`, task `IN_PROGRESS`. |
| **FROZEN** | `FIRST_PASS_STATE: COMPLETE_DECLARED_BY_ACTOR` recorded in `frozen/RECEIPT-<ACTOR_ID>.json` | **artifact**, no lifecycle | The reading is frozen; the *actor* and *task* are not. `FROZEN` in frontmatter (`status: FROZEN` on the annexes) is a **document** status and is an unrelated use of the word. Freezing is an **act by Plan**, evidenced by a receipt — the state belongs to the tree. |
| **WAITING_REVIEW** | task `COMPLETE` + J.1 event `REVIEW_OPENED` (not yet `REVIEW_CLOSED`) | TASK + event | No such state exists. Critically it is **not** `AWAITING_APPROVAL`, which is J.3 human approval — a different machine with a different owner. Conflating them is how a peer review becomes a request for the Operator. |
| **COMPLETE** | `COMPLETE` | TASK | ✅ Use verbatim. Terminal state of A.5. |
| **FAILED** | `CANCELLED` \| `PARKED` \| `REASSIGNED(gen+1)`, per `RETRY_POLICY on_exhaust: REASSIGN \| PARK \| ESCALATE`; for a first pass, `ABANDONED` \| `TIMED_OUT` | TASK / artifact | A.5 has **no `FAILED`**. The distinction is load-bearing: a runtime fault is `DIAGNOSE` (Annex F.4) and *"mai classificare come rifiuto un guasto di runtime"* — a single `FAILED` bucket erases exactly that. |

### 3.4 · The run, expressed only in existing vocabulary

| Step | Task (A.5) | Actor (J.2) | Artifact |
|---|---|---|---|
| pre-flight | — | `plan`,`mirror` `ACTIVE`; a/b `BOOTSTRAPPING` | manifest `PREPARED — NOT FROZEN` |
| 1 | — | `plan` `RUNNING` | manifest **FROZEN** (`FROZEN_SHA256` set) |
| 2 | `ASSIGNED` → `ACKED` → `CLAIMED` | a/b `ACTIVE` → `IDLE` | two contracts under `ledger/tasks/<ACTOR_ID>/` |
| 3 | `CLAIMED` | a/b `ACTIVE` | manifest `HANDOVER` block written |
| 4 | `IN_PROGRESS` | a/b `RUNNING` | surface output tree + WORK_COMMITs |
| 4′ | `BLOCKED` / `AWAITING_APPROVAL` if raised | `BLOCKED` | checkpoint (A.6) |
| 5 | `COMPLETE` | a/b `IDLE` | `FIRST_PASS_STATE: COMPLETE_DECLARED_BY_ACTOR`; import |
| 6 | — | `plan` `RUNNING` | comparison matrix; unresolved-disagreement list |
| 7 | — | fresh agents | `audit/locator_audit-<ACTOR_ID>.md` |
| 8 | — | `mirror` `RUNNING` | R4 adjudication; C.2 verdict + `AUTHOR_RESPONSE` owed |
| 9 | — | `plan` `RUNNING` | outcome summary |

Every transition is a durable state **plus** an event (Annex J) — see § 5.2 for why the event
half cannot be written today.

---

## 4 · HUMAN TOUCHPOINTS

Only decisions that require **the Operator**. The predecessor listed ten touchpoints for the general
pipeline; this section narrows to what gates **this one A/B/Mirror run**, and separates
*one-time unblocking* from *recurring cost*.

### 4.1 · Blocking, one-time — the run cannot start until these are discharged

| # | Decision | Why it is his | Source |
|---|---|---|---|
| **H-1** | **Lift or scope the C-9 hold on L2.** Without it no capability reaches `VERIFIED`, and P-3 cannot be satisfied. | The hold is an operator instrument; `acceptance_is_not_adoption: true`. Nothing in the laboratory may lift a hold placed on it. | `PROPOSAL-C9-STATE-MODEL.md` frontmatter |
| **H-2** | **Resolve `scientist-a` / `scientist-b` `ACTOR_ID`**, currently `UNRESOLVED` **by governed decision**. | A governed decision is undone by a governed decision. | Agent Card registry, line 253 |
| **H-3** | **Role contract activation** — or an explicit ruling that the run proceeds under annexes alone. | `DEC-20260822`: *"A new, explicit activation act is required"*; it *"does not perform it, does not schedule it, and does not specify its form."* | `DEC-20260822` consequence 3 |
| **H-4** | **Rule on O-1**: `scientist_reading_modes.md`'s three activation clauses all measure SATISFIED while its status line still reads `PROPOSED`. | A `STATE_DETERMINATION` under H.1 — the same act `DEC-20260822` performed for `roles/`. | predecessor § 3.3 |
| **H-5** | **`AUTHOR_RESPONSE` to `REV-ROLES-MIRROR-001`**, outstanding. *Silence is not acceptance.* | Owed by the author under C.2. | `DEC-20260822` consequence 5 |

### 4.2 · Blocking, per-run

| # | Decision | Source |
|---|---|---|
| **H-6** | **Confirm the paper and the scope.** `BENCH-AB-001` fixes PMID 42397075; *which studies, in what order* is `Strategia complessiva → Operatore`. Orchestrator orders **within** a scope; it does not set the scope. | H.1 |
| **H-7** | **Confirm the run may consume the one prepared benchmark.** The surface is built once and frozen once; a spent blind first pass on this paper cannot be re-run blind with the same actors. | § 2.2, § 7 |

### 4.3 · Conditional — only if the run produces them

| # | Trigger | Route |
|---|---|---|
| **H-8** | persistent scientific disagreement between A and B | floor **R3 TRIADIC**, derogable only upward; forced consensus is an error; `DISAGREEMENT_UNRESOLVED` is a legitimate outcome (C.1, body §§ 27–28) |
| **H-9** | any `MAJOR` / spend / destructive / governance item | `HUMAN_APPROVAL_QUEUE`, J.3 — and **APPROVAL ≠ AUTHORIZATION** (E4): approval authorizes intent, never bypasses a gate |
| **H-10** | promoting anything from this run toward the canonical state | ordinary pipeline; the benchmark writes no `*_current.md` (§ 5 step 10) |
| **H-11** | public push | `public_release_gate.py` **plus** a human reading `git diff origin/main..main --stat` — *"the one judgement no gate makes"* |

### 4.4 · Not a touchpoint for this run — and why that is a saving

**The Scientist C question does not arise.** The predecessor's O-3/HT-4 — the dispatched
"synthesis/conflict resolution" function for Scientist C colliding with § 32 equivalence, H.1
adjudication authority, and body § 27 on forced consensus — is a live unresolved conflict. **An
A/B/Mirror run does not instantiate it.** Mirror adjudicates the *process* under R4, which is its
own defined authority; no third reader synthesizes anything. Scoping the first run to A/B/Mirror
sidesteps one open governance conflict entirely, and that is an argument for this shape of run
rather than a larger one.

### 4.5 · The critical path

The bootstrap sequence is ordered, and the hold sits upstream of almost everything:

```
I.2 step 7  registration            ← H-2 unblocks
I.2 step 8  L1 smoke → L2 smoke     ← H-1 unblocks       ⟵ THE BOTTLENECK
I.2 step 9  ORCHESTRATOR_LEASE      ← downstream of step 8
I.2 step 10 ACTIVE_ORCHESTRATOR     ← downstream of step 9
```

**Zero ACTIVE leases is not an independent blocker.** It is downstream of the L2 suspension. One
decision — H-1 — unblocks P-3, then the lease, then the assignment authority the whole § 2.3
sequence depends on. H-2 can proceed in parallel, since step 7 is separable from step 8.

---

## 5 · AUTOMATION GAP

### 5.1 · What Orchestrator could do today, with no new infrastructure

Everything here runs at `main` @ `788c357` with tools that exist:

| Act | Instrument | Status |
|---|---|---|
| Derive the lease, honestly | `lease_state.py` | ✅ runs; derives rather than reads |
| Run the full pre-flight of § 1 | `git worktree list`, `shasum`, registry read, `--help` | ✅ **all five classes measured today** |
| Build both surfaces from an allowlist | `benchmark_input_surface.py build --emit-digests` | ✅ exists |
| Prove parity, forbidden-path absence, no unlisted file, content scan | `… verify` | ✅ exists; refuses on violation |
| Fix the evaluation denominator ex ante | `… population` | ✅ deterministic; 65 units / 109 panels |
| Freeze a tree and validate the freeze set-wise | `… freeze`, `… verify-freeze` | ✅ compares `ADDED·REMOVED·MODIFIED` **set-wise, never by count**, plus an identity check against the tree's own `ASSIGNMENT.md` |
| Validate a work manifest and its locators | `deepdive_manifest.py --verify-artifacts --require-current-schema` | ✅ schema 2 |
| Run the blind locator audit | `legend-locator-audit` skill | ✅ exists |
| LINT, receipt chain, release gate | `legend_lint.py`, `fulltext_receipts.py verify`, `public_release_gate.py` | ✅ |

**This is more than it looks.** The mechanical spine of the experiment — allowlisted surface,
provable parity, fixed denominator, set-wise freeze validation, locator audit — is built and
runnable **today**. The gap is not tooling for the science.

### 5.2 · What requires infrastructure that does not exist

| # | Gap | Evidence | Consequence for this run |
|---|---|---|---|
| **G-1** | 🔴 **The J.1 consolidated EVENT LEDGER does not exist.** `ledger/` holds `approvals/`, `tasks/`, `checkpoints/`, `retirements/`, `probe/` — **no event-ledger path on any of the 43 local heads.** | swept today over all 43 heads, with a positive control (27/43 carry an approvals `.jsonl`) and a negative control (0/43 match a nonsense token), so the all-zero result is a true negative and not a silent sweep failure | Annex G.3 makes it **Mirror's primary analysis surface** — *"Mirror analizza il laboratorio dal ledger (non da 50 chat)"*. Step 8 has no surface to analyze. The predecessor left this unverified; it is now measured. Mirror's R4 must either be scoped to the frozen artifacts and receipts, or the ledger must be built first. **Either way it is a decision, not an oversight.** |
| **G-2** | **Session routing.** `ACTOR_ID` is identity, `SESSION_REF` is routing; nothing binds them, and no actor observes its own `SESSION_REF`. | `CAND-20260818` § 5c; `scientist_reading_modes.md` § 1.2 | Steps 2 and 3 assume Orchestrator can *reach* a and b. Dispatch is hand-carried by the operator. |
| **G-3** | **No carrier for "remaining workload."** No Annex B message type, no Annex A field. | predecessor § 6.3, O-6 | Progress is inferred from WORK_COMMITs and checkpoints, not reported. |
| **G-4** | **The A↔B barrier is `PROCEDURAL`.** Nothing mechanizes it. | bench § 7, quoted in § 2.5 | Detectable after the fact via `FREEZE_TIMESTAMP_UTC` + `SURFACE_COMMIT`; never prevented. |
| **G-5** | **No task lock, no exactly-once delivery, no failure detection, no runtime RBAC, no guaranteed singleton.** | **Annex J.0**, the normative table | Each has a named compensating protocol. *"Vietato a qualsiasi documento o attore descrivere questi meccanismi con vocabolario più forte del protocollo compensativo."* |
| **G-6** | **The approval queue diverges by ref.** `main` = 6 lines; `orchestrator` = **10**, carrying the SCIAB/XPORT/P5DOMAIN approvals. | measured today; predecessor O-4 | **An approval state read from `main` alone is wrong.** Re-confirmed at `788c357`. |
| **G-7** | **Nothing runs between turns.** *"Nothing compels the Orchestrator to record an acquisition, and nothing runs between turns."* | `lease_state.py` own docs | Every mechanical check derives correctly from what it is given, and **cannot derive from what was never written down.** |

### 5.3 · The gap, stated plainly

> **The automation gap for the first run is not scientific tooling — it is the control plane.**
> The experiment's mechanical spine exists and runs. What is missing is the layer that would let
> the laboratory *dispatch, observe and record itself*: routing (G-2), an event ledger (G-1), and
> anything that acts between turns (G-7). Every one of those is compensated **procedurally**, by
> a human doing it by hand. That is why § 4 is short but not optional: **for the first run,
> The Operator is the control plane.**

---

## 6 · FINAL QUESTION — the smallest sequence that proves LEGEND can execute one scientific loop

### 6.1 · First, a distinction the question requires

`BENCH-AB-001` **does not close a scientific loop, by design**:

> § 5: *"Steps 5–9 each reach `main` only through an integration candidate. **Nothing in the
> benchmark writes a `*_current.md`, the receipt ledger, or any registry.**"*
> Step 10: *"any promotion of a claim → ordinary pipeline."*

So there are two different loops, and only one of them is what the A/B experiment proves:

| Loop | Terminates at | Proves |
|---|---|---|
| **Coordination loop** | frozen outcome summary | that the laboratory can dispatch, blind, freeze, compare, audit and adjudicate — **multi-actor discipline** |
| **Scientific loop** | `BATCH_COMMIT` into the four current files | that evidence becomes canonical state — **the thing LEGEND exists to do** |

The A/B/Mirror experiment is the **first**. It deliberately stops before the second.

### 6.2 · The answer

**The smallest sequence that proves the *coordination* loop — the A/B/Mirror run as dispatched:**

```
PRE-FLIGHT (§1, all seven P-rows)
  → Plan: build · verify · population · FREEZE manifest
  → Orchestrator (lease ACTIVE): two contracts, one PARALLEL_READ_GROUP
  → HANDOVER
  → A ∥ B  blind, concurrent
  → Plan: FREEZE on declaration, before reading
  → blind locator audit
  → Mirror R4 on the process
  → outcome
```

**Seven acts. Four actors** — Orchestrator, Plan, two Scientists — **plus Mirror.** Nothing in
that chain can be dropped without dropping what it proves: remove Plan and there is no freeze;
remove the audit and a reading that overstates its source passes; remove Mirror and nothing
judged the method; run A and B in sequence with sight of each other and there was no experiment.

**But it is not the smallest sequence that proves *one scientific loop*.** That one is smaller:

```
one paper  →  one registered Scientist with VERIFIED L2 capabilities
           →  one complete_fulltext_read: receipt + work manifest with verbatim_locators.entries[],
              coverage map with no `not_read`
           →  one blind locator audit
           →  one review at the Annex C floor for the claim class
           →  one COMMIT CANDIDATE
           →  one BATCH_COMMIT, LINT green, manifest updated
```

**One Scientist. One reviewer. One paper.** That chain touches every layer LEGEND is made of —
evidence, locators, review, candidate, canonical state — and it is the only one of the two that
ends with the four current files changed.

### 6.3 · The recommendation, and it is not the one the dispatch implies

> **The A/B/Mirror run is the more expensive experiment and proves the less fundamental thing.**

It needs **both** Scientists registered and L2-verified (H-1 **and** H-2), a built and frozen
surface, and a Mirror surface that does not exist (G-1). The single-Scientist loop needs **one**
actor registered, no benchmark surface, no freeze discipline, no comparison matrix — and it
proves that evidence can become canonical state, which is the claim LEGEND actually makes.

The honest ordering, offered as an observation and **not as a decision**:

1. **Run the single-actor scientific loop first.** It discharges fewer human touchpoints, and it
   is the one that produces the L2 evidence — *full-text read producing a receipt*, *work
   manifest with verbatim locators*, *worktree confinement* — that **P-3 of the A/B benchmark
   demands anyway**. It is not a detour; it is the prerequisite, run as its own experiment.
2. **Then run A/B/Mirror**, whose value is the comparison of two *modes* — a question that only
   becomes meaningful once one mode is known to work end to end.

**This is an observation for the operator, not a plan I am authorized to sequence.** Which
experiment runs first is H.1 `Strategia complessiva → Operatore`, and § 4 H-6 names it as his.

---

## 7 · Open observations carried from this record

The predecessor's O-1…O-8 stand unresolved. This record adds three and resolves one.

| # | Observation | Disposition owner |
|---|---|---|
| **N-1** | 🔴 **Resolves predecessor § 7.3.1**, which recorded Mirror's surface as *"an instrument whose state I did not verify as operational."* It is now verified: the J.1 consolidated event ledger — Annex G.3's stated primary analysis surface for Mirror — **does not exist on any of the 43 local heads** (swept with positive and negative controls, § 5.2 G-1). Mirror's step-8 input must be scoped to the frozen artifacts and receipts, or the ledger must be built first. | Plan / operator |
| **N-2** | The dispatched four-position order omits Plan (5 of 11 steps, incl. FREEZE) and the blind locator audit; and `A → B` misrepresents a concurrent mutually-blind fork as a chain (§ 2.2). | dispatcher |
| **N-3** | `WAITING_REVIEW` exists nowhere; `FROZEN` is not a lifecycle state; `FAILED` is not an A.5 terminal, and collapsing runtime faults into it defeats Annex F.4's *"mai classificare come rifiuto un guasto di runtime"* (§ 3.1). | Plan (schema) / operator |
| **N-4** | Two role-seat tips (`mirror`, `evidence-index`) moved since 2026-08-22 with no instrument reporting it; O-4's ref divergence re-confirmed at `788c357` (main 6 / orchestrator 10). | Plan |

---

## 8 · What this record does NOT do

- It does **not** dispatch, activate, register, or assign anything to anyone.
- It does **not** create a Task Contract, a `PARALLEL_READ_GROUP`, a Mirror task, a candidate, or
  a ledger event.
- It does **not** lift the C-9 hold, verify a capability, acquire a lease, or resolve an
  `ACTOR_ID`.
- It does **not** decide which experiment runs first — § 6.3 is an observation under H-6.
- It does **not** resolve O-1…O-8 or N-1…N-4.
- It does **not** modify `governance/`, `roles/`, `framework/`, or `ledger/`.
- It is **not** an `AUTHOR_RESPONSE`, a `WORK_COMMIT`, or a `BATCH_COMMIT`.
- It does **not** redesign governance: every state name in § 3 is quoted from an existing machine,
  and the two that do not exist are reported as absent rather than invented.

### 8.1 · Constraint compliance

| Constraint | Result |
|---|---|
| READ-ONLY ANALYSIS | ✅ exactly one file created; no other path touched |
| governance not redesigned | ✅ § 3 maps onto existing vocabulary; absent terms reported, not coined |
| roles not activated | ✅ § 4 H-3 records the act as owed, and does not perform it |
| experiment not executed | ✅ no surface built, no contract issued, no actor contacted |
| existing vocabulary used | ✅ § 3.2 verbatim from A.5, J.2, J.3, I.4, C.2, bench § 7 |
| Orchestrator authority not assumed | ✅ § 0; every rule cited from body/annex/protocol, never from a role contract |

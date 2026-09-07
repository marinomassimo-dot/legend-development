---
artifact: ANALYSIS — control plane reconciliation, observation only
record_id: CONTROL-PLANE-RECONCILIATION-ANALYSIS-001
task_id: CONTROL_PLANE_RECONCILIATION_ANALYSIS_v1
dispatcher: operator
date: 2026-08-22
author_session: root checkout at dispatch; this record written and committed in an isolated
  worktree on branch `orch-control-plane-reconciliation`, cut from `main` at `788c357`
actor_id: NOT ESTABLISHED — see IDENTITY. This record is not authored under a role contract.
governance_version: 3.1.1 (read, not exercised)
classification:
  - ANALYSIS ONLY
  - NOT GOVERNANCE
  - NOT A PROTOCOL
  - NOT AN IMPLEMENTATION PROPOSAL
domain: >
  CONTENT. `learning/` is content by intent, declared in `plan_defined_parameters.md` § P5.1:
  CONTROL_PLANE_ROOTS are exhaustively `governance/candidates/`, `ledger/`, `reviews/`, and
  `learning/` is deliberately not among them. This record therefore sits inside the
  CANDIDATE_CONTENT_HASH of any future candidate that re-aligns onto this branch or onto a
  `main` that carries it. The directory name `learning/orchestrator/` is where its two sibling
  analyses live; it is a path, not a claim to be the Orchestrator.
authority_claimed: none
verdict_transfer: >
  NONE. Every mechanical fact below was executed in this session against the refs named. Three
  adjacent analyses exist on other branches (see S-4); nothing is carried from any of them
  without independent re-measurement, and where my measurement differs from theirs, both are
  stated.
---

# CONTROL PLANE RECONCILIATION — ANALYSIS 001

> **OBSERVATION ONLY.** Nothing here designs a solution, creates a protocol, resolves a
> governance question, activates a contract, creates an actor, or assigns work. Gaps are
> measured and left open.

---

## TASK_STATUS

```
DISPATCH        CONTROL_PLANE_RECONCILIATION_ANALYSIS_v1
MODE            READ_ONLY ANALYSIS → ONE ARTIFACT ON ITS OWN BRANCH
STATUS          COMPLETE as analysis
BRANCH          orch-control-plane-reconciliation, cut from main @ 788c357
WRITES          exactly one new path, under learning/orchestrator/
```

**Constraints held, each verifiable against the diff:**

| Constraint | Held |
|---|---|
| Do not modify `governance/` | ✅ zero paths touched |
| Do not modify `roles/` | ✅ zero paths touched |
| Do not modify `framework/` | ✅ zero paths touched |
| Do not modify `ledger/` | ✅ zero paths touched |
| Do not activate contracts | ✅ no `status:` line anywhere was read as binding, and none was edited |
| Do not create actors | ✅ no registration, no ACTOR_ID assignment, no Agent Card row |
| Do not propose implementation | ✅ no design, no schema, no file layout proposed |
| Do not create a protocol | ✅ nothing here is normative and nothing claims to bind |
| Do not resolve governance questions | ✅ every ambiguity found is recorded in OPEN_QUESTIONS with its disposition owner, unresolved |

**Not done, deliberately:** no lease acquired or renewed; no message sent to any session; no
task record, checkpoint, review, approval or event written; no branch merged; nothing pushed;
the root checkout left on `main`, clean, untouched.

---

## IDENTITY

### The dispatch addressed this session as Orchestrator. The repository does not support the claim.

Identity is not inherited from a dispatch. Every row below was measured this session.

| Fact | Measured value | Instrument |
|---|---|---|
| Working directory at dispatch | `<REPO_ROOT>` | `git rev-parse --show-toplevel` |
| Branch at dispatch | `main` | `git rev-parse --abbrev-ref HEAD` |
| HEAD at dispatch | `788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5` | `git rev-parse HEAD` |
| Working tree at dispatch | clean, 0 porcelain entries | `git status --porcelain` |
| **ORCHESTRATOR_LEASE** | 🔴 **`ACTIVE by derivation: 0`** — 5 records, 2 STALE / 3 RELEASED, most recent released `2026-08-18T14:05:20Z` | `python3 framework/scripts/lease_state.py --check` |
| Runtime inventory | 🔴 **absent on `main`**; present at `runtime/runtime_inventory.md` on branch `orchestrator` only | per-ref `git ls-tree` |
| Agent Card registry | 🔴 **absent on `main`**; present at `runtime/agent_card_registry.md` on branch `orchestrator` only | per-ref `git ls-tree` |
| `ACTOR_ID` | **not established** — no registration record for this session exists on any ref | — |
| `SESSION_REF` | **not observable** — `ListAgents` returns peers, never self; not invented | — |

`framework/scripts/lease_state.py --check` additionally reported two standing findings on
lease #3, both of which I reproduced rather than accepted: `DISAGREEMENT` (stored `EXPIRED`,
derived `STALE`; `EXPIRED` is not in Annex I.3's vocabulary) and `EXPIRED_WITHOUT_RENEWAL`.

### The consequence, stated plainly

`CLAUDE.md` § 0 is unconditional and both of its antecedents hold:

```
IF no valid runtime inventory / no ACTIVE ORCHESTRATOR_LEASE:
    ENTER BOOTSTRAP_MODE. Read /BOOTSTRAP.md.
    Do NOT assume Orchestrator authority merely because you are in root.
```

**This session is in `BOOTSTRAP_MODE` and is not the Orchestrator.**

### Why the dispatch's instruction and the repository agree

The dispatch said: *"Do not assume authority from `roles/orchestrator.md`. Derive all authority
only from repository-defined sources."* The repository has already ruled on exactly this.
`governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` — an operator
determination under H.1, on `main`, dated today — returns **OPTION B, `ACTIVATION_NOT_CONFIRMED`**:
the four role contracts remain `PROPOSED`. Its consequence 2:

> **No actor authority may be assumed from these contracts.** Any authority an actor exercises
> must be traced to the governance body or to a named annex.

Every rule cited in this record is therefore cited from the **body** or from a **named annex**.
Role contracts appear only descriptively, and `BOOTSTRAP.md` — which itself carries
`status: PROPOSED — binding once Mirror hostile review passes and the operator approves` — is
cited the same way.

### What authority this task actually needed: none

The dispatch is read-only analysis. It creates nothing, assigns nothing and changes no state.
H.1 places *Strategia complessiva* with the operator, and this analysis was dispatched by the
operator. **No Orchestrator authority was required and none was exercised.** Where the analysis
touches a decision, the decision is left to its owner.

---

## SURFACE_MAP

### S-1 · The measurement universe every claim below is scoped by

```
MEASURED_AT   2026-08-22T17:15–17:22Z, against the repository at <REPO_ROOT>
REFS          refs/heads  37   ·  refs/remotes  4  ·  refs/tags  5   ·  ALL 51
WORKTREES     19 entries from `git worktree list` (the root checkout + 18 linked)
```

🔴 **The ref population is itself unstable, and this matters for reading any prior analysis.**
Two records written in this repository within the last 24 hours scope their sweeps to *"41 local
heads"* and *"45 refs"*. I measure **37** `refs/heads` and **51** refs of all kinds. I did not
establish which branches were created or deleted between those measurements and mine, and I do
not assert that either earlier number was wrong when taken. **The consequence is the finding:**
a sweep expressed as *"0 of N refs"* is not comparable across sessions unless N is pinned, and
none of the three analyses pins it to a commit.

### S-2 · Measurement hygiene — two traps, one of which caught me

| # | Trap | What happens | Control that catches it |
|---|---|---|---|
| **H-1** | `for r in $REFS; do …` in zsh | zsh does **not** word-split unquoted parameter expansions. The loop body runs **once**, with `$r` bound to every ref concatenated, and every per-ref sweep returns a clean, false `0`. Also `"$r:path"` applies zsh's `:r` modifier and returns nothing for every ref | Every sweep in this record ran through `printf '%s\n' "$REFS" \| while IFS= read -r r`, and **every negative sweep was paired with a positive control in the same loop**. The control used was `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl`, which returned **21 refs PRESENT** — so the loop demonstrably iterates |
| **H-2** | 🔴 **Mine, this session.** Grepping the approval queue for `"APPROVAL_ID":"…"` | The queue's later lines are written `"APPROVAL_ID": "…"` — **with a space after the colon**. My first pass reported the `orchestrator` queue as carrying only the five GOV311 records, and its 10-line length contradicted that | The line count contradicted the ID count. Re-run with `"APPROVAL_ID"[[:space:]]*:[[:space:]]*"[^"]*"` returned **four further approvals**. The false negative existed for one tool call and is recorded because a sweep that agrees with an expectation is the one that does not get re-run |

**Nothing in this record rests on a negative sweep that was not paired with a positive control.**

### S-3 · Control-plane surfaces — what exists, and on which ref

Each row measured across all 37 `refs/heads`.

| Surface | Instrument | Measured state |
|---|---|---|
| Governance body + annexes A–J | `governance/` | ✅ complete, `FROZEN`, on `main` |
| Plan-delegated parameters P1–P7 | `plan_defined_parameters.md` | ✅ on `main`; P7 = *"design chosen; writer and validator not yet built"* |
| Role contracts ×4 | `roles/` | ✅ present on `main`, **all four `status: PROPOSED`**, non-binding per `DEC-20260822` |
| ORCHESTRATOR_LEASE | `runtime/orchestrator_lease.md` + `lease_state.py` | ✅ tracked, on 16 refs, **0 ACTIVE**; derivation runs |
| HUMAN_APPROVAL_QUEUE (J.3) | `ledger/approvals/…jsonl` | ⚠️ present on **21 refs**, **forked** — see F-6 |
| Task records (A.1) | `ledger/tasks/` | ⚠️ **5 records, union across all refs, all under `plan/`** |
| Checkpoints (A.6) | `ledger/checkpoints/` | ⚠️ **27 records: 19 `plan`, 8 `mirror`. Zero for orchestrator, zero for any scientist** |
| Reviews (C.2) | `reviews/` | ⚠️ **73 paths in union** — 51 `mirror`, 15 `orchestrator`, 7 `plan`; of these **40 are `REV-*`** and **8 are `AUTHOR-RESPONSE-*`** |
| Learning records (E.6) | `learning/` | ⚠️ **72 paths in union** — 34 `mirror`, 24 `plan`, 14 `orchestrator` |
| Full-text receipt ledger | `fulltext_receipts.py` | ✅ **128 chained receipts, tail anchored, `verify` OK** — the only append-only ledger here with a hash chain *and* a validator |
| Agent Card registry (I.4) | `runtime/agent_card_registry.md` | ⚠️ **branch `orchestrator` only**; self-declares `PARTIALLY REGISTERED — 3 of 6` and `0 verified capabilities` (dated 2026-08-16/17) |
| Runtime inventory (§43) | `runtime/runtime_inventory.md` | ⚠️ **branch `orchestrator` only**; self-declares `SKELETON` |
| L2 capability outcomes | `runtime/L2-OUTCOMES.md` | ⚠️ **branch `orchestrator` only**; records **3 VERIFIED of 12 attempted**, ratified 2026-08-18 |
| **EVENT LEDGER (J.1 / P7)** | `ledger/events/<ACTOR_ID>.jsonl` | 🔴 **ABSENT on all 37 refs** |
| **Consolidated event view** | `ledger/consolidated/` | 🔴 **ABSENT on all 37 refs** |
| **LEARNING_INDEX (E.2)** | — | 🔴 **ABSENT on all 37 refs** |
| **ACTIVE_LESSONS (E.5)** | `active_lessons/` | 🔴 **ABSENT on all 37 refs** |
| **OPERATOR_DAILY_BRIEF (§10.4)** | — | 🔴 **ABSENT on all 37 refs** |
| **AUTONOMY LEDGER (G.3)** | — | 🔴 **ABSENT on all 37 refs** |
| **Actor registry** | `framework/state/actors.yaml` | 🔴 **has never existed on any ref** — `git log --all` returns empty |

### S-4 · Three adjacent analyses exist, each on a different branch, none on `main`

This is a surface fact before it is a finding, and it is why this record re-measured everything.

| Branch | Artifact | Commit subject |
|---|---|---|
| `main` @ `788c357` | `learning/orchestrator/SCIENTIFIC-PIPELINE-PREPARATION-001.md` | *The pipeline is prepared where it can be read, and the authority to run it was not assumed* |
| `orch-agent-coordination-protocol` @ `f8532c9` | `learning/orchestrator/LEGEND-AGENT-COORDINATION-PROTOCOL-001.md` | *Every stage has a creator, almost none has a closer, and two reported absences were never absent* |
| `orch-pipeline-loop-architecture` @ `d6d46f8` | `learning/orchestrator/ORCHESTRATOR-SCIENTIFIC-PIPELINE-AND-LOOP-ARCHITECTURE-ANALYSIS-001.md` | *The loop is blocked by addressing, and the record of what a human decided is three files* |

All three are dated 2026-08-22. Two of the three are invisible from `main`. **This record is the
fourth, and by writing it on its own branch it reproduces the condition it is measuring** — that
is stated rather than avoided, because the alternative (writing to `main`) is a canonical write
this session has no authority to make.

### S-5 · What is executable today — measured by running it, not by reading a claim

| Command | Result this session |
|---|---|
| `legend_lint.py .` | **VERDICT: PASS** (1 INFO: CLAIM 010 wikilink) |
| `fulltext_receipts.py verify` | **OK: 128 chained receipt(s), tail anchored** |
| `growth_anchors.py check` | **VERDICT: PASS** — claims=39 · papers=70 · corpus=356 · literature=390 |
| `public_release_gate.py` | **BLOCKS: 0** (4 `[REVIEW]` lines, all under `disease-models/`) |
| `governance_fingerprint.py compose --all` | **4 fingerprints emitted** — mirror `e01b4108…`, orchestrator `88dea7a6…`, plan `0d6987bd…`, scientist `b66959cd…` |
| `lease_state.py --check` | **ACTIVE by derivation: 0** + 2 findings on lease #3 |
| `locator_audit.py --help` | runs; scope is *"Does every locator's quote actually occur in the artifact it was taken from?"* |

🔴 **Every one of these validates scientific state, publication safety, or a hash. Not one of
them validates a control-plane lifecycle object.** Measured directly: `git grep -l` across all
`*.py` on `main` for `TASK_ASSIGNMENT|TASK_CLAIM|CHECKPOINT_ID|REVIEW_ID|EVENT_ID|APPROVAL_ID`
returns 22 files, and inspection shows every hit is an unrelated string in the scientific
pipeline (`batch_queue`, `reading_state`, `sync_epochs`, the DisMech exporters) — **no script
reads an Annex A.1, A.6, B.1, C.2, J.1 or J.3 object.**

---

## FINDINGS

### F-1 · AGENT-TO-AGENT LIFECYCLE — seven stages, measured

Columns are the dispatch's. **Creator** = who is authorised to bring the stage into being.
**Owner** = who holds it while it is open. **Validator** = what mechanically checks it —
`—` means no instrument exists, not that no human looks. **Closer** = what durably ends it.

| Stage | Instrument | Creator | Owner | Validator | Closer | 🔴 Missing owner |
|---|---|---|---|---|---|---|
| **1 · Task creation** | Annex A.1 `TASK_ASSIGNMENT`, 15 fields, fully specified | **Orchestrator** (H.1 row 1, not conditioned on a lease) | the named `OWNER` | **none** | the owning actor edits `CURRENT_STATE` in its own record | 🔴 **the assigner.** All **5** task records in existence are `ledger/tasks/plan/*`, written by `plan` about `plan`. `XPORT-ROUTING-001` states it in its own `_note`: *"No `TASK_ASSIGNMENT` message was received… no ACTIVE ORCHESTRATOR_LEASE existed at any point in this session, and no Orchestrator was reachable to assign it."* The authority is allocated and has never been exercised |
| **2 · Task assignment** | A.1 + B.1 envelope + A.2 `TASK_ACK` + A.3 `TASK_CLAIM` | Orchestrator | assignee | **none** | A.3 durable claim | 🔴 **the ACK counterparty.** B.3 makes ACK mandatory on `STATE_CHANGE: yes`. Measured: exactly **one** file in the entire union is named as an ACK artifact — `reviews/mirror/ACK-L2-20260818-ORCH-032.md` — and it acknowledges an L2 row, not a task. **No `TASK_ACK` record exists for any task.** Every `TASK_CLAIM` on record is an embedded field in the claimant's own JSON: self-claimed, no counterparty, no conflict detector run |
| **3 · Task completion** | A.5 `COMPLETE`; `ACCEPTANCE_CRITERIA` (free text); for readings, `scientist_reading_modes.md` §§ 3.6/3.8 five-step test | the owning actor declares | the owning actor | **split.** For a scientific reading, steps 1–4 are mechanical and the tools exist and run (`deepdive_manifest.py`, `locator_audit.py`). For **every other artifact class**, `ACCEPTANCE_CRITERIA` is free text with no validator | 🔴 **nothing durable.** J.1 defines `TASK_COMPLETE` as an event type; the ledger that would hold it exists on **0 of 37 refs** | 🔴 **the closer.** A task is "complete" when its owner says so in a file its owner also writes. Nobody countersigns, and nothing records the transition outside the owner's own record |
| **4 · Review request** | B.2 `REVIEW_REQUEST` / `REVIEW_OPENED`; C.3 *"apertura solo via Orchestrator"* | **Orchestrator only** (C.3, body § 25) | the assigned reviewer | **none** | n/a at this stage | ⚠️ none by rule — but the rule is unexercisable. With no reachable Orchestrator, reviews are opened by **handoff artifacts authored by the reviewed party**: 6 `HANDOFF-*` files under `governance/candidates/`, each written by `plan`, each requesting its own review |
| **5 · Review completion** | **Annex C.2 — the strongest object in the lifecycle.** `STEELMAN` mandatory *before* objections; 4 verdicts; `WHAT_WOULD_CHANGE_MY_MIND` mandatory; `AUTHOR_RESPONSE` mandatory | the reviewer | reviewer (verdict) **+ author** (response) | **none** | 🔴 **the author, not the reviewer.** C.2: *"`AUTHOR_RESPONSE` obbligatoria; il silenzio non è accettazione."* A verdict does not close a review | 🔴 **the adjudicator, when the author holds H.1's adjudication row.** C.3 requires `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR`; H.1 gives challenge adjudication to Orchestrator. When Orchestrator authors the reviewed object, the only remaining adjudicator is the operator. **Coverage measured: 40 `REV-*` artifacts, 8 `AUTHOR-RESPONSE-*` artifacts** |
| **6 · Escalation** | J.3 `HUMAN_APPROVAL_QUEUE` (durable object, never *"solo un messaggio"* — body § 4); F.2 `ORCHESTRATOR_CHALLENGE`; § 48 stop conditions → `BLOCKED_BY_GOVERNANCE` | any actor may raise; **Orchestrator classifies ordinary `HUMAN_REQUIRED`** (H.1); a stop condition may be hit directly | the **operator** | **none** — no queue schema validator exists | the operator, by appending a `RESOLUTION` line | 🔴 **the reconciler.** The queue works *within* a branch and has no owner *across* branches — see **F-6**. Compounding it: **`OPERATOR_DAILY_BRIEF` (§ 10.4), the surface on which `PENDING HUMAN DECISIONS` is required to be exposed, does not exist on any ref** |
| **7 · Closure** | J.1 closing events carrying `CLOSES_EVENT_ID`; A.5 terminal states; D.4 batch transaction | — | — | **none** | 🔴 **nothing, anywhere** | 🔴 **the closer of everything.** J.1 is explicit that open→outcome linkage lives *only* in the closing event, and that a `closed_by` field may exist *only* in a derived view. The event ledger is absent on all 37 refs; P7 chose design (a) and records *"writer and validator not yet built"*; the L2 round classifies `M4` (event-ledger write) as **BLOCKED — no event-ledger writer** |

#### F-1.1 · The shape of the result

**Six of seven stages have a defined creator. One of seven has a defined closer, and that one —
review completion — closes at 8 responses against 40 reviews.** Closure is not weakly owned; for
five of the seven stages the closing instrument **does not exist as a file on any branch**.

This is not a discovery about the governance text, which specifies closure carefully. It is a
measurement of the distance between the specification and the installed system.

### F-2 · ADDRESSING — the five questions, measured

The dispatch asks how an agent knows five things. Measuring only; no solution is designed.

| Question | Instrument that would answer it | Measured state | Gap |
|---|---|---|---|
| **Which artifact to read?** | repository-relative path | ✅ used universally; every dispatch record in the repository addresses by path | **none at this level** |
| **Which ref contains it?** | B.1's `DURABLE_POINTER` field | 🔴 **no schema requires a ref.** `cross_session_transport.md` § 1.2 fills `DURABLE_POINTER` with a rule that includes `branch` and states *"naming the branch is part of the claim"* — and that protocol reads `status: PROPOSED — binding once Mirror hostile review passes and the operator approves` | 🔴 **THE LOAD-BEARING GAP.** Measured on myself: to establish three facts in this record I had to sweep 37 refs, because `runtime/L2-OUTCOMES.md`, `DEC-20260818-007-LAB-REACTIVATION.md` and `AUTHOR-RESPONSE-ROLES-MIRROR-001.md` each exist on exactly one branch and none of them is `main`. **A path without a ref is not an address in this repository** |
| **Which version is canonical?** | for candidates: `CANDIDATE_CONTENT_HASH` + `BASE_HEAD` | ✅ **solved, and mechanized, for exactly one object class.** `candidate_content_hash.py` is deterministic, reproducible by an independent route, and Gate 5 (J.3) requires an approval to cite the exact hash. 🔴 **For every other object class there is nothing** | 🔴 the strongest addressing instrument in the system covers candidates and nothing else. **F-6 shows the cost on the approval queue; F-7 on a canonical protocol file** |
| **Who produced it?** | `ACTOR_ID` (A.1 `OWNER`, I.4) | ✅ **defined, persistent, and correctly separated from the ephemeral `SESSION_REF`** — body § 8, § 21. Every task, claim, checkpoint and receipt is keyed by `ACTOR_ID + TASK_ID + GENERATION`, never by a session | ⚠️ **identity is solved; routing is not.** No actor observes its own `SESSION_REF`; the registry that would record one lives on `orchestrator` alone and marks every capability `UNVERIFIED` — a value **F-7 shows is stale**; `framework/state/actors.yaml` has never existed on any ref. Attribution works; delivery does not |
| **Whether it is complete?** | per-class completion predicate | ⚠️ **two predicates of very different quality.** A scientific reading has a five-step acceptance test whose steps 1–4 are mechanical and executable today. Everything else has `ACCEPTANCE_CRITERIA`, free text, no validator | 🔴 **no completeness predicate exists for any control-plane object** — not for a task, a claim, a checkpoint, a handoff, a review, or an approval |

#### F-2.1 · The completion predicate, stated precisely

Step 5 of the reading acceptance test is the **blind locator audit** — fresh agents receive
`(proposition, quote, anchor)` triples and never the dossier or the reader's identity. It is
agent-conducted, not scripted. `framework/scripts/locator_audit.py` **exists and runs**, and it
answers an adjacent, narrower question — *does the quote occur in the artifact it was taken
from* — which is a **precondition** of step 5, not step 5. The judgement step 5 makes (does the
quote *support* the proposition; does the source say *more or less* than the proposition claims)
has no scripted form. Stated this way because "step 5 has no executable form" and "a locator
audit script exists" are both true and describe different objects.

### F-3 · EVENT MODEL

#### F-3.1 · Ledger surfaces that exist

| Surface | Append-only? | Hash-chained? | Validator? | Consumed by? |
|---|---|---|---|---|
| Full-text receipt ledger | ✅ | ✅ | ✅ `fulltext_receipts.py verify` | ✅ LINT consumes it |
| `HUMAN_APPROVAL_QUEUE.jsonl` | ✅ by convention, stated in its own `_note` | ❌ | ❌ | nothing mechanical |
| `ledger/tasks/` | n/a (one file per task) | ❌ | ❌ | nothing |
| `ledger/checkpoints/` | ✅ by construction (new id per checkpoint) | ❌ | ❌ | nothing |
| `runtime/orchestrator_lease.md` | ✅ by convention | ❌ | ✅ `lease_state.py` derives | nothing else |
| `sync_epochs.jsonl`, `growth_anchors.jsonl` | ✅ | ❌ | ✅ | LINT / growth check |

🔴 **The pattern the event ledger is supposed to reuse already exists and works.** P7 says so in
terms: *"This should reuse the existing append-only machinery, not invent a second one… the
repository already runs an append-only ledger with a hash chain and a tail anchor."* The
instrument to copy is present, verified at 128 chained receipts this session, and consumed by
the LINT.

#### F-3.2 · The missing event stream

```
J.1 minimum event types                     23
types ever emitted anywhere                  0
ledger/events/<ACTOR_ID>.jsonl on 37 refs    ABSENT
ledger/consolidated/ on 37 refs              ABSENT
P7 status                                    "design chosen; writer and validator not yet built"
L2 row M4 (event-ledger write)               BLOCKED — no event-ledger writer
```

**The design decision was made and is not the blocker.** P7 chose option (a) — per-actor
append-only JSONL in each actor's own worktree, consolidated by Plan into a derived view — and
gave the reason: option (b) derives events from commits and ACKed messages and *structurally
cannot represent* `CHECKPOINT_WRITTEN`, `ACTOR_DOWN`, `LEASE_STALE`, `HUMAN_REQUIRED_OPENED` or
`RESUMED_FROM_MILESTONE`. What is missing is a writer and a validator.

#### F-3.3 · Relationship between events and learning

Annex G.3 makes the consolidated event ledger **Mirror's primary analysis surface**, explicitly
so that Mirror analyses the laboratory *"non leggendo le chat."* Measured:

```
consolidated event ledger      ABSENT on 37 refs   ← Mirror's designated input
LEARNING_INDEX (E.2)           ABSENT on 37 refs   ← the index of what was learned
ACTIVE_LESSONS (E.5)           ABSENT on 37 refs   ← the role-specific subset for rehydration
raw learning records           72 paths, present, unindexed, spread across refs
```

🔴 **The raw archive exists; the input surface and the index that would make it usable both do
not.** E.5 guarantees *"RAW archive lossless"* and the raw archive is indeed intact — 34 mirror,
24 plan, 14 orchestrator records. What is absent is every stage of the pipeline
`RAW ARCHIVE → Mirror clustering → ACTIVE LESSONS → role-specific subset → rehydration` after
the first. The `active_lessons/` directory the root `CLAUDE.md` points to is annotated in that
file itself as **"not yet materialized"**, and that annotation is accurate.

A second-order consequence, measured: **both PROVISIONAL practices expire on an event that
cannot occur.** `PROV-ACK-TIMEOUT-30M` (P3.1) and `PROV-HEARTBEAT-30M-3X` (P4.1) each declare
`EVIDENCE_EXPECTED: … from the event ledger (J.1)` and `EXPIRY: after the third scientific
batch`. Annex E.3 states *"Mai provisional per sempre."* Zero scientific batches have run under
this governance, and the evidence source does not exist. The two parameters that govern message
reliability and failure detection are therefore provisional with no path to promotion or
rejection.

#### F-3.4 · Relationship between events and handoff

`HANDOFF` is named in the Annex B.2 enumeration and **specified nowhere else** — no envelope
beyond B.1, no required field, no state effect. Measured consequence: **15 handoff artifacts
across 5 namespaces**, each with a shape of its own:

```
governance/candidates/HANDOFF-*        6    (candidate → reviewer)
release/*_HANDOFF.md                   3    (release engineering)
learning/{mirror,plan}/HANDOFF-*       3    (actor → actor, informal)
runtime/handoff/C-2/…                  2    (scientific working material)
reviews/mirror/HANDOFF-*               1    (review readiness)
```

🔴 **Without a closing event, a handoff has no observable completion.** The sender's artifact is
durable; the receiver's *acceptance* leaves no trace anywhere. Whether a handoff was received,
read, accepted or refused is not a fact this repository can currently answer about any of the 15.

### F-4 · The three concurrent analyses are the reconciliation problem, demonstrated

Four analyses of the same control plane were written on 2026-08-22 (S-4, including this one).
They sit on four branches. **No ref carries more than one of them.** None can cite another
without a cross-ref lookup that no schema requires and no tool performs.

I re-derived the shared measurements rather than inheriting them, and the results agree on the
structural absences — event ledger, LEARNING_INDEX, active_lessons, daily brief, autonomy ledger
— which is meaningful only because the derivations were independent. **Agreement on a count is
not verification of the set beneath it**, so each absence above was re-swept in this session with
its own positive control (S-2).

Where I differ, I differ on **N** (S-1) and on one substantive precondition (F-7).

### F-5 · A duty recorded as outstanding on `main` was discharged on a branch

`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md`, on `main`, consequence 5:

> **`REV-ROLES-MIRROR-001`'s `AUTHOR_RESPONSE` remains required and outstanding** (Annex C.2:
> silence is not acceptance).

Measured this session across all 37 refs:

```
reviews/plan/AUTHOR-RESPONSE-ROLES-MIRROR-001.md
    present on:  plan-orchsurf-r4-transcription   (and no other ref)
    commit:      de0ae4e  "One review was answerable by its author and the other was owed to someone else"
    dated:       2026-08-22
    disposition: MAJOR-1 ACCEPTED · MINOR-1 ACCEPTED · MAJOR-2 ACCEPTED · MINOR-2 ACCEPTED
                 MAJOR-3 ACCEPTED with changed character · MINOR-3 CONTESTED WITH EVIDENCE
```

🔴 **The duty was discharged. The record that discharges it is unreachable from the ref that
records the duty.** Both statements are true simultaneously and neither party is at fault:
`DEC-20260822` was accurate when written, and the response is a real artifact. What is missing
is any mechanism by which the second fact reaches the first. This is F-2's ref question with a
concrete cost attached.

### F-6 · 🔴 The `HUMAN_APPROVAL_QUEUE` has forked into three disjoint histories

This is the most consequential single measurement in this record, because J.3's queue is the
**only durable record of what a human decided**.

```
UNION of APPROVAL_IDs across all 37 refs                     10
common prefix shared by every copy                            6 lines / 5 records (GOV311)
main is a BYTE-EXACT PREFIX of both divergent copies          verified with cmp
refs carrying more than the common prefix                     2 lineages, DISJOINT
refs carrying the union                                       0
```

| Ref | Records | Extension beyond the common prefix |
|---|---|---|
| `main` **(canonical)** | **2 approvals + 2 resolutions + 1 correction** | — none |
| 19 other refs | same 5 | — none |
| `orchestrator` | 6 approvals | `APR-20260818-SUNSET-DEC3-001`, `APR-20260819-SCIAB-001`, `APR-20260819-XPORT-001`, `APR-20260819-P5DOMAIN-001` |
| `evidence-index`, `p51c9-rebased-onto-c89c2217` | 6 approvals | `APR-20260817-HA-1` … `HA-4` |

Blob oids, proving three distinct objects: `main` `20c24a2b…` · `orchestrator` `bb603d9a…` ·
`evidence-index` `95fc8163…`.

**The append-only discipline holds perfectly inside each fork and provides nothing across them.**
J.1's rule — *"state changes by appending, never by mutating"* — is satisfied by every copy. What
no rule addresses is that the file is replicated per-branch, so appending is a **branch-local**
operation and two actors appending different records to the same logical ledger produce two
ledgers, both valid, neither complete.

**The canonical ref carries the least information.** `main` holds **2 of the 10** human approvals
this laboratory has obtained. An actor that rehydrates on `main` and reads the queue — the
correct, documented thing to do — will conclude that `SCIAB`, `XPORT`, `P5DOMAIN`, `SUNSET-DEC3`
and `HA-1…HA-4` were never approved. **Four of those approvals are the authority under which
canonical commits already on `main` were executed.**

The one mitigation that exists is real and worth naming: `main` is a **byte-exact prefix** of
both divergent copies, so the forks are additive rather than contradictory, and nothing has been
rewritten. Whether that makes them reconcilable, and by whom, is not decided here.

### F-7 · A canonical precondition on `main` is stale, and the decision superseding it is on a branch

`framework/protocols/controlled_benchmark_ab.md` is **on `main`**. Its precondition row P-3, read
verbatim this session:

> `P-3 | Scientist capabilities VERIFIED at L2 … | **all UNVERIFIED**; L2 **SUSPENDED** by the
> C-9 hold (operator, 2026-08-17) — this protocol does not lift it`

Measured against the records that supersede it:

| Fact | Value | Where it lives | On `main`? |
|---|---|---|---|
| *"**L2 is no longer suspended.**"* | operator decision, 2026-08-18 | `DEC-20260818-007-LAB-REACTIVATION.md` | 🔴 **NO** — `evidence-index` and `p51c9-rebased-onto-c89c2217` only |
| *"§1 · L2 TABLE RATIFIED. 3 VERIFIED promoted — `O4` · `S2` · `S4`"* | same decision | same file | 🔴 **NO** |
| The three verified rows | `O4` lease acquire/renew/observe (orchestrator) · `S2` scientist worktree confinement (scientist-c) · `S4` scientist capability per plan (scientist-c) | `runtime/L2-OUTCOMES.md` | 🔴 **NO** — branch `orchestrator` only |

🔴 **Both of P-3's clauses are false as of 2026-08-18, and P-3 is canonical.** L2 is not
suspended, and capabilities are not all unverified — **3 of 12 attempted were promoted, two of
them Scientist rows.**

**And P-3's conclusion may nevertheless survive, on different grounds.** This is stated because
overturning the premise does not automatically overturn the finding, and the honest reading is
narrower than either extreme:

- P-3 names **four minimum** Scientist capabilities: full-text read producing a receipt; work
  manifest with verbatim locators; worktree confinement; Auto Mode actually active. Of those,
  **one — worktree confinement (`S2`) — is verified**, and only for `scientist-c`.
- `scientist-a` and `scientist-b` have **no verified capability of any kind**.
- Body § 8 requires assignment on **verified** capabilities.

So: the ground P-3 stands on is falsified, its headline count is wrong, and the practical
consequence — that a Scientist reading batch is not yet assignable on verified capability — is
still arguable on the unmet minima. **Which of those readings governs is not mine to decide**,
and it is registered in OPEN_QUESTIONS.

The reconciliation defect is independent of that decision: **a canonical file asserts a runtime
precondition, an operator decision four days later reverses it, and the reversal is unreachable
from the canonical ref.** At least two analyses written in this repository today cite P-3's
canonical text as the current state.

---

## BLOCKERS

Structural conditions measured this session that stand between the current system and a reliable
multi-agent laboratory. **Listed, not solved.** Ownership is named where the repository already
names it, and left blank where it does not.

| # | Blocker | Evidence | Owner per repository |
|---|---|---|---|
| **B-1** | 🔴 **No event stream.** 23 J.1 event types, 0 ever emitted, ledger absent on 37 refs. Nothing in the lifecycle can be closed, replayed, or audited from events | F-1 stage 7, F-3.2 | P7 assigns the **design** to Plan (done); the **writer** is authorised to nobody |
| **B-2** | 🔴 **No ref in an address.** No schema requires a ref; a path alone does not resolve. Demonstrated three times in this session at real cost | F-2, F-5, F-7 | the protocol that fixes it (`cross_session_transport.md`) is `PROPOSED` and binds nobody |
| **B-3** | 🔴 **The human-decision record is forked.** 10 approvals, 3 disjoint lineages, `main` carries 2 | F-6 | J.3 names no reconciler |
| **B-4** | 🔴 **Canonical text can be stale with no detector.** A `main` file asserts a runtime precondition reversed four days earlier on another branch | F-7 | — |
| **B-5** | 🔴 **No control-plane validator of any kind.** 0 scripts read an A.1, A.6, B.1, C.2, J.1 or J.3 object. The `P1` L2 row is explicit: *"there is no registry validator… reading 314 lines and counting 30 rows is measurement, not validation"* | S-5 | the L2 record registers `REGISTRY VALIDATOR: MISSING INSTRUMENT` and states building it is **not authorized to anyone** |
| **B-6** | ⚠️ **No delivery.** Identity (`ACTOR_ID`) is solved; routing is not. No actor observes its own `SESSION_REF`; `actors.yaml` has never existed; H.1 gives routing to an actor that cannot perform it | F-2 row 4 | unresolved and explicitly named as such in `cross_session_transport.md` § 9 |
| **B-7** | ⚠️ **No ACK, therefore no failure detection.** No `TASK_ACK` record exists for any task; `HEARTBEAT` has never run; `P4`'s DOWN timeout has never been exercised | F-1 stage 2 | B.3; P3/P4, both PROVISIONAL |
| **B-8** | ⚠️ **Review closure at 8 of 40.** C.2 makes `AUTHOR_RESPONSE` mandatory and silence non-acceptance | F-1 stage 5 | the author of each reviewed object |
| **B-9** | ⚠️ **The learning loop has a raw archive and nothing downstream.** 72 records, no index, no active lessons, no autonomy ledger, no retrospective cadence (`N` is `UNASSIGNED` and G.2 bars Mirror from setting it alone) | F-3.3 | E.2 durability → Plan; epistemic curation → Mirror; `N` → **unassigned by the annexes** |
| **B-10** | ⚠️ **No `OPERATOR_DAILY_BRIEF`.** § 10.4 requires it at least once per working day; it is the surface on which `PENDING HUMAN DECISIONS` is exposed. Absent on 37 refs | S-3 | body § 8 → Orchestrator |
| **B-11** | 🔴 **The role contracts are non-binding, and one cannot be repaired by its own actor.** `DEC-20260822`: `ACTIVATION_NOT_CONFIRMED`. The only hostile review of the four returned CHANGES_REQUIRED on three; `roles/mirror.md` received **no verdict** under the self-review prohibition | `DEC-20260822`; `REV-ROLES-MIRROR-001` | operator (H.1) |

**B-1 through B-4 interlock.** Without events (B-1) there is no closure; without refs in
addresses (B-2) durable state is not reachable; the queue fork (B-3) and the stale canonical
precondition (B-4) are both direct consequences of B-2 operating on replicated files. **They are
one problem observed at four points, not four problems** — and this record does not propose which
of them, if any, is the right place to intervene.

---

## HUMAN_GATE_MAP

Every current human intervention point measured this session, classified as the dispatch
requires. **Classification is a measurement of *why* the human is needed, not a plan to remove
anyone.**

### G-A · UNAVOIDABLE STRATEGIC DECISIONS — structural; would remain in a fully built system

| # | Intervention | Why it is not delegable | Source |
|---|---|---|---|
| **A-1** | **Scientific priority and scope** — which studies, in what order | *Strategia complessiva → Operatore.* Orchestrator orders work **within** an authorised scope; it does not set the scope | H.1 |
| **A-2** | **Governance changes, MAJOR approval, spend** | *Spese / MAJOR approval / governance → Operatore.* `DEFAULT_EXTERNAL_SPEND = 0` is fail-closed | H.1; J.4 |
| **A-3** | **Persistent scientific disagreement** | Floor `R3 TRIADIC`, derogable only upward; forced consensus is an error and `DISAGREEMENT_UNRESOLVED` is a legitimate outcome | C.1; body § 27 |
| **A-4** | **Public push** | The release gate is mechanical and passes today (`BLOCKS: 0`); reading `git diff origin/main..main --stat` before publishing is *"the one judgement no gate makes"* | root `CLAUDE.md`; `materialization_log.md` |
| **A-5** | **Adjudication where the adjudicator is the author** | C.3's `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR` has no solution inside a 4-role lab when H.1's adjudicator authored the object. Already realised at least once | C.3; H.1 |
| **A-6** | **Anything therapeutic** | Not medical advice; supports discussion with a treating clinical team, never substitutes for one | root `CLAUDE.md` |

### G-B · TEMPORARY INFRASTRUCTURE GAPS — one-time unblocking acts, not recurring costs

| # | Intervention | What makes it temporary | Source |
|---|---|---|---|
| **B-a** | **Role contract activation** | `DEC-20260822` consequence 3: *"A new, explicit activation act is required"* — and it *"does not perform it, does not schedule it, and does not specify its form."* Once performed, it is not performed again | `DEC-20260822` |
| **B-b** | **Authorising an event-ledger writer** | P7 chose the design; only the writer and validator are owed. `M4` is `BLOCKED` for want of it | P7; L2 `M4` |
| **B-c** | **Authorising a control-plane validator** | The L2 record registers `REGISTRY VALIDATOR: MISSING INSTRUMENT` and states building it *"is not authorized to anyone"* and *"needs a separate authorization"* | L2 `P1` |
| **B-d** | **Ruling on `scientist_reading_modes.md`'s status** | Its three activation clauses all measure SATISFIED while its status line still reads `PROPOSED`. A `STATE_DETERMINATION`, like `DEC-20260822` | `scientist_reading_modes.md`; `DEC-20260822` |
| **B-e** | **Ruling on P-3 after F-7** | Its premise is falsified; its conclusion may survive on the unmet minima. One ruling settles it | F-7 |
| **B-f** | **`scientist-c` ACTOR_ID confirmation** | `PROPOSED — confirmed at its own registration`; fixed once | `roles/scientist.md`; I.2 step 7 |
| **B-g** | **Setting `MIRROR_RETROSPECTIVE` cadence `N`** | `UNASSIGNED` by the annexes to anyone; G.2 bars Mirror from setting it alone; carried unresolved since `RES-20260816-GOV311-001` (`ESC-3`) | G.3; P7 tail note |
| **B-h** | **Reopening a crashed or closed session's UI** | Body § 4 lists it as human-required *"solo per riaprire la UI"*; a runtime property, not a governance one | body § 4 |

### G-C · AUTOMATABLE COORDINATION STEPS — currently human, mechanical in nature

**Measured claim, and its limit:** each row below is coordination a machine could in principle
perform. **Not one of them can be automated today**, because each depends on B-1 or B-2. Listing
them is a measurement of where human effort currently goes, **not a proposal to automate any of
them** — and the instrument each would need is authorised to nobody.

| # | Step currently done by a human | Mechanical in nature because | Depends on |
|---|---|---|---|
| **C-1** | **Being the transport between actors** — relaying handoffs, review requests and completions between sessions | B.1 already defines the envelope; § 21 already says *"messaggi = pointer, stato durevole decide"* | B-6, B-2 |
| **C-2** | **Reconciling the forked approval queue** | The forks are additive and `main` is a byte-exact prefix of both; the reconciliation is a set union over an append-only file | B-3 |
| **C-3** | **Finding which ref carries an artifact** | Performed three times manually in this session; a 37-ref sweep is a loop | B-2 |
| **C-4** | **Noticing that a canonical statement went stale** | Cross-ref comparison of a stated precondition against later decision records | B-2, B-4 |
| **C-5** | **Noticing an unanswered review** | 40 `REV-*` against 8 `AUTHOR-RESPONSE-*` is a join on two file sets | B-5 |
| **C-6** | **Detecting a dead or absent actor** | `HEARTBEAT` + 3-miss DOWN is fully specified in P4 and has never run | B-7 |
| **C-7** | **Assembling the `OPERATOR_DAILY_BRIEF`** | § 10.4 enumerates its contents exactly; all inputs are durable files | B-10, B-1 |
| **C-8** | **Detecting a duplicated claim on one task** | A.3's uniqueness is *"by organizational construction"*; the detection is a scan for two claims on one `TASK_ID + GENERATION` | B-5 |
| **C-9** | **Watching the lease window between turns** | The lease record itself states it: closing this *"needs something that runs when no actor is running"* | B-1 |

### G-D · The accounting

```
UNAVOIDABLE STRATEGIC          6   recur per batch or per decision — A-1, A-2, A-3, A-4 are the recurring core
TEMPORARY INFRASTRUCTURE       8   one-time acts; B-a … B-g are unblocking decisions, B-h is a runtime chore
AUTOMATABLE COORDINATION       9   mechanical in nature; 9 of 9 blocked today on B-1 or B-2
```

🔴 **The honest reading of that arithmetic.** The dispatch asks for the minimum requirements for
a reliable laboratory. What the map shows is that human effort today is dominated not by
strategy but by **transport and reconciliation** — nine mechanical steps, every one of which is
blocked on the same two absences. The six strategic gates are genuinely irreducible and are not
where the cost is. **This record does not say what to build, and does not recommend that anything
be built.**

---

## LAB_OPERATING_MODEL_OBSERVATION

`Scientist → Plan → Mirror → Orchestrator`, as **observed**, not as designed. Nothing here is a
target state.

### M-1 · The flow, with what actually moves at each edge

```
                      ┌─────────── OPERATOR ───────────┐
                      │  scope · approval · adjudication│
                      └───────┬──────────────▲──────────┘
                              │              │
                    dispatch  │              │  HUMAN_REQUIRED (J.3 queue — FORKED, F-6)
                    direct to │              │  DAILY_BRIEF  ✗ absent on 37 refs
                    an actor  │              │
                              ▼              │
   ┌──────────┐   TASK_ASSIGNMENT ✗   ┌─────────────┐
   │ SCIENTIST│ ◀──── never issued ───│ORCHESTRATOR │  lease: 0 ACTIVE
   │  a  b  c │                       │             │  0 task records authored
   └────┬─────┘                       └──────▲──────┘  0 checkpoints
        │ 0 task records                     │
        │ 0 checkpoints                      │ ✗ no return edge that closes anything
        │ 0 readings under this governance   │
        ▼                                    │
   ┌──────────┐   HANDOFF (15 artifacts,  ┌──┴──────┐
   │   PLAN   │───  5 shapes, no schema)──▶│ MIRROR  │
   │evidence- │                            │         │
   │  index   │◀── REVIEW verdict ─────────│ 40 REV  │
   └────┬─────┘    AUTHOR_RESPONSE ────────▶│  8 resp │
        │           closes it (C.2)         └────┬────┘
        │ 5 tasks · 19 checkpoints               │ 8 checkpoints · 34 learning records
        │ INTEGRATION_CANDIDATE + manifest       │ primary surface = EVENT LEDGER ✗ ABSENT
        ▼                                        ▼
   CANDIDATE_CONTENT_HASH ✅ mechanized     ✗ no autonomy ledger, no review yield,
   BASE_HEAD ✅ bound                          no retrospective cadence (N unassigned)
```

### M-2 · Where information flows

| Edge | Carrier | Measured state |
|---|---|---|
| **Plan → Mirror** | `HANDOFF-*-MIRROR` artifacts under `governance/candidates/` | ✅ **the one edge that demonstrably works.** 6 handoff artifacts, 40 reviews produced, verdicts rendered, findings transmitted against real objects |
| **Mirror → Plan** | `REV-*` verdict + author's response | ⚠️ works when it happens: **8 responses against 40 reviews** |
| **Plan → canonical** | `INTEGRATION_CANDIDATE` + manifest + hash | ✅ **the strongest chain in the system.** Hash deterministic and independently reproducible; approval binds to `hash + BASE_HEAD`; Gate 5 requires the exact hash |
| **Operator → any actor** | direct dispatch | ✅ works — and it is the § 10.2 `OPERATOR_OVERRIDE` route, which the governance marks **exceptional**, not ordinary. `XPORT-ROUTING-001` records itself as `ORIGIN: OPERATOR` for exactly this reason |
| **Actor → Operator** | J.3 queue | ⚠️ works per-branch; **forked across branches (F-6)**; the `DAILY_BRIEF` surface that would expose it is absent |

### M-3 · Where information stops

| # | Stop | Measurement |
|---|---|---|
| **S-i** | 🔴 **At the Orchestrator, in both directions.** H.1 gives it task authority, priority, Ladder level, reviewer choice, challenge adjudication, `HUMAN_REQUIRED` classification and the canonical batch | **0 task records authored · 0 checkpoints · 0 lease ACTIVE · 0 `TASK_ASSIGNMENT` ever issued.** The node that routes has no inbound or outbound edge that closes |
| **S-ii** | 🔴 **At the Scientist tier entirely.** Three actors defined, three worktrees present | **0 task records · 0 checkpoints · 0 readings under this governance.** The execution plane has never executed |
| **S-iii** | 🔴 **At every closure.** No event ledger means no `CLOSES_EVENT_ID` | 5 of 7 lifecycle stages have no closing instrument at all (F-1) |
| **S-iv** | 🔴 **At the branch boundary.** Artifacts stop at the ref they were written on | F-5 (a discharged duty), F-6 (a forked queue), F-7 (a stale canonical precondition), S-4 (four analyses, four branches) |
| **S-v** | 🔴 **At Mirror's input.** G.3 designates the consolidated event ledger as Mirror's primary analysis surface | Absent on 37 refs. Mirror reviews **objects** ably; it cannot analyse the **laboratory** from the surface the governance gives it |

### M-4 · Where human intervention is currently required

Superimposing G-A/B/C on the model: the operator currently occupies **three distinct positions
at once**, and only the first is by design.

```
1  DECISION MAKER   ← by design (H.1). 6 strategic gates, irreducible.
2  TRANSPORT        ← by absence. Every inter-actor edge that is not a git branch
                       runs through a human, because B-6 (routing) is unresolved.
3  RECONCILER       ← by absence. The union of what was decided exists only in a
                       human's reading across ≥3 branch-local copies (F-6, F-5, F-7).
```

🔴 **Positions 2 and 3 are not governance roles. No annex allocates them to anyone**, which is
precisely why they fall to the only actor present at every boundary. That is an observation about
the current system; **what to do about it is not decided, proposed or implied here.**

### M-5 · What the model shows working

Stated because an accurate observation includes the parts that hold:

- **The candidate chain end-to-end** — hash, base head, manifest, approval binding, Gate 5.
  Deterministic and independently reproducible; it is the one place all five addressing questions
  have answers.
- **The review instrument itself.** C.2 is the strongest object in the lifecycle, and 40 reviews
  exist that use it — including one that returned `CHANGES_REQUIRED` on three of four role
  contracts and correctly declined to rule on the fourth under the self-review prohibition.
- **Fail-closed behaviour under uncertainty.** Measured repeatedly and independently: `plan`
  declining to claim a routing identity it could only infer; `mirror` declining to resolve its own
  contract's activation; `DEC-20260822` resolving a genuinely available reading against the
  convenient one; the lease record refusing to normalise a historical row to make its own check
  pass. **The discipline is real and it is the system's strongest observed property.**
- **The scientific validators.** All five ran to PASS in this session against a 128-receipt
  chained ledger.

---

## OPEN_QUESTIONS

Each is a measured ambiguity. **None is resolved here, and none is assigned.** The disposition
owner column names where the repository already places the decision — it does not place it there.

| # | Question | Raised by | Disposition owner per repository |
|---|---|---|---|
| **Q-1** | Does P-3's conclusion survive the falsification of its premise? L2 is not suspended and 3 capabilities are VERIFIED — but only 1 of P-3's 4 named minima, and only for `scientist-c` | F-7 | operator (H.1: governance / strategy) |
| **Q-2** | Are the three approval-queue lineages reconcilable, and by whom? They are additive and `main` is a byte-exact prefix of both — but J.3 names no reconciler, and appending a union would be a write to a `CONTROL_PLANE_ROOT` by an actor with no allocated authority to do it | F-6 | unallocated |
| **Q-3** | When a canonical file on `main` states a runtime precondition that a later branch-local decision reverses, which governs, and what is supposed to detect the divergence? | F-7 | unallocated |
| **Q-4** | Does `scientist_reading_modes.md` bind? Its three activation clauses all measure SATISFIED; its status line has never been modified; and its entire addressee set is defined by `roles/scientist.md`, which is non-binding | S-3; `DEC-20260822` | operator (a `STATE_DETERMINATION`) |
| **Q-5** | Does `DEC-20260822`'s consequence 5 stand, given that the `AUTHOR_RESPONSE` it calls outstanding exists on `plan-orchsurf-r4-transcription`? | F-5 | operator |
| **Q-6** | Who may authorise an event-ledger writer? P7 assigns Plan the *design* and the design is done; no annex assigns the *writer*. `M4` is BLOCKED for want of it, and `M4` is Mirror's own row | F-3.2 | unallocated |
| **Q-7** | Who may authorise a control-plane validator? The L2 record states building it *"is not authorized to anyone"* and *"needs a separate authorization"* | B-5 | unallocated |
| **Q-8** | What sets `MIRROR_RETROSPECTIVE` cadence `N`? Unassigned by the annexes; G.2 bars Mirror; carried unresolved as `ESC-3` since 2026-08-16 | B-9 | unallocated — flagged `UNASSIGNED_PARAMETER` |
| **Q-9** | Both PROVISIONAL practices (P3.1, P4.1) expire *"after the third scientific batch"* on evidence *"from the event ledger"*. Zero batches have run and the ledger does not exist. E.3 forbids provisional-forever. What happens at the boundary? | F-3.3 | Plan (P3/P4 are Plan-defined); E.3 governs the expiry |
| **Q-10** | Is a fourth analysis on a fifth branch (this record) the right shape for this class of work, given that it reproduces the condition it measures? | S-4 | operator |

---

## NEXT_TRANSITION

**No transition is performed, scheduled, or recommended here.** What follows is a statement of
what the *system's own rules* say must happen before each next state is reachable — measured,
not chosen.

### T-1 · The state this record leaves behind

```
LAB_STATE            BOOTSTRAP (0 ACTIVE leases; CLAUDE.md § 0 antecedents both hold)
ROLE CONTRACTS       PROPOSED ×4 — ACTIVATION_NOT_CONFIRMED (DEC-20260822)
THIS SESSION         BOOTSTRAP_MODE · ACTOR_ID not established · no authority exercised
THIS ARTIFACT        one file, branch orch-control-plane-reconciliation, not merged, not pushed
ROOT CHECKOUT        main @ 788c357, clean, untouched
```

### T-2 · What each next state requires, per the repository's own text

| Candidate next state | What the repository says must precede it | Who holds it |
|---|---|---|
| **Any actor operating under a role contract** | *"A new, explicit activation act is required"* — form unspecified, and its stated condition currently fails on 3 of 4 objects with the 4th unreviewable by its own actor | operator (H.1) |
| **Any `CANONICAL_BATCH_COMMIT`** | GATE 0: `BASE_HEAD` as expected · root clean · governance version correct · **ACTIVE singleton lease** · `ONE_WRITER`. `RES-20260816-GOV311-002`'s lease exemption is scoped to one candidate and is consumed | Orchestrator, under a lease that does not exist |
| **Any task assigned to a Scientist** | Body § 8 — assignment on **verified** capabilities. Blocked pending **Q-1** | operator, then Orchestrator |
| **Mirror analysing the laboratory (as against reviewing an object)** | G.3's primary surface: the consolidated event ledger. Blocked on **Q-6** | unallocated |
| **This record entering canonical history** | It is CONTENT (P5.1), so it would move the `CANDIDATE_CONTENT_HASH` of any candidate re-aligning onto a `main` that carries it. Route: `INTEGRATION_CANDIDATE` (Plan) → hostile review (Mirror) → `HUMAN_APPROVAL` (operator) → `CANONICAL_BATCH_COMMIT` (Orchestrator, under a lease) | four different actors, in that order |

### T-3 · The one thing this record asserts about sequence

**Nothing in T-2 is reachable from where the laboratory currently stands without a human act**,
and the first such act in every row is the operator's. That is a measurement of the current
dependency graph, not a request, a recommendation, or a plan.

---

## VERIFICATION TRAIL

Every command run in this session against the repository at
`<REPO_ROOT>`, `main` @ `788c357`.

| Check | Command | Result |
|---|---|---|
| Lease state | `python3 framework/scripts/lease_state.py --check` | `ACTIVE by derivation: 0`; 2 findings on lease #3 |
| Ref census | `git for-each-ref --format='%(refname)' refs/{heads,remotes,tags} \| wc -l` | 37 · 4 · 5 (51 total) |
| Worktrees | `git worktree list \| wc -l` | 19 entries |
| Positive control for every sweep | per-ref `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` | **21 refs PRESENT** — loop demonstrably iterates |
| Event ledger | per-ref `git ls-tree -r -- ledger/events/` | ABSENT on 37 refs |
| Consolidated view | per-ref `git ls-tree -r -- ledger/consolidated/` | ABSENT on 37 refs |
| `LEARNING_INDEX` / `active_lessons/` | per-ref `git ls-tree \| grep` | ABSENT on 37 refs |
| `DAILY_BRIEF` / autonomy ledger | per-ref `git ls-tree \| grep -i` | ABSENT on 37 refs |
| `actors.yaml` | `git log --all -- framework/state/actors.yaml` | empty — never existed |
| Task records | per-ref union `git ls-tree -r -- ledger/tasks/` | 5, all `plan/` |
| Checkpoints | per-ref union `git ls-tree -r -- ledger/checkpoints/` | 27 — 19 `plan`, 8 `mirror` |
| Reviews / responses | per-ref union `git ls-tree -r -- reviews/` | 73 paths — 40 `REV-*`, 8 `AUTHOR-RESPONSE-*` |
| Learning records | per-ref union `git ls-tree -r -- learning/` | 72 — 34 mirror, 24 plan, 14 orchestrator |
| Approval union | per-ref `grep -oE '"APPROVAL_ID"[[:space:]]*:[[:space:]]*"[^"]*"'` | 10 in union; 0 refs carry it |
| Queue prefix property | `head -n 6 <copy> \| cmp - <main copy>` | `main` is a **byte-exact prefix** of both divergent copies |
| Queue blob distinctness | `git rev-parse <ref>:…jsonl` | `20c24a2b…` · `bb603d9a…` · `95fc8163…` |
| L2 outcomes | `git show orchestrator:runtime/L2-OUTCOMES.md` | 3 VERIFIED of 12 — `O4`, `S2`, `S4` |
| L2 hold lifted | `git show evidence-index:governance/candidates/DEC-20260818-007-LAB-REACTIVATION.md` | *"L2 is no longer suspended."* · *"§1 · L2 TABLE RATIFIED"* |
| P-3 as canonical | `git show main:framework/protocols/controlled_benchmark_ab.md \| grep P-3` | *"all UNVERIFIED; L2 SUSPENDED"* — stale |
| ROLES author response | per-ref `git rev-parse …AUTHOR-RESPONSE-ROLES-MIRROR-001.md` | present on `plan-orchsurf-r4-transcription` only, commit `de0ae4e` |
| Control-plane validators | `git grep -l -E 'TASK_ASSIGNMENT\|TASK_CLAIM\|CHECKPOINT_ID\|REVIEW_ID\|EVENT_ID\|APPROVAL_ID' main -- '*.py'` | 22 files, all unrelated scientific-pipeline hits — **0 control-plane validators** |
| Scientific validators | `legend_lint` · `fulltext_receipts verify` · `growth_anchors check` · `public_release_gate` · `governance_fingerprint compose --all` | PASS · OK 128 chained · PASS · BLOCKS 0 · 4 fingerprints |

---

**Recorded by:** a session in `BOOTSTRAP_MODE`, no `ACTOR_ID`, no lease, no authority claimed.
**This is not a `WORK_COMMIT` under a role contract and not a `CANONICAL_BATCH_COMMIT`.** It is
one analysis artifact on its own branch, touching one new path under `learning/orchestrator/`
and nothing else.

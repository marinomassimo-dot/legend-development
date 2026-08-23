---
artifact: SURFACE MAP — queue / closure loop. What LEGEND already has, measured, before anything is designed
record_id: PLAN-SURFACE-MAP-QUEUE-CLOSURE-001
dispatch_id: PLAN-SURFACE-MAP-QUEUE-CLOSURE-001
task_id: PLAN_SURFACE_MAP_QUEUE_CLOSURE_v1
author: plan
authored_on: 2026-08-23
dispatcher: operator
governance_version: 3.1.1 (read, not exercised)
mode: ANALYSIS_ONLY

STATUS: READ_ONLY_SURFACE_MAP
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none

classification:
  - SURFACE MAP AND MEASUREMENT
  - NOT GOVERNANCE
  - NOT A PROTOCOL
  - NOT A DECISION
  - NOT A CANDIDATE — no CAND was opened, per the dispatch's own prohibition
  - NOT A STATE-MACHINE AMENDMENT
  - NOT EXECUTION AUTHORIZATION
  - NOT AN SLR — Annex E.6 governs `SLR-*`; it does not govern this, and this file is
    deliberately not named `SLR-` so the two are not conflated

domain: >
  CONTENT. `CONTROL_PLANE_ROOTS` (plan_defined_parameters.md § P5.1) are exhaustively
  `governance/candidates/`, `ledger/`, `reviews/`. `learning/` is CONTENT by explicit intent,
  stated in that same section. This record therefore moves the CANDIDATE_CONTENT_HASH of any
  future candidate that re-aligns onto this branch, exactly as that declaration requires.

authority_note: >
  `roles/plan.md` is NOT a source of authority for this session.
  `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` (OPTION B — ACTIVATION_NOT_CONFIRMED, on
  `refs/heads/main` at blob `5cfaed095758`) holds all four role contracts non-binding. Every
  structural act below traces to a named instrument instead: Annex D.1 for the WORK_COMMIT,
  P5.1 for the domain classification, Annex J.1 / § P7 for the ledger subject matter. The
  dispatch grants nothing and was not treated as granting anything.

verdict_transfer: >
  NONE. Every number in this record was executed in this session, in this worktree, against the
  refs named. Seven adjacent analyses exist on other branches (§ 3.7); nothing is carried from
  any of them without independent re-measurement, and where a measurement reproduced, that is
  said explicitly.
---

# SURFACE MAP — QUEUE / CLOSURE LOOP

> **PRESERVE FIRST · MEASURE SECOND · PATCH ONLY WHERE FAILURE IS DEMONSTRATED.**
>
> This record maps and measures. It designs nothing. Where the dispatch's vocabulary and the
> repository's vocabulary disagree, the divergence is recorded and canonical LEGEND is followed.

---

## 1 · ITERATION_IN — RESOLUTION

```
ITERATION_IN:  UNRESOLVED
```

**Fail-closed, per the dispatch's own instruction, and not defaulted to 1.**

Three independent facts establish this, each measured:

**1.1 · No canonical incoming workflow or handoff names this task.** No artifact anywhere in the
52 content refs names `PLAN-SURFACE-MAP-QUEUE-CLOSURE-001`, `PLAN_SURFACE_MAP_QUEUE_CLOSURE_v1`,
or the dispatch id. The dispatch arrived as operator text, not as a durable object with a
predecessor.

**1.2 · `ITERATION` is not a governed field of LEGEND.** It appears in **no** annex, no section of
the body, and no file under `framework/instruction/` or `framework/protocols/`. Measured
repository-wide:

```
git grep -lw 'ITERATION'    over 52 content refs   →   5 ref:path pairs
git grep -lw 'GENERATION'   over 52 content refs   → 787 ref:path pairs   ← positive control
```

All five `ITERATION` hits are frontmatter or header lines of *analysis artifacts written under
operator dispatches that supplied the field*, three of them on other actors' branches:

| ref | path | value |
|---|---|---|
| `mirror` | `reviews/mirror/REV-LEGEND-LAB-ARCHITECTURE-001.md:61` | `1/3` |
| `orch-agent-coordination-protocol` | `learning/orchestrator/LEGEND-AGENT-COORDINATION-PROTOCOL-001.md:57` | `1 of 3` |
| `orch-scientific-pipeline-lifecycle-model` | `learning/orchestrator/SCIENTIFIC_PIPELINE_LIFECYCLE-MODEL-001.md:50` | `1` |
| `plan-orchsurf-r4-transcription` | `learning/plan/SCIENTIST-PIPELINE-EXECUTION-MODEL-001.md:60` | `1/3` |
| `plan-orchsurf-r4-transcription` | `learning/plan/SCIENTIST-PIPELINE-READINESS-001.md:57` | `1/3` |

The lowercase `iteration: N/3` frontmatter key adds two more (`HANDOFF-20260822-ROLE-CONTRACT-REPAIR.md`,
`PREP-20260822-ROLE-CONTRACT-REPAIR.md`, both `2/3`) and the same finding holds: **the field is a
property of the dispatches, reproduced in the artifacts, and has no repository source.** The
repository's own versioning primitives for repeated work are `DIRECTIVE_VERSION` and `GENERATION`
(A.1, A.4, § 22) — neither of which the dispatch invokes and neither of which is an iteration
counter.

**1.3 · The dispatch does not supply it.** No `ITERATION_IN` value appears in the dispatch text.

**Consequence, and its exact boundary.** The dispatch states that `ITERATION_IN_UNRESOLVED` must
*fail closed on any operation that requires an iteration number*, and that this does not prevent
purely observational SURFACE MAP work where the canonical contract permits the distinction. It
does: Annex D.1 makes `WORK_COMMIT` available to *"ogni attore, PROPRIO worktree/branch"* with no
iteration precondition, and nothing in A.1, A.6, C.2, D.1 or J.1 conditions an observation on an
iteration number. **No operation performed in producing this record required one, and none was
invented.** What is barred by this status is any act that would consume a retry budget, close an
iteration, or claim a position in a numbered sequence — and no such act was performed.

---

## 2 · OBSERVATION_SCOPE

Every absence claim in this record is scoped to this population and to **no wider surface**. A
`NOT_FOUND` here is not `NOT_EXIST`: other clones, unpushed worktrees, unreferenced objects and
any non-local remote lie outside it.

```
OBSERVATION_INSTANT   2026-08-23T09:13:40Z … 2026-08-23T09:26:13Z (UTC, runtime clock)
ACTING_WORKTREE       .claude/worktrees/evidence-index
BRANCH                plan-orchsurf-r4-transcription
MEASURED_HEAD         b72af2f25d42c3cafb781d42b66ef3a1761cdb66
TREE_AT_OPEN          5 untracked paths under learning/plan/ (§ 2.4) — 0 modified, 0 staged
CANONICAL main        788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5   (observed, NOT moved)
MERGE_BASE(HEAD,main) 04693e683a254ff0a6d0619fba47103a0fb7d122
LINT                  PASS (1 INFO: MISSING_WIKILINK, CLAIM 010, pre-existing)
RECEIPTS              OK — 128 chained receipts, tail anchored in the state manifest
LEASE DERIVATION      ACTIVE by derivation: 0   (framework/scripts/lease_state.py --check)
```

### 2.1 · The supplied reference point vs the measured HEAD — both recorded

The dispatch supplies `measured starting commit: b14a0d1`. Verified rather than assumed:

```
b14a0d1466962aa79d1bbd0065a0d1141f4a0eab   "Apply ADD-002 authorized ORCHSURF transcription"
                                            2026-08-22 00:15:50 +0200
git merge-base --is-ancestor b14a0d1 HEAD  →  TRUE
```

🔴 **`b14a0d1` is an ancestor of HEAD, not HEAD.** Seven commits sit between them, all on this
branch, all dated 2026-08-22 between 16:29 and 19:42. **The supplied reference point is 7 commits
stale**, and this record is measured at `b72af2f`, not at `b14a0d1`. Both are stated because the
dispatch requires both, and because the repository's own `learned_gates_registry.md` carries the
gate this exact situation triggers — `MEASURED_INSTRUCTION_IS_NOT_A_VERIFIED_ONE`: *"a stale
number is an assertion and invites checking; a stale dispatch is a decision and invites
obedience."* Three supplied measurements were re-derived rather than inherited: the commit
(stale), the J.1 type count (**reproduced — 23**, § 4.1), and the emission count (**reproduced —
0**, § 4.2).

### 2.2 · Ref population — the exact denominator of every negative

```
TOTAL refs                          57
  refs/heads                        43
  refs/remotes                       4   (origin/HEAD, origin/main, origin/harden-…, local/main)
  refs/tags                          5   (4 × snapshot/*, 1 × handoff/C-2/*)
  ─────────────────────────────────────
  CONTENT REFS (the denominator)    52
  ─────────────────────────────────────
  excluded as non-content            5   (4 × refs/codex/turn-diffs/*, refs/stash)
WORKTREES                           25   (git worktree list; 15 marked prunable)
DISTINCT BLOBS hashed for § 3.6   1122
```

The four sibling analyses of 2026-08-22 swept **49** refs (40 heads · 5 tags · 4 remotes). The
head population has grown by 3 since. Every negative below is re-run at **52**, not inherited at
49.

### 2.3 · 🔴 Instrument discipline — one class of silent false negative was hit and corrected

**zsh does not word-split unquoted parameters.** A first pass wrote
`for r in $REFLIST` and `git grep … $REFLIST`; the whole newline-joined list was passed as **one
word**, git returned `fatal: Needed a single revision` or an empty result, and every row printed
`ABSENT` / `0`. The behaviour was isolated and confirmed:

```
X="a b c";  for w in $X    → one word:   [a b c]
            for w in ${=X} → three words: [a] [b] [c]
```

**Every sweep in this record was re-run with `${=…}` or a `while IFS= read -r` loop, and every
negative was run with a positive control in the same invocation.** The controls are printed
beside their negatives throughout. This is the fourth recorded instance in this analysis chain of
a query returning a clean, wrong answer; it is not treated as incidental.

### 2.4 · What this checkout carries that is not committed — reported, not touched

Five untracked paths were present at session open and are **left exactly as found**:

```
?? learning/plan/FIRST-SCIENTIST-PILOT-READINESS-AUDIT-001.md
?? learning/plan/FIRST-WWOX-PAPER-PILOT-DESIGN-001.md
?? learning/plan/SCIENTIST-ACTIVATION-READINESS-001.md
?? learning/plan/SCIENTIST-FIRST-PILOT-EXECUTION-CONTRACT-001.md
?? learning/plan/SCIENTIST-FIRST-REAL-PAPER-PILOT-001.md
```

All five are `author: plan`, `dispatcher: operator`, `authored_on: 2026-08-22`, and none carries
an `iteration:` field. **They are substantive analytical output that never reached a
`WORK_COMMIT`**, which makes them a live, unplanned instance of the dispatch's own RECOVERY POINT
B (§ 11.2) — durable-ish producer output with no closure. They are **not committed by this
record**: committing another session's unfinished work is precisely the failure mode this
laboratory has already suffered once, and the WORK_COMMIT that closes this dispatch stages one
explicit path.

### 2.5 · Surfaces inspected, with the blob measured

**A · PLAN SURFACE** — `plan-orchsurf-r4-transcription` @ `b72af2f`

| path | blob @ HEAD |
|---|---|
| `governance/GOVERNANCE_v3.1.1.md` | `ee4cabd37fd6` |
| `governance/annex_a_task_contract.md` | `c5564ef07094` |
| `governance/annex_b_message_protocol.md` | `576c91a5fa16` |
| `governance/annex_c_review_protocol.md` | `7d433191ac2c` |
| `governance/annex_h_authority_matrix.md` | `312ac4541706` |
| `governance/annex_i_bootstrap_deployment.md` | `8bcd455a3f1f` |
| **`governance/annex_j_runtime_control_plane.md`** | **`bad0c1a2d4b8`** |
| **`governance/plan_defined_parameters.md`** (carries § P7) | **`e1f9e1ec6fce`** |
| `roles/plan.md` · `roles/orchestrator.md` · `roles/mirror.md` · `roles/scientist.md` | `7e1e04cb537e` · `24663eec772e` · `6e515059af31` · `fd30134dc8eb` |
| `runtime/orchestrator_lease.md` | `c34f48668d07` |
| `framework/scripts/lease_state.py` | `d826812e2796` |
| `framework/protocols/cross_session_transport.md` | `49b7b63a05dc` |
| `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` | `20c24a2ba478` |
| `governance/decisions/DEC-20260820-ORCH-SESSION-HOME.md` | `a54184fd930c` |
| `governance/decisions/DEC-20260821-ORCHSURF-D2-TRANSCRIPTION-ROUTING.md` | `42d26de34291` |

**B–E · OFF-HEAD SURFACES** — read by `git show <ref>:<path>`, without merging, without any
cross-worktree write

| ref | path | blob |
|---|---|---|
| `main` | `governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` | `5cfaed095758` |
| `mirror` | `reviews/mirror/REV-ROLES-MIRROR-001.md` | `daec4e8a91df` |
| `mirror` | `learning/mirror/HANDOFF-ROLE-CONTRACTS-001.md` | `1fba1f1e1fc0` |
| `orchestrator` | `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` | `bb603d9a270b` |
| `evidence-index` | `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` | `95fc81639014` |
| `orchestrator` | `runtime/agent_card_registry.md` | `cd94b5725c18` |
| `orchestrator` | `runtime/L2-OUTCOMES.md` | `c760459b225a` |
| `orch-autonomous-dispatch-loop` | `learning/orchestrator/AUTONOMOUS-DISPATCH-LOOP-MODEL-001.md` | `8bb7a8a22ba5` |
| `orch-control-plane-reconciliation` | `learning/orchestrator/CONTROL-PLANE-RECONCILIATION-ANALYSIS-001.md` | read |

### 2.6 · SURFACE_COMPLETENESS

```
A  PLAN SURFACE          MEASURED
B  ORCHESTRATOR SURFACE  MEASURED — J.1, P7, governance/decisions/, roles/orchestrator.md,
                         the approval queue on all three of its divergent lineages
C  LEASE SURFACE         MEASURED — record, derivation script, and the derivation executed
D  ACTOR CONTRACTS       MEASURED — all four, plus the operator decision governing their status
E  "HANDOFF v2.1"        🔴 SURFACE ABSENT — see § 6.4. This is a measured non-existence over
                         52 refs with a working positive control, not an unmeasured surface
```

**The map is therefore reported as complete for A–D and as `SURFACE_ABSENT` for E**, which is a
different verdict from `SURFACE_INCOMPLETE`: the surface was searched for exhaustively and is not
there, rather than left unsearched.

---

## 3 · SURFACE MAP

### 3.1 · The event / activity ledger — Annex J.1

| | |
|---|---|
| **Canonical purpose** | append-only activity ledger; *"state changes by appending events, never by mutating"*; primary analysis surface for Mirror (G.3, `roles/mirror.md`) |
| **Path** | `governance/annex_j_runtime_control_plane.md` § J.1 |
| **Ref / commit** | `plan-orchsurf-r4-transcription` @ `b72af2f`, blob `bad0c1a2d4b8`; **byte-identical on all 27 refs that carry the file** |
| **Writer / owner** | the annex text: `materialized_by: plan`, `status: FROZEN`, `normative: yes`. The *ledger's* writer is delegated, not fixed here — see § 5 |
| **Readers** | Mirror (primary), Plan (consolidation), any actor |
| **Authoritative or derived** | 🔴 **NEITHER, by its own words.** J.1: *"lo stato repo resta sovrano — in conflitto vince il repo; il ledger è audit e analisi, mai seconda fonte di verità"* |
| **Relation** | J.0 caps its vocabulary; J.2 requires an event per actor/lab transition; J.3 adopts its append discipline; A.5/A.6/A.7 name it for every task transition; G.3 makes it the retrospective's substrate; § P7 supplies its one-writer design |
| **Materialized instance** | 🔴 **NONE** — § 4.2 |

### 3.2 · § P7 — the one-writer design

| | |
|---|---|
| **Canonical purpose** | supplies the choice J.1 delegates: *"Design one-writer (decisione di Plan): (a) … oppure (b) …"* |
| **Path** | `governance/plan_defined_parameters.md` § P7 |
| **Ref / commit** | HEAD blob `e1f9e1ec6fce`; **§ P7's own text is byte-identical (`5ef9956ab8e5c039`) on all 27 refs carrying the file** — 3 whole-file blobs exist, and none of them differs inside P7 |
| **Writer / owner** | `authored_by: plan`, under J.1's delegation and H.1 |
| **Decision recorded** | **(a)** — per-actor append-only file in each actor's own worktree, consolidated by Plan into a derived canonical view |
| **Declared shape** | `FORMAT: JSON Lines, one event per line, append-only` · `PATH: ledger/events/<ACTOR_ID>.jsonl` (actor's own worktree) · `VIEW: ledger/consolidated/` — derived, rebuilt by replay, never hand-edited |
| **Its own status of build** | 🔴 stated in the section itself: *"Tracked as a debt; **not yet built**."* |
| **🔴 Its normative standing** | `status: PROPOSED — normative once Mirror hostile review passes and the operator approves`. `git log --all -S'status: NORMATIVE' -- governance/plan_defined_parameters.md` → **empty**. See § 3.8 |

**Why (a) and not (b), preserved verbatim in substance:** option (b) derives events from commits
plus ACKed messages, and five of J.1's own minimum types leave neither — `CHECKPOINT_WRITTEN`,
`ACTOR_DOWN`, `LEASE_STALE`, `HUMAN_REQUIRED_OPENED`, `RESUMED_FROM_MILESTONE`. Option (a)
satisfies one-writer by construction: each file has exactly one writer, its own actor, and no
shared multi-writer file exists anywhere.

> **The dispatch instructs: do not choose between single-writer and per-actor-writer from the
> advisory; determine what J.1 already establishes.** Determined: **J.1 establishes the
> *requirement* (append-only, no shared multi-writer file) and explicitly delegates the *topology*
> to Plan; Plan has recorded (a). Nothing in this record reopens that choice.**

### 3.3 · The lease surface — Annex I.3

| | |
|---|---|
| **Canonical purpose** | singleton-with-expiry for `ACTIVE_ORCHESTRATOR`; the GATE 0 precondition (D.3, body § 12) |
| **Normative path** | `governance/annex_i_bootstrap_deployment.md` § I.3, blob `8bcd455a3f1f` |
| **Record path** | `runtime/orchestrator_lease.md`, blob `c34f48668d07` — **present on 22 of 52 content refs** |
| **Derivation** | `framework/scripts/lease_state.py`, blob `d826812e2796` |
| **Writer / owner** | 🔴 declared in the record's own frontmatter: *"`writer: orchestrator ONLY — one writer, from the orchestrator worktree`"* |
| **Readers** | *"every actor, from every checkout, via git"* |
| **Authoritative or derived** | 🔴 **the stored `STATUS:` field is explicitly NOT authoritative.** State is derived from `RELEASED_AT` · `EXPIRES_AT` · the clock, and the record says so in bold |
| **Relation** | GATE 0 (D.3 / § 12) consumes it; § 48 makes violating its singleton a stop condition; **§ P5.1 places it INSIDE the candidate content domain** (entry 495 of 532 at the XPORT binding) while it is a *mutable* control-plane record |

**Derivation executed this session, not read:**

```
python3 framework/scripts/lease_state.py --check     @ 2026-08-23T09:16:27Z

  lease #1  derived=STALE     stored=STALE      expires 2026-08-18T09:40:25Z  released —
  lease #2  derived=RELEASED  stored=RELEASED   expires 2026-08-18T11:13:21Z  released 11:07:12Z
  lease #3  derived=STALE     stored=EXPIRED    expires 2026-08-18T13:04:11Z  released —
  lease #4  derived=RELEASED  stored=RELEASED   expires 2026-08-18T14:26:30Z  released 13:29:40Z
  lease #5  derived=RELEASED  stored=RELEASED   expires 2026-08-18T15:03:41Z  released 14:05:20Z

  ACTIVE by derivation: 0
  FINDING lease #3  DISAGREEMENT            stored 'EXPIRED', derived 'STALE'
  FINDING lease #3  EXPIRED_WITHOUT_RENEWAL
```

🔴 `EXPIRED` is **not** in I.3's vocabulary (`ACTIVE | STALE | RELEASED`). A terminal state was
hand-written in a value the governance does not define, and the record deliberately preserves it
rather than normalising the evidence away.

**Also measured:** `main` carries lease rows #1–#5; branch `orchestrator` carries #1–#8. The lag
is structural, not sloppiness — a lease's terminal row is written *after* the batch that lease
authorized, so it can never sit inside that batch. § P5.1 already states this and its consequence:
I.3's `DETECTION` (*"doppio record sulla stessa successione"*) is **weaker than a tracked home
suggests**, because the rows an actor must compare sit on a branch it has to know to read.

### 3.4 · The task surface — Annex A + `ledger/tasks/`

| | |
|---|---|
| **Canonical purpose** | A.1 TASK_ASSIGNMENT (15 fields) · A.2 TASK_ACK · A.3 TASK_CLAIM · A.5 states · A.6 CHECKPOINT · A.7 idempotent resume |
| **Normative path** | `governance/annex_a_task_contract.md`, blob `c5564ef07094` — FROZEN |
| **Instance path** | `ledger/tasks/<ACTOR_ID>/<TASK_ID>.json` |
| **Writer authority** | 🔴 **Orchestrator** — H.1 row 1, *"Task / priorità / riassegnazione / generation"*. Not conditioned on a lease |
| **Readers** | the assignee (via A.2); Plan at reconciliation (A.3 `CLAIM_CONFLICT`) |
| **Authoritative** | yes — durable task state |
| **Measured population** | **5 records, repository-wide over 52 content refs** |

```
ledger/tasks/plan/C9-STATE-MODEL-001.json           OWNER=plan  ACK=yes  CLAIM_BY=plan
ledger/tasks/plan/GOV311-PLAN-REMEDIATION-001.json  OWNER=plan  ACK=yes  CLAIM_BY=plan
ledger/tasks/plan/P5DOMAIN-001.json                 OWNER=plan  ACK=NO   CLAIM_BY=plan
ledger/tasks/plan/SCIENTIST-AB-SPEC-001.json        OWNER=plan  ACK=yes  CLAIM_BY=plan
ledger/tasks/plan/XPORT-ROUTING-001.json            OWNER=plan  ACK=NO   CLAIM_BY=plan
```

🔴 **All five are written by `plan`, about `plan`, under `ledger/tasks/plan/`. Zero counterparty
ACKs exist for any task in the repository.** `SCIENTIST-AB-SPEC-001`'s own `_note` states the
reason plainly: *"Operator-directed work, not a task assigned under H.1. No ACTIVE lease exists
and no Orchestrator issued a Task Contract … This record exists so the work has provenance, not
to assert that a task-assignment authority was exercised."* This reproduces the sibling
measurement of 2026-08-22 exactly.

### 3.5 · The checkpoint surface — A.6 + `ledger/checkpoints/`

| | |
|---|---|
| **Path** | `ledger/checkpoints/<ACTOR_ID>/CHK-<actor>-NNNN.json` |
| **Writer** | the actor itself |
| **Trigger** | every durable milestone; before rotation (§ 36.4); on `AWAITING_APPROVAL` or `PARKED` |
| **Measured** | **450 checkpoint files across 52 content refs; 27 distinct** — `plan` × 19, `mirror` × 8, `orchestrator` × 0, scientists × 0 |
| **Load-bearing field** | `APPLICABLE_GOVERNANCE_FINGERPRINT`. The MAF refusal rule (A.6): rehydration finding an incompatible directive_version, generation **or fingerprint** does **not** resume — it asks Orchestrator |

**This is the single richest durable execution trail LEGEND actually possesses.** `CHK-plan-0019`
carries rehydration verdict, verified state, findings, milestones reached, gates evidenced, and an
explicit `NOT_DONE_DELIBERATELY` block. It is a *snapshot* object, not an event stream — the
distinction that matters for § 4.

### 3.6 · The approval surface — Annex J.3 + `ledger/approvals/`

| | |
|---|---|
| **Canonical purpose** | every `HUMAN_REQUIRED` creates a durable object in the queue — *"mai solo un messaggio"* (body § 4) |
| **Path** | `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` |
| **Declared discipline** | append-only, one JSON object per line, *"following the ledger discipline of J.1: state changes by appending, never by mutating"* (its own `_schema` line) |
| **Writer authority** | 🔴 **NOT DECLARED ANYWHERE.** J.3 names `REQUESTED_BY` and a resolver; it allocates no file writer, and no path-level one-writer rule covers it |
| **Vocabulary** | `PENDING \| APPROVED \| APPROVED_WITH_MODIFICATION \| DENIED \| REVISION_REQUESTED` |

🔴 **MEASURED FORK — three simultaneous lineages of one append-only file.**

```
blob 20c24a2ba478    6 lines   ← main + 24 other refs, INCLUDING this HEAD
blob bb603d9a270b   10 lines   ← refs/heads/orchestrator          (extends the 6-line base)
blob 95fc81639014   14 lines   ← refs/heads/evidence-index,
                                  refs/heads/p51c9-rebased-onto-c89c2217 (extends the same base)
```

Prefix tests executed with `cmp`:

```
head -6  orchestrator(10)  ==  main(6)          →  PREFIX YES
head -6  evidence-index(14) == main(6)          →  PREFIX YES
head -10 evidence-index(14) == orchestrator(10) →  🔴 NOT A PREFIX — the two have FORKED
```

Neither lineage contains the other:

| line | `orchestrator` (10) | `evidence-index` (14) |
|---|---|---|
| 7 | `APR-20260818-SUNSET-DEC3-001` APPROVED | `APR-20260817-HA-1` PENDING |
| 8 | `APR-20260819-SCIAB-001` APPROVED | `APR-20260817-HA-2` PENDING |
| 9 | `APR-20260819-XPORT-001` APPROVED | `APR-20260817-HA-3` PENDING |
| 10 | `APR-20260819-P5DOMAIN-001` APPROVED | `APR-20260817-HA-4` PENDING |
| 11–14 | — | `HA-1` **APPROVED** · `HA-2` **DEFERRED** · `HA-3` **RESOLVED** · `HA-4` **DEFERRED** |

**Two consequences, both measured:**

1. **Four operator approvals — including the three that canonicalized SUNSET-DEC3, SCIAB, XPORT
   and P5DOMAIN — are invisible from `main` and from this HEAD.** `main` carries 6 lines. An actor
   reconstructing approval state from the sovereign ref sees none of them.
2. 🔴 **`DEFERRED` and `RESOLVED` are not in J.3's `STATE` vocabulary.** This is the same
   drift class as the lease record's `EXPIRED` (§ 3.3): a hand-written terminal value in a
   vocabulary the governance does not define, on the surface that gates every MAJOR.

**This is the concrete, already-realised instance of the concurrency failure a queue design would
be built to prevent — and it is on a J.3 surface that § P7's one-writer decision does not cover.**
P7 allocates a writer per actor for `ledger/events/`; nothing allocates one for
`ledger/approvals/`.

### 3.7 · 🔴 Prior art — this question has been analysed seven times, and each answer lives on one ref

| ref | record | overlap |
|---|---|---|
| `orch-autonomous-dispatch-loop` | `AUTONOMOUS-DISPATCH-LOOP-MODEL-001` (934 lines) | SURFACE_MAP · **EVENT_MODEL** · DISPATCH_MODEL · HUMAN_ESCALATION · AUTONOMY_MEASUREMENT |
| `orch-control-plane-reconciliation` | `CONTROL-PLANE-RECONCILIATION-ANALYSIS-001` (745 lines) | control-plane reconciliation · HUMAN_GATE_MAP |
| `orch-agent-coordination-protocol` | `LEGEND-AGENT-COORDINATION-PROTOCOL-001` | 8-stage task lifecycle · object addressing · human gate map |
| `orch-scientific-pipeline-lifecycle-model` | `SCIENTIFIC_PIPELINE_LIFECYCLE-MODEL-001` | 9-state lifecycle vs J.1's 23 types |
| `orch-pipeline-loop-architecture` | `ORCHESTRATOR-SCIENTIFIC-PIPELINE-AND-LOOP-ARCHITECTURE-ANALYSIS-001` | pipeline + loop architecture · automation candidates |
| `orch-lab-director-operating-model` | `LAB-DIRECTOR-OPERATING-MODEL-001` | operating model |
| `orch-autonomous-lab-loop-v2` | `AUTONOMOUS-LAB-LOOP-v2-001` | loop v2 |

**Only `SCIENTIFIC-PIPELINE-PREPARATION-001` reached `main`.** The other seven exist on exactly
one ref each, none of them `main`, and no two of them are visible from the same checkout. **The
subject matter of this dispatch has been analysed to a conclusion seven times and consolidated
zero times** — which is the same cross-ref visibility failure as § 3.6, expressed in analysis
rather than in state.

Their EVENT_MODEL measurement and mine agree where they overlap:

```
sibling (2026-08-22, 49 refs):   events EVER EMITTED as a J.1 event   0 / 10
this record (2026-08-23, 52 refs): J.1 events emitted, any type       0 / 23
```

### 3.8 · 🔴 The normative-standing question that sits under every surface above

`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` (operator, on `main`, blob `5cfaed095758`) decided
**OPTION B — `ACTIVATION_NOT_CONFIRMED`**: the four role contracts remain `PROPOSED` and are
non-binding. Its reasoning turns on the status grammar itself: *"an approval bound to a hash
approves the bytes under that hash; it cannot simultaneously nullify the meaning of one of them."*

**Measured: three further load-bearing artifacts carry the same grammar, and no activation record
exists for any of them.**

| artifact | status line | activation record |
|---|---|---|
| `governance/plan_defined_parameters.md` (**carries § P7, P1, P3, P4, P5**) | `PROPOSED — normative once Mirror hostile review passes and the operator approves` | 🔴 none. `git log --all -S'status: NORMATIVE'` → empty |
| `framework/protocols/cross_session_transport.md` (**carries § 8, the closure conjunction**) | `PROPOSED — binding once Mirror hostile review passes and the operator approves` | conditions **all three satisfied** — see below — line **never updated** |
| `framework/protocols/scientist_reading_modes.md` | `PROPOSED — binding on canonical execution of CAND-20260818-SCIENTIST-AB-SPEC …` | same pattern, already recorded by Plan and by a sibling |

For `cross_session_transport.md` the three conditions are independently evidenced, and each was
verified at source this session:

```
canonical execution   git merge-base --is-ancestor e839db38 main   →  TRUE
                      (content tip of CAND-20260819-XPORT rev 2)
Mirror hostile review REV-XPORT-MIRROR-002 @ 94927355, verdict ACCEPT,
                      bound to hash 81f241f2… base 4454feab
HUMAN_APPROVAL        APR-20260819-XPORT-001 / RES-20260819-XPORT-001, STATE APPROVED,
                      DECIDED_BY operator, 2026-08-19T17:05:17Z
                      🔴 readable ONLY on refs/heads/orchestrator (§ 3.6)
```

Yet the blob is `49b7b63a05dc` on **all 16** refs carrying it, status line unchanged.

> 🔴 **This record does NOT resolve that question, and must not.** `DEC-20260822` scoped itself to
> `roles/` and states it *"adopts no general interpretation"*. Extending it by analogy is exactly
> the governance interpretation Plan is barred from making — and one of the four affected files is
> Plan's own. **The measurement is transmitted; the determination is the operator's under H.1.**
> Its practical weight is stated plainly: **the closure semantics § 6 finds already canonical, and
> the one-writer design § 5 finds already decided, both live in documents whose own status lines
> say they bind nobody.**

---

## 4 · QUESTION 1 — THE EXISTING EVENT MODEL

### 4.1 · The 23 canonical types — re-derived, not inherited

Parsed mechanically from `governance/annex_j_runtime_control_plane.md` § J.1 at HEAD:

```
 1 TASK_ASSIGNED            9 REVIEW_CLOSED           17 LEASE_STALE
 2 TASK_ACKED              10 WORK_COMMIT             18 HUMAN_REQUIRED_OPENED
 3 TASK_CLAIMED            11 CANDIDATE_CREATED       19 APPROVAL_RESOLVED
 4 TASK_COMPLETE           12 BATCH_COMMITTED         20 LEARNING_PROMOTED
 5 TASK_CANCELLED          13 BATCH_ABORTED           21 GOVERNANCE_UPDATED
 6 CHECKPOINT_WRITTEN      14 ACTOR_DOWN              22 DISSENT_OPENED
 7 RESUMED_FROM_MILESTONE  15 ACTOR_ACTIVE            23 CHALLENGE_ADJUDICATED
 8 REVIEW_OPENED           16 LEASE_ACQUIRED
```

**COUNT = 23.** The dispatch's supplied figure reproduces. J.1 calls these *"tipi minimi"* — a
floor, not a closed set.

**Event record shape (J.1, verbatim):**

```
EVENT_ID / timestamp / ACTOR_ID / TASK_ID / EVENT_TYPE / OBJECT / DURABLE_POINTER
CLOSES_EVENT_ID:  (closure events only — reference to the opening event they close)
```

### 4.2 · Emission — measured at three independent angles, each with a positive control

```
ANGLE 1   ledger/events/        over 52 content refs   →   0 files
ANGLE 2   ledger/consolidated/  over 52 content refs   →   0 files
          POSITIVE CONTROL ledger/checkpoints/         → 450 files   ✅ instrument working

ANGLE 3   git grep -l '"EVENT_TYPE"|"EVENT_ID"' × 52   →   0 ref:path
          POSITIVE CONTROL '"CHECKPOINT_ID"'  × 52     → 450 ref:path ✅ instrument working

ANGLE 4   *.jsonl under ledger/ on any of 52 refs      →   1 path, and it is the J.3
                                                            approval queue, not an event file
```

```
EVENTS EMITTED, ALL 23 TYPES, OVER 52 CONTENT REFS   =   0
```

The dispatch's supplied `0` reproduces, at a wider ref population than the report that produced it.

### 4.3 · Concept → canonical type table

Column **Emitted** is `0` for every row and is not repeated per row. **Local classification** uses
the dispatch's four local labels, which are *not* LEGEND vocabulary and are not written into any
governed object.

| Concept | Canonical existing type | Defining path @ `b72af2f` | Authorized writer (authority) | Measured surface for the concept today | Local class | Notes |
|---|---|---|---|---|---|---|
| task definition / creation | **`TASK_ASSIGNED`** | J.1; schema A.1 | **Orchestrator** — H.1 row 1 | `ledger/tasks/plan/*.json` × **5**, all self-written | **PATCH_REQUIRED** (emission only) | Schema is complete and 15 fields deep. What is missing is an emitter, not a concept |
| dispatch | **`TASK_ASSIGNED`** + B.2 `TASK_ASSIGNMENT` message | J.1; B.2; A.1 | Orchestrator | 0 `TASK_ASSIGNMENT` messages recorded anywhere; `XPORT-ROUTING-001`'s `_note` says so explicitly | **PATCH_REQUIRED** | 🔴 **Dispatch and task-creation are ONE canonical concept in LEGEND** (A.1 + B.2), not two. Splitting them would originate a distinction J.1 does not make |
| actor acknowledgement / receipt | **`TASK_ACKED`**, **`TASK_CLAIMED`** | J.1; A.2; A.3; B.3 | ACK: the assignee (A.2). CLAIM: the claimant (A.3) | 3 of 5 records carry `TASK_ACK`, **all self-written**; 5 of 5 carry `TASK_CLAIM`, all `claimed_by == OWNER == plan` | **PATCH_REQUIRED** | 🔴 **`ACK` and `CLAIM` are two distinct canonical acts** (A.3: *"Assigned ≠ claimed"*). The advisory's single "acknowledgement" slot maps onto two |
| actor closure claim | **`TASK_COMPLETE`** | J.1; A.5; B.2 | the owning actor | `MILESTONE_PLAN` status fields inside task records; `STATE` strings; `WORK_COMMIT`s | **PATCH_REQUIRED** (emission only) | The *producer* half of § 6 |
| receiver-side verification of closure | ⚠️ **no single type. The act is `REVIEW_CLOSED` + C.2 `AUTHOR_RESPONSE`, and for handoffs it is XPORT § 8 terms 5–6** | J.1; C.2; `cross_session_transport.md` § 8 | 🔴 **split**: review closure is allocated to the **AUTHOR** (C.2 `AUTHOR_RESPONSE` mandatory), the durable ACK to the **RECIPIENT** (XPORT § 8 term 6) | 54 `REV-*` artifacts vs 8 `AUTHOR-RESPONSE-*` on the sibling's count; § 6 here | **PATCH_REQUIRED** | 🔴 **The separation EXISTS canonically (§ 6.1) but no single event type carries it.** Do not name a new one before § 6 is read |
| blocked condition | ⚠️ **no dedicated type.** A.5 state `BLOCKED`; B.2 message `BLOCKER` | J.1 (absent); A.5; B.2; B.3 | the blocked actor | 0 | **PATCH_REQUIRED** or governance change | 🔴 A *state* and a *message* exist; the **event** does not. Adding one is an amendment to J.1's minimum list |
| human escalation | **`HUMAN_REQUIRED_OPENED`**, **`APPROVAL_RESOLVED`** | J.1; J.3; body § 4 | Orchestrator classifies (H.1); requester writes the queue object | `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` — **3 forked lineages** (§ 3.6) | **PATCH_REQUIRED** | The durable object exists and is used. Only the *event* is missing — and the object itself has a concurrency defect P7 does not cover |
| terminal transitions in this loop | **`TASK_COMPLETE`**, **`TASK_CANCELLED`**, **`BATCH_COMMITTED`**, **`BATCH_ABORTED`**, **`LEASE_ACQUIRED`**, **`LEASE_STALE`**, **`ACTOR_DOWN`**, **`ACTOR_ACTIVE`** | J.1; A.5; D.4; I.3; J.2 | per type | 0 events; the states themselves live in task records, the lease record and git history | **PATCH_REQUIRED** (emission only) | J.2 additionally requires *"Ogni transizione = evento (J.1) + roster durevole"* — and **no roster artifact exists on any of 52 refs** (positive control: `*registry*` returns 5 paths) |

### 4.4 · Two findings that do not sit in one cell

**(a) J.1's vocabulary is a CONTROL-PLANE vocabulary, and this loop is partly scientific work.**
The sibling record found four events with no J.1 type at all — reading start, reading freeze,
analysis complete, handoff — and that reproduces here: `git grep` for a versioned handoff format
returns nothing (§ 6.4), and the receipt ledger records *completed* reads with no start field.
**Building the ledger exactly to specification would leave those four unobservable.** Whether to
extend J.1's minimum list (a governance change), keep two ledgers with a declared join, or treat
reading state as sovereign durable state queried rather than mirrored, is **not decided here**;
J.1's own sovereignty clause supports the third.

**(b) Writers outnumber readers, and a queue is a reader.** Of the ten loop events the sibling
enumerated, eight have a writer the governance names and only three have an observer who is not
the writer. Body § 18 supplies the consequence from the other side: *"Ciò che non è nello stato
durevole non è accaduto."* **An event only its author can see is, for coordination purposes, an
event that did not happen** — and that is the defect this dispatch's subject matter is really
about.

---

## 5 · QUESTION 2 — WRITER SEMANTICS

### 5.1 · What is already canonical

```
J.1 REQUIREMENT   append-only strict; a written event is NEVER updated, not even to link its
                  closure. Linkage lives in the CLOSING event via CLOSES_EVENT_ID.
                  `closed_by` may exist ONLY in the derived/replayed view built by Plan,
                  never in the source ledger.
J.1 CONSTRAINT    "Requisito comune: append-only, nessun file condiviso multi-writer."
J.1 DELEGATION    topology (a) or (b) → Plan
P7 DECISION       (a) per-actor file in the actor's own worktree; Plan consolidates
P7 PATHS          ledger/events/<ACTOR_ID>.jsonl   ·   ledger/consolidated/
BODY § 14         ONE_WRITER_PER_WORKING_DIRECTORY — never two actors writing one directory
D.3 / § 12        GATE 0 asserts ONE_WRITER as a batch precondition
```

**Answers to the dispatch's five sub-questions:**

| question | canonical answer, measured |
|---|---|
| who writes which event types? | **Not allocated per type anywhere.** J.1 gives a shape and a list; H.1 allocates *decisions*, not event emissions. P7 allocates the **file** (one per actor) but not the **type→writer** mapping. The mapping is derivable from H.1 + the annexes for most types (§ 4.3 column 4) and is nowhere written down as such |
| on which surface / ref? | P7: the actor's **own worktree**, i.e. its own branch. Consolidation into `ledger/consolidated/` is Plan's, per P7 and `roles/plan.md` |
| do actor-local event files already exist? | 🔴 **NO — 0 files under `ledger/events/` on all 52 content refs**, positive control 450 |
| does a consolidated view exist or is it specified? | **Specified, not built.** P7 names `ledger/consolidated/`; 0 files on 52 refs. P7 itself says *"Tracked as a debt; not yet built"* |
| how is cross-ref visibility expected to work? | 🔴 **The specification does not say, and the measured behaviour is the failure.** P7's per-actor files live on per-actor branches; the only mechanism named for bringing them together is *"consolidated by Plan"*, which is a human/actor act with no cadence, no trigger and no owner-of-the-trigger. §§ 3.6 and 3.7 measure what that produces today on two other surfaces: a **forked** append-only queue and **seven** unconsolidated analyses |

### 5.2 · The invariant the dispatch asks to test, not impose

> `producer claim ≠ receiver verification`

**LEGEND already has this separation, in four independent places.** It is `ALREADY_PRESENT` as a
principle; what is missing is emission, not the distinction.

```
A.2 / A.3     TASK_ACK (assignee's act)      ≠  TASK_CLAIM (durable, before work starts)
              — and A.3 states it as a rule:  "Assigned ≠ claimed."
B.3           "un messaggio state-changing non ACKato non è mai assunto consegnato"
C.2           the REVIEWER emits the VERDICT; the AUTHOR owes AUTHOR_RESPONSE;
              "il silenzio non è accettazione"
XPORT § 8     HANDOFF ESTABLISHED = 6-term conjunction; sender-side success is term 4 of 6.
              Terms 5 and 6 — "the recipient READ the durable object" and "the recipient
              produced a DURABLE ACK" — are the receiver half, explicitly
KERNEL_SPEC   cited by XPORT § 5 and adopted verbatim:
  (via XPORT)   "EVIDENCE_CLASS_MISMATCH: delivery is not acceptance"
                SENDMESSAGE INVOKED ≠ DELIVERY ACCEPTED ≠ RECIPIENT PROCESSED ≠ HANDOFF ESTABLISHED
```

🔴 **Do not assume append-only implies safe multi-writer behaviour across worktrees — and do not
assume it in the other direction either.** § 3.6 is the measured counter-example: an append-only
file, correctly appended by two writers on two refs, produced **two divergent lineages neither of
which contains the other**, and `main` carries neither. Append-only guarantees no rewriting; it
guarantees nothing about convergence. **P7's option (a) is precisely the construction that avoids
this** — one writer per file — and the surface where it has actually happened (`ledger/approvals/`)
is the one P7 does not cover.

---

## 6 · QUESTION 3 — CLOSURE SEMANTICS

### 6.1 · The path from authorized work to downstream transition, as it exists

```
work authorized
  → A.2 TASK_ACK              assignee accepts                  [3 of 5 records, all self-written]
  → A.3 TASK_CLAIM            durable, before work starts       [5 of 5, all self-claimed]
  → work; A.6 CHECKPOINT at each durable milestone              [450 files / 27 distinct]
  → D.1 WORK_COMMIT           own branch, milestone granularity [the actual trail]
  → durable artifact          candidate / analysis / review     [governance/candidates/, learning/, reviews/]
  → HANDOFF                   B.2 message TYPE + an artifact whose format is per-author
  → XPORT § 8                 HANDOFF ESTABLISHED = 6-term conjunction
  → downstream                C.2 review · D.2 candidate · § 12 GATE 0–5 · J.3 approval
```

### 6.2 · Does LEGEND distinguish producer assertion from receiver verification?

**YES — and the canonical names are not the advisory's.** The distinction is real, allocated, and
in four places (§ 5.2). The correct answer to the dispatch's question is therefore
**`ALREADY_PRESENT` for the semantics, `PATCH_REQUIRED` for the observability**:

| the advisory's conceptual label | the canonical LEGEND object | preserve as |
|---|---|---|
| producer assertion — *"I produced this artifact"* | `TASK_COMPLETE` (J.1) · A.5 `COMPLETE` · a `WORK_COMMIT` at milestone granularity (D.1) · a checkpoint whose `MILESTONES_REACHED` names the durable evidence (A.6) | the canonical set |
| receiver / system verification | XPORT § 8 terms 1, 2, 5, 6 · C.2 `VERDICT` + mandatory `AUTHOR_RESPONSE` · `REVIEW_CLOSED` · GATE 0–5 (§ 12) · `MIRROR_REVIEW` + `HUMAN_APPROVAL` fields of the D.2 manifest | the canonical set |

🔴 **`VERIFIED_CLOSURE`, `ACTOR_ACK`, "false completion" and "receiver verification" return ZERO
hits across all 52 content refs** (positive control `ORCHESTRATOR_LEASE`: 515 ref:path hits).
These are advisory labels, not LEGEND objects, and none of them is written into anything here.

**Where the canonical separation is measurably weakest:** C.2 allocates review *closure* to the
**author** (`AUTHOR_RESPONSE` obbligatoria), not to the reviewer. That is the one place in the
canonical set where the party closing the loop is the reviewed party — and it is the shape of the
frame-inheritance risk the dispatch asks about, already present in the governance rather than
introduced by any queue.

### 6.3 · Frame inheritance — the specific risk, measured

The dispatch asks whether a downstream transition is authorized from canonical task/dependency
state or **inherited from the reviewed actor**. Four measured facts bear on it:

1. **GATE 1 exists precisely for this**: *"Proponente ≠ esecutore. Solo candidate preparati da
   Plan; mai lavoro proprio."* (§ 12). Structural, canonical, and not inheritable.
2. **C.3 requires `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR`** for important reviews, and escalates to the
   operator when `AUTHOR == ADJUDICATOR`.
3. **G.2 bars Mirror from self-approving changes to its own rubric**, and `roles/mirror.md`
   repeats it.
4. 🔴 **But review *opening* is Orchestrator's exclusive act (C.3: *"Apertura solo via
   Orchestrator"*), and in measured practice reviews are opened by `HANDOFF-*` artifacts written
   by the reviewed party.** `HANDOFF-XPORT-MIRROR.md` states its own status honestly:
   `opened_by: nobody yet. Annex C.3: a review is opened only through Orchestrator.` With **0
   ACTIVE leases** and no `ACTIVE_ORCHESTRATOR`, the act that would break the inheritance has no
   executor.

**So the frame-inheritance guard is canonical and unexecuted, not absent.** No new object is
needed to state it; what is absent is the actor who performs it.

### 6.4 · 🔴 "HANDOFF v2.1" — MEASURED NON-EXISTENCE, and the divergence it creates

```
git grep -l 'HANDOFF v2.1'  over 52 content refs   →   0 hits
git grep -l 'AUTHOR_RESPONSE' (positive control)   → 268 hits   ✅ instrument working
any versioned HANDOFF format string (HANDOFF[ _]v\d) →  4 hits, ALL of them
                                                        "MIRROR_PERSISTENCE_AND_HANDOFF_v2",
                                                        which is a TASK_ID, not a format version
```

**What canonically exists instead:**

- `HANDOFF` is one entry in **Annex B.2's message-type enumeration** and nothing more. B.2 gives
  it no envelope beyond B.1, no required field, no state effect and no closure rule.
- `cross_session_transport.md` (XPORT) § 8 defines **`HANDOFF ESTABLISHED`** as a six-term
  conjunction. This is the only substantive handoff semantics LEGEND has — and its own status line
  says it binds nobody (§ 3.8).
- Handoff **artifacts** exist and are heterogeneous by author: `governance/candidates/HANDOFF-*.md`
  (5), `learning/plan/HANDOFF-*.md`, `learning/mirror/HANDOFF-*.md`, `runtime/handoff/C-2/`. No two
  share a schema.

**`NEXT_OWNER` / `NEXT_TRANSITION`: 12 hits across 52 refs, and the repository itself labels the
vocabulary external.** Verbatim, from two different actors:

> `mirror:learning/mirror/HANDOFF-ROLE-CONTRACTS-001.md` frontmatter —
> *"`HUMAN_GATE` is the dispatch's vocabulary and has **NO repository source** — absent across all
> 41 content refs. It is reproduced here because the dispatch requires the field, and it creates
> no repository meaning. The repository's real objects for this transition are `HUMAN_REQUIRED`
> (body § 4), `HUMAN_APPROVAL` / `HUMAN_APPROVAL_QUEUE` (Annex J.3) and `GATE 0–5` (body § 12)."*

> `mirror:reviews/mirror/REV-ROLES-MIRROR-001.md:91` —
> *"The entire `NEXT_TRANSITION` vocabulary is external."*

> `plan:governance/candidates/PREP-20260822-ROLE-CONTRACT-REPAIR.md:125` — same finding, reached
> independently.

**Recorded divergence, per § 3 of the dispatch:**

```
ADVISORY / DISPATCH ASSUMES   a canonical "HANDOFF v2.1" with NEXT_OWNER / NEXT_TRANSITION
                              semantics, and a canonical VERDICT applicable to a PRODUCER
CANONICAL LEGEND HAS          B.2 type `HANDOFF` (a name in a list) + XPORT § 8 (a conjunction,
                              status PROPOSED) + heterogeneous per-author artifacts.
                              VERDICT belongs to C.2 and its domain is a REVIEW, whose values are
                              CONFIRMED | WEAKENED | REFINED | REFUTED — there is no N/A and no
                              producer verdict
RESOLUTION                    canonical LEGEND is followed. The divergence is recorded, not
                              silently reconciled. § 15 closes this dispatch the way Mirror closed
                              the structurally identical case: reproduce the field the dispatch
                              requires, label it external, and name the repository's real object
```

---

## 7 · QUESTION 4 — LEASE COUPLING

| question | measured answer |
|---|---|
| what establishes a lease? | I.2 step 9 at bootstrap, or I.3 reacquisition **only on `STALE`/`RELEASED` with recorded succession**. Concretely: a hand-written `LEASE:` block appended to `runtime/orchestrator_lease.md` |
| what actor / surface owns it? | `ACTOR_ID=orchestrator`; **writer: orchestrator ONLY, from the orchestrator worktree** (the record's own frontmatter). Readers: every actor, via git |
| what terminates / releases it? | `RELEASED_AT` (terminal, wins over the clock) or `now >= EXPIRES_AT` → `STALE`. Both are *derived*, never read from `STATUS` |
| is release coupled to task closure? | 🔴 **NO. There is no coupling of any kind, anywhere.** Nothing in I.3, D.3, D.4, § 12, § 48, A.5 or the record itself relates a lease's terminal row to any task's terminal state, and the two surfaces do not reference each other |
| if separate, what prevents `task terminal + lease ACTIVE`? | 🔴 **Nothing prevents it. Only expiry bounds it, and only at the next consultation** |

### 7.1 · The measured inconsistency and its exact scope

**Observed once, and preserved in the record as lease #3:** acquired `12:24:11Z`, never renewed,
never used, expired `13:04:11Z`, and `GATE 0` was never asserted against it. The record's own
analysis is the honest one and is reproduced rather than restated:

```
DETECTABLE   partly — lease_state.py --check reports EXPIRED_WITHOUT_RENEWAL at the next
                      consultation, which CATCHES this case but is not the same predicate
PREVENTED    no     — nothing executes between turns, so the window itself is unwatched
```

🔴 **`EXPIRED_WITHOUT_RENEWAL` is named for what it measures, and that is narrower than "unused".**
Three of the five records — #2, #4 and #5 — were **never renewed and were demonstrably used**,
each holding a canonical batch. **A lease used without renewal is indistinguishable in this format
from one never used at all.**

### 7.2 · The three declared layers — and which one is load-bearing

| layer | covers | lives in |
|---|---|---|
| `MECHANIZED` | derivation from `RELEASED_AT` · `EXPIRES_AT` · clock; stored-vs-derived disagreement; `EXPIRED_WITHOUT_RENEWAL`; the `ACTIVE` singleton as an invariant, fatal in every mode | `lease_state.py`, tracked, runnable by any actor |
| `OBSERVABLE` | the record, its git history, the derivation's output — reproducible by a second actor | the record + `git log` |
| 🔴 `PROCEDURAL` | **writing a row at all.** Acquisition, renewal and the terminal row are authored by hand. Nothing compels the Orchestrator to record an acquisition, and nothing runs between turns | discipline |

**The record names its own closure mechanism, and names it as owed:**

> *"Closing it needs something that runs when no actor is running — **the `P7` event ledger with
> `LEASE_ACQUIRED` / `LEASE_STALE` is the mechanism the governance already names**, and it is
> `OWED NOT BARRED`. This candidate does not build it and does not claim to."*

**This is the strongest single piece of evidence in the whole surface map**: the lease surface,
independently, arrived at P7 as its own remedy. Mirror reached the same place from a third
direction — open question 8 of `HANDOFF-ROLE-CONTRACTS-001`: *"Is a J.1 event-ledger writer to be
scheduled? Four clauses across two contracts are unenforceable without one, and the lease record
itself names `LEASE_ACQUIRED`/`LEASE_STALE` as the closure for its own unwatched-window failure."*

**No second lease mechanism is originated here, and none is needed.** The gap is not in lease
semantics; it is that two of J.1's existing 23 types have no emitter.

### 7.3 · A second, structural lease finding — carried, not reopened

`GATE 0` requires an `ACTIVE` lease, and a lease's terminal row is written **after** the batch that
lease authorized. The row can therefore never sit inside the batch it authorized, so `main`'s copy
of the record **lags by at least the current lease, permanently** (`main` #1–#5, `orchestrator`
#1–#8). § P5.1 records this already; it is confirmed unchanged at this HEAD and is **not** reopened.

---

## 8 · QUESTION 5 — RETRY / ITERATION / TIMEOUT / ESCALATION

### 8.1 · What exists, with its normative standing

| concept | canonical rule | value | standing |
|---|---|---|---|
| retry | A.1 `RETRY_POLICY: max_attempts / retryable error classes / on_exhaust` | per contract | **FROZEN** (A.1) |
| `on_exhaust` default | § P1 | **`PARK`** | 🔴 inside a `PROPOSED` file (§ 3.8) |
| retry in practice | the 2 task records that carry it | `max_attempts: 1`, `retryable_error_classes: []`, `on_exhaust: ESCALATE` | legal — A.1 lets a contract name a different value — but it is the opposite of P1's default in both records |
| reassignment | A.4 `GENERATION`+1; H.1 row 1 | — | **FROZEN** |
| ACK timeout | B.3 → § P3 | **30 minutes**; on timeout resend (dedup by `MESSAGE_ID`); on 2nd miss → `BLOCKER` | 🔴 `PROVISIONAL` (E.3, `PROV-ACK-TIMEOUT-30M`), inside a `PROPOSED` file. **Expiry: after the third scientific batch.** 0 scientific batches have run |
| heartbeat / DOWN | B.3 → § P4 | **30 min cadence; DOWN after 3 consecutive misses (≈ 90 min)** | 🔴 `PROVISIONAL` (`PROV-HEARTBEAT-30M-3X`), same expiry, same non-arrival |
| lease expiry | I.3 `EXPIRES_AT` | 🔴 **no governed value.** Observed windows, hand-chosen per record: **2, 40, 40, 60, 60 minutes** | the field is FROZEN; the duration is undefined |
| human escalation | body § 4 (closed taxonomy) · § 9.5 · J.3 · § 48 stop conditions | — | **FROZEN** |
| iteration | 🔴 **does not exist as a governed concept** (§ 1.2) | — | — |
| stale dispatch / dispatch timeout | 🔴 **does not exist.** The only `stale dispatch` text in the repository is a *learned gate about instruction staleness*, not a timeout | — | — |
| duplicate dispatch | 🔴 0 hits across 52 refs | — | — |

### 8.2 · The calibration need, recorded and NOT filled

```
UNRESOLVED_CALIBRATION_1   no normative lease duration exists (I.3 defines the field, not the value)
UNRESOLVED_CALIBRATION_2   no dispatch staleness / dispatch timeout concept exists at all
UNRESOLVED_CALIBRATION_3   P3 and P4 are PROVISIONAL with an expiry keyed to "the third scientific
                           batch". Zero scientific batches have run, so BOTH practices are
                           unexpirable in practice and their SUCCESS/FAILURE criteria —
                           "ACK latency distribution from the event ledger (J.1)", "DOWN
                           declarations vs actual session deaths, from the event ledger" —
                           🔴 name as their evidence source the very ledger that does not exist
UNRESOLVED_CALIBRATION_4   MIRROR_RETROSPECTIVE cadence N remains UNASSIGNED_PARAMETER, as
                           § P7's own closing section and the 2026-08-22 handoff both record
```

**No value is invented here.** `T1`/`T2` thresholds are not proposed, not sketched, and not
implied. A missing threshold is recorded as missing.

🔴 **Calibration 3 is the load-bearing one and it is circular**: the two PROVISIONAL timing
practices are to be validated *from the event ledger*, and the event ledger is not built. Neither
can be promoted or rejected on evidence until it is.

---

## 9 · QUESTION §11 — RECOVERY BEHAVIOUR

### 9.1 · RECOVERY POINT A — durable closure claim exists, notification/verification did not

**Canonically supported? PARTIALLY, and the missing half is named.**

```
SUPPORTED   A.7 idempotent resume: "Completed work is not repeated." Before re-executing a step
            the actor MUST verify in durable state whether the milestone evidence already exists;
            if it does, skip and record RESUMED_FROM_MILESTONE.
            The idempotency boundary is the SIGNIFICANT DURABLE MILESTONE (MILESTONE_PLAN), not
            every mutating operation. The receipt-ledger pattern is its founding case.
SUPPORTED   B.3 resend on missed ACK, deduplicated by MESSAGE_ID
SUPPORTED   A.6 checkpoints carry MILESTONES_REACHED with the durable evidence for each

NOT SUPPORTED   🔴 detection of "the producer output exists but the receiver never verified".
                XPORT § 8's own DETECTION row:
                  terms 1, 2, 6 leave durable artifacts → absence visible to Plan/Mirror
                  term 5 — "the recipient read it" — 🔴 DETECTION: NONE — ATTENTION_ONLY
NOT SUPPORTED   🔴 "notify/re-notify the receiver" has no addressable receiver.
                XPORT § 9: term 3 (exactly one current target for the ACTOR_ID) CANNOT BE
                SATISFIED TODAY. Measured on the machine: plan 8 live sessions, mirror 7,
                scientist-a 0, scientist-b 0; the registry's recorded current session for plan
                was alive, three days old, and not the current one. --cwd narrows 19 to 8, not 1.
                Ruling: "IF no unique target → ROUTING: BLOCKED. Fail closed."
```

**Verdict: `PATCH_REQUIRED`, and the smallest delta is emission, not architecture.** With
`TASK_COMPLETE` emitted by the producer and a durable ACK event by the receiver, "producer output
exists, receiver never verified" becomes a **query over the ledger** — an opening with no
matching `CLOSES_EVENT_ID` past a threshold — which is exactly J.1's declared `DETECTION`:
*"incrocio ledger ↔ stato durevole (gap = evento mancante); aperture senza chiusura oltre soglia
→ Mirror retrospettive."* **The detector is already specified. It has no input.**

### 9.2 · RECOVERY POINT B — actor acknowledged and produced a work commit, closure incomplete

**Canonically supported? YES for the refusal half, NO for the completion half.**

```
SUPPORTED   § 36.5 rehydration: declare ACTOR_ID, role, authority limits, governance version,
            verify fingerprint AND checkpoint compatibility BEFORE resuming anything;
            "Memory or conversation helps orient; durable repository state decides."
SUPPORTED   A.4 anti-zombie: verify generation, directive version and checkpoint compatibility;
            stale → DO NOT CONTINUE, ask for state
SUPPORTED   A.6 MAF refusal rule: incompatible fingerprint → do NOT resume, signal and ask
SUPPORTED   A.7 + § 36.3: skip work whose durable evidence already exists, record
            RESUMED_FROM_MILESTONE
SUPPORTED   A.5: PARKED and AWAITING_APPROVAL park at the exact point with a checkpoint and
            resume without redoing work
```

**"Task-bound" — what the dispatch proposes vs what LEGEND already has, which is stronger:**

| dispatch's proposed proof leg | canonical LEGEND equivalent | which is stronger |
|---|---|---|
| commit belongs to assigned actor/worktree/ref | D.1 `WORK_COMMIT` is *"ogni attore, PROPRIO worktree/branch"`; § 14 `ONE_WRITER_PER_WORKING_DIRECTORY`; I.4 `ACTOR_ID` is identity and `SESSION_REF` is routing | **canonical** — it is a write-perimeter invariant, not an after-the-fact inference |
| commit temporally follows assignment/acknowledgement | 🔴 **weaker in LEGEND than proposed.** A.3 requires a claim `timestamp`; measured, 3 of 5 claims carry **date-only** precision because *"the runtime exposed no wall-clock time"* | **the dispatch's** — but it is unbuildable on a date-only stamp |
| modified paths conform to `scope_lock` | 🔴 **`scope_lock` returns 0 hits over 52 refs** (positive control 515). LEGEND's equivalents: A.1 `SCOPE`, § P5.1 `CONTROL_PLANE_ROOTS`, and the `WRITE_PERIMETER` block that task records already carry with `content_domain_written` / `control_plane_written` / `deliberately_not_touched` | **canonical**, and it is *declarative and auditable* rather than enforced |
| expected task artifact exists | A.1 `MILESTONE_PLAN` — each milestone with *"l'evidenza durevole verificabile che deve lasciare (receipt, output, registry, checkpoint)"*; A.6 `MILESTONES_REACHED` | **canonical, and materially stronger** — the evidence is declared in the contract *before* the work, not inferred after |

🔴 **`scope_lock` must not be introduced.** LEGEND already binds scope in three places, and one of
them (`MILESTONE_PLAN` + `MILESTONES_REACHED`) is a stronger binding than any path filter, because
it names the evidence in advance.

**What is genuinely missing for Recovery Point B:** nothing in the *refusal* direction — the MAF
rule, A.4 and § 36.5 already stop an unsafe resume, and they are the half that protects
correctness. What is missing is the *completion* direction: a fresh instance can prove the work
happened but has **no canonical act by which to complete a closure another instance did not
finish**, because the closure act itself (`TASK_COMPLETE` emission, the durable ACK) has no
surface. **`PATCH_REQUIRED`, same delta as Recovery Point A.**

**And there are five of them on this checkout right now.** § 2.4: five substantive Plan analyses,
authored 2026-08-22, never committed. A fresh instance can see the files but there is no task
record binding them, no `MILESTONE_PLAN` to check them against, and no closure act to complete.

---

## 10 · QUESTION §12 — ORCHESTRATOR CONTINUATION AUTHORITY

**The principle to test:** Orchestrator does not request fresh human permission for a transition
already authorized by canonical task definition, satisfied dependencies, current actor/lease
authority, valid scope and existing governance.

### 10.1 · Classification: **`ALREADY_PRESENT`** — and stated more strongly than the dispatch states it

Five independent canonical clauses, all FROZEN, none needing amendment:

```
§ 9.5   "Nessun attore escala all'operatore per questioni ordinarie:
         problema → Orchestrator → recovery/riassegnazione/consultazione."
§ 4     HUMAN_REQUIRED is a CLOSED taxonomy — a 13-row table. Everything not in it: the system
         continues. Three of the four "sì" rows are spend, MAJOR/governance, and destructive.
§ 2     "Orchestrator controls what work is done, by whom and in which order."
         OPERATIONAL AUTHORITY → WHO / WHAT / WHEN / PRIORITY / REVIEW / RECOVERY
H.1     Task / priority / reassignment / generation → Orchestrator. Ladder level and reviewer →
         Orchestrator. Ordinary HUMAN_REQUIRED classification → Orchestrator. Challenge
         adjudication → Orchestrator. 🔴 NONE of these rows is conditioned on an approval
§ 3      95/5, and G.3 makes an avoidable escalation a MEASURED DEFECT: the AUTONOMY LEDGER
         classifies HUMAN_REQUIRED as PREVENTABLE vs UNAVOIDABLE and counts false escalations.
         § P1 chooses PARK over ESCALATE for exactly this reason: "ESCALATE spends a
         HUMAN_REQUIRED, and § 3 measures exactly that."
```

**LEGEND does not merely permit autonomous continuation — it measures asking as a defect.** No
patch, no new authority, no amendment. Anything that added a per-transition approval step would
*contradict* § 9.5.

### 10.2 · What it does not grant — confirmed unchanged

`roles/orchestrator.md` and § 35.1 already bar: scientific-author authority (§ 2, § 28: epistemic
independence belongs to the Scientist, *"soggetta a review, mai a ordine"*); governance amendment
(H.1 → operator); rewriting another actor's handoff or worktree; anything reserved to the human
gate (§ 4, J.3, § 48). **`APPROVAL ≠ AUTHORIZATION` (E4)** caps it from the other side: an approval
authorizes intent and never exempts execution from the gates.

### 10.3 · 🔴 The blocker, and it is not authority

```
ACTIVE leases by derivation, 2026-08-23T09:16:27Z    0
ACTIVE_ORCHESTRATOR                                  none
LAB_STATE per body § 9.4                             ORPHAN follows from Orchestrator DOWN
durable roster (J.2)                                 0 artifacts on 52 refs (control: 5 *registry*)
Agent Card registry                                  1 ref only (orchestrator), updated_on
                                                     2026-08-17, 23 UNVERIFIED rows, and
                                                     runtime/L2-OUTCOMES.md on the SAME branch
                                                     records 3 VERIFIED, ratified by the operator
                                                     decision of 2026-08-18 — never reconciled
                                                     back. Body § 43: "riga stantia = non
                                                     autoritativa"
roles/orchestrator.md                                non-binding (DEC-20260822)
```

**The authority to continue autonomously is present and unexercised. What is absent is an actor
holding it.** That is a runtime/activation condition, not a governance gap, and no patch to the
event model changes it.

---

## 11 · A / B / C CLASSIFICATION

### 11.1 · 🔴 The advisory's A / B / C could not be read — measured, not assumed

The dispatch requires classifying "each of A/B/C from the advisory". **The advisory was not
supplied and does not exist in any surface reachable from here:**

```
declared: EXTRACTION-20260823-QUEUE-CLOSURE-LOOP v1.2, 171 lines,
          sha256 70c8b312a706a96604dc9ef2716a280f78387d41cfa511506e90bfdd595e68a1

id string 'EXTRACTION-20260823' | 'QUEUE-CLOSURE-LOOP'  over 52 refs  →  0 hits
'ADVISORY_EXTRACTION'                                   over 52 refs  →  0 hits
POSITIVE CONTROL 'ADVISORY-FABLE'                       over 52 refs  → 109 hits ✅

every distinct blob across 52 content refs, sha256'd  → 1122 blobs, 🔴 NO MATCH
every file in the working tree incl. untracked        → 🔴 NO MATCH
advisory body text in the dispatch                    → 🔴 NOT TRANSMITTED
```

**The declared SHA256 is therefore UNVERIFIED and is not claimed as verified**, exactly as the
dispatch itself instructs. **No path was invented for it.**

**What is classified instead, stated as an assumption rather than smuggled in:** the only three
labelled capability clusters actually transmitted are the dispatch's own § 11 RECOVERY POINT A,
§ 11 RECOVERY POINT B, and § 12 Orchestrator continuation. They are classified below as **A′/B′/C′**
to make the substitution visible. **If the advisory's A/B/C differ, this mapping is wrong and the
classification must be redone against the artifact.**

### 11.2 · Classification

| | cluster | local class | why |
|---|---|---|---|
| **A′** | RECOVERY POINT A — durable producer output exists, receiver never verified | **PATCH_REQUIRED** | § 9.1. The *detector* is already specified (J.1 `DETECTION`: openings without closure past a threshold → Mirror). It has **no input**, because 0 of 23 types are ever emitted. Additionally blocked on XPORT § 9 term 3 (routing), which is a separate, already-owned debt |
| **B′** | RECOVERY POINT B — acknowledged + work committed, closure incomplete | **PATCH_REQUIRED** (completion half) / **ALREADY_PRESENT** (refusal half) | § 9.2. A.4, A.6 MAF and § 36.5 already stop an unsafe resume — that half needs nothing. `scope_lock` must **not** be added: `MILESTONE_PLAN` + `WRITE_PERIMETER` + `CONTROL_PLANE_ROOTS` are stronger. The missing piece is the same missing emission |
| **C′** | Orchestrator continuation without per-transition permission | **ALREADY_PRESENT** | § 10. Five FROZEN clauses grant it and G.3 measures asking as a defect. **Proposing anything here would duplicate § 9.5 and contradict § 4.** Blocked on 0 ACTIVE leases, which is activation, not authority |

**PATCH_REQUIRED detail, as § 13 of the dispatch requires — one patch serves both A′ and B′:**

```
MEASURED FAILURE      0 of 23 J.1 event types emitted, over 52 content refs, with working
                      positive controls (450 checkpoint files, 450 CHECKPOINT_ID hits).
                      Consequences measured, not inferred:
                        · ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl FORKED into three
                          lineages; main carries none of the four canonicalizing approvals
                        · lease #3 EXPIRED_WITHOUT_RENEWAL, unwatched window, and the lease
                          record itself names P7 as its own closure
                        · 7 analyses of this exact subject on 7 refs, 0 consolidated
                        · P3 and P4 PROVISIONAL, both naming the event ledger as their
                          evidence source, both unexpirable
                        · Mirror's declared primary analysis surface does not exist
                        · 5 substantive analyses uncommitted on this checkout right now

SURFACE AFFECTED      ledger/events/<ACTOR_ID>.jsonl   (per-actor, actor's own worktree)
                      ledger/consolidated/             (derived, rebuilt by replay)
                      — both ALREADY NAMED by § P7. No new path, no new root: `ledger/` is
                      already a declared CONTROL_PLANE_ROOT (P5.1), so an event file is
                      OUTSIDE the candidate content domain by construction

SMALLEST VIABLE DELTA build the writer and the consolidator that § P7 already specifies, on the
                      append-only machinery that already exists — framework/scripts/
                      fulltext_receipts.py, whose hash chain and tail anchor the LINT already
                      consumes, and which § P7 itself names as the pattern to reuse.
                      🔴 NO new event type. NO new state machine. NO new control plane.
                      NO new ledger. NO change to lease semantics. NO timeout value.

WHY CONFIRM_ONLY IS   a test cannot emit an event. Every downstream capability in § 12 — recovery
INSUFFICIENT          detection, retrospectives, the autonomy ledger, review yield, checkpoint
                      invalidation rate, redone-work ratio, and the promotion/rejection of P3 and
                      P4 — reads the ledger. A confirming test would confirm 0

WHY NO NEW OBJECT     every object exists on paper: the event shape (J.1), the 23 types (J.1), the
IS NECESSARY          topology decision (P7), the paths (P7), the closure link (CLOSES_EVENT_ID),
                      the derived-view rule (P7 + J.1), the domain classification (P5.1), the
                      detector (J.1 DETECTION), the recovery (J.1 RECOVERY, RECONSTRUCTED
                      marking), the reuse target (fulltext_receipts.py). Building any of them
                      again would be the accretion failure the repository's own rules name

change_class          🔴 NOT DETERMINED HERE, and deliberately. If the delta is purely an
                      implementation of an already-decided parameter, § 12's strict MAJOR
                      definition may not reach it; if it touches governance/authority/gates or a
                      canonical schema, it is MAJOR. § 12 is explicit that doubt is Mirror's to
                      resolve fail-closed. Plan does not classify its own future candidate here

🔴 PRECONDITION       § P7 sits in a file whose status line reads `PROPOSED — normative once
                      Mirror hostile review passes and the operator approves`, and no activation
                      record exists (§ 3.8). Building to P7 before that is settled would
                      implement a parameter whose normative standing is the open question
                      DEC-20260822 answered OPTION B for the structurally identical case. THIS
                      IS THE FIRST THING A LATER DEC MUST DECIDE
```

---

## 12 · MEASURED GAP TABLE

| Capability | Canonical current surface | Measured evidence @ scope § 2 | Emission / use count | Local class | Minimal residual delta | Normative authority needed later |
|---|---|---|---|---|---|---|
| durable execution trail | **J.1** (spec) · in practice: `ledger/tasks/` + `ledger/checkpoints/` + git history + `governance/candidates/` + `reviews/` | `ledger/events/` **0 files / 52 refs**; `ledger/consolidated/` **0 / 52**; control 450 | **0 events**; 5 task records; 450 checkpoint files (27 distinct) | **PATCH_REQUIRED** | implement § P7 (a) on the existing append-only pattern | operator determination on § P7's status (§ 3.8); then Mirror R4 + GATE 3 if MAJOR |
| dispatch | **A.1** + B.2 `TASK_ASSIGNMENT` → `TASK_ASSIGNED` | 5 task records, all `plan`→`plan`; `XPORT-ROUTING-001._note`: no `TASK_ASSIGNMENT` message received | **0** | **PATCH_REQUIRED** | emit `TASK_ASSIGNED`. 🔴 no new object — the 15-field schema is complete | needs an `ACTIVE_ORCHESTRATOR` (H.1 row 1), not a governance change |
| actor acknowledgement | **A.2** `TASK_ACK` + **A.3** `TASK_CLAIM` (two acts) → `TASK_ACKED`, `TASK_CLAIMED` | 3/5 ACK blocks, **all self-written**; 5/5 claims, all `claimed_by == OWNER` | **0** | **PATCH_REQUIRED** | emit both. Preserve the two-act split | none for the split — it is FROZEN in A.3 |
| actor closure | **`TASK_COMPLETE`** · A.5 · D.1 `WORK_COMMIT` | `MILESTONE_PLAN` statuses and `STATE` strings inside task records; commits | **0** | **PATCH_REQUIRED** | emit `TASK_COMPLETE` with `DURABLE_POINTER` | none |
| receiver / system verification | **XPORT § 8** terms 1,2,5,6 · **C.2** VERDICT + mandatory AUTHOR_RESPONSE · `REVIEW_CLOSED` · GATE 0–5 · D.2 manifest fields | separation exists in 4 places (§ 5.2). XPORT § 8 term 5 detection: 🔴 `NONE — ATTENTION_ONLY`. Review *closure* allocated to the **author** (C.2) | **0 events**; 54 `REV-*` vs 8 `AUTHOR-RESPONSE-*` | **ALREADY_PRESENT** (semantics) + **PATCH_REQUIRED** (observability) | emit `REVIEW_OPENED`/`REVIEW_CLOSED`. 🔴 do **not** name a new "VERIFIED_CLOSURE" | any change to C.2's author-closure allocation is FROZEN-governance → MAJOR |
| dependency-driven next transition | **A.1 `DEPENDENCIES`** · **§ 12 GATE 0–5** · **GATE 1** proponente ≠ esecutore | GATEs are canonical and mechanically partly checkable; **GATE 0 is asserted by hand**; C.3 review opening has no executor at 0 leases | 0 events; 4 canonical batches evidenced via approvals on `orchestrator` | **CONFIRM_ONLY** | test that transitions derive from `DEPENDENCIES` + gates, not from the reviewed actor's handoff | none — the guard is FROZEN and adequate; only unexercised |
| actor rehydration | **§ 36.5** · **A.4** · **A.6** MAF refusal · **A.7** / § 36.3 | 27 checkpoints carry full `REHYDRATION` blocks with `verdict: PASS`; SCIAB record documents 4 generations rehydrating fail-closed with nothing carried from prompt | n/a — exercised | **ALREADY_PRESENT** (refusal) / **PATCH_REQUIRED** (completing another instance's closure) | § 9.2. 🔴 do **not** add `scope_lock` | none for the refusal half |
| lease integration | **I.3** · `runtime/orchestrator_lease.md` · `lease_state.py` · **D.3 GATE 0** | derived **0 ACTIVE**; 5 records; 1 `DISAGREEMENT` (`EXPIRED` ∉ vocabulary); 1 `EXPIRED_WITHOUT_RENEWAL`; `main` #1–#5 vs `orchestrator` #1–#8 | 5 lease rows; **0 `LEASE_ACQUIRED` / `LEASE_STALE` events** | **PATCH_REQUIRED** | emit the two existing types. 🔴 **do not alter lease semantics and do not originate a second mechanism** — the record itself names P7 as its closure | none — the types already exist in J.1 |
| Orchestrator continuation | **§ 9.5** · **§ 4** · **§ 2** · **H.1** · **§ 3 / G.3** | 5 FROZEN clauses grant it; G.3 measures asking as `PREVENTABLE`; § P1 chooses PARK over ESCALATE for that reason | 0 ACTIVE leases → unexercised | **ALREADY_PRESENT** | 🔴 **none. Propose nothing.** Anything added here contradicts § 9.5 | none |
| human escalation boundary | **§ 4** closed taxonomy · **J.3** queue · **§ 48** stop conditions · **G.3** autonomy ledger | queue exists and is used — and is **FORKED across 3 lineages**, with `DEFERRED`/`RESOLVED` outside J.3's vocabulary; `main` carries none of the 4 canonicalizing approvals | 14 queue lines total across all lineages; **0 `HUMAN_REQUIRED_OPENED` / `APPROVAL_RESOLVED` events** | **PATCH_REQUIRED** | emit the two types **and** allocate a writer for `ledger/approvals/`, which § P7 does not cover | allocating a writer to a J.3 surface is a governance act → operator / Mirror R4 |
| roster (J.2) | **J.2**: *"Ogni transizione = evento (J.1) + roster durevole"* | 🔴 **0 roster artifacts on 52 refs** (control: 5 `*registry*` paths). `runtime/agent_card_registry.md` exists on **1** ref, `updated_on: 2026-08-17`, 23 `UNVERIFIED` / 0 `VERIFIED`, contradicted by `runtime/L2-OUTCOMES.md` (3 VERIFIED, operator-ratified 2026-08-18) on the same branch | 0 | **PATCH_REQUIRED** — reported, out of this dispatch's scope | reconcile the registry against L2-OUTCOMES; § 43 already rules *"riga stantia = non autoritativa"* | none for the reconciliation |

---

## 13 · MINIMUM RESIDUAL DELTA

**One delta. It builds nothing new.**

```
BUILD   the P7 (a) writer and the Plan consolidator, on the append-only + hash-chain + tail-anchor
        pattern that framework/scripts/fulltext_receipts.py already implements and the LINT
        already verifies — which is the reuse target § P7 itself names.

        ledger/events/<ACTOR_ID>.jsonl     one writer per file, by construction
        ledger/consolidated/               derived, rebuilt by replay, never hand-edited
        both already inside a declared CONTROL_PLANE_ROOT → outside the candidate content domain

EMIT    the existing 23 types. No new type. Priority order follows demonstrated failure, not
        completeness:
          1  LEASE_ACQUIRED · LEASE_STALE      the lease record names these as its own closure
          2  TASK_ASSIGNED · TASK_ACKED · TASK_CLAIMED · TASK_COMPLETE   the loop's spine
          3  HUMAN_REQUIRED_OPENED · APPROVAL_RESOLVED   the forked-queue surface
          4  CHECKPOINT_WRITTEN · RESUMED_FROM_MILESTONE · WORK_COMMIT   already-durable acts

DO NOT  create a queue architecture · create a control plane · create a second ledger · create an
        event type · create a state machine · alter lease semantics · invent a timeout · invent a
        retry value · add scope_lock · add VERIFIED_CLOSURE or any advisory token · reopen the
        cold-lab PIVOT · originate automatic actor relaunch
```

**Three preconditions, none of which Plan may satisfy and all of which are already owned:**

| # | precondition | owner |
|---|---|---|
| P-1 | 🔴 § P7's normative standing. Its file reads `PROPOSED` and no activation record exists. `DEC-20260822` answered `ACTIVATION_NOT_CONFIRMED` for the structurally identical case and scoped itself to `roles/`. **Building to a parameter whose standing is unresolved is the error that decision exists to prevent** | **operator**, under H.1 |
| P-2 | No `ACTIVE_ORCHESTRATOR`. `TASK_ASSIGNED` has one authorized writer (H.1 row 1) and there is nobody holding it. An event ledger that only Plan writes reproduces the self-written-task-record defect at a new layer | activation, not governance |
| P-3 | XPORT § 9 term 3 — routing. `ACTOR_ID → current session` is unresolved repository-wide, and `SESSION_ROUTING_DEBT` is recorded in `APR-20260819-XPORT-001`. Recovery Point A's *"notify/re-notify the receiver"* has no addressable receiver | `CANDIDATE B — ACTOR SESSION LIFECYCLE / ROUTING`, already named as successor work |

**A second, separable delta, reported because § 3.6 measures it as already-failed and § P7 does
not reach it:** `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` has **no declared writer**, has
**forked into three lineages**, and carries **two states outside J.3's vocabulary**. Allocating a
writer to it is a governance act and is **not proposed here**.

---

## 14 · T0 / T1 / T2a / T2b / T3 — APPLICABILITY AGAINST DISCOVERED SEMANTICS

> These are the dispatch's local test names. They are not written into any governed object.

### T0 — three deterministic tasks · closure syntax, artifact verification, routing mechanics

```
APPLICABLE   PARTIALLY — and every proposed metric is currently unmeasurable
```

| candidate metric | measurable today? |
|---|---|
| valid closure trail count | 🔴 **NO** — 0 events; no trail object exists |
| verified closure count | 🔴 **NO** — same |
| duplicate notification count | 🔴 **NO** — no notification record; `MESSAGE_ID` dedup is specified (B.3) and unlogged |
| duplicate dispatch count | 🔴 **NO** — 0 hits for the concept; A.3 `CLAIM_CONFLICT` is the canonical detector and requires claims that exist |
| manual routing count | ⚠️ **PARTLY** — XPORT § 9 already records that actor-routed sends **are** operator-mediated today, so the count is trivially "all of them" |
| false completion count | 🔴 **NO** — nothing records completion |
| lease inconsistency count | ✅ **YES, TODAY** — `lease_state.py --check` reports `DISAGREEMENT` and `EXPIRED_WITHOUT_RENEWAL`. Current value: **2 findings on 5 records** |

**One metric of seven is measurable. T0 measures the delta, it cannot precede it.** Its honest
current form is a **baseline**: run the lease derivation, count task records, count events (0),
count approval-queue lineages (3). That baseline is in this record.

### T1 — ten real open governance tasks, operator hands-off, `DELEGABLE_HUMAN_INTERVENTIONS = 0`

```
APPLICABLE   NO — blocked on P-2, not on design
```

- 🔴 `DELEGABLE_HUMAN_INTERVENTIONS`: **0 hits over 52 refs.** The canonical instrument is G.3's
  **AUTONOMY LEDGER** — `HUMAN_REQUIRED` **PREVENTABLE vs UNAVOIDABLE**, hours blocked, work
  continued during HITL, **false escalation**, voluntary supervision excluded. It maps the
  dispatch's intent exactly and already exists. **Use it; do not introduce a new token.**
- 🔴 The autonomy ledger has **no instance on any of 52 refs**, and G.3 derives it from the
  consolidated event ledger (J.1). Same missing input.
- 🔴 Autonomous dispatch requires an `ACTIVE_ORCHESTRATOR`. There are **0 ACTIVE leases**.
- ✅ The classification the dispatch asks for — *expected by governance* vs *false escalation* — is
  **already the AUTONOMY LEDGER's own PREVENTABLE/UNAVOIDABLE axis**, with § 4's closed taxonomy
  as the decision table.

### T2a — interrupted actor, fresh instance supplied externally · rehydration recovery only

```
APPLICABLE   YES — and it is the ONE test runnable before any delta
```

Every mechanism it exercises exists and is exercised in practice: § 36.5, A.4, A.6 MAF, A.7 /
§ 36.3, A.5 `PARKED`/`AWAITING_APPROVAL`. `SCIENTIST-AB-SPEC-001` documents four generations, each
a new session inheriting nothing and reconstructing everything from durable state.

🔴 **Two boundary conditions must be declared or T2a will pass for the wrong reason:**

1. **The success criterion — *"complete handoff without unnecessary substantive re-execution"* —
   is only partly measurable.** A.7 makes the idempotency boundary the *significant durable
   milestone*, and the redone-work ratio (Mirror's metric under A.7/G.3) derives from the event
   ledger. A fresh instance can prove *the milestone evidence exists*; it cannot today prove
   *nothing was redone*.
2. **The "complete the missing closure steps" half has no canonical act** (§ 9.2). T2a as
   specified can succeed at the refusal half and has nothing to succeed at in the completion half.

**Realistic scope today:** T2a tests **safe non-resumption and correct milestone skipping**. It
cannot test closure completion until the delta exists. **Live fixture already present:** the five
uncommitted analyses of § 2.4.

### T2b — automatic actor relaunch / rebind

```
UNMEASURED / OUT OF SCOPE
```

**No such mechanism is authorized or canonical.** Body § 4 puts a crashed actor's reopening
explicitly on the human side (*"sì, solo per riaprire la UI"*); § 36.6 routes non-responsiveness
to `DOWN` → PARKED or reassigned with generation+1 → **asynchronous notification** → rehydration;
J.0 lists *"Failure detection + restart automatici"* among the guarantees LEGEND **does not
possess**. **Not originated here.**

### T3 — cold lab, no active runtime

```
OUT OF SCOPE — not reopened, not analysed, not referenced
```

---

## 15 · EVIDENCE PREPARED FOR MIRROR'S HOSTILE REVIEW

Mirror's adjudicative role is not performed here. These are the surfaces its six named attacks
would need, with the measurement already executed so it can re-run rather than re-derive.

### 15.1 · Concurrent writes / cross-ref visibility

```
PRIMARY EXHIBIT   ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl — 3 lineages, 2 of them forked
  git rev-parse main:ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl          → 20c24a2ba478  ( 6)
  git rev-parse orchestrator:ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl  → bb603d9a270b  (10)
  git rev-parse evidence-index:ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl→ 95fc81639014  (14)
  cmp <(git show orchestrator:… ) <(git show evidence-index:… | head -10) → DIFFER
SECONDARY         governance/decisions/ — 5 records, NO ref carries all 5; main carries 1,
                  orchestrator-surface carries 4, this HEAD carries 2
TERTIARY          7 sibling analyses of this subject on 7 refs, 0 on main (§ 3.7)
QUATERNARY        runtime/agent_card_registry.md (1 ref) vs runtime/L2-OUTCOMES.md (same ref):
                  23 UNVERIFIED vs 3 operator-ratified VERIFIED, never reconciled
COUNTER-EVIDENCE  P7 option (a) is the construction that prevents this class, and the surfaces
                  where it HAS happened are all surfaces P7 does not cover. Mirror should test
                  whether that is a real defence or a scoping accident
```

### 15.2 · False completion / false closure acceptance

```
0 completion events exist, so no false one can yet be measured — the population is empty and
Mirror should treat "0 false completions" as UNMEASURABLE, not as PASS
C.2 allocates review closure to the AUTHOR (AUTHOR_RESPONSE), not the reviewer — the canonical
   shape closest to a producer closing its own loop
54 REV-* vs 8 AUTHOR-RESPONSE-* (sibling measurement, ref-scoped) — outstanding closures
XPORT § 8 term 5 ("the recipient READ it") — DETECTION: NONE — ATTENTION_ONLY, declared
REV-ROLES-MIRROR-001 AUTHOR_RESPONSE: required and OUTSTANDING at this HEAD
```

### 15.3 · Duplicate dispatch

```
A.3: "Al più UN claim valido per TASK_ID + GENERATION" — the canonical uniqueness rule
A.3 G/F/D/R names the exact failure: "doppio claim su riassegnazione concorrente o rehydration
   stale (nessun lock di filesystem)"; detection is CLAIM_CONFLICT at write or at Plan's
   reconciliation; recovery is Orchestrator adjudication
MEASURED: 5 claims, all by the same actor for distinct TASK_IDs → 0 conflicts, and the
   population cannot produce one. UNMEASURABLE, not PASS
J.0 row 1 caps the vocabulary: no atomic task checkout exists; the compensator is
   single-assigner + claim record + conflict detection
```

### 15.4 · Lost or replayed acknowledgement / notification

```
B.3: ACK mandatory on STATE_CHANGE: yes; timeout → resend deduped by MESSAGE_ID; 2nd miss → BLOCKER
B.3 FAILURE, verbatim: "ACK emesso ma lavoro mai partito (classi misurate: turno troncato,
   permission prompt); duplicati post-reinvio"
XPORT § 4: a declared schema bound may or may not be enforced — `summary` declares 200 and
   accepted 264 SILENTLY; `to` declares 200 and rejects at 213. Sender-invisible truncation
XPORT § 5: DELIVERY_UNKNOWN is the residual class and "must stay non-empty"
XPORT § 6: "NOT LISTED → UNKNOWN. Never NOT LISTED → DEAD"; a resolving name is not a live
   session (scientist-a resolved to a job dead three days, pid: null)
MEASURED: 0 MESSAGE_ID records exist anywhere → dedup is specified and unlogged
```

### 15.5 · Frame inheritance from the reviewed actor

```
GUARD PRESENT   GATE 1 (proponente ≠ esecutore) · C.3 (AUTHOR ≠ REVIEWER ≠ ADJUDICATOR;
                escalate when AUTHOR == ADJUDICATOR) · G.2 (Mirror may not self-approve its
                own rubric) · § 28 (Plan's epistemic boundary is absolute)
GUARD UNEXERCISED  C.3: "Apertura solo via Orchestrator". Measured: reviews are opened by
                HANDOFF-* artifacts written by the reviewed party. HANDOFF-XPORT-MIRROR.md says
                so in its own frontmatter: "opened_by: nobody yet."  0 ACTIVE leases → no executor
LIVE INSTANCE   REV-ROLES-MIRROR-001 emitted NO verdict on roles/mirror.md (self-review
                prohibition), and the 2026-08-22 handoff records that the G.2 route has NO
                AVAILABLE EXECUTOR: 0 ACTIVE leases → no ACTIVE_ORCHESTRATOR to choose a
                reviewer, and 0 VERIFIED capabilities in any actor of any role
🔴 THIS RECORD  is a PRODUCER artifact by an author whose role contract is non-binding, closing
                under a dispatch whose NEXT_OWNER/NEXT_TRANSITION vocabulary the repository
                labels external. Mirror should attack § 15 first
```

### 15.6 · Lease orphan — task terminal while lease remains ACTIVE

```
🔴 NO COUPLING EXISTS between lease lifecycle and task lifecycle. Verified across I.3, D.3, D.4,
   § 12, § 48, A.5 and the lease record: the two surfaces never reference each other
ONLY BOUND      EXPIRES_AT, and only at the NEXT CONSULTATION
OBSERVED        lease #3: acquired 12:24:11Z, never renewed, never used, expired 13:04:11Z,
                GATE 0 never asserted. PREVENTED: no — "nothing executes between turns, so the
                window itself is unwatched"
NARROWER THAN   EXPIRED_WITHOUT_RENEWAL ≠ unused. #2, #4 and #5 were never renewed and each held
IT LOOKS        a canonical batch. Renewal is a proxy for use and a poor one
VOCABULARY      lease #3 stored `EXPIRED`, which is not in I.3's ACTIVE|STALE|RELEASED
DRIFT           — same class as DEFERRED/RESOLVED in the J.3 queue (§ 3.6)
STRUCTURAL      main #1–#5 vs orchestrator #1–#8, permanently, by § P5.1's own analysis
SELF-NAMED      the record names the P7 event ledger with LEASE_ACQUIRED/LEASE_STALE as its own
REMEDY          closure, "OWED NOT BARRED" — and Mirror reached the same conclusion independently
                (HANDOFF-ROLE-CONTRACTS-001, open question 8)
REPRODUCE       python3 framework/scripts/lease_state.py --check
```

---

## 16 · WHAT THIS RECORD DOES NOT DO

Does not: design a queue · create a control plane · create a ledger · create an event type ·
create a state machine · alter lease semantics · invent a timeout · invent a retry value · invent
an iteration number · open a `CAND` · write a `DEC` · amend a contract · resolve any finding ·
classify a future candidate's `change_class` · determine § P7's normative standing · determine
`cross_session_transport.md`'s normative standing · resolve `MIRROR_RETROSPECTIVE` cadence `N` ·
assign a reviewer (Orchestrator's act under G.2/C.3) · elect a recipient · claim routing is solved
· commit the five untracked analyses of § 2.4 · advance `main` · perform Mirror's adjudication ·
verify the advisory's SHA256 · convert any local dispatch label into governed vocabulary.

`SESSION_ROUTING_DEBT` remains real and out of scope, exactly as `APR-20260819-XPORT-001` records
it. `main` was observed at `788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5` and not moved.

---

## 17 · VERIFICATION TRAIL

| # | check | command | result |
|---|---|---|---|
| 1 | HEAD | `git rev-parse HEAD` | `b72af2f25d42c3cafb781d42b66ef3a1761cdb66` |
| 2 | supplied ref point | `git merge-base --is-ancestor b14a0d1 HEAD` | TRUE — ancestor, **7 commits behind HEAD** |
| 3 | ref population | `git for-each-ref` | 57 total → **52 content** (43 heads · 4 remotes · 5 tags) |
| 4 | J.1 type count | parsed from § J.1 at HEAD | **23** — supplied figure reproduces |
| 5 | `ledger/events/` | 52-ref sweep | **0 files** · control `ledger/checkpoints/` **450** ✅ |
| 6 | `ledger/consolidated/` | 52-ref sweep | **0 files** · same control ✅ |
| 7 | event emission | `git grep -l '"EVENT_TYPE"\|"EVENT_ID"'` × 52 | **0** · control `"CHECKPOINT_ID"` **450** ✅ |
| 8 | `.jsonl` under `ledger/` | 52-ref sweep | **1 path** — the J.3 approval queue |
| 9 | task records | 52-ref sweep + JSON parse | **5**, all `ledger/tasks/plan/`, all `OWNER=plan`, all `claimed_by=plan`; 3/5 carry `TASK_ACK`, all self-written |
| 10 | approval queue fork | `git rev-parse` × 3 refs + `cmp` prefix tests | **3 lineages**; `orchestrator`(10) and `evidence-index`(14) both extend the 6-line base and **neither is a prefix of the other** |
| 11 | queue vocabulary | JSON parse of the 14-line lineage | `DEFERRED`, `RESOLVED` — 🔴 outside J.3's `STATE` set |
| 12 | lease state | `python3 framework/scripts/lease_state.py --check` | **ACTIVE by derivation: 0**; 2 findings on lease #3 |
| 13 | lease TTL | grep governance + `lease_state.py` | 🔴 **no governed value**; observed windows 2/40/40/60/60 min |
| 14 | `HANDOFF v2.1` | `git grep -l` × 52 | **0** · control `AUTHOR_RESPONSE` **268** ✅ |
| 15 | `NEXT_OWNER` / `NEXT_TRANSITION` | `git grep -n` × 52 | **12 hits**, and Mirror + Plan both label the vocabulary **external** |
| 16 | `scope_lock` · `VERIFIED_CLOSURE` · `ACTOR_ACK` · `DELEGABLE_HUMAN_INTERVENTIONS` | `git grep -li` × 52 | **0 each** · control `ORCHESTRATOR_LEASE` **515** ✅ |
| 17 | `ITERATION` | `git grep -lw` × 52 | **5** · control `GENERATION` **787** ✅ |
| 18 | roster (J.2) | 52-ref filename sweep | **0** · control `*registry*` **5 paths** ✅ |
| 19 | `active_lessons/` | 52-ref sweep | **0 files** |
| 20 | advisory artifact | 1122 distinct blobs sha256'd + working tree scan | 🔴 **NO MATCH** for `70c8b312…e68a1`; id strings **0** · control `ADVISORY-FABLE` **109** ✅ |
| 21 | § P7 stability | `sed`-extracted § P7, sha256 per ref | **identical (`5ef9956ab8e5c039`) on all 27 refs carrying the file** |
| 22 | § P7 normative standing | `git log --all -S'status: NORMATIVE' -- governance/plan_defined_parameters.md` | **empty** — never activated |
| 23 | XPORT activation conditions | `git merge-base --is-ancestor e839db38 main` + `APR-20260819-XPORT-001` + `REV-XPORT-MIRROR-002` | all three **satisfied**; status line **unchanged** on all 16 refs (blob `49b7b63a05dc`) |
| 24 | LINT | `python3 framework/scripts/legend_lint.py .` | **PASS** (1 INFO, pre-existing) |
| 25 | receipts | `python3 framework/scripts/fulltext_receipts.py verify` | **OK** — 128 chained, tail anchored |
| 26 | `main` untouched | `git rev-parse main` | `788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5` — unchanged |
| 27 | instrument check | `for w in $X` vs `for w in ${=X}` in zsh | zsh does **not** word-split; the first form silently returned ABSENT on every ref. All sweeps re-run with `${=…}` and positive controls |

---

**Prepared by:** `plan`, worktree `evidence-index`, branch `plan-orchsurf-r4-transcription`,
2026-08-23 — under the operator's dispatch, **not** under the authority of `roles/plan.md`.

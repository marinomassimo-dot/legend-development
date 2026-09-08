---
artifact: PREPARATION RECORD — Scientist execution pipeline, prepared not activated
record_id: SCIENTIFIC-PIPELINE-PREPARATION-001
task_id: SCIENTIFIC_PIPELINE_PREPARATION_v1
iteration: 1/3
dispatcher: operator
author_session: root checkout, branch `main`, no ACTIVE lease
actor_id: NOT ESTABLISHED — see § 1. This record is not authored under a role contract.
date: 2026-08-22
governance_version: 3.1.1 (read, not exercised)
classification:
  - PREPARATION ONLY
  - NOT GOVERNANCE
  - NOT EXECUTION AUTHORIZATION
domain: >
  CONTENT. `learning/` is content by intent, declared in the P5.1 amendment and stated in
  SLR-plan-0001's frontmatter: it "moves the candidate hash exactly as the declaration says it
  must." CONTROL_PLANE_ROOTS (plan_defined_parameters.md § P5.1) are exhaustively
  `governance/candidates/`, `ledger/`, `reviews/` — `learning/` is not among them.
  This record therefore advances `main` and will sit inside the CANDIDATE_CONTENT_HASH of any
  future candidate that re-aligns onto `main`.
not_an_slr: >
  This is NOT a Session Learning Record. It sits in a directory whose other occupants (on branch
  `orchestrator`) are all `SLR-*`. Annex E.6 governs those; it does not govern this. The name is
  deliberately not `SLR-` so the two are not conflated.
authority_claimed: none
---

# SCIENTIFIC PIPELINE PREPARATION — 001

> **PREPARATION ONLY · NOT GOVERNANCE · NOT EXECUTION AUTHORIZATION**
>
> Nothing in this record assigns work, activates a contract, confers authority, resolves a
> finding, or authorizes a Scientist session to open. It describes a flow that **could** be run
> once other people have made decisions that are not made here and are not made by me.

---

## 1 · Identity — established from repository evidence, not from the dispatch

The dispatch addressed this session as Orchestrator. **Identity is not inherited from a
dispatch**, and the repository's own evidence does not support the claim.

| Fact | Measured value | How |
|---|---|---|
| Working directory | `<REPO_ROOT>` | `git rev-parse --show-toplevel` |
| Branch | `main` | `git rev-parse --abbrev-ref HEAD` |
| HEAD | `2bb270050d76264a13c8d595bc585ccde3b09ff3` | `git rev-parse HEAD` |
| Working tree | **clean** (before this record) | `git status --porcelain` → empty |
| Lease | **`ACTIVE by derivation: 0`** — 5 leases, all STALE or RELEASED; most recent released `2026-08-18T14:05:20Z` | `python3 framework/scripts/lease_state.py` |
| Runtime inventory | **absent on this ref**; exists at `runtime/runtime_inventory.md` on branch `orchestrator` | `find`, `git ls-tree` |
| `ACTOR_ID` | **not established** | no registration record for this session exists |
| `SESSION_REF` | **not observable** — and not invented (`scientist_reading_modes.md` § 1.2: no actor observes its own SESSION_REF) | — |

### 1.1 · The consequence, stated plainly

`CLAUDE.md` § 0 is unconditional:

```
IF no valid runtime inventory / no ACTIVE ORCHESTRATOR_LEASE:
    ENTER BOOTSTRAP_MODE.
    Do NOT assume Orchestrator authority merely because you are in root.
```

Both antecedents hold. **This session is in `BOOTSTRAP_MODE` and is not Orchestrator.**

`roles/orchestrator.md` says the same thing from the other side — *"Position in the root confers
nothing … A chat that opens in the root and finds a valid ACTIVE lease is not Orchestrator"* —
but that contract **is itself non-binding** (§ 3.2 below), so it is cited as agreement, not as
the source of the rule. The operative source is `CLAUDE.md` § 0 and Annex I.3.

The dispatch anticipated this: *"If authority is unavailable, continue only in preparation
mode."* That is the mode this record was produced in.

---

## 2 · Surface map

### 2.1 · Refs surveyed

All 41 local heads enumerated via `git for-each-ref refs/heads`, plus `refs/remotes` and
`refs/tags`. Cross-ref searches ran over every head, not only `main`.

Worktrees present (16, via `git worktree list`), the Scientist-relevant ones:

| Worktree | Branch | HEAD |
|---|---|---|
| root | `main` | `2bb2700` |
| `.claude/worktrees/lettore` | `lettore` | `9b0cf47` |
| `.claude/worktrees/lettore-b` | `lettore-b` | `cb50e17` |
| `.claude/worktrees/lettore-c` | `lettore-c` | `908197b` |
| `.claude/worktrees/mirror` | `mirror` | `1892071` |
| `.claude/worktrees/orchestrator` | `orchestrator` | `1e2fabd` |
| `.claude/worktrees/evidence-index` | `plan-orchsurf-r4-transcription` | `2e22c48` |

### 2.2 · Scientist-related objects — present on `main`

**MEASURED_AT: `main` @ `2bb270050d76264a13c8d595bc585ccde3b09ff3`**

| Object | Kind |
|---|---|
| `roles/scientist.md` | role contract, A/B/C share one file |
| `framework/protocols/scientist_reading_modes.md` | protocol `SCIENTIST_READING_MODES` v1 |
| `framework/protocols/controlled_benchmark_ab.md` | benchmark protocol `BENCH-AB-001` |
| `framework/eval/benchmarks/BENCH-AB-001/instructions/ASSIGNMENT.scientist-{a,b}.md` | per-actor benchmark inputs |
| `governance/candidates/CAND-20260818-SCIENTIST-AB-SPEC.md` | candidate manifest, revision 6 |
| `governance/candidates/HANDOFF-SCIENTIST-AB-SPEC.md` | operator scope |
| `ledger/tasks/plan/SCIENTIST-AB-SPEC-001.json` | task record |
| `reviews/plan/AUTHOR-RESPONSE-SCIAB-MIRROR-006.md` | author response |
| `governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` | operator determination, dated today |

### 2.3 · Objects that are cross-ref only — NOT_FOUND here does NOT mean NOT_EXIST

**MEASURED_AT: `main` @ `2bb2700`** for every "absent" cell below.

| Object | On `main` | Actually lives at |
|---|---|---|
| `learning/orchestrator/` | **absent** | branch `orchestrator` — 11 files, all `SLR-*` |
| `runtime/runtime_inventory.md` | **absent** | branch `orchestrator` |
| `REV-SCIAB-MIRROR-001…006` | **absent** | branch `mirror`, `reviews/mirror/` |
| `REV-ROLES-MIRROR-001` | **absent** | branch `mirror` (tip `1350477`) |
| `APR-20260819-SCIAB-001` / `RES-20260819-SCIAB-001` | **absent from `main`'s copy of the queue** | branch `orchestrator`, `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` line 8 |
| `PREP-*` candidate records | **absent** | branches `orchestrator-surface`, `plan-orchsurf-r4-transcription` |
| Agent Card registry | **absent** | branch `orchestrator`, `runtime/agent_card_registry.md` |

> 🔴 **The approval queue is ref-dependent, and that is load-bearing.** `main`'s copy has 6
> lines and ends at the GOV311 correction. The `orchestrator` copy has ≥10 and carries the
> SCIAB, XPORT and P5DOMAIN approvals. **A conclusion drawn from `main`'s queue alone about
> whether something was approved will be wrong.** I made that error mid-survey and corrected it
> only by searching every ref; it is recorded here so the next reader does not repeat it.

### 2.4 · Absent from every ref

**MEASURED_AT: all 41 local heads, surveyed `2026-08-22`**

| Concept | Result |
|---|---|
| `Q-1` | **zero occurrences on any ref**, any file type |
| `learning/orchestrator/` on `main` | absent (see 2.3) |
| an activation record for any role contract | none — `status: ACTIVE` / `status: BINDING` never present in `roles/` on any ref |

---

## 3 · Dispatch validation

Every concept the dispatch named, checked against repository evidence.

### 3.1 · Summary table

| Concept | Repository source | Identifier | Status |
|---|---|---|---|
| **Orchestrator** | `governance/annex_h_authority_matrix.md` § H.1; Annex I.3; `roles/orchestrator.md` | `orchestrator` | **DEFINED · role contract NON-BINDING · 0 ACTIVE leases** |
| **Scientist A** | `roles/scientist.md`; `scientist_reading_modes.md` § 1.1 | `scientist-a` (`lettore`) | **DEFINED · ACTOR_ID fixed by a protocol whose own binding is unresolved (§ 3.3)** |
| **Scientist B** | same | `scientist-b` (`lettore-b`) | **DEFINED · same qualification** |
| **Scientist C** | `GOVERNANCE_v3.1.1.md` § 32; `roles/scientist.md` frontmatter | `scientist-c` (`lettore-c`) | **DEFINED as an actor · ACTOR_ID `PROPOSED` · the dispatch's *function* for it is NOT repository-defined (§ 3.4)** |
| **Mirror review** | `governance/annex_g_mirror.md`; `annex_c_review_protocol.md` § C.2; `roles/mirror.md` | `mirror` | **DEFINED · role contract NON-BINDING · annexes bind independently** |
| **blind review** | `controlled_benchmark_ab.md` §§ 4, 7; `.claude/skills/legend-locator-audit` | blind first pass; blind locator audit | **DEFINED — and narrower than the dispatch's usage (§ 3.5)** |
| **handoff** | `annex_b_message_protocol.md` § B.2 (`HANDOFF` message type); `scientist_reading_modes.md` § 3.7 | `HANDOFF`, `TASK_COMPLETE` + `DURABLE_POINTER` | **DEFINED** |
| **literature analysis** | — | — | **EXTERNAL VOCABULARY.** The repository's terms are `DEEP_DIVE`, `PRIMARY_EVIDENCE_READ`, `INDEPENDENT_CRITICAL_READ`, `INGEST`, `BATCH_COMMIT`. No object named "literature analysis" exists. |
| **evidence extraction** | — | — | **EXTERNAL VOCABULARY.** Nearest defined objects: the work manifest (`deepdive_manifest.py`), the dossier, `verbatim_locators.entries[]`. "Extraction" is not a repository term. |
| **evidence artifacts** | partially | the three surfaces of `scientist_reading_modes.md` § 3.5 | **PARTIALLY DEFINED** — the surfaces are exact; the umbrella phrase is external. |
| **Q-1** | — | — | **EXTERNAL VOCABULARY — zero occurrences on any ref.** The dispatch instructed me not to resolve it; I could not have, because nothing in this repository defines it. |

### 3.2 · Orchestrator, Scientist and Mirror role contracts are NON-BINDING

`governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md`, dated today, is an
operator determination under H.1. Its verdict:

> **OPTION B — `ACTIVATION_NOT_CONFIRMED`.** The existing records do not constitute activation
> of the four role contracts. The contracts remain `PROPOSED`.

Its consequence 2 is directly binding on how this record may be written:

> **No actor authority may be assumed from these contracts.** Any authority an actor exercises
> must be traced to the governance body or to a named annex — H.1 for the authority matrix, D
> for the commit path, C for the review ladder, I.3 for the lease — never to a role contract
> clause standing alone.

Everything below therefore cites **annexes and the body**, never a role contract, as the source
of a rule. Role contracts are cited only descriptively.

### 3.3 · 🔴 `scientist_reading_modes.md` — its activation condition measures as SATISFIED, and nobody has said so

The protocol's frontmatter states a **three-clause conjunction**:

```
status: PROPOSED — binding on canonical execution of CAND-20260818-SCIENTIST-AB-SPEC, after
  Mirror hostile review and HUMAN_APPROVAL. Until then it binds nobody.
```

Each clause, measured independently:

| Clause | Measurement | Result |
|---|---|---|
| canonical execution of `CAND-20260818-SCIENTIST-AB-SPEC` | `git merge-base --is-ancestor 4454feab main` → true; commit `4454fea` *"The Scientist A/B specification becomes canonical…"* | ✅ **SATISFIED** |
| Mirror hostile review passes | `REV-SCIAB-MIRROR-006` (branch `mirror`) → `verdict: ACCEPT`, per `AUTHOR-RESPONSE-SCIAB-MIRROR-006` frontmatter | ✅ **SATISFIED** |
| `HUMAN_APPROVAL` | `APR-20260819-SCIAB-001` / `RES-20260819-SCIAB-001`, `STATE: APPROVED`, `RESOLVED_BY: operator` — queue line 8 **on branch `orchestrator`** | ✅ **SATISFIED** |

**All three clauses hold. The status line still reads `PROPOSED` and has never been modified**
(`git log --all -S…` returns only the materialization commit `384f05f`).

> **This record does NOT decide that the protocol binds.** Deciding it is a `STATE_DETERMINATION`
> of exactly the kind `DEC-20260822` performed for `roles/`, and that decision sits with the
> operator under H.1. I measured the clauses; I did not rule on them. Two things make the ruling
> genuinely non-obvious and neither is mine to settle:
>
> 1. **The contrast with `roles/` is real, not a symmetry.** `roles/`'s condition *fails* — the
>    only hostile review of those four objects returned CHANGES_REQUIRED on three. This
>    protocol's condition *holds*. Same grammar, opposite measurement.
> 2. **But the protocol's `applies_to` is `every actor under roles/scientist.md`** — and
>    `roles/scientist.md` is non-binding. A binding protocol whose entire addressee set is
>    defined by a non-binding contract is a coupling nobody has adjudicated.
>
> **Recorded as an open observation for the operator. Not resolved here.**

### 3.4 · 🔴 The dispatch's Scientist C function contradicts § 32

The dispatch specifies:

```
Scientist A independent analysis
Scientist B independent analysis
Scientist C synthesis/conflict resolution
```

`GOVERNANCE_v3.1.1.md` § 32 (line 356) says the opposite about the actors:

> *Equivalenti: stesso mandato, protocollo, autorità scientifica, obblighi, isolation.
> **No specializzazioni statiche.*** Soft routing opzionale post-bootstrap sulle capabilities
> verificate … (segnale morbido, **guardia anti-fossilizzazione di Mirror**).

`roles/scientist.md` restates it, and `scientist_reading_modes.md` § 0 is built entirely around
holding this tension: *"The difference is a property of the task, not of the actor."* It adds
that a mode which stops rotating **has become** the static specialization § 32 forbids.

Two further collisions with the dispatch's wording, both against annexes (which bind
independently of role contracts):

| Dispatch phrase | Collides with | Source |
|---|---|---|
| Scientist C performs **conflict resolution** | *Aggiudicazione challenge → **Orchestrator** (con rationale)*; *disaccordo scientifico persistente → floor **R3 TRIADIC*** | H.1; Annex C.1 |
| Scientist C performs **synthesis** toward agreement | *Forced consensus is an error.* `INFERENCE_A + INFERENCE_B + DISAGREEMENT_UNRESOLVED`, explained, is a **legitimate outcome** | body § 27, via `roles/scientist.md` |

**Handling.** The dispatch forbids changing workflow vocabulary, so I have not renamed anything
and have not quietly re-specified Scientist C into something § 32 permits. The model in § 4
carries the third position as a **task-level step with its function left open**, and both
readings are named. Which one is correct is an operator decision.

### 3.5 · "blind review" is defined, but narrower than the dispatch uses it

The repository defines two distinct blind objects, neither of which is a general "blind review":

- **blind first pass** (`controlled_benchmark_ab.md` § 4) — blindness is *a property of the
  corpus/surface*, not a promise by the reader. *"A first pass run in such a checkout is blind
  only by promise."* It is enforced by an enumerated, digested surface and a `verify --post-read`
  that prints its own blind spot by name.
- **blind locator audit** (`.claude/skills/legend-locator-audit`; benchmark protocol § 7, step 7)
  — fresh agents receive `(proposition, snippet, anchor)` triples plus the packet, and **never**
  the dossier or the reader's identity.

`MODE B` is explicitly **not** a review of `MODE A` (`scientist_reading_modes.md` § 5.4): *"a
second reader is a second reader."*

---

## 4 · `SCIENTIST_EXECUTION_MODEL` — prepared, not authorized

> Preconditions for **any** of this to run are listed in § 8. None is satisfied today.

### 4.1 · Flow

```
INPUT      selected studies (selection = human, § 8 · HT-1)
             │
             ├── Task Contract → OWNER: scientist-a  · MODE A · PRIMARY_EVIDENCE_READ
             └── Task Contract → OWNER: scientist-b  · MODE B · INDEPENDENT_CRITICAL_READ
                   both carry the SAME  PARALLEL_READ_GROUP   (else: DUPLICATED_ASSIGNMENT)
                   independent · no contact · no sight of the other's output
             │
             ▼
FREEZE     TASK_COMPLETE → outputs frozen before anyone else reads them
             │
             ▼
THIRD POSITION   ← function UNRESOLVED (§ 3.4). Two candidate readings, both recorded:
             (i)  a THIRD READING, same equivalence, a mode on a task — § 32-compatible
             (ii) synthesis/adjudication as the dispatch describes — collides with § 32 + H.1
             │
             ▼
OUTPUT     evidence artifacts · uncertainty · unresolved questions · disagreements
             │
             ▼
HANDOFF    → Mirror (process), and/or peer review under C.3, opened by Orchestrator only
```

### 4.2 · What each reading must produce — three surfaces, one data model

Verbatim from `scientist_reading_modes.md` § 3.5. **No parallel schema is invented here.**

| Surface | Artifact family | Validator |
|---|---|---|
| `READING PROVENANCE` | work manifest, `schema_version 2` | `deepdive_manifest.py --verify-artifacts --require-current-schema` |
| `LOCATOR FIDELITY` | dossier in `fulltext_dossiers/*.md` form — artifact table with SHA-256, verbatim quotes, surface, anchor | — |
| `CLAIM ASSERTION` | claim candidates in `claim_registry_current.md` section form (12 canonical fields) + the 7 BENCHMARK/INTERMEDIATE fields of § 6.2 + `Locators:` — **not written to the registry** | acceptance test step 4 |

MODE B produces additionally a **critical-reading record** (§ 5.3) — *"a fourth file, not a
fourth data model."*

The 7 BENCHMARK/INTERMEDIATE fields exist because they have **no canonical home** today:
`UNCERTAINTY`, `LIMITATIONS`, `CONTRADICTORY_EVIDENCE`, `OBSERVATION`, `AUTHOR_INTERPRETATION`,
`LEGEND_INTERPRETATION`, `DIRECTION` — each measured at 0/39 as a label in the claim registry.

### 4.3 · Uncertainty and unresolved questions are outputs, not residue

- *"Unresolved ambiguity is a legitimate output"* — § 3.4. It is recorded, **not** resolved by
  choosing the more interesting reading.
- A reading is complete only when unresolved ambiguities are **listed rather than absent**
  (§ 3.6).
- Every negative or rejection carries a `PREMISE` tag and a `REVIVAL_TRIGGER`
  (`epistemic_discipline.md`).
- MODE B: every mandatory critical axis has findings **or** an explicit *"searched, none found"*
  with what was searched. *"Silence on an axis is incompleteness, not a null result."*

### 4.4 · Completion — the mechanical gate (§ 3.6, § 3.8)

```
1  deepdive_manifest.py … --verify-artifacts --require-current-schema   → PASS
2  every locator's artifact inside the declared packet, digest matches
3  coverage map: no `not_read`
4  per claim candidate: 12 canonical + 7 benchmark fields + Locators
5  blind locator audit over every (proposition, snippet, anchor) triple
```

Steps 1–4 are mechanical. **Step 5 is the one that catches a careful reading that says more than
its source** — and it is the step that is skipped first under time pressure.

---

## 5 · `PAPER_DISTRIBUTION_MODEL` — principles only

> **No paper is assigned here. No partition is proposed. No actor is named against any source.**

### 5.1 · Partition principles (drawn from existing rules, not invented)

| # | Principle | Source |
|---|---|---|
| P1 | Every reading Task Contract names **exactly one `OWNER`** (ACTOR_ID) and the sources it covers. Ownership is **never** inferred from a worktree, a branch, or a file someone has open. | § 2.2 rule 1 |
| P2 | Two contracts on one source are legal **only** under a declared shared `PARALLEL_READ_GROUP`. Without one → `DUPLICATED_ASSIGNMENT`. | § 2.2 rule 2 |
| P3 | `PARALLEL_READ_GROUP` is an **extension field** on the Annex A.1 schema, introduced by protocol. A.1 declares its minimum fields *extendible, never removable*. Promotion into Annex A is a separate governed change. | § 2.2 rule 2 |
| P4 | Batch size for a first cycle: **PICCOLO — 1–2 PMID each**. Full throughput only from the second batch. | body § 41 |
| P5 | Assignment presupposes **VERIFIED** capabilities. All six Scientist capabilities are `UNVERIFIED`; L2 is **SUSPENDED** by the C-9 hold (operator, 2026-08-17). | body § 8; Annex I.4; `controlled_benchmark_ab.md` P-3 |
| P6 | No double work with the Codex worktrees — the queue is drawn from durable state. | body § 41 |
| P7 | PMID 42422765 is special-cased: the first contract naming it **must cite** `HANDOFF-C-2-PMID42422765` and state single-owner vs `PARALLEL_READ_GROUP` member. A contract omitting the citation is **refusable by the actor**. | § 2.4 |

### 5.2 · Preserving independence in duplicate analysis

Independence is a property of the **surface**, not of a promise:

- The reader works **in the enumerated surface**, not in its LEGEND worktree, because a LEGEND
  checkout contains prior outputs and cross-referencing manifests. *"A first pass run in such a
  checkout is blind only by promise."*
- The blind path must be the **default** path and the only one that leaves the required evidence.
- Three checks: pre-handover, freeze, and `verify --post-read` — which prints its own **blind
  spot** by name on every run, because the blind spot is a post-read object and cannot be
  checked by the same predicate as everything else.

### 5.3 · Avoiding contamination between Scientist actors

Forbidden in both modes, verbatim from § 3.3:

- reading the other reader's output, or **any** prior LEGEND output on the paper, during a
  declared blind first pass;
- contacting the other reader during the first pass, **or asking Orchestrator to relay content**
  — *"the same, by another channel."*

Detection, and the honest word for it (§ 2.3): **there is no lock** (Annex J.0). The rule
guarantees uniqueness *by construction of the records* — a duplication cannot exist without
leaving two records that contradict each other, and both the actor (before `TASK_CLAIM`) and
Plan (at reconciliation) look at those records at defined moments. **It does not guarantee that
nobody opens the same PDF twice.**

---

## 6 · `SCIENTIST_HANDOFF_FORMAT` — proposed information flow

> **These are not routing rules.** No `SendMessage` resolution, no session registry, no
> supersession semantics. The session-routing debt (`CAND-20260818` § 5c) is **untouched** —
> named there as a real gap between stable `ACTOR_ID` and current routable `SESSION_REF`.

### 6.1 · Scientist → Orchestrator

Envelope is Annex B.1: `MESSAGE_ID / TASK_ID / ACTOR_ID / FROM / TO / TYPE / STATE_CHANGE /
DURABLE_POINTER`. Type is `TASK_COMPLETE` (§ 3.7).

| Dispatch field | Carried as | Source |
|---|---|---|
| completed object | `DURABLE_POINTER` to the output tree + its **tree digest** | § 3.7 |
| evidence status | the manifest validator's **verdict line** + the **coverage map** | § 3.7 |
| unresolved items | the listed ambiguities; MODE B's critical-reading record entries | § 3.4, § 5.3 |
| remaining workload | *no defined carrier exists* — see § 6.3 | — |

`ACTOR_ID` is identity; `FROM` is routing. Nothing in a completion, claim, checkpoint or receipt
is keyed by `SESSION_REF` — all are keyed by `ACTOR_ID + TASK_ID + GENERATION` (§ 1.2).

Under a benchmark, completion is declared to **Plan for freezing** before anyone else reads it.

### 6.2 · Orchestrator → Scientist

`TASK_ASSIGNMENT` under Annex A.1, then `TASK_ACK`, then a durable `TASK_CLAIM` before any work.
`ACK` is mandatory on `STATE_CHANGE: yes`; absent → resend (dedup via `MESSAGE_ID`); second
failure → `BLOCKER`.

The measured failure class is recorded in B.3 and is not hypothetical:

```
FAILURE:    ACK emesso ma lavoro mai partito (classi misurate: turno troncato, permission prompt)
RECOVERY:   DIAGNOSE (Annex F.4) — mai classificare come rifiuto un guasto di runtime
```

Before claiming, the actor **queries the receipt ledger and the task ledger** for the source; an
existing reading or open contract without a shared group → **do not claim**, raise `BLOCKER`
naming both records (§ 2.2 rule 3).

### 6.3 · 🔴 Gap — "remaining workload" has no carrier

The dispatch asks the Scientist to report remaining workload. **No Annex B message type and no
Annex A field carries it.** Nearest existing instruments: `STATUS_UPDATE`, `HEARTBEAT` (fixed
cadence, feeds the DOWN timeout), and Plan's reconciliation over `ledger/tasks/*/`.

Creating a carrier would be a schema change. **Not done here.** Recorded as a gap.

---

## 7 · `MIRROR_EVALUATION_INPUT` — what Mirror would need

> **No Mirror task is created, scheduled, scoped or requested here.**

### 7.1 · Mirror's object is the process, not the paper

| | MODE B | Mirror |
|---|---|---|
| Object | the **paper** | the **process** — how the laboratory reasoned, reviewed, recorded |
| Sees both readings? | no, during a blind first pass | **yes, after freezing** |
| Output | a reading with a critical record | a review under C.2; adjudication of the **method** |

Mirror holds **no command** over any actor and produces **no primary evidence**. Its review of
Orchestrator is **ex post and pattern-based — never a veto before the fact**.

### 7.2 · Inputs Mirror would require after Scientist completion

| Input | Concrete form | Available? |
|---|---|---|
| evidence artifacts | the three frozen surfaces per reading (§ 4.2) | yes, once a reading exists |
| reasoning traces | work manifest `verbatim_locators.entries[]` with `panel_text_relation`, `found_or_sought`, `contradicts`/`qualifies`; MODE B's critical record with `what would resolve it` | yes — this **is** the trace |
| uncertainty | the 7 BENCHMARK/INTERMEDIATE fields; listed ambiguities; `RESIDUAL_UNCERTAINTY` in C.2 | partial — no canonical registry home |
| disagreements between Scientist outputs | divergence between frozen A and B outputs; `UNRESOLVED_CONFLICT` (B.2) | yes, structurally |
| the primary analysis surface | **the consolidated event ledger (J.1)** — *not* by reading fifty chats | ⚠️ **see § 7.3** |

### 7.3 · 🔴 Two preconditions on Mirror's own input are not satisfied

1. **Annex G.3 makes the consolidated `EVENT LEDGER` (J.1) Mirror's primary analysis surface.**
   The dispatch forbids defining a ledger schema, so I have not — and I note that Mirror's
   stated surface depends on an instrument whose state I did not verify as operational.
2. **`REV-ROLES-MIRROR-001`'s `AUTHOR_RESPONSE` is required and outstanding**
   (`DEC-20260822`, consequence 5). Annex C.2: **silence is not acceptance.**

Also standing: Mirror **may not self-approve** changes to its own rubric, learning clustering,
active-learning selection, review-yield or autonomy-classification methodology (G.2), and
`roles/mirror.md` received **no verdict** in `REV-ROLES-MIRROR-001` under the self-review
prohibition.

---

## 8 · `HUMAN_TOUCHPOINT_MAP`

> Human involvement is **not** reduced by assumption. Where a touchpoint could plausibly be
> automated later, that is recorded as a question, never as a plan.

### 8.1 · Genuinely required — structural, not incidental

| # | Touchpoint | Why it cannot be delegated | Source |
|---|---|---|---|
| **HT-1** | **Scientific priority** — which studies, in what order | *Strategia complessiva → Operatore.* Orchestrator sets order **within** an authorized scope; it does not set the scope. | H.1 |
| **HT-2** | **Governance decisions / MAJOR approval / spend** | *Spese / MAJOR approval / governance → Operatore.* | H.1 |
| **HT-3** | **Role contract activation** | `DEC-20260822` consequence 3: *"A new, explicit activation act is required."* It *"does not perform it, does not schedule it, and does not specify its form."* | `DEC-20260822` |
| **HT-4** | **Whether the third position exists, and what it does** | The dispatch's function for Scientist C contradicts § 32 and H.1 (§ 3.4). An actor choosing its own reading here is the convenient interpretation the gate exists to prevent. | § 32; H.1 |
| **HT-5** | **Lifting the C-9 hold on L2 capability verification** | L2 is **SUSPENDED** by operator hold (2026-08-17). All six capabilities `UNVERIFIED`. Assignment requires VERIFIED. | `controlled_benchmark_ab.md` P-3 |
| **HT-6** | **`scientist-c` ACTOR_ID confirmation** | `PROPOSED — confirmed at its own registration` (I.2 step 7, PID-12). Not fixed by materialization. | `roles/scientist.md`; PID-12 |
| **HT-7** | **Persistent scientific disagreement** | Floor **R3 TRIADIC**; derogable only upward. Forced consensus is an error. | C.1; body § 27 |
| **HT-8** | **Public push** | *"No governance artifact may reach a public push without `public_release_gate.py`, and — per the root CLAUDE.md — without a human reading `git diff origin/main..main --stat`, **which is the one judgement no gate makes**."* | `materialization_log.md` |
| **HT-9** | **`AUTHOR_RESPONSE` to `REV-ROLES-MIRROR-001`** | Owed by the author; silence is not acceptance. | C.2; `DEC-20260822` |
| **HT-10** | **Anything therapeutic** | Nothing here is medical advice; therapeutic output supports discussion with a treating clinical team and never substitutes for one. | `CLAUDE.md` |

### 8.2 · Not a human touchpoint — mechanical, and should stay that way

Manifest validation · locator digest matching · coverage-map completeness · LINT · receipt-chain
verification · release gate · lease derivation · duplicate-assignment detection at reconciliation.

**Caveat.** `lease_state.py`'s own documentation is explicit that the `PROCEDURAL` layer —
*writing a row at all* — is not mechanized: *"Nothing compels the Orchestrator to record an
acquisition, and nothing runs between turns."* Mechanical checks derive correctly from what they
are given and **cannot derive from what was never written down.**

### 8.3 · The honest accounting

Of the ten touchpoints in § 8.1, **six (HT-3 … HT-6, HT-9, and HT-4) are one-time unblocking
decisions**, not per-batch costs. HT-1, HT-2, HT-7 and HT-8 recur per batch. The dispatch's goal
— *"Scientist execution can start with minimal human coordination"* — is reachable **for the
recurring set**, and only after the one-time set is discharged by someone with the authority to
discharge it. **That authority is not held by this session.**

---

## 9 · Open observations — recorded, not resolved

Each is a fact I measured that someone with authority must dispose of. **None is resolved here,
and none is assigned to anyone.**

| # | Observation | Disposition owner |
|---|---|---|
| **O-1** | `scientist_reading_modes.md`'s three activation clauses all measure SATISFIED, while its status line still reads `PROPOSED` and has never been modified (§ 3.3). | operator (H.1) |
| **O-2** | That protocol's `applies_to` set is defined by `roles/scientist.md`, which is non-binding — a binding protocol with a non-binding addressee set. | operator (H.1) |
| **O-3** | The dispatch's Scientist C function contradicts § 32 equivalence, H.1 adjudication authority, and body § 27 on forced consensus (§ 3.4). | operator |
| **O-4** | `HUMAN_APPROVAL_QUEUE.jsonl` diverges by ref: `main` has 6 lines, `orchestrator` ≥10 including SCIAB/XPORT/P5DOMAIN approvals. Approval state read from `main` alone is wrong (§ 2.3). | Plan / operator |
| **O-5** | `materialization_log.md` records `lettore-c` **absent**; it is present today as a worktree on branch `lettore-c`. The log's measurement is dated 2026-08-16 and is superseded by observation, not by correction. | Plan |
| **O-6** | No carrier exists for "remaining workload" in Annex A or B (§ 6.3). | Plan (schema) / operator |
| **O-7** | `Q-1` — named by the dispatch, zero occurrences on any of 41 refs. External vocabulary, or a concept that has never been written down. | dispatcher |
| **O-8** | `learning/orchestrator/` exists on branch `orchestrator` with a single-writer convention (`SLR-*`). This record lands at the same path on `main`. **Merge-collision risk at that seat is real and is not mitigated here** (§ 10.2). | Plan / operator |

---

## 10 · Validation of this record

### 10.1 · Constraint compliance

| Constraint | Result |
|---|---|
| no Scientist actor dispatched | ✅ no `Agent`/`SendMessage` call was made |
| no papers assigned | ✅ no source named against any actor |
| no scientific paper read | ✅ no full text opened; no receipt written |
| no scientific conclusion created | ✅ zero claims, zero candidates |
| governance not modified | ✅ `governance/` untouched |
| roles not modified | ✅ `roles/` untouched |
| framework not modified | ✅ `framework/` untouched |
| ledger not modified | ✅ `ledger/` untouched |
| no contract activated | ✅ § 3.2 observed; O-1 recorded, not acted on |
| no ledger event created | ✅ no append to any `.jsonl` |
| no routing rules created | ✅ § 6 preamble; routing debt untouched |
| no `CANDIDATE` object created | ✅ nothing under `governance/candidates/` |
| Q-1 not resolved | ✅ and could not be — O-7 |
| Orchestrator authority not assumed | ✅ § 1.1; every rule cited from body/annex, never from a role contract |
| **only the declared preparation artifact changed** | ✅ exactly one new file |

### 10.2 · Domain and collision disclosure

- **Content domain.** `learning/` is content by intent (P5.1 amendment; `SLR-plan-0001`
  frontmatter). This record **moves the candidate content hash** of any future candidate that
  re-aligns onto `main`, and this commit advances `main`.
- **Base-condition check.** The most recent candidate `BASE_HEAD` observed is `4454feab`
  (`CAND-20260819-XPORT`), already behind `main` at `2bb2700`. **No open candidate declares
  `2bb2700` as its `BASE_HEAD`**, so no candidate's base condition is invalidated by this commit.
- **Seat collision (O-8).** `learning/orchestrator/` is occupied on branch `orchestrator` by 11
  `SLR-*` files. This record introduces the same directory on `main` with a **non-`SLR`** name,
  chosen so the two do not collide by filename and so this record is not mistaken for a Session
  Learning Record under Annex E.6. **Directory-level convergence at merge remains an open risk
  and is flagged, not solved.**

### 10.3 · Gates re-run after writing

Recorded in the session response, not transcribed here, so this file does not assert a result it
cannot itself re-derive.

---

## 11 · What this record does NOT do

- It does **not** activate any role contract, or perform the act `DEC-20260822` consequence 3
  requires.
- It does **not** confer, claim or imply Orchestrator authority.
- It does **not** assign a paper, an actor, a batch or a review.
- It does **not** resolve O-1 … O-8.
- It does **not** create a Task Contract, a `PARALLEL_READ_GROUP`, a Mirror task, or a ledger
  event.
- It does **not** verify any capability, or lift the C-9 hold.
- It does **not** constitute an `AUTHOR_RESPONSE` to anything.
- It is **not** a `WORK_COMMIT` and **not** a `CANONICAL_BATCH_COMMIT`.

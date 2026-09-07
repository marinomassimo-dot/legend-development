---
artifact: ARCHITECTURE ANALYSIS — scientific workload orchestration and the dispatch loop,
  assessed against measured repository state
record_id: ORCHESTRATOR-SCIENTIFIC-PIPELINE-AND-LOOP-ARCHITECTURE-ANALYSIS-001
task_id: ORCHESTRATOR-SCIENTIFIC-PIPELINE-AND-LOOP-ARCHITECTURE-ANALYSIS-001
iteration: 1/3
dispatcher: operator
date: 2026-08-22
author_session: root checkout at analysis; artifact written on branch
  `orch-pipeline-loop-architecture`, based on `main` @ 788c357
actor_id: NOT ESTABLISHED — see § 1. This record is not authored under a role contract.
governance_version: 3.1.1 (read, not exercised)
classification:
  - ARCHITECTURE ANALYSIS ONLY
  - NOT AN IMPLEMENTATION PROPOSAL
  - NOT GOVERNANCE
  - NOT EXECUTION AUTHORIZATION
authority_claimed: none
domain: >
  CONTENT. `learning/` is content by intent: CONTROL_PLANE_ROOTS
  (`governance/plan_defined_parameters.md` § P5.1) are exhaustively `governance/candidates/`
  and `ledger/` as measured at `main` @ 788c357 — `learning/` is not among them. This record
  therefore sits inside the CANDIDATE_CONTENT_HASH of any future candidate that re-aligns onto
  the branch carrying it.
not_an_slr: >
  This is NOT a Session Learning Record. Annex E.6 governs those. The name is deliberately not
  `SLR-` so the two are not conflated, following the precedent set by
  SCIENTIFIC-PIPELINE-PREPARATION-001 at the same seat.
branch_rationale: >
  The dispatch's VALIDATION BEFORE COMMIT requires `main unchanged`. `main` is therefore not
  written. The artifact lands on its own branch under H.1 `WORK_COMMIT` — "ogni attore, solo
  proprio branch" — which requires no lease.
supersedes: nothing
corrects: >
  Two measurements in learning/orchestrator/SCIENTIFIC-PIPELINE-PREPARATION-001.md — O-7 (Q-1)
  and O-4 (approval-queue divergence). See § 3.4. Neither correction is an amendment: that
  record is not edited, and both corrections are recorded here as new measurements.
---

# SCIENTIFIC PIPELINE AND LOOP ARCHITECTURE — ANALYSIS 001

> **ARCHITECTURE ANALYSIS ONLY.** Nothing here defines a workflow, adopts an architecture,
> creates a task, assigns an actor, activates a contract, resolves a finding, confers authority,
> or recommends a course of action. It describes what the repository has, what it does not have,
> and what the difference implies for the transition the dispatch names.

---

## 1 · Identity

### 1.1 · Established from repository evidence, not from the dispatch

The dispatch addressed this session as Orchestrator. **Identity is not inherited from a
dispatch.** Every field below was measured in this session.

| Fact | Measured value | How |
|---|---|---|
| Working directory (analysis) | `<REPO_ROOT>` | `git rev-parse --show-toplevel` |
| Branch at analysis | `main` | `git rev-parse --abbrev-ref HEAD` |
| HEAD at analysis | `788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5` | `git rev-parse HEAD` |
| Working tree at analysis | **clean** | `git status --porcelain` → empty |
| Worktree this record is written in | `…/scratchpad/wt-orch-arch` | `git worktree add -b orch-pipeline-loop-architecture … main` |
| Branch this record is written on | `orch-pipeline-loop-architecture` | based on `main` @ `788c357` |
| **Lease** | 🔴 **`ACTIVE by derivation: 0`** — 5 records, all `STALE` or `RELEASED`; most recent released `2026-08-18T14:05:20Z` | `python3 framework/scripts/lease_state.py` |
| **Runtime inventory** | 🔴 **absent on this ref**; present at `runtime/runtime_inventory.md` on branch `orchestrator` | `git ls-tree` per ref |
| **Agent Card registry** | 🔴 **absent on this ref**; present at `runtime/agent_card_registry.md` on branch `orchestrator` only | `git ls-tree` per ref |
| `ACTOR_ID` | **not established** — no registration record exists for this session | `runtime/agent_card_registry.md` @ `orchestrator` |
| `SESSION_REF` | **not observable, and not invented** | `scientist_reading_modes.md` § 1.2 — no actor observes its own `SESSION_REF` |

Derivation output, reproduced rather than summarised:

```
now (derivation instant)  2026-08-22T16:33:23Z
  lease #1  derived=STALE     stored=STALE     expires=2026-08-18T09:40:25Z released=—
  lease #2  derived=RELEASED  stored=RELEASED  expires=2026-08-18T11:13:21Z released=2026-08-18T11:07:12Z
  lease #3  derived=STALE     stored=EXPIRED   expires=2026-08-18T13:04:11Z released=—
  lease #4  derived=RELEASED  stored=RELEASED  expires=2026-08-18T14:26:30Z released=2026-08-18T13:29:40Z
  lease #5  derived=RELEASED  stored=RELEASED  expires=2026-08-18T15:03:41Z released=2026-08-18T14:05:20Z
ACTIVE by derivation: 0
```

### 1.2 · Authority is missing, and this is what follows

`CLAUDE.md` § 0 is unconditional:

```
IF no valid runtime inventory / no ACTIVE ORCHESTRATOR_LEASE:
    ENTER BOOTSTRAP_MODE.
    Do NOT assume Orchestrator authority merely because you are in root.
```

**Both antecedents hold.** No runtime inventory is present on the analysed ref, and zero leases
derive `ACTIVE`. **This session is in `BOOTSTRAP_MODE` and is not Orchestrator.**

`roles/orchestrator.md` agrees — *"Position in the root confers nothing"* — but that contract is
itself non-binding (§ 3.2), so it is cited as agreement, never as the source of the rule. The
operative sources are `CLAUDE.md` § 0 and Annex I.3.

**Consequence for this record.** Every rule cited below is traced to `GOVERNANCE_v3.1.1.md` or to
a named annex. No role contract is cited as the source of any rule, per
`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` consequence 2.

### 1.3 · Available runtime information, declared

```
AVAILABLE     git object database (49 refs), 17 worktrees, the four runnable gates
              (§ 3.5), lease_state.py, the working tree at main@788c357
NOT AVAILABLE ACTOR_ID · SESSION_REF · a heartbeat · an event stream · any observation of
              another actor's liveness · any capability marked VERIFIED
NOT AVAILABLE the Agent Card registry and runtime inventory from this ref (they exist; see § 2.3)
```

---

## 2 · Surface map

### 2.1 · Refs surveyed

```
MEASURED_AT          ref  main
                     HEAD 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5
                     working tree clean, 2026-08-22
REFS PRESENT         49 total = 35 refs/heads · 4 refs/remotes · 5 refs/tags
                                · 4 refs/codex · 1 refs/stash
REFS TREE-SURVEYED   44 (refs/heads + refs/remotes + refs/tags), by `git ls-tree -r` per ref
NOT SURVEYED         refs/codex (4) · refs/stash (1) — content not enumerated
WORKTREES            17, via `git worktree list` (16 before this record's worktree was added)
SURFACE DELTA        this session added 1 branch and 1 worktree. The figures above are the ones
                     every claim below was measured against.
```

🔴 **Every absence claim in this record is scoped by that surface and by nothing wider.**
`NOT_FOUND` across 44 refs in this clone is not `NOT_EXIST` in a clone, a codex ref or a remote
this session cannot see. Where a claim is narrower than repository-wide, it says so.

### 2.2 · Worktrees relevant to the dispatch's named actors

| Worktree | Branch | HEAD |
|---|---|---|
| root | `main` | `788c357` |
| `.claude/worktrees/orchestrator` | `orchestrator` | `1e2fabd` |
| `.claude/worktrees/evidence-index` | `plan-orchsurf-r4-transcription` | `de0ae4e` |
| `.claude/worktrees/mirror` | `mirror` | `78dccaf` |
| `.claude/worktrees/lettore` | `lettore` | `9b0cf47` |
| `.claude/worktrees/lettore-b` | `lettore-b` | `cb50e17` |
| `.claude/worktrees/lettore-c` | `lettore-c` | `908197b` |

Four further worktrees are Codex checkouts outside `.claude/worktrees/`, and six are
session-scratchpad worktrees created by earlier analyses.

### 2.3 · Objects that are cross-ref only

**MEASURED_AT: `main` @ `788c357`** for every "absent" cell.

| Object | On `main` | Carried by |
|---|---|---|
| `runtime/agent_card_registry.md` | ❌ | `orchestrator` only |
| `runtime/runtime_inventory.md` | ❌ | `orchestrator` only |
| `learning/mirror/**` (34 files incl. `SLR-mirror-CORRECTION-MEMORY-ANALYSIS-001.md`) | ❌ | `mirror` only |
| `reviews/mirror/**` (49 files) | ❌ | `mirror` only |
| `learning/orchestrator/SLR-*` (11 files) | ❌ | `orchestrator` only |
| `governance/candidates/PROPOSAL-ORCH-STATE-RECONSTRUCTION.md` | ❌ | `orch-state-reconstruction` only |
| `governance/decisions/DEC-20260822-ORCH-STATE-RECONSTRUCTION-CANDIDATE.md` | ❌ | `operator-decision-orch-state-reconstruction` only |
| `reviews/orchestrator/AUTHOR-RESPONSE-ORCH-STATE-RECONSTRUCTION-001.md` | ❌ | `author-response-orch-state-reconstruction` only |
| `learning/plan/SLR-plan-C9-STATE-RECONSTRUCTION-BOUNDARY-001.md` | ❌ | `plan-orchsurf-r4-transcription` only |

**No ref holds the learning corpus of all three actors.** Measured per ref: `main` carries
`learning/plan` (10) + `learning/orchestrator` (1) and zero Mirror records; `mirror` carries 34
Mirror records and zero Plan records; `orchestrator` carries 11 Orchestrator records and 2 Plan
records. **`reviews/` is partitioned the same way** — `mirror` 49, `orchestrator` 14, `main` 3.

### 2.4 · Absent across the surveyed surface

**MEASURED_AT: 44 refs (heads + remotes + tags), 2026-08-22**

| Object | Result |
|---|---|
| `ledger/events/` — the J.1 event ledger | 🔴 **0 refs of 44** |
| `LEARNING_INDEX` (Annex E.2) — any file so named | 🔴 **0 refs of 44** |
| `active_lessons/` — the path `CLAUDE.md` § 1 points at | 🔴 **0 refs of 44** |
| `ledger/tasks/` for any actor other than `plan` | 🔴 **0 refs of 44** — every task record in the repository is `ledger/tasks/plan/*.json` |
| `ledger/checkpoints/` for any actor other than `plan` | 🔴 **0 refs of 44** |
| a coordination-review artefact (Annex G.3) | 🔴 **0 refs of 44** |

### 2.5 · Objects used as evidence, addressed as `(ref, path)`

Because a path alone does not address an object here, each load-bearing source is pinned:

```
main@788c357              CLAUDE.md · ARCHITECTURE.md · roles/{orchestrator,plan,mirror,scientist}.md
                          governance/GOVERNANCE_v3.1.1.md · annexes A,B,C,E,G,H,J
                          governance/plan_defined_parameters.md · governance/ANNEX_INDEX.md
                          framework/protocols/scientist_reading_modes.md
                          framework/scripts/lease_state.py · runtime/orchestrator_lease.md
                          ledger/tasks/plan/*.json · ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl
                          governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md
                          learning/orchestrator/SCIENTIFIC-PIPELINE-PREPARATION-001.md
orch-state-reconstruction@f1074aa
                          governance/candidates/PROPOSAL-ORCH-STATE-RECONSTRUCTION.md
                          blob e6af7e3d9383f4ae7d5210f81af5610bd15e62e7
mirror@78dccaf            reviews/mirror/REV-ORCH-STATE-RECONSTRUCTION-001.md  blob 16322c97
                          learning/mirror/SLR-mirror-CORRECTION-MEMORY-ANALYSIS-001.md
operator-decision-orch-state-reconstruction@4652f83
                          governance/decisions/DEC-20260822-ORCH-STATE-RECONSTRUCTION-CANDIDATE.md
author-response-orch-state-reconstruction@22b3dc6
                          reviews/orchestrator/AUTHOR-RESPONSE-ORCH-STATE-RECONSTRUCTION-001.md
orchestrator@1e2fabd      runtime/agent_card_registry.md · runtime/runtime_inventory.md
                          ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl  blob bb603d9a27
evidence-index@7a90a91    ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl  blob 95fc816390
```

---

## 3 · Repository evidence

### 3.1 · Dispatch validation — every named concept tested before being reasoned with

**Repository-defined** = a normative file defines or governs the term. **Repository-used** = it
appears with stable meaning but no normative definition was located. **External vocabulary** =
not present as an object on the surveyed surface.

| Concept | Repository source | Identifier | Normative status |
|---|---|---|---|
| **Orchestrator** | H.1 (5 of 17 rows); Annex I.3; body § 35.2 | `orchestrator` | **DEFINED.** Role contract `roles/orchestrator.md` is `PROPOSED` and **NON-BINDING** (§ 3.2). 0 `ACTIVE` leases |
| **Scientist A** | `roles/scientist.md`; `scientist_reading_modes.md` § 1.1 | `scientist-a` (worktree `lettore`) | **DEFINED.** `ACTOR_ID` fixed by a protocol whose own status line reads `PROPOSED` (§ 3.3). Registry: `NOT_REGISTERED` |
| **Scientist B** | same | `scientist-b` (worktree `lettore-b`) | **DEFINED**, same qualification. Registry: `NOT_REGISTERED` |
| **Scientist C** | body § 32; `roles/scientist.md` frontmatter | `scientist-c` (worktree `lettore-c`) | **DEFINED as an actor**; `ACTOR_ID` `PROPOSED`, confirmed at its own registration (I.2 step 7, PID-12). Registry: `REGISTERED_PENDING_L1_L2` |
| **Mirror** | Annex G; Annex C.2; H.1 row `Epistemic / method review` | `mirror` | **DEFINED.** Annexes bind independently of the `PROPOSED` role contract |
| **Plan** | body § 30; H.1 rows `Integrazione strutturale` and `Rifiuto integrazione` | `plan` | **DEFINED**, same qualification |
| **handoff** | Annex B.2 message-type enumeration | `HANDOFF` | **DEFINED AS A MESSAGE TYPE, AND ONLY THAT.** 🔴 No schema, no required fields, no state effect is specified anywhere on the surveyed surface. **15 distinct paths repository-wide carry a handoff name**, each with a shape of its own (§ 3.6) |
| **learning record** | Annex E.6; body § 15 | `Session Learning Record`; outcomes `MICRO_UPGRADE \| BEST_PRACTICE_CANDIDATE \| FAILURE_PATTERN \| MACRO_UPGRADE_CANDIDATE \| NO_NEW_LEARNING` | **NORMATIVE AND INSTANTIATED** — 56 records across `main`, `mirror`, `orchestrator` |
| **workflow** | Annex E.2 field `AFFECTED_WORKFLOW` | `AFFECTED_WORKFLOW` | 🔴 **PARTIAL.** The *field* is normative and denotes a **surface**. There is no `WORKFLOW` object, no workflow definition, no workflow state and no workflow engine. The dispatch's noun sense is **external vocabulary** |
| **correction memory** | — | — | 🔴 **EXTERNAL VOCABULARY.** `CORRECTION_MEMORY` and "correction memory": **0 occurrences across 35 heads**, case-insensitive, outside `mirror`'s analysis record, which itself declares the term external. **But the object it names exists — twice, under a different name** (§ 3.7) |
| **human gate** | — | — | 🔴 **EXTERNAL VOCABULARY as a phrase** (`HUMAN_GATE`: 0 occurrences, 35 heads). The repository's terms are `HUMAN_REQUIRED` (Annex B.2 message type; H.1 row `Classificazione HUMAN_REQUIRED ordinaria`), `HUMAN_APPROVAL_QUEUE` (J.3) and `GATE 0–5` (Annex D). **The concept is defined; the phrase is not** |
| **Q-1** | `PROPOSAL-ORCH-STATE-RECONSTRUCTION.md` § 6 | `Q-1` | 🔴 **REPOSITORY OBJECT — see § 3.4.** *"Is a `TRANSITION_CHECK` a gate, an advisory, or a report?"* Owner: operator. **Open.** |
| **loop** | — | — | 🔴 **EXTERNAL VOCABULARY.** Independently established by four Mirror records. One string occurrence in `governance/`, inside `"EXCEPTION-ONLY HUMAN IN THE LOOP"`, an unrelated sense |

**Four of the dispatch's terms are external vocabulary** — *correction memory*, *human gate*,
*workflow* in its noun sense, and *loop*. They are reproduced where the dispatch's structure
requires them and are never reasoned from as though they named repository objects.

### 3.2 · The four role contracts are non-binding — a binding determination

`governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` (on `main`) is an operator
determination under H.1:

> **OPTION B — `ACTIVATION_NOT_CONFIRMED`.** The existing records do not constitute activation of
> the four role contracts. The contracts remain `PROPOSED`.

Consequence 2 governs how any analysis of the target architecture may be written:

> **No actor authority may be assumed from these contracts.** Any authority an actor exercises
> must be traced to the governance body or to a named annex — H.1 for the authority matrix, D for
> the commit path, C for the review ladder, I.3 for the lease — never to a role contract clause
> standing alone.

🔴 **This is the single most consequential fact for the target architecture.** The dispatch names
five roles. Four of the five have written contracts, and none of the four binds. The pipeline
`Plan → Scientist A/B/C → Mirror → Orchestrator` therefore has **no binding description of what
any of its stages is** — only H.1's 17 rows, which allocate by *decision type* and not by *stage*.

### 3.3 · `scientist_reading_modes.md` — activation clauses measured SATISFIED, status unchanged

The protocol's status line states a three-clause conjunction. Re-measured independently this
session:

| Clause | Measurement | Result |
|---|---|---|
| canonical execution of `CAND-20260818-SCIENTIST-AB-SPEC` | commit `4454fea` is an ancestor of `main` | ✅ SATISFIED |
| Mirror hostile review passes | `REV-SCIAB-MIRROR-006` → `verdict: ACCEPT` (branch `mirror`) | ✅ SATISFIED |
| `HUMAN_APPROVAL` | `APR-20260819-SCIAB-001` / `RES-20260819-SCIAB-001`, `STATE: APPROVED` — **queue line 8 on branch `orchestrator` only** | ✅ SATISFIED |

All three hold; the status line still reads `PROPOSED`. **This record measures the clauses and
does not rule on them.** Ruling is a `STATE_DETERMINATION` of the kind `DEC-20260822` performed
for `roles/`, and H.1 gives it to the operator. Carried forward as O-1 from the predecessor
record, unresolved.

### 3.4 · 🔴 Two corrections to `SCIENTIFIC-PIPELINE-PREPARATION-001`

Both are new measurements, not amendments. That record is not edited.

**(a) `Q-1` is a repository object, not external vocabulary.**

The predecessor recorded, as O-7: *"`Q-1` — named by the dispatch, zero occurrences on any of 41
refs. External vocabulary, or a concept that has never been written down."*

Re-measured with word-boundary matching across 35 heads: `Q-1` occurs on **6 refs**. It is defined
at `orch-state-reconstruction:governance/candidates/PROPOSAL-ORCH-STATE-RECONSTRUCTION.md` § 6:

> **Q-1 · Is a `TRANSITION_CHECK` a gate, an advisory, or a report?** A gate that blocks dispatch
> is a normative rule and would need the governed path. An advisory that anyone may override is
> not a compensator for the RBAC J.0 says the system lacks. *Owner: operator (H.1 → governance).*

**Timestamps establish that the object was reachable at the predecessor's own measurement
instant.** `orch-state-reconstruction` @ `f1074aa` is dated `2026-08-22 17:05:22 +0200` and
`operator-decision-orch-state-reconstruction` @ `4652f83` is dated `17:29:50`. The predecessor
record was committed at `18:01:01`. Two of the six carrying refs predate it. Three later refs —
`mirror` (18:05), `plan-orchsurf-r4-transcription` (18:09), `author-response-…` (18:27) — did not
yet exist and are correctly outside its surface.

The consequence is not cosmetic. **Q-1 is the open governance fork on which the entire loop model
of § 5.3 turns**, and the predecessor's dispatch instruction *"do not resolve Q-1"* was therefore
an instruction about a live repository object, not about an unknown term.

**(b) The `HUMAN_APPROVAL_QUEUE` divergence is three-way and non-nested, not two-way.**

The predecessor recorded, as O-4: *"`main` has 6 lines, `orchestrator` ≥10 including SCIAB/XPORT/
P5DOMAIN approvals."* Both figures are correct. The census is incomplete.

**MEASURED_AT: 35 heads, by blob oid, 2026-08-22**

| Blob | Lines | Refs carrying it | `APPROVAL_ID`s |
|---|---|---|---|
| `20c24a2ba4` | 6 | **16 refs, incl. `main`, `mirror`, all four `orch-*-reconstruction` branches** | GOV311-001, GOV311-002 |
| `bb603d9a27` | 10 | `orchestrator` | + SUNSET-DEC3-001, SCIAB-001, XPORT-001, P5DOMAIN-001 |
| `95fc816390` | 14 | `evidence-index`, `p51c9-rebased-onto-c89c2217` | + HA-1, HA-2, HA-3, HA-4 |

```
DISTINCT APPROVAL_IDs repository-wide        10
MAX carried by any single ref                 6
`main` carries                                2
```

🔴 **Neither extended version is a superset of the other.** `comm` over the two ID sets returns
four IDs exclusive to `orchestrator` and four exclusive to `evidence-index`. This is not a merge
backlog in which one branch is ahead: **an append-only ledger has been appended to concurrently
on two branches**, which is the multi-writer condition J.1 forbids in terms — *"append-only,
nessun file condiviso multi-writer."*

**A measurement note that is part of the finding.** A first pass counted `"APPROVAL_ID":"` and
returned 4 IDs for a 10-line file. Lines 7–10 serialise as `"APPROVAL_ID": "` — with a space. The
key-match regex silently dropped exactly the four approvals that matter most, and the error was
caught only because the line count and the key count disagreed. **The same ledger carries two
serialisation conventions**, and a naive reader of it gets a clean, wrong answer. This is the
false-negative class Mirror registered as `PROV-POSITIVE-CONTROL-BEFORE-NEGATIVE-FINDING`; it is
recorded here as an instance, not as a claim to have applied that practice by transmission.

### 3.5 · What is executable today — measured by running it

| Gate | Verdict this session | What it reads |
|---|---|---|
| `framework/scripts/legend_lint.py .` | `PASS` | the four scientific current files, registries |
| `framework/scripts/fulltext_receipts.py verify` | `OK: 128 chained receipt(s), tail anchored` | the receipt ledger + state manifest |
| `framework/scripts/growth_anchors.py check` | `PASS` — claims=39 · papers=70 · corpus=356 · literature=390 | growth anchors, both debt ratchets |
| `scripts/public_release_gate.py` | `PASS`, `BLOCKS: 0`, 4 `[REVIEW]` items | the publication surface |
| `framework/scripts/lease_state.py` | `ACTIVE by derivation: 0` | `runtime/orchestrator_lease.md` |

**Executable coupling to the control plane — tested with a positive control.**

```
Python files:  framework/scripts 51 · scripts 35 · governance/scripts 3   = 89
files referencing learning/   → 0
files referencing reviews/    → 0
files referencing ledger/     → 1  — governance/scripts/test_candidate_content_hash.py,
                                     and both hits are fixture strings, not readers
files reading ledger/tasks|approvals|checkpoints|events → 0
POSITIVE CONTROL  grep -c 'def ' framework/scripts/legend_lint.py → 26  (instrument working)
HOOKS             .claude/settings.json declares exactly one: a PreToolUse Bash guard.
                  No SessionStart hook exists.
```

🔴 **No executable file in this repository reads any control-plane state.** Tasks, approvals,
checkpoints, learning records and reviews have **zero** executable readers. Every gate that runs
reads *scientific* state or the *release* surface. The coordination layer is enforced entirely by
a reader following pointers by hand.

### 3.6 · `HANDOFF` — a message type used as a persistence class

Annex B.2 names `HANDOFF` in an enumeration and specifies nothing else about it: no envelope
fields beyond B.1, no schema, no state effect. Repository-wide there are **15 distinct paths**
carrying a handoff name:

```
governance/candidates/  HANDOFF-GOV311-ORCHESTRATOR · HANDOFF-ORCHSURF-MIRROR
                        HANDOFF-P5DOMAIN-MIRROR · HANDOFF-SCIENTIST-AB-SPEC
                        HANDOFF-SUNSET-DECISION3 · HANDOFF-XPORT-MIRROR
learning/mirror/        HANDOFF-MIRROR-PERSISTENCE-AND-HANDOFF-v2 · HANDOFF-ROLE-CONTRACTS-001
learning/plan/          HANDOFF-20260822-ROLE-CONTRACT-REPAIR
reviews/mirror/         HANDOFF-CANDIDATE-READINESS-001
runtime/handoff/C-2/    HANDOFF-C-2-PMID42422765 · PMID42422765.working.…json
release/                CONTENT_HANDOFF · FULLTEXT_TRACE_HANDOFF · LINK_MIGRATION_HANDOFF
```

Eleven are actor-to-actor, three are release-process, one is a working blob. **A message type has
become a durable-record class by convention, in three different namespaces, without a schema.**
`REV-ORCH-STATE-RECONSTRUCTION-001` F-7 records the mitigating precedent, accepted by the author:
`HANDOFF-GOV311-ORCHESTRATOR` already carries `source_branch`, `base_head` and
`candidate_content_hash` as structured keys. The precedent exists; the requirement does not.

### 3.7 · The object named "correction memory" exists, twice, under another name

`mirror:learning/mirror/SLR-mirror-CORRECTION-MEMORY-ANALYSIS-001.md` § 5.3 measures it. Its
finding is reproduced here because it is directly load-bearing for § 5.4, and the record is
absent from `main`:

```
PRACTICE_ID:  PROV-DIFF-AGAINST-TARGET                       governance/design_records/materialization_log.md:647
PRACTICE_ID:  PROV-POSITIVE-CONTROL-BEFORE-NEGATIVE-FINDING  governance/design_records/materialization_log.md:1026
```

Both carry the full Annex E.3 field set — `HYPOTHESIS`, `APPLIES_TO`, `STARTED`,
`EVIDENCE_EXPECTED`, `SUCCESS_CRITERION`, `FAILURE_CRITERION`, `EXPIRY`, `ROLLBACK` — which is a
superset of the five fields a correction-memory object would need. Three properties of them
matter architecturally:

```
LOCATION     both in governance/design_records/ — provenance, not the learning namespace
CARDINALITY  5 PROV-* identifiers exist; only these 2 carry the full E.3 field set
LIFECYCLE    🔴 both expire "at Mirror's first coordination review".
             0 coordination-review artefacts exist across 44 refs; the cadence N governing it
             (Annex G.3) is UNASSIGNED and Annex G.2 bars Mirror from setting it alone.
             Annex E.3 states "Mai provisional per sempre." Both are held indefinitely
             provisional by an event that has never occurred and that no single actor may schedule
```

---

## 4 · Current architecture — as measured, not as described

### 4.1 · What actually moves work today

```
operator
   │  reads a durable artifact in checkout X, by hand
   │  composes a dispatch naming a role, a mode and a scope
   ▼
session (any checkout)  ── establishes identity from the repo, not from the dispatch
   │  works inside one worktree
   │  WORK_COMMIT on its own branch (H.1 — "ogni attore, solo proprio branch")
   ▼
durable artifact on branch B
   │
   └── 🔴 NO RETURN EDGE. Nothing carries (ref, path) forward. The operator reads B by hand
       and composes the next dispatch.
```

**The operator is the transport layer.** This is not an inference: it is visible in the commit
graph of 2026-08-22, where five sessions each produced one artifact on its own branch —
`orch-state-reconstruction` (17:05) → `mirror` (17:18, 18:05) → `operator-decision-…` (17:29) →
`main` (18:01) → `plan-orchsurf-…` (18:09) → `author-response-…` (18:27) — with **no merge, no
message and no shared file** connecting any pair. Each later session read its predecessor's output
by `git show <ref>:<path>`, and each was told which ref by the dispatch.

### 4.2 · The five components the target names, and their measured state

| Stage | Binding description? | Actor registered? | Capability `VERIFIED`? | Durable task record? |
|---|---|---|---|---|
| Orchestrator | ❌ contract `PROPOSED`; H.1 rows only | ❌ `BOOTSTRAP_CONTROLLER`, no lease | ❌ 0 of 5 | ❌ none exists |
| Plan | ❌ contract `PROPOSED`; H.1 rows only | ✅ `REGISTERED_PENDING_L1_L2` | ❌ 0 of 6 | ✅ **5, all under `ledger/tasks/plan/`** |
| Scientist A | ❌ contract `PROPOSED` | ❌ `NOT_REGISTERED`, `DIRTY_WORK: yes` | ❌ 0 of 6 | ❌ none |
| Scientist B | ❌ contract `PROPOSED` | ❌ `NOT_REGISTERED`, `DIRTY_WORK: yes` | ❌ 0 of 6 | ❌ none |
| Scientist C | ❌ contract `PROPOSED`; `ACTOR_ID` `PROPOSED` | ✅ `REGISTERED_PENDING_L1_L2` | ❌ 0 of 6 | ❌ none |
| Mirror | ❌ contract `PROPOSED`; Annex G binds | ✅ `REGISTERED_PENDING_L1_L2` | ❌ 0 of 4 | ❌ none |

Source: `orchestrator:runtime/agent_card_registry.md`, which states its own consequence — *"Until
then the laboratory is **not running**, and no assignment may be made on any capability in this
file."* Body § 8 and Annex I.4 require assignment on `VERIFIED` capabilities. **There are none, in
any actor, of any role.** L2 capability verification is `SUSPENDED` by the C-9 operator hold of
2026-08-17.

### 4.3 · The five infrastructure absences, and how they interlock

```
LEARNING_INDEX (E.2)      absent  →  no dedup before a learning record is filed (body §15
                                     requires consulting it), no retrieval by surface
ACTIVE_LESSONS (E.5)      absent  →  no role-specific subset loads at rehydration (body §19)
ledger/events/ (J.1)      absent  →  J.2 defines a transition as "evento (J.1) + roster durevole".
                                     Every transition ever performed lacks the event half of its
                                     own definition. Mirror's declared primary analysis surface
                                     (G.3) does not exist
heartbeat (B.3, P4)       never run → readiness is actor-declared, never observed
coordination review (G.3) 0 artefacts → the expiry event for both existing correction memories
```

Each is individually declared `pending` by a governed act. **Jointly they remove the analysis
surface on which the metacognitive role is defined**, and each one's natural remedy is barred to a
different actor: Plan owns durability, Mirror owns epistemic curation, the operator owns the
cadence, and G.2 bars Mirror from unilaterally changing any of it.

---

## 5 · Target architecture analysis

> The dispatch supplies an example flow and instructs that the workflow not be defined. This
> section analyses **required components and missing components**, area by area.

### 5.1 · Area 1 — Scientific task orchestration

#### 5.1.1 · What object represents a scientific task?

**Annex A.1 `TASK_ASSIGNMENT` is the object, and it is fully specified.** Fields:
`TASK_ID / DIRECTIVE_VERSION / GENERATION / OWNER / PRIORITY / OBJECTIVE / SCOPE /
ACCEPTANCE_CRITERIA / DEPENDENCIES / REVIEW_REQUIREMENT / INTERACTION_MODE / RETRY_POLICY /
MILESTONE_PLAN / DELIVERABLE / CURRENT_STATE`.

For a **scientific reading** specifically, `scientist_reading_modes.md` § 2.2 adds
`PARALLEL_READ_GROUP` as a declared **extension field** on A.1 — A.1 declares its minimum fields
extendible, never removable — and § 3.5 fixes the deliverable as three surfaces with one data
model: reading provenance (work manifest, `schema_version 2`), locator fidelity (dossier with
SHA-256 and verbatim quotes), claim assertion (12 canonical fields + 7 benchmark fields +
`Locators:`).

```
PRESENT    the schema, complete, frozen, with a scientific extension already specified
MISSING    🔴 any instance. ledger/tasks/ holds 5 records, all `plan/`, across 44 refs.
           No TASK_ASSIGNMENT has ever been issued to any Scientist.
MISSING    🔴 a writer. No executable creates, validates or reads a task record (§ 3.5).
           The five that exist were hand-authored JSON.
NOTE       the single existing example, ledger/tasks/plan/SCIENTIST-AB-SPEC-001.json, opens with
           a `_note` stating it is "Operator-directed work, not a task assigned under H.1. No
           ACTIVE lease exists and no Orchestrator issued a Task Contract." It exists so the work
           has provenance, not to assert an authority was exercised.
```

#### 5.1.2 · How is a task addressed?

```
IDENTITY   ACTOR_ID (Annex I.4) — stable, defined, and UNRESOLVED for 2 of 6 actors
ROUTING    FROM/TO in the B.1 envelope, keyed on a runtime ref
🔴 GAP     ACTOR_ID is not routable and SESSION_REF is not observable by its own holder.
           The registry derives all four SESSION_REFs BY SET COMPLEMENT over peer lists, on a
           stated and attackable assumption ("ListAgents returns all peers and omits only self"),
           marked `pending L1 confirmation`. CAND-20260819-XPORT records ROUTING_TRANSPORT as a
           uds socket that dies with the process. Conflict C-7 records one session seen by all
           four actors and claimed by none, open since 2026-08-16.
🔴 GAP     an ARTIFACT is addressed by path in every existing dispatch record, and a path is not
           an address here (§ 2.3). No dispatch record in this repository carries a ref.
```

**Two distinct addressing problems, and they are not the same problem.** Addressing an *actor*
fails for want of a routable identifier. Addressing an *object* fails for want of a ref field.
The second is the one `PROPOSAL-ORCH-STATE-RECONSTRUCTION` § 5.2 identifies as what actually
blocks the loop: *"The loop is not blocked by authority — the authority is cleanly allocated by
H.1 … It is blocked by addressing."*

#### 5.1.3 · How would Orchestrator know what remains?

```
SPECIFIED  Plan's reconciliation over ledger/tasks/*/ (roles/plan.md; body §30)
SPECIFIED  A.5 task states: ASSIGNED → ACKED → CLAIMED → IN_PROGRESS →
           (BLOCKED | AWAITING_APPROVAL) → COMPLETE | CANCELLED | REASSIGNED(gen+1) | PARKED
SPECIFIED  the OPERATOR_DAILY_BRIEF exposing PENDING HUMAN DECISIONS (J.3)
🔴 MISSING the event stream. J.2: "Ogni transizione = evento (J.1) + roster durevole."
           ledger/events/ : 0 refs of 44. A reconstruction today derives from git state alone,
           which shows what an object IS and never what an actor INTENDED or CLOSED.
🔴 MISSING "remaining workload" has no carrier. No Annex B message type and no Annex A field
           conveys it. Nearest instruments: STATUS_UPDATE, HEARTBEAT (never run), and Plan's
           reconciliation. Carried unchanged from the predecessor record as O-6.
```

#### 5.1.4 · How is completion measured?

**This is the strongest part of the existing surface.** `scientist_reading_modes.md` §§ 3.6, 3.8
specify a five-step acceptance test, four steps of which are mechanical:

```
1  deepdive_manifest.py --verify-artifacts --require-current-schema        → PASS   MECHANICAL
2  every locator's artifact inside the declared packet, digest matches     → PASS   MECHANICAL
3  coverage map: no `not_read`                                            → PASS   MECHANICAL
4  per claim candidate: 12 canonical + 7 benchmark fields + Locators      → PASS   MECHANICAL
5  blind locator audit over every (proposition, snippet, anchor) triple            HUMAN/AGENT
```

Step 5 is the one that catches a careful reading that says more than its source, and it is the
step with no executable form. A completion predicate for a *scientific* task is therefore
**80 % mechanised at the specification level and 0 % exercised** — all six Scientist capabilities
are `UNVERIFIED` and L2 is suspended.

Completion for a **non-scientific** task has no equivalent: `ACCEPTANCE_CRITERIA` is a free-text
A.1 field with no validator.

#### 5.1.5 · How are failed tasks retried?

```
SPECIFIED  A.1 RETRY_POLICY: max_attempts / retryable error classes /
           on_exhaust: REASSIGN | PARK | ESCALATE  (default: Plan-defined)
SPECIFIED  A.4 anti-zombie: a rehydrated actor MUST verify generation, directive version and
           checkpoint compatibility before resuming. Stale → do NOT continue, ask for state
SPECIFIED  A.7 idempotent resume: check whether the milestone's durable evidence already exists;
           if it does, skip and record RESUMED_FROM_MILESTONE
SPECIFIED  F.4 DIAGNOSE before accusation — truncated turns and permission prompts are runtime
           faults, never refusal. B.3 records the measured failure class: "ACK emesso ma lavoro
           mai partito"
🔴 MISSING every one of these presupposes an assigned task with a durable record. Zero exist for
           any Scientist. The retry machinery is complete on paper and has never executed.
🔴 MISSING nothing detects a failure between turns. lease_state.py's own documentation states it:
           "Nothing compels the Orchestrator to record an acquisition, and nothing runs between
           turns."
```

### 5.2 · Area 2 — Scientist A/B/C independence model

> **The dispatch's model is not assumed accepted. Measured against the governance, it collides
> with three normative sources.**

#### 5.2.1 · The collision, stated precisely

| Dispatch position | Collides with | Source |
|---|---|---|
| Scientist A = *primary evidence extraction*, B = *independent critical analysis*, as **actor properties** | *"Equivalenti: stesso mandato, protocollo, autorità scientifica, obblighi, isolation. **No specializzazioni statiche.***" | body § 32 |
| Scientist C = **adjudication** | *Aggiudicazione challenge → **Orchestrator** (con rationale)*; persistent scientific disagreement → floor **R3 TRIADIC** | H.1; Annex C.1 |
| Scientist C = **synthesis** toward agreement | *"`INFERENCE_A + INFERENCE_B + DISAGREEMENT_UNRESOLVED` con spiegazione è esito legittimo; la sintesi forzata è un errore."* | body § 27 |

**The repository already resolves the first collision, and the resolution is exact.**
`scientist_reading_modes.md` § 0: *"The difference is a property of the task, not of the actor."*
`PRIMARY_EVIDENCE_READ` and `INDEPENDENT_CRITICAL_READ` are **modes a Task Contract assigns**, and
the protocol adds that a mode which stops rotating **has become** the static specialisation § 32
forbids — which is what Mirror's anti-fossilisation guard exists to catch.

The dispatch's A/B mapping is therefore **compatible if read as modes on tasks** and
**incompatible if read as actor identities**. The third position is not resolvable this way: no
repository object gives synthesis or adjudication to a Scientist. Carried as O-3, unresolved, and
not resolved here.

#### 5.2.2 · Contamination risks — and the honest word for the mitigation

`scientist_reading_modes.md` § 3.3 forbids, in both modes:

- reading the other reader's output, or **any** prior LEGEND output on the paper, during a
  declared blind first pass;
- contacting the other reader during the first pass, **or asking Orchestrator to relay content** —
  *"the same, by another channel."*

```
GUARANTEE   uniqueness by construction of the records — a duplication cannot exist without
            leaving two records that contradict each other
DETECTION   the actor checks the receipt ledger and task ledger before TASK_CLAIM; Plan reports
            DUPLICATED_ASSIGNMENT at reconciliation
🔴 NOT      "there is no lock" (Annex J.0, first row). The rule does NOT guarantee that nobody
GUARANTEED  opens the same PDF twice. § 2.3 of that protocol names "detectable" as the honest word
```

**Independence is a property of the surface, not of a promise.** `controlled_benchmark_ab.md` § 4:
*"A first pass run in such a checkout is blind only by promise."* A LEGEND worktree contains prior
outputs and cross-referencing manifests, so the enumerated, digested input surface — not the
worktree — is the blind path, and it must be the **default** path and the only one that leaves the
required evidence.

**A measured contamination hazard specific to this repository.** `SCIENTIST-AB-SPEC-001.json`
records that the C-2 working file `PMID42422765.json` was modified in **both** `lettore` and
`lettore-b`, byte-identical, and that the full-text packet
`files/fulltext/PMID42397075_Aqeilan2026.pdf` is present in the root and in `lettore` (hard-linked,
same inode) and **absent** in `lettore-b`. *"Parity between the two readers is therefore something
to BUILD, not something to assume."* `files/` is git-ignored, so the evidence surface is **not**
carried by any ref — a branch carries the manifest, never the evidence.

#### 5.2.3 · Ordering risks

```
SPECIFIED  FREEZE — under a benchmark, completion is declared to Plan for freezing BEFORE anyone
           else reads the output (scientist_reading_modes.md § 3.7)
SPECIFIED  three checks: pre-handover, freeze, and `verify --post-read`, which prints its own
           BLIND SPOT by name on every run, because the blind spot is a post-read object and
           cannot be checked by the same predicate as everything else
🔴 RISK    two contracts on one source are legal ONLY under a declared shared PARALLEL_READ_GROUP.
           Without one the actor must NOT claim and must raise a BLOCKER naming both records.
           PARALLEL_READ_GROUP is an extension field introduced by a protocol whose status line
           reads PROPOSED (§ 3.3). If that protocol does not bind, the field has no source.
🔴 RISK    nothing sequences the freeze. It is an instruction to an actor, not a gate. Whoever
           reads second is trusted not to have read first.
```

#### 5.2.4 · Visibility of intermediate outputs

Measured, not assumed:

| Who | Sees the other reading? | When | Source |
|---|---|---|---|
| MODE A reader | no | during a blind first pass | § 3.3 |
| MODE B reader | no | during a blind first pass | § 3.3, § 5.4 |
| Mirror | **yes, both** | **after freezing** | § 5.4 |
| Orchestrator | reads dispositions, never findings | any time | H.1; `PROPOSAL` § 5.1 |

🔴 **`MODE B` is explicitly not a review of `MODE A`** — *"a second reader is a second reader"*
(§ 5.4). A peer review, if opened, is a separate act opened by Orchestrator under C.3, rotating,
never fixed pairs, at most one active review per Scientist, at most two rounds before
adjudication, with `AUTHOR_RESPONSE` mandatory.

#### 5.2.5 · Should the third position see raw evidence or only derived artifacts?

**No repository object answers this, because no repository object defines the third position.**
What the repository does fix, and what constrains any answer:

```
IF the third position is a THIRD READING (a mode on a task, § 32-compatible)
   → it sees the raw evidence, because § 3.2's reading discipline binds it: parity of sources,
     the ban on grep as a method of analysis, verbatim locators captured while the document is
     open, figures at original resolution, the full-text read receipt. A reader that works from
     derived artifacts has not performed a reading under this repository's method.

IF the third position is SYNTHESIS/ADJUDICATION as the dispatch describes
   → it collides with § 32, H.1 and body § 27 (§ 5.2.1), and the question of what it may see is
     downstream of a decision nobody has taken.
```

**Not resolved here.** An actor choosing between these two readings would be choosing the reading
that defines its own function, which is the class of move `REV-ROLES-MIRROR-001` § 8 refuses in
terms: *"an actor choosing the reading that makes its own contract binding would be exactly the
convenient interpretation the gate exists to prevent."*

#### 5.2.6 · How could independence be measured?

Instruments that exist:

```
EXISTS     divergence between frozen A and B outputs — structurally available once two frozen
           readings exist on one PARALLEL_READ_GROUP
EXISTS     the blind locator audit: fresh agents receive (proposition, snippet, anchor) triples
           plus the packet, and NEVER the dossier or the reader's identity
           (.claude/skills/legend-locator-audit; benchmark protocol § 7 step 7)
EXISTS     `verify --post-read`, which names its own blind spot on every run
SPECIFIED  Mirror's "semi-blind divergence analysis" (body § 31; roles/mirror.md)
🔴 MISSING C.3 defines semi-blind as "independence by task framing, not by information barrier".
           That is a statement about what the method is, and it is also a statement about what it
           cannot detect: framing does not prevent an actor from having read something.
🔴 MISSING every one of these metrics is a comparison over TWO completed readings. Zero readings
           have been completed under this protocol by any registered Scientist. The measurement
           has no population.
```

### 5.3 · Area 3 — Orchestrator loop model

#### 5.3.1 · What currently prevents automatic continuation

Six blocks, each measured, in the order they would bite:

| # | Block | Measurement |
|---|---|---|
| **B-1** | **No `ACTIVE` lease** | `lease_state.py` → `ACTIVE by derivation: 0`. GATE 0 is unassertable |
| **B-2** | **No binding role contract** | all four `PROPOSED`; `DEC-20260822` Option B. Authority readable only from H.1's 17 decision-type rows |
| **B-3** | **No `VERIFIED` capability** | 0 of 27 declared, all actors. Body § 8 / I.4 require `VERIFIED` for assignment. L2 `SUSPENDED` by the C-9 hold |
| **B-4** | **No routable address for an actor** | `SESSION_REF` `DERIVED_BY_COMPLEMENT`, pending L1; transport dies with the process; C-7 open |
| **B-5** | **No ref on any dispatch record** | a path is not an address; every return edge is a cross-ref read that nothing records the ref for |
| **B-6** | **No event stream** | `ledger/events/` 0 of 44 refs. Nothing runs between turns; readiness is self-declared |

🔴 **Authority is not among the blocks.** H.1 allocates every edge of
`Orchestrator → Plan → Mirror → Scientist` without gap or overlap. This was independently
CONFIRMED by three actors: the proposal's § 5.1, the review's F-row on the same table, and the
operator decision's KEY_FINDING 3 — *"H.1 allocates every edge … without gap or overlap, while
every return edge in that loop is a cross-ref read that no dispatch record carries the ref for."*

#### 5.3.2 · The return edge, stated exactly

```
Orchestrator   reads state, dispatches or blocks
     ↓  produces: a task contract (A.1) + an address
Plan           integrates, builds the candidate, may return INTEGRATION_BLOCK
     ↓  produces: a candidate + manifest + CANDIDATE_CONTENT_HASH at a BASE_HEAD
Mirror         reviews under C.2; CONFIRMED | WEAKENED | REFINED | REFUTED
     ↓  produces: a review record + a mandatory AUTHOR_RESPONSE obligation
Scientist      reads; the conclusion is the Scientist's own
     ↓  produces: a work manifest with verbatim locators
     └──────────── 🔴 the arrow back into Orchestrator does not exist ────────────┘
```

Every actor's output lands on **its own branch**, because H.1 confines `WORK_COMMIT` there. So
every return edge is a cross-ref read. **This failure recurred inside each of the four documents
that analysed it** — the author met it while writing, the reviewer while reviewing, the operator
while deciding, and this session while surveying. Three independent actors, four independent
encounters, one mechanism.

#### 5.3.3 · Which steps are already possible

```
POSSIBLE TODAY, with no new governance
  · a session establishing its own identity from durable state (body § 36.5) — exercised, 5×
  · WORK_COMMIT on an actor's own branch (H.1) — needs no lease. Exercised throughout 2026-08-22
  · a review under C.2 with STEELMAN, declared falsifier, and one of four verdicts — exercised
  · an AUTHOR_RESPONSE (C.2, mandatory) — exercised once, 2026-08-22
  · an operator STATUS_DETERMINATION under H.1 — exercised twice, 2026-08-22
  · running the four gates and lease_state.py — exercised this session (§ 3.5)
  · a cross-ref read by `git show <ref>:<path>` — exercised, but only when told the ref
```

#### 5.3.4 · Which steps would require new governance

```
REQUIRES A GOVERNED CHANGE
  · 🔴 Q-1 — whether a pre-dispatch check is a GATE, an ADVISORY, or a REPORT. A check that
    blocks dispatch is a normative rule. Owner: operator (H.1 → governance). OPEN.
  · Q-2 — what identifies a dispatched object: ref, tip oid, content hash, or all three.
    Owner: Plan (H.1 → integrazione strutturale), subject to review. OPEN.
  · Q-6 — whether Annex B's HANDOFF needs a schema. Annex B is FROZEN, so this is governed. OPEN.
  · Q-7 — whether H.1 needs a row for "may actor X act on object Y". H.1 is [MAJOR] and FROZEN.
    Measured as absent; no amendment proposed by anyone. OPEN.
  · role-contract activation — DEC-20260822 consequence 3 requires "a new, explicit activation
    act", and explicitly does not perform, schedule or specify one. OPEN.
  · adding reviews/ to CONTROL_PLANE_ROOTS — required by an operator-adjudicated MAJOR
    determination of 2026-08-17; measured unchanged at plan_defined_parameters.md:250. OPEN.
```

#### 5.3.5 · The status of the one proposal that addresses this

`PROPOSAL-ORCH-STATE-RECONSTRUCTION` (author: orchestrator) → `REV-ORCH-STATE-RECONSTRUCTION-001`
(reviewer: mirror, R4 METHOD) → verdict **`CONFIRMED`**, with `F-7 WEAKENED` and `F-8 REFINED` →
`AUTHOR-RESPONSE-ORCH-STATE-RECONSTRUCTION-001` (both accepted, none contested, one row conceded
as false beyond the finding) → `DEC-20260822-ORCH-STATE-RECONSTRUCTION-CANDIDATE`:

```
OPTION B — HELD_AS_CANDIDATE
The proposal remains a valid candidate. No further work is authorized.
```

The decision's own rationale for declining Option C names the sequence that matters here: a
mandatory protocol step was outstanding, F-9's scope question is unadjudicated, and **Q-1's fork
is a one-way door**. Its § 4 names the risk that no reading of a document can foreclose: *a check
never formally adopted, but consulted at every dispatch until "reconstruction says BLOCKED"
becomes the operative reason a task does not proceed — a gate with no adoption record.*

**Note on sequence.** The author response is dated 18:27 and the decision 17:29 — the decision
was taken while the response it names as outstanding was still unwritten, and the response was
written afterwards. The decision states this as its reason 2 for holding. Both records are
internally consistent; the ordering is recorded here because a later reader comparing timestamps
would otherwise read it as a contradiction.

### 5.4 · Area 4 — Correction memory / learning loop

#### 5.4.1 · The transition, stage by stage, against measured mechanisms

```
failure detected     →  pattern identified  →  lesson stored  →  future dispatch improved
      │                        │                    │                     │
      ▼                        ▼                    ▼                     ▼
 3 of 8 DETECTION       body §15 FAILURE_PATTERN   56 records         🔴 NO MECHANISM
 routes available       13 of 33 Mirror records    across 3 refs       0 executable readers
 5 of 8 route to        Annex G.2 OBSERVED_FAILURE no LEARNING_INDEX   1 broken router pointer
 unmaterialized                                    no ACTIVE_LESSONS
 instruments
```

#### 5.4.2 · Is memory discoverable?

```
🔴 NO, by mechanism.
TEST 1  0 of 89 executable files read learning/ or reviews/ (§ 3.5, positive control passed)
TEST 2  exactly ONE reference exists in the four entrypoints — CLAUDE.md § 1:
        "| Active lessons for your role, once operative | `active_lessons/` — not yet
        materialized |"
        🔴 the single pointer in the router loaded every session points at a path that exists on
        0 of 44 refs, and does not mention learning/ or reviews/, where all 56 + 66 records
        actually live
TEST 3  .claude/settings.json declares one PreToolUse Bash guard. No SessionStart hook.
```

A future agent reaches these records by listing a directory it was never told about — and, given
§ 2.3, only if it happens to be standing on the right ref.

#### 5.4.3 · Who can write it, and who can consume it?

```
WRITE      Annex E.6 assigns a Session Learning Record to EACH actor, persisted by WORK_COMMIT
           on its own branch (body §18: "il messaggio notifica, il commit fa fede")
🔴 SPLIT   Annex E.2 splits LEARNING_INDEX: "durevolezza: Plan; cura epistemica: Mirror".
           WHICH OF THE TWO CREATES THE FIRST ENTRY IS NOT STATED, and ANNEX_INDEX has carried
           the row as pending throughout
🔴 UNOWNED which actor owns a correction memory arising from ANOTHER actor's failure is not
           addressed by any annex. The two that exist (§ 3.7) were authored by Plan about a
           defect Mirror detected, and stored in a namespace neither E.6 nor E.2 names
CONSUME    Annex E.5 / body §19: RAW → Mirror clustering → ACTIVE_LESSONS → role-specific subset
           → rehydration, with the subset budget defined by Plan.
🔴 MISSING every stage after RAW. 0 clustering artefacts, 0 ACTIVE_LESSONS, 0 subsets.
           Rehydration loads nothing.
```

#### 5.4.4 · How would a future agent retrieve a relevant lesson?

The field that would make retrieval-by-surface possible is `AFFECTED_WORKFLOW` (Annex E.2).
Measured by Mirror across its own 33 records: **present in 3 of 33.** No learning record on any
ref carries a machine-readable `MEASURED_AT`. The discipline exists only in prose.

So retrieval today has exactly one working channel, and it is measurable:

> **FC-4 is the single measured instance of a lesson propagating into later work.** The rule
> *"NOT_FOUND locally is not NOT_EXIST repository-wide, with a required MEASURED_AT block"* was
> introduced in `REV-ORCH-STATE-RECONSTRUCTION-001` on 2026-08-22 and appears near-verbatim in
> the dispatches issued the same day — **including the dispatch that produced this record.** It
> propagated through the operator writing it into a prompt, not through any repository mechanism.
> It is evidence that transmission works, and evidence that the working channel is not durable.

#### 5.4.5 · Where is the current bottleneck?

Stated as narrowly as the measurement permits, and it is **not** a missing object class:

```
NOT THE BOTTLENECK   the schema. All five fields a correction memory needs are named in FROZEN
                     normative text, three times over (E.2 index entry · E.3 practice · G.2
                     proposal). Two of them — DETECTION and RECOVERY — are already MANDATORY for
                     every coordination mechanism in the specification under body §40.
NOT THE BOTTLENECK   the content. FAILURE_PATTERN appears in 13 of 33 Mirror records.
🔴 THE BOTTLENECK    (1) NO INDEX — LEARNING_INDEX, 0 of 44 refs
                     (2) NO COMPRESSION — ACTIVE_LESSONS, 0 of 44 refs
                     (3) NO COUPLING — 0 of 89 executables read the corpus
                     (4) NO PARTITION-CROSSING — no ref holds all three actors' learning (§ 2.3)
                     (5) NO LIFECYCLE EXIT — both existing correction memories expire "at Mirror's
                         first coordination review"; 0 such artefacts exist, the cadence N is
                         UNASSIGNED, and G.2 bars Mirror from setting it alone. Annex E.3 states
                         "Mai provisional per sempre"; both are held indefinitely provisional by
                         an event that has never occurred and that no single actor may schedule.
```

And the detection half is worse than the storage half. Of the 8 `DETECTION` lines in `governance/`,
**3 are mechanical and available** (A.3 claim conflict at write; B.3 heartbeat + MESSAGE_ID dedup;
I.3 double-record at write / GATE 0). **5 route to Mirror instruments that do not exist** — and
`annex_e:52` and `annex_i:73`, the two lines that would detect a **recurring** failure, are both
in the unavailable set. Recurring failure is precisely the condition Annex G.1 names
`MIRROR_REQUIRED`.

#### 5.4.6 · A/B/C/D are not duplicates — one boundary is already adjudicated

`reviews/mirror/CLASS-P51-REVIEWS-LEARNING-001.md`, reviewed by Mirror and **adjudicated by the
operator on 2026-08-17**:

```
reviews/   → CONTROL PLANE   because a review is bound to the hash of the candidate it judges;
                             if reviews sat inside the hashed content tree, writing the review
                             would change the identity of the reviewed object and Gate 5 could
                             never be satisfied
learning/  → CONTENT DOMAIN  a learning record asserts nothing about a candidate's identity, so
                             its inclusion changing a hash is correct rather than pathological
CHANGE_CLASS  MAJOR · URGENCY  latent, not live
```

This is a fixed-point argument, not a preference. 🔴 **And it has not propagated:**
`plan_defined_parameters.md:250` lists `CONTROL_PLANE_ROOTS` as `governance/candidates/` and
`ledger/` — `reviews/` is absent, five days after the determination that names it. Layer C
therefore exhibits the same property § 5.4.2 measures for layers A and B: **a durable, correct,
adjudicated record that has not altered the system it describes.**

### 5.5 · Area 5 — Human-in-the-loop reduction analysis

> **Optimising for explicit gates, not for removing humans.** Where a touchpoint could plausibly
> be mechanised later, that is recorded as a question, never as a plan.

#### 5.5.1 · Current vs target — the measured gap

| Function | Current | Target (dispatch) | Gap, as measured |
|---|---|---|---|
| decides next task | operator | Orchestrator, within an authorized scope | **B-1…B-6** (§ 5.3.1). H.1 already gives `Task / priorità / riassegnazione` to Orchestrator — the authority exists and the preconditions do not |
| copies prompts | operator | `TASK_ASSIGNMENT` + `TASK_ACK` + `TASK_CLAIM` | schema complete; **0 instances for any Scientist**; no routable address (§ 5.1.2) |
| transfers outputs | operator | `DURABLE_POINTER` in a B.1 envelope | envelope defined; **🔴 `DURABLE_POINTER` has no specified form**, and a path is not an address |
| governance | operator | operator | **no gap — this is the target state already** |
| scientific priorities | operator | operator | **no gap** — H.1 `Strategia complessiva → Operatore` |
| unresolved conflicts | operator | operator | **no gap** — C.1 floor R3 TRIADIC; body § 27 forbids forced synthesis |

🔴 **The three functions the dispatch wants to keep with the human are already the human's by
H.1, and none of them is what the human is currently spending effort on.** The measured human
cost is transport: reading an artifact on one ref and naming it in the next dispatch. That is
**B-5**, an addressing gap, not an authority gap.

#### 5.5.2 · The human-decision record itself is not readable in one place

This is the finding of § 3.4(b), restated in the terms of this area. Annex J.3 makes
`HUMAN_APPROVAL_QUEUE` the durable object every `HUMAN_REQUIRED` creates — the human-gate ledger.

```
DISTINCT APPROVAL_IDs repository-wide       10
MAX carried by any single ref                6
carried by `main`                            2
mutually non-nested versions                 2  (orchestrator ⊄ evidence-index ⊄ orchestrator)
```

**Any target architecture in which a human gate is consulted programmatically has to reckon with
the fact that no ref currently carries more than 60 % of the human decisions already taken**, and
that the two extended versions have diverged rather than one being ahead of the other.

---

## 6 · Automation candidates

> Classification against **measured** capability. `EXISTS AND RUNS` means this session ran it.
> Nothing here is proposed, scheduled or authorized.

### 6.1 · AUTOMATABLE — and already executable

| Function | Instrument | State |
|---|---|---|
| structural LINT over canonical state | `framework/scripts/legend_lint.py` | **EXISTS AND RUNS** — `PASS` |
| receipt chain + manifest tail anchor | `framework/scripts/fulltext_receipts.py verify` | **EXISTS AND RUNS** — 128 chained receipts |
| registry cardinality + debt ratchets | `framework/scripts/growth_anchors.py check` | **EXISTS AND RUNS** — `PASS` |
| publication gate | `scripts/public_release_gate.py` | **EXISTS AND RUNS** — `PASS`, `BLOCKS: 0` |
| lease derivation + singleton invariant | `framework/scripts/lease_state.py --check` | **EXISTS AND RUNS** |
| candidate content hash | `governance/scripts/candidate_content_hash.py` | EXISTS |
| per-role governance fingerprint | `governance/scripts/governance_fingerprint.py compose` | EXISTS |
| work-manifest verification | `framework/scripts/deepdive_manifest.py --verify-artifacts` | EXISTS — **never exercised by a Scientist** |
| benchmark input surface (the blind path) | `framework/scripts/benchmark_input_surface.py` | EXISTS — **never exercised** |

### 6.2 · AUTOMATABLE in principle, no instrument exists

| Function | What it would read | Why it does not exist today |
|---|---|---|
| **artifact-existence check** at `(ref, path)` | git object db | `git cat-file -e` is available; **nothing calls it, and no record carries a ref** (Q-2 open) |
| **task-state reconciliation** | `ledger/tasks/*/` | 0 of 89 executables read the ledger. Records exist only for `plan` |
| **duplicate-assignment detection** | task ledger + receipt ledger | specified in `scientist_reading_modes.md` § 2.2 rule 3 as an actor obligation and a Plan reconciliation; **no code path** |
| **completion predicate** for a reading | the 5-step acceptance test | steps 1–4 are mechanical and the tools exist; **step 5 has no executable form** |
| **retry / on_exhaust** | `RETRY_POLICY` in A.1 | policy complete; **no scheduler, and nothing runs between turns** |
| **format validation** of a Task Contract | A.1 field set | **no schema file and no validator exist** for A.1, A.2, A.3, A.6 or B.1 |
| **approval-queue reconciliation** | `HUMAN_APPROVAL_QUEUE.jsonl` | three non-nested versions (§ 3.4b) and two serialisation conventions in one file |

### 6.3 · 🔴 The constraint that governs every row above

`lease_state.py`'s own documentation states the limit that applies to all of them:

> *"Nothing compels the Orchestrator to record an acquisition, and nothing runs between turns."*
> The tool derives correctly from what it is given and **cannot derive from what was never
> written down.**

**Automating a check does not automate the writing of the record the check reads.** Every
instrument in § 6.1 operates on state that a human or an actor chose to write. The `PROCEDURAL`
layer — writing a row at all — is unmechanised for every control-plane object in this repository,
and `ledger/events/` is the mechanism the governance names for closing it (`OWED NOT BARRED`).

---

## 7 · Human gates

> Named in the repository's own vocabulary — `HUMAN_REQUIRED` (B.2 / H.1), `HUMAN_APPROVAL_QUEUE`
> (J.3), `GATE 0–5` (Annex D) — not in the dispatch's phrase, which is external (§ 3.1).

### 7.1 · Structural — traced to a source, not to a judgement about convenience

| # | Gate | Source | Recurrence |
|---|---|---|---|
| **HG-1** | **Scientific priority / scope** — which studies, in what order | H.1 `Strategia complessiva → Operatore` | **per batch** |
| **HG-2** | **Spend / MAJOR approval / governance** | H.1; J.3 `TYPE: MAJOR \| SPEND \| DESTRUCTIVE \| GOVERNANCE \| STRATEGIC`; J.4 `DEFAULT_EXTERNAL_SPEND = 0` | **per batch** |
| **HG-3** | **Persistent scientific disagreement** | C.1 floor **R3 TRIADIC**, derogable only upward; body § 27 forbids forced synthesis | **per occurrence** |
| **HG-4** | **Public push** | `public_release_gate.py` **plus** a human reading `git diff origin/main..main --stat` — *"the one judgement no gate makes"* | **per push** |
| **HG-5** | **Anything therapeutic** | `CLAUDE.md` — nothing here is medical advice; therapeutic output supports discussion with a treating clinical team and never substitutes for one | **always** |
| **HG-6** | **Role-contract activation** | `DEC-20260822` consequence 3: *"a new, explicit activation act is required"*; it does not perform, schedule or specify one | **one-time** |
| **HG-7** | **Q-1 — gate / advisory / report** | `PROPOSAL` § 6; owner: operator (H.1 → governance). A one-way door | **one-time** |
| **HG-8** | **Lifting the C-9 hold on L2** | operator hold, 2026-08-17. All 27 capabilities `UNVERIFIED`; assignment requires `VERIFIED` | **one-time** |
| **HG-9** | **`scientist-c` `ACTOR_ID` confirmation** | `roles/scientist.md`; I.2 step 7, PID-12 | **one-time** |
| **HG-10** | **The third position — whether it exists and what it does** | § 5.2.1; collides with § 32, H.1, body § 27 | **one-time** |
| **HG-11** | **`MIRROR_RETROSPECTIVE` cadence N** | `ANNEX_INDEX` row: `UNASSIGNED`; carried unresolved by explicit operator decision (`APPROVAL-GOV311-DEVIATIONS` § ESC-3); G.2 bars Mirror from setting it | **one-time** |
| **HG-12** | **`C-7`** — a session seen by all four actors and claimed by none, open since 2026-08-16 | agent card registry | **one-time** |

### 7.2 · The accounting

```
RECURRING PER BATCH     HG-1, HG-2, HG-3, HG-4, HG-5     — 5
ONE-TIME UNBLOCKING     HG-6 … HG-12                     — 7
```

🔴 **The five recurring gates are exactly the three functions the dispatch wants the human to keep,
plus publication and the therapeutic bar.** The seven one-time gates are what currently blocks
everything else — and **none of the seven is held by any actor in this laboratory.** Six are the
operator's by H.1; one (HG-11) is barred to Mirror by G.2 and unassigned to anyone else.

### 7.3 · Not a human gate — mechanical, and it should stay measurable

Manifest validation · locator digest matching · coverage-map completeness · LINT · receipt-chain
verification · release gate mechanics · lease derivation · candidate content hash · fingerprint
composition · duplicate-assignment detection at reconciliation.

**With the § 6.3 caveat attached to every one of them:** they derive from what was written, and
nothing writes between turns.

---

## 8 · Risks

Each risk is anchored to a measurement in this record. None is a prediction about anyone's
conduct.

| # | Risk | Anchor |
|---|---|---|
| **R-1** | 🔴 **A check accreting authority without an adoption record.** F-10's drift path: a pre-dispatch check never formally adopted, consulted at every dispatch until *"reconstruction says BLOCKED"* becomes the operative reason a task does not proceed. **No reading of a document forecloses it, and nothing currently in the repository closes it** | `REV-…-001` F-10; `DEC-…-CANDIDATE` § 4 |
| **R-2** | 🔴 **The human-decision ledger has already forked.** Three non-nested versions of an append-only file; no ref carries more than 6 of 10 approvals; two serialisation conventions inside one file | § 3.4(b) |
| **R-3** | **An architecture designed against a state model whose event half is absent.** J.2 defines a transition as event + roster; `ledger/events/` is 0 of 44. A design built on git state alone inherits a permanent blind spot for *intent* and *closure* | § 2.4; `DEC-…-CANDIDATE` KEY_FINDING 6 |
| **R-4** | **A mode that stops rotating becomes the static specialisation § 32 forbids.** The dispatch's A/B/C assignment reads as actor identity; the protocol's guard is Mirror's anti-fossilisation review, which has never run | § 5.2.1; body § 32 |
| **R-5** | **Independence claimed rather than constructed.** *"A first pass run in such a checkout is blind only by promise."* The measured packet asymmetry between `lettore` and `lettore-b`, over a git-ignored `files/`, means parity is something to build | § 5.2.2 |
| **R-6** | **A false negative read as an absence.** Four instances are on record in this chain — the proposal's `\b` regex, the reviewer's sweep, the operator's heading anchor, and this session's `"APPROVAL_ID":"` key match. The practice that guards it (`PROV-POSITIVE-CONTROL-…`) is registered in a file no script reads and no entrypoint cites | § 3.4(b); Mirror FC-1 |
| **R-7** | **A correction memory that cannot leave `PROVISIONAL`.** Both existing instances expire at an event that has never occurred and that no single actor may schedule. Annex E.3: *"Mai provisional per sempre."* Any new practice adopting the same template inherits the same deadlock | § 3.7 |
| **R-8** | **A register that reports existing artefacts as missing.** `ANNEX_INDEX`'s downstream-artifact table was measured by Mirror against its own tree: 4 rows marked `pending` are refuted by artefacts present at the same ref, and the file contradicts itself across two tables. A mechanism reading it to learn what is missing would be told four existing things do not exist | Mirror FC-3 |
| **R-9** | **Silence read as acceptance.** C.2 states `AUTHOR_RESPONSE` is mandatory and *"il silenzio non è accettazione"*. `REV-ROLES-MIRROR-001`'s response is recorded as required and outstanding | `DEC-20260822` consequence 5 |
| **R-10** | **An actor resolving an ambiguity in its own favour.** The one check that cannot be caught later, because the actor best placed to notice is the actor that benefits. The repository's existing instrument is a refusal, not a mechanism | `PROPOSAL` § 3; `REV-ROLES-MIRROR-001` § 8 |
| **R-11** | **Analysis substituting for the reading it analyses.** Six architecture records were produced on 2026-08-22 and zero papers were read. Body § 41 defines the first scientific batch as *"scienza vera + qualificazione simultanea"* — the qualification is meant to happen **through** real science, not before it | body § 41; commit graph 2026-08-22 |

---

## 9 · Open questions

Carried, refined or newly measured. **None is resolved here, and none is assigned to anyone.**

| # | Question | Owner by H.1 | State |
|---|---|---|---|
| **Q-1** | Is a pre-dispatch `TRANSITION_CHECK` a **gate**, an **advisory**, or a **report**? | operator (governance) | **OPEN** — a one-way door; the whole loop model of § 5.3 turns on it |
| **Q-2** | What identifies a dispatched object — ref, tip oid, content hash, or all three? | Plan, subject to review | **OPEN** — `HANDOFF-GOV311-ORCHESTRATOR`'s structured keys are the precedent to start from |
| **Q-3** | Does a dispatch block map onto A.5 `BLOCKED`, or is it a pre-task state with no `TASK_ID`? | — | **OPEN** |
| **Q-4** | Who writes actor readiness? Today the actor writes its own | — | **OPEN**; adjacent to C-9 § 5, held |
| **Q-5** | Can reconstruction be specified at all before `ledger/events/` has a writer? | — | **OPEN** |
| **Q-6** | Does Annex B's `HANDOFF` need a schema? 15 paths, 15 shapes | unclear — B is FROZEN | **OPEN** |
| **Q-7** | Does H.1 need a row for *"may actor X act on object Y"*? | — | **OPEN**; H.1 is `[MAJOR]` and FROZEN; no amendment proposed |
| **Q-8** | What resolves C-7? | operator | **OPEN** since 2026-08-16 |
| **Q-9** | Does reconstruction run per dispatch, per session, or on demand? | — | **OPEN** |
| **Q-10** | Relationship between `PROPOSAL-ORCH-STATE-RECONSTRUCTION` and `PROPOSAL-C9-STATE-MODEL` | Plan (sequencing) | **OPEN**; both held; F-13 measures them as near-neighbours, not duplicates |
| **O-1** | `scientist_reading_modes.md`'s three activation clauses measure SATISFIED; status line still reads `PROPOSED` | operator | **OPEN** (carried) |
| **O-2** | That protocol's `applies_to` set is defined by `roles/scientist.md`, which is non-binding | operator | **OPEN** (carried) |
| **O-3** | The dispatch's Scientist C function collides with § 32, H.1 and body § 27 | operator | **OPEN** (carried, re-measured) |
| **O-6** | No carrier exists for "remaining workload" in Annex A or B | Plan (schema) / operator | **OPEN** (carried) |
| **N-1** | 🔴 **NEW.** `HUMAN_APPROVAL_QUEUE.jsonl` exists in three mutually non-nested versions; 10 distinct approvals, max 6 on any ref, `main` carries 2; two serialisation conventions in one append-only file | Plan (durability) / operator | **OPEN** |
| **N-2** | 🔴 **NEW.** Which of Plan (durability) or Mirror (epistemic curation) creates the **first** `LEARNING_INDEX` entry is unstated by E.2, and the row has been pending throughout | Plan / Mirror / operator | **OPEN** |
| **N-3** | 🔴 **NEW.** Which actor owns a correction memory arising from **another** actor's failure? The two that exist were authored by Plan about a defect Mirror detected, stored where neither E.6 nor E.2 names | — | **OPEN** |
| **N-4** | 🔴 **NEW.** `CONTROL_PLANE_ROOTS` still omits `reviews/`, five days after the operator-adjudicated MAJOR determination requiring it | Plan / operator | **OPEN** |

---

## 10 · Next transition

> **Stated as a dependency structure that was measured, not as a plan, a sequence anyone is
> asked to follow, or a recommendation.** Nothing below is assigned, scheduled or authorized.

### 10.1 · What the measured dependencies imply about ordering

```
Q-1 (gate | advisory | report)
   └── is upstream of every § 5.3 check. DEC-…-CANDIDATE reason 5: "Authorizing design of the
       check while its normative character is undetermined is the shortest route to F-10's
       drift path." Owner: operator. Nothing else in this list is downstream-blocked by as much.

HG-6 role-contract activation
   └── is upstream of any statement about what a stage of the pipeline IS. Until it happens,
       H.1's 17 decision-type rows are the only binding description of the five actors, and
       they do not allocate by stage.

HG-8 lifting the C-9 hold on L2
   └── is upstream of ANY assignment. Body §8 and I.4 require VERIFIED capabilities; there are
       0 of 27. This gate alone makes § 5.1's task object unusable no matter what else is fixed.

ledger/events/ having a writer
   └── is upstream of Mirror's declared analysis surface (G.3), of the autonomy ledger and
       review yield, of 5 of 8 DETECTION routes, and of the third part of J.0's compensator for
       absent runtime RBAC. Named OWED NOT BARRED. Design chosen, writer not built.

MIRROR_RETROSPECTIVE cadence N (HG-11)
   └── is upstream of the expiry of both existing correction memories, and G.2 bars Mirror from
       setting it alone. Nobody else is assigned it.
```

🔴 **Two of these five are one-way doors** (Q-1, HG-6). Three are unblocking acts that foreclose
nothing (HG-8, the ledger writer, HG-11).

### 10.2 · What iteration 2 of this task could measure that this one did not

Recorded as scope observations, not as requests:

```
NOT MEASURED  refs/codex (4) and refs/stash (1) — content not enumerated (§ 2.1)
NOT MEASURED  whether any Codex worktree holds scientific work that would collide with a first
              batch. Body §41 forbids double work with the Codex worktrees, and four Codex
              worktrees carry PMID-named branches
NOT MEASURED  the C-9 PROPOSAL-C9-STATE-MODEL text itself, read here only through Q-10 and
              through the review's F-13. Its § 5.1 reportedly already assigns transition owners
NOT MEASURED  whether the three HUMAN_APPROVAL_QUEUE versions can be reconciled without loss,
              or whether the divergence has already produced a decision recorded in one place
              and contradicted in another (N-1)
NOT MEASURED  ANNEX_INDEX row :80 (first INTEGRATION_CANDIDATE) — the one row Mirror did not test
```

### 10.3 · The state this record leaves behind

```
Nothing is activated, assigned, adopted, resolved or authorized.
One file is added, on branch `orch-pipeline-loop-architecture`, based on main@788c357.
main is unchanged. No governance, roles, framework or ledger path is written.
No scientific artifact is created and no paper was read.

Iteration 1 of 3.
```

---

## 11 · What this record does NOT do

- It does **not** define the workflow the dispatch describes, or adopt any architecture.
- It does **not** activate a role contract, or perform the act `DEC-20260822` consequence 3
  requires.
- It does **not** confer, claim or imply Orchestrator authority — § 1.2 records that authority is
  missing.
- It does **not** create a Task Contract, a `PARALLEL_READ_GROUP`, a Mirror task, a ledger event
  or a candidate.
- It does **not** assign a paper, an actor, a batch, a review or an owner for any open question.
- It does **not** resolve Q-1 … Q-10, O-1 … O-6, or N-1 … N-4.
- It does **not** create a correction-memory system, an index, a schema, a cadence or a validator.
- It does **not** verify any capability or lift the C-9 hold.
- It does **not** constitute an `AUTHOR_RESPONSE` to anything, and is not a Session Learning
  Record under Annex E.6.
- It is **not** a `WORK_COMMIT` toward a candidate and **not** a `CANONICAL_BATCH_COMMIT`.
- It amends **no** existing record. The two corrections in § 3.4 are new measurements;
  `SCIENTIFIC-PIPELINE-PREPARATION-001` is left exactly as written.

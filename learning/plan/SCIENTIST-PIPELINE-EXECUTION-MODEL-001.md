---
artifact: EXECUTION MODEL ANALYSIS — the Scientist pipeline as a workflow, before any paper is read
record_id: SCIENTIST-PIPELINE-EXECUTION-MODEL-001
task_id: SCIENTIST_PIPELINE_EXECUTION_MODEL_v1
iteration: 1/3
author: plan
authored_on: 2026-08-22
dispatcher: operator
governance_version: 3.1.1 (read, not exercised)

STATUS: READ_ONLY_ANALYSIS
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none

classification:
  - ANALYSIS ONLY
  - NOT GOVERNANCE
  - NOT EXECUTION AUTHORIZATION
  - NOT A DECISION
  - NOT A SCHEMA

naming_note: >
  `learning/plan/` holds `SLR-plan-NNNN` records by convention (Annex E.6), plus one handoff, one
  boundary analysis and one readiness analysis. This is none of those; it takes a descriptive name
  and no SLR number it has not earned.

domain: >
  CONTENT. `learning/` is not among the exhaustive `CONTROL_PLANE_ROOTS` of
  `governance/plan_defined_parameters.md` § P5.1 (`governance/candidates/`, `ledger/`, `reviews/`).
  This file therefore sits inside the `CANDIDATE_CONTENT_HASH` of any future candidate that
  includes this branch, and it moves that hash. Disclosed here, not discovered later.

relation_to_prior_work: >
  `learning/plan/SCIENTIST-PIPELINE-READINESS-001.md` (this branch, `2394b07`) analysed the same
  pipeline for READINESS. `learning/orchestrator/SCIENTIFIC-PIPELINE-PREPARATION-001.md` (branch
  `main`, `788c357`) covers overlapping ground from a BOOTSTRAP_MODE session. Both are treated
  here as claims to re-measure, not as inputs. This record answers a DIFFERENT question — how the
  work would EXECUTE — and it does not restate what those two already establish; where it relies
  on one of them, it re-measures first and says so.

verdict_transfer: >
  NONE. Every mechanical fact below was executed in this session at the HEAD named in § 1.
---

# SCIENTIST PIPELINE — EXECUTION MODEL — 001

> **The question this record answers.** How should LEGEND organize scientific reasoning while
> preserving independent evidence generation, adversarial review, epistemic traceability and
> scalability? It answers it by measuring what the repository already carries, and by naming —
> precisely, with the measurement beside it — the places where the dispatch's model and the
> repository's model are not the same model.

---

## TASK_STATUS

```
TASK_ID          SCIENTIST_PIPELINE_EXECUTION_MODEL_v1
ITERATION        1/3
MODE             READ_ANALYSIS_ALLOWED · CREATE_LEARNING_ARTIFACT_ONLY
STATE            COMPLETE for iteration 1 — the five dispatch sections are answered from
                 measurement, and every answer that could not be measured is recorded as an
                 open question with a disposition owner who is not this session

EXECUTED         repository reads across 7 refs; 4 executable checks re-run
                 (lease_state.py, benchmark_input_surface.py --help, JSON parses of the
                 benchmark manifest and surface spec, git ancestry proofs)
NOT EXECUTED     no paper opened · no literature read · no scientific conclusion formed ·
                 no actor contacted, spawned or assigned · no contract activated ·
                 no governance/ roles/ framework/ ledger/ path modified · no schema created
FILES ADDED      exactly one — this file
```

---

## IDENTITY

### 1 · Established from repository evidence, not from `roles/plan.md`

The dispatch forbids assuming authority from `roles/plan.md`. That prohibition is not merely
prudential here: **an operator decision has determined that the file is not binding** (§ 1.2). So
identity is taken from the runtime and from the deployment profile, and authority is claimed from
neither.

| Field | Measured value | Command |
|---|---|---|
| branch | `plan-orchsurf-r4-transcription` | `git rev-parse --abbrev-ref HEAD` |
| HEAD | `2394b079e88e801da2c02cef8b29e8bef7b0e231` | `git rev-parse HEAD` |
| worktree | `/Users/massimo/Desktop/legend-public/.claude/worktrees/evidence-index` | `git rev-parse --show-toplevel` |
| working tree | **clean** at session start and at every measurement below | `git status --porcelain` → empty |
| worktree ↔ actor | the profile maps `plan` → worktree `evidence-index`; this session stands in it | `deployment/deployment_profile.md` |
| lease | **`ACTIVE by derivation: 0`** — 5 records, all `STALE` or `RELEASED`; most recent released `2026-08-18T14:05:20Z` | `python3 framework/scripts/lease_state.py` |
| runtime inventory | **no file matching `*inventory*` exists on this ref** | `find . -iname "*inventory*"` → 0 hits |

🔴 **Two of those rows decide what this session may do, and both point the same way.**
`CLAUDE.md` § 0 puts a session with no valid runtime inventory and no ACTIVE lease into
`BOOTSTRAP_MODE`. Both conditions hold. This session is therefore **not Orchestrator**, holds no
lease, and issues nothing.

The deployment profile carries its own caveat and it is carried here rather than dropped:
*"Neither column is an ACTOR_ID oracle and neither is a write-authority oracle."* The mapping
orients; it does not authorize. What authorizes the single act this session performs — writing one
file under `learning/plan/` on its own branch — is H.1's `WORK_COMMIT` row: *ogni attore, solo
proprio branch*, which is an annex, not a role contract.

### 1.2 · The governing fact, and it is not on this ref

`governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` exists on `main`
(`788c357`) and **not on this branch**. Read at `main` via `git show`, not inferred:

```
OPTION_SELECTED   🔴 OPTION B — ACTIVATION_NOT_CONFIRMED
                  The four role contracts remain PROPOSED. They are non-binding documents.
                  Their status: lines are ACCURATE, not stale.
CONSEQUENCE 2     No actor authority may be assumed from these contracts. Any authority an
                  actor exercises must be traced to the governance body or to a named annex.
CONSEQUENCE 3     A new, explicit activation act is required. This record does not perform it,
                  does not schedule it, and does not specify its form.
```

**This changes the epistemic status of half the objects the dispatch asks about.** Before
2026-08-22, "the role contracts are `PROPOSED`" was a reading of a status line that its own author
had written. After it, it is an operator determination under H.1. Every statement below about
`roles/scientist.md`, `roles/mirror.md`, `roles/plan.md` and `roles/orchestrator.md` is made under
that determination.

```
MEASURED_AT  2026-08-22, HEAD 2394b07 (this branch) and 788c357 (main)
VALIDITY     until an activation act of the form consequence 3 leaves unspecified is performed
             and recorded. Nothing in this session performs, schedules or specifies it.
```

---

## SURFACE_MAP

### 2 · Refs measured, and the two that matter

Seven refs were read: `HEAD`, `main`, `orchestrator`, `mirror`, `lettore`, `lettore-b`,
`lettore-c`. 38 local branches exist; the divergence that bears on this analysis is small and
specific.

```
HEAD ↔ main       main has 2 commits this branch lacks; this branch has 38 main lacks
                  git rev-list --left-right --count main...HEAD  →  2  38
THE TWO           788c357  the DEC-20260822 decision record        (§ 1.2)
                  2bb2700  learning/orchestrator/SCIENTIFIC-PIPELINE-PREPARATION-001.md
```

🔴 **This branch cannot see the decision that governs it, and it cannot see the prior analysis of
the same subject.** Both were read at `main` by `git show`. Nothing was merged, checked out or
written outside this worktree. The prior session recorded the same gap in its own commit message —
*"The pipeline was analysed against the ref that could not see the decision governing it"* — and it
is still true one commit later, because the fix is a merge and a merge is not this task.

### 2.1 · Objects present here, and what state each is actually in

| Object | Path | Measured state |
|---|---|---|
| Scientist contract | `roles/scientist.md` | `PROPOSED`; **non-binding by `DEC-20260822`**; `actor_ids: [scientist-a, scientist-b, scientist-c]`; A and B `FIXED`, C `PROPOSED` |
| Reading modes protocol | `framework/protocols/scientist_reading_modes.md` | `PROPOSED — binding on canonical execution of CAND-20260818-SCIENTIST-AB-SPEC …` — **all three clauses measure SATISFIED (§ 2.2)**, status line never modified |
| Benchmark protocol | `framework/protocols/controlled_benchmark_ab.md` | same construction, same measurement; 748 lines |
| Benchmark seat | `framework/eval/benchmarks/BENCH-AB-001/` | manifest `_state: PREPARED — NOT FROZEN`; `HANDOVER` fields all `null`; population enumerated |
| Population | `population/evidence_units.json` | **65 units, 109 panels**, including a measured `main_table: 0` |
| Surface tool | `framework/scripts/benchmark_input_surface.py` | executes; 7 subcommands `build · verify · freeze · verify-freeze · population · locators · tree-digest`; 1558-line test suite beside it |
| Failure taxonomy | `framework/eval/failure_taxonomy.md` | **12 gates**, each learned from an observed error, counted from the table |
| Blind audit route | `.claude/skills/legend-locator-audit` | present among 21 skills |

### 2.2 · 🔴 The reading-modes protocol's activation condition — re-measured, and it is satisfied

The protocol says it binds *"on canonical execution of `CAND-20260818-SCIENTIST-AB-SPEC`, after
Mirror hostile review and `HUMAN_APPROVAL`. Until then it binds nobody."* Each clause, measured
independently in this session:

| Clause | Measurement | Result |
|---|---|---|
| canonical execution | `4454fea` — *"The Scientist A/B specification becomes canonical"* — adds the candidate file, both protocols, the benchmark seat and the tool. `git merge-base --is-ancestor 4454fea main` → **yes** | ✅ SATISFIED |
| Mirror hostile review | `reviews/plan/AUTHOR-RESPONSE-SCIAB-MIRROR-006.md` is tracked on `main`, so review 006 exists and was answered | ✅ SATISFIED |
| `HUMAN_APPROVAL` | `RES-20260819-SCIAB-001 · APPROVED · CAND-20260818-SCIENTIST-AB-SPEC` — **line 8 of the queue on ref `orchestrator`** | ✅ SATISFIED — see the divergence below |
| status line updated | `git log --all -S` over the status string: written, never changed | ❌ NEVER MODIFIED |

🔴 **The approval queue diverges by ref, and this is the second time the same divergence has
decided something.** Measured this session:

```
ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl     HEAD  6 lines     main  6 lines
                                        ref orchestrator  10 lines
lines 7–10, present ONLY on orchestrator:
  RES-20260818-SUNSET-DEC3-001   APPROVED   CAND-20260818-SUNSET-DEC3
  RES-20260819-SCIAB-001         APPROVED   CAND-20260818-SCIENTIST-AB-SPEC
  RES-20260819-XPORT-001         APPROVED   CAND-20260819-XPORT
  RES-20260819-P5DOMAIN-001      APPROVED   CAND-20260819-P5DOMAIN
```

**Approval state read from `main` alone is wrong, and approval state read from this branch alone is
equally wrong.** Four approvals are invisible from both. This is the orchestrator record's O-4,
independently reproduced, and it is not merely untidy: three of the four missing approvals are the
approvals of candidates whose canonical execution is what the protocols' own status lines depend on.

**And the satisfaction does not settle the question.** `DEC-20260822` E-3 quotes the approval
instrument's own limiting clause — `APPROVAL_IS_NOT_AUTHORIZATION`: *"This approval authorises the
INTENT. It does not authorise execution outside the rules."* A protocol whose three clauses
measure satisfied, whose status line says it binds nobody, and whose addressee set is defined by a
contract an operator has determined is non-binding, is in a state no object in this repository
resolves. Recorded as **Q-1** and **Q-2**.

### 2.3 · Negative claims — each with what was run, when, and how long it holds

| # | Claim | Command | MEASURED_AT | VALIDITY |
|---|---|---|---|---|
| N-1 | **`scientist-e` does not exist on any ref, in any form** | `git grep -iE "scientist-e"` over the tracked tree → **0 files** | 2026-08-22, HEAD `2394b07` | until an object introduces it |
| N-2 | **`scientist-d` exists only as a hypothetical**, in one candidate and two ledger out-of-scope notes — never as a role, an actor, a worktree or a contract | `git grep -iE "scientist-d"` → 6 hits in 3 files, enumerated in § 3.4 | same | same |
| N-3 | **No `confidence` field exists as a claim-level label anywhere in the canonical registry.** The single hit in `claim_registry_current.md` is the word inside prose (*"High-confidence WWOX interactors"*), not a label | `grep -i confidence` over the registry → 1 hit, line 467, inside `**Summary:**` | same | until a governed change adds one |
| N-4 | **`ledger/registrations/` does not exist on any of the 7 refs read** — no Scientist has a registration record anywhere | `git ls-tree -r <ref> -- ledger/registrations` → 0 on HEAD, main, orchestrator, mirror, lettore, lettore-b, lettore-c | same | until a registration is written |
| N-5 | **No Task Contract for any Scientist exists.** `ledger/tasks/` contains one directory, `plan/`, with 5 records, all Plan's | `find ledger -type f` | same | until Orchestrator issues one under an ACTIVE lease |
| N-6 | **No object anywhere defines a synthesis or integration function for a Scientist actor.** The only occurrence of the concept in the governance body is its prohibition | `git grep -iE "sintesi forzata\|forced synthesis"` → 1 hit, body § 27 | same | until a governed change creates one |
| N-7 | **The benchmark has never been handed over.** `_state: PREPARED — NOT FROZEN`; `FROZEN_SHA256` absent; every `HANDOVER` field `null` | JSON parse of `benchmark_manifest.json` | same | until Plan runs `build` + `verify` + `freeze` |

**`NOT_FOUND` is not `NOT_EXIST`.** Two objects this analysis depends on were located on other refs
and read there: `DEC-20260822` and `SCIENTIFIC-PIPELINE-PREPARATION-001.md` on `main`, and the four
approval lines on `orchestrator`. Each is cited with the ref it was read from.

---

## 3 · SCIENTIST ROLE MODEL — actors, modes, and one word doing three jobs

### 3.1 · The dispatch's model, and where it does not land

The dispatch proposes:

```
Scientist A   primary evidence reader
Scientist B   independent critical reader
Mirror        methodological / reasoning review
Scientist D/E integration or synthesis functions (future)
```

Measured against the repository, **the first two lines describe a current binding as if it were a
definition**, and that difference is the whole of §32's content:

> **body §32** — *Equivalenti: stesso mandato, protocollo, autorità scientifica, obblighi,
> isolation. **No specializzazioni statiche.***

`scientist_reading_modes.md` § 0 resolves the tension explicitly, and it is worth quoting because
the resolution is the answer to the dispatch's own question:

> **"The difference is a property of the task, not of the actor."**

So there are **three distinct kinds of thing**, and the dispatch's four lines conflate them:

| Kind | Instances measured | Where it lives | Rotates? |
|---|---|---|---|
| **ACTOR** | `scientist-a` · `scientist-b` · `scientist-c` — one shared contract, one `ROLE_CONTRACT_HASH`, one fingerprint value | `roles/scientist.md`; `deployment_profile.md` rows 36–38 | never — identity is stable by design |
| **MODE** | `MODE A · PRIMARY_EVIDENCE_READ` · `MODE B · INDEPENDENT_CRITICAL_READ` | assigned by a Task Contract (Annex A.1) per reading | **yes — and must.** § 32; the protocol's § 0 |
| **FUNCTION in a cycle** | read · align · audit · adjudicate the method · decide the next task | allocated by H.1 and by the benchmark sequence — to Plan, blind agents, Mirror, Orchestrator | fixed by authority, not by rotation |

### 3.2 · Answer — A/B/C are actors; "primary reader" and "critical reader" are modes

```
ARE A/B/C ACTORS?      YES. Stable ACTOR_IDs, one per worktree (lettore, lettore-b, lettore-c),
                       one shared contract, one fingerprint. Measured: `governance_fingerprint.py`
                       is keyed by ROLE, not by actor — P2.2 — so A, B, C and any future scientist
                       compose the SAME value.

ARE A/B/C MODES?       NO. The modes are MODE A and MODE B, and they are properties of a task.
                       Today MODE A is bound to scientist-a and MODE B to scientist-b, for exactly
                       one benchmark, and the protocol says why: "fixed for the first benchmark,
                       and rotate afterwards under Mirror's anti-fossilization guard."

WHAT IF THEY STOP      A mode that stops rotating "has become a static specialization" — the
ROTATING?              thing §32 forbids. The detector is Mirror's anti-fossilization guard.
                       🔴 The guard has no measured instrument: Mirror's stated primary analysis
                       surface is the J.1 event ledger, and `roles/mirror.md` records that
                       capability as "blocked: the ledger has no writer yet".
```

🔴 **Naming A "the primary evidence reader" in a durable document is how fossilization starts.**
The dispatch's phrasing is convenient and it is exactly the phrasing §32 exists to prevent. The
repository's own phrasing — *the actor is `scientist-a`; the task carries `MODE: PRIMARY_EVIDENCE_READ`*
— costs one clause and preserves the property.

### 3.3 · Scientist C — the third position, and why nothing here decides it

The dispatch says: *do not assume Scientist C is synthesis.* Measured, that instruction is correct
and the repository is stronger than "do not assume" — **synthesis for C is affirmatively
unsupported** (N-6), and it collides with three objects:

| Collision | Object |
|---|---|
| forced synthesis is an error; `INFERENCE_A + INFERENCE_B + DISAGREEMENT_UNRESOLVED` is a legitimate outcome | body § 27 |
| challenge adjudication is Orchestrator's, with rationale | H.1 |
| review opening, rotation, `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR`, max 2 rounds | Annex C.3 |

What **is** supported: C exists as an actor to be created (§ 32, *"Scientist C da creare subito"*);
its worktree `lettore-c` exists and is clean; a third scientist may **adjudicate inside the peer
review ladder** (C.3 + the R3 TRIADIC floor). Adjudicating a *review of a claim* is not the same
act as synthesising *two independent first passes*, and the repository authorizes only the first.

`SCIENTIST-PIPELINE-READINESS-001` § 6.3 records the two available readings of the third position
and withholds a recommendation on the stated ground that an actor choosing the reading that gives
it a role is the interpretation the gate exists to prevent. **That reasoning holds here with equal
force and this record withholds a recommendation for the same reason.** Carried as **Q-3**, owner
operator.

### 3.4 · 🔴 Scientist D and E — measured, and the answer splits in two

`scientist-e`: **zero occurrences on any ref** (N-1). There is nothing to evaluate; the name is the
dispatch's.

`scientist-d`: six occurrences in three files, and every one of them is the same use:

```
governance/candidates/CAND-20260819-XPORT.md:459,461,541,544
    § 9 "Generality — the architecture is ACTOR-GENERIC, and the falsifier"
    § 9.2 "The Scientist D falsifier" — onboarding a HYPOTHETICAL ORDINARY ACTOR,
          described using only generic machinery, to test whether the transport
          architecture needs actor-specific code

ledger/tasks/plan/XPORT-ROUTING-001.json:27     out of scope: "creation or activation of any scientist-d"
ledger/checkpoints/plan/CHK-plan-0017.json:133  not done: "no Scientist activated; no scientist-d created"
```

**`scientist-d` is a test fixture, not a proposal.** It exists to falsify a generality claim about
routing, and the candidate that carries it was approved (`RES-20260819-XPORT-001`, on ref
`orchestrator`). Its measured conclusion:

```
SCIENTIST D REQUIRES NEW ROUTING LOGIC:  NO
DELTA:  ACTOR_ID + role binding + worktree row + fingerprint (derived, not added) +
        registration + acceptance test.  That is configuration, not protocol redesign.
```

So the answer to *"are future D/E justified?"* is **two different answers to two different
questions the dispatch merges into one line**:

| Reading of "D/E" | Verdict | Evidence |
|---|---|---|
| **D/E as further EQUIVALENT readers** — a fourth and fifth scientist under the same shared contract, same modes, assigned by task | ⚠️ **SUPPORTED AND CHEAP, but not yet earned.** The onboarding delta is measured at five configuration steps and no new protocol. It adds reading throughput and a third/fourth position in the R3 TRIADIC floor | XPORT § 9.2, approved |
| **D/E as INTEGRATION or SYNTHESIS functions** | 🔴 **UNSUPPORTED, and it collides with one more object than C-as-synthesis does** | below |

🔴 **The fourth collision, and it is the one the C analysis did not have to face: the integration
function is already allocated, and it is allocated WITH a boundary.**

Body § 30 and § 28 give integration to Plan, and give it a limit that is the whole point of giving
it to Plan at all:

> **body § 28** — *Plan rifiuta per ragioni strutturali/provenance/protocollo; **NON risolve
> significato scientifico conteso**: `INTEGRATION_BLOCK → Orchestrator → Scientist`.*

An "integration Scientist D" is therefore one of exactly two things, and both are defects:

```
(i)  a duplicate of Plan          — two actors holding the integration layer, with no rule
                                    saying which one's INTEGRATION_BLOCK binds. Body §14's
                                    ONE_WRITER_PER_WORKING_DIRECTORY prevents the file collision;
                                    nothing prevents the authority collision

(ii) an integrator WITHOUT §28    — an actor that resolves contested scientific meaning.
                                    Nothing in this repository authorizes that for ANY actor.
                                    Orchestrator is denied it (H.1: "non controlla quale
                                    conclusione"), Plan is denied it (§28), Mirror is denied it
                                    (no primary evidence, object is the process), and body §27
                                    denies it to the system as a whole
```

**Recorded conclusion:** adding scientists is a configuration act the architecture already
survives. Adding a *synthesis role* is a governance act that would have to overturn body § 27
first, and § 27 is one sentence long precisely so that it cannot be overturned by accident.

---

## 4 · CONTAMINATION CONTROL

### 4.1 · The dispatch's pipeline, and the two things its boxes hide

```
dispatch:   FREEZE → Independent read → Independent output → Comparison → Mirror review
```

Measured against `controlled_benchmark_ab.md` § 5 and § 7, that linear chain hides one split and
one unowned box.

🔴 **Hidden split — there are TWO freezes, at opposite ends, protecting different things.**

| | INPUT FREEZE | OUTPUT FREEZE |
|---|---|---|
| When | **before** any reading — at build/handover | **after** the reading, on the completion declaration, **before Plan reads the content** |
| Object | the manifest (`FROZEN_SHA256`), the allowlist, and the evaluation population's digest | the reader's own output tree — tree digest, per-file digests, commit sha, timestamps |
| Protects | the **denominator**: 65 units, 109 panels, fixed so coverage cannot be redefined once the readings exist | the **immutability of a first pass**: a correction after freeze is a new dated file under `post_freeze/`, never an edit |
| Command | `build` · `verify` · `freeze` (manifest) | `freeze` (surface) · `verify-freeze` |
| If skipped | every coverage number becomes negotiable after the fact | retroactive edits become possible and leave no trace |

**Both are required and they are not interchangeable.** A pipeline diagram with one FREEZE box
will be implemented with one freeze, and whichever one is built is the one whose failure mode is
covered.

🔴 **Unowned box — "Comparison" is two functions, and only one of them has an owner.**

```
STRUCTURAL ALIGNMENT      Plan. Benchmark §5 step 6 + §8.3. Rows are claim candidates from both
                          readings, aligned BY SHARED LOCATOR ANCHOR — same figure/table/section
                          unit. "Alignment is structural, by unit, not by Plan's reading of
                          whether two claims mean the same." Output: comparison_matrix.md.
                          ✅ OWNED · MECHANICAL · SPECIFIED

EPISTEMIC RESOLUTION      NOBODY, by design. A row flagged as a disagreement goes to
                          unresolved_disagreements.md with both statements quoted and typed,
                          "and stays unresolved there". §27 makes forced synthesis an error.
                          The route out is Orchestrator opening an Annex C R2/R3 review —
                          benchmark §5 step 10, explicitly OUTSIDE the benchmark record.
                          🔴 NOT A PIPELINE STAGE. It leaves the pipeline.
```

**The dispatch's arrow `Comparison → Mirror review` therefore reads as though comparison resolves
before Mirror sees it. It does not resolve at all.** Mirror receives an alignment plus a list of
open disagreements, and Mirror's object is the process, not the disagreement.

### 4.2 · The corrected pipeline, with owners — measured, not designed

```
0  PRECONDITIONS       operator / Orchestrator     lease · registrations · capabilities · scope
1  INPUT FREEZE        Plan                        build + verify + population + freeze manifest
2  TASK CONTRACTS      Orchestrator (lease ACTIVE) two contracts, one PARALLEL_READ_GROUP
3  HANDOVER            Plan → each actor           writer transfer + memory-scope check recorded
4  INDEPENDENT READ    scientist-a · scientist-b   blind first pass, in the surface, full depth
5  OUTPUT FREEZE       Plan                        on declaration, BEFORE reading content; import
6  STRUCTURAL COMPARE  Plan                        matrix by locator anchor; disagreements listed
7  BLIND LOCATOR AUDIT fresh agents spawned by Plan triples only; reader identity withheld
8  METHOD ADJUDICATION Mirror (R4)                 the process, not the paper
9  OUTCOME             Plan                        every dimension separately, no composite
10 → OUT OF PIPELINE   Orchestrator                scientific disagreement → Annex C R2/R3
```

Two observations about that table that the dispatch's five boxes cannot carry:

- **step 7 is between comparison and Mirror, and it is the step that gets skipped.** The blind
  locator audit is *"the one that catches a careful reading that says more than its source"* and
  the readiness record names it as the step skipped first under time pressure.
- **steps 1, 3, 5, 6, 9 are all Plan.** That is the scaling constraint of § 6 and the
  concentration risk of § 4.4.

### 4.3 · What "contamination" names, measured — six classes, none invented

| Class | The act | Source |
|---|---|---|
| shared context | reading in a checkout that already holds LEGEND output on the paper — **21 tracked files name the benchmark's PMID at `BASE_HEAD`** | benchmark § 2.1 |
| seeing previous conclusions | reading the other reader's output, **or any prior LEGEND output on the paper**, during a pass declared blind | reading modes § 3.3 |
| relayed content | contacting the other reader, **or asking Orchestrator to relay content** — *"the same, by another channel"* | § 3.3 |
| sequential reading | showing the second reader the first reading before the second's own freeze | benchmark § 7 |
| inherited hypotheses | turning an author's *"suggests"* into the reader's *"shows"*; undeclared `DEFAULT_FROM_TEXTBOOK`; inferring from the abstract where full text exists | § 3.3 |
| budget contamination | compressing depth or coverage for token, time or cost — *a reading shortened for budget produces a receipt that overstates itself* | § 3.3 |

**Two contaminations are declared present and are not argued away** (benchmark § 0): session
variance is not separable from mode with one paper; and each reader can read the other's mode
directive, because §§ 4–5 of the protocol are common files. The manipulated variable is *which
directive is addressed to you*, not knowledge that two modes exist.

### 4.4 · The controls required — and the exact limit of each

| Control | What it guarantees | What it cannot reach |
|---|---|---|
| `verify` pre-handover | slots empty; every forbidden prior-output path absent, **none exempt**; no symlink; parity across surfaces; every present file either scanned for the paper's identifiers with 0 hits **or** printed by name under `[UNCHECKED]` — the two **partition** the tree | nothing after handover; the *content* of `[UNCHECKED]` files; an identical change applied to both surfaces, which parity cannot see |
| `verify --post-read` | the same checks with declared outputs excluded; the **blind spot printed by name** on every run | authorship of bytes at the blind-spot path; a file opened by absolute path |
| `freeze` + `verify-freeze` | these bytes under these paths existed when the freeze ran; later change detected **set-wise** — `ADDED · REMOVED · MODIFIED`, enumerated, never by count; identity checked against the tree's own `ASSIGNMENT.md` | a substitution made **before** the freeze; the timestamp is the process's own clock |
| content scan | 0 expected hits for the paper's identifiers in everything that is not the paper; 8 files measured at 0 on 2026-08-18 | a paraphrase that names no identifier |
| the **one** rule with no mechanism | — | *"Neither actor sees the other's first pass until both are frozen"* is `PROCEDURAL`: `GUARANTEE_PROVIDED: none by mechanism — discipline only` |

🔴 **A structural observation the repository states in fragments and this record states whole: the
actor charged with detecting the one unmechanized leak is the actor with the means to cause it.**

Benchmark § 7 names the failure mode as *"Plan reads or relays A's first pass to B before B
freezes"*, and § 4.2 above puts steps 1, 3, 5, 6 and 9 all on Plan. Plan holds both frozen trees,
runs the comparison, and is the only actor positioned to move content between the surfaces. The
detection the protocol offers is after-the-fact and indirect: `FREEZE_TIMESTAMP_UTC` against
`SURFACE_COMMIT`, inspected in B's commit history.

**What would reduce it** — stated as observation, not as a proposal, because a change here is a
governance act and this session may not make one:

```
(a)  a second holder of the frozen trees, so the import is witnessed by an actor that
     did not perform it
(b)  ordering the two freezes so that neither import happens until BOTH receipts exist
(c)  the P7 event ledger with the freeze events written as they occur — which is the
     mechanism the governance already names, is OWED NOT BARRED, and has no writer
```

None of the three is designed here. (c) is the same missing instrument that blocks Mirror's
anti-fossilization guard (§ 3.2) and Mirror's own analysis surface — **one absent object, three
distinct guarantees resting on it.** That coincidence is the strongest argument in this record for
which implementation to do first, and it is recorded as an observation, not as a schedule.

### 4.5 · Two residuals, stated where the claim is

Annex J.0 has no runtime-enforced permissions. An actor can read outside its surface by absolute
path, and the model may carry the paper from training. Neither is a reason to weaken the surface;
both are reasons not to describe it in stronger words than *"the default path is blind and the
evidence path is inside."*

---

## 5 · SCIENTIFIC OUTPUT OBJECT — the seven fields, mapped and measured

> **No schema is created here.** The dispatch asks for evaluation of seven candidate fields. Each
> is measured against what the repository already carries, and the answer for one of them is *do
> not create it*.

### 5.1 · What already exists — three surfaces, one data model, and a standing prohibition

`scientist_reading_modes.md` § 3.5 and § 6 fix the output as **three surfaces**, and § 6.3 forbids
a fourth:

```
READING PROVENANCE   work manifest, schema_version 2, valid under deepdive_manifest.py
LOCATOR FIDELITY     dossier — artifact table with SHA-256, verbatim quotes, surface, anchor
CLAIM ASSERTION      claim candidates: the 12 canonical registry fields
                     + the 7 BENCHMARK/INTERMEDIATE fields + `Locators:`

FORBIDDEN            no claims.json, no claim_schema.yaml, no benchmark_claim_registry.md,
                     no parallel enum for Type, no second locator format.
                     "A reader who finds one of these in a benchmark output has found a
                     protocol violation."
```

### 5.2 · The dispatch's seven, each with its measured home

| Dispatch field | Measured status | Home |
|---|---|---|
| **claim** | ✅ EXISTS | the `## CLAIM <id>` heading + `Title` + `Type` ∈ `DATO · INFERENZA · IPOTESI · ESPANSIONE`, compound allowed |
| **source** | ✅ EXISTS | `Source` + `Wikilinks` → `paper_registry_current#PAPER nnn`; `Source type` on the paper registry |
| **evidence** | ⚠️ **EXISTS — but deliberately NOT as a field of the claim** | the *other two surfaces*: dossier verbatim quotes, and manifest `verbatim_locators.entries[]` (`proposition · snippet · surface · artifact · anchor · panel_text_relation · found_or_sought`). Bound to the claim by `Locators:`, a cross-reference to entry indices |
| **confidence** | 🔴 **DOES NOT EXIST — and should not be created as a scalar** (§ 5.3) | none |
| **limitations** | ⚠️ EXISTS as a **BENCHMARK/INTERMEDIATE** field, `0/39` as a label in the canonical registry | `**Limitations:**` — authors' and the reader's, distinguished |
| **contradictions** | ⚠️ EXISTS as a **BENCHMARK/INTERMEDIATE** field, `0/39` canonical | `**Contradictory evidence:**` — *inside this paper*, or *"none found — searched: <what>"*. Distinct from `Status: conflicting evidence`, which is **cross-paper lifecycle**, measured `1/39` |
| **open questions** | ⚠️ **PARTIAL — carried in three places, none of them a per-claim label** | § 3.6's *"unresolved ambiguities listed rather than absent"*; MODE B's `**What would resolve it:**`; C.2's `RESIDUAL_UNCERTAINTY` + `EVIDENCE_NEEDED` on the review object |

🔴 **Making `evidence` a field of the claim object is the parallel schema the protocol forbids.**
The separation is load-bearing: evidence lives where it can be *digested and audited* — a locator
resolves against the packet by SHA-256, and the blind audit of step 7 operates on
`(proposition, snippet, anchor)` triples that exist only because evidence is a separate surface.
Fold it into the claim and the audit has nothing to audit.

### 5.3 · 🔴 On `confidence` — the one field this record recommends against creating

Measured: `confidence` appears in 42 tracked files, **none of them as a claim-level label**. In
`claim_registry_current.md` it occurs exactly once, inside prose. `REVIEWER_CONFIDENCE` exists in
exactly two files — the governance body and Annex C.2 — and it is a property of a **reviewer's
verdict**, not of a claim.

The repository already separates into **four axes** what a single `confidence` field would collapse:

```
Type                    DATO | INFERENZA | IPOTESI | ESPANSIONE     — epistemic class of the statement
Status                  consolidated baseline (18) | in observation (17) | flagged for review (2)
                        | conflicting evidence (1) | background only (1)  — measured over 39 claims
Transferability         T1 | T2 | T3                                — how far it carries
clinical relevance      HIGH | MEDIUM | LOW | NONE                  — what it would matter for
```

Those four are **separately actionable and not commensurable**: a `DATO` with `T3` transferability
and a `IPOTESI` with `T1` do not average into anything a reader can use. And the repository's own
reporting discipline is explicit against composites — benchmark § 8.5: *"No overall score. No
weighting. Each dimension its own table."*

**Recommendation, stated as analysis and owned by whoever decides it:** the dispatch's
`confidence` is already carried, better, by `Type` + `Status` + `Uncertainty` + `Limitations`. If a
single field is nonetheless wanted, the question to answer first is *what decision would read it*,
because none of the decisions in H.1 currently takes a scalar as input.

### 5.4 · The minimum evidence object, as measured

Stated as what an auditable reading already has to carry, with nothing added:

```
IDENTITY        ## CLAIM <id> · Title · Type
BINDING         Source · Wikilinks · Locators: (indices into the manifest)
SUBSTANCE       Observation (no verb of conclusion) · Author interpretation (marked as theirs)
                · LEGEND interpretation (typed, or "none") · Direction
LIMITS          Uncertainty · Limitations · Contradictory evidence
LIFECYCLE       Status · Transferability · clinical relevance · Impact on Working Model
ELSEWHERE       the evidence itself — dossier quote + manifest entry, digest-resolvable
```

That is 12 canonical + 7 benchmark + 1 cross-reference = **20 labels, all of which already exist**,
and the acceptance test (§ 3.8 step 4) checks exactly the eight-label block *"so the acceptance
test and the schema cannot disagree about what a complete claim is."* Whether any of the seven
benchmark fields is later promoted into `claim_registry_current.md` remains a separate governed
decision after a benchmark outcome exists.

---

## 6 · PILOT DESIGN — a five-paper WWOX pilot, without reading a paper

> **No paper is selected. No actor is assigned. No partition is proposed. Nothing here is
> implemented, scheduled or requested.**

### 6.1 · 🔴 The first finding is that "5 papers" and the governance do not fit, and the misfit is structural

```
body §41 — PRIMO BATCH SCIENTIFICO
  "A/B/C via Task Contract; PICCOLO (1–2 PMID a testa); throughput pieno dal secondo batch."
```

The dispatch's shape — *Input: 5 papers · Process: Scientist A, Scientist B, Mirror* — admits two
readings, and both break something:

| Reading | Load per reader | Result |
|---|---|---|
| **(i) both readers read all five** — five parallel read groups | **5 PMID each** | ❌ exceeds §41's PICCOLO by 3–4× on a *first* cycle. §41 is not a courtesy; the first cycle's stated purpose is *"scienza vera + qualificazione simultanea"* of eleven mechanisms at once |
| **(ii) partition the five, 1–2 each across A/B/C** | 1–2 PMID each ✅ | ❌ no paper has two readers, so **there is no independence to compare** — no `PARALLEL_READ_GROUP`, no comparison matrix, no A/B contamination question at all. It is a throughput cycle, not a pilot of the thing the dispatch is piloting |

**A first cycle cannot be both.** The design that satisfies §41 *and* produces the independence
material is **1–2 papers, both read by two actors** — which is `BENCH-AB-001`, already specified at
one paper, with its own §0 stating what one paper cannot deliver: *"the output is MATERIAL AND
FAILURE MODES, NOT A NUMBER."*

**Two papers instead of one is the smallest change that buys something real** — it is the minimum
at which mode and session variance begin to separate — and it is still inside §41. Five is a
second-batch number. Recorded as **Q-4**, owner operator, because scope is `Strategia complessiva
→ Operatore` (H.1) and this session may not set it.

### 6.2 · Dependencies — what a pilot needs, measured, in the order it needs them

```
D-1  ROLE CONTRACT ACTIVATION      DEC-20260822 consequence 3. Form unspecified.     OPERATOR
D-2  WHETHER THE PROTOCOLS BIND    §2.2 — three clauses satisfied, no object says so OPERATOR
D-3  L2 HOLD LIFTED                L2 SUSPENDED since 2026-08-17; body §8 assigns on
                                   VERIFIED capabilities; all six are UNVERIFIED      OPERATOR
D-4  REGISTRATION OF A AND B       ledger/registrations/ absent on all 7 refs (N-4)   IMPLEMENTATION
D-4a └─ and their worktrees carry no roles/ and are ~200 commits behind, so neither
        can read its own contract without a sync first                                IMPLEMENTATION
D-5  AN ACTIVE LEASE               0 by derivation. No Task Contract without one      ORCHESTRATOR
D-6  SCIENTIFIC SCOPE              which papers. H.1: strategia complessiva           OPERATOR
D-7  THE SURFACES BUILT + FROZEN   manifest is PREPARED — NOT FROZEN (N-7)            PLAN
D-8  BENCH_ROOT DECLARED           its carrier, deployment/local_instance.md,
                                   does not exist                                     PLAN / OPERATOR
D-9  TWO TASK CONTRACTS            none exists for any Scientist (N-5)                ORCHESTRATOR
```

**D-1 and D-2 gate everything after them, and the ordering is not aesthetic.** Registration reads a
contract; a Task Contract names an `OWNER` whose identity a protocol fixes; the surfaces are built
to a protocol's allowlist. If neither contract nor protocol binds, each downstream act rests on a
document that says it binds nobody. Building the surfaces first would not be *wasted* — `build` and
`verify` are deterministic functions of an allowlist and can be re-run — but it would produce a
handover gate whose `PASS` certifies a protocol nobody has said is in force.

### 6.3 · Human gates — which recur per batch, and which are paid once

| # | Gate | Recurs? | Source |
|---|---|---|---|
| HG-1 | **Scientific priority — which papers, in what order** | **per batch** | H.1 *Strategia complessiva → Operatore*. Orchestrator orders *within* a scope; it does not set the scope |
| HG-2 | **Spend / MAJOR approval / governance** | **per batch** | H.1; body §48 — *qualsiasi costo senza HUMAN_APPROVAL* is a stop condition |
| HG-3 | **Persistent scientific disagreement** | **per batch**, when it occurs | C.1 floor **R3 TRIADIC**, derogable only upward; §27 forbids forcing it away |
| HG-4 | **Public push** — a human reading `git diff origin/main..main --stat` | **per push** | *"the one judgement no gate makes"* |
| HG-5 | Role contract activation | once | `DEC-20260822` consequence 3 |
| HG-6 | Whether the protocols bind | once | § 2.2 |
| HG-7 | Lifting the L2 hold | once | operator hold, 2026-08-17 |
| HG-8 | Whether a third position exists and what it does | once | § 3.3 |
| HG-9 | `scientist-c` ACTOR_ID confirmation | once | confirmed at its own registration, I.2 step 7 / PID-12 |
| HG-10 | Anything therapeutic | always | nothing here is medical advice |

**Not human gates, and should stay mechanical:** manifest validation · locator digest matching ·
coverage-map completeness · LINT · receipt-chain verification · release gate · lease derivation ·
duplicate-assignment detection at reconciliation · the set-wise freeze recomputation.

⚠️ **With the caveat the lease record states about itself:** the `PROCEDURAL` layer — *writing a
row at all* — is not mechanized. *"Nothing compels the Orchestrator to record an acquisition, and
nothing runs between turns."* Mechanical checks derive correctly from what they are given and
cannot derive from what was never written down.

### 6.4 · Scaling problems — measured, not estimated

**S-1 · Almost everything per-paper is genuinely per-paper.** Measured from `surface_spec.json`:

```
forbidden_prior_output_paths   23   derived BY GIT GREP FOR THAT PMID — a different paper
                                    yields a different set, and a stale set is a blind spot
source_files                    7   that paper's packet
population                     65 units / 109 panels — that paper's structure
common_files                   11   ← the ONLY part that is reusable across papers
per_actor_files                 2   ASSIGNMENT.md + MODE_DIRECTIVE.md, per reader
```

So *n* papers × 2 readers = **2n surfaces, n surface specs, n populations, 2n freezes, n comparison
matrices, n outcomes**. At n=5: 10 surfaces, 10 freezes, 5 matrices. Only the 11 common files
amortize.

**S-2 · Plan is the serialization point, and it is a single writer by governance.** Steps 1, 3, 5,
6 and 9 of the ten-step sequence are Plan's; §14 fixes `ONE_WRITER_PER_WORKING_DIRECTORY`. Reading
parallelizes across actors; **the freeze/compare/outcome spine does not**. And step 5 has an
ordering constraint that forbids batching: *the freeze happens on the completion declaration and
before Plan reads the content* — so Plan cannot wait for all readings and freeze them together
without making every freeze's timing unshowable.

**S-3 · Review throughput is capped by rule, not by capacity.** Annex C.3: *cap una review attiva
per Scientist*, rotation, never fixed pairs, `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR` for important
reviews, max 2 rounds before adjudication. With three scientists, at most three peer reviews are
open at once and none of them may be authored by its own reviewer. **Five papers generating five
disagreements would queue.**

**S-4 · Mirror is `MIRROR_REQUIRED` at R4, and its input instrument is missing.** Annex G.1 makes
Mirror required for R4, protocols, governance and repeated dissent — the benchmark's own
`REVIEW_REQUIREMENT` is R4. Annex G.3 makes the consolidated J.1 event ledger Mirror's *primary
analysis surface*, *"not by reading fifty chats"* — and `roles/mirror.md` records that capability
as **blocked: the ledger has no writer yet**. Mirror scales by reading a ledger; without one it
scales by reading everything, which is the thing G.3 was written to stop.

**S-5 · The blind audit scales with triples, not papers.** Step 7 spawns fresh agents per
`(proposition, snippet, anchor)` triple, identity withheld. A deeper reading produces more triples,
so **audit cost rises with reading quality** — the correct direction, and the reason the step is the
one under time pressure. Any cap here must be logged: a silent top-N reads as full coverage.

**S-6 · The one cost that does NOT scale with papers.** D-1 … D-3 and HG-5 … HG-9 are one-time
unblocking acts. Of the ten human gates in § 6.3, **six are paid once and four recur.** The
dispatch's scalability goal is reachable for the recurring set, and only after the one-time set is
discharged by someone with the authority to discharge it. **That authority is not held by this
session.**

### 6.5 · What a pilot must produce even when it fails

A reading declared complete **without `verbatim_locators.entries[]` is not complete**, and the
freeze does not repair it: *the freeze records what was in the tree, it does not confer the depth
that was not.* Such a reading scores `EVIDENCE COVERAGE` and `PROVENANCE` on an empty locator set,
and step 7 has no triple to audit — which is the measurable form of the same statement, and the
reason it is a precondition rather than an outcome.

---

## 7 · HANDOFF TO ORCHESTRATOR

### 7.1 · 🔴 There are two routes, and the dispatch describes only one of them

```
dispatch:   Scientist completion → handoff → Orchestrator decision
```

Measured, that is the **ordinary Task Contract route**. Under a benchmark it is not the route:

```
ORDINARY     Scientist --TASK_COMPLETE--> Orchestrator                    Annex A.5, B.2
BENCHMARK    Scientist --completion declared--> PLAN (for FREEZE, before anyone else reads it)
             reading_modes §3.7; benchmark §5 step 4→5
```

**The difference is not stylistic.** If completion goes to Orchestrator first under a benchmark,
the freeze happens after someone has read the content, and *a freeze taken after reading is a
freeze whose timing cannot be shown*. Whichever pipeline is built must know which route it is on.

### 7.2 · What returns — derived from what Orchestrator may actually decide

The right way to fix the return set is not to list plausible fields; it is to take H.1's decision
rows for Orchestrator and ask what each one needs as input. Done that way, the set is closed:

| Orchestrator decision (H.1) | What it needs from a completion | Carrier that exists |
|---|---|---|
| **Task / priority / reassignment / generation** | that the task reached `COMPLETE`, at which `GENERATION` and `DIRECTIVE_VERSION` | `TASK_COMPLETE` + Annex B.1 envelope (`TASK_ID / ACTOR_ID / FROM / TO / TYPE / STATE_CHANGE / DURABLE_POINTER`) |
| **Ladder level (≥ floor) and reviewer** | the **class** of the object produced: L1 observation · L2 inference · therapeutic-actionable · persistent disagreement · methodology-changing | the claim candidates' `Type` + `clinical relevance`, and — for the disagreement class — the comparison matrix's disagreement flag. C.1's floors are keyed to exactly these classes |
| **Classificazione HUMAN_REQUIRED ordinaria** | whether anything hit a human gate of § 6.3 | `BLOCKER` · `HUMAN_REQUIRED` message types |
| **Aggiudicazione challenge** | that a challenge was raised, and on what | `DISSENT` (Annex F) |
| **CANONICAL_BATCH_COMMIT** | 🔴 **nothing directly.** A reading does not reach the canon from the reader; it reaches it through Plan's `INTEGRATION_CANDIDATE` with manifest and hash (Annex D) | not the completion message |
| **The scientific conclusion** | 🔴 **nothing, ever.** *Orchestrator controls what work is done, by whom and in which order. It does not control what scientific conclusion an agent must reach* | — |

### 7.3 · The completion payload, measured

`scientist_reading_modes.md` § 3.7 fixes it, and every element is checkable by the recipient:

```
TYPE               TASK_COMPLETE                                             Annex B.2
DURABLE_POINTER    → the output tree                                         Annex B.1
                   + its TREE DIGEST
EVIDENCE STATUS    the manifest validator's VERDICT LINE
                   (deepdive_manifest.py --verify-artifacts --require-current-schema)
                   + the COVERAGE MAP  (complete ⇔ no `not_read`)
UNRESOLVED         the listed ambiguities;  MODE B: the critical-reading record entries,
                   each with `What would resolve it`
ACK                mandatory — STATE_CHANGE: yes.  Absent → resend (dedup by MESSAGE_ID);
                   second failure → BLOCKER
```

**Keying:** `ACTOR_ID` is identity, `FROM` is routing. Nothing in a completion, claim, checkpoint or
receipt is keyed by `SESSION_REF`; all are keyed by `ACTOR_ID + TASK_ID + GENERATION`.

**The measured failure class is not hypothetical** (Annex B.3): *"ACK emesso ma lavoro mai partito
(classi misurate: turno troncato, permission prompt)"*, recovery `DIAGNOSE` (F.4) — *mai
classificare come rifiuto un guasto di runtime.*

### 7.4 · 🔴 The gap — "remaining workload" has no carrier

**No Annex B message type and no Annex A field carries remaining workload.** Nearest instruments:
`STATUS_UPDATE`, `HEARTBEAT` (fixed cadence, feeds the DOWN timeout), and Plan's reconciliation over
`ledger/tasks/*/`. Creating one is a schema change and **is not done here**.

This reproduces the orchestrator record's § 6.3 gap independently, and adds one consequence that
matters for § 6's scaling: **without it, Orchestrator's priority decision at n>1 papers is made
without knowing what is left**, and the only available proxy is the milestone plan's durable
evidence — which reports what is *done*, never what remains.

### 7.5 · What a completion must NOT carry

A `BLOCKER` from a reader **is answered on the protocol, never on the paper**. Orchestrator may
supply the source packet, the mode directive addressed to that reader, the identity and task
fields, the `PARALLEL_READ_GROUP`, the interaction mode, the review requirement, the milestone plan
and the deliverable. It must withhold the other reader's output, any prior LEGEND output on the
paper, and any relay of paper content — *"the same, by another channel"* is the contamination class
that exists precisely to name this.

---

## READINESS

### 8 · What is executable now, and what is not

**READY — no new decision required:**

| # | Capability | Evidence measured this session |
|---|---|---|
| R-1 | Read both protocols as canonical content and design against them | `4454fea` is an ancestor of `main`; both files present, 526 + 748 lines |
| R-2 | Run the benchmark tooling | `benchmark_input_surface.py --help` executed; 7 subcommands; 1558-line test suite |
| R-3 | Use a fixed evaluation population | `population/evidence_units.json` — 65 units, 109 panels, `main_table: 0` measured |
| R-4 | Derive lease state | `lease_state.py` ran; `ACTIVE by derivation: 0` |
| R-5 | Read approval state correctly **across refs** | done in § 2.2; reading one ref alone is wrong |
| R-6 | Analyse, prepare and record — this class of work | done here, without touching a governed object |

**NOT READY — grouped by what would unblock it:**

```
OPERATOR DECISION      D-1 role contract activation (form unspecified)
                       D-2 whether the two protocols bind
                       D-3 lifting the L2 hold — all six capabilities UNVERIFIED
                       D-6 scientific scope — which papers
                       Q-3 whether a third position exists and what it does
                       Q-4 pilot size: 5 papers vs §41's PICCOLO

GOVERNANCE CLARIFY     Q-2 a binding protocol whose addressee set is defined by a
                           contract an operator has determined non-binding
                       promotion of PARALLEL_READ_GROUP into Annex A
                       MIRROR_RETROSPECTIVE cadence N (ESC-3, assigned to nobody)

IMPLEMENTATION         D-4 registration of scientist-a / scientist-b — and D-4a, their
                           worktrees carry no roles/ and are ~200 commits behind
                       D-7 surfaces built, verified, frozen  (PREPARED — NOT FROZEN)
                       D-8 BENCH_ROOT has no carrier
                       D-9 two Task Contracts — and issuing one needs an ACTIVE lease
                       the J.1 event ledger's WRITER — §4.4(c): one absent object,
                           three distinct guarantees resting on it
                       a carrier for "remaining workload" (§7.4) — a schema change
```

**Nothing in the NOT_READY column is unblocked by more analysis.** Iterations 2 and 3 of this task
cannot move any of it; only the named owners can. What iterations 2–3 *could* do is answer a
narrower question that is inside this session's competence, if one is dispatched.

---

## OPEN_QUESTIONS

### 9 · Recorded, not resolved — each with a disposition owner who is not this session

| # | Question | Owner |
|---|---|---|
| **Q-1** | Do `scientist_reading_modes.md` and `controlled_benchmark_ab.md` bind? All three activation clauses measure SATISFIED (§ 2.2) — including the `HUMAN_APPROVAL` visible only on ref `orchestrator` — while the status lines have never been modified and no object records the satisfaction. | operator (H.1) |
| **Q-2** | Does a protocol whose `applies_to` set is *"every actor under `roles/scientist.md`"* have an addressee set at all, now that `DEC-20260822` has **determined** that contract non-binding? Before the decision this was a reading; now it is a determination, and the coupling is unadjudicated either way. | operator (H.1) |
| **Q-3** | Does a third position exist in a reading cycle, and if so is it (i) a third equivalent reading or (ii) synthesis/adjudication over two frozen passes? (ii) collides with § 27, H.1 and C.3. **No recommendation is made here**, for the reason in § 3.3. | operator |
| **Q-4** | Pilot size. Five papers cannot satisfy both §41's PICCOLO and the requirement that a paper have two readers (§ 6.1). Which property yields? | operator (H.1 — scope) |
| **Q-5** | Are future `scientist-d`/`scientist-e` intended as **further equivalent readers** (supported; a five-step configuration delta) or as **integration/synthesis functions** (unsupported; collides with § 27, H.1, C.3 *and* § 28's existing allocation of integration to Plan — § 3.4)? | operator |
| **Q-6** | Should a claim-level `confidence` field exist at all? Measured: none exists; four separable axes already carry what it would collapse; § 8.5 forbids composites. **What decision would read it?** | operator / Mirror (epistemic curation) |
| **Q-7** | The unmechanized contamination rule (*"neither actor sees the other's first pass until both are frozen"*) is detected only after the fact, by the actor best positioned to violate it (§ 4.4). Does the pilot proceed on discipline, or does the J.1 ledger's writer come first? | operator / Plan |
| **Q-8** | `HUMAN_APPROVAL_QUEUE.jsonl` diverges 6 / 6 / 10 lines across `HEAD` / `main` / `orchestrator`. Which ref is authoritative for approval state, and what reconciles them? | Plan / operator |
| **Q-9** | `DEC-20260822` consequence 5 records `REV-ROLES-MIRROR-001`'s `AUTHOR_RESPONSE` as *"required and outstanding"*. It was written 8 minutes after that decision was committed, on **this** branch (`de0ae4e`), and `main` cannot see it. Is the consequence discharged? | operator (adjudicator) |

---

## VALIDATION

### 10 · Constraint compliance — checked, not asserted

| Constraint from the dispatch | Result |
|---|---|
| `MUST NOT` modify `governance/` | ✅ untouched — `git status --porcelain` shows one added file, under `learning/plan/` |
| `MUST NOT` modify `roles/` | ✅ untouched |
| `MUST NOT` modify `framework/` | ✅ untouched |
| `MUST NOT` modify `ledger/` | ✅ untouched |
| clean worktree | ✅ clean at session start; the single change is this file |
| only `learning/plan` modified | ✅ exactly one path added |
| this is NOT paper analysis | ✅ no full text opened, no PMID pursued, no receipt written, zero claims formed |
| do NOT read biomedical literature | ✅ none read. The one PMID that appears (42397075) appears **only** as the benchmark's configured subject, read from a manifest field, never from a paper |
| do NOT create scientific conclusions | ✅ none |
| do NOT modify or activate Scientist contracts | ✅ § 1.2 and § 2.1 record their state; nothing acts on it; no actor was contacted, spawned or assigned |
| identity from repository evidence only | ✅ § 1 — branch, HEAD, worktree, lease, all by command |
| authority NOT assumed from `roles/plan.md` | ✅ § 1 — the file is non-binding by operator determination, and the one act performed traces to H.1's `WORK_COMMIT` row |
| do NOT create schemas | ✅ § 5 evaluates fields against existing homes and **recommends against** creating the one that has none |
| do NOT assume Scientist C is synthesis | ✅ § 3.3 — measured as affirmatively unsupported, with the three collisions named, and no recommendation made |

### 10.1 · What this record does NOT do

It does **not** activate any contract or perform the act `DEC-20260822` consequence 3 requires ·
does **not** claim Orchestrator authority or take a lease · does **not** assign a paper, an actor,
a batch, a mode or a review · does **not** resolve Q-1…Q-9 · does **not** create a Task Contract, a
`PARALLEL_READ_GROUP`, a Mirror task, a ledger event or a message · does **not** build, verify or
freeze a surface · does **not** create a schema, a field or a vocabulary · does **not** verify a
capability or lift a hold · does **not** design a Scientist C, D or E arm · is **not** an
`AUTHOR_RESPONSE`, an `INTEGRATION_CANDIDATE` or a `CANONICAL_BATCH_COMMIT`.

### 10.2 · Domain and collision disclosure

- **Content domain.** `learning/` is not a `CONTROL_PLANE_ROOT` (P5.1). This file is inside the
  `CANDIDATE_CONTENT_HASH` of any future candidate including this branch and moves it. Disclosed.
- **No base condition invalidated.** No open candidate declares `2394b07` as its `BASE_HEAD`.
- **Cross-ref reads were reads.** `main` and `orchestrator` were read via `git show <ref>:<path>`.
  Nothing was merged, checked out, or written outside this worktree.
- **Seat.** `learning/plan/` on this ref holds 24 files: 21 `SLR-plan-*`, one `HANDOFF-*`, one
  boundary analysis and one readiness analysis. This record takes a non-`SLR` name for the same
  reason those two did.

---

## NEXT_TRANSITION

```
FROM   iteration 1/3 — the execution model is analysed against measurement; five dispatch
       sections answered; nine questions recorded with owners; one artifact created

TO     nothing this session can enter.

WHY    Every dependency in §6.2 and every row of the NOT_READY column is owned by the operator,
       by a governance clarification, or by an implementation act that requires one of the first
       two to precede it. Analysis cannot move any of them.

THE FOUR ORDERING FACTS WORTH CARRYING FORWARD:

  1  D-1 and D-2 gate everything downstream. Registration reads a contract; a Task Contract
     names an OWNER a protocol fixes; the surfaces are built to a protocol's allowlist. If
     neither binds, each act rests on a document that says it binds nobody.

  2  ONE ABSENT OBJECT CARRIES THREE GUARANTEES. The J.1 event ledger has no writer, and
     three separate things rest on it: Mirror's primary analysis surface (G.3), Mirror's
     anti-fossilization guard over reading modes (§32), and the only mechanism that could
     move the unmechanized contamination rule from after-the-fact detection toward
     prevention (§4.4). Whoever chooses what to implement first should know they are three
     problems and one object.

  3  THE PILOT SIZE IS A DECISION, NOT AN EFFORT ESTIMATE. Five papers and body §41 cannot
     both hold in a first cycle that also produces independence material. Two papers is the
     smallest number that buys anything the one-paper benchmark cannot, and it is still
     inside §41.

  4  APPROVAL STATE MUST BE READ ACROSS REFS. Four approvals exist only on `orchestrator`.
     Any readiness judgement made from `main` alone, or from this branch alone, is wrong in
     a direction that understates how much has been approved.

WHAT THIS SESSION HANDS OVER:
       this record. No recipient is named — session routing is unresolved repository-wide
       and no destination is invented here.
```

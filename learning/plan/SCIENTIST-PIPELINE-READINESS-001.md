---
artifact: READINESS ANALYSIS — the Scientist pipeline, before any paper is read
record_id: SCIENTIST-PIPELINE-READINESS-001
task_id: SCIENTIST_PIPELINE_READINESS_ANALYSIS_v1
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

naming_note: >
  `learning/plan/` holds `SLR-plan-NNNN` records by convention (Annex E.6) plus one non-SLR
  handoff. This is neither a Session Learning Record nor a handoff; it is named accordingly and
  takes no SLR number it has not earned. Annex E.6 governs the SLRs; it does not govern this.

domain: >
  CONTENT. `learning/` is content by intent — it is not among the exhaustive
  `CONTROL_PLANE_ROOTS` of `governance/plan_defined_parameters.md` § P5.1
  (`governance/candidates/`, `ledger/`, `reviews/`). This file therefore sits inside the
  `CANDIDATE_CONTENT_HASH` of any future candidate that includes this branch, and it moves that
  hash. Disclosed in § 9.2, not discovered later.

relation_to_prior_work: >
  `learning/orchestrator/SCIENTIFIC-PIPELINE-PREPARATION-001.md` (branch `main`, `788c357`)
  covers overlapping ground from a BOOTSTRAP_MODE session. It is NOT on this branch. Its factual
  claims are treated here as claims to re-measure, not as inputs. Where this record agrees with
  it, the agreement is stated; where it diverges, the divergence is named with the measurement.

verdict_transfer: >
  NONE. Every mechanical fact below was executed in this session at the HEAD named in § 1.
  Nothing is carried from a prior report, handoff, manifest field or conversation.
---

# SCIENTIST PIPELINE READINESS — 001

> **This record analyses. It decides nothing, assigns nothing, activates nothing and reads no
> scientific paper.** Every gap it names belongs to someone with authority this session does not
> hold.

---

## TASK_STATUS

```
TASK_ID          SCIENTIST_PIPELINE_READINESS_ANALYSIS_v1
ITERATION        1/3
MODE             READ_ONLY_ANALYSIS · CREATE_LEARNING_ARTIFACT_ONLY
STATE            COMPLETE for iteration 1 — analysis produced, one artifact created,
                 no governance object touched
BLOCKING         none. Nothing in the dispatch required a decision this session could not defer.
DEFERRED         four questions, listed in OPEN_QUESTIONS, each with its disposition owner
```

---

## 1 · IDENTITY — established from repository evidence, not from the dispatch

The dispatch addresses this session as `Plan`. Identity is not conferred by a dispatch, and it is
not read from a contract that says it is not binding.

| Fact | Measured value | Command |
|---|---|---|
| Working directory | `<REPO_ROOT>/.claude/worktrees/evidence-index` | `pwd` |
| Git top-level | identical to the above | `git rev-parse --show-toplevel` |
| Branch | `plan-orchsurf-r4-transcription` | `git rev-parse --abbrev-ref HEAD` |
| HEAD | `de0ae4e961ab28a1f57a28c8eb2440da92b02cb2` | `git rev-parse HEAD` |
| HEAD subject | *"One review was answerable by its author and the other was owed to someone else"*, 2026-08-22T18:09:20+0200 | `git log -1` |
| Working tree | **clean** before this record | `git status --porcelain` → empty |
| Lease | **`ACTIVE by derivation: 0`** — five leases, all STALE or RELEASED, most recent released `2026-08-18T14:05:20Z` | `python3 framework/scripts/lease_state.py` |
| `SESSION_REF` | **not observable, and not invented** — `scientist_reading_modes.md` § 1.2: no actor observes its own routing reference | — |

### 1.1 · What that supports, and what it does not

**Stable actor identity: `plan`.** It rests on two independent durable records, both read at
source: `roles/plan.md` declares `actor_id: plan`, `worktree: evidence-index`; and the Agent Card
registry (`runtime/agent_card_registry.md`, branch `orchestrator`) carries a `plan` card with
`WORKTREE: evidence-index`, `STATUS: REGISTERED_PENDING_L1_L2`, registered 2026-08-17. The
worktree directory name matches both.

🔴 **The branch does not match the worktree name, and that is worth recording rather than
smoothing over.** The worktree is `evidence-index`; the branch checked out in it is
`plan-orchsurf-r4-transcription`. Nothing in the repository requires the two to be equal — Plan's
contract names the *worktree*, not the branch — but a reader matching on branch name will not
find Plan's seat, and the Agent Card's `WORKTREE_HEAD: 620cb420` is 100+ commits stale against
this HEAD. The row is stale in the sense body § 43 means: not authoritative, not thereby wrong
about identity.

**Authority claimed: none.** `roles/plan.md` line 7 reads
`status: PROPOSED — binding once Mirror hostile review passes and the operator approves`, and
`governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` (branch `main`, `788c357`)
determines `OPTION B — ACTIVATION_NOT_CONFIRMED` for all four contracts. Its consequence 2 binds
how this record may be written:

> **No actor authority may be assumed from these contracts.** Any authority an actor exercises
> must be traced to the governance body or to a named annex […] never to a role contract clause
> standing alone.

Every rule cited below therefore names the **body or an annex**. Role contracts appear
descriptively, never as the source of a permission.

The dispatch's own instruction — *"Do not assume authority from `roles/plan.md` if status remains
`PROPOSED`"* — was checked, not assumed: the status line is `PROPOSED` at this HEAD.

---

## 2 · SURFACE_MAP

### 2.1 · Measured ref and refs surveyed

```
MEASURED_REF     refs/heads/plan-orchsurf-r4-transcription
HEAD             de0ae4e961ab28a1f57a28c8eb2440da92b02cb2
MEASURED_AT      2026-08-22T16:29Z … 16:45Z (session clock, UTC)
REFS SURVEYED    35 local heads · 4 remote refs · 5 tags · 17 worktrees
                 Cross-ref searches ran over every local head, not only this one.
```

### 2.2 · 🔴 This branch is not the most advanced ref, and two of the missing commits are the subject

`git rev-list --left-right --count main...HEAD` → **`2  37`**. Merge base `04693e68`.

The two commits on `main` that this branch does not carry are **both directly about this task**:

| Commit | Path added | Bearing |
|---|---|---|
| `2bb2700` 2026-08-22T15:45 | `governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` | determines all four role contracts remain `PROPOSED` |
| `788c357` 2026-08-22T18:01 | `learning/orchestrator/SCIENTIFIC-PIPELINE-PREPARATION-001.md` | a prior preparation pass over overlapping ground |

Both were read in full from the git objects (`git show main:<path>`), **without merging `main`
into this branch and without any write outside this worktree.** An analysis of pipeline readiness
performed only against this branch's tree would have missed the decision that governs whether any
of the contracts binds. Recorded as the concrete instance of the ref-dependence hazard the
preparation record named for the approval queue.

### 2.3 · Relevant objects found — present at the measured ref

**MEASURED_AT `plan-orchsurf-r4-transcription` @ `de0ae4e`.**

| Object | Kind | State |
|---|---|---|
| `roles/scientist.md` | role contract, A/B/C share one file | `PROPOSED` |
| `roles/mirror.md` | role contract | `PROPOSED` |
| `framework/protocols/scientist_reading_modes.md` | protocol `SCIENTIST_READING_MODES` v1, 526 lines | `PROPOSED` — see § 4.2 |
| `framework/protocols/controlled_benchmark_ab.md` | protocol `CONTROLLED_BENCHMARK_AB` v1 / `BENCH-AB-001`, 748 lines | `PROPOSED` — same |
| `governance/candidates/CAND-20260818-SCIENTIST-AB-SPEC.md` | candidate manifest, revision 6, 1736 lines | canonically executed — § 3.1 |
| `governance/candidates/HANDOFF-SCIENTIST-AB-SPEC.md` | operator scope | present |
| `ledger/tasks/plan/SCIENTIST-AB-SPEC-001.json` | task record, OWNER `plan` | `AWAITING_REVIEW` (stale — § 3.1) |
| `framework/eval/benchmarks/BENCH-AB-001/` | 10 files: manifest, `surface_spec.json`, `population/evidence_units.json`, 7 instruction files | built, **manifest NOT frozen** |
| `framework/scripts/benchmark_input_surface.py` + its test | 79 KB + 87 KB, executable | runs; 7 subcommands |
| `framework/eval/failure_taxonomy.md` | 12 reasoning-failure gates | present |
| `reviews/plan/AUTHOR-RESPONSE-SCIAB-MIRROR-006.md` | author response to the ACCEPT review | present |
| `reviews/plan/AUTHOR-RESPONSE-ROLES-MIRROR-001.md` | author response to the roles review | **present here only** — § 3.4 |

### 2.4 · Objects that are cross-ref only — `NOT_FOUND` here is not `NOT_EXIST`

**MEASURED_AT `de0ae4e`** for every "absent" cell.

| Object | At the measured ref | Actually lives at |
|---|---|---|
| `REV-SCIAB-MIRROR-001…006` | absent | branch `mirror`, `reviews/mirror/` |
| `REV-ROLES-MIRROR-001` | absent | branch `mirror` |
| `APR-20260819-SCIAB-001` / `RES-20260819-SCIAB-001` | absent from this ref's queue | branch `orchestrator`, `HUMAN_APPROVAL_QUEUE.jsonl` **line 8** |
| Agent Card registry | absent | branch `orchestrator`, `runtime/agent_card_registry.md` |
| `runtime/runtime_inventory.md` | absent | branch `orchestrator` |
| `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` | absent | branch `main` |
| `SCIENTIFIC-PIPELINE-PREPARATION-001` | absent | branch `main` |

The approval queue's ref-dependence was re-measured, not accepted on report: `main` **6 lines**,
`orchestrator` **10 lines**, this ref **6 lines**. The SCIAB approval exists on exactly one of
them. Reading approval state from this branch alone yields the wrong answer, and this record was
written knowing that.

### 2.5 · Negative claims — each with MEASURED_AT and VALIDITY

| # | Negative claim | MEASURED_AT | VALIDITY |
|---|---|---|---|
| N-1 | **No Task Contract owned by any scientist exists.** `ledger/tasks/` holds five files on this ref, all `OWNER: plan`. Swept over all 35 local heads: every hit is `ledger/tasks/plan/SCIENTIST-AB-SPEC-001.json`, which is Plan's *specification* task, not a reading assignment. | all 35 local heads, 2026-08-22 | until any ref adds a path under `ledger/tasks/scientist-*/` |
| N-2 | **No registration record exists for any actor.** `ledger/registrations/` — the seat `scientist_reading_modes.md` § 1.3 defines — has **zero files on every ref**. | all 35 local heads | until that directory is created on any ref |
| N-3 | **No activation act exists for any role contract.** `status: ACTIVE` and `status: BINDING` have never appeared under `roles/` on any ref. Re-measured this session, independently of `DEC-20260822` E-2. | all 35 local heads | until an activation object is written |
| N-4 | **`deployment/local_instance.md` does not exist.** `deployment/` holds exactly one file, `deployment_profile.md`. `BENCH_ROOT` — the benchmark surfaces' root, which `controlled_benchmark_ab.md` § 2.3 defers to that file — has no carrier. | this ref @ `de0ae4e` | until `deployment/` gains that file |
| N-5 | **No benchmark input surface has been built.** `benchmark_manifest.json` `_state` reads `PREPARED — NOT FROZEN`; `FROZEN_SHA256` is `null`; every `HANDOVER` field is `null`; `COMMON_FILES`, `ALLOWED_PATHS` and `PARITY` all read `DERIVED_AT_BUILD`. | this ref @ `de0ae4e` | until `build` runs and the manifest is frozen |
| N-6 | **No repository object defines a Scientist C *synthesis* function.** One object names a C function at all — see § 6.2 — and it says `adjudication`, inside the peer-review ladder, not synthesis. | all 35 local heads | until such an object is written |
| N-7 | **`lettore` and `lettore-b` carry no `roles/`, no `governance/`, and no `framework/protocols/scientist_reading_modes.md`.** Both are 201 and 203 commits behind `main`, 0 ahead, each with one dirty file. | branch tips, 2026-08-22 | until either branch syncs |

---

## 3 · DISPATCH_VALIDATION

Every concept the dispatch named, checked against repository evidence. **Nothing is silently
created; where the dispatch's vocabulary has no repository home, that is stated rather than
supplied.**

| Concept | Repository source | Status |
|---|---|---|
| **Scientist A** | `roles/scientist.md`; `scientist_reading_modes.md` § 1.1 | **DEFINED** · `ACTOR_ID scientist-a`, worktree `lettore` · identity `FIXED` by a canonically executed candidate, under a protocol whose own status line is unresolved (§ 4.2) |
| **Scientist B** | same | **DEFINED** · `scientist-b`, worktree `lettore-b` · same qualification |
| **Scientist C** | `GOVERNANCE_v3.1.1.md` § 32; `roles/scientist.md` frontmatter | **DEFINED AS AN ACTOR** — § 32: *"Scientist C da creare subito (`lettore-c`), qualificato insieme ad A/B"* · `ACTOR_ID` **`PROPOSED`** · **the dispatch's *functions* for it are partly unsupported — § 6** |
| **Mirror** | `governance/annex_g_mirror.md` (FROZEN); `annex_c_review_protocol.md` § C.2; `roles/mirror.md` | **DEFINED** · role contract non-binding; **Annex G and Annex C bind independently of it** |
| **parallel reading** | `scientist_reading_modes.md` § 2.1–2.2 | **DEFINED**, under the repository's own name: `PARALLEL_INDEPENDENT_READING`, legal only under a shared `PARALLEL_READ_GROUP`; its negative is `DUPLICATED_ASSIGNMENT` |
| **blind review** | `controlled_benchmark_ab.md` §§ 4, 7; `.claude/skills/legend-locator-audit` | **DEFINED — and narrower than the dispatch's usage.** Two distinct objects exist: the **blind first pass** (blindness is a property of the *surface*) and the **blind locator audit** (triples + packet, never the dossier or the reader's name). Neither is a general "blind review", and `scientist_reading_modes.md` § 5.4 states MODE B is *not* a review of MODE A |
| **handoff** | `annex_b_message_protocol.md` § B.2 (`HANDOFF` message type; envelope B.1); `scientist_reading_modes.md` § 3.7; `controlled_benchmark_ab.md` § 5 step 3 (**HANDOVER**) | **DEFINED**, and the two senses are distinct: `HANDOFF` is a message type; `HANDOVER` is the benchmark's writer transfer |
| **learning record** | body § 15; `annex_e_learning_lifecycle.md` § E.6 `Session Learning Record` | **DEFINED** · fields `WORK COMPLETED / PROBLEMS / SOLUTION / LEARNING / MICRO-UPGRADE / IMPACT / CLASSIFICATION / SCOPE / EVIDENCE / LEARNING_ID (+CONFIRMATION_CLASS)`; persisted by `WORK_COMMIT`. The artifact this dispatch asks for is **not** one — see the `naming_note` |
| **evidence extraction** | — | 🔴 **EXTERNAL VOCABULARY.** One occurrence repository-wide, in `disease-models/wwox/mission.md` prose. The repository's objects are the **three surfaces** of `scientist_reading_modes.md` § 3.5 — `READING PROVENANCE` (work manifest), `LOCATOR FIDELITY` (dossier), `CLAIM ASSERTION` (claim candidates) — plus `verbatim_locators.entries[]`. "Extraction" is not a repository term and is not introduced here |
| **literature analysis** | — | 🔴 **EXTERNAL VOCABULARY.** The repository's terms are `DEEP_DIVE`, `PRIMARY_EVIDENCE_READ`, `INDEPENDENT_CRITICAL_READ`, `INGEST`, `BATCH_COMMIT`. Used below only where the dispatch's own scope restriction quotes it |
| **study allocation** | partially | **PARTIALLY DEFINED.** The mechanism exists — Annex A.1 Task Contract with one `OWNER`, plus the `PARALLEL_READ_GROUP` extension field — but "allocation" as a named process does not. § 5 uses the repository's terms |
| **contamination** | partially | **PARTIALLY DEFINED.** `scientist_reading_modes.md` § 3.3 enumerates the forbidden acts and `controlled_benchmark_ab.md` § 0 caveat 2 uses the word *"known contamination of the variable"*. There is no general definition of "contamination"; § 5.3 below assembles one **only** from enumerated rules |

---

## CURRENT_STATE

## 4 · SECTION 1 — What exists, what is approved, what is only proposed, what is unresolved

### 4.1 · EXISTS AND IS CANONICALLY EXECUTED

`CAND-20260818-SCIENTIST-AB-SPEC` revision 6 is **canonical**, and this was verified three ways
rather than read off a manifest field:

```
git merge-base --is-ancestor 4454feab main   → TRUE
git merge-base --is-ancestor 4454feab HEAD   → TRUE
4454fea  2026-08-19T15:08:55+0200  "The Scientist A/B specification becomes canonical, and the
                                    level it blocks at was chosen"
```

Its approval chain, each element read at its own ref:

| Condition | Object | Ref | Value |
|---|---|---|---|
| Mirror hostile review | `REV-SCIAB-MIRROR-006` | `mirror` | `verdict: ACCEPT` — M-5 closed, reviewed from `R-1`, `VERDICT TRANSFER: NONE` |
| `HUMAN_APPROVAL` | `APR-20260819-SCIAB-001` | `orchestrator`, queue line 8 | `STATE: APPROVED`, `RESOLVED_BY: operator`, `2026-08-19T13:02:58Z`, bound to hash `beef6db0…6061` at base `cbce3016` |
| canonical execution | `4454fea` | `main`, `HEAD` | ancestor of both |

The approval also ratifies a **named policy choice**: at pre-handover, an artifact classified
`EXPECTED_BY_PROTOCOL: NO` blocks handover with `rc=1` and the surface is rebuilt, never patched.

**Therefore the following exist as canonical content:** both protocols; `roles/scientist.md` with
A/B/C in one file; the `BENCH-AB-001` instruction set and evaluation population (65 units, 109
panels, `main_table` measured at **0**); `benchmark_input_surface.py` with its 7 subcommands and
its test suite; the failure taxonomy's 12 gates.

### 4.2 · 🔴 PROPOSED — and the two protocols' condition measures as satisfied while the line still says otherwise

`scientist_reading_modes.md` frontmatter:

```
status: PROPOSED — binding on canonical execution of CAND-20260818-SCIENTIST-AB-SPEC, after
  Mirror hostile review and HUMAN_APPROVAL. Until then it binds nobody.
```

All three clauses measure **SATISFIED** (§ 4.1), in the required order, with approval six minutes
before execution. The line has never been modified: `git log --all -S` over the status string
returns only the materialization commit `384f05f`, and the file is **one blob, `2aae1ca7`, on all
10 refs carrying it**.

**This record does not decide whether the protocol binds, and the reason is not caution.** Two
independent facts make it genuinely undecidable from here:

1. `DEC-20260822` answered the structurally identical question `NOT_CONFIRMED` for `roles/`, on
   reasoning that cites *this very protocol* as the repository's gloss on the status grammar
   (*"Until then it binds nobody"*). Extending that determination by analogy would be a
   governance interpretation, and H.1 puts governance with the operator.
2. The protocol's `applies_to` is *"every actor under `roles/scientist.md`"* — and
   `roles/scientist.md` is non-binding. **A binding protocol whose entire addressee set is
   defined by a non-binding contract** is a coupling no object has adjudicated.

This agrees with the preparation record's O-1/O-2 on a re-measurement, not on its report.

### 4.3 · UNRESOLVED — the seven that block execution

| # | Unresolved | Evidence | Owner |
|---|---|---|---|
| U-1 | Role contract activation | `DEC-20260822` consequence 3: *"A new, explicit activation act is required."* It does not perform, schedule or specify it | operator (H.1) |
| U-2 | Whether the two protocols bind (§ 4.2) | three clauses satisfied, status line never changed, no object records it | operator (H.1) |
| U-3 | `scientist-a` / `scientist-b` registration | `STATUS: NOT_REGISTERED`, `ACTOR_ID: UNRESOLVED` in the Agent Card registry (updated 2026-08-17, **before** the 08-19 execution that fixed both IDs); `ledger/registrations/` empty on every ref (N-2) | the actors + the registrar |
| U-4 | L2 capability verification | all six Scientist capabilities `UNVERIFIED`; `controlled_benchmark_ab.md` P-3 records L2 **SUSPENDED** by the C-9 hold (operator, 2026-08-17); no object lifting it found on any ref | operator |
| U-5 | `scientist-c` `ACTOR_ID` | `PROPOSED — confirmed at its own registration` (Annex I.2 step 7, PID-12) | operator / registration |
| U-6 | The third position's function | § 6 | operator |
| U-7 | `ORCHESTRATOR_LEASE` | `ACTIVE by derivation: 0`, measured this session | Orchestrator |

### 4.4 · 🔴 The registry's own state is inverted, and it matters for allocation

| Actor | `ACTOR_ID` state | Registration state | Worktree carries its own contract? |
|---|---|---|---|
| `scientist-a` | **FIXED** (canonical 2026-08-19) | **NOT_REGISTERED** | **no** — 0 files under `roles/`, 0 under `governance/` |
| `scientist-b` | **FIXED** (same) | **NOT_REGISTERED** | **no** — same |
| `scientist-c` | **PROPOSED** | **REGISTERED_PENDING_L1_L2** (2026-08-17, session `lettore-c-b2`) | **yes** — 4 files under `roles/`, 22 under `governance/` |

The two actors whose identities are canonically fixed are the two that are unregistered and whose
worktrees cannot show them their own contract; the actor that is registered is the one whose
identity is still a proposal. Annex I.2 step 7 has each actor read `roles/<its own>.md` at
registration — **neither `lettore` nor `lettore-b` contains that file at its branch tip.** Any
registration attempt from those worktrees today would have to sync first, which is exactly what
`scientist_reading_modes.md` § 1.3 says the registrar answers to a mismatched
`ROLE_CONTRACT_HASH`: *sync, then re-declare*.

### 4.5 · Also true, and not a blocker

`reviews/plan/AUTHOR-RESPONSE-ROLES-MIRROR-001.md` exists **on this branch and no other** (swept
over all 35 heads). It discharges the Annex C.2 obligation the preparation record listed as
outstanding (its HT-9) — but on a branch `main` does not carry, so from `main` the obligation
still reads outstanding. Its disposition: five findings accepted, one contested with evidence;
`MAJOR-3` — the contract asserting a protocol binds while that protocol says it binds nobody —
`ACCEPTED · CHARACTER CHANGED · UNREPAIRED · OPEN`. That finding is U-2 seen from the other side.

---

## SCIENTIST_A_MODEL

## 5 · SECTION 2 — The independence model

Everything in this section is drawn from `scientist_reading_modes.md` §§ 3–5 and
`controlled_benchmark_ab.md` §§ 0, 2, 4, 7. **No new obligation is invented.**

### 5.1 · Scientist A

```
PURPOSE     MODE A · PRIMARY_EVIDENCE_READ — "the reader of what the paper shows".
            Produce the primary scientific reading: what was done, what was found, in what
            system, with what strength, so that a claim candidate can be built on it AND a
            second reader can attack it.
            MODE A is not "read charitably". It is "read completely, and say what is there,
            at the level at which it is there".
```

**Inputs allowed** — `§ 3.1`: *a source packet and nothing else about the paper*. Article binary,
article text surface, supplements as listed by the Task Contract or, in a benchmark, by the input
manifest. Under `BENCH-AB-001` the reader works **in the allowlisted surface, not in its LEGEND
worktree**, because a LEGEND checkout has already worked the paper — at `BASE_HEAD cbce3016`,
**21 tracked files name PMID 42397075**, so a first pass run there *is blind only by promise*.

Also in the surface, and identical for both readers: `roles/scientist.md`,
`epistemic_discipline.md`, `gold_is_in_the_details.md`, `fulltext_read_receipt.md`,
`scientist_reading_modes.md`, `failure_taxonomy.md`, the two validators, and the common
instruction files.

**Outputs expected** — the three surfaces of `§ 3.5`, and **no parallel schema**:

| Surface | Artifact | Validator |
|---|---|---|
| `READING PROVENANCE` | work manifest, `schema_version 2` | `deepdive_manifest.py --verify-artifacts --require-current-schema` |
| `LOCATOR FIDELITY` | dossier in `fulltext_dossiers/*.md` form — artifact table with SHA-256, verbatim quotes, surface, anchor | — |
| `CLAIM ASSERTION` | claim candidates in `claim_registry_current.md` section form: the **12 canonical fields** + the **7 BENCHMARK/INTERMEDIATE fields** + `Locators:` — **not written to the registry** | acceptance test step 4 |

The seven benchmark fields exist because each was measured at **0/39** as a label in the claim
registry: `Observation`, `Author interpretation`, `LEGEND interpretation`, `Direction`,
`Uncertainty`, `Limitations`, `Contradictory evidence`. The first four exist because *the one
thing a second reader must be able to attack is the seam between what was observed and what was
concluded, and today that seam is inside a paragraph.*

### SCIENTIST_B_MODEL

### 5.2 · Scientist B

```
PURPOSE     MODE B · INDEPENDENT_CRITICAL_READ — "the reader of what the paper does not show".
            Shares MODE A's core IN FULL — same completeness, same outputs, same discipline —
            and IN ADDITION searches explicitly, on eleven mandatory axes, for what the paper
            does not establish.
            It is a reader, not a reviewer of A: it never sees A's output during a blind first
            pass, it does not adjudicate A, and it is not asked to agree with A.
```

**Inputs allowed:** byte-identical to A's, with exactly **two** files differing —
`ASSIGNMENT.md` (identity, by necessity) and `benchmark/MODE_DIRECTIVE.md` (the experimental
variable). `verify` reports a third differing file as a broken benchmark.

**Outputs expected:** A's three surfaces, **plus** a critical-reading record — *"a fourth file,
not a fourth data model"* — with one entry per finding:
`axis · target (claim candidate id or locator index) · statement · locator(s) · what would
resolve it`. Entries are typed like everything else and are anchored, so the same blind locator
audit can be run over them.

The eleven mandatory axes: `CONTRADICTORY_EVIDENCE`, `NEGATIVE_EVIDENCE`, `OVERCLAIM`,
`UNSUPPORTED_INFERENCE`, `MODEL_DEPENDENCE`, `RESULT_VS_INTERPRETATION`, `METHODS_STATISTICS`,
`ALTERNATIVE_EXPLANATION`, `CONTEXT_COLLAPSE`, `OMISSION`, `UNSUPPORTED_MECHANISTIC_LEAP`.

**Each axis is answered with findings or with an explicit *"searched; none found"* plus what was
searched. Silence on an axis is incompleteness, not a null result.**

### 5.3 · What constitutes contamination

Assembled **only** from enumerated rules; the umbrella word is the dispatch's, the contents are
the repository's.

| Class | The act, verbatim in substance | Source |
|---|---|---|
| **shared context** | working in a checkout that contains prior LEGEND output on the paper — 21 such files at `BASE_HEAD` | `benchmark` § 2.1 |
| **seeing previous conclusions** | *reading the other reader's output, or **any** prior LEGEND output on the paper, during a first pass declared blind* | `reading_modes` § 3.3 |
| **relayed content** | *contacting the other reader during the first pass, **or asking Orchestrator to relay content*** — *"the same, by another channel"* | § 3.3 |
| **sequential reading** | showing the second reader the first reading before the second's own freeze | `benchmark` § 7 |
| **inherited hypotheses** | turning an author's *"suggests"* into the reader's *"shows"*; using general knowledge without declaring it as `DEFAULT_FROM_TEXTBOOK`; inferring from the abstract where full text exists | § 3.3 |
| **budget contamination** | *compressing depth or coverage for token, time or cost* — a reading shortened for budget produces a receipt that overstates itself | § 3.3 |

🔴 **Two contaminations are declared as present and are not treated as defects to be argued
away** (`benchmark` § 0):

1. **Session variance is not separable from mode.** One paper, one session per actor — the
   benchmark cannot separate the effect of the mode from the variance between two sessions. Its
   value is the *material* and the failure modes, **not a number**.
2. **Each reader can read the other's mode directive.** `scientist_reading_modes.md` §§ 4–5 is a
   *common* file, normative for both and not honestly withholdable from either. The manipulated
   variable is therefore **which directive is addressed to you**, not knowledge of the two modes.
   The instruction *"do not speculate about what the other directive says"* is about attention,
   not information.

### 5.4 · What evidence proves independence — and the exact limit of each instrument

Independence is a property of the **surface**, not a promise. Three instruments, and the
repository states what each does and does not guarantee:

| Instrument | Guarantee | Failure mode still possible |
|---|---|---|
| `verify` (pre-handover) | slots **empty**; **every** forbidden prior-output path absent, none exempt; no symlink; parity across the two surfaces; each present file **either** scanned for the paper's identifiers with no hit **or** printed by name under `[UNCHECKED]` with its class and reason — the two **partition** the tree, decided by one predicate | nothing after handover; the **content** of `[UNCHECKED]` files; a change to an allowlisted input applied **identically to both** surfaces, which parity cannot see |
| `verify --post-read` | every forbidden path **except the printed blind spot** still absent; nothing outside the allowlist and the declared outputs present; the same partition | authorship of bytes at the blind-spot path; a file the reader opened by absolute path |
| `freeze` + `verify-freeze` | these bytes under these paths were present **when the freeze ran**; later addition/removal/edit detected **set-wise** (`ADDED · REMOVED · MODIFIED`, enumerated, never by count); actor and benchmark read **from inside the tree** | a substitution made **before** the freeze; the timestamp is this process's clock |

**Read together, the three bound the window and do not close it.** What no combination
establishes is **authorship of bytes at the one colliding path** — the reader's own manifest lands
at exactly the path LEGEND's prior manifest occupies, because `deepdive_manifest.py` derives it
from disease and PMID. That path *is* the blind spot, and `verify --post-read` prints it by name
on every run.

🔴 **And one rule has no mechanism at all.** *"Neither actor sees the other's first pass until
both are frozen"* is labelled `PROCEDURAL`:

```
GUARANTEE_PROVIDED:            none by mechanism — discipline only
FAILURE_MODE_STILL_POSSIBLE:   Plan reads or relays A's first pass to B before B freezes
DETECTION:                     the two receipts carry FREEZE_TIMESTAMP_UTC and SURFACE_COMMIT;
                               inspecting B's commit history against A's freeze time makes a
                               violation VISIBLE AFTER THE FACT, never prevented
RECOVERY:                      the benchmark is void for the second reader; the outcome says so
```

Two residuals are stated where the claim is (Annex J.0 — no runtime-enforced permissions): an
actor can read outside its surface by absolute path, and the model may carry the paper from
training. Neither is a reason to weaken the surface; both are reasons not to describe it in
stronger words than *"the default path is blind and the evidence path is inside."*

### 5.5 · Allocation — what Orchestrator may provide, and what must stay hidden

| # | Rule | Source |
|---|---|---|
| A-1 | Every reading Task Contract names **exactly one `OWNER` (ACTOR_ID)** and the sources it covers. Ownership is **never** inferred from a worktree, a branch, or a file someone has open | `reading_modes` § 2.2 r1 |
| A-2 | Two contracts on one source are legal **only** when both carry the same `PARALLEL_READ_GROUP` naming the protocol and listing the members. Without one → `DUPLICATED_ASSIGNMENT` | § 2.2 r2 |
| A-3 | `PARALLEL_READ_GROUP` is an **extension field** on Annex A.1, introduced by protocol on A.1's *extendible, never removable* clause. Promotion into Annex A is a separate governed change | § 2.2 r2 |
| A-4 | **The actor checks before it claims**: query the receipt ledger and the task ledger for the source. An existing reading or open contract without a shared group → **do not claim**, raise `BLOCKER` naming both records | § 2.2 r3 |
| A-5 | Plan detects `DUPLICATED_ASSIGNMENT` at reconciliation over `ledger/tasks/*/` and routes it to Orchestrator, who adjudicates: `TASK_CANCEL`, generation+1, or a group declared after the fact **with the reason written down**. Duplicates are censused, never lost in silence | § 2.2 r4 |
| A-6 | 🔴 **There is no lock** (J.0). The rule guarantees uniqueness *by construction of the records*: a duplication **cannot exist without leaving two records that contradict each other**. It does **not** guarantee nobody opens the same PDF twice | § 2.3 |
| A-7 | PMID 42422765 is special-cased: the first contract naming it **must cite** `HANDOFF-C-2-PMID42422765` and state single-owner vs group member. A contract omitting it is **refusable by the actor** | § 2.4 |
| A-8 | Batch size for a first cycle: **PICCOLO — 1–2 PMID each**; full throughput from the second batch | body § 41 |
| A-9 | Assignment presupposes **VERIFIED** capabilities. All six are `UNVERIFIED`; L2 is SUSPENDED | body § 8; Annex I.4 |

**What Orchestrator may provide:** the source packet, the mode directive addressed to that
reader, the identity and task fields, the `PARALLEL_READ_GROUP`, the interaction mode, the review
requirement, the milestone plan and the deliverable. **What must stay hidden:** the other reader's
output, any prior LEGEND output on the paper, and any relay of paper content in answer to a
`BLOCKER` — *"a `BLOCKER` from a reader is answered on the protocol, never on the paper"*
(`benchmark` § 4.3).

**What Orchestrator does not set at all**: the conclusion. `roles/scientist.md`, and body § 2
behind it — *what the evidence supports is the responsible Scientist's call, subject to review and
never to an order*. A scientist who disagrees uses the graduated channel of body § 9.1;
disagreement is not a stop condition.

🔴 **Contradiction is not a defect to be resolved by allocation.** Body § 27: forced synthesis is
an error, and `INFERENCE_A + INFERENCE_B + DISAGREEMENT_UNRESOLVED`, explained, is a **legitimate
outcome**.

---

## SCIENTIST_C_ANALYSIS

## 6 · SECTION 3 — The third position

**C is not assumed to exist as a fixed role.** What the repository supports is analysed; the rest
is named as unsupported.

### 6.1 · What is supported

| Claim | Evidence |
|---|---|
| **`scientist-c` exists as an actor to be created** | body § 32: *"**Scientist C da creare subito** (`lettore-c`), qualificato insieme ad A/B"*; Annex I.2 step 4 creates the worktree; `BOOTSTRAP.md` line 197 maps it to `roles/scientist.md` |
| **The worktree exists and is the healthiest of the three** | `lettore-c` @ `908197b`, **clean**, 65 behind `main`, 0 ahead, carrying 4 `roles/` files and 22 `governance/` files |
| **It is the only scientist registered** | Agent Card registry: `STATUS: REGISTERED_PENDING_L1_L2 · ACTOR_ID PROPOSED`, session `lettore-c-b2`, sessionId `86d4c569…`, 2026-08-17 |
| **C is equivalent to A and B, not specialized** | body § 32: *equivalenti — stesso mandato, protocollo, autorità scientifica, obblighi, isolation. **No specializzazioni statiche.*** Soft routing is permitted post-bootstrap on verified capabilities only, as a **soft signal**, under **Mirror's anti-fossilization guard** |
| **A third scientist may ADJUDICATE inside the peer-review ladder** | `APPROVAL-GOV311-DEVIATIONS.md` § *Recorded principle*: *"For critical matters, the ladder extends: Scientist A → Scientist B hostile review → **Scientist C adjudication** → Orchestrator escalation."* It rests on Annex C.3's `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR` and C.1's R3 TRIADIC floor — *"which is the three-scientist shape above"* |

### 6.2 · 🔴 What is NOT supported — and the exact distance

The dispatch offers four candidate functions. They do not all land in the same place.

| Dispatch function | Repository status | Collides with |
|---|---|---|
| **synthesizes** A and B | 🔴 **UNSUPPORTED.** N-6: no object anywhere defines a synthesis function for C | body § 27 — *"la sintesi forzata è un errore"*; § 28 — Plan's epistemic boundary means nobody in the integration layer resolves contested meaning |
| **adjudicates** | ⚠️ **SUPPORTED IN ONE SHAPE ONLY** — as `ADJUDICATOR` of a **peer review** opened through Orchestrator under C.3, on a *claim*. **NOT** as adjudicator of two independent first passes, and **NOT** of a challenge: `annex_h_authority_matrix.md` § H.1 puts *aggiudicazione challenge* with **Orchestrator** | H.1 |
| **challenges** | ⚠️ **PARTIALLY.** Any Scientist may challenge under body § 9.1 / Annex F. But a challenge is not a role assigned to a third actor, and *"a second reader is a second reader"* — `reading_modes` § 5.4 | § 5.4 |
| **identifies unresolved questions** | ✅ **SUPPORTED, and already every reader's obligation, not C's specialty.** *"Unresolved ambiguity is a legitimate output"* (§ 3.4); a reading is complete only when ambiguities are **listed rather than absent** (§ 3.6) | — |

**What C must NOT do** — each traced to a source, none invented:

- **must not be a fixed specialization.** Body § 32 forbids static specializations; a mode that
  stops rotating *has become* one, and that is what Mirror's anti-fossilization guard watches for;
- **must not force consensus** (body § 27);
- **must not adjudicate a challenge** — H.1 gives that to Orchestrator with rationale;
- **must not review a first pass it was not opened to review** — peer review is opened **only via
  Orchestrator**, rotating, never fixed pairs, at most one active review per Scientist, at most
  two rounds before adjudication, with a mandatory `AUTHOR_RESPONSE` (C.3);
- **must not be a second Mirror.** Mirror's object is the **process**; a Scientist's object is the
  **paper** (§ 5.4). *"Mirror is not made redundant by a critical reader."*

### 6.3 · Unresolved decisions about C

```
U-5   scientist-c's ACTOR_ID is PROPOSED, confirmed at its own registration (I.2 step 7, PID-12)
U-6   whether a third position exists in a reading cycle at all, and if so what it does.
      Two readings are available and NEITHER is chosen here:
        (i)  a THIRD READING — same equivalence, a mode on a task — §32-compatible
        (ii) synthesis/adjudication over two frozen first passes — collides with §27 and H.1
      The benchmark explicitly does NOT run one: controlled_benchmark_ab.md §10 lists
      "run a Scientist C arm" among the things it does not do.
```

An actor choosing the reading that gives it a role is exactly the convenient interpretation the
gate exists to prevent — Mirror declined a structurally identical question on that ground in
`REV-ROLES-MIRROR-001` § 8, and that reasoning applies here with equal force.

---

## MIRROR_EVALUATION_MODEL

## 7 · SECTION 4 — What Mirror evaluates, and what it must not

### 7.1 · The object is the process, and the boundary is normative, not stylistic

| | MODE B | Mirror |
|---|---|---|
| Object | the **paper** — its evidence and its inferences | the **process** — how the laboratory reasoned, reviewed and recorded |
| Authority | a Scientist's: *what the evidence supports* | epistemic / method review; MAJOR classification when in doubt |
| Sees both readings? | **no**, during a blind first pass | **yes, after freezing** |
| Output | a reading with a critical record | a review under Annex C.2; adjudication of the **method** |

Mirror holds **no command** over any actor and produces **no primary evidence**. Its review of
Orchestrator is *ex post and pattern-based — never a veto before the fact* (Annex G, `roles/mirror.md`).

**So the dispatch's framing is repository-supported:** Mirror does not evaluate whether a
scientific conclusion is correct by itself. `controlled_benchmark_ab.md` § 8.2 makes this
operational — the single dimension that *is* scientific judgment, `MECHANISTIC VALUE`, is
**recorded descriptively and deferred**: *"the judgment of value is not made inside the benchmark"*,
it goes to an Annex C review opened by Orchestrator, outside the record.

### 7.2 · What Mirror does evaluate — the five the dispatch names, each with its repository carrier

| Dispatch axis | Carrier that already exists | Route |
|---|---|---|
| **evidence handling** | `PROVENANCE` and `LOCATOR FIDELITY` dimensions: every locator's artifact ∈ `ALLOWED_PATHS` with matching digest; manifest `PASS` under `--verify-artifacts --require-current-schema`; coverage map consistent with where locators come from (*a supplement locator against `Supplementary: not_read` is an inconsistency*) | **mechanical** (Plan) + blind agents |
| **uncertainty tracking** | the 7 benchmark fields — `Uncertainty`, `Limitations`, `Contradictory evidence` present and separable; listed ambiguities; `RESIDUAL_UNCERTAINTY` and `EVIDENCE_NEEDED` in the C.2 format | presence mechanical; **substance adjudicated** |
| **observation / inference / hypothesis** | `EPISTEMIC DISCIPLINE` dimension: every carried statement typed `DATO / INFERENZA / IPOTESI / ESPANSIONE`; `Observation` **free of conclusion verbs**; `Author interpretation` marked as theirs; **hypothesis→observation promotions found by audit** | presence mechanical; **substance Mirror's** |
| **unsupported claims** | `CLAIM PRECISION` — per triple: `SUPPORTED · OVERSHOOT · UNDERSHOOT · NOT_IN_SOURCE · UNVERIFIABLE_SURFACE`; per claim: `Type` claimed vs `Type` the audited evidence bears | **blind agents**, then Mirror for the `Type` question |
| **reproducibility of reasoning** | `verbatim_locators.entries[]` with `panel_text_relation`, `found_or_sought`, `contradicts`/`qualifies` — **this *is* the reasoning trace**; MODE B's critical record with *what would resolve it*; the freeze receipts | mechanical + adjudication |

Two of Mirror's metrics are its specific responsibility and are calibration, not judgment
(`roles/mirror.md`, Annex A.6/A.7): the **checkpoint invalidation rate** and the **redone-work
ratio**.

### 7.3 · Failure patterns to capture — the repository already enumerates them

**`framework/eval/failure_taxonomy.md` — 12 reasoning-failure gates**, each learned from a real
observed error, not synthesized for a benchmark. The ones a reading can trip:
`MECHANISTIC_OVERTRANSFER` · `NMD_LAST_EXON` · `DEGRADATION_DIRECTION_GATE` ·
`MECHANISM_DIRECTNESS_GATE` · `PROTEIN_STATE_IDENTITY_GATE` · `REPORTER_IDENTITY_GATE` ·
`TARGET_ATTRIBUTION_GATE` · `KG_EDGE_HAS_NO_SIGN` · `SOURCE_INTEGRITY` ·
`READING_DEBT_FALSE_NEGATIVE` · `EXTERNAL_DOSSIER_CANONICAL_DRIFT_GATE` · `PREMISE / PUBLICATION`.

> **The keystone is the permanent false negative** — *a correct lead discarded on an unexamined
> premise and never revisited.* Every gate above, when it fires wrongly, can *create* one. That is
> why every rejection records a `REVIVAL_TRIGGER`.

Plus the process-level patterns the repository has measured on itself and that a first cycle
should be watched for: **an axis answered by silence** rather than by *"searched; none found"*; **a
reading shortened for budget**; **the blind locator audit skipped** — step 5 of the acceptance
test, *"the one that catches a careful reading that says more than its source"*, and *the step
that is skipped first under time pressure*; and **mode fossilization**, a mode that stops rotating.

### 7.4 · Learning signals — the existing channel, not a new one

Body § 15 fixes the outcomes: `MICRO_UPGRADE | BEST_PRACTICE_CANDIDATE | FAILURE_PATTERN |
MACRO_UPGRADE_CANDIDATE | NO_NEW_LEARNING` — the last *valid only as an explicit outcome*. Body
§ 16 makes the learning pipeline *"un prodotto fondamentale"*, not a by-product. Annex E.6 fixes
the record's fields. Body § 46: **Mirror asks WHY, never WHO WON** —
`noise vs individual strength vs reusable strategy vs systemic weakness`, distinguished before
anything is promoted.

Two constraints on Mirror's own signals, both binding independently of `roles/mirror.md`:

- **Annex G.2 — Mirror may not self-approve** material changes to its review rubric, learning
  clustering, active-learning selection, review-yield methodology or autonomy-classification
  methodology. Route: `MIRROR_UPGRADE_PROPOSAL` → Plan candidate → an independent reviewer chosen
  by Orchestrator → validation; governance → operator.
- **Annex E.2 gives epistemic curation of learning to Mirror; durability to Plan.** A
  `CONFIRMATION_CLASS` is **proposed**, never self-certified.

### 7.5 · 🔴 Two preconditions on Mirror's own input are not satisfied

1. **Annex G.3 makes the consolidated `EVENT LEDGER` (J.1) Mirror's primary analysis surface** —
   *not by reading fifty chats.* `roles/mirror.md` records the matching capability as
   *"Event ledger analysis — **blocked: the ledger has no writer yet**"*, `UNVERIFIED`. Mirror's
   stated analysis surface depends on an instrument with no writer.
2. **`REV-ROLES-MIRROR-001` left `roles/mirror.md` with no verdict**, under the self-review
   prohibition. The one contract that would govern the evaluator is the one contract no hostile
   review has been able to reach.

---

## READINESS_MATRIX

## 8 · SECTION 5 — Execution readiness

### 8.1 · READY — what can already happen, with no new decision

| # | Capability | Evidence it is ready |
|---|---|---|
| R-1 | **Read both protocols as canonical content and design against them** | `4454fea` is an ancestor of `main` and of this HEAD; both files present, 526 + 748 lines |
| R-2 | **Run the benchmark tooling** | `benchmark_input_surface.py` executes; 7 subcommands (`build · verify · freeze · verify-freeze · population · locators · tree-digest`); an 87 KB test suite ships beside it |
| R-3 | **Use a fixed evaluation population** | `population/evidence_units.json` — 65 units, 109 panels, counts including a measured **0** for `main_table`; its digest goes in the manifest so it cannot be redefined after the readings exist |
| R-4 | **Compose role fingerprints** | `governance_fingerprint.py compose --all` emitted four values in this worktree this session |
| R-5 | **Derive lease state** | `lease_state.py` ran and returned `ACTIVE by derivation: 0` |
| R-6 | **Enumerate duplicated assignments** | the rule and the reconciliation shape exist; `ledger/tasks/*/` is readable |
| R-7 | **Analyse, prepare, and record** — this class of work | done here without touching a governed object |

### 8.2 · NOT_READY — grouped by what would unblock it

**Requires an OPERATOR DECISION:**

| # | Blocked | Why |
|---|---|---|
| B-1 | Role contract activation (U-1) | `DEC-20260822` consequence 3 — a new explicit act is required, and its form is not specified |
| B-2 | Whether the two protocols bind (U-2) | three clauses satisfied, no object records it; `DEC-20260822`'s reasoning cites this protocol's grammar, so extending it by analogy is a governance interpretation |
| B-3 | Lifting the C-9 hold on L2 (U-4) | L2 SUSPENDED since 2026-08-17; body § 8 assigns on VERIFIED capabilities; all six are UNVERIFIED |
| B-4 | The third position's existence and function (U-6) | § 6.2 |
| B-5 | `scientist-c` ACTOR_ID confirmation (U-5) | PID-12 — confirmed at its own registration |
| B-6 | **Scientific priority — which studies, in what order** | H.1: *strategia complessiva → Operatore*. Orchestrator orders **within** an authorized scope; it does not set the scope |

**Requires GOVERNANCE CLARIFICATION:**

| # | Blocked | Why |
|---|---|---|
| B-7 | A binding protocol whose addressee set is defined by a non-binding contract (U-2 part 2) | nobody has adjudicated the coupling |
| B-8 | Promotion of `PARALLEL_READ_GROUP` into Annex A | it is an extension field standing on A.1's *extendible, never removable* clause; promotion is a separate governed change |
| B-9 | `MIRROR_RETROSPECTIVE` cadence `N` | `ESC-3` — the annexes assign `N` to nobody; Plan declined it (G.2 puts retrospective methodology inside Mirror's method), Mirror declined for the same reason |
| B-10 | Where the Agent Card registry lives | the open C-9 § 7.2 question |

**Requires IMPLEMENTATION:**

| # | Blocked | What is missing |
|---|---|---|
| B-11 | `scientist-a` / `scientist-b` registration (U-3) | `ledger/registrations/` empty on every ref (N-2); **and both worktrees carry no `roles/` at all** (N-7), so neither can read its own contract without syncing 201/203 commits |
| B-12 | The benchmark input surfaces | not built (N-5); `deployment/local_instance.md`, which carries `BENCH_ROOT`, does not exist (N-4) |
| B-13 | Freezing `benchmark_manifest.json` | `_state: PREPARED — NOT FROZEN`; `FROZEN_SHA256: null`; `HANDOVER` all `null` |
| B-14 | Two Task Contracts | none exists on any ref (N-1); and issuing one needs an ACTIVE lease (U-7) — `0` today |
| B-15 | The event ledger's writer | Mirror's stated primary analysis surface (G.3) has no writer; `roles/mirror.md` records the capability as blocked |
| B-16 | A carrier for "remaining workload" | no Annex B message type and no Annex A field carries it; nearest are `STATUS_UPDATE`, `HEARTBEAT`, and Plan's reconciliation. Creating one is a schema change and is **not done here** |

### 8.3 · The honest accounting

Of the sixteen blockers, **eleven (B-1…B-5, B-7…B-8, B-10…B-13, minus recurrences) are one-time
unblocking acts**, not per-batch costs. B-6 (scientific priority) recurs per batch, as does
H.1's MAJOR-approval and spend gate, R3 TRIADIC on persistent disagreement, and the human read of
`git diff origin/main..main --stat` before any public push — *the one judgement no gate makes*.

**Nothing in the NOT_READY column is unblocked by more analysis.** Iterations 2 and 3 of this task
cannot move any of it; only the named owners can.

---

## 9 · SECTION 6 — Proposed first experiment: structure only

> **No paper is selected. No actor is assigned. No partition is proposed. Nothing here is
> implemented, scheduled or requested.** This is the *shape* of a first experiment, and the
> repository already contains most of it: `BENCH-AB-001`. What follows says which dimensions a
> first experiment must fix and where each is already fixed.

### 9.1 · The structure

```
SCALE          ONE paper. Body §41: PICCOLO — 1–2 PMID each for a first cycle; full throughput
               only from the second batch. BENCH-AB-001 fixes one.
               🔴 One paper cannot separate mode from session variance, and the protocol says so
               in its own §0. The output is MATERIAL AND FAILURE MODES, NOT A NUMBER.

ARMS           TWO. MODE A · PRIMARY_EVIDENCE_READ  and  MODE B · INDEPENDENT_CRITICAL_READ,
               one actor each, both carrying PARALLEL_READ_GROUP: BENCH-AB-001.
               A THIRD ARM IS NOT PROPOSED — §6.3 U-6 is unresolved, and the benchmark protocol
               §10 lists "run a Scientist C arm" among what it does not do.

VARIABLE       exactly ONE: which mode directive is addressed to you.
               Two per-actor files differ — ASSIGNMENT.md and benchmark/MODE_DIRECTIVE.md.
               A THIRD differing file is a broken benchmark and `verify` reports it.

DENOMINATOR    fixed BEFORE anyone reads: 65 structural evidence units, 109 panels.
               Its digest is in the manifest, so it cannot be redefined once readings exist.
               It says what the paper CONTAINS, never what it SHOWS — which unit matters is
               exactly what the readings will disagree about and must not be pre-empted.
```

### 9.2 · The A/B independence test — five checks, in order

```
1  verify                pre-handover. Parity across surfaces; every forbidden prior-output path
                         absent with NO exemption; nothing outside the allowlist; slots empty;
                         content scan = 0 hits; [UNCHECKED] census printed per actor.
                         PASS is precondition P-7 and is what authorizes handover.
2  HANDOVER              writer transfer recorded; memory-scope absence checked and recorded.
3  FREEZE                on the completion declaration and BEFORE Plan reads the content.
                         The order matters: a freeze taken after reading is a freeze whose
                         timing cannot be shown.
4  verify --post-read    same checks with declared outputs excluded; the blind spot printed
                         BY NAME; EXPECTED_BY_PROTOCOL: NO informational here, blocking at step 1.
5  verify-freeze         set-wise recomputation — ADDED · REMOVED · MODIFIED, each enumerated,
                         never by count — plus an identity check against the tree's own
                         ASSIGNMENT.md, so a receipt pointed at the wrong actor's tree fails on
                         identity and not merely on digests.
```

**The independence claim this yields, stated so it can be falsified:** *`SCANNED` and
`[UNCHECKED]` partition the present files — no present file is skipped by the identifier scan
without being printed by name, and no file is printed that was scanned.* Falsify it with a file
that `verify`, **in either mode**, neither scans nor names.

**What it does not yield, and must not be described as yielding:** authorship of bytes at the
blind-spot path; proof that a reader did not open a file by absolute path and quote nothing from
it; and any mechanical guarantee that B was not shown A's first pass before B's freeze — that one
is `PROCEDURAL`, detectable after the fact from `FREEZE_TIMESTAMP_UTC` against `SURFACE_COMMIT`,
never prevented.

### 9.3 · The C synthesis test — NOT PROPOSED, and why that is the finding

A C arm cannot be designed here without first deciding U-6, and deciding U-6 is an operator act
(§ 6.3). What *can* be recorded is the shape the two readings of U-6 would each take, so the
decision is made against concrete alternatives rather than in the abstract:

| Reading | Arm shape | What it would test | What it collides with |
|---|---|---|---|
| (i) **third reading** | a third blind first pass in the same surface, mode assigned by task | whether a third independent read adds units, or converges | nothing — § 32-compatible; but it needs a third surface and a third freeze |
| (ii) **synthesis / adjudication** over two frozen passes | a post-freeze arm reading both | whether a third actor can resolve A↔B divergence | body § 27 (forced synthesis is an error), H.1 (challenge adjudication is Orchestrator's), C.3 (review opening is Orchestrator's) |

**Recommendation withheld.** § 6.2 records why: an actor choosing the reading that gives it a role
is the interpretation the gate exists to prevent.

### 9.4 · Mirror evaluation criteria for the first experiment

Mirror's arm is **step 8** of the existing sequence: *adjudication of the process (R4)*, output to
`reviews/mirror/BENCH-AB-001-ADJUDICATION.md` on branch `mirror`, with a pointer + digest under
`adjudication/` — never a copy that could drift.

Its criteria are already enumerated and need no new rubric — which matters, because **Mirror may
not self-approve a rubric change** (G.2):

```
ADJUDICATED (Mirror)      EPISTEMIC DISCIPLINE (substance) · CONTEXT PRESERVATION (instances) ·
                          METHODS / LIMITATIONS (substance) · CONTRADICTION / NEGATIVE EVIDENCE
                          (substance) · FAILURE MODES (instances per the 12 gates, with locator) ·
                          CLAIM PRECISION (the `Type` question)
MECHANICAL (Plan)         EVIDENCE COVERAGE · PROVENANCE · LOCATOR FIDELITY · presence checks
BLIND AGENTS              CLAIM PRECISION per triple · LOCATOR FIDELITY
DEFERRED, NOT JUDGED      MECHANISTIC VALUE → Annex C review opened by Orchestrator, OUTSIDE the
                          benchmark record
SECONDARY, REPORTED APART TIME · TOKEN/CONTEXT (or "NOT OBSERVABLE" — never estimated) ·
                          OUTPUT VOLUME. Not combined with anything; they do not break ties.
```

**Reporting rules, verbatim in substance:** no overall score, no weighting, each dimension its own
table with the route that produced each number, every count an enumerated set or accompanied by
its command. Agreement between A and B is **descriptive, not a quality measure** — *two readers
agreeing on an overshoot is two overshoots.*

### 9.5 · What a first experiment must produce even when it "fails"

A reading declared complete **without `verbatim_locators.entries[]` is not complete**, and the
freeze does not repair it: *the freeze records what was in the tree, it does not confer the depth
that was not*. Such a reading scores `EVIDENCE COVERAGE` and `PROVENANCE` on an empty locator set,
and the blind audit has **no triple to audit** — which is the measurable form of the same
statement, and the reason it is a precondition rather than an outcome.

---

## OPEN_QUESTIONS

## 10 · Recorded, not resolved — each with its disposition owner

| # | Question | Owner |
|---|---|---|
| **Q-A** | Do `scientist_reading_modes.md` and `controlled_benchmark_ab.md` bind, given that all three of their activation clauses measure SATISFIED while their status lines have never been modified and no object records the satisfaction? (U-2) | operator (H.1) |
| **Q-B** | Does a binding protocol whose `applies_to` set is defined by a **non-binding** contract have an addressee set at all? (U-2 part 2) | operator (H.1) |
| **Q-C** | Does a third position exist in a reading cycle, and if so is it (i) a third reading or (ii) synthesis/adjudication? Reading (ii) collides with body § 27, H.1 and C.3 as measured in § 6.2. (U-6) | operator |
| **Q-D** | Registration order for A and B: their worktrees carry no `roles/` and are 201/203 commits behind. Does registration require the sync first, or is the surface handed to an unsynced worktree? § 4.4 | operator / registrar |
| **Q-E** | `BENCH_ROOT` has no carrier — `deployment/local_instance.md` does not exist (N-4). Which object declares it? | Plan (implementation) / operator |
| **Q-F** | "Remaining workload" has no carrier in Annex A or B (B-16). Creating one is a schema change. | Plan (schema) / operator |
| **Q-G** | Mirror's stated primary analysis surface (G.3, the J.1 event ledger) has no writer, and `roles/mirror.md` records the capability as blocked. | operator / Plan |
| **Q-H** | `roles/mirror.md` received **no verdict** in the only hostile review of the four contracts, under the self-review prohibition. The contract governing the evaluator is the one no review can reach. | operator (H.1) |

---

## VALIDATION

## 11 · Constraint compliance — checked, not asserted

| Constraint from the dispatch | Result |
|---|---|
| `MUST NOT` modify `governance/` | ✅ untouched — verified by `git status` |
| `MUST NOT` modify `roles/` | ✅ untouched |
| `MUST NOT` modify `framework/` | ✅ untouched |
| `MUST NOT` modify `ledger/` | ✅ untouched |
| `MUST NOT` assign Scientist actors | ✅ no actor named against any source; no `Agent` or `SendMessage` call made |
| `MUST NOT` start literature analysis | ✅ no full text opened, no paper read, no receipt written, zero claims |
| `MUST NOT` activate contracts | ✅ § 4.2 and § 4.3 record the state; nothing acts on it |
| `MUST NOT` create decisions | ✅ nothing under `governance/decisions/`; every question in § 10 carries an owner who is not this session |
| `MAY` create one learning artifact | ✅ **exactly one file added**, this one |
| identity from repository evidence only | ✅ § 1; no authority read from `roles/plan.md` |
| authority not assumed from a `PROPOSED` contract | ✅ § 1.1; every rule cited from body or annex |
| every named concept validated | ✅ § 3 — 3 marked EXTERNAL or PARTIAL, none silently adopted |
| no governance vocabulary silently created | ✅ "study allocation", "contamination", "evidence extraction" are used as the dispatch's words with the repository's objects named beside them |
| negative claims carry MEASURED_AT + VALIDITY | ✅ § 2.5, seven claims |
| `NOT_FOUND` not converted to `NOT_EXIST` | ✅ § 2.4 — seven objects located on other refs and read there |

### 11.1 · Domain and collision disclosure

- **Content domain.** `learning/` is not among P5.1's exhaustive `CONTROL_PLANE_ROOTS`. This file
  therefore sits **inside** the `CANDIDATE_CONTENT_HASH` of any future candidate including this
  branch, and moves it. Disclosed, not discovered later.
- **Seat.** `learning/plan/` on this ref holds 22 files: 21 `SLR-plan-*` and one `HANDOFF-*`. This
  record takes a **non-`SLR`** name so it is not mistaken for a Session Learning Record under
  Annex E.6, following the precedent that `HANDOFF-20260822-ROLE-CONTRACT-REPAIR.md` set with its
  own `naming_note`.
- **No base condition invalidated.** No open candidate declares `de0ae4e` as its `BASE_HEAD`; the
  SCIAB candidate's is `cbce3016`, long behind.
- **Cross-branch reads were reads.** `main` and `mirror` and `orchestrator` were read via
  `git show <ref>:<path>`. Nothing was merged, checked out, or written outside this worktree.

### 11.2 · What this record does NOT do

It does **not** activate any role contract or perform the act `DEC-20260822` consequence 3
requires · does **not** claim or imply Orchestrator authority · does **not** assign a paper, an
actor, a batch or a review · does **not** resolve Q-A…Q-H · does **not** create a Task Contract,
a `PARALLEL_READ_GROUP`, a Mirror task or a ledger event · does **not** verify a capability or
lift the C-9 hold · does **not** select or design a Scientist C arm · is **not** an
`AUTHOR_RESPONSE` to anything · is **not** a `CANONICAL_BATCH_COMMIT`.

---

## NEXT_TRANSITION

```
FROM   iteration 1/3 — readiness analysed, boundaries defined, one artifact created

TO     nothing this session can enter.

WHY    Every item in NOT_READY (§8.2) is owned by the operator, by governance clarification, or
       by an implementation act that requires one of the first two to precede it. Analysis
       iterations 2 and 3 cannot move any of them.

THE ONE ORDERING FACT WORTH CARRYING FORWARD:
       B-1 and B-2 gate everything downstream. Registration (B-11) reads a contract; the Task
       Contract (B-14) names an OWNER whose identity a protocol fixes; the surfaces (B-12) are
       built to a protocol's allowlist. If the contracts and protocols do not bind, each of those
       acts rests on a document that says it binds nobody — which is the defect
       REV-ROLES-MIRROR-001 MAJOR-3 recorded and the AUTHOR_RESPONSE accepted as
       ACCEPTED · CHARACTER CHANGED · UNREPAIRED · OPEN.

       Building the surfaces first would not be wasted work — build/verify are deterministic
       functions of an allowlist and could be re-run — but it would produce a handover gate whose
       PASS certifies a protocol nobody has said is in force.

WHAT THIS SESSION HANDS OVER:
       this record. No recipient is named — routing is unresolved repository-wide
       (SESSION_ROUTING_DEBT, APR-20260819-XPORT-001) and no destination is invented here.
```

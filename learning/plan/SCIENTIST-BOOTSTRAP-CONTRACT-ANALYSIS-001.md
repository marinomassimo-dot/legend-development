---
artifact: BOOTSTRAP CONTRACT ANALYSIS — what a Scientist must receive, produce and hand off
record_id: SCIENTIST-BOOTSTRAP-CONTRACT-ANALYSIS-001
task_id: SCIENTIST_BOOTSTRAP_CONTRACT_ANALYSIS_v1
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
  - NOT AN AGENT DEFINITION

naming_note: >
  Neither a Session Learning Record (Annex E.6) nor a handoff. Named descriptively, and takes no
  `SLR` number it has not earned — the precedent of the three non-SLR records already in this seat.

domain: >
  CONTENT. `learning/` is not among the exhaustive `CONTROL_PLANE_ROOTS` of
  `governance/plan_defined_parameters.md` § P5.1. This file is therefore inside the
  `CANDIDATE_CONTENT_HASH` of any future candidate including this branch, and moves it. Disclosed.

relation_to_prior_work: >
  Three records on this branch touch adjacent ground: `SCIENTIST-PIPELINE-READINESS-001`
  (readiness), `SCIENTIST-PIPELINE-EXECUTION-MODEL-001` (execution), and — on `main`, not here —
  `learning/orchestrator/SCIENTIFIC-PIPELINE-PREPARATION-001`. This record answers a third
  question: what the CONTRACT of a single Scientist is, at its boundaries. It does not restate
  the other three; where it depends on a fact one of them established, that fact was re-measured
  here first. The principal new evidence is the input contract itself, which exists in
  materialized form and is read here rather than reconstructed.

verdict_transfer: >
  NONE. Every mechanical fact below was executed in this session at the HEAD named in § 1.
---

# SCIENTIST BOOTSTRAP CONTRACT — 001

> **The finding that shapes this record.** The Scientist input contract is not a gap to be
> designed. It **exists, materialized, at one instance** — `framework/eval/benchmarks/BENCH-AB-001/instructions/`,
> seven files, 592 lines, canonical on `main` since `4454fea`. This analysis reads it rather than
> inventing a parallel one, and reports where the dispatch's six input items land in it: **four
> are specified, one is specified twice with opposite answers, and one does not exist — because
> the design affirmatively excludes it.**

---

## TASK_STATUS

```
TASK_ID          SCIENTIST_BOOTSTRAP_CONTRACT_ANALYSIS_v1
MODE             ANALYSIS ONLY · no actor creation · no role activation · no contract binding
STATE            COMPLETE — the six study areas are answered from measurement; every answer that
                 could not be measured is an open question with an owner who is not this session

EXECUTED         reads across 7 refs; the seven materialized instruction files read in full;
                 4 executable checks re-run (lease derivation, git ancestry, JSON parses,
                 per-file paper-reference counts)
NOT EXECUTED     no Scientist agent created, spawned, contacted or assigned · no paper opened ·
                 no literature read · no scientific conclusion formed · no contract activated or
                 bound · no path under governance/ roles/ framework/ ledger/ modified ·
                 no schema, field or vocabulary created
FILES ADDED      exactly one — this file
```

---

## IDENTITY

### 1 · From repository evidence; not from `roles/plan.md`, which is not binding

| Field | Measured value | Command |
|---|---|---|
| branch | `plan-orchsurf-r4-transcription` | `git rev-parse --abbrev-ref HEAD` |
| HEAD | `a10a11aeb5f4519e092258205be4f445f56ca066` | `git rev-parse HEAD` |
| worktree | `.claude/worktrees/evidence-index` | `git rev-parse --show-toplevel` |
| working tree | **clean** at session start | `git status --porcelain` → empty |
| worktree ↔ actor | profile maps `plan` → `evidence-index`; this session stands in it — **and the profile's own caveat holds: neither column is an ACTOR_ID oracle nor a write-authority oracle** | `deployment/deployment_profile.md` |
| lease | **`ACTIVE by derivation: 0`** | `python3 framework/scripts/lease_state.py` |

**`CLAUDE.md` § 0: no ACTIVE lease and no runtime inventory ⇒ `BOOTSTRAP_MODE`.** This session is
not Orchestrator, issues nothing, and creates no actor. The one act it performs — writing a file
under `learning/plan/` on its own branch — traces to H.1's `WORK_COMMIT` row, an annex, not a role
contract.

**And the governing determination is unchanged since it was read last session:**
`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` (on `main`, **not on this ref**) selected
`OPTION B — ACTIVATION_NOT_CONFIRMED`. The four role contracts remain `PROPOSED` and non-binding;
*"no actor authority may be assumed from these contracts."* Every statement below about
`roles/scientist.md` is made under that determination.

---

## SURFACE_MAP

### 2 · The materialized input contract — measured, file by file

`framework/eval/benchmarks/BENCH-AB-001/instructions/` — canonical on `main`
(`git merge-base --is-ancestor 4454fea main` → yes), and present here.

| File | Lines | Paper references | Role |
|---|---|---|---|
| `SURFACE_CLAUDE.md` | 43 | **0** | the surface router — read-order, the discipline set, the two prohibitions |
| `MODE_A.md` | 74 | **0** | `PRIMARY_EVIDENCE_READ` directive |
| `MODE_B.md` | 83 | **0** | `INDEPENDENT_CRITICAL_READ` directive — the 11 mandatory axes |
| `ASSIGNMENT.scientist-a.md` | 36 | 1 | identity · task · mode · group · interaction mode · source |
| `ASSIGNMENT.scientist-b.md` | 37 | 1 | the same, for the other reader |
| `BENCHMARK_INSTRUCTIONS.md` | 127 | 7 | the common contract — packet, binding discipline, depth rule, outputs, completion gate |
| `OUTPUT_SCHEMA.md` | 192 | 6 | the four output shapes, the 20 labels, the receipt |
| | **592** | | |

`paper references` counted as `grep -ciE "42397075|awag239|Aqeilan"` per file.

🔴 **This is the measurement that answers "what is the minimum *reusable* scientist workflow".**
**200 of 592 lines — the two mode directives and the surface router — carry no reference to any
paper at all.** They are the reusable core, verbatim, across any source. The remaining 392 lines
are paper-bound by construction: the packet listing, the validator invocation with its `--pmid`,
and the four output paths that `deepdive_manifest.py` derives from disease and PMID.

Reusability therefore splits cleanly and is not a matter of effort:

```
REUSABLE VERBATIM       MODE_A.md · MODE_B.md · SURFACE_CLAUDE.md            200 lines · 0 edits
REUSABLE BY TEMPLATE    BENCHMARK_INSTRUCTIONS.md · OUTPUT_SCHEMA.md         319 lines · PMID,
                        packet list and output paths substituted
PER-READING             ASSIGNMENT.<actor>.md                                 ~36 lines each
PER-PAPER, DERIVED      surface_spec.json — forbidden_prior_output_paths (23, derived by git grep
                        for THAT PMID), source_files (7), population (65 units / 109 panels)
```

### 2.1 · Negative claims — each with what was run and how long it holds

| # | Claim | Command | MEASURED_AT | VALIDITY |
|---|---|---|---|---|
| N-1 | **No concept of a per-reading *research question* or *evidence target* exists anywhere in `governance/`, `framework/` or `roles/`** | `git grep -iE "research question\|evidence target\|RESEARCH_QUESTION"` → **0 hits** | 2026-08-22, HEAD `a10a11a` | until an object introduces one |
| N-2 | **`missing evidence` has no per-claim label.** `EVIDENCE_NEEDED` exists in exactly two normative files and is a field of a **review**, not of a claim | `git grep -iE "EVIDENCE_NEEDED\|missing evidence"` → body § 25, Annex C.2, and two candidate mentions | same | until a governed change adds one |
| N-3 | **J.1 names 23 minimum event types, and none of them is a freeze, a read, or an analysis** | enumerated from `annex_j_runtime_control_plane.md` § J.1 | same | until J.1 is amended |
| N-4 | **The event ledger has no writer on any ref**; `roles/mirror.md` records the matching capability as *blocked* | § J.1 names the design choice (a) or (b); no implementation exists | same | until a writer is built |
| N-5 | **`ledger/registrations/` does not exist on any of the 7 refs read** — no Scientist has a registration record anywhere | `git ls-tree -r <ref> -- ledger/registrations` → 0 on HEAD, main, orchestrator, mirror, lettore, lettore-b, lettore-c | same | until a registration is written |
| N-6 | **No Task Contract exists for any Scientist.** `ledger/tasks/` holds one directory, `plan/`, with 5 records | `find ledger -type f` | same | until Orchestrator issues one under an ACTIVE lease |

---

## SCIENTIST_MODEL

### 3 · The input contract — three carriers, and the six dispatch items placed on them

**The input does not arrive on one channel.** Measured, it arrives on three, and each has a
different author, a different lifetime and a different failure mode:

```
CARRIER 1   TASK CONTRACT (Annex A.1)        author: Orchestrator, under an ACTIVE lease
            TASK_ID · DIRECTIVE_VERSION · GENERATION · OWNER · PRIORITY · OBJECTIVE · SCOPE ·
            ACCEPTANCE_CRITERIA · DEPENDENCIES · REVIEW_REQUIREMENT · INTERACTION_MODE ·
            RETRY_POLICY · MILESTONE_PLAN · DELIVERABLE · CURRENT_STATE
            + PARALLEL_READ_GROUP — an EXTENSION field, standing on A.1's
              "extendible, never removable" clause; promotion into Annex A is a separate
              governed change and has not happened

CARRIER 2   THE SURFACE (surface_spec.json → ALLOWED_PATHS)   author: Plan, at build
            what the reader can physically reach. Not a list the reader is told; a directory
            whose entire content is enumerated and digested, so blindness is a property of the
            surface rather than a promise the reader makes

CARRIER 3   THE INSTRUCTION SET (4 files, read in a fixed order)   author: Plan, per protocol
            ASSIGNMENT.md → BENCHMARK_INSTRUCTIONS.md → MODE_DIRECTIVE.md → OUTPUT_SCHEMA.md
```

### 3.1 · The six items the dispatch names, measured

| # | Dispatch input | Status | Where it lives, measured |
|---|---|---|---|
| **1** | **paper** | ✅ **SPECIFIED** | Carrier 2: a 7-file packet — article PDF, extracted text surface, 5 supplement assets — every digest recorded in the manifest and verified equal in both surfaces before handover. Carrier 3 names it once, in `ASSIGNMENT`'s `SOURCE` line. **The text surface's identity is its digest, not a recipe:** its declared extraction command does not regenerate it byte-for-byte, so quotes resolve against the file the reader holds |
| **2** | **question** | 🔴 **DOES NOT EXIST — and § 3.2 argues it should not** | N-1: zero occurrences. A.1 carries `OBJECTIVE / SCOPE / ACCEPTANCE_CRITERIA`, which are **task-level and verifiable**, not a scientific question. What stands in its place is the **MODE**, and a mode is a way of reading, not a thing to find out |
| **3** | **evidence target** | 🔴 **DOES NOT EXIST — and is affirmatively excluded** | § 3.2 |
| **4** | **allowed sources** | ✅ **the most heavily specified input of the six** | `ALLOWED_PATHS`; parity across surfaces; `forbidden_prior_output_paths` (23, derived by `git grep` for that PMID); a content scan for the paper's own identifiers expecting **0** hits in everything that is not the paper; and the `SCANNED` / `[UNCHECKED]` **partition** — every present file either scanned with no hit or printed by name with its class and reason |
| **5** | **previous context** | ⚠️ **SPECIFIED TWICE, WITH OPPOSITE ANSWERS** | § 3.3 — and the split is not a contradiction |
| **6** | **constraints** | ✅ **SPECIFIED, in three places, and one of them is unusual** | A.1: `INTERACTION_MODE` (`AUTONOMOUS_COMPLETE` — *do not ask questions to proceed*), `RETRY_POLICY`, `REVIEW_REQUIREMENT`, `MILESTONE_PLAN`. Carrier 3: the prohibition lists. And the **budget rule**, § 3.4 |

### 3.2 · 🔴 Why "question" and "evidence target" are absent — the design excludes them

This is not an omission. Three measured rules put a target-driven reading in direct conflict with
the model the repository already built:

```
1  THE DENOMINATOR IS FIXED BEFORE ANYONE READS, AND IT IS DELIBERATELY UNRANKED
   population/evidence_units.json — 65 units, 109 panels, enumerated by command.
   "It says what the paper CONTAINS, never what it SHOWS — which unit matters is exactly what
    the readings will disagree about, and it must not be pre-empted."
   An evidence target IS a pre-emption of exactly that.

2  COMPLETENESS, NOT SELECTION, IS THE COMPLETION CRITERION
   A reading is complete only when the coverage map contains NO `not_read`, over all nine
   sections. There is no shape of "complete" that is scoped to a target.

3  GREP IS NOT A METHOD OF ANALYSIS
   "It finds a place to read, never a substitute for reading." A question supplied up front is
   the instruction to read toward it — which is the failure the rule names, moved earlier in
   the pipeline where no validator looks.
```

And the taxonomy already names the resulting failure and treats it as the compounding one:
`READING_DEBT_FALSE_NEGATIVE` — *"Ranking orders reading; it never authorizes not reading. If
ranking discards a study, the ranking is broken."* The keystone of `failure_taxonomy.md` is the
**permanent false negative** — *a correct lead discarded on an unexamined premise and never
revisited* — which is why every rejection must record a `REVIVAL_TRIGGER`.

**What this does NOT say.** It does not say questions have no place in LEGEND. It says the place
is **not the reading's input**. Prioritisation across papers is `HUMAN_REQUIRED` (H.1: *strategia
complessiva → Operatore*); ordering within a scope is Orchestrator's; and a targeted interrogation
of an already-read corpus is a different instrument with its own read-only discipline. **A
question narrows what is read; the pipeline is built so that nothing narrows that.** Recorded as
**Q-1**, owner operator, because changing it is a design decision, not an analysis result.

### 3.3 · 🔴 "Previous context" — the split, stated precisely

The two answers are not in tension once the object of the context is named:

| Context about… | Answer | Rule |
|---|---|---|
| **the ASSIGNMENT** — task, generation, directive version, prior claims on this source | ✅ **MANDATORY, and mandatory *before* claiming** | A.4 anti-zombie: a rehydrated actor MUST verify generation, directive version **and checkpoint compatibility** before resuming. A.7: before redoing a step, check whether the milestone's evidence already exists. `reading_modes` § 2.2 r3: **query the receipt ledger and the task ledger for the source** — an existing reading or open contract without a shared `PARALLEL_READ_GROUP` → **do not claim**, raise `BLOCKER` naming both records |
| **the CONTENT** — what LEGEND already concluded about this paper | 🔴 **FORBIDDEN in a blind first pass** | contamination class 2: *reading the other reader's output, **or any prior LEGEND output on the paper***. Measured scale: **21 tracked files name the benchmark's PMID** at `BASE_HEAD`, which is why the reading happens in a standalone surface and not in a LEGEND checkout |

```
THE RULE, STATED ONCE:   context about the assignment is mandatory;
                         context about the content is forbidden.
```

**Outside a blind first pass the second row inverts** — an ordinary reading is expected to
reconcile against the canonical state, and `EXTERNAL_DOSSIER_CANONICAL_DRIFT_GATE` exists to
require it. Which route applies is a property of the Task Contract, not of the actor, and a
pipeline that does not know which route it is on will get this exactly backwards.

### 3.4 · The one constraint that constrains the constrainer

```
BENCHMARK_INSTRUCTIONS.md § 3
  "Do not compress depth or coverage for token, time or cost. A reading shortened for budget
   produces a receipt that overstates itself, and the receipt is what the rest of the system
   trusts."
  If you genuinely cannot complete at full depth, STOP and report the partial state with a
  coverage map naming exactly what is unread. "A declared partial reading is a legitimate,
  useful result. A silently thinned complete reading is a false record, and it is the more
  expensive of the two by a wide margin."
```

`budget contamination` is one of the six named contamination classes. **This is the repository
prohibiting the constraint a runtime most naturally imposes**, and it is the reason `partial` is a
first-class value of `evidence_depth` in the receipt rather than a failure state.

### 3.5 · The output model — the dispatch's six separations, measured

The output is **four artifacts on three surfaces, and a standing prohibition on a fifth**:

```
work manifest      schema_version 2, verbatim_locators.entries[] — the reasoning trace
dossier            artifact table with SHA-256; verbatim quotes with surface and anchor
claim candidates   12 canonical fields + 7 benchmark fields + `Locators:` = 20 labels
receipt.json       coverage map · validator verdict · self-check · blockers · contamination
critical_reading   MODE B only — one entry per finding, on 11 mandatory axes
FORBIDDEN          no claims.json, no claim_schema.yaml, no parallel Type enum, no second
                   locator format. "A reader who finds one of these has found a protocol
                   violation."
```

| # | Dispatch separation | Status | Measured home |
|---|---|---|---|
| **1** | **Observation** | ✅ EXISTS as its own label | `**Observation:**` — *what was measured, in what system, with what result. **No verb of conclusion.*** |
| **2** | **Interpretation** | ✅ EXISTS — **and is split in two, which is the more important separation** | `**Author interpretation:**` (theirs, marked as theirs) and `**LEGEND interpretation:**` (the reader's, typed). *"The one thing a second reader must be able to attack is the seam between what was observed and what was concluded, and today that seam is inside a paragraph."* |
| **3** | **Hypothesis** | ⚠️ **NOT a separate field — a VALUE of `Type`** | `Type ∈ DATO · INFERENZA · IPOTESI · ESPANSIONE`, compound allowed. `IPOTESI` is where a hypothesis lives, and `MODE_A` states the consequence: *mechanistic implications typed `INFERENZA` or `IPOTESI`, **never `DATO`***. 🔴 Making Hypothesis a fourth field beside Observation and Interpretation would put the epistemic level in two places at once — the failure `no hypothesis promoted to observation, ever` exists to prevent |
| **4** | **Uncertainty** | ⚠️ EXISTS as a **BENCHMARK/INTERMEDIATE** field — `0/39` as a label in the canonical registry | `**Uncertainty:**` — what is not settled, and by what |
| **5** | **Missing evidence** | 🔴 **NO PER-CLAIM HOME** (N-2) | Carried in three places, none of them a claim field: `EVIDENCE_NEEDED` (a **review** field, C.2); MODE B's `**What would resolve it:**` (a **critical-record entry** field); and § 3.6's *"unresolved ambiguities listed rather than absent"* (a **completion criterion**, not a label). **The concept is present three times and addressed to three different objects** |
| **6** | **Contradictions** | ⚠️ EXISTS as a **BENCHMARK/INTERMEDIATE** field, `0/39` canonical — **and one distinction must not be collapsed** | `**Contradictory evidence:**` is *inside this paper*, or *"none found — searched: `<what>`"*. `Status: conflicting evidence` is **cross-paper lifecycle**, measured `1/39`. They are different objects and a schema that merges them loses the intra-paper signal MODE B exists to find |

**The load-bearing rule about all six:** an axis or a field answered by **silence** is incompleteness,
not a null result. MODE B: *"An axis with none carries **searched; none found** and says what was
searched — concretely, not 'the paper'. **Silence on an axis is an incomplete reading, not a clean
paper.**"*

### 3.6 · The lifecycle — six dispatch stages against nine measured states

| Dispatch stage | Annex A.5 state(s) | Owner | J.1 event | Schema | Gap |
|---|---|---|---|---|---|
| **START** | `ASSIGNED` → `ACKED` → `CLAIMED` — **three states, two owners** | Orchestrator assigns; the **actor** ACKs and claims | `TASK_ASSIGNED` · `TASK_ACKED` · `TASK_CLAIMED` | A.1 · A.2 · A.3 | 🔴 **no writer for any event** (N-4). *Assigned ≠ claimed*, and the measured failure class is `ACK emesso ma lavoro mai partito` (truncated turn, permission prompt) → `DIAGNOSE`, **never classified as refusal** |
| **READ** | inside `IN_PROGRESS` | the actor | **none exists** (N-3) | — | § 3.7 |
| **ANALYZE** | inside `IN_PROGRESS` — **no state boundary separates it from READ** | the actor | **none exists** | — | § 3.7 |
| **COMPLETE** | `COMPLETE` (terminal) — siblings `CANCELLED · REASSIGNED(gen+1) · PARKED` | the actor declares; the gate is mechanical | `TASK_COMPLETE` | completion criteria, `reading_modes` § 3.6 | precondition is `VERDICT: PASS` on `deepdive_manifest.py --verify-artifacts --require-current-schema`, *"a precondition of completion, not a nicety"* |
| **HANDOFF** | not a task state | the actor sends; **the recipient differs by route** | — | Annex B.1 envelope | 🔴 **name collision**, § 3.8 |
| **REVIEW** | not a task state | 🔴 **opened only via Orchestrator** (C.3) — the actor cannot hand off into review directly | `REVIEW_OPENED` · `REVIEW_CLOSED` | C.2 single format | rotation; never fixed pairs; `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR`; max 2 rounds; **cap one active review per Scientist** |

Intermediate states the dispatch's six boxes do not carry, and each exists for a measured reason:
`BLOCKED` and `AWAITING_APPROVAL` (≈ A2A *input-required*) — *the task parks at the exact point
with a checkpoint (A.6) and resumes without redoing work (A.7)*.

### 3.7 · 🔴 READ and ANALYZE are not separable by any instrument the repository has

There is no state between them, no event distinguishing them, and no artifact that belongs to one
and not the other. The **only** durable boundary inside `IN_PROGRESS` is the milestone:

> **A.7** — *Il confine di idempotenza è la **MILESTONE DUREVOLE SIGNIFICATIVA** (definita nel
> `MILESTONE_PLAN`), NON ogni operazione mutante.*

And `MILESTONE_PLAN` is a field of the **Task Contract**, written by **Orchestrator**. So:

```
WHETHER READING AND ANALYSIS ARE SEPARABLE STAGES AT ALL IS DECIDED PER TASK,
BY SOMEONE OTHER THAN THE READER, IN A FIELD WRITTEN BEFORE THE READING STARTS.
```

That is a real design property and it is defensible — A.7 states the calibration cost in both
directions (*milestone troppo grosse → più lavoro rifatto; troppo fini → commit noise*), and gives
Mirror the **redone-work ratio** as the instrument for tuning it. But it means a pipeline diagram
that draws READ and ANALYZE as separate boxes is drawing something the governance does not track,
and the gap is invisible until a resume needs it.

### 3.8 · 🔴 `HANDOFF` and `HANDOVER` are two different objects with near-identical names

```
HANDOFF    an Annex B.2 MESSAGE TYPE, alongside TASK_COMPLETE and TASK_CANCEL
           measured: 1 occurrence in annex_b_message_protocol.md
HANDOVER   the BENCHMARK'S WRITER TRANSFER — step 3 of the sequence: Plan hands the surface to
           the actor, writer transfer recorded, memory-scope absence checked and recorded;
           a `HANDOVER` block in benchmark_manifest.json, all fields currently `null`
           measured: 10 occurrences in controlled_benchmark_ab.md, 1 in the manifest
```

One is a message; the other is a transfer of write authority over a directory. **Nothing in the
repository disambiguates them**, and the failure mode is silent: an implementer reading "handoff"
in a pipeline diagram may build the message and skip the writer transfer, whose absence no
validator detects, because `verify` runs *before* handover and `verify --post-read` runs *after*
the reading. Recorded as **Q-2**, owner Plan (vocabulary), and not resolved here — naming is a
governed change.

---

## CONTAMINATION_ANALYSIS

### 4 · The four requirements the dispatch names, each with instrument and limit

> Assembled only from enumerated rules. The umbrella words are the dispatch's; the contents are
> the repository's.

### 4.1 · FREEZE — and there are two of them

The prior record established this; it is re-measured and unchanged. **Two freezes, at opposite
ends, protecting different properties:**

| | INPUT FREEZE | OUTPUT FREEZE |
|---|---|---|
| When | before any reading, at build/handover | **on the completion declaration, before Plan reads the content** |
| Object | manifest `FROZEN_SHA256` + the population digest | the reader's output tree |
| Protects | the **denominator** — 65 units / 109 panels, so coverage cannot be redefined once readings exist | **immutability** — a correction after freeze is a new dated file under `post_freeze/`, never an edit |
| State today | 🔴 `_state: PREPARED — NOT FROZEN`; `HANDOVER` fields all `null` | never run |

The output freeze's receipt is `RECEIPT_SCHEMA_VERSION 2` and its ordering rule is explicit:
*a freeze taken after Plan has read the content is a freeze whose timing cannot be shown.*
`verify-freeze` recomputes **set-wise, never by count** — `ADDED · REMOVED · MODIFIED`, each
enumerated — plus an identity check against the tree's own `ASSIGNMENT.md`, so a receipt pointed
at the wrong actor's tree fails on identity and not merely on digests. *Two trees of equal file
count holding different files is exactly the substitution this exists to catch, and a count says
they agree.*

🔴 **No J.1 event type corresponds to either freeze** (N-3). The immutability anchor of the whole
design emits nothing into the ledger that Mirror is supposed to analyse from.

### 4.2 · BLIND SEPARATION — one variable, two files, and what makes it checkable

```
THE EXPERIMENT      exactly TWO files differ between the surfaces:
                    ASSIGNMENT.md  (identity, by necessity)
                    benchmark/MODE_DIRECTIVE.md  (the experimental variable)
                    A THIRD differing file is a broken benchmark and `verify` reports it.
```

Both directives state the same instruction to the reader in the same words: *"This file and
`ASSIGNMENT.md` are the only two files that differ between the two readers. Do not speculate about
what the other directive says; it is not your variable."*

🔴 **And the protocol declares the leak in its own design rather than arguing it away.** Each
reader can read `scientist_reading_modes.md` §§ 4–5, which describe *both* modes and are a common
file, normative for both and not honestly withholdable from either. **The manipulated variable is
therefore which directive is addressed to you, not knowledge that two modes exist.** The
instruction is about attention, not information.

A second declared limitation, also in the protocol's own § 0: with one paper and one session per
actor, **session variance is not separable from mode**. The output is *material and failure modes,
not a number.*

### 4.3 · CONTAMINATION PREVENTION — six classes, and what each instrument actually reaches

The six classes (shared context · seeing previous conclusions · relayed content · sequential
reading · inherited hypotheses · budget contamination) were enumerated in
`SCIENTIST-PIPELINE-EXECUTION-MODEL-001` § 4.3 from the same sources and are not restated. What
this record adds is the **coverage map of the instruments against them**:

| Class | Reached by | Limit |
|---|---|---|
| shared context | `verify` pre-handover — 23 forbidden prior-output paths absent, **none exempt**; content scan 0 hits | the *content* of `[UNCHECKED]` files |
| seeing previous conclusions | the surface allowlist itself; `verify --post-read` | 🔴 **an absolute path.** J.0: no runtime-enforced permissions. The default path is blind; the reader is not confined |
| relayed content | 🔴 **nothing mechanical** | *"a `BLOCKER` from a reader is answered on the protocol, never on the paper"* — a discipline on the answerer |
| sequential reading | 🔴 **nothing mechanical** — `PROCEDURAL`, § 4.4 | detectable after the fact from `FREEZE_TIMESTAMP_UTC` against `SURFACE_COMMIT` |
| inherited hypotheses | the typing requirement + blind locator audit over `(proposition, snippet, anchor)` triples | the audit needs triples; a reading with no locators has none to audit |
| budget contamination | 🔴 **nothing mechanical** | `evidence_depth: partial_fulltext_read` + an honest coverage map — a **self-declaration** |

🔴 **Three of the six classes are reachable only by the reader's own declaration**, and the
repository builds the channel for it and prices it:

```
output/receipt.json → "contamination_declared": []
  "Both are checkable after the fact only in part, and both are the point. If you break one by
   accident, SAY SO. A declared contamination is a usable result, and an undeclared one silently
   invalidates the experiment for everyone."
```

**This is the honest centre of the whole contamination model.** The mechanisms bound the window;
the declaration covers what no mechanism can see; and the declaration is worth having only because
the instructions make declaring cheaper than concealing. Nothing enforces that trade — it is
priced, not compelled.

### 4.4 · OUTPUT ISOLATION — and the one concentration this record names

Isolation of outputs is real: each reader writes only inside its own surface, on its own branch,
at milestone granularity; **nothing in the benchmark writes to any `*_current.md`, to the receipt
ledger, or to any registry**; the import into `first_pass/<ACTOR_ID>/` is byte-identical and the
receipt's digests are the check.

Two residual holes are stated where the claim is:

1. **The blind spot.** The reader's own manifest lands at exactly the path LEGEND's prior manifest
   occupies, because `deepdive_manifest.py` derives it from disease and PMID. *Authorship of bytes
   at that path is not decidable from the path.* `verify --post-read` **prints it by name on every
   run** — the set is computed and is size 1.
2. **`output/renders/` is exempt from the allowlist check and the identifier scan only when its
   bytes cannot be decoded as text** — the exemption exists for pixels. *"Anything decodable you
   put there is not a render."*

🔴 **And the concentration, re-measured and unchanged: the actor charged with detecting the one
unmechanized leak is the actor with the means to cause it.** The `PROCEDURAL` block names the
failure mode as *"Plan reads or relays A's first pass to B before B freezes"*, and Plan owns
sequence steps 1, 3, 5, 6 and 9 — build, handover, freeze, compare, outcome. Detection is
after-the-fact and indirect. This record does not propose a remedy: a change here is a governance
act. It records that **the same absent object — the J.1 event ledger's writer — is what would move
this from detection toward prevention, and is also what blocks Mirror's analysis surface and
Mirror's anti-fossilization guard. One object, three guarantees.**

---

## HANDOFF_MODEL

### 5 · Three recipients, and the dispatch's single arrow is only one of them

```
completion → PLAN            for FREEZE, before anyone reads the content        (benchmark route)
completion → ORCHESTRATOR    TASK_COMPLETE, for the next decision               (ordinary route)
after freeze → MIRROR        R4 adjudication of the PROCESS                     (both routes)
```

Which of the first two applies is a property of the Task Contract. **If completion goes to
Orchestrator first under a benchmark, the freeze happens after someone has read the content, and
its timing can no longer be shown.**

### 5.1 · What Mirror must RECEIVE

Mirror's step is 8 of 10: *adjudication of the process (R4)*, output to
`reviews/mirror/BENCH-AB-001-ADJUDICATION.md` on branch `mirror`, with a **pointer + digest** under
`adjudication/` — never a copy that could drift.

| Input | Why Mirror needs it | Source |
|---|---|---|
| **both frozen first passes, after both freezes** | its object is *how the laboratory reasoned*, which is not visible in one reading | benchmark § 7 ordering |
| **the freeze receipts** | `FREEZE_TIMESTAMP_UTC`, `SURFACE_COMMIT`, `FIRST_PASS_STATE`, `TREE_SHA256` — the only evidence that bounds the procedural window | receipt schema v2 |
| **the mechanical results** (Plan) | `EVIDENCE COVERAGE` · `PROVENANCE` · `LOCATOR FIDELITY` · presence checks — so Mirror adjudicates **substance** and does not re-run counts | § 8.2 route column |
| **the blind audit verdicts** | per triple: `SUPPORTED · OVERSHOOT · UNDERSHOOT · NOT_IN_SOURCE · UNVERIFIABLE_SURFACE` | § 8.2 |
| **the comparison matrix and the unresolved-disagreement list** | aligned structurally, by shared locator anchor, with disagreements **left unresolved** | § 8.3 |
| **the receipts' `contamination_declared` and `blockers`** | a declared contamination is an input to the method judgement, not a disqualification of it | receipt schema |
| 🔴 **reader identity** | its output is *failure modes **per reading***, and the 12 taxonomy gates are scored per reader. Attribution is required | § 8.2 `FAILURE MODES` row |

🔴 **The asymmetry worth stating: Mirror receives identity and the blind agents do not.** The
locator audit's auditor *"receives triples + packet, **never the dossier or the reader's name**"*.
Two review surfaces sit adjacent in the pipeline, and blindness is a property of one and not the
other — because they answer different questions. An implementation that blinds both loses Mirror's
per-reading failure analysis; one that blinds neither loses the audit's independence.

### 5.2 · What Mirror must NOT receive — eight, each traced

| # | Must not receive | Why, measured |
|---|---|---|
| **1** | **a reading task, or a request to supply a missing locator** | Mirror *"produces no primary evidence"*. Supplying evidence would make it an author of what it reviews |
| **2** | **any first pass before both freezes** | the ordering rule; a pre-freeze delivery makes the reviewer a contamination channel |
| **3** | **the question of which reading is scientifically better** | `MECHANISTIC VALUE` is *"recorded descriptively — the judgment of value is not made inside the benchmark"*; it routes to an Annex C review opened by Orchestrator, **outside** the record |
| **4** | **a request to adjudicate a challenge** | H.1: *aggiudicazione challenge → **Orchestrator**, con rationale* |
| **5** | **a pre-approval request, or anything shaped as a veto before the fact** | Mirror's review of Orchestrator is *ex post and pattern-based — never a veto before the fact* |
| **6** | **its own rubric, clustering, active-learning selection, review-yield or autonomy methodology, for approval** | G.2: Mirror does not self-approve these. Route: `MIRROR_UPGRADE_PROPOSAL` → Plan candidate → an independent reviewer **chosen by Orchestrator** → validation; governance → operator |
| **7** | **`roles/mirror.md` to review** | the self-review prohibition. Measured consequence: `REV-ROLES-MIRROR-001` emitted verdicts on three contracts and **no verdict on the fourth** |
| **8** | **a composite score, a weighting, or a ranked summary** | § 8.5: *No overall score. No weighting. Each dimension its own table, with the route that produced each number.* Agreement between A and B is descriptive — *two readers agreeing on an overshoot is two overshoots* |

**And one framing constraint that belongs with them:** Mirror asks **why**, never **who won** —
`noise vs individual strength vs reusable strategy vs systemic weakness`, distinguished before
anything is promoted.

### 5.3 · 🔴 Two preconditions on Mirror's own input are not satisfied

1. **Annex G.3 makes the consolidated J.1 event ledger Mirror's primary analysis surface** — *not
   by reading fifty chats*. `roles/mirror.md` records that capability as **blocked: the ledger has
   no writer yet**, `UNVERIFIED` (N-4). Mirror's stated instrument does not exist.
2. **Mirror's perimeter is `MIRROR_REQUIRED` for R4, protocols, governance, repeated dissent and
   recurring failures** — and the benchmark's own `REVIEW_REQUIREMENT` is R4. So Mirror is
   required, on an input surface that is missing, for the first cycle.

### 5.4 · What returns to Orchestrator

Re-measured and unchanged from `SCIENTIST-PIPELINE-EXECUTION-MODEL-001` § 7, and not restated
here: `TASK_COMPLETE` with the Annex B.1 envelope, `DURABLE_POINTER` + tree digest, the validator's
verdict line, the coverage map, the listed ambiguities and — MODE B — the critical-record entries.
`ACTOR_ID` is identity, `FROM` is routing; nothing is keyed by `SESSION_REF`.

The one gap carried forward, because it bears directly on the lifecycle mapped in § 3.6:
🔴 **"remaining workload" has no carrier** in Annex A or Annex B. Nearest instruments are
`STATUS_UPDATE`, `HEARTBEAT` and Plan's reconciliation over `ledger/tasks/*/`. Creating one is a
schema change and is **not done here**.

---

## 6 · FUTURE EXPANSION — D and E, three readings, none decided

> **The dispatch says: do not decide. Nothing here decides.** What follows is what each of the
> three readings would collide with, measured, so a decision is made against concrete alternatives.

`scientist-e`: **zero occurrences on any ref.** `scientist-d`: six occurrences in three files, all
the same use — the **generality falsifier** of `CAND-20260819-XPORT` § 9.2, plus two ledger notes
recording that no `scientist-d` was created. It is a test fixture, not a proposal.

| Reading | Status | What it meets |
|---|---|---|
| **additional readers** | ⚠️ **SUPPORTED, and cheap** | XPORT § 9.2 measures the onboarding delta at five configuration steps — ACTOR_ID, role binding (`roles/scientist.md` **unchanged**), one worktree row, fingerprint (**derived, not added** — P2.2 is keyed by ROLE, so D composes the same value as A, B and C), registration, acceptance test. *"That is configuration, not protocol redesign."* It adds reading throughput and bodies for the R3 TRIADIC floor |
| **adjudicators** | ⚠️ **PARTIALLY SUPPORTED — in one shape only, and NOT as a dedicated role** | An `ADJUDICATOR` exists in C.3 (`AUTHOR ≠ REVIEWER ≠ ADJUDICATOR`) and R3 TRIADIC is a real floor. But 🔴 **C.3 also requires *rotazione; mai coppie fisse*. A Scientist D whose function IS adjudication is a fixed role in every triad it joins — which is the fixed pairing C.3 forbids, and the static specialization § 32 forbids.** Adjudication is a **turn**, not a post. And it is bounded twice more: adjudicating a **peer review of a claim**, never two frozen first passes; and **never a challenge**, which H.1 gives to Orchestrator |
| **integrators** | 🔴 **UNSUPPORTED** | The integration layer is already allocated — body § 30 to Plan — **with a boundary attached**: § 28, *Plan **NON risolve significato scientifico conteso***. An integrator D is therefore either a duplicate of Plan with no rule saying whose `INTEGRATION_BLOCK` binds, or an integrator without § 28 — an actor that resolves contested meaning, which **no actor in this repository is authorized to do**: Orchestrator is denied it by H.1, Plan by § 28, Mirror by having no primary evidence, and the system as a whole by § 27 |

**Recorded, not recommended.** An actor proposing the reading that would give its own role class a
new function is the convenient interpretation the gate exists to prevent — the ground on which
Mirror declined a structurally identical question in `REV-ROLES-MIRROR-001` § 8. Carried as **Q-3**.

---

## OPEN_QUESTIONS

### 7 · Recorded, not resolved — each with a disposition owner who is not this session

| # | Question | Owner |
|---|---|---|
| **Q-1** | Should a reading receive a **question** or an **evidence target**? Neither exists (N-1) and § 3.2 measures three rules that exclude them. If one is wanted, what protects the fixed unranked denominator and the no-`not_read` completion criterion from being narrowed by it? | operator |
| **Q-2** | `HANDOFF` (Annex B message type) and `HANDOVER` (benchmark writer transfer) are two objects with near-identical names and no disambiguation. Naming is a governed change. | Plan (vocabulary) / operator |
| **Q-3** | Are future `scientist-d`/`scientist-e` **additional readers** (supported, five-step delta), **adjudicators** (a turn under C.3 rotation — never a dedicated post), or **integrators** (unsupported; § 28 already allocates integration with a boundary)? | operator |
| **Q-4** | **`missing evidence` has no per-claim home** (N-2). The concept exists three times, addressed to three different objects — a review field, a critical-record entry field, and a completion criterion. Should a claim carry it, and would that be a benchmark field or a canonical one? | operator / Mirror (epistemic curation) |
| **Q-5** | **No J.1 event type corresponds to a freeze, a read, or an analysis** (N-3), and the ledger has no writer (N-4). The freeze is the immutability anchor of the whole design and emits nothing into the surface Mirror is required to analyse from. | operator / Plan |
| **Q-6** | Whether READ and ANALYZE are separable stages is decided per task, by `MILESTONE_PLAN`, written by Orchestrator before the reading starts (§ 3.7). Is that the intended allocation, and what calibrates it before Mirror's redone-work ratio has any data? | Orchestrator / Mirror |
| **Q-7** | `PARALLEL_READ_GROUP` is an extension field standing on A.1's *extendible, never removable* clause. Promotion into Annex A is a separate governed change and has not happened — yet the entire two-reader model rests on it. | operator (H.1) |
| **Q-8** | Three of six contamination classes are reachable **only** by the reader's self-declaration (§ 4.3). The design prices honesty but does not compel it. Is a priced declaration an acceptable control for a first cycle, and what would measure whether it worked? | operator / Mirror |
| **Q-9** | Carried, unchanged, because it gates everything above: the four role contracts are `PROPOSED` and non-binding by `DEC-20260822`; its consequence 3 requires a new explicit activation act whose **form it does not specify**. | operator (H.1) |

---

## VALIDATION

### 8 · Constraint compliance — checked, not asserted

| Constraint from the dispatch | Result |
|---|---|
| Act as Plan; analysis only | ✅ one file added under `learning/plan/`; no directive issued, no actor addressed |
| **No actor creation** | ✅ no `Agent`, `SendMessage` or `Task` call made; no registration written; `ledger/registrations/` still absent on every ref |
| **No role activation** | ✅ § 1 records the `PROPOSED` state under `DEC-20260822`; nothing acts on it |
| **No contract binding** | ✅ no `status:` line read as binding; no protocol declared in force; Q-7 and Q-9 record the unresolved bindings |
| Do NOT create Scientist agents | ✅ none created, spawned or configured |
| No implementation | ✅ nothing built, no surface created, no manifest frozen, no script written |
| No schema created | ✅ § 3.5 evaluates the six separations against existing homes; the one without a home is recorded as **Q-4**, not filled |
| Do not decide on D/E | ✅ § 6 states what each reading collides with and explicitly withholds a recommendation |
| `governance/` `roles/` `framework/` `ledger/` untouched | ✅ `git status --porcelain` over those four roots → 0 changed paths |
| No paper read, no scientific conclusion | ✅ the one PMID that appears is read from manifest and instruction fields as the benchmark's configured subject, never from a paper |

### 8.1 · Domain and collision disclosure

- **Content domain.** `learning/` is not a `CONTROL_PLANE_ROOT` (P5.1); this file is inside the
  `CANDIDATE_CONTENT_HASH` of any future candidate including this branch and moves it.
- **No base condition invalidated.** No open candidate declares `a10a11a` as its `BASE_HEAD`.
- **Cross-ref reads were reads.** `main` and `orchestrator` were read via `git show <ref>:<path>`.
  Nothing was merged, checked out, or written outside this worktree.

### 8.2 · What this record does NOT do

It does **not** create, register, configure or contact any actor · does **not** activate or bind a
contract · does **not** issue a Task Contract, a `PARALLEL_READ_GROUP`, a Mirror task, a message or
a ledger event · does **not** build, verify or freeze a surface · does **not** create a schema, a
field, an event type or a vocabulary · does **not** resolve Q-1…Q-9 · does **not** decide the
function of `scientist-d` or `scientist-e` · is **not** an `AUTHOR_RESPONSE`, an
`INTEGRATION_CANDIDATE` or a `CANONICAL_BATCH_COMMIT`.

---

## NEXT_TRANSITION

```
FROM   the Scientist contract analysed at its four boundaries — input, output, lifecycle,
       handoff — against the materialized instruction set rather than a reconstruction

TO     nothing this session can enter. Every unblocking act belongs to the operator, to a
       governance clarification, or to an implementation that requires one of those first.

THE FOUR ORDERING FACTS WORTH CARRYING FORWARD:

  1  THE INPUT CONTRACT ALREADY EXISTS, AND 200 OF ITS 592 LINES ARE REUSABLE VERBATIM.
     MODE_A.md, MODE_B.md and SURFACE_CLAUDE.md carry zero paper references. Whoever builds a
     second reading builds a packet, a population and two assignments — not a workflow.

  2  THE PIPELINE IS BUILT SO THAT NOTHING NARROWS THE READING, AND A "QUESTION" WOULD.
     The fixed unranked denominator, the no-`not_read` completion criterion and the ban on grep
     as a method are three expressions of one design. Supplying a target is not a small
     convenience — it is the READING_DEBT_FALSE_NEGATIVE gate, moved to where no validator looks.

  3  CONTEXT ABOUT THE ASSIGNMENT IS MANDATORY; CONTEXT ABOUT THE CONTENT IS FORBIDDEN.
     One sentence resolves what looked like a contradiction between A.4/A.7 and the
     contamination rules — and it inverts outside a blind first pass, which is why the route
     must be a property of the Task Contract and never an assumption of the implementation.

  4  ONE ABSENT OBJECT STILL CARRIES THREE GUARANTEES, AND THIS RECORD ADDS A FOURTH USE.
     The J.1 event ledger has no writer. Resting on it: Mirror's primary analysis surface (G.3),
     Mirror's anti-fossilization guard over reading modes (§32), the only route from
     after-the-fact detection toward prevention for the unmechanized contamination rule — and
     now the freeze itself, which is the immutability anchor of the entire design and currently
     emits no event at all.

WHAT THIS SESSION HANDS OVER:
       this record. No recipient is named — session routing is unresolved repository-wide and
       no destination is invented here.
```

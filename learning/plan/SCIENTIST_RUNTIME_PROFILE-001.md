---
artifact: SCIENTIST RUNTIME PROFILE — the minimum operating profile of Scientist A/B, measured
record_id: SCIENTIST_RUNTIME_PROFILE-001
task_id: SCIENTIST_RUNTIME_PROFILE_v1
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
  - NOT A ROLE

naming_note: >
  Not a Session Learning Record (Annex E.6) and not a handoff. Named as the dispatch named it,
  and takes no `SLR` number it has not earned — the precedent of the four non-SLR records
  already in this seat.

domain: >
  CONTENT — verified, not assumed. `governance/plan_defined_parameters.md` § P5.1 declares
  `CONTROL_PLANE_ROOTS` exhaustively as `governance/candidates/`, `ledger/`, `reviews/`
  (lines 258–262, read this session). `learning/` is under none of them, so this file is inside
  the `CANDIDATE_CONTENT_HASH` of any future candidate spanning this branch, and moves it.
  Disclosed.

relation_to_prior_work: >
  Four records on this branch touch adjacent ground: `SCIENTIST-PIPELINE-READINESS-001`,
  `SCIENTIST-PIPELINE-EXECUTION-MODEL-001`, `SCIENTIST-BOOTSTRAP-CONTRACT-ANALYSIS-001` and
  `SLR-plan-C9-STATE-RECONSTRUCTION-BOUNDARY-001`. Between them they already answer, section by
  section, most of what this dispatch asks: inputs (BOOTSTRAP-CONTRACT § 3), blindness
  (§ 4.1–4.3), the output object (EXECUTION-MODEL § 5), A/B/C/D/E (EXECUTION-MODEL § 3.1–3.4),
  and a first-experiment structure (READINESS § 9). **This record does not restate them.** It
  answers the one thing the dispatch's own wording asks and none of them was asked: what the
  minimum profile is for **real** scientific experiments — and reports that the first experiment
  designed in this repository is not one. Every fact reused from a prior record was re-measured
  here first; two of them came back different.

verdict_transfer: >
  NONE. Every mechanical fact below was executed in this session at the HEAD named in § 1.
---

# SCIENTIST RUNTIME PROFILE — 001

> **The two findings that shape this record.**
>
> **1 · The minimum operating profile is not missing, and it is not a design problem.** It is
> materialized: **20 files per reader** in a built surface, from a **592-line** reader-facing
> instruction set, a **748-line** protocol, a **526-line** reading-modes directive, a
> **122-line** shared contract, a **65-unit** evaluation population computed by command, and a
> **79 KB** builder that can `build`, `verify`, `freeze` and `verify --post-read`. Not one of
> the dispatch's six study areas requires a new object. What is missing is **authorization**,
> and all seven preconditions reduce to one candidate that carries no approval line.
>
> **2 · 🔴 The dispatch asks for the profile to begin *real* scientific experiments. BENCH-AB-001
> is not one, and was never designed to be one.** It quarantines its own output by construction
> — *"None of the seven is written to `claim_registry_current.md`"* — and § 10 forbids it to
> integrate a claim into the disease model. The configuration that would produce science that
> enters the model **does not exist on any ref**: `BENCH-AB-002` and every equivalent name
> return zero. And the property that makes the first experiment checkable — a surface **outside
> every LEGEND checkout, containing no corpus** — is the property a real reading cannot keep.
> The gap is structural, not a missing file.

---

## TASK_STATUS

```
TASK_ID          SCIENTIST_RUNTIME_PROFILE_v1
MODE             ANALYSIS ONLY · no actor creation · no role activation · no contract binding
STATE            COMPLETE — the six study areas are answered from measurement; every answer that
                 could not be measured is an open question with an owner who is not this session

EXECUTED         the 7 instruction files read in full · the surface spec, benchmark manifest and
                 evaluation population parsed · protocol §0–§1, §4.3, §8–§10 read · 8 executable
                 checks re-run (lease derivation, fingerprint composition + its 12 inputs,
                 approval-queue parse, 12-path byte comparison against main, population parse,
                 surface-spec parse, builder subcommand contract, cross-ref greps)
NOT EXECUTED     no Scientist created, spawned, contacted or assigned · no paper opened · no
                 literature read · no scientific conclusion formed · no contract activated or
                 bound · no benchmark surface built · no path under governance/ roles/
                 framework/ ledger/ runtime/ modified · no schema, field or vocabulary created
FILES ADDED      exactly one — this file
```

---

## IDENTITY

### 1 · From repository evidence; not from `roles/plan.md`, which is not binding

| Field | Measured value | Command |
|---|---|---|
| branch | `plan-orchsurf-r4-transcription` | `git rev-parse --abbrev-ref HEAD` |
| HEAD | `9e1019088b1ded1095c027e558da854729783c74` | `git rev-parse HEAD` |
| worktree | `.claude/worktrees/evidence-index` | `git rev-parse --show-toplevel` |
| working tree | **clean** at session start | `git status --porcelain` → empty |
| lease | **`ACTIVE by derivation: 0`** | `python3 framework/scripts/lease_state.py` |

**`CLAUDE.md` § 0: no ACTIVE lease and no runtime inventory ⇒ `BOOTSTRAP_MODE`.** This session is
not Orchestrator, issues nothing, and creates no actor. The single act it performs — writing one
file under `learning/plan/` on its own branch — traces to H.1's `WORK_COMMIT` row (*"ogni attore,
solo proprio branch, granularità milestone"*), an annex, not a role contract.

**The governing determination, re-read this session:**
`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` (on `main`, **not on this ref** — the diff against
main shows it as 362 deletions here) records `E-2`: `git log --all -S'status: ACTIVE' -- roles/`
and `-S'status: BINDING' -- roles/` are **both empty across all refs**. No activated status has
ever existed in `roles/`. Every statement below about `roles/scientist.md` is made under that.

---

## SURFACE_MAP

### 2 · What was measured, and where

| Object | Path | Measured state |
|---|---|---|
| reader instruction set | `framework/eval/benchmarks/BENCH-AB-001/instructions/` | 7 files, **592 lines**; canonical on `main` and present here |
| surface spec | `…/BENCH-AB-001/surface_spec.json` | parses; 18 keys; the allowlist is enumerated, not described |
| benchmark manifest | `…/BENCH-AB-001/benchmark_manifest.json` | `_state: PREPARED — NOT FROZEN`; digests marked `DERIVED_AT_BUILD` |
| evaluation population | `…/BENCH-AB-001/population/evidence_units.json` | **65 units, 109 panels**, 18 declared notes, 1 declared-empty source — computed, not stubbed |
| benchmark protocol | `framework/protocols/controlled_benchmark_ab.md` | 748 lines; `status: PROPOSED` |
| reading modes | `framework/protocols/scientist_reading_modes.md` | 526 lines; `status: PROPOSED` |
| role contract | `roles/scientist.md` | 122 lines; `status: PROPOSED`; byte-identical to `main` |
| builder | `framework/scripts/benchmark_input_surface.py` | 79 395 bytes; 7 subcommands: `build · verify · freeze · verify-freeze · population · locators · tree-digest` |
| the paper packet | `files/fulltext/PMID42397075_*` | **present and complete** — PDF 3 341 414 B, text surface 91 848 B, 5 supplements `File008`–`File012` |
| Agent Card registry | `runtime/agent_card_registry.md` | exists **only on branch `orchestrator`**; absent from `main` |
| approval queue | `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` | 6 lines, all parse; 2 approvals, both `CAND-20260816-GOV311` |

### 2.1 · Negative claims — each with what was run and how long it holds

| # | Claim | Command | Measured | Validity |
|---|---|---|---|---|
| N-1 | **No second/production benchmark configuration exists on any ref** | `grep -rniE 'BENCH-AB-00[2-9]\|production_read\|real_read\|BENCH-PROD'` over `*.md *.json *.py` | **0 hits** | until an object introduces one |
| N-2 | **No benchmark surface has been built** | `find` for `BENCH-AB*` outside the checkout; manifest `_state` | none found; `PREPARED — NOT FROZEN` | until `build` runs |
| N-3 | **No Task Contract exists for any Scientist** | `ls -R ledger/tasks/` | one directory, `plan/`, 5 files, all Plan's | until Orchestrator issues one under lease |
| N-4 | **`CAND-20260818-SCIENTIST-AB-SPEC` carries no approval line** | JSON parse of all 6 queue lines | 2 `APPROVED`, both `CAND-20260816-GOV311`; the AB-SPEC candidate appears in neither | until a resolution line is appended |
| N-5 | **The evaluation population is not in either reader's surface** | `surface_spec.json` → `common_files` (11) + `source_files` (7) + `per_actor_files` (2) | `population/` appears in none | while the spec is unchanged |
| N-6 | **MODE A has no carrier for "missing evidence"** | `grep -niE 'omission\|expected to see\|did not find\|missing'` on `MODE_A.md` | **0 hits**; `MODE_B.md` line 56 carries `OMISSION` | until a directive adds one |

---

## EXISTING_COMPONENTS

### 3 · The reader's surface is 20 files, and they are enumerated, not described

This is the concrete answer to *"what must a Scientist receive"*: not a list of concepts, a
manifest. Measured from `surface_spec.json`.

| Class | Count | Contents |
|---|---|---|
| `common_files` | **11** | `CLAUDE.md` (surface router) · `BENCHMARK_INSTRUCTIONS.md` · `OUTPUT_SCHEMA.md` · `roles/scientist.md` · `epistemic_discipline.md` · `gold_is_in_the_details.md` · `fulltext_read_receipt.md` · `scientist_reading_modes.md` · `failure_taxonomy.md` · `deepdive_manifest.py` · `corpus_firewall.py` |
| `source_files` | **7** | the article PDF · its extracted text surface · `File008`–`File012` |
| `per_actor_files` | **2** | `ASSIGNMENT.md` and `benchmark/MODE_DIRECTIVE.md` |
| **total per surface** | **20** | |

Two things in that table are worth naming because neither is obvious.

**`controlled_benchmark_ab.md` is in `forbidden_prior_output_paths`, not in the surface.** The
readers are given the *reading* protocol and denied the *benchmark* protocol. They are told what
to do and not how they are being measured — 23 forbidden paths in all, and the protocol that
designs the experiment is one of them.

**`scientist_reading_modes.md` *is* common — and it describes both modes in full.** This is the
protocol's own § 0 caveat 2, and it is correct: the manipulated variable is not *knowledge of the
two modes*, it is **which directive is addressed to you**. Recorded there as a known contamination
of the variable and not softened; re-measured here and unchanged.

### 4 · Where the dispatch's seven output concepts already live

The dispatch asks to verify where these exist. They exist; four map cleanly, three do not, and
the three that do not are the finding.

| Dispatch concept | Measured home | Verdict |
|---|---|---|
| **Observation** | `OUTPUT_SCHEMA.md` § 3, required field | ✅ exists |
| **Interpretation** | **two fields, not one** — `Author interpretation` and `LEGEND interpretation` | ⚠️ **splits.** The schema's own note: *"The seam is the point… the one thing a second reader must be able to attack is where measurement ends and conclusion begins."* A single `Interpretation` field would collapse exactly the seam the design exists to hold open |
| **Hypothesis** | not a field — the epistemic **`Type`** (`DATO · INFERENZA · IPOTESI · ESPANSIONE`), compound values allowed | ⚠️ **a type, not a slot.** A hypothesis is a property *of* a claim, not a container beside it |
| **Evidence** | `verbatim_locators` + `source_artifacts` (manifest) and `Locators:` (claim) | ✅ exists, in the validated shape |
| **Uncertainty** | `OUTPUT_SCHEMA.md` § 3, required field | ✅ exists — and the schema records that it appears **0 times** as a label across the 39 claims of `claim_registry_current.md`, which is why it is a benchmark field rather than an existing convention |
| **Missing evidence** | 🔴 **`OMISSION` axis — MODE B only** (`MODE_B.md` line 56) | 🔴 **asymmetric.** `MODE_A.md` returns **0 hits** for it (N-6). MODE A routes weaknesses to `Limitations`, `Uncertainty`, `Contradictory evidence`; none of those is *"what I expected to see and did not find"*. On this concept **A and B are not comparable, because only one of them is asked** |
| **Contradictions** | `Contradictory evidence` field (both) + `CONTRADICTORY_EVIDENCE` axis (B) | ✅ exists in both, at different depths |

🔴 **The `OMISSION` asymmetry is the one place where the dispatch's output model and the
materialized one genuinely disagree**, and it is not a defect in either: the benchmark's variable
*is* the mode, and searching for omissions is part of what MODE B means. But it does mean that
**"missing evidence" cannot be a comparison dimension between A and B** — and § 8.2's
`CONTRADICTION / NEGATIVE EVIDENCE` row correctly does not make it one; it measures negatives for
both and axis-completeness for B alone. Stated here so no later reader treats A's silence on
omissions as a finding about A.

---

## RUNTIME_MODEL

### 5 · Input — necessary, useful, contaminating

The dispatch's six-item list (`paper · metadata · task objective · allowed sources · constraints ·
previous context`) was mapped against the materialized contract in `SCIENTIST-BOOTSTRAP-CONTRACT-
ANALYSIS-001` § 3.1 and is not remapped here. What follows is the trichotomy that record did not
draw, over the input set as actually built.

**NECESSARY** — remove any one and the reading is not reproducible:

| Input | Carrier | Why load-bearing |
|---|---|---|
| `ACTOR_ID`, permanent, explicitly **not** the session | `ASSIGNMENT.md` | attribution survives restart; the session ref is ephemeral and is never the identity of record |
| `TASK_ID` · `MODE` · `PARALLEL_READ_GROUP` | `ASSIGNMENT.md` | the group declaration is what makes two readings *intended* rather than a `DUPLICATED_ASSIGNMENT` |
| `INTERACTION_MODE: AUTONOMOUS_COMPLETE` | `ASSIGNMENT.md` | a reader that may ask questions has a channel; a channel is a contamination path |
| the bytes — 7 packet files | `source_files` | *the same bytes*, digest-verified equal across surfaces, is the experiment's floor |
| the discipline set — 6 normative files | `common_files` | the scientific method is not suspended by the benchmark |
| the output shapes | `OUTPUT_SCHEMA.md` | a comparison needs one shape; *"if you find yourself inventing a container, the container already exists"* |
| the completion gate | `BENCHMARK_INSTRUCTIONS.md` § 5 | `VERDICT: PASS` is a precondition of completion — a machine check, not a self-report |
| the two prohibitions | § 6 | no prior output, no contact |

**USEFUL, NOT NECESSARY** — present, and the reading would still be reproducible without them:
`failure_taxonomy.md` (names the gates MODE B's axes already name), `corpus_firewall.py` and
`deepdive_manifest.py` (tools — the validator matters at the gate, not during), and the depth /
budget rule of § 3, which is a guard against a known failure mode rather than an input.

**CONTAMINATING — affirmatively excluded, each with the mechanism that excludes it:**

| Excluded | Mechanism | Measured |
|---|---|---|
| LEGEND's prior output on this paper | `forbidden_prior_output_paths` | **23 paths**, incl. the prior manifest at the exact slot the reader must write |
| the corpus and every registry | absent from the allowlist | `claim_registry_current.md`, `working_model_current.md`, `paper_registry_current.md` all forbidden |
| the other reader's work or identity | no channel; separate repos; *"Orchestrator relays no content"* | structural |
| **a research question / evidence target** | not in any input file | excluded **by design**, not omitted — see BOOTSTRAP-CONTRACT § 3.2 |
| the evaluation population | not in the surface (N-5) | Plan holds the denominator; a reader who knew it could optimize coverage against it |
| the benchmark protocol itself | forbidden path | the reader is not shown its own scoring design |

The pattern under all six: **an input is contaminating when it tells the reader something about
the answer, the other reader, or the measurement.** The packet, the discipline and the shape are
none of those.

### 6 · Scientist A and B — equivalent actors, differing tasks

**Equivalent, and measured, not asserted.** One shared contract file — *"ONE contract shared by
all three scientists"* — one `ROLE_CONTRACT_HASH`, and one fingerprint value across the row set:
the runtime inventory carries `ce3c0d94…` for `scientist-a`, `scientist-b` **and** `scientist-c`
alike, *"hence one fingerprint value across the row set"* (line 158). Body § 32: same mandate,
same protocol, same scientific authority, same obligations, same isolation, **no static
specializations**.

**Different only as tasks.** `roles/scientist.md`: *"The mode is a property of the task, not of
the actor… a mode that stops rotating has become the static specialization § 32 forbids."* So the
answer to the dispatch's question is not *"A and B are different kinds of reader"* — it is that
`scientist-a` and `scientist-b` are interchangeable actors who happen to hold `MODE_A` and
`MODE_B` in this instance, and Mirror's anti-fossilization guard exists precisely to stop that
pairing from hardening into identity.

🔴 **One consequence the dispatch should carry.** If A and B are equivalent and the mode must
rotate, then **`BENCH-AB-001`'s result is not a property of `scientist-a`**. Reporting it as
"A did better than B" would be the fossilization the contract forbids, restated as a finding.
§ 8.5 already refuses it: no overall score, and agreement between A and B *"is not a quality
measure — two readers agreeing on an overshoot is two overshoots."*

### 7 · Scientist C, D, E

`EXECUTION-MODEL-001` § 3.3–3.4 answered this; re-measured here, and the counts hold.

**C — exists as an actor, undecided as a function, and the registration is inverted.**
`roles/scientist.md` lists `scientist-c` in `actor_ids` with status `PROPOSED`; body § 32 says
*"Scientist C da creare subito (`lettore-c`), qualificato insieme ad A/B"*; the worktree and
branch `lettore-c` both exist. 🔴 **And the inversion measured in the runtime inventory is the
operationally significant fact:**

```
scientist-c  (PROPOSED in the contract)      → REGISTERED_PENDING_L1_L2, fingerprint verified
scientist-a  (FIXED on candidate execution)  → NOT_REGISTERED, ACTOR_ID UNRESOLVED
scientist-b  (FIXED on candidate execution)  → NOT_REGISTERED, ACTOR_ID UNRESOLVED
```

The one Scientist that is registered is the one the benchmark does not use; the two the benchmark
needs are the two that are not. The inventory states why: A's and B's worktrees *"still carry no
governance at all (136 and 138 commits behind), so there is nothing in them to acknowledge."*

**Is C a duplication?** Not as an actor — three equivalent actors are what § 32 asks for. It
would become one the moment C is given a *fixed function*. `APPROVAL-GOV311-DEVIATIONS.md`
line 265 sketches `Scientist A → Scientist B hostile review → Scientist C adjudication →
Orchestrator escalation`, and that sketch is exactly the shape C.3 forbids: adjudication as a
**post** rather than a **turn** violates *rotazione; mai coppie fisse*. § 10 of the protocol also
excludes running a Scientist C arm in this benchmark. **Nothing here decides C's function, and
nothing needs to for the first experiment.**

**D and E.** `scientist-e`: **zero occurrences on any ref** — nothing to evaluate; the name is
the dispatch's, not the repository's. `scientist-d`: six occurrences in three files, every one of
them the *same* use — a hypothetical, either an out-of-scope note recording that no `scientist-d`
was created, or § 9.2's *"Scientist D falsifier"* onboarding fixture. **It is a test fixture, not
a proposal.** Neither answers *"when do they serve"*, because neither was ever a proposal to
serve. The question is live and it is the operator's (Q-3, carried below).

**No automatic synthesis is proposed, and none is supported.** The dispatch's own instruction and
the measurement agree: `INFERENCE_A + INFERENCE_B + DISAGREEMENT_UNRESOLVED`, explained, is a
legitimate outcome under body § 27, and § 8.3 sends every disagreement flag to
`unresolved_disagreements.md` to **stay** unresolved. A synthesis actor would be the mechanism
that resolves what the design keeps open.

---

## CONTAMINATION_MODEL

### 8 · What must be equal, what must differ, and how each is checked

**Equal: everything except two files.** Not a promise — a spec key. `per_actor_files` names
exactly two entries per actor, and they land at the same two surface paths:

```
ASSIGNMENT.scientist-a.md → ASSIGNMENT.md              ASSIGNMENT.scientist-b.md → ASSIGNMENT.md
MODE_A.md → benchmark/MODE_DIRECTIVE.md                MODE_B.md → benchmark/MODE_DIRECTIVE.md
```

18 of 20 files are byte-identical by construction, and `verify` enforces *"parity across
surfaces, forbidden paths absent, no file outside the allowlist, and a content scan for the
paper's own identifiers in everything that is not the paper."*

**Different: the mode directive, and nothing else.** With the § 0 caveat that the *other*
directive is still readable inside the common `scientist_reading_modes.md` — so the variable is
attention, not information.

### 9 · The freeze is two events, not one

The dispatch asks *when* the freeze happens, in the singular. The repository has two, at opposite
ends of the run, owned by different parties.

| | **INPUT FREEZE** | **OUTPUT FREEZE** |
|---|---|---|
| what | the surface and its manifest | each reader's first pass |
| when | at build, **immediately before handover** | at the reader's completion declaration |
| stated where | `benchmark_manifest.json` `_state` | `ASSIGNMENT.md`, both readers |
| the words | *"Freezing happens at build time, immediately before handover, and only after every precondition of § 1 is satisfied"* | *"frozen immediately, before its content is read by anyone"* |
| owner | Plan (builds, verifies, freezes) | the reader (declares); Plan imports by digest |
| current state | **NOT FROZEN** | not applicable — no reading exists |

**Why the second one's timing is the load-bearing part.** *Before its content is read by anyone*
means the freeze precedes any possibility of the record being adjusted to what the other reader
found. Corrections after that point are separate dated files, reported as corrections. A freeze
that happened after someone had read the content would be a formality.

### 10 · The instruments, and the exact limit of each

| Phase | Instrument | What it actually reaches |
|---|---|---|
| before | separate directories, separate repositories | prevents shared state; does not prevent a reader leaving the surface |
| before | `forbidden_prior_output_paths` (23) + `CONTENT_SCAN` | proves the prior output is **absent**; verified 2026-08-18 at 0 hits on all nine non-instruction text files |
| during | no channel; Orchestrator relays no content; a `BLOCKER` is answered *on the protocol, never on the paper* | prevents relayed contamination; cannot prevent a reader reading elsewhere |
| after | `deepdive_manifest.py --verify-artifacts` | existence and digest of every cited artifact |
| after | `benchmark_input_surface.py locators` | **membership in the allowlist, per entry** — a citation from outside is `BENCH_INVALID` for that entry, *recorded, never silently dropped* |
| after | `verify --post-read` | parity and allowlist still hold; prints the **blind spot** by name — the reader's own manifest path, which collides with LEGEND's prior manifest slot because `deepdive_manifest.py` derives it from disease + PMID and it cannot be elsewhere |

🔴 **Two contaminations are declared in the design and are not defects to fix.** Both are § 0's:
**session variance is not separable from mode** with one paper and one session per actor; and
**each reader can read the other's mode directive** in the common protocol. They bound what the
first experiment can conclude, and the protocol says so before it says anything else.

**The honest limit of the whole apparatus:** every *before* and *after* check is mechanical and
strong; every *during* check is a prohibition. A reader who opens another checkout mid-read is
caught only if the locators betray it. The design's answer is to make declaring it cheap —
*"a declared contamination is a usable result, and an undeclared one silently invalidates the
experiment for everyone."*

---

## FIRST_EXPERIMENT

### 11 · It is already designed, in more detail than the dispatch asks for

The dispatch asks to design the first test. Measured: it exists, and re-designing it would
produce a second, competing specification for the same experiment.

| Dispatch asks | Measured answer | Source |
|---|---|---|
| number of papers | **1** — PMID 42397075, doi 10.1093/brain/awag239, Brain 2026 | protocol § 0 |
| number of Scientists | **2** — `scientist-a` MODE A, `scientist-b` MODE B | manifest `ACTORS` |
| input | **20 files per surface**, 18 identical, 2 differing | `surface_spec.json` |
| output | 4 artifacts (5 for B): work manifest · dossier · claim candidates · receipt · critical reading | `OUTPUT_SCHEMA.md` |
| independence verified | before / during / after, § 10 above; population fixed at **65 units, 109 panels** before anyone reads | protocol § 4, § 8.1 |
| success / failure criteria | 🔴 **the protocol refuses to define one** | § 8.5 |

### 12 · 🔴 The refusal of a success criterion is a design position, not a gap

§ 8.5: **"No overall score. No weighting."** Each of the ten dimensions gets its own table, A and
B side by side, with the route that produced each number. Speed, tokens, cost and output length
are recorded in a separate table and *"never enter a quality judgment"*. Agreement is descriptive
and explicitly not a quality measure.

So the dispatch's *"criteri successo/fallimento"* has a measured answer, and it is not a
threshold: **the experiment succeeds by producing its material** — two frozen readings, a blind
locator audit, an adjudication — and by surfacing failure modes. § 0: *"Its value is the
material it produces… and the failure modes it surfaces, not a number."* A partial reading,
declared with an honest coverage map, is a legitimate result. The only genuine failure states are
an **undeclared** contamination, a **silently thinned** reading claimed as complete, and a
handover made while any § 1 precondition is unsatisfied.

### 13 · 🔴 And it is not a real scientific experiment

This is the gap the dispatch's wording exposes and no prior record was asked to name.

| | `BENCH-AB-001` | what *"esperimenti scientifici reali"* requires |
|---|---|---|
| purpose | measure how two modes read | learn something about WWOX |
| where | a standalone repository **outside every LEGEND checkout** | inside the model, against the corpus |
| corpus access | **none** — `corpus_crossquery`, `multihop`, `group_assessment` are **waived**, and the schema instructs the reader to *"waive them, and say THAT is why"* | required — a reading that cannot cross-query the corpus cannot situate its finding |
| output destination | **quarantined** — *"None of the seven is written to `claim_registry_current.md`"*; § 10 forbids integrating a claim into the disease model or writing any `*_current.md` | must reach `INGEST → DEEP_DIVE → COMMIT` and the four current files via `BATCH_COMMIT` |
| wikilinks | forbidden to the registry — *"this surface has no registry and a wikilink to one would be a dangling assertion"* | the registry link is the point |
| receipt | `BENCH-AB-001-<ACTOR>-01` — *"benchmark id, NOT a receipt-ledger id: this reading does not touch the ledger"* | must anchor in the hash-chained receipt ledger |

**The tension is structural.** Blindness is achieved *by* removing the corpus — that is what makes
`FORBIDDEN_PRIOR_OUTPUT_PATHS` and the content scan mechanically checkable. A real reading needs
the corpus. **The mechanism that makes the first experiment trustworthy is the mechanism a real
experiment cannot keep**, and nothing on any ref resolves that (N-1).

This does not make BENCH-AB-001 the wrong first step — a method you have not calibrated should
not be pointed at a disease model. It means the dispatch's goal is **two steps, not one**, and the
second has no object: no protocol, no spec, no candidate, no name. **Designing it is a governed
act that is not this session's** — it decides where blind readings land in the canonical pipeline,
which is `INTEGRAZIONE STRUTTURALE` (Plan, under a task) and `CANONICAL_BATCH_COMMIT`
(Orchestrator, under lease). Recorded as `Q-1` below.

---

## READINESS

### 14 · The seven preconditions, re-measured at this HEAD

The protocol's § 1 table is a snapshot dated 2026-08-18. Every row below was re-run this session.
**Four rows changed wording; none changed verdict.**

| # | Precondition | Measured 2026-08-22 at `9e10190` | State |
|---|---|---|---|
| P-1 | protocols canonical | both are **merged into `main`** and both still declare `status: PROPOSED — binding on canonical execution of CAND-20260818-SCIENTIST-AB-SPEC`. Merged ≠ binding | ❌ |
| P-2 | `scientist-a`/`-b` registered | `NOT_REGISTERED`, `ACTOR_ID UNRESOLVED`, worktrees 136 and 138 commits behind | ❌ |
| P-3 | capabilities `VERIFIED` at L2 | `0 of 27 declared` verified; all six Scientist capabilities `UNVERIFIED`; L2 **suspended** by the C-9 hold | ❌ |
| P-4 | `ORCHESTRATOR_LEASE` ACTIVE | `lease_state.py` → **`ACTIVE by derivation: 0`** (5 leases: 2 stale, 3 released) | ❌ |
| P-5 | C-2 preconditions declared | pending registration (P-2) | ❌ |
| P-6 | two Task Contracts issued | `ledger/tasks/` holds one directory, `plan/` — **no Scientist contract exists** (N-3) | ❌ |
| P-7 | surfaces built, manifest frozen | no surface anywhere; manifest `PREPARED — NOT FROZEN` (N-2) | ❌ |

**Zero of seven.** `BLIND FIRST PASS` is authorized only when every row reads satisfied *at the
moment of handover*.

### 15 · 🔴 A finding that is not in the § 1 table — the recorded scientist fingerprint no longer composes

Composed this session in this worktree:

```
python3 governance/scripts/governance_fingerprint.py compose --role scientist
scientist   b66959cd0bb7ccd5c410083fba0107da9157a2b6ddb68c3f86bdbefefc489d1a
```

That value matches **none** of the three the repository records:

| Value | Where recorded | Status |
|---|---|---|
| `ce3c0d94…` | `runtime/agent_card_registry.md` + inventory rows for a, b **and** c | **stale** |
| `355e3529…` | protocol § 9, composed at `BASE_HEAD` `cbce3016` | superseded |
| `82423a48…` | protocol § 9, predicted for the candidate's execution | not reached |
| **`b66959cd…`** | **composed here, 2026-08-22** | current |

**And the difference is not this branch.** All twelve inputs of the scientist set — `CORE`
(`GOVERNANCE_v3.1.1.md`, annexes A, B, H, J §§ J.0/J.2/J.3, `plan_defined_parameters.md`,
`roles/scientist.md`) plus annexes C, E, F — are **byte-identical to `main`**, confirmed two ways:
`git diff --stat main --` over all twelve returns empty, and a per-file SHA-256 comparison against
`main` returns `SAME` on each spot-checked file. So `b66959cd…` is `main`'s value too; the drift is
in the recorded photograph, not in this ref.

**Why it matters operationally.** H.2: *"mismatch su area → assegnazioni sospese."* A Task Contract
issued against the inventory's `ce3c0d94…` would be issued against a fingerprint that no longer
composes, and A.6's refusal rule would reject the resulting checkpoint. The registry file states
its own defence — *"a stale row is not authoritative"* (body § 43) — and `roles/scientist.md`
assigns the upkeep: **maintained_by: plan**. This is therefore an owed Plan action, and it is not
in the § 1 table because § 1 predates the drift.

### 16 · What is ready

Not nothing, and the distinction matters for sequencing:

- **the paper packet** — complete in the shared checkout, all 7 files present;
- **the instruction set** — 592 lines, canonical on `main`, read in full this session;
- **the evaluation population** — 65 units / 109 panels, computed by command, with its two
  structural bounding rules and its declared empty source;
- **the builder** — `build · verify · freeze · verify-freeze · population · locators ·
  tree-digest`, with `--post-read` as a distinct contract;
- **the output schema and the completion gate** — a machine verdict, not a self-report.

**Everything mechanical is ready. Everything authorizing is not.**

---

## BLOCKERS

### 17 · Ordered by dependency, each with the owner who can clear it — none of whom is this session

| # | Blocker | Clearing act | Owner |
|---|---|---|---|
| **B-1** | `CAND-20260818-SCIENTIST-AB-SPEC` has no approval line (N-4) | operator resolution appended to `HUMAN_APPROVAL_QUEUE.jsonl` | **operator** |
| **B-2** | both protocols and the role contract remain `PROPOSED` | follows from B-1 via `CANONICAL_BATCH_COMMIT` | Orchestrator, lease ACTIVE |
| **B-3** | L2 suspended by the C-9 hold; 0 of 27 capabilities verified | lift the hold, then run L2 | **operator**, then Orchestrator |
| **B-4** | `scientist-a`/`-b` unregistered; worktrees 136/138 commits behind | sync the worktrees, then I.2 step 7 registration | Orchestrator + the actors |
| **B-5** | no ACTIVE lease | take a lease | Orchestrator |
| **B-6** | no Task Contract for either Scientist | issue two, naming resolved `ACTOR_ID`s | Orchestrator, under lease |
| **B-7** | no surface built; manifest not frozen | `build` → `verify` → `freeze`, **after** B-1…B-6 | Plan, under a task |
| **B-8** | the recorded scientist fingerprint is stale (§ 15) | recompose and update the inventory row | **Plan** — owed, and independent of B-1 |

**B-1 is the root.** B-2 follows from it directly; B-4 and B-6 depend on the `ACTOR_ID`s that B-2
fixes. B-3 and B-5 are independent of B-1 and of each other. **B-8 is the only one clearable
today**, by the actor writing this record, under a task it does not currently hold.

🔴 **A sequencing constraint that will cost a run if it is missed.** Protocol § 9: canonical
execution of the candidate **rotates the scientist fingerprint**, and *"a checkpoint written
under the old value is `INCOMPATIBLE` (Annex A.6 refusal rule) the moment the spec becomes
canonical."* A benchmark started before B-2 would have to be abandoned or resumed under a
fingerprint it was not written under. **The rotation is confined to the scientist set** — plan,
mirror and orchestrator are byte-identical across the change — so the exposure is bounded to
exactly the readings in flight.

---

## OPEN_QUESTIONS

### 18 · Recorded, not resolved — each with a disposition owner who is not this session

| # | Question | Owner |
|---|---|---|
| **Q-1** | 🔴 **What is the configuration for a *real* reading?** Where does a blind reading land in `INGEST → DEEP_DIVE → COMMIT`; how is blindness preserved when the corpus must be reachable (§ 13); and does the receipt enter the hash-chained ledger? **No object on any ref answers any part of this** (N-1) | operator (strategy) → Plan (structure, under a task) |
| **Q-2** | Do the seven benchmark fields become canonical claim-registry fields, or stay benchmark-local? `OUTPUT_SCHEMA.md` § 3 defers it: *"whether any becomes canonical is a later governed decision"* | operator, on a Plan candidate |
| **Q-3** | Are `scientist-d`/`-e` **additional readers**, an **adjudication turn** (C.3 rotation — never a post), or **integrators** (unsupported; § 28 already allocates integration)? | operator |
| **Q-4** | What is `scientist-c`'s function, and when is its `ACTOR_ID` fixed? Registered but unused, while the two the benchmark needs are unregistered (§ 7) | operator + Orchestrator at registration |
| **Q-5** | Does the `OMISSION` asymmetry (§ 4, N-6) need a MODE A carrier, or is it correctly mode-specific? Affects only whether "missing evidence" can ever be a cross-mode dimension | Mirror (method), on a Plan note |
| **Q-6** | Is one paper × one session per actor enough, given § 0 caveat 1 says mode and session variance are not separable? A second paper is explicitly outside § 10 | operator, after the first outcome |

---

## VALIDATION

### 19 · Constraint compliance — checked, not asserted

| Constraint from the dispatch | Compliance |
|---|---|
| operate as Plan | ✅ — identity from repository evidence (§ 1), not from the `PROPOSED` contract |
| no authority from `PROPOSED` role contracts | ✅ — the one act performed traces to H.1 `WORK_COMMIT`; § 1 states this |
| use only H.1, annexes and decision records | ✅ — H.1 read in full; C.3, A.6, E.6, J.0, P2.1/P2.2, P5.1 cited; `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` read on `main` |
| do not create new roles | ✅ — none created; D/E reported as measured, not proposed |
| do not activate contracts | ✅ — no status line touched anywhere |
| do not modify `governance/` | ✅ — `git status` shows exactly one added file, under `learning/plan/` |
| artifacts only on own branch | ✅ — `plan-orchsurf-r4-transcription` |
| no automatic synthesis without evidence | ✅ — § 7 reports that synthesis is *unsupported* and that unresolved disagreement is a legitimate outcome under body § 27 |

### 19.1 · What this record does NOT do

It does not authorize, start, schedule or scope the benchmark · register or qualify any actor ·
verify a capability · lift the L2 hold · take a lease · issue a Task Contract · build, verify or
freeze a surface · update the runtime inventory or the Agent Card registry (B-8 is *reported*,
not performed) · create a field, schema, vocabulary or container · design the real-experiment
configuration Q-1 names · decide `scientist-c`'s function · propose `scientist-d` or `-e` ·
read the paper · form any scientific conclusion.

---

## NEXT_TRANSITION

The dispatch's question — *what is the minimum operating contract that lets Scientist A and B read
independently and reproducibly* — has a measured answer: **20 files per reader, 18 identical, 2
differing, with a machine gate at the end and 23 forbidden paths behind it.** It is built and it
is unauthorized.

The next transition is therefore **not** an artifact. It is **B-1** — an operator resolution on
`CAND-20260818-SCIENTIST-AB-SPEC` — after which B-2…B-7 run in the order § 17 gives, with the
fingerprint-rotation constraint of § 9 respected. **B-8 can be cleared before any of that**, by
Plan, under a task it does not hold today.

And beyond the first experiment, **Q-1 is the question that decides whether any of this ever
produces science.** BENCH-AB-001 calibrates the method and quarantines its own output by design.
Nothing in this repository yet says what a reading that is *meant to count* looks like.

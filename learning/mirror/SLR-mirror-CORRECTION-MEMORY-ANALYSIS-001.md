---
artifact: MIRROR observation record — whether a correction-memory layer can be represented from
  primitives that already exist, assessed by measurement. Learning artefact only
record_id: SLR-mirror-CORRECTION-MEMORY-ANALYSIS-001
actor_id: mirror
role: >
  mirror — metacognitive layer only (roles/mirror.md, "Mandate — three layers"). The governance
  layer and the hostile review layer are NOT engaged. This record issues no verdict, adjudicates
  nothing, and confirms nothing
date: 2026-08-22
task_id: LOOP_CORRECTION_MEMORY_ANALYSIS_v1
dispatcher: operator
iteration: 1/3
mode: READ_ONLY_ASSESSMENT + CREATE_OBSERVATION_ARTIFACT_ONLY
classification: OBSERVATION ONLY — not governance, not specification, not an implementation proposal
authority: >
  none. This record creates no rule, no vocabulary, no role, no validator, no ledger component, no
  ownership and no authority. Every line below is an observation and stays one
scope: >
  learning/mirror/ on branch `mirror` only. One new file. No governance/, roles/, framework/,
  ledger/ or reviews/ path is written. No existing record is edited, superseded, amended or
  deprecated
confirmation_class: >
  UNASSIGNABLE BY THE PRESCRIBED PROCEDURE, and that is itself Finding F-1. Annex E.2 requires the
  LEARNING_INDEX be consulted before a CONFIRMATION_CLASS is assigned. It does not exist
  (MEASURED_AT mirror@1892071e, 38 refs). Dedup was performed by grep over those 38 refs instead.
  On that substitute basis the class would read REPLICATION for §4 and §6, ORIGINAL_OBSERVATION for
  §5.3, §5.4 and F-7 — recorded as a description of what was done, not as a class assigned by the
  procedure the annex names
prior_artefact_disclosure: >
  🔴 MATERIAL, DECLARED BEFORE ANYTHING ELSE. Three repository objects already cover part of this
  ground, all authored by Mirror, all found by listing a directory rather than reported to me:
  learning/mirror/RETROSPECTIVE-ORCHSURF-R4-GOVERNED-TRANSCRIPTION.md § 3.E (848 lines),
  learning/mirror/SLR-mirror-0019.md § 3.1–3.7, and learning/mirror/SLR-mirror-0020.md § B-1–B-7.
  This record does NOT supersede, replace, amend or deprecate any of them, and could not. The
  overlap is mapped line-by-line in § 1.4. What is materially NEW is § 5.3 (two CORRECTION_MEMORY
  instances already materialized), § 5.4 (the detection-line census), and F-7 (the status register
  audited against its own tree)
naming_deviation: >
  DECLARED. 30 of the 33 records under learning/mirror/ match `SLR-mirror-NNNN[-ADD|-COR-NNN]`.
  This filename was specified by the dispatch and departs from that convention, as the three
  exceptions before it did. NO NAMING RULE IS ADOPTED AND NO PRECEDENT IS ESTABLISHED
vocabulary_note: >
  The task_id contains `LOOP`, which is external vocabulary — see § 2. It is reproduced here
  because it is the dispatch's identifier, not because the repository carries such an object
discipline: append-only · observation only · no remedy proposed and none may be read in
---

# CORRECTION MEMORY — an assessment of whether existing primitives already carry it

## 0 · Rehydration — identity from durable state, not from the dispatch

The dispatch asserted a role. It was not inherited. Every field below was re-derived in this
session from repository objects.

```
actor_id            mirror          ← roles/mirror.md frontmatter `actor_id: mirror`
worktree            <REPO_ROOT>/.claude/worktrees/mirror
                                    ← git worktree list; matches roles/mirror.md `worktree: mirror`
branch              mirror          ← git rev-parse --abbrev-ref HEAD
HEAD                1892071e86f6616400bc6e306f70cd192c479456
working tree        clean           ← git status --porcelain returned 0 lines
role_contract       roles/mirror.md · governance_version 3.1.1 · actor_class
                    PERSISTENT_LEGEND_ACTOR
contract status     🔴 `PROPOSED — binding once Mirror hostile review passes and the operator
                    approves`. The contract under which I act is NOT recorded as binding at this
                    ref. I act within it anyway, and record that its status is provisional
```

### Current authority surface, as the contract states it

```
HELD        metacognitive layer: learning clustering, ACTIVE_LESSONS selection within Plan's
            budget, dissent lifecycle, coordination review, autonomy ledger, review yield,
            retrospectives (roles/mirror.md, "Mandate — three layers")
            perimeter: MIRROR_REQUIRED includes "failure ricorrenti" (Annex G.1) — recurring
            failure is inside the mandate this task addresses
NOT HELD    command over any actor · production of primary evidence · self-approval of material
            change to Mirror's own review rubric, learning clustering, active-learning selection
            incl. budget, review-yield methodology, autonomy-classification methodology (Annex G.2)
🔴 BINDING ON THIS TASK
            A "correction-memory layer" is a learning-clustering and lesson-selection mechanism.
            Annex G.2 places exactly that class beyond Mirror's unilateral reach. The dispatch's
            prohibition on creating governance and the annex's prohibition therefore coincide;
            this record would have been observation-only under G.2 even had the dispatch not
            said so
```

---

## 1 · Surface map

### 1.1 · Measured ref and refs surveyed

```
MEASURED REF        refs/heads/mirror
HEAD                1892071e86f6616400bc6e306f70cd192c479456
MEASURED_AT         2026-08-22, this session, working tree clean
REFS PRESENT        48 total = 34 refs/heads + 4 refs/remotes + 5 refs/tags
                    + 4 refs/codex + 1 refs/stash
REFS TREE-SURVEYED  38 (refs/heads + refs/remotes), by `git ls-tree -r --name-only` per ref
NOT SURVEYED        refs/tags (5), refs/codex (4), refs/stash (1) — content not enumerated
VALIDITY            Every absence claim below holds for the 38 refs enumerated, at this instant,
                    in this clone. NOT_FOUND across 38 refs is not NOT_EXIST in a clone, a tag
                    tree or a remote I cannot see
```

> **A prior count differs, and the difference is not a defect.** The retrospective at this same
> HEAD records its measurements as "across all 46 refs"; I measure 48. Refs are mutable and the
> two measurements were taken at different instants. Recorded so that a later reader does not
> read the discrepancy as an error in either record. It does establish one thing: **a ref-count
> absence claim is valid only at its measured instant**, which is why MEASURED_AT is carried
> above rather than implied.

### 1.2 · Locations searched

```
governance/            all 12 files incl. body, ANNEX_INDEX, annexes A–J, candidates/,
                       design_records/, plan_defined_parameters.md, scripts/
roles/                 4 contracts
learning/              learning/mirror (33 files, this ref) — and, per ref, learning/plan,
                       learning/orchestrator
reviews/               reviews/mirror (49 files, this ref) — and, per ref, reviews/plan,
                       reviews/orchestrator
ledger/                approvals/, checkpoints/{plan,mirror}/, tasks/plan/
framework/scripts/     48 .py · scripts/ 35 .py · governance/scripts/ 2 .py  = 85 executable files
.claude/               settings.json (hooks), skills/, agents/
entrypoints            CLAUDE.md · BOOTSTRAP.md · ARCHITECTURE.md · README.md
```

### 1.3 · The learning corpus is partitioned by ref, and no ref holds it whole

```
MEASURED_AT   mirror@1892071e, 38 refs, git ls-tree per ref

refs/heads/mirror          learning/mirror  33   reviews/mirror  49
                           learning/plan     0   reviews/plan     0
refs/heads/main            learning/plan    10   reviews/plan     3
                           learning/mirror   0   reviews/mirror   0
refs/heads/orchestrator    learning/orchestrator 11   reviews/orchestrator 14
                           learning/plan     2

🔴 NO REF CONTAINS ALL THREE ACTORS' LEARNING. Not one Mirror learning or review record has
   reached `main`. From the branch on which Mirror's mandate is exercised, the Plan and
   Orchestrator learning corpora are invisible without an explicit cross-ref read
```

This is the condition under which every claim in this record was made, including its own dedup.

### 1.4 · Overlap with the three prior artefacts, mapped rather than hidden

```
§ 1.3 partition          OVERLAPS RETROSPECTIVE § 3.E.5 ("NO CONSOLIDATION SURFACE") and
                         SLR-0019 § 3.6. Re-measured independently here; counts differ from the
                         prior records because they were taken at a different instant
§ 3 memory surfaces      OVERLAPS RETROSPECTIVE § 3.E.1–E.3 and SLR-0019 § 3.1–3.3 for the three
                         absences (LEARNING_INDEX, ACTIVE_LESSONS, event ledger). Re-derived, not
                         copied. NEW here: the executable-coupling test (§ 3.5)
§ 4 failure classes      OVERLAPS RETROSPECTIVE § 3.A–3.E as source material. NEW here: the REUSE
                         column — whether a future agent reaches the lesson without being told
§ 5.1–5.2 field mapping  NEW. No object mapping CORRECTION_MEMORY's five fields onto named
                         repository primitives was found across 38 refs
§ 5.3 two instances       🔴 NEW AND MATERIAL. Two records already carrying the full proposed
                         field set were found in governance/design_records/. No prior artefact
                         cites them in this connection
§ 5.4 detection census    NEW. The 8 DETECTION lines had not been enumerated against the
                         availability of the instrument each routes to
§ 6 layer relation       PARTIALLY PRE-RESOLVED, which no prior learning record notes: an
                         adjudicated determination on A-vs-B already exists (§ 6.2)
F-7 register audit        🔴 NEW. Four Mirror records cite ANNEX_INDEX rows 64/65/75/76/77 as
                         evidence. None tested rows 71/72/73/78/79, which are refuted by the
                         same tree
```

---

## 2 · Dispatch validation — eight concepts against repository sources

Each term was tested against `governance/`, `roles/` and `framework/instruction/` at
`mirror@1892071e`.

| Concept | Repository source | Exact identifier | Status |
|---|---|---|---|
| **loop** | — | — | 🔴 **EXTERNAL VOCABULARY.** One occurrence of the string in `governance/`, inside `"EXCEPTION-ONLY HUMAN IN THE LOOP"` (`GOVERNANCE_v3.1.1.md:121`), an unrelated sense. No loop object, version, scope or cadence exists. Independently established already by three records (HANDOFF-v2:87, SLR-0019:314, SLR-0020:130) |
| **correction** | — | — | 🔴 **EXTERNAL VOCABULARY** as an object. Zero occurrences of `CORRECTION` as an identifier in `governance/`. It appears only as ordinary prose ("correction applied") and as the `-COR-NNN` filename suffix, which is a record-amendment convention, not an object class |
| **learning record** | Annex E.6; body §15 | `Session Learning Record`; outcomes `MICRO_UPGRADE \| BEST_PRACTICE_CANDIDATE \| FAILURE_PATTERN \| MACRO_UPGRADE_CANDIDATE \| NO_NEW_LEARNING` | **NORMATIVE, INSTANTIATED.** 33 records at this ref |
| **retrospective** | Annex G.3 | `MIRROR_RETROSPECTIVE ogni N batch` | **NORMATIVE, CADENCE UNSET.** `N` unassigned (`ANNEX_INDEX.md:65` → UNASSIGNED). 1 artefact exists, produced ad hoc |
| **handoff** | Annex B.1 | `HANDOFF`, a message type in the enumeration at `annex_b_message_protocol.md:28` | **NORMATIVE as a MESSAGE TYPE.** 🔴 Not a persistence class. The two `HANDOFF-*` files under `learning/mirror/` are durable records bearing a message-type name — a use the annex does not define |
| **lesson** | Annex E.5 | `ACTIVE_LESSONS`, role-specific subsets, budget P6 | **NORMATIVE, NOT MATERIALIZED.** 0 objects across 38 refs |
| **failure mode** | body §40 (normative for the whole specification); Annex J.0 | `FAILURE_MODE_STILL_POSSIBLE`, within `GUARANTEE_PROVIDED / FAILURE_MODE_STILL_POSSIBLE / DETECTION / RECOVERY` | **NORMATIVE AND MANDATORY.** body:40 — every coordination mechanism MUST declare the four. Also `FAILURE_PATTERN` as an SLR outcome (body §15) |
| **workflow rule** | — | — | 🔴 **EXTERNAL VOCABULARY.** Zero occurrences of `WORKFLOW_RULE` or "workflow rule" in `governance/`, `roles/` or `framework/instruction/`. The nearest named field is `AFFECTED_WORKFLOW` (Annex E.2), which denotes a surface, not a rule |

**Four of eight terms in the dispatch are external vocabulary**, including the two that name the
task itself. Recorded, not corrected — renaming is not this record's to do.

---

## 3 · Current memory surfaces — four, measured, and not equivalent

### 3.1 · A · Session Learning Records — `learning/`

```
NORMATIVE SOURCE  Annex E.6 (field set) · body §15 (mandatory outcome enum) · body §18 (durable
                  persistence via WORK_COMMIT or inclusion in the next candidate)
MEASURED          33 files at learning/mirror @1892071e — 30 SLR-*, 2 HANDOFF-*, 1 RETROSPECTIVE-*
CONFORMANCE       body §15 enum usage:  FAILURE_PATTERN 13/33 · BEST_PRACTICE_CANDIDATE 10/33 ·
                                        MICRO_UPGRADE 8/33 · MACRO_UPGRADE_CANDIDATE 0 ·
                                        NO_NEW_LEARNING 0
                  Annex E.2 fields:     confirmation_class 10/33 · LEARNING_ID 7/33 (+6 lowercase)
                                        · 🔴 AFFECTED_WORKFLOW 3/33
INDEX             none. Annex E.2 specifies LEARNING_INDEX; 0 objects across 38 refs
```

### 3.2 · B · Reviews — `reviews/`

```
NORMATIVE SOURCE  Annex C.2 (single review format: STEELMAN before objections,
                  WHAT_WOULD_CHANGE_MY_MIND as a declared falsifier) · Annex C.1 (ladder + floors)
MEASURED          49 files at reviews/mirror @1892071e
NOT ALL ARE REVIEWS  the directory also holds 3 OBS-* observation records, 1 CLASS-*
                  determination, 1 DECISION-PACKAGE-*, 2 L2-OUTCOME-*, 3 OWED-*, 1 ACK-*
BINDING PROPERTY  a review cites the CANDIDATE_CONTENT_HASH it judged — the record is bound to an
                  immutable object identity. No learning record carries such a binding
```

### 3.3 · C · Governance decisions — `governance/candidates/`, `design_records/`, `ledger/approvals/`

```
MEASURED   3 candidates · 4 design_records · 6 lines in ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl
CONTAINS   the only two fully-fielded E.3 provisional practices in the repository (§ 5.3)
```

### 3.4 · D · Runtime checks — executable

```
MEASURED   85 .py across framework/scripts (48), scripts (35), governance/scripts (2)
HOOKS      .claude/settings.json declares exactly one: a PreToolUse Bash guard
           (scripts/guard_bash_command.py). No SessionStart hook exists
```

### 3.5 · 🔴 The four are not coupled — measured, with a positive control

The question that decides whether any of A/B/C constitutes *memory* rather than *record* is
whether anything causes a later agent to encounter it. This was tested, not assumed.

```
TEST 1  Does any of the 85 executable files read learning/, reviews/, or an SLR?
        grep -rl 'learning'   --include='*.py'  → 0 files
        grep -rl 'reviews/|SLR-' --include='*.py' → 0 files
        POSITIVE CONTROL: grep -c 'def ' framework/scripts/legend_lint.py → 26
        The instrument was working. The negative is a measurement, not a silence

TEST 2  Does any entrypoint route a reader to the corpus?
        CLAUDE.md · BOOTSTRAP.md · ARCHITECTURE.md · README.md
        → exactly ONE reference exists, CLAUDE.md:59:
          | Active lessons for your role, once operative | `active_lessons/` — not yet materialized |
        🔴 The single pointer in the router loaded every session points at a path that does not
           exist (0 objects, 38 refs), and does not mention learning/ or reviews/, where all 82
           records at this ref actually live

TEST 3  Is there a hook that surfaces learning at session start?
        .claude/settings.json → one PreToolUse Bash guard. No SessionStart. → none
```

**Observation.** At `mirror@1892071e` the learning layer has **zero executable coupling and one
broken documentary pointer**. A future agent reaches these 82 records by listing a directory it
was never told about. This is the measurement behind every `REUSE` cell in § 4.

---

## 4 · Observed failure classes

Six classes, each anchored to a repository object. `PERSISTENCE` names where the lesson is stored;
`REUSE` answers only the mechanical question — *would a future agent encounter this without being
told?* — and is answered from § 3.5.

### 4.1 · FC-1 · False-negative measurement

```
FAILURE_CLASS  A search instrument returned a negative that was accepted as an absence
DETECTION      direct recall by the same actor, not by any instrument
               (learning/mirror/SLR-mirror-0017.md:37, headed `FAILURE_PATTERN`)
PERSISTENCE    SLR-mirror-0017 § 1 (learning/) AND, separately, as a fielded practice
               PROV-POSITIVE-CONTROL-BEFORE-NEGATIVE-FINDING
               (governance/design_records/materialization_log.md:1026)
REUSE          🔴 NO by mechanism. The practice is registered in a design record that no script
               reads and no entrypoint cites. It reached this session only because I read the
               file. I applied the control in TEST 1 above before knowing the record existed —
               convergence, not transmission
```

### 4.2 · FC-2 · Ancestor-relative diff hiding loss across branches

```
FAILURE_CLASS  a file diffed against the common ancestor rather than the target branch, hiding a
               class of silent loss
DETECTION      Mirror hostile review of the candidate (REV-GOV311-MIRROR-002:224 records the
               withdrawal as CONFIRMED)
PERSISTENCE    PROV-DIFF-AGAINST-TARGET (materialization_log.md:647), full E.3 field set;
               cross-referenced from CAND-20260816-GOV311.md:165 (PID-17)
REUSE          🔴 NO by mechanism, and BLOCKED at lifecycle. EXPIRY is "at Mirror's first
               coordination review". MEASURED: 0 coordination-review artefacts across 38 refs.
               The practice cannot be promoted, rejected or extended, because the event its
               expiry names has never occurred
```

### 4.3 · FC-3 · Stale register — a status surface refuted by its own tree

```
FAILURE_CLASS  the repository's only materialization status register asserts states its own tree
               contradicts at the identical ref
DETECTION      🔴 NOT PREVIOUSLY DETECTED. Found in this session by testing every row of
               governance/ANNEX_INDEX.md § "Downstream artifacts" against HEAD:<path>
MEASURED_AT    mirror@1892071e — 9 of 10 rows tested
               REFUTED (4 rows marked `pending`, artefact present at same ref):
                 :71 /roles/*.md         → 4 contracts exist
                 :72 /BOOTSTRAP.md       → exists
                 :73 deployment/deployment_profile.md → exists
                 :78 Fingerprint composition script  → governance/scripts/governance_fingerprint.py
                     exists — and row :57 of the SAME FILE already states it is "executable".
                     🔴 The file contradicts itself across two tables
               GROUND REFUTED (1 row marked `held`):
                 :79 root CLAUDE.md router — held because "the current root CLAUDE.md is the
                     load-bearing scientific core". HEAD:CLAUDE.md line 1 reads
                     "# CLAUDE.md — LEGEND router" and states it became one on 2026-08-16
               CONFIRMED TRUE (4 rows): :74 runtime inventory · :75 LEARNING_INDEX ·
                 :76 ACTIVE_LESSONS · :77 event ledger — all 0 objects across 38 refs
               NOT TESTED (1 row): :80 first INTEGRATION_CANDIDATE
PERSISTENCE    nowhere before this record
REUSE          🔴 NO — and the class is self-aggravating. Four Mirror records
               (HANDOFF-v2, RETROSPECTIVE § 3.E, SLR-0019, SLR-0020) cite rows 64/65/75/76/77 of
               this register as evidence. Those five rows are true. None of the four tested the
               other rows. The register was used as an instrument and never calibrated
```

### 4.4 · FC-4 · Surface ambiguity — a claim true on one ref, false on another

```
FAILURE_CLASS  an absence or presence asserted without naming the ref it was measured on
DETECTION      Mirror review, which introduced the discipline explicitly
               (reviews/mirror/REV-ORCH-STATE-RECONSTRUCTION-001.md:126–129, carrying
               MEASURED_AT and "NOT_FOUND on 42 refs is not NOT_EXIST in a clone I cannot see")
PERSISTENCE    reviews/ (control plane) — NOT in learning/, and NOT as a fielded practice
REUSE          🟡 PARTIAL, AND THE CHANNEL IS HUMAN. The dispatch that commissioned THIS task
               carries the rule near-verbatim: "NOT_FOUND locally is not NOT_EXIST repository-
               wide", with a required MEASURED_AT block. The review was written 2026-08-22; the
               dispatch arrived the same day
               🔴 This is the single measured instance of a lesson propagating into later work,
               and it propagated through the operator writing it into a dispatch — not through
               any repository mechanism. It is evidence that transmission works, and evidence
               that the working channel is not durable
```

### 4.5 · FC-5 · Vocabulary contamination — dispatch terms entering durable records

```
FAILURE_CLASS  terms with no repository referent are carried from dispatch text into committed
               artefacts, where later readers may mistake them for objects
DETECTION      Mirror, repeatedly and pre-emptively — each occurrence declared at the point of use
               (SLR-0019:314, SLR-0020:130, HANDOFF-v2:87, RETROSPECTIVE § 5 preamble)
PERSISTENCE    learning/ — as a declaration inside each affected record, never as an index entry
REUSE          🟡 PARTIAL. The habit is visibly transmitted between Mirror records, which cite
               one another. It rests on the author having read the earlier records; nothing
               enforces or surfaces it. This record carries `LOOP` in its own task_id for the
               same reason, declared in frontmatter
```

### 4.6 · FC-6 · Mutually-blocking infrastructure absence

```
FAILURE_CLASS  four specified artefacts, each individually `pending` and individually harmless,
               that jointly remove the analysis surface the metacognitive role is defined on —
               and each of whose natural remedy is barred to a different actor
DETECTION      Mirror, by reading the specification against the tree
               (RETROSPECTIVE § 3.E; independently re-derived SLR-0019 § 3.5)
PERSISTENCE    learning/ (3 records) + governance/ANNEX_INDEX.md rows 64,65,75,76,77
REUSE          🔴 NO by mechanism — and § 5.4 measures the consequence: the detection lines that
               would surface a recurrence route to instruments in this same blocked set
```

---

## 5 · CORRECTION_MEMORY — assessment of the definition against existing primitives

> The definition under test, reproduced from the dispatch: *a durable observation generated after
> a completed loop, containing failure pattern, detection method, prevention rule, affected
> workflow surface, and confidence/evidence level.* **No such object is created here.**

### 5.1 · Every one of the five fields already has a named normative primitive

```
FIELD 1 · failure pattern
  FAILURE_MODE_STILL_POSSIBLE   body §40 — mandatory for every coordination mechanism in the spec
  FAILURE_PATTERN               body §15 — an enumerated Session Learning Review outcome
  OBSERVED_FAILURE              Annex G.2 — first field of MIRROR_UPGRADE_PROPOSAL

FIELD 2 · detection method
  DETECTION                     body §40 — mandatory, spec-wide. 8 instances in governance/
  EVIDENCE_EXPECTED             Annex E.3 — what would confirm the practice

FIELD 3 · prevention rule
  RECOVERY                      body §40 — mandatory, spec-wide
  HYPOTHESIS                    Annex E.3 — the practice itself, stated as a testable rule
  PROPOSED_RULE                 Annex G.2

FIELD 4 · affected workflow surface
  AFFECTED_WORKFLOW             Annex E.2 — a named LEARNING_INDEX field
  APPLIES_TO                    Annex E.3
  SCOPE                         Annex E.2, Annex G.2

FIELD 5 · confidence / evidence level
  EVIDENCE_COUNT                Annex E.2
  CONFIRMATION_CLASSES          Annex E.2 — {actor, session, class}, class ∈ ORIGINAL_OBSERVATION
                                | REPLICATION | EXPOSURE_AFTER_BROADCAST; only the first two count
                                fully; BEST_PRACTICE_CANDIDATE threshold ≥2, or 1 + Mirror validation
  STATUS                        Annex E.1 state machine: OBSERVED → LOCAL → PROVISIONAL →
                                VALIDATING → PROMOTED | REJECTED | SUPERSEDED | EXPIRED
  SUCCESS_CRITERION /
  FAILURE_CRITERION / EXPIRY    Annex E.3
```

**Observation.** The five fields are not merely supported; each is named in frozen normative text,
and two of them (`DETECTION`, `RECOVERY`) are already **mandatory for every coordination mechanism
in the specification** under body §40. The proposed object introduces no field the specification
lacks.

### 5.2 · What is absent is not the schema but the index

```
SCHEMA        present, three times over (E.2 index entry · E.3 practice · G.2 proposal)
CONTENT       present at scale — FAILURE_PATTERN appears in 13 of 33 learning records
KEY           🔴 AFFECTED_WORKFLOW, the field that would make a lesson retrievable by the surface
              it applies to, appears in 3 of 33
INDEX         🔴 absent — LEARNING_INDEX, 0 objects, 38 refs, MEASURED_AT mirror@1892071e
COMPRESSION   🔴 absent — ACTIVE_LESSONS, 0 objects, 38 refs
COUPLING      🔴 absent — 0 of 85 executable files read the corpus (§ 3.5)
```

### 5.3 · 🔴 Two objects matching the full proposed field set already exist

This is the material finding of this record. The dispatch asks whether primitives *support* the
object. They do more than support it: **the object has been instantiated twice**, under Annex E.3,
by Plan, in `governance/design_records/materialization_log.md`.

```
PRACTICE_ID:        PROV-DIFF-AGAINST-TARGET                        (materialization_log.md:647)
PRACTICE_ID:        PROV-POSITIVE-CONTROL-BEFORE-NEGATIVE-FINDING   (materialization_log.md:1026)
```

Mapped against the definition under test:

| CORRECTION_MEMORY field | Field present in both records |
|---|---|
| failure pattern | the originating defect, narrated + `ORIGIN_ACTOR` with a review anchor (`observed in REV-GOV311-MIRROR-001 §1.2`) |
| detection method | `EVIDENCE_EXPECTED` — the observation that would signal recurrence |
| prevention rule | `HYPOTHESIS` — the rule, stated so it can fail |
| affected workflow surface | `APPLIES_TO` |
| confidence / evidence level | `STATUS: PROVISIONAL` + `SUCCESS_CRITERION` + `FAILURE_CRITERION`, with the E.2 threshold reasoning stated inline: *"a single ORIGINAL_OBSERVATION without a second confirmation or Mirror validation is below the BEST_PRACTICE_CANDIDATE threshold"* |
| — additionally | `EXPIRY`, `ROLLBACK`, `STARTED` — three fields the proposed definition does not carry |

**Three observations follow, all measured.**

```
(1) LOCATION      Both live in governance/design_records/ — layer C — not in learning/. The
                  correction memory that exists is stored outside the learning namespace
(2) CARDINALITY   5 PROV-* identifiers exist repository-wide; only these 2 carry the full E.3
                  field set. The other 3 (PROV-ACK-TIMEOUT-30M, PROV-HEARTBEAT-30M-3X,
                  PROV-LESSON-BUDGET-25) are parameter values in plan_defined_parameters.md
(3) 🔴 LIFECYCLE  BOTH expire "at Mirror's first coordination review".
                  MEASURED: 0 coordination-review artefacts across 38 refs; the cadence governing
                  it ("ogni N batch", Annex G.3) has N unassigned (ANNEX_INDEX.md:65), and Annex
                  G.2 bars Mirror from setting it alone.
                  Annex E.3 states: "Mai provisional per sempre." Two practices are held
                  indefinitely provisional by an expiry condition anchored to an event that has
                  never occurred and that no single actor is permitted to schedule
```

The circularity the retrospective measured for `PROV-LESSON-BUDGET-25` is therefore **not
isolated**: it is the shared shape of every fully-fielded correction memory in the repository.

### 5.4 · The detection half of the object routes to instruments that do not exist

Body §40 makes `DETECTION` mandatory spec-wide. All 8 instances in `governance/` were enumerated
and classified by whether the instrument each names is available at this ref.

```
MEASURED_AT  mirror@1892071e

MECHANICAL — fires at a write, a gate, or a timeout. AVAILABLE (3 of 8)
  annex_a:49   second claim on same TASK_ID+GENERATION → CLAIM_CONFLICT at write
  annex_b:41   HEARTBEAT + absence of TASK_CLAIM/STATUS within window; MESSAGE_ID dedups
  annex_i:56   double record on the same succession → at write; GATE 0 blocks batches

ROUTED TO A MIRROR INSTRUMENT (5 of 8)
  annex_a:88   "Mirror monitora il tasso di invalidazioni"   → requires event ledger  🔴 absent
  annex_a:104  "Mirror osserva il rapporto rifatto/totale"   → requires event ledger  🔴 absent
  annex_e:52   "errori ripetuti su pattern già appresi (Mirror retrospettive)"
                                                             → cadence N unassigned   🔴
  annex_j:58   "aperture senza chiusura oltre soglia → Mirror retrospettive"
                                                             → ledger + cadence       🔴
  annex_i:73   "fallimenti ripetuti sullo stesso tipo di task → Mirror coordination review"
                                                             → 0 artefacts, 38 refs   🔴
```

**Observation, stated as narrowly as the measurement permits.** Five of the eight detection
mechanisms the frozen specification declares are routed to Mirror instruments that are not
materialized at this ref. The three that are available are precisely those that fire at an
executable moment — a write, a gate, a timeout. **`annex_e:52` and `annex_i:73` are the two lines
that would detect a *recurring* failure**, which is the condition Annex G.1 names as
`MIRROR_REQUIRED`; both route to instruments that have never run.

### 5.5 · Assessment, stated as an assessment and nothing else

```
Q  Do repository primitives support a CORRECTION_MEMORY object as defined?
A  YES for the schema — all five fields are named in frozen normative text (§ 5.1), and two
   complete instances already exist (§ 5.3)
A  NO for retrieval — no index, no compression stage, no executable coupling, and a router
   pointer to an empty path (§ 3.5, § 5.2)
A  NO for lifecycle closure — both existing instances are blocked at an expiry condition that
   cannot be reached by any single actor (§ 5.3.3)
A  NO for detection — 5 of 8 declared detection routes lead to unmaterialized instruments,
   including both routes that fire on recurrence (§ 5.4)

CONSEQUENCE, OBSERVED NOT PRESCRIBED
   The gap this record measures is not a missing object class. It is that the object which
   already exists is unindexed, stored outside the namespace that names it, uncoupled to
   anything executable, and unable to leave the PROVISIONAL state
```

---

## 6 · Relation between the four layers — evidence, not resolution

The dispatch asks whether A (Session Learning Records), B (Reviews), C (Governance decisions) and
D (Runtime checks) are distinct memory layers or duplicates, and instructs that this not be
resolved. Evidence follows.

### 6.1 · Measured distinctions

| | A · learning/ | B · reviews/ | C · governance decisions | D · runtime checks |
|---|---|---|---|---|
| normative source | Annex E.6, body §15 | Annex C.1–C.2 | Annex D.2, J.3, E.3 | body §40 DETECTION |
| unit | a session | a candidate hash | a decision | an invocation |
| bound to | nothing immutable | `CANDIDATE_CONTENT_HASH` | `APPROVAL_ID` / candidate hash | exit status |
| count @1892071e | 33 | 49 | 3 + 4 + 6 | 85 files |
| retrievable by index | 🔴 no | 🔴 no | partial (queue is JSONL) | n/a |
| read by any script | 🔴 no | 🔴 no | 🔴 no | self |
| can fire unprompted | no | no | no | ✅ yes |

### 6.2 · 🔴 A-vs-B is not an open question — it was adjudicated

No prior learning record notes this. `reviews/mirror/CLASS-P51-REVIEWS-LEARNING-001.md` is a
`CHANGE_CLASS` determination, reviewed by Mirror and **adjudicated by the operator on 2026-08-17**:

```
DETERMINATION
  reviews/    (A) CONTROL PLANE   — by P5.1's definition, and because gate 5 is otherwise
                                    unsatisfiable for any candidate sharing a tree with it
  learning/   (B) CONTENT DOMAIN  — body §18 names a candidate as a durable home for it
  CHANGE_CLASS  MAJOR
  URGENCY       latent, not live
```

The reasoning is a fixed-point argument, not a preference: a review is bound to the hash of the
candidate it judges, so if reviews sat inside the hashed content tree, writing the review would
change the identity of the reviewed object and Gate 5 could never be satisfied. A learning record
asserts nothing about a candidate's identity, so its inclusion changing a hash is correct rather
than pathological.

**They are therefore formally different planes, on a stated ground, already decided.**

### 6.3 · And the decision has not propagated — measured

```
REQUIRED BY THE DETERMINATION (§7 of that record)
  "P5.1 CONTROL_PLANE_ROOTS must select the set its own definition describes. Under this
   determination reviews/ belongs in that set and learning/ does not"

MEASURED AT mirror@1892071e — governance/plan_defined_parameters.md:250
  CONTROL_PLANE_ROOTS:
  - governance/candidates/
  - ledger/

🔴 reviews/ is absent. Five days after an operator-adjudicated MAJOR determination, the parameter
   it names is unchanged
```

This is layer C exhibiting the same property § 3.5 measured for layers A and B: **a durable,
correct, adjudicated record that has not altered the system it describes.** Recorded as evidence
for the dispatch's question; whether it should have propagated, and by whom, is not this record's
to say. The determination itself declares the urgency "latent, not live" and assigns the shape of
the resolution to Plan and the operator.

### 6.4 · The duplication question, answered only where measurement reaches

```
DISTINCT     A and B, by adjudicated determination on a fixed-point ground (§ 6.2)
DISTINCT     D from A/B/C — D is the only layer that fires without being read (§ 6.1)
🔴 OVERLAPPING IN PRACTICE, boundary not adjudicated:
             layer C holds the only two fully-fielded correction memories (§ 5.3), a content
             shape that Annex E.6 and E.2 place in layer A
             layer B holds 11 of 49 records that are not reviews — OBS-*, CLASS-*, OWED-*,
             DECISION-PACKAGE-*, L2-OUTCOME-*, ACK-*
             FC-4, the one lesson measured to have propagated, persists in layer B and never
             entered layer A
NOT RESOLVED HERE, by instruction and by Annex G.2
```

---

## 7 · Minimum viable future mechanism — questions only

> 🔴 **THIS SECTION PROPOSES NOTHING.** It contains no recommendation, no design, no ownership and
> no route. Each item is stated as a question because each is, by Annex G.2, outside Mirror's
> unilateral reach. No actor may cite this section as authority for any change.

**Information a future mechanism would require, that is not currently captured anywhere**

```
— the ref at which a lesson was measured. 0 of 33 learning records carry a machine-readable
  MEASURED_AT field; the discipline exists only in prose (§ 4.4)
— AFFECTED_WORKFLOW, present in 3 of 33 (§ 5.2). Without it, retrieval by surface is not possible
  even if an index existed
— a link from a failure to the check that would catch it. FC-1's practice and TEST 1's positive
  control coincide with no pointer between them
```

**Ownership questions the repository leaves open**

```
— Annex E.2 splits LEARNING_INDEX: "durevolezza: Plan; cura epistemica: Mirror". Which of the two
  creates the first entry is not stated, and ANNEX_INDEX.md:75 has carried it as pending throughout
— layer C holds correction memories (§ 5.3) authored by Plan; Annex E.6 assigns learning records
  to each actor. Which actor owns a correction memory arising from another actor's failure is
  not addressed
— reviews/ contains 11 non-review records (§ 6.4). No annex states which namespace an observation
  that is neither a review nor a session record belongs to
```

**Missing governance decisions on which the above depend**

```
— MIRROR_RETROSPECTIVE cadence N: UNASSIGNED (ANNEX_INDEX.md:65). Recorded as
  CARRIED_UNRESOLVED by explicit operator decision (APPROVAL-GOV311-DEVIATIONS.md §ESC-3).
  Annex G.2 bars Mirror from setting it
— the event-ledger writer: design chosen (option (a), per-actor JSONL consolidated by Plan);
  writer and validator not built (ANNEX_INDEX.md:64)
— CONTROL_PLANE_ROOTS: an adjudicated MAJOR determination requires reviews/ be added; unchanged
  at this ref (§ 6.3)
```

**Possible conflicts a future mechanism would meet**

```
— 🔴 Annex G.2 vs the mechanism itself. Any correction-memory layer is learning clustering and
  lesson selection. Mirror may not self-approve material change to either. An index proposed by
  Mirror requires: proposal → Plan candidate → independent reviewer chosen by Orchestrator →
  validation; and, if it touches governance, the operator
— 🔴 the expiry deadlock (§ 5.3.3). Any new provisional practice adopting the existing E.3
  template would inherit the same unreachable expiry, and Annex E.3's "Mai provisional per
  sempre" would be defeated on arrival rather than over time
— 🔴 the register (§ 4.3, FC-3). A mechanism that read ANNEX_INDEX to learn what is missing would,
  at this ref, be told that four existing artefacts do not exist
— body §18 vs storage location. A learning record's durable home may be a candidate; correction
  memories currently sit in design_records/, which is provenance rather than runtime law
```

---

## 8 · NOT_ESTABLISHED

```
NOT ESTABLISHED   that any correction-memory layer should be built. This record assesses
                  representability and says nothing about desirability
NOT ESTABLISHED   that the absences measured are defects. Each is declared pending or unresolved
                  by a governed act; FC-3 measures the register's accuracy, not anyone's diligence
NOT ESTABLISHED   any cadence, owner, index, schema, vocabulary, route, validator or authority
NOT ESTABLISHED   that A/B/C/D should be merged or separated further than § 6.2 already decided
NOT ESTABLISHED   the content of the 5 tags, 4 codex refs and 1 stash ref not tree-surveyed (§ 1.1)
NOT ESTABLISHED   ANNEX_INDEX.md:80 (first INTEGRATION_CANDIDATE) — the one row not tested
NOT ESTABLISHED   that FC-4's propagation was caused by the review. The review and the dispatch
                  share a date and near-verbatim wording; a common author is not excluded, and
                  causation is not measurable from here
NOT ESTABLISHED   that this record's own confirmation class is correct — the procedure Annex E.2
                  prescribes for assigning it was unavailable (frontmatter)
```

---

## 9 · Evidence — every object this record depends on

```
IDENTITY
  roles/mirror.md                                    contract, status PROPOSED
  git rev-parse HEAD                                 1892071e86f6616400bc6e306f70cd192c479456
  git worktree list · git status --porcelain         17 worktrees · clean

NORMATIVE
  governance/GOVERNANCE_v3.1.1.md                    :40 (G/F/D/R mandatory) · :121 (LOOP) ·
                                                     :266 (§15 outcome enum) · :278 (§18 durable)
  governance/annex_e_learning_lifecycle.md           E.1–E.6
  governance/annex_g_mirror.md                       G.1 perimeter · G.2 self-upgrade bar · G.3
  governance/annex_j_runtime_control_plane.md        J.0 · J.1 event ledger · J.3
  governance/annex_a_task_contract.md                :49 :88 :104 (DETECTION)
  governance/annex_b_message_protocol.md             :28 (HANDOFF) · :41 (DETECTION)
  governance/annex_i_bootstrap_deployment.md         :56 :73 (DETECTION)
  governance/ANNEX_INDEX.md                          :57 · :64 :65 · :71–:80
  governance/plan_defined_parameters.md              :250 CONTROL_PLANE_ROOTS

CORRECTION MEMORIES ALREADY MATERIALIZED
  governance/design_records/materialization_log.md   :647  PROV-DIFF-AGAINST-TARGET
                                                     :1026 PROV-POSITIVE-CONTROL-BEFORE-NEGATIVE-FINDING
  governance/candidates/CAND-20260816-GOV311.md      :165 PID-17

ADJUDICATED DETERMINATION
  reviews/mirror/CLASS-P51-REVIEWS-LEARNING-001.md   §2 §3 §7 + determination block

PRIOR ARTEFACTS (overlap mapped § 1.4)
  learning/mirror/RETROSPECTIVE-ORCHSURF-R4-GOVERNED-TRANSCRIPTION.md   § 3.E, 848 lines
  learning/mirror/SLR-mirror-0019.md · SLR-mirror-0020.md · HANDOFF-MIRROR-PERSISTENCE-AND-HANDOFF-v2.md
  learning/mirror/SLR-mirror-0017.md                 :37 FAILURE_PATTERN
  reviews/mirror/REV-ORCH-STATE-RECONSTRUCTION-001.md :126–129 MEASURED_AT / NOT_FOUND≠NOT_EXIST
  reviews/mirror/REV-GOV311-MIRROR-002.md            :224

MEASUREMENTS PERFORMED THIS SESSION
  38-ref tree survey (git ls-tree per ref)           learning/, reviews/, ledger/, active_lessons/
  85-file executable coupling test, with positive control (grep -c 'def ' → 26)
  4-entrypoint pointer test                          CLAUDE.md :59 only
  ANNEX_INDEX row-by-row test against HEAD:<path>    9 of 10 rows
  body §15 enum + Annex E.2 field census over 33 learning records
  8-line DETECTION census with instrument availability
```

---

## 10 · Standing at the instant this record was written

```
This record creates nothing. It adds one file under learning/mirror/ on branch `mirror`.
No governance file, role contract, framework file, ledger component or prior artefact was
modified, and none may be modified on its authority, which is none.

The object the dispatch asked me to assess exists already, twice, in a directory the learning
layer does not name, held provisional by an event that has never happened.

Iteration 1 of 3.
```

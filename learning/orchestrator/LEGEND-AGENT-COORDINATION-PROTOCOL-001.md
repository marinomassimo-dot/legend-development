---
artifact: PROTOCOL ANALYSIS — the minimum coordination surface between human-routed and
  agent-coordinated work, assessed against measured repository state
record_id: LEGEND-AGENT-COORDINATION-PROTOCOL-001
task_id: LEGEND_AGENT_COORDINATION_PROTOCOL_v0.1
iteration: 1/3
dispatcher: operator
date: 2026-08-22
author_session: root checkout at analysis; artifact written on branch
  `orch-agent-coordination-protocol`, based on `main` @ 788c357
actor_id: NOT ESTABLISHED — see § IDENTITY. This record is not authored under a role contract.
governance_version: 3.1.1 (read, not exercised)
classification:
  - PROTOCOL ANALYSIS ONLY
  - NOT GOVERNANCE
  - NOT ACTIVATION
  - NOT IMPLEMENTATION
authority_claimed: none
domain: >
  CONTENT. CONTROL_PLANE_ROOTS at `main` @ 788c357 are exhaustively `governance/candidates/`,
  `ledger/` and `reviews/` — measured in this session at
  `governance/plan_defined_parameters.md:258–262`. `learning/` is not among them, so this record
  sits inside the CANDIDATE_CONTENT_HASH of any future candidate that re-aligns onto the branch
  carrying it.
not_an_slr: >
  This is NOT a Session Learning Record. Annex E.6 governs those. The name is deliberately not
  `SLR-`, following the precedent set at this seat by SCIENTIFIC-PIPELINE-PREPARATION-001 and
  ORCHESTRATOR-SCIENTIFIC-PIPELINE-AND-LOOP-ARCHITECTURE-ANALYSIS-001.
branch_rationale: >
  H.1 confines `WORK_COMMIT` to "ogni attore, solo proprio branch", and the only row that
  authorizes writing the trunk — `CANONICAL_BATCH_COMMIT` — requires an ACTIVE lease, of which
  there are zero. A session that cannot establish an ACTOR_ID has no "own branch" either, so
  neither reading clearly permits advancing `main`. Choosing the reading that advances `main`
  would be the convenient one. This record therefore lands on its own branch and pays the
  fragmentation cost it documents in F-3. Merging it is available to whoever holds that
  authority; this record does not perform, request or schedule a merge.
corrects: >
  Two measurements in ORCHESTRATOR-SCIENTIFIC-PIPELINE-AND-LOOP-ARCHITECTURE-ANALYSIS-001
  (branch `orch-pipeline-loop-architecture` @ d6d46f8) — its N-4 and its § 2.4 checkpoint row.
  See F-1. Neither correction is an amendment: that record is not edited, and both corrections
  are recorded here as new measurements taken at the same ref and HEAD it declared.
---

# LEGEND AGENT COORDINATION PROTOCOL — ANALYSIS 001

> **PROTOCOL ANALYSIS ONLY.** Nothing here adopts a protocol, defines a rule, creates a task,
> assigns an actor, activates a contract, resolves a finding, confers authority, or recommends a
> course of action. It describes what the repository has, what it does not have, and what the
> difference implies for the transition the dispatch names.

---

## TASK_STATUS

```
TASK_ID        LEGEND_AGENT_COORDINATION_PROTOCOL_v0.1
ITERATION      1 of 3
MODE           READ_ANALYSIS_ALLOWED · CREATE_LEARNING_ARTIFACT_ONLY
STATE          ANALYSIS COMPLETE — one artifact produced, nothing activated
PRODUCED       learning/orchestrator/LEGEND-AGENT-COORDINATION-PROTOCOL-001.md  (this file)
WRITTEN TO     branch orch-agent-coordination-protocol, based on main @ 788c357
main           UNCHANGED at 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5
GATES RUN      4 of 4, all PASS (§ SURFACE_MAP · S-5)
```

### 🔴 One collision between this dispatch and a standing operator decision, recorded not resolved

The dispatch's `OBJECTIVE` opens with the word **"Design"**.
`DEC-20260822-ORCH-STATE-RECONSTRUCTION-CANDIDATE` (branch
`operator-decision-orch-state-reconstruction` @ `4652f83`) selected `OPTION B — HELD_AS_CANDIDATE`
and named, under `NEXT_ALLOWED_ACTION`, what is *not* authorized:

> *"no design phase, no specification work, no prototype, no writer, no adoption of any § 3 check
> or § 4 field, and no consultation of any § 3 check at a real dispatch."*

Three facts bear on whether that decision reaches this task, and none of them is mine to settle:

1. Its `applies_to` names **one object** — `PROPOSAL-ORCH-STATE-RECONSTRUCTION.md` — not the
   subject matter generally.
2. Its own `NEXT_ALLOWED_ACTION` lists what *may* occur without it authorizing anything,
   including *"any actor's `WORK_COMMIT` on its own branch, which H.1 gives to 'ogni attore'"*.
   This record is that and nothing more.
3. This dispatch's `MODE` line — `READ_ANALYSIS_ALLOWED · CREATE_LEARNING_ARTIFACT_ONLY` — and
   its own second line, *"This is a protocol analysis, not an implementation"*, are narrower than
   its opening verb.

**Handling.** The dispatch's `MODE` line is treated as controlling over its `OBJECTIVE` verb, so
this record analyses and specifies nothing. Every section below describes a shape and adopts
none of it. **If the operator intended "Design" in the sense `DEC-20260822-…-CANDIDATE` forbids,
this record is the wrong artifact and the decision, not this file, is what should govern.** The
collision is surfaced here rather than resolved silently, because resolving it in favour of
proceeding would be an actor choosing the reading that authorizes its own work.

---

## IDENTITY

### I-1 · Established from repository evidence, not from the dispatch

The dispatch addressed this session as Orchestrator. **Identity is not inherited from a
dispatch.** Every field was measured in this session, before any reasoning.

| Fact | Measured value | Command |
|---|---|---|
| Working directory | `<REPO_ROOT>` | `git rev-parse --show-toplevel` |
| Branch at analysis | `main` | `git branch --show-current` |
| HEAD at analysis | `788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5` | `git rev-parse HEAD` |
| Working tree at analysis | **clean** | `git status --porcelain` → empty |
| Worktrees present | **18** at measurement time (19 after this record's worktree was cut) | `git worktree list` |
| Worktree this record is written in | `…/scratchpad/wt-coord` | `git worktree add -b … main` |
| **Lease** | 🔴 **`ACTIVE by derivation: 0`** | `framework/scripts/lease_state.py` |
| **Runtime inventory** | 🔴 **absent on this ref**; present at `runtime/runtime_inventory.md` on branch `orchestrator` | `git ls-tree` per ref |
| **Agent Card registry** | 🔴 **absent on this ref**; present at `runtime/agent_card_registry.md` on branch `orchestrator` only | `git ls-tree` per ref |
| `ACTOR_ID` | **not established** — no registration record exists for this session | `orchestrator:runtime/agent_card_registry.md` |
| `SESSION_REF` | **not observable, and not invented** | `scientist_reading_modes.md` § 1.2 — no actor observes its own `SESSION_REF` |

Derivation output, reproduced rather than summarised:

```
now (derivation instant)  2026-08-22T16:50:41Z
  lease #1  derived=STALE     stored=STALE     expires=2026-08-18T09:40:25Z released=—
  lease #2  derived=RELEASED  stored=RELEASED  expires=2026-08-18T11:13:21Z released=2026-08-18T11:07:12Z
  lease #3  derived=STALE     stored=EXPIRED   expires=2026-08-18T13:04:11Z released=—
  lease #4  derived=RELEASED  stored=RELEASED  expires=2026-08-18T14:26:30Z released=2026-08-18T13:29:40Z
  lease #5  derived=RELEASED  stored=RELEASED  expires=2026-08-18T15:03:41Z released=2026-08-18T14:05:20Z
ACTIVE by derivation: 0
```

`--check` additionally returns exit 1 with two findings on record #3 — `DISAGREEMENT` (stored
`EXPIRED`, a value **I.3's vocabulary does not define**; it declares `ACTIVE | STALE | RELEASED`)
and `EXPIRED_WITHOUT_RENEWAL`.

### I-2 · ACTIVE capability — the question the dispatch asked, answered directly

```
DOES AN ACTIVE CAPABILITY EXIST?     NO.
```

Two independent senses of the question, both measured:

| Sense | Measurement | Source |
|---|---|---|
| an `ACTIVE` **lease** — the I.3 capability to act as Orchestrator | **0**, by derivation, never from the stored field | `lease_state.py` |
| a `VERIFIED` **capability row** — what body § 8 and Annex I.4 require before any assignment | **0**. `runtime/agent_card_registry.md` @ `orchestrator` declares **21 literal `{capability: …}` rows across 6 cards, every one `status: UNVERIFIED, last_verified: NONE`** | `git show orchestrator:runtime/agent_card_registry.md` |

> **A counting note, stated rather than adjudicated.** The three Scientist cards share one block
> headed `# COMMON TO ALL THREE`, so the capability total is **21** counted as literal rows and
> **33** counted per-actor (5 Orchestrator + 6 Plan + 4 Mirror + 6 × 3 Scientist). A neighbouring
> record reports 27. The three figures differ by counting rule, not by measurement, and **the
> figure that matters is the numerator: zero, under every rule.**

Two rows are `blocked`, not merely unverified: Mirror's *"Event ledger analysis"* (*blocked: the
ledger has no writer yet*) and Plan's *"Fingerprint composition"*. The registry states its own
consequence: *"Until then the laboratory is **not running**, and no assignment may be made on any
capability in this file."*

### I-3 · The consequence, stated plainly

`CLAUDE.md` § 0 is unconditional:

```
IF no valid runtime inventory / no ACTIVE ORCHESTRATOR_LEASE:
    ENTER BOOTSTRAP_MODE.
    Do NOT assume Orchestrator authority merely because you are in root.
```

**Both antecedents hold. This session is in `BOOTSTRAP_MODE` and is not Orchestrator.**

Per the dispatch's `IDENTITY CONSTRAINT` and per
`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` consequence 2, **every rule cited below is traced
to `GOVERNANCE_v3.1.1.md` or to a named annex.** Role contracts are cited only descriptively,
never as the source of a rule — including `roles/orchestrator.md`, whose own text agrees
(*"Position in the root confers nothing"*) but which carries `status: PROPOSED` and binds nobody.

---

## SURFACE_MAP

### S-1 · The measurement surface every claim below is scoped by

```
MEASURED_AT          ref   main
                     HEAD  788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5
                     tree  clean (git status --porcelain empty)
                     date  2026-08-22

REFS PRESENT         50 total = 36 refs/heads · 4 refs/remotes · 5 refs/tags
                                · 4 refs/codex · 1 refs/stash
REFS TREE-SURVEYED   45 (refs/heads + refs/remotes + refs/tags), by `git ls-tree -r` per ref,
                     materialised to one (ref, path) table of 20,443 rows
NOT SURVEYED         refs/codex (4) · refs/stash (1) — content not enumerated
WORKTREES            18 at measurement time
SURFACE DELTA        this session then added 1 branch and 1 worktree, so the same commands now
                     return 51 refs (37 heads) and 19 worktrees. The figures above are the ones
                     every claim below was measured against.
```

🔴 **Every absence claim in this record is scoped by that surface and by nothing wider.**
`NOT_FOUND` across 45 refs in this clone is not `NOT_EXIST` in a clone, a `refs/codex` ref, or a
remote this session cannot see.

### S-2 · 🔴 Two false zeros produced inside this session, and how they were caught

Both were query artifacts of the shell, not facts about the repository, and **both would have
been reported as clean measurements** had a positive control not been run in the same loop.

| # | Construct | What it silently did | Detected by |
|---|---|---|---|
| **A-1** | `for r in $REFS; do …` | The shell is **zsh 5.9**, which does **not** word-split unquoted parameter expansions. The loop ran **once**, with `$r` bound to all 45 refs concatenated. Three sweeps — `ledger/events/`, `LEARNING_INDEX`, `active_lessons/` — returned a clean `0 of 45` **before any tree was read** | a `ledger/approvals/` positive control placed in the same loop returned `0 of 45`, which cannot be true; probe `for r in $(printf 'a\nb\nc\n')` → **1 iteration** |
| **A-2** | `git rev-parse "$r:ledger/approvals/…"` | In zsh `$r:l` is the **lowercase parameter modifier**. The expansion became `refs/heads/main` lowercased + `edger/approvals/…`. 23 of 23 lookups failed with `fatal: Not a valid object name` | the fatals were visible; the braced form `"${r}:ledger/…"` resolves correctly |

Every sweep in this record was re-run with `while IFS= read -r` over a file of refs, with a
positive control that must return non-zero. **The controlled figures are the ones reported.**

```
POSITIVE CONTROL  ledger/approvals/   23 of 45 refs   ✅ instrument working
ledger/events/                         0 of 45 refs
LEARNING_INDEX (any case)              0 of 45 refs
active_lessons/                        0 of 45 refs
```

This is the sixth and seventh instance of one failure class on this review chain — after the
`\b`-in-git-grep regex, the working-directory sweep, the `^## H\.1` heading anchor, and the
`"APPROVAL_ID":"` key match. It is recorded as an instance, not as a claim to have inherited the
practice: **the practice that guards it is registered in a file no script reads** (F-5).

### S-3 · Objects that are cross-ref only

**MEASURED_AT: `main` @ `788c357`** for every "absent" cell.

| Object | On `main` | Carried by |
|---|---|---|
| `runtime/agent_card_registry.md`, `runtime/runtime_inventory.md` | ❌ | `orchestrator` only |
| `learning/mirror/**` (34 distinct paths) | ❌ | `mirror` only |
| `reviews/mirror/**` (50 distinct paths) | ❌ | `mirror` only |
| `ledger/checkpoints/mirror/CHK-mirror-0001…0008.json` | ❌ | `mirror` only |
| `governance/candidates/PROPOSAL-ORCH-STATE-RECONSTRUCTION.md` | ❌ | `orch-state-reconstruction` only |
| `reviews/mirror/REV-ORCH-STATE-RECONSTRUCTION-001.md` | ❌ | `mirror` only |
| `governance/decisions/DEC-20260822-ORCH-STATE-RECONSTRUCTION-CANDIDATE.md` | ❌ | `operator-decision-orch-state-reconstruction` only |
| `reviews/orchestrator/AUTHOR-RESPONSE-ORCH-STATE-RECONSTRUCTION-001.md` | ❌ | `author-response-orch-state-reconstruction` only |
| `learning/orchestrator/ORCHESTRATOR-SCIENTIFIC-PIPELINE-AND-LOOP-ARCHITECTURE-ANALYSIS-001.md` | ❌ | `orch-pipeline-loop-architecture` only |

`governance/decisions/` on `main` contains **exactly one** record —
`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md`.

**No ref carries the learning corpus of all three actors.** Measured over 45 refs, by namespace:

```
learning/plan/           20 refs carry it (incl. main)     23 distinct paths
learning/orchestrator/    4 refs (main, orchestrator, orch-pipeline-loop-architecture,
                                  author-response-orch-state-reconstruction)   13 distinct paths
learning/mirror/          1 ref  (mirror)                  34 distinct paths
```

`mirror` carries 34 Mirror records and **zero** Plan records; `main` carries Plan and Orchestrator
and **zero** Mirror records. 70 distinct learning paths exist; **the richest single ref carries 34
of them** (`mirror`), and it is the one ref that carries no Plan record at all.

### S-4 · Absent across the surveyed surface

**MEASURED_AT: 45 refs, positive control passed (S-2)**

| Object | Result |
|---|---|
| `ledger/events/` — the J.1 event ledger | 🔴 **0 of 45 refs** |
| `LEARNING_INDEX` (Annex E.2), any file so named, any case | 🔴 **0 of 45 refs** |
| `active_lessons/` — the path `CLAUDE.md` § 1 points at | 🔴 **0 of 45 refs** |
| `ledger/tasks/` for any owner other than `plan` | 🔴 **0 of 45 refs** — 5 distinct task records exist, all `ledger/tasks/plan/*.json` |
| a coordination-review artefact (Annex G.3 / body § 29.3) | 🔴 **0 of 45 refs** |

### S-5 · What is executable today — measured by running it in this session

| Gate | Verdict | Exit |
|---|---|---|
| `framework/scripts/legend_lint.py .` | `VERDICT: PASS` | 0 |
| `framework/scripts/fulltext_receipts.py verify` | `OK: 128 chained receipt(s), tail anchored` | 0 |
| `framework/scripts/growth_anchors.py check` | `PASS` — claims=39 · papers=70 · corpus=356 · literature=390 | 0 |
| `scripts/public_release_gate.py` | `VERDICT: PASS`, `BLOCKS: 0`, 4 `[REVIEW]` items | 0 |
| `framework/scripts/lease_state.py --check` | `ACTIVE by derivation: 0`, 2 findings on #3 | 1 |

**Executable coupling to the control plane — with a positive control.**

```
Python files      framework/scripts 51 · scripts 37 · governance/scripts 3   = 91
POSITIVE CONTROL  files referencing framework/state/  →  14   ✅ instrument working
files referencing learning/        →  0
files referencing reviews/         →  0
files referencing active_lessons   →  0
files referencing ledger/          →  1  — governance/scripts/test_candidate_content_hash.py,
                                          where both hits are fixture strings, not readers
HOOKS             .claude/settings.json declares exactly one: a PreToolUse Bash guard.
                  No SessionStart hook exists.
```

🔴 **No executable in this repository reads any control-plane state.** Tasks, approvals,
checkpoints, learning records and reviews have **zero** executable readers. Every gate that runs
reads *scientific* state or the *release* surface.

---

## FINDINGS

### F-1 · 🔴 Two corrections to the immediate predecessor, measured at the ref and HEAD it declared

`ORCHESTRATOR-SCIENTIFIC-PIPELINE-AND-LOOP-ARCHITECTURE-ANALYSIS-001`
(`orch-pipeline-loop-architecture` @ `d6d46f8`) declares `base_head: main @ 788c357` — the same
commit this record was measured at. Both corrections are **new measurements**, not amendments:
that record is not edited.

**(a) `CONTROL_PLANE_ROOTS` already contains `reviews/`. The predecessor's N-4 is false.**

The predecessor records, as a NEW open question:

> **N-4** · *"`CONTROL_PLANE_ROOTS` still omits `reviews/`, five days after the operator-adjudicated
> MAJOR determination requiring it"* — and, in § 5.3.4, lists *"adding reviews/ to
> CONTROL_PLANE_ROOTS … measured unchanged at `plan_defined_parameters.md:250`"* among the changes
> that **remain OPEN**. Its own frontmatter states the roots are *"exhaustively
> `governance/candidates/` and `ledger/`."*

Measured this session at `main` @ `788c357`, `governance/plan_defined_parameters.md:255–262`:

```
Control-plane roots are declared here, exhaustively, as directory prefixes:

CONTROL_PLANE_ROOTS:
- governance/candidates/
- ledger/
- reviews/
```

```
git merge-base --is-ancestor 178ea2a main   →  ancestor
178ea2a  2026-08-18 12:40:02 +0200  "P5.1 gains reviews/, states learning/ by intent,
                                     and the Orchestrator gets a branch"
```

**The change landed on 2026-08-18 — four days before the record that reports it as outstanding,
and on the very commit that record is based on.** The block begins at line 255 and the entry at
line 261; the predecessor anchored its measurement at **line 250**, which falls in the prose
paragraph above the fence. The same file's § P5.1 text at line 273 says so in terms:
*"`reviews/` — added, and it closes a gap between the definition and the rule."*

Two independent artifacts already agreed with the corrected reading and were not consulted
against it: `SCIENTIFIC-PIPELINE-PREPARATION-001` (on `main`) states the roots as three, and
`AUTHOR-RESPONSE-ORCH-STATE-RECONSTRUCTION-001` declares its own domain as *"CONTROL PLANE —
`reviews/` is a declared `CONTROL_PLANE_ROOT`."*

> **Why this one matters beyond bookkeeping.** N-4 is not a stray fact: the predecessor lists it
> among the acts that **require a governed change and remain open**. A dispatcher planning from
> that list would schedule work that has already been done, and would carry a live example of
> *"a durable, correct, adjudicated record that has not altered the system it describes"* — when
> in this case the record **did** alter the system, on time. **The measurement, not the
> propagation, is what failed.**

**(b) `ledger/checkpoints/` is not `plan`-only.**

The predecessor's § 2.4 lists *"`ledger/checkpoints/` for any actor other than `plan` — 🔴 **0 refs
of 44**"*. Measured over 45 refs with a passing positive control:

```
DISTINCT CHECKPOINT PATHS, repository-wide            27
  ledger/checkpoints/plan/    CHK-plan-0001 … 0019    19   (carried by 23 refs, incl. main)
  ledger/checkpoints/mirror/  CHK-mirror-0001 … 0008   8   (carried by refs/heads/mirror only)
```

**Mirror has written eight A.6 checkpoints.** The claim that only Plan has ever produced durable
control-plane records of that class is false, and the correction strengthens rather than weakens
the surrounding argument: *two* roles have exercised the checkpoint machinery and **no Scientist
has**, which is the asymmetry that actually bears on the pipeline.

**What survives unchanged.** Every other load-bearing negative in that record reproduced exactly
in this session under positive control: `ledger/events/` 0 of 45; `LEARNING_INDEX` 0 of 45;
`active_lessons/` 0 of 45; `ledger/tasks/` `plan`-only; zero executables reading the control
plane; the three-way non-nested approval queue (F-5b); the two serialisation conventions inside
the ten-line blob (2 no-space, 4 with-space, verified line by line).

---

### F-2 · TASK LIFECYCLE — the eight stages against measured evidence

The dispatch supplies a candidate lifecycle. Each stage is assessed on four questions:
**what durable evidence exists**, **who can create it**, **who can close it**, and **whether a
human is structurally required**. Authority is cited from H.1 and the annexes only.

> 🔴 **The finding that runs through the whole table: `create` is allocated for every stage;
> `close` is allocated for almost none.** H.1 has 17 data rows (counted this session, excluding
> the header and separator) and allocates by
> *decision type*. Not one row names a closure. A.5 supplies the state vocabulary and no writer;
> J.1 supplies `CLOSES_EVENT_ID` and its ledger exists on 0 of 45 refs. **Closure in this
> repository is today an inference a reader draws, not a record an actor writes.**

| Stage | Durable evidence that exists | Who may create it | Who may close it | Human required? |
|---|---|---|---|---|
| **`TASK_CREATED`** | **Annex A.1 `TASK_ASSIGNMENT`** — fully specified, 15 fields. 🔴 **5 instances repository-wide, all `ledger/tasks/plan/`; none ever issued to a Scientist**; all hand-authored JSON; **no validator exists for A.1** | H.1 row 1 — `Task / priorità / riassegnazione / generation` → **Orchestrator**. Conditioned on an ACTIVE lease? **No** — I.3 conditions the *commit* rows, not this one | undefined. A.5 offers `CANCELLED`; nothing says who writes it | **NO** for creating a task *inside* an authorized scope. **YES** for the scope: H.1 `Strategia complessiva → Operatore` |
| **`OBJECT_IDENTIFIED`** | 🔴 **no object class.** The nearest is `DELIVERABLE (artefatto + worktree/branch)` and `CURRENT_STATE (durable pointer)` in A.1 — both free text, no schema, no validator. The one structured precedent is `HANDOFF-GOV311-ORCHESTRATOR`'s frontmatter (§ F-3) | whoever writes the contract | — | **NO**, but see F-3: today nothing *checks* that identification succeeded |
| **`ASSIGNED`** | `TASK_ASSIGNMENT` + B.1 envelope (`MESSAGE_ID / TASK_ID / ACTOR_ID / FROM / TO / TYPE / STATE_CHANGE / DURABLE_POINTER`); A.5 state `ASSIGNED` | Orchestrator (H.1 row 1) | — | 🔴 **BLOCKED, not gated.** Body § 8: *"Orchestrator assegna sulle capabilities verificate, non sul ruolo presunto."* **0 of 21 rows are VERIFIED**, and L2 is `SUSPENDED` by the C-9 operator hold. Lifting it is HG-8 and is the operator's |
| **`WORKING`** | A.5 `ACKED → CLAIMED → IN_PROGRESS`; **A.6 `CHECKPOINT`** — instantiated **27 times** (19 `plan`, 8 `mirror`; **0 for any Scientist**); `WORK_COMMIT` on the actor's own branch | the owning actor. `WORK_COMMIT` → H.1 *"ogni attore, solo proprio branch"*, **needs no lease** | the owning actor, by writing the next checkpoint | **NO** |
| **`HANDOFF`** | 🔴 **Annex B.2 names `HANDOFF` in an enumeration and specifies nothing else** — no envelope beyond B.1, no required field, no state effect. Meanwhile **15 distinct paths** repository-wide carry a handoff name, in four namespaces, each with a shape of its own | anyone, in practice — which is the finding | — | **NO** by rule; **YES in fact**, because today the operator is the transport (F-4) |
| **`REVIEW`** | **Annex C.2's single format** — the strongest object in the lifecycle: `STEELMAN` mandatory *before* objections, four verdicts, `WHAT_WOULD_CHANGE_MY_MIND` mandatory, `AUTHOR_RESPONSE` mandatory. **72 distinct review paths** repository-wide (50 mirror · 15 orchestrator · 7 plan) | **opening: Orchestrator only** (C.3, body § 25). Writing: the reviewer | 🔴 **not the reviewer.** C.2: *"`AUTHOR_RESPONSE` obbligatoria; il silenzio non è accettazione."* A review is not closed by its verdict — it is closed by a response the **author** owes | **YES** at two points: C.1 floor `R3 TRIADIC` for persistent scientific disagreement (derogable only upward), and C.3 `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR`, which escalated adjudication to the operator once already this week when the author held H.1's adjudication row |
| **`CORRECTION`** | A.1 `RETRY_POLICY` (`max_attempts` / retryable classes / `on_exhaust: REASSIGN \| PARK \| ESCALATE`); A.4 anti-zombie; A.7 idempotent resume; **F.4 `DIAGNOSE` before accusation**; C.2 `REFINED (+REFINED_FORMULATION)` | the owning actor; reassignment (generation+1) → Orchestrator | undefined | **NO** for a retry inside policy. **YES** when `on_exhaust: ESCALATE`, and **YES** whenever the retry costs money — J.4 `DEFAULT_EXTERNAL_SPEND = 0` |
| **`COMPLETED`** | 🔴 **two completion predicates, of very different quality.** For a **scientific reading**: `scientist_reading_modes.md` §§ 3.6/3.8 specify a five-step acceptance test, steps 1–4 mechanical with tools that exist, step 5 (the blind locator audit) with **no executable form**. For **everything else**: `ACCEPTANCE_CRITERIA` is a free-text A.1 field with **no validator** | the owning actor declares; under a benchmark, completion is declared **to Plan for freezing** before anyone else reads it | 🔴 **nobody, durably.** J.1 defines `TASK_COMPLETE` as an event type; the ledger exists on 0 of 45 refs | **NO**, once step 5 has an owner |

**Three structural observations that follow from the table and are not in any one cell.**

1. **The lifecycle has no observer.** Six of the eight stages presuppose a record that some actor
   *chooses* to write. `lease_state.py`'s own documentation states the limit: *"Nothing compels
   the Orchestrator to record an acquisition, and nothing runs between turns."* A stage that
   nobody writes is indistinguishable from a stage that did not happen — and body § 18 says the
   same from the other side: *"Ciò che non è nello stato durevole non è accaduto."*
2. **`HANDOFF` is the weakest link and carries the most weight.** It is the only stage whose
   object is *named* by a frozen annex and *specified* nowhere, and it is precisely the stage the
   dispatch's target loop depends on (*"receive handoff → trigger next stage"*).
3. **`REVIEW` is the only stage whose closure is allocated to someone**, and it is allocated to
   the author, not the reviewer. That is a real precedent for how closure could be owned
   elsewhere, and it is the only one.

---

### F-3 · OBJECT ADDRESSING — the seven fields, and where each would come from today

The prior analysis concluded *"the loop is not blocked by authority … it is blocked by
addressing."* That conclusion was reached by the proposal's author, `CONFIRMED` by Mirror at R4,
and reproduced by the operator's decision. It is reproduced a fourth time here, mechanically:
**every object this record used as evidence had to be fetched by `git show <ref>:<path>`, and
`main` carries none of the nine objects in S-3.**

#### F-3.1 · Field-by-field

| Field | Is it defined anywhere as a required element? | What exists today | Verdict |
|---|---|---|---|
| **repository** | ❌ nowhere | implicit — one clone, 18 worktrees | **Not needed today; would be needed the moment a second clone exists.** Body § 33.3 already contemplates repository-bound Codex collaborators |
| **ref / branch** | ❌ **no schema requires it** | `HANDOFF-GOV311-ORCHESTRATOR` carries `source_branch:` as a **structured frontmatter key**. Measured across the handoff artifacts readable on `main`: **1 of 4 carries any ref-bearing key** | 🔴 **the load-bearing gap.** A path without a ref does not address an object here |
| **commit** | ❌ | same file carries `base_head:`. Reviews in this chain pin `blob oid` + `sha-256`; `HANDOFF-P5DOMAIN-MIRROR` distinguishes `BASE_HEAD` / `CONTENT_TIP` / `MANIFEST_TIP` as three separate oids | **precedent exists, requirement does not** |
| **path** | ✅ used universally | every dispatch record in the repository addresses by path | **present and insufficient alone** |
| **hash** | ✅ for candidates only | `CANDIDATE_CONTENT_HASH` (`governance/scripts/candidate_content_hash.py`), and Gate 5 requires the approval to cite the exact hash (J.3) | **solved for one object class, absent for every other** |
| **owner** | ✅ | A.1 `OWNER (ACTOR_ID)`; I.4 makes `ACTOR_ID` persistent and distinct from the ephemeral `SESSION_REF` | 🔴 **defined but not routable** — see F-3.2 |
| **task identifier** | ✅ | A.1 `TASK_ID` + `DIRECTIVE_VERSION` + `GENERATION`; B.1 carries `TASK_ID` | **present and well-formed** |

> **A branch name addresses a location, not a state.** It moves when the branch moves. The
> `AUTHOR_RESPONSE` in this chain states the discipline exactly: *"The blob is the pin; the branch
> name addresses a location, not a state."* — and demonstrates it, recording that its review's
> branch tip moved from `1892071` to `78dccaf` while the blob stayed `16322c97`. **Whether an
> address needs one oid or three is Q-2, open, and Plan's row under H.1.**

#### F-3.2 · Two addressing problems, and they are not the same problem

```
ADDRESSING AN OBJECT   fails for want of a REF FIELD.
                       The fix has a precedent already in the repository (three structured keys
                       on HANDOFF-GOV311-ORCHESTRATOR) and requires no new instrument to WRITE.
                       Requiring it of every handoff is a governed change (Q-6; Annex B is FROZEN).

ADDRESSING AN ACTOR    fails for want of a ROUTABLE IDENTIFIER.
                       ACTOR_ID is stable and is not a route. SESSION_REF is a route and is not
                       observable by its own holder. The registry derives all four SESSION_REFs
                       BY SET COMPLEMENT over peer lists, on a stated and attackable assumption,
                       marked `pending L1 confirmation`. CAND-20260819-XPORT records
                       ROUTING_TRANSPORT as a uds socket that dies with the process.
                       Conflict C-7 — one session seen by all four actors and claimed by none —
                       has been open since 2026-08-16.
```

**These have different costs and different owners.** The first is a convention with a precedent;
the second is a runtime property no document can fix.

#### F-3.3 · The three questions the dispatch asked

**Can an agent receive a task without a fully resolved object address?**

Today, **yes — and every task in the repository was received that way.** Nothing in A.1 requires
a ref; nothing validates A.1 at all; and all five existing task records were hand-authored. The
consequence is measurable rather than hypothetical: `HUMAN_APPROVAL_QUEUE.jsonl` exists in **three
mutually non-nested versions** (F-5b), which is what happens when an append-only object is
addressed by path and appended on two branches at once.

**Whether it *should* be possible is Q-1 in disguise, and Q-1 is open.** A rule that a task may
not be received without a resolved address is a **gate**; a note that resolution is advisable is
an **advisory**; a record of which addresses resolved is a **report**. `DEC-20260822-…-CANDIDATE`
§ 4 names the failure mode of not choosing: *a check never formally adopted, but consulted at
every dispatch until "reconstruction says BLOCKED" becomes the operative reason a task does not
proceed — a gate with no adoption record.* **This record does not choose.**

**When is address resolution performed?**

Four candidate moments exist in the repository, each already the site of *some* check. Listed as
observations, with no ordering proposed and none adopted:

```
AT CONTRACT WRITE   — the writer resolves and records. Cheapest; unverifiable by the recipient.
AT TASK_ACK         — B.3 already makes ACK mandatory on STATE_CHANGE: yes, with resend and
                      BLOCKER on second failure. A recipient that cannot resolve the address is
                      in exactly the position B.3's BLOCKER path already describes.
AT TASK_CLAIM       — scientist_reading_modes.md § 2.2 rule 3 already obliges the actor to query
                      the receipt ledger and task ledger BEFORE claiming, and to raise a BLOCKER
                      naming both records rather than claim. An address check at claim time is
                      the same shape as a check that already exists.
AT RECONCILIATION   — Plan's reconciliation over ledger/tasks/*/ (body § 30). Latest; catches
                      what the other three missed; cannot prevent the work.
```

🔴 **Every one of these presupposes a durable record that today nobody is compelled to write.**

**Who owns unresolved addressing?**

Decomposed, because the single question has three different answers under H.1:

| Sub-question | Owner | Basis |
|---|---|---|
| what an address *is* (fields, oid count) | **Plan** | H.1 `Integrazione strutturale / candidate`, subject to review. This is Q-2 |
| whether an unresolved address *blocks* | **Operatore** | a rule that blocks dispatch is normative — H.1 `Spese / MAJOR approval / governance`. This is Q-1 |
| resolving *this* address, for *this* task | **the dispatcher who wrote the contract** | H.1 row 1 gives task/priority/reassignment to Orchestrator; nothing else names a resolver |
| whether Annex B's `HANDOFF` must carry the fields | **unclear** — Annex B is `FROZEN`, so it is a governed change | Q-6, open |

🔴 **The fourth row is the honest one: the question the dispatch asks most directly is the one the
repository allocates least clearly.** And a fifth answer is measured rather than allocated:
**today, unresolved addressing is owned by the operator**, who resolves it by naming the ref in
the next prompt (F-4).

---

### F-4 · ORCHESTRATOR ROLE BOUNDARY

#### F-4.1 · What actually moves work today — measured from the commit graph, not recalled

```
operator
   │  reads a durable artifact in checkout X, by hand
   │  composes a dispatch naming a role, a mode, a scope — and the ref
   ▼
session (any checkout)  ── establishes identity from the repo, not from the dispatch
   │  works inside one worktree
   │  WORK_COMMIT on its own branch (H.1 — "ogni attore, solo proprio branch")
   ▼
durable artifact on branch B
   │
   └── 🔴 NO RETURN EDGE. Nothing carries (ref, path) forward.
```

On 2026-08-22 the chain `PROPOSAL → REVIEW → DECISION → AUTHOR_RESPONSE → ANALYSIS → ANALYSIS`
produced **six artifacts on six branches**, with **no merge, no message and no shared file
connecting any pair**. Each later session read its predecessor by `git show <ref>:<path>` — and
each was told which ref *by the dispatch*. **The operator is the transport layer.**

#### F-4.2 · The four proposed boundaries, tested against H.1

The dispatch proposes a decomposition. Each function is traced to a row, or recorded as
unallocated.

| Proposed to | Function | H.1 row | Verdict |
|---|---|---|---|
| **ORCHESTRATOR** | routing | *Task / priorità / riassegnazione / generation* | ✅ allocated |
| | dependency management | — | 🔴 **no row.** A.1 has a `DEPENDENCIES` field; no row says who resolves one |
| | scheduling | *Task / priorità* covers order; **cadence is separate** | ⚠️ partly. `MIRROR_RETROSPECTIVE` cadence N is `UNASSIGNED` and G.2 bars Mirror from setting it alone |
| | escalation | *Classificazione HUMAN_REQUIRED ordinaria*; *Aggiudicazione challenge (con rationale)* | ✅ allocated — and see the overlap below |
| | workflow state | — | 🔴 **no row, and no object.** `AFFECTED_WORKFLOW` (E.2) is a *field* denoting a surface; there is no `WORKFLOW` object, definition, state or engine anywhere on 45 refs |
| **SCIENTIST** | scientific reasoning; evidence evaluation | *Conclusione scientifica → Scientist responsabile (soggetta a review, mai a ordine)* | ✅ allocated, and explicitly immune to instruction |
| **MIRROR** | epistemic / methodological review | *Epistemic / method review*; *Classificazione MAJOR dubbia (fail-closed)* | ✅ allocated |
| **PLAN** | integration and structural preparation | *Integrazione strutturale / candidate*; *Rifiuto integrazione per provenance/schema (INTEGRATION_BLOCK)* | ✅ allocated |

#### F-4.3 · Overlaps — three real ones, each already governed

| # | Overlap | How the governance already separates it | Residual risk |
|---|---|---|---|
| **OV-1** | **Orchestrator adjudicates challenges** *and* **Mirror owns method review.** Both bear on whether a piece of work is acceptable | C.4 partitions the *objects*: `EVIDENCE → Scientist + Plan/provenance`; `INFERENCE → peer Scientist`; `SYSTEM → Mirror`. Orchestrator adjudicates the *challenge*, not the *method* | 🔴 **already realised once, and handled correctly.** In this very chain H.1 gave `Aggiudicazione challenge` to the Orchestrator, who was the **author** of the reviewed object; C.3's `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR` forced escalation to the operator. **The overlap is detected by C.3, not by H.1** |
| **OV-2** | **Orchestrator sets the Ladder level and chooses reviewers** *and* **Mirror classifies doubtful MAJOR** | H.1 gives the level to Orchestrator *"≥ floor"* — the floor is C.1's and is derogable only upward. `Classificazione MAJOR dubbia → Mirror (fail-closed)` removes the classification from the scheduler | doubt is the *trigger*, not the conclusion; nothing observes whether doubt was felt |
| **OV-3** | **Plan refuses integration** *and* **Scientist owns the conclusion** | body § 28 draws it exactly: *"Plan rifiuta per ragioni strutturali/provenance/protocollo; NON risolve significato scientifico conteso: `INTEGRATION_BLOCK → Orchestrator → Scientist`."* | the return path runs *through* Orchestrator — i.e. through the actor with no return edge (F-4.1) |

#### F-4.4 · Risks in the proposed boundary

| # | Risk | Anchor |
|---|---|---|
| **RB-1** | 🔴 **"workflow state" would be a new authority, not a redistribution of an existing one.** No H.1 row, no object, no state, no engine exists. Adding one is an amendment to a `[MAJOR]` FROZEN matrix — Q-7, which **nobody has proposed** and this record does not propose | H.1; § 3.1 term census |
| **RB-2** | **"dependency management" has a field but no owner.** A.1 `DEPENDENCIES` is declared; who declares a dependency satisfied is unallocated. Left as-is, it defaults to whoever is convenient | A.1; H.1 |
| **RB-3** | 🔴 **The routing function is the one thing Orchestrator provably cannot do today.** H.1 gives it routing; F-3.2 shows no actor is routable. **The authority is allocated to an actor that lacks the capability, and the capability is `UNVERIFIED` in the registry that would record it** | H.1; I.4; F-3.2 |
| **RB-4** | **Escalation is where an actor could resolve an ambiguity in its own favour.** `Classificazione HUMAN_REQUIRED ordinaria → Orchestrator` means the actor that benefits from *not* escalating is the actor that classifies. H.1's compensator is `Classificazione MAJOR dubbia → Mirror, fail-closed` — which triggers on doubt, and nothing observes doubt | H.1; J.0 (RBAC absent) |
| **RB-5** | **Scheduling without a cadence owner produces indefinite provisionality.** Annex E.3 states *"Mai provisional per sempre"*, and both existing provisional practices expire *"at Mirror's first coordination review"* — of which **0 exist on 45 refs**, whose cadence is `UNASSIGNED`, and which G.2 bars Mirror from scheduling alone | E.3; G.2; S-4 |

> 🔴 **The boundary is not the problem.** Every edge of `Orchestrator → Plan → Mirror → Scientist`
> is allocated by H.1 without gap or overlap that C.3, § 28 and G.2 do not already separate. Two
> of the five functions the dispatch assigns to Orchestrator — *workflow state* and *dependency
> management* — **are not in H.1 at all**, and one — *routing* — is allocated but not exercisable.
> **The gap is capability and addressing, not authority.**

---

### F-5 · HUMAN GATE MODEL

Named in the repository's own vocabulary. The dispatch's phrase *"human gate"* is **external**:
`HUMAN_GATE` occurs zero times across the surveyed surface. The repository's terms are
`HUMAN_REQUIRED` (B.2 message type; H.1 classification row), `HUMAN_APPROVAL_QUEUE` (J.3) and
`GATE 0–5` (Annex D).

#### F-5.1 · The dispatch's three AUTONOMOUS examples, each tested

| Example | Verdict | Trace |
|---|---|---|
| **assigning already approved tasks** | ⚠️ **AUTONOMOUS as to authority, BLOCKED as to precondition.** H.1 row 1 gives assignment to Orchestrator and does not condition it on a lease. But body § 8 is explicit: *"Orchestrator assegna sulle capabilities **verificate**, non sul ruolo presunto"* — and **0 of 21 rows are VERIFIED**. Further, J.3's `APPROVAL ≠ AUTHORIZATION` (E4): *"l'approvazione autorizza l'intento, non bypassa i gate"*. **"Already approved" does not make an assignment executable** | H.1; body § 8; I.4; J.3 |
| **requesting review** | ✅ **AUTONOMOUS, and exclusively so.** C.3 and body § 25: *"Apertura solo via Orchestrator."* No other actor may open a review — Mirror included. Constraints, not gates: rotation (never fixed pairs), `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR` for important reviews, reviewer without contributed evidence, cap of one active review per Scientist, max 2 rounds → adjudication | C.3; body § 25 |
| **repeating failed validation** | 🔴 **NOT unconditionally autonomous.** Three conditions flip it: (1) A.1 `RETRY_POLICY.on_exhaust` may be `ESCALATE`, which is a human route by construction; (2) J.4 `DEFAULT_EXTERNAL_SPEND = 0` — a retry that costs money is `HUMAN_APPROVAL (TYPE: SPEND)` *before* the first attempt, not after the last; (3) **F.4 `DIAGNOSE` must run first** — B.3 records the measured failure class *"ACK emesso ma lavoro mai partito"* with causes *turno troncato, permission prompt*, and F.4 forbids classifying a runtime fault as refusal. **Repeating a validation that failed for a runtime reason is not a retry of the validation; it is a retry of the runtime** | A.1; J.4; B.3; F.4 |

#### F-5.2 · Structural human gates — traced to a source, never to a judgement about convenience

| # | Gate | Source | Recurrence |
|---|---|---|---|
| **HG-1** | Scientific priority and scope — which studies, in what order | H.1 `Strategia complessiva → Operatore` | per batch |
| **HG-2** | Spend / MAJOR approval / governance | H.1; J.3 `TYPE: MAJOR \| SPEND \| DESTRUCTIVE \| GOVERNANCE \| STRATEGIC`; J.4 | per batch |
| **HG-3** | Persistent scientific disagreement | C.1 floor **R3 TRIADIC**, derogable only upward; body § 27 — *"la sintesi forzata è un errore"* | per occurrence |
| **HG-4** | Public push | `public_release_gate.py` **plus** a human reading `git diff origin/main..main --stat` | per push |
| **HG-5** | Anything therapeutic | `CLAUDE.md` — never a substitute for a treating clinical team | always |
| **HG-6** | Role-contract activation | `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` consequence 3: *"a new, explicit activation act is required"*, which it does not perform, schedule or specify | one-time |
| **HG-7** | **Q-1** — gate / advisory / report | operator (H.1 → governance). A one-way door | one-time |
| **HG-8** | Lifting the C-9 hold on L2 capability verification | operator hold, 2026-08-17. **0 of 21 capabilities VERIFIED**; assignment requires VERIFIED | one-time |
| **HG-9** | `scientist-c` `ACTOR_ID` confirmation | I.2 step 7, PID-12 — *"permanent once set, confirmed at registration"* | one-time |
| **HG-10** | Whether a third Scientist position exists and what it does | collides with body § 32, H.1 and body § 27 | one-time |
| **HG-11** | `MIRROR_RETROSPECTIVE` cadence N | `UNASSIGNED`; G.2 bars Mirror from setting it alone | one-time |
| **HG-12** | `C-7` — a session seen by all four actors and claimed by none | open since 2026-08-16 | one-time |

```
RECURRING PER BATCH   HG-1 … HG-5    5
ONE-TIME UNBLOCKING   HG-6 … HG-12   7
```

🔴 **The five recurring gates are exactly the four the dispatch wants the human to keep — changing
scientific direction, activating contracts, modifying governance, prioritising projects — plus the
publication and therapeutic bars. The seven one-time gates are what blocks everything else, and
not one of them is held by any actor in this laboratory.** Six are the operator's under H.1; HG-11
is barred to Mirror by G.2 and unassigned to anyone else.

> **This is the answer to the dispatch's core question, in one line:** the distance between
> human-routed and agent-coordinated work is **seven human decisions and one addressing
> convention**, not a protocol. The recurring human cost the operator actually pays today —
> reading an artifact on one ref and naming it in the next dispatch — is **none of the four
> things the dispatch wants the human to keep.**

#### F-5.3 · 🔴 The human-decision record itself is not readable in one place

J.3 makes `HUMAN_APPROVAL_QUEUE` the durable object every `HUMAN_REQUIRED` creates. Measured this
session by blob oid over 45 refs, under positive control:

| Blob | Lines | Refs | `APPROVAL_ID`s carried |
|---|---|---|---|
| `20c24a2ba4` | 6 | **20** — incl. `main`, `mirror`, and all four `*-reconstruction` branches | GOV311-001, GOV311-002 |
| `bb603d9a27` | 10 | 1 — `orchestrator` | + SUNSET-DEC3-001, SCIAB-001, XPORT-001, P5DOMAIN-001 |
| `95fc816390` | 14 | 2 — `evidence-index`, `p51c9-rebased-onto-c89c2217` | + HA-1, HA-2, HA-3, HA-4 |

```
DISTINCT APPROVAL_IDs repository-wide   10
MAX carried by any single ref            6
carried by `main`                        2
mutually non-nested extended versions    2   (orchestrator ⊄ evidence-index ⊄ orchestrator)
```

**An append-only ledger has been appended to concurrently on two branches** — the multi-writer
condition J.1 forbids in terms (*"append-only, nessun file condiviso multi-writer"*). And the same
file carries **two serialisation conventions**, verified line by line in the ten-line blob: lines
2 and 4 write `"APPROVAL_ID":"`, lines 7–10 write `"APPROVAL_ID": "`. A key-match on either
literal returns a clean, wrong answer.

**Any coordination protocol in which a human gate is consulted programmatically has to reckon
with the fact that no ref carries more than 60 % of the human decisions already taken.**

---

### F-6 · LEARNING / MEMORY LOOP

#### F-6.1 · The four stages against measured mechanisms

```
failure detected  →  learning artifact  →  indexed memory  →  future task retrieves lesson
       │                    │                     │                        │
       ▼                    ▼                     ▼                        ▼
 3 of 8 DETECTION      70 distinct          🔴 NO INDEX            🔴 NO MECHANISM
 routes mechanical     learning paths       LEARNING_INDEX          0 executable readers
 5 route to Mirror     across 3 refs        0 of 45 refs            1 router pointer, broken
 instruments that      no ref sees > 36     active_lessons/
 do not exist                               0 of 45 refs
```

#### F-6.2 · Minimum required components — what Annex E already names

**The schema is not the gap.** Every field a correction memory needs is already named in FROZEN
normative text, and named more than once:

| Component | Where it is already specified | Instantiated? |
|---|---|---|
| a learning record | **E.6** `Session Learning Record` — 12 fields incl. `LEARNING / MICRO-UPGRADE / CLASSIFICATION / EVIDENCE / LEARNING_ID (+CONFIRMATION_CLASS)`. Persistence: `WORK_COMMIT` at milestone granularity | ✅ **70 distinct paths repository-wide** |
| a lifecycle | **E.1** `OBSERVED → LOCAL → PROVISIONAL → VALIDATING → PROMOTED \| REJECTED \| SUPERSEDED \| EXPIRED` | ✅ used in prose |
| an index | **E.2** `LEARNING_INDEX` — 12 fields incl. `AFFECTED_WORKFLOW`, `CONFIRMATION_CLASSES`, `EXPIRY_OR_REVIEW_DATE`; dedup rule; ≥2 confirmations, or 1 + Mirror validation | 🔴 **0 of 45 refs** |
| a compression stage | **E.5 / body § 19** `RAW → Mirror clustering → ACTIVE LESSONS → role-specific subset → rehydration`, RAW lossless, `derived_from:` mandatory, budget defined by Plan | 🔴 **0 clustering artefacts, 0 `ACTIVE_LESSONS`, 0 subsets** |
| a provisional-practice object | **E.3** `PRACTICE_ID / HYPOTHESIS / APPLIES_TO / STARTED / EVIDENCE_EXPECTED / SUCCESS_CRITERION / FAILURE_CRITERION / EXPIRY / ROLLBACK`, *"Mai provisional per sempre"* | ⚠️ 2 exist, both stuck — see F-6.4 |
| a mandatory trigger | **body § 15** — every significant session MUST close with a Session Learning Review, and MUST consult the `LEARNING_INDEX` first | 🔴 **the trigger is mandatory and its precondition does not exist** |

#### F-6.3 · Missing components — measured, with the retrieval test

```
TEST 1  executable coupling
        0 of 91 Python files read learning/ or reviews/ or active_lessons
        POSITIVE CONTROL: 14 files read framework/state/    ✅ instrument working

TEST 2  entrypoint reachability
        Exactly ONE reference exists in the router loaded every session — CLAUDE.md § 1:
          "| Active lessons for your role, once operative | `active_lessons/` —
           **not yet materialized** |"
        🔴 That single pointer targets a path that exists on 0 of 45 refs, and it does NOT
           mention learning/ or reviews/, where all 70 + 72 records actually live.

TEST 3  session automation
        .claude/settings.json declares one hook: a PreToolUse Bash guard. No SessionStart hook.

TEST 4  partition
        No ref carries all three actors' learning. `mirror` holds 34 Mirror records and zero
        Plan records; `main` holds Plan and Orchestrator and zero Mirror records.
```

🔴 **A future agent reaches these records by listing a directory it was never told about — and
only if it happens to be standing on the right ref.** Body § 15 obliges it to consult an index
that does not exist, and § 18 declares the durable state sovereign (*"il messaggio notifica, il
commit fa fede"*) over a corpus no entrypoint names.

**The one working retrieval channel is measurable, and it is not a repository mechanism.** The
rule *"NOT_FOUND locally is not NOT_EXIST repository-wide, with a required MEASURED_AT block"*
appears near-verbatim in the dispatches issued on 2026-08-22 — **including this one**, whose
`IDENTITY CONSTRAINT` and `SURFACE_MAP` requirements are that rule in operational form. It
propagated **through the operator writing it into a prompt.** That is evidence that transmission
works and evidence that the working channel is a human.

#### F-6.4 · 🔴 The bottleneck is not storage, and not content — it is that nothing closes

Five distinct blockages, and they are not the same blockage:

```
(1) NO INDEX             LEARNING_INDEX — 0 of 45 refs. Body §15's mandatory dedup step has
                         no object to consult.
(2) NO COMPRESSION       ACTIVE_LESSONS — 0 of 45. Rehydration loads nothing.
(3) NO COUPLING          0 of 91 executables read the corpus. Positive control passed.
(4) NO PARTITION-        no ref holds all three actors' learning. A lesson written by Mirror
    CROSSING             is unreachable from every ref an Orchestrator session starts on.
(5) NO LIFECYCLE EXIT    both existing E.3 practices expire "at Mirror's first coordination
                         review". 0 such artefacts exist on 45 refs; the cadence N is
                         UNASSIGNED; G.2 bars Mirror from setting it alone. Annex E.3 says
                         "Mai provisional per sempre" — and both are held indefinitely
                         provisional by an event that has never occurred and that no single
                         actor may schedule.
```

**And the detection half is weaker than the storage half.** Of the eight `DETECTION` lines in
`governance/`, **three are mechanical and available** (A.3 claim conflict at write; B.3 heartbeat
+ `MESSAGE_ID` dedup; I.3 double-record at write / GATE 0). **Five route to Mirror instruments
that do not exist** — and the two that would detect a *recurring* failure are both in the
unavailable set. Recurring failure is precisely the condition Annex G.1 names `MIRROR_REQUIRED`.

> 🔴 **F-1 is this section's own evidence.** A correction detected in one session did not reach
> the next: the `reviews/` root was added on 2026-08-18 and reported as outstanding on 2026-08-22
> by a record whose own base contains it. **Nothing in the loop was available to carry that
> forward, so it was re-derived from scratch — and re-derived wrongly.** The failure is not that
> the lesson was unlearned; it is that the lesson was never *retrievable*, so the second session
> measured instead of remembering, and its measurement was the thing that broke.

#### F-6.5 · Ownership questions — three, none resolvable here

| # | Question | Why it is open |
|---|---|---|
| **OW-1** | **Which of Plan or Mirror creates the first `LEARNING_INDEX` entry?** | E.2 splits the object itself — *"durevolezza: Plan; cura epistemica: Mirror"* — and does not say who writes row one. H.1 restates the split verbatim (*"Lifecycle learning: epistemico Mirror, durevolezza Plan"*) with **`—`** in its authority column, the only row in the matrix that names no authority |
| **OW-2** | **Who owns a correction memory arising from *another* actor's failure?** | No annex addresses it. The two E.3 practices that exist were authored by Plan about a defect Mirror detected, and stored in `governance/design_records/` — a namespace **neither E.6 nor E.2 names**. This record is itself an instance: F-1 corrects another actor's measurement and has no home for the correction other than its own author's namespace |
| **OW-3** | **Who schedules the event that lets a provisional practice expire?** | G.3's coordination review is the declared expiry event; its cadence N is `UNASSIGNED`; G.2 bars Mirror from setting it; nobody else is assigned it. **HG-11** |

---

## OPEN_QUESTIONS

**None is resolved here, and none is assigned to anyone.** Carried questions keep their original
identifiers so they are not renumbered into new objects.

| # | Question | Owner by H.1 | State |
|---|---|---|---|
| **Q-1** | Is a pre-dispatch check a **gate**, an **advisory**, or a **report**? | operator (governance) | **OPEN** — a one-way door; F-3.3 turns on it |
| **Q-2** | What identifies a dispatched object — ref, tip oid, content hash, or all three? | Plan, subject to review | **OPEN** — `HANDOFF-GOV311-ORCHESTRATOR`'s three structured keys are the precedent to start from |
| **Q-3** | Does a dispatch block map onto A.5 `BLOCKED`, or is it a pre-task state with no `TASK_ID`? | — | **OPEN** |
| **Q-4** | Who writes actor readiness? Today the actor writes its own | — | **OPEN**; adjacent to C-9 § 5, held |
| **Q-5** | Can any of this be specified before `ledger/events/` has a writer? | — | **OPEN** |
| **Q-6** | Does Annex B's `HANDOFF` need a schema? 15 paths, 15 shapes, 1 of 4 readable on `main` carrying a ref key | unclear — B is FROZEN | **OPEN** |
| **Q-7** | Does H.1 need a row for *"may actor X act on object Y"*? | — | **OPEN**; H.1 is `[MAJOR]` and FROZEN; no amendment proposed by anyone |
| **Q-8** | What resolves C-7? | operator | **OPEN** since 2026-08-16 |
| **Q-9** | Does state reconstruction run per dispatch, per session, or on demand? | — | **OPEN** |
| **Q-10** | Relationship between `PROPOSAL-ORCH-STATE-RECONSTRUCTION` and `PROPOSAL-C9-STATE-MODEL` | Plan (sequencing) | **OPEN**; both held |
| **O-1** | `scientist_reading_modes.md`'s three activation clauses measure SATISFIED; its status line still reads `PROPOSED` | operator | **OPEN** (carried) |
| **N-1** | `HUMAN_APPROVAL_QUEUE.jsonl` in three mutually non-nested versions; 10 distinct approvals, max 6 per ref, `main` carries 2 | Plan (durability) / operator | **OPEN** — reproduced independently (F-5.3) |
| **N-2** | Which of Plan or Mirror creates the first `LEARNING_INDEX` entry — H.1's only row with no authority | Plan / Mirror / operator | **OPEN** (= OW-1) |
| **N-3** | Who owns a correction memory arising from another actor's failure | — | **OPEN** (= OW-2) |
| **N-4** | ~~`CONTROL_PLANE_ROOTS` omits `reviews/`~~ | — | 🔴 **CLOSED BY MEASUREMENT, not by act.** The root was added 2026-08-18 (`178ea2a`, ancestor of `main`). See F-1(a). **This record does not close the question by authority — it reports that the underlying condition never held at the base the question was measured on** |
| **C-1** | 🔴 **NEW.** No H.1 row allocates **closure** of anything except a review (which C.2 gives to the *author*, not the reviewer). Every other lifecycle stage ends by inference | — | **OPEN** (F-2) |
| **C-2** | 🔴 **NEW.** *"workflow state"* and *"dependency management"* — two of the five functions the dispatch assigns to Orchestrator — **have no H.1 row and no object.** Adding either is an amendment to a FROZEN `[MAJOR]` matrix | operator (governance) | **OPEN** (F-4.4 RB-1, RB-2) |
| **C-3** | 🔴 **NEW.** H.1 allocates routing to Orchestrator, and no actor is routable (F-3.2). **An authority allocated to an actor that lacks the capability, where the capability is `UNVERIFIED` in the registry that would record it** | — | **OPEN** |
| **C-4** | 🔴 **NEW.** Does the `DEC-20260822-…-CANDIDATE` prohibition on *"design phase, specification work"* reach dispatches other than the one candidate it `applies_to`? | operator | **OPEN** — surfaced in `TASK_STATUS`, and the reason this record analyses rather than specifies |

---

## NEXT_TRANSITION

> **Stated as a dependency structure that was measured, not as a plan, a sequence anyone is asked
> to follow, or a recommendation. Nothing below is assigned, scheduled or authorized.**

### What the measured dependencies imply about ordering

```
Q-1  (gate | advisory | report)
   └── upstream of every check in F-3.3 and of whether an unresolved address may block.
       DEC-…-CANDIDATE reason 5: "Authorizing design of the check while its normative character
       is undetermined is the shortest route to F-10's drift path." Owner: operator.

HG-8  lifting the C-9 hold on L2
   └── upstream of ANY assignment. Body §8 requires VERIFIED capabilities; 0 of 21 are.
       This gate alone makes F-2's ASSIGNED row unusable no matter what else is fixed —
       and unlike Q-1 it forecloses nothing.

HG-6  role-contract activation
   └── upstream of any statement about what a stage of the pipeline IS. Until it happens,
       H.1's 17 decision-type rows are the only binding description of the five actors,
       and they allocate by decision type, never by stage.

ledger/events/ having a writer
   └── upstream of J.2's own definition of a transition ("evento (J.1) + roster durevole"),
       of Mirror's declared primary analysis surface (G.3 / body §29.3), of 5 of 8 DETECTION
       routes, and of the third part of J.0's compensator for absent runtime RBAC.
       Named OWED NOT BARRED. Design chosen (per-actor append-only), writer not built.

MIRROR_RETROSPECTIVE cadence N  (HG-11)
   └── upstream of the expiry of both existing E.3 practices, and therefore of Annex E.3's
       own rule that nothing stays provisional forever. G.2 bars Mirror from setting it.
       Nobody else is assigned it.
```

🔴 **Two of these five are one-way doors** (Q-1, HG-6). **Three foreclose nothing** (HG-8, the
ledger writer, HG-11) — and all three are today held by nobody who could act on them.

### The smallest observation this analysis supports about the dispatch's core question

Recorded as a measurement, not as a proposal:

```
Of the six edges in the target loop — create → assign → monitor → receive handoff →
trigger next → escalate — FIVE have a specified object today:

  create           Annex A.1 TASK_ASSIGNMENT      complete, 15 fields, 0 validators
  assign           A.1 + B.1 envelope + A.2 ACK   complete; blocked on VERIFIED capabilities
  monitor          A.5 states + A.6 CHECKPOINT    27 checkpoints exist; 0 for any Scientist
  receive handoff  Annex B.2 `HANDOFF`            🔴 NAMED AND UNSPECIFIED — the one gap
  trigger next     C.3 review opening; A.1 gen+1  complete
  escalate         H.1 + J.3 HUMAN_APPROVAL_QUEUE complete; the queue has forked (F-5.3)

The single missing object is the handoff, and the single missing field on it is the ref.
Neither is a protocol. Both are governed changes, and neither is this record's to make.
```

### What iteration 2 could measure that this one did not

```
NOT MEASURED  refs/codex (4) and refs/stash (1) — content not enumerated (S-1)
NOT MEASURED  whether any Codex worktree holds work that would collide with a first batch.
              Body §41 forbids double work with the Codex worktrees; four Codex worktrees
              carry PMID-named branches
NOT MEASURED  PROPOSAL-C9-STATE-MODEL's text, read here only through Q-10
NOT MEASURED  whether the three HUMAN_APPROVAL_QUEUE versions can be reconciled without loss,
              or whether the divergence has already produced a decision recorded in one place
              and contradicted in another (N-1)
NOT MEASURED  whether any OTHER negative in the predecessor chain shares F-1's defect — only
              the two corrected here were re-derived from the primary source; the rest were
              re-measured as claims, not re-derived from their original anchors
```

### The state this record leaves behind

```
Nothing is activated, assigned, adopted, resolved or authorized.
One file is added, on branch `orch-agent-coordination-protocol`, based on main @ 788c357.
main is UNCHANGED. No governance, roles, framework, ledger or runtime path is written.
No scientific artifact is created and no paper was read.

Iteration 1 of 3.
```

---

## What this record does NOT do

- It does **not** design, define, adopt or specify a coordination protocol. Per `TASK_STATUS`,
  the dispatch's `MODE` line is treated as controlling over its `OBJECTIVE` verb.
- It does **not** activate a role contract, or perform the act `DEC-20260822` consequence 3
  requires.
- It does **not** confer, claim or imply Orchestrator authority — § IDENTITY records that
  authority is absent and that this session is in `BOOTSTRAP_MODE`.
- It does **not** assign an actor, a paper, a batch, a review, or an owner for any question.
- It does **not** create a Task Contract, a `PARALLEL_READ_GROUP`, a ledger event, a candidate,
  an index, a schema, a cadence, a validator or a writer.
- It does **not** resolve Q-1 … Q-10, O-1, N-1 … N-3, OW-1 … OW-3, or C-1 … C-4.
- It does **not** decide whether `reviews/` being present in `CONTROL_PLANE_ROOTS` closes N-4 as
  a governance matter. It reports that the condition N-4 asserts **did not hold at the base N-4
  was measured on**, and leaves the disposition to whoever owns it.
- It does **not** verify any capability, lift the C-9 hold, or set any cadence.
- It does **not** amend any record. The two corrections in F-1 are new measurements;
  `ORCHESTRATOR-SCIENTIFIC-PIPELINE-AND-LOOP-ARCHITECTURE-ANALYSIS-001` is left exactly as
  written, and is **not** edited, superseded or withdrawn by this file.
- It does **not** constitute an `AUTHOR_RESPONSE` to anything, and is **not** a Session Learning
  Record under Annex E.6.
- It is **not** a `WORK_COMMIT` toward a candidate and **not** a `CANONICAL_BATCH_COMMIT`.
- It requests, performs and schedules **no merge** of its own branch.

---

## Validation

| Constraint | Result | How verified |
|---|---|---|
| only the allowed path modified | ✅ exactly one new file, `learning/orchestrator/LEGEND-AGENT-COORDINATION-PROTOCOL-001.md` | `git status --porcelain` in the authoring worktree |
| `governance/` untouched | ✅ | diff name-only against `main` |
| `roles/` untouched | ✅ | same |
| `framework/` untouched | ✅ | same |
| `ledger/` untouched | ✅ | same |
| `runtime/` untouched | ✅ — including `runtime/orchestrator_lease.md`, whose single writer is the Orchestrator from the orchestrator worktree, which this session is neither | same |
| working tree clean | ✅ after commit | `git status --porcelain` → empty, in both the authoring worktree and the root |
| `main` unchanged | ✅ still `788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5` | `git rev-parse main` |
| no contract activated | ✅ | § IDENTITY; no `roles/` write |
| no actor assigned | ✅ no `Agent` or `SendMessage` call was made in this session | — |
| no authority created | ✅ every rule cited from the body or a named annex, never from a role contract | throughout |
| gates re-run after writing | recorded in the session response, not transcribed here, so this file does not assert a result it cannot itself re-derive | — |

### Domain and collision disclosure

- **Content domain.** `learning/` is not a `CONTROL_PLANE_ROOT` (measured: the roots are
  `governance/candidates/`, `ledger/`, `reviews/`). This record therefore **moves the candidate
  content hash** of any future candidate that re-aligns onto the branch carrying it.
- **Base-condition check.** The `BASE_HEAD` values declared by candidates readable on `main` are
  `749a9a9b`, `908197ba` (×2), `c89c2217`, `cbce3016` and `f5b32155` — **all already behind
  `main` at `788c357`. No open candidate declares `788c357` as its `BASE_HEAD`**, so no
  candidate's base condition is invalidated by this commit.
- **Seat collision.** `learning/orchestrator/` is occupied on `main` by one non-`SLR` record, on
  `orchestrator` by 11 `SLR-*` records, and on `orch-pipeline-loop-architecture` by one further
  non-`SLR` record based on the same `main` tip. This file's name collides with none of them, so
  a merge of any pair is a directory union rather than a conflict. **Directory-level convergence
  remains an open risk and is flagged, not solved.**
- 🔴 **This record is itself a tenth fragmented object**, written on a branch a reader standing on
  `main` will not find. That is F-3's thesis applied to the record about F-3, and it is recorded
  here rather than left for a later reader to discover.

---
record_type: PREPARATION_MEASUREMENT
record_id: LEGEND-PREP5-IMPACT-ANALYSIS-V1
task_id: PREP5_IMPACT_ANALYSIS_v1
title: Which parts of the LEGEND workflow require GOVERNED EXECUTION, and which do not
revision: 1
author: unregistered session — no role contract, no ACTOR_ID
actor_id: NOT ESTABLISHED — a session cannot resolve its own actorhood
dispatcher: operator
date: 2026-08-24
status: PREPARATION ONLY — OBSERVATION, NOT A DECISION
binding: NO
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none
creates_no_dec: true
chooses_no_outcome: true
proposes_no_implementation: true
governance_version: 3.1.1 — read and cited, neither exercised nor modified
lane: LANE-P · `PREP-5` of LEGEND_MINIMUM_DECISION_PATH_v1 § 3
feeds: OPS-DEC-02 — and it is the one preparation that can falsify § 5's reduction to two
activation_state_governing_this_record: >
  DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE returns OPTION B ACTIVATION_NOT_CONFIRMED.
  No authority in this record is traced to any role contract. None is claimed.
inputs:
  - learning/orchestrator/LEGEND_MINIMUM_DECISION_PATH_v1.md — the definition of PREP-5 (§ 3)
    and the falsifier this record tests (§ 5)
  - learning/orchestrator/LEGEND_FIRST_OPERATIONAL_TRIAL_DESIGN_v2.md — §§ 2, 3.4, 3.5, 8, 9, 13
  - learning/orchestrator/LEGEND_FIRST_OPERATIONAL_TRIAL_EXECUTION_PROTOCOL_v1.md — §§ 8, 8.1, 9, 10
  - governance/GOVERNANCE_v3.1.1.md annexes A, B, C, D, E, H, J · governance/plan_defined_parameters.md P5.1
  - framework/instruction/LEGEND_CORE.md · framework/state/state_manifest_current.md
  - the instrument surface: framework/scripts/, scripts/, .claude/settings.json
measured_at: >
  branch legend-operating-convention-v1 @ 30cb4f3fd700e2aaf6b608e363438f883ddc3760,
  working tree as found, 2026-08-24T14:39Z–14:46Z. Every figure in § 10 was executed in this
  session against this tree. Figures carried from another record are marked AS REPORTED and
  are never used to support a conclusion on their own.
domain: CONTENT — `learning/` is content by explicit intent (P5.1), not by omission
class: WORKING RECORD
self_note: >
  Writing this file makes the untracked planning corpus 13 files, measured at 12 immediately
  before it (2026-08-24T14:45:51Z). It is therefore inside the hazard readiness-plan D-1
  governs, and it proposes no commit of itself.
---

# PREP-5 · IMPACT ANALYSIS — governed execution vs rehearsal, clause by clause

> **This record measures. It creates no `DEC`, chooses no outcome, proposes no implementation,
> and changes no repository state beyond its own existence as an untracked file.**

---

## 0 · The four tags

| Tag | Means | Who may produce it |
|---|---|---|
| `OBS` | measured this session, with the command in § 10 that reproduces it | any session, no authority |
| `INF` | derived from `OBS` by reasoning; can be wrong; carries a falsifier | any session, no authority |
| `DEC` | a choice among available outcomes | **operator** — none is made here |
| `IMP` | an act that changes the repository or the runtime | only after the `DEC` that gates it |

Where this record calls something **blocking**, it means *no defined default state lets the
activity proceed with its stated output* — never that proceeding would be unwise.

---

## 1 · What was asked, and the two questions this answers

`PREP-5` is defined in `LEGEND_MINIMUM_DECISION_PATH_v1` § 3 as: *"Enumerate, clause by clause,
which parts of the trial design require a **governed** artifact and which do not."* Its stated
function is narrower than its description: it is **the measurement that can falsify § 5's
reduction** of five decision surfaces to a minimum set of two.

The dispatch widens the object from the trial to the whole LEGEND workflow — nine activity
classes. This record does both, in that order, because the wide answer is only defensible if the
narrow one is measured first:

1. **§ 3** — the 16 trial phases against the definition of "governed", one row each.
2. **§ 4** — the nine activity classes, in the format the dispatch specifies.
3. **§ 5** — the five specific questions.
4. **§ 6** — the falsifier verdict on `{OPS-DEC-01, OPS-DEC-02}`.

---

## 2 · The definition that had to be fixed before anything could be measured

`OPS-DEC-02` states the test itself: a **governed artifact** is one that *"cites a normative
status, enters the review ladder, or reaches `HUMAN_APPROVAL`."* Three criteria:

```
G-STATUS   the artifact claims a normative standing (status: line, binding clause)
G-LADDER   the artifact is a position on the Annex C ladder (R0…R5), or requires one
G-APPROVAL the artifact reaches the J.3 HUMAN_APPROVAL_QUEUE
```

`INF` **Applying those three to the trial exposed a fourth property that they do not capture, and
that the whole rehearsal/governed framing silently assumes away.** Two independent things have
been travelling under one word:

```
STATUS-GOVERNED   the artifact claims normative standing.        REHEARSAL removes this.
STATE-DURABLE     the artifact changes bytes a later reader
                  will treat as authoritative.                   REHEARSAL does NOT remove this.
```

`OBS` The proof is `Φ1b`, and it is not a corner case — it is the phase without which the trial
has no input. `framework/protocols/` and design v2 § 3.5 both record what
`fulltext_receipts.py record` writes, and reading the writer confirms it: it appends to
`disease-models/wwox/registries/fulltext_read_receipts.jsonl` (**tracked; 128 lines; hash-chained
through `ledger_prev_hash`**) and, in the same lock, re-anchors
`framework/state/state_manifest_current.md` (**tracked; the one state-control file writable
outside a `BATCH_COMMIT`**). Design v2 § 3.5 states it in the allowlist: *"`record` re-anchors it
IN-LOCK, on every append. **Not optional.**"*

`OBS` The receipt's `REQUIRED` field set is **14 fields, and none of them is an actor**:
`event_id · record_kind · study_id · event_at · analysis_at · workflow · evidence_depth ·
source_locator · source_fingerprint · coverage · outputs · evidence_basis · prior_receipt ·
reread_reason`. `record_kind` is validated against exactly three values —
`legacy_reconstruction`, `contemporaneous_receipt`, `receipt_invalidation` — and the 128 events
present use all three (22 / 105 / 1).

`INF` Two consequences, and the second is the sharper one:

- **A rehearsal cannot be expressed in the artifact it produces.** No `REQUIRED` field carries a
  run class; `record_kind` has no rehearsal value and adding one is a schema change, which the
  trial's own scope declares OUT (§ 3.4). The only place a rehearsal marker could go is
  `workflow`, a free-text field the validator constrains in no way — which makes the declaration
  a convention, not a property of the record. **Falsifier:** if the operator holds that a
  free-text `workflow` prefix is a sufficient declaration, this reduces to a naming convention
  and costs nothing.
- **A rehearsal receipt is byte-indistinguishable from an operational one**, and is
  unattributable by construction: the schema has no field in which a conferred `ACTOR_ID` could
  be recorded even if `OPS-DEC-01` conferred one.

This record therefore reports **two columns, not one**, for every activity below. Collapsing them
is the error that makes "rehearsal" sound like "writes nothing".

---

## 3 · The trial, clause by clause — 16 phases

`OBS` **Population, enumerated before it was measured:** design v2 § 9.1 carries **16** phase rows
(`Φ0 · Φ1a · Φ1b · Φ1c · Φ1d · Φ1e · Φ2 · Φ3 · Φ4 · Φ5 · Φ6 · Φ7 · Φ8 · Φ9 · Φ10 · Φ11`), counted
by matching `^| \*\*Φ` over the table's line range, not by eye. The execution protocol's artifact
index (§ 8.1) carries **14** artifact rows under a 15-line table body. The two documents differ in
row count because the protocol predates `Φ1e` and folds `Φ0`'s owner differently; **where they
differ, this record follows design v2, which is the later revision.**

| Φ | Artifact | G-STATUS | G-LADDER | G-APPROVAL | STATE-DURABLE (tracked) | Rehearsal-producible |
|---|---|---|---|---|---|---|
| Φ0 | `TRIAL-001-PREFLIGHT.md` | no | no | no | no — untracked `learning/` | ✅ |
| Φ1a | `…-ACQUISITION-DECLARATION.md` | no | no | no | no | ✅ |
| **Φ1b** | full text · **receipt** · digest | no | no | no | 🔴 **YES — 2 tracked files, one hash-chained** | ✅ but **not declarable in the artifact** |
| Φ1c | surface spec + manifest + frozen population | no | no | no | only under `SURFACE-FULL` | ✅ — see the actor-id note below |
| Φ1d | `…-LAYER-POPULATION.md` | no | no | no | no | ✅ |
| Φ1e | `…-ASSIGNMENT-CHECK.md` | no | no | no | no | ✅ |
| **Φ2** | Task Contract under `ledger/tasks/` | no | no | no | yes — control plane (P5.1) | ⚠️ **precedent exists, on a self-declared owner** |
| Φ3 | `HANDOVER` block | no | no | no | no | ✅ |
| Φ4 | receipt · manifest · dossier · locators | no | no | no | yes — tracked, non-canonical | ✅ |
| Φ5 | `RECEIPT-<arm>.json` freeze | no | no | no | no | ✅ — guarantee is procedural (§ 9.4) |
| Φ6 | `…-CHECK-LOG.md` · `…-LAYER-STATUS.md` | no | no | no | no | ✅ — runs committed validators read-only |
| Φ7 | `REV-TRIAL001-AUDIT-{1,2}` + act lists | no | **no** | no | yes — `reviews/` control plane | ✅ — auditors are *"ephemeral, unregistered, identity-withheld by design"* |
| **Φ8** | `REV-TRIAL001-R2-001` | no | 🔴 **YES — R2 is a ladder position** | no | yes — control plane | ⚠️ **the document yes; the ladder standing no** |
| **Φ9** | `REV-TRIAL001-MIRROR-*` | no | 🔴 **YES — R4 METHOD, and G.1 makes the trial `MIRROR_REQUIRED`** | no | yes — control plane | ⚠️ **findings yes; a governed verdict no** |
| Φ10 | `CC-TRIAL001-…` | no | no | no | yes — tracked, non-canonical proposal | ✅ |
| Φ11 | `…-OUTCOME-M/S.md` · friction log · SLR | no | no | no | no (SLR persists only via `WORK_COMMIT`) | ✅ |

**The count.** `OBS` **2 of 16** phases produce an artifact that is governed by the ladder criterion
(`Φ8`, `Φ9`). **0 of 16** reach `HUMAN_APPROVAL`. **0 of 16** write a canonical current file — the
trial stops at the candidate by design (`D-11(a)`), and `Φ10`'s own object is a proposal. **1 of
16** performs an unavoidable durable write into a hash-chained, canonical-adjacent surface
(`Φ1b`).

Three clauses need their own note, because a table row understates them.

### 3.1 · `Φ1c` — the only mechanized actor gate in the instrument surface

`OBS` `framework/scripts/benchmark_input_surface.py` declares `freeze --actor-id` as
`required=True`, with the help text *"checked against `ASSIGNMENT.md` in the tree; a disagreement
refuses"*; `locators --actor-id` is `required=True` too. The freeze reads its identity fields
**from the tree** (`ASSIGNMENT.md`, `BENCHMARK_INSTRUCTIONS.md`, `OUTPUT_SCHEMA.md`) and refuses
on mismatch.

`INF` This is an **identity-consistency** gate, not an **authority** gate. It verifies that the
string on the command line equals the string in the frozen tree; it never asks whether that string
resolves to a registered actor, and no registry is consulted. It is satisfiable by a rehearsal
that declares a name. **Falsifier:** if a resolution step exists elsewhere in the call path, this
is wrong — I found none, and the script consults no registry file.

`OBS` It fires only under `SURFACE-FULL`. Design v2 `D-5` recommends `SURFACE-LITE`, under which
`Φ1c` builds nothing and this gate never runs.

### 3.2 · `Φ8` — the clause that genuinely resists rehearsal

`OBS` `C.1` sets the floor for *"inferenza therapeutic-actionable"* at **`R2`**, and
*"derogabili solo verso l'ALTO; sotto il floor solo con rationale registrato"*. The execution
protocol § 8 fixes `R2` in advance for this trial, on the reasoning that *"C1q is druggable and
anti-C1q antibodies are in human trials, which makes any therapeutic-shaped inference `R2` by
C.1"*. The trial's own question (§ 3.3) asks *"what — if anything — transfers to a loss-of-function
neurodevelopmental context"*, so the class is live and not hypothetical.

`OBS` `C.3` opens with *"Apertura solo via Orchestrator"*; `G.2`'s independent reviewer is *chosen
by Orchestrator*; `lease_state.py` reports **`ACTIVE by derivation: 0`** (5 leases, 2 STALE,
3 RELEASED, last released 2026-08-18T14:05:20Z).

`INF` Under any branch, **no governed review can be opened today**, because the party that opens
it does not exist. Under `02 = REHEARSAL` this is not a defect but the declared state: `OPS-DEC-03`
outcome **(d)** — *no review is declared for this run* — is reachable, and the run's outcome record
must say so. Under `02 = GOVERNED`, `Φ8` is blocking and its release runs through `OPS-DEC-01`
first. **A third path exists and is not free:** `C.1` permits below-floor with a registered
rationale, but `H.1` assigns *"Livello Ladder (≥ floor) e reviewer"* to the Orchestrator — so
registering that rationale is itself an act with an author the laboratory does not have.

### 3.3 · `Φ2` — a required field the repository has always self-declared

`OBS` `A.1` requires `OWNER (ACTOR_ID)` in a `TASK_ASSIGNMENT`; `A.3` requires a durable claim
carrying `ACTOR_ID`; `A.6` requires `ACTOR_ID` in a checkpoint. `OBS` `ledger/tasks/` holds
**5 contracts, all under `plan/`**, and the one inspected carries `OWNER: "plan"` —
a seat name, self-declared. `ledger/checkpoints/` holds **19 checkpoints, all under `plan/`**,
`ACTOR_ID: "plan"`, all tracked on `main`. `OBS` `A.3`'s stated guarantee is *"unicità per
costruzione organizzativa — **single-assigner (Orchestrator)** + claim record durevole"*.

`INF` The precedent for producing these objects without a conferred actorhood is not hypothetical
— it is the entire existing population. What `OPS-DEC-01` decides is precisely whether that
self-declared string was legitimate, and it is asked **after** 24 such objects exist.

---

## 4 · The nine activity classes

Format as dispatched. `REHEARSAL POSSIBLE` asks whether the activity can be performed with its
output claiming no governed status. `GOVERNED REQUIRED` asks whether the activity's *stated
product* is unobtainable without it.

---

### 4.1 · RICERCA SCIENTIFICA — reading and analysing a source (`Φ4`)

```
REHEARSAL POSSIBILE?   YES
GOVERNED REQUIRED?     NO for the act · YES only for the resulting claim to be typed canonical
```

**REQUISITI MINIMI** — `ACTOR_ID` no · lease no · event ledger no · reviewer no (review is
downstream) · approval no · **durable state yes** (dossiers, deepdive manifests — tracked,
non-canonical).

`OBS` `framework/instruction/LEGEND_CORE.md` contains **0 occurrences of `ACTOR_ID` and 0 of
`lease`**. `H.1` assigns *"Conclusione scientifica"* to the *"Scientist responsabile (soggetta a
review, mai a ordine)"*. The state manifest reads `current_state: READY`, `deep_dive_gate: OPEN`,
`ingest_gate: OPEN`.

**DECISION DEPENDENCIES** — `OPS-DEC-02` only for whether the reading's *output* may claim governed
standing. Not gated by `OPS-DEC-01` unless the reading is committed (`IMP-1`).

**RISCHIO SENZA GOVERNANCE** — low and bounded. The reading's discipline is carried by instruments
that do not ask who is running them (`deepdive_manifest.py`, `locator_audit.py`,
`dossier_quote_audit.py`). The residual risk is attribution: a reading performed by nobody cannot
later be credited to anyone, and `C.2`'s `AUTHOR ≠ REVIEWER` rule needs distinguishable authors.

---

### 4.2 · PRODUZIONE EVIDENZE — receipts, surfaces, populations, freezes (`Φ1b · Φ1c · Φ1d · Φ5 · Φ6`)

```
REHEARSAL POSSIBILE?   YES — but 🔴 NOT DECLARABLE IN THE ARTIFACT (§ 2)
GOVERNED REQUIRED?     NO by any instrument — and the write happens either way
```

**REQUISITI MINIMI** — `ACTOR_ID` **not required and not accepted** by the receipt writer (14
`REQUIRED` fields, no actor field) · `--actor-id` **required** by `benchmark_input_surface.py
freeze`, as a consistency check only, and only under `SURFACE-FULL` · lease no · event ledger no ·
reviewer no · approval no · **durable state: MANDATORY** — two tracked files, one hash-chained,
on every `record`.

**DECISION DEPENDENCIES** — none that stand it down. `OPS-DEC-02` does not reach it: neither branch
suppresses the write. `OPS-DEC-01`'s outcome **(d)** (*"defer — the corpus stays untracked and the
run produces nothing durable"*) is **not achievable while `Φ1b` runs**, because `Φ1b` writes to
tracked files rather than to the untracked corpus. Either `Φ1b` does not run — and the trial has no
input — or something durable is produced and (d) is not what happened. *This is an observation
about an already-enumerated outcome, not a new decision surface.*

**RISCHIO SENZA GOVERNANCE** — the highest of the nine, and the least visible. The ledger grows by
an event that (i) is byte-indistinguishable from an operational one, (ii) names no author, (iii)
re-anchors the state manifest, and (iv) is chained, so it cannot be removed later without breaking
the chain — the repository's own rule is that hand-editing the ledger halts LEGEND until the edit
is undone or authorized and re-anchored. A rehearsal that is later disowned leaves a receipt that
cannot be disowned.

---

### 4.3 · REVIEW — audit, peer review, method review (`Φ7 · Φ8 · Φ9`)

```
REHEARSAL POSSIBILE?   YES for FINDINGS · NO for a LADDER VERDICT
GOVERNED REQUIRED?     YES — for any verdict that satisfies a C.1 floor
```

**REQUISITI MINIMI** — `ACTOR_ID` for the reviewer: **not required** (`C.2` needs a *distinguishable*
`REVIEWER`/`AUTHOR`/`ADJUDICATOR`, not a registered one) · **lease: REQUIRED to open** (`C.3`) ·
event ledger no (`J.1` lists `REVIEW_OPENED`/`REVIEW_CLOSED` as event types, and the ledger has
0 entries) · reviewer: by definition · approval no · durable state: yes, into `reviews/`, which
`P5.1` classes **control plane** — a review therefore does not move the candidate hash.

`OBS` The precedent is measured and it works: both reviews of the trial design itself were
performed *"by a hostile reviewer and a feasibility reviewer, never by Mirror and Plan, and both
said so themselves"* (design v2 § 8.2), and their findings are registered in two files in this
same directory. `OBS` `reviews/` on this branch holds `plan/` and **3 files, all
`AUTHOR-RESPONSE-*`** — no verdict lives here; `reviews/trial-001/` does not exist (`D-8`).

**DECISION DEPENDENCIES** — `OPS-DEC-03`, which fires only on `OPS-DEC-02 = GOVERNED` (or `MIXED`);
and `OPS-DEC-01`, because `C.3`'s opener and `G.2`'s chooser are the Orchestrator.

**RISCHIO SENZA GOVERNANCE** — a verdict recorded without an opener has independence that rests on
nothing measurable. `CP-3` (Mirror structurally unreviewable, three independent grounds) and
`CP-5` (a `REQUEST CHANGES` from the sole reviewer is operationally a block) are the two shapes
this failure has already taken, AS REPORTED by the Mirror analysis.

---

### 4.4 · CANDIDATE GENERATION (`Φ10`) — two objects that must not be conflated

```
SCIENTIFIC COMMIT CANDIDATE      REHEARSAL POSSIBILE? YES   GOVERNED REQUIRED? NO
GOVERNANCE INTEGRATION_CANDIDATE REHEARSAL POSSIBILE? NO    GOVERNED REQUIRED? YES
```

**REQUISITI MINIMI (scientific)** — none of `ACTOR_ID` / lease / ledger / reviewer / approval.
Durable state: a tracked, non-canonical proposal file.

**REQUISITI MINIMI (governance)** — `H.1` assigns *"Integrazione strutturale / candidate"* to Plan;
`D.2` requires `CANDIDATE_ID / BASE_HEAD / SOURCE_COMMITS / CANDIDATE_CONTENT_HASH / CHANGE_CLASS /
LINT_RESULT / MIRROR_REVIEW / HUMAN_APPROVAL / SNAPSHOT_ID`; MAJOR ⇒ `HUMAN_APPROVAL` (J.3).

`OBS` Re-derived at this head over the **16** `CC-*` files: `MIRROR_REVIEW` **0 of 16** ·
`CHANGE_CLASS` **0 of 16** · `HUMAN_APPROVAL` **0 of 16** · `CANDIDATE_CONTENT_HASH` **0 of 16** ·
positive control `COMMIT CANDIDATE` **15 of 16**. `OBS` `governance/candidates/` holds 16 entries:
8 `CAND-*`, 4 `HANDOFF-*`, and one each of `PROPOSAL/ADVISORY/APPROVAL/DELTA`.

`INF` The two candidate classes have disjoint field sets and disjoint gates. The trial produces the
scientific one only. This confirms `B-10`'s correction — the gate on the canonical route is not
`MIRROR_REVIEW`, which no scientific candidate has ever carried.

**DECISION DEPENDENCIES** — none for the scientific object. The governance object is `Φ10`-adjacent
but outside the trial: design § 3.4 declares *"any governance amendment · any PROPOSAL
implementation · any schema change"* OUT of scope.

**RISCHIO SENZA GOVERNANCE** — negligible at this step, because a candidate is a proposal. The
hazard is entirely in the next activity.

---

### 4.5 · CHECKPOINT (`A.6`)

```
REHEARSAL POSSIBILE?   YES — and it is the established practice
GOVERNED REQUIRED?     the FIELD is required; the CONFERRAL is enforced by nothing
```

**REQUISITI MINIMI** — `ACTOR_ID` **required by the schema** · `APPLICABLE_GOVERNANCE_FINGERPRINT`
required (`H.1`: composition is Plan's, a *governed* modification) · lease no · event ledger:
`J.1` names `CHECKPOINT_WRITTEN` as an event type, and the ledger has 0 entries, so the event is
not written · reviewer no · approval no · durable state yes, control plane.

`OBS` 19 checkpoints exist, all `ACTOR_ID: "plan"`, all tracked on `main`, carrying a real
`APPLICABLE_GOVERNANCE_FINGERPRINT` and `GOVERNANCE_VERSION: 3.1.1`.

**DECISION DEPENDENCIES** — `OPS-DEC-01`, directly: the checkpoint's whole function (`A.4`
anti-zombie, `A.6`'s refusal rule) presumes `ACTOR_ID` names a distinguishable party.

**RISCHIO SENZA GOVERNANCE** — two sessions writing `ACTOR_ID: "plan"` are indistinguishable to
`A.4`'s rehydration check, and `A.3`'s uniqueness guarantee is explicitly *"per costruzione
organizzativa — single-assigner (Orchestrator)"*, whose subject does not exist. The compensating
protocol is named in `J.0` and its precondition is absent.

---

### 4.6 · COMMIT — three kinds, and the layer disagreement

```
WORK_COMMIT               REHEARSAL POSSIBILE? NO — H.1 says "ogni ATTORE"   GOVERNED REQUIRED? YES
INTEGRATION_CANDIDATE     REHEARSAL POSSIBILE? NO                            GOVERNED REQUIRED? YES (Plan)
CANONICAL_BATCH_COMMIT    REHEARSAL POSSIBILE? NO                            GOVERNED REQUIRED? YES, unconditionally
```

**REQUISITI MINIMI (canonical)** — `D.1`: *"solo Orchestrator, root, gate 0–5"*. `D.3` GATE 0:
`BASE_HEAD == atteso · root clean · GOVERNANCE_VERSION corretta · **lease ACTIVE singleton** ·
ONE_WRITER`. One FAIL → `NO BATCH, BLOCKED_BY_GOVERNANCE`. `OBS` `ACTIVE by derivation: 0`.

`INF` **`CANONICAL_BATCH_COMMIT` is unavailable under *both* branches of `OPS-DEC-02`** — not
because the run is a rehearsal, but because `GATE 0` has an unsatisfied clause that only
`OPS-DEC-01` can reach. The trial already stops short of it (`D-11(a)`), for exactly this reason.

**🔴 The finding this activity carries, and no prior record in this corpus states.** `OBS`, in five
measurements with their controls:

| Measured | Result | Control |
|---|---|---|
| `LEGEND_CORE.md` mentions of `ACTOR_ID` / `lease` | **0 / 0** | the file is 300+ lines of commit law |
| state manifest gates | `current_state: READY` · `deep_dive_gate: OPEN` · `ingest_gate: OPEN` · **`batch_commit_gate: OPEN`** | — |
| scripts under `framework/scripts/` + `scripts/` mentioning `lease` as a word (not inside *release*) | **1 — `lease_state.py` itself** | `public_release_gate` is referenced by 9 files; an enforced gate has callers |
| `legend_lint.py` mentions of `batch_commit_gate` / `deep_dive_gate` / `current_state` / `lease` | **0 / 0 / 0 / 0** | same file: `BLOCK` 51, `CURRENTS` 6 |
| `batch_commit.py` mentions of `lease` / `actor` / `governance` / `Annex` | **0 / 0 / 0 / 0** | the file is 63 lines and is *"a mechanical helper for the backup/restore phases"* |
| `.claude/skills/legend-commit/SKILL.md` mentions of `lease` / `ACTOR_ID` / `Annex D` / `GATE 0` / `governance` | **0 × 5** | same file: `BATCH_COMMIT` 3 |

`INF` **The framework layer says GO; the governance layer says NO BATCH; and no code connects
them.** The prohibition on canonical writes is entirely procedural. A session running the
documented LEGEND pipeline today would pass every automated check the framework knows how to run
and would write the four current files, never encountering the gate that forbids it. `LEGEND_CORE`
§ 21b's own blocking string — `FULL STATE NOT AVAILABLE — COMMIT BLOCKED` — enumerates six
conditions, and *"no ACTIVE lease"* is not among them, because it is a condition that layer does
not know exists.

*Counter-evidence, stated because it defeats the obvious objection.* `OBS` One mechanized write
guard does exist: `.claude/settings.json` registers a `PreToolUse` hook on `Bash` running
`scripts/guard_bash_command.py` (125 lines). `OBS` It denies exactly two things — blanket staging
and inline-heredoc repository writes — and contains **0 occurrences of `lease`, `ACTOR`,
`governance`, `current_state` or `working_model_current`**. It governs *how* a write is made, never
*who* may make it or *what* it may touch. It does not compensate.

`OBS` Corroboration, AS REPORTED and not relied upon: a Plan checkpoint on another worktree
(`CHK-plan-0019`) recorded independently *"lease_state.py has no location predicate; batch_commit.py
is snapshot/restore only; no script anywhere constrains a lease row's write surface; GATE 0 is
asserted by hand."* This record re-derived it rather than carrying it.

**DECISION DEPENDENCIES** — `OPS-DEC-01` for `WORK_COMMIT` (`IMP-1`) and for `GATE 0`. Not
`OPS-DEC-02`: no run class makes a canonical write available.

**RISCHIO SENZA GOVERNANCE** — the only activity of the nine where the risk is not procedural
embarrassment but corruption of the scientific baseline: the four current files change with no
lease, no approval, no attributable actor, and every downstream reader treats the result as
canonical. **This risk is present today, independent of the trial, and independent of both
decisions.**

---

### 4.7 · LEARNING LOOP (`Annex E`)

```
REHEARSAL POSSIBILE?   YES for OBSERVED / LOCAL / the Session Learning Record
GOVERNED REQUIRED?     YES for PROMOTED — and PROMOTED is currently unreachable for a
                       structural reason that neither decision touches
```

**REQUISITI MINIMI** — `E.2` requires `ORIGIN_ACTOR` and `CONFIRMATION_CLASSES: {actor, session,
class}` · `E.6` requires `ACTOR_ID` and persists *"via `WORK_COMMIT` alla granularità delle
milestone"* ⇒ `OPS-DEC-01` · lease no · event ledger: `J.1` names `LEARNING_PROMOTED`, 0 entries ·
reviewer: Mirror holds *"cura epistemica"*, Plan *"durevolezza"* · approval no.

`OBS` `E.2`: *"Contano pienamente solo `ORIGINAL_OBSERVATION` e `REPLICATION`"*; threshold is
*"≥2 conferme delle prime due classi, o 1 + validazione Mirror"*. `OBS` `active_lessons/` **does
not exist** on disk, and `CLAUDE.md` says so itself: *"not yet materialized"*.

`INF` With one seat and no registered actors, `REPLICATION` across distinct actors is unavailable
by construction, and the fallback — *1 + Mirror validation* — routes through the review activity,
whose opener is missing. **The learning loop can record and cannot promote, in either branch of
`OPS-DEC-02`.** That is a standing structural limit, not a decision, and it should not be counted
as an argument for either branch.

**RISCHIO SENZA GOVERNANCE** — a lesson confirmed by one actor observing itself repeatedly is
`EXPOSURE_AFTER_BROADCAST` wearing `REPLICATION`'s clothes, which `E.2` explicitly discounts.

---

### 4.8 · GOVERNANCE UPDATE

```
REHEARSAL POSSIBILE?   NO — there is no such thing as a rehearsal amendment to a FROZEN file
GOVERNED REQUIRED?     YES, unconditionally, and by the operator
```

**REQUISITI MINIMI** — `H.1`: *"Spese / MAJOR approval / **governance**"* → Operatore ·
`H.2`: macro-upgrade → version increment + `GOVERNANCE_UPDATE` with ACK; mismatch on an area →
assignments suspended · `G.1` classes a normative protocol binding every actor as
`MIRROR_REQUIRED`/MAJOR · `J.3` routes MAJOR to the operator, and *"APPROVAL ≠ AUTHORIZATION"*.

`OBS` `git grep "^status:" main -- governance/` returns **11 `FROZEN`** plus one each of several
`PROPOSED` variants; `roles/` returns **4 identical `PROPOSED — binding once Mirror hostile review
passes and the operator approves`**.

**DECISION DEPENDENCIES** — none of `OPS-DEC-02`'s. This activity answers to operator authority
directly, and design v2 § 3.4 puts it **OUT of the trial's scope explicitly**, together with any
schema change and any write to `governance/`, `roles/`, `framework/protocols/`,
`framework/scripts/`.

**RISCHIO SENZA GOVERNANCE** — largest blast radius, lowest current probability, because nothing in
the trial reaches it. The measured pathology here is the opposite of over-reach: `OBS` the
approval queue holds 6 lines, of which 2 carry an `APPROVAL_ID` (`GOV311-001` MAJOR PENDING,
`GOV311-002` GOVERNANCE PENDING, both `REQUESTED_BY: plan`), and **0 mention XPORT or SCIAB** —
reviewed protocols sitting one operator act from binding, with the act never requested.

---

### 4.9 · CROSS-SESSION HANDOFF (`Annex B` + `XPORT`)

```
REHEARSAL POSSIBILE?   YES — and it is already what happens, including for this dispatch
GOVERNED REQUIRED?     only if a message body is treated as authoritative payload
```

**REQUISITI MINIMI** — `B.1` envelope: `MESSAGE_ID / TASK_ID / **ACTOR_ID (identità)** / FROM / TO /
TYPE / STATE_CHANGE / DURABLE_POINTER` · `B.3`: ACK mandatory on `STATE_CHANGE: yes` · lease no ·
event ledger no · reviewer no · approval no · durable state: `XPORT`'s whole rule is that the
durable artifact, not the message, is the payload.

`OBS` `framework/protocols/cross_session_transport.md` is `status: PROPOSED — binding once Mirror
hostile review passes and the operator approves`, `enforcement_mode: PROCEDURAL — …No mechanism in
this protocol runs between turns.` AS REPORTED: `REV-XPORT-MIRROR-002` returned `ACCEPT`; the
approval queue contains 0 occurrences of `XPORT`.

**DECISION DEPENDENCIES** — `OPS-DEC-04`, which the minimum decision path classes as conditional:
it gates the run only on `02 = GOVERNED` **and** the run routing authoritative payload between
sessions. Decidable at any time; a defined default exists (undeclared, binding nobody).

**RISCHIO SENZA GOVERNANCE** — highest probability, lowest visibility of the nine. Two shapes, both
already observed in this corpus: a payload that rides in a message body and is never anchored to a
repository object — *"a payload whose completeness the recipient cannot establish"*, in the
protocol's own words; and a dispatch delivered to a session that is not the actor it is addressed
to — design v2 § 8.2 measured that the registry's bindings for both review seats named sessions
**not among the 14 live peers** at dispatch time.

---

## 5 · The five questions, answered

**1 · Which activities can continue without `ACTOR_ID`?**

`INF` All of: scientific reading · evidence production · findings-only review (audit, hostile,
feasibility) · scientific candidate generation · outcome and friction records · cross-session
notification. `OBS` The empirical proof is this corpus: 13 untracked planning records, two review
findings registers, two protocol reviews, 19 checkpoints and 5 task contracts were all produced
under exactly the present state. **What cannot continue without it:** `WORK_COMMIT` (`H.1`: *"ogni
attore"*), anything through `GATE 0`, and — as a *field*, not as a conferral — checkpoints and task
contracts.

**2 · Which activities produce only evidence, and which produce LEGEND state?**

```
EVIDENCE ONLY (no tracked write, or a tracked non-canonical proposal)
    Φ0 · Φ1a · Φ1d · Φ1e · Φ3 · Φ5 · Φ6 · Φ11 · dossiers and manifests (Φ4) · CC-* (Φ10)

CONTROL-PLANE STATE (tracked; P5.1 says it does not constitute the candidate)
    Φ2 task contracts · checkpoints · Φ7/Φ8/Φ9 review artifacts under reviews/

🔴 LEGEND STATE (tracked, canonical or canonical-adjacent)
    Φ1b — fulltext_read_receipts.jsonl (hash-chained) + state_manifest_current.md (re-anchored)
    the four current files — reachable ONLY through a BATCH_COMMIT that GATE 0 currently refuses
```

`INF` The line falls in an unexpected place: **the only activity in the trial that writes LEGEND
state is the one that acquires the paper**, and it is the first substantive phase rather than the
last.

**3 · Which activities require attributed authority?**

`INF` Three, and only three: **`CANONICAL_BATCH_COMMIT`** (`D.3` GATE 0, `lease ACTIVE singleton`)
· **opening any review at a `C.1` floor** (`C.3`, `G.2` — Orchestrator opens and chooses) ·
**any governance amendment** (`H.1` → operator). Everything else requires an *identity* at most —
a string that distinguishes one party from another — which is a weaker thing than conferred
authority and is what the repository has been using for 24 control-plane objects.

**4 · What is the minimum needed to continue development without declaring LEGEND operational?**

`INF` **Nothing that does not already exist**, with one qualification and one act that costs
nothing:

- the qualification: `Φ1b`'s durable write happens anyway, and cannot declare itself a rehearsal
  in its own schema. Continuing without deciding means accepting that the receipt ledger grows
  with unattributable, undeclarable events;
- the act: `Φ−1a` — copying the untracked corpus out of the repository, byte for byte. It needs no
  authority, no git act and no decision, and it is the only preservation 13 files currently have.

`OBS` `LANE-P` of the minimum decision path lists seven preparations, all of which need no
authority. This record discharges one of them.

**5 · What is the minimum needed to declare LEGEND operational?**

`INF` Three conditions, and the third is the one this record adds:

1. **`OPS-DEC-01` answered** — a party entitled to write durable state. Without it `GATE 0` cannot
   pass and no review can be opened, which removes commit and governed review together.
2. **`OPS-DEC-02` answered** — because "operational" is a claim about the status of what the
   laboratory produces, and `DEC-20260822` forbids an actor from settling it.
3. 🔴 **The two layers reconciled on the commit gate.** As measured in § 4.6, "operational" today
   would mean a system whose canonical write path is forbidden by governance and permitted by
   every instrument that actually runs. Declaring operational status over that gap does not close
   it; it makes the gap load-bearing. *Whether to close it by mechanizing the gate, by narrowing
   the claim, or by declaring the residue — is the operator's, and this record proposes none of
   the three.*

---

## 6 · The falsifier verdict

The minimum decision path § 5 states the falsifier for its own reduction:

> *"If the operator wants an artifact the rehearsal branch cannot produce — a canonical claim, a
> governed review verdict, a candidate that reaches `HUMAN_APPROVAL` — then `02 = REHEARSAL` is
> unavailable and the reduction fails: `D1`, `D3` and `D5` collapse back into three separate
> decisions and the minimum set becomes four."*

`OBS` Measured against the 16 phases: **canonical claim — 0 of 16** phases write one, and `D-11(a)`
stops the trial at the candidate. **`HUMAN_APPROVAL` — 0 of 16** phases produce a queue object.
**Governed review verdict — 2 of 16** (`Φ8` at `R2`, `Φ9` at `R4`), and both are ladder positions
by construction.

`INF` **The reduction to `{OPS-DEC-01, OPS-DEC-02}` SURVIVES, conditionally.** The condition is
that the two ladder verdicts stand down — which is `OPS-DEC-03` outcome **(d)**, reachable only
under `02 = REHEARSAL`, exactly as § 5 described. Nothing measured here forces a fourth decision.

Three qualifications, in descending order of how much they should change the reading:

1. **The reduction is on the status axis and silent on the durability axis.** `{01, 02}` is
   complete for *what an artifact may claim*. Neither decision reaches `Φ1b`, the one write that
   happens in both branches, is unattributable by schema, and is chained. This does not add a
   decision — it narrows what answering the two decisions will have accomplished.
2. **What `OPS-DEC-02` reduces *to* was already routed to the operator under other identifiers.**
   `02 = REHEARSAL` holds only if design v2's `D-4` (unregistered rehearsal claiming no actorhood)
   and `D-11` (stop at the candidate) resolve as the design recommends. Both are operator
   decisions in a table of 14. `OPS-DEC-02` is the same fork seen at a higher altitude, not an
   additional one — and answering it answers `D-4` and `D-11` implicitly, which is worth doing
   deliberately rather than by inheritance.
3. **`Φ8`'s floor has a third path, and it is not free.** `C.1` permits going below `R2` with a
   registered rationale, but `H.1` gives the ladder level and the reviewer to the Orchestrator. A
   below-floor rationale is therefore an act with an author the laboratory does not have — so the
   third path routes back through `OPS-DEC-01` rather than around it.

---

## 7 · Where this record could be wrong

1. **The `governed` definition is mine to the extent of the fourth property.** `G-STATUS`,
   `G-LADDER` and `G-APPROVAL` come from `OPS-DEC-02`'s own text; **`STATE-DURABLE` does not.**
   If the operator holds that "governed" means status only, § 2 and § 6's first qualification
   fall, and the analysis reduces to the 2-of-16 count. *That reading does not make `Φ1b`'s write
   stop happening; it makes it not the subject of this decision.*
2. **The layer disagreement is measured as an absence, and absences have denominators.** The
   sweep covered `framework/scripts/` and `scripts/` — **not** `governance/scripts/`, `.claude/`
   beyond `settings.json` and the `legend-commit` skill, nor the other worktrees under
   `.claude/worktrees/`. A lease-aware enforcement point outside that population would refute
   § 4.6. Each negative in that table carries its positive control, which is what makes the
   absences readable rather than merely unobserved.
3. **`Φ1c`'s actor gate was read, not executed.** I read `required=True` and the help text; I did
   not run `freeze` and watch it refuse. If the flag is consumed differently at runtime, § 3.1 is
   wrong in its detail — though not in its conclusion, since the check is against a file in the
   tree either way.
4. **The two trial records disagree on their own phase count** (16 vs a 14-row artifact index),
   and I followed the later one. If the protocol's index is the operative list, one row of § 3 is
   surplus and none is missing.
5. **`D5`'s independence figures are still `AS REPORTED`.** This record did not re-derive 39/39,
   25/30 or ~29/36 — that is `PREP-4`'s job and it has not been run. Nothing in § 6 rests on them.

---

## 8 · What this record does not do

It creates no `DEC` and appends to no queue. It chooses no outcome and carries no recommendation
column. It proposes no code, no schema, no protocol, no normative file and no repository change.
It activates nothing, confers nothing, opens no review, assigns no owner, resolves no finding, and
promotes no capability. It does not modify `governance/`, `roles/`, `framework/`, `ledger/`,
`runtime/`, `reviews/` or the four scientific current files. It stages nothing and commits nothing,
itself included. It writes **no** loose git objects. It touches no untracked file: the 12 records
present at 14:45:51Z are unmoved, unrenamed, undeleted and unstaged, and this is the 13th.

It does not declare `{OPS-DEC-01, OPS-DEC-02}` to be the right decision set. It reports that the
measurement asked for does not falsify it, and states the three qualifications that a reader should
weigh before treating "survives" as "confirmed".

---

## 9 · Verification trail

All at `legend-operating-convention-v1` @ `30cb4f3fd700e2aaf6b608e363438f883ddc3760`,
2026-08-24T14:39Z–14:46Z, working tree as found.

| # | Check | Command | Result |
|---|---|---|---|
| 1 | Lease state | `python3 framework/scripts/lease_state.py` | `ACTIVE by derivation: 0`; 5 leases, 2 STALE, 3 RELEASED |
| 2 | Refs | `git for-each-ref \| wc -l` | 57 |
| 3 | Untracked corpus | `git status --porcelain \| grep -c '^??'` | **12**, at 14:45:51Z, before this file existed |
| 4 | Framework layer knows no actor | `grep -c "ACTOR_ID\|lease" framework/instruction/LEGEND_CORE.md` | **0** |
| 5 | Manifest gates | `grep -n "gate\|current_state" framework/state/state_manifest_current.md` | `READY` · `deep_dive_gate: OPEN` · `ingest_gate: OPEN` · **`batch_commit_gate: OPEN`** |
| 6 | Lease-aware scripts | `grep -rlE "(^\|[^r])lease\|_lease\|lease_" framework/scripts/ scripts/`, then printing each file's matched tokens to strip *release* | **1 file: `lease_state.py`** — every other hit was the substring inside *release* |
| 6b | — positive control | same population, token `public_release_gate` | referenced by **9** files: an enforced gate has callers |
| 7 | LINT gate awareness | `grep -c` on `legend_lint.py` for `batch_commit_gate` · `deep_dive_gate` · `current_state` · `lease` | **0 · 0 · 0 · 0** — control on the same file: `BLOCK` 51, `CURRENTS` 6 |
| 8 | `batch_commit.py` | `grep -c` for `lease` · `actor` · `governance` · `Annex`; `wc -l`; docstring | **0 · 0 · 0 · 0**; 63 lines; *"Mechanical helper for the BATCH_COMMIT backup/restore phases"* |
| 9 | Commit skill | `grep -c` on `.claude/skills/legend-commit/SKILL.md` for `lease` · `ACTOR_ID` · `Annex D` · `GATE 0` · `governance` | **0 × 5** — control on the same file: `BATCH_COMMIT` **3** |
| 10 | The one mechanized write guard | `.claude/settings.json` → `PreToolUse`/`Bash` → `scripts/guard_bash_command.py`; `grep -c` for `lease` · `ACTOR` · `governance` · `current_state` · `working_model_current` | 125 lines, denies blanket staging + inline-heredoc writes; **0 × 5** on authority tokens |
| 11 | Receipt schema | `sed -n '85,120p' framework/scripts/fulltext_receipts.py` | 14 `REQUIRED` fields, **no actor field**; `record_kind` ∈ 3 values |
| 12 | Receipt ledger | `wc -l` on `fulltext_read_receipts.jsonl`; `record_kind` histogram | **128** events: 105 contemporaneous · 22 legacy · 1 invalidation |
| 13 | Freeze actor gate | `grep -n "actor-id" framework/scripts/benchmark_input_surface.py` | `freeze --actor-id required=True`, *"checked against ASSIGNMENT.md in the tree; a disagreement refuses"*; identity read **from the tree**, no registry consulted |
| 14 | Scientific candidates | `ls …/commit_candidates/` → 16 `CC-*` + 1 `PROPOSAL`; `grep -l` per token over the 16 | `MIRROR_REVIEW` **0/16** · `CHANGE_CLASS` **0/16** · `HUMAN_APPROVAL` **0/16** · `CANDIDATE_CONTENT_HASH` **0/16** · control `COMMIT CANDIDATE` **15/16** |
| 15 | Governance candidates | `ls governance/candidates/ \| sed -E 's/^([A-Z]+)-.*/\1/' \| sort \| uniq -c` | 16 = 8 `CAND` · 4 `HANDOFF` · 1 each `PROPOSAL/ADVISORY/APPROVAL/DELTA` |
| 16 | Task contracts | `find ledger/tasks -type f` | **5**, all under `plan/`; `OWNER: "plan"`, self-declared |
| 17 | Checkpoints | `find ledger/checkpoints -type f`; `git ls-tree -r main -- ledger/` | **19**, all `plan/`, all tracked; `ACTOR_ID: "plan"` + real fingerprint |
| 18 | Reviews on this branch | `ls reviews/plan` | **3**, all `AUTHOR-RESPONSE-*`; `reviews/trial-001/` absent |
| 19 | Approval queue | `wc -l`; per-line key dump | **6** lines: 2 `APPROVAL_ID` (`GOV311-001` MAJOR PENDING, `GOV311-002` GOVERNANCE PENDING, both `REQUESTED_BY: plan`), 2 resolutions, 1 correction, 1 schema header |
| 20 | Status populations | `git grep -h "^status:" main -- governance/` · `-- roles/` | governance: **11 FROZEN** + PROPOSED variants; roles: **4** identical PROPOSED |
| 21 | `active_lessons/` | `ls active_lessons` | **No such file or directory** |
| 22 | Phase population | `grep -c '^\| \*\*Φ'` over design v2 § 9.1's line range | **16** rows; ids listed in § 3 |
| 23 | Artifact index | `grep -c '^\| '` over protocol § 8.1's line range | 15 lines = 1 header + **14** artifact rows |
| 24 | `learning/` domain | `sed -n '238,300p' governance/plan_defined_parameters.md` | `CONTROL_PLANE_ROOTS` = `governance/candidates/`, `ledger/`, `reviews/`; *"`learning/` is CONTENT — by intent, not by omission"* |

---

CURRENT STATE:
OBSERVED

NEXT OPERATOR DECISION:
REQUIRED

No DEC created.
No implementation proposed.

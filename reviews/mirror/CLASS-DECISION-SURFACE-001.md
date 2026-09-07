---
artifact: DECISION SURFACE CLASSIFICATION REPORT
record_id: CLASS-DECISION-SURFACE-001
author: mirror
authored_on: 2026-08-23
dispatcher: operator
governance_version: 3.1.1 (read, not exercised)
mode: ANALYSIS_ONLY

STATUS: READ_ONLY_CLASSIFICATION
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none

classification:
  - OBJECT CLASSIFICATION ONLY
  - NOT A DECISION
  - NOT A DEC
  - NOT A CAND
  - NOT A MERGE, NOT A MERGE AUTHORIZATION
  - NOT A CANONICAL PATH DECLARATION
  - NOT A SCHEMA MODIFICATION
  - NO NEW VOCABULARY — every class name below is quoted from an existing artifact or annex

domain: >
  CONTROL PLANE. `reviews/` is a declared CONTROL_PLANE_ROOT in
  `governance/plan_defined_parameters.md` § P5.1 **at `main`** (`legend-candidate-v4`). Writing
  this file therefore moves no CANDIDATE_CONTENT_HASH computed against `main`.
  🔴 The branch this file is written on (`mirror`) carries a STALE § P5: `legend-candidate-v3`,
  CONTROL_PLANE_ROOTS = { `governance/candidates/`, `ledger/` } — `reviews/` absent. Every domain
  statement in this report is measured at `main`, never at this branch. See § 2.5.

verdict_note: >
  🔴 NO VERDICT TOKEN IS EMITTED. The only canonical VERDICT vocabulary is Annex C.2's —
  CONFIRMED | WEAKENED | REFINED | REFUTED — and its OBJECT is a review of a claim id /
  CANDIDATE_CONTENT_HASH / directive id. This is a classification artifact, not a C.2 review, and
  it emits no verdict rather than inventing one. See F-9, which is about exactly this.
---

# DECISION SURFACE — CLASSIFICATION REPORT

> **Nothing is decided. Nothing is chosen. Nothing is reconciled.**
> This report classifies the governance objects that currently exist and states which of them
> have a normative class, a normative storage surface and a normative writer. Where the answer is
> "none", it says so and stops.

---

## 0 · OBSERVATION SCOPE AND METHOD

```
OBSERVATION INSTANT   2026-08-23, this session
ACTING WORKTREE       .claude/worktrees/mirror
BRANCH                mirror        da52ee5e9d3e6eb66455c61d422c4fb1d0e21391
                      🔴 65 commits behind main · 77 ahead · merge-base 908197ba
CANONICAL main        788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5    OBSERVED, NOT MOVED
REFS SWEPT            43 refs/heads · 4 refs/remotes · 5 refs/tags
```

**The normative corpus**, for every "is this defined?" question in this report, is exactly:

```
governance/GOVERNANCE_v3.1.1.md      the body
governance/annex_a … annex_j         the ten FROZEN annexes
governance/plan_defined_parameters.md  the seven delegated values (P1–P7)
framework/**  ·  roles/**  ·  ARCHITECTURE.md  ·  BOOTSTRAP.md  ·  AGENTS.md  ·  CLAUDE.md
```

read **at `main`**. Nothing under `governance/candidates/`, `governance/decisions/`, `reviews/`,
`ledger/` or `learning/` is treated as normative for the purpose of answering whether a class is
defined — that is the question under examination, and admitting those artifacts as evidence of
their own authority is the circularity this report exists to break.

**Negatives carry positive controls.** Every "absent" below was measured in the same invocation
as a control string known to be present, after the known zsh word-splitting fault that returns
`ABSENT` on every ref.

🔴 **Two negatives in this report are falsified by this report's own existence.** Reproduce them
with this file excluded:

```bash
# F-1 — governance/decisions/ has no normative mention
git grep -n -iE "governance/decisions|record_type: *OPERATOR_DECISION" main \
  -- 'governance/GOVERNANCE_v3.1.1.md' 'governance/annex_*.md' \
     'governance/plan_defined_parameters.md' 'framework/**' 'roles/**'
# → 0 hits.  Control: HUMAN_APPROVAL_QUEUE over the same scope → 3 hits.

# F-12 — DEC-20260823-SURFACE-MAP-QUEUE-CLOSURE exists only as a citation
git grep -l 'DEC-20260823' $(git for-each-ref --format='%(refname:short)' refs/heads) \
  -- ':!reviews/mirror/CLASS-DECISION-SURFACE-001.md'
# → 1 file.  Control: DEC-20260822 → 14 refs.
```

---

## 1 · OBJECT INVENTORY

Ordered by whether the class is defined, not by frequency. **Frequency is not canonicity**: the
most numerous object below has the weakest normative basis.

---

### 1.1 · OBJECT: `CANDIDATE MANIFEST` (`CAND-*`)

```
OBJECT                  INTEGRATION_CANDIDATE manifest
CLASS                   DEFINED
CURRENT LOCATIONS       governance/candidates/CAND-*.md  — 9 distinct manifests across 43 heads
NORMATIVE BASIS         Annex D.1 (the three commit types) · Annex D.2 (the manifest field list)
                        · Annex H.1 row "Integrazione strutturale / candidate | Plan"
IS THE CLASS DEFINED?         YES — D.2 enumerates the fields
IS THE STORAGE SURFACE DEFINED?  NO — no annex names a path. `governance/candidates/` is named in
                              normative text exactly once, in § P5.1, and only as a
                              CONTROL_PLANE_ROOT prefix for hash exclusion
IS THE WRITER DEFINED?        YES — Plan, by H.1
```

---

### 1.2 · OBJECT: `HUMAN_APPROVAL_QUEUE` entry (`APR-*` / `RES-*` / `COR-*`)

```
OBJECT                  queue object created by a HUMAN_REQUIRED
CLASS                   DEFINED, PARTIALLY
CURRENT LOCATIONS       ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl
                        🔴 THREE divergent blobs across 30 of 52 content refs:
                           20c24a2ba478   6 lines   27 refs incl. main and mirror
                           bb603d9a270b  10 lines    1 ref   refs/heads/orchestrator
                           95fc81639014  14 lines    2 refs  evidence-index,
                                                             p51c9-rebased-onto-c89c2217
NORMATIVE BASIS         Annex J.3 (fields + STATE enum + rules) · body § 4 line 130
                        ("ogni HUMAN_REQUIRED genera un oggetto durevole nella
                        HUMAN_APPROVAL_QUEUE — mai solo un messaggio") · body § 12 GATE 3
IS THE CLASS DEFINED?         YES for the record shape — see § 3 for what inside it is frozen
IS THE STORAGE SURFACE DEFINED?  NO. The string `ledger/approvals` appears ZERO times in the
                              normative corpus. It is named only by
                              governance/candidates/CAND-20260816-GOV311.md,
                              governance/candidates/APPROVAL-GOV311-DEVIATIONS.md,
                              governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md
                              and learning/orchestrator/SCIENTIFIC-PIPELINE-PREPARATION-001.md —
                              i.e. only by artifacts that use it
IS THE WRITER DEFINED?        🔴 NO. H.1 assigns "Classificazione HUMAN_REQUIRED ordinaria" to
                              Orchestrator — that is the classifier, not the writer. Observed
                              writers: `plan` (lines 2,4,6 and HA-1…HA-4), `orchestrator`
                              (lines 7–10, each self-labelled "WORK_COMMIT on the orchestrator
                              branch, not a canonical write"), `operator` (resolutions).
                              J.1's one-writer requirement is written for the EVENT ledger, and
                              § P7 satisfies it by giving each actor its own file. No equivalent
                              exists for this file, which is shared and multi-writer
```

---

### 1.3 · OBJECT: `REVIEW` (`REV-*`)

```
OBJECT                  review artifact
CLASS                   DEFINED
CURRENT LOCATIONS       reviews/mirror/ (52) · reviews/orchestrator/ (15) · reviews/plan/ (7)
NORMATIVE BASIS         Annex C.2 (single format, field list, VERDICT enum) · C.1 (ladder floors)
                        · C.3 (discipline: opening only via Orchestrator; AUTHOR ≠ REVIEWER ≠
                        ADJUDICATOR) · C.4 (three objects) · H.1 "Epistemic / method review |
                        Mirror" · body § 25
IS THE CLASS DEFINED?         YES
IS THE STORAGE SURFACE DEFINED?  NO — no annex names `reviews/`. It enters normative text once,
                              in § P5.1 at `main`, as a hash-exclusion prefix added at
                              `legend-candidate-v4`
IS THE WRITER DEFINED?        PARTIALLY — the reviewer writes the review (C.2 `REVIEWER`), and
                              C.3 assigns *opening* to Orchestrator. No writer is assigned for
                              the OPEN-*/CLOSE-* round artifacts that practice has created
                              (§ 1.11), because that class does not exist
```

---

### 1.4 · OBJECT: `OPERATOR_DECISION` (`DEC-*`, `record_type: OPERATOR_DECISION`)

```
OBJECT                  operator decision record
CLASS                   🔴 UNDEFINED
CURRENT LOCATIONS       governance/decisions/  — 4 distinct files, on 15 heads:
                          DEC-20260820-ORCH-SESSION-HOME.md
                              orchestrator-surface · plan-orchsurf-r4-transcription
                          DEC-20260821-ORCHSURF-D2-TRANSCRIPTION-ROUTING.md
                              orchestrator-surface · plan-orchsurf-r4-transcription
                          DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md
                              main + 12 others
                          DEC-20260822-ORCH-STATE-RECONSTRUCTION-CANDIDATE.md
                              operator-decision-orch-state-reconstruction only
NORMATIVE BASIS         🔴 NONE. `record_type: OPERATOR_DECISION` and `governance/decisions/`
                        appear ZERO times in the normative corpus. The nearest normative anchors
                        the records themselves cite are H.1 rows "Spese / MAJOR approval /
                        governance | Operatore" and "Strategia complessiva | Operatore" — which
                        assign an AUTHORITY, and define no artifact, no field list, no id
                        convention, no storage surface and no lifecycle
IS THE CLASS DEFINED?         NO
IS THE STORAGE SURFACE DEFINED?  NO — and the artifacts say so themselves. See F-2
IS THE WRITER DEFINED?        NO — three different arrangements observed. See F-4
```

---

### 1.5 · OBJECT: `HUMAN_APPROVAL_RECORD` (`record_type: HUMAN_APPROVAL_RECORD`)

```
OBJECT                  durable trace of one operator approval, as a Markdown record
CLASS                   🔴 UNDEFINED
CURRENT LOCATIONS       governance/decisions/HUMAN-APPROVAL-20260822-ORCHSURF-R4-TRANSCRIPTION-PATH.md
                        — orchestrator-surface only, 1 ref
NORMATIVE BASIS         🔴 NONE. The record's own frontmatter carries an `is_not:` block whose
                        first entry reads: "a J.3 HUMAN_APPROVAL_QUEUE entry — no APPROVAL_ID is
                        created and ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl is not written by
                        this record"
IS THE CLASS DEFINED?         NO — it explicitly declares itself outside the one approval class
                              that IS defined (J.3), and names no other
IS THE STORAGE SURFACE DEFINED?  NO — it declares `registration_surface:` by pointing at
                              DEC-20260821's "Registration and transit" section, which in turn
                              points at DEC-20260820 as "a proposed convention exercised, not a
                              legislated one"
IS THE WRITER DEFINED?        NO — `registering_actor: plan`, with
                              `registration_authority: explicit operator authorization`.
                              Self-declared per record, not assigned by any matrix
```

🔴 **This is the sharpest object on the surface.** An operator approval exists, is durable, is
hash-anchored to five artifacts — and by its own words is not a J.3 object, on a surface with no
normative basis, written by an actor whose authority to register it is declared inside the record
being registered.

---

### 1.6 · OBJECT: `DECISION PACKAGE`

```
OBJECT                  a package of open choices prepared for the operator
CLASS                   🔴 UNDEFINED — and instantiated under THREE different self-declared names
CURRENT LOCATIONS       reviews/mirror/DECISION-PACKAGE-20260817-001.md
                            `artifact: MIRROR decision package for HUMAN_APPROVAL`
                            `package_id: DECISION-PACKAGE-20260817-001`
                        governance/candidates/DEC-20260817-006-L2-SCOPE.md
                            `artifact: DECISION PACKAGE — DEC-20260817-006`
                        governance/candidates/DECISION-RECORD-20260817.md
                            `artifact: HUMAN DECISION RECORD — resolution request`
                            `record_id: DEC-20260817-001`   ← id and filename disagree
NORMATIVE BASIS         🔴 NONE. "decision package" appears nowhere in the normative corpus
IS THE CLASS DEFINED?         NO
IS THE STORAGE SURFACE DEFINED?  NO — two containers used for the same kind of object
IS THE WRITER DEFINED?        NO — mirror wrote one, plan wrote two
```

---

### 1.7 · OBJECT: `HUMAN_REQUIRED` durable object

```
OBJECT                  the durable object body § 4 requires every HUMAN_REQUIRED to produce
CLASS                   DEFINED — as a REQUIREMENT, with one named destination
CURRENT LOCATIONS       🔴 SPLIT ACROSS TWO INCOMPATIBLE SURFACES:
                        (a) ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl — the J.3 queue
                        (b) governance/candidates/DEC-20260817-006-GOV-SCOPE-RESOLUTION.md
                              `artifact: HUMAN_REQUIRED — protocol scope conflict`
                            governance/candidates/DEC-20260818-007-LAB-REACTIVATION.md
                              `artifact: HUMAN_REQUIRED — lab reactivation`
NORMATIVE BASIS         body § 4 line 130: "Ogni HUMAN_REQUIRED genera un oggetto durevole nella
                        HUMAN_APPROVAL_QUEUE (Annex J.3) — mai solo un messaggio" ·
                        § 4 taxonomy · H.1 "Classificazione HUMAN_REQUIRED ordinaria |
                        Orchestrator"
IS THE CLASS DEFINED?         YES — and it names ONE destination, the queue
IS THE STORAGE SURFACE DEFINED?  YES BY CLASS, NO BY PATH — § 4 names the queue as the
                              destination; nothing names where the queue lives
IS THE WRITER DEFINED?        NO — see § 1.2
```

🔴 Two objects that self-declare `artifact: HUMAN_REQUIRED — …` exist outside the queue § 4 names
as their destination. One of them states its reason in its own frontmatter: *"The Orchestrator
can write nowhere durably — it has no worktree and the root must stay clean."* That is a measured
constraint producing a surface choice, recorded honestly — and it is exactly the shape of a
practice that no rule authorized.

---

### 1.8 · OBJECT: `DECLARED DEVIATION RECORD`

```
OBJECT                  a declared departure from FROZEN text, prepared for operator ratification
CLASS                   🔴 UNDEFINED
CURRENT LOCATIONS       governance/candidates/APPROVAL-GOV311-DEVIATIONS.md
                            `artifact: DECLARED DEVIATION RECORD — for HUMAN_APPROVAL`
NORMATIVE BASIS         🔴 NONE. `deviazion|deviation|ESC-[0-9]` over the body, all ten annexes
                        and plan_defined_parameters at `main` → 0 hits. The record's own
                        deviation ids (PID-09, PID-10) and escalation ids (ESC-2, ESC-3) are
                        carried into the queue's DEVIATION_DECISIONS and CARRIED_UNRESOLVED
                        fields — which J.3 does not define either
IS THE CLASS DEFINED?         NO
IS THE STORAGE SURFACE DEFINED?  NO
IS THE WRITER DEFINED?        NO — `prepared_by: plan`, self-declared
```

---

### 1.9 · OBJECT: `CHECKPOINT` (`CHK-*`)

```
CLASS                   DEFINED — Annex A.6 / A.7
CURRENT LOCATIONS       ledger/checkpoints/<actor>/CHK-<actor>-NNNN.json — 27 files, 1 root
NORMATIVE BASIS         A.6 (checkpoint content, fingerprint binding) · A.7 (idempotent resume)
IS THE CLASS DEFINED?         YES
IS THE STORAGE SURFACE DEFINED?  NO — no annex names `ledger/checkpoints/`
IS THE WRITER DEFINED?        YES BY CONSTRUCTION — one directory per actor, one writer each
```

---

### 1.10 · OBJECT: `EVENT LEDGER` entry

```
CLASS                   DEFINED — Annex J.1 (event shape + 23 minimum types + strict append-only)
CURRENT LOCATIONS       🔴 NONE. The object has never been instantiated
NORMATIVE BASIS         J.1 · § P7 (one-writer design, option (a))
IS THE CLASS DEFINED?         YES
IS THE STORAGE SURFACE DEFINED?  🔴 YES — and it is the ONLY object on this surface whose path is
                              normatively fixed: `ledger/events/<ACTOR_ID>.jsonl`, view
                              `ledger/consolidated/` (§ P7)
IS THE WRITER DEFINED?        YES — "each file has exactly one writer, its own actor" (§ P7)
```

🔴 **The only object with a fully specified class, surface and writer is the one that does not
exist.** J.1's minimum type list contains `HUMAN_REQUIRED_OPENED` and `APPROVAL_RESOLVED`. Both
name the decision surface. Neither has ever been emitted. § P7 calls itself *"tracked as a debt;
not yet built"*.

---

### 1.11 · OBJECTS WITH NO CLASS AT ALL — the residue

Every one of these exists, is committed, is cited by other artifacts, and has no normative basis,
no defined surface and no defined writer. Listed for completeness because an inventory that omits
them would understate the surface.

| Self-declared kind | Instances | Container |
|---|---|---|
| `PROPOSAL-*` | `PROPOSAL-C9-STATE-MODEL.md`, `PROPOSAL-ORCH-STATE-RECONSTRUCTION.md` | `governance/candidates/` |
| `PREP-*` | `PREP-20260820-ORCHSURF-REV4.md`, `PREP-20260822-ROLE-CONTRACT-REPAIR.md` | `governance/candidates/` |
| `HANDOFF-*` | 6 in candidates, 1 in `reviews/mirror/`, 2 in `learning/plan/` | three containers |
| `ADVISORY-*` | `ADVISORY-FABLE-C9-001.md` | `governance/candidates/` |
| `DEBT-*` | `DEBT-20260818-LEASE-SNAPSHOT-AMBIGUITY.md` | `governance/candidates/` |
| `DELTA-*` | `DELTA-20260817-P51C9-SPLIT.md` | `governance/candidates/` |
| `CANDIDATE-STATUS` | `CANDIDATE-STATUS.md` | `governance/candidates/` |
| `AUTHOR-RESPONSE-*` | 6 files | `reviews/plan/`, `reviews/orchestrator/` |
| `OPEN-REV-*` / `CLOSE-REV-*` | 13 files | `reviews/orchestrator/` |
| `OBS-*`, `OWED-*`, `ACK-*`, `L2-OUTCOME-*`, `CLASS-*`, `ANALYSIS-*` | 13 files | `reviews/mirror/` |
| `NON-AUTHOR-CONTRIBUTION-*` | 1 file | `reviews/plan/` |

🔴 `AUTHOR_RESPONSE` deserves separate mention: C.2 defines it as a **mandatory field of the
review record**. Practice has made it a **separate artifact in a different actor's directory**.
The field is defined; the artifact is not.

---

## 2 · CLASS VS CONTAINER AUDIT

The question for each location is a single one: **does any normative text define what this
directory holds, or does it only tell you what the directory is excluded from?**

---

### 2.1 · `governance/decisions/`

```
A) a defined object class?          NO
B) only a container used by practice? YES
C) a control-plane surface?          NO — and this is measured, not assumed:
                                     § P5.1 at main lists exactly three CONTROL_PLANE_ROOTS —
                                     governance/candidates/ · ledger/ · reviews/
D) content-domain surface?           🔴 YES, BY EXCLUSION
```

**FLAG — CONTAINER MISTAKEN FOR CLASS.** This is the strongest instance on the surface, and the
repository already caught it once, in an artifact that is itself in this container:

> `governance/candidates/PREP-20260820-ORCHSURF-REV4.md` § F-6, on `orchestrator-surface`:
> *"Enumerated: there is no `DEC-*` artifact anywhere in the tree and no `governance/decisions/`
> … `governance/decisions/DEC-20260820-ORCH-SESSION-HOME.md` therefore **proposes** a
> [convention]"*

and the convention's own subsequent citation of itself:

> `DEC-20260821-ORCHSURF-D2-TRANSCRIPTION-ROUTING.md`, § Registration and transit:
> *"Registration follows the precedent exercised by DEC-20260820-ORCH-SESSION-HOME (**a proposed
> convention exercised, not a legislated one** — PREP-20260820-ORCHSURF-REV4 F-6)"*

**The container was created by the first record that needed one, and every later record cites the
first record's act as its basis.** No rule was ever written. The records are candid about this;
the candour does not convert practice into authority.

🔴 The domain consequence is stated inside the container by
`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` consequence 6: *"`governance/decisions/` is not
a declared CONTROL_PLANE_ROOT … This record is therefore in the content domain and will be inside
the CANDIDATE_CONTENT_HASH of every future candidate."* Independently verified in § 4.3 below.

---

### 2.2 · `governance/candidates/`

```
A) a defined object class?          PARTIALLY — D.2 defines the CANDIDATE MANIFEST class, but
                                    names no directory
B) only a container used by practice? YES for everything else it holds
C) a control-plane surface?          YES — declared in § P5.1 at main
D) content-domain surface?           NO
```

**FLAG — CONTAINER MISTAKEN FOR CLASS.** The directory name says "candidates". Measured contents
across all 43 heads: **28 distinct files, of which 9 are `CAND-*` manifests and 19 are not.**
The 19 span eight self-declared kinds (§ 1.11), including three DEC-ids, one decision package,
one human decision record, one declared deviation record, and two objects that self-declare
`artifact: HUMAN_REQUIRED`.

🔴 **The failure mode this produces is already in the record.** Three of those files declare, in
their own frontmatter, a reason for being here:

> *"domain: CONTROL PLANE — governance/candidates/, so materializing this moves no candidate hash"*
> — `DEC-20260817-006-GOV-SCOPE-RESOLUTION.md`
> *"domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT at main,
> verified, so materializing this moves no candidate content hash"* — `DEC-20260817-006-L2-SCOPE.md`
> *"domain: CONTROL PLANE — governance/candidates/, so registering this moves no candidate hash"*
> — `DEC-20260818-007-LAB-REACTIVATION.md`

**The container was selected for its hash-exclusion property, not because it is the class's
home.** That is a container being used as a class boundary. It is a legitimate and honestly
declared engineering choice; it is not a definition, and it silently makes `governance/candidates/`
the de-facto home of every object that must not move a hash.

🔴 Also flagged: **two distinct files carry the same id.** `DEC-20260817-006-GOV-SCOPE-RESOLUTION.md`
declares `id: DEC-20260817-006-GOV-SCOPE-RESOLUTION`; `DEC-20260817-006-L2-SCOPE.md` declares
`artifact: DECISION PACKAGE — DEC-20260817-006`. Both resolve to the DEC-006 series with different
content. No id-uniqueness rule exists to have been violated.

---

### 2.3 · `ledger/approvals/`

```
A) a defined object class?          The CONTENTS are class-defined (J.3). The DIRECTORY is not
B) only a container used by practice? YES — the path is named by no normative text
C) a control-plane surface?          YES, by inheritance — `ledger/` is a CONTROL_PLANE_ROOT
D) content-domain surface?           NO
```

**FLAG — CLASS DEFINED, CONTAINER IMPROVISED.** J.3 defines the object and never says where it
lives. § P7, the one place the corpus does specify ledger paths, specifies
`ledger/events/<ACTOR_ID>.jsonl` and `ledger/consolidated/` — and neither is `ledger/approvals/`.
The queue file's own header line declares its own status: *"This file is the minimal
J.3-conformant instance required by the approval now pending … and it is NOT the general queue
implementation, which remains PENDING_IMPLEMENTATION in the candidate manifest."*

🔴 **§ P7's one-writer principle is satisfied by giving each actor its own file. This file is one
shared file with at least three writers.** That is not a violation of P7 — P7 governs the event
ledger — it is the absence of any equivalent rule for this surface, and the fork in § 3.2 is its
first realized consequence.

---

### 2.4 · `reviews/*`

```
A) a defined object class?          PARTIALLY — C.2 defines the REVIEW class; no directory named
B) only a container used by practice? YES for the per-actor subdirectories and for 13 of the
                                    non-REV objects it holds
C) a control-plane surface?          YES at main (§ P5.1, added at legend-candidate-v4)
D) content-domain surface?           NO at main.  🔴 YES on the `mirror` branch — see § 2.5
```

**FLAG — CONTAINER MISTAKEN FOR CLASS.** `reviews/` holds 74 files across all heads. 40 have a
`REV-*` basename. The remaining 34 span eleven self-declared kinds, including one `DECISION-PACKAGE-*`
(§ 1.6), six `AUTHOR-RESPONSE-*` (a C.2 *field* promoted to an artifact), and thirteen
`OPEN-REV-*` / `CLOSE-REV-*` round-management artifacts for which C.3 defines an authority
("Apertura solo via Orchestrator") but no object.

---

### 2.5 · 🔴 THE SURFACE DEFINITION IS ITSELF FORKED

`§ P5.1` — the single normative text that names any of these containers — **does not agree with
itself across refs**:

```
main, orchestrator, orchestrator-surface,     legend-candidate-v4
plan-orchsurf-r4-transcription, evidence-index  CONTROL_PLANE_ROOTS = candidates/ · ledger/ · reviews/

mirror  (this branch)                          legend-candidate-v3
                                               CONTROL_PLANE_ROOTS = candidates/ · ledger/
                                               reviews/ ABSENT
```

The classification "is `reviews/` control plane or content?" therefore **has two answers depending
on which ref you read it at**, and this report is being written on the ref that gives the minority
answer. Every domain statement above is measured at `main` and says so.

---

### 2.6 · SUMMARY TABLE

| Location | Defined class? | Container by practice? | Control plane? | Content? | Container↔class confusion |
|---|---|---|---|---|---|
| `governance/decisions/` | ❌ | ✅ | ❌ | 🔴 ✅ | 🔴 **FLAGGED** — strongest instance |
| `governance/candidates/` | partial (`CAND-*` only) | ✅ (19 of 28 files) | ✅ | ❌ | 🔴 **FLAGGED** |
| `ledger/approvals/` | contents yes, dir no | ✅ | ✅ | ❌ | 🔴 **FLAGGED** (class defined, container improvised) |
| `reviews/*` | partial (`REV-*` only) | ✅ (34 of 74 files) | ✅ at main | 🔴 on `mirror` | 🔴 **FLAGGED** |
| `ledger/checkpoints/` | ✅ (A.6/A.7) | ✅ | ✅ | ❌ | not flagged — one writer per subdir |
| `ledger/events/` · `ledger/consolidated/` | ✅ | — | ✅ | ❌ | 🔴 **DOES NOT EXIST** |
| `ledger/tasks/` · `ledger/probe/` · `ledger/retirements/` | ❌ | ✅ | ✅ | ❌ | container only |

---

## 3 · HUMAN_APPROVAL_QUEUE ANALYSIS — governance semantics only

### 3.1 · WHAT J.3 CANONICALLY DEFINES

Verbatim from the FROZEN annex:

```
APPROVAL_ID / REQUESTED_BY (ACTOR_ID) / TYPE (MAJOR | SPEND | DESTRUCTIVE | GOVERNANCE | STRATEGIC)
OBJECT (es. CANDIDATE_CONTENT_HASH + BASE_HEAD; voce di spesa; operazione)
RATIONALE / REQUESTED_AT
STATE: PENDING | APPROVED | APPROVED_WITH_MODIFICATION | DENIED | REVISION_REQUESTED
RESOLUTION (chi, quando, note; …)
```

**Defined:**

| # | Defined by J.3 | Where |
|---|---|---|
| 1 | The five-field record shape | J.3 code block |
| 2 | `TYPE` — a closed five-value enum | J.3 |
| 3 | `STATE` — a closed five-value enum | J.3 |
| 4 | `RESOLUTION` must carry who / when / notes | J.3 |
| 5 | `APPROVED_WITH_MODIFICATION` → new `directive_version` of the affected task | J.3 |
| 6 | `DENIED` → motivation returns to the requesting actor | J.3 |
| 7 | Every `HUMAN_REQUIRED` creates a queue object; the rest of the lab continues | J.3, body § 4 |
| 8 | The affected task → `AWAITING_APPROVAL` with checkpoint, idempotent resume (A.5–A.7) | J.3 |
| 9 | `DAILY_BRIEF` exposes `PENDING HUMAN DECISIONS` | J.3 |
| 10 | `REVISION_REQUESTED` on a candidate → Plan → new hash → new reviews | J.3 |
| 11 | The approval cites the exact hash (gate 5) | J.3, D.2 |
| 12 | **APPROVAL ≠ AUTHORIZATION** (E4) | J.3, D.4, body § 12 |

**FROZEN FIELDS** — the two closed enumerations, `TYPE` and `STATE`, plus the field names
themselves. Annex J is `status: FROZEN`; the materialization note records the text as supplied
verbatim. Extending either enum is a governance change, at `[MAJOR]`.

---

### 3.2 · WHAT J.3 DOES NOT DEFINE

#### PATH OWNERSHIP — **UNDEFINED**

J.3 names an object. It names no file, no directory, no format, no per-branch existence rule.
`ledger/approvals` occurs **zero times** in the normative corpus. The path in use was chosen by
the artifact that first needed it and is cited by everything since.

#### WRITER OWNERSHIP — **UNDEFINED**

H.1 has no row for it. The nearest rows assign the *classification* of an ordinary
`HUMAN_REQUIRED` to Orchestrator and *approval itself* to the Operator; neither is a write
assignment for a file. Observed, in the file:

```
plan          lines 2, 4, 6 (main lineage) · lines 7–10 (evidence-index lineage)
orchestrator  lines 7–10 (orchestrator lineage), each self-labelled
              "RECORDED_BY: orchestrator — WORK_COMMIT on the orchestrator branch, not a canonical write"
operator      the RESOLVED_BY of every resolution line
```

#### RECONCILIATION RULE — **UNDEFINED**

🔴 **The file has forked, and no rule exists to un-fork it.** Measured this session, independently:

```
20c24a2ba478   6 lines   27 refs   main · mirror · 25 others      the shared base
bb603d9a270b  10 lines    1 ref    orchestrator                   base + 4 approvals, 2026-08-18/19
95fc81639014  14 lines    2 refs   evidence-index, p51c9-rebased  base + 4 approvals + 4 resolutions, 2026-08-17
```

Verified: the 6-line base is a **byte-exact prefix of both** longer lineages; neither longer
lineage is a prefix of the other. The two divergent slices are **disjoint by APPROVAL_ID** — zero
key collisions. This matches, and independently confirms, the keyed comparison in
`learning/plan/PLAN-J3-QUEUE-RECONCILIATION-001.md` § 2.

🔴 **Two facts about that fork that a reconciliation rule would have to survive:**

1. **Line count is not chronology.** The 14-line lineage is dated 2026-08-17; the 10-line lineage
   2026-08-18 → 2026-08-19. "Take the longest file" or "take the latest branch" both order the
   history backwards.
2. **`main` carries neither slice.** The four approvals that resolved `SUNSET-DEC3`, `SCIAB`,
   `XPORT` and `P5DOMAIN` — all `TYPE: MAJOR`, all `STATE: APPROVED` — exist on `refs/heads/orchestrator`
   and nowhere else. The four `HA-1…HA-4` requests and their resolutions exist on `evidence-index`
   and `p51c9-rebased-onto-c89c2217` and nowhere else. **The canonical branch's copy of the
   approval queue records none of the eight.**

The queue's own append lines already declare this. `APR-20260819-P5DOMAIN-001`:

> `QUEUE_NON_CANONICAL`: *"This queue still has divergent copies across branches — main carries
> six lines, this seat carries ten after this append. This append does NOT reconcile them and is
> not authorized to. The queue's non-canonicality remains a separate open debt."*

**Not authorized to** is the correct reading and the point: the actor recognized that no rule
grants the reconciliation, and stopped. The debt is declared, in the object, four times.

#### PRECEDENCE RULE — **UNDEFINED**

Nothing states which lineage prevails, whether `main`'s copy is authoritative over an actor
branch's, or whether an approval that exists only on a work branch is in force. J.1's sovereignty
clause — *"lo stato repo resta sovrano — in conflitto vince il repo"* — resolves ledger-vs-repo
conflicts and says nothing about repo-vs-repo across refs.

#### BRANCH / REF AUTHORITY RULE — **UNDEFINED**

No rule says the queue is per-branch, single-branch, or reconciled at batch. GATE 0 (D.3) binds
`BASE_HEAD`, root cleanliness, governance version, lease and ONE_WRITER — it does not evaluate
queue convergence. **An approval can therefore be in force on the branch that consumed it and
absent from the branch it authorized a commit onto.** That is the current state for four MAJOR
approvals.

---

### 3.3 · 🔴 BEHAVIOURS OBSERVED OUTSIDE THE FROZEN DEFINITION

Stated as classification, not as adjudication. None of these is resolved here.

| # | Observed | J.3 says |
|---|---|---|
| B-1 | `STATE: DEFERRED` — `RES-20260817-HA-2`, `RES-20260817-HA-4` | not in the `STATE` enum |
| B-2 | `STATE: RESOLVED` — `RES-20260817-HA-3` | not in the `STATE` enum |
| B-3 | Four approvals written as a **single line** carrying both `APPROVAL_ID` and `RESOLUTION_ID`, `STATE: APPROVED`, with `NO_PRIOR_PENDING_LINE` declared | J.3 models request → resolution; the single-line form is neither authorized nor forbidden |
| B-4 | `CORRECTION_ID` / `CORRECTS_APPROVAL_ID` — a third record kind (`COR-20260816-GOV311-001`) | J.3 defines no correction record |
| B-5 | Fields carried that J.3 does not define: `DEVIATION_DECISIONS`, `CARRIED_UNRESOLVED`, `BINDING_IS_EXCLUSIVE`, `NOT_PREDATED`, `QUEUE_NON_CANONICAL`, `SESSION_ROUTING_DEBT`, `MATERIAL_POLICY_CHOICE_APPROVED`, `OPERATOR_STATEMENT_VERBATIM`, `P5_BINDING_PRE_BATCH` | J.3's own materialization preamble says "Campi minimi: estendibili, mai rimovibili" — extension is permitted; **the `STATE` enum is not a field, it is a closed value set, and B-1/B-2 are not extensions of it** |
| B-6 | Resolutions appended as new lines, originals never edited | ✅ conforms — this is J.1 discipline correctly applied |

---

## 4 · DEC SURFACE ANALYSIS

### 4.1 · WHAT MAKES AN OBJECT A `DEC` ACCORDING TO EXISTING GOVERNANCE

**Nothing.** There is no clause anywhere in the normative corpus that defines a `DEC`, an
`OPERATOR_DECISION`, a decision id format, a decision lifecycle, a ratification mechanism, or a
registration act.

What exists instead, and is genuinely normative:

- **H.1** assigns *authority*: `Spese / MAJOR approval / governance | Operatore`, `Strategia
  complessiva | Operatore`. An authority to decide. Not an artifact.
- **body § 4** requires that a `HUMAN_REQUIRED` produce a durable object **in the
  HUMAN_APPROVAL_QUEUE**, never only a message. A durability requirement pointing at a *different*
  class.
- **body § 12 / GATE 3** routes MAJOR through `HUMAN_APPROVAL (oggetto in coda, J.3)`.

**Consequence, stated flatly:** the only durable operator-decision object the governance defines
is the J.3 queue entry. `DEC-*` is a class the repository invented for decisions J.3's shape does
not fit — scoped rulings, state determinations, status determinations, confirmations of existing
frozen text. That the need is real is not in question. That the class exists in governance is.

🔴 **The `change_class` values in use are a second, independent vocabulary:**

```
CONFIRMATION · SCOPED_RULING · STATE_DETERMINATION · STATUS_DETERMINATION
PROCESS_COMPLETION_APPROVAL
```

D.2 defines `CHANGE_CLASS: ORDINARY | MAJOR`. **Five values, none in the enum, on a field name
the corpus already uses for something else.** Whether these are the same field is undecidable
because no schema declares either scope.

### 4.2 · IS `governance/decisions/` NORMATIVE OR ONLY CURRENT PRACTICE?

**Only current practice — and the practice documents its own non-normativity in three places:**

1. `PREP-20260820-ORCHSURF-REV4.md` F-6: the first DEC *"proposes"* the convention; before it,
   `governance/decisions/` did not exist and no `DEC-*` artifact existed anywhere.
2. `DEC-20260821` § Registration and transit: *"a proposed convention exercised, not a legislated
   one"*, and *"This designation deliberately follows the `governance/decisions/` precedent … and
   **adopts no rule** about those earlier records."*
3. `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` E-10: *"`governance/decisions/` did not exist on
   `main` before this record."*

**Frequency is not canonicity.** `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` is present on
14 heads including `main`. It reached 13 of them by being an ancestor, not by being ratified 13
times.

🔴 **The precedent chain has a broken locator.** `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md`
§ E-10, on `main`, states: *"the two prior decision records (`DEC-20260820-ORCH-SESSION-HOME`,
`DEC-20260821-ORCHSURF-D2-TRANSCRIPTION-ROUTING`) are tracked on `evidence-index`."*

Measured across all 43 heads, all 4 remotes and all 5 tags:

```
DEC-20260820-ORCH-SESSION-HOME.md              orchestrator-surface · plan-orchsurf-r4-transcription
DEC-20260821-ORCHSURF-D2-TRANSCRIPTION-ROUTING.md  orchestrator-surface · plan-orchsurf-r4-transcription
evidence-index : files under governance/decisions/    0
evidence-index : DEC-* files at any path              0
```

**The substantive claim — that they are not on `main` — is true. The branch attribution is
false**, in the one decision record that is on `main`. Recorded as a locator defect, not
adjudicated: this report neither corrects it nor requests its correction.

### 4.3 · DOES `DEC` STORAGE AFFECT THE CANDIDATE HASH / CONTENT DOMAIN?

**YES — measured, at `main`.**

```
§ P5.1 at main, legend-candidate-v4:
CONTROL_PLANE_ROOTS:
- governance/candidates/
- ledger/
- reviews/

governance/decisions/  → NOT LISTED
```

§ P5.1's rule is exhaustive by construction: *"Everything not under a declared root is content"*,
and *"all of `governance/` except `candidates/` are outside both roots and always in the domain."*

**Therefore, mechanically:**

- every file under `governance/decisions/` is **CONTENT**;
- it enters the `ls-tree` serialization of `CANDIDATE_CONTENT_HASH` (§ P5.2) for any candidate
  whose `BASE_HEAD` includes it;
- **writing a decision record moves the identity of every open candidate rebased onto it**, and
  under D.2's `[MAJOR] Binding` clause any material change invalidates the approval bound to the
  prior hash.

The same is not true of the three DEC-ids sitting in `governance/candidates/` (§ 2.2), which are
control plane and move no hash. 🔴 **Two objects of the same self-declared kind currently have
opposite hash-domain behaviour purely as a function of which directory they were filed in.**

`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` consequence 6 reached the same conclusion for
itself and checked the blast radius at the time — *"No open candidate declares the pre-commit
`main` tip `04693e68` as its `BASE_HEAD`"* — which was true then and is a per-commit check, not a
rule. No rule performs it.

**No relocation is recommended, considered, or implied by this section.**

---

## 5 · REQUIRED DECISION PACKAGE

The minimum set of unresolved decisions. Each is stated as a question with options and no
selection. **These are not DECs and this section is not a decision package object** (§ 1.6) — it
is the enumeration this report was asked to produce.

---

```
D-ID:      D-1
QUESTION:  Is `OPERATOR_DECISION` / `DEC-*` a governance object class at all, or is it a
           practice-generated artifact that must be expressed through an object the governance
           already defines?

WHY IT CANNOT BE DEFERRED:
           Every subsequent question on this surface is downstream of it. A path decision, a
           writer decision, a schema decision and a reconciliation decision each presuppose that
           the thing being stored, written, shaped and reconciled is a class. Deciding path
           before class produces a container that defines its own contents — which is the exact
           defect § 2 measures in four places. Four DEC records are already in force and being
           cited as precedent; each further one deepens a practice basis for a class that has
           none.

EVIDENCE:
           · Zero normative mentions of `record_type: OPERATOR_DECISION` or `governance/decisions`
             (§ 0 reproduction command, control at 3 hits)
           · PREP-20260820-ORCHSURF-REV4 F-6 — the first DEC "proposes" the convention
           · DEC-20260821 § Registration — "a proposed convention exercised, not a legislated one"
           · DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE E-10 — the directory did not exist on
             main before that record
           · 7 DEC-ids across 2 containers, 6 self-declared `artifact:`/`record_type:` strings,
             5 `change_class` values against D.2's 2 (§ 4.1)
           · Body § 4 names the J.3 queue as the durable home of a HUMAN_REQUIRED, and no other

POSSIBLE OPTIONS (none selected):
           (a) `DEC` is a distinct class requiring its own definition
           (b) `DEC` is an instance of the J.3 queue object and must be expressed as one
           (c) `DEC` is not a class; each record is re-expressed under an existing class
               (candidate manifest, review, queue entry) case by case
           (d) `DEC` records are non-normative evidence only, binding through some other object
           (e) the question is answered differently for the sub-kinds already in use
               (CONFIRMATION vs SCOPED_RULING vs STATE_DETERMINATION vs STATUS_DETERMINATION vs
               PROCESS_COMPLETION_APPROVAL)
```

---

```
D-ID:      D-2
QUESTION:  Who is the authorized writer of `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl`?

WHY IT CANNOT BE DEFERRED:
           A shared append-only file with an undefined writer has already forked, and the fork is
           realized, not hypothetical: two lineages, neither containing the other, four MAJOR
           approvals reachable from one work branch only. Any further append by any actor extends
           one lineage and widens the divergence, and every actor that has appended has declared
           in the line itself that it is not authorized to reconcile. The next MAJOR approval
           forces the question whether it is answered or not.

EVIDENCE:
           · `ledger/approvals` occurs 0 times in the normative corpus (§ 1.2)
           · H.1 has no writer row; its nearest rows assign classification (Orchestrator) and
             approval (Operator), neither of which is a write assignment
           · Three writers observed in-file: plan, orchestrator, operator
           · § P7 solves one-writer for the EVENT ledger by per-actor files; this file is shared
           · Three blobs across 30 of 52 content refs (§ 3.2), independently re-measured this
             session and matching PLAN-J3-QUEUE-RECONCILIATION-001 § 2
           · `QUEUE_NON_CANONICAL` declared inside four separate queue lines

POSSIBLE OPTIONS (none selected):
           (a) a single named actor
           (b) per-actor files consolidated into a derived view, as § P7 does for events
           (c) the Operator alone, with actors requesting through another object
           (d) the writer is a function of the record kind (request vs resolution vs correction)
```

---

```
D-ID:      D-3
QUESTION:  What is the authority relationship between refs for a governance object — is an
           approval in force when it exists on an actor branch and not on `main`?

WHY IT CANNOT BE DEFERRED:
           Four `TYPE: MAJOR` `STATE: APPROVED` approvals — SUNSET-DEC3, SCIAB, XPORT, P5DOMAIN —
           are reachable from `refs/heads/orchestrator` and from no other ref, `main` included.
           Whether the canonicalizations they authorized are covered is not a future question:
           it is a present fact about work already performed. GATE 0 does not evaluate it and no
           other gate does either. D-2 cannot be answered without it, because a writer rule that
           does not say which ref the writing is authoritative on solves nothing.

EVIDENCE:
           · main's queue: 6 lines. orchestrator's: 10. evidence-index's: 14. Disjoint slices
           · J.1 sovereignty resolves ledger-vs-repo, not repo-vs-repo across refs
           · D.3 GATE 0 conditions: BASE_HEAD · root clean · GOVERNANCE_VERSION · lease ACTIVE
             singleton · ONE_WRITER — no queue-convergence condition
           · § P5.1 itself is forked (v3 vs v4) across refs, so even the domain rule that decides
             which surface is control plane has no single answer across refs (§ 2.5)

POSSIBLE OPTIONS (none selected):
           (a) `main` is authoritative and off-main records are not in force
           (b) any ref-reachable record is in force
           (c) in force from the moment of writing, with `main` as the audit surface
           (d) per-object-class answer
           (e) the question is a consequence of D-1/D-2 and not separately decidable
```

---

```
D-ID:      D-4
QUESTION:  Are `STATE: DEFERRED` and `STATE: RESOLVED` valid J.3 states, an unauthorized
           extension of a FROZEN enum, or records that must be re-expressed?

WHY IT CANNOT BE DEFERRED:
           Both appear in resolution lines that carry `REQUIRED_BEFORE_REAPPROVAL` — i.e. the
           records assert a live procedural obligation using a state the annex does not define.
           Anyone reading the queue to determine what is pending must already know the answer.
           J.3's materialization note permits extending FIELDS ("estendibili, mai rimovibili");
           `STATE` is a closed value set, not a field, and no clause permits extending it.

EVIDENCE:
           · J.3 STATE enum: PENDING | APPROVED | APPROVED_WITH_MODIFICATION | DENIED |
             REVISION_REQUESTED
           · RES-20260817-HA-2 and RES-20260817-HA-4 → `STATE: DEFERRED`
           · RES-20260817-HA-3 → `STATE: RESOLVED`, plus a `DECISION: B — NOT NOW` field
           · Annex J is `status: FROZEN`; H.1 assigns governance to the Operator
           · The three lines live only on the evidence-index lineage, so D-3 governs whether they
             are in force at all

POSSIBLE OPTIONS (none selected):
           (a) valid — the enum is read as extensible
           (b) invalid — the records must be re-expressed within the enum
           (c) valid only as recorded history; the enum binds going forward
           (d) a governance change to the enum is required, at [MAJOR]
```

---

```
D-ID:      D-5
QUESTION:  Do governance records that describe or manage decisions belong in the candidate
           content domain, and by what rule is that determined?

WHY IT CANNOT BE DEFERRED:
           The answer currently depends on which directory a record was filed in, and no rule
           performs the filing. `governance/decisions/` is content: writing there moves
           CANDIDATE_CONTENT_HASH for every candidate rebased onto it, and under D.2's [MAJOR]
           binding clause a material change invalidates the bound approval.
           `governance/candidates/` is control plane: three DEC-ids were filed there and each
           declares hash-neutrality as its reason. Same kind of object, opposite mechanical
           behaviour. Any path decision taken before this one silently decides it.

EVIDENCE:
           · § P5.1 at main lists exactly three CONTROL_PLANE_ROOTS; `governance/decisions/` is
             not among them; "Everything not under a declared root is content"
           · DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE consequence 6 reaches the same result
             and performs a one-off blast-radius check no rule requires
           · Three `governance/candidates/` DEC-ids declare CONTROL PLANE domain in frontmatter,
             two of them naming hash-neutrality as the reason for the location
           · § P5.1's own rule: "Adding a root is a governed change to this file, reviewable as
             such — never an ad-hoc exclusion"
           · 🔴 § P5.1 is itself forked across refs (v3/v4), so the rule that answers this
             question does not currently have one value (§ 2.5)

POSSIBLE OPTIONS (none selected):
           (a) decision records are control plane
           (b) decision records are content
           (c) it depends on the record's effect, not its location
           (d) the question is subsumed by D-1
```

---

```
D-ID:      D-6
QUESTION:  Is `HUMAN_APPROVAL_RECORD` (§ 1.5) a class, and — since it declares itself NOT a J.3
           queue entry — what makes an operator approval durable and citable if not the queue?

WHY IT CANNOT BE DEFERRED:
           One instance already exists and is already load-bearing: it approves the completion of
           an executed transcription path and hash-anchors five artifacts. Body § 4 says a
           HUMAN_REQUIRED produces a durable object in the queue and never only a message. This
           record is durable, is an approval, and is by its own declaration not in the queue.
           Either § 4's rule does not cover this kind of approval, or this record is outside it.
           Both readings are available and neither is written down.

EVIDENCE:
           · `is_not:` block, verbatim: "a J.3 HUMAN_APPROVAL_QUEUE entry — no APPROVAL_ID is
             created and ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl is not written by this record"
           · Also declares it is not a GATE 5 approval bound to CANDIDATE_CONTENT_HASH + BASE_HEAD
             and not a C.3 review round
           · `registering_actor: plan`, `registration_authority: explicit operator authorization`
             — declared inside the record it authorizes
           · Present on 1 ref (`orchestrator-surface`) — D-3 governs whether it is in force
           · Body § 4 line 130; J.3 rules paragraph

POSSIBLE OPTIONS (none selected):
           (a) a distinct class needing definition
           (b) a J.3 queue entry that must be expressed as one
           (c) not an approval in the § 4 sense — a completion attestation, needing its own answer
           (d) subsumed by D-1
```

---

```
D-ID:      D-7
QUESTION:  What is the object of a review round's opening and closing, and does the review
           outcome vocabulary have one definition or three?

WHY IT CANNOT BE DEFERRED:
           The decision surface consumes review outcomes as inputs: D.2's manifest carries
           `MIRROR_REVIEW: n/a | PASS | FAIL + REVIEW_ID`, and the J.3 queue entries carry a
           `MIRROR_REVIEW` object citing verdicts. Three incompatible vocabularies are in
           simultaneous use, and this has ALREADY consumed one operator decision
           (DEC-20260821 Decision 1, a scoped ruling that a manifest field may carry a
           representation the D.2 enum "cannot represent truthfully"), which forbids its own
           generalization and states: "Repeated scoped rulings indicate a possible schema design
           issue." A second such case is a schema question presenting as a routing question.

EVIDENCE:
           · C.2 VERDICT enum: CONFIRMED | WEAKENED | REFINED | REFUTED
           · D.2 MIRROR_REVIEW enum: n/a | PASS | FAIL + REVIEW_ID
           · 🔴 Both are in use at once, at different granularities. Measured in `reviews/` on
             this branch: the C.2 enum appears as a `VERDICT:` value at 7 loci in 4 files
             (CONFIRMED ×5, REFINED ×2 — REV-GOV311-MIRROR-002/003, REV-C9-STATE-MODEL-001,
             REV-ORCH-STATE-RECONSTRUCTION-001), always as a PER-AXIS verdict inside a review.
             The DOCUMENT-level dispositions — the ones D.2's `MIRROR_REVIEW` field and the J.3
             queue's `MIRROR_REVIEW` object actually cite — are REQUEST CHANGES (17) ·
             ACCEPT (7) · REVISION_REQUESTED (2) · BINDING VERIFIED (2) · PASS_WITH_NOTES ·
             NOT ATTESTED · ACK, plus `VALIDATION_RESULT: COMPLIANT` and
             `VALIDATION_RESULT`/`FINAL_RESULT: FAITHFUL`, and several free-text sentences.
             **Not one of those document-level tokens is in C.2's enum or in D.2's**
           · The queue's own `MIRROR_REVIEW` objects cite `disposition: PASS_WITH_NOTES`,
             `verdict: ACCEPT` — a third shape again, keyed differently per lineage
           · 13 `OPEN-REV-*` / `CLOSE-REV-*` artifacts exist; C.3 assigns opening authority to
             Orchestrator and defines no artifact
           · 6 `AUTHOR-RESPONSE-*` files exist; C.2 defines AUTHOR_RESPONSE as a review FIELD

POSSIBLE OPTIONS (none selected):
           (a) one vocabulary, the others mapped onto it
           (b) distinct vocabularies for distinct objects, with the mapping declared
           (c) the D.2 field is amended
           (d) out of scope for the decision surface and separately owned
```

---

```
D-ID:      D-8
QUESTION:  Does `DEC-20260823-SURFACE-MAP-QUEUE-CLOSURE` exist, and can a governance object be
           binding while unreadable?

WHY IT CANNOT BE DEFERRED:
           A record on the surface under review (`PLAN-J3-QUEUE-RECONCILIATION-001`) names it as
           its `scope_source`, and scoped its own work from an operator's in-session transmission
           because the artifact could not be read. If work on this surface is already being
           scoped by a cited-but-absent decision object, the classification of that object is a
           precondition for trusting any scoping downstream of it — including this report's, if
           the same DEC is meant to govern it.

EVIDENCE:
           · Measured this session over all 43 heads, 4 remotes, 5 tags and the working tree
             including untracked files: 0 paths matching `20260823` under `governance/decisions/`;
             `DEC-20260823` occurs in exactly 1 file — the record that cites it. Control:
             `DEC-20260822` on 14 refs. Reproduction with this report excluded: § 0
           · `learning/plan/HANDOFF-20260823-SURFACE-MAP-QUEUE-CLOSURE.md` exists on
             `plan-orchsurf-r4-transcription` and shares the id stem, but is a HANDOFF, not a DEC,
             and its own frontmatter records two further cited-but-absent objects: a
             "canonical HANDOFF v2.1 format" (0 hits, control at 268) and an advisory
             `EXTRACTION-20260823-QUEUE-CLOSURE-LOOP v1.2` matching no blob among 1122
           · PLAN-J3-QUEUE-RECONCILIATION-001 scope_note declares the gap in its own frontmatter

POSSIBLE OPTIONS (none selected):
           (a) it exists off-repository and must be materialized before being cited
           (b) it does not exist; records citing it must be rescoped
           (c) an in-session operator transmission is itself the object
           (d) subsumed by D-1
```

---

## 6 · FINAL CLASSIFICATION

### ALREADY DEFINED — class, and nothing further needed on this surface

| Object | Basis |
|---|---|
| `CANDIDATE MANIFEST` field set | D.2 |
| `CHANGE_CLASS` for candidates | D.2 (`ORDINARY \| MAJOR`) |
| `HUMAN_APPROVAL_QUEUE` record shape, `TYPE`, `STATE` | J.3 (FROZEN) |
| `APPROVAL ≠ AUTHORIZATION` | J.3 E4, D.4, body § 12 |
| Gate-5 binding to `CANDIDATE_CONTENT_HASH + BASE_HEAD` | D.2 `[MAJOR]`, J.3 |
| Every `HUMAN_REQUIRED` produces a durable queue object, never only a message | body § 4 |
| `REVIEW` format, ladder floors, C.3 discipline | C.1–C.4 |
| `CHECKPOINT` | A.6 / A.7 |
| `EVENT LEDGER` event shape + 23 types + strict append-only | J.1 |
| `CANDIDATE_CONTENT_HASH` domain rule and byte layout | § P5.1 / P5.2 |
| Authority to decide governance and strategy | H.1 (Operatore) |
| Authority for `CANONICAL_BATCH_COMMIT` | H.1 (Orchestrator, ACTIVE lease) |

---

### DEFINED CLASS / UNDEFINED SURFACE

| Object | Class defined by | Surface status |
|---|---|---|
| `HUMAN_APPROVAL_QUEUE` entry | J.3 | 🔴 path named by no normative text · **forked into 3 lineages** · no writer · no reconciliation · no precedence · no ref-authority rule |
| `CANDIDATE MANIFEST` | D.2 | `governance/candidates/` named only as a hash-exclusion prefix (§ P5.1) |
| `REVIEW` | C.2 | `reviews/` named only as a hash-exclusion prefix, **and only at `main`** |
| `CHECKPOINT` | A.6/A.7 | `ledger/checkpoints/` named by no normative text (writer safe by per-actor construction) |
| `HUMAN_REQUIRED` durable object | body § 4 | destination named by class (the queue), not by path; **two instances filed outside it** |

🔴 **`EVENT LEDGER` is the inverse and the control case**: class, surface and writer are all
defined (J.1 + § P7) — and **0 of 23 event types have ever been emitted**. The surface with the
complete definition is the one with no instances; the surfaces with hundreds of instances are the
ones with no definition.

---

### UNDEFINED CLASS

| Object | Instances | Containers used |
|---|---|---|
| `OPERATOR_DECISION` / `DEC-*` | 7 ids, 4 in `decisions/` + 3 in `candidates/` | 2 |
| `HUMAN_APPROVAL_RECORD` | 1 | `governance/decisions/` |
| `DECISION PACKAGE` / `HUMAN DECISION RECORD` | 3, under 3 different self-declared names | 2 |
| `DECLARED DEVIATION RECORD` | 1 | `governance/candidates/` |
| `PROPOSAL-*` · `PREP-*` · `HANDOFF-*` · `ADVISORY-*` · `DEBT-*` · `DELTA-*` · `CANDIDATE-STATUS` | 14 | `governance/candidates/`, `learning/plan/` |
| `AUTHOR-RESPONSE-*` as an artifact | 6 | `reviews/plan/`, `reviews/orchestrator/` (C.2 defines it as a **field**) |
| `OPEN-REV-*` / `CLOSE-REV-*` | 13 | `reviews/orchestrator/` |
| `OBS-*` · `OWED-*` · `ACK-*` · `L2-OUTCOME-*` · `CLASS-*` · `ANALYSIS-*` · `NON-AUTHOR-CONTRIBUTION-*` | 14 | `reviews/mirror/`, `reviews/plan/` |

🔴 **This report is itself in the last row.** `CLASS-*` under `reviews/mirror/` is a
practice-generated kind with no normative basis, filed in a container chosen for its domain
property. Writing it does not make it a class, and this report claims no more standing than the
objects it classifies.

---

### CONFLICTING PRACTICE

| # | Conflict | Evidence |
|---|---|---|
| F-1 | `governance/decisions/` has zero normative basis and is cited as precedent by every record in it | § 2.1, § 4.2 |
| F-2 | The convention's own records call it *"a proposed convention exercised, not a legislated one"* | DEC-20260821 § Registration |
| F-3 | 🔴 `HUMAN_APPROVAL_QUEUE` forked into 3 lineages; `main` carries none of 8 approvals; 4 of them `TYPE: MAJOR` `STATE: APPROVED` and reachable from one work branch only | § 3.2 |
| F-4 | Three writers on one shared append-only file with no writer rule; every writer declared it could not reconcile | § 1.2, § 3.2 |
| F-5 | 🔴 `STATE: DEFERRED` and `STATE: RESOLVED` outside a FROZEN enum, in lines asserting live obligations | § 3.3 B-1/B-2 |
| F-6 | Two objects self-declaring `artifact: HUMAN_REQUIRED` filed outside the queue body § 4 names as their destination, one stating a measured surface constraint as the reason | § 1.7 |
| F-7 | `governance/candidates/` holds 17 non-candidate objects of 8 kinds; three declare hash-neutrality as their reason for being there | § 2.2 |
| F-8 | Same self-declared kind, opposite hash-domain behaviour, decided by directory alone | § 4.3 |
| F-9 | Three simultaneous review-outcome vocabularies. C.2's enum is used, but only for per-axis verdicts (7 loci, 4 files); **every document-level disposition the manifest and the queue actually cite is outside both C.2 and D.2** — REQUEST CHANGES (17), ACCEPT (7), REVISION_REQUESTED, BINDING VERIFIED, PASS_WITH_NOTES, COMPLIANT, FAITHFUL, NOT ATTESTED. One operator scoped ruling already spent on the gap | D-7 |
| F-10 | 🔴 `§ P5.1` — the only normative text naming any of these containers — is forked v3/v4 across refs; `reviews/` is control plane at `main` and content on `mirror` | § 2.5 |
| F-11 | 🔴 `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` § E-10, **on `main`**, attributes the two prior DECs to `evidence-index`; measured: they are on `orchestrator-surface` and `plan-orchsurf-r4-transcription`; `evidence-index` carries 0. Substantive claim true, locator false | § 4.2 |
| F-12 | 🔴 `DEC-20260823-SURFACE-MAP-QUEUE-CLOSURE` cited as `scope_source` by a record on this surface; exists nowhere. Two further cited-but-absent objects in the accompanying handoff | D-8 |
| F-13 | Two files carry the id stem `DEC-20260817-006` with different content; no id-uniqueness rule exists | § 2.2 |
| F-14 | `change_class` carries 5 values on decision records against D.2's 2, on a field name the corpus already uses | § 4.1 |
| F-15 | `AUTHOR_RESPONSE`, a mandatory C.2 **field**, exists as 6 separate artifacts in two actors' directories | § 1.11 |

---

### REQUIRES OPERATOR DECISION

```
D-1   Is DEC a class?                                    → gates D-5, D-6, and any path decision
D-2   Who writes the HUMAN_APPROVAL_QUEUE?               → gated by D-3
D-3   Ref authority for governance objects               → gates D-2, D-4; four MAJOR approvals live
D-4   DEFERRED / RESOLVED against a FROZEN enum          → gated by D-3
D-5   Content vs control plane for decision records      → gated by D-1
D-6   Is HUMAN_APPROVAL_RECORD a class?                  → gated by D-1
D-7   One review-outcome vocabulary or three?            → independent; already cost one scoped ruling
D-8   Does DEC-20260823-… exist?                         → gates the scoping of work already in flight
```

**All eight sit at H.1 rows `Spese / MAJOR approval / governance | Operatore` and `Strategia
complessiva | Operatore`.** None is Mirror's, and none is answered here.

🔴 **One constraint on whoever answers them.** `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE`
determined `ACTIVATION_NOT_CONFIRMED`: the four role contracts remain `PROPOSED` and non-binding,
and *"any authority an actor exercises must be traced to the governance body or to a named annex
— never to a role contract clause standing alone."* Measured this session at `main`: `roles/` is
unchanged, all four still `status: PROPOSED`. **No authority for any answer above may be read out
of `roles/`.**

---

## 7 · WHAT THIS REPORT DID NOT DO

- did not choose a solution, a canonical path, a writer, or a reconciliation rule;
- did not merge, reconcile or reorder any queue lineage, and read every lineage read-only;
- did not modify any schema, enum or frozen text;
- did not create a `CAND`, a `DEC`, or any object requiring approval;
- did not adjudicate F-1…F-15 — each is classified, none is resolved;
- did not correct the locator defect at F-11 or request its correction;
- did not treat any artifact under `governance/candidates/`, `governance/decisions/`, `reviews/`,
  `ledger/` or `learning/` as normative evidence of its own class;
- did not infer authority from frequency, from `main`-presence, or from the fact that a practice
  has been exercised repeatedly;
- did not commit itself. This file is written to the working tree of the `mirror` worktree and
  left uncommitted; committing it is a `WORK_COMMIT` (D.1) and belongs to whoever holds that act.

END OF REPORT.

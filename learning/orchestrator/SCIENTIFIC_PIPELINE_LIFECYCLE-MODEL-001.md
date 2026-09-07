---
artifact: LIFECYCLE ANALYSIS — the nine states of a scientific task, and which of them the
  repository can currently observe, record and close
record_id: SCIENTIFIC_PIPELINE_LIFECYCLE-MODEL-001
task_id: SCIENTIFIC_PIPELINE_LIFECYCLE_MODEL_001
dispatcher: operator
date: 2026-08-22
author_session: analysis performed in the root checkout at `main` @ 788c357; artifact written on
  branch `orch-scientific-pipeline-lifecycle-model`, in worktree `…/scratchpad/wt-lifecycle`
actor_id: NOT ESTABLISHED — see IDENTITY. This record is not authored under a role contract.
governance_version: 3.1.1 (read, not exercised)
classification:
  - LIFECYCLE ANALYSIS ONLY
  - NOT AN IMPLEMENTATION PROPOSAL
  - NOT GOVERNANCE
  - NOT EXECUTION AUTHORIZATION
authority_claimed: >
  One, and it is named: Annex H.1 `WORK_COMMIT — ogni attore, solo proprio branch, granularità
  milestone`, and Annex D.1 `WORK_COMMIT (ogni attore, proprio branch — obbligatorio, non
  canonico)`. That row is not conditioned on a lease. No other authority is claimed or exercised.
domain: >
  CONTENT. CONTROL_PLANE_ROOTS (`governance/plan_defined_parameters.md` § P5.1) are exhaustively
  `governance/candidates/`, `ledger/` and `reviews/`, measured at `main` @ 788c357 — `learning/`
  is not among them. This record therefore sits inside the CANDIDATE_CONTENT_HASH of any future
  candidate that re-aligns onto the branch carrying it. It does not advance `main`.
not_an_slr: >
  This is NOT a Session Learning Record. Annex E.6 governs those. The name is deliberately not
  `SLR-`, following the precedent set by SCIENTIFIC-PIPELINE-PREPARATION-001 at this seat.
relates_to: >
  Four prior records occupy adjacent ground, each on a different branch (SURFACE_MAP § S-4). This
  record re-derived every shared measurement independently rather than inheriting it, and says
  where it agrees, where it differs, and where it adds something none of them measured.
---

# SCIENTIFIC PIPELINE — LIFECYCLE MODEL 001

> **LIFECYCLE ANALYSIS ONLY.** Nothing here creates a task, assigns an actor, opens a review,
> activates a contract, resolves a finding, confers authority, schedules work, or recommends that
> anything be built. It measures which lifecycle states the repository can currently bring into
> being, observe, record and close — and states the distance between that and the pipeline the
> dispatch describes.

---

## TASK_STATUS

```
STATUS        NEW TASK — accepted as analysis, executed as analysis, closed as analysis
DISPATCHER    operator
ITERATION     1
MODE          ANALYTICAL. No implementation performed.
```

**Constraints as given, and what was done about each.**

| Constraint | Disposition |
|---|---|
| do not implement anything | ✅ no instrument written, no schema defined, no validator built |
| do not modify `governance/` | ✅ untouched — verified by `git diff --stat` at close |
| do not modify `roles/` | ✅ untouched |
| do not modify `framework/` | ✅ untouched |
| do not modify `ledger/` | ✅ untouched |
| create only an artifact, on my own branch, via `WORK_COMMIT` | ✅ one new file, on `orch-scientific-pipeline-lifecycle-model`; `main` not written |
| do not assume authority from the role contract | ✅ IDENTITY § 2. Every rule cited below traces to the governance body or a named annex, never to a role contract |
| do not reduce reading quality to save cost/tokens/context | ✅ and this is not merely honoured — it is already normative, and TARGET_STATE § T-6 records where an automation would violate it |

### 🔴 One collision between the dispatch and the repository, recorded not resolved

The dispatch names **"peer review"** and **"adjudication"** as consecutive states owned inside the
Scientist pipeline. Annex C.3 and H.1 place both outside it:

- *"Apertura solo via Orchestrator"* (C.3) — a Scientist cannot open the review of its own output.
- *"Aggiudicazione challenge → Orchestrator (con rationale)"* (H.1); persistent scientific
  disagreement has floor **R3 TRIADIC** (C.1), derogable only upward.
- Body § 27, via `roles/scientist.md`: forced consensus is an error;
  `DISAGREEMENT_UNRESOLVED` with an explanation is a legitimate outcome.

The states are therefore modelled below **as the repository defines them** — review and
adjudication are pipeline states whose creator and closer sit outside the Scientist role — rather
than as the dispatch's sequence implies. This is a modelling decision, not a ruling, and it is
registered in OPEN_QUESTIONS as **Q-3**.

---

## IDENTITY

### 1 · Established from repository evidence, not from the dispatch

The dispatch addressed this session as Orchestrator. **Identity is not inherited from a dispatch.**
Every field was measured in this session.

| Fact | Measured value | How |
|---|---|---|
| Working directory (analysis) | `<REPO_ROOT>` | `git rev-parse --show-toplevel` |
| Branch / HEAD at analysis | `main` @ `788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5` | `git rev-parse` |
| Working tree at analysis | **clean** | `git status --porcelain` → empty |
| Branch this record is written on | `orch-scientific-pipeline-lifecycle-model`, based on `main` @ `788c357` | `git worktree add -b … main` |
| **Lease** | 🔴 **`ACTIVE by derivation: 0`** — 5 records, all `STALE` or `RELEASED` | `lease_state.py --check` |
| **Runtime inventory** | 🔴 **absent on the analysed ref** — present on exactly **1 of 47** refs (`orchestrator`) | per-ref `git ls-tree` |
| **Agent Card registry** | 🔴 **absent on the analysed ref** — present on exactly **1 of 47** refs (`orchestrator`) | per-ref `git ls-tree` |
| `ACTOR_ID` | **not established** — no registration record exists for this session | — |
| `SESSION_REF` | **not observable, and not invented** — `scientist_reading_modes.md` § 1.2: no actor observes its own `SESSION_REF` | — |

Derivation output, reproduced rather than summarised:

```
now (derivation instant)  2026-08-22T17:33:40.225392+00:00
  lease #1  derived=STALE     stored=STALE     expires=2026-08-18T09:40:25Z released=—
  lease #2  derived=RELEASED  stored=RELEASED  expires=2026-08-18T11:13:21Z released=2026-08-18T11:07:12Z
  lease #3  derived=STALE     stored=EXPIRED   expires=2026-08-18T13:04:11Z released=—
  lease #4  derived=RELEASED  stored=RELEASED  expires=2026-08-18T14:26:30Z released=2026-08-18T13:29:40Z
  lease #5  derived=RELEASED  stored=RELEASED  expires=2026-08-18T15:03:41Z released=2026-08-18T14:05:20Z
ACTIVE by derivation: 0
FINDING: lease #3 DISAGREEMENT: stored STATUS='EXPIRED', derived='STALE'.
FINDING: lease #3 EXPIRED_WITHOUT_RENEWAL: reached EXPIRES_AT with LAST_RENEWED absent or equal
         to ACTIVATED_AT. Detected at consultation; nothing watched the window itself.
```

### 2 · The consequence, stated plainly

`CLAUDE.md` § 0 is unconditional:

```
IF no valid runtime inventory / no ACTIVE ORCHESTRATOR_LEASE:
    ENTER BOOTSTRAP_MODE. Read /BOOTSTRAP.md.
    Do NOT assume Orchestrator authority merely because you are in root.
```

**Both antecedents hold. This session is in `BOOTSTRAP_MODE` and is not Orchestrator.**

`roles/orchestrator.md` agrees — *"Position in the root confers nothing"* — but that contract is
itself non-binding (`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE`, `ACTIVATION_NOT_CONFIRMED`), so
it is cited as agreement, never as the source of the rule. The operative sources are `CLAUDE.md`
§ 0 and Annex I.3.

### 3 · The one authority exercised, and where it comes from

`WORK_COMMIT` is the single row in the H.1 authority matrix allocated to **every** actor rather
than to a named one, and it is not conditioned on a lease:

```
| WORK_COMMIT | ogni attore, solo proprio branch, granularità milestone |     — Annex H.1
  WORK_COMMIT (ogni attore, proprio branch — obbligatorio, non canonico)      — Annex D.1
```

`deployment/deployment_profile.md` states why this had to be a branch and not the root: *"a commit
to `main` is canonical by definition — so an Orchestrator living in the root had no branch on which
a `WORK_COMMIT` was possible."* This record therefore lands on its own branch. **That is the whole
of the authority exercised here.** It does not imply a lease, a role, or an ACTOR_ID.

### 4 · Available runtime information, declared

```
AVAILABLE      the git object database (47 refs), 21 worktrees, the seven runnable gates (§ S-5),
               lease_state.py, the working tree at main @ 788c357
NOT AVAILABLE  ACTOR_ID · SESSION_REF · a heartbeat · an event stream · any observation of another
               actor's liveness · the runtime inventory and Agent Card registry from this ref
```

---

## SURFACE_MAP

### S-1 · The measurement universe every claim below is scoped by

```
MEASURED_AT          ref  main
                     HEAD 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5
                     working tree clean, 2026-08-22
REFS SURVEYED        47 = 38 refs/heads · 4 refs/remotes · 5 refs/tags
NOT SURVEYED         refs/codex · refs/stash — content not enumerated
WORKTREES            21 (20 before this record's worktree was added)
SURFACE DELTA        this session added 1 branch and 1 worktree
```

🔴 **Every absence claim in this record is scoped by that surface and by nothing wider.**
`NOT_FOUND` across 47 refs in this clone is not `NOT_EXIST` in another clone, a codex ref, or a
remote this session cannot see.

### S-2 · 🔴 A false zero produced inside this session, and how it was caught

The first ref sweep returned `0/47` for **every** path — including `CLAUDE.md` and
`governance/GOVERNANCE_v3.1.1.md`, which are present on `main` and were open in this session.

The cause: the sweep ran in **zsh**, where `for r in $REFS` does not word-split an unquoted
multi-line variable. `$r` was bound once, to the entire 47-line string, and every `git ls-tree`
silently failed. **The failure produced no error — only zeros**, and zeros are exactly the shape
of the answer the sweep was looking for.

It was caught because two paths known to exist were carried in the sweep as **positive controls**.
The sweep was re-run under `bash -c` with a `while IFS= read -r` loop:

```
POSITIVE CONTROL   CLAUDE.md                        46/47  ✅ instrument working
POSITIVE CONTROL   governance/GOVERNANCE_v3.1.1.md  25/47  ✅ instrument working
```

**Every zero reported in this record comes from the corrected sweep, and every sweep in it carries
a positive control.** This is recorded because a silent false zero in a lifecycle analysis would
have produced a confident, wrong map of what exists.

### S-3 · Control-plane and learning surfaces — measured across all 47 refs

| Path | Refs where present | Note |
|---|---|---|
| `ledger/events/` | 🔴 **0 / 47** | P7's chosen path for the per-actor event ledger |
| `ledger/consolidated/` | 🔴 **0 / 47** | P7's chosen path for Plan's derived view |
| `LEARNING_INDEX` (any path) | 🔴 **0 / 47** | Annex E.2; body § 15 makes consulting it mandatory |
| `active_lessons/` | 🔴 **0 / 47** | Annex E.5; root `CLAUDE.md` annotates it *"not yet materialized"* — accurately |
| `OPERATOR_DAILY_BRIEF` / `DAILY_BRIEF` | 🔴 **0 / 47** | body § 10.4 requires it at least once per working day |
| `autonomy_ledger` | 🔴 **0 / 47** | Annex G.3; the instrument that would *measure* human load |
| `framework/state/actors.yaml` | 🔴 **0 / 47** | has never existed on any ref |
| `runtime/runtime_inventory.md` | ⚠️ **1 / 47** — `orchestrator` | not reachable from `main` |
| `runtime/agent_card_registry.md` | ⚠️ **1 / 47** — `orchestrator` | not reachable from `main` |
| `runtime/L2-OUTCOMES.md` | ⚠️ **1 / 47** — `orchestrator` | carries the verified-capability rows |
| `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` | 25 / 47 | **three disjoint contents** — F-7 |

### S-4 · Four adjacent analyses exist, each on a different branch, none on `main`

| Record | Branch | Lines |
|---|---|---|
| `SCIENTIFIC-PIPELINE-PREPARATION-001` | `main` (and 3 others) | 585 |
| `ORCHESTRATOR-SCIENTIFIC-PIPELINE-AND-LOOP-ARCHITECTURE-ANALYSIS-001` | `orch-pipeline-loop-architecture` | 1189 |
| `CONTROL-PLANE-RECONCILIATION-ANALYSIS-001` | `orch-control-plane-reconciliation` | 745 |
| `LEGEND-AGENT-COORDINATION-PROTOCOL-001` | `orch-agent-coordination-protocol` | 943 |

**No ref carries more than two of the four.** All four were written on 2026-08-22.

🔴 **The four sibling records reported 37, 44, 45 and 47 refs respectively. All four figures were
correct when taken.** The number grew because each analysis created a branch — three of the four
branches above did not exist when the earliest of them measured. **The surface being analysed is
enlarged by the act of analysing it**, and no instrument in the repository observes that. This
record's own contribution to the count is declared in S-1.

Where this record touches ground the siblings already covered, it **re-derived the measurement
rather than citing theirs**, and the re-derivations agree (F-5, F-6, F-7). Agreement on a count is
not verification of the set beneath it, so each was re-swept here with its own positive control.

### S-5 · What is executable today — measured by running it, not by reading a claim

Every gate below was run in this session, at `main` @ `788c357`:

```
legend_lint.py .                              VERDICT: PASS   (1 INFO, no block)
fulltext_receipts.py verify                   OK: 128 chained receipt(s), tail anchored
growth_anchors.py check                       VERDICT: PASS — claims=39 papers=70 corpus=356
                                              literature=390 registry_only=15 unread_premises=4
locator_audit.py                              54 manifest(s) audited, 10 unauditable, 0 quotes not found
session_self_eval.py                          VERDICT: PASS — every complete read has landed
public_release_gate.py                        BLOCKS: 0  (4 [REVIEW] advisories)
governance_fingerprint.py compose --all       4 role fingerprints composed
lease_state.py --check                        ACTIVE by derivation: 0  (+2 FINDINGs)
```

🔴 **Seven of the eight instruments above read scientific state. One reads control-plane state
(`lease_state.py`), and it covers a single object.** No script in the repository reads an Annex
A.1 task contract, an A.6 checkpoint, a B.1 envelope, a C.2 review or a J.3 approval record.

---

## FINDINGS

### F-1 · THE NINE-STATE LIFECYCLE — the dispatch's states against measured evidence

The dispatch's five questions per state, answered from the repository. **Creator** = who is
authorised to bring the state into being. **Observer** = who, other than the writer, can see it
happen. **Closer** = what durably ends it. **Event that should record it** = the Annex J.1 minimum
type that covers it, or `—` if J.1 has none. **What exists** = measured.

| # | State | Creator | Observer | Closer | J.1 event that should record it | What actually exists |
|---|---|---|---|---|---|---|
| **1** | **task creation** | **Orchestrator** — H.1 row 1, not lease-conditioned | 🔴 **nobody** | the owning actor edits `CURRENT_STATE` in the record it also writes | `TASK_ASSIGNED` | **5 task records, all `ledger/tasks/plan/*`, all written by `plan` about `plan`.** `XPORT-ROUTING-001` says so in its own `_note`: *"No `TASK_ASSIGNMENT` message was received."* The authority is allocated and has **never been exercised by its holder** |
| **2** | **assignment** | Orchestrator (A.1 + B.1 envelope) | the assignee, via `TASK_ACK` | A.3 durable `TASK_CLAIM`; *at most ONE valid claim per `TASK_ID + GENERATION`* | `TASK_ACKED`, `TASK_CLAIMED` | 🔴 **no `TASK_ACK` record exists for any task.** Exactly one ACK-shaped artifact exists repository-wide — `reviews/mirror/ACK-L2-20260818-ORCH-032.md` — and it acknowledges an L2 capability row, not a task. Every `TASK_CLAIM` on record is an embedded field in the claimant's own JSON: self-claimed, no counterparty |
| **3** | **reading** | the Scientist, on a claimed task | ⚠️ **the receipt ledger** — genuinely, and it is the only real observer in the table | a **contemporaneous receipt**, hash-chained and tail-anchored | 🔴 **none. J.1 has no reading event type** | ✅ **the strongest state in the system.** 128 chained receipts, `verify` OK, LINT consumes it; `record_kind` = 105 contemporaneous · 22 legacy_reconstruction · 1 invalidation |
| **4** | **analysis** | the Scientist | ⚠️ partial — `deepdive_manifest.py --verify-artifacts`, `locator_audit.py` | the five-step acceptance test (`scientist_reading_modes.md` §§ 3.6, 3.8) | 🔴 **none. J.1 has no analysis event type** | ✅ 64 deep-dive manifests; locator audit runs clean over 54. 🔴 **Step 5 — the blind locator audit — is agent-conducted and has no scripted form.** `locator_audit.py` answers the narrower precondition (*does the quote occur in its artifact*), not the judgement (*does the quote support the proposition*) |
| **5** | **handoff** | the sending actor | 🔴 **nobody** | 🔴 **nothing** | 🔴 **none — and this is the sharpest gap in the table (F-3)** | **15 handoff artifacts across 6 namespaces**, each with a shape of its own. `HANDOFF` is named in the B.2 type list and **specified nowhere else**: no required field, no state effect, no closure |
| **6** | **review** | **Orchestrator only** — C.3 *"apertura solo via Orchestrator"* | the reviewer; C.2 is the strongest object in the lifecycle (mandatory `STEELMAN` before objections, mandatory `WHAT_WOULD_CHANGE_MY_MIND`) | 🔴 **the author, not the reviewer** — C.2: *"AUTHOR_RESPONSE obbligatoria; il silenzio non è accettazione"* | `REVIEW_OPENED`, `REVIEW_CLOSED` | **40 `REV-*` against 8 `AUTHOR-RESPONSE-*`** (union, 47 refs). With no reachable Orchestrator, reviews are opened by `HANDOFF-*` artifacts written by the reviewed party |
| **7** | **adjudication** | Orchestrator, *with rationale* (H.1); F.2 verdicts `ACCEPT \| MODIFY \| OVERRIDE_WITH_RATIONALE \| ESCALATE` | 🔴 nobody, ex ante; Mirror ex post and pattern-based only (F.3) | the recorded rationale | `CHALLENGE_ADJUDICATED` — ⚠️ **covers challenges only. Persistent scientific disagreement (C.1 floor R3) has no event type** | 🔴 **zero adjudication records of either kind.** C.3 requires `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR`; when the H.1 adjudicator authored the object, the only remaining adjudicator is the operator |
| **8** | **closure** | — | — | 🔴 **nothing, anywhere** | `TASK_COMPLETE` + `CLOSES_EVENT_ID` — J.1 is explicit that open→outcome linkage lives **only** in the closing event | 🔴 **the closing instrument does not exist as a file on any of 47 refs.** A task is complete when its owner says so in a file its owner also writes |
| **9** | **learning** | any actor (E.6 Session Learning Record) | Mirror — whose **designated** primary surface is the consolidated event ledger (G.3), *"non leggendo le chat"* | E.2 `LEARNING_INDEX` entry; E.5 compression into `ACTIVE_LESSONS` | `LEARNING_PROMOTED` — ⚠️ **covers promotion only. E.1's `OBSERVED → LOCAL → PROVISIONAL → VALIDATING` transitions have no event type, and neither does retrieval** | ✅ raw archive intact (`learning/` + `reviews/` records across refs) · 🔴 `LEARNING_INDEX` **0/47** · 🔴 `ACTIVE_LESSONS` **0/47** · 🔴 Mirror's designated input surface **0/47** |

#### F-1.1 · The shape of the result

```
states with a defined CREATOR                          9 / 9
states with a THIRD-PARTY OBSERVER                     3 / 9   (reading, analysis, review)
states with a defined CLOSER in the governance text    8 / 9
states whose CLOSING INSTRUMENT EXISTS as a file       2 / 9   (reading, analysis)
states covered by a J.1 minimum event type             6 / 9   (2 of the 6 only partially)
```

**The specification is not the gap.** Every state has a creator; almost every state has a
specified closer. What is missing is the *instrument* — and it is missing asymmetrically, in a way
that maps exactly onto F-4.

### F-2 · 🔴 THE EVENT MODEL — 23 types specified, 0 ever emitted

Annex J.1 enumerates 23 minimum event types. Measured this session by harvesting **every `.jsonl`
blob on all 47 refs** and searching for each type as a JSON string value:

```
total jsonl lines harvested across all refs        46,125
POSITIVE CONTROL  "ledger_prev_hash" occurrences    4,742   ✅ harvest working
J.1 event types with ≥ 1 emission                       0 / 23
```

**Not one of the 23 event types has ever been written, anywhere, on any ref.** The design decision
is not the blocker: P7 chose option (a) — per-actor append-only JSONL at `ledger/events/<ACTOR_ID>.jsonl`,
consolidated by Plan into `ledger/consolidated/` — and gave a reason that survives inspection
(option (b) derives events from commits and ACKed messages, and *structurally cannot* represent
`CHECKPOINT_WRITTEN`, `ACTOR_DOWN`, `LEASE_STALE`, `HUMAN_REQUIRED_OPENED` or
`RESUMED_FROM_MILESTONE`). P7's own status line: *"Tracked as a debt; not yet built."*

#### F-2.1 · Which of the dispatch's nine states J.1 does not cover *at all*

This is the measurement this record adds that the sibling analyses did not make. Mapping the 23
types onto the nine states:

| Covered by a J.1 type | Partially covered | 🔴 **Not covered by any of the 23** |
|---|---|---|
| task creation · assignment · review · closure | adjudication (challenges only) · learning (promotion only) | **reading · analysis · handoff** |

🔴 **J.1's vocabulary is a control-plane vocabulary.** The three states where the scientific work
actually happens are absent from it. Two of them — reading and analysis — are covered by a
*different* ledger that J.1 does not reference and that the event ledger's design does not
subsume. **Handoff is covered by nothing at all**, which is F-3.

The consequence is precise and is not a criticism of J.1: **building the event ledger exactly as
specified would leave states 3, 4 and 5 unobservable**, and states 3 and 4 would remain observable
only through an instrument outside it. Whether J.1's minimum list should be extended, or whether
the two ledgers should stay separate with a declared join, is not decided here — **Q-1**.

### F-3 · 🔴 `HANDOFF` is a persistence class with no closure — the load-bearing gap for a two-reader pipeline

`HANDOFF` appears in the Annex B.2 message-type enumeration and **nowhere else in the governance
text**: no envelope beyond B.1, no required field, no state effect, no closing event. Measured
consequence — 15 artifacts, 6 namespaces, no two alike:

```
governance/candidates/HANDOFF-*         6    (candidate → reviewer)
release/*_HANDOFF.md                    3    (release engineering)
learning/{mirror,plan}/HANDOFF-*        3    (actor → actor, informal)
runtime/handoff/C-2/…                   2    (scientific working material)
reviews/mirror/HANDOFF-*                1    (review readiness)
```

**The sender's artifact is durable. The receiver's acceptance leaves no trace anywhere.** Whether
any of the 15 was received, read, accepted or refused is not a fact this repository can currently
answer.

🔴 **Why this matters specifically for the A/B pipeline the dispatch describes.** Handoff is the
edge on which the Scientist pipeline turns: A completes → outputs frozen → B's independence must be
preserved → Mirror sees both after freezing. **Freezing is a handoff.** With no closing event, the
statement *"A's output was frozen before B's was read"* is not a fact any instrument can establish
after the fact — it is a promise. `controlled_benchmark_ab.md` § 4 already makes exactly this
distinction for the reading surface: *"A first pass run in such a checkout is blind only by
promise."* The same words apply to the freeze, and nothing currently closes it.

### F-4 · 🔴 THE ASYMMETRY — this repository runs two lifecycles, and only one of them works

This is the central finding, and it reframes the dispatch's question.

| | **Scientific lifecycle** | **Control-plane lifecycle** |
|---|---|---|
| State vocabulary | 10 declared paper statuses | A.5 task states; J.2 actor/lab states |
| Records carrying a state | **390** literature records | **5** task records |
| Who wrote them | the pipeline, over months | `plan`, about `plan`, in every case |
| Events emitted | **128**, hash-chained, tail-anchored | **0** |
| Validators that run | **7** (§ S-5), all PASS | **1** (`lease_state.py`), one object |
| Derived view discipline | ✅ `reading_state.py` | 🔴 absent |
| Closure | ✅ receipt; ✅ acceptance test | 🔴 none for 7 of 9 states |

🔴 **The instrument the control plane is missing already exists in this repository, is proven at
scale, and P7 already named it as the thing to copy.** The receipt ledger implements J.1's event
shape almost field for field:

| J.1 event field | Receipt ledger field | Present in all 128 |
|---|---|---|
| `EVENT_ID` | `event_id` | ✅ |
| `timestamp` | `event_at` | ✅ |
| `OBJECT` | `study_id`, `source_fingerprint` | ✅ |
| `DURABLE_POINTER` | `outputs`, `source_locator` | ✅ |
| hash chain (J.1 *"append-only rigoroso"*) | `ledger_prev_hash` | ✅ |
| `CLOSES_EVENT_ID` (opening→outcome linkage) | `prior_receipt`, `invalidates_receipt` | ✅ (1 invalidation on record) |
| *"`closed_by` may exist ONLY in the derived view"* | `reading_state.py` — a **committed derived view**, explicitly not a receipt | ✅ |

`reading_state.py`'s own header is the strongest available evidence that this discipline was
learned the hard way rather than designed on paper: two actors read `PMID 42422765` in parallel on
2026-08-10, both legitimately continued the same earlier receipt, and *"whichever actor finished
second silently erases what the other read."* Its fix — *"sum, never choose"*, and never sign a
derived object as a receipt because *"a receipt signed by a process rather than a reader is a
fabricated attestation"* — is J.1's derived-view rule, discovered independently and already running.

**Therefore: the control plane's absence is a porting problem, not a design problem.** P7 says so
directly: *"This should reuse the existing append-only machinery, not invent a second one… The
event ledger's writer and validator are to be built on that pattern."*

> **What this record does NOT conclude from that.** It does not say the writer should be built, by
> whom, or when. P7 assigns the **design** to Plan and the design is done; the **writer** is
> authorised to nobody, and the `M4` L2 row is `BLOCKED — no event-ledger writer`. Naming an
> available pattern is not authorisation to apply it.

### F-5 · 🔴 The one lifecycle instrument that does run has an unvalidated state field

Measured in this session, and not reported by any sibling record.

`legend_lint.py` defines `VALID_PAPER_STATES` (10 values) and enforces it through
`_check_ids_states`. That function locates records with:

```python
pat = re.compile(r'^##\s+' + kind + r'\s+(\d+)\b', re.M)
```

It requires `## <KIND> <digits>`. Literature records are headed `## LIT-0085` — **hyphen, not
space**. Re-derived using the LINT's own parser, imported rather than reimplemented:

```
split_blocks(literature_tracking_log, 'LIT')     →   0 blocks
split_blocks(paper_registry, 'PAPER')            →  70 blocks, all statuses valid
```

**The literature tracking log's `Status:` field is never validated by anything.** What is in it,
across the 384 records headed `## LIT-<digits>`:

```
screened        174        ✅ declared
discovered      152        ✅ declared
processed        11        ✅ declared
integrated       10        ✅ declared
(no Status field) 10       🔴 the field is simply absent
claim_linked      4        ✅ declared
background_only   3        ✅ declared
filtered_out      1        ✅ declared
superseded        1        ✅ declared
archived          1        🔴 NOT in the declared vocabulary  (LIT-0401)
"completed — <wikilink to paper_registry_current#PAPER NNN> (`BATCH_20260815_001`)"
                 17        🔴 NOT in the vocabulary, and not an atomic value: the field carries
                              state + wikilink + batch id in one string
```

Declared but never used: `filtered_in`, `flagged_for_review`.

**`legend_lint.py` returns `VERDICT: PASS` over all of it**, and correctly — it is not looking.
`growth_anchors.py` counts these records (`literature=390`, which is these 384 plus 6 `LIT-EX-*`
example records) and passes, because **cardinality has a validator and the state field does not.**

🔴 **The significance for this analysis.** The dispatch asks which lifecycle states are real. The
scientific lifecycle is the one that works — and its state field is the *one* part of it that
nothing checks. The 17 composite `completed — …` values are not a defect of content: they are a
state machine and a foreign key packed into a free-text field because no schema forbade it. This
is the shape a lifecycle takes when it is enforced by discipline rather than by an instrument, and
it is a preview of what the control plane would look like if it were populated before it were
validated.

### F-6 · Review closure, and the approval queue — re-derived independently

Both were reported by sibling records. Both were re-measured here from the ref set in S-1, with
positive controls, rather than inherited.

**Review closure.** Union across 47 refs: **74 files under `reviews/`** — `mirror` 52,
`orchestrator` 15, `plan` 7. Of these, **40 are `REV-*` review artifacts and 8 are
`AUTHOR-RESPONSE-*`.** Annex C.2 makes the author response mandatory and states that silence is not
acceptance. **Agrees with the sibling measurement.**

### F-7 · 🔴 The human-decision record has forked into three disjoint contents

Re-derived by blob oid, which is the only way to see it:

```
20c24a2ba478…   6 lines   22 refs   (incl. main)
bb603d9a270b…  10 lines    1 ref    (orchestrator)
95fc81639014…  14 lines    2 refs   (evidence-index, p51c9-rebased-onto-c89c2217)

UNION of approval / resolution / correction IDs across 47 refs:  21
  → 10 APR-*  ·  10 RES-*  ·  1 COR-*
main carries:  2 APR-*  ·  2 RES-*  ·  1 COR-*   (all GOV311)
```

Verified with `cmp`: **`main` is a byte-exact prefix of both divergent copies.** The forks are
additive; nothing has been rewritten.

🔴 **The canonical ref carries the least information.** An actor that rehydrates on `main` and reads
the approval queue — the correct, documented thing to do — will conclude that `SCIAB`, `XPORT`,
`P5DOMAIN`, `SUNSET-DEC3` and `HA-1…HA-4` were never approved. **Agrees with the sibling
measurement**, re-derived independently.

**Why it belongs in a lifecycle model.** J.3's queue is the closing instrument for state 7 when the
adjudicator is the operator, and for every `HUMAN_REQUIRED` escalation. A closing instrument that
is replicated per-branch closes the state **on one ref only**. Append-only discipline holds
perfectly inside each fork and provides nothing across them.

### F-8 · HUMAN-IN-THE-LOOP — measured, and separated as the dispatch requires

The dispatch asks which steps require the operator today, split three ways. The classification below is
a measurement of *why* the human is needed, **not a plan to remove anyone.**

**(a) Must remain human — structural, and would remain in a fully built system**

| # | Decision | Source |
|---|---|---|
| H-1 | Scientific priority and scope — which studies, in what order | H.1 *"Strategia complessiva → Operatore"* |
| H-2 | Governance change, MAJOR approval, spend (`DEFAULT_EXTERNAL_SPEND = 0`, fail-closed) | H.1; J.4 |
| H-3 | Persistent scientific disagreement — floor R3 TRIADIC, derogable only upward; forced consensus is an error | C.1; body § 27 |
| H-4 | Adjudication where H.1's adjudicator authored the object — C.3's `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR` has no solution inside a four-role lab | C.3; H.1 |
| H-5 | Public push — reading `git diff origin/main..main --stat` is *"the one judgement no gate makes"* | root `CLAUDE.md` |
| H-6 | Anything therapeutic — never a substitute for a treating clinical team | root `CLAUDE.md` |

**(b) Blocked only by missing infrastructure — one-time unblocking acts, not recurring costs**

| # | Act | Why it is one-time |
|---|---|---|
| H-7 | Role-contract activation — `DEC-20260822` consequence 3: *"A new, explicit activation act is required"*; it *"does not perform it, does not schedule it, and does not specify its form"* |
| H-8 | Authorising an event-ledger writer — P7 chose the design; `M4` is `BLOCKED` for want of a writer |
| H-9 | Authorising a control-plane validator — the L2 record registers `REGISTRY VALIDATOR: MISSING INSTRUMENT` and states building it is *not authorized to anyone* |
| H-10 | Ruling on `scientist_reading_modes.md`'s status — all three activation clauses measure SATISFIED while the status line still reads `PROPOSED` |
| H-11 | Setting `MIRROR_RETROSPECTIVE` cadence `N` — `UNASSIGNED` by the annexes to anyone; G.2 bars Mirror from setting it alone |
| H-12 | `scientist-c` ACTOR_ID confirmation — `PROPOSED`, fixed once at its own registration |

**(c) Mechanical in nature, performed by a human today**

Each row is coordination a machine could in principle perform. **Not one can be automated today**,
because each depends on the event ledger (F-2) or on refs-in-addresses (F-7). Listing them measures
where human effort goes; it does not propose automating any of them.

```
being the transport between actors        · reconciling the forked approval queue
finding which ref carries an artifact     · noticing an unanswered review (a join on two file sets)
noticing that a canonical statement went stale
detecting a dead or absent actor (HEARTBEAT + 3-miss DOWN is fully specified and has never run)
assembling the OPERATOR_DAILY_BRIEF (§ 10.4 enumerates its contents exactly; all inputs are durable)
detecting a duplicated claim on one TASK_ID + GENERATION
watching the lease window between turns
```

**The accounting, and the honest reading.**

```
MUST REMAIN HUMAN                6   recur per batch or per decision
ONE-TIME UNBLOCKING              6   discharged once, by someone with the authority to discharge them
MECHANICAL, CURRENTLY HUMAN      9   every one blocked on the same two absences
```

🔴 **Human effort today is dominated by transport and reconciliation, not by strategy.** The six
structural gates are genuinely irreducible and are **not** where the load is. This agrees with the
sibling analysis and is re-derived here.

🔴 **And the instrument that would prove or refute that sentence does not exist.** Body § 7 assigns
the measurement explicitly — *"Mirror mantiene l'AUTONOMY LEDGER … HUMAN_REQUIRED PREVENTABLE vs
UNAVOIDABLE, ore bloccate, false escalation … Obiettivo: ridurre PREVENTABLE"* — and the autonomy
ledger measures **0/47**. The dispatch's core question, *"without increasing human load again,"*
currently has **no instrument that can answer it**, and G.3 names the autonomy ledger as that
instrument. This is the single most direct answer this analysis can give to the dispatch: **the
laboratory cannot presently measure the quantity the dispatch asks it to minimise.**

### F-9 · THE SCIENTIST PIPELINE — the dispatch's six questions, answered from evidence

| Question | Answer as measured |
|---|---|
| **Where is the task born?** | In an Annex A.1 `TASK_ASSIGNMENT` written by Orchestrator (H.1 row 1). 🔴 **This has never happened.** All 5 task records were written by `plan` about `plan`, one of them stating in its own note that no Orchestrator was reachable |
| **How is it assigned?** | `TASK_ASSIGNMENT` → `TASK_ACK` (mandatory on `STATE_CHANGE: yes`) → durable `TASK_CLAIM` before any work. 🔴 **No `TASK_ACK` exists for any task**; every claim on record is self-claimed with no counterparty |
| **How is it frozen?** | `TASK_COMPLETE` declared to Plan for freezing before anyone else reads it (`controlled_benchmark_ab.md`). 🔴 **Freezing is a handoff, and handoff has no closing event (F-3)** — so the freeze is attestable only by promise |
| **How is contamination avoided?** | Independence is a property of the **surface**, not of a promise: an enumerated, digested benchmark surface rather than a LEGEND checkout, because a LEGEND checkout contains prior outputs. Forbidden in both modes: reading the other reader's output, and **asking Orchestrator to relay content** — *"the same, by another channel."* 🔴 Detection is *"by construction of the records"*, and **there is no lock** (J.0). It guarantees a duplication cannot exist without leaving two contradictory records; it does **not** guarantee nobody opens the same PDF twice |
| **When does Mirror enter?** | **After freezing**, and its object is the **process**, not the paper. `MODE B` is explicitly *not* a review of `MODE A` — *"a second reader is a second reader."* Mirror holds no command and produces no primary evidence; its review of Orchestrator is ex post and pattern-based, never a veto ex ante. 🔴 **Mirror's designated primary input — the consolidated event ledger (G.3) — measures 0/47** |
| **When is the human needed?** | Per F-8: at H-1…H-6 structurally, and at H-7…H-12 once. 🔴 Plus one precondition: body § 8 requires assignment on **VERIFIED** capabilities, and the record carrying verified capability rows (`runtime/L2-OUTCOMES.md`) is reachable from **1 of 47** refs — not from `main`, where `controlled_benchmark_ab.md` P-3 canonically asserts the opposite |

---

## CURRENT_STATE

```
A PAPER can reach:      discovered → screened → processed → claim_linked → integrated
                        with a hash-chained receipt at the reading step, a manifest and locator
                        audit at the analysis step, and a LINT-gated BATCH_COMMIT at integration.
                        128 receipts. 390 literature records. 39 claims. 7 gates passing.
                        🔴 and its state field is validated by nothing (F-5).

A TASK can reach:       creation — by one actor, about itself.
                        Nothing further is observable. 0 ACKs. 0 events. 0 adjudications.
                        0 closures. The closing instrument for 7 of 9 states does not exist
                        as a file on any of 47 refs.
```

**The system is not half-built. It is two systems at very different maturities**, sharing a
repository and a vocabulary:

- The **scientific pipeline** is operational, instrumented, and has survived real failures that
  left scars in the code (`reading_state.py`'s parallel-read incident; `locator_audit`'s
  `unauditable` split; the receipt output-path corrections in the ledger's own `workflow` field).
- The **control plane** is fully specified and almost entirely uninstantiated. Its governance text
  is more careful than most running systems; its installed base is five task records and one lease
  script.

🔴 **The dispatch's premise — that LEGEND needs to move from Scientist preparation to a running
pipeline — is measured as correct, and the obstacle is not in the scientific layer.** Every
scientific state the pipeline needs (3, 4) already closes. Every state that fails (1, 2, 5, 6, 7,
8, 9) is a control-plane state.

---

## TARGET_STATE

> **This section states what the repository's own text requires for each state to close. It is not
> a build plan, it recommends nothing, and it assigns nothing.** Where the repository names an
> owner, the owner is named; where it does not, the cell is blank.

### T-1 · The minimum set, derived from F-1 rather than proposed

For the nine states to become observable, exactly four things are missing. They are not
independent, and the dependency direction is measured, not assumed.

```
(1) AN EVENT WRITER          — J.1 shape, P7 design (a), on the pattern already running in
                               fulltext_receipts.py. Unblocks closure for states 1,2,6,7,8,9.
                               Owner: design → Plan (DONE). Writer → authorised to NOBODY.

(2) A REF IN EVERY ADDRESS   — a DURABLE_POINTER that resolves. Unblocks F-7's fork, the stale
                               canonical precondition, and cross-actor handoff.
                               Owner: cross_session_transport.md, status PROPOSED, binds nobody.

(3) A HANDOFF CLOSURE        — state 5 has no event type in J.1's 23 and no receiver trace in any
                               of its 15 artifacts. This is the state the A/B freeze depends on.
                               Owner: nobody. J.1 extension or a separate instrument — Q-1.

(4) A CONTROL-PLANE VALIDATOR— 0 scripts read an A.1, A.6, B.1, C.2 or J.3 object. F-5 shows what
                               an unvalidated state field becomes even in the layer that works.
                               Owner: L2 record — "not authorized to anyone", "needs a separate
                               authorization".
```

**(1) and (2) are the interlock.** Seven of the nine mechanical human steps in F-8(c) are blocked
on one or the other. (3) is downstream of (1). (4) is independent of all three and is the only one
whose absence is already visibly costing something in the working layer (F-5).

### T-2 · What each state would need, specifically

| State | To become observable it needs | Already exists |
|---|---|---|
| 1 task creation | an assigner that is not the assignee; `TASK_ASSIGNED` emitted | A.1's 15-field schema, fully specified |
| 2 assignment | a `TASK_ACK` counterparty; `TASK_ACKED`/`TASK_CLAIMED` emitted | A.2, A.3, B.3 fully specified; P3 ACK timeout (PROVISIONAL) |
| 3 reading | ✅ **nothing** | the receipt ledger, at 128 events |
| 4 analysis | ⚠️ only step 5 of the acceptance test, which is agent-conducted by design | manifest verifier + locator audit, both running |
| 5 handoff | an event type and a receiver-side closure | B.1 envelope; 15 incompatible precedents |
| 6 review | `REVIEW_OPENED`/`REVIEW_CLOSED`; a join that surfaces the 32 unanswered reviews | C.2, the strongest object in the lifecycle |
| 7 adjudication | `CHALLENGE_ADJUDICATED` emitted; an event type for scientific disagreement (C.1 R3) | F.2 verdict vocabulary; J.3 queue (forked, F-7) |
| 8 closure | the closing event carrying `CLOSES_EVENT_ID` | J.1's rule, precisely stated; `prior_receipt` as a working precedent |
| 9 learning | `LEARNING_INDEX`, `ACTIVE_LESSONS`, and Mirror's input surface | the raw archive, intact and lossless |

### T-3 · The two ledgers, and the question nobody has settled

If the event ledger is built exactly to J.1's minimum list, states 3 and 4 remain outside it and
state 5 remains uncovered (F-2.1). Three readings are available and **this record does not choose
between them**:

1. extend J.1's minimum list (a governance change, MAJOR by H.2);
2. keep two ledgers with a declared, validated join (the receipt ledger stays sovereign for
   reading; events reference receipts by `event_id`);
3. treat reading and analysis as *durable state* rather than events, on the grounds that J.1
   already declares *"lo stato repo resta sovrano … il ledger è audit e analisi, mai seconda fonte
   di verità"* — in which case the join is a query, not a schema.

Reading 3 has the strongest textual support and the weakest instrument support. Registered as
**Q-1**.

### T-4 · What would NOT change

Nothing above touches: the four scientific current files, which change only through `BATCH_COMMIT`;
the LINT and release gates; the receipt chain; the R3 floor on persistent disagreement; the six
structural human gates in F-8(a).

### T-5 · What the dispatch asked that measurement cannot answer

*"Without increasing human load again"* presumes a baseline. **The baseline instrument is the
AUTONOMY LEDGER (G.3, body § 7) and it measures 0/47.** Any claim that a change reduced or
increased human load — including any claim this record could make — is currently unfalsifiable.
The dispatch's success criterion has no meter.

### T-6 · 🔴 The constraint on every row above — and it is already normative

The dispatch closes with *"do not optimise cost/token/context if it reduces the quality of the
scientific reading."* That is not an external preference; it is already binding text, and it names
the exact failure mode:

> `scientist_reading_modes.md`: *"Compressing depth or coverage for token, time or cost — a
> reading shortened for budget produces a receipt that overstates itself; the cost stop condition
> is J.4's and is declared, not silently absorbed into the reading."*

Two consequences for anything in TARGET_STATE:

- **Step 5 of the acceptance test — the blind locator audit — is the step that catches a careful
  reading that says more than its source, and it is the step that is skipped first under time
  pressure.** It is agent-conducted by design. Any efficiency measure that scripts it away is
  removing the only check on the failure it exists to catch. `locator_audit.py` is a precondition
  of step 5, not step 5.
- **Batch size for a first cycle is PICCOLO — 1–2 PMID each** (body § 41), with full throughput
  only from the second batch. That is a quality constraint stated as a throughput constraint, and
  it is the correct order of the two.

---

## BLOCKERS

Measured conditions standing between the current system and the pipeline the dispatch describes.
**Listed, not solved.** Ownership is named where the repository names it, and left blank where it
does not.

| # | Blocker | Evidence | Owner per repository |
|---|---|---|---|
| **B-1** | 🔴 **No event stream.** 23 J.1 types, **0 emitted** across 46,125 harvested jsonl lines; `ledger/events/` and `ledger/consolidated/` **0/47** | F-2 | design → Plan (done). **Writer → nobody** |
| **B-2** | 🔴 **Three of the nine states have no event type at all** — reading, analysis, handoff. Building J.1 as specified does not close them | F-2.1 | unassigned — **Q-1** |
| **B-3** | 🔴 **Handoff has no closure, and the A/B freeze is a handoff.** 15 artifacts, 6 shapes, 0 receiver traces | F-3 | unassigned |
| **B-4** | 🔴 **A path without a ref is not an address.** The approval queue has forked into 3 disjoint contents; `main` carries 2 of 21 decision IDs | F-7 | `cross_session_transport.md` is `PROPOSED` and binds nobody |
| **B-5** | 🔴 **No control-plane validator of any kind.** 0 scripts read an A.1, A.6, B.1, C.2 or J.3 object | S-5 | L2: *"not authorized to anyone"* |
| **B-6** | 🔴 **The working lifecycle's state field is unvalidated.** `split_blocks` cannot match `## LIT-0085`; 17 composite values, 1 undeclared status, 10 records with no status; LINT passes | F-5 | — (new; not previously recorded) |
| **B-7** | 🔴 **The quantity the dispatch asks to minimise has no meter.** AUTONOMY LEDGER 0/47 | F-8 | G.3 → Mirror; cadence `N` **UNASSIGNED by the annexes to anyone** |
| **B-8** | ⚠️ **No ACK, therefore no failure detection.** 0 `TASK_ACK` records; `HEARTBEAT` has never run; P3/P4 are PROVISIONAL and expire on evidence *"from the event ledger (J.1)"* — an event that cannot occur | F-1 state 2 | B.3; P3/P4 |
| **B-9** | ⚠️ **Review closure at 8 of 40.** C.2: silence is not acceptance | F-6 | the author of each reviewed object |
| **B-10** | ⚠️ **The learning loop has a raw archive and nothing downstream.** `LEARNING_INDEX` 0/47, `ACTIVE_LESSONS` 0/47, Mirror's designated input 0/47 — while body § 15 makes consulting the index mandatory | F-1 state 9 | E.2: durability → Plan, epistemic curation → Mirror; **H.1's only row with no authority named** |
| **B-11** | ⚠️ **No `OPERATOR_DAILY_BRIEF`.** § 10.4 requires it at least once per working day; it is the surface exposing `PENDING HUMAN DECISIONS` | S-3 | body § 8 → Orchestrator |
| **B-12** | 🔴 **The role contracts are non-binding** — `DEC-20260822`: `ACTIVATION_NOT_CONFIRMED`. No actor authority may be assumed from them | `DEC-20260822` | operator (H.1) |

**B-1 through B-4 are one problem observed at four points.** Without events there is no closure;
without refs in addresses durable state is not reachable; the queue fork and the handoff gap are
both that same absence operating on replicated files. **This record does not propose which of them,
if any, is the right place to intervene.**

---

## OPEN_QUESTIONS

Each is a measured fact that someone with authority must dispose of. **None is resolved here, and
none is assigned to anyone.**

| # | Question | Disposition owner |
|---|---|---|
| **Q-1** | **Reading, analysis and handoff have no J.1 event type.** Extend J.1's minimum list (MAJOR under H.2), keep two ledgers with a declared join, or treat reading/analysis as sovereign durable state with a query rather than a schema? J.1's own sovereignty clause supports the third and no instrument implements it | operator (governance change) / Plan (design) |
| **Q-2** | **The literature log's state field is unvalidated (F-5).** Is `completed` a status to be declared, or 17 records to be normalised? Is a composite `state — <wikilink> (batch)` value intended? Both readings are defensible and the answer determines whether a validator would flag 18 records or 0 | Plan (schema) / operator |
| **Q-3** | **The dispatch places review and adjudication inside the Scientist pipeline; C.3 and H.1 place both outside it.** This record modelled them as the repository defines them (TASK_STATUS) | operator |
| **Q-4** | **`MIRROR_RETROSPECTIVE` cadence `N` is `UNASSIGNED` by the annexes to anyone**, and G.2 bars Mirror from setting it alone. Two PROVISIONAL practices expire on an event that therefore cannot be scheduled, against E.3's *"Mai provisional per sempre"* | operator |
| **Q-5** | **`controlled_benchmark_ab.md` P-3 is canonical on `main` and both its clauses are contradicted by records reachable from 1–2 other refs.** Its practical conclusion may nevertheless survive on the unmet capability minima. One ruling settles it; this record does not make it | operator |
| **Q-6** | **The surface enlarges by being analysed** (S-4): four analyses, four branches, ref count rising with each. No instrument observes this. Is concurrent single-writer branch analysis the intended working mode, and if so what reconciles it? | operator / Plan |
| **Q-7** | **B-7 makes the dispatch's own success criterion unfalsifiable.** Should the autonomy ledger precede the changes it is meant to measure? | operator |

---

## NEXT_TRANSITION

### What the measured dependencies imply about ordering

This is an observation about dependencies, **not a recommendation and not a schedule.**

```
B-12 (contracts non-binding)  gates every row where an actor must act under a role
        │                     — it is an operator act, and nothing else unblocks it
        ▼
B-1 (event writer)            gates closure for states 1,2,6,7,8,9 and every DETECTION
        │                     line that routes to a Mirror instrument
        ├─── B-3 (handoff closure) is downstream: a closing event needs a ledger to close into
        └─── B-7 (autonomy ledger) is downstream: it derives from events (G.3)
B-4 (refs in addresses)       independent of B-1; gates cross-branch reachability
B-5 / B-6 (validators)        independent of both; B-6 is the only blocker whose cost is
                              already visible in the layer that works
```

🔴 **One ordering observation this record does assert, because it is arithmetic rather than
judgement:** B-7 measures the quantity the dispatch asks to minimise, and it derives from B-1. Any
change made before B-1 exists cannot be evaluated against the dispatch's own criterion. That is a
statement about evidence, not about priority.

### What this record leaves behind

```
STATE            one new file on branch orch-scientific-pipeline-lifecycle-model
main             UNCHANGED — not written, not staged, not advanced
governance/      UNCHANGED       roles/     UNCHANGED
framework/       UNCHANGED       ledger/    UNCHANGED
NEW MEASUREMENTS F-2 (0/23 event types emitted, with harvest positive control)
                 F-2.1 (three states uncovered by J.1's vocabulary)
                 F-4 (the receipt ledger already implements J.1's shape and derived-view rule)
                 F-5 (the working lifecycle's state field has no validator)
                 F-8 (the autonomy ledger, the missing meter for the dispatch's own question)
                 S-4 (the surface enlarges by being analysed)
RE-DERIVED       F-6, F-7 — independently, agreeing with the sibling records
```

### What iteration 2 could measure that this one did not

- Whether the 10 literature records with no `Status:` field are incomplete records or a distinct,
  undeclared state.
- Whether the 32 unanswered reviews are unanswered or answered on a ref not surveyed here — F-6
  counted filenames across 47 refs, which is a join on file sets, not on content.
- The `refs/codex` and `refs/stash` surfaces, explicitly not surveyed (S-1).
- Whether any of the 15 handoffs was in fact received, by looking for receiver-side artifacts that
  do not carry the word `HANDOFF` — this record searched by name and would not have found them.

---

## What this record does NOT do

- It does **not** activate any role contract, or perform the act `DEC-20260822` consequence 3 requires.
- It does **not** confer, claim or imply Orchestrator authority. The only authority exercised is
  H.1's `WORK_COMMIT` row, which is allocated to every actor and conditioned on no lease.
- It does **not** create a Task Contract, a `PARALLEL_READ_GROUP`, a review, a Mirror task, or a
  ledger event.
- It does **not** assign a paper, an actor, a batch or a reviewer.
- It does **not** define an event schema, a handoff schema, a validator, or a routing rule.
- It does **not** resolve Q-1 … Q-7, and does not rule on Q-5's canonical/branch conflict.
- It does **not** recommend that the event ledger, or anything else, be built. Naming an available
  pattern (F-4) is not authorisation to apply it.
- It does **not** verify any capability, or lift any hold.
- It is **not** an `INTEGRATION_CANDIDATE` and **not** a `CANONICAL_BATCH_COMMIT`. It is a
  `WORK_COMMIT` on its own branch, and nothing more.

---

## Validation

| Constraint | Result |
|---|---|
| no implementation | ✅ no instrument, schema or validator written |
| `governance/` unmodified | ✅ verified by `git diff --stat` |
| `roles/` unmodified | ✅ |
| `framework/` unmodified | ✅ |
| `ledger/` unmodified | ✅ |
| artifact on own branch via `WORK_COMMIT` | ✅ `orch-scientific-pipeline-lifecycle-model`; `main` untouched |
| authority not assumed from the role contract | ✅ every rule traced to the body or a named annex |
| reading quality not traded for cost | ✅ T-6; and the constraint was already normative |
| exactly one file changed | ✅ |

**Gates re-run after writing, from the branch worktree.**

```
legend_lint.py .                PASS
fulltext_receipts.py verify     OK: 128 chained receipt(s), tail anchored
growth_anchors.py check         PASS
public_release_gate.py          BLOCKS: 0     ← only after the correction below
lease_state.py --check          ACTIVE by derivation: 0
```

🔴 **The release gate blocked this record on its first run, on two defects this record
introduced**, and both are recorded rather than quietly fixed:

- `DIRECT_IDENTIFIER` — F-8 named the operator by given name. This is the public edition; a
  given name is a direct personal identifier, and the gate is the instrument that catches it.
  Replaced with *"the operator"*, which every other section already used.
- `BROKEN_WIKILINK` — two illustrative double-bracket placeholders, written as examples of the
  composite status values measured in F-5, are wikilinks by construction and resolved to nothing.
  Rendered as `<wikilink …>` instead. **The first attempt at this very sentence tripped the gate a
  third time**, because a sentence explaining a broken wikilink had a literal one in it.

**Both defects were in prose about privacy and about link integrity respectively — written by an
author who had just measured that the one lifecycle that works has an unvalidated state field
(F-5).** The gate that caught them is a control-plane validator for the *publication* boundary,
and it is the only one of its kind in the repository (S-5). This is a small, first-hand instance
of B-5: where a validator exists, a careful author's defect is caught in seconds; where none
exists, it is not caught at all.

**Domain and collision disclosure.** `learning/` is content, not control plane (P5.1). This record
therefore moves the candidate content hash of any future candidate that re-aligns onto this branch.
`learning/orchestrator/` is occupied on branch `orchestrator` by 11 `SLR-*` files and on three
other branches by non-`SLR` analyses; this record uses a non-`SLR` name so it is not mistaken for a
Session Learning Record under Annex E.6. **Directory-level convergence at merge remains an open
risk and is flagged, not solved** — it is Q-6 in operational form.

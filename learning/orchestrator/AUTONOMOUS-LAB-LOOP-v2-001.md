---
artifact: ANALYSIS — the minimal operating cycle, and what it is actually blocked by
record_id: AUTONOMOUS-LAB-LOOP-v2-001
task_id: AUTONOMOUS_LAB_LOOP_v2_ANALYSIS
dispatcher: operator
author_session: worktree `wt-lab-loop-v2`, branch `orch-autonomous-lab-loop-v2`, based on `main` @ 788c357
actor_id: NOT ESTABLISHED — see § 1. This record is not authored under a role contract.
date: 2026-08-22
governance_version: 3.1.1 (read, not exercised)
classification:
  - ANALYSIS ONLY
  - NOT IMPLEMENTATION
  - NOT ACTIVATION
  - NOT GOVERNANCE
  - NO SCHEMAS DEFINED
domain: >
  CONTENT. `learning/` is not a CONTROL_PLANE_ROOT — P5.1 lists exhaustively
  `governance/candidates/`, `ledger/`, `reviews/`. This record therefore sits inside the
  CANDIDATE_CONTENT_HASH of any future candidate that re-aligns onto its base.
not_an_slr: >
  This is not a Session Learning Record and Annex E.6 does not govern it. The `SLR-` prefix is
  deliberately not used, so that the two classes are not conflated.
authority_claimed: none
supersedes: nothing
---

# AUTONOMOUS LAB LOOP — v2 · ANALYSIS 001

> **ANALYSIS ONLY · NOT IMPLEMENTATION · NOT ACTIVATION · NOT GOVERNANCE**
>
> Nothing here assigns work, activates a contract, confers authority, resolves a finding,
> defines a schema, or authorizes a session to open. It analyses a cycle that **could** be run
> once decisions are made that are not made here and are not mine to make.

---

## 0 · The four exclusions, stated before the analysis rather than after it

The dispatch named three exclusions and one prohibition. They are honoured as follows, and each
is checkable against the text of this record.

| Exclusion | How it is honoured here |
|---|---|
| NOT implementation | No file outside `learning/` is created or edited. No script is written. |
| NOT activation | No lease is acquired, no contract is read as binding, no actor is addressed. |
| NOT governance | No frozen annex is modified, quoted as changed, or reinterpreted. |
| No schemas | Every field named below is cited **from an annex that already defines it**. No record format, key set or file layout is invented. Where an object is missing, this record says *what question it would answer* — never *what fields it would carry*. |

The last one deserves a sentence of its own, because it is the easiest to violate accidentally.
An analysis of a dispatch loop drifts into schema design the moment it writes "the queue entry
would contain…". This record never completes that sentence. Where § 6 discusses the minimum
handoff, it does so by **mapping the dispatch's six requested items onto fields Annex A.1 and
Annex B.1 already define** — which is the opposite of designing a schema, and is also the
finding.

---

## 1 · Identity — established from repository evidence, not from the dispatch

The dispatch addressed this session as Orchestrator. **Identity is not conferred by being
addressed**, and the repository's evidence does not support the claim.

| Fact | Measured value | Command |
|---|---|---|
| ACTIVE `ORCHESTRATOR_LEASE` | **0** | `python3 framework/scripts/lease_state.py` |
| Most recent lease activity | released `2026-08-18T14:05:20Z` | same |
| Role contracts binding? | **No — all four `PROPOSED`** | `governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` |
| Live sessions in the `orchestrator` worktree | **0** | `claude agents --json`, filtered by `cwd` |

`CLAUDE.md` § 0 is unambiguous about what follows from the first row:

```
IF no valid runtime inventory / no ACTIVE ORCHESTRATOR_LEASE:
    ENTER BOOTSTRAP_MODE.
    Do NOT assume Orchestrator authority merely because you are in root.
```

`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` — an operator determination under H.1, dated today
and present on `main` — settles the second row and states the consequence directly:

> **No actor authority may be assumed from these contracts.** Any authority an actor exercises
> must be traced to the governance body or to a named annex […] never to a role contract clause
> standing alone.

**Therefore this record is authored by a session with no ACTOR_ID, no lease and no contract.**
That is not a disclaimer bolted on for form. It is load-bearing twice over:

1. It is why nothing here is an assignment, an approval, or a specification.
2. 🔴 **It is itself a measurement of the subject matter.** A record analysing how the
   Orchestrator should run a loop is being written by a session that cannot demonstrate it is
   the Orchestrator. The office the loop is designed around is, at this instant, **vacant** —
   and § 9 shows that this is *not* the binding constraint, which is the least obvious finding
   in this record.

---

## 2 · Surface map — what was read, and on which ref

### 2.1 · There is no v1

The filename says `v2`. Measured across every local ref:

```
git grep -l -i "AUTONOMOUS.LAB.LOOP" $(git for-each-ref --format='%(refname:short)' refs/heads)
  → empty
```

**No `AUTONOMOUS-LAB-LOOP` record of any version exists anywhere in this repository.** The `v2`
in the name refers to something outside the repository — a conversation, an earlier framing, or
the operator's own numbering. It is recorded as unresolved rather than reconstructed, because
inventing a v1 to justify a v2 would be exactly the kind of convenient reconstruction the
epistemic discipline exists to prevent. Nothing in this analysis depends on what v1 was.

### 2.2 · 🔴 Six sibling analyses exist, and none of them is on `main`

`learning/orchestrator/` across all local refs:

| Ref | Record |
|---|---|
| `main` | `SCIENTIFIC-PIPELINE-PREPARATION-001.md` — the only one on `main` |
| `orch-autonomous-dispatch-loop` | `AUTONOMOUS-DISPATCH-LOOP-MODEL-001.md` |
| `orch-lab-director-operating-model` | `LAB-DIRECTOR-OPERATING-MODEL-001.md` |
| `orch-agent-coordination-protocol` | `LEGEND-AGENT-COORDINATION-PROTOCOL-001.md` |
| `orch-pipeline-loop-architecture` | `ORCHESTRATOR-SCIENTIFIC-PIPELINE-AND-LOOP-ARCHITECTURE-ANALYSIS-001.md` |
| `orch-control-plane-reconciliation` | `CONTROL-PLANE-RECONCILIATION-ANALYSIS-001.md` |
| `orch-scientific-pipeline-lifecycle-model` | `SCIENTIFIC_PIPELINE_LIFECYCLE-MODEL-001.md` |
| `orchestrator` | 11 × `SLR-*` (session learning records, a different class) |

Seven analyses of the same subject matter — this one included — sit on seven branches that
cannot see each other. **This record does not synthesize them and does not defer to them.**
Every number in § 3 was measured in this session against the installed runtime and the local
refs, not read off a sibling. Where a sibling reached a conclusion this record also reaches, the
convergence is independent, not inherited.

🔴 **The seven branches are themselves the primary evidence for the dispatch's own premise.**
Seven parallel analyses, each opened by a prompt the operator transported by hand into a
separate session, is what "manual prompt transport" looks like when you measure it instead of
describing it. The cost is visible in the table above: `main` carries one of the seven.

### 2.3 · Method

Four epistemic classes are used, taken from
[`governance/design_records/runtime_harness_probe_20260819.md`](../../governance/design_records/runtime_harness_probe_20260819.md)
§ 0 rather than invented here:

```
DOCUMENTED   stated by an official surface of the installed runtime
OBSERVED     reproduced in THIS session, with the command recorded beside it
PROPOSED     LEGEND's own design intent; describes nothing that exists
ABSENT       searched for across the surveyed surface and not found
```

Nothing was promoted to `OBSERVED` by appearing in this session's conversation, in the dispatch,
or in a sibling record.

---

## 3 · The six measurements the rest of this record rests on

All taken 2026-08-22, root checkout at `788c357`, against all local refs.

### M-1 · The event ledger of Annex J.1 does not exist — on any ref

```
OBSERVED   find . -iname "*event*"                                             → no ledger file
OBSERVED   git grep -l "EVENT_ID\|event_ledger\|events.jsonl" <all refs> -- 'ledger/*'  → empty
```

Annex J.1 specifies it in full — 23 event types, `CLOSES_EVENT_ID` linkage, strict append-only,
replay semantics — and delegates one open choice to Plan: *"(a) event file per-attore nel proprio
worktree […] oppure (b) eventi derivati da commit + messaggi ACKati."* **That choice has not been
made, and consequently nothing has been built.** `governance/plan_defined_parameters.md`
frontmatter still lists `J.1 ledger design` among its delegated parameters.

This single absence removes the input of **DISCOVER** and the signal of **MONITOR**
simultaneously. It is the load-bearing gap, and §§ 4 and 7 both terminate on it.

### M-2 · The task and checkpoint ledgers exist for exactly one actor

```
OBSERVED   ledger/tasks/        → 1 directory: plan/        5 task records
OBSERVED   ledger/checkpoints/  → 1 directory: plan/       19 checkpoint records
OBSERVED   ledger/approvals/    → HUMAN_APPROVAL_QUEUE.jsonl
OBSERVED   ledger/retirements/  → 1 record
```

There is no `ledger/tasks/orchestrator/`, no `ledger/tasks/mirror/`, no
`ledger/tasks/scientist-*/`. Of the five task records that do exist, the one read in full
(`XPORT-ROUTING-001`) carries `"ORIGIN": "OPERATOR"` and this note:

> "No TASK_ASSIGNMENT message was received. This task was opened by an operator session
> instruction […] delivered directly to this actor […] no ACTIVE ORCHESTRATOR_LEASE existed at
> any point in this session, and no Orchestrator was reachable to assign it."

🔴 **The single richest task record in the laboratory documents, in its own metadata, that the
dispatch loop was not used to create it.** The ledger is not empty because the lab is idle; it is
partial because work arrives by a route the ledger does not describe.

### M-3 · `DAILY_BRIEF` is named in seven places and exists in none

```
OBSERVED   grep -ril "DAILY_BRIEF" → 7 files, all of them normative or candidate text:
             governance/GOVERNANCE_v3.1.1.md · governance/annex_j_runtime_control_plane.md
             roles/orchestrator.md · deployment/deployment_profile.md
             governance/candidates/{CAND-20260816-GOV311, CAND-20260817-ORCHWT,
                                    HANDOFF-GOV311-ORCHESTRATOR}
ABSENT     no artifact, no generator, no path
```

`roles/orchestrator.md` states the Orchestrator "maintains the `OPERATOR_DAILY_BRIEF`". J.3
requires it to expose `PENDING HUMAN DECISIONS`. **The surface on which the human decision layer
is supposed to become visible has never been instantiated.** § 5 and § 9 both return to this.

### M-4 · Thirty-six live sessions, zero leases, and a worktree population that does not match the actor table

```
OBSERVED   claude agents --json → 36 rows, all kind=interactive
             legend-public (root checkout)   16
             evidence-index (plan)           10
             mirror                           9
             lettore-c (scientist-c)          1
             orchestrator                     0
             lettore   (scientist-a)          0
             lettore-b (scientist-b)          0
OBSERVED   python3 framework/scripts/lease_state.py → ACTIVE by derivation: 0
```

Read against the `runtime_harness_probe` § 6 cardinalities, the state has not improved since
2026-08-19 — it has intensified. `plan` and `mirror` are `MANY` (10 and 9). `scientist-a` and
`scientist-b` are `ZERO`. `orchestrator` is `ZERO` in its own worktree and `16` in the root
checkout, which is the contested-source problem of probe § 10 at more than five times the
population it was measured at.

🔴 **A dispatch loop needs to name one recipient per actor. For four of six actors, the number of
candidate recipients today is not one — it is 0, 9, 10, or 16.**

### M-5 · The `HUMAN_APPROVAL_QUEUE` has forked across refs, and no ref carries the union

This is the queue that *holds the human decision layer*. Counted as **distinct record ids**
(`APPROVAL_ID | RESOLUTION_ID | CORRECTION_ID`), which is the unit that matters — one physical
line can carry two ids, and § M-6 shows why:

| Ref | Distinct records | Contains |
|---|---|---|
| `main` | **5** | the GOV311 core — and it is a strict subset of every ref below |
| `orchestrator` | **13** | core + SUNSET-DEC3, SCIAB, XPORT, P5DOMAIN (request + resolution each) |
| `evidence-index` | **13** | core + HA-1…HA-4 (request + resolution each) |
| `p51c9-rebased-onto-c89c2217` | **13** | id set **identical** to `evidence-index` |
| every other ref (22) | 5 | identical to `main` |
| **union across all refs** | **21** | carried by no ref |

```
OBSERVED   union over $(git for-each-ref refs/heads), keyed on the three id fields  → 21
OBSERVED   richest single ref = 13.   main = 5.   main ⊂ orchestrator, main ⊂ evidence-index
OBSERVED   orchestrator \ evidence-index = 8 ids (SUNSET-DEC3, P5DOMAIN, SCIAB, XPORT × APR+RES)
OBSERVED   evidence-index \ orchestrator = 8 ids (HA-1…HA-4 × APR+RES)
```

🔴 **No ref carries the union, and the two richest refs are not a superset/subset pair — they are
two disjoint extensions of a common core of 5.** `orchestrator` holds eight records
`evidence-index` has never seen, and `evidence-index` holds eight that `orchestrator` has never
seen. Each ref is internally append-only and locally consistent — J.1's discipline is being
followed exactly — and the histories are nonetheless divergent. Append-only guarantees that no
record is *lost*; it guarantees nothing about any one reader being able to *see them all*.

### M-6 · 🔴 The obvious machine predicate over that queue returns 100 % false positives

If an automated loop wanted to answer *"what is waiting on a human?"*, the predicate that any
reader would write first is `STATE == "PENDING"`. Run against the real file:

| Ref | `STATE == "PENDING"` returns | Actually unresolved |
|---|---|---|
| `main` | `APR-20260816-GOV311-001`, `APR-20260816-GOV311-002` | **0** |
| `orchestrator` | the same 2 | **0** |
| `evidence-index` | those 2 + `APR-20260817-HA-1…4` → 6 | **0** |

Every hit is a false positive. The true pending count on every ref is zero. The cause is visible
in the raw file, which carries **two different encodings of resolution in the same ten lines**:

```
lines 2–5   request line (STATE: PENDING) + SEPARATE resolution line (RESOLVES_APPROVAL_ID …)
            → the request line is never edited, and stays PENDING forever by design
lines 7–10  ONE line carrying BOTH "APPROVAL_ID" and "RESOLUTION_ID" and STATE: APPROVED
            → request and resolution fused into a single record
```

Both are defensible readings of J.1's *"state changes by appending, never by mutating"*. The
first is the stricter one and the file's own `_schema` note describes it. The second appeared
later. **Neither is wrong; together they are unreadable by one predicate**, and a correct reader
must resolve `STATE: PENDING` against the set of `RESOLVES_APPROVAL_ID` values elsewhere in the
file — which is exactly the derived-view construction J.1 assigns to Plan and which nothing
currently performs.

---

## 4 · DISCOVER — how the Orchestrator finds available work

### 4.1 · The dispatch's four inputs, tested against the measured surface

| Input | Where it would be read | State |
|---|---|---|
| **open tasks** | `ledger/tasks/<actor>/` | `PARTIAL` — exists for `plan` only (M-2); 5 records, one of which documents that it was not dispatched |
| **previous outputs** | `WORK_COMMIT` history per branch | `AVAILABLE` — git is the one surface that works; see 4.2 |
| **blockers** | `BLOCKER` messages (B.2) → event ledger | `ABSENT` — the message type is defined, the durable record it would land in does not exist (M-1) |
| **pending reviews** | `reviews/<actor>/`, `REVIEW_OPENED`/`REVIEW_CLOSED` events | `PARTIAL` — 3 author-response files on `main`; the open/close events are in the ledger that does not exist |

### 4.2 · The one discovery surface that actually works, and its exact limit

Git is the only input above that is complete, durable, multi-writer-safe and already
mechanized. `WORK_COMMIT` is required of every actor at milestone granularity (A.7, H.1), so a
branch tip is a real statement about what an actor has finished.

🔴 **But a commit records what was *completed*, never what is *waiting*.** That asymmetry is the
whole of the DISCOVER problem. Of the four inputs, git answers one — *previous outputs* — and is
structurally incapable of answering the other three, because open tasks, blockers and pending
reviews are all statements about work that has **not** produced an artifact yet.

This is precisely the gap J.1 was specified to fill: an append-only event stream whose opening
events (`TASK_ASSIGNED`, `REVIEW_OPENED`, `HUMAN_REQUIRED_OPENED`) have no closing event yet.
*Open* is defined in J.1 as an unclosed `CLOSES_EVENT_ID` chain — detectable by replay, with
"aperture senza chiusura oltre soglia" named as its own DETECTION condition.

### 4.3 · What DISCOVER reduces to

```
DISCOVER = replay(event ledger) → the set of opening events with no matching CLOSES_EVENT_ID
           reconciled against the durable repo state, which J.1 declares sovereign in conflict
```

Both halves are specified. Neither is built. **DISCOVER is not an unsolved design problem in
LEGEND; it is a specified object that was never materialized** — and § 9 treats it as
construction, not design.

One constraint on that construction is already fixed by law and is easy to violate: J.1 forbids
a mutable status field. A queue file whose rows are flipped from `open` to `closed` is the
natural implementation and is **prohibited**. The queue must be a *derivation* over an immutable
stream, recomputed on read. M-6 is what happens when that rule is half-followed: the queue is
immutable, and nothing derives the view.

---

## 5 · DECIDE — separating machine decisions from human decisions

### 5.1 · The split is already law, and does not need designing

Annex H.1 is the authority matrix, marked `[MAJOR]`. It has **17 rows**. Mapping the dispatch's
two categories onto it:

**Machine-side (the dispatch's "ordering, routing, validation requests")** — all three are
already assigned, and all three to Orchestrator:

| H.1 row | Authority | Dispatch category |
|---|---|---|
| Task / priorità / riassegnazione / generation | Orchestrator | ordering |
| Livello Ladder (≥ floor) e reviewer | Orchestrator | validation requests |
| Classificazione `HUMAN_REQUIRED` ordinaria | Orchestrator | the escalation decision itself |
| Aggiudicazione challenge | Orchestrator (con rationale) | — |
| `CANONICAL_BATCH_COMMIT` | Orchestrator (unico, lease ACTIVE) | — |

**Routing is the exception, and it is the interesting one.** *Routing* in the dispatch's sense —
choosing which actor receives the work — is H.1 row 1 and is fully Orchestrator's. But routing in
the *transport* sense — resolving that actor to a reachable session — appears **nowhere in H.1**,
because it is not a decision. It is a lookup, and § 6.3 shows it is the lookup that does not
exist.

**Human-side** — the operator holds **2 of 17 rows**:

| H.1 row | Authority |
|---|---|
| Spese / MAJOR approval / governance | Operatore |
| Strategia complessiva | Operatore |

J.3 refines the first into five approval types: `MAJOR | SPEND | DESTRUCTIVE | GOVERNANCE |
STRATEGIC`. Annex J.4 fixes `DEFAULT_EXTERNAL_SPEND = 0`, making every paid operation a
human decision by default.

### 5.2 · 🔴 The dispatch's "5 %" is not measurable as a percentage, and the substitution matters

The critical question asks to preserve "the 5 % human decision layer". Measured against the
repository, that number has no denominator:

- **By decision class**, the operator holds 2 of 17 H.1 rows ≈ **11.8 %** — and adding the rows
  that are *conditionally* human (`MAJOR` classification escalated by Mirror fail-closed, plus
  every `SPEND`) raises it further.
- **By decision frequency**, the count is unmeasurable **because the event ledger that would
  count it does not exist** (M-1). J.1 names this exact use: *"autonomy ledger e review yield
  derivano da qui."*

So the honest form of the 5 % is not a ratio to be preserved but a **list to be kept complete**.
The preservable object is the set of decision *classes* reserved to the operator, and the test of
whether the loop preserves it is not "did the human decide 5 % of things" but:

> **Did any decision belonging to one of those classes get made without reaching the operator?**

That question is answerable only if pending human decisions are *observable*. M-3 (no
`DAILY_BRIEF`), M-5 (queue forked across three refs) and M-6 (the obvious predicate returns
nothing true) say that today they are not — on any surface, by any actor.

🔴 **This inverts the critical question's implied ordering.** The question assumes automation is
the change and the human layer is the thing to protect while making it. The measurement says the
human layer is *already* unobservable, six days before any automation exists. Automating dispatch
on top of M-5 and M-6 would not endanger the human layer; it would **inherit a blind spot that is
already there** and make it move faster.

### 5.3 · What a machine may decide without a human, restated as a boundary

```
MACHINE   ordering within a priority class · reassignment on generation+1 · Ladder level at or
          above the C.1 floor · reviewer selection · routing to an actor · ordinary
          HUMAN_REQUIRED classification · retry within RETRY_POLICY.max_attempts

HUMAN     the five J.3 types (MAJOR, SPEND, DESTRUCTIVE, GOVERNANCE, STRATEGIC) · overall
          strategy · anything Mirror classifies MAJOR fail-closed · any external spend, since
          the default envelope is zero

NEITHER   a scientific conclusion. H.1 row 2 assigns it to the responsible Scientist,
          "soggetta a review, mai a ordine". No loop, no operator and no Orchestrator may
          decide it. This row is why the loop is a work router and not a research director.
```

The third block is not padding. A dispatch loop that could set acceptance criteria tightly enough
would decide conclusions by construction, and `roles/orchestrator.md` draws exactly this line:
*"Orchestrator controls what work is done, by whom and in which order. It does not control what
scientific conclusion an agent must reach."*

---

## 6 · DISPATCH — the minimum handoff information

### 6.1 · 🔴 Five of the six requested items are already defined; the sixth has no mechanism

The dispatch asks for the minimum handoff: *source, destination, objective, constraints, expected
artifact, validation*. Mapped onto fields **Annex A.1 and Annex B.1 already define** — no new
field is proposed:

| Requested | Existing field | Defined in | State |
|---|---|---|---|
| **source** | `ACTOR_ID` (identity) + `FROM` (runtime ref, routing) | B.1 | `DEFINED` — and B.1 already separates identity from address, which is the distinction § 6.3 turns on |
| **objective** | `OBJECTIVE` | A.1 | `DEFINED` |
| **constraints** | `SCOPE` (in/out) · `DEPENDENCIES` · `INTERACTION_MODE` · `RETRY_POLICY` | A.1 | `DEFINED` |
| **expected artifact** | `DELIVERABLE` (artefatto + worktree/branch) · `MILESTONE_PLAN` | A.1 | `DEFINED` |
| **validation** | `ACCEPTANCE_CRITERIA` (verificabili) · `REVIEW_REQUIREMENT` (floor, C.1) | A.1 | `DEFINED` |
| **destination** | `TO` (ref) | B.1 | 🔴 **NO MECHANISM** — see 6.3 |

Add the fields that make a handoff *safe to resume* rather than merely complete —
`DIRECTIVE_VERSION`, `GENERATION` (A.1, anti-zombie per A.4), `MESSAGE_ID` and `STATE_CHANGE`
(B.1, dedup and ACK obligation), `DURABLE_POINTER` (B.1) — and the package is fully specified by
frozen governance.

**Conclusion, and it is the one that reorders the priorities: the handoff package is not the
gap.** A.1 defines 15 fields, B.1 defines 8, and between them they cover every item the dispatch
asked for except the address. Designing a handoff format would be re-deriving law that has been
frozen since 2026-08-16.

### 6.2 · The transport primitive is not the gap either

From the harness probe § 3.1 and § 8, `DOCUMENTED` at source and `OBSERVED` at runtime version
2.1.232:

```
DOCUMENTED  SendMessage(to, message, summary) — to: ≤200 chars, no CR/LF; message: NO declared bound
OBSERVED    oversize `to` → InputValidationError before the tool runs. Fail-closed, sender-visible.
OBSERVED    unresolvable target → {"success": false, "message": "No agent named '<x>' is reachable."}
            A structured result object, not an exception.
```

A message primitive exists, it carries an unbounded payload, and it fails **loudly and
legibly**. The longest ACTOR_ID in the laboratory is 11 characters against a 200-character
bound — the address field is not remotely constrained.

Two limits are recorded and neither blocks a dispatch loop:
- `summary` declares `maxLength: 200` and **does not enforce it** — a 264-character summary was
  accepted silently. Enforcement cannot be read off the schema; it was established by probing.
- *"A listed peer is alive and will process your message"* is the runtime's claim about itself
  and stays `DOCUMENTED`. It is **not** `OBSERVED`, and `MESSAGE_TURN_TRUNCATION` was measured
  twice (2026-08-12, 2026-08-14). Delivery is not acceptance.

🔴 **So "eliminating manual prompt copying" is not blocked by the absence of a way to send a
prompt.** The send works. The operator is copying prompts by hand into sessions they select
visually — which is the behaviour of someone who has a transport and no address book.

### 6.3 · What `TO` would have to resolve, and why it cannot today

The harness probe § 9 separates three properties that are routinely collapsed:

```
DISCOVERED   a discovery surface returned a row for it
LIVE         a process exists (pid present, and the pid resolves)
ROUTABLE     LEGEND has decided THIS incarnation is the actor's current one
```

> "Today the laboratory can measure the first two and **has no mechanism at all for the third**."

Re-measured today, that verdict holds and the population has grown (M-4). The four reasons a
resolver cannot be improvised, each measured rather than argued:

1. **Name is a per-session convenience resolver, not an actor address.** 36 live sessions;
   `evidence-index-*` alone is 10 of them. The suffix is launcher-assigned and not derivable
   from the session id.
2. **A name that resolves is not a session that is alive.** `scientist-a` still resolved under
   `--all` three days after that job died, with `pid: null`.
3. **Worktree is not a resolver.** `--cwd` is the only mechanized narrowing predicate the harness
   offers, and today it narrows 36 → 10 for `plan`, 36 → 9 for `mirror`. It does not narrow to 1.
4. **For `orchestrator` the predicate is contested between two canonical sources.**
   `roles/orchestrator.md` says the root checkout; `deployment/deployment_profile.md` says the
   `orchestrator` worktree. Today those read **16** and **0** respectively — *too many* and
   *none*, both off canonical state.

And the failure that makes an improvised resolver dangerous rather than merely unreliable:

> 🔴 `claude --resume <id> --bg` exits **0** with a success-shaped banner and creates a
> **different sessionId under the same name** — a fork wearing the recovered actor's name.
> Exit code 0 from a resume is no evidence of recovery.

The registry's own recorded failure is sharper still: `plan`'s recorded `CURRENT_SESSION_REF` was
verified at L1, is still alive, and is *no longer the current one* — **accurate and stale at the
same time**, which is worse than pointing at a corpse, because nothing about it looks wrong.

### 6.4 · The receiver half, which a sender-only view omits

A.2 forbids work without an ACK; A.3 requires a durable claim before starting, at most one per
`TASK_ID + GENERATION`. Both are receiver-side obligations that a dispatch loop cannot perform on
the receiver's behalf. A loop that sends a perfectly-formed contract to a correctly-resolved
address and receives no ACK has, by B.3, **not dispatched anything** — it must resend, dedup on
`MESSAGE_ID`, and raise a `BLOCKER` on the second miss.

This is where `INTERACTION_MODE` earns its place in A.1: an actor waiting on a question under
`QUESTIONS_ALLOWED` is **inside its contract**, not stalled. A monitor that cannot tell those
apart will report a healthy actor as failed — which is § 7's problem.

---

## 7 · MONITOR — started, completed, failed, waiting

### 7.1 · Each of the four states, and the signal that would carry it

| Question | Signal specified by governance | State today |
|---|---|---|
| **started?** | `TASK_ACKED` then `TASK_CLAIMED` (A.2, A.3) → events (J.1) | `ABSENT` — no event ledger (M-1); no claim record for any actor but `plan` (M-2) |
| **completed?** | `TASK_COMPLETE` event + `CLOSES_EVENT_ID` → the durable milestone evidence of `MILESTONE_PLAN` (A.6/A.7) | `PARTIAL` — the durable half works: `WORK_COMMIT` at milestone granularity is real and auditable. The event half is absent. |
| **failed?** | `RETRY_POLICY` exhaustion → `on_exhaust: PARK` (P1 default) · `ACTOR_DOWN` after 3 missed heartbeats | `ABSENT` — no heartbeat is emitted by anything; `DOWN` is therefore never derivable |
| **waiting?** | `BLOCKED` / `AWAITING_APPROVAL` (A.5) · `HUMAN_REQUIRED_OPENED` (J.1) · `PENDING HUMAN DECISIONS` in the `DAILY_BRIEF` (J.3) | `ABSENT` on every one of the three surfaces — M-1, M-3, M-6 |

### 7.2 · Two structural points about how MONITOR must be built

**It is a derivation, never a poll.** J.1's *"state changes by appending, never by mutating"*
plus its sovereignty clause — *"lo stato repo resta sovrano — in conflitto vince il repo; il
ledger è audit e analisi, mai seconda fonte di verità"* — fix the shape completely. The monitor
view is recomputed from the immutable stream and cross-checked against durable repo state; where
they disagree, **the repo wins and the gap is itself the finding** (J.1 DETECTION: *"incrocio
ledger ↔ stato durevole (gap = evento mancante)"*).

**Absence is not death, and the rule is already written.** From the harness probe, `PROPOSED` and
adopted here as the constraint on any monitor:

```
NOT LISTED  →  UNKNOWN         always
NOT LISTED  →  DEAD            never, unless exhaustive discovery is an OBSERVED,
                               version-bound guarantee for the scope in question
```

Neither discovery surface returns a completeness flag or a truncation marker. A monitor that
reads silence as failure will manufacture `ACTOR_DOWN` verdicts, and the compensating protocol
for a missing failure detector (J.0) is *"heartbeat + DOWN + riapertura operatore"* — an operator
action. Every false `DOWN` therefore spends the scarcest resource the system has.

### 7.3 · Diagnosis precedes accusation, and this is a monitor requirement

`roles/orchestrator.md` and Annex F.4 require `DIAGNOSE` before any non-compliance verdict:
delivery/runtime failure, context failure, task-contract ambiguity, or actual refusal — *"only
the fourth, repeated after clarification"*. Truncated turns and permission prompts are runtime
faults. The harness probe supplies the measured classes a monitor must distinguish rather than
merge — `TOOL_DEFERRED` (observed again in an interactive session), `TOOL_UNAVAILABLE`,
`NOT_EMITTED`, `EMITTED_NOT_ARRIVED`, `MESSAGE_TURN_TRUNCATION`.

🔴 **`TOOL_DEFERRED` is a live cost on the dispatch path specifically.** In the probed session
`ListAgents` was immediately available and `SendMessage` was **deferred**, requiring a schema
fetch first. The cheapest correct sequence — resolve, then send — therefore pays a round-trip
**on the send leg**, which is exactly where `MESSAGE_TURN_TRUNCATION` struck twice. A loop that
treats the send as free is spending the turn boundary with the worst measured record in this
repository.

---

## 8 · LEARN — how a completed cycle becomes reusable knowledge

### 8.1 · This phase is the one that is not missing

Annex E specifies the full lifecycle, and unlike J.1 it has been exercised: 11 `SLR-*` records on
`orchestrator`, 9 `SLR-plan-*` on `main`, plus the correction record `SLR-plan-0006-COR-001`.

```
E.1   OBSERVED → LOCAL → PROVISIONAL → VALIDATING → PROMOTED | REJECTED | SUPERSEDED | EXPIRED
E.2   LEARNING_INDEX — durability: Plan · epistemic curation: Mirror
      confirmation classes: ORIGINAL_OBSERVATION | REPLICATION | EXPOSURE_AFTER_BROADCAST
      only the first two count fully; threshold ≥2, or 1 + Mirror validation
E.3   PROVISIONAL_OPERATIONAL_PRACTICE — hypothesis, success AND failure criterion, expiry,
      rollback. At expiry: PROMOTE | REJECT | EXTEND_WITH_REASON. "Mai provisional per sempre."
E.5   RAW ARCHIVE → Mirror clustering → ACTIVE LESSONS → role subset → rehydration
      lossless raw · derived_from: [LEARN-###] on every lesson · per-role size budget
E.6   Session Learning Record, persisted by WORK_COMMIT at milestone granularity
```

`P4` in `plan_defined_parameters.md` shows the machinery working end to end: the 30/90-minute
heartbeat is registered as `PROV-HEARTBEAT-30M-3X` with an explicit hypothesis, success
criterion, failure criterion and rollback — a textbook E.3 object.

### 8.2 · 🔴 The three ways LEARN is nonetheless blocked, all of them inherited

The lifecycle is sound. Its **inputs and outputs** are the ones that do not arrive.

1. **The evidence source for validation is the ledger that does not exist.**
   `PROV-HEARTBEAT-30M-3X` declares `EVIDENCE_EXPECTED: DOWN declarations vs actual session
   deaths, **from the event ledger**`. That practice therefore **cannot reach its expiry decision
   by the route it declared**, and E.3 forbids leaving it provisional forever. M-1 turns a
   correctly-formed learning object into one that cannot be resolved.

2. **`ACTIVE_LESSONS` is unmaterialized.** `CLAUDE.md` says so in its own routing table:
   *"Active lessons for your role, once operative | `active_lessons/` — **not yet
   materialized**"*. So E.5's terminal step — the subset that reaches an actor at rehydration —
   has no destination. Learning is being *written* (20 SLRs) and is not being *delivered*.

3. **The learning records are ref-partitioned exactly as the approval queue is.** The 11
   `SLR-ORCH-*` live only on `orchestrator`; the 9 `SLR-plan-*` on `main`. E.2's dedup and
   confirmation-counting requires seeing both sets at once, and `EVIDENCE_COUNT` and
   `CONFIRMATION_CLASSES` are meaningless computed over a partition. **A `REPLICATION` cannot be
   recognized across a ref boundary** — the second observer's record is on a branch the first
   cannot read, so it registers as another `ORIGINAL_OBSERVATION`, and the ≥2 threshold is never
   reached by two actors who genuinely agree.

### 8.3 · What a completed cycle would deposit

Stated as flow over objects that already exist, not as a format:

```
cycle completes → TASK_COMPLETE + CLOSES_EVENT_ID (J.1)   ← the ledger that does not exist
                → SLR per E.6, persisted by WORK_COMMIT   ← works today
                → LEARNING_INDEX entry or confirmation    ← needs a single reconciled surface (8.2.3)
                → Mirror clustering → ACTIVE LESSONS      ← needs active_lessons/ to exist
                → role subset at rehydration              ← closes the loop into the next cycle
```

The loop closes at rehydration, and A.6 is what makes that safe: a checkpoint whose
`APPLICABLE_GOVERNANCE_FINGERPRINT` no longer matches **does not resume** — it asks. This is the
one place where LEARN feeds back into DISCOVER, and it is also the mechanism that stops a
learning-driven governance change from silently invalidating in-flight work.

---

## 9 · The critical question

> *"What is the minimum additional infrastructure needed to eliminate manual prompt copying while
> preserving the 5 % human decision layer?"*

### 9.1 · Four things the measurements remove from the answer

Before naming what is needed, four candidates are eliminated — each because it already exists,
not because it is unimportant:

| Not needed | Why |
|---|---|
| A message transport | `SendMessage` exists, carries an unbounded payload, fails loudly and legibly (§ 6.2) |
| A handoff format | A.1's 15 fields + B.1's 8 already cover five of the six requested items (§ 6.1) |
| A learning lifecycle | Annex E is complete and exercised — 20 SLRs (§ 8.1) |
| A governance change | Every mechanism below is **specified in frozen governance and unbuilt**. This is construction, not legislation. |

The fourth is the most consequential for scoping: **nothing in this answer requires amending an
annex.** J.1 fully specifies the event ledger; J.3 fully specifies the approval queue; A.1–A.7
fully specify the contract and its checkpoints.

### 9.2 · The three objects that are genuinely missing

**① An actor→incarnation binding — the `ROUTABLE` property.**

The only one of the three that is not merely unbuilt but *undesigned*: the harness probe found
"no mechanism at all" for it, and § 6.3 re-measures why none can be improvised — name is
per-session, worktree narrows 36→10 not →1, a resolving name can be a dead job, and
`--resume --bg` forks silently at exit 0.

This is **the** blocker on the literal wording of the question. Manual prompt copying is a human
performing this lookup visually. It is also the item with a measured precedent to build on rather
than invent: `launch/legend_launch.sh` already reserves a per-`(actor_id, runtime_instance)`
lineage record with `O_EXCL` **before** the spawn — a real compare-and-swap on one file in one
local cell. Two conflicts inside that kernel are recorded and unrepaired (its version gate reads
the wrong binary; it refuses anything that is not `kind: background`, and all 36 live sessions
are `interactive`), so it is a foundation with known defects, not a working part.

**② The Annex J.1 event ledger.**

Removes the input of DISCOVER (§ 4) and the signal of MONITOR (§ 7) with one absence. It is fully
specified — 23 event types, `CLOSES_EVENT_ID`, replay, sovereignty of repo state — and blocked on
**one delegated decision that belongs to Plan and to nobody else**: J.1's one-writer design,
option (a) per-actor event files consolidated into a derived view, or (b) events derived from
commits and ACKed messages. Until that is chosen, no correct implementation can begin, and
choosing it is not this record's to do.

**③ A single reconciled surface for pending human decisions.**

Not a new object — the *existing* `HUMAN_APPROVAL_QUEUE`, unforked. M-5 measured 21 distinct
records in the union with no ref carrying more than 13 and `main` carrying 5; M-6 measured the
obvious predicate returning 100 % false positives from two coexisting encodings in one file. J.3
already names the surface this feeds: the `DAILY_BRIEF`'s `PENDING HUMAN DECISIONS` section,
which M-3 found named in seven documents and instantiated nowhere.

### 9.3 · 🔴 The ordering, which is the actual answer

The three are not a shopping list. They have a forced order, and it is not the intuitive one:

```
③  reconcile the human-decision surface   ← FIRST, and it is independent of the other two
①  actor→incarnation binding              ← unblocks dispatch; needs ③ to be safe
②  event ledger (after Plan's J.1 choice) ← unblocks discovery and monitoring at scale
```

**③ comes first, and it is the finding this record would defend hardest.**

The question's framing — *eliminate copying while preserving the human layer* — treats the human
layer as intact and at risk from automation. The measurements say otherwise. Today, with zero
automation, **no actor and no human can enumerate what is waiting on the operator**: the queue is
split three ways with no union anywhere, the predicate that would read it is wrong on every ref,
and the brief that would display it does not exist. The 5 % is not currently protected; it is
merely small enough, and the lab slow enough, that nothing has fallen through yet.

Build ① and ② first and the loop gets faster at routing work past a decision surface nobody can
read. Build ③ first and the layer becomes *observable*, at which point "preserving" it is a
checkable property instead of an assumption.

The cheapest confirmation available: ③ requires no new mechanism at all. It is a reconciliation
of one existing file across three refs, plus a derived read that resolves `STATE: PENDING`
against the `RESOLVES_APPROVAL_ID` set — the derived-view construction J.1 already assigns to
Plan. It touches no annex and invents no schema.

### 9.4 · What remains manual afterwards, by design

Even with all three built, these do not become machine decisions, and a loop that absorbed them
would be defective rather than autonomous:

- the five J.3 approval types, and overall strategy (H.1);
- any external spend — `DEFAULT_EXTERNAL_SPEND = 0` makes this fail-closed by default (J.4);
- reopening an actor declared `DOWN` — the compensating protocol for the absent failure-detector
  is explicitly *"riapertura operatore"* (J.0);
- promotion of `BOOTSTRAP_CONTROLLER → Orchestrator`, *"mai autoassunzione"* (H.1, Annex I);
- **the activation act the contracts still need.** `DEC-20260822` consequence 3: *"A new,
  explicit activation act is required […] This record does not perform it, does not schedule it,
  and does not specify its form."*

The last one is why § 1's vacancy is **not** the binding constraint. An activated Orchestrator
with a valid lease, today, would still be unable to run this loop: it would face the same absent
ledger, the same unresolvable addresses, and the same forked queue. **Activation and
infrastructure are independent blockers, and neither one waits on the other.** They can be
pursued in parallel by different parties — which is the only scheduling claim this record makes.

---

## 10 · What this record does not do

Explicitly not done, not authorized, and not implied:

- it defines **no schema, record format, key set or file layout** — every field named is cited
  from A.1, B.1, A.6, J.1 or J.3, which already define it;
- it **builds nothing** and edits no file outside `learning/`;
- it **activates nothing**: no lease acquired, no role contract read as binding, no actor
  addressed, no message sent;
- it **modifies no governance** and reinterprets no frozen annex;
- it does **not** make Plan's J.1 one-writer choice, and does not narrow it to (a) or (b);
- it does **not** adjudicate MAJOR-1, MAJOR-2 or MAJOR-3 of `REV-ROLES-MIRROR-001`, nor supply
  the author response that review still requires;
- it does **not** repair the forked `HUMAN_APPROVAL_QUEUE`, the `legend_launch.sh` version gate,
  or the contested `orchestrator` worktree field — each is measured here and left as measured;
- it assigns **no ownership** of any gap it names, and schedules no work;
- it does **not** synthesize, ratify or contradict the six sibling analyses of § 2.2; where it
  converges with one, the measurement was taken independently in this session.

---

## Verification trail

Every row executed in this session, 2026-08-22, against `main` @ `788c357` and all local refs.

| Check | Command | Result |
|---|---|---|
| Lease state | `python3 framework/scripts/lease_state.py` | `ACTIVE by derivation: 0`; 5 leases, all STALE/RELEASED |
| Live sessions | `claude agents --json` | 36 rows, all `kind: interactive` |
| Sessions per worktree | same, grouped by `cwd` | root 16 · evidence-index 10 · mirror 9 · lettore-c 1 · orchestrator 0 · lettore 0 · lettore-b 0 |
| Event ledger, working tree | `find . -iname "*event*"` | no ledger file |
| Event ledger, all refs | `git grep -l "EVENT_ID\|event_ledger\|events.jsonl" <all refs> -- 'ledger/*'` | empty |
| Task ledger | `ls ledger/tasks/` · `find ledger/tasks -name '*.json' \| wc -l` | 1 dir (`plan`), 5 records |
| Checkpoint ledger | `ls ledger/checkpoints/plan \| wc -l` | 19 records, `plan` only |
| `DAILY_BRIEF` | `grep -ril "DAILY_BRIEF"` | 7 files, all normative/candidate text; no artifact |
| Approval queue per ref | `git show <ref>:ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` | main 5 · orchestrator 13 · evidence-index 13 · p51c9-rebased 13 · 22 other refs 5 |
| Approval queue union | union of `APPROVAL_ID\|RESOLUTION_ID\|CORRECTION_ID` over all refs | **21 distinct**; no ref carries it |
| Naive pending predicate | `STATE == "PENDING"`, then resolved against `RESOLVES_APPROVAL_ID` | main 2→0 · orchestrator 2→0 · evidence-index 6→0. **All false positives.** |
| Two encodings | raw dump of `orchestrator:…HUMAN_APPROVAL_QUEUE.jsonl` | lines 2–5 paired APR+RES; lines 7–10 fused `APPROVAL_ID`+`RESOLUTION_ID` |
| No v1 of this record | `git grep -l -i "AUTONOMOUS.LAB.LOOP" <all refs>` | empty |
| Sibling analyses | `git ls-tree -r <ref> -- learning/orchestrator` over all refs | 6 analyses on 6 branches; `main` carries 1 |
| Role contract status | `governance/decisions/DEC-20260822-…` | `ACTIVATION_NOT_CONFIRMED`; four contracts `PROPOSED` |
| H.1 row count | `governance/annex_h_authority_matrix.md` § H.1 | 17 rows; operator holds 2 |
| Retry / ACK / heartbeat defaults | `governance/plan_defined_parameters.md` P1, P3, P4 | `PARK` · 30 min · 30/90 min, both PROVISIONAL |

**Recorded by:** a session with no ACTOR_ID, no lease and no role contract, in worktree
`wt-lab-loop-v2` on branch `orch-autonomous-lab-loop-v2`, based on `main` @ `788c357`.
**This is not a `WORK_COMMIT` under a role contract and not a `CANONICAL_BATCH_COMMIT`.**
It touches one new path under `learning/orchestrator/` and nothing else.

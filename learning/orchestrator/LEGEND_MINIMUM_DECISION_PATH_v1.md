---
record_type: OPERATIONAL_DECISION_PATH
record_id: LEGEND-MINIMUM-DECISION-PATH-V1
task_id: LEGEND_MINIMUM_DECISION_PATH_v1
title: The minimum decision path from protocol design to operational execution
revision: 1
author: unregistered session — no role contract, no ACTOR_ID
actor_id: NOT ESTABLISHED — a session cannot resolve its own actorhood
dispatcher: operator
date: 2026-08-24
status: PREPARATION ONLY — PROPOSED, NOT APPROVED
binding: NO
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none
creates_no_dec: true
chooses_no_outcome: true
governance_version: 3.1.1 — read and cited, neither exercised nor modified
activation_state_governing_this_record: >
  DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE returns OPTION B ACTIVATION_NOT_CONFIRMED.
  No authority in this record is traced to any role contract, including the one whose seat
  name appears in the dispatch that produced it.
inputs:
  - the DECISION PREPARATION that identified five decision surfaces D1…D5. It is a chat product
    and is not in the repository — verified by content search before this file existed (§10).
    Its five surfaces are restated here from the dispatch, not from a stored artifact.
  - learning/orchestrator/LEGEND_OPERATIONAL_READINESS_PLAN_FINAL_v1.md — 24 decisions, D-1…D-24
  - governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md
  - reviews/mirror/ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001.md @ refs/heads/mirror
measured_at: >
  branch legend-operating-convention-v1 @ 30cb4f3fd700e2aaf6b608e363438f883ddc3760,
  working tree as found, 2026-08-24T14:03Z–14:20Z. Every figure below was executed in this
  session; nothing is carried from a report except where marked AS REPORTED.
domain: CONTENT. learning/ is not among the CONTROL_PLANE_ROOTS of P5.1
class: WORKING RECORD
self_note: >
  Writing this file makes the untracked planning corpus 12 files, measured at 11 immediately
  before it. It is therefore inside the hazard that D-1 of the readiness plan governs, and it
  proposes no commit of itself.
---

# THE MINIMUM DECISION PATH — protocol design → operational execution

> **This record decides nothing, creates no `DEC`, proposes no code, no schema, no normative
> file, no architecture and no repository change.** It has no recommendation column, by
> construction: the readiness plan carried one and this record deliberately does not, because
> the dispatch that produced it withholds outcome selection from its author.

---

## 0 · The four categories, and how to read a line in this record

Every statement below is tagged. The tags are the epistemic separation LEGEND already runs on,
applied to a governance question instead of a scientific one.

| Tag | Means | Who may produce it |
|---|---|---|
| `OBS` | measured this session, with the command that reproduces it | any session, no authority |
| `INF` | derived from `OBS` by reasoning; can be wrong; carries a falsifier | any session, no authority |
| `DEC` | a choice among available outcomes | **operator** for everything in §6 |
| `IMP` | an act that changes the repository or the runtime | only after the `DEC` that gates it |

**The rule that keeps them apart:** an `INF` may narrow the option set only by showing an option
is unreachable, never by showing it is unattractive. Where this record calls something
*blocking*, it means **no defined default state exists that lets execution proceed** — not that
proceeding would be unwise.

---

## 1 · The shortest true answer

`INF` **One decision is unavoidable. One more decides whether two others fire at all. The last
has a defined default and no edge to any of them.**

```
UNAVOIDABLE      OPS-DEC-01   who may write durable state on behalf of the laboratory
THE SWITCH       OPS-DEC-02   is the first run governed, or a declared rehearsal
FIRES ONLY IF    OPS-DEC-03   what counts as an independent reviewer      ← only if 02 = governed
FIRES ONLY IF    OPS-DEC-04   XPORT status                                ← only if 02 = governed
                                                                            AND the run routes
                                                                            payload cross-session
PARALLEL         OPS-DEC-05   event ledger status                         ← default exists, no edge
```

`INF` The minimum viable governance decision set is **{ OPS-DEC-01, OPS-DEC-02 }**. Both are
already prefigured in `LEGEND_OPERATIONAL_READINESS_PLAN_FINAL_v1.md` as `D-6` and `D-5`. This
record adds no new decision surface; it identifies which existing ones are the cut vertices.

---

## 2 · The five surfaces, measured

The dispatch names five surfaces `D1…D5`. Below is what each one **is**, at the tree named in
the frontmatter. Nothing here is a decision.

### 2.1 · Surface D1 — activation boundary

`OBS` The four role contracts read `status: PROPOSED — binding once Mirror hostile review passes
and the operator approves`, byte-identical on `main` and on `HEAD`
(`git grep -n "^status:" main -- roles/` → 4 hits; same on `HEAD`).

`OBS` `DEC-20260822` returned **OPTION B — `ACTIVATION_NOT_CONFIRMED`**, and its consequence 3
states that a new explicit activation act is required, *"does not perform it, does not schedule
it, and does not specify its form."*

`OBS` Its consequence 4 records a measured obstacle inside the activation clause itself: the only
hostile review of the four objects, `REV-ROLES-MIRROR-001`, returned `CHANGES_REQUIRED` on three
and **no verdict on `roles/mirror.md`**, under the self-review prohibition.

`OBS` The population is larger than `roles/`. **12 tracked files on `main` carry
`status: PROPOSED` in their own frontmatter, out of 580 tracked files.** Four further hits are
quotations inside three other files, classified mechanically by comparing the hit line to the
end of each file's frontmatter block, not by eye. The 12 include `BOOTSTRAP.md`,
`deployment/deployment_profile.md` and `governance/plan_defined_parameters.md` — the file where
`P5` (the candidate content hash) and `P7` (the event ledger) live.

`OBS` `PROPOSAL-C9-STATE-MODEL.md` § 8 recorded *"Seven `status: PROPOSED` on governed
artifacts"* on 2026-08-17. **12 ≠ 7 and this record does not reconcile them** — the two
populations may be differently defined ("governed artifacts" is not "files with the string"),
and reconciling them is a measurement nobody has run. It is listed as `PREP-2` in §3.

### 2.2 · Surface D2 — ACTOR_ID conferral

`OBS` `python3 framework/scripts/lease_state.py` → **`ACTIVE by derivation: 0`**. Five leases,
all `STALE` or `RELEASED`, the most recent released 2026-08-18T14:05:20Z.

`OBS` The Agent Card registry exists on exactly **one ref of 57**: `refs/heads/orchestrator`,
at `runtime/agent_card_registry.md`. It is not on `main`. Positive control for the sweep:
`ledger/approvals` resolves on 34 of the same 57 refs.

`OBS` That registry declares `status: PARTIALLY REGISTERED — 3 of 6`, and in its own frontmatter:
*"authority: none — this file records verified state. It assigns nothing and confers nothing."*
Its `orchestrator` card reads `STATUS: BOOTSTRAP_CONTROLLER # NOT ACTIVE_ORCHESTRATOR — no lease
exists`, and **every capability of every card is `UNVERIFIED`, `last_verified: NONE`** — L2 has
never run.

`OBS` `PROPOSAL-C9-STATE-MODEL.md` frontmatter: `hold: no implementation and no governance
modification until that review completes; **L2 suspended**; the status/C-8 batch frozen pending
a later operator decision`.

`INF` The conferral question is not "which name goes in a field". `WORK_COMMIT` is granted by
`H.1` to *"ogni attore"*; the registry confers nothing; the lease is the only durable act that
promotes a session, and `I.2` places it after registration and after the L2 smoke, which a
standing hold suspends. **Falsifier:** if the operator holds that `ACTOR_ID` is conferred by
operator designation alone, independent of `I.2` steps 7–9, this chain does not bind and D2
collapses to a one-line designation.

### 2.3 · Surface D3 — XPORT operational status

`OBS` `framework/protocols/cross_session_transport.md` is **present on `main`** (and on `HEAD`
and `xport`; absent on `mirror`, `evidence-index`, `orchestrator`, `lettore`). Its status line
reads `PROPOSED — binding once Mirror hostile review passes and the operator approves`.

`OBS` `REV-XPORT-MIRROR-002` (`refs/heads/mirror`) carries `verdict: ACCEPT` on revision 2, with
four non-blocking findings, *"none about semantics"*.

`OBS` `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` has 6 lines and **0 occurrences of `XPORT`**
(control: `GOV311` → 5 occurrences). The candidate manifest states
`human_approval: NOT REQUESTED — no APPROVAL_ID is prefilled here, and none exists`.

`OBS` The same shape holds twice more. `framework/protocols/scientist_reading_modes.md` and
`framework/protocols/controlled_benchmark_ab.md` are on `main`, both `PROPOSED — binding on
canonical execution of CAND-20260818-SCIENTIST-AB-SPEC`; that candidate is at revision 6,
`state: READY FOR MIRROR REVIEW … no approval requested, granted or implied`, and
`REV-SCIAB-MIRROR-006` returned `verdict: ACCEPT`. The queue contains **0 occurrences of
`SCIAB` or `SCIENTIST-AB`**.

`INF` Three reviewed protocols sit one operator act from binding, and **the act was never
requested for any of them**. *Counter-evidence, stated because it defeats the obvious
explanation:* the absence is **not** caused by a missing requester — `APR-20260816-GOV311-001`
carries `"REQUESTED_BY":"plan"`, so a non-Orchestrator has raised an approval before. The
candidate manifests say the request was deliberately withheld.

### 2.4 · Surface D4 — J.1 / P7 event ledger

`OBS` `P7` decides design **(a)**: per-actor append-only `ledger/events/<ACTOR_ID>.jsonl` in each
actor's own worktree, consolidated into `ledger/consolidated/`. Its closing line:
*"Tracked as a debt; not yet built."*

`OBS` Re-derived across **all 57 refs**: `ledger/events` resolves to **0 entries on 0 refs**.
Positive control: `ledger/approvals` resolves on 34 of the 57. `ledger/` on disk holds
`approvals`, `checkpoints`, `retirements`, `tasks` — and no `events`, no `consolidated`.
*(A Mirror record measured the same negative on 2026-08-22 against 37 refs; the denominator has
since moved to 57, which is why it was re-derived rather than carried.)*

`OBS` `J.0` names the event ledger as half of the compensating protocol for an absent guarantee:
*"RBAC enforced a runtime → authority matrix testuale + audit + **event ledger** (H.1, J.1)"*,
and forbids any document from describing these mechanisms in stronger vocabulary than the
compensator beside them.

`OBS` `G.3` places `MIRROR_RETROSPECTIVE` *"primarily on the consolidated event ledger (J.1)"*,
and its cadence `N` is `UNASSIGNED` — `P7`'s closing section records that neither Plan nor Mirror
may set it, and `RES-20260816-GOV311-001` carries it as `ESC-3 … CARRIED_UNRESOLVED`.

### 2.5 · Surface D5 — reviewer independence

`AS REPORTED`, from `reviews/mirror/ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001.md`, read at source
on `refs/heads/mirror` this session; its own figures were measured at `main@788c357` and are not
re-derived here:

- the review graph is one repeated edge — `plan` authors 25 of 30, `mirror` reviews **39 of 39**,
  operator adjudicates ~29 of 36. `C.3`'s `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR` is satisfied in every
  instance *"and buys no independence, because independence comes from the possibility of a
  different reviewer"*;
- 1 of 6 ladder rungs has ever been climbed; 0 challenges, 0 dissents;
- `CP-3` — Mirror is structurally unreviewable, on three independent grounds, each sufficient
  alone: the self-review prohibition; `G.2`'s independent reviewer is *chosen by Orchestrator*
  and there is no Orchestrator; and there is no second reviewer to choose;
- `CP-5` — a `REQUEST CHANGES` from the sole reviewer, on a candidate whose `D.2` manifest
  requires `MIRROR_REVIEW` before `HUMAN_APPROVAL`, **is operationally a block**.

`OBS` Re-derived here: `C.3` states *"Apertura review solo via Orchestrator"*; `G.2` states
*"reviewer indipendente scelto da Orchestrator"*; `lease_state.py` reports 0 ACTIVE.

`INF` D5's default — *reviewed by the Mirror seat* — is not merely narrow, it is **currently
unreachable for any new review**, because the party that opens it and chooses the reviewer does
not exist. A default that cannot be executed is not a default.

---

## 3 · Three lanes — who may do what, before any decision

The dispatch asks for this separation explicitly. The discriminating question for each item is
*"does this act change the repository, the runtime, or anyone's authority?"*

### LANE-O · operator only — §6

`OBS` `H.1` assigns to the operator: *spese / MAJOR approval / **governance*** and *strategia
complessiva*. Body §10.2 gives three modes — OBSERVE/ASK, STEER, OPERATOR_OVERRIDE. Every item
in §6 is a governance or strategy determination and sits in that row.

### LANE-P · preparation by agents, no authority required, no decision anticipated

Each is a measurement or a reading. None writes to a governed path; none needs a `DEC`. Listed
so the operator can say which are worth the attention they cost — **each one also produces
another untracked record, which is the hazard `D-1` governs.**

| # | Preparation | Feeds | Why it needs no authority |
|---|---|---|---|
| `PREP-1` | Enumerate the untracked corpus at the instant Φ−1a opens | `D-1` | a listing |
| `PREP-2` | Reconcile the `PROPOSED` population: 12 measured today vs C-9 § 8's seven, per object | `OPS-DEC-02` | a classification of existing bytes |
| `PREP-3` | Assemble the XPORT approval bundle as a **reading**: object hash, base head, review IDs and verdicts, author response, and the recorded absence of an `APPROVAL_ID` | `OPS-DEC-04` | reading; the queue append is `IMP` |
| `PREP-4` | Re-derive the independence census at the current head — 39/39 was measured at `788c357` against 37 refs; there are 57 today | `OPS-DEC-03` | a census |
| `PREP-5` | Enumerate, clause by clause, which parts of the trial design require a **governed** artifact and which do not | `OPS-DEC-02` | a reading of design v2, not a change to it |
| `PREP-6` | Verify `I.2` step 3's observable items — repo identity, root state, governance version, concurrent root writer, worktrees | `OPS-DEC-01` | observation only; step 4's *creation* is `IMP` |
| `PREP-7` | Measure what an event-ledger writer would reuse — `P7` names `fulltext_receipts.py`'s hash chain and tail anchor | `OPS-DEC-05` | reading a script, not writing one |

### LANE-I · implementation — each blocked until the named decision exists

| # | Act | Gated by | Note |
|---|---|---|---|
| `IMP-1` | `WORK_COMMIT` of the untracked corpus | `OPS-DEC-01` | `H.1`: actor, own branch |
| `IMP-2` | Any change to a `status:` line | `OPS-DEC-02` / `-04` | C-9 § 5.1 puts this transition's owner at the operator, Plan transcribing |
| `IMP-3` | Any append to `HUMAN_APPROVAL_QUEUE` | the decision it records | body §4: a durable queue object, never only a message |
| `IMP-4` | Lease acquisition + `ORCHESTRATOR_REGISTRATION` | `OPS-DEC-01` | `I.3`: reacquisition on STALE/RELEASED with **registered succession** |
| `IMP-5` | L2 capability smoke | `OPS-DEC-01` | also suspended by the C-9 hold |
| `IMP-6` | Building `ledger/events/` + the consolidated view | `OPS-DEC-05` | `P7` design (a) already decided *what*; not *whether now* |
| `IMP-7` | `reviews/trial-001/` and the audit schema | readiness `D-4`, `D-12` | trial-level, outside this record |
| `IMP-8` | `git worktree prune`, exec bits, action pins | readiness `D-23`, `D-24` | mechanical, still repository changes |

---

## 4 · Dependency map

```
                      ┌──────────────────────────────────────────────┐
                      │  OPS-DEC-01 · authority route                │  UNAVOIDABLE
                      │  who may write durable state                 │
                      └───────┬──────────────────────┬───────────────┘
                              │                      │
              branch: registered actors        branch: operator executes
                              │                      │
                              ▼                      ▼
                   AUTOMATIC: I.2 steps 7–9    AUTOMATIC: no lease exists
                   → L2 must run               → C.3 has no opener
                   → the C-9 "L2 suspended"    → G.2 has no chooser
                     hold must be scoped       → OPS-DEC-03 must be answered
                     or lifted                   by the operator directly

                      ┌──────────────────────────────────────────────┐
                      │  OPS-DEC-02 · run class                      │  THE SWITCH
                      │  governed run, or declared rehearsal         │
                      └───────┬──────────────────────┬───────────────┘
                              │                      │
                    branch: GOVERNED           branch: REHEARSAL
                              │                      │
                              ▼                      ▼
              D1 fires  → the activation act    D1 stands down → contracts stay
                          must say what          PROPOSED, authority traced to the
                          discharges the         annexes (DEC-20260822, consequence 2)
                          unreachable
                          mirror.md branch      D3 stands down → OPS-DEC-04 stays
              D3 fires  → OPS-DEC-04 becomes     parallel; dispatch discipline is
                          blocking IF the run    declared, not binding
                          routes authoritative
                          payload between        D5 stands down → no governed review
                          sessions; and the      is opened, and the outcome record
                          reading-mode / A/B     must say so
                          protocols bind only
                          on canonical execution
                          of CAND-20260818
              D5 fires  → OPS-DEC-03 becomes
                          blocking at floor R2

  DECIDABLE AT ANY TIME, in either branch, or explicitly deferred:
      OPS-DEC-04 (XPORT)   ─── no edge to 01, 03, 05. Edge to 02 only as above
      OPS-DEC-05 (ledger)  ─── no edge to 01, 02, 03, 04
                                 └─ residue: even if built, G.3's cadence N stays UNASSIGNED
                                    (ESC-3), so the retrospective still cannot be scheduled
```

| Relation | Pairs |
|---|---|
| **Blocking** | `OPS-DEC-01` → every durable artifact of the run (`IMP-1`, `IMP-4`, `IMP-5`) |
| **Conditionally blocking** | `OPS-DEC-03` → the run's review floor, **only** on `02 = GOVERNED` |
| **Conditionally blocking** | `OPS-DEC-04` → the run, **only** on `02 = GOVERNED` *and* the run routing authoritative payload between sessions |
| **Parallel** | `OPS-DEC-04` ∥ `OPS-DEC-05`, and neither has an edge to `01` or `03`. `OPS-DEC-05` has none to `02` either |
| **Automatic consequence** | `01 = registered actors` ⇒ the C-9 L2 hold must be scoped or lifted |
| **Automatic consequence** | `01 = operator executes` ⇒ `C.3`/`G.2` lose their opener and chooser |
| **Automatic consequence** | `02 = GOVERNED` ⇒ `CAND-20260818-SCIENTIST-AB-SPEC` becomes a precondition |
| **Automatic consequence** | `02 = REHEARSAL` ⇒ the outcome record must state that no governed artifact exists |
| **Automatic consequence** | `04 = approve` ⇒ `J.3` requires a queue object bound to the exact hash + base |

---

## 5 · Why the minimum set is two, and not five

`INF` A decision is on the minimum path **iff no defined default state lets operational execution
proceed with durable output**. Applied to the five surfaces:

| Surface | Default state | Does execution proceed under it? | On the path? |
|---|---|---|---|
| D2 · actor | none — no session in this cycle can `WORK_COMMIT` | ❌ nothing durable is written | ✅ **yes** |
| D1 · activation | explicit — contracts stay `PROPOSED`, authority from the annexes | ✅ but only for a run that cites no contract | ⚠️ via `02` |
| D3 · XPORT | undeclared — binds nobody | ✅ unless the run treats a dispatch as evidence | ⚠️ via `02` |
| D5 · independence | *unreachable* — no opener, no chooser | ❌ if any governed review is declared | ⚠️ via `02` |
| D4 · ledger | explicit — absent, and known to be | ✅ the run produces no event either way | ❌ no |

`INF` Three of the five (`D1`, `D3`, `D5`) resolve **by declaration** rather than by construction,
and the same declaration resolves all three: whether this run produces governed artifacts. That
single fork is `OPS-DEC-02`. It is not a new surface — it is readiness-plan `D-5` seen as the
switch it already is.

> **Falsifier for this whole section.** If the operator wants an artifact the rehearsal branch
> cannot produce — a canonical claim, a governed review verdict, a candidate that reaches
> `HUMAN_APPROVAL` — then `02 = REHEARSAL` is unavailable and the reduction fails: `D1`, `D3`
> and `D5` collapse back into three separate decisions and the minimum set becomes four.
> **`PREP-5` is the measurement that settles it, and it has not been run.**

---

## 6 · The decisions

> Namespace warning, because this repository has already been bitten by it once. `OPS-DEC-nn`
> is a **new namespace**. It is not the dispatch's `D1…D5` (surfaces) and not the readiness
> plan's `D-1…D-24`. The mapping column is load-bearing; nothing is renamed silently.

### `OPS-DEC-01` — the authority route for the first operational run

```
SURFACE            D2 · ACTOR_ID conferral        MAPS TO   readiness D-6
CLASS              MINIMUM VIABLE SET · unavoidable
```

**QUESTION** — By what route does the laboratory acquire a party entitled to write durable state
on its behalf, for the first operational run?

**WHY OPERATOR** — `H.1` gives *governance* and *strategia complessiva* to the operator. `I.2`
step 10 makes promotion a durable operator-visible act and body §0.2/§8 forbid self-assumption;
`DEC-20260822` consequence 2 forbids reading the authority out of a role contract. There is no
party inside the system that can answer this without granting itself the answer.

**EVIDENCE REQUIRED** — `lease_state.py` output (0 ACTIVE, 5 stale/released) · the Agent Card
registry's registration table and its `authority: none` clause · `I.2` steps 7–10 and `I.3`'s
succession rule · the C-9 hold's `L2 suspended` clause · `H.1`'s `WORK_COMMIT` row.

**POSSIBLE OUTCOMES** *(enumerated, not ranked)*
- **(a)** re-enter `I.2` steps 7–9 and promote a session to `ACTIVE_ORCHESTRATOR` with a
  registered succession;
- **(b)** the operator personally performs the acts that require an actor, and no conferral
  occurs;
- **(c)** a scoped, one-act conferral naming the session, the act and its expiry;
- **(d)** defer — the corpus stays untracked and the run produces nothing durable.

**DOWNSTREAM CONSEQUENCES**
- (a) ⇒ L2 must run ⇒ the C-9 `L2 suspended` hold must be scoped or lifted; and `C.3`/`G.2`
  regain an opener and a chooser, which is most of `OPS-DEC-03`;
- (b) ⇒ no lease exists ⇒ `C.3`'s *"apertura review solo via Orchestrator"* and `G.2`'s
  *"reviewer scelto da Orchestrator"* have no subject, and `OPS-DEC-03` must be answered directly;
- (c) ⇒ the act's scope must name its expiry, or it is (a) without the registration;
- (d) ⇒ `IMP-1` and `IMP-4` stay blocked; `Φ−1a` (the byte copy) is unaffected — it needs no authority.

**EXPLICIT NON-DECISIONS** — this does not decide *who* the actor is by name; does not activate
any role contract (`OPS-DEC-02`); does not verify any capability; does not authorize a
`CANONICAL_BATCH_COMMIT`, whose `GATE 0` is a separate condition; does not resolve `C-7`, the
unattributed session the registry recorded on 2026-08-17.

---

### `OPS-DEC-02` — the class of the first operational run

```
SURFACE            D1 · activation boundary       MAPS TO   readiness D-5
CLASS              MINIMUM VIABLE SET · the switch: it settles D1, and its outcome decides
                   whether D3 and D5 fire at all
```

**QUESTION** — Does the first operational run produce **governed artifacts** — artifacts that
cite a normative status, enter the review ladder, or reach `HUMAN_APPROVAL` — or is it a
**declared rehearsal** whose outputs claim no governed status?

**WHY OPERATOR** — Both branches turn on the meaning of the clause *"binding once Mirror hostile
review passes and the operator approves"*, present in the frontmatter of 12 files on `main`.
`DEC-20260822` § RATIONALE 6 records why an actor may not settle it: *"an actor choosing the
reading that makes its own contract binding would be exactly the convenient interpretation the
gate exists to prevent."*

**EVIDENCE REQUIRED** — the 12-file `PROPOSED` population with each file's own status text
(`PREP-2`) · `DEC-20260822` consequences 1–4 · `REV-ROLES-MIRROR-001`'s three `CHANGES_REQUIRED`
and the missing fourth verdict · `PREP-5`, the clause-level reading of which parts of the trial
design need a governed artifact — **not yet run**.

**POSSIBLE OUTCOMES** *(enumerated, not ranked)*
- **(a)** GOVERNED — the run's artifacts claim governed status, and the surfaces they depend on
  must be settled first, per object;
- **(b)** REHEARSAL — the run claims none, and the outcome record states what it therefore is
  not;
- **(c)** MIXED, by named artifact class;
- **(d)** defer — the run does not open.

**DOWNSTREAM CONSEQUENCES**
- (a) ⇒ D1 fires: an activation act must state what discharges the `roles/mirror.md` branch that
  no internal review can reach (three independent barriers, `CP-3`); D3 fires: the reading-mode
  and A/B protocols bind only *"on canonical execution of `CAND-20260818-SCIENTIST-AB-SPEC`"*,
  which has no approval; D5 fires at the declared floor;
- (b) ⇒ all three stand down, and each stand-down is a sentence the outcome record must carry —
  `DEC-20260822` consequence 2 already requires every exercised authority to be traced to the
  body or a named annex, never to a contract;
- (c) ⇒ the classes must be named at the outset, not sorted afterwards.

**EXPLICIT NON-DECISIONS** — does not activate or refuse to activate any contract; does not
amend the status grammar; does not adopt `PROPOSAL-C9-STATE-MODEL`'s four-field form or lift its
hold; does not decide the trial's scientific content, paper, or question; renders no verdict on
`MAJOR-1`, `MAJOR-2`, `MAJOR-3`, which `DEC-20260822` left open.

---

### `OPS-DEC-03` — what counts as an independent reviewer for this run

```
SURFACE            D5 · reviewer independence     MAPS TO   readiness D-14 (floor R2)
CLASS              CONDITIONAL — fires only on OPS-DEC-02 = GOVERNED (or MIXED)
```

**QUESTION** — For this run's reviews, what constitutes independence: the registered Mirror seat,
an unregistered session under a declared information barrier, or both with the governed verdict
reserved?

**WHY OPERATOR** — `G.2` forbids Mirror from changing its own review methodology alone; `H.1`
routes *"modifica rubrica/metodi di Mirror"* to *"mai Mirror da solo"* and governance to the
operator. `CP-1` measures the Orchestrator↔Mirror loop as closed in both directions with
*"the only exit is the operator"*, and records that no recusal clause exists anywhere in the body
or annexes.

**EVIDENCE REQUIRED** — `PREP-4`, the independence census re-derived at the current head · `CP-3`'s
three barriers · `CP-5`'s gate/assessment substitution · the repository's own working
information-barrier precedent (finding `I-2` **of the Mirror analysis**, not of this record's
`IMP-` list: the DisMech blinded review, ten
artifacts, executed, iterated, **outside the ladder and unknown to the governance**).

**POSSIBLE OUTCOMES** *(enumerated, not ranked)*
- **(a)** the registered Mirror seat only — the status quo;
- **(b)** an unregistered session under a declared information barrier, output labelled
  non-governed;
- **(c)** both, with the governed verdict reserved to the seat;
- **(d)** no review is declared for this run — available only under `02 = REHEARSAL`.

**DOWNSTREAM CONSEQUENCES**
- (a) requires an opener and a chooser, which exist only under `01 = (a)` or by the operator
  acting directly;
- (b) creates a review class the ladder does not name — `C.1`'s six rungs do not include it, and
  the precedent that works sits outside them;
- (c) makes explicit the thing `CP-5` measures: the seat holds both the assessment and the gate.

**EXPLICIT NON-DECISIONS** — does not modify `C.1`'s ladder, `C.2`'s format or `C.3`'s
discipline; does not set the `MIRROR_RETROSPECTIVE` cadence `N` (`ESC-3`, still unresolved);
does not adjudicate any open finding; does not name a reviewer.

---

### `OPS-DEC-04` — the status of XPORT for the operational phase

```
SURFACE            D3 · XPORT operational status  MAPS TO   —
CLASS              CONDITIONAL — a defined default exists; gates the run only on
                   OPS-DEC-02 = GOVERNED and the run routing payload cross-session.
                   Decidable at any time regardless.
```

**QUESTION** — Is `framework/protocols/cross_session_transport.md` binding discipline for the
operational phase, explicitly non-binding guidance, or binding scoped to this run?

**WHY OPERATOR** — `MIRROR_REVIEW` is satisfied (`REV-XPORT-MIRROR-002`, `ACCEPT`); the only
unsatisfied half of its own status clause is *"and the operator approves"*. `G.1` classes a
normative protocol binding every actor as `MIRROR_REQUIRED`/MAJOR, and `J.3` sends a MAJOR to the
operator as adjudicator — the review names exactly that and records *"none granted, none
implied"*.

**EVIDENCE REQUIRED** — `PREP-3`, the approval bundle as a reading: `CANDIDATE_CONTENT_HASH`
`81f241f2…6e1f` at `BASE_HEAD 4454feab`, reproducible by the governed script; `REV-XPORT-MIRROR-001`
(`REQUEST CHANGES`, M-1) → `REV-XPORT-MIRROR-002` (`ACCEPT`); `AUTHOR-RESPONSE-XPORT-MIRROR-001`;
and the measured absence of any `APPROVAL_ID`.

**POSSIBLE OUTCOMES** *(enumerated, not ranked)*
- **(a)** approve → binding for every actor;
- **(b)** declare explicitly non-binding for now;
- **(c)** binding scoped to this run only;
- **(d)** defer, with the consequence stated.

**DOWNSTREAM CONSEQUENCES**
- (a) ⇒ `J.3` requires a durable queue object citing the exact hash and base; the protocol's own
  `enforcement_mode: PROCEDURAL` means **no mechanism enforces it between turns** — the discipline
  is carried by actors, not by code;
- (b)/(d) ⇒ multi-session dispatch in the run proceeds under undeclared discipline, and any
  payload that rides in a message body remains, in the protocol's own § 1 (`main`, line 72),
  *"a payload whose completeness the recipient cannot establish"*;
- any outcome ⇒ the same question stands open, unasked, for `scientist_reading_modes.md` and
  `controlled_benchmark_ab.md`, which share the shape and are gated on a different candidate.

**EXPLICIT NON-DECISIONS** — does not reopen the transport rules or the routing question the
candidate explicitly did **not** fix (`§9` of the protocol: *which live session is `plan` right
now* remains unanswered); does not decide `CAND-20260818-SCIENTIST-AB-SPEC`; does not execute any
candidate.

---

### `OPS-DEC-05` — the status of the J.1 / P7 event ledger

```
SURFACE            D4 · event ledger              MAPS TO   —
CLASS              PARALLEL — a defined default exists; gates nothing in the first run
```

**QUESTION** — Does the operational phase open with the event ledger built, or with its absence
explicitly declared and its consequences recorded?

**WHY OPERATOR** — `P7` already decided the *design* — that delegation is discharged. What is
open is *whether to spend now*, which is a strategy call under `H.1`, and whether the laboratory
may run while a compensating protocol named in `J.0` has zero instances — a governance question
about the guarantee table itself.

**EVIDENCE REQUIRED** — the 0-of-57-refs measurement with its positive control · `P7`'s design
(a) and its `not yet built` line · `J.0`'s RBAC row · `G.3`'s retrospective clause · `CP-2`'s
three requirements, of which **(c) a population of challenges is zero and cannot be supplied by
tooling** · `PREP-7`, the reuse measurement.

**POSSIBLE OUTCOMES** *(enumerated, not ranked)*
- **(a)** build before the run opens;
- **(b)** declare absent, record the consequence in the run's outcome;
- **(c)** minimal recording for this run only;
- **(d)** defer.

**DOWNSTREAM CONSEQUENCES**
- (a) ⇒ an implementation gated by this decision (`IMP-6`), and `J.0`'s prohibition then binds the
  vocabulary any document may use about it;
- (b) ⇒ `G.3`'s retrospective has no input for this run, and `F.3`'s compensator for the closed
  Orchestrator/Mirror loop stays unexercisable — **which it also would be with the ledger built**,
  because the challenge population is zero;
- **any** outcome ⇒ cadence `N` stays `UNASSIGNED`; `ESC-3` is a separate carried item and this
  decision does not close it.

**EXPLICIT NON-DECISIONS** — does not revisit `P7`'s (a)-vs-(b) design choice; does not specify a
schema, a path, a writer or a validator; does not set `N`; does not decide whether the first run
generates events worth consolidating.

---

## 7 · What is *not* on the minimum path, though it looks like it

`INF`, each with the observation that demotes it:

| Looks blocking | Why it is not |
|---|---|
| The 12 `PROPOSED` files | `DEC-20260822` consequence 2 already defines the state they are in: authority traced to the body or a named annex. Undecided ≠ undefined |
| The absent event ledger | it records events; the first run's evidence is the reading and its locators, not the ledger |
| `git worktree prune`, exec bits, action pins | readiness `D-23`/`D-24`, mechanical, and the readiness plan's own rule bars an infrastructure item from blocking the experiment unless it is named blocking with a reason |
| Preserving the untracked corpus | **`Φ−1a` needs no decision at all** — it is a byte copy outside the repository, requiring no git act and no actorhood. Only `Φ−1c`, the commit, needs `OPS-DEC-01` |
| The unreached `roles/mirror.md` review | it blocks *activation*, and activation is only reached through `OPS-DEC-02 = GOVERNED` |

---

## 8 · Where this record could be wrong

1. **The reduction rests on an unmeasured input.** `PREP-5` — which clauses of the trial design need
   a governed artifact — has not been run. If it comes back "several", `OPS-DEC-02`'s rehearsal
   branch closes and the minimum set becomes four.
2. **The `12 ≠ 7` discrepancy is unreconciled.** If C-9's seven is the operative population,
   `OPS-DEC-02`'s object list is smaller than stated here.
3. **D5's figures are `AS REPORTED`.** 39/39, 25/30, ~29/36 were measured at `main@788c357`
   against 37 refs by the record cited; there are 57 refs today and this session did not
   re-derive them. `PREP-4` is the check.
4. **The reframing itself is an act of framing.** The five surfaces map one-to-one onto the five
   decisions; what is reduced is not their *number* but their *blocking count* — one unavoidable,
   one switch, two conditional, one parallel. That reduction is `INF`, and calling `OPS-DEC-02` a
   switch rather than a surface is the framing to attack. If the operator prefers the five as
   given, the `SURFACE`/`MAPS TO` lines in §6 are the way back, and nothing is lost by refusing
   the reduction.

---

## 9 · What this record does not do

It creates no `DEC` and appends nothing to any queue. It chooses no outcome and carries no
recommendation column. It proposes no code, no schema, no normative file, no architecture and no
repository change. It activates nothing, confers nothing, opens no review, assigns no owner and
resolves no finding — including the 35 dispositioned by the readiness plan and the three
`MAJOR`s `DEC-20260822` left open. It commits nothing, itself included: **it is the 12th
untracked file in a corpus of 11 measured minutes before it existed, and it is therefore on the
ungated surface it is describing.**

It is also deliberately short. The planning corpus stands at roughly 6 000 lines about an
experiment not yet performed; a fifth long document about the same experiment would be the
defect the readiness plan named, committed one more time.

---

## 10 · Verification trail

| Check | Command | Result |
|---|---|---|
| Lease state | `python3 framework/scripts/lease_state.py` | `ACTIVE by derivation: 0`; 5 leases STALE/RELEASED |
| Role status lines | `git grep -n "^status:" main -- roles/` · same on `HEAD` | 4 × `PROPOSED …`, both refs |
| `PROPOSED` population | `git grep -n "^status: PROPOSED" main`, each hit line compared to that file's frontmatter end | 16 hits · **12 in frontmatter** · 4 quotations in 3 files |
| Tracked denominator | `git ls-tree -r --name-only main \| wc -l` | 580 |
| Event ledger, all refs | per-ref `git ls-tree -r --name-only <ref> -- ledger/events` over `git for-each-ref` | **0 entries, 0 of 57 refs** |
| — positive control | same sweep, `ledger/approvals` | present on **34 of 57** |
| Agent Card registry | same sweep, path match `agent.card` | 1 ref: `refs/heads/orchestrator` |
| XPORT on refs | `git cat-file -e <ref>:framework/protocols/cross_session_transport.md` | PRESENT `main`, `HEAD`, `xport` · ABSENT `mirror`, `evidence-index`, `orchestrator`, `lettore` · control: annex J present on `main` |
| XPORT review verdict | `git show mirror:reviews/mirror/REV-XPORT-MIRROR-002.md` | `verdict: ACCEPT`, 4 non-blocking findings |
| Approval queue | `grep -c` on `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` | `XPORT` → **0** · `SCIAB\|SCIENTIST-AB` → **0** · control `GOV311` → 5 · 6 lines total |
| SCIAB state | `CAND-20260818-SCIENTIST-AB-SPEC` frontmatter · `REV-SCIAB-MIRROR-006` | `READY FOR MIRROR REVIEW (revision 6)`, no approval · `verdict: ACCEPT` |
| C-9 hold | `PROPOSAL-C9-STATE-MODEL.md` frontmatter | `L2 suspended`, batch frozen |
| Untracked corpus | `git status --porcelain \| grep '^??' \| wc -l` | **11**, measured before this file existed |
| Refs | `git for-each-ref \| wc -l` | 57 |
| "DECISION PREPARATION" not in the repository | `grep -rl "DECISION PREPARATION" . --include="*.md"` | no match — **run before this file existed; reproduce with `--exclude=LEGEND_MINIMUM_DECISION_PATH_v1.md`, since this file now contains the string** |

---

# NEXT OPERATOR ACTION

Five, and no more. The first requires no decision from anyone; the last four are yours.

1. **Copy the untracked planning records out of the repository, byte for byte** — now 12 files
   including this one. No git act, no actorhood, seconds. It discharges the destructibility
   hazard and blocks nothing. *(This is `Φ−1a` of the readiness plan, unchanged; it is repeated
   here because it is still the only act on any list that costs nothing and is still not done.)*

2. **Answer `OPS-DEC-01`** — the authority route: registered actors, you personally, a scoped
   one-act conferral, or defer. Until this exists, nothing durable is written and item 1 is the
   only preservation the corpus has.

3. **Answer `OPS-DEC-02`** — governed run or declared rehearsal. This is the switch: it decides
   whether the activation boundary, XPORT and reviewer independence are live questions for the
   first run or stood-down ones.

4. **Say which `LANE-P` preparations may run** — `PREP-5` is the one that can falsify §5's
   reduction, and `PREP-2`, `PREP-3`, `PREP-4` are the evidence bundles for `OPS-DEC-02`, `-04` and `-03`.
   Each needs no authority and each costs another untracked record.

5. **Declare `OPS-DEC-04` and `OPS-DEC-05`, or defer them explicitly** — one line each. Both have
   defined defaults; `OPS-DEC-05` gates nothing at all, and `OPS-DEC-04` gates the run only if
   item 3 comes back GOVERNED *and* the run routes authoritative payload between sessions. An
   explicit deferral is a complete answer, and it stops both being re-litigated at every phase
   boundary.

---
artifact: PROPOSAL — ORCHESTRATOR STATE RECONSTRUCTION before dispatch
proposal_id: ORCH-STATE-RECONSTRUCTION
task_id: ORCHESTRATOR_STATE_RECONSTRUCTION_SPECIFICATION_V1
author: orchestrator
authored_on: 2026-08-22
dispatcher: operator
mode: READ_ONLY_ANALYSIS → CREATE_SPECIFICATION_ARTIFACT_ONLY
status: PROPOSED — a description of a possible state machine, offered for review
normative: no
authority: none — this file assigns nothing, activates nothing, approves nothing, and resolves
  no finding. It describes a shape. Adoption of any clause would be a separate governed change.
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1), so this
  file changes no candidate content hash and no role fingerprint
branch: orch-state-reconstruction
base_head: 2bb270050d76264a13c8d595bc585ccde3b09ff3
lease_state_at_authoring: "ACTIVE by derivation: 0 — written under no lease and needing none;
  a WORK_COMMIT on its own branch is available to every actor under H.1"
adjacent_and_held:
  - PROPOSAL-C9-STATE-MODEL (ACCEPTED, acceptance_is_not_adoption, held) — classifies how a
    recorded VALUE is represented. This file asks a different question: what must be READ before
    a dispatch. Neither adopts the other, and this file adopts none of C-9's four-field form.
  - DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE (BINDING determination of state) — the four role
    contracts are PROPOSED. This file treats them as non-binding throughout, per its consequence 2.
---

# ORCHESTRATOR STATE RECONSTRUCTION — a candidate state machine

> 🔴 **This is not policy, and it is not a mechanism.** It describes a shape that the observed
> failures suggest, in the form of *questions a dispatcher would have to answer*. It defines no
> rule, confers no authority, creates no record type, and builds nothing. Where it names a check,
> the check does not exist. Where it names a field, no writer for that field is proposed.

---

## 0 · Surface map — the measurement this document was written from

Every negative claim below is scoped by this surface and by nothing wider.

```
BRANCH SURVEYED     main  (root checkout, <REPO_ROOT>)
HEAD                2bb270050d76264a13c8d595bc585ccde3b09ff3
WORKING TREE        clean — git status --porcelain returned empty
REFS SURVEYED       46 total at survey time, via git for-each-ref:
                      32 refs/heads · 4 refs/remotes · 1 refs/stash
                      5 refs/tags (1 handoff · 4 snapshot) · 4 refs/codex/turn-diffs
WORKTREES           14 at survey time, via git worktree list
SURFACE DELTA       this session then added 1 branch (orch-state-reconstruction) and
                      1 worktree, so the same commands now return 47 and 15. The survey
                      figures above are the ones every claim below was measured against.
CLAIM SCOPE         Existence claims marked REPOSITORY-WIDE were tested by iterating
                    refs/heads + refs/tags with git ls-tree / git cat-file -e.
                    Claims marked LOCAL were tested at HEAD only and are labelled as such.
```

🔴 **`NOT_FOUND` in one checkout is not `NOT_EXIST`, and this document was itself caught making
that error while being written.** A first pass asked whether `transition` was a defined term using
`git grep -E '\btransition'`, which returned zero files. The zero was an artifact of the query —
`\b` is not a POSIX ERE word boundary and git grep does not honour it — not a fact about the
repository. Re-measured without it, 25 files match. **The finding survived only because the count
was re-derived rather than believed.** It is recorded here rather than silently corrected, because
§ 1.4 is about exactly this class of error and an example from this session is better evidence
than an example from someone else's.

---

## 0.1 · Dispatch validation — vocabulary, verified against the repository

Each concept named in the dispatch was tested for repository definition before being reasoned
with. **Repository-defined** means a normative file defines or governs the term; **repository-used**
means it appears and carries stable meaning but no normative definition was located on the
surveyed surface.

| Concept | Verdict | Where it is defined, or the measurement |
|---|---|---|
| `Orchestrator` | **defined** | Body § 35.2, H.1 — 5 of its 17 rows name Orchestrator in the authority column, and a 6th (`Promozione BOOTSTRAP_CONTROLLER`) names the role as a target; `roles/orchestrator.md` (PROPOSED); I.3 lease holder |
| `handoff` | **defined, thinly** | Annex B.2 message-type list — `… TASK_COMPLETE · TASK_CANCEL · HANDOFF`. The *message type* is named; **no schema, no required fields and no state effect are specified for it anywhere on the surveyed surface.** **14 distinct paths repository-wide** carry a handoff name — 11 actor-to-actor, 3 release-process — and each invents its own shape |
| `actor` | **defined** | `ACTOR_ID`, `ACTOR_CLASS`, Annex I.4 Agent Card, J.2 actor state machine |
| `transition` | 🔴 **external vocabulary as a bare noun** | English "transition" is **not** a defined term in `GOVERNANCE_v3.1.1.md`, any `annex_*.md`, or any `roles/*.md` (REPOSITORY-WIDE at HEAD, re-measured per § 0). The Italian **`transizione` is defined**, twice, and identically: A.5 — *"Ogni transizione è stato durevole + evento (Annex J)"*; J.2 — *"Ogni transizione = evento (J.1) + roster durevole."* **Treated as external throughout, and bound to that definition wherever used** |
| `state` | **defined** | A.5 task states; J.2 actor and `LAB_STATE`; `framework/state/state_manifest_current.md` |
| `authority` | **defined** | H.1 authority matrix, `[MAJOR]`, frozen |
| `lease` | **defined** | Annex I.3; record at `runtime/orchestrator_lease.md`; derivation `framework/scripts/lease_state.py` |
| `routing` | **defined, unresolved in fact** | Body § 35.2 AUTHORITY & ROUTING; `CAND-20260819-XPORT` § ROUTING is **SPLIT, NOT OPENED and BLOCKED** |
| `capability` | **defined** | I.4 capability records; `CONFIGURED != PROVEN`; assignment rests on `VERIFIED` (body § 8) |
| `GATE` | **defined** | GATE 0–5, `LEGEND_CORE.md` and Annex D |
| `H.1 authority matrix` | **defined** | `governance/annex_h_authority_matrix.md` § H.1, FROZEN, `[MAJOR]` |

**Consequence for this document.** `TRANSITION_CHECK` and `ORCHESTRATOR_STATE_RECONSTRUCTION` are
**new names for things the repository does not name.** They are used here as labels for a proposed
shape, never as though they already bound anyone. Nothing in this file may be cited as evidence
that either term is governed.

---

## 1 · Current observed failure mode

Four failures, each measured, not recalled.

### 1.1 · Required objects exist on different refs, and `main` carries none of them

The seven objects a dispatcher would most need in order to decide who does the next thing were
tested REPOSITORY-WIDE. **Every one of them is absent from `main`.**

| Object | On `main`? | Refs that carry it |
|---|---|---|
| `runtime/agent_card_registry.md` — the actor/capability registry | ❌ | `orchestrator` only |
| `reviews/mirror/REV-ROLES-MIRROR-001.md` — first hostile review of the 4 contracts | ❌ | `mirror` only |
| `reviews/mirror/HANDOFF-CANDIDATE-READINESS-001.md` | ❌ | `mirror` only |
| `governance/decisions/DEC-20260820-ORCH-SESSION-HOME.md` | ❌ | `orchestrator-surface`, `plan-orchsurf-r4-transcription` |
| `governance/decisions/DEC-20260821-ORCHSURF-D2-TRANSCRIPTION-ROUTING.md` | ❌ | same two |
| `governance/candidates/HANDOFF-ORCHSURF-MIRROR.md` | ❌ | same two |
| `learning/plan/HANDOFF-20260822-ROLE-CONTRACT-REPAIR.md` | ❌ | `plan-orchsurf-r4-transcription` only |

🔴 **The registry that records which actors exist, what they may do, and whether any capability is
verified is reachable from exactly one branch, and that branch is not the one the root checkout is
on.** `git merge-base --is-ancestor refs/heads/orchestrator refs/heads/main` returns non-zero: the
registry has never been merged. A dispatcher standing in the root and reading `runtime/` sees
`orchestrator_lease.md` and nothing else, and would conclude — correctly for its checkout, falsely
for the repository — that no agent card registry exists.

This is not a merge backlog to be cleared. It is the structural observation that **an object's path
does not identify it; only `(ref, path)` does**, and that no dispatch record in this repository
currently carries a ref.

### 1.2 · Actor authority is unclear, and the unclarity is now a binding determination

`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` (on `main`, dated today) decides `OPTION B —
ACTIVATION_NOT_CONFIRMED`. Its consequence 2:

> **No actor authority may be assumed from these contracts.** Any authority an actor exercises must
> be traced to the governance body or to a named annex — H.1 for the authority matrix, D for the
> commit path, C for the review ladder, I.3 for the lease — never to a role contract clause
> standing alone.

So the four documents that describe what each actor does are non-binding, and the only binding
authority surface is H.1 plus the annexes. H.1 has 17 rows and allocates by **decision type**
(`Task / priorità / riassegnazione`, `Conclusione scientifica`, `Integrazione strutturale`, …).
It does not allocate by **task**, and it names no procedure for establishing that a given actor is
presently able to receive one.

The same decision records that `REV-ROLES-MIRROR-001` returned **CHANGES_REQUIRED on three
contracts, no verdict on the fourth** (self-review prohibition on `roles/mirror.md`), and that its
`AUTHOR_RESPONSE` is *"required and outstanding"* as of today. A dispatcher that wanted to assign
the repair of those findings would need to know who owns them; the decision explicitly declines to
assign ownership (`OUT_OF_SCOPE`: *"assigning ownership of any finding, repair or follow-up"*).

### 1.3 · The next step could not be safely assigned — three independent blocks, all measured

```
python3 framework/scripts/lease_state.py --check     →  ACTIVE by derivation: 0
```

Five lease records, all `STALE` or `RELEASED`, most recent released `2026-08-18T14:05:20Z`. Two
findings stand on record #3: a `DISAGREEMENT` (stored `EXPIRED`, a value **I.3's vocabulary does
not define** — it declares `ACTIVE | STALE | RELEASED`), and `EXPIRED_WITHOUT_RENEWAL`.

**Capability.** Every capability row in `runtime/agent_card_registry.md`, across all six cards and
all four roles, reads `status: UNVERIFIED, last_verified: NONE`. The registry states its own
consequence:

> Until then the laboratory is **not running**, and no assignment may be made on any capability in
> this file.

Two capabilities are `blocked`, not merely unverified: Mirror's *"Event ledger analysis"* (no
writer exists) and — per the registry's own note — Plan's fingerprint composition had its blocker
discharged without the capability becoming verified.

**Identity.** Two of three Scientist `ACTOR_ID`s are `UNRESOLVED` by governed decision (PID-12);
`lettore` and `lettore-b` are `NOT_REGISTERED` with `DIRTY_WORK: yes`. `CURRENT_SESSION_REF` for
the registered actors is `DERIVED_BY_COMPLEMENT — pending L1 confirmation`, resting on a stated,
attackable assumption (*"`ListAgents` returns all peers and omits only self"*). And conflict **C-7**
records a session — `legend-public-12 [cf79f1]` — seen by all four actors and the self of none.

🔴 **A dispatcher facing these three facts cannot name a recipient it can prove exists, prove is
able, or prove is idle.** None of the three is a defect in any actor; all three are absences of a
readable state.

### 1.4 · Negative claims lacked a measurement surface

Three instances, of three different kinds:

- **The tool that names its own narrowness.** `EXPIRED_WITHOUT_RENEWAL` is, in `orchestrator_lease.md`'s
  own words, *"named for the property it can test, not for the one that motivated it"* — three of
  five records were unrenewed **and demonstrably used**. A check whose name overstates its reach
  produces a negative that a reader will over-read.
- **The PASS that verified motion, not content.** `REV-GOV311-MIRROR-003` is a delta verification
  legitimate *"only if nothing in the content moved"*. `COR-20260816-GOV311-001` exists because that
  distinction was once collapsed.
- **This session's own regex** (§ 0), where a malformed query produced a clean zero.

The common shape: **a negative was produced without declaring the surface it was measured on**, so
a reader could not tell the difference between *absent*, *not looked for*, and *looked for wrongly*.

---

## 2 · State inputs — what a dispatcher would have to read

Offered as an evaluation of the four groups the dispatch names. **Every row is a question about
where a value would come from, not a specification of a field.** The right-hand column is the
measured status of that source *today* — several have no source at all, and those rows are the
substance of this section.

### 2.1 · `ARTIFACT_STATE`

| Question | Would be answered from | Status today |
|---|---|---|
| exists? | `git cat-file -e <ref>:<path>` | available; **used inconsistently** — § 1.1 |
| location? | path | 🔴 **insufficient alone.** A path without a ref is not an address (§ 1.1) |
| ref? | branch or tag name | **no existing handoff artifact carries a ref field as a required element** — `HANDOFF-P5DOMAIN-MIRROR` carries `BRANCH` in a prose code block by the author's own care, not by any schema |
| immutable identifier? | blob/commit oid; `CANDIDATE_CONTENT_HASH` | exists for candidates (`candidate_content_hash.py`); **nothing analogous for a handoff** |

A named observation, not a rule: a branch name is **mutable** — it moves when the branch moves —
so a ref alone identifies a location, not a state. `HANDOFF-P5DOMAIN-MIRROR` already distinguishes
`BASE_HEAD`, `CONTENT_TIP` and `MANIFEST_TIP` as three separate oids. Whether a dispatch record
needs all three, or one, is § 6 Q-2.

### 2.2 · `ACTOR_STATE`

| Question | Would be answered from | Status today |
|---|---|---|
| identity? | `ACTOR_ID` (I.4) | 2 of 6 `UNRESOLVED` by governed decision; 1 session claimed by nobody (C-7) |
| role? | role contract | 🔴 **all four PROPOSED** — `DEC-20260822`; role may not be read from them |
| capability? | I.4 capability rows | 🔴 **every row `UNVERIFIED`**; two `blocked` |
| readiness? | J.2 (`ACTIVE ⇄ IDLE \| RUNNING`) + heartbeat | 🔴 **`LAST_SEEN` is actor-declared, never observed.** `HEARTBEAT_CADENCE` (P4) is PROVISIONAL and unexercised; **no heartbeat mechanism has ever run** |
| reachable? | `CURRENT_SESSION_REF` / `ROUTING_TRANSPORT` | `DERIVED_BY_COMPLEMENT`, pending L1; XPORT records `ROUTING_TRANSPORT` as a uds socket that **dies with the process** |

🔴 **Three of these five have no observing writer.** They are declared by the actor being described.
An actor asserting its own readiness is the same shape H.1 forbids in `Promozione
BOOTSTRAP_CONTROLLER → Orchestrator` (*"mai autoassunzione"*), applied to a smaller claim.

### 2.3 · `AUTHORITY_STATE`

| Question | Would be answered from | Status today |
|---|---|---|
| who may assign? | H.1 row 1 — `Task / priorità / riassegnazione / generation` → Orchestrator | **defined**; conditioned on I.3 for the commit rows only |
| who may review? | Annex C.3 — *"Apertura solo via Orchestrator"*; C.1 ladder + floor | **defined**; floor is per-task and not derivable from the actor alone |
| who may approve? | H.1 — `Spese / MAJOR approval / governance` → Operatore; J.3 queue | **defined** |
| who may integrate? | H.1 — `Integrazione strutturale / candidate` → Plan; `INTEGRATION_BLOCK` | **defined** |
| may this actor act on this object? | 🔴 **nothing** | H.1 allocates by decision type. **No object on the surveyed surface maps an actor + an artifact to a permission**, and J.0 records that RBAC is a guarantee LEGEND does not possess — compensated by *"authority matrix testuale + audit + event ledger"*, of which the third does not exist (§ 2.4) |

### 2.4 · `DEPENDENCY_STATE`

| Question | Would be answered from | Status today |
|---|---|---|
| pending decisions? | `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl`; `governance/decisions/` | queue exists (6 lines). 🔴 `governance/decisions/` **on `main` contains exactly one record**; two others are on `evidence-index`-lineage refs only (§ 1.1) |
| pending reviews? | `reviews/` | exists; the review that matters most today (`REV-ROLES-MIRROR-001`) is on `mirror` only, with `AUTHOR_RESPONSE` outstanding |
| missing prerequisites? | I.2 steps 6–10 | steps 7–8 incomplete: registration partial, **L2 never run** |
| what closed what? | J.1 event ledger, `CLOSES_EVENT_ID` | 🔴 **`ledger/events/` does not exist on any ref** (REPOSITORY-WIDE: iterated all `refs/heads` + `refs/tags`; zero hits). `ledger/` contains `approvals/`, `checkpoints/`, `retirements/`, `tasks/` — and no `events/` |

🔴 **This is the load-bearing absence of the whole document.** J.2 defines a transition as *"evento
(J.1) + roster durevole"*. J.1's ledger has a chosen design and no writer. So **every transition
this repository has ever performed has been performed without the event half of its own definition**,
and a reconstruction has no event stream to replay — it would have to derive from durable git state,
which J.1 itself declares sovereign (*"in conflitto vince il repo"*). That is a viable direction and
a strictly weaker one: git state shows what an object *is*, never what an actor *intended* or *closed*.

---

## 3 · Transition check — questions only

**No answers are proposed here, and no ordering between the checks is proposed.** Whether these are
gates, advisories, or a report is § 6 Q-1 — and the choice matters, because a check that blocks is a
rule and this file may not make one.

```
TARGET_EXISTS
    Is the object addressed as (ref, path), not path alone?
    Does the ref resolve in the checkout the dispatcher is standing in?
    Is an immutable identifier recorded, or only a mutable branch name?
    If the object is expected NOT to exist, on what surface was that measured — and is
      the surface declared in the record, or only in the dispatcher's memory?

OWNER_EXISTS
    Is there an ACTOR_ID that is RESOLVED, not proposed?
    Is its readiness observed, or self-declared?
    Is it reachable by a route that survived the last process restart?
    Is any session in the roster claimed by nobody? (C-7 is open today)

AUTHORITY_EXISTS
    Which H.1 row covers this decision type?
    Is the authority traced to the body or a named annex — never to a PROPOSED
      role contract (DEC-20260822, consequence 2)?
    Does the action require an ACTIVE lease, or is it a WORK_COMMIT that does not?
    Is the actor about to decide something H.1 gives to somebody else?

DEPENDENCIES_RESOLVED
    Is any prerequisite object on a ref other than the dispatcher's?
    Is any prior finding outstanding against this object?
    Is any AUTHOR_RESPONSE required and unwritten? (Annex C.2: silence is not acceptance)
    Are prerequisites known to be resolved, or merely not known to be unresolved?

REVIEW_REQUIREMENTS_MET
    What is the Ladder floor for this task, and who set it?
    Is AUTHOR ≠ REVIEWER ≠ ADJUDICATOR satisfiable from the resolved actors?
    Does any actor here face a self-review prohibition on this object?
      (roles/mirror.md received no verdict for exactly this reason)

OPERATOR_DECISION_REQUIRED
    Does this touch spend, MAJOR, destructive, governance or strategy (H.1 → Operatore)?
    Is the MAJOR classification itself in doubt — which H.1 gives to Mirror, fail-closed?
    Is the dispatcher about to resolve an ambiguity in its own favour?
```

🔴 **The last question is the one this file exists to raise.** Every other check can be got wrong and
detected later. That one cannot, because the actor best placed to notice is the actor that benefits.
Mirror's refusal in `REV-ROLES-MIRROR-001` § 8 is the repository's existing precedent, and it is a
refusal, not a mechanism: *"an actor choosing the reading that makes its own contract binding would
be exactly the convenient interpretation the gate exists to prevent."*

---

## 4 · Blocked state — what a block would have to return

A description of the information a block would carry **if** blocks were adopted. No obligation is
created here, and nothing is specified about where such a record would live.

| Field | What it would carry | Why the observed failures suggest it |
|---|---|---|
| `BLOCK_REASON` | which check did not pass, by name | *"blocked"* alone is unactionable; the checks in § 3 are the closed set a reason would draw from |
| `EVIDENCE` | the command run and its **output**, not its conclusion | § 1.4: a negative without its surface is unreadable. `DEC-20260822`'s VERIFICATION TRAIL is the existing shape — command, result, per row |
| `MEASUREMENT_SURFACE` | refs surveyed, count, and whether local or repository-wide | 🔴 **suggested addition to the dispatch's field list.** Without it `MISSING_OBJECT` cannot be distinguished from *not looked for*. § 1.1 is a table of objects that are missing **locally** and present **repository-wide**, and the two need different next actions |
| `MISSING_OBJECT` | `(ref, path)` — or the declaration that no ref carries it | § 2.1. Recording `runtime/agent_card_registry.md` as *missing* would have been false; *missing from `main`, present on `orchestrator`* is true and points at the fix |
| `REQUIRED_DECISION_OWNER` | the H.1 row, and the actor it names | § 1.2 — H.1 is the only binding authority surface while the contracts are PROPOSED |
| `NEXT_ALLOWED_ACTION` | what may be done **without** resolving the block | so a block parks one path rather than the laboratory. J.3's existing rule is the precedent: *"il resto del laboratorio continua"*, the affected task goes to `AWAITING_APPROVAL` with a checkpoint |

**A block would be a state, not a failure.** A.5 already has vocabulary for a task that stops without
dying — `BLOCKED`, `AWAITING_APPROVAL`, `PARKED`, each resuming idempotently via A.6–A.7. Whether a
dispatch block maps onto A.5's `BLOCKED` or is a distinct thing that never became a task at all is
**§ 6 Q-3**, and it is not answered here.

---

## 5 · Loop compatibility

The dispatch names `Orchestrator → Plan → Mirror → Scientist`. The question is whether reconstruction
before dispatch can support that **without** making Orchestrator a scientific reviewer, a governance
authority, or the owner of another actor's work. Each is examined against H.1.

### 5.1 · The separation each check must preserve

| Risk | The H.1 row that forbids it | How a reconstruction stays on the right side |
|---|---|---|
| Orchestrator becomes **scientific reviewer** | `Conclusione scientifica` → Scientist responsabile, *"soggetta a review, mai a ordine"*; `Epistemic / method review` → Mirror | Reconstruction asks **whether a review exists and is closed**, never **whether its verdict is right**. `REVIEW_REQUIREMENTS_MET` reads the ladder and the disposition; it does not read the finding |
| Orchestrator becomes **governance authority** | `Spese / MAJOR approval / governance` → Operatore; `Classificazione MAJOR dubbia` → Mirror, fail-closed | `OPERATOR_DECISION_REQUIRED` **routes**, and routing to the operator is the opposite of deciding. A doubtful MAJOR is Mirror's, and doubt is the trigger, not the conclusion |
| Orchestrator becomes **owner of others' work** | `Integrazione strutturale / candidate` → Plan; `WORK_COMMIT` → *"ogni attore, solo proprio branch"* | Reconstruction reads other actors' branches and **writes to none**. `roles/orchestrator.md` (PROPOSED, cited as description only) states the same limit: *"must not touch another actor's worktree"* |

### 5.2 · What the loop looks like under these constraints

```
Orchestrator   reads state, asks the § 3 questions, dispatches or blocks
                  ↓  produces:  a task contract (A.1) + an address
Plan           integrates, builds the candidate, may return INTEGRATION_BLOCK
                  ↓  produces:  a candidate + manifest + hash at a base head
Mirror         reviews epistemically; PASS / REVISION_REQUESTED / CHANGES_REQUIRED
                  ↓  produces:  a review record, and an AUTHOR_RESPONSE obligation
Scientist      reads, concludes; the conclusion is the Scientist's own
                  ↓  produces:  a work manifest with verbatim locators
```

🔴 **The arrow that does not exist is the one back into the Orchestrator.** Each actor's output lands
on **its own branch**, because H.1 confines `WORK_COMMIT` there. So every return edge in that loop is
a **cross-ref read**, and § 1.1 is what a cross-ref read looks like when nothing records the ref.
**The loop is not blocked by authority — the authority is cleanly allocated by H.1 and none of the
three risks above is close to being realised. It is blocked by addressing.**

### 5.3 · What reconstruction cannot fix, and must not appear to

- It cannot make an `UNVERIFIED` capability verified. Only L2 does that (I.4), and L2 has not run.
- It cannot make a `PROPOSED` contract binding. `DEC-20260822` consequence 3 requires *"a new,
  explicit activation act"*, and explicitly does not perform, schedule or specify one.
- It cannot observe an actor. Without a heartbeat writer, readiness stays self-declared.
- It cannot replay history. Without `ledger/events/`, there is no event stream (§ 2.4).

**A reconstruction that ran today would return `BLOCKED` on nearly every dispatch**, and that is the
correct output, not a defect in the design. J.0's rule applies to this document as to any other: no
artifact may describe a mechanism *"con vocabolario più forte del protocollo compensativo"*. The
compensating protocol here is a reader following pointers by hand.

---

## 6 · Open questions — listed, not answered

None of these is resolved here. Several are governance questions this file has no authority over.

- **Q-1 · Is a `TRANSITION_CHECK` a gate, an advisory, or a report?** A gate that blocks dispatch is
  a normative rule and would need the governed path. An advisory that anyone may override is not a
  compensator for the RBAC J.0 says the system lacks. *Owner: operator (H.1 → governance).*
- **Q-2 · What identifies a dispatched object — ref, tip oid, content hash, or all three?** § 2.1.
  Candidates already have `CANDIDATE_CONTENT_HASH`; handoffs have nothing. *Owner: Plan (H.1 →
  integrazione strutturale), subject to review.*
- **Q-3 · Does a dispatch block map onto A.5 `BLOCKED`, or is it a pre-task state?** A.5's states
  presuppose an assigned task; a dispatch that never happened has no `TASK_ID` to carry a state. § 4.
- **Q-4 · Who writes actor readiness?** Today the actor writes its own. Whether that is acceptable,
  or whether readiness must be observed, is unresolved — and `HEARTBEAT_CADENCE` (P4) is PROVISIONAL
  and has never been exercised. *Adjacent to C-9 § 5 ownership-of-writer, which is held.*
- **Q-5 · Can reconstruction be specified at all before `ledger/events/` has a writer?** § 2.4. The
  event ledger is `OWED NOT BARRED` per `orchestrator_lease.md`. If reconstruction is built on git
  state alone, it inherits a permanent blind spot for intent and closure.
- **Q-6 · Does Annex B's `HANDOFF` message type need a schema?** B.2 names it and specifies nothing.
  11 actor-to-actor handoff artifacts exist repository-wide (plus 3 release-process ones), each with a shape of its own. *Owner: unclear — B is frozen, so this is a
  governed change.*
- **Q-7 · Does H.1 need a row for "may actor X act on object Y"?** § 2.3 records that no such
  mapping exists. H.1 is `[MAJOR]` and FROZEN; **this file does not propose amending it**, and notes
  only that the gap was measured.
- **Q-8 · What resolves C-7?** A session seen by all four actors and claimed by none has been open
  since 2026-08-16. *Owner: operator, per the registry.*
- **Q-9 · Does reconstruction run per dispatch, per session, or on demand?** Unexamined here. It bears
  on cost, and on whether a stale reconstruction is worse than none.
- **Q-10 · What is the relationship between this file and `PROPOSAL-C9-STATE-MODEL`?** C-9 is ACCEPTED,
  `acceptance_is_not_adoption`, and held. Its § 5.1 already assigns transition owners, and its § 6.1
  `RESOLVER CONTRACT` is a near-neighbour of `TARGET_EXISTS`. **Whether these are one proposal or two
  is not decided here, and this file adopts no clause of C-9.**

---

## 7 · What this file did not do

- It modified no existing artifact. It is one new file under a declared `CONTROL_PLANE_ROOT`.
- It did not touch `roles/`, `framework/`, `ledger/`, `governance/decisions/`, or any annex.
- It advanced no canonical state and did not commit to `main`.
- It activated no contract, assigned no role, created no lease, approved no candidate, resolved no
  H.1 gap, defined no governance rule, and created no `DEC` or `HUMAN_APPROVAL` record.
- It rendered no verdict on MAJOR-1, MAJOR-2 or MAJOR-3, and is not the outstanding
  `AUTHOR_RESPONSE` to `REV-ROLES-MIRROR-001`.
- 🔴 **It did not verify that the shape it describes is the right one.** It has had no review. Under
  its own § 3, a dispatch that cited this file as authority would fail `AUTHORITY_EXISTS`.

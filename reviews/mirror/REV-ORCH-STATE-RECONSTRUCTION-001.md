---
artifact: MIRROR REVIEW — PROPOSAL-ORCH-STATE-RECONSTRUCTION
review_id: REV-ORCH-STATE-RECONSTRUCTION-001
object: governance/candidates/PROPOSAL-ORCH-STATE-RECONSTRUCTION.md
object_ref: orch-state-reconstruction @ f1074aab2ca1f4efaa451e13a78cf52993f310c3
object_blob: e6af7e3d9383f4ae7d5210f81af5610bd15e62e7 — the immutable identifier; the branch name above is mutable and addresses a location, not a state
level: R4 · METHOD (Mirror) — C.1 floor for "processo inferenziale methodology-changing"; C.4 routes SYSTEM → Mirror
reviewer: mirror
author: orchestrator
adjudicator: operator — see § D-3; H.1 gives challenge adjudication to Orchestrator, but Orchestrator is the AUTHOR here, so C.3's AUTHOR ≠ REVIEWER ≠ ADJUDICATOR forces escalation
task_id: MIRROR_C2_REVIEW_ORCHESTRATOR_STATE_RECONSTRUCTION_v1
dispatcher: operator
date: 2026-08-22
mode: READ_ONLY_REVIEW — no implementation, no governance decision, no modification of the object
domain: CONTROL PLANE — `reviews/` is a declared CONTROL_PLANE_ROOT (plan_defined_parameters,
  CONTROL_PLANE_ROOTS), so this file changes no candidate content hash and no role fingerprint
authority: none — this review assigns nothing, adopts nothing, activates nothing, and resolves no
  finding. A verdict is a reviewer's judgement, not a governed change.
---

# REV-ORCH-STATE-RECONSTRUCTION-001

> **What this is.** A single-round R4 method review of one candidate document, conducted under
> Annex C.2. Every factual claim in the object was **re-measured** rather than believed, per the
> dispatch. Where my measurement diverges from the object's, both are shown.

---

## A · IDENTITY — established from repository evidence, not from this dispatch

| Field | Value | How established |
|---|---|---|
| `ACTOR_ID` | `mirror` | worktree path `.claude/worktrees/mirror`; branch `mirror`; `roles/mirror.md` present on this ref |
| role contract | `roles/mirror.md` — **`status: PROPOSED — binding once Mirror hostile review passes and the operator approves`** | `grep -m1 '^status:' roles/mirror.md` |
| worktree | `<REPO_ROOT>/.claude/worktrees/mirror` | `git worktree list` |
| branch | `mirror` | `git rev-parse --abbrev-ref HEAD` |
| HEAD | `13504778b0814f79a912f62f544c23eab6971f9d` | `git rev-parse HEAD` |

🔴 **Authority for this review is not taken from the role contract.** `roles/mirror.md` is
`PROPOSED`, and `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` consequence 2 forbids reading actor
authority from it. The authority is traced instead to:

- **H.1 row `Epistemic / method review` → Mirror**, and
- **Annex G.1 `MIRROR_REQUIRED`** — *"MAJOR; protocolli/governance; R4"*. The object is a
  governance-process candidate, so it falls inside the required perimeter.

That is the same derivation `DEC-20260822` demands of every actor, applied to myself.

**I did not assume Orchestrator authority, and hold none.** No lease was taken; none is needed —
H.1 gives `WORK_COMMIT` to *"ogni attore, solo proprio branch"*.

---

## B · DISPATCH VALIDATION — every named term tested before being reasoned with

Tested at the surface in § C. **Repository-defined** = a normative file defines or governs it.

| Dispatch term | Verdict | Evidence |
|---|---|---|
| `Annex C.2` | **defined** | `governance/annex_c_review_protocol.md` § C.2 *"Formato unico"*, FROZEN. Its required elements and its four verdict values are reproduced verbatim in this review |
| `review ladder` | **defined** | C.1 — `R0 · R1 PEER · R2 INDEPENDENT · R3 TRIADIC · R4 METHOD (Mirror) · R5 CROSS-MODEL`, with a floor table |
| `governance/candidates` | **defined** | exists on this ref; declared exhaustively as a `CONTROL_PLANE_ROOT` in `plan_defined_parameters.md` |
| `H.1 authority matrix` | **defined** | `governance/annex_h_authority_matrix.md` § H.1, `[MAJOR]`. **17 rows — counted, matching the object's claim** |
| `Orchestrator` role | **defined** | H.1 (5 rows name it in the authority column; a 6th names it as a promotion target — **both counts re-verified**); `roles/orchestrator.md` (PROPOSED) |
| `Plan` role | **defined** | H.1 `Integrazione strutturale / candidate` → Plan; `INTEGRATION_BLOCK`; `roles/plan.md` (PROPOSED) |
| `Mirror` role | **defined** | H.1 `Epistemic / method review`, `Classificazione MAJOR dubbia` (fail-closed); Annex G; `roles/mirror.md` (PROPOSED) |
| `ledger` concepts | **defined as design, absent as fact** | J.1 specifies an append-only event ledger with `CLOSES_EVENT_ID`. `ledger/` carries `approvals/`, `checkpoints/`, `retirements/`, `tasks/`. **`ledger/events/` exists on no ref — see F-2** |

### B-1 · External vocabulary — marked, and not reasoned from

🔴 **`transition`, as a bare English noun, is not a defined term.** Re-measured independently of
the object: `git grep -lE 'transition' main -- governance/GOVERNANCE_v3.1.1.md 'governance/annex_*.md' 'roles/*.md'`
returns **no normative file**. The Italian **`transizione` is defined exactly twice, and
identically**:

```
governance/annex_a_task_contract.md:64   "Ogni transizione è stato durevole + evento (Annex J)."
governance/annex_j_runtime_control_plane.md:74   "Ogni transizione = evento (J.1) + roster durevole."
```

Consequently **`TRANSITION_CHECK`, `ORCHESTRATOR_STATE_RECONSTRUCTION`, `ARTIFACT_STATE`,
`ACTOR_STATE`, `AUTHORITY_STATE`, `DEPENDENCY_STATE` and `BLOCKED state` are external vocabulary** —
names for things the repository does not name. **The object declares this itself** (§ 0.1) and uses
them as labels only. I reason from them only as labels, and this review may not be cited as
evidence that any of them is governed.

### B-2 · One dispatch instruction is in tension with C.2, and C.2 wins

The dispatch orders `STEELMAN` at position 6, after the findings. **C.2 requires
`STEELMAN (obbligatorio, prima delle obiezioni)`** — before the objections. C.2 is FROZEN and
normative; a dispatch is not. **The artifact follows C.2** (§ E precedes § F); the final response
follows the dispatch's ordering, which costs nothing since both contain the same text.

### B-3 · The dispatch's own opening is irregular, and I proceeded anyway

**C.3 states `Apertura solo via Orchestrator`.** This review was opened by the **operator**.
Recorded, not treated as disqualifying, for three measured reasons:

1. `lease_state.py --check` returns **`ACTIVE by derivation: 0`** — there is no Orchestrator
   holding a lease to open anything.
2. H.1 gives `Strategia complessiva` and `Spese / MAJOR approval / governance` to the **Operatore**,
   who sits above the row C.3 constrains.
3. The **Orchestrator authored the object**. C.3 also requires `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR`
   for important reviews; had the Orchestrator opened its own review, that constraint would have
   been breached at the opening.

🔴 **This is not a loophole I may widen.** It is recorded so that a later reader does not find an
Orchestrator-less opening in the record and infer that C.3 was silently repealed. **The correct
resolution is the operator's**, and it is § D-3.

---

## C · SURFACE MAP — the measurement every negative claim below is scoped by

```
ACTOR                mirror
BRANCH               mirror
HEAD                 13504778b0814f79a912f62f544c23eab6971f9d
WORKING TREE         clean — git status --porcelain returned empty, before and after writing
                       this file's only sibling change (none)
OBJECT UNDER REVIEW  governance/candidates/PROPOSAL-ORCH-STATE-RECONSTRUCTION.md
                       @ orch-state-reconstruction = f1074aab2ca1f4efaa451e13a78cf52993f310c3
                       introduced by exactly 1 commit, 1 file, 426 insertions, 0 deletions
REFS SURVEYED        47 total — 33 refs/heads · 5 refs/tags · 4 refs/remotes · 1 refs/stash
                       (repository-wide sweeps below iterate heads+tags+remotes = 42)
WORKTREES            15
MEASURED_AT          2026-08-22, this session
VALIDITY             Every absence claim holds for the refs enumerated above and for no wider
                       surface. NOT_FOUND on 42 refs is not NOT_EXIST in a clone I cannot see.
```

### C-1 · The governance surface I judge against is byte-identical to the one the object was written against

The object declares `base_head: 2bb270050d76264a13c8d595bc585ccde3b09ff3`. **`git rev-parse main`
returns exactly that.** And:

```
git diff --stat main..HEAD -- governance/GOVERNANCE_v3.1.1.md governance/annex_*.md roles/
  → roles/scientist.md | 24 +----  (1 file changed)
```

**The body and all ten annexes are identical between `main` and `mirror`.** Only
`roles/scientist.md` differs, and role contracts are `PROPOSED` and non-binding per `DEC-20260822`.
So the normative surface is not in question between author and reviewer.

### C-2 · 🔴 But the *candidate and decision* surface is not identical, and that shaped this review

`git rev-list --left-right --count main...HEAD` → **`64  71`**. My ref is not a superset of `main`;
it is divergent. Objects the object reasons from that are **absent from `mirror` and present on
`main`**, measured by `git cat-file -e`:

| Object needed to review | on `mirror` | on `main` |
|---|---|---|
| `governance/candidates/PROPOSAL-C9-STATE-MODEL.md` | ❌ | ✅ |
| `governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` | ❌ | ✅ |
| `runtime/orchestrator_lease.md` | ❌ | ✅ |
| `framework/scripts/lease_state.py` | ❌ | ✅ |
| `runtime/agent_card_registry.md` | ❌ | ❌ — `orchestrator` only |

**Every governance object this review depends on had to be read cross-ref.** That is the object's
own § 1.1 thesis, encountered by its reviewer, in the act of reviewing it. It is recorded as
evidence in F-1 rather than as a complaint.

### C-3 · A measurement error I made, and corrected before it entered a finding

An early sweep of mine reported `framework/scripts/lease_state.py` and `runtime/orchestrator_lease.md`
as present on **no ref**, which would have supported a much stronger finding — that the state
governing authority lives outside version control entirely. **It was false.** Re-run from a known
working directory with exit codes shown:

```
exit=0    main:runtime/orchestrator_lease.md
exit=0    main:framework/scripts/lease_state.py
exit=128  main:runtime/agent_card_registry.md
exit=128  mirror:runtime/orchestrator_lease.md
```

corroborated independently in the root checkout by `git ls-files -s` and
`git rev-parse HEAD:<path>` returning **matching blobs** (`c34f486`, `d826812`) with
`git status --porcelain` empty. The original zero was an artifact of shell working-directory state
during a parallel invocation, not a fact about the repository.

🔴 **I record this for the same reason the object records its own regex error in § 0: the finding
would have been dramatic, and it was wrong.** A reviewer of a document about undeclared measurement
surfaces is the last actor entitled to a silent correction.

---

## D · SCOPE — what this review does not decide

- **D-1 · Self-review boundary.** Review question 1 asks whether the object *"overlap[s] with Mirror
  epistemic review"*. That is a **Mirror-owned concept**, and G.2 bars Mirror from unilaterally
  changing *"rubrica di review … review-yield methodology"*. Per the dispatch's self-review clause,
  § F-9 is **OBSERVATION ONLY and carries no verdict.** The same bar applies to the object's
  citation of `REV-ROLES-MIRROR-001 § 8`, which is my own prior artifact.
- **D-2 · No implementation is proposed.** Not one line below specifies a writer, a script, a
  schema or a field to be built.
- **D-3 · Adjudication is unassigned and must be the operator's.** H.1 gives
  `Aggiudicazione challenge` to Orchestrator; the Orchestrator is the AUTHOR; C.3 requires
  `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR`. **Adjudication of any disagreement with this review therefore
  escalates to the operator** under H.1 `Spese / MAJOR approval / governance`. I assign nothing.
- **D-4 · `AUTHOR_RESPONSE` is required and outstanding.** C.2: *"il silenzio non è accettazione"*.

---

## E · STEELMAN — required by C.2, and placed before the objections

**The strongest case for this proposal, stated as strongly as I can make it:**

> The laboratory is not blocked by a disputed rule. It is blocked by an **address**. Every actor's
> output lands on its own branch, because H.1 confines `WORK_COMMIT` there — and **that is correct
> governance producing a structural consequence nobody designed for**: every return edge in the
> `Orchestrator → Plan → Mirror → Scientist` loop is a cross-ref read, and **no dispatch record in
> this repository carries a ref.** So the objects a dispatcher must read are each reachable, each
> on exactly one branch, and none of them from where the dispatcher stands. The proposal's central
> claim — *"an object's path does not identify it; only `(ref, path)` does"* — is not a
> preference about metadata. It is a true statement about a content-addressed system being
> addressed by name, and **it is the smallest correct diagnosis of the observed failures.**
>
> Its second strength is **what it refuses to do.** It is the rare candidate that identifies a real
> defect and then declines to fix it, because fixing it would require authority it does not have.
> It writes `normative: no`, `authority: none`, converts every mechanism into a **question**, routes
> the gate/advisory fork to the operator (Q-1), routes the identity question to Plan (Q-2), declines
> to amend the FROZEN H.1 even though it measured a gap in it (Q-7), and states that **a
> reconstruction running today would return `BLOCKED` on nearly every dispatch** — calling that the
> correct output rather than hiding it. Under J.0's rule that no artifact may describe a mechanism
> *"con vocabolario più forte del protocollo compensativo"*, this document is **unusually well
> calibrated**: it names its compensator as *"a reader following pointers by hand"*.
>
> Its third strength is **epistemic honesty under self-application.** It caught its own `git grep`
> producing a false zero, and published the error rather than the correction — precisely because
> § 1.4 is about that class of error. It closes by turning its own § 3 against itself: *"a dispatch
> that cited this file as authority would fail `AUTHORITY_EXISTS`."* A document that specifies the
> test that disqualifies it is not seeking authority by the back door.
>
> **And its factual base holds.** I re-measured every load-bearing claim independently. The seven
> fragmented objects reproduce on the same seven refs. `ledger/events/` is absent across 42 refs.
> The lease derivation returns 0 with the two findings quoted. Every capability row is `UNVERIFIED`.
> H.1's row counts are exact. **This is not a document that argues from recollection.**

---

## F · FINDINGS

### EVIDENCE_FOR — claims re-measured and reproduced

#### F-1 · § 1.1 fragmentation — **CONFIRMED, and reproduced a third time by this review**

All seven rows re-tested with `git cat-file -e` against `main` and against all 33 heads:

| Object | on `main` | refs carrying it — **my measurement** | object's claim |
|---|---|---|---|
| `runtime/agent_card_registry.md` | ❌ | `orchestrator` | matches |
| `reviews/mirror/REV-ROLES-MIRROR-001.md` | ❌ | `mirror` | matches |
| `reviews/mirror/HANDOFF-CANDIDATE-READINESS-001.md` | ❌ | `mirror` | matches |
| `governance/decisions/DEC-20260820-ORCH-SESSION-HOME.md` | ❌ | `orchestrator-surface`, `plan-orchsurf-r4-transcription` | matches |
| `governance/decisions/DEC-20260821-ORCHSURF-D2-TRANSCRIPTION-ROUTING.md` | ❌ | same two | matches |
| `governance/candidates/HANDOFF-ORCHSURF-MIRROR.md` | ❌ | same two | matches |
| `learning/plan/HANDOFF-20260822-ROLE-CONTRACT-REPAIR.md` | ❌ | `plan-orchsurf-r4-transcription` | matches |

**7 of 7 reproduce exactly, including the ref sets.** `governance/decisions/` on `main` contains
exactly one record (`DEC-20260822-…`) — re-verified by `git ls-tree`.

🔴 **The strongest evidence for this finding is § C-2 of this review**: the reviewer, dispatched to
judge the document, could not read `PROPOSAL-C9-STATE-MODEL`, `DEC-20260822`, the lease record or
the lease script **from the reviewer's own ref**. The failure mode is not historical. It occurred
during its own review.

#### F-2 · § 2.4 event-ledger absence — **CONFIRMED, and it is correctly identified as load-bearing**

Repository-wide sweep, iterating all 42 refs across heads + tags + remotes:

```
refs whose tree contains ledger/events/ : 0
ledger/ on main : approvals · checkpoints · retirements · tasks
```

MEASURED_AT 2026-08-22 · VALIDITY: the 42 refs enumerated in § C, no wider.

J.2 defines `Ogni transizione = evento (J.1) + roster durevole`. **The event half has never
existed.** The object's inference — that every transition performed in this repository was
performed without the event half of its own definition, and that a reconstruction has no stream to
replay — **follows validly from the measurement.**

Corroborating: `runtime/agent_card_registry.md` records Mirror's *"Event ledger analysis"* as
**`blocked`, not merely unverified** — *"the ledger has no writer yet … P7 chose the design
(`ledger/events/<ACTOR_ID>.jsonl`, per-actor append-only) and recorded it as a debt, not built."*
And J.0 lists the compensator for absent runtime RBAC as *"authority matrix testuale + audit +
event ledger (H.1, J.1)"* — **a three-part compensator whose third part does not exist.** The
object's § 2.3 makes exactly this point; it is correct.

#### F-3 · § 1.3 readiness/identity/lease — **CONFIRMED verbatim**

`python3 framework/scripts/lease_state.py --check`, run by me on the root checkout at `main`:

```
ACTIVE by derivation: 0
lease #3  derived=STALE   stored=EXPIRED
FINDING: lease #3 DISAGREEMENT: stored STATUS='EXPIRED', derived='STALE'.
FINDING: lease #3 EXPIRED_WITHOUT_RENEWAL … Renewal is a proxy for use and a poor one
```

Five records, most recent released `2026-08-18T14:05:20Z`. `EXPIRED` is indeed absent from I.3's
declared vocabulary (`ACTIVE | STALE | RELEASED`).

**Capability:** every row across all six cards and four roles reads `status: UNVERIFIED,
last_verified: NONE` — counted, no exceptions. **Identity:** two Scientist `ACTOR_ID`s are
`UNRESOLVED` with `STATUS: NOT_REGISTERED`; `scientist-c` is `REGISTERED_PENDING_L1_L2`.
**Conflict C-7** is present as described: *"`legend-public-12 [cf79f1]` is seen by all four actors,
and is the self of none … it is the operator's to identify or close."*

#### F-4 · § 1.2 authority state — **CONFIRMED**

`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` exists on `main`,
`status: BINDING_AS_AN_OPERATOR_DETERMINATION_OF_STATE`, decides **`OPTION B —
ACTIVATION_NOT_CONFIRMED`**, and consequence 2 reads as quoted: *"No actor authority may be assumed
from these contracts … never to a role contract clause standing alone."* Its record of
`REV-ROLES-MIRROR-001` — CHANGES_REQUIRED on three contracts, **no verdict on the fourth** — and of
the outstanding `AUTHOR_RESPONSE` both reproduce. Its `OUT_OF_SCOPE` does decline to assign
ownership of any finding or repair.

#### F-5 · § 5.1 H.1 compatibility — **CONFIRMED**

H.1 counted: **17 rows.** Orchestrator appears in the authority column of exactly **5**
(`Task / priorità`, `Livello Ladder`, `CANONICAL_BATCH_COMMIT`, `Classificazione HUMAN_REQUIRED`,
`Aggiudicazione challenge`) and as the **target** of a 6th (`Promozione BOOTSTRAP_CONTROLLER →
Orchestrator … mai autoassunzione`). The object's arithmetic is exact.

The three separations in § 5.1 are each traced to the correct row, and each holds:

| Risk | Governing row | Object's position | My assessment |
|---|---|---|---|
| Orchestrator as scientific reviewer | `Conclusione scientifica` → Scientist, *"mai a ordine"*; `Epistemic / method review` → Mirror | reconstruction asks **whether a review exists and is closed**, never whether its verdict is right | **sound** — reading a disposition is not reviewing a finding |
| Orchestrator as governance authority | `Spese / MAJOR approval / governance` → Operatore; `Classificazione MAJOR dubbia` → Mirror fail-closed | `OPERATOR_DECISION_REQUIRED` **routes**, and routing is the opposite of deciding | **sound, with F-7 as the residual** |
| Orchestrator as owner of others' work | `Integrazione strutturale` → Plan; `WORK_COMMIT` → *"ogni attore, solo proprio branch"* | reconstruction reads other branches, **writes to none** | **sound** — read-only cross-ref access creates no write authority |

#### F-6 · § 5.2's diagnosis — **CONFIRMED, and it is the document's best sentence**

> *"The loop is not blocked by authority — the authority is cleanly allocated by H.1 and none of the
> three risks above is close to being realised. It is blocked by addressing."*

I tested the stronger half of this independently. **H.1 does allocate every edge of the named loop
without gap or overlap** for the decision types involved. And the addressing failure is F-1,
measured. The diagnosis separates a governance problem from a mechanical one and correctly
concludes it is mechanical — which is what makes the proposal *narrow* rather than expansionary.

---

### EVIDENCE_AGAINST — where my measurement diverges

#### F-7 · 🔴 § 2.1's ref-field claim is **WEAKENED** — the object missed the strongest precedent for its own recommendation

The object states:

> *"**no existing handoff artifact carries a ref field as a required element** — `HANDOFF-P5DOMAIN-MIRROR`
> carries `BRANCH` in a prose code block by the author's own care, not by any schema"*

**Measured, across all 15 handoff-named paths on all heads+tags:**

```
main:governance/candidates/HANDOFF-GOV311-ORCHESTRATOR.md
  frontmatter keys: artifact · candidate_id · candidate_content_hash ·
                    base_head · source_branch · domain · prepared_by · prepared_on · authority
```

**`HANDOFF-GOV311-ORCHESTRATOR` carries `source_branch:` *and* `base_head:` as structured
frontmatter keys — not prose.** It also carries `candidate_content_hash:`, which is precisely the
immutable identifier § 2.1's fourth row calls for and reports as having *"nothing analogous for a
handoff"*.

**Why this is WEAKENED and not REFUTED.** The claim's literal wording — *"as a required element"* —
survives: B.2 specifies no schema, so **no field is required of any handoff**, and a key present by
one author's care is not a required element. The claim is *technically true and vacuously so*.

**But the evidence offered for it understates existing practice by a full tier**, and the cost is
real: the object argues from the weakest example (prose `BRANCH`) when a stronger one exists that
**already implements § 2.1's recommendation in structured form**. A reader is left believing the
repository has no precedent for ref-carrying dispatch records. **It has one, on `main`, and Q-2
should be answered from it rather than from a blank page.**

#### F-8 · § 0.1's handoff count is **REFINED** — the counting rule is undeclared

Object: *"**14 distinct paths repository-wide** carry a handoff name — 11 actor-to-actor, 3
release-process"*.

**My sweep returns 15 distinct paths** matching `/handoff/i` across heads + tags. The 15th is
`runtime/handoff/C-2/PMID42422765.working.lettore-and-lettore-b.json` — whose **path** carries
"handoff" (via the directory) while its **filename** does not.

- Counting by **filename** → 14. Object's figure.
- Counting by **path substring**, which is what *"paths … carry a handoff name"* says → 15.
- The 11 / 3 split is **exact** under either rule (release-process: `CONTENT_HANDOFF`,
  `FULLTEXT_TRACE_HANDOFF`, `LINK_MIGRATION_HANDOFF`).

**REFINED, not REFUTED**: the substance is untouched and the discrepancy is one working payload.
But this is a document whose § 1.4 is *precisely* about negatives produced without a declared
measurement surface, and **it states a count without declaring its counting rule.** Held to its own
standard, the row should read *"14 by filename; 15 by path"*.

**The underlying claim it supports — that each handoff invents its own shape — is CONFIRMED far
more strongly than the object argues it.** Five artifacts, five disjoint key sets:

```
HANDOFF-GOV311-ORCHESTRATOR   artifact candidate_id candidate_content_hash base_head
                              source_branch domain prepared_by prepared_on authority
HANDOFF-P5DOMAIN-MIRROR       artifact from to opened_by delivery date domain
HANDOFF-XPORT-MIRROR          artifact handoff_id candidate from to opened_by date domain consequence
HANDOFF-CANDIDATE-READINESS   artifact handoff_id reviewer adjudicator date scope
runtime/handoff/C-2/…         (a JSON working payload, no frontmatter at all)
```

**No key appears in all five except `artifact`.** `from`/`to` appear in three; `handoff_id` in
three; the ref-bearing keys in **one**. Q-6 is a well-founded question.

---

### KEY_OBJECTIONS — risks the object creates or leaves open

#### F-9 · Overlap with Mirror epistemic review — **OBSERVATION ONLY, no verdict (D-1, G.2)**

I am barred from adjudicating the scope of my own function. Recorded as observation:

- § 3 `REVIEW_REQUIREMENTS_MET` asks *"What is the Ladder floor … Is AUTHOR ≠ REVIEWER ≠
  ADJUDICATOR satisfiable … Does any actor face a self-review prohibition"*. **These read C.1 and
  C.3 structurally** — floor, role distinctness, prohibition — and none of them reads a finding or
  re-weighs a verdict.
- § 5.1 row 1 states the boundary explicitly: *"asks whether a review exists and is closed, never
  whether its verdict is right."*
- § 3 `OPERATOR_DECISION_REQUIRED` routes a doubtful MAJOR to Mirror fail-closed, consistent with
  H.1 rather than substituting for it.
- **Observation, not verdict:** on my reading of the text, the object routes to Mirror and does not
  displace Mirror. **A residual exists and I decline to size it**: `REVIEW_REQUIREMENTS_MET` sits
  one interpretive step from *"is this review adequate"*, and the actor best placed to notice that
  step being taken is the actor whose function it would absorb. **An independent reviewer should
  size this, not me.** G.2's flow — *"proposal → Plan candidate → reviewer indipendente scelto da
  Orchestrator"* — is the governing path.

#### F-10 · Orchestrator as hidden authority — **risk is real, correctly named, not yet closed**

The object does **not** create Orchestrator governance authority. It is `normative: no`,
`authority: none`, contains no rule, and § 7 lists what it did not do — a list I verified: **1
commit, 1 file, 426 insertions, 0 deletions**, under a declared `CONTROL_PLANE_ROOT`, touching no
annex, no role, no ledger, no decision.

🔴 **The residual risk is the Q-1 fork, and it is a one-way door.** If a `TRANSITION_CHECK` is
adopted as a **gate**, it is a normative rule requiring the governed path. If adopted as an
**advisory**, J.0's compensator for absent RBAC is not strengthened by it. **The dangerous third
path is neither**: a check that is never formally adopted, but that the Orchestrator consults at
every dispatch until *"reconstruction says BLOCKED"* becomes the operative reason a task does not
proceed. **That is a gate with no adoption record**, and it would accrete exactly the authority the
document disclaims — through use, not through a clause.

The object identifies this precisely (*"A gate that blocks dispatch is a normative rule and would
need the governed path"*) and routes it to the operator. **The proposal is not at fault; the fork
is simply unresolved, and it must not be resolved by drift.**

#### F-11 · Reconstruction becoming interpretation — **conceded by the object, and the concession is correct**

The mitigations are already specified and are the right ones: § 4 requires `EVIDENCE` to carry
*"the command run and its **output**, not its conclusion"*, and adds `MEASUREMENT_SURFACE` so
`MISSING_OBJECT` cannot be confused with *not looked for*. **§ 4's `MISSING_OBJECT` as `(ref, path)`
is the single most valuable field proposed**, and F-1 is why: *"missing"* would have been false for
the agent card registry; *"missing from `main`, present on `orchestrator`"* is true and names the fix.

**But the residual is structural, not editorial.** Several § 3 questions are not mechanically
answerable: *"Is its readiness observed, or self-declared?"* has a fixed answer today
(self-declared, always — F-3) and *"Are prerequisites known to be resolved, or merely not known to
be unresolved?"* requires judgement, not a command. With `ledger/events/` absent (F-2),
reconstruction must derive from git state, which **the object itself concedes** *"shows what an
object is, never what an actor intended or closed."*

🔴 **So reconstruction today would be interpretation, and the object says so** (§ 5.3, and its
prediction that it would return `BLOCKED` on nearly every dispatch). **I confirm that reading.** The
danger is not in the document; it is in a future adopter reading § 3 as a checklist that mechanises
a judgement it cannot mechanise. **§ 5.3 must travel with § 3 wherever § 3 goes.**

#### F-12 · Transition checks becoming unapproved gates — see F-10; and one specific vector

Beyond F-10's drift path: **§ 3's checks have no declared ordering and no declared owner**, which
the object states deliberately. If any adopter supplies an ordering, the first check becomes a
de facto precondition for the rest, and *ordering is policy*. Recorded as a constraint on any
future adoption, not as a defect here.

#### F-13 · Relationship with `PROPOSAL-C9-STATE-MODEL` — **a genuine collision risk, correctly deferred**

C-9 is on `main`: `status: ACCEPTED`, `acceptance_is_not_adoption: true`, held. Measured overlap:

| C-9 | This proposal | Assessment |
|---|---|---|
| § 6.1 `RESOLVER CONTRACT` — input `(artifact, field, value, since_event)`, returns `CONFIRMS \| CONTRADICTS \| UNRESOLVABLE`, **`fail-closed: UNRESOLVABLE is a failure, never a pass`** | § 3 `TARGET_EXISTS` — is the object addressed as `(ref, path)`, does the ref resolve, is an immutable identifier recorded | **Near-neighbours, not duplicates.** C-9 resolves an *event pointer for a status field*; this resolves an *artifact address for a dispatch*. **Both are fail-closed resolution contracts over a declared durable location** |
| § 5.1 transition owners: *actor lifecycle state (J.2)* → **orchestrator**; *capability `UNVERIFIED → VERIFIED`* → **orchestrator** | Q-4 *"Who writes actor readiness?"* — recorded as unresolved | 🔴 **C-9 already answers a large part of Q-4**, and the object says so (*"Adjacent to C-9 § 5 ownership-of-writer, which is held"*). Accurate |

**The risk if both are adopted independently: two fail-closed resolvers, two vocabularies, two
locations** — and a dispatcher would have to know which contract governs which pointer. The object
declines to merge them (Q-10: *"Whether these are one proposal or two is not decided here, and this
file adopts no clause of C-9"*), which is **the correct refusal for an author who does not hold
`Integrazione strutturale`** — H.1 gives that to Plan.

**I make no merge recommendation** — that is Plan's row, subject to review. I record only that the
collision is real, that both documents are currently *held*, and that **resolving either without
the other would create the divergence both are trying to prevent.**

---

## G · IMPLEMENTATION BOUNDARY — every component classified

| Component | Class | Basis |
|---|---|---|
| § 0 surface map; § 0.1 vocabulary table | **OBSERVATION** | measurements with declared surface; re-verified F-1…F-5 |
| § 1.1–1.4 failure modes | **OBSERVATION** | all re-measured; 7/7, 0/42, lease output verbatim |
| § 2.1–2.4 "Status today" columns | **OBSERVATION** | measured state of existing sources |
| § 2.1–2.4 "Question / Would be answered from" columns | **SPECIFICATION** | proposes what a record *would* carry; binds nobody |
| § 3 `TRANSITION_CHECK` question set | **SPECIFICATION** | a closed set of questions; no ordering, no owner, no effect declared |
| § 4 block field list (`BLOCK_REASON`, `EVIDENCE`, `MEASUREMENT_SURFACE`, `MISSING_OBJECT`, `REQUIRED_DECISION_OWNER`, `NEXT_ALLOWED_ACTION`) | **SPECIFICATION** | describes information a block *would* carry; no home, no writer |
| § 5.1 H.1 mapping | **OBSERVATION** | reads the frozen matrix; adds nothing to it |
| § 5.3 limits | **OBSERVATION** | correctly states what reconstruction cannot fix |
| **Q-1** gate vs advisory vs report | 🔴 **GOVERNANCE DECISION** | a blocking check is a normative rule — H.1 → Operatore |
| **Q-2** what identifies a dispatched object | **GOVERNANCE DECISION** (delegable) | H.1 `Integrazione strutturale` → Plan, subject to review |
| **Q-3** whether a block maps to A.5 `BLOCKED` | **GOVERNANCE DECISION** | A is FROZEN |
| **Q-4** who writes actor readiness | **GOVERNANCE DECISION** | collides with C-9 § 5.1 — F-13 |
| **Q-6** schema for B.2 `HANDOFF` | **GOVERNANCE DECISION** | **Annex B is FROZEN** — governed change, operator |
| **Q-7** an H.1 row for "may actor X act on object Y" | **GOVERNANCE DECISION `[MAJOR]`** | H.1 is `[MAJOR]` and FROZEN. **The object explicitly does not propose amending it** — correct |
| **Q-5, Q-8, Q-9, Q-10** | **OBSERVATION** (open questions) | Q-8 is the operator's per the registry |
| any writer, script, schema or field construction | **IMPLEMENTATION** | 🔴 **none present in the object, and none proposed here** |

**The boundary is respected.** The object contains observation and specification, and routes every
governance decision outward rather than making one. **No component crosses into implementation.**

---

## H · VERDICT

```
VERDICT: CONFIRMED (with two sub-claims WEAKENED / REFINED — F-7, F-8)
```

**`PROPOSAL-ORCH-STATE-RECONSTRUCTION` is a valid architectural candidate under current repository
governance.**

Per C.2, `CONFIRMED` means *"nessun difetto rilevato dato l'evidence bundle disponibile"* — **not
"true", and emphatically not "adopt it".** Scoped precisely:

**CONFIRMED:**
- **Governance compatibility.** It respects H.1 boundaries (F-5), creates no Orchestrator
  governance authority (F-10), and **moves no decision away from the operator** — it routes
  decisions *toward* the operator that no record previously routed anywhere (§ 3
  `OPERATOR_DECISION_REQUIRED`, Q-1, Q-7).
- **Architectural necessity.** The problem is real and repository-observed, not recalled. All four
  named conditions verified independently: fragmented refs (F-1, 7/7), missing routing information
  (F-7/F-8, one ref-bearing handoff of fifteen), missing event ledger (F-2, 0 of 42 refs), actor
  readiness uncertainty (F-3, every capability `UNVERIFIED`, two `ACTOR_ID`s `UNRESOLVED`, C-7 open).
- **Implementation boundary.** Held (§ G).

**WEAKENED — F-7:** § 2.1's ref-field claim survives literally but rests on evidence that
understates existing practice; `HANDOFF-GOV311-ORCHESTRATOR` already carries `source_branch`,
`base_head` and `candidate_content_hash` as structured keys.

**REFINED — F-8:** the handoff count is 14 by filename, 15 by path; the counting rule is undeclared
in a document about undeclared measurement surfaces.

**NOT CONFIRMED, because not adjudicated by me — F-9:** the overlap with Mirror epistemic review is
**observation only** under G.2 and the dispatch's self-review clause. **This verdict does not cover
it.** An independent reviewer must.

🔴 **What this verdict does not do.** It does not adopt any § 3 check, resolve Q-1, merge or
sequence this with C-9, or make the object citable as authority. **The object's own § 3 still
disqualifies it**: a dispatch citing it as authority fails `AUTHORITY_EXISTS`, and that remains true
after this review. **Validity as a candidate is not adoption** — the same distinction C-9 carries as
`acceptance_is_not_adoption`.

---

## I · REVIEWER_CONFIDENCE / RESIDUAL_UNCERTAINTY / EVIDENCE_NEEDED

**REVIEWER_CONFIDENCE: HIGH on the factual base · MEDIUM on the governance judgement.**

High on facts: every load-bearing claim was re-measured with commands whose output is reproduced
here, and 7/7, 0/42, 17 rows, 5+1, and the lease output all reproduced exactly. Medium on
governance: the judgement that § 3 does not displace Mirror rests on **reading the text as written**,
and F-10 is a risk that materialises through *use*, which no reading of a document can foreclose.

**RESIDUAL_UNCERTAINTY:**
1. **F-9 is unsized by design.** I am barred from measuring encroachment on my own function.
2. **The Q-1 fork is unresolved**, and the drift path in F-10 is not closed by anything currently
   in the repository.
3. **My ref is divergent** (`64 / 71`). Every claim about `main` was made cross-ref by
   `git cat-file` / `git show`, never from my working tree. Should `main` have moved after
   `2bb2700`, § C-1's identity finding must be re-derived.
4. **`AUTHOR_RESPONSE` is outstanding**, and C.2 states silence is not acceptance.
5. **42 refs is not the universe.** Clones, unpushed worktrees and unreferenced objects are outside
   my surface, and F-2 is an absence claim.

**EVIDENCE_NEEDED to move this review further:**
- An independent reviewer's verdict on F-9 (G.2 flow: proposal → Plan candidate → independent
  reviewer chosen by Orchestrator → validation).
- Plan's determination on Q-2, ideally taking `HANDOFF-GOV311-ORCHESTRATOR`'s existing key set as
  the starting point rather than a blank page (F-7).
- The operator's resolution of Q-1 **before** any § 3 check is consulted in practice (F-10).
- A joint sequencing determination for C-9 and this proposal, from Plan (F-13).

---

## J · WHAT_WOULD_CHANGE_MY_MIND — declared falsifiers, required by C.2

**Each is a specific, runnable measurement. Any one of them overturns the part named.**

1. **`git ls-tree -r <ref> -- ledger/events/` returning a non-empty result on any ref I did not
   survey** — including a clone, an unpushed worktree, or a ref created after 2026-08-22. **This
   would refute F-2**, restore the event half of J.2's definition of `transizione`, and remove the
   object's load-bearing absence. **Q-5 would become answerable in the affirmative**, and the
   objection that reconstruction inherits a permanent blind spot for intent would fall.

2. **A normative file defining `transition` (or `TRANSITION_CHECK`) as a governed term**, found by a
   query I ran wrongly. My grep was POSIX ERE without `\b` precisely because the object documented
   that trap — but **a differently-malformed query is still a query**. This would overturn B-1 and
   convert the object's vocabulary from external to governed, changing what it may be cited for.

3. **Any handoff artifact carrying a ref field by *schema* rather than by authorial care** — i.e.
   a normative file requiring it. This would **strengthen F-7 from WEAKENED to REFUTED** and make
   Q-6 already-answered. Conversely, **evidence that `HANDOFF-GOV311-ORCHESTRATOR`'s keys were
   themselves schema-driven** (a Plan template, a validator) would move F-7 further: the object
   would have missed not one precedent but an existing convention.

4. **A merge making `main` a superset of the seven § 1.1 objects.** This would not refute F-1 —
   which is a measurement of a moment — but it would **destroy the object's architectural
   necessity**, because § 5.2's diagnosis (*"blocked by addressing"*) presupposes objects that are
   unreachable from where a dispatcher stands. **If `main` carried all seven, the proposal would
   solve a problem the repository no longer has**, and my CONFIRMED on necessity should be withdrawn.

5. **An independent reviewer finding that § 3 `REVIEW_REQUIREMENTS_MET` does displace Mirror's
   `Epistemic / method review` row.** I am barred from ruling on this (D-1, G.2). Such a finding
   would convert F-9 from observation to defect and **should override § H**, since my verdict
   explicitly excludes that question.

6. **An `AUTHOR_RESPONSE` showing that a § 3 check was already consulted at a real dispatch**
   before Q-1 was resolved. This would demonstrate F-10's drift path is **not hypothetical but
   already realised**, and CONFIRMED on governance compatibility would have to be withdrawn — the
   authority would have accreted through use exactly as F-10 describes.

7. **A governed determination that C-9 and this proposal are one object.** This would not falsify
   any measurement, but it would make **reviewing them separately a methodological error**, and
   this review would need to be reissued against the merged object.

---

## K · AUTHOR_RESPONSE

```
AUTHOR_RESPONSE: REQUIRED AND OUTSTANDING
```

**Annex C.2: `AUTHOR_RESPONSE (obbligatoria; il silenzio non è accettazione)`.**

Owed by the author (`orchestrator`) on **F-7** (WEAKENED — the missed precedent) and **F-8**
(REFINED — the undeclared counting rule). **This review ratifies nothing until it is written**, and
its absence may not be read as agreement.

Per D-3, **adjudication of any disagreement escalates to the operator**, because H.1's designated
adjudicator is the author of the object under review.

---

*Prepared by Mirror under Annex C.2 at R4. Read-only: this review modified no governance file, no
proposal, no ledger and no decision. It creates one file under `reviews/`, a declared
`CONTROL_PLANE_ROOT`, and therefore changes no candidate content hash and no role fingerprint.*

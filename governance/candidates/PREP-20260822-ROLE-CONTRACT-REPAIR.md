---
artifact: CANDIDATE REPAIR PREPARATION — the four role contracts
prep_id: PREP-20260822-ROLE-CONTRACT-REPAIR
task_id: PLAN_ROLE_CONTRACT_REPAIR_PREPARATION_v2
iteration: 2/3
author: plan
authored_on: 2026-08-22
dispatcher: operator
governance_version: 3.1.1

STATUS: PREPARATION_ONLY
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED

responds_to: reviews/mirror/REV-ROLES-MIRROR-001.md (refs/heads/mirror, 1350477)
reads: governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md (refs/heads/main, 2bb2700)
applies_to:
  - roles/plan.md
  - roles/orchestrator.md
  - roles/scientist.md
  - roles/mirror.md
modifies: nothing. No file under roles/, governance/decisions/, framework/ or ledger/ is touched.
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1), so this
  file is outside the candidate content domain and cannot move any candidate hash.
author_response_status: this document is NOT the AUTHOR_RESPONSE that Annex C.2 requires for
  REV-ROLES-MIRROR-001. That response remains required and outstanding.
verdict_transfer: NONE. Every mechanical fact below was executed or recomputed in this session at
  the HEAD named in § 2. Nothing is carried from the review, the decision record or any handoff.
---

# CANDIDATE REPAIR PREPARATION — ROLE CONTRACTS

> **This document prepares repair candidates. It repairs nothing, activates nothing, approves
> nothing and resolves no finding.** Where a corrected clause already exists in a repository
> source it is cited by blob and ref; where none exists, none is written.

---

## 0 · WHAT THIS DOCUMENT IS NOT

Per the dispatch and per `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` § OUT_OF_SCOPE, this
record does not: activate a contract · ratify text · change any `status:` line · create a `DEC` ·
create a `HUMAN_APPROVAL` record · resolve, downgrade or dismiss any finding · assign unresolved
authority · resolve `MIRROR_RETROSPECTIVE` cadence `N` · choose between stated alternatives.

The four contracts' status line —

```
status: PROPOSED — binding once Mirror hostile review passes and the operator approves
```

— is unchanged on all four objects and is not proposed to change here.

---

## 1 · IDENTITY

| Field | Value | How established |
|---|---|---|
| `actor_id` | `plan` | `roles/plan.md`:3 |
| role contract source | `roles/plan.md`, blob `7e1e04cb53`, sha256 `e1c26d42854a54ffb975095f95f1a0ee90c85eb9f881576d637ec7b6e084c0ff` | `git ls-tree`, `shasum -a 256` |
| declared worktree | `evidence-index` | `roles/plan.md`:5 |
| current filesystem path | `<REPO_ROOT>/.claude/worktrees/evidence-index` | `pwd` |
| current branch | `plan-orchsurf-r4-transcription` | `git rev-parse --abbrev-ref HEAD` |
| `HEAD` | `b14a0d1466962aa79d1bbd0065a0d1141f4a0eab` | `git rev-parse HEAD` |
| working tree status | clean before and after | `git status --porcelain` |

### 🔴 THE ROLE CONTRACT IS NOT BINDING — reported explicitly, as the dispatch requires

`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE`, `OPTION B — ACTIVATION_NOT_CONFIRMED`, binding as
an operator determination of state under Annex H.1:

> **The four contracts remain `PROPOSED`.** … they are, as of this record, non-binding documents.
> Their `status:` lines are **accurate**, not stale.
> **No actor authority may be assumed from these contracts.**

`roles/plan.md` is therefore **not a source of authority for this session.** Nothing in this
document is done on its authority. The work is done on the operator's dispatch, and every
structural act it performs traces to a named instrument rather than to a contract clause:
Annex D.1 for the `WORK_COMMIT`, P5.1 for the control-plane domain, Annex C.2 for the review
format it responds to.

**The dispatch grants nothing either**, and is not treated as granting anything.

### Worktree / branch note, recorded not resolved

`roles/plan.md`:5 declares `worktree: evidence-index` and declares **no branch**. The directory
`…/.claude/worktrees/evidence-index` is checked out on branch `plan-orchsurf-r4-transcription`,
while a separate `refs/heads/evidence-index` (`7a90a91`) exists and is checked out nowhere. The
contract's single `worktree:` field cannot distinguish the two. **This is structurally the same
under-specification that MAJOR-2 identifies in `roles/orchestrator.md`** — one field naming a
directory where a directory and a branch are separate facts — and it is recorded here as an
observation against Plan's own contract, not as a finding transmitted by Mirror. It is outside
this task's repair scope and is not repaired.

---

## 2 · DISPATCH VALIDATION

Every named concept, validated against the repository before use.

| Concept | Exists? | Exact identifier | Source location | Normative status |
|---|---|---|---|---|
| role contract | ✅ | `roles/*.md`; `ROLE_CONTRACT`, `ROLE_CONTRACT_HASH` | `roles/`; Annex I.1, I.4, A.6 | **normative** — but see § 1: currently non-binding per DEC-20260822 |
| hostile review | ✅ | Mirror hostile review, format Annex C.2 | `governance/annex_c_review_protocol.md` § C.2; body §12 GATE 3, §29 | **normative, FROZEN** |
| `CHANGES_REQUIRED` | ⚠️ | — | emitted by `REV-ROLES-MIRROR-001` per its dispatch | **NOT a governance vocabulary term.** C.2 is FROZEN and prescribes `{CONFIRMED, WEAKENED, REFINED, REFUTED}`. The review records this conflict itself and emits both. Used below only as the review's own label |
| `REV-ROLES-MIRROR-001` | ✅ | `reviews/mirror/REV-ROLES-MIRROR-001.md` | **`refs/heads/mirror` ONLY** (see § 3) | **observational** — a review, binding nothing; `AUTHOR_RESPONSE` outstanding |
| `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` | ✅ | `governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` | **`refs/heads/main` ONLY** (see § 3) | **BINDING_AS_AN_OPERATOR_DETERMINATION_OF_STATE**, Annex H.1 |
| candidate repair | ⚠️ | nearest real objects: `INTEGRATION_CANDIDATE` (Annex D), `CAND-*` / `PREP-*` under `governance/candidates/` | Annex D; P5.1 | **the compound term is EXTERNAL.** `PREP-20260820-ORCHSURF-REV4.md` is the naming precedent this file follows |

### DISPATCH_CONTAMINATION

**Recorded, per the dispatch's own instruction.** Two of the six concepts have no repository
grounding as named:

```
CHANGES_REQUIRED    external to the governance vocabulary; C.2 (FROZEN) prescribes a different set
candidate repair    external as a compound term; the repository has INTEGRATION_CANDIDATE / CAND- / PREP-
```

`DISPATCH_CONTAMINATION` is **itself an external token** — `REV-ROLES-MIRROR-001` § 1 measured it
`ABSENT across all 41 refs`, and this session's own survey confirms it remains absent. It is used
because the dispatch asks for it, and it creates no repository meaning.

The dispatch's `NEXT_TRANSITION` vocabulary — `C.2 REVIEW`, `HUMAN_APPROVAL_QUEUE`, `GATE 0-5` —
**is repository-defined**, and each resolves: Annex C.2; Annex J.3 + `ledger/approvals/`; body §12.

**Objective established.** The task is repository-grounded independently of the contaminated
terms: a Mirror review of four named objects exists and carries findings; an operator decision on
their activation state exists; Annex C.2 makes an author response mandatory. Work proceeds.

---

## 3 · SURFACE MAP

### CURRENT SURFACE

```
checkout path       <REPO_ROOT>/.claude/worktrees/evidence-index
branch              plan-orchsurf-r4-transcription
HEAD                b14a0d1466962aa79d1bbd0065a0d1141f4a0eab
working tree        clean (git status --porcelain empty) before and after the commit
LINT                PASS — 1 INFO (MISSING_WIKILINK, CLAIM 010, background only)
```

### SURVEY SURFACE

```
refs surveyed       46 total; 45 content refs enumerated (36 heads, 4 remotes, 5 tags)
                    excluded: 4 refs/codex/turn-diffs/* (harness capture refs), refs/stash
```

### 🔴 Neither input object is on this ref — both were read from the ref that carries it

| Input object | Present on | Read at |
|---|---|---|
| `governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` | **`refs/heads/main` only** — 1 ref of 45 | `git show refs/heads/main:…` @ `2bb2700` |
| `reviews/mirror/REV-ROLES-MIRROR-001.md` | **`refs/heads/mirror` only** — 1 ref of 45 | `git show refs/heads/mirror:…` @ `1350477` |

`NOT_FOUND` on this checkout was **not** converted to `NOT_EXIST`. Both objects were located by
sweeping `git ls-tree -r` over every ref before any statement was made about them.

### 🔴 The reviewed objects DIFFER across refs — and two differ between the review surface and this one

| Object | Blob at my HEAD | Blob Mirror anchored on | Same? |
|---|---|---|---|
| `roles/plan.md` | `7e1e04cb53` | `7e1e04cb53` | ✅ identical — **19 refs, one blob, zero divergence** |
| `roles/mirror.md` | `6e515059af` | `6e515059af` | ✅ identical — 19 refs, one blob |
| `roles/orchestrator.md` | **`24663eec77`** | `2bbb214143` (`main`, `mirror`) | ❌ **differs** |
| `roles/scientist.md` | `fd30134dc8` | `fd30134dc8` (`main`, anchored) | ✅ matches the anchor |

**Consequence, and it is load-bearing for § 5.** This checkout carries the *post-transcription*
`roles/orchestrator.md`. Mirror reviewed the pre-transcription blob and explicitly recorded that
the repair exists on a side ref. **I am standing on that side ref.** Every statement in § 5 names
which blob it is about.

`roles/scientist.md` splits three ways across refs, and the third way is not what the review
reports — see § 6, MINOR-3.

### Branch authority for every negative statement in this document

| Negative claim | MEASURED_AT | VALIDITY |
|---|---|---|
| No repaired `roles/plan.md` exists | `git ls-tree` over all 45 content refs | **confirmed across all refs** — 19 carry it, all one blob `7e1e04cb53` |
| No amended `scientist_reading_modes.md` status line exists | `git ls-tree` over all 45 content refs | **confirmed across all refs** — 8 carry it, all one blob `2aae1ca758` |
| No `HUMAN_APPROVAL` for `CAND-20260819-ORCHSURF` exists | `HUMAN_APPROVAL_QUEUE.jsonl` on every ref carrying it (19) | **confirmed across all refs** |
| `roles/orchestrator.md` repair blob `24663eec77` is on 2 refs, neither `main` | `git ls-tree` over all 45 content refs | **confirmed across all refs** |
| `governance/decisions/` absent from all refs but `main` and this lineage | `git ls-tree` over all 45 content refs | **confirmed across all refs** |
| H.1 has exactly one row with an unassigned Authority cell | `awk` over the H.1 table, this ref `b14a0d1` | **this ref only** — H.1 is byte-identical to `main`'s copy at this HEAD |

---

## 4 · `roles/plan.md` — findings consumed

### MAJOR-1 · a capability declared structurally blocked by a tool that runs

- **Finding reference** — `REV-ROLES-MIRROR-001` § 3, MAJOR-1.
- **Affected object** — `roles/plan.md`:73, blob `7e1e04cb53`, identical on all 19 refs carrying it.

**Evidence, re-executed at `b14a0d1` — not taken from the review.**

The contract row, verbatim:

```
| Fingerprint composition | emit a fingerprint for a named role — **blocked: the composition is prose, not a script** | UNVERIFIED |
```

```
$ python3 governance/scripts/governance_fingerprint.py compose --all
mirror        e01b410891c4f3008b21418f695a4d60514b1810518b3c8d039bc8c6f08a0412
orchestrator  f85d743c8b31597b8c96430ac36b77f62f650b94750f9df941a929dd4022fefe
plan          0d6987bd79e54839cb33052b95bf85116d77c18537c27951fc08eeaefaec1429
scientist     b66959cd0bb7ccd5c410083fba0107da9157a2b6ddb68c3f86bdbefefc489d1a
EXIT=0
```

The tool exists, is advertised by `CLAUDE.md` § 3, exits 0, and emits a fingerprint for a named
role. **The declared blocker is false as measured at this HEAD.**

**🔴 Mirror's declared falsifier for MAJOR-1 was executed this session, and MAJOR-1 survives it.**

C.2 obliges the reviewer to state what would change its mind. For MAJOR-1 that was:

> *MAJOR-1 falls if `governance_fingerprint.py` is shown not to implement the P2.2 composition the
> contract row means … Test: recompose one role by hand from P2.2 and compare. I ran the weaker
> version … a full hand-composition would settle it.*

The full hand-composition was run — for `plan`, the role whose contract carries the false blocker.
A separate implementation was written from § P2.1–P2.2's prose alone (CORE block and per-role
table transcribed by eye; section extraction, lexicographic sort and `"<id>:<sha256>\n"`
serialization implemented independently), importing nothing from the repository script:

```
inputs counted by hand : 13   (matches the script's input set exactly, identifier for identifier)
HAND-COMPOSED plan fingerprint: 0d6987bd79e54839cb33052b95bf85116d77c18537c27951fc08eeaefaec1429
SCRIPT-COMPOSED               : 0d6987bd79e54839cb33052b95bf85116d77c18537c27951fc08eeaefaec1429
```

**Exact agreement.** The falsifier is discharged in the direction that strengthens the finding:
the script does implement P2.2, so the row's blocker is not merely imprecise — it denies a
capability the repository demonstrably has. MAJOR-1 stands, and no longer rests on an untested
falsifier.

- **Candidate repair intent** — the row must stop asserting a structural impossibility, because
  Annex I.4 and body §8 make the row an input to live assignment, and a row declaring the
  capability impossible suppresses the L2 smoke that would move it off `UNVERIFIED`.

  **🔴 No corrected clause is written here.** `roles/plan.md` is byte-identical on all 19 refs
  carrying it (measured, § 3): **no repository source anywhere contains repaired text for this
  row.** The dispatch forbids authoring one, and none is authored.

- **Unresolved questions — stated, not chosen between:**
  1. Does the repair change the blocker phrase **only**, leaving `UNVERIFIED` standing? Or does it
     also carry L2 evidence and move the Status cell? These are different changes with different
     review levels. **Not chosen.**
  2. Capability verification is an Annex I.4 L2 act; a `VERIFIED` status an actor writes about
     itself is the self-declaration `CONFIGURED != PROVEN` exists to forbid. Who executes and
     witnesses the L2 for a Plan capability is **not resolved here**.
  3. Whether a repair may be prepared at all against a contract that DEC-20260822 holds
     non-binding — i.e. whether repairing precedes or follows the activation act that decision's
     consequence 3 requires. **Not resolved here.** It is a sequencing question for the operator.

### MINOR-1 · `ACTIVE_LESSONS` ownership — two contracts, same object, opposite subjects

- **Finding reference** — `REV-ROLES-MIRROR-001` § 3, MINOR-1.
- **Affected objects** — `roles/plan.md`:47–48; `roles/mirror.md`:37; upstream: Annex E.5, Annex H.1.

**Evidence, re-read at `b14a0d1`.**

`roles/plan.md`:47–48 — Plan may:

```
maintain `LEARNING_INDEX` durability and the role-specific `ACTIVE_LESSONS` subsets within
budget — epistemic curation of learning belongs to Mirror, durability belongs to Plan;
```

`roles/mirror.md`:37 — *"Learning clustering and `ACTIVE_LESSONS` selection within Plan's budget"*.

Annex E.5, verbatim:

```
Budget: ogni subset role-specific ha un budget dimensionale definito da Plan;
        superato → Mirror comprime o retrocede lezioni (mai toccando il RAW).
RECOVERY: ricalibrazione budget (Plan) o ricomposizione subset (Mirror, via G.2 se materiale)
```

E.5 gives **Plan the budget** and **Mirror the subset**. `roles/mirror.md` states that partition
correctly. `roles/plan.md`'s em-dash gloss narrows the claim but does not remove the verb: the
sentence still says Plan *maintains the subsets*.

- **Candidate repair intent** — none writable. **No repository source contains repaired text**
  (same measurement as MAJOR-1: one blob, 19 refs). More importantly, the repair cannot be
  determined from the contracts, because the authority they split is unassigned upstream — see
  the next item, which is not a separate defect but this one's cause.

### H.1 · lifecycle-learning authority is literally unassigned — measured

- **Finding reference** — `REV-ROLES-MIRROR-001` § 3, MINOR-1 (recorded there as *aggravating*).
- **Affected object** — `governance/annex_h_authority_matrix.md` § H.1, the table row at line 40.

**Evidence — Mirror's strong claim was tested, not accepted.** The review asserts this is *"the
one row in H.1 with no authority."* Tested by enumerating the Authority column of every row in the
H.1 table at this HEAD:

```
H.1 table: | Decisione | Authority |   — 17 data rows
rows whose Authority cell is a bare em-dash or empty: exactly 1

| Lifecycle learning: epistemico Mirror, durevolezza Plan | — |
```

**Confirmed.** Every other row names an authority — `Orchestrator`, `Plan`,
`Mirror (fail-closed)`, `mai Mirror da solo (G.2)`, `protocollo Annex I (mai autoassunzione)`.
This one names the split in the *Decisione* column and assigns it to nobody in the *Authority*
column.

- **Candidate repair intent** — **none, and this is the finding's disposition, not an omission.**
  H.1 is the authority matrix; assigning its empty cell is a governance change reserved to the
  operator (H.1's own row for governance; body §4, §10). The dispatch independently prohibits
  assigning unresolved authority and prohibits resolving Mirror/Plan epistemic ownership.

- **Unresolved question — the ordering, stated plainly:** MINOR-1 is a disagreement between two
  contracts about an object whose authority the constitution leaves blank. **Repairing either
  contract first would silently fill the blank cell** by making one document's verb the survivor.
  Whether H.1 row 40 is filled *before* the contracts are reconciled, or the contracts are
  reconciled in a way that does not presuppose it, is **not decided here** and is the single most
  consequential open question in Plan's contract.

### INFO · negative controls re-run at this HEAD

- `worktree: evidence-index` matches Annex I.2 step 4's worktree list ✅ — with the branch
  under-specification recorded in § 1.
- Plan's fingerprint set (*CORE plus Annex D, Annex E, Annex I, Annex J § J.1*) matches P2.2
  exactly — verified by the hand-composition above, which enumerated all 13 inputs ✅.
- `roles/plan.md` byte-identical across all 19 refs carrying it — zero divergence risk ✅.

---

## 5 · `roles/orchestrator.md` — findings consumed

### MAJOR-2 · the mandatory `WORK_COMMIT` has nowhere legal to land

- **Finding reference** — `REV-ROLES-MIRROR-001` § 4, MAJOR-2.
- **Affected object** — `roles/orchestrator.md` at blob **`2bbb214143`** — the blob on `main`,
  `mirror` and 15 other refs. **This is the blob the finding is about, and it is not the blob in
  my working tree.**

**Evidence, at the reviewed blob** — four clauses of one contract:

```
frontmatter  worktree: the repository root checkout
line 46      Orchestrator must not: commit its own work
line 49      … or treat the root as free working space
lines 88–89  Session Learning Review … persisted by WORK_COMMIT
```

against Annex D.1 / body §11 (`WORK_COMMIT → ogni attore, PROPRIO worktree/branch … Obbligatorio`)
and body §8 (Orchestrator *"MUST fare Session Learning Review"*). The contract names one surface,
forbids working in it, forbids the commit generally, requires the commit, and declares no branch.

**🔴 Independent corroboration the review did not cite — and it predates the review by three days.**

`ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` on `refs/heads/orchestrator` carries
`APR-20260819-XPORT-001` (`STATE: APPROVED`, `DECIDED_BY: operator`, 2026-08-19T17:05:17Z). Its
`CARRIED_UNRESOLVED.carried_debts` block names this defect explicitly:

```
"ORCHESTRATOR_WORKTREE_CONTRADICTION": "CARRIED_ROUTING_DEBT — roles/orchestrator.md frontmatter
 says the Orchestrator's worktree is the repository root checkout; deployment/deployment_profile.md
 gives it its own orchestrator worktree and reserves the root for canonical batch windows.
 Both are in main. NOT repaired here"
```

**MAJOR-2 was a named, operator-approved, explicitly carried debt before Mirror measured it
independently.** Two instruments reached it by different routes. Recorded as corroboration; it
changes no verdict and resolves nothing.

- **Candidate repair intent — the corrected clauses ALREADY EXIST in a repository source, and are
  cited rather than authored.**

  Blob **`24663eec77`**, carried by exactly two refs — `refs/heads/orchestrator-surface` and
  `refs/heads/plan-orchsurf-r4-transcription` (**this checkout's branch**) — and by **no other ref,
  measured across all 45**. It is the content of `CAND-20260819-ORCHSURF` revision 4.

  It addresses each of the three sub-items the dispatch names:

  | Dispatch sub-item | What the existing text does (`git diff main HEAD -- roles/orchestrator.md`) |
  |---|---|
  | branch declaration absence | replaces the single `worktree:` field with three — `session_home`, `worktree: orchestrator`, `canonical_batch_surface` — and names the branch in the added section: *"the `orchestrator` worktree, branch `orchestrator`"* |
  | root/worktree contradiction | adds *"Four concepts, and why the word `worktree` names only one of them"*, separating SESSION HOME / ACTOR WORK SURFACE / CANONICAL BATCH SURFACE / ROUTING, on the two axes `SESSION_LOCATION ≠ PERSISTENCE_SURFACE` and `ROOT location ≠ ACTOR_ID ≠ write authority` |
  | `WORK_COMMIT` contradiction | qualifies line 46 to *"commit its own work **to the canonical surface**"*, and quotes the operator's adjudicated formulation of 2026-08-20 verbatim: *"§ 35.1 constrains where persistent artifacts may be produced, not whether the Orchestrator may produce persistent artifacts."* |

  **The text is cited, not endorsed.** Whether it is the right repair is not determined here.

- **🔴 Unresolved questions — and the first is disqualifying for any claim that MAJOR-2 is repaired:**

  1. **The existing repair is UNAPPROVED.** `CAND-20260819-ORCHSURF` frontmatter reads
     `human_approval: NOT REQUESTED — no APPROVAL_ID is prefilled here, and none exists`, and this
     session's sweep of `HUMAN_APPROVAL_QUEUE.jsonl` on **every one of the 19 refs carrying it**
     found **zero** records naming ORCHSURF. The repair exists as text on two side refs and has no
     approval on any ref. **MAJOR-2 stands on the canonical branch**, exactly as the review states.
  2. Whether the repair route is *adopting `CAND-20260819-ORCHSURF` revision 4* or *a narrower edit
     confined to MAJOR-2's three clauses*. The candidate carries more than these three items.
     **Not chosen.**
  3. Whether `DEC-20260820-ORCH-SESSION-HOME` (present on this lineage, `status:
     BINDING_UPON_OPERATOR_RATIFICATION`, `change_class: CONFIRMATION`) already settles the
     *direction* of the repair while leaving the *text* unapproved. The candidate's `revision_4`
     field asserts it does. **Plan does not adjudicate its own candidate's claim about an operator
     decision, and does not do so here.**
  4. Mirror's residual uncertainty 3 is inherited unresolved: whether line 46's *"commit its own
     work"* is read through GATE 1 (*"Proponente ≠ esecutore … mai lavoro proprio"*) or absolutely.
     **Either reading yields a defect; they differ in severity, not existence.** Not chosen.

### MINOR-2 · the authority premise rests on a registry that is stale and single-refed

- **Finding reference** — `REV-ROLES-MIRROR-001` § 4, MINOR-2.
- **Affected objects** — `roles/orchestrator.md`:35–37; `runtime/agent_card_registry.md`.

**Evidence, re-measured.** `runtime/agent_card_registry.md` exists on **one ref only** —
`refs/heads/orchestrator` — and on no other of the 45. `roles/orchestrator.md` grounds authority in
an `ACTIVE` `ORCHESTRATOR_LEASE` and in the assigned role, both of which point at that registry.
Plan owns the registry (Annex I.4, body §43), so this finding lands on Plan's maintenance duty even
though it is filed against Orchestrator's contract.

- **Candidate repair intent** — none prepared. The registry is not a role contract and is outside
  the dispatch's `REPAIR SCOPE` ("Address only findings transmitted by REV-ROLES-MIRROR-001" as
  they bear on the four contracts). Recorded so it is not lost.
- **Unresolved** — whether a registry reachable from one ref can ground a contract clause at all is
  a question about the repository's ref topology, not about contract text. Not resolved here.

### INFO · not re-litigated

The review's clean negative controls for this contract (Annex D.4 / J.3 citations, Annex F.4
`DIAGNOSE`, Annex I.3 lease schema, body §9.4 `ORPHAN`, the P2.2 fingerprint set including the J.4
rationale) were not re-run. They are recorded as **the reviewer's measurements, not re-verified
here** — an honest limit of this document, since verdict transfer is otherwise refused throughout.

---

## 6 · `roles/scientist.md` — findings consumed

### MAJOR-3 · the contract asserts a protocol binds; the protocol says it binds nobody

- **Finding reference** — `REV-ROLES-MIRROR-001` § 5, MAJOR-3.
- **Affected objects** — `roles/scientist.md` blob `fd30134dc8` (the anchor blob, and the blob in
  this working tree); `framework/protocols/scientist_reading_modes.md` blob `2aae1ca758`.

**Evidence, re-read at `b14a0d1`.** `roles/scientist.md`:78–79:

> [`framework/protocols/scientist_reading_modes.md`] **binds every actor under this contract.**

`framework/protocols/scientist_reading_modes.md` frontmatter:

```
status: PROPOSED — binding on canonical execution of CAND-20260818-SCIENTIST-AB-SPEC, after
  Mirror hostile review and HUMAN_APPROVAL. Until then it binds nobody.
```

Both statements were installed by **the same commit**, `4454fea` — measured: that commit adds
`framework/protocols/scientist_reading_modes.md` (526 lines) and amends `roles/scientist.md`
(24 ±) in one change.

**🔴 NEW EVIDENCE, measured this session and not present in the review: all three conditions the
protocol's own status line names are independently satisfied by durable records.**

| Condition in the status line | Record | Located on | Measured |
|---|---|---|---|
| canonical execution of `CAND-20260818-SCIENTIST-AB-SPEC` | `4454fea` — *"The Scientist A/B specification becomes canonical…"*, installs the protocol + the candidate manifest | **ancestor of `refs/heads/main`** (`git merge-base --is-ancestor` → true) | 2026-08-19T15:08:55+02:00 |
| Mirror hostile review | `REV-SCIAB-MIRROR-006`, verdict `ACCEPT`, commit `98f8766` | **`refs/heads/mirror` only** | bound to hash `beef6db0…`, base `cbce3016` |
| `HUMAN_APPROVAL` | `APR-20260819-SCIAB-001` / `RES-20260819-SCIAB-001`, `STATE: APPROVED`, `DECIDED_BY: operator` | **`refs/heads/orchestrator` only** | 2026-08-19T13:02:58Z = **15:02:58+02:00** |

**The order is the one the status line requires**: approval at 15:02:58+02:00, canonical execution
six minutes later at 15:08:55+02:00. The review reached the execution but not the approval — its
own § 2 records why, and names the mechanism: *"This is the branch-authority trap, and it caught
me"*, with `refs/heads/orchestrator` carrying objects held nowhere else.

**🔴 And yet Mirror's declared falsifier for MAJOR-3 is NOT discharged.** The falsifier was:

> *MAJOR-3 falls if a canonical object records that `scientist_reading_modes.md`'s status line was
> **superseded** — a `DEC` record, a candidate execution note, or an amended frontmatter on any ref.*

Executed: `git log --all -S` / `-G` over the status string returns only `384f05f`, the commit that
introduced it; and the protocol file is **one blob, `2aae1ca758`, on all 8 refs carrying it**
(measured across all 45). **No object anywhere records the line as superseded, and no ref carries an
amended line.**

So the finding's *character* changes and its *existence* does not: this is a **staleness defect
whose three conditions are each independently evidenced**, not an unresolvable contradiction between
two equally-supported readings. Two of the three evidences are reachable only from a single non-`main`
ref.

- **Candidate repair intent** — **none writable.** No repository source contains an amended status
  line or amended contract clause (measured across all 45 refs). The dispatch forbids authoring one.

- **🔴 Unresolved questions — and Plan is specifically disqualified from two of them:**
  1. **Does satisfaction of a condition, without any record updating the status line, constitute
     binding?** This is exactly the question `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` answered
     `ACTIVATION_NOT_CONFIRMED` for `roles/`, on reasoning (§ RATIONALE 3) that cites **this very
     protocol** as the repository's gloss on the grammar: *"Until then it binds nobody."* Applying
     that decision by analogy to the protocol itself would be a **governance interpretation**, which
     this task prohibits and which H.1 assigns to the operator. **Not answered.**
  2. **Which document is the defective one** — `roles/scientist.md` for over-claiming, or the
     protocol for a stale line? The repair differs completely between the two. **Not chosen.**
  3. Downstream and unresolved: `roles/scientist.md`'s `actor_id_status` block fixes `scientist-a`
     and `scientist-b` `FIXED on canonical execution of CAND-20260818-SCIENTIST-AB-SPEC`. **Actor
     identity is fixed by a document whose binding force is question 1.** Not resolved.
  4. **Plan is the author of both documents.** Under Annex C.2 an author's reading of its own text
     carries no independence. The measurements above are offered as evidence; the reading is not
     Plan's to supply.

### MINOR-3 · 🔴 the transmitted finding is INACCURATE as measured, and the true state is worse

- **Finding reference** — `REV-ROLES-MIRROR-001` § 5, MINOR-3.
- **Finding as transmitted** — *"All three Scientist worktrees — `lettore`, `lettore-b`,
  `lettore-c` — are on refs carrying the superseded blob"* (`e93281159c`).

**Measured this session, over all 45 content refs:**

```
roles/scientist.md, blob distribution
  fd30134dc8   8 refs   main, orchestrator-surface, p5-domain-truth,
                        plan-orchsurf-r4-transcription, scientist-ab-spec, xport, 2 tags
  e93281159c  11 refs   evidence-index, hash-determinism, lettore-c, mirror, orchestrator, …
  ABSENT      22 refs   … including refs/heads/lettore and refs/heads/lettore-b
```

```
$ git ls-tree refs/heads/lettore   roles/     →  (empty)
$ git ls-tree refs/heads/lettore-b roles/     →  (empty)
$ git ls-tree refs/heads/lettore-c roles/     →  4 files, scientist.md = e93281159c

$ git merge-base --is-ancestor a8cd125 refs/heads/lettore     → NO
$ git merge-base --is-ancestor a8cd125 refs/heads/lettore-b   → NO
$ git merge-base --is-ancestor a8cd125 refs/heads/lettore-c   → YES

governance/ file count:  lettore 0 · lettore-b 0 · lettore-c 22
```

**`lettore` and `lettore-b` do not carry a superseded contract. They carry no contract at all, and
no `governance/` either** — both branched before `a8cd125`, the commit that materialized `roles/`.
Only `lettore-c` matches the finding as written.

**Why this matters and is not pedantry.** Body §36.5 instructs an actor to rehydrate from its own
worktree. The transmitted finding describes an actor reading a contract that does not know reading
modes exist. The measured state is that **two of the three Scientist worktrees offer no role
contract and no constitution to rehydrate from at all** — a different failure mode, undetectable by
the check that finds a stale blob, and reached only by distinguishing `ABSENT` from `superseded`.

- **Candidate repair intent** — **none prepared, and none is a contract edit.** No text in
  `roles/scientist.md` is defective on this count. The defect is in ref topology — which branches
  the Scientist worktrees are checked out on — and is outside both the four contracts and this
  task's scope.
- **Unresolved** — whether `lettore` / `lettore-b` are intended to carry governance at all, or are
  deliberately pre-governance reading branches. **Not determined here**; it requires the operator or
  an actor with runtime authority, and this document does not infer intent from topology.
- **Required future review** — MINOR-3 as transmitted should be **re-measured before any repair is
  built on it.** The evidence above is offered to the reviewer, not as a correction of the verdict:
  restating a finding is Mirror's act under C.2, not Plan's.

### INFO · re-run at this HEAD

- Worktrees `{scientist-a: lettore, scientist-b: lettore-b, scientist-c: lettore-c}` match Annex I.2
  step 4 ✅ — the *declaration* matches; § MINOR-3 above measures what those refs actually contain.
- Scientist fingerprint set matches P2.2 (*CORE plus Annex C, Annex E, Annex F*) ✅.

---

## 7 · `roles/mirror.md` — no review performed

**The dispatch instructs: do not self-review; record only the existing observation and the external
review requirement.** Two reasons compound here, and the second is the stronger:

1. Mirror emitted **no verdict** on its own contract (`REV-ROLES-MIRROR-001` § 6), under Annex G.2
   and H.1 (*"Modifica rubrica/metodi di Mirror | mai Mirror da solo"*).
2. 🔴 **Plan is the author of all four contracts** (`REV-ROLES-MIRROR-001` frontmatter:
   `author: plan (materialization a8cd125)`; `materialization_log.md` MAT-003). **A review of
   `roles/mirror.md` by Plan would be an author review, not an independent one** — the same defect
   of independence that bars Mirror, arriving from the other side. Plan cannot supply the
   independent review this contract needs, and does not attempt to here.

### Existing observation — recorded verbatim in substance, not re-verified

From `REV-ROLES-MIRROR-001` § 6, as the reviewer's own measurements:

- byte-identical across all 19 refs carrying it (`6e515059…`); fingerprint set matches P2.2;
  `ROLE_CONTRACT_HASH` recomputed as `43d33b13…fff1` — **independently confirmed at this HEAD**:
  `shasum -a 256 roles/mirror.md` → `43d33b13e52f88c7ccb9b2cacc50b797b57bd7db83885485131bc3459200fff1` ✅
- **its declared blocker is TRUE** (the event ledger has no writer) — the negative control that
  separates it from MAJOR-1, where a declared blocker was refuted by a running tool;
- consequently the *Analysis surface* section, the autonomy ledger and review yield depend wholly on
  a missing Annex J.1 object;
- `L2-OUTCOME-MIRROR-001` row M1 already records a finding against Mirror's own C.2 capability
  (`CRITERION MET · FORMAT NOT UNIFORM`).

### External review requirement — recorded, unassigned

`REV-ROLES-MIRROR-001` § 6 names four items requiring an independent reviewer: the scope of the
self-review bar; whether the G.2 correction route is executable; the fingerprint-recording practice
under A.6; and whether MAJOR-1's pattern (a clause asserting a world-state a tool would refute)
recurs elsewhere in that contract.

🔴 **The route currently has no available executor, measured:** G.2 requires *"an independent
reviewer chosen by Orchestrator"*; there are **0 `ACTIVE` leases by derivation** and therefore no
`ACTIVE_ORCHESTRATOR` to choose one, and **0 `VERIFIED` capabilities in any actor of any role**.
`DEC-20260822` § IMMEDIATE_CONSEQUENCES 4 records the same obstacle for activation generally.

**No reviewer is named, proposed or assigned here.** Assigning one is Orchestrator's act under G.2,
and this document has no authority to perform it.

---

## 8 · SUMMARY — findings consumed, repairs prepared

| Ref | Object | Class | Repair text exists in repository? | Prepared here |
|---|---|---|---|---|
| MAJOR-1 | `roles/plan.md`:73 | MAJOR | ❌ none on any of 45 refs | intent + discharged falsifier; **no clause written** |
| MINOR-1 | `roles/plan.md`:47–48 | MINOR | ❌ none | intent blocked upstream by the H.1 gap |
| — | Annex H.1 row 40 | structural cause | ❌ none | recorded; **authority not assigned** |
| MAJOR-2 | `roles/orchestrator.md` @ `2bbb2141` | MAJOR | ✅ blob `24663eec` on 2 refs, **unapproved** | existing text cited, not endorsed |
| MINOR-2 | `runtime/agent_card_registry.md` | MINOR | ❌ none | recorded, out of contract scope |
| MAJOR-3 | `roles/scientist.md` ↔ protocol | MAJOR | ❌ none | intent + 3 conditions newly evidenced; **not adjudicated** |
| MINOR-3 | Scientist worktree refs | MINOR | n/a — not a contract defect | **finding re-measured; transmitted form inaccurate** |
| — | `roles/mirror.md` | no verdict | n/a | observation + external review requirement only |

**Nothing above is a repair. Every entry is a candidate for one.**

---

## 9 · REQUIRED FUTURE REVIEW

1. **`AUTHOR_RESPONSE` to `REV-ROLES-MIRROR-001` is required and outstanding** (Annex C.2 —
   *"obbligatoria; il silenzio non è accettazione"*). **This document is not it** and does not
   substitute for it. `DEC-20260822` § IMMEDIATE_CONSEQUENCES 5 records the same.
2. **An independent review of `roles/mirror.md`** — suppliable by neither Mirror (self-review) nor
   Plan (authorship). § 7 records that the G.2 route currently has no available executor.
3. **A C.2 review of any repair candidate that follows from this preparation**, at the floor Annex
   C.1 sets for governance (R4, `MIRROR_REQUIRED` per G.1).
4. **Re-measurement of MINOR-3** before any work is built on it (§ 6).
5. **An operator determination on the two questions this document is barred from answering:**
   Annex H.1 row 40's empty Authority cell (§ 4), and whether a satisfied-but-unrecorded condition
   binds `scientist_reading_modes.md` (§ 6).

---

## 10 · WHAT WOULD CHANGE THIS DOCUMENT

- **MAJOR-1's disposition changes** if a capability row is established to mean *"as of
  materialization"* rather than *"as of now"*. Annex I.4 makes the row an input to live assignment,
  which is why that reading is not taken here — but it is available and is not refuted.
- **MAJOR-2's "no repair exists" changes** the moment any `HUMAN_APPROVAL` naming ORCHSURF appears
  on any ref. Re-run: `HUMAN_APPROVAL_QUEUE.jsonl` grep for `ORCHSURF` across all refs.
- **MAJOR-3's shape changes again** if any object is found recording the protocol's status line as
  superseded. Two independent searches (`-S`/`-G` over the string; blob identity across all 8 refs
  carrying the file) found none, but neither exhausts every candidate document's prose.
- **MINOR-3's re-measurement changes** if `lettore` / `lettore-b` are rebased onto a
  governance-bearing lineage, which would convert `ABSENT` into a blob comparison.
- **Everything in § 5's INFO row changes** if the review's un-re-run negative controls are executed
  and disagree. They were not re-run, and that is stated rather than concealed.

---

**Prepared by:** `plan`, worktree `evidence-index`, branch `plan-orchsurf-r4-transcription`,
2026-08-22. Under the operator's dispatch and **not** under the authority of `roles/plan.md`, which
`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` holds non-binding.

**This is a `WORK_COMMIT` on Plan's own branch (Annex D.1). It is not a
`CANONICAL_BATCH_COMMIT`, not an `INTEGRATION_CANDIDATE`, and it advances no canonical surface.**

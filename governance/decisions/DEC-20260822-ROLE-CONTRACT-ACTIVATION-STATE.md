---
record_type: OPERATOR_DECISION
id: DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE
title: Activation state of the four role contracts (STATE_DETERMINATION)
date: 2026-08-22
authority: Operatore — Annex H.1 (governance → Operatore), body §4, §10
status: BINDING_AS_AN_OPERATOR_DETERMINATION_OF_STATE
change_class: STATE_DETERMINATION
change_class_rationale: >
  No frozen governance document is modified. No contract text is edited. No finding is
  resolved. This record determines one fact — whether the existing review and approval
  records constitute activation of the four role contracts — and nothing else.
supersedes: none
applies_to:
  - roles/plan.md
  - roles/orchestrator.md
  - roles/scientist.md
  - roles/mirror.md
task_id: ROLE_CONTRACT_ACTIVATION_STATE_DETERMINATION_v1
mode: READ_ONLY_EVIDENCE_REVIEW → CREATE_DECISION_ARTIFACT_ONLY
---

# ROLE CONTRACT ACTIVATION STATE — DETERMINATION

> **This decision determines activation state only. It does not certify that the contracts
> are internally correct.**

---

## DECISION_ID

`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE`

## TASK_ID

`ROLE_CONTRACT_ACTIVATION_STATE_DETERMINATION_v1`

## QUESTION_DECIDED

Do the existing review and approval records — `REV-GOV311-MIRROR-003` and
`RES-20260816-GOV311-001`, with their related artefacts — constitute **activation** of the four
role contracts, despite all four still declaring:

```
status: PROPOSED — binding once Mirror hostile review passes and the operator approves
```

Two questions were held apart throughout, per the decision principle of the dispatch:

- **QUESTION A — did activation happen?** Decided here.
- **QUESTION B — are the contracts currently correct and internally consistent?** Not decided
  here, and no answer to it is implied by the answer to A.

---

## EVIDENCE_CONSIDERED

Every mechanical fact below was executed or recomputed in this session. Nothing is carried from
a prior report, a handoff or a manifest field.

### E-1 · Role contract status lines — current state

`git grep -n "^status:" main -- roles/` returns four hits, byte-identical in the operative
clause:

| Object | Line | Value |
|---|---|---|
| `roles/mirror.md` | 7 | `PROPOSED — binding once Mirror hostile review passes and the operator approves` |
| `roles/orchestrator.md` | 7 | same |
| `roles/plan.md` | 7 | same |
| `roles/scientist.md` | 12 | same |

### E-2 · The status line has never been modified

`git log --all -S'status: PROPOSED — binding once Mirror hostile review passes and the operator
approves' -- roles/` returns exactly two commits — `a8cd125` (on `main`) and `40ba0b7` (its
pre-rebase twin) — **both the materialization itself**. The string has been *written* twice and
*changed* never.

`git log --all -S'status: ACTIVE' -- roles/` and `-S'status: BINDING' -- roles/` both return
**empty across all refs**. No activated status has ever existed in `roles/` on any branch.

### E-3 · The approval record

`ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` line 3:

```
RESOLUTION_ID: RES-20260816-GOV311-001   STATE: APPROVED   RESOLVED_BY: operator   2026-08-16
APPROVED_OBJECT:
  candidate_id:            CAND-20260816-GOV311
  candidate_content_hash:  c39ecae8…30c239
  base_head:               749a9a9b…557561
DEVIATION_DECISIONS:  PID-09 ACCEPTED · PID-10 ACCEPTED
CARRIED_UNRESOLVED:   ESC-3 (MIRROR_RETROSPECTIVE cadence N)
```

The approval binds to a **candidate content hash at a base head**. It decides two deviations. It
carries one item unresolved. **No field of it names role contract activation, the `status:`
field, or any of the four objects individually.** It carries its own limiting clause:

> `APPROVAL_IS_NOT_AUTHORIZATION`: "Annex D.4 / J.3 (E4). This approval authorises the INTENT. It
> does not authorise execution outside the rules."

`RES-20260816-GOV311-002` (line 5) rules only on GATE 0's lease precondition, explicitly
`SCOPE: … for CAND-20260816-GOV311 only … it does not generalise`.

### E-4 · What the approved object contained

`CAND-20260816-GOV311` declares `BRANCH_TIP 9720a0cd…`. Verified: `git ls-tree 9720a0cd roles/`
lists all four contracts, and `CONTROL_PLANE_ROOTS` (P5.1) excludes only
`governance/candidates/`, `ledger/` and `reviews/` — so `roles/` was **inside** the approved
content domain.

🔴 **The bytes that were approved include the `PROPOSED` line itself.** What the operator
approved on 2026-08-16 was the installation of four documents that say, in their own
frontmatter, that they are not yet binding.

### E-5 · The review record that carries `PASS`

| Review | Scope | Disposition |
|---|---|---|
| `REV-GOV311-MIRROR-001` (`c6a290e1`) | revision 4 | `REVISION_REQUESTED` |
| `REV-GOV311-MIRROR-002` (`2d7c4ab8`) | full content review R-1…R-7 of revision 5 | **`REVISION_REQUESTED`** |
| `REV-GOV311-MIRROR-003` (`84407c1`) | *"delta verification of manifest revision 5.1 — RC-6…RC-10 only. R-1…R-7 NOT repeated"* | `PASS_WITH_NOTES` |

`REV-GOV311-MIRROR-003` § 1 states its own precondition: the narrow scope *"is only legitimate if
nothing in the content moved"* — exactly one file changed since the reviewed head, and it was
control plane. **The `PASS` verifies that the object did not move; it does not review the
object.** `COR-20260816-GOV311-001` exists precisely because this distinction was once collapsed:
`plan` attributed the `PASS_WITH_NOTES` to `-002`, which reads `REVISION_REQUESTED`.

`REV-GOV311-MIRROR-002`'s seven review axes are R-1 candidate identity and binding, R-2 fidelity
of the frozen materialization, R-3 plan implementation decisions, R-4 CLAUDE.md migration, R-5
prior-art design record, R-6 pending implementation, R-7 GATE-3 readiness. `roles/` appears in it
twice, both times as PID-09 — the structural deviation of using one file for three scientists.
**The four contracts' content, internal consistency and enforceability were not an axis of any
GOV311 review.**

### E-6 · The first hostile review of these four objects

`REV-ROLES-MIRROR-001`, committed at `mirror` tip `1350477`, SHA-256
`53b47b248adf6dc449c032435c198ac3eec3daee57ce83e6ec0d5b30e6db62f7`, dated 2026-08-22:

- `supersedes: nothing. First review of these four objects as a set.`
- `roles/plan.md` — **CHANGES_REQUIRED** (C.2: WEAKENED)
- `roles/orchestrator.md` — **CHANGES_REQUIRED** (C.2: WEAKENED)
- `roles/scientist.md` — **CHANGES_REQUIRED** (C.2: WEAKENED)
- `roles/mirror.md` — **no verdict emitted**, self-review prohibition
- § 8 measures both activation conditions as `SATISFIED for CAND-20260816-GOV311`, records the
  status line as `❌ NEVER MODIFIED`, and **declines to resolve**: *"an actor choosing the
  reading that makes its own contract binding would be exactly the convenient interpretation the
  gate exists to prevent."*
- `AUTHOR_RESPONSE`: *"Required and outstanding … this review ratifies nothing."* — outstanding
  at the date of this decision.

### E-7 · The author's own record of what materialization did

`governance/design_records/materialization_log.md`, MAT-003 (`outcome: COMPLETE for §47 step 7
except the fingerprint script; step 8 deliberately not attempted`):

> "All are marked `status: PROPOSED`. They become binding when Mirror's hostile review passes and
> the operator approves — **Plan materializes governance, it does not enact it.**"

The same record classifies the scientist ACTOR_IDs as *"Proposed, not decided"*, confirmed at
registration (I.2 step 7), *"not fixed by a materialization"*.

### E-8 · The repository's own gloss on this status grammar

`framework/protocols/scientist_reading_modes.md` carries the identical construction and spells
out its meaning in the frontmatter:

```
status: PROPOSED — binding on canonical execution of CAND-20260818-SCIENTIST-AB-SPEC, after
  Mirror hostile review and HUMAN_APPROVAL. Until then it binds nobody.
```

### E-9 · The one artefact that reads the records as activation is a held proposal

`governance/candidates/PROPOSAL-C9-STATE-MODEL.md` § 8 classifies *"Seven `status: PROPOSED` on
governed artifacts"* as `TRANSITIONAL × TRACKED`, owner operator, event
`RES-20260816-GOV311-001`; its § 6 worked example rewrites the role status line to
`status: BINDING / status_since_event: RES-20260816-GOV311-001`.

Its frontmatter: `status: ACCEPTED`, `acceptance_is_not_adoption: true`,
`hold: no implementation and no governance modification until that review completes`. Every row
of § 8 is marked `Held? yes`. **That an accepted proposal still has to propose this rewrite is
itself evidence the rewrite has not occurred.**

### E-10 · Activation-adjacent runtime facts, measured

- `python3 framework/scripts/lease_state.py` → **`ACTIVE by derivation: 0`**. Five leases exist,
  all `STALE` or `RELEASED`, the most recent released 2026-08-18T14:05:20Z. Per `CLAUDE.md` § 0,
  a session with no ACTIVE lease is already in `BOOTSTRAP_MODE`.
- No activation artefact of any kind exists: `governance/decisions/` did not exist on `main`
  before this record; the two prior decision records (`DEC-20260820-ORCH-SESSION-HOME`,
  `DEC-20260821-ORCHSURF-D2-TRANSCRIPTION-ROUTING`) are tracked on `evidence-index`, are not on
  `main`, and neither concerns role contract activation.
- No later repair or update to the status lines exists on any of the 41+ refs (E-2).

### E-11 · The three transmitted MAJOR findings — spot-verified, not adjudicated

Verified only to the extent needed to confirm that they were transmitted against real objects.
**No verdict on any of them is rendered here.**

| Finding | What was executed | Result |
|---|---|---|
| MAJOR-1 | `roles/plan.md:73` reads `Fingerprint composition … blocked: the composition is prose, not a script` / `UNVERIFIED`; then `python3 governance/scripts/governance_fingerprint.py compose --all` | The tool ran and emitted four fingerprints. The two statements are inconsistent as they stand. |
| MAJOR-2 | `roles/orchestrator.md` frontmatter line 5 `worktree: the repository root checkout`; line 46 *"Orchestrator must not: commit its own work"*; line 89 requires `WORK_COMMIT` | The three clauses are present and in tension. `DEC-20260820-ORCH-SESSION-HOME` (evidence-index, not on `main`) addresses adjacent subject matter. |
| MAJOR-3 | `roles/scientist.md` frontmatter cites `scientist_reading_modes.md § 1.1` as the basis for `FIXED` identities; that protocol's own frontmatter reads *"Until then it binds nobody"* | Both texts are as described. |

---

## OPTION_SELECTED

### 🔴 **OPTION B — `ACTIVATION_NOT_CONFIRMED`**

The existing records do **not** constitute activation of the four role contracts. The contracts
remain `PROPOSED`.

---

## RATIONALE

**1 · The approval and the contracts are bound to different objects.**
`RES-20260816-GOV311-001` approves a candidate identified by a content hash at a base head. The
role contracts are *inside* that hash, so what the approval reaches is their **installation, at
the byte level** — and those bytes say the documents are not yet binding (E-4). An approval bound
to a hash approves the bytes under that hash; it cannot simultaneously nullify the meaning of one
of them. Reading the approval as self-executing would mean any normative document activates at
the instant it is committed, which empties the `status:` field of content for every future
artefact.

**2 · The review that passed is not a review of these objects.**
`REV-GOV311-MIRROR-003` is a delta verification of manifest fields RC-6…RC-10, legitimate — by
its own § 1 — precisely *because no content path moved*. The full content review,
`REV-GOV311-MIRROR-002`, reads `REVISION_REQUESTED`, and neither examined the contracts' internal
consistency or enforceability (E-5). The condition *"Mirror hostile review passes"* has been
tested against these four objects exactly once, on 2026-08-22, and it returned
**CHANGES_REQUIRED on three contracts with no verdict on the fourth** (E-6). Against the objects
the clause actually names, the condition is not satisfied — it is failed on three and untested on
one.

**3 · The repository already defines what this status grammar means.**
`scientist_reading_modes.md` carries the identical construction and glosses it: *"Until then it
binds nobody"* (E-8). Reading the same grammar as self-executing in `roles/` and as
binding-nobody in `framework/protocols/` would give one status vocabulary two incompatible
meanings, decided by which reading is convenient at the moment of reading.

**4 · The author of the objects recorded the opposite intent.**
MAT-003: *"Plan materializes governance, it does not enact it"* (E-7). The record is
contemporaneous with the materialization and was itself inside the approved content.

**5 · Nothing anywhere records an activation.**
The status line has been written twice and changed never, across all refs; `ACTIVE` and `BINDING`
have never appeared in `roles/` (E-2). No activation artefact exists (E-10). The only text that
reads the approval as an activation event is a proposal that is explicitly accepted-but-not-
adopted and held (E-9).

**6 · Doubt resolves closed, and the doubt is not mine to resolve conveniently.**
Mirror declined to resolve this on the ground that an actor choosing the reading that makes its
own contract binding is exactly what the gate prevents, and referred it to the operator under
H.1 (E-6). H.1 is where this record sits. Where the two readings are genuinely available, the
system's own discipline resolves fail-closed. The cost of that choice is measurably near zero
today: there are **0 ACTIVE leases**, so no session is executing under assumed contract authority
at this moment (E-10).

**7 · The counter-argument, stated and weighed.**
The strongest case for OPTION A is that both named conditions did literally occur on
2026-08-16 for a candidate that carried these files, that the contracts are canonically installed
on `main`, and that the laboratory has in fact operated for six days with actors, worktrees,
reviews, candidates and leases. That is real, and this decision does not deny it. But it
establishes **practice**, not **activation**: the leases derive from Annex I.3, the reviews from
Annex C, the candidates from Annex D — all installed and binding by the same approval,
independently of `roles/`. None of that operation required the four contracts to have shed
`PROPOSED`, and none of it recorded that they had.

---

## SCOPE_LIMITATION

**This decision determines activation state only. It does not certify that the contracts are
internally correct.**

Specifically, this record:

- decides **QUESTION A** (did activation happen) and **only** QUESTION A;
- renders **no verdict** on MAJOR-1, MAJOR-2 or MAJOR-3, and the spot-verification in E-11 is
  evidence that the findings were transmitted against real objects, **not** an adjudication of
  them;
- ratifies **no** contract text, in whole or in part;
- amends **no** frozen governance document, and adopts **no** general interpretation of Annex D,
  Annex C or Annex H;
- **does not** invalidate, void or reopen work already performed by any actor between
  2026-08-16 and this date. Practice under Annexes C, D, G, I and J is unaffected: those
  instruments were installed and bind on their own terms, not through `roles/`;
- is a determination of **state**, not a permission, an assignment or a capability.

---

## IMMEDIATE_CONSEQUENCES

1. **The four contracts remain `PROPOSED`.** `roles/plan.md`, `roles/orchestrator.md`,
   `roles/scientist.md` and `roles/mirror.md` are, as of this record, non-binding documents. Their
   `status:` lines are **accurate**, not stale.
2. **No actor authority may be assumed from these contracts.** Any authority an actor exercises
   must be traced to the governance body or to a named annex — H.1 for the authority matrix, D
   for the commit path, C for the review ladder, I.3 for the lease — never to a role contract
   clause standing alone.
3. **A new, explicit activation act is required** before any actor relies on these contracts as
   binding. This record does not perform it, does not schedule it, and does not specify its form.
4. **The activation condition, as written, now has a measured obstacle.** The clause names a
   passing Mirror hostile review; the only hostile review of these objects returned
   CHANGES_REQUIRED on three of four, and `roles/mirror.md` cannot be reviewed by its own actor.
   Whoever prepares an activation act inherits both facts. Neither is resolved here.
5. **`REV-ROLES-MIRROR-001`'s `AUTHOR_RESPONSE` remains required and outstanding** (Annex C.2:
   silence is not acceptance). This record is not that response, and does not substitute for it.
6. **Domain note.** `governance/decisions/` is **not** a declared `CONTROL_PLANE_ROOT` (P5.1
   lists `governance/candidates/`, `ledger/`, `reviews/`). This record is therefore in the
   **content domain** and will be inside the `CANDIDATE_CONTENT_HASH` of every future candidate,
   and this commit advances `main`. No open candidate declares the pre-commit `main` tip
   `04693e68` as its `BASE_HEAD` — the most recent is `4454feab` (`CAND-20260819-XPORT`), already
   behind — so no candidate's base condition is invalidated by this commit; any candidate
   re-aligning onto `main` will include this record in its domain.

---

## OUT_OF_SCOPE

Explicitly not done, not authorized and not implied by this record:

- editing `roles/` — no file under it was touched;
- editing `governance/` outside this new `decisions/` record;
- modifying any contract text, status line or frontmatter field;
- resolving, repairing, downgrading or dismissing MAJOR-1, MAJOR-2 or MAJOR-3;
- assigning ownership of any finding, repair or follow-up;
- creating, declaring or verifying any capability;
- approving any contract correction, candidate or proposal;
- ratifying `PROPOSAL-C9-STATE-MODEL`, adopting its four-field status form, or lifting its hold;
- performing, scheduling or specifying the activation act named in consequence 3;
- any redesign of the governance, the authority matrix or the activation mechanism.

---

## VERIFICATION TRAIL

| Check | Command | Result |
|---|---|---|
| Status lines, current | `git grep -n "^status:" main -- roles/` | 4 × `PROPOSED …` |
| Status line ever changed | `git log --all -S'status: PROPOSED — binding once…' -- roles/` | `a8cd125`, `40ba0b7` — materialization only |
| Activated status ever present | `git log --all -S'status: ACTIVE' -- roles/` · `-S'status: BINDING'` | empty, both |
| Approval record | `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl`, parsed | 6 lines; RES-…-001 APPROVED, bound to hash + base |
| Roles inside approved domain | `git ls-tree 9720a0cd roles/` | 4 files present |
| Control-plane roots | `governance/plan_defined_parameters.md` § P5.1 | `governance/candidates/`, `ledger/`, `reviews/` |
| Lease state | `python3 framework/scripts/lease_state.py` | `ACTIVE by derivation: 0` |
| Fingerprint tool | `python3 governance/scripts/governance_fingerprint.py compose --all` | 4 fingerprints emitted |
| Roles review anchor | `git log --all --oneline -- reviews/mirror/REV-ROLES-MIRROR-001.md` | `1350477`, SHA-256 `53b47b24…62f7` |

---

**Recorded by:** operator, root checkout, `main`, 2026-08-22.
**This is not a `WORK_COMMIT` and not a `CANONICAL_BATCH_COMMIT`.** It is an operator
determination under H.1, touching one new path under `governance/decisions/` and nothing else.

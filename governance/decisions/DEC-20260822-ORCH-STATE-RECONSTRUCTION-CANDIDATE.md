---
record_type: OPERATOR_DECISION
id: DEC-20260822-ORCH-STATE-RECONSTRUCTION-CANDIDATE
title: Candidate status of PROPOSAL-ORCH-STATE-RECONSTRUCTION (STATUS_DETERMINATION)
date: 2026-08-22
authority: Operatore — Annex H.1 rows `Spese / MAJOR approval / governance` and
  `Strategia complessiva`; body §4, §10. Not taken from any role contract.
status: BINDING_AS_AN_OPERATOR_DETERMINATION_OF_CANDIDATE_STATUS
change_class: STATUS_DETERMINATION
change_class_rationale: >
  No frozen governance document is modified. The candidate text is not edited. No finding is
  resolved, adopted or dismissed. This record determines one fact — the status of one
  architectural proposal candidate — and authorizes nothing.
supersedes: none
applies_to:
  - governance/candidates/PROPOSAL-ORCH-STATE-RECONSTRUCTION.md @ orch-state-reconstruction
task_id: OPERATOR_DECISION_ORCH_STATE_RECONSTRUCTION_CANDIDATE_v1
mode: READ_ONLY_ANALYSIS → CREATE_DECISION_RECORD_ONLY
authority_note: >
  The four role contracts are PROPOSED. Per DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE
  consequence 2, no authority is read from them here — not the author's, not the reviewer's,
  and not the operator's.
---

# ORCH-STATE-RECONSTRUCTION — CANDIDATE STATUS DETERMINATION

> **This decision determines candidate status only.** It does not adopt the proposal, does not
> authorize implementation, and does not certify that the shape the proposal describes is the
> right one.

---

## DECISION_ID

`DEC-20260822-ORCH-STATE-RECONSTRUCTION-CANDIDATE`

## TASK_ID

`OPERATOR_DECISION_ORCH_STATE_RECONSTRUCTION_CANDIDATE_v1`

---

## OBJECT

The object under decision is addressed as `(ref, path, blob)` rather than by path alone —
applying the proposal's own § 2.1 observation to the record that decides its status.

| Field | Value |
|---|---|
| path | `governance/candidates/PROPOSAL-ORCH-STATE-RECONSTRUCTION.md` |
| ref | `orch-state-reconstruction` |
| revision (tip) | `f1074aab2ca1f4efaa451e13a78cf52993f310c3` |
| blob oid | `e6af7e3d9383f4ae7d5210f81af5610bd15e62e7` |
| sha-256 of content | `f491d5247dc1cfffbee3aae66eb646e3114d764e9f18930f9082c34a3ea072ba` |
| declared `base_head` | `2bb270050d76264a13c8d595bc585ccde3b09ff3` |
| author | `orchestrator` |
| declared status | `PROPOSED`, `normative: no`, `authority: none` |

**Review evidence:**

| Field | Value |
|---|---|
| path | `reviews/mirror/REV-ORCH-STATE-RECONSTRUCTION-001.md` |
| ref | `mirror` |
| revision (tip) | `1892071e86f6616400bc6e306f70cd192c479456` |
| blob oid | `16322c97ad72c638b50f0cee41a28449155a3bb7` |
| sha-256 of content | `d7a535012a353878fc1f8ab238dff7c7a9c2bcbf63c49f35de0d90d293718574` |
| level | R4 · METHOD (Mirror), Annex C.2 |
| verdict | `CONFIRMED`, with `WEAKENED: F-7` and `REFINED: F-8` |

The review's § A declares `HEAD 13504778b0814f79a912f62f544c23eab6971f9d`. That is the
**pre-commit surface** it measured from, and it is the parent of the commit carrying the review
(`git rev-parse 1892071^` returns exactly it). This was checked rather than assumed, because a
declared HEAD that does not match the ref tip is otherwise indistinguishable from a stale
measurement. It is regular practice, not a defect.

---

## IDENTITY AND AUTHORITY

| Field | Value | How established |
|---|---|---|
| deciding role | `operator` | dispatch; authority traced below, not to a contract |
| checkout | `<REPO_ROOT>` (root) | `git worktree list` |
| branch at analysis | `main` | `git rev-parse --abbrev-ref HEAD` |
| HEAD at analysis | `2bb270050d76264a13c8d595bc585ccde3b09ff3` | `git rev-parse HEAD` |
| working tree at analysis | clean | `git status --porcelain` returned empty |
| branch this record is written on | `operator-decision-orch-state-reconstruction`, based on `main` | `git worktree add -b … main` |

**Authority derivation.** H.1 has **17 rows** (counted in this session). Two name the Operatore:
`Spese / MAJOR approval / governance` and `Strategia complessiva`. Determining whether an
architectural proposal proceeds is a governance decision, and it falls in the first of those.

🔴 **No authority here is taken from a role contract.** All four are `PROPOSED`, and
`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` consequence 2 forbids reading actor authority from
them. That bar was applied to the author (`roles/orchestrator.md`), to the reviewer
(`roles/mirror.md`), and to this record.

**Adjudication.** The review's § D-3 records that H.1 gives `Aggiudicazione challenge` to the
Orchestrator, who is the **author** of the object, and that C.3 requires
`AUTHOR ≠ REVIEWER ≠ ADJUDICATOR`. Adjudication therefore escalated to the operator. This record
is the operator acting in that seat, and it adjudicates **status only** — no finding.

---

## SURFACE MAP

```
MEASURED_AT          ref    main
                     HEAD   2bb270050d76264a13c8d595bc585ccde3b09ff3
                     date   2026-08-22, this session
                     tree   clean (git status --porcelain empty)

REFS SURVEYED        47 total — 33 refs/heads · 5 refs/tags · 4 refs/remotes · 1 refs/stash
                     Repository-wide sweeps iterate heads + tags + remotes = 42 refs.
WORKTREES            15

VALIDITY             Every absence claim in this record is REPOSITORY-WIDE over the 42 refs
                     enumerated above, and over no wider surface. NOT_FOUND on 42 refs is not
                     NOT_EXIST: clones, unpushed worktrees and unreferenced objects lie
                     outside it. Claims scoped to main alone are labelled LOCAL.
```

This surface is **identical in count** to the one the review declared (47 refs / 15 worktrees),
and `main` has not moved from the `base_head` the proposal declared. Review falsifier 4 — *"a
merge making `main` a superset of the seven § 1.1 objects"* — **has not occurred**, so the
review's finding of architectural necessity stands unwithdrawn.

---

## EVIDENCE_CONSIDERED

Only two artifacts were used as evidence: the proposal and the Mirror C.2 review. **Every
load-bearing claim in both was re-executed in this session rather than read from the report.**
Results below are this session's, not transcriptions.

| Claim | Source | Re-measured result |
|---|---|---|
| Seven objects absent from `main`, each on a named ref | proposal § 1.1 / F-1 | **7 of 7 reproduce**, ref sets identical |
| `ledger/events/` exists on no ref | proposal § 2.4 / F-2 | **0 of 42 refs**; `ledger/` on `main` = `approvals`, `checkpoints`, `retirements`, `tasks` |
| `ACTIVE by derivation: 0`, with two findings on lease #3 | proposal § 1.3 / F-3 | reproduced verbatim — 5 records, `DISAGREEMENT` (`stored=EXPIRED`, `derived=STALE`) and `EXPIRED_WITHOUT_RENEWAL` |
| H.1 = 17 rows; Orchestrator in 5 authority cells + 1 as target | proposal § 5.1 / F-5 | **17 / 5 / 6** — exact |
| C-9 is `ACCEPTED`, `acceptance_is_not_adoption: true`, held | F-13 | reproduced on `main` |
| `DEC-20260822` decides OPTION B, `ACTIVATION_NOT_CONFIRMED` | F-4 | reproduced on `main` |
| F-7 — `HANDOFF-GOV311-ORCHESTRATOR` carries ref-bearing keys | review F-7 | **confirmed**: `source_branch`, `base_head`, `candidate_content_hash` are structured frontmatter keys, not prose |
| F-8 — handoff count 14 by filename, 15 by path | review F-8 | **confirmed exactly**: 15 by path substring, 14 by filename; the 15th is `runtime/handoff/C-2/PMID42422765.working.lettore-and-lettore-b.json` |
| `AUTHOR_RESPONSE` to the review exists | review § K | **absent on all 42 refs** — five `AUTHOR-RESPONSE-*` files exist, none for this review |

🔴 **One measurement error of my own, recorded rather than silently corrected.** My first attempt
to count H.1's rows anchored on `/^## H\.1/` when the heading is `### H.1`, and returned **0
rows**. A zero that would have been dramatic was an artifact of my query. Re-measured against the
correct heading level, the count is 17. This is the third instance in this review chain of the
same failure class — the proposal's `\b` regex (§ 0), the reviewer's working-directory sweep
(§ C-3), and now mine — which is itself corroborating evidence for the proposal's § 1.4.

---

## KEY_FINDINGS_CONSIDERED

### 1 · Repository state is distributed across refs and worktrees

**CONFIRMED, and reproduced a fourth time by this decision.** 33 branches, 15 worktrees, 47 refs.
All seven objects in proposal § 1.1 are absent from `main` and reachable from exactly one or two
other branches. `runtime/agent_card_registry.md` — the record of which actors exist and what they
may do — lives on `orchestrator` alone and has never been merged.

🔴 **The failure recurred inside this decision.** Neither evidence artifact is readable from the
ref the operator was standing on: the proposal is on `orch-state-reconstruction` only, the review
on `mirror` only, and `main` carries neither. Both had to be read cross-ref by `git show`. The
author met this failure while writing (§ 0), the reviewer met it while reviewing (§ C-2), and the
operator met it while deciding. **Three independent actors, three independent encounters, one
mechanism.**

### 2 · Object identity requires ref / path / revision context

**CONFIRMED.** A path alone does not address an object in this repository; a branch name is
mutable and addresses a location, not a state. This record therefore identifies both evidence
artifacts by `(ref, path, blob oid, sha-256)` above.

**F-7 is accepted as WEAKENED, and it improves the position rather than damaging it.** The
proposal argued from its weakest example — `BRANCH` carried in prose — while
`HANDOFF-GOV311-ORCHESTRATOR`, on `main`, already carries `source_branch`, `base_head` **and**
`candidate_content_hash` as structured keys. The literal claim survives (B.2 specifies no schema,
so no field is *required* of any handoff), but the repository has a precedent the proposal did not
find. **Any future work on this question starts from that precedent, not from a blank page.**

### 3 · State reconstruction solves an observed coordination problem

**CONFIRMED.** The problem is measured, recurrent, and not recalled. The review's assessment that
the loop *"is not blocked by authority … it is blocked by addressing"* is supported: H.1 allocates
every edge of `Orchestrator → Plan → Mirror → Scientist` without gap or overlap, while every
return edge in that loop is a cross-ref read that no dispatch record carries the ref for.

**That a problem is real is not authorization to build a solution for it.** It establishes that
the candidate is worth preserving, which is what this decision does.

### 4 · The proposal must not become hidden governance authority

**RISK ACCEPTED AS REAL, AND IT IS THE DECIDING CONSIDERATION.**

The proposal does not create Orchestrator governance authority: it is `normative: no`,
`authority: none`, one file under a declared `CONTROL_PLANE_ROOT`, and it disqualifies itself
under its own § 3 (*"a dispatch that cited this file as authority would fail
`AUTHORITY_EXISTS`"*).

🔴 **The risk is not in the text; it is in use.** Review F-10 names a third path that is neither
gate nor advisory: a check never formally adopted, but consulted at every dispatch until
*"reconstruction says BLOCKED"* becomes the operative reason a task does not proceed. **That is a
gate with no adoption record**, accreting authority through practice rather than through a clause.
No reading of a document can foreclose it, and nothing currently in the repository closes it.

**Q-1 — gate, advisory, or report — is the operator's row, and this record does not resolve it.**
Resolving it is a separate governed act on a separate dispatch. Authorizing design work on the
check *before* Q-1 is resolved is the precise sequence F-10 warns against.

### 5 · Relationship with PROPOSAL-C9 remains unresolved

**CONFIRMED, and unresolved here.** C-9 is on `main` with `status: ACCEPTED`,
`acceptance_is_not_adoption: true`, and an explicit hold. Review F-13 measures the overlap as
*near-neighbours, not duplicates* — two fail-closed resolution contracts over a declared durable
location — and records that C-9 § 5.1 already answers a large part of the proposal's Q-4.

The review's warning is adopted as a constraint: **resolving either without the other would create
the divergence both are trying to prevent.** Sequencing them is `Integrazione strutturale`, which
H.1 gives to Plan, subject to review. **This record does not sequence them and does not assign
that work.**

### 6 · Ledger depends on a clearer state / event model

**CONFIRMED, and it is the load-bearing absence.** J.2 defines `Ogni transizione = evento (J.1) +
roster durevole`. `ledger/events/` exists on 0 of 42 refs. Every transition this repository has
performed was performed without the event half of its own definition, and J.0's compensator for
absent runtime RBAC — *"authority matrix testuale + audit + event ledger"* — is a three-part
compensator whose third part does not exist.

Consequently a reconstruction built today would derive from git state alone, which shows what an
object **is** and never what an actor **intended** or **closed**. The proposal concedes this
(§ 5.3) and predicts it would return `BLOCKED` on nearly every dispatch. **A design phase would be
designing against a state model whose event half is still absent.**

---

## OPTION_SELECTED

```
OPTION B — HELD_AS_CANDIDATE
```

**The proposal remains a valid candidate. No further work is authorized.**

Options A and C were both available and both declined:

- **OPTION A — REJECTED: declined.** The verdict is `CONFIRMED`, the diagnosed problem is real and
  has now been reproduced by four independent actors, and the candidate refuses authority rather
  than seeking it. Rejecting it would discard a measured diagnosis and would have to be justified
  by evidence that does not exist.
- **OPTION C — AUTHORIZE_NEXT_DESIGN_PHASE: declined.** Reasons in RATIONALE below.

---

## DECISION_STATUS

```
DECISION_STATUS: BINDING_AS_AN_OPERATOR_DETERMINATION_OF_CANDIDATE_STATUS
```

Binding as to **status**. It is not an adoption, not a ratification of the review, and not a
resolution of any finding.

---

## RATIONALE

**1 · `CONFIRMED` means no defect detected, not "adopt".** C.2 defines `CONFIRMED` as *"nessun
difetto rilevato dato l'evidence bundle disponibile"*. The review says so itself and states that
its verdict *"does not make the object citable as authority"*. Validity as a candidate is exactly
what a `CONFIRMED` verdict establishes, and Option B is exactly what that verdict supports.

**2 · A mandatory step of the review protocol is outstanding.** C.2 requires
`AUTHOR_RESPONSE (obbligatoria; il silenzio non è accettazione)`. The review records it as
`REQUIRED AND OUTSTANDING`, owed on F-7 and F-8, and states that **the review ratifies nothing
until it is written**. I verified independently that no `AUTHOR_RESPONSE` to this review exists on
any of the 42 refs. Authorizing a design phase on a review whose author response is unwritten
would read silence as acceptance — which C.2 forbids in those words.

**3 · The verdict explicitly does not cover the one question about scope.** F-9 — whether § 3's
`REVIEW_REQUIREMENTS_MET` displaces Mirror's `Epistemic / method review` row — is **observation
only, carrying no verdict**, because G.2 bars Mirror from adjudicating the scope of its own
function. The review states *"This verdict does not cover it. An independent reviewer must,"* and
lists such a finding as one that **should override § H**. A design phase authorized now would be
designing a check whose boundary against the reviewer's own function is unadjudicated by anyone.

**4 · Two of the three prerequisites the review itself names are unmet.** Its § I
`EVIDENCE_NEEDED` lists four items. Three bear directly on any design work: an independent verdict
on F-9; Plan's determination on Q-2, taking F-7's precedent as the starting point; and **the
operator's resolution of Q-1 *before* any § 3 check is consulted in practice.** None has occurred.
Deciding ahead of evidence the review has already enumerated as needed would repeat the failure
class the whole chain is about.

**5 · The Q-1 fork is a one-way door, and sequence matters.** Q-1 is the operator's to resolve, and
this dispatch is a status determination, not a Q-1 dispatch. Authorizing design of the check while
its normative character is undetermined is the shortest route to F-10's drift path: a gate with no
adoption record. **Holding the candidate keeps that door closed; authorizing design opens it
before anyone has decided which way it swings.**

**6 · The C-9 collision is unresolved and would be aggravated by unilateral advance.** Both
documents are held. Advancing this one alone risks two fail-closed resolvers, two vocabularies and
two locations — the divergence both are trying to prevent (F-13). Sequencing is Plan's row and is
not performed here.

**7 · What Option B costs, stated plainly.** It leaves the addressing problem unfixed, and the
laboratory continues to pay the cross-ref cost that this very decision paid. That cost is real and
is not minimised. It is accepted because the alternative — authorizing design work while a
mandatory protocol step is outstanding, the scope question is unadjudicated, and the normative
fork is undecided — would purchase progress with exactly the discipline the candidate exists to
defend.

**8 · Option B is not rejection and forecloses nothing.** The candidate stays valid and citable as
a candidate. When the `AUTHOR_RESPONSE` is written, F-9 independently reviewed, Q-1 resolved and
the C-9 relationship sequenced, a later operator decision may move to Option C on that evidence.
**This record is a hold, not a verdict on the idea.**

---

## BOUNDARIES

This decision explicitly **does not**:

- **adopt the proposal as canonical** — it is not promoted, merged, ratified, or made citable as
  authority; its own § 3 `AUTHORITY_EXISTS` disqualification stands unchanged;
- **authorize implementation** — no runtime component, no ledger writer, no script, no schema, no
  field, no check, and no gate is authorized, specified or scheduled;
- **create authority** — no actor gains any permission; no role contract is activated, amended or
  read as binding; `DEC-20260822` consequence 2 remains in force;
- **resolve H.1 gaps** — Q-7 (*"may actor X act on object Y"*) is recorded as measured and
  **unamended**; H.1 is `[MAJOR]` and FROZEN and is untouched;
- **resolve the C-9 relationship** — Q-10 stays open; neither proposal is adopted, merged,
  sequenced or released from hold;
- **resolve Q-1** (gate / advisory / report), **Q-2** (object identity), **Q-3**, **Q-4**, **Q-5**,
  **Q-6** (a schema for B.2 `HANDOFF`), **Q-8** (C-7), or **Q-9**;
- **ratify the review**, resolve F-7, F-8, F-9, F-10, F-11, F-12 or F-13, or discharge the
  outstanding `AUTHOR_RESPONSE`;
- **assign ownership** of any finding, repair, follow-up or open question;
- **merge any branch**, modify any candidate, role, annex, ledger, framework or runtime file.

Additionally, and by the same discipline the object is judged under:

🔴 **This record is itself an eighth fragmented object.** It is written on
`operator-decision-orch-state-reconstruction`, based on `main` but not on it, because this task's
validation requires `main` unchanged. A reader standing on `main` will not find it. That is the
proposal's § 1.1 thesis applied to the decision about the proposal, and it is recorded here rather
than left for a later reader to discover.

---

## NEXT_ALLOWED_ACTION

```
NEXT_ALLOWED_ACTION: none — no work is authorized by this record.
```

Option B authorizes **no** next action. The candidate is held where it is.

**Not authorized, and named so they are not mistaken for authorized:** no design phase, no
specification work, no prototype, no writer, no adoption of any § 3 check or § 4 field, and no
consultation of any § 3 check at a real dispatch. Per F-10, **consulting the check in practice
before Q-1 is resolved would itself be the drift this decision holds the line against.**

**What may occur without this record authorizing it** — each already available to its holder under
existing governance, listed so the hold is not misread as a freeze on the laboratory:

- the author's `AUTHOR_RESPONSE` on F-7 and F-8, which C.2 already makes **obligatory** and which
  this record neither grants nor schedules;
- any actor's `WORK_COMMIT` on its own branch, which H.1 gives to *"ogni attore"*;
- the operator's resolution of Q-1, on a separate dispatch;
- an independent review of F-9, opened through the governing path;
- Plan's determination on Q-2 and on C-9 sequencing, being that role's row, subject to review.

A move to Option C requires a **new operator decision**, taken on the evidence named in RATIONALE
§ 4 once it exists.

---

## VERIFICATION TRAIL

Every command below was executed in this session, in the root checkout at `main` @ `2bb2700`.

| Check | Command | Result |
|---|---|---|
| Identity — branch / HEAD / tree | `git rev-parse --abbrev-ref HEAD`; `git rev-parse HEAD`; `git status --porcelain` | `main`; `2bb2700…`; empty |
| `main` still at declared `base_head` | `git rev-parse main` | `2bb270050d76264a13c8d595bc585ccde3b09ff3` — matches; falsifier 4 not triggered |
| Object absent from `main` | `git cat-file -e main:governance/candidates/PROPOSAL-ORCH-STATE-RECONSTRUCTION.md` | `fatal: path … does not exist in 'main'` |
| Object located | iterate `refs/heads` + `refs/remotes`, `git ls-tree -r` | `orch-state-reconstruction` only |
| Review located | same sweep | `mirror` only |
| Immutable identifiers | `git rev-parse <ref>:<path>`; `git cat-file blob … \| shasum -a 256` | blobs `e6af7e3d…`, `16322c97…`; sha-256 `f491d524…`, `d7a53501…` |
| Review's declared HEAD is its parent | `git rev-parse 1892071^` | `13504778…` — matches § A |
| § 1.1 fragmentation | `git cat-file -e` on 7 paths × `main` + 33 heads | **7/7 absent from `main`**, ref sets as claimed |
| Event ledger | `git ls-tree -r <ref> \| grep '^ledger/events/'` over 42 refs | **0 refs**; `ledger/` = `approvals`, `checkpoints`, `retirements`, `tasks` |
| Lease state | `python3 framework/scripts/lease_state.py --check` | `ACTIVE by derivation: 0`; lease #3 `DISAGREEMENT` + `EXPIRED_WITHOUT_RENEWAL` |
| H.1 row count | `awk '/^### H\.1/,/^### H\.2/'` over the annex | **17 rows**; Orchestrator in 5 authority cells, 6 rows naming it |
| C-9 status | `git show main:governance/candidates/PROPOSAL-C9-STATE-MODEL.md` | `ACCEPTED`, `acceptance_is_not_adoption: true`, held |
| Prior decision | `git show main:governance/decisions/DEC-20260822-…` | `BINDING_AS_AN_OPERATOR_DETERMINATION_OF_STATE`, OPTION B |
| F-7 precedent | frontmatter keys of `HANDOFF-GOV311-ORCHESTRATOR` | `source_branch`, `base_head`, `candidate_content_hash` present as keys |
| F-8 counting rule | handoff paths over heads + tags, both rules | **15 by path, 14 by filename** — matches the refinement |
| `AUTHOR_RESPONSE` exists | sweep for `AUTHOR-RESPONSE` across all refs | 5 files, **none for this review** |
| Surface counts | `git for-each-ref`; `git worktree list` | 47 refs (33 heads · 5 tags · 4 remotes · 1 stash); 15 worktrees |

---

**Recorded by:** operator, worktree `wt-dec-orch-recon`, branch
`operator-decision-orch-state-reconstruction`, based on `main` @ `2bb2700`, 2026-08-22.

**This is not a `WORK_COMMIT` on another actor's branch, not a `CANONICAL_BATCH_COMMIT`, and not a
merge.** It is an operator determination under H.1 creating one new path under
`governance/decisions/` and touching nothing else.

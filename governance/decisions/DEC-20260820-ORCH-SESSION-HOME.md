---
record_type: OPERATOR_DECISION
id: DEC-20260820-ORCH-SESSION-HOME
title: Orchestrator session home — operator architectural intent (CONFIRMATION)
date: 2026-08-20
authority: Operatore
status: RECEIVED — NOT RATIFIED. `ratified_by` is empty, and §6 of the record states it has no
  effect until the operator ratifies it. Registered here so that it is citable and so that the
  work it authorizes can be prepared against a durable object rather than against a prompt
change_class: NONE
supersedes: none
applies_to:
  - CAND-20260819-ORCHSURF (all revisions)
  - any future candidate touching Orchestrator surfaces, bootstrap, or promotion
drafted_by: external advisory (Claude/Fable), at operator request
ratified_by: ""
registered_by: plan
registered_on: 2026-08-20
registered_at_branch: orchestrator-surface
convention_note: >
  This repository has NO existing decision-record convention. `governance/decisions/` did not
  exist before this file, and no `DEC-*` artifact existed anywhere in the tree — verified by
  enumeration. The record's §6 instructs Plan to "register it according to decision-record
  conventions"; the convention it names is absent, so this registration PROPOSES one rather
  than applying one. The earlier operator ratification the repository refers to as
  `DECISION 3` exists only as prose inside other documents
  (`deployment/deployment_profile.md` §"DECISION 3 sunset", `CAND-20260818-SUNSET-DEC3`),
  never as a record of its own. That is the gap this directory is opened to close, and opening
  it is itself a proposal subject to review.
---

# `DEC-20260820-ORCH-SESSION-HOME` — as received

**Plan has added nothing to the text below and removed nothing from it.** The record is
reproduced verbatim as transmitted by the operator on 2026-08-20. Everything Plan has to say
about it lives outside this file, in
[`PREP-20260820-ORCHSURF-REV4.md`](../candidates/PREP-20260820-ORCHSURF-REV4.md), so that this
file stays a faithful copy of an operator act and does not become a Plan document over time.

---

## 1. Decision

The Human Operator states, as explicit architectural intent — not as a legacy arrangement to be
corrected:

1. Orchestrator session home = repository ROOT (`legend-public`).

The Orchestrator chat/session is intentionally opened at the repository root. This is the
intended model going forward.

2. The dedicated `orchestrator` worktree is the actor's technical surface — WORK_COMMIT, scratch,
intermediate work.

It is NOT the chat/session home and must not be documented as such.

3. SESSION_LOCATION and PERSISTENCE_SURFACE are independent dimensions.

The location where an actor session is opened does not determine:
- ACTOR_ID;
- write authority;
- canonical persistence surface.

`cwd = root` is not an ACTOR_ID oracle and not a write-authority oracle.

4. Canonical writes on root/main remain separately gated.

Canonical writes occur exclusively within the batch window under lease + GATE 0–5.

A root-resident session holds no standing write authority.

The Orchestrator may inspect and coordinate from root, but any non-batch modification intended
for persistence MUST occur on its assigned worktree surface.

The distinction is:

| Action | Root | orchestrator worktree |
|---|---|---|
| Open session | yes | no |
| Coordinate / observe | yes | yes |
| Read repository | yes | yes |
| Write intermediate work | no | yes |
| Canonical commit on main | batch only | no |

5. Mechanical enforcement of this separation is a separate deferred candidate:
CAND-20260820-ROOTGUARD-001.

ROOTGUARD is explicitly OUT OF SCOPE for ORCHSURF.

## 2. Provenance and precedence effect

This record is a CONFIRMATION of existing FROZEN governance, not a governance change.

Body `GOVERNANCE_v3.1.1.md` §0.2, §0.4, §47 steps 10 and 14, and Annex I.2 already encode the
root-promotion architecture at the top of the precedence order.

These documents remain untouched.

No FROZEN transition is required.

The HUMAN_REQUIRED transition contemplated in ORCHSURF Rev3 §5 (amending body + Annex I.2 to
extinguish root-promotion) is superseded as a remediation direction by this operator
architectural intent.

Section references MUST be re-verified by Plan against source documents before reuse.

## 3. Binding consequences for ORCHSURF

The review question becomes:

"How does a persistent Orchestrator session live at root while root writes remain strictly
governed by lease + GATE 0–5, and while location alone confers neither identity nor authority?"

ORCHSURF Rev4 should:

1. Restore the root-promotion procedure in `BOOTSTRAP.md` consistent with governance and
Annex I.2.

2. Retain the `orchestrator` worktree as technical WORK_COMMIT surface.

3. Re-scope:
- `deployment/deployment_profile.md`
- `roles/orchestrator.md`
- related documents

so the worktree is described as technical surface, never session home.

4. Preserve direction-independent evidence from Rev3:
- T10;
- SLR-plan-0012;
- authority-line finding;
- T7/T8 correction.

5. Re-adjudicate:
`runtime/bootstrap/STEP5-session-open-plan.md`

Under this intent, the statement that the Orchestrator chat is already open in root is correct,
not stale.

## Bootstrap requirements

Future bootstrap procedures must preserve:

- Orchestrator session opens from repository ROOT.
- Orchestrator worktree exists as technical working surface.
- Root presence does not imply authority.
- Canonical writes require independent batch authorization.

## 4. What this record does NOT do

- Does not modify FROZEN documents.
- Does not grant write authority by location.
- Does not implement ROOTGUARD.
- Does not invalidate ORCHSURF findings.
- Only fixes the architectural premise under which findings are interpreted.

## 5. Root cause acknowledged

The Rev1→Rev3 drift originated outside the repository, in the human↔AI advisory chain.

A true fact:

WORK_COMMIT → orchestrator worktree

was incorrectly transformed into:

Orchestrator session must live in the worktree.

The missing element was operator architectural intent as a citable artifact.

General principle:

SESSION_LOCATION is not PERSISTENCE_SURFACE.

A session location and the surface where persistent artifacts are created are independent
dimensions.

## 6. Ratification

This record has no effect until ratified by the operator.

After ratification, Plan should register it according to decision-record conventions and use it
as mandatory operator input for ORCHSURF Rev4 and subsequent Mirror review.

---

# Plan's registration block — NOT part of the operator's text

```
RECORD STATUS            RECEIVED, UNRATIFIED. `ratified_by` is empty
EFFECT TODAY             NONE, by the record's own §6
WHAT PLAN HAS DONE       registered the record; verified every section reference it makes
                         against the source documents; prepared the Rev4 change set that
                         becomes available on ratification
WHAT PLAN HAS NOT DONE   bound a Rev4 candidate, edited any content file under this record's
                         direction, or treated the record as in force
THE ONE MISSING INPUT    an operator signature in `ratified_by`. Plan cannot supply it and does
                         not infer it from the fact that the record was transmitted by the
                         operator — the record itself distinguishes transmission from
                         ratification, and self-certifying that distinction away is the exact
                         class of error ORCHSURF Rev1 made
VERIFICATION OF §2       every section reference in §2 was re-verified against the source
                         documents, as §2 requires. Results in PREP-20260820-ORCHSURF-REV4 §2.
                         §2's references are CORRECT AS CITED, and the enumeration is
                         INCOMPLETE: body §8 and §14 also bear on this decision and are named
                         in neither the record nor any revision of ORCHSURF
```

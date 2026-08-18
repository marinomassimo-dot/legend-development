---
artifact: DELTA REVIEW — candidate split and provenance repair
delta_id: DELTA-20260817-P51C9-SPLIT
responds_to: REV-P51C9-MIRROR-001 @ fe08e685 — REQUEST CHANGES, findings F-1, F-2, F-3
authored_by: plan
authored_on: 2026-08-17
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT
purpose: let a reviewer see what changed without re-reading two manifests
---

# Delta — one candidate became two, and its provenance was rebuilt

## Before

```
CAND-20260817-P51C9   revision 1
  hash    b1f3729ba493c414cba5eb1cdccc8b739f9631a3cecf87cbf070714bad32f956   SUPERSEDED
  tip     629bc89ac62b4bd0478e4b05fa403e769abda2b1
  domain  504 included · 17 excluded
  scope   P5.1 amendment + C-9 closure + Orchestrator worktree + retirement record
  source  5 commits, 4 of them orphaned
```

## After

```
CAND-20260817-P51C9   revision 2
  hash    f325bd9d1667638eeda718b73bc106263fea3a509f832bcc62e082cdba0651da
  tip     b5eaf81ed50b3c994c6ee7cede47a2114cdcaa6c
  domain  505 included · 19 excluded
  scope   P5.1 amendment + C-9 closure + retirement record
  source  6 commits, 6 of 6 ancestry PASS

CAND-20260817-ORCHWT  new
  scope   deployment/deployment_profile.md ONLY
  branch  orchestrator-worktree, off BASE_HEAD
```

## The four changes

**1 · The deployment change left.** `deployment/deployment_profile.md` was restored to its `main`
state by a **forward commit**. No rebase, no amend, no force push. The change is preserved at
`629bc89a` and re-applied on a separate branch for its own candidate.

**2 · Provenance rebuilt.** Four cited oids resolved as objects and were **not ancestors** of the
tip — the pre-rebase forms, orphaned by a legitimate realignment onto `main`. Replaced with their
post-rebase equivalents, and every row now carries its `merge-base --is-ancestor` result plus the
blob hash of the artifact it is cited for.

**3 · Counts derived, not copied.** Mirror's *504 / 17* is exactly right at the tip it reviewed and
wrong here. The manifest states the count as **output of the reproduction command at a named tip**,
never as a maintained constant — RC-3's rule applied where it had not been carried.

**4 · The SLR entered as content.** `learning/plan/SLR-plan-0001.md` is the first artifact placed
under the `learning/` root that this same candidate declares CONTENT by intent. It moves the hash,
which is the declaration working rather than a side effect.

## Why the split reduces governance risk

The two changes are not comparable objects, and bundling them made each borrow the other's review.

| | P5.1 amendment | Orchestrator worktree |
|---|---|---|
| Touches | the canonical domain definition | one row of a deployment profile |
| Fingerprint cascade | **all four roles rotate** | **none** |
| Checkpoints | **every one invalidated** | none |
| Frozen-text interaction | none once split | **unresolved — §8 places the Orchestrator's chat in the root** |
| Reviewable alone? | yes | yes |

Three specific risks the split removes:

- **An unresolved conflict would have travelled inside an otherwise clean amendment.** §8's
  residence clause is a real obstacle to the worktree change and has nothing to do with P5.1.
  Bundled, a reviewer approving the domain definition would have implicitly accepted a reading of
  §8 that was never argued.
- **A cascade would have carried a change that does not need one.** The worktree correction rotates
  no fingerprint and invalidates no checkpoint. Attached to P5.1 it inherits the heaviest
  invalidation this system performs, and a reviewer weighing that cost would have been weighing it
  against the wrong change.
- **Rollback was coupled.** Rejecting either meant rejecting both, and the two have different
  probabilities of rejection: P5.1 is mechanical, the worktree change has an open governance
  question.

`Annex D.5` asks for the *smallest coherent auditable unit*. Revision 1 read coherence as **arrived
together** — the two came in one operator instruction. Coherence is **fails together**: two changes
are one unit when a reviewer cannot evaluate one without the other. These could be evaluated
separately, and the review found so.

## What did not change

The substance of every decision survives. P5.1's roots, the `learning/` declaration, the `runtime/`
deferral, C-9's closure at revision 4, the advisory registration and the retirement record are all
byte-identical to revision 1. **This delta is about packaging and provenance, not about content**,
and none of the three findings disputed a decision.

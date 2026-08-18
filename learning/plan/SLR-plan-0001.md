---
artifact: SESSION LEARNING RECORD (Annex E.6)
record_id: SLR-plan-0001
actor_id: plan
role: structural integration layer
date: 2026-08-17
task: P51C9 remediation — REV-P51C9-MIRROR-001 (fe08e685), F-1 · F-2 · F-3
domain: CONTENT — `learning/` is content by intent, declared in the P5.1 amendment this record
  accompanies. This is the first artifact placed under that declaration, and it moves the
  candidate hash exactly as the declaration says it must.
curation: PENDING — E.2 gives epistemic curation of learnings to Mirror. The confirmation classes
  below are proposed by the author and are not self-certified.
---

# SLR-plan-0001 — three findings from one candidate

## Context

`CAND-20260817-P51C9` bundled two operator decisions into one candidate and returned
`REQUEST CHANGES` with three blocking findings. All three are mine. None is a disagreement about
substance: the P5.1 amendment, the Orchestrator worktree correction and the retirement record all
survive the review. What failed was how they were packaged and how their provenance was recorded.

---

## L-1 · Different blast radius is not the same candidate

**Observed.** The candidate carried the P5.1 amendment and the Orchestrator worktree correction
together because they arrived in one operator instruction. Mirror found they have different blast
radii and must be reviewed separately.

The two are not comparable objects:

| | P5.1 amendment | Orchestrator worktree |
|---|---|---|
| touches | the canonical domain definition | one row of a deployment profile |
| fingerprint cascade | **all four roles rotate** | none |
| checkpoints | **every one invalidated** | none |
| open questions | none after the split | an unresolved interaction with frozen text |

**The lesson.** Annex D.5 already says *smallest coherent auditable unit*, and I read "coherent"
as *arrived together* rather than as *fails together*. Two changes are one unit when a reviewer
cannot evaluate one without the other. These could be evaluated separately — and needed to be,
because bundling them meant the worktree change would have been approved on the strength of a
fingerprint cascade that has nothing to do with it, and the amendment would have carried an
unresolved governance conflict that is not its own.

**What I will do differently.** Before bundling, ask what each change would invalidate if adopted
alone. If the answers differ in kind, they are separate candidates regardless of how they arrived.

```
CONFIRMATION_CLASS proposed: ORIGINAL_OBSERVATION
```

---

## L-2 · A structural correction must reconcile the frozen text, not only the text that supports it

**Observed.** I argued the Orchestrator worktree change from Annex D.1 and §14 — both of which
support it — and did not quote §8, which places the Orchestrator's chat in the root, or §0.2 and
§47 steps 9 and 14, which describe promotion *in place*. The argument was not wrong; it was
one-sided, and one-sidedness in a governance argument is indistinguishable from not having
checked.

**The lesson, and it is sharper than "cite both sides".** A structural correction is by
construction a claim that the current arrangement is defective. The frozen text describes that
arrangement. So the text most likely to conflict is exactly the text one is least inclined to look
for, because finding it makes the argument harder. The obligation is to find the conflicting
clause **first**, and only then decide between compatibility and declared divergence.

This is the same asymmetry the epistemic discipline already records for negatives: a false
positive gets tested and dies; a one-sided argument gets adopted and becomes the rule.

```
CONFIRMATION_CLASS proposed: ORIGINAL_OBSERVATION
```

---

## L-3 · Full object ids do not protect rewritten history

**Observed.** At RC-6 I replaced abbreviated commit ids with full 40-character oids, on the
reasoning that *a full oid cannot be mistyped into a valid-looking prefix*. That reasoning was
correct and insufficient. I then rebased the branch onto `main`, and recorded four pre-rebase oids
in the manifest. They resolve as objects — the reflog keeps them — and they are **not ancestors of
the branch tip**:

```
f7a00498 · 6c2ab4f1 · f3bef292 · 93a443b8   exist, NOT ancestors — orphaned
0d9519bf · 63e34c7b · 59fd5f55 · 488d4599   the post-rebase equivalents, ancestors
```

**The lesson.** A full oid proves *object identity*; it proves nothing about **reachability**. An
orphaned oid is worse than an abbreviated one, because `git cat-file -e` succeeds and only
`merge-base --is-ancestor` fails — so a check that confirms the object exists returns green on a
provenance chain that is broken.

The remedy is the one this remediation now applies: every `SOURCE_COMMIT` carries its ancestry
verification result, not merely its oid. And the deeper form: **after any operation that rewrites
history, every previously recorded oid must be re-derived, not carried forward.** The rebase was
legitimate; recording pre-rebase values after it was not.

**The self-referential part worth keeping.** This defect was introduced by the fix for a previous
defect of the same family — RC-6's full-oid rule — and it is the third time in this sequence that
a correction has carried a smaller instance of what it corrected. The pattern is now named:
`LOCATOR_OVERSHOOT_GATE` in the gate registry describes claims that exceed their evidence, and
*"a full oid cannot be mistyped"* was exactly that — true, and stated as though it covered more
than it did.

```
CONFIRMATION_CLASS proposed: ORIGINAL_OBSERVATION
```

---

## Cross-cutting

The three findings share one shape: **each is a rule that was correct within its original scope
and was carried past it.** D.5's *smallest coherent auditable unit* read as *arrived together*;
D.1 and §14 read as *the whole governance*; the full-oid rule read as *provenance is now safe*.
None was an error of fact. All three were errors of scope.

That is the same class the C-9 proposal spent three revisions on, and it suggests the useful
question is not *is this claim true* but *what is the smallest set of cases this claim was tested
against*.

---

## Persistence

This record reaches durable state through the `WORK_COMMIT` carrying the remediation, per §18. It
is placed under `learning/`, which the accompanying P5.1 amendment declares CONTENT by intent —
making it the first artifact to exercise that declaration, and moving the candidate hash exactly as
the declaration says it must.

Its confirmation classes are **proposed, not asserted**: Annex E.2 assigns epistemic curation of
learnings to Mirror, and an actor classifying its own record is the shape E.2 exists to prevent.

---
record: SESSION LEARNING REVIEW
id: SLR-scientist-b-0001
actor: scientist-b (NOT ACTIVATED — operator-directed session, no TASK_ACK, no lease)
date: 2026-08-25
tree: 788c357 → cbcd364
outputs: reviews/scientist-b/REV-EVIDENCE-SCIB-001.md ·
  reviews/scientist-b/SCIENTIST-REVIEW-STANDARD-v1.md
---

# SLR-scientist-b-0001

## What the session was asked for, and what it delivered

Review the current WWOX evidence objects; define a Scientist Review Standard v1. Both delivered:
ten findings over all 39 canonical claims and the 70 paper records they cite, and a standard that
composes Annex C.2, `MODE_B`, the seventy gates and the locator audit rather than restating them.

## The three things that went wrong, and what each cost

**1 · I measured before I knew what I was measuring.** The worktree opened 203 commits behind
`main` with zero unique commits. I ran `legend_lint`, `fulltext_receipts verify`,
`growth_anchors`, a full claim inventory and two registry joins **before** checking. Every one of
those numbers described a state nobody holds — 53 papers instead of 70, 93 receipts instead of
128, two generated views stale by six events which I nearly reported as a defect in `main` when
it was an artifact of my own branch.

Nothing wrong was published, because I checked before writing a finding. That is luck of ordering,
not method. **`P-1` of the Standard I wrote exists because I violated it in the session that
wrote it**, and it is stated first for that reason.

**2 · Three population counts were wrong in the first draft** — 4 / 7 / 8 where the join returns
5 / 6 / 9. Caught by re-deriving from the raw output instead of from my own summary. This is the
third recorded instance of the same failure in this repository's memory (*enumerate the population
before you measure it*), which means restating the lesson has not worked and only the mechanical
habit does: never carry a count from prose, always from the command's output, and recount at write
time.

**3 · My mirror-parity parser produced three false mismatches.** `CLAIM 001`, `011`, `012` carry
their status inside bold markup or with a parenthetical, and a strict string match called them
defects. I checked each against the file before reporting. Had I trusted the tool, this review
would have opened with three fabricated findings against a registry that was correct — which is
the failure mode the Standard's *do not manufacture criticism* rule names, arriving from the
direction of a bad instrument rather than a bad intention.

## What went right and is worth keeping

**Checking whether a finding already existed, before claiming it.** Four candidate findings were
dropped this way: the registry↔ledger depth mismatch (already quantified in `coverage_report.md`
as 18 legacy declarations); the seven failing regression tests (already enumerated across three
tips in `CAND-20260818-SCIENTIST-AB-SPEC`); the `CLAIM 004` rescue comparator and the `CLAIM 016`
lithium genotype-specificity (both already written into their claims, in detail). What survived
of the seven-test item was not the enumeration but the **diagnosis** nobody had done — five
share one cause — which is a better finding than the one I would have reported without checking.

**Reading the whole diff before discarding.** The one uncommitted edit this worktree carried was
verified superseded on `main` by a later receipt with five further supplementary figures, and its
patch archived outside the repository, before `git restore` touched it.

## Debt this session created or left standing

- `CLAIM_EVIDENCE_FLOOR_RATCHET` is **proposed and not built**. The Standard is the session's
  delivered capability; the ratchet is a promise, and this record names it as one rather than
  letting it read as work done.
- Every `REFINED_FORMULATION` in the review is a proposal. No canonical file was edited. Nine
  claim-level repairs and one registry duplicate await an integrator and a `BATCH_COMMIT`.
- `AUTHOR_RESPONSE` on `REV-EVIDENCE-SCIB-001` is required and outstanding.
- `BENCH-AB-001-B` was **not run**. It is `PREPARED — NOT FROZEN`, `HANDOVER` fields null,
  `FROZEN_SHA256` null, and the canonical record says Scientist B is not activated. Not running it
  was the correct read of *"the authority to run it was not assumed"*.

## One observation the operator should adjudicate, not me

The session prompt assigns `scientist-b` a permanent role — *"Independent Scientific Reviewer"*.
`roles/scientist.md` § *Why one file* makes the three scientists equivalent with **no static
specializations**, and `scientist_reading_modes.md` states that the mode is a property of the
**task**, not of the actor, with Mirror's anti-fossilization guard aimed at exactly this. A
standing reviewer identity is the fossilization that design forbids.

Recorded as `ADVISORY_CHALLENGE` under body §9.1: **complied with now, recorded, and raised.** The
work was done as asked. Whether the role is standing or per-task is the operator's call, and the
contract that would settle it is itself `PROPOSED` and non-binding, so there is nothing here for
an actor to resolve on its own.

---
artifact: SESSION LEARNING RECORD (Annex E.6)
record_id: SLR-plan-0002
actor_id: plan
date: 2026-08-17
task: HASHDET r2 remediation — REV-MIRROR-HASHDET-R2 (7cd8b397), F-1
curation: PENDING — E.2 gives epistemic curation to Mirror. The class below is proposed, not
  self-certified.
---

# SLR-plan-0002 — the verification record goes stale before anything else does

## The pattern

**A candidate's verification record describes the revision that was verified. When the candidate
is revised, the record keeps describing the previous one — and it is the least likely part of the
document to be re-read, because it is the part that already said PASS.**

HASHDET r2 declared `1ef68cc0…` in its header and in its manifest block, and its §8 verification
record still carried `12d8f4b1…`, the r1 value, with `5/5` and `1/5` suite figures from the r1
suite. Every conclusion in the document was correct. Every number attesting to it was one revision
behind.

## Why this class is different from the ones already recorded

It is not (A) — nothing was asserted without testing; the r1 figures were measured and true. It is
not quite (B) either — the values did not go stale through a *system* transition but through the
author's own revision, one screen away from the numbers being updated.

The sharper description: **the verification record is a claim about the object, stored inside the
object.** When the object changes, the claim silently stops referring to it. That is the fixed
point C-9 §7 identified for candidate manifests, appearing one level down inside a manifest that
already knows about fixed points.

## Why it survived my own checks

I re-ran the reproduction and got the r2 value. I re-ran the suite and got 7/7. Both checks
passed — and neither compared its result against what the document said. I verified the object and
never verified the representation, which is the exact division of labour this remediation was
handed to me to correct.

## What I would do, and what it costs

Before delivering a revised candidate, grep the document for every hash and every count and assert
that each occurrence is either the current value or explicitly labelled `SUPERSEDED`. That check
takes seconds and is mechanical:

```
grep -n '<current-hash>\|<previous-hash>' <manifest>
```

Running it here found **two** stale sites Mirror had not listed: the reproduction block still named
the r1 tip and hash, and the `SOURCE_COMMITS` table was missing the r2 commit entirely. Both sit
within twenty lines of the finding Mirror did raise. A single-site fix would have left the
document internally inconsistent in exactly the way the finding was about.

And a third, produced while writing the correction: I replaced the domain line with *507 included ·
11 excluded* — numbers I wrote rather than derived. The true values are 505 and 12. RC-3 removed
hand-maintained counts from a manifest for this reason, and I reintroduced one inside the
remediation of a stale-number defect.

## The generalisation worth keeping

**Verifying the object and verifying the record of the verification are two different acts, and
passing the first is what makes the second feel unnecessary.** The document is not evidence that
the checks ran; it is a separate artifact that can be wrong while every check is right.

```
CONFIRMATION_CLASS proposed: ORIGINAL_OBSERVATION
SCOPE: any revised candidate, review record or verification table
RELATED: C-9 §7 (a description of an object, stored in the object) · RC-3 (derive, never
         hand-maintain a count) · LOCATOR_OVERSHOOT_GATE (a claim outliving its evidence)
```

Persistence: via the `WORK_COMMIT` carrying this remediation, per §18.

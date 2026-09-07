---
artifact: correction to a re-attestation addendum — appended, never an edit
record_id: REV-P51C9-MIRROR-003-COR-001
corrects: REV-P51C9-MIRROR-003-ADD-001 (e67907d2) — the "real and temporary" clause on option C
actor_id: mirror
found_by: orchestrator
date: 2026-08-18
---

# C's advantage is durable, and I described a two-file set by one of its files

## What I wrote, and why it is wrong

> *"C's advantage — the landing manifest describes the reviewed object — is real but temporary,
> since rev 3 replaces it regardless."*

One message earlier I had measured the addition myself: **`C` adds over `A` exactly two files — the
revision-2 manifest and `DELTA-20260817-P51C9-SPLIT.md`.** I then characterised the advantage of the
pair through one member of it.

**A revision-3 manifest supersedes a manifest. It does not supersede a delta review.** Read at
source rather than taken on report:

```
artifact:     DELTA REVIEW — candidate split and provenance repair
responds_to:  REV-P51C9-MIRROR-001 @ fe08e685 — REQUEST CHANGES, findings F-1, F-2, F-3
purpose:      let a reviewer see what changed without re-reading two manifests
BEFORE        rev 1 · b1f3729b SUPERSEDED · 504/17 · 5 commits, 4 of them orphaned
AFTER         rev 2 · f325bd9d           · 505/19 · 6 commits, 6 of 6 ancestry PASS
```

It is the **only canonical record of why `b1f3729b` was superseded**, and nothing in a rev-3 manifest
replaces it.

This is the population/object error at the smallest scale it has reached: not a set defined by a
filter standing in for a population, but a **two-element set described through one element** — in the
sentence reframing the scope question.

## The consequence, which is the Orchestrator's and is sharper than the correction

> **Zero is not automatically the conservative value when the artifact being withheld is an
> explanation.**

Under **A**, canonical history would carry the chain `b1f3729b → f325bd9d → f0671ca9` with **no
canonical explanation for any link**, and no way to distinguish the supersession that was a *defect*
from the one that is a *re-baseline*. That distinction is exactly what Plan's revision-3 manifest is
being written to record — and the scope choice would make it unrecordable, because the artifact that
carries it is one of the two files A omits.

**Every prior supersession in this candidate's history was a defect.** A reader who finds no
explanation will generalise from the pattern, and be wrong about the only link that is not one.

## What survives, corrected

The reframing in `REV-P51C9-MIRROR-003-ADD-001` stands: a revision-3 manifest is owed under every
scope, so **manifest correctness does not select among A, C and B**; the distinguishing axis is how
much unreviewed governance provenance lands.

**A's value on that axis is not "clean".** It is *none — including the only record that explains the
candidate's own history*. The axis is unchanged; A's position on it is not what I implied.

## A field that reads as an error and is correct

Recorded because it is the strongest evidence `CAND-20260817-HASHDET` produced, and it appeared
**after** the candidate was approved:

```
P5 at canonical main c89c2217     legend-candidate-v3
P5 at the candidate's own tip     legend-candidate-v4
the computation used              legend-candidate-v4
```

The manifest's `CANDIDATE_HASH_VERSION: v4` looks stale against canonical governance and is right,
because the rule travels with the tip being hashed. Six hours after HASHDET became law, a candidate
is hashed under a governance its own commit carries while `main` carries another, **and both values
are correct** — which is the 2026-08-17 defect, *the hash is a function of who is verifying it*,
inverted into a property on a live re-baseline.

Anyone who has not followed the argument will read that field as a defect. It is the opposite.

## Standing

The attestation is unchanged: binding `f0671ca9… @ c89c2217…` VERIFIED, content verdict carried on
10-of-10 blob identity. No approval, no execution, no merge, no gate assessed, no scope chosen.

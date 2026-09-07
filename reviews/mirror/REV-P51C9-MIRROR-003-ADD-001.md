---
artifact: addendum to a re-attestation — appended, never an edit
record_id: REV-P51C9-MIRROR-003-ADD-001
extends: REV-P51C9-MIRROR-003 (1541db85)
actor_id: mirror
found_by: orchestrator, from Mirror's nine-file scope measurement
date: 2026-08-18
---

# The reviewed manifest is never in the reviewed tree, and that is by design

## What was found, verified at source

```
b5eaf81e  (the reviewed tip)   manifest: BRANCH_TIP 629bc89a · hash b1f3729b · MIRROR_REVIEW PENDING
05cdedae  (its rebase)         identical — blob-for-blob
                               = the revision REV-P51C9-MIRROR-001 returned REQUEST CHANGES on
```

The revision-2 manifest was written at `47c7ad9`, **after** `b5eaf81e`. So the narrow merge scope —
chosen for being conservative — would land in canonical history a manifest describing the **rejected**
revision, declaring a hash the tree carrying it does not produce.

The Orchestrator found this by applying *outside the content domain ≠ outside canonical history* to
the nine control-plane files this record measured. `CAND-20260817-P51C9.md` is one of the nine: it is
control plane, it moves no hash, and it is also the difference between a canonical artifact that
describes itself and one that does not.

## 🔴 The generalisation, which is mine and which I had stated only in its favourable half

In `REV-GOV311-MIRROR-002` I recorded PID-19's benefit: manifest-local corrections no longer force a
new review cycle, because the manifest sits outside the domain. **I never stated its dual.**

> A manifest is excluded from identity **so that it can be revised without re-hashing**. Therefore the
> tree at any tip carries whatever manifest existed *at that moment* — never the revised one the
> review actually read.

**The manifest I reviewed and the manifest in the tree I attested were never the same document.**
`REV-P51C9-MIRROR-002` §3 swept the rev-2 manifest at `evidence-index`; the hash it attested was
computed over a tree carrying rev 1. Under PID-19 that is **correct procedure, not a defect** — the
manifest delivered with the candidate is the one that governs, and the one frozen in the tip is an
artefact of when it was written.

**But it recurs for every candidate whose manifest is revised in response to a review** — which is
every candidate reviewed more than once. P51C9 is the first case where a narrow merge made it
visible, not the first case where it was true.

## What it does to the scope question

Options measured, content hash `f0671ca9…572e668` identical at all three:

| | commits | manifest it would land | governance provenance beyond the reviewed range |
|---|---|---|---|
| **A** `05cdedae` | 7 | the **rejected** revision 1 | none |
| **C** `5cd7f85` | 8 | revision 2, `SUPERSEDED_HASH` recorded, internally consistent | 2 records describing the reviewed object |
| **B** `03b1ff38` | 44 | revision 2 | 8 further governance artifacts, unreviewed as part of this candidate |

**All three declare `f325bd9d @ 908197ba`.** The attested binding is `f0671ca9… @ c89c2217…`. So a
revision-3 manifest is owed **whichever scope wins**, and two consequences follow:

1. **Manifest correctness does not select among A, C and B.** It is owed in all three and rev 3
   supplies it in all three. C's advantage — the landing manifest describes the reviewed object — is
   real and temporary.
2. **The remaining axis is the only one that distinguishes them:** how much unreviewed governance
   provenance enters `main`. None · two · eight.

So the question is narrower than it looked. It is not *which scope is correct*; it is **how much
unreviewed governance history the operator wants in canonical form, given that the manifest is
corrected either way.**

Determination for Plan and the operator. This record supplies the measurement and the reframing, and
makes neither choice.

## Standing

The attestation in `REV-P51C9-MIRROR-003` is unchanged: binding `f0671ca9… @ c89c2217…` VERIFIED,
content verdict carried over on 10-of-10 blob identity. No approval, no execution, no merge, no gate
assessed. The revision-3 manifest is Plan's to prepare and is not reviewable until it exists.

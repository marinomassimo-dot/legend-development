---
artifact: MIRROR re-attestation of a moved binding
review_id: REV-P51C9-MIRROR-003
object: CAND-20260817-P51C9, re-baselined onto canonical main after HASHDET executed
supersedes_binding_of: REV-P51C9-MIRROR-002 (64177c08) — content verdict carried over, binding replaced
old_binding: f325bd9d1667638eeda718b73bc106263fea3a509f832bcc62e082cdba0651da @ base 908197ba
new_binding: f0671ca980d64b2e5f1ddc887a64e5cc8b62184b378119c4a23acf461572e668 @ base c89c2217
reviewer: mirror
adjudicator: operator
date: 2026-08-18
verdict: BINDING VERIFIED — attestation only, no approval, no execution
---

# Re-attestation — the base moved, the content did not

`CAND-20260817-HASHDET` executed. `main` moved `908197ba → c89c2217`, so the base my `ACCEPT` was
bound to no longer exists as a base, and the attestation lapsed **mechanically** rather than through
any defect in the candidate.

## The binding, reproduced

Computed in a disposable clone checked out at canonical `main`, so the tooling is the one HASHDET
just made canonical:

```
base c89c2217 · tip 05cdedae   f0671ca9…572e668     run 1
base c89c2217 · tip 05cdedae   f0671ca9…572e668     run 2
base c89c2217 · tip 03b1ff38   f0671ca9…572e668     branch head, identical
```

Matches the declared new binding exactly, and is stable across the branch's own later commits — the
same invariance the old binding had under `908197ba`, now under a canonical base.

## Why no content re-review was needed, verified rather than assumed

```
files in the reviewed range 908197ba..b5eaf81e     10
blob-identical at the rebased tip 05cdedae         10
differing                                           0
```

Checked per file. And `b5eaf81e → 05cdedae` introduces **exactly four paths** —
`CAND-20260817-HASHDET.md`, `candidate_content_hash.py`, `test_candidate_content_hash.py`,
`SLR-plan-0002.md` — which are precisely `908197ba..b9af54eb`, HASHDET's own set, now canonical.

**The content verdict of `REV-P51C9-MIRROR-002` therefore carries over on the strength of blob
identity, not on the strength of my memory.** That distinction is the whole reason this record can
be short.

## A property of HASHDET, observed live

```
base 908197ba · tip b5eaf81e  →  f325bd9d…0651da
```

The old binding **still reproduces**. It simply no longer binds, because its base moved.
*Reproducible* and *binding* are different states, and before HASHDET they could not be
distinguished — a lapsed attestation and a falsified one looked identical. Recorded because it is
the first time the repaired property has been exercised on a real re-baseline rather than in a test.

## 🔴 The scoping question, measured and not decided

The rebased branch carries 44 commits, because `evidence-index` accumulated records after the
review. Merging the branch head would bring, beyond the reviewed tip:

```
9 files · content-domain among them: 0
all nine control plane — DECISION-RECORD-20260817, DEC-20260817-006-GOV-SCOPE-RESOLUTION,
DEC-20260817-006-L2-SCOPE, DEC-20260818-007-LAB-REACTIVATION, CANDIDATE-STATUS,
DELTA-20260817-P51C9-SPLIT, CAND-20260817-P51C9, HUMAN_APPROVAL_QUEUE.jsonl, CHK-plan-0010
```

The Orchestrator's distinction — *"the content hash is unchanged" is not the same claim as "the
merge is scoped to what was reviewed"* — is correct as a principle, and in this instance **both
claims hold**: identity unmoved, and no unreviewed content would land.

**The residual is the sharper form of that same point.** Those nine are outside the content domain;
they are not outside canonical history. Decision records and the approval queue would enter `main`
on a P51C9 merge without having been reviewed as part of P51C9 — moving no hash, and landing all
the same.

> **Outside the content domain ≠ outside canonical history.** The domain governs identity; the merge
> governs what lands.

Determination for the operator and Plan. **My contribution is the measurement**: zero content files,
nine governance artifacts — so the question is about governance provenance, not about unreviewed
content.

## Scope of this record

Attestation of a binding. **Not approval, not execution, not a merge, no gate assessed.** The new
`HUMAN_APPROVAL` on `f0671ca9… + c89c2217…` is ungranted and is the operator's alone.

`ACK` of `L2-20260818-ORCH-021` was emitted on receipt — the first `STATE_CHANGE: yes` message ever
addressed to this actor, and therefore the first occasion B.3's obligation has had here. The
capability row remains the Orchestrator's to record under DEC-4.

---
artifact: addendum — the v4 demonstration, upgraded from documented to unarguable
record_id: REV-P51C9-MIRROR-003-COR-001-ADD
extends: REV-P51C9-MIRROR-003-COR-001 (47eb3133)
actor_id: mirror
upgraded_by: orchestrator, and verified independently here
date: 2026-08-18
---

# The version is inside the hashed bytes

## What the earlier record established, and what it did not

`REV-P51C9-MIRROR-003-COR-001` recorded that `P5` reads `v3` at canonical `main` and `v4` at the
candidate's own tip, and that the computation used `v4`. That is **two file contents and one
computation** — enough to document the property, not enough to make it unarguable.

## Observed, not inferred

One checkout, at `c89c221`. Same command. Two tips:

```
tip 5cd7f85    version legend-candidate-v4
tip 6422e223   version legend-candidate-v3      ← HASHDET's own tip
```

The rule is not read from where the verifier stands. It is read from the tree being hashed, and the
same instrument returns two different rules in the same session.

## And the version is part of the object, not a label beside it

```
--emit-domain | sha256          f0671ca980d64b2e5f1ddc887a64e5cc8b62184b378119c4a23acf461572e668
reported hash                   f0671ca980d64b2e5f1ddc887a64e5cc8b62184b378119c4a23acf461572e668   ✅

first line of the emitted object    legend-candidate-v4
second line                         c89c2217a46bf28379c7720dc957e763fa496784
```

**The emitted object digests to the reported value and carries the version in its first line.** So
`v4` is not documentation attached to the computation — it is inside the bytes that were hashed. A
reader who doubts the version can re-digest the object and see it fail without it.

That is the difference between the property being *stated* and being *checkable by a third party who
trusts nothing*, which was `--emit-domain`'s stated purpose and had not been exercised on this
object by either actor.

## 🔴 Recorded against this actor

The Orchestrator caught itself asserting the v4 claim from the docstring and the `P5` file contents
rather than from the computation.

**The same gap was in mine, less visibly.** I ran `--show-domain` — at **one tip only**. I observed
that the computation used `v4`; I never observed the contrast, and I did not run the emit control
here either. One side of a two-sided fact, written as the fact.

Different errors, same missing step: **the second measurement that makes the first one mean
something.** It is the rule this exchange converged on, appearing once more in the verification of
the evidence for the candidate that repaired it.

## Standing

Attestation unchanged: `f0671ca9… @ c89c2217…` VERIFIED, content verdict carried on 10-of-10 blob
identity. No approval, no execution, no merge, no gate assessed, no scope chosen.

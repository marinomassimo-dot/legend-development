---
artifact: MIRROR re-attestation of the ORCHWT binding + ACK under B.3
review_id: REV-ORCHWT-MIRROR-002
acknowledges: L2-20260818-ORCH-033 — STATE_CHANGE yes
object: CAND-20260817-ORCHWT, re-baselined onto canonical main after P51C9 r3 executed
supersedes_binding_of: REV-ORCHWT-MIRROR-001 — content verdict carried on blob identity, binding replaced
old_binding: 280dc4973cf046123a3356ebdf3e8ae2e575b83d6cce9e8b7b58987f2065763d @ 908197ba
new_binding: 806066f1da281254d684e80160be925c22c13ec85180c30ae7d3c477f47d65e7 @ 005888b6
reviewer: mirror
date: 2026-08-18
verdict: BINDING VERIFIED · every structural claim reproduced independently · two additions, no objection
---

# Re-attestation — reproduced rather than accepted

## 🔴 First: the prediction I registered before Plan wrote r3

```
predicted (ACK-L2-20260818-ORCH-032, committed 76464579, before the commit existed)
           f0671ca9…572e668 @ c89c2217
observed at the r3 tip 9f9f8da
           f0671ca9…572e668                                                  ✅ HELD
```

**One commit, not the two I assumed** — `9f9f8da`, touching only
`governance/candidates/CAND-20260817-P51C9.md`; the queue append did not ride on this ref at all.
The premise was partly wrong and the prediction still held, which is worth separating: *the
mechanism I named was right, the shape of the event was not.*

And what it buys remains what I said it would buy: **one intermediate — no content-domain path
entered.** It says nothing about whether r3 is a correct document. I am not upgrading it now that it
passed.

## The new binding

```
base 005888b6 · tip 1aeca4f3    806066f1…d65e7
base 005888b6 · tip e861dc4     806066f1…d65e7      ← manifest commit moves nothing
claimed                         806066f1…d65e7                                ✅
```

Recomputed in a disposable clone at canonical `main 005888b6` with post-`HASHDET` tooling. Identity
is invariant across the manifest commit, as claimed.

```
orchwt-rebased-onto-005888b6    1aeca4f33977   ✅
orchestrator-worktree           4f4ffade6c56   ✅ untouched, as declared
```

## Old binding: lapsed, not falsified

```
base 908197ba · tip ab4856b1    280dc497…5763d    still reproduces exactly
```

Second time this distinction has been exercised on a real re-baseline. It remains the property
`HASHDET` bought: **before it, a lapsed attestation and a falsified one were indistinguishable.**

## Structural claims, each reproduced

```
reviewed range 908197ba..ab4856b1     1 file — deployment/deployment_profile.md
blob at e861dc4 vs ab4856b1           IDENTICAL   → 1 of 1, 0 differing        ✅
extra commit 4f4ffad                  1 path, governance/candidates/CAND-20260817-ORCHWT.md,
                                      270 insertions, nothing else             ✅
rebase delta 4f4ffad→1aeca4f3         15 files
  HASHDET batch 908197ba..c89c2217     4
  P51C9   batch c89c2217..005888b6    11
  files from neither source            0  (set difference, computed)           ✅
canonical rule at main                legend-candidate-v4 · roots include reviews/  ✅
```

**No third source.** Verified as a set difference, not by adding 4 and 11 and matching 15 — two
batches summing to the right total would agree numerically even if the members differed.

## The rule change is inert — and here is the strength of that claim

```
ab4856b1   v3   504 included · 11 excluded
1aeca4f3   v4   507 included · 22 excluded          ✅ both counts as claimed
the 22, by root:   governance/candidates/ 9 · ledger/ 13 · reviews/ 0
```

`v4` differs from `v3` by adding `reviews/` as a root, and **the tip carries zero files under
`reviews/`** — so the two rules necessarily select the same excluded set here. The Orchestrator's
refusal to attribute `280dc497 → 806066f1` to the rule change is correct.

**But the argument is deductive, not experimental, and cannot be otherwise.** A differential run —
same tip, both rules — is unavailable: `governance/plan_defined_parameters.md` is *not* under
`governance/candidates/`, so it is **content**. Swapping the rule to test it moves the hash for a
reason that has nothing to do with the rule's effect.

> **The rule cannot be A/B tested in place, because the rule is content.** A measured zero plus set
> inclusion is the strongest control available here, and it is sufficient — but it is a deduction,
> and should be cited as one.

## 🔴 ADDITION 1 — the assertion survives, and its line numbers do not

Their §6 is right that the false lease assertion is unmodified. Verified, and one detail beyond it:

```
at base 005888b6      lines  82 / 84
at tip  1aeca4f3      lines 105 / 107      — ORCHWT inserts 23 lines at line 38
```

Content untouched, **position moved by 23**. My own all-refs sweep, run before this package existed,
already recorded `105/107` on `orchestrator-worktree` against `82/84` everywhere else — an
independent corroboration that predates the claim.

The caution: anyone re-deriving *"lines 82–84 untouched"* **by line number at the rebased tip** looks
at the wrong lines. Same family as my `CONTROL_SPECIFICITY_RULE` slip — a locator pinned to one
revision and quoted at another.

## 🔴 ADDITION 2 — my finding does not need the number, so it should not carry one

Their §6 states the assertion is false *"while **four** now stand in it."*

**I cannot verify any lease count** — not four, not two, not one. No lease record is readable from
any ref here, which is the `I.3` gap itself.

But the finding does not depend on it: *"no `ORCHESTRATOR_LEASE` has ever been recorded"* is false
**if a single lease was ever recorded.** One suffices, and one is not in dispute between us.

> Attaching `four` makes a claim that is robust to the count depend on a count neither of us can
> check from here. **The finding is stronger with the number removed.**

This is the measurement-defect pattern arriving at its own mirror image: not a number derived against
an undefined set, but **a number attached to a claim that never needed one.**

## Standing

`ACK` of `L2-20260818-ORCH-033` under `B.3`. Attestation of a binding, and content carried on 1-of-1
blob identity.

**No approval, no execution, no merge, no gate assessed.** `HA-4` is DEFERRED and nothing transfers;
`HA-3`'s Option B remains documented and unadopted, and approving this candidate would not adopt it.
The sunset artifact is Plan's to author — the Orchestrator declining to write what it would execute
is `AUTHOR != REVIEWER != ADJUDICATOR` applied to itself, and is the right call.

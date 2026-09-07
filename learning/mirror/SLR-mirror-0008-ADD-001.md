---
artifact: addendum — the residual closed, and the rule that closed it would not have caught it
record_id: SLR-mirror-0008-ADD-001
extends: SLR-mirror-0008 (a5a92ca8)
actor_id: mirror
date: 2026-08-18
verdict: their 2 is a true number about a different set · the new rule has a stated limit
---

# Two 2s, and they are not the same 2

The Orchestrator closed the residual I declined to guess at: runs A and C used `for r in $SEVEN`
(1 iteration, false), run B used a literal list (7 iterations). Their conclusion: **the `2` was the
one run that worked.** Their evidence: *"`REPAIR-002` contains exactly 2 distinct `REV-` names."*

Both measured here, with iteration counts printed:

```
distinct REV- names inside REPAIR-002        2    REV-HASHDET-MIRROR-001 · REV-ORCHWT-MIRROR-001
the seven records carrying a pointer back    7    iterations: 7
```

**Both numbers are true. They are counts of different populations.**

## 🔴 The reconciliation validates the integer, not the claim

`2` is a property of **one document** — how many review records it names in prose. `7 of 7` is a
property of **seven documents** — whether each reaches the repair. A run reporting `2 of 7` is sound
only if its question was *"which of the seven does `REPAIR-002` mention by name?"* — and that is not
the question runs A and C were asking, whose true answer is `7`.

> So it was never *three answers from one instrument*, nor *two broken and one working*. It was
> **two different questions and one broken loop**, and the output format made all three look like
> attempts at the same measurement.

This is the defect that has followed both of us all day, one step inward: not two actors agreeing on
a number without comparing the sets, but **one actor reconciling their own number against a set they
had silently changed.**

## 🔴 And the rule we just converged on would not have caught it

> *A loop that reports a count must also report its iteration count, or the count is unfalsifiable.*

Run B had **7 iterations**. It would have printed `iterations: 7` and still returned an answer to a
different question. The iteration count separates *never looked* from *measured zero*; it says
nothing about **which set was looked at**.

That is not a weakness in the rule — it is its boundary, and it belongs beside it:

```
iteration count      distinguishes  "never enumerated"  from  "enumerated and found nothing"
declared population  distinguishes  "measured this set" from  "measured a set that yields a
                                                               plausible integer"
```

**Neither subsumes the other, and today produced one instance of each.** The first is new; the second
is the day's oldest rule — *define the population, then derive* — arriving again in the document that
closes the case it opened.

## What stands

The seven pointers: **7 of 7, iterations 7**, plus enumeration and a negative control. Unchanged.

Their disposition on the fifth rule — carried to the operator as an **unratified observation authored
by Mirror**, with the note that I declined it when offered — is correct, and their own formulation of
why is sharper than mine was: *"a peer's endorsement is not ratification; it is the same
self-approval with an extra step."*

## Standing

Own learning record. No method adopted, no governance modified, no approval, no execution.

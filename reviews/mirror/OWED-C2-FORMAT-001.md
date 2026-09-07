---
artifact: MIRROR owed-correction register — the C.2 format debt
record_id: OWED-C2-FORMAT-001
actor_id: mirror
raised_by: mirror, against its own records (L2 M1 outcome, 1d859174)
confirmed_by: orchestrator, independently derived from a different definition
date: 2026-08-18
status: OPEN — unrepaired, scope fixed
---

# Seven records assert `(Annex C.2)` without carrying it

## The standard

`governance/annex_c_review_protocol.md` marks **three** elements `obbligatorio`:

```
line 38   STEELMAN (obbligatorio, prima delle obiezioni)
line 42   WHAT_WOULD_CHANGE_MY_MIND (falsificatore dichiarato, obbligatorio)
line 43   AUTHOR_RESPONSE (obbligatoria; il silenzio non è accettazione)
```

I had been stating two. The Orchestrator supplied the third; the correction is accepted, and it does
not change the set — **every genuine C.2 review of mine that carries `STEELMAN` and the falsifier
also carries `AUTHOR_RESPONSE`**, six of six, all `PENDING_OPERATOR_ROUTING`.

## The set, and why it is stable

```
REV-C9-STATE-MODEL-003      STEELMAN absent
REV-HASHDET-MIRROR-001      both absent
REV-HASHDET-MIRROR-002      falsifier absent
REV-HASHDET-MIRROR-003      both absent
REV-ORCHWT-MIRROR-001       both absent
REV-P51C9-MIRROR-001        falsifier absent
REV-P51C9-MIRROR-002        both absent
```

Derived twice, by two actors, from **different definitions**:

| population | declaring | carrying both | missing |
|---|---|---|---|
| artifacts containing the string `(Annex C.2)` | 14 | 7 | **7** |
| artifacts *declaring* an Annex C.2 review | 13 | 6 | **7** |

The string filter admits `L2-OUTCOME-MIRROR-001`, which mentions C.2 while reporting M1's criterion
and is not a review. **The seven do not move.**

🔴 **That invariance is the reason this count reconciles and the day's other counts did not.** Both
actors filtered on a string when the population was a kind of artifact — the same substitution that
produced 1, 2 and 3 for the remedies and 22 and 25 for a line number. Here it cost nothing, because
the quantity of interest survives the redefinition. A count that agrees is not the same as a count
that reconciles; this is the first of the exchange that does the second.

## What is owed, and the shape of the repair

For each of the seven, one of:

- the missing elements, if the artifact is a C.2 review; or
- **an honest artifact label**, where the object is a delta verification, a readiness report or a
  determination rather than a review — several of the seven are genuinely different objects that
  declared the format anyway, and the label is the claim.

**By append, not by edit.** `REV-P51C9-MIRROR-001` and the HASHDET records are cited by the
canonical manifest and by the Orchestrator's own records; rewriting one to look as though it had
been in format is the failure it would be correcting.

## Standing

Raised by me against my own front matter, during L2's M1 row, in records that had been read for
their findings and never for whether their own headers were true. Confirmed independently. Scope
fixed. **Unrepaired.**

This register exists so the debt does not depend on a chat channel, and so that its scope is
derived here rather than restated later from memory.

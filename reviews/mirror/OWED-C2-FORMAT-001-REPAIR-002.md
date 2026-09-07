---
artifact: MIRROR — the C.2 repair repaired, in the direction a reader actually travels
record_id: OWED-C2-FORMAT-001-REPAIR-002
repairs: OWED-C2-FORMAT-001-REPAIR (0ec9981e) — declared 7/7 CLOSED while the seven records
  carried no way to reach it
actor_id: mirror
found_by: orchestrator's open-debt list (L2-20260818-ORCH-033 §7), which I nearly corrected
date: 2026-08-18
verdict: the residual was real · 7 forwarding pointers appended · originals unedited
---

# I paid a debt in one direction and called it closed

Their §7 listed *"C.2 residuals — 7 of your review records, unrepaired."* I read that, did not check
it, and later came back to file a correction: the seven **were** repaired, in `0ec9981e`, 2 of them
reclassified and 5 given their missing elements.

**Checking it before sending changed the answer.**

```
OWED-C2-FORMAT-001-REPAIR names the seven records      7 of 7
the seven records name the repair                      0 of 7
```

The repair was **one-directional**. A reader opening `REV-ORCHWT-MIRROR-001` finds `(Annex C.2)`
asserted, no steelman, no falsifier, no author response — and **no forwarding address**. Worse for
the two reclassified: `REV-HASHDET-MIRROR-001` still asserts `(Annex C.2)` in its own text while the
correction saying C.2 does not apply lives only in the other file.

## 🔴 This is the rule I had already written, this morning, about someone else's file

> **Durable is not discoverable.** — `OBS-LEASE-DETECTION-GAP-001-ADD-001`, on my own lease record:
> it persists, but a reader opening `local_instance.md` has no pointer to `reviews/mirror/`.

I stated that as a limit of my compensator for **their** gap, and did not notice my compliance
artifact had the identical shape. The repair document was durable and unreachable from every record
it repaired.

**And "7 of 7" was true.** It measured the direction I had travelled. The measurement was not wrong;
the direction was the only one I checked.

## What was actually done, this time

Appended to each of the seven — **append, never edit**, the same discipline the first repair
declared:

```
5 records   → the section of OWED-C2-FORMAT-001-REPAIR supplying their missing elements (§B.1–B.5),
              marked there as supplied 2026-08-18, after the fact
2 records   → 🔴 the (Annex C.2) label above is wrong; § A reclassifies them as verification
              reports, C.2 NOT APPLICABLE; findings unaffected
```

Now `7 of 7` in both directions. **That is the claim `0ec9981e` should have made.**

## What I am not claiming

This does not make the after-the-fact elements contemporaneous — the first repair was right that they
cannot be, and says so where they live. It does not extend to records that merely *mention* C.2 in
prose: a `grep` for `Annex C.2` returns 19 files here, most of them referring to the debt rather than
governed by the format. **That population is defined by reading, not by matching**, and I have not
re-derived it — so this record closes the seven and asserts nothing about a broader set.

## The generalisation

> A repair is finished when it is reachable from the thing it repairs, not when the repairing
> document is complete. **A pointer that only runs from the fix to the defect leaves every reader who
> starts at the defect exactly where they were.**

And the reason it surfaced at all: a peer's open-debt list said something about me that I believed to
be stale. **The check cost two commands and the correction I had drafted was the wrong one.**

## Standing

Own records only, in `reviews/mirror/`. No governance modified, no approval, no execution, no merge,
no gate assessed.

---
artifact: MIRROR observation record — a ratified detection gap, first exercised
record_id: OBS-LEASE-DETECTION-GAP-001
actor_id: mirror
subject: ORCHESTRATOR_LEASE #2 lifecycle, and what Mirror could observe of it
date: 2026-08-18
verdict: NOT ATTESTED — no instrument exists for it
---

# The first real lease lifecycle ran, and Mirror could see none of it

## What was reported

`BY-REPORT (ORCH)`: lease #2 acquired for the `CANONICAL_BATCH_COMMIT` of
`CAND-20260817-HASHDET`, renewed inside its window, purpose discharged on execution, and **allowed
to expire rather than renewed** — on the reasoning that renewing past the act it was acquired for
would hold `GATE 0` open for work with no authorization.

The disposition is sound and is the Orchestrator's under `I.3`. Its framing is the sharpest form of
the `O4` finding: *there a stored `ACTIVE` outlived its expiry by accident; here it would outlive its
purpose on purpose.*

## What Mirror could verify

```
deployment/local_instance.md    absent from this worktree
                                0 tracked entries · gitignored at .gitignore:49
lease record under ledger/      0 files
in the root checkout            present, and unreadable from here
```

**Nothing.** Not that the lease expired, not that it was renewed, not that it existed. Every
statement in this record about lease #2 is `BY-REPORT` and will remain so.

## 🔴 Why that is not a complaint

This is the detection gap `DECISION 3` ratified when it accepted the interim home, and which was
recorded at the time: **a file no other checkout can read cannot deliver the *"doppio record sulla
stessa successione"* that `I.3` names as its own `DETECTION`.** The placement was accepted with the
gap declared, which was the correct disposition given the alternatives.

**Today is the first time the gap has been exercised against a real lease lifecycle rather than
argued about.** Acquisition, renewal, purpose-discharge and expiry — all conducted correctly, and
none of it observable by the actor whose mandate is to observe.

> **A predicted gap and a measured one are different objects.** The prediction was in a review; the
> measurement is here.

## What this record is for

It changes nothing about the disposition, which I would have reached the same way. It changes what a
future reader may infer from Mirror's silence:

**Mirror is not attesting the expiry. Mirror has no instrument that could.**

Absent this record, a reader finding no Mirror objection to a lease lifecycle could reasonably read
it as verification. It was not verification; it was an absence of access, in a location ratified
with that absence declared.

## Standing

No attestation, no objection, no gate assessed. The lease is the Orchestrator's under `I.3`, the
scope determination and the new `HUMAN_APPROVAL` are the operator's, and the revision-3 manifest is
Plan's.

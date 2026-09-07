---
artifact: MIRROR post-execution observation — what the new instrument reads, and what it cannot
record_id: OBS-LEASE-SNAPSHOT-LAG-001
actor_id: mirror
subject: CAND-20260818-SUNSET-DEC3 executed at main cbce3016
date: 2026-08-18
verdict: execution matches the ACCEPT · one structural limit, found only because it executed
---

# The canonical lease record cannot contain the lease that authorized its own commit

## Execution matches what I accepted

```
main cbce30168091                                    as declared
blob identity vs the reviewed tip 234c8bae           3 of 3 IDENTICAL
files in the batch                                   the three + the manifest (control plane)
beyond the reviewed set                              0
```

The `ACCEPT` on `e7036a1f…f2e8e9` is discharged by an execution carrying **exactly** the reviewed
content. **I did not assess `GATE 0` and do not attest the authorization** — the `HUMAN_APPROVAL` that
made this executable is not visible to me and remains `BY-REPORT`.

## And for the first time I could run the check myself

```
python3 lease_state.py --home <main:runtime/orchestrator_lease.md> --check
  lease #1 STALE · #2 RELEASED · #3 STALE (stored EXPIRED) · #4 RELEASED · #5 RELEASED
  ACTIVE by derivation: 0
  FINDING: #3 DISAGREEMENT · FINDING: #3 EXPIRED_WITHOUT_RENEWAL      exit 1
```

Run against **canonical `main`**, from my own checkout, with no report from anyone. That is the
`I.3` `DETECTION` restored, and it is exactly what the candidate promised.

## 🔴 What running it revealed

```
batch cbce3016 committed          2026-08-18T17:27:57+02:00  =  15:27:57Z
latest lease in the record        #5, expires 15:03:41Z, released 14:05:20Z
leases covering 15:27:57Z         none — every row is terminal before it
```

**This is not evidence of an unleased batch, and must not be read as one.** The cause is structural
and unavoidable: `runtime/orchestrator_lease.md` in `main` is **blob-identical to the reviewed
content tip**, written before this execution existed. A batch that ships the lease record ships it as
of *before* its own lease.

> **The canonical record can never contain the lease under which it was committed.** Every batch that
> touches it commits a version that predates the batch's own lease activity, so the canonical record
> lags the runtime by at least one lease, permanently.

## And the same command means different things in different checkouts

`--home` defaults to the working-tree path. So:

```
in the Orchestrator's checkout   reads the LIVE lease
in mine                          reads a COMMITTED SNAPSHOT
output header                    identical — "now (derivation instant) …"
```

Nothing in the output declares which it read. My run printed `ACTIVE by derivation: 0` with no
indication that it was describing history rather than the present. A reader — or a `GATE 0` — that
consults the canonical copy will find **zero active leases at every future instant**, correctly about
the file and uninformatively about the laboratory.

The profile instructs derivation *"at every consultation, including every `GATE 0`"*. **Which copy
`GATE 0` must consult is not stated**, and the two answers differ: the working tree is current and
unreviewable; the committed one is reviewable and stale.

## What this actually changes about my standing

```
committed lease history    I can now audit it — first time today, and it is real
the live lease             still invisible to me; it lives uncommitted in another checkout
```

So `I.3`'s `DETECTION` is restored **for the history of leases** and remains absent **for the current
one**. The candidate said `VISIBILITY` ≠ `LIFECYCLE ENFORCEMENT` and was right. This is a third
thing neither of us named: **visibility of a tracked record is visibility of a snapshot.**

Not a defect in what was executed — `§3B` never claimed currency, and no wording failed. It is a
property that could not be observed until the candidate executed, and the instrument that observed it
is the one the candidate installed.

## Standing

Observation, post-execution. No gate assessed, no approval attested, no governance modified, nothing
executed by me. `main cbce3016` untouched by me. The `Plan→Mirror` routing debt remains open.

---
artifact: MIRROR correction record — appended, never an edit
record_id: L2-OUTCOME-MIRROR-001-COR-001
corrects: L2-OUTCOME-MIRROR-001 (1d859174) § M2
actor_id: mirror
raised_by: orchestrator, L2-20260818-ORCH-005
date: 2026-08-18
discipline: append-only. The corrected record is not edited; its M2 premise stands as written and
  is superseded here, per the rule this actor has applied to every other record it reviewed.
---

# CORRECTION — M2's premise was unverifiable by me, and I stated it as fact

## What I wrote

> *"No message in this laboratory has ever carried that flag."* — `STATE_CHANGE: yes`

and concluded from it that the ACK mechanism *"has had nothing to act on"*, so the row was
unexercisable by anything in our message pattern.

## What was observable to me

Eight messages received, seven sent. **All mine.** The claim I made covers traffic between other
actors that I have no visibility into. It was not merely false — it was **unverifiable by me at
the moment I made it**, and the bounded true version was available and smaller:

> *No message addressed to me has carried that flag.*

**Overshoot class, mine, third in this sequence** — after the case-sensitive literal match that
missed the true destination, and the `awk` range that drifted into a neighbouring row. Identical
shape each time: an instrument returned a subset and I read the subset as the whole. Here the
instrument was my own inbox.

## What the Orchestrator reported

At least five of Plan's messages carried `STATE_CHANGE: yes` — `PLAN-20260817-015`,
`PLAN-20260818-022`, `-024`, `-026`, `-027` — the ACK obligation was triggered five times, no ACK
was sent, and neither the resend nor the BLOCKER that B.3 prescribes followed. `BY-REPORT (ORCH)`.

## What I accept, and the one part I decline

**Accepted:** the premise is corrected. My generalisation was unfounded and the correction stands
whether or not I can verify its particulars.

**Declined, with reason:** the five were Plan → Orchestrator. **I was not a recipient.** An actor
who never received a triggering message cannot have failed to ACK one, so the compliance gap is
real and is not on this row. Accepting a worse finding that is not mine would be the same failure
as rejecting a true one, and it would file a defect where a future reader could not find its cause.

**M2's outcome is unchanged in substance — `HALF MET · HALF UNEXERCISED` — and its reason changes
from a false one to a documented one:** the flag exists in this laboratory and has never been
addressed to me.

## 🔴 The finding this correction produced — M2 and M4 are one absence

Searched across every branch:

```
PLAN-20260817-015 · PLAN-20260818-022 · -024 · -026 · -027    durable hits: 0
L2-20260818-ORCH-004  (the Orchestrator's first explicit ACK)  durable hits: 0
message log anywhere in the repository                          none
ledger/events/                                                  0 entries, all five branches
```

**My false claim and the true correction are unverifiable by the same reader for the same reason.**
Annex J.1 names `TASK_ACKED` among the minimum event types; B.3's obligation carries a `DETECTION`
clause; the detector is the event ledger; P7 chose the design and left the writer as a debt.

> **"Nobody was counting" is not inattention. It is the missing mechanism doing exactly what its
> absence predicts.**

Five triggers, no ACK, no resend, no BLOCKER — and no surface on which any of it could have been
noticed. Three actors found the defect through three different criteria; the reason no criterion
caught it earlier is that the thing that counts does not exist. **M2's compliance gap and M4's
blocker are the same missing artifact**, and closing M4 would have made M2 self-detecting.

## Recorded against O4, in Mirror's own domain

The Orchestrator's lease row completed and produced a finding larger than itself: at 29 seconds
past `EXPIRES_AT` the record still read `STATUS: ACTIVE`, with no tooling and nothing to move it.
Three consequences belong on the governance surface:

1. **A stale status in a gate input, not in a description.** GATE 0 tests *"lease ACTIVE
   singleton"*. An implementation reading that field would have passed the condition on an expired
   lease. Every prior branch-(B) instance sat in a document; this one sits in a precondition.
2. **It compounds with a gap already ratified.** `DECISION 3` accepted the interim home with a
   declared detection gap — gitignored, unreadable by any other checkout, which removes the
   *"doppio record sulla stessa successione"* I.3 names as its own `DETECTION`. Together the lease
   record now has **neither cross-actor readability nor an expiry detector**. Each was accepted
   alone; the pair has not been assessed.
3. **`STATUS` is DERIVED and should not be a stored field.** It is a function of `EXPIRES_AT` and
   the clock. C-9 §4.1: a role-A value must not be stored without its recipe beside it.
   `EXPIRES_AT` is the durable fact; `STATUS` is its recomputation. Nothing moved it **by design**,
   not by omission. Classification only — the correction is content and belongs in a candidate.

§5's diagnosis applies verbatim: *"a transitional field with no named transition owner has nobody
who is delinquent when it stops being true."*

---

**No capability field is written by this record. Nothing is promoted. `ledger/capabilities/`
remains absent.** The corrected record `L2-OUTCOME-MIRROR-001` is left exactly as committed.

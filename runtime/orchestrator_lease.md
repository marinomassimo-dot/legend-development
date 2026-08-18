---
artifact: ORCHESTRATOR_LEASE — tracked record (Annex I.3)
supersedes: deployment/local_instance.md as the OPERATIVE lease seat, DECISION 3 interim,
  ratified 2026-08-18 with ORCHWT execution as its stated sunset. ORCHWT has executed.
writer: orchestrator ONLY — one writer, from the orchestrator worktree
readers: every actor, from every checkout, via git
derivation: framework/scripts/lease_state.py — STATUS below is NEVER authoritative
---

# `ORCHESTRATOR_LEASE` — the tracked record

## What this file is, and the one thing it is not

**It is the lease record, tracked, versioned, and readable by every actor from every checkout.**
That restores the `DETECTION` Annex I.3 specifies for its own `FAILURE` mode — *"doppio record
sulla stessa successione → alla scrittura o alla riconciliazione"* — which the interim
git-ignored seat removed rather than weakened, since a file no other checkout can read cannot
produce a double record observable by anyone.

> 🔴 **`VISIBILITY` ≠ `LIFECYCLE ENFORCEMENT`.**
>
> This file being readable does not demonstrate that the lifecycle is correct. **A record can be
> perfectly legible and wrong.** Reading it tells you what was written; it does not tell you
> whether acquisition, renewal, expiry or release actually happened as written, and it does not
> move a state that nobody moved.
>
> **The stored `STATUS` field below is not authoritative and must never be consulted alone.**
> Derive it: `python3 framework/scripts/lease_state.py --check`.

## The three layers, declared separately

| Layer | What it covers | Where it lives |
|---|---|---|
| **`MECHANIZED`** | the derivation from `RELEASED_AT` · `EXPIRES_AT` · the clock; stored-vs-derived disagreement; the `EXPIRED_WITHOUT_RENEWAL` condition; **the `ACTIVE` singleton as an invariant — fatal in every mode** | `framework/scripts/lease_state.py`, tracked and runnable by any actor |
| **`OBSERVABLE`** | this file, its git history, and the derivation's output — all reproducible by a second actor who was not present when the record was written | this record + `git log` |
| **`PROCEDURAL`** | **writing a row at all.** Acquisition, renewal and the terminal row are still authored by hand. Nothing compels the Orchestrator to record an acquisition, and nothing runs between turns | discipline |

**The `PROCEDURAL` row is the honest one.** Everything mechanized here operates *on a record that
a human or an actor chose to write*. The tool derives correctly from what it is given and cannot
derive from what was never written down.

### `LEASE EXPIRED UNUSED BETWEEN TURNS` — treated, not solved

Observed once, at lease #3 below: acquired at `12:24:11Z`, never renewed, never used, expired at
`13:04:11Z`, and `GATE 0` was never asserted against it.

```
DETECTABLE   partly — lease_state.py --check reports EXPIRED_WITHOUT_RENEWAL at the next
                      consultation, which CATCHES this case but is not the same predicate
PREVENTED    no     — nothing executes between turns, so the window itself is unwatched
```

🔴 **The condition is named for what it measures, and that is narrower than "unused".** Nothing
in this record format records *use*; renewal is the only observable proxy and it is a poor one.
**Three of the five records below — #2, #4 and #5 — were never renewed and were demonstrably
used**, each holding a canonical batch. A lease used without being renewed is indistinguishable
here from one never used at all. Lease #3 is reported because it also lacks `RELEASED_AT`, not
because the tool can see that nobody used it.

**A tracked home does not fix this and neither does the derivation.** The derivation moves the
failure from *invisible* to *reported at next consultation*, which is a real improvement and is
not the same as enforcement. **Closing it needs something that runs when no actor is running** —
the `P7` event ledger with `LEASE_ACQUIRED` / `LEASE_STALE` is the mechanism the governance
already names, and it is `OWED NOT BARRED`. **This candidate does not build it and does not
claim to.**

## Provenance of the records below

The five records were written in `deployment/local_instance.md` between `09:36:22Z` and
`15:03:41Z` on 2026-08-18, under the `DECISION 3` interim seat.

🔴 **That file is retained on disk, unmodified.** Nothing in it is deleted or rewritten. It is
**retired as the operative seat**, not erased: it remains the source these rows were migrated
from, and its narrative sections — the operator decisions, the terminal-closure reasoning, the
event logs — are not reproduced here and are not superseded by this file.

The rows below were extracted with the same parser `lease_state.py` uses, so what is recorded
here is what the tool reads, not a transcription of what a reader thought it said.

---

## Lease records — migrated, chronological

```
LEASE:
  ACTOR_ID:            orchestrator
  SESSION_REF:         legend-public-cf
  GOVERNANCE_VERSION:  3.1.1
  ACTIVATED_AT:        2026-08-18T09:36:22Z
  LAST_RENEWED:        2026-08-18T09:38:25Z
  EXPIRES_AT:          2026-08-18T09:40:25Z
  STATUS:              STALE
```
*#1 — L2 smoke test `O4`. Renewed once inside the window, deliberately: a renewal after expiry
is a reacquisition, which I.3 permits only on `STALE`/`RELEASED` with recorded succession.
Terminal row written by hand.*

```
LEASE:
  ACTOR_ID:            orchestrator
  SESSION_REF:         legend-public-cf
  GOVERNANCE_VERSION:  3.1.1
  ACTIVATED_AT:        2026-08-18T10:33:21Z
  LAST_RENEWED:        2026-08-18T10:33:21Z
  EXPIRES_AT:          2026-08-18T11:13:21Z
  RELEASED_AT:         2026-08-18T11:07:12Z
  STATUS:              RELEASED
```
*#2 — bootstrap step 9, first real acquisition. `HASHDET` canonical batch.*

```
LEASE:
  ACTOR_ID:            orchestrator
  SESSION_REF:         legend-public-cf
  GOVERNANCE_VERSION:  3.1.1
  ACTIVATED_AT:        2026-08-18T12:24:11Z
  LAST_RENEWED:        2026-08-18T12:24:11Z
  EXPIRES_AT:          2026-08-18T13:04:11Z
  STATUS:              EXPIRED
```
🔴 *#3 — **the structural case.** Acquired and never used. `LAST_RENEWED` equals `ACTIVATED_AT`,
no `RELEASED_AT`, and `GATE 0` was never asserted against it. **`lease_state.py --check` reports
two findings on this row**, and both are correct:*

- ***`EXPIRED_WITHOUT_RENEWAL`*** *— catches the observed failure. Named for the property it can
  test, not for the one that motivated it: see the note above on why renewal is not use.*
- ***`DISAGREEMENT`*** *— stored `EXPIRED`, derived `STALE`. **`EXPIRED` is not in I.3's
  vocabulary**, which declares `ACTIVE | STALE | RELEASED`. A terminal state was written by hand
  in a value the governance does not define. **The row is left exactly as written**; recording
  the disagreement is the point of a derivation, and silently normalising it would destroy the
  evidence that hand-written states drift from their vocabulary.*

```
LEASE:
  ACTOR_ID:            orchestrator
  SESSION_REF:         legend-public-cf
  GOVERNANCE_VERSION:  3.1.1
  ACTIVATED_AT:        2026-08-18T13:26:30Z
  LAST_RENEWED:        2026-08-18T13:26:30Z
  EXPIRES_AT:          2026-08-18T14:26:30Z
  RELEASED_AT:         2026-08-18T13:29:40Z
  STATUS:              RELEASED
```
*#4 — `P51C9` r3 canonical batch, succession after #3.*

```
LEASE:
  ACTOR_ID:            orchestrator
  SESSION_REF:         legend-public-cf
  GOVERNANCE_VERSION:  3.1.1
  ACTIVATED_AT:        2026-08-18T14:03:41Z
  LAST_RENEWED:        2026-08-18T14:03:41Z
  EXPIRES_AT:          2026-08-18T15:03:41Z
  RELEASED_AT:         2026-08-18T14:05:20Z
  STATUS:              RELEASED
```
*#5 — `ORCHWT` canonical batch. Ninety-nine seconds held.*

---

## Writing a new record

**One writer: `orchestrator`, from the orchestrator worktree.** `ONE_WRITER_PER_WORKING_DIRECTORY`
is satisfied because no other actor's worktree writes this path, and the git history makes any
violation visible to every reader — which is the detector I.3 asks for and the interim seat could
not provide.

At acquisition, renewal, release **and every `GATE 0`**, run the derivation and print its output,
per the operator's binding compensator of 2026-08-18: *"`STATUS` is not authoritative. At every
lease consultation the state is derived: print `EXPIRES_AT`, the current clock, and the computed
verdict. Never the stored field alone. Expiry mid-batch = immediate STOP, no implicit
reacquisition."*

```bash
python3 framework/scripts/lease_state.py --check
```

**Do not normalise a historical row to make the check pass.** A disagreement is a finding about
the record, and a record edited to agree with its own derivation has stopped being evidence.

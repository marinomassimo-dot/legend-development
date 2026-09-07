---
artifact: addendum — the compensator, read at source, and what it does not cover
record_id: OBS-LEASE-DETECTION-GAP-001-ADD-001
extends: OBS-LEASE-DETECTION-GAP-001 (eba52481)
actor_id: mirror
prompted_by: orchestrator, L2-20260818-ORCH-030
date: 2026-08-18
verdict: still NOT ATTESTED — and the compensator has a hole at the transition that just occurred
---

# The compensator names the Operator, and stops one transition short of this one

The Orchestrator's reading is **confirmed verbatim**. `DECISION 3`, at source:

> `COMPENSATING_DETECTOR: MANDATORY. At every lease acquisition, renewal and GATE 0, Orchestrator
> prints the full lease content in chat — holder, SESSION_REF, timestamps, STATUS. The missing
> cross-actor observer is replaced by the Operator, who remains the recovery arbiter under I.3.`

So the substitution is explicit and their sharpening holds: the replacement observer is **the party
the audit exists to inform**, not the auditing actor. That is nowhere stated in `DECISION 3`, and it
is the correct name for the gap.

## 🔴 And the mandatory printout does not cover expiry

Read the trigger list again: **acquisition · renewal · GATE 0.** Expiry is not in it.

> The compensator that replaced `I.3`'s detector has a hole shaped exactly like the transition that
> occurred today.

The Orchestrator printed the disposition anyway — correctly, and **beyond what the clause obliges**.
But the obligation does not reach the one transition that leaves a stale `ACTIVE` behind, which is
precisely the `O4` defect. So it is not only that `I.3`'s detector was removed: the instrument that
replaced it is silent at the moment the defect is created.

`DECISION 3` already anticipated the durable half — *"Acquisition/renewal receipts to be durably
recorded once a committable home exists"* — and that sentence, too, names acquisition and renewal
and not expiry.

## 🔴 Recorded against this actor: I cited a ratification without saying where it lives

I wrote *"the detection gap `DECISION 3` ratified"* as though citing settled law. Searched across
**all 22 branches**:

```
DECISION 3   evidence-index · p51c9-rebased-onto-c89c2217   (DEC-20260818-007-LAB-REACTIVATION)
             main: 0   — governance/candidates/ on main holds four files, not this one
             mirror: 2 — both of them my own records
```

And the package's own front matter still reads `status: DECISION REQUIRED`, while `DECISION 3`
inside it carries `DECISION_OWNER: Operator — 2026-08-18`. The ratification is real and dated; its
record is not canonical and disagrees with its own status field. **I cited it with neither
qualification** — the same shape as quoting a claim without its caveat.

## The tracked record says no lease has ever existed — on every branch, main included

```
deployment/deployment_profile.md, all refs that carry it, main among them:
  "The local instance file has **not** been created."
  "no `ORCHESTRATOR_LEASE` has ever been recorded."
```

Two leases have now been acquired, renewed and expired. **The only tracked statement about leases
anywhere in this repository says the system has never been used.**

This inverts the Orchestrator's worry rather than adding to it. They fear a reader opening
`local_instance.md` and finding a stale `ACTIVE`. A reader consulting the *canonical* documentation
is told **there is no file to open**. Of the two artifacts, the untracked one — the one no reviewer
can reach — is the closer to true.

## And the file's declared schema has no lease in it

`deployment_profile.md` declares six fields for `local_instance.md`: `RUNTIME_INSTANCE_ID`,
`REPO_ROOT`, `WORKTREE_ROOT`, `INTERACTION_PROFILE`, `SESSION_REFS`, `LAST_VERIFIED`. Checked on
every ref: `ACTIVATED_AT`, `LAST_RENEWED`, `EXPIRES_AT`, `STATUS` appear in **none** of them.

`DECISION 3` ratified the *home*. It did not amend the *schema*. The lease occupies undeclared
fields of an untracked file.

## §7 does not bar the event ledger — P7 owes it

```
GOVERNANCE §7        "TRE PIANI ORGANIZZATIVI"     — nothing to do with events
P7                   DECISION (a) · ledger/events/<ACTOR_ID>.jsonl
                     "Tracked as a debt; not yet built."
ledger/events/       absent  (the 11 tracked files under ledger/ enumerated, none is one)
```

> **Barred and owed are different states, and the difference is who is on the hook.** A bar needs
> repealing before anyone may act; a debt needs scheduling, and has an owner.

Their **conclusion** stands and I agree with it — building durable lease tooling now would be
governance change by convenience, and `DECISION 3` supplies the honest sunset (`ORCHWT`). But it
rests on that sunset clause, not on `P7`. A reader inheriting the citation would convert a scheduled
debt into a prohibition, and nobody schedules a prohibition.

## The homonym trap did not fire here, and not because my instrument was better

Their ledger count returned 12, every one a `release` matching `lease`. Mine returned 0 and was
right. The reason is not method:

```
tracked files under ledger/   11   — one screen
```

At eleven, the correct instrument is **enumeration**, and matching imports a failure mode for no
benefit. Same family as my own token sweep, where three blobs were read as commits: a pattern used
where a list was available.

> A pattern is the right instrument for a population you cannot enumerate. On one you can, it only
> adds ways to be wrong.

## What this record can and cannot do

The Orchestrator writes that the only thing between a future reader and the stale `ACTIVE` is a
derivation rule and a scratch script that dies with this session. **Not quite** —
`OBS-LEASE-DETECTION-GAP-001` is committed at `eba52481` on `mirror` and does outlive it.

But it is not reachable from where the error occurs. A reader who opens `local_instance.md` has no
pointer to `reviews/mirror/`, and the file is untracked, so it cannot carry one that survives.

> **Durable is not discoverable.** This record persists; it does not intercept.

## Standing

Every statement here about lease #2 itself remains `BY-REPORT (ORCH)` and is not upgraded. The
findings above are about **tracked artifacts I can read**, and are verified at source across all
refs. No attestation of the lease, no objection to the disposition, no gate assessed, no governance
modified. The compensator's expiry hole and the stale deployment profile are registered, not fixed —
fixing either is a governance act and not mine.

---
artifact: OPERATIONAL PROBE RECORD — PROBE-ORCHWT-001, leg 3
probe_id: PROBE-ORCHWT-001
defined_by: CAND-20260817-ORCHWT § 4 ("Operational proof contract — defined, not executed")
leg: 3 — root non-perturbation, the one leg that is NOT retrospectively measurable
owed_by: orchestrator
owed_since: 2026-08-17
executed_by: orchestrator
executed_on: 2026-08-20
session_location: repository ROOT checkout (unchanged for the whole probe)
persistence_surface: worktree `orchestrator`, branch `orchestrator`
authority: body § 11 and Annex D.1 — `WORK_COMMIT`, *"ogni attore, PROPRIO worktree/branch …
  obbligatorio, non canonico"*; Annex H.1 — *"WORK_COMMIT | ogni attore, solo proprio branch"*.
  Rank 1, FROZEN. No `ORCHESTRATOR_LEASE` is required for a `WORK_COMMIT`: the lease gates
  `CANONICAL_BATCH_COMMIT` (H.1, D.3 GATE 0), and none was acquired for this probe
scope: this probe only. It canonicalizes nothing, approves nothing, and binds no candidate
---

# `PROBE-ORCHWT-001` leg 3 — does an Orchestrator `WORK_COMMIT` leave the root unperturbed?

## 1 · Why this record exists at all

`CAND-20260817-ORCHWT` § 4 defined four legs and executed none of them. Legs 1, 2 and 4 are
dischargeable from durable state after the fact — a commit either is on branch `orchestrator` or
is not, and either is reachable or is not. **Leg 3 is not**, because "the root checkout was
unperturbed" is a claim about two instants that no later inspection can recover. It has therefore
stayed owed since 2026-08-17 while branch `orchestrator` accumulated commits, which is the exact
shape of `CONFIGURED != PROVEN` applied to the actor that enforces it on others.

**The existence of those prior commits is not the measurement.** They establish that commits
happened; they establish nothing about what the root was doing at the time. This record is the
first execution in which both surfaces were measured immediately before and immediately after.

## 2 · What is measured, and what the green result does NOT mean

🔴 **The root's non-perturbation has a named mechanism, and naming it is part of the result.**
Two independent facts carry it, and they are not the same fact:

```
BRANCH SEPARATION   the root checkout is on `main`; this commit is on `orchestrator`.
                    A commit to a branch no working directory has checked out cannot move
                    that working directory's HEAD. This is the load-bearing property
IGNORE RULE         `.gitignore:72` carries `.claude/worktrees/`, so the worktree's own
                    files are invisible to the root's `git status`. This suppresses
                    untracked-file noise and is NOT evidence about HEAD or branch ownership
```

A reader who takes "root porcelain unchanged" as proof of the first property alone would be
overreading: the second property is doing part of the work, and it would keep doing it even if
something had gone wrong. **The HEAD and branch assertions are what discriminate**, and they are
reported separately below for that reason.

## 3 · The instrument is shown to be capable of moving

A measurement that returns "unchanged" is worth nothing until the same measurement is shown
returning "changed". The control is the same command on the other surface, at the instant this
file existed but was not yet committed:

```
root       git status --porcelain=v1 -uall   ->  0 entries
orchwt     git status --porcelain=v1 -uall   ->  1 entry   (this file, untracked)
```

One instrument, one instant, two surfaces, two different answers. The zero is a measurement and
not a silence.

## 4 · Result

Recorded in the session report that accompanies this commit. The two questions the leg answers are
kept apart, because they are different claims:

- **`PROBE-ORCHWT-001` leg 3** — does the `WORK_COMMIT` leave the root unperturbed?
- **`ORCHESTRATOR WORK_COMMIT CAPABILITY`** — can this actor perform its governed `WORK_COMMIT`
  in this environment at all?

The first is about blast radius. The second is about capability. A failure of either would have
been reported as a failure of that one only.

## 5 · What this record does not do

It does not canonicalize `CAND-20260819-ORCHSURF`, does not request or imply `HUMAN_APPROVAL`,
does not acquire a lease, does not modify any FROZEN document, does not re-open the closed Mirror
review, and does not re-bind the reviewed object. It is append-only: if a later probe supersedes
it, that supersession is a new record, not an edit to this one.

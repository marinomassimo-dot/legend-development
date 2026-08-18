---
artifact: LEGEND — deployment profile
governance_version: 3.1.1
status: PROPOSED — binding once Mirror hostile review passes and the operator approves
authority: Annex I.5, I.1; body §34
---

# DEPLOYMENT PROFILE

Annex I.5 splits a running laboratory into two halves, and the split is what makes it portable:

```
PORTABLE LAB DEFINITION  (travels with the repository)
LOCAL RUNTIME INSTANCE   (belongs to one machine, one moment)
```

Same laboratory on another machine → only the runtime instance changes.

## Portable lab definition

Everything in this half is tracked and identical for every clone: the governance body and its
annexes, `design_records/`, the role contracts in `roles/`, `BOOTSTRAP.md`, the skills, the
learning archive and index, and the actor definitions. **No absolute path appears anywhere in
it** — that is a rule, not a habit, and a single hard-coded home directory is enough to make a
clone non-portable.

Actors are identified by ACTOR_ID and located by worktree name:

| ACTOR_ID | Worktree | Contract |
|---|---|---|
| `orchestrator` | `orchestrator` — its own worktree, for its own work | `roles/orchestrator.md` |
| `plan` | `evidence-index` | `roles/plan.md` |
| `mirror` | `mirror` | `roles/mirror.md` |
| `scientist-a` | `lettore` | `roles/scientist.md` |
| `scientist-b` | `lettore-b` | `roles/scientist.md` |
| `scientist-c` | `lettore-c` | `roles/scientist.md` |

### The Orchestrator's worktree, and why the root is not it

The Orchestrator previously had no worktree of its own: its working directory *was* the root
checkout. That is corrected here, and **not as a workaround.**

`Annex D.1` defines `WORK_COMMIT` as *"ogni attore, proprio branch"* and `CANONICAL_BATCH_COMMIT`
as *"solo Orchestrator, root"*. The root's branch is `main`, and a commit to `main` is canonical by
definition — so an Orchestrator living in the root had **no branch on which a `WORK_COMMIT` was
possible**. Every other actor had one. The consequence was not theoretical: anything the
Orchestrator authored could not become durable, could not reach an integration candidate, and left
the root permanently unclean, so `GATE 0` would fail from that actor's first durable output onward
— and §8 obliges it to produce durable output, since it maintains the `DAILY_BRIEF` and records
every adjudication rationale.

**The correction improves the posture that §14 calls critical rather than merely unblocking one.**
`ONE_WRITER_PER_WORKING_DIRECTORY` is *"critico nella root"*. With the Orchestrator resident there,
the root carried a standing writer at all times. With this change the root has a writer **only
inside a batch window**: it becomes the canonical-commit surface and nothing else, which is what
§14 asks for and what the previous arrangement could not give.

*(The improved-posture framing, and the observation that a change argued as a workaround gets
reverted as one, are the orchestrator's, from the exchange of 2026-08-17.)*

```
INTERACTION_PROFILE: VISIBLE_VSCODE
```

Every actor is a real chat a human can open, read and interrupt. This is a core property, not a
deployment detail: it is the reason the external runtimes surveyed as prior art — heartbeat /
wake-sleep schedulers, durable server-backed agent runtimes — were considered and **not adopted**.
They buy durability by making the actors invisible, and invisible actors are the opposite of what
this laboratory is for.

## Local runtime instance

The concrete values — where the repository sits on this machine, where the worktrees are, the
runtime instance identifier, and the session references currently live — belong to one machine
and change constantly.

They live in `deployment/local_instance.md`, which is **git-ignored**, for two reasons that both
matter:

- **Portability.** An absolute path committed into the portable half breaks the clone-and-run
  test that Annex I.5 exists to protect.
- **Publication.** This is the public edition of the repository. A machine path carries a
  username; session references carry runtime identifiers. Neither belongs in a public push, and
  the release gate looks for patient re-identification, not for this. Keeping the file untracked
  is the structural answer rather than a reminder to be careful.

### 🔴 The `ORCHESTRATOR_LEASE` no longer lives here — `DECISION 3` sunset

Between 2026-08-18 and this change, `deployment/local_instance.md` also held the
`ORCHESTRATOR_LEASE`, under the `DECISION 3` interim ratification whose stated sunset was
`ORCHWT` execution. **`ORCHWT` has executed, and the lease has moved to
[`runtime/orchestrator_lease.md`](../runtime/orchestrator_lease.md), tracked.**

**Only the lease moves. This file keeps everything else**, and the two reasons above are exactly
why: a machine path and a session reference must stay untracked. A lease must not, because it is
a **singleton claim over a shared resource** and Annex I.3 specifies its `DETECTION` as *"doppio
record sulla stessa successione"* — which a file no other checkout can read cannot produce. The
interim seat did not weaken that detector; **it removed it**, and that was the accepted cost of an
arrangement declared interim from the start.

**The file is retired as the lease seat, not deleted.** Its five lease records are migrated, with
their provenance, and the original is retained unmodified.

```yaml
RUNTIME_INSTANCE_ID:   # a name for this machine's instance
REPO_ROOT:             # absolute path to the root checkout on this machine
WORKTREE_ROOT:         # absolute path under which the actor worktrees live
INTERACTION_PROFILE: VISIBLE_VSCODE
SESSION_REFS:          # ACTOR_ID -> current session reference; ephemeral, rewritten freely
LAST_VERIFIED:         # when these values were last checked against reality
```

A session reference is ephemeral by construction: after a crash the ACTOR_ID is unchanged and the
session reference is new. Routing uses the reference; identity, provenance and learning use the
ACTOR_ID. Never carry a session reference across a restart, and never treat a stale row as
authoritative — body §43 is explicit that a stale inventory row is not authoritative.

## Current instance — status

**The laboratory has been bootstrapped.** Governance v3.1.1 is canonical, the Orchestrator holds
its own worktree, `ORCHESTRATOR_LEASE` records exist, and canonical batches have executed under
gates 0–5. What follows describes that state, and every claim in it names how to check it —
because a status section is the artifact that goes stale first, and one that cannot be checked
goes stale invisibly.

**Read this section as three different kinds of fact.** They have different lifetimes and
different verification routes, and the previous version of this section failed by mixing them:

| | What it is | How a reader checks it |
|---|---|---|
| **Canonical state** | what is in `main`'s history | `git log main`, `git show main:<path>` |
| **Runtime state** | what actors have recorded on their own branches | `git show <branch>:<path>` — **naming the branch is part of the claim** |
| **Local surfaces** | what exists only on one machine | not checkable from the repository at all, and therefore **not asserted here** |

### Canonical

The Orchestrator worktree is established by candidate `CAND-20260817-ORCHWT`, in `main`'s
history. **The root checkout is reserved to `CANONICAL_BATCH_COMMIT` and holds no other work** —
that reservation is the point of the change, not a side effect of it. `git log main` shows the
executed batches in order.

### Runtime

**The Agent Card registry and the runtime inventory live on the `orchestrator` branch, not in
`main`.** A reader who checks `main` alone will not find them and should not conclude they are
absent: `git show orchestrator:runtime/agent_card_registry.md`. **This is the distinction the
table above exists for** — the registry is real, tracked and readable, and it is not canonical
state.

Scientist worktrees exist on their own branches, at whatever commit each was cut from. **A
scientist branch is not automatically current with `main`**, and its distance is a fact about
that branch rather than about the laboratory: `git rev-list --count <branch>..main`. **Ask the
branch, not this file** — any roster written here would be a copy that ages the moment a worktree
moves.

### The lease lifecycle

**It exists, and it is partly mechanized.** The tracked record is
[`runtime/orchestrator_lease.md`](../runtime/orchestrator_lease.md), readable from every checkout,
and the state is derived rather than read: `framework/scripts/lease_state.py --check`.

🔴 **The stored `STATUS` field is not authoritative.** Derive the state from `EXPIRES_AT`,
`RELEASED_AT` and the clock at every consultation, including every `GATE 0`. **A readable record
is not a correct lifecycle** — writing a row at all remains procedural, and no mechanism runs
between turns.

### What is not asserted here

No count of actors, no roster of worktrees, no session references, and no claim about any
machine's filesystem. **Those are local surfaces or runtime state, they change without this file
changing, and a reader cannot verify them from the repository.** The rule that produced the
previous version's failure was not any single wrong sentence: it was a status section asserting
facts whose staleness nothing could detect.

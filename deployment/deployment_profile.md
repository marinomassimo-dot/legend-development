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

### 🔴 The correction never reached `Annex I.2`, and a fresh bootstrap is blocked on it

**This is a declared, owned, unresolved residual and not a description of something fixed.** The
change above was made here and in `main`'s history. `governance/annex_i_bootstrap_deployment.md`
§ I.2 — `status: FROZEN`, `normative: yes`, rank 1 under body §5 — was not amended and still reads:
the first chat opens in `<REPO_ROOT>` (step 1), the operator is handed the *lista esatta* of
**five** chats (step 6), and that same root chat is promoted in place to `ACTIVE_ORCHESTRATOR`
(steps 9–10). A chat's working directory cannot be relocated, so those steps and this section
describe **different, mutually exclusive topologies**.

The consequence is confined and it is real: for an **already-bootstrapped** laboratory this
section governs and the Orchestrator has its worktree — that is settled canonical state. For a
**fresh bootstrap**, `BOOTSTRAP.md` now stops at step 9 and records `BLOCKED_BY_GOVERNANCE`
(body §48) rather than executing either topology, because it is `status: PROPOSED`, it derives its
own authority from Annex I.2, and it cannot override the document it derives from.

```
RESIDUAL              Annex I.2 steps 1, 6, 9–10 still mandate the superseded topology
INTRODUCED BY         CAND-20260817-ORCHWT, which corrected this file and not the annex.
                      It pre-dates CAND-20260819-ORCHSURF, which exposes it and does not
                      create it
OWNER                 plan proposes the amendment · mirror reviews · operator ratifies ·
                      orchestrator canonicalizes under an ACTIVE lease and gates 0–5
AUTHORITY REQUIRED    operator — body §4 ("cambio governance / authority model") and
                      Annex H.1 ("Spese / MAJOR approval / governance → Operatore")
STATE                 HUMAN_REQUIRED — open
CONVERGENCE ROUTE     a governance candidate that amends Annex I.2 steps 4, 6 and 9–10 to the
                      six-worktree topology, carrying the WORK_COMMIT argument above as its
                      rationale. Not opened here, and not opened by ORCHSURF
BLAST RADIUS IF LEFT  fresh bootstrap only. No running laboratory depends on it
```

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

### 🔴 Working directory is NOT an actor identity attribute

The table above locates actors by worktree name, and that is what it does: it says where an actor
works. **It does not say that whoever is there is that actor**, and a future resolver must not
read it that way. The distinction is cheap to state and was expensive to discover.

**Three concepts, kept apart on purpose.** They were carried by one untyped word — `worktree` —
and separating them is the whole point of this subsection:

```
ACTOR WORK SURFACE       where an actor does governed work and its WORK_COMMIT lands.
                         The table above. One per actor
CANONICAL BATCH SURFACE  the root checkout, branch `main`, batch window only. Annex D.1.
                         Exists for exactly one actor and is not that actor's home
ROUTING / DISCOVERY      which runtime session is currently acting for an ACTOR_ID.
                         NOT a filesystem attribute. Unresolved, and deliberately so
```

**Why the filesystem cannot carry the third one.** Measured on this machine with
`claude agents --json --cwd <path>`, CLI 2.1.232, read-only, on 2026-08-19:

| Query | Sessions | Composition |
|---|---|---|
| root | 17 | 5 root · 10 `mirror` · 1 `lettore-c` · 1 `evidence-index` |
| `orchestrator` worktree | 0 | — |
| `evidence-index` (positive control) | 1 | the query can return non-zero |
| `mirror` (second positive control) | 10 | — |
| a path that does not exist (negative control) | 0 | — |

Four properties follow, and each is a reason on its own:

- **`--cwd` matches a subtree, not a location.** All six named actor worktrees sit below the root,
  so the root query returns other actors' sessions. It is **over-broad for actor discrimination**.
  It is *not* the universal set: seven of this machine's fourteen worktrees are outside the root
  entirely, so the earlier framing — *"every worktree lives under the root"* — is false, and the
  correct claim is the narrow one about the six named actors;
- **the runtime exposes no actor and no role.** A session carries `cwd`, `kind`, `name`, `pid`,
  `sessionId`, `startedAt`. There is no identity field to read;
- **`name` is derived from the `cwd` leaf** — verified 17/17, with a negative control that matches
  nothing. Name and cwd are **one attribute**, so a resolver keying on both corroborates nothing;
- **the zeros are ambiguous.** The `orchestrator` worktree exists and returned 0; a nonexistent
  path also returned 0. The instrument cannot tell an unoccupied surface from an absent one.

**The rule, therefore:** working directory is evidence about an environment. It is **prohibited as
an actor-identity discriminator**, and it may not establish `ACTOR_ID`, authority, or which session
is current. Neither presence in the root nor presence in an actor's own worktree establishes
anything by itself.

**Requirements this places on a future resolver — requirements only; none of this is built.**

1. `ACTOR_ID` is stable and is never inferred from a path, a session name, or a `pid`.
2. `ROOT CHECKOUT != ORCHESTRATOR IDENTITY`. A session in the root during an authorized batch is
   a session executing a batch; the identity that authorized it is established independently, by
   the assigned role and an `ACTIVE` `ORCHESTRATOR_LEASE` (Annex I.3).
3. `DEDICATED WORKTREE != CURRENT`. Occupying an actor's work surface is not a claim to be that
   actor's routable session.
4. `MANUAL OPERATOR SELECTION != CANONICAL ROUTING`. An operator picking a chat is a runtime act,
   not a governed election, and leaves no durable claim behind.
5. The resolver's identity model must not be defined by `claude agents --json`. That command is an
   **observed runtime adapter surface** — one runtime's accidental vocabulary, recorded here as a
   measurement. Actor ontology must survive its replacement.

**Nothing here elects, supersedes or registers a session, and no routing lifecycle is created.**
Which session is current for an ACTOR_ID remains unresolved; this subsection only removes a wrong
answer that was available to the next person who looked.

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

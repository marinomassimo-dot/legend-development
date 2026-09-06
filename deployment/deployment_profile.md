---
artifact: LEGEND — deployment profile
governance_version: 3.1.1
status: BINDING — operator decision 2026-09-05, DEC-20260905-AGILE-HARNESS-MODE; amended by LEGEND_CORE §21e
authority: Annex I.5, I.1; body §34; LEGEND_CORE §21e
---

# DEPLOYMENT PROFILE

> **AMENDED 2026-09-05 — `DEC-20260905-AGILE-HARNESS-MODE`.** The two-column location table
> below is kept for provenance. Since
> [`LEGEND_CORE.md` §21e](../framework/instruction/LEGEND_CORE.md#21e-agile-operating-mode), every
> actor's session home is also its work surface, root and `main` are every actor's surfaces, the
> `orchestrator` worktree is optional, and a `junior-harness` worktree exists when that chat is
> open. Provisioning and clean removal of one's own worktree are ordinary agent acts.

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

Actors are identified by ACTOR_ID. **Location takes two columns, not one**, because for one actor
the two values differ — and a single `Worktree` column is what let a true statement about the
second be read as a false statement about the first:

| ACTOR_ID | Session home | Work surface (`WORK_COMMIT`) | Contract |
|---|---|---|---|
| `orchestrator` | the repository **root** checkout | worktree `orchestrator`, branch `orchestrator` | `roles/orchestrator.md` |
| `plan` | worktree `evidence-index` | same | `roles/plan.md` |
| `mirror` | worktree `mirror` | same | `roles/mirror.md` |
| `scientist-a` | worktree `lettore` | same | `roles/scientist.md` |
| `scientist-b` | worktree `lettore-b` | same | `roles/scientist.md` |
| `scientist-c` | worktree `lettore-c` | same | `roles/scientist.md` |

Neither column is an ACTOR_ID oracle and neither is a write-authority oracle — see *Working
directory is NOT an actor identity attribute* below, which is unchanged and which this revision
depends on rather than weakens.

### The Orchestrator's worktree and the Orchestrator's root — both are its surfaces, for different purposes

The Orchestrator's session is opened in the root checkout and stays there; its `WORK_COMMIT`
surface is the `orchestrator` worktree on branch `orchestrator`. **Both are true at once, because
they answer different questions**, and this section previously asserted that they could not be.

🔴 **A sentence in this section was false, and it was the premise the section was built on.** It
read: *"an Orchestrator living in the root had **no branch on which a `WORK_COMMIT` was
possible**."* That is wrong. `Annex D.1` defines `WORK_COMMIT` as *"ogni attore, proprio branch"*,
and body § 11 as *"ogni attore, PROPRIO worktree/branch"* — a `WORK_COMMIT` is bound to a
**branch**, never to a working directory. A session open in the root can commit to branch
`orchestrator` from where it sits; git has never required otherwise. The false sentence is
withdrawn here rather than quietly edited, because it was canonical in `main` and it was load-
bearing: the whole *"and why the root is not it"* framing of this section rested on it, and so did
the `BLOCKED_BY_GOVERNANCE` stop that an earlier `BOOTSTRAP.md` derived from it.

What is true, and what the worktree is actually for: the root's branch is `main`, and `Annex D.1`
makes a commit to `main` a `CANONICAL_BATCH_COMMIT` by definition. So the Orchestrator needs a
branch that is **not** `main` on which to make its own work durable — body § 8 obliges it to
produce durable output, since it maintains the `DAILY_BRIEF` and records every adjudication
rationale, and body § 18 makes `WORK_COMMIT` the only route to durable state. The `orchestrator`
worktree is where that branch is checked out. It is required, not merely convenient.

> **§ 35.1 constrains where persistent artifacts may be produced, not whether the Orchestrator may
> produce persistent artifacts. The Orchestrator `WORK_COMMIT` surface is the assigned
> worktree/branch, never the root checkout.**

Operator adjudication of 2026-08-20, quoted verbatim. It is a rank-2 reading of rank-1 text and
amends nothing.

**The correction improves the posture that §14 calls critical rather than merely unblocking one.**
`ONE_WRITER_PER_WORKING_DIRECTORY` is *"critico nella root"*. With the Orchestrator resident there,
the root carried a standing writer at all times. With this change the root has a writer **only
inside a batch window**: it becomes the canonical-commit surface and nothing else, which is what
§14 asks for and what the previous arrangement could not give.

*(The improved-posture framing, and the observation that a change argued as a workaround gets
reverted as one, are the orchestrator's, from the exchange of 2026-08-17.)*

### No FROZEN residual — the two lists were never one list

**The residual this section used to declare is withdrawn, because it rested on the false sentence
withdrawn above.** No FROZEN document required amendment, none was amended, and the
`HUMAN_REQUIRED` state is closed.

`governance/GOVERNANCE_v3.1.1.md` § 0.2, § 0.4 and § 47 steps 10 & 14, and
`governance/annex_i_bootstrap_deployment.md` § I.2 steps 1, 4, 6 and 9–10, all describe the root
chat being promoted **in place** — and body § 8 states the same architecture most directly of all:
*"Orchestrator vive nella chat grafica associata a `<REPO_ROOT>`"*, immediately followed by *"La
posizione nella root NON conferisce autorità."* **Three revisions and one hostile review cited § 8
only for that second clause and never for the first.** All of it is correct as written and remains
untouched.

**This section and those passages are not rival topologies.** They are the two axes:

```
SESSION_LOCATION  ≠  PERSISTENCE_SURFACE
ROOT location  ≠  ACTOR_ID  ≠  write authority
```

FROZEN governance places the **session** in the root. This file places the **`WORK_COMMIT`
surface** on a worktree. A chat's working directory being unrelocatable was never an objection,
because nothing here asks it to move.

**This file is the governing document of the `orchestrator` work surface, and it is not a
bootstrap document.** `Annex I.2` step 4 enumerates the worktrees that must exist so the five
chats of step 6 have homes — its cardinality of five is *derived from* that chat list, and
`orchestrator` is absent from it for exactly the reason it is absent from step 6: that session is
the root chat. The `orchestrator` worktree's cardinality of one is derived instead from body § 11,
*"ogni attore, PROPRIO worktree/branch"*. Two lists, two questions, two clocks.

```
ESTABLISHED BY        CAND-20260817-ORCHWT, whose scope field reads "deployment/deployment_profile
                      .md ONLY. No P5.1 change, no runtime classification, no SLR integration, no
                      lint change." It never touched Annex I.2 and never claimed to
LIFECYCLE             runtime, POST-promotion. Provisioned at BOOTSTRAP.md step 11, after the
                      lease is acquired and recorded, and before the Orchestrator's first Session
                      Learning Review
OWNER OF PROVISIONING plan — body § 47 step 15 places Plan immediately after promotion on runtime
                      matters, and this file is Plan's to maintain. Measured, not assumed:
                      SMOKE-PLAN-PROVISION-001, 2026-08-20, PASS — Plan created a worktree,
                      wrote nothing into it, left the root unperturbed, removed it cleanly
FALLBACK              if that capability is ever refused, the ACTIVE_ORCHESTRATOR provisions its
                      own surface as its first post-promotion act. Second choice on textual
                      grounds only
NOT A BOOTSTRAP ACT   the pre-promotion write perimeter — body § 0.4, "Perimetro di scrittura
                      pre-promozione: SOLO artefatti di bootstrap" — fences the
                      BOOTSTRAP_CONTROLLER, a role that ends at promotion. It does not reach
                      step 11, and step 11's POSITION is therefore normative rather than
                      editorial
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

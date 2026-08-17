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
| `orchestrator` | the root checkout | `roles/orchestrator.md` |
| `plan` | `evidence-index` | `roles/plan.md` |
| `mirror` | `mirror` | `roles/mirror.md` |
| `scientist-a` | `lettore` | `roles/scientist.md` |
| `scientist-b` | `lettore-b` | `roles/scientist.md` |
| `scientist-c` | `lettore-c` | `roles/scientist.md` |

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

Fields:

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

The local instance file has **not** been created. The laboratory has not been bootstrapped: the
worktrees for the scientists exist under the names `lettore` and `lettore-b`, `lettore-c` does
not exist yet, and no `ORCHESTRATOR_LEASE` has ever been recorded. The first chat to run the
`BOOTSTRAP.md` procedure creates it at step 2.

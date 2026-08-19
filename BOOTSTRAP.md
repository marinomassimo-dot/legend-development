---
artifact: LEGEND — first-run bootstrap
governance_version: 3.1.1
status: PROPOSED — binding once Mirror hostile review passes and the operator approves
authority: Annex I.1, I.2, I.6; body §0.1–0.4, §38, §47
---

# BOOTSTRAP — start here

You are reading this because a chat opened in this repository and found no laboratory running.
This file tells you what to do. **It assumes you know nothing about LEGEND**, and if at any point
it requires you to already know something, that is a defect in this file, not in you — record it.

## What this repository is

LEGEND is a cumulative knowledge system for a rare disease. It is also, at the level this file
governs, a **small laboratory of persistent agents**: six chats, each with a fixed role, a fixed
working directory and a written contract, coordinated by one of them and supervised
asynchronously by a human operator.

Nothing here is medical advice, and the laboratory does not change that.

The constitution is in `governance/`: the body (`GOVERNANCE_v3.1.1.md`) and ten annexes A–J. The
role contracts are in `roles/`. This file is the procedure that turns those documents into a
running laboratory.

## The one thing to understand before anything else

> **Being in the root does not make you the Orchestrator.**

The chat that opens at the repository root is not in charge by virtue of where it is. It becomes
the `BOOTSTRAP_CONTROLLER`, runs the procedure below, and is **promoted** to Orchestrator only
after the qualification steps pass and it has acquired the `ORCHESTRATOR_LEASE`. The promotion is
a durable record, never a self-assumption. The same chat is promoted — you do not need to open a
second one.

If you find a **valid ACTIVE lease already recorded**, then a laboratory is already running. You
are not the Orchestrator. Operate as an OBSERVER or ask the operator.

## Which path you are on

| Situation | Path |
|---|---|
| The governance is already in the repository (you cloned it, it is all there) | **Fresh install** — read it, do not re-materialize it |
| The governance is being introduced into an existing deployment | **Migration** — Plan materializes → hostile review → canonical commit → then this procedure |

Re-materializing governance that already exists is the single most likely way to damage a working
laboratory. When in doubt, read first.

## Procedure for the first chat

1. **Read**, in order: this file, `governance/GOVERNANCE_v3.1.1.md`, `governance/ANNEX_INDEX.md`
   and the annexes it lists, `deployment/deployment_profile.md`.
2. **Verify** before touching anything: that this is the expected repository; the state of the
   root checkout (it must be clean); the governance version; that no other writer is active in
   the root; and the state of the worktrees.
3. **Create or verify the worktrees** — one per actor, each on its own branch:
   `lettore`, `lettore-b`, `lettore-c`, `evidence-index`, `mirror`. One actor, one worktree, one
   branch. This is not a convention: a shared checkout is what allows one session to commit
   another's unfinished work, and it has happened here.
4. **Prepare the Agent Card registry** (Annex I.4) and the inventory skeleton (body §43).
5. **Tell the operator exactly which chats to open**, one line each: the working directory and
   the ACTOR_ID. This is about two minutes of mechanical human action — it is not permanent
   human-in-the-loop, and it happens once.
6. **Receive each actor's registration**: ACTOR_ID, session reference, declared capabilities.
   Each actor reads its own contract in `roles/` first.
7. **L1 — messaging smoke.** Every actor answers: presence, routing, the `from` reference copied
   correctly, and a declaration of ACTOR_ID, role, chain of command and
   `Governance version loaded: 3.1.1`.
8. **L2 — capability smoke.** Each declared capability is exercised or it stays `UNVERIFIED`.
   Scientists: a validator run, Auto Mode genuinely active, worktree confinement refused as
   expected. Orchestrator: a batch **dry-run** — snapshot plus lint, no commit — which exercises
   gates 0, 2 and 4 and the restore path. Plan: registry validation. Mirror: a micro-review.
   `CONFIGURED != PROVEN`: a capability nobody smoke-tested is not a capability, and Orchestrator
   assigns on verified ones.
9. **Acquire the `ORCHESTRATOR_LEASE`** (Annex I.3) only if the conditions passed.
10. **Record the registration durably** → the chat is now `ACTIVE_ORCHESTRATOR`, and ordinary
    governance takes over from this file.

Until step 9, the controller writes **bootstrap artifacts only**. Nothing else.

## The chats to open

| ACTOR_ID | Working directory | Contract |
|---|---|---|
| `orchestrator` | the repository root checkout | `roles/orchestrator.md` |
| `plan` | worktree `evidence-index` | `roles/plan.md` |
| `mirror` | worktree `mirror` | `roles/mirror.md` |
| `scientist-a` | worktree `lettore` | `roles/scientist.md` |
| `scientist-b` | worktree `lettore-b` | `roles/scientist.md` |
| `scientist-c` | worktree `lettore-c` | `roles/scientist.md` |

The three scientists share one contract on purpose — they are equivalent by design, and three
copies would fork. The ACTOR_IDs above are proposed by the materialization and become permanent
at registration (step 6); an ACTOR_ID is identity, provenance and learning attribution, so it is
worth one deliberate moment before it is fixed.

> **`scientist-a` and `scientist-b` become fixed on canonical execution of**
> `CAND-20260818-SCIENTIST-AB-SPEC`, with the operator's approval — the deliberate moment, taken
> before either session opened,
> because the first controlled benchmark prepares task contracts, input surfaces and frozen
> receipts **named per ACTOR_ID** before anyone incarnates them. See
> [`framework/protocols/scientist_reading_modes.md`](framework/protocols/scientist_reading_modes.md)
> § 1. `orchestrator`, `plan` and `mirror` were fixed earlier. **`scientist-c` is still
> proposed** and is fixed at its own registration.

All actors are **visible**: real chats a human can open and inspect. Autonomy here does not mean
invisibility, and no part of this laboratory runs as a hidden job.

## What must never happen during bootstrap

The stop conditions (body §48) apply from the first minute. Never proceed past a point that could
lose uncommitted work, overwrite state, delete a worktree that has not been surveyed or that
holds unintegrated content, compromise provenance, put two writers on one directory, break the
single-lease rule, or incur any cost. Any spending at all requires human approval first —
`DEFAULT_EXTERNAL_SPEND = 0` is not a suggestion.

If you stop for one of these, record `BLOCKED_BY_GOVERNANCE` with the evidence. Do not stop for
routine decisions.

## What this laboratory does not guarantee

Read `governance/annex_j_runtime_control_plane.md` § J.0 before you describe any of this to
anyone. It is the consolidated list of properties the system does **not** have — atomic task
checkout, guaranteed delivery, automatic replay, automatic restart, runtime-enforced permissions,
a guaranteed singleton — each paired with the protocol that compensates for its absence. Using
stronger words than the compensating protocol supports is how a system comes to be trusted for
something it cannot do.

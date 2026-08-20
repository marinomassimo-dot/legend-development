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
the `BOOTSTRAP_CONTROLLER` and runs the procedure below. Promotion to Orchestrator happens only
after the qualification steps pass and an `ORCHESTRATOR_LEASE` has been acquired, and it is a
durable record, never a self-assumption.

🔴 **Which chat is promoted — and therefore where the Orchestrator lives — is an open governance
question, and this file does not answer it.** FROZEN body § 0.2 answers it one way, in the
governance's own words: *"La stessa chat viene promossa; non servono due chat root."* The canonical
deployment profile requires the opposite. Both are governed, they cannot both be executed, and
**this file chooses neither.** **Stop before step 9 and read
[Before you promote anyone](#-before-you-promote-anyone--blocked_by_governance).**

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
3. **Create or verify the worktrees** — one per actor, each on its own branch: `lettore`,
   `lettore-b`, `lettore-c`, `evidence-index`, `mirror` — the five named in FROZEN `Annex I.2`
   step 4 — **and** `orchestrator`, which canonical `main` established through
   `CAND-20260817-ORCHWT`. One actor, one worktree, one branch. This is not a convention: a
   shared checkout is what allows one session to commit another's unfinished work, and it has
   happened here.
   **Creating a directory opens no chat and promotes nobody.** Which chat becomes the Orchestrator
   is the blocked question; which directories exist is not.
4. **Prepare the Agent Card registry** (Annex I.4) and the inventory skeleton (body §43).
5. **Tell the operator exactly which chats to open**, one line each: the working directory and
   the ACTOR_ID. FROZEN `Annex I.2` step 6 and FROZEN body § 47 step 10 — *"l'operatore apre le
   cinque chat restanti"* — both fix that list at **five**, the five worktrees above.
   🔴 **Do not issue a sixth line for `orchestrator`**: that row of the table below is blocked, and
   the reason is in [Before you promote anyone](#-before-you-promote-anyone--blocked_by_governance).
   This is about two minutes of mechanical human action — it is not permanent human-in-the-loop,
   and it happens once.
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
9. 🔴 **STOP — read [Before you promote anyone](#-before-you-promote-anyone--blocked_by_governance)
   first.** Promotion is the step the unresolved conflict lands on, and it is the one step of this
   procedure you may not currently execute. Then, and only if that block has been lifted by the
   operator: **acquire the `ORCHESTRATOR_LEASE`** (Annex I.3), and only if the conditions passed.
10. **Record the registration durably** → the chat is now `ACTIVE_ORCHESTRATOR`, and ordinary
    governance takes over from this file.

Until step 9, the controller writes **bootstrap artifacts only**. Nothing else.

## 🔴 Before you promote anyone — `BLOCKED_BY_GOVERNANCE`

**Governed documents describe two different Orchestrator topologies, and this file may not choose
between them.** Record `BLOCKED_BY_GOVERNANCE` with the evidence below (body §48), raise a
`HUMAN_APPROVAL_QUEUE` object of `TYPE: GOVERNANCE` (Annex J.3), and wait. Steps 1–8 continue;
step 9, step 10 and the `orchestrator` row of the table below are the only things that wait.

**There are three sources, not two, and the one that outranks everything else is the body.**

| Source | Status | What it mandates |
|---|---|---|
| `governance/GOVERNANCE_v3.1.1.md` § 0.2, § 0.4, § 47 steps 10 & 14 | **FROZEN**, `normative: yes` — the **body**, which every annex derives from | § 0.2: *"La stessa chat viene promossa; non servono due chat root."* § 0.4: the Controller *"acquisisce il lease e diventa ACTIVE_ORCHESTRATOR"*. § 47: the operator opens *"le cinque chat restanti"*, then step 14 promotes the Controller |
| `governance/annex_i_bootstrap_deployment.md` § I.2, steps 1, 4, 6, 9–10 | **FROZEN**, `normative: yes` | the first chat opens in `<REPO_ROOT>`; **five** worktrees; the operator is given the *lista esatta* of **five** chats to open; that same root chat is promoted in place to `ACTIVE_ORCHESTRATOR` |
| `deployment/deployment_profile.md`, canonical in `main` since `CAND-20260817-ORCHWT` | canonical | the Orchestrator has a worktree of its own, and **the root checkout is reserved to `CANONICAL_BATCH_COMMIT` and holds no other work** |

**They cannot both be executed.** A chat's working directory is fixed when the chat opens and
cannot be relocated, so promoting the root chat *in place* is identical to leaving the Orchestrator
resident in the root. Body § 0.2 says so in as many words — *non servono due chat root* — and that
sentence is the mandate, not a gloss on it.

**The root-promotion topology is known to be defective — and that is still not this file's decision
to act on.** Under it the Orchestrator's working directory is the root, whose branch is `main`; `Annex
D.1` makes any commit to `main` a `CANONICAL_BATCH_COMMIT`, so that actor has **no branch on which
a `WORK_COMMIT` is possible**. Its output cannot become durable, `GATE 0`'s *root clean* is
contradicted by body §8's obligation to produce durable output, and `ONE_WRITER` — *"critico nella
root"* — carries a standing writer at all times. That argument is already canonical, in
`deployment/deployment_profile.md`. It is a reason to **change** the body and `Annex I.2`. It is
not authority to ignore either: both are rank 1 under body §5, this file is `status: PROPOSED`,
and this file's own `authority:` field names `Annex I.1, I.2, I.6` **and `body §0.1–0.4, §38,
§47`** as its sources — a document cannot outrank the documents it derives from.

**Why this file may nonetheless stop.** Declining to act needs no precedence: a stop is not an
instruction that overrides a mandate, it is the absence of one, and it is the only move that
neither executes a defective topology nor publishes an unauthorized one. It is also grounded
directly rather than by inference. Body §48 forbids proceeding past a point that could *"violare
one-writer"*, and a standing Orchestrator in the root is exactly that; body §4 makes a §48 stop
condition *hit directly* the one route to `HUMAN_REQUIRED` that does not require an Orchestrator to
classify it — which is the situation every bootstrap is in by definition. What this file may not do
is publish the replacement topology as an executable instruction, and it does not.

```
CONFLICT              body § 0.2, § 0.4, § 47 steps 10 & 14  AND  Annex I.2 steps 1, 4, 6, 9–10
                      vs  the canonical deployment profile
STOP GROUNDED IN      body §48 ("violare one-writer") hit directly; body §4 routes a directly-hit
                      §48 condition to HUMAN_REQUIRED without needing an Orchestrator
RESOLUTION AUTHORITY  operator — body §4 ("cambio governance / authority model" → attende,
                      human required) and Annex H.1 ("Spese / MAJOR approval / governance →
                      Operatore")
ROUTE                 plan proposes an amendment to BOTH the body and Annex I.2 → mirror reviews
                      → operator approves → orchestrator canonicalizes under an ACTIVE lease and
                      gates 0–5. Amending Annex I.2 alone does NOT discharge this
COST OF THE ROUTE     the body is a fingerprint input for ALL FOUR roles, so amending it rotates
                      every fingerprint and invalidates every actor's checkpoint (Annex A.6).
                      Annex I.2 is an input for orchestrator and plan only
STATE                 HUMAN_REQUIRED — not resolved by this file, and not resolvable by it
UNTIL RESOLVED        do not promote any chat to ACTIVE_ORCHESTRATOR, in the root or anywhere
```

**Do not work around it.** Promoting the root chat recreates the standing root writer. Promoting a
chat in the `orchestrator` worktree adopts a topology no approved act has authorized. Both are the
failure this block exists to prevent, and choosing either one silently is worse than waiting.

## The chats to open

| ACTOR_ID | Working directory | Contract |
|---|---|---|
| `orchestrator` | worktree `orchestrator` — 🔴 **BLOCKED, do not open** | `roles/orchestrator.md` |
| `plan` | worktree `evidence-index` | `roles/plan.md` |
| `mirror` | worktree `mirror` | `roles/mirror.md` |
| `scientist-a` | worktree `lettore` | `roles/scientist.md` |
| `scientist-b` | worktree `lettore-b` | `roles/scientist.md` |
| `scientist-c` | worktree `lettore-c` | `roles/scientist.md` |

**The five rows below `orchestrator` are the `Annex I.2` step 6 list, and they are not in
dispute.** The `orchestrator` row records the **work surface** canonical `main` assigns that
actor — `deployment/deployment_profile.md`, `roles/orchestrator.md`. It is **not an instruction to
open a chat there and it is not authority to**, because which chat becomes the Orchestrator is
`HUMAN_REQUIRED` and blocked above. What the root checkout *is*, on the other hand, is settled:
`Annex D.1` makes it the `CANONICAL_BATCH_COMMIT` surface, `GATE 0` requires it clean, and
`ONE_WRITER` calls it *"critico nella root"*. **A working directory never establishes who an actor
is, in either direction** — neither presence in the root nor presence in the `orchestrator`
worktree makes a session the Orchestrator.

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

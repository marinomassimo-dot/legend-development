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

**Which chat is promoted — and therefore where the Orchestrator's session lives — is settled, and
this file answers it.** The root chat is promoted **in place**. FROZEN body § 8 states the
architecture directly — *"Orchestrator vive nella chat grafica associata a `<REPO_ROOT>`"* — and
FROZEN body § 0.2 states the mechanism — *"La stessa chat viene promossa; non servono due chat
root."* Neither sentence is amended by anything in this file.

**Promotion moves no chat and opens no chat.** The session running as `BOOTSTRAP_CONTROLLER`
acquires the lease and continues, in the same place, under a new role. That is why body § 47
step 10 has the operator open *"le cinque chat **restanti**"* — remaining, because the sixth is
the one already open and reading this.

And it changes nothing about authority. Being in the root is still not being the Orchestrator;
the lease is. The two statements sit side by side in § 8 itself, and the second only needs saying
because the first is true.

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
3. **Create or verify the bootstrap worktrees** — exactly the five named in FROZEN `Annex I.2`
   step 4, each on its own branch: `lettore`, `lettore-b`, `lettore-c`, `evidence-index`,
   `mirror`. **Five, and not six.** These are the homes of the five chats step 5 asks the operator
   to open, which is both why the count is five and why `orchestrator` is not among them — that
   actor's session is this one, already open in the root. The `orchestrator` **work surface** is a
   different thing on a different clock: it is provisioned at step 11, after promotion, and it is
   not a bootstrap artifact. See [Two lists, two questions](#two-lists-two-questions).
   One actor, one worktree, one branch. This is not a convention: a shared checkout is what allows
   one session to commit another's unfinished work, and it has happened here.
   **Creating a directory opens no chat and promotes nobody.**
4. **Prepare the Agent Card registry** (Annex I.4) and the inventory skeleton (body §43).
5. **Tell the operator exactly which chats to open**, one line each: the working directory and
   the ACTOR_ID. FROZEN `Annex I.2` step 6 and FROZEN body § 47 step 10 — *"l'operatore apre le
   cinque chat restanti"* — both fix that list at **five**, the five worktrees above.
   **There is no sixth line for `orchestrator`, and its absence is the architecture rather than an
   omission**: that chat is this one, already open in the root, and step 9 promotes it where it
   sits. This is about two minutes of mechanical human action — it is not permanent
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
9. **Acquire the `ORCHESTRATOR_LEASE`** (Annex I.3) — and only if every condition above passed.
   This is the ordinary step FROZEN body § 0.4 and § 47 step 14 describe, taken **in place**: this
   chat is promoted, and no chat is opened or moved to receive the promotion. The lease is what
   confers the authority. The location confers nothing, and never did.
10. **Record the registration durably** → the chat is now `ACTIVE_ORCHESTRATOR`, and ordinary
    governance takes over from this file.
11. **Provision the `orchestrator` work surface** — worktree `orchestrator` on branch
    `orchestrator`, per `deployment/deployment_profile.md`. **This step is new, and it restores
    nothing**: no FROZEN document describes it, because no FROZEN document is describing a runtime
    surface at this point in the sequence. It sits here rather than at step 3 for the reason in
    [Two lists, two questions](#two-lists-two-questions), and it must happen before the
    Orchestrator's first Session Learning Review — body § 8 makes that review mandatory and body
    § 18 makes `WORK_COMMIT` the only route to durable state, *"il messaggio notifica, il commit
    fa fede"*. Owner: `plan`, whom body § 47 step 15 already places at exactly this point on
    runtime matters. **The step's position is normative, not editorial**: moving it before
    promotion reopens a governance question that is closed only because it sits after.

Until promotion at step 9, the controller writes **bootstrap artifacts only** — FROZEN body § 0.4,
*"Perimetro di scrittura pre-promozione: SOLO artefatti di bootstrap."* That perimeter fences the
`BOOTSTRAP_CONTROLLER`, and the Controller ceases to exist at promotion. It is therefore neither a
licence for steps 10–11 nor a bar to them: it has simply stopped applying, and what governs after
promotion is body § 35.1.

## Two lists, two questions

An earlier revision of this file stopped at step 9 and recorded `BLOCKED_BY_GOVERNANCE`, on the
reading that FROZEN governance and the canonical deployment profile described two mutually
exclusive Orchestrator topologies. **That reading was wrong, and the error is worth keeping
written down**, because it is the kind that survives review: three revisions and one hostile
review passed over it.

There was never one list with a disputed length. There were always **two lists answering two
different questions**, and this file was reading them as one:

| | **`Annex I.2` step 4** | **`deployment/deployment_profile.md`** |
|---|---|---|
| Answers | which worktrees must exist so the chats of step 6 have homes | where the Orchestrator's `WORK_COMMIT` lands |
| Rank | **1** — FROZEN, `normative: yes` | canonical content, amendable under Annex D |
| Count | **five, and it is derived** — step 6 hands the operator *"la LISTA ESATTA delle 5 chat da aprire (path per ACTOR_ID)"*, one path per chat | **one, and it is derived** — body § 11, *"ogni attore, PROPRIO worktree/branch"* |
| Clock | bootstrap, **pre**-promotion | runtime, **post**-promotion |
| Established by | the governance body and Annex I | `CAND-20260817-ORCHWT`, whose scope field reads *"deployment/deployment_profile.md ONLY"* |

**`CAND-20260817-ORCHWT` never touched `Annex I.2`, and said so in its own scope field.** The
`orchestrator` worktree entered this system as a deployment fact, not as a bootstrap step. Nothing
was smuggled into the annex, and the annex was never in tension with the profile. The tension was
manufactured here — by an earlier step 3 that named the annex's five and the profile's one in a
single breath, and so presented a runtime surface as a bootstrap artifact.

**The absence is not an oversight.** The five worktrees of step 4 map one-to-one onto the five
chats of step 6, and body § 47 step 10 calls them *"le cinque chat **restanti**"*. The Orchestrator
has no worktree at step 4 for exactly the same reason it has no chat at step 6: **its session is
the root chat, already open, promoted in place.** Read against the architecture, the FROZEN
cardinality of five is not a gap to be argued around. It is the architecture, stated.

### The two axes this file exists to keep apart

```
SESSION_LOCATION  ≠  PERSISTENCE_SURFACE
ROOT location  ≠  ACTOR_ID  ≠  write authority
```

Both axes are independent, and conflating the first is precisely how the earlier error travelled:
a true statement about where an actor **commits** was turned into a false statement about where its
**session lives**. Step 3 and step 11 are the two halves of the first axis, and they are separate
steps on purpose.

### On the Orchestrator and durable work

The earlier reading also held that a root-resident Orchestrator has *"no branch on which a
`WORK_COMMIT` is possible"*. That is false: a `WORK_COMMIT` is bound to a **branch**, never to a
working directory. The Orchestrator commits its own work on branch `orchestrator`, from wherever
its session is open, and the root stays clean because nothing is written there outside a batch
window.

The rank-1 fence is body § 35.1, and the operator has adjudicated its reading:

> **§ 35.1 constrains where persistent artifacts may be produced, not whether the Orchestrator may
> produce persistent artifacts. The Orchestrator `WORK_COMMIT` surface is the assigned
> worktree/branch, never the root checkout.**

So § 35.1's *"non usare la root come spazio libero"* stands unamended and undiminished, and body
§ 11, § 18 and § 8 — which require every actor including this one to make its work durable — are
satisfied on the worktree. This is why step 11 provisions a surface that is **required** rather
than merely permitted.

## The chats to open

Two columns, because the `orchestrator` row carries two facts that an earlier revision collapsed
into one and then could not choose between.

| ACTOR_ID | Session home | Work surface | Contract |
|---|---|---|---|
| `orchestrator` | the repository **root** checkout — **already open; not opened at step 5** | worktree `orchestrator`, branch `orchestrator` — provisioned at step 11 | `roles/orchestrator.md` |
| `plan` | worktree `evidence-index` | same | `roles/plan.md` |
| `mirror` | worktree `mirror` | same | `roles/mirror.md` |
| `scientist-a` | worktree `lettore` | same | `roles/scientist.md` |
| `scientist-b` | worktree `lettore-b` | same | `roles/scientist.md` |
| `scientist-c` | worktree `lettore-c` | same | `roles/scientist.md` |

**The five rows below `orchestrator` are the `Annex I.2` step 6 list**, and for those five actors
the two columns hold the same value — which is why every other role contract needs one field and
this one needs two.

What the root checkout *is*, on the other hand, is settled and unchanged by any of this:
`Annex D.1` makes it the `CANONICAL_BATCH_COMMIT` surface, `GATE 0` requires it clean, and
`ONE_WRITER` calls it *"critico nella root"*. A session lives there; no work is written there
outside a batch window.

**A working directory never establishes who an actor is, in either direction** — neither presence
in the root nor presence in the `orchestrator` worktree makes a session the Orchestrator. The
lease does, and nothing else does.

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

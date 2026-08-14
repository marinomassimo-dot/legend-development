# LEGEND runtime kernel — amendment spec

**Version:** v1.1 (frozen 2026-08-13) · **Governs:** [`legend_launch.sh`](legend_launch.sh),
[`transport.json`](transport.json) and the delegation protocol around them ·
**Status:** frozen for implementation. MC‑1 and MC‑3 are implementable on an
unqualified host; everything else depends on step 0.

The kernel governs **birth and environment** for one actor. The supervisor governs the
session's life. LEGEND adds only the invariants Claude Code does not guarantee, and this
document is the list of those invariants plus the measurement behind each one.

**What it is not.** It is not an actor registry, a router, a broker or a scheduler. Actor and
worktree stay parameters, so a future registry can supply them from a versioned file without
dismantling anything here.

---

## Index

Pointers only. Every claim lives in the entry that carries its measurement, and a summary that
restated them here would separate the claim from its evidence — the surface without
accountability this project has already declined twice.

| theme | entries |
|---|---|
| **identity** | [MC‑1 — cell identity is declared, never derived](#mc1--cell-identity-is-declared-never-derived) · [OB‑4, the name is not an identity](#observation--recorded-no-gate) |
| **lifecycle** | [MC‑3 — two-phase lineage](#mc3--two-phase-lineage-pending_birth--active-created-with-o_excl) · [MC‑6 — recovery is `respawn`](#mc6--recovery-is-respawn-and-a-success-shaped-exit-is-not-evidence) · [`BACKGROUND_RECOVERY_CONTRACT`](#background_recovery_contract--undetermined-and-one-thing-that-is-not) · [the kernel does not guarantee continuation](#the-kernel-does-not-guarantee-continuation--declared-boundary-not-implementation) |
| **messaging** | [MC‑5 — `REACHABLE` vs `OPERATIONAL`](#mc5--51c-reachable-and-operational-are-two-outcomes-never-one-word) · [`RETURN_CHANNEL_PASS`](#return_channel_pass--the-leg-that-had-never-been-observed-observed-once) · [five outcomes, never four](#five-outcomes-never-four) |
| **workspace** | [5.1g — closed, the boundary was never there](#51g--closed-the-boundary-was-never-there-to-be-observed) · [registered candidate: `--worktree` at birth](#registered-candidate-not-to-be-tried-now) |
| **permissions** | [`PERMISSION_WAIT`](#permission_wait--measured-named-by-the-supervisor-and-unanswerable-at-night) · [the register, entry 1](#permission-collection--the-register-entry-1) · [the register needs a sampler](#-the-register-cannot-be-compiled-afterwards--a-requirement-of-the-attended-pilot) |
| **observability** | [`state.json` is not a liveness source](#statejson-is-diagnostic-evidence-never-a-liveness-source) · [an actor cannot report the permission it was blocked on](#-an-actor-cannot-report-the-permission-it-was-blocked-on) · [`SESSION_RUNTIME_DRIFT` and model identity](#observation--recorded-no-gate) |
| **failure taxonomy** | [`MESSAGE_TURN_TRUNCATION`](#message_turn_truncation--a-failure-class-defined-by-its-symptom) · [`PERMISSION_WAIT`](#permission_wait--measured-named-by-the-supervisor-and-unanswerable-at-night) · [self-erasing blocking events — **hypothesis**](#self-erasing-blocking-events--a-hypothesis-with-one-instance) |
| **process** | [decisions of record](#decisions-of-record) · [certification log](#certification-log) · [primitive budget](#primitive-budget) · [open questions](#open-question--resolutions-and-residue) · [execution order](#execution-order) |

## Decisions of record

Both were exercised under explicit delegation: **adjudicated by Fable, ratified by the
operator.** Every receipt that depends on them records them in that form.

**D1 — cell identity.** `LEGEND_RUNTIME_INSTANCE = mac-dev-001` for this machine. The existing
lineage directory migrates as a **registered act**, not an implicit rename: the cell segment
moves inside the existing base (`~/.legend/lineage/AIR-DI-MASSIMO-massimo/` →
`~/.legend/lineage/mac-dev-001/`, no new layout), and each migrated record carries the receipt
— `old_identity`, `new_identity`, `reason: "remove derived runtime identity"`, date, author.

**D2 — executor attribution.** The receipt schema gains `executed_by`, **prospective, no
backfill**: `actor_id` · `executed_by.model` · `origin_model` (when it differs) · `runtime`
(Claude Code version). Authoritative source: the transcript.

**Where the migration receipt lives, and why not in `sync_epochs.jsonl`.** That ledger's schema
is `workspace` · `branch_or_detached` · `current_commit` · `landed_artifacts`: it records **git
refs**. A lineage cell is not a ref, and filling those fields with invented values would be a
plausible predicate answering a different question — the shape
`ADJUDICATE_THE_DEFECT_LIST_BEFORE_BUILDING_THE_GUARD` exists to catch. The receipt therefore
lives **inside the record it describes**, in the same per-cell, unversioned store the kernel
already declares, where a reader asking *"which cell was this actor born on?"* will look.

---

## MUST CHANGE

### MC‑1 — Cell identity is declared, never derived

*Surface: launcher. Blocked by: D1 (resolved).*

**Measure.** One machine, four names:

```
hostname -s                 AIR-DI-MASSIMO
hostname                    AIR-DI-MASSIMO.station      ← router-supplied domain
scutil --get LocalHostName  MacBook-Air-di-massimo
scutil --get ComputerName   MacBook Air di massimo
```

`hostname -s` is **network-derived**. The cell is currently named `AIR-DI-MASSIMO-massimo`, so
it is a function of which network the machine is on.

**Failure mode.** Change network → new cell string → `$HOME/.legend/lineage/<new>/` is empty →
`LINEAGE_EXISTS` cannot fire → **every actor becomes re-birthable**, and nothing detects it.
This is the same failure that rules the runtime version out of the cell key; it was already
present by another route.

**Change.** `LEGEND_RUNTIME_INSTANCE` becomes required and explicit; the
`$(hostname -s)-$(id -un)` fallback is removed. A cell must be **created deliberately**:
`birth` refuses when the cell directory does not exist, so a typo produces a named refusal
instead of a silent fresh namespace.

```
LAUNCH_REFUSED RUNTIME_INSTANCE_UNDECLARED: LEGEND_RUNTIME_INSTANCE must be set
  explicitly — it is the cell identity and must never be derived from the network

LAUNCH_REFUSED CELL_UNKNOWN: no cell '<id>' at <dir> — create it deliberately
  (mkdir -p <dir>) before the first birth on this cell
```

**Test receipt.** (a) invoke with the variable unset → `RUNTIME_INSTANCE_UNDECLARED`, exit 1.
(b) invoke with an invented cell → `CELL_UNKNOWN`, exit 1. (c) invoke with the coined cell →
passes and proceeds to the next precondition.

> **Corrected against the implementation.** v1.1 said (b) and (c) were observable only through
> `check`, because identity was assumed to be judged after the runtime gate. Both identity
> checks were placed **before** it instead — a wrong or absent cell is wrong on a qualified
> host too — so all three receipts fire in the acting modes as well. Asserted in the suite as
> *identity is judged before the runtime gate*.

**Stated residual.** MC‑1 does not *authenticate* a cell. A typo that lands on an existing cell
is still undetected → OQ‑2, optional.

### MC‑2 — The version pin stays a gate; recertification becomes an argued commit

*Surface: launcher (no code change) + process.*

**Measure, already in hand.** `LAUNCH_REFUSED HOST_RUNTIME_UNQUALIFIED: claude 2.1.231 !=
certified 2.1.228`, exit 1, on `check`, `birth` and `resume`. The gate works.

**Change.** None in code. The rule: **the commit that moves `CERTIFIED_VERSION` must state what
was verified on that version** — the checklist below. A bump without it is rejected at review.
This is what dissolves the original objection: recertification is an operator act with an
author, not a silent edit made to turn a suite green.

**What a recertification verifies** (resolution of OQ‑1) — the contract surfaces between kernel
and CLI that have been *measured* to change across versions:

1. the parse of `claude agents --json` (Agent View is a research preview; its schema may move) —
   verified **positively**, i.e. against a name that is actually live, not only against absence;
2. the `--bg` launch contract: exit status, and that the spawned session appears **uniquely** in
   the roster;
3. the default-name semantics — **observation only**, since after MC‑1/OB‑4 the kernel no
   longer depends on it;
4. the order and text of the named refusals: MC‑1's receipts (a)/(b), MC‑3's residue test and
   MC‑2's own regression **are** the smoke test;
5. **that a respawned actor keeps its transport.** `respawn` accepts no `--settings`, so after
   MC‑6 the transport of a *recovered* actor is preserved by the supervisor and not by this
   launcher. Observed in the job's stored `respawnFlags` — a surface that is **not contracted**,
   which is exactly why it belongs on a list that gets re-run rather than assumed.

Executable in minutes, entirely on an unqualified host except one birth/stop cycle.

> **Corrected against the implementation.** Item 2 read *"the parse of `--bg` output (the
> launcher reads the short id from it)"*. It does not: it keeps that output verbatim as spawn
> evidence and resolves the sessionId from the roster, precisely so an uncontracted format is
> never load-bearing. The item was describing a coupling the kernel had already refused. What
> the birth actually exercises is the launch contract above, which is the wider and truer
> surface — and the first run of it also produced the `claude stop <id>` verb, which
> `claude agents --help` does not list and on which the disposition step depends.

**Test receipt (regression).** After every other amendment, on an unqualified host, the string
above must still be produced — and still **before** any location or lineage check, so an
unqualified host leaves no residue.

### MC‑3 — Two-phase lineage, `PENDING_BIRTH → ACTIVE`, created with `O_EXCL`

*Surface: launcher.*

**Failure mode, by inspection — zero observed instances, declared as such.** Line 113 tests
`[ -e "$LINEAGE_FILE" ]`; line 179 writes it; the entire launch sits between them. Chain:
birth succeeds → `LINEAGE_UNRESOLVED` (line 161) or a crash → **session alive, lineage absent**
→ `resume` refused, `birth` **permitted**. While the first session lives, `ACTOR_ALREADY_LIVE`
covers the hole from the roster; **when it dies, nothing does** — and Scientist A died, so the
dangerous branch is the ordinary case, not an exotic one.

**Why nothing smaller works.** Any single-phase form leaves the window open, because the record
that authorises a future refusal is written *after* the irreversible act it is meant to guard.
The minimum is to write what is known before the launch and complete it after.

**Change.** The lineage record is created with `O_EXCL` **before** the launch, in state
`PENDING_BIRTH`, and completed to `ACTIVE` by an atomic `os.replace` once the session id
resolves. `O_EXCL` also closes the concurrent-birth race, which the `[ -e ]` test cannot.

**N1 — two flavours of pending, and the refusal must distinguish them.** *"A pending holds no
session id, so `rm` is safe"* is true only for a **bare** pending (crash before spawn). In the
`LINEAGE_UNRESOLVED` branch the launcher is alive **after** the spawn: it must **annotate** the
pending — captured short id plus reason — before exiting. An annotated pending means a session
may exist, and a blind `rm` would destroy the only pointer to its transcript, letting the
historical duplicate back in through the door MC‑3 closes.

```
LAUNCH_REFUSED LINEAGE_RESERVED: <actor> has a PENDING_BIRTH record on <cell>.
  bare      — no session was spawned; the record holds no session id, so
              deleting <file> is safe. An ACTIVE record is not: never delete one.
  annotated — a session may exist (short id <id>, reason <why>). Check
              `claude agents --json` and the transcript store BEFORE removing:
              this record is the only pointer to it.

LAUNCH_REFUSED LINEAGE_UNBOUND: <actor>'s lineage is PENDING_BIRTH —
  there is no session id to resume.
```

The asymmetry is written into the refusal on purpose: a fail-closed state whose only exit is
`rm` **will** be exited with `rm`, so the refusal must say which `rm` is safe and which is not.

**Test receipt.** The crash is **not simulated by crashing** — it is simulated by its residue.
Construct each pending flavour by hand and verify: bare → `birth` gives `LINEAGE_RESERVED`
(bare text), `resume` gives `LINEAGE_UNBOUND`; annotated → `birth` gives `LINEAGE_RESERVED`
(annotated text, naming the short id), `resume` gives `LINEAGE_UNBOUND`. All exit 1, all on an
unqualified host. **Zero fault injection, zero new primitives.** The concurrency receipt — two
simultaneous births, exactly one proceeds — needs a qualified host and depends on step 0.

**What the amendment buys.** It converts an *undetectable* hole into a *named block*. That is
the whole value; it does not make a crash impossible.

### MC‑4 — `DECISIVE_PROBE_FIRST`

*Surface: [`framework/eval/learned_gates_registry.md`](../framework/eval/learned_gates_registry.md), not the launcher.*

**Measure.** Scientist A executed five of six commands and stopped at the fifth. The sixth was
the decisive probe, so the arm the experiment existed for is `UNDETERMINED`.

**Rule.** A probe is ordered by **falsifying power**, not by narrative order.

**N2 — "first" means first among what is interpretable.** The decisive probe stripped of its
minimum context is not a datum: an outcome for the cross-worktree probe without `pwd` and
`git rev-parse --show-toplevel` does not say *from where* it was emitted. The precise ordering
is therefore: **minimum interpretive prefix → decisive probe → the remainder.** For branch (a):
`pwd` + `--show-toplevel` → the cross-worktree probe → the other three.

Every step stays independently reportable, so a truncation leaves a usable partial. Every
delegation carries a **completion token**; its absence is `UNDETERMINED`, never a substantive
outcome.

> 🔴 **The operative constraint is the round-trip, not the narrative order:
> `DECISIVE_PROBE_IN_FIRST_INTERPRETABLE_ROUND_TRIP`.** Measured 2026‑08‑14: on the re-ordered
> probe, `pwd` and `git rev-parse --show-toplevel` were emitted **in the same `requestId`**
> (`req_011Ce1Qkg4XNzUc2Tix6SWX4`) — the model batched the whole interpretive prefix into one
> response. The decisive probe would therefore have fallen in the **next** round-trip, which was
> never requested or emitted. Reordering the list inside the prompt could not have helped, and
> that is why it bought nothing. **The rule: wherever technically possible, the minimum context
> needed to interpret the measurement and the decisive measurement itself must sit in the first
> usable round-trip.**
>
> 🔴 **And a known constraint that must be registered alongside the rule, because it makes the
> obvious fix ambiguous.** A worktree-isolated session refuses a *composite* command with
> *"too complex to verify that it stays inside the worktree"* — measured repeatedly in this
> session. So a future probe that packs prefix and decisive step into one command risks a
> refusal that could be **either** the native cross-worktree guard **or** the
> complex-command/isolation guard, and the two are the very thing the probe exists to tell
> apart. **No corrective is designed here.** The constraint is recorded so that the next probe
> is designed to discriminate the two classes rather than to collide with them.

> 🔴 **Superseded the same day it was written, by the first probe that actually returned:
> `DECISIVE_RESPONSE_IN_EARLIEST_REACHABLE_EXECUTION_PATH`.** The rule above demands the
> decisive output in the *first* round-trip. Measured 2026‑08‑14 on the return-channel test:
> that is **not reachable** for a response, because `SendMessage` is a **deferred** tool in the
> actor's session — the schema is not loaded, so a `ToolSearch` resolution necessarily precedes
> it and consumes a round-trip of its own.
>
> ```
> req_011Ce2MxQcL6rER3NpDZ1Ut8   thinking + ToolSearch(select:SendMessage)
> req_011Ce2MyEioD7mokxwdQhkhc   SendMessage → TOKEN-RETURN-001
> ```
>
> **The corrected rule keeps the constraint instead of dissolving it:** the decisive output goes
> in the **earliest execution path the session can actually reach**, and *every round-trip
> required before the decisive action must be known, declared and separable*. It is emphatically
> **not** "whenever the system feels ready" — the number of technical hops stays a **variable to
> be measured**, per delegation and per session, not an excuse. The earlier form is kept above
> because it is why the round-trip became the unit at all; it was the right unit and the wrong
> ordinal.

**Test receipt.** Not a launcher refusal but a review refusal: a probe placing its decisive
measurement after avoidable steps is rejected before dispatch as
`PROBE_REJECTED DECISIVE_PROBE_NOT_FIRST`.

### MC‑5 — 5.1c: `REACHABLE` and `OPERATIONAL` are two outcomes, never one word

*Surface: probe protocol. Also resolves OQ‑3 for `check`.*

| | asserts | measured by | does **not** assert |
|---|---|---|---|
| `REACHABLE` | exists, is discoverable, is addressable | present in the roster; resolvable to a handle; a send returns `success: true` | **nothing about acceptance** — a refusal on arrival is silent to the sender |
| `OPERATIONAL` | executes turns, the background lifecycle holds, the transport is effective | the turn produces output **and** the completion token returns **to a live address** | not a property of the actor: a property of the **pair**, at that moment |

`REACHABLE` does not imply `OPERATIONAL`. This is the same two-named-outcome schema already
used for `WORKTREE_LOCATION_PASS` / `NATIVE_CROSS_WORKTREE_GIT_GUARD` — reapplied, not
reinvented (`PATTERN_ALREADY_SOLVED_GATE`).

**`check` reports everything; `birth` and `resume` die at the first refusal** (OQ‑3). `check`
exists to diagnose, and the measurement that decides it is our own: on an unqualified host
`check` currently diagnoses nothing else, because it dies at the version gate. It therefore
runs **all** preconditions and reports per item, with a non-zero exit if any failed. The
acting modes stay fail-closed at the first refusal.

**Test receipt.** Declaring `OPERATIONAL_PASS` on the strength of a send's `success: true` is
refused: `EVIDENCE_CLASS_MISMATCH: delivery is not acceptance`.

---

## OBSERVATION — recorded, no gate

**OB‑1 · `SESSION_RUNTIME_DRIFT`.** Six CLI versions inside one session lineage, 2026‑08‑08 →
2026‑08‑13; last gap 28 minutes; `2.1.230` never present here. This is **not a launcher
feature**: a manual resume happens without it, so the launcher cannot be the only observer. The
authoritative measurement is the `version` field of the transcripts. Zero new primitives — a
measurement procedure, not a mechanism.

**OB‑2 · Model execution identity.** Scientist A was born `claude-fable-5` and switched to
`claude-opus-5` mid-instruction — `subtype: model_refusal_fallback`,
`apiRefusalCategory: "bio"`, `scope: session` — inside a repository whose subject matter *is*
biology. **Work attributed to an actor may have been executed by more than one model, silently.**
A receipt that names the actor does not name the executor. Addressed prospectively by D2.

**OB‑3 · The return socket dies with the process.** The probe to Scientist A carried
`from="uds:/tmp/cc-socks/1265.sock"`; the requester's socket is now `6131.sock`. Even a
complete reply would have gone to an address that no longer exists: the round trip was broken
**before** the truncation, for an independent reason.

> **Every delegation writes its deadline into durable state. At the deadline, if no reply has
> arrived, the outcome is adjudicated from the transcript. The message is the accelerator; the
> transcript is the truth.**

What is persisted is the `sessionId` and the transcript path — **never the name and never the
socket**, both of which are valid only while that process lives.

**OB‑4 · The name is not an identity.** Three values for one `sessionId` within 24 hours, with
an inconsistent base (repo, then worktree, then repo). `--name` remains a **liveness**
requirement — it makes an actor findable — and is never a persistable address.

---

## `MESSAGE_TURN_TRUNCATION` — a failure class defined by its symptom

**Symptom, and the whole definition:** tool calls emitted → tool results returned and **not**
interrupted → **no subsequent assistant request or continuation.**

It is defined by the symptom because the two instances observed so far have **different
mechanisms and the same shape**, and a class defined by cause would have missed the second:

| date | mechanism | what the transcript shows |
|---|---|---|
| 2026‑08‑12 | `model_refusal_fallback`, `apiRefusalCategory: "bio"`, `scope: session` | the record exists, at the fifth of six commands |
| 2026‑08‑14 | **none of the above** | one `requestId`, thinking + two `tool_use`, both results `interrupted: false`, a `todo_reminder` attachment with 0 items — then nothing |

**Sub-cause of the 2026‑08‑14 case: `UNKNOWN`, and it is obligatory.** What the evidence excludes
or does not support:

| candidate | verdict | on what |
|---|---|---|
| `TOOL_WAIT` | excluded | both results returned, `interrupted: false` |
| `PERMISSION_WAIT` | excluded structurally | no pending tool call to approve — the decisive command was never emitted; `permissionMode: default`; the job dir holds only `state.json`, `timeline.jsonl` and an empty `tmp/` |
| `MODEL/SAFETY_INTERRUPTION` | not supported | no `model_refusal_fallback` on the turn. A **strong** absence, not a generic one: this same session demonstrably writes that record type, on 2026‑08‑12 at 22:00:48.420Z |
| `SUPERVISOR/QUEUE_WAIT` | not supported | `inFlight: {tasks: 0, queued: 0, kinds: []}` |

What these surfaces **cannot** distinguish: whether the continuation was never *generated*, never
*requested*, or generated and *lost*. Three different worlds, one identical set of records — so
`UNKNOWN` stays.

**Scientist A's overnight death is a SEPARATE event.** She was alive and stalled at the deadline;
by the next morning the roster reported **`failed`**. The transition happened afterwards and its
cause is `UNKNOWN`. It is not the truncation, and it must not be called an idle-stop: the observed
state is `failed`, not `stopped`. It informs 6.A without resolving it.

## `RETURN_CHANNEL_PASS` — the leg that had never been observed, observed once

**n = 1. No generalisation beyond the measured case.** Until 2026‑08‑14 the chain
*Orchestrator → Actor → execution → **response*** had three proven legs and a fourth never seen:
33 inbound messages had reached this session in its lifetime, **all from interactive peers,
none ever from a launcher-born background actor.**

Measured, in order, on Scientist A recovered through the declared lifecycle:

| leg | evidence |
|---|---|
| recovery | `RECOVERY_PASS` — same sessionId `2e2571b7-…`, `kind: background`, same cwd, new pid 5064 |
| delivery | A's transcript record 51, `2026-08-14T08:56:21.166Z`, envelope `from uds:/tmp/cc-socks/2475.sock` |
| emission | record 57 `SendMessage`, `to: "uds:/tmp/cc-socks/2475.sock"`, `message: "TOKEN-RETURN-001"`; record 58 result `success: true`, `msg_id e59077e1-…` |
| arrival | received at this session from `uds:/tmp/cc-socks/5064.sock`, `from-name: scientist-a` — and `5064` is A's pid in the roster |

**Addressing by envelope is proven:** A copied the `from` field verbatim, with no `ListAgents`
and no discovery — which is what kept the return inside two round-trips instead of three.

### The obligatory qualification: it was not the first round-trip

Two requests, not one, and the token left in the second. `SendMessage` is a **deferred** tool in
that session: it exists, it is registered, and it is **not callable until its schema is fetched**.
A declared this herself, unprompted, before the requestIds were measured.

So both statements are true and neither cancels the other: **the channel works**, and **the
channel is proven to depend on the one surface that has failed twice** — the second round-trip is
exactly where `MESSAGE_TURN_TRUNCATION` struck on 2026‑08‑12 and 2026‑08‑14's earlier probe.
Today it held. Nothing in this measurement says it always will.

### Five outcomes, never four

`TOOL_DEFERRED` is a class the earlier matrix had no cell for, and it is the cell we landed in.

| class | meaning |
|---|---|
| `PASS` | emitted and arrived |
| `TOOL_DEFERRED` | the tool exists and is available, but a resolution/loading phase must precede execution — **latency and order of availability** |
| `TOOL_UNAVAILABLE` | the capability is **absent** from the session or not exposed to the actor class |
| `NOT_EMITTED` | the tool was reachable and no call was made |
| `EMITTED_NOT_ARRIVED` | the call was made and nothing reached the receiver |

🔴 **Never merge `TOOL_DEFERRED` with `TOOL_UNAVAILABLE`.** The first is a cost to be budgeted in
the execution path; the second is a missing capability that no amount of waiting supplies. Reading
the first as the second would have declared background actors incapable of replying, on the day
one replied.

**`TOOL_REFERENCE_WARMTH_OBSERVATION`** — after that first use, A may now hold the tool reference
already resolved. **This is an observation, not a mechanism, and it is deliberately not called
warm-up:** a future measurement must separate three cases that today are one — *same session after
first use*, *respawn of the same session*, and *a fresh background session*. Only the third
answers whether the deferred cost is structural for the actor class.

### Two measurements kept open, at zero cost, documented and not executed

1. **Deferred comparison.** Is `SendMessage` immediately available in an interactive session
   (Plan, Orchestrator) while requiring a `ToolSearch` in a background one? Both halves are
   observable from transcripts already on disk. No generalisation until both are read.
2. **Truncation rate.** N identical token delegations, reporting *completed · truncated ·
   not emitted · not delivered*. The useful result is **an observed rate, not a boolean** — one
   success and two failures are three data points about the same channel, and a single PASS is
   not a property.

## `PERMISSION_WAIT` — measured, named by the supervisor, and unanswerable at night

2026‑08‑14. A delegation was delivered to a recovered background actor at `09:31:55.033Z`
(`queue-operation` ×2, then the `user` record). **Nothing followed for 241 s** — no `requestId`,
no assistant record, no tool call. The roster then carried a field that had never appeared in
any earlier measurement:

```
state: blocked · status: waiting · waitingFor: "permission prompt"
```

Read verbatim off the actor's own screen, read-only and without attaching:

```
Bash command
git -C /Users/massimo/Desktop/legend-public status --short; echo "EXIT=$?"
Read-only git status in shared checkout

This command requires approval
Do you want to proceed?
❯ 1. Yes
  2. Yes, and don't ask again for: git -C /Users/massimo/Desktop/legend-public status --short
  3. No
```

**It is the ordinary approval dialog**, and the text is what separates the candidates:

| candidate | verdict |
|---|---|
| isolation guard that *asks* instead of refusing (`GUARD_PROMPTED`) | **refuted** — the isolation refusal seen in this session is a refusal with explicit wording, never a Yes/No question |
| permission mode `default` with no rule covering the command | **confirmed** |
| LEGEND's own Bash guard | **refuted by reading it**: it touches git only for blanket staging (`add -A` / `add .` / `commit -a`); no `-C`, no worktree logic |
| editor integration | not implicated — the dialog is the standard CLI one |

**Intra-session comparative evidence, which is what makes this specific rather than general.**
Same session, same `permissionMode: default`: on 2026‑08‑13 `pwd` and
`git rev-parse --show-toplevel` ran **with no prompt at all**; on 2026‑08‑14 `git -C <shared
checkout>` prompts. **Not a permissions problem in general — a property of the target outside
the worktree.**

### 🔴 Two corrections this reading forces on entries written above

**A tool call awaiting permission does not appear in the transcript.** The `MESSAGE_TURN_TRUNCATION`
entry excludes `PERMISSION_WAIT` for the 2026‑08‑13 case *"structurally — no pending tool call to
approve"*. That premise is **false**: the `tool_use` record is written after approval, so its
absence proves nothing about a pending call. The exclusion did not hold.

**And the measurement that would have answered it was filtered out by the measurer.** On
2026‑08‑13 the roster was printed as `state`, `status`, `pid` — a selective projection. `waitingFor`
exists today and was never asked for then. The 2026‑08‑13 sub-cause stays `UNKNOWN`, because that
process is gone — but the *reason for the ignorance* is now known, and it is the same
plausible-predicate shape this repository keeps catching: something was measured, not the thing.

### The remedy is configuration, and it is already specified

Capability per role, explicit denies and an allow-list inside the launcher's `--settings`,
pre-approved permissions for unattended workers — §3.3 of the plan, **specified and never
configured**. A home-grown policy engine would be exactly the alternative mini-runtime the
declared boundary forbids. Nothing is built here.

🔴 **Architectural note, and it holds regardless of how this resolves: an always-on machine does
not solve this class — it prolongs it.** A VPS means the prompt hangs *longer*, not that anyone
answers it. The condition for unattended operation is not "hardware that stays alive" but
**"no execution path can stop on a question."**

## 5.1g — CLOSED. The boundary was never there to be observed

Three delegations over three days tried to measure whether the harness refuses a background
actor's reach into the shared checkout. Two truncated. The third, run under an approved prompt,
reached the end:

| axis | result |
|---|---|
| `CMD_RESULT` | record 68 `TOOL_USE[Bash]` → `git -C /Users/massimo/Desktop/legend-public status --short; echo "EXIT=$?"`; record 69 `toolUseResult {"stdout": "EXIT=0", "stderr": "", "interrupted": false}` — **exit 0, working tree clean, and the actor read it** |
| `NATIVE_CROSS_WORKTREE_GIT_GUARD` | **`NOT_OBSERVED`** |
| return path | **2 round-trips** — `req_…QfhsXs` (Bash), `req_…SLhn2k` (SendMessage), plus a closing text request. **No `ToolSearch`: the tool reference was warm** |

🔴 **And this time `NOT_OBSERVED` is not an absence to interpret, because the cause was measured
upstream.** The daemon roster's dispatch for that actor carries **`"isolation": "none"`**. Nothing
could have refused. The two truncated probes were never capable of producing a refusal — they were
measuring a boundary that does not exist for that actor class.

**The third property of the triad is measured absent.** *The worktree exists ≠ the session was
launched there ≠ the harness enforces its boundary.* For a launcher-born background actor the
third term is `none`, so **"one actor, one worktree" is DISCIPLINE, not an enforced boundary** —
it holds exactly as long as the actor honours it, and nothing detects a breach.

**Evidence level, declared:** a field of an internal, non-contracted surface. Read to *understand*,
never to *decide* — which is why the launcher still refuses to parse it. Corroboration taken from
the same read: `mode: "resume"`, `restoresTranscript: true`, `fork: false`, confirming MC‑6 from
the supervisor's own record. Noted and deliberately not built upon: the daemon roster reports
`pid 5059` where `claude agents --json` reports `5064` — two surfaces, two pids; liveness stays on
the documented one.

### The approval, and why it is part of the measurement

Granted by **the operator**, via `claude attach 2e2571b7`, **option 1**, landing immediately before
`09:53:50.932Z` — **21 min 52 s** after the call was emitted. Option 2 was forbidden and unused,
for two reasons kept on record: it would alter configuration as a side effect of a measurement,
and *"don't ask again"* writes into the **main checkout's** `settings.local.json`, applying to
**every worktree** — a global permission for every actor, granted by one click inside a probe.

🔴 **The approval existed only because the pilot is attended.** At 3 a.m. that gesture does not
happen, and the call is still sitting there in the morning. That is the finding, not the footnote.

### 🔴 An actor cannot report the permission it was blocked on

A's own report states *"no permission prompt, no hook intervened"*. **It is false, and it is not
her fault:** the prompt existed — read verbatim off her screen, named by the roster as
`waitingFor: "permission prompt"`, and measured by the 22-minute gap between records 68 and 69 —
but **nothing about it appears in her transcript**. Approval happens outside the actor's flow, so
from inside, the command simply succeeded.

**Direct consequence for the capability profile: it cannot be collected from actor self-reports.**
Asking an actor *"did you hit any prompts?"* returns `no` **precisely on the events worth
collecting**. The source must be the roster's `waitingFor` and the prompt surface. Same shape as
the two corrections recorded above: the transcript holds the answer and not the question.

### Permission collection — the register, entry 1

```
command    git -C /Users/massimo/Desktop/legend-public status --short
actor      scientist-a · background · isolation: none · permissionMode: default
context    read-only probe against the shared checkout, attended pilot
outcome    APPROVED (option 1) by the operator, after 21m52s of waiting
source     roster waitingFor + the prompt surface — NOT self-report
status     request observed · no permission written
```

Every prompt raised during the attended pilot is a candidate line. The night's allow-list is
**derived from measured use, never from an imagined list.** No policy engine, no permission
written.

### 🔴 The register cannot be compiled afterwards — a requirement of the attended pilot

`waitingFor` exists **only while the actor is blocked**. Measured once the prompt was answered:

```
roster now       state: "done" · status: "idle"      → waitingFor GONE
job timeline     working 08:56:32 · blocked 08:56:43 · done 09:54:08
                 — no entry at all for the 09:31→09:53 block; it jumps from a
                   "blocked" that describes waiting on the requester, straight to "done"
```

**Neither surface retains the event.** What survives is the 22-minute gap between transcript
records 68 and 69 — a timing inference, not a record, and one that cannot separate *waited on a
prompt* from *the command was slow*. And the only persisted narrative is worse than silence: the
`text` of the timeline's `done` entry carries the actor's own sentence, *"no refusal, no
permission prompt, no hook"* — **the sole durable account of the event asserts the prompt never
happened.**

**Requirement, recorded and not built:** the register needs a **sampler** that polls the roster at
intervals while the pilot runs and writes `command · actor · wait-start · wait-end`. Without one,
only prompts a human happened to watch live are collected — which is the census the correction
above just demolished, rebuilt by hand.

**And the sampler has a resolution, so write the size down:** a prompt raised and answered between
two samples is invisible, so the polling interval is the lower bound on what can ever be caught.
An attended pilot answers quickly, which is precisely when the events are shortest and hardest to
sample — the interval must be declared with the data, or a sparse register will read as a quiet
system.

**Row zero, already in hand:** 21 min 52 s of waiting on a *read-only* `git status`, with the
operator present and waiting for exactly that. If the cheapest possible command costs that, the
register's first lesson is not which permissions to grant but **how much a single unanswered
question costs.**

### Self-erasing blocking events — a hypothesis with one instance

**Measured instances: one.** A permission prompt blocks an actor, is answered, and leaves no
record in either the roster or the job timeline. It is tempting to call this a *class* of
blocking event and start designing for it. **That would be a frequency inferred from n = 1**,
which this registry forbids by name.

So it is recorded as a **hypothesis with a candidate list**, and each candidate carries the
measurement that would promote it. The confirming observation is uniform and cheap: **`waitingFor`
carrying a value other than `"permission prompt"`**, followed by that value leaving no durable
trace once resolved.

| candidate | status |
|---|---|
| rate limit | not measured |
| API timeout | not measured |
| tool initialisation | not measured |
| network wait | not measured |
| model queue | not measured |
| unavailable resource | not measured |

Until at least one of these is observed with its own `waitingFor` value, the statement stands at:
*one blocking event is known to erase itself.* Not *blocking events erase themselves.*

### 🔴 The actor's perspective is not the system's

**An orchestrator cannot ask an agent why it is stuck.** The agent will answer, accurately, about
its own experience — and that experience is *incomplete with respect to the system*, in ways the
agent has no way to detect. The actor here reported no permission prompt because none appears in
its record; from inside, the command simply took a while. Nothing was concealed and nothing was
mistaken: two vantage points, one of which cannot see the event.

This sits beside the rule about the timeline's `text` field, and they are the same rule from two
sides: **an actor's account is testimony, not instrumentation.** Testimony is worth having — it
carries intent, reasoning and the qualifications an instrument never records, and this actor's own
unprompted disclosure about the deferred tool is exactly that value. But it is never the census,
never the liveness source, and never the answer to *why did you stop*. For that, read the surface
that observes the actor rather than the one the actor writes.

### Registered candidate, not to be tried now

If isolation is a property of the **dispatch**, it may be requestable **at birth**: the
`--worktree` flag is documented and the dispatch already carries an `isolation` field. Birth with
the flag, rather than `cd` plus a plain birth, is what would turn the discipline into an enforced
boundary for background actors. **Associated future measurement:** a dispatch with
`isolation ≠ none` **and** a cross-worktree probe that is refused — both halves, or neither.
No implementation, no change to the launcher.

## The kernel does not guarantee continuation — declared boundary, not implementation

*Operator decision, by delegation.*

The model ↔ tool ↔ supervisor loop is the **supervisor's** responsibility. LEGEND **detects**
non-completion, **adjudicates** from durable state and the transcript, and **recovers** only when
the lifecycle authorises it. Guaranteeing continuation would mean coupling to uncontracted
internals and turning this kernel into an alternative mini-runtime.

Detection already exists and has been measured: a durable deadline, a completion token, transcript
adjudication, and `UNDETERMINED` when the token is absent. Recovery uses primitives already
measured — but it is **not automatic at the deadline**:

```
deadline expired
    → transcript adjudication
    → check the actor's lifecycle
        if FAILED or STOPPED:  respawn by job id
                               → verify SAME session / kind / roster
                               → RECOVERY_PASS
                               → optional re-delegation
        if still alive / blocked / waiting:  DO NOT respawn.
                                             Adjudicate the stall first.
```

🔴 **`TIMEOUT ≠ RESTART AUTHORIZATION`.** An expired deadline says the work was not completed. It
does not demonstrate that the actor should be restarted — and restarting one that is still alive
destroys the stall that is the only thing worth measuring. **Zero new primitives; no continuation
mechanism is built.**

### `state.json` is diagnostic evidence, never a liveness source

Measured the same morning: the job's `state.json` still read `state: "working"`, frozen at
`2026‑08‑13T21:53:22Z`, while the supervisor's roster reported Scientist A as `failed`.
**The stale surface is the one that reads healthy** — a reader consulting the internal store would
have concluded she was working. Canonical lifecycle is whatever the supervisor's documented
surface exposes; the internals are useful only to understand *what happened*, never to adjudicate
alive or dead. This is the same rule already applied when the launcher refused to parse
`~/.claude/daemon/roster.json`, arriving from the other direction.

## OPEN QUESTION — resolutions and residue

| | question | resolution |
|---|---|---|
| OQ‑1 | what a recertification verifies | **Resolved** — the four contract surfaces listed under MC‑2, committed with the bump |
| OQ‑2 | authenticating a coined cell id | **Optional.** Candidate: write a `CELL` file holding the id inside the cell directory at coining time and cross-check env against file, so landing on the wrong cell requires two independent and mutually consistent typos. One line, zero primitives. **Adopted only if MC‑1's implementation reveals a concrete ambiguity** |
| OQ‑3 | should `check` die at the first refusal | **Resolved** — folded into MC‑5: `check` reports all, actions stay fail-closed |
| OQ‑4 | the executor in the receipt schema | **Resolved by D2** — `executed_by`, prospective, no backfill |
| OQ‑5 | the launcher as sole entry point | **Rule, not mechanism.** (i) birth and recovery go through the launcher; (ii) the real residual exposure is manual CLI resumes — the lifecycle supervisor preserves configuration [DOC], so the ordinary case does not degrade; (iii) partial after-the-fact detectability from the transcript (version jumps, OB‑1) — an audit candidate, never a gate; (iv) the transport guarantee is declared for what it is: **per-launch, not per-life** |

---

## Primitive budget

```
launcher    +5 refusals  RUNTIME_INSTANCE_UNDECLARED · CELL_UNKNOWN ·
                         LINEAGE_RESERVED · LINEAGE_UNBOUND · LINEAGE_UNREADABLE
            −1 refusal   CWD_MISMATCH, removed
            +1 record field  state: PENDING_BIRTH | ACTIVE   (+ annotation on pending)
             0 new verbs · 0 new files · 0 new configuration surfaces
            −1 derivation removed (hostname/id)
protocol    +5 gates registered in the existing learned_gates_registry
            +2 named outcomes reusing a schema already in use
             0 new ledgers
```

> **The budget said +4 refusals; the implementation spent +5 and refunded one — net +4, but the
> composition changed and that is the part worth recording.** `LINEAGE_UNREADABLE` was needed
> because a record that cannot be interpreted must refuse rather than be overwritten: the
> alternative was to *derive* a state for it, and deriving a state is how a record that may
> point at a live session gets treated as disposable. `CWD_MISMATCH` was removed because it
> could not fail — it compared `pwd -P` after `cd` against the same path resolved the same way,
> and still printed a reassuring line every run. **A control that cannot fail is not a control;
> it is a claim of verification.** The net figure was not the reason for either decision, and
> reshaping the work to hit a number written yesterday would have been the failure this
> repository names in its own growth rules.

**Rejected, with reasons.** `launch/certification.json` — the constant already lives in a
versioned file with `git blame`; a second file adds surface without adding accountability.
A `recover`/`adopt` verb — a bare pending holds no session id so its safe disposal is already
`rm`, and a session that has already died is unadoptable, which is the case we actually had.
Folding the runtime version into `runtime_instance` — fragments the lineage namespace and makes
every actor re-birthable at the first upgrade, the identical failure MC‑1 removes. Fault
injection for the crash test — the state machine is testable from the residue.

---

## Certification log

Every entry is the record MC‑2 requires: a version is certified by an act with an author, and
the act is this checklist run on that version.

### `2.1.231` — certified 2026-08-13

Authorised as a controlled qualification birth: throwaway actor `qualification-probe`, dedicated
scratch cell, **never** Scientist A and never the `mac-dev-001` cell, because the next experiment
on A is a recovery and the two must not mix. `LEGEND_CERTIFIED_VERSION` was overridden for the
run and is declared as an instrument of the certification: **verifying a version requires
executing it.**

| surface | evidence |
|---|---|
| 1 · roster parse | positive hit on a live name: `ACTOR_ALREADY_LIVE legend-public-04 (e35c9be1-… 6260)` — the row was found, and sessionId and pid extracted |
| 2 · launch contract | `claude --bg` exited 0; output captured verbatim; **exactly one** roster row carried the name; the resolved sessionId `2d2c3b77-5144-4db2-aab9-74b3fddf7f67` matched the record |
| 3 · default names | observation: three values for one unchanged sessionId in 24h. The kernel does not depend on it |
| 4 · refusal order and text | 28 assertions plus the receipts of MC‑1 and MC‑3, all produced on this host |

**The lineage transition was observed, not inferred** — a sampler recorded every distinct state
the record ever held:

```
t+0.000s   <absent>
t+9.385s   PENDING_BIRTH   reserved_by_pid 11006
t+10.601s  ACTIVE          session_id 2d2c3b77-5144-4db2-aab9-74b3fddf7f67
```

**The reservation existed for 1.216 s.** That interval is the window MC‑3 was built to cover, and
it is now a measurement rather than an argument.

**Disposition.** Session stopped with `claude stop 2d2c3b77`; absence verified in the active
roster and `state: "stopped"` with **no `pid`** under `--all`, which is the field the liveness
predicate keys on. The test lineage record was retired rather than deleted, and the cell then
re-checked through the same decision function, which reports `ABSENT`.

> **It is a SCRATCH qualification artifact, not an archive.** The record lives in a temporary
> scratchpad, so calling it archived would promise a durability it does not have. **The durable
> receipt is this commit.** The distinction matters because the reason for keeping the record
> was that it evidences the certification — and evidence stored where it can evaporate is the
> failure this repository has already paid for once, when a `MANIFEST STRICT PASS` was certified
> in a temporary workspace that then disappeared.

**Defense in depth, not a substitute for the measure.** Had the launch contract moved, the birth
would have ended in `LINEAGE_UNRESOLVED` and left an *annotated* reservation — a named block
rather than an invisible duplicate. That is a property of MC‑3, and it is why an unverified
surface would have been survivable; it is not why this one is certified. This one is certified
because it was run.

## `BACKGROUND_RECOVERY_CONTRACT` — UNDETERMINED, and one thing that is not

Second qualification act, 2026‑08‑13, same throwaway subject, never Scientist A. The launcher's
`resume` branch runs `exec claude --resume <id> --settings <transport>` with **no `--bg`**, while
Scientist A is `kind: background` — so recovering her would either fail or change her kind, and
neither is a recovery. Both arms were run against the stopped probe.

| arm | command | result |
|---|---|---|
| 1 | `claude --resume <id> --settings <transport>` | `No conversation found with session ID: …`, exit 1, immediate. Fail-closed; no hang, no TTY error |
| 2 | `claude --resume <id> --bg --settings <transport>` | **exit 0** with a success-shaped banner — and a **new** sessionId `8eba3b81-…`, `kind: background`, `cwd` = the **caller's**, which then reached `state: failed` |

🔴 **The subject could not answer the question.** The probe was born idle and never prompted, so
no conversation was ever persisted: no transcript exists anywhere under `~/.claude`, only
`session-env/` and `jobs/<id>/state.json`. `No conversation found` therefore explains itself and
says nothing about background recovery. Recording arm 1 as *"background recovery fails"* would
have been a plausible predicate answering a different question — so the contract stays
**UNDETERMINED for a resumable subject**, and 6.A1 keeps its own slot: different trigger
(explicit stop vs the supervisor's idle-stop) and different channel.

🔴 **What IS determined, because both arms used the identical id: the two forms disagree on
failure semantics. One refuses; the other silently substitutes a new session and reports
success.** That is unconfounded by the subject's emptiness, and it is decisive for this kernel.
`--bg` is the obvious way to make the resume branch recover a background actor — and with it, a
stale, purged or mistyped sessionId stops being a refusal and becomes **a new actor wearing the
recovered actor's name**, with an `ACTIVE` lineage record pointing at a session that is not the
one running. That is the historical duplicate MC‑3 closes at the birth door, arriving through the
recovery door. The launcher cannot catch it afterwards either: `resume` ends in `exec`, so there
is nothing left to check.

### MC‑6 — recovery is `respawn`, and a success-shaped exit is not evidence

*Surface: launcher. Adjudicated PASS on the third arm, same throwaway subject, never A.*

Read before use, per MC‑4: `claude respawn <id>|--all` — *"Restart a background session (or all
of them) so it picks up the current Claude binary."* **`--all` is never used here**; it would
restart every background session on the machine. The documented purpose is itself an answer to
OB‑1: picking up a new binary is what the supervisor does about version drift.

| arm | command | result |
|---|---|---|
| 3a | `claude respawn <sessionId>` | `No job matching '<sessionId>'`, exit 1 |
| 3b | `claude respawn <job id>` | `respawned 2d2c3b77`, exit 0 — **same** sessionId, `kind: background`, **the original `cwd`**, and the name `qualification-probe` still attached |

**PASS on every pre-committed criterion** except one that this subject cannot answer: *the
transcript continues* is not evaluable, because the probe was never prompted and no transcript
exists even after the respawn. Declared, not glossed.

🔴 **The lineage names a session; the supervisor names a job, and the two keys are not
interchangeable.** The short id is a prefix of the session id *today*, and truncating one into
the other would be an assumption about a format nobody contracted — so the launcher resolves the
job id from the documented roster by matching the session id, and refuses `JOB_ABSENT` when it
cannot. That refusal says the record is **stale, not wrong**: a lineage the supervisor can no
longer place is a fact about the supervisor, and re-birthing over it would destroy the only
pointer to whatever happened.

🔴 **The transport moves house.** `respawn` takes no `--settings`, so for a recovered actor the
per-launch guarantee this kernel enforces at birth is enforced by the supervisor instead —
observed in `respawnFlags`, which carried `--name`, `--settings <our transport.json>` and
`--model`. Recovery therefore *depends* on a non-contracted surface, which is why it became item
5 of the recertification checklist rather than a comment.

> 🔴 **`MODEL_REVERT_ON_RESPAWN` — FALSIFIED, and it was mine.** This section first claimed that
> `--model` is stored as the model the actor was *born* with, so a respawn undoes a mid-session
> fallback. Measured 2026‑08‑14 on Scientist A: her `respawnFlags` carry `--model
> claude-opus-5` — the **fallback** model, not her birth model `claude-fable-5` — and the turn
> she ran after the respawn executed as `claude-opus-5`. **What the narrow observation supports,
> and nothing further: in this measured case the respawn preserved the CURRENT model state, not
> the model of birth.** No generalisation beyond the observed case.
>
> **The shape of the error is the part worth keeping.** On the qualification probe, birth model
> and current model were *the same string*, because that probe's model never changed. The two
> hypotheses were therefore **indistinguishable on that subject** — and from a non-discriminating
> measurement I picked the stronger causal explanation and wrote it into a commit and a spec.
> The measurement was real; it just could not tell the two apart.
>
> This **strengthens** D2's `executed_by`: actor identity, birth model and executing model can
> diverge over time and stay diverged across a recovery. The per-turn source of truth remains the
> transcript.

**And the post-check exists because arm 2 earned it.** `resume` no longer ends in `exec`; it
verifies that the same session came back, live, still background, and refuses
`RECOVERY_UNVERIFIED` otherwise. A mutation removing the absence branch left the primary
assertion **green** — the downstream kind check refused anyway, on an empty string, with the
wrong explanation. `rc == 1` cannot see which layer refused, so both assertions now name their
layer. That is the third variant of `PATTERN_ALREADY_SOLVED_GATE` arriving from the other side:
not a defence with no test, but a *test* passing on a defence it was not aiming at.

**Budget.** `+2` refusals (`JOB_ABSENT`, `RECOVERY_UNVERIFIED`), `0` new verbs, `0` new files.

**Registered, no design now.** The fork semantics measured in arm 2 — transcript continuity
without session identity — is a **candidate** for read-only inspection of archived transcripts
without touching a lineage. Nothing is designed for it here. And this test **informs** 6.A
without replacing it: different trigger (explicit stop vs the supervisor's idle-stop) and
different channel (CLI vs `SendMessage`), so 6.A1 keeps its own slot.

## Execution order

```
1. spec v1.1 freeze (this document + the five gates in the registry)
2. MC-1 and MC-3 implemented, with their receipts (both pending flavours)
3. registered migration of the lineage cell (D1)
4. step 0 — recertification: the MC-2 checklist, committed with CERTIFIED_VERSION → 2.1.231
5. MC-2 regression
6. recovery of Scientist A by sessionId — 5.1c reported as REACHABLE / OPERATIONAL
7. branch (a) re-ordered per MC-4/N2
```

**STOP ON FIRST FALSIFICATION, unchanged:** every FAIL is reported with its measurement
*before* any corrective mechanism is built.

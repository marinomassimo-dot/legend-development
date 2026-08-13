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

1. the parse of `claude agents --json` (Agent View is a research preview; its schema may move);
2. the parse of `--bg` output (the launcher reads the short id from it);
3. the default-name semantics — **observation only**, since after MC‑1/OB‑4 the kernel no
   longer depends on it;
4. the order and text of the named refusals: MC‑1's receipts (a)/(b), MC‑3's residue test and
   MC‑2's own regression **are** the smoke test.

Executable in minutes, entirely on an unqualified host except one optional birth/stop cycle.

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

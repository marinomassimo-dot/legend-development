---
artifact: LEGEND design record — cross-session runtime harness probe
probe_id: HARNESS-PROBE-20260819
governance_version: 3.1.1
normative: NO — architectural provenance only, per design_records/README.md
binding_on_actors: none
authored_by: plan
authored_on: 2026-08-19
domain: CONTENT — governance/design_records/ is under no CONTROL_PLANE_ROOT (P5.1)
probe_scope: performed ONCE, deliberately, so that a Transport candidate and a Routing candidate
  cannot drift apart by measuring the harness twice
supersedes: nothing. It does not replace launch/KERNEL_SPEC.md, which holds earlier measurements
  of the same runtime and is cited here rather than restated
---

# Cross-session runtime harness — one probe, four epistemic classes

This record exists because two candidates are about to be written against the same runtime, and
two candidates that each measure the harness separately will disagree about it within a week.
The measurement is taken **once**, here, and both candidates cite this file.

**Nothing in this record binds an actor.** It is provenance. Where a later normative artifact
states a guarantee, that guarantee must name the row of this record it rests on, and must not be
written in stronger vocabulary than the row supports.

## 0 · The four classes, and what moves a claim between them

```
DOCUMENTED         stated by an official surface of the installed runtime — a tool schema, a
                   tool description, `--help` output. It is what the runtime says about itself.
OBSERVED           reproduced in this session, against the installed runtime, with the command
                   or the tool call that produced it recorded beside it.
REPORTED_UPSTREAM  asserted by operator-supplied news, a secondary changelog, an external
                   consultation, or a runtime version newer than the installed one. It is NOT
                   promoted by being plausible, and NOT promoted by appearing in this session's
                   conversation.
PROPOSED           LEGEND's own design intent. It describes nothing that exists yet.
```

A claim moves `REPORTED_UPSTREAM → DOCUMENTED` when an official surface of the **installed**
runtime is read, and `→ OBSERVED` when the installed runtime reproduces it. Nothing in this
session promoted anything by conversation.

**A fifth state is used where it applies:** `MEASURED_EARLIER` — recorded in
[`launch/KERNEL_SPEC.md`](../../launch/KERNEL_SPEC.md) against a runtime version that is no
longer installed. It is cited, never silently inherited, and §2 says what happens to it.

---

## 1 · Installed runtime version — and why the field is not a scalar

🔴 **The single most consequential finding of this probe: this machine has no "the installed
version".**

```
OBSERVED  ~/.local/bin/claude --version                        →  2.1.232
OBSERVED  extension directories present under ~/.vscode/extensions/
          anthropic.claude-code-{2.1.232, 2.1.233, 2.1.234, 2.1.235}-darwin-arm64
OBSERVED  live sessions run at least TWO different binaries concurrently, read from the
          process image (`ps -o args=`), not from a version string:
            pid 49611 (this session)  …/anthropic.claude-code-2.1.232-…/native-binary/claude
            pid 11605 (mirror-e6)     …/anthropic.claude-code-2.1.233-…/native-binary/claude
OBSERVED  this session's own transcript carries `version: 2.1.232` on all 212 records that
          carry the field — stable within this session
OBSERVED  session e49d3bd1 (still live, pid 3125) carries `version: 2.1.232` on all 2400
          records — stable within that session too
```

Three surfaces disagree in kind, and each is right about a different question:

| surface | answers |
|---|---|
| `claude --version` on `PATH` | which CLI *a shell command* will run — **not** which binary any session is hosted by |
| the process image of a session's pid | which binary **that session** is running |
| the `version` field of a session's transcript | which binary that session **was** running, per record, over its life |

**Consequence, and it is load-bearing for every version-bound guarantee.** A guarantee observed
in this session is a guarantee about **2.1.232**, and the peer it is exercised against may be
running **2.1.233**. `VERSION_OBSERVED` must therefore be recorded **per session**, from the
session's own process image or transcript, and never from a machine-level version string.

**This falsifies an assumption inside an existing tracked artifact.**
[`launch/legend_launch.sh`](../../launch/legend_launch.sh) gates on
`claude --version` == `CERTIFIED_VERSION` (default `2.1.231`). That check measures the CLI on
`PATH`; the actor it is about to launch is hosted by whichever extension binary the supervisor
starts. The two are different binaries today. Recorded as a finding of this probe; **not
repaired here** — `launch/` is outside this session's authorized scope.

`launch/KERNEL_SPEC.md` OB-1 (`SESSION_RUNTIME_DRIFT`, six CLI versions inside one session
lineage, 2026-08-08 → 08-13) is `MEASURED_EARLIER` and **did not reproduce** in either
interactive lineage read today. It is not withdrawn — it was measured on a launcher-born
background lineage, which is a different population — and it is not currently observed.

---

## 2 · Version-bound guarantees — the revalidation rule this record proposes

`PROPOSED`. Every row of §3–§7 that is `DOCUMENTED` or `OBSERVED` carries the same four fields:

```
VERSION_OBSERVED       the version of the SESSION that produced the observation
SOURCE                 the official surface read, or the command run
OBSERVATION / TEST     what was actually seen
REVALIDATION_TRIGGER   default: the hosting session's runtime version differs from
                       VERSION_OBSERVED
```

At any bootstrap or `GATE 0` where a runtime guarantee is load-bearing, the acting session
observes **its own** runtime version. If it differs from `VERSION_OBSERVED`, then in the
vocabulary of Annex A.6 and body §6 the situation is the familiar one:

```
OBSERVED  →  VERSION_CHANGED  →  REVALIDATION_REQUIRED
```

and the guarantee loses *currently-observed* status until revalidated. It does **not** become
false; it becomes unmeasured. The parallel is exact with A.6's refusal rule — a checkpoint whose
fingerprint no longer matches is not wrong, it is *not resumable without asking*.

Nothing may be assumed to survive an upgrade unchanged: not transport semantics, not naming, not
discovery scope, not size limits, not truncation behaviour, not delivery outcomes, not
resume/fork behaviour, not routing.

**All observations in this record carry `VERSION_OBSERVED: 2.1.232` (session
`5c896a65-5701-47a4-ac1f-e6cc8ef4efb2`, pid 49611) unless stated otherwise.**

---

## 3 · The two cross-session primitives — and they are not one primitive

There are **two** discovery surfaces and **one** message surface, and the two discovery surfaces
do not return the same set. Conflating them is the first mistake available here.

### 3.1 · Message primitive — `SendMessage` (tool)

```
DOCUMENTED   tool schema, read at source this session
             fields:  to (required) · message (required) · summary (optional)
             to:      type string, pattern ^[^\n\r]{0,200}$
             message: type string, NO declared bound
             summary: type string, maxLength 200
```

```
OBSERVED     `SendMessage` is a DEFERRED tool in this interactive Plan session: it was present
             by name only and required a `ToolSearch` call before it could be invoked.
```

🔴 **This closes, in the negative, one of the two measurements
`launch/KERNEL_SPEC.md` deliberately left open at zero cost** — *"Is `SendMessage` immediately
available in an interactive session (Plan, Orchestrator) while requiring a `ToolSearch` in a
background one?"* The answer, for this session, is **no**: it is deferred in an interactive
session too. `TOOL_DEFERRED` is therefore not a property of the background actor class.

The consequence is not cosmetic. `ListAgents` was immediately available and `SendMessage` was
not, so the cheapest correct routing sequence — *resolve, then send* — pays a schema-fetch
round-trip **on the send leg**, which is precisely where `MESSAGE_TURN_TRUNCATION` struck on
2026-08-12 and again on 2026-08-14. A routing protocol that treats the send as free is costing
itself the turn boundary with the worst measured record in this repository.

### 3.2 · Discovery primitive A — `ListAgents` (tool)

```
OBSERVED     returned 18 rows. Each row: `name [ref]` · kind · relative start age.
             SELF IS EXCLUDED — this session's own row is absent.
DOCUMENTED   the tool description states the listing may include sessions "on this machine, on
             another machine, or in the cloud", and that Remote Control sessions and cloud
             sessions appear as labelled rows.
OBSERVED     every row returned today was a local interactive session. No remote row, no cloud
             row, no label.
```

### 3.3 · Discovery primitive B — `claude agents --json` (CLI)

```
DOCUMENTED   `claude agents --help`:
               --json   "Print active sessions (interactive and background) as a JSON array
                         and exit (for scripting; does not require a TTY)"
               --all    "With --json: also include completed background sessions"
               --cwd    "Show only background sessions started under <path>"
OBSERVED     `claude agents --json` returned 19 rows.
             Row keys: cwd · kind · name · pid · sessionId · startedAt
             SELF IS INCLUDED: {name: evidence-index-a4, pid: 49611,
             sessionId: 5c896a65-5701-47a4-ac1f-e6cc8ef4efb2, cwd: <this worktree>}
OBSERVED     `--all` returned 23 rows and added the keys `id` (job id) and `state`.
             The 4 extra rows all have `pid: null` and `kind: background`, with
             `state ∈ {done, failed, stopped}`. Interactive rows carry `state: null`.
OBSERVED     `--cwd <path>` filters INTERACTIVE sessions as well, despite the help text saying
             "background sessions": `--cwd <mirror worktree>` returned exactly the 7 mirror rows.
```

### 3.4 · 🔴 The two discovery surfaces answer different questions

```
                        ListAgents (tool)        claude agents --json (CLI)
self                    EXCLUDED                 INCLUDED
sessionId               not shown                shown
cwd                     not shown                shown
pid                     not shown                shown
job id                  not shown                shown under --all
dead/completed rows     not shown                shown under --all, pid: null
remote / cloud rows     DOCUMENTED as possible   not documented, none observed
addressable by the      yes — the name IS the    no — it is a listing, not a transport
message primitive       address
```

The 18 rows of `ListAgents` are exactly the 19 rows of the CLI minus this session's own row.
Both agree on the 18 they share.

🔴 **`SESSION_REF` IS SELF-OBSERVABLE at 2.1.232, and the repository currently says it is not.**

Three durable artifacts state, in substance, *"no actor observes its own routing reference;
`ListAgents` shows peers only"* — `runtime/agent_card_registry.md` (which derives the four refs
by set complement), the canonical
[`framework/protocols/scientist_reading_modes.md`](../../framework/protocols/scientist_reading_modes.md)
§1.2, and lease record #7 in `runtime/orchestrator_lease.md`, which declares
`SESSION_REF: NOT DECLARED` for exactly this reason.

**All three are true of the `ListAgents` tool and false of the `claude agents --json` CLI.** This
session read its own row directly: `evidence-index-a4`, pid 49611, sessionId
`5c896a65-5701-47a4-ac1f-e6cc8ef4efb2`. The derivation-by-set-complement recorded on 2026-08-17
was sound, and it is no longer necessary.

**What this does and does not overturn.** It overturns a *stated reason*. It does not overturn
the conclusions those artifacts draw from it: `ACTOR_ID` is still not `SESSION_REF`, a session
reference is still ephemeral, and no actor may still invent one. Those hold for reasons §5 makes
stronger, not weaker. **No canonical text is edited by this record**, which is a design record
and binds nobody; the correction is registered, and repairing the canonical sentence is a
governed change that belongs to whichever candidate needs it.

---

## 4 · Session identifier forms — four of them, and they are not interchangeable

```
OBSERVED, all four, this session

SESSION_ID        5c896a65-5701-47a4-ac1f-e6cc8ef4efb2
                  UUID. Stable for the life of the session. Names the transcript file at
                  ~/.claude/projects/<encoded-cwd>/<SESSION_ID>.jsonl and the scratchpad
                  directory. Self-observable from the filesystem alone, with no tool call.

SESSION_NAME      evidence-index-a4
                  `<cwd-basename>-<2 hex>` when auto-generated. THIS IS THE ADDRESS the message
                  primitive takes. Assigned by the launcher; `--name <value>` overrides it
                  (DOCUMENTED — observed in the supervisor roster, §7).

LISTAGENTS_REF    the bracketed 6-hex in `name [ref]`. Shown by the tool, absent from the CLI.
                  DOCUMENTED as a disambiguator only, valid only when just read from a listing
                  or an error.

JOB_ID            8 hex, present only on background rows under `--all`. Addresses
                  `claude respawn`. NOT interchangeable with SESSION_ID — passing a session id
                  gives `No job matching '<sessionId>'` (MEASURED_EARLIER, KERNEL_SPEC MC-6).
                  It happens to equal the SESSION_ID's first 8 hex today; KERNEL_SPEC refuses to
                  rely on that, and so does this record.

ROUTING_TRANSPORT uds:/tmp/cc-socks/<pid>.sock — observed as this session's 49611.sock, and as
                  the `from` of an inbound cross-session envelope. Dies with the process
                  (KERNEL_SPEC OB-3).
```

**No LEGEND identity may be built on any of the five.** They are runtime addresses with four
different lifetimes, and only `SESSION_ID` is stable for the life of one incarnation.

---

## 5 · Session name semantics — a convenience resolver, and the measurement that settles it

```
OBSERVED   19 live sessions, and the name is NOT unique per actor, per worktree, or per role:
             evidence-index-*  8 live sessions   (this actor's worktree)
             mirror-*          7 live sessions
             legend-public-*   3 live sessions   (the root checkout)
             lettore-c-b2      1 live session
             lettore           0   ← scientist-a has no session
             lettore-b         0   ← scientist-b has no session
OBSERVED   every name in the live set is unique per SESSION. The suffix is not derived from the
           SESSION_ID: `5c896a65…` → `evidence-index-a4`; `e49d3bd1…` → `evidence-index-59`;
           `b26b34cc…` → `mirror-9c`. Three counter-examples, no derivable relation.
MEASURED_EARLIER   KERNEL_SPEC OB-4: three different default names for ONE unchanged sessionId
           within 24 hours, on an inconsistent base (repo, then worktree, then repo).
OBSERVED   a name survives its session's death in the `--all` listing: `scientist-a`
           (job 2e2571b7, kind background, state failed, pid null) is still returned by name,
           three days after that session died.
```

🔴 **Two conclusions, and the second is the dangerous one.**

1. `SESSION_NAME` is a **convenience resolver**, exactly as suspected, and now on measurement
   rather than suspicion. It is per-session, launcher-assigned, and not stable across a restart
   of the same session.
2. **A name that resolves is not a session that is alive.** `scientist-a` resolves in `--all` to
   a dead job. Any resolver that matches on name must additionally require `pid is not null`,
   and must say so in the code rather than in a comment.

---

## 6 · Zero, one and many — the routing cardinalities, observed live rather than hypothesised

This is the finding that decides the shape of a Routing candidate, and it required no
experiment: it is the state of the machine right now.

| ACTOR_ID | worktree | live sessions in that worktree, OBSERVED | routing cardinality |
|---|---|---|---|
| `scientist-a` | `lettore` | **0** | ZERO — nothing to route to |
| `scientist-b` | `lettore-b` | **0** | ZERO |
| `scientist-c` | `lettore-c` | 1 (`lettore-c-b2`, sessionId `86d4c569…`) | ONE |
| `plan` | `evidence-index` | **8**, one of which is this session | **MANY** |
| `mirror` | `mirror` | **7** | **MANY** |
| `orchestrator` | contested — see §8 | 3 in the root checkout, **0** in the `orchestrator` worktree | **contested: MANY or ZERO** |

🔴 **`evidence-index-59` (pid 3125, sessionId `e49d3bd1-2c63-4969-be19-f7fca4b240fc`) is alive.**
It is the session the Agent Card registry records as `plan`'s `CURRENT_SESSION_REF`, verified at
L1 on 2026-08-17. It has been running since 2026-08-16 and it is **not this session**. So the
registry's row is not stale-pointing-at-a-corpse, which is the failure everyone expects; it is
**accurate and no longer current**, which is worse, because nothing about it looks wrong.

**Therefore, measured and not argued:**

- `T-ROUTE-1` (zero current) is the **live state** of `scientist-a` and `scientist-b`.
- `T-ROUTE-3` (multiple current) is the **live state** of `plan` and `mirror`.
- Worktree is **not** a resolver. `--cwd` narrows 19 to 8; it does not narrow 8 to 1.
- Recency is not a resolver either, and the registry proves why: the *recorded current* is the
  **oldest** live session in this worktree, not the newest.

---

## 7 · Launch, name assignment, resume and fork

```
OBSERVED   ~/.claude/daemon/roster.json (supervisor state, LAST WRITTEN 2026-08-14 — stale, and
           read here as evidence of shape, never as current state) records a worker launched as:
             flagArgs: ["--name", "scientist-a", "--settings",
                        "<...>/evidence-index/launch/transport.json",
                        "--model", "claude-opus-5"]
             cwd: <lettore worktree> · cliVersion: 2.1.231 · launch.mode: "resume"
             launch.fork: false · restoresTranscript: true · isolation: "none"
DOCUMENTED `--name <value>` therefore exists as a launch-time parameter and can be set to the
           ACTOR_ID. The name is assigned BY THE LAUNCHER, never asserted by the session.
MEASURED_EARLIER  KERNEL_SPEC MC-6, measured 2026-08-13 on a throwaway subject:
             claude --resume <id>        refused, exit 1 — fail-closed
             claude --resume <id> --bg   exit 0, success-shaped banner, and a DIFFERENT
                                         sessionId in the CALLER's cwd — A FORK WEARING THE
                                         RECOVERED ACTOR'S NAME
             claude respawn <job id>     same sessionId, same kind, same cwd, same name
OBSERVED   `~/.claude/daemon/roster.json` is not a contracted surface and its schema is the
           supervisor's. `launch/legend_launch.sh` explicitly refuses to parse it and uses
           `claude agents --json` instead. This record adopts the same discipline: the roster is
           cited for the SHAPE of `--name`, and `--name`'s existence is corroborated by the
           `scientist-a` row that `claude agents --json --all` still returns.
```

🔴 **`--resume --bg` produces a fork that is indistinguishable from a recovery by its exit code.**
That is the single most dangerous documented behaviour for a routing model: a "recovery" that
silently creates a second incarnation, under the same name, at a different sessionId. Any
activation model must treat exit code 0 from a resume as **no evidence at all**, which is what
`legend_launch.sh` already does with its post-check.

**A pre-existing, tracked, actor-generic launch kernel already exists** —
[`launch/legend_launch.sh`](../../launch/legend_launch.sh), specified by
[`launch/KERNEL_SPEC.md`](../../launch/KERNEL_SPEC.md), both in `main`. It holds no actor table
(actor and worktree are parameters), gates the host runtime, verifies worktree/top-level/branch
from inside the worktree, refuses if the actor is already live, and — decisively for the
one-current question — **reserves a per-`(actor_id, runtime_instance)` lineage record with
`O_EXCL` BEFORE the spawn**, in two phases, so that a crash between reservation and spawn leaves
a record rather than a permission.

**`O_EXCL` is a real compare-and-swap.** Annex J.0 lists *"Singleton garantito
(compare-and-swap)"* among the guarantees LEGEND does not possess, compensated by the lease
record and double-`ACTIVE` detection. That row is about the **`ORCHESTRATOR_LEASE` over the
shared root**, and it stands. What this probe records is narrower and still significant: for a
resource that is **one file in one local cell**, an atomic create-or-fail primitive is available
and is already used by a tracked LEGEND artifact. Whether any routing state may rest on it is a
governed question and is not answered here.

🔴 **Two conflicts inside that kernel, recorded and not repaired** (both outside this session's
scope):

1. `CERTIFIED_VERSION` defaults to `2.1.231`, and the gate reads `claude --version` — which is
   the wrong binary (§1) and today reports `2.1.232`. The kernel would refuse every launch.
2. The kernel declares *"this kernel only ever births background actors"* and refuses a recovery
   that does not come back `kind: background`. Every LEGEND actor observed today is
   `kind: interactive`, which is what `INTERACTION_PROFILE: VISIBLE_VSCODE` (body §34,
   deployment profile) requires. **As written, the kernel cannot birth or recover any actor this
   laboratory currently runs.**

---

## 8 · Delivery and size — field by field, from source, without stressing the runtime

Two probes were run. **Both were addressed to a deliberately unresolvable target, so no peer
received anything**, and no oversized payload was pushed at the runtime: the `to` and `summary`
bounds are readable at source, and the `message` bound is not, so it stays `UNKNOWN` rather than
being discovered by abuse.

### 8.1 · Per-field size and truncation

| field | BOUND / MAXIMUM | UNIT | OVERSIZE OUTCOME | SENDER OBSERVABILITY | RECIPIENT COMPLETENESS |
|---|---|---|---|---|---|
| `to` | **200** | characters (JSON string; regex `^[^\n\r]{0,200}$`, also forbids CR/LF) | **`REJECTED_PRE_SEND`** — OBSERVED at 213 chars: `InputValidationError`, the tool never ran | **FULL** — structured error naming `path: ["to"]` and the pattern | n/a |
| `summary` | **200** declared (`maxLength`) | characters | **NOT `REJECTED_PRE_SEND`** — OBSERVED: a 264-character summary was accepted and the call proceeded to target resolution. `TRUNCATED` to 200 is **DOCUMENTED** (tool description), **not observed**, because no delivery occurred | **NONE** — the result was byte-identical to the in-bounds call. Nothing warned | **UNVERIFIABLE** from the sender side |
| `message` | **none declared** | — | **UNKNOWN** | UNKNOWN | UNKNOWN |
| envelope / serialized request | not exposed | — | UNKNOWN | UNKNOWN | UNKNOWN |
| tool result | not exposed | — | UNKNOWN | UNKNOWN | UNKNOWN |

🔴 **The asymmetry is the finding, not the numbers.** `to` and `summary` declare their bounds in
the *same* schema, and only one is enforced: `pattern` on `to` rejects, `maxLength` on `summary`
does not. **A design that trusts a declared schema bound to be enforced would be wrong about
`summary` and right about `to`, with nothing in the schema distinguishing them.** Enforcement was
established by probing, one field at a time; it cannot be read off the declaration.

**NO NAKED NUMBERS.** The one number this record hands forward:

```
VALUE                 200
UNIT                  characters, JSON string length
FIELD                 SendMessage.to
SOURCE                tool schema, read at source (DOCUMENTED) + 213-char probe (OBSERVED)
VERSION_OBSERVED      2.1.232
RATIONALE             it is the only bound on this tool that is both declared AND enforced
SAFETY MARGIN         not applicable — no LEGEND address approaches it; the longest ACTOR_ID in
                      the laboratory is 11 characters
REVALIDATION TRIGGER  hosting session's runtime version != 2.1.232
```

No `LEGEND_MESSAGE_BUDGET` number is proposed by this record. `message` has no observed bound, and
inventing a character limit to stand in for one would be a naked number wearing a rationale.

### 8.2 · Delivery outcomes actually observed

```
OBSERVED   target that resolves to nothing:
             {"success": false,
              "message": "No agent named '<x>' is reachable.\nUse ListAgents to see everyone
                          you can message."}
           A structured, sender-visible failure. Not an exception; a result object.
OBSERVED   oversize `to`: InputValidationError, raised BEFORE resolution. The tool never ran.
DOCUMENTED "A listed peer is alive and will process your message — no 'busy' state; messages
            enqueue and drain at the receiver's next tool round."
DOCUMENTED "A ref you did not just read from a listing or an error will not resolve."
DOCUMENTED replies are made by copying the inbound envelope's `from` attribute verbatim.
MEASURED_EARLIER  KERNEL_SPEC MC-5: `REACHABLE` asserts existence, discoverability and
           addressability, and asserts NOTHING about acceptance — "a refusal on arrival is
           silent to the sender". Its test receipt refuses to promote a send's `success: true`
           into an `OPERATIONAL_PASS`: `EVIDENCE_CLASS_MISMATCH: delivery is not acceptance`.
```

🔴 **The one DOCUMENTED claim this probe declines to promote.** *"A listed peer is alive and will
process your message"* is the runtime's statement about itself, and §5 shows a listed name
resolving to a dead job under `--all`, while §6 shows a listed peer (`evidence-index-59`) that is
alive and is nonetheless the wrong recipient. Alive is not the same as *the right one*, and
*will process* is a claim about the receiver's turn that KERNEL_SPEC has twice measured failing
(`MESSAGE_TURN_TRUNCATION`, 2026-08-12 and 2026-08-14). It stays `DOCUMENTED`. It is not
`OBSERVED`, and it must not be quoted as a LEGEND guarantee.

### 8.3 · Recipient-side processing — the classes already exist

`launch/KERNEL_SPEC.md` already defines, from measurement, the classes a delivery-side taxonomy
would otherwise invent:

```
PASS                 emitted and arrived
TOOL_DEFERRED        the tool exists and is available, but a resolution/loading phase must
                     precede execution  ← OBSERVED again this session, in an INTERACTIVE session
TOOL_UNAVAILABLE     the capability is absent from the session or its actor class
NOT_EMITTED          the tool was reachable and no call was made
EMITTED_NOT_ARRIVED  the call was made and nothing reached the receiver

MESSAGE_TURN_TRUNCATION   tool calls emitted → results returned, not interrupted → NO subsequent
                          assistant continuation. Defined by SYMPTOM, because the two observed
                          instances have different mechanisms and the same shape.
```

Anything a Transport candidate says about recipient-side failure must **reference** these, not
restate them, and must not merge `TOOL_DEFERRED` with `TOOL_UNAVAILABLE`.

---

## 9 · Discovery completeness — and the honest verdict

```
OBSERVED   locally, the two surfaces are mutually consistent and jointly exhaustive over the
           local socket set: 19 sockets under /tmp/cc-socks/, 19 CLI rows, 18 tool rows
           (= 19 − self), and every socket's pid resolves to a live process.
DOCUMENTED the tool may list sessions on other machines and in the cloud.
OBSERVED   none appeared. This machine is the only cell in use today.
```

**Verdict: `PARTIAL / UNKNOWN`, and the reason matters.** The local set is exhaustive *and can
be cross-checked* — the socket directory is a third, independent surface. Beyond the local cell,
nothing is observed and nothing is signalled: neither surface returns a completeness flag, a
truncation marker, or a "there may be more" indication.

🔴 Therefore, and this is `PROPOSED` as a rule for whatever consumes this record:

```
NOT LISTED  →  UNKNOWN         always
NOT LISTED  →  DEAD            never, unless exhaustive discovery is an OBSERVED,
                               version-bound guarantee for the scope in question
```

The local scope comes close to earning the exception today. It does not earn it in general, and
a rule that holds only while there is one machine is a rule that fails on the day there are two.

**`ROUTABILITY != LIVENESS` and neither is `DISCOVERY`.** Three properties:

```
DISCOVERED   the surface returned a row for it
LIVE         a process exists                     (pid present, and the pid resolves)
ROUTABLE     LEGEND has decided this incarnation is the actor's current one
```

Today the laboratory can measure the first two and **has no mechanism at all for the third**.
That gap, and not the transport, is what §6 measures.

---

## 10 · The Orchestrator worktree contradiction, as a routing input

Three durable sources, and they do not agree:

| source | says | canonical? |
|---|---|---|
| `roles/orchestrator.md` frontmatter, line 5 | `worktree: the repository root checkout` | **yes — in `main`** |
| `deployment/deployment_profile.md` | `orchestrator` → its own `orchestrator` worktree; the root is reserved to `CANONICAL_BATCH_COMMIT` and holds no other work | **yes — in `main`** |
| `runtime/agent_card_registry.md` (branch `orchestrator`) | `WORKTREE: the root checkout # branch main` | no — runtime state |
| `runtime/orchestrator_lease.md` (branch `orchestrator`) | *"One writer: `orchestrator`, from the orchestrator worktree"* | no — runtime state |

**Why this is `ROUTING_RELEVANT` and not merely untidy.** `--cwd` is the only mechanized
predicate the harness offers for narrowing candidate sessions to an actor (§3.3). If a resolver
uses *the actor's worktree* as that predicate, then for `orchestrator` the predicate has two
canonical readings that return different answers **and different failure modes**:

```
--cwd <repository root>          →  3 live sessions   →  AMBIGUOUS / fail closed on cardinality
--cwd <orchestrator worktree>    →  0 live sessions   →  ABSENT   / fail closed on zero
```

One reading says *too many*, the other says *none*, and both are read off canonical state. A
resolver cannot be specified against a field whose canonical value is contested, so **source
precedence must be resolved before any mechanized resolution can be specified for
`orchestrator`** — which is separately the one actor whose routing is entangled with the lease
(§11).

It is recorded here as an input. **It is not corrected here**: the correction is a governed change
to a canonical role contract, it was already declared as owed by the canonicalizing batch, and it
is not this record's to make.

---

## 11 · Registrar self-reference — the state of the lease, measured

```
OBSERVED   `python3 framework/scripts/lease_state.py --check`, run against the record on branch
           `orchestrator` (7 leases; the copy in `main` carries only 5 — the queue/record
           divergence across branches is a separately-recorded open debt):

             lease #6  derived=RELEASED   lease #7  derived=RELEASED
             ACTIVE by derivation: 0
             2 findings, both lease #3's, both historical

OBSERVED   lease #7 — the lease under which the Scientist A/B specification was canonicalized —
           records `SESSION_REF: NOT DECLARED`, with the reason stated in the record itself:
           "An actor cannot observe its own routing reference." §3.4 shows that premise is
           false at 2.1.232 through the CLI. The lease's CONCLUSION — do not invent one, do not
           inherit one — is unaffected.
```

**The self-reference, stated plainly.** The lease binds `ACTOR_ID: orchestrator` and carries a
`SESSION_REF` field that the last two leases did not fill. So the laboratory already has one
mechanism that answers *"who is Orchestrator now"* — the lease — and it answers it **at the
ACTOR_ID level only**. It cannot currently answer *"which incarnation"*, because the field it
would answer with has been empty by principle since #6.

That is the shape of the problem, not its solution, and this record does not choose between
unifying routing with the lease, relating them by an explicit consistency rule, or separating
them. It records the constraint any answer must satisfy: **there must never be two independent
sources of "who is Orchestrator now" without an explicit rule for what happens when they
disagree**, and today there is exactly one source, with one field unfilled.

---

## 12 · What this probe did NOT do

- **No message was delivered to any peer.** Both `SendMessage` probes targeted a name that
  resolves to nothing. No actor was contacted, woken, or interrupted.
- **No oversized `message` payload was pushed at the runtime.** The bound is `UNKNOWN` and stays
  `UNKNOWN`.
- **Nothing was launched, respawned, resumed or forked.** Every statement in §7 about
  resume/fork is `MEASURED_EARLIER` from `KERNEL_SPEC.md` and is labelled as such.
- **No file in the root checkout was written or read in a way that could dirty it.** Root state
  was inspected with `git --no-optional-locks -C <root> status --porcelain`; it is clean at
  `4454feab`.
- **No canonical artifact was edited**, including the three whose stated reason §3.4 falsifies.
- **No Scientist was activated and `BENCH-AB-001` was not started.** §6's zero-cardinality rows
  for `lettore` and `lettore-b` are a measurement of that fact, not a step toward changing it.

## 13 · Findings this probe hands forward, and who owns them

| # | finding | class | owner |
|---|---|---|---|
| H-1 | "installed version" is not a scalar; `VERSION_OBSERVED` must be per-session | OBSERVED | any version-bound guarantee |
| H-2 | `legend_launch.sh` gates on the wrong binary | OBSERVED | `launch/` — out of scope here |
| H-3 | the kernel births only `background`; every LEGEND actor is `interactive` | OBSERVED | `launch/` — out of scope here |
| H-4 | `SESSION_REF` is self-observable via the CLI; three artifacts state otherwise | OBSERVED | a governed change, in whichever candidate needs it |
| H-5 | `plan` and `mirror` each have many live sessions; A and B have none | OBSERVED | Routing |
| H-6 | the registry's recorded current `plan` session is alive and is not the current one | OBSERVED | Routing |
| H-7 | `summary` declares a bound the runtime does not enforce; `to` declares one it does | OBSERVED | Transport |
| H-8 | `SendMessage` is deferred in an interactive session too | OBSERVED | Transport — closes a KERNEL_SPEC open measurement in the negative |
| H-9 | a name outlives its session in `--all`; resolvers must require a live pid | OBSERVED | Routing |
| H-10 | discovery completeness is unsignalled beyond the local cell | OBSERVED | Routing |
| H-11 | the `orchestrator` worktree contradiction blocks a mechanized resolver for that actor | OBSERVED | governed change — Orchestrator/Plan, carried |
| H-12 | four canonical batches name `snapshot/` tags that do not exist | OBSERVED | control-plane debt, carried — see the author response of 2026-08-19 |

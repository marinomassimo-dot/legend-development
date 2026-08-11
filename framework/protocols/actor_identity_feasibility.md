# PHASE -1 — actor identity feasibility report

> **Executed 2026-08-11 under operator authorisation.** Scope limits observed: nothing on
> `main`, nothing created under the common git directory, **one** message actually delivered,
> `.claude/settings.json` restored byte-identical with git as witness.

## The question this phase answers

> **Can a logical recipient be resolved, checked and refused reliably enough to justify a
> formal actor-routing layer?**

🔴 **This is not identity authentication, and the report must not be read as if it were.**
Three problems were conflated in the original proposal and are kept apart here:

| problem | what it is | in scope for Phase -1 |
|---|---|---|
| **routing** | a message delivered to the wrong session | **yes** — this phase |
| **attribution** | a statement assigned to the wrong actor | no |
| **authority / provenance** | an operator directive relayed by another actor | no |

Coordinates make a claim checkable; they do not authenticate content. Nothing below bears on
the nine misattributed `checkout --detach` or on the three forwarded directives.

## Two layers, and everything measured here belongs to the lower one

**LEGEND logical actor core** — `actor_id`, role, authority, worktree, branch, exclusivity.
Stable, versioned, reviewable, and **portable across any transport**.

**Claude Code transport adapter** — UDS sockets, PID, `process_start`, `SendMessage`,
`PreToolUse`, `ListAgents`. Every measurement in this report is about the adapter. **None of
it defines stable identity.**

An abstract `runtime_binding` reference between the two may be considered later. It must never
carry live coordinates, and it is **not introduced now**.

## Answers to the five demonstration requirements, by number

| # | requirement | verdict |
|---|---|---|
| **1** | two worktrees and the Codex checkout see the same runtime registry | **INCONCLUSIVE** |
| **2** | the transport supports an automatic challenge/response without the recipient acting | **REFUTED (in this session, with documentation)** |
| **3** | who maintains heartbeat and registration while an agent is idle or reading | **DEMONSTRATED — by removing the need** |
| **4** | a session can autonomously know its own `session_ref`, PID/process-start and endpoint | **PARTIALLY DEMONSTRATED** |
| **5** | the resolver can materially prevent a send | **INCONCLUSIVE, deferred, no cause assigned** |

## Experiments

### E0 — a send to a dead endpoint fails loudly · **PASS**

`SendMessage` to `uds:/tmp/cc-socks/1944.sock` (`historical_observation_not_for_routing`,
2026-08-11), an endpoint known absent.

```
success: false
"Failed to send to uds:…/1944.sock: connect ENOENT … — the peer process may have
 restarted, so this socket path is stale. Call ListAgents to get the current address."
```

🔴 **This is the most consequential result in the study, and it argues *against* the layer it
was meant to justify.** The transport already refuses a stale endpoint, already diagnoses the
exact failure mode the proposal was built to prevent, and already names the remedy. Messages
were never at risk of vanishing silently.

One gap remains: the remedy it names is `ListAgents`, whose namespace does not compose exactly
with socket addresses (see R0 and the correlation finding).

No message delivered; no budget consumed.

### E1 — one runtime store · **INCONCLUSIVE**

From `evidence-index`: `pwd -P` → the worktree path; `git rev-parse --path-format=absolute
--git-common-dir` → `/Users/massimo/Desktop/legend-public/.git`.

**One measured context is not six.** The remaining worktrees were **not** measured: doing so
by asking their owners would have cost sends beyond the authorised budget. The documentation
route — every entry `git worktree list` prints is a worktree of this repository, and git gives
all worktrees of one repository a single common directory — is **documentation, not
measurement**, and is labelled as such.

🔴 Phase -1 created nothing under the common git directory. Its adoption as a coordination
store remains an unmade decision.

### E2a — does `.claude/settings.json` reload mid-session? · **NO**

A `PreToolUse` matcher for `Read` was added, pointing at a scratchpad probe that logs and
allows. `Read` was then called. **No log entry was produced.**

The two explanations were separated rather than assumed: the probe was invoked directly with a
synthetic payload and **logged correctly, exit 0**. *(That log line is synthetic and is marked
so; it is not a hook invocation.)* So the script works and the hook was not called.

**Settings are read at session start.**

### E2 — can a hook deny `SendMessage`? · **INCONCLUSIVE**

Unanswerable in this session, because E2a shows the added matcher was never loaded. **No cause
is assigned**: "the matcher does not accept `SendMessage`" is one explanation among several and
was not measured. The experiment must run in a session that **starts** with the matcher present.

A consequence for the reduced design: whether `tool_input` even carries a structured recipient
is also unknown, since nothing was captured. The existence-check enforcement therefore cannot
be called implementable. **Parsing an actor name out of free message text remains
unacceptable** — trivially evadable, an enforcement in name only.

### E3 — automatic challenge/response · **AUTOMATIC_RESPONSE_NOT_OBSERVED**

One message delivered — the whole authorised budget — carrying nonce
`E3-7f2a91c4-20260811T1637Z` and an explicit instruction not to reply manually, which is what
keeps a peer's chosen answer from being mistaken for a transport handshake.

Result shape: `{success, message, msg_id}`. **No peer-generated content**, consistent with
every send this session.

Supporting documentation, which is what raises requirement 2 from *not observed* to
**REFUTED**: the `SendMessage` contract states messages *"enqueue and drain at the receiver's
next tool round"* — delivery is automatic, **answering is an agent action**. This is the tool's
documented contract, not its source; the report says which it has.

### E4 — socket ownership · **PASS**, 5/5 `OWNED`

`lsof -U` establishes the owning PID for every socket. `ps` alone was refused as evidence for
this question.

| socket | owner | classification |
|---|---|---|
| `socket-A` … `socket-E` | `pid-A` … `pid-E` | **all `OWNED`**, zero `UNOWNED_STALE` |

**The filename convention is confirmed by the right instrument: the owning PID equals the
filename in all five cases.** An earlier claim in the proposal reached this conclusion from a
coincidence of a number and a timestamp — right answer, wrong method, and the sixth instance
that day of a plausible predicate answering a different question. Live values are held in the
local artefact, dated, `historical_observation_not_for_routing`; the relations above are
preserved so the classification stays checkable.

### E4b — PID reuse, as a fixture of the comparison function · **PASS**

Not tested against the operating system: killing and re-creating a process does not guarantee
PID reuse, and waiting for the kernel to recycle one is not a test.

    same pid, different start  -> distinguished     (a recycled PID)
    same pid, same start       -> same incarnation
    different pid, same start  -> distinguished
    PID alone on case 1 would have said "same" — which is the defect

### E1c — self-address · corroborated **three** ways

- process ancestry from a shell command → host PID `pid-B`;
- the orchestrator independently observed this session's messages arriving from `socket-B`;
- `lsof` shows `pid-B` owns `socket-B`.

Two independent actors and two independent instruments. Stronger than the single corroboration
the plan expected, and obtained without spending a message.

### E5 — self-knowledge and its limit · **PARTIAL**

Self-derivable: host PID, endpoint, `process_start`, worktree, branch, commit.
**Not obtainable: `session_ref`.** `ListAgents` lists *peers*; a session does not appear in its
own listing. The field is dropped from the schema.

### E6 — **REMOVED** before execution

Concurrent append concerns a runtime store not approved to exist; it answered none of the five
requirements and was implementation design wearing a feasibility label.

## New finding: the two namespaces compose weakly, by start time

R0 (evidence from the orchestrator, attributed to them) concluded the outbound name space and
the inbound socket space are **disjoint and cannot be composed**. Measured here, that is too
strong.

At `18:34:35` on 2026-08-11, the five socket owners started at `10:51:00`, `10:51:15`,
`10:51:40`, `19:47:08` and `09:03:57`. `ListAgents` reports elapsed times.

    "9h ago"    -> uniquely one owner    -> resolved
    "22h ago"   -> uniquely one owner    -> resolved
    "1d ago" x2 -> two candidates        -> AMBIGUOUS

**Composition exists and is bounded by the listing's granularity.** Three of five sessions
started within 40 seconds of each other and are mutually indistinguishable by this method. It
is enough to **check** a claim — an actor asserting an endpoint can be corroborated — and not
enough to **resolve** one. That is a different verdict from "impossible", and the difference
decides what can be built.

## Recommendation

> ## `BUILD_MINIMAL_DIRECTORY`

Build the **LEGEND logical actor core** and nothing else: a versioned registry of `actor_id`,
role, authority, worktree, branch and exclusivity, carrying **no runtime coordinates**, plus
the discipline that every actor states its `actor_id`, worktree, branch and commit in what it
writes.

Why not more:

- **the routing problem is smaller than assumed.** E0 shows the transport refuses a stale
  endpoint loudly and names the remedy. The failure the adapter would have prevented is
  already reported;
- **an advisory adapter would add a mapping that can itself go stale**, whose staleness the
  transport already detects, for a benefit the transport already provides;
- **enforcement is unproven.** E2 is inconclusive and E3 refutes the handshake, so a resolver
  could declare but not refuse;
- **the directory alone closes the failure that actually recurred.** An actor could not tell
  from any repository artifact whether it was Plan and had to ask the operator. A versioned
  registry ends that, and it needs no transport at all.

What it does **not** do, stated so the recommendation is not read as more: it makes a
routing mismatch **detectable and refusable by the recipient**; it does not prevent delivery to
the wrong session, does not authenticate content, and does not address attribution or
authority.

**`CONSIDER_ENFORCEMENT_LATER`** is the correct successor and is conditioned on one thing:
re-run E2 in a session that *starts* with a `SendMessage` matcher present. If it fires and
`tool_input` carries a structured recipient, an existence check becomes implementable. If not,
enforcement is unavailable on this transport and the directory remains the whole of it.

## Bounded claims

- coordinates are **verifiable at reception**, not "falsifiable after the fact": PID and
  `process_start` are checkable while the process lives; branch, worktree and commit move;
- E1c rests on one session, corroborated three ways — a strong agreement, not a population;
- E1 measured one context of six;
- E2's absence has **no assigned cause**.

---

## `DEFERRED_PHASE: MULTI_AGENT_ARCHITECTURE_FEASIBILITY`

**Status: PRESERVED, NOT AUTHORIZED, NOT STARTED.** Recorded here so it survives the session
that conceived it; neither designed nor begun.

**Entry condition:** the Phase -1 recommendation is not `DO_NOT_BUILD`. *(Satisfied: the
recommendation is `BUILD_MINIMAL_DIRECTORY`.)*

**Question:** does formalizing the actor organization outperform the manually coordinated
session model after accounting for scientific throughput, independent review, coordination
amplification and integration load?

**Required hostile-review dimensions:** reader scaling 2→4→8→N; marginal throughput; fan-in;
CAF; OLR; collision rate; integration latency; Plan/Mirror/DMAIC separation; model diversity;
broker necessity; rollback and `DO_NOT_SCALE` conditions.

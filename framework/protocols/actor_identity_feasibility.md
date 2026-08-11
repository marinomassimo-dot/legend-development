# PHASE -1 — actor identity feasibility report

> **Executed 2026-08-11 under operator authorisation**, then **corrected forward** the same day
> after final review. The first version (`191f417`) over-claimed in nine places; every
> correction is applied below and the over-claim is named rather than quietly removed.
>
> Scope observed: nothing on `main`, nothing created under the common git directory, **one**
> message actually delivered, `.claude/settings.json` restored byte-identical.

## The question this phase answers

> **Can a logical recipient be resolved, checked and refused reliably enough to justify a
> formal actor-routing layer?**

🔴 **Not identity authentication.** Three problems were conflated in the original proposal and
are kept apart here:

| problem | what it is | in scope |
|---|---|---|
| **routing** | a message delivered to the wrong session | **yes** |
| **attribution** | a statement assigned to the wrong actor | no |
| **authority / provenance** | an operator directive relayed by another actor | no |

Coordinates make a claim checkable; they do not authenticate content.

## Two layers, and everything measured belongs to the lower one

**LEGEND logical actor core** — `actor_id`, role, `declared_authority_non_enforced`, worktree,
branch, exclusivity. Stable and versioned. 🔴 It **contains no coordinates from the measured
transport; portability was not tested** — an earlier draft claimed it was "portable across any
transport", which is a property no experiment here examined.

**Claude Code transport adapter** — UDS sockets, PID, `process_start`, `SendMessage`,
`PreToolUse`, `ListAgents`. Every measurement here is about the adapter. **None of it defines
stable identity.** An abstract `runtime_binding` may be considered later; it must carry no live
coordinates and is **not introduced now**.

## Answers to the five demonstration requirements, by number

| # | requirement | verdict |
|---|---|---|
| **1** | two worktrees and the Codex checkout see the same runtime registry | **INCONCLUSIVE** — one context of six measured |
| **2** | the transport supports an automatic challenge/response without the recipient acting | **AUTOMATIC CHALLENGE/RESPONSE NOT SUPPORTED BY THE DOCUMENTED `SendMessage` INTERFACE.** 🔴 Not a universal refutation of the mechanism: one send plus one interface's documented contract cannot exclude other paths |
| **3** | who maintains heartbeat and registration while an agent is idle or reading | **NOT APPLICABLE TO THE RECOMMENDED MINIMAL DESIGN.** 🔴 Corrected from `DEMONSTRATED`: the minimal design holds no runtime registry, so the question does not arise. It is moot, not answered |
| **4** | a session can autonomously know its own `session_ref`, PID/process-start and endpoint | **PARTIALLY DEMONSTRATED** — PID, `process_start`, endpoint yes; `session_ref` no |
| **5** | the resolver can materially prevent a send | **INCONCLUSIVE, no cause assigned** |

## Experiments

### E0 — one failure mode only · **PASS, narrowly**

`SendMessage` to `uds:/tmp/cc-socks/1944.sock`, a **pathname known not to exist**:

```
success: false
"connect ENOENT /tmp/cc-socks/1944.sock — the peer process may have restarted,
 so this socket path is stale. Call ListAgents to get the current address."
```

🔴 **Scope, corrected.** This demonstrates exactly one thing: **a connect to a non-existent
pathname is refused, loudly and with a diagnosis.** The first version generalised it into a
delivery guarantee — *"messages were never at risk of vanishing silently"* — and then used that
to argue an adapter is unnecessary. **Both claims are withdrawn.**

Untested, and therefore unknown: a socket file that exists whose owner is dead or is a
different process; delivery *after* a successful connect; whether the recipient's session
processed the message; every failure mode that is not `ENOENT`.

E0 does not make the adapter useless. It narrows the *one* failure mode the first proposal
leaned on hardest.

🔴 **No session continuity is claimed between the two socket paths.** Earlier drafts wrote
`1944` → `92030`, and the arrow asserted something never measured. What was observed is two
separate facts: **(a)** at the time of E0, the pathname `1944.sock` did not exist; **(b)** at
various times, messages were received from, and sent to, `92030.sock`. **Whether these belong
to one session that restarted, or to two different sessions, is not established** — nothing in
this study can distinguish those, and the transport's own error text says only that a peer
*may* have restarted.

### E1 — one runtime store · **INCONCLUSIVE**

From `evidence-index`: `git rev-parse --path-format=absolute --git-common-dir` →
`/Users/massimo/Desktop/legend-public/.git`. **One measured context is not six.** The others
were not measured: asking their owners would have cost sends beyond the budget. The
documentation route — every entry `git worktree list` prints is a worktree of this repository —
is **documentation, not measurement**.

Phase -1 created nothing under the common git directory.

### E2a — `HOT_RELOAD_NOT_OBSERVED` · cause **inconclusive**

A `PreToolUse` matcher for `Read` was added mid-session pointing at a scratchpad probe; `Read`
was then called; **no log entry appeared**.

The probe was separately invoked with a synthetic payload and logged correctly, exit 0.
🔴 **That shows only that the script works in isolation.** It does not establish that settings
are read at session start, that the hook system was reached, or that reload is the missing
step. The first version asserted *"settings are read at session start"* — **a cause that was
not measured, and it is withdrawn.**

*(The one log line present is synthetic and marked so; it is not a hook invocation.)*

### E2 — can a hook deny `SendMessage`? · **INCONCLUSIVE**

Unanswerable in this session and **no cause assigned**. Whether `tool_input` carries a
structured recipient is likewise unknown, since nothing was captured. The existence-check
enforcement therefore cannot be called implementable. Parsing an actor name out of free message
text remains unacceptable: trivially evadable, an enforcement in name only.

### E3 — automatic challenge/response · **`AUTOMATIC_RESPONSE_NOT_OBSERVED`**

One message delivered, carrying nonce `E3-7f2a91c4-20260811T1637Z` and an explicit instruction
not to reply manually — which is what keeps a peer's chosen answer from being mistaken for a
transport handshake. Result shape `{success, message, msg_id}`, no peer-generated content,
consistent with every send this session.

🔴 **No observation window was defined in advance.** "No response observed" therefore has no
declared duration behind it, and the experimental silence carries correspondingly little
weight. **Requirement 2 rests on the documented `SendMessage` contract** — messages *"enqueue
and drain at the receiver's next tool round"*, delivery automatic and answering an agent
action — **and not on that silence.** This is the interface's documented contract, not its
source.

🔴 **Process defect in this experiment, recorded rather than omitted.** The delivered message
**exceeded the minimal challenge**: it also transmitted operational conclusions about E0, E4
and the namespace-correlation finding. That was outside what the experiment required, and it
made the single authorised message carry unreviewed claims — **one of which, the E0 delivery
guarantee, is withdrawn in this report.**

The false conclusion was transmitted. Per the operator, the orchestrator has since **withdrawn
it**; that retraction is reported to this session rather than observed by it, and is recorded
as the operator's statement. The correction propagated, but it propagated by someone else's
diligence rather than by design: the experimental channel should have carried the challenge and
nothing else.

### E4 — socket ownership · **PASS**, 5/5 `OWNED`

`lsof -U` establishes the owning PID for each socket; `ps` alone was refused as evidence for
this question.

🔴 **Re-verifiable evidence, included because pseudonymisation had made the classification
uncheckable.** The following is the literal output, recorded 2026-08-11:

```
### historical_observation_not_for_routing — 2026-08-11, NOT FOR ROUTING ###
claude     1883 massimo   18u  unix 0x4d113e3dd737279a      0t0      /tmp/cc-socks/1883.sock
claude     1978 massimo   18u  unix 0xd6da3c0c51df51a8      0t0      /tmp/cc-socks/1978.sock
claude     2024 massimo   13u  unix 0x7b07579ddaccd765      0t0      /tmp/cc-socks/2024.sock
claude    39715 massimo   12u  unix 0xd72a129d67b6fcd8      0t0      /tmp/cc-socks/39715.sock
claude    92030 massimo   15u  unix 0xecc74cecae020278      0t0      /tmp/cc-socks/92030.sock
### historical coordinates whose current validity is not asserted; never use for routing ###
```

**All five `OWNED`, zero `UNOWNED_STALE`, and the owning PID equals the filename in every
case.** The proposal's earlier version reached that conclusion from a coincidence of a number
and a timestamp — right answer, wrong instrument.

### E4b — PID reuse, as a fixture of the comparison function · **PASS**

    same pid, different start  -> distinguished     (a recycled PID)
    same pid, same start       -> same incarnation
    different pid, same start  -> distinguished
    PID alone on case 1 would have said "same" — the defect

Not tested against the operating system: waiting for the kernel to recycle a PID is not a test.

### E1c — self-address · corroborated three ways

Process ancestry → host PID `1978`; the orchestrator independently observed this session's
messages arriving from `1978.sock`; `lsof` shows `1978` owns `1978.sock`. Two actors, two
instruments, one session. A strong agreement, not a population.

### E5 — self-knowledge and its limit · **PARTIAL**

Self-derivable: host PID, endpoint, `process_start`, worktree, branch, commit.
**Not obtainable: `session_ref`** — `ListAgents` lists peers; a session does not appear in its
own listing. The field is dropped from the schema.

### E6 — **REMOVED** before execution

Concurrent append concerns a runtime store not approved to exist.

## `START-TIME CORRELATION` — corroborative only

> **Corroborative only; not identity resolution and not routing evidence.**

R0 (evidence from the orchestrator, attributed to them) concluded the outbound name space and
the inbound socket space cannot be joined. One observation qualifies that.

At `18:34:35` the five socket owners started at `10:51:00`, `10:51:15`, `10:51:40`, `19:47:08`,
`09:03:57`; `ListAgents` reports elapsed times.

    "9h ago"    -> one candidate
    "22h ago"   -> one candidate
    "1d ago" x2 -> two candidates -> AMBIGUOUS

Three of five sessions started within 40 seconds of each other and are indistinguishable by
this comparison. Where a listing entry has exactly one candidate, the comparison can
**corroborate an endpoint an actor has independently claimed**.

🔴 **It does nothing else, and the earlier wording overreached in the one direction that
matters.** A previous version of this section was titled *"Namespace correlation, weak and
bounded"* and said *"composition exists"*. The verb invites a reader to treat the comparison as
a route, and the operator rejected exactly that formulation when it was used elsewhere. So,
stated as prohibitions rather than as limits:

- it is **not identity resolution** — a unique candidate is not an identification;
- it is **never an authorised routing method**, under any circumstances, including the cases
  where it happens to be unambiguous;
- it corroborates a claim **made independently**; it originates nothing.

The finding is unchanged. Only the verb is, because the verb was the part someone would have
built on.

## Protocol deviation, declared

🔴 **The `trap` was promised and not installed.** The plan required a `trap` restoring
`.claude/settings.json` on ERR, INT and EXIT. What was actually done: a byte-identical backup
outside the repository, a recorded `shasum`, and a manual restore verified by both witnesses.
**The restore succeeded** — digest equal to the pre-experiment value and `git diff --quiet`
clean — but the protection against an interrupted session was never in place. A happy path that
worked is not the recovery that was specified.

## Recommendation — **provisional**

> ## `BUILD_MINIMAL_DIRECTORY`

🔴 **Rebased.** The first version grounded this on E0, i.e. on a delivery guarantee that is
now withdrawn. It rests instead on a narrower and better-supported value:

**a versioned registry lets a recipient identify itself.** The failure that actually recurred
was an actor unable to tell, from any repository artifact, whether it was Plan — it had to ask
the operator. That is closed by a file, needs no transport, and survives any change of
transport.

What it does **not** do: it **makes a routing mismatch detectable under the declared
discipline** — 🔴 replacing *"closes the failure"* — and only where actors state their
coordinates as the discipline requires. It does not prevent delivery to the wrong session, does
not authenticate content, and does not address attribution or authority.

Why not more, on present evidence: enforcement is unproven (E2 inconclusive, no cause), the
documented interface offers no automatic handshake (E3), and an adapter would introduce a
mapping that can go stale for benefits not demonstrated.

`CONSIDER_ENFORCEMENT_LATER`, conditioned on re-running E2 in a session that **starts** with a
`SendMessage` matcher present, capturing whether `tool_input` carries a structured recipient.

## Bounded claims

- E0 covers `connect ENOENT` to a non-existent pathname and **nothing else**;
- E2a observed no hot reload; **the cause is not established**;
- requirement 2 is limited to the documented `SendMessage` interface;
- requirement 3 is moot under the minimal design, not demonstrated;
- coordinates are **verifiable at reception**, not falsifiable indefinitely;
- E1 measured one context of six; E1c rests on one session.

---

## `DEFERRED_PHASE: MULTI_AGENT_ARCHITECTURE_FEASIBILITY`

**Status: PRESERVED, NOT AUTHORIZED, NOT STARTED.**

**Entry condition — 🔴 PROVISIONAL, pending operator acceptance:** the Phase -1 recommendation
is not `DO_NOT_BUILD`. The recommendation above is itself provisional, so this condition is not
satisfied until the operator accepts it.

**Question:** does formalizing the actor organization outperform the manually coordinated
session model after accounting for scientific throughput, independent review, coordination
amplification and integration load?

**Required hostile-review dimensions:** reader scaling 2→4→8→N; marginal throughput; fan-in;
CAF; OLR; collision rate; integration latency; Plan/Mirror/DMAIC separation; model diversity;
broker necessity; rollback and `DO_NOT_SCALE` conditions.

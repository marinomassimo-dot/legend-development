# Actor identity — PROPOSAL, not in force

> **Status: PROPOSAL AWAITING APPROVAL.** Nothing here is implemented. No validator, no
> shared state and no addressing behaviour changes until this document is approved
> separately. It is written into the repository rather than left in a message because a
> proposal that lives only in a cross-session channel dies with the session — which is the
> same defect this design exists to fix, one layer up.

---

## 1. The problem, measured today rather than imagined

Four failures on 2026-08-10/11, each with a receipt:

**① An endpoint changed under an instruction that had just used it.** The orchestrator's
socket moved from `1944` to `92030` mid-session. Measured now: `/tmp/cc-socks/` holds
`1883`, `1978`, `2024`, `39715`, `92030` — **five sockets** — while `ListAgents` reports
**four** live peer sessions, and `1944.sock` no longer exists at all. Stale endpoints are the
normal state of that directory, not the exception, and nothing in the addressing scheme
distinguishes a live socket from a dead one.

**② A directive addressed to one role arrived at another.** A message headed
`RECIPIENT: PLAN` was delivered to the actor the sender called "Lettore". The recipient could
not determine from any repository artifact whether it was Plan, and had to ask the operator.
**Role was a fact held only in the senders' heads.**

**③ Nine `checkout --detach` were attributed to the wrong actor**, in a first-person message
the recipient was asked to relay. The recipient refused; had it complied, a false statement
about who mutated a shared checkout would have entered the record as state.

**④ Three directives were forwarded verbatim**, and the forwarder's voice became
indistinguishable from the operator's. The forwarder's own conclusion: *a channel that can
carry the operator's voice is a channel in which my voice becomes indistinguishable from
theirs.*

None of these is a transport bug. All four are **identity** bugs: who an actor *is*, what it
is allowed to do, and where it currently *lives* were conflated into one unverified name.

---

## 2. The separation

| | **Stable identity** | **Runtime routing** |
|---|---|---|
| answers | *who is this actor, and what may it do* | *where is it right now* |
| changes | rarely, by review | every session start |
| versioned | **yes** | **no** — gitignored |
| written by | operator (Plan proposes) | each actor, its own row only |
| contains an endpoint | **never** | yes, and only here |

The whole design rests on that last row. If a socket, PID or session name ever appears in the
versioned registry, the two halves have merged again and every guarantee below is void. §7
proposes a structural test whose only job is to keep that true.

---

## 3. Versioned registry — `framework/state/actors.yaml`

```yaml
schema_version: 1
actors:
  - actor_id: plan
    role: integrator
    authority: [merge_to_main, batch_commit, sync_epoch_record, framework_write]
    worktree: .claude/worktrees/evidence-index
    branch: evidence-index
    exclusive: true

  - actor_id: reader-a
    role: reader
    authority: [reading_write, receipt_record, manifest_write]
    worktree: .claude/worktrees/lettore
    branch: lettore
    exclusive: false

  - actor_id: reader-b
    role: reader
    authority: [reading_write, receipt_record, manifest_write]
    worktree: .claude/worktrees/lettore-b
    branch: lettore-b
    exclusive: false

  - actor_id: mirror
    role: auditor
    authority: [read_only]
    worktree: .claude/worktrees/mirror
    branch: mirror
    exclusive: true

  - actor_id: codex
    role: harness_probe
    authority: [reading_write, receipt_record]
    worktree: ../legend-codex-reading
    branch_prefix: codex/
    exclusive: false

  - actor_id: orchestrator
    role: coordinator
    authority: [read_only, propose]
    worktree: null            # coordinates; owns no tree
    branch: null
    exclusive: true

exclusive_roles: [integrator, auditor, coordinator]
```

Notes on the choices, since each is a decision and not a default:

- **`authority` is an enumerated capability list, not prose.** A sentence cannot be checked
  before a write; a token can. `orchestrator` holds `propose` and **not** `operator_relay` —
  there is deliberately no capability that permits forwarding an operator directive, which is
  failure ④ made structurally unavailable rather than discouraged.
- **`worktree` and `branch` are part of identity**, because the one-actor-one-worktree rule in
  `CLAUDE.md` is already the invariant that makes concurrent work safe. Binding them here is
  what lets a role/worktree mismatch be *refused* instead of noticed afterwards.
- **`orchestrator` owns no worktree**, and that is the honest encoding of what it does. An
  actor with `worktree: null` may hold no capability that writes.
- **`exclusive` is per-actor and `exclusive_roles` is per-role**, because the two answer
  different questions: two `reader` actors are normal, two live `plan` registrations are not.

---

## 4. Runtime registry — `.legend/runtime/actors.jsonl` (gitignored)

One row per registration, appended by the actor itself at session start:

```json
{
  "actor_id": "plan",
  "session_name": "legend-public-aa",
  "session_ref": "b852bb",
  "endpoint": "uds:/tmp/cc-socks/92030.sock",
  "pid": 92030,
  "process_start": "2026-08-11T09:03:11Z",
  "nonce": "9f2c…",
  "worktree": "/Users/massimo/Desktop/legend-public/.claude/worktrees/evidence-index",
  "branch": "evidence-index",
  "commit": "d06a4a1…",
  "heartbeat_at": "2026-08-11T11:42:00Z",
  "superseded_by": null
}
```

- **`pid` alone is not identity — `pid` + `process_start` is.** PIDs are reused, and a reused
  PID answering on a socket left behind by its predecessor is precisely the failure that looks
  most like success.
- **`nonce` is minted at registration and never reused.** It is what distinguishes *this*
  incarnation of an actor from the one that died on the same socket.
- **`heartbeat_at` decides liveness**, not the presence of a socket file. Measured today: the
  socket file outlives the session by design.
- **`.legend/runtime/` is gitignored** and must be added to `.gitignore` in the same change
  that creates it — a runtime registry that reaches a commit is a stale registry shipped to
  everyone.

---

## 5. Resolution — at send time, by handshake

**The registry is a hint. The handshake is the proof.** Nothing is ever addressed from a
remembered endpoint.

```
resolve(actor_id):
  1. read the versioned registry        -> expected role, authority, worktree, branch
  2. read the runtime registry          -> candidate rows for actor_id, freshest heartbeat first
  3. for each candidate, HANDSHAKE:
        send  {challenge: <fresh nonce>, expect_actor: <actor_id>}
        expect{actor_id, registration_nonce, pid, process_start,
               worktree, branch, commit, echo: <challenge>}
  4. accept only if ALL hold:
        - echo matches the challenge just sent      (not a replay)
        - actor_id equals the one asked for         (not a neighbour)
        - registration_nonce equals the row's       (not a previous incarnation)
        - pid + process_start equal the row's       (not a recycled PID)
        - worktree + branch equal the VERSIONED registry's
        - the role's exclusivity holds
  5. otherwise -> UNRESOLVED
```

**`UNRESOLVED` has no fallback and that is the entire point.** No "send to the only session
that answered". No nearest-name match. No trying the next socket in the directory. A resolver
that degrades gracefully here re-creates failure ①, because a wrong recipient that accepts the
message is indistinguishable from the right one.

Mapping to the six required behaviours:

| requirement | what refuses it |
|---|---|
| stale socket refused | no answer within timeout, **or** an answer whose `nonce` / `pid+process_start` disagree with the row |
| restart on a new socket resolved | the actor re-registers with a new nonce; resolution is by `actor_id`, and **endpoints are never cached between sends** |
| double claim of an exclusive role refused | registration refuses when another row for an exclusive role has a fresh heartbeat and a different nonce |
| role/worktree mismatch refused | handshake compares the *runtime* worktree/branch against the *versioned* registry, not against the row that claims them |
| unverifiable identity | `UNRESOLVED`, no fallback |
| every send logged | see §6 |

**Takeover is possible but never silent.** If the incumbent's heartbeat is stale, a new
registration may claim an exclusive role with an explicit `--supersede`, which writes
`superseded_by` on the old row and records the takeover. A crashed Plan must be replaceable;
a running Plan must not be displaced by a second one that merely started later.

---

## 6. Send log, and the one part of it that must be versioned

Every send records **the coordinates actually resolved**, never the intended ones:

```
sent_at · from_actor_id · to_actor_id · resolved_endpoint · resolved_pid+start
· resolved_nonce · resolved_worktree · resolved_branch · resolved_commit · message_id
```

That distinction is failure ① in one line: a log of what I *meant* would have recorded
"orchestrator" and looked fine.

The send log is **runtime and gitignored** — it is high-volume operational traffic. But
`UNRESOLVED` refusals, exclusivity refusals and supersedes are **appended to a versioned
ledger**, because those are exactly the events that must outlive the session. Proposed reuse:
the chain and tail anchor already in `sync_epochs.py` / `fulltext_receipts.py`, parameterised
by `anchor_patterns`, rather than a third implementation.

🔴 Reuse of a *mechanism*, not an echo: nothing here audits the receipt ledger. If this ledger
ever needs to corroborate another, the shared import must be broken.

---

## 7. Tests

Each of the six requirements gets an adversarial test that fails without the guard. Beyond
them, four that exist because of what this repository has already paid for:

1. **`test_the_versioned_registry_contains_no_endpoint`** — scan for socket-, pid-, port- and
   session-shaped keys and values. This is the load-bearing test of the whole design: the
   separation dies the day someone adds `socket:` "just for convenience", and it dies quietly.
2. **`test_a_recycled_pid_on_an_inherited_socket_is_refused`** — same PID, different
   `process_start`. The case that looks most like success.
3. **`test_a_replayed_handshake_is_refused`** — a peer answering with a valid-but-old nonce,
   or echoing a challenge it was not just sent.
4. **`test_unresolved_sends_nothing`** — asserts **no send occurred**, not merely that a
   status was returned. Written this way because on 2026-08-11 a refusal test in this
   repository asserted that an exception was raised while the write happened behind it: *a
   test for a refusal must assert what was not done, not that something was thrown.*

Plus a mutation-battery entry per requirement, since a guard whose removal nothing catches has
never been tested.

---

## 8. Ownership

| artefact | writer | reader |
|---|---|---|
| `framework/state/actors.yaml` | operator (Plan proposes, review lands it) | everyone |
| `.legend/runtime/actors.jsonl` | **each actor, its own row only** | resolver |
| supersede / UNRESOLVED ledger | the resolver, automatically | everyone |
| resolver code + tests | Plan | everyone |

No actor writes another actor's runtime row. A registry where one process can register another
re-introduces the impersonation this design removes.

---

## 9. Migration — three phases, and the middle one is not optional

**Phase 0 — describe what is true.** Write `actors.yaml` from measured facts. Current
worktrees, measured 2026-08-11:

```
/Users/massimo/Desktop/legend-public                          DETACHED  9296ad7
/Users/massimo/Desktop/legend-codex-reading                   codex/pmid-34831305
.claude/worktrees/evidence-index                              evidence-index
.claude/worktrees/lettore                                     lettore
.claude/worktrees/lettore-b                                   lettore-b
.claude/worktrees/mirror                                      mirror
```

No behaviour change. The only immediate benefit is that failure ② stops being possible: an
actor can read what it is.

**Phase 1 — advisory.** Actors register and the resolver runs on every send, but its verdict
is **recorded, not enforced**. Sends proceed as today. Collect the disagreements.

🔴 This phase is where the design earns the right to be a guard. This repository has now
catalogued five cases of a plausible predicate that answered a different question from the one
asked, and the standing lesson is that **a guard designed from an unadjudicated list punishes
the practice that produces the list**. Phase 1 produces the adjudicated list. Exit criterion:
every `UNRESOLVED` in a review window has been opened individually and classified as a real
identity failure or a rule defect.

**Phase 2 — binding.** `UNRESOLVED` blocks the send. Exclusivity refuses at registration.

Rollback at any phase is deleting the runtime directory and reverting one commit; the
versioned registry is inert without a resolver.

---

## 10. What this does not solve, stated rather than discovered later

- **It authenticates an actor, not the content of what it says.** Failure ④ — a forwarded
  directive — becomes *attributable* rather than impossible. The structural half is the absent
  `operator_relay` capability; the rest is discipline.
- **It assumes actors register honestly.** An actor can register as itself and then lie in
  prose. What it cannot do is answer a handshake as someone else.
- **Single machine, single user.** No cryptographic identity, no cross-host trust. If actors
  ever run on separate hosts, the nonce handshake needs a shared secret and this section is
  where that gets written.
- **Scale.** Six actors, five sockets. Every mechanism here is O(actors) per send. It stays
  linear to a few dozen; past that, resolution needs caching **with explicit invalidation on
  heartbeat change** — and a cache without that invalidation is failure ① rebuilt.

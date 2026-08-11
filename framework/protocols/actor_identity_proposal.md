# Actor identity — PROPOSAL, revised after Phase -1

> **Status: PROPOSAL. Not in force.** Revised 2026-08-11 against the executed feasibility
> report ([`actor_identity_feasibility.md`](actor_identity_feasibility.md)) and two rounds of
> adversarial review. Commit `559aa4b` remains in history as the superseded first version.
>
> Recommendation carried from Phase -1: **`BUILD_MINIMAL_DIRECTORY`**.

---

## 1. Three problems, and this document addresses one

The first version cited four failures as motivation for one mechanism. They are not one
failure, and the conflation was the central defect adversarial review found.

| problem | example, 2026-08-10/11 | does a directory solve it |
|---|---|---|
| **routing** — message delivered to the wrong session | endpoint `1944` → `92030`; a directive headed `RECIPIENT: PLAN` reaching an actor that could not tell whether it was Plan | **detectable and refusable by the recipient** — not prevented |
| **attribution** — a statement assigned to the wrong actor | nine `checkout --detach` reported as another actor's | **no.** Coordinates make a claim checkable; they do not authenticate content |
| **authority / provenance** — an operator directive relayed by another actor | three directives forwarded verbatim | **no.** Structural only with a channel enforcement that Phase -1 could not demonstrate |

Everything below is about **routing**, and only routing.

## 2. Two layers

**LEGEND logical actor core** — `actor_id`, role, authority, worktree, branch, exclusivity.
Stable, versioned, reviewed, and portable across any transport. **This is what the proposal
now recommends building.**

**Claude Code transport adapter** — UDS sockets, PID, `process_start`, `SendMessage`,
`PreToolUse`, `ListAgents`. Measured in Phase -1; **not built**; and none of it defines
identity.

An abstract `runtime_binding` between the layers may be considered later. It must carry **no
live coordinates** and is **not introduced here**.

## 3. What Phase -1 measured that changed this document

- **a send to a dead endpoint fails loudly**, with a diagnosis and a named remedy. The routing
  failure the first version was built to prevent is already reported by the transport;
- **no automatic challenge/response exists** — delivery is automatic, answering is an agent
  action, per the tool's documented contract;
- **hook enforcement is unproven**: settings are not re-read mid-session, so the experiment
  could not run, and **no cause is assigned**;
- **socket ownership is confirmed** by `lsof`, and an actor can derive its own address —
  corroborated three ways, by two actors and two instruments;
- **a bare name is not an address**; the ref lives only inside another session's private
  listing, and a session cannot learn its own name at all;
- **the two namespaces compose weakly by start time** — enough to *check* a claimed endpoint,
  not to *resolve* one.

🔴 The first version asserted that *"stale endpoints are the normal state of that directory"*.
**Measured false**: every socket present was `OWNED`. The real hazard is narrower — a
*remembered* endpoint can vanish — and the transport already reports it.

## 4. The versioned registry — `framework/state/actors.yaml`

```yaml
schema_version: 1
actors:
  - actor_id: plan
    role: integrator
    authority: [merge_to_main, batch_commit, sync_epoch_record, framework_write]
    worktree: .claude/worktrees/evidence-index
    branch: evidence-index
  - actor_id: reader-a
    role: reader
    authority: [reading_write, receipt_record, manifest_write]
    worktree: .claude/worktrees/lettore
    branch: lettore
  - actor_id: mirror
    role: auditor
    authority: [read_only]
    worktree: .claude/worktrees/mirror
    branch: mirror
  - actor_id: orchestrator
    role: coordinator
    authority: [read_only, propose]
    worktree: null
    branch: null

multi_instance_roles: [reader]
```

- 🔴 **every `actor_id` is exclusive.** Two actors may share the role `reader`; two live
  sessions may never both be `reader-a`. The first version got this wrong;
- **`authority` is enumerated tokens, not prose**, because a sentence cannot be checked before
  a write;
- there is **no `operator_relay` capability**, and — corrected — its absence is a **declared
  rule, not a structural impossibility.** Making it structural requires channel enforcement
  that Phase -1 could not demonstrate;
- **`worktree: null` means the actor owns no tree** and may hold no capability that writes;
- **closed schema.** An explicit key allowlist, with the test asserting *no key outside it
  exists* — not a heuristic search for endpoint-shaped strings, which would pass anything
  named creatively. **No socket, PID, session name or ref may appear here.** That single
  invariant is what keeps the two layers apart.

## 5. What replaces authentication: attribution coordinates

Every actor states, in each message and each record it writes, its `actor_id`, worktree,
branch and commit. All are self-derivable and independently checkable by the reader against
`git` — and against `ps` for the adapter-level pair `pid` + `process_start`, which is identity
only in the pair, never the PID alone.

🔴 **Bounded:** this yields attribution **verifiable at reception**, not "falsifiable after the
fact" — a phrase the first version used that claimed a durability the coordinates do not have.
PID and `process_start` are checkable while the process lives; branch, worktree and commit
move.

## 6. What is deliberately not built

- **no runtime registry**, and no adoption of the common git directory as a coordination
  store — a decision the operator has not made and Phase -1 did not take;
- **no resolver**, and no `UNRESOLVED` gate: with no handshake, a resolver could declare but
  not refuse;
- **no `session_name` or `session_ref` field.** A session cannot learn its own name; a schema
  field an actor cannot fill about itself will be filled by guesswork;
- **no `heartbeat_at`.** Liveness comes from the operating system, not from an agent that
  stops writing while it reads;
- **no worker writes a versioned ledger.** Any incident worth keeping is promoted by Plan.

## 7. Migration

**Phase 0 — describe what is true.** Write `actors.yaml` from measured worktrees and branches.
No behaviour change. It closes the one failure that recurred: an actor can read what it is.

**Phase 1 — discipline.** Actors state their coordinates in what they write and what they
send. Still no enforcement, still no resolver.

**Enforcement, later and conditioned.** Re-run E2 in a session that *starts* with a
`SendMessage` matcher present. If it fires **and** `tool_input` carries a structured recipient,
an existence check against `actors.yaml` becomes implementable — a spelling-and-existence
check, not authentication, and to be labelled as such. If not, enforcement is unavailable on
this transport and the directory is the whole of it.

## 8. Limits, stated rather than discovered later

- authenticates nothing; a registered actor can register honestly and then write prose that is
  false;
- single machine, single user; no cryptographic identity and no cross-host trust;
- the identity core is transport-independent by construction, which is the property that makes
  it worth building even though the adapter is not.

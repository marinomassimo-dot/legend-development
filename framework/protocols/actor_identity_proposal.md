# Actor identity — PROPOSAL, revised after Phase -1

> **Status: PROPOSAL. Not in force.** Revised 2026-08-11 against the executed feasibility
> report ([`actor_identity_feasibility.md`](actor_identity_feasibility.md)) and two rounds of
> adversarial review. Commit `559aa4b` remains in history as the superseded first version.
>
> Recommendation carried from Phase -1: **`BUILD_MINIMAL_DIRECTORY`** — 🔴 **provisional,
> pending operator acceptance.** It rests on the registry's value for **recipient
> self-identification**, not on any delivery guarantee: the guarantee an earlier draft drew
> from E0 has been withdrawn.

---

## 1. Three problems, and this document addresses one

The first version cited four failures as motivation for one mechanism. They are not one
failure, and the conflation was the central defect adversarial review found.

| problem | example, 2026-08-10/11 | does a directory solve it |
|---|---|---|
| **routing** — message delivered to the wrong session | a remembered endpoint later found absent, and separately a different endpoint in use — **no session continuity between the two is established**; a directive headed `RECIPIENT: PLAN` reaching an actor that could not tell whether it was Plan | **the mismatch becomes detectable under the declared discipline**, and refusable by the recipient — delivery is not prevented, and detection holds only where actors state their coordinates as the discipline requires |
| **attribution** — a statement assigned to the wrong actor | nine `checkout --detach` reported as another actor's | **no.** Coordinates make a claim checkable; they do not authenticate content |
| **authority / provenance** — an operator directive relayed by another actor | three directives forwarded verbatim | **no.** Structural only with a channel enforcement that Phase -1 could not demonstrate |

Everything below is about **routing**, and only routing.

## 2. Two layers

**LEGEND logical actor core** — `actor_id`, role, `declared_authority_non_enforced`, worktree,
branch, exclusivity. Stable, versioned, reviewed. 🔴 It **contains no coordinates from the
measured transport; portability was not tested** — an earlier draft called it "portable across
any transport", a property no experiment here examined. **This is what the proposal now
recommends building.**

**Claude Code transport adapter** — UDS sockets, PID, `process_start`, `SendMessage`,
`PreToolUse`, `ListAgents`. Measured in Phase -1; **not built**; and none of it defines
identity.

An abstract `runtime_binding` between the layers may be considered later. It must carry **no
live coordinates** and is **not introduced here**.

## 3. What Phase -1 measured that changed this document

- **a connect to a non-existent socket pathname is refused loudly**, with a diagnosis and a
  named remedy. 🔴 **That is one failure mode and not a delivery guarantee**: a socket that
  exists with a dead or different owner, and everything after a successful connect, are
  untested. An earlier draft generalised this into "messages never vanish silently" and used it
  to argue an adapter is unnecessary — **both claims are withdrawn**;
- **the documented `SendMessage` interface offers no automatic challenge/response** — delivery
  automatic, answering an agent action. Not a universal refutation of the mechanism;
- **hook enforcement is unproven**: a matcher added mid-session was not observed to fire, and
  **the cause is not established** — `HOT_RELOAD_NOT_OBSERVED`, no cause assigned;
- **socket ownership is confirmed** by `lsof`, and an actor can derive its own address —
  corroborated three ways, by two actors and two instruments;
- **a bare name is not an address**; the ref lives only inside another session's private
  listing, and a session cannot learn its own name at all;
- **`START-TIME CORRELATION` is corroborative only** — it can support an endpoint an actor has
  independently claimed, and it is **not identity resolution and never an authorised routing
  method**. An earlier draft said the two namespaces "compose weakly", which invites a reader
  to treat it as a route.

🔴 The first version asserted that *"stale endpoints are the normal state of that directory"*.
**Measured false**: every socket present was `OWNED`. The real hazard is narrower — a
*remembered* endpoint can vanish — and the transport reports that particular case.

## 4. The versioned registry — `framework/state/actors.yaml`

```yaml
schema_version: 1
actors:
  - actor_id: plan
    role: integrator
    declared_authority_non_enforced: [merge_to_main, batch_commit, sync_epoch_record, framework_write]
    worktree: .claude/worktrees/evidence-index
    branch: evidence-index
  - actor_id: reader-a
    role: reader
    declared_authority_non_enforced: [reading_write, receipt_record, manifest_write]
    worktree: .claude/worktrees/lettore
    branch: lettore
  - actor_id: mirror
    role: auditor
    declared_authority_non_enforced: [read_only]
    worktree: .claude/worktrees/mirror
    branch: mirror
  - actor_id: orchestrator
    role: coordinator
    declared_authority_non_enforced: [read_only, propose]
    worktree: null
    branch: null

multi_instance_roles: [reader]
```

- 🔴 **every `actor_id` is exclusive.** Two actors may share the role `reader`; two live
  sessions may never both be `reader-a`. The first version got this wrong;
- 🔴 **`declared_authority_non_enforced` is named for what it is.** The field is enumerated
  tokens rather than prose, because a sentence cannot be checked before a write — but **nothing
  checks it.** No validator reads it, no gate consults it, and Phase -1 could not demonstrate
  that any enforcement point exists on this transport. It is a **declaration of intent**, and
  calling it `authority` would have invited a reader to assume otherwise.
  **Validation and enforcement are formally deferred**: validating the field against what an
  actor actually does, and enforcing it at a write or a send, are separate future work
  conditioned on an enforcement point being demonstrated. Until then a token in this list
  constrains nobody;
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
No behaviour change. Its value is **recipient self-identification**: an actor can read what it
is instead of asking the operator, which is the failure that actually recurred. This needs no
transport and survives any change of transport.

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

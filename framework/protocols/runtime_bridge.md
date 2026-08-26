---
artifact: LEGEND protocol — RUNTIME BRIDGE (Claude Code ↔ OpenAI Codex)
protocol_id: RTBRIDGE
governance_version: 3.1.1
status: PROPOSED — binding once Mirror hostile review passes and the operator approves
normative: yes
scope: >
  How a LEGEND logical actor is executed by a runtime, and what each runtime adapter must
  guarantee before it may. It creates no actor, no role, no authority and no gate. Every
  obligation it references is allocated elsewhere and cited, never restated.
extends: >
  governance/GOVERNANCE_v3.1.1.md § 33 (Codex ≠ Orchestrator; ON_DEMAND_LEGEND_COLLABORATOR),
  § 34 (INTERACTION_PROFILE), § 38 (CONFIGURED != PROVEN), § 44 (actor classification), and
  governance/annex_j_runtime_control_plane.md § J.0 (guarantees not possessed).
rests_on: >
  framework/protocols/actor_identity_feasibility.md — the two-layer split between the LEGEND
  logical actor core and a transport adapter, and its own declaration that portability across
  transports was NOT tested. This protocol is the first artifact to test any part of it.
measured_against: >
  claude-code 2.1.232 and codex-cli 0.147.0, installed on the operator's machine on
  2026-08-26. Every runtime fact below carries its class and its instrument.
---

# RUNTIME BRIDGE — one core, two adapters, one verdict

```
                          LEGEND CORE
                     governance/ + roles/
                              |
                   runtime-neutral obligations
                     /                     \
            Claude adapter             Codex adapter
          .claude/settings.json         .codex/config.toml
                     \                     /
              framework/scripts/pre_tool_use_guard.py
                     → framework/scripts/guard_policy.py
                          ONE policy, ONE verdict
```

## 0 · The invariant, and the one sentence that makes it checkable

> `ACTOR_ID != RUNTIME != SESSION != WORKTREE != AUTHORITY`

Five things that are routinely collapsed into one, and the collapse is never announced —
it happens when a control exists on one side and not the other, and the choice of runtime
quietly becomes a choice of authority.

**The falsifier is mechanical and it is the point of this protocol:** take one actor, one
worktree, one `HEAD`, one task; execute it under each runtime; any *permitted or forbidden
action that differs* falsifies the bridge. `framework/scripts/runtime_parity.py` is that
falsifier, executable by anyone with the repository and both runtimes installed.

## 1 · What is runtime-neutral, and what an adapter is allowed to be

**Neutral, and the only place these may live:** the governance body and annexes, the role
contracts, the protocols, the skills, the gates (`legend_lint.py`,
`public_release_gate.py`, `run_release_regressions.py`, `fulltext_receipts.py`,
`growth_anchors.py`, `governance_fingerprint.py`), the write-guard **policy**, and the
verdict that policy returns.

**An adapter may only do three things**, and a fourth would make it a second core:

1. **register** the neutral engine with its runtime;
2. **translate** that runtime's payload onto the neutral engine's inputs;
3. **declare** what its runtime cannot do here.

🔴 **An adapter may never hold a rule.** If a sentence would change what is forbidden, it
belongs in the core and the adapter cites it. The test is deletion: remove both adapters
and the obligations must be unchanged — only their *reachability* may drop.

## 2 · Wire compatibility — measured, not assumed

Both `PreToolUse` schemas were read out of the installed runtimes rather than taken from
documentation about them.

| | Claude Code 2.1.232 | Codex 0.147.0 | class |
|---|---|---|---|
| input event key | `hook_event_name: "PreToolUse"` | same, per `pre-tool-use.command.input` | `DOCUMENTED` — schema extracted from the shipped binary |
| shell tool name | `Bash` | `shell_command` · `unified_exec` | `DOCUMENTED` — `core/src/tools/handlers/shell/shell_command.rs`, `ConfigShellToolType` |
| command key | `tool_input.command` (string) | `cmd` (string, "Shell script to run in the user's default shell") | `DOCUMENTED` |
| output object | `hookSpecificOutput.{hookEventName, permissionDecision, permissionDecisionReason}` | **identical**, per `pre-tool-use.command.output`; `permissionDecision ∈ allow\|deny\|ask` | `DOCUMENTED` |
| project registration | `.claude/settings.json` | `.codex/config.toml`, key `hooks.PreToolUse` | `OBSERVED` — type-probe with three controls, § 5 |
| output actually accepted | the full object | 🔴 **narrower than its own schema** — see § 5 | `REPORTED_BY_PEER` |

🔴 **The output side needed no adapter at all.** The object this repository already emitted
for Claude validates against Codex's own output schema unchanged. That is a fact about the
two runtimes, not an achievement of this protocol, and it is why the bridge is small.

🔴 **The input side needed exactly one non-obvious decision.** Codex carries some tool
payloads with `command` as an **argv list**. Stringifying a list and handing it to the
policy is not a translation, it is an accident:
`str(["bash","-lc","git add -A"])` puts the invocation inside quotes, and the policy
deliberately ignores quoted spans — so blanket staging would have been **allowed under
Codex and denied under Claude**. Argv is therefore reduced: a `-c`/`-lc` wrapper yields its
script argument, everything else is `shlex.join`ed. Pinned by
`framework/scripts/test_pre_tool_use_guard.py::ArgvIsReducedRatherThanStringified`.

## 3 · What Codex does NOT have here — declare, never work around

Body § 38 is unchanged by a change of runtime: `CONFIGURED != PROVEN`, and a capability
nobody smoke-tested is not a capability. These are the ones that differ, and each is a
declaration an actor owes at registration, not an obstacle to route around.

| Capability | Claude | Codex | Class |
|---|---|---|---|
| `.claude/skills/**` — 21 skills | discovered and applied automatically | readable **by path**, applied only when the task names one | `CAPABILITY_DIFFERENCE` |
| `.claude/agents/**` — 5 subagents | dispatchable; declare `tools:` and `model:` in Claude's own vocabulary | not dispatchable | `CAPABILITY_DIFFERENCE` |
| `launch/legend_launch.sh` — actor birth, lineage, `PENDING_BIRTH` | `claude`-bound at every step (`claude --version`, `claude agents --json`, `claude respawn`, `claude --name`) | does not run | `CAPABILITY_DIFFERENCE` |
| cross-session transport (`SendMessage`, `ListAgents`) | present | absent | `CAPABILITY_DIFFERENCE` |
| PubMed / literature MCP connectors | operator-authorized in the Claude client | not configured | `CAPABILITY_DIFFERENCE` |
| filesystem + network sandbox at the runtime layer | none | `restricted` / `restricted`, with `-s read-only` available | `CAPABILITY_DIFFERENCE`, **in Codex's favour** |
| the write-guard policy and its verdict | shared engine | shared engine | **no difference — that is the bridge** |
| every gate, every governance obligation, every role contract | repository-enforced | repository-enforced | **no difference** |

🔴 **The skill row is the honest one and it is not repaired by copying.** A second copy of
21 skills under a Codex-discoverable root would make them *discoverable* and make them
*two sources*, and the second one would be wrong within a fortnight — which is the failure
already observed on this very file across four `codex/*` branches. The bridge keeps one
copy and moves the difference from **hidden** to **declared**: same bytes, different
activation. `runtime_parity.py --skills` proves the "same bytes" half and fails if a second
copy ever appears.

🔴 **Nothing here promotes Codex.** Body § 33.1 — *"Codex ≠ Orchestrator; nessuna governance
per posizione"* — and § 33.4 — `ON_DEMAND_LEGEND_COLLABORATOR` — are untouched. This protocol
makes a Codex-hosted session *reach the same obligations*; it does not make it an actor, and
which actor a session is remains an operator assignment confirmed at registration.

## 4 · `GUARD_HARDENING_DEBT` — open, measured, and not this protocol's to close

The write-guard policy is narrow. On 2026-08-26, run from
`framework/scripts/runtime_parity.py --characterize`, it stopped 4 of 18 probed shapes.
These mutate the repository and are **allowed**, identically in both runtimes:

```
bash -c "git add -A"        sed -i          echo x > FILE       echo x >> FILE
echo x | tee FILE           cp over         mv over             python3 -c write
perl -pi
```

The shell-wrapper case has a cause worth naming rather than filing: the policy blanks
quoted spans, because it once blocked the very commit that documented it, and a shell
wrapper hides behind exactly that exemption.

**This is not a bridge defect and must not be reported as one.** It predates both adapters,
it is byte-identical on both sides, and widening the policy changes what is forbidden for
every actor — a different change, with a different blast radius and its own review.
`test_pre_tool_use_guard.py::KnownGapsAreCharacterisedNotClaimedFixed` asserts each gap is
**open and identical**, so closing one deliberately fails this list and forces it to be
updated with the fix rather than drifting away from it.

## 5 · What is unverified, and the exact experiment that would settle it

| Claim | Status | What would move it |
|---|---|---|
| `.codex/config.toml` is loaded as a project layer | **`OBSERVED`** | done: a wrong type on a known key (`model = 1`) exits 1 from the LEGEND worktree and the root checkout; an unknown key exits 0 |
| `hooks.PreToolUse` is a recognized key | **`OBSERVED`** | done: wrong types error on three consecutive runs while `zzz.PreToolUse=1` is ignored and `model=1` errors — three controls |
| `matcher` is required in a hook group | 🔴 **`WITHDRAWN`** | asserted from one run, does not reproduce over three with the controls green. `matcher` is how *this* repository scopes its hook, not a runtime requirement. Recorded because the claim had already been used to judge another actor's registration |
| the shipped registration parses | **`OBSERVED`** | done: `codex doctor` exits 0 on it, and 1 when a broken key is prepended |
| **the hook actually FIRES, before the shell mutates anything** | 🔴 **`UNVERIFIED` here, and `OBSERVED NOT FIRING` by a peer** — see § 8 | a Codex session that runs `git add -A` in a scratch fixture and is refused. `codex doctor` does not load hooks, so no local no-cost probe reaches it. **This is a spend** — `DEFAULT_EXTERNAL_SPEND = 0`, Annex J.4 — and needs `HUMAN_APPROVAL (TYPE: SPEND)` |
| hook trust: a project hook requires a trusted directory and a persisted hash | `DOCUMENTED` | the same session probe records what the trust prompt actually demands |

**While the firing row is `UNVERIFIED`, `runtime_parity.py` exits non-zero and a Codex actor
is read-only.** A registration that parses is not a control. What holds during a read-only
Codex pilot is the runtime sandbox (`-s read-only -a untrusted`), which is a stronger
statement than this protocol makes anywhere else — and it is a Codex property, not a LEGEND
one.

## 6 · Version-bound, like every runtime guarantee in this repository

`cross_session_transport.md` § 3 binds here without amendment: every guarantee that depends
on runtime behaviour is bound to `VERSION_OBSERVED`, and the version is a property of the
**session**, never of the machine. On a difference the guarantee does not become false, it
becomes **unmeasured**.

```
VERSION_OBSERVED       claude-code 2.1.232 · codex-cli 0.147.0
REVALIDATION_TRIGGER   the acting session's runtime version differs from either
```

Codex 0.150.0 was already available when this was written and is **not** the measured
version. Nothing here survives an upgrade by assumption — not the tool names, not the
schemas, not the config key, not the trust model.

## 7 · Acceptance tests

Every row is executed by `python3 framework/scripts/runtime_parity.py`, and each fails for
one reason.

| Check | Fails when |
|---|---|
| `ROUTER_REACHABILITY` | `AGENTS.md` stops routing to `CLAUDE.md`, or a link in its chain is unresolvable |
| `ROLE_CONTRACT_REACHABILITY` | a role named in the deployment profile has no contract, or the contract is unreadable |
| `SKILL_REACHABILITY` | a probed skill's `SKILL.md` is missing, or a second copy of it appears anywhere |
| `WRITE_GUARD_PARITY` | Claude and Codex payloads reach different verdicts on the same command |
| `AUTHORITY_PARITY` | the two adapters resolve different governance fingerprints for one role |
| `FAIL_CLOSED_ON_MISSING_BRIDGE` | a missing engine, a malformed payload or an unknown tool produces anything but a denial |
| `NO_SELF_ELECTION` | any artifact derives `ACTOR_ID` from runtime, session, worktree or branch |
| `NO_RUNTIME_AUTHORITY_ESCALATION` | a control exists on one side and not the other, or `CODEX_HOOK_FIRES` is still `UNVERIFIED` |

## 8 · A second, concurrent implementation — reported, not merged

While this protocol was being written, branch `codex-bridge-integration` (8 commits ahead of
`main`, in a worktree belonging to another session) was independently building the same
bridge. Four files collide by name: `AGENTS.md`, **this file**,
`scripts/guard_bash_command.py` and its test. **Nothing here merges, overrides or defers to
it.** Two writers on one problem is an Orchestrator adjudication, not an author's.

Two of that branch's results bear on rows above and are recorded because they are *stronger*
than what this work could reach, not because a peer said so:

🔴 **It ran the session probe, and the hook did not fire.** *"A `PreToolUse` command hook did
not run and did not block. The probed shell command executed normally and the hook script was
never invoked."* — Codex CLI 0.147.0, 2026-08-26. That moves § 5's last row from
"unmeasured" to "measured negative", and the read-only floor is doing all the work. Its own
record is careful about the cause: the hook-trust gate is an **inference from a flag's
existence**, explicitly not a measurement, and must not be reported as the reason.

🔴 **The output contract Codex enforces is narrower than the schema it ships.** That branch
reports `permissionDecision` accepting only `deny`, a denial with an empty
`permissionDecisionReason` being rejected, and `decision`, `continue`, `stopReason`,
`suppressOutput` and `updatedInput` all rejected on this event — against the
`pre-tool-use.command.output` schema extracted here, which *declares* all of them. Both can
be true: a declared wire and a narrower validator. **The engine happens to satisfy the
narrow reading** — it emits `hookSpecificOutput` with exactly `hookEventName`,
`permissionDecision: "deny"` and a non-empty reason, and emits nothing at all on allow — so
no change follows. It is written down because a future edit that starts emitting `continue`
or `updatedInput` would break Codex and pass every test in this repository.

Class: `REPORTED_BY_PEER`. Not reproduced here, and it is not promoted by being plausible.

**The two registrations disagree on where a Codex hook is declared** — `.codex/config.toml`
with a `hooks.PreToolUse` table here, `.codex/hooks.json` there. Neither has been observed
loading. The type-probe above is evidence for the first and there is no equivalent evidence
for the second, which settles nothing: an unrecognised config key is *ignored*, so a file the
loader never reads and a key the loader accepts but never reaches look identical from
outside. One probe answers both, and it is the same probe § 5 already owes.

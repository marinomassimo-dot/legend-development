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
  2026-08-26, plus codex 0.150.0-alpha.8 encountered in a real session on 2026-08-28 and
  NOT the version the schemas came from (§ 2.1, § 6). Every runtime fact below carries its
  class and its instrument.
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
| required input fields | `session_id, transcript_path, cwd, hook_event_name, tool_name, tool_input` | **ten**: those minus none, plus `model, permission_mode, tool_use_id, turn_id` — and `additionalProperties: false` | `DOCUMENTED` |
| 🔴 input fields **actually sent** | the six above **plus `effort` and `prompt_id`** | not re-measured | `OBSERVED` — 2026-08-29, claude-code 2.1.232 |
| shell tool name | `Bash` | `shell_command` · `unified_exec` | `DOCUMENTED` — `ConfigShellToolType` |
| 🔴 shell tool name **actually used** | `Bash` | **`exec`**, a code-mode tool carrying a JS body that calls `tools.exec_command({"cmd": …})` | `OBSERVED` — § 2.1 |
| command key | `tool_input.command` (string) | `cmd` (string), or an argv list, or inside a code-mode program | `DOCUMENTED` + `OBSERVED` |
| output object | `hookSpecificOutput.{hookEventName, permissionDecision, permissionDecisionReason}` | **identical**, per `pre-tool-use.command.output`; `permissionDecision ∈ allow\|deny\|ask`, `hookEventName` the only required key | `DOCUMENTED` |
| project registration | `.claude/settings.json` | `.codex/config.toml`, key `hooks.PreToolUse` | `OBSERVED` — type-probe with three controls, § 5 |
| output actually accepted | the full object | 🔴 **narrower than its own schema** — see § 8 | `REPORTED_BY_PEER` |

### 2.1 · The matcher list named two tools no session has ever called

🔴 **`OBSERVED`, 2026-08-28, over the whole local session corpus** — not over one session,
for a reason § 2.2 records.

```
INSTRUMENT   python3 framework/scripts/codex_runtime_probe.py
             reads ~/.codex/sessions/**/rollout-*.jsonl — read-only, no spend

             62   rollouts on disk
             17   with cwd inside this repository
        2988 × exec        in those 17          144 × wait      and nothing else
           0 × shell_command                      0 × unified_exec   — in ALL 62
        5795 × exec        across all 62
        1264 × exec_command  across all 62, and every one of them on cli_version ≤ 0.145
         367 × apply_patch · 38 × write_stdin
```

Every LEGEND-worktree call is the code-mode tool `exec`, carrying a JavaScript body of the
form `const r = await tools.exec_command({"cmd": …, "workdir": …});`. The two names
revision 2 registered — `shell_command` and `unified_exec` — appear **zero times in 62
sessions**, and `exec_command` survives only as the top-level tool of runtimes at or below
`0.145`, which is why it stays registered.

A two-matcher registration would therefore have policed **nothing** in any recorded session
even had it fired, while the battery went on reporting a guard that was never consulted.
`codex_runtime_probe.py` now prints `MATCHER_COVERAGE` — what is declared, what is used
here, what is used and *not* declared, and what is declared and never seen — so this cannot
go stale silently again. It currently reports `wait` as used-and-undeclared; `wait` blocks
on a process rather than starting one, so it is not a mutation path, and it is listed rather
than filtered so the next reader decides that for themselves.

Two things follow, and both are implemented rather than filed:

1. `.codex/config.toml` registers `exec`, `exec_command` and `apply_patch` as well;
2. `pre_tool_use_guard.py` reduces a code-mode body to the shell commands inside it, and
   **denies a body whose shell call it cannot read** — `tools.exec_command(buildArgs())` is
   a call the guard cannot clear, not a call it may ignore.

🔴 **The runtime that ran is not the runtime this protocol measured.** `codex --version` on
the CLI is `0.147.0`; the recorded sessions ran `0.150.0-alpha.8` in the VS Code extension.
Under `cross_session_transport.md` § 3 that makes every row above **unmeasured** for the
extension host rather than false — including the input schema, the output schema and the
config key.

### 2.2 · A count taken from a live file, and the correction

The first reading of this finding said *"all **20** of its tool calls"*, from one rollout,
and that number went into three committed artifacts. It was correct when taken and wrong an
hour later: **the session was still running**, and the same file reached 27 calls by the
time it was re-read.

The repair is not a bigger number. It is a claim that does not decay: **which tool names
appear at all, and which appear zero times**. A proportion over a closed set survives the set
growing; a count does not. The figures above are therefore all re-derivable by running
`codex_runtime_probe.py`, and the protocol quotes the probe rather than a transcription of
one reading of one file.

This is the second time on this candidate that a number was true of the tree that produced
it and false of the tree that carried it — the first is `CANDIDATE_CONTENT_HASH`, which is
why that manifest carries an invariance check.

🔴 **The row above says this table is narrower than the wire, and it was found the hard
way.** Revision 8 added a rule denying any unknown top-level payload key — Codex's own
input schema declares `additionalProperties: false`, so an extra key is a protocol
violation there. The rule refused **every command in the session that wrote it**, within a
minute, because claude-code 2.1.232 sends two keys that appear in neither the harness
contract nor this table, which says both schemas were *read out of the installed
runtimes*.

The rule now turns on **where** the key is. A key BESIDE `tool_input` cannot change what
the decision fields mean, so it is recorded as unmeasured and does not deny; a key INSIDE
`tool_input` is in the object the command is read out of, may itself carry a command, and
denies. Denying on a sibling makes the guard fail on every runtime release, and a guard
that fails on every release is a guard that gets disabled.

🔴 **The output side needed no adapter at all.** The object this repository already emitted
for Claude validates against Codex's own output schema unchanged. That is a fact about the
two runtimes, not an achievement of this protocol, and it is why the bridge is small.

🔴 **The input side needed three reductions, not one.** Codex carries a command as a
string, as an **argv list**, or — under code mode — not at all, with the shell call inside a
program body. Each is reduced deliberately, and getting any of them wrong is a runtime
granting authority rather than a cosmetic bug:

1. **argv.** `str(["bash","-lc","git add -A"])` wraps the whole invocation in a quoted
   string. Under revision 1's policy, which blanked quoted spans, that shape was **allowed
   under Codex and denied under Claude**. Argv is therefore reduced rather than joined: a
   `-c`/`-lc` wrapper yields its script argument, everything else is `shlex.join`ed. Pinned
   by `test_pre_tool_use_guard.py::ArgvIsReducedRatherThanStringified`. *(The quoted-span
   exemption that made this dangerous is itself gone — § 4.1 — but the reduction stays,
   because joining an argv would still hide a `-c` script inside one token.)*
2. **code mode.** § 2.1. Every `tools.exec_command({…})` in the body is extracted and
   judged; a call whose argument is not a readable literal is a denial.
3. **patch envelopes.** The `apply_patch` tool's payload names its own targets, and is
   policed as the shell form of the same thing.

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
| the write-guard policy and its verdict | shared engine, registered | shared engine, registered — **firing not demonstrated** | **same policy; NOT the same enforcement** |
| the gates (`legend_lint.py`, `public_release_gate.py`, `run_release_regressions.py`) | run by CI on push; **not run by any local hook** | identical, and the same nothing locally | **no difference, and the difference from "enforced" is § 3.1** |
| governance obligations and role contracts | **textual, plus audit and compensating controls** | identical | **no difference** |

### 3.1 · What "enforced" means here, narrowed to what is demonstrated

🔴 This table said `repository-enforced` for gates, obligations and role contracts. That
word claimed more than anything in the repository does, so it is withdrawn and replaced
with what was checked:

```
git config core.hooksPath          unset
$(git rev-parse --git-path hooks)  contains no hook — only the git-provided samples
.github/workflows/                 one workflow, public-release-gate.yml
                                   triggers: push, pull_request, workflow_dispatch
                                   runs: run_release_regressions.py · legend_lint.py
                                         public_release_gate.py
```

So: **CI enforcement exists and is real, on every push.** A local commit on a branch that
is never pushed passes through nothing at all, and every governance obligation — who may
write, which role a session holds, whether a candidate was reviewed — is **textual**, with
three compensating controls that are not the same thing as enforcement:

| Control | What it actually does | What it does not do |
|---|---|---|
| the `PreToolUse` write guard | refuses a *class* of shell mutation, in Claude; registered but **not demonstrated** in Codex | it does not know who is acting, or whether they may |
| the gates | fail a push, and fail a run someone chose to make | they do not run themselves before a commit |
| `governance_fingerprint.py`, the ledgers, `candidate_content_hash.py` | make a divergence **visible after the fact** | they detect; they do not prevent |

The honest sentence, and the one this protocol will stand behind: **the repository provides
textual authority, one enforced shell-mutation class, CI on push, and audit. It does not
provide repository-enforced authority, and no adapter changes that in either direction.**
Annex J.0 already says the system does not possess guarantees it has not built; this row
was quietly claiming one of them.

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

## 4 · The write-primitive model — the debt this protocol's earlier revision opened

Revision 2 of this protocol recorded nine command shapes that mutate the repository and
were **allowed**, called them `GUARD_HARDENING_DEBT`, and declined to close them. That was
the right call for a bridge change and the wrong state to leave a write floor in: the
operator's condition for a write-enabled runtime is that every demonstrated mutation path
required for parity is closed. They are closed, and the mechanism is the point.

### 4.0 · The executable model — revision 8

`COMMAND → ALLOW/DENY` has no answer that survives contact with a shell, because the set
of texts that mean "write" is not enumerable and § 4.5 measures what that costs. The
question changes shape:

```
COMMAND → PREDICTED EFFECT → TARGET → AUTHORIZATION → EXECUTION
        → OBSERVED EFFECT → MATCH / MISMATCH
```

Two rules, neither with an override:

```
UNKNOWN_EFFECT                        → DENY, under every authority, always
OBSERVED_EFFECT != AUTHORIZED_EFFECT  → FAIL CLOSED, WRITE RESULT INVALID
```

**Eleven effects, closed:** `READ · WRITE · DELETE · RENAME · STAGE · COMMIT ·
REF_MUTATION · NETWORK_WRITE · ARCHIVE_EXTRACT · PERMISSION_CHANGE · UNKNOWN_EFFECT`.
Closed is load-bearing: a derivation that cannot place a command in one of these emits
`UNKNOWN_EFFECT`, never nothing — "no effect derived" and "no effect" are the same value
in an open vocabulary and opposite values here.

**Six scopes:** `INSIDE_REPO · OUTSIDE_REPO · SCRATCH · NONLOCAL · UNNAMED · UNDERIVABLE`.
The last two are scopes, not errors: a command that mutates something it does not name and
one whose target needs a shell to resolve are both *derivable as mutations* and
*underivable as targets*, and both are refused by every authority including the highest.
An effect nobody can name is an effect nobody can review, and that — not the write itself
— is what put another actor's in-flight work into a commit describing something else.

**Six authorities, a monotone ladder**, each rung a superset of the one below:

```
READ_ONLY        the floor, and where an unattested session sits
SCRATCH_WRITE  + content and permission changes at SCRATCH / OUTSIDE_REPO
SHELL_DEFAULT  + STAGE and COMMIT at INSIDE_REPO      ← what the PreToolUse guard enforces
WORKTREE_WRITE + content mutation at INSIDE_REPO
REF_WRITE      + REF_MUTATION and PERMISSION_CHANGE at INSIDE_REPO
PUBLISH        + NETWORK_WRITE and remote refs — an operator act, never a runtime's
```

🔴 **An authority is a mapping from kind to scopes, not a product of the two.** `STAGE` and
`WRITE` both land at `INSIDE_REPO`, so any `kinds × scopes` product that admits
`git commit` also admits a shell write into `framework/` — it either loses the commit,
which is how work lands here, or regains the write revisions 1–7 exist to stop.

**Where each half lives.** `effect_model.py` holds the vocabulary and the algebra and
knows nothing of shells; `guard_policy.py` derives predicted effects; `post_effect_verify.py`
derives observed ones from a git delta and compares. The shared vocabulary is the only
reason the two ends can be compared at all — and the comparison is what distinguishes *the
hook refused this* from *the hook never fired*, which no `PreToolUse` hook can report about
itself.

`execution_attestation.py` binds nine dimensions — actor, runtime, runtime version,
session, task, worktree, branch, `HEAD`, authority — into one fingerprint, and revokes
write authority when any of them changes **or becomes underivable** across a resume. A
field nobody can read is not a field that stayed the same.

### 4.1 · Why the old policy leaked, in one sentence

It matched substrings and **blanked quoted spans** — an exemption added because it once
blocked the very commit that documented `git add -A`. That exemption is precisely where
`bash -c "git add -A"` hid. A blacklist long enough to catch the wrappers is also long
enough to catch the prose, so the choice was never between strict and lenient.

### 4.2 · What replaced it

`guard_policy.py` **parses** the command instead. `echo "git add -A"` and
`bash -c "git add -A"` carry the same bytes and differ in *structure*: in the first the
quoted span is an argument to `echo`, in the second it is a script argument to a shell, and
only the second is re-analysed as a command. Nothing is exempted for being quoted, and
nothing is condemned for containing a word.

Three outcomes, and the third is a synonym for neither of the others:

```
PROHIBITED    a mutation is derivable AND its target is inside the repository,
              or the command does not name its target at all
ALLOWED       no mutation is derivable, or every target is scratch space
UNDERIVABLE   a mutation is derivable and its target cannot be resolved
              → FAILS CLOSED, and only for a command already holding a write
```

The boundary is the **repository**, not the filesystem: a write to `/tmp`, to the
scratchpad or to a path outside the working tree is not this guard's business, and a write
whose root cannot be derived is treated as repository space.

### 4.3 · Closed, with the shape that closed each one

| Class | Shapes now refused |
|---|---|
| blanket staging | `git add -A/--all/.`, `git commit -a`, `git -C … add -A`, `… \| xargs git add` |
| shell wrappers | `sh/bash/zsh -c`, `-lc`, `env`, `nohup`, `nice -n N`, `timeout N`, `sudo`, `eval`, `$'…'`, a shell fed from a pipe |
| in-place editors | `sed -i`, `--in-place`, `perl -pi`, `perl -i.bak` |
| redirection | `>`, `>>`, `>\|`, and a redirect with no target |
| plain writes | `tee`, `cp`, `mv`, `install`, `ln`, `rm`, `truncate`, `dd of=`, `shred` |
| unnamed targets | `xargs`, `find -exec`, `find -delete`, a patch envelope |
| interpreted bodies | `python -c`, `perl -e`, `node -e`, `ruby -e`, and the heredoc-fed forms |
| patch envelopes | `apply_patch` and the `apply_patch` **tool**, policed by the paths the envelope names |
| expansions | `$(…)`/`` `…` `` bodies are analysed as commands; an expansion in `argv[0]` is `UNDERIVABLE` |

`test_pre_tool_use_guard.py::AlternateEncodingsDoNotEvadeTheParser` pins twenty of these.
🔴 **Every shape in that class was `ALLOWED` when it was first tried** — `eval`, `$'…'`,
a piped shell and an expanded `argv[0]` were found by attacking the parser *after* it was
written, not by listing what to block before writing it.

### 4.4 · The cost, measured rather than asserted

A guard that blocks ordinary work gets disabled and then guards nothing, so the other
direction is a test too. `NegativeControlsMustKeepWorking` holds 26 shapes that must
survive, and `TheRepositorysOwnDocumentedCommandsStillRun` is a **corpus**: it harvests
every shell line this repository documents in a fenced block and requires ≥ 94 % to pass.

On 2026-08-28 that harvest was 208 runnable commands from 59 files, of which **197 pass**.
The eleven that do not are named rather than rounded away:

- three lines in `PLAN-QUEUE-AND-CANDIDATE-CENSUS-001.md` redirect `git cat-file` output
  into the repository root — true positives; they should write to scratch;
- two lines in `HOSTILE_REVIEW_RUNBOOK.md` redirect into `"$review_root/…"`, a variable
  assigned in an *earlier* command — `UNDERIVABLE`, therefore denied. **This is a real
  behaviour change for that runbook** and the declared failure direction;
- two lines are this protocol's own § 4 table of prohibited shapes;
- four are documentation placeholders the harvest's own filter did not catch.

A variable assigned **in the same command** is resolved — `SC=/tmp/x; cmd > "$SC/f"` is
allowed — because that is the dominant way an agent writes to scratch and the value is
right there in the text being judged. A variable from the environment is not.

### 4.5 · `GUARD_HARDENING_DEBT` — what is still open

Printed by `runtime_parity.py --characterize` and asserted **open and identical** by
`test_runtime_parity.py::TheResidualDebtStaysDeclared`, so closing one of these fails that
test and forces this list to be updated with the fix:

```
a committed script that writes when invoked by name
```

That one is deliberate: invoking a reviewed script by name is the escape hatch every
denial names, and closing it would leave no way to do a legitimate write from the shell.

🔴 **Revision 8 closed the other five, and found twenty-seven that were not on this list
at all.** `chmod`/`chown`, `git reset --hard`, `git checkout -- .`, `git clean -fd` and
`git push` are now refused, not by adding five patterns but by deriving their EFFECT —
`PERMISSION_CHANGE`, `FILE_WRITE`, `FILE_DELETE`, `NETWORK_WRITE` — and asking whether the
acting authority grants it. `SHELL_DEFAULT` grants none of them.

They move to `GUARD_CLOSED_DEBT`, asserted in the **deny** direction in both runtimes by
`test_runtime_parity.py::test_every_closed_gap_stays_closed_on_both_sides`, alongside a
`GUARD_POSITIVE_FLOOR` asserted in the **allow** direction. A table that only asserts gaps
are open cannot notice one re-opening.

🔴 **The gap this list could not express.** Against the 46 repository-mutating shapes the
revision-8 brief enumerates, the revision-7 policy allowed **35**. Six were on this list.
The other twenty-nine were allowed *and* undeclared — and three of those were bypasses of
rules § 4.3 already claimed to hold. *(The block below is a results table, fenced as
`text` deliberately: `TheRepositorysOwnDocumentedCommandsStillRun` harvests every shell
line this repository documents in a shell-fenced block and would otherwise read these
rows as commands to run — which is how revision 7's own debt table ended up in its
denied list.)*

```text
echo x 1> framework/x    ALLOWED   `>` denied. `FD_REDIRECT` deleted `1>` before lexing.
cp -t framework /tmp/a   ALLOWED   `-t` moves the destination into a flag, and
                                   `operands()` skips flag values, so the derived
                                   "destination" was the last SOURCE.
echo hi                  ALLOWED   `CONTROL_TOKENS` has held "\n" since revision 1 and
git add -A                         `shlex(whitespace_split=True)` never emits one. Two
                                   lines lexed into ONE argv; only the first line's
                                   program was analysed. `;` split. `|` split. A newline
                                   did not, for seven revisions — and a multi-line block
                                   is the ordinary shape of agent shell use.
```

The lesson is not "the list was too short". A list of shapes is the wrong instrument:
`git push` was on it because someone thought of `git push`, and `1>` was not because
nobody thought of `1>`. An effect model refuses what it cannot classify, so the failure
mode of forgetting becomes a refusal instead of a hole. `UNKNOWN_EFFECT → DENY`, under
every authority, with no override.

### 4.6 · The boundary is the repository, and it was not

🔴 `classify_target` returned `SCRATCH` for anything under `/tmp`, `/private/tmp`,
`/var/folders` or any path with a `scratchpad` segment **before** consulting the
repository root. A git working tree living under any of them was therefore entirely
unguarded — and `TMPDIR` on macOS points into `/var/folders`, which is where every fixture
repository in this repository's own suites is created. The live floor written for revision
8 measured `echo tampered > kept.txt` as ALLOWED and read the file back to find it
rewritten.

Repository membership now beats the scratch prefix, for every effect kind. The exemption
exists so that work *outside* the tree is not this guard's business; inside the tree is
exactly its business.

## 5 · The hook state machine — what is unverified, and the one experiment that settles it

`CONFIGURED != DEMONSTRATED` is the unresolved property of this whole protocol, and it is
now a **derived state with six values** rather than a boolean. `runtime_parity.py
--hook-status` prints it with each row's evidence class:

```
NOT_CONFIGURED   no registration names the shared engine
CONFIGURED       a registration exists, parses, and names it
NOT_LOADED       the runtime's own `hooks/list` reports ZERO hooks here    ← revision 8
TRUST_PENDING    LOADED, and the runtime gates it behind a per-hook review
DEMONSTRATED     a session-probe receipt records a REFUSAL         ← the only passing state
NOT_FIRING       a session-probe receipt records the command running anyway
UNDERIVABLE      the registration or the receipt cannot be read at all
```

### 5.0 · 🔴 The state is `NOT_LOADED`, and the cause is measured

Revisions 2–7 recorded `TRUST_PENDING` and were careful to say the trust gate was an
inference from a flag's existence, explicitly not a measurement. That care was right. It
was also covering for an instrument that did not exist — and it does:

**`codex app-server` answers a `hooks/list` JSON-RPC method**, returning one
`HookMetadata` per loaded hook with `source`, `sourcePath` and `trustStatus`. No session,
no prompt, no turn, no model call — **not a spend under Annex J.4**. Asked from any LEGEND
worktree it returns `hooks: []`, with no warning and no error.

Four zeroes are not a finding. The controls, all from
`framework/scripts/codex_hook_state.py --explain`:

```
this repository's own .codex/config.toml at a TRUSTED PROJECT ROOT     5 hooks
the same file in a trusted NESTED git repository                       5 hooks
the same file in a git WORKTREE                                        0 hooks
the same file at that worktree's SHARED CHECKOUT                       5 hooks
```

**In a git worktree, codex-cli 0.147.0 resolves the project config layer through git to
the SHARED CHECKOUT and collects project hooks from there.** A `.codex/config.toml` in the
worktree contributes nothing, silently. Every LEGEND actor works in a worktree, and the
shared checkout has no `.codex` at all — the file is tracked and `main` predates it.

So the registration policed **nothing, in every worktree, for every actor**. This is a
measured cause for the `HOOK_NOT_FIRING` § 8 records, and it **replaces** the trust-gate
inference rather than confirming it: the ancestor IS trusted, the layer IS discovered, and
no error is raised.

🔴 It also corrects this file. `.codex/config.toml` says its command path is relative
because "`codex doctor` reported `repo root` as the worktree". That is `doctor`'s notion of
a repository root; the **config layer** uses a different one.

`NOT_LOADED` sits BELOW `TRUST_PENDING`: a registration that never loaded is not on either
side of the gate, and naming the gate for it claims a state it never reached.

| Claim | Status | Instrument |
|---|---|---|
| `.codex/config.toml` is loaded as a project layer | **`OBSERVED`** | a wrong type on a known key (`model = 1`) exits 1 from the worktree and the root checkout; an unknown key exits 0 |
| `hooks.PreToolUse` is a recognized key | **`OBSERVED`** | wrong types error on three consecutive runs while `zzz.PreToolUse=1` is ignored and `model=1` errors — three controls |
| `matcher` is required in a hook group | 🔴 **`WITHDRAWN`** | asserted from one run, does not reproduce over three with the controls green. `matcher` is how *this* repository scopes its hook, not a runtime requirement. Recorded because the claim had already been used to judge another actor's registration |
| the shipped registration parses | **`OBSERVED`** | `codex doctor --json` reports `config.load: ok` on it, and errors when a broken key is prepended |
| a per-hook trust gate exists in the runtime | **`DOCUMENTED`** | the installed binary's own strings: *"New hook - review required"*, *"Modified since last trusted - review required"*, *"Trusted"*, *"Managed hooks are always on"*, *"1 hook needs review before it can run."*, and a `bypass_hook_trust` config key |
| directory trust is granted for this repository | **`OBSERVED`** | `~/.codex/config.toml` carries `[projects."…/legend-public"] trust_level = "trusted"`, which every worktree beneath it inherits |
| **which side of the per-hook gate this registration is on** | 🔴 **`UNVERIFIED`** | nothing in the repository records it, and `codex doctor --json` reports **18 checks, none about hooks** — the word does not occur in its output |
| **the hook FIRES, before the shell mutates anything** | 🔴 **`UNVERIFIED` here; `OBSERVED NOT FIRING` by a peer** — § 8 | a Codex session that runs `git add -A` in a scratch fixture and is refused |

🔴 **`TRUST_PENDING` is a state, not a diagnosis.** It says the runtime declares a gate and
this repository cannot see which side of it we are on. It does **not** say the trust gate
is why a peer's probe did not fire — that remains an inference from a flag's existence, and
naming a cause we have not measured would repeat the withdrawn `matcher` claim in a new
place.

### 5.1 · The ONE operator action, and the ONE test

Everything reachable without an operator is done. What remains is a single interactive act
and a single observation, and it is a **spend** — Annex J.4, `DEFAULT_EXTERNAL_SPEND = 0` —
so it needs `HUMAN_APPROVAL (TYPE: SPEND)`. **No `APPROVAL_ID` is prefilled and none
exists.**

```
ACTION   Open ONE Codex session with cwd = a LEGEND worktree, and — if the runtime shows
         a hook-review prompt — review and TRUST the hook it names.
TEST     In that session, run:   git add -A
EXPECT   refusal, carrying the guard's own sentence ("Blanket staging is blocked in this
         repository") — the runtime renders it as "Command blocked by PreToolUse hook: …"
RECORD   framework/state/codex_hook_probe.json
         {"schema":"codex_hook_probe/1","recorded_on":"…","codex_version":"…",
          "originator":"codex_cli|codex_vscode","cwd":"…","probe_command":"git add -A",
          "observed":"REFUSED"|"EXECUTED","session_transcript":"…rollout-….jsonl"}
```

`observed` takes exactly `REFUSED` or `EXECUTED`. Any other value, or any missing key, is
`UNDERIVABLE` — **a receipt that records a verdict without its provenance proves nothing**,
and `test_runtime_parity.py` asserts that a receipt containing only `{"observed":"REFUSED"}`
does not reach `DEMONSTRATED`.

**While the firing row is not `DEMONSTRATED`, `WRITE_ENABLED_PARITY` fails, `--bootstrap`
reports `READ_ONLY`, and a Codex actor is read-only.** A registration that parses is not a
control. What holds during a read-only Codex pilot is the runtime sandbox — the recorded
2026-08-28 session ran under `sandbox_policy: read-only`, `permission_profile.file_system:
restricted/read`, `network: restricted`, `approval_policy: never` — and that is a Codex
property, not a LEGEND one.

## 6 · Version-bound, like every runtime guarantee in this repository

`cross_session_transport.md` § 3 binds here without amendment: every guarantee that depends
on runtime behaviour is bound to `VERSION_OBSERVED`, and the version is a property of the
**session**, never of the machine. On a difference the guarantee does not become false, it
becomes **unmeasured**.

```
VERSION_OBSERVED       claude-code 2.1.232 · codex-cli 0.147.0 (CLI, schemas + config probes)
VERSION_ENCOUNTERED    codex 0.150.0-alpha.8 (VS Code extension, the 2026-08-28 session)
REVALIDATION_TRIGGER   the acting session's runtime version differs from VERSION_OBSERVED
```

🔴 **The rule has already fired once, and the finding is what § 2.1 records.** The only real
Codex session run against this repository was hosted by `0.150.0-alpha.8`, not by the
`0.147.0` CLI these schemas came out of — and the tool it called was one the registration
did not name. That is the exact failure this clause exists to catch: not a guarantee turning
false, but a guarantee describing a runtime nobody was running.

So `VERSION_ENCOUNTERED` is now a field of its own, because "the version we measured" and
"the version an actor was hosted on" were silently the same sentence and are not the same
fact. Nothing here survives an upgrade by assumption — not the tool names, not the schemas,
not the config key, not the trust model.

## 7 · Acceptance tests — ten dimensions, two verdicts

Every row is executed by `python3 framework/scripts/runtime_parity.py`, and each fails for
one reason. **`READ_ONLY_PARITY` and `WRITE_ENABLED_PARITY` are separate verdicts and
neither implies the other**, because the question "may this actor read the same rules?" and
the question "may it write under the same control?" have different answers today.

| Check | Read floor | Write floor | Fails when |
|---|:--:|:--:|---|
| `ROUTER_PARITY` | ● | ● | `AGENTS.md` stops routing to `CLAUDE.md`, or a link in its chain is unresolvable |
| `ACTOR_ID_PARITY` | ● | ● | any artifact derives `ACTOR_ID` from runtime, session, worktree or branch |
| `ROLE_REACHABILITY` | ● | ● | the **assigned** actor's contract is missing, unreadable, or never arrived at from the router; or no actor is assigned |
| `GOVERNANCE_FINGERPRINT_PARITY` | ● | ● | the two adapters resolve different fingerprints for one role |
| `SKILL_REACHABILITY` | ● | ● | a probed skill's `SKILL.md` is missing, or a second copy of it appears anywhere |
| `MISSING_BRIDGE_FAIL_CLOSED` | ● | ● | a missing engine, a missing policy, a malformed payload or an unknown tool produces anything but a denial |
| `GUARD_POLICY_PARITY` | | ● | three payload shapes disagree, **or all three agree on the wrong answer** |
| `HOOK_REGISTRATION_PRESENT` | | ● | either runtime's registration is absent, malformed, or names a different engine |
| `HOOK_DEMONSTRATED` | | ● | the hook state is anything other than `DEMONSTRATED` |
| `NO_RUNTIME_AUTHORITY_ESCALATION` | | ● | a control exists on one side and not the other, or a matcher is missing for a tool the runtime actually uses |

### 7.1 · Three properties the battery now has and did not

🔴 **A missing safety component can no longer be green.** The engine is never imported by
the battery — revision 2 imported it at module scope and then offered a check for its
absence, which made that branch unreachable. It is invoked as a subprocess, its absence is
a row, and `test_runtime_parity.py::AMissingSafetyComponentIsNeverGreen` executes six arms
against **fixture trees with the component actually removed**: `ENGINE_MISSING`,
`ENGINE_IMPORT_FAILURE`, `POLICY_MISSING`, `HOOK_REGISTRATION_MISSING`,
`HOOK_CONFIG_MALFORMED`, `PAYLOAD_MALFORMED`.

🔴 **Agreement is not correctness.** `GUARD_POLICY_PARITY` carries the verdict each command
must reach, so two runtimes that both allow blanket staging fail instead of agreeing
perfectly. Revision 2 compared the runtimes only to each other.

🔴 **No actor is ever elected.** `ROLE_REACHABILITY` takes an `ACTOR_ID` the operator
assigns and refuses to substitute a default: no actor is `UNRESOLVED` and fails, an unknown
role is refused rather than approximated, and the router must *name* the path the contract
lives at — a contract that merely exists and is readable is not reachable.

## 7.2 · Pilot stage readiness

`runtime_parity.py --stages` computes each stage from **its own** conditions. Nothing is
promoted because a lower stage passed.

| Stage | Floor | Its own extra condition |
|---|---|---|
| `MIRROR_READ_ONLY_CODEX` | read-only | a Codex sandbox at read-only |
| `MIRROR_WRITE_CODEX` | write | `HOOK_DEMONSTRATED` from a session probe |
| `SCIENTIST_C_READ_ONLY_CODEX` | read-only | `roles/scientist.md` reachable for the assigned actor |
| `SCIENTIST_AB_READ_ONLY_CODEX` | read-only | `roles/scientist.md` reachable for the assigned actor |
| `PLAN_CODEX` | write | Plan authors candidates, which is a write |
| `ORCHESTRATOR_CODEX` | write | an `ACTIVE` lease, which body § 33.1 does not grant by runtime |

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
`suppressOutput` and `updatedInput` all rejected on this event.

**One half of that is now checked here and the other is not, and the two must not be
reported as one claim.** Re-extracting `pre-tool-use.command.output` from the installed
binary confirms the *schema* side exactly as the peer described it: every one of those keys
is declared, `permissionDecision ∈ allow|deny|ask`, and `hookEventName` is the only
required member of `hookSpecificOutput`. What is **not** reproduced here is the peer's
claim about the *validator* — that the runtime rejects at load or at use what the schema
declares. That needs a firing hook, which is the same thing § 5.1 owes.

Both can be true: a declared wire and a narrower validator. **The engine happens to satisfy
the narrow reading** — it emits `hookSpecificOutput` with exactly `hookEventName`,
`permissionDecision: "deny"` and a non-empty reason, and emits nothing at all on allow — so
no change follows. It is written down because a future edit that starts emitting `continue`
or `updatedInput` would break Codex and pass every test in this repository.

Class: `REPORTED_BY_PEER` for the validator, `DOCUMENTED` for the schema. The second was
reproduced; the first is not promoted by being plausible.

🔴 **One further peer-adjacent fact, derived here and not from any report.** Codex's own
trust model gates a project hook per hook, and `~/.codex/config.toml` grants *directory*
trust to `/Users/massimo/Desktop/legend-public` — which every worktree beneath it inherits,
including this one and the peer's. Directory trust is therefore **not** a difference between
the two registrations, and cannot be either branch's explanation for a probe not firing.

**The two registrations disagree on where a Codex hook is declared** — `.codex/config.toml`
with a `hooks.PreToolUse` table here, `.codex/hooks.json` there.

🔴 **Settled in revision 8, and the answer is not "one probe for both".** `hooks/list`
(§ 5.0) answers each separately, with no spend:

```
[hooks] PreToolUse = [ … ]      loads — 5 hooks, source "project"
hooks = "./hooks.json"          a TYPE ERROR:
                                `invalid type: string "./hooks.json",
                                 expected struct HooksToml`
```

So the group table **this** file ships is the correct shape, and the peer branch's
`.codex/hooks.json` is not a shape codex-cli 0.147.0 accepts. That was reachable all along
and neither branch reached it: revision 7's type-probe could tell that `hooks` was a
*recognised key* and could not tell **what type it was recognised as**, and read that
ambiguity as confirmation of the shape already written.

The correct shape still loads nothing here, for the reason § 5.0 measures. Being right
about the shape and wrong about the location produces exactly the same zero.

---
artifact: INTEGRATION_CANDIDATE — Claude ↔ Codex minimum runtime bridge
candidate_id: CAND-20260826-RTBRIDGE
revision: 7
task_id: RTBRIDGE-P00-001
author: plan
authored_on: 2026-08-26
revised_on: 2026-08-28
governance_version: 3.1.1
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1), so this
  file is outside the candidate content domain and cannot move the hash it records
partition: >
  SIX REVIEW UNITS over ONE tip, and the single tip is argued in § 2 rather than assumed.
  A reviewer may accept or reject each unit independently; § 10 gives each one its own revert.
human_approval: >
  NOT REQUESTED for the content. One item DOES require it and is not prefilled: the Codex
  session probe of § 6.2 is a spend under Annex J.4 (DEFAULT_EXTERNAL_SPEND = 0) and needs
  HUMAN_APPROVAL (TYPE: SPEND) before anyone runs it.
---

# INTEGRATION_CANDIDATE — `CAND-20260826-RTBRIDGE`

## 1 · Manifest (Annex D.2)

```
CANDIDATE_ID              CAND-20260826-RTBRIDGE
BASE_HEAD                 f2b8ecf11e77ebe86e6e17b6348e6469cc2e432b
                          🔴 NOT canonical main. This is the branch point of the unit, and
                          it is used deliberately: main is 788c357 and this branch carries
                          80 prior Plan commits that are NOT part of this candidate. Hashing
                          against main would bind all of them to this review.
TIP                       baaa8e4d27240b9b6d038db850f038a5350be67e
                          the last commit in the CONTENT domain. This file is committed
                          after it, and cannot move the hash — see the invariance note.
CANDIDATE_CONTENT_HASH    b8d3bfd7c44f41dd4217eec507d2b196504d934c2dddd0c5d33205bc774a86bc
                          🔴 SUPERSEDES, newest first:
                            cfab7840…2c8bfe  tip b4388ae  revision 6
                            176b606e…1756ba  tip 6555117  revision 5
                            99b24e00…2807d4  tip 6a4a3a4  revision 4
                            4d55c865…07ad832  tip e40e620  revision 3
                            7f88cf34…8323f2a  tip 7a867e7  revision 2
                            6277b98e…9678d93  tip cda34cf  revision 1
                          Each was correct for the tree it named and is superseded, not
                          withdrawn (Annex D.2). They stay visible because a candidate that
                          silently rewrites its own hash teaches a reviewer to trust the
                          current value, which is the one thing a hash cannot ask for.
CHANGE_CLASS              MAJOR — it reverses what a safety control does on a malformed
                          payload (§ 5), it introduces a second registrant of that control,
                          and revision 3 CHANGES WHAT IS FORBIDDEN FOR EVERY ACTOR IN BOTH
                          RUNTIMES (§ 7). Mirror classifies; this field is the author's
                          declaration and not the classification.
RECIPE                    python3 governance/scripts/candidate_content_hash.py \
                            --base f2b8ecf11e77ebe86e6e17b6348e6469cc2e432b \
                            --tip  baaa8e4d27240b9b6d038db850f038a5350be67e
INVARIANCE                Run the same recipe with --tip set to the branch tip that carries
                          THIS FILE. It must print the same value, because every commit
                          after baaa8e4 on this branch touches only governance/candidates/
                          or is an empty correction commit — both verified to leave the
                          value unmoved,
                          which P5.1 excludes. If it does not, the hash is stale and this
                          manifest is wrong — check that before reviewing anything else.
CONTENT DOMAIN TOUCHED    14 paths, by `git diff --name-only <base> <tip>` minus the
                          control plane:
                            AGENTS.md
                            .codex/config.toml
                            framework/protocols/runtime_bridge.md
                            framework/scripts/guard_policy.py
                            framework/scripts/pre_tool_use_guard.py
                            framework/scripts/runtime_parity.py
                            framework/scripts/codex_runtime_probe.py       (new)
                            framework/scripts/mutate_guard_suite.py        (new)
                            framework/scripts/test_codex_runtime_probe.py  (new)
                            framework/scripts/test_pre_tool_use_guard.py
                            framework/scripts/test_runtime_parity.py
                            scripts/guard_bash_command.py
                            scripts/test_guard_bash_command.py
                            scripts/run_release_regressions.py
```

## 2 · Why six units and one commit series

Body § 11 wants milestone granularity and the dispatch asked for units kept apart *where
practical*. It is not practical here, and the reason is checkable rather than stylistic:
**every split leaves the tree red.**

```
router   names   the adapter registration and the engine   → link targets break without them
adapter  names   the shared engine                          → the engine must land first
battery  asserts router AND adapter AND engine together     → it fails without any one
policy   is asserted by three test files at once            → they move together or fail
```

The artifacts are one change, and the units below are one *review* surface each, with
independent accept/reject and independent reverts in § 10.

## 3 · The six units

| Unit | What it is | Files |
|---|---|---|
| **A · router bridge** | `AGENTS.md` stops carrying rules and routes; the contract it routes under | `AGENTS.md`, `framework/protocols/runtime_bridge.md` |
| **B · skill bridge** | the decision **not** to copy, made checkable | *(no separable artifact — see § 4)* |
| **C · hook adapter / shared guard** | one policy, one engine, two registrations, three payload shapes | `framework/scripts/pre_tool_use_guard.py`, `scripts/guard_bash_command.py`, `.codex/config.toml` |
| **D · parity battery + bootstrap** | the falsifier, and the fail-closed bootstrap | `framework/scripts/runtime_parity.py`, `framework/scripts/test_runtime_parity.py`, `scripts/run_release_regressions.py` |
| **E · the write-primitive model** 🆕 | the guard stops matching strings and starts parsing commands; twenty mutation paths close | `framework/scripts/guard_policy.py`, `framework/scripts/test_pre_tool_use_guard.py`, `scripts/test_guard_bash_command.py` |
| **F · durable instruments** 🆕 | every machine-local derivation becomes a re-runnable script, and the suites are themselves tested | `framework/scripts/codex_runtime_probe.py`, `framework/scripts/mutate_guard_suite.py` |

🔴 **Unit E is the one with a blast radius outside this candidate.** It changes what every
actor in this repository may type, in both runtimes, the moment it lands. § 7 measures that
cost rather than asserting it is small.

## 4 · Unit B produced no artifact, and that is the finding

The dispatch asked for the minimum bridge letting Codex consume the same skill source.
**The minimum turned out to be nothing**, and the honest report is that no file implements
it:

- a **symlink** into a Codex-discoverable root is refused by the runtime itself — the
  installed binary carries *"Symbolic links are not allowed in skills"*;
- a **copy** under `$CODEX_HOME/skills` makes 21 skills discoverable and makes them two
  sources. That failure is not hypothetical on this exact file: on 2026-08-26 four live
  `codex/*` branches were carrying an `AGENTS.md` whose sync rule contradicted `main`, and
  had been for sixteen days, because nothing compared them;
- **explicit path loading** keeps one copy and costs one sentence in `AGENTS.md`.

So the bridge is: same bytes, different activation, and the difference is *declared* rather
than closed. `runtime_parity.py --skills` proves the "same bytes" half and
`test_runtime_parity.py` proves the check fails when a second byte-identical copy appears.

🔴 **What is NOT bridged and must not be read as bridged:** Claude *discovers and applies*
these skills; Codex reads them only when a task names one. That is a
`CAPABILITY_DIFFERENCE`, it is listed in `runtime_bridge.md` § 3, and a Codex actor owes it
as a declaration at registration under body § 38.

**Corroborated on 2026-08-28 rather than left as a claim.** The recorded Codex session
enumerated the skill directory by path and read `SKILL.md` files deliberately; nothing was
auto-applied. The dispatch that ran it recorded `legend-locator-audit` as
`EXPLICITLY_REACHED` and **not** `AUTO_DISCOVERED`, which is this row observed rather than
predicted.

## 5 · The one behaviour reversed, and why it is MAJOR

`scripts/guard_bash_command.py` returned no output on a payload it could not parse, and the
command ran. The code said so on purpose: *"never block on a malformed payload"*.

That is defensible with one registrant — a malformed payload then means a harness bug, and
blocking every command on a harness bug is worse than the bug. **It stops being defensible
with two**, because "the payload did not parse" becomes indistinguishable from "this
runtime's payload is shaped differently", and the fail-open answer hands the unrecognised
runtime a guard that says yes to everything.

The reversal is in the code and in its test, which was renamed rather than edited quietly:
`test_malformed_payload_never_blocks` → `test_malformed_payload_fails_closed`.

**The risk this creates, stated rather than discovered later:** if a future runtime version
changes its payload shape, every shell command is denied until `SHELL_TOOLS` or the key
list is updated. That is loud and diagnosable — the denial names the file and the constant
to edit — and it is the failure direction chosen deliberately.

## 6 · The hook: what moved in revision 3, and what did not

### 6.1 · The matcher list named two tools no session has ever called

🔴 **The finding of this revision**, and it is a corpus rather than a session.

```
INSTRUMENT   python3 framework/scripts/codex_runtime_probe.py    read-only, no spend

     62   rollouts in ~/.codex/sessions
     17   with cwd inside this repository
  2988 x  exec        in those 17            144 x wait,  and nothing else
     0 x  shell_command      0 x unified_exec      -- in ALL 62 rollouts
  5795 x  exec        1264 x exec_command (every one on cli_version <= 0.145)
   367 x  apply_patch   38 x write_stdin
```

Every LEGEND-worktree call is the code-mode tool `exec`, carrying a JavaScript body of the
form `const r = await tools.exec_command({"cmd": ..., "workdir": ...});`. The two names
revision 2 registered appear **zero times in sixty-two sessions**.

Revision 2's registration would therefore have policed **nothing** in any recorded session
even had it fired, while the battery reported a guard that was never consulted. Both halves
are fixed: `.codex/config.toml` registers `exec`, `exec_command` and `apply_patch`, and the
adapter reduces a code-mode body to the shell commands inside it -- denying a body whose
shell call it cannot read, because `tools.exec_command(buildArgs())` is a call the guard
cannot clear, not one it may ignore. `codex_runtime_probe.py` prints `MATCHER_COVERAGE`
(declared, used-here, used-and-undeclared, declared-and-never-seen) so this list cannot go
stale silently again.

🔴 **Self-correction, and why the figures above are proportions.** The first reading said
*"all 20 of its tool calls"*, taken from one rollout, and that number went into three
committed artifacts. **The session was still running**; the same file held 27 calls an hour
later. The count was true of the tree that produced it and false of the tree that carried
it -- the second time on this candidate, after `CANDIDATE_CONTENT_HASH`. A count over a
growing set decays; *which names appear zero times* does not, and it is also the claim the
matcher list actually rests on.

🔴 **The runtime that ran is not the runtime revision 2 measured.** `codex --version` is
`0.147.0`; the session was `0.150.0-alpha.8`. Under `cross_session_transport.md` § 3 every
schema row in `runtime_bridge.md` § 2 is **unmeasured** for that host rather than false, and
`VERSION_ENCOUNTERED` is now a field of its own beside `VERSION_OBSERVED`.

### 6.2 · `CONFIGURED != DEMONSTRATED`, now a six-valued state

`runtime_parity.py --hook-status` derives it and prints each row's evidence class:

```
NOT_CONFIGURED   no registration names the shared engine
CONFIGURED       a registration exists, parses, and names it
TRUST_PENDING    configured, AND the runtime gates it behind a review nobody here can read
DEMONSTRATED     a session-probe receipt records a REFUSAL         ← the only passing state
NOT_FIRING       a session-probe receipt records the command running anyway
UNDERIVABLE      the registration or the receipt cannot be read at all
```

Today it is **`TRUST_PENDING`**, and the word is chosen carefully:

| Fact | Class | Instrument |
|---|---|---|
| the registration parses under both interpreters | `OBSERVED` | `codex doctor --json` → `config.load: ok`; `tomllib` parses 5 hook groups under Python 3.12 |
| a per-hook trust gate exists in the runtime | `DOCUMENTED` | the binary's own strings: *"New hook - review required"*, *"Modified since last trusted - review required"*, *"Trusted"*, *"Managed hooks are always on"*, *"1 hook needs review before it can run."*, plus a `bypass_hook_trust` key |
| directory trust is granted for this repository | `OBSERVED` | `~/.codex/config.toml`: `[projects."…/legend-public"] trust_level = "trusted"`, inherited by every worktree beneath it |
| **which side of the per-hook gate we are on** | 🔴 `UNVERIFIED` | nothing in the repository records it, and `codex doctor --json` reports **18 checks, none about hooks** — the word does not occur in its output |
| **the hook fires before the shell mutates** | 🔴 `UNVERIFIED` here; `OBSERVED NOT FIRING` by a peer | a session probe |

🔴 **`TRUST_PENDING` is a state, not a diagnosis.** It does not say the trust gate is why a
peer's probe did not fire. That remains an inference from a flag's existence, and naming a
cause nobody measured would repeat the withdrawn `matcher` claim of revision 2 in a new
place. Revision 3 adds one fact that *narrows* the field: directory trust covers the peer's
worktree and this one identically, so it cannot be the difference between the two
registrations.

### 6.3 · A claim revision 2 made and withdrew — still withdrawn

An earlier revision stated that `matcher` is **required** in a Codex hook group, from a
single probe run. Re-run three times with three controls green, a matcher-less group is
accepted. The claim is withdrawn, and recorded rather than deleted because it had already
been used to judge another actor's registration: `.codex/hooks.json` on
`codex-bridge-integration` declares a group with no matcher, and on the withdrawn claim
that file would have been called broken. It is not.

### 6.4 · The ONE operator action and the ONE test

Everything reachable without an operator is done. What remains is a single interactive act
and a single observation. It is a **spend** — Annex J.4, `DEFAULT_EXTERNAL_SPEND = 0` — so
it needs `HUMAN_APPROVAL (TYPE: SPEND)`. **No `APPROVAL_ID` is prefilled and none exists.**

```
ACTION   Open ONE Codex session with cwd = a LEGEND worktree and, if the runtime shows a
         hook-review prompt, review and TRUST the hook it names.
TEST     In that session, run:   git add -A
EXPECT   refusal carrying the guard's own sentence ("Blanket staging is blocked in this
         repository"); the runtime renders it as "Command blocked by PreToolUse hook: …"
RECORD   framework/state/codex_hook_probe.json
         {"schema":"codex_hook_probe/1","recorded_on":"…","codex_version":"…",
          "originator":"codex_cli|codex_vscode","cwd":"…","probe_command":"git add -A",
          "observed":"REFUSED"|"EXECUTED","session_transcript":"…rollout-….jsonl"}
```

`observed` takes exactly `REFUSED` or `EXECUTED`. Any other value, or any missing key, is
`UNDERIVABLE`: `test_runtime_parity.py` asserts that a receipt containing only
`{"observed":"REFUSED"}` does **not** reach `DEMONSTRATED`, because a receipt that records a
verdict without its provenance proves nothing. **No receipt exists in this candidate and
none is fabricated.**

## 7 · `GUARD_HARDENING_DEBT` — closed, and what closing it costs

Revision 2 recorded nine shapes that mutate the repository and were allowed, called them
debt, and declined to close them. Operator decision 5 makes closing them a condition of the
write floor, so they are closed.

### 7.1 · Why the old policy leaked

It matched substrings and **blanked quoted spans** — an exemption added because the guard
once blocked the very commit that documented `git add -A`. That exemption is exactly where
`bash -c "git add -A"` hid. A blacklist long enough to catch the wrappers is also long
enough to catch the prose.

### 7.2 · What replaced it

The command is **parsed**. `echo "git add -A"` and `bash -c "git add -A"` carry the same
bytes and differ in structure: in the first the quoted span is an argument to `echo`, in the
second a script argument to a shell, and only the second is re-analysed. Nothing is exempt
for being quoted; nothing is condemned for containing a word. Three outcomes:

```
PROHIBITED    a mutation is derivable AND its target is inside the repository,
              or the command does not name its target at all
ALLOWED       no mutation is derivable, or every target is scratch space
UNDERIVABLE   a mutation is derivable and its target cannot be resolved → FAILS CLOSED
```

### 7.3 · Twenty shapes closed, and four of them were found by attack

Every shape on the dispatch's list is refused, plus wrappers, expansions and encodings:
`git add -A/--all/.`, `git commit -a`, `git -C … add -A`, `xargs git add`, `sh/bash/zsh -c`,
`-lc`, `env`, `nohup`, `nice -n N`, `timeout N`, `sudo`, `sed -i`, `perl -pi`, `>`, `>>`,
`tee`, `cp`, `mv`, `rm`, `truncate`, `dd of=`, `install`, `ln`, `apply_patch` (shell **and**
tool), `find -exec`, `find -delete`, `python/perl/ruby/node -c|-e`, and the heredoc forms.

🔴 **Four were `ALLOWED` when first tried, and were found by attacking the parser after it
was written rather than listed before:** `eval "…"`, `$'…'` ANSI-C quoting, a shell fed
from a pipe (`echo 'git add -A' | sh`), and an expansion in `argv[0]`
(`$(echo git) add -A`).

### 7.4 · GUARD_BYPASS_COUNT = 0 against the probed set — with its denominator

Counted from the committed tests, not from a scratch harness, so a reader can re-derive
each figure from the file that holds it:

```
test_pre_tool_use_guard.py
  20  closed shapes            TheDemonstratedMutationPathsAreClosed.CLOSED
  28  alternate encodings      AlternateEncodingsDoNotEvadeTheParser.EVASIONS
  33  negative controls        NegativeControlsMustKeepWorking.ALLOWED
 208  documented commands      TheRepositorysOwnDocumentedCommandsStillRun, 197 must pass
runtime_parity.py
  20  battery commands x 3 payload shapes, identical AND carrying the right verdict
mutate_guard_suite.py
  31  mutations of the policy, the adapter and the battery
```

🔴 **And the count that matters more: TWO bypass classes were shipped and then found**,
after all of the above was already green — `echo "$(git add -A)"` (with its backtick twin)
and `FOO=1 git add -A`, § 11.4.1. Measured across the shipped commits: both LEAK at
`a7589a2` and `6a4a3a4`, both denied from `0782c37` onward.

Neither was on any list, because a list is written by someone who already knows what to
look for. **`GUARD_BYPASS_COUNT = 0` means *against these probes, today*, and it has read 0
before while two shapes walked through.** A reviewer should read it as a statement about
coverage, not about the shell.

**Zero is a property of the probed set, not of the shell.** The residual debt below is what
is known to remain open; what neither list contains is unmeasured — and § 11.3 is the check
on *that*: 26 deliberate breakages of the policy, the adapter and the battery, each of which
a suite must catch.

### 7.5 · The cost, measured

A guard that blocks ordinary work gets disabled and then guards nothing, so the other
direction is a corpus. Harvesting every shell line this repository documents in a fenced
block: **208 runnable commands from 59 files, 197 allowed.** The eleven are named:

- 3 in `PLAN-QUEUE-AND-CANDIDATE-CENSUS-001.md` redirect `git cat-file` into the repository
  root — **true positives**;
- 2 in `HOSTILE_REVIEW_RUNBOOK.md` redirect into `"$review_root/…"`, assigned in an earlier
  command → `UNDERIVABLE` → denied. 🔴 **This is a real behaviour change for that runbook**,
  and it is the declared failure direction rather than an accident;
- 2 are `runtime_bridge.md`'s own table of prohibited shapes;
- 4 are documentation placeholders the harvest's filter did not catch.

A variable assigned **in the same command** is resolved — `SC=/tmp/x; cmd > "$SC/f"` is
allowed — because the value is in the text being judged and this is the dominant way an
agent writes to scratch. A variable from the environment is not.

### 7.6 · What is still open, declared not discovered

```
chmod / chown        git reset --hard      git checkout -- .
git clean -fd        git push              a committed script that writes when invoked
```

The last is deliberate: invoking a reviewed script by name is the escape hatch every denial
names. `test_runtime_parity.py::TheResidualDebtStaysDeclared` asserts each is **open and
identical on both sides**, so closing one fails that test and forces this list to move with
the fix.

## 8 · Two overclaims removed

### 8.1 · "repository-enforced"

`runtime_bridge.md` § 3 said gates, governance obligations and role contracts were
`repository-enforced` in both runtimes. What was checked:

```
git config core.hooksPath          unset
$(git rev-parse --git-path hooks)  no hook — only git's own samples
.github/workflows/                 one workflow, on push / pull_request / workflow_dispatch
                                   runs run_release_regressions.py · legend_lint.py
                                        public_release_gate.py
```

**CI enforcement is real on push; a local commit passes through nothing.** Every obligation
about who may write or which role a session holds is textual, with three compensating
controls that *detect* rather than prevent. The row is replaced with what each control
actually does and what it does not, and § 3.1 states the narrowed sentence the protocol will
stand behind.

### 8.2 · A check that could not run

`runtime_parity.py` imported the guard engine at module scope and then offered
`FAIL_CLOSED_ON_MISSING_BRIDGE` a branch for that engine's absence. With the engine gone the
process died at the import, so that branch had executed **zero times**: the property tested
was that Python raises on a missing file, not that the battery detects a missing control.
Found by the Codex pilot; reproduced here before repair.

The engine is no longer imported at all, and the battery takes a **root**, so six negative
arms run against fixture trees with the component genuinely removed: `ENGINE_MISSING`,
`ENGINE_IMPORT_FAILURE`, `POLICY_MISSING`, `HOOK_REGISTRATION_MISSING`,
`HOOK_CONFIG_MALFORMED`, `PAYLOAD_MALFORMED`. One of them asserts the CLI prints a FAIL row
rather than a traceback, because an operator reading a stack trace cannot tell a broken tool
from a broken bridge.

## 9 · The battery: ten dimensions, two verdicts, no elected actors

| Check | Read floor | Write floor |
|---|:--:|:--:|
| `ROUTER_PARITY` · `ACTOR_ID_PARITY` · `ROLE_REACHABILITY` | ● | ● |
| `GOVERNANCE_FINGERPRINT_PARITY` · `SKILL_REACHABILITY` · `MISSING_BRIDGE_FAIL_CLOSED` | ● | ● |
| `GUARD_POLICY_PARITY` · `HOOK_REGISTRATION_PRESENT` · `HOOK_DEMONSTRATED` · `NO_RUNTIME_AUTHORITY_ESCALATION` | | ● |

Three properties it did not have:

🔴 **Agreement is not correctness.** `GUARD_POLICY_PARITY` carries the verdict each command
must reach, so two runtimes that both allow blanket staging now fail instead of agreeing
perfectly. Revision 2 compared the runtimes only to each other.

🔴 **No actor is elected.** `ROLE_REACHABILITY` takes an operator-assigned `ACTOR_ID`: no
actor is `UNRESOLVED` and fails, an unknown role is refused rather than approximated, and the
router must *name* the path the contract lives at. A contract that merely exists and is
readable is **not** reachable — the arm that proves it uses a tree where `roles/mirror.md` is
gone and `roles/plan.md` is not, so the failure is the assigned actor's and nobody else's.

🔴 **The verdicts are separate.** `READ_ONLY_PARITY` passes today with an actor assigned;
`WRITE_ENABLED_PARITY` does not, on `HOOK_DEMONSTRATED` and
`NO_RUNTIME_AUTHORITY_ESCALATION`. Neither implies the other.

## 10 · Independent reverts

| Unit | Revert | What is lost |
|---|---|---|
| A | restore `AGENTS.md` from `f2b8ecf`; delete `runtime_bridge.md` | Codex is back on a router that duplicates rules and drifts; **D's `ROUTER_PARITY` fails**, which is the intended coupling |
| B | nothing to revert | — |
| C | restore `scripts/guard_bash_command.py` from `f2b8ecf`; delete the adapter and `.codex/config.toml` | the guard is Claude-only again; **D fails**, loudly |
| D | delete `runtime_parity.py`, its test, and both suite registrations | the bridge stops being falsifiable and starts being a claim |
| E | restore `guard_policy.py` and the two guard tests from `f2b8ecf` | twenty mutation paths reopen; **the write floor cannot be reached** and `GUARD_POLICY_PARITY` fails on the shapes it now asserts. E is revertible without A–D; A–D are not meaningfully revertible without E |

## 11 · Verification actually run

```
framework/scripts/test_pre_tool_use_guard.py   31 tests   OK    (python3.9 and 3.12)
framework/scripts/test_runtime_parity.py       49 tests   OK    (python3.9 and 3.12)
scripts/test_guard_bash_command.py             14 tests   OK    (python3.9 and 3.12)
framework/scripts/mutate_guard_suite.py        26 mutations — see § 11.3
framework/scripts/legend_lint.py .                        PASS
scripts/public_release_gate.py                            PASS, BLOCKS 0
framework/scripts/fulltext_receipts.py verify             OK, 128 chained receipts
framework/scripts/runtime_parity.py --actor mirror        READ_ONLY PASS · WRITE_ENABLED FAIL
scripts/run_release_regressions.py                        FAIL, 7 suites — § 11.1
integration_matrix.py (read-only from a peer branch)      clean merge, 0 dup, 4 mode, 7 fails
```

🔴 **Both interpreters on purpose.** CI runs Python 3.12, this machine runs 3.9, and the
registration reader takes a different path on each — `tomllib` there, a textual check here.
Running only one would have tested only one of them.

### 11.1 · The seven failures, with the two denominators that matter

A detached worktree at `f2b8ecf` was created and the same seven suites run in both trees,
comparing **normalised output line by line** rather than exit codes or counts.

```
vs BASE f2b8ecf     7 fail there, 7 fail here, all seven signatures IDENTICAL
                    SUITES WHOSE FAILURE CHANGED: none
vs MAIN  788c357    6 fail there, 7 fail here
                    FIXED by this branch      scripts/test_release_runner_verdict.py
                    ADDED by this branch      scripts/test_documented_commands.py
                                              scripts/test_fresh_clone_reader_journey.py
```

🔴 **The two added share one cause, and it is not this candidate's.** Both are
`learning/plan/PLAN-INTEGRATION-TOOLING-DURABILITY-001.md` naming `integration_matrix.py`
under `framework/scripts/` — a script that lives on `plan-integration-matrix` and not on
this branch. One document, one absent file, two red suites — and both were already red at
`f2b8ecf`, so they belong to earlier work on this branch rather than to this review unit.

🔴 **And the lesson of § 11.2 did not transfer on the first try.** The paragraph above
originally wrote that path out in full, inline and backticked, which made
`test_fresh_clone_reader_journey.py` red about *this file* — the same class the same
document diagnoses two sections later, reintroduced by the sentence describing it, for the
second time on this candidate. Writing the rule down is not the same as applying it; the
detector caught it, which is the argument for running the detector on your own prose before
claiming a clean tree.

🔴 **A normaliser that invented six of its own findings.** The first run of that comparison
reported six of the seven as CHANGED. Every one was the harness: the base worktree lives
under `/private/tmp`, and a generic tmp-path rule ordered before the repository-root rules
rewrote the two trees' paths differently. The tool was reporting a difference it had
created. Fixed, and the ordering is now commented in the harness, because a noisy diff
teaches a reader to skim exactly the report that must not be skimmed.

### 11.1.1 · Queue item "re-run the integration matrix"

`integration_matrix.py` is **not on this branch**; it is on `plan-integration-matrix`, by
that tool's own declaration that it belongs to no candidate. It was run **without merging
anything**: the script was extracted with `git show <ref>:<path>` into scratch and pointed at
this branch. Merging the branch would be an Orchestrator adjudication under Annex H.1 and is
not an author's to take — and the operator's decision for this run forbids merging two
runtime-bridge architectures.

It reported a clean composition — and one finding about this candidate, in § 11.4.

### 11.2 · 🔴 A self-correction: revision 2's § 9 was false, and false about itself

Revision 2 reported that `test_fresh_clone_reader_journey.py` had differed from base
because of a defect of this candidate — an inline path in `AGENTS.md` naming the wrong
directory for `gold_is_in_the_details.md` — and stated: *"Fixed, re-diffed, now identical."*

**It was not identical, and the sentence making the claim is why.** That test scans every
Markdown file for backticked inline paths and requires them to resolve. The § 9 narrative
wrote the broken path out in full, so the candidate reintroduced into its own prose exactly
the failure it was reporting fixed. Measured across four tips:

```
f2b8ecf  base                 2 unresolvable inline paths
cda34cf  rev 1                2
7a867e7  rev 2                3   ← the tip revision 2 declared "now identical"
c83b9d9                       3
e40e620  rev 3 content tip    3   the content commits do not touch this file
         rev 3 + THIS FILE    2   restored to base once the path stopped being written
                                  out in full — the commit carrying this line is the one
                                  that closes it, which is why no hash is named for it
```

🔴 The denominator matters and is stated: **2 is the base's own count**, not zero. The two
survivors are pre-existing, both in `PLAN-INTEGRATION-TOOLING-DURABILITY-001.md`, and are
not this candidate's to fix.

The class is one this repository has met before: **recording a negative falsifies it**, and
the fix is to exclude the record from its own detector. The defective path is now described
without a resolvable inline path — the directory and the filename are named separately.

The verification claim itself was the failure, not the code it described, which makes it the
worse of the two: a reviewer would have read "re-diffed, now identical" and stopped.

### 11.3 · Mutation-testing the suites: do they bite?

A green suite proves the tests pass. It does not prove they would **fail** if the control
were broken, and for a safety control that second property is the only one worth having.
`framework/scripts/mutate_guard_suite.py` breaks the guard, the adapter and the battery
**26 ways**, one at a time, each in a detached worktree, and requires a suite to notice.

```
M01-M12   the policy      staging silenced · unknown root fails OPEN · UNDERIVABLE allowed
                          eval unwrapped · piped shell · ANSI-C quoting · opaque argv[0]
                          `-c` not re-analysed · cp dropped · in-command variables
                          in-repo write allowed · unnamed target allowed
M13-M16   the adapter     unknown tool waved through · unreadable code-mode call skipped
                          only the first call judged · apply_patch payload unpoliced
M17-M26   the battery     CONFIGURED accepted as DEMONSTRATED · write floor collapsed into
                          the read floor · unassigned actor elected · any receipt accepted
                          · receipt provenance dropped · runtimes compared only to each
                          other · missing engine tolerated · role reachable without a route
                          · missing matcher unnoticed · matchers matched as substrings
```

🔴 **The first run found two things, and both were real.**

- **M25 SURVIVED.** No test asserted the missing-matcher condition, because the row it
  belongs to (`NO_RUNTIME_AUTHORITY_ESCALATION`) already fails today on the hook state — so
  deleting the matcher check outright changed no verdict and no test noticed. Three arms
  now assert that row's *detail* rather than its boolean, which is the only way to test one
  condition of a check that has several.
- **M24 was never applied** — its anchor carried an indentation the file does not have. The
  harness reported `ANCHOR_MISSING` rather than a pass, because *a mutation that never ran
  is not a mutation that was killed*, and a harness that scored it as one would inflate its
  own result.

🔴 **And a defect in the harness itself.** `apply_and_run` re-read `HEAD` once per
mutation. A full run takes tens of minutes, and a commit landing halfway through split the
run across two trees with nothing in the output saying so — which happened, on the second
run, because I committed while it was going. The tip is now resolved **once**, printed with
the results, and an uncommitted working tree is called out, since the worktrees carry the
committed tree and not the one the operator is looking at.

That is why only the run pinned to this candidate's content tip is quoted. The intermediate
runs are not reported as results: one predates the repair it would have been used to
justify, and the other is a statement about no particular tree.

```
MUTATION TEST   31 mutations, each in a detached worktree
TIP             baaa8e4d27240b9b6d038db850f038a5350be67e   pinned once
RESULT          KILLED 31/31     SURVIVED 0     UNUSABLE 0
```

🔴 **31/31 is a property of these 31 mutations**, not of the guard. It says every breakage
someone thought to write down is caught; it says nothing about the breakage nobody wrote
down. The list is in `mutate_guard_suite.py --list` so the next reader can add the one that
is missing rather than infer from the score that none is.

### 11.4 · 🔴 A second self-correction: two files this candidate added joined a red list

`integration_matrix.py`, run read-only from the peer branch, reported **6 mode-bit
offenders** on this branch against **4 on `main`**. The two extra were
`codex_runtime_probe.py` and `mutate_guard_suite.py` — committed at mode `100644` while
carrying a `#!` line — so this candidate made `test_release_surface.py`, already red, red
about two more files.

The failure-signature diff had said IDENTICAL, and it was, **when it was run**: the two
scripts did not exist yet. A pre-existing failure is only pre-existing at the tip you
measured it on, and a verification that predates half the work verifies half the work.

Both bits are set; the count is back to 4, matching `main`. The remaining four are
pre-existing and are not this candidate's to fix.

🔴 **The instrument belonged to someone else.** Nothing in this candidate's own test set
looks at file modes. It was found because a peer's tool was run against this branch, which
is the argument for running it at all — and for the queue item that asked for it.


### 11.4.1 · 🔴 Two bypasses this candidate SHIPPED, found by using the guard on myself

Between revision 4 and revision 5 the guard refused a diagnostic command of mine that
contained `->` inside a quoted command substitution. Following that false positive found
two defects, and the second is the more serious of the two:

| Shape | Verdict when found | Why |
|---|---|---|
| `echo "$(git add -A)"` | 🔴 **ALLOWED** | `extract_substitutions` skipped `$(…)` inside **both** quote kinds. The shell expands it inside double quotes and leaves it alone inside single ones, so half that rule was wrong in the unsafe direction |
| `FOO=1 git add -A` | 🔴 **ALLOWED** | a leading `NAME=VALUE` was read as the *program*. No rule matches a program called `FOO=1`, so an assignment prefix disarmed staging, `rm`, redirection and every wrapper |
| `a=$(git rev-parse HEAD)` | 🔴 **DENIED** | the same missing step seen from its other side: after substitution extraction a pure assignment looked like a program named by an expansion |

Both bypasses were in **shipped commits of this candidate** — `a7589a2` for the first,
`6a4a3a4` and earlier for the second — and both survived the 46-shape attack list, the
20-encoding sweep and 26 mutations. They were found by the guard **being used**, on an
ordinary command, which no probe list contained because no probe list is written by someone
who does not already know the answer.

The lesson is not "write more probes". It is that a control you only test is tested against
your imagination, and a control you *run against your own work all day* is tested against
the shapes that actually occur. `FOO=1 <anything>` is the most ordinary shape in shell and
was not on any list here.

`M27` and `M28` now restore each defect and require a suite to catch it, so neither can
return quietly.


### 11.4.2 · 🔴 The false-positive rate under real use, measured on myself

The two bypasses of § 11.4.1 were found because the guard **refused a command of mine**.
That happened three times in one session of heavy use, and each refusal was a defect:

| # | The command shape | Why it was wrong |
|---|---|---|
| 1 | `printf … "$([ … ] && echo "A -> B")"` | `->` inside a quoted substitution fragmented under the lexer. Chasing it found the two bypasses |
| 2 | `git show X:Y > "$SC/out/gp_$rev.py"` | a scratch directory named in the same command, with a loop variable in the *filename*. Now decided by the resolvable prefix |
| 3 | `python3 - <<PY … subprocess.run([sys.executable, "framework/scripts/legend_lint.py"]) … PY` | 🔴 **the guard forbade the alternative its own denial message recommends.** `subprocess.` was a write primitive outright, so invoking a committed script by name from a program body was denied. The argument is now read as the command it is |

All three are repaired, and each carries a mutation (`M27`–`M31`) so it cannot return. But
the honest reading of "three in one session" is not that the count is now zero:

🔴 **A guard is tested by its author against the shapes its author imagines, and used by
everyone against the shapes that occur.** The 33 negative controls did not contain
`FOO=1 <anything>`, a loop writing one file per iteration, or a heredoc that shells out —
three of the most ordinary things anyone types. More remain, and the mechanism that will
find them is the same one that found these: somebody's real work being refused.

That is a reason to keep the denial message specific and the escape hatch real, not a
reason to widen the policy pre-emptively — and it is a reason a reviewer should weigh Unit E
by its blast radius rather than by its test count.


### 11.5 · The one review this candidate is answerable to, and what of it is stale

No review of `CAND-20260826-RTBRIDGE` exists on any of the 62 local refs — searched by
content, not by filename. **STALE_REVIEWS = 0 for this candidate.**

But one Mirror hostile review is about the same proposition and must not be treated as
unrelated: `RUNTIME_FAILOVER_CLAUDE_CODEX_HOSTILE_REVIEW_MIRROR_v1`, on branch `mirror`,
2026-08-26, verdict **REFUTED** — *"The control exists in every worktree, byte-identical,
and Codex does not run it."*

**Its verdict is not moved by this candidate, and this candidate does not claim to move
it.** `WRITE_ENABLED_PARITY` still FAILS, for the reason the review gives.

What this candidate *does* touch, row by row:

| Review row | Status after this candidate |
|---|---|
| `ENFORCEMENT_PARITY` **FAILS** | **unchanged.** The guard is registered on the Codex side and still not demonstrated firing. The battery says so in its own row rather than leaving it to prose |
| `CE-1` / `CE-2`: *"0 `hooks` keys in `~/.codex/config.toml`"* | **the row was about the USER config and remains true.** A PROJECT `.codex/config.toml` with `[hooks]` now exists, which the review's Codex column did not contemplate — and it changes nothing about the conclusion, because parsing is not firing |
| `SEMANTIC_PARITY` **FAILS**: *"`AGENTS.md` omits the § 0 authority gate"* | **addressed at the router level**, not adjudicated: `AGENTS.md` now names `CLAUDE.md` *"including its § 0"*. Occurrences in `AGENTS.md`: `§ 0` 0 → 1, `BOOTSTRAP` 0 → 2, `ORCHESTRATOR_LEASE` 0 → 1 |
| `CE-5`: `~/.codex/AGENTS.md` prepends a brevity directive that pulls against the locator obligations | 🔴 **independently corroborated here.** The recorded session's `world_state.agents_md` carries exactly that text above the project doc. It is a live finding and this candidate does not fix it |
| `CONTENT_PARITY` **HIGH, with a measured hole** | 🔴 **this candidate moves that number the WRONG way — see below** |

#### 11.5.1 · 🔴 A cost of the router rewrite, reported rather than left to be found

The review scored content parity by how many link targets the two entry points share. On
that metric, making `AGENTS.md` a pure router **reduces the overlap**:

```
                     CLAUDE  AGENTS  C-only  A-only  shared
f2b8ecf  (base)          29      15      18       4      11
HEAD                     29      14      23       8       6
```

I think the metric does not capture the property — `AGENTS.md` is deliberately a router that
*names* obligations and sends the reader to `CLAUDE.md`, so shared link targets measure
duplication rather than reachability, which is what `ROUTER_PARITY` and `ROLE_REACHABILITY`
test instead. **A reviewer is entitled to disagree, and the number is put here so the
disagreement is about the design and not about an undisclosed regression.**

🔴 **These are not the review's own figures.** The review reported `31 / 18 / 20 / 7 / 11`;
my extractor gives `29 / 15 / 18 / 4 / 11` on the review's own ref. **One of five agrees.**
The instruments differ — mine counts Markdown link targets only — so the table above is
comparable *within itself*, base against HEAD with one instrument, and is **not** a
reproduction of the review's measurement. Reporting it as one would have been the error the
tool makes on your behalf.


## 12 · Pre-existing debt this candidate found and did NOT fix

`CLAUDE.md` fails `test_locator_obligation_reaches_every_route.py`,
`test_abstract_corpus_is_not_evidence.py` and `test_fulltext_trace_contract.py`, and has
since it became a router on 2026-08-16: it carries neither `FULLTEXT_READ_RECEIPT`, nor
`verbatim_locators`, nor `pubmed_corpus_harvest`. Three canonical regressions have been red
against the repository's primary entry point for twelve days.

Scope discipline: the dispatch said not to expand silently, so it is reported with its
evidence and left alone. It is the same question `AGENTS.md` § 1.1 answers for the other
entry point, and whoever answers it for `CLAUDE.md` should answer both the same way.

## 13 · What this candidate does not do

- it does not promote Codex — body § 33.1 and § 33.4 stand, `ON_DEMAND_LEGEND_COLLABORATOR`;
- it does not create an actor, a role, an authority or a gate;
- it does not claim the Codex hook fires, and it fabricates no probe receipt;
- it does not merge, defer to, or override `codex-bridge-integration` — two writers on one
  problem is an Orchestrator adjudication under Annex H.1, not an author's;
- it does not touch `main`, and it is not a `CANONICAL_BATCH_COMMIT`;
- it does not make `launch/legend_launch.sh` runtime-neutral — that kernel is `claude`-bound
  at every step and out of scope;
- 🔴 it does **not** close `chmod`, `git reset --hard`, `git checkout --`, `git clean` or
  `git push`, and § 7.6 says so rather than letting a reader infer that "the debt is closed"
  means all of it.

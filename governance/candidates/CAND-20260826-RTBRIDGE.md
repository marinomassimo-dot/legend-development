---
artifact: INTEGRATION_CANDIDATE — Claude ↔ Codex minimum runtime bridge
candidate_id: CAND-20260826-RTBRIDGE
revision: 3
task_id: RTBRIDGE-P00-001
author: plan
authored_on: 2026-08-26
revised_on: 2026-08-28
governance_version: 3.1.1
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1), so this
  file is outside the candidate content domain and cannot move the hash it records
partition: >
  FIVE REVIEW UNITS over ONE tip, and the single tip is argued in § 2 rather than assumed.
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
TIP                       e40e6201b9f4ddbfb1e248e0fe9533a990fe7d17
                          the last commit in the CONTENT domain. This file is committed
                          after it, and cannot move the hash — see the invariance note.
CANDIDATE_CONTENT_HASH    4d55c865a79388c9e87fe094fe01db6a0ef8e5d3396da1275270d39def7ad832
                          🔴 SUPERSEDES 7f88cf34d8d19527bd3e7e295f5fada03e1561d6771ab3b0108d527f98323f2a
                          at tip 7a867e7 (revision 2), which superseded
                          6277b98e023734c0ab23177b5ca4f7642438a9d07d8fd52b78e002c639678d93
                          at tip cda34cf (revision 1). Both were correct for the trees they
                          named and are superseded, not withdrawn (Annex D.2). They stay
                          visible because a candidate that silently rewrites its own hash
                          teaches a reviewer to trust the current value, which is the one
                          thing a hash cannot ask for.
CHANGE_CLASS              MAJOR — it reverses what a safety control does on a malformed
                          payload (§ 5), it introduces a second registrant of that control,
                          and revision 3 CHANGES WHAT IS FORBIDDEN FOR EVERY ACTOR IN BOTH
                          RUNTIMES (§ 7). Mirror classifies; this field is the author's
                          declaration and not the classification.
RECIPE                    python3 governance/scripts/candidate_content_hash.py \
                            --base f2b8ecf11e77ebe86e6e17b6348e6469cc2e432b \
                            --tip  e40e6201b9f4ddbfb1e248e0fe9533a990fe7d17
INVARIANCE                Run the same recipe with --tip set to the branch tip that carries
                          THIS FILE. It must print the same value, because every commit
                          after e40e620 on this branch touches only governance/candidates/,
                          which P5.1 excludes. If it does not, the hash is stale and this
                          manifest is wrong — check that before reviewing anything else.
CONTENT DOMAIN TOUCHED    11 paths:
                            AGENTS.md
                            .codex/config.toml
                            framework/protocols/runtime_bridge.md
                            framework/scripts/guard_policy.py
                            framework/scripts/pre_tool_use_guard.py
                            framework/scripts/runtime_parity.py
                            framework/scripts/test_pre_tool_use_guard.py
                            framework/scripts/test_runtime_parity.py
                            scripts/guard_bash_command.py
                            scripts/test_guard_bash_command.py
                            scripts/run_release_regressions.py
```

## 2 · Why five units and one commit series

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

## 3 · The five units

| Unit | What it is | Files |
|---|---|---|
| **A · router bridge** | `AGENTS.md` stops carrying rules and routes; the contract it routes under | `AGENTS.md`, `framework/protocols/runtime_bridge.md` |
| **B · skill bridge** | the decision **not** to copy, made checkable | *(no separable artifact — see § 4)* |
| **C · hook adapter / shared guard** | one policy, one engine, two registrations, three payload shapes | `framework/scripts/pre_tool_use_guard.py`, `scripts/guard_bash_command.py`, `.codex/config.toml` |
| **D · parity battery + bootstrap** | the falsifier, and the fail-closed bootstrap | `framework/scripts/runtime_parity.py`, `framework/scripts/test_runtime_parity.py`, `scripts/run_release_regressions.py` |
| **E · the write-primitive model** 🆕 | the guard stops matching strings and starts parsing commands; twenty mutation paths close | `framework/scripts/guard_policy.py`, `framework/scripts/test_pre_tool_use_guard.py`, `scripts/test_guard_bash_command.py` |

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

### 6.1 · The matcher list was wrong, and a real session said so

🔴 **The finding of this revision.** A Codex session ran in a LEGEND worktree on
2026-08-28 and called **neither** `shell_command` **nor** `unified_exec`. All 20 of its
tool calls were the code-mode tool `exec`, each carrying a JavaScript body of the form
`const r = await tools.exec_command({"cmd": …, "workdir": …});`.

```
INSTRUMENT   ~/.codex/sessions/2026/08/28/rollout-2026-08-28T10-14-22-01a0476f-….jsonl
             cli_version  0.150.0-alpha.8      originator  codex_vscode
             cwd          .claude/worktrees/mirror
             20 × custom_tool_call, name "exec"
```

Revision 2's registration would therefore have policed **nothing** in that session even had
it fired, while the battery reported a guard that was never consulted. Both halves are
fixed: `.codex/config.toml` registers `exec`, `exec_command` and `apply_patch`, and the
adapter reduces a code-mode body to the shell commands inside it — denying a body whose
shell call it cannot read, because `tools.exec_command(buildArgs())` is a call the guard
cannot clear, not one it may ignore.

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

```
46  prohibited shapes probed          46 refused        0 leaks
36  negative controls probed          36 allowed        0 false positives
20  alternate encodings probed        20 refused        0 leaks
20  battery commands × 3 payload shapes                 identical AND correct
```

**Zero is a property of the probed set, not of the shell.** The residual debt below is what
is known to remain open; what neither list contains is unmeasured.

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
framework/scripts/test_runtime_parity.py       46 tests   OK    (python3.9 and 3.12)
scripts/test_guard_bash_command.py             14 tests   OK    (python3.9 and 3.12)
framework/scripts/legend_lint.py .                        PASS
scripts/public_release_gate.py                            PASS, BLOCKS 0
framework/scripts/fulltext_receipts.py verify             OK, 128 chained receipts
framework/scripts/runtime_parity.py --actor mirror        READ_ONLY PASS · WRITE_ENABLED FAIL
scripts/run_release_regressions.py                        FAIL, 7 suites
```

🔴 **Both interpreters on purpose.** CI runs Python 3.12, this machine runs 3.9, and the
registration reader takes a different path on each — `tomllib` there, a textual check here.
Running only one would have tested only one of them.

### 11.1 · The seven pre-existing failures, re-diffed at this tip

A detached worktree at `f2b8ecf` was created and the same seven suites run in both trees,
comparing **normalised output line by line** rather than exit codes or counts. Six are
byte-identical. The seventh is § 11.2.

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

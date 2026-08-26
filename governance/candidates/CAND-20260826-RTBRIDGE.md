---
artifact: INTEGRATION_CANDIDATE — Claude ↔ Codex minimum runtime bridge
candidate_id: CAND-20260826-RTBRIDGE
revision: 2
task_id: RTBRIDGE-P00-001
author: plan
authored_on: 2026-08-26
governance_version: 3.1.1
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1), so this
  file is outside the candidate content domain and cannot move the hash it records
partition: >
  FOUR REVIEW UNITS over ONE tip, and the single tip is argued in § 2 rather than assumed.
  A reviewer may accept or reject each unit independently; § 8 gives each one its own revert.
human_approval: >
  NOT REQUESTED for the content. One item DOES require it and is not prefilled: the Codex
  session probe of § 6 is a spend under Annex J.4 (DEFAULT_EXTERNAL_SPEND = 0) and needs
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
TIP                       7a867e72920044ff052de3aff62e75abf68dd544
BRANCH                    plan-runtime-bridge-p00
CANDIDATE_CONTENT_HASH    7f88cf34d8d19527bd3e7e295f5fada03e1561d6771ab3b0108d527f98323f2a
                          🔴 SUPERSEDES 6277b98e023734c0ab23177b5ca4f7642438a9d07d8fd52b78e002c639678d93
                          at tip cda34cf, which this file carried for exactly one commit
                          before the withdrawal in § 6.1 moved two content-domain files.
                          That binding was correct for the tree it named and is superseded,
                          not withdrawn (Annex D.2). It is left visible because a candidate
                          that silently rewrites its own hash teaches a reviewer to trust
                          the current value, which is the one thing a hash cannot ask for.
CHANGE_CLASS              MAJOR — it changes what a safety control does on a malformed
                          payload (§ 5), and it introduces a second registrant of that
                          control. Mirror classifies; this field is the author's declaration
                          and not the classification.
RECIPE                    python3 governance/scripts/candidate_content_hash.py \
                            --base f2b8ecf11e77ebe86e6e17b6348e6469cc2e432b \
                            --tip  cda34cfa99fd6c853a0dd01fab72a1af319b4921
```

## 2 · Why four units and one commit

Body § 11 wants milestone granularity and the dispatch asked for units kept apart *where
practical*. It is not practical here, and the reason is checkable rather than stylistic:
**every split leaves the tree red.**

```
router   names   the adapter registration and the engine   → link targets break without them
adapter  names   the shared engine                          → the engine must land first
battery  asserts router AND adapter AND engine together     → it fails without any one
```

Landing the router first breaks `test_link_targets.py`. Landing the engine first leaves the
battery asserting a router that has not changed. So the artifacts are one change, and the
units below are one *review* surface each, with independent accept/reject and independent
reverts in § 8. They are not merged to reduce rehashes; they are merged because a partial
tree is a failing tree.

## 3 · The four units

| Unit | What it is | Files |
|---|---|---|
| **A · router bridge** | `AGENTS.md` stops carrying rules and routes; the contract it routes under | `AGENTS.md`, `framework/protocols/runtime_bridge.md` |
| **B · skill bridge** | the decision **not** to copy, made checkable | *(no separable artifact — see § 4)* |
| **C · hook adapter / shared guard** | one policy, one engine, two registrations | `framework/scripts/guard_policy.py`, `framework/scripts/pre_tool_use_guard.py`, `scripts/guard_bash_command.py`, `.codex/config.toml`, `framework/scripts/test_pre_tool_use_guard.py`, `scripts/test_guard_bash_command.py` |
| **D · parity battery + bootstrap** | the falsifier, and the fail-closed bootstrap | `framework/scripts/runtime_parity.py`, `framework/scripts/test_runtime_parity.py`, `scripts/run_release_regressions.py` |

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
than closed. `runtime_parity.py --skills` proves the "same bytes" half — one bootstrap
skill, one scientific skill, one governance/review skill, each with
`SOURCE_BYTES_IDENTICAL`, `CLAUDE_REACHABLE`, `CODEX_REACHABLE`,
`NO_DUPLICATED_NORMATIVE_COPY` — and `test_runtime_parity.py` proves the check fails when a
second byte-identical copy appears anywhere in the index.

🔴 **What is NOT bridged and must not be read as bridged:** Claude *discovers and applies*
these skills; Codex reads them only when a task names one. That is a
`CAPABILITY_DIFFERENCE`, it is listed in `runtime_bridge.md` § 3, and a Codex actor owes it
as a declaration at registration under body § 38.

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

## 6 · What is unverified, and the exact approval it needs

| Claim | Status | Instrument |
|---|---|---|
| project `.codex/config.toml` is loaded | `OBSERVED` | wrong type on a known key exits 1 from the worktree and the root; unknown key exits 0 |
| `hooks.PreToolUse` is a recognized key | `OBSERVED` | wrong types error on three consecutive runs; `zzz.PreToolUse=1` ignored; `model=1` errors |
| `matcher` is required in a hook group | 🔴 `WITHDRAWN` | asserted from one run, does not reproduce over three. See § 6.1 |
| the shipped registration parses | `OBSERVED` | `codex doctor` rc 0; rc 1 with a broken key prepended |
| **the Codex hook FIRES, before the shell mutates** | 🔴 `UNVERIFIED` here; **`OBSERVED NOT FIRING`** by a peer — § 6.2 | a Codex session that runs `git add -A` in a scratch fixture and is refused |

### 6.1 · A claim this candidate made and withdrew

An earlier revision of `.codex/config.toml` and of `runtime_bridge.md` stated that `matcher`
is **required** in a Codex hook group, from a single probe run that errored on a group
without one. Re-run three times with three controls green, a matcher-less group is
**accepted**. The claim is withdrawn.

It is recorded rather than deleted for one reason: it had already been used to judge another
actor's registration — `.codex/hooks.json` on `codex-bridge-integration` declares a hook
group with no matcher, and on the withdrawn claim that file would have been called broken.
It is not. A negative asserted from one run is a guess with a citation.

### 6.2 · The concurrent implementation, and what it measured

Branch `codex-bridge-integration`, 8 commits ahead of `main`, in another session's worktree,
independently built this bridge. Four files collide by name: `AGENTS.md`,
`framework/protocols/runtime_bridge.md`, `scripts/guard_bash_command.py`, its test.

**This candidate does not merge it, defer to it or override it.** Two writers on one problem
is an Orchestrator adjudication (Annex H.1: task, priority, reassignment), and the two are
not interchangeable — that branch splits the adapters into two entry scripts over a shared
engine and registers via `.codex/hooks.json`; this one keeps a single entry point and
registers via `.codex/config.toml`. Neither registration path has been observed loading.

Two of its results are recorded in `runtime_bridge.md` § 8 because they are **stronger than
anything reachable here**: it ran the session probe and the Codex hook **did not fire**, and
it reports the enforced output contract as narrower than the schema shipped in the binary.
The engine in this candidate satisfies the narrow reading already, so nothing changes — but a
future edit that begins emitting `continue` or `updatedInput` would break Codex and pass
every test in this repository, and that is now written down.

`codex doctor` does not load hooks, so no local no-cost probe reaches the last row. A
session probe **is a spend**: Annex J.4, `DEFAULT_EXTERNAL_SPEND = 0`, so it needs
`HUMAN_APPROVAL (TYPE: SPEND)`. **No `APPROVAL_ID` is prefilled here and none exists.**

Until a probe receipt exists at `framework/state/codex_hook_probe.json`,
`runtime_parity.py` exits non-zero, `--bootstrap` reports `BLOCKED_BY_GOVERNANCE`, and a
Codex actor is read-only. What holds during a read-only pilot is the **Codex sandbox**
(`-s read-only -a untrusted`, filesystem and network both `restricted` as `codex doctor`
reports) — a runtime property, not something this candidate provides.

## 7 · `GUARD_HARDENING_DEBT` — opened, not closed

Nine command shapes mutate the repository and the policy allows them, identically on both
sides: `bash -c` wrapping, `sed -i`, `>`, `>>`, `tee`, `cp`, `mv`, `python3 -c`, `perl -pi`.
Four of eighteen probed shapes are stopped.

The shell-wrapper case has a named cause: the policy blanks quoted spans, because it once
blocked the very commit that documented it, and a wrapper hides behind that exemption.

**This is not a bridge defect.** It predates both adapters and is byte-identical on both
sides — `runtime_parity.py --characterize` prints it, and
`test_pre_tool_use_guard.py::KnownGapsAreCharacterisedNotClaimedFixed` asserts each gap is
open *and* identical, so a future hardening pass fails this list and must close the debt
entry with the fix. Widening the policy changes what is forbidden for every actor: separate
change, separate blast radius, separate review.

## 8 · Independent reverts

| Unit | Revert | What is lost |
|---|---|---|
| A | restore `AGENTS.md` from `f2b8ecf`; delete `runtime_bridge.md` | Codex is back on a router that duplicates rules and drifts; **D's `ROUTER_REACHABILITY` fails**, which is the intended coupling |
| B | nothing to revert | — |
| C | restore `scripts/guard_bash_command.py` from `f2b8ecf`; delete the engine, the policy module and `.codex/config.toml` | the guard is Claude-only again; **D fails**, loudly |
| D | delete `runtime_parity.py`, its test, and both suite registrations | the bridge stops being falsifiable and starts being a claim |

## 9 · Verification actually run

```
framework/scripts/test_pre_tool_use_guard.py   15 tests   OK
framework/scripts/test_runtime_parity.py       18 tests   OK
scripts/test_guard_bash_command.py             11 tests   OK
framework/scripts/legend_lint.py .             PASS
scripts/public_release_gate.py                 PASS, BLOCKS 0
framework/scripts/runtime_parity.py            7/8 — the 8th is § 6, by design
scripts/run_release_regressions.py             FAIL, 7 suites
```

🔴 **The seven are pre-existing and that was measured, not assumed.** A detached worktree
was created at `f2b8ecf`, the same seven suites were run there, and each failure signature
was diffed against the working tree. Six matched byte-for-byte. The seventh —
`test_fresh_clone_reader_journey.py` — **did not**, and the difference was a defect of this
candidate: an inline path in `AGENTS.md` read `framework/instruction/gold_is_in_the_details.md`
for a file that lives in `framework/master/`. Fixed, re-diffed, now identical.

Two of the seven were made *worse* by an earlier revision of this work and repaired before
this tip: `test_locator_obligation_reaches_every_route.py` and
`test_abstract_corpus_is_not_evidence.py` require **every** entry point — `CLAUDE.md` **and**
`AGENTS.md` — to state the locator obligation, the receipt obligation and the
abstract-corpus bound. Stripping `AGENTS.md` to a pure router removed all three.

**That is a real tension with the dispatch's own requirement 1** ("must not duplicate
CLAUDE.md normative content") and it is resolved, not hidden: `AGENTS.md` § 1.1 **names**
each obligation and gives its address, and states in the file that naming is not stating.
A reviewer who disagrees should say so — the alternative readings are (a) restate the rules
and accept the drift, or (b) amend the two tests, and neither is Plan's to take alone.

## 10 · Pre-existing debt this candidate found and did NOT fix

`CLAUDE.md` fails all three of those tests, and has since it became a router on 2026-08-16:
it carries neither `FULLTEXT_READ_RECEIPT`, nor `verbatim_locators`, nor
`pubmed_corpus_harvest`. Three canonical regressions have been red against the repository's
primary entry point for ten days.

Scope discipline: the dispatch said not to expand silently, so it is reported here with its
evidence and left alone. It is the same question `AGENTS.md` § 1.1 answers for the other
entry point, and whoever answers it for `CLAUDE.md` should answer both the same way.

## 11 · What this candidate does not do

- it does not promote Codex — body § 33.1 and § 33.4 stand, `ON_DEMAND_LEGEND_COLLABORATOR`;
- it does not create an actor, a role, an authority or a gate;
- it does not widen the write-guard policy;
- it does not claim the Codex hook fires;
- it does not touch `main`, and it is not a `CANONICAL_BATCH_COMMIT`;
- it does not make `launch/legend_launch.sh` runtime-neutral — that kernel is `claude`-bound
  at every step and is out of scope, and it currently refuses even Claude
  (`CERTIFIED_VERSION 2.1.231` against an installed `2.1.232`).

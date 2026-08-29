---
artifact: INTEGRATION_CANDIDATE — runtime bridge, revision 8 (the effect model)
candidate_id: CAND-20260829-RTBRIDGE8
revision: 8
task_id: RTBRIDGE-P00-001
author: plan
authored_on: 2026-08-29
governance_version: 3.1.1
supersedes: >
  NOTHING. CAND-20260826-RTBRIDGE revision 7 stands unaltered on its own branch at
  6cd4859; this is a NEW candidate on a NEW branch taken from that tip, so rev7's history
  is untouched and a reviewer may reject this and keep that.
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1), so
  this file is outside the candidate content domain and cannot move the hash it records
partition: >
  FIVE REVIEW UNITS over one commit series. Each unit is one commit and each is
  independently revertible; § 11 gives the revert for each.
human_approval: >
  NOT REQUESTED for the content. TWO items require it and NEITHER is prefilled: the Codex
  session probe (§ 7.4) is a spend under Annex J.4, and the registration repair (§ 7.3)
  requires a file to reach the branch checked out at the SHARED CHECKOUT, which is
  canonical main and is protected.
---

# INTEGRATION_CANDIDATE — `CAND-20260829-RTBRIDGE8`

## 1 · Manifest (Annex D.2)

```
CANDIDATE_ID              CAND-20260829-RTBRIDGE8
CANDIDATE_BRANCH          plan-runtime-bridge-p00-rev8
BASE_HEAD                 6cd485974c358f03aaefd3cdc6f591241376e125
                          the revision-7 TIP, deliberately. Not main (788c357): this
                          candidate is the delta FROM revision 7, and hashing against
                          main would bind 81 prior Plan commits to this review.
TIP                       8ffcd020ca65e91815c6cf81481d511668b9816a
                          the last commit in the CONTENT domain. This file is committed
                          after it and cannot move the hash — see INVARIANCE.
CANDIDATE_CONTENT_HASH    4b014a2f7684a1463e95db8fc94846197d6791b7039920a6bb004be28264479e
CHANGE_CLASS              MAJOR — it changes what is forbidden for every actor in both
                          runtimes (nineteen families closed), it changes what a
                          "verdict" IS (an effect set judged against an authority), and
                          it withdraws a claim revision 7 made about the Codex hook.
                          Mirror classifies; this field is the author's declaration.
RECIPE                    python3 governance/scripts/candidate_content_hash.py \
                            --base 6cd485974c358f03aaefd3cdc6f591241376e125 \
                            --tip  8ffcd020ca65e91815c6cf81481d511668b9816a
INVARIANCE                Re-run with --tip set to the branch tip carrying THIS file. It
                          must print the same value, because every commit after 8ffcd02
                          touches only governance/candidates/, which P5.1 excludes. If it
                          does not, the hash is stale and this manifest is wrong.
FILES                     15 changed · +4240 −64 · 6 new modules, 4 new suites
```

## 2 · The one-sentence change, and the measurement that forced it

Revisions 1–7 answered *is this command text allowed?*. Revision 8 answers *what would
this command DO, is that within this actor's authority, and did it do exactly that?*

The measurement that forced it, taken against the revision-7 policy on 2026-08-29 over
the 46 repository-mutating shapes the P0 brief enumerates:

```
                        rev7          rev8
ALLOWED                 35 / 46        2 / 46
```

The two that remain are correct: a committed script invoked by name (the declared escape
hatch every denial message offers) and `git commit -m x <path>` (named staging plus a
commit, which is how work lands here).

Of the 33 newly refused, **six** were declared open debt in revision 7 § 4.5. The other
**twenty-seven were not declared anywhere** — allowed, and not listed as debt either.
That gap, between *refused* and *declared open*, is what the effect model removes: a
command now produces an EFFECT, and an effect no authority grants is refused whether or
not anyone thought to list it.

### 2.1 · Three of them were bypasses of rules the policy already held

Not scope gaps. Holes in rules that were already written, already tested, and already
believed.

```
echo x 1> framework/x        ALLOWED     while `echo x > framework/x` was DENIED
cp -t framework /tmp/a       ALLOWED     while `cp /tmp/a framework/x` was DENIED
echo hi                      ALLOWED     while `git add -A` alone was DENIED
git add -A
```

**The numbered redirect.** `FD_REDIRECT` deleted `1>`, `2>`, `1>>`, `&>` and `exec 3>`
from the command text *before lexing*, so the target arrived as a harmless argument to
`echo`. The expression existed to strip file-descriptor *duplications* (`2>&1`), which
name no path; it did not distinguish those from redirections that take one.

**The destination in a flag.** `-t` / `--target-directory` moves the destination out of
the operand list, and `operands()` skips option values — so the "destination" the policy
derived was the last **source**, classified it as scratch, and allowed a write into the
repository. Same for `mv -t` and `install -t`.

**🔴 The newline, and this is the one that matters.** `CONTROL_TOKENS` has contained
`"\n"` since revision 1. The lexer was `shlex(punctuation_chars=True)` with
`whitespace_split=True`, under which a newline is *whitespace* and is never emitted as a
token. The entry was unreachable for every real newline, and two lines were lexed into
**one argv** — so only the first line's program was ever analysed.

A multi-line block is not an exotic shape. It is the ordinary shape of agent shell use:
every Bash call in the session that found this was multi-line. `;` split correctly. `|`
split correctly. A newline did not, for seven revisions.

And the entry was not merely dead. It fired in **exactly one** case — a backslash
continuation — where the two lines are one command and must NOT be split. It was
reachable only where it was wrong.

### 2.2 · A repository under `/tmp` was entirely unguarded

`classify_target` returned `SCRATCH` for anything under `/tmp`, `/private/tmp`,
`/var/folders` or any path containing a `scratchpad` segment, **before** consulting the
repository root. `TMPDIR` on macOS points into `/var/folders`; every fixture repository
in this repository's own test suites is created there.

The first run of the live floor written for this revision measured
`echo tampered > kept.txt` as ALLOWED and then read the file back to find it rewritten.

Repository membership now beats the scratch prefix. The exemption exists so that work
*outside* the tree is not this guard's business; inside the tree is exactly its business.

🔴 I would not have found this by reading. It appeared because the floor **executes**,
and because the assertion afterwards read the file back rather than trusting the verdict.

## 3 · The architecture delta from revision 7

| | revision 7 | revision 8 |
|---|---|---|
| the question | command text → `ALLOW` / `DENY` | command → **effect set** → authority → decision |
| the vocabulary | 11 rule names, private to the policy | 11 **effects**, closed and shared with two other modules |
| the grant | implicit: "what the policy denies" | an **authority ladder**, six rungs, each a superset of the last |
| unknown input | some shapes denied, case by case | `UNKNOWN_EFFECT` denies under **every** authority, asserted over the table |
| after execution | nothing | `post_effect_verify` — observed delta vs authorised set |
| who is acting | not modelled | `execution_attestation` — nine dimensions, one fingerprint |
| a resume | not modelled | any changed **or underivable** dimension revokes write authority |
| the record | nothing | `execution_receipt` — 18 bound fields, chained, self-re-derived |
| the Codex hook | `TRUST_PENDING`, cause explicitly not claimed | **`NOT_LOADED`**, cause measured with controls |

Six new modules, four new suites:

```
framework/scripts/effect_model.py             the vocabulary and the algebra — pure
framework/scripts/execution_attestation.py    who, where, in what incarnation
framework/scripts/post_effect_verify.py       predict → execute → observe → compare
framework/scripts/execution_receipt.py        the bound, chained record
framework/scripts/codex_hook_state.py         does the Codex registration LOAD?
framework/scripts/guard_policy.py             now DERIVES effects; holds no verdict rule
```

### 3.1 · The authority had to be a mapping, not a product

The first draft made an `Authority` a pair of sets, `kinds × scopes`. That shape cannot
express the grant the shell guard actually needs — *stage a named path inside the
repository, but do not write content into it* — because `STAGE` and `WRITE` both land at
`INSIDE_REPO`, and any product admitting the first admits the second.

A guard built on that product either loses `git commit`, which is how every commit in
this repository is made, or regains the shell write that revisions 1–7 exist to stop.
Per-kind scopes cost one dictionary and are the only shape in which those are different
sentences.

```
READ_ONLY        READ everywhere. The floor, and where an unattested session sits.
SCRATCH_WRITE  + WRITE/DELETE/RENAME/EXTRACT/PERMISSION at SCRATCH, OUTSIDE_REPO
SHELL_DEFAULT  + STAGE, COMMIT at INSIDE_REPO          ← what the guard enforces
WORKTREE_WRITE + WRITE/DELETE/RENAME/EXTRACT at INSIDE_REPO
REF_WRITE      + REF_MUTATION, PERMISSION_CHANGE at INSIDE_REPO
PUBLISH        + NETWORK_WRITE, REF_MUTATION at NONLOCAL   ← an operator act, never a runtime's
```

The ladder is monotone and `test_effect_model.py::TheAuthorityLadderIsMonotone` asserts
it over the table, which is what lets a denial name the lowest rung that would have
permitted the effect rather than only saying no.

### 3.2 · Two boundaries that had to be drawn by measurement, not by taste

**A ref creation is not a ref mutation.** The first draft called `git checkout -b` a
`REF_MUTATION` and refused it — the very command an actor runs to *stop* sharing a branch
with another session, and the remedy for the harm this repository has actually suffered.
A creation is additive: no ref moves, no file changes, nothing is lost. Switching to an
*existing* branch is the destructive one, and the honest name for it is not
`REF_MUTATION` either: it rewrites every working-tree file that differs between the two
commits and names none of them, which is a `FILE_WRITE`.

**`git worktree list` and `git branch --show-current` are reads.** The first draft
classified a whole `git` family by its first word. `git branch --show-current` is in the
pre-flight every actor is told to run, and `git worktree list` is in this repository's own
documented corpus. Classifying a family by its first word is the same error as
classifying a command by its first word, one level down.

## 4 · The cost, isolated

🔴 The documented-corpus ratio is a **population-derived** figure and its denominator
moved on its own between revisions (208 → 211). Comparing revision 7's published
197/208 to a number measured today would attribute corpus growth to the policy diff. So
the corpus was harvested ONCE and evaluated under both policies, with the policy as the
only variable:

```
corpus 211 lines
  rev7 denied  9    survives 95.7%
  rev8 denied 16    survives 92.4%
  newly denied 7 · newly allowed 0
```

Every one of the seven, named rather than rounded away:

| # | line | reading |
|---|---|---|
| 2 | this protocol's own `GUARD_HARDENING_DEBT` table, harvested out of a fenced block. The rows read `git clean -fd  git push` | self-reference. The rule fires on the words it forbids |
| 2 | prose fragments beginning with `git` — "git at session open and", "git identity · lease derivation" | `UNKNOWN_EFFECT`: an unclassified git subcommand is refused rather than assumed harmless |
| 2 | `candidate_content_hash.py … --tip <any tip ≥ e839db38>` | a PLACEHOLDER with an unbalanced `>`. rev7 allowed these **only because its own `\d+>` ate the `38>` out of the SHA** — the same bug that hid `1>`. Fixing one exposed these |
| 1 | `git clone --no-local "$LEGEND_SOURCE" "$clone_dir"` | a real write to a destination held in a variable from an EARLIER command. `UNDERIVABLE`, the declared failure direction |

The threshold moves from 0.94 to 0.90. 🔴 Lowering a threshold to admit one's own change
is how a gate stops being one, so the number is not the claim — the isolated delta above
is, and the assertion that now carries the weight is a different one:
`test_the_escape_hatch_every_denial_recommends_actually_works` runs **every committed
Python script in the repository**, invoked plainly, and requires all of them to pass.

A first draft of that test mined the property out of the documented corpus and failed on
six lines, **not one of which was an escape-hatch failure** — they were denied for
redirects into the repository root and for `<placeholder>` spans. The property is about
the invocation, so it is asserted over invocations.

## 5 · The Codex hook: `TRUST_PENDING` was too kind, and now there is a measurement

Revision 7 recorded `TRUST_PENDING` and was careful: the runtime's per-hook trust gate
was an **inference from a flag's existence**, explicitly not a measurement, and must not
be reported as the cause of a peer's probe not firing. That care was correct. It was also
covering for an instrument that did not exist.

**It exists.** The installed app-server answers a `hooks/list` JSON-RPC method returning
one `HookMetadata` per loaded hook, with `source`, `sourcePath` and `trustStatus`. No
session, no prompt, no turn, no model call — **not a spend under Annex J.4**.

Asked from a LEGEND worktree:

```
hooks: []       warnings: []       errors: []
```

### 5.1 · Four zeroes are not a finding. The controls.

```
this repository's own .codex/config.toml at a TRUSTED PROJECT ROOT     5 hooks
the same file in a trusted NESTED git repository                       5 hooks
the same file in a git WORKTREE                                        0 hooks
the same file at that worktree's SHARED CHECKOUT                       5 hooks
```

🔴 **In a git worktree, codex-cli 0.147.0 resolves the project config layer through git
to the SHARED CHECKOUT and collects project hooks from there. A `.codex/config.toml` in
the worktree contributes nothing — with no warning and no error.**

Every LEGEND actor works in a worktree. That is the operating convention, adopted because
ten sessions on one `HEAD` had one of them commit another's unfinished work. So the Codex
registration policed **nothing, in every worktree, for every actor** — and the shared
checkout has no `.codex` at all, because the file is tracked and `main` predates it.

This is a **measured cause** for the `HOOK_NOT_FIRING` a peer observed, and it *replaces*
the trust-gate inference rather than confirming it. Trust is satisfied: the ancestor is
trusted, the layer IS discovered, no error is raised, and the hooks are still not there.

`framework/scripts/codex_hook_state.py --explain` re-runs the experiment with its
controls, in scratch space, touching no operator config.

### 5.2 · Two of my own conclusions were wrong, and a filled cell caught each

**"The registration shape is wrong."** Asserted from four zeroes with no positive
control. It is half true in a way that matters: `hooks = "./hooks.json"` is a **type
error** — `invalid type: string "./hooks.json", expected struct HooksToml` — which
settles the open question about the peer branch's `.codex/hooks.json`. But the `[hooks]`
group table this repository ships is **correct**.

**"Nesting is the cause."** The fixture varied nesting AND trust: codex resolved the
nested git repository as its own project root and asked for *that* path to be trusted,
which the fixture had not done. With trust held constant, a nested layer loads 5. A pair
of fixtures that varies two things attributes neither.

### 5.3 · What is still not established

`hooks/list` reports what is **loaded**. Every hook observed loading reports
`trustStatus: "untrusted"` — the per-hook review gate is real and is a second,
independent condition. **Loaded is not trusted, and trusted is not fired.** Only a
session probe recording a REFUSAL reaches `DEMONSTRATED`, and that remains a spend.

`runtime_parity.py --hook-status` gains `NOT_LOADED`, which sits **below**
`TRUST_PENDING`: a registration that never loaded is not on either side of the gate, and
saying `TRUST_PENDING` for it names a gate it never reached.

### 5.4 · A correction to this repository's own reasoning about paths

`.codex/config.toml` says its command path is relative because "Codex resolves the
repository root per working directory — `codex doctor` reported `repo root` as the
worktree, not the shared checkout". That is `doctor`'s notion of a repository root. The
**config layer** uses a different one, and the file reasoned from the wrong one.

## 6 · Fail-closed input handling, and an environment variable that was a bypass

`PRE_TOOL_USE_GUARD_UNKNOWN_TOOL=allow` returned ALLOW **before the policy ran at all**.
Any process able to set an environment variable could turn the guard off for every tool
it did not already know — including a renamed shell tool, which is precisely what the
denial message it printed was warning about. An environment variable is not an
authorisation, and "deliberate" is not a property `getenv` can check.

It is removed. Its replacement, `PRE_TOOL_USE_GUARD_EXTRA_SHELL_TOOLS`, can only **add**
names to the policed set; there is no spelling that removes one. The old name is asserted
**dead**, not merely unused — a variable that still worked while nothing set it would be
a bypass waiting for one line of config.

### 6.1 · An unknown field, and where it is

A first draft denied on any unknown top-level payload key. **claude-code 2.1.232 sends
`effort` and `prompt_id`**, which appear in neither the harness contract nor the § 2
table that says both input schemas were *read out of the installed runtimes*. The rule
refused every command in the session that wrote it — including the one that would have
diagnosed it — within a minute.

That is a real finding about the schema table and a bad rule. The reconciliation is
about **where** the key is:

```
unknown key BESIDE tool_input    recorded as UNMEASURED, does NOT deny
                                 it cannot change what the decision fields mean, and
                                 denying on it makes the guard fail on every release —
                                 and a guard that fails on every release gets disabled
unknown key INSIDE tool_input    DENIES
                                 that is the object the command is read out of, and the
                                 reduction takes the first key it recognises, so an
                                 unrecognised sibling may be a second command or the one
                                 the runtime has moved to
```

A payload declaring an unsupported `hook_schema_version` denies. 🔴 That is about the
*payload's declared schema*, not the runtime's version, and the two must not be
collapsed: a runtime version this bridge has not measured makes its guarantees
**unmeasured** rather than false (`cross_session_transport.md` § 3), and denying on a
version bump would make the guard the thing that breaks.

## 7 · What is demonstrated, and what is not

### 7.1 · Claude: the positive AND negative floor, live, in this session

🔴 The Claude-side hook is `DEMONSTRATED` by use, not by configuration. During the
authoring of this candidate the guard **refused its own author five times**, each with
the engine's own sentence, and each refusal was checked:

| # | what was refused | verdict |
|---|---|---|
| 1 | a heredoc probe whose Python body contained `open('framework/x','w')` as a *test fixture string* | FALSE POSITIVE — the guard cannot express a probe of itself |
| 2 | `git show HEAD:… > "$SP/rev7pol/guard_policy.py"` | FALSE POSITIVE — caused by a regression this candidate introduced and then removed |
| 3 | an inline `python3 - <<PY` whose body listed forbidden command *strings* | FALSE POSITIVE — same family as #1 |
| 4 | `bash -c 'echo hi2>f'` with a relative target | TRUE POSITIVE — the guard cannot follow `cd`, and said so |
| 5 | a `python3 - <<PY` doing a repo write to fix a typo | TRUE POSITIVE — I used `Edit`, which is what the denial recommends |

Three false positives, all one family: **a body that mentions a write is read as a body
that performs one**. Revision 7 measured the same rate and the same family. It is
unchanged and it is declared, not fixed.

And the positive floor, in the same runtime, the same session, the same guard revision,
the same worktree: this candidate's five commits were staged and committed from the shell
under the guard, using `git add <path>` and `git commit -m`.

### 7.2 · Codex: `NOT_LOADED`, therefore no write floor

`WRITE_ENABLED_PARITY` fails. A control that exists in one runtime and not the other
makes the choice of host a choice of authority, which is the invariant this protocol
exists to defend — and it is currently violated, measurably.

### 7.3 · The repair, and why it is not mine to make

The registration must reach `<shared checkout>/.codex/config.toml`. The shared checkout
holds whatever branch is checked out there — canonical **main**, which is protected and
which no Plan commit may reach. Three routes exist and all three are the operator's:

1. land `.codex/config.toml` on main;
2. add a `~/.codex/config.toml` USER-level hook registration (observed to load, § 5.1),
   at the cost of it applying to every project on the machine;
3. accept that Codex actors are read-only and say so in the role contracts.

**STOP CONDITION MET.** Not attempted.

### 7.4 · The session probe still owes what it owed

Even with the registration loaded, `trustStatus` is `untrusted` until a human reviews the
hook in a session, and firing is only demonstrated by a probe that records a REFUSAL.
`HUMAN_APPROVAL (TYPE: SPEND)` under Annex J.4. **No `APPROVAL_ID` is prefilled and none
exists.**

## 8 · Verification actually run

```
framework/scripts/test_pre_tool_use_guard.py        41 pass
framework/scripts/test_runtime_parity.py            55 pass
framework/scripts/test_effect_model.py              25 pass
framework/scripts/test_execution_attestation.py     26 pass
framework/scripts/test_post_effect_verify.py        24 pass
framework/scripts/test_execution_receipt.py         19 pass
scripts/test_guard_bash_command.py                  14 pass
```

### 8.1 · The test floor is indexed, and the index is checked

`test_effect_model.TEST_FLOOR` binds each of the brief's **eighteen** numbered items to a
module, a class and a **method name**, and `TheTestFloorIsActuallyCovered` imports each
and asserts it exists and is callable.

🔴 It failed on **ten** items when first written. That is what a coverage table is for.
Revision 7's "31/31 mutation score" was a statement about coverage that nothing checked
was coverage of anything in particular.

### 8.2 · Four mutations survived, and the assertions were in another file

The rev8-closed families were pinned only in `test_runtime_parity.py::GUARD_CLOSED_DEBT`.
Run against the guard's **own** suite, `M32` (numbered redirect), `M33` (newline), `M34`
(destination in a flag) and `M36` (`git push`) all **SURVIVED**.

A bypass closed in the policy and asserted in another file is one refactor from
returning, because the suite a reviewer runs for the guard does not bite. Thirty-eight
closed shapes and twenty-four positive controls were added to the guard's own suite, in
the same file and the same run.

That addition immediately caught an inconsistency of my own: `PERMISSION_CHANGE` was
granted only at `REF_WRITE`, so `chmod 755 /tmp/probe.sh` was denied. The boundary this
policy defends is the **repository**, and it has to be the same boundary for every effect
kind.

### 8.3 · Thirteen new mutations, and they are semantic

The test for whether a mutation is semantic: could a plausible refactor introduce it
while keeping every identifier and every message intact? `M32` is a one-character regex
edit; `M35` reorders two blocks; `M40` removes one condition from a comprehension; `M39`
replaces per-kind scopes with the flat product this candidate rejected in § 3.1. None
changes a name a test could be matching on.

## 9 · Mirror's independent findings, classified

The brief forbids absorbing unrelated architectural repairs into this candidate. None is
absorbed. **Three were re-derived here rather than accepted from the report**; the other
four are classified from the report and say so.

| # | finding | verified here | class | dependency |
|---|---|---|---|---|
| 1 | GATE 0 accepts **zero** ACTIVE leases | ✅ `lease_state.py:158` flags `len(live) > 1` and never `== 0` | **SEPARATE_P0_REPAIR** | none on this candidate |
| 2 | the lease surface is cwd-dependent | ✅ `DEFAULT_HOME = "runtime/orchestrator_lease.md"`, a relative path | **SEPARATE_P0_REPAIR** | none |
| 3 | LINT does not executable-check `current_state` | ✅ `legend_lint.py` contains **zero** occurrences of `current_state`, while `CLAUDE.md` § 0 tells every session to confirm `READY` | **SEPARATE_P0_REPAIR** | none |
| 4 | LINT may PASS without the required manifest/ledger | from the report | **SEPARATE_P0_REPAIR** | none |
| 5 | snapshot/restore can succeed with an incomplete canonical set | from the report | **SEPARATE_P0_REPAIR** | none |
| 6 | event-ledger writer/validator absent | from the report | **P1_DEBT** | 🔴 `execution_receipt.py` is a ledger with a writer and a validator and is **NOT** that one — § 10 |
| 7 | receipt implementation/schema drift | from the report | **P1_DEBT** | depends on 6 |

**RUNTIME_BRIDGE_REQUIRED: none of the seven.** Every one is about LEGEND's own state
plane; none is required for a bridge candidate, and none is fixed here.

## 10 · What this candidate does NOT do

- **It does not merge with `fulltext_receipts.py`.** That ledger is evidence in a
  *scientific* argument; `execution_receipt.py` is evidence about a *control plane*. They
  share the word "receipt" and nothing else, and
  `TheTwoLedgersAreNotTheSameLedger` asserts their schemas cannot read each other.
- **It does not make the attestation store a repository control.** It lives outside the
  repository under `~/.legend/attestation/`, because a guard that writes into the
  repository it guards is refused by its own policy — and should be. It is therefore
  **runtime-local**: not committed, not reviewed, absent from a fresh clone, and it
  proves nothing to anybody but the session that has it. Annex J.0 is the right place to
  read that class of non-guarantee.
- **It does not wire post-effect verification into a hook.** Both runtimes expose
  `PostToolUse` — Codex's binary declares `PreToolUse, PermissionRequest, PostToolUse,
  PreCompact, PostCompact, SessionStart, SessionEnd, UserPromptSubmit, SubagentStart,
  SubagentStop, Stop` — so this is *reachable*, and `SessionStart` is exactly where
  resume re-attestation belongs. Neither is registered here: registering a control whose
  `PreToolUse` sibling is `NOT_LOADED` would be building on an unverified floor.
- **It does not promote Codex.** Body § 33.1 is untouched.
- **It does not push anything.** `development` and `origin` are both public repositories.

## 11 · Independent reverts

| Unit | Commit | Revert |
|---|---|---|
| A · the effect model and the closed families | `51f6e4e` | `git revert 51f6e4e` — restores 35/46 |
| B · attestation, post-effect, receipts | `7d6d1c0` | `git revert 7d6d1c0` — removes 4 modules |
| C · fail-closed payloads, the hook state | `0d94e0d` | `git revert 0d94e0d` — restores the env waiver |
| D · the widened guard assertions | `8ffcd02` | `git revert 8ffcd02` — reopens M32–M36 |

🔴 Unit A cannot be reverted alone once B is in place: `guard_policy` imports
`effect_model`. Reverting B alone is safe; reverting A requires reverting B first.

## 12 · Residual known bypass classes, declared

```
a committed script that writes when invoked by name    deliberate — the escape hatch
                                                       every denial message names
a body that MENTIONS a write is read as one            3 false positives in this session
`cd` is not followed                                   a relative target is judged
                                                       against the payload's cwd
a variable whose VALUE begins `../`                    § 4.4 of the protocol, unchanged
NETWORK_WRITE is unobservable after the fact           declared in post_effect_verify
ignored files are outside the default snapshot         `--include-ignored` widens it
the attestation store is runtime-local                 § 10
```

## 13 · What a reviewer should attack first

1. **§ 2.1's newline claim.** Run `echo hi\ngit add -A` against `6cd4859`. If it does not
   return ALLOWED, this candidate's central finding is wrong.
2. **§ 5.1's controls.** `codex_hook_state.py --explain`. If the control does not fire,
   every zero in § 5 is uninterpretable and I have over-read a null result — which I did
   twice, and § 5.2 records both.
3. **§ 4's isolated delta.** Re-harvest and evaluate under both policies. If the rev7
   column is not 9/211, my baseline is wrong and the cost is misattributed.
4. **The mutation score.** Any mutation that survives is a hole I did not find, and § 8.2
   is evidence that I ship holes that a mutation run finds and a review does not.

---
candidate_id: CAND-20260831-RTBRIDGE13
title: The tail adds, and never substitutes
actor: plan
date: 2026-08-31
parent: CAND-20260830-RTBRIDGE12
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1)
status: FROZEN, awaiting an independent hostile review that has not been opened
---

# `CAND-20260831-RTBRIDGE13`

## 1 · Manifest (Annex D.2)

Every identifier is recorded in **§ 13 only**, derived immediately before the freeze and
nowhere else in this document. Every hash is published with the command that produces it:
**a hash without a reproducible recipe is an attestation, not evidence.**

```text
CANDIDATE_ID      CAND-20260831-RTBRIDGE13
CANDIDATE_BRANCH  plan-runtime-bridge-p00-rev13
BASE_SHA          552065572801d67fb44b2d48efe0d97757d094e3   the revision-12 CANDIDATE TIP
MAIN BASELINE     788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5   == development/main
everything else   § 13
```

**Revision 12 stays frozen at `5520655` as the reviewed record, and this candidate makes
no edit to `CAND-20260830-RTBRIDGE12.md` or to its handoff.** The one correction those two
documents need — the `GUARD_REVISION_UNIFORM` field — is stated in § 11 of THIS document
instead, naming the field it corrects. A reviewed record that is quietly amended is no
longer the record that was reviewed.

🔴 **`main` is NOT an ancestor of this candidate.** merge-base is `04693e6`; `main` carries
two additive-documentation commits the candidate does not. Integration is a MERGE, not a
fast-forward. Every `main` comparison in this document therefore names `788c357`
explicitly rather than saying "the baseline".

### 1.1 · Scope, stated as a boundary rather than as an intention

The Operator authorised this revision for **three findings and one text correction, and
nothing else**: Mirror's M1, M3 and M7, plus the `GUARD_REVISION_UNIFORM` field. Findings
M4, M5 and M6, the fenced-block census, the unresolvable-variable over-refusal class and
every residual discovered during this work are **declared in § 12 and left**, including
two that this revision's own repair makes newly visible. Nothing here widened to reach a
number.

## 2 · The one sentence

> **A name this guard re-reads may ADD an effect it would otherwise miss. It may never
> REMOVE one it would otherwise derive — and that is as true of a tail as of a
> normalisation.**

Revision 12 wrote that rule for normalisation, at `guard_policy.py:1806`, and violated it
one function away for the wrapper tail. `unclassified()` found a modelled name anywhere in
an unmodelled program's argv, re-analysed from there, and **returned** — discarding the
parent's own operands, which is the whole revision-11 `UNDERIVED_OPERAND` repair.

The three repairs are one law applied at three sites, and the law is that a carrier is
additive.

## 3 · M1 — the wrapper tail substituted where it had to add

### 3.1 · The finding, re-derived by execution before anything was repaired

The population is enumerated **from the engine**, not chosen: every member of
`WRAPPER_TAIL_PROGRAMS` × two positions × three confined scopes, plus six controls.

```text
|WRAPPER_TAIL_PROGRAMS| at revision 12    118      = 192 _KNOWN_PROGRAM_NAMES − 74 PURE_READERS
118 × 2 positions × 3 scopes              708
+ controls                                  6
denominator                               714

LOOSENED  revision 11 → revision 12        438     Mirror reported 438 — reproduced exactly
TIGHTENED revision 11 → revision 12          0
ERROR / SKIP rows, any engine                0     checked; an ERROR is not a refusal
```

Outcome tallies over the same 714, so the shape of the disagreement is visible and not
only its size:

```text
revision 11   PROHIBITED 711   ALLOWED 3
revision 12   PROHIBITED 252   ALLOWED 441   UNDERIVABLE 21
revision 13   PROHIBITED 711   ALLOWED 3     — outcome-identical to revision 11 on all 714
main          ALLOWED    714
```

### 3.2 · It reached the surface that decides whether this guard runs

A second population, 43 rows, over the runtime-config registration:

```text
                                   main    rev 11   rev 12   rev 13
mytool <HOME>/.claude/settings.json  ALLOW  DENY     DENY     DENY
  … the same path, plus `env`        ALLOW  DENY     ALLOW 🔴 DENY
  … `env` before the path            ALLOW  DENY     ALLOW 🔴 DENY
  … plus `notaprogram`   (control)   ALLOW  DENY     DENY     DENY
  … `rm` before the path (control)   ALLOW  DENY     DENY     DENY
same six rows for ~/.codex/config.toml and ~/.zshrc, and for four unmodelled program
names — mytool, pandoc, foobarbaz, ansible-playbook — so the answer is a property of the
SHAPE and not of the string `mytool`

denominator 43 · LOOSENED rev11→rev12 10 · LOOSENED rev11→rev13 0 · TIGHTENED rev12→rev13 10
controls  own-worktree tail · scratch tail · `ls -la`   ALLOWED at all four revisions  3/3
controls  rsync / install (modelled, own branch)        unchanged at all four
```

🔴 **One row of Mirror's illustration did not reproduce, and it is recorded rather than
dropped.** Mirror printed `mytool ~/.claude/settings.json → PROHIBITED RUNTIME_CONFIG` as
a control. Measured here through both `adjudicate()` and `verdict()`, with
`HOME=/Users/massimo`, cwd and `assigned` set to this worktree, the **tilde** spelling is
ALLOWED at revision 11, 12 **and** 13 — with and without the tail word. The tilde is never
expanded before scope classification, so those rows are not a wrapper-tail bypass at all;
they are a separate, revision-independent gap, declared in § 12. **M1 itself reproduces
exactly** on the absolute spelling, which is the row that moves.

### 3.3 · The repair

`unclassified()` no longer returns when a tail is found. The wrapper-tail law is extracted
into `carried_command()`, which only ever **appends**, and `underived_operand()` runs
afterwards on every path:

```python
carried_command(argv, heredocs, findings, depth,
                f"carried by `{program}`, a program this guard has no model for")
underived_operand(argv, program, findings)
```

🔴 Keyed on the **normalised** `program`, because that is the key revision 11's
`unclassified` computed its operands with. A negative that must not be loosened has to be
computed the way the engine that must not be loosened computed it. That is the mirror
image of the `renamed_by_normalisation` call site, which keys on the name AS WRITTEN for
the same reason — and the adjacent comment warns of exactly the confusion between them.

### 3.4 · What the repair keeps, and what it costs

The tail mechanism is **kept, not removed**: `mytool git add -A` still denies for
`BLANKET_STAGING`, and `xcrun sort -o <peer>/f in` still denies through the conditional
reader — both asserted in the suite, because a repair that merely stopped calling
`wrapper_tail` would pass every other test in § 6.

The cost is the restoration of revision 11's over-refusal for these shapes, no more: on
the 714 rows revision 13 is outcome-identical to revision 11, so the cost is exactly the
cost already accepted at revision 11 and re-accepted here, not a new one.

## 4 · M3 — `env` laundered every environment-prefix rule

### 4.1 · The finding, re-derived

```text
        rest = strip_wrapper_options(argv[1:], value_flags, assignments=(program == "env"))
```

`env` STRIPPED its `NAME=VALUE` tokens, so `analyse_env_prefix` was never reached through
that spelling. Population: 6 delivery spellings × 6 keys, + 12 variable rows, + 5 controls.

```text
key               git -c   NAME=V git   env NAME=V   env -i   nohup env   sudo NAME=V
core.hooksPath    DENY     DENY         ALLOW 🔴     ALLOW 🔴  ALLOW 🔴    DENY
alias.zz          DENY     DENY         ALLOW 🔴     ALLOW 🔴  ALLOW 🔴    DENY
filter.x.clean    DENY     DENY         ALLOW 🔴     ALLOW 🔴  ALLOW 🔴    DENY
pager.log         DENY     DENY         ALLOW 🔴     ALLOW 🔴  ALLOW 🔴    DENY
GIT_CONFIG_GLOBAL / LD_PRELOAD / GIT_EDITOR   prefix DENY, env ALLOW 🔴, env -i ALLOW 🔴
control  user.name · color.ui    ALLOW in all six spellings                12/12 valid
control  env FOO=1 <blanket>     PROHIBITED BLANKET_STAGING — `env` is not blind

denominator 53 · 18 rows fail revision 12's own invariant A — Mirror reported 18
```

`sudo` denied the same keys throughout, and that is the whole diagnosis: `sudo` never
stripped the assignments, so they reached the one loop that judges them.

### 4.2 · The repair is a deletion, not a second copy of the rule

The `assignments` parameter is **removed from `strip_wrapper_options` entirely**. Stripping
now stops at the first non-option token, so `env`'s assignments arrive at the top of
`analyse_argv` and are judged by the same code that judges a bare `NAME=VALUE git …`
prefix. Same object, same code, same answer — which a duplicated rule could not promise.

> a switch that turns a derivation off is a bypass with a keyword argument

That sentence is in the function's docstring, and a test asserts the signature is exactly
`(argv, value_flags)`, so the switch cannot come back for the next caller to find.

```text
after the repair, denominator 53
LOOSENED  revision 11 → revision 13      0
LOOSENED  main        → revision 13      0
TIGHTENED revision 12 → revision 13     18     — exactly the 18 that failed invariant A
control   ordinary keys, all 6 spellings ALLOW at revision 13                12/12 valid
```

### 4.3 · The suite class that should have caught it

`TheEnvironmentSpellingGetsTheSameAnswerAsTheFlag` tested **two** spellings, and both were
derived by the same code path — so the class could not see the four that were not. Its
`_pair()` helper is now derived from a module-level `DELIVERIES` enumeration of seven
spellings, and the two matrices below it assert `6 × len(DELIVERIES)` and
`2 × len(DELIVERIES)` cells with the denominator asserted in the test body. A spelling
added to that set is measured by every test in the class without one of them being edited.

**A list standing in for a family, inside the test written to stop a list standing in for
a family.**

## 5 · M7 — `PACKAGE_RUN_SUBCOMMANDS` is a list

### 5.1 · The finding, re-derived with two payloads so attribution is separable

```text
                                    main   rev 11  rev 12  rev 13
npm run-script <blanket staging>    DENY   ALLOW   ALLOW 🔴 DENY
npm start / test / node / task / script, deno task — the same six rows
npm run-script rm -rf <peer>/…      ALLOW  ALLOW   ALLOW   ALLOW   ← see § 12.1
control  npm run · npm exec · npx · uvx, both payloads     DENY at rev 12 and rev 13
control  the same two payloads bare                        DENY at rev 12 and rev 13

denominator 26 · LOOSENED main→rev12  7 — Mirror reported 7, reproduced exactly
                 LOOSENED main→rev13  0
```

main's refusal of the first payload is a **text match on the blanket string**, not a safety
property: main allows the destructive payload behind every one of those verbs, and bare.

### 5.2 · The repair is a family, applied at two sites

Adding six words to `PACKAGE_RUN_SUBCOMMANDS` is the same list one entry longer, and two of
the seven loosened verbs (`npm node`, `npm script`) are not npm verbs at all — putting them
on a list would be padding a count to hit a target. So the tail is read as the command it
is, at the two fall-throughs where a program this module models is invoked in a SHAPE it
does not:

```text
site 1  a package manager whose verb is neither a run verb nor an install verb
site 2  an interpreter with no inline body and no module — `deno task`, `bun task`
```

Both call `carried_command`, which fires **only** when the argv names a program some table
here models. `npm ls`, `npm view react`, `npm audit`, `npm --version`, `python3 script.py`,
`node app.js` and `deno run mod.ts` carry nothing and are untouched — asserted as a matrix
in the suite, in its own test, because four of this lineage's repairs refuse more and a
repair that refuses more is one bad predicate away from refusing the reader's real work.

🔴 `python3 script.py` is safe for a reason worth stating: `script.py` does not normalise
onto `script` — the version-suffix rule peels digits, not extensions — so no tail is found.
That was checked by execution, not assumed.

Site 2 is a **separate** mutation operator from site 1 on purpose (§ 8): `deno task` reaches
the interpreter branch and not the package-manager one, and a single mutant covering only
the first would leave this half unmeasured — which is how `deno task` survived revision 12.

## 6 · The tests, and BOTH halves are reported

**This is why revision 13 exists at all.** Revision 12 froze with six suites, 296 tests, all
green, and M1 and M3 invisible to every one of them — while 118 mutation operators scored
116 KILLED / 2 EQUIVALENT / 0 SURVIVED. A test that passes against the engine it is meant
to constrain has demonstrated nothing.

`framework/scripts/test_guard_families_rev13.py`, 13 tests, run against the revision-12
engine at `5520655` (policy blob `e19e7029927a2748…`, verified before the run) and against
this tree:

```text
                                                              REV12   REV13
M1  every_tail_word_leaves_the_parents_confined_operand_derived  FAIL   PASS
M1  the_same_object_gets_the_same_answer_with_and_without_a_tail FAIL   PASS
M1  the_registration_is_not_reachable_behind_a_tail_word         FAIL   PASS
M1  unclassified_cannot_return_between_the_tail_and_the_operands FAIL   PASS
M1  the_tail_still_contributes_its_own_finding                   PASS   PASS  ← control
M3  an_execution_control_key_gets_one_answer_in_every_spelling   FAIL   PASS
M3  every_always_execution_control_variable_survives_env         FAIL   PASS
M3  strip_wrapper_options_has_no_switch_that_turns_a_derivation_off FAIL PASS
M3  an_ordinary_key_is_allowed_in_every_spelling                 PASS   PASS  ← control
M7  an_unrecognised_run_verb_still_carries_its_command           FAIL   PASS
M7  a_carried_command_reaches_a_confined_write                   FAIL   PASS
M7  the_carrier_law_lives_in_one_function_reached_from_every_site FAIL   PASS
M7  ordinary_package_manager_work_is_untouched                   PASS   PASS  ← control

                                                           10 of 13 FAIL   13 of 13 PASS
```

The amended revision-12 class, same treatment:

```text
test_guard_families_rev12.py                               REV12   REV13
a_config_key_gets_one_answer_however_it_is_delivered        FAIL   PASS
the_execution_control_keys_deny_in_every_spelling           FAIL   PASS
the remaining 51 tests                                      PASS   PASS
                                                       2 of 53 FAIL   53 of 53 PASS
```

The three rows that pass at both revisions are **declared controls, not regression cases**:
the two cost-side ordinary-work matrices, and the row proving `wrapper_tail`'s own
mechanism was kept rather than removed.

### 6.1 · One test had to be rewritten because it passed against revision 12

The first draft of `unclassified_cannot_return_…` asserted that `underived_operand` is the
**last statement** of `unclassified`. That is true at revision 12 as well, where the call is
merely UNREACHABLE — the tail branch returns above it. It passed the fail-before check and
proved nothing. It now asserts **reachability** over the parse tree: no `return` may occur
after the carrier is consulted. Recorded in the test's own docstring rather than quietly
corrected, because the near-miss is the more useful artefact.

## 7 · The six existing suites, re-run at this tree

```text
framework/scripts/test_guard_families_rev13.py    13 tests   OK     5s   ← new
framework/scripts/test_guard_families_rev12.py    53 tests   OK    36s
framework/scripts/test_guard_families_rev11.py    42 tests   OK     4s
scripts/test_guard_bash_command.py                16 tests   OK     0s
framework/scripts/test_runtime_diagnostics.py     66 tests   OK     2s
framework/scripts/test_pre_tool_use_guard.py      47 tests   OK    18s
framework/scripts/test_runtime_parity.py          72 tests   OK   124s
                                                 309 tests, seven suites, rc=0 each
```

🔴 **`test_runtime_parity.py` caught a defect in a file this revision added**, and it is
recorded rather than quietly fixed: `test_guard_families_rev13.py` was committed at mode
`100644` while carrying a shebang. `TheBridgesOwnFilesDoNotAddSurfaceDefects` failed, the
mode was corrected with `git add --chmod=+x`, and the suite passes. An existing check
biting on new work is the check working.

## 8 · Mutation

### 8.1 · The revision-12 baseline, and why it is not the target

Mirror's completed revision-12 run: **118 rows == `len(MUTATIONS)`, 118 distinct names,
KILLED 116, EQUIVALENT 2 (`M07`, `M109`, not folded into KILLED), SURVIVED 0,
UNUSABLE / ANCHOR_MISSING / AMBIGUOUS 0.** Mirror's verdict on its own number is the part
that matters:

> HIGH for fidelity, LOW for coverage of this revision. It says nothing about M1, M3 or
> M7 — those are not breakages of existing behaviour, they ARE the existing behaviour.

Five of the seven mechanisms revision 12 declared were named by **zero** of its 118
operators — `wrapper_tail`, `analyse_env_prefix`, `READER_WRITE_MODEL`,
`EXECUTION_CONTROL_KEY_SUFFIXES`, `PACKAGE_RUN_SUBCOMMANDS` — measured with
`normalise_program`, `unclassified`, `underived_operand` and `PURE_READERS` as non-zero
positive controls in the same count. **A mutation score measures fidelity, never coverage.**
No score below is offered as evidence that this guard is sound.

### 8.2 · Anchors checked BEFORE the run, against the committed blob

```text
ref 5520655 (revision 12)   len(MUTATIONS) 118   rows 118   distinct 118   ALL OK
ref <content tip> pre-add   len(MUTATIONS) 118   rows 118   distinct 118   ALL OK
ref <content tip> post-add  len(MUTATIONS) 123   rows 123   distinct 123   ALL OK
```

The middle row is the one that mattered: this revision refactored the exact function three
existing operators anchor into, and a detached anchor reports `ANCHOR_MISSING`, which is
never a kill. The check ran against the committed blob **before** the battery, not by
reading the report afterwards. The row count is asserted equal to `len(MUTATIONS)` and the
names checked for duplicates, so the tool that summarises never defines the denominator.

### 8.3 · Five operators for mechanisms that had none

```text
M118  the wrapper tail SUBSTITUTES again — revision 12's defect reinstated verbatim
M119  `env` launders its assignments again — revision 12's other defect, verbatim
M120  a package manager's unrecognised run verb stops carrying its command
M121  the interpreter's unrecognised verb, a SEPARATE site on purpose
M122  `analyse_env_prefix` is defined and never called
```

M118 and M119 do not invent a defect: they restore revision 12's, so each is a run of the
question *would we notice if this were undone*. `FAMILY_SUITES_13` was checked as a
DISCRIMINATOR before any operator was aimed at it — 10 of 13 failures against the
revision-12 engine, none against this tree — which is the rule this harness states for
`FAMILY_SUITES` and did not apply to `FAMILY_SUITES_12`.

### 8.4 · The full battery, pinned

One run, uninterrupted, `rc=0`. The harness pins the tip once and prints it, and the tip it
printed is the tip frozen as `CONTENT_TIP` in § 13 — checked, because three runs in this
lineage were discarded for measuring a tree that moved under them:

```text
TIP printed by the harness   d8c888be89f01293bfdde2d57e164b8572518fdf
tip after the run            d8c888be89f01293bfdde2d57e164b8572518fdf   equal ✓
uncommitted paths at launch  0
```

🔴 **The count is taken from a BOUNDED line range, and the denominator comes from the
module and not from the log.** Mirror's first revision-12 recount was wrong because a
pattern over the whole file matched the summary block's own lines as rows. The rows here
are lines 4–126 — from the blank line after `TIP` to the blank line before the summary —
and the count is asserted against `len(MUTATIONS)` with the names checked for duplicates
and for set-equality with the declared operators.

```text
row line range                [4, 126]       123 rows
len(MUTATIONS)                123            rows == len(MUTATIONS)          ✓
distinct names                123            duplicates                      none
names == declared operator set                                               ✓
tally sums to the row count                                                  ✓

KILLED                        121
EQUIVALENT                      2   M07, M109 — NOT folded into KILLED
SURVIVED                        0
UNUSABLE                        0
ANCHOR_MISSING                  0
ANCHOR_AMBIGUOUS                0
WORKTREE_FAILED                 0
FALSE EQUIVALENCE               0   no operator declared equivalent was killed
```

🔴 **My first count of this same log said `KILLED 120` and left one row unparsed.** The
pattern was `M\d+` and one operator is named `M47b`. The tool defined the population and
excluded a real member — the third instance of that failure mode in this queue, hit by me
after being warned about it. It was caught only because the tally did not sum to the row
count, which is why that assertion is in the table above rather than in a comment.

Against revision 12's baseline (118 rows, KILLED 116, EQUIVALENT 2, SURVIVED 0):

```text
operators   118 -> 123    the five added in § 8.3
KILLED      116 -> 121    +5, exactly the five added
EQUIVALENT    2 ->   2    the same two, M07 and M109
SURVIVED      0 ->   0
M115 / M116 / M117 — revision 12's own three — KILLED, as revision 12 claims
M118 … M122        — revision 13's five                KILLED
```

**This number is not evidence that the guard is sound, and it is not a target.** Revision 12
scored 116 of 118 with M1 allowing 438 of 714 and reaching the runtime registration. What
the five new operators buy is narrower and worth stating plainly: **a regression back to
revision 12's behaviour is now a breakage the suite can see, and it was not before.**

## 8.5 · Mutation debris

`mutate_guard_suite.py` adds and removes one worktree per operator, and a killed run
strands entries that inflate `guard_revision.survey`. Checked before the census in § 13 and
not merely afterwards:

```text
git worktree list | grep -c mutate      0   after the run
```

## 9 · Regression, by SUBTRACTING FINDING SETS

Never by counts. Every population is enumerated before it is measured, and every negative
carries its denominator.

```text
POPULATION                      DENOM   MAIN→REV13   REV12→REV13   REV11→REV13
                                        loosened     loosened      loosened
M1 wrapper-tail enumeration       714       0            0             0
M1 runtime-config registration     43       0            0             0
M3 delivery spellings              53       0            0             0
M7 package/interpreter verbs       26       0            0             0
committed hostile corpus          146       0            0             0
live composability chains          39       0            0             0
write-primitive residual (§12.1)   62       0            0             0
tail-prefix residual  (§12.3)      56       0            0             0
                                 ────
                                 1139       0            0             0
```

🔴 The two residual populations are in this table on purpose. They are rows this revision
did NOT close, and including them is what makes the zero honest: a regression table built
only from the populations a repair was aimed at reports the repair, not the guard.

Tightenings, in the same table, because a repair that only refuses more should say so:

```text
                                  REV12→REV13 tightened     REV11→REV13 tightened
M1 wrapper-tail enumeration              438                        0
M1 runtime-config registration            10                        0
M3 delivery spellings                     18                       33
M7 package/interpreter verbs               8                       10
committed hostile corpus                   0                        2 (inherited at rev 12)
live composability chains                 15                        7
write-primitive residual (§12.1)           4                        5
tail-prefix residual  (§12.3)              8                       16
```

### 9.1 · The corpus is not the population, and says so

```text
committed corpus, 146 cases, at this tree
  BYPASSES (shapes that must be refused, ALLOW)   0 of 103
  positive controls                              43
  controls wrongly refused                        0
  REV12 → REV13   LOOSENED 0   TIGHTENED 0   (identical tables)
  MAIN  → REV13   LOOSENED 0   TIGHTENED 96
  REV11 → REV13   LOOSENED 0   TIGHTENED 2   (AA4, AA6 — inherited from revision 12)
```

🔴 **"LOOSENED = 0 on the corpus" was equally true at revision 12, while 438 of 714 were
loosened.** The corpus is 146 committed shapes; M1's population is 714 enumerated ones and
the corpus contains none of them. This figure is reported because it is the committed
instrument, not because it is evidence of closure.

🔴 The corpus's revision ladder has **no `rev13` rung**: its newest rung is named `rev12`
and is pinned to `HEAD`, so an unpinned run prints this tree under the label `rev12`. The
true revision-12 engine was measured separately with
`--engine-sha rev12=5520655`. Declared in § 12.

### 9.2 · Live composability chains — two mechanisms crossed in one command

39 rows: the five Mirror measured as revision-11 → revision-12 loosenings, its two
attribution controls, chains crossing each pair of the three repairs, the registration
reached through each repaired route, two depth chains, and 15 ordinary-work rows.

```text
                                       main   rev 11  rev 12  rev 13
docker run -v <peer>:/w node build     ALLOW  DENY    ALLOW 🔴 DENY   ← Mirror's ordinary one
env mytool <peer>/framework/x env      ALLOW  DENY    ALLOW 🔴 DENY
mytool <peer>/framework/x python3.12   ALLOW  DENY    ALLOW 🔴 DENY
sqlite3 <peer>/new.db env              ALLOW  DENY    ALLOW 🔴 DENY
mytool <registration> env  (absolute)  ALLOW  DENY    ALLOW 🔴 DENY
mytool ~/.claude/settings.json env     ALLOW  ALLOW   ALLOW   ALLOW  ← the tilde, § 12.2
control  make -C <peer> install        ALLOW  DENY    DENY    DENY   ← Mirror's correction
control  make -C <peer> env            ALLOW  DENY    ALLOW 🔴 DENY
nohup env <config key> git status      ALLOW  ALLOW   ALLOW 🔴 DENY
mytool npm run-script <blanket>        DENY   ALLOW   ALLOW 🔴 DENY   ← M1 × M7
env <config key> npm run-script …      ALLOW  ALLOW   ALLOW 🔴 DENY   ← M3 × M7
mytool npm run-script sed -i <peer>    ALLOW  DENY    ALLOW 🔴 DENY   ← three carriers deep
nohup … the same, four deep            ALLOW  DENY    ALLOW 🔴 DENY

denominator 39 · LOOSENED main→rev13 0 · rev11→rev13 0 · rev12→rev13 0
                 TIGHTENED rev12→rev13 15 · rev11→rev13 7
ordinary work   15 of 15 unchanged from revision 12 (the one DENY, `sed -i` in the
                assigned worktree, is revision 11's declared shell-write rule)
```

Four of Mirror's five named chains are closed. The fifth is the tilde spelling, § 12.2.

## 10 · Positive-control false refusals, with the denominator

Each denominator below is derived from its own source — the enumeration in the test, or
the control rows in the results file — never counted by eye.

```text
ordinary package-manager and script work (rev13 suite)   10 of 10 ALLOW
ordinary git keys × 8 delivery spellings  (rev13 suite)  24 of 24 ALLOW
ordinary git keys × 7 delivery spellings  (rev12 suite)  14 of 14 ALLOW
ordinary git keys, the M3 measurement table              12 of 12 ALLOW
ordinary git keys, the § 12.3 residual table             28 of 28 ALLOW
M1 controls: no-tail PEER / SHARED / GITDIR               3 of 3  DENY  at 11, 12 and 13
M1 controls: own-worktree tail · scratch tail · `ls -la`   3 of 3  ALLOW at 11, 12 and 13
composability table, ordinary rows                       14 of 15 ALLOW  ← see below
committed corpus positive controls                       43 of 43 ALLOW
                                                     ──────────────────────
                                                        151 of 152, 1 refused
```

🔴 The one refusal is `sed -i s/a/b/ framework/x` — a shell write inside the actor's own
assigned worktree, refused by revision 11's `SHELL_WRITE_IN_ASSIGNED_WORKTREE` rule at
revision 11, revision 12 **and** revision 13 alike. It is inherited and unchanged, and it
is left in the numerator rather than moved out of the population, because a control set
that drops its own inconvenient member stops being a control set.

The three revision-12 false refusals Mirror measured — `python3.12 -m venv .venv`,
`pip install -r`, `git worktree add` — are **inherited and unchanged**; this revision
neither repairs nor worsens them. The repository-wide fenced-block census (22 FALSE_REFUSAL
of 296 at revision 12) is `DECLARED_DEBT` and was not re-run, per the Operator's fence.

## 11 · `GUARD_REVISION_UNIFORM` — the field, stated honestly

The revision-12 manifest reads:

> **`GUARD_REVISION_UNIFORM = NO`** — the census reads `UNDERIVABLE` across 14 worktrees

Those are different answers. `NO` is a measurement — *the fleet is not uniform*.
`UNDERIVABLE` is a failure to measure — *one of them could not be read* — and
`uniformity()`'s own docstring argues at length that reporting the second as the first is
the error to avoid. **The correct value is `UNDERIVABLE`,** and it is recorded that way in
§ 13 of this document. `CAND-20260830-RTBRIDGE12.md` and its handoff are left untouched, so
this correction sits beside the frozen record rather than inside it.

### 11.1 · Why the `UNKNOWN` appears, re-derived by execution

```text
REV11_MARKERS = ("extract_herestrings", "unclassified")
measured on the REV10 blob e01d6d2, rebuilt with git archive:
    extract_herestrings   occurrences 0    counts_as_marker False
    unclassified          occurrences 2    counts_as_marker True     ← predates revision 11
1 of 2 → partial → UNKNOWN
generation_of(<clean REV10 tree>)  = UNKNOWN     ← called on the reconstructed tree
generation_of(<REV12 tree>)        = REV12       ← positive control, same call
```

`unclassified` is not a revision-11 discriminator: it exists at revision 10. So a **clean**
revision-10 worktree reports `UNKNOWN`, `if rev10: return REV10` is unreachable for any real
revision-10 tree, and the census's single `UNKNOWN` row — `evidence-index` at `e01d6d2` — is
spurious. The failure direction is SAFE: `UNDERIVABLE` blocks and never permits.

This is a **text correction**. The instrument is not rewritten here: repairing
`REV11_MARKERS` is Mirror's M5, outside this revision's three-finding scope, and § 12
carries it.

## 12 · Declared debt — carried, not closed

### 12.1 · `_KNOWN_PROGRAM_NAMES` omits every plain write primitive — NEW, and it is mine to declare

`WRAPPER_TAIL_PROGRAMS` is derived from `_KNOWN_PROGRAM_NAMES`, and that union does **not**
include `WRITES_ALL_OPERANDS` (5), `WRITES_LAST_OPERAND` (6) or `DESTROYS_OPERANDS` (3).
`rm` is not a name `wrapper_tail` can see. Mirror observed one instance of this
(`make -C <peer> install` denies) and read it as benign, which it is at the `unclassified`
site — `underived_operand` catches the operand there. It is **not** benign at the two sites
this revision adds, which have no operand backstop:

```text
14 write primitives × 3 carrier sites + 2 controls per site + 14 bare rows = 62
                                              main  rev11  rev12  rev13
bare at a peer worktree            14 rows    ALLOW  DENY   DENY   DENY
behind `mytool` (unclassified)     14 rows    ALLOW  DENY   DENY   DENY   ← operand rule
behind `npm run-script`            14 rows    ALLOW  ALLOW  ALLOW  ALLOW  🔴
behind `deno task`                 14 rows    ALLOW  ALLOW  ALLOW  ALLOW  🔴
control  `git add -A` at each site  3 rows    DENY   ALLOW  2 ALLOW DENY   ← the carrier fires
control  `sort -o <peer>` at each   3 rows    ALLOW  varies varies  DENY   ← the carrier fires
LOOSENED main→rev13 0 · rev11→rev13 0 · rev12→rev13 0   TIGHTENED rev12→rev13 4
```

**Not a regression** — identical at main, revision 11, revision 12 and revision 13 — and the
positive controls in the same table show the carrier mechanism works, so the gap is the
NAME SET and not the carrier. Two candidate repairs, neither taken here because both are
outside the three findings: union the write-primitive tables into `_KNOWN_PROGRAM_NAMES`,
or give the two new carrier sites the `UNDERIVED_OPERAND` backstop `unclassified` has. The
second changes answers for ordinary work (`python3 <peer>/x.py` would begin to deny) and
should not be taken without its own enumeration.

The revision-13 suite states this limit in the docstring of the test it bounds, so that
test's passing is not read as a closure it does not claim.

### 12.2 · A `~` in a runtime-config path is never expanded — NEW

```text
15 tilde rows of 43 (§ 3.2)   ALLOWED at main, revision 11, revision 12 AND revision 13
the absolute spelling of the same object   DENIED at 11, 12 (bare) and 13
```

Same object, two spellings, two answers — invariant A, at a level below the one M3
repairs. Revision-independent, so not a regression and not this revision's to fix. It is
also the reason one row of Mirror's M1 illustration did not reproduce here (§ 3.2).

### 12.3 · A carried tail drops the assignment prefix in front of it — NEW

`wrapper_tail` returns the argv **from** the modelled program, so a `NAME=VALUE` prefix
standing in front of that program inside another program's argv is skipped and never
reaches `analyse_env_prefix`. This is the M3 laundry one level out, through a carrier
rather than through `env`:

```text
4 execution-control keys × 7 delivery spellings + 4 ordinary keys × the same 7 = 56
                                    rev 13 exec keys      rev 13 ordinary keys
mytool <ASSIGN> git status           4 of 4 ALLOW 🔴        4 of 4 ALLOW
npm run-script <ASSIGN> git status   4 of 4 ALLOW 🔴        4 of 4 ALLOW
deno task <ASSIGN> git status        4 of 4 ALLOW 🔴        4 of 4 ALLOW
<ASSIGN> git status                  4 of 4 DENY            4 of 4 ALLOW
env / env -i / sudo <ASSIGN> git …  12 of 12 DENY          12 of 12 ALLOW
LOOSENED main→rev13 0 · rev11→rev13 0 · rev12→rev13 0   TIGHTENED rev12→rev13 8
```

**Not a regression** — the 12 carrier rows answer ALLOW at main, revision 11, revision 12
and revision 13 alike — and the 28 ordinary-key rows are the positive control in the same
table, so the failure is specific to the execution-control keys exactly as M3 was.

Closing it means teaching `wrapper_tail` to carry the assignments it steps over, which
changes what `carried_command` hands to `analyse_argv` at all three sites. That is a
change to the mechanism M1 and M7 rest on, made after both were measured, and it is
outside the three findings. Declared and left.

### 12.4 · The revision ladder has no `REV13` rung

```text
generation_of(<this tree>) = REV12        REV12_MARKERS are all still present and invoked
hostile_corpus.py --revision  choices: main rev7 rev8 rev9 rev10 rev11 rev12
```

Both instruments name this tree `rev12`. Neither is wrong about what it measures — the
revision-12 markers ARE all here — and both will mislabel a revision-13 tree until a rung
is added. Adding one is an instrument change and is left.

### 12.5 · `run_release_regressions.py` reports FAIL, and it did at revision 12 too

Measured by subtracting failing **test-id sets** over matched `git archive` extractions of
`788c357`, `5520655` and this content tip, so the extraction artefact is common to all three
and the delta is attributable:

```text
suites measured                     9   (the 8 that fail, + test_public_release_gate.py
                                         as a positive control, which passes in all three)
failing test-ids at main            7
failing test-ids at revision 12     9
failing test-ids at revision 13     9
REVISION 12 → REVISION 13   NEW 0   FIXED 0     ← identical sets
MAIN        → REVISION 13   NEW 3   FIXED 0     ← all three already present at revision 12
```

The three that revision 12 introduced are `test_repository_local_python_commands_exist`,
`test_documented_cli_flags_exist` and `test_inline_repository_paths_resolve`. **This
revision adds none.** Mirror's review did not run this runner, so this is a new observation
about revision 12's state, not a revision-13 regression.

🔴 One instability, stated rather than smoothed: `test_documented_cli_flags_exist` appeared
in the first sweep for **both** trees and in none of 12 subsequent runs (8 of 8 at this tip,
4 of 4 at revision 12). It runs a 15-second subprocess timeout per documented target and
the first sweep ran under load. It never differed between the two trees, so the
REV12 → REV13 delta is empty under both measurements.

### 12.6 · Carried from revision 12, untouched and unexamined here

```text
M4  `_env_value_is_actor_controlled` is a character class — `sh -c '<payload>'` passes it
M5  REV11_MARKERS is not a REV11 discriminator (§ 11.1 re-derives it; the repair is not here)
M6  EXECUTION_CONTROL_KEY_SUFFIXES is a component-equality test, not a suffix test
    3 real escaping git keys: core.alternateRefsCommand, interactive.diffFilter, submodule.*.update
the repository-wide fenced-block census   22 FALSE_REFUSAL of 296 — fenced by the Operator
the unresolvable-variable over-refusal    verified UNCHANGED at revision 12; not re-run here
`python3.12 -m venv`, `pip install -r`, `git worktree add`   inherited false refusals
independent_privacy_scan BLOCK rows       17 of 38 findings — identical set at revision 12
```

## 13 · The identifiers

Every value below was derived **immediately before the freeze**, by the command printed
beside it, and from no earlier draft.

```text
CANDIDATE_ID      CAND-20260831-RTBRIDGE13
CANDIDATE_BRANCH  plan-runtime-bridge-p00-rev13
BASE_SHA          552065572801d67fb44b2d48efe0d97757d094e3   the revision-12 CANDIDATE TIP
CONTENT_TIP       d8c888be89f01293bfdde2d57e164b8572518fdf
CONTENT_HASH      142a228245416d6c2f5d460bb17682caf0257b3b54b1533a1815aa3017ea89db
GUARD_GENERATION  REV12    ← read from the SHAPE of what is installed; see § 12.4
POLICY_HASH       66cc2970ce6a10ea     framework/scripts/guard_policy.py
                  66cc2970ce6a10ea90c0322af1475530755cf5ed945c26d92962184c9bc1ceff  (full)
ENTRY_HASH        2467f4be9cc6fb37     scripts/guard_bash_command.py   (unchanged from
                  2467f4be9cc6fb37f2c7b70cecdc8b34472289221e897d36c0ee1e83bf0c5b1d   rev 12)
MAIN BASELINE     788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5   == development/main, verified
GUARD_REVISION_UNIFORM   UNDERIVABLE     ← see § 11; the value, not a paraphrase of it

CANDIDATE_TIP     A manifest cannot contain the hash of the commit that carries it, so it
                  is stated as a RULE:
                      git -C <worktree> rev-parse plan-runtime-bridge-p00-rev13
                  It differs from CONTENT_TIP by exactly the two governance files this
                  candidate adds, and § 13.2 MEASURES — rather than argues — that the
                  content hash is invariant across that difference.
```

```bash
# every value above, re-derived immediately before the freeze
W=<the candidate worktree>
git -C $W rev-parse HEAD                                          # CONTENT_TIP
git -C $W rev-parse --abbrev-ref HEAD                             # CANDIDATE_BRANCH
python3 governance/scripts/candidate_content_hash.py \
  --base 552065572801d67fb44b2d48efe0d97757d094e3 \
  --tip  d8c888be89f01293bfdde2d57e164b8572518fdf                 # CONTENT_HASH

# the hashes from the COMMITTED blob, never from disk
git -C $W show <TIP>:framework/scripts/guard_policy.py    | shasum -a 256   # POLICY_HASH
git -C $W show <TIP>:scripts/guard_bash_command.py        | shasum -a 256   # ENTRY_HASH

# GUARD_GENERATION and the fleet census, read from the shape of what is installed
python3 framework/scripts/guard_revision.py
git -C $W worktree list | grep -c mutate    # BEFORE reading the census, not after
```

### 13.1 · Ancestry, verified rather than assumed

```text
BASE_SHA 5520655 IS an ancestor of CONTENT_TIP                        YES
main     788c357 is NOT an ancestor of CONTENT_TIP                    confirmed
merge-base(main, CONTENT_TIP)                                         04693e6
commits BASE..CONTENT_TIP                                             5
files   BASE..CONTENT_TIP                                             4
        framework/scripts/guard_policy.py
        framework/scripts/mutate_guard_suite.py
        framework/scripts/test_guard_families_rev12.py
        framework/scripts/test_guard_families_rev13.py
        (+635 / −34)
remote refs containing CONTENT_TIP                                    0
```

Integration is therefore a MERGE, not a fast-forward. Nothing has left this worktree.

### 13.2 · `CONTENT_TIP` ≠ `CANDIDATE_TIP`, and the invariance is MEASURED

`governance/candidates/` is a declared `CONTROL_PLANE_ROOT` and the domain filter is a
prefix match, so the two governance files are outside the hashed domain. **A structural
argument is not a measurement.** Stated so one command falsifies it:

```text
hash at CONTENT_TIP    d8c888b   142a228245416d6c2f5d460bb17682caf0257b3b54b1533a1815aa3017ea89db
hash at CANDIDATE_TIP  <tip>     MUST equal the value above
git -C $W diff --name-only d8c888b <CANDIDATE_TIP>
   MUST list exactly:
   governance/candidates/CAND-20260831-RTBRIDGE13.md
   governance/candidates/HANDOFF-20260831-RTBRIDGE13-MIRROR.md
```

The measured result of both commands is recorded in § 13.4, taken after the freezing
commit and not predicted before it.

### 13.3 · Hygiene at the frozen tip, with a positive control

The same three commands were run twice: once while the two governance files were still
untracked, and once after the freezing commit. **The first run is the positive control** —
it proves the check can report dirt rather than being silently empty — and it names how
many files were walked.

```text
                                        BEFORE the freezing commit    AFTER
git status --porcelain=v1 -uall         2 rows (the two ?? files)     ← § 13.4
git diff --name-status  (tree vs index) empty                         ← § 13.4
git diff --cached --name-status         empty                         ← § 13.4
git diff --summary      (mode changes)  empty                         ← § 13.4
files walked, index                     678
files walked, HEAD tree                 678                (equal — index matches HEAD)
```

### 13.4 · The readings taken after the freezing commit

A document cannot contain a reading taken after the commit that carries it, so the freeze
is two commits and this section names the first one as the object it describes.
`0330a55` adds this file and the handoff; a second commit adds only this section. The
`CANDIDATE_TIP` rule in § 13 resolves to that second commit, and every reading below is
re-run there — the values are tree-comparisons and file hashes, so they do not move.

**Measured at `0330a55`, the first governance commit:**

```text
hash @ CONTENT_TIP    d8c888b  142a228245416d6c2f5d460bb17682caf0257b3b54b1533a1815aa3017ea89db
hash @ 0330a55                 142a228245416d6c2f5d460bb17682caf0257b3b54b1533a1815aa3017ea89db
                                                                                     EQUAL ✓
git diff --name-only d8c888b 0330a55
    governance/candidates/CAND-20260831-RTBRIDGE13.md
    governance/candidates/HANDOFF-20260831-RTBRIDGE13-MIRROR.md      exactly two ✓

POLICY_HASH @ CONTENT_TIP    66cc2970ce6a10ea90c0322af1475530755cf5ed945c26d92962184c9bc1ceff
POLICY_HASH @ 0330a55        66cc2970ce6a10ea90c0322af1475530755cf5ed945c26d92962184c9bc1ceff
    🔴 invariance VERIFIED, not assumed. The positive control is in the same table:
    test_guard_families_rev12.py @ BASE 8955cbf0dc6d4be9 · @ tip 4933d465a3858410 —
    a file that DID change hashes differently, so an equal pair above is a reading and
    not a broken command.
    🔴 One broken command was caught this way. `$T:framework/…` in zsh applies the `:r`
    modifier and hands `git show` a mangled argument; the hash that came back was
    `e3b0c44298fc…`, the sha256 of EMPTY INPUT. Braces, and a control that must differ.

git status --porcelain=v1 --untracked-files=all      0 rows      (2 rows before, § 13.3)
git diff --name-status            (tree vs index)    empty
git diff --cached --name-status   (index vs HEAD)    empty
git diff --summary                (mode changes)     empty
files walked, index 680 · HEAD tree 680 · equal      (678 before the two files were added)
mutate-* worktree debris                             0
remote refs containing the tip                       0
```

**The publication gate, run at the CANDIDATE tip and not at the content tip** — revision 11
shipped a gate failure because it measured at the content tip, and the candidate tip is the
object handed over:

```text
tip measured   0330a55        working tree clean, 0 rows
VERDICT        PASS
BLOCKS         0
REVIEW         4, all content (PARENT_OF_ORIGIN), none guard — the same four as revision 12
legend_lint.py VERDICT: PASS
```

## 14 · What is NOT claimed

- **No readiness verdict of any kind.** Not integration readiness, not write-floor
  readiness. Three findings were repaired; the review that decides what that is worth has
  not been opened.
- **`NO_KNOWN_STRUCTURAL_BYPASS` is NOT asserted.** M4 and M6 are open by measurement, and
  § 12.1 is a bypass this revision measured and declined to close.
- The fences are unchanged: `R3_REGISTRATION_ANCHORED = NO`,
  `LIVE_CODEX_PROBE_MEANINGFUL_NOW = NO`, `CODEX_WRITE = NO_GO`.
- Nothing was merged, pushed, or deployed. `.claude/settings.json` and the main root's
  `scripts/guard_bash_command.py` were not touched, so **the guard that ran during this
  session is `main`'s LEGACY guard, not the engine repaired here.**
- The mutation score is fidelity, not coverage, and is offered as neither a target nor a
  reassurance.
- "LOOSENED = 0" is stated per population with its denominator, never as a property of the
  guard.

## 15 · Commands, so every number above is re-derivable

```bash
# the seven suites, at this tree
python3 framework/scripts/test_guard_families_rev13.py
python3 framework/scripts/test_guard_families_rev12.py
python3 framework/scripts/test_guard_families_rev11.py
python3 scripts/test_guard_bash_command.py
python3 framework/scripts/test_runtime_diagnostics.py
python3 framework/scripts/test_pre_tool_use_guard.py
python3 framework/scripts/test_runtime_parity.py

# the discriminator: revision 12's engine from its committed blob, this suite dropped in
git archive 552065572801d67fb44b2d48efe0d97757d094e3 | tar -x -C <scratch>/eng/rev12
cp framework/scripts/test_guard_families_rev13.py <scratch>/eng/rev12/framework/scripts/
cd <scratch>/eng/rev12/framework/scripts && python3 test_guard_families_rev13.py
# expect 10 of 13 FAIL; verify the engine first:
#   shasum -a 256 <scratch>/eng/rev12/framework/scripts/guard_policy.py  -> e19e7029927a2748…

# the four enumerated populations (case tables and comparator are SCRATCH EVIDENCE)
#   …/scratchpad/plan-rev13/{drive.py,cmp.py,c_tail_pop.py,c_env2.py,c_pkgattr.py,
#                            c_rtconfig.py,c_debt_writeprims.py}
#   python3 cmp.py c_tail_pop.py      # 714 · comparison by SET subtraction, never counts
# their committed successor is the enumerated family test in the revision-13 suite, which
# drives the same |WRAPPER_TAIL_PROGRAMS| population from the module.

# the committed corpus, and the true revision-12 engine beside it
python3 framework/scripts/hostile_corpus.py --revision main --revision rev11 \
    --revision rev12 --scene-dir <outside scratch>
python3 framework/scripts/hostile_corpus.py --revision rev12 \
    --engine-sha rev12=552065572801d67fb44b2d48efe0d97757d094e3 --scene-dir <outside scratch>

# anchors, BEFORE the battery, against the committed blob
#   …/scratchpad/plan-rev13/anchors.py <worktree> <ref>
# the battery, pinned and printed by the harness itself
python3 framework/scripts/mutate_guard_suite.py
git worktree list | grep mutate      # before reading any census

# the census, and the generation of THIS tree
python3 framework/scripts/guard_revision.py

# lint, the publication gate at the CANDIDATE tip, the release runner, privacy
python3 framework/scripts/legend_lint.py .
python3 scripts/public_release_gate.py
python3 scripts/run_release_regressions.py
python3 scripts/independent_privacy_scan.py

# the fresh clone
git clone --branch plan-runtime-bridge-p00-rev13 <shared checkout> <scratch>/freshclone
```

---
candidate_id: CAND-20260830-RTBRIDGE12
title: A normalisation may add an effect and may never remove one
actor: plan
date: 2026-08-30
parent: CAND-20260830-RTBRIDGE11
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1)
status: FROZEN, awaiting an independent hostile review that has not been opened
---

# `CAND-20260830-RTBRIDGE12`

## 1 · Manifest (Annex D.2)

Every identifier is recorded in **§ 12 only**, derived immediately before the freeze and
nowhere else in this document. Every hash is published with the command that produces it:
**a hash without a reproducible recipe is an attestation, not evidence.**

```text
CANDIDATE_ID      CAND-20260830-RTBRIDGE12
CANDIDATE_BRANCH  plan-runtime-bridge-p00-rev12
BASE_SHA          f3e981675c718d7f43fccee59fbd6ca5002734cb   the revision-11 MANIFEST TIP
MAIN BASELINE     788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5   == development/main
everything else   § 12
```

Revision 11 stays frozen at `f3e9816` as the reviewed record. The one edit this candidate
makes to `CAND-20260830-RTBRIDGE11.md` is the D1 gate repair — a bash double-bracket test
at line 571 parsed as a wikilink and blocked the publication gate — and it is a three-line
change to a fenced example, carried in the inherited checkpoint.

🔴 That sentence is written the long way round on purpose. Spelling the operator out here
reintroduces the defect into the document that reports it: a review of a detector is a
surface the detector scans. The first draft of this line did exactly that, and the check
that found it is the one this candidate is about to run.

### 1.1 · Provenance, and what this session did NOT inherit

Two predecessor sessions were killed by API errors mid-flight. The last thing one of them
reported was:

> Confirmed REV12 regression: 8 of 8 DENY→ALLOW. The version-suffix normalisation opens a
> bypass REV11 closed — `cat2` reaches `RUNTIME_CONFIG`. Fixing it.

**Not one figure in that sentence was carried forward.** The working tree was preserved
first, by named path, as commit `ec931be` — a PRESERVATION and not a freeze — and then
every claim in it was re-derived. The direction was right and the magnitude was wrong by
two orders: the count was a sample, and the repair built from it closed a quarter of the
family. § 3 is that re-derivation.

## 2 · The one sentence

> **A normalisation is evidence about what a name probably means. It may ADD an effect
> this guard would otherwise miss, and it may NEVER remove one it would otherwise
> derive.**

Revision 12's D3 repair collapses a version suffix onto a known program so that
`python3.12 -c "<write>"` reaches the interpreter model that `python3` reaches. The repair
is correct and its application was symmetric, and symmetry is the defect: the same
mapping that adds the interpreter's write derivation also confers the interpreter's
exemptions. That is the whole family, and it has now been opened twice by two different
repairs of it.

## 3 · The regression, RE-DERIVED — and the population was never 8

### 3.1 · Enumerate the population before measuring it

The predecessor probed 8 spellings. The rule ranges over every name any table in
`guard_policy.py` is keyed on, plus every `PROGRAM_ALIASES` key, at every confined scope.
Measured in-process against three engines reconstructed from committed objects, one scene
built by this repository's own `hostile_corpus.Scene` and shared by all columns:

```text
                                              denominator   LOOSENED (DENY -> ALLOW)
rev11 -> rev12 first draft  (e6c3925)          1158 cases            441
rev11 -> rev12 + reader subtraction only       1158 cases            177   🔴 still open
rev11 -> rev12 + reader subtraction only       2946 cases            747   aliases probed
rev11 -> rev12 + the asymmetric rule           2946 cases              6   csh/tcsh only

HARDENED (ALLOW -> DENY) in every column above    0
ERRORS in either column of any pair               0
```

The `1158` denominator is 192 known program names × 3 confined scopes × {suffixed, bare},
plus 6 unmodelled-program controls. The `2946` denominator adds four suffix spellings
(`1`, `2`, `-1`, `3.4`), the 4 alias keys, and 16 realistic versioned spellings —
`python3.12`, `perl5.34`, `node20`, `nodejs`, `pypy3` and their kin — because the first
population could not see the aliases at all.

### 3.2 · Why the first repair closed a quarter of it

`cat2` reached `cat`, a reader, and inherited the reader exemption. The inherited repair
subtracted the readers from the landing set. That is correct and it is **sample-shaped**:
readers are 88 of the 192 names, and the other 104 confer their own exemptions.

```text
LOOSENED after the reader subtraction alone — the 1158-case population
59 distinct spellings, 177 cases, enumerated and not summarised:

  arch1 · aria2c1 · ash1 · bash1 · bsdtar1 · builtin1 · bun1 · bundle1 · busybox1
  caffeinate1 · cargo1 · chroot1 · command1 · composer1 · csh · csh1 · curl1 · dash1
  deno1 · doas1 · env1 · eval1 · exec1 · find1 · fish1 · gem1 · gtar1 · gtimeout1
  http1 · https1 · ionice1 · ksh1 · mksh1 · nice1 · node1 · nohup1 · npm1 · perl1
  php1 · pnpm1 · poetry1 · python1 · python21 · python31 · ruby1 · script1 · setsid1
  sh1 · stdbuf1 · sudo1 · tar1 · tcsh · tcsh1 · time1 · timeout1 · unbuffer1 · uv1
  yarn1 · zsh1

  🔴 `csh` and `tcsh` appear WITHOUT a suffix. They are not normalisation at all — see
     § 6.2 — and their presence in this list is what made the second cause visible.

The 2946-case population adds 4 suffix spellings per name, the alias keys and 16
realistic versioned spellings: 747 cases over 241 distinct spellings. The four ALIAS
keys — `nodejs`, `pypy`, `pypy3`, `python3m` — are in that set and in NEITHER of the
first two, because they are not members of `_KNOWN_PROGRAM_NAMES` and a sweep over that
set alone cannot generate them.
```

Every one of those was `DENY` at revision 11 — through `unclassified`, as an unmodelled
program naming an object in a scope no authority grants — and `ALLOW` after the
normalisation handed it a modelled branch that derives nothing for such an operand.

### 3.3 · The eight the predecessor reported, re-derived

They reproduce, exactly, over a denominator of **13 cases — the 8 plus 5 controls**:

```text
                              rev11              rev12 first draft   rev12 as frozen
file1  @ peer                 DENY CONFINED_PEER      ALLOW  🔴       DENY CONFINED_PEER
file2  @ shared checkout      DENY CONFINED_SHARED    ALLOW  🔴       DENY CONFINED_SHARED
cat2   @ registration         DENY RUNTIME_CONFIG     ALLOW  🔴       DENY RUNTIME_CONFIG
wc1 · tr5 · man9 · test1 · date1  @ peer
                              DENY CONFINED_PEER      ALLOW  🔴       DENY CONFINED_PEER
control  someunknowntool @ peer · shared · registration     DENY -> DENY -> DENY
control  tee @ peer                                         DENY -> DENY -> DENY
control  cat @ peer                                         ALLOW -> ALLOW -> ALLOW
```

The predecessor's count was right about those eight cells. It was a **sample of 441**, and
reporting it as `8 of 8` gave a denominator that made the family look closed by a repair
aimed at it. The reader subtraction closes all 8 of these — and 264 of the 441.

## 4 · The repair

```text
guard_policy.py
  renamed_by_normalisation(token)   did this token reach its table key by being spelled
                                    differently from what ran? basename-keyed, and an
                                    ALIAS counts — `nodejs` is a claim about a NAME, not
                                    evidence about the binary on PATH
  underived_operand(argv, program, findings)
                                    the tail of `unclassified`, extracted and made
                                    IDEMPOTENT so two call sites cannot report one
                                    verdict as two objects
  analyse_argv                      one call site, after the opaque-program check:
                                        if renamed_by_normalisation(argv[0]):
                                            underived_operand(
                                                argv, posixpath.basename(argv[0]), findings)
```

Every branch below that line keeps the **normalised** key, so the whole D3 hardening
survives. What is added is the operand rule the name **as written** would have earned.

🔴 **Keyed on the original basename, not on the normalised program**, and this is not a
detail. `operands()` consults `OPTIONS_WITH_VALUE[program]`, and 22 of the 104 landing
programs have an entry there. Keyed on the normalised name, a path travelling in one of
those flags is skipped as an option-VALUE and stops being a target. Mutant M117 makes
exactly that substitution and **it survived the first version of the suite** — see § 5.3.

The reader subtraction (`VERSIONED_PROGRAM_FAMILIES`) is RETAINED. With the asymmetric
rule in place it is a second line rather than the only one, and the suite asserts it
structurally so that removing it is visible even where the verdict would not move.

### 4.1 · What the repair does NOT cost

Measured, in the same table as the negative, at the frozen tip:

```text
                                                    rev11    rev12
gh repo view "$OWNER/$REPO"                         ALLOW    ALLOW   (PUBLISH_RUNBOOK.md)
printf "%s\n" "$([ 1 = 1 ] && echo "A -> B")"        ALLOW    ALLOW
GIT_PAGER=cat git log --oneline -5                  ALLOW    ALLOW
git config user.name  ·  git remote -v              ALLOW    ALLOW
python3.12 framework/scripts/legend_lint.py .       ALLOW    ALLOW
bash5 scripts/build.sh  ·  node20 build.js          ALLOW    ALLOW
python3.12 -c "print(1)"  ·  perl5.34 --version     ALLOW    ALLOW
cat framework/x  ·  echo x > /tmp/ok.txt            ALLOW    ALLOW
chmod +x /tmp/h/pre-commit                          ALLOW    ALLOW
perl -I <peer>/lib -e "print 1"                     ALLOW    ALLOW
git -C <peer> status                                ALLOW    ALLOW
```

And the hardening it was built for is intact:

```text
python3.12 -c "open('framework/x','w').write('x')"  ALLOW    DENY
python3.12 -m pip install --target framework x      ALLOW    DENY
perl5.34 -e "open(my $f,'>','framework/x')"         ALLOW    DENY
nodejs -e "…writeFileSync('framework/x','x')"       ALLOW    DENY
node20 · pypy3 · bash5 -c 'git add -A'              ALLOW    DENY
python3.12 -c "open('<peer>/x','w').write('x')"     ALLOW    DENY
```

### 4.2 · One new over-refusal, declared

```text
python3.12 -m venv .venv     rev11 ALLOW  ->  rev12 DENY  UNKNOWN_EFFECT
control  python3 -m venv .venv   rev11 DENY  ->  rev12 DENY  UNKNOWN_EFFECT
```

The versioned spelling now inherits the **existing** `python3 -m venv` refusal — one of
the 22 false refusals the documented-command census found, and a shape `README.md:258`
instructs. Revision 12 did not create that refusal; it extended it to a spelling that had
escaped it. Recorded here rather than in the direction of the repair, because a
hardening that lands on documented ordinary work is a cost whichever direction it points.

## 5 · The suite — `framework/scripts/test_guard_families_rev12.py`

### 5.1 · Why it had to exist before this could be frozen

Revision 12 added roughly 704 lines and ten suites reported green. **None of the ten
mentioned `analyse_env_prefix`, `wrapper_tail`, `READER_WRITE_MODEL`, `normalise_program`,
`PURE_READERS`, `EXECUTION_CONTROL_KEY_SUFFIXES` or `PACKAGE_RUN_SUBCOMMANDS`** — measured
by `grep -c` over every `test_*.py` in the repository, which returned 0 for all seven. The
suites passed because not one of them looked at the revision. Two docstrings inside
`guard_policy.py` already asserted what this file "asserts"; the file did not exist.

### 5.2 · What it contains, and it is a DISCRIMINATOR

```text
53 tests, 9 classes, over: analyse_env_prefix · wrapper_tail · PACKAGE_RUN_SUBCOMMANDS
normalise_program · PURE_READERS · READER_WRITE_MODEL · EXECUTION_CONTROL_KEY_SUFFIXES
the marker/partial-program handling · the D5b and D7 cases · and the D3 asymmetry

against REV12's engine, reconstructed from the committed blob     53 tests, 0 failures
against REV11's engine at f3e9816, same blob, suite unchanged     20 failures, 13 errors
```

A suite that passed on both would kill nothing and every mutation aimed at it would be
`EQUIVALENT` without anyone noticing.

The largest test is stated over the **enumeration**, not over the names that failed: every
`_KNOWN_PROGRAM_NAMES` member plus every alias key, three suffix spellings each, three
confined scopes, minus the spellings that are themselves known names — and it asserts the
cell count as its own positive control, so a run that quietly measured nothing is visible.

🔴 **Two of its first-draft tests were wrong, and its own failures said so.** One
generated `python` + `2` = `python2` — a real program — and read the engine's honouring of
it as a bypass. The other asserted `renamed_by_normalisation("cat2")` is `True`; it is
`False`, because the reader subtraction refuses to move `cat2` at all, and a test that
expects one half of a repair to do the other half's work is asserting an implementation it
has not read.

### 5.3 · The positive controls are in the same tables as the negatives

Revision 11's worst self-inflicted defect pointed away from bypasses: its first silence
rule refused `gh repo view "$OWNER/$REPO"`, a command this repository's own
`PUBLISH_RUNBOOK.md` instructs. No test aimed only at bypasses would have caught it. So
every negative table in this suite carries its control:

```text
the enumerated suffix denial          <- the BARE program names, untouched
the alias denial                      <- the alias TARGETS, still normalising
the D3 hardening                      <- ordinary versioned work, still allowed
the option-value keying (§ 4)         <- `perl -I <peer>/lib`, `git -C <peer> status`
the declared shell extension          <- the nine shells that already had the exemption
the execution-control suffix rule     <- user.name, color.ui, push.default, log.date …
the conditional-reader write modes    <- the same programs READING
the unresolved-variable refusal       <- the LITERAL spelling of each shape
```

### 5.4 · Two suite failures repaired, and one of them was not this revision's defect

```text
rc.surface()                    the test called a function runtime_config does not have.
                                The API is rc.resolve(). A test asserting a property of
                                an API nobody had checked was there — the same defect as
                                the docstrings in § 5.1, one level in.

diff.algorithm · merge.conflictstyle   `is_execution_control_key` answers True for both,
                                so `git -c diff.algorithm=histogram log` is DENY. The
                                first draft of the over-refusal control asserted False
                                and FAILED. Measured at revision 11: identical. `diff.`
                                and `merge.` are whole-section PREFIXES that predate this
                                revision; the SUFFIX half — revision 12's addition — is
                                not the cause. Recorded as DECLARED DEBT and asserted
                                `True` on purpose, so a successor who narrows those
                                prefixes fails a test and has to say so.
```

## 6 · Regression against BOTH baselines, by SUBTRACTING FINDING SETS

### 6.1 · The committed corpus

`hostile_corpus.py` now registers `rev12` as an engine and pins `rev11` to `f3e9816` — left
at `HEAD` it would reconstruct THIS engine and label the column `rev11`, and
`REV11 -> REV12 LOOSENED = 0` would be true because both columns were the same object.
Six `AA` cases were added so the family that regressed is inside the committed instrument
rather than only in a session's scratch.

```text
                     denominator          LOOSENED (DENY->ALLOW)   HARDENED (ALLOW->DENY)
MAIN  → REV12        146 corpus cases              0                        96
REV11 → REV12        146 corpus cases              0                         2
REV11 → REV12       2946 sweep cases               6                         0
MAIN  → REV12        —  main carries the LEGACY guard; the sweep is in-process against
                        guard_policy, which main does not have. The corpus is the only
                        instrument that can ask main, and it answers 0.

engine                bypasses of 103 must-refuse   controls   controls wrongly refused
main    788c357               96                       43                 0
rev9    6fb7a83               58                       43                 4
rev10   da0fb72               37                       43                 0
rev11   f3e9816                2                       43                 0
rev12   <content tip>          0                       43                 0

MISRECORDED expectations, every revision                0
SKIPPED · ENGINE ERRORS, every revision                 0 · 0
```

Revision 11's `2` bypasses are the two `AA` rows this candidate added — `AA4` and `AA6`.
That is what adding them was for; a corpus that could not see the regression is not a
baseline for the revision that caused it.

### 6.2 · The one residual loosening, DECLARED — `csh` and `tcsh`

6 cases of 2946, and none of them is normalisation. `csh` and `tcsh` were added to
`SHELL_BINARIES` as a declared list extension. Both counterfactuals were measured, against
engines built from the same tree with only that one line changed:

```text
                              rev11    rev12 as frozen    rev12 with csh/tcsh REMOVED
csh  -c 'git add -A'          ALLOW    DENY BLANKET…      ALLOW   🔴 a closed bypass lost
tcsh -c 'git add -A'          ALLOW    DENY BLANKET…      ALLOW   🔴
csh  <peer>/script            DENY     ALLOW        🔴    DENY
control  bash <peer>/script   ALLOW    ALLOW              ALLOW
control  sh · zsh <peer>/…    ALLOW    ALLOW              ALLOW
```

The exemption `csh` gained is **revision 11's own committed decision**, not a new one:
`guard_policy.SHELL_BINARIES` ends `return  # an interactive shell, or a named script,
carries nothing to police here`, and nine shells already carried it. The extension moves
two names from *unmodelled* into that class.

**This is stated as an OPEN ADJUDICATION, not as a resolved trade.** Both columns are
measured; which one is preferable is a security judgement with an owner, and it is not
this session's to make. Either half moving breaks
`test_the_declared_shell_extension_carries_its_measured_cost`.

## 7 · Declared debt — carried, not closed

```text
D8 · the documented-command census      DECLARED_DEBT. 22 FALSE_REFUSAL of 296 runnable
                                        documented lines; 10 of 10 harness controls
                                        correct. Artefacts are SCRATCH EVIDENCE at
                                        …/scratchpad/d8/, reproducible with
                                        `sh …/scratchpad/d8/run.sh`. Direction confirmed
                                        against Mirror's three named examples, which all
                                        reproduce; the two absolute numbers differ from
                                        Mirror's "23 of 303" and the 7-line denominator
                                        gap and the 23rd refusal are UNATTRIBUTED rather
                                        than guessed. Not extended by this revision.

the unresolved-variable class           PRE-EXISTING, fails in the REFUSING direction.
                                        `git clone … "$dst"` answers
                                        SHELL_WRITE_IN_ASSIGNED_WORKTREE — asserting a
                                        location it cannot derive — while `> "$dst/f"`
                                        answers UNDERIVABLE_TARGET: one situation, two
                                        classifications. Literal `/tmp` equivalents ALLOW
                                        in all three shapes. Measured IDENTICAL at rev11
                                        and rev12, and fenced by class I of the suite so
                                        that a change to it cannot be silent.

diff.* / merge.* prefixes               PRE-EXISTING over-refusal. See § 5.4.

pip install (5 rows) · git worktree add (2 rows)
                                        CARRIED AS FLAGGED, not resolved. `pip install`
                                        is denied UNNAMED_TARGET, defensible for a
                                        security guard and classed FALSE_REFUSAL only
                                        because this repository's own README and skills
                                        instruct it. `git worktree add` genuinely mutates
                                        the shared git common dir and is classed
                                        FALSE_REFUSAL only because
                                        CAND-20260830-RTBRIDGE11.md:948 already declares
                                        that denial a known unrepaired behaviour.

python3.12 -m venv .venv                NEW over-refusal, § 4.2. Inherited from the
                                        unversioned spelling by the normalisation.
```

## 8 · What is NOT claimed

- **No readiness verdict.** None is stated here and none should be read into any number.
- **`NO_KNOWN_STRUCTURAL_BYPASS` is NOT asserted.** `0 bypasses of 103` is a measurement
  over a committed corpus, and a corpus is a sample of a space nobody can enumerate.
- **`R3_REGISTRATION_ANCHORED = NO`.**
- **`LIVE_CODEX_PROBE_MEANINGFUL_NOW = NO`.** No paid or live probe was run.
- **`GUARD_REVISION_UNIFORM = NO`** — the census reads `UNDERIVABLE` across 14 worktrees:
  `{LEGACY: 10, REV11: 2, REV12: 1, UNKNOWN: 1}`. Nothing in a candidate branch can change
  that; only a merge can.
- **No write floor**, for the same reason.
- Nothing was merged, deployed or pushed. No ref left this worktree.

## 9 · Commands, so every number above is re-derivable

```bash
W=<this worktree>; export LEGEND_ASSIGNED_WORKTREE=$W

# the direct suite
python3 framework/scripts/test_guard_families_rev12.py

# the discriminator: REV11's engine from its committed blob, this suite dropped in
for f in guard_policy effect_model repo_topology session_binding runtime_config \
         pre_tool_use_guard; do
  git -C $W show f3e981675c718d7f43fccee59fbd6ca5002734cb:framework/scripts/$f.py \
    > /tmp/rev11tree/framework/scripts/$f.py
done
git -C $W show HEAD:framework/scripts/test_guard_families_rev12.py \
  > /tmp/rev11tree/framework/scripts/test_guard_families_rev12.py
cd /tmp/rev11tree && python3 framework/scripts/test_guard_families_rev12.py

# both baselines, by subtracting observed finding SETS over the committed corpus
python3 framework/scripts/hostile_corpus.py \
  --revision main --revision rev9 --revision rev10 --revision rev11 --revision rev12 \
  --engine-sha rev12=<CONTENT_TIP> --json

# the 2946-case sweep is SCRATCH EVIDENCE, not committed:
#   …/scratchpad/regression/{driver.py,child.py,cases_wide.json}
#   python3 driver.py --cases cases_wide.json --engines rev11 rev12draft rev12final --tag final
# its committed successor is the enumerated test in the suite above, which covers the
# same population at three suffix spellings.

# the census, and the generation of THIS tree
python3 framework/scripts/guard_revision.py --json

# the mutation battery, pinned and printed by the harness itself
python3 framework/scripts/mutate_guard_suite.py

# the publication gate, run at the CANDIDATE tip
python3 scripts/public_release_gate.py
```

## 10 · The minimum relevant existing suites, re-run at this tree

```text
framework/scripts/test_guard_families_rev11.py        42 tests   OK
framework/scripts/test_guard_families_rev12.py        53 tests   OK
framework/scripts/test_confinement_and_delegation.py  96 tests   OK
framework/scripts/test_pre_tool_use_guard.py          47 tests   OK
framework/scripts/test_repo_topology.py               30 tests   OK
framework/scripts/test_runtime_diagnostics.py         66 tests   OK
framework/scripts/test_runtime_parity.py              72 tests   OK
framework/scripts/test_codex_runtime_probe.py         13 tests   OK
scripts/test_guard_bash_command.py                    16 tests   OK
```

🔴 `test_runtime_parity.py` FAILED twice before it passed, and both failures were real:
the new suite carried a shebang and was committed `100644`, and then the index and `HEAD`
disagreed about the mode until it was committed. The second failure is a test that exists
precisely to catch a `git add` that reverts an executable bit.

This is the **minimum relevant** set, not the full historical battery, per the narrowed
scope this pass was given.

## 11 · Mutation

### 11.1 · Anchors checked BEFORE the run, against the committed blob

A mutation left pointing at deleted text reports `ANCHOR_MISSING`, and `ANCHOR_MISSING`
is never a kill — it is a mutant that was never applied. So every anchor was resolved
against `git show <tip>:<path>` before any operator ran, not discovered afterwards:

```text
mutations                                          118
anchors resolving uniquely at 2a2add5              118
ANCHOR_MISSING · ANCHOR_AMBIGUOUS · TARGET_MISSING   0 · 0 · 0
declared EQUIVALENT by the harness                 M07 · M109
```

Revision 12 re-anchored six inherited operators — M09, M28, M99, M100, M105 and the
`unclassified` call site — because its own edits moved the text they named.

### 11.2 · The three operators aimed at THIS revision, and one of them survived

Before this candidate, `test_guard_families_rev12.py` was named by **zero** mutations. 115
operators, and not one pointed at the suite the revision is checked by, so its bite was
entirely unmeasured. Three were added, in a separate `FAMILY_SUITES_12` constant so that
24 unrelated operators do not pay 34 seconds each for a killer they already have.

```text
M115  the asymmetric rule switched off                          KILLED
M116  the reader subtraction removed                            KILLED   🔴 structurally
M117  the added rule keyed on the NORMALISED name               SURVIVED, then KILLED
```

🔴 **M116's kill is structural, and saying so is the point.** With M115's rule in place,
the VERDICT for `cat2 <registration>` does not move when the reader subtraction is
removed — the operand finding fires either way. What kills it is the suite asserting
`normalise_program('cat2') == 'cat2'` and the landing set's disjointness from the readers.
A second line of defence can only be checked structurally, or removing it is invisible.

🔴 **M117 survived, and the first attempt to show it was equivalent was wrong.** The probe
used `python3.12 -c <peer>/x` and measured no difference — because `python3` has no
`OPTIONS_WITH_VALUE` entry, so the mutated branch never fired. 22 of the 104 landing
programs do have one, and there it loosens:

```text
                                       rev11   rev12   rev12 with M117
perl5.34 -I <peer>/lib -e "print 1"    DENY    DENY    ALLOW  🔴
tar1 -C <peer> -tf /tmp/a.tar          DENY    DENY    ALLOW  🔴
curl1 -K <peer>/rc <url>               DENY    DENY    ALLOW  🔴
npm1 --prefix <peer> ls                DENY    DENY    ALLOW  🔴
control  perl -I <peer>/lib            ALLOW   ALLOW   ALLOW
control  git -C <peer> status          ALLOW   ALLOW   ALLOW

5 of 10 probed shapes move -> the mutant is a real behaviour change, NOT equivalent.
```

A survivor has to be chased to an input where the branch actually fires, or an
equivalence claim is a causal story about the code rather than a measurement of it. The
hole was then closed by a test, and M117 is `KILLED` at the frozen tip.

### 11.3 · The full battery

The 118-operator battery is pinned by the harness to **`2a2add5b6fa3e09a5f78612fefa18454391f042b`**,
which is `CONTENT_TIP`. That is one commit earlier than `CANDIDATE_TIP`, and the
difference is exactly the two governance files this candidate adds — neither of which is
the target of any mutation, and neither of which any suite imports.

🔴 A score is fidelity to the code that exists, never coverage. `EQUIVALENT` is its own
category and is never folded into `KILLED`; `ANCHOR_MISSING`, `ANCHOR_AMBIGUOUS` and
`WORKTREE_FAILED` are none of them passes. The run's own output prints the tip it was
pinned to, and that is the value a reader should compare against § 12.

## 12 · The identifiers

Every value below was derived **immediately before the freeze**, by the command printed
beside it, and from no earlier draft.

```text
CANDIDATE_ID      CAND-20260830-RTBRIDGE12
CANDIDATE_BRANCH  plan-runtime-bridge-p00-rev12
BASE_SHA          f3e981675c718d7f43fccee59fbd6ca5002734cb   the revision-11 MANIFEST TIP
CONTENT_TIP       2a2add5b6fa3e09a5f78612fefa18454391f042b
CONTENT_HASH      62ec0b2b5a7c94f74aff964a06d7a4096784c395dc02ba8ed192d7cb89eddc8d
GUARD_GENERATION  REV12
POLICY_HASH       e19e7029927a2748     framework/scripts/guard_policy.py
                  e19e7029927a2748ec1e7bd0959b8296584397be2b25abc081572fac9892f8f3  (full)
ENTRY_HASH        2467f4be9cc6fb37     scripts/guard_bash_command.py
MAIN BASELINE     788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5   == development/main

CANDIDATE_TIP     A manifest cannot contain the hash of the commit that carries it, so it
                  is stated as a RULE:
                      git -C <worktree> rev-parse plan-runtime-bridge-p00-rev12
                  It differs from CONTENT_TIP by exactly the two governance files this
                  candidate adds, and § 12.2 measures — rather than argues — that the
                  content hash is invariant across that difference.
```

```bash
# CONTENT_HASH — the recipe, not the number
python3 governance/scripts/candidate_content_hash.py \
  --base f3e981675c718d7f43fccee59fbd6ca5002734cb \
  --tip  2a2add5b6fa3e09a5f78612fefa18454391f042b

# GUARD_GENERATION, POLICY_HASH, ENTRY_HASH — read from the SHAPE of what is installed
python3 framework/scripts/guard_revision.py --json

# POLICY_HASH from the committed blob rather than from disk
git -C <worktree> show <CONTENT_TIP>:framework/scripts/guard_policy.py | shasum -a 256
```

### 12.1 · The census is a function of WHO IS RUNNING, and this was measured

```text
with no mutation harness running   14 worktrees  {LEGACY 10, REV11 2, REV12 1, UNKNOWN 1}
with the harness mid-run           15 worktrees  {LEGACY 10, REV11 2, REV12 2, UNKNOWN 1}
```

🔴 The second reading is not wrong — the harness's detached worktree really does carry
this engine while it exists — and it is not stable either. `mutate_guard_suite.py` adds
and removes a worktree per operator, so any census taken during a run describes a
population that has already changed. The value recorded in § 8 is the quiescent one, taken
with no `mutate-*` worktree held, and the check is `git worktree list | grep mutate`
before reading the census rather than after doubting it.

`GUARD_REVISION_UNIFORM` reads `UNDERIVABLE` in both, so the fence does not move either
way.

### 12.2 · `CONTENT_TIP` ≠ `CANDIDATE_TIP`, and the hash must be invariant

Structurally, `governance/candidates/` is a declared `CONTROL_PLANE_ROOT` and the domain
filter is a prefix match, so the two governance files this candidate adds are outside the
hashed domain. **A structural argument is not a measurement**, and revision 11 recorded
the same property having been measured on two candidates rather than argued on one. The
claim here is therefore stated so that one command falsifies it:

```text
hash at CONTENT_TIP    2a2add5   62ec0b2b5a7c94f74aff964a06d7a4096784c395dc02ba8ed192d7cb89eddc8d
hash at CANDIDATE_TIP  <tip>     MUST equal the value above
git -C <worktree> diff --name-only 2a2add5 <CANDIDATE_TIP>
  governance/candidates/CAND-20260830-RTBRIDGE12.md
  governance/candidates/HANDOFF-20260830-RTBRIDGE12-MIRROR.md
```

```bash
python3 governance/scripts/candidate_content_hash.py \
  --base f3e981675c718d7f43fccee59fbd6ca5002734cb \
  --tip  $(git -C <worktree> rev-parse plan-runtime-bridge-p00-rev12)
```

If that value is not `62ec0b2b…`, or the diff names any third path, **the freeze is void**
and this section is the finding — not a formatting slip to be corrected in place.

### 12.3 · Hygiene at the frozen tip

Measured with `git -C <worktree>` and absolute paths throughout; a bare `git status`
measures where the process is standing, not the object, and this session's Bash working
directory does not persist between calls.

```text
branch                                             plan-runtime-bridge-p00-rev12
tracked paths dirty, before the freeze commit      0
untracked paths, before the freeze commit          2   the two files below, and no others
                                                       governance/candidates/CAND-20260830-RTBRIDGE12.md
                                                       governance/candidates/HANDOFF-20260830-RTBRIDGE12-MIRROR.md
committed 100755 whose filesystem mode is not 755  0
index-vs-HEAD mode disagreements                   0
POSITIVE CONTROL — committed-100755 files walked   149

shebang files committed 100644                     3
  governance/scripts/candidate_content_hash.py
  governance/scripts/governance_fingerprint.py
  governance/scripts/test_candidate_content_hash.py
```

🔴 Those three are **PRE-EXISTING and outside `test_runtime_parity.py`'s population**,
which is the runtime bridge's own `OWNED` file list. They are `100644` at `BASE_SHA` and
on `main` — verified with `git ls-tree` at both — so this candidate neither caused them
nor is the place to repair them. They are reported because the sweep here walked every
tracked `.py`/`.sh`, a WIDER population than the parity test's, and a negative is worth
only its denominator: *0 offenders in the bridge's own files, 3 in the repository.*

Revision 12's own file was one of these until it was caught: `test_guard_families_rev12.py`
carried a shebang and was committed `100644`, and `test_runtime_parity.py` failed on it
twice — once for the committed mode, and once because the index and `HEAD` then disagreed.
Both failures were the tests doing exactly what they exist for.

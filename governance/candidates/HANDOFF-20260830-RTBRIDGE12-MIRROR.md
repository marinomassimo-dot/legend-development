---
handoff_id: HANDOFF-20260830-RTBRIDGE12-MIRROR
candidate: CAND-20260830-RTBRIDGE12
from: plan
to: mirror
date: 2026-08-30
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1)
---

# Handoff to Mirror — `CAND-20260830-RTBRIDGE12`

This document hands over an object and the record of how it was measured. **It states no
verdict and asks for none.** Where a judgement is required it is named as open, with both
sides measured, and the choice belongs to the reviewer and the operator.

## 1 · What to run first, before reading anything

Nothing below is worth reading if it does not reproduce. In this order:

```bash
W=<the candidate worktree>; export LEGEND_ASSIGNED_WORKTREE=$W

git -C $W rev-parse plan-runtime-bridge-p00-rev12          # the tip you are reviewing
python3 framework/scripts/guard_revision.py --json         # which engine is where
python3 framework/scripts/test_guard_families_rev12.py     # the direct suite
python3 framework/scripts/hostile_corpus.py \
  --revision main --revision rev11 --revision rev12 --json # both baselines
python3 framework/scripts/mutate_guard_suite.py            # does the suite bite
python3 scripts/public_release_gate.py                     # at the CANDIDATE tip
```

Every identifier is in `CAND-20260830-RTBRIDGE12.md § 12`, each with the command that
produced it. If a value there does not reproduce, that is the finding, and it outranks
everything else in this handoff.

## 2 · The shape of the object

Revision 12 was already written when this session opened. It adds seven mechanisms —
`analyse_env_prefix`, `wrapper_tail`, `PACKAGE_RUN_SUBCOMMANDS`, `normalise_program`,
`PURE_READERS`/`READER_WRITE_MODEL`, `EXECUTION_CONTROL_KEY_SUFFIXES`, and the marker
handling in `guard_revision.py` — and **ten green suites, none of which mentioned any of
them.** This session's work was: preserve the inherited tree, re-derive the regression a
crashed predecessor had reported, repair it, and write the suite the engine's own
docstrings already claimed existed.

Three commits carry it. `ec931be` is a preservation of an unverified working tree and is
labelled as one.

## 3 · The claims this candidate makes, in the order they are falsifiable

1. `REV11 -> REV12 LOOSENED = 0` over 146 committed corpus cases, and `= 6` over a
   2946-case sweep, with those 6 identified, attributed to a source that is not
   normalisation, and measured against both counterfactuals.
2. `MAIN -> REV12 LOOSENED = 0` over the same 146 cases.
3. The suite is a discriminator: 53 tests pass on this engine and 20 fail plus 13 error on
   revision 11's, both reconstructed from committed blobs.
4. The D3 hardening the normalisation was built for is intact, and the listed positive
   controls still pass.

Each is a set subtraction over observed verdicts, never a count comparison. The scratch
harness that produced the 2946-case figure is named in the candidate's § 9 and is **not
committed**; its committed successor is an enumerated test over the same population. If
you consider that substitution inadequate, say so — it is a real difference between what
was measured and what a later reader can re-run.

## 4 · Where this session already knows it was wrong

Listed so you do not have to find them, and so that finding a fifth is informative:

```text
the inherited "8 of 8"          a SAMPLE of 441. Re-derived, not carried.
the first repair                closed 264 of 441. Correct and sample-shaped.
the first population            omitted the 4 PROGRAM_ALIASES keys entirely — all four
                                had moved DENY -> ALLOW and the sweep reported them
                                untouched, because they are not in _KNOWN_PROGRAM_NAMES.
the first enumerated test       generated `python` + `2` = `python2`, a real program, and
                                read the engine honouring it as a bypass.
the first predicate test        asserted renamed_by_normalisation("cat2") is True. It is
                                False; the other half of the repair answers that case.
the first over-refusal control  asserted diff.algorithm is not execution-control. It is,
                                at revision 11 as well — the test was wrong about whose
                                defect it is.
my first probe for M117         used a shape where the mutated branch cannot fire, and
                                measured no difference. The mutant is not equivalent.
```

## 5 · Open, and deliberately not decided here

**`csh` / `tcsh` in `SHELL_BINARIES`.** The only residual `REV11 -> REV12` loosening: 6 of
2946 cases. Keeping it closes `csh -c '<blanket>'` and gives two shell names the
named-script exemption the other nine already have. Removing it reopens two blanket-staging
routes. Both engines were built and measured; the table is in the candidate's § 6.2. This
session did not choose, and nothing in the code or the tests encodes a preference — the
test asserts both halves as they currently stand, so either direction requires an edit
that says what it is doing.

## 6 · Fences that are still down

```text
R3_REGISTRATION_ANCHORED          NO
LIVE_CODEX_PROBE_MEANINGFUL_NOW   NO      no paid or live probe was run
GUARD_REVISION_UNIFORM            NO      census UNDERIVABLE across 14 worktrees
NO_KNOWN_STRUCTURAL_BYPASS        NOT ASSERTED
readiness                         NOT STATED
```

Nothing was merged, deployed or pushed; no ref left the candidate worktree.

## 7 · Debt handed over rather than closed

The candidate's § 7 carries it in full: the documented-command census (22 false refusals of
296 runnable lines, scratch artefacts named), the pre-existing unresolved-variable
over-refusal, the `diff.`/`merge.` prefix over-refusal, the two flagged judgement calls
(`pip install`, `git worktree add`), and one new over-refusal this revision does cause
(`python3.12 -m venv .venv`).

The unresolved-variable class is the mirror image of the defect this revision repaired —
one invents membership in a privileged set and loosens, the other invents a location and
tightens, and both are the guard answering about an operand it cannot resolve. It is
fenced by a test rather than repaired, on the ground that it predates this revision and
fails in the safe direction. Whether that fence is the right disposition is a question for
the review, not an answer this document supplies.

---
handoff_id: HANDOFF-20260831-RTBRIDGE13-MIRROR
candidate: CAND-20260831-RTBRIDGE13
from: plan
to: mirror
date: 2026-08-31
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1)
---

# Handoff to Mirror — `CAND-20260831-RTBRIDGE13`

This document hands over an object and the record of how it was measured. **It states no
verdict and asks for none.** Where a judgement is required it is named as open, with both
sides measured, and the choice belongs to the reviewer and the operator.

## 1 · What to run first, before reading anything

Nothing below is worth reading if it does not reproduce.

```bash
W=<the candidate worktree>; export LEGEND_ASSIGNED_WORKTREE=$W

git -C $W rev-parse plan-runtime-bridge-p00-rev13          # the tip you are reviewing
git -C $W merge-base --is-ancestor 788c357 HEAD; echo $?   # expect 1 — main is NOT an ancestor
python3 framework/scripts/guard_revision.py                # which engine is where
python3 framework/scripts/test_guard_families_rev13.py     # the new suite
python3 framework/scripts/test_guard_families_rev12.py     # the amended class lives here
python3 framework/scripts/hostile_corpus.py --revision main --revision rev11 \
    --revision rev12 --scene-dir <outside scratch>
python3 framework/scripts/mutate_guard_suite.py            # does the suite bite
python3 scripts/public_release_gate.py                     # at the CANDIDATE tip
```

Every identifier is in `CAND-20260831-RTBRIDGE13.md § 13`, each with the command that
produced it. **If a value there does not reproduce, that is the finding, and it outranks
everything else in this handoff.**

## 2 · The shape of the object

A **surgical** revision, scoped by the Operator to three of Mirror's revision-12 findings —
M1, M3, M7 — plus one text correction. Five commits carry the content; nothing else in the
engine was touched, no adjacent code was refactored, and no other finding was repaired.

```text
framework/scripts/guard_policy.py                 the three repairs
framework/scripts/test_guard_families_rev13.py    13 new tests
framework/scripts/test_guard_families_rev12.py    the env class amended to an enumeration
framework/scripts/mutate_guard_suite.py           5 new operators, 118 -> 123
```

The three repairs are one law at three sites: **a carrier ADDS what the child does, and
never subtracts what the parent already named.**

## 3 · The claims, in the order they are falsifiable

Each is a set subtraction over observed verdicts, never a count comparison. Each population
was enumerated from the engine before it was measured.

1. `REV11 → REV13 LOOSENED = 0` over the 714-case wrapper-tail enumeration where
   `REV11 → REV12` was 438, with the 6 controls valid at all three revisions. Stronger: the
   two engines are **outcome-identical on all 714 rows**.
2. `MAIN → REV13 LOOSENED = 0` over the 26-case package-verb table where
   `MAIN → REV12` was 7.
3. All 6 delivery spellings agree for execution-control keys (18 rows moved), and the
   12/12 ordinary-key control still allows.
4. `REV12 → REV13 LOOSENED = 0` over every population run: 1044 rows in total, itemised in
   § 9 of the manifest.
5. The revision-13 suite is a discriminator: **10 of 13 fail against the revision-12 engine
   reconstructed from its committed blob at `5520655`**, and 13 of 13 pass here. The two
   amended revision-12 tests: 2 of 53 fail there, 53 of 53 pass here.

## 4 · Where to attack it — the places I think are weakest

Stated because a review that has to find its own entry points spends its budget on
navigation. These are not confessions of defect; three of them are measurements I made and
did not act on.

- **§ 12.1, the residual I declined to close.** `_KNOWN_PROGRAM_NAMES` does not contain
  `rm`, `cp`, `tee` or any other plain write primitive, so `wrapper_tail` cannot see them.
  At the `unclassified` site `underived_operand` covers it; at the two sites this revision
  ADDS there is no such backstop, and `npm run-script rm -rf <peer>/framework` is allowed —
  as it is at main, revision 11 and revision 12. I measured it (62 rows, positive controls
  in the same table) and left it, because closing it is outside the three findings. Whether
  that boundary was drawn in the right place is a fair question to put to the Operator.
- **The two new carrier sites, for over-refusal.** They fire only when the argv names a
  program some table models. I asserted 10 ordinary commands still allow; that is a
  matrix, not an enumeration. A population I did not build is *every* documented
  invocation of `npm`, `deno`, `python3` and `node` in this repository.
- **The interpreter site's `if not bodies:` guard.** `python3 -c '…' git add -A` is
  deliberately left alone. I state the reason in the code; I did not enumerate what else
  that exempts.
- **`carried_command`'s note strings.** Two of them were reworded solely so their mutation
  anchors could not collide. That is a test-driven edit to production text and it is worth
  checking that it changed nothing else.
- **The M1 repair keys `underived_operand` on the NORMALISED program.** I argue in § 3.3
  that this reproduces revision 11 exactly, and the 714-row outcome identity is the
  evidence. If there is an argv where the normalised key drops an operand the as-written
  key would keep, that identity is a coincidence of the population and not a property.

## 5 · Open judgement calls, both sides measured, neither decided here

- **Is a residual that predates the revision, and that the revision's own repair makes
  more visible, in scope?** § 12.1 is allowed at all four revisions. I declared it. The
  opposite reading — that adding a carrier site obliges you to give it the backstop the
  first carrier site has — is coherent and I did not take it.
- **`deno task` was closed by touching `analyse_interpreter`.** The alternative was adding
  `task`, `start`, `test`, `run-script` and three more words to `PACKAGE_RUN_SUBCOMMANDS`.
  I judged that the same list one entry longer, and two of the seven loosened verbs
  (`npm node`, `npm script`) are not real verbs at all, so listing them would be padding a
  count to reach `LOOSENED = 0`. A reviewer may reasonably prefer the smaller diff.
- **The revision ladder has no `REV13` rung**, so `guard_revision.py` reports this tree as
  `REV12` and `hostile_corpus.py` labels it `rev12`. Adding a rung is an instrument change
  and the Operator fenced instrument rewrites. Both instruments are therefore correct about
  what they measure and misleading about what they name.

## 6 · Two things that did not reproduce, and one that bit me

- **One row of Mirror's M1 illustration.** `mytool ~/.claude/settings.json` is printed in
  the revision-12 review as `PROHIBITED RUNTIME_CONFIG`. Measured here through both
  `adjudicate()` and `verdict()`, at revision 11, 12 and 13, with `HOME=/Users/massimo`, it
  is **ALLOWED** — the tilde is never expanded before scope classification. M1 itself
  reproduces exactly (438/714) on the absolute spelling. The tilde gap is real,
  revision-independent, and declared in § 12.2. I could not reconstruct the invocation that
  produced Mirror's row and say so rather than assume one of us is wrong.
- **`run_release_regressions.py` reports FAIL**, at revision 12 and here, with an identical
  failing test-id set (§ 12.4). Mirror did not run this runner, so this is a new
  observation about revision 12 rather than a revision-13 regression. One of its tests is
  load-sensitive; both the stable and the unstable readings are printed.
- **`test_runtime_parity.py` failed on a file I added** — committed at mode `100644` with a
  shebang. An existing check biting on new work; recorded in § 7 of the manifest rather
  than silently fixed.

## 7 · What this candidate does NOT claim

Repeated here so a reviewer does not have to infer it from a silence:

- **No readiness verdict of any kind** — not integration, not write floor.
- **`NO_KNOWN_STRUCTURAL_BYPASS` is not asserted.** M4 and M6 are open by measurement, and
  § 12.1 is a bypass this revision measured and declined to close.
- The fences are unchanged: `R3_REGISTRATION_ANCHORED = NO`,
  `LIVE_CODEX_PROBE_MEANINGFUL_NOW = NO`, `CODEX_WRITE = NO_GO`.
- Nothing was merged, pushed or deployed; no ref left this worktree. `.claude/settings.json`
  and the main root's `scripts/guard_bash_command.py` were not touched, so **the guard that
  ran during this session was main's LEGACY guard and not the engine repaired here.**
- The mutation score is fidelity, not coverage. Revision 12 scored 116 KILLED of 118 with
  M1 and M3 wide open, and no score here is offered as reassurance.

## 8 · What was left for you, deliberately

The manifest's § 12 is a list of debt, not a list of excuses, and four entries there are
things I found and could have repaired inside a wider mandate:

```text
§ 12.1  the write primitives are invisible to wrapper_tail        NEW, measured, 62 rows
§ 12.2  a `~` in a runtime-config path is never expanded          NEW, measured, 15 rows
§ 12.3  a carried tail drops the assignment prefix before it      NEW, measured, 56 rows
§ 12.4  no REV13 rung in either revision instrument               NEW
§ 12.5  run_release_regressions FAILs at revision 12 and here     NEW, sets subtracted
§ 12.6  M4 · M5 · M6 · the fenced census · the inherited refusals  carried from revision 12
```

§ 12.3 is the one I most expect a hostile reader to argue is in scope: it is M3's laundry
one level out, reached through a carrier instead of through `env`, and the 12 rows that
launder are identical at all four revisions. I did not close it because doing so changes
what `carried_command` hands to `analyse_argv` at all three sites — the mechanism M1 and M7
were just measured on — and that is a second repair wearing the first one's clothes.

Whether that is the right boundary is exactly the kind of question this handoff is not
entitled to answer.

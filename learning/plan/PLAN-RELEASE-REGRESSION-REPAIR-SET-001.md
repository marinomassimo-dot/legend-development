---
record_type: WORK_ANALYSIS
id: PLAN-RELEASE-REGRESSION-REPAIR-SET-001
title: Every red release surface, its introducing commit — and three branches that each fix what another breaks
date: 2026-08-26
role: PRODUCER
mode: ANALYSIS_FIRST / MINIMAL_DELTA
authority: Plan role contract — candidate preparation on own branch. No foreign file committed
  to any canonical surface. No policy amended.
status: ANALYSIS_COMPLETE — CAND-20260826-RELSURF prepared; four surfaces routed as a normative
  decision rather than repaired
---

# RELEASE REGRESSION REPAIR SET, AND THE GOVERNANCE TOOL TESTS

> **Nothing here is medical advice.** Release infrastructure only.

---

## 1 · The measurement, on clean checkouts, not inherited

`python3 scripts/run_release_regressions.py`, run to completion on three separate worktrees.

| Red surface | `main` | `plan-exec-repair-prep` | this branch | `plan-release-surface-repair` |
|---|:--:|:--:|:--:|:--:|
| `test_locator_obligation_reaches_every_route` | 🔴 | 🔴 | 🔴 | 🔴 |
| `test_abstract_corpus_is_not_evidence` | 🔴 | 🔴 | 🔴 | 🔴 |
| `test_fulltext_trace_contract` | 🔴 | 🔴 | 🔴 | 🔴 |
| `test_session_self_eval` | 🔴 | 🔴 | 🔴 | 🔴 |
| `test_release_surface` (executable bits) | 🔴 | ✅ | 🔴 | ✅ |
| `test_release_runner_verdict` (unrun suite) | 🔴 | ✅ | ✅ | ✅ |
| `test_documented_commands` | ✅ | 🔴 | ✅ | ✅ |
| `test_fresh_clone_reader_journey` | ✅ | 🔴 | ✅ | ✅ |
| **total** | **6** | **6** | **5** | **4** |

🔴 **No ref carries all the repairs, and two of them each reintroduce what another fixed.**
`plan-exec-repair-prep` fixes the executable bits and the unrun suite, and is red on the two
document guards because it predates the editorial repair. This branch fixes the document guards
and the unrun suite, and is red on the executable bits. **The union of the four columns is a green
battery except for the first four rows, and the union exists nowhere.**

That is the finding, not a bookkeeping note: **each branch's total is 6, 6, 5, 4 — and reading any
one of them as "the state of the repository" gives a different answer to the same question.**

---

## 2 · The repair set, one row per surface

### 2.1 · Rows 1–4 — the CLAUDE.md router class

| | |
|---|---|
| **ROOT_CAUSE** | Four suites assert that specific rule text is present **in `CLAUDE.md`**. On 2026-08-16 CLAUDE.md became a router whose opening line is *"Every operating rule lives in a named normative file and is reproduced nowhere else."* **The guards require exactly what the document now forbids itself to do.** |
| **INTRODUCING_COMMIT** | `04cbd3b` (2026-08-16) — *"CLAUDE.md becomes a router, after every rule in it was given a canonical home"*. Verified with a before/after control: all four strings present at `04cbd3b~1`, absent at `04cbd3b`; **all four suites exit 0 at `04cbd3b~1` and exit 1 at `04cbd3b`**. All four suites already existed before the migration. Positive control on the same run: `BATCH_COMMIT` went 13 → 1 and did not vanish, so the sweep was not simply reporting an empty file. |
| **OWNER** | whoever owns the release battery, jointly with whoever owns the router principle. Not Plan alone. |
| **MINIMUM_REPAIR** | **Teach each guard to accept a pointer.** CLAUDE.md already links `framework/instruction/LEGEND_CORE.md` and `framework/master/gold_is_in_the_details.md`, which is where three of the four rules now live. The guard should follow the link rather than grep the router. |
| **NEGATIVE_TEST** | remove the pointer from CLAUDE.md **and** the rule from its normative home → the guard must still fail. Otherwise the repair has only widened the hole. |
| **MUTATION_TEST** | delete the rule text from the normative home while leaving the pointer → must fail. Delete the pointer while leaving the rule → must fail. **Both arms, or a pointer-following guard degenerates into a link check.** |
| **CAN_FIX_WITHOUT_POLICY_CHANGE** | 🔴 **NO.** |

**Why not, stated precisely.** The two available repairs are (a) re-state the rules in CLAUDE.md,
which reverses the migration `04cbd3b` performed deliberately; or (b) change what the guards
consider a satisfied obligation, which redefines a `BLOCK`-severity property. **Either is a policy
act.** Plan does not choose between them inside a work record.

**And one of the four is worse than the other three.** `test_abstract_corpus_is_not_evidence`
requires `pubmed_corpus_harvest` in **both** `CLAUDE.md` and `AGENTS.md`. `AGENTS.md` still carries
it. **`pubmed_corpus_harvest` appears in no normative file on `main` at all** — not in
`framework/instruction/`, not in `framework/master/`, not in `framework/protocols/` — and the
migration map records no home for it. For the other three the rule moved; **for this one there is
no canonical home to point at**, so "follow the pointer" has nowhere to go. The migration map
mentions `session_self_evaluation` once and the other three zero times.

⇒ **Route as a normative decision boundary, with the abstract-corpus row flagged as possibly a
lost rule rather than a relocated one.** That distinction is not adjudicated here.

### 2.2 · Row 5 — executable bits

| | |
|---|---|
| **ROOT_CAUSE** | `test_release_surface.test_shebang_python_entrypoints_are_executable` requires every tracked `.py` beginning `#!` to be mode `100755`. Four are `100644`: `framework/scripts/lease_state.py`, `governance/scripts/candidate_content_hash.py`, `governance/scripts/governance_fingerprint.py`, `governance/scripts/test_candidate_content_hash.py`. |
| **INTRODUCING_COMMIT** | four separate additions — `9720a0c` and `36305c6` (2026-08-16), `b2c326b` (2026-08-17), `325da04` (2026-08-18). The guard predates all four: it is in `a2e0dd0`, 2026-07-26. **Nobody ran the battery after adding a script, four times running.** |
| **OWNER** | Plan for the three under `governance/`; the guard's owner for the check. `lease_state.py` sits in `framework/scripts/`. |
| **MINIMUM_REPAIR** | `chmod +x` on the four. Nothing else. |
| **NEGATIVE_TEST** | `chmod -x` any one → the guard must name that file. |
| **MUTATION_TEST** | run at `main` (**exit 1**, four files named) and at the candidate tip (**exit 0**). Both measured. |
| **CAN_FIX_WITHOUT_POLICY_CHANGE** | ✅ **yes** — it changes a file mode and no text. |

### 2.3 · Row 6 — the unexecuted test suite

| | |
|---|---|
| **ROOT_CAUSE** | `governance/scripts/test_candidate_content_hash.py` is tracked on `main` and absent from `TESTS` in `scripts/run_release_regressions.py`. `test_release_runner_verdict.test_every_tracked_test_file_is_in_the_runner` exists precisely to catch this and **has been red on `main` ever since**. |
| **INTRODUCING_COMMIT** | the suite arrives at `b2c326b` (2026-08-17); the check that demands its registration is older, `6a2efc6` (2026-08-10). The registration line exists at `c964324` — **on this branch and `plan-exec-repair-prep`, and on `main` it does not.** |
| **OWNER** | the runner's owner. |
| **MINIMUM_REPAIR** | one inventory line. |
| **NEGATIVE_TEST** | add a tracked `test_*.py` without registering it → the guard must name it. **Observed live**: adding `test_regenerate_adjudications_fails_closed.py` to the adjudication candidate made this guard demand its registration before anything else was run. The guard works. |
| **MUTATION_TEST** | `main` exit 1 → candidate exit 0, measured. |
| **CAN_FIX_WITHOUT_POLICY_CHANGE** | ✅ **yes.** |

### 2.4 · Rows 7–8 — the document guards, and the population question

| | |
|---|---|
| **ROOT_CAUSE** | `test_documented_commands` and `test_fresh_clone_reader_journey` read **raw bytes** and cannot distinguish *documenting a path* from *reporting that a path is missing*. Tracking a Plan record that reports `pathograph.py` absent from every ref made both guards demand that it exist. |
| **INTRODUCING_COMMIT** | `43cf690` / `702df73` (2026-08-25), which tracked twelve Plan records. Repaired at the text layer by `7a0d48e` (2026-08-26, this session). |
| **OWNER** | Plan owns the records; the guards' owner owns the class. |
| **MINIMUM_REPAIR** | **done** for the instances — paths written as filename plus directory. **Not done** for the class: code-span stripping in the extractor, which changes what a `BLOCK`-severity gate blocks on. |
| **NEGATIVE_TEST** | plant a genuinely broken path → both guards must fire. **Run: they do.** |
| **MUTATION_TEST** | measured before/after on clean extractions; the full runner shows the same six failures as the pre-commit baseline and no seventh. |
| **CAN_FIX_WITHOUT_POLICY_CHANGE** | instance: ✅. **Class: ❌ — GATE 3.** |

### 2.5 · The dot-slash reference problem — not a red surface on `main`, and it reproduced here

Measured first, with the guard that would catch it:

| Where | `test_documented_commands` |
|---|---|
| clean `main` checkout | **exit 0** |
| this worktree | **exit 0** |

No tracked file of that name exists on `main`. The dot-slash form **does** exist — two documents,
`dismech_phase3_dryrun_result.md` and `dismech_sidecar_phase2.md`, both in
`disease-models/wwox/analysis/`, carry links to scripts in the `scripts/` directory beside them,
written with a leading dot-slash — and every one **resolves**, because `resolve_reference()`
resolves that form against the **document's own** directory and the targets sit next to it.

🔴 **And then this record reproduced the defect while describing it.** The paragraph above
originally quoted one of those links verbatim. `test_documented_commands` and
`test_fresh_clone_reader_journey` both went red, naming two references in **this file**: the
quoted example, and the illustrative name in this section's own heading. Both had resolved
correctly in `disease-models/wwox/analysis/`; quoted from `learning/plan/`, the same characters
resolved to `learning/plan/scripts/…` and to `learning/plan/file.py`, **neither of which exists.**

⇒ **The fragility is not latent. It is demonstrated, by the section asserting it, in one move.**
A dot-slash reference is not a reference to a file; it is a reference to *wherever the reader
happens to be standing*, and copying the text moves the target without moving a character of it.
The form is now described rather than written, which is also why the heading no longer contains it.

⇒ **Repair: repository-local references are written from the repository root, never dot-slash
relative.** That is a convention, not a policy change, and it costs nothing — but it belongs in the
guard, because the guard is what would otherwise keep finding it one document at a time. **The two
documents on `main` are correct where they sit and become wrong the moment anything quotes them**,
which is the argument for the rule and is not an argument for editing them today.

---

## 3 · Repository population vs disk population — measured, not argued

`test_documented_commands` and its neighbours scan `ROOT.rglob("*.md")` — **the disk**, not the
index.

| Working directory | markdown on disk | markdown tracked | delta |
|---|:--:|:--:|:--:|
| clean `main` checkout | 281 | 281 | **0** |
| this worktree | **328** | 326 | **2** |

The two extra are `staging/commit_candidate_20260810_claim004_review.md` and
`…claim011_review.md` — **gitignored**, so `git ls-files --others --exclude-standard` reports
zero and they are invisible to the ordinary "untracked?" question.

🔴 **The asymmetry runs both ways and neither direction is detectable from inside a single run.**
A local run can go red on a file that exists in no clone; a CI run can go green while a file on the
operator's disk is broken. **And the delta is a property of the working directory, not of the
repository** — the same commit measured in two places gives 0 and 2.

---

## 4 · Phase 5 — the governance tool tests

### 4.1 · They exist, they are green, and their arms kill

| Suite | Tests | Result |
|---|:--:|---|
| `test_lease_state.py`, in `framework/scripts/` | 22 | **OK** |
| `governance/scripts/test_governance_fingerprint.py` | 27 | **OK** |

✎ **Written that way because writing it the other way broke two guards, in this record, one
section above where the class is described.** The first draft named the suite as one slash-joined
path under `framework/`, which is a `REPO_PREFIXES` root, so `test_documented_commands` and
`test_fresh_clone_reader_journey` both went red — on a record whose § 2.4 explains that those two
guards cannot tell *documenting a path* from *reporting that a path is absent*. The suite exists on
`plan-exec-repair-prep` and on no other ref, which is § 4.2's whole point, and **naming it is what
the guards forbid.** `governance/` is not a scanned prefix, so its neighbour on the row above needs
no such treatment — the asymmetry is in the guard, not in the two files.

Mutation battery, run against a copy, baseline asserted green **before any arm** so that a red arm
means something:

| Arm | Verdict |
|---|---|
| lease: expiry no longer terminal — every unreleased lease derives ACTIVE | **CAUGHT** |
| lease: `RELEASED_AT` stops winning over the clock | **CAUGHT** |
| lease: a record with neither timestamp is guessed instead of refused | **CAUGHT** |
| lease: the singleton invariant stops being checked | **CAUGHT** |
| fingerprint: composition stops being order-independent | **CAUGHT** |
| fingerprint: CORE need not include the actor's own contract | **CAUGHT** |
| fingerprint: an unparseable § P2.2 falls back instead of raising | **CAUGHT** |
| fingerprint: an unknown role is accepted instead of refused | **CAUGHT** |

**8 caught · 0 survived · 0 stale anchors.** A stale anchor is counted separately and never as a
catch: a mutation that did not apply tested nothing.

### 4.2 · 🔴 The gap is not coverage, and calling it a coverage gap would be wrong

Both suites are **registered in `TESTS`** on `plan-exec-repair-prep`, where
`test_release_runner_verdict` is green.

**They exist on that ref and on no other.** One of 51. That branch is **65 commits ahead of `main`
and 2 behind**, and nothing merges from it.

| Question | Answer |
|---|---|
| Do the tests exist? | yes |
| Do they pass? | yes, 49 of 49 |
| Do they kill wrong behaviour? | yes, 8 of 8 arms |
| Is the runner registration written? | yes |
| Does anything on `main` run them? | **no — neither the tests nor the registration is on `main`** |

⇒ **Classified as a `DURABILITY_GAP`, not an `EXECUTABLE_GAP`.** The distinction decides the
repair: an executable gap is closed by writing a test, and this one is closed by **moving work that
already exists onto a ref that is read**. The measured facts and their measured absence from `main`
are the whole of it.

**And `lease_state.py` is tracked on `main` and on 27 of 47 local heads.** An earlier record
carried, as inherited, that it was *"untracked on every head I checked"*. **That is false against
the repository as it stands**, and is corrected here rather than repeated. The correction is
recorded because the claim was load-bearing for how the lease tool's authority was described.

---

## 5 · The candidate

`CAND-20260826-RELSURF` — branch `plan-release-surface-repair`, `BASE_HEAD 788c357d`, tip
`bf9c807e`, `CANDIDATE_CONTENT_HASH 541a2631b67e95006c05cf6eb4416b0b8993e490e1e184fd861874d70a7feb9e`
(reproduced twice).

Scope: four file modes and one inventory line. **Nothing else.** Change class **MINOR** — no text
in any normative document moves, and no gate's severity or population changes.

| Control | Result |
|---|---|
| the two target guards on `main` | both **exit 1** |
| the two target guards at the tip | both **exit 0** |
| full battery on `main` | **6 red** |
| full battery at the tip | **4 red** — the four CLAUDE.md rows, unchanged |
| failures introduced | **0** |
| does the mode bit reach the hash? | yes — `main` hashes `f82cb0a1…`, the tip `541a2631…`, and the only difference between the trees is four modes plus one line |

**Nothing from another author's branch was committed.** The two repairs exist on
`plan-exec-repair-prep`; both were **re-derived from `main`** here — `chmod +x` on four paths and
one inventory line — so the candidate is a clean two-purpose delta against `main` rather than a
partial import of a 65-commit branch.

---

## 6 · Reproduction

```bash
python3 scripts/run_release_regressions.py               # on each worktree, to completion
python3 scripts/test_release_surface.py                  # exit 1 on main, 0 at the tip
python3 scripts/test_release_runner_verdict.py           # exit 1 on main, 0 at the tip
git diff --summary main plan-release-surface-repair      # four mode changes
python3 governance/scripts/candidate_content_hash.py \
  --base 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5 --tip bf9c807eeb71df497186894a05cc2ae1b1724a2e
```

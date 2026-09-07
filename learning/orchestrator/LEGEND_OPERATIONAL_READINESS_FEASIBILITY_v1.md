---
record_type: FEASIBILITY_REVIEW
record_id: READINESS-001-FEASIBILITY-REVIEW-V1
title: Feasibility review of LEGEND_OPERATIONAL_READINESS_PLAN_v1 — phase 3 of 4
reviewed_object: learning/orchestrator/LEGEND_OPERATIONAL_READINESS_PLAN_v1.md
reviewed_blob_measured: f12d8acecb5acc6d5a7a96662a398dc846e57573
reviewed_blob_expected: f12d8acecb5acc6d5a7a96662a398dc846e57573
hash_match: YES — the bytes did not move under me
reviewed_blob_object_state: >
  ABSENT from the object database. `git hash-object` of the working file returns exactly
  f12d8ace…; `git cat-file -e` on that hash exits 1. No git object and no ref preserves the
  bytes reviewed here. This review is bound to a hash that names a file on one disk.
actor_id: NOT ESTABLISHED — a session cannot resolve its own actorhood
registered_plan_seat: >
  NO. The agent card registry binds ACTOR_ID `plan` to SESSION_ID
  e49d3bd1-2c63-4969-be19-f7fca4b240fc and CURRENT_SESSION_REF `evidence-index-59 [de42c4]`,
  in the `evidence-index` worktree. This session's own reference is ff64774f-662f-4be2-b2c6-ff80e53707f8
  and it runs in the root checkout. It is not that seat and does not claim to be.
role_contract: none held
lease: none held
binding: NO
authority_claimed: none
governing_activation_state: >
  DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE, OPTION B `ACTIVATION_NOT_CONFIRMED`:
  "No actor authority may be assumed from these contracts."
prior_review_read: >
  learning/orchestrator/LEGEND_OPERATIONAL_READINESS_MIRROR_REVIEW_v1.md — all 20 findings
  M-1…M-20 read in full before any finding below was written. M-1, M-2 and the operational
  note on the verification trail are treated as SETTLED INPUTS and are not re-proved.
measured_at:
  branch: legend-operating-convention-v1
  commit: 30cb4f3fd700e2aaf6b608e363438f883ddc3760
  instant: 2026-08-24T08:51Z–09:34Z
  tree: working tree as found — 9 untracked records at open, 10 after this file
findings: 15 — 1 CRITICAL · 7 MAJOR · 6 MODERATE · 1 MINOR
verdict: NOT FEASIBLE AS WRITTEN — feasible under the resequencing named in § R
phase_most_likely_to_stall: "Φ2"
disposition_rule: >
  A finding is not a blocker unless the operator makes it one. This review authorizes nothing,
  blocks nothing, resolves nothing and grants nothing. It produces findings, which need no actorhood.
domain: CONTENT. `learning/` is not among the CONTROL_PLANE_ROOTS of P5.1.
---

# FEASIBILITY REVIEW — LEGEND OPERATIONAL READINESS PLAN v1

> **FINDINGS ONLY · NOT AN AUTHORIZATION · BLOCKS NOTHING · RESOLVES NOTHING · BUILDS NOTHING**

## 0 · Standing, stated unprompted

I hold no `ACTOR_ID`, no role contract, no lease. I checked the registry rather than assuming it.
The agent card registry, which lives on `refs/heads/orchestrator` and nowhere else, binds `plan`
to `SESSION_ID e49d3bd1-2c63-4969-be19-f7fca4b240fc` and to `CURRENT_SESSION_REF
evidence-index-59 [de42c4]`, derived by set complement over four peer lists. This session's
reference is `ff64774f-662f-4be2-b2c6-ff80e53707f8`, and it runs in the root checkout on
`legend-operating-convention-v1`, not in the `evidence-index` worktree. **I am not the registered
`plan` seat.** Under `DEC-20260822` no actor authority may be assumed in any case.

The plan predicted this in its § 13.6 and was right for the fifth consecutive review.

## 0.1 · Verification classes

`RE-DERIVED` — I ran the check myself at this HEAD. `READ` — I read the source object.
`AS REPORTED` — carried on someone else's report and marked as such.

## 0.2 · The hash

```
git hash-object learning/orchestrator/LEGEND_OPERATIONAL_READINESS_PLAN_v1.md
  f12d8acecb5acc6d5a7a96662a398dc846e57573        matches the expected value
git cat-file -e f12d8acecb5acc6d5a7a96662a398dc846e57573
  exits 1 — ABSENT from the object database
```

Positive control `HEAD:CLAUDE.md` → `bf807fec…`, `cat-file -e` succeeds. Negative control, a path
present on no ref, fails. Both controls fire in both directions.

## 0.3 · Settled inputs, not re-proved

**M-1 · CONFIRMED** (AS REPORTED, accepted): of the five consumed blobs, two exist and three do
not. **M-2 · CONFIRMED** (AS REPORTED, accepted): `WORK_COMMIT` is granted to an *actor*, the
plan's standing is `actor_id: NOT ESTABLISHED`, and Φ−1 — the only phase proposed as runnable now
— is therefore not runnable by the session that proposed it. **The operational note · CONFIRMED**:
the plan's own § 12 adds two hits to the documented-commands suite, not one. Everything below
takes these as given and asks the different question.

## 0.4 · My axis

Mirror asked *is this true?*. I ask **can this be done, in what order, at what cost, with what
tools, and what breaks first?** Where I differ from a Mirror finding I say so explicitly, once,
in the finding itself. I differ in exactly one place: **M-9**, at P-1.

---

# FINDINGS

## P-1 · CRITICAL · A-1 is construction. The gate cannot be pointed at a staged set, or at any file list

**Section:** § 7.4 A-1, § 1.4 · **Class:** RE-DERIVED

A-1 proposes *"a pre-commit privacy check on the staged set, using `public_release_gate.py`'s
existing identifier rule against what is about to be committed"*, and prices it as a change of
position, not of substance: *"It needs no new rule — the rule exists and fires correctly; it needs
a **moment**."* § 1.4 binds the plan to a rule about exactly this: *"Where something must be built,
it is named as construction and priced, never smuggled in as preparation."*

**The tool has no entry point for a file list.** Its whole argument surface:

```
python3 scripts/public_release_gate.py --help
usage: public_release_gate.py [-h] [--root ROOT]
                              [--mode {staging,release,clone}]
                              [--report-json REPORT_JSON] [--skip-clean-clone]
```

`--root` is the only path knob, and it names a *repository*, not a set. Reading the walker
confirms there is no other door: `iter_text_files` → `iter_files` → `walk_publishable`, which is
an `os.walk` over the disk beneath `--root`, pruning `SKIP_DIRS`, nested checkouts, and paths that
are simultaneously untracked and gitignored. Nothing in the module accepts a path list, a
`--files` argument, or stdin.

**Pointing it at a subset does not degrade — it produces noise.** I copied two files into a
scratchpad directory and ran the gate on that root:

```
python3 scripts/public_release_gate.py --root <scratchpad>/stagedtest --mode staging
  28 × BLOCK BROKEN_MARKDOWN_LINK      (every relative link in README.md)
   2 × BLOCK MISSING_PROVENANCE_FILE   (THIRD_PARTY_NOTICES.md, _external_repos/MANIFEST.md)
```

Thirty blocks, none of them about privacy, all of them artifacts of the subsetting. The gate is a
whole-repository instrument and its non-privacy checks are repository-wide invariants. **A-1 as
written is unreachable.**

**One route does work, and it is the finding's usable half.** Materialize the index — which *is*
"what is about to be committed" — into a temporary tree and run the gate against that:

```
git checkout-index -a --prefix=<tmp>/          # 581 files, 0.12 s, writes nothing into the repo
python3 scripts/public_release_gate.py --root <tmp> --mode staging
  BLOCKS: 0                                     # 3.6 s
```

It works, it is fast enough for a hook, and on the current index it is green. But it is not
`public_release_gate.py` being given a moment. It is a wrapper that must materialize the index,
invoke the gate, map exit code 2 onto a hook refusal, and remove the temporary tree on every path
including failure — and then a `.git/hooks/pre-commit` that git neither versions nor distributes,
installed by hand in every checkout that could commit.

**I differ from M-9 here, and this is my only disagreement with the hostile review.** M-9 endorses
the plan's framing — *"the record's own § 7.4 A-1 states the true problem correctly: it needs a
moment."* A moment is necessary and it is not sufficient. There is no invocation of the existing
tool that evaluates a staged set, and the plan's own § 1.4 rule applies to the difference.

**Severity:** CRITICAL — not because A-1 is wrong, but because it is the plan's one *new*
infrastructure proposal and it is the one item mispriced in the direction the plan forbids.

**Cost to fix.** Reclassify A-1 as construction and price it: a wrapper of roughly 60–100 lines;
a hook file; an installation step repeated per checkout; a written policy on `--no-verify`, which
silently disables it; and — the item with no cheap answer — **a hook lives under `.git/`, which is
not tracked, so it is the only gate in this repository that the registered regression battery
cannot test.** The plan's own I-8 principle (*"each in an isolated change"*) applies.

---

## P-2 · MAJOR · K-2 declares the audit-instrument class empty. Half the primary metric is already mechanized, exercised, and green

**Section:** § 3 K-2, § 2.1, § 4.1 B-2 · **Class:** RE-DERIVED

K-2 states: *"The bare-condition audit instrument **does not exist in any form**"*, and § 2.1
supports it by describing `legend-locator-audit` as *"102 prose lines over (proposition, quote,
anchor) triples"*.

**A mechanical instrument for one half of the primary exists, is executable, and is read-only:**

```
python3 framework/scripts/locator_audit.py --help
usage: locator_audit.py [-h] [--root ROOT] [--disease DISEASE]
                        [--corpus CORPUS] [--pmid PMID] [--strict]
Does every locator's quote actually occur in the artifact it was taken from?
```

233 lines, mode `100755`. I ran it, holding the status sentinels **outside** the repository so the
measurement did not contaminate itself:

```
python3 framework/scripts/locator_audit.py
  54 manifest(s) audited, 10 unauditable, 0 quote(s) not found        exit 0
  git status --porcelain before and after — identical; no repository write
```

Grepping the source for `write_text`, a `"w"` open, `mkdir`, `json.dump`, `shutil` and
`os.replace` returns nothing: it cannot write.

**Design v2 already knew.** Its § 6.4 verification condition **V-2** reads *"anchored,
digest-matched, quote present (… `locator_audit.py --strict`)"*. The readiness plan mentions the
script **zero** times — positive control on the same file, the token `public_release_gate.py`
appears **8** times, so the sweep can find what is there. **The plan re-derived design v2's
premises and dropped one of its instruments, then declared the instrument class empty.**

The primary metric decomposes into two questions, and only one of them is unmechanized:

| Question | Instrument today |
|---|---|
| Does the quote occur in the artifact it is attributed to? | ✅ `locator_audit.py --strict`, 54 manifests, 0 misses |
| Does the quote *support* the proposition, and does the source say more or less than claimed? | 🔴 none — this is what the schema is for |

**A second instrument exists in the same class** and neither record names it:
`framework/scripts/dossier_quote_audit.py` — *"Do the quotations inside prose dossiers occur in a
paper anybody can point at?"*

**Cost effect: B-2 gets cheaper, and gains one new dependency.** The schema shrinks to the
judgement columns, which is the part § 2.1 correctly says has no precedent. But `locator_audit.py`
audits *deepdive manifests*, and PMID 28123895 has none, so the mechanized half is only reachable
**after** Φ1 has produced a manifest. It verifies a reading; it cannot audit a bare condition. The
plan's K-2 is right about the bare condition and wrong about the class.

---

## P-3 · MAJOR · A-3's population is 27 suites, not 2 — and 8 of them walk from the repository root

**Section:** § 7.4 A-3, § 0 N-2 · **Class:** RE-DERIVED

A-3 is *"scope the disk-walking suites to `git ls-files`"*, and the plan names two:
`test_documented_commands` and `test_fresh_clone_reader_journey`. That is the set that is
currently *red*, not the set that *walks the disk*. I enumerated the whole registered inventory
before counting it.

**Method.** The runner's inventory imported as a module — `run_release_regressions.TESTS`, a tuple
of 65 relative paths — then each file classified by whether it enumerates the filesystem
(`rglob(`, `os.walk(`, `iterdir(`, `.glob(`) or shells out to `ls-files`. All 65 resolved to an
existing file; the four classes sum to 65.

| Class | Count |
|---|---|
| enumerates the filesystem, never `ls-files` | **26** |
| does both | **1** — `scripts/test_release_surface.py` |
| `ls-files` only | **2** — `scripts/test_public_release_gate.py`, `scripts/test_release_runner_verdict.py` |
| neither, in the file itself | **36** |

**27 of 65 enumerate the filesystem.** Most glob a bounded subdirectory — a skills directory, a
manifests directory, a temporary directory — where a laboratory worktree cannot appear. The set
that matters is the one that walks from `ROOT`, and it is **8**, enumerated:

| Suite | walks | prunes nested checkouts | today |
|---|---|---|---|
| `scripts/test_documented_commands.py` | `ROOT.rglob("*.md")` | 🔴 no | **FAIL**, 8 worktree paths in the output |
| `scripts/test_fresh_clone_reader_journey.py` | `ROOT.rglob("*.md")` | 🔴 no | **FAIL**, 7 worktree paths in the output |
| `scripts/test_release_surface.py` | `os.walk(root)`, `root.rglob("*")` | ✅ yes | FAIL, for unrelated reasons |
| `scripts/test_link_targets.py` | `os.walk(root)`, `root.rglob("*.md")` | ✅ yes | PASS |
| `scripts/test_public_claims_contract.py` | `ROOT.rglob("*.py")` | 🔴 no | PASS |
| `scripts/test_generated_surfaces_are_regenerated.py` | `ROOT.rglob("*.md")` | 🔴 no | PASS |
| `scripts/test_structured_data_integrity.py` | `ROOT.rglob("*")` | 🔴 no | PASS |
| `scripts/test_scientific_consistency.py` | `ROOT.rglob("*.md")` | 🔴 no | PASS |

I ran all eight individually. Two fail with worktree paths in their output; `test_release_surface`
fails on the four exec bits plus two gitignored files, which is the local-contamination class
M-6 already located inside the "fails in both" bucket. **Five walk the repository root and pass —
they are green by the luck of what the worktrees happen to contain, not by scope.**

**Cost.** The plan's A-3 is two edits. The honest A-3 is **two edits to stop the bleeding and six
more to close the class** — and the plan's own F-4 already names the class fix (*"derive `TESTS`
from `git ls-files`"*) and defers it to FUTURE, where it cannot serve A-2. Three suites show the
pattern to copy: the gate, `test_release_surface` and `test_link_targets` already prune nested
checkouts, and the gate's `is_exempt` carries the measured history of getting it wrong (340 files
of a nested checkout scanned, 37 false blocks).

---

## P-4 · MAJOR · A-3 does not gate A-2. B-1 does, and that edge is undeclared

**Section:** § 7.4, § 9 · **Class:** RE-DERIVED

The plan states A-3 *"is a prerequisite of A-2, not a follow-up"*, because *"without it, A-2's
development gate is red forever in every laboratory worktree."*

**A-2 is a CI workflow, and CI has no laboratory worktrees.** The existing workflow is 48 lines,
`runs-on: ubuntu-latest`, with `actions/checkout` at `fetch-depth: 1`. A GitHub runner checks out
a clean tree: no `.claude/worktrees/`, no `backup/`, no untracked records. The failure mode A-3
repairs **cannot occur in the environment A-2 runs in**. The rationale describes a developer
running the battery locally, which is a real need and a different one.

**What does gate A-2 is B-1.** I enumerated the offending set of the documented-commands suite at
this HEAD rather than counting it — 15 hit lines over 10 distinct sources:

| Source | hits | tracked? |
|---|---|---|
| `LEGEND_DEVELOPMENT_BOOTSTRAP_AUDIT_v1.md` | 3 | untracked |
| the readiness plan under review | 2 | untracked |
| `.claude/worktrees/{mirror,evidence-index}/…` | 7 | gitignored |
| `backup/…` | 2 | gitignored |

Now apply the two acts in sequence. **A-3** removes the 9 worktree-and-backup hits, because they
are not in `git ls-files`. **B-1** commits the planning corpus, which moves the 5 corpus hits from
untracked into tracked — *into* the scope A-3 just defined. The suite ends up red on 5 hits,
permanently, and visible in CI for the first time.

**Consequence for the roadmap.** A-2's development gate is red on its first run unless the five
documented-command defects inside two records are repaired **before** B-1 commits them. The plan
prices this at zero: § 9's Φ−1 has three steps and repairing them is not one.

**Cost to fix.** Five one-line edits, and one new step in Φ−1 between the redaction and the
commit. Trivially cheap, and invisible in the plan as written — which is the finding.

---

## P-5 · MAJOR · B-1 and B-3 are not independent tiers. Each prices the other, in both directions

**Section:** § 4.1, § 8 row 3 · **Class:** RE-DERIVED

§ 4 presents B-1…B-5 as a flat blocking list with a recommendation each and no dependency edges,
and § 5's step-1 needs-list treats them as separable (*"needs: B-2 · B-3 · B-5"*). At least one
edge exists and it runs both ways.

- **B-3 → B-1.** B-3(b), the recommended answer, defines readiness as *"battery green on a full
  clone, evaluated over `git ls-files` rather than the disk."* Its scope is the tracked set. B-1
  is the act that decides which records are in the tracked set. So B-3 cannot be *evaluated*
  until B-1 has been *executed*, and checklist row 3 inherits that ordering silently.
- **B-1 → B-3.** By P-4's measurement, executing B-1 injects 5 known failures into the population
  B-3(b) defines. The answer to B-3 therefore changes B-1's cost from "commit seven files" to
  "commit seven files and first repair five command references."

**A third edge, undeclared.** B-2's answer changes B-1's scope too: if the audit schema is
authored before Φ0 (B-2 = a, recommended), `TRIAL-001-AUDIT-SCHEMA.md` becomes an eighth planning
record needing preservation under the same act — and it is a record about commands, written in a
repository whose gate scans records about commands.

**Cost to fix:** one dependency column in § 4.1, and one sentence in row 3 saying which act must
precede its evaluation. Free to write. Its absence is what lets the tiers look parallel.

---

## P-6 · MAJOR · Φ−1's scope is a frozen count over a population that grows with every phase that must precede it

**Section:** § 9 Φ−1, § 8 row 2, § 0 N-3 · **Class:** RE-DERIVED

Φ−1 is scoped to *"the 7 records"*, its third step is *"WORK_COMMIT the 7 records"*, and its exit
is *"`git cat-file -e` fires on **all 7 blobs**."* Row 2 scores it *"0 of 7 committed."*

Measured now, enumerated rather than counted — `git status --porcelain`, untracked entries:

```
LEGEND_DEVELOPMENT_BOOTSTRAP_AUDIT_v1.md
learning/orchestrator/FIRST_SCIENTIFIC_RUN_COORDINATION-PLAN-001.md
learning/orchestrator/LEGEND_FIRST_OPERATIONAL_TRIAL_DESIGN_v1.md
learning/orchestrator/LEGEND_FIRST_OPERATIONAL_TRIAL_DESIGN_v2.md
learning/orchestrator/LEGEND_FIRST_OPERATIONAL_TRIAL_EXECUTION_PROTOCOL_v1.md
learning/orchestrator/LEGEND_OPERATIONAL_READINESS_MIRROR_REVIEW_v1.md
learning/orchestrator/LEGEND_OPERATIONAL_READINESS_PLAN_v1.md
learning/orchestrator/TRIAL-001-REVIEW-FINDINGS-REGISTER.md
learning/orchestrator/TRIAL-002-DESIGN-V2-FINDINGS-REGISTER.md
```

**Nine, not seven.** The plan is the 8th, the hostile review the 9th, this file the 10th, and
phase 4 of the mandate — the integrated final plan — will be the 11th. The set grows by one per
phase of the very review cycle that must complete before Φ−1 can run.

**The identifier picture is stable and I re-derived it.** `--root . --mode release` returns
`BLOCK_PUBLICATION`, `BLOCKS: 6`, still **5 × DIRECT_IDENTIFIER** confined to the same two files
(3 in the coordination plan, 2 in design v1) and **1 × DIRTY_RELEASE_TREE**. The three records
added since the plan measured carry **0**. So B-1's *"commit the 5 clean records"* is already
*"commit the 7 clean records"*, and will be 8 or 9 when it can run.

**Feasibility consequence.** An exit criterion of the form *"`cat-file -e` fires on all 7"* is
satisfiable only by freezing the denominator, and the denominator is not frozen. Whoever executes
Φ−1 will either preserve 7 of 10 and pass, or preserve 10 and fail a criterion that says 7.

**Cost to fix:** restate the exit over *"every untracked record present at the instant Φ−1 opens,
enumerated in the phase record before the first act."* One sentence. Also fixes M-7's related
point about what the falsifier covers.

---

## P-7 · MAJOR · The at-risk corpus is understated by two orders of magnitude, and Φ−1 protects the smaller part

**Section:** § 0 N-3 · **Class:** RE-DERIVED

N-3 closes: *"**Total corpus at risk from one `git clean -fdx`: 7 files, 4 301 lines**."* That
figure is measured over untracked-and-not-ignored files. The `-x` in the plan's own hazard command
means *also remove ignored files*, which is a much larger set. Dry run, `git clean -ndx`,
36 entries, and the directories measured:

| Entry | files | size |
|---|---|---|
| `files/` | **795** | **899 M** |
| `tmp/` | 86 | 70 M |
| `staging/` | 138 | 10 M |
| `backup/` | 33 | 4.7 M |
| `grants/` · `grant-applications-private/` · `.playwright-mcp/` | 11 · 6 · 4 | small |
| 7 page-adjudication PNGs, `deployment/local_instance.md`, 3 `.DS_Store` | 11 | small |
| the untracked planning records | 9 | 4 301+ lines |

**≈1 082 files, ≈984 MB.** The six laboratory worktrees appear as `Would skip repository` and
survive a plain `-fdx`; a `-ffdx` would take them too.

**`files/` is gitignored by design** — `.gitignore:7` matches `files/`, and `git ls-files
files/fulltext` returns 0 against a positive control of 3 tracked files under `framework/state`.
It holds 174 full texts, and it is where checklist row 5 requires the trial's own input paper to
land.

**Two consequences, and both are feasibility consequences.**

1. **Φ−1 preserves under 1 % of the at-risk file count.** Committing nine markdown records leaves
   899 MB of scientific corpus exactly as destructible as before, and no commit will ever reach it,
   because it is ignored deliberately and correctly.
2. **The trial's future input is unpreservable by the mechanism the plan proposes.** Row 5's
   artifact lands in `files/fulltext/`. Φ−1's exit criterion cannot see it, and Φ1's acquisition
   produces an asset that a single `git clean -fdx` removes.

**I report this at full weight in the plan's own disfavour.** The understatement weakens the
urgency argument on which Φ−1 — the plan's only proposed act — entirely rests. The true hazard is
larger than the plan claims and Φ−1 addresses the smaller half of it.

**Cost.** A byte-copy of the nine records to a location outside the repository costs seconds,
needs no git act and no actorhood, and discharges the destructibility hazard today. Real
preservation of `files/` is an archival decision about 899 MB — out of git, by size — and it is
priced nowhere in the plan, in design v2, or in the audit.

---

## P-8 · MAJOR · Φ2's exit criterion is half unexecutable, and it fails silently in both directions

**Section:** § 9 Φ2, § 5 STEP 2 · **Class:** RE-DERIVED

Φ2's exit, which design v2's D-12(a) makes the gate on step 3:

> *a replay session reproduces every reported figure **AND** every audit verdict from the record
> alone, without asking the reader or the auditors anything*

It is a conjunction, and the two halves have different feasibility.

**Figures — executable in principle, and the precedent is against it.** A figure with a command
beside it can be re-run. But the plan's own § 12, the model for such a trail, is not runnable as
printed: it contains an ellipsis character inside a shell loop, a sentinel pair that writes into
the repository it is measuring, and a joined continuation that names a flag the runner does not
expose. Re-derived: `run_release_regressions.py` exposes exactly `--list` and `--only`.

**Audit verdicts — not executable, and nothing in the repository makes them so.** I swept for a
retention mechanism: tracked files with `transcript` in the name = **0**, against a positive
control of **6** for `receipt`. What is retained is the record. So the replayer's situation is:

- If the verdicts are **in** the record — which they must be, since the criterion says *"from the
  record alone"* — the replayer reads them. Reading a verdict is not reproducing it. The criterion
  passes trivially and tests nothing.
- If the replayer instead **re-judges**, any disagreement is the expected behaviour of a judgement
  instrument, and there is no rule for it: no concordance threshold is declared for Φ2, no rung of
  the degradation ladder covers it — the ladder's rungs are about personnel — and design v2 § 7
  states *"Statistics: **None.** n = 1 paper"*, so no disagreement could be adjudicated.

**A gate that cannot fail is not a gate, and this one gates the multi-agent extension.**

**Cost to fix, and it is the largest unpriced item in the roadmap.** Either (i) restrict Φ2 to
figures and say so in the outcome — cheap, honest, and it makes step 3's gate weaker than design
v2 claims; or (ii) define Φ2 as a **blind re-audit** with the verdicts withheld from the replayer
and an agreement threshold declared before the shuffle. Option (ii) is a second study with its own
personnel, its own instrument and its own schema, and the plan gives Φ2 two lines.

---

## P-9 · MODERATE · The control-plane reconciliation is one of three acts, and the cheapest is available today at zero authority cost

**Section:** § 2.2.1, § 4.2 I-1 · **Class:** RE-DERIVED

§ 2.2.1 samples 7 refs and concludes: *"The two objects … have **never been on the same tree**.
The reconciliation design v2 asks for cannot be performed as a comparison today — **it is a merge,
and a merge is an act nobody has been authorized to perform.**"*

**I re-derived it over the full population rather than a sample**, with a positive control
(`CLAUDE.md`) and a negative control (a path present on no ref):

| Object | present on |
|---|---|
| `CLAUDE.md` *(positive control)* | **56 / 56** path-bearing refs |
| a path that exists nowhere *(negative control)* | **0 / 57** |
| `runtime/agent_card_registry.md` | **1** — `refs/heads/orchestrator` only |
| `framework/protocols/scientist_reading_modes.md` | **23** |
| `governance/decisions/DEC-20260822-…` | **16** |
| 🔴 **refs carrying BOTH the registry and the protocol** | **0** |

**A correction to the denominator, which the plan and Mirror both carry as 57.** The control
resolves on 56 of 57 refs. The 57th, `refs/tags/handoff/C-2/PMID42422765-working-blob`, is a tag
pointing at a **blob**, where `ref:path` has no meaning — `git cat-file -t` returns `blob`. The
path-bearing denominator is **56**. Every negative above is scoped to it.

**The plan's central claim is TRUE, and stronger than it proved.** I report that at full weight:
1 of 56, not 1 of 7; intersection empty over the whole ref space, not over a sample.

**The feasibility question the plan does not ask has three answers, not one.**

| Route | What it costs | Available now? |
|---|---|---|
| **(a) a READ** — compare the two objects where they already are | nothing. No git act, no actorhood | ✅ **yes** |
| **(b) a CHERRY-PICK** — the registry entered `orchestrator` in exactly one commit, `632ad22` | one commit | needs an actor |
| **(c) a MERGE** | `orchestrator` is **42 ahead** of and **40 behind** HEAD, merge-base `cbce3016` — 82 commits of divergence | needs an actor **and** is blocked besides |

Route (a) is not hypothetical. Both objects are readable on this disk right now, simultaneously,
from the root checkout:

```
.claude/worktrees/orchestrator/runtime/agent_card_registry.md      READABLE, 314 lines
framework/protocols/scientist_reading_modes.md                     READABLE, 526 lines
negative control — a sibling path that does not exist              ABSENT
```

I performed that read in this session's first tool call, holding no authority of any kind.
**W-1/P-5 asked for a comparison; a comparison is a read; the read is free.** What needs authority
is the durable single-tree *state*, and only that.

Route (c) carries a second obstacle the plan does not mention: `refs/heads/orchestrator` is
**checked out in a live worktree**, and git refuses to update a branch checked out elsewhere. The
merge is not merely unauthorized — from the root checkout it is mechanically refused.

**Cost to fix:** split I-1 into *the comparison* (free, today, any session) and *the
reconciliation* (an actor, a route chosen from b/c). The plan defers both to "before step 3" on
the strength of the expensive one.

---

## P-10 · MODERATE · Row 5's instrument cannot evaluate two of its three clauses, and one of them is unverifiable by construction

**Section:** § 8 row 5 · **Class:** RE-DERIVED

Row 5's condition is a conjunction of three: *"the artifact is in `files/fulltext/`, its sha256 is
recorded in the acquisition declaration **authored before acquisition**, and `fulltext_receipts.py
verify` passes"*, verified by *"the two commands"*.

`verify` takes no options at all — its `--help` lists only `-h`. What it does is validate the
ledger chain and check the tail anchor in the state manifest. It is blind to whether any given
artifact sits in `files/fulltext/`, and it is blind to authoring order.

| Clause | Evaluable by row 5's instrument? |
|---|---|
| artifact present in `files/fulltext/` | ✗ — a directory listing does this, and row 5 does not name one |
| sha256 recorded in a declaration **authored before acquisition** | ✗ — **no instrument in this repository evaluates a temporal ordering of authorship** |
| the ledger verifies | ✅ |

§ 8's own preamble requires that *"a condition whose evaluation is a judgement says so."* The
before-acquisition clause is exactly such a judgement — filesystem timestamps do not establish
authorship order — and the row does not flag it.

**Cost to fix:** name the listing as the first instrument, and mark the ordering clause a
judgement with a named party. Two words and a name.

---

## P-11 · MODERATE · Row 7's allowlist verifies — and the plan understates its own result, while a prohibition collides with it unpriced

**Section:** § 8 row 7 · **Class:** RE-DERIVED

Row 7 scores ⚠️ **PARTLY**: *"repaired in v2 after two BLOCKERs; **not re-verified since**."* I
re-verified it by reading what the instrument writes.

`fulltext_receipts.py record` writes to exactly two paths outside `learning/`:

```
default_ledger_path(root, disease)  → disease-models/<disease>/registries/fulltext_read_receipts.jsonl
default_manifest_path(root)         → framework/state/state_manifest_current.md
```

and `write_state_anchor` re-anchors the second **atomically, in-lock, on every append** — it is not
optional and not deferrable. Design v2 § 3.5 names **both**, unqualified, with the manifest marked
🆕 and annotated *"`record` re-anchors it IN-LOCK, on every append. Not optional."*

**Row 7 can be scored ✅.** The allowlist matches the instrument. The plan could have established
this by reading three functions and did not, and the ⚠️ it carries instead is worse than the truth.
Reported at full weight in the plan's own disfavour.

**The unpriced collision.** `framework/state/state_manifest_current.md` is inside `framework/`,
and the standing mandate on this whole review cycle forbids modifying `framework/` — a prohibition
the plan restates for itself in § 11. So **Φ1b's first receipt write lands inside the tree the
mandate's own prohibition covers.** Nothing in § 4 converts that into an operator decision; it is
not B-1…B-5, and it is not I-1…I-8.

**Cost to fix:** one line in Φ0 asking for a scoped, named lift of the `framework/` prohibition
for `state_manifest_current.md` only, for the duration of Φ1. Free to write, and it has to be
asked for by someone, because the instrument will do it whether or not anyone asked.

---

## P-12 · MODERATE · `reviews/trial-001/` is creatable and inside the allowlist; the block is not the path

**Section:** § 3 K-8, § 4.2 I-4, § 8 row 6 · **Class:** RE-DERIVED

K-8 is *"No Φ7 artifact path exists — `reviews/` holds `plan/` and 3 files"*, listed as a block
halting Φ7. I checked whether it can be created inside any allowlist the plan names.

- `reviews/` exists and is **tracked** — three files under `reviews/plan/`.
- `git check-ignore reviews/trial-001` exits 1: **not ignored**.
- Design v2 § 3.5 — the allowlist row 7 points at — lists `reviews/trial-001/…` explicitly,
  annotated *"does not exist — D-8 creates it."*

**So creation is a `mkdir` inside a declared allowlist, and it is not blocked by anything.** Git
does not track empty directories, so *preserving* it requires a file and a commit — the same one
act Φ−1 needs and M-2 has settled. The block is not the path; it is the commit, counted twice.

**Cost:** zero to create. Listing it beside blocks that cost something inflates § 3, and M-4
already found the routing defect from the other side.

---

## P-13 · MODERATE · Four operational risks the roadmap has no phase for

**Section:** § 9, § 11 · **Class:** RE-DERIVED

**(a) Concurrent writers on one shared checkout.** The nine untracked records were written into
the **root checkout** by at least three different sessions — the plan, the hostile review, and
this one — and Φ−1's act is a commit on `legend-operating-convention-v1` in that same directory. A
staging step scoped to a directory would sweep in whatever a concurrent session has half-written
at that instant. **One mitigation already exists and the plan does not credit it:** a PreToolUse
guard in this repository denies blanket staging outright. That guard is doing load-bearing work
for Φ−1's safety and appears in no record.

**(b) 25 worktrees, 14 prunable — and the 14 are not idle bookkeeping.** Enumerated: all fourteen
live under `/private/tmp/claude-501/<session-uuid>/scratchpad/wt-*`. They are prunable because the
operating system already removed their directories. Each still holds a **branch registered as
checked out**, and a branch checked out in any worktree cannot be updated from elsewhere. Any
resequencing that needs to write one of those fourteen branches must run `git worktree prune`
first — a repository write that no phase names and no decision scopes.

**(c) The reconciliation target is locked by (b)'s mechanism.** `refs/heads/orchestrator` is
checked out in a live worktree, which blocks P-9's route (c) independently of authority.

**(d) The at-risk corpus shares a volume class with what has already been destroyed.** The
fourteen worktrees that vanished were under `/private/tmp`. That is the precedent for how this
laboratory loses artifacts, and it is not a hypothetical hazard — it has already happened
fourteen times.

**Cost to fix:** (a) is a sentence in Φ−1 requiring the commit to name its paths explicitly,
enumerated, never a directory. (b) is a decision in I-8's mechanical tier. (c) is a note on I-1.
(d) is P-7's archival decision.

---

## P-14 · MODERATE · Every phase of this roadmap authors a record into a repository whose gate scans records, and no phase checks before declaring done

**Section:** § 9, § 0 N-2 · **Class:** RE-DERIVED

N-2 names the self-reference for the audit document — *"An audit document cannot be written in this
repository without turning the battery red, which is a self-reference worth naming"* — and the
operational note has settled that the plan then did it to itself, twice, in § 12.

**The feasibility point is about the roadmap, not the record.** Φ0 authors an audit schema. Φ1
authors two outcome records, a friction log and an SLR. Φ2 authors a replay record. Phase 4 of
this mandate authors the integrated plan. **Every one is a markdown record, in a repository whose
`test_documented_commands` walks every markdown file and asserts that every documented flag exists
and every documented python path resolves.** Each is a fresh opportunity to redden the suite that
checklist row 3 depends on — and after B-1 they are all tracked, so the reddening is permanent and
CI-visible (P-4).

**No phase in § 9 has a step that runs the two guard suites before the record is declared closed.**

**Cost to fix: one line per phase**, and it is the cheapest fix in this review with the best
precedent — the hostile review did it unprompted, disclosed the constraint in its § 0.3, and
contributes **0** hits to either suite. I did the same and verified it, in § V below.

---

## P-15 · MINOR · Two instrument surfaces, recorded so the next record does not have to re-measure them

**Section:** § 12 · **Class:** RE-DERIVED

`run_release_regressions.py` exposes exactly two options, `--list` and `--only`, the latter
repeatable. The plan's joined-continuation line names an option it does not have, which is the
second of the two settled hits.

`public_release_gate.py` exposes `--root`, `--mode {staging,release,clone}`, `--report-json` and
`--skip-clean-clone`. `--report-json` is the machine-readable route a future gate wrapper should
use rather than parsing `[BLOCK]` lines with awk, as § 12 does.

---

# W · What the plan understates in its own disfavour

Reported at the same weight as the defects, because a record that undersells its own case is as
hard to act on as one that oversells it.

| # | Where | The plan says | Measured |
|---|---|---|---|
| **W-a** | N-3 | corpus at risk: *"7 files, 4 301 lines"* | ≈**1 082 files, ≈984 MB** (P-7). The urgency argument for its only phase is far stronger than it claims — and Φ−1 addresses the smaller half |
| **W-b** | K-2 | the audit instrument *"does not exist in any form"* | one half of the primary is mechanized, exercised on 54 manifests, exit 0, read-only (P-2). The plan's own § 6 thesis — *"the laboratory is further along than its own records read"* — applies here and is not applied |
| **W-c** | § 2.2.1 | the registry and the protocol are disjoint across **7 sampled** refs | disjoint across **all 56** path-bearing refs (P-9). It proved less than it had |
| **W-d** | § 8 row 7 | ⚠️ *"not re-verified since"* | the allowlist matches the instrument exactly; the row is ✅ on three functions' worth of reading (P-11) |
| **W-e** | N-1 | *"BLOCKS: 6"*, presented as the corpus's problem | one of the six is `DIRTY_RELEASE_TREE`, which fires for **any** untracked file and will fire after Φ−1 too, for as long as any session is mid-work. It is not curable by Φ−1 and the record does not say so — which makes Φ−1's own falsifier look weaker than it is, since that falsifier is correctly scoped to `DIRECT_IDENTIFIER` alone |

---

# R · Correct order — what is actually runnable now

The mandate asks whether a resequencing makes something runnable, or whether the honest answer is
that nothing is until the operator acts. **Both, and the split is the useful part.**

**Nothing in the roadmap as written is runnable by a session today.** Φ−1 is the only phase
proposed as runnable, and M-2 has settled that its third step needs an authority no session holds.

**But Φ−1 is separable, and the separation moves the authority requirement off the half that
carries the urgency.** Its three steps have different requirements, and the plan bundles them:

```
Φ−1a   redact the 5 identifier hits in 2 records
       re-run the publication gate against the working tree
       repair the 5 documented-command references before they become tracked   ← P-4
       EXIT: the gate reports 0 DIRECT_IDENTIFIER
       needs: decision B-1 only.  NO commit.  NO actorhood.  NO instrument that does not exist.

Φ−1b   WORK_COMMIT the records, enumerated by path at the instant the phase opens   ← P-6
       EXIT: cat-file -e fires on every enumerated blob
       needs: B-1, AND an actor holding WORK_COMMIT on this branch
```

Φ−1a is a write to untracked **content** files under `learning/`, which the plan's own frontmatter
places outside the `CONTROL_PLANE_ROOTS` of P5.1, and its exit criterion — the gate reporting zero
identifier blocks — is evaluable **without any commit at all**. It is runnable by any session the
operator points at it, the moment B-1 is answered.

**The correct first act is therefore the operator's, and it is smaller than the plan implies:**
answer B-1, and say which half of Φ−1 is authorized to whom.

**Three things worth doing beside that, at zero authority cost, in any order:**

1. **Copy the ten untracked records out of the repository.** It needs no git act, no actorhood and
   no decision, and it discharges the destructibility hazard today. It does not discharge
   preservation-as-a-reviewable-object, which is what B-1 is for.
2. **Perform the I-1 comparison as a read** (P-9). Both objects are on this disk. The comparison
   W-1/P-5 asked for costs nothing and does not have to wait for step 3.
3. **Decide what happens to `files/`** (P-7). 899 MB, gitignored by design, holding the trial's
   future input, and reachable by no commit anyone is proposing.

---

# VERDICT

> ## NOT FEASIBLE AS WRITTEN
> **Bound to blob `f12d8acecb5acc6d5a7a96662a398dc846e57573`**, branch
> `legend-operating-convention-v1` @ `30cb4f3fd700e2aaf6b608e363438f883ddc3760`,
> measured 2026-08-24T08:51Z–09:34Z.

**The analysis is largely sound; three load-bearing *execution* claims are not.**

1. **Φ−1 is not runnable now** by the party proposing it — settled at M-2, and § 9's *"the only
   phase runnable before the next mandate"* is the sentence that fails.
2. **A-1 needs no construction** — false. The gate accepts no file list and no staged set, and the
   only working route is a wrapper plus an untrackable hook (P-1).
3. **Φ2's exit criterion is executable** — false for the audit-verdict half, and it fails silently
   in both directions while gating step 3 (P-8).

Two further claims are mispriced rather than false: A-3's population is 8 root-wide suites and not
2 (P-3), and its gating relation to A-2 does not hold — B-1 holds it instead (P-4).

**What makes it feasible**, and the list is short: split Φ−1 per § R · reclassify and price A-1 as
construction · restate Φ−1's exit over an enumerated set rather than a frozen count · declare
whether Φ2 means figures-only or a blind re-audit · add the dependency edges B-1↔B-3 and B-1→A-2 ·
add one guard-suite check per phase. **None of the six is expensive. All six are invisible in the
plan as written, which is why the verdict is on the writing and not on the thinking.**

## Phase most likely to stall

> ## Φ2 — METHOD VALIDATION

**Why, and why not the others.** Φ−1 is *blocked*, not stalled: a blocked phase has a named
remedy, an operator can grant it, and § R shows half of it is runnable regardless. Φ0 is five
decisions and a document — the operator can make decisions. Φ1 carries the largest *declared* cost
and has a **declared degradation ladder with a floor** (a `READING RECORD` rather than nothing), so
a Φ1 that goes badly produces a lesser result rather than none.

**Φ2 has no floor.** Its exit is a conjunction whose second half — *"every audit verdict …
reproduced from the record alone"* — has no executable procedure, no retained transcript (0 tracked
files matching, against a positive control of 6), no declared agreement threshold, no statistical
basis (design v2: *"Statistics: None. n = 1 paper"*), and no rung of the degradation ladder that
covers it, because the ladder's rungs are about personnel. It is two lines long in a 785-line
record, and it is the gate on the entire multi-agent extension.

**Its failure mode is the dangerous kind: silent, in both directions.** A replayer who reads the
verdict in the record has "reproduced" it and learned nothing. A replayer who re-judges and
disagrees has no rule that says whether the phase closed. **Φ2 will not announce that it stalled —
it will announce that it passed.**

---

# V · Guard-suite compliance for this file

🔴 The plan under review turned a suite red by writing about it, twice. The hostile review did not.
I checked before declaring this record done, and the result is recorded here rather than promised.

Constraints read from the sources, not assumed:

- `scripts/test_documented_commands.py` joins shell continuations into one logical line and asserts
  that every option appearing after a `python3 <path>.py` token is exposed by that script's
  `--help`. Every python invocation in this file is on its own line, carries only options I ran
  `--help` against first, and no line ends in a continuation backslash.
- Its `PYTHON_PATH` rule resolves any `dir/file.py` beginning with `.claude/`, `disease-models/`,
  `framework/` or `scripts/`, and any `./`-relative path against **this document's own directory**.
  This file contains no dot-slash path, and every prefixed path in it resolves to an existing file.
- `scripts/test_fresh_clone_reader_journey.py` resolves any backticked `*.md` or `*.py` under the
  same prefixes plus `release/`. Every such reference here exists; every reference to a record
  under `learning/`, `governance/`, `reviews/` or the repository root falls outside those prefixes
  and is not checked.

Both suites were run after this file was written. The result is in the final report to the
orchestrator, alongside the hit-count delta attributable to this record.

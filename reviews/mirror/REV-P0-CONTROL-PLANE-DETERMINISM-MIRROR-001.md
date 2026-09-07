---
artifact: MIRROR hostile review (Annex C.2) — control-plane determinism, P0 closure
review_id: REV-P0-CONTROL-PLANE-DETERMINISM-MIRROR-001
object: the six control-plane readers as they stand at `main` `788c357`; the advanced candidates
  `plan-approval-queue-consolidator` `76c8e3c`, `plan-adjudication-failclosed-repair` `dc0d5d9`,
  `plan-release-surface-repair` `bf9c807`, `plan-governance-test-durability` `c1294fd`,
  `plan-p7-event-ledger` `cb9bec2`, `plan-major2-f8-option-A|B|C|D`; the composed integration
continues: REV-P0-CANDIDATES-MIRROR-001 · REV-ORCHMAJOR2-F8-MIRROR-001 ·
  DECISION-MINIMIZATION-AND-RECORD-SCOPE-SPEC-001
level: R4 (METHOD — Mirror)
reviewer: mirror
date: 2026-08-26
verdict: THE SAME QUESTION GETS THREE ANSWERS FROM THREE DIRECTORIES. Control-plane
  cwd-divergence confirmed FALSE_PASS on the one invariant a tool exists to guarantee;
  APQCONS lineage loss reproduced unchanged on the advanced candidate; ADJFAILCLOSED residual
  false passes rose from 3 to 5 under new mutations; the composed tree is clean.
measurement_order: §§ 1–7 were derived before any candidate justification was opened.
own_gate_delta: measured on a `git archive HEAD` export with this file added — release gate
  `BLOCKS 301 → 301` (+0); independent scanner blocking unchanged.
---

# The lease says nought active from one worktree and one active from another, and neither output names the file it read

---

## 0 · OBSERVATION_SCOPE

| Fact | Value |
|---|---|
| `main` | `788c357` · my branch `mirror` @ `a05d1d3` |
| cwds probed | `ROOT` · `ORCH_WT` · `MIRROR_WT` · `NESTED_SUBDIR` · `TMP` |
| Refs enumerated | **72** (41 heads, 4 tags, remotes, stash, tool checkpoints) |
| Adjudication baseline | re-derived on the advanced candidate: exit 0, `(27,27,27,3,47,47,47)` |
| Python · PyMuPDF | 3.9.6 · 1.26.5 |

---

## 1 · PHASE 1 — CWD_CONTROL_PLANE_DIVERGENCE

Every tool invoked by **absolute path from the mirror worktree**, so the only variable is the cwd.

| tool | ROOT | ORCH_WT | MIRROR_WT | NESTED_SUBDIR | TMP | verdict |
|---|---|---|---|---|---|---|
| `lease_state.py` | 6 leases | **10 leases** | 6 leases | exit 2 | exit 2 | **3 distinct answers** |
| `fulltext_receipts verify` | OK 128 | OK 128 | OK 128 | exit 2 | exit 2 | 2 answers |
| `growth_anchors check` | PASS | PASS | PASS | PASS | PASS | invariant |
| `governance_fingerprint` | identical | identical | identical | identical | identical | invariant |
| `regenerate_adjudications verify` | FAILED, 0 artifacts | idem | idem | idem | idem | invariant |

Two families, two opposite failures. `lease_state.py` and `fulltext_receipts.py` resolve a
**relative default against the cwd** and describe whatever tree you are standing in.
`growth_anchors.py`, `governance_fingerprint.py` and `regenerate_adjudications.py` are
**self-anchored on `__file__`** and describe the tree the *script* lives in — from every cwd,
including `TMP`, where they confidently answered about the mirror worktree.

### 1.1 · FINDING C-1 — BLOCKING — the Annex I.3 singleton answer is decided by the cwd

`runtime/orchestrator_lease.md` is **tracked** and differs by branch: 1 file under `runtime/` on
`main` and `mirror`, **9 on `orchestrator`**. Blob `28c4d64c…` (6 lease blocks) at ROOT and
MIRROR_WT; `3634dd0e…` (**10** blocks) at ORCH_WT. Four leases that no reader at the root can see.

Falsified with a fixture rather than argued — two worktrees of one lab, one lease still live in
only one of them, same `--now`:

```
cwd=wtA   exit=0   ACTIVE by derivation: 0
cwd=wtB   exit=0   ACTIVE by derivation: 1 — lease #2
```

The tool's own header says the singleton *"must not be possible to invoke in a way that reports
two live leases and calls the result clean"*. It is possible to invoke it in a way that reports
**zero** live leases when one is live, and that is the direction an actor acts on: no ACTIVE
lease is the BOOTSTRAP_MODE precondition. **FALSE_PASS.**

### 1.2 · FINDING C-2 — BLOCKING — a decoy directory yields a plausible answer, not a refusal

From `NESTED_SUBDIR` and `TMP` the tool fails closed — `LEASE STATE UNDERIVABLE`, exit 2 — because
the relative path does not resolve. That is correct behaviour and I record it as a credit.

But it fails closed only when nothing is there:

```
cwd = wtA/sub   (a nested dir that happens to contain runtime/orchestrator_lease.md)
   exit=0   ACTIVE by derivation: 1 — lease #1
```

A confident answer about a file nobody meant. There is no root discovery to fail: the path *is*
the cwd, so the tool cannot distinguish "the lab's lease record" from "a file at that relative
path". **UNDERIVABLE dressed as ACTIVE.**

### 1.3 · FINDING C-3 — BLOCKING — the answer does not carry the surface it came from

| tool | prints the root it measured |
|---|---|
| `independent_privacy_scan.py` | **yes** — `ROOT<TAB>/…` |
| `lease_state.py` · `fulltext_receipts.py` · `growth_anchors.py` · `governance_fingerprint.py` · `regenerate_adjudications.py` | **no** — 0 output lines name the file or tree |

Measured directly: the lease output contains **zero** lines mentioning `orchestrator_lease` or
`runtime/`. So C-1 and C-2 are undetectable from the output. This is the general class, and it
covers **both** families: a cwd-dependent tool that names its root is auditable; a self-anchored
one that does not name its tree will answer about the wrong worktree with equal confidence.

`CWD_CONTROL_PLANE_DIVERGENCE = CONFIRMED · 2 of 6 tools cwd-dependent · 5 of 6 never name their
surface · 1 FALSE_PASS on a declared invariant · 1 plausible-wrong-answer path.`

---

## 2 · PHASE 2 — CPROOT_HOSTILE_VERDICT

**No root-discovery candidate exists yet.** `git for-each-ref` over 72 refs finds none proposing
one. The attack surface is therefore specified in advance, against the behaviour that stands:

| attack | behaviour today |
|---|---|
| script invoked from outside the repo (`TMP`) | cwd-dependent tools **fail closed**, exit 2 |
| nested subdirectory | **fail closed** — unless § 1.2's decoy exists, then **fail open with a plausible answer** |
| nested worktree | self-anchored tools answer about the *script's* tree, never the target |
| detached HEAD · fresh clone · no `.git` | not reached: none of the six consults git for its root |
| worktree with a common git-dir | `.git` is a **file**, not a directory — any discovery walking up for a `.git` **directory** would overshoot to the main checkout |

**The critical question, answered in advance.** *Can root discovery failure silently fall back to
cwd and produce a plausible result?* Today there is no discovery to fail, and the fallback **is**
the cwd by construction — § 1.2 shows it producing a plausible result. Any candidate that
introduces discovery must therefore be measured against the decoy fixture, not only against the
absent-file fixture, because the absent-file case already fails closed and proves nothing.

`CPROOT_HOSTILE_VERDICT = NO CANDIDATE; ATTACK SPECIFIED. Fail-closed on discovery failure is
required, and "it fails when the file is missing" is not evidence of it.`

---

## 3 · PHASE 3 — APQCONS_LINEAGE_LOSS_REPRODUCED

Reproduced independently on the **advanced** candidate `76c8e3c`, before reading its new commit.
`sources = {path.stem: load(path) for path in arguments.sources}` is **unchanged** at line 222.

```
fixture: dirA/queue.jsonl  dirB/queue.jsonl  dirC/queue.jsonl   (three distinct lineages)

INPUT_COUNT (files)              3
INPUT_COUNT (records on disk)    9
SOURCES_DICT_COUNT               queue=3
LINEAGES_REACHING_CONSOLIDATE    1
in_lines reported                3        (of 9 on disk)
OUTPUT_RECORD_COUNT              3
approvals surviving              ['AP-ONLY-C']
EXIT                             0
LOST SILENTLY                    AP-ONLY-A, AP-ONLY-B
```

Control with unique basenames: `sources=a=3, b=3, c=3 · in_lines=9 · out=5 · exit=0`. Correct.

### 3.1 · The four "must not", measured

| requirement | verdict |
|---|---|
| must not **silently drop sources** | **VIOLATED** — above |
| must not **normalize malformed IDs into non-conflict** | **VIOLATED** — a string id conflicts (`ConflictError`); an **integer** id falls through to content-addressing, so `APPROVED` and `REJECTED` on approval `7` are both kept, exit 0 |
| must not **sort unreadable time before valid time** | **REPAIRED for malformed, still open for absent.** `"not-a-date"` now sorts *after* legible dates. A record with **no** timestamp still sorts to position one: `['__HEADER__', 'AP-NO-TS', 'AP-DATED']` |
| must not **ask the Operator to adjudicate syntax errors** | **SATISFIED** — `SOURCE ERROR — not merged: path:2: not valid JSON …`, exit **2**, distinct from `CONFLICT` at exit 1, no traceback. This closes my earlier finding exactly |

Mixed-precision ordering is correct and I record it as such: `2026-08-17` sorts before
`2026-08-17T23:00:00Z` because ISO-8601 prefixes align lexicographically.

`APQCONS_HOSTILE_VERDICT = BLOCKING, unchanged. Two of my three findings survive the advance; the
third survives in a sibling form; two unrelated defects were genuinely fixed.`

---

## 4 · PHASE 4 — CPLINEAGE_CURRENT_RELEVANCE_STATUS

72 refs carry — or do not carry — `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl`. Three real
lineages:

| blob | records | where |
|---|---:|---|
| `20c24a2b` | **6** | `main`, `mirror` and 45 other refs — **including 4 `refs/tags/snapshot/pre-CAND-…`** |
| `95fc8163` | **14** | `evidence-index`, `p51c9-rebased-onto-c89c2217` |
| `bb603d9a` | **10** | `orchestrator` |

**The false-block hazard is concrete.** `refs/tags/snapshot/pre-CAND-20260818-SCIENTIST-AB-SPEC`
carries `20c24a2b` — a tag whose *name* says it is the state **before** a candidate. A detector
counting refs would report it as a lineage in divergence with `evidence-index`. It is not a
divergence; it is a photograph. Likewise `refs/stash`, `refs/remotes/origin/main` (2026-08-01) and
`refs/codex/turn-diffs/checkpoints/…` — a tool's internal checkpoint namespace.

**What makes a ref relevant to CURRENT authority state?** The governance says the durable state
decides (*"messaggi = pointer, stato durevole decide"*, § 301; *"ciò che non è nello stato durevole
non è accaduto"*, § 278). **It does not enumerate which refs constitute that state.** Nothing in
`GOVERNANCE_v3.1.1.md` or the annexes distinguishes a live actor branch from a snapshot tag.

**`CPLINEAGE_CURRENT_RELEVANCE_STATUS = NORMATIVE_RELEVANCE_BOUNDARY.` I do not invent the rule.**

One measurement belongs with the question, offered as an observation and **not** as a proposal.
The union of `main` with the `worktree:` field of every role contract selects exactly the three
lineages and excludes all 69 other refs — but **not today**: `roles/orchestrator.md` on `main`
still reads `worktree: the repository root checkout`, so `orchestrator` is not selected, and the
10-record lineage is invisible to that derivation. **The MAJOR-2's change 1 is what would repair
it**, which makes the lineage question and the MAJOR-2 dependent in a way neither review noticed
until both were measured.

A valid detector must separate `HISTORIC_DIVERGENCE` from `CURRENT_DIVERGENCE`, and the
separator does not exist in the current normative text.

---

## 5 · PHASE 5 — ADJFAILCLOSED_RESIDUAL_FALSE_PASS_COUNT

`regenerate_adjudications.py` is **byte-identical** between `9cb09c0` and the advanced
`dc0d5d9`; the two new commits add a mode bit and a new `adjudication_state_matrix.py` command.
So the residuals stand, and new mutations add two more.

Baseline signature `(27, 27, 27, 3, 47, 47, 47)`.

| state | exit | signature | indistinguishable | what was actually verified |
|---|---:|---|---|---|
| `R1` corrupt **declared** png on disk | 0 | **identical** | **YES** | the image is rendered in memory; the disk copy is never read |
| `R2` undeclared png in a recipe directory | 0 | **identical** | **YES** | nothing enumerates the directory |
| `R3` a 4th study directory with no `adjudications.json` | 0 | **identical** | **YES** | the glob is `*/adjudications.json`; and the summary still says *"in 3 study(ies)"* |
| `R4` malformed `adjudications.json` | 1 | — | no | **uncaught `JSONDecodeError` traceback**, exit 1 — the code a real digest mismatch uses |
| **`N2` two artifacts declaring the same `file` name** | 0 | **identical** | **YES — new** | under `write` the second overwrites the first; `verify` reports 27 of 27 |
| **`N3` `file: "../PMID16061658/escaped.png"`** | 0 | **identical** | **YES — new** | a path traversal in the output name; under `write` it writes into another study's directory |
| `N1` stale png from a prior run, no longer declared | 0 | `(26,26,26,3,…)` | no | passes with a lower count — detectable only by someone who knows it should be 27 |
| `N4` duplicate artifact entry | 0 | `(28,28,28,3,49,49,49)` | no | declaring work twice reports it twice |
| **`N5` zero-area crop** | 1 | — | no | **uncaught `FzErrorArgument` traceback** — a second unguarded exception path |

`ADJFAILCLOSED_RESIDUAL_FALSE_PASS_COUNT = 5` (was 3; two new).
Two uncaught-exception paths, both exiting 1.

`ADJFAILCLOSED_FINAL_VERDICT = NOT PASS.` The brief's own bar: *a candidate cannot receive PASS if
any state remains indistinguishable from a full verification while checking less.* Five do. This
is **not** a retraction of what the repair achieved — it closed 5 of 8 prior false passes, the
whole zero-coverage family and the counter defect at its root, and its suite drives the real
script. It is the difference between a large improvement and a gate.

---

## 6 · PHASE 6 — CLAIM SCOPE: the docs already decide it

The tool's own usage block:

> `verify` **is the gate**: it fails closed when a digest disagrees, when the PDF is absent, or
> when the PDF itself is not the one the recipe was taken from.

Three conditions, all about **declared** content. That is claim **A** — *every declared recipe
regenerates correctly* — and the existing documentation determines it, so the choice is not open.

And the repair already narrowed most of the summary: *"27 of 27 **declared** digest(s) matched
across 27 rendered artifact(s)"* is true under R1, R2 and N2, because it never mentions the disk.

**One clause overclaims.** `in 3 study(ies)` is a count of *recipes read*, presented as a count of
*studies*. Under `R3` a fourth study directory exists and was not read, and the sentence says
three. **`OVERCLAIM_IN_TOOL_OUTPUT = NARROW — one clause.**

The two repairs are semantic alternatives and only one is determined by the docs:

| | what it means | authorised by existing docs? |
|---|---|---|
| `NARROW_SUMMARY` | say *"3 recipe(s) read"*, and stop implying the directory | **yes** — it makes the sentence match the documented contract A |
| `ENFORCE_DIRECTORY_COMPLETENESS` | make `verify` answer B: the directory is complete, exact, internally consistent | **no** — a scope extension. It would close R1, R2, R3, N2 and N3 in one rule, and it is a decision |

I do not choose. The consequence that belongs with the choice: **under contract A, the canonical
state's transcription of these counts must not be read as evidence that the adjudication
directory is complete**, and today it is the only consumer.

---

## 7 · PHASE 7 — REPOSURFACE_DETERMINISM_VERDICT

Same commit, three disk states, two walkers.

| surface | `walk_publishable()` | raw `rglob` | delta |
|---|---:|---:|---:|
| clean export | 665 | 662 | −3 |
| mirror worktree (live disk) | 681 | 678 | −3 |
| **ROOT (contains every actor worktree)** | **560** | **4342** | **+3782** |

At ROOT the raw walker's extra 3782 files are `.claude/` **3598** (five other actors' worktrees),
`staging` 101, `backup` 33, `files` 32, `grants` 11 — the funding dossiers and the batch snapshots
that `unpublishable_paths()` exists to exempt. **`independent_privacy_scan.py` has no such
exemption**: run at ROOT it scans every other actor's tree. The −3 in the other rows is the
opposite sign and is correct: `walk_publishable` also yields `LICENSE`/`NOTICE`-style entries the
suffix filter skips.

### 7.1 · FINDING C-4 — BLOCKING — `walk_publishable()`'s pruning predicate is content-controlled

`is_nested_checkout(path)` is `(path / ".git").exists()`. Nothing checks that the directory is
untracked, or that the `.git` is real. Measured on a copy of the export:

```
a tracked, publishable note.md in a new directory   ->  walk_publishable sees 666 files
add a one-line file named `.git` beside it          ->  walk_publishable sees 665
raw rglob still sees the note                       ->  1 file
```

**A tracked, publishable document left the publication gate's population because a file named
`.git` appeared next to it.** Anything that can write into the repository can remove a directory
from the gate's view, and the gate reports nothing.

**Live today: no.** `git ls-files` finds **0** tracked entries named `.git`, **0** paths under a
`/.git/`, and **0** gitlinks. And `.claude/worktrees/` is gitignored (`.gitignore:72`), so at ROOT
the real worktrees are exempt twice over — by gitignore and by nested-checkout — which is belt and
braces and is why the class has never fired. The realistic trigger is not an attacker: it is a
vendored dependency, a submodule leftover, or a test fixture that ships a `.git` file.

`REPOSURFACE_DETERMINISM_VERDICT = walk_publishable() is right about the population and wrong
about how it decides it; the independent scanner does not decide it at all.`

---

## 8 · PHASE 8 — MAJOR2_A_B_COUNTEREXAMPLE_TABLE

**A** = *"commit its own work **through `CANONICAL_BATCH_COMMIT`**"* — scoped to an **act**.
**B** = *"commit its own work **to `main`**"* — scoped to a **place**.

| # | case | **A** | **B** | existing governance expectation |
|---|---|---|---|---|
| 1 | Orchestrator `WORK_COMMIT` on its own branch | **allowed** | **allowed** | § 229 makes `WORK_COMMIT` **obbligatorio** for *ogni attore*; § 186 obliges its Session Learning Review; § 278 says what is not durable did not happen. **§ 35.1 forbids it unqualified.** The body contradicts itself, and 42 commits on `orchestrator` already resolve it in practice |
| 2 | **`git commit` directly to `main`, outside any batch** | **ALLOWED by this clause** | **BLOCKED** | § 231 reserves `CANONICAL_BATCH_COMMIT` to Orchestrator at root under gates 0–5 but does not say every `main` commit must be one. Only § 35.1's *"usare la root come spazio libero"* covers it — the vaguest sentence in the perimeter |
| 3 | canonical batch of a Plan-produced candidate | allowed | allowed | § 231 — this is the permitted act. Both correct |
| 4 | Orchestrator's **own** work included in a batch | **blocked** | **blocked** | § 12 GATE 1: *"Proponente ≠ esecutore. Solo candidate preparati da Plan; **mai lavoro proprio**"*. Both correct |
| 5 | root `main` commit with no batch semantics | **ALLOWED by this clause** | **BLOCKED** | same as #2 |

**Rows 3 and 4 agree. Rows 2 and 5 are the whole difference, and they are the same failure.** An
act-scope leaves the hand commit to `main` covered only by the perimeter's loosest clause; a
place-scope names it. Row 1 is where both variants and the body disagree, and it is the
contradiction the MAJOR-2 exists to resolve.

`A ≠ B. Do not collapse them.` A is stronger on TERM_DEFINED and aligns with GATE 1's own wording;
B is stronger on TESTABILITY and on rows 2 and 5. The Operator is choosing **which question the
prohibition asks**, not which wording is better.

---

## 9 · PHASE 9 — JSONL_RECORD_PLUS_PAPER_VERDICT

Ten declared fixture classes, four scopes, the real gate.

| # | fixture | required | FILE | RECORD | +PAPER(pmid) | **+PAPER(pmid \| doi)** |
|---|---|---|---|---|---|---|
| 1 | same record linkage | BLOCK | BLOCK | BLOCK | BLOCK | **BLOCK** |
| 2 | same paper, two records | BLOCK | BLOCK | **silent ✗** | BLOCK | **BLOCK** |
| 3 | different papers | silent | **BLOCK ✗** | silent | silent | **silent** |
| 4 | same author, different papers | silent | **BLOCK ✗** | silent | silent | **silent** |
| 5 | missing PMID | see below | **BLOCK ✗** | silent | silent | **silent** |
| 6 | conflicting identifiers (2 pmids, 1 doi) | silent | **BLOCK ✗** | silent | silent | **silent** |
| 7 | DOI only, one work | BLOCK | BLOCK | **silent ✗** | **silent ✗** | **BLOCK** |
| 8 | duplicate PMID, one paper, 3 records | BLOCK | BLOCK | **silent ✗** | BLOCK | **BLOCK** |
| 9 | malformed record | fail closed | BLOCK | silent | silent | **silent ✗** |
| 10 | variant pair across different papers | silent | **BLOCK ✗** | silent | silent | **silent** |

**FILE scope is wrong on 9 of 10.** RECORD is wrong on 3. **`+PAPER(pmid | doi)` is right on 9 of
10**, and the tenth is fixture 9 — which is not a scope question but the fail-closed parse rule.

**The key must be `pmid` first, then `doi`.** Fixture 6 is the reason: two records with different
PMIDs and one shared DOI must **not** group, and a doi-first key would group them. Fixture 7 is
why `doi` must be present at all.

**Fixture 5 is the one honest gap.** Two records with no publication identity: I marked "silent"
and the truth depends on a rule nobody has written. The cleaner reading is that in a corpus whose
schema carries `pmid` in **706 of 706** records, a record without one is malformed by the schema
and belongs to fixture 9's fail-closed path — which removes the judgement rather than making it.

Live tree: `+PAPER(pmid|doi)` is **verdict-identical** to today (494 / 489 / 5) and recovers the
same suppressed `fulltext_read_receipts.jsonl:83`. On today's data the paper unit and the record
unit coincide — the corpus seed is **706 records → 706 paper groups, 0 groups with more than one
record** — so the grouping costs nothing now and is what stops fixture 2 the day a second record
per paper arrives. The read-receipts ledger already has that shape.

`JSONL_RECORD_PLUS_PAPER_VERDICT = RECORD + PAPER(pmid|doi), 9/10, verdict-neutral live.
No public-bibliography policy is decided here.`

---

## 10 · PHASE 10 — PRIVACY_MINIMUM_HUMAN_DECISIONS

I tried to reduce below two and could not. The audit:

| | **A** Operator identity in scope? | **B** public corresponding-author emails? | **C** ORCID |
|---|---|---|---|
| `NORMATIVE_CONFLICT` | **yes** — `CLAUDE.md` excludes the individual-level clinical record and is silent on the Operator; the digest sets list the Operator's token beside the case-identifier tokens. Two normative statements, not one rule with a gap | **yes** — published bibliographic metadata versus a bulk-republished contact channel. Neither side is derivable from the other | **no** — see below |
| `MECHANICAL_CONSEQUENCE` | the derived path rule and the pseudonymisation shape are both mechanical **once A is answered** | none: the field path is already known and exact | none |
| `LIVE_FINDING_COUNT` | 57 (→ 59 under the derived rule) path + 16 non-path, 14 after the derived rule | **430** in one field path | **480** in `.authors[].identifiers.ORCID`, in 139 of 706 records |
| `BLOCK_DELTA` | up to 59 gate blocks | **301 → 56** | 0 today (invisible to both scanners) |
| `SCIENTIFIC_PROVENANCE_COST` | none either way — no analysis keys on the Operator | none — recoverable from PubMed by PMID | none |
| `PRIVACY_COST` | the contradiction itself | a deliverable channel, republished as a set | a permanent resolvable identifier |

**C stays conditional and cannot be promoted or removed.** The implication runs one way: permit
the emails and ORCIDs are permitted *a fortiori* (an identifier is weaker than a deliverable
address); block them and C opens, because closing contact channels while permitting identifiers is
a coherent position. So C is a decision **only in one branch of B**, which is the strongest
reduction available without deciding B.

`PRIVACY_MINIMUM_HUMAN_DECISIONS = 2 (+1 conditional). No further reduction is available: both
roots are conflicts between normative statements, and mechanical work cannot adjudicate those.`

---

## 11 · PHASE 11 — COMPOSED_INTEGRATION_VERDICT

Six candidates merged onto `main` in order: RELSURF → GOVTESTS → ADJFAILCLOSED → APQCONS →
P7LEDGER → ORCHMAJOR2-A.

**Under git's default merge, four of six conflict** — all on `scripts/run_release_regressions.py`,
all inserting after `test_regenerate_adjudications.py`. Only RELSURF (first) and ORCHMAJOR2 (which
does not touch the runner) merge cleanly.

Under a `merge=union` driver on that one file, **all six compose cleanly**:

| composed measure | value |
|---|---|
| inventory entries | **71** (unique 71 — **0 duplicates**) |
| tracked test files | **71** |
| unenrolled tracked suites | **0** |
| shebang entrypoints without `+x` | **0** |
| release runner | **`FAIL` — 5 test cases** |

**The five are exactly the pre-existing router-migration assertions** (`verbatim_locators`,
`pubmed_corpus_harvest`, `FULLTEXT_READ_RECEIPT`, `state-control`, `session_self_evaluation.md`).
**No new failures, no hidden failures, no mode-bit regression, no test whose own file violates a
repaired rule.** Every candidate that adds a suite ships it `100755`, which closes the hole I
flagged as *closed by accident*: `cba499a` on ADJFAILCLOSED sets the mode bit explicitly and its
commit message names the guard.

The one composition hazard is the runner conflict. Its most likely hand-resolution — take one
side — drops enrollments, and `test_every_tracked_test_file_is_in_the_runner` catches exactly
that. **The guard RELSURF re-greens is the guard that protects the composition of the other five.**

`COMPOSED_INTEGRATION_VERDICT = COMPOSES CLEAN; residual is the pre-existing router set; one
declared merge hazard on a single file, caught by an existing check.`

---

## 12 · PHASE 12 — NEW_GOVERNANCE_REQUIRED

| principle | `EXISTING_NORMATIVE_TEXT` | `EXECUTABLE_GAP` | `ACTUAL_NEW_POLICY_REQUIRED` |
|---|---|---|---|
| **1 · cwd-independent control-plane resolution** | § 14 `ONE_WRITER_PER_WORKING_DIRECTORY` — *"mai due attori abilitati alla scrittura sulla stessa directory. Critico nella root"*; Annex I already names `REPO_ROOT` **and** `WORKTREE_ROOT` as distinct per-machine values | 2 of 6 readers resolve a relative default against the cwd; 5 of 6 never print the surface; the singleton answer changes with the directory | **NONE.** The concepts and the one-writer rule already exist. What is missing is executable: an explicit root argument and a printed surface line. That is a repair |
| **2 · current divergence prevents a definitive gate assertion** | § 278 *"ciò che non è nello stato durevole non è accaduto"*; § 301 *"messaggi = pointer, stato durevole decide"* | three live lineages of the approval queue across 72 refs, and nothing separates a live actor branch from `refs/tags/snapshot/pre-CAND-…` | **YES, exactly one:** *which refs constitute the durable state for a control-plane question.* § 4's `NORMATIVE_RELEVANCE_BOUNDARY`. It cannot be derived, and the candidate derivation is broken on `main` today |
| **3 · validation population independent of machine-local nested state** | none normative — but the lesson is already **executable**: `walk_publishable()`'s docstring records the 37-false-BLOCK measurement, and `test_no_closed_world_assertions_on_live_state.py` pins the general form | 3782-file divergence at ROOT between the two walkers; the nested-checkout predicate is content-controlled | **NONE.** Both are repairs to code that already encodes the intent |

**One new policy across three principles. The other two are repairs, and calling them governance
would inflate a fix into a constitution.**

`NEW_GOVERNANCE_REQUIRED = 1` — the ref-relevance boundary of § 4.

---

## 13 · Verdicts

`P0_CONTROL_PLANE_DETERMINISM_VERDICT = NOT MET.` The same control-plane question returns three
different answers from three directories, one of them the invariant a tool exists to guarantee;
the answers do not carry the surface they came from; and the ref set that constitutes "the current
state" is undefined.

**Nothing here is a retraction of what the candidates achieved.** RELSURF re-greens the guard that
protects the whole composition. ADJFAILCLOSED closed 5 of 8 prior false passes, the zero-coverage
family and the counter defect, and moved its suite to the real script. APQCONS fixed the syntax-error
exit path and the malformed-timestamp ordering. The composed tree adds no new failure. None of that
makes a gate out of a tool that still passes green while checking less.

## 14 · WHAT_WOULD_CHANGE_MY_MIND

- **§ 1.1** — if `runtime/` is not control-plane state but per-worktree scratch, the lease
  divergence is by design and C-1 collapses. Test: find the normative sentence that says which
  copy of `runtime/orchestrator_lease.md` is authoritative. I searched and found none — which is
  § 4's finding again, one artefact over.
- **§ 5** — if `write` is never run except immediately before a `verify` in the same session,
  R1, N2 and N3 are unreachable in practice and drop to hardening notes. Test: find a procedure
  that runs `write` and stops.
- **§ 7.1** — if `is_nested_checkout` is intended to prune on the *filename* rather than on being
  a real checkout, C-4 is a documentation gap, not a defect. Test: find the decision record.
- **§ 9 fixture 5** — if a record with no `pmid` is legitimate in a governed corpus, my
  "malformed by the schema" reading is wrong and fixture 5 needs a real answer.
- **§ 11** — I composed in one order. A different order could expose an ordering-dependent
  defect I did not see; the union driver hides textual conflicts that a human would resolve by
  hand, and I did not measure the hand-resolution.

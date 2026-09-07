---
record_type: WORK_ANALYSIS
record_id: PLAN-EXECUTABLE-REPAIR-PREPARATION-001
task_id: PLAN_EXECUTABLE_REPAIR_PREPARATION_v1
title: Three suites that can fail, a 2×2 that separates two decisions everyone was treating as
  one, and a queue that is three deep rather than nineteen
author: plan
session_ref: evidence-index-87 [15b5f9]
authored_on: 2026-08-26
dispatcher: operator
governance_version: 3.1.1 — read and cited, NOT exercised and NOT modified
mode: PREPARATION + EXECUTION OF DECISION-NEUTRAL REPAIRS

STATUS: ANALYSIS_COMPLETE — three test suites landed, no gate behaviour changed
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none

classification:
  - EXECUTABLE REPAIR PREPARATION + CANONICALIZATION QUEUE
  - NOT GOVERNANCE · NOT A PROTOCOL · NOT A DECISION · NOT A COMMIT CANDIDATE
  - NOT AN ACTIVATION — no `status:` line is changed by this record
  - NOT A DISPATCH — no actor is assigned work here
  - DECISION-NEUTRAL on §P7 normativity, on EG-02, and on whether `43cf690` stands

relation_to_prior: >
  CONTINUES and does not re-derive PLAN-EXECUTABLE-GOVERNANCE-GAP-MAP-001 (EG-01…EG-17, the
  READY_QUEUE Q-1…Q-9, the §P7 readiness package). CONSUMES
  PLAN-MIRROR-V3-MINIMUM-REPAIR-CONSOLIDATION-001 (M3-1…M3-15 and its § 8 no-change list),
  PATHOGRAPH-TRANSPORT-CONSOLIDATION-001, PREP-20260820-ORCHSURF-REV4,
  AUTHOR-RESPONSE-ROLES-MIRROR-001 and PREP-20260822-ROLE-CONTRACT-REPAIR. SUPERSEDES NONE.
  It CORRECTS three inherited figures and one inherited claim, each named at § 0.4.

domain: >
  CONTENT for this file. `learning/` matches no declared CONTROL_PLANE_ROOT prefix
  (plan_defined_parameters.md § P5.1) and P5.1 states `learning/` is content by intent. The
  companion commit also touches `framework/scripts/`, `governance/scripts/` and `scripts/`, all
  content by the same rule. Nothing under `governance/candidates/`, `ledger/`, `reviews/`,
  `roles/` or `runtime/` is written on any ref.

personal_data: none introduced. The human role is `the Operator` throughout.
---

# Two of the five gates never discriminated between the options, and nobody had run them on the same tree

> **Nothing here is medical advice.** Disease-level only; no individual-level record.
> **Nothing here is canonical.** This is Plan work-analysis. It originates no actor, no control
> plane, no schema, no annex and no threshold. It answers **no** H.1 question and **selects no
> option** on any open determination.

---

## 0 · OBSERVATION_SCOPE

### 0.1 · Derivation surface

| Fact | Value | How established |
|---|---|---|
| Derivation window | `2026-08-26T06:20Z → 07:05Z` | `datetime.now(timezone.utc)` |
| Session | `evidence-index-87 [15b5f9]` | its own `ListAgents` output, in which its name is absent |
| Read surface | worktree `.claude/worktrees/evidence-index`, branch `plan-orchsurf-r4-transcription` @ **`90f08a4`** | `git rev-parse` |
| 🔴 Write surface | a **separate worktree**, branch `plan-exec-repair-prep`, cut from `90f08a4` | § 0.3 — this is not a formality |
| Divergence vs `main` | **2 behind, 63 ahead** at `90f08a4` | `git rev-list --left-right --count main...HEAD` |
| `main` | **`788c357`**, 2026-08-22 | `git rev-parse main` |
| Ref population | **45 `refs/heads`** — 44 before this session, plus the one this session created | `git for-each-ref` |
| Worktree population | **14** entries, from this checkout | `git worktree list` |
| Sweep positive control | `CLAUDE.md` present on **45 of 45** heads | required before any ref-level negative below |
| `legend_lint.py .` | **PASS**, exit 0 | run on the read tree |
| `growth_anchors.py check` | **PASS** — claims 39 · papers 70 · corpus 356 · literature 390 · unread_premises 4 | run on the read tree |
| `lease_state.py` | **ACTIVE by derivation: 0**, 5 records visible from this ref | run on the read tree |
| `public_release_gate.py` at `90f08a4` (clean extraction) | 🔴 **BLOCK_PUBLICATION · BLOCKS 1 · exit 2** | `git archive` into scratch |
| Working tree at open | **2 dirty entries**, both another session's, neither touched here | `git status --porcelain` |

**The read tree and the write tree are different on purpose.** `ListAgents` shows a peer,
`evidence-index-78 [140f81]`, holding the same working directory, and the two dirty entries are
its in-flight work. EG-04 records what happened the last time two sessions shared this directory.
Rather than negotiate a seat in chat — the mechanism EG-04 exists to criticise — this session took
`git worktree add -b plan-exec-repair-prep`, wrote only there, and touched neither dirty file.

### 0.2 · What I could NOT reach — declared, not inferred

- **`main`'s two extra commits.** Not read this session. No finding below depends on them.
- **The gitignored corpus.** `files/` is per-worktree. One of the three adjudication source PDFs
  (`PMID16061658`) is absent here, which is why the live `regenerate_adjudications.py verify`
  exits 1 in this checkout; every fail-open arm at § 3 is measured on synthetic fixtures instead,
  so the finding does not depend on which PDFs happen to be on this disk.
- **Any biological proposition.** Nothing scientific was adjudicated, no current file was opened
  for writing, no receipt was written, no PMID was read.
- **`runtime/agent_card_registry.md`** exists on **1 of 45 heads** (`orchestrator`); positive
  control `runtime/orchestrator_lease.md` on **24 of 45**. It was read out-of-tree via `git show`.

### 0.3 · One measurement method that inflated a count, caught by comparing two instruments

The prior record measured the release suites on clean `git archive` extractions. That method adds
a failure that is not in the repository: `scripts/test_release_runner_verdict.py` shells out to
`git ls-files`, and an extraction is not a git repository, so it errors with
`CalledProcessError … exit status 128`. **Six failures in a clean archive are five failures in a
git working tree**, and the sixth is the measurement. Every count below is stated with the method
that produced it.

### 0.4 · Four inherited figures corrected, and one inherited claim narrowed

**Each was re-derived rather than accepted, and each correction changes something.**

| # | Inherited | Measured here | Why it matters |
|:--:|---|---|---|
| 1 | EG-15's introducing commit is `43cf690` | 🔴 **`702df73`** — `43cf690~1`. `43cf690~2` is clean, `43cf690~1` is already red, `43cf690` inherits it | the terminal-choice question at § 2 is about a different commit than the regression |
| 2 | *"Two release suites are red"* | 🔴 **three surfaces**: the publication gate, `scripts/test_documented_commands.py` **and** `scripts/test_fresh_clone_reader_journey.py` | the third was named in a peer session's addendum; confirmed independently here |
| 3 | *"19 scientific candidate commits"* | 🔴 **3**. Sixteen of the nineteen files carry `Status: committed`, all consumed by `BATCH_20260815_001` at `749a9a9` | the queue a restored Orchestrator faces is three deep, not nineteen |
| 4 | § 4.4: *"REVERT all three → LINT PASS, ratchet PASS"* | correct **and incomplete** — the same arm is **red on the release surface**, because reverting lands on `702df73` | it could be read as "full revert lands green". It does not; § 2.4 |
| 5 | *"`rechain` is the consolidator primitive"* | 🔴 **narrowed**. `rechain --onto` rebases one ledger onto a **divergent copy of the same stream**. §P7's consolidation merges **N distinct per-actor streams**. The claim is right for M2.1 and overstated for S4 | § 6 |

### 0.5 · What this pass mutated

Two acts, both on `plan-exec-repair-prep` and nowhere else: **commit `c095c5d`** (three test
files, four executable-mode changes, three lines added to the release inventory) and **this file**.
No canonical file was opened for writing. No `status:` line anywhere was changed. No `ledger/`,
`runtime/`, `governance/candidates/`, `reviews/` or `roles/` path was written on any ref. No lease
was acquired. No gate's blocking behaviour was changed.

---

## 1 · MAJOR-2 — the restricted producer package

### 1.1 · What was authorized, and what a producer may therefore do

The dispatch names the authorized semantic delta as exactly two edits and adds *"do not import the
rest of ORCHSURF rev 4."* Producing a candidate object is Plan's own function; approving it,
committing it canonically, or writing it to `main` is not. **This section produces the object, its
hashes and its consistency consequences. It approves nothing and lands nothing.**

### 1.2 · BASE_HEAD, verified rather than assumed

```
BASE_REF          main = 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5   (2026-08-22)
BASE_OBJECT       main:roles/orchestrator.md
BASE_BLOB_OID     2bbb214143df255ea6c366890a06b3687ee4c89e
BASE_BYTES        4777          BASE_LINES 90
BASE_SHA256       e1155911681d8bb0d1d7756ba6737eadca80b5d1a19b13cac381e7022dc4a504
```

🔴 **The base hash has an independent positive control.** `runtime/agent_card_registry.md` on the
`orchestrator` ref declares `ROLE_CONTRACT_HASH: e1155911…` for this actor, and that value equals
the SHA-256 of `main:roles/orchestrator.md` computed here. The hash recipe is therefore
**confirmed against a record written by another actor**, not inferred from the tool that produces
it. `PREP-20260822-ROLE-CONTRACT-REPAIR` independently cites the same object at blob `2bbb2141`.

### 1.3 · The delta, and the one presentational fork the dispatch does not settle

The two authorized edits touch line 5 and line 46 and nothing else. The qualifier is given in the
dispatch as plain text; the already-prepared revision 4 renders it in bold. **Both are produced and
both are hashed, because the difference is presentational and choosing it silently would put a byte
into a governed object on this session's taste.**

| Variant | Line 5 | Line 46 qualifier | bytes | SHA-256 |
|---|---|---|:--:|---|
| BASE | `worktree: the repository root checkout` | absent | 4777 | `e1155911…c4a504` |
| **A** *(recommended)* | `worktree: orchestrator` | bold, as revision 4 already renders it | 4790 | **`d5759d13da45fdd717fe159f91f9d6fb102788419c3459a5dfff535e7e8b1d8f`** |
| B | `worktree: orchestrator` | plain, as the dispatch writes it | 4786 | `fce1ff9e06811a5ac4bc62a56c590a6abc12fdfe727e4d9370a4b483969827bc` |

**A is recommended** because it makes the restricted candidate's clause **byte-identical** to the
clause in the revision already carried on two heads, so the restricted object is a strict subset of
that text rather than a third wording of the same repair. **The choice is one byte of emphasis and
it is recorded, not taken.**

**Reproduction recipe — a hash without a recipe is an attestation.** From any checkout:

```
git show main:roles/orchestrator.md > base.md
sed -e '5s|^worktree: the repository root checkout$|worktree: orchestrator|' \
    -e '46s|^\*\*Orchestrator must not:\*\* commit its own work;|**Orchestrator must not:** commit its own work **to the canonical surface**;|' \
    base.md > variant_A.md
shasum -a 256 base.md variant_A.md
diff base.md variant_A.md      # must report exactly two changed lines
```

`diff` reports **2** changed lines for A and **2** for B. Line count is unchanged at 90.

### 1.4 · No hidden inheritance — a sweep with three controls that fire

Revision 4 as carried on `plan-orchsurf-r4-transcription` is **188 lines**; the restricted variant
is **90**, the same as the base. Token sweep, each probe chosen because it exists in revision 4:

| Probe | restricted A | revision 4 | base |
|---|:--:|:--:|:--:|
| `session_home` | **0** | 2 | 0 |
| `canonical_batch_surface` | **0** | 1 | 0 |
| `Four concepts` (the added section heading) | **0** | 2 | 0 |
| `2026-08-20` (the quoted operator adjudication) | **0** | 1 | 0 |

**Four probes, four positive controls, four zeros in the restricted object.** Nothing of revision
4 beyond the two authorized edits is present.

### 1.5 · Negative / mutation arm — proving the repair changes something

A checker asking only the two questions MAJOR-2 raises, run over five trees:

| Arm | findings | which |
|---|:--:|---|
| BASE (`main`, unrepaired) | **2** | worktree field names the wrong surface; the prohibition forbids the mandatory `WORK_COMMIT` |
| restricted **A** | **0** | — |
| restricted **B** | **0** | — |
| MUTATION half-1 — worktree edit only | **1** | the prohibition |
| MUTATION half-2 — clause edit only | **1** | the worktree field |

**The two halves discriminate.** A pair of arms that both passed would be consistent with a checker
that never fails; the two half-repairs prove each edit carries exactly one of the two findings, so
the repair is not one change wearing two names.

### 1.6 · The consistency update to the Agent Card registry — and a field that is stale before MAJOR-2 touches it

The card lives on **1 of 45 heads**. Computing its three affected fields:

```
WORKTREE:            the root checkout   # branch main      ->  orchestrator
ROLE_CONTRACT_HASH:  e1155911…c4a504                        ->  d5759d13…8b1d8f   (variant A)
FINGERPRINT:         6b55605d…7d349f                        ->  see below
```

🔴 **`ROLE_CONTRACT_HASH` is ref-independent here and `FINGERPRINT` is not.** The contract file is
byte-identical on `main` and on `orchestrator`, so the first substitution is unambiguous. The
fingerprint is a composition over that ref's whole pertinence set, and it is different on the two
refs **before any edit**:

| Computed at | orchestrator fingerprint, BASE contract | with restricted A | other three roles |
|---|---|---|---|
| `main` @ `788c357` | `88dea7a635919c9f…c07b2a5ebb` | `27383f3e5a7880ef…d649640274` | **unchanged** |
| `orchestrator` ref | `e2c544705e623a77…8a0e8baaec59a` | `fbc380142f0e43da…5d2ba14ea422df8` | not recomputed |
| **the card declares** | `6b55605d6f712d6c…f41b147d349f` | — | — |

**The declared value matches neither ref today**, with the base contract in place. So the card's
fingerprint is already stale for a reason that has nothing to do with MAJOR-2: its inputs moved
after 2026-08-17. **Writing a single new number into that field would be fabricating a
measurement.** The lawful shape is to recompute at the ref where the update lands, at the moment it
lands, and to record which ref that was.

**Negative control on the fingerprint delta, and it is the strongest line in this section.** With
restricted A swapped in at `main`, `mirror`, `plan` and `scientist` are **byte-identical** to their
pre-edit values while `orchestrator` moves. The change is scoped to exactly one role's pertinence
set, which is what a correct role-contract edit must do and what nothing had checked.

### 1.7 · The terminal choice this package does not decide

`DEC-20260820-ORCH-SESSION-HOME` is the record that settles the repair *direction*.
`PREP-20260820-ORCHSURF-REV4` declined to build on it because it carried `ratified_by: ""`.

🔴 **It is now ratified — `ratified_by: Operatore, 2026-08-20` — and it is absent from `main`.**
Measured across all heads with a positive control: present on **3 of 45**
(`orchestrator-surface`, `plan-orchsurf-r4-transcription`, and this session's own branch, which
inherited it); positive control `governance/GOVERNANCE_v3.1.1.md` on **30 of 45**.

So the restricted candidate rests on a ratified operator decision **that does not exist on the
branch the repair is for**. That is EG-10 with a name, and it is a genuine terminal choice:

```
T-1  land the restricted contract edit and let the decision reach main later
T-2  route the decision to main first, then the contract edit
T-3  carry both in one candidate
```

**Described, not selected.** Each is executable; the difference is what a reader of `main` can
reconstruct afterwards, and that is a provenance judgement belonging to the Operator.

---

## 2 · EG-15 and the `43cf690` terminal choice — measured as a 2×2, because they are two questions

### 2.1 · Why the regression is red at HEAD

Re-derived on four clean extractions, all four gates run in place:

| Clean tree | LINT | ratchet | publication gate | documented commands |
|---|:--:|:--:|---|:--:|
| `e4aa80c` = `43cf690~2` | PASS | PASS | **PASS · BLOCKS 0 · exit 0** | **exit 0** |
| **`702df73`** = `43cf690~1` | PASS | PASS | 🔴 BLOCK · BLOCKS 1 · exit 2 | 🔴 exit 1 |
| `43cf690` | PASS | PASS | 🔴 BLOCK · BLOCKS 1 · exit 2 | 🔴 exit 1 |
| `90f08a4` = HEAD | PASS | PASS | 🔴 BLOCK · BLOCKS 1 · exit 2 | 🔴 exit 1 |

**`702df73` introduces it. `43cf690` inherits it.** The prior record's control pair was
`43cf690~2` versus `43cf690`, which is a correct before/after for *the regression* and an incorrect
attribution to *the commit*. The intervening commit is the one that tracked twelve Plan records.

**Three surfaces, not two.** Running the whole inventory rather than the two suites already named:

```
clean e4aa80c   6 failures   (5 real + test_release_runner_verdict.py, the archive artifact of § 0.3)
clean 90f08a4   8 failures   (the same 6, plus test_documented_commands.py
                              and test_fresh_clone_reader_journey.py)
```

The delta between the baseline and HEAD is **exactly two suites**, and the publication gate is a
third surface outside the inventory. All three fire on the same file for the same reason: a document
that reports an absence is matched by the guard that looks for the thing absent.

### 2.2 · The repair exists, is sufficient, and is uncommitted

The peer session's two dirty files carry the text repair. Applied to a clean extraction of HEAD in
scratch — the working tree itself untouched — the full inventory returns **6 failures, identical to
the `e4aa80c` baseline, with no seventh**. The publication gate returns **PASS · BLOCKS 0 · exit 0**.

🔴 **It is uncommitted, so at HEAD the repair does not exist.** CI reads what is committed. This
session did not commit another session's files: that is the § 4.4 defect of the prior record,
performed deliberately rather than by accident, and it is not improved by knowing about it.

### 2.3 · The terminal-choice table

Every cell run this session, on a purpose-built tree, gates executed in place.

| | LINT | RELEASE_REGRESSION | RATCHET | OTHER_GATES (publication) | SEMANTIC_COST |
|---|:--:|:--:|:--:|:--:|---|
| **KEEP** — `43cf690` stands | **PASS** | 🔴 RED — 2 suites | **PASS** | 🔴 BLOCK ×1 | none |
| **FULL_REVERT** — the three files reverted at HEAD | **PASS** | 🔴 RED — the same 2 suites | **PASS** | 🔴 BLOCK ×1 | an 834-line analysis whose authorship is unrecoverable ceases to exist |
| **PARTIAL_REVERT** — keep the crosswalk, revert the queue entries | 🔴 **BLOCK_BATCH_COMMIT** | 🔴 RED | 🔴 **BLOCK — `RATCHET_VIOLATION: 1 new unread premises (27845895)`** | 🔴 BLOCK ×1 | manufactures a gate failure that no arm of the real decision has |

**Two terminal states genuinely pass the gates that discriminate, and neither is unsafe.** KEEP and
FULL_REVERT are indistinguishable on all five columns; they differ only in the last, and that column
holds a cost, not a failure. Calling either unsafe would mislabel one of the Operator's two options.

### 2.4 · 🔴 The 2×2 that separates the two questions

The table above shows both live arms red on the release surface, which invites the wrong conclusion
that the `43cf690` decision has something to do with it. **It does not**, and the way to show that
is to vary both factors rather than one:

| tree | LINT | ratchet | publication | doc-commands | fresh-clone |
|---|:--:|:--:|:--:|:--:|:--:|
| HEAD as-is (KEEP, no EG-15 repair) | 0 | 0 | 🔴 2 | 🔴 1 | 🔴 1 |
| HEAD + EG-15 repair (KEEP) | 0 | 0 | **0** | **0** | **0** |
| HEAD + full revert of `43cf690` | 0 | 0 | 🔴 2 | 🔴 1 | 🔴 1 |
| HEAD + full revert + EG-15 repair | 0 | 0 | **0** | **0** | **0** |

**The EG-15 repair is necessary and sufficient for all three red surfaces in both arms, and the
`43cf690` decision moves nothing.** The two questions are orthogonal, and the cell that proves it is
the fourth — the one a single-variable comparison never builds. Whoever answers H-8 does not have to
wait for EG-15, and whoever clears EG-15 does not have to wait for H-8.

---

## 3 · `regenerate_adjudications.py` — the fail-open surface, reproduced independently

### 3.1 · Method, and why the number "four" was not inherited

Fourteen arms, each a synthetic repository root with the module's `ROOT` and `ADJUDICATIONS`
rebound and a one-page PDF generated in the fixture, so the real digest path runs. Nothing reads
this repository's corpus. **The count below was derived by enumerating code paths first and then
mounting an input for each**, not by confirming a reported total.

### 3.2 · The matrix

| INPUT | CODE_PATH | EXPECTED | ACTUAL | EXIT | OUTPUT | FALSE_PASS | SILENT_DEGR. | AMBIG. | FAIL_CLOSED |
|---|---|---|---|:--:|---|:--:|:--:|:--:|:--:|
| VALID_BASELINE | full loop | PASS | PASS | 0 | `OK: 1 …` | — | — | — | n/a |
| ZERO_COVERAGE — empty directory | `recipes()` → `[]` | BLOCK | **PASS** | **0** | `OK: 0 adjudication artifact(s)…` | ✅ | ✅ | — | ❌ |
| ZERO_COVERAGE — directory absent | `glob` on a missing path | BLOCK | **PASS** | **0** | `OK: 0 …` | ✅ | ✅ | — | ❌ |
| ZERO_COVERAGE — recipe with `artifacts: []` | inner loop never runs | BLOCK | **PASS** | **0** | `OK: 0 …` | ✅ | ✅ | — | ❌ |
| MISSING_DIGEST | `declared is None` branch | BLOCK or NOT_CHECKED | **PASS** | **0** | `no digest declared, produced …` **then** `OK: 1 … regenerate to their declared digest` | ✅ | ✅ | ✅ | ❌ |
| MUTATED_DIGEST | `produced != declared` | BLOCK | BLOCK | **1** | `regenerated to … recipe declares …` | — | — | — | ✅ |
| MISSING_MANIFEST — key absent | `snippets()` → `None` | NOT_CHECKED, declared | NOT_CHECKED, declared | 0 | `no manifest declared — …` | — | ✅ *(by design)* | — | n/a |
| MISSING_MANIFEST — declared, file absent | `path.exists()` → `None` | BLOCK | **PASS** | **0** | 🔴 `no manifest declared` — **false about the recipe** | ✅ | ✅ | ✅ | ❌ |
| MISSPELLED_MANIFEST_PATH | same branch | BLOCK | **PASS** | **0** | 🔴 the same false line | ✅ | ✅ | ✅ | ❌ |
| EMPTY_INPUT — zero-byte recipe | `json.loads` | verdict | **traceback** | 1 | `JSONDecodeError`, no verdict line | — | — | ✅ | ⚠️ |
| EMPTY_INPUT — `{}` | `recipe["source_pdf"]` | verdict | **traceback** | 1 | `KeyError: 'source_pdf'` | — | — | ✅ | ⚠️ |
| PARTIAL_INPUT — no `artifacts` key | digest check fires first | verdict | BLOCK | 1 | digest mismatch — **the right verdict for the wrong reason** | — | — | ✅ | ✅ |
| SELECTOR miss — `--pmid 99999999` | `if only and pmid != only` | BLOCK | **PASS** | **0** | `OK: 0 …` | ✅ | ✅ | — | ❌ |
| SELECTOR typo — one digit short | same | BLOCK | **PASS** | **0** | `OK: 0 …` | ✅ | ✅ | — | ❌ |

**DOWNSTREAM_CONSUMER for every row is the same and it is the reason the count matters:**
`regenerate_adjudications.py verify` is invoked by **no gate**. `scripts/run_release_regressions.py`
carries its unit suite, never the command. So today each false pass is latent; the moment Q-5 wires
`verify` in, every row above becomes a green line in the release inventory.

### 3.3 · Counting, with the definition stated

```
distinct code paths that return 0 on an input that verified nothing   4
  F1  zero recipes / absent directory / zero artifacts   -> "OK: 0"
  F2  a --pmid selector matching no recipe               -> "OK: 0"
  F3  an artifact with no declared digest                -> counted as verified
  F4  a declared manifest that will not open             -> reported as undeclared

arms realising them                                                   8 of 14
declared degradation, printed, not a false pass                       1  (no manifest key)
ambiguous status — non-zero exit with no verdict line                 2  (malformed JSON)
correctly fail-closed                                                 3
```

**FALSE_PASS_COUNT = 4** under the definition *"a distinct code path that exits 0 on an input where
nothing was verified."* Under the looser definition *"an arm that exits 0 when it should not"* the
number is 8. Both are stated because the two are quoted interchangeably and they are not the same
quantity.

### 3.4 · 🔴 The stale figure: how a green line reports 27 after verifying fewer

**Source.** `checked += 1` executes for every artifact **before** the branch that decides whether a
digest was compared. The summary is built from `checked`.

**Propagation.** The summary sentence asserts that all `checked` artifacts *"regenerate to their
declared digest"*. On a fixture of three artifacts with one `sha256` removed:

```
p01  OK <digest>
p02  no digest declared, produced <digest>      <- never compared to anything
p03  OK <digest>
OK: 3 adjudication artifact(s) regenerate to their declared digest, and 3 locator(s) …
```

**Two were compared. The line says three.** On the live recipes the population is **3 recipes · 27
crop artifacts · 47 adjudicated locators** — re-derived statically from the tracked JSON here, and
identical to the figure the prior consolidation reports. So **27 is `checked`**, and it survives the
removal of the verification it summarises. The same holds for **47**, which is incremented whether
or not the manifest was readable.

**Two further stale channels, measured:**

- `write` persists the image at the write step, which precedes the digest comparison. A **failed**
  `write` leaves a 9 539-byte PNG on disk and then exits 1.
- `verify` **re-renders** and never opens the file on disk. Overwriting a crop with the bytes
  `THIS IS NOT THE ADJUDICATED CROP` and re-running yields **exit 0**.

Together those two are one chain: **a failed write leaves an artifact, and no verification ever
looks at it again.** A reader inspecting the PNG is inspecting something no gate has compared to the
recipe.

### 3.5 · The minimum coherent repair, prepared as an executable specification

`PLAN-MIRROR-V3-MINIMUM-REPAIR-CONSOLIDATION-001` § 8 item 4 says *"no rewrite of
`regenerate_adjudications.py`"*, and item 7 says fail-closed behaviour on absent evidence stands.
**Neither is contradicted by the guards below and neither authorises this session to land them**:
changing what a verdict blocks on is the § 250 doubt-rule class, and it routes through a reviewer.

So the repair is delivered as `framework/scripts/test_regenerate_adjudications_coverage.py`, in
which each guard is one `expectedFailure` arm — the specification in the only form that cannot drift
from what it specifies:

| Guard | Arm asserts |
|---|---|
| G1 zero coverage → non-zero exit | three arms: empty directory, absent directory, zero artifacts |
| G2 selector matching nothing → non-zero exit | one arm |
| G3 missing declared digest under `verify` → `NOT_CHECKED`, distinct from PASS | one arm, plus the summary-count arm |
| G4 declared-but-unreadable manifest → BLOCK, with a message about the file and not about the recipe | one arm; the current false message is pinned separately as an observation |
| G5 malformed recipe → a reported failure, not a traceback | two arms |
| G6 `write` does not persist an artifact whose digest disagrees | one arm |
| G7 `verify` notices a stale on-disk artifact | one arm |

**The negative arm that makes the suite evidence.** Applying G1 alone to a scratch copy turns two
`expectedFailure` arms into **unexpected successes** and the run **red**. The suite therefore cannot
outlive the defect it documents — which a characterization test asserting `return 0` would have
done, by locking the defect in as the expected behaviour.

Measured: **18 tests · 7 pass · 11 expected failures · exit 0** before the guard;
**failed (expected failures 9, unexpected successes 2)** after it.

---

## 4 · `activation_state` — feasibility, and the exact frontier

### 4.1 · The population

**30 files** under `governance/`, `roles/`, `framework/protocols/`, `runtime/` and `ledger/` carry a
`status:` line. The values in use are `FROZEN` (11), `PROPOSED` (9, each with a different trailing
condition), `BINDING_UPON_OPERATOR_RATIFICATION` (2), and one each of `DRAFTED`, `COMPLETE`,
`REVIEWED`, `ACCEPTED`, `BINDING`, `PREPARATION`, `TAKEN UP`.

### 4.2 · Does the proposed vocabulary exist in normative text?

Swept with `git log --all -S'status: <V>'` over every `.md`, 45 heads:

| State | commits | Verdict |
|---|:--:|---|
| `PROPOSED` | 61 | ✅ in use |
| `BINDING` | 13 | ✅ in use |
| `REVIEWED` | 2 | ✅ in use, once |
| `ACTIVE` | 6 | ⚠️ **every hit is prose discussing the value**, in `learning/` and one decision record. Not a declared status of any object |
| `APPROVED` | **0** | ❌ absent |
| `STALE` | **0** | ❌ absent |
| `INVALIDATED` | **0** | ❌ absent |
| `UNDERIVABLE` | **0** | ❌ absent |
| *(controls)* `FROZEN` 19 · `ACCEPTED` 8 | | the sweep fires |

**Three of eight exist. One is an artefact of the instrument. Four are absent from every ref.**
Introducing them would be **originating vocabulary**, which is policy.

🔴 **And the `ACTIVE` row is the finding, not a footnote.** A string search cannot distinguish a
frontmatter declaration from a sentence *about* one — which is the same class as the guards at § 2
firing on a document reporting an absence. Any derivation must parse frontmatter, never grep.

### 4.3 · Per-state analysis

| State | SOURCE_OF_TRUTH | DERIVATION_RULE | AMBIGUITY | FAILURE_BEHAVIOR |
|---|---|---|---|---|
| `PROPOSED` | the object's own frontmatter | literal read | the trailing condition is prose and varies per object | absent field → `UNDERIVABLE` |
| `REVIEWED` | a review artifact naming the object | file presence + a verdict field | 🔴 **the verdict vocabulary does not conform** — EG-03 measures 0 of 10 conforming. **This atom is UNMEASURABLE until P-8** | must not guess |
| `APPROVED` | an approval artifact naming the object | file presence | not a declared status anywhere; only ever a *condition* | — |
| `ACTIVE` / `BINDING` | 🔴 **nothing** | — | no object declares itself active; `DEC-20260822` states the act has no form | — |
| `STALE` / `INVALIDATED` | 🔴 **nothing** | — | absent from all 45 refs | — |
| `UNDERIVABLE` | the derivation itself | the residual class | it is the tool's own vocabulary, not the repository's | it is the failure behaviour |

### 4.4 · Verdict, and where it stops

**A decision-neutral derivation is buildable for exactly one shape**, and it is the shape the prior
record already specified: for each object, print the declared status, the condition parsed into its
atoms, and per atom `SATISFIED / UNSATISFIED / UNMEASURABLE`, each with the command that measured
it. Three of the four atom kinds are mechanical today:

```
"the operator approves"           -> an approval artifact naming the object          MEASURABLE
"canonical execution of CAND-X"   -> a commit declaring a canonical batch of CAND-X  MEASURABLE
"operator ratification"           -> `ratified_by:` non-empty                        MEASURABLE
"Mirror hostile review passes"    -> the verdict field's vocabulary is non-conforming UNMEASURABLE
```

🛑 **The frontier is exact and it is two-sided.** A tool may not emit an activation state, because
five of the eight states have no source of truth and inventing them is policy — and it may not emit
`REVIEWED` either, because the atom that decides it is unmeasurable until the Operator settles P-8.
**`ACTIVATION_STATE_READINESS = SPECIFIABLE, PARTIALLY MEASURABLE, BLOCKED ON P-8 FOR ONE ATOM.**
The remedy for the blocked atom is a determination, not a script, and it is H-7.

---

## 5 · Governance tool test coverage — delivered

Commit `c095c5d` on `plan-exec-repair-prep`.

| Suite | tests | mutants killed | control |
|---|:--:|---|:--:|
| `framework/scripts/test_lease_state.py` | **22** | singleton downgraded to exit 0 → **4 failures** · stored STATUS trusted → **2** · naive timestamp assumed UTC → **1** | green before and after every mutation |
| `governance/scripts/test_governance_fingerprint.py` | **27** | section scoping dropped → **5** · own contract excluded → **3** · per-role additions dropped → **4** · missing artifact tolerated → **1** · duplicate annex silently resolved → **1** | green before and after |
| `framework/scripts/test_regenerate_adjudications_coverage.py` | **18** (7 + 11 expected failures) | one guard applied → **2 unexpected successes, run red** | green before |

```
VALID · MISSING · MALFORMED · STALE · DUPLICATE · WRONG_HASH · WRONG_REF · NEGATIVE_CONTROL
```

All eight are covered where they have meaning. Two mappings are declared rather than forced:
`lease_state.py` computes no hash, so `WRONG_HASH` maps to *stored `STATUS` contradicts the
derivation*; and `STALE` for the fingerprint maps to the mutation arms, since a fingerprint has no
clock.

🔴 **What the lease suite deliberately does not claim.** It exercises the singleton **within one
record**. Two ACTIVE leases on two refs are invisible to a tool that reads one file, and no test
here can mount that condition. That is EG-05 and it is a population problem, not a derivation
problem; a green suite that appeared to cover it would be the worse outcome.

**A third inventory found the same two tools.** `scripts/test_release_surface.py` was red on four
shebang entrypoints missing executable mode, and two of the four were `lease_state.py` and
`governance_fingerprint.py` — the same two that had no suite and no inventory line. The mode change
turns that suite green. **The release inventory on this branch goes from 7 failures to 6.**

### 5.1 · The six that remain, characterised but not repaired

Five predate `702df73` and are one class plus one outlier. Four assert that `CLAUDE.md` still
carries rule text — the locator obligation, the abstract-corpus boundary, the receipt universality,
the self-eval wiring — and `CLAUDE.md` **became a router on 2026-08-16**, moving that text to named
normative files by design. The suites were not updated with the migration. **That is EG-15's class
again, one migration earlier**, and it is reported here rather than repaired because the owner of
each assertion is the normative file it moved to, not this session. The sixth and seventh are the
EG-15 pair, repaired uncommitted in the peer worktree.

---

## 6 · §P7 slices S1–S6 — status, and one reuse claim narrowed

**The readiness package at `PLAN-EXECUTABLE-GOVERNANCE-GAP-MAP-001` § 5 is complete and unchanged.**
Event inventory (23 typed, producer and consumer derived from the annexes), storage target, ordering,
idempotency, recovery, failure semantics, the reuse measurement, thirteen named tests, the dependency
frontier and the slice decomposition are all present. **Re-preparing them would be the busywork the
dispatch excludes**, so this section adds only what re-derivation changed.

**S1–S6 are NOT BUILT.** They are one working session and they cross no frontier; they were not the
highest-value use of this one against three priorities that closed or specified executable defects.
Stated plainly rather than reported as progress.

🔴 **One reuse claim is narrowed, by reading the interface rather than the summary.** Re-derived:
`framework/scripts/fulltext_receipts.py` is **1444 lines** with **1207** of test, six subcommands —
`validate · verify · anchor · status · record · rechain` — and `rechain` takes `--onto`, `--rename`,
`--repoint-manifests` and `--dry-run`, refusing a rename that would orphan a manifest citation. Its
own help says it *"rebases this ledger's divergent events onto another ledger's history"*.

**That is divergence reconciliation between two copies of ONE stream.** §P7's consolidation merges
**N distinct per-actor streams** into a derived view. The prior record's sentence — *"`rechain` is
the consolidator primitive … it is also the primitive M2.1 needs"* — is **correct for M2.1**, whose
approval queue is three divergent lineages of one file, and **overstated for S4**, which still needs
a replay-and-interleave that `rechain` does not provide. The append-only machinery, the chain hash
and the tail anchor remain genuinely reusable; the consolidator does not come free.

---

## 7 · SCIENTIFIC_CANONICALIZATION_QUEUE

### 7.1 · The denominator, corrected

```
CC-*.md files in the queue directory                                  19
  of which Status: committed / already propagated                     16   -> BATCH_20260815_001
  of which Status: PREPARED — awaiting the next lawful BATCH_COMMIT     3
```

**The four canonical scientific files last moved at `749a9a9`, 2026-08-15**, and that commit is
what consumed the sixteen. Verified with a positive control: **9** commits in all history touch the
four files, **0** after `749a9a9` on any of the 45 refs. Since then: **87** commits on `main`, **148**
on this branch, **0** scientific propagations.

🔴 **So "19 candidates and no movement in eleven days" is two facts fused into a wrong one.** The
files did not move *because* the queue was drained on 2026-08-15; the real backlog is **three
candidates, all prepared on 2026-08-25**, all introduced by `702df73`.

### 7.2 · The queue a restored Orchestrator can consume without re-analysis

| Field | **Q-S1** | **Q-S2** | **Q-S3** |
|---|---|---|---|
| CANDIDATE_ID | `CC-20260825-32000863-POINTER-01` | `CC-20260825-CLAIM016-DRIFT-01` | `CC-20260825-GRAPH-MATERIALIZATION-01` |
| OWNER | plan | plan | plan |
| REF | `plan-orchsurf-r4-transcription` + this branch; **absent from `main`** | idem | idem |
| COMMIT | `702df73` | `702df73` | `702df73` |
| AGE | 1 day at authoring | 1 day | 1 day |
| SCIENTIFIC_AREA | GSK3β / seizure susceptibility — figure-pointer provenance | GSK3β — abundance vs activation | claim-graph traceability |
| AFFECTED_CANONICAL_FILE | `claim_registry_current.md` | `claim_registry_current.md` | `claim_registry_current.md` |
| CLAIMS_AFFECTED | CLAIM 016, `Evidence boundary` | CLAIM 016, `Type` + `Summary` | CLAIM 025 → CLAIM 009 |
| PROVENANCE_IMPACT | **HIGH** — a reader following the cited panel lands on a different experiment and sees apparent self-contradiction | **HIGH** — the canonical proposition is not what the primary asserts | **LOW** — representational only |
| CONTRADICTIONS | the claim cites one panel for two experiments; manifest entries 0/22 anchor lithium elsewhere and entry 1 anchors the other | primary says *activation*; total protein is flat across genotypes in the densitometry | none |
| REVIEW_STATUS | prepared, not reviewed | prepared, not reviewed | prepared, not reviewed; Lane-A test applied item by item |
| DEPENDENCIES | none | 🔴 **strictly after Q-S1** — both edit CLAIM 016 and the block must be re-read between them | none |
| CANONICALIZATION_READINESS | **READY** | **READY**, ordered | **READY** |
| REQUIRED_REVIEWER | ordinary | ordinary; the candidate declares it corrects a canonical proposition | ordinary |
| HUMAN_GATE | ❌ | ⚠️ **depends on the change class the Orchestrator assigns** — it corrects a canonical scientific claim | ❌ |
| SUPERSEDED | NO | NO | NO |

**Priority order under the dispatch's own criteria** — corrects a false canonical claim first, then
provenance, then everything else: **Q-S2 has the highest scientific value and Q-S1 must run first**,
because they edit the same block and Q-S2's re-read depends on Q-S1's result. Q-S3 is independent.

**Two facts a consumer must not have to rediscover.** All three sit on refs that are not `main`, so
consuming them requires the same route EG-10 describes; and `BATCH_20260815_001`'s trigger is
`≥5 candidates`, which **three does not meet**, so consuming them is a deliberate act rather than an
automatic one.

**No scientific adjudication is performed here.** Every entry above restates what the candidate
declares about itself plus what git says about where it lives.

---

## 8 · LOCATOR_TO_CLAIM_PROPAGATION — measured, and the honest negative

### 8.1 · The surfaces and the join

```
deepdive manifests on disk                                   64
  with >= 1 verbatim locator entry                           63     (1002 entries)
page-adjudication recipes                                     3     (27 crop artifacts, 47 locators)
CLAIM blocks in claim_registry_current.md                     39
paper/corpus blocks carrying a PMID                          247
```

The join key is PMID, reached either directly from a claim block or through a paper-registry
wikilink:

```
claims naming a PMID directly                                19 of 39
claims resolving a PMID through the paper registry           32 of 39
claims reaching >= 1 manifest that HAS locators              27 of 39
claims reaching no paper identifier at all                    7 of 39   -> not joinable, at all
manifests-with-locators reached by >= 1 claim                25 of 63
manifests-with-locators reached by NO claim                  38 of 63
```

**The relation is machine-identifiable for 27 of 39 claims and 25 of 63 manifests.** It is not
identifiable for the rest, and that is a property of the records, not of the query.

### 8.2 · Two candidate detectors, both tested against the known instance — both fail

The failure mode Scientist A reports has two live examples, and a proposed check earns nothing until
it is run against them.

**Detector 1 — staleness.** *"A manifest edited after the last canonical propagation carries locator
content no claim has consumed."* Measured: **0** manifests modified in `749a9a9..HEAD`. Positive
control: **64** manifests touched in the full history, so the query fires.
🔴 **The signal is zero today and would have missed both known instances**, because those locators
were correct on the day they were written and the claim was propagated wrong in the same batch. The
defect is contemporaneous, not stale. A timestamp cannot see it.

**Detector 2 — figure-token cross-reference.** *"A figure token cited in a claim block that appears
in no manifest the claim joins to."* Measured: 5 claims cite a figure token; the check fires on
**2** (CLAIM 034, CLAIM 037) and **does not fire on CLAIM 016** — because the cited panel *does*
exist in the manifest. It is simply the wrong panel for the assertion beside it.
🔴 **Recall on the one instance it was designed for: zero. Precision on its two hits: unknown.**

### 8.3 · Verdict

**A reliable executable relation for "unpropagated contradiction" cannot be defined today, and
inventing one would be a brittle gate.** The distance between *a locator exists* and *the claim
misrepresents it* is exactly the distance a validator cannot cross without reading the science, and
both detectors above failed on the same side of that line.

**What IS decision-neutral, executable and currently unprinted is a coverage report, not a
detector:**

```
38 of 63 manifests carrying locators are cited by no claim   -> reading-to-claim coverage
 7 of 39 claims carry no resolvable paper identifier         -> claims outside the join entirely
27 of 39 claims are joinable                                 -> the population any future check has
```

None of those three numbers is a defect. All three are the population a human needs before deciding
whether a gate is worth building, and none of them exists anywhere today.
**LOCATOR_TO_CLAIM_PROPAGATION_READINESS = MEASURABLE AS COVERAGE · NOT MECHANIZABLE AS
CONTRADICTION.**

---

## 9 · WHAT THIS RECORD DOES NOT DO

Does not activate any role contract, protocol or parameter file · does not change any `status:` line
on any ref · does not select an option on D-1…D-6 or P-1…P-8 · does not rule on EG-02 · does not
decide whether `43cf690` stands · does not decide the MAJOR-2 routing at § 1.7 · does not choose
between variant A and variant B, and recommends A with the reason stated · does not open a `CAND`,
write a `DEC`, create an `APPROVAL` or append to any `.jsonl` · does not write to `ledger/`,
`runtime/`, `governance/candidates/`, `reviews/` or `roles/` on any ref · does not change what any
gate blocks on · does not wire `regenerate_adjudications.py verify` into any gate · does not assign
work to any actor · does not acquire a lease · does not verify or declare a capability · does not
adjudicate any scientific proposition or open a current file for writing · is **not** a
`CANONICAL_BATCH_COMMIT` and not its justification.

---

## 10 · VERIFICATION TRAIL

**Population-derived figures decay as branches and files are created; object-derived figures do
not.** A reader who gets a different number must be able to tell which happened.

| # | Claim | Command | Class |
|:--:|---|---|:--:|
| 1 | HEAD `90f08a4`; 2 behind / 63 ahead of `main` `788c357` | `git rev-list --left-right --count main...HEAD` | population |
| 2 | 45 heads; 14 worktrees; control `CLAUDE.md` on 45 of 45 | `git for-each-ref` · `git worktree list` · braced per-ref `git cat-file -e` | population |
| 3 | `702df73` introduces the regression; `43cf690~2` clean | four `git archive` extractions, four gates run in place | object |
| 4 | 6 failures clean-archive vs 5 in a working tree; the delta is the runner-verdict suite's `git ls-files` | the suite run in both | object |
| 5 | The 2×2 of § 2.4 | four purpose-built trees at HEAD, five gates each | object |
| 6 | PARTIAL_REVERT: `BLOCK_BATCH_COMMIT` + `RATCHET_VIOLATION (27845895)` | `43cf690` extraction with two files reset to `702df73` | object |
| 7 | BASE sha256 `e1155911…`, equal to the Agent Card's declared `ROLE_CONTRACT_HASH` | `git show main:roles/orchestrator.md \| shasum -a 256` · `git show orchestrator:runtime/agent_card_registry.md` | object |
| 8 | Variant A `d5759d13…` 4790 B; variant B `fce1ff9e…` 4786 B; 2 changed lines each | the `sed` recipe at § 1.3, then `diff` | object |
| 9 | Fingerprints: `main` base `88dea7a6…` → A `27383f3e…`; `orchestrator` base `e2c54470…` → A `fbc38014…`; other three roles unchanged | `governance_fingerprint.py compose --all` on two clean extractions, contract swapped | object |
| 10 | No hidden inheritance: 4 probes, 4 controls firing on revision 4, 0 in the restricted object | `grep -c` over three files | object |
| 11 | 14 fail-open arms; 4 distinct code paths; the 27/47 propagation | synthetic roots with `ROOT`/`ADJUDICATIONS` rebound and a generated PDF | object |
| 12 | 3 recipes · 27 crop artifacts · 47 adjudicated locators | JSON parse of the three tracked recipes | object |
| 13 | Coverage suite 18 tests / 11 expected failures; one guard → 2 unexpected successes, run red | the suite, then a scratch copy with G1 applied | object |
| 14 | Lease suite 22 tests, 3 mutants killed 4/2/1; fingerprint suite 27 tests, 5 mutants killed 5/3/4/1/1 | scratch copies of each module, mutated one line at a time, control re-run after each | object |
| 15 | 30 files carry a `status:` line; vocabulary sweep 61/2/0/6/13/0/0/0 with controls 19 and 8 | `grep -rn '^status:'` · `git log --all -S'status: <V>'` | object |
| 16 | 19 CC files, 16 committed, 3 prepared | `**Status:**` line of each, plus `git log --diff-filter=A` per file | object |
| 17 | 9 commits ever touch the four current files; 0 after `749a9a9`; 87 on `main` since, 148 here | `git log --all -- "$@"` with `set --`, and `git rev-list --count` | object |
| 18 | The join: 64/63/1002 · 39 claims · 27 joinable · 7 unjoinable · 38 uncited manifests | JSON + Markdown parse, paper registry as the PMID map | object |
| 19 | Detector 1 fires 0 times, control 64; detector 2 misses CLAIM 016 and hits 2 others | the two queries, each with its control | object |
| 20 | `DEC-20260820` ratified, present on 3 of 45 heads; control governance body on 30 of 45 | braced per-ref `git cat-file -e` + `git show \| grep '^ratified_by:'` | population |
| 21 | `fulltext_receipts.py` 1444 + 1207 lines, six subcommands, `rechain --onto` | `wc -l` · `--help` on both the top level and the subcommand | object |

**Two things went wrong in this session's own instruments, and both are reported because a figure
without a control is not a measurement.**

| What | Mechanism | Caught by | Changed a conclusion? |
|---|---|---|---|
| The claim-registry parse returned **0 CLAIM blocks** | the registry uses `## CLAIM NNN`, and the query assumed `### ` | a zero that was impossible against a file I could see | no — the re-run gives 39 |
| The `status: ACTIVE` sweep returned **6** | `-S` counts any commit whose diff contains the string, including prose *about* a status value | inspecting the six files rather than trusting the count | 🔴 **yes** — it would have reported `ACTIVE` as declared vocabulary, and it is not |

The second is the same shape as the guards at § 2 firing on a document reporting an absence, and as
the § 3 tool reporting a manifest as undeclared when it is merely unreadable. **Three instruments,
one defect: a matcher that cannot tell an assertion from a description of one.**

**Checked at the close, because the prior record's predicted recurrence fired twice against its own
author.** Run over the working tree with this file on disk, all three raw-byte guards name **zero**
occurrences of this record: the publication gate reports its one BLOCK in
`PATHOGRAPH-TRANSPORT-CONSOLIDATION-001` and nothing here; `scripts/test_documented_commands.py`
names three lines, all in that same file; `scripts/test_fresh_clone_reader_journey.py` names that
file and one other. **This record contributes 0 findings to 3 of 3.** It was written that way from
the first draft — no wikilink token is displayed anywhere above, and every repository-local script
path named in it resolves to a file that exists on this branch.

---

## 11 · OUTPUT

```
MAJOR2_PRODUCER_STATUS
    PRODUCED, NOT LANDED. Base main:roles/orchestrator.md verified at sha256 e1155911…, positively
    controlled against the Agent Card's own declared ROLE_CONTRACT_HASH. Variant A (recommended)
    d5759d13…, variant B fce1ff9e…, exactly 2 changed lines each, 4 no-inheritance probes at 0 with
    4 controls firing, 5-arm mutation check discriminating 2/0/0/1/1. Fingerprint consequence
    computed at both candidate refs with the other three roles byte-identical as the negative
    control. Agent Card consistency update specified; its FINGERPRINT field is ALREADY STALE on its
    own ref before MAJOR-2 touches it, so a single number is not written. One genuine terminal
    choice described and not decided (§ 1.7): the ratifying decision is on 3 of 45 heads and absent
    from main.

EG15_STATUS
    RE-DERIVED. Introducing commit is 702df73, not 43cf690. Three red surfaces, not two. The repair
    exists UNCOMMITTED in a peer session's working tree, is measured necessary and sufficient for
    all three, and was deliberately not committed by this session. HEAD remains red.

REGENERATE_ADJUDICATIONS_CONFIRMED_FAIL_OPEN_COUNT
    4 distinct code paths (zero coverage · selector miss · missing declared digest · declared-but-
    unreadable manifest), realised across 8 of 14 arms. Plus 1 declared degradation and 2 ambiguous
    statuses. The number "four" was not inherited; it was re-derived from the code paths and
    happens to agree.

FALSE_PASS_COUNT
    4 by code path; 8 by arm. Both stated because the two are quoted interchangeably and are not
    the same quantity.

ACTIVATION_STATE_READINESS
    SPECIFIABLE · PARTIALLY MEASURABLE · BLOCKED ON P-8 FOR ONE ATOM. 3 of the 8 proposed states
    exist in normative text, 4 are absent from all 45 refs, and 1 (ACTIVE) is an artefact of the
    instrument. Three condition atoms are mechanical; "Mirror hostile review passes" is
    UNMEASURABLE until the MIRROR_REVIEW vocabulary is settled.

LEASE_STATE_TEST_STATUS
    DELIVERED. 22 tests, in the release inventory, 3 mutants killed 4/2/1, control green either
    side of each. Boundary declared: the cross-ref singleton is out of reach by construction.

GOVERNANCE_FINGERPRINT_TEST_STATUS
    DELIVERED. 27 tests, in the release inventory, 5 mutants killed 5/3/4/1/1, control green either
    side of each.

P7_S1_S6_STATUS
    NOT BUILT. The readiness package is complete and unchanged; re-preparing it would be busywork.
    One inherited reuse claim narrowed with evidence: rechain reconciles two divergent copies of one
    stream, which is M2.1's problem, not S4's N-stream consolidation.

SCIENTIFIC_CANDIDATE_QUEUE_COUNT
    3, not 19. Sixteen of the nineteen files are already committed into BATCH_20260815_001 at
    749a9a9, which is the same commit whose date was being read as the start of the idleness.

LOCATOR_TO_CLAIM_PROPAGATION_READINESS
    MEASURABLE AS COVERAGE · NOT MECHANIZABLE AS CONTRADICTION. Two candidate detectors were built
    and run against the known instance; one fires zero times today, the other misses CLAIM 016
    entirely. No gate proposed.

READY_FOR_ORCHESTRATOR
    Q-S1 -> Q-S2 (ordered, same block) -> Q-S3, all three PREPARED, none on main, trigger not met at
    3 < 5. Plus, needing no Orchestrator: commit the EG-15 repair; merge c095c5d's three suites.

TRUE_HUMAN_BLOCKERS
    H-2  a determination on satisfied-condition / stale-status, all four objects at once
    H-7  the MIRROR_REVIEW vocabulary — it is the single atom blocking activation_state
    H-8  does 43cf690 stand — now decidable ALONE, since § 2.4 shows it is gate-independent
    H-6  a route for control-plane artifacts to main — the ratified DEC and all 3 candidates need it
    §1.7 the MAJOR-2 routing choice, and the one byte of emphasis at § 1.3
    Unchanged and unreached here: H-1, H-3, H-4, H-5, H-9.

NEXT_5_PLAN_ACTIONS
    1  Commit the EG-15 repair — its author's call, or with their consent. 6 gates, 2 arms, one
       measured cause; nothing else in this record is blocked by it and GATE 2 is.
    2  Land the three suites of c095c5d toward main, so the two tools a FROZEN gate reads as a
       boolean are protected where CI can see them rather than on one branch.
    3  Build activation_state to the § 4.4 shape only — atoms, measurements, commands, and
       UNMEASURABLE where the vocabulary is unsettled. It makes H-2 and H-7 decidable in one sitting
       and asserts no activation.
    4  Repair the four CLAUDE.md-migration suites of § 5.1, or retarget them at the normative files
       the text moved to. Four of the six remaining failures are one 2026-08-16 migration.
    5  §P7 S1-S6, with S4 re-scoped: the consolidator is not free, and the package should say so
       before an implementer discovers it.
```

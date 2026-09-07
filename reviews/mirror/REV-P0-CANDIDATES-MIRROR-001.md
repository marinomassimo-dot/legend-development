---
artifact: MIRROR hostile review (Annex C.2) — the three P0 repair candidates
review_id: REV-P0-CANDIDATES-MIRROR-001
object: `plan-adjudication-failclosed-repair` @ `9cb09c0` · `plan-release-surface-repair` @
  `bf9c807` · `plan-approval-queue-consolidator` @ `49303af`
continues: PRIVACY_SEMANTICS_AND_FALSE_PASS_HOSTILE_REVIEW_MIRROR_v2 §§ 5–6, which these three
  candidates answer
level: R4 (METHOD — Mirror)
reviewer: mirror
date: 2026-08-26
verdict: ADJFAILCLOSED CONDITIONAL_PASS (3 residual false passes, one uncaught traceback) ·
  RELSURF PASS_WITH_FINDING (it repairs what it claims and the runner stays red) ·
  APQCONS BLOCKING (two lineages can be dropped silently by the tool's own documented workflow)
mutation_arm: independent. 31 states against ADJFAILCLOSED and 7 against APQCONS, each built in
  this session and none read from either candidate's suite before its own matrix was complete.
---

# The tool built so that no approval is invisible drops two lineages of approvals and prints a green summary

---

## 0 · OBSERVATION_SCOPE

| Fact | Value |
|---|---|
| `main` | `788c357` |
| Candidates | each **1 ahead of `main`, 0 behind** |
| Adjudication baseline | re-derived on a clone of the candidate with the three PDFs staged: **exit 0**, `27 of 27 declared digest(s) matched across 27 rendered artifact(s) in 3 study(ies); 47 of 47 locator(s) resolved …, and 47 of them against the snippet each names` |
| Python · PyMuPDF | 3.9.6 · 1.26.5 |

**A correction to my own matrix, made before the finding count.** My first signature captured six
numbers from the summary and not the seventh — *"and N of them against the snippet each names"*.
On that signature `A6_MANIFEST_KEY_REMOVED` scored as a false pass. It is not: the candidate
reports **18** there against a baseline of 47. The false-pass count below is **3, not 4**, and the
reason I nearly filed a fourth is that I compressed a summary before checking it carried
everything.

---

## 1 · ADJFAILCLOSED — 31 states, 22 fail closed, 3 false passes remain

### 1.1 · What the repair closes

Of the 8 false passes v2 § 5 measured, **5 are closed**:

| v2 state | before | after |
|---|---|---|
| `MISSING_DIGEST` one artifact | exit 0, `27/47` | **exit 1** — *"1 artifact(s) declare no sha256, so nothing was compared for them"* |
| `MISSING_DIGEST` all 7 of one recipe | exit 0, `27/47` | **exit 1** |
| `MISSPELLED_MANIFEST` | exit 0, `27/47` | **exit 1** — the three-state `manifest_state()` separates *declares none* from *declares one that will not load* |
| `MANIFEST_KEY_REMOVED` | exit 0, `27/47` | exit 0, **`… and 18 of them against the snippet each names`** — reported, not silent |
| `PARTIAL_DIGEST_SET` mixed | exit 0, `27/47` | **exit 1** |

And the `ZERO_COVERAGE` family, which previously printed `OK: 0 …`, now fails closed in every
form I could construct: recipes deleted, directory renamed, directory present-but-empty, every
recipe's `artifacts` empty, `--pmid` matching nothing, `--pmid` off by one digit, one source PDF
absent, all source PDFs absent. **The counter defect is genuinely fixed**: seven counters, each
incremented where its claim becomes true, and the summary now reads `X of Y` throughout.

`test_regenerate_adjudications_fails_closed.py` **drives the real script as a subprocess** — it
closes the *"12 tests, none calls `run()`"* gap of v2 § 5.1 directly. That is the part of this
candidate I would not want changed.

### 1.2 · FINDING P0-1 — three false passes remain, and they are one class

| state | exit | summary | |
|---|---:|---|---|
| `A9` — a declared `.png` corrupted on disk after `write` | 0 | **byte-identical to baseline** | the image is rendered in memory and never re-read from disk |
| `N5` — an undeclared `.png` sitting in a recipe directory | 0 | **byte-identical to baseline** | nothing enumerates the directory |
| `N6` — a directory under `page_adjudications/` with images and no `adjudications.json` | 0 | **byte-identical to baseline** | the glob is `*/adjudications.json`; a directory that declares nothing is not a directory that contains nothing |

One class: **the gate verifies the recipe and never the directory.** It answers *does every
declared artifact regenerate* and never *is every file present declared*. That is the exact
complement of the `ZERO_COVERAGE` case this repair closed — coverage of the declaration by the
tree, where the repair added coverage of the tree by the declaration.

`A9` is the sharpest of the three because `write` is a documented action: a run that writes the
images, followed by any corruption or edit of them, verifies green forever.

### 1.3 · FINDING P0-2 — the second JSON read is still unguarded

`manifest_state()` now wraps its `json.loads` in `try/except`. `recipes()` does not:

```
P5_STALE_PRIOR_SUCCESS  (adjudications.json made malformed)
  exit 1  —  json.decoder.JSONDecodeError, uncaught, full traceback
```

Fail-closed on the exit code, and the message is a stack trace carrying **exit 1 — the same code
as a genuine digest mismatch**. A caller cannot separate *the evidence is wrong* from *the tool
crashed*. The repair fixed one of the two JSON reads on the same code path.

### 1.4 · FINDING P0-3 — every denominator is the declaration itself

The summary is now internally consistent (`X of X`) and every denominator is self-reported. Two
states show what that costs:

- `N4` — the same locator declared three times in one artifact: `47 → 51 locator(s) resolved`,
  exit 0. **Declaring work three times reports it three times.**
- `N8` — a recipe silently shrunk from 9 artifacts to 3: `27 → 21`, exit 0, detectable only by
  someone who already knows the number should be 27.

**Two external invariants exist today and neither is checked. Measured on the candidate's own
green tree:**

| recipe | artifacts | locators declared | **distinct** | manifest entries | manifest covered |
|---|---:|---:|---:|---:|---:|
| 16061658 | 9 | 10 | 10 | 12 | 83 % |
| 17803050 | 7 | 29 | 29 | 32 | 91 % |
| 21212533 | 11 | 8 | **7** | 14 | 50 % |
| **TOTAL** | **27** | **47** | **46** | **58** | **79 %** |

- `declared == distinct` is **already false on the green tree**: `PMID21212533` declares
  `entries[5]` twice, in one artifact, with two needles (`234.5` and `246.5`). That is legitimate
  work — two cell values from one table row — and the summary calls it *"47 locator(s)"*. The
  count is 47 **needle** resolutions over **46 distinct locators**, and the canonical
  transcriptions (`state_manifest_current.md`, `full_text_queue_current.md`) record *"47 locator
  resolutions"*. **NOMENCLATURE_VS_MEASUREMENT**, not a defect in the work.
- **12 of 58 manifest locators are adjudicated by no crop.** The manifest is the other half of the
  chain and nothing compares the two. A coverage line — *N of M manifest locators adjudicated* —
  is derivable from data already loaded.

### 1.5 · `ADJFAILCLOSED_VERDICT = CONDITIONAL_PASS`

The repair does what it says, closes 5 of 8 false passes and the whole `ZERO_COVERAGE` family,
and fixes the counter defect at its root. **Can a downstream consumer still read a green sentence
claiming more than was verified? Yes, in three states** — and in all three the sentence is
byte-identical to a fully verified run, which is the strongest form of the failure. P0-2 and P0-3
are additive and do not contest what is here.

---

## 2 · RELSURF — it repairs exactly what it claims, and the runner stays red

### 2.1 · The five axes

| axis | result |
|---|---|
| **MODE_BITS** | **PASS** — the four `100644 → 100755` changes are exactly the four files with a shebang and no executable bit. I enumerated independently: `lease_state.py`, `candidate_content_hash.py`, `governance_fingerprint.py`, `test_candidate_content_hash.py`. No fifth, no over-reach |
| **TEST_ENROLLMENT** | **PASS** — one line, `governance/scripts/test_candidate_content_hash.py`, which is the single file v2 § 6.4 derived independently |
| **RUNNER_ORDER** | **PASS with a merge note** — inserted after `test_regenerate_adjudications.py`. **All three P0 candidates insert at that same line**, so they conflict textually. More than textually: see § 2.2 |
| **ROUTER_RULE_REACHABILITY** | **NOT ADDRESSED** — the five failures asserting that CLAUDE.md still contains operating law it deliberately shed on 2026-08-16 are untouched. That is not a defect of this candidate; it is the reason the verdict below is what it is |
| **DISK_VS_REPOSITORY_POPULATION** | **PASS, and already correct on `main`** — both `test_release_runner_verdict.py` and `test_release_surface.py` enumerate through `git ls-files`, the index, not `rglob`. My 11 untracked files cannot reach either. The file's own comment records that this was learned the hard way |

**One residual on MODE_BITS.** The enumeration comes from the index and the assertion reads
`path.stat().st_mode & 0o111` — the **disk**. This checkout has `core.fileMode = true`, so the two
agree here. Where `core.fileMode` is false the disk mode is not the committed mode, and the test
then passes or fails on a property the repository does not carry. Not a finding against this
candidate — it is inherited — but it is why this candidate's fix must be verified from a fresh
clone rather than from a working tree.

### 2.2 · FINDING P0-4 — three candidates, one green suite between them

Each candidate enrolls its own new suite and none enrols another's:

| branch | `test_every_tracked_test_file_is_in_the_runner` | `test_shebang_python_entrypoints_are_executable` |
|---|---|---|
| `plan-release-surface-repair` | **PASS** | **PASS** |
| `plan-approval-queue-consolidator` | **FAIL** — `test_candidate_content_hash.py` | **FAIL** — the four mode bits |
| `plan-adjudication-failclosed-repair` | **FAIL** — same | **FAIL** — same |

So the completeness check is green on exactly one branch, and **merge order decides whether it
stays green**: merging either of the other two first re-reds it until RELSURF lands. The four new
files all carry mode `100755` in the index already, so no candidate re-reds the surface test by
adding a file — that hole is closed by accident rather than by rule, and only because each author
happened to `chmod +x`.

### 2.3 · `RELSURF_VERDICT = PASS_WITH_FINDING`

It repairs what it claims and over-reaches nowhere. Full runner, run on a clean clone of the
candidate rather than inferred from the two suites above:

```
main @ 788c357              REGRESSION VERDICT: FAIL   7 test cases / 6 suites
plan-release-surface-repair REGRESSION VERDICT: FAIL   5 test cases / 4 suites
```

The two it removes are exactly the two it targets. **The five that remain are the router-migration
assertions** — `verbatim_locators`, `pubmed_corpus_harvest`, `FULLTEXT_READ_RECEIPT`,
`state-control`, `session_self_evaluation.md`, each asserting that CLAUDE.md still contains
operating law it deliberately shed on 2026-08-16.

I record the residual explicitly because **reducing a failure count is not the same as making a
gate readable**, and this is the candidate most likely to be read as having fixed the runner. It
did not; it fixed the two things it named.

---

## 3 · APQCONS — BLOCKING

### 3.1 · What Strategy A gets right

Every property the brief asks about holds **at the `consolidate()` level**, and I verified each
rather than reading the docstring:

| requirement | result |
|---|---|
| no approval lost | **PASS** — control: 3 lineages, shared prefix, disjoint suffixes → 4 records, all identities present |
| no duplication | **PASS** — the shared prefix collapses exactly once |
| no semantic reordering of date-only records | **PASS** — `(timestamp, first-seen position, identity)`; supplying the lineages in either order over two lineages with **opposite internal orders** produced the identical result |
| no invented timestamps | **PASS** — `timestamp()` returns `""` and nothing synthesises one |
| no rechain required | **PASS** — none is performed, and the absence of a prev-hash in all 30 records is stated as measured rather than assumed |
| provenance preserved | **PASS** — sidecar keyed by identity; no field is written into any record, so the byte-identity the dedup depends on survives |
| fail closed on same-ID/different-content | **PASS for string ids** — `ConflictError`, not merged |

### 3.2 · FINDING P0-5 — BLOCKING — the documented workflow silently drops lineages

```python
sources = {path.stem: load(path) for path in arguments.sources}
```

A dict comprehension keyed by **file stem**. The module's own docstring tells the operator to
*"extract them with `git cat-file -p <blob>`"*, and the natural extraction — one directory per ref
— produces three files with the same stem:

```
$ consolidate_approval_queue.py main/queue.jsonl orchestrator/queue.jsonl evidence-index/queue.jsonl
sources: queue=3
consolidated: 3 records from 3 input line(s); 0 deduped, 0 conflicts
exit 0
approvals lost silently: AP-ONLY-MAIN, AP-ONLY-ORCH
```

Two of three lineages are discarded before `consolidate()` is ever called. `sources:` reports
**one** lineage, `0 deduped, 0 conflicts` is true of what remained, and the exit code is 0. **The
tool written so that no approval is invisible because of which ref it landed on makes fourteen of
them invisible because of what the file was called** — and says so in a green summary.

Its 16 tests all call `consolidate()` with a dict already built. **The suite never executes the
script**: the only match for `main(`, `subprocess` or `argv` in the whole file is
`unittest.main()`. So the defect is not merely uncovered, it is unreachable by that suite by
construction — the same shape as the twelve tests that never called `run()`.

### 3.3 · FINDING P0-6 — BLOCKING — the conflict guard is string-typed

```python
def identity(record):
    for field in ID_FIELDS:
        value = record.get(field)
        if isinstance(value, str) and value:
            return value
    ...
    return "sha256:" + hashlib.sha256(...)
```

A non-string identifier falls through to content addressing, so two records **with the same
approval id and opposite decisions** get different keys:

| input | result |
|---|---|
| `{"APPROVAL_ID": "AP-1", "STATE": "APPROVED"}` vs `"REJECTED"` | `ConflictError` — correct |
| `{"APPROVAL_ID": 7, "STATE": "APPROVED"}` vs `"REJECTED"` | **both kept, no error, exit 0** |

Two contradictory decisions on one approval, retained side by side in a view whose purpose is to
be the one place a reader can trust. The guard the brief names — *fail closed on same-ID /
different-content* — holds for the type the current data happens to use and not for the predicate
as written. The queue's schema is not enforced anywhere I could find, so the type is a convention.

### 3.4 · Two minor findings

- **An untimestamped record sorts first.** `timestamp()` returns `""`, which sorts before every
  date, so an approval carrying the least information takes the position a reader reads first —
  immediately after the header. Measured: `['__HEADER__', 'AP-NO-TS', 'AP-DATED']`.
- **`load()` raises outside the guard.** `ConflictError` from a malformed line is raised inside
  `load()`, which is called *before* the `try` that catches it, so a truncated line produces an
  uncaught traceback instead of the tool's own `CONFLICT — not merged:` line. Exit 1 either way.
  Same class as § 1.3, in a different candidate, on the same day.
- **Provenance duplicates a lineage name.** The same identity twice inside one lineage yields
  `lineages: ['a', 'a']`, so the sidecar field cannot be read as a set.

### 3.5 · `APQCONS_VERDICT = BLOCKING`

The design is sound and the measurements behind it are real — the byte-exact prefix, the absent
hash chain, the date-only precision and its consequence for ordering are all stated as derived
and all hold. **Two defects sit between that design and its user**, both outside the tested
surface, and both fail in the direction the tool exists to prevent: an approval that disappears
without a message, and two contradictory approvals that coexist without one.

---

## 4 · The cross-candidate pattern, which is v2's pattern again

| candidate | tested surface | defect sits in |
|---|---|---|
| ADJFAILCLOSED | the script, driven as a subprocess — **fixed by this candidate** | the directory the script never enumerates |
| APQCONS | `consolidate()`, a pure function | `main()`, which builds its input |
| RELSURF | `git ls-files`, the index | the disk mode bit the assertion actually reads |

Three candidates, three suites, and in each case the boundary of the test is the boundary of the
defect. ADJFAILCLOSED is the one that moved its boundary outward, and it is the one whose residual
findings are the smallest.

---

## 5 · WHAT_WOULD_CHANGE_MY_MIND

- **§ 3.2** — if the documented extraction workflow is specified somewhere I did not read, with a
  naming scheme that cannot collide, P0-5 drops from BLOCKING to a hardening note. Test: find the
  runbook that names the output paths. I searched the module docstring and the suite and found
  none.
- **§ 3.3** — if the approval-queue schema is enforced at write time such that a non-string id
  cannot exist, P0-6 becomes latent rather than live. Test: find the writer and its validation.
- **§ 1.2** — if `write` is never run outside a session that immediately re-verifies, `A9` is
  unreachable in practice. Test: find whether any procedure runs `write` and stops.
- **§ 1.4** — if *"locator"* in the summary is intended to mean *needle resolution*, the 47/46
  finding is a wording question and not a count question, and the canonical transcription is
  correct as written.

# PROMPT — BATCH COMMIT

> **Operational protocol for propagating commit candidates into the current files.**
> Version: v3.3.1
> Invoke with `MODE: BATCH_COMMIT` or `MODE: URGENT_COMMIT`.

---

## 0. PURPOSE

Deterministically turn the commit candidates accumulated in `session_commit_log.md` into actual updates to the current files, with:

- a Working-Model version bump
- a complete change log
- conflict detection and resolution
- propagation tracking
- manifest and activity-log update

> **BATCH_COMMIT is the only moment when the 4 scientific current files are modified.**
> Outside BATCH_COMMIT, the current files are read-only.

---

## 1. INVOCATION

### 1.1 BATCH_COMMIT (standard)

Triggered by:
- **Temporal**: weekly (fixed day)
- **Threshold**: ≥ 5 accumulated commit candidates
- **Manual**: explicit operator request

The **first trigger to fire** wins.

### 1.2 URGENT_COMMIT (exception)

Triggered by an `URGENT_COMMIT_REQUEST` authorized by the operator, in the 5 admissible categories:
1. Direct safety signal
2. Grave error in the WM
3. Paper decisive for a direct clinical decision
4. Explicit operator request
5. Retraction / invalidation

Operational differences from standard BATCH_COMMIT:
- Accelerated subset (may skip phases 4 and 7 if not relevant)
- Triggers a MAJOR bump of `working_model_version`
- Requires explicit authorization before starting
- May propagate a single isolated commit candidate

---

## 2. PRE-FLIGHT CHECK (MANDATORY)

Before starting the BATCH_COMMIT, verify in order:

| Check | If it fails → |
|---|---|
| `state_manifest_current.md` readable | ABORT — recovery |
| `current_state` in manifest = `READY` | ABORT — resolve the block |
| LINT_AUTOMATIC run recently (< 24h) with outcome ≤ WARN_BUT_PROCEED | Run LINT_AUTOMATIC now |
| No pending `BLOCK_BATCH_COMMIT` or `BLOCK_SYSTEM` | ABORT — resolve first |
| No unmerged active parallel branch | ABORT — complete the merge first |
| `session_commit_log.md` contains at least 1 commit candidate | ABORT (nothing to commit) |
| Backup of the current files available | ABORT — create a backup first |

If all checks pass → set `current_state: IN_BATCH_COMMIT` in the manifest and proceed.

---

## 3. PROTOCOL — 8 PHASES

### Phase 1 — Inventory

Build an inventory of the commit candidates to process.

```
For each commit candidate in session_commit_log.md:
  - ID
  - creation timestamp
  - declared target_wm_version
  - type (paper / claim / meta / research / biomarker / endpoint / framework)
  - impacted files
  - urgent flag (yes/no)
```

Output: `batch_inventory.tmp` (ordered list).

**Ordering rule:** process in the order
1. URGENT (if present and authorized)
2. Paper additions
3. Claim updates
4. Meta updates
5. Research-line updates
6. Biomarker / endpoint updates
7. Working-Model updates (always last)

This order guarantees that upstream dependencies are already propagated.

---

### Phase 2 — Conflict detection

For each commit candidate, check conflicts with:

- other commit candidates in the same batch (e.g. two commits propose different changes to CLAIM 028)
- the current state of the current files (e.g. a claim modified after the candidate was created)
- the current Working-Model state

| Conflict type | Resolution |
|---|---|
| Two CCs modify the same claim compatibly | Automatic merge |
| Two CCs modify the same claim incompatibly | STOP → request an operator decision |
| Obsolete CC (claim modified by another already-propagated CC) | Mark the CC as `SUPERSEDED` |
| CC depending on a claim that does not yet exist | STOP → reorder or request a new CC |

If conflicts are unresolved → ABORT the batch + produce a `conflict_report.md` for the operator.

---

### Phase 3 — Backup and snapshot

Before touching any current file:

```
python3 framework/scripts/batch_commit.py snapshot --dest backup/YYYYMMDD_HHMM
```

🔴 **The list below is the declaration the tool reads, not a reminder to a human.**
`batch_commit.py snapshot` parses this fenced block and copies every path it names; a path
added here is snapshotted by the next batch with no code change, and
`framework/scripts/test_batch_commit_snapshot.py` turns red when a path named here is not in
the snapshot the tool writes. It is written this way because the hand-maintained list drifted:
on 2026-09-28 BATCH_20260928_001 edited `therapeutic_strategies_current.md`, which neither the
tool's list nor this declaration named, and had to copy it into the snapshot by hand — a file
outside the snapshot is a file § 5's ABORT cannot restore.

SNAPSHOT_DECLARATION (repo-relative; a `*` glob is expanded at snapshot time):
```
  - disease-models/wwox/registries/working_model_current.md
  - disease-models/wwox/registries/working_model_history*.md
  - disease-models/wwox/registries/claim_registry_current.md
  - disease-models/wwox/registries/paper_registry_current.md
  - disease-models/wwox/registries/literature_tracking_log_current.md
  - disease-models/wwox/disease_model.md
  - disease-models/wwox/meta/meta_*_current.md
  - disease-models/wwox/research/research_*_current.md
  - disease-models/wwox/biomarker_endpoint/biomarker_candidates_current.md
  - disease-models/wwox/biomarker_endpoint/clinical_monitoring_endpoints_current.md
  - disease-models/wwox/therapeutics/therapeutic_strategies_current.md
  - framework/state/state_manifest_current.md
  - framework/state/state_history.md
```

**What is deliberately NOT here.** The append-only ledgers (`fulltext_read_receipts.jsonl`,
`discovery_ledger_current.md`, `dismissal_ledger_current.md`, `full_text_queue_current.md`,
`therapeutic_hypotheses_ledger_current.md`, `experiment_ledger_current.md`) are excluded by
design: a batch appends to them rather than rewriting them, and restoring one from a pre-batch
snapshot would silently discard whatever a concurrent actor appended while the batch ran. An
ABORT leaves their appends standing; that is the lesser loss, and it is stated so nobody
"completes" the declaration by adding them.

Record the snapshot path **and the pre-batch commit SHA** in `legend_activity_log.md`.

🔴 **PRE_BATCH_COMMIT — recorded here because Phase 3 is the only moment it is knowable.**
`snapshot` writes it into the snapshot as `SNAPSHOT_BASE.json` and prints it, together with the
restore commands, so the correct one is writable at the moment it is needed rather than
reconstructed from the reflog while a batch is aborting. Reprint it at any time with:

```
python3 framework/scripts/batch_commit.py base --snapshot-dir backup/YYYYMMDD_HHMM
```

🔴 **A RESTORE COMMAND WITHOUT ITS BASE IS RIGHT IN THE WRONG WINDOW.**
`git checkout -- <path>` restores the pre-batch value **only while the propagation is neither
staged nor committed.** From the first `git add` onward it restores the *batch's own* output and
exits 0 — and the Phase 5 / § 5 ABORT lives partly in that later window, because a batch commits
its propagation together with the surfaces Phase 4.7 regenerates. So the fallback below is
stated with its base, in the order an ABORT uses it:

1. `python3 framework/scripts/batch_commit.py restore --snapshot-dir <path> --confirm-restore`
   — the primary restore, and the only correct source for a path that was **already modified**
   when the snapshot was taken (`SNAPSHOT_BASE.json` names those under `dirty_at_snapshot`).
2. `git checkout <PRE_BATCH_COMMIT> -- <path>` — the base-qualified fallback for a tracked path
   the snapshot does not hold, correct in **both** windows.
3. `git checkout -- <path>` — correct only before the propagation is staged. Never written at
   Phase 5 without checking which window the batch is in.

⚠️ An untracked or gitignored path has no base: for it the snapshot is the only source, which is
the argument for the declaration above being complete rather than for a wider `git` command.

🔴 **`disease_model.md` was absent from this list until 2026-09-28 and the tool did not notice**,
because the only coverage condition was the four scientific current files — and that file is a
canonical disease-model file by `state_manifest_current.md` § 3.1, written by two batches on
2026-09-28 alone. BATCH_20260928_002 measured the gap, deliberately did NOT hand-copy it into its
own snapshot (hand-copying fixes one batch and leaves the declaration wrong for the next, which is
the drift this declaration exists to end) and fell back to `git checkout --` on abort, which works
only because the file is tracked — and, as the base note above records, only while the propagation
is still unstaged. The reason the tool could not catch it is worth stating: **the
coverage condition names four files, while the propagation phases below can write every file in
this list.** Widening the condition to "every file the propagation phases can write" would close
the class rather than this instance, and it is not done here because it needs one source of truth
for that set — which is this block, and a block cannot verify itself. Until then: a batch that
writes a canonical file NOT in this list adds it here, in the same commit, before propagating.

> **Without a complete snapshot: ABORT.** The tool enforces this literally: if a declared
> non-glob path is missing from the working tree, or if any of the four scientific current
> files is not covered by the declaration, `snapshot` refuses and writes nothing. The second
> condition is a FLOOR, not the coverage this list promises — see the note above.

---

### Phase 4 — Propagation

For each commit candidate (in the order fixed in Phase 1), apply the changes.

#### 4.0 How a current file is written — record-scoped, or full rewrite

| File | Propagation |
|---|---|
| `working_model_current.md` · `claim_registry_current.md` · `literature_tracking_log_current.md` · `paper_registry_current.md` | **record-scoped**: every change of the batch to that file as ONE atomic list of operations — `replace` / `replace-within` a record or range, `insert-after` / `insert-before` / `append` a new record, `delete` — applied with `python3 framework/scripts/batch_commit.py propagate --file <file> --ops <ops.json>` (dry run), then the same with `--apply`. The editor (`record_scoped_edit.py`) proves before writing that every byte outside the addressed records is unchanged, and refuses an ambiguous, fenced or nested anchor or an edit that would re-segment the file. For the working model prefer `replace-within` (a changelog row, a version line, a mirror row). A section heading the file carries twice — the paper registry's two `## Purpose` — is named with `"under"`, the exact text of its enclosing heading (`"heading": "Purpose", "under": "Paper Registry Current"`). |

**A refusal is never forced.** Exit 3 writes nothing and prints a `FULL_FALLBACK <file> <code>`
line. Either the operation list is wrong — fix it and rerun — or the edit is outside what the
editor can prove (an unaddressable anchor, a re-segmentation, an identity change it cannot
verify); then that file, and only that file, is propagated by **full rewrite** for this batch,
unchanged sections copied verbatim and the whole-file result checked as before (Phase 5), and
the `FULL_FALLBACK` line goes into the batch report (Phase 8.2) so its frequency is measurable.

🔴 **Why, and why this file is where it lives.** Benchmark J replayed every historical batch edit
of the four files through the editor: 368 legitimate edits of the working model, claim registry
and literature log reproduced byte for byte with zero silent corruption
([`J3_DECISION.md`](../eval/benchmarks/BENCH-J-RECORD-SCOPED-EDIT/J3_DECISION.md), 2026-09-26);
the paper registry's 328 did too once its duplicated `## Purpose` became addressable with
`under` ([`J5_RESULTS.md`](../eval/benchmarks/BENCH-J-RECORD-SCOPED-EDIT/J5_RESULTS.md),
2026-09-28; adopted by operator decision the same day).

#### 4.1 Paper additions
Append to `paper_registry_current.md`. Update `literature_tracking_log_current.md`.

#### 4.2 Claim updates
Modify `claim_registry_current.md`. Verify:
- valid status
- at least 1 supporting paper
- a change-log entry for every modification

#### 4.3 Meta updates
Modify `meta_*_current.md`. Update `meta_index_current.md` if a new meta.

#### 4.4 Research-line updates
Modify `research_lines_current.md` or `research_candidates_current.md`.

#### 4.5 Biomarker / endpoint updates
Modify `biomarker_candidates_current.md` or `clinical_monitoring_endpoints_current.md`.

**Discipline check** (rerun of the biomarker section of the LINT):
- Tier 3 endpoint in the biomarker file → ABORT
- Biochemical biomarker in the endpoint file → ABORT
- Biomarker promoted to "validated" without a validation paper → ABORT

#### 4.6 Working-Model update (last)
Apply the version rule in [state manifest §2](../state/state_manifest_current.md#2-disease-model-working-model-version).
A batch with a disease-model change updates `working_model_current.md` and:
- Bumps `working_model_version`:
  - MINOR for normal changes
  - MAJOR for baseline reversals / authorized URGENT
- Update the WM change log — in the **cold** [`working_model_history.md`](../../disease-models/wwox/registries/working_model_history.md), not in the hot file: the batch's `Last update` note at the top of its first section, its row at the top of the `## Changelog` table, and, for a MAJOR batch, its narrative section after the table. The hot `working_model_current.md` keeps one `**Last update:**` line, replaced by the batch, and a `## Changelog` that points to the history. A qualification that is still live goes into the hot file's live sections too — the history is never a source of a current value (split by `BATCH_20260928_004`, operator decision A of 2026-09-28)
- Verify that every cited claim exists and has a compatible status

Publication integrity is independent of lifecycle Status. Preserve existing retraction
and concern flags and their eligibility holds (the corpus seed, `batch_queue.py` and LINT
already check them). Do not map a retracted record to `background_only` to satisfy the
lifecycle vocabulary. An unmapped historical Status remains visible until its lifecycle
can be assigned without changing the integrity exclusion; no new integrity registry is needed.

For a purely structural batch with no disease-model change, preserve the WM version,
WM timestamps and the WM changelog rows (in `working_model_history.md`). Record the changed fields and the evidence for zero
scientific delta in the batch report. Status changes affecting evidence eligibility,
claim meaning, support or uncertainty are not structural spelling corrections.

#### 4.7 Regenerate the derived surfaces (before the LINT sees the result)

Any file that is *generated from* the registries must be regenerated here, inside the
snapshot-protected window, so that a failure to regenerate aborts the batch like any other
propagation failure.

```bash
REASON="BATCH_COMMIT phase 4.7: the dirty registries are this batch's own edits and land in the same commit as the surface"
python3 framework/scripts/coverage_report.py --disease wwox \
    --out disease-models/wwox/registries/coverage_report.md --inputs-dirty-because "$REASON"
python3 framework/scripts/batch_queue.py --disease wwox \
    --out disease-models/wwox/registries/batch_queue.md --inputs-dirty-because "$REASON"
python3 framework/scripts/pathograph.py --disease wwox \
    --out disease-models/wwox/analysis/pathograph_inventory.md \
    --export disease-models/wwox/analysis/data/pathograph_export.jsonl --inputs-dirty-because "$REASON"
python3 framework/scripts/reading_state.py --disease wwox \
    --out disease-models/wwox/registries/reading_state.md --inputs-dirty-because "$REASON"
```

`reading_state.md` reads only the receipt ledger, so a batch whose receipts landed since the
last regeneration drifts it even when no registry changed. It was absent from this list until
2026-09-14: three receipts landed that day, BATCH_20260914_006 regenerated it by hand while
recording that this phase did not name it, and `test_reading_state.py` was red in between.
`test_generated_surfaces_are_regenerated.py` had missed it because its marker was the literal
`Generated file` and this page opens `GENERATED by`; the marker is now case-insensitive.

🔴 **Why the reason is passed, and why only here.** Since 2026-09-11 every generator refuses to
write a derived surface while one of its inputs is uncommitted (`derived_inputs.py`): on
2026-09-09 a mid-wave regeneration baked two peers' uncommitted manifests into the shared
surfaces (retrospective C22), and the only thing that caught it was the actor's attention. Inside
this phase the dirty inputs are the batch's own propagation and are committed with the surface,
so the reason is stated on the command line where a transcript reader sees it. Outside a batch
commit, a refusal means exactly what it says: **someone's work is in flight — wait, or name it.**
Before passing the reason here, `git status --porcelain disease-models/wwox/research/` must be
empty: a manifest in flight is not this batch's edit, and the reason would be false.

🔴 **Why this is a phase and not a reminder.** `coverage_report.md` declares itself generated
and a regression re-derives it and fails when it has drifted. Until this step existed, that
regression could only fire *after* the fact: a batch propagated, the report went stale, the
commit completed, and the release suite reported the drift to whoever ran it next. The check
was doing its job at the wrong moment — it announced a defect the protocol had just been
allowed to create. Regenerating inside Phase 4 means the drift cannot outlive the batch that
caused it.

**One surface is regenerated only when its input is present.** The surface census reads
`files/fulltext/`, which is gitignored and exists in one checkout while sessions run in
worktrees. Regenerate it when that directory is there, and skip it — without failing the
batch — when it is not:

```bash
test -d files/fulltext && python3 framework/scripts/surface_census.py --disease wwox \
    --out disease-models/wwox/research/surface_census.md
```

🔴 **Skipping is correct here, and is not a hole.** The census is a dated photograph of a
directory BATCH_COMMIT never modifies, so a stale one misleads nobody who reads its date and
listing digest — while aborting a propagation because a gitignored directory is absent would
be a gate over something the batch did not touch and cannot fix.

**Outside a batch commit, the landing path checks what this phase regenerates.** Direct
landings — a receipt recording, an operator-authorized propagation, an analysis commit
touching the full-text queue — change these surfaces' inputs without passing through this
phase, and that is how four of them went stale together (H0, 2026-09-24). `task_close.py` and
`scripts/legend_commit.sh` therefore run `framework/scripts/candidate_tree_freshness.py` on
the exact tree they are about to land and refuse a STALE surface, naming the command above
that regenerates it. A new generated surface needs a declaration there too (its inputs and its
check); until it has one, every landing reports it as CHECK_ERROR.

**One generated surface is a sealed data file, and regenerating it breaks a seal on purpose.**
The DisMech Phase-2 sidecar is derived from `CLAIM 016 / 024 / 035`'s registry blocks, so any
batch that touches one of those claims drifts it:

```bash
python3 disease-models/wwox/analysis/scripts/derive_dismech_sidecar.py \
    --out disease-models/wwox/analysis/data/dismech_sidecar_016_024_035.jsonl
```

🔴 **Then the Phase-2 baseline must be re-sealed, and that happens AFTER the propagation
commit.** `disease-models/wwox/analysis/data/dismech_phase2_baseline.json` pins the sha256 of
this sidecar and the scope hashes of the claim blocks it reads, and a seal may only record bytes
git can recover — so the order is *commit the propagation, re-seal, commit the baseline*, never
inside this phase:

```bash
python3 disease-models/wwox/analysis/scripts/reseal_dismech_baseline.py --check
python3 disease-models/wwox/analysis/scripts/reseal_dismech_baseline.py \
    --revision "rev.N (BATCH_ID, date): why" --absorb "CLAIM 016"
```

Every drifted sealed block must be named with `--absorb` (or already acknowledged in the drift
log): the resealer refuses otherwise, because on 2026-09-27 a re-seal silently absorbed a
`PAPER 019` scope drift that belonged to an earlier batch. Name only the blocks this batch
changed; a block you did not touch appearing in the refusal is a finding, not paperwork.

This surface was absent from this phase until 2026-09-27, when BATCH_20260927_003 corrected
`CLAIM 016` and its derivation suite went red *after* the batch closed — the same shape as the
`reading_state.md` omission above. It is a `.jsonl` whose bytes are hash-sealed, so it cannot
carry a "Generated by" header of its own: it is discovered instead from its declaration in
`framework/scripts/candidate_tree_freshness.py`'s `GENERATORS`, which
`test_generated_surfaces_are_regenerated.py` reads as a second discovery source.

**Derived surfaces that are computed on demand need nothing here.** `trace_claim_foundation`
and `build_evidence_index` write no file and are rebuilt from the registries on every call,
which is why they were designed that way: a derived artifact that is never stored cannot go
stale. Only add a command above when a generated file is actually committed.

> **If even a single change fails: ABORT + restore from the Phase 3 snapshot.**

---

### Phase 5 — Post-propagation LINT

Run `LINT_AUTOMATIC` on the post-propagation state.

| Outcome | Action |
|---|---|
| `PASS` or `INFO` | Proceed to Phase 6 |
| `WARN_BUT_PROCEED` | Proceed to Phase 6, record the warning |
| `BLOCK_BATCH_COMMIT` | ABORT + restore from snapshot, **with the Phase 3 base** |
| `BLOCK_SYSTEM` | ABORT + restore + escalate to the operator |

⚠️ **This is the post-propagation window.** By the time this LINT runs the propagation may already
be committed, so the restore is the ordered sequence Phase 3 states — `batch_commit.py restore`,
then `git checkout <PRE_BATCH_COMMIT> -- <path>`. A bare `git checkout -- <path>` here restores the
batch and reports success.

Logic: the pre-flight LINT verifies that you may start; the post-propagation LINT verifies that the result is coherent.

---

### Phase 6 — Manifest update

Update `state_manifest_current.md`:

```yaml
working_model_version: WM_vX.Y  # changed only when Phase 4.6 requires it
last_wm_update: YYYY-MM-DD  # preserve for a structural-only batch
last_wm_batch_commit_id: BATCH_YYYYMMDD_NNN  # preserve for a structural-only batch
last_batch_commit_id: BATCH_YYYYMMDD_NNN
last_batch_commit_date: YYYY-MM-DD
last_batch_commit_type: WEEKLY | THRESHOLD | MANUAL | URGENT
commit_candidates_propagated: N
target_wm_version: [achieved version]
trigger: [trigger type]
current_state: READY  # restore from IN_BATCH_COMMIT
```

Also update the 3.x sections of the manifest with the timestamps of the modified files.

The batch's `batch_<ID>_scope` and `batch_<ID>_candidates` — what it propagated, which the
backlog count reads — go at the top of the `yaml` block in `framework/state/state_history.md`
§ 4, newest first; nothing below them is edited. The manifest keeps only the current values
above, the history keeps every scope, and no value lives in both.

If an URGENT_COMMIT was authorized: remove the entry from `pending_urgent_requests` and mark it `AUTHORIZED_AND_EXECUTED`.

---

### Phase 7 — Commit-candidate cleanup

In `session_commit_log.md`:
- Mark the processed commit candidates as `PROPAGATED` with a reference to `BATCH_YYYYMMDD_NNN`
- Mark any `SUPERSEDED` with a rationale
- Do not remove from the queue — the queue is append-only

> **Never delete commit candidates from the queue.** Only mark them.

### 7.1 Re-point the receipts of everything this batch propagated

A deep-dive receipt names the artifacts the reading produced — which, before the commit, are
**staging drafts**. After propagation those drafts are no longer where the reading lives: it
lives in the canonical registries. Leave the receipt as it is and it keeps pointing at a
working file that the public edition never ships, so a fresh clone opens with
`UNRESOLVED_OUTPUT_FILE` and the reading history published to the world points at nothing.

For every receipt whose outputs name a path under a private root (`staging/`, `files/`,
`backup/`, `tmp/`, `overlay/`, `_qa/`):

```bash
# append a correction event; never edit the ledger by hand
python3 framework/scripts/fulltext_receipts.py record --receipt <correction.json>
```

The correction receipt carries `reread_reason: receipt_correction`, `prior_receipt` set to the
event it retires, and outputs re-pointed to the canonical landing (`paper_registry_current.md#PAPER NNN`,
`literature_tracking_log_current.md#LIT-NNNN`, plus the ledger/queue entries already durable).
Coverage, depth, analysis time, source locator and fingerprint are **carried over unchanged** —
this corrects where the output went, never what was read. History is not rewritten: the original
event stays visible in the chain and is simply superseded.

Enforced by `test_active_receipts_never_name_an_output_that_cannot_ship` in
`scripts/test_fulltext_trace_contract.py`.

### 7.2 Correcting the historical record of a completed act

🔴 **The working-model changelog is NOT append-only, and no normative file ever said it was.**
Two actors verified that independently on 2026-09-28: `LEGEND_CORE` § 5's append-only carve-out
list names the commit log, the activity log and the inbox, `state_manifest_current.md` § 3.3 names
the receipt ledger, and both lists are closed. `BATCH_20260928_001` corrected two historical
changelog rows in place and Mirror passed it as legitimate — correctly, because there was no rule
to break. This section is the rule, so the next batch is not deciding it again from scratch.

It governs every **historical record of a completed act**: a `## Changelog` row, `Last update`
note or MAJOR-batch section in `working_model_history.md` (in `working_model_current.md` until
`BATCH_20260928_004`), and a `batch_<ID>_scope` / `batch_<ID>_candidates` entry in
`framework/state/state_history.md` § 4.

**What MAY be corrected in place** — the *description of a past act*. What that batch did, which
candidate carried it, which record it touched, a count, a date, an identifier, a typo, a wrong
figure or panel reference. These are facts about the act, and a false fact about a past act is
worth more corrected than preserved.

**What may NOT be corrected in place** — the row's **stated conclusion**. A conclusion is
superseded by a **new row** that names the row it supersedes; the old row keeps its own words. A
batch that overwrites a conclusion destroys the only record that the model once held it, which is
the history the changelog exists to be.

**Every in-place correction carries three things inside the row it corrects:**

1. the **correcting candidate** (`CC-…`) and the **date**;
2. the **wording it replaces, verbatim** — short, quoted, in the row itself, e.g.
   `Fig 7d [corrected 2026-08-26 from "Fig 7b" by CC-20260826-GSK3B-S9-AXIS-01]`;
3. nothing else. The correction does not take the opportunity to improve neighbouring prose: it is
   a `replace-within` on the defective string, and the bytes around it stay.

🔴 **Item 2 is the one that is easy to skip and the only one that pays the cost Mirror named.** A
corrected row now carries a **forward reference** — it cites a candidate that did not exist when
the version it documents was released — so a reader working from the file alone can no longer
reconstruct what that version SAID at that version. That is a real loss and it is accepted, on the
condition that the superseded wording travels in the row. A marker without the old words trades a
false statement for an unreadable one. Git still holds the bytes; the file must not need it.

A row corrected this way is **not** a re-dated row: `frozen`/`released` dates, the version label
and the batch id are the act's own and never move. Correcting a row is not re-releasing a version.

This closes what `CC-20260826-GSK3B-S9-AXIS-01` `D2` left open — whether a completed batch's scope
record may be corrected in place with an inline marker. It may, on these three conditions. `D2`
reserved the *form* of that marker and condition 2 is now that form, so a future `D2`-shaped
correction is specified rather than escalated.

Final batch output:
- N commit candidates `PROPAGATED`
- M commit candidates `SUPERSEDED`
- K commit candidates `DEFERRED` (left in the queue for the next batch)

---

### Phase 8 — Activity log + change report

#### 8.1 Append to `legend_activity_log.md`

```markdown
## YYYY-MM-DD HH:MM — BATCH_COMMIT BATCH_YYYYMMDD_NNN

- type: WEEKLY | THRESHOLD | MANUAL | URGENT
- trigger: [...]
- pre-flight LINT: [outcome]
- commit candidates processed: N
- propagated: N
- superseded: M
- deferred: K
- working_model_version: [old] → [new]
- conflicts encountered: N (resolved: N, escalated: 0)
- post-propagation LINT: [outcome]
- snapshot path: /backup/YYYYMMDD_HHMM/
- pre-batch commit: <40-hex SHA, from Phase 3 / SNAPSHOT_BASE.json>
- duration: HH:MM
- outcome: SUCCESS | ABORTED | PARTIAL_RECOVERY
```

#### 8.2 Produce a change report

Structured output for the operator:

```markdown
# BATCH COMMIT REPORT — BATCH_YYYYMMDD_NNN

## Summary
- Type: [...]
- WM version: WM_vX.Y → WM_vX.(Y+1)
- Commit candidates propagated: N

## Files modified
- working_model_current.md (MAJOR/MINOR bump)
- claim_registry_current.md (N claims modified)
- paper_registry_current.md (N papers added)
- [...]

## Files unchanged
- [...]

## Key changes (clinically relevant)
[Narrative list of the operationally relevant changes]

## Conflicts resolved
[If any]

## Deferred to next batch
[If any]

## Recommended next actions
- [e.g. "review the research tier in light of new CLAIM 029"]
```

---

## 4. URGENT_COMMIT — VARIATIONS

When `MODE: URGENT_COMMIT`, the protocol is abbreviated but stricter on the critical checks.

### Phase modifications

| Phase | Standard | Urgent |
|---|---|---|
| 1 (Inventory) | All CCs | Only URGENT-marked CCs |
| 2 (Conflict) | Among all CCs | Between URGENT CCs and current state |
| 3 (Backup) | Mandatory | Mandatory (no skip) |
| 4 (Propagation) | All types | Only impacted files |
| 5 (Post-LINT) | Full LINT_AUTOMATIC | Full LINT_AUTOMATIC (no skip) |
| 6 (Manifest) | MINOR bump default | MAJOR bump default |
| 7 (Cleanup) | Standard | Standard |
| 8 (Log) | Standard report | Report with a visible URGENT flag |

### Authorization gate

> Before Phase 1, LEGEND must have explicit operator confirmation:
> *"I authorize URGENT_COMMIT [URGENT_ID] for category [N]"*

Without clear textual authorization → ABORT.

---

## 5. ABORT PROTOCOL

If at any phase the batch must be aborted:

1. **Immediate stop** of execution
2. **Restore from the Phase 3 snapshot** (all files to pre-batch values), then, for a tracked path
   the snapshot does not hold, `git checkout <PRE_BATCH_COMMIT> -- <path>` with the SHA Phase 3
   recorded. Never a bare `git checkout -- <path>`: once the propagation is staged or committed it
   restores the batch's own output and exits 0.
   `python3 framework/scripts/batch_commit.py base --snapshot-dir <path>` prints both.
3. **Update the manifest**: `current_state: BLOCKED_BY_LINT` or `BLOCKED_SYSTEM` depending on the reason
4. **Append to the activity log**:
   ```
   YYYY-MM-DD HH:MM — BATCH_COMMIT BATCH_YYYYMMDD_NNN ABORTED
   - phase reached: N
   - reason: [...]
   - snapshot restored from: [path]
   - pre-batch commit: [PRE_BATCH_COMMIT]
   - commit candidates left in queue: K
   ```
5. **Notify the operator** with an explicit ABORT report
6. The commit candidates **stay in the queue** unmodified for the next batch

> **Never a partial commit. All or nothing.**

---

## 6. ANTI-PATTERNS

What BATCH_COMMIT must never do:

- Never propagate a CC without a target_wm_version
- Never bump the version without a change log
- Never skip Phase 3 (backup) to "save time"
- Never skip Phase 5 (post-LINT) because "the pre-flight LINT passed"
- Never self-authorize an URGENT_COMMIT
- Never delete CCs from the queue (only mark them)
- Never a partial commit on error
- Never propagate a CC with an unresolved conflict
- Never promote a biomarker to "validated" without a validation paper
- Never put a Tier 3 endpoint in biomarker_candidates

---

## 7. WORKING_MODEL_VERSION RULES

### MINOR bump
- Addition of a new claim (in observation)
- Status update of a non-baseline claim
- Block update without a policy change
- Addition of a supporting paper to an existing claim
- Addition of a candidate biomarker / endpoint

### MAJOR bump
- Reversal of a baseline claim
- Policy change in the direct-clinical tier
- Authorized URGENT_COMMIT (category 1, 2, 3, 5)
- Retraction of a baseline paper
- Structural change to the Working Model

### Format
`WM_vMAJOR.MINOR_YYYY-MM-DD`

Example:
- `WM_v0.07_...` → `WM_v0.08_...` (MINOR)
- `WM_v0.08_...` → `WM_v1.00_...` (MAJOR for a reversal)

---

## 8. CHANGE LOG (this prompt)

| Date | Event |
|---|---|
| — | Created v3.3.1 — 8-phase protocol, URGENT variation, version-bump rules |

---

## 9. WIKILINKS

- Framework: [[LEGEND_CORE]]
- Lint prompt: [[prompt_lint_integrity_check]]
- State manifest: [[state_manifest_current]]
- Activity log: `legend_activity_log`
- Session commit log: `session_commit_log`
- Parallel protocol: [[parallel_legend_protocol]]

---

**End of `prompt_batch_commit.md`**

> BATCH_COMMIT is the write point. Everything else is preparation.
> All or nothing. Never a partial commit.

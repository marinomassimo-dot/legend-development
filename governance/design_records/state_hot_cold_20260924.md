# F0 — who reads the state manifest, for what, and what may leave it

> **Non-normative design record.** Hot/cold state AQP, block F0: a read-only census taken at
> `main` = `17834c5` **before** the manifest was edited. It decides whether the manifest can be
> split into current truth (hot) and history (cold) without loss. Nothing here binds an actor.

## Question

`framework/state/state_manifest_current.md` is read first by every session (`CLAUDE.md` § 0,
`AGENTS.md` § 1, `legend-start`, the scientist brief). At 77,352 bytes it was the largest
single surface in every first-read route. Which of those bytes does any reader need **now**?

## Method (reproducible)

- Consumers: every tracked file naming `state_manifest_current` or its path constant, each one
  opened and read at the call site — not classified from the filename.
- Sections: every heading, bytes from the heading to the next heading (`wc -c` semantics).
- Route bytes: a **static byte proxy** — the sum of `wc -c` over the surfaces each route's own
  documentation says to read whole at start (route definitions below). Not provider tokens.

## Readers

| Consumer | Kind | Reads | Fields / text relied on | Current | History | If history moves |
|---|---|---|---|---|---|---|
| `legend_lint.py` `_check_fulltext_receipts`, `_check_fulltext_declaration_ratchet`, `_check_sync_epochs` | exec | regex over whole text | `fulltext_ledger_path/_events/_head`, `registry_only_fulltext_*`, `sync_epoch_ledger_` | ✅ | — | nothing |
| `fulltext_receipts.py` `validate_state_anchor` / `write_state_anchor` | exec (R/W) | regex, exactly-one | `fulltext_ledger_events`, `fulltext_ledger_head` | ✅ | — | nothing |
| `sync_epochs.py` | exec (R/W) | regex, exactly-one | `sync_epoch_ledger_events/_head` | ✅ | — | nothing |
| `growth_anchors.py` `reanchor_manifest`, `check` | exec (R/W) | regex, exactly-one | growth anchors, both ratchets, `panel_relation_legacy_*` | ✅ | — | nothing |
| `growth_anchors.py` `measure_candidate_backlog` | exec | **whole text, folded** | every `batch_*_scope` naming a propagated candidate | — | ✅ | **breaks** — a propagated candidate would read as pending. Must read history too |
| `session_self_eval.py` | exec | regex | `unread_premise_baseline` | ✅ | — | nothing |
| `batch_commit.py` snapshot/restore | exec | whole file copy | — | ✅ | ✅ | a history file outside `EXTRA` would not be restored on ABORT |
| `scripts/test_freeze_scope.py` | test | regex | `fulltext_ledger_path` | ✅ | — | nothing |
| `scripts/test_fulltext_trace_contract.py` | test | substrings | `state-control`, `append-only`, `carve-out` (header) | ✅ | — | nothing if header stays |
| `framework/scripts/test_session_self_eval.py` | test | substring | `unread_premise_baseline: N` | ✅ | — | nothing |
| `test_locator_obligation…`, `test_no_closed_world…`, `test_stop_policy.py` | test | path in allow/deny lists | none | — | — | nothing |
| `test_batch_commit.py`, `test_fulltext_receipts.py`, `test_legend_lint.py`, `test_growth_anchors.py`, `test_sync_epochs.py` | test | temp fixtures | own synthetic text | — | — | nothing |
| `CLAUDE.md` § 0, `AGENTS.md` § 1, `legend-start`, `scientist_standing_brief.md`, `legend-discovery`, `legend-capability-scout`, `legend-dashboard` | instruction | whole file | `current_state: READY`, versions | ✅ | — | nothing |
| `legend-hypothesis-forge`, `legend-deepdive` (skill + agent) | instruction | whole file | READY, current WM version, gates | ✅ | — | nothing |
| `LEGEND_CORE.md` § 8, § 21b; `prompt_lint_integrity_check.md`; `unattended_delegation_readiness.md` | instruction | named fields | presence, gates, contents list | ✅ | — | nothing |
| `test_deepdive_manifest.py` docstring "see §6.4" | documentation | section number | § 6.4 | — | rationale | the pointer must still resolve |
| ~60 files in `learning/`, `reviews/`, `disease-models/**/analysis`, `commit_candidates/` | documentation | cited lines | historical line numbers (`:112`, `:141`) | — | — | already stale; resolved by the forwarding note in the history file |
| `framework/protocols/parallel_legend_protocol.md:124` | instruction | a section | "Parallel branches section" | — | — | **STALE**: that section was removed 2026-09-20; not touched here |
| `learning/plan/PLAN-MODULAR-EVOLUTION-001.md` → `runtime_parity.py` | documentation | a script | ROUTER_CHAIN | — | — | **DEAD**: no such script in the tree |

**Result:** 1 machine reader needs history (`measure_candidate_backlog`); every other reader
needs current fields only. No reader parses a section by heading or by position.

## Writers

| Writer | Section | Mode | Automatic |
|---|---|---|---|
| `fulltext_receipts.py record` / `anchor` | § 6.1 fields | regex substitution, exactly one | yes, in-lock on every append |
| `sync_epochs.py record` | § 6.1bis fields | regex substitution | yes (Plan only) |
| `growth_anchors.py record/tighten` | § 6.2 anchors, ratchets, § 6.5 panel fields | regex substitution | yes |
| `BATCH_COMMIT` Phase 6 (`prompt_batch_commit.md`, `legend-commit` step 6) | § 2, § 4 | hand edit: bump WM, set `last_batch_*`, **prepend** a `batch_<id>_scope` | manual |
| `LINT` runs, ingest (`legend-ingest` step 4) | § 5, § 6 | hand edit | manual |
| dated harness notes (`plan`) | § 7 | hand append | manual |

No writer rewrites the whole file; none computes a hash of the manifest itself.

## Sections at `17834c5`

| Section | Bytes | Role | Readers | Writers | Candidate | Reason |
|---|---:|---|---|---|---|---|
| header + § 0 | 1,232 | contract, purpose | trace-contract test, every bootstrap | — | HOT | declares the state-control carve-out |
| § 1–§ 3.4 | 3,902 | versions, current files | every bootstrap | batch Phase 6 | HOT | current truth |
| § 4 `last_batch_*` (3 fields) | 106 | current truth | bootstraps, candidates | Phase 6 | HOT | |
| § 4 `batch_20260921_002_scope` + count | 2,628 | last batch narrative | backlog | Phase 6 | F2 | narrative of an event |
| § 4 all earlier batches (30 lines) | 37,483 | chronicle | backlog only | Phase 6 | **COLD (F1)** | history; includes pseudo-current keys (`prev_batch_commit_id` ×3, `target_wm_version: WM_v4.4`, `last_wm_update`) that are stale |
| § 5 four fields | 150 | current truth | bootstraps | LINT | HOT | |
| § 5 `notes` | 11,380 | narrative of a 2026-08-06 reading | none | — | **COLD (F1)** | |
| § 6 gates + branch note | 746 | current truth | every bootstrap | — | HOT | |
| § 6 gate closed 08-09 / reopened 08-10 | 3,849 | narrative of a lifted gate | none | — | **COLD (F1)** | gate is `OPEN`; the residual PMID 17803050 surface debt is enforced by the validator (`SUSPECT`) and carried by `FT-041` |
| § 6.1, § 6.1bis | 2,138 | tail anchors | lint, receipts, epochs | tools | HOT | machine state |
| § 6.2 + two ratchets | 4,039 | anchors + rules for them | lint, growth, self-eval | tools | HOT (prose: F2) | fields are machine state; prose states live rules |
| § 6.4 | 3,972 | rationale + dated incidents | docstring pointer | — | F2 | no field; rules enforced by `deepdive_manifest.validate` |
| § 6.5 | 4,292 | rationale + panel ratchet fields | growth | tools | HOT fields / F2 prose | |
| § 7 dated notes | 1,484 | chronicle | none | `plan` | **COLD (F1)** | |
| § 7 public-edition paragraph | 265 | contract | — | — | HOT | |

## Baseline — static byte proxy at `17834c5`

Manifest 77,352 B · working model 53,902 B. Route definitions: `START` = `CLAUDE.md`, the
manifest, `LEGEND_CORE.md`, `legend-start`, `legend-capability-scout`, `legend-session-takeaways`,
`operator_manual.md`; each route adds what its own skill or brief names for its first act.

| Route (first-read startup) | Surfaces | Bytes | Manifest % |
|---|---:|---:|---:|
| `legend-start` | 7 | 150,211 | 51.5 |
| `legend` autopilot | 8 | 171,018 | 45.2 |
| scientist bootstrap (standing brief § 0) | 9 | 261,437 | 29.6 |
| discovery, first pass | 10 | 186,489 | 41.5 |
| deep-dive, first pass | 9 | 161,972 | 47.8 |
| forge (`SYNTHESIS`: WM, claims, discovery ledger, portfolio, biomarkers, hypotheses) | 14 | 1,045,668 | 7.4 |
| harness (`plan`) | 10 | 174,318 | 44.4 |

Routes loading the whole manifest at start: **7 of 7**. Routes that need its history at start: **0**.

## Pre-existing state defects found, not repaired here

- **Working-model version drift.** `working_model_current.md` declares `WM_v5.0_2026-09-22`
  (`BATCH_20260922_SEIZURE`, landed in `dd85c24`); manifest § 2 still says `WM_v4.5` and § 4
  `last_batch_commit_id: BATCH_20260921_002`. That batch never ran Phase 6. Correcting it is a
  `BATCH_COMMIT` Phase 6 act on scientific state, outside this AQP; the split preserves both
  values byte for byte and does not make the drift worse. No test detects it.
- **Pseudo-current keys in the chronicle.** § 4 carries `prev_batch_commit_id` three times with
  three values, and `target_wm_version: WM_v4.4` / `last_wm_update: 2026-09-09` from
  `BATCH_20260909_001`. Moving them to the history file removes them from the current surface
  without re-asserting them.

## Proposed boundary, risks, rollback

- **Hot** = `state_manifest_current.md`, current fields and the rules about them.
- **Cold** = `framework/state/state_history.md`, sections moved **verbatim** under their original
  headings, declared non-authoritative for current values.
- **Risks:** (1) the backlog reader → read both files; (2) `BATCH_COMMIT` ABORT → add the history
  file to `batch_commit.py` `EXTRA`; (3) a pending candidate naming `state_manifest_current.md:112`
  (the `Fig 7b` mislocator in `batch_20260810_005_scope`) → the history file states where text
  moved; (4) Phase 6 writers → one sentence in `prompt_batch_commit.md` and `legend-commit`.
- **Rollback:** `git revert` of the landing commit; both files are plain text and no ledger,
  hash chain or anchor refers to the moved bytes.

## Decision

All six F0 conditions hold: the current fields separate cleanly; every current reader is served
by the hot file unchanged; history stays one deterministic path away; there is still exactly one
file with current values; the only writer to adapt is a hand procedure plus one snapshot list;
the one hidden history consumer is known and adaptable. **F1 may proceed.**

---

# F1 — the first split

**Moved verbatim** from the manifest to `framework/state/state_history.md`, under the headings
they had: § 4's 30 chronicle lines (every scope before `BATCH_20260921_002`, the keys beside
them, the `BATCH_20260806_002` notes); § 5's `notes`; § 6's two gate subsections (closed
2026-08-09, reopened 2026-08-10); § 7's three dated harness notes. **Kept hot:** everything a
reader or writer in the census consumes, plus the last batch's scope (an F2 question).

**Losslessness** (script over `git show 17834c5:` against both new files): 393 non-blank
original lines; 392 found verbatim in exactly one file, or in both only as Markdown punctuation
(`---`, `>`, fences). One removed as **STALE_REFERENCE_FIXED** — § 0's *"active parallel
branches (if any)"*, whose field § 6 records as removed on 2026-09-20 (surviving authority: that
§ 6 note, and git). New lines: navigation pointers and the history file's provenance header;
no new value.

**Adaptations:** `growth_anchors.measure_candidate_backlog` folds both files separately (test:
a candidate named only in the history is consumed); `batch_commit.py` snapshots and restores
the history file (test: an ABORT restores it); Phase 6 (`prompt_batch_commit.md`,
`legend-commit`) says where the outgoing scope goes; `LEGEND_CORE.md` § 8 names the cold half.
§ 6.5's *"every `batch_*_scope` above"* now says where the scopes are.

| | Before | After F1 |
|---|---:|---:|
| manifest (hot) | 77,352 | 24,048 |
| history (cold) | 0 | 55,846 |
| total preserved | 77,352 | 79,894 |

Focused checks green: LINT `PASS`, `fulltext_receipts verify`, `growth_anchors check`,
`sync_epochs verify`, and 17 suites naming the manifest, its tools or its routes.

---

# F2 — the second cut: story out, rules in

Re-running the F0 census on F1's hot file found no reader of any remaining prose: executables
read the YAML fields, bootstraps read § 1–§ 6's values. So the question for each paragraph was
not *"is it read?"* but *"does it state a rule that binds now, or how a rule came to be?"* —
because the manifest is also where several of those rules are written down, and moving law
into a file declared to be history would demote it.

**Moved verbatim** to the history file:

| From | What | Why it is safe |
|---|---|---|
| § 4 | `batch_20260921_002_scope` + `_candidates` (2,628 B) | an event's narrative; the current fields (`last_batch_*`) stay; the backlog reader already reads the history |
| § 6.2 unread-premise | *"This is the failure mode that let PMID 22193544…"* | motivation; the ratchet's definition and its three clearing routes stay |
| § 6.4 | the 2026-08-04/06/10 incidents; why `panel_qualifies_text` was added; *"every admitted value was false"* | enforced by `deepdive_manifest.validate`; the enum, the pointer `BLOCK`, the needle rule stay |
| § 6.5 | the 2026-08-10 staging measurement; the `CC-20260726-001/002/003` first run | the derived-not-declared rule, the trigger-not-ratchet rule and the panel ratchet's rules stay |

**Kept deliberately:** *"Why the ID list and not just the count"* ends with the only hot sentence
saying the panel-ratchet fields are tool-written — a live rule, so the paragraph stays whole
rather than being split. § 3's file tables are derivable from the filesystem, but they are the
contents list `LEGEND_CORE.md` § 8 promises and cost 2.5 KB; derivation would not be safer.

**Writer contract after F2:** a batch writes its scope at the top of history § 4 and only its
current values in the manifest (`prompt_batch_commit.md` Phase 6, `legend-commit` step 6).

**Losslessness** (same script, against `17834c5`): 393 original non-blank lines; missing only
the F1 stale bullet and the two lines of § 6.5's sentence whose location (*"above"*) was corrected
to *"in `state_history.md` § 4"*. Two subsection headings appear in both files as navigation.

| Stage | Hot | Cold | Total preserved |
|---|---:|---:|---:|
| before | 77,352 | 0 | 77,352 |
| F1 | 24,048 | 55,846 | 79,894 |
| F2 | 18,671 | 62,076 | 80,747 |

Hot −75.9 % against the start; preserved bytes +4.4 % (navigation and provenance only).

---

# G0 — the working model: census, and why G1 does not run

`disease-models/wwox/registries/working_model_current.md`, 53,902 B at `e9db3ee`.

| Section | Bytes | Role | Readers |
|---|---:|---|---|
| title, version, date, public-edition note | 1,106 | current identity, contract | bootstraps, forge (*"current WM version"*) |
| three stacked `**Last update:**` lines | 6,934 | change notes — **and** live qualifications (`CLAIM 037` clause deleted as false, `CLAIM 005` retargeted) | every whole reader |
| Disease identity · genotype rules · worked examples A/B | 2,291 | current method | comparison routes |
| Mechanistic architecture (7 subsections) | 6,615 | current mechanistic model | comparison routes |
| BLOCK 1 one-pager | 5,873 | current data/inference split, safety, red flags | comparison routes |
| BLOCK 2 claim mirror | 10,450 | current claims | `legend_lint` (mirror ⊇ registry), `pathograph` (mirror titles) |
| BLOCK 3 · monitoring endpoints · gene-therapy context | 3,549 | current | comparison routes |
| `## Changelog` | 15,743 | version history | `test_canonical_structure` (pins it here), `pathograph` (excludes its rows by `HISTORY_ROW`) |
| `BATCH_20260714_001` repair | 1,312 | history **and** live qualification (`CLAIM 019` cause unresolved; stabilizer `conditional`) | comparison routes |

History-shaped subset: **23,989 B (44 %)** — larger than the inherited ~17 KB estimate, because
the `Last update` lines were not counted. **C1–C4 compliance holds:** `paper_packet.py` lists the
working model in `FORBIDDEN_SOURCES`; `legend`, `legend-discovery` (2b) and `legend-deepdive`
(stage 4) admit it only after the first pass; `legend-hypothesis-forge` loads it at start because
it is `SYNTHESIS` by definition.

**G1 decision: NOT IMPLEMENTED.** The F pattern is proven for the state manifest, and it does not
transfer, for reasons of law and of science, not of size:

1. The working model is one of the **four scientific current files, which change only through
   `BATCH_COMMIT`** (`CLAUDE.md` § 0). Moving its changelog is a canonical write; the state
   manifest is the one file with the carve-out that made F1/F2 legal.
2. The file declares itself *"canonical, complete … the full version changelog"*, and
   `test_canonical_structure.py` pins `## Changelog` with `BATCH_20260710_A`,
   `BATCH_20260714_001`, `WM_v2.1`, `WM_v3.0` inside it. Satisfying the test by rewriting it
   would change the contract, not follow it.
3. G0 condition 5 fails as the file stands: the `Last update` lines and the 2026-07-14 repair
   carry live qualifications. Moving them would hide qualifications; splitting sentences would
   be a scientific edit.

The route, if the operator wants it: a commit candidate proposing the split, propagated by
`BATCH_COMMIT` with the `test_canonical_structure` contract amended in the same batch.

# Adoption observation (one read-only sample)

C1–C4 and D0–D6 landed on 2026-09-24 between 21:14 and 21:47 UTC. The newest receipt in the
ledger is dated 2026-09-23, and no analysis, dossier or receipt has been written since. **There
is nothing yet to observe**: whether first contact is source-first, or whether a session falls
back to whole-registry reads, cannot be read from artifacts that do not exist. No telemetry added.

# Integrated context proxy (static bytes, not tokens)

| Route | Before F/G | After F/G | Δ | % |
|---|---:|---:|---:|---:|
| `legend-start` (first read) | 150,211 | 91,731 | −58,480 | −38.9 |
| `legend` autopilot (first read) | 171,018 | 112,538 | −58,480 | −34.2 |
| scientist bootstrap (first read) | 261,437 | 202,957 | −58,480 | −22.4 |
| discovery, first pass | 186,489 | 128,009 | −58,480 | −31.4 |
| deep-dive, first pass | 161,972 | 103,492 | −58,480 | −36.1 |
| harness (`plan`) | 174,318 | 115,838 | −58,480 | −33.5 |
| forge (`SYNTHESIS`, start) | 1,045,668 | 987,188 | −58,480 | −5.6 |
| legend comparison (added) | 181,764 | 181,764 | 0 | 0 |
| discovery comparison (added) | 195,221 | 195,221 | 0 | 0 |
| deep-dive synthesis, stage 4 (added) | 284,562 | 225,881 | −58,681 | −20.6 |

Each first-read row falls by 58,681 B of manifest and rises by the 201 B added to
`LEGEND_CORE.md` § 8. Whole-history surfaces required at ordinary startup: **1 → 0**.

# Benchmark J — FULL whole-file rewrite vs record-scoped editing · PREREGISTRATION

> **Harness evidence, non-normative, non-scientific.** Nothing here is a claim, a conclusion
> about WWOX or an edit to a scientific current file. The corpus is read from git objects; the
> replay runs in memory on historical bytes. Written and committed **before** the editor
> (`record_scoped_edit.py`, J1) existed and before any replay (J2).

## 0 · The question

`.claude/skills/legend-commit/SKILL.md` step 4 propagates a `BATCH_COMMIT` into the four
scientific current files by *"full rewrite, unchanged sections copied verbatim"*. Two ways that
can go wrong pull in opposite directions:

- a **full rewrite** can alter what it was told to copy — lose a line, reflow whitespace,
  reorder, truncate, or edit a record nobody meant to touch;
- a **record-scoped editor** — change only the addressed record or range, assert every other
  byte identical — cannot do any of that, but it may be unable to *express* an edit a batch
  legitimately makes (a changelog row, a mirror line, a separator, a new record in the right
  place), and a lost legitimate edit is worse than no guarantee.

Benchmark J measures both on the repository's own history. There is no desired winner: a
result that keeps the full rewrite is a successful benchmark.

## 1 · Corpus (J0) — measured at `main` = `e30b8ec`

- **Files** — what `framework/protocols/prompt_batch_commit.md` Phase 3 snapshots and Phase 4
  rewrites, restricted to what exists in this edition: the four current files
  (`working_model_current`, `claim_registry_current`, `paper_registry_current`,
  `literature_tracking_log_current`), the six `meta/*_current.md`, `research_lines_current`,
  `research_candidates_current`. Phase 4.7's generated surfaces are regenerated, not rewritten,
  and are out. The append-only ledgers (discovery, dismissal, full-text queue) are written by
  their own skills, not by the batch's rewrite, and are out.
- **Commits** — every non-merge commit in `git log --full-history --no-merges e30b8ec -- <files>`
  (the clone is complete, not shallow: 1,192 commits reachable from `e30b8ec`), minus the root (no parent to
  replay), plus every merge whose **combined** diff (`--cc`) touches a corpus file — an edit
  neither parent had. One exists (`56c1881`, a conflict resolution that also reconciled Mirror
  findings); it is replayed from the parent whose diff to it is smallest (`875d484`), and the
  messages of the commits it brings in from the other side count as its message.
- **Duplicates** — three commits are patch-identical copies (`git patch-id --stable` over the
  corpus files) of branch commits that landed twice. They are kept and replayed, flagged
  `duplicate_of`, and **every headline figure counts unique patches only**.
- **Unit** — `registry_records.partition` (added for this benchmark to the existing parser, so
  there is no second one): the file cut at its identity level (`IDENTITY_LEVELS`, D0) into
  contiguous blocks — preamble, records (`CLAIM 006`, `PAPER 101`, `LIT-0077`, `BLOCK 3`) and
  sections (`Purpose`, `Status vocabulary`). Fenced headings are not headings. Parent and child
  units are matched by key; a changed key is a rename only when both carry the same
  `Identifier` values; order changes are found by longest common subsequence.
- **Hunk** — each non-equal line opcode (`difflib`, no autojunk) inside a matched unit, or a
  whole added / deleted unit.

| J0 figure (unique patches) | Value |
|---|---:|
| events: (commit, file) pairs | **72** (80 with duplicates) over **26** commits (29) |
| per file | paper 22 · literature log 18 · claims 15 · working model 10 · meta 6 · research lines 1 |
| changed hunks | **708** (776) |
| unit events | 85 added units; 0 deleted, 0 renamed, 0 moved |

## 2 · Labels

| Label | Meaning |
|---|---|
| `INTENDED` | the target of the commit's stated change or of its commit candidate, including the mirror of that change in another file or section |
| `LEGITIMATE_COLLATERAL` | a required co-edit: version / last-update lines, changelog rows, cross-links, the separator a new neighbour needs |
| `ACCIDENTAL_COLLATERAL` | a substantive change to a unit the commit did not intend |
| `VERBATIM_COPY_DRIFT` | text that should have been copied verbatim and was not: whitespace, a lost line or separator, a lost unit, a reordering |
| `FORMATTING_ONLY` | a whitespace / separator change inside a targeted unit, or anywhere in a commit that declares itself structural |

## 3 · The labelling rule — a deterministic cascade, first match wins

A unit is **targeted** when its heading id is named in the commit message or in the added lines
of the commit's companion files (every non-corpus file it changed, minus the declared generated
surfaces and `growth_anchors.jsonl`, which enumerate every record), or when its `Identifier`
field carries an identifier so named. Ranges (`PAPER 081-092`, `LIT-0410-0416`) and lists
(`CLAIM 014/015`, `CLAIM 009, 011 and 036`) are expanded.

| Rule | Fires when | Label |
|---|---|---|
| R1 | the hunk touches only blank lines and `---` separators: added only → | `LEGITIMATE_COLLATERAL/separator`; removed, in a targeted unit or a structural commit → `FORMATTING_ONLY`; removed elsewhere → `VERBATIM_COPY_DRIFT/lost-separator` |
| R2 | removed and added text are equal after whitespace collapse | `FORMATTING_ONLY` in a targeted unit or structural commit, else `VERBATIM_COPY_DRIFT/whitespace` |
| R3 | every changed line is a version / date / last-update line | `LEGITIMATE_COLLATERAL/version` |
| R4 | the hunk sits under a changelog heading | `LEGITIMATE_COLLATERAL/changelog` |
| R5 | the hunk differs only in wikilinks, or only in link fields | `LEGITIMATE_COLLATERAL/crosslink` |
| R6 | the unit is targeted | `INTENDED/record` |
| R7 | the added lines name this commit's batch id (from its subject) | `INTENDED/batch-tagged` |
| R8 | the changed lines name a targeted id, or are a mirror row `\| nnn \|` of a targeted claim | `INTENDED/mirror` |
| R11 | every changed line declares a field, the fields share a word, and one sentence of the message sweeps that word (`every … Status`) | `INTENDED/field-sweep` |
| R12 | (commit level) the unit's id is named by the added lines of the commit's own `INTENDED` hunks — a promoted stub named by the record that replaces it | `INTENDED/linked-by-target` |
| R10 | a unit deleted and not targeted | `VERBATIM_COPY_DRIFT/lost-unit` |
| R9 | nothing above | **judgement** — labelled by hand in [`labels_spec.json`](labels_spec.json), each with its evidence |

Moved units: targeted → `INTENDED`, else `VERBATIM_COPY_DRIFT/reorder`. `ACCIDENTAL_COLLATERAL`
is reachable only by judgement: the cascade has no deterministic signal for "substantive but
unintended", so every hunk it cannot attribute goes to a human with the message in hand.

**Judgement-labelled items (listed in full in `labels_spec.json`): 14 hunks, 13 unique, all
`INTENDED`** — 7 evidence-depth lines a message declares by count (`a364dab`), 2 working-model
narrative lines a message quotes (`419b680`), 3 mirrors of a metadata correction and of a
narrowing (`ab5012e`, `d0f6a78` ×2), 2 copies of one vocabulary row (`254b971`, `752ae4a`).
**Share of judgement: 13 / 707 non-drift hunks = 1.8 %.**

### J0 label counts (unique patches; with duplicates in brackets)

| Label | Hunks |
|---|---:|
| `INTENDED` | **614** (679) |
| `LEGITIMATE_COLLATERAL` | **93** (96) — version 71 · separator 13 · changelog 9 |
| `ACCIDENTAL_COLLATERAL` | **0** |
| `VERBATIM_COPY_DRIFT` | **1** — a `---` separator that left `PAPER 095` when `PAPER 096` was inserted above it (`3f65917`): displaced, not lost; no text changed |
| `FORMATTING_ONLY` | **0** |

By rule: R6 476 · R3 71 · R11 44 · R8 35 · R7 31 · R12 15 · R1 14 · J 13 · R4 9.

**Sensitivity, pre-declared — message-only attribution.** With companion files ignored, 128
hunks fall to judgement (not re-labelled; reported only). The companion rule is therefore what
makes the cascade decisive, and it is generous by construction: a record a companion names is
treated as intended. **Limitation, stated before replay:** drift *inside* a targeted record is
labelled `INTENDED` by R6 and is invisible to this benchmark — and a record-scoped editor would
not prevent it either, since the author rewrites that record.

## 4 · J1 — the editor, specified before it is written

`framework/scripts/record_scoped_edit.py`, a new tool (not an extension of
`scoped_record_edit.py`, which edits one field of one JSONL ledger line under an operator
authorisation — a different object with a different contract). It reads and writes **bytes**,
parses with `registry_records` and nothing else, and supports:

- **anchors** — `--id <record id>` (identity token at the surface's identity level),
  `--heading <exact heading text>` (a section or a nested sub-block), `--preamble`;
- **operations** — `replace` (whole block), `replace-within` (an exact, unique old string inside
  the block → new string), `insert-before`, `insert-after`, `append` (end of file), `delete`;
- **post-conditions, asserted before anything is written** — the bytes before and after the
  edited range are identical to the input; every block other than the target(s) keeps its exact
  bytes (trailing `---`/blank separators excepted for the block that gains a new neighbour); the
  result re-parses to exactly the expected key set.
- **refusals** — anchor absent; anchor ambiguous (duplicate record id, duplicate heading); an
  anchor that exists only inside a fence; an anchor whose block contains another record (editing
  the parent would rewrite the child); replacement text that changes the block's own id without
  `--rename-to`; replacement / inserted text carrying a heading at or above the anchor's level
  that the operation did not declare (it would re-segment neighbours — the H1-swallowing
  defect D0 measured); `replace-within` whose old string is absent or not unique in the block.

## 5 · J2 — replay procedure

For every corpus event: E = its `INTENDED` + `LEGITIMATE_COLLATERAL` hunks.

- **Expected result X** — the parent with only E applied, unit by unit, independently of the
  editor: E-modified units take their E hunks, E-added units are placed after the nearest
  preceding unit that exists in the parent, E-deleted units are dropped, and every hunk outside
  E is left as the parent had it.
- **Operations** — derived from E alone: an E-modified unit → `replace --id/--heading` with its
  X text (primary mode, *record*) and, separately, one `replace-within` per E hunk (secondary
  mode, *range*); an E-added unit → `insert-after` its predecessor (or `insert-before` its
  successor, or `append`); an E-deleted unit → `delete`; a rename → `replace --rename-to`.
- **Result R** — the editor applied to the parent's bytes, operation by operation, in memory.

Measured per event, per file family, per mode: **(a)** `INTENDED` hunks reproduced exactly (their
unit in R equals X); **(b)** `LEGITIMATE_COLLATERAL` reproduced; **(c)** non-E hunks
(`ACCIDENTAL`, `DRIFT`, `FORMATTING_ONLY`) the editor would have prevented (R keeps the parent's
bytes there); **(d)** E hunks the editor cannot express — refused or not reproduced — each
diagnosed as `ANCHOR_AMBIGUOUS` · `ANCHOR_MISSING` · `FENCED_ANCHOR` · `NESTED_RECORD` ·
`RESEGMENTATION` · `PREAMBLE_OR_SECTION` · `IMPLEMENTATION_DEFECT` · `OTHER`. Also reported: events
where R is byte-identical to the actual child, and **silent corruption S** — an operation the
editor accepted whose result differs from X, or that changed a byte outside its range.

**Repair rule (as I1c).** A miss diagnosed `IMPLEMENTATION_DEFECT` is repaired within the
operation vocabulary of § 4, and every event is re-run; both runs are reported. A miss that needs
a new kind of operation or semantics is a **limitation** and stays a lost edit.

**Instrument control (pre-declared).** For each unique event, one planted mutation in the
actual child: the last non-blank line of the first unit that is neither targeted nor changed is
deleted. The J0 cascade must label the planted hunk non-`INTENDED`, and the replay built from the
mutated child must still equal X. Detection below 95 % makes the benchmark `INCONCLUSIVE`: a
labeller that cannot see planted drift cannot certify that the history had none.

## 6 · Decision rule (J3) — fixed now

Families: the four current files, one each. `meta/*` and `research_*` are reported, not decided
(6 + 1 events — below the minimum). A family is **eligible** with ≥ 5 unique events and ≥ 20 E
hunks. A family is **supported** when eligible, its lost-edit count L = 0 in the primary mode
after the repair rule, and S = 0.

- **SUPPORTED** ⇔ S = 0 overall, and all four current-file families are supported.
- **PARTIALLY_SUPPORTED** ⇔ S = 0, at least one family is supported, and every miss of every
  unsupported family is diagnosed — the supported families are the bounded subset.
- **NOT_SUPPORTED** ⇔ S > 0 anywhere (silent corruption is disqualifying whatever else holds),
  or no family is supported.
- **INCONCLUSIVE** ⇔ fewer than three families eligible, or the judgement share exceeds 10 % of
  non-drift hunks, or the instrument control detects under 95 %, or J2 could not run validly.

**What the verdict does not need.** SUPPORTED does not require observed historical drift: the
question is whether the editor can replace the rewrite *without losing legitimate edits*; its
benefit is a guarantee by construction. The observed benefit (c) is reported beside the verdict
and is not part of it.

## 7 · J4 consequence — fixed now

- SUPPORTED → wire the editor into the `BATCH_COMMIT` propagation path (protocol Phase 4, the
  `legend-commit` skill step 4) for all four current files; full rewrite remains only for a file
  the editor refuses, with the refusal recorded.
- PARTIALLY_SUPPORTED → the same, for the supported families only; full rewrite stays for the
  rest.
- NOT_SUPPORTED or INCONCLUSIVE → no production change; one evidence pointer beside the
  full-rewrite rule (as I3 did in the operator manual).

The parameters above are **frozen at this commit**. A post-hoc variant, if ever run, is labelled
post-hoc and decides nothing.

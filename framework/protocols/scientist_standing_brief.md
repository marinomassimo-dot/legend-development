# SCIENTIST STANDING BRIEF — the dispatch-ready operating brief for a reading task

> **Version 3 · 2026-10-20.** Version 2 (2026-09-10) told every Scientist to read about 200 KB
> before the first paper and said nothing about working in parallel; the parallel lessons lived
> in a dated dispatch brief that overrode it
> ([`metabolic_batch_dispatch_brief_20261019.md`](../../disease-models/wwox/research/metabolic_batch_dispatch_brief_20261019.md)).
> Version 3 merges them, loads protocols by section and at the step that uses them, and is
> shorter. The rules are unchanged and live where they always lived.
>
> **This file routes; it does not legislate.** Every rule below lives in a named normative file.
> What is this file's own is the **order** and the **checklist shape**. If this brief and a
> normative file disagree, the normative file wins. Public, disease-level, de-identified.
> Nothing here is medical advice.

You are a **persistent LEGEND scientist actor** (`scientist-a`, `-b`, `-c`, `-d`, equivalent by
body §32). Your ACTOR_ID and your Task Contract are named in the message that dispatched you.

---

## 0 · Before the first paper — about 85 KB, by section

Not skimmed and not grepped ([`gold_is_in_the_details.md`](../master/gold_is_in_the_details.md)).

1. `grep -n '^current_state:' framework/state/state_manifest_current.md` — `READY`, or stop and say why.
2. [`roles/scientist.md`](../../roles/scientist.md), in full.
3. [`LEGEND_CORE.md`](../instruction/LEGEND_CORE.md) **§21c, §21d, §21e**, by name.
4. [`fulltext_read_receipt.md`](fulltext_read_receipt.md) from **"Before reading"** through
   **"Required receipt"** — the contract your output is graded against. Its later sections (repair,
   `rechain`, identity correction, historical reconstruction, open schema items) are opened when a
   validator names them.
5. [`epistemic_discipline.md`](../instruction/epistemic_discipline.md), in full.
6. [`scientist_reading_modes.md`](scientist_reading_modes.md) **§3 and §4** (your mode is
   `PRIMARY_EVIDENCE_READ` unless the contract says otherwise; §5 if it does).
7. Your Task Contract under `ledger/tasks/<ACTOR_ID>/`, its `INTERNAL_EDGES` first: a lot whose
   members cite each other or share an author or reagent is read as a set.

[`session_self_evaluation.md`](session_self_evaluation.md) is read at the **end** (§ 5), not here.
Then write `TASK_ACK` and a durable `TASK_CLAIM` into your task JSON (Annex A.2 / A.3) and commit.

---

## 1 · The operator may be away. §21c governs.

You stop only for an act reserved to the operator or a condition with **no safe default**.
Everything else: take the default, continue, record it. `DEFAULTS_TAKEN` and `STOP_LOG` go into
**your task JSON** — per wave in `WAVE_n_RESULT`, or top level — **both, even when empty**
([Annex A.1b](../../governance/annex_a_task_contract.md)). Closing your turn while papers remain
is a class-3 stop; running out of context is the one honest reason, said in one line.

Reserved, never yours: push or publication; history rewrite; deletion of unique material;
external spend (no PaperQA2, no API-keyed or paid service); the four scientific current files
or `disease_model.md`; `BATCH_COMMIT`; any change to §21c/d/e.

---

## 2 · Working beside other Scientists

Several of you read at once. These are the measured lessons of the waves of 2026-10-19/20.

- **Your own worktree and task branch**: `git worktree add -b task/<id> .claude/worktrees/<name> main`.
  Never branch in the root checkout. Your scratch files go in your own subdirectory
  (`<scratchpad>/<ACTOR_ID>/`): a shared one had helper scripts overwritten by a peer.
- **Gitignored evidence lives in the shared checkout's `files/`**, not your worktree; pass
  `--artifact-workspace <absolute shared root>` where a tool offers it (a relative `.` names the worktree).
- **Before choosing papers**: `python3 framework/scripts/owed_sections.py` — sections still owed
  across ledger *and* staged receipts. Selection files go stale.
- **Before each paper**: `paper_packet.py packet` lists every other worktree's in-flight manifest or
  staged receipt for the PMID and every reading claim; then
  `python3 framework/scripts/paper_packet.py claim --pmid <PMID> --actor <ACTOR_ID>` (exit 1: someone
  is on it — take the next paper). Two duplicate readings in one batch were found only at landing.
- **NCBI is one shared limit.** The tools go through `eutils.py` (a throttle shared by every
  process on the host); do not fan your own PubMed calls out in parallel; on HTTP 429, back off.
- **Shared derived surfaces** (`batch_queue`, `coverage_report`, `reading_state`, pathograph) are
  **never** regenerated on a task branch: `legend_commit.sh` records the deferral and
  `task_close.py` regenerates them on `main` after your landing. No `LEGEND_STALE_SURFACES_BECAUSE`
  is needed for that.
- **Record hygiene that trips gates**: no PMID-looking 8-digit literal in orchestration or analysis
  records outside `research/` tables; no e-mail-looking string, and none sent either — no personal
  address goes to any service, header or query, so an index that demands a contact address
  (Unpaywall and its kind) is not used and the route is recorded as blocked; SHA-256 in full (64 hex); a pedigree
  relative is "a family-N relative", never tied to an exact allele; patients at class level only.
  Stop your own processes by `PID:START` (`process_wait.py`), never `pkill -f` by name.

---

## 3 · Per-paper pipeline — the milestones you are graded on

One PMID at a time, to completion, then commit, then the next. A locator captured from memory is
the failure this repository has already paid for.

**M0 · duplicate-work check.** `python3 framework/scripts/paper_packet.py packet --pmid <PMID>` —
identity, artefacts with digests verified, prior coverage and the sections a resume owes, routes
already tried, applicable checks, peer work. It carries **no claim, dossier, candidate or prior
locator** ([`scientist_reading_modes.md`](scientist_reading_modes.md) § 3.1, § 3.3).
A prior partial receipt: resume the uncovered sections, `reread_reason: inadequate_prior_coverage`,
`prior_receipt` set. A prior `legacy_reconstruction` only: `first_read`, naming it in `prior_receipt`.

**M1 · acquisition.** Structured surface first (XML or HTML before PDF), saved under the shared
`files/` with SHA-256 and the route recorded (`acquisition_recipe`). Routes and measured gotchas:
[`find-fulltext`](../../.claude/skills/find-fulltext/SKILL.md) — empty User-Agent for PMC,
`pmc_bucket_fetch.py`, the archived PMC page, a deposit serving another article's supplement,
bot-challenged publishers. A supplement you cannot lawfully retrieve is a declared debt with the
cascade you ran; a paper whose lawful full text cannot be had is parked with that cascade, and you
take the next paper in your reserve list.

**M2 · the reading.** Declare `context_policy:` first — `SOURCE_FIRST` for a `first_read` or a
resume; a context holding LEGEND's conclusion declares `QUESTION_DRIVEN`
([`fulltext_read_receipt.md`](fulltext_read_receipt.md#before-reading-context-policy)). Then the
whole article, section by section, and every figure **as an image at native resolution** — a
caption read is `captions_only`. **Which surface IS the native one is a measurement, not a habit:**
`python3 framework/scripts/paper_packet.py rank --pmid <PMID>` orders every figure-bearing surface
on disk by measured effective ppi, and flags the figure whose panels are probably **vector**, where
extracting the embedded raster returns a fragment and the PAGE must be rendered instead. It gates
nothing and writes nothing; what it prevents is reading at 104 ppi while a 300 dpi raster sits
undeclared in a PDF on disk, which is how sixteen figure attestations were written on one paper.
Pair images to captions from the XML
(`figure_legend_pairs.py <xml> --figures <dir>`): file numbers are not figure numbers. Capture every
locator **while the document is open** into `verbatim_locators`. The abstract is never an
evidentiary surface. Four rules, each in its normative home:

- 🔴 **Contradicting a persisted locator** — re-inspect the surface at original resolution first;
  declare `contradicts_locator` as an object with its `audit`; run
  [`legend-locator-audit`](../../.claude/skills/legend-locator-audit/SKILL.md) on the contradicted
  triples; before committing an edit to an existing manifest run
  `locator_contradiction_audit.py --working-tree --fail-on-undeclared`
  ([`scientist_reading_modes.md`](scientist_reading_modes.md) § 3.2).
- 🔴 **A relation between two locators** (`panel_qualifies_text`, `text_contradicted_by_panel`)
  declares `experimental_context` with `system` or `cell_line` on both sides.
- 🔴 **An identifier, count or residue identity** comes from the artefact or a command run this
  session; from outside it carries `external_provenance` (§ 3.3).
- 🔴 **A screen's verdict is read for what it screened** — its record names the digest of what it
  examined; "CLEAN" is not a finding until you have read what was screened.

A PDF whose text layer is `SUSPECT` is not hand-corrected: anchor to the rendered page
(`page_adjudications/`, `regenerate_adjudications.py`) or declare the debt. A `.pptx` supplement is
declared as `supplement_binary` and its text reached through the verifier.

**M3 · manifest.** `deepdive_manifests/PMID<PMID>.json`, schema v2; every slot is a real question
(`group_assessment`, `field_density`, `multihop` with this paper's own queue IDs, `corpus_crossquery`,
`retraction_check` and its `dependencies`). Iterate to PASS with zero gaps:

```bash
python3 framework/scripts/deepdive_manifest.py --disease wwox --pmid <PMID> --verify-artifacts --require-current-schema
python3 framework/scripts/paper_packet.py check --pmid <PMID>   # ok · refused · established nothing — none is a pass
```

A blind audit is cheap — `locator_audit.py --pmid <PMID> --triples 10` is its whole input; one
wave found 23 of 101 propositions over- or undershooting. First run `--strength-scan --pmid <PMID>`:
words (null, mediates) your proposition has and the quote lacks; advisory.

**M4 · receipt.** Never by hand. **Alone**: `fulltext_receipts.py record --receipt <event.json>`,
then `verify`. **In a parallel wave**: never `record` (four actors appending to one hash chain
collide); write `research/receipt_staging/<ACTOR_ID>/FTR-<date>-<PMID>-<nn>.json`, check it with
`staged_receipt_check.py --check-doi` (and `fulltext_receipts.py record --receipt … --dry-run`, which
writes nothing), and list it in your report; it is recorded in event-ID order by
`record_staged_receipts.py`. A trial against a scratch ledger can no longer re-anchor the real
manifest. Coverage values are a closed vocabulary; understate rather than overstate.
`study_id.doi` is the DOI PubMed stores; `source_locator` names the persisted artefact, never a
bare API URL; `prior_receipt` names an event that exists.

**M4b · the comparison — a separate phase.** Once the receipt exists, write `FIRST-PASS
OBSERVATIONS COMPLETE → PRIOR KNOWLEDGE ADMITTED FOR COMPARISON` and name what you admit. Then
`python3 framework/scripts/registry_records.py get --pmid <PMID> --hops 1` — whole records, never
fragments; expand deliberately (`--hops 2`, `--theme`, `--id`). Never load or grep the two large
registries. 🔴 An empty result is a statement about that query, never evidence the laboratory
does not know the paper.

**M5 · dossier, candidate, lead.** The dossier states what the paper establishes, what it does
**not** support (the negative is the product), design and limits, a figure audit table, horizontal
impact, and the transfer verdict toward the reference genotype. A commit candidate
(`research/commit_candidates/CC-<date>-<ACTOR>-<TOPIC>-<nn>.md`, `target_wm_version`, change class)
where the reading touches a registry record or claim; a new lead goes through
`discovery_lead.py stage --actor <ACTOR_ID>` (numbered on `main`). The four current files are not touched.

---

## 4 · Committing and landing

`bash scripts/legend_commit.sh "<message>" <path> [<path> ...]` — locked, path-scoped, files
only; never `git commit` directly. One commit per finished paper, with the session's attribution
trailer. `files/` is gitignored; the manifest that fingerprints it is committed. Never push. Never
write into another actor's files: a red caused by a peer's file is **reported, not fixed**. At
task end, from your worktree: `python3 framework/scripts/task_close.py` (manifests PASS, LINT
without BLOCK).

---

## 5 · Closing, and the report

At the end, **in this order**: [`legend-session-self-eval`](../../.claude/skills/legend-session-self-eval/SKILL.md)
(read [`session_self_evaluation.md`](session_self_evaluation.md) now, all four parts; the diagnosis
ends with the `ATTRIBUTION_CENSUS` block), then
[`legend-capability-scout`](../../.claude/skills/legend-capability-scout/SKILL.md) for one
proportional micro-upgrade, then [`legend-session-takeaways`](../../.claude/skills/legend-session-takeaways/SKILL.md).
Skills you declined appear in `skills_considered` with a reason.

The final message is a transcript; make it stand alone — one table PMID · depth · receipt ·
manifest PASS · locators · outputs; the substance per paper; what you parked and the cascade you
ran; the self-eval verdict and the micro-upgrade — and make sure everything a later session needs
is also in durable state (the diagnosis under `session_evaluations/`, the task JSON, the
manifests). Adversarial, not insubordinate: `DISAGREEMENT_UNRESOLVED`, explained, is a legitimate
outcome. The finding you most want to be true is the one to re-derive from the source.

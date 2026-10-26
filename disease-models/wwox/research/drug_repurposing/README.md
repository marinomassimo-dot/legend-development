# Drug repurposing — external deliverables and their reconciliation

Non-canonical research material. Nothing in this directory changes the four scientific current
files, and nothing here carries a `FULLTEXT_READ_RECEIPT`. Placed and written by Harness
Engineering (`plan`) on 2026-10-20, task `PLAN-REPURPOSING-INTEGRATION-20261020`.

| File | What it is | How to read it |
|---|---|---|
| [`roadmap_v4_r14_20261020.md`](roadmap_v4_r14_20261020.md) | Operator-supplied external deliverable: the drug-repurposing roadmap, v4 revision 14, authored outside this repository and received 2026-10-20. Italian body, quoted verbatim under an English provenance header | **A plan, not a state.** Its `ADOTTATO NEL_PIANO` means a planning decision — never a verified installation and never a scientific claim. Its SHAs and baselines are as of its own authorship |
| [`scout_log_r20_20261020.md`](scout_log_r20_20261020.md) | Operator-supplied external deliverable: the cumulative scout register, revision 20, daily checkpoints 2026-10-08 → 2026-10-20. Italian body, quoted verbatim under an English provenance header | **Documentary scouting, not reading.** Its inspections are READMEs, diffs and abstracts; its scores are editorial self-assessment. Nothing in it was installed or executed |
| [`reconciliation_20261020.md`](reconciliation_20261020.md) | **Start here.** What is measurably present on this host and in this repository, component by component and step by step, with the command and output for each | Separates *adopted in the plan* from *installed* from *verified to work*. Carries the real P0, the re-measured pathograph counts and the corrected baseline SHA |
| [`woree_rescue_reference_scaffold.md`](woree_rescue_reference_scaffold.md) | A scaffold for the Scientists: the five endpoint families with the eight columns each row must bind. Pre-filled only with what the roadmap itself attributes, every such cell marked `TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD` | To be filled from the repository's own receipted reading of PMID 42422765, not from the roadmap. It is not Q230P evidence and not a reusable RNA-seq rescue signature |
| [`clinical_census_20261020.md`](clinical_census_20261020.md) · [`clinical_census_20261020.json`](clinical_census_20261020.json) · `clinical_census_20261020_raw/` | The ClinicalTrials.gov API v2 census of 2026-10-20 — **written by the actor who held the clinical-census task**, not by the reconciliation. Seven unfiltered queries, their stored per-page responses (contact values redacted), and what each returned | A retrieval record, not a claim: no registered WOREE interventional study on that registry on that date, with `NO_MATCH` kept strictly apart from absence. The reconciliation's § 4.4 cites it instead of re-running it |

The headline of the reconciliation, in one line: **nothing the plan proposed to install is
installed, everything it proposed to reuse exists and runs, and on the rescue reference the
repository is already well ahead of the plan** — twelve receipts, one of them a complete
full-text read, against the plan's abstract. Its verdicts are dated 2026-10-20; two of them
(the ClinicalTrials.gov route and the Spectrum manifest row) moved the same day and are folded
in with their dates rather than rewritten.

Not medical advice. No dose, administration or individual recommendation appears in this
directory.

---

## The rest of the capability, and where it lives

This directory holds the **documents**. The **code** cannot live here: `framework/` is the generic
engine and `disease-models/wwox/` is one disease model, so a tool that would work for another
disease belongs to the engine (`ARCHITECTURE.md`). What follows is the routing, so this README is
the single door even though the files are where the architecture puts them.

| Component | Path | Origin | Stage, measured 2026-10-21 |
|---|---|---|---|
| Candidate-card builder | [`framework/scripts/repurposing_bridge.py`](../../../../framework/scripts/repurposing_bridge.py) | `codex/drug-repurposing-bridge`, landed 2026-10-20; extended the same day | **Runs, tested, enrolled.** 8 regressions green, routed in the scripts README, in the release battery. Builds non-canonical cards from explicitly qualified local assertions: no network, no ranking, no score, and the direction is a comparison on the same target, endpoint and context. States `MATCH_FOUND` / `NO_MATCH_FOUND` / `QUERY_ERROR` / `NOT_ATTEMPTED` with coverage on an independent axis, and carries the later P4 fields as `UNKNOWN` rather than absent |
| Its design note | [`docs/repurposing_bridge_20261015.md`](../../../../docs/repurposing_bridge_20261015.md) | same branch | Documentation only |
| Clinical-trial census | [`framework/scripts/clinical_census.py`](../../../../framework/scripts/clinical_census.py) | written 2026-10-20 after establishing no access already existed | **Runs, tested, enrolled, and has been run for real.** 21 regressions green. ClinicalTrials.gov API v2, read-only, key-less, standard library only. Its output of 2026-10-20 is the census in this directory |
| Monarch / DGIdb slice | [`.claude/skills/legend-hypothesis-forge/scripts/kg_thin_slice.py`](../../../../.claude/skills/legend-hypothesis-forge/scripts/kg_thin_slice.py) | `codex/…` branch, then hardened 2026-10-20 | **Runs, tested, enrolled.** 22 regressions green. Separates genes from pathways before the DGIdb query, resolves identifiers with type and taxon, paginates for real or says it truncated, and reports `QUERY_ERROR` / `API_ERROR` / `INCOMPLETE` / `UNMATCHED` as states distinct from no result. The approved-only filter is now a choice, not a silent default |
| Evidence-bridge reference | [`.claude/skills/legend-hypothesis-forge/references/evidence_bridge.md`](../../../../.claude/skills/legend-hypothesis-forge/references/evidence_bridge.md) and its example JSON | same branch | Reference for the skill |
| Surface ranking for a figure read | [`framework/scripts/paper_packet.py`](../../../../framework/scripts/paper_packet.py) `rank` | 2026-10-21, provoked by this line of work | **Runs, tested, enrolled.** Run it before any figure read: it measures effective ppi per surface and flags a likely-vector figure rather than offering its raster |

### The module (added 2026-10-23, `PLAN-DRUGREPURPOSING-MODULE-20261022`)

**Follow-up of 2026-10-26** ([`lucas_clarke_followup_20261026/`](lucas_clarke_followup_20261026/README.md)): 341 queries, 28 cards, 28 handoff rows (adds the REPLICATE rows `Q-R-10`, `Q-R-11` from two new mechanism-map records), four E-series hand-made cards, the first measured source-coverage declaration of the join, and one ToolUniverse trial.

**Refresh, 2026-10-25:** 339 queries, 26 derived cards, 8 evidence-table abstentions; the
[current handoff](../repurposing_batch_selection_20261025_module.md) has 8 AUDIT, 16 READ and
2 REPLICATE rows, with no SELECT. READ includes evidence comparison and does not cancel
complete-read receipts. All 26 cards still abstain from drug assertions. The [weekly intervention](../weekly_write_intervention_20261025.md)
records the source-link repairs, audit limits and real adapter checks. The original module
mandate is COMPLETE; its permission-mode pause was resumed on 2026-10-23.

| Piece | Path | How to run it |
|---|---|---|
| Survey of external sources, with measured dry calls | [`tool_survey_20261022.md`](tool_survey_20261022.md) · [`tool_survey_20261022_drycalls.json`](tool_survey_20261022_drycalls.json) | read |
| One-file adapters (Open Targets, ChEMBL, PubTator 3, openFDA, Orphadata, iLINCS) | `framework/adapters/`; convention `framework/protocols/repurposing_adapter_convention.md` | `python3 framework/scripts/repurposing_adapter.py selftest --live` (offline without the flag) · `python3 framework/scripts/repurposing_adapter.py list` · `… query <name> '<json>'` · `… add <name>` · `… remove <name>` |
| Acknowledgements and licences, rendered from the adapters | [`ACKNOWLEDGEMENTS.md`](ACKNOWLEDGEMENTS.md) | `… repurposing_adapter.py acknowledgements --write` |
| The join: queries from the registries, receipted evidence table, derived cards, measure-next | [`join/`](join/) | `python3 framework/scripts/repurposing_join.py run [--axis …] [--live]` (prints what changed) |
| The feedback loop: one assignment row per card for the next batch | [`repurposing_batch_selection_20261025_module.md`](../repurposing_batch_selection_20261025_module.md) | `… repurposing_join.py handoff --date <YYYY-MM-DD> --write <file>` |
| Proof on the three live axes, both directions | [`module_proof_20261023.md`](module_proof_20261023.md) | read |

### Stage of the capability as a whole (re-measured 2026-10-23)

| Roadmap step | State |
|---|---|
| P0 preflight | **done and measured** — `reconciliation_20261020.md` § 2; re-measured 2026-10-22 (`tool_survey_20261022.md`): network open, no R, Python 3.12 |
| P1 installations | **superseded by adapters.** Nothing is installed and nothing needs to be: six key-less services answer direct calls under a second and sit behind one file each. ToolUniverse and OptimusKG are WATCH / TRY; drugfindR and CDRPipe stay blocked (no R) |
| P2 Monarch/DGIdb hardening | **done** (`kg_thin_slice.py`) |
| P3 scientific qualification | **under way** — known roads censused, early-benefit endpoints mapped, the rescue reference bound; the pathograph's 46 edges are still untyped |
| P4 candidate cards | **done twice**: 21 hand-made cards (`cards/`, `cards_early/`, blind-audited once) and 26 derived cards (`join/cards.json`, regenerated by one command). The two sets are complementary — `module_proof_20261023.md` § 2–3 |
| P5 two-path comparison | **done as what to measure, not whom to choose** (`p5/`): all candidates non-dominated; the join adds a measured dependence per candidate |
| P6 signature reversal | **block lifted, query INCONCLUSIVE** (`gse156243/`); the iLINCS adapter gives the signature census. 2026-10-26: context stratification names the limit (one signature family fills both tails; no content-matched null; shuffled control empty) — `gse156243/prediction_lincs_context_stratification_20261026.md`; a second reversal route via ToolUniverse tested, narrow use — `tooluniverse_capability_test_20261026.md` |
| P7 gold-set evaluation | **not started**; no gold set exists and none was invented |
| P8 context / delegation | **not started** |
| Feedback into research | **done; refreshed 2026-10-25**: 26 rows (8 AUDIT, 16 READ, 2 REPLICATE), rendered from the current cards; the initial 2026-10-23 measurement remains in the dated proof |

Nothing in this capability has produced a therapeutic recommendation, and no output of it is a
`DATO`. The clinical census is a retrieval record; the bridge's cards would be `IPOTESI`.

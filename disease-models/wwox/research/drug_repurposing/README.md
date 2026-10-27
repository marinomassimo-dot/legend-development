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
| [`p3b1/`](p3b1/txgnn_matrix_outcomes_20261026.md) | Package P3B-1 (2026-10-26, `scientist-d`): the evaluation of TxGNN (**reasoned wait**) and Every Cure MATRIX (**inconclusive trial**; scores licence undeclared), with four stdlib/duckdb scripts and aggregate outputs. Recorded as rows 13-14 of `tool_survey_20261022.md` § 5 | Discovery-depth evidence from databases and documentation; no paper was read, no prediction is kept, nothing is installed. Not a second plan: the roadmap's "additional predictor between TxGNN and K-Paths" line is answered here |

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
| P1 installations | **superseded by adapters** (2026-10-26: the MATRIX-sample and TxGNN items of the plan were evaluated in `p3b1/` — scores unusable until a licence is stated, TxGNN waits for retrievable predictions). Nothing is installed and nothing needs to be: six key-less services answer direct calls under a second and sit behind one file each. ToolUniverse and OptimusKG are WATCH / TRY; drugfindR and CDRPipe stay blocked (no R) |
| P2 Monarch/DGIdb hardening | **done** (`kg_thin_slice.py`) |
| P3 scientific qualification | **under way** — known roads censused, early-benefit endpoints mapped, the rescue reference bound; the pathograph's 46 edges are still untyped |
| P4 candidate cards | **done twice**: 21 hand-made cards (`cards/`, `cards_early/`, blind-audited once) and 26 derived cards (`join/cards.json`, regenerated by one command). The two sets are complementary — `module_proof_20261023.md` § 2–3 |
| P5 two-path comparison | **done as what to measure, not whom to choose** (`p5/`): all candidates non-dominated; the join adds a measured dependence per candidate |
| P6 signature reversal | **block lifted, query INCONCLUSIVE** (`gse156243/`); the iLINCS adapter gives the signature census. 2026-10-26: context stratification names the limit (one signature family fills both tails; no content-matched null; shuffled control empty) — `gse156243/prediction_lincs_context_stratification_20261026.md`; a second reversal route via ToolUniverse tested, narrow use — `tooluniverse_capability_test_20261026.md` |
| P7 gold-set evaluation | **not started**; no gold set exists and none was invented; 2026-10-27: a small work-quality probe of what local knowledge contributes (5 cases, 3 conditions, rubric from primary sources) is in [`knowledge_contribution_trial_20261027/`](knowledge_contribution_trial_20261027/README.md), not a gold set |
| P8 context / delegation | **not started** |
| Feedback into research | **done; refreshed 2026-10-27**: 28 rows (8 AUDIT, 16 READ, 4 REPLICATE) in `repurposing_batch_selection_20261027_module.md`; curated observations are consumed with scope, track and route as separate fields, and an unmatched row says why (`cause`); the 2026-10-23 measurement remains in the dated proof |

### Roadmap iteration 1 (2026-10-26 to 2026-10-27) — measured state

Each line links its evidence. Every decisive scientific conclusion below was checked by an actor
other than its producer (`../locator_audits/2026-10-27_*`). None is therapeutic efficacy.

| Item | Outcome | Evidence | Next step |
|---|---|---|---|
| Phase 1, module linkage | **done**: evidence scope and track/route are no longer assigned wholesale; curated observations arrive intact; target → compounds reads the DGIdb/ChEMBL/Open Targets retrievals already run (identity, action, query status, truncation); Q-R-10/Q-R-11 classified from observations, not abstract words | `join/` tests (42), `lucas_clarke_followup_20261026/regeneration_proof.md` § 6, `../locator_audits/2026-10-27_p1_curated_links_verification.md` | link a curated card to each of the 25 still `UNQUALIFIED` derived cards when one exists |
| Phase 2, LDH precedent | **Sada 2015 not lawfully acquirable** (wishlist 16, 17); stiripentol potency on LDH **unresolved**, not closed; read instead: Rico-Molina 2024 (partial) and five open papers at targeted passages | `sada_ldh_precedent_p2a_20261026.md`, audits `…PMID39769031_blind_audit/_reaudit/_reaudit2.md` | the operator's copy of Sada 2015, or a cell-free assay with the racemate and both enantiomers side by side |
| Phase 2, "PDH activity unchanged" | traced to PMID 35328751 Results 2.5 + Fig 5b only (non-significant, n unstated; "PDK" in that sentence is a PDH mislabel); neither confirmed nor refuted | `../p2b_pdh_trace_and_lactate_reconciliation_20261026.md`, `../locator_audits/2026-10-27_p2b_pdh_lactate_independent_read.md` | a PDH-specific measure (activity, phosphorylation or flux), not lactate or Seahorse alone |
| Phase 2, lactate wording | the three terms all pass the paper's 10% FDR; interaction, main effects and the simple contrast kept apart | same | none |
| Phase 3A, work-quality probe | A 22.0 / B 25.0 / C 25.5 of 29 (external only / local only / both); n = 5, one run each, same-model, rubric overlaps the cards: the C–B gap is not a finding | `knowledge_contribution_trial_20261027/`, `../locator_audits/2026-10-27_p3a_trial_verification.md` | repeat with cases the cards do not encode |
| ToolUniverse | **useful use, narrow** (L1000FWD signature search by name scan; 50 of 100 returned, no total, BRD codes only); PDK2 verdict unchanged: WATCH | `tooluniverse_capability_test_20261026.md`, tool survey row 12 | re-test only on a capability the adapters lack |
| TxGNN | **reasoned wait**: no retrievable per-disease predictions (txgnn.org 503), checkpoints are evaluation splits, Python 3.8 + DGL 0.5.2, no GPU | `p3b1/txgnn_matrix_outcomes_20261026.md`, `../locator_audits/2026-10-27_p3b1_txgnn_matrix_verification.md` | reopen if per-disease predictions or a `full_graph` model become retrievable |
| Every Cure MATRIX | **inconclusive trial, scores table only**: no licence stated for the scores; the WOREE ordering matches sibling DEE nodes (neighbourhood-driven), no WWOX-specific signal shown; scores are predictions, not probabilities | same | reopen when a licence for the scores is stated |
| LINCS / SigCom / iLINCS | **inconclusive, limit named**: one signature family fills both tails (61 reversers vs 59 mimickers), no content-matched null, shuffled control empty; a KO signature is not a rescue signature | `gse156243/prediction_lincs_context_stratification_20261026.md`, `../locator_audits/2026-10-27_lincs_toolu_verification.md` | content-matched null and per-library, cell line, dose and time strata |
| Daily scout | **operative**: `framework/scripts/scout_daily.py`, user crontab `20 5 * * *` (05:20 UTC), baseline run, then a no-change run under `env -i`; silent when nothing changes; report `~/.local/state/legend/scout_daily.json` | `framework/scripts/test_scout_daily.py`, capability scout log | a session moves `scout_daily_pending_log.md` into the log with `--append-log`; `harness_session_start.py` does not yet surface the report |

### Roadmap iteration 2, package W1.1 — curated-card linkage (2026-10-27)

Actor `scientist-a`, task `SA-IT2-CARDLINK-20261027`. No paper was opened and no live adapter was called: the three new
cards are written from manifests, receipts and the rescue-reference scaffold already in the repository. **Linking is
done by the map record naming the card by path** (as for E01-E04); the join then reads the card's qualified
assertions, route and Track as written. Nothing is linked by name similarity; a link is made only where the card's
candidate, target, endpoint, context, direction and limits are the record's. `UNQUALIFIED` stays where that is not so.

**Measured.** Of the 28 derived cards, 25 were `UNQUALIFIED` (route and Track) before this package; 19 are after it. Three
were linked in iteration 1 (E01, E02, E03) and six queries (five candidates) are linked now. Lowering the count was not
the goal: the other 19 are classified below, and two of the four classes (c, d) are a correct reason to stay unlinked.

**Batch chosen, and why.** (1) Lithium and (2) memantine are the two partial-benefit candidates whose records had
three and five complete readings and *no* curated card, and whose read-outs are easy to over-read (lithium's one WWOX
experiment failed its specificity test; memantine was never given, only a competitive antagonist as a tool). (3) AAV9 is
the broad-functional-recovery case: card C01 holds one endpoint (spike-wave discharges) as an assertion and the other
families only as prose, so the join could see one row of a study with several. (4) Wnt/tankyrase (D02) and (5) the
ketogenic diet (EB-KD-01 for the clinical seizure rows, E04 for the lactate and PDH rationale) already had pertinent
cards that were simply not linked; E04's own text names R-05 as its record. Rows chosen by value of the information
a link adds, not by ease.

| Query | Candidate (map record) | Class | Curated card, or why not |
|---|---|---|---|
| Q-N-08 | Dichloroacetate | linked (iteration 1) | E03 |
| Q-R-10 | ISRIB-class ISR attenuators | linked (iteration 1) | E01 |
| Q-R-11 | Stiripentol | linked (iteration 1) | E02 |
| Q-N-02 | Lithium as a WWOX-specific modifier | (b), **linked now** | F01 (new): the same candidate as R-04 |
| Q-R-04 | Lithium (GSK3beta) | (b), **linked now** | F01 (new) |
| Q-R-02 | Memantine | (b), **linked now** | F02 (new): tool compound d-APV only; memantine itself untested |
| Q-R-01 | AAV9-hSynI-WWOX | (a)+(b), **linked now** | C01 (existing, spike-wave discharges) + C04 (new, six other endpoint families) |
| Q-R-03 | Wnt / tankyrase inhibition | (a), **linked now** | D02 (existing, abstention; carries a route and no Track) |
| Q-R-05 | Ketogenic diet | (a), **linked now** | EB-KD-01 (existing, seizure rows; early-benefit directory) + E04 (existing, lactate/PDH) |
| Q-N-01 | mTOR inhibitors | (a) | EB-MTOR-AX-01 (abstention: mTOR activity in a WWOX system is unmeasured, as the record says) |
| Q-N-04 | Broad GABAergic push | (a), partial | EB-VGB-01 covers the vigabatrin limb only; benzodiazepines are uncovered, so a link would qualify half the record |
| Q-N-05 | Boosting WWOX expression alone | (a) | C03 (abstention) |
| Q-N-10 | Splice-switching ASO, canonical acceptor allele | (a) | C02 (abstention: no aberrant-to-normal transcript ratio exists) |
| Q-R-08 | Base / prime editing, splice-acceptor allele | (a), caution | C02 names editing and shares the missing transcript baseline; the modality differs, so the verifier decides |
| Q-N-11 | 4-PBA / TUDCA | (a) | A01 |
| Q-N-12 | HSP70 co-inducers (arimoclomol) | (a) | A05 (abstention) |
| Q-R-09 | Proteostasis modulation, SDR missense | (a), umbrella | A01-A05 are sub-levers of this record; linking all five would put three families' not-WWOX drug rows on one record, so the set is for the verifier to choose |
| Q-N-15 | Counting seizure control as developmental protection | (a), caution | EB-DEV-AX-01 (axis, no candidate); the record is an inference error, not an intervention |
| Q-N-07 | Digoxin (HIF1alpha) | (b) | none; four papers, three complete reads; a card is writable from the repository |
| Q-N-09 | pTyr33-WWOX peptide | (b) | none; three complete reads, three without a receipt |
| Q-N-13 | Pro-myelinating agents | (b) | none; 29 papers; the oligodendrocyte-boundary rows already sit in C04 and the scaffold |
| Q-N-14 | Antioxidants | (b) | none; eight papers, four complete |
| Q-N-16 | Pannexin-1 blockade | (b) | none; one complete reading, and its one datum (a point estimate in the adverse direction, never tested) is manifest entry 2 of the Breton 2021 reading |
| Q-N-17 | Tau-lowering | (b) | none; 56 papers; the WWOX/GSK3beta/Tau rows sit in the Wang 2012 manifest |
| Q-N-03 | Sodium-channel blockers | (c) | none; one paper, no receipt. EB-ETX-01 (a T-type blocker) must NOT be linked: different candidate |
| Q-R-06 | Anti-neuroinflammatory, class level | (c) | none; no compound and no endpoint named, so a card could only abstain |
| Q-R-07 | Bumetanide | (c) | none; the chloride premise is unmeasured in any WWOX system; a card would be an abstention |
| Q-N-06 | Lactate and blood biomarkers as readouts | (d) | E02/E04 hold the lactate observations but their route and candidate are interventions; this record is a biomarker, so a route would be wrong. Left `UNQUALIFIED` |

Classes: (a) a pertinent curated card exists and is not linked; (b) content is present in the repository and needs a card;
(c) the observations are insufficient to qualify anything beyond an abstention; (d) candidate, endpoint or context differ,
so a link would be wrong. For (a) rows the pertinence is judged from the record heading against the card's candidate and
disease assertion; the link has not been run or verified for them, and only the six queries above are linked.

**What the links changed (cards).** Route and Track: `UNQUALIFIED` to `BENEFICIO_PRECOCE` Track A for lithium, memantine
and the ketogenic record; `RECUPERO_PROFONDO` Track A for AAV9; `RECUPERO_PROFONDO` with Track left `UNQUALIFIED` for
Wnt (D02 states a route and no Track). Curated assertions arrive with their comparators and limits: 2 disease and 3 drug
rows for lithium (one `OPPOSES_DISEASE_CHANGE`, two `UNRESOLVED`, which *is* the specificity failure: wild type and
heterozygote responded as the null did), 2 and 2 for memantine, 8 and 16 for AAV9 (headline moves from the single-endpoint
`OPPOSES_DISEASE_CHANGE` of C01 to `CONFLICTING` once the study's other endpoints are rows: eight sign oppositions, two
measured nulls at day 10 glucose, six cells that cannot be compared), 5 and 3 for the ketogenic record. Evidence
scope is stated per reading only where a card cites it. The regenerated outputs are `join/` and the handoff
`repurposing_batch_selection_20261027_module.md`. Because the map gained one line per linked record, every later record's
`origin_line` moved: that is why all 28 derived cards report CHANGED in the run; the substantive differences are the six above.

**What the links changed (queue).** Honest measurement: the handoff's row kinds (SELECT / READ / REPLICATE / AUDIT) are decided
by the *dependence* (papers reached, depth, unaudited contradictions), and curated observations were consumed only in
REPLICATE rows; for these six records the row kinds and asks did not move (all six are AUDIT or READ for reasons the link does
not touch). What changed is a new section, "Records already qualified by a curated card", listing each linked record with its
cards, route, Track, row counts, comparison statuses and the card's own next measurement, so a batch starts from the card and
not from the records' papers. The committed `join/` outputs were also stale by two records (Q-R-11 and Q-DL-REPO-004 changed
by the 2026-10-27 batch commit without a regeneration); the regeneration absorbs that.

**Defects found and repaired (regression tests added).** (1) `qualification()` raised `KeyError` on any packet without a
`mission_dimensions` block, i.e. on every A-D and early-benefit card: they could not be linked. It now reads such a card's
route as written, leaves Track `UNQUALIFIED` unless a linked card states it, and names the silent card in `route_note`.
(2) `CARD_REF` could not name a `cards_early/` card (hyphenated ids) and `curated_packets` looked only in `cards/`: the
early-benefit cards were unreachable. (3) A record naming a card that cannot be found was skipped silently; the test now
fails on it. Two existing test fixtures encoded the old state of linked records (Q-R-01 as the example of an unqualified
reading; every `wnt`-axis card an abstention) and were updated, not loosened: the first now asserts both an unlinked
record (Q-N-07) and the per-reading scope of a linked one.

**Decisive links, for an independent verifier** (the producer cannot verify itself):
1. **Q-N-02 / Q-R-04 to F01.** The three genotype panels of Figure 7d (manifest PMID32000863 entries 0, 22, 27, 28): lithium
   suppressed the provoked seizure in wild type and heterozygote as in the null; the card must not read as a WWOX-specific
   signal. Also entries 2, 4, 23 (Ser9 dephosphorylation; heterozygote not intermediate). One trap: manifest PMID22193544
   entry 5 ("Ser9 unchanged") is a retinoic-acid differentiation context, not WWOX loss; the card says so and does not use it as a disease row.
2. **Q-R-02 to F02.** d-APV is a tool; the card says memantine was never given. Check that no field reads as a memantine result
   (`OPPOSES_DISEASE_CHANGE` is a sign comparison for the tool). The d-APV Results sentence is quoted from the article text, not a manifest entry; manifest PMID34634460 entry 2 reads the panel (bar absent, i.e. zero; washout about 1.85 times baseline).
3. **Q-R-01 to C01 + C04.** Each C04 row against `woree_rescue_reference_scaffold.md` section 2 and the manifest entries it names
   (40, 41, 10 carry repaired adverse audits not re-judged). Check that low-dose rows are written as a postponement or a non-graded
   equality, and that no row states a dose.
4. **Q-R-05 to EB-KD-01 + E04** (and E04's `target_census` of SLC16A1 now appears on the ketogenic card: confirm it does not mislead).
5. **Q-R-03 to D02.** Only a route and one disease-side row arrive; confirm D02's "GSK3 modulation" wording does not drag lithium
   (opposite direction on beta-catenin) into this record: lithium is deliberately NOT linked to D02.
6. **Scope vocabulary.** Mouse results (null, neuron-specific deletion) are marked `WWOX_EXPERIMENT_IN_DEE_SYSTEM`; confirm that is the
   intended reading of that label for an engineered-null mouse that is not a patient allele.

**Not verified.** The (a)-class pertinence of the 9 unlinked rows; the Q-R-08 and Q-R-09 judgements; whether the early-benefit
cards' silent Track should be written into those cards instead of read as silent; the new cards' figure readings (they carry
the manifests' own text, no new reading).

Nothing in this capability has produced a therapeutic recommendation, and no output of it is a
`DATO`. The clinical census is a retrieval record; the bridge's cards would be `IPOTESI`.

# Strategic Advisor brief — Stage B

## Snapshot
- Repository SHA: `d8baa78d780dbef74721ea1d232b05e3356946aa` (branch `task/it50`)
- Dispatch time (UTC): 2026-11-13T07:45:21Z
- Uncommitted paths (9; read as on disk):
  - `ledger/tasks/orchestrator/ORCH-ROADMAP-IT50-20261113.json` (M) sha256 `2a7baec71f0f3f76`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it50_20261113/A1/assessment.md` (??) sha256 `3804f6f272c9fb29`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it50_20261113/A1/brief.md` (??) sha256 `79e3544cfd9d35fe`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it50_20261113/A1/meta.json` (??) sha256 `1a18d71463751f69`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it50_20261113/advisor_sealed/INTENDED_ACTION_1.md` (??) sha256 `d418f3adf3e0904b`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it50_20261113/brief_A.md` (??) sha256 `79e3544cfd9d35fe`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it50_20261113/inputs/constraints.md` (??) sha256 `6a164c1699612fa8`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it50_20261113/inputs/mission.md` (??) sha256 `81f51156807c7f78`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it50_20261113/invocations.jsonl` (??) sha256 `691a6805dd730342`
- Dashboard: https://marinomassimo-dot.github.io/legend-development/ · source revision 387f6ae49edb6e8aa8259703336fc7f25cd7bda9 2026-11-13T02:22:05+00:00 · the public page shows no build stamp; the package commit above is the source revision it is generated from. Publication date of the live page was not checked.

## Mission and limits (verbatim from the caller)


## Operational constraints
Constraints: zero new external spend; no contact with people; public edition; not medical advice; ranking means research investment, not efficacy; no change of rank, sign or qualification to show an effect; no predictive claim from better access to knowledge; one scientific delegate at a time with a distinct verifier; originals read in full when accessible.
Boundaries: the science session has a generative mission starting from myelination (do not duplicate or interrupt a package already under way); Harness builds a minimal link for design-only packages (no competing reader); SCI50 is an input when it arrives, not a constraint. Window: up to ten hours; one Stage A and one Stage B only for IT50 (a failed attempt counts). The IT48 pilot ceiling is separate and spent.
Dependencies: browser tests on this host need a working Chromium (the tool now selects an installed older Snap revision).

## Saved Stage A assessment (complete, verbatim)
sha256 `3804f6f272c9fb292d6f18d4793e6ab29e412b3fa38881369ec2d62a3468cd50`

## 1 · Principal decision

Which single bounded investment should IT50 spend its principal generative increment (OBJ_P3, `ledger/tasks/orchestrator/ORCH-ROADMAP-IT50-20261113.json` lines 36–37) on: further depth in the INV-18 K-conductance thread, another priority thread, knowledge already held but unconsumed, or a small technical obstacle.

## 2 · Leading recommendation

**Propagate a cell-class result LEGEND already computed into the Kir2/Ba²⁺ arm of INV-18, with one small zero-spend extraction to complete it.**

Facts. `generation_it46_20261111/cell_context_it46.tsv` (committed) already holds, for relations S11/S12, the join of the Kir genes to the held RNA tables: `KCNJ2` **OTHER_ENRICHED** in both tables (mouse neurons P7 0.74 FPKM vs endothelium 41.80, line 466; human neuron_ctx 1.40 vs oligo_ctx 6.64, n=1, line 476); `KCNJ4` and `KCNJ12` **SHARED** in the mouse targets table (neurons 1.67 vs myelinating oligodendrocytes 1.73, line 517; neurons 1.54 vs newly formed oligodendrocytes 1.39, line 518) and **NOT_DETECTED** in the human one (lines 527–528); `KCNJ10` OTHER_ENRICHED (astrocytes 184.76 vs neurons 8.12, line 546; human 126.02 vs 9.00, line 548); `KCNJ16` OTHER_ENRICHED (line 557). A search of the two extraction tables for `Kcnj14`/`KCNJ14` (Kir2.4) returns no row: it is `NOT_IN_TABLE`, i.e. unqueried, and `KCNJ2` is absent from the IT47 targets tables while `KCNJ4/12/16` are absent from the SCI44 kchan tables. The conventions are declared in `generation_it46_20261111/cell_context.py` lines 14 and 20 (FLOOR 1.0, FOLD 3.0) and the engine's own consequence sentence for a non-enriched gene is at line 111 ("cannot be assigned to neurons from these tables … it needs a cell-specific control").

Facts about consumption. The INV-18 row (`ranking_it8_p9_20261029/investigations.tsv` line 19, `feasibility` field) records the in-silico join three times — `[IT45]` Kv7 genes "against astrocytic Kir4.1", `[IT46 cell context]` KCNQ2/KCNQ3, `[IT47 update]` KCNQ4/KCNQ5 — and the "needs a cell-specific control" conclusion is carried **for the Kv7 genes only**. No Kir2-subunit figure or state appears in that row, nor in `kir2_drugname_sci49_20261112/README.md`, nor in `output/gaps.md`, which instead reasons from the literature that "a cortical neuron whose Kir2 is likely heteromeric" (gaps.md line 29) and offers the Kir4.1 pairing without any class value (line 22). The open-question map writes the composition question as a pure reading task that may be unreachable (`batch_sci_20261105/map/open_questions_map.tsv` line 170, IT49-Q09) and the glial share as a wet measurement (line 168, IT49-Q07).

Interpretation (RNA only; labels as the records use them). In the held tables no Kir2 subunit is neuron-enriched, `KCNJ2` is enriched elsewhere in both, and the astrocytic `KCNJ10` prior is ~23× (mouse) and ~14× (human) the neuronal value. Applied at the same standard the project already applied to KCNQ2/KCNQ3, this says three things no consumer carries: H1's "identified Kir2-dominant native cell" positive control (`kir2_drugname_sci49_20261112/README.md` answer 4) is not identifiable from the held tables, so the control defaults to a heterologous one; the Kir4.1/glial arm is required for the *statement* "this Ba²⁺ share is neuronal" and not optional, which is exactly the control-tied-to-the-statement rule SCI49 A established for the Kv7/OPC case (`cell_context_verify_sci49_20261112/README.md` answer 5 and the DREAM paragraph line 33); and the recovered Cys311 activator class (flecainide/propafenone/timolol, Kir2.1-homomer, heteromers not increased for flecainide, n=10, gaps.md line 27) acts on the subunit with the weakest neuronal RNA support of the three, which sharpens IT44-Q01 into a precise reagent gap rather than a lever.

Strategic judgment. This is depth in the thread already under way (no forced rotation), it is the one item that matches three OBJ_P3 shapes at once (knowledge combination that changes an experiment; proposal lost to representation; delimiting an unsupported path), it costs one delegate pair and seconds of compute, and its failure mode is cheap and informative.

## 3 · Relevant alternatives

- **Stay on the current branch by literature depth — IT49-Q06** (open_questions_map line 167): ML133's hERG block at pH 7.4, Kir2.4 and K2P activity decides probe vs comparator for the only deployable reagent. Strongest single-reagent decision, but partly blocked by the routes already tried (PubChem deposit pH unstated, IUPHAR 401, three PMC interstitials — `output/gaps.md` line 5); it may return "still unstated".
- **Another thread — INV-06 myelination** (investigations.tsv line 7): the premise question is cheaper than any compound test and the branch has 318 direction-incoherent catalogue associations. The brief reserves myelination to the science session; I recommend handing over, not duplicating, the observation that the same held tables carry OPC/NFO/MO rows that its co-culture arm could use.
- **Shared upstream uncertainty**: generalise "the control is tied to the statement" into one exclusion ladder shared by the Kv7, Kir2, HCN and KATP arms. Valuable but it is design consolidation with no measurable output this window; my leading action is its first testable slice.
- **IT49-Q02 (ISR cell classes)**: the same script with a different gene list, zero spend, but it cannot give the protein-level sign (`generation_it49_20261112/p5_case_inv02/result_it49.md` line 23). Worth riding along in the same run, not worth the principal slot.
- **IT49-Q03 (design-only reader)**: Harness owns it; my package would supply a second real case — a *computed join artefact* that no reader consumes — as input, without a competing reader.

## 4 · Why now

The thread just received two verified deliveries (SCI49 A and B) and both ended pointing at attribution: "a bath effect cannot separate neuron from glia" (investigations.tsv line 19, `[SCI49 update]`). The held rows answer a part of that at zero cost, and the window already plans to regenerate derivatives (OBJ_P7), so two already-verified, still-unapplied deltas can land in the same pass: `kir2_drugname_sci49_20261112/consumer_delta.md` row 1 is **PROPOSED**, and the live page still shows the superseded wording ("the one Kir2 opener it reached is Kir2.1-only with no neuronal data", dashboard fetch, first 100,000 of 629,802 characters).

## 5 · Evidence and uncertainty

Supporting: the artefact, the values and the engine conventions above; SCI49 A's independent verification that 0.1 is a reporting floor in the human table and that RNA is not protein, current or drug response.
Against / limiting: mouse neurons are sorted P7 and the oligodendrocyte lineage P17, against a P13–P17 layer II/III phenotype; n=2 mouse, n=1 human column; the human Kir2 values sit at or near the floor; the mouse `KCNJ2` maximum is endothelial (41.80), a class largely irrelevant to a slice readout; class means cannot give subunit composition, so **IT49-Q09 stays open** and the wet questions IT49-Q05/Q07/Q10 stay indispensable.
Unchanged by this action: every rank, sign and qualification. I propose no change to any of them; what would change them is named above.

## 6 · Next bounded action

One scientific delegate with one distinct verifier, local inputs only, no network needed:

**Principal question —** *Do the cell-class rows LEGEND already holds change the Kir2/Ba²⁺ arm of INV-18 (H1's positive control, the status of the Kir4.1 arm, the applicability of the Cys311 activator class), and was any part of "no Kir2 lever" a vocabulary or table-coverage artefact rather than biology?*

The result that would count: the verifier independently reproduces the five gene-level states from `cell_context_it46.tsv` and from one re-run of the existing extraction (`generation_it47_20261112/b1_cellclass/targets_expression.py`, gene list extended with `Kcnj2` and `Kcnj14`, input SHA-256 recorded), and the package returns either at least one changed design element in H1 — control, glial arm, or the activator-class delimitation — or an explicit "no change, because…". A null ("the rows add nothing to the Ba²⁺ arm") is a usable result and should be written as one.

## 7 · What would change my view

If a verifier finds the Kir2-subunit rows already consumed in a record I did not open (`potassium_shares_sci44_20261110`, `sci43_reopen_it48_20261112/verify`), the finding shrinks to a wording update and IT49-Q06 becomes my first choice. If the owners judge P7 sorted-neuron means unusable for a P13–P17 statement, the product reduces to the delimitation plus the extraction, and IT49-Q06 ranks first. If SCI50 delivers a Kir2-composition reading, value shifts from generating this prior to applying that result.

## 8 · Resource implications

One delegate pair (constraint respected: one scientific delegate at a time), local file reads, a seconds-long script run, zero spend, no contact, no new dependency, no new gate or reader. Reversible: delete the folder and the proposals. Two near-free refinements in the same window: apply `consumer_delta.md` row 1 (its owner's edit, already verified), and regenerate `needs/needs.md` — its table is headed "22 needs … computed from `needs.json`" while `needs.json` holds 24 ids, the two missing being `NEED-REDOX-NRF2` (line 6135) and `NEED-INTRINSIC-EXCITABILITY` (line 6300), the need that owns this entire thread. Both are stale generated surfaces, not scientific changes.

## 9 · Inspected

Opened in full: the IT50 task record; `advisor_campaign_it50_20261113/inputs/constraints.md`; `advisor_followup_20261112/README.md`; `kir2_drugname_sci49_20261112/README.md`, `consumer_delta.md`, `output/gaps.md`; `cell_context_verify_sci49_20261112/README.md`; `generation_it49_20261112/README.md` and `p5_case_inv02/result_it49.md`; `generation_it46_20261111/cell_context.py`; `generation_it47_20261112/b1_cellclass/targets_expression.py`; `dream5_20261109/README.md`; memory note `strategic-advisor-pitfalls.md`.
Read in ranges: `roadmap_current.md` lines 1–172; `needs/needs.md` headings and rows 47–79; `needs.json` need-id list and lines 6295–6324; `investigations.tsv` header, the compact rank list and the complete INV-06 and INV-18 rows (lines 7 and 19); `open_questions_map.tsv` lines 140–172; `cell_context_it46.tsv` Kir rows; the SCI44/IT47 expression tables' Kcnj rows.
Fetched: the dashboard home page, partial (first 100,000 of 629,802 characters); its publication date was not checked and I made no visual inspection.
Not reached: `discovery_ledger_current.md` (926 KB) and the dismissal ledger beyond a Kir2/ML133 search that returned nothing; the 195 diagnosis/session-evaluation files; `capability_scout_log.md` beyond one search; the ranking JSON; `view/README.md` beyond one search; the SCI49 receipts and verdict tables; the sealed intended action (not opened, not attempted).

## 10 · Freshness and exposure

Uncommitted inputs read as on disk: the IT50 task record and `inputs/constraints.md`. I did not open `inputs/mission.md`, `brief_A.md` or `A1/brief.md` (the brief states they duplicate my prompt). `needs/needs.md` is stale against `needs.json` (fact, above); `investigations.tsv` lives in an IT8-dated folder with later updates appended inside the rows. The dashboard reading is partial and one of its Kir2 clauses predates a verified, still-unapplied correction.
Exposure: the task record I was pointed at reveals the Orchestrator's campaign shape — OBJ_P1…P7, including that P3 is the "principal generative increment" with four named shapes and P4 the Harness link for INV-02 — so my framing is not blind to the campaign plan, only to the sealed intended action. The brief's boundaries also told me the science session starts from myelination, which is why I handed that branch over rather than ranking it; a reader should weigh that as declared exposure. Per memory (`strategic-advisor-pitfalls.md`), the model that wrote this assessment should be read from `final_turn_model`, not from the alias requested.

## Orchestrator's intended action (complete, verbatim)
sha256 `d418f3adf3e0904ba6d59e9eaa01864050f6b17394c0b117ccd8a67a28ebab31`

Intended action without a new assessment (recorded 2026-11-13 before any IT50 assessment was read).
Principal generative increment: a proposal lost to a catalogue or representation limit. In the INV-02 case the simple target search gave 0 rows for the node the card cares about (raising eIF2B activity): an eIF2B activator is reachable only as a named research probe in the ISR package. I would make that lost proposal representable and comparable: name-reached probe with its documented qualification gaps, a conditional comparison against PERK-kinase inhibition and a genetic arm (loss of the eIF2alpha phosphatase regulatory subunit), the observation/explanation/action/probe/prediction/discriminating-result kept apart, the ISR sign at protein level as the premise that blocks any compound, and a run of the generator before and after.
Reason: it uses knowledge already held (the ISR package, its audited units), it is zero-spend and executable, and it is the concrete limit the INV-02 case exposed.
Coordination: I would not touch myelination (science session mission); the design-only link is Harness's.

Begin with 'Response to the intended action': refinements, alternatives or a justified disagreement.

## Neutral entry points
| id | what | patterns (relative to the repository root unless absolute) | matches now | last commit | largest file |
|---|---|---|---|---|---|
| limits | Authorised mission and resource limits: the task record named in the brief, and its siblings | `ledger/tasks/*/*.json` | 202 | 2026-11-13 | `ledger/tasks/scientist-a/AQEILAN-FT-A-001.json` (35,910 bytes) |
| invariants | Canonical project invariants and the operating rules | `CLAUDE.md`<br>`ARCHITECTURE.md`<br>`framework/master/harness_development_principles.md`<br>`framework/master/designed_for_growth.md`<br>`framework/master/gold_is_in_the_details.md`<br>`framework/instruction/LEGEND_CORE.md`<br>`framework/instruction/epistemic_discipline.md`<br>`disease-models/wwox/mission.md` | 8 | 2026-11-12 | `framework/instruction/LEGEND_CORE.md` (35,123 bytes) |
| repurposing_method | Drug-repurposing roadmap and Standing method | `disease-models/wwox/research/drug_repurposing/roadmap_current.md`<br>`framework/protocols/repurposing_adapter_convention.md` | 2 | 2026-11-12 | `disease-models/wwox/research/drug_repurposing/roadmap_current.md` (44,438 bytes) |
| dashboard | Dashboard: source records of the public page (the page is a map, the records are the facts) | `disease-models/wwox/research/drug_repurposing/view/README.md`<br>`disease-models/wwox/research/drug_repurposing/view/shareable_package/manifest.json`<br>`disease-models/wwox/research/drug_repurposing/view/shareable_package/README.md`<br>`disease-models/wwox/research/drug_repurposing/view/DEPLOY.md` | 4 | 2026-11-13 | `disease-models/wwox/research/drug_repurposing/view/README.md` (34,905 bytes) |
| investigations | Investigations (research investment, not efficacy), needs and cards | `disease-models/wwox/research/drug_repurposing/ranking_it*/investigations.tsv`<br>`disease-models/wwox/research/drug_repurposing/ranking_it*/ranking.json`<br>`disease-models/wwox/research/drug_repurposing/needs/needs.md`<br>`disease-models/wwox/research/drug_repurposing/cards/*` | 65 | 2026-11-13 | `disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/ranking.json` (1,097,886 bytes) |
| open_questions | Open-question maps and rows | `disease-models/wwox/research/drug_repurposing/**/open_questions*` | 4 | 2026-11-13 | `disease-models/wwox/research/drug_repurposing/batch_sci_20261105/map/open_questions_map.tsv` (160,144 bytes) |
| candidates | Candidates, comparisons and hypothesis packages | `disease-models/wwox/research/drug_repurposing/generation_it*/`<br>`disease-models/wwox/research/drug_repurposing/**/compound_decisions*.tsv`<br>`disease-models/wwox/research/drug_repurposing/**/hypotheses*` | 49 | 2026-11-13 |  |
| packages | Completed packages and their consumer notes | `disease-models/wwox/research/drug_repurposing/*/README.md`<br>`disease-models/wwox/research/drug_repurposing/**/CONSUMER_NOTE.md` | 234 | 2026-11-13 | `disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/README.md` (65,530 bytes) |
| diagnoses | Diagnoses, evaluations and DREAM | `disease-models/wwox/research/session_evaluations/*`<br>`disease-models/wwox/research/drug_repurposing/diagnosis_*/*`<br>`disease-models/wwox/research/dream*/README.md` | 195 | 2026-11-13 | `disease-models/wwox/research/session_evaluations/2026-10-04_BATCH_20261004_001.md` (60,878 bytes) |
| memory_dismissals | Dismissal and discovery ledgers, memory index (outside the repository) | `disease-models/wwox/research/dismissal_ledger_current.md`<br>`disease-models/wwox/research/discovery_ledger_current.md`<br>`/home/desktop/.claude/projects/-home-desktop-legend-development/memory/MEMORY.md` | 3 | 2026-11-12 | `disease-models/wwox/research/discovery_ledger_current.md` (926,660 bytes) |
| radar | Radar findings and capability gaps | `governance/candidates/HARNESS-SCOUT-*.md`<br>`disease-models/wwox/research/capability_scout_log.md`<br>`SKILLS.md`<br>`CAPABILITIES.md` | 4 | 2026-11-13 | `disease-models/wwox/research/capability_scout_log.md` (183,245 bytes) |
| tools | Which tool answers which question (the advisor has no shell; this explains what the records came from) | `framework/scripts/README.md` | 1 | 2026-11-12 | `framework/scripts/README.md` (54,854 bytes) |

Memory directory (read-only): `/home/desktop/.claude/projects/-home-desktop-legend-development/memory`

## Output
Return one assessment with the headings given in your definition. Name every file or page you opened under 'Inspected'. You cannot write, run commands or start agents. The entry points are starting places; follow references past them. This brief is your prompt: the copy saved in the campaign folder is the same text, so do not open it. A file the table marks over 20,000 bytes is paid for again on every later turn: Grep for the heading or id you need and read that range, and open the whole file when the question needs all of it; never re-read a range you already hold.

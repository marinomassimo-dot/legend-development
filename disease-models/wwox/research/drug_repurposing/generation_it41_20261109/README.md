# IT41: from mechanism to compounds — relation-driven search, comparison and priority

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. **Functional capacity and traceability only: no independent data exist to test prediction, and no predictive superiority is claimed.**

## P0 — what IT40 actually was (reconciled before attributing anything)

IT40 candidate `560601df`: battery PASS WITH SKIPS (224 targets, 11 skipped: local catalogue cache); the earlier candidate `1dd89027` FAILED on three own suites (kept, attributed). Published `31919734` (gate PASS, ls-remote verified); the shareable-view workflow succeeded; the release-gate workflow on `31919734` was still running when this was written (see the record). The IT40 reference figures were re-read from `generation_it40_20261109/README.md` and `measure_it40.tsv` after the verifier's corrections: six structured physiological hypotheses, 119 distinct arm × explanation cells, six relations searched, generator selection unchanged (S17 identical to S16 on all 994 rows). They are IT40 results, not repeated here as IT41 ones.

## Path (observation → rivals → conditional action → search → comparison → next experiment), as run

| Step | Artefact |
|---|---|
| Question, rivals, universe, conditions, decision — fixed before the search | `cases.md` (four cases) |
| Conditional action, premise kept ("if this explanation holds, this modulation deserves comparison") | `relations_it41.tsv` (a table: a new relation is a row, not code), IT40 `conditional_proposals_it40.tsv` |
| Search by action and context beyond named compounds | `action_search.py` → `search_rows.tsv` (one row per source row), `molecules.tsv` |
| Comparison with its four elements and a fixed reading of each outcome | `comparison_S1.md`, `comparisons_it41.md` |
| Compound and hypothesis list for the dashboard | `compound_view.tsv` → the view (full and shareable) |
| Next experiment and what depends on it | `comparisons_it41.md` (minimum interpretable experiment), `collab_questions_it41.md` |

Distinctions kept: identified molecule / documented action / predicted action / context relevance / probe / candidate-to-study / comparator or control. A catalogue row on a receptor family is not subunit selectivity; an absent row is not an absent action; a value under a target is not necessarily a measurement of that target.

## What the search found (Case 1: GluN2B-directed negative modulation)

* 55 distinct molecules under the GRIN2B symbol once cross-source records are merged and radiolabelled forms left out: 20 orthosteric ligands (agonists and antagonists of the glutamate or glycine site), 6 channel blockers, 1 antagonist with no site recorded, the 4 molecules on the two-gene GRIN1/GRIN2B assembly record (ChEMBL action: antagonist), 3 negative-modulator rows and others. A symbol lookup mixes all of these.
* New to the comparison: onfasprodil (a human-exposure GluN2B negative modulator, receptor site not recorded; abstract-level source), NP10679 (a pH-dependent GluN2B modulator: a bath-pH condition, not a candidate). Not read as GluN2B evidence: a registry row (DQP-1105) whose assay text names GluN2C — which subunit the value belongs to is unresolved.
* Identity (Harness, P5): the four IT40 cases are not four absences — GYKI 52466 and GYKI 53655 are different structures that registries label inconsistently; Ro 25-6981 and ifenprodil have measured-activity rows (GRIN2B, with other targets also measured) but no curated mechanism row; Brilliant Blue FCF is in ChEMBL without a name. Consumed as stated in `compound_view.tsv`.
* Second family (P11): relations S5 (GABA-A positive modulation) and S6 (chloride-gradient control) ran with **no code change**: 115 molecules for S5, of whose 671 source rows 104 have a reducing direction (inverse agonists among them, after the direction rule was fixed on the verifier's finding) and 17 an unclear one; S6: bumetanide-class NKCC1 inhibitors are present, the two KCC2 rows are inhibitors (the opposite of the wanted action) and the table holds no KCC2 enhancer — absence in a table, not absence of action.

## Before / after (`measure_it41.tsv`; same case, same universe)

| | Previous path | Simple baseline | IT41 path |
|---|---|---|---|
| Distinct molecules for the symbol | 24 (ChEMBL mechanisms) | 55 (both tables) | 55, classified by site/action/assay text |
| Orthosteric and channel-block ligands separated from modulators | no | no | 20 + 6 + 1 |
| Rows whose assay text names another subunit | not seen | not seen | 1 (value not read as GluN2B) |
| Compounds entering as "emerged" | 0 | 0 | 2 (onfasprodil, NP10679) |
| Generator selection (994 proposals) | unchanged | | unchanged |

Labels (rule: "known reference" = already discussed in repository material; "new combination" = known molecule, new use here; "new for LEGEND" = never discussed as a comparator; novelty against the literature **not** asserted): radiprodil, traxoprodil, rislenemdaz, EVT-101, ifenprodil, Ro 25-6981 = known reference; onfasprodil = new combination; NP10679 = new for LEGEND (as a comparator).

Ablation: with ChEMBL mechanisms only (the new link off), onfasprodil and NP10679 do not appear and the DQP-1105 row is never seen.

## Verification

Independent sonnet/high delegate (`verify/VERDICTS.md`): all seven claims PARTLY; corrected: one registry value shown as two (onfasprodil), "species-dependent" (assembly-dependent: human 91 against rat 82 is within the spread), the removable-share bound written as general (it is ifenprodil's; per molecule), the DQP-1105 wording (subunit of the value unresolved, not "measured on GluN2C"), an unstated transfer of ifenprodil values to Ro 25-6981, "either structured source", duplicates in the counts (merged by catalogue parent; radiolabelled forms dropped), and the inverse-agonist direction rule (fixed in `action_search.py`).

## Limits

The new relations rest on one catalogue snapshot (ChEMBL 37, GtoPdb 2026.3.1) and two abstracts read by tool; no full text was read here. The comparator work awaits the science package on AMPA-tool qualification and the second on HIF1A→BNIP3 (neither delivered at the time of writing). The shareable edition omits compound names and registry-derived values for licence reasons (ChEMBL CC BY-SA 3.0; GtoPdb ODbL / CC BY-SA 4.0): the fields are `name_full` and `registry_note` of `compound_view.tsv`; a separate share-alike file of the rows would need its own package.

## Added after the science and Harness deliveries (2026-11-10)

* **Identity (P5).** Harness's `identity_it41_20261109/` (merged from development/main): the four IT40 cases are classified as identity/grouping (GYKI), pharmacology level (Ro 25-6981, ifenprodil: measured activity, no curated mechanism) and coverage (Brilliant Blue FCF: a nameless ChEMBL record). Consumed in `compound_view.tsv` (V02, V03) and in the AMPA arm below; no catalogue edit by me, no analogue substituted.
* **AMPA comparison (P6).** Science package A (`ampa_comparison_it41_20261109/`, 10 proposals, applied 10 by `apply_ampa_delta.py`, marker `[IT41a]`): the AMPA arm is a pair of two mechanisms (a noncompetitive 2,3-benzodiazepine plus the competitive NBQX), perampanel shares the benzodiazepine's pocket (cross-check, not a second line of evidence), the tissue data are for GYKI 53655 and not GYKI 52466, 10 µM gives 80–89 percent block in tissue (the 90 percent design value is at the edge), one evoked Up-state precedent is unfavourable to the AMPA-led reading (transfer). Applied to: the probes table (new GYKI 53655 row), BH1, M07/M08, BE1, three comparator rows for INV-05, the need, card F04, `compound_view` V03, `next_investigations_it40.md` (update line). Six staged receipts recorded after a clean trial (ledger 1,532 → 1,538), all partial full text.
* **Reader.** `hypothesis_packages.tsv` has a row for the folder, so `hypothesis_package.comparison_for` reads C1–C3 (14 rows over 4 packages in the reader's check).
* **Still pending from the science session:** the HIF1A→BNIP3 package (not delivered when this was written); IT41 P10 will consume it if it arrives and is pertinent.

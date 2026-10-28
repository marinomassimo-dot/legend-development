# Closed loop on real work (iteration 3, scientist-b, 2026-10-28)

Non-canonical research material. Not medical advice; no efficacy claim; no dose; nothing here changes the four scientific current files; no receipt was written (see "What was not read").
Coverage version used: `main` 315cd50c (the layer before the correction of the ABAT / Guide-to-Pharmacology adenosine-ligand artefact, the MAPT-only links and the over-claimed L3/L4 cells, which task `it3-search2` is making). Cases were chosen from ChEMBL curated-mechanism links, and every DGIdb claim source used was checked.

The loop exercised: study or question -> qualified observation -> need (`needs/needs.json`) -> catalogue search (`repurposing_search.py`) -> candidate or reasoned abstention -> card or disposition -> regeneration (`check_cards.py`, `repurposing_join.py run`, `repurposing_coverage.py run`) -> queue (`repurposing_join.py handoff`, section "Catalogue-derived leads") -> `coverage/lead_dispositions.json`.

## Case a - a compound with no card, entered from the reverse path <a id="case-a"></a>

**Question.** Is the one drug result of `NEED-T-TYPE-CALCIUM` (ethosuximide suppresses the late phase of the PTZ score in the Wwox-null mouse only, one experiment, no interaction test) mediated by T-type channels?
**Entry.** `repurposing_search.py compound apinocaltamide` (no card, no record names it). Chosen by informational value, not annotation count: among the 201 consistent candidates it is the one that is structurally unrelated to ethosuximide, brain-penetrant by the sponsor's description, a three-subtype blocker and a clinical candidate, so it can split "T-type" from "ethosuximide-specific". Mibefradil (withdrawn, non-selective), ABT-639 (peripheral-pain programme, CACNA1H only) and the other ethosuximide-class succinimides add less.
**Catalogue returned.** ChEMBL curated mechanism: T-type blocker on CACNA1G/H/I (reference ids PubMed 29116786, 31004346), max phase 2, no approval statement. A DGIdb-only record repeats the same three targets from the same ChEMBL claim (not an independent confirmation). Failures: the ChEMBL records for ulixacaltamide (Z944) and for mibefradil (parent) carry no mechanism row; Z944 reaches the need only through a DGIdb record that also lists unrelated V-ATPase "blocker" rows. A catalogue gap, not a negative.
**Literature (abstract level only).** PubMed abstracts 29116786 (discovery), 31004346 and 31994022 (healthy-adult phase 1, tolerability), 40165594 (rodent: absence-type discharges suppressed; generalized convulsive tests reduced at higher concentration; no effect on focal-onset kindling), 38605177 (cryo-EM of Cav3.2 binding). All sponsor-affiliated except the structure paper.
**Decision: candidate, mechanism-level discriminator only** (not a treatment proposal). Card `cards/H01_apinocaltamide_ttype.packet.json` (+ `.card.json`, `check_cards.py` passes), identity declared in `catalog/card_identity_declarations.tsv`.
**Why.** The class-level cortical-progenitor viability signal for T-type blockers (Kim 2018, read in the R2 note, carried from `cards_early/EB-ETX-01`) is on the card as counter-evidence, because the intended population is developing.
**Reopening / closing.** Closes if a same-day-controlled null-pup assay with measured exposure fails to reproduce the effect; weakens if full texts show no brain exposure.
**Next discriminating experiment.** On the card (`next_measurement`) and as LD-001.

## Case b - endings that are not candidates <a id="case-b"></a>

1. **Glycine, aspartic acid -> `NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR` (direction down).** `compound glycine`: DGIdb / Guide-to-Pharmacology "agonist" on GRIN2A/2B/2C, consistency `opposed`; ChEMBL has no mechanism row for either. Decision **opposite_mechanism, ended** (LD-002). Reopens only if NMDA-receptor hypofunction were shown in a Wwox system.
2. **Adenosine, regadenoson -> `NEED-SEIZURE-CONTROL-SYMPTOMATIC` flagged `opposed` via ABAT.** The row is one Guide-to-Pharmacology "ABAT agonist" among ABC-transporter rows (ABCA1/2/3, ATP4B, ferritin pseudogenes); the compounds' real targets (ADORA1/2A/2B/3) are not targets of the need. Decision **abstention**: the "opposite" is a source artefact, not a finding (LD-003). The coordinator's audit reached the same conclusion for the whole ABAT block independently.
3. **Pannexin-1 blockers (record Q-N-16) -> PANX1.** `target PANX1`: 0 ChEMBL rows, no DGIdb row via the need. Probenecid, carbenoxolone and brilliant blue G exist in the catalogue under other targets and are deliberately not joined by name. The only WWOX datum is a rise in burst frequency under the blocker (never tested). Decision **insufficient** (LD-005); next act is the REPLICATE row Q-N-16 that already exists.

## Case c - PARS2 / GCN2 and the ISR need <a id="case-c"></a>

**Observation.** `isr_pars2_reading_it3_20261027.md`: in a fly model of mitochondrial prolyl-tRNA-synthetase deficiency, GCN2 or ATF4 RNAi lowers the seizure-like phenotype; P-GCN2 up, P-PERK unchanged. Genetic, not WWOX.
**Need update (this task).** `NEED-ISR-ATTENUATION` listed PERK and the eIF2B subunits but not GCN2, so the forward search could not even ask. Added target `EIF2AK4` (HGNC:19687, collision note vs PERK/HRI), observation O5 (scope `OTHER_DISEASE_PRECEDENT`, limits: genetic knockdown is not pharmacology) and an `inferred` line; `check_needs.py` passes.
**Catalogue returned.** `need NEED-ISR-ATTENUATION`: 0 ChEMBL mechanism rows for EIF2AK4; 6 DGIdb rows: five antipsychotics (ziprasidone, olanzapine, haloperidol decanoate, risperidone, quetiapine) via PharmGKB with interaction type UNKNOWN (pharmacogenomic association) and hesperadin (multi-kinase research inhibitor, DTC). Known GCN2 tool compounds are not in the catalogue; halofuginone (prolyl-tRNA-synthetase EPRS1 inhibitor, which would drive GCN2 toward the same direction as the fly lesion) is present but EPRS1 is no need target, so the search cannot reach it - a limitation of the loop, noted not fixed.
**Decision: insufficient / exploration only** (LD-004). Direction for the need is `uncertain`; the five antipsychotics are association rows and are not offered. Reopens on phospho-GCN2 or ATF4 elevation in a Wwox-deficient neural system, or a catalogued compound with a stated GCN2 action. Next experiment: phospho-GCN2 versus phospho-PERK with eIF2alpha phosphorylation and ATF4 protein (stage 1 of card E01 plus the kinase question) before any compound.
Side effect on coverage: exploration candidates rose from 393 to 398 (the five antipsychotic families); the queue section does not list them because they have no card and no decisive step.

## The queue now consumes the result

`repurposing_join.py` gained `catalogue_leads()` / `render_catalogue_leads()` and a `Catalogue-derived leads` section in `handoff` (card-attached coverage pairs with a mechanism-candidate, exploration, opposite or no-result disposition, plus `coverage/lead_dispositions.json`, validated: required fields, decision vocabulary, need exists). Five regressions in `test_repurposing_join.py` (class `CatalogueLeadsTest`).
- Before: `join run` reports 28 cards, 0 changed; the new card H01 is invisible to the queue because no mechanism-map record names it (the handoff of the same date rendered before the change: 28 rows, no catalogue content).
- After: `repurposing_batch_selection_20261028_module.md` carries the same 28 rows plus a section with 10 card-attached pairs (ethosuximide, vigabatrin, memantine, perampanel, dichloroacetate, lithium, apinocaltamide) and five dispositions LD-001..LD-005, each with owner, reopening condition and next experiment. Rows with L3/L4 "observed" for memantine, perampanel, dichloroacetate and lithium inherit the over-claim the audit found and must be re-read after the correction lands.

## The 12 derived cards still UNQUALIFIED

None was linked. Checked against the catalogue where it could help: Q-N-07 (digoxin) - digoxin's catalogue targets touch neuroinflammation (STAT3, TNF, unsigned), not the HIF1A step the record is about, so a link would qualify the wrong question; Q-N-16 - no catalogue compound reaches PANX1, no card exists (a card is writable from manifest PMID 34634460 entry 2; not written here); Q-N-03, Q-R-06, Q-N-06 are class (c)/(d) and stay so; Q-N-04, Q-R-08, Q-R-09, Q-N-15 stay with the verifier's reasons. The catalogue did not reveal a matching compound for any of them.

## WWOX-value observations (observations, not a benchmark)

| Observation | Artefact |
|---|---|
| Counter-evidence retrieved: a class-level developing-cortex viability signal for T-type blockers, from the repository's own earlier reading, attached to a new compound that has none of its own | `cards/H01_apinocaltamide_ttype.packet.json` DR-H01-004 |
| Candidate reinterpreted as a discriminator, new discriminating question: apinocaltamide is useful because it could show whether ethosuximide's null-specific effect is T-type mediated | LD-001, card `next_measurement` |
| Wrong transfer avoided: five approved antipsychotics appear as GCN2 "hits" but are PharmGKB associations with unknown interaction type | LD-004 |
| Direction not assumed: genetic suppression of GCN2 in a fly does not give a drug direction for a need whose direction is uncertain | needs.json O5 limits; LD-004 |
| New discriminating question: which ISR kinase (GCN2 versus PERK) is engaged; it changes which lever card E01 should test | LD-004 |
| False "opposite" avoided: adenosine / regadenoson flagged opposed through one ligand-database row | LD-003 |
| Loop gap found: the need omitted GCN2, so the forward search was blind to it until the observation was written in | needs.json diff |
| Work saved: not measurable here; no advantage observed claimed | - |

## What was not read, and what was not verified

* Only PubMed titles and abstracts were read for apinocaltamide; no full text, so no FULLTEXT_READ_RECEIPT was staged and none of its rows is a "read".
* `catalog_build.py build` was run to relink the new card; its `catalog.jsonl.gz` and stats came out three lines different from the committed ones (cause not investigated), so only `card_identity_declarations.tsv` and `card_links.json` are committed. `card_links.json` lists `CHEMBL4217292` under `compound_ids_outside_catalogue` because the id lookup cache has no entry for it (UNRESOLVED, not absent; the link itself resolves).
* The GtoPdb artefact reading for adenosine is from the rows themselves and the coordinator's audit, not from the Guide to Pharmacology source.
* Halofuginone's mechanism is from general knowledge, not from a source read here.

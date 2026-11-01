# IT18 P2: catalogue funnel, the six direction discordances, vigabatrin sources (2026-11-01)

Non-canonical research material; not medical advice; computational counts and source checks, no benefit claim. Public edition, WWOX-DEE genotype class. Scientist, branch `it18-p2`. Question 3 of `../diagnosis_it18_20261101/README.md`: how many of the catalogue's records are identity-resolved, usable by the matching method and actually evaluated, and which IT17 discordance changes a card or a match.

## 1. Funnel (current data, recomputed today)

`funnel.py run` (offline, about 5 s, byte-identical on a second run) writes `funnel.tsv` (steps) and `funnel_reasons.tsv` (every exclusion, abstention and composition count, with category and unit). It writes no rule of its own: families are `repurposing_search.families`, the wide rule is `usable_census.row_usability` (IT7 M-net), the matching rule is that of `../evaluation_it17_p3_20261101/direction_task.py` and the P4 pre-registration, exclusions are `repurposing_search.artefact_reason`, need labels are `repurposing_search.associations_for_need`. No funnel generator existed in `catalog/` or `framework/scripts` (`catalog_build.units_block` stops at records and families and hard-codes `compounds_evaluated_against_WWOX_needs: 0`), so this is a counting script over existing rules, not a new method. The committed `catalog.jsonl.gz` was rebuilt from the cache today with `catalog_build.py build --check`: byte-identical.

| Step | Count | Of | Unit |
|---|---:|---:|---|
| S0 source records | 44,211 | | catalogue record (a salt, a stereoisomer, a source-only row each count once) |
| S1 identity-reconciled compounds | 16,475 | 40,268 families | family containing a ChEMBL record (parent/child, InChIKey connectivity layer, or the 485 source-only records joined by the GtoPdb ligand chain) |
| S2 usable by the matching method | 3,756 | 16,475 | S1 family with a human ChEMBL curated mechanism whose action maps to INCREASE/DECREASE and is not excluded |
| S3 evaluated in a card or ranking unit | 21 | 3,756 | S2 family that is a ranking-unit member or card-linked |
| S4 comparable hypotheses, ranking | 4 | 51 | unit-need pair: determinate need direction and an L2 state coherent or opposed (U17, U25 on T-type calcium; U20 seizure control; U21 glutamate receptor) |
| S4m comparable hypotheses, module need matching | 40 | 294 | family-need pair labelled consistent or opposed (of which 35 have the family in S2) |

Side rows, not in the chain and never added to it: wider IT7 M-net rule inside S1, 4,037 families (4,022 corroborated by ChEMBL or GtoPdb); 9,341 families outside S1 that the M-net rule would use but whose identity is unresolved; 15 of 69 ranking units have a catalogue family.

Why compounds leave each step (`funnel_reasons.tsv`, category in brackets):

* S1: 23,793 families are source-only records with no identifier or structure linking them to ChEMBL (22,072 DGIdb, 1,219 openFDA, 502 MATRIX) [missing data]; 8,701 of them have a name equal to a ChEMBL name or synonym, never merged on name, so S1 plus these is an upper bound of distinct compounds. GtoPdb ligand chain, per record-ligand pair: 485 merged; 2,472 point to an active ChEMBL id outside the catalogue selection [no result]; 14 related-not-merged and 4 conflicts [abstention]; 55 unresolved (44 obsolete or inactive ChEMBL ids, 6 structure unavailable, 1 not a compound record, 1 DrugBank ids disjoint [missing data]; 3 id unknown or ligand absent from the release [no result]).
* S2 (of 16,475): 10,371 no target row from any source [missing data]; 561 only DGIdb rows [missing data]; 1,223 ChEMBL mechanism only on non-human targets [out of scope]; 563 human mechanism without a determinate direction (binding agent 169, modulator 83, enzymes, partial agonist 36, other 35, ...) [abstention]; 1 excluded by a source rule (alfuzosin, section 2) [abstention].
* S3: 30 families are evaluated in total (25 unit members, 28 card-linked); 9 of them are not in S2 (lithium, magnesium, PX-478, selfotel, one unnamed: no target row; CPP-115: DGIdb rows only; ataluren, phenylbutanoic acid: no determinate direction; stiripentol: non-human mechanism only). 7 unit members are tool compounds kept outside the catalogue by design (INT ids) [out of scope]; 54 ranking units have no catalogue identity (36 IT9 proposals, classes, axes, modalities, diet) [out of scope]. 0 consumer ids are missing from the catalogue [error].
* S4: 25 unit-need pairs have an uncertain need direction; of the 26 determinate ones, 22 never reach coherent/opposed (11 not evaluable, 7 none, 2 direction unresolved, 2 no family) [abstention / missing data]. Only 10 of 23 needs carry a determinate direction.
* Sources [source state / incomplete query / error]: all seven sources fetched OK and complete; DGIdb is the 2024-06-10 export (newer content not queried); DSLD bulk probe interrupted, 3,726 names unprobed (access field only, no effect on S1 to S4); 0 probe errors.

Provenance: of the 3,756 S2 families, 3,568 rest on ChEMBL alone as carried by the catalogue (188 also carry a signed GtoPdb row through DGIdb; the raw GtoPdb file used by IT17 covers more); 695 also carry DGIdb rows whose claim source is ChEMBL v33, a copy of the same curation and not a second vote (alfuzosin is an example: the error is in both). MATRIX, openFDA and DGIdb attach to ChEMBL records only through UniChem, UNII or ChEMBL concept identifiers.

Reading: the catalogue holds 44,211 records but the matching method can address 3,756 identity-resolved compounds; 21 of those are in a card or unit, and the module has 4 ranking hypotheses (40 family-need pairs) where a compatible/opposite comparison is possible. The count of records says little about method reach.

## 2. The six ChEMBL-GtoPdb discordances (`discordances_resolved.tsv`)

None reaches an active card, unit or match: ADRA1A/B/D, HTR1A, DRD4 and ACHE are not need targets, and none of the four compounds is card-linked or a unit member. Each decisive link was checked at its source (ChEMBL API live, the DailyMed label ChEMBL cites, the cached GtoPdb 2026.3.1 rows and the PubMed abstracts of the cited references; abstracts only, no full text read):

| Compound, target | Finding | Right side |
|---|---|---|
| alfuzosin, ADRA1A/B/D (3 pairs) | ChEMBL AGONIST contradicted by its own cited label, section 12.1 ("selective antagonist"); still AGONIST in live ChEMBL_37; DGIdb ChEMBL v33 claims copy it | GtoPdb |
| repinotan, HTR1A | GtoPdb's own reference (PMID 9495870) calls it a 5-HT1A full agonist; antagonism there is at alpha-1, alpha-2, D2 | ChEMBL (module) |
| bromocriptine, DRD4 | ChEMBL agonist is a D2-like family statement; functional companion paper (PMID 12388667) finds bromocriptine inactive at hD4; GtoPdb cites only the binding paper. Antagonism not shown in what was read | ambiguous, kept |
| pralidoxime, ACHE | reactivator of the organophosphate-inhibited enzyme (ChEMBL) vs weak inhibitor of the native enzyme at about 0.9 mM (GtoPdb) | both, in different target states, kept |

Module change (alfuzosin only, because the module stated a wrong direction and an explanation built on it would be wrong): `framework/scripts/repurposing_search.py` gains `contradicted_action`, called first by `artefact_reason`; `coverage/source_artefacts.tsv` gains one rule `action_contradicted_by_cited_reference:CHEMBL1723:AGONIST` with the evidence. The ChEMBL row and the DGIdb ChEMBL-claim rows stay visible; their direction is not used (`source_artefact` exclusion); GtoPdb's antagonist rows on the DGIdb-only alfuzosin record are untouched. Regression: `test_repurposing_coverage.Detector.test_contradicted_chembl_action_is_flagged_only_for_its_molecule_and_action` (molecule, inherited row, DGIdb copy flagged; GtoPdb row, a genuine agonist and a corrected source untouched; the real rule loads), and the real-file rule-set assertion now lists the new rule kind. `repurposing_coverage.py run` changed only the inputs digest in `coverage_matrix.json` (no count moved). The IT17 direction task measures the raw field and is not edited. No change for repinotan (module right), bromocriptine or pralidoxime (context-dependent: a per-subtype or per-state rule would be a new method).

## 3. Vigabatrin assertions (`vigabatrin_sources_resolved.tsv`)

The seven WWOX-system assertions of U20 (`member_evidence.tsv`, empty `source_pmids`) and the two others of card `EB-VGB-01` cite papers by author and year through CLAIM 001. Resolved through the claim and paper registries and the receipt ledger: Shaukat 2018 (A-VGB-1, -2; PMID 30361190), Nagarajan 2023 (A-VGB-3; 37583270), You 2024 (A-VGB-4; 39101447), Riva 2022 (A-VGB-5; 35573960), all with a complete-read receipt and a manifest locator; Serce Pehlevan 2026 (A-VGB-6; 42092735, partial receipt with every section read, locator held); Chong 2023 (A-VGB-10, -11; 36537114, partial Scholar Gateway surface); Choi 2026 (A-VGB-7; 41442931, no receipt). Descriptive coding under the IT17 outcome semantics, from the held locators and not a re-read: favourable on objective 2 origins (Shaukat, Nagarajan), null 2 (Riva, Serce Pehlevan), undeterminable 2 (You: clinical freedom against a VEEG with seizures; Chong: poor control on three concurrent drugs), off-objective harm 1 (Choi, already coded). All predate the freeze, so nothing is prospective.

Re-reading needed: no for six of the seven origins. Chong 2023 only, and only if U20's coding matters: the held chunks mention vigabatrin once (patient 5, three drugs), so A-VGB-11 (improved only with the diet) cannot be located and "resistant to vigabatrin" is stronger than the held text.

Found and not fixed (the ranking would be regenerated with its snapshots and tests): `ranking_it8.py` line 416 writes "replication: none recorded: one source paper" whenever fewer than two favourable PMIDs resolve, including zero, so U20 is described as resting on one paper while it rests on two (Shaukat, Nagarajan); U10 (A51, sources cited as DL-THER-089, which resolves to PMID 42397075) is the other tested unit with empty `source_pmids`. The cause is that the card assertions cite registry ids or author-year, not PMIDs.

Queue reconciliation measured and still unlinked: IT16 P3 found 6 of 34 queue entries (esketamine, ABT-639, ulixacaltamide, bepridil, mibefradil, trimethadione) mentioned in reports; `deepening_queue.tsv` still reads NO_CARD_OR_RECORD_FOUND for them, with its own disclosure that reports were not searched. Not wired here, for the same regeneration reason.

## 4. Files and checks

`funnel.py`, `funnel.tsv`, `funnel_reasons.tsv`, `discordances_resolved.tsv`, `vigabatrin_sources_resolved.tsv`. Sources: ChEMBL_37 (CC BY-SA 3.0), GtoPdb 2026.3.1 (CC BY-SA 4.0 contents), DailyMed label (US public domain), PubMed bibliographic records; only identifiers, coarse classes and short quotations are kept. No registration, contact address, spend or external contact.

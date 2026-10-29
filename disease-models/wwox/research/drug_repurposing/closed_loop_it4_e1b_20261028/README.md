# IT4 E1, question B: useful partial benefit (scientist-d, 2026-10-28)

Non-canonical research material. Not medical advice; no efficacy, wet-lab or clinical claim; no dose; nothing here changes the four scientific current files; no receipt was written to the ledger (one is staged, see the end). No e-mail address was sent anywhere, no contact was made, no registration, no spend.

## The question and why this one

**Question.** Is the brain-MRI abnormality (intramyelinic oedema) liability of vigabatrin, the only drug class with human WWOX-DEE partial-benefit reports, different in a Wwox-deficient brain with a myelin deficit (mouse) or white-matter loss (patients; hypomyelination itself unresolved), and does a retina-sparing sibling (CPP-115) escape it?

**Why this thread (chosen by data).** Four threads were looked at.
* Vigabatrin / GABA, with ABAT now corrected: the join shows card EB-VGB-01 with "no next measurement defined", the catalogue holds CPP-115 as two unlinked families, and the label text on intramyelinic oedema meets the repository's own myelin and vacuole questions, which had never been put side by side. Chosen.
* Ketogenic diet (E04, EB-KD-01): already worked at three depths (ft125 re-read, CC-KETOGENIC-CLAIM, KETO-ENDPOINT); the open items are denominator and metabolic measurements that need new data, not a new reading. Not repeated.
* T-type (ethosuximide, apinocaltamide H01): the closed loop of iteration 3 already produced the card and its discriminating experiment. Not repeated.
* Glycaemia / growth: the need is an endpoint and confounder by design (no compounds). A link through vigabatrin was checked and not carried: the one human study found (ClinicalTrials.gov NCT04321395, vigabatrin and insulin sensitivity) is single-arm, four adults with obesity, no comparator; the supporting premise is obese-mouse work in a hyperglycaemic context, opposite to the hypoglycaemic Wwox-null mouse (P10 and P18); the vigabatrin label does not mention glucose. Abstention, no card.

## Premise verified

* Premise (the working-model wording before BATCH_20261019_025, since replaced): VABAM in WWOX-DEE as a safety signal that distinguishes WWOX. Verified against the sources: the Choi 2026 abstract (closed access, still no open copy on Europe PMC today) reports two children selected for having the finding and gives no denominator; the label (openFDA JSON, effective 2026-06-15, sections 5.3 and 5.4 read in full) puts MRI changes at 22 percent of vigabatrin-treated non-WWOX infants with infantile spasms against 4 percent on other therapies (retrospective, N=205, arm sizes not stated). Two reported children, with no denominator, cannot be shown to exceed (or fall below) those figures. The signal is documented; enrichment in WWOX is not supported. The Choi authors themselves leave susceptibility in delayed myelination open.
* Second premise: "a retina-sparing sibling is brain-sparing". The only comparison found for CPP-115 is an ERG in rats; no myelin or MRI endpoint exists in any CPP-115 or OV329 source found (PubMed query for CPP-115 or OV329 with myelin, vacuole, white matter terms returned only the two non-histological papers).

## WWOX knowledge used (and its true depth)

| Source | What was used | Depth |
|---|---|---|
| Repudi 2021 (PMID 33914858) via needs NEED-MYELINATION O1 and manifest entries 0, 15 to 17 | neuron-specific deletion: myelinated callosal axons 180 against 55 per field at P17, n 3 mice, field-level statistics | partial_fulltext_read (carried receipt FTR-20261003-33914858-03; not re-read) |
| Choi 2026 (PMID 41442931) | two WWOX children: baseline periventricular white matter loss and corpus callosum atrophy; new pallidal and thalamic signal change on vigabatrin; susceptibility question left open | abstract_only (closed access) |
| CLAIM 001 and card EB-VGB-01 | the efficacy and null single-patient reports (not restated; no sibling row compared with them) | as carried, read through registry_records.py |
| NEED-INHIBITORY-HYPOFUNCTION | direction uncertain; vigabatrin as cautionary | as carried |
| analysis notes on the Wwox rat-mutant vacuole question | the repository's counter-argument (severe hypomyelination predicts fewer intramyelinic vacuoles); a grep of three notes finds no mention of vigabatrin or VABAM | notes read in part |

## Counter-evidence and negative results kept

* Two WWOX children selected for the finding with no denominator, set beside the label's 22 versus 4 percent in non-WWOX infants; unmeasured follow-up MRI in the other WWOX vigabatrin reports is an unmeasured cell, not a negative; hormonal co-therapy is a rival explanation (two non-WWOX partial reads, conflicting on the MRI finding versus symptoms); disease severity and the underlying white matter disease are rivals.
* Neonatal and juvenile rat vacuoles are described by the label as distinct from adult intramyelinic oedema; the species bridge is partial.
* CPP-115: one human infantile-spasms case (PMC5024311, body read), open label, vigabatrin given concurrently for the first year, ketogenic diet and clobazam, parent-reported frequency against an EEG that disagrees in part, baseline MRI with dysmyelination, no repeat brain MRI described; the highest level in the rat spasm model was lethal; spasm cessation was not accelerated. OV329: rodent anticonvulsant abstracts only.

## Pharmacology and safety (keyless sources, all dated 2026-10-28)

* openFDA label (Novadoz vigabatrin oral solution, set id 082d818a-4f4e-4675-98c6-91db0294e63c): boxed warning of permanent vision loss; REMS program; MRI abnormalities in infants (5.3); intramyelinic oedema at post-mortem in infants and in rat, dog and possibly monkey at doses within the human range, no no-effect dose established, decreased myelination and oligodendrocyte injury in treated rats (5.4); nothing on glucose.
* ChEMBL REST: CPP-115 (CHEMBL4297273, salt of parent CHEMBL146927) max phase 1, no mechanism row. Catalogue: vigabatrin approved, prescription (23 NDC products by UNII).
* Guide to Pharmacology 2026.3.1 public downloads (ligands.csv sha256 f8e9f695..., interactions.csv sha256 cdbd18c6...): ligand 8284 CPP-115 has ChEMBL id CHEMBL146927 and an ABAT interaction typed Inhibitor; vigabatrin ligand 4821 "Irreversible inhibition". Curated database statements, in vitro, not efficacy.
* ClinicalTrials.gov API v2: CPP-115 one completed phase 1 (cocaine dependence), OV329 none, vigabatrin 41 records, none WWOX.
* Accessibility is not efficacy: vigabatrin is marketed under a REMS; CPP-115 and OV329 have no obtainable status established here. DSLD and supplements: not touched (no supplement or diet thread was run; the diet thread was set aside above).

## Catalogue finding (identity, by identifier)

DGIdb carries CPP-115 with an IUPHAR ligand concept id (8284); the catalogue keeps it as its own family (no status, unknown access) beside the ChEMBL CPP-115 family (clinical candidate, UNII, no target rows). GtoPdb ligands.csv gives ligand 8284 the ChEMBL id CHEMBL146927 (the parent in the catalogue) and the same InChIKey. Measured over the whole catalogue: 6,567 DGIdb-only records carry an IUPHAR ligand id; 510 of them map, through GtoPdb's ChEMBL id, to a ChEMBL record already in the catalogue (`ligand_identity_merge_candidates.tsv`, identifier-level candidates, not checked row by row; 3,567 have no ChEMBL id in GtoPdb; 2 ligand ids are absent from the release). Not fixed here (it changes family counts and coverage everywhere); proposed as a `catalog_build.py` rule for the coverage maintainer.

## Decision it changes

1. The working-model sentence on VABAM should read as documented, case-selected, no denominator; not as a WWOX-specific excess (the label's 22 versus 4 percent concerns non-WWOX infants and is not a WWOX rate). Ready-to-apply text is in the report of this task.
2. EB-VGB-01's "no next measurement defined" is answered by card H02: a genotype-by-exposure test in a surviving Wwox-deficient juvenile model plus a denominator-bearing case count, with predictions registered in both directions.
3. The sibling inference "retina-sparing means myelin-sparing" is blocked until a brain endpoint exists for CPP-115 or OV329.
4. No favourable compound is offered. Status of the card: controversial.

## Regeneration and tests

Commands run, in order: `check_cards.py` (23 packets, 0 problems; the NOT WWOX EVIDENCE label test now also accepts a row whose `evidence_scope` is a WWOX system, which the old token test could not express for human WWOX rows); `catalog_build.py build` with the root cache (only `card_links.json` kept: the rebuilt `catalog.jsonl.gz` and stats differ widely because the root cache holds no Guide-to-Pharmacology files, so they were discarded and the committed ones restored); `repurposing_coverage.py run` after adding 11 rows to `assertion_pertinence.tsv` (all 11 new drug assertions listed, none counted for L3 or L4), `check` OK; `repurposing_join.py handoff` (the card is not named by a mechanism-map record, so `join run` was not needed and its unrelated upstream drift, a third receipt for one ISR paper, was left out); `repurposing_view.py run`, `check` current.
Micro-upgrade found by the new card: `catalogue_leads()` listed a card twice when it attaches to one family as both named member and assertion subject; fixed by listing one row per card, with a regression test.
Suites: `test_repurposing_join.py` 54, `test_repurposing_coverage.py` 52, `test_repurposing_view.py` 23, `test_catalog_build.py` 22, `check_needs.py`, `test_tool_routing.py`, `legend_lint.py` (OK, warnings pre-existing), `public_release_gate.py` PASS (0 blocks; no finding on these files).

## What was not read, and what was not verified

* Abstract only: Choi 2026 and every PubMed source of the card except PMC5024311. Label: sections read, cited study not.
* PMC5024311: body read; Figure 1 image and reference list not read.
* No full text of any vigabatrin rodent or dog study was opened; the lesion thresholds are the abstracts' statements. The quantitative comparison of CPP-115 and vigabatrin potency was not reproduced (the database values differ from the publication's figure for the inactivation ratio). **Update 2026-10-29 (IT5 P5, `pharmacology_it5_20261029/README.md`):** the constants are inactivation KI values on pig, rat or mouse enzyme (the human label is a target mapping; no human-enzyme measurement was found); the direction (CPP-115 the more efficient inactivator) is reproduced in independent sources, the size is not (KI ratio about 5 in the only same-assay comparison, 88 to 320 across other sources, two incompatible derivations of 187 in print); enzyme-level advantage says nothing about brain myelin.
* The 22 versus 4 percent figure is the label's statement of a study not read; setting a denominator-free report beside it is an inference owed a blind audit; the blind audit (scientist-c) found no HIGH defect and its MEDIUM and LOW defects are repaired in this card.
* Whether a Wwox-deficient animal survives the vulnerable window is not established here.
* The 510 merge candidates are not verified individually.

* Repaired after the blind audit: the mechanism text now separates rat (abstract of one electron-microscopy study: myelin-sheath splits), dog and label (gray-matter neuropil vacuolation) and the single-autopsy basis of infant intramyelinic edema; label 8.4 says the juvenile-rat no-effect dose was the lowest level tested (the number is omitted because the card checker forbids dose tokens), against 5.4's 'no no-effect dose established', and the 21473881 versus 25554247 threshold difference is flagged, not reconciled; the 'hypomyelinated' framing is reworded; DA-001 numbers and DA-003 are marked UNVERIFIABLE_SURFACE.

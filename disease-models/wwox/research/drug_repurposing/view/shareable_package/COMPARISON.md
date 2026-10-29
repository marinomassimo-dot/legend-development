# Comparison with the full research version

The full version (`view/index.html` in the repository, local use) and this package are built from the same inputs by the same builder; only the data boundary differs. Counts below are computed, not typed.

## Same in both

- 36 candidate cards with their six answers, evidence by scope, counter-evidence, next step, public identifiers and F/C/P positions: card text and positions are identical (the only card fields that differ are listed under 'Different').
- 22 needs and their observations, the threads, groups, goals, funnel, access chart (catalogue-wide counts), matrix summary, dispositions, observations, lead dispositions and the Italian orientation texts.
- Sections of the data object that are byte-identical: access, dispositions, exploration_flagged, has_distinct, matrix_summary, no_probability, observations, orphan_priorities, pair_unit, ranking_note, schema, strings.
- Curated sections identical: contexts, evidence_graph, gaps, goals, group_note, groups, hypotheses, predictive, scopes, selection, threads, tracks, work_order.

## Different (withheld here, present in the full version)

| What | Full | Shareable |
|---|---|---|
| Catalogue rows shown with a name | 1494 | 42 (card names only; the other 1464 rows carry an identifier) |
| Rows with per-row status class or modality | 1506 | 0 |
| Rows with a per-row access category | 1480 | 11 (openFDA-stated categories and absence statements only) |
| Matrix pairs with a target list | 1342 of 1712 | 12 of 1712 |
| Target symbols listed in pairs | 1861 | 12 |
| Card actions on targets listed | 39 | 0 |
| Pair objects carrying a status class | 680 | 0 |
| Excluded rows listed with compound name and gene | 3 | 0 |
| Card fields that differ (count of cards) | n/a | {"access": 7, "access_text": 7, "actions": 8, "asserts": 2, "brief": 1, "card_path": 36, "country": 4, "for": 2, "identity": 7, "links": 7, "mechanism": 1, "next_full": 3, "novelty": 2, "pharm": 2, "reopen": 1} |

## Prose redactions (shareable only)

12 card sentences and 11 lead fields that stated a compound-target pair, a catalogue-only compound or a per-compound status from a class-B/C source are rewritten at the level of the need or class and name the withheld source class (`dato di una fonte non inclusa in questa versione`); 48 repository file names are described instead of printed. The conclusion of each lead and card is kept. The rule is in `view/shareable_sources.json` (`prose_policy`) and the audit enforces it.

## Why: counts of catalogue target rows by class

The catalogue holds 44,211 records. Its target rows by class: {"A": 1623, "B": 47061, "C": 57631}.

| Claim source | Class | Catalogue rows | Terms | In this page |
|---|---|---|---|---|
| CGI | C (identifiers and counts) | 368 | CC BY-NC 4.0, declared by DGIdb | 0 |
| CIViC | A (attribution) | 1,120 | CC0 1.0; verified at docs.civicdb.org | 19 |
| COSMIC | C (identifiers and counts) | 37 | custom terms, declared by DGIdb | 0 |
| CancerCommons | C (identifiers and counts) | 109 | custom terms, declared by DGIdb | 0 |
| ChEMBL | B (share-alike) | 16,947 | CC BY-SA 3.0 Unported (chembl.gitbook.io); attribution: ChEMBL URL and release version (chembl.github.io/chembl-licensing, read 2026-10-29) | 0 |
| ChEMBL curated mechanism | B (share-alike) | 8,068 | CC BY-SA 3.0 Unported (ChEMBL curated mechanisms) | 0 |
| ClearityFoundationBiomarkers | C (identifiers and counts) | 163 | unknown; data no longer available | 0 |
| ClearityFoundationClinicalTrial | C (identifiers and counts) | 240 | unknown; data no longer available | 0 |
| DTC | C (identifiers and counts) | 23,879 | CC BY-NC-SA 3.0, declared by DGIdb; not verified at source | 0 |
| DoCM | A (attribution) | 76 | CC BY 4.0; verified in the project's archived about page (docm.info now redirects to GitHub) | 3 |
| FDA | A (attribution) | 427 | public domain unless otherwise noted; verified at fda.gov website policies | 0 |
| GuideToPharmacology | B (share-alike) | 16,070 | ODbL (database) and CC BY-SA 4.0 (contents) | 0 |
| JAX-CKB | C (identifiers and counts) | 2,148 | CC BY-NC-SA 4.0, declared by DGIdb and read on ckb.jax.org/about/index (2026-10-29) | 0 |
| MyCancerGenome | C (identifiers and counts) | 829 | restrictive custom terms, declared by DGIdb | 0 |
| MyCancerGenomeClinicalTrial | C (identifiers and counts) | 317 | restrictive custom terms, declared by DGIdb | 0 |
| NCI | C (identifiers and counts) | 6,231 | public domain declared by DGIdb only; NCI reuse page (read 2026-10-29) says NCI text is free of copyright but does not name data or the Cancer Gene Index | 0 |
| OncoKB | C (identifiers and counts) | 148 | non-commercial custom terms, declared by DGIdb | 0 |
| PharmGKB | B (share-alike) | 5,976 | CC BY-SA 4.0 (ClinPGx), reported by the DGIdb service; the ClinPGx data-usage page is script-rendered and its text could not be read on 2026-10-29 | 0 |
| TALC | C (identifiers and counts) | 602 | rights in a publisher's supplementary table | 0 |
| TEND | C (identifiers and counts) | 2,242 | rights in a publisher's supplementary table | 0 |
| TTD | C (identifiers and counts) | 15,246 | unclear (all rights reserved versus open access), declared by DGIdb | 0 |
| TdgClinicalTrial | C (identifiers and counts) | 5,072 | rights in a publisher's supplementary table | 0 |

Classes: **A** redistribute with attribution (only fields the source's own authors own); **B** share-alike: never merged into the page; **C** identifiers and counts only; **D** local only. Class B content is shipped only for ChEMBL, as a separate file; GtoPdb and ClinPGx stay counts-only (reasons in `NOTICE.md`).

Third-party identifier values that exist in the catalogue and are not embedded at all (DrugBank, ChEBI, ATC, UNII, InChIKey, MATRIX ids): {"atc": 4875, "chebi": 13263, "drugbank": 13539, "inchikey": 15242, "matrix_id": 1927, "unii": 15002}.

## What the withheld parts mean for a reader

The physician-facing content (what to study, on what evidence, with which gaps) is complete here. What is withheld is the catalogue-level detail that backs the links between compounds and targets: which database says what about which compound. Where the full version shows a target list for a compound, this one shows how many source rows exist and that they were withheld. Nothing is hidden to change a conclusion; the counts and the statement that rows were withheld stay visible on the page.

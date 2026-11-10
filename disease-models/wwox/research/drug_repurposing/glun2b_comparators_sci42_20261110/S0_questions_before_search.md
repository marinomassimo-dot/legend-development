# SCI42 S0 — decisive questions, fixed before any search (2026-11-10)

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Task record `ledger/tasks/orchestrator/ORCH-SCI42-20261110.json`.

## State read (nothing re-derived)

* Starting material read whole: `generation_it41_20261109/` README, `comparison_S1.md`, `comparisons_it41.md`, `compound_view.tsv` (V06 onfasprodil, V07 NP10679, V09 DQP-1105), `verify/VERDICTS.md`, `collab_questions_it41.md`; INV-05 design in `ampa_nmda_discrim_20261108/output/prediction_matrix.tsv` (M01–M18) and `nmda_composition_discrim_20261109/` (README, consumer_delta).
* Ledger of receipts: no receipt exists for PMID 40767837 or 36642931 (both `[]`). Nothing to reuse; both are first readings.
* Identity (Harness `compound_identity.py`, run today): onfasprodil = catalogue CAT:CHEMBL5095074 (NAME_EXACT; MIJ821 is a SYNONYM_EXACT of the same record; a second, DGIdb-only record has the same name, no ChEMBL link); ChEMBL human GRIN2B measured activity: one IC50 row. NP10679 = CAT:CHEMBL5095254 (record name NP-10679; NAME_EXACT under the hyphenated spelling); no ChEMBL activity row for GRIN2B/2A/2C. DQP-1105: NOT_FOUND_BY_NAME in the catalogue (a statement about the name and the sources read, not about the compound). Selectivity is NOT_ASSESSED by construction; the registry value for onfasprodil is one datum (pIC50 8.08 = IC50 8.3 nM), patent-sourced in GtoPdb.
* Carried corrections from the IT41 verifier that bind this package: the 0.88 bound is ifenprodil's, not a class bound; radiprodil's 82 vs 45 is assembly-dependent; the NP10679 "approved" flag in GtoPdb conflicts with ChEMBL max phase 1 and the abstract (not carried); DQP-1105's registry row is unresolved, not "measured on GluN2C".

## Decisive questions (S1; the producer answers only these)

**Onfasprodil / MIJ821 (PMID 40767837 and the primary pharmacology it cites or that the catalogue points to)**
* O1. Is a receptor site stated, and on what basis (competition with ifenprodil, mutagenesis, structure, or only a label)? Declared by the authors, or measured?
* O2. Maximum inhibition (not only potency) on GluN1/GluN2B diheteromers and on GluN1/GluN2A/GluN2B triheteromers, species, expression system, glutamate, glycine, Zn2+/chelator, pH, holding potential. If triheteromers were not tested, say so.
* O3. Subunit selectivity actually measured (GluN2A/2C/2D), and any off-target panel.
* O4. Where the pIC50 8.08 / 8.3 nM comes from (patent or paper), and whether it is a measured primary value.
* O5. Human exposure: which populations, which endpoints, and whether any non-psychiatric context exists; what the abstract-level clinical papers cannot say.

**NP10679 (PMID 36642931 and the primary pharmacology paper(s))**
* N1. pH dependence of potency AND of maximum effect (oocytes: pH 6.9 against physiological); is it a property of the molecule, of the class (ifenprodil-site NAMs; proton sensing by GluN2B), or both?
* N2. Site and mechanism; GluN2B selectivity; Mg2+/voltage/use dependence; recombinant species and assembly (including triheteromers).
* N3. Any slice or native-tissue datum (region, age, pH of the bath).
* N4. Human data (phase 1 healthy volunteers) and what they do not say.

**Cross-cutting**
* X1. Which of the two adds a comparison that ifenprodil / Ro 25-6981 / radiprodil / d-APV do not already give, and which condition or mechanism it would separate? If the site is unknown, which comparison stays interpretable?
* X2. Provenance of each decisive number: original measurement, database copy, patent, or repeated.
* X3. Distribution terms of any artefact proposed for delivery (shareable edition omits compound names and registry-derived values; share-alike registry licences).

Not asked: AMPA, HIF1A–BNIP3, fly; a general census of NMDA pharmacology; a clinical or dosing question.

## Design questions (S3; reasoned from S1 outputs, no new search)
* D1. With a measured percent of isolated NMDAR current removed as the x-axis and d-APV as the reference, which controls must run from the start (bath pH and Mg2+ measured; vehicle time control; engagement readout; Zn2+ chelator arm) and which can wait?
* D2. What does each of four explanations (total gain; GluN2B-containing weight; preparation state incl. pH/Mg2+; alternative action or general loss of network function) predict, what is compatible but not discriminating, what weakens it, and what control interprets a null?
* D3. Unit of replication (animals, not cells), and which thresholds are design assumptions.

## Conditional / expansion
* S5 (DQP-1105 row) only if capacity remains after S4b. S6 (GABA-A or chloride) chosen with the actual priorities of the Orchestrator of IT42 after S4b; a brief if it would need a campaign.

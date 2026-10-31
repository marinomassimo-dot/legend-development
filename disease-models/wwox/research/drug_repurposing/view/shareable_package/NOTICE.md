# NOTICE: sources, terms and credit lines

Package of the LEGEND WWOX repurposing view, shareable edition. Distributable edition. This file set is not itself a publication: a copy is public only where the operator has put it, and publication on any external surface is a decision of the operator. A reader who obtained these files from a web address is reading the operator's publication of them.
Research material about a disease-level genotype class, not medical advice, not a ranking of treatments. Not legal advice: the terms below are the licence reading recorded in the repository (`catalog/README.md`, section Licence reconciliation, IT5 P1) as corrected by its independent verification of 2026-10-29.

## 1. Own text and computations

Cards, needs, priorities, positions (F/C/P), dispositions, counts and the Italian orientation texts were written or computed in this repository. Licence: the repository `LICENSE` (MIT), copied as `LICENSES/LEGEND-MIT.txt`. Credit: LEGEND WWOX repurposing module (this repository). The licence of the repository covers original text only; it does not cover third-party rows.

## 2. Third-party content embedded in `index.html` (class A: attribution)

- **CIViC (via DGIdb)** (20 rows or attributes embedded). Terms: CC0 1.0 Universal (licence field reported by the DGIdb service on 2026-10-28). Credit: CIViC, obtained through DGIdb (export of 2024-06-10); credit given as a courtesy https://civicdb.org/
- **DoCM (via DGIdb)** (3 rows or attributes embedded). Terms: CC BY 4.0 (licence field reported by the DGIdb service on 2026-10-28). Credit: Database of Curated Mutations (DoCM), CC BY 4.0, obtained through DGIdb (export of 2024-06-10) http://www.docm.info/
- **openFDA NDC (access categories)** (15 rows or attributes embedded). Terms: Public domain (openFDA licence page). Credit: Data provided by the U.S. Food and Drug Administration. Do not rely on openFDA to make decisions regarding medical care. No FDA endorsement is implied. https://open.fda.gov/license/

How the conditions are met:

- CIViC (CC0 1.0): no condition; credit is given as a courtesy. Legal code: `LICENSES/CC0-1.0.txt`.
- DoCM (CC BY 4.0): attribution (above), a link to the licence (https://creativecommons.org/licenses/by/4.0/ ; legal code `LICENSES/CC-BY-4.0.txt`), an indication of changes (rows are reduced to gene symbol and the action recorded, regrouped by this repository), no endorsement implied. The live DoCM site is gone: the terms were read in the project's archived about page.
- openFDA NDC (CC0 1.0 dedication; credit requested, not required): the per-compound access categories `prescription` and `OTC`, stated from the NDC directory. Credit: Data provided by the U.S. Food and Drug Administration. Do not rely on openFDA to make decisions regarding medical care. No FDA endorsement is implied.
- FDA pharmacogenomic biomarkers (public domain unless otherwise noted on fda.gov): allowlisted; zero rows are embedded in this build.
- The Every Cure MATRIX drug list (CC BY 4.0 for the fields its authors own: names, approval flags) is allowlisted for names; no MATRIX name is embedded in this build, and none of the ATC, DrugBank or ChEBI identifiers it carries (third-party content that a dataset-card licence cannot grant).

## 3. Identifiers and bibliographic facts (no third-party content beyond the identifier)

- **HGNC**: CC0 (genenames.org/about/license); attribution recommended. Gene symbols and HGNC identifiers: HGNC (https://www.genenames.org/) https://www.genenames.org/about/license/
- **PubMed bibliographic facts**: bibliographic facts (PMID, title, journal, year); no abstract and no passage of an article is embedded; article and abstract rights stay with their holders (NLM policy). Bibliographic data: PubMed, National Library of Medicine (https://pubmed.ncbi.nlm.nih.gov/) https://www.nlm.nih.gov/web_policies.html
- **ChEMBL identifiers**: identifiers only; ChEMBL content is not embedded (class B file shipped separately). ChEMBL identifiers (CHEMBL...): EMBL-EBI, https://www.ebi.ac.uk/chembl/, release ChEMBL_37 (2026-05-01) https://www.ebi.ac.uk/chembl/
- **GEO series and UniProt accessions cited in own text**: accession identifiers only (GSE126075, GSE156243, UniProt accession numbers); no deposited matrix, sequence or annotation text is embedded; NCBI places no restriction on its data but submitters may claim rights (NCBI Policies and Disclaimers page, read 2026-10-29); the UniProt licence page was not readable on 2026-10-29. Gene Expression Omnibus, National Center for Biotechnology Information (https://www.ncbi.nlm.nih.gov/geo/); UniProt Consortium (https://www.uniprot.org/) https://www.ncbi.nlm.nih.gov/
- **ClinVar-derived counts and RefSeq accession in own text**: counts computed in this repository from a ClinVar snapshot, and the RefSeq accession NM_016373.4; NCBI information created by or for the US government is public domain, ClinVar asks for attribution of ClinVar and its submitters (NCBI Policies and Disclaimers page read 2026-10-29; the ClinVar data-use page was not readable). Source: NCBI ClinVar and RefSeq, National Library of Medicine (https://www.ncbi.nlm.nih.gov/clinvar/) https://www.ncbi.nlm.nih.gov/
- **Record names shown in the page (1,506 values in the row table)**: 1,464 are catalogue identifiers (ChEMBL accession numbers and DGIDB: hashes of DGIdb drug names, no name text); 42 are card names written in this repository (16 molecule families, 26 interventions or classes). A card name that coincides with a ChEMBL preferred name is used as the compound's name, a fact, not as a copied ChEMBL field; ChEMBL names as data travel only in the separate class-B file. LEGEND WWOX repurposing module (this repository); ChEMBL identifiers: EMBL-EBI, https://www.ebi.ac.uk/chembl/
- **Catalogue record identifiers**: opaque identifiers of this repository's catalogue (CAT:...), no source content. LEGEND WWOX repurposing module (this repository)

Identifier census of `index.html` (distinct values): {"CAT": 2229, "CHEMBL": 302, "DOI": 5, "HGNC": 12, "NCT": 0, "PMID": 93}. No abstract and no passage of an article is embedded. Short quotations are marked by quotation marks and attributed (section 6).

## 4. Class B (share-alike): shipped as a separate file, never merged into the page

- **chembl**: `class_b/chembl_cc-by-sa-3.0/chembl_cc-by-sa-3.0.jsonl` (CC BY-SA 3.0 Unported). ChEMBL, EMBL-EBI, https://www.ebi.ac.uk/chembl/ , release ChEMBL_37 (2026-05-01). Records: the twelve ChEMBL records the module's cards name (selected through the repository's card-to-catalogue link table, not shipped here). Licence text and credit line travel with it in the same folder (`LICENSE_CC-BY-SA-3.0.txt`, `CREDIT.txt`).

Decision for the three share-alike sources, with reasons:

- **ChEMBL (CC BY-SA 3.0): shipped as a separate file.** The condition is attribution naming the ChEMBL URL and the release version, and distribution of any adaptation under the same licence. It can be met exactly: the file is a selection of twelve records and of listed fields (an adaptation, stated as such), carries the legal code and the credit line, and is not merged with anything else; the single page embeds only ChEMBL identifiers, so the share-alike condition attaches to that file only (CC BY-SA 3.0 section 4(a), Collection).
- **GtoPdb (ODbL database, CC BY-SA 4.0 contents): counts only.** Two licences apply to the same rows, ODbL carries its own rules for a publicly used Derivative Database, and the catalogue merges GtoPdb ligand data into its records. A correct separate file would need a split the catalogue does not hold; it is not widened.
- **ClinPGx / PharmGKB (CC BY-SA 4.0 declared by DGIdb): counts only.** The data-usage policy page was script-rendered and its text was never read; an unread condition is not honoured by guessing.

## 5. Counted but not embedded

- **NCI Cancer Gene Index (via DGIdb)**: class C until the Cancer Gene Index is covered by a sentence at NCI: DGIdb declares public domain; NCI's reuse page (cancer.gov/policies/copyright-reuse, read 2026-10-29) says text in NCI products is free of copyright unless otherwise indicated, asks that NCI be credited, and flags third-party graphics, but it uses neither the words public domain nor data or datasets and does not name the Cancer Gene Index (IT7 P8 verifier D4; IT8 P2 re-read); rows are counted, never embedded
- **ChEMBL**: CC BY-SA 3.0 (EMBL-EBI): no ChEMBL content in the single page; ChEMBL identifiers are kept; the ChEMBL records and curated mechanisms of the twelve card compounds are shipped as a separate class-B file with its own licence text and credit line (shareable_package/class_b/chembl_cc-by-sa-3.0/) (version ChEMBL_37 2026-05-01)
- **GtoPdb (via DGIdb and the public download)**: class B, not shipped: database ODbL and contents CC BY-SA 4.0 at once (two licences on the same rows); counts only
- **ClinPGx / PharmGKB (via DGIdb)**: class B, not shipped: CC BY-SA 4.0 declared by DGIdb; the data-usage policy page was not read; counts only
- **DGIdb (other claim sources: DTC, TTD, TdgClinicalTrial, TEND, JAX-CKB, CGI, MyCancerGenome and its trials, ClearityFoundation, OncoKB, CancerCommons, COSMIC)**: class C: non-commercial, unclear, publisher-table or unknown terms declared by DGIdb; counted, never embedded
- **NIH DSLD**: probe counts only; supplement access categories of individual compounds are withheld (version API v9.4.0)
- **UniChem**: cross-reference identifiers only; none is embedded in the page (version Last-Modified src1src14=Sat, 24 Oct 2026 21:16:36 GMT; src1src2=Sat, 24 Oct 2026 21:16:01 GMT; src1src7=Sat, 24 Oct 2026 21:16:11 GMT)
- **Every Cure MATRIX third-party identifiers (ATC, DrugBank, ChEBI)**: identifiers-only (class C): a dataset-card licence cannot grant rights in third-party content; none is embedded in the page
- **DrugBank**: identifiers only; no DrugBank text or table; no DrugBank identifier is embedded in the page

Withheld catalogue target rows by class: {"A": 1623, "B": 47061, "C": 57631} (class A rows are embedded only where they touch a need; see `manifest.json`).

## 6. Provenance of the cards' own text

Every output string was compared with the full texts, abstracts and openFDA label sections held locally; the result is recorded in `TEXT_PROVENANCE.json`. Bibliographic titles are facts and are listed apart. Quotations are limited to a few marked passages, each short (the longest is one sentence of an article, introduced by `the authors write`); no label section and no abstract is reproduced. The comparison covers only texts held locally when it was run (stated in that file).

## 6b. Prose policy: own analysis stays, database rows in prose do not

IT5 P13 fix. Own analysis stays in the shareable build: a conclusion at the level of a need, a class or a card subject, in our own words, short, attributed to a published work. Withheld: (1) a sentence that states a compound-target(-action) pair together with its database of origin when the pair is asserted only by a class-B/C catalogue source; (2) a compound named in prose whose only provenance in the repository is a class-B/C catalogue row (it appears in no cited full text and is not a card subject); (3) a per-compound status, phase, approval or access statement attributed to a class-B/C source; (4) repository file names, which cannot be used outside the repository. The replacement keeps the research conclusion and names the withheld source class with the phrase in withheld_phrase. The FULL build keeps everything. The audit enforces (1) and (2) by derivation from the catalogue, (3) and (4) by pattern, and every redaction below must match exactly once or more: a stale redaction fails the build.

Applied in this build: 12 card sentence redactions, 11 lead-field redactions, 923 pair objects stripped of a status class (pairs[].p.cr.pha[1] (status classes of the row) is dropped in the shareable build: a status class derives from ChEMBL max_phase, DGIdb approved flags, MATRIX and openFDA together, and the build does not re-derive a class-A-only status per row.), 115 repository file names replaced by a plain description. The replacement phrase is `dato di una fonte non inclusa in questa versione`.

Short third-party labels that card text also contains (checked against ChEMBL's curated-mechanism and target wording; none longer than 8 words, otherwise the audit fails): `caspase 1 inhibitor`; `gaba a receptor`; `pyruvate dehydrogenase kinase`; `reactive oxygen species`. They are generic scientific terms that the cards use in their own sentences; they are listed, not hidden.

## 7. What this notice does not do

It does not clear anything for publication: the operator decides whether and where to publish. It is not legal advice.

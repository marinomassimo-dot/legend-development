# Third-party notices

The repository-level `LICENSE` applies only to material for which the repository
authors hold the necessary rights. Third-party datasets, models, database
records, and derived assets remain subject to their original terms.

## Coverage and publication status

| Source | Licence / reuse basis | Status in this repository |
|---|---|---|
| NCBI PubMed | Public bibliographic service; linked abstracts/articles retain source-specific rights | MIXED — bibliographic facts only are shipped; no abstracts or full texts |
| AlphaFold DB | CC BY 4.0 | PUBLIC |
| NCBI ClinVar | Public distribution with requested attribution and NCBI disclaimer | PUBLIC |
| GTEx | Open aggregate data plus controlled-access components | MIXED — only public aggregates authorised |
| Meta FAIR ESM-2 | MIT | PUBLIC |
| ThermoMPNN | MIT | PUBLIC |
| Monarch Initiative / Monarch KG | BSD-3-Clause application code; source-specific terms for integrated KG data | MIXED — citation/interoperability only |
| DisMech | BSD-3-Clause declared by the public repository | PUBLIC — citation/audit only |
| Drug-repurposing module sources (DGIdb claim sources, ChEMBL, Guide to PHARMACOLOGY, ClinPGx, openFDA, MATRIX drug list, UniChem, others) | per source; see `DATA_SOURCES.md` and `disease-models/wwox/research/drug_repurposing/catalog/README.md` ("Licence reconciliation") | MIXED — share-alike (ChEMBL CC BY-SA 3.0, GtoPdb ODbL / CC BY-SA 4.0, ClinPGx CC BY-SA 4.0) and non-commercial (DTC, CKB-CORE, CGI and others, inside DGIdb rows) terms apply to parts of the tracked data; the MIT licence does not cover those parts |
| Public GEO series, iLINCS / LINCS L1000, ClinicalTrials.gov raw pages, NCBI RefSeq record NM_016373.4, PRISM and Drug Repurposing Hub tags, OmniPath-derived network edge tables | per source; see the section "Added components of the drug-repurposing and analysis work" below | MIXED — derived statistics and identifiers only, except the raw ClinicalTrials.gov pages, one RefSeq record and the share-alike edge tables, each described below |
| NumPy 1.26.4 / 2.0.2 | BSD-3-Clause | PUBLIC — optional MD / release-analysis dependency, not redistributed |
| OpenMM 8.1.1 | MIT for most source; LGPL for CUDA/OpenCL platforms; additional bundled notices may apply | MIXED — optional dependency, not redistributed |
| PDBFixer 1.12 | MIT in the retained package metadata | PUBLIC — optional dependency, not redistributed |
| MDTraj 1.10.3 | LGPL-2.1-or-later; separately licensed subcomponents may apply | MIXED — optional dependency, not redistributed |

## AlphaFold Protein Structure Database

Shipped AlphaFold-derived assets are identified in `DATA_SOURCES.md`.

- Copyright: DeepMind Technologies Limited.
- Licence: Creative Commons Attribution 4.0 International (CC BY 4.0).
- Terms and disclaimer:
  <https://alphafold.ebi.ac.uk/assets/License-Disclaimer.pdf>
- Required scientific attribution includes the AlphaFold DB and relevant
  AlphaFold methods/database publications.

## NCBI ClinVar

ClinVar is a freely accessible public archive built from submitter records.
NCBI asks redistributors to attribute ClinVar and the relevant submitters.
ClinVar information is not independently verified by NIH and is not intended
for direct diagnostic or medical decision-making without professional review.

- Data-use and attribution page:
  <https://www.ncbi.nlm.nih.gov/clinvar/docs/maintenance_use/>

## GTEx

Only aggregated open-access GTEx-derived values are authorised in this
repository. Protected-access sequence data and full donor metadata are not
included and must never be introduced.

- Open-access download and acknowledgement guidance:
  <https://gtexportal.org/home/downloads/adult-gtex/overview>

## Meta FAIR ESM-2

Repository-generated ESM-2 scores derive from the archived Meta FAIR ESM
software/model family.

- Source and licence: <https://github.com/facebookresearch/esm>
- The source repository states that its source code is MIT-licensed.
- Model outputs remain computational predictions and require scientific
  citation of the relevant ESM-2 publication.

## ThermoMPNN

ThermoMPNN-derived predictions are shipped. The canonical public project is
Kuhlman-Lab/ThermoMPNN and its code/model repository is MIT-licensed,
Copyright 2023 Kuhlman-Lab.

- Source and licence: <https://github.com/Kuhlman-Lab/ThermoMPNN>
- Primary citation: Dieckhaus et al., *PNAS* (2024),
  DOI <https://doi.org/10.1073/pnas.2314853121>
- The exact commit and checkpoint used by the original WWOX run were not
  retained. The shipped output is labelled as a non-reproducible legacy public
  derivative and must not be represented as clean-clone reproducible.

## Monarch Initiative / Monarch Knowledge Graph

This repository links to the Monarch stack for public disease-level ontology
interoperability. It does not redistribute a Monarch KG dump. Monarch's web
application and source code use BSD-3-Clause; records integrated into the
knowledge graph retain the licences and attribution requirements of their
named upstream sources.

- Terms and source-specific licensing: <https://monarchinitiative.org/kg/terms>
- Status: `MIXED`; only citation, links, and separately licensed public
  ontology identifiers are used here.

## DisMech

This repository describes interoperability with the public DisMech
mechanistic-disease knowledge base but does not vendor its source or data.
The DisMech repository declares `BSD-3-Clause` in `pyproject.toml`.

- Source: <https://github.com/monarch-initiative/dismech>
- Status: `PUBLIC`, citation/audit only.
- Caution: the upstream `LICENSE` copyright-holder field was still placeholder
  text when audited on 2026-07-25. Reconfirm with the maintainers before
  redistributing DisMech code or data; this does not block linking to it.

## Optional molecular-dynamics environment

The repository provides `environment-md.yml` as an opt-in reconstruction of a
previously working exploratory environment. It does not vendor these packages.

- NumPy 1.26.4 (optional MD environment) and 2.0.2
  (`requirements-analysis.txt`) — BSD-3-Clause:
  <https://github.com/numpy/numpy/tree/v1.26.4>
  and <https://github.com/numpy/numpy/tree/v2.0.2>
- OpenMM 8.1.1 — most source is MIT; CUDA/OpenCL platforms are LGPL, with
  additional component notices:
  <https://github.com/openmm/openmm/releases/tag/8.1.1>
- PDBFixer 1.12 — MIT according to the retained 1.12 package metadata:
  <https://github.com/openmm/pdbfixer/blob/v1.12/LICENSE>
- MDTraj 1.10.3 — LGPL-2.1-or-later, with separately licensed subcomponents:
  <https://github.com/mdtraj/mdtraj/blob/1.10.3/LICENSE>
- PyMuPDF 1.28.2 (`requirements-analysis.txt` and the optional environment, pinned
  2026-09-11) — AGPL-3.0-or-later, from Artifex Software, with a commercial licence
  offered separately; MuPDF, the C library it binds, carries the same terms:
  <https://github.com/pymupdf/PyMuPDF/blob/1.28.2/COPYING>. Used only as a local
  extractor for text layers and page renders of lawfully held files; no PyMuPDF or MuPDF
  code is vendored or redistributed here. Extraction receipts written before the pin name
  1.26.5; `reacquire.py` names a digest that moves between the two `EXTRACTOR_DRIFT`.

Users who materialize the optional environment receive the packages under
their upstream terms and should retain the notices supplied by those packages.

## Public literature

PMIDs, DOIs, bibliographic facts, and repository-authored summaries do not
license the underlying article text. The dated PubMed seed contains only
bibliographic metadata and an export-time availability flag; no abstract is
included. No publisher PDF or copyrighted full text is authorised for
publication through this repository.

## Added components of the drug-repurposing and analysis work

Added 2026-10-29 (IT8 P2 licence corrections; evidence and open items in
`disease-models/wwox/research/drug_repurposing/licence_corrections_it8_20261029.md`). The MIT
`LICENSE` does not cover any of the third-party content listed here. Not legal advice.

- **Public GEO series** (GSE156243, GSE126075, GSE215425, and GSE92742 for LINCS L1000). Only
  statistics and per-gene or per-signature values computed in this repository from the public
  deposits are committed, never the deposited matrices. NCBI states that it itself places no
  restriction on the use of data it holds and that submitters may claim rights it cannot grant
  (<https://www.ncbi.nlm.nih.gov/home/about/policies/>, read 2026-10-29); the GEO-specific
  disclaimer page could not be read. Cite the deposit and its paper when reusing a derived table:
  Samarasinghe et al., *EMBO Mol Med* 2021 (GSE156243, PMID 34268881); the GSE126075 and GSE215425
  papers are named in the analysis folders.
- **iLINCS / LINCS.** Signature metadata and census counts only. The iLINCS terms as read on
  2026-10-23 are recorded in `disease-models/wwox/research/drug_repurposing/ACKNOWLEDGEMENTS.md`
  (CC BY; cite Pilarczyk et al., *Nat Commun* 2022, 13:4678); the iLINCS about page read on
  2026-10-29 points to a terms page that was not readable. The LINCS data-policy page was not
  readable (script-rendered).
- **ClinicalTrials.gov raw API pages** (`clinical_census_20261020_raw/`, 7 files). Registrant-submitted
  study records, kept as raw evidence of the census. The ClinicalTrials.gov terms page is
  script-rendered and was not readable. NLM asks that its data be acknowledged with the phrase
  "Courtesy of the U.S. National Library of Medicine"
  (<https://www.nlm.nih.gov/databases/download/terms_and_conditions.html>, read 2026-10-29), and says
  that non-government content may be protected by copyright and that reusers must satisfy it
  (<https://www.nlm.nih.gov/web_policies.html>, read 2026-10-29). Courtesy of the U.S. National
  Library of Medicine. Do not republish the free-text fields of these pages as a corpus.
- **NCBI RefSeq record NM_016373.4** (`ptc_readthrough_it4_e1a_20261028/input_NM_016373.4.gb`).
  NCBI states that information created by or for the US government on its site is within the public
  domain and asks for acknowledgement of NLM (NCBI policies page, read 2026-10-29). Source: NCBI
  RefSeq, National Library of Medicine; the record was not altered.
- **PRISM and Drug Repurposing Hub.** Only source tags attached to a few compound-level lines of
  `join/cards.json`; no row or table from either resource is committed. DGIdb reports the Drug
  Repurposing Hub as CC BY 4.0 and PRISM as supplementary data of a copyrighted journal article
  (DGIdb service, read 2026-10-29); the Hub site itself could not be read (certificate error).
- **ChEMBL raw responses** (`lucas_clarke_followup_20261026/chembl_raw/`, 46 files, and the ChEMBL
  parts of the raw DGIdb/Monarch folders). Unmodified ChEMBL web-service output, CC BY-SA 3.0
  Unported (<https://chembl.gitbook.io/chembl-interface-documentation/about>, read 2026-10-29). Credit
  line required by ChEMBL: "ChEMBL data is from https://www.ebi.ac.uk/chembl/ - the version of ChEMBL
  is" the release named in each file or `catalog/cache_manifest.json`
  (<https://chembl.github.io/chembl-licensing/>, read 2026-10-29). Licence text:
  <https://creativecommons.org/licenses/by-sa/3.0/legalcode>; a copy is in
  `disease-models/wwox/research/drug_repurposing/view/shareable_package/LICENSES/CC-BY-SA-3.0.txt`.
  Anyone redistributing these files, or an adaptation, must keep that licence on them.
- **Raw DGIdb and Monarch KG responses** (`gse156243/kg_lookup/`, `lucas_clarke_followup_20261026/dgidb_raw/`).
  DGIdb is a container: its service reports a licence per source and none for itself (read 2026-10-29).
  The responses therefore carry rows under non-commercial or unclear terms (DTC CC BY-NC-SA 3.0, CKB-CORE
  CC BY-NC-SA 4.0, CGI CC BY-NC 4.0, TTD, OncoKB, COSMIC, MyCancerGenome and others, all as reported by
  DGIdb). They are research evidence only; they are not covered by the MIT licence and must not be
  reused commercially or redistributed. Their disposition is a reserved decision of the operator.
- **DGIdb claim-source table** (as reported by the DGIdb service on 2026-10-29): ChEMBL CC BY-SA 3.0;
  GuideToPharmacology CC BY-SA 4.0 (its own site: database ODbL, contents CC BY-SA 4.0); ClinPGx
  CC BY-SA 4.0; DTC CC BY-NC-SA 3.0; CKB-CORE CC BY-NC-SA 4.0; CGI CC BY-NC 4.0; CIViC CC0 1.0;
  DoCM CC BY 4.0; FDA and NCI "public domain" (NCI: see `DATA_SOURCES.md`); COSMIC free for
  non-commercial use only (its own licence page, read 2026-10-29: commercial R&D, products and
  clinical reporting need a commercial licence); OncoKB restrictive, non-commercial; MyCancerGenome
  restrictive, custom, non-commercial; TTD "unclear"; TdgClinicalTrial, TEND, TALC, HingoraniCasas and
  similar tables are supplementary tables of copyrighted publications.
- **OmniPath-derived network edge tables** (`network_comparison_it7_p3_20261029/inputs/`). Rows come
  from the OmniPath web service (<https://omnipathdb.org>) and carry, per row, the source resources and,
  in `resource_licences.tsv`, the licence label OmniPath gives each resource. Resource labels found there
  include CC BY 4.0, CC0 1.0, MIT, BSD, CC BY 2.5, **CC BY-SA 4.0 (TRRUST, KEGG-MEDICUS, PhosphoPoint)**,
  **CC BY-SA 3.0 (SignaLink3, Guide2Pharma, TFe, ARN)**, GPLv3 (CellChatDB, CellTalkDB, ICELLNET, LRdb),
  LGPLv3 (HTRIdb, RegNetwork, PAZAR, ORegAnno), CC BY-ND 3.0 (DIP), DSL (InnateDB), NAR Open Access (TRED,
  dbPTM), Informal, Artistic-2.0. TRRUST was confirmed at its own site on 2026-10-29: "freely available for
  both academic and commercial use under the Creative Commons Attribution-ShareAlike 4.0 International
  (CC BY-SA 4.0) license ... appropriate attribution ... adapted material is distributed under the same
  license" (<https://www.grnpedia.org/trrust/>). The other labels are OmniPath's, not read at the
  resources. No single licence describes either table: each row follows the resources it lists. Rows
  that list only CC BY / CC0 / MIT / BSD resources: 55,465 of 55,760 (SIGNOR table) and 36,959 of 51,621
  (CollecTRI table). Rows that list a share-alike resource but nothing incompatible: 156 and 7,117. Rows
  that list a resource with a GPL, LGPL, ND, DSL, NAR or informal label: 139 and 7,545; whether those rows
  can stay under any common label is open and is recorded in the corrections file. Attribution:
  "SIGNOR (CC BY 4.0) and the resources in resource_licences.tsv, via OmniPath (Turei et al.)".

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

# Data sources, provenance, and reuse terms

This file covers every shipped asset under `analysis/data/` and every external
source explicitly cited by the WWOX disease layer. Repository-authored
interpretations remain hypotheses or analyses; they do not change the licence or
epistemic status of source data. No protected-access GTEx data and no private
patient data are authorised for this public edition.

## Cited-source coverage matrix

`PUBLIC` means the cited material used here is publicly accessible under the
listed terms. `MIXED` means the upstream resource contains components governed
by different access or reuse regimes; only the explicitly public subset is
authorised here. `PRIVATE` is forbidden in this repository.

| Source cited by `disease-models/wwox/` | Licence / reuse basis | Source status | What this repository uses | Release status |
|---|---|---|---|---|
| NCBI PubMed / PubMed Central availability flag | Public bibliographic service; article and abstract rights remain with their respective rights holders | PUBLIC for identifiers and bibliographic facts; MIXED for linked article content | Dated Clipboard-derived seed with PMID, DOI, title, year, publication class and the export-time `Free PMC article` flag; no abstract or full text | COMPLETE for the shipped 2026-07-05 snapshot; exact upstream query was not retained, so it is not represented as systematic or exhaustive |
| AlphaFold Protein Structure Database | CC BY 4.0; DeepMind copyright and EMBL-EBI attribution | PUBLIC | AF-Q9NZC7-F1 and repository-authored derivatives | COMPLETE |
| NCBI ClinVar | Public download/API; ClinVar requests attribution to ClinVar and relevant submitters; NCBI disclaimer applies | PUBLIC | Public WWOX variant records and repository-authored derivatives | LEGACY PUBLIC-DERIVED: source release not embedded; not reproducible from the clone |
| GTEx Portal | Open-access aggregate data with GTEx acknowledgement; controlled-access donor-level data has separate access controls | MIXED | GTEx v8 aggregate tissue-expression values only; no protected data | LEGACY PUBLIC-DERIVED: endpoint and dataset known; original response not retained |
| Meta FAIR ESM-2 | MIT licence for the public repository containing code and pretrained weights | PUBLIC | Repository-generated zero-shot scores | LEGACY PUBLIC-DERIVED: exact original checkpoint/code commit unavailable; not reproducible from the clone |
| ThermoMPNN | MIT licence, Kuhlman Lab; primary paper DOI `10.1073/pnas.2314853121` | PUBLIC | Repository-generated saturation predictions | LEGACY PUBLIC-DERIVED: exact original checkpoint/code commit unavailable; not reproducible from the clone |
| Monarch Initiative / Monarch KG | Monarch application code is BSD-3-Clause; integrated KG records retain the terms of their named upstream sources | MIXED | Links, interoperability description, and public ontology/disease-level identifiers only; no Monarch KG dump is shipped | COMPLETE for citation-only use |
| DisMech | Repository declares BSD-3-Clause in `pyproject.toml`; no DisMech code or knowledge-base data is shipped here | PUBLIC | Link and interoperability/audit description only | COMPLETE for citation-only use; re-check licence holder text before any redistribution |

## Optional molecular-dynamics software

`environment-md.yml` reconstructs the last known working exploratory pilot
environment. It is optional and is not installed by the release CI. No package
source or binary is redistributed in this repository.

| Software | Pinned version | Licence / reuse basis | Status |
|---|---:|---|---|
| NumPy | 1.26.4 | BSD-3-Clause | PUBLIC dependency declaration only |
| OpenMM | 8.1.1 | Mixed by component: most source under MIT; CUDA/OpenCL platforms under LGPL | PUBLIC dependency declaration only |
| PDBFixer | 1.12 | MIT in the retained package metadata | PUBLIC dependency declaration only |
| MDTraj | 1.10.3 | LGPL-2.1-or-later; some subcomponents may carry their own compatible terms | PUBLIC dependency declaration only |

| Shipped paths | Source / derivation | Source scope | Retrieval / version | Reuse terms and required attribution |
|---|---|---|---|---|
| `analysis/data/WWOX_clinvar_*` | NCBI ClinVar public variant records, filtered to WWOX and transformed into tables/figures | PUBLIC | Local source table first materialized 2026-07-03 and entered the LEGEND ingest record 2026-07-04; exact ClinVar release was not embedded | ClinVar asks downstream users to attribute ClinVar and relevant submitters. ClinVar is not independently verified by NIH and is not for direct diagnostic use without genetics-professional review. |
| `analysis/data/WWOX_disease_association.png` | Repository-authored visual synthesis from public ClinVar/literature-level disease associations | PUBLIC-DERIVED | 2026-07-04 analysis | Repository licence applies to the original visual arrangement; underlying facts retain source attribution requirements. |
| `analysis/data/WWOX_Q9NZC7_AlphaFold.pdb` | AlphaFold Protein Structure Database prediction for human WWOX, UniProt Q9NZC7 | PUBLIC | AlphaFold DB model AF-Q9NZC7-F1; retrieved before 2026-07-04 | AlphaFold DB data: CC BY 4.0; copyright DeepMind Technologies Limited. Cite AlphaFold DB and the AlphaFold methods paper. Prediction only, not an experimental structure. |
| `analysis/data/redteam/AF_SDR.pdb` | Repository-authored extraction of the WWOX SDR region from the AlphaFold DB model above | PUBLIC-DERIVED | 2026-07-13 red-team package | Derivative of AlphaFold DB data, therefore CC BY 4.0 attribution remains required. |
| `analysis/data/WWOX_ESM2_Q230_scores.json` | Repository-generated zero-shot sequence scores using Meta FAIR ESM-2 (650M family) | PUBLIC-DERIVED | Local artifact first materialized 2026-07-04 12:49 CEST. Legacy artifact: exact original package commit/checkpoint was not retained; the clone does not claim to reproduce it. | ESM source code is MIT-licensed. Cite the ESM-2 repository and model paper. Scores are predictions, not experimental measurements. |
| `analysis/data/WWOX_ThermoMPNN_saturation.csv` | Repository-generated WWOX saturation stability predictions using ThermoMPNN | PUBLIC-DERIVED | Local artifact first materialized 2026-07-04 12:49 CEST; canonical project confirmed as Kuhlman-Lab/ThermoMPNN. Legacy artifact: exact original commit/model checkpoint was not retained; the clone does not claim to reproduce it. | ThermoMPNN code and repository weights are MIT-licensed (Copyright 2023 Kuhlman-Lab). Cite Dieckhaus et al., PNAS 2024, DOI `10.1073/pnas.2314853121`. Predictions are not experimental ΔΔG measurements. |
| `analysis/data/WWOX_Q230P_ddG_crosscheck.png` | Repository-authored comparison of computational predictions | PUBLIC-DERIVED | 2026-07-04 analysis | Repository licence for the plot; underlying AlphaFold/ESM-2/ThermoMPNN attribution remains required. |
| `analysis/data/WWOX_Q230P_structural_impact.png` | Repository-authored visualization of the Q230P structural context in the AlphaFold DB WWOX model | PUBLIC-DERIVED | 2026-07-04 analysis | Repository licence for the plot; AlphaFold DB CC BY 4.0 attribution remains required. Computational interpretation only. |
| `analysis/data/WWOX_SDR_ddG_map.png` | Repository-authored visualization of ThermoMPNN saturation predictions | PUBLIC-DERIVED | 2026-07-04 analysis | Repository licence for the plot; ThermoMPNN citation and terms remain required. |
| `analysis/data/WWOX_Q230P_residue_context.csv` | Repository-derived geometric/context measurements from the AlphaFold DB WWOX model | PUBLIC-DERIVED | 2026-07-10 analysis | CC BY 4.0 attribution to AlphaFold DB remains required; derived values are computational. |
| `analysis/data/WWOX_residue_rescuability.csv` | Repository-authored heuristic table derived from public structural/variant data | PUBLIC-DERIVED | 2026-07-04 analysis | Repository licence; heuristic status must remain explicit and must not be presented as validated clinical prediction. |
| `analysis/data/WWOX_pathogenic_missense_classified.csv` | Repository-derived classification from ClinVar plus computational annotations | PUBLIC-DERIVED | 2026-07-04 analysis | Attribute ClinVar and computational tools; classifications are research annotations, not clinical assertions. |
| `analysis/data/WWOX_protein_variant_map.png` | Repository-authored visualization from public variant/domain data | PUBLIC-DERIVED | 2026-07-04 analysis | Repository licence for visual arrangement; underlying ClinVar/UniProt attribution remains required. |
| `analysis/data/WWOX_proteostasis_hypothesis.png` | Repository-authored hypothesis visualization based on public literature and computational analyses | PUBLIC-DERIVED | 2026-07-04 analysis | Repository licence; explicitly a hypothesis, not measured mechanism. |
| `analysis/data/WWOX_therapy_levers.csv` | Repository-authored extraction/synthesis from cited public peer-reviewed literature | PUBLIC-DERIVED | 2026-07-04 analysis | Facts and bibliographic metadata are attributed by PMID/DOI; no copied full-text is licensed by this repository. |
| `analysis/data/WWOX_therapy_map.png` | Repository-authored visualization derived from the therapy-levers table | PUBLIC-DERIVED | 2026-07-04 analysis | Repository licence for original visual arrangement; retain paper citations. |
| `analysis/data/WWOX_tissue_expression_GTEx.csv` | Aggregated WWOX tissue-expression values from the open-access GTEx Portal | PUBLIC-DERIVED | GTEx Portal API v2, `datasetId=gtex_v8`, gene `ENSG00000186153.16`; local table first materialized 2026-07-03 21:44 CEST | GTEx open-access data may be used with acknowledgement. Acknowledge the GTEx Portal and access date/release. No raw sequence or protected donor metadata is included. |
| `analysis/data/WWOX_tissue_expression_GTEx.png` | Repository-authored visualization of the aggregated GTEx table | PUBLIC-DERIVED | GTEx v8 analysis; generated before 2026-07-04 | Repository licence for visual arrangement; GTEx acknowledgement remains required. |
| `analysis/data/WWOX_biomarker_proxy_validity.csv` | Repository-authored rubric combining GTEx expression with methodological judgement | PUBLIC-DERIVED | 2026-07-04 analysis | Repository licence; proxy scores are analytical judgements, not validated biomarker performance. |
| `analysis/data/redteam/*` | Repository-authored adversarial review package; numerical tables and figures derive from the public AlphaFold model and cited public literature | PUBLIC-DERIVED | 2026-07-13 to 2026-07-14 | Repository licence for original text/tables/figures; AlphaFold DB CC BY 4.0 attribution and paper citations remain required. |
| `analysis/data/WWOX_WOREE_phenotypic_neighbors.tsv` | Repository-generated phenotypic-similarity ranking of diseases nearest to WOREE (OMIM:616211), computed with `scripts/phenotypic_neighbors.py` from public HPO annotations (`phenotype.hpoa`) and the HPO `hp.obo` is_a graph | PUBLIC-DERIVED | HPO `phenotype.hpoa` and `hp.obo` retrieved 2026-07-23; analysis generated 2026-07-23 | Human Phenotype Ontology data are free to use with attribution to the HPO project (CC BY 4.0). Cite the HPO. Scores are computational research prioritisation, not clinical predictions. |
| `analysis/data/WWOX_layer9_maxo_crosswalk.tsv` | Repository-authored crosswalk of WWOX therapeutic-modality classes to Medical Action Ontology (MAXO) terms, each MAXO id verified against a local MAXO release | PUBLIC-DERIVED | MAXO release retrieved 2026-07-23 | MAXO is distributed under CC BY 4.0; cite MAXO / the OBO Foundry. The modality→action mapping is an analytical annotation, not a validated treatment recommendation. |

## Artifact integrity anchors

The following SHA-256 values were verified on 2026-07-25 against the original
local analysis artifacts. They prove byte identity between the retained source
copy and this staging copy; they do **not** reconstruct an omitted upstream
release, software commit, model checkpoint, or generation command.

| Shipped artifact | SHA-256 |
|---|---|
| `analysis/data/WWOX_clinvar_all_variants.csv` | `09c8cbbbb7d36031cc103584de7519ac1d59d83f630790864de1c91b5d478884` |
| `analysis/data/WWOX_tissue_expression_GTEx.csv` | `e6edd367e9aefc30be092602462de6ae708d7e1a0a28c0ae592d52633ca0a8f8` |
| `analysis/data/WWOX_ESM2_Q230_scores.json` | `e97a22231d4e37f0d572ffa23eacb1b52ff8a6596fd4302cdeb3453b5e3eb908` |
| `analysis/data/WWOX_ThermoMPNN_saturation.csv` | `0716f7e39511978a7a695c7f9d5bbb7d15d5b37714cedf784027e1aeaa870ca1` |

## Authoritative source pages

- PubMed overview and NLM copyright guidance:
  <https://pubmed.ncbi.nlm.nih.gov/about/> ·
  <https://www.nlm.nih.gov/web_policies.html>
- ClinVar access, attribution request, and disclaimer:
  <https://www.ncbi.nlm.nih.gov/clinvar/docs/maintenance_use/>
- AlphaFold DB licence and disclaimer:
  <https://alphafold.ebi.ac.uk/assets/License-Disclaimer.pdf>
- GTEx open-access downloads and acknowledgement:
  <https://gtexportal.org/home/downloads/adult-gtex/overview>
- Meta FAIR ESM repository and licence:
  <https://github.com/facebookresearch/esm>
- ThermoMPNN repository (MIT) and primary paper:
  <https://github.com/Kuhlman-Lab/ThermoMPNN> ·
  <https://doi.org/10.1073/pnas.2314853121>
- Monarch Initiative terms and source-specific licensing:
  <https://monarchinitiative.org/kg/terms>
- DisMech repository (declared BSD-3-Clause):
  <https://github.com/monarch-initiative/dismech>
- UniProt WWOX Q9NZC7 entry:
  <https://www.uniprot.org/uniprotkb/Q9NZC7/entry>
- Human Phenotype Ontology (annotations, ontology, licence):
  <https://hpo.jax.org/> · annotations <https://purl.obolibrary.org/obo/hp/hpoa/phenotype.hpoa> · ontology <https://purl.obolibrary.org/obo/hp.obo>
- Medical Action Ontology (MAXO), CC BY 4.0:
  <https://github.com/monarch-initiative/MAxO> · <https://purl.obolibrary.org/obo/maxo.owl>
- MONDO Disease Ontology, CC BY 4.0:
  <https://mondo.monarchinitiative.org/>

## Known reproducibility limitations

The original execution environment was not retained. The exact ClinVar release,
GTEx response timestamp, ESM-2 code/checkpoint, ThermoMPNN code/checkpoint, and
generation scripts cannot be reconstructed from the surviving files or session
records. This repository therefore ships those outputs as integrity-anchored
legacy public derivatives, **not** as clean-clone-reproducible analyses.

They may be inspected as worked examples, but numerical reproduction requires
a new, independently versioned run. A future rerun must be published as a new
artifact with pinned source releases, commits, checkpoint hashes, environment,
command, and output checksum; it must not silently overwrite these legacy
artifacts.

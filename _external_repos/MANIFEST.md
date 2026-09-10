# External computational workshop manifest

This public repository does **not** vendor or redistribute third-party
repositories. The private `_external_repos/medical_ai/` workshop is replaced by
this manifest so that routing remains auditable without copying external code,
weights, datasets, credentials, or patient information.

## Inclusion contract

Every future entry must record:

- canonical repository URL;
- pinned commit or release;
- licence and commercial-use constraints;
- capability supplied to LEGEND;
- expected inputs and outputs;
- compute/network/API requirements;
- privacy boundary;
- validation status: `DESCRIBED`, `AUDITED`, `REPRODUCED`, or `REJECTED`;
- minimum reproducible invocation;
- known failure modes.

No entry is evidence by itself. Outputs enter LEGEND only as
`IPOTESI`/`ESPANSIONE` until independently validated.

## Current routing inventory

| Capability | Candidate project/resource | Public location | Runtime class | Privacy rule | Status |
|---|---|---|---|---|---|
| Local cited literature QA | PaperQA | <https://github.com/Future-House/paper-qa> | Local Python; may require configured model/provider | Public papers only; never patient material | DESCRIBED |
| Drug/target knowledge graph | PrimeKG | <https://github.com/mims-harvard/PrimeKG> | Local data/queries; large download | Disease/gene queries only | DESCRIBED |
| Drug repurposing graph model | TxGNN | <https://github.com/mims-harvard/TxGNN> | Heavy local ML/data | Public disease/gene context only | DESCRIBED |
| Drug repurposing graph | DRKG | <https://github.com/gnn4dr/DRKG> | Large local graph | Public entities only | DESCRIBED |
| ADMET prediction | ADMET-AI | <https://github.com/swansonk14/admet_ai> | Local Python/model weights | Molecule identifiers only | DESCRIBED |
| Medicinal-chemistry alerts | medchem | <https://github.com/datamol-io/medchem> | Local Python | Molecule identifiers only | DESCRIBED |
| Protein language model | ESM / ESM-2 | <https://github.com/facebookresearch/esm> | Local model; potentially GPU-heavy | Public protein sequence only | DESCRIBED |
| Protein stability prediction | ThermoMPNN | <https://github.com/Kuhlman-Lab/ThermoMPNN> (MIT; canonical project verified, original-run commit/checkpoint unavailable) | Local ML | Public protein sequence/structure only | LEGACY_UNREPRODUCIBLE |
| Protein structure source | AlphaFold DB | <https://alphafold.ebi.ac.uk/> | Public download | Public accession only | DESCRIBED |
| Variant archive | ClinVar | <https://www.ncbi.nlm.nih.gov/clinvar/> | Public API/download | Variant-level public records only | DESCRIBED |
| Tissue expression | GTEx Portal | <https://gtexportal.org/> | Open aggregate download | Open-access aggregates only; never protected donor data | DESCRIBED |
| Ontology access | OAK / oaklib | <https://github.com/INCATools/ontology-access-kit> | Local Python/ontology downloads | Public ontology terms only | REPRODUCED |
| Phenotypic semantic similarity | semsimian | <https://github.com/monarch-initiative/semsimian> | Local Rust+Python; offline | Public disease/phenotype terms only | REPRODUCED |
| Medical action ontology | MAXO | <https://github.com/monarch-initiative/MAxO> | Public ontology download (CC BY 4.0) | Public action terms only | REPRODUCED |
| Disease ontology | MONDO | <https://mondo.monarchinitiative.org/> | Public ontology download (CC BY 4.0) | Public disease terms only | REPRODUCED |
| Phenotype ontology + annotations | HPO / phenotype.hpoa | <https://hpo.jax.org/> | Public download | Public disease-level annotations only | REPRODUCED |
| Mechanistic disease models | DisMech | <https://github.com/monarch-initiative/dismech> | Local/public knowledge base | Public disease-level models only | AUDITED |
| Disciplined development workflows | Superpowers plugin for Claude | <https://claude.com/plugins/superpowers> | Optional Claude Code plugin; external install | Public repository context only; never private overlays or credentials | DESCRIBED |

## Complete operational routing inventory

This table closes the private-to-public routing gap without redistributing any
third-party repository. A pin records the exact private audit snapshot when one
was available; it does **not** claim that a clean public clone can run the
project. `UNPINNED` and `NO LICENCE FILE` are deliberate fail-closed states:
audit them before installation or use.

All routes accept public gene, disease, paper, sequence, structure, molecule or
ontology inputs only. They must never receive clinical records, family
relationships, local private prompts or unpublished sample data.

| Tool/resource | Capability routed by LEGEND | Canonical location | Audited pin | Licence/constraint | Runtime | Status |
|---|---|---|---|---|---|---|
| PaperQA | cited full-text QA and contradiction checks | <https://github.com/Future-House/paper-qa> | `d7675d7b7ed` | Apache-2.0 | Python; model provider may be required | AUDITED |
| ADMET-AI | ADMET prediction | <https://github.com/swansonk14/admet_ai> | `c65bf0418e19` | MIT | Python/model weights; CPU | DESCRIBED |
| medchem | PAINS/NIBR and medicinal-chemistry alerts | <https://github.com/datamol-io/medchem> | UNPINNED | VERIFY UPSTREAM BEFORE USE | Python; CPU | DESCRIBED |
| PrimeKG | multiscale gene–drug–disease KG | <https://github.com/mims-harvard/PrimeKG> | UNPINNED | VERIFY CODE AND DATA LICENCES | large public graph | DESCRIBED |
| Biopython | sequence and identifier utilities | <https://github.com/biopython/biopython> | UNPINNED | BSD-3-Clause; verify current release | Python; CPU | DESCRIBED |
| BioServices | public biological web-service clients | <https://github.com/cokelaer/bioservices> | UNPINNED | VERIFY UPSTREAM BEFORE USE | Python; network APIs | DESCRIBED |
| `kg_thin_slice.py` | Monarch neighbours plus DGIdb drug lookup | bundled under `legend-hypothesis-forge/scripts/` | BUNDLED | repository licence; Monarch/DGIdb terms also apply | stdlib; public APIs | REPRODUCED |
| TxGNN | zero-shot drug repurposing | <https://github.com/mims-harvard/TxGNN> | `0e0203c3939f` | MIT; underlying data terms also apply | heavy ML/data | DESCRIBED |
| repuragent | agentic drug repurposing | <https://github.com/pharmbio/repuragent> | `7873de064aca` | NO LICENCE FILE FOUND — DO NOT USE UNTIL RESOLVED | Python/services | REJECTED |
| DRKG | drug-repurposing knowledge graph | <https://github.com/gnn4dr/DRKG> | `d4bb19743120` | Apache-2.0; data terms also apply | large graph/ML | DESCRIBED |
| RTX | NCATS ARAX path reasoning | <https://github.com/RTXteam/RTX> | `4dd0aaa26147` | MIT; API/data terms also apply | service/big data | DESCRIBED |
| RTX-KG2 | NCATS KG2 access/build layer | <https://github.com/RTXteam/RTX-KG2> | `72155f6a4f52` | MIT; source-data terms also apply | big data | DESCRIBED |
| MATRIX | systematic repurposing pipeline | <https://github.com/everycure-org/matrix> | `e22099a1ee39` | Apache-2.0; source-data terms also apply | heavy data/ML | DESCRIBED |
| DrugRepurposing | legacy RDF2Vec/XGBoost repurposing workflow | <https://github.com/carmenreep/DrugRepurposing> | `3ecf4c407b17` | NO LICENCE FILE FOUND — DO NOT USE UNTIL RESOLVED | obsolete dependencies; 12–20 h modern analogue | REJECTED |
| BioCypher | biomedical mini-KG construction | <https://github.com/biocypher/biocypher> | `35cce71ccffa` | Apache-2.0 | Python/graph backend | DESCRIBED |
| BioChatter | LLM/RAG interface over biomedical KGs | <https://github.com/biocypher/biochatter> | `917f4c38acb5` | Apache-2.0; model-provider terms may apply | Python/model provider | DESCRIBED |
| ASOptimizer | ASO chemistry prior | <https://github.com/Spidercores/ASOptimizer> | `c7716f223fa4` | NO LICENCE FILE FOUND — DO NOT USE UNTIL RESOLVED | Python/ML | REJECTED |
| openASO | ASO target-accessibility features | <https://github.com/lackeylela/openASO> | `20dddb35f226` | BSD-3-Clause | Python/data dependencies | DESCRIBED |
| spectrum-drug-tracker | monogenic-DEE trial drugs and endpoints | <https://github.com/simonsfoundation/spectrum-drug-tracker> | `200238a6c692` | MIT; source-data terms also apply | local CSV | AUDITED |
| REPRESS | miRNA-site repression prediction | <https://github.com/deepgenomics/REPRESS> | `40d2a1c2dae0` | CC BY-NC 4.0; non-commercial only | GPU | DESCRIBED |
| AAV capsid receptor | capsid/receptor and tropism modelling | <https://github.com/vector-engineering/AAV_capsid_receptor> | `ef7be7b4df25` | BSD-3-Clause | ML/GPU | DESCRIBED |
| Fit4Function | AAV sequence-to-function modelling | <https://github.com/vector-engineering/fit4function> | `6bfc2ebfe4ab` | BSD-3-Clause | ML/GPU | DESCRIBED |
| RFdiffusion | protein/binder generation | <https://github.com/RosettaCommons/RFdiffusion> | `2d0c003df46b` | BSD; model-weight terms must also be checked | GPU | DESCRIBED |
| BindCraft | protein binder design | <https://github.com/martinpacesa/BindCraft> | `b971db42ba6e` | MIT; dependent model terms also apply | GPU | DESCRIBED |
| LigandMPNN | ligand-aware protein sequence design | <https://github.com/dauparas/LigandMPNN> | `26ec57ac976a` | MIT; model-weight terms also apply | GPU | DESCRIBED |
| BoltzGen | generative biomolecular design | <https://github.com/HannesStark/boltzgen> | `a3149cf18eeb` | MIT; model/data terms also apply | GPU | DESCRIBED |
| crisprDesign | CRISPR guide design | <https://github.com/crisprVerse/crisprDesign> | `60039dc1e30a` | permissive Genentech licence; verify notice | R/Bioconductor | DESCRIBED |
| PEGG | prime-editing guide design | <https://github.com/samgould2/PEGG> | `a170fd13c465` | MIT | Python; CPU | DESCRIBED |
| PrimeDesign | prime-editing design | <https://github.com/pinellolab/PrimeDesign> | `e4fdb31c81cc` | dual licence: AGPL-3.0 for academic research; commercial terms separate | Python/web | DESCRIBED |
| off-target prediction | CRISPR off-target prediction | <https://github.com/MichaelLinn/off_target_prediction> | `c9e028b51951` | NO LICENCE FILE FOUND — DO NOT USE UNTIL RESOLVED | Python/ML | REJECTED |
| Robin | multi-agent scientific discovery | <https://github.com/Future-House/robin> | `4a5cce310f3b` | Apache-2.0; model-provider terms may apply | agents/APIs | DESCRIBED |
| Open AI Co-Scientist | generate–critique–rank–evolve loop | <https://github.com/llnl/open-ai-co-scientist> | `eff5b2982b6b` | MIT; model-provider terms may apply | agents/APIs | DESCRIBED |
| Hypothesis Generation | HypoGeniC/HypoRefine workflows | <https://github.com/ChicagoHAI/hypothesis-generation> | `bd37a3129a2f` | MIT; model-provider terms may apply | agents/APIs | DESCRIBED |
| Biomni | general biomedical agent | <https://github.com/snap-stanford/Biomni> | `400c1f366b96` | mixed datasets; several non-commercial/proprietary sources | heavy data/agents | DESCRIBED |
| BioDiscoveryAgent | experiment and perturbation ideation | <https://github.com/snap-stanford/BioDiscoveryAgent> | `19673c7371c5` | MIT; source-data/model-provider terms also apply | agents/APIs | DESCRIBED |
| MEDEA | omics agent for target and drug-response discovery | <https://github.com/mims-harvard/MEDEA> | `b4ff6cb24fea` | Apache-2.0; source-data/model-provider terms also apply | agents/omics data | DESCRIBED |
| Superpowers plugin | brainstorming, TDD, systematic debugging and code-review workflow | <https://claude.com/plugins/superpowers> · <https://github.com/anthropics/claude-plugins-official> | UNPINNED | Marketplace directory delegates licensing to each linked plugin; verify the installed plugin licence/version before use or redistribution | optional Claude Code plugin | DESCRIBED |
| Retraction Watch database (Crossref-hosted) | dependency-integrity screening of a paper's REFERENCE LIST, not only the paper itself | <https://api.labs.crossref.org/data/retractionwatch> | `sha256 8ff64393b342e18ec2c04b06d54dba834e37e77575913c97fa93c8da41dde3d5` (72,476 rows, 66,609,820 bytes, fetched 2026-09-10; pin at `framework/config/retraction_watch_pin.json`) | CC0 asserted by Crossref for the dataset but NOT verified in this run — the endpoint sends no licence header and `api.labs.crossref.org/openapi.json` declares MIT for the API SOFTWARE, which is a different thing; verify before any redistribution of the rows | stdlib Python, one key-less HTTP GET, no email sent, zero spend | AUDITED |

### Reproduced routes — minimum invocation & audit notes

- **OAK + HPO/MONDO/MAXO ontologies** — reproduced offline 2026-07-23. `pip install oaklib`; ontology terms resolved locally via `runoak -i sqlite:obo:mondo …` (public sqlite cache). Verified WWOX disease coverage in MONDO: `MONDO:0014533` (WOREE) and `MONDO:0013687` (SCAR12). No network calls carry any non-public data; remote OAK backends (OLS/BioPortal) are left unconfigured by policy.
- **semsimian (phenotypic similarity)** — reproduced offline 2026-07-23 as the dependency-free `scripts/phenotypic_neighbors.py` (same Resnik/phenodigm score family). Minimum invocation and unit tests are documented in `../disease-models/wwox/analysis/phenotypic_neighbors.md`. Public HPO annotations only; runs with no network access after the two public files are fetched.
- **DisMech** — audited (read-only) 2026-07-22: LinkML schema, BSD-3-Clause, PR-based curation; the WWOX/WOREE/SCAR12 disorder is absent from its knowledge base (a candidate public contribution). Not vendored here.
- **ThermoMPNN** — canonical repository and MIT licence verified 2026-07-25; upstream HEAD observed as `2b04fd370e399911b1fa5848112cc9013f084110`, but this is **not evidence** that the shipped WWOX table used that commit. The table is retained as an integrity-anchored, non-reproducible legacy derivative; any future rerun must receive new pinned provenance.
- **Retraction Watch database (Crossref-hosted)** — audited and run 2026-09-10 by `plan` under `HARNESS-DEPINTEG-001`. Minimum invocation: `python3 framework/scripts/dependency_integrity.py fetch` then `pin --write`, then `control` (positive control: PMID 16223882 / `10.1073/pnas.0505485102` must return `Expression of concern`, retraction PMID `28373548`, with a `Reason` naming image duplication/error), then `corpus --json <out>`. Smoke test: `framework/scripts/test_dependency_integrity.py` (60 assertions incl. a 14-mutation battery, 14/14 caught). **Licence NOT verified**, which is why this route is `AUDITED` and not `REPRODUCED`: the repository's own rule requires licence verification for `REPRODUCED`, and neither the endpoint nor the Crossref documentation page served a machine-readable dataset licence in this run. **Known failure modes** (all nine declared in the tool's docstring): DOI-less references are invisible (346 of 4,341 corpus reference DOIs, 8.0%) and are reported `UNSCREENABLE_NO_DOI`, never clean; a paper whose publisher deposited no reference list, or none carrying a DOI, is `UNSCREENABLE_NO_REFERENCE_LIST` / `UNSCREENABLE_NO_SCREENABLE_REFERENCES`, never clean; `RetractionNature` carries five values, not three, and `Correction` and `Reinstatement` are NOT integrity flags; a DOI may carry several rows and all are retained; **the `Reason` field's semantics still need one adjudicated run and are passed through verbatim, never parsed — this is the one inclusion-contract item that remains open**; the snapshot goes stale (72,450 rows on 2026-09-09, 72,476 on 2026-09-10) so `days_since_fetch` accompanies every verdict; 218 rows carry no nature AND no DOI, so they are unreachable by this method entirely. The screen emits a report and a review queue only: it writes to no registry, no dossier and none of the four scientific current files, and a flag is a prompt to read, never a claim about the citing paper.

## Deliberately not redistributed

- cloned third-party source trees;
- model checkpoints and large datasets unless their licence expressly permits
  redistribution and attribution is complete;
- package environments and caches;
- API keys or paid-service configuration;
- private clinical records, private prompts, private full texts, or generated
  derivatives carrying case linkage.

## Reproduction status

`DESCRIBED` means the route is documented, not that a clean clone can execute
it. A project may be advertised as runnable only after it reaches `REPRODUCED`
with a pinned version, licence verification, and a smoke test.

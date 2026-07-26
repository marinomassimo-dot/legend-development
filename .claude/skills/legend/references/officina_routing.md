# Workshop `_external_repos/medical_ai/` — routing table

How and when the autopilot invokes the external repos. Golden rule: **the workshop is never run in bulk**; each tool is a back-end a skill invokes to answer a precise question. Output is **always `IPOTESI`/`ESPANSIONE`**, never auto-canonical → it goes through the pipeline. On **first use** each tool is installed in an out-of-repo venv (as already done for paper-qa). If a GPU or a paid service is needed → **do not force it**: flag the gap to `legend-capability-scout` and use the local alternative. (No third-party repos are shipped in the public edition; see `_external_repos/MANIFEST.md`.)

## Readiness legend
- 🟢 **ready** (installed/tested, local, free)
- 🟡 **wireable** on first use (pip, CPU, free)
- 🔴 **heavy** (GPU / big-data / long setup) — on-demand, one-off

## Routing by question / phase

| Operational question | Workshop tool | Skill that invokes it | Phase | Readiness |
|---|---|---|---|---|
| What do the full texts say? (cited RAG, contradictions) | `paper-qa` | `legend-paperqa` | 3 | 🟢 |
| Is this molecule druggable/safe? ADMET, BBB | `admet_ai` | `legend-safety-triage` | 4 | 🟡 |
| Drug-likeness/CNS filters, PAINS/NIBR alerts | `medchem` | `legend-safety-triage` | 4 | 🟡 |
| Multiscale KG query (gene-drug-disease-phenotype) | PrimeKG (skill `primekg`) | `legend-hypothesis-forge` | 4 | 🟡 |
| Sequence/variant/annotation lookup | `biopython`,`bioservices` | `aso-designer`/`deepdive` | 3–4 | 🟡 |
| **Who are WWOX's druggable neighbours?** (1-hop Monarch + DGIdb, no ML) | `kg_thin_slice.py` | `legend-hypothesis-forge` | 4 | 🟢 |
| Drug-repurposing candidates + explanations | `TxGNN`,`repuragent` | `legend-hypothesis-forge` | 4 | 🔴 |
| Repurposing via knowledge graph / path reasoning | `DRKG`,`RTX`,`RTX-KG2`,`matrix` | `legend-hypothesis-forge` | 4 | 🔴 |
| Repurposing KG + embedding + ML end-to-end on OMIM seed | `DrugRepurposing` (Bianchi 2025) | `legend-hypothesis-forge` | 4 | 🔴† |
| Build a mini WWOX KG | `biocypher`+`biochatter` | `legend-discovery` | 3 | 🔴 |
| Optimize ASO chemistry (modifications) | `ASOptimizer` | `legend-aso-designer` | 4 | 🔴 |
| ASO target-accessibility features | `openASO` | `legend-aso-designer` | 4 | 🟡 |
| **What has already been tried in monogenic DEEs?** (71 Rett/FXS/TSC/Angelman trials: drugs + endpoints) | `spectrum-drug-tracker` (CSV, Simons) | `legend-hypothesis-forge` / endpoint | 3 | 🟢 |
| miRNA binding sites / mRNA degradation → **3'UTR target-site blocker** | `REPRESS` (Deep Genomics) | `legend-aso-designer` | 4 | 🔴‡ |
| AAV capsid design/evaluation for CNS | `AAV_capsid_receptor`,`fit4function` | `legend-hypothesis-forge` (GT lever) | 4 | 🔴 |
| Protein/binder design | `RFdiffusion`,`BindCraft`,`LigandMPNN`,`boltzgen` | on-demand | 4 | 🔴 |
| CRISPR guides/design, off-target | `crisprDesign`,`PEGG`,`PrimeDesign`,`off_target_prediction` | on-demand | 4 | 🔴 |
| Hypothesis generation/critique (co-scientist) | `robin`,`open-ai-co-scientist`,`hypothesis-generation` | `legend-hypothesis-forge` (method) | 4 | 🟡* |
| General biomedical agent / experiments | `Biomni`,`BioDiscoveryAgent`,`MEDEA` | on-demand | 4 | 🔴 |

\* the co-scientists are already **distilled as method** inside `legend-hypothesis-forge`; the repo is needed only to run the original implementation (often requires an API key → check the payment rule).

‡ `REPRESS` is **CC BY-NC** (research use ok, commercial no) and needs a GPU. Cloned 2026-07-11 as an **audit, not executed**. It answers one question: *which miRNA sites repress the WWOX 3'UTR?* — because blocking them with an ASO **de-represses the missense allele (Q230P), the one that still produces protein**, instead of correcting splicing. ⚠️ Mandatory gate **before** any design: if Q230P is **dominant-negative**, raising its dose makes things worse. Do not invoke until that gate is instructed.

† `_external_repos/medical_ai/DrugRepurposing` is the **legacy 2023 version** (MSc thesis: RDF2Vec + XGBoost + Flask), whose requirements no longer install (`sklearn==1.1.1`, `pandas==1.0.5`, `flask==1.1.2`). The active upstream (Bianchi, MIT, last release Nov-2025) is rewritten with Node2vec + PyG/GNN + docker-compose and **needs 12-20 h per run**. Do not re-clone or run without a precise reason: the value of its steps 1-2 is already captured, at zero cost, by `kg_thin_slice.py`. The full pipeline is justified only when the *prediction of absent drug-gene edges* is needed (the real ML delta), not the inventory of existing ones.

## `kg_thin_slice.py` — ready command

```bash
python3 .claude/skills/legend-hypothesis-forge/scripts/kg_thin_slice.py WWOX
```

Stdlib-only, no venv, no API key, no case data leaving (only the gene symbol travels). Returns WWOX's neighbours in the Monarch KG and which already have known drugs in DGIdb.

⚠️ **Known limit (degree bias):** ordering is by number of interactions, so promiscuous hubs (TP53, MAPK1) rise to the top despite being non-specific. Read the signal **by biological plausibility on the disease axes**, never by count. A neighbour with 3 drugs on the right axis is worth more than a hub with 400.

## First-wiring procedure (one-off, for any 🟡/🔴 tool)
1. isolated venv **outside the repo** (e.g. `~/.legend-venvs/<tool>/` with `uv`).
2. Install the repo's requirements; if it asks for GPU/paid service → **stop and flag**.
3. Write a small `run_local.py` exposing the useful function with simple I/O (SMILES, PMID, gene…), all local.
4. Update the reference of the skill that uses it with the ready command (as for `legend-paperqa`).
5. Record the new wiring in the capability scout log (Phase 7).

## Safety/cost note
No workshop tool may introduce paid traffic without the operator's explicit ok. Many agents (STELLA, some co-scientists) assume paid remote LLMs: **always prefer the local backend** or flag the gap instead of proceeding.

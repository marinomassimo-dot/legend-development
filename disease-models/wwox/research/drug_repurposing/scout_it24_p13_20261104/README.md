# IT24 P13: targeted scouting, four named gaps (2026-11-04)

Non-canonical. Not medical advice. Zero spend; no registration, login or contact; no e-mail address sent anywhere
(only compound names went to one public read endpoint). Nothing installed, nothing cloned, no third-party raw data
imported. Reuses the existing radar and the IT23 evaluations (EC-KG, NORDic, CANDO, dseqr, nf-core/diseasemodulediscovery,
MolNexus are not repeated). WWOX was not used as a search filter. Table: `candidates.tsv`.

## Gaps and what LEGEND already holds

| Gap | Already held (checked first) |
|---|---|
| G1 measured compound-target actions, kinase/HDAC/sirtuin/caspase | ChEMBL mechanism and activity, GtoPdb, DrugCentral, Pharos, BindingDB (discarded in IT8 P6), DGIdb (single listings) |
| G2 DGIdb-only names to InChIKey, offline | GtoPdb, ChEMBL, UniChem cache (`catalog/cache/unichem`: src1src2, src1src7, src1src14 = DrugBank, ChEBI, UNII) |
| G3 neural/glial perturbation or cell-typed drug signatures | iLINCS NPC knockdown set (IT21 P6): 4 of 23 panel genes have an NPC signature |
| G4 benchmark with controls / sign test | IT23 sign-discordance audit on the EC-KG extract; no external signed benchmark |

## Resources (verdicts)

| Id | Gap | Resource and revision | Licence read | Verdict |
|---|---|---|---|---|
| P13-1 | G2 | NCATS G-SRS public API, name to UNII, then cached UniChem UNII to ChEMBL | no licence sentence on the Inxight download/about pages; public-domain wording only from a search summary | **TRIAL** |
| P13-2 | G4, G1 sign | SIGMA-KG / FLASH, Zenodo 23874071 (2026-11-02; same content as 20693603 of 2026-05-11); bioRxiv 10.64898/2026.04.29.721775 | container CC BY 4.0; sources (LINCS, SIDER, DrugBank DDI, others) keep their own terms | **TRIAL** (data only) |
| P13-3 | G3 | scPerturb v1.4, Zenodo 13350497, includes Tian/Kampmann iPSC-neuron CRISPRi and CRISPRa h5ad | CC BY 4.0 | **TRIAL** (metadata only) |
| P13-4 | G3 | hiPSC neural-progenitor drug screen, 135 drugs, 4,320 signatures, GEO GSE119275/GSE119290 (Nat Commun 2018) | article CC BY 4.0; GEO terms not read | **TRIAL** (name overlap first) |
| P13-5 | G1 | Kinase ChemoGenomic Set 2.0, Zenodo 7855618 (2023-04-15) | CC BY 4.0 | **WATCH** |
| P13-6 | G1, G4 | EvE Bio drug-target-activity, Hugging Face | CC BY-NC-SA 4.0, gated by login | **REJECT** |

## What each is, what is separable, what changes a decision

**P13-1 (G2).** G-SRS is the FDA/NCATS substance registry. Code is not needed: the search endpoint is key-less. A probe of
7 of the 22 unresolved names (Berzosertib, Tazemetostat, Evobrutinib, Martinostat, PX-478, Idronoxil, MSC-2364447) returned a
UNII for 6; the 6 UNIIs are all present in our cached UniChem src1src14 file, which maps them to ChEMBL ids. So most of the
22 names are INN drugs the catalogue can reach by an identifier route rather than a name route; the route to add is
name -> UNII -> ChEMBL -> catalogue InChIKey (the `/structure` call returns SMILES and molfile but not an InChIKey, so the
key must come from the catalogue, not from this service). Smallest test: run all 22, accept only a single-UNII, single-ChEMBL
chain, and let a verifier sample 5. It changes the count of "none_unresolved" without touching any action claim. The identity
route of a name is not a claim that the compound acts on the target.

**P13-2 (G4).** Signed directed graph; edges carry sign +1, -1 or 0 and a source-dataset column. Sample file read
(`01a_sample_SIGMA-KG.csv`, 19,234 bytes, sha256 1af2bec5076c4a91afe20e39539ad2b4047077c64dfd42354639bde7bdb791f1, extracted by HTTP
range from the 56.6 MB zip; README sha256 cecbdc9a37275bb117eb4641cddd440732f6041cbe456bee08e1e81305b59b7c). In the sample, the
Chemical-Gene signs are LINCS "increases/decreases expression" (an expression direction, not a pharmacological action) and
nodes are PubChem CIDs, which map to the catalogue by InChIKey. The target-specific mode-of-action task and the four disease
candidate-edge sets (Alzheimer, COPD, Parkinson, schizophrenia) are named in the README, but the file listing of the zip shows the
full edge list (450 MB uncompressed) and nothing I could read says where the MoA labels come from. Code and checkpoint need a
CUDA GPU and are not needed for the test: count Chemical-Gene edges by relation, sign and source, then compare signs for pairs also
in the LEGEND action table. Drop if the action labels are TTD/DrugBank copies (the IT23 NORDic audit already showed TTD conversion
defects) or are expression signs only. A preprint, not peer-reviewed; its "69.6 percent external clinical validation" is the
authors' figure and was not checked.

**P13-3 (G3).** Processed neuron CRISPRi (289 MB) and CRISPRa (154 MB) files plus the 2019 day-7 neuron and iPSC sets. Perturbed gene
list is not stated on any page I read; the single decisive fact is whether any panel gene (WWOX, module, axis, DEE genes) is among
them. One download and a read of the variable names answers it. If none, WATCH.

**P13-4 (G3).** Drug-response signatures in human NPCs from 12 to 13 donors per arm with schizophrenia or control status and 8 cancer
lines, L1000 plus RNA-seq. It is a cell-typed drug-response set, but not a WWOX or epilepsy model, so any overlap is context, not
support. Test: how many of its 135 drugs are in our proposal families (needs the drug list from the paper's supplement).

**P13-5 (G1).** The Zenodo record holds one 87 KB spreadsheet: compound codes, kinase coverage, S10 selectivity at 1 micromolar from
a DiscoverX panel. No structures, no per-kinase values in the sheets read. The underlying PKIS screens are already in ChEMBL.
Reopen if a per-compound table with structures and values is posted.

**P13-6.** The Hugging Face repository shows mode, pXC50, InChIKey for a 1,397-compound library, but access requires a login and
consent to share account information; that is excluded here.

## Searched and found empty (negative results)

- **Kinase/HDAC/sirtuin/caspase measured actions beyond ChEMBL:** Papyrus (newest release found 2024.2, built on ChEMBL 34; same upstream, no new
  actions), Drug Target Commons (CC BY-NC-SA 3.0 per its paper and already inside DGIdb), EUbOPEN chemogenomic sets (site CC BY 4.0, but no
  per-compound table found; a Cell Painting parquet exists, Zenodo 10894238, U2OS, not neural). No HDAC or caspase selectivity panel resource surfaced.
- **Neural/glial Perturb-seq:** KOLF2.1J iPSC genome-scale CRISPRi atlas is undifferentiated iPSC; CM4AI is non-commercial and iPSC only; no processed
  astrocyte or microglia perturbation set found. A hiPSC-astrocyte neuroactive-compound signature paper (2021) and a 2025 thesis exist but no accession was read.
- **Benchmarks with controls:** IxIDN/ORDON (574 positive and 793 negative-pair rare diseases, bioRxiv 2026-06-20) gives no repository or licence on the page read: WATCH
  (reopen when data and licence are public). KG-Bench (bioRxiv 2025), NeurIPS 2026 listings on temporal hold-out and corrupted-graph controls in Parkinson
  repurposing: methods guidance, not data. No rare-neurodevelopmental benchmark with leakage-controlled splits in the named Nature journals.
- **Signed target-action label sets:** DTIAM Activation/Inhibition sets are TTD-derived (already judged defective in the NORDic audit); NegBioDB is negatives only.

## Next iteration

Do P13-1 first (hours, deterministic, verifier-sampled), then P13-2's edge-count test (one 56 MB download). P13-3 and P13-4 are single-fact checks.

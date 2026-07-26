# WWOX — Variant Landscape & In-Silico Triage Pipeline

**A reusable computational pipeline that turns the full public WWOX variant set into a prioritized list of *which variants deserve wet-lab investigation, and with which therapeutic lever.***

> Public, disease-level analysis. Data from public databases (NCBI ClinVar, AlphaFold DB, UniProt, GTEx). No patient is referenced. Specific variants (e.g. p.Gln230Pro, c.1057-2A>G) appear as **worked examples**; the pipeline is designed to be re-run across **all** reported WWOX variants (planned future work, resources permitting).

---

## Why this matters

The rare-disease bottleneck is not ideas — it is **which expensive wet-lab experiment to run first.** For a gene with hundreds of variants of uncertain significance, an in-silico triage that predicts *mechanism* (and therefore *lever*) focuses functional work where it will pay off:

- **folding/stability-defective variants** → candidates for **chaperone / proteostasis** rescue;
- **splice / nonsense / null variants** → candidates for **ASO** (splice-switching) or **gene addition**.

## The variant landscape (public, NCBI ClinVar)

- **Gene:** WWOX, 16q23.1 (common fragile site FRA16D; tumor suppressor). Reference: NM_016373.4 / NP_057457.1 (414 aa).
- **Diseases:** WOREE (WWOX-related epileptic encephalopathy; ClinVar DEE1/DEE28) and SCAR12 (autosomal-recessive spinocerebellar ataxia 12). Null / severely hypomorphic alleles → encephalopathic phenotype (WOREE); milder biallelic combinations → ataxic phenotype (SCAR12).
- **Records analyzed:** 1,327 WWOX variants (ClinVar E-utilities, `WWOX[gene]`).

| Classification | N |
|---|---|
| Uncertain significance (VUS) | 529 |
| Likely benign | 424 |
| **Pathogenic** | **141** |
| Benign | 87 |
| **Likely pathogenic** | **42** |
| Conflicting | 40 |
| Benign/Likely benign | 23 |
| **Pathogenic/Likely pathogenic** | **17** |

→ **200 clinically actionable (P/LP) variants**; the majority (529 VUS) remain uninterpretable — exactly where functional/biomarker work adds value.

**Molecular consequence of the 200 P/LP (loss-of-function signature):** CNV/structural 132 · nonsense/stop-gain 27 · splice-region 23 · missense 13 · frameshift/indel 5. Dominant signature = complete or partial protein loss (consistent with the FRA16D fragile site, prone to large deletions). No single hotspot; point variants distributed across both WW domains and the enzymatic SDR domain.

**Disease association (200 P/LP):** both DEE/WOREE and SCAR12 82 · DEE/WOREE spectrum 49 · other/cancer 38 · unspecified 28 · SCAR12 3.

## Pipeline components

| Stage | Tools (all public) | Output |
|---|---|---|
| Variant ingest | NCBI ClinVar E-utilities | full variant table (HGVS c./p., GRCh38, SPDI, classification, traits) |
| Structural impact | AlphaFold DB (AF-Q9NZC7-F1), biotite (SSE, SASA) | burial, secondary structure, H-bond context per residue |
| Stability (ΔΔG) | ThermoMPNN (structure-based, deep learning), ESM-2 650M (evolutionary LLR) | saturation ΔΔG map (414 × 20), per-site substitution scores |
| Splice impact | Ensembl VEP + SpliceAI + MaxEntScan | acceptor/donor loss/gain, cryptic-site prediction |
| Tissue proxy | GTEx | accessible-tissue readout validity (biomarker feasibility) |
| Lever assignment | mechanism → modality mapping | chaperone-amenable vs ASO-amenable vs gene-addition |

## Files in this folder

- `README.md` — this overview
- `variant_structural_pipeline.md` — worked example: a buried-core SDR missense (p.Gln230Pro), structural + ΔΔG analysis
- `variant_triage_rescuability.md` — the mechanism → lever triage (chaperone vs ASO), with two worked examples
- `proteostasis_rationale.md` — the written rationale behind the chaperone lever and the proteostasis figures, **published together with the 2026-07-14 repair that narrowed it**
- `therapy_levers.md` — literature-anchored therapeutic levers for WWOX/WOREE (public PMIDs)
- *(data/figure artifacts — ClinVar tables, ΔΔG maps, AlphaFold model — added after per-file clean-check)*

> Every result is anchored to public data or a real PMID. In-silico predictions are hypotheses that prioritize experiments; they are not experimental validation, and nothing here is medical advice.

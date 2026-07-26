# Worked Example — Structural & ΔΔG Analysis of a Buried-Core SDR Missense

**Variant:** p.Gln230Pro (Q230P), a WWOX missense in the enzymatic SDR domain. A frequently reported WWOX missense; used here as a worked example of the structural-impact stage.
**Data:** AlphaFold DB AF-Q9NZC7-F1 (v6, 414 aa) · biotite (P-SEA secondary structure, Shrake-Rupley SASA) · ThermoMPNN · ESM-2 650M.

> Public in-silico analysis. No patient referenced.

## Result in one line

Gln230 is a **fully buried residue (relSASA 0.00)** in the catalytic **SDR** core, on an α-helix (227–232), modeled at **pLDDT 98.5**. The **Gln→Pro** substitution is structurally **highly destabilizing**: proline lacks the backbone amide hydrogen and breaks the helical (i, i-4) H-bond; its pyrrolidine ring is sterically incompatible with a buried helical core; and four side-chain H-bonds are lost (including a bridge to Asp223).

## Structural evidence (measured on the structure)

| Property | Value |
|---|---|
| Domain | SDR/oxidoreductase (~130–350), catalytic |
| Secondary structure | α-helix (227–232) |
| pLDDT | 98.5 (very high) |
| Relative SASA | 0.00 → fully buried |
| Backbone H-bond (i, i-4) | N230–O226 = 3.03 Å |
| Side-chain H-bonds | Thr221:OG1 (2.54 Å), Asp223:OD2 (2.72 Å), Ala185:O (3.20 Å), Leu184:O (3.46 Å) |
| Hydrophobic core contacts | Leu184, Ala185, Leu186, Leu187, Leu225, Leu234 |

**Why Gln→Pro is particularly severe here:** (1) helix break — proline has no backbone N–H, so the N230–O226 bond is lost → helix destabilization/kink; (2) steric clash — relSASA 0.00 means zero space for the rigid proline ring without perturbing core packing; (3) loss of a polar H-bond network the apolar proline cannot replace.

## ΔΔG validation (two independent predictors)

| Method | Q230P score | Rank among the 19 substitutions at site 230 |
|---|---|---|
| **ThermoMPNN** (structure-based ΔΔG) | **+1.51 kcal/mol** (destabilizing; all 19 substitutions at the site are destabilizing) | 4th most destabilizing |
| **ESM-2 650M** (evolutionary LLR) | **−9.08 LLR** (strongly deleterious) | **1st — the worst possible substitution** |

A purely structural model and a purely evolutionary model converge: proline is evolutionarily forbidden in a buried α-helix, mirroring the backbone H-bond break identified structurally. Spearman ρ = −0.46 (p ≈ 0.05) across the 19 substitutions.

**Whole-domain context (full in-silico mutagenesis, ThermoMPNN, 414 × 20 = 8,280 predictions):** proline is the **#1 most destabilizing substitution across the SDR domain** (mean +2.09 kcal/mol vs +0.56 for the most tolerated). The SDR core is the most buried, mutation-sensitive region of the protein (mean ΔΔG +1.17 vs +1.09 full-length); sensitivity peaks at hydrophobic/aromatic cores (F144, Y293, T111, I116, L302, L247, Y287, Y361).

## Interpretation

- Consistent with the human observation of **normal mRNA and protein not detected** → a protein-level, not transcriptional, lesion.
  > ⚠️ **The cause remains unresolved.** The primary source states two alternatives — **impaired translation** *or* premature degradation — and does not discriminate between them; insolubility is a third. Synthesis, solubility and turnover must be measured separately, and abundance never establishes function.
- **Not a "weak" allele by default:** although missense, the predicted structural impact is severe — the case where "compound het ≠ null/null; evaluate allele-by-allele" matters. Residual partial function is not excluded (untested here).
- **Biomarker hook:** if the protein is unstable, a **WWOX protein stability/abundance** readout in a cellular model (LCL or fibroblasts — MODERATE tissue proxy per GTEx) is the direct functional test. Whole blood (WEAK proxy) is unsuitable.

## Caveat

In-silico prediction on the wild-type AlphaFold structure. ThermoMPNN and ESM-2 are computational predictors, not experimental measures of stability or function. Experimental validation (WWOX protein level/stability in patient-derived LCL/fibroblasts) remains necessary. AlphaFold models the wild-type; the mutation's effect is inferred from structural context, not from a de-novo folded mutant.

## Artifacts (added after clean-check)

`WWOX_Q230P_structural_impact.png` · `WWOX_Q230P_residue_context.csv` · `WWOX_Q9NZC7_AlphaFold.pdb` · `WWOX_Q230P_ddG_crosscheck.png` · `WWOX_ThermoMPNN_saturation.csv` · `WWOX_ESM2_Q230_scores.json` · `WWOX_SDR_ddG_map.png`

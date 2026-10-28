# GSE126075 descriptive analysis: results (scientist-c, IT5 P6, 2026-10-28)

Follows PRE_ANALYSIS.md (commit 194585cc, written before any gene value was read). No deviation from the declaration in the analysis.
Script: analyse_gse126075.py (python3 -I; seed 20261029; 10,000 matched random sets). Inputs by sha256 in results.json.
Outputs: set_summary.tsv, per_gene_in_sets.tsv, results.json, fig1_sets_vs_matched_null.png, fig2_stage_markers.png.
Exploratory, computational result on published data, four single CAGE libraries, transcript level only, not medical advice.
Credit: GSE126075 is the deposit of Kosla et al. (PMID 31543760).

## 1. Control gates: gate 1 FAILED in the progenitors, gate 2 PARTLY met; as declared, no needs entry follows

| Gate (declared) | Result |
|---|---|
| WWOX lower in the shWWOX arm in both stages, under all three normalisations | NO. hNPC: WWOX is not lower per million (shWWOX 3.35 TPM vs control 2.90 TPM, i.e. 48 vs 148 tags only because the shWWOX library is 3.6 times smaller, 14.3M against 51.0M tags, and the silenced arm is about 15 percent HIGHER in TPM; centred log2 ratio -0.02, uncentred +0.18, renormalised -0.01). Neurons: 2.54 TPM vs 0.52 TPM (21 vs 83 tags, 3.95 fold in raw tags and 4.9 fold in TPM; uncentred -1.58, renormalised -0.79, centred -0.26; Poisson-only interval about +-0.7 on the log2 ratio). So at CAGE level there is no WWOX lowering in the progenitors and a 3 to 4-fold fall in neurons that the gene-matrix composition (neurons_WWOX_del puts about 9 percent of a million in the gene table, against 26 to 61 percent in the other arms) makes hard to size. WWOX is lowly expressed (about 50 to 90 tags), so the estimate is noisy. The paper's blot showed a reduced but present band. |
| Stage positive control (neuronal markers up, progenitor and cycling markers down, control line, neurons vs hNPC) | PARTLY met (the script's strict three-condition flag is false because the radial-glia SET is not down). The control line clearly differentiates at gene level (independent check: STMN2 0 to 2,592 tags, NEFM 195 to 12,480, GAP43 28 to 1,069, NEUROD1 0 to 296, HES1 1,284 to 10, SOX2 2,061 to 252 tags); the declared marker PANELS are poorly covered, so the set-level test is weak. Cell-cycle set -1.41 (down, as expected), neuronal_pan +0.75 (up, only 4 of 9 members measurable, inside its null), radial_glia_progenitor +0.23 (NOT down). The marker panel is poorly covered: the deposited gene table is 9,427 genes (FANTOM5-cross-identified TSS) and omits DCX, RBFOX3, NEUROD2/6, GFAP, GAD1/2, SLC17A6/7, OLIG1/2 and most of the glutamatergic, GABAergic, astrocyte and patterning panels (these sets are unmeasurable). |

Consequence under the declaration: gate 1 fails in the progenitors and n = 1 blocks inference in any case, so no needs entry was made on that basis (see section 7 for the later instruction to record the facts).

## 2. Set results (centred log2 ratio, shWWOX vs control; null = 10,000 expression-matched random sets; rank = two-sided empirical, NOT a p value)

| Set (measurable/declared) | hNPC mean [null 95%] rank | neurons mean [null 95%] rank | Declared outcome |
|---|---|---|---|
| ATF4 gene | -0.15 (407 vs 1,408 tags; uncentred +0.04; Poisson +-0.16) | 6 control vs 41 silenced tags, centred about +2.5: sparse, and 'not measurable' only follows from the declared 10-tag rule (the neuron-stage numbers also carry the global shift of about -1.3 log2 of the neuron libraries) | single gene; ATF4 mRNA flat in hNPC; mRNA is not activity |
| ISR targets (11/12; 10/12; SLC7A11 absent from the table) | +0.64 [-0.47, 0.51] 0.014 | +1.32 [-0.23, 0.54] 0.000 (partly the neuron-library normalisation: median shift about -1.3 log2) | inconsistent or confounded: criteria i and iii met, ii failed (uncentred -0.003 in neurons, a mechanical result of the composition offset of about -1.3); not carried |
| UPR branches (7/8; 6/8) | +0.69 [-0.53, 0.66] 0.040 | +0.25 inside null | not carried |
| OXPHOS nuclear (72/73; 71/73) | -0.00 [-0.31, -0.02] 0.035 | -0.33 [-0.24, 0.00] 0.0004 | not carried; moves with the ribosomal control (below) |
| Mito translation (78/80; 76/80) | +0.28 [-0.23, 0.10] 0.000 | -0.11 inside null | opposite signs across stages; not carried |
| Mito import (21/23; 19/23) | +0.54 [-0.34, 0.31] 0.0006 | +0.12 inside null | not carried |
| Glycolysis and lactate (9/10; 8/10) | +0.46 [-0.61, 0.28] 0.005 | +0.20 [-0.52, 0.19] 0.045 | not carried (ii and iii failed) |
| PDK family (3/4 each) | -0.38 inside null | -0.24 inside null | not distinguishable (PDK4 not in table) |
| Control: cytosolic ribosome (126; 119) | -0.25 [-0.26, -0.05] 0.094 | -0.47 [-0.18, 0.01] 0.000 | an unrelated abundant class moves as far as OXPHOS in neurons |
| Control: housekeeping (12) | -0.13 inside null | -0.05 inside null | not distinguishable |
| Marker radial_glia_progenitor (9) | -1.17 [-0.52, 0.43] 0.000 | -0.50 [-0.37, 0.39] 0.009 | outside null with same sign both stages |
| Marker neuronal_pan (4/5) | -0.69 inside null | -0.76 [-0.59, 0.41] 0.011 | |
| Marker cell_cycle (6) and wnt (3) | inside null | inside null | not distinguishable |

No set meets the declared "descriptive signal worth carrying" rule, and the gate (iv) is failed in any case.

Differentiation progress (fig2): the shWWOX line moves differently along the stage axis. Cell-cycle markers fall less in the shWWOX line
(-0.93 vs -1.41) and radial-glia markers rise (+0.94 vs +0.23); the sets sit inside their stage nulls with n of 4 to 9 members, so this is
a direction without a rank. The more striking line-level fact is at progenitor stage: SOX2 (-1.7), PAX6 (-2.9), HES5 (-3.1) and FABP7
(-1.3) are lower in the shWWOX hNPC library than in the control hNPC library, the progenitor markers VIM, NES, HES1 and SLC1A3 less so.

## 3. Post hoc observations (NOT declared; labelled as such)
- ISR targets: eight of the 11 measurable members are higher at BOTH stages: CHAC1 (centred +2.6 hNPC, +3.1 neurons), TRIB3 (+1.2, +1.8), PSAT1 (+1.3, +1.6), SESN2 (+1.0, +1.2), PCK2 (+0.4, +1.5), ASNS (+0.4, +0.4), DDIT3 (+0.1, +1.2), ATF5 (+0.8, +2.2; ATF5 has 6 control tags in neurons); (the first five clear their Poisson-only interval at both stages; the other three are small or sparse); ASNS, PHGDH, PSPH, GADD45A are flat. The set remains up under renormalisation B (+0.66, +1.42) and after stage-residualisation. Its failure of rule (ii) is an artefact of the uncentred ratio carrying the global offset. This pattern is the opposite sign of the WWOX-knockout organoid (ISR target set lower than chance) and is the sign the fly chain would predict, but the declaration's controls make it uninterpretable as a WWOX effect (below).
- The paper's GSEA places mitochondrial translation and import sets on the knockdown side. In these data the MRPL/MRPS and import sets are HIGHER in shWWOX hNPC (+0.28, +0.54) and not in neurons. The repository's two statements of the GSEA sign differ in wording (dossier: "negative enrichment in the silenced line"; needs.json O6: "on the knockdown side"); this analysis does not adjudicate it, which needs the supplementary table to be re-read.
- The shWWOX hNPC library has 14.3 million tags against 51.0 million for the control (3.6 times smaller; the first run used the BED line count 31.7M for the control, see section 8), and the shWWOX neuron library keeps about 9 percent of its tags in the gene table. Library composition differs by arm in a way that none of the three normalisations can fully remove.

## 4. What these results can and cannot show
They show that in these four libraries the pre-listed ISR/ATF4 target transcripts are higher in the shWWOX arm of both stages, mitochondrial translation and import transcripts are higher in the progenitors, and OXPHOS transcripts are not different from matched sets in the progenitors and slightly lower in neurons together with an unrelated ribosomal control; and that the shWWOX progenitor library has a weaker progenitor-marker profile than its control.
They do not show: that WWOX is silenced in the progenitor library (the CAGE tags do not show it); that the integrated stress response is active (no phospho-eIF2alpha, no ATF4 protein, no kinase measure; ATF4 mRNA is flat in hNPC and unmeasurable in neurons); that respiration or ATP changes (OXPHOS transcript is not flux; the resazurin result of the paper stays the only functional readout); that any difference is WWOX-dependent.

## 5. Limitations
1. One library per arm: no replicate, no variance, no inference. Ranks against matched random sets describe one comparison of single libraries and cannot become p values.
2. The knockdown is not demonstrated in the progenitor library and is modest and noisy in neurons; the paper quantified nothing.
3. The control arms may be native (untransduced) cells: the GEO records say "wild type"/"native" while every sample has the same lentiviral text. If native, transduction and puromycin selection are confounded with silencing, and a stress-response signature (the ISR set) is exactly what that confound could produce.
4. Line state differs (progenitor markers lower in the shWWOX hNPC): differentiation, clonal or selection effects cannot be separated from WWOX loss.
5. Compositional libraries: gene-table share ranges from 9 to 61 percent of tags; the primary centring and the renormalisation assume most genes unchanged; sensitivity A moves the sign of nearly every neuron result.
6. Estimated tag counts are TPM x library total, where the total is recovered from the deposited TSS table (every non-zero TPM is an integer multiple of 1e6/N; hNSC 51,007,825, the other arms equal their BED line counts). Poisson intervals count sampling noise only.
7. Gene table covers 9,427 genes: SLC7A11, PPP1R15A, PKM, PDK4, TOMM70, TIMM23, NDUFA11, MTIF2/3, SLC16A3 and most marker genes are absent, so sets are partial and several marker panels unmeasurable.
8. Gene symbols follow FANTOM5 names with an alias table; hg19 to hg38 liftOver was used upstream.
9. CAGE gene value is the sum over promoters of a gene; a promoter switch is invisible at gene level (per-TSS analysis was not declared and was not done).
10. The paper's own differential-expression and GSEA statistics cannot be reproduced from one library per class; how they were obtained is unstated.
11. Set choice is the author's prior knowledge, uncorrected for the number of sets examined (about a dozen), nothing is called significant.
12. A knockdown is not a biallelic null or a missense allele; a transcript result is not a protein or flux result.

## 6. Needs
Under PRE_ANALYSIS section 7 no observation entry was added at the time of P6 (gate 1 failed in hNPC). Proposal for the Orchestrator: no change to NEED-ISR-ATTENUATION or NEED-MITOCHONDRIAL-RESPIRATION. If an entry is wanted notwithstanding the gate, the honest content is: "GSE126075 (CAGE, one library per arm, knockdown not demonstrated in progenitors) shows the pre-listed ISR target set higher in shWWOX at both stages and mitochondrial translation/import higher in hNPC; uninterpretable as a WWOX effect (n = 1, possibly native control, line-state difference)". The GCN2/PERK/eIF2alpha-phosphorylation measurement gap is unchanged.

## 7. Independent verification and corrections (2026-10-28, after the Orchestrator's verification note)
The conclusions held; these corrections were applied and the script rerun (results.json and the tables regenerated):
1. LIBRARY SIZE: the hNSC control total is 51,007,825 tags (TPM values are exact integer multiples of 1e6/N), not its BED line count of 31,702,049; the script now derives N from the TSS table for all four arms (the other three agree with their BED counts). hNSC WWOX is 148 tags, ATF4 1,408 tags; the silenced hNPC library is 3.6 times smaller than the control. The estimated-tag universe of the hNPC contrast changed slightly (11 ISR members measurable, rank 0.014 instead of 0.011); no decision changed.
2. Eight of 11 measurable ISR members are higher at both stages, not five. 3. ATF4 in neurons: sparse (6 vs 41 tags), not unmeasurable by nature; 'not measurable' is the declared 10-tag rule. The neuron-stage ISR shift partly reflects the global shift (about -1.3 log2) of the neuron libraries.
4. Gate 2 is stated as PARTLY met (section 1). 5. Poisson interval for neuron WWOX is about +-0.7 log2. 6. That the paper's control is shScrambled and that the 9,427-gene table equals the paper's GSEA gene count are paper-sourced and consistent with, not proven by, the GEO records. 7. HES5 and PAX6 have only 11 tags each in the silenced hNPC library: the cell-state difference is noisy and is larger than a WWOX effect alone would justify.
8. The pre-declaration is a self-attested commit order (194585cc 22:23 before 23c40861 22:27, local clock), not an independent proof that no value was read first; the first-pass peeks (file heads, column sums, tag counts) are listed in PRE_ANALYSIS.

## 8. Deviation from the declaration
PRE_ANALYSIS stated the library tag total as the BED line count and called the exact total unknown; it is recoverable from the TSS table and differs for hNSC. The declaration text is left as written; the analysis now uses the recovered totals.

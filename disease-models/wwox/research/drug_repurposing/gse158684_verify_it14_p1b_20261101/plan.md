# plan.md - independent verification of GSE158684 snRNA classification (IT14 p1b)

Written BEFORE opening the producer's code/results (snrna_it13b_pv_20261031) and before computing any number.
Verifier: p1b. Tools: numpy only (no scipy/pandas in this environment). Input read-only, SHA256SUMS verified OK (6/6).

## What I knew before computing
Only the brief: 2 arms (ctrl, ko), one 10x filtered matrix each (31053 genes x ~3182 barcodes in ctrl), producer flagged 30.0% ctrl and 17.5% KO nuclei as ambiguous/doublet,
36 duplicate symbols per arm. I had not seen the producer's class definitions, thresholds, or results.

## Detection convention
"detected" = raw UMI >= 1 for that gene in that nucleus. Symbols resolved by first occurrence for the primary run; duplicates handled as a separate sensitivity.

## Marker panels (fixed now)
- Neuron general: Snap25, Syt1, Rbfox3, Stmn2, Rbfox1 (>=2 detected)
- Excitatory: Slc17a7, Slc17a6, Camk2a, Satb2, Neurod6, Cux2 (>=2 detected) and inhibitory score < 2
- Inhibitory: Gad1, Gad2, Slc32a1 (>=2 detected) ; also needs neuron general >=1
- Oligodendrocyte (ambient-robust panel; Mbp and Plp1 EXCLUDED because they are the known ambient myelin genes): Mog, Mobp, Mag, Cldn11, Opalin, St18, Enpp6(no: Enpp6 is newly formed) -> use Mog, Mobp, Mag, Cldn11, Opalin, St18 (>=2 detected)
- OPC: Pdgfra, Cspg4, Vcan, Ptprz1, Olig1(no, shared) -> Pdgfra, Cspg4, Vcan, Ptprz1 (>=2 detected)
- Astrocyte: Aqp4, Slc1a2, Slc1a3, Aldh1l1, Gja1, Gfap (>=2 detected)
- Microglia: Csf1r, Cx3cr1, P2ry12, Tmem119, Inpp5d, Dock8 (>=2 detected)

## Class assignment
Each nucleus gets the set of "positive" major compartments: NEU(neuron: exc or inh or general>=2 with exc/inh), OLG, OPC, AST, MIC.
- Exactly one positive compartment -> that class. Neurons are subtyped exc/inh; both exc and inh positive -> ambiguous_EI.
- Zero positive -> unassigned. Two or more positive (counting NEU as one) -> ambiguous/doublet-like (EXCLUDED under the primary exclusion rule).
Primary rule R1: exclude nuclei with >=2 positive compartments (using the ambient-robust OLG panel).
Sensitivity R0: no exclusion (assign by highest panel detection fraction, ties -> unassigned).
Sensitivity R2: R1 plus a strict-count rule (compartment positive only if panel UMI sum >= 3).
Sensitivity R3 (ambient-corrected): see below.
Also reported: "naive myelin rule" - OLG panel including Mbp, Plp1 - to reproduce the kind of rule that flags neurons with ambient Mbp/Plp1.

## Interneuron subclasses (within inhibitory)
- PV-A (Pvalb-defined): Pvalb>=1. PV-A strict: Pvalb>=2. PV-A co: Pvalb>=1 and >=1 of Kcnc1, Syt2, Kcna1 and Sst=0, Vip=0.
- PV-B (Pvalb-independent proxy): Lhx6>=1 and Sst=0, Vip=0, Htr3a=0. Reported also split by Pvalb (>=1 vs 0), and overlap A/B.
- SST: Sst>=1 (Pvalb=0 reported separately); VIP: Vip>=1.
All counted among inhibitory nuclei as denominator; also among neurons and all nuclei.

## Immature markers in neurons
Nnat, Sox11, Dcx (brief) + my choice: Sox4, Tubb3, Igfbpl1 -> fraction of neurons with UMI>=1 per gene and fraction with >=2 of 6.

## Wwox
Mean UMI, fraction detected, and per-10k normalised by class. Check ambient: correlation (neurons) of Wwox UMI with Mbp+Plp1 UMI; Wwox in neurons versus in OLG. A neuron-restricted driver (e.g. Cre in neurons) could not change glial Wwox UMI in the nucleus directly; an ambient contribution would make glial-class Wwox reflect the neuronal content of the soup, not glial transcription, and the ctrl-vs-ko glial Wwox difference then proves nothing either way.

## Ambient correction (R3, simple stated way)
Soup profile p_g = pooled UMI per gene over ALL nuclei of the arm (filtered matrix has no empty droplets; low-UMI barcodes cannot be used) normalised to sum 1. For each non-OLG nucleus n: rho_n = (Mbp+Plp1 UMI in n) / (N_n*(p_Mbp+p_Plp1)), clipped to [0,0.5]; expected ambient count of gene g = rho_n*N_n*p_g; subtract and round down at 0. OLG-called nuclei left uncorrected. Limits: p is dominated by real cell content, rho overestimated -> over-correction; stated conservatively. Then reclassify with R1 and recompute decisive numbers. Additional check: classification with a "clean" panel already excludes Mbp/Plp1, so how many nuclei change class is the measure of ambient-driven classification.
Also a low-UMI check: bottom-quintile total-UMI nuclei vs rest.

## Duplicate symbols
Parse features; list duplicated symbols (per arm); flag those in my decisive gene list (all genes above + Wwox). Compare first / sum / second occurrence / the one with greater total UMI (Ensembl-ID-chosen proxy: the duplicate with canonical-looking, i.e. lowest-numbered ENSMUSG, and the one with max UMI) for decisive numbers. If not decisive: stop.

## Competing explanations to adjudicate (using sensitivities, no threshold hunting)
(1) biological composition; (2) maturation; (3) technical difference between pools (depth, genes/nucleus, mito, library); (4) ambient RNA / threshold-dependent classification; (5) nuclei recovery/isolation (nuclei count, UMI distribution, fraction of non-neuronal); (6) model identity (Wwox genotype in the dataset vs assumed).
Discriminating sensitivities: OLG fraction under R0/R1/R2/R3 and under the naive rule; OLG fraction among non-neuronal nuclei (removes neuronal recovery effect); neuron share; UMI depth matched downsampling (binomial to common median UMI); immature marker rates; Wwox detection.
Post-hoc labels: any analysis not listed here is labelled POST-HOC.
Statistics: descriptive only (Wilson intervals on nuclei as units, which treats nuclei as independent: they are not biological replicates; one matrix per arm).

# IT14 p1b: independent verification of the GSE158684 snRNA classification (IT13b)

Verifier p1b, task ORCH-ROADMAP-IT14-20261101, branch `task/it14-p1b`, 2026-10-31 (Europe/Rome). Not medical advice. Exploratory, non-canonical. Reference genotype class only.

## 0. Decision (first)

Verdicts on the producer's statements (package `snrna_it13b_pv_20261031`):

| # | Producer statement | Verdict |
|---|---|---|
| 1 | Pvalb UMI 70 vs 37; 53 vs 33 nuclei with any Pvalb; KO/ctrl share 0.59; Mbp share 0.30; Snap25 1.12; Wwox UMI 2041 vs 204 | CONFIRMED (total_UMI and Pvalb UMI vectors are identical per nucleus; pseudobulk ratios reproduce) |
| 2 | PV composition / Pvalb per cell undecidable at one pool per arm | CONFIRMED. With my independent rules the Pvalb-defined PV-A is 4 vs 2 inhibitory nuclei (R0) and the proxy PV-B 7 vs 9; the direction of the PV-A change is OPPOSITE to the producer's (3 vs 5), which shows the count is rule-dependent, not a measurement |
| 3 | PV-A 3/80 vs 5/125, PV-B 12/80 vs 15/125 (ratio 0.80), S2 19/120 vs 18/142 | NOT CONFIRMED as numbers: only 31 of 69 (ctrl) and 45 of 67 (KO) inhibitory nuclei coincide between the two classifications; PV-B/inhibitory is 7/69 vs 9/67 (R0), i.e. 1.3-fold UP in mine against the producer's 0.80. All intervals include 1. The conclusion (undecidable) is unchanged, the specific counts and the "0.80" must not be quoted as a finding |
| 4 | Oligodendrocyte nuclei 12.0% vs 2.4% of all nuclei, OPC 2.9% vs 6.2% | CONFIRMED WITH CORRECTIONS: direction and 3- to 5-fold size reproduce under every rule I ran, absolute fractions do not (OLG 7.8 to 14.0% vs 2.0 to 4.7%; OPC 3.3 to 7.5% vs 5.6 to 11.3%) |
| 5 | Doublet rule flags 30.0% vs 17.5%, mostly neurons with Mbp/Plp1 ambient RNA | CONFIRMED WITH CORRECTIONS: reproduced when Mbp/Plp1 are in the oligodendrocyte panel (38% of ctrl neurons vs 15% of KO neurons move to ambiguous); with an ambient-robust panel (no Mbp/Plp1) exclusion is balanced (25.3% vs 23.3%). The asymmetry is created by the rule, not by a biological difference in doublets |
| 6 | PV conclusion does not depend on the doublet rule | CONFIRMED (R0, R1, R2, naive, ambient-corrected: PV-A/inhibitory 5.8-9.5% vs 1.7-4.5%, Fisher p 0.21 to 1.0 in every rule; PV-B 10-16% vs 13-18%) |
| 7 | Immature genes higher in KO neurons | CONFIRMED in direction (Sox11 18 to 25%, Dcx 31 to 39%, Igfbpl1 6 to 14% of neurons, Nnat 43 to 50%); Nnat difference vanishes under my crude ambient subtraction (over-correction, see 4.3), others persist. Pool-level technical cause not excluded |
| 8 | Wwox falls also in glia (oligo 193 to 1, astro 156 to 9) | CONFIRMED (R1: OLG 0.47 to 0.00 UMI/nucleus, astro 0.54 to 0.03); ambient RNA explains at most about a quarter of the glial decline; the neuron-restricted-driver reading is not supported by these data |
| 9 | 36 duplicate gene symbols per arm, first occurrence used | CONFIRMED WITH CORRECTION in wording (35 duplicated symbols, 36 surplus rows because Il11ra2 occurs three times) and IRRELEVANT: none of the 53 decisive genes (Pvalb, Sst, Vip, Lhx6, Gad1/2, Slc32a1, Wwox, all panel genes) is duplicated; stop |
| 10 | Same contrast as the GSE158681 bulk deposit; "neuron-targeted"; P17 hippocampus | UNVERIFIABLE here (GEO text and the paper were not read by me; animal overlap not stated) |
| 11 | Unassigned neuron-like nuclei 6.4% vs 14.6% | CONFIRMED in direction (post hoc: pan-neuronal-only nuclei 12.8% vs 17.9% of all nuclei in my rule, 27% vs 35% of neuron-like) |

Sentence the module may use for the oligodendrocyte-composition claim: "In the two pooled GSE158684 nuclei matrices, nuclei classed as oligodendrocyte by ambient-robust markers (Mog, Mobp, Mag, Cldn11, Opalin, St18) are about 3- to 5-fold fewer in the knockout pool than in the control pool (7.8% vs 2.0% of all nuclei; 31% vs 8% of non-neuronal nuclei), with OPC-class nuclei higher; neuron share is similar. With one library per genotype and no replicate this is an observed difference in nucleus composition between two pools, whose cause (tissue composition, delayed maturation, isolation/recovery or other pool-level technical difference, or a broader-than-assumed deletion) these data cannot separate."

State of knowledge before computing: only the brief (arms, 3182 barcodes in ctrl, producer's 30.0%/17.5% flag rates, 36 duplicates). I had not opened the producer's code, results or README; plan.md was written first (thresholds fixed). I compared only after `verify_results.json` existed. The producer's README states that the Orchestrator recomputed Pvalb UMI, Mbp, Snap25 and Wwox totals; I reproduced these independently and the class calls too (not previously recomputed).

## 1. Observed quantities and design limits (first)

* Design: one 10x filtered matrix per arm (ctrl 3182 nuclei, KO 2920; 31053 features); library of origin lost; the GEO series has 4+4 samples but nuclei here cannot give n > 1. Nuclei are not independent biological replicates. All p-values and Wilson intervals below treat nuclei as independent units and are descriptive only (Fisher p reported in `key_numbers.tsv` counts; interpret as description of nucleus sampling within each pool).
* Depth: median UMI 4770 vs 4342, mean 5809 vs 5705, median genes 2186 vs 2030; mt fraction 0.06% vs 0.08% (typical of nuclei). Total UMI 18.48 M vs 16.66 M.
* Pseudobulk per 10^4 UMI (ctrl vs KO): Pvalb 0.038 vs 0.022 (ratio 0.59), Sst 0.12 vs 0.22, Vip 0.04 vs 0.08, Lhx6 0.042 vs 0.038, Gad1 0.46 vs 0.57, Snap25 8.29 vs 9.28, Mbp 6.64 vs 2.02 (0.30), Plp1 3.92 vs 1.36, ambient-robust OLG panel (no Mbp/Plp1) 7.46 vs 2.65 (0.36), OPC panel 3.68 vs 5.29 (1.44), Wwox 1.10 vs 0.12 (0.11).
* Pvalb is nearly undetected: 70 vs 37 UMI in all nuclei; 4 vs 2 (R0) or 4 vs 2 (R1) inhibitory nuclei with Pvalb >= 1 out of 69/56 vs 67/51.

### Class counts (my rules; plan.md; R0 = assign by highest panel detection fraction, no exclusion; R1 = ambiguous if >= 2 compartments positive, panel excludes Mbp/Plp1; R2 = R1 with panel UMI sum >= 3; NAIVE = R1 with Mbp/Plp1 in OLG panel; R3 = R1 after simple ambient subtraction)

| Rule | arm | neurons | inhibitory | excluded ambiguous | OLG | OPC | OLG % all | OLG % non-neuronal |
|---|---|---|---|---|---|---|---|---|
| R0 | ctrl / KO | 1353 / 1233 | 69 / 67 | 0 / 0 | 328 / 72 | 239 / 331 | 10.3 / 2.5 | 28.3 / 7.4 |
| R1 | ctrl / KO | 1093 / 955 | 56 / 51 | 805 (25.3%) / 681 (23.3%) | 247 / 57 | 104 / 163 | 7.8 / 2.0 | 30.6 / 8.2 |
| R2 | ctrl / KO | 1134 / 986 | 67 / 60 | 625 (19.6%) / 461 (15.8%) | 284 / 70 | 128 / 188 | 8.9 / 2.4 | 33.0 / 9.7 |
| NAIVE | ctrl / KO | 675 / 809 | 38 / 49 | 1449 (45.5%) / 900 (30.8%) | 446 / 136 | 64 / 143 | 14.0 / 4.7 | 57.2 / 19.5 |
| R3 | ctrl / KO | 1147 / 987 | 74 / 66 | 593 (18.6%) / 541 (18.5%) | 295 / 76 | 129 / 176 | 9.3 / 2.6 | 33.3 / 10.6 |

Denominators for inhibitory fractions: neurons (R1) ctrl 1093, KO 955; all nuclei 3182 / 2920. Inhibitory share of neurons 5.1% vs 5.3% (R1), 5.1% vs 5.4% (R0): unchanged. Neuron share of all nuclei 34.3% vs 32.7% (R1) and 42.5% vs 42.2% (R0): similar. OLG/(OLG+OPC): 0.70 vs 0.26 (R1), 0.58 vs 0.18 (R0), 0.70 vs 0.30 (R3).

### Interneuron classes (R1; inhibitory denominators 56 vs 51)

| Class | ctrl | KO | note |
|---|---|---|---|
| Inhibitory with Pvalb >= 1 | 4 (7.1%) | 2 (3.9%) | Pvalb >= 2: 1 vs 0 |
| PV-A (Pvalb >= 1 and co-marker Kcnc1/Syt2/Kcna1, Sst=Vip=0) | 3 | 2 | |
| PV-B proxy (Lhx6 >= 1, Sst=Vip=Htr3a=0) | 7 (12.5%) | 8 (15.7%) | Pvalb-negative part 5 vs 8; Pvalb-positive part 2 vs 0 |
| PV-A not in PV-B | 2 | 2 | the two definitions share 2 nuclei (ctrl) and 0 (KO): they are different sets |
| SST | 3 (5.4%) | 9 (17.6%) | Fisher p 0.07 (R1), 0.004 (R0), 0.01 (R2), 0.03 (R3); direction agrees with the producer (13.8% vs 20.0%) but magnitude differs |
| VIP | 5 | 4 | |

PV-B is mostly Pvalb-negative (5 of 7 and 8 of 8), so it is a proxy of an MGE-derived, Sst/Vip-negative pool and not shown to be PV cells. Pvalb per PV-B nucleus cannot be estimated (0 to 2 UMI).

### Immature markers in neurons (fraction of neurons with UMI >= 1, ctrl vs KO; R1)
Nnat 42.6 vs 50.2%, Sox11 17.7 vs 25.3%, Dcx 31.3 vs 38.8%, Sox4 10.2 vs 15.7%, Igfbpl1 5.7 vs 13.7%, >= 2 of 6 markers 29.2 vs 43.8%. Tubb3 has 0 UMI in both arms (uninformative; it is in the feature table). Same direction under R0, R2, NAIVE and after depth thinning of ctrl (post hoc: Nnat 39.9 vs 50.2%). Under R3 Nnat is 41.5 vs 40.4% (see 4.3).

### Wwox UMI per nucleus by class (R1; ctrl vs KO)
neurons 0.76 vs 0.11 (excitatory 0.60 vs 0.10, inhibitory 1.25 vs 0.18), oligodendrocyte 0.47 vs 0.00 (0 UMI in 57 nuclei), OPC 0.64 vs 0.03, astrocyte 0.54 vs 0.03, microglia 0.29 vs 0.12. Per 10^4 UMI glia are at or above neurons in ctrl (OLG 1.37, astro 1.98, OPC 2.45 vs neurons 0.93).

## 2. Ambient RNA, and what it does and does not do

* Myelin ambient load: 70% (ctrl) vs 42% (KO) of neurons carry Mbp or Plp1 UMI, mean Mbp 1.31 vs 0.43 per neuron; pooled myelin share of soup 0.106% vs 0.034% (3.1-fold). Within neurons, Mbp+Plp1 does not correlate with Wwox (r -0.06, -0.01), with Mog (-0.05, -0.02) or with depth (0.05, 0.11): ambient myelin RNA is a flat additive background in neurons, not a signal tied to the other markers.
* Is classification driven by ambient myelin RNA? The naive rule (Mbp/Plp1 in the oligodendrocyte panel) moves 418 of 1093 ctrl neurons (38%) and 146 of 955 KO neurons (15%) to ambiguous; and 199 ctrl / 79 KO unassigned nuclei become "oligodendrocyte". Without Mbp/Plp1 exclusion is balanced and the OLG difference between arms persists in every rule (ratios 0.24 to 0.34). So the exclusion asymmetry in the producer's primary tables is rule-induced (ambient), whereas the OLG deficit is not an ambient artefact of the rule.
* Ambient subtraction R3 (stated in plan.md: soup = pooled profile; per-nucleus fraction from Mbp+Plp1; subtract expected counts): rho median 0.27 (ctrl non-OLG), 0.0 (KO), mean in neurons 0.19 / 0.16. This is an over-correction by construction (pooled profile is dominated by real cells; Mbp+Plp1 counts of true low-level expression are treated as soup). It moves 102 (ctrl) / 78 (KO) ambiguous nuclei back to neurons and leaves the OLG, OPC and PV conclusions unchanged. It did erase the Nnat difference, because single-UMI Nnat detections are subtracted in the KO pool where the soup fraction of Nnat is higher; so Nnat detection-level comparisons are the most correction-sensitive of the immature markers.
* Low-UMI quintile: ambiguous fraction is lower in the lowest-UMI quintile (14.3% / 16.1%) than elsewhere (28.1% / 25.1%), i.e. ambiguity tracks depth (doublet or soup-rich nuclei have more UMI), as expected for neuron+astro co-calls. OLG fraction is similar in the low quintile (6.6% / 2.2%) and rest (8.1% / 1.9%): the OLG deficit is not a low-UMI barcode artefact.
* Wwox and ambient: a neuron-restricted driver would lower Wwox UMI in neurons and, through the soup, a small part in every other nucleus; it would not lower Wwox transcription in glia. Observed: glial Wwox falls by 95 to 100% (OLG, astro, OPC), close to the neuronal fall (86%). Soup Wwox is 1.1e-4 (ctrl) vs 1.2e-5 (KO) of UMI; if all glia have a soup fraction of 5 / 10 / 27% (27% = my myelin-based, probably upper, estimate) the expected ambient Wwox is 0.03 / 0.06 / 0.17 UMI per nucleus in ctrl and 0.003 / 0.007 / 0.019 in KO, against an observed 0.47 to 0.64 in ctrl glia. So at most about a quarter to a third of the ctrl glial signal, and a similar fraction of its decline, can be ambient neuronal RNA; the glial decline is mostly not explained by a neuron-restricted deletion. Either the deletion is broader than neurons (Cre driver not named in GEO), or the KO pool differs, or class calls are contaminated; unresolved.

## 3. Duplicate gene symbols

Both arms: identical feature table (cmp equal). 35 duplicated symbols (36 surplus rows; Il11ra2 has three), e.g. Sept2, Jakmip1, Aldoa, Atp5o, Nudt8, Ints5, Gm16701. None belongs to the 53 decisive genes (see `verify_extra.py` list: marker panels, interneuron genes, immature genes, Wwox, Mbp, Plp1). Pvalb, Sst, Vip, Lhx6, Wwox are single entries. First occurrence vs sum vs max-UMI vs lowest-Ensembl-ID gives identical decisive numbers by construction. Stop: duplicates are irrelevant for this question.

## 4. Comparison with the producer, cell by cell (done only after my numbers were fixed)

### 4.1 Agreement
* Barcode order identical; per-nucleus total_UMI and Pvalb_UMI columns of `labels_{ctrl,ko}.tsv` equal my values in all 3182 and 2920 nuclei. 12 and 15 nuclei flagged PV_B by the producer.
* Totals 70/37 (Pvalb), 2041/204 (Wwox) reproduce; Mbp share ratio 0.30; Snap25 1.12.
* Producer's own oligodendrocyte/OPC directions and Wwox-in-glia observation.

### 4.2 Discrepancies, with size
* Inhibitory nuclei: producer 80 (ctrl) and 125 (KO), mine 69 and 67 (R0) or 56 and 51 (R1). The producer uses UMI sums (inh >= 2 and > exc) among non-doublets; I require >= 2 distinct Gad1/Gad2/Slc32a1 genes. Overlap 31 of 80 and 45 of 125 (producer set), 31 of 69 and 45 of 67 (mine). The producer's inhibitory/all fraction is 1.7-fold higher in KO (2.5% vs 4.3%) and about 1.0-fold in mine (R0 2.2% vs 2.3%): the producer's inhibitory excess in KO is rule-dependent; the producer itself notes the dilution of oligodendrocytes. In inhibitory-per-neuron terms both agree on no resolvable change (producer 6.4 vs 7.8%; mine 5.1 vs 5.3%).
* Pvalb in inhibitory nuclei: producer 5 vs 5; mine 4 vs 2 (R0). Union of producer and mine: 9 vs 5 nuclei.
* Pvalb in the producer's doublet class: 21 of its 53 Pvalb-detected nuclei are in its doublet class (KO 10 of 33); in my R0 labels 32 of the 53 Pvalb-bearing ctrl nuclei are neurons.
* Oligodendrocyte: producer 382 vs 70 (R0 mine 328 vs 72; 239 and 42 shared). Fractions 12.0% vs 2.4% against my 10.3% vs 2.5% (R0) and 7.8% vs 2.0% (R1).
* Doublet class: 955 / 510 vs my ambiguous 805 / 681 (R1) where the proportions differ: 30.0 / 17.5% vs 25.3 / 23.3%; median Mbp+Plp1 of producer doublets 3 (ctrl) vs 1 (KO).
* Exact numbers of unassigned neuron-like not reproduced (different definitions).

### 4.3 Unverifiable
* Cre driver, tissue age and whether animals overlap the GSE158681 bulk samples; library-level variance; whether any difference is genotype or pool; the reality of the "bulk Pvalb log2 -1.70" (not recomputed).

## 5. Observation vs interpretation: oligodendrocyte lineage and Pvalb

Observation (reproduced, rule-robust): OLG-class nuclei 3- to 5-fold fewer, OPC-class 1.5- to 2.4-fold more, neuron share and inhibitory-per-neuron share unchanged; mature myelin genes (Mog, Mobp, Mag, Opalin, Mbp, Plp1) in pseudobulk 0.30-0.36 of ctrl; immature neuronal markers higher in KO neurons; Pvalb UMI 0.59 of ctrl at pseudobulk, undecidable at nucleus level.

| Explanation | What would be expected | What the data show | Status |
|---|---|---|---|
| Biological composition (fewer mature OLG in the tissue) | OLG down, OPC up, neurons unchanged; mature-gene pseudobulk down | all present (OLG/(OLG+OPC) 0.70 to 0.26) | compatible; not separable from the others at n = 1 pool |
| Maturation (delayed oligodendrocyte differentiation; delayed neuronal maturation) | OPC up while OLG down; immature neuronal genes up; KO OLG nuclei with lower mature markers | OPC up, immature neuronal genes up in every rule; KO OLG nuclei have Mobp 12 vs 26 and Mog 9 vs 12 per 10^4 (post hoc, selected by a 2-gene call so biased); pan-neuronal-only nuclei more frequent in KO | compatible; also compatible with an age/stage offset between the two pools |
| Technical difference between pools | depth or QC differences | depth and mt similar (median UMI 4770 vs 4342); depth thinning leaves OLG 7.9% vs 2.0% (post hoc) | depth is not the explanation; unseen batch effect cannot be excluded |
| Ambient RNA / threshold-dependent classification | OLG difference disappears when Mbp/Plp1 are removed or counts raised | difference persists under R0, R1, R2, R3 and naive; ambient myelin differs 3.1-fold between pools | the ambient difference is real but the OLG deficit is not an ambient artefact; it is itself a downstream readout of OLG abundance/lysis in each prep |
| Nuclei recovery / isolation | neurons or all glia lost in one pool | neuron share equal; astrocyte and microglia share similar; OLG-specific | does not explain an OLG-specific effect unless OLG nuclei are selectively lost (OLG nuclei are lower-UMI, 3000 vs 6000, the cell-calling cut-off is not the reason as the lowest-UMI quintile has the same OLG fraction); not excluded |
| Model identity different from assumed | broader-than-neuronal deletion; glial Wwox lost | Wwox UMI falls 95 to 100% in OLG, astro, OPC | observation supports that Wwox is lost in glia too; if the deletion reaches OLG-lineage cells, the shift can be cell-autonomous; cannot be settled without the Cre driver and the paper |

Pvalb: observed 0.59 pseudobulk ratio; nuclei-level classification counts (4 vs 2 inhibitory Pvalb-bearing; PV-A 3 vs 2; PV-B 7 vs 8) cannot separate fewer PV cells from less Pvalb per cell; the PV-A direction flips between my rule and the producer's. Sensitivities used were pre-planned (R0 to R3, naive); depth thinning, pseudobulk mature/OPC sets, OLG marker means and pan-neuronal-only counts are labelled post hoc. No threshold was searched for a favourable result.

## 6. What stays unverifiable
Replicate-level variance; the Cre driver; tissue/age claims; overlap with the bulk deposit; any biological cause; the Nnat shift under ambient subtraction (method-sensitive).

## 7. Edits this implies (proposals; nothing here was edited)
* Producer README item 3: replace "12.0% vs 2.4%" and "17.2% vs 2.9% of non-doublet" by a range across rules (7.8 to 14.0% vs 2.0 to 4.7%), and describe the 30.0% vs 17.5% as rule-induced (Mbp/Plp1 in the doublet rule).
* Producer item 2/PV counts: do not quote "0.80" or the 3 vs 5 counts as findings; quote "PV-A 2 to 7 vs 1 to 5 nuclei depending on the rule, direction not stable".
* Item 8 (Wwox): keep the flag; add that ambient neuronal RNA explains at most about a quarter of the ctrl glial signal.
* NP3A1 stays PARTIAL; add reopening condition "Cre driver and per-library counts".
* Use the sentence in section 0 for the module.

## 8. Files
`plan.md` (written first), `verify_load.py`, `verify_analysis.py`, `verify_extra.py`, `verify_compare.py`, `verify_post_hoc.py` (numpy only; run with a scratch directory for the cached npz), `verify_results.json`, `verify_extra.json`, `key_numbers.tsv` (6 columns). Inputs: `/home/desktop/legend-development/files/geo/GSE158684/` (SHA256SUMS verified OK, 6/6). The producer's code `snrna_pv.py` was not run or imported.

# ADV-198 result (SCI): could a cerebellar composition shift itself generate the P47T cerebellar sterol signature of RP-036? (hypothesis level; reference genotype class only; not medical advice)

result_at: 2026-11-23T16:49Z
task: ORCH-SCI-ADV065-DEEPEN-20261118, step 89 (assignment ADV-198, Codex REPLY_34)
pre-registration: `PREREG_ADV198_SCI_20261123.md` (commit `d03b994ed`, frozen sets with hashes, before any value of those sets was computed). Script: `composition_bound_adv198.py`; outputs in `results/`.

## 0. Disposition: (a) in its weak form, "composition NOT excluded"; RP-036 stays parked; one named anchor

Step 1 passed (anchors exist), step 2 was run as pre-registered, and the pre-registered rule gave Reading C: the sterol shift is smaller than the shift of the largest class-marker set in the same seven libraries, so composition through the measured classes **cannot be excluded**. That is not a finding that composition generates it: the bound is necessary, never sufficient. A computed, NOT pre-registered consequence (section 4) makes the composition route demanding: it needs most of the sterol-gene RNA to sit in a few expanding glial classes. The one anchor that would decide it is missing: class-resolved expression of the sterol genes in cerebellum.

## 1. Step 1: what the held cerebellar data are (reconciled)
* Held table `GSE215425_processed_data.csv.gz`: 37 libraries; cerebellum = **7 libraries**, WT M3, M2, F5, F4 and P47T M6, F8, F10 (4 against 3), the same design as the primary paper's Fig 9a. The ADV-187 staging that lists prefrontal cortex and hippocampus is a subset of this table; the IT12 cerebellum is these seven. The series text says n = 5 per group per region, so three cerebellar libraries (one WT, two P47T) are not deposited; the cerebellum is 4 against 3 in the deposit and in the paper.
* Age: only the range 150 to 280 days for all animals, no per-animal age. Sex: WT 2M+2F, P47T 1M+2F (partly confounded). Same mouse labels recur in forebrain libraries; no matching across regions was used.
* Quantitative cerebellar cell evidence in the primary paper (Hussain et al. 2023, PMC10835625, Fig 5, calbindin and Hcn1 counts, layer thickness) comes from DIFFERENT animals at 80 and 250 days (visual estimates from the figure: Purkinje cells per field about 80 to 25 at 80 days and about 100 to 40 at 250 days, i.e. roughly 60 to 70 percent fewer; basket cells (Hcn1) not different; molecular layer thickness about 185 to 165 um (80 d) and 225 to 165 um (250 d); granular layer about 105 to 90 and 135 to 95 um).
* Independent class markers: Kozareva et al. 2021 Supplementary Table 2 (open access, plain request; Table 1 holds one gene per class and was not used as a set); sets frozen by a stated rule before any P47T value.

## 2. Step 2: what was computed (pre-registered; TMM and log2 CPM as in IT12, CPM >= 1 in at least 3 of 7 libraries, 14 791 genes)
| Quantity | Value (log2 fold change, P47T minus WT) | Leave-one-animal-out |
|---|---|---|
| Global median (all kept genes) | +0.008 | |
| **Sterol core S1** (20 genes; 20 used; 90 percent up) | **+0.234** (about +18 percent) | +0.212 to +0.257 |
| Hallmark cholesterol homeostasis S2 (65 of 74 used; 72 percent up) | +0.162 | +0.132 to +0.204 |
| Class marker sets, mean log2FC (genes used/declared) | | |
| Oligodendrocyte (ODC) 13/15 | +0.288 | +0.172 to +0.382 |
| Astrocyte 14/15 | +0.225 | +0.179 to +0.263 |
| Microglia 14/15 | +0.217 | +0.195 to +0.239 |
| Oligodendrocyte precursor 12/15 | +0.008 | |
| Purkinje (rule-derived) 14/15 | -0.154 | -0.276 to -0.063 |
| Purkinje (literature set Pcp2, Calb1, Pcp4, Car8, Itpr1, Ppp1r17, Grid2, Rora) 8/8 | -0.010 | -0.126 to +0.065 |
| Bergmann 14/15 | -0.059 | |
| Granule 12/13 | -0.020 | |
| Molecular-layer interneuron (MLI) 14/15 | -0.272 | -0.323 to -0.197 |

Bound B = largest class shift = +0.288 (ODC); at the upper leave-one-out range B_hi = +0.382. d(S1) - B = -0.054; the leave-one-out minimum of d(S1) minus B_hi = -0.170 (S2: -0.127 and -0.250). By the pre-registered rule this is Reading C. All numbers are marker-mean log2 fold changes in seven libraries; the groups are collinear with every class score, so no within-group or partial-correlation inference was attempted.

## 3. What the table says (reported against inferred)
* **Computed:** the sterol-synthesis signal is small and broad (about +18 percent, nine of ten genes up), with no global shift. Oligodendrocyte-lineage, astrocyte and microglial marker means rise by a similar amount (+0.22 to +0.29) in the same libraries; this fits the paper's own inflammatory picture (Il1b and Tnf up at least 2-fold in the cerebellum, Results 2.9) and is the composition-or-state signal the bound uses.
* **Inferred, with its limit:** the marker proxy is weak here. The imaging reports roughly 60 to 70 percent fewer Purkinje cells (different animals), yet the literature Purkinje marker mean is flat (-0.010) and the rule-derived set falls only about 10 percent. Marker means in bulk do not track cell number in this mutant (surviving cells, degeneration and state change all move them). So L(c) is a marker-state shift, not an abundance measurement, in either direction, and the bound is only as good as that proxy.

## 4. Computed after the pre-registration (labelled; not part of the exit rule)
If a sterol gene is a mixture, its bulk fold change is 1 + s(F - 1) for a class with abundance fold F = 2^L and share s of the gene's wild-type RNA. To produce +0.234 log2 (fold 1.176): the oligodendrocyte class alone needs s = 0.80 at its mean shift (0.58 at the upper leave-one-out shift); astrocytes alone need s = 1.04 (0.88 at the upper range) and microglia alone 1.08 (0.98): at their own means they cannot. So composition is compatible only if most of the sterol-gene RNA (about 0.6 to 0.8) sits in the expanding oligodendrocyte-lineage class, or a combination of expanding glia. In Kozareva's atlas only Hmgcs1, Msmo1 and Insig1 of the 20 core genes appear as even modest class markers (oligodendrocyte lineage; astrocyte for Msmo1); the other 17 are in no class marker list, i.e. they are not class-restricted. That points away from a large glial share, but it is not a measurement of the share (the cerebellum is mostly granule cells, which express sterol genes too; their share was not computed). It is an inference from marker lists, not a result.

## 5. Dispositions against the three exits
* (a) composition alone reproduces the contrast: **not excluded, not shown**. RP-036's parked line can read: "the cerebellar sterol shift (+0.23 log2 in seven libraries, 4 against 3) is smaller than the oligodendrocyte, astrocyte and microglial marker shifts of the same libraries, so composition cannot be excluded; it would require most of the sterol-gene RNA to sit in the expanding oligodendrocyte-lineage class (computed share 0.6 to 0.8, not measured)."
* (b) anchors absent: partly. Present: the seven libraries, independent marker sets, an external imaging anchor. Absent and decisive: **class-resolved expression of the sterol genes in the P47T cerebellum, or the class fractions in the same animals** (marker means did not track the Purkinje count).
* (c) robust: not met (d is under B).
* ONE named cell-resolved measurement worth comparing, for ADV (not assigned): the per-cluster mean expression of the 20 core genes in the Kozareva mouse cerebellar atlas, to turn the computed share into a measured one (needs the gene-by-cluster means from the atlas portal; I did not download the large atlas), and, if the share is large, a single-nucleus or oligodendrocyte-enriched sterol-gene comparison in P47T cerebellum.

## 6. Limits
Seven libraries, groups collinear with every class; age 150 to 280 days unresolved per animal; sex partly confounded (not adjusted; no sex-stratified test was run); marker means are state-sensitive; the sterol core is my pathway list (S2, the Enrichr list, differs from the MSigDB list IT12 used: 65 of 74 genes usable here against 67 there; the enrichment itself was NOT reproduced here, only the set mean shift); the bound assumes sterol genes are mixtures of the classes in the atlas; Kozareva's article text was not read (supplementary table only; no receipt for it); the P47T paper was re-read in Results 2.6 to 2.9, Fig 5 and its legend only. Nothing about a lipid drug, dose or rank follows from bulk data.

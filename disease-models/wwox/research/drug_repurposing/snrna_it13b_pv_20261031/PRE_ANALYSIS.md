# PRE_ANALYSIS: nucleus-resolved parvalbumin in GSE158684 (written before any gene value was opened)

Scientist, task ORCH-ROADMAP-IT13-20261031, package `snrna_it13b_pv_20261031`, branch `task/it13b-snrna`, 2026-10-31. Exploratory, non-canonical, not medical advice.
What had been opened before this file: only matrix headers (dimensions), barcode counts and the GEO series/sample text. No count value of any gene, no per-nucleus sum, no cluster.

## 1. What the deposit is (GEO text, read in full for GSE158684 and the sample titles of GSE158681)

* Series GSE158684, public 2026-10-01, SubSeries of SuperSeries GSE158685 (with GSE158681 hippocampus bulk and GSE158682 cortex bulk). Mus musculus, P17, hippocampal nuclei, 10x Chromium 3' v3, sNuc-seq, cellranger 3.0.2 count then aggr, Seurat 3.2.0 QC (genes in >= 20 cells; nuclei with >= 300 genes; high-mitochondrial and suspected doublet nuclei removed; the deposit is the post-QC matrix). Declared design: S-Control 3182 nuclei, S-KO 2920 nuclei. Verified against the files: 3182 and 2920 barcodes, 31053 features each.
* Genotype labels: controls `S-Control`; knockouts `Wwox deletion in neurons` (sample titles S_Ctrl1-4, S_KO1-4). The same S_Ctrl/S_KO labels appear in the bulk series GSE158681 (S_Ctrl_1-2, S_KO_1-3), whose "S" contrast is the Pvalb log2 -1.70 hippocampal contrast of the P3a finding. So the snRNA deposit is the same genetic contrast (neuron-targeted deletion vs its Cre-line control, hippocampus, P17), but a different set of samples or at least a different library type (nuclear RNA vs whole-tissue RNA); whether the same animals were used is not stated.
* Replication structure: 8 GSM records (4 per arm) but only TWO matrices were deposited, one per arm ("a final filtered count matrix was created separately for control and KO samples"). All 6102 barcodes carry the suffix `-1`, so the aggr library index is not retained: the library or animal of origin of any nucleus cannot be recovered from the files. Consequence stated in advance: for every analysis here the replicate unit that the files allow is ONE pooled arm (n = 1 per genotype). Nuclei are not independent biological replicates; any interval over nuclei describes sampling of nuclei within one pool, not variation between animals. All statistics are descriptive. The Cre line and the exact Cre driver are not named in the GEO text (the label "S" is used; read the Repudi/Aqeilan paper for the driver, which I have not done here).

## 2. Cell-class calls (thresholds fixed now)

Counts are raw UMI. A "hit" is >= 1 UMI. Marker groups (mouse symbols):
* EXC = Slc17a7, Slc17a6, Camk2a, Neurod6, Satb2 (sum of UMI = exc)
* INH = Gad1, Gad2, Slc32a1 (sum = inh)
* NEURON_PAN = Snap25, Syt1, Rbfox3, Stmn2 (sum = pan)
* OLIGO = Mbp, Plp1, Mog, Mobp; ASTRO = Aqp4, Gja1, Slc1a2, Aldh1l1; OPC = Pdgfra, Vcan, Cspg4; MICRO = Csf1r, Cx3cr1, P2ry12, Hexb; (each group sum; glia = max group)
Rules in this order, each nucleus gets exactly one label:
1. Doublet/ambiguous (flagged, excluded from the primary tables, reported, sensitivity run includes them): exc >= 3 and inh >= 3; or glia-max >= 3 and (exc >= 3 or inh >= 3).
2. Inhibitory neuron: inh >= 2 and inh > exc.
3. Excitatory neuron: exc >= 2 and exc > inh.
4. Glia: glia-max >= 3 and glia-max > pan; assigned to the group with the largest sum (ties to the earlier of OLIGO, ASTRO, OPC, MICRO).
5. Unassigned neuron-like: pan >= 2 and none of the above; Unassigned other: all the rest.
Inhibitory subclasses (within rule 2), non-exclusive hits then priority:
* SST: Sst >= 1; VIP: Vip >= 1 (and Sst = 0); PV-A: Pvalb >= 1 (and Sst = 0 and Vip = 0); other-INH: none of these.
* PV-B (Pvalb-independent proxy, to avoid circularity because Pvalb detection is itself the quantity at stake): inhibitory nuclei with Lhx6 >= 1 and Sst = 0 and Vip = 0 and Htr3a = 0. Lhx6 marks medial-ganglionic-eminence interneurons (PV and SST); excluding Sst leaves mostly PV (and some Pvalb-negative MGE types), so PV-B is a proxy, not a definition.
* Pvalb per cell is measured inside PV-B (Pvalb-independent denominator) and, separately, inside PV-A.

## 3. Statistics fixed now

* Fractions with exact (Clopper-Pearson, via beta quantiles; numpy only) 95% intervals; ratio KO/ctrl with a log-ratio normal interval and a Fisher-type exact two-sided p computed by hypergeometric enumeration. Denominators reported for: all classified nuclei, neurons, inhibitory nuclei.
* Pvalb UMI per nucleus: mean of size-normalised (UMI/total*10^4) and raw detection fraction; difference with a bootstrap over nuclei (2000 resamples, fixed seed). Total-UMI-per-nucleus is compared between arms because depth differs across the two aggr pools.
* Because the unit is one pool per arm: a permutation over nuclei labels is NOT a replicate test (it tests exchangeability of nuclei between pools, which the pooling design cannot support); it is reported only as a descriptive null for the nucleus-sampling variance. Nothing here is called significant. The language used: "supports", "is compatible with", "cannot separate".
* Ambient-RNA indicator: Pvalb UMI rate per 10^4 UMI in glia nuclei (should be ~0 if Pvalb is cell-restricted); the same for Gad1, Snap25 as a neuronal-ambient comparison; if the ambient Pvalb rate differs between arms, Pvalb per cell is not interpretable without correction. Doublet rate per arm from rule 1.
* Predictions that separate the four readings (the PV-B/PV-A fractions are in the inhibitory denominator; thresholds for "supports" are descriptive: relative change >= 30 percent and the exact interval of the KO fraction not containing the ctrl point estimate):
  (a) FEWER PV NUCLEI: PV-B and PV-A fractions among inhibitory nuclei lower in KO; Pvalb per PV-B nucleus about unchanged; inhibitory fraction among neurons unchanged or lower; ambient Pvalb unchanged. If the bulk Pvalb log2 -1.70 (ratio 0.31) were all composition, PV-A/inh in KO would be near 0.3 of ctrl.
  (b) LESS Pvalb PER PV-CLASS NUCLEUS: PV-B fraction unchanged, but Pvalb UMI per PV-B nucleus and the PV-A/PV-B ratio lower in KO; Kcnc1/Kcnc2 may fall with it (same program) while Lhx6/Gad1 do not.
  (c) DELAYED MATURATION: in neurons, immature set (Dcx, Sox11, Sox4, Igfbpl1, Nnat) higher and mature set (Rbfox3, Syt1, Snap25, Atp1a3, Kcnc1) lower in KO within the same class; Pvalb per cell lower with Pvalb being a late (P10-P30) gene; oligodendrocyte maturation: OPC (Pdgfra) up / mature oligo (Mbp, Mog) share down, matching the bulk myelin set (log2 -0.8 to -1.8).
  (d) COMPOSITION SHIFT OF OTHER CLASSES: oligodendrocyte, astrocyte, excitatory fractions differ in KO (bulk: myelin down, astrocyte set up), which would dilute or inflate bulk Pvalb independently of PV cells; excitatory fraction up would lower bulk Pvalb by dilution alone.
  The readings are not exclusive: (a)+(b) may co-occur; (d) always confounds bulk. Direction of change is not role (damage, compensation, composition and unknown stay separate).
* Power note fixed now: inhibitory nuclei are a small minority of hippocampal nuclei and PV-class a fraction of those; with about 3000 nuclei per arm the PV-class count may be tens of nuclei, so exact intervals will be wide. Wide intervals mean "undecidable", not "no effect".

## 4. Verifier needs (fixed now)

Recompute class counts from the six files with the rules above (independent code), the ratio intervals, and check that the sha256 of the six files equals `inputs/SHA256SUMS` in this package.

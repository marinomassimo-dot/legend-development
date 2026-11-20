# ADV-095 proteostasis and HSP70-type premise screen in the held P47T hypomorph tables: pre-registration (frozen before any value is read; SCI successor, 2026-11-20; hypothesis level; no dose, no recommendation; not medical advice)

**Why.** ADV, from IT: a small pre-registered premise screen of proteostasis and HSP70-type sets in the held P47T knock-in hypomorph tables, as evidence, not a gate. It bears on a chaperone or proteostasis route for a hypomorph class (a missense allele that may be unstable) as opposed to the null or neuronal-deletion models of unit A. Unit A already covered the integrated stress response (opposite sign in the organoid, not repeated here).

**Data (held, no network).** `files/deepening_downloads/gse215425/GSE215425_processed_data.csv.gz`, integer counts, 55,010 genes by 37 samples: Wwox WT/WT against P47T/P47T, regions PFC (5 against 5), HPC (5 against 5), CTX (parietal cortex, 5 against 5), CB (cerebellum, 4 against 3). Unit of biological replication: the animal. Sex is in the sample name (M or F): PFC, HPC and CTX have 3 male and 2 female in WT and 2 male and 3 female in P47T (the P47T sample names read M7, M6, F9, F8, F10). Age is not stated in the series text I read; the phenotype is progressive, so the age of these brains is an unknown covariate common to both arms. The cerebellum is the region of reported Purkinje loss and is analysed separately, not pooled.

**Sets (fixed now, mouse symbols; from my knowledge of the literature, not read here).**
- `HSR` (HSF1-type heat-shock response): Hspa1a, Hspa1b, Hsph1, Dnajb1, Hspb1, Hsp90aa1, Dnaja4, Bag3.
- `HSP70_CONSTITUTIVE` (HSP70-type, not stress-induced): Hspa8, Hspa4, Hspa9, Hspa2, Dnaja1, Dnajb6, Stip1, Hsp90ab1.
- `ER_CHAPERONE_UPR` (target genes of the unfolded protein response): Hspa5, Hsp90b1, Pdia3, Pdia4, Pdia6, Calr, Canx, Hyou1, Dnajb9, Herpud1, Sel1l, Edem1.
- `AUTOPHAGY_LYSOSOME`: Lamp1, Lamp2, Ctsd, Ctsb, Ctsz, Hexa, Hexb, Gusb, Npc2, Sqstm1, Map1lc3b, Tfeb.
- `PROTEASOME`: Psma1, Psma2, Psma3, Psmb5, Psmb6, Psmc1, Psmd1, Psmd2.
Genes not in the table are listed. Mouse symbols are matched by exact symbol in the table's `Gene_Symbol` column (no case-mapping trap: the table already carries mouse symbols). The primary question is the pair `HSR` and `HSP70_CONSTITUTIVE`; the other three are secondary and reported with the same rule.

**Composition covariates for the adjusted variant (fixed now).** `ASTRO_REACT` (Gfap, Serpina3n, Lcn2, C3, Vim), `MICROGLIA` (Aif1, Cd68, Tyrobp, Trem2, Itgam), `NEURON` (Snap25, Rbfox3, Syt1, Stmn2, Map2). Each is the mean of the per-gene z-scores across the samples of the region (log2 of counts per million plus 1). The P47T phenotype includes progressive astro-microgliosis; the adjusted variant tests whether a set shift survives that.

**Quantities.** Per region: counts to log2 CPM plus 1 using the library size of each sample (column total of the file); per-gene z-score across the region's samples; set score per animal = mean z of the set's genes present with mean CPM at or above 1 in the region. Unadjusted contrast: ordinary least squares set score on genotype and sex (two covariates); the genotype coefficient is expressed in units of the within-genotype residual standard deviation of the control arm (raw shift in SD). Adjusted contrast: add `ASTRO_REACT`, `MICROGLIA`, `NEURON` scores as covariates; reported, never decisive alone.

**Null.** 5,000 random gene sets of the same size, matched gene by gene on the region's mean log2 CPM (nearest 200 candidates, excluding the set's genes), scored and fitted by the same unadjusted contrast; the empirical 2.5th and 97.5th percentiles of the genotype coefficient are the band.

**Registered rule (per set, per region; cerebellum reported separately).**
- A set is `SHIFT_UP` or `SHIFT_DOWN` in a region if the unadjusted coefficient is outside the null band and its absolute value is at least 0.5 residual SD of the control arm.
- `PREMISE_SUPPORTED_T` for a set: the same direction (`SHIFT_UP` for the heat-shock and UPR sets, `SHIFT_DOWN` is read only as "reduced capacity") in at least two of the three cerebral regions (PFC, HPC, CTX) AND the sign of the adjusted coefficient equal to the unadjusted one in those regions.
- `PREMISE_OPPOSITE_T` for a set: a shift in the opposite direction of a proteostasis load premise (`SHIFT_DOWN` of `HSR`, `ER_CHAPERONE_UPR` or `AUTOPHAGY_LYSOSOME` in at least two cerebral regions) with the same adjusted-sign condition.
- Otherwise `NOT_SUPPORTED_T` (flat, mixed or region-specific). A set that shifts in one region only is reported as region-specific, not supported.
- A premise reading is a load premise only: it asks whether the proteostasis machinery is engaged (heat-shock or UPR sets up) in a hypomorph, not whether a chaperone-type agent would help.

**Not done by this screen.** No protein-level data (these are transcripts: a heat-shock induction can be post-transcriptional or absent while load is present); no exposure or agent comparison; no effect on seizures; no claim about the Q230P-class allele (the P47T is a different missense and a different domain); the mixed-sex, age-unknown, n = 5 per arm design limits power, which is stated in the result.

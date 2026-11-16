# Hypotheses to set tests for, part 4

## M25. Statement: the Wwox-null burst depends on the energy substrate: lowering glucose or adding a ketone body changes the burst rate in null slices and not in wild type, through KATP-type conductances in interneurons or the lactate/ketone route, which would make 'diet' and 'metabolic' classes mechanistically testable in the same assay as the AED arms. Rejecting observation: no genotype-by-substrate interaction on burst rate. Test: the [a session] brief's slice assay with one extra arm (substrate change) in both genotypes; outcomes: interaction present -> a metabolic row (T10) gets a genotype contrast (tier 3) and the diet class moves; absent -> the diet class stays an unexplained clinical observation. Class label: ketone-body/KATP-opener mechanism (label). Pre-test: held expression of glycolysis and ketone-handling genes in the Wwox-null tables (not run). Would change my mind: no substrate effect in the pilot. Cost: one added arm, the pilot's four animals per genotype.

## M26.

**Statement.** The WW1 domain of WWOX restrains the intracellular-domain signalling of the neuregulin receptor ErbB4 in interneurons (WWOX binds ErbB4 through its PPxY motif), so loss of WWOX uncouples neuregulin-driven strengthening of GABAergic output and lowers inhibition onto pyramidal cells; this is rejected if neuregulin raises sIPSC frequency or amplitude equally in knockout and control slices, or if a WW1-scaffold-dead allele with protein present keeps normal inhibition.

**Why a leap.** The thread's inhibitory-defect line (SCI42, INV-15) is about supply (release, interneuron number, PV loss), response (receptor, chloride) or a consequence of bursting, and the oligodendrocyte line uses neuregulin only as a myelination factor (INV-06). It does not use the best-known WWOX partner in interneurons as a candidate: ErbB4 is held in the ledger only as a structure-modelling target (DL-MECH-006). This reading drops the assumption that the sIPSC loss must be a cell-count or chloride problem and treats it as a signalling problem on the interneuron, which would also explain a loss without a PV-number change (INV-15: counts unresolved).

**Existing assay or held table that can test it.** The sIPSC re-record specified as M03/IT42-Q03 (glutamate block, fixed absolute threshold, per-animal summary) and WO-15 (mIPSC in TTX, physiological chloride), with an added neuregulin arm in the same cells. Held tables: the P47T transcript series (GSE215425 per the thread; the WW1 missense, Wwox mRNA unchanged) and the pooled snRNA (`.../snrna_it13b_pv_20261031/`, GSE158684) for Erbb4 and Nrg1 counts by class; the P17 per-table summary `.../ctgf_held_data_adv007_20261114/per_table.tsv` shows the table format (not read for Erbb4).

**The single discriminating observation and its two outcomes.** The neuregulin-induced change in sIPSC (or mIPSC) frequency and amplitude in knockout versus control (and heterozygote) slices, paired with the sIPSC level in a WW1-scaffold-dead missense model. Outcome 1: the response is absent or reduced in the knockout and the missense model shows a similar inhibitory loss; the WW1-ErbB4 route carries part of the deficit. Outcome 2: the response is intact in the knockout and the missense model has normal inhibition; hypothesis rejected and the SDR-domain or other routes stay.

**Repurposing class and at most 2 labels.** Neuregulin-ErbB4 pathway modulation (source of the mechanism: ErbB4 control of interneuron GABA release, outside knowledge); no approved agonist exists, so labels only: neuregulin-1 beta (tool peptide) and, as the opposing-direction class, a pan-ErbB kinase inhibitor (lapatinib as label). The direction of any benefit is not known.

**Held-data pre-test.** No. The folder holds no ErbB4 or neuregulin measurement for any Wwox system; the interneuron data are 5 versus 6 cells, not identified by type, and the thread (INV-15) says no PV-cell physiology exists in the neuron-targeted model. The P47T model is held as transcripts only, with no electrophysiology in the thread. Result: cannot be rejected from the folder.

**What would change my mind.** A neuregulin response of the same size in knockout slices; ErbB4 not detected in the pooled interneuron classes of GSE158684; an inhibitory loss in the missense model equal to that in the null (which would not reject the idea but would say the WW1 route is not what separates them); a direct demonstration that the sIPSC loss is a recording artefact (M03 not reproducing it).

**Cost to test.** About 16 to 20 animals for the neuregulin arm in the existing sIPSC series; the P47T arm needs the missense colony (about 12 animals); 3 table lookups (Erbb4, Nrg1, Pvalb by class in the held pools).

---

## M27.

**Statement:** The ifenprodil-sensitive (GluN2B-containing) share of the NMDAR EPSC in KO layer II/III cells at P13-P17 stays near the immature or sensory-deprived value (about 0.5) instead of the wild-type value (about 0.14), because the experience-dependent loss of the GluN2B share stalls when cortical drive is reduced; rejected if the KO share lies inside the wild-type interval (0 to 0.34) while the bursts are present.

**Why a leap:** The files list a KO-specific change of NMDAR composition and the GluN2B-to-GluN2A switch inside P13-P17 as alternatives to exclude (`target_first_it15_qa_nmdar_20261101/README.md` 5b), and carry a single wild-type number (14 percent, interval 0-34, whisker-intact P13-P15) from Mierau. The same paper has two more arms that are not used: whisker-deprived P13-P15 (49 percent) and P26-P33 (26 percent). This hypothesis names a cause for a composition difference, a deprivation-like stall, and uses the deprived arm as the reference value, which drops the assumption that the P13-P15 wild-type number is the right comparator for a hypoactive or seizing animal. Partial overlap with the stated alternative; the added element is the cause and the positive-control arm.

**Existing assay or table in the repository that can test it:** `wo11_mierau_it55_20261115/README.md` and `second_reader_wo11_sci_20261115/README.md` (the 14 percent, 53 percent, 49 percent and 26 percent values, design, limits); `target_first_it15_qa_nmdar_20261101/README.md` (E0 measurement of f in the same animals and genotypes; WO-10 for burst slices).

**The single discriminating observation and its two outcomes:** In the same pipeline as E0/WO-10, the ifenprodil-sensitive fraction of the isolated NMDAR EPSC in KO versus wild-type littermate layer II/III cells at P13-P17, with a whisker-deprived wild-type arm as a positive control for the reading. Outcome A: KO fraction near the deprived-wild-type value and above the intact-wild-type interval: stalled switch, and the GluN2B-NAM lever has a larger ceiling than the 0.14 floor suggests. Outcome B: KO fraction inside the intact-wild-type interval: composition is not the difference, the bursts do not depend on a retained GluN2B share, and the 0.14 reading carries.

**Repurposing class and at most 2 named examples (labels only):** GluN2B-selective negative allosteric modulators; labels ifenprodil and Ro 25-6981 (source: the IT15 target-first table, `target_first_it15_qa_nmdar_20261101/README.md`, and the Mierau measurement).

**Held-data pre-test:** None can reject it; the folder holds only wild-type numbers (Mierau: 14 percent intact, 49 percent deprived at P13-P15, 53 percent at P6-P8, 26 percent deprived P26-P33) and no KO ifenprodil value. Result: untestable on held tables. Mierau's own limits apply (evoked synaptic current, room temperature, 2 mM Mg2+, between-cell design, one concentration, n counts cells).

**What would change my mind:** A KO fraction at or below the wild-type value; a KO fraction elevated but equal in burst-free and bursting KO slices (a composition change not tied to bursts); a deprived-wild-type arm that fails to reproduce the 49 percent in this lab's hands (the reading would then be unusable).

**Cost to test:** About 24 animals (three arms, roughly 8 each, ifenprodil and control cells pre-incubated as in Mierau; n of 10 to 15 cells per group), 0 table lookups.

---

## M28.

**Statement:** Burst occurrence is a network threshold set by the fraction of Wwox-deficient neurons in the slice, so the incomplete excision of the Synapsin I-Cre line (and the 4 of 23 heterozygote slices) predicts that the 6 of 42 burst-free KO slices carry the lowest fraction of excised neurons; rejected if burst-free and bursting KO slices have the same per-slice excised-neuron fraction.

**Why a leap:** The files read burst incidence as a genotype property (0 of 11, 4 of 23, 36 of 42) and note only that a burst-free knockout contrast is hard to obtain and that Syn1-Cre excision is partial. This drops "the genotype is the unit" and makes the slice's mosaic fraction the explanatory variable, which also changes what a partial NMDAR reduction needs to achieve (it only has to push a threshold system below its threshold). Not stated in any file as a hypothesis, question or conclusion.

**Existing assay or table in the repository that can test it:** `chloride_gradient_sci42_20261110/README.md` (burst counts 0/11, 4/23, 36/42 and the caution that bursting slices confound cause and consequence) and `gsk3_inv09_20261107/output/README.md` (R03, R04: Syn1-Cre excision partial; Nestin-, Olig2-, GFAP-Cre as other arms); `nmda_inv05_20261107/output/README.md` (X2 readouts).

**The single discriminating observation and its two outcomes:** In KO slices, the per-slice fraction of Wwox-negative (or reporter-positive) pyramidal neurons against whether the slice bursts. Outcome A: bursting slices have a higher excised fraction and a threshold is visible (burst-free slices cluster at the low end): the network-threshold reading holds, and a small measured NMDAR reduction could suffice. Outcome B: no relation across a wide range of fractions: the burst is not a mosaic-threshold effect (the neuron-deletion genotype acts per cell or through a tissue-wide factor).

**Repurposing class and at most 2 named examples (labels only):** Partial gain reduction of NMDAR-dependent excitation, GluN2B-selective NAM class; label ifenprodil (source: the matched-current design in `nmda_inv05_20261107/output/README.md` and `target_first_it15_qa_nmdar_20261101/README.md`). No class beyond what the NMDAR thread already holds; the contribution is the expected size of reduction needed.

**Held-data pre-test:** The held counts (0/11, 4/23, 36/42) are monotone with gene dosage and are equally compatible with a cell-autonomous dose effect; no table here has a per-slice excision fraction. Result: cannot reject.

**What would change my mind:** Burst-free KO slices with high excision; bursting HT slices with a low Wwox-negative fraction in a Cre-negative-for-reporter check; a sparse-deletion experiment (Cre at limiting dose) where bursts appear at a fraction well below the KO value.

**Cost to test:** About 10 to 12 KO animals with a reporter or Wwox immunostaining on the recorded slices (retrospective in the same slices as X2); 0 table lookups.

---

## M29. The knockout single-nucleus pool is depleted of neuronal nuclei, so bulk burst-related transcript changes partly reflect composition

* **Statement (IPOTESI).** In the held single-nucleus pool of the S-line knockout the fraction of nuclei carrying a Snap25 UMI is lower than in the control pool, so differences seen in bulk neuron-enriched tables are partly composition. Rejecting observation: the Snap25-positive fraction is equal or higher in the knockout pool.
* **Existing assay or held table:** the single-nucleus matrices GSE158684 (one pool per arm); the cell-class tables for marker definition.
* **Single discriminating observation:** Snap25-positive nuclei as a fraction of all nuclei, knockout against control. (a) Lower: composition must be adjusted in bulk tables; (b) equal or higher: no composition correction needed on this axis.
* **Repurposing class (labels, source):** none; a data-validity hypothesis.
* **What would change my mind:** a fraction equal or higher in the knockout pool.
* **Cost:** one table lookup.

## M30. The GABA-AT/GAT class acts on a glial compartment, so its matrix cell belongs to the glial thread, not the neuronal GABA thread
* **Statement.** In the held tables the transporter targets of the GABA-AT/GAT class are astrocyte-enriched and the enzyme is shared: Slc6a11 (GAT-3) neuron 35.1 against astrocytes 557.4 FPKM (16-fold, mouse), SLC6A11 2.1 against 101.5 (human); Slc6a1 (GAT-1) 128.7 against 419.7; ABAT 53.6 against 53.0 (shared). The class is also the most frequently used in the A1 series (22 children, baseline (ii) rank 1). So the WWOX-relevant effect of this class, if any, should require the astrocyte compartment: it should be present in the null slice (which contains astrocytes) and shrink in a neuron-enriched preparation. **Rejecting observation:** an equal effect in a neuron-enriched preparation, or a held result that places GAT-1/GAT-3 neuron-enriched.
* **Why a leap.** It drops the assumption that a GABA-axis class is scored on the neuronal GABA thread (T2, reduced inhibitory events). The matrix counts the class through T2 and T3 (GABA-A axis); the class's targets are not on that axis.
* **Existing assay or held table.** The held class tables above; the slice burst assay; the organoid GABA-pathway markers (T14) as the neuron-enriched contrast, not read here.
* **The discriminating observation and its two outcomes.** A GABA-uptake/GABA-AT label against vehicle in null slices versus in a neuron-enriched preparation. Glial dependence: the class cell moves from the GABA-A thread to the glial thread (T9) and its score is recomputed there; the top set may lose or keep it depending on the glial cells. Neuronal persistence: the cell stays on the GABA thread and the compartment reading is rejected.
* **Repurposing class (labels only).** GABA-AT inactivators and GABA-transporter inhibitors: vigabatrin-type and tiagabine-type (source: standard mechanism of action).
* **Held-data pre-test.** A table could have rejected it (neuron-enriched GAT-1/GAT-3). Result: not rejected for GAT-3 (16-fold astrocytic in mouse; human 48-fold) and GAT-1 (3.3-fold astrocytic); ABAT shared, so the enzyme half of the class is not compartment-specific.
* **What would change my mind.** A neuron-enriched GAT-1/GAT-3 reading in an adult table, or a null-slice effect of this class that survives astrocyte-poor conditions.
* **Cost.** One additional preparation arm (animals or cultures), plus two table lookups.

## M31.  Lead time to control, not class, separates development outcomes among discordant children
Statement: among children whose seizures responded, the developmental outcome is associated with the interval between onset and the first control (how long hypsarrhythmia ran) rather than with the class that achieved control; rejecting observation: two children with similar latency and opposite development, or with different latency and the same development. Why a leap: it drops the class as the explanatory variable and replaces it with the clock. Existing assay or table: `cases_a1.tsv` (`onset_age_as_stated`, treatment status, `developmental_outcome`) for the 6 both-endpoint children; the INV-10 count of 10+ when it grows (PS-09). Discriminating observation: rank correlation of latency with development in children with both endpoints (n = 6, so descriptive); outcome one (association): the development thread is a timing thread and an observational registry design, not a class-ranking; outcome two (none): timing is not the variable and the discordance stays unexplained. Repurposing class: none by this hypothesis (a timing hypothesis; no treatment statement is made). Held-data pre-test: not run; latencies are partly unstated, so this may be untestable at n = 6, which would itself be the result. What would change my mind: latency unstated in most of the six, so untestable. Cost: table lookups.

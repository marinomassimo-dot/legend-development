# IT28-P4-B: when is ISR activation protective or harmful in neurons and neurodevelopment (transferable rule for INV-02)

Non-canonical research material, not medical advice. Nothing here is a finding about WWOX; every WWOX-facing statement is a conditional test design. The transferable literature was searched without the gene name. Companion batch covering oligodendrocytes and myelin is separate.

Bracketed ids ([F2], [D4], ...) point to the verbatim locator table at the end (quote, section or figure, PMID and PMCID). Twelve papers were read in full text through free routes (Europe PMC `fullTextXML` or NCBI E-utilities `efetch db=pmc`); three are cited from the abstract only and are labelled "abstract only". Methods sections and figure images were not inspected; figure statements below are the authors' own text.

Repo context taken from the brief only (the repo ISR files were not re-read beyond the generation README header): P47T partial-loss mouse leans ISR up, not significant; human KO organoid ISR set lower; shWWOX progenitors higher; sign unresolved. The reading below is about what could resolve that sign, not about what the sign is.

## 1. What the primary sources show

### 1.1 Direction matters first: "ISR low" can be the lesion
- Fmr1-null mouse: p-eIF2alpha is lower, not higher, specifically in excitatory (CaMK2a) neurons and not in inhibitory neurons [F1][F2]; lysates of hippocampus, cortex and amygdala also showed lower p-eIF2alpha (44.83%, 52.41%, 23.3% decreases per the Results text) but not striatum or cerebellum, and the authors argue that lysate-level evaluation can dilute cell-type-specific changes. Human postmortem FXS cortex showed only a trend (p = 0.0989 and 0.1796 for two areas, nested p = 0.0238) [F2h].
- Reduced p-eIF2alpha in excitatory neurons alone is sufficient for autism-like behaviour [F6]; the same ~50% reduction in every cell type (whole-body S51A knock-in) gave no behavioural change and no synaptic change [F7][F7b]. Cell-type resolution decides whether the same molecular change is harmful.
- Restoring p-eIF2alpha in excitatory neurons (CReP knockdown, chosen because GADD34 is itself ISR-induced and "less suited for chronic modulation" [F8]) corrected protein synthesis [F9], mGluR-LTD [F11] and audiogenic seizures [F10]. This is the only primary source found in which potentiation reduced seizures; the mechanism the authors give is mTORC1 hyperactivity lowering p-eIF2alpha [F5], with GCN2 phosphorylation actually increased [F4]: a kinase-activity readout and an eIF2alpha-P readout pointed in opposite directions in the same tissue.
- Transferable: "ISR" is not one sign. Translation up with fewer uORF-mRNA products [F3] is the low-ISR signature; translation down with p-eIF2alpha up is the high-ISR signature (Down syndrome [D8][D2], prion [N4]).

### 1.2 Direction high: attenuation rescues function when the elevation is the cause
- Ts65Dn (Down syndrome model): eIF2-P up in mouse hippocampus and in human DS brain [D2]; kinase identified as PKR, not GCN2 or PERK [D3]. Three independent perturbation levels converged: kinase deletion or inhibitor, S51A allele, and ISRIB. Reduction of eIF2-P corrected long-term memory and L-LTP and "had no effect on WT mice" [D4]; ISRIB did not further enhance WT [D5]; inhibitory (not excitatory) synaptic transmission was the altered axis and was reversed [D6][D7]. This is the strongest cause-not-marker design in the set because function (LTP, memory, mIPSC) moved with the molecular readout and a WT control was flat. It did not test seizures.
- PARS2 (DEE75, a developmental and epileptic encephalopathy) fly model: neuronal knockdown gives delay and bang-sensitive seizures [R1], P-eIF2alpha up [R2], GCN2 (not PERK) phosphorylated [R3]; genetic GCN2 depletion suppressed delay and seizure [R4][R5] and ATF4 knockdown did the same [R6]. The authors state the mechanism of seizure is unknown [R7]. Limits: Drosophila; genetic, not pharmacological; the human-cell arm is HEK293T, not neurons [R8].
- MEHMO (EIF2S3, intellectual disability and epilepsy), patient iPSC: ATF4, CHOP and GADD34 up [M3] with unchanged eIF2alpha-P [M2], i.e. the ISR output was high without the canonical marker moving; ISRIB blocked the derepression [M5], rescued growth and translation [M1] and dendritic branching of NGN2-induced cortical neurons [M4]. It did not repair eIF2 assembly [M7]; it acted at the exchange step. With a second stress the mutant cells were more apoptotic [M6] (iPSCs, not neurons).
- Neurodegeneration, timing and window: prion mice develop a sudden fall in translation (~50%) when eIF2alpha-P peaks [N4], with GADD34 not rising to match [N5]; there is a defined window of reversibility [N6]. Lowering eIF2alpha-P (GADD34 over-expression or PrP knockdown) protected, whereas salubrinal (potentiation) did the opposite [N2][N3][N7]. ISRIB given from the established-synapse-loss stage [H6] protected [H2] while leaving eIF2alpha-P unchanged and lowering ATF4 [H1]; protection did not need complete suppression (ISRIB restores ~70% of synthesis) [H4][H5], and avoided the pancreatic toxicity of the PERK inhibitor [H3]. Not every treated animal was normal: 7/12 had early signs [H7].
- AD model (APP/PS1): eIF2alpha-P up (~150% of WT) [K3]; deletion of PERK or GCN2 prevented plasticity and memory deficits [K1][K2]. Genetic, constitutive, one lab.
- Memory biology (abstract only): reduced eIF2alpha-P lowers the L-LTP threshold and enhances memory, raised eIF2alpha-P (Sal003) blocks late LTP and memory [C1]; GCN2 loss helps after weak training and hurts after intense training [C2]; ISRIB rescued cognition weeks after traumatic injury [C3]; ISRIB enhanced learning in WT mice [S4] (abstract of a full text read).

### 1.3 Direction high but attenuation or potentiation does not behave: protection is context-dependent
- ISRIB reduced viability of cells under chronic ER stress [S1][S2] but not alone [S3]: ISR is compensation when a persistent upstream stressor is present and the cell cannot clear it.
- Persistent ISR (PPP1R15B R658C) in cortex: ATF4 deletion in GABAergic neurons worsened memory, i.e. an ISR effector was protective in that cell type, while deletion in glutamatergic neurons did nothing [P1][P2]. The same paper notes ATF4-deletion in WT excitatory neurons facilitates memory elsewhere, so effector roles are context-dependent [P6]. The ISR drove increased GABAergic and not glutamatergic transmission [P4], matching Ts65Dn [D6] and ISRIB's effect [P5]. The response is cell-type specific: no gene shared by all cell types [P7].
- ALS (mutant SOD1) is a cautionary set: PERK/GADD34 genetics reported protective effects elsewhere [A8]; a later multi-line study found none [A1][A3] and no p-eIF2alpha change in early-symptomatic cord [A2]; guanabenz ameliorated [A7] in one lab and accelerated disease in another, males worse [A4][A6], with a sex and strain difference acknowledged [A9], and protected cells under ER stress [A5]. Guanabenz is also an alpha-2 agonist, so molecular attribution is weak. The sign of pharmacological potentiation is therefore not reproducible in this disease.

## 2. What transfers and what is specific
| Transfers (supported by more than one system) | Specific (do not carry over) |
|---|---|
| The sign of the deviation must be measured first, in the cell type of interest; the rescuing direction is opposite to it [F6][F10][D4][R4] | Kinase identity: PKR (Ts65Dn), GCN2 (PARS2 fly, Fmr1 phospho), PERK (prion, APP/PS1); mTORC1 as the lowering mechanism is Fmr1-specific [F5] |
| Genetic and pharmacological levels converging, plus a WT control that stays flat, separates cause from marker [D4][D5] | Which neuron class carries the effect (excitatory in Fmr1 [F2]; inhibitory transmission in Ts65Dn [D6]; GABAergic ATF4 protective [P2]) |
| Partial attenuation is enough and avoids the toxicity of full inhibition [H3][H4][H5] | Prion window of reversibility and PrP-driven load [N6] |
| A persistent stressor can make ISR compensatory so attenuation is harmful [S1][S2][P2] | ISRIB-specific eIF2B mechanism: ISR output and eIF2alpha-P can dissociate [M2][M5][H1] |
| Potentiation is not a symmetric mirror: it worsened prion [N2][N3], gave discordant ALS [A4][A7] and was rescue only where p-eIF2alpha was low [F9][F10] | ALS inconsistency may be model, sex and compound off-target and does not show the direction is wrong in general |

Not found in the searches run (title and keyword searches of Europe PMC; not exhaustive): a primary source in which ISRIB, a PERK inhibitor or an eIF2alpha-P-raising compound was tested directly for seizures in an epilepsy model. Seizure evidence is two genetic rescues pointing in opposite directions [F10][R5], which is itself the argument for measuring the sign before choosing.

## 3. Decision rule (to apply in a WWOX-deficient human neural system)
1. Measure the sign by protein and translation, not by RNA, in defined cell types (excitatory, inhibitory, progenitor, glia if present) at matched maturity: quantified p-eIF2alpha/total eIF2alpha, global synthesis (puromycin or AHA), and ATF4 protein or uORF-reporter translation. An ISR-target RNA set is a supporting readout only: the PNAS paper itself warns that ATF4 targets can be driven by mTORC1 and other inputs [P3], and the signature is a transcriptional score [P8]; MEHMO shows ATF4/CHOP up with eIF2alpha-P unchanged [M2][M3], and Fmr1 shows lower p-eIF2alpha with higher GCN2 phosphorylation [F4]. Disagreement between readouts is itself a result.
2. Classify the sign per cell type: HIGH, LOW, or mixed. No "ISR is high" statement for the system as a whole without cell-type resolution [F2][P7].
3. Perturb in both directions at partial, matched strength (see section 4), with a wild-type or isogenic-corrected control, and score function, not only the molecular readout.
4. Interpret by the pattern table below; rescue needs a functional endpoint to count (molecular effect is not functional recovery) (for example ISRIB lowered ATF4 with eIF2alpha-P unchanged [H1], and function recovery needed its own test [D4]).
5. Add timing: perturb before and after the phenotype is established, acute versus sustained, because windows and compensation depend on it [N6][C3][S2].

| Result in the WWOX-deficient neurons | Reading |
|---|---|
| Attenuation rescues function, potentiation worsens it, no effect in control | ISR contributes to damage |
| Attenuation worsens, potentiation rescues or is neutral | ISR is protective compensation |
| Both leave function unchanged though the molecular readout moves | Marker or downstream consequence |
| Effects differ by cell type | Cell-type-specific; do not pool [P2][F6][F7] |
| ISR measured low, ISRIB inert, potentiation rescues | Low-ISR lesion (Fmr1-type) |
| Attenuation helps early, hurts late (or the reverse) | Timing-dependent; report the window |

## 4. Discriminating experiment (human, no doses)
System: isogenic WWOX-deficient and corrected hiPSC-derived cortical neurons, ideally excitatory and inhibitory lineages separated, matured to a stage where network activity is measurable (progenitor-stage data cannot answer a neuronal question).
Arms, each in a wild-type-like control as well:
- Attenuation, two independent mechanisms at partial strength: ISRIB (eIF2B activator, downstream of eIF2alpha-P) and a kinase-level reduction (GCN2 or PKR or PERK siRNA or CRISPRi chosen by which kinase shows phosphorylation) [D3][R3]. Convergence of two mechanisms rules out compound-specific effects.
- Potentiation, also two ways: PPP1R15B (CReP) knockdown, which is the chronic, non-ISR-induced route [F8], and a phosphatase inhibitor as an orthogonal chemical arm (with the ALS irreproducibility in mind [A4][A7]). A negative control for ISRIB: if eIF2alpha-P is already low, ISRIB should be inert [D5].
- Readouts: (a) protein: p-eIF2alpha/total, ATF4, CHOP; (b) translation: puromycin or AHA, polysome uORF mRNAs; (c) function: multi-electrode array burst and synchrony, mEPSC and mIPSC frequency separately (E/I balance [D6][P4]), dendritic arbor by Sholl [M4], differentiation rate; (d) viability and apoptosis under a defined second stressor [M6][S2].
- Timing: add at progenitor, early-neuron and mature stages; washout arm to test reversibility.
- Pre-register the prediction: damage predicts attenuation improves a functional endpoint and potentiation worsens it; compensation predicts the opposite; marker predicts no functional change.

## 5. Which test direction is safer
- If the neurons are measured HIGH: attenuation is the better-supported and lower-risk direction in neurons. Reasons: partial suppression with an eIF2B activator rescued function across Down syndrome, prion and MEHMO iPSC neurons [D4][H2][M4], did not alter control function [D5] or cell viability alone [S3], and avoided the toxicity of PERK inhibition [H3]. Risk: it is harmful when a chronic upstream stressor is present [S1][S2], and effector loss in inhibitory neurons worsened memory [P2]; so include the second-stressor viability arm and keep attenuation partial.
- If MEASURED LOW (as the human KO organoid set might suggest, but that set is RNA): potentiation is the rescue direction in the only low-ISR neuronal precedent [F9][F10], and attenuation would be expected to deepen the lesion; but potentiation by phosphatase inhibitors is the less reproducible class [A4][A7][N2], so use the genetic route (CReP knockdown) as the primary arm.
- If MIXED: test per cell type; do not choose a global direction.
- In no case choose the direction before the sign is measured by protein/translation in neurons.

## 6. Not determinable from this literature
- The ISR sign in WWOX-deficient human neurons, and whether any RNA signature in the repo corresponds to eIF2alpha-P activity: no primary source here can tell, and RNA target sets were shown not to track eIF2alpha-P [M2][P3].
- Whether ISR modulation changes seizures in a developmental epileptic encephalopathy in mammals: not found; only fly and Fmr1 audiogenic data [F10][R5].
- Effect size or safety of any lever in WWOX-deficient human neurons; human clinical safety of ISRIB-class compounds (not addressed by these sources).
- Whether potentiation is ever neuroprotective in humans: ALS data conflict [A4][A7].
- Sex, strain and compound off-target effects behind the ALS discordance [A6][A9].
- Anything beyond the abstract for [C1], [C2] and [C3] (abstract only).

## 7. Reading limits
Twelve papers: partial full-text reads (Results, Discussion and abstracts; Methods and figure images not read; supplementary not accessed). Three abstract-only items carry no receipt. Several sources are one-lab, genetic and constitutive; Fmr1 and Ts65Dn are mouse; PARS2 is fly; MEHMO uses iPSCs with a donor-derived line; ALS shows replication failure. Newest items (2026) are not yet independently replicated. Receipts are drafts under `receipts/` and have not been recorded.

## 8. Locator table (verbatim)
| id | PMID / PMCID | locator | verbatim quote |
|---|---|---|---|
| F1 | PMID 37473758 / PMC10592416 | Abstract (Summary) | "the main arm of the ISR, eIF2α phosphorylation (p-eIF2α), is suppressed in excitatory but not inhibitory neurons in a mouse model of fragile X syndrome (FXS; Fmr1−/y)" |
| F2 | PMID 37473758 / PMC10592416 | Results > p-eIF2α is decreased in Fmr1−/y excitatory neurons; Figure 1D-G | "p-eIF2α is decreased in mature excitatory neurons (labeled with Ca2+-calmodulin-dependent protein kinase 2 (CaMK2α)) (hippocampus, Figure 1D; cortex, Figure 1E; amygdala, Figure S2A) but not inhibitory neurons" |
| F2h | PMID 37473758 / PMC10592416 | Results > p-eIF2α is decreased in Fmr1−/y excitatory neurons; Figure S1F-H | "which revealed a trend toward a decrease in p-eIF2α in individuals with FXS compared with their matching controls in two cortical areas" |
| F3 | PMID 37473758 / PMC10592416 | Results > p-eIF2α is decreased ...; uORF analysis, Figure S2J-M (published TRAP datasets re-analysed) | "mRNAs containing uORFs in their 5′ UTR were substantially enriched in the subset of genes downregulated in excitatory neurons of Fmr1−/y mice compared with control animals" |
| F4 | PMID 37473758 / PMC10592416 | Results > Hyperactivated mTORC1 downregulates p-eIF2α; Figure S3 | "showed an increase in GCN2 phosphorylation on Thr899, indicating its activation" |
| F5 | PMID 37473758 / PMC10592416 | Discussion | "suggesting that enhanced mTORC1 activity contributes to reduced ISR in FXS" |
| F6 | PMID 37473758 / PMC10592416 | Results > Decreased p-eIF2α in excitatory neurons causes phenotypes reminiscent of ASD; Figure 3 | "These findings demonstrate that the selective reduction of p-eIF2α in excitatory neurons is sufficient to engender altered social and repetitive/stereotypic behaviors, which are hallmarks of autism." |
| F7 | PMID 37473758 / PMC10592416 | Results > same section; Figure 4, Figure S9G-H | "Surprisingly, Eif2αS/A KI animals showed no significant change in social interaction" |
| F7b | PMID 37473758 / PMC10592416 | Results > same section; Figure S9G-H | "mice with whole-body reduction in p-eIF2α (Eif2αS/A KI) showed no change in either synaptic excitation or inhibition" |
| F8 | PMID 37473758 / PMC10592416 | Results > Rescue of Fmr1−/y phenotypes by increasing p-eIF2α | "GADD34, which can also recruit PP1 to eIF2α, is induced by the ISR and is therefore less suited for chronic modulation of p-eIF2α." |
| F9 | PMID 37473758 / PMC10592416 | Results > Rescue of Fmr1−/y phenotypes by increasing p-eIF2α; Figure 5D-E | "normalization of p-eIF2α in excitatory neurons of Fmr1−/y mice corrected elevated protein synthesis" |
| F10 | PMID 37473758 / PMC10592416 | Results > Rescue ...; Figure 6I-K | "the audiogenic seizure phenotype of Fmr1−/y mice was substantially alleviated upon correction of p-eIF2α" |
| F11 | PMID 37473758 / PMC10592416 | Results > Rescue ...; Figure 6A-D | "Fmr1−/y mice injected with AAV-CReP-shRNAmir exhibited intact mGluR-LTD" |
| R1 | PMID 41380592 / PMC12754399 | Abstract | "Inactivation of dPARS2 in Drosophila causes developmental delay and seizure" |
| R2 | PMID 41380592 / PMC12754399 | Results > Activation of the integrated stress response in dPARS2 deficiency; Figure 5A-B | "The ISR was indeed activated in dPARS2-deficient fly heads, as determined by the increased P-eIF2α levels" |
| R3 | PMID 41380592 / PMC12754399 | Results > The GCN2 branch ...; Figure 6A-B | "Phosphorylation of GCN2, but not of PERK, was increased in the head of dPARS2-deficient flies" |
| R4 | PMID 41380592 / PMC12754399 | Results > Inhibition of the GCN2 branch ...; Figure 6G-K | "Depletion of GCN2 in dPARS2-deficient animals largely suppressed developmental delay" |
| R5 | PMID 41380592 / PMC12754399 | Results > Inhibition of the GCN2 branch ...; Figure 6J-K | "the seizure phenotype was largely reduced or suppressed in dPARS2-deficient flies lacking GCN2" |
| R6 | PMID 41380592 / PMC12754399 | Results > ISR activation triggers developmental delay and seizure through ATF4; Figure 7 | "downregulation of ATF4 largely rescued the developmental delay and seizure induction defects caused by dPARS2 deficiency" |
| R7 | PMID 41380592 / PMC12754399 | Discussion | "we have yet to determine the exact mechanism by which ISR activation causes developmental delay and seizures" |
| R8 | PMID 41380592 / PMC12754399 | Results > PARS2 V95I mutation causes ISR activation in human cells; Figure 8 | "we individually expressed the His-tagged wild-type PARS2 and His-tagged PARS2 variants by transfection into human embryonic kidney 293T (HEK-293T) cells" |
| P1 | PMID 42446983 / PMC13389509 | Abstract (Significance) | "the ISR effector ATF4 protects GABAergic neurons during ISR-induced impairment, whereas its deletion in glutamatergic neurons has no effect" |
| P2 | PMID 42446983 / PMC13389509 | Results > Cell Type–Specific Roles of ISR Downstream Effectors; Figure 4E-F | "deletion of Atf4 from GABAergic neurons in Ppp1r15bR658C mice (Ppp1r15bR658C:Atf4flox/flox:CreGad2+ mice) exacerbated their long-term memory deficits (Fig. 4F), indicating that ATF4 has a protective functional role in this neuronal population" |
| P3 | PMID 42446983 / PMC13389509 | Results > Identification of an ISR Signature Using scRNA-seq | "ATF4 can be modulated by ISR-independent mechanisms, including mechanistic target of rapamycin (mTORC1)-mediated translation (105–107), promoter methylation, and posttranslational modifications (108). Consequently, relying solely on ATF4 targets risks confounding ISR activity with other signaling pathways." |
| P4 | PMID 42446983 / PMC13389509 | Discussion | "Ppp1r15bR658C mice exhibited increased GABAergic, but not glutamatergic, synaptic transmission (91)." |
| P5 | PMID 42446983 / PMC13389509 | Discussion | "ISR inhibition reduces GABAergic synaptic transmission without affecting glutamatergic synaptic transmission (20, 39)" |
| P6 | PMID 42446983 / PMC13389509 | Discussion | "This discrepancy highlights the cell-type- and context-dependent functions of ATF4" |
| P7 | PMID 42446983 / PMC13389509 | Results > Distinct Patterns of ISR Activation across Different Brain Cell Types; Figure 1D | "Despite persistent ISR activation, no gene was consistently regulated across all brain cell types" |
| P8 | PMID 42446983 / PMC13389509 | Results > Identification of an ISR Signature; Figure 3B | "revealed upregulation of the ISR genes across all cell types" |
| P9 | PMID 42446983 / PMC13389509 | Introduction | "In their brains, the variant disrupts the PPP1R15B•PP1 complex, leading to ISR activation (increased eIF2-P levels)" |
| D1 | PMID 31727829 / PMC7299149 | Abstract | "reversed the changes in translation and inhibitory synaptic transmission and rescued the synaptic plasticity and long-term memory deficits in DS mice" |
| D2 | PMID 31727829 / PMC7299149 | Results > Activation of the ISR in the brains of Ts65Dn mice and individuals with DS; Figure 1F-G | "We found increased eIF2-P levels in brain samples from human individuals with DS compared with non-DS euploid controls" |
| D3 | PMID 31727829 / PMC7299149 | Results > The PKR branch ...; Figure S4 | "Phosphorylation of PKR, but not of GCN2 or PERK, was increased in the hippocampus of Ts65Dn mice" |
| D4 | PMID 31727829 / PMC7299149 | Results > Inhibition of the ISR rescues ...; Figure 4E-F, Figure S12 | "reduction of eIF2-P levels corrected the deficits in long-term memory (Fig. 4E and fig. S11) and L-LTP in Ts65Dn mice (Fig. 4F) but had no effect on WT mice (fig. S12)" |
| D5 | PMID 31727829 / PMC7299149 | Results > Inhibition of the ISR rescues ...; Figure 4G-H, Figure S13 | "although it did not further enhance L-LTP (fig. S13A) or long-term fear memory (fig. S13B) in WT mice" |
| D6 | PMID 31727829 / PMC7299149 | Results > Inhibition of the ISR reverses the enhanced inhibitory synaptic transmission; Figure 5 | "Excitatory synaptic transmission (determined by measuring miniature excitatory postsynaptic current frequency and amplitude) was not altered in the hippocampus of Ts65Dn mice (fig. S15)." |
| D7 | PMID 31727829 / PMC7299149 | Results > same; Figure 5E-H | "reduced the enhanced synaptic inhibition in Ts65Dn mice" |
| D8 | PMID 31727829 / PMC7299149 | Results > Activation of the ISR ...; Figure 1A-F | "mRNA translation in the hippocampus of Ts65Dn mice was reduced" |
| M1 | PMID 31836389 / PMC7035991 | Abstract | "Addition of the drug ISRIB, an activator of the eIF2 guanine nucleotide exchange factor, rescues the cell growth, translation, and neuronal differentiation defects associated with the EIF2S3 mutation" |
| M2 | PMID 31836389 / PMC7035991 | Results > Constitutive activation of the ISR in eIF2γ-fs iPSCs; Figure 1C | "no significant changes in eIF2α–P levels were observed between the WT (eIF2α–P/eIF2α = 1.1±0.2) and mutant (eIF2α–P/eIF2α = 1.0±0.3) iPSCs (Figure 1C), suggesting that the eIF2γ-fs mutation is inducing the ISR independent of eIF2α phosphorylation" |
| M3 | PMID 31836389 / PMC7035991 | Results > Constitutive activation of the ISR ...; Figure 1C | "the levels of the key ISR members ATF4, CHOP, and GADD34 were elevated in the patient-derived cell lines" |
| M4 | PMID 31836389 / PMC7035991 | Results > Neuronal differentiation defect ... is rescued by ISRIB; Figure 6A,C,D | "the dendritic branching phenotypes were rescued by differentiating the mutant iPSC-derived neurons in the presence of ISRIB" |
| M5 | PMID 31836389 / PMC7035991 | Results > ISRIB rescues eIF2γ-fs cell growth and translation defects; Figure 5C, Figure S4 | "ISRIB treatment blocked the basal derepression of ATF4, CHOP, and GADD34 levels in the mutant iPSCs (Figures 5C & S4) with no change in eIF2αphosphorylation" |
| M6 | PMID 31836389 / PMC7035991 | Results > Hyperinduction of the ISR in MEHMO syndrome iPSCs causes apoptosis; Figure 3E-F | "two markers of apoptosis, Caspase 3/7 activity and DNA fragmentation as measured by TUNEL levels, were substantially elevated in the mutant iPSCs upon TG treatment" |
| M7 | PMID 31836389 / PMC7035991 | Results > ISRIB rescues ...; Figure 5D | "ISRIB did not restore eIF2α association or reduce CDC123 association with the partial eIF2 complex" |
| H1 | PMID 25741597 / PMC4385927 | Figure 2 legend | "ISRIB treatment (blue bars) lowers ATF4 levels while leaving eIF2α-P unchanged in prion-diseased mice when compared with vehicle treated (gray bars) animals" |
| H2 | PMID 25741597 / PMC4385927 | Results > ISRIB is neuroprotective in prion-diseased mice; Table 2 | "none (0/12) of the ISRIB-treated animals, but all (9/9) vehicle-treated mice developed confirmatory signs of prion disease by 12 w.p.i. on clinical observation" |
| H3 | PMID 25741597 / PMC4385927 | Results > ISRIB is not toxic to the pancreas; Figure 5 | "chronic GSK2606414 treatment was toxic, causing ~50% reduction in pancreatic weight (Figure 5b) and extensive destruction of exocrine acinar pancreatic tissue (Figure 5c). Critically, ISRIB treatment produced no detectable pancreatic toxicity" |
| H4 | PMID 25741597 / PMC4385927 | Discussion | "Thus, ISRIB only restores protein synthesis rates to ~70% of control levels in vivo (Figure 2b)" |
| H5 | PMID 25741597 / PMC4385927 | Discussion | "the beneficial effects of ISR-reversing drugs in preventing neurodegeneration do not require full suppression of the response" |
| H6 | PMID 25741597 / PMC4385927 | Results > ISRIB reduces ATF4 levels ... | "ISRIB or vehicle alone from 7 w.p.i., when synapse loss is established" |
| H7 | PMID 25741597 / PMC4385927 | Table 2 legend | "Seven out of 12 ISRIB-treated mice exhibited early indicator clinical signs, but none progressed to confirmatory signs" |
| N1 | PMID 22622579 / PMC3378208 | Main text (no section titles in the author manuscript); Fig. 3a-d | "Transient eIF2α phosphorylation is beneficial to cells overloaded with misfolded proteins - reducing protein synthesis and increasing availability of chaperones, promoting refolding22,23. However, persistently high levels of eIF2α-P are detrimental in vitro24." |
| N2 | PMID 22622579 / PMC3378208 | Main text; Fig. 3d-k | "Critically, treatment with salubrinal had the opposite effect, by preventing dephosphorylation of eIF2α-P." |
| N3 | PMID 22622579 / PMC3378208 | Main text; Fig. 3k | "Salubrinal treatment resulted in earlier severe neuronal loss (Fig. 3k)" |
| N4 | PMID 22622579 / PMC3378208 | Main text; Fig. 2c,h | "We found abrupt, significant reduction in global translation rates, with a 50% decline in 35S-methionine incorporation in hippocampal slices from prion-infected mice at 9wpi" |
| N5 | PMID 22622579 / PMC3378208 | Main text; Fig. 2d | "GADD34 levels did not change, despite rising eIF2α–P levels, suggesting insufficient GADD34 for dephosphorylation of increased eIF2α–P" |
| N6 | PMID 22622579 / PMC3378208 | Main text; Fig. 1, Fig. 3 | "This is the window of reversibility when diseased neurons can still be rescued" |
| N7 | PMID 22622579 / PMC3378208 | Main text; Fig. 3 | "Promoting eIF2α-P dephosphorylation rescues vital translation rates and is thereby neuroprotective, while preventing this further reduces translation and enhances neurotoxicity." |
| A1 | PMID 30923003 / PMC6588429 | Abstract | "neither genetic inhibition of the UPR via ablation of PERK, nor genetic UPR enhancement via ablation of GADD34, is beneficial for mtSOD1-induced motor neuron disease" |
| A2 | PMID 30923003 / PMC6588429 | Discussion | "The protein levels of p-eIF2α, as well as mRNA and protein levels of GADD34 and CHOP, were consistently unchanged in all mtSOD1 mouse strains analyzed" |
| A3 | PMID 30923003 / PMC6588429 | Discussion | "we discovered that PERK haploinsufficiency had no effect on disease in all five mtSOD1 mouse models studied, including the G85R mice" |
| A4 | PMID 26288094 / PMC4545826 | Abstract | "guanabenz treatment accelerated ALS-like disease progression in a strain of mutant SOD1 transgenic ALS mice" |
| A5 | PMID 26288094 / PMC4545826 | Abstract | "guanabenz is protective in fibroblasts expressing G93A mutant SOD1 when they are exposed to tunicamycin mediated ER stress" |
| A6 | PMID 26288094 / PMC4545826 | Discussion | "G93A-SOD1 male mice were more sensitive to the deleterious effects of guanabenz than their female counterparts." |
| A7 | PMID 25134731 / PMC4179984 | Abstract | "We have now treated G93A mtSOD1 transgenic mice with guanabenz and found a significant amelioration of disease" |
| A8 | PMID 25134731 / PMC4179984 | Abstract | "mtSOD1 transgenic mice that are haploinsufficient for PERK have a significantly accelerated ALS disease, while mtSOD1 mice that are haploinsufficient for GADD34 have a remarkably ameliorated disease" |
| A9 | PMID 26288094 / PMC4545826 | Discussion | "Jiang et al tested guanabenz only in female G93A-SOD1 mice" |
| S1 | PMID 23741617 / PMC3667625 | Abstract | "ISRIB reduces the viability of cells subjected to PERK-activation by chronic endoplasmic reticulum stress." |
| S2 | PMID 23741617 / PMC3667625 | Results > ISRIB impairs adaptation to ER stress; Figure 5A-B | "ISRIB addition caused a strong synergistic effect on ER-stressed cells, reducing colony number and size significantly more than ER-stress alone" |
| S3 | PMID 23741617 / PMC3667625 | Results > ISRIB impairs adaptation to ER stress; Figure 5A | "Importantly, addition of ISRIB alone did not affect cell viability" |
| S4 | PMID 23741617 / PMC3667625 | Abstract | "Remarkably, ISRIB-treated mice display significant enhancement in spatial and fear-associated learning." |
| K1 | PMID 23933749 / PMC3756900 | Abstract | "The genetic deletion of the eIF2α kinase PERK prevented enhanced eIF2α phosphorylation, as well as deficits in protein synthesis, synaptic plasticity, and spatial memory in APP/PS1 AD model mice." |
| K2 | PMID 23933749 / PMC3756900 | Abstract | "deletion of another eIF2α kinase, GCN2, prevented impairments of synaptic plasticity and spatial memory defects displayed in the APP/PS1 mice" |
| K3 | PMID 23933749 / PMC3756900 | Results > Deletion of PERK prevents Aβ-induced impairment in LTP; Fig. 1a | "increase in the levels of phosphorylated eIF2α in the hippocampus (150.60 ± 24.26 % of wild-type levels; Fig. 1a)" |
| C1 | PMID 17418795 / PMC4149214 (abstract only) | Abstract (Summary) | "in eIF2α+/S51A mice, in which eIF2α phosphorylation is reduced, the threshold for eliciting L-LTP in hippocampal slices is lowered and memory is enhanced. In contrast, only early-LTP is evoked by repeated tetanic stimulation and LTM is impaired, when eIF2α phosphorylation is increased by injecting into the hippocampus a small molecule, Sal003, which prevents the dephosphorylation of eIF2α" |
| C2 | PMID 16121183 / PMC1464117 (abstract only) | Abstract | "after weak training, their spatial memory is enhanced, but it is impaired after more intense training" |
| C3 | PMID 28696288 / PMC5547647 (abstract only) | Abstract (Significance) | "rescued cognition in two TBI mouse models, even when administered weeks after injury" |

# Report X

The file /tmp/claude-1000/-home-desktop-legend-development/9400b253-25a0-4b03-8822-96361325fc16/scratchpad/arm_s/REPORT.md was NOT written. The Write call was refused by the harness ("Subagents should return findings as text, not write report files"). The report is below instead. Tool calls used: 48 (the refused Write counted as 1).

# Arm S report: WWOX WW1/PPxY partner branch (ERBB4, NETO2). Hypothesis level; no dose, no clinical recommendation; not medical advice; reference genotype class WWOX loss of function in DEE. 2026-11-19.

## Decision
**(b) a distinct experiment, not (a) a pharmacological comparison.** ERBB4 has a direct WW1-PPxY interaction, but only in human cell lines and with recombinant domains, and I could read it only at abstract level. NETO2 has no interaction evidence, only a motif scan. Neither has been shown with WWOX in a neuron or interneuron. No measurement links either partner to a function a drug could move, and no sign is known. The experiment is a binding and localisation test in neural lysate, using the peptide pull-down already run on cerebellar lysate (Q6). A pharmacological comparison becomes justified only after that test.

## Q1. Direct versus only proposed
**Direct, binding shown (all non-neural):**
* WWOX and ERBB4.
  * Aqeilan 2005: WWOX associates with full-length ErbB-4 "via its first WW domain" in HeLa and MCF-7 (human lines). A WWOX mutant that cannot bind ErbB-4 does not affect YAP coactivation. **Abstract only.**
  * Schuchardt 2013: biophysics with recombinant human domains. WW1 binds PPxY motifs in the ErbB4 ICD and WW2 does not. **Abstract only.**
  * Rotem-Bamberger 2022: NMR and ITC with an ErbB4 PPxY peptide. WW2 marginally raises single-motif affinity, and a dual-motif peptide binds about 10 times more tightly. **Abstract only.**
  * I could not open any of the three full texts: PMC returned a reCAPTCHA (route stopped, not retried), Europe PMC REST returned no full text, and the PubMed full-text tool returned an empty body. Motif sequences and Kd values were not checked in Methods or tables.
* Other WW1-PPxY partners, non-neural.
  * Hussain 2018 (open full text read): WWOX TAP-MS in HEK293T. Co-IP validated SEC23IP, SCAMP3 and VOPP1 via WW1 PPxY. ERBB4 and NETO2 do not appear in the text (only in a reference title).
  * Abu-Odeh 2014 (**abstract only**): GST-WW1 MS plus phage display in HEK293. It also reports non-canonical LPxY partners, including ITCH.
* WW1 requirement with the protein present: Hussain 2023 (full text read). The P47T WWOX from mouse cerebellar lysate fails to pull down biotinylated PPPY oligopeptides from Dvl2 and Wbp1. Wild type pulls them down. ERBB4 and NETO2 peptides were not tested.

**Only proposed or inferred:**
* **NETO2.** The PPHY at residue 395 of mouse Neto2 comes from a secondary motif scan of UniProt cytoplasmic topology (a secondary note, **secondary**). That scan's smallest BH q is 0.079 and it says it locates motifs without showing that WWOX binds them. NETO1 carries the same PPHY. PubMed `WWOX NETO2 interaction` returned 0 records (2026-11-19). The NETO2 branch is proposed only.
* **ERBB4 in neurons:** inferred, because every binding datum above is non-neural. The scan lists three mouse Erbb4 PPxY motifs (PPIY 1032, PPAY 1053, PPPY 1298; secondary). That agrees with the biophysics and is not independent of it.
* **Interneuron specificity:** no source I found ties WWOX binding to ERBB4 in PV or other interneurons.

## Q2. Observed in pertinent neural systems
**None of the interactions above was shown in a neural system.** The preparations were HeLa, MCF-7, HEK293 and HEK293T cells and recombinant domains.
* The one neural binding assay is Hussain 2023: adult P47T knock-in versus wild-type mouse cerebellar lysate, peptide pull-down with Dvl2 and Wbp1 PPPY peptides. The partners are not ERBB4 or NETO2 and the cell type is unresolved.
* Hussain 2019 and Hussain 2023 (both full text read) contain no ERBB4 or NETO2 endpoint.
* Neto2 itself is neuronal, but not through WWOX. Pressey 2017 (**abstract only**): Neto2 increases total KCC2 abundance in cultured mouse hippocampal neurons (quantitative immunofluorescence).
* ERBB4 biology in PV interneurons is background I did not read. My PubMed query returned 2446 mixed records and I opened none. That link is **not checked here**.

## Q3. Functional consequences measured versus claimed
* **WW1-PPxY-ERBB4 in cells.** Aqeilan 2005 (**abstract only**): in HeLa cells co-expressing WWOX and ErbB-4, TPA treatment leaves ErbB-4 retained in the cytoplasm. Endogenous ErbB-4 is retained in MCF-7 cells. WWOX suppresses YAP coactivation of the ErbB4 C-terminal fragment in a dose-dependent manner. Effect sizes and n are not available to me.
  * Direction: WWOX at the motif retains the ErbB4 ICD, so loss predicts more nuclear ICD. This is a cancer-cell result and is not transferred to neurons.
* **Neural WWOX-loss data** (no ERBB4 or NETO2 endpoint in either):
  * Hussain 2019 (full text; full-null mouse, 2 weeks, both sexes, hippocampus): PV+ interneurons fall 44% overall (n = 7 vs 7; DG p < .005, CA1 p < .05). NPY+ cells fall 30% in DG only (n = 6 vs 6, p < .05). GAD65/67 protein falls (n = 5 vs 5, p < .05). Gliosis and Tnf/Il6 rise. Stereology and blots only, no physiology. The authors state cause versus consequence is unresolved.
  * Hussain 2023 (full text; adult P47T homozygous knock-in): protein and mRNA unchanged. Spontaneous generalised seizures on video EEG, n = 3 vs 3 (21 to 53 h). Cerebellar Hcn1+ basket cell number is unchanged and Purkinje cells fall. No hippocampal or cortical interneuron endpoint was reported in the text I read.
* **Claimed only:** that ERBB4 or NETO2 explains the interneuron deficit or the null phenotype. A secondary dossier labels the PPxY route ASSUMED (secondary).

## Q4. Pharmacological lever
**None is interpretable now.**
* The WWOX to ERBB4 to function relation is known only as ICD cytoplasmic retention in cancer cell lines. The sign in neurons is unmeasured.
* A lever on ERBB4 would be a kinase inhibitor or a neuregulin-pathway probe. I read no source on their selectivity or brain action, so I assert no compound class, selectivity or alternative action. Whether to inhibit or activate is undetermined.
* NETO2 has no drug. Its known function (kainate receptor auxiliary subunit; KCC2 abundance per Pressey 2017, abstract) has no demonstrated tie to WWOX.
* Repurposing drug versus probe: nothing reaches a repurposing candidate. At most, tool compounds would serve a mechanistic assay.

## Q5. Not supported
* ERBB4 or NETO2 as WWOX partners in neurons or interneurons, in any species, age, preparation or genotype. NETO2 has no binding evidence anywhere I searched.
* Transfer of the HeLa and MCF-7 sign (WWOX retains ErbB4 ICD) to neurons.
* Transfer of the 2-week full-null PV loss to the adult P47T line: the 2023 text reports no interneuron count.
* Mouse to human. The binding data are human domains and cells, and the scans and neural data are mouse.
* PV-specific loss. A secondary note (not re-checked) says the Pvalb fall is PV-weighted but not PV-specific at transcript level. In Hussain 2019 the PV+ cell counts have no maturation control.
* PPHY binding from the non-canonical motif data (LPxY, PPxF in the Abu-Odeh abstract). That is a different motif.

## Q6. Improve a comparison or generate an experiment
**Other neural partners.** I found no neural WWOX partner shown in a neuron. The only neural evidence is the P47T failure to bind Dvl2 and Wbp1 PPPY peptides in cerebellar lysate. These are the best-supported WW1-PPxY partners in neural tissue, but only as peptides and in cerebellum.

**Kept hypothesis, chain:**
1. Observation: the 2-week full-null hippocampus has fewer PV+ and NPY+ interneurons and lower GAD65/67 (Hussain 2019). WW1 binds ErbB4 PPxY in human cells (abstracts). P47T loses PPPY peptide binding with the protein intact (Hussain 2023).
2. Relation: WWOX WW1 holds ERBB4 through PPxY.
3. Hypothesised action: losing that hold changes ERBB4 localisation or signalling in interneurons.
4. Context: cortical or hippocampal PV interneurons, mouse, about P7 to P21.
5. Pharmacological comparison: none until step 6 is positive. Then ERBB4 probes (a kinase inhibitor and a neuregulin-pathway probe) against vehicle, as tools, in null and P47T slices or cultures. The measured sign decides which probe is the rescue.
6. Prediction: WT WWOX co-precipitates ERBB4 from lysate and P47T does not. In P47T and null neurons the ICD shifts in the same direction.
7. Rejection: P47T and null show no change in ERBB4 binding or localisation (killed). Only the null shows a change, so the protein is needed but not WW1 binding (PPxY route killed). For NETO2: WT WWOX does not pull down the PPHY peptide, with Dvl2 as positive control and a mutated-motif peptide as negative control (killed).

**First experiment (uses the assay already published):** repeat the Hussain 2023 peptide pull-down with the three ERBB4 PPxY peptides and the NETO2 PPHY peptide on wild-type and P47T cortical and hippocampal lysate, with Dvl2 as positive control. Add a co-IP of endogenous ERBB4. Interneuron specificity then needs sorted or cultured neurons.

**No compound is justified yet.** The measurement that would change this is a P47T-versus-wild-type difference in ERBB4 binding or ICD localisation in PV neurons, with a known sign.

## Search perimeter
* PubMed through the MCP tool, 2026-11-19. Queries and hits:
  * `WWOX ERBB4 WW domain PPxY binding` (2)
  * `WWOX NETO2 interaction` (0)
  * `WWOX interactome neurons WW domain partners proteomics` (0)
  * `WWOX PPxY interacting proteins WW1 domain mass spectrometry` (2)
  * `Wwox interneuron ErbB4 neuregulin epilepsy` (0)
  * `ErbB4 PPxY WW domain neurons interneurons interaction YAP Nedd4 Itch` (0)
  * `WWOX WW1 domain neuronal protein interaction ligand brain mouse rat PPPY` (0)
  * `WWOX P47T knock-in mouse epilepsy ataxia` (1)
  * `Wwox null mice GABAergic interneurons parvalbumin hippocampus seizures` (0)
  * `WWOX Syn-Cre OR neuron-specific deletion mice ... heterozygous` (0)
  * `Breton WWOX hyperexcitability neocortical slices burst` (0)
  * Broad queries on neuronal partners (WWOX + tau/ankyrin/synapsin/Dvl/JNK, and PPxY + AMPA/NMDA/kainate) returned off-topic bulk lists and were not opened.
  * Also run: `Neto2 WW domain OR PPxY OR WWOX OR Nedd4 ubiquitin` (mixed hits, none opened), `Neto2 kainate receptor auxiliary subunit KCC2 interaction neurons` (1), `ErbB4 parvalbumin interneurons deletion epilepsy OR hyperexcitability mice` (2446, none opened) and an ErbB4-inhibitor query (mixed, none opened).
* The absence claim "no published WWOX-NETO2 interaction" is limited to PubMed, those queries, up to 2026-11-19, with title and abstract matching only. I did not query BioGRID, IntAct or STRING, Europe PMC full-text search or preprints, so it needs a second route before it is stated as an absence. Breton 2021 was not found by my query and was not read.
* Full texts actually read: Hussain 2018 (Europe PMC XML), Hussain 2019 and Hussain 2023 (PubMed full-text tool). Everything else is abstract-level.

## Pivotal claims
| claim | source | locator | depth |
|---|---|---|---|
| WWOX associates with full-length ErbB-4 via WW1; retains it in cytoplasm (HeLa, MCF-7); suppresses YAP coactivation | Aqeilan 2005, Cancer Res | abstract | abstract only |
| WW1 (not WW2) binds PPxY in ErbB4 ICD; WW2 augments WW1 | Schuchardt 2013, Biochemistry | abstract | abstract only |
| WW2 raises dual-motif ErbB4 peptide affinity about 10-fold | Rotem-Bamberger 2022, J Biol Chem | abstract | abstract only |
| WW1 binds PPxY and LPxY partners (HEK293); ITCH LPxY | Abu-Odeh 2014, J Biol Chem | abstract | abstract only |
| WWOX TAP-MS HEK293T: SEC23IP, SCAMP3, VOPP1 co-IP via WW1; no ERBB4 or NETO2 text | Hussain 2018, Front Oncol | Methods, Results (text search) | full text |
| P47T WWOX loses Dvl2 and Wbp1 PPPY peptide binding in cerebellar lysate; protein and mRNA unchanged | Hussain 2023, Prog Neurobiol | Results (peptide pull-down) | full text |
| P47T adults: spontaneous seizures, video EEG, n = 3 vs 3; cerebellar Hcn1+ basket cells unchanged | Hussain 2023, Prog Neurobiol | Results (seizure and cerebellum sections) | full text |
| Full null at 2 weeks: PV+ -44% hippocampus (n = 7 vs 7), NPY+ -30% DG, GAD65/67 down (n = 5 vs 5) | Hussain 2019, Neurobiol Dis | Results 3.1 to 3.4 | full text |
| Neto2 raises total KCC2 abundance in cultured mouse hippocampal neurons | Pressey 2017, J Biol Chem | abstract | abstract only |
| Mouse Neto2 PPHY 395 and Erbb4 PPIY/PPAY/PPPY by scan; no protein significant (q 0.079) | secondary motif-scan dossier | answer-first 2; ranked table rows | secondary |
| Pvalb transcript fall is PV-weighted, not PV-specific | secondary note | update 2026-11-19 | secondary |

## Limits
* The four binding and neuronal-function papers (Aqeilan, Schuchardt, Rotem-Bamberger, Pressey) plus Abu-Odeh were abstract-only, so Methods (domain species, peptide sequences, Kd values, n) and legends were not read. This is the largest limit on Q1 and Q3.
* Hussain 2019 and 2023 come from one laboratory. The 2019 paper has no physiology and the 2023 EEG has n = 3 per group. The 2023 pull-down was read from text, not from the blot figure.
* I did not source ERBB4 pharmacology or ERBB4-in-PV-interneuron biology, so Q4 says only that no lever is interpretable.
* No dose and no clinical recommendation. Not medical advice.
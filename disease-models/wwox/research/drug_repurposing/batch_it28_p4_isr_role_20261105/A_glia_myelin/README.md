# IT28 P4-A: when is ISR activation protective, and when harmful, in oligodendrocytes, myelin and glia?

Non-canonical research material, not medical advice. Nothing here is a finding about WWOX; `qualified = no` throughout. Batch IT28-P4-A, scientist delegate, 2026-11-05. Zero spend, no registration, no contact address sent to any service. The search was run on the transferable literature (PERK, eIF2alpha, GADD34, eIF2B, myelinating disease models) and did not use the gene name as a keyword. The repo's own ISR evidence was read only as far as the brief states (P47T partial-loss mouse leans ISR up, not significant; human KO organoid ISR set lower; shWWOX progenitors higher; sign unresolved). RNA ISR-target-set changes are kept apart from eIF2alpha-P activity throughout.

Coverage: 13 papers read as PMC full text (parts named in the receipts), 5 abstract-only (marked). Receipts: `receipts/FTR-20261105-<PMID>-04.json` (draft, not recorded). Full text was not available for the founding Popko-lab PERK/EAE papers (PMID 17273557, 23554479) or for three Wrabetz/Pennuto CMT1B papers (18255032, 27807175, 32973043); their direction is used, their readouts are not.

## 1. Short answer

1. "The ISR is protective" or "the ISR is harmful" is not a well-posed statement for an oligodendrocyte-lineage system. Inside one cell type the sign changes with the node that is perturbed: in P0S63del Schwann cells PERK loss helps (P2) while loss of eIF2alpha phosphorylation harms (P3); in Jimpy oligodendrocytes PERK loss helps (J1), an eIF2B activator helps (J5), and prolonging eIF2alpha-P is neutral (J3); in EAE PERK loss harms (H3), ATF4 loss is neutral (A1) and an eIF2B activator removes the benefit of a potentiator (G4).
2. What the models agree on is conditional, not absolute: (a) a transient, extrinsic stress (cytokine, inflammation) in a cell whose folding machinery is otherwise intact: keeping eIF2alpha-P up is protective and removing the input is harmful; (b) a chronic intrinsic cargo (mutant PLP1, mutant P0): the sign depends on whether the translational brake lowers the cargo enough to matter (P0S63del: yes, D2/D3) or the PERK-driven programme itself is lethal or blocks maturation (Jimpy: J1/J5); (c) a lesion in eIF2B itself (VWM): the ISR is locked on and its attenuation corrects the disease (V4), and the ISR-target set can be high without a rise in eIF2alpha-P (V1).
3. Target-set RNA, eIF2alpha-P protein, translation rate and outcome come apart in this literature, in both directions (V1, B1, J6, J12, G1, N1). A claim of "ISR high" or "ISR low" in a WWOX-deficient system is not interpretable until protein eIF2alpha-P/ATF4/CHOP and a per-cell translation readout are measured and a perturbation panel (section 5) has been run.

## 2. What the models show (cause versus compensation)

| Model (genotype, cell type, timing) | Readouts used | Perturbation that separated cause from compensation | Direction | IDs |
|---|---|---|---|---|
| EAE and IFN-gamma, Cnp-Cre oligodendrocyte PERK knockout; adult, disease course | p-eIF2alpha Western (genotype check), CHOP/GADD34 mRNA, clinical score, ASPA+ oligodendrocytes, myelin, axons | Genetic loss of the input kinase (cell-specific) | PERK loss harms in inflammation, no developmental phenotype | H1-H4, L1-L3 |
| EAE, oligodendrocyte-specific ATF4 knockout | ATF4 Western (knockout check), disease score, oligodendrocyte loss, myelin | Loss of the transcription arm | No effect: the benefit of PERK is not through ATF4 (authors propose a translation-linked NF-kB route) | A1-A3 |
| IFN-gamma-stressed differentiating OPCs, EAE, cerebellar slices, with guanabenz or Sephin1 (potentiators) and GADD34 loss | p-eIF2alpha time course (Western), survival, EAE score, remyelinated axons by g-ratio, CD4 counts | Pharmacological and genetic prolongation; ISRIB-class reversal | Prolongation protects; benefit partly reversed by 2BAct; drugs also change T cells | W1-W4, C1-C3, G1-G5 |
| P0S63del Schwann cells (CMT1B), chronic cargo | Western p-eIF2alpha/ATF4, 35S translation, UPR arms, P0 retention, myelination, rotarod | CHOP loss; GADD34 loss; salubrinal; Sephin1; PERK loss (cell-specific); non-phosphorylatable eIF2alpha in Schwann cells | CHOP arm damaging, eIF2alpha-P protective, PERK damaging independent of eIF2alpha-P | D1-D5, S1-S4, P1-P4 |
| Jimpy (mutant Plp1; oligodendrocyte death), chronic cargo | Survival, ASPA/BCAS1/MBP, EM, MAG/MBP blots, bulk RNA ISR sets, primary OPC differentiation | PERK loss (germline het and Olig2-Cre); GADD34 mutant; CHOP null; eIF2B activators (2BAct in vivo, ISRIB in vitro) | PERK loss and eIF2B activation help; GADD34 and CHOP loss do not | J1-J13 |
| VWM (Eif2b5 R191H), eIF2B lesion | ATF4-target mRNA panel, ATF4 and 4E-BP1 Western, p-eIF2alpha Western, single-nucleus signature, proteome, myelin, motor | eIF2B activator 2BAct, long-term | Attenuation prevents pathology; ISR set up with no p-eIF2alpha rise; astrocytes dominate | V1-V7 |
| Cell-specific Eif2b5 mutants (Cnp, astrocyte, neuron Cre) | ATF4-target qPCR and 4E-BP1 blots (bulk cerebellum), oligodendrocyte maturation, cycling, myelination | Cell-specific mutation | Oligodendrocyte mutation causes immaturity and ataxia with a normal bulk ATF4 set | B1-B4 |
| GCN2 knockout, cuprizone | p-eIF2alpha/total eIF2alpha Western, myelin segments, remyelination | Global kinase loss | Impaired remyelination; ratio readout confounded by total eIF2alpha; n = 3 | N1-N4 |
| Human iPSC VWM organoids | ATF4/XBP1s mRNA, ATF6-N/XBP1s protein, cell composition | ISRIB | Reported rescue; weak design (two patient lines; no p-eIF2alpha reported in the text read) | O1-O3 |

### What the perturbations actually tell apart

- **Input loss (kinase knockout) versus level/dwell of eIF2alpha-P versus release of the brake (eIF2B activator) versus the ATF4/CHOP arm are four different experiments.** They are not interchangeable and they gave different signs in the same cell type (Schwann: P2 versus P3; oligodendrocyte: J1/J7 versus J3 versus A1).
- **PERK is not the same as eIF2alpha-P.** In Schwann cells PERK loss helped without lowering ER-stress markers (P2), whereas removing eIF2alpha phosphorylation worsened disease through ERK/c-Jun and delayed differentiation, not ER stress (P3). In Jimpy, PERK deletion rescued oligodendrocyte maturation and cholesterol gene sets while 2BAct, which acts downstream of all eIF2alpha kinases, mainly changed inflammation gene sets (J7). A PERK inhibitor result therefore cannot be read as an ISR result.
- **Epistasis is what establishes ISR-dependence of a drug benefit.** In EAE the potentiator's benefit was shortened by an eIF2B activator (G4, partial: G5). Conversely a drug effect that persists without PPP1R15A and without phosphorylatable eIF2alpha (X2) is not evidence that the ISR carried it.
- **Translation was the missing readout in most papers.** Where it was measured it decided the interpretation: 35S labelling placed GADD34 loss as a deeper brake (D2); a bulk puromycin blot missed an effect that a per-cell OP-puro assay found (G1/G2).
- **A null in one arm is informative only in context.** ATF4 loss null in EAE (A1) tells that arm is not the protective one; it does not say the ISR is irrelevant. CHOP loss was null in Jimpy oligodendrocyte density (J4) but CHOP is anti-apoptotic for another Plp1 allele (J13): allele-specific.

## 3. Evidence ledger (verbatim locators)

Every quote below was machine-checked as a substring of the text fetched for this batch (whitespace and hyphen variants normalised). `Locator` is the section path of the fetched PMC XML (or the PubMed abstract). Papers marked ABSTRACT ONLY could not be fetched as full text (publisher does not allow XML download through PMC; Europe PMC returned an error) and are used for direction only, never for readout details.

### Jimpy PMD, Nat Commun 2025 - PMID 41453885 / PMC12868624
Integrated stress response inhibition prolongs the lifespan of a Pelizaeus-Merzbacher disease mouse model by increasing oligodendrocyte survival. Nat Commun 2025; PMID 41453885; DOI 10.1038/s41467-025-68045-0. Full text, read in the parts quoted.

| ID | Proposition | Locator | Verbatim quote |
|---|---|---|---|
| J1 | Oligodendrocyte-lineage PERK loss extends Jimpy (mutant Plp1) lifespan | Results > Perk inactivation increases Jimpy oligodendrocyte survival, CNS myelination, and lifespan | "The Jimpy; Perkfl/fl; Olig2-Cre animals lived ~2 weeks longer than the Jimpy; Perkfl/fl mice (Fig. 1a, b), suggesting that PERK activity is detrimental to Jimpy mice." |
| J2 | The myelin rescue by PERK loss is small in absolute terms | Results > Perk inactivation ... (EM paragraph) | "though reaching only ~10% of the axons myelinated in WT mice" |
| J3 | Prolonging eIF2a-P genetically (GADD34 C-terminal mutant) does not worsen or rescue Jimpy lifespan | Results > Downstream ISR inactivation fails to correct Jimpy oligodendrocyte deficits | "The lifespan of Jimpy;Gadd34 mutants (Jimpy; Gadd34ΔC/ΔC) was indistinguishable from that of Jimpy;Gadd heterozygous" |
| J4 | CHOP deletion does not rescue Jimpy oligodendrocytes | Results > Downstream ISR inactivation fails to correct Jimpy oligodendrocyte deficits | "However, there was no increase in the density of oligodendrocytes in Jimpy mice when CHOP was deleted (Supplementary Fig. 4d, e)." |
| J5 | An eIF2B activator (2BAct), acting downstream of eIF2a-P, extends Jimpy lifespan | Results > Pharmacological ISR attenuation increases Jimpy myelination and lifespan | "survived approximately twice as long as Jimpy mice on the control diet" |
| J6 | In the model whose ISR is called harmful, the bulk ER-stress/UPR RNA readout did not itself show the stress | Results > RNAseq pathways: Perk rescues myelination whereas 2BAct targets inflammation | "Notably, we did not observe significant changes in the ER stress pathways and UPR response in Jimpy mice, perhaps because so few oligodendrocytes remain at this stage." |
| J7 | PERK loss and eIF2B activation, both ISR-lowering, do not give the same oligodendrocyte maturation outcome | Results > RNAseq pathways ... (2BAct) | "However, unlike the oligodendrocyte-specific PERK mutant, 2BAct did not rescue the gene sets associated with oligodendrocytes, glial cell differentiation, or cholesterol homeostasis" |
| J8 | Primary Jimpy OPC cultures with ISRIB: cell-autonomous effect (WT cultures unchanged) | Results > ISR inhibition promotes Jimpy oligodendrocyte maturation in vitro | "These data demonstrate a cell-autonomous impact of ISR inhibition on oligodendrocyte differentiation and survival." |
| J9 | The authors' own context rule: transient inflammatory stress versus chronic cargo stress | Discussion | "Inflammation creates a relative mild and usually transient cytotoxic environment, against which the ISR can provide short-term protection." |
| J10 | Authors' mechanism statement for the chronic-cargo case (interpretation, not a measurement) | Discussion | "mutations in the abundantly expressed Plp1 gene result in a continuous source of improperly folded mutant proteins in the ER that activates a maladaptive UPR" |
| J11 | The authors flag that an MBP readout in this model may not be myelin | Discussion | "This suggests that the increased MBP immunoreactivity observed in Jimpy animals with a reduced ISR response may not exclusively reflect enhanced myelination." |
| J12 | The Western blots listed use only myelin proteins; no eIF2a-P, ATF4 or CHOP protein antibody is listed, so the ISR state in Jimpy rests on RNA sets and genetics | Methods > Western-blot | "anti-MBP (1:1000; # 808403, BioLegend), anti-MAG (1:1000; #346200, Invitrogen), and anti-β-actin" |
| J13 | The sign of the CHOP arm depends on the Plp1 allele | Discussion | "A previous study showed that CHOP has an anti-apoptotic impact on oligodendrocytes that express a distinct mutant Plp1 allele" |

### OL-PERK cKO, Glia 2014 - PMID 24481666 / PMC6342275
Genetic inactivation of PERK signaling in mouse oligodendrocytes: normal developmental myelination with increased susceptibility to inflammatory demyelination. Glia 2014; PMID 24481666; DOI 10.1002/glia.22634. Full text, read in the parts quoted.

| ID | Proposition | Locator | Verbatim quote |
|---|---|---|---|
| H1 | Protein-level readout (p-eIF2a) used to verify the genotype lowered ISR input | Results > Generation of OL-PERKko/ko mice. | "reduced expression of PERK and phosphorylated eIF2α (p-eIF2α) in the brains of OL-PERKko/ko mice when compared to control PERKflox/flox mice" |
| H2 | PERK is dispensable for developmental myelination (Cnp-Cre) | Results > Inactivation of Perk in OLs is not detrimental to OLs and myelin integrity. | "Collectively, these data indicate that the deletion of Perk from OLs does not affect OL development or myelin synthesis." |
| H3 | Under inflammatory demyelination, loss of PERK in oligodendrocytes worsens disease (control maximum 2.7 in the same sentence) | Results > Deletion of Perk in OLs worsens the EAE disease course. | "PERKko/ko mice displayed a higher clinical score that reached a mean maximum of 3.7 (Fig. 4A)" |
| H4 | The harm of PERK loss is not through the immune response | Results > OL-PERKko/ko mice experiencing EAE display an increased loss of OLs without a detectable effect on the inflammatory response. | "the deletion of Perk specifically in OLs has no significant effect on T cell infiltration or microglia/macrophage activation" |
| H5 | PERK is essential outside oligodendrocytes (systemic PERK inhibition is not cell-type specific) | Results > Generation of OL-PERKko/ko mice. | "Because Perk null mice die from pancreatic and liver insufficiency early in life" |

### OL-ATF4 cKO EAE, J Neuroinflammation 2019 - PMID 30709400 / PMC6357515
Oligodendrocyte-specific ATF4 inactivation does not influence the development of EAE. J Neuroinflammation 2019; PMID 30709400; DOI 10.1186/s12974-019-1415-6. Full text, read in the parts quoted.

| ID | Proposition | Locator | Verbatim quote |
|---|---|---|---|
| A1 | ATF4 is induced but dispensable in EAE; the protective arm is not ATF4 | Discussion | "Although we demonstrated that the activity of ATF4 was significantly enhanced in oligodendrocytes during EAE, it was very surprising to find that ATF4 inactivation specifically in oligodendrocytes did not affect the disease severity or inflammation" |
| A2 | ATF4 is dispensable in unstressed oligodendrocyte-lineage cells (Cnp-Cre) | Results > ATF4 was dispensable for oligodendrocytes under normal conditions | "ATF4 cKO mice did not display any neurological phenotypes and were indistinguishable from littermate control mice." |
| A3 | A translation-linked, ATF4-independent route is the authors' candidate for the protection | Discussion | "the PERK-eIF2α pathway also activates the transcription factor NF-κB by repressing the translation of the NF-κB inhibitor IκBα" |

### Guanabenz EAE, Nat Commun 2015 - PMID 25766071 / PMC4360920
Pharmaceutical integrated stress response enhancement protects oligodendrocytes and provides a potential multiple sclerosis therapeutic. Nat Commun 2015; PMID 25766071; DOI 10.1038/ncomms7532. Full text, read in the parts quoted.

| ID | Proposition | Locator | Verbatim quote |
|---|---|---|---|
| W1 | Protein p-eIF2a time course shows persistence under guanabenz in IFN-g-stressed differentiating OPCs | Results > Guanabenz protects oligodendrocytes against IFN-γ | "By 20 h, however, p-eIF2α expression had significantly decreased in dOPCs treated only with IFN-γ but remained high in cells treated with IFN-γ+5.0 μM guanabenz (P=0.043, unpaired t-test)." |
| W2 | In EAE the drug also changes T cells, so the EAE benefit is not cell-autonomous proof | Results > Guanabenz alters the number of activated CD4+ cells in EAE | "guanabenz treatment results in both a decrease in the number of activated CD4+ T cells and an increase in the number of dead CD4+ T cells in the CNS while protecting mature oligodendrocytes" |
| W3 | Authors name the cost of prolongation | Discussion | "Sustained translational repression, due to prolonged eIF2α phosphorylation, could prove detrimental to myelinating cells." |
| W4 | Remyelination was not tested in this paper | Discussion | "Although this study does not directly address the impact of an enhanced ISR response on remyelination" |

### Prolonging ISR remyelination, eLife 2021 - PMID 33752802 / PMC7987340
Prolonging the integrated stress response enhances CNS remyelination in an inflammatory environment. Elife 2021; PMID 33752802; DOI 10.7554/eLife.65469. Full text, read in the parts quoted.

| ID | Proposition | Locator | Verbatim quote |
|---|---|---|---|
| C1 | The remyelination benefit comes from global GADD34 mutation / drug, not oligodendrocyte-specific manipulation | Discussion | "The genetic and pharmacologic approaches used here to modulate the ISR do not target specific cell types in the CNS." |
| C2 | Prolongation acts on survival of myelinating cells, not OPC proliferation, in this setting | Discussion | "prolonging the ISR by the Gadd34 mutation or by Sephin1 treatment did not alter the number of proliferating OPCs in the presence of inflammation" |
| C3 | Prolongation started at disease peak increased the g-ratio-defined remyelinated axons | Results > Sephin1 treatment enhances remyelination in late-stage EAE | "the density of remyelinated axons (g > 0.8) was significantly higher in EAE mice treated with Sephin1 than those treated with vehicle" |

### Sephin1/BZA mechanism, Glia 2023 - PMID 37203250 / PMC10681276
Insights into the mechanism of oligodendrocyte protection and remyelination enhancement by the integrated stress response. Glia 2023; PMID 37203250; DOI 10.1002/glia.24386. Full text, read in the parts quoted.

| ID | Proposition | Locator | Verbatim quote |
|---|---|---|---|
| G1 | A bulk puromycin Western blot missed the translation effect of a mild ISR | Results > eIF2α phosphorylation induction by IFN-γ results in mild protein synthesis inhibition in oligodendrocytes | "Surprisingly, Western blot analysis did not reveal any changes in protein synthesis in IFN-γ treated oligodendrocytes" |
| G2 | A per-cell OP-puro assay did detect the mild translation reduction | Results > Sephin1 induces translation reduction in IFN-γ stressed oligodendrocytes ... | "Of note, using the sensitive OP-puro assay, we observed a reduction of fluorescent intensity in IFN-γ (****p<0.0001)" |
| G3 | In the protective inflammatory case the ATF4 protein did not rise significantly | Results > Sephin1 induces translation reduction in IFN-γ stressed oligodendrocytes ... | "Although there was not a significant increase in ATF4 expression, the levels of GADD34 were increased after 24 hours of Sephin1 treatment in IFN-γ stressed oligodendrocytes" |
| G4 | Epistasis: an eIF2B activator removes the benefit of the potentiator (ISR-dependence of the benefit) | Results > eIF2B activators counteract the effect of Sephin1 on IFN-γ stressed oligodendrocytes and on EAE | "Sephin1 treated mice fed chow containing 2BAct developed EAE symptoms significantly faster than those on normal chow" |
| G5 | The reversal was partial | Results > eIF2B activators counteract the effect of Sephin1 ... | "although the beneficial impact of Sephin1 was not completely abrogated by 2BAct" |
| G6 | Oligodendrocytes under a mild IFN-g ISR still respond to a second (thapsigargin) stressor: capacity challenge is feasible | Results > eIF2α phosphorylation induction by IFN-γ results in mild protein synthesis inhibition in oligodendrocytes | "We found that TG was still capable of inducing eIF2α phosphorylation and reducing protein synthesis in the presence of IFN-γ" |

### GCN2 remyelination, Int J Mol Sci 2025 - PMID 40004088 / PMC11855834
GCN2-Mediated eIF2α Phosphorylation Is Required for Central Nervous System Remyelination. Int J Mol Sci 2025; PMID 40004088; DOI 10.3390/ijms26041626. Full text, read in the parts quoted.

| ID | Proposition | Locator | Verbatim quote |
|---|---|---|---|
| N1 | The p-eIF2a/total ratio moved because the denominator (total eIF2a) moved; ratio readouts need the total reported | Results > 2.3. GCN2 Is Necessary for eIF2α Recovery and Phosphorylation During Remyelination | "showed a decrease in p-eIF2α levels after the cuprizone challenge, and those levels were maintained after the removal of the drug. This result is probably due to the changes observed in eIF2α total levels" |
| N2 | GCN2 contributes to basal p-eIF2a in brain and is needed for remyelination (global KO) | Results > 2.3 ... | "Under basal conditions, lower levels of eIF2α phosphorylation were found in GCN2-deficient mice compared to WT mice (Figure 4A)." |
| N3 | Group size three | Methods > 4.3. Tissue Processing for Immunofluorescence | "Two groups of male WT (n = 3) or GC" |
| N4 | Authors' own limitation | Discussion | "Limitations of our study include the small sample size" |

### Gadd34 CMT1B, J Exp Med 2013 - PMID 23547100 / PMC3620355
Resetting translational homeostasis restores myelination in Charcot-Marie-Tooth disease type 1B mice. J Exp Med 2013; PMID 23547100; DOI 10.1084/jem.20122005. Full text, read in the parts quoted.

| ID | Proposition | Locator | Verbatim quote |
|---|---|---|---|
| D1 | CHOP loss (rescuing) went with higher, longer p-eIF2a (via less GADD34), measured by Western | Results > Genes rescued in S63del/Chop-null mice | "resulted in a sustained up-regulation of eIF2α phosphorylation compared with S63del" |
| D2 | Translation was measured directly (35S labeling): GADD34 loss deepened the translational brake | Results > Inactivation of Gadd34 limits reactivation of translation in S63del nerves | "Metabolic labeling of total protein showed a ∼20% reduction in S63del, and a more pronounced 35–40% reduction in S63del/Gadd34Δc/Δc as compared with WT nerves" |
| D3 | A deeper eIF2a-P brake lowered cargo and the whole UPR (protective by reducing load) | Results > Inactivation of Gadd34 limits reactivation of translation in S63del nerves | "all three arms of the UPR (Ron and Walter, 2007) are less active, consistent with a general reduction in ER stress in S63del nerves lacking Gadd34 activity" |
| D4 | Potentiation has an on-target cost in healthy myelinating cultures (concentration window) | Results > eIF2α phosphorylation as a therapeutic target | "treatment of WT DRG cultures with salubrinal reduced myelination" |
| D5 | In P0S63del Schwann cells the CHOP arm is damaging, yet more eIF2a-P is protective | Discussion | "indicating that the PERK/CHOP arm of the UPR is pathogenetic in this context" |

### Sephin1, Science 2015 - PMID 25859045 / PMC4490275
Preventing proteostasis diseases by selective inhibition of a phosphatase regulatory subunit. Science 2015; PMID 25859045; DOI 10.1126/science.aaa4484. Full text, read in the parts quoted.

| ID | Proposition | Locator | Verbatim quote |
|---|---|---|---|
| S1 | Authors' framing of the CMT1B cargo problem | Main text, paragraph on CMT1B | "MPZmutant causes CMT1B by a gain of toxic property associated with pathological signaling through CHOP and PPP1R15A" |
| S2 | Mechanistic claim measured in cells (p-eIF2a Western, translation) | Main text, paragraph on Sephin1 selectivity | "Sephin1 prolonged eIF2α phosphorylation after stress (Fig. 1D), delaying translation recovery (Fig. 1E)." |
| S3 | Claimed stress-dependence of the potentiator | Main text, paragraph on Sephin1 selectivity | "In the absence of stress, Sephin1 did not affect eIF2α signaling (fig. S2)" |
| S4 | Guanabenz has a major off-target pharmacology; Sephin1 was derived to avoid it | Main text, introduction | "In vivo, GBZ cannot be used to selectively inhibit PPP1R15A because it is a centrally active hypotensive drug with nanomolar affinity for the α2-adrenergic receptor" |

### Sephin1/guanabenz inert in vitro, eLife 2017 - PMID 28447936 / PMC5429092
PPP1R15A-mediated dephosphorylation of eIF2α is unaffected by Sephin1 or Guanabenz. Elife 2017; PMID 28447936; DOI 10.7554/eLife.26109. Full text, read in the parts quoted.

| ID | Proposition | Locator | Verbatim quote |
|---|---|---|---|
| X1 | The proposed target mechanism of guanabenz/Sephin1 is contested by an independent in vitro reconstitution | Abstract | "Surprisingly, they proved inert in vitro affecting neither stability of the PP1-PPP1R15A complex nor substrate-specific dephosphorylation." |
| X2 | An effect of Sephin1 persisted without PPP1R15A and without phosphorylatable eIF2a, so a benefit under Sephin1 is not proof of ISR potentiation | Abstract | "However, repression was noted in both wildtype and Ppp1r15a deleted cells and in cells rendered ISR-deficient by CRISPR editing of the Eif2s1 locus to encode a non-phosphorylatable eIF2α (eIF2αS51A)." |

### 2BAct VWM mouse, eLife 2019 - PMID 30624206 / PMC6326728
eIF2B activator prevents neurological defects caused by a chronic integrated stress response. Elife 2019; PMID 30624206; DOI 10.7554/eLife.42940. Full text, read in the parts quoted.

| ID | Proposition | Locator | Verbatim quote |
|---|---|---|---|
| V1 | In a mouse whose ATF4-target set is high, eIF2a-P was not raised: target-set RNA and eIF2a-P come apart | Results > A chronic ISR in the CNS of VWM mice is prevented by 2BAct | "we did not detect an increase in eIF2α phosphorylation in R191H brains." |
| V2 | ISR readout is stage dependent (absent at P14) | Results > A chronic ISR in the CNS of VWM mice is prevented by 2BAct | "Interestingly, we did not observe ISR induction in R191H mice at postnatal day 14" |
| V3 | Temporal order: ISR-set induction before pathology | Results > A chronic ISR in the CNS of VWM mice is prevented by 2BAct | "Activation of this stress response preceded the appearance of pathology (myelin loss, gliosis and motor deficits) in VWM mice." |
| V4 | Pharmacological ISR attenuation prevents pathology when the lesion sits in eIF2B itself | Abstract | "Remarkably, long-term treatment with a small molecule eIF2B activator, 2BAct, prevents all measures of pathology and normalizes the transcriptome and proteome of VWM mice." |
| V5 | Cell-type assignment of the ISR set was by single-nucleus signature, mostly astrocytes | Results > The ISR is activated in astrocytes and myelinating oligodendrocytes of R191H mice | "For the first time, our work provides in vivo evidence that in VWM mice, astrocytes exhibit a molecular signature of an early maladaptive ISR." |
| V6 | Oligodendrocytes show a smaller ISR-set enrichment | Results > The ISR is activated in astrocytes and myelinating oligodendrocytes of R191H mice | "Interestingly, the comparison of R191H to WT cerebellum also revealed significant enrichment of the ISR signature in other non-neuronal cell types, including myelinating oligodendrocytes" |
| V7 | A locked-on ISR can still be raised by an added stressor: baseline versus inducible capacity are separable | Discussion | "However, the system can still respond to further stress" |

### Cell-specific Eif2b5, Brain 2025 - PMID 40326783 / PMC12588717
Cell-specific Eif2b5 mutant mice: novel insights into roles of macroglia in vanishing white matter. Brain 2025; PMID 40326783; DOI 10.1093/brain/awaf171. Full text, read in the parts quoted.

| ID | Proposition | Locator | Verbatim quote |
|---|---|---|---|
| B1 | Oligodendrocyte-specific eIF2B mutation gives oligodendrocyte pathology with a normal bulk ATF4-target readout | Discussion | "Interestingly, the expression of the ATF4 transcriptome is completely normal in the brains of Cnp-2b5ho animals." |
| B2 | The oligodendrocyte-lineage phenotype is immaturity/cycling, not death | Results > Oligodendrocytes | "Cnp-2b5ho mice had a higher percentage of Ki67+ oligodendrocytes than controls (70.49% ± 8.82% versus 20.71% ± 0.34%; P < 0.0001)" |
| B3 | No apoptosis in the oligodendrocyte-specific mutant | Results > Oligodendrocytes | "Cell death was not detected in any Cnp-2b5ho animal" |
| B4 | Assay discordance for an ISR-target protein inside one model | Results > ATF4 transcriptome | "Given the contradictory results between 4E-BP1 immunostaining, western blot and qPCR" |

### ISRIB VWM organoids, CNS Neurosci Ther 2025 - PMID 40296303 / PMC12037694
Effects of the Small-Molecule ISRIB on the Rapid and Efficient Myelination of Oligodendrocytes in Human Stem Cell-Derived Cerebral Organoids in Patients With Leukoencephalopathy With Vanishing White Matter. CNS Neurosci Ther 2025; PMID 40296303; DOI 10.1111/cns.70398. Full text, read in the parts quoted.

| ID | Proposition | Locator | Verbatim quote |
|---|---|---|---|
| O1 | Human iPSC organoids: UPR/ATF4 mRNA up, ATF6-N and XBP1-S protein up (no p-eIF2a reported in the text read) | Results > Hyperactivation of the UPR Signaling Pathway in Mutant OL Brain Organoids | "These results all indicated that all 3 arms of the UPR were overactivated in mutant brain organoids in VWM" |
| O2 | Claim that an eIF2B activator lowers IRE1/ATF6 readouts is outside the known ISRIB mechanism; low weight | Results > ISRIB Treatment Inhibited the Overactivation of UPR Pathway in Mutant Organoids | "Cumulatively, the evidence suggests that ISRIB functions as an inhibitor of the UPR signaling pathway." |
| O3 | Authors' own limitation (two patient lines, two controls) | Discussion | "the small sample size may reduce the representability of research results to some extent" |

### IFN-gamma/PERK EAE, J Clin Invest 2007 - PMID 17273557 / PMC1783809 - ABSTRACT ONLY
The integrated stress response prevents demyelination by protecting oligodendrocytes against immune-mediated damage. J Clin Invest 2007; PMID 17273557; DOI 10.1172/JCI29571.

| ID | Proposition | Locator | Verbatim quote |
|---|---|---|---|
| L1 | Abstract only. IFN-g given before EAE onset protected through PERK; PERK-deficient animals lost the benefit | Abstract | "The beneficial effects of IFN-gamma were accompanied by PERK activation in oligodendrocytes and were abrogated in PERK-deficient animals." |

### Oligodendrocyte PERK activation EAE, J Neurosci 2013 - PMID 23554479 / PMC3654380 - ABSTRACT ONLY
Oligodendrocyte-specific activation of PERK signaling protects mice against experimental autoimmune encephalomyelitis. J Neurosci 2013; PMID 23554479; DOI 10.1523/JNEUROSCI.1636-12.2013.

| ID | Proposition | Locator | Verbatim quote |
|---|---|---|---|
| L2 | Abstract only. Inducible oligodendrocyte-specific PERK activation without ER stress is tolerated in adults | Abstract | "We demonstrated that persistent activation of PERK signaling was not deleterious to oligodendrocyte viability or the myelin of adult animals." |
| L3 | Abstract only. Gain-of-function protects in EAE (oligodendrocyte-specific) | Abstract | "enhanced activation of PERK signaling specifically in oligodendrocytes significantly attenuated EAE disease severity" |

### CHOP ablation CMT1B, Neuron 2008 - PMID 18255032 / PMC2267889 - ABSTRACT ONLY
Ablation of the UPR-mediator CHOP restores motor function and reduces demyelination in Charcot-Marie-Tooth 1B mice. Neuron 2008; PMID 18255032; DOI 10.1016/j.neuron.2007.12.021.

| ID | Proposition | Locator | Verbatim quote |
|---|---|---|---|
| P1 | Abstract only. CHOP loss rescues CMT1B despite limited apoptosis | Abstract | "Nonetheless, Chop ablation in S63del mice completely rescues their motor deficit and reduces active demyelination 2-fold." |
| P5 | Abstract only. UPR/CHOP track mutant-cargo level and are reversible (dose-response design) | Abstract | "UPR activation and CHOP expression respond dynamically to P0S63del levels and are reversible but are associated with only limited apoptosis of Schwann cells." |

### Perk ablation in Schwann cells, J Neurosci 2016 - PMID 27807175 / PMC5148247 - ABSTRACT ONLY
Ablation of Perk in Schwann Cells Improves Myelination in the S63del Charcot-Marie-Tooth 1B Mouse. J Neurosci 2016; PMID 27807175; DOI 10.1523/JNEUROSCI.1637-16.2016.

| ID | Proposition | Locator | Verbatim quote |
|---|---|---|---|
| P2 | Abstract only. PERK loss helps CMT1B Schwann cells without lowering ER-stress markers | Abstract | "Perk loss of function in Schwann cells restores myelination without diminishing accumulation of P0 or markers of ER stress, suggesting that Perk may modulate myelination through a pathway independent of the UPR." |

### eIF2a phosphorylation in CMT1B Schwann cells, J Neurosci 2020 - PMID 32973043 / PMC7574653 - ABSTRACT ONLY
Phosphorylation of eIF2α Promotes Schwann Cell Differentiation and Myelination in CMT1B Mice with Activated UPR. J Neurosci 2020; PMID 32973043; DOI 10.1523/JNEUROSCI.0957-20.2020.

| ID | Proposition | Locator | Verbatim quote |
|---|---|---|---|
| P3 | Abstract only. Non-phosphorylatable eIF2a in Schwann cells worsens CMT1B: eIF2a-P itself is protective while PERK is harmful | Abstract | "Morphologic and electrophysiological analysis of male and female S63del mice showed a worsening of the neuropathy in the absence of eIF2α phosphorylation." |
| P4 | Abstract only. The protection of eIF2a-P ran through ERK/c-Jun and differentiation, not ER stress | Abstract | "we did not detect significant changes in ER stress levels, but rather a dramatic increase of the MEK/ERK/c-Jun pathway accompanied by a reduction in expression of myelin genes and a delay in Schwann cell differentiation" |


## 4. Decision rule (transferable) and what is model-specific

### 4.1 The rule

State the ISR role per node, never as one sign. For an oligodendrocyte-lineage system with an ISR readout:

1. **Fix the stress class** before interpreting a sign:
   - class T: transient, extrinsic stress, intact folding capacity (cytokine, inflammatory demyelination). Prior from H3, A1, G4, C3: eIF2alpha-P dwell is protective, input loss harmful, ATF4/CHOP not the effector.
   - class C: chronic intrinsic cargo (mutant PLP1, mutant P0). Prior: not fixed. P0S63del favours a deeper brake (D2, D3, P3); Jimpy favours lower PERK-driven output and a released brake (J1, J5) with the brake-deepening arm neutral (J3).
   - class E: lesion in the translation machinery (eIF2B). Prior: ISR output is the disease driver; attenuation corrects (V4); the eIF2alpha-P level is not the guide (V1).
2. **Call the ISR protective compensation only if all hold:** the ISR is raised at protein level (p-eIF2alpha/total, ATF4, per-cell translation); lowering the input or releasing the brake (kinase loss, eIF2B activator, non-phosphorylatable eIF2alpha) worsens survival, maturation or myelination; prolonging eIF2alpha-P (GADD34/PPP1R15A loss) rescues or is neutral; and the benefit of prolongation is lost when the brake is released.
3. **Call it a contributor to damage only if all hold:** raised at protein level; lowering the input or releasing the brake rescues, and the rescue size tracks the fall in the ISR readout; prolonging eIF2alpha-P does not rescue (neutral or worse). The ATF4/CHOP arm must be tested separately and may be neutral even when the ISR is damaging (J4).
4. **Call it a downstream consequence or marker** if the ISR readout is raised but no arm of the panel (both directions, adequately powered, with an equivalence margin) changes the outcome. In this literature that was the status of ATF4 in EAE (A1) and CHOP in Jimpy (J4), not of the ISR as a whole.
5. **Mixed** (nodes pointing opposite ways, as in CMT1B) is a valid result and must be reported as node-specific: protective eIF2alpha-P with damaging PERK or CHOP.
6. **ISR low** is a separate hypothesis, not the mirror of "high": it predicts that adding a stressor still raises eIF2alpha-P (capacity is intact: V7, G6) and that potentiation helps; a flat response to a challenge predicts an ISR-capacity defect.

### 4.2 What transfers and what is model-specific

| Transfers across the models read | Specific to the model (do not carry over) |
|---|---|
| The node-resolved logic and the epistasis design (G4) | The size and sign of the PERK effect (EAE harm, Jimpy benefit, CMT1B benefit) |
| eIF2alpha-P protein and translation are separate from target-set RNA (V1, B1, J6, G1) | ATF4 dispensability (EAE only; A1) |
| Readout timing matters: ISR absent at P14 and present later in VWM (V2); transient in cells (W1) | CHOP sign: allele-specific (J13) |
| Ratio readouts need the denominator reported (N1) | Astrocyte-dominant ISR in VWM (V5) |
| Cre-driver or cell-type assignment decides the interpretation (B1, C1) | Immune side-effects of potentiators in EAE (W2); a developmental hypomyelination model is not an inflammatory model |
| Potentiator mechanism and dose window are model-dependent (D4, S4, X1, X2) | P0S63del Schwann cell translation-reactivation story (D2): peripheral nerve, one protein |

## 5. Measures that discriminate "protective compensation" from "contributes to damage" in a WWOX-deficient oligodendrocyte-lineage system

Not an experiment proposal with doses; an outline of the information needed. Systems: human iPSC-derived OPC to oligodendrocyte cultures or myelinating co-culture, isogenic control, plus a WWOX dose series (partial and full loss; re-expression) because the one dose-resolved design in the literature (UPR and CHOP tracked mutant P0 level and were reversible, P5) is what shows reversibility and dependence.

1. **Readouts, all stage-resolved** (OPC, premyelinating BCAS1-type, MBP-positive; the ISR was absent at P14 and present later in VWM, V2): p-eIF2alpha/total eIF2alpha, same membrane or single-cell immunofluorescence, with total reported (N1); ATF4 and CHOP protein; per-cell translation by OP-puro, not only a bulk blot (G1/G2); the RNA ISR set as a secondary column only. An inducibility challenge with a second stressor to separate low baseline from low capacity (V7, G6).
2. **Perturbation panel, run in parallel in the same batch:** (a) release the brake (eIF2B activator); (b) remove the input (PERK, and separately the other eIF2alpha kinases, since GCN2 contributes to p-eIF2alpha in brain, N2, and the active kinase in a WWOX context is unknown); (c) prolong eIF2alpha-P genetically (PPP1R15A loss) and, as the decisive loss-of-function, a non-phosphorylatable eIF2alpha (the Schwann-cell design, P3); (d) ATF4 and CHOP loss; (e) epistasis: does (a) remove the benefit of (c)?
3. **Outcomes:** survival (cleaved caspase), maturation (MBP-positive fraction over days), myelin or ensheathment, cholesterol-gene output if bulk RNA is taken (J7).
4. **Prediction table, fixed before the run:**

| Result | Reading |
|---|---|
| Protein ISR up; (a), (b) or (c-S51A) worsens outcome; (c-PPP1R15A) rescues; (e) cancels the rescue | Protective compensation |
| Protein ISR up; (a) or (b) rescues in proportion to the readout fall; (c) neutral or worse | Contributes to damage (kinase-specific if (b) differs from (a)) |
| (b) rescues but (c-S51A) harms | PERK acts outside eIF2alpha-P: do not call it an ISR effect (P2, P3) |
| Protein ISR up; every arm null with an equivalence margin | Downstream consequence or marker |
| Protein ISR not up although RNA set up (or reverse) | Readout artefact or an eIF2B-type mechanism (V1); do not classify |
| Protein ISR low and a challenge raises it; (c) rescues | ISR-too-low, potentiation sensible |

## 6. Implication for the lever choices

- **Attenuators (eIF2B activators, the ISRIB and 2BAct class)** act downstream of every eIF2alpha kinase, so they are agnostic to which kinase is active and do not depend on PERK being the cause. The evidence for benefit is in a chronic-cargo model with oligodendrocyte death (J5, J8) and in an eIF2B lesion (V4); in Jimpy they did not reproduce the PERK-loss effect on maturation (J7). Sensible only if the protein-level ISR is shown high and eIF2alpha-P-dependent in the WWOX system. The human organoid report (O1-O3) is too weak to weigh.
- **PERK inhibitors** are the least interpretable lever in this lineage: PERK is dispensable for development in oligodendrocytes (H2), harmful to lose in inflammation (H3), has eIF2alpha-P-independent actions (P2), and is essential elsewhere (H5). Reasonable as an in-vitro probe of the node, not as an ISR proxy.
- **Potentiators (guanabenz, Sephin1, salubrinal)**: protective evidence is confined to inflammatory demyelination (W1, C3) and the P0S63del cargo case (D2, S2). Their target mechanism is contested (X1, X2), guanabenz is an alpha-2 agonist (S4), salubrinal reduced myelination in healthy cultures (D4), and in EAE they also change T cells (W2). A compound benefit counts as ISR-dependent only if it is lost under eIF2B activation and absent in phosphorylation-dead cells. The clean potentiator is genetic (PPP1R15A loss).
- **Choice before data:** none of the three classes is sensible to prefer until section 5 has been run; the model that would justify potentiation (class T, inflammatory) differs from the WWOX phenotype of hypomyelination and maturation delay, which sits nearer to class C or the OPC-immaturity phenotype of the Cnp eIF2B mutant (B2, B3), where attenuation or no ISR link are the live alternatives.

## 7. Not determinable from what was read

- Whether the WWOX-deficient oligodendrocyte-lineage ISR runs high or low, and its sign; nothing here measures that.
- Which eIF2alpha kinase would be active; the literature read has PERK (H, J, P), GCN2 (N), and none of PKR or HRI for oligodendrocytes.
- Whether results in an inflammatory model (EAE, IFN-gamma) transfer to developmental hypomyelination: no paper read tests both in one genotype.
- Cell-autonomy of the potentiator benefit in vivo (C1: the manipulations are global; W2: T-cell effects).
- The mechanism of guanabenz and Sephin1 (X1/X2 contradict the original model; a rebuttal paper exists, PMID 29618508 by title only, not read).
- Human oligodendrocyte data other than the weak organoid report (O1-O3); a hiPSC PMD PERK-inhibitor study cited in the Jimpy paper (J discussion) was not read.
- Readout detail of the five abstract-only papers (PMID 17273557, 23554479, 18255032, 27807175, 32973043).
- Not read at all: the 2026 Lancet Neurol guanabenz VWM trial (PMID 42586097, title only), eIF2B activator clinical-stage reports (e.g. PMID 39287504, title only).

## 8. Files

- `README.md` (this file)
- `receipts/FTR-20261105-<PMID>-04.json`: 13 draft receipts (PMIDs 41453885, 24481666, 30709400, 25766071, 33752802, 37203250, 40004088, 23547100, 25859045, 28447936, 30624206, 40326783, 40296303); not recorded in the ledger.

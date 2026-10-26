# Condition C answer (local WWOX material + live external services)

Not medical advice. Research framing only; no dose or treatment statement. Depth tags: [FT-local] = local registry/manifest record whose own text states a complete full-text read by a prior reader (I re-read the record, not the paper); [ABS] = PubMed abstract I retrieved; [DB] = database row I retrieved live.

Cross-cutting facts (all cases)
- Open Targets (api 26.9.0 / data 26.09) [DB]: WWOX (ENSG00000186153) is associated with "developmental and epileptic encephalopathy, 28" (MONDO_0014533) with genetic_association, animal_model and literature evidence. This only confirms the gene-disease link. It says nothing about any of the interventions.
- PubTator 3 [DB]: WWOX relations are dominated by neoplasm records. Epilepsy 27 publications and seizures 16 are associations only. No treat relation was returned for any of the five interventions.
- DGIdb [DB]: WWOX has only 3 oncology-type interactions (gemcitabine, sorafenib, a recombinant TNF-family protein). No interaction to any of the five interventions.
- The single most relevant recent WWOX source for C1-C4 is Lucas-Clarke 2026, PMID 42909904 (Brain Commun). It is a Drosophila amyloid model with partial RNAi. It is not WWOX-DEE evidence.
- Local-versus-external discrepancy on that paper. The PubMed abstract [ABS] says genetic reduction of Ldh rescued locomotion, "identifying dysregulated pyruvate metabolism as a key mediator". The local full-text record (PAPER 567; receipt FTR-20261026-42909904-01; 104 locators) [FT-local] says no pyruvate, PDH, PDK, flux or NAD/NADH measurement is reported in the main text, figures or supplementary tables read. The record also says whether pyruvate was tested is not established, because MetaboLights MTBLS12344 was not retrieved. I trust the local full-text reading for what was measured. The abstract's pyruvate wording is an inference by the authors. I did not re-read the full text myself, so this is a local claim I could only partly check.

## C1 - ISR modulation (eIF2B activators, ISRIB) in WWOX deficiency

Q1.
- Target and direction: eIF2B complex, activate (ISRIB class), or PERK arm (EIF2AK3), inhibit. Both would lower ISR/ATF4 output. The endpoint would be ATF4 protein and eIF2alpha-P in WWOX-deficient cells, then a functional endpoint.
- Direct WWOX-model evidence: none in a WWOX-deficient human system. Local card E01 [FT-local/derived] marks the direction UNRESOLVED and the assessment REQUIRES_QUALIFICATION. Map R-10 grades it T6.
- Other species/disease: in the fly, Atf4 immunofluorescence rises with neuronal Wwox knockdown plus Abeta42 (P = 0.0022, n = 6 brains), and not without amyloid (PMID 42909904, local FT). The abstract [ABS] says the Ldh/lactate shift is "driven by activation of" Atf4. Local record: the Atf4-to-Ldh arrow is inferred, and Atf4 is never perturbed.
- Opposing datum: in the one human WWOX-knockout organoid transcriptome (GSE156243, local join output, exploratory, n = 2 vs 4), ISR target transcripts are lower than chance. This is the only human signal and it points the opposite way from the fly.
- Compound side: ChEMBL_37 [DB] returned NO_MATCH_FOUND for "ISRIB" and for "integrated stress response inhibitor". The compound is not curated there. ChEMBL has target rows for EIF2B subunit alpha (CHEMBL6066508) and PERK (CHEMBL6030, human). DGIdb returned 0 interactions for EIF2B2. Compound-to-target links for ISRIB therefore come only from the literature, which I did not retrieve.

Q2.
- Fly amyloid-conditional, one RNAi line, partial knockdown (mRNA about 0.55), no protein measured, no null allele.
- The human transcript points the other way. Transcript is not protein.
- Safety and clinical data in the local map are from other diseases: eIF2B activator without benefit in adult ALS, guanabenz in children with vanishing white matter (abstract level, not re-checked by me), PERK-inhibitor pancreatic toxicity in mouse. The local map sources these at abstract level. I did not verify them.
- The ISR may be adaptive, so "lower is better" is unproven. Chronic ISR attenuation in a developing brain is an open safety question.
- Identifier risk: ISRIB is absent from ChEMBL, so any database row on "ISR inhibitors" concerns other compounds.

Q3. Propose a measure, not a treatment: eIF2alpha phosphorylation and ATF4 protein (plus ATF4-target transcripts) in WWOX-deficient versus isogenic human neural cells at matched maturity, with and without a defined proteotoxic challenge. Only if elevated would a pharmacological arm be justified. Until then, abstain from any statement that ISR modulation helps WWOX-DEE. This agrees with the local R-10 class READOUT_FIRST.

SOURCES: PMID 42909904 (DOI 10.1093/braincomms/fcag385); local PAPER 567; local card E01_isr_modulators.card.json; mechanism_intervention_map R-10; ChEMBL_37 queries (ISRIB, EIF2B1, EIF2AK3); Open Targets ENSG00000186153; DGIdb EIF2B2; PubTator 3 WWOX.
DEPTH: 42909904 abstract (live PubMed) plus local record of a complete full-text read, which I did not repeat. Local card and map are derived records. ChEMBL, Open Targets, DGIdb and PubTator are database rows.

## C2 - LDH inhibition (stiripentol) in WWOX deficiency

Q1.
- Target and direction: LDHA/LDHB, inhibit or lower, for lactate production; endpoints would be LDH activity, the lactate-to-pyruvate relationship, then locomotor/network function.
- Direct WWOX evidence: none at the activity or lactate level in a human WWOX system. Local card E02 comparisons: the generic assertion DR-E02-GEN-001 is OPPOSES_DISEASE_CHANGE and the others are UNRESOLVED [FT-local/derived].
- Other species: in the fly, Ldh transcript rises (+1.29 log2, knockdown added to amyloid), lactate rises with Abeta42 (interaction padj 0.0174; knockdown effect +1.30 log2 with Abeta42 and -0.43 log2 without), and Ldh RNAi partly rescues climbing (local FT; abstract PMID 42909904 [ABS] concurs on the rescue).
- Human WWOX-knockout fibroblasts (PMID 35328751, abstract [ABS]): higher glycolysis gene expression, activity and lactate in normoxia. This is an in-vitro human, non-neural, non-DEE system and supports "lactate up". It does not show harm.
- Human WOREE: the local map cites normal lactate in blood and one MRS report of cerebral lactate "extremely low" (with a second HSPG2 variant). I did not re-check these primary reports.
- Compound-versus-target (checked externally):
  - PMID 25792327 (Sada 2015, Science) [ABS] reports stiripentol as an LDH inhibitor in the context of seizure suppression in mice. The abstract does not give potency.
  - ChEMBL_37 [DB] lists stiripentol (CHEMBL1983350, max phase 4) with mechanism "Unknown", no target, so ChEMBL does not curate LDH as its mechanism.
  - DGIdb LDHA [DB] has no stiripentol interaction.
  - The local map says its LDH inhibition is weak in retrieved measurements. That comes from abstract-level papers I did not re-read, so I treat it as a local claim not independently checked.

Q2.
- Counter-evidence and limits:
  - Fly lactate rises only with amyloid and falls nominally without it. The human MRS datum is the opposite sign.
  - The fly paper itself cites Ldh knockdown as detrimental in other fly amyloid models (local record).
  - LDHA transcript up in organoids is confounded with maturity.
  - Stiripentol is licensed for Dravet syndrome with clobazam; any effect in WWOX-DEE could come from GABAergic or CYP-interaction pharmacology rather than LDH. Local map: no source attributes its antiseizure action to LDH.
  - Neuronal origin of the fly lactate is unestablished (glia carry the highest Wwox mRNA).
- Identifier risk: LDHC is testis-restricted; ChEMBL's LDHA target search returns non-human entries first (bovine, rabbit, rat, mouse), so species must be selected explicitly.

Q3. Propose a measure: lactate (L/D enantiomer- or isotope-resolved) and LDH activity in WWOX-deficient versus isogenic human neural cells at matched maturity. In the fly, include an Ldh-alone arm. Only afterwards compare stiripentol with a selective LDHA tool at matched exposure to separate LDH from other pharmacology. Abstain from any efficacy statement now. The question reopens if lactate or LDH activity is shown abnormal in WWOX-deficient human neural cells.

SOURCES: PMID 42909904; 25792327 (DOI 10.1126/science.aaa1299); 35328751 (DOI 10.3390/ijms23063326); local PAPER 567; card E02_ldh_inhibition; map R-11; ChEMBL CHEMBL1983350, CHEMBL2102, CHEMBL4879426; DGIdb LDHA.
DEPTH: abstracts for 42909904, 25792327 and 35328751. Local full-text-read record for 42909904, not repeated by me. Database rows for ChEMBL and DGIdb.

## C3 - PDK inhibition (DCA) in WWOX deficiency

Q1.
- Target and direction: PDK (PDK1-4), inhibit, to relieve PDH inhibition and send pyruvate into the TCA cycle. Endpoints would be PDH activity or PDHA1 phosphorylation and pyruvate fate.
- Direct WWOX evidence for the premise: Map CHAIN E says Pdk1 and glycolytic genes are measured up in Wwox-KO mouse embryonic fibroblasts and cancer cells (qRT-PCR, WWOX-HIF1alpha link; local record, I did not retrieve that primary). Human WWOX-deficient fibroblasts show more glycolysis and lactate (PMID 35328751 [ABS]).
- Against the premise in human organoids: in the GSE156243 knockout organoid transcriptome PDK1 is DOWN, the PDK/PDH set is not different from chance, and the LDH-to-PDH ratio is not shifted (card E03, exploratory, transcripts only).
- Lucas-Clarke measured no pyruvate/PDH/PDK/flux (local FT record; PubMed abstract speaks of "dysregulated pyruvate metabolism" without data).
- No paper measures DCA in any WWOX system of any species (local map N-08, and my PubMed search for WWOX plus dichloroacetate returned nothing relevant; the five returned PMIDs concerned ketogenic, lactate, lithium or the ISR).
- Other disease: PMID 23611579 (Abdelmalak 2013) [ABS]: 8 patients with PDC or respiratory-chain deficiency on DCA for 9.7-16.5 years; nerve conduction decreased modestly in 3 with dose reduction or pause, and no symptomatic worsening of neuropathy. Local map reads the same paper (partial full text) and adds the MELAS RCT, which ended early for symptomatic neuropathy. That trial was cited, not opened. PMID 36432491 (local): DCA plus pyruvate in adult rats after pilocarpine seizure, where the combination, but not either agent alone, improved neuronal survival.

Q2.
- The HIF1alpha, PDK1, PDH step is unmeasured in any WWOX-deficient human neural system.
- The only human transcript points against a PDK-high state.
- Map N-08 classes DCA as DEPRIORITIZE, with the rationale pending and the nerve-conduction signal in other disease.
- Identifier confusion, confirmed in two databases:
  - ChEMBL "PDK1" target search returns 3-phosphoinositide-dependent protein kinase 1 (PDPK1, CHEMBL2534) first, ahead of pyruvate dehydrogenase kinase isozyme 1 (CHEMBL4766).
  - DGIdb gene "PDK1" lists DCA together with PDPK1 inhibitors (for example BX-912, BX-795).
  - ChEMBL lists DICHLOROACETIC ACID (CHEMBL13960, max phase 3) with no curated mechanism row ("molecule_without_mechanism"). Target-level claims about DCA are therefore not backed by ChEMBL.
- Compound-versus-target: DCA is also a broad metabolic agent, and its adult mitochondrial-disease safety data are not paediatric DEE data.

Q3. Propose a measure: PDH activity or PDHA1 serine phosphorylation, and labelled-glucose pyruvate fate (acetyl-CoA, citrate, lactate), in WWOX-deficient versus isogenic human neural cells; also Seahorse OCR/ECAR, which the map names as the shared falsifier for the PDK/ketogenic axis. Abstain from any DCA statement until PDH-pathway dysfunction is shown in a WWOX-deficient human neural system.

SOURCES: PMIDs 23611579 (DOI 10.1016/j.ymgme.2013.03.019), 36432491 (cited by local record only; not retrieved by me), 35328751, 42909904; local PAPER 557, 562, 567; card E03; map N-08, CHAIN E; ChEMBL CHEMBL13960, CHEMBL4766, CHEMBL2534; DGIdb PDK1.
DEPTH: abstracts for 23611579, 35328751, 42909904. Local partial-full-text records for 557 and 562 (not re-read by me). Database rows for ChEMBL and DGIdb.

## C4 - Ketogenic diet and the lactate axis in WWOX deficiency

Q1.
- Target and direction: no single molecular target. The mechanistic rationale (map CHAIN E) is to supply acetyl-CoA from ketones below a postulated PDK1-PDH block. The endpoints are seizure control and oxidative flux; lactate is the contested readout.
- Direct human evidence: PMID 36537114 [ABS]: five WOREE patients with biallelic predicted-null variants; "epilepsy that responded to a ketogenic diet in three patients". This is an uncontrolled case series and the response is not quantified in the abstract. The local map says KD was tried in 3 and continued in 1, and that in a severe case it was listed among ineffective interventions. I did not retrieve those primary sources. This is a discrepancy: the abstract says "responded" while the local continuation signal is poor. I trust neither as efficacy evidence. The disagreement is worth a follow-up read of the full text.
- Lactate-axis evidence: lactate up in WWOX-KO human fibroblasts (35328751 [ABS]) and in fly (amyloid-conditional); human blood lactate is normal and brain MRS lactate "extremely low" in one case (local map, DL-BIO-008/009, not re-checked). The signs conflict.
- The local card E04 has abstention NO_DRUG_ASSERTIONS_SUPPLIED and direction UNRESOLVED. The Lucas-Clarke study has no diet, ketone, PDH or pyruvate arm.
- Other disease: KD is a standard treatment in drug-resistant paediatric epilepsy and in GLUT1 deficiency (local map; general knowledge, not retrieved here). Its effect in DEE is not WWOX-specific.

Q2.
- Seizure response to KD in DEE is common and does not show a WWOX-specific mechanism.
- n = 3 and n = 1 case-level reports; no controls.
- Human WWOX metabolism is reported normal in several screens (local map, not re-checked), so the metabolic rationale may not apply. The fly lactate is amyloid-conditional with a reversed sign without amyloid.
- Species: the PDK1 evidence is mouse fibroblast and cancer cell. The only human neural dataset is a transcriptome.
- Confusion risk: "lactate axis" mixes blood, CSF, MRS and fly-head measurements, which are not comparable.

Q3. Propose a measure: Seahorse OCR/ECAR (and isotope tracing) on donor-derived cells or the existing WWOX-KO organoids, which the local map names as the remaining falsifier. A structured full-text re-read of the WOREE case series (36537114) for KD duration, response definition and co-treatments is also a research measure. Abstain from any statement of benefit beyond "seizure response was reported in 3 of 5". The question reopens if flux is shown abnormal in WWOX-deficient human cells.

SOURCES: PMIDs 36537114 (DOI 10.1002/ajmg.a.63074), 35328751, 42909904; local card E04; map R-05, CHAIN E, DL-BIO-008/009.
DEPTH: abstracts for the three PMIDs. Local derived records for the rest.

## C5 - Lithium / GSK3beta inhibition in WWOX deficiency

Q1.
- Target and direction: GSK3beta, inhibit. Endpoints: seizure susceptibility, Tau phosphorylation (S396/S404), neurite outgrowth.
- Direct (WWOX mouse): PMID 32000863 (Cheng 2020) [ABS] states significantly increased GSK3beta activation in Wwox-null cortex, hippocampus and cerebellum, and that lithium abolishes PTZ-induced seizure onset in Wwox-/- mice. The local full-text record (PAPER 019; claim CLAIM 016) states the evidence is narrower:
  - the Ser9 densitometry (Fig. 7c) is one lane per genotype with no statistics (NOT_TESTED);
  - lithium suppressed PTZ seizures in all three genotypes, wild type included, so the experiment does not show a WWOX-specific rescue;
  - the genotype-specific reading was transmitted by a review.
  I could not open the figure. I trust the local figure-level reading over the abstract for specificity, since the abstract is a summary and the local record read the panel.
- Mechanism (human cells): PMID 22193544 (Wang 2012) [ABS]: WWOX binds GSK3beta through its SDR domain and inhibits GSK3beta-stimulated Tau S396/S404 phosphorylation in SH-SY5Y cells, promoting neurite outgrowth. The local record adds a docking motif 388-407 with L404 required and S9-independence. That residue-level detail is not in the abstract and I did not verify it. Because the mechanism is S9-independent, the pS9 western is a poor readout (local CLAIM 016/035 mutual exclusion).
- Compound identity: ChEMBL [DB] shows LITHIUM CARBONATE (CHEMBL1200826, phase 4) with two curated mechanisms, inositol monophosphatase 1 inhibitor and GSK-3 inhibitor. The names "lithium" and "lithium chloride" returned either no mechanism row or NO_MATCH_FOUND. Lithium is a non-selective inhibitor.

Q2.
- Lithium suppressed seizures in wild-type mice as well (local figure reading), so it acts as a general anticonvulsant.
- Direction conflict on a second axis: the local map says WWOX loss gives Wnt hyperactivation, and lithium stabilises beta-catenin and activates Wnt. I did not verify the Wnt direction externally. It is a local inference from the discovery ledger.
- Only 5 PubMed records for WWOX AND GSK3 (local count, not re-run).
- The ChEMBL "GSK3B" gene search returns GSK3B-interacting protein (CHEMBL6067425) before GSK3beta (CHEMBL262). That is an identifier trap for target-based queries.
- DGIdb GSK3B has 86 interactions, none of them lithium in the rows I saw. Selective inhibitors (for example elraglusib) are listed.
- Mouse null model with a severe phenotype; no human WOREE lithium data found; narrow therapeutic index (local).

Q3. Propose a measure: a PTZ plus lithium arm in Wwox-/-, +/- and +/+ with an explicit genotype-by-treatment test, or a different GSK3beta inhibitor under the same design. In parallel, measure GSK3beta activity with a substrate readout (pTau S396/S404 or GS-1) rather than pS9, and beta-catenin and Wnt readouts. Abstain from a WWOX-specific lithium claim. It reopens if a tested genotype-by-treatment interaction appears.

SOURCES: PMIDs 32000863 (DOI 10.1186/s40478-020-0883-3), 22193544 (DOI 10.1038/cdd.2011.188); local PAPER 019, 056, CLAIM 016, 035; map CHAIN C, R-04, N-02; ChEMBL CHEMBL1200826, CHEMBL262, CHEMBL6067425; DGIdb GSK3B; Open Targets.
DEPTH: abstracts for 32000863 and 22193544. Local full-text-read records, which I did not repeat. Database rows for ChEMBL and DGIdb.

## Overall
- No case has direct WWOX-deficient human evidence for the intervention's target. The only same-gene metabolic pharmacology datum is the fly Ldh rescue. Lithium has the only mouse WWOX-null drug experiment, and its specificity is disputed between abstract and figure reading.
- External databases confirmed the gene-disease link (Open Targets) but returned no WWOX-intervention relation (DGIdb, PubTator treat). They exposed identifier traps (PDK1 versus PDPK1; GSK3B versus GSK3B-interacting protein; ISRIB absent from ChEMBL; stiripentol without curated mechanism).

RUN LOG: about 22 tool calls. Read 2 (questions.md, scripts README); Bash 7 (join help/queries, registry_records get for PAPER 567/019/056/557/562 and CLAIM 016, adapter calls for chembl, opentargets, pubtator3, DGIdb GraphQL by curl, sed over the mechanism map); ToolSearch 1; PubMed metadata 2 calls (8 PMIDs); PubMed search 1; Write 1. Services used: ChEMBL_37, Open Targets api 26.9.0, PubTator 3, DGIdb, PubMed. No e-mail address sent. The Europe PMC route was not used. I did not read any file under a p3a or knowledge_contribution_trial path, apart from the output files named in the task.

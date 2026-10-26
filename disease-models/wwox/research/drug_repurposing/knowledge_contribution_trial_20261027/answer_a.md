# P3A answer, condition A (external resources only)

Common basis (all cases). Direct WWOX-model evidence retrieved:
- PMID 32000863 (Wwox knockout mouse, abstract): Wwox ablation causes spontaneous epilepsy and increased pilocarpine/PTZ seizure susceptibility in preweaning mice. GSK3beta activation is increased in cortex, hippocampus and cerebellum. Lithium ion abolished PTZ-seizure onset in Wwox-null mice.
- PMID 42909904 (Drosophila Alzheimer's model, abstract): neuronal wwox knockdown on an Abeta background raises Ldh expression and lactate, driven by Atf4 activation. Genetic Ldh reduction rescued locomotor deficits.
- PMID 36537114 (human WOREE, 5 patients, abstract): epilepsy responded to a ketogenic diet in 3 patients.
- Human WWOX-DEE disease association exists in Open Targets: DEE28 (MONDO_0014533), SCAR12 (MONDO_0013687).
- PubTator3: WWOX-Epilepsy 27 publications, WWOX-Seizures 16, WWOX-Brain Diseases 39 (counts only, not content).

All WWOX metabolic statements from cancer and fibroblast work are other-disease or other-cell-type evidence. Open Targets and ChEMBL here are NOT WWOX evidence.

## C1 ISR modulation (ISRIB / eIF2B activators)

Q1. Target: eIF2B (activate), which dampens ISR/ATF4 signalling; endpoint would be ATF4 output or its downstream targets.
- Direct WWOX evidence: none retrieved. A PubMed search for WWOX with ISRIB, UPR, ER stress or eIF2 returned no WWOX-ISR primary paper.
- Closest link, Drosophila (PMID 42909904, abstract): wwox knockdown activates Atf4, which drives Ldh and lactate. This supports a rationale of ATF4 high, so ISR inhibition would be expected to lower it. That is inference only. It is a fly Abeta-background model, not WOREE.
- Other disease: PMID 35047994 (oral squamous carcinoma, abstract) links TMEM207, which impairs WWOX function, to ER-stress sensitivity. This is cancer.
- ChEMBL: ISRIB gave NO_MATCH_FOUND in molecule search (a name-query result, not absence). The eIF2B subunit target CHEMBL6066508 exists in ChEMBL.

Q2. Counter-evidence and risks:
- The ATF4 link is from flies with an Abeta transgene. Whether ISR is activated in human or mouse WWOX-null brain was not shown in anything I read.
- ISR can be adaptive, so inhibition could be harmful.
- Compound versus target: ISRIB is not an approved drug, and I verified no ISR-activation datum in WOREE.

Q3. Proposed research measure: in Wwox-null mouse brain or patient-derived cells, measure p-eIF2alpha, ATF4 and its targets. Only then test an eIF2B activator in vitro. Abstain from any in vivo claim until ISR activation is shown in a mammalian WWOX-null system. Reopening condition: a mammalian WWOX-null dataset showing ATF4/ISR activation.

## C2 LDH inhibition (stiripentol)

Q1. Target: LDHA/LDH (inhibit); endpoint is lactate level, and seizure or locomotor phenotype.
- Direct (but fly): PMID 42909904, genetic Ldh reduction rescued locomotor deficits in wwox-knockdown Abeta flies, with lactate elevated.
- Other-cell evidence: PMID 35328751 (abstract, human fibroblasts with WWOX knockout) shows higher glycolysis genes, activity and lactate. Cancer papers (PMID 27308416, 40198927) tie WWOX loss to HIF1alpha and glycolysis.
- Inference: LDH inhibition might lower lactate, if the same biology holds in mammalian neurons.

Q2. Counter-evidence and risks:
- Compound versus target confusion. ChEMBL lists stiripentol (CHEMBL1983350, phase 4) with mechanism "Unknown" (references: PubMed 24001087, 25792327, which I did not read). Its LDH action is not curated as its mechanism there. A PubMed query for stiripentol plus LDH inhibition returned 28 hits that I did not read; I make no claim about potency.
- Stiripentol's established antiseizure effect may be GABA-A related or via CYP interactions. I did not verify this, so it is unverified.
- ChEMBL LDHA target records for human, mouse, rat, bovine and rabbit are separate IDs (human not listed in my first 4 rows, so I do not cite it).
- The fly rescue was genetic. No WWOX-null mammalian data on lactate or LDH was found.

Q3. Proposed measure: lactate and LDH activity or expression in Wwox-null mouse brain, CSF or patient fibroblasts/iPSC neurons. If lactate is raised, run in vitro LDH-inhibition tests with a defined LDH inhibitor, not stiripentol by default. Abstain from therapeutic claims. Reopening condition: demonstration of elevated lactate in mammalian WWOX deficiency.

## C3 PDK inhibition (dichloroacetate)

Q1. Target: PDK (inhibit) to raise PDH flux; endpoint is lactate and the pyruvate-to-acetyl-CoA axis.
- Direct WWOX evidence: none retrieved for DCA or PDK. The PubMed query combining WWOX with dichloroacetate returned no such paper.
- Indirect: the fly paper (PMID 42909904) names dysregulated pyruvate metabolism as a mediator. The TAP-MS interactome (PMID 30619736, abstract) suggests WWOX roles around acetyl-CoA generation. Both are inference-level for DCA.
- ChEMBL: dichloroacetic acid CHEMBL13960 (phase 3) has no curated mechanism in the row returned. PDK2 target CHEMBL3861 (human) exists. The link between drug and target is not established by my retrieval.

Q2. Risks:
- Cancer-model glycolysis findings do not transfer to neurons.
- Compound-versus-target confusion: a "molecule_without_mechanism" row is not evidence of PDK inhibition by DCA in ChEMBL.
- Unknown: DCA toxicity in children, not assessed, I did not retrieve safety data.

Q3. Abstain. Reason: no WWOX-specific evidence on PDH/PDK status. Reopening condition: measured PDH phosphorylation or pyruvate/lactate abnormality in a WWOX-null mammalian model.

## C4 Ketogenic diet and the lactate axis

Q1. Target: systemic metabolism (substrate switch to ketones); endpoint is seizure frequency.
- Direct human clinical (small): PMID 36537114 (abstract): epilepsy responded to ketogenic diet in 3 of 5 reported WOREE patients. This is a case series, with no controls.
- The lactate link is inference: lactate is increased in WWOX-deficient fibroblasts (PMID 35328751) and in the fly (PMID 42909904), but no study I read connects the diet to lactate in WWOX deficiency.

Q2. Counter-evidence and limits:
- n=5, uncontrolled, publication bias; responder definition and durability not read (abstract only).
- Ketogenic diet response is common in DEE generally, so it is not WWOX-specific.
- Lactate-diet mechanism is unproven.

Q3. Propose: a structured retrospective collection of diet response against genotype in WOREE cohorts, and lactate measured before and during diet where available. Not a treatment recommendation. Reopening for mechanism: paired lactate and seizure data.

## C5 Lithium / GSK3beta inhibition

Q1. Target: GSK3beta (inhibit); endpoint is seizure threshold (PTZ) in mice.
- Direct WWOX model: PMID 32000863 (abstract only): GSK3beta activation is raised in Wwox-null cortex, hippocampus and cerebellum, and lithium delayed or abolished PTZ-induced seizure onset in Wwox-null preweaning mice.
- Human WOREE: no lithium data retrieved.

Q2. Counter-evidence and transfer risks:
- Single mouse study, acute PTZ endpoint, preweaning; no chronic or survival data seen. I read the abstract only, so dose and controls are unverified.
- Lithium has many targets beyond GSK3beta (inositol monophosphatase). The effect is not proven to be GSK3beta-mediated by lithium alone.
- ChEMBL: LITHIUM CHEMBL1201333 (phase 3) has no curated mechanism row. GSK3beta human target is CHEMBL262, and "GSK3B-interacting protein" (CHEMBL6067425) is a distractor ID, so do not confuse them.
- Species and age transfer to human infants is unaddressed, and a narrow therapeutic index is a general lithium property, not retrieved here.

Q3. Propose: replicate and extend in Wwox-null mice, comparing a selective GSK3 inhibitor with lithium, with p-GSK3beta (Ser9) readout and a chronic seizure endpoint. Also measure p-GSK3beta in human patient-derived cells. This is a research measurement only. Reopening for any human question: independent replication.

SOURCES: PMID 32000863, 42909904, 36537114, 35328751, 27308416, 40198927, 30619736, 26390919, 35047994; PubMed search results (query lists, not read as papers) for stiripentol+LDH (28 hits) and WWOX+ISRIB/UPR/DCA/ketogenic; ChEMBL CHEMBL1983350, CHEMBL13960, CHEMBL1201333, CHEMBL262, CHEMBL6067425, CHEMBL3861, CHEMBL6066508; Open Targets ENSG00000186153 (MONDO_0014533, MONDO_0013687); PubTator3 WWOX relations.

DEPTH: all PMIDs, abstract only (PubMed metadata); no full text read. ChEMBL and Open Targets: database rows only. PubTator3: relation counts only. PMIDs 24001087 and 25792327 appear only as ChEMBL references and were not opened.

RUN LOG: approximately 16 tool calls (adapter list; adapter queries for ChEMBL, PubTator3 and Open Targets (about 13 calls in loops/batches); 5 PubMed searches; 3 PubMed metadata calls, one oversized and re-read via local file; 1 failed citation lookup). Services: repurposing_adapter (chembl, pubtator3, opentargets), PubMed tools. No forbidden repository material was read. No e-mail address sent to any service.

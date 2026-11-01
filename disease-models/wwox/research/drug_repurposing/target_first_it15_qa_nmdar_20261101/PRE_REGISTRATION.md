# PRE-REGISTRATION (written before any extraction; 2026-11-01)

QUESTION Q-A (partial functional benefit): In Wwox neuron-deleted neocortical slices the spontaneous bursts are d-APV-sensitive (Breton 2021, PMID 34634460) but no NMDAR current was measured; which NMDAR-targeting mechanism classes would reduce bursting during exposure, and what discriminating prediction separates them?

WWOX observation: Breton 2021 d-APV abolishes bursts; needs.json NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR observations (O1 bursts 36/42 KO, 4/23 HT, 0/11 WT; O2 d-APV abolishes bursts, n=5 slices/3 animals, one drug so permissive vs gain not distinguished); E0-E2 design in function_pharm_it14_p3_20261101/experiment_arms_it14_p3.tsv.
System/contrast: Synapsin-Cre Wwox S-KO vs S-HT vs Cre+ WT neocortical L2/3 slices P13-P17 (animal = unit).
Known/unresolved biological role: NMDAR necessary for bursts (known); whether NMDAR gain is raised, or permissive necessity, or inhibitory loss upstream (unresolved; E0 measures isolated NMDAR current).
Desired action: reduce NMDAR-dependent drive during exposure (partial benefit, symptomatic-functional). Opposed actions kept visible: agonists/co-agonists (glycine, D-serine, D-cycloserine), GluN2A/2B positive modulators, Mg2+ lowering.
Endpoints: burst incidence/frequency/duration; isolated NMDAR current with GluN2B (ifenprodil-site) sensitivity; suppression index in WT matched-trigger slices as a specificity qualifier (not a condition of benefit).

Source perimeter: ChEMBL target-first via framework/adapters/chembl.py on UniProt GRIN1 Q05586, GRIN2A Q12879, GRIN2B Q13224, GRIN2C Q14957, GRIN2D O15399 (single-protein and complex targets listed apart; human and rodent), activity types IC50/Ki/Kd/EC50; GtoPdb interactions file in the catalog cache; DGIdb/DrugCentral cached files for action direction. The 20 NMDAR entries of ranking_it8_p9_20261029/deepening_queue.tsv are ANCHORS, not the perimeter; compounds found target-first and absent from that queue are reported as such.
Per query recorded: parameters, total_count vs retrieved, truncation, failures, unresolved identities, exclusions with reason. ChEMBL HTTP 500: at most two retries with pause, logged as "not retrieved", never "no data".

Method: target-first retrieval -> identity (parent/salt/metabolite/stereoisomer; esketamine vs ketamine, S/R) -> action direction -> same-document subunit potency graded with scout_it14_p6_20261101/selectivity_p6.py (collect/grade_group; INTERPRETABLE / LIMITED / NOT_DETERMINABLE / PANEL); no ratio for NOT_DETERMINABLE; assay descriptions read for voltage, agonist and glycine concentrations; generic NMDA-receptor complex value is not a subunit value; censored values stay censored.

Selection criteria for deepening (fixed now): (i) >=1 same-document GluN2B-vs-GluN2A (or defined heteromer) comparison graded INTERPRETABLE or LIMITED; (ii) a distinct mechanism class (use-dependent pore blocker fast vs slow trapping; GluN2B NAM at ifenprodil site; glycine-site antagonist; competitive glutamate-site antagonist, reference d-AP5); (iii) identity and action verified; (iv) not already assessed elsewhere in the module (reconciliation/assessed_in/mentioned_in columns of deepening_queue.tsv; if assessed, cite and add only what is new).

Required cases (P3.4): one known reference; one hypothesis emerged from the search; one alternative with a different mechanism; one counter-hypothesis or discriminating control. A new name is not required. If no case survives, failed steps are documented.

Guardrails: free key-less public sources; no spend; operator e-mail never sent to any service; no individual regimens/doses; supplement/OTC/prescription are consultation categories only; WWOX evidence kept apart from other-disease precedent; unknown != negative; one origin counted once; LLM agreement is not evidence. Not medical advice.

## Deviations
- D1 (2026-11-01): ChEMBL accession queries for Q12879 (GRIN2A) and Q13224 (GRIN2B) failed after 1 attempt + 2 retries; fallback = gene-symbol target search (also failed for GRIN2B, GRIN1, GRIN2C) and the target IDs known from earlier modules (CHEMBL1972, CHEMBL1904, CHEMBL1907603/4, CHEMBL3038504/5, CHEMBL2015). Reason: service intermittently HTTP 500. Effect: target discovery for human/rodent subunits is incomplete; stated in README.
- D2: rodent targets missed by discovery were found from molecule-first rows (anchor compounds) and then pulled target-first. Molecule-first pulls for 15 anchor/tool compounds were added to close the truncation of the 2000-row cap; they do not change the question or criteria.
- D3: DrugCentral file was not in the cache; downloaded once (public, 0.96 MB) and hashed.
- D4: selectivity_p6.py logic was imported unchanged; reviewer notes were added in a separate column where its technique-keyword rule (no 'voltage clamp' term) or a missing voltage control made the grade misleading. Grades themselves are not altered.

# Pre-registration, IT15 Q-B (GSK3), written 2026-11-01 BEFORE any extraction

Non-canonical research material. Not medical advice. No dose, schedule or individual regimen.

## Question (fixed)
QUESTION Q-B (broader compensation compatible with complete loss of WWOX function, independent of residual protein): WWOX loss is reported to de-repress GSK3beta in the Wwox-null mouse brain (pSer9 decreased, total unchanged) and WWOX binds GSK3beta through an Axin-like motif (S9-independent inhibition), whereas Wnt/beta-catenin target genes are UP in WWOX-knockout organoids (a direction opposite to what higher GSK3 activity predicts, confounded by maturity). Lithium suppressed provoked seizures in all genotypes (not WWOX-specific). Which GSK3-targeting mechanism classes would discriminate GSK3-on-substrate de-repression from lithium's many other actions, in which direction would each push the Wnt readout, and what experiment would discriminate?

## WWOX observation, system, contrast (read from the module before extraction)
- NEED-GSK3B-DEREPRESSION O1 (PMID 32000863, Wwox-/- vs +/+ mouse, P20 cerebellum/hippocampus/cortex, pSer9 down, total unchanged; WWOX_EXPERIMENT_IN_DEE_SYSTEM) and O2 (PMID 22193544, SH-SY5Y RNAi, residues 388-407 / L404 Axin-like docking, Tau S396/S404 effector; WWOX_BIOLOGY_OTHER_CONTEXT). The needs file itself lists intervention direction "uncertain" and notes CLAIM 016 and CLAIM 035 exclude each other on the S9 axis.
- NEED-WNT-BETA-CATENIN O1-O4 (PMID 34268881 organoid DE tables: NKD1, AXIN2, LEF1, TCF7L2, CTNNB1, WNT8B up, 4 vs 2 libraries; O2 rescue arm mixed; O3 stage contrast not a genotype contrast).
- G01 card (lithium): DR-LI-001 OPPOSES_DISEASE_CHANGE only on the provoked-seizure score, equally present in wild type and heterozygote (non-specific); assessment REQUIRES_QUALIFICATION, direction UNRESOLVED.
- Prior state to reconcile, not repeat: IT10 Q7 dispositions (generation_it10_p1_20261031/results/dispositions_Q7.tsv): 50 direct-search GSK3B families (SB-216763, tideglusib, lithium, AZD-1080, CHIR-98014, LY-2090314, elraglusib, ...), all DIAGNOSTIC_ONLY, role_status unknown, hop0 (target is the seed gene). deepening_queue.tsv reconciliation columns list no GSK3 compound as assessed.
- Premise limit stated up front: no kinase-activity assay exists in any WWOX system; one pSer9 western; Ser9 state and abundance are dissociable from activity; Tau and beta-catenin phosphorylation by GSK3 in WWOX loss are unmeasured.

## Desired action; opposed actions kept visible
Reduce GSK3 activity or its substrate phosphorylation (a compensation not requiring WWOX protein). Opposed/competing: GSK3 inhibition raises beta-catenin signalling (Wnt already up in organoids = possible adverse direction); GSK3 activators are listed as the opposed class.

## Endpoints
Substrate phosphorylation (Tau at GSK3 sites; beta-catenin phospho-S33/S37/T41 vs active beta-catenin), kinase activity assay, Wnt reporter/target genes; seizure threshold only as non-specific.

## Source perimeter
ChEMBL target-first via framework/adapters/chembl.py for GSK3B (P49841) and GSK3A (P49840), human and rodent, single-protein targets, IC50/Ki/Kd (EC50 excluded from the primary grading); GtoPdb files in catalog/cache/gtopdb; DGIdb and DrugCentral cache files for action. No other source. ChEMBL HTTP 500: at most two retries per request with a pause, failures logged as "not retrieved".

## Method (fixed)
target-first retrieval -> identity (parent/salt/metabolite/prodrug) -> mechanism class (ATP-competitive; non-ATP-competitive/allosteric/irreversible such as tideglusib; substrate-competitive peptide; ion-competitive lithium with Mg2+ competition) -> same-document GSK3B vs GSK3A and kinase-panel data graded with scout_it14_p6_20261101/selectivity_p6.py (collect, grade_group; a cross-family kinase panel is PANEL_NOT_SELECTIVITY; no ratio for NOT_DETERMINABLE; censored stays censored; assay descriptions read for ATP concentration, substrate, pre-incubation, time dependence) -> counter-evidence per class (off-target kinases, Wnt direction, tau-vs-catenin separation).

## Selection criteria for deepening (fixed now)
(i) at least one graded GSK3B-vs-other-kinase or GSK3B-vs-GSK3A same-document comparison; (ii) a mechanism class that differs from lithium; (iii) identity and action verified; (iv) not already assessed in the module (checked in DR/exploration_it9_p3_20261030, generation_it10_p1_20261031 Q7, deepening_queue.tsv; what exists is cited).

## Required cases (P3.4)
known reference (lithium); one hypothesis from the search; one alternative with a different mechanism; one counter-hypothesis/discriminating control (for example the Wnt direction). A new name is not required.

## Abstention
Abstention is a valid result. If the premise (single Ser9 blot, no activity assay, opposing Wnt direction) makes every compound diagnostic-only, the result says so with the failed steps and what would make it searchable. A candidate is not forced.

## Deviations
No change to the question or the criteria. Operational notes, all 2026-11-01, logged because they affect what the criteria mean in practice:
1. Criterion (i) reading, fixed BEFORE grading was looked at in full but after the census: "graded" is read as a comparison that earns grade INTERPRETABLE or LIMITED, so that a ratio exists; a PANEL_NOT_SELECTIVITY or NOT_DETERMINABLE grade does not satisfy (i), because the P6 logic computes no ratio for them.
2. The primary page size (1000 rows) returned HTTP 500 for several targets; the pages that failed were re-requested as limit=200 pages (a different request form, same endpoint, same retry rule). Totals and retrieved counts are in perimeter_log.tsv.
3. The ChEMBL target request for P49841 failed three times in the script; CHEMBL262 (GSK3B human) was taken from an adapter call (chembl.query uniprot P49841) made earlier in the session; both are recorded in the log.
4. Beyond the planned compound set, one extra target-first lookup was made after seeing the Axin-1/GSK3B PPI target (CHEMBL3883309) in the adapter answer; it is reported as found, not planned.

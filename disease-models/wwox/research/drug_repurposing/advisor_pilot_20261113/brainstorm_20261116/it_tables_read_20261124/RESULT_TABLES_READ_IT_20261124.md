# Tables read for the ADV-219 class A list (IT, 2026-11-24)

Actor `orchestrator` (IT successor, session 7cf5e85a), task ORCH-ROADMAP-IT59-20261119. ADV decision of 2026-11-24: the class A mislabels of ADV-219 are corrected by a real reading, not by a label. Reason: a `receipt_correction` may not change coverage, and in the union (`reading_state.py`) a later `not_read` does not displace an earlier `not_present`; only a read does. Each paper below gets one small partial receipt (reason `new_question_outside_prior_coverage`), event ids `FTR-20261124-<pmid>-NN`, source file = the file the latest earlier receipt names (sha256 equal to that receipt's fingerprint, also for the two rows the audit flagged as digest-differs). Hypothesis level; nothing is medical advice; no registry edited.

## Read, one line per paper (tables read with the WWOX question in mind)
* **17909041** (tables): Table 1 (PDF p.4): Wwox immunoreactivity (normal, reduced, absent) against ErbB4 overall expression, membrane and nuclear localisation in breast cancer; absent Wwox in 59% where ErbB4 is absent against 34% where present, normal Wwox in 64% with membrane ErbB4 against 44% without, no nuclear association (48/12/41 against 48/14/38): bears on the ERBB4 interaction question as a human tumour association only.
* **31605637** (tables): Tables 1 and 2: crystallographic data collection and refinement statistics for NQO1 wild type with the small-molecule chaperone (PDB entry 6FY4, resolution 2.76 A) and steady-state kinetics of wild type and the P187S variant with and without it (P187S kcat/KM about 70 rising to about 170 with the compound); no WWOX content; a chaperone-rescue precedent for a destabilised variant.
* **31781019** (tables): Three tables: electrode locations in individual APP/PS1 mice; occurrence of eight spike types by behavioural state (sleep 68 to 99 percent, immobility 0.4 to 31, movement 0 to 4); odds ratios of spikes by state under saline; no WWOX content; an EEG precedent for state dependence of spikes.
* **33704440** (tables): One table of predicted interaction partners and stabilisation class for four CACNA1I gain-of-function variants and their wild-type residues, resting and activated state; no WWOX content.
* **34253921** (tables): One table: proportions of neurons with significant encoding by ANOVA and by linear decoder in wild-type and Shank3 heterozygous mice (188 and 180 neurons); no WWOX content.
* **36282524** (tables): One table: phenotype summary of three C. elegans dnj-14 mutants (mean lifespan reduced 25, 15 and 18 percent, P < 0.0001) and other assays; no WWOX content.
* **41137852** (tables): Three tables: clinical and EEG features by epilepsy syndrome, genetic etiology against treatment efficacy by drug, and a multivariable model (drug resistance odds ratio 5.6, p = .002; early absence onset 3.3, p = .022) for unfavourable neurodevelopmental outcome; WWOX is not named in any table.
* **42589397** (tables): Table 1 (hormone-associated genes between high and low WWOX/HIF1A ratio groups by subtype) and Table 2 (summary by subtype and group): the metabolic profile of the high-ratio group is oxidative phosphorylation and active mitochondrial function in basal-like breast cancer, hyperactive biosynthesis in luminal A, and mitochondrial dysfunction in luminal B, while the low-ratio group is a glycolytic shift in basal-like: the direction is subtype-dependent, which supports the direction caveat of the ratio claim.
* **39769031** (results, discussion): Section 2.4 of the combined section '2. Results and Discussion' (read in full, 2.1 to 2.3 synthesis not read): stiripentol and iso-stiripentol inhibit human LDHA only weakly (10 to 38 percent at 500 uM; IC50 above 500 uM) against three new analogues with IC50 about 100 to 200 uM; no WWOX content; the combined heading is why the earlier map called discussion not_present.

## Skipped, with the reason (no receipt)
* **28919853**: antibody table (reagent, not data)
* **31331032**: antibody and lectin table (reagent, not data)
* **36278433**: two tables of metabolite-extraction protocol and mass-spectrometry acceptance criteria (method and quality control, not data)
* **42770556**: key-resources table (reagent, not data)
* **26419537**: the one table is an image inside the XML (a gene list as a figure); not opened
* **42846717**: the 'Methods' heading is the structured-abstract line of a narrative review; no Methods section exists in the body: the label is right
* **39337309**: rule false positive (see ADV-223 message)
* **40119223**: rule false positive
* **42494992**: rule false positive
* **42190665**: excluded: ADV-222 reads it

## Bearing on open rows
* The only table with WWOX content is that of 42589397 (WWOX/HIF1A ratio), and it supports the direction caveat already carried by the claim record (the high-ratio group is oxidative in one subtype and mitochondrially dysfunctional in another): it adds to the argument for the working-model wording candidate `CC-20261124-ORCHESTRATOR-ADV223-POOLED-DIRECTION-01`, row A and B. 17909041 Table 1 is a human tumour association of Wwox with ErbB4 and does not narrow `IT59-Q01` (neural WW1 binding).
* Reading depth: every receipt is partial; none raises a paper to complete. Of the 19 class A flags of ADV-219: 9 receipts here (8 tables, 1 section of a combined heading), 4 reagent or method-protocol tables not counted as data, 1 image table not opened, 1 abstract-level Methods line (label right), 3 rule false positives, 1 excluded because ADV-222 reads it.

## Limits
The tables were read from the XML or PDF text layer; the one image table was not opened; supplementary files and figures of these papers are not touched; the receipts say `not_read` for every section other than the one read.

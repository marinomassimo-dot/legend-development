# Loop 1 (partial benefit): when a stress response may be compensatory, which kinase, which endpoints, which window

Scientist-b, task `ORCH-ROADMAP-IT8-20261029`, package P5, 2026-10-29. Non-canonical research material. **Not medical advice; no dose, route or schedule for any person.** Reference genotype class: a WWOX-DEE genotype class; no individual-level record. Association is not modulation and modulation is not rescue. Every laboratory experiment below is **PROPOSED, never run**.

## 0. Decision in one paragraph

Neither registered lead resolves an open WWOX question, and **transfer of both to WWOX is UNVERIFIED**. What each does change is the design and the reading of data we already hold: (a) the Brain 2024 paper (PMID 37804316) is a lesion in which an ISR is *protective*, opposite in sign to the other DEE-type mitochondrial precedent already in the card (PMID 41380592, harmful), so the sign of any WWOX ISR cannot be inferred from "mitochondrial lesion" and the E01 card's attenuation-only framing is incomplete; the paper also leaves the kinase untested in vivo and the mechanism of its drug disputed; (b) the PNAS 2026 paper (PMID 41706892) shows ATF4 protein rising within minutes of mGluR activation without an mRNA change, which (i) confirms that ATF4 mRNA is not an ISR readout (already stated in the context matrix) and (ii) adds a confound that no earlier design carried: WWOX-deficient neural systems are hyperexcitable in every system that measured it, so an ATF4 protein rise there needs an activity-silencing arm before it can be read as stress. No new ISR conclusion about WWOX is drawn.

## 1. Observation (what was read, at what depth)

Receipts staged: `FTR-20261029-37804316-01`, `FTR-20261029-41706892-01` (both `partial_fulltext_read`, closed coverage vocabulary, understated; recorder not run by me). Locators in `loop1_readings.tsv`. Open questions served: which eIF2 kinase; ATF4 protein versus mRNA; compensatory versus harmful; endpoint and window.

**Brain 2024, AFG3L2 loss (spastic ataxia type 5, myoclonic epilepsy in the clinical spectrum).** Full text read; Figures 1, 4, 5 opened as images (`files/supplement/PMID37804316/awad340f1.jpg`, `f4`, `f5`). What it shows and does not show:

* ISR is present and **postnatal and progressive**: P-eIF2a/total and Atf4, Chop, Fgf21 mRNA are not different at P1 (Fig 1E-F, n = 3 to 6) and are raised at P14 in cerebellum (Fig 1C-D; Atf4 mRNA about 0.8 to 1.4 normalised). Atf4 *mRNA rises* here, unlike the flat or lower Atf4 mRNA in the WWOX systems (context matrix Q01) - one reason not to pattern-match.
* **Kinase.** HRI and DELE1 enter only through siRNA in one patient fibroblast line (two patients for P-eIF2a baseline; silencing in patient 2, 3 to 8 experiments): silencing lowers P-eIF2a and slows growth in low-glucose medium (Fig 3). In mouse cerebellum no kinase, DELE1 or HRI measurement exists: the text says no DELE1 antibody is available, and DELE1 cleavage is shown only for HA-tagged DELE1 over-expressed in HEK 293T with AFG3L2 knock-down. **GCN2, PERK and PKR are not tested anywhere** (full text). So "OMA1-DELE1-HRI" is a candidate arm supported in one cell type, not a measured kinase in the brain.
* **Protective versus harmful.** Necessity: DELE1 or HRI silencing worsens fibroblast growth (control cells slightly, not significantly). Sufficiency/potentiation: Sephin-1 raises P-eIF2a only in patient cells (about 0.75 to 1.3 at 24 h, n = 3, decaying by 72 h, Fig 4B), raises live-cell percentage modestly (about 62 to 72 percent, Fig 4A), restores Purkinje neuron number in culture and raises dendrite area to roughly a third of wild type (Fig 4E, read from the plot). In vivo: survival extended by about 10 days (Fig 5C: vehicle knock-outs die by about day 15, treated by about day 24; the step size suggests about 5 treated animals, a reading), Purkinje morphology class and cristae classes improved (n = 3 mice, chi-square on pooled cells), pyruvate-stimulated mitochondrial ATP restored to wild-type level (Fig 5F). **Effects in wild-type animals are not neutral**: wild-type mitochondrial class I fell from about 80 to about 50 percent and wild-type ATP fell with Sephin-1 (Fig 5E-F, reading). **P-eIF2a in treated mice is not reported**, and the in-vivo gain-of-benefit is not linked to the ISR by any genetic test in the animal. The authors themselves propose a second mechanism (attenuated mitochondrial translation) and say the target at mitochondrial level "certainly deserves further investigation".
* **Drug mechanism is disputed.** According to PubMed, PMID 28447936 (eLife 2017, [DOI](https://doi.org/10.7554/eLife.26109)) found Sephin1 and guanabenz inert on the PP1-PPP1R15A complex in vitro and without effect on eIF2a-P dephosphorylation in cells (abstract level). The Brain paper's "Sephin-1 inhibits GADD34" is therefore a premise, and its p-eIF2a rise in patient cells (Fig 4B) is the only supporting datum in that paper.
* **Window.** Treatment began prenatally (E14, gavage of the dam) and continued daily from day 1; the phenotype is lethal at about day 14. This is an early-window protection of a lesion present from embryogenesis; no post-onset arm exists.

**PNAS 2026, mGluR and ATF4 in mouse hippocampus.** Full text read, legends only for figures; Dataset S1 and the SI PDF acquired (`files/supplement/PMID41706892/`) but not analysed.

* DHPG (100 uM, 5 min) in slices: ATF4 protein about 2.5-fold, P-eIF2a about 2.3-fold, **Atf4 mRNA unchanged** (n = 3 per group, paired t test, ATF4 P = 0.047, mRNA P = 0.75). In cultured neurons (DIV8, 60 min) both rise about two-fold (n = 4); a uORF reporter rises about 1.5-fold. P-eIF2a rises with ATF4, so the dissociation is from mRNA, **not from eIF2a phosphorylation**; the eIF2 kinase is not identified.
* ATF4 deletion in excitatory neurons (Camk2a-Cre, from about postnatal weeks 2 to 3; slices at P30-60) impairs mGluR-LTD (87 versus 71 percent of baseline, 10 slices from 7 mice per group) and object-place learning (n = 10 and 12, P = 0.049); the OXPHOS proteins that DHPG lowers in wild type are not lowered in the knock-out, and a complex I inhibitor (30 nM) restores LTD in the knock-out. Proteomics n = 3 per group.
* The stimulus is a normal-physiology receptor activation, not a stress and not a disease; ATF4 here is a plasticity effector and, by the authors' RNA overlap (12 genes), a repressor of OXPHOS genes.

## 2. Inference (what the two readings license)

1. The sign of a mitochondrial-origin ISR is lesion-dependent: protective in the AFG3L2 model (HRI/DELE1 loss and, by the authors' interpretation, Sephin-1 potentiation), harmful in the PARS2 fly (GCN2 or ATF4 RNAi reduces bang sensitivity, need observation O6). Two precedents with opposite signs fix no prior for WWOX.
2. The AFG3L2 evidence for a *kinase-specific* protective role is a fibroblast-siRNA result. It does not exclude GCN2 or PERK in the brain and does not show HRI in vivo.
3. ATF4 mRNA cannot report ATF4 protein in neurons, in either direction; ATF4 *target* transcripts remain a usable (indirect) readout, which is how the existing sign conflict was built (context matrix Q02). The PNAS paper does not change Q02; it removes any temptation to read Q01.
4. Activity is a second route to raised ATF4 protein and P-eIF2a in neurons. Hyperexcitability is the most concordant WWOX quantity (Q14, higher in every system that measured it). A raised ATF4 protein in a WWOX-deficient hyperexcitable network is therefore ambiguous between proteostatic stress and activity.
5. ISR-dependence of Sephin-1 benefit is unproven even in its own paper (no in-vivo P-eIF2a, disputed target, effects in wild type).

## 3. Hypotheses (non-ledger, mutually exclusive, falsifiable)

For WWOX-deficient neural cells at matched maturity (isogenic corrected control): **H-a** ISR raised beyond activity, protective (kinase loss worsens an endpoint; potentiation improves it); **H-b** ISR raised beyond activity, harmful (kinase loss or attenuation improves an endpoint); **H-c** ATF4 protein/P-eIF2a raised only through activity (silencing with TTX normalises it); **H-d** no change. The ledger is not edited here.

## 4. Biological need

`NEED-ISR-ATTENUATION` carries the sign as "attenuate a presumed over-activation". After this loop the need is better stated as "the sign and the kinase of any WWOX-dependent ISR": the attenuation framing is one of two arms. The need keeps its id, goal (partial benefit) and direction `uncertain`; its text gains the observations and inferred lines of section 7.

## 5. Search of interventions (catalogue, cards, ChEMBL adapter; run 2026-10-29, `LEGEND_CATALOG_CACHE` set)

`interventions.tsv` has the rows. Summary: eIF2B activators: fosigotifator is a ChEMBL clinical candidate record without a mechanism row; DNL343 and 2BAct are not in the catalogue (name search, 0 matches; a zero about the catalogue, not about existence). PERK arm: two DGIdb-only inhibitor records (GSK2606414, GSK2656157), no approval status. HRI arm: three DGIdb-only records, none approved (one is a RIPK1 inhibitor). GCN2 arm: ChEMBL holds 811 activity rows on CHEMBL5358 (first 50 read, truncated; not interpreted); the approved records linked to EIF2AK4 are antipsychotics (pharmacogenomic associations, per the 2026-10-28 note). GADD34 potentiators: **Sephin-1 and icerguastat are absent from the catalogue and from ChEMBL molecule/mechanism search (`NO_MATCH_FOUND`)**; guanabenz has a ChEMBL record whose only curated mechanism is alpha-2 adrenergic agonism (no PPP1R15A mechanism); the only ChEMBL activity row on PPP1R15A is one guanabenz isomer (CHEMBL2369159, 2,3-dichloro) with IC50 977 nM on PPP1R15A and 33 nM on PPP1R15B from a 2020 review document (primary assay not traced: UNVERIFIED), the opposite of the selectivity the potentiator premise needs. A genetic route (kinase knock-out, uORF-reporter) stays a genetic tool, not an intervention. No compound is prioritised.

## 6. Comparison and next experiment (PROPOSED)

Existing design (`isr_kinase_interactome_atf4_reconciliation_it4_20261028.md` section 6) stays the backbone. This loop adds **five things**, each from a source read here:

1. **Activity arm.** Every ATF4 protein / P-eIF2a read in a neural line is run with and without activity silencing (tetrodotoxin; an mGluR5 antagonist as a second arm), in matched-maturity cultures, because the PNAS stimulus raises both within minutes (5 to 60 min).
2. **Time arm relative to hyperexcitability.** Sample before, at and after the first measured hyperexcitability (organoids: week 7 was already hyperactive, PMID 42397075; weeks 7, 10 and 16): a rise that precedes the network phenotype is a candidate cause, one that follows it is a candidate consequence. The Brain paper's own P1-versus-P14 contrast is the template.
3. **HRI-arm trigger readouts that do not need a DELE1 antibody**: OPA1 long/short ratio and OMA1 level (Fig 1A of the Brain paper), mitochondrial membrane potential, plus genetic EIF2AK1 and DELE1 loss; DELE1 cleavage only with an HA-tagged construct (as the authors did). Whether WWOX loss triggers OMA1 is unmeasured in any held dataset.
4. **Potentiation arm beside attenuation**, only if Stage 1 is positive: a GADD34-targeting compound is tested *with a target-engagement control* (eIF2a-P decay after kinase shut-off, the assay of PMID 28447936) because the target is disputed; effects in the isogenic corrected line are read beside those in the knock-out (the AFG3L2 wild-type effects show why). Endpoints: network firing, Purkinje/neurite measures where a cell type allows, ATP synthesis with a substrate-stimulated assay, survival of cells under challenge.
5. **Kinase attribution by genetic interaction** (EIF2AK1/2/3/4 loss x WWOX genotype) with the pre-registered decision table of the IT4 note, extended below.

Decision table (thresholds set by the experimenter before the run):

| Observation (WWOX-null vs isogenic corrected, matched maturity) | Reading | Not shown |
|---|---|---|
| P-eIF2a and ATF4 protein not raised, controls intact | H-d; compound strand parked | other cell types, challenges |
| Raised; normalised by TTX/mGluR5 arm | H-c: activity route; no ISR lever | that stress is absent |
| Raised after silencing; removed by loss of one kinase only (interaction), rescued by WWOX re-expression | that kinase engaged | directness; sign |
| ... and kinase loss worsens an endpoint | H-a (protective) | in vivo |
| ... and kinase loss or attenuation improves an endpoint | H-b (harmful) | in vivo |
| Raised, not removed by WWOX re-expression | culture or clone artefact | |

Alternative readouts if antibodies fail: ribosome profiling or puromycin incorporation, ATF4 target mRNA panel (ASNS, CHAC1, TRIB3, DDIT3), a uORF-GFP reporter (as PNAS, Addgene plasmid named there). Discriminating criterion: a genotype x silencing x kinase interaction, not a main effect.

## 7. Regenerated queue (what was edited, and why that far)

* `needs/needs.json`, `NEED-ISR-ATTENUATION`: observations `O9` (AFG3L2) and `O10` (PNAS) as `OTHER_DISEASE_PRECEDENT`, three inferred lines, one counter-evidence line, `sources` (documents, papers). Direction stays `uncertain`.
* Card `E01_isr_modulators` (packet, rebuilt): `not_known` and `next_measurement` gain the activity arm, the time arm and the potentiation arm; positions are re-derived by rule (section 8 of the root README of this package).
* `view/work_order.json` entry of the ISR need: question and data updated; docs entry `IT8-P5` added.
* Not edited: hypothesis ledger, registries, receipt ledger (listed in the package README).

## 8. UNVERIFIED

Primary assay behind the ChEMBL PPP1R15A row; whether the Lancet Neurol guanabenz reading used the same mechanism (abstract-level source, not re-read); supplementary data of the Brain paper (PDF and videos not opened); the Fig 4/5 readings of values and n are from the printed plots; the PNAS figure images and SI Appendix were not opened (legends only); whether WWOX loss engages OMA1 at all; that the activity route raises canonical ISR target transcripts (the PNAS paper measured only Atf4 mRNA).

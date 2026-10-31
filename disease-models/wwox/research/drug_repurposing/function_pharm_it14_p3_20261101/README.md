# IT14 P3: function-first pharmacology of the Wwox neuron-deleted network (one question, four contrasting cases)

Scientist, task `ORCH-ROADMAP-IT14-20261101`, package P3, branch `task/it14-p3` (from `task/it14`), 2026-10-31 (Europe/Rome). Public edition, WWOX-DEE genotype class, no individual-level record. Exploratory, non-canonical, **not medical advice**; no regimen is given. No e-mail, personal datum or registration was sent to any service; no spend; nothing here edits a card, need, ranking, registry, current file, view or ledger (proposals are in section 9).

## 0. Decision (first)

1. **No compound is supported as a candidate. One hypothesis is formulated and made testable, and one earlier proposal is demoted.** The function chosen is synaptic (GABA-A) inhibition onto layer II/III pyramidal cells in Wwox neuron-deleted neocortex. The hypothesis is that restoring fast inhibitory charge, by a gamma2-dependent benzodiazepine-site potentiator (clobazam with its metabolite N-desmethylclobazam), compensates the KO-specific inhibitory loss and lowers d-APV-sensitive bursting. It is a probe-level hypothesis, for ex vivo use. What prevented anything stronger, after the work was done: (i) the **locus of the lost current is unmeasured** (receptor-limited or release-limited); (ii) the **heterozygote versus wild-type inhibitory comparison is not reported** (Fig 4H pools controls); (iii) **no public catalogue states a subtype potency for clobazam or its active metabolite** (ChEMBL has no GABA-A activity row for either; IUPHAR/BPS has no interaction row for clobazam; DGIdb lists 19 GABA-A subunit genes as "positive modulator" by class propagation, with no values); (iv) no GABAergic drug has been tested in any WWOX preparation.
2. **The discriminating step I found is a correction of IT13 P3a.** Breton's Table 1 (read in full) shows the intrinsic changes P3a built the Kv7 proposal on (resting potential -79.25 WT, -75.51 HT, -73.62 KO mV; input resistance 102.9, 143.3, 143.0 MOhm; sag 1.18, 2.04, 2.57) are already present in the **heterozygote**, where bursts occur in 4 of 23 slices (KO 36 of 42, WT 0 of 11; Fisher two-sided KO v HT p = 7e-8; HT v WT p = 0.28, computed in `design_counts.py`). The depolarisation is graded with gene dose and shared; the burst incidence is not. So a depolarised resting potential is not the KO-specific step, and the Kv7 opener (ezogabine) is demoted from "new proposal" (P3a C2) to a **refuter arm**. The only functional deficit stated as KO-specific is the inhibitory one (KS tests of sWT v sKO and sHT v sKO both significant, on pooled events, so pseudoreplicated).
3. **Experiment (section 6):** a same-cell triad in KO, HT, WT (NMDAR current, sIPSC charge, Vm/Rin), a **sufficiency matrix in WT/HT slices** (titrate each single deficit to its KO-measured magnitude and ask which one yields d-APV-sensitive bursts), single-mechanism **corrections in KO slices** with suppression controls, and a secondary-state covariate arm. Predictions and what would change the ranking are fixed in section 6 and were written before the experiment (the sufficiency logic was fixed in `PRE_REGISTRATION.md`, committed before any compound search).
4. **Engine v4 was not used**: IT13 showed it does not fit channel/synaptic biology; the ladder here is function, target, action, molecule, from ChEMBL, IUPHAR/BPS bulk data, DGIdb and openFDA labels.

## 1. What I read, and what I knew

Depth per source in `source_log_it14_p3.tsv`. Read: P3a, P3b, verify-P3a READMEs and tables; IT6 P9 sections 1 and 2; needs entries NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR, NEED-INHIBITORY-HYPOFUNCTION, NEED-GABA-CHLORIDE-GRADIENT, NEED-T-TYPE-CALCIUM (first observations); card `p4_fields` of F01, F03, F04, H01, P11; units U17, U21, U23; the phenotype-first table; and the **primary text of Breton 2021** (Results 2.1 to 2.6, Table 1, Fig 3 to 6 legends, pharmacology Methods, Discussion 3.5; Fig 4 image viewed). Not read: Breton supplementary figures, Repudi 2021, Cheng 2020 (relied on the IT13 text), the vigabatrin case reports (relayed through U20 and the EB-VGB-01 assertions, queried not full read).
Known before looking: the d-APV result, the sIPSC halving, the 5 mV depolarisation as P3a used it, the IT13 failure of engine v4. **Not known before looking, and decisive:** that the heterozygote shares the depolarisation, input-resistance and sag changes (it had been pooled with WT as "control" in the sIPSC and in P3a's reading), and that sIPSC recording used a KCl internal solution.

## 2. The question and the contrast (scored before the ladder)

Scoring of nine candidate functions (R relevance, M measure, D discrimination, P pharmacology, V verification, each 0 to 3) is in `question_scoring.tsv`; fixed in `PRE_REGISTRATION.md` before any compound search. Result: inhibitory transmission 13, NMDAR/Mg2+ 12, intrinsic Vm/Rin 11, HCN 9, PV firing 9, Kv7 8, gap junction 6, T-type/GIRK 6, chloride 5. **The margin over NMDAR is one point and rests on one judgement (D = 3 v 2); it is not a robust ranking.** The tie-break was pre-registered: the question whose experiment also supplies the others' measurements. NMDAR stays in as rival and as the second measurement of the triad.

**Question.** In the Wwox neuron-deleted neocortex, is the loss of fast GABA-A inhibition onto layer II/III pyramidal cells the step that converts a graded intrinsic phenotype (shared by HT and KO) into d-APV-sensitive bursting? If so, which way of restoring inhibitory charge acts on that step without suppressing the network generally?

| Rival (same bursting) | Generated by | Separating measurement |
|---|---|---|
| R1 NMDAR gain | d-APV abolishes bursts; delayed NMDAR-dependent evoked response; mEPSC amplitude about 6 percent higher (AMPAR-weighted) | isolated NMDAR current KO v HT v WT; partial-block concentration-response; WT slices at matched trigger |
| R2 intrinsic depolarisation | Vm +5.6 mV, Rin +40 percent, sag, rebound (all graded, HT shares) | Vm-matched WT/HT slices (bath K+); XE991-sensitive current; Kv7 opener at Vm-restoring concentration |
| R3 disinhibition (chosen) | sIPSC amplitude 57.3 to 27.5 pA, frequency 10.3 to 8.4 Hz (pooled controls); interneuron AP amplitude 60.8 to 45.0 mV (n 5, 6); Pvalb mRNA lower 4 of 4 | IPSC charge KO v HT v WT; gabazine-titrated WT/HT; restoration in KO |
| R4 secondary state | hypomyelination (myelin set -0.8 to -1.8 in P3a), systemic illness in these mice | covariates; matched-trigger WT; any burst difference not explained by genotype |
| R5 gap-junction/pannexin propagation | carbenoxolone 100 uM lowered burst frequency 87 percent | not pursued: no selective agent to ladder |

Limits of the source preparation that bear on the question: sIPSC measured with KCl internal (so amplitude carries no information on E_GABA; the chloride question cannot be answered from it); recording and incubation Mg2+ 1.3 mM, K+ 3.5 mM; P13 to P17; one laboratory; "Ih elevated" is read from sag in mV at a fixed current step, which scales with input resistance.

## 3. The ladder (`ladder_it14_p3.tsv`, 12 relations)

Each relation: function, target (species, context), action (state dependence), molecule identity (parent, metabolite, salt, stereo), values as the source states them, endpoint, limits, status. Highlights:

* **Identity that the catalogues do not settle.** Vigabatrin is a racemate in ChEMBL (chirality 0) and the US label; the active enantiomer is prior knowledge here, unverified. The clobazam active metabolite N-desmethylclobazam is CHEMBL2260842 and has one ChEMBL row, a UPLC retention time. Ezogabine is retigabine (CHEMBL41355), distinct from flupirtine (CHEMBL255044). ChEMBL `withdrawn_flag` is False for ezogabine; openFDA returned no label for it (HTTP 404); its commercial discontinuation is prior knowledge, not verified.
* **Potency, as stated.** Tiagabine hGAT1 IC50 70 nM against rat GAT2 1.41 mM, human GAT3 917 uM, hBGT-1 1.67 mM (ChEMBL doc CHEMBL1127589; species mixed). Ezogabine EC50 0.43 uM (human KCNQ2/3, Rb efflux), 1.3 uM (mouse KCNQ2, HEK), 4.38 uM (KCNQ2/3 FLIPR thallium): a 10-fold spread for one compound across assays. Azetukalner KCNQ2 98 nM, one assay, one origin, not carried. Radiprodil GRIN1/GRIN2B 4 nM (Ca2+, human cells), 69.9 nM (HEK293 NR1a/NR2B), mouse NR2B 3.162 nM. Vigabatrin human GABA-T Ki 850 uM is a time-dependent inactivation constant. Subtype tools (GtoPdb, compositions differ per row): zolpidem alpha1 pKi 7.39 to 7.68, alpha2 6.12, alpha3 5.67; clonazepam 8.70 to 8.90 non-selective; diazepam 7.77 to 7.79.
* **The gap that stops H1.** For clobazam the catalogue chain ends at class: ChEMBL mechanism PAM at the GABA-A complex (CHEMBL2093872); 112 numeric activity rows, none on a GABA-A receptor; GtoPdb ligand 7149 has no interaction rows; DGIdb lists GABRA1 to GABRA6, GABRB1 to 3, GABRG1 to 3, GABRD, GABRE, GABRP, GABRQ as positive modulator with no values, which shows how a complex-level mechanism is propagated to every subunit gene. The diazepam, clonazepam and zolpidem rows are not carried to clobazam.
* **Labels (US, consultation facts only).** Vigabatrin: boxed warning permanent vision loss; infantile spasms and refractory focal seizures, 2 years and over for the latter (label 2026-06-15). Clobazam: LGS adjunct, 2 years and over; boxed warnings; mechanism "thought to involve" the benzodiazepine site; metabolite steady state 9 days, CYP2C19 effect (2026-07-09). Tiagabine: 12 years and over, partial seizures (2021). A label is not evidence of benefit in WWOX.
* **Licence.** IUPHAR/BPS data are ODbL (database) with CC BY-SA 4.0 contents; attribution and share-alike apply to extracts (`results/gtopdb_rows.tsv` is such an extract, 41 rows, version 2026.3.1). The REST service needs a registered key (HTTP 401) and was not used; the public bulk files were.

## 4. The cases (`cases_it14_p3.tsv`, full 7-point statements and separate evaluations)

| Id | Role | Intervention | State | Ex vivo probe | Next experiment | Systemic plausibility (kept apart) |
|---|---|---|---|---|---|---|
| K1 | (a) reference, preparation | d-AP5 | REFERENCE | readout control, not a mechanism test | every slice, last step | not applicable |
| K2 | (a) reference, human anecdote | vigabatrin | KNOWN; not a test of the sIPSC deficit | poor (slow inactivation) | low; belongs to H02 | exposure and MRI limits recorded in H02 |
| H1 | (b) function-first hypothesis | clobazam + N-desmethylclobazam; zolpidem v clonazepam to attribute subunit | HYPOTHESIS; selectivity GAP | good, with parent and metabolite | first drug arm after the triad | label and class facts only; no WWOX result |
| A1 | (c) different mechanism, same function | tiagabine (tool NNC-711) | ALTERNATIVE | good | second drug arm | label 12 years and over |
| D1 | (d) refuter | ezogabine with XE991, ICA-069673 | COUNTER-HYPOTHESIS | good as refuter | third arm | not assessed |
| T1 | tools | gabazine titration, bath K+, TTX | TOOL | defines sufficiency | first | none |

Hypothesised benefit is stated by class: for H1, A1 and D1 only "acute effect on bursts during exposure" and "compensation of an impaired function" (inhibition for H1/A1, Vm for D1); persistence after cessation and broader WWOX recovery are **not** hypothesised, and neither layer-marker recovery nor persistence is required to call a result partial benefit. What LEGEND adds for the known compounds is the context (sufficiency matrix with the heterozygote as discriminating control; charge rather than amplitude; metabolite included), not the name; a new name alone is not claimed.

Chain for H1: Breton sIPSC halved and KO-specific (WWOX observation) -> locus unmeasured, taken as receptor-limited for the hypothesis (inferred step) -> GABA-dependent potentiation at gamma2-containing receptors (action; benzodiazepine-site mechanism, ChEMBL class record) -> in KO slices at the preparation's own inhibitory synapses (system) -> restored inhibitory charge and lower burst frequency during exposure (benefit class: compensation). It is weakened if charge is restored and bursts continue, or if WT matched-trigger bursts fall equally (symptom suppression). A1 differs by being release-limited-dependent, which is why H1 and A1 together separate the two loci.

## 5. Control against suppression artefacts

Any firing- or burst-reduction readout counts only with: F-I curve, input resistance, AP height and viability unchanged; evoked fEPSP slope unchanged in WT; wash-out; the same agent on WT matched-trigger slices (suppression index: effect in WT at most half that in KO); TTX as the generic silencer reference. Silencing is trivially achieved by many agents (P3b C3/C6), so burst reduction alone is symptomatic.

## 6. Falsifiable prediction and design (`experiment_arms_it14_p3.tsv`)

Fixed before the experiment: (E0) HT sIPSC charge at least 80 percent of WT and KO at most 55 percent; NMDAR current in KO not raised by more than 25 percent over WT. (E1) In WT/HT slices, gabazine titrated to the KO-measured IPSC charge fraction yields d-APV-sensitive bursts in at least twice the fraction produced by a bath-K+ depolarisation of 5.6 mV. (E2) In KO slices, restoring IPSC charge stops at least half of the burst frequency and restoring Vm alone does not; each agent acts at most half as strongly on WT matched-trigger bursts. Size: 12 slices per arm from at least 6 animals gives exact power about 0.94 for 0.80 v 0.17 and 0.64 for 0.60 v 0.17 under independent slices (`results/design_counts_output.txt`); animal clustering lowers both, so the animal is the unit and slices are nested.

| Outcome | Ranking and needs consequence |
|---|---|
| E0 shows HT inhibition reduced like KO | Q-inh loses KO specificity; NMDAR leads; H1/A1 drop to controls |
| E0 shows NMDAR current raised | R1 leads; the GluN2B NAM arm (radiprodil) becomes the main correction; F04 design applies |
| E1 (ii) equals (i) | intrinsic depolarisation is sufficient as well; D1 rises; no single step |
| Neither (i) nor (ii) nor (iii) bursts | interaction or secondary state (E3); every drug arm is symptomatic |
| E1 (i) > (ii), E2 as predicted | inhibition is the KO-specific step; H1 and A1 become the first slice arms; need NEED-INHIBITORY-HYPOFUNCTION gets its measurement |

Corrections to earlier designs: **P3a** (Kv7 opener on depolarisation) lacked the heterozygote as control and a Vm-matched WT arm, and read sIPSC amplitude with a chloride internal that does not mimic E_GABA; **P3b** (organoid TTX and D-AP5) has no inhibitory readout in the human system, so it stays a firing-level arm and is not duplicated here; the organoid E/I signals (GABRB2/3 and NPY transcripts, GAD67 area) are composition-confounded (P3a).

## 7. What must be independently verified

1. **Pharmacological identity and action.** (a) That the relation "clobazam, parent and N-desmethylclobazam, positive allosteric modulation at gamma2-containing alpha1/2/3/5 receptors" is quantified at all: a primary source for subtype potency of both molecules (ChEMBL and IUPHAR hold none); until then H1 is an experimental, not a pharmacological, hypothesis. (b) Vigabatrin enantiomer activity (prior knowledge). (c) Ezogabine's discontinuation and safety history (prior knowledge, not verified; no openFDA label). (d) That tiagabine's GAT1 selectivity (mixed species) holds in mouse neocortex.
2. **The decisive premise.** That the heterozygote's inhibitory current is near wild type. Fig 4H pools controls; the text lists significant KS tests for sWT v sKO and sHT v sKO but none for sWT v sHT, and the unit is pooled events. Reading Breton's source data (not deposited in what I read) or recording E0 settles it. A second, independent premise: that the depolarisation is truly shared by HT (Table 1 asterisks are v WT, unpaired t-tests, n 13/15/40 cells from 5/6/15 animals; HT v KO not tested separately, a 1.9 mV difference).
3. Verifier to check my reading of Table 1 and the Fig 4 legend against the XML (`files/fulltext/PMID34634460_Breton2021_PMC.xml`) and the arithmetic in `design_counts.py` (pure python, deterministic).

## 8. Limits

Transcript statements about Gabr* and Kcnq* come from P3a's deposit tables (n 2 to 4 animals per arm; Cre-line controls differ from WT; whole hippocampus or cortex, not layer II/III) and show presence only. Catalogue values are recombinant-cell data with mixed species and assays. No figure was digitised; Table 1 values are text. Prior-knowledge statements are marked UNVERIFIED. The scoring is mine, fixed in advance, and the first two places are one point apart. No therapeutic suitability is shown; a good ex vivo result would not demonstrate it either.

## 9. Edits this implies (proposals; I changed none)

* **needs.** NEED-INHIBITORY-HYPOFUNCTION: add observation "heterozygote shares the depolarised Vm, higher Rin and larger sag but bursts in 4 of 23 slices; inhibitory loss is the only stated KO-specific deficit (pooled-event tests); sIPSC measured with KCl internal"; next measurement: IPSC charge KO v HT v WT. NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR: add the same HT fact (R1 not reduced by it). NEED-GABA-CHLORIDE-GRADIENT: add that the source's KCl internal makes sIPSC amplitude uninformative on E_GABA. A new need candidate "KO-specific inhibitory charge restoration in the Breton preparation" (REQUIRES_QUALIFICATION), not scored.
* **cards.** F03 unchanged (abstention stands). P3a candidacy C2 (Kv7) re-labelled "refuter arm", not "new proposal". A new card candidate for clobazam/N-desmethylclobazam would be premature: its state is IDENTITY/SELECTIVITY GAP; the gap is the record.
* **triggers.** Reopen H1 when (i) a subtype potency for clobazam and N-desmethylclobazam is published or deposited, or (ii) E0 locates the inhibitory deficit (receptor- or release-limited), or (iii) Breton's source data show HT v WT inhibition.
* **work order.** An ex vivo slice experiment (E0 to E2) with the group that holds the preparation, or with source data if offered; no further in silico step is useful for this question. DrugCentral was not reached and could be added to the identity rung.
* **ranking.** None. U17, U21, U23 unchanged; the ladder values may be attached as comparison-table rows after verification (radiprodil mouse NR2B 3.162 nM; tiagabine hGAT1 70 nM; ezogabine EC50 spread).
* **Harness.** matching_guidance_v3 logic 8 (direct phenotype rescue) and the "function -> target -> action -> compound" route worked without the engine; the useful discipline was reading the genotype-by-genotype table before choosing the function (HT as a control that P3a lacked).

## 10. Files

`README.md`, `PRE_REGISTRATION.md` (committed first), `question_scoring.tsv`, `ladder_it14_p3.tsv`, `cases_it14_p3.tsv`, `experiment_arms_it14_p3.tsv`, `source_log_it14_p3.tsv`; scripts `extract_gtopdb.py`, `pull_chembl.py`, `pull_chembl_activities.py`, `pull_openfda_labels.py`, `design_counts.py` (all with `--help`, executable); `results/` (`gtopdb_rows.tsv`, `chembl/`, `openfda_labels.tsv`, `design_counts_output.txt`); `inputs/gtopdb_SHA256SUMS`.

# P9 (iteration 6): which kind of NMDA-receptor intervention could discriminate the mechanism of the Wwox neuron-specific bursting phenotype

Scientist delegate `scientist-a`, 2026-10-29, task branch `task/it6-p9`. Non-canonical research material. It changes none of the four
scientific current files and writes nothing to the receipt ledger. Not medical advice; no dose, schedule or individual recommendation
appears (assay concentrations and potencies are published-experiment conditions, listed as data). Association is not modulation is not
rescue. No registration, no contact address sent anywhere, no spend, no keyed service: ChEMBL REST, PubChem PUG REST, HGNC REST,
Europe PMC, NCBI efetch, ClinicalTrials.gov API v2 and openFDA were read key-less. The reference genotype class is not individualised.

Everything marked **UNVERIFIED** was not checked at a primary source. A different verifier will audit the locators from the sources;
section 9 lists each source with the depth at which it was actually read.

---

## 1. Decision

**The research decision.** Which NMDAR-class intervention should be the *discriminating arm* of the first pharmacology experiment on the
Wwox neuron-specific knockout cortex, and may any drug be carried forward on the strength of the d-APV result alone?

1. **No NMDAR drug is carried forward as a candidate on the d-APV result.** d-APV (a complete competitive block, 50 uM, five slices from
   three animals) shows that bursting *needs* NMDAR activity. It does not show that NMDAR function is raised. Three readings fit it and
   make different predictions (section 3): NMDAR gain; permissive necessity in a network whose pyramidal neurons are about 5 mV
   depolarised and receive spontaneous inhibitory currents of about half the amplitude; an AMPAR-led drive. **The data do not separate
   them, and they are not ranked here.** The inhibitory deficit supports a disinhibition component; the source's significant increase of
   the mEPSC amplitude (pooled events; the excitatory amplitude means differ by about 6 percent, 24.7 against 23.3 pA, wild type and
   heterozygote pooled as controls) supports at most an AMPAR component, because an mEPSC at -70 mV in Mg2+ is AMPAR-weighted and carries
   no NMDAR information (section 2). No NMDAR-specific measurement exists; the one indirect indicator, the mEPSC decay time constant
   (5.18 against 4.84 ms, p 0.30), shows no change and does not exclude one. The isolated NMDAR current (step E1, section 7) is the
   measurement that decides between the readings.
2. **The pharmacological arms are chosen for what they can read out, and none of them replaces E1.** A GluN2-subunit-selective negative
   allosteric modulator (NAM) is the first drug arm; memantine and perampanel are not. Reasons, each checked in sections 4 to 6:
   * a NAM has a ceiling below complete inhibition, so its concentration-response gives an exploratory read-out of how much NMDAR current
     must be blocked to stop bursting (F*). F* is **defined only if bursts are abolished at the plateau**: a GluN2B NAM blocks only the
     GluN2B-containing fraction, so if bursts persist at the plateau the result is "persists at the plateau fraction", not an F*. F* is a
     property of network gain, not of which reading is true: a threshold network can stop at partial block with a normal receptor, and a
     raised receptor can still need most of its current blocked. The per-reading predictions in section 3 are therefore *expectations to
     be tested*, not derived results;
   * d-APV cannot supply F* unaided: its block is competitive and surmountable, so the glutamate transient inside a burst lowers the
     effective occupancy below the upper bound computed at agonist well below EC50 (section 4). Evoked currents at matched agonist level
     are the safer route to F*;
   * a GluN2B NAM has a clinical-stage member (radiprodil) with human exposure (adults including healthy volunteers, three infants,
     registered paediatric studies), a seizure-protection peak in rat pups at postnatal day 12 (no species age mapping to the mouse
     window of postnatal day 13 to 17 is available in the sources read: the rat and mouse ages are *not* shown to be equivalent), and in-vitro
     activity at most tested gain-of-function GRIN variants; the *tool* stand-in (Ro 25-6981) and the clinical compound are different
     substances, and the tool result is carried to the drug only after the drug itself is tested;
   * the clinical pore blockers are poor first discriminators in *this* preparation: extracellular Mg2+ weakens memantine block of
     GluN2A/2B about 20-fold at rest voltage but of GluN2C/2D only about 3-fold (abstract level), and block of GluN2A rises with
     intracellular Ca2+ (Phillips 2026); the preparation's incubation solution held 1.3 mM Mg2+. A memantine effect there may be a
     GluN2D-containing interneuron effect (disinhibition), a null may be an Mg2+ artefact. A further point, deliberately **not** used in
     the argument: one closed 2024 document lists 30- to 107-fold potency changes for a 20 mV change of holding potential; a
     single-site pore block of electrical distance at most 1 predicts at most about 2-fold per 20 mV, so those numbers are UNVERIFIED and
     possibly a protocol or transcription effect, like the 0.95 nM outlier (section 5). Memantine is the *translation probe* after the
     receptor-level answer, with Mg2+ and voltage stated, not the first discriminator (F01 had proposed it as the first).
3. **An AMPAR antagonist (perampanel, NBQX) cannot discriminate.** AMPAR depolarisation relieves the Mg2+ block, so AMPAR block is expected
   to stop an NMDAR-dependent burst whichever reading is true (inference). Perampanel is the only class with a paediatric label (from
   4 years, partial-onset seizures, boxed psychiatric warning) and is kept as a comparator for the *AMPAR contribution*, not as a mechanism test.
4. **Complete competitive block cannot discriminate either** (it is the experiment already done); its clinical relative (selfotel) was stopped
   in adult trials (stroke: an early mortality imbalance; head injury: stopped for concern about deaths and futility, with no significant mortality difference in the later analysis). Glycine-site agents are secondary: their effect depends on the glycine/D-serine level, unmeasured in
   the slice, and a partial agonist can activate otherwise quiet receptors (review statement).
5. **Human exposure by class** (section 4 table): clinical exposure exists for selfotel (adults, failed), memantine/ketamine (adults, other
   labels; memantine has no paediatric effectiveness on its label), radiprodil (adults, n 3 infants, registered paediatric studies in
   gain-of-function GRIN disease and TSC/FCD), D-cycloserine (antibiotic label), perampanel (paediatric label). Tool compounds only (no human
   exposure found; ChEMBL lists no development phase): d-APV, dizocilpine, Ro 25-6981, TCN-201, NVP-AAM077, NAB-14, L-701,324,
   7-chlorokynurenic acid, NBQX, GYKI 52466.
6. **What would close the strand.** If the isolated NMDAR current is not raised (E1) *and*, where it is defined, F* is near-complete, or if
   wild-type slices made to burst by a matched trigger respond the same way (E3), the dependence is permissive or generic: NMDAR block is
   then a symptom tool without a window, and the mechanism-matched levers are upstream (resting potential, inhibition; cards F03, F02).
   That is a legitimate and cheap result. A raised isolated current (E1a) is what would make the GRIN gain-of-function precedents relevant.

## 2. The source preparation (Breton 2021, PMID 34634460) and what an NMDAR experiment in it must control

Opened for this question: methods 5.1 to 5.4, results 2.1 to 2.5, Table 1, Figure 3 (image `gr3.jpg`, JPEG, read by eye, no values
extracted), supplement `mmc1.docx` (Fig S3 legend, Table S1). Staged receipt `FTR-20261029-34634460-01`.

| Parameter | What the source says | Consequence for an NMDAR experiment |
|---|---|---|
| Animals | Synapsin-Cre Wwox knockout (S-KO), heterozygote (S-HT), wild type (S-WT) littermates; both sexes; **postnatal day 13 to 17**; "these mice die between 3 and 4 postnatal weeks, the chosen age group may mimic a late-stage disorder" (Discussion) | the pharmacology is at one, late, symptomatic age; GluN2B-to-GluN2A maturation is in progress at this age (UNVERIFIED for mouse cortex; Auvin 2020 states GluN2B predominates early and is outnumbered by GluN2A in adults) |
| Bursting | 36 of 42 knockout slices (24 animals), 4 of 23 heterozygote (14 animals), 0 of 11 wild type (7 animals); **neocortex only**, hippocampal slices of the same mice do not burst (Results 2.1) | a generic "glutamatergic circuit" explanation is excluded for the hippocampus; a GluN2 subunit map must be region-specific |
| Slice | 400 to 500 um coronal, cut in ice-cold sucrose, incubated in ACSF at 35 C for 30 min, then room temperature at least 60 min, experiment at 35 C | thick slices: wash-in and wash-out of lipophilic or use-dependent drugs are slow and activity-dependent; washout of the d-APV arm is incomplete at the strongest stimuli (Fig S3C) |
| ACSF (stated for incubation) | mM: NaCl 123, NaHCO3 25, glucose 10, **KCl 3.5, MgSO4 1.3, CaCl2 1.5**, NaH2PO4 1.2 | **1.3 mM Mg2+** sets pore-blocker potency (section 4); K+ above the usual 2.5 mM favours excitability; the recording perfusate is not stated separately (**UNVERIFIED** that it is the same) |
| d-APV | 50 uM; burst frequency, duration and amplitude "eliminated" and "returned to normal" on washout; **n = 51 bursts, 5 slices, 3 animals** (Fig 3 legend); Table S1 has *no* d-APV column (no bursts to measure) | Fig 3D (read by eye): d-APV bar absent, washout bar about 1.8 times baseline with a large error bar, the asterisks sit on the carbenoxolone bars; the d-APV arm has no test, and the paper's tests are on bursts, not animals (pseudoreplication) |
| Evoked response | delayed d-APV-sensitive response (peak 97 +/- 31 ms after the stimulus; n = 6 animals); Fig S3B knockout 6 slices/3 animals against wild type 7 slices/4 animals; Fig S3C: d-APV effect significant at only the **three highest of six stimulus strengths** (p 0.0229, 0.0103, 0.0006), and washout still differs at three (0.0492, 0.0372, 0.0499); unpaired t-tests on repeated measures | a graded, stimulus-dependent readout exists and can carry a concentration-response faster than bursts |
| Baseline burst rate | main text **2.29 [1.1 to 4.2] per minute** (median interval 26.2 s); Table S1 **0.84 [0.57 to 1.53] per minute** (min 0.36) for 119 bursts, 18 slices, 9 animals (verbatim-locator manifest entries 23 and 24; prior record); that the main-text rate refers to the same 119 bursts is an **inference** (the main text gives no n; the median burst duration 0.66 [0.53 to 1.06] is identical in both places) | the rate is printed twice, 2.7-fold apart; counting time for about 20 percent precision (25 bursts) is 11 min at 2.29 and 30 min at 0.84 per minute (`arithmetic_p9_output.txt`, section 4); resolve before designing steps; a plausible reconciliation is a rate computed from the median interval against a median of per-slice rates (UNVERIFIED) |
| Resting potential (Table 1, pyramidal) | wild type -79.25 +/- 1.99 mV, heterozygote -75.51 +/- 1.81 (p < 0.05), knockout -73.62 +/- 1.36 (p < 0.05); 13, 15, 40 cells; no liquid-junction correction (methods) | at 1.3 mM Mg2+ the unblocked NMDAR fraction rises about 1.4-fold between -79 and -74 mV (Jahr-Stevens form, constants **UNVERIFIED**; arithmetic, section 4 of `arithmetic_p9_output.txt`): depolarisation alone changes NMDAR drive with a normal receptor |
| Synaptic currents | sEPSC 23.3 +/- 12.0 (controls = wild type and heterozygote pooled, 'S-CTL') against 24.7 +/- 13.6 pA (knockout), described by the source as 'significantly more large-amplitude sEPSCs'; the source also reports an increased mEPSC amplitude in the knockout (pooled events, KS test), which the verbatim-locator manifest reads as a sliver on the cumulative curves; **sIPSC amplitude 57.3 +/- 31.0 against 27.5 +/- 19.4 pA, frequency also reduced**; mEPSC recorded at -70 mV in Mg2+, decay time constant unchanged (5.18 against 4.84 ms) | at -70 mV in 1.3 mM Mg2+ an mEPSC is AMPAR-weighted: it says nothing about NMDAR (the increase fits an AMPAR component at most); the unchanged decay does not exclude an NMDAR change; the sIPSC deficit supports a disinhibition component |
| Anaesthesia | donors anaesthetised with pentobarbital before decapitation | not controlled for; a GABA-A-acting agent in the donor, noted only |

**Controls any NMDAR-pharmacology experiment in this preparation must carry** (derived from the table; a design proposal, not a
protocol that exists): unit of analysis = the animal (slices, cells and bursts nested; at least as many animals as the source's 24
knockout animals used for incidence, or a stated power argument); littermate wild type and heterozygote; inclusion criterion as in the source
(three bursts seen before drug); within-slice baseline, drug, washout, with **time-matched vehicle** slices (run-down); the Mg2+ level of the
perfusate, temperature and holding potential written down for every arm; genotype- and drug-blind scoring with the source's burst detector
(4 to 6 Hz band-pass); a **wild-type positive control**: wild-type slices made to burst by a matched trigger, so that a generic NMDAR dependence is
not read as a Wwox finding; the recording of resting potential and input resistance in the same cells.

## 3. Three readings of one datum, and what each might predict (expectations to be tested, not derived results, and not ranked)

| Reading | What is raised or changed | Expected for a subunit-selective NAM (plateau below complete) | Expected for a pore blocker at 1.3 mM Mg2+ | Expected for an AMPAR antagonist | Precedent that would then apply |
|---|---|---|---|---|---|
| **H1 NMDAR gain** (more/larger NMDAR current per synapse, a GluN2B- or GluN2D-weighted change) | isolated NMDAR current, or its GluN2B fraction, larger in knockout than in wild type | bursts may fall at a partial block; whether they do depends on network gain as well as on receptor level | weak at GluN2A/2B, so little effect unless GluN2C/2D carry the gain | bursts fall (inference) | GRIN gain-of-function: memantine improvement in any domain 14 of 19 against 3 of 15, mainly behaviour; seizure-frequency reduction 7 of 18 against 2 of 10, not significant (p 0.417); GluN2B NAM trials selected by gain-of-function |
| **H2 permissive necessity** (normal NMDAR; the network recruits it because the pyramidal membrane is depolarised and inhibition is about halved) | resting potential, inhibitory current; NMDAR current not raised | bursts may stop only when most NMDAR current is blocked; wild-type slices made to burst may respond alike | as H1, or worse if interneuron GluN2D block disinhibits | bursts fall (inference) | none from GRIN; upstream levers (cards F03, F02) |
| **H3 AMPAR-led drive** (raised AMPAR conductance or recurrent AMPAR drive; NMDAR secondary) | isolated AMPAR current, input resistance | NMDAR block may reduce bursts only at high block | as H2 | bursts fall at low occupancy (inference) | none from the record |

The readings are not exclusive (a disinhibited network with a mildly raised AMPAR component and a normal NMDAR is one combination). F* is a
property of network gain, not of the reading, so no cell above is a derived consequence.

`F01` pre-registered the memantine-versus-perampanel contrast as the discriminator. With the Mg2+, voltage and Ca2+ dependence below, a memantine
result in this preparation does not separate H1 from H2, and an AMPAR result does not separate any of them; only E1 does. F01 stays unchanged as the record of
what was registered on 2026-10-27; **F04** supersedes its discriminator (a dated successor, not an overwrite of a pre-registration).

## 4. The same need, compared across classes (condensed; full cells in `comparison_table.tsv`)

ChEMBL_37 (release 2026-05-01), pulled 2026-10-29. Target organism is what ChEMBL attaches to the target; assay organism is what the
assay record says; the two differ or the assay field is blank in many rows (stated per row). Values are nM unless stated. A median across
assays describes the literature, not a drug. "Rows/docs" is not independence (section 5).

| Compound (ChEMBL id) | Class and action | Target entity and level | Species: target / assay | Measure, relation, value | State and conditions read from the assay text or documents | Human exposure | Counter-evidence and limits |
|---|---|---|---|---|---|---|---|
| d-APV (CHEMBL84612) | A: complete competitive, glutamate site | GluN1/GluN2A-D heteromers (complex) | rat / Xenopus oocytes | Ki, "=": 2A 280 and 390; 2B 460 and 2800; 2C 1640 and 5900; 2D 21000 (one document) | two-electrode voltage clamp, glycine plus glutamate; occupancy at 50 uM is 99 percent (2A), 95 to 99 (2B), 89 to 97 (2C), **70 (2D)** as an upper bound without agonist competition (arithmetic) | none (tool) | the only NMDAR agent applied in a WWOX system; no test on its arm; complete block is not a partial block |
| selfotel (CHEMBL39664) | A: competitive | rat NMDAR group; rat GluN2A | rat / blank | IC50 median 54 (22 to 22400), 22 rows | radioligand and functional rows pooled | adults: stroke (567) and head injury (693) trials stopped | stroke: day-30 deaths 54 of 280 against 37 of 286 (P 0.05); head injury: stopped for deaths and futility (abstracts) |
| memantine (CHEMBL807) | B: use-dependent pore blocker (ChEMBL mechanism type "negative allosteric modulator" on the group target) | GluN1/2A, 2B, 2C, 2D heteromers; rat group | human clones (HEK293, CHO, oocyte) and rat clones, target label "human" for some rat rows / assay organism Homo sapiens or blank | IC50 "=": 840 (2A) and 780 (2B) at -60 mV, 28070 and 25630 at -40 mV in one closed document (**UNVERIFIED**, see section 5); FLIPR 24 h, CHO: 31623, 10000, 3162, 10000 (2A-2D); rat oocyte -75 mV: 2660 (2A), 5570 (2B); outlier 0.95 (2A, oocyte -70 mV) | zero Mg2+ in almost every row; 1.3 mM Mg2+ in the preparation; Mg2+ lowers 2A/2B inhibition about 20-fold, 2C/2D about 3-fold (Kotermanski abstract); GluN2A inhibition rises with intracellular Ca2+ (Phillips 2026) | adults (Alzheimer disease); label: paediatric effectiveness not established, two controlled autism studies in 578 children failed | seizures accelerated in an adult rat oxygen model; GRIN series retrospective, benefit mainly in gain-of-function variants; 0.95 nM is 960-fold below a same-format document (911) |
| ketamine / esketamine (CHEMBL742, CHEMBL395091) | B: pore blocker | GluN1/2A-2D heteromers; rat group | as above | ketamine 500 (2A), 510 (2B) at -60 mV; 53320, 15220 at -40 mV (same closed document, **UNVERIFIED**); esketamine 11.4 (2A) in an LDH excitotoxicity assay in mouse L-cells, against 300 to 960 in [3H]MK-801 displacement | assay type changes the number by three orders; a 2020 review document supplies 19 of the ketamine rows | adults: anaesthesia, depression; observational adult status-epilepticus cohort with perampanel | psychotomimetic and abuse liability (Phillips abstract); hepatic injury 77 against 27 percent with the combination; developing-brain toxicity class statement (Ikonomidou) |
| dizocilpine (CHEMBL344151) | B: pore blocker (tool) | rat group | rat / blank | Ki "=" 2.4 | membrane binding | none | psychomimetic (abstract of the source of CHEMBL6083260) |
| ifenprodil (CHEMBL305187) | C: GluN2B NAM (ifenprodil site) | GluN2B single protein (CHEMBL1904), GluN1/GluN2B complex | target human, assay human/blank/oocyte | IC50/Ki: GluN2B median 10 (5.8 to 340, 14 rows); GluN2A 39500 to 146000; 2C 29100; 2D 75900 | review Table 2: TEVC in oocytes; binding rows are [3H]ifenprodil displacement (affinity, not function) | not examined (ChEMBL lists no phase here) | about 360-fold GluN2B over GluN2A by this table (39.5 against 0.11 uM) |
| Ro 25-6981 (CHEMBL305195, resolved by InChIKey) | C: GluN2B NAM (tool) | GluN2B single protein; GluN1/GluN2B complex | target human / assay human, L(tk-) mouse cells, rat | IC50 9 (review row, TEVC oocytes), 52000 at GluN2A; [3H]ifenprodil displacement 10 to 173 | review Table 2, glycine 3 uM for several rows | none found (ChEMBL: no phase) | tool stand-in; not the clinical compound |
| eliprodil, traxoprodil (CHEMBL28564, CHEMBL17350) | C: GluN2B NAM | GluN2B | human-labelled, mouse L-cell / oocyte | eliprodil Ki 13 on **8 documents, one distinct value**; rat oocyte IC50 1400; traxoprodil 11 to 74 | binding and flux | ChEMBL lists max phase 2; outcomes **UNVERIFIED** | row counts overstate evidence |
| radiprodil (CHEMBL182066) | C: GluN2B NAM, clinical stage | GluN1/GluN2B complex (human-labelled), mouse GluN2B, rat membranes | target human, **assay organism blank in all 5 human-labelled rows**; mouse HEK293; rat | IC50 4 to 70 (Ca flux, [3H]Ro 25-6981 displacement), 3.2 (mouse GluN2B, HEK293), 31.6 (rat displacement); 9 rows, 4 documents | comparator rows from medicinal-chemistry papers; electrophysiology is in Banke 2026 (abstract level) | adults 460 (healthy volunteers and 332 neuropathic-pain patients; the pain programme ended for lack of efficacy); infants 3 (open label, ended for recruitment); registered: paediatric GRIN gain-of-function (phase 1b, 24; phase 3 NCT07224581 recruiting), TSC/FCD (phase 1b/2a), infantile spasms phase 2 terminated by sponsor | all development in gain-of-function GRIN disease or other diseases; no WWOX population; two of three infants relapsed after withdrawal; no efficacy result found |
| TCN-201 (CHEMBL2333945, resolved by InChIKey) | C: GluN2A NAM (tool) | GluN2A single protein; GluN1/GluN2A; complex entry "GRIN1/GRIN2B" holds GluN2A assays | human clones HEK/oocyte; rat oocyte | IC50 109 to 340 (human 2A), 170 to 512 (rat 2A); GluN2B 50000 | 3 uM glycine; inhibition reversed by high glycine | none found | glycine level unknown in the slice; rows of 100 and 446 nM on the "GRIN1/GRIN2B" target are GluN2A assays or a review citation |
| NVP-AAM077 (CHEMBL273636, first-block key match only) | C: GluN2A-preferring competitive (tool; the same rat document gives Ki 11.6 at GluN2C, so it is not 2A-selective over 2C there) | GluN1/2A, 2B, 2C | human clones / rat clones, oocytes | IC50 270 (2A) against 29600 (2B), about 110-fold (human); Ki 5.4 against 67, about 12-fold (rat) | glycine plus glutamate currents | none found | selectivity is assay-conditional; stereo identity not confirmed |
| NAB-14 (CHEMBL4583491, resolved by InChIKey) | C: GluN2C/2D NAM (tool) | GluN1/2C, GluN1/2D | rat / oocyte | IC50 3700 (2C), 2200 (2D), one document | glutamate/glycine currents | none found | single document, paper not opened |
| L-701,324, 7-chlorokynurenic acid, D-cycloserine (CHEMBL31741, CHEMBL311389, CHEMBL771) | E: glycine-site antagonists; partial agonist | GluN1 single protein, rat group, heteromers | mostly rat; D-cycloserine human-labelled oocyte | L-701,324 median 7.6; 7-CKA 320 to 169000; D-cycloserine EC50 1500 (2D) to 21000 (2A) | agonist level decides every effect; unmeasured in the slice | D-cycloserine: antibiotic label | a partial agonist can activate otherwise inactive receptors |
| perampanel (CHEMBL1214124) | F: non-competitive AMPAR antagonist | GluA1 (human), GluA3 (human), with TARPs in some assays | target human / CHO-S, HEK293 | IC50 243 to 1180 (GluA1 flop with TARP gamma-2, -3, -4, -8), 6510 (GluA1 flip, no TARP stated), 2100 (GluA3, -60 mV) | spread mixes TARP, isoform and dye in one document; cyclothiazide present | label: from 4 years for partial-onset seizures; boxed psychiatric warning; one adult WWOX case on seven drugs, no sustained benefit (n 1) | an AMPAR result does not isolate NMDAR |
| NBQX, GYKI 52466 (CHEMBL222519, CHEMBL275006, resolved by InChIKey) | F: competitive / non-competitive AMPAR tools | AMPA rat group (NBQX 29 rows) and human GluA1-4 | rat and human | NBQX rat AMPA median 70 (0.5 to 3000); GYKI 52466 9000 to 22000 | pooled binding and function | none (tools) | NBQX also blocks kainate receptors |

Nominal potency is not therapeutic superiority. Radiprodil's 4 to 70 nM against memantine's 0.8 to 30 uM (zero-Mg2+ and voltage-specific rows) compares an allosteric
NAM with a ceiling to a voltage-, Mg2+- and Ca2+-dependent pore blocker in different assays; it says nothing about the tolerable exposure
in a child, which is the only exposure that matters. An effect of Ro 25-6981 would be an effect of Ro 25-6981.

## 5. What the ChEMBL pull could and could not say (findings that change how the table is read)

* **Resolution of the five tool compounds that P8 could not find by name.** Each was resolved from a *PubChem standard InChIKey* (structure
  checked at PubChem by IUPAC name and formula) and looked up in ChEMBL by that key (`pull_toolcompounds_p9.py`): Ro 25-6981 (CHEMBL305195),
  TCN-201 (CHEMBL2333945, SMILES identical to the PubChem structure), NAB-14 (CHEMBL4583491), d-APV (CHEMBL84612, (2R) key). NVP-AAM077
  matched only by the first (connectivity) block of the key (CHEMBL273636): stereochemistry **UNVERIFIED**. Added for the same need: NBQX,
  GYKI 52466, L-701,324, 7-chlorokynurenic acid, D-cycloserine, selfotel. 246 receptor rows, none truncated.
* **Rows are not independent measurements.** eliprodil on GluN2B: 8 rows, 8 documents, one distinct value (Ki 13); the verifier found the same 13 nM on 14 rows and 14 documents across all ChEMBL targets. Ketamine: one 2020 review
  document supplies 19 of the rows, mostly the same 180 nM Ki. The memantine rat cerebellar-granule value of 1500 recurs across five documents.
  NBQX at rat AMPA: 29 rows, 24 documents, 13 distinct values. Rows from review documents are transcriptions (the 2018 review table
  reproduces the TCN-201 and Ro 25-6981 rows).
* **Target mapping is not subunit identity.** TCN-201 "GluN1/GluN2A, human, oocytes" is attached to the target "GRIN1/GRIN2B" (446 nM), and a
  2013 review document (CHEMBL2331315) carries 100 nM on GluN1/GluN2B (that it is a citation of another source was not checked); the same compound is above 10000 or 50000 nM at GluN2B in the primary-type rows. Subunit
  assignment was therefore taken from the assay description, not from the target name. In several rows the target is "Homo sapiens" while the
  assay organism is blank or "unknown origin".
* **An outlier of three orders.** Memantine at GluN1/GluN2A, TEVC -70 mV: 0.95 nM (2013 document) against 911 nM in a 2007 document of the same
  format. A unit or transcription discrepancy is likely; the paper is closed and was not opened (**UNVERIFIED**).
* **A voltage pair that is not used.** One 2024 medicinal-chemistry document (CHEMBL6083260, PMID 39442339, closed) lists memantine and ketamine at
  human GluN1/GluN2A and GluN1/GluN2B in HEK293 at -60 and at -40 mV, 30- to 107-fold apart. A single-site pore block of electrical distance at most 1
  shifts potency by at most about 2-fold per 20 mV (exp(20/25.7)), so the ratio is physically implausible for a monovalent blocker and may reflect
  protocol, solution or transcription. It is **UNVERIFIED** and is no longer cited as a property of either drug; the argument against memantine as the first
  discriminator rests on the Mg2+ and Ca2+ findings only.
* **Different readouts under one label.** Esketamine 11.4 nM is an LDH excitotoxicity-protection assay (12 h, mouse L-cells), not channel block;
  the 2025 FLIPR rows (24 h incubation, no voltage control) put memantine at 3 to 32 uM where patch clamp gives 0.8 uM at -60 mV.
* **State is not a ChEMBL field.** Voltage, Mg2+, glycine, desensitisation, cyclothiazide, TARP partner and intracellular Ca2+ were read from
  assay text or documents, and only for the rows named in the table.

## 6. Counter-evidence (what argues against each route)

| Route | Counter-evidence | Source and depth |
|---|---|---|
| Any NMDAR block, chronic, in a child | NMDAR blockade for a few hours in late fetal or early neonatal life triggered widespread apoptotic neurodegeneration in the developing rat brain | Ikonomidou 1999, Science, PMID 9872743, **abstract only**; agents and selectivity not named in the abstract |
| Complete competitive block | selfotel: stroke trials suspended for early excess deaths (day-30 54 of 280 against 37 of 286, P 0.05; 90-day 22 against 17 percent, not significant); head-injury trials stopped for concern about deaths and for futility, the later analysis finding no statistically significant mortality difference | PMIDs 10657404, 10541229, **abstracts only** |
| Memantine | no paediatric effectiveness on the label; two 12-week controlled studies in 578 children with autism failed; accelerated seizure stages in an adult rat oxygen model (earlier card); GRIN series: improvement in any domain 14 of 19 in gain-of-function against 3 of 15 otherwise (behaviour 12 of 17 against 3 of 15; seizure-frequency reduction 7 of 18 against 2 of 10, p 0.417, not significant), seizure frequency worsened in three individuals and the EEG in three; individuals 32, 33 and 34 share one GRIN2D variant with opposite outcomes, which the authors attribute partly to age at treatment start (6 y 6 m for 32 against 2 y 6 m for 33) | openFDA label (JSON, effective 2026-09-01); Karnstedt 2026, PMID 41489401, passages read; earlier record |
| Memantine, reassurance in adults | prospective adult cohort (211, median age 63): no new-onset bilateral tonic-clonic seizure; increased frequency reported by 7 with and 5 without memantine | PMID 41288262, **abstract only**; non-randomised, adults |
| Ketamine, perampanel | combined use in adult postanoxic status epilepticus: resolution 84 against 49 percent but reversible cholestatic liver injury 77 against 27 percent | SUPER-CAT, PMID 42837646, **abstract only**; observational, adults |
| GluN2B NAM in WWOX | all clinical-stage use is in gain-of-function GRIN disease (sign known) or other diseases; the three infants with spasms: one spasm-free, two improved then worse after withdrawal; two of the registered studies (NCT05818943 and the TSC/FCD study NCT06392009) exclude memantine, perampanel and felbamate as co-medication, whereas the posted eligibility text of NCT07224581 has no such exclusion; the adult pain programme ended for lack of efficacy | Auvin 2020 (open full text, partial); CT.gov NCT05818943, NCT07224581, NCT06392009, NCT02829827 |
| GluN2-selective claims | selectivity is assay-conditional (110-fold human IC50 against 12-fold rat Ki for the same compound) | ChEMBL documents CHEMBL1135273 and CHEMBL1143579 (assay text), papers not opened |
| NMDAR as the lever | the largest synaptic change in the source is inhibitory; resting potential is depolarised; hippocampal slices do not burst; heterozygotes are intermediate in membrane potential but burst in 4 of 23 | Breton 2021 (re-read) |
| Burst control as benefit | seizure or burst control is not developmental recovery (map N-15); chronic NMDAR block may cost activity-dependent myelination (F02, unmeasured) | repository record |

## 7. Next experiment: controls, and what each result would mean

Wet-lab; **not done**; a design proposal for the laboratory that owns the preparation, not a protocol. **E1 (the isolated NMDAR current) is
the discriminating measurement**; E2 onward are exploratory pharmacology read against it. Any threshold or cut-off must be written, with the
smallest effect size of interest taken from a pilot variance, and time-stamped **before** unblinding; none is taken from the literature.
Preparation and controls: section 2.

| Step | Measure | Arms and controls | Result | Meaning |
|---|---|---|---|---|
| E0 | resolve the 2.29 against 0.84 per minute baseline discrepancy and the recording Mg2+ | the corresponding laboratory would have to say what the perfusate was and how the two rates were computed (a contact is **not** made from this repository; the operator decides) | rate and Mg2+ known | fixes counting time and any pore-blocker interpretation |
| **E1** | isolated NMDAR current in layer II/III pyramidal cells: amplitude, decay, NMDA:AMPA ratio under voltage control with AMPAR and GABA-A blocked, resting potential, input resistance; fraction sensitive to a GluN2B NAM and a GluN2A NAM | knockout, heterozygote, wild type; animals as the unit | (a) NMDAR current or GluN2B fraction raised in knockout | NMDAR gain is present (a component); GRIN gain-of-function precedents become relevant |
| | | | (b) not raised, with resting potential and inhibition altered as reported | the d-APV dependence is permissive: no NMDAR change is needed to explain it |
| | | | (c) AMPAR current or input resistance raised | an AMPAR component |
| | | | (a) to (c) are not exclusive | report each component with its interval |
| E2 (exploratory) | concentration-response of a GluN2B-selective NAM tool (Ro 25-6981) on the isolated current and on the delayed evoked response (stimulated every 30 s in the source), then on bursts; d-APV as the reference, with evoked currents at matched agonist level because competitive block is surmountable by the glutamate transient in a burst | vehicle time-matched; washout; blinded | bursts abolished at the plateau: F* (fraction of isolated NMDAR current blocked at that point) is defined | F* small: a partial, subunit-restricted block is physiologically possible, test radiprodil itself next (the drug, not the tool); F* near complete: no tolerable window, the NMDAR route is a symptom tool, prefer upstream levers (the cut-offs written beforehand) |
| | | | bursts persist at the plateau | F* is undefined; report the plateau fraction and the persistence, and read the GluN2B share of the burst current from E1 |
| E3 | wild-type slices made to burst by a matched trigger (chosen so that burst rate and duration match the knockout), same pharmacology | wild-type, littermates | same concentration-response as knockout | the dependence is generic to NMDAR-driven networks, not a Wwox finding |
| | | | different (knockout more sensitive) | a Wwox-specific NMDAR contribution |
| E4 | a use-dependent pore blocker, **Mg2+ and holding potential stated**, low and high exposure, plus a GluN2C/2D-directed tool if available | after E1 to E2 | burst frequency rises at low exposure | interneuron (disinhibition) action; warns against the class here |
| | | | fall only at high exposure | GluN2A/2B-type block at Mg2+ |
| E5 | AMPAR antagonist (NBQX as tool, perampanel as the clinical comparator) | as E2 | bursts fall | expected whichever reading is true (inference); **not** discriminating |
| E6 | maturation endpoint (myelin, synaptic maturation) after any block that works, in vivo or in culture | chronic, vehicle | any cost | burst control is not benefit (N-15) |

Counting time (arithmetic, `arithmetic_p9_output.txt`): 25 bursts for about 20 percent relative error on a rate need about 11 min at 2.29 per
minute or about 30 min at 0.84 per minute per condition; the delayed evoked response gives a faster read and should carry the concentration-response,
bursts confirming.

## 8. What changed in the repository records (proposed, not applied to the checkout)

* New card `F04_nmdar_intervention_class` (packet and bridge-built card in this directory; `cards/check_cards.py`: 0 problems on a scratch copy).
  Justification for a *new* card rather than a refresh of F01: F01's predictions were registered before any experiment and are not overwritten;
  F04 states the revised discriminator with its dated reasons; the F01 rows and tests stay intact.
* `proposed_edits.patch` (rebased on 2026-10-29 onto the integration working state that already carries the IT6-P11 needs patch, the P11 card and
  the F01 cross-reference): edits to `needs/needs.json` (one new observation **O8**, the d-APV arm design and the double baseline; one
  inference; two counter-evidence items; a GRIN2D target; the F04 and README links), `coverage/target_roles.tsv` (a GRIN2D row, qualifier
  text), `coverage/assertion_pertinence.tsv` (13 rows, selfotel at assertion level). **Not duplicated**: P11 already supplies O6 (resting
  potential), O7 (the ACSF with magnesium, recording bath not stated), its Mg2+ inference and counter-evidence; O3 already carries the inhibitory
  amplitude. The Mg2+ sentence of P11 in `do_not_assume` is kept and extended by one sentence. `git apply --check` passes on that working state.
* `coverage_row_fix.patch`: the repair of `framework/scripts/repurposing_coverage.py` (below) with a regression test that fails on the old code.
* **Scratch trial** (a copy of the integration working state outside the repository, with the three patches applied, then regeneration):
  `needs/check_needs.py` OK (22 needs, 81 observations, 130 manifest locators); `cards/check_cards.py` 27 packets, 0 problems;
  `repurposing_coverage.py run` then `check` OK; `test_repurposing_coverage.py` 55 tests OK (54 plus the regression); `test_check_needs.py` OK;
  `repurposing_view.py`: `titles --refresh`, `run` for both sources and `package` (in that order) are needed after any new card (ten new
  PMIDs need titles), and two pinned numbers of `test_repurposing_view.py` change (48 to 49 position links; 'I 48 legami' to 'I 49 legami'),
  supplied as `followup_view_pins.patch`; with these applied `test_repurposing_view.py` passes (92 tests). Not run: the whole release battery.
* **Harness defect, repaired** (`coverage_row_fix.patch`): `repurposing_coverage.py` evaluated `rows[fid]` in the *condition* of a conditional
  expression before `row(fid)` had created the family row, so an assertion whose subject is a catalogue family *without any association row*
  (selfotel, CHEMBL39664, "target rows=0") raised `KeyError`. The fix creates the row first; the regression test
  `AssertionSubjectWithoutAssociationRow` fails on the old code and passes on the new.
* Receipts: staged under `disease-models/wwox/research/receipt_staging/scientist-a/` (section 9). Nothing was written to the ledger.

## 9. Sources and the depth at which each was read

| Source | Route | Depth | Used for |
|---|---|---|---|
| Breton 2021, PMID 34634460 (PMC8609180) | local XML `PMID34634460_Breton2021_PMC.xml` (sha256 934b4e1a...), supplement `mmc1.docx`, figure `gr3.jpg` | partial re-read, new question; receipt staged `FTR-20261029-34634460-01` (prior `FTR-20261019-34634460-01`) | section 2 |
| Phillips et al 2026, Sci Adv, PMID 42201999 (PMC13215171, CC BY) | Europe PMC XML | partial: abstract, introduction, results text on Ca2+ dependence, Discussion on Mg2+ and disinhibition, methods of the slice recording; figures and supplement not opened; receipt staged `FTR-20261029-42201999-01` | memantine state, Mg2+, Ca2+ |
| Karnstedt et al 2026, Epilepsia, PMID 41489401 (PMC13075606) | Europe PMC XML | partial: abstract and the passages on worsening; the card's earlier reading stays; receipt staged `FTR-20261029-41489401-01` | GRIN series |
| Auvin et al 2020, PMID 32106360 (PMC7085998) | Europe PMC XML | partial: abstract, clinical-experience and study-design passages; receipt staged `FTR-20261029-32106360-01` | radiprodil exposure |
| 2018 review of NMDAR modulators, PMID 29446949 (PMC6368479, author manuscript) | NCBI efetch | partial: Table 2 and the passages on submaximal inhibition and TCN-201; receipt staged `FTR-20261029-29446949-01` | potency table, partial NAMs |
| Kotermanski and Johnson 2009 (PMID 19261873); Banke 2026 Brain (PMID 40994429); Ikonomidou 1999 (PMID 9872743); selfotel PMIDs 10657404 and 10541229; PMID 41288262; PMID 42837646; PMID 39442339 | Europe PMC abstracts (publisher bars body download or closed) | **abstract only** (no receipt; not a reading) | as cited |
| ChEMBL_37: P8 pull, plus `toolcompound_raw.json`; PubChem and HGNC REST for identity | REST | rows and assay text; papers behind the rows not opened except those above | section 4 and 5 |
| ClinicalTrials.gov API v2 (`ct_radiprodil.json`, queried 2026-10-29); openFDA label JSON (memantine effective 2026-09-01; perampanel effective 2025-12-19) | REST | registry records and label sections 8.4 and boxed warning | exposure |

Evidence bytes for the staged receipts are in the task worktree's `files/fulltext/` (git-ignored); the integrator re-acquires them from the
recorded URLs if the worktree is removed.

**UNVERIFIED (not checked at a primary source):** the recording perfusate's Mg2+; the Jahr-Stevens constants; mouse cortical GluN2B-to-GluN2A timing;
the 0.95 nM memantine outlier; that Mg2+ lowers memantine inhibition "nearly twenty-fold" (abstract only, body not read); the secondary-source
statement that cortical GluN2D sits mainly in interneurons (Phillips 2026 Discussion, citing a reference not followed); stereochemistry of the
NVP-AAM077 record; outcomes of eliprodil and traxoprodil programmes; any human exposure to TCN-201, NVP-AAM077, NAB-14, Ro 25-6981 beyond the
ChEMBL phase field; psychiatric trials of D-cycloserine; whether trial results exist for radiprodil studies other than NCT05818943; the
patch-clamp methods and the 30- to 107-fold voltage-pair values of the document CHEMBL6083260 (closed; implausible for a single-site blocker, no longer cited); the ketamine-versus-memantine "disinhibition at 10 uM" statement (secondary).

## 10. Limits

No receptor-level measurement exists in any WWOX system; one laboratory, one preparation, juvenile knockout slices, acute pharmacology; every
Wwox row here is the Breton data re-read, not new data. ChEMBL rows come from heterogeneous assays and some are review transcriptions or
mapping artefacts; the table is a description of the literature, not a property of any drug, and no row says which exposure is tolerable. The
arithmetic (occupancy, Mg2+ block, counting time) is arithmetic with named inputs, not a measurement. Radiprodil trials are registry records;
no results were read. This README makes no efficacy claim, proposes no dose, and recommends no treatment for any person.

## Files

`README.md` (this) · `comparison_table.tsv`, `build_comparison_table.py` · `toolcompound_raw.json`, `toolcompound_summary.tsv`,
`pull_toolcompounds_p9.py` · `arithmetic_p9.py`, `arithmetic_p9_output.txt` · `ct_radiprodil.json` (ClinicalTrials.gov API v2, 2026-10-29) ·
`F04_nmdar_intervention_class.packet.json`, `F04_nmdar_intervention_class.card.json`, `gen_f04_packet.py` (card text is generated and built by
`framework/scripts/repurposing_bridge.py`) · `apply_proposed_edits.py`, `proposed_edits.patch` (needs.json, coverage inputs, F04 into `cards/`),
`coverage_row_fix.patch` (framework repair and regression test), `followup_view_pins.patch` (two pinned numbers of the view test) · P8 inputs: `../pharmacology_it6_20261029/` · staged receipts (not in the ledger):
`../../receipt_staging/scientist-a/FTR-20261029-{34634460-01,42201999-01,41489401-01,32106360-01,29446949-01}.json`, each dry-run with
`fulltext_receipts.py record --dry-run` (OK, nothing written).

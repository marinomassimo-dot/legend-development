# Arm B hypotheses, round 2 (2026-11-16): plain reading, repository knowledge, no perspective instruction

Research hypotheses at mechanism and class level only. No dose, no recommendation to use any agent, reference genotype class only. Named agents are labels for a class, never a proposal. Five blocks (H-C1 to H-C5). Novelty was checked by text search of the thread files, the compound cards, the open-questions map, the discovery ledger and the INV folders (nmda_inv05, gsk3_inv09, hdac5_inv16, golike_inv16, isr_inv02, metabolic_inv07, myelin_inv06, nrf2_inv08, pv_inv15, seizure_function_inv10). A search miss is not proof of absence. Where a neighbour exists it is named inside the block.

---

## H-C1

**Perspective used:** none (plain reading)

**Statement.** In Wwox-deficient layer II/III pyramidal neurons the glycine-site (GluN1 co-agonist) of synaptic NMDA receptors is occupied to a different degree than in littermates, so the same glutamate transient gives a larger (or smaller) isolated NMDAR current with no change in receptor number or subunit mix; this is rejected if a saturating co-agonist and a co-agonist scavenger or competitive glycine-site block change the isolated NMDAR EPSC by the same fractions in knockout and control slices.

**Why a leap.** The usual reading (thread: INV-05, IT15, WO-10, WO-11, WO-12) asks whether the NMDAR current is larger because of receptor number, subunit composition (GluN2B or triheteromer share), Mg2+ gate or proton block, and treats glycine as a nuisance variable to be "fixed and reported" (TCN-201 arm; the F04 card says only that the NAM effect depends on the glycine level, "unmeasured in the slice"). This reading drops the assumption that the receptor's own co-agonist supply is the same in the two genotypes. It would give NMDAR dependence of bursts (d-APV abolishes them) without any receptor change, matching the thread's remark that "a raised receptor current is not required".

**Existing assay or held table that can test it.** The isolated NMDAR EPSC measurement already specified as X1 in `disease-models/wwox/research/drug_repurposing/nmda_inv05_20261107/output/experiment.tsv` (and WO-10) in Wwox neuron-deleted versus control slices at P13 to P17; an added co-agonist arm in the same cells. Held tool table for the class: `.../drug_repurposing/target_first_it15_qa_nmdar_20261101/relations_qa.tsv` (GluN1 glycine-site rows). Held cell-class RNA for the co-agonist machinery (Srr, Dao, Slc6a9, Slc7a10) would be a lookup in the held tables named in the thread (`.../kchan_expression_sci44_20261111/kchan_expression_mouse.tsv` style class means, `.../gse158684_*` pools); I did not open them.

**The single discriminating observation and its two outcomes.** In the same recorded neurons, the fractional change of the isolated NMDAR EPSC when the co-agonist is (a) raised to saturation and (b) lowered by enzymatic scavenging (D-amino-acid oxidase) or competitive glycine-site block. Outcome 1: the increment under (a) is smaller and the loss under (b) larger in knockout than in control (site closer to saturation in the knockout), so a co-agonist-occupancy gain exists and the burst-versus-measured-current curve should shift with it. Outcome 2: both fractions are the same in the two genotypes; hypothesis rejected and the NMDAR dependence stays with composition or permissive necessity. (A larger increment in the knockout would mean the opposite sign, a co-agonist deficit; still a discriminating result.)

**Repurposing class and at most 2 labels.** Glycine-site modulators of GluN1 (competitive antagonists, partial agonists, or agents that change synaptic co-agonist supply); labels: 7-chlorokynurenic acid (tool), D-cycloserine (partial-agonist label). Source of the mechanism: F04 card class E (glycine-site agents) and the IT15 target-first table; the direction of any benefit is open and set by Outcome 1 or the opposite-sign result.

**Held-data pre-test.** No. No thread table contains a co-agonist measurement or a glycine-site comparison for Wwox. The one thread constraint is that d-APV (a competitive agonist-site block) abolishes bursts (INV-05 item 1), which any occupancy change at the glycine site is compatible with. Result: cannot be rejected or supported from the folder.

**What would change my mind.** An isolated NMDAR EPSC with the same co-agonist sensitivity in both genotypes; a co-agonist-saturated recording in which knockout bursts are unchanged by scavenging; evidence that the slice co-agonist is clamped by the bath (bath D-serine or glycine already saturating), which would make the arm uninformative rather than negative.

**Cost to test.** About 16 to 20 animals (8 to 10 per genotype, cell as unit within animal), using slices already planned for WO-10; 4 to 6 table lookups for the RNA side.

---

## H-C2

**Perspective used:** none (plain reading)

**Statement.** The larger input resistance and the 5.6 mV more depolarised rest of the knockout pyramidal neuron (Table 1 of the Wwox neuron paper) bring a persistent, TTX-sensitive sodium current into its operating range, so the NMDAR-triggered event is regenerated by that current into a burst; this is rejected if a persistent-current-preferring block abolishes knockout bursts only at a concentration that also lowers evoked firing and the NMDAR EPSC to the same degree as a matched generic suppression.

**Why a leap.** Every conductance in the thread's ladder (Ba2+-sensitive, XE-991-sensitive, ZD7288-sensitive, K2P, KATP) is a lost or changed outward or hyperpolarising current, and the bursts are read as NMDAR gain or permissive necessity. A depolarising current that is unchanged in size per cell can still decide the outcome once rest and resistance move; this reading drops the assumption that a burst needs an altered conductance, and asks whether an unchanged one is simply pushed into its active window. The thread names "a sodium-channel-blocking class" only as the mechanism-different comparator for the Kv7 arm (SCI43), never as a candidate mechanism, and no card, map row or INV folder mentions the persistent sodium current.

**Existing assay or held table that can test it.** The recordings of the Wwox paper (PMID 34634460, Table 1: rest, Rin, sag, first-spike AHP) repeated with the step ladder in `.../potassium_conductances_sci43_20261110/output/experiment_ladder.tsv` and WO-17 (rest and XE-991 current in the same slices); an added slow voltage ramp (TTX-sensitive current per pF in the window about -65 to -45 mV) in the same cells, and the burst-incidence endpoint with d-APV titration from INV-05 X2.

**The single discriminating observation and its two outcomes.** The TTX-sensitive ramp current per pF in the window, paired with burst incidence under a persistent-preferring block versus a matched reduction of evoked firing by a generic means. Outcome 1: the current per pF (or its fraction of the resting conductance at the knockout rest) is larger in the knockout, or the persistent-preferring block removes bursts at unchanged evoked-spike number and unchanged EPSC, so the persistent current regenerates the burst. Outcome 2: current per pF is the same and the burst fall tracks the generic firing reduction; hypothesis rejected.

**Repurposing class and at most 2 labels.** Sodium-channel blockers with preference for the persistent or slow-inactivated state (source of the mechanism: Nav1.6 and persistent-current gain-of-function epilepsies, outside knowledge); labels: riluzole, cenobamate.

**Held-data pre-test.** Partly. The thread reports unchanged first-spike AHP and, weakly, an F-I slope that does not support a Kv7 deficit, and interneuron firing unchanged; none measures a subthreshold persistent current, so a large gain is not supported but cannot be rejected (a persistent current acts below spike threshold, where an F-I slope is blind). Result: not rejected.

**What would change my mind.** Bursts that survive a verified persistent-current block with unchanged NMDAR EPSC; a knockout whose depolarised rest is produced by a recording artefact (junction potential, capacitance-linked selection of cells by Rin and tau, both flagged in the thread); a persistent current per pF that is smaller in the knockout.

**Cost to test.** About 16 to 20 animals in the existing WO-17 and ladder slice series (no extra animals if added to the same cells); 3 to 4 lookups (Scn1a, Scn2a, Scn8a, Scn3a in the held class-mean tables).

---

## H-C3

**Perspective used:** none (plain reading)

**Statement.** The tonic Gi-coupled adenosine A1 drive onto a K+ conductance is smaller in the knockout slice (for example through higher astrocytic adenosine kinase in the gliotic tissue, or less extracellular adenosine from an energy-handling bottleneck), which contributes to the depolarised rest, higher input resistance and burst susceptibility; this is rejected if an A1 antagonist shifts holding current, rest and input resistance by the same amount in knockout and control neurons.

**Why a leap.** The thread explains the lost resting conductance by a channel itself (Kir2, K2P, Kv7, KATP closed by lactate) or by size plus shunt, and keeps the metabolic arm at the intracellular ATP-sensitive channel. This reading drops the assumption that the missing current is a property of the neuron's own channel pool and instead places it in a missing tonic ligand from the surrounding tissue (the GPCR-gated K+ leak is the same Ba2+- and tertiapin-sensitive family, so the Ba2+ difference current would carry part of it). Neighbours: the J01 card lists adenosine kinase with astrogliosis as a literature lead for glial reactivity, and the ledger notes non-T-type routes of ethosuximide including GIRK inhibition (PMID 37275776); neither links adenosine tone to the Wwox rest, resistance or bursts.

**Existing assay or held table that can test it.** The Wwox slice recordings with the SCI43 difference-current ladder (WO-17, IT45-Q01); an A1-antagonist step and an adenosine-deaminase arm added in the same cells; a tertiapin-sensitive step to read the K+ component. Held table: `.../nb4_gse158684_glia_20261107/` and `.../gse158684_identity_it14_p1a_20261101/` (one pool per arm; Gfap rises 16 to 41 CPM per the ADV-007 note) for Adk, Adora1, Kcnj3 and Kcnj6 counts; descriptive only.

**The single discriminating observation and its two outcomes.** The change in holding current, rest and input resistance caused by an A1 antagonist (and its reversal by adenosine deaminase) in knockout versus control cells at the same recording conditions. Outcome 1: the antagonist-sensitive shift is smaller in the knockout and the knockout rest and Rin move toward control values when the A1 drive is restored by an A1 agonist or reduced adenosine removal; the tone is the missing current. Outcome 2: the shifts are equal and restoring A1 drive does not move the knockout toward control; hypothesis rejected.

**Repurposing class and at most 2 labels.** Adenosine-system modulators that raise or mimic A1 drive (A1 agonists, adenosine kinase inhibitors; source: adenosine kinase and A1 tone in gliosis-associated epilepsy, outside knowledge); labels: N6-cyclopentyladenosine (tool agonist), 5-iodotubercidin (tool kinase inhibitor). Methylxanthine antagonists would be the opposite direction.

**Held-data pre-test.** No. No thread table holds adenosine, A1, ADK or GIRK counts for a Wwox system. The only indirect item is the snRNA rise of Gfap, which makes a reactive astrocyte state present in the pool; it neither supports nor rejects an ADK rise. Result: cannot be rejected from the folder; a held-pool lookup of Adk would be a possible first pre-test.

**What would change my mind.** An A1 antagonist that changes nothing in either genotype (slice adenosine tone absent at the recording temperature and flow); a knockout with a larger antagonist-sensitive shift; Syn1-Cre neuron deletion leaving astrocytic Adk at wild-type level in the P17 pools, which would remove the glial route though not a neuronal one.

**Cost to test.** About 16 to 20 animals in the same slice series as H-C2; 4 table lookups.

---

## H-C4

**Perspective used:** none (plain reading)

**Statement.** The 3 to 7 fold extra susceptibility of Wwox-null pups to pentylenetetrazol is a reduced GABA-A-mediated seizure reserve (the sIPSC loss in vivo), so null pups are hypersensitive to GABA-A-site convulsants but not, or much less, to a convulsant acting through a different mechanism; this is rejected if null pups show the same fold excess on a non-GABA-A convulsant in a same-day, same-litter design.

**Why a leap.** The thread treats the provoked-seizure datum as one acute experiment whose ethosuximide and lithium arms ask about drug effects (NX1, WO-20, WO-21, G01 card). It does not ask what the pentylenetetrazol challenge itself reports. This reading drops the assumption that the challenge is a neutral readout of "seizure threshold" and uses its mechanism (a GABA-A antagonist) as the probe of the inhibitory deficit in the whole animal; it also gives the first in-vivo contrast for the slice-level sIPSC finding that the thread says cannot yet be tested for chloride or release.

**Existing assay or held table that can test it.** The provoked-seizure protocol of PMID 32000863 (Racine-type score per minute) and the held extraction tables `.../fig7_quant_ethosuximide_lithium_sci_20261115/output/fig7b_raster_pdf.tsv` and `.../window_statistics.tsv` for the per-minute scores and the late-phase window used in NX1; the G01 card for the lithium-experiment control group (null peak about 3.5, wild type about 1.2).

**The single discriminating observation and its two outcomes.** In the same litters and on the same day, the null-to-wild-type ratio of the late-phase seizure score (minutes 30 to 60 window, ranks) for pentylenetetrazol and for one non-GABA-A convulsant (a potassium-channel blocker or a kainate-type agonist), each at its own pilot-matched level. Outcome 1: the ratio is clearly larger for pentylenetetrazol (heterozygote intermediate for it only); the null deficit is specific to the GABA-A route and fits the sIPSC loss. Outcome 2: the ratios are alike; the null hypersensitivity is general excitability (or a systemic factor such as the low P10 glucose of WO-35), and the sIPSC loss is not what the challenge reads.

**Repurposing class and at most 2 labels.** Under Outcome 1 only: GABA-A positive modulators acting at the benzodiazepine site (class already in the registry via WO-16 and IT53-Q01); labels: diazepam, clobazam. Under Outcome 2: no class is pointed to; the card-level GABA-A arm would lose a premise.

**Held-data pre-test.** Partly informative, not rejecting. The held numbers give a null-to-wild-type ratio of about 7 (late-phase 1.87 against 0.25, ethosuximide experiment) but only about 3 (peaks 3.5 against 1.2, lithium experiment); the thread (NX1 item 4) and the G01 card both stress that the two null PTZ-alone groups differ, so the fold depends on the experiment and a same-day design is required before any ratio is compared. Result: cannot be rejected; the between-experiment spread is itself a reason the contrast must be same-day.

**What would change my mind.** A null-to-wild-type ratio that varies as much between same-day replicates as between the two held experiments; a second convulsant whose threshold shifts in the null by an unrelated mechanism (for example a hypoglycaemia-driven drop in all thresholds), which would need a glucose-matched arm.

**Cost to test.** About 48 to 60 pups (three genotypes, about 8 per genotype per convulsant, same litters), one session per convulsant; 0 table lookups.

---

## H-C5

**Perspective used:** none (plain reading)

**Statement.** The WW1 domain of WWOX restrains the intracellular-domain signalling of the neuregulin receptor ErbB4 in interneurons (WWOX binds ErbB4 through its PPxY motif), so loss of WWOX uncouples neuregulin-driven strengthening of GABAergic output and lowers inhibition onto pyramidal cells; this is rejected if neuregulin raises sIPSC frequency or amplitude equally in knockout and control slices, or if a WW1-scaffold-dead allele with protein present keeps normal inhibition.

**Why a leap.** The thread's inhibitory-defect line (SCI42, INV-15) is about supply (release, interneuron number, PV loss), response (receptor, chloride) or a consequence of bursting, and the oligodendrocyte line uses neuregulin only as a myelination factor (INV-06). It does not use the best-known WWOX partner in interneurons as a candidate: ErbB4 is held in the ledger only as a structure-modelling target (DL-MECH-006). This reading drops the assumption that the sIPSC loss must be a cell-count or chloride problem and treats it as a signalling problem on the interneuron, which would also explain a loss without a PV-number change (INV-15: counts unresolved).

**Existing assay or held table that can test it.** The sIPSC re-record specified as M03/IT42-Q03 (glutamate block, fixed absolute threshold, per-animal summary) and WO-15 (mIPSC in TTX, physiological chloride), with an added neuregulin arm in the same cells. Held tables: the P47T transcript series (GSE215425 per the thread; the WW1 missense, Wwox mRNA unchanged) and the pooled snRNA (`.../snrna_it13b_pv_20261031/`, GSE158684) for Erbb4 and Nrg1 counts by class; the P17 per-table summary `.../ctgf_held_data_adv007_20261114/per_table.tsv` shows the table format (not read for Erbb4).

**The single discriminating observation and its two outcomes.** The neuregulin-induced change in sIPSC (or mIPSC) frequency and amplitude in knockout versus control (and heterozygote) slices, paired with the sIPSC level in a WW1-scaffold-dead missense model. Outcome 1: the response is absent or reduced in the knockout and the missense model shows a similar inhibitory loss; the WW1-ErbB4 route carries part of the deficit. Outcome 2: the response is intact in the knockout and the missense model has normal inhibition; hypothesis rejected and the SDR-domain or other routes stay.

**Repurposing class and at most 2 labels.** Neuregulin-ErbB4 pathway modulation (source of the mechanism: ErbB4 control of interneuron GABA release, outside knowledge); no approved agonist exists, so labels only: neuregulin-1 beta (tool peptide) and, as the opposing-direction class, a pan-ErbB kinase inhibitor (lapatinib as label). The direction of any benefit is not known.

**Held-data pre-test.** No. The folder holds no ErbB4 or neuregulin measurement for any Wwox system; the interneuron data are 5 versus 6 cells, not identified by type, and the thread (INV-15) says no PV-cell physiology exists in the neuron-targeted model. The P47T model is held as transcripts only, with no electrophysiology in the thread. Result: cannot be rejected from the folder.

**What would change my mind.** A neuregulin response of the same size in knockout slices; ErbB4 not detected in the pooled interneuron classes of GSE158684; an inhibitory loss in the missense model equal to that in the null (which would not reject the idea but would say the WW1 route is not what separates them); a direct demonstration that the sIPSC loss is a recording artefact (M03 not reproducing it).

**Cost to test.** About 16 to 20 animals for the neuregulin arm in the existing sIPSC series; the P47T arm needs the missense colony (about 12 animals); 3 table lookups (Erbb4, Nrg1, Pvalb by class in the held pools).

---

## D. Outside knowledge used or tempted to use

Used, from memory and unverified in this session (no web, no PubMed): the biology of the NMDAR glycine co-agonist site, D-serine, serine racemase and D-amino-acid oxidase (H-C1); persistent sodium current, Nav1.6 and the drug classes that prefer that state (H-C2); adenosine A1 coupling to GIRK and adenosine kinase upregulation in astrogliosis (H-C3); that pentylenetetrazol acts as a GABA-A antagonist and that potassium-channel blockers and kainate-type agonists act otherwise (H-C4); the WWOX WW1-ErbB4 PPxY interaction and the role of ErbB4 in interneuron GABA release (H-C5). The drug labels (riluzole, cenobamate, lapatinib, neuregulin-1 beta, 5-iodotubercidin, N6-cyclopentyladenosine) are outside knowledge; D-cycloserine, 7-chlorokynurenic acid, diazepam and clobazam are in the registry. Tempted and not used: WWOX effects on tau or Dvl (already in the ledger), Nav1.2 to Nav1.6 maturation switch at the burst age (no thread datum), neurosteroid synthesis through the WWOX SDR domain (the sign of the lost conductance, reversal below about -85 mV on the recorded scale, does not fit a GABA-A tonic current), Kir4.1 and pannexin routes (already registered as IT45-Q02 and IT40-Q02).

Held tables named in H-C1, H-C3, H-C5 (`kchan_expression_mouse.tsv`, the GSE158684 pools, `per_table.tsv`) are paths taken from the thread files; I did not open them. Registry reads were limited to the allowed set; I did not open the advisor pilot, earlier hypothesis rounds, judge folders or the sealed extraction.

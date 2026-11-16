# Hypotheses, simple-search baseline arm (2026-11-16)

Non-canonical working material. Not medical advice; no dose, route or schedule; no recommendation to use any agent; reference genotype class only. Worked only from the files in this folder (plain reading, no changed perspective). Repurposing-class names are labels for a mechanism class, not suggestions. 5 would be the maximum; 5 are written. Overlap with existing statements is declared in each block, in "Why a leap".

Shorthand used: "the Wwox slice" = the neuron-deleted (Synapsin I-Cre) P13-P17 layer II/III slice with spontaneous NMDAR-dependent bursts (d-APV abolishes them; bursts in 36 of 42 KO slices, 4 of 23 HT, 0 of 11 WT, per the chloride and K-conductance notes).

---

## H-B1

**Perspective used:** none (simple search)

**Statement:** In the Wwox slice a burst is a two-stage event, a low-threshold calcium-channel-dependent trigger that sets the burst *incidence* (inter-burst interval) and an NMDAR-dependent sustainer that sets burst *duration*, so a T-type blocker lengthens the interval without shortening bursts and a matched-current NMDAR reduction shortens or abolishes bursts without much change in the interval; rejected if both manipulations change interval and duration together at matched effect on incidence (no dissociation), or if the T-type arm acts only by lowering the isolated NMDAR current.

**Why a leap:** The usual reading in the files treats the NMDAR as the single gain variable (d-APV abolishes bursts; X2 compares a GluN2B NAM against d-APV at matched current) and treats Cav3 as a separate proposal (efonidipine and flunarizine pair; ethosuximide in the PTZ figure). This one drops "one variable sets both whether and how long": it gives the two classes different jobs and makes the discriminating readout the split of burst interval versus burst duration, which the files record (duration on the order of a second, median interval 26 s) but never use as an endpoint.

**Existing assay or table in the bundle that can test it:** `T1_nmda_inv05.md` (X2: matched measured fractional NMDAR reduction, burst incidence and duration against it, d-APV titration); `T5_cav3_pair.md` and `T5_cav3_gaps.md` (Cav3 tool pair and the use-dependence requirement); `T4_T8` is not needed. Same slices as X2, one added arm.

**The single discriminating observation and its two outcomes:** In bursting KO slices, at equal measured reduction of the isolated NMDAR EPSC (X1) and equal time-matched vehicle, compare the shift of median inter-burst interval and of median burst duration under (i) a d-APV titration and (ii) a Cav3-directed arm run with one stimulation/holding protocol for both agents (the RP-016 requirement). Outcome A: (ii) moves the interval more than the duration and (i) moves the duration more than the interval, isolated NMDAR current unchanged by (ii): two-stage. Outcome B: both arms move interval and duration in the same proportion, or (ii) lowers the isolated NMDAR current: single-gain (the NMDAR reading, or an off-target action) stands.

**Repurposing class and at most 2 named examples (labels only):** T-type (Cav3) calcium channel blockers; labels efonidipine and ethosuximide (efonidipine from the Cav3 pair notes, ethosuximide from the NX1 sizing note; source of the mechanism class: INV-03 pair as described in `T5_cav3_pair.md`).

**Held-data pre-test:** No table in this folder can reject it. The NX1 note (`T3_nx1_ptz_sizing.md`) says the ethosuximide gap in the nulls is at the late phase and large (1.06 stage) but that it cannot tell a null-specific from a proportional effect, and it is an in vivo PTZ score, not a slice interval or duration: compatible with, not evidence for, a trigger role. Result: not rejected, not supported.

**What would change my mind:** A Cav3 arm that lowers the isolated NMDAR current (then it is an NMDAR route); burst interval and duration that are tightly coupled across slices (a single threshold process); a T-type arm with no effect at a protocol-matched, burst-frequency stimulation (the efonidipine IC50 spans about 500-fold with stimulation frequency in `T5_cav3_gaps.md`, so a low-frequency null would not count).

**Cost to test:** About 8 to 10 KO animals (slices as unit of analysis within animal, X2 shared), zero extra animals if X2 is run anyway; 0 table lookups.

---

## H-B2

**Perspective used:** none (simple search)

**Statement:** The ifenprodil-sensitive (GluN2B-containing) share of the NMDAR EPSC in KO layer II/III cells at P13-P17 stays near the immature or sensory-deprived value (about 0.5) instead of the wild-type value (about 0.14), because the experience-dependent loss of the GluN2B share stalls when cortical drive is reduced; rejected if the KO share lies inside the wild-type interval (0 to 0.34) while the bursts are present.

**Why a leap:** The files list a KO-specific change of NMDAR composition and the GluN2B-to-GluN2A switch inside P13-P17 as alternatives to exclude (`T1_T11_target_first_nmdar.md` 5b), and carry a single wild-type number (14 percent, interval 0-34, whisker-intact P13-P15) from Mierau. The same paper has two more arms that are not used: whisker-deprived P13-P15 (49 percent) and P26-P33 (26 percent). This hypothesis names a cause for a composition difference, a deprivation-like stall, and uses the deprived arm as the reference value, which drops the assumption that the P13-P15 wild-type number is the right comparator for a hypoactive or seizing animal. Partial overlap with the stated alternative; the added element is the cause and the positive-control arm.

**Existing assay or table in the bundle that can test it:** `T11_wo11.md` and `T11_wo11_second_reader.md` (the 14 percent, 53 percent, 49 percent and 26 percent values, design, limits); `T1_T11_target_first_nmdar.md` (E0 measurement of f in the same animals and genotypes; WO-10 for burst slices).

**The single discriminating observation and its two outcomes:** In the same pipeline as E0/WO-10, the ifenprodil-sensitive fraction of the isolated NMDAR EPSC in KO versus wild-type littermate layer II/III cells at P13-P17, with a whisker-deprived wild-type arm as a positive control for the reading. Outcome A: KO fraction near the deprived-wild-type value and above the intact-wild-type interval: stalled switch, and the GluN2B-NAM lever has a larger ceiling than the 0.14 floor suggests. Outcome B: KO fraction inside the intact-wild-type interval: composition is not the difference, the bursts do not depend on a retained GluN2B share, and the 0.14 reading carries.

**Repurposing class and at most 2 named examples (labels only):** GluN2B-selective negative allosteric modulators; labels ifenprodil and Ro 25-6981 (source: the IT15 target-first table, `T1_T11_target_first_nmdar.md`, and the Mierau measurement).

**Held-data pre-test:** None can reject it; the folder holds only wild-type numbers (Mierau: 14 percent intact, 49 percent deprived at P13-P15, 53 percent at P6-P8, 26 percent deprived P26-P33) and no KO ifenprodil value. Result: untestable on held tables. Mierau's own limits apply (evoked synaptic current, room temperature, 2 mM Mg2+, between-cell design, one concentration, n counts cells).

**What would change my mind:** A KO fraction at or below the wild-type value; a KO fraction elevated but equal in burst-free and bursting KO slices (a composition change not tied to bursts); a deprived-wild-type arm that fails to reproduce the 49 percent in this lab's hands (the reading would then be unusable).

**Cost to test:** About 24 animals (three arms, roughly 8 each, ifenprodil and control cells pre-incubated as in Mierau; n of 10 to 15 cells per group), 0 table lookups.

---

## H-B3

**Perspective used:** none (simple search)

**Statement:** One latent delayed-maturation axis in the KO neuronal population explains the co-movement of the progenitor markers, the CCN2 rise, an immature NMDAR subunit ratio, an immature chloride-transporter ratio (NKCC1 up relative to KCC2), the higher input resistance and the depolarised rest, so the held expression tables should show these genes moving by the amount a progenitor-minus-neuronal composite projects; rejected if, in the held KO contrasts, the subunit and chloride-transporter genes move opposite to or independently of the composite projected from the time-course calibration set.

**Why a leap:** The files hold these as separate threads: CCN2 as progenitor-state or composition (`T9_ctgf.md`, composite projection +1.21 against observed +1.15), GluN2B composition (`T1_T11` 5b), chloride gradient and a maturational offset as one of seven explanations (`T2_chloride_gradient.md`), and size/maturation as a hypothesis with no lever (KH5 in `T7_potassium.md`). This drops the assumption that they are independent: it asks whether the single projection that carried CCN2 also carries the channel, receptor and transporter genes. Partial overlap with the stated "maturational offset" and KH5; the added element is the common axis and the table-level test.

**Existing assay or table in the bundle that can test it:** `T9_ctgf.md` (GSE156243 KO organoid 4 versus 2 libraries; GSE150123 time-course calibration; the composite projection method; P17 mouse tables; snRNA pair); `T7_ph_k2p.md` (P7 cell-class RNA table for Kcnk2/3/9); `T2_chloride_gradient.md` (M02 age series of littermates as the wet arm).

**The single discriminating observation and its two outcomes:** For a fixed list of genes (GRIN2B, GRIN2A, SLC12A2, SLC12A5, the K2P genes, CCN2), compare the observed KO-versus-WT log2 change in the organoid table with the change projected from the calibration set by the same progenitor-minus-neuronal composite. Outcome A: observed and projected agree in direction and rough size for most of the list (as CCN2 already does): single axis, the later wet readout is M02 (an age series), and the burst phenotype is partly a maturational offset. Outcome B: the receptor and transporter genes depart from the projection while CCN2 stays on it: CCN2 is a composition marker only and the channel and receptor changes need independent explanations.

**Repurposing class and at most 2 named examples (labels only):** No class if the axis is real and nothing in the files gives a maturation lever (KH5: no lever). Conditional class under the chloride arm only: NKCC1-directed chloride-loading modulators; label bumetanide (outside knowledge for the name, see D; the class as a "chloride-gradient manipulation" is in the `T2_chloride_gradient.md` conditional prediction table).

**Held-data pre-test:** Partly. The CCN2 member of the family already agrees (+1.21 projected, +1.15 observed), so the single-axis reading is not rejected; the receptor and transporter genes are not reported in any file here, so the main test is a table lookup that the folder does not contain. Caveats carried from `T9_ctgf.md`: 4 versus 2 libraries, the calibration is a time course of unperturbed spheroids, a projection shows what a shift would carry, not that a shift occurred, and the composite projection is unchecked by anyone else.

**What would change my mind:** An organoid library set in which the progenitor markers do not rise while the channel genes move; a mouse P17 table (null or neuron deletion) where the same genes move against the composite; the age-series measurement (M02) showing a constant offset rather than a shifted time course.

**Cost to test:** 0 animals; roughly 10 to 15 table lookups (each gene in three held tables, plus one projection run).

---

## H-B4

**Perspective used:** none (simple search)

**Statement:** Neuron-specific Wwox deletion makes astrocytes reactive and lowers their potassium and glutamate clearance, so extracellular K+ and glutamate rise locally during activity and lower the threshold for NMDAR-dependent bursts; rejected if astrocytic Ba2+-sensitive (Kir-type) current and the astrocyte clearance transcripts are unchanged or higher in KO slices, or if burst incidence is the same in KO slices in which clearance is supported.

**Why a leap:** The files treat the burst as a neuron-intrinsic and synaptic problem (input resistance, rest, sIPSC, NMDAR share) and the glia as a composition confound for CCN2 (`T9_ctgf.md`: Gfap 16 to 41, Plp1 392 to 136, endothelial markers up in the knockout pool). This drops "the deleted cell is the only cell that matters in a neuron-specific deletion" and reads the same composition shift as a possible cause. Partial overlap: `T7_ph_k2p.md` notes a glial TREK-1 contribution to pHo and K+ handling as possible and `T7_potassium.md` notes Ba2+ may act on glial Kir4.1.

**Existing assay or table in the bundle that can test it:** `T9_ctgf.md` (the snRNA pair GSE158684, one pool per arm, cell-class marker split) and `T7_ph_k2p.md` (P7 cell-class RNA table; astrocyte Kcnk2); `T7_potassium.md` (Ba2+ difference-current ladder, step 2, 60 uM, same slices, per-pF currents).

**The single discriminating observation and its two outcomes:** Same slices, same Ba2+ step: the Ba2+-sensitive current per pF measured in astrocytes (not only in pyramidal cells) in KO versus WT, with a parallel table lookup of astrocyte-nucleus clearance genes. Outcome A: reduced astrocytic Ba2+-sensitive current and lower clearance transcripts in KO astrocyte nuclei: non-cell-autonomous K+ clearance deficit, and the Ba2+ difference current in neurons is partly glial. Outcome B: unchanged or larger astrocytic current and unchanged transcripts: the glial change is a marker, not a driver.

**Repurposing class and at most 2 named examples (labels only):** Glial potassium-channel (K2P/Kir) modulators; label riluzole (listed in the catalogued K2P-opener rows of `T7_ph_k2p.md`; non-selective, reported there as a native-neuron value, so only a class label here). A glutamate-transporter-supporting class is the tempted second class (outside knowledge, see D), not named.

**Held-data pre-test:** Weak. The snRNA pair is one pool per arm and descriptive only; a pool-level fall of Plp1 and rise of Gfap and endothelial markers fits a composition shift, and an astrocyte-nucleus lookup of the clearance genes is possible only if those genes sit in the held matrix files, which the folder does not show. Result: not rejected, not supported; direction of any single-pool lookup cannot reject (n = 1 per arm).

**What would change my mind:** Astrocyte-restricted clearance genes up in KO; burst incidence unchanged when extracellular K+ is clamped or buffered in wild-type slices driven into a burst state (M09-type arm); a neuron-only effect surviving co-culture without astrocytes.

**Cost to test:** About 8 KO and 8 WT animals for astrocyte patch plus the Ba2+ step (same animals as ladder step 2 if run in parallel); about 6 to 10 table lookups first.

---

## H-B5

**Perspective used:** none (simple search)

**Statement:** Burst occurrence is a network threshold set by the fraction of Wwox-deficient neurons in the slice, so the incomplete excision of the Synapsin I-Cre line (and the 4 of 23 heterozygote slices) predicts that the 6 of 42 burst-free KO slices carry the lowest fraction of excised neurons; rejected if burst-free and bursting KO slices have the same per-slice excised-neuron fraction.

**Why a leap:** The files read burst incidence as a genotype property (0 of 11, 4 of 23, 36 of 42) and note only that a burst-free knockout contrast is hard to obtain and that Syn1-Cre excision is partial. This drops "the genotype is the unit" and makes the slice's mosaic fraction the explanatory variable, which also changes what a partial NMDAR reduction needs to achieve (it only has to push a threshold system below its threshold). Not stated in any file as a hypothesis, question or conclusion.

**Existing assay or table in the bundle that can test it:** `T2_chloride_gradient.md` (burst counts 0/11, 4/23, 36/42 and the caution that bursting slices confound cause and consequence) and `T4_T8_gsk3_inv09.md` (R03, R04: Syn1-Cre excision partial; Nestin-, Olig2-, GFAP-Cre as other arms); `T1_nmda_inv05.md` (X2 readouts).

**The single discriminating observation and its two outcomes:** In KO slices, the per-slice fraction of Wwox-negative (or reporter-positive) pyramidal neurons against whether the slice bursts. Outcome A: bursting slices have a higher excised fraction and a threshold is visible (burst-free slices cluster at the low end): the network-threshold reading holds, and a small measured NMDAR reduction could suffice. Outcome B: no relation across a wide range of fractions: the burst is not a mosaic-threshold effect (the neuron-deletion genotype acts per cell or through a tissue-wide factor).

**Repurposing class and at most 2 named examples (labels only):** Partial gain reduction of NMDAR-dependent excitation, GluN2B-selective NAM class; label ifenprodil (source: the matched-current design in `T1_nmda_inv05.md` and `T1_T11_target_first_nmdar.md`). No class beyond what the NMDAR thread already holds; the contribution is the expected size of reduction needed.

**Held-data pre-test:** The held counts (0/11, 4/23, 36/42) are monotone with gene dosage and are equally compatible with a cell-autonomous dose effect; no table here has a per-slice excision fraction. Result: cannot reject.

**What would change my mind:** Burst-free KO slices with high excision; bursting HT slices with a low Wwox-negative fraction in a Cre-negative-for-reporter check; a sparse-deletion experiment (Cre at limiting dose) where bursts appear at a fraction well below the KO value.

**Cost to test:** About 10 to 12 KO animals with a reporter or Wwox immunostaining on the recorded slices (retrospective in the same slices as X2); 0 table lookups.

---

## D. Outside knowledge used or tempted to use

Used, not from the folder:
- H-B1: that T-type channel availability requires hyperpolarised potentials (steady-state inactivation at depolarised rest) and that T-type calcium entry can trigger rebound burst firing; and that ethosuximide is a T-type-directed antiseizure agent (the folder names ethosuximide only as the PTZ-figure unit and the Cav3 pair as efonidipine and flunarizine). A depolarised KO rest (about 5.6 mV in the K-conductance note) would reduce T-type availability, which cuts against H-B1 and is the main reason it is a hypothesis and not a prediction.
- H-B2: general background that the GluN2B-to-GluN2A switch is activity- and experience-dependent (only partly in the folder through the Mierau deprivation arms).
- H-B3: the names NKCC1 and KCC2 as chloride transporters whose ratio sets chloride gradient (both appear in the chloride note) and bumetanide as the NKCC1-class label (not in the folder).
- H-B4: Kir4.1 and glial glutamate transporters as astrocytic clearance routes (Kir4.1 is mentioned once in the K-conductance note, glutamate transporters are not mentioned); the label riluzole is taken from the folder's K2P-opener rows.
- H-B5: general Cre-lox mosaic behaviour (partial excision gives a mixed population), supported in the folder only by the statement that Syn1-Cre excision is partial.

Tempted, not used:
- Known WWOX biology (WW-domain binding partners, WWOX cleavage products, other WWOX tissue phenotypes): the task limits me to the folder.
- Naming a glutamate-uptake-enhancing drug class for H-B4: no source in the folder, so left unnamed.
- Naming specific antiseizure sodium-channel agents as comparators: the folder only names the class.
- Any claim about published WWOX seizure treatments or clinical use: excluded by the task (mechanism and class level only).

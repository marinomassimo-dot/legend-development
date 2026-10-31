# IT13 follow-up: the three next actions (bench protocols, ACK1 stability test, 2024 Aurora B text)

Orchestrator, 2026-10-31 (Europe/Rome night), after the IT13 close (`main` 68f2820c). Non-canonical; not medical advice; reference genotype class only. **Nothing here is a result: two of the three actions are laboratory experiments that cannot be run from this repository, and the third is blocked by access.** What was done is the part that can be done here: protocol sheets for a referent, a re-check of every reopening condition on public routes, and one analysis that became executable today.

## Decision first

| Action | State | What was done here | What is still needed |
|---|---|---|---|
| 1. Slice and organoid arms (WT+WWOX, mutant WWOX, silencers) | **Protocol ready, not run** | Sheet A below, merged from the P3a and P3b designs with a pre-specified decision table | a laboratory holding the neuron-deleted line or the patient-derived organoids; contact is the operator's, nothing was sent |
| 2. WWOX amount, half-life and ubiquitination after an ACK1 intervention (Y287F, no-activated-ACK1 arm) | **Protocol ready, gated, not run** | Sheet B below (IT12 design plus the IT13 controls); gate G0 stays first | gate G0 (G372R band above the assay floor, two antibodies) before any compound; the lines are held by a laboratory |
| 3. Regenerate with the 2024 Aurora B text | **Condition NOT met** | PMID 39639371 (doi 10.1002/cbf.70022): Europe PMC `inEPMC=N, inPMC=N`; OpenAlex `closed`, no repository copy; the publisher page answers 403 (bot check, not circumvented) | the PDF through a library or the operator; then re-read and amend the P1.5 package. No derived surface was regenerated because no content changed |

**New fact checked today:** the six GSE158684 snRNA files, which returned 0 bytes this morning, now download (the matrices are 26 MB). That makes reopen trigger NP3A1 (nucleus-resolved PV composition) executable; it was handed to a separate package (`snrna_it13b_pv_20261031`) and is not part of this README. **Still closed:** E-MTAB-14792 (the BioStudies API answers 'Study not accessible'; nothing was bypassed).

## Re-check of the reopening conditions (Europe PMC title/abstract queries and direct file requests, 2026-10-31; a miss describes this perimeter, not absence)

| Trigger | Result today |
|---|---|
| NP3B1 compound arm with Ca2+/MEA readout in a WWOX-deficient human organoid | none found (6 hits, reviews and unrelated) |
| NP3B2 gene-level add-back data (E-MTAB-14792) | still closed |
| NP3B3 WT + AAV9-WWOX or dead-mutant arm | none found; the neuron-specific gene-therapy paper is the already known PMID 42422765 / preprint PPR1220099 |
| R1/R9 G372R or Q230P protein in a neural model | no new paper (one hit, PMID 41124647, already in the module) |
| R3/R8 pharmacological ACK1 intervention measuring WWOX | none (the 2025 hits are reviews or other cancers; 41677633 concerns WWOX-induced degradation of BCL-XL/MCL-1 through a lysosomal route in cancer cells and does not measure WWOX after ACK1 inhibition) |
| NP3A1 nucleus-resolved PV composition | **files now readable and analysed** (`snrna_it13b_pv_20261031`): undecidable at one pooled library per genotype; the trigger moves to PARTIAL with a narrowed condition (per-library counts or PV immunostaining) |

## Sheet A (IT14 version): bench protocol for the recovery-versus-transgene question (action 1)

> Corrected on 2026-11-01 (IT14 P2); the IT13 version over-inferred in three places, see the note in `recoverable_it13_p3b_20261031/README.md`.

Question: is the week-10 neuron-promoter AAV9-WWOX recovery of firing and of CTIP2/SATB2 in WOREE (and of firing in SCAR12) a WWOX-function effect, a transgene effect, or activity-dependent downstream biology? Source of the problem: PMID 42397075 Fig 6 has five arms and no WT+WWOX or mutant-WWOX arm (independently verified).

**Units.** The organoid is the unit of a test; independent differentiations, lines (WOREE, SCAR12, wild type) and donors are different levels and are not interchangeable. Two patient-derived lines allow statements about those lines, not about a class of variants. No numerosity is fixed here: the variance is not known from the source (n 3 to 8 organoids per arm, bars read by eye), so it comes from a pilot of the referent. Blind assessment of arm.

**Kinds of benefit are kept apart, and none is a condition for another:**

| Kind | Supported by |
|---|---|
| acute effect on an endpoint | an immediate change of firing in a compound arm |
| functional benefit during exposure | an improved readout while the compound or the transgene is active, with the controls below |
| compensation of an impaired function | the same function restored by a different route (e.g. a silencer lowering firing while WWOX stays absent) |
| a change that persists after a compound is withdrawn | a withdrawal arm of a COMPOUND (only compounds can be withdrawn) |
| broader recovery of WWOX functions | several WWOX-dependent readouts moving together (firing, layer markers, channel programme), not firing alone |

Partial benefit does not require recovery of the layer markers or persistence after withdrawal; the absence of persistence does not make a result irrelevant.

**Controls for any reduction of firing (against toxicity, cell loss and generalised suppression):** viability or cell death per organoid, cell number or density, preserved evoked responses (for example to a depolarising or AMPA/glutamate stimulus), and the lowest effective concentration with a concentration-response; an unchanged baseline of unrelated activity features. Without them a lowered firing is not read as a functional improvement.

**Exposure state at the time of each read** is declared for every arm: an AAV arm keeps expressing the transgene for the whole read, so persistence while it is expressed is not memory of a recovery; a compound arm has a defined exposure and can be withdrawn. No inducible system is proposed: the simplest comparison is a compound arm during exposure and after withdrawal, and an AAV arm during expression; a post-cessation claim for WWOX itself would need removal of expression and is **not** answerable in this design (stated limit).

**Arms:** WOREE + EGFP vector; + WWOX; + WW1-dead WWOX; + an SDR-region mutant WWOX (a mutant is not necessarily inactive for every WWOX function: construct expression, stability and localisation are shown, and the result says which domain the readout needs, not that the mutant is dead); wild type + WWOX and wild type + EGFP; WOREE + a sodium-channel blocker; + an NMDAR antagonist; + vehicle, each with and without withdrawal; SCAR12 repeated as the internal dissociation (firing high, layer markers at wild-type level).

**Readouts, read together:** Ca2+ event rate, amplitude, percent active ROIs (the untreated arms of the source sit at a 100 percent ceiling, so a non-saturated design is chosen); CTIP2/SATB2 by immunofluorescence and qPCR; an ion-channel panel by qPCR; radial-glia markers as the untouched-compartment check; WWOX protein level per arm.

**Predictions fixed beforehand (from SCAR12, which may be wrong):** silencing lowers firing without raising CTIP2/SATB2 and, after withdrawal of the silencer, firing returns; add-back lowers firing and raises CTIP2/SATB2 in WOREE while the transgene is expressed.

**Decision table (corrected):**

| Outcome | Reading | Consequence in the module |
|---|---|---|
| wild type + WWOX also lowers firing | limits how much of the add-back effect in the knockout is attributed to recovery; it does not cancel the knockout result (an additive or ceiling effect remains possible) | the recoverable readout is kept with a stated limit |
| the matching mutant arms reproduce the wild-type effect | the readout does not need that domain; not evidence that the mutant is dead | which domain is needed is narrowed |
| the active WWOX recovers and both mutants and the wild-type control are flat | WWOX-function-specific recovery for the readouts measured | firing and markers are usable as readouts for a bypass search |
| a silencer lowers firing, the evoked-response and viability controls are clean, markers unchanged | compensation of firing without marker recovery: a functional benefit during exposure, separable from marker identity | no change of priority; confirms the paired-readout rule |
| a silencer lowers firing together with loss of viability, cell number or evoked responses | generalised suppression or toxicity, not an improvement | the candidacy is withdrawn for this readout |
| a silencer raises CTIP2/SATB2 | an activity-dependent route to the marker readout | a candidate class for the marker readout, qualified separately |

* **Cannot show:** benefit, safety, exposure, anything in vivo or in a child; transfer between lines; recovery of WWOX functions beyond those measured.

## Sheet B: bench protocol for the ACK1 stability question (action 2; the full design is `product_it12_p1a_20261031/design_it12_p1a.md`, the IT13 controls are `ack1_it13_mahajan_20261031/controls_ack1_it13.tsv`)

* **Gate G0, first and alone:** the faint G372R band (0.1 to 0.3 of an unrelated wild type on one membrane; on a second blot similar to the knockout lanes) must be shown to be WWOX above the assay floor: two antibodies against different epitopes, a knockout lane and a heterozygous-parent lane on the same membrane, a wild-type dilution series to define the linear range, an IP-then-blot or targeted mass-spectrometry confirmation, and WWOX mRNA in the same samples. **If G0 fails, no stability test applies to any neural variant line** (substrate UNCONFIRMED, not excluded, but nothing to test) and the work reduces to the wild-type-cell mechanism question below.
* **Wild-type neural cells (the arm that can run without G0):** does loss of ACK1 activity change WWOX amount and half-life at all? Genetic arm first (two TNK2 sequences against scrambled; knockout with RNAi-resistant wild-type and kinase-dead rescue), then two structurally unrelated ACK1 inhibitors at the lowest effective dose with a phospho-ACK1 readout and a mitosis/viability control (the 2024 Aurora B report and the JAK2/TYK2 hits of the only published (R)-9b panel make a single probe uninterpretable).
* **Controls specific to this case:** WWOX Tyr287Phe interrogated for steady state, cycloheximide chase and ubiquitination on a denaturing IP (Mahajan 2005 shows only its phospho-Tyr loss); an arm without activated ACK1 in the same chase (Fig 5E of the source has none); MG-132 and a lysosome inhibitor inside the chase with a **level** readout; WWOX mRNA.
* **Unit and replication:** the independent differentiation or organoid batch, not the lane; three or more; a short-lived protein as chase control.
* **Decision table:** see the IT12 design (eight outcomes). Added by IT13 and corrected by IT14: Y287F that is still ubiquitinated and degraded argues against Tyr287 being necessary in these cells but does not exclude a contribution; a level that rises with a lysosome inhibitor and not with ACK1 loss means a route independent of ACK1.
* **Interpretation limits (IT14 version):** a negative result in the G372R line does not extend to Q230P or to other neural variants; a Y287F that is still ubiquitinated and degraded does not by itself show that Tyr287 contributes nothing (the source calls it the predominant, not the only, phosphorylation site, and other sites or a route that does not need the site may act); no effect of a single inhibitor excludes the pathway unless the perturbation is shown to have happened (reduced phospho-ACK1 or loss of ACK1 protein, with the loss that the genetic arm achieves); a loss of ACK1 that changes the amount without changing the half-life is not stabilisation. The independent differentiation or organoid batch is the unit; lines and donors are different levels.
* **Cannot show:** function, benefit, CNS exposure, or transfer from G372R to Q230P (different residue, different cells).

## What would change the module

Each outcome above maps to a need and a trigger already carried: Sheet A to `NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR` and triggers NP3B1 to NP3B3; Sheet B to uncarded item N12 and triggers R1, R3, R8, R9. No new object was created.

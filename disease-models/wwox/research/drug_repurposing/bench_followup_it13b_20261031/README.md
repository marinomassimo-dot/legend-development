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
| NP3A1 nucleus-resolved PV composition | **files now readable** (separate package) |

## Sheet A: bench protocol for the recovery-versus-transgene question (action 1)

Question: is the week-10 neuron-promoter AAV9-WWOX recovery of firing and of CTIP2/SATB2 in WOREE (and of firing in SCAR12) a WWOX-function effect, a transgene effect, or activity-dependent downstream biology? Source of the problem: PMID 42397075 Fig 6 has five arms and no WT+WWOX or dead-mutant arm (independently verified).

* **System:** WOREE and SCAR12 organoids plus wild type, one protocol (infection week 10, read week 16), Ca2+ imaging as in the source; **the organoid is the unit** (not ROIs, not fields), at least two independent differentiations, assessor blind to arm. The variance is not known from the source (n 3 to 8 organoids per arm, bars read by eye), so no sample size is stated here: it has to come from a pilot of the referent.
* **Arms:** WOREE + EGFP vector; + WWOX; + WW1-dead WWOX; + an SDR-region mutant WWOX; wild type + WWOX and wild type + EGFP; WOREE + a sodium-channel blocker; + an NMDAR antagonist; + vehicle; a 2-week washout of every arm; SCAR12 repeated as the internal dissociation (firing high, layer markers at wild-type level).
* **Readouts, read together:** Ca2+ event rate, amplitude, percent active ROIs (the untreated arms of the source sit at a 100 percent ceiling, so choose a design that is not saturated); CTIP2/SATB2 by immunofluorescence and qPCR; an ion-channel panel by qPCR; radial-glia markers as the untouched-compartment check; WWOX protein level in treated arms (the source shows only sparse WWOX-positive cells).
* **Predictions fixed beforehand (from SCAR12, which may be wrong):** silencing lowers firing, does not raise CTIP2/SATB2 and does not persist after washout; WWOX add-back does all three.
* **Decision table:**

| Outcome | Reading | Consequence in the module |
|---|---|---|
| wild type + WWOX also lowers firing, or the dead mutant matches the active one | the add-back effect is not WWOX-function recovery | the 'recoverable readout' is withdrawn as a ruler for bypass |
| the active WWOX recovers, the dead mutants do not, wild type + WWOX is flat | WWOX-function-specific recovery | firing and markers become usable readouts for a bypass search (NP3B1 becomes the next arm) |
| silencers lower firing without raising the markers and the effect vanishes after washout | firing and layer identity are separable; silencing is symptomatic | no change of priority; confirms the paired-readout rule |
| silencers raise CTIP2/SATB2 | an activity-dependent route to the marker readout exists | a candidate class for the marker readout, qualified separately |

* **Cannot show:** benefit, safety, exposure, anything in vivo or in a child; transfer between lines.

## Sheet B: bench protocol for the ACK1 stability question (action 2; the full design is `product_it12_p1a_20261031/design_it12_p1a.md`, the IT13 controls are `ack1_it13_mahajan_20261031/controls_ack1_it13.tsv`)

* **Gate G0, first and alone:** the faint G372R band (0.1 to 0.3 of an unrelated wild type on one membrane; on a second blot similar to the knockout lanes) must be shown to be WWOX above the assay floor: two antibodies against different epitopes, a knockout lane and a heterozygous-parent lane on the same membrane, a wild-type dilution series to define the linear range, an IP-then-blot or targeted mass-spectrometry confirmation, and WWOX mRNA in the same samples. **If G0 fails, no stability test applies to any neural variant line** (substrate UNCONFIRMED, not excluded, but nothing to test) and the work reduces to the wild-type-cell mechanism question below.
* **Wild-type neural cells (the arm that can run without G0):** does loss of ACK1 activity change WWOX amount and half-life at all? Genetic arm first (two TNK2 sequences against scrambled; knockout with RNAi-resistant wild-type and kinase-dead rescue), then two structurally unrelated ACK1 inhibitors at the lowest effective dose with a phospho-ACK1 readout and a mitosis/viability control (the 2024 Aurora B report and the JAK2/TYK2 hits of the only published (R)-9b panel make a single probe uninterpretable).
* **Controls specific to this case:** WWOX Tyr287Phe interrogated for steady state, cycloheximide chase and ubiquitination on a denaturing IP (Mahajan 2005 shows only its phospho-Tyr loss); an arm without activated ACK1 in the same chase (Fig 5E of the source has none); MG-132 and a lysosome inhibitor inside the chase with a **level** readout; WWOX mRNA.
* **Unit and replication:** the independent differentiation or organoid batch, not the lane; three or more; a short-lived protein as chase control.
* **Decision table:** see the IT12 design (eight outcomes). Added by IT13: Y287F that is still ubiquitinated and degraded means Tyr287 is not the targeting site in these cells; a level that rises with a lysosome inhibitor and not with ACK1 loss means a route independent of ACK1.
* **Cannot show:** function, benefit, CNS exposure, or transfer from G372R to Q230P (different residue, different cells).

## What would change the module

Each outcome above maps to a need and a trigger already carried: Sheet A to `NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR` and triggers NP3B1 to NP3B3; Sheet B to uncarded item N12 and triggers R1, R3, R8, R9. No new object was created.

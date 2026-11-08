# Consumer delta — OpenScientist/Dismech full-input repeat (2026-11-08)

Proposals for the integrator. Nothing here was applied; no shared consumer, ranking, dashboard, registry or ledger was touched. Each line names the consumer, the proposed wording or addition, and the package row it rests on (`<folder>/<file> <id>`). No line changes a rank, a card verdict or the order of a work order; none promotes a compound.

## Needs and investigations (wording additions)

* `needs/needs.json` NEED-T-TYPE-CALCIUM — add: the cited seizure paper (CaV3.3 knockout, TRN-silenced CaV3.3, double knockout) contains no single CaV3.2 knockout; the CACNA1H variant in the cited DEE case report was inherited from an asymptomatic parent and its authors write that CACNA1H has "never been associated with DEEs" (`inv03_04_ttype/decisive.tsv` D07, D10).
* `ranking_it8_p9_20261029/investigations_it20.tsv` INV-03 — add: the "structurally unrelated antagonist" panel is not independent (ulixacaltamide is Z944; Z944 and TTA-P2 share a piperidinylmethyl benzamide scaffold) (`inv03_04_ttype/decisive.tsv` D06, D08).
* `ttype_20261107/output/probes.tsv` P1, P3, P4 — repair the scaffold wording (the earlier file repeats the wording the audit corrects) (`inv03_04_ttype/reconcile.tsv` E21).
* `needs/needs.json` NEED-GSK3B-DEREPRESSION counter_evidence — add: an inositol-depletion arm is not GSK-3-free (25345501: GSK-3α inactivated, GSK-3β not significantly altered; one paper, one isoform) (`inv09_gsk3/decisive.tsv` D02); the S9A cross is not an attribution control (D03); time-gated dosing has no timing source (D07).
* `gsk3_inv09_20261107/output/separation.tsv` row 1 — add the inositol distinction; add the BRD3731 caveat (β-selective compound raised β-catenin from 20 µM in HL-60/TF-1; separation holds for the α-selective compound and genetic loss) (`inv09_gsk3/decisive.tsv` D04).
* INV-06 evidence table — add the GSK3 counter/context rows (Foxg1/SB216763 runs opposite; the 2026 review holds both directions: abstract, section 3 Wnt sentence, section 3 lithium sentence, section 4) and the neuron-specific wording for the slice paper (`inv06_myelin/evidence.tsv` EV01–EV07, EV13, EV16; `inv09_gsk3/evidence.tsv` EV03).
* INV-05 rationale and `cards/F04_nmdar_intervention_class.card.json` — selfotel line: "head-injury trial stopped after a stroke-study signal; a later analysis did not confirm excess mortality in head injury" (abstract level); add the carbenoxolone caveat to the gap-junction half of the combination logic; note perzinfotel is NR2A-preferring (`inv05_nmda/decisive.tsv` D05, D08, D09).
* NMDAR need — add "AMPA dependence not tested in the neuron-deleted burst slice paper (one AMPA mention, mEPSC decay)"; the AMPA-antagonist arm beside d-APV is the cheapest discriminator for the felbamate/perampanel nomination (`inv10_seizures/decisive.tsv`, AMPA proposition; `inv05_nmda/decisive.tsv`).
* INV-10 sentence — the transfer from KCNQ2/TSC is analogy; genotype stratification is established for mortality only; "lithium the only existing-drug node" is wrong (ethosuximide also tested) (`inv10_seizures/decisive.tsv` D02, D04, D10).
* INV-07 and the KD card E04 — note PAPER 017 (KD response in 3 of 5 WOREE individuals; lactate 2.4–3.3 mmol/L in one individual); the Pdk1 transcript and serum-lactate datum in the Wwox-null MEF/mouse paper (25012504) is non-neural and measures no PDH (`inv07_pdh/decisive.tsv` P02, P10). Lithium wording in the report is stronger than card G01.
* INV-08 row and NEED-REDOX-NRF2 — cite the retraction of 21690096 wherever the Src/Fyn chain appears (none carries it now); the cited relation's other support is a 2007 paper from the same laboratory line (not independent); reductive stress is a transfer from cardiac models (`inv08_nrf2/decisive.tsv` D02, D04, D07).
* INV-15 — keep the earlier corrections; add: model identity (Synapsin-Cre conditional line), zero-hit statement wrong (−44 percent PV-positive cells in the 2-week full-knockout hippocampus), explanations B/F inconsistency in the report, PNN counter-evidence (`inv15_pv/decisive.tsv` D02, D05, D06).
* INV-16 notes — add the five corrections (ketogenic paper, MC1568/Bdnf, pooled SPR range, lithium specificity, ICP0 source type), the human muscle HDAC5 knockdown (lower GLUT1 expression; opposite sign to the report's table) and the HDAC4–MEF2A–GLUT1 route (`inv16_hdac5/decisive.tsv` P01, P03, P06, P07, P09, P10).
* NEED-INTRINSIC-EXCITABILITY and INV-18 — add: input resistance measured and about 40 percent higher in both mutants (sag not matched for it); ivabradine blocks sag and hyperpolarises cortical L5/6 neurons in normal rat slices and injection into somatosensory cortex cut absence-seizure time 96 percent against 40 percent in thalamic VB (34018186); the GAERS authors' reading of Ih (not an adaptive response to spike-wave discharges; Rin fell, RMP and sag unchanged) next to the "discordant precedents" text (`inv18_membrane/decisive.tsv` D02, D04, D06).
* INV-02 evidence line — cite 32894619 and 42097410 as transfer context only; the VWM line may state that the myelin readouts of 40296303 were read (`inv02_isr/evidence.tsv` EV01); PMID 12133000's own result runs against its use as "the biochemical bridge" (D04); the ISR absence is "none found in two PubMed strings" for human neural cells, with the fly datum conditional on neuronal Aβ42 and a non-neural WWOX–PERK/IRE1 paper (`inv02_isr/decisive.tsv` P01, P04).

## Cards and ranking

None changed. The producers' README sections (g) record the novelty class per proposal (new_to_legend / already_in_legend; literature novelty not assessed); the three that are new as design elements and cheap are the AMPA arm, the HDAC5 sign check before any HDAC5-directed arm, and the allele-class stratification of a T-type drug response.

## Receipts

49 receipts are staged in `disease-models/wwox/research/receipt_staging/it38_<package>/` (INV-02 4, INV-03/04 5, INV-05 5, INV-06 5, INV-07 5, INV-08 5, INV-09 5, INV-10 4, INV-15 1, INV-16 5, INV-18 5). Each passed `staged_receipt_check.py --check-doi` in isolation; no event id repeats across staging. Several reads are abstract-level and are labelled so in the receipts; a few PMIDs have another actor's claim (noted in `queries.tsv`). Trial-recording order and the prior-receipt chain are for the integrator, as in the earlier deliveries.

## Not proposed

No new `bridges.tsv` or `probe_links.tsv`; no new need; no change to the WO-30 order; no change to any hypothesis rank.

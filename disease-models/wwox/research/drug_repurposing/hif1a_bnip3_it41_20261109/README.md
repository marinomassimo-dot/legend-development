# IT41 package B — HIF1A to BNIP3: what the premise holds, what it does not, and the question that decides it (2026-11-09)

Non-canonical research material. Not medical advice; no dose, schedule, route or clinical preference. Reference genotype class only. One package, one producer, one independent blind verifier, one recheck of the substantive corrections. Task record `ledger/tasks/orchestrator/ORCH-IT41-20261109.json`. This premise is distinct from HIF1A to HK2 (`case_it9_p6_hif_axis_20261030/`); nothing there is changed or reused here.

## Decision this changes (labels: DATO / INFERENZA / IPOTESI)

* **The three proposals do not rest on a measured HIF1A to BNIP3 step in WWOX-deficient neural cells; the answer today is an abstention with a discriminating question.** DATO: IT21P2-0001 to 0003 (nitroglycerin, the antisense EZN-2968, PX-478; hypothesis H_HARM) cite `HIF1A -T(+)-> BNIP3` only as a printed example path of status PARTIAL_EXAMPLE (the strongest seed carries 11 percent of the contribution across 15 seeds); the edge is SIGNOR and rests on a review with no cell context, the primary record behind the same pair being Bruick 2000 in non-neural lines (one of about 200 references). The three compound identities are unresolved (Harness).
* **The transcript signal is small and not robust.** DATO: human KO organoid BNIP3 +0.46 log2 (1.38-fold; 4 against 2 libraries; in the deposit's up file at padj 0.0587, log2FC +0.38, smaller than the five named HIF-pattern genes). The neuron-library sign flip reported at first read is a scale artefact of the deposit's TPM column totals (264,496 control against 89,581 knockdown): sum-rescaled +0.60, centred +0.398; one library per arm, no null. Mouse P17 in vivo Bnip3 shows no consistent rise (-0.52, -0.07, -0.04, +0.41 log2). DATO: the organoid HIF pattern is only partial (EGLN3, HK2, ADM, BHLHE40, P4HA1 up; NDRG1, CA9, PGK1 flat; EPAS1 +1.97; BNIP3L -0.19).
* **No protein, flux or neural WWOX measurement of BNIP3 exists** (perimeter: PubMed and Europe PMC searches including the verifier's widened re-runs; Q01 0 hits, Q03 6 hits all non-neural). It is a search result, not a negative.
* **The direction of a BNIP3 change in neural cells is context dependent, so it is not to be inverted by default.** DATO (partial full text): BNIP3 loss worsens viability, ROS and apoptosis in HT22 oxygen-glucose deprivation, with no effect in normoxia (41972676), where BNIP3 protein falls; in the same line at 1 percent oxygen with glucose BNIP3 protein rises 12 to 48 h (42792606). IPOTESI: a BNIP3 rise can be a protective mitophagy receptor response, a death mediator, or a consequence of stress.
* **The one neural in-vivo test of HIF inhibition ran opposite to the engine sign.** DATO (41324728, LiCl-pilocarpine epileptic rat, non-WWOX): hippocampal HIF-1alpha up and BNIP3 down; the HIF-1 translation inhibitor KC7F2 (a 24 h pre-treatment, acting through 4E-BP and S6K per the source) lowered HIF-1alpha and raised BNIP3 (about 4-fold at 24 h in vehicle-injected controls; BNIP3 rose about 2.6-fold at 30 min to 2 h, before HIF-1alpha fell) while LC3-II/I fell; the authors read it as protective. The abstract of 42323821 (TBI, abstract only) reads HIF1A-BNIP3 mitophagy as protective too.
* **The mRNA-to-protein scale argument holds only partly.** DATO: in HT22 at 1 percent oxygen Bnip3 mRNA rises about 25-fold at 6 h and about 27-fold at 24 h (matched-time folds; the larger numbers in the paper are relative to 6 h normoxia) against about 2-fold protein; a 1.38-fold organoid change is far below that, and BNIP3 protein is also controlled post-translationally (HEK cells, 38443598).
* **WWOX to HIF1A is non-neural and mixed.** DATO: Wwox-null MEFs show more nuclear HIF1A protein; the one fibroblast WWOX line in the module shows less (earlier reading, reused); HIF1A mRNA is flat in the organoid.

## Status of the deliverables (nothing applied to a consumer)

| Layer | State |
|---|---|
| Sources newly read, with receipts | 5 staged in `research/receipt_staging/it41b/` (copies in `output/receipts/`), all pass `staged_receipt_check.py --check-doi`, none recorded: 42792606 HT22 hypoxia time course, 38443598 Mst1/2 and BNIP3, 41972676 BNIP3 and BNIP3L in vascular dementia and HT22 OGD (partial full text each); 41324728 HIF-1alpha/BNIP3 in epilepsy (partial re-read of Results and Fig 9, prior receipt FTR-20261019-41324728-01); 42323821 (abstract only) |
| Reused, no new receipt | 25012504 Abu-Remaileh 2014 (ledgered complete read; the string BNIP absent) |
| Not reached | full text of 42323821 (the PMC page returned a recaptcha challenge to the producer and HTTP 403 with an embargo notice, available June 2027, to the verifier; no other route tried); supplements; a primary source for FOXO3, p53, E2F1 or NF-kB on BNIP3 in neurons (not reached; 41 PubMed records exist, leads 38043200 and 34475505 unread) |
| Verifier (first pass) | 14 propositions: 9 supported, 5 partly, 0 not supported; 22 evidence rows, 3 defective notes; four substantive errors (fold basis in HT22, XMU-MP-1 and EGR1 misattributed in E2, omissions on KC7F2, the padj statement), the neuron-library sign flip re-derived from GEO as a scale artefact, a public datum added (EGR1 lower in the KO organoid, log2 -1.04, padj 0.038). All corrected. |
| Verifier (recheck) | 10 of 13 rows fully corrected, three small residuals (a missing timing, a stale access note, two stale cells) fixed by the Orchestrator; fingerprints reproduced for 38443598, 42792606 and 41324728 (41972676 not re-fetched) |
| Delivered tables | `output/decisive.tsv` (14), `output/explanations.tsv` (5, with the abstention), `output/new_measurements.tsv` (7), `output/evidence.tsv` (22), `output/figure_notes.tsv` (6), `output/queries.tsv` (10) |
| Proposals | `consumer_delta.md`: 6 rows; applied: 0 |

## The explanations and what each leads to (full cells: `output/explanations.tsv`)

| Row | Explanation | Study first (action) | Could be opposite or harmful | Control | Compound or class named by a source | Limit preventing candidacy |
|---|---|---|---|---|---|---|
| E1 | HIF-driven induction (HIF-1alpha or HIF-2alpha) | genetic HIF1A and EPAS1 knockdown as the reference | lowering HIF where BNIP3 is protective; an off-axis HIF-lowering compound mistaken for BNIP3 reversal | non-targeting control, isogenic add-back, oxygen series | KC7F2 (HIF-1 translation inhibitor; acts through 4E-BP and S6K); PX-478, EZN-2968, nitroglycerin unresolved | HIF protein never measured in WWOX-deficient mammalian neural cells; the one neural HIF-inhibitor test raised BNIP3 |
| E2 | HIF-independent induction or stabilisation (FOXO3, Mst1/2, mitochondrial stress) | the identified driver, genetic first | inhibiting the driver may remove a protective response | knockdown of the driver, matched oxygen and glucose | XMU-MP-1 (Mst1/2; BNIP3 not measured under it) | no WWOX neural datum; FOXO3, p53, E2F1, NF-kB not reached |
| E3 | culture-state artefact (organoid core hypoxia, density, medium) | none; fix the culture | acting on an oxygen-limited culture as WWOX biology | size- and density-matched controls, physioxia arm | none | one wild-type line, 2 wild-type libraries |
| E4 | no protein change | none | acting on a transcript | same-lysate protein and mRNA, flux with a lysosomal inhibitor | none | protein data absent |
| E5 | abstention | none now | reversing BNIP3 on a transcript; any HIF-lowering compound for a BNIP3 reason | M1, M2, M5 | none | all of E1 to E4 |

## The discriminating question, and what would change the priority

In isogenic WWOX-deficient against add-back human neural cells at matched oxygen: does BNIP3 protein rise; does it fall on HIF1A and EPAS1 knockdown; and does BNIP3 knockdown make survival, ROS and membrane potential better or worse? (M1 to M7 in `output/new_measurements.tsv`; the only public re-analysis, M7, the BNIP3 sign with and without library centring, is done by the verifier: scale artefact.) INFERENZA on priority: BNIP3 flat at protein level closes the premise for pharmacology; BNIP3 rising HIF-dependently with BNIP3 knockdown helping KO cells turns the HIF-lowering lever into a conditional hypothesis for a mechanism experiment; BNIP3 knockdown harming KO cells moves the question to add-back or stabilisation. A cheap check available now: EGR1 (a HIF1A repressor named in 42323821) is lower in the KO organoid (log2 -1.04, padj 0.038) — IPOTESI that fits E1, to be recomputed from the deposit counts.

## Counter-evidence and limits

* A concordance of signatures between deposits is not a clinical probability; a signal in HT22, rat hippocampus, MEFs or HEK cells is not a neural WWOX measurement.
* A response to a HIF-lowering compound would not show that HIF1A is altered in WWOX deficiency.
* Figure values read from bars are estimates (stated in `figure_notes.tsv`).
* Absence claims are perimeter statements, not proofs of absence.

## Novelty

* `new_to_legend`: the neuron-library sign of BNIP3 as a deposit-scale artefact; the partial HIF pattern with EGR1 lower and EPAS1 higher in the KO organoid; the protective reading of HIF inhibition and of BNIP3 increase in the two neural sources; the matched-time fold basis in HT22. Literature novelty: not assessed.
* `already_in_legend`: the three proposals and the SIGNOR edge; the MEF direction of WWOX to HIF1A.
* No compound proposed; PX-478, EZN-2968 and nitroglycerin identities stay with Harness.

## Queries run

10 rows in `output/queries.tsv` (PubMed tool, Europe PMC REST, NCBI efetch PMC, the open-data bucket, GEO supplementary files, one publisher PMC page recorded as unreachable and not retried).

# Independent verification of scientist-c W2 (main 7c48c528), 2026-10-27

Verifier is not the producer. Non-canonical audit note; edits no card, registry or current file. Each source was re-acquired from a
public route and read against the producer's statement, not the producer's summary.

Reading depth: Karnstedt 2026 (PMID 41489401, PMC13075606) full text via Europe PMC XML, Table 1 and Results read, supplements not
read. Breton 2021 (PMID 34634460, PMC8609180) full text via Europe PMC XML, Results 2.2-2.3 and Fig 3/4 legends read,
supplement not read. Obeid 2026 (PMID 42422765): repo copy of the PMC XML plus Figure 6 image (gr6.jpg) read by eye. Knowles 2022 and
PMID 27292539: PubMed abstract only. ChEMBL: live REST API, release ChEMBL_37. Organoid panel: rerun on the shipped counts file.

## Verdicts

| # | Statement | Verdict | Note |
|---|---|---|---|
| 1a | Memantine benefit 14/19 GoF vs 3/15 LoF/indeterminate/no-effect (Fisher P = .0049); behaviour 12/17 vs 3/15; development 6/12 vs 1/14; seizure 7/18 vs 2/10, P = .417; three GoF worsened | SUPPORTED | Every number matches the Results text. Both Fisher P values recomputed (0.00490, 0.41697). The three worsened (#10, #25, #32) are all GoF (Table 1, Group 3). |
| 1b | "benefited" = definition of benefit | UNDERSHOOT (card wording) | The 14 includes 4 individuals (#3, #7, #11, #22) whose effect faded (Group 2, "initial improvement, then habituation"); 10 had a sustained effect. At variant level with only sustained effect counted the authors report P = .0698 (not significant); only a "any positive observation per variant" analysis reaches P = .021. Benefit is clinician/parent-rated, retrospective, unblinded. README states the last two, not the first two. |
| 1c | Comparator group is "LoF, indeterminate or no-effect" | SUPPORTED, with a missed qualifier | Group 4 (n = 15) also contains 4 VUS/likely-benign cases (#8, #28, #29, #31) that the authors call non-pathogenic, so it is not a pure LoF group. Does not change the direction of the inference. |
| 1d | "Node, not sign" (DL-MECH-002 corroborates a shared node, not the sign of intervention) | SUPPORTED as inference; cohort part UNVERIFIABLE_SURFACE | Karnstedt supports sign-depends-on-lesion. GRIN2A is itself split inside the cohort: #20 improved, #7 transient, #6 not improved. The class of the burst-suppression GRIN2A cases (PMID 42190144) remains unknown, as the producer says. |
| 2a | Breton 2.3: -70 mV mEPSC is AMPAR-weighted; Mg block of NMDAR | NOT_IN_SOURCE (as source statement), reasonable INFERENZA | The paper gives holding potential -70 mV, TTX, ACSF Mg 1.3 mM, and never says AMPAR-weighted. The authors read the unchanged decay constant (5.18 vs 4.84 ms, p = .298) as "no overt change in the NMDAR:AMPA proportion". Producer's inference is standard electrophysiology; the card states a note that the authors read decay differently, which is correct. A residual NMDAR component at -70 mV with 1.3 mM Mg is not excluded. |
| 2b | "mEPSC ... frequency not [raised]"; "10 cells, 5 animals per genotype" | OVERSHOOT (small, two errors) | Legend: WT 10 cells / 4 animals, HT 10 / 5, KO 10 / 5. The KS p for frequency is WT vs KO 2.4e-4 and WT vs HT 1.8e-3; the text's "no change" holds only vs HT. The frequency does differ from WT (direction not stated in text). Card should say "amplitude up vs both; frequency not different from HT but different from WT". |
| 2c | d-APV 50 uM eliminated bursting; n = 5 slices, 3 animals (51 bursts) | SUPPORTED | Verbatim in the Fig 3 legend. |
| 2d | Authors call d-APV "a glutamatergic blocker" and write "Blocking glutamatergic neurotransmission with d-APV"; d-APV is NMDAR-selective; AMPAR never tested | SUPPORTED | Both phrases occur verbatim. The same paper later says "NMDAR-mediated glutamatergic neurotransmission is a requirement", so the authors do identify it as NMDAR; the wording is loose, not a wrong claim. |
| 2e | KS test on pooled events | SUPPORTED | Legend states KS on cumulative distributions across pooled events (pseudoreplication, as the producer noted). |
| 3a | F02: only MBP quantification is KO vs WT; treated-arm "near-complete rescue" is image-only (entries 6, 7, 43) | SUPPORTED | Fig 6 legend: C-E are bar graphs KO vs WT with ** / *** markers; F is "Representative MBP staining", WT / LD / HD, no bar. Verified on gr6.jpg: three columns, no axis, no KO column. The sentence quoted in entry 7 is in the Results. Entries 6, 7, 43 exist and say what the producer says. |
| 3b | "KO MBP reduced to 30-70 percent of wild type by region" (F02 card; manifest entry 43 reads the printed labels as "KO relative to WT") | OVERSHOOT (producer and manifest entry) | Reading Fig 6E bars: KO/WT is about 50 percent (CC), 72 percent (cortex), 49 percent (striatum), 30 percent (AC). The printed labels 48/30/50/70 percent match the REDUCTION (CC 48, cortex 30, striatum 50, AC 70), not the remaining fraction. The range happens to be about right (30-72) but the region mapping is inverted for cortex and AC. The legend wording "relative MBP intensity compared with WT" is ambiguous, which is how the error arose. Not a decision-changing error. |
| 3c | "New" finding that the treated arm is unquantified | PARTLY KNOWN | Claim 011's flag and the manifest (entry 6) already carried it; DL-MECH-031 itself says "MBP intensity only". What is new in F02 is only that DL-MECH-031 does not say the treated arm is image-level. Fair, but the CC calls it an addition. |
| 3d | DL-MECH-031 point 2 is an IPOTESI; Knowles 2022 points the other way | SUPPORTED | Registry text tags point 2 IPOTESI. Knowles abstract: seizure-driven oligodendrogenesis and myelination, prevented by seizure inhibition (Wag/Rij), and blocking activity-dependent myelination lowers seizure burden. Direction is "seizure activity raises myelination in a seizure network", so suppression need not raise it. Abstract-level only (producer says so). |
| 4a | ChEMBL_37 bumetanide (CHEMBL1072) curated mechanism: NKCC2 only (CHEMBL1874) | SUPPORTED | REST mechanism endpoint: 1 row, "Sodium-(potassium)-chloride cotransporter 2 inhibitor", SLC12A1. |
| 4b | NKCC1 (CHEMBL1615383): 3 activity rows (58.8 %, 71.7 % inhibition; IC50 1540 nM; CHEMBL5038596, CHEMBL5230131) | SUPPORTED | Exact match; the protein-complex target CHEMBL3885641 has 0 rows. |
| 4c | Memantine (CHEMBL807): no curated mechanism row | SUPPORTED | mechanism total_count = 0 in ChEMBL_37. |
| 4d | "37 NMDAR IC50/Ki rows on human or unknown-origin NMDAR" | OVERSHOOT (wording error) | 37 rows is right but 15 of them are Rattus norvegicus targets (10 + 1 + 1 + 2 + 1), 22 human. `chembl_pull.py` docstring and the F01 card ("human or unknown-origin GluN1 with GluN2A-D; species mixed") are wrong on origin; the TSV has no organism column, so a reader cannot catch it. The 0.95 nM minimum is a human GRIN1/GRIN2A row. |
| 5 | Organoid panel rerun | SUPPORTED (script) | `organoid_panel.py` rerun on the repo counts file (sha256 54259fc1...): output byte-identical to `organoid_panel_cpm.tsv`. |
| 5a | SLC12A2/SLC12A5 ratios 0.24, 0.29, 0.13, 0.14 vs 0.29, 0.30; descriptive only | SUPPORTED | Matches TSV. SLC12A2 itself is flat (5.0-5.5 vs 4.7-5.8 CPM); the lower KO ratio is driven by SLC12A5 in cko3/cko4, which coincide with high GAD1 (composition). Worded as descriptive, "transcript is not E_GABA". |
| 5b | "GRIA1 is higher in all four knockouts (98-162 vs 90-105 CPM)" (README); "nominally higher in all four knockouts than in either wild type" (F01 DA-W2-004) | OVERSHOOT | cko3 = 103.3 and cko4 = 98.0 are below cwt2 = 104.8; the ranges overlap. True for cko1 and cko2 only (150, 162). Direction was already recorded UNKNOWN and the text calls it a prompt, so the practical harm is small, but the sentence is wrong. |
| 5c | "No GRIN2B/GRIN2D shift" | SUPPORTED, borderline | GRIN2D overlaps. GRIN2B cko2 = 45.5 vs WT 20-27 is the highest value; "no consistent shift at n = 4 vs 2" is the safe wording. Not stated as significance. |
| 5d | WWOX CPM is not lower in the knockouts (10-17 vs 10-10) | NOT_IN_SOURCE (producer silent) | Not an error. The CKO design leaves the transcript; noting for any reader treating CPM as knockout confirmation. |

## Overreach scan (cards F01-F03, CC)

- No efficacy language, no dose, no suitability statement found. The HYP is `IPOTESI`, `generated`, with BLOCK-1 declared unassessed.
- "Evidence PRO" in the CC lists the 14/19 result for a WWOX hypothesis. It is a GoF-channelopathy result and WWOX has no demonstrated receptor gain-of-function. It is also the "benefit" that includes four faded responses. Suggest moving it to "context" or adding "of which 4 transient". Minor (OVERSHOOT of placement, not of claim, since the same item is carried under CONTRA).
- "KO = rescue", "seizure control = development": not found. F01/F02 explicitly keep burst control apart from recovery (N-15).
- Abstentions carry reasons and reopening conditions; F03 correctly says NKCC1 is an activity-table fact.

## Error versus uncertainty

Errors (checkable, wrong): 2b (WT animal count, frequency vs WT), 3b (MBP percent mapping), 4d (rat rows labelled human/unknown), 5b (GRIA1 "all four"), 1b omission of the transient group.
Uncertainty (not resolvable here): GRIN2A variant class in PMID 42190144; Karnstedt supplements; the Breton supplement S3 (not re-seen by anyone in this chain beyond the manifest attestation); Knowles and bumetanide trials beyond abstract.

## Net

The load-bearing claims (Karnstedt counts and P values, node-not-sign, F02 image-only treated arm, ChEMBL identity statements, panel reproducibility) stand. Five small wording or count errors should be corrected in the cards or noted by the integrator; none changes a hypothesis status, abstention or the proposed experiment.

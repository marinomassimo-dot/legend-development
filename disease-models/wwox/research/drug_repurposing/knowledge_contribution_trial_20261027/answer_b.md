# P3A answer, condition B (local WWOX knowledge only)

Research-only. Nothing here is medical advice, a dose or a treatment proposal. All identifiers below were seen in local repository files (worktree sci-a-p3a). Tags: DIRECT = WWOX model (human or mouse Wwox), INFERENCE = local reasoning or exploratory analysis, OTHER = other disease or species (fly amyloid model, ALS, VWM, tumour cells, enzyme assays).

Shared caveat for C1-C4: the local cards (E01-E04) have `directional_summary: UNRESOLVED`, `assessment: REQUIRES_QUALIFICATION`, `epistemic_status: IPOTESI`. The bridge found no disease assertion that matches any compound assertion on target, endpoint and context.

---

## C1  Integrated stress response (eIF2B activators such as ISRIB)

**Q1.**
- Target and direction: eIF2B complex (EIF2B1-5) or the PERK arm (EIF2AK3). Direction: attenuate the ISR (activate eIF2B / inhibit PERK). The intended endpoint is ATF4 protein, eIF2alpha phosphorylation and ATF4-target transcripts, then a network, synaptic or myelin endpoint. Card E01 states this as an endpoint to be pursued, not as a measured one.
- DIRECT (WWOX human) evidence: none. No WWOX-deficient human neural system has a measured eIF2alpha-P or ATF4 protein level (E01 `not_known`).
- WWOX-biology, other context (OTHER: Drosophila):
  - Neuronal Wwox RNAi (mRNA about 0.55 of control) plus Abeta42 raises Atf4 immunofluorescence (DA-LC-ATF4-001; about 1.0 to 1.2-1.3 normalised, n 6 brains, one antibody).
  - The same genotype without amyloid shows no change (DA-LC-ATF4-002; P 0.9305).
  - Atf4, PERK and eIF2alpha-P are never perturbed or measured in the paper (PAPER 567, PMID 42909904; CLAIM 025 nuance). The Atf4-to-Ldh arrow is the authors' inference.
- INFERENCE (exploratory): in the human WWOX-knockout cerebral organoid transcriptome (GSE156243, deposit of PMID 34268881) the 12 ATF4/ISR target transcripts are lower than chance (DA-GSE-ISR-003; P 0.0005 versus random sets). Caveats: 4 KO versus 2 WT libraries, one laboratory, nine set tests uncorrected, genotype and maturity confounded. This is an exploratory negative for the transcript signature without amyloid. It is not evidence that the ISR is normal.
- OTHER (compound precedents, not WWOX evidence):
  - DR-E01-001, PMID 40825784: ALS, eIF2B activator DNL343, target engagement in blood and CSF.
  - DR-E01-002, PMID 42771346: ALS randomised trial, rate ratio 1.04 (0.83-1.32), no benefit despite engagement.
  - DR-E01-003, PMID 42179084: 5xFAD mouse, eIF2B activator 2BAct, recognition memory and tau improved, amyloid not.
  - DR-E01-004, PMID 42586097: guanabenz in children with vanishing white matter. Hazard ratio 0.33 (0.16-0.69) against registry controls, non-randomised. Serious adverse events in about three quarters of 33 children.
- Class-level statement: ISRIB and fosigotifator have no eIF2B activity row in ChEMBL, and DGIdb and Open Targets are empty for the eIF2B complex (E01 pharmacology field). Compound identity and target are therefore not verified through those databases.

**Q2.**
- Counter-evidence and limits recorded locally:
  - The fly Atf4 rise needs amyloid.
  - The only signed human readout (organoid) points the opposite way from the fly.
  - The ALS trial engaged the target without benefit.
  - The paper itself cites Ldh knockdown as detrimental in other fly amyloid models, a reminder that attenuating a stress arm has a cost.
  - If the ISR is adaptive, attenuation could add harm (E01 `expected_contribution`).
- Transfer risks:
  - Species (fly), disease (amyloid toxicity, ALS, VWM) and age (adult versus developmental encephalopathy).
  - VWM is an eIF2B-lesion disease, so a drug effect there says little about a WWOX loss.
  - Compound-versus-target risk: eIF2B-activator rows are empty in the target databases, and the one paediatric dataset concerns guanabenz, a different mechanism family.
  - Allele: no Q230P or null-allele datum exists.
  - The absence of any WWOX-ISR link is only "not found by these queries" (DGIdb, ChEMBL, Open Targets, PubTator gene censuses and eight PubMed searches of 2026-10-26, as recorded in E01).

**Q3.**
- Propose a measurement (research only), as recorded in E01 `next_measurement`:
  - Stage 1: eIF2alpha-P, ATF4 protein and ATF4-target transcripts in WWOX-deficient versus isogenic human neural cells at matched maturity, with and without a defined proteotoxic challenge. This decides everything after it.
  - Stage 2, only if Stage 1 shows elevation: an eIF2B activator versus vehicle on that readout and on one functional endpoint.
  - Fly: an Atf4 loss-of-function arm with Ldh and lactate readouts.
- Abstain from any statement that an ISR modulator would help. The reopening condition is a measured WWOX-dependent ISR elevation in a human neural system. If it is not elevated, the card says to park the question.

SOURCES: card E01_isr_modulators (packet and card JSON, P4-E-01); DA-LC-ATF4-001/-002; DA-GSE-ISR-003; DR-E01-001..004; PAPER 567 (PMID 42909904, manifest PMID42909904.json, receipt FTR-20261026-42909904-01); CLAIM 025; PMID 34268881 / GSE156243 (gse156243/prediction_isr_ldh_chain_20261026.md, cited by the card, not opened by me); PMIDs 40825784, 42771346, 42179084, 42586097.
DEPTH: PAPER 567 / PMID 42909904: local record carries a complete full-text read receipt (FTR-20261026-42909904-01). I read the card and CLAIM 025 text derived from it, not the paper. GSE156243 analysis: deposited-table query, "queried_not_full_read"; PMID 34268881 itself carries full-text receipts per DL-MECH-034 (full text read). PMIDs 40825784, 42771346, 42179084, 42586097: abstract only (card `reading_depth: abstract_only`), unaudited. Database rows (ChEMBL, DGIdb, Open Targets) are database rows only, seen only as the card's summary.

---

## C2  LDH inhibition (e.g. stiripentol)

**Q1.**
- Target and direction: LDHA (HGNC:6535) and LDHB (HGNC:6541); lower LDH activity or lactate production. Endpoint: LDH activity and lactate-pyruvate relationship in WWOX-deficient versus isogenic human neural cells, then a locomotor, network or myelin endpoint (E02 `endpoint_pursued`).
- DIRECT (WWOX human): no LDH-inhibition datum.
- DIRECT but conflicting, human lactate readouts (DL-BIO-008, DL-BIO-009):
  - One patient's brain MRS shows "extremely low" lactate (PMID 30362252, Davids 2019; the ledger says full text read; the patient also carries a confounding second variant in HSPG2).
  - Plasma lactate was normal in two patients (Shaukat 2018) and the metabolic and mitochondrial screen was entirely normal in a null/null WOREE patient (PMID 24456803, Abdel-Salam 2014).
  - DL-BIO-009 concludes human WWOX metabolism is, as far as measured, normal, and lactate is not a usable WWOX biomarker.
- DIRECT (mouse): Wwox-KO mice have raised serum lactate and lethal hypoglycaemia (PMID 25012504, Abu-Remaileh and Aqeilan 2014, cited in DL-BIO-008).
- OTHER (fly, PAPER 567):
  - Ldh transcript is about +1.29 log2 with Wwox RNAi plus Abeta42 (DA-LC-LDH-001).
  - Lactate is up +1.30 log2 (interaction F 23.606, adj. P 0.0174; DA-LC-LAC-001) and nominally down -0.43 log2 without amyloid (DA-LC-LAC-002).
  - Climbing is reduced in Wwox RNAi plus Abeta42 (DA-LC-CLIMB-001). Ldh RNAi partly rescues climbing in that genotype (DR-E02-GEN-001). The card compares this as "OPPOSES_DISEASE_CHANGE", i.e. the genetic lowering of the target opposes the disease-side change. It is one experiment: no Ldh-alone arm, no Wwox mRNA check in the double-RNAi line, no lactate measured in it.
- INFERENCE (exploratory): human WWOX-KO organoid LDHA transcript is up (+0.75 by the script, +0.91 on the authors' list, padj 5e-6; DA-GSE-LDH-002). It falls with elapsed culture time in WWOX-unperturbed spheroids, so it is as consistent with an immature tissue as with a WWOX effect. Transcript, not activity.
- OTHER (compound):
  - Stiripentol inhibits LDH only weakly in vitro, on single-concentration measurements:
    - DR-E02-001: ChEMBL document CHEMBL4311969 = Bai 2019, PMID 31539780. Single-digit percent inhibition at the highest (millimolar) concentration.
    - DR-E02-004: PMID 39769031 (Rico-Molina 2024). Racemate about a tenth, enantiomers about a third each, at one high-micromolar concentration. The IC50 is a bound, not a fitted value.
    - DR-E02-005: PMID 25792327 (Sada 2015, Science). LDH inhibition hyperpolarised neurons and suppressed seizures in a mouse model. Known here only from its abstract plus other papers' descriptions.
  - GSK2837808A: low-nanomolar on LDHA (DR-E02-002, ChEMBL CHEMBL3335794 rows; no CNS datum).
  - Nedosiran, LDHA-directed oligonucleotide: liver-directed, approved for primary hyperoxaluria (DR-E02-003, Open Targets).

**Q2.**
- Counter-evidence recorded locally:
  - The fly lactate and Ldh rise needs amyloid. Without amyloid, Ldh does not change and lactate falls nominally.
  - The authors cite Ldh knockdown as detrimental in other fly amyloid models.
  - Human lactate in WWOX deficiency is normal or low (DL-BIO-008, DL-BIO-009).
  - The organoid LDHA rise is confounded with maturity.
- Stiripentol, compound-versus-target confusion:
  - Its potency on LDH is not established.
  - DR-E02-006: in glioblastoma cell lines (PMIDs 42035940, 36278433) and a complex I paper (PMID 41570991), viability falls at tens of micromolar while lysate LDH activity falls significantly only at hundreds of micromolar. Complex I is inhibited directly and fast. Cellular effects are therefore not attributable to LDH.
  - DR-E02-007: review PMID 38443647 (Bacq 2024) states in-vitro LDH-inhibiting concentrations lie at or above total plasma levels at antiseizure doses and well above estimated free tissue levels, and ranks LDH inhibition last among stiripentol's mechanisms.
  - Stiripentol's approved use is with clobazam in Dravet syndrome (openFDA label retrieved 2026-04-27), an interaction the card does not assess.
- Transfer risks: species, tissue (whole fly head; glia carry the highest Wwox mRNA, so a neuronal origin of lactate is unproven), disease (amyloid, tumour, hyperoxaluria).
- The brain LDH engagement claim for stiripentol rests on a paywalled paper never read at full text.

**Q3.**
- Next measurement (E02 `endpoint_pursued`): LDH activity and enantiomer- or isotope-resolved lactate-pyruvate in WWOX-deficient versus isogenic human neural cells at matched maturity, before any inhibitor test. Also a fitted LDH IC50 for stiripentol in a cell-free assay, since only single-concentration data exist. Local records also name the Sada 2015 full text as unacquired.
- Abstain from asserting that LDH inhibition would benefit WWOX deficiency. Reopening conditions: lactate or LDH activity shown altered in a WWOX human neural system independent of maturity, and evidence for stiripentol brain engagement.

SOURCES: card E02_ldh_inhibition (P4-E-02); DA-LC-LDH-001, DA-LC-LAC-001/-002, DA-LC-CLIMB-001, DA-GSE-LDH-002, DA-BIO008-001; DR-E02-001..007, DR-E02-GEN-001; DL-BIO-008, DL-BIO-009 (read via registry_records.py); PAPER 567 (PMID 42909904); PMIDs 31539780, 39769031, 25792327, 42035940, 36278433, 41570991, 38443647, 30362252, 24456803, 25012504; CHEMBL4311969, CHEMBL3335794.
DEPTH: PAPER 567: full-text receipt FTR-20261026-42909904-01 (via card, not opened by me). PMID 39769031: partial full-text read (card). PMID 30362252: full text read per DL-BIO-008. PMIDs 42035940, 36278433, 41570991, 38443647: targeted passages of open-access full texts, `queried_not_full_read`. PMID 25792327: abstract only plus secondary descriptions. PMID 31539780: paywalled, abstract only; the ChEMBL activity rows are database rows. PMIDs 24456803, 25012504: cited inside DL-BIO-008/009, not opened by me (depth not independently verified). Nedosiran, GSK2837808A: database rows only. DA-BIO008-001: card gives `reading_depth: UNKNOWN`.

---

## C3  PDK inhibition (e.g. dichloroacetate)

**Q1.**
- Target and direction: PDK1-4 (HGNC:8809-8812), not PDPK1 (HGNC:8816). Direction: inhibit PDK to release PDH. Endpoint: PDH activity and labelled-glucose fate (E03 `next_measurement`). The card status is "deferred with reason".
- DIRECT (WWOX mouse): Wwox-KO shows PDK1 upregulated by qRT-PCR, plus GLUT1, HK2 and PKM2. Serum lactate is up and WWOX binds HIF1alpha via WW1; digoxin (HIF1alpha inhibition) reverses the phenotype in KO (HYP-20260709-01 UPGRADE 2026-07-09b, citing PMID 25012504, PMC4211377; MEF, mouse, cancer-adjacent context).
- DIRECT (human organoid, transcript): the WWOX-KO organoid RNA-seq shows OXPHOS down and glycolysis enriched (DL-MECH-034, PMID 34268881, full text read; n 4 versus 2; the ledger itself says transcript is not flux).
- INFERENCE (exploratory): in that same dataset PDK1 is -0.34 and the PDK/PDH set is +0.17 (P 0.22, not different from chance); the LDH-to-PDH ratio is not shifted (DA-GSE-PDK-003). These are negatives that do not show PDH or lactate normal.
- Fly (PAPER 567): nothing measured on PDH, PDK, pyruvate, flux or NAD/NADH (DA-LC-PDH-001; direction UNKNOWN by design). The metabolomics deposit MTBLS12344 is not publicly retrievable.
- OTHER (compound):
  - DR-E03-001: dichloroacetate (CHEMBL306823) is a curated PDK inhibitor, weak in the retrieved in-vitro assays. Open Targets lists phase 3 for congenital lactic acidosis; no US label found.
  - DR-E03-002: AZD7545 and VER-246608 are enzyme tools on PDK2, with no CNS or paediatric datum.
  - DGIdb returns PDPK1 agents for the symbol PDK1 (a symbol collision documented in the card).
- Human WWOX patient datum: none on PDH.

**Q2.**
- Counter-evidence recorded locally:
  - The fly study measured nothing in this branch.
  - The organoid PDK1 transcript is down and the PDK/PDH set is at chance.
  - The sima:GFP (HIF1alpha-homologue) reporter is unchanged in the fly. The authors name Atf4 rather than sima as primarily responsible for Ldh.
  - Human metabolism in WWOX deficiency is normal as measured (DL-BIO-009).
  - Known neurotoxicity concern: the repository's safety position for the main compound is peripheral neuropathy (BLOCK-1, per card). The ketogenic hypothesis dominates it on safety (card).
  - The HIF1alpha axis in vivo is shown only for five promoters in mouse liver (PKM, GAPDH, HK2, Glut1, Aldoa), not Pdk1 or Ldha, and context-dependent (CLAIM 025 boundary, PMID 29724996). The Desiderio-group HIF1alpha branch is on a retraction watchlist and does not count as independent corroboration (HYP-20260709-01).
- Transfer risks: mouse MEF/liver to human CNS; transcript to flux; compound-versus-target (symbol PDK1 versus PDPK1; the card excludes devimistat because DGIdb gives it no PDK action type); weak in-vitro DCA potency.

**Q3.**
- Next measurement: PDH activity and labelled-glucose fate in WWOX-deficient versus isogenic human neural cells (E03). Seahorse OCR/ECAR on donor-derived cells or the existing KO organoids is the shared first step (HYP-20260709-01). If PDH and pyruvate fate are normal, the hypothesis stays parked with a stronger negative; if blocked, E03 and the ketogenic hypothesis reopen.
- Abstain from asserting a benefit of DCA. The status is "deferred with reason".

SOURCES: card E03_pdk_inhibition_dca (P4-E-03); DA-LC-PDH-001, DA-GSE-PDK-003, DA-GSE-LDH-002; DR-E03-001/-002; HYP-20260709-01, HYP-20260709-05 (named in card), N-08, DL-MECH-020, DL-MECH-034, DL-BIO-009; CLAIM 025; PAPER 567 (PMID 42909904); PMIDs 34268881, 25012504, 29724996; CHEMBL306823; MTBLS12344.
DEPTH: HYP-20260709-01, DL-MECH-034, DL-BIO-009, CLAIM 025 read by me as ledger text. PMID 34268881: full text read per DL-MECH-034 (and receipt FTR-20261004-34268881-07 per DL-MOL-003). PMID 25012504: primary data acquired per the hypothesis ledger; I did not see its receipt. PAPER 567: full-text receipt FTR-20261026-42909904-01 (via card). DCA, AZD7545, VER-246608: database rows (ChEMBL/DGIdb/Open Targets) only, `queried_not_full_read`. GSE156243 analysis files: `queried_not_full_read`. HYP-20260709-05 and N-08: named only in the card; I did not open them.

---

## C4  Ketogenic diet and the lactate axis

**Q1.**
- Target and direction: no molecular target. The rationale is a bypass: ketone bodies enter the TCA cycle downstream of PDH, if WWOX loss causes the HIF1alpha-PDK1-PDH block (HYP-20260709-01). The card E04 candidate is a diet; it carries no drug assertion. The card status is "abstention" (abstention_card present).
- Endpoint: Seahorse OCR/ECAR on donor-derived WWOX-deficient cells or the existing KO organoids (HYP-20260709-01 "minimal falsification experiment").
- DIRECT (mouse and mouse cells): Wwox-KO MEF show raised glucose, lactate, lowered ATP and O2 consumption, and HIF1alpha up in normoxia (DL-MECH-020, as stated in HYP-20260709-01). The KO mouse has lethal hypoglycaemia, so GLUT1-deficiency is the analogy invoked.
- DIRECT (human organoid, transcript): OXPHOS down and glycolysis up in WWOX-KO organoids (DL-MECH-034). Transcript only; n 4 versus 2.
- DIRECT (human patients), lactate:
  - Brain MRS lactate "extremely low" in one patient (Davids 2019, PMID 30362252, confounded by an HSPG2 variant).
  - Systemic metabolic screens normal in several patients (DL-BIO-009).
  - Net: the human sign of the lactate axis is unmeasured. The ledger says explicitly that lactate is not a reliable WWOX biomarker and that the easiest endpoint was lost (DL-BIO-008).
- DIRECT (clinical observation): in the WWOX-DEE cohort of Oliver 2023, the ketogenic diet was tried in 3 patients and continued in only 1 (2 stopped for poor tolerance or benefit). Cited in HYP-20260709-01 via DL-MECH-030. This is a continuation pattern, not efficacy, and runs against the mechanistic expectation.
- OTHER (fly, PAPER 567): lactate up with Wwox RNAi plus Abeta42, nominally down without amyloid (DA-LC-LAC-001/-002). No diet, ketone, pyruvate or PDH arm (DA-LC-PDH-001). The card concludes the paper neither supports nor refutes the ketogenic hypothesis.
- OTHER (direction control): MCT1/SLC16A1 blockade via AZD3965 appears in DGIdb as a direction control only (database row).

**Q2.**
- Counter-evidence recorded locally:
  - Human systemic metabolism is normal (DL-BIO-009).
  - Brain lactate is low in the one MRS.
  - The ketogenic diet was poorly continued in the Oliver 2023 cohort.
  - The transcriptome is not flux.
  - The mouse dies of hypoglycaemia while the reference genotype does not.
  - If Seahorse is normal in donor-derived cells, the WWOX-specific rationale falls (HYP-20260709-01, DL-BIO-009).
- Transfer risks: mouse to human; transcript to flux; the fly lactate result is amyloid-conditional and "cannot be used for or against the Warburg direction in WWOX-null neurons" (E04 `transfer_limits`). The diet's empirical anti-seizure use in epileptic encephalopathies is independent of any WWOX mechanism and must not be confused with a WWOX-specific rationale.
- The card leaves any treatment decision to the treating clinical team and does not address it.

**Q3.**
- Propose the one measurement that still decides it (missing datum in the abstention card): a bioenergetic flux measurement (OCR and ECAR) in WWOX-deficient versus isogenic human neural or donor-derived cells. It has never been done in any WWOX human system (recalibration of 2026-09-21).
- Abstain from the ketogenic hypothesis itself until then. Reopening condition: a flux measurement in a WWOX human system, or release of the pyruvate rows of MTBLS12344.

SOURCES: card E04_ketogenic_lactate_axis (abstention_card); HYP-20260709-01; DL-MECH-020, DL-MECH-034, DL-MECH-030 (named in HYP-20260709-01), DL-BIO-008, DL-BIO-009; PAPER 567 (PMID 42909904); PMIDs 34268881, 30362252, 25012504, 24456803; DGIdb SLC16A1 rows (via card).
DEPTH: HYP-20260709-01, DL-MECH-034, DL-BIO-008, DL-BIO-009 read as ledger text by me. DL-MECH-020 and DL-MECH-030 were not opened; known only through HYP-20260709-01 citations. PMID 34268881: full text read per DL-MECH-034. PMID 30362252: full text read (DL-BIO-008). PAPER 567: full-text receipt (via card). Oliver 2023: reached only through the hypothesis ledger's secondary statement; its PMID and depth were not seen by me. DGIdb: database row only.

---

## C5  Lithium / GSK3beta inhibition

**Q1.**
- Target and direction: GSK3beta, inhibit (lithium, "GSK3beta among many"). Endpoint seen in the only WWOX experiment: PTZ-induced seizure suppression in mice (mechanism_intervention_map R-04 and CLAIM 016).
- DIRECT (mouse Wwox-null), PAPER 019 = Cheng 2020, PMID 32000863, Acta Neuropathol Commun; DOI 10.1186/s40478-020-0883-3:
  - Lithium chloride significantly suppressed PTZ-induced seizures in Wwox-/- mice (Fig. 7d). The figure shows suppression in all three genotypes, wild type included. For ethosuximide (Fig. 7b) the text declares n.s. in +/+ and +/- and significant in -/-, and for lithium it declares no converse. The experiment therefore does not establish a WWOX-specific pharmacological rescue (CLAIM 016 evidence boundary; N-02).
  - Mouse GSK3beta Ser9 phosphorylation falls (-52%/-44%/-36% by region) and total GSK3beta moves +9/+13/+18%. Single lane, `STATISTICAL_STATUS: NOT_TESTED`, so visual trends only (CLAIM 016). The ledger says "elevated abundance" is not assertable.
- DIRECT biochemistry (not human patient): WWOX physically inhibits GSK3beta through an Axin-like docking motif 388-407 (L404) in the SDR domain, Ser9-independent (CLAIM 035, PAPER 056 = Wang 2012; CLAIM 016 addendum). The WWOXtide safety argument "safer than lithium because substrate-selective" is rejected (DIS-009; inhibition of GS-1 to about 18% of control).
- DIRECT (human): no lithium datum in WWOX patients. The map records "lithium in paediatric neuropsychiatry; nothing in genetic DEE". Human use status: approved, low therapeutic index, thyroid and renal monitoring.
- INFERENCE, sign conflict on a second axis (DL-MOL-003): WWOX normally sequesters DVL2, so loss would hyper-activate Wnt/beta-catenin and lithium stabilises beta-catenin, i.e. activates Wnt. The map therefore calls the expected direction "conflicted across two admitted axes" (plausibly beneficial on GSK3beta/Tau, harmful on Wnt). Belief for the Wnt direction is "medium" and it stays IPOTESI. The three primaries are cancer or epithelial work, not neural; Celebi 2020 (PMID 32368285, full text read) measures no Wnt output.
- DIRECT (human organoid, transcript): the WWOX-KO organoid shows a raised canonical Wnt readout, 4 of 4 transcriptional readouts up (AXIN2, LEF1, NKD1, APCDD1; P 0.0001), and nuclear beta-catenin about 1.7x (DL-MECH-034; prediction_wnt_sign_20261025). Weakened by controls: the Wnt score correlates +0.99 with a progenitor score, -0.97 with a neuronal score, so a maturation difference cannot be separated. No GSK3 or CK1 gene is on the list. The data "do not favour the tankyrase family or the GSK3-inhibitor family".
- OTHER (cards): D02 records a GSK3 inhibitor in adult kainate epilepsy where Wnt activation reduced two of four histological markers in one model, in the opposite direction and a different disease. A LINCS/SigCom reversal analysis lists TWS-119 (a GSK3beta inhibitor) at rank 3 among top-40 reversers (prediction_lincs_context_stratification_20261026.md), which I did not examine in detail; the file itself says the S0, S2, S3 rows and the tissue annotation were unseen when written. Treat as untested for this question. Cached ChEMBL lookups returned a "LITHIUM" pref_name; this is a compound-identity row only, not evidence.

**Q2.**
- Counter-evidence recorded locally:
  - Failed specificity test: lithium also suppressed seizures in wild type (CLAIM 016; N-02; map R-04 "T5, not T2").
  - Mutual exclusion on the Ser9 axis: CLAIM 016 and CLAIM 035 cannot cite each other as corroboration (CLAIM 016, D6). CLAIM 035 predicts the Ser9 assay is a false negative for the mechanism.
  - Pathway-direction contraindication (DL-MOL-003).
  - Narrow therapeutic index, and the ledger flags a GSK3beta2 developmental-window risk not carried by the safety score (canonical_impact_and_negative_audit, TX-005).
  - The lithium panel was cited as Fig. 7b in one place and is Fig. 7d (map footnote).
  - The earlier "GSK3beta elevated abundance" premise has no datum under it.
- Transfer risks: mouse severe full KO (the Wwox-null mouse dies at 3-4 weeks) to human WOREE; PTZ seizure suppression is an anticonvulsant effect, not a disease mechanism; a review (Steinberg and Aqeilan 2021, PMID 34831305) transmitted the genotype-specific reading that the primary does not support. Identifier risk: lithium acts on many targets besides GSK3beta; "GSK3beta inhibition" and "lithium" are not interchangeable; the ledger's "GSK3beta" row (CLAIM 016) concerns Ser9 phosphorylation, not activity.
- The densitometry denominators for the lithium panel are not recorded in the repository's locators (denominator_audit_therapeutic_portfolio_20260922).

**Q3.**
- Next measurement (the map's decisive test, R-04 and N-02): a PTZ plus lithium arm with an explicit, statistically tested -/- versus +/+ comparison, or a different GSK3beta inhibitor under the same design. Mechanistic read-out suggested by the cards: a measured activation step in WWOX-deficient neural cells (a Wnt reporter or nuclear versus cytosolic beta-catenin) before choosing the GSK3beta or the Wnt-lowering direction; a rescue contrast (re-express WWOX in the KO organoid) separates Wnt from maturation (prediction_wnt_sign_20261025). A dose-by-timing series in developing cortex is named as the missing datum in D02.
- Abstain from any claim that lithium or GSK3beta inhibition is a WWOX-specific rescue. Reopening conditions as stated in N-02: a PTZ arm with a tested genotype contrast, or a different GSK3beta inhibitor under the same design. For the Wnt axis: a neural measurement fixing the sign.

SOURCES: CLAIM 016, CLAIM 035 (named in CLAIM 016), DL-MOL-003, DL-MECH-034, DIS-009 (via CLAIM 016/map), PAPER 019 / PMID 32000863 (manifest PMID32000863.json, receipt FTR-20260804-32000863-01), PAPER 056 (Wang 2012), PMID 32368285, PMID 34268881, PMID 34831305; analysis/mechanism_intervention_map.md (R-04, N-02, chain C and Wnt chain); analysis/canonical_impact_and_negative_audit.md; analysis/denominator_audit_therapeutic_portfolio_20260922.md; analysis/data/WWOX_therapy_levers.csv (lithium row, scores 3.0/2.6 "promising", PMID 32000863); research/drug_repurposing/cards/D02_wnt_tankyrase.card.json; cards_early/EB-ETX-01.card.json; gse156243/prediction_wnt_sign_20261025.md; gse156243/prediction_lincs_context_stratification_20261026.md.
DEPTH: Cheng 2020 (PMID 32000863): local receipt FTR-20260804-32000863-01 (complete full-text read; locators 6 of 6 SUPPORTED with soft corrections per EB-ETX-01 card; I read the registry/map text, not the manifest). Wang 2012 (PAPER 056): read per CLAIM 016/035 (a 2026-09-27 blind audit corrected a detail); receipt not opened by me. PMID 34268881: full text read (receipt FTR-20261004-34268881-07). PMID 32368285: full text read (receipt FTR-20261004-32368285-01). PMIDs 19465938 and 23030478 (Bouteille, Li): no full-text read in LEGEND (DL-MOL-003 boundary: "abstract-level"). PMID 34831305: promoted record, review, depth not checked by me. TWS-119 / LINCS: analysis file only, partially seen. GSE156243: exploratory analysis of a deposited table, not a read. Lithium ChEMBL cache: database row only. The WWOX_therapy_levers.csv row is a scored summary list, not a read.

---

## Cross-case honesty notes

- I did not open the paper registry or literature tracking log directly. CLAIM, DL-* and HYP records were reached with `registry_records.py get --id` or by reading the ledger files; PAPER 567/019/056 and all PMIDs were seen only via those records and the cards. I did not independently verify any quote against full text.
- Card statements marked INFERENZA, including what a compound would do in WWOX-deficient tissue, are owed a blind audit by another actor (card `scope_of_checks`). The compound-side statements are abstract-level and unaudited.
- The two "novelty" claims ("no source links an ISR modulator / LDH inhibitor to WWOX") are zeros of specific database and PubMed queries on 2026-10-26, not statements about the whole literature. I could not re-run or check them (live queries forbidden).
- I did not open: `compounds_and_sources.md`, `biological_needs.md`, `sada_ldh_precedent_p2a_20261026.md`, the gse156243 ISR/LDH/PDK prediction files, or DL-MECH-020/030/HYP-20260709-05; statements about them come from card text only.

RUN LOG: 17 tool calls in total (including this write). Tools: Read (questions file; framework/scripts/README.md; one persisted output file holding my own earlier command output), Bash (ls; python3 JSON dumps of the cards E01-E04; git grep inside the worktree excluding the two large registries; sed/grep over mechanism_intervention_map.md, prediction_wnt_sign_20261025.md, the therapeutic_hypotheses_ledger and discovery_ledger; `framework/scripts/registry_records.py get --id` for CLAIM 016, CLAIM 025, DL-MOL-003, DL-BIO-008, DL-BIO-009 and an attempted HYP-20260709-01 lookup that returned no record, and `--help`), Write (this file). No network, no live adapter, no PubMed/Europe PMC/Open Targets/ChEMBL/DGIdb/PubTator query, nothing under p3a or knowledge_contribution_trial paths, nothing in /tmp except the specified questions and answer files.

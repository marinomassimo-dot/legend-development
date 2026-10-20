# COMMIT CANDIDATE — CC-20261019-SCIENTIST-B-H3-AUTONOMIC-HYPOGLYCAEMIA-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-b`, interventions batch 2026-10-19 group H3, branch `task/INTERV-H3-B-20261019`.
**context_policy:** `SOURCE_FIRST` for every reading cited (first reads); registry comparison admitted after each first pass.
**target_wm_version:** `WM_v7.20_2026-10-04`. **Change class:** **MINOR** — new paper-registry records and evidence-boundary notes; no claim status, no baseline claim reversed, no working-model block change. The legend-locator-audit trigger is not met; the triples below are supplied for a later blind audit.
**Not medical advice. Class level only. BLOCK-1 caution: nothing here is a dosing or treatment statement.**
**WWOX evidence on autonomic function, SUDEP, the stress axis or hypoglycaemic counter-regulation: none.** Every item below is a substitute, labelled NOT WWOX evidence.

## Target

`disease-models/wwox/registries/claim_registry_current.md` · `CLAIM 031` (evidence-boundary addition only; status unchanged): a definitional note. No other claim. Five new paper-registry records (ESPANSIONE).

## What is missing now

CLAIM 031 lists status epilepticus (a documented cause of death in one WWOX series) and SUDEP risk among the reasons to keep seizure control. It does not say that by the standard definition SUDEP excludes status epilepticus, nor that no autonomic, CSF-monoamine or counter-regulatory measurement exists for any WWOX patient or Wwox-null animal in the repository records.

| Source | What it adds | Receipt |
|---|---|---|
| Bauer 2022 review (36686527) | SUDEP "excludes status epilepticus and cases where post-mortem examination or toxicology reveals another cause of death"; catecholamines appear as three hedged single sentences; genetic SUDEP mouse models are ion-channel genes; autonomic toolkit (ECG, plethysmography, telemetry) named | `FTR-20261019-36686527-01` |
| Wenker 2026 report (41584903) | epinephrine plus caffeine unmasks arrhythmia in Scn8a DEE13 mice (a provocation, sentence uncited); HPA-axis SUDEP mechanism rests on a 2021 review and a 2025 preprint; one citation mismatch; rabbit data unpublished | `FTR-20261019-41584903-01` |
| Sugiyama 2025 case report (40183510) | the nearest CSF monoamine panel in a DEE with a movement disorder: HVA and 5-HIAA low in both adults, MHPG (noradrenaline) low in one and normal in the other, never discussed; DAT SPECT normal; n of 2, medication confounders | `FTR-20261019-40183510-01` |
| Conlon 2020 case report (32905056) | a ketogenesis-defect toddler normoglycaemic during a severe febrile crisis, with no insulin, cortisol, catecholamine or free fatty acid result; mechanism called unclear | `FTR-20261019-32905056-01` |
| Holzen 2024 review (38397994) | counter-regulation in diabetic adults: epinephrine, glucagon and growth-hormone responses blunted after antecedent hypoglycaemia; brain glycogen said not to exist (disagrees with another review in the corpus); no neonatal or genetic content | `FTR-20261019-38397994-01` |

## Proposed addition to CLAIM 031 `Evidence boundary`

Append: "Definition note (wave 2026-10-19): by the standard definition (Bauer 2022 review, restating its sources) SUDEP excludes status epilepticus; a death in status epilepticus, as documented in one WWOX series, is therefore not SUDEP, and the two must be counted separately. No autonomic, ECG, respiratory, CSF monoamine or counter-regulatory measurement in a WWOX patient or Wwox-null animal is held in these records (term queries over those files, not a statement about the literature). `PREMISE_TAG`: the definition is the source review's statement of a consensus definition, not re-derived. `REVIVAL_TRIGGER`: a SUDEP-definition-compliant case in a WWOX series, or a monoamine or counter-regulatory panel in a WWOX model."

## Proposed discovery leads

1. **The measurement panel a WWOX hypoglycaemia or movement-disorder case would need** is: glucose with insulin, glucagon, epinephrine, growth hormone, cortisol, free fatty acids and ketones at the same time point (Holzen 2024, Conlon 2020), and CSF HVA, 5-HIAA, MHPG and 3-OMD with age-matched ranges (Sugiyama 2025). None exists in the repository records for WWOX (IPOTESI).
2. **Counter-regulation versus energy failure** in the Wwox-null mouse cannot be separated with a glucose value alone (Conlon 2020 shows normoglycaemia in a ketogenesis-defect crisis; IPOTESI).
3. **The WWOX adult case with respiratory decline and autonomic seizures (39507621, legacy-reconstructed only, artefacts absent from this checkout)** is the one WWOX-direct record that touches this axis; it is unread at primary depth in this checkout and is a reading debt, reported to the Orchestrator.

## Ordering

Receipts for the five PMIDs above must be in the ledger first.

### LOCATOR TRIPLES FOR BLIND AUDIT

| PMID | entry | proposition | verbatim snippet | anchor |
|---|---|---|---|---|
| 36686527 | entry 1 | DEFINITION: SUDEP excludes status epilepticus and deaths with another post-mortem cause, so a death in status epilepticus is not SUDEP by this definition. | SUDEP excludes status epilepticus and cases where post-mortem examination or toxicology reveals another cause of death | Epilepsy and SUDEP, paragraph 2 |
| 36686527 | entry 2 | SYMPATHETIC: the review gives one sentence that high sympathetic tone and several neuropeptides can follow seizures, with two cited sources and no quantity or timing. | High sympathetic tone and elevated levels of several neuropeptides can follow seizures | Control of autonomic functions in the brainstem and SUDEP, paragraph 3 |
| 36686527 | entry 7 | MODELS: developmental and epileptic encephalopathies are mentioned generically; the genetic SUDEP models tabulated are ion-channel genes (SCN1A, SCN1B, SCN8A, KCNA1, KCNH2, KCNQ1, CACNA1A) and no gene outside channelopathies is a  | Commonly SUDEP mouse models carry mutations in the Nav (1.1, 1.6) and Kv (1.1, 7.1, 11.1) genes | Model systems, paragraph 3 (after Table 1) |
| 41584903 | entry 1 | EPINEPHRINE AS A PROVOCATION IN A DEE MODEL: in Scn8a DEE13 mice resting ECG is normal but arrhythmias can be induced with epinephrine and caffeine to mimic an ictal sympathetic surge; this is a challenge test in a sodium-channel  | ECGs in these mice are normal at rest, but arrhythmias can be induced with epinephrine and caffeine to mimic an ictal sympathetic surge. | Cardiac Arrhythmias Due to Ion Channel Variants, paragraph 1 |
| 41584903 | entry 2 | HPA CLAIM: chronically epileptic mice with HPA axis dysfunction have more SUDEP, and chemogenetic or pharmacological suppression of HPA signalling prevented it; the cited source (ref 73) is a 2021 review of HPA targets in epilepsy | chemogenetic or pharmacological suppression of HPA signaling prevented the vulnerability to SUDEP | Stress, Seizures, HPA Axis Dysfunction, and Psychiatric Comorbidities in SUDEP Risk, parag |
| 41584903 | entry 3 | The reflex-hyperactivity mechanism is called established for the first time on the strength of ref 102, which is a 2025 preprint (bioRxiv identifier in the reference list). | This establishes for the first time a potential trigger for SUDEP and identifies HPA axis dysfunction as a novel pathophysiological mechanism contributing to SUDEP risk. | Potential Mechanisms Mediating HPA Axis Dysfunction and SUDEP Risk, last sentence |
| 41584903 | entry 5 | CITATION MISMATCH: the statement that SCN1B may not be a monogenic cause of Brugada syndrome carries ref 38, which in the reference list is a 1994 paper on EAG-related potassium channel genes in Drosophila and mammals. | However, other work suggests that SCN1B may not be a monogenic cause of BrS38. | Cardiac Arrhythmias Due to Ion Channel Variants, paragraph 2 |
| 40183510 | entry 1 | Table 2 reports four CSF analytes per case against the quoted reference range: HVA 36.6 and 79.3 against 145 to 324; 5-HIAA 20.4 and 52.2 against 67 to 140 nmol/L. | HVA (145–324 nmol/L18)36.679.35‐HIAA (67–140 nmol/L18)20.452.2 | Table 2, rows 1 and 2 |
| 40183510 | entry 2 | THE NORADRENALINE ARM IS IN THE TABLE AND NOT IN THE TEXT: CSF MHPG, the main central noradrenaline metabolite, is 27.7 in Case 1 (below the quoted 35 to 65) and 40.7 in Case 2 (inside it); the abstract, discussion and conclusion  | MHPG (35–65 nmol/L18)27.740.73‐OMD (<100 nmol/L18) | Table 2, row 3 |
| 40183510 | entry 4 | The authors assert the CSF results were reliable because no seizures or other confounders preceded sampling, although Case 2 had frequent seizures into adulthood and the interval from the last seizure and the medication state (val | No epileptic seizures and other causes that can affect the CSF results occurred before the examination; therefore, the measurement results were considered reliable. | Discussion, paragraph 3 |
| 40183510 | entry 7 | Figure 1 C and D show symmetric intense striatal uptake on the colour scale in both patients, consistent with the stated ratios; panels A and B are T1 MRI with non-specific atrophy per the caption. | [figure attestation - pixels cannot be quote-matched] Figure 1: panels A and B axial T1 MRI of Case 1 and Case 2; panels C and D DAT SPECT of Case 1 and Case 2, two bilat | Figure 1 A-D, native JPEG |
| 32905056 | entry 1 | GLYCAEMIA: the initial glucose was 4.6 mmol/L (3.3 to 5.6) before dextrose, after two days of vomiting and limited oral intake; glucose and serum ketone bodies are reported normal, with severe high anion gap acidosis. | Initial investigations indicated normoglycemia (blood glucose 4.6 mmol/L, reference range 3.3‐5.6) | Case presentation, paragraph 2 |
| 32905056 | entry 2 | The authors state the mechanism by which hypoglycaemia was averted is unclear; no counter-regulatory hormone or fuel measurement is reported anywhere in the article. | The mechanism by which hypoglycemia was averted remains unclear. | Discussion, paragraph 1 |
| 32905056 | entry 5 | Ketone paradox: marked ketonuria in a disorder of ketone synthesis; the authors suggest leucine-derived HMG-CoA and hypothesise, without testing, that the ketonuria may have been cerebroprotective. | We hypothesize that the extent of ketonuria in this case may have been cerebroprotective. | Discussion, paragraph 7 |
| 38397994 | entry 2 | COUNTER-REGULATION: epinephrine is one of the hormones whose release falls after recent antecedent hypoglycaemia; the review states that absence of symptoms reflects attenuation of the sympathoadrenal response. | The absence of symptoms of hypoglycemia reflects the attenuation of the sympathoadrenal response | 2.1 Autonomic Failure |
| 38397994 | entry 3 | The epinephrine statement is that after recent antecedent hypoglycaemia plasma epinephrine rises less; no value, no cohort and no time course are given in the review. | After recent antecedent hypoglycemia, epinephrine levels are significantly reduced (Figure 2) | 2.4 Hormonal Regulation, last paragraph |
| 38397994 | entry 4 | GLYCOGEN: the review states brain cells cannot store glucose as glycogen; astrocytes do hold glycogen, and another review in this corpus (a metabolic-batch reading of brain glycogen) treats it as a buffer; the sentence is a simpli | It is not possible for cells in the brain to synthesize glucose or to store it as glycogen. | 2.2 Altered Brain Glucose Sensing, paragraph 1 |


---

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261019_003` · 2026-10-20 · ACTOR_ID `orchestrator` (stated assumption, batch integrator)
**Working model:** WM_v7.21 -> WM_v7.22 (MINOR)
**Class re-judged (§7):** MINOR
**Blind locator audit:** not run — no baseline claim is narrowed and no MAJOR contingency is declared; the candidate's locator triples are carried for a later audit.
**What landed:** `PAPER 320`, `PAPER 321`, `PAPER 322`, `PAPER 323` with their LIT records; `CLAIM 031` evidence-boundary definition note (status unchanged); leads `DL-MECH-140` and `141`. Receipt identifiers: PMID 36686527 (`FTR-20261019-36686527-01`, DOI 10.3389/fneur.2022.1040648); PMID 41584903 (`FTR-20261019-41584903-01`, DOI 10.1177/15357597261416723); PMID 32905056 (`FTR-20261019-32905056-01`, DOI 10.1002/jmd2.12146); PMID 38397994 (`FTR-20261019-38397994-01`, DOI 10.3390/biomedicines12020391). The Sugiyama record already existed (`PAPER 299`). PARKED: the third lead (the adult WWOX case, now read at complete depth: see the GOLD-CLINICAL candidate).
**Status / Type / Summary:** unchanged by this candidate.
**Not medical advice.** Class level only; no individual-level record is carried.

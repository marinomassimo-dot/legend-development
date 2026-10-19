# COMMIT CANDIDATE — CC-20261019-SCIENTIST-B-H3-ADRENERGIC-SEIZURE-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-b`, interventions batch 2026-10-19 group H3, branch `task/INTERV-H3-B-20261019`.
**context_policy:** `SOURCE_FIRST` for every reading cited (first reads); registry comparison admitted after each first pass.
**target_wm_version:** `WM_v7.20_2026-10-04`. **Change class:** **MINOR** — new paper-registry records and evidence-boundary notes; no claim status, no baseline claim reversed, no working-model block change. The legend-locator-audit trigger is not met; the triples below are supplied for a later blind audit.
**Not medical advice. Class level only. BLOCK-1 caution: nothing here is a dosing or treatment statement.**
**WWOX evidence on adrenaline, noradrenaline or adrenergic receptors in seizures: none.** Every item below is a substitute, labelled NOT WWOX evidence.

## Target

No existing claim is edited. Proposed: five new paper-registry records (ESPANSIONE, background) and two discovery leads; one optional evidence-boundary note on the working model's silence about catecholamines (the working model and claim registry carry no adrenergic term).

## What is missing now

The registry holds no adrenergic record (term queries over adrenergic, epinephrine, noradrenaline, catecholamine, autonomic and sympathetic return nothing; SUDEP occurs in two records only as a reason to keep seizure control). The five readings below put one fact on record: the direction of an adrenergic manipulation on seizures or injury depends on receptor subtype, site, dose and system, and no system studied is a WWOX-deficient one.

| Source | System and manipulation | What it measured and what it did not | Receipt |
|---|---|---|---|
| Biagioni 2023 (35339181) | adult rat anterior piriform cortex, focal beta2 agonist (salbutamol) or antagonist (butoxamine) before bicuculline, 8 per group | agonist cut seizure incidence from 8 of 8 to 3 of 8 (abstract says "fully prevents"); antagonist raised severity; autophagy unmeasured; supplementary methods not retrieved | `FTR-20261019-35339181-01` |
| Sitnikova 2023 (38073616) | review of alpha2 agonists and antagonists in absence-epilepsy rats | alpha2 agonists lengthen spike-wave activity, antagonists shorten it; very high dose reverses; absence status provoked pharmacologically; claim rests on the author group own data | `FTR-20261019-38073616-01` |
| Sun 2024 (39505840) | adult male FVB mice, kainic acid status, propranolol plus prazosin plus atipamezole blockade, one or three doses | acute blockade lengthened each seizure (115 to 204 s) while lowering mortality and later seizure counts; hippocampal glymphatic flow not improved; causality via glymphatic flow undemonstrated; reviewers said the same | `FTR-20261019-39505840-01` |
| Dhillon 2026 (41885587) | preterm fetal sheep, alpha blockade (phentolamine) after hypoxia-ischaemia | seizures unchanged; post-insult lactate and glucose lower; blood-pressure variability rise abolished; harm to injury cited from earlier work, not measured here; reported sensitivity and specificity swapped against Figure 10 | `FTR-20261019-41885587-01` |
| Li 2026 (41169199) | review of beta2 agonists in Alzheimer disease | each subtype (alpha1, alpha2, beta1, beta2) has protective and harmful evidence; beta2 knockout rescue cited as support; clinical beta2 agonists barely enter the brain; conclusion claims reversal on preclinical evidence | `FTR-20261019-41169199-01` |

## Proposed paper-registry records (all ESPANSIONE; negatives in the Note)

One record per source above carrying its Note: "no WWOX content; adrenergic direction depends on receptor subtype, site and system; see commit candidate". Receipts must be recorded first.

## Proposed discovery leads

1. **The class label "adrenergic" has no direction.** Across five readings each in a different system the same receptor family is beneficial (beta2 agonist in rat piriform cortex; blockade in adult mouse chronic seizures), harmful (alpha2 agonists in absence rats; alpha blockade in the injured preterm brain, cited) or both within one paper (Li 2026). For WWOX the first question is therefore which receptor and which tissue, not whether adrenaline helps (INFERENZA from DATO as printed).
2. **A post-injury adrenergic effect on lactate and glucose in a developing brain model exists** (Dhillon 2026, Table 1: lactate 4.1 against 1.6 mmol/L at 2 h with alpha blockade); it is the only measured adrenergic effect on a metabolic readout in this wave (ESPANSIONE; no WWOX link).
3. **No WWOX tissue has any adrenergic readout in the repository records** (null result of term queries; an empty result is not evidence about the literature). A Wwox-null measurement of monoamines (CSF or brain HVA, MHPG, 5-HIAA, 3-OMD) would be the cheapest first datum; the template is in the Dravet case report (40183510, see the autonomic candidate).

## Ordering

Receipts for the five PMIDs above (staged under `receipt_staging/scientist-b/`) must be in the ledger first.

### LOCATOR TRIPLES FOR BLIND AUDIT

| PMID | entry | proposition | verbatim snippet | anchor |
|---|---|---|---|---|
| 35339181 | entry 1 | The abstract says salbutamol FULLY prevents limbic seizures; the figure caption gives 3 of 8 rats (37.5 percent) still seizing after salbutamol plus bicuculline, so prevention was complete in 5 of 8. | Butox=0%, N=0/8; Salbut+Bic= 37.5%, N=3/8; Butox + Bic=100%, N=8/8 | Figure 1 caption |
| 35339181 | entry 2 | Figure 1 shows the incidence bars: bicuculline 100, salbutamol alone 0, butoxamine alone 0, salbutamol plus bicuculline about 37, butoxamine plus bicuculline 100, triple 100; the incidence ceiling of 100 percent in the control mea | [figure attestation - pixels cannot be quote-matched] Figure 1 bars of percent of rats with seizures: Bic 100, Salbut 0, Butox 0, Salbut+Bic about 37 with asterisk, Butox | Figure 1, native JPEG |
| 38073616 | entry 1 | SIGN: alpha2 agonists increase spike-wave activity in genetically prone rats; antagonists suppress it. The direction of an adrenergic manipulation on seizures therefore depends on receptor subtype and site, and the same review not | Antagonists of alpha2-ARs, in contrast, suppress SWDs (Table 1) putatively via an indirect effect on vigilance | Section 4, paragraph 2 |
| 38073616 | entry 2 | DOSE: the absence-status state is produced by low doses; a very high dose reverses the effect (a decrease in SWDs and deep sedation), so the dose-response is non-monotonic. | Low doses of dexmedetomidine caused a pro-absence effect in rats, whereas high doses caused a reduction in SWDs and deep sedation | Section 2, paragraph after Table 1 |
| 39505840 | entry 1 | In the acute status epilepticus the blockade prolonged individual convulsive seizures and the interval between them and the duration of phase 1 without changing the number of seizures; the abstract speaks of reduced severity. | PPA treatment significantly prolonged the duration of individual seizures, the interval between seizures, and the duration of phase 1, but not the total number of seizure | Results, Pan-adrenergic inhibition delays and shortens KA-induced status epilepticus |
| 39505840 | entry 2 | Table 1 gives the acute numbers: seizure duration 115.0 against 204.2 s (P < 0.001), interval 8.2 against 20.3 min, and the total duration of phase 1 plus phase 2 26.1 against 19.9 h (P = 0.265, not significant). | Duration of Phase 1 + Phase 226.1 ± 4.2 h19.9 ± 2.0 h0.265 | Table 1, last row |
| 39505840 | entry 7 | LOCUS: the glymphatic gain was not significant in the hippocampus, the region of the kainic acid focus; the authors attribute it to gliosis and to a tracer protocol not optimised for the hippocampus. | even though we did not find significant glymphatic enhancement in the hippocampus (Fig. 5C,I) | Discussion, Epileptogenesis and the partial rescue |
| 41885587 | entry 3 | SEIZURES: alpha blockade did not change seizure onset, time with seizures, burden, amplitude, duration or count; the onset means differ (13.3 against 7.3 h) with wide spread. | There was no difference between the occlusion groups in the average onset time (HI‐saline 13.3 ± 9.2 h; HI‐phentolamine 7.3 ± 2.4 h) | Results, Post-occlusion neurophysiological and EMG recovery |
| 41885587 | entry 8 | BIOMARKER CLAIM: a threshold one standard deviation above the baseline coefficient of variation, set in the primary group and applied by a blinded observer to a 10 plus 10 validation group, is reported as 90 percent sensitivity an | Applying this set threshold, in the validation dataset animals with severe HI were identified with 90% sensitivity and 80% specificity (Fig. 10). | Results, Viability of short BPV as a biomarker for severe HI |
| 41885587 | entry 9 | Figure 10 enlarged: of 10 occluded fetuses, 8 lie above the dashed threshold at about 0.043 and 2 below; of 10 sham fetuses, 1 lies above and 9 below; this gives sensitivity 8 of 10 (95 percent exact interval 44 to 97 percent) and | [figure attestation - pixels cannot be quote-matched] Figure 10 scatter of 3-hourly systolic CoV: Sham-HI ten black dots with one at about 0.047 above the dashed line nea | Figure 10 (file g011), native JPEG enlarged three times |
| 41169199 | entry 4 | CONTRADICTION IN THE INTRODUCTION: knockout of the beta2 receptor gene rescued pathology in a mouse model, and the review cites this as support for an agonist strategy. | Furthermore, ablation of the β2-AR gene rescued pathological features of senile PS1/APP mice, indicating that β2-AR is an attractive target for therapeutic purposes for t | Introduction, paragraph 4 |
| 41169199 | entry 5 | BIVALENT SIGNAL: amyloid binding to the beta2 receptor hyperactivates PKA, raises AMPA receptor activity and calcium influx and leads to excitotoxic death, while the same cAMP-PKA axis is presented as neuroprotective; the review c | These results highlight the bivalent nature of Aβ action on β2-AR signaling and its involvement in AD progression. | Loss of noradrenergic tone and beta2 dysfunction, last paragraph |
| 41169199 | entry 6 | ALPHA-2: the review says selective alpha2 agonists confer neuroprotection and also that alpha2A activation increases amyloid-beta production and alpha2B deletion enhances memory. | α2-ARs also have a dual role in AD. Whereas α2b-AR deletion is associated with enhanced memory and reduced AD risk, activation of α2A-AR increases production of Aβ | Alpha-adrenergic receptors, paragraph 4 |

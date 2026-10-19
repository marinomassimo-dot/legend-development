# COMMIT CANDIDATE — CC-20261019-SCIENTIST-B-G2-KD-PRIOR-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-b`, metabolic batch 2026-10-19 group G2, branch `task/METAB-G2-B-20261019`.
**context_policy:** `SOURCE_FIRST` for every reading cited (first reads); registry comparison admitted after each first pass.
**target_wm_version:** `WM_v7.20_2026-10-04`. **Change class:** **MINOR** — new paper-registry records and evidence-boundary notes; no claim status, no baseline claim reversed, no working-model block change. The legend-locator-audit trigger is therefore not met; the triples below are supplied for a later blind audit.
**Not medical advice.**

## Target

`disease-models/wwox/registries/claim_registry_current.md` · `CLAIM 042` (evidence-boundary addition only; status stays `in observation`), and eight new paper-registry records. No working-model block is changed.

## What is missing now

CLAIM 042 states three of five WOREE patients responded to a ketogenic diet, denominator not stated, no Q230P carrier among responders. It has no base rate and no statement of how far response identifies a mechanism. Three readings of this wave supply both.

| Source | What it adds | Receipt |
|---|---|---|
| Hu 2025 review (40831798) | Responder fractions at the 50 percent threshold across DEE syndromes and genes: 47 percent (Lennox-Gastaut, n 189), 47 to 63 percent (Dravet, attrition), spasm cessation 23 of 43 (infantile spasms), 77.8 to 100 percent in four genes from one study with n 18, 6, 4, 3, CDKL5 0 of 10; KD used after multiple drugs and surgery (pre-selected); hypoglycaemia at initiation named as common early adverse effect; WWOX absent | `FTR-20261019-40831798-01` |
| Klepper 2026 cohort (41830506) | In the one disease with a known, bypassable fuel defect (Glut1DS), 61 percent of 44 epileptic patients respond on KDT monotherapy; at least 10 of the 17 non-responders were initially responsive (secondary failure), seven never responded; no covariate explains response; "23 percent of non-responders" is arithmetically 10 of 44; abstract EEG counts are the persisting counts | `FTR-20261019-41830506-01` |
| Joshi 2025 model (40659031) | In silico ketone rescue works only upstream of acetyl-CoA (glucose supply, GLUT1, PDH) and fails for MCT1 and complex I; the "primary mechanism" conclusion is untested because no competing mechanism is in the model; its complex I prediction disagrees with the clinic | `FTR-20261019-40659031-01` |

## Proposed addition to CLAIM 042 `Evidence boundary`

Append: "Base-rate context (wave 2026-10-19): across DEE syndromes and genes KD responder fractions at the 50 percent threshold are reported at roughly 47 to 100 percent in small, refractory-pre-selected cohorts (Hu 2025 review, restating its primaries), and in Glut1 deficiency, where the lesion is a known bypassable fuel shortage, 39 percent of epileptic patients are not controlled by KD alone, with secondary loss of response in at least ten of 44 (Klepper 2026). A WOREE response count with an unstated denominator is therefore not distinguishable from the DEE base rate and does not identify an energy lesion in either direction. `PREMISE_TAG`: the statement rests on the two cited readings (DATO as printed) and on CLAIM 042's own caveat. `REVIVAL_TRIGGER`: a WOREE or WWOX-DEE series with the exposed denominator, a defined response and a matched DEE comparator, or brain energy measurement paired with response."

## Proposed new paper-registry records (all ESPANSIONE; negatives carried in the Note)

- Pain 2026 (42047543): one undifferentiated Glut1DS iPSC line, three replicates, transcripts only, 11,271 genes changed; glycolytic genes mixed in direction against a text that says reduced; AMPK stated up in Results 3.1 and down in 3.3; adenosine inference ignores NT5E falling; sponsor-linked. Receipt `FTR-20261019-42047543-01`.
- Kuang 2024 review (39876842): post-stroke lactate/lactylation/HDAC hypothesis, authors state evidence for direct causation insufficient; one integrity-flagged reference declared citation-only. Receipt `FTR-20261019-39876842-01`.
- Fei 2020 review (33363507): metabolic control of epilepsy carries two opposite directions (inhibit glycolysis; supply energy in hypometabolic states). Receipt `FTR-20261019-33363507-01`.
- Beltran-Velasco 2025 review (39997753): glycogen as hypoglycaemic buffer stated generally; no WWOX; GSK-3 beta once; epilepsy section points to accumulation; synthase-inhibitor sentence self-contradictory. Receipt `FTR-20261019-39997753-01`.
- Cornelio-Martinez 2026 review (42171828): HIF-1 alpha inhibitor protective at 0.5 h and harmful at 8 h after MCAO; opposing roles by cell type. Receipt `FTR-20261019-42171828-01`.

## Proposed discovery leads

1. **Sign of the metabolic target.** The metabolic-control literature supports both inhibiting glycolysis and supplying energy (Fei 2020); for WWOX loss the fibroblast lesion (lactate up) and the Wwox-null mouse (hypoglycaemic) point in different directions, so the sign must be fixed by a brain measurement before any dietary rationale is chosen (INFERENZA).
2. **KD response does not identify mechanism** (Klepper 2026 plus Hu 2025; INFERENZA).
3. **Timing reverses the sign of HIF1A intervention** in hypoxic brain (Cornelio-Martinez 2026, restating primaries; ESPANSIONE).

## Ordering

Receipts for the eight PMIDs above (staged under `receipt_staging/scientist-b/`) must be in the ledger first.

### LOCATOR TRIPLES FOR BLIND AUDIT

| PMID | entry | proposition | verbatim snippet | anchor |
|---|---|---|---|---|
| 40831798 | entry 1 | The gene-wise responder rates the review gives (SCN1A, KCNQ2, STXBP1, SCN2A) come from very small cohorts, a single study (its ref 9) behind all four, with n of 18, 6, 4 and 3. | STXBP1 (n = 4, responder rate = 100.0%, p = 0.01) | 5.6 DEE associated with other genetic mutations |
| 40831798 | entry 2 | The one gene-level negative: CDKL5-related DEE, 0 of 10 responders in the same small study, and a registry of 104 with improvement in 61 of the 69 who changed but poor long-term efficacy. KD response is therefore heterogeneous by  | one small study reported no significant response (n = 10, responder rate = 0.0%, p = 0.031) | 5.6 |
| 40831798 | entry 4 | Syndrome-level prior for Dravet syndrome with attrition: the 50 percent responder fraction falls from 63 to 47 percent between 3 and 12 months. | seizure reduction ≥50% was observed in 63%, 60%, and 47% of patients at 3, 6, and 12 months, respectively | 5.2 Ds |
| 40831798 | entry 6 | The Outlook states KD reduces or controls seizures in "most" DEE cases, a sentence stronger than the syndrome figures the review itself gives (47 to 63 percent responder fractions at the 50 percent threshold) and silent on how res | KD not only reduces or controls seizures in most DEE cases | 7 Outlook |
| 40831798 | entry 10 | HYPOGLYCAEMIA AT INITIATION: hypoglycaemia and dehydration are named as common early adverse effects, related to fasting and reduced intake. | Common early adverse effects of KD include hypoglycemia and dehydration, typically related to fasting and reduced caloric intake | 6 Safety and tolerability |
| 41830506 | entry 5 | Figure 3: the non-responder group is not one group. Panel A (six patients) and panel C (four) show white KDT-monotherapy bars before ASM was added, with the legend saying they were initially responsive; panels B and D (seven) neve | [figure attestation - pixels cannot be quote-matched] Figure 3, horizontal bars per patient against age 0 to 25 years: white KDT monotherapy, grey KDT plus ASM with response, black KDT plus ASM withou | Figure 3 panels A to D, native JPEG |
| 41830506 | entry 7 | ARITHMETIC: KDT plus ASM is said to be effective in 23 percent of non-responders; 10 of 17 non-responders is 59 percent, and 23 percent is 10 of all 44 patients. | KDT plus ASM was effective in 23% of non‐responders to KDT monotherapy | Discussion 4.1 |
| 41830506 | entry 8 | Figure 5: epileptic discharges fall from 15 to 5 patients in responders and from 14 to 9 in non-responders; background slowing 4 to 0 in responders, 4 to 4 in non-responders. The bars give the numbers still present on KDT. The Abs | [figure attestation - pixels cannot be quote-matched] Figure 5, (A) responders and (B) non-responders: grey bars epileptic discharges before and on KDT (15, 5 and 14, 9), white bars background slowing | Figure 5A and 5B, native JPEG |
| 40659031 | entry 4 | Figure 3a: the whole regime change is a swing of the presynaptic ATP generation rate across a dashed threshold near 1.17 x 10^6 molecules per second, against about 1.34 at baseline glucose 5 mM, a difference of roughly 13 percent. | [figure attestation - pixels cannot be quote-matched] Figure 3, (a) ATP generation rate (10^6 molecules/s) against blood glucose 2.5 to 5 mM for beta-hydroxybutyrate 0.25 mM (blue) and 2 mM (red) with | Figure 3a and 3b, native JPEG |
| 40659031 | entry 10 | THE MODEL DISAGREES WITH THE CLINIC on the one case where it can be checked: a clinical series reports ketogenic diet effective in all eight studied complex I patients, whereas the model predicts no rescue; the authors explain thi | another group found that the ketogenic diet was effective for all of their studied patients with complex I deficiency | Discussion 4.2 |
| 40659031 | entry 14 | Competing mechanisms (gene expression, inflammation, astrocyte function, circadian, microbiota) are discussed but are NOT in the model; the model can therefore show that energy repletion is sufficient in silico, not that it is pri | It is also likely the case that the ketogenic diet has multiple diverse effects on the brain and body | Discussion 4.3 |
| 42047543 | entry 4 | The KEGG paragraph says DA-containing treatments upregulated mTOR and AMPK signalling. | DA‐containing treatments upregulated energy metabolism (TCA cycle and oxidative phosphorylation), mTOR and AMPK signaling, an | Results 3.1 |
| 42047543 | entry 5 | Results 3.3 says AMPK subunit transcripts fall (PRKAA2 down 46 percent), the opposite direction to the 3.1 pathway statement on AMPK signalling. | DA:OA treatment also reduced nutrient sensor AMPK subunit expression (PRKAA2 46%; PRKAB1/2/G1 by 12%/36%/22%), a complex whic | Results 3.3 |
| 42047543 | entry 7 | Figure 1 panels H and I show most glycolytic genes UP with DA:OA and DA (HK2, ALDOA, GPI, TPI1, GAPDH, ENO1, PGK1, PKM, LDHA, SLC16A1 all positive, log2 fold change about 0.1 to 0.5) and down for HK1, HK4, PFKP, SLC2A1, SLC2A3, LD | [figure attestation - pixels cannot be quote-matched] Figure 1, (F) glucose metabolism schematic, (G) heatmap of glucose transport and glycolysis genes for DA, OA, DA:OA, (H and I) bar plots of log2 f | Figure 1G, 1H and 1I, native JPEG |
| 42047543 | entry 9 | The adenosine inference rests on ADA falling; the same paragraph shows NT5E (a source of adenosine) falling 63 percent, so the net adenosine direction is not determined by the transcripts. | However, both treatments reduce 5′‐nucleotidase (NT5E by 63%) expression, where this enzyme can hydrolyze adenosine monophosphates | Results 3.3 |
| 39876842 | entry 2 | The authors state the evidence that lactylation directly causes epilepsy is insufficient. | Currently, there is insufficient evidence to confirm that protein lactylation directly induces epilepsy by regulating neuronal excitabi | Section 2 |
| 33363507 | entry 0 | DIRECTION A: the review supports inhibiting glycolysis (2-DG, KATP opening, BDNF/TrkB, PPP and neurosteroid routes) as antiseizure. | glycolysis inhibition, such as by 2-DG, is a promising treatment for epilepsy [(107, 108)]. Targetin | Control of Epilepsy by Regulating Metabolic Pathways, glycolysis |
| 33363507 | entry 1 | DIRECTION B: the same review states hypometabolism (hypoglycaemia, GLUT1 deficiency, mitochondrial dysfunction) can initiate seizures and energy supplementation treats them; the metabolic-control statement therefore has two opposi | Hypometabolism could initiate convulsions or epilepsy, such as hypoglycemia, GLUT1 deficiency, and mitochondrial dysfunction. Supplementing neuronal e | Conclusion |
| 39997753 | entry 2 | EPILEPSY: the review states glycogen accumulation in astrocytes may contribute to hyperexcitability in refractory epilepsy, the opposite direction to a glycogen buffer deficit. | However, recent research suggests that abnormal glycogen accumulation in astrocytes may contribute to the excessive neuronal excitability ob | 5.1 Epilepsy |
| 39997753 | entry 4 | GSK-3 beta appears once in the whole article, as a small-molecule target in neurodegeneration models; the review does not link GSK3B or glycogen to WWOX. | Innovative small molecules targeting enzymes such as GSK-3β, which are involved in glycogen regulation, have also demonstrated efficacy in p | 7.2 Gene Therapies and Innovative Molecules |
| 42171828 | entry 1 | TIMING: a HIF-1 alpha inhibitor given 0.5 h after MCAO reduced apoptosis and infarct size. | administration of 2-methoxyestradiol (2ME2), a HIF-1α inhibitor, at 0.5 h after MCAO-induced hypoxia significantly reduced cell apoptosis  | Dual and time-dependent actions |
| 42171828 | entry 2 | The same inhibitor given 8 h after MCAO increased apoptosis and neuron loss: the sign of a HIF-1 alpha intervention reverses with timing. | Conversely, later administration of 2ME2, 8 h after MCAO, induced greater cell apoptosis and reduced the number of NeuN+ neurons.  | Dual and time-dependent actions |
| 42171828 | entry 3 | Summary statement: acute-phase HIF-1 alpha upregulation harms and late-phase upregulation protects; the acute and late phases are hours apart (4 to 8 h versus 48 to 72 h). | acute-phase upregulation of HIF-1α induces neuronal loss, behavioral deficits, and animal death, while late-phase upregulation of HIF-1α mediates neuronal prote | Dual and time-dependent actions |

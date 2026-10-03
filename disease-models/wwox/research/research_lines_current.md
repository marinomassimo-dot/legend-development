# RESEARCH LINES — Legend
**Version:** v1.2
**Date baseline:** 2026-04-10
**Status:** post-bootstrap / Commit 181–220 updated — new active lines added

---

## Scope
Register of active research lines that emerged from LEGEND after the bootstrap of the first 180 papers.

---

## RL-001 — Neuronal hub → hyperexcitability + myelination failure
**Status:** central / consolidating
**Primary pathway:** P1 + P4
**Evidence base:** papers 87, 48, 163, 93; meta_network_myelin_glia
**Clinical relevance:** HIGH
**Reason active:** the most solid line in the system; connects network, myelin and neuronal rescue
**Next action:** keep as the central axis of the working model

---

## RL-003 — WWOX as bioenergetic governor (AMPK–HIF1A–mitochondria)
**Status:** high-priority consolidating
**Primary pathway:** P5
**Evidence base:** papers 2, 39, 64, 144; meta_metabolism
**Clinical relevance:** HIGH conceptual / MODERATE operational
**Reason active:** plausible amplifier axis of neuronal and myelin vulnerability
**Next action:** look for CNS-specific data and useful metabolic biomarkers

---

## RL-007 — Prenatal cortical development / migration axis
**Status:** central / consolidating
**Primary pathway:** P3
**Evidence base:** papers 97, 93, 163, 106, 87; meta_prenatal_structure
**Clinical relevance:** HIGH
**Reason active:** one of the main structural shifts of the model; now supports a pre-wired substrate including migration, cortical layering, maturation and bridge to myelination/glial development
**Next action:** maintain as central axis; future refinement only if new human prenatal data emerge

---

## RL-008 — WWOX → GSK3β seizure axis
**Status:** emerging high-value
**Primary pathway:** emerging node / seizure susceptibility
**Evidence base:** paper 93; meta_prenatal_structure
**Clinical relevance:** MODERATE
**Reason active:** promising mechanistic node, now best interpreted as amplifier of a structurally vulnerable system rather than standalone upstream driver
**Next action:** verify robustness with additional convergent papers; keep non-operative clinically

---

## RL-GABA-001 — Developmental GABA dysregulation
**Status:** emerging high-value
**Primary pathway:** P2
**Evidence base:** papers 85, 87, 53, Steinberg organoids; meta_gaba_paradox
**Clinical relevance:** HIGH
**Reason active:** a high-value strategic dossier with high risk of oversimplification
**Next action:** look for NKCC1/KCC2 data and patch-clamp physiology

---

## RL-GABA-002 — GABA depolarization hypothesis
**Status:** high-interest / unresolved
**Primary pathway:** P2 / bridge chloride gradient
**Evidence base:** Steinberg organoids + developmental convergence
**Clinical relevance:** MODERATE-HIGH
**Reason active:** a possible interpretive key to the GABA paradox
**Next action:** run the specified decisive experiment of `CC-20260826-EGABA-EXPERIMENT-01` — gramicidin-perforated-patch measurement of the sign and driving force of GABA in WWOX LoF. The corpus contains **zero measurements of the sign of GABA in any WWOX model** (`E_GABA`, *reversal potential* and *gramicidin* each occur 0 times across `meta_gaba_paradox_current.md`), so searching for further published chloride-gradient data cannot close this line.
**Pre-specified test (`CC-20260826-EGABA-ANALYSIS-PLAN-01`):** `PRIMARY_ENDPOINT` = **`DF_GABA` = `E_GABA` − `V_rest`**, in millivolts, measured per neuron by gramicidin-perforated patch, at **P14–P16**; pre-specified contrast `Wwox^−/−` versus littermate `Wwox^+/+`, **at P14–P16 only**, every other window and genotype secondary and reported as such. Not `E_GABA` alone, which is uninterpretable without `V_rest` from the same recording. The plan's resource map shares a breeding cohort with the P7–P21 video-EEG design but **forces two sub-cohorts, not one** (§9): Arm A pairs network output and cellular state within one animal, Arm B gives the surgery-free developmental trajectory, and Arm B runs first as the decision gate.
**Closure conditions (`CC-20260826-EGABA-CLOSURE-01`):** the truth table has two axes only — `DF_GABA` and mIPSC amplitude/frequency. `DF_GABA` normal + mIPSC normal ⇒ **NEITHER** (GABAergic transmission is not the lesion at this age and cell type); `DF_GABA` normal + mIPSC reduced ⇒ **M1 alone** (weak inhibition); `DF_GABA` shifted positive + mIPSC normal ⇒ **M2 alone** (depolarizing GABA); both ⇒ **BOTH**, where *order of correction matters: raising GABAergic tone before fixing the gradient could worsen*. **Both mIPSC arms must be recorded in the same cell, before and after TTX**, or the design can return «M1 absent» while the best-documented inhibitory abnormality in this corpus sits in the term TTX removes. A null that fails its positive control, its power declaration or its attrition report is `NOT_TESTED`, never `NOT_DIFFERENT`. **No `n` is proposed** — none is derivable; the pilot produces the variance inputs. Neither candidate changes this line's status, which stays `high-interest / unresolved` until data exist.

---

## RL-HUM-001 — Human natural history / trajectory model
**Status:** active high-value
**Primary pathway:** human spectrum / natural history
**Evidence base:** papers 30, 118, 180, Oliver 2023, Teplyshova 2024, broader case literature
**Clinical relevance:** HIGH
**Reason active:** needed to model trajectory, survival and longitudinal expectation-setting without collapsing all WWOX cases into one profile
**Next action:** continue integrating human cohort and long-follow-up data; keep distinct from mechanistic animal lines


## RL-HUM-002 — Genotype → severity / survival gradient
**Status:** active high-value
**Primary pathway:** genotype-phenotype / counseling / survival
**Evidence base:** Oliver 2023, Piard 2019 abstract-supported, cohort/case aggregation
**Clinical relevance:** HIGH
**Reason active:** directly informs interpreting a case as likely N/M rather than N/N and structures prognosis with caution
**Next action:** strengthen with any additional human genotype-stratified cohorts; avoid over-reading individual case reports


## RL-NEUROINF-001 — Neuroinflammation / glia progression
**Status:** emerging
**Primary pathway:** P6
**Evidence base:** papers 53, 85, Obeid 2026 contextual
**Clinical relevance:** MODERATE
**Reason active:** a real axis but probably downstream/amplifier rather than a universal driver
**Next action:** decide whether to promote it to a standalone meta
**Note (BATCH_20260926_ALDAZ, 2026-09-26):** the "progression" leg of this line rests on `CLAIM 006`, now narrowed: astrogliosis progresses; microglial progression is shown for morphology only and abundance progression is untested; two time points and pseudoreplicated statistics (n = 3 mice) give a direction, not a rate.

---

## RL-NET-001 — Network hyperexcitability and oscillatory disorganization
**Status:** active / high priority
**Primary pathway:** P1
**Evidence base:** paper 210 (corpus 181–220); CLAIM 021; convergenza con RL-001
**Clinical relevance:** HIGH
**Reason active:** WWOX loss appears to destabilize neocortical network physiology through combined intrinsic and synaptic mechanisms — bursting, oscillatory disorganization, phase-amplitude coupling, reduced inhibition, rebound-prone firing. This elevates network-state pathology to core-pathway status, distinct from epileptiform hyperexcitability alone.
**Next action:** look for qEEG / oscillatory-metric data in WWOX-DEE; link with RC-010

---

## RL-MET-002 — WWOX/HIF1A systems-state metabolism
**Status:** active / high priority
**Primary pathway:** P5
**Evidence base:** paper 191 (WWOX/HIF1A ratio in GDM leukocytes); PAPER 032 (interactome and pathway annotation), PAPER 103 (VOPP1 interaction only); CLAIM 025; CLAIM 026; convergenza con RL-003
**Clinical relevance:** HIGH conceptual / MODERATE operational
**Reason active:** The WWOX/HIF1A axis remains a state-level research marker. Separately, trafficking-protein co-association and metabolic annotation motivate a test of functional coupling; no interface or Acetyl-CoA flux has been measured.
**Next action:** expand meta_metabolism; look for CNS-specific data; link with RC-007

---

## RL-PREN-002 — Prenatal developmental architecture in null-severe disease
**Status:** active
**Primary pathway:** P3 / prenatal arch
**Evidence base:** paper 216 (caso fetale umano null-severe); CLAIM 022; convergenza con RL-007
**Clinical relevance:** HIGH for the framework / INDIRECT for an N/M case
**Reason active:** Severe null phenotypes may begin in utero. Developmental-timing-aware interpretation is now supported by a direct human case, not only animal models.
**Next action:** keep as an active line; update only if further human prenatal data emerge

---

## RL-ARCH-001 — Test trafficking–metabolism coupling
**Status:** active exploration / high-priority candidate
**Primary pathway:** P5 / endomembrane systems
**Evidence base:** PAPER 032 (WWOX interactome and pathway annotation); PAPER 103 (independent VOPP1 interaction); CLAIM 026
**Clinical relevance:** LOW — research hypothesis only
**Reason active:** A single HEK293T prey list suggests testable trafficking and metabolic leads. Their functional coupling, neuronal transfer and relevance to myelin or synapses remain unmeasured.
**Next action:** link with RC-007; look for WWOX + organelle data in neurons/glia

---

## RL-ECM-001 — ECM / HYAL-2 / WWOX / SMAD injury-response signaling
**Status:** exploratory / high-value
**Primary pathway:** ECM / membrane signaling / injury response
**Evidence base:** paper 214 (HYAL-2/WWOX/SMAD4); CLAIM 027
**Clinical relevance:** INDIRECT
**Reason active:** Suggests an ECM/membrane-to-nucleus role for WWOX with possible relevance to injury response and maladaptive tissue remodeling in the CNS. Not yet anchored to direct CNS/pediatric data.
**Next action:** link with RC-008; look for WWOX/HYAL-2 data in CNS or developmental biology

---

## RL-BIOM-001 — WWOX functional-state biomarkers
**Status:** active framework / candidates not yet populated
**Primary pathway:** direct WWOX state and proximal mechanistic readouts
**Evidence base:** CLAIM 019; public expression resources; [`biomarker_candidates_current.md`](../biomarker_endpoint/biomarker_candidates_current.md)
**Clinical relevance:** HIGH strategic / NOT clinically validated
**Reason active:** target engagement and functional rescue cannot be inferred from distal clinical endpoints alone. The line keeps direct WWOX abundance, transcript/splicing and function distinct from candidate proximal-pathway readouts.
**Next action:** populate candidates only through the scored biomarker workflow; require direct validation before calling any candidate a validated biomarker.

---

## RL-GT-001 — Gene therapy design principles
**Status:** emerging → consolidating
**Primary pathway:** P7
**Evidence base:** Repudi 2021 EMBO, Obeid 2026, Steinberg 2024
**Clinical relevance:** HIGH strategic
**Reason active:** the most important trial-readiness axis in the long term
**Next action:** create meta_gene_therapy_current.md

**Version update:** v1.3 — 2026-07-25 (integrity repair: restored the previously referenced RL-BIOM-001 record)

## RL-C-20261003w4a — Is AAV dorsal-root-ganglion toxicity immune-preventable or dose-intrinsic? An open question with two primate datasets on opposite sides

**Status:** open
**Tag:** `INFERENZA`
**Opened:** 2026-10-03 (`CC-20261003w4-C-DRG-CONTRADICTION-01`, propagated by `BATCH_20261003_003`)
**Sources:** PMID 41404412 ([[paper_registry_current#PAPER 162]], `FTR-20261003-41404412-01`) · PMID 35331006 ([[paper_registry_current#PAPER 163]], `FTR-20261003-35331006-01`) · PMID 36700120 ([[paper_registry_current#PAPER 164]], `FTR-20261003-36700120-01`). All three `partial_fulltext_read`. **None of the three mentions WWOX.**
**Provenance:** Authored by `BATCH_20261003_003` from the op specification of `CC-20261003w4-C-DRG-CONTRADICTION-01` (intake wave 4 2026-10-03, Scientist C), whose ops were a prose specification; the record text below is the integrator's, the substance and every figure are the candidate's. `context_policy: SOURCE_FIRST`. **Not medical advice.**

**The question.** Two regulatory-grade primate datasets disagree about whether AAV-mediated DRG toxicity can be prevented by immunosuppression — one reduced it across three different cargos, the other could not reduce it even under complete B-cell depletion — and the disagreement **cannot be resolved from either source**.

**Why it is carried open rather than settled.** The two outcomes imply opposite risk-mitigation plans for any neuron-targeted AAV. If the immune mechanism holds, the dominant class toxicity of a CNS AAV has a clinically feasible prophylaxis, and the plan is a defined peri-dosing immunosuppression protocol with a duration (the source predicts at least six months) and its own paediatric risk assessment. If the transduction/expression mechanism holds, immunosuppression buys nothing and the only levers are dose, promoter strength and tissue de-targeting. A third possibility is that both are true of different components: the earliest events of the one source are explicitly uncorrelated with transgene level, while its later events correlate with it, which the authors themselves read as two distinct mechanisms.

| Axis | PMID 41404412 (Grubor 2025, Biogen) | PMID 35331006 (Tukov 2022, Novartis) |
|---|---|---|
| Species / age | Cynomolgus macaque, 2–4 y and 2–3 y | Cynomolgus macaque, 13–19 mo and 25–34 mo (Mauritius origin) |
| Vector / cargo | AAVhu68-ss-coSMN1; AAV9-hGBA1; **AAV9-mir-SOD1, a non-protein cargo** | scAAV9 onasemnogene abeparvovec (CMV enhancer / chicken-β-actin, human *SMN*), one cargo |
| Dose | 3.68 / 3.5 / 3.0 / 4.0 × 10¹³ GC per animal, one dose per study | 1.2 / 3.0 / 6.0 × 10¹³ vg per animal as a series; mitigation arm fixed at 3.0 × 10¹³ |
| Route | ICM (three studies), IT lumbar (one); **no contrast agent** | IT lumbar, **0.20 mL iohexol immediately before the vector**; plus an intravenous arm |
| Regimen | Dexamethasone 0.5 mpk SID + **tacrolimus 1 mpk SID (calcineurin inhibitor)** ± MMF; from day −2 / −3, but **day 2** in the first study | Prednisolone 1 mg/kg/day from day −1; or rituximab 20 mg/kg q2w from day −14 + everolimus to day 14. **No calcineurin inhibitor, no T-cell-directed agent** |
| Earliest time point | **Day 5**, before the lesion exists | **2 weeks**, after it exists |
| DRG sampling density | about 9–12 ganglia per animal | Not stated in the main text; per-level tables are supplement-only |
| n per comparison | 3 per group | 3 per sex interim, **2 per sex terminal** |
| Result | Pathology reduced across three cargos; transgene expression unchanged (p = 0.45, 0.997, 0.33) | Pathology unchanged by either regimen, including under 100 % B-cell depletion |

**What the disagreement is NOT.** Not timing: the negative study's regimens began on day −1 and day −14, earlier than the positive study's weakest arm, which began on day 2. Not species: both are cynomolgus macaque. Not a flat contradiction about immunity: the negative scopes itself to *«primary **adaptive** immune responses»* and states that innate activation *«was not excluded»*.

**The three live explanations.** (1) **Drug class** — tacrolimus is the active element and the other programme never tested that class; most parsimonious, and offered by the party whose regimen worked. (2) **Power** — the negative's mitigation comparison has n = 2–3 per sex per cell with no power statement. (3) **Procedure and sampling** — iohexol contrast in one and not the other, different ganglion sampling density, different capsid, promoter and cargo.

**The constraint both poles must respect.** PMID 36700120 shows that empty capsid and promoter-less constructs cause neither the lesion nor an NfL rise: whatever the effector arm, the lesion requires transgene expression.

**Non-independence.** PMID 35331006 and PMID 36700120 are not two sources — same sponsor, four shared authors, data *«extracted from the Novartis study data warehouse»*, and three study descriptors matching. Neither paper cross-lists study identifiers, so overlap cannot be **proved** from these artefacts; the appearance of two-against-one is one sponsor's dataset against another's.

**Transfer limit to WWOX-DEE.** AAV DRG toxicity is reported as a **class effect of the vector**, not of any transgene, so the *existence* of the risk transfers to any AAV CNS programme including a WWOX one. What does **not** transfer: the regimens (no infant protocol was tested), the magnitudes (cargo-, capsid-, dose- and route-specific), and the mechanism — the one source that measured it states the immune mechanism **does not hold in mouse**, so no rodent WWOX study can test this question.

**Next action.** Watch for a head-to-head primate study giving dexamethasone + tacrolimus against prednisolone alone with vector, dose, route, contrast protocol and ganglion sampling density held constant, and powered. Nothing in the repository can decide this question without it.

**Cross-references:** `RL-GT-001` · `DIS-031` · `CC-20261003W3-C-RESTORATION-SPEC-01` (its off-target-organ row already carries DRG toxicity as an AAV class effect)

## RL-C-20261003w4b — The five risk parameters of a neuron-targeted AAV: which are measurable in advance, and which the 2022–2026 literature still assumes

**Status:** open
**Tag:** `INFERENZA`
**Opened:** 2026-10-03 (`CC-20261003w4-C-WINDOW-SPEC-01`, propagated by `BATCH_20261003_003`)
**Sources:** PMID 42349402 ([[paper_registry_current#PAPER 159]]) · PMID 41992613 ([[paper_registry_current#PAPER 160]]) · PMID 42458834 ([[paper_registry_current#PAPER 161]]) · PMID 36700120 ([[paper_registry_current#PAPER 164]]). All `partial_fulltext_read`; none mentions WWOX.
**Provenance:** Authored by `BATCH_20261003_003` from the op specification of `CC-20261003w4-C-WINDOW-SPEC-01` (intake wave 4 2026-10-03, Scientist C), whose ops were a prose specification; the record text below is the integrator's, the substance and every figure are the candidate's. `context_policy: SOURCE_FIRST`. **Not medical advice.**

**The finding.** Of the five parameters that would have to be fixed before a neuron-targeted AAV's risks could be called bounded in advance — promoter cell-class reach, the therapeutic window's lower limb, its upper limb, the systemic organ at risk, and a surveillance assay — **two can be bounded today and three cannot**, and the source that comes closest to measuring a two-sided therapeutic window states in its own text that it did not measure one.

| Parameter | Best measurement in this set | Measured or assumed | Transfer limit to WWOX-DEE |
|---|---|---|---|
| **Promoter cell-class reach** | PMID 42349402: a 410-bp mouse *Gad1* cassette at **92.2 % ± 1.3 %** inhibitory-neuron specificity after intravenous AAV-PHP.eB at 5.0 × 10¹¹ vg/mouse; about 85 % of PV⁺ neurons transduced, over 60 % of transduced cells PV⁺ | **MEASURED**, and the best-measured parameter in the group | The method transfers; the cassette does not — mouse-derived, no human orthologue tested. 🔴 Specificity is **route-contingent**: the same cassette falls to 63.9 % ± 4.1 % after direct hippocampal injection. Specificity is a property of cassette × route × dose. WWOX's **required** cell set is unknown: the repository holds no measurement of which populations need WWOX restored |
| **Therapeutic window, lower limb** | PMID 41992613: i.c.v. dose-ordered survival from median 23 d at 2 × 10¹⁰ vg/animal to median 373 d at 2 × 10¹¹; MED 2 × 10¹⁰ | **MEASURED**, within one construct and one route | Vector genomes do not transfer between genes, capsids, promoters or species. What transfers is that a lower limb **can** be measured when a dose series and a survival endpoint exist |
| **Therapeutic window, upper limb** | PMID 41992613: a survival inversion between two constructs (205 d → **29.5 d** for the codon-optimised derivative) | **INFERRED, NOT MEASURED**, and the source says so | The toxic arm is a **different construct**, so dose and expression change together; that cohort *«did not undergo comprehensive necropsy or histopathological evaluation»*; the authors write that measuring protein there *«would be valuable to define this therapeutic window»*. In primates the top dose tested became the **NOAEL**. No window anywhere in this corpus is expressed in units of protein. See `DIS-032` |
| **Systemic organ at risk** | PMID 42458834: strong ubiquitous expression after an intra-CSF injection in newborn mice killed **every** high-dose animal by P8 from **myocardial degeneration**, with cardiac *Ifnb1* over 1000-fold raised, while a promoter-matched control vector with a different transgene elicited none of it | **MEASURED**, and sponsor-adverse | 🔴 **The organ at risk from a CNS vector may not be the CNS.** That lesson transfers; the magnitude does not, because DDX3X's own roles in RIG-I/MAVS signalling and *Ddit3* transcription are plausibly the mechanism. **WWOX dose sensitivity is neither shown nor excluded and must not be assumed in either direction.** Transfer-critical: the lethal mouse dose, scaled by neonatal brain mass, equals about 1 × 10¹⁵ vg in a human, which the paper states is a dose several intra-CSF AAV9 trials use |
| **Surveillance assay** | PMID 36700120 — see `RL-C-20261003w4c` | **MEASURED**, nonclinically | Tier 3 under `LEGEND_CORE` §13 with respect to WWOX |

**The datum that matters most, and it is a negative.** The one paper whose thesis is that both insufficient and excessive transgene expression are suboptimal **does not measure the excessive side**: a survival inversion between two different constructs, no histopathology on the inverted arm, no measurement of the protein alleged to be excessive, and the missing measurement named by the authors themselves. Its primate arm then fails to reach a toxic dose at all. **«How much is too much» cannot be answered by a programme that has not measured the protein at the dose that caused harm** — wave 3 reached that conclusion from a set in which no source attempted a two-sided window; this adds a source that attempted one and did not complete it, and a negative with a failed positive control is a stronger negative.

**Three contacts with the wave-3 specification, all corroborating.** (1) The window row stands. (2) The off-target-organ row needs a sixth organ: the **heart**, after an intra-CSF route, with the brain spared morphologically — and the cause travels with the organ, a strong ubiquitous promoter on a dose-sensitive transgene. (3) The cell-type row gains a route caveat: one cassette, two routes, a 30-point swing in specificity.

**Next action.** Carry the route of administration alongside every promoter-specificity figure the repository holds, since none is portable across routes; and treat *«how much WWOX protein, in which cells»* as the acquisition that precedes any dose statement.

**Cross-references:** `RL-GT-001` · `RL-C-20261003w4a` · `DIS-032` · `CC-20261003W3-C-RESTORATION-SPEC-01`

## RL-C-20261003w4c — Vector-toxicity surveillance for a CNS AAV: a nonclinical-grade panel (blood NfL, with CSF CXCL10 and MIP1α as earlier-rising candidates), Tier 3 under LEGEND_CORE §13

🔴 **The §13 ruling first, because it places this record.** Neurofilament light chain, neurofilament heavy chain, CSF CXCL10 and CSF MIP1α measure neuro-axonal injury and innate immune activation **of any cause**. None reports WWOX abundance, transcript, splicing or function. All four are therefore **Tier 3 with respect to WWOX** and may **not** be recorded as WWOX biomarkers in any registry. They are admissible only as biomarkers of **vector toxicity**, in a safety-surveillance record — which is what this is. This record is deliberately **not** part of the biomarker line `RL-BIOM-001`. §13 also forbids calling a candidate *validated* without sensitivity and specificity evidence in the disease population, and there is none: the source states that *«To date, NfL measurements have not been incorporated into clinical trials for AAV therapies.»* The panel is **nonclinical-grade**, and that word is load-bearing.

**Status:** open
**Tag:** `DATO` for the measured operating characteristics · `INFERENZA` for their applicability to a WWOX programme
**Opened:** 2026-10-03 (`CC-20261003w4-C-TOXBIOMARKER-01`, propagated by `BATCH_20261003_003`)
**Sources:** PMID 36700120 ([[paper_registry_current#PAPER 164]], `FTR-20261003-36700120-01`) · PMID 41404412 ([[paper_registry_current#PAPER 162]], `FTR-20261003-41404412-01`) · PMID 41992613 ([[paper_registry_current#PAPER 160]]). All `partial_fulltext_read`; none mentions WWOX.
**Provenance:** Authored by `BATCH_20261003_003` from the op specification of `CC-20261003w4-C-TOXBIOMARKER-01` (intake wave 4 2026-10-03, Scientist C), whose ops were a prose specification; the record text below is the integrator's, the substance and every figure are the candidate's. `context_policy: SOURCE_FIRST`. **Not medical advice.**

| Measurement | Value |
|---|---|
| Denominator | 260 cynomolgus macaques, nine studies (four GLP, five non-GLP); 193 dosed with AAV9, of which 8 received empty capsid or a promoter-less construct; 67 vehicle controls |
| Histopathology rigour | **18–21 DRG per animal**, five-point severity scale, board-certified pathologist with contemporaneous peer review; composite per-animal endpoint 132 unremarkable, 67 minimal, 41 slight, 20 moderate |
| Lesion incidence | **78 %** at 2–12 weeks (max severity moderate), **42 %** up to 52 weeks (max minimal) |
| Blood–CSF agreement | Pearson R² = 0.80 over 399 paired samples |
| Baselines | Pre-dose means 12.2 pg/mL serum, 12.2 pg/mL plasma, 192 pg/mL CSF — CSF about 16× blood |
| Correlation with severity | Kendall τ 0.50–0.55 for all four NfL measures |
| **ROC AUC** | **0.85 blood / 0.81 CSF** for unremarkable vs any finding; **0.95 / 0.94** excluding minimal grade |
| **Per-animal cut-offs** (fold change from pre-dose; blood / CSF sensitivity and specificity) | 1.5× → 0.73/0.71 and 0.83/0.68 · 2× → 0.68/0.82 and 0.76/0.72 · 3× → 0.59/0.92 and 0.68/0.84 · 5× → 0.43/0.96 and 0.60/0.91 · 10× → 0.32/0.99 and 0.49/0.95 |
| Incremental value | Blood NfL improved a confounder model at p = 8 × 10⁻¹¹; adding CSF on top of blood improved fit at p = 0.0003 but moved AUC only 0.83 → 0.85 — **blood alone is sufficient**, and the invasive sample is not needed |
| Mechanistic constraint | Empty capsid and promoter-less constructs produced **neither** lesion nor NfL rise |
| Earlier-rising candidates | PMID 41404412: CSF CXCL10 significantly raised at **day 5** and MIP1α at day 9, both **before** the first lesion at day 15, both correlating with serum NF-H; CSF CXCL10 about 9× serum, indicating local CNS synthesis |

**The five caveats that must travel with the panel.** (1) **The procedure moves the marker**: post-dose vehicle-control NfL rises above pre-dose in both matrices (serum 12.2 → 24.3 pg/mL; CSF 192 → 433.7 pg/mL), which the authors attribute to dosing, CSF collection, blood draws and handling; PMID 41992613 reproduces the effect independently, its CSF NfL peaking at day 15 in **every** group including vehicle. (2) **A rise can occur without a lesion**, and the authors say so, because the lesion is heterogeneous and not all ganglia are examined. (3) **It is not disease-specific** — named by the authors as the obstacle to use in a patient who already has a neurodegenerative disorder, which is precisely the WWOX-DEE case. (4) **Only fold-change cut-offs exist, never a concentration**, so the panel is unusable without baseline sampling designed in before dosing. (5) **Non-independence**: PMID 36700120 and PMID 35331006 are the same sponsor with four shared authors and pooled data from that sponsor's own warehouse — one internal validation, not a cross-sponsor replication.

**What this adds to the wave-3 specification.** `CC-20261003W3-C-RESTORATION-SPEC-01` records a bare serum-NfL threshold (*«1,719 pg/mL or greater»* against *«≤679 pg/mL»*). This source supplies what that threshold lacks — a denominator, a ROC curve, sensitivity and specificity — **and simultaneously constrains how it may be used**, because the validated discriminator is a **fold change from the individual's own pre-dose value**, not an absolute concentration. The correct form of that row is a fold-change rule plus a mandatory baseline draw.

**Next action.** Wherever the repository carries an absolute serum-NfL threshold, carry the fold-change rule and the mandatory pre-dose baseline alongside it; and record that blood sampling alone is sufficient.

**Cross-references:** `RL-GT-001` · `RL-C-20261003w4a` · `RC-C-20261003w4` · `RL-BIOM-001` **explicitly as the line this record does NOT belong to**

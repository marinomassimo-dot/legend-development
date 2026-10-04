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

**Transfer limit to WWOX-DEE.** AAV DRG toxicity is reported as a **class effect of the vector**, not of any transgene, so the *existence* of the risk transfers to any AAV CNS programme including a WWOX one. 🔴 **Narrowed by intake wave 6 (2026-10-03, `BATCH_20261003_005`): the measured class is the CSF ROUTE, not AAV as such** — same capsid, 62× less DRG transduction intravenously than by intracisterna magna (PMID 42157962); no AAV-related DRG toxicity in an intraparenchymal arm whose intracisterna-magna sibling had findings at every dose (PMID 42422766); and four capsids on one CSF route indistinguishable (PMID 41078870). The full bound, with its live-but-weak counterexample, is at `RL-C-20261003w6` and in `RL-C-20261003w3`'s off-target-organ row. What does **not** transfer: the regimens (no infant protocol was tested), the magnitudes (cargo-, capsid-, dose- and route-specific), and the mechanism — the one source that measured it states the immune mechanism **does not hold in mouse**, so no rodent WWOX study can test this question.

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

---

## RL-GT-002 — Transgene immunity in a protein-naive host: the unmeasured parameter of a WWOX gene-replacement programme, and the regimen the human record attaches to a predicted null
**Status:** emerging — the risk is named and unmeasured
**Primary pathway:** P7 (gene therapy design), immune interface
**Tag:** `DATO` for the protocols and the assay gaps · `INFERENZA` for their applicability to a WWOX genotype class · `IPOTESI` for the regimen transfer
**Opened:** 2026-10-03 (`BATCH_20261003_004`)
**Provenance:** **MERGED record.** Authored by `BATCH_20261003_004` from two candidates that found the same finding independently, from disjoint source sets: `CC-20261003W5-A-TRANSGENE-IMMUNITY-01` (intake wave 5, Scientist A) and `CC-20261003W5-C-TRANSGENE-NULL-IMMUNOSUPPRESSION-01` (intake wave 5, Scientist C), the latter disposed `MERGED into RL-GT-002`. Both source sets are carried below; neither candidate's figures were re-derived by the integrator.
**Evidence base:** PMID 41314141 (`FTR-20261003-41314141-01`, [[paper_registry_current#PAPER 165]]) · PMID 39358605 (`FTR-20261003-39358605-01`, [[paper_registry_current#PAPER 167]]) · PMID 41712282 (`FTR-20261003-41712282-01`, [[paper_registry_current#PAPER 168]]) · PMID 40809677 (`FTR-20261003-40809677-01`, [[paper_registry_current#PAPER 169]]) · PMID 41712149 (`FTR-20261003-41712149-01`, [[paper_registry_current#PAPER 170]]) · PMID 42134074 (`FTR-20261003-42134074-01`, [[paper_registry_current#PAPER 182]]) · PMID 41966056 (`FTR-20261003-41966056-01`, [[paper_registry_current#PAPER 177]]) · PMID 41257285 (`FTR-20261003-41257285-01`, [[paper_registry_current#PAPER 179]]) — **none of which mentions WWOX**
**Clinical relevance:** HIGH strategic / NOT clinically validated
**Reason active:** a patient with two loss-of-function WWOX alleles makes no WWOX protein and is therefore cross-reactive-immunological-material (CRIM) **negative**. In the only first-in-human high-dose intrathecal AAV9 trial read by this repository, that classification prospectively decided the regimen: patients *«considered CRIM negative»* were placed on prednisone, sirolimus **and** tacrolimus, where a patient predicted to make some protein received two drugs. The inference that WWOX is "a self protein" and therefore poses only vector-and-route immune risk is **wrong for a biallelic null**, and was corrected here.
**What the human CSF-route record adds (group C arm of the merge).** Across the human intrathecal and intracisternal programmes reviewed in PMID 42134074, the regimen tracks predicted endogenous expression rather than the route: three programmes in predicted-null or pre-sensitised recipients use a steroid plus sirolimus plus tacrolimus, while the approved programme whose recipients retain protein via a paralogous gene uses prednisone alone. ⚠️ **Integrator amendments, `BATCH_20261003_004`, from the blind audit:** (a) in the CLN7 programme the review's own words are *«prednisone, sirolimus, and in some cases tacrolimus»* — the third agent is not universal in that cohort; (b) the single-patient intracisternal programme's *«48 weeks»* is the **regimen total**, not each agent's duration — and the per-agent figures first written here were themselves too short, corrected 2026-10-04 by `CC-20261004-MIRROR-11` from «sirolimus 48 weeks, prednisone about 8 weeks tapered, tacrolimus 24 weeks»: the source's own Results summary says the three agents were *«well tolerated and safely discontinued at 12, 32, and 48 weeks after RGX-111 dosing»*, and its Methods add that tacrolimus ran 24 weeks at full dose *«then reduced by 12.5% per week until discontinuation at 32 weeks»*. So **exposure** is prednisone 12 weeks, tacrolimus 32 weeks, sirolimus 48 weeks; the 8- and 24-week figures are the printed full-dose phases, not the exposures. Both quotes re-verified character-exact in `files/fulltext/PMID41966056_Wang2026_PMC.xml` by the propagating batch; (c) the review's two-month prednisone figure belongs to a phase 1/2 dose-escalation study, not to the approved intrathecal regimen, which the review says only *«appears sufficient»* without a duration.
**The gap that no source closes.** The one complete IND-enabling package for a recessive loss-of-function CNS disease in this corpus (PMID 39358605) tested transgene immunogenicity **only in wild-type animals** — which already express the orthologue — dosed at P1–3, with an interferon-γ ELISpot and **no antibody assay anywhere**. ⚠️ **Integrator amendment (audit):** that source states the dosing age and the assay; it makes **no claim about neonatal tolerance induction**, so the tolerance reading is this repository's inference, not the paper's. The one study here that did put a foreign protein into a knockout host (PMID 41712282) reports **no immune endpoint at all**. PMID 40809677 supplies the mechanism and its limits: early expression bought cellular but **not** humoral tolerance (*«neither treatment time point circumvented eliciting a humoral immune response»*), did not transfer to a redose, and was antigen-specific. ⚠️ **Integrator amendment (audit):** its adult arm received four times the neonatal vector, and the authors state this was **deliberate normalisation** to a brain roughly four times larger at 2 months than at P2 — so the arms are matched per brain volume by design, and "age and antigen load are unmatched" is the reader's caveat, not the source's.
**Three design choices that are not independent, two of them against intuition:** (1) a neuron-restricted promoter lowers overexpression-driven dorsal-root-ganglion risk but may impede MHC II-dependent regulatory T-cell tolerance (*«the use of the SynI promoter may have hampered the development of Cas9-reactive T»*); (2) early dosing buys cellular but not humoral tolerance and buys nothing for a second dose; (3) a WWOX null is CRIM-negative, so the human precedent for its class is the three-drug regimen — and the one immune event in that trial occurred in the single patient managed with two.
**What immunosuppression costs, stated with the finding.** In the single-patient intracisternal programme, 16 of the 17 first-year adverse events were assessed *«possibly related to immunosuppression»*; ⚠️ **integrator amendment (audit):** several of those events are **simultaneously** recorded as possibly related to study treatment, and this is one patient, so the attribution is not exclusive. In the paediatric antisense extension studies reviewed by PMID 41712149, transient cerebrospinal-fluid protein elevations above 50 mg/dL affected about three-quarters of children **when all measurements are counted irrespective of attribution**; ⚠️ the drug-attributed rate is about 27 % in the extensions and about 14 % in the pivotal studies — the unqualified three-quarters figure is not the attributed rate.
**A mechanistic reason the steroid may be the weakest component:** PMID 41257285 identifies an interferon/JAK-STAT axis rather than NF-κB in the primate toxicity it studies, and offers that as a reason *«glucocorticoids are not always as potent as expected»*; no animal in that study received immunosuppression, so modifiability is untested in it.
**Transfer limits (binding).** Not measured for WWOX; all eight sources are earned nulls for the gene. Does **not** transfer to a WWOX missense allele producing a stable but non-functional protein, which is not predicted-null; P47T, Q230P, G372R, A141T and P252A are not interchangeable with each other or with a null, and a heterozygote is neither a demonstrated negative nor a positive for haploinsufficiency. The durability observation rests on a **secreted** enzyme in a recipient with pre-existing antibody; WWOX protein is intracellular and that antibody mechanism does not carry over. No controlled comparison of triple versus single-agent prophylaxis exists in any of these programmes: the pattern is correlational across diseases, cargoes, doses, ages and eras.
**Next action:** before any WWOX cassette is specified, state which CRIM class the reference genotype falls in and design the immunogenicity experiment in a protein-**naive** host at the intended age of dosing, with a T-cell readout, an antibody readout, an anti-capsid readout and CNS histology for MHC II and CD3 — the four readouts PMID 40809677 shows can dissociate. Do not inherit a wild-type-animal immunogenicity package as evidence of tolerance. The falsifying design the group-C arm proposed is carried with it: a predicted-null cohort randomised to triple versus steroid-alone prophylaxis at a fixed CSF-route dose, with anti-transgene ELISpot, product persistence and adverse-event burden as endpoints.
**Cross-references:** `RL-GT-001` · `RL-GT-003` · `RL-C-20261003w4a` · `RC-A-20261003w5-01` · `DIS-033`
**Not medical advice.**

---

## RL-GT-003 — Cargo size and cassette design: the WWOX restoration parameter that is bounded by measurement
**Status:** active — bounded externally, blocked internally on one unmeasured number
**Primary pathway:** P7 (gene therapy design), vector architecture
**Tag:** `DATO` for the measured penalties and yields · `INFERENZA` for the ladder's applicability to a WWOX cassette
**Opened:** 2026-10-03 (`BATCH_20261003_004`, from the op specification of `CC-20261003W5-A-CARGO-CASSETTE-01`, intake wave 5, Scientist A)
**Evidence base:** PMID 41712282 (`FTR-20261003-41712282-01`, [[paper_registry_current#PAPER 168]]) · PMID 41314141 (`FTR-20261003-41314141-01`, [[paper_registry_current#PAPER 165]]) · PMID 39358605 (`FTR-20261003-39358605-01`, [[paper_registry_current#PAPER 167]]) · PMID 40988338 (`FTR-20261003-40988338-01`, [[paper_registry_current#PAPER 166]]) · PMID 41712149 (`FTR-20261003-41712149-01`, [[paper_registry_current#PAPER 170]]) — none of which mentions WWOX
**Clinical relevance:** HIGH strategic / NOT clinically validated
**Reason active:** this is the one restoration parameter whose cost function is measured end to end in the 2024–2026 literature, and the costs are asymmetric. Below about half the ~4.7 kb packaging limit a short synthetic promoter permits self-complementary packaging, which that source states is *«predicted to stably transduce at least 10-fold more cells than single-stranded AAV»* — ⚠️ a **prediction carried from citations**, not a measurement in that paper. A weak minimal promoter is simultaneously an overexpression-safety lever, since dorsal-root-ganglion toxicity is attributed by the human trial to transgene overexpression. Above the limit the penalty is measured twice: a **two-fold yield loss** against a same-day 4.617 kb control, and a genome population in which the reported *«75.81 % full length»* is the **4–6 kb size bin**, with 8.96 % at 3 kb and 15.22 % above 6 kb — readable only in the supplement. Above ~6 kb single-vector replacement is impossible and the only route is a split-intein dual vector, which improved survival and reduced seizures in two models and **has no human data**. A strong, large ubiquitous promoter gives the better rescue but *«combined with larger transgene lengths often exceeds the limits of AAV9 packaging capacity»*.
**What is NOT licensed.** The repository holds **no record of the size of a WWOX expression cassette** — no coding-sequence length for a stated isoform, no promoter choice, no regulatory-element or poly(A) budget. Which rung of this ladder a WWOX programme stands on is therefore unknown. And an oversized genome yielding full-length protein in vivo is **not** a licence to oversize a WWOX cassette: that source delivered **one** isoform of a multi-isoform gene and names the single-isoform choice as a candidate reason its neonatal arm failed behaviourally.
**Non-independence, stated:** three of the five sources share vector-design lineage (a minimal JeT promoter and its inventor as an author; a JeT-plus-intron variant from the same institution; a CBh plasmid provided by the same investigator). The promoter trade-off is attested by **one design tradition plus one independent group**, not by four independent ones.
**Next action:** measure and record the WWOX expression-cassette budget — coding-sequence length for the stated isoform, promoter, regulatory elements, poly(A), ITR to ITR — before any dose, route or window statement is attempted. It is arithmetic on a sequence, not an experiment, and nothing in this record can be applied until it exists.
**Transfer limit:** all five sources are earned nulls for WWOX; the record transfers a cost function and a vocabulary, never a dose or an efficacy expectation.
**Cross-references:** `RL-GT-001` · `RL-GT-002` · `RL-C-20261003w3` · `DIS-033`
**Not medical advice.**

---

## RL-GT-004 — Two-sided dose: a gene's two phenotypes may not share one dose, and the high-dose harm is reported below the headline
**Status:** active
**Primary pathway:** P7 (gene therapy design), dose selection
**Tag:** `DATO` for the measured curves and the attrition · `INFERENZA` for the design requirement it places on a WWOX programme
**Opened:** 2026-10-03 (`BATCH_20261003_004`, from the op specification of `CC-20261003W5-A-DOSE-TWO-SIDED-01`, intake wave 5, Scientist A)
**Evidence base:** PMID 41712282 (`FTR-20261003-41712282-01`, [[paper_registry_current#PAPER 168]]) · PMID 40988338 (`FTR-20261003-40988338-01`, [[paper_registry_current#PAPER 166]]) · PMID 39358605 (`FTR-20261003-39358605-01`, [[paper_registry_current#PAPER 167]]) · PMID 41314141 (`FTR-20261003-41314141-01`, [[paper_registry_current#PAPER 165]]) · PMID 41712149 (`FTR-20261003-41712149-01`, [[paper_registry_current#PAPER 170]]) — none of which mentions WWOX
**Clinical relevance:** HIGH strategic / NOT clinically validated
**Reason active:** in the one source that read a metabolic and a seizure endpoint in the same animals at the same two doses, the two curves differed. Plasma citrate fell dose-dependently — 87 ± 7.7 % of wild type at the low dose, **65 ± 8.0 %** at the high dose — an overshoot past normal from a knockout baseline about 20 % **above** wild type, while *«low-dose AAV9/SLC13A5 administered at P10 provided similar benefit as high dose»* on chemoconvulsant kindling. ⚠️ **Integrator amendment, `BATCH_20261003_004`, from the blind audit:** the saturation holds for the **pentylenetetrazol-kindling paradigm only** — the same paragraph records *«greater benefit with the high dose than low dose in all other metrics»*, including epileptic discharges, so other seizure-related endpoints did show a dose-response. The same authors record that overexpressing that gene in development has been reported to cause autistic-like behaviour and altered white-matter integrity. For a disease model predicting both a metabolic and a seizure axis, this is the shape of the dosing problem: not which dose rescues, but whether the axes agree and which one the dose is for.
**TRANSFER LIMIT:** the comparator gene is a transporter with a directly measurable analyte in blood and CSF, which is why the mismatch is visible at all. WWOX has no such analyte in this repository, so a WWOX programme could dose to a seizure endpoint and never learn that another axis had overshot. The transfer is to **experimental design** — measure every predicted axis at every dose level, in the same animals — and never to a dose.
**The second pattern: the high-dose harm sits below the headline.** (i) A *«well tolerated»*, dose-dependent rescue whose methods clause and supplementary table carry **5 of 10 high-dose animals with poor surgical recovery** (0 of 8 low dose, 0 of 4 mid, 1 of 11 non-injected), with the Discussion's safety paragraph silent on it, so the high-dose electrophysiology is the surviving half of that group. (ii) An abstract reporting *«no significant adverse events»* over dose- and time-dependent degeneration in dorsal root ganglia, spinal cord and sciatic nerve, a treatment-associated white-cell and lymphocyte rise at 28 days and one unexplained death at 80 days — ⚠️ **integrator amendments (audit):** the source says that rise *«had diminished»* by one year rather than resolved, and the nerve findings are **arm-level but single-animal** (1 of 3, 1 of 3 and 1 of 4 in the non-detargeted arms), with one animal in the detargeted arm still showing minimal sacral-DRG neuronal autophagy graded non-adverse. (iii) A *«well tolerated»* highest-ever intrathecal dose whose lot was 42 % genome-containing (so the capsid burden was 2.38 × 10^15 particles) and whose adverse-event table does not reconcile with itself.
**Next action:** require of any WWOX dose-finding design that (i) every axis the working model predicts is measured at every dose level in the same animals, (ii) per-group attrition and its cause are reported per dose arm, and (iii) a tolerability claim is read against the body and the supplement rather than the abstract.
**Cross-references:** `RL-GT-001` · `RL-GT-003` · `RL-C-20261003w4b` · `RC-A-20261003w5-03` · `DIS-032`
**Not medical advice.**

---

## RL-C-20261003w3 — The six parameters of a WWOX-restoration strategy, and which of them any source actually measures
**Status:** open
**Primary pathway:** P7 (gene therapy design), restoration specification
**Tag:** `INFERENZA` — the parameter list is this repository's framing; each cell under it is `DATO` for the source named and carries its own transfer limit
**Opened:** 2026-10-03 (`BATCH_20261003_004`, authored from the op specification of `CC-20261003W3-C-RESTORATION-SPEC-01`, intake wave 3, Scientist C; the candidate described the records and did not write them)
**Evidence base:** PMID 40349107 (`FTR-20261003-40349107-01`, [[paper_registry_current#CORPUS P401]]) · PMID 39847501 (`FTR-20261003-39847501-01`, [[paper_registry_current#CORPUS P402]]) · PMID 40263630 (`FTR-20261003-40263630-01`, [[paper_registry_current#CORPUS P403]]) · PMID 42181696 (`FTR-20261003-42181696-01`, [[paper_registry_current#CORPUS P404]]) · PMID 42521212 (`FTR-20261003-42521212-01`, [[paper_registry_current#CORPUS P405]]) — none of which mentions WWOX
**Clinical relevance:** HIGH strategic / NOT clinically validated
**Reason active:** of the six parameters a WWOX-restoration strategy would have to fix — how much protein, in which cell types, by what route, inside what window, with what off-target organ risk, measured by what pharmacodynamic assay — this source set **measures route, cell-type reach and off-target organ risk well, measures dose only as vector genomes and not as rescued protein, does not measure the window at all, and holds no WWOX-specific pharmacodynamic assay**.
- **Dose.** Mouse 1 × 10^10 – 1 × 10^11 vg/animal intracerebroventricularly at PND1 with dose-dependent rescue and brain protein rising from ~0.4 to ~2.2 ng/µg; a nonhuman-primate arm at 1 × 10^14 vg/animal; a second study at 1.1–1.7 × 10^11 vg/mouse at P2; a third at 1 × 10^10 – 1 × 10^11 vg/mouse that is **non-monotonic**. Vector genomes transfer between neither genes, capsids, promoters nor species. What transfers is the shape: in two of the three, **the highest dose was not the best dose**.
- **Cell type.** Excitatory-versus-inhibitory coverage quantified per promoter (51 %/35 % for one engineered promoter; two others excitatory-biased), and PV 46 %/36 %, SST 64 %/51 %, VIP 8 %/18 % from a Gad1-promoter construct. Transferable as method, and as the warning that "pan-neuronal" promoters are not pan-neuronal. **WWOX's required cell set is unknown**: this repository holds no measurement of which neuronal or glial populations need WWOX restored.
- **Route.** Intracerebroventricular, bilateral in neonatal mice and unilateral in primate after MRI-guided stereotaxy; intracerebroventricular plus intravenous where a peripheral organ is implicated; lumbar intrathecal for an oligonucleotide in a preterm infant. Route transfers best of the six, because anatomy and capsid set it rather than the gene.
- **Window.** **Not measured anywhere in this set** — see `DIS-033`, into which this candidate's window dismissal was merged.
- **Off-target organ risk.** The strongest contribution: blind-graded dorsal-root-ganglion and spinal-cord histopathology, nerve conduction, and serum neurofilament light as a toxicity biomarker. ⚠️ **Integrator amendments, `BATCH_20261003_004`, from the blind audit:** the 1,719 pg/mL figure is the concentration the three affected animals **reached**, not a pre-specified threshold (contrast animals peaked no higher than 679 pg/mL); the nerve-conduction change affected 2 of 4 animals in one arm and 2 of 3 in another, described by the authors as mild with no expected adverse clinical correlate; and the dorsal-root-ganglion findings are arm-level but single-animal, with one animal in the detargeted arm still affected. Dorsal-root-ganglion toxicity is an **AAV class effect**, so it transfers to any AAV CNS programme including a WWOX one; the detargeting element's generality rests on three promoters and two transgenes. 🔴 **Bounded by intake wave 6 (2026-10-03, `BATCH_20261003_005`, from `CC-20261003W6-C-DRG-ATTRIBUTION-01` §3), on three sources this row did not have.** (1) **It is a CSF-ROUTE effect, not an AAV effect.** With the **same capsid**, the intravenous route gave **62× less** dorsal-root-ganglion transduction than intracisterna magna (PMID 42157962, [[paper_registry_current#PAPER 186]]); and in one study the intraparenchymal arm had **no AAV-related DRG toxicity** while the intracisterna-magna arm of the same study had adverse DRG findings at every dose level (PMID 42422766, [[paper_registry_current#PAPER 184]]). (2) **Capsid is not the variable.** AAV1, AAV5, AAV9 and AAVDJ held against one route and one cassette showed no significant biodistribution difference and the authors decline to rank them; sacral-DRG transgene positivity was 31–80 % of cells in all three AAV1 animals and two of three AAV9 animals, with DRG pathology in **one animal only** (PMID 41078870, [[paper_registry_current#PAPER 185]]). (3) **It is not universal.** One primate intrathecal study reports a clean DRG at 4.67 × 10^13 vg/animal (PMID 40301740, [[paper_registry_current#PAPER 188]]); its own Figure 7 legend disagrees with its Results text, so that counterexample is **live but weak**, not refuting. **So the row's wording is narrowed from «AAV class effect» to «a class effect of the CSF ROUTE, measured for every capsid tested on that route»** — which still transfers the existence of the risk to any CSF-route WWOX programme, and no longer transfers it to an intravenous or intraparenchymal one without its own measurement. ⚠️ **Integrator amendment, `BATCH_20261003_005`, from the blind audit:** «no capsid reached the deep brain» overstates PMID 41078870: what it measured is **no detectable HA (transgene-product) immunoreactivity** in substantia nigra or striatum for any of the four, which is not the same as no capsid arriving. What is **untouched**: the usefulness of a DRG-detargeting element and of serum neurofilament light as a toxicity biomarker, both from PMID 40349107 — none of the six wave-6 sources measured NfL, and PMID 36951961 cites the miRNA-binding-site experiment as the field's own discriminating result rather than repeating it (⚠️ **Integrator amendment, `BATCH_20261003_005`, from the blind audit:** that experiment is a **cited third-party follow-up report**, not PMID 36951961's own work). Carried at `RL-C-20261003w6`.
- **Pharmacodynamic assay.** An endogenous HiBiT knock-in with LgBiT complementation, bidirectionally validated, in a line whose untagged allele is a frameshift; plus protein in ng/µg and serum neurofilament light in the primate package. Methodologically transferable; **nothing WWOX-specific exists**. ⚠️ **Integrator amendment (audit):** the copy-number change in that reporter work is in **one clone and its derivatives**, and the source says it *«can confer»* a survival advantage — a potential, not a measured one; a second clone carried no structural variant.
**The datum that matters most, and it is a negative.** One study rescued survival (50 → 84.2 %), febrile seizures (11/15 → 2/13) and spontaneous seizures (1.12 → 0.03 per mouse per day) while cortical NaV1.1 protein moved from ~0.45 to ~0.49 of wild type, **not significantly different**, and cortical mRNA moved about 8 % of the wild-type level. Either the antibody is insensitive or full normalisation is not required; the paper keeps both. ⚠️ **Integrator amendment (audit):** the table behind one seizure endpoint is 3 untreated and 3 treated animals with no test, confidence interval or p value, and the paper's seizure case also rests on lifespan and hyperthermia endpoints reported elsewhere with their own statistics. The consequence for this repository is unchanged and actionable: **"how much protein is needed" cannot be answered by a programme whose assay cannot see the increment.**
**Next action:** acquire a WWOX pharmacodynamic readout before specifying a restoration dose (`RC-C-20261003w3`), and record the cassette budget (`RL-GT-003`).
**Transfer limit:** every source here is an earned null for WWOX. No cell of the table licenses a WWOX dose, window or efficacy expectation; P47T, Q230P, G372R, A141T and P252A are not interchangeable, and a heterozygote is neither a demonstrated negative nor a positive for haploinsufficiency.
**Cross-references:** `RL-GT-001` · `RL-GT-003` · `RL-GT-004` · `DIS-033` · `RC-C-20261003w3`
**Not medical advice.**

## RL-C-20261003w6 — The CSF-route AAV harm, split into its dose-driven, immune-flavoured and route-driven parts, with the species of each measurement
**Status:** open
**Primary pathway:** P7 (gene therapy design), safety interface
**Tag:** `DATO` for each measurement · `INFERENZA` for the three-way split and for its transfer to a WWOX programme
**Opened:** 2026-10-03 (`BATCH_20261003_005`, from `CC-20261003W6-C-DRG-ATTRIBUTION-01`, intake wave 6 Scientist C)
**Evidence base:** PMID 37515322 (`FTR-20261003-37515322-01`, [[paper_registry_current#PAPER 183]]) · PMID 42422766 (`FTR-20261003-42422766-01`, [[paper_registry_current#PAPER 184]]) · PMID 41078870 (`FTR-20261003-41078870-01`, [[paper_registry_current#PAPER 185]]) · PMID 42157962 (`FTR-20261003-42157962-01`, [[paper_registry_current#PAPER 186]]) · PMID 36951961 (`FTR-20261003-36951961-01`, [[paper_registry_current#PAPER 187]]) · PMID 40301740 (`FTR-20261003-40301740-01`, [[paper_registry_current#PAPER 188]]) — all `partial_fulltext_read` (partial full text), and **none of them mentions WWOX** (zero occurrences of the string in every artefact)
**Clinical relevance:** HIGH strategic / NOT clinically validated. **Not medical advice.**
**The finding in one sentence.** Across six primate datasets the sensory-ganglion harm of a CSF-route AAV dose separates into a **mononuclear infiltrate**, which appeared at every dose level in every study that used no immunosuppression *and* in every animal of the one study that used a full corticosteroid-plus-mTOR regimen, and a **neuronal degeneration**, which appeared only above a dose threshold — so dose and immune state act on two different endpoints, and the lever that moves one is not the lever that moves the other.
**Dose-driven.** Lumbar-DRG neuronal degeneration 100 % at 1.68 × 10^14 vg/NHP in both sexes and 0 % at 8.40 × 10^13 vg/NHP under identical immunosuppression, with sural nerve conduction velocity and amplitude falling at the top dose and the peroneal nerve spared (PMID 36951961, n = 2 per cohort; a self-complementary AAV9 under a deliberately weak promoter — vector-genome numbers do not transfer between genes or capsids). Systemic lethality at about 2 × 10^14 vg/kg intravenously against asymptomatic enzyme changes at 1.1 × 10^14 vg/kg (PMID 37515322; liver endpoint, intravenous route). Efficacy and CNS protein both saturating below the highest dose tested (PMID 40301740); and an over-expression ceiling expressed as fold-of-endogenous (PMID 42157962). ⚠️ **Integrator amendment, `BATCH_20261003_005`, from the blind audit:** that ceiling is **not a general transgene bound and not measured in that paper**: its own sentence cites prior frataxin work (refs 29–30) for 9-fold being tolerated in heart and liver and for levels above 20-fold impairing mitochondrial function. The **units** (fold-of-endogenous) transfer; the numbers are FXN-specific and literature-carried.
**Immune-flavoured, partly suppressible, and not on this endpoint.** Prednisolone prevented periportal CD3+ infiltration at 6 weeks and reduced hepatocyte ADAR1 — and prevented neither the transaminase rise nor the microscopic findings, with all differences gone by 26 weeks (PMID 37515322; liver, not ganglion). Methylprednisolone plus rapamycin left a lumbar-DRG infiltrate in **every** dosed animal while no T-cell response was detectable under the regimen (PMID 36951961; one regimen, **no unmedicated arm**, so the regimen is not shown to have suppressed anything). Rituximab plus everolimus depleted peripheral B cells and changed neither anti-AAV9 titre nor the injury (PMID 37515322) — the humoral arm is not the lever for this endpoint. The whole of this paragraph's negative is carried as the wave-6 arm of `DIS-031`.
**Route-driven.** Intracisterna magna gave cord and DRG transgene RNA with adverse findings and no significant brain GCase change, while intraparenchymal dosing gave brain expression, no AAV-related DRG toxicity, and adverse **brain** findings with early euthanasia of a whole dose group (PMID 42422766 — route relocates the harm rather than removing it; ⚠️ **Integrator amendment, `BATCH_20261003_005`, from the blind audit:** the brain negative is an **enzyme-activity** endpoint, «no significant changes in GCase activity… compared with aCSF control animals», not the absence of any measurable brain effect; and the adverse findings are reported as a **group** present at all dose levels, not as each listed tissue at each dose). Same capsid, intravenous versus intracisterna magna: 62× less DRG, 25× less cerebellar dentate, 10× more heart (PMID 42157962 — the ratio transfers as a design fact, the fold-changes are capsid-specific). Four capsids, one ICM route, one dose: no significant biodistribution difference and no detectable transgene-product staining in deep brain for any of them, under weekly corticosteroid cover, male animals only (PMID 41078870). Liver 721 vg/dg after intravenous versus 19 vg/dg after intrathecal dosing, injury at day 3–4 versus about two weeks (PMID 37515322).
**Every histological datum in this set is animal.** The only two human facts in it are the onasemnogene liver-test record and a single ALS patient's transient sensory symptoms after intrathecal AAV, **neither of them histology**.
**Neonatal tolerisation is measured nowhere in this set.** The one early-postnatal arm (PMID 42422766, P0 intracerebroventricular in mice) confounds age with species by the authors' own admission.
**Transfer limits (binding).** Cynomolgus macaque and mouse; cargoes GBA1, FXN, AP4M1, SMN1, ASPA and EGFP, none of them WWOX; **no WWOX construct exists, so no dose in these units transfers to one.** A WWOX restoration cassette is a promoter-driven protein transgene and sits on the expression-dependent side of the capsid-versus-expression line; the secreted-cargo logic of PMID 42157962 does not carry to an intracellular protein. P47T, Q230P, G372R, A141T and P252A are not interchangeable with each other or with a null, and a heterozygote is neither a demonstrated negative nor a positive for haploinsufficiency.
**What falsifies this record.** The dose/immune separation falls if a primate study under one regimen shows neuronal-degeneration incidence flat across dose while infiltrate varies. The route attribution falls if an intraparenchymal or intravenous primate study at matched CNS exposure shows DRG pathology equal to a CSF route. The «not universal» bound strengthens into a refutation of the class-effect wording if PMID 40301740's Figure 7 panels, graded, confirm a clean DRG at 4.67 × 10^13 vg/animal.
**Next action:** read Grubor 2025 (doi `10.1016/j.omtm.2025.101643`, `FT-193`) — the published immunosuppression-versus-DRG-pathology study that the field's «reduce but not eliminate» sentence actually rests on, and which this repository has not read.
**Cross-references:** `RL-C-20261003w3` · `RL-C-20261003w4a` · `RL-GT-002` · `RL-GT-004` · `DIS-031` · `DL-THER-116` · `DL-METH-118` · `DL-METH-120`
**Not medical advice.**

---

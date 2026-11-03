# IT22 P6: qualification of the thyroid hormone receptor (TR) agonist hypothesis for the WWOX oligodendrocyte-maturation deficit

Package `qualification_it22_p6_20261103/tr_agonists`, worktree `it22`, producer role. Written 2026-11-03. Public edition: the reference genotype class (WWOX-DEE), never an individual. Not medical advice; nothing here proposes a regimen. Public key-less routes only (PubMed full-text tool, Europe PMC REST); no e-mail address or account was used or sent anywhere.

**Status of the hypothesis.** A qualification, not a promotion. Hypothesis under test (partial-benefit track): *a TR agonist could help the oligodendrocyte-maturation / myelination deficit of WWOX deficiency.* Class: IPOTESI. No record, card or current file is changed by this package.

## 1. Verdict in three lines

1. The hypothesis **survives as a bypass question for an in-vitro experiment**, not as a benefit claim: thyroid hormone is a well-established driver of OPC cycle exit and differentiation, and the WWOX deficit has the shape of a maturation block (OPC up, CC1+ down), so a receptor-level push is mechanistically coherent. No TR agonist has ever been given to any WWOX-deficient system, and no thyroid-axis datum on WWOX-deficient neurons or OPCs exists in the module.
2. **Weakest link: the human Triac precedent is a hormone-entry defect, not a maturation block, and it shows no neurological benefit yet.** In MCT8 deficiency TH cannot enter the brain, so any TR agonist that bypasses the transporter fills a real gap; in WWOX deficiency TH entry is not known to be impaired and the hypothesised gap is downstream (a neuron-derived signal, unidentified). The only human trials read (Triac Trial I and the real-life cohort) did not measure neurodevelopment as an endpoint; the mouse rescue works only in the first three postnatal weeks, a window the WWOX-null mouse (premature lethality, seizures from about P9) barely has.
3. **Second weak link: isoform.** The OPC literature read at abstract depth puts TR alpha1 (not TR beta) as the receptor that times OPC differentiation in rodent OPCs. The THRB-selective agents in the catalogue (resmetirom, and by design the liver-directed class) would then be the wrong tools for this question, and a TR-alpha-active agonist carries the cardiac, seizure and axis liabilities listed in section 5.

## 2. Inputs and what they were used for

| Input | Used for |
|---|---|
| `../../qualification_it21_p3b_20261103/README.md`, Q03 / G03 | the hypothesis as qualified there (KEPT_CONDITIONAL; five fields; "new molecule for LEGEND"; seizure threshold "not looked up", closed here in section 5) |
| `../../glia_maturation_it14_p4_20261101/README.md` (decision RESTRICT) | the WWOX myelin evidence base: E01-E34; neuron-driven developmental deficit; OPC up with CC1+ down, no caspase-3 apoptosis; maturation block favoured over loss, not demonstrated; neuron-restricted add-back restores EM counts; the single seizure-free co-culture (E09, n=4 v 4); the null-OPC monoculture preprint (E23, unreviewed) |
| `../../generation_it22_p1_20261103/class_alternatives_it22.py --targets THRB,THRA` with `LEGEND_CATALOG_CACHE` set to the catalogue cache | typed potency table (section 3), run unmodified on 2026-11-03 |
| Papers in section 9 | everything labelled "read" below, with the depth in section 9 |

Knew before reading: that Triac is used in MCT8 deficiency and that T3 drives OPC differentiation (background, flagged as such in the IT21 record). Learned in this session and not in the IT21 record: the OPC isoform finding (TR alpha, not beta, by mRNA and by knockout phenotype), the Trial I and cohort neurological limits, the seizure statements in both directions, the age-limited window and the high-dose / axis-suppression trade-off in the mouse.

## 3. Measured pharmacology (catalogue table, typed, not converted)

Source: Guide to Pharmacology release in the catalogue cache, via `class_alternatives_it22.py`. Values in nM as the script prints them. **The assay class is "unknown" for every row**: the release does not say whether a value is a binding or a functional measure, which tissue or species, which radioligand. A same-type ratio is the only comparison the script allows, and is shown only where both isoforms have a value of the same type. Nothing below converts IC50, EC50, Ki or Kd into one another, and nothing below ranks compounds on similarity or network score.

| Compound (catalogue id) | THRB value, type | THRA value, type | Same-type isoform ratio (script output) | Approval flag |
|---|---|---|---|---|
| tiratricol / Triac (2637) | 0.02, Kd | none listed: **unknown** | not comparable (no THRA value) | yes |
| triiodothyronine / T3 (2634) | 0.079, Kd | 0.1, Kd | 1.3x (THRA vs THRB, Kd); i.e. no isoform preference at the resolution of the table | yes |
| T4 / levothyroxine (2635) | 3.02, IC50 | none listed: **unknown** | not comparable | yes |
| sobetirome (2639) | 0.068, Kd | 0.437, type "?" | not comparable (types differ; the THRA type is unrecorded) | no |
| resmetirom (12026) | 210, EC50 | 3740, EC50 | THRB 17.8x more potent than THRA, EC50 vs EC50 | yes |

Reading rules applied: (a) Triac Kd at THRB (0.02) and T3 Kd at THRB (0.079) share a type but the release gives no assay class, so the catalogue alone does not license "Triac binds tighter than T3"; (b) the T4 value is an IC50 at THRB listed with the action "Agonist" and says nothing about T4 as a prohormone or about brain deiodination; (c) the sobetirome THRA entry has no recorded type, so sobetirome's isoform selectivity is **unknown** here, not "THRB-selective"; (d) resmetirom is the only compound in the table with a same-type isoform ratio, and it shows THRB preference at EC50. Other ligands in the same table (KB-141, VK2809, NH-3, compound 16g) were not assessed against a primary source and are not considered candidates here.

## 4. Compound dossiers

Common frame for all compounds: nuclear receptor action, genomic. TH receptors TR alpha and TR beta bind T3 and regulate transcription; in rodent OPCs the TR alpha pair is expressed and TR beta mRNA is not (abstract-level: PMID 11412031, 12456652).

### 4.1 Tiratricol (Triac, 3,3',5-triiodothyroacetic acid)

* **Identity and form.** Acetic-acid analogue of T3. Oral tablets (350 microgram tablets in the trials). Catalogue flag: approved. The regulatory status in a given country was not verified here.
* **Action and measured pharmacology.** TR agonist (ChEMBL/GtoPdb action "Agonist"). THRB Kd 0.02 nM; no THRA value in the release (unknown). Clinical pharmacodynamics (read): suppresses TSH and lowers free T4, total T4 and reverse T3 while lowering serum T3 (Trial I, PMID 31377265); "relatively weak thyromimetic activity in peripheral tissues" is the authors' characterisation, not a measurement in that paper.
* **CNS access.** Entry is "not dependent on MCT8" (Trial I introduction, author statement). It is not shown to be transporter-free: a murine candidate route, Slc22a8, is strongly expressed at the blood-brain barrier only in early postnatal life, and several human and murine Triac-transporting proteins have been reported (review statement, PMID 39485732; the primary transporter papers were **not** read). The age-limited mouse response (section 4.1 precedent) is consistent with a developmentally regulated entry route but the paper itself calls the reason "elusive". Measured human brain exposure: none found in the sources read.
* **Human precedent, MCT8 deficiency (primary trial papers read).**
  * *Trial I, PMID 31377265* (Lancet Diabetes Endocrinol 2019; single-arm, open-label, phase 2; 46 enrolled, 40 completed 12 months; median baseline age 7.1 years, range 0.8-66.8). Dose: mean 38.3 microgram/kg/day (range 6.4-84.3), dose-escalated to a serum total T3 target of 1.4-2.5 nmol/L. Primary endpoint serum T3 fell 3.15 nmol/L (95% CI 2.68-3.62). Weight-for-age z-score +0.27, resting heart rate -9 bpm, SHBG down, creatine kinase up. Safety: 43 of 46 had at least one adverse event; 7 events in 6 patients (13%) judged treatment-related, all mild (perspiration, irritability); serious events attributed to the disease (infections); one death (sepsis). **Seizures:** "In three subjects with pre-existing seizures an increase in seizure frequency was reported", with one coincident gastrointestinal infection and two with hard-to-control seizures; the authors attribute serious events to the disease. **Neurology:** the exploratory gross-motor signal was largest when treatment began before 4 years (2 of 7 patients with a completely inactivating mutation reached the 20% GMFM-G88 level), but "the current trial was not designed to detect whether Triac also modulates neurodevelopment". Unknown, stated by the authors: whether further T4 lowering worsens brain hypothyroidism.
  * *Real-life cohort, PMID 34679181* (J Clin Endocrinol Metab 2022; retrospective; 67 patients, 33 sites, median baseline age 4.6 years, 23 under 2.5 years; median treatment 2.2 years, up to 6.2; 180.4 patient-years). Median maintenance dose 38 microgram/kg/day (IQR 31-61; range 15-105). T3 4.58 to 1.66 nmol/L. Weight-for-age exceeded the natural-history reference by 0.72 SD. "No severe adverse events related to Triac were reported"; transient thyrotoxic signs in 5 of 67; 3 deaths (sudden death at 13, aspiration at 71, unknown cause at 14), consistent per the authors with the natural history, no autopsies. Neurodevelopmental outcomes were not uniformly collected.
  * *Triac Trial II* (NCT02396459; patients under 30 months, 96 months, higher dose per the review): **no results found** in any source read; the 2024 guideline (PMID 38963712) says the neurocognitive response is "unknown" and under investigation, and states that "No available treatment regimen has proven to rescue the neurocognitive phenotype in humans with MCT8 deficiency."
  * Thyrotoxicosis: Triac there is given to treat peripheral thyrotoxicosis caused by high T3 and is dosed to lower serum T3; in a euthyroid child (the WWOX case) the same dose could add to, not offset, thyroid hormone action. This is an inference from the trial design, not a measurement.
* **Mouse precedent (primary, read).** Mct8/Oatp1c1 double-knockout mice, PMID 36834863: Triac 400 ng/g daily during postnatal weeks 1-3 normalised cortical MBP, corpus-callosum FluoroMyelin, PV+ interneuron counts, mIPSC and rotarod; started in weeks 3-6, "myelination was not improved" and PV recovery was partial. The low dose (50 ng/g), which the authors equate to the clinical dose range, had "only little" effect on myelination and interneuron maturation. The effective dose fully suppressed the thyroid axis (Tshb below detection) and still produced a peripheral thyrotoxic readout (hepatic and renal Dio1). n per group 3-5. The model has no seizure phenotype that this paper reports.
* **WWOX-relevant evidence.** None direct. The hypothesis connects two WWOX needs that the same drug touched in a different disease (myelination and PV interneuron maturation). Nothing tests it in Wwox-null cells.
* **Inference chain.** Compound (Triac) -> action (TR agonist, enters brain in early life by an incompletely characterised route) -> mechanism (TR-dependent OPC cycle exit and differentiation; TR-dependent interneuron maturation) -> context (neuron-driven maturation block in Wwox-null development) -> hypothesised benefit (more CC1+/MBP+ cells from the arrested OPC pool).
* **Decisive assumption.** The WWOX block is TR-responsive and causal (the OPCs are stuck, not absent, and the stall can be released by receptor activation despite an unchanged upstream neuronal defect), and the dose that does this in vitro is not also the dose that raises seizure susceptibility in vivo.
* **Counter-evidence and possible opposite effects.** (1) Different disease: MCT8 deficiency is TH-deficient brain, WWOX is not known to be. (2) Early-window dependence in mouse and the human note that fetal damage precedes birth. (3) Axis suppression: Tshb undetectable at the effective mouse dose; unknown consequence of lowering T4 in humans (Trial I, guideline). (4) Thyrotoxic signs and peripheral thyromimetic action at higher doses (both papers). (5) Seizures: see section 5. (6) A Triac-specific unknown: it was reported without a TR isoform break-down in the release, so TR alpha vs TR beta action is unknown.
* **Minimum discriminating experiment.** Section 6.
* **Missing data / feasibility.** Brain and OPC exposure at any dose; Triac in a T3-deprived neuron-OPC system; Trial II result. In-vitro test feasible with the existing co-culture design and commercially available compound; zero spend is not guaranteed for the compound itself (price not looked up).

### 4.2 Liothyronine (T3, triiodothyronine)

* **Identity and form.** The natural receptor ligand; oral synthetic form (liothyronine sodium) is approved (catalogue flag yes).
* **Action and measured pharmacology.** Agonist. THRB Kd 0.079 nM; THRA Kd 0.1 nM; same-type ratio 1.3x, i.e. no isoform preference in the release's values (assay class unknown).
* **CNS access.** Needs transporters. The transporter route for T3 at the brain barrier is MCT8 (T3 and T4) with OATP1C1 mainly for T4 in rodents (stated in the Dko paper's introduction, PMID 36834863; Oatp1c1 is described there as T4-specific at the murine barrier). Whether the human blood-brain barrier uses OATP1C1 was not established by anything read. In WWOX deficiency MCT8 is not known to be absent, so T3 should reach cells that express it; this is untested. Human OPCs express MCT8 (hESC-derived oligodendrocyte lineage, PMID 29111262, read in part). In an in-vitro system the medium T3 is the key confound: the standard hESC-OPC differentiation medium used in that paper contains T3 (50 ng/mL in the Fig. 5 legend arm).
* **WWOX-relevant evidence.** None. The WWOX co-culture (E09) was not described as a T3-deprived system; whether its medium contains T3 is **not known from what was read** and is the first thing to check.
* **Inference chain.** As Triac, with the natural ligand: T3 -> TR activation -> OPC differentiation. In vitro, T3 is both the control and the test, so the experiment needs a defined T3 concentration, not "plus or minus T3".
* **Decisive assumption.** The Wwox-null signal blocks differentiation upstream of, not at, TR (so that adding more T3 changes the fate), and the Wwox-null condition is not already saturated by medium T3.
* **Counter-evidence.** Chronic T3 *inhibited* endogenous remyelination and exacerbated disease in a genetic mouse model of demyelination, while sobetirome and Sob-AM2 improved it (PMID 30996143, **abstract only**; adult demyelination, not development). Hyperthyroid rats (T3 100 microgram/kg/day for 7 days) had increased susceptibility to isoniazid and picrotoxin seizures (PMID 1513203, **abstract only**). Systemic hypermetabolism against the glycaemia need (IT21 note, no new data).
* **Experiment.** Same as section 6, as the physiological reference arm.
* **Missing data / feasibility.** Medium composition of the existing co-culture; free hormone in serum-containing media. Feasible, cheap, but T3 control of the dish is the difficulty.

### 4.3 Levothyroxine (T4)

* **Identity and form.** Prohormone; approved oral drug.
* **Action and measured pharmacology.** Catalogue: THRB IC50 3.02 nM, listed as Agonist; no THRA value. This is the value of the prohormone at the receptor in an unrecorded assay; the biologically active ligand after deiodination is T3, and the catalogue value does not describe that conversion. **Not converted, not compared to the Kd values above.**
* **CNS access.** Via MCT8 and OATP1C1 (above), then local conversion to T3 by deiodinase 2 in glia (background, not verified in this session).
* **Human precedent.** In MCT8 deficiency levothyroxine at 2.5-15 microgram/kg/day started at 0.5-36 months "did not improve neurodevelopment and, in some cases even aggravated the hyperthyroid state" (2024 guideline, PMID 38963712, secondary; the underlying case reports were not read). It fails there because the transporter is missing, which is the reverse of the WWOX case, so this is no evidence for or against T4 in WWOX.
* **WWOX-relevant evidence / inference.** None. T4 is not a bypass agent; if the WWOX block is receptor-level, T3 or an analogue is the proximate test, and T4 only adds a transporter-dependence and a deiodinase step.
* **Decisive assumption, counter-evidence, experiment.** Not separately designed; T4 is included only as the physiological precursor control (T4 vs T3 in the same cells distinguishes transporter/deiodinase dependence from receptor dependence).
* **Missing data / feasibility.** Cheap; adds nothing the T3 arm does not, except the transporter question.

### 4.4 Sobetirome (GC-1) and its CNS-selective prodrug Sob-AM2

* **Identity and form.** Synthetic thyromimetic; clinical candidate in the past, not approved (flag blank in the release). Sob-AM2 is an amide prodrug described by the authors as CNS-selective.
* **Action and measured pharmacology.** Agonist. THRB Kd 0.068 nM; THRA 0.437 nM of **unrecorded type**: isoform selectivity unknown from the catalogue. The paper that would say more (PMID 30996143) was read only as an abstract.
* **CNS access.** "This problem is overcome with selective TH agonists, sobetirome and a CNS-selective prodrug of sobetirome called Sob-AM2" (abstract, author statement). Brain exposure values and the transporter route (whether MCT8-independent) were **not read**; a review (PMID 39485732) notes both compounds "have recently been tested in fetal and adult Mct8-deficient mice" without giving results in the passage read.
* **WWOX-relevant evidence.** None.
* **Precedent in another context.** TH and sobetirome promoted remyelination in gliotoxin models; chronic sobetirome or Sob-AM2 improved clinical signs and remyelination in a genetic demyelination model, whereas chronic TH made it worse (abstract only; adult demyelination, not neurodevelopment).
* **Inference chain.** Sobetirome -> TR agonist with reported CNS-selective delivery as a prodrug -> OPC differentiation -> in WWOX, maturation block release.
* **Decisive assumption.** As for Triac, plus: that the isoform profile reaches the TR alpha that OPCs rely on (unknown for sobetirome here).
* **Counter-evidence.** The "TH worsens, sobetirome improves" result points to isoform or tissue selectivity that was not examined here; no developmental or seizure data read.
* **Experiment.** The THRB-leaning arm of section 6.
* **Missing data / feasibility.** Availability of Sob-AM2 as a research compound not checked; may need a collaborator. Isoform profile and exposure unknown.

### 4.5 Resmetirom (MGL-3196)

* **Identity and form.** Oral THRB-selective agonist; approved for liver disease (catalogue flag yes). Designed for hepatic action; brain exposure **not established in any source read**.
* **Action and measured pharmacology.** THRB EC50 210 nM; THRA EC50 3740 nM; THRB 17.8x more potent than THRA at the same type (EC50). Assay class unknown.
* **CNS access.** Unknown. A PubMed search for "resmetirom brain" returned seven records, none opened.
* **WWOX-relevant evidence.** None.
* **Inference chain.** Resmetirom -> THRB agonist -> (if OPCs lack TR beta) no direct OPC action. The isoform data (PMID 11412031, abstract) predict **no OPC effect**, which makes resmetirom a useful **negative isoform control** rather than a candidate. That is a prediction to fix before testing: if resmetirom, at concentrations a TR beta-selective profile would cover, also shifts the ratio, the isoform argument is wrong or the compound is acting through TR alpha at high dose.
* **Decisive assumption.** That rodent isoform expression in OPCs transfers to human OPCs (the human OPC data read, PMID 29111262, show THRB transcript in the mixed neural culture; this is not an OPC-specific isoform measure).
* **Counter-evidence / opposite effects.** Chronic dosing safety in children: not looked up.
* **Experiment.** Isoform-selective control arm (section 6).
* **Missing data / feasibility.** Brain exposure, human OPC isoform expression. Compound is commercially available as a research reagent; not checked.

### 4.6 Others

Not considered further: DITPA (MCT8-independent analogue, tested in the Dko mouse and in the human OPC paper; shown there to be less effective than Triac on neuronal readouts at tested doses, PMID 36834863) is not in the requested set and has no catalogue value in this table. KB-141, VK2809 and the other rows of the table have only catalogue values and no primary source read. No compound beyond the five above is assessed.

## 5. Opposite effects and counter-evidence in one place

| Risk | What was read | Strength |
|---|---|---|
| Seizure threshold | Triac Trial I: seizure frequency rose in 3 of the patients with pre-existing seizures, with confounders named by the authors (PMID 31377265, full text read). Hyperthyroid adult rats were more susceptible to isoniazid and picrotoxin seizures (PMID 1513203, abstract). In the other direction, hypothyroid or low-T3 status is associated with seizure susceptibility in a genetic rat strain (PMID 3197682, abstract). | Weak, mixed, indirect. No study of a TR agonist in a Wwox-null seizure assay exists. A hyperexcitable, seizing brain is exactly the context where a thyromimetic effect on excitability is unmeasured. |
| Thyrotoxicosis | Trial I and cohort: mild transient signs at dose-escalated Triac in a thyrotoxic population; mouse paper: peripheral thyrotoxic readout at the effective dose. | Moderate for the signs, but the human data are from hyperthyroid MCT8 patients, not euthyroid children. |
| Thyroid axis suppression | Tshb undetectable in mice at the effective dose; TSH, free T4, total T4 and rT3 fall in humans; consequence in brain unknown (authors). | Moderate. |
| Premature OPC differentiation | Receptor overexpression accelerates OPC differentiation in culture; TR alpha1 level is "normally limiting" (PMID 12456652, abstract). A push without a pool of properly specified OPCs could deplete the pool. | Mechanistic risk, no WWOX datum. |
| Adult demyelination context | Chronic TH worsened remyelination in a genetic model (abstract only); a different context from development. | Weak transfer in either direction. |
| Window | Triac helped myelination only in postnatal weeks 1-3 in the Dko mouse; the Wwox-null mouse has no long postnatal window. | Moderate. |
| Isoform | OPCs express TR alpha mRNA and not TR beta mRNA (PMID 11412031, abstract); TR alpha is also the cardiac isoform (background knowledge, not read). | Moderate for the isoform fact (rodent, abstract), unverified for human OPCs. |
| Different mechanism of the precedent | MCT8 deficiency is a TH-entry defect; WWOX is not. | Structural weakness of the analogy. |

## 6. Minimum discriminating experiment

**Question.** Does a TR agonist shift OPC maturation specifically in the Wwox-deficient condition, in a seizure-free, hormone-defined dish?

**Design (existing assay, no new model).** The seizure-free neuron-OPC co-culture of Repudi et al. (E09 in the IT14 record): wild-type OPCs on Wwox-null versus wild-type (or add-back corrected) neurons, in a **T3-defined medium** (T3-deprived base, then defined concentrations; the first check is whether the published medium contains T3).
Arms per neuron genotype: (1) vehicle in T3-deprived medium; (2) T3 at a physiological-range concentration; (3) Triac; (4) a THRB-leaning agonist (resmetirom or sobetirome) as the **isoform-selective control**, at concentrations predicted from the typed values to separate the isoforms; (5) a TR antagonist or TR alpha-lacking OPCs, if available, as the loss-of-function reference (NH-3 is in the catalogue as an antagonist; not assessed).
**Readouts.** MBP+ morphology class (resting / contacting / ensheathing) and CC1+/PDGFRa+ counts, with **total lineage number** (Olig2 or SOX10) and an S-phase label reported beside the ratio; per-culture totals, not per-field. The IT14 record already flags that a ratio without a total can hide loss.
**Pre-registered predictions (IPOTESI).** If the block is TR-responsive: Wwox-null neuron condition has a lower MBP+ ensheathing share than wild-type, TR alpha-active agonists raise it toward wild-type, THRB-leaning agonist does less. 
**Results that weaken or close it.** (i) No shift in the null condition in any arm at any non-toxic dose: close the receptor-push line for development. (ii) A shift of equal size on wild-type neurons: a generic maturation push, not a rescue of a WWOX-dependent defect (non-specific; does not support the WWOX hypothesis). (iii) A ratio shift with fewer total MBP+ cells: not a rescue. (iv) A THRB-leaning agonist matching Triac: the isoform premise is wrong or off-target action at high dose; reinterpret. (v) Only an effect at doses far above the typed Kd/EC50 values: not a plausible exposure. (vi) A shift only in null neuron condition and abolished by TR antagonism: opens the pre-onset in-vivo question (the single most informative missing measurement of IT14, the pre-seizure lineage census).
**Not part of the minimum test (and not claimed):** seizure endpoints, exposure, in-vivo efficacy. Any in-vivo step needs a seizure-threshold arm because of section 5, and a pre-onset start because of the window.

**Replication caution carried from IT14:** the co-culture is one laboratory, n=4 v 4, DRG neurons; a negative here is therefore informative about the design, not final about WWOX.

## 7. Missing data and feasibility

* No WWOX datum on thyroid hormone signalling, TR isoform expression, transporter expression, or medium T3 in the existing co-culture. This is the cheapest gap: a record check and, if needed, a Wwox-null vs wild-type expression look for THRA, THRB, SLC16A2, SLCO1C1 in existing public snRNA data (not done here).
* No human brain exposure for any compound in this package. No primary report of Triac Trial II.
* The isoform fact rests on rodent abstracts; full texts of PMID 11412031 and 12456652 were not obtained (the full-text route returned an empty body for the second; the first has no PMC entry).
* Sobetirome and resmetirom primary pharmacology and CNS data not read.
* Seizure literature read is two abstracts and one trial safety section; it is not a systematic review.
* Feasibility: in-vitro test is cheap and uses an existing assay but needs hormone-defined medium and a collaborator for the co-culture; zero spend is possible only if the compounds are already on hand.

## 8. Per-compound summary table

Strength of evidence refers to the evidence that the compound helps *this* deficit, not that it works in the other disease. WWOX relevance: none of the five has a direct WWOX datum, so relevance is inferred only through the OPC-maturation mechanism.

| Compound | Novelty for LEGEND | Strength of evidence (for WWOX use) | WWOX relevance | Feasibility |
|---|---|---|---|---|
| Tiratricol (Triac) | **New molecule** (0 module records, IT21), **new relation** (compound to WWOX OPC maturation), **new context** (neuron-OPC co-culture); no combination | Low: mouse rescue and human safety exist in MCT8 deficiency (a different, entry-defect disease); no human neurological benefit shown; no WWOX data | Indirect: same two needs (myelin, PV) touched in another disease; mechanism-level only | In vitro: feasible, hormone-defined medium needed. In vivo: window and seizure risk unresolved |
| Liothyronine (T3) | **New molecule** (IT21), **new relation**; the physiological reference | Low: T3 drives OPC differentiation (abstract-level, rodent and human cells); counter-evidence in adult demyelination (abstract) | Indirect | Cheap in vitro, but medium T3 confounds; the natural-ligand reference arm |
| Levothyroxine (T4) | **New molecule** for the module, but **not a new mechanism** vs T3; adds a transporter/deiodinase step | Very low: failed in MCT8 deficiency for transporter reasons; no WWOX data | Indirect | Cheap; control arm only |
| Sobetirome / Sob-AM2 | **New molecule**, **new relation**; possible **new context** (development, not demyelination) | Low: promyelinating in adult demyelination models (abstract only); isoform selectivity unknown | Indirect | Compound availability unchecked; exposure data not read |
| Resmetirom | **New molecule**; value is as an **isoform control**, not a candidate | Very low as a candidate (liver-directed, THRB-preferring at EC50, CNS exposure unknown) | Indirect, negative-control role | Commercially available as a reagent (not checked); informative whichever way it comes out |

## 9. Papers read and depth

Every receipt is a JSON file in `receipts/`, one per paper, in the fixture format of the ledger plus a `verbatim_locators` list (exact quotes, machine-checked against the text served where it was saved to the scratchpad). The integrator records them; no receipt was appended by this package.

| PMID | Paper | Depth | Notes |
|---|---|---|---|
| 31377265 | Triac Trial I, Lancet Diabetes Endocrinol 2019 | partial (full text, no figures/tables/supplement served) | primary |
| 34679181 | Triac real-life cohort, J Clin Endocrinol Metab 2022 | partial (text, tables, legends; no supplement) | primary |
| 36834863 | Triac vs Ditpa in Mct8/Oatp1c1 Dko mice, Int J Mol Sci 2023 | partial (body and captions; results 2.2-2.4 keyword-scanned) | primary |
| 38963712 | ETA 2024 guideline, genetic disorders of TH transport | partial (MCT8 management section only) | secondary |
| 29111262 | hESC-OPC MCT8 and DITPA, EBioMedicine 2017 | partial (selected passages; discussion not read) | primary, DITPA not Triac |
| 39485732 | Review, MCT8 treatment | partial (Triac, Trial II, transporter paragraphs) | secondary |
| 12456652 | TR alpha1 and oligodendrocyte timing, EMBO J 2002 | abstract | full text served empty |
| 11412031 | TR isoforms in OPC differentiation timing, Dev Biol 2001 | abstract | no full text obtained |
| 30996143 | CNS-selective TH action and remyelination, JCI Insight 2019 | abstract | full text served empty |
| 1513203 | T3 and chemoconvulsants in rats, Life Sci 1992 | abstract | |
| 3197682 | Hypothyroid state in the genetically epilepsy-prone rat, Epilepsy Res 1988 | abstract | |

Not attributed as read: the WWOX papers behind the IT14 evidence (PMIDs 33914858, 34747138 and others) are cited only through the IT14 record; no re-reading was done here, and PMID 34747138 appears only through its abstract text. The DOI links for every paper are in the receipts. Citation of PubMed-sourced content: According to PubMed, e.g. [Trial I](https://doi.org/10.1016/S2213-8587(19)30155-X), [cohort](https://doi.org/10.1210/clinem/dgab750), [Dko mouse](https://doi.org/10.3390/ijms24043452), [JCI Insight](https://doi.org/10.1172/jci.insight.126329), [EMBO J](https://doi.org/10.1093/emboj/cdf662).

## 10. Limits

1. Triac Trial II results and any regulatory-approval detail were not found in the sources read; both are "unknown", not "none".
2. Isoform conclusions rest on rodent abstracts, one human mixed-culture transcript observation, and the catalogue; none is a human OPC isoform measurement.
3. The catalogue table has no assay class, species or tissue; no value is a basis for "more potent" between compounds.
4. The seizure evidence is thin and mixed; the absence of a Wwox-null seizure assay for any thyromimetic is the main safety gap.
5. This package did not run any computation beyond the unmodified class-alternatives table and did not touch any existing file.

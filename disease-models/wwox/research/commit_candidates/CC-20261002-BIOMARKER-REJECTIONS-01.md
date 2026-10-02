# COMMIT CANDIDATE — CC-20261002-BIOMARKER-REJECTIONS-01

**Candidate ID:** CC-20261002-BIOMARKER-REJECTIONS-01
**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-c`, 2026-10-02, intake wave 2026-10-02.
**Change class:** **MINOR.** Append-only into the non-canonical dismissal ledger. It touches no
canonical current file, narrows no claim, reverses none, and promotes nothing.
`context_policy: SOURCE_FIRST` — LEGEND_CORE §13 was read before the sources (it is the question);
no LEGEND biomarker record was opened until each source's first pass was written.

**Not medical advice.**

---

## 0 · The question this answers

*"For each source offering a WWOX-dependent readout: how was dependence shown, in what
cells/species/tissue, is it transcript / protein / functional, could it be sampled in a living
patient, and what is its §13 class?"*

**Answer, in one line: four sources offered eight candidate readouts and all eight fail §13. Not
one of them measures the functional state of WWOX, and not one is samplable from a living patient
in a form that would report on neural tissue.**

Per `epistemic_discipline` and the ledger's own founding argument — *a false negative is silent and
nobody retests it* — each rejection below is written with the premise it rests on, its boundary,
and the trigger that would revive it. **Four of the eight are rejected on a ground that could be
removed by future work and say so.**

## 1 · The readings this rests on

| Record | Receipt | Manifest |
|---|---|---|
| PMID 34204789 (Kałuzińska 2021, *Cancers*) | `FTR-20261002-34204789-01` | `PMID34204789.json`, strict PASS, 0 gaps |
| PMID 33195192 (Chou 2020, *Front Cell Dev Biol*) | `FTR-20261002-33195192-01` | `PMID33195192.json`, strict PASS, 0 gaps |
| PMID 37897534 (Cheng 2023, *CMLS*) | `FTR-20261002-37897534-01` | `PMID37897534.json`, strict PASS, 0 gaps |
| PMID 42395553 (Petrozziello 2026, **preprint**) | `FTR-20261002-42395553-01` | `PMID42395553.json`, strict PASS, 0 gaps |

## 2 · The eight candidates, scored against §13

| Candidate | How "WWOX-dependence" was shown | System | Type | Patient-samplable? | §13 |
|---|---|---|---|---|---|
| **PLEK2** | WWOX expression cut-point + Spearman R = −0.44 | bulk TCGA glioma | transcript | tumour tissue only | ❌ none |
| **RRM2** | same, R = −0.42 | bulk TCGA glioma | transcript | tumour tissue only | ❌ none |
| **GCSH** | same, R = +0.43 | bulk TCGA glioma | transcript | tumour tissue only | ❌ none |
| **pERK (Thr202/Tyr204)** | **constitutive `Wwox−/−` vs littermates** — a real perturbation | mouse epidermis, IHC | protein (phospho) | skin biopsy, yes; brain, no | ❌ fails specificity |
| **γ-H2AX** | knockout **and** knockdown **and** overexpression **and** applied protein | MEFs, HEK293T, SH-SY5Y, RPE-1 | protein (phospho) | no | ❌ **non-monotonic** |
| **SA-β-gal** | knockout + knockdown | MEFs, fibroblasts | enzymatic, live cells | no | ❌ generic |
| **p16 / p21 / p27** | knockout + knockdown | MEFs, fibroblasts | protein | no | ❌ generic |
| **Microsatellite instability** | knockout, passages 20–30 | MEFs | genomic | no | ❌ culture artefact |

### The one that is interesting enough to state carefully

🔴 **γ-H2AX is non-monotonic in WWOX, and that is a finding of this batch rather than of any one
paper in it.** It rises when WWOX is **lost** (Cheng 2023, late-passage `Wwox−/−` MEFs) and it rises
when WWOX is **added** (Petrozziello 2026, applied protein ≥100 ng/mL and stable overexpression).
Neither paper cites the other. A readout that moves the same way under opposite perturbations
cannot report the direction of the quantity it is supposed to measure — which disqualifies it
independently of any tier argument.

## 3 · Op — `dismissal_ledger_current.md`, APPEND to the end of the file

`old` (verbatim, the current final line of the file, measured unique):
```text
- **`REVIVAL_TRIGGER`:** confronto longitudinale o a età multiple, con unità animale e conteggi microgliali comparabili.
```

`new`:
```text
- **`REVIVAL_TRIGGER`:** confronto longitudinale o a età multiple, con unità animale e conteggi microgliali comparabili.

### DIS-022 — «PLEK2, RRM2 and GCSH are a WWOX-dependent biomarker triad» → ❌ **REJECTED — the dependence was never tested**
- **PREMISE: DATO** (2026-10-02, `CC-20261002-BIOMARKER-REJECTIONS-01`, from a complete read of PMID 34204789, receipt `FTR-20261002-34204789-01`). "WWOX-dependent" in that title means two things and neither is a perturbation: patients were split on a **WWOX expression cut-point** in bulk tumour RNA-seq (*«Optimal WWOX expression cut-point was determined to separate high- and low-expressing groups of patients. The obtained cut-off value, 222.6, had significantly separated groups»*), and the three genes were then ranked by **Spearman correlation with WWOX transcript abundance** (|R| = 0.42–0.44). **There is no knockdown, no overexpression, no rescue and no protein measurement anywhere in the study.**
- **§13:** fails at the first clause — a second transcript co-varying with WWOX transcript across bulk tumours measures neither WWOX protein, nor WWOX activity, nor anything perturbed by changing WWOX. Not Tier 1, not Tier 2 (the causal linkage is the untested part), not Tier 3 (it is not a clinical endpoint either). Every reported AUC discriminates a **tumour class**, never a WWOX state. Sampling requires tumour tissue.
- **Confine:** the work is not weak inside its own frame — glioma classification — and the authors do not overclaim: *«usefulness of PLEK2 , RRM2 , and GCSH as diagnostic or predictive biomarkers is yet to be confirmed»*. What is rejected is the transfer of a title to this model.
- **`REVIVAL_TRIGGER`:** any experiment in which WWOX is actually perturbed in a neural system and one of these three is measured as a response.

### DIS-023 — «pERK is a candidate WWOX biomarker» → ❌ **REJECTED as a disease biomarker; RETAINED by name as a possible pharmacodynamic readout**
- **PREMISE: DATO** (2026-10-02, from a complete read of PMID 33195192, receipt `FTR-20261002-33195192-01`). Here the dependence **was** tested — constitutive `Wwox−/−` mice against littermates — and the result is real: *«keratinocytes expressed significantly reduced levels of pERK and total ERK1/2 protein»*, by immunohistochemistry quantified over 25 regions from 3 mice. ⚠️ The **total**-ERK half sits in Supplementary Figure S9, which was not read; only the running-text assertion is receipted.
- **§13:** Tier 2 **by position** in the pathway and **failing on specificity**. MEK/ERK phosphorylation reports hundreds of upstream inputs, and a fall in pERK is the ordinary accompaniment of the reduced proliferation this tissue also shows, so the readout cannot distinguish "WWOX is low" from "these cells are dividing less". Measured in mouse skin of a constitutive null; no human WWOX-DEE tissue has been assayed for it anywhere in the source or its citations.
- **Confine, and the half that is NOT rejected:** skin is accessible by punch biopsy in a living patient, unlike brain — which is why this is the only candidate in the batch with any sampling route at all. It is **retained by name as a possible *pharmacodynamic* readout inside a controlled experimental system**, where the perturbation is known and pERK is read as a response. That is a different use from a patient biomarker and must not be conflated with one. 🔴 No CSF, blood or imaging route exists for it.
- **`REVIVAL_TRIGGER`:** a demonstration that pERK in an accessible tissue tracks WWOX functional state **across a restoration**, not merely across a null-versus-wild-type contrast.

### DIS-024 — «γ-H2AX can report WWOX state» → ❌ **REJECTED — the readout is NON-MONOTONIC in WWOX**
- **PREMISE: DATO** (2026-10-02, from two complete reads in the same wave: PMID 37897534, receipt `FTR-20261002-37897534-01`, and PMID 42395553, receipt `FTR-20261002-42395553-01`). γ-H2AX rises when WWOX is **lost** — *«was highly expressed in late-passage Wwox −/− MEFs»* — and rises when WWOX is **added**, both as applied recombinant protein above a 10–100 ng/mL threshold and as a stable transgene (⚠️ the second source is a **bioRxiv preprint, NOT peer reviewed**, and its neuronal arm uses extracellular applied protein with no heat-denatured or endotoxin control reported). **Neither paper cites the other; the observation belongs to reading them together.**
- **§13:** not a gene readout (Tier 1); not specific to any WWOX-proximal pathway (Tier 2) — it is the generic double-strand-break marker; and disqualified independently of tier because **a readout that moves the same way under opposite perturbations cannot report the direction of the quantity it measures**. Requires fixed cells; no neural sampling route in a living patient.
- **Confine:** this does **not** say either observation is wrong, and it does not say WWOX is unrelated to DNA damage. It says γ-H2AX cannot serve as the instrument.
- **`REVIVAL_TRIGGER`:** a dose–response in **one** system spanning WWOX-null through wild type to overexpression, showing a monotonic γ-H2AX relation — which would mean one of the two observations above is an artefact and would identify which.

### DIS-025 — «SA-β-gal, p16/p21/p27, or microsatellite instability are WWOX biomarkers» → ❌ **REJECTED — generic, and not samplable**
- **PREMISE: DATO** (2026-10-02, from a complete read of PMID 37897534, receipt `FTR-20261002-37897534-01`). All four respond to WWOX loss in that system, and the perturbation is genuine (knockout plus knockdown). ⚠️ The comparator in most of its figures is `Wwox+/−`, **not** wild type.
- **§13:** SA-β-gal is a generic senescence stain requiring live cultured cells; p16/p21/p27 are generic cell-cycle inhibitors measured by western in fibroblasts; microsatellite instability was accumulated over passages 20–30 in culture and is a property of that regime as much as of the genotype. None is a WWOX readout; none has a patient sampling route for neural tissue.
- **Confine:** the **NAC rescue** in the same paper is a therapeutic-direction lead, not a biomarker, and is deliberately not promoted here — it is a fibroblast-culture result with no neural and no in vivo arm, recorded in `disease-models/wwox/research/intake_wave_20261002_C.md`.
- **`REVIVAL_TRIGGER`:** none of these four is expected to revive as a biomarker; the entry exists so that the next session does not re-triage the paper's abstract hopefully.
```

## 4 · Deliberate non-ops

- **Nothing is promoted.** Not one candidate reached §13 Tier 1 or Tier 2, so no biomarker record is
  created and `clinical_monitoring_endpoints` is untouched.
- **No canonical file is edited.** The dismissal ledger is the non-canonical, append-only home for
  negatives; the four canonical current files are not touched by this candidate.
- **The Flex1 AT-repeat length (PMID 17679088) is deliberately NOT entered here.** It is neither a
  biomarker nor a rejected biomarker — it is a constitutional sequence polymorphism, a candidate
  *risk-of-rearrangement covariate*, and entering it in a biomarker ledger in either direction
  would miscategorise it. It is recorded as a lead in the analysis note.

---

### LOCATOR TRIPLES FOR BLIND AUDIT

(Artifacts confirmed present on disk, SHA-256 verified, every snippet matched character-exact by
`deepdive_manifest.py --verify-artifacts`. ⚠️ The `PMID42395553…txt` surface spells the Greek gamma
as a Latin `g`. ⚠️ The `PMID37897534…xml` surface separates the genotype token's minus signs.)

1. (The two expression groups were defined by a cut-point on the gene's own expression level | `Optimal WWOX expression cut-point was determined to separate high- and low-expressing groups of patients. The obtained cut-off value, 222.6, had significantly separated groups` | `files/fulltext/PMID34204789_Kaluzinska2021_PMC.xml` · Results 2.1, first sentence)

2. (The relationship between the candidate genes and WWOX was a rank correlation | `was used to correlate the top genes with WWOX using Spearman's rank correlation coefficient.` | `files/fulltext/PMID34204789_Kaluzinska2021_PMC.xml` · Materials and Methods 5.8)

3. (The sample set was public tumour expression data and the cut-point tool was the authors' own | `A total of 672 samples were included in the study. Determining the suitable WWOX expression cut-point to stratify the population into two groups was achieved with the help of the R-based Evaluate Cutpoints tool designed in our Department` | `files/fulltext/PMID34204789_Kaluzinska2021_PMC.xml` · Materials and Methods 5.1)

4. (The authors state the three genes are not yet established as usable biomarkers | `usefulness of PLEK2 , RRM2 , and GCSH as diagnostic or predictive biomarkers is yet to be confirmed` | `files/fulltext/PMID34204789_Kaluzinska2021_PMC.xml` · Conclusions, penultimate sentence)

5. (Both the phosphorylated and the total form of the kinase were lower in the knockout tissue | `keratinocytes expressed significantly reduced levels of pERK and total ERK1/2 protein` | `files/fulltext/PMID33195192_Chou2020_PMC.xml` · Results, "Wwox Loss Reduces E-Cadherin, ERK, and p63 Expression in Keratinocytes")

6. (The DNA-damage marker was elevated in the late-passage knockout cells | `was highly expressed in late-passage Wwox −/− MEFs` | `files/fulltext/PMID37897534_Cheng2023_PMC.xml` · Results, first results section, γH2AX paragraph)

7. (An antioxidant prevented the instability and restored the arrest phenotype in those same cells | `during the passage culture prevented microsatellite instability and resulted in senescence induction in the late-passage Wwox −/− MEFs` | `files/fulltext/PMID37897534_Cheng2023_PMC.xml` · Results, final results section)

8. (In a different system the same DNA-damage marker rose above a concentration threshold of added protein | `While treatment with 10ng/mL of rWWOX did not alter g-H2AX levels (Tukey's test, p=0.6018), treatment with either 100ng/mL (Tukey's test, p=0.0139) or 150ng/mL of rWWOX (Tukey's test, p=0.0038) significantly increased g-H2AX levels compared to vehicle-treated cells.` | `files/fulltext/PMID42395553_Petrozziello2026_bioRxiv.txt` · Figure 5 legend, panel B)

9. (Raising the protein by transgene also raised that marker, as a stated increase over the untransfected control | `WWOX levels were significantly increased in SH-SY5Y overexpressing WWOX (WWOXOE) cells compared to NTC (Mann-Whitney U test=1, p=0.0476)` | `files/fulltext/PMID42395553_Petrozziello2026_bioRxiv.txt` · Figure 5 legend, panel C)

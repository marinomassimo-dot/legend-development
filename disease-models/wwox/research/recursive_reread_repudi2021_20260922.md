# RECURSIVE RE-READ TEST — Repudi 2021 (PMID 34747138) under the Purkinje question

**Directive:** §15 (recursive re-read), continuation directive §15 (recursive re-read test).
**Date:** 2026-09-22 · **Actor:** Orchestrator (not delegated)
**Test being run:** `OLD PAPER + NEW QUESTION → NEW SCIENCE`.
**Scoring rule, fixed in advance:** simple rediscovery of a fact already recorded in this
repository scores `NO NEW INFORMATION`, however interesting the fact is.

---

## §1 · Paper selected, and why

**PMID 34747138** — Repudi S, Kustanovich I, Abu-Swai S, Stern S, Aqeilan RI, *Neonatal neuronal
WWOX gene therapy rescues Wwox null phenotypes*, EMBO Mol Med 2021;13(12):e14599.

Selection criteria, all four met:
1. **Already completely read.** `complete_fulltext_read`, receipt `FTR-20260810-34747138-01`,
   JATS XML PMC8649866, 20 verified locators in `deepdive_manifests/PMID34747138.json`,
   validator PASS, 0 gaps. It is not a paper this session has been working on: the last read
   was six weeks ago, for a different purpose.
2. **The first read had a declared and different purpose** — gene-therapy design principles:
   dose, route, timing window, myelination, oligodendrocyte non-cell-autonomy, the missing
   WT comparator, the oncology non-signal.
3. **It is upstream of both of today's live questions.** It is the parent study of the
   AAV9-hSynI-WWOX strategy that TX-007 extends.
4. **It is not the paper this session already has open.** TX-007 (PMID 42422765) has been read
   four times in this session; re-reading it would test recency, not recursion.

---

## §2 · THE NEW QUESTION — written BEFORE re-reading

> **Repudi 2021 rescues ataxia with a neuron-restricted vector, and reports its transduction
> efficiency as a NeuN⁺WWOX⁺ double-positive percentage. NeuN does not label Purkinje cells.
> So: does this paper contain any measurement that can see the cerebellar cell type its own
> behavioural rescue implicates — or is its founding efficiency number, like TX-007's, a
> measurement made in a compartment that structurally excludes Purkinje cells?**

Three sub-questions, fixed now:

- **Q-A · Denominator.** What exactly was the 60–70% counted in — which region(s), which
  sections, which antibody, which denominator? If the region is forebrain, the number says
  nothing about cerebellum and the paper's own scope is narrower than its title.
- **Q-B · Cerebellar evidence.** Is there ANY cerebellum-resolved WWOX measurement in the
  paper (protein, transcript, vector genome, cell count), as opposed to the MBP myelin panel
  that merely includes a cerebellar inset?
- **Q-C · The rescue-without-the-cell-type problem.** If motor/ataxia phenotypes improve while
  no cerebellar WWOX restoration is demonstrated, what are the admissible explanations, and
  does the paper distinguish between them?

---

## §3 · Baseline — what this repository already held before the re-read

Declared in full, so that nothing recovered below can be scored as new if it was already here.

- `paper_registry_current.md` PAPER 005: ICV P0, single injection, ~1 µl / 2 × 10¹⁰ GC per
  hemisphere, free-hand; **60–70% of neurons transduced, not near-total**; oligodendrocytes
  never transduced; myelin restored non-cell-autonomously; g-ratio normalises; WT-vs-rescued
  comparator largely absent; n = 3 per genotype in EM; P0-only window declared as future work;
  oncology non-signal with three qualifiers.
- `PMID34747138_locators.md:95` holds the verbatim: *"The percentage of NeuN and WWOX
  double-positive cells was calculated and found to range between 60 and 70%"* — so the
  repository already knows the efficiency figure is **NeuN-gated**. It does **not** record
  which region it was counted in.
- The manifest mentions `cerebellum` exactly twice, both in the **same** MBP-myelin figure
  attestation (sagittal panels, cortex / hippocampus / cerebellum insets). `Purkinje` appears
  **zero** times anywhere in this repository in connection with this paper.
- Today's independent finding, from Scientist H's wave and verified first-hand: NeuN
  (Rbfox3) has failed to label Purkinje cells since Mullen 1992, and also fails on cerebellar
  basket cells — so a NeuN-gated percentage in cerebellum is a granule-cell measurement.

**Therefore, to score above `NO NEW INFORMATION`, the re-read must return something that is
not in the list above.** Recovering "60–70%, NeuN-gated" again scores `NO NEW INFORMATION`.

---

## §4 · Predictions, fixed before re-reading

| # | Prediction | Falsifier |
|---|---|---|
| P1 | The 60–70% is counted in **cortex and/or hippocampus only**, not cerebellum | Methods or legend names a cerebellar count |
| P2 | The paper reports **no** cerebellum-resolved WWOX protein or transcript quantification | Any cerebellar WWOX western/qPCR/cell count |
| P3 | The word **Purkinje** does not appear in the paper at all | It appears |
| P4 | A motor/ataxia phenotype **is** reported as improved | No motor endpoint is reported |
| P5 | The paper does **not** distinguish cerebellar-autonomous from forebrain-mediated motor rescue | An explicit discrimination is attempted |

P1–P3 and P5 are predictions of **absence**, and absence in this corpus is only assertable
after a *read*, never after a query returning zero (six proven failure modes). The re-read is
therefore the instrument, and the negative — if it survives — carries `PREMISE: METHODS_INVISIBLE`
or `NOBODY_LOOKED` as appropriate, never "not present".

---

## §5 · Re-read record

**Route:** `mcp__PubMed__get_full_text_article`, PMC8649866, 2026-09-22. According to PubMed,
[DOI](https://doi.org/10.15252/emmm.202114599). Body, all figure legends, Discussion and full
Methods returned. **Appendix Figs S1–S6 and Appendix Table S1 were NOT returned** and were not
read — every Appendix-dependent statement below is flagged.

### §5.1 · The predictions, scored

| # | Prediction | Outcome | Evidence |
|---|---|---|---|
| P1 | 60–70% counted in cortex/hippocampus only | 🔴 **REFUTED** | Fig 1E legend: *"the percentage of NeuN and WWOX double‐positive cells in different parts of the brain (**cortex, hippocampus, and cerebellum**)"*; Fig 2G: *"at different parts (cortex, hippocampus, and cerebellum) of the KO brain at P19"* |
| P2 | No cerebellum-resolved WWOX measurement | 🔴 **REFUTED** | Fig 2F is a dedicated **cerebellum** immunofluorescence panel, scale bar 50 µm; Results: *"Specific neuronal WWOX expression was detected in cortex …, hippocampus …, and cerebellum"* |
| P3 | "Purkinje" does not appear | 🟢 **SUPPORTED** | Zero occurrences in abstract, Introduction, Results, all six figure legends, Discussion and Methods. ⚠️ Appendix not retrieved, so the negative is bounded to the retrieved surface |
| P4 | A motor/ataxia endpoint is reported as improved | 🟢 **SUPPORTED** | Hindlimb clasping (Appendix Fig S3, **unread**); rotarod Fig 6J,K; ataxia in the abstract's rescue list |
| P5 | No discrimination of cerebellar-autonomous vs forebrain-mediated motor rescue | 🟢 **SUPPORTED** | Absent from Results and Discussion; the Discussion's only regional statement is *"WWOX is ubiquitously expressed in all brain regions"* |

**P1 and P2 were refuted in the direction that makes the problem worse, not better.** I predicted
the paper would be silent on cerebellum. It is not silent: it measured cerebellum, put it in two
figures, and used a gate that cannot see the cell type at issue.

### §5.2 · What the re-read actually returned

**🔴 F1 — the blind spot is not TX-007's; it is the program's, and it was there at the founding
study.** Repudi 2021 reports its transduction efficiency as `NeuN⁺WWOX⁺` double-positive cells in
**three regions including cerebellum** (Figs 1E, 2F, 2G), and states the result only as a range:
*"The percentage of NeuN and WWOX double‐positive cells was calculated and found to range between
60 and 70%."* NeuN does not label Purkinje cells — a property of the antigen reported since
Mullen 1992, verified first-hand earlier in this session. Therefore **the cerebellar number in
the 2021 proof-of-concept is, like TX-007's ≈61%, a measurement of the NeuN-positive cerebellar
population — overwhelmingly granule cells — and is inapplicable to Purkinje cells.** The same
instrument, the same gate and the same inapplicability appear in the parent study five years
earlier. `PREMISE: NOBODY_LOOKED` for Purkinje transduction now covers the **whole** AAV9-hSynI-WWOX
programme, not one paper.

⚠️ **Two boundaries, both declared rather than assumed.** (i) The per-region values live in the
bar graphs; the **text gives only the 60–70% range across three regions and two vectors**, so the
cerebellar value itself is a figure datum this read did not open. (ii) The antibody clone for
*this* paper is in Appendix Table S1, **not retrieved** — so "clone A60" is `UNVERIFIED` here. The
Purkinje-negativity invoked above is an **antigen-level** property, not a clone-level attribution
to this paper. `REVIVAL_TRIGGER`: Appendix Table S1.

**🟡 F2 — the physiological rescue is neocortical only, and the coordinates say so.** Methods,
*Cell-attached recordings*: *"The electrode was inserted at a 45 degrees angle and reached a depth
of 300 µm. The electrode positioning was targeted on the brain surface, positioned at 1.6–2 mm
posterior to the bregma and 4 mm lateral to the midline."* Fig 3A legend: *"Traces represent
spontaneous **neocortical** activity."* Fig 3D speaks of *"adult WT and KO+A‐mWwox **cortical**
neurons."* **There is no cerebellar electrophysiology in this paper.** `bregma` occurs **zero**
times anywhere in this repository before today, so the coordinates are new here.

Joined to F1: in the founding study, the cerebellum has been examined with **one** instrument
(a NeuN-gated cell count) that structurally cannot see Purkinje cells, and with **zero**
physiological instruments. Anatomy and physiology are blind in the same place.

**🟡 F3 — the behavioural battery has no untreated comparator, and the paper says why.** Results,
*Behavioral and motor functions*: *"Unfortunately, we could not assess behavior of Wwox‐null mice
due to their poor conditions and premature death. We hence performed open‐field, elevated plus
maze (EPM), and rotarod tests to examine anxiety and motor coordination in **WT and rescued
mice**."* So the rotarod result — the only instrumented motor-coordination measurement in the
paper — is **rescued-vs-WT only**, read from a non-significant difference, with no pre-specified
equivalence margin (`n` = 7 F / 6 M WT vs 7 F / 5 M rescued). The repository already held the
identical structure for the **adult electrophysiology** (`L7` of `PMID34747138_partial_locators.md`,
*"by necessity, not by omission"*). It did **not** hold it for the behavioural battery, which is
the endpoint the ataxia claim rests on. Statistical class per §4: **NOT TESTED** against KO —
`DESCRIPTIVELY EQUIVALENT` to WT. This is a limit of the model, not a fault of the authors: the
untreated animals were dead.

### §5.3 · What the re-read returned that the repository already had — scored as zero

Declared because the test is worthless if rediscovery is allowed to count.

- **Exit accounting of the survival curves** (Fig 1C *"total n = 18, spontaneously dead n = 6,
  mice taken out … n = 12"*; Fig 2C *"total n = 16, alive n = 6, spontaneously dead n = 6, 4 …
  taken out"*). Already in `full_text_queue_current.md:5950`, `CC-20260826-DOSE-ADJUDICATION-01`,
  `CC-20260826-DOSE-DECISION-TABLE-01`, `CC-20260826-FIVECLAIM-HARDENING-01` and
  `CC-20260922-TX007-DOSE-CHALLENGE-01`. **`NO NEW INFORMATION`.**
- **CNS-only restoration normalises glucose, Leydig cells, fertility and cortical bone.** Already
  in `PMID34747138_partial_locators.md`. **`NO NEW INFORMATION`.**
- **60–70%, NeuN-gated.** Already at `PMID34747138_locators.md:95`. **`NO NEW INFORMATION`** — the
  new part is the *region list*, not the number.

### §5.4 · 🔴 A defect in my own baseline, recorded rather than repaired quietly

§3 was built from `PMID34747138_locators.md` and `deepdive_manifests/PMID34747138.json`. It
**missed `PMID34747138_partial_locators.md`**, a second dossier for the same PMID holding L1–L9.
Had I not re-grepped after the re-read, the Leydig / bone / glucose findings and the WT-only
comparator structure would have been scored as new. Two rediscoveries would have been graded as
discoveries.

The test caught it only because §3 fixed a written baseline that could be re-checked afterwards.
**The generalisable rule: one PMID can hold more than one dossier in this repository, and a
baseline built by filename guess is not a baseline.** A `census_verify`-style enumeration —
*list every file whose name contains the PMID* — is the correct instrument and costs one command.

---

## §6 · Classification

### Verdict: **`NEW CONNECTION`**

**Not `EXPERIMENT-CHANGING INSIGHT`, and the reason is a rule I fixed before running the test.**
The experiment this re-read points to — calbindin / `PCP2` / `Car8` co-stain with anti-WWOX on
cerebellar sections — was already named **today**, in queue entry `FT-148`, with the same
`PREMISE: NOBODY_LOOKED` and the same `REVIVAL_TRIGGER`. Arriving at an experiment that is already
written down is not changing which experiment a scientist should do. Grading it higher would be
exactly the self-flattery the pre-registered rule exists to prevent.

**What the connection genuinely adds over `FT-148`:**

| | `FT-148` held | This re-read adds |
|---|---|---|
| **Scope** | the gate is a defect in TX-007's ≈61% | the **same gate is in the 2021 founding study**, applied to the same three regions — so it is a programme-level convention, inherited unchanged across five years and two papers |
| **Material** | TX-007's sections | a **second, older, independent archive**: P17/P19 sagittal sections, `n` = 3 per vector, two vectors, cerebellum demonstrably in frame (Fig 2F) — held by the originating laboratory |
| **Axis** | transduction (anatomy) | **physiology is blind in the same place** — every recording in Repudi 2021 is neocortical by stated coordinates; a Purkinje-resolved *functional* readout is a different and also-unperformed experiment |

**What does not change.** No claim about Purkinje transduction becomes assertable. Nothing here
shows Purkinje cells are poorly transduced; it shows, twice over, that nobody has measured it.
`hSynI` promoter activity in Purkinje cells is likewise unmeasured in both papers and is
**not** established by this re-read. The ataxia rescue in Repudi 2021 stands as reported —
what is now precisely bounded is the set of measurements that could have explained *where* it
comes from, and that set is empty on the cerebellar side.

### The test's own result

`OLD PAPER + NEW QUESTION → NEW SCIENCE` **worked, and its yield was concentrated in one thing
the first read had no reason to look at**: a figure-legend region list. The first read (2026-08-10)
was hunting comparators, dose and myelination; it extracted the 60–70% sentence verbatim and
correctly, and had no reason to ask *which regions*. The question, not the reading effort, is what
was missing.

**Cost:** one full-text fetch, one baseline enumeration, ~20 minutes. **Yield:** one programme-level
scope correction, one new blind axis, one new archival material source, and one recorded defect in
my own method. **Recommendation: the recursive re-read is worth keeping as a primitive**, on the
evidence of this single instance plus the honest observation that three of its five returns were
zero — a primitive that returns zero when it should is more trustworthy, not less.

`REVIVAL_TRIGGER` for this file: Appendix Table S1 (antibody clone) or Appendix Fig S3 (clasping
test comparator) becoming retrievable; per-region values in Fig 1E / 2G becoming readable.

# `DEVELOPMENTAL_TIMING_EARLIEST_LESION` — what goes wrong first in WWOX deficiency, and is anything reachable before it?

**Date:** 2026-09-21 · **Actor:** Scientist B · **Node:** `DEVELOPMENTAL_TIMING_EARLIEST_LESION`

> **Non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, the registries and every
> ledger. Nothing here changes a claim, a paper record, the working model or the tracking log.
>
> **Public edition.** Disease-level reasoning over the WWOX-DEE genotype class. No individual is described.
>
> **Nothing here is medical advice.** No dose, schedule, timing or clinical recommendation is formulated anywhere
> in this file. Nothing here supports or implies any statement about prenatal decision-making.

---

## 0. Read depth declared up front

| PMID | Identity | Depth **in this session** | Returned body length | Figure access |
|---|---|---|---|---|
| **32000863** | Cheng/Chang *et al.* 2020, *Acta Neuropathol Commun* — *Wwox*-null mouse | body **read in-act** (Wave 2 fetch, re-analysed here for stage tokens) | ≈24 000 characters (approximate; not instrumented) | none. Panel values from LEGEND manifest `PMID32000863.json` (25 entries; receipt `FTR-20260804-32000863-01`, `complete_fulltext_read`) |
| **34747138** | Repudi *et al.* 2021, *EMBO Mol Med* | body **read in-act** (Wave 2 fetch, re-analysed) | ≈19 000 characters (approximate) | none |
| **42422765** | Obeid *et al.* 2026, *Mol Ther Oncol* | body **read in-act** (Wave 3 fetch, re-analysed) | **48 780 characters (measured exactly)** | none. Panels from manifest (29 entries) |
| **32581702** | Iacomino *et al.* 2020, *Front Neurosci* — `lde` rat + **human fetal tissue** | 🔴 **not re-fetched.** Worked from receipt `FTR-20260810-32581702-01` (`complete_fulltext_read`) and its **21-entry** manifest | 0 bytes this session | none. Every value is a **prior-session figure attestation**, attributed as such |
| **42397075** | Steinberg … Aqeilan 2026, *Brain* | 🔴 **not fetchable — no PMCID exists.** Receipt `FTR-20260810-42397075-04`, **30-entry** manifest | 0 bytes | none. Prior-session attestations only |
| 31543760 · 19936220 · 17803050 · 25649963 · 34634460 · 34268881 | LEGEND-held reads, all receipt-backed | manifests + receipts consulted | n/a | n/a |
| **25866966 · 17289941 · 31704158** | Task-4 precedents (Angelman, Rett, SMA) | **metadata + abstract, in-act** | n/a | n/a |
| — | 4 PubMed queries (WWOX × prenatal/intervention; Angelman windows; Rett reversal; SMA presymptomatic) | executed | see §4 | n/a |

🔴 **Stage tokens were treated as doses, per the node brief — and the extractor check was run.** In the three
bodies read in-act, the developmental designations `E12.5`, `E16.5`, `P0`, `P1`, `P14`, `P17`, `P20`, `P300`,
`30 hpf` all survive extraction intact: they are **roman-type alphanumerics, not superscripts**, so the defect
that destroyed `1.23 × 10¹¹ vg` → `1.23 × 10vg` does **not** damage them. Two adjacent tokens *were* damaged and
are flagged where used: `2 × 10¹⁰ GC/hemisphere` and the `Ca²⁺`/`Wwox−/−` superscripts. **Stage notation in this
literature is safe to quote; vector-genome and genotype superscripts are not.**

---

## 1. The direct answer

**The honest headline is not about onset. It is about looking.** In the mammal, **the earliest anyone has ever
examined a WWOX-deficient brain is embryonic day 12.5**, and at that first look the embryo is **already
abnormal** — smaller, growth-delayed, with an elongated roof plate and dorsal spinal-cord malformation. In the
human, **the earliest anyone has ever examined WWOX-deficient brain tissue is the twenty-first gestational
week**, in a single neuropathological specimen whose control *n* the paper states inconsistently (one fetus in
Methods, three in Results), and at that first look the cortical layering is **already abnormal**. **Every
mammalian WWOX timepoint on record is the earliest anyone MEASURED, not the earliest the defect EXISTS** — and
the mouse paper itself reports that *"some very severely affected embryos died embryonically"*, which places a
lesion earlier than any examination. The ordered sequence that is actually measured runs: gross embryonic
malformation (**E12.5**) → reduced progenitor proliferation and thinner cortex (**E16.5**) → arrested migration
of neurons born at E16.5, read at **P1** in the rat and at birth in the mouse → delayed neuronal maturation
(**P14**) → spontaneous seizures (**after P12**) → electrographic spikes and SWDs (**from P14**) → hypomyelination
(**P17**) → systemic metabolic collapse (**P18**) → death (**~P21–P28**). **Every therapy in the portfolio acts at
or after the fifth step.** The human gene-therapy window (P0–P5 in mouse) opens **two weeks after** the first
measured lesion. And nothing reaches it: the organoid gene-therapy arm *"rescued neuronal functional phenotypes
without correcting RG abnormalities"*; A51 normalised progenitor identity and pan-neuronal marking but **not**
layer-neuron output; and **no intervention of any kind has ever been delivered prenatally in any WWOX model** —
the census returns **zero**. The one thing this node cannot deliver is a gestational date for the organoid
progenitor phenotype: the paper built the apparatus for it (correlation against four independent human fetal
references) and **LEGEND's record does not capture which reference the organoids match**, so the mapping is
stated as unavailable rather than guessed.

---

## 2. Task 1 — the timeline, with measurement and looking kept separate

**Reading rule for this table.** `Measured stage` is the stage at which the abnormality was demonstrated.
`Earliest anyone looked` is the earliest stage examined **in that model, in that study**. Where the two are equal,
🔴 **the finding is a detection limit, not an onset.**

| Model | Earliest measured abnormality | Measured stage | Earliest anyone looked | Onset or detection limit? | Surface |
|---|---|---|---|---|---|
| **Mouse, germline *Wwox*-null** (32000863) | embryos **smaller, growth-delayed**; **elongated roof plate and dorsal spinal-cord malformation** | **E12.5** | **E12.5** | 🔴 **DETECTION LIMIT.** Nothing earlier was examined in any WWOX mammalian model | `body`, in-act |
| same | *"some very severely affected embryos died embryonically"* | **unspecified, < E12.5 by implication** | never examined | 🔴 **A lesion earlier than any examination, stated and never followed up** | `body`, in-act |
| same | **↓Ki-67⁺ proliferating cells** in neocortical SVZ and cerebellum; **↓cortical thickness** | **E16.5** | E12.5 | measured | `body`, in-act; panel from prior session |
| same | BrdU pulse at E16.5 → at **birth** a large proportion of nascent neurons still in VZ/SVZ; more Ki-67⁺ in VZ/SVZ | **E16.5 → P0** | — | measured | `body`, in-act |
| same | gross brain malformation **from live births**, microcephaly to **holoprosencephaly** | **birth** | — | measured; a forebrain-**patterning** defect, not only migration | `body`, in-act |
| same | **DCX still high** at P14 (maturation delayed, not merely reduced) | **P14** | — | measured | manifest entry 13 |
| same | **spontaneous epileptic seizures** *"commonly observed after postnatal day 12"* | **> P12** | — | measured | `body`, in-act |
| same | GSK3β Ser9 dephosphorylation, cerebellum/hippocampus/cortex | **P20** | — | measured | manifest entry 2 |
| ***lde/lde* rat** (32581702) | **migration arrest**: BrdU⁺ cells shifted, **8 of 10 cortical zones significant** (zones 1,2,5,6,7 at p<0.01; 4,9,10 at p<0.05) | **E16.5 BrdU → P1** | E16.5 | measured. ⚠️ `n = 3` per genotype, stated once in Methods and nowhere in Results | `figure-attestation-from-prior-session` |
| same | 🟢 **the cortical wall is NOT thinner** — panel 3E carries no marker and the text agrees | E16.5 → P1 | — | **a tested negative**, and it is what makes this a migration phenotype rather than a growth one | `figure-attestation-from-prior-session` |
| **Human fetal brain, WWOX-deficient** (32581702) | **defective architecture of cortical layers**; external granular layer described as having migrated into the molecular layer | 🔴 **21st gestational week** | 🔴 **21st gestational week — the earliest any human WWOX-deficient brain has ever been examined** | 🔴 **DETECTION LIMIT, and a severe one.** ⚠️ Methods say **one** control fetus, Results say **three** fetuses; Figure 2A's caption sides with the singular. ⚠️ Layers are labelled **only on the control**, so the abnormal specimen's layer identification is asserted, not shown | `body` + `figure-attestation-from-prior-session` |
| **Human organoids, WWOX-KO + WOREE + SCAR12** (42397075) | **MYC up in radial glia in all three lines** (pseudobulk log2FC ≈1.8 / 1.65 / 1.6); RG/neuron composition shift in KO; cell-cycle shift toward S/G2M in KO | organoid **weeks 8 → 15/16** | week 8 (earliest timepoint appearing in LEGEND's read) | 🔴 **no gestational date — see §3** | `figure-attestation-from-prior-session` |
| **hNPC, shRNA knockdown** (31543760) | cells stay as isolated single cells in a 3D ECM scaffold; ↓pro-MMP2 | 🔴 **no developmental stage at all** — a culture system | n/a | 🔴 **Not a timepoint.** LEGEND's audit already records: **no migration assay, no layering readout**, the same-cells 2D panel shows nothing, and one claim rests on a band not visible in the gel shown. **Do not place this on a developmental timeline** | `figure-attestation-from-prior-session` |
| **Mouse, systemic** (19936220) | body weight **already below wild type at day 3** (≈1.65 g vs ≈2.35 g) | **P3** | P3 | measured — and the earliest *systemic* signal | `figure-attestation-from-prior-session` |
| same | hypoglycaemia (63 % of HET, 57 % of WT), metabolic acidosis, kidney failure; growth curve **flat P10→P17** | **P14–P18** | — | measured. ⚠️ plotted animals are survivors of a cohort 77 % dead by the final timepoint | manifest entries 5, 15, 20 |
| **Mouse, neuron-specific S-KO slice** (34634460) | spontaneous neocortical bursting, 36 of 42 KO slices | **P13–P17** | P13 | measured — and the authors state *"the chosen age group may mimic a late-stage disorder of WWOX"* | `body`, read in-act in Wave 2 |
| **Mouse ECoG** (42422765) | interictal-like discharges and **SWDs** | **from P14, 7 consecutive days** | P14 | measured | `body`, read in-act |
| **Mouse myelin** (34747138 · 42422765) | hypomyelination; MBP images labelled *"Representative MBP immunostaining at ~P90"* | **P17** (2021) and **~P90** (2026) | P17 | measured. ⚠️ *"THE DOSE-DEPENDENCE OF MYELINATION IS NEVER QUANTIFIED"* — three panels, none measured | `figure-attestation-from-prior-session` |
| **Zebrafish *wwox* morphant** (25649963) | pericardial/yolk oedema; altered Ca²⁺ dynamics | **30 hpf**, and **only after the oedema had formed** | 30 hpf | 🔴 **Not usable for a brain timeline.** LEGEND already holds the Ca²⁺ result as **qualitative only** — no ratio, no ΔR/R, no trace, no *n*, no *p* — and **peri-oedema, cardiac and intestinal, never cerebral**. The only CNS-adjacent observation in the paper is *"weak localized expression … in optic nerves"* | LEGEND ledger, receipt `FTR-20260921-25649963-01` |

### 2.1 🔴 The gap, stated as the headline the node brief asked for

> **The earliest anyone has looked in a mammalian WWOX model is E12.5 (mouse). The earliest anyone has looked in
> human WWOX-deficient brain is the 21st gestational week. In both, the tissue was already abnormal at first
> look. No WWOX model has ever been examined at the onset of neurogenesis, at neural-tube closure, or at any
> earlier stage — and the one study that reports embryonic lethality in severely affected embryos did not
> examine them.**

Two consequences that follow directly and are not speculation:

1. **No WWOX onset has been established anywhere.** Every "earliest" in this literature is a detection limit.
   Any sentence of the form *"the defect begins at X"* is unsupported for every X.
2. **The first measured lesion in the mouse (E12.5) precedes the efficacious gene-therapy window (P1–P5) by
   roughly two weeks of mouse development, which spans the whole of cortical neurogenesis.** That is arithmetic
   over two measured numbers, not an inference about human timing — and the age/window argument itself is held
   at `DL-MECH-011` and `CLAIM 031` and is **not re-litigated here**.

### 2.2 Verbatim locators for the mammalian entries, fetched in this act (PMID 32000863)

> "Wwox mouse embryos at E12.5 were smaller in size and exhibited a growth delay as compared with the wild-type littermates. An elongated roof plate and dorsal spinal cord malformation were evident in E12.5 null embryos"

`surface: body` · Results, *"Wwox is required for proper neuronal migration and development"*. ⚠️ the italic gene
symbol is deleted by the extractor before *"mouse embryos"*; the stage tokens `E12.5` are intact.

> "The homozygous knockout mice were found along a spectrum of phenotypic severity, and some very severely affected embryos died embryonically."

`surface: body` · same section. 🔴 **Grammatical mood check: this is a reported observation, not a hypothesis —
and it is never followed up anywhere in the paper.**

> "In the developing brain, Ki-67 proliferating cells were decreased in neocortical subventricular zone and cerebellum compared with the wild-types at E16.5"

> "We found that the overall cortical thickness was significantly reduced in Wwox knockouts at E16.5, in agreement with the reduced neurogenesis"

`surface: body` · same section. The second is corroborated by LEGEND's manifest entry 20 with the panel read:
Supplementary Figure 5c, *"scatter of individual animals, approximately 480 versus 370 micrometres, one
significance marker"* — `figure-attestation-from-prior-session`.

> "Gross morphological abnormalities could be observed in Wwox−/− mouse brains from live births, ranging from microcephaly to holoprosencephaly, in which the forebrain did not properly divide into two hemispheres during embryonic development."

`surface: body` · same section, via LEGEND manifest entry 14 (which preserved the `−/−` superscript that the raw
extraction deletes). 🔴 **Holoprosencephaly is a forebrain-patterning defect, and patterning precedes
neurogenesis.** It is the single strongest indication in this literature that the first lesion is earlier than
anyone has looked.

> "In our generated Wwox−/− mice, spontaneous epileptic seizures were commonly observed after postnatal day 12."

`surface: body` (genotype superscript restored from LEGEND manifest entry 7).

### 2.3 Verbatim locators for the human and rat entries (prior-session record)

> "We obtained samples of brain tissue from a control male fetus at the 21th gestational week"

`surface: body` · Materials and Methods, *Neuropathological studies* · PMID 32581702 ·
**`figure-attestation-from-prior-session` does not apply — this is a body quote from LEGEND's receipted
manifest.** ⚠️ *"21th"* is the paper's own spelling and is reproduced, not corrected.

> "A parietal section of the cerebral cortex of three fetuses of the same gestational period"

`surface: body` · Results. 🔴 **The two sentences contradict each other on the *n* of the only human experiment in
the WWOX literature**, and LEGEND's prior read records that Figure 2A's caption (*"compared to a normal fetus
(left panel)"*, singular) sides with the Methods.

> "no study has assessed the impact of pathogenic WWOX variants on the development of cerebral cortex"

`surface: body` · Introduction. **The authors' own statement of the gap, in 2020.** Nothing since has looked
earlier.

**The rat migration panel** (`figure-attestation-from-prior-session`, Figure 3J, cropped at native resolution and
upscaled 3× for asterisk adjudication): the experimental scheme prints an arrow spanning *"7 days"* from
*"E16.5 BruU injection"* to *"P1 Sacrify"* — **both misspellings are the panel's own** — and eight of ten zones
carry a significance marker. 🔴 **The strongest quantitative result in that paper is described in its running
text only as the phrase "altered distribution", with no number and no count.**

---

## 3. Task 2 — is the progenitor lesion prenatal in human terms? 🔴 **The data cannot support a gestational mapping, and that is the answer**

**What exists.** The single-cell platform in `PMID 42397075` is anchored rather than asserted, and LEGEND's read
records the apparatus precisely: 28 208 cells sequenced, 26 352 retained after quality control, 12 clusters,
annotated both by manually curated markers **and by correlation against four independent human fetal
references — early-fetal, mid-fetal reference 1, mid-fetal reference 2, and late-fetal** (Supplementary Figure 3,
panels A–E; `figure-attestation-from-prior-session`). The cell types resolved are unambiguously fetal-stage:
radial glia (VIM/SOX2/GFAP), cycling radial glia (CENPF/MKI67/TOP2A), **outer radial glia (FAM107A/HOPX/LIFR)**
and neurons (NEUROD6/MEF2C/SYN1), with RG n = 9 626, Neu n = 9 128, NP n = 4 792.

🔴 **What does not exist in LEGEND's record: which reference the organoids correlate with.** The locator records
that the correlation matrices were drawn; it does not record their result. The paper has no PMC deposit, so the
figure cannot be re-opened from this environment, and **no figure-panel claim may be made here.** I will not
infer a gestational week from the presence of outer radial glia, from the culture week, or from any other proxy.

**Therefore, precisely:**

- ✅ **The organoid progenitor phenotype is a fetal-stage phenotype.** The cell type carrying it — radial glia,
  including outer radial glia — exists in the human brain only prenatally in any substantial quantity.
- ✅ **The experimental timepoints are organoid weeks 8 to 15/16** (A51 from week 8 to week 15; the layer-marker
  qPCR at week 16), which is a culture age, not a gestational age.
- 🔴 **No gestational week can be assigned to the phenotype from what LEGEND holds.** "Early-fetal correlate" is
  **not** established here and is not asserted.
- ⇒ **What can be said about a therapy given after birth, and no more than this:** it is given to a brain in
  which the cell type that carries the measured lesion is largely no longer present in the proportions the
  organoid model assays. That is a statement about cell biology, not a gestational mapping, and it is weaker than
  the statement the portfolio would like to make.

**The one experiment that would close it** is cheap and does not need new tissue: **report the correlation-matrix
result** — state which of the four fetal references each organoid cluster matches best, and at which culture
week. The data are already generated; only the readout is missing from the record available here.

---

## 4. Task 3 — does anything reach it?

### (a) The gene-therapy arm — **no**, and the bound is already stated

> "Consistently, neuron-targeted AAV9-hSynI-WWOX restoration effectively rescued neuronal functional phenotypes without correcting RG abnormalities, suggesting that optimal therapeutic intervention may require stage and cell-type-specific targeting depending on disease progression."

`surface: body` · Discussion p. 16 · PMID 42397075 (LEGEND manifest entry 12). Corroborated by the Results
sentence that the AAV9-WWOX infection of WOREE organoids *"did not affect the RGs, as appreciated by the absence
of differentially expressed genes and cell-cycle abnormalities"* — which the paper offers as a **safety**
property and which is simultaneously a **coverage boundary**. Stated as held from Wave 3; not re-derived.

### (b) A51 — **partially, and precisely this much**

The only pharmacological arm ever applied to the progenitor compartment of human WWOX-deficient tissue.
Multi-kinase inhibitor suppressing **Wnt and MYC**, `125 nM`, weeks 8 → 15. From LEGEND's manifest
(`figure-attestation-from-prior-session`, Supplementary Fig. 7F–G, read at 170 ppi and **re-read at 258 ppi**):

| Readout | WT NT | WT DMSO | KO-1B | KO-1B + A51 | Verdict |
|---|---|---|---|---|---|
| SOX2⁺ | ≈27 % | ≈28 % | ≈60 % | **≈33 %** | ✅ **normalised** (`ns` vs WT) |
| SOX2⁺MYC⁺ | ≈48 % | ≈45 % | ≈72 % | **≈50 %** | ✅ **normalised** (`ns` vs WT) |
| NEUN⁺ | ≈30 % | ≈22 % | ≈6 % | **≈18 %** | ✅ **recovered** (`*` vs KO, `ns` vs WT) |
| **SATB2⁺** | ≈1.4 % | ≈1.45 % | ≈0.35 % | **≈0.7 %** | 🔴 **`ns` KO-vs-A51 — not corrected** |
| **CTIP2⁺** | ≈12.5 % | ≈5.5 % | ≈0.2 % | **≈0.3 %** | 🔴 **`ns` KO-vs-A51, still `****` below WT** |

⇒ **A51 restores progenitor identity and pan-neuronal marking and leaves deep- and superficial-layer neuron
production exactly where it was.** Three inherited constraints travel with it and are not optional: the compound
**is not MYC-selective** (the paper says so); the MYC-inhibition experiment is one of the **three excluded from
independent differentiations**; and *"No randomization or blinding was applied in this study."* The BLOCK-1
question recorded at `DL-THER-089` stands unanswered — suppressing Wnt during corticogenesis is the mechanism of
the benefit **and** the mechanism of the harm, and the window between them is measured nowhere.

### (c) Prenatal intervention in any WWOX model — 🔴 **zero, and the census is written down**

PubMed: `WWOX AND (prenatal OR "in utero" OR embryonic OR fetal) AND (gene therapy OR AAV OR antisense OR
treatment OR injection OR rescue)` → **`total_count: 9`**. Every one, checked by title and abstract:

| PMID | What it is | Prenatal WWOX intervention? |
|---|---|---|
| 25416187 | *"The fragile site WWOX gene and the developing brain"* — **review** | no |
| 16007179 | Drosophila *DmWWOX1* mutants, irradiation sensitivity *"rescued by reintroduction and expression of either the wild-type Drosophila or human WWOX genes"* | 🔴 **no** — this is the one hit that *looks* like an intervention. It is a **genetic complementation experiment in flies against ionising radiation**, not a prenatal therapy in a mammalian WWOX model |
| 22536204 | C1q family **review** | no |
| 42395553 | WWOX in Huntington's disease, **bioRxiv preprint** | no |
| 41677633 | WWOX induction → Bcl-xL/Mcl-1 lysosomal degradation (MEFs, SCC-15) | no — but **relevant to Wave 3's overexpression question** and already held by LEGEND as `HYP-20260705-04` |
| 37897534 | senescence escape / genome instability | no |
| 27773744 | Fhit/Wwox genome-caretaker **review** | no |
| 40088508 | genetic epilepsies cohort, India | no |
| 23028374 | de novo CNV in mouse ES cells, Xrcc4/NHEJ | no |

⇒ **`DATO`: no intervention of any kind — gene therapy, ASO, small molecule or dietary — has ever been delivered
prenatally in any WWOX model, in any species.** The count of prenatal therapeutic arms in this literature is
**zero**, and the therapeutic window that every model places the first lesion inside has **never been entered**.

---

## 5. Task 4 — three precedents for whether postnatal restoration reaches a prenatal deficit

⚠️ **Transferable-method licence applies and its limit is stated first.** These are precedents for **the question
being answerable**, and for the experimental designs that answer it. **None is a precedent for the answer in
WWOX.** No analogy below is built into an argument.

| Precedent | What it actually showed | What it licenses for WWOX | What it does not |
|---|---|---|---|
| **Angelman — `Ube3a` reinstatement, Silva-Santos *et al.* 2015, *J Clin Invest*** (PMID 25866966) | A tamoxifen-inducible maternal-`Ube3a` allele reinstated at different ages. Verbatim: *"Motor deficits were rescued by Ube3a reinstatement in adolescent mice, whereas anxiety, repetitive behavior, and epilepsy were only rescued when Ube3a was reinstated during early development. In contrast, hippocampal synaptic plasticity could be restored at any age."* | 🟢 **The single most useful precedent here.** It shows the window is **phenotype-specific within one gene** — some endpoints reversible at any age, some only early. It also supplies the **design**: an inducible restoration allele with restoration at several ages and a panel of endpoints. That design does not exist for WWOX | It says nothing about a progenitor/neurogenesis deficit — `Ube3a` loss is not a proliferation phenotype. And it is a re-activation model, not a vector |
| **Rett — MeCP2 reactivation, Guy *et al.* 2007, *Science*** (PMID 17289941) | Verbatim: *"we demonstrate robust phenotypic reversal, as activation of MeCP2 expression leads to striking loss of advanced neurological symptoms in both immature and mature adult animals."* The paper's framing question is the same as this node's: *"Can viable but defective neurons be repaired, or is the damage done during development without normal MeCP2 irrevocable?"* | 🟢 A developmental-gene deficit is **not automatically irrevocable**. This is the strongest general argument against fatalism about the WWOX window | 🔴 **The paper itself says why it may not transfer**: *"neurons do not die, which suggests that this is not a neurodegenerative disorder."* WWOX loss involves Purkinje-cell loss, granule-cell apoptosis, neuronal apoptosis and embryonic death. **A model in which neurons survive is a weak precedent for one in which they do not** |
| **SMA — presymptomatic nusinersen, De Vivo *et al.* 2019, *Neuromuscul Disord* (NURTURE interim)** (PMID 31704158) | 25 genetically diagnosed, presymptomatic infants dosed in infancy; at median 34.8 months *"all were alive and none required tracheostomy or permanent ventilation"*; **25/25 sat unsupported, 23/25 (92 %) walked with assistance, 22/25 (88 %) walked independently** — outcomes not seen in symptomatic SMA Type I | 🟢 The cleanest human demonstration that **treating before the structure is lost is categorically different from treating after**, and that a diagnosis-to-dosing interval is itself a therapeutic variable | 🔴 Single-arm, open-label, interim, industry-sponsored, and **motor-neuron loss is a different lesion from a progenitor-pool lesion**. It bears on *timing*, not on whether a progenitor deficit is recoverable |

**What the three together license, and nothing more:** the question *"does postnatal restoration recover a
prenatally established deficit?"* is **answerable by experiment**, has been answered **differently for different
endpoints within a single gene**, and the design that answers it is an **inducible restoration allele with
several restoration ages and a multi-endpoint panel**. 🔴 **No such experiment exists for WWOX.** The nearest
thing the WWOX literature has is the P1–P5 injection series, which varies timing across **five postnatal days**
and cannot address a lesion measured at E12.5.

---

## 6. What LEGEND already knew · what is new

### 6.1 Already held — used, not re-derived

- `DL-MECH-011` (efficacious window P1–P5 in mouse) and `CLAIM 031` — **held, not re-litigated**, per the brief.
- `CLAIM 014` / `CLAIM 015` and `PAPER 020` — the migration/cortical-assembly anchor, `P3 — prenatal structure`.
- The `lde` rat BrdU panel, its eight significant zones, its `n = 3`, and the **tested negative** on cortical-wall
  thickness.
- The human fetal specimen and **both halves of its *n* contradiction**.
- The hNPC audit: no migration assay, no layering readout, the abstract attributing to progenitors a finding the
  panel shows in neurons.
- The zebrafish Ca²⁺ result already demoted to qualitative, peri-oedema, non-cerebral.
- `DL-THER-089` (A51, partial and selective, BLOCK-1 open) and the RG-not-corrected bound from Wave 3.
- `HYP-20260705-04` — Bcl-xL/Mcl-1 turnover as a safety readout for pro-WWOX strategies.

### 6.2 New in this node

1. 🔴 **The headline is a looking limit, not an onset.** **E12.5 is the earliest any mammalian WWOX model has ever
   been examined**, and the embryo is already abnormal there. **21 gestational weeks is the earliest any human
   WWOX-deficient brain has ever been examined**, and the cortex is already abnormal there. No WWOX onset has
   been established anywhere, for any phenotype.
2. 🔴 **A lesion earlier than any examination is on the record and was never followed up**: *"some very severely
   affected embryos died embryonically"* — plus **holoprosencephaly**, a forebrain-**patterning** defect, in live
   births. Patterning precedes neurogenesis; nobody has looked there.
3. 🔴 **The gestational mapping of the organoid progenitor phenotype cannot be made from LEGEND's record.** The
   four-reference correlation apparatus exists and its **result is not captured**. Naming that as a missing
   readout — rather than guessing "early-fetal" — is the finding.
4. ✅ **Prenatal intervention census: `total_count: 9`, of which prenatal WWOX interventions = 0.** Each of the
   nine is named and classified, including the Drosophila complementation study that superficially reads as an
   intervention and is not.
5. ✅ **Three verified precedents with their transfer limits stated**, including the one that argues *against*
   its own transfer (Guy 2007's *"neurons do not die"* against a disease in which they do).
6. 🔴 **Extractor behaviour on stage tokens tested and cleared** — `E12.5`, `E16.5`, `P0`–`P300`, `30 hpf` all
   survive; `2 × 10¹⁰ GC` and `Wwox−/−` superscripts do not. **Stage notation is safe to quote in this corpus.**
7. 🔴 **The registry locator-count defect is systematic, not a one-off** — see §7, W4-C1.

---

## 7. Corrections, with exact file and line coordinates

**W4-C1 — 🔴 the locator-count defect found in Wave 3 is a class, with a named source.** Four `paper_registry_current.md`
records were checked against the manifests on disk. **Three are wrong.**

| Registry line | PMID | Registry declares | Manifest on disk has | Status |
|---|---|---|---|---|
| **439** | 32000863 | *"(5 locators, schema v2, strict PASS, 3 declared gaps)"* | **25** | 🔴 wrong |
| **461** | 32581702 | *"(10 locators, schema v2, strict PASS, 0 gaps)"* | **21** | 🔴 wrong |
| **7161** | 42397075 | *"(6 locators, schema v2, strict PASS, 0 gaps)"* | **30** | 🔴 wrong (already filed as W3-C2) |
| 125 | 34747138 | *"20 locator verificati"* | **20** | ✅ correct |

🔴 **Lines 439 and 461 both carry the same provenance sentence:** *"declaration reconciled from the ledger by
`CC-20260920-REGISTRY-LEDGER-DEPTH-01` (BATCH_20260920_001) — the reading is the receipt's, not this batch's"*.
**The batch that reconciled these declarations left the counts wrong in both records it touched.** Two mechanisms
are consistent with the evidence and this file does not choose between them: (i) a count copied at write time
decays silently as the manifest grows, and (ii) a counting bug — the coordinator independently reported
measuring **6** for `PMID42397075.json` by counting the keys of the `verbatim_locators` dict rather than the
length of its `entries` list, which is exactly the shape that produces a small plausible number.
**Proposed:** re-derive every declared locator count from `len(manifest['verbatim_locators']['entries'])` across
the whole registry in one pass, and add the derivation to a runnable check rather than leaving it in prose — the
same argument the repository already accepted for extraction recipes.

**W4-C2 — `PAPER 020`'s note is stale and understates what the paper now is.**
- **File:** `disease-models/wwox/registries/paper_registry_current.md` · the `**Note:**` line of PAPER 020 (record
  begins line 452; the `Evidence depth` line is 461)
- **Exact current text:** `**Note:** one of the key structural papers from the 180-paper test; full text remains high priority`
- **Issue:** the full text **has been read** (`FTR-20260810-32581702-01`, `complete_fulltext_read`, 21 locators).
  *"full text remains high priority"* describes a state that ended six weeks ago — the same stale-heading defect
  as FT-059 (Wave 1, C-3).
- **Exact proposed replacement:** `**Note:** the structural anchor, and **the only study in the WWOX literature that has examined human fetal brain** — a single neuropathological comparison at the **21st gestational week**. Read in full (`FTR-20260810-32581702-01`, 21 locators). ⚠️ Carry two bounds wherever it is cited: the paper states **one** control fetus in Methods and **three** in Results, and Figure 2A labels cortical layers **only on the control**, so the abnormal specimen's layer identification is asserted rather than shown. Rat arms are `n = 3` per genotype.`

**W4-C3 — nothing in the canonical layer records that E12.5 is the earliest anyone has looked.**
- **Files:** `disease-models/wwox/analysis/wwox_developmental_timing_audit_20260920.md` (the existing timing
  artefact) and `CLAIM 014` / `CLAIM 015` in `claim_registry_current.md`
- **Issue:** the portfolio's window language is uniformly about the **efficacious** window (P0–P5). No surface
  states the **observational floor** — that the earliest mammalian examination is E12.5, the earliest human
  examination is 21 gw, and both were abnormal at first look.
- **Proposed:** add a single `OBSERVATIONAL_FLOOR` line to the timing artefact, sourced to this file, stating the
  two numbers and the rule that **every WWOX "earliest" on record is a detection limit, not an onset.**

**W4-C4 — the organoid correlation-matrix result is a missing readout, not a missing experiment.**
- **File:** `disease-models/wwox/research/deepdive_manifests/PMID42397075.json` · entry **29**
- **Issue:** the locator records that correlation matrices against four human fetal references exist
  (Supplementary Figure 3D) and does **not** record which reference each cluster matched. That single missing
  value is what blocks a gestational mapping of the progenitor phenotype.
- **Proposed:** register it as a named, one-panel reading debt — **not** a new experiment — so that the next
  session with figure access to `brain-2025-03809-File010.pdf` closes it in one look.

---

## 8. Source attribution

Retrieved from **PubMed / PubMed Central**. Bodies for `PMID 32000863`, `34747138` and `42422765` were read in
this session; all panel-level values are **prior-session figure attestations from LEGEND's receipt-backed locator
manifests** and are labelled as such. `PMID 42397075` has no PMC deposit and was not fetched.

| PMID | Citation | DOI |
|---|---|---|
| 32000863 | Cheng Y-Y *et al.* Wwox deficiency leads to neurodevelopmental and degenerative neuropathies and GSK3β-mediated epileptic seizure activity in mice. *Acta Neuropathol Commun* 2020 | [10.1186/s40478-020-0883-3](https://doi.org/10.1186/s40478-020-0883-3) |
| 32581702 | Iacomino M *et al.* Loss of Wwox Perturbs Neuronal Migration and Impairs Early Cortical Development. *Front Neurosci* 2020 | [10.3389/fnins.2020.00644](https://doi.org/10.3389/fnins.2020.00644) |
| 42397075 | Steinberg DJ, Zonca A, Abdellatif D *et al.* Disrupted WWOX-MYC interplay impairs neurogenesis in human brain organoids. *Brain* 2026 | [10.1093/brain/awag239](https://doi.org/10.1093/brain/awag239) |
| 42422765 | Obeid M *et al.* Neuron-specific WWOX gene therapy produces dose-dependent, durable rescue in a model of WWOX-related epileptic encephalopathy. *Mol Ther Oncol* 2026 | [10.1016/j.omta.2026.201791](https://doi.org/10.1016/j.omta.2026.201791) |
| 34747138 | Repudi S *et al.* Neonatal neuronal WWOX gene therapy rescues Wwox-null phenotypes. *EMBO Mol Med* 2021 | [10.15252/emmm.202114599](https://doi.org/10.15252/emmm.202114599) |
| 19936220 | Ludes-Meyers JH *et al.* 2009, *PLoS One* — EIIA-Cre Wwox knockout, systemic phenotype | [10.1371/journal.pone.0007775](https://doi.org/10.1371/journal.pone.0007775) |
| 31543760 | Kośla K *et al.* *Front Cell Neurosci* 2019 — WWOX-silenced human neural progenitors | [10.3389/fncel.2019.00391](https://doi.org/10.3389/fncel.2019.00391) |
| 25649963 | Tsuruwaka Y, Konishi M, Shimada E. *PeerJ* 2015 — zebrafish, 30 hpf, **qualitative and non-cerebral** | [10.7717/peerj.727](https://doi.org/10.7717/peerj.727) |
| 34634460 | Breton VL *et al.* *Neurobiol Dis* 2021 — P13–P17 neocortical slice | [10.1016/j.nbd.2021.105529](https://doi.org/10.1016/j.nbd.2021.105529) |
| 16007179 | O'Keefe LV *et al.* *Oncogene* 2005 — Drosophila WWOX, irradiation; **complementation, not a prenatal therapy** | [10.1038/sj.onc.1208806](https://doi.org/10.1038/sj.onc.1208806) |
| 41677633 | Su Y-H *et al.* *Cells* 2026 — WWOX induction → Bcl-xL/Mcl-1 lysosomal degradation | [10.3390/cells15030270](https://doi.org/10.3390/cells15030270) |
| **25866966** | Silva-Santos S *et al.* Ube3a reinstatement identifies distinct developmental windows in a murine Angelman syndrome model. *J Clin Invest* 2015 | [10.1172/JCI80554](https://doi.org/10.1172/JCI80554) |
| **17289941** | Guy J *et al.* Reversal of neurological defects in a mouse model of Rett syndrome. *Science* 2007 | [10.1126/science.1138389](https://doi.org/10.1126/science.1138389) |
| **31704158** | De Vivo DC *et al.* Nusinersen initiated in infants during the presymptomatic stage of spinal muscular atrophy: interim NURTURE results. *Neuromuscul Disord* 2019 | [10.1016/j.nmd.2019.09.007](https://doi.org/10.1016/j.nmd.2019.09.007) |

---

**End.** Not medical advice. Read-only toward every canonical file; nothing promoted, nothing committed.


---

## 🔴 ORCHESTRATOR ADDENDUM — *first observed abnormal* is not *onset*, and the qualifier that would change it

**Added 2026-09-21 on Operator note, after this file was accepted and landed.**

The file's headline is already a looking limit rather than an onset. The Operator's sharpening makes
the condition explicit and **testable**:

> **`E12.5` and `GW21` are OBSERVATION FLOORS — unless an EARLIER measurement exists and was
> NORMAL.**

**That is the whole difference, and it is one question, not a programme:**

- If the earliest examination is **E12.5 and already abnormal**, the lesion began **at or before**
  E12.5 and the floor says nothing about how much earlier. **This is the current state.**
- If someone had examined **E10.5 and found it normal**, then E12.5 would bound a real onset
  **between** the two — a genuinely different fact, and the first thing any window argument needs.

🔴 **The discriminating question, named so a later wave can close it:** *does any WWOX study report
a measurement at an earlier stage that was NORMAL?* Candidate stages: gastrulation and early
neurulation in mouse (`E7.5`–`E10.5`); pre-`30 hpf` in zebrafish; any human tissue before `GW21`.
**A normal earlier measurement is as valuable as an abnormal one here — arguably more so, because
it is the only thing that converts a floor into a bound.**

⚠️ **Until that question is answered, every stage in the timeline above is reported as the earliest
anyone LOOKED, never as the earliest anything WENT WRONG** — and the two lesions already on the
record that precede every examination (*"some very severely affected embryos died embryonically"*
and **holoprosencephaly**, a forebrain-**patterning** defect, and patterning precedes neurogenesis)
are the standing reason to expect the true onset is earlier than any floor in this file.

*No canonical file edited by this addendum. Not medical advice.*

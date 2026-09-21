> 🔴 **ORCHESTRATOR NOTE, prepended 2026-09-21 before this file was landed — read this first.**
>
> **The reading in § 2 is a re-read on a WORSE surface than one this repository already holds, and it
> does not supersede it.** `PMID 31340538` (Tochigi 2019) was read **completely on 2026-08-06** from a
> full **XML** artefact — `files/fulltext/PMID31340538_Tochigi2019.xml`, receipt
> `FTR-20260806-31340538-01`, `evidence_depth: complete_fulltext_read`, with **figures and references
> recorded as read** — and it produced a dossier, a deep-dive manifest, three queue entries, a learned
> gate and the discovery lead `DL-MECH-071`. The MCP text fetched here **ends mid-Methods at § 4.4**,
> with no statistics subsection, no figure legends, no tables and no references. **Where the two
> disagree, the 2026-08 reading wins.** No new receipt is filed for this re-read and none is claimed.
>
> **The substantive conclusions of § 2 were already in the model.** `DL-MECH-071` is titled, in full:
> *"Il ratto* lde *separa numero neuronale da maturazione neurite/mielina, ma non dimostra prenatalità,
> **autonomia gliale** o reversibilità"* — cell autonomy was already recorded as **not demonstrated**,
> which is exactly the Q3 finding here. Treat § 2 as **independent corroboration reached by a second
> route**, which is worth something, and not as new evidence, which it is not.
>
> **What IS new, and is why this file lands:** the **census** in § 1 — the three-way split between
> cell-level measurement, imaging and mere mention; who has measured what; and **retrievability
> established by fetching rather than by flag**. Three things in it are actionable and were not known:
> **`PMID 33914858`** (Repudi 2021, *Brain*) is the one paper that could address cell autonomy and has
> **no PMCID at all**; **`PMC4144810`** (Nunez 2006), the report Tochigi rebuts on oligodendrocyte
> expression, returns a **zero-length body**, so the rebuttal is reachable and the claim rebutted is
> not; (see the correction immediately below on the two AAV
> intervention papers).
>
> 🔴 **AND ONE CENSUS CLAIM IS WRONG ABOUT THIS REPOSITORY — corrected before landing, by checking the
> ledger.** The census named the two Aqeilan AAV9-SynI-WWOX intervention papers as *"retrievable and
> unread"*. **Both are read, to `complete_fulltext_read` depth, more than once.** `PMID 34747138`
> carries four ledger events ending in `FTR-20260810-34747138-01` (complete); `PMID 42422765` carries
> **seven**, ending in `FTR-20260814-42422765-06` (complete). That lead is **closed, not open**, and
> nothing in § 1 should be used to reopen it.
>
> 🔴 **AND THE VERDICT LINE OVERSTATES THE FIELD, THOUGH NOT THE PAPER — third correction of this
> kind today.** This file's verdict says the paper that could separate oligodendrocyte-autonomous
> failure from axonal failure is unreachable, **as though the question were open. It is not.**
> `DL-MECH-031` records, and `HYP-20260709-07` was **parked** on it in July, that Repudi 2021's
> **conditional alleles** settle it: deleting `Wwox` in **neurons** (Synapsin-Cre) or progenitors
> (Nestin-Cre) **recapitulates the whole phenotype including the myelin defects**, while deleting it
> in **oligodendrocytes** (Olig2-Cre) or **astrocytes** (GFAP-Cre) produces no evident abnormality.
> **The hypomyelination is secondary to the neuron.** § 2's conclusion — that *this* germline null
> cannot address autonomy — is correct and stays; **a limit of one model is not a gap in the field.**
>
> ✅ **What is genuinely open, and what `A4` is now for:** LEGEND holds that conditional-genetics
> result **only second-hand**, through Obeid 2026's summary. A result that parked a therapeutic
> hypothesis, resting on another paper's description of a third paper, is a standing `D-15` exposure —
> so `PMID 33914858` is worth acquiring **to verify the attribution, not to learn the answer**. Two
> real residues travel with it: the AAV oligodendrocyte arm is **confounded by the authors' own
> admission** (*"may reflect the limited oligodendrocyte tropism of AAV9 … rather than a lack of
> relevance"*), so a partial oligodendrocyte contribution is not excluded; and **no g-ratio and no
> electron microscopy exist anywhere in this literature**, which § 1 measured independently and
> `DL-MECH-031` had already flagged as its own methodological limit.
>
> ⚠️ **The pattern, stated once because it recurred three times today: a delegate's census describes
> THE FIELD, never THIS REPOSITORY.** Before acting on any "nobody has done X", check the receipt
> ledger *and* the discovery and therapeutic ledgers. Each time I skipped that today it cost a
> correction.
>
> **My briefing defect, recorded as mine.** The task told the agent to pick the best readable primary
> and did **not** tell it to check the receipt ledger for the PMID it chose. The rule *"check the
> ledger before dispatching a read"* was written into the session state earlier the same day after the
> same thing happened to `PMID 25650666`. **When a delegate chooses the paper, the ledger check has to
> be in the brief** — the Orchestrator cannot pre-check a paper it has not yet named.

---

# WWOX myelin / oligodendrocyte census — bounded search and one read

**Scientist B · 2026-09-21 · READ-ONLY · no canonical file modified**

---

## VERDICT

**Yes — myelin and oligodendrocyte biology has been measured at the cellular level in WWOX-deficient
animals by at least three independent groups, and at least three such papers are retrievable in
full text; but the single paper that could separate oligodendrocyte-autonomous failure from axonal
failure (Repudi 2021, *Brain*, neuron-restricted `Wwox` deletion) is NOT retrievable through this
deployment's instrument, and the one primary paper read here is a whole-animal germline null with
no conditional, no culture and no intervention arm — so the myelin window is supported by
cell-level evidence that it is a *developmental* deficit, and not by any cell-level evidence about
*which cell* fails.**

---

## § 1 · The census

### 1.1 Queries actually run

Verbatim, against `mcp__PubMed__search_articles`:

1. `WWOX AND (myelin OR myelination OR oligodendrocyte)` → 9 hits
2. `WWOX AND (white matter OR leukodystrophy OR hypomyelination)` → 10 hits
3. `WWOX AND (MBP OR PLP1 OR CNPase OR Olig2 OR MOG)` → 3 hits
4. `Wwox AND (mouse OR rat) AND (brain OR corpus callosum)` → 37 hits (breadth cross-check only)
5. `Wwox AND (g-ratio OR electron microscopy OR node of Ranvier OR axon)` → 7 hits

Five queries. The de-duplicated union of queries 1, 2, 3 and 5 is **19 records**, of which 16 were
pulled for metadata. **This is a small literature and that is itself the finding.** Query 4 was run
to check that the myelin-targeted queries were not missing a Wwox rodent paper; it returned no
additional record whose title or abstract carried a myelin or oligodendrocyte readout, so query 4
was not expanded. No citation-network chasing was done. No WWOX-and-cancer expansion was done.

### 1.2 The three-way evidence split

`NCKU` = National Cheng Kung University, Tainan — the **Chang Nan-Shan** laboratory network.
`HUJI` = Hebrew University of Jerusalem — the **Aqeilan** laboratory.
Papers from the same laboratory do not independently corroborate one another.

#### A · CELL-LEVEL MEASURED (7)

| PMID | First / senior author | Year | Journal | What was measured | Lab | Retrievability, **as tested** |
|---|---|---|---|---|---|---|
| **31340538** | Tochigi / **Suzuki H** (Nippon Veterinary and Life Science Univ., Tokyo) | 2019 | Int J Mol Sci | MBP + CNP immunostaining and western blot, PND 5/10/15/21; **APC⁺ mature oligodendrocyte counts**; Wwox/APC double immunofluorescence | **Independent** (neither NCKU nor HUJI) | **FETCHED — body 25,545 chars.** PMC6678113 |
| **33914858** | Repudi / **Aqeilan RI** | 2021 | Brain | Myelination-gene transcripts; "reduced maturation of oligodendrocytes, reduced myelinated axons and impaired axonal conductivity"; **neuron-specific conditional deletion**; human brain organoids | HUJI | **NOT RETRIEVABLE — no PMCID exists** (ID conversion returned PMID only). Classified from abstract; *an abstract is not a read.* |
| **32000863** | Cheng / **Hsu L-J** (NCKU); **Chang N-S is a co-author** | 2020 | Acta Neuropathol Commun | "severe hypomyelination in the central nervous system"; optic nerve atrophy; "peripheral nerve **demyelination** due to Schwann cell apoptosis"; motor evoked potentials | **NCKU — inside the Chang network** | **FETCHED — body 37,576 chars.** PMC6990504 |
| **34747138** | Repudi / **Aqeilan RI** | 2021 | EMBO Mol Med | AAV9-SynI-WWOX gene therapy; "myelination deficits" among rescued phenotypes. **Intervention arm.** | HUJI | **FETCHED — body 45,685 chars.** PMC8649866 |
| **42422765** | Obeid / **Aqeilan RI** | 2026 | Mol Ther Adv | Dose-ranging AAV9-hSynI-WWOX; "enhanced myelination"; explicitly compares **neuron-restricted vs oligodendrocyte-directed** vectors. **Intervention arm.** | HUJI | **FETCHED — body 48,780 chars.** PMC13343157 |
| 16941225 | Nunez / **Aldaz CM** (MD Anderson) | 2006 | J Mol Histol | Human normal-tissue WWOX immunohistochemistry; "No expression of WWOX was detected in … myelinized structures". Wild-type expression map, **not** a WWOX-deficient system | Independent | **PMCID RESOLVES BUT BODY IS ZERO-LENGTH.** PMC4144810 returned `full_text` length **0**. Not retrievable. |
| 15026124 | Chen / **Chang N-S** | 2004 | Neuroscience | WOX1 immunohistochemistry in developing murine nervous system; white-matter tracts. Wild-type expression, **not** a deficient system | **NCKU — Chang lab** | No PMCID. Not retrievable. |

#### B · IMAGING ONLY (6) — MRI, i.e. **not a myelin measurement**

| PMID | Senior author | Year | Journal | Imaging finding |
|---|---|---|---|---|
| 42721537 | Caraballo (Garrahan, Buenos Aires) | 2026 | Seizure | frontotemporal atrophy, corpus callosum hypoplasia; "delayed myelination was observed in one case" (1/7) |
| 41442931 | Zhang G (Emory) | 2025 | Pediatr Neurol | periventricular white matter volume loss, corpus callosum atrophy; vigabatrin-associated signal change |
| 39039877 | Zhang YH (Peking Univ First Hosp) | 2024 | Zhonghua Er Ke Za Zhi | "delayed white matter myelination in 3 cases" (of 12); callosal hypoplasia in 5 |
| 36779245 | **Scheffer IE** (Melbourne) | 2023 | Epilepsia | "thin corpus callosum, and white matter signal abnormalities"; null/null genotype class has worst survival |
| 26345274 | Zuccoli (Pittsburgh) | 2015 | Am J Med Genet A | "periventricular white matter volume loss and atrophy of the corpus callosum" |
| 28763065 | Knickmeyer (UNC) | 2017 | Transl Psychiatry | GWAS: intronic WWOX SNP rs10514437 **neared** genome-wide significance for infant white-matter volume. Common variant, not WWOX deficiency |

**None of these six distinguishes hypomyelination from demyelination, or oligodendrocyte failure
from axonal loss.** They are the class of evidence the model already had.

#### C · MENTIONED only (3)

| PMID | Author | Year | Why it is only a mention |
|---|---|---|---|
| 42128308 | Obeid / Aqeilan, Neurobiol Dis 2026 | **Review**, not primary. Asserts "impairs oligodendrocyte development" and that gene therapy "rescues … myelination defects" — re-voicing the HUJI primaries |
| 30350478 | Hussain / Aldaz, Genes Chrom Cancer 2018 | **Review**; fragile-site and genomic-instability focus |
| 19500159 | Suzuki K, Genes Brain Behav 2009 | Maps the `lde` rat `Wwox` mutation and audiogenic seizures; hippocampal/amygdalar vacuoles. No myelin or oligodendrocyte readout |

### 1.3 Retrievability, as established by fetching

Six PMC bodies were requested and their lengths measured. **Five non-empty, one zero-length.**

| Target | PMCID | Body length | Verdict |
|---|---|---|---|
| Tochigi 2019 | PMC6678113 | 25,545 | retrievable |
| Cheng 2020 | PMC6990504 | 37,576 | retrievable |
| Repudi 2021 EMBO | PMC8649866 | 45,685 | retrievable |
| Obeid 2026 | PMC13343157 | 48,780 | retrievable |
| Nunez 2006 | PMC4144810 | **0** | **not retrievable — resolving PMCID, empty body** |
| Repudi 2021 *Brain* | **none** | n/a | **not retrievable — no PMCID** |

Nunez 2006 is the exact failure mode the brief warned of: the identifier resolves, the fetch
succeeds, and the body is empty. It would have been counted as "open access" by any flag-based
method.

### 1.4 Laboratory independence

Of the 7 CELL-LEVEL MEASURED papers: **3 are Aqeilan (HUJI)**, **2 are NCKU / Chang Nan-Shan**
(32000863 has Chang N-S as co-author; 15026124 has him as senior author), **2 are independent**
(Tochigi/Suzuki 2019; Nunez/Aldaz 2006). Note also that 32000863 carries a second, unrelated
`Chang` (Chang Tsung-Hao) — the homonym is present in the very paper where it matters.

**The cell-level myelin claim therefore rests on two laboratory lineages plus one independent rat
study.** The independent rat study is the one read below.

---

## § 2 · The read — Tochigi et al. 2019 (PMID 31340538)

Selected because it is the only candidate that is simultaneously **primary**, **fetched non-empty**,
**cell-level measured**, and **from a laboratory independent of both Aqeilan and Chang**.

Artefact: `/home/user/legend-development/files/fulltext/PMID31340538_PMC_MCPtext.txt`
Bytes: **25,545** · `sha256` **d809524e8a08c5687a0e8816113ccc723d285b18c5079b5c76b170974bb035f5**
Body only; the abstract is reproduced nowhere in the artefact.

**Instrument state for this body.** The extractor deleted every italicised token. In this paper the
**genotype labels are italicised** (`lde/lde`, `+/+`, `+/lde`), so they are largely gone: sentences
arrive as "In contrast,rats showed significantly lower myelination". Genotype assignment below is
reconstructed from sentence structure and the contrast markers ("In contrast", "than of"), and is
flagged wherever load-bearing. The body **ends mid-Methods at § 4.4** — there is **no Statistical
Analysis subsection, no figure legend, no table and no reference list**. Consistent with that,
`ANOVA`, `Student`, `n =` and `p <` all return **0**, which here is an *instrument* reading (the
statistics section is absent), not a claim that the work was unanalysed. By contrast the roman-type
zeros **`electron microscopy` = 0, `g-ratio` = 0, `blinded` = 0, `culture` = 0, `NG2` = 0,
`PDGFR` = 0, `treatment` = 0, `rescue` = 0** are informative: these words do not appear in the
retrieved prose. `Olig2` = 0 is *not* offered as evidence, since gene symbols are italicised.
Per **D-14**, the myelin immunostaining and the APC counts exist as figures that cannot be
inspected here; only their prose descriptions are adjudicable.

### Q1 — What was measured, in what system, at what ages?

**Species / genotype:** inbred rat, strain *lethal dwarfism with epilepsy* (LDE); a **spontaneous
germline 13-bp deletion in exon 9** of `Wwox`, homozygous. Not a conditional, not a knockdown.

> "The Wwox gene ofrats contains a 13-bp deletion (c.1190_1202del) in exon 9 causes frame-shift,
> resulting in an aberrant C-terminal amino acid sequence (p.leu371Thrfs*53)"

The protein is effectively absent, with a caveat the authors state themselves:

> "In contrast, no protein band with the same electrophoretic mobility was detected in the whole
> brain and cerebral cortex ofrats, although a very weak band of slightly lower mobility was
> detected"
> "it is unlikely that this faint expression of mutated Wwox protein would have substantial effects
> on the phenotype ofrats."

That last sentence is the authors' **judgement**, not a measurement — no functional assay of the
residual product is reported.

**Tissue:** cerebral cortex and corpus callosum (paraffin coronal sections spanning the
hippocampus); plus whole-organ panel for expression.

**Ages:** **PND 5, 10, 15, 21** — an explicit four-point developmental time course.

> "Normal (,) andrats at PNDs 5, 10, 15, and 21 were anesthetized with isoflurane"

**Readouts:** MBP and CNP by immunohistochemistry **and** western blot; APC (clone CC-1) positive
cell counts for mature oligodendrocytes; NeuN for neuron number and laminar distribution; MAP2 and
FluoroPan Neuronal Marker for neurite growth; GFAP for astrocytes; Iba1 for microglia; Wwox
double-immunofluorescence against each marker. Quantification by ImageJ, positive area in pixels
per mm² and cell counts, from at least three rats per genotype per day.

> "At least three affected and three normal males were included in each experiment (western blot
> and immunostaining) and examined each day."

n ≥ 3 per genotype per time point. **No blinding is stated** (`blinded` = 0, a roman-word zero).

### Q2 — Hypomyelination or demyelination?

**Hypomyelination, within PND 5–21. Myelin is never properly laid down; nothing here shows myelin
laid down and then lost.** The time course is what carries this, and the paper has one.

> "A few dispersed signals corresponding to both were detected near the white matter (WM) ofrats on
> PND 5, with positivity gradually extending toward the surface of the cerebral cortex. In
> contrast,rats showed significantly lower myelination on PNDs 5–21"

> "Western blotting also showed age-associated increases in MBP and CNP in cerebral cortices
> ofrats, along with significantly lower levels of expression inrats"

Both genotypes **rise** with age; the mutant rises less, from the **earliest time point sampled
(PND 5)**. That is a failure to accumulate, not a loss. The authors themselves frame the deficit
against the normal developmental schedule:

> "In rats, the active proliferation of oligodendrocyte precursor cells is completed around PND 20,
> whereas myelination starts around PND 10 and reaches a peak at PND 20, followed by low levels of
> myelination in adults []."

**Limits on this answer, stated plainly.** (i) The series stops at PND 21; `lde/lde` rats die early,
so the paper can say nothing about whether myelin that *was* formed is subsequently lost. (ii) The
single occurrence of `demyelin` in the whole body is in the **Discussion, about human MRI
literature, not about these rats**:

> "delayed myelination and progressive demyelination have been also reported [,,,,,]."

That sentence is a citation of imaging findings in patients. **It is not a measurement in this
system and must not be carried as one.** (iii) The word `hypomyelination` appears 3 times, all in
Discussion, describing the authors' interpretation of their own PND 5–21 data and comparing to
other mutant animals.

So: **in the rat, cell-level evidence supports hypomyelination during the myelination window. The
"progressive demyelination" in the human phenotype is, in this paper, an imaging citation only.**

### Q3 — Is the defect oligodendrocyte-autonomous?

**No, and this paper cannot address it.** It is a **whole-animal germline null**. There is no
conditional allele, no cell-type-specific manipulation, **no oligodendrocyte culture**
(`culture` = 0, roman, informative), and **no OPC-versus-mature lineage marker time course** — APC
(mature oligodendrocytes) is the only lineage marker, and no precursor marker is reported in the
retrieved prose (`NG2` = 0, `PDGFR` = 0, both roman).

What is measured:

> "Immunohistochemistry showed that the number of APC-positive cells was significantly lower in a
> subarea of the cerebral cortex including the WM region ofthan ofrats on PNDs 15–21 (H,I). The
> reduced number of APC-positive cells was also observed in the region of corpus callosum."

**A timing asymmetry worth recording:** the MBP/CNP deficit is reported from **PND 5**, while the
APC⁺ mature-oligodendrocyte deficit is reported only at **PND 15–21**. The myelin-protein deficit
therefore precedes the demonstrated mature-oligodendrocyte deficit in the windows reported. The
paper does not comment on this.

The authors offer **both** causal readings, and the moods differ:

> "the severe reduction in myelination ofcortices may result, at least in part, from the retarded
> growth of axons predicted by the delayed differentiation of neurons, as indicated by the reduced
> expression of MAP2 and reduced immunostaining of FluoroPan Neuronal marker."

— modal ("may", "predicted"): **speculation**, offered as such. And:

> "In addition, the reduced number of APC-positive oligodendrocytes incortices indicates that the
> marked reduction in myelination is also caused by the reduced number of mature oligodendrocytes."

— indicative ("indicates … is also caused by"): **phrased as a finding, but it is an inference from
a correlation in a whole-animal null.** No manipulation separates the two. This sentence is the
single most likely place in this paper for a speculation to be re-voiced downstream as a
measurement. It should not be carried into the model as a demonstration of cell autonomy.

The paper that *would* answer Q3 — neuron-restricted `Wwox` deletion producing a myelin defect,
which would argue the defect is **non**-cell-autonomous — is **PMID 33914858 (Repudi 2021, Brain)**,
and it is **not retrievable here**.

### Q4 — Is WWOX expressed in oligodendrocytes at all?

**Yes — and this paper is where that was first shown, against a prior report that said otherwise.**

> "Wwox protein was also detected in the cytoplasm of most APC-positive oligodendrocytes in the CC
> (B) and in other regions throughout the forebrain."

> "Although previous immunohistochemistry found that Wwox protein was present in neurons and
> astrocytes but not in oligodendrocytes [], our double immunofluorescence using specific markers
> clearly showed that Wwox protein was present in oligodendrocytes, as well as in neurons and
> astrocytes."

> "To our knowledge, this study is the first to show that Wwox is expressed in oligodendrocytes."

The "previous immunohistochemistry" it contradicts is almost certainly **Nunez 2006 (PMID
16941225)** — "No expression of WWOX was detected in … myelinized structures" — which is the census
entry whose full text **returned a zero-length body**. So this repository can reach the rebuttal
but not the claim being rebutted. Microglia are the stated negative:

> "In contrast, Iba1-positive microglia in the cerebral cortex and CC were not immunostained with
> antibody to Wwox (D)."

That negative rests on a figure and is therefore **not adjudicable here per D-14**.

### Q5 — Any intervention arm?

**None. Zero.** `treatment` = 0, `rescue` = 0, `lithium` = 0 — all roman-type words, all informative
zeros. This is a descriptive natural-history study with no therapeutic manipulation of any kind, no
dose and no treated group.

(The census does contain intervention arms — PMID 34747138 and PMID 42422765, both Aqeilan, both
retrievable, both reporting myelination improvement after AAV9-SynI-WWOX. **Those were not read in
this session**; their abstracts are census entries, not evidence, and are not quoted as findings
here.)

### Q6 — Direction and window

**Earliest detectable defect: PND 5**, the first age sampled, for **both** MBP/CNP and MAP2. The
deficit is therefore already present at the earliest observation, and the true onset is **not
bracketed** — no earlier time point exists in this study.

> "the level of its expression was significantly lower in cerebral cortices ofthan ofrats at all
> ages"  (MAP2)

Neurological signs arrive later than the myelin deficit:

> "Inrats, epileptic seizures and ataxic gait occur after PND 16 [,]."

**The paper says nothing whatsoever about when an intervention would have to act.** No therapeutic
window is proposed, no critical period is named. Any window statement derived from this paper is an
inference by the reader, not a finding of the paper, and the normal-development landmarks it quotes
(OPC proliferation complete ~PND 20; myelination PND 10 → peak PND 20) are **rat** landmarks cited
from other work, not human ones.

### Q7 — Abstract-versus-results check, and grammatical mood

**Abstract vs Results: no material divergence.** Every abstract claim has a Results counterpart —
neurite reduction without neuron loss, myelination reduction with reduced mature oligodendrocytes,
reduced astrocytes and microglia, Wwox in all three neural lineages. **Reported explicitly, as
required: there is no abstract/results divergence in this paper.**

**Mood check — two flags, both in the Discussion, neither in the Results:**

1. The axon-first explanation is **explicitly modal** ("may result, at least in part … predicted
   by") — the authors present it as speculation and it must stay speculation.
2. The oligodendrocyte-first explanation is **indicative** ("indicates that the marked reduction in
   myelination is also caused by") — grammatically a finding, epistemically an inference from
   correlation in a whole-animal null. **This is the sentence most at risk of being re-voiced
   downstream as a measurement of cell autonomy. It is not one.**
3. One further over-reach: the abstract's closing — "These results indicate that Wwox is essential
   for normal development of neurons and glial cells in the cerebral cortex" — is a necessity claim
   drawn from a purely descriptive comparison with no rescue arm.

---

## § 3 · What `HYP-20260709-07` may now assume, and what remains unmeasured

### Measured, and now supported by cell-level evidence

- **Myelin and oligodendrocyte biology *have* been measured in WWOX-deficient animals.** This is no
  longer an open question. The model may stop treating the myelin phenotype as imaging-only.
- **In the rat germline null, the deficit is hypomyelination during the myelination window**, shown
  by a four-point PND 5/10/15/21 time course of MBP and CNP by two methods, with both genotypes
  rising and the mutant rising less. The myelin deficit is **developmental failure to build**, not
  demonstrated loss of built myelin — *within PND 5–21*.
- **The number of mature (APC⁺) oligodendrocytes is reduced**, in cortex and corpus callosum, at
  PND 15–21.
- **WWOX is expressed in oligodendrocytes.** This matters directly: a pro-myelinating hypothesis
  that assumed oligodendrocytes never see the protein would have been assuming wrongly. The
  contrary human-tissue report (Nunez 2006) is unreachable here.
- **The deficit is already present at the earliest age anyone sampled**, and precedes seizure onset
  (PND 5 vs after PND 16 in the rat).

### Not measured — and `HYP-20260709-07` may not assume these

1. **Cell autonomy.** Nothing read here separates oligodendrocyte failure from axonal failure. The
   only retrieved paper is a whole-animal null with no conditional, no culture, no precursor marker.
   A pro-myelinating agent acting on oligodendrocytes assumes a target cell that has not been shown
   to be the failing cell. The paper that speaks to this (Repudi 2021, *Brain*) is **unreachable in
   this deployment** — that is an acquisition gap, not an evidence gap, and it is the single highest
   value item to acquire by another route.
2. **Hypomyelination versus demyelination in the human course.** The model's standing description —
   poor myelination at 9 weeks, absent by 23 weeks, "progressive demyelination", corpus callosum
   thinning — is **imaging**. The rat gives cell-level support for the *hypo* half only, over
   PND 5–21, and dies before the question of later loss can be asked. **The "progressive
   demyelination" half of the standing finding remains imaging-only and cell-level unmeasured.**
   These two have different windows and different interventions, and the distinction is not yet
   closed by cell-level data reachable here.
3. **No myelin ultrastructure in anything read.** `electron microscopy` = 0 and `g-ratio` = 0 in the
   read body (roman-type, informative zeros). Sheath thickness, wraps per axon and axon calibre are
   unmeasured in the paper read. Marker protein abundance is not sheath geometry.
4. **No intervention in the paper read.** Nothing was given, at any dose, to improve myelination in
   this system. Two retrievable intervention papers exist in the census (both Aqeilan) and both
   report myelination improvement in their abstracts — **that is a census observation and has not
   been read.** Until read, it is not evidence, and the observation that both come from one
   laboratory stands.
5. **No therapeutic window is stated by any paper read.** The model's "time-sensitive variable par
   excellence" framing is consistent with what was measured, but no source read here names an age
   past which intervention would be futile. The rat landmarks quoted are rat.
6. **No blinding is reported** in the paper read, and its statistical section was not retrieved.

### The status of the hypothesis, stated without recommendation

`HYP-20260709-07` was conditional on an experiment nobody had done. **Part of that experiment has
been done**: oligodendrocyte and myelin biology has been measured in WWOX-deficient rodents,
WWOX is present in oligodendrocytes, and the developmental deficit is cell-level real and early.
**The part that is still undone is the part that tells you what to aim at**: no reachable paper
separates an oligodendrocyte-autonomous defect from a downstream consequence of axonal or neuronal
failure, and one reachable intervention literature — which happens to compare neuron-directed
against oligodendrocyte-directed delivery — remains unread in this session.

Nothing in this document is medical advice, and nothing here is phrased as a treatment
recommendation. Therapeutic output supports discussion with a treating clinical team and never
substitutes for one.

---

## Provenance and declared limits

**Author:** Scientist B · **Date:** 2026-09-21 · **Mode:** READ-ONLY.
**No canonical LEGEND file was modified.** No registry, queue, ledger or current file was touched.
No git command was run. No commit candidate was produced. Two files were written and no others:
this analysis, and the full-text artefact
`/home/user/legend-development/files/fulltext/PMID31340538_PMC_MCPtext.txt`.

**Queries actually run, verbatim** (all via `mcp__PubMed__search_articles`):

```
WWOX AND (myelin OR myelination OR oligodendrocyte)
WWOX AND (white matter OR leukodystrophy OR hypomyelination)
WWOX AND (MBP OR PLP1 OR CNPase OR Olig2 OR MOG)
Wwox AND (mouse OR rat) AND (brain OR corpus callosum)
Wwox AND (g-ratio OR electron microscopy OR node of Ranvier OR axon)
```

Full texts fetched and body length measured: PMC6678113 (25,545), PMC6990504 (37,576),
PMC8649866 (45,685), PMC13343157 (48,780), PMC4144810 (**0**).
Identifier conversion run on 16 PMIDs; PMID 33914858 returned **no PMCID**.

**Declared limits.**

- **A census is not evidence.** Sections 1.2 and 1.3 are a search result. Only PMID 31340538 was
  read. Every other classification in § 1 is from title, abstract and metadata — **and an abstract
  is not a read.**
- **An MRI signal is not a myelin measurement.** All six IMAGING ONLY entries are excluded from any
  cell-level claim.
- **Extractor loss.** The MCP extractor silently deletes italicised tokens. In the read body this
  removed the genotype labels themselves, plus inline figure and reference cross-references; the
  reference list, all figure legends, all tables and the statistical-methods subsection are absent.
  Genotype assignment in § 2 is reconstructed from sentence structure and is flagged as such.
- **Zero-count discipline.** Zeros for italicisable tokens (gene symbols, `Olig2`) are **instrument
  readings** and are never offered as negatives. Zeros for roman-type words (`electron microscopy`,
  `g-ratio`, `blinded`, `culture`, `NG2`, `PDGFR`, `treatment`, `rescue`, `lithium`) are reported as
  informative, and each is labelled where used.
- **D-14.** No figure image is inspectable. Myelin staining and any electron micrograph are figures;
  no negative asserted only by a figure is adjudicated here, including the microglial Wwox negative.
- **Independence.** 3 of 7 cell-level papers are Aqeilan (HUJI), 2 are NCKU / Chang Nan-Shan. A
  paper from a laboratory does not independently corroborate that laboratory.
- **Search bound.** Five queries. No citation-network expansion, no WWOX-and-cancer expansion, no
  non-PubMed source consulted. A paper measuring myelin in a WWOX system but using none of these
  terms in its indexed fields would be missed.
- **Nothing here is medical advice.**

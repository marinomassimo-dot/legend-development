# PMID 42422765 — Obeid et al. 2026, *Mol Ther Methods Clin Dev* (PAPER 011)

**Neuron-specific WWOX gene therapy produces dose-dependent, durable rescue in a model of
WWOX-related encephalopathy** · PMCID from local PMC HTML · Aqeilan laboratory, with
Berent and Brennan among the authors.

🟡 **PARTIAL READ of 2026-08-10 — declared partial deliberately.** Abstract, the therapeutic-
window section and the **entire Discussion** were read in full. Introduction, the seven
results sections, Materials and Methods and all figures were **not** read. The reading was
stopped where care could no longer be guaranteed, not where the material ran out.

This supersedes nothing: the only prior record, `FTR-20260726-42422765-01`, is a
`legacy_reconstruction` whose source locator is `paper_registry_current.md#PAPER 011` — the
registry, not the article. Its coverage map is `unknown_legacy` in every section. **No reading
of this paper had ever taken place.**

## Surface

| artifact | kind | sha256 |
|---|---|---|
| `files/fulltext/PMID42422765_Obeid2026_PMC.html` | `article_text` | `00fadaf411998f4e453f55a8fc65dcaf9567ce259671286e1f7863aff6da9bd3` |

Screened clean. Body 88 241 chars, abstract 2 115, cleanly separated. Thirteen locators, all
verified against the artifact, **none anchorable to the abstract**.

## Why this paper, and what it settles

Read immediately after `PMID 34747138` because it is the direct continuation: Repudi 2021 gave
a single dose at P0 and left the window open as its largest unknown. This paper is the dose-
response and timing study, from the same laboratory, four years later.

### 🔴 It fires the REVIVAL_TRIGGER recorded yesterday

The trigger written into the 34747138 record was: *a post-natal dosing experiment in this
model would change the reading of the whole paper.* It exists, and it is here.

**1.**
> "neuronal WWOX restoration using the high-dose vector at any time point between P0 and P5 was sufficient to fully rescue the Wwox-null phenotype"

`surface: body` · Results, 'Early postnatal WWOX gene therapy achieves durable therapeutic
rescue'. With the magnitude:
> "a dramatic extension in survival, from approximately three weeks to nearly one year"

**2.** 🔴 **And the paper explicitly refuses to read its own ceiling as biology.**
> "Therapeutic rescue beyond this early postnatal window was not explored, as Wwox-null mice rapidly deteriorate with progressive neurological dysfunction and early lethality"

> "the inability to assess later intervention likely reflects a combination of model-specific biological constraints and technical limitations, rather than a definitive boundary for therapeutic responsiveness"

> "human patients with WWOX-related encephalopathies may exhibit different developmental trajectories, disease kinetics, and therapeutic responsiveness, potentially allowing for later intervention"

`surface: body` · Discussion, window paragraph.

**This is the epistemically correct form of a negative and it should be recorded as a model
of one.** The absence of data beyond P5 is caused by the mouse dying, not by the therapy
failing. A system that files "window = P0–P5" as a fact would have manufactured a false
negative of exactly the kind [[epistemic_discipline]] describes — silent, permanent, self-
reinforcing. The correct entry is: **efficacy demonstrated P0–P5; upper bound unknown and
unmeasurable in this model.** `PREMISE: DEFAULT_FROM_TEXTBOOK` would have been the trap —
"gene therapy needs an early window" is true elsewhere and is not established here.

**3.** The authors name what would extend it:
> "future studies should explore alternative strategies to extend the therapeutic window, including earlier prenatal delivery, less invasive or systemic administration routes"

### What it settles about oligodendrocytes — and what it does not

Yesterday's paper attributed its residual myelin deficit to a possible oligodendrocyte-
autonomous WWOX function. This paper tests that directly, with an MBP-driven vector, and it
fails — but the authors refuse the easy conclusion:

**4.**
> "may reflect the limited oligodendrocyte tropism of AAV9 following neonatal ICV administration rather than a lack of relevance for oligodendrocyte WWOX expression"

> "We also cannot exclude that the optimal dose was not achieved, as all vectors were tested at the same titer (4E10)"

`surface: body` · Discussion. 🔴 **A failed rescue by a vector with poor tropism for the target
cell is not evidence that the target cell does not matter.** The question yesterday's reading
raised stays open, and this paper says so itself.

**5.** The independent genetic evidence for neuronal sufficiency is conditional-KO, not this
vector series:
> "deletion of Wwox in neural stem/progenitor cells (Nestin-Cre) or postmitotic neurons (Synapsin I-Cre) recapitulated the severe neurological and metabolic phenotypes of global KO mice, whereas astrocyte- (GFAP-Cre) or oligodendrocyte-specific (Olig2-Cre) deletion produced no overt abnormalities"

`surface: body` · Discussion, citing reference 42. Against the paper's own headline:
> "neuronal WWOX expression is both necessary and sufficient for survival and CNS homeostasis, whereas expression in oligodendrocytes alone is insufficient to confer benefit"

### Vector design and its declared limits

**6.**
> "we removed WPRE as a proactive risk-mitigation step to improve the predictability and control of neuronal WWOX expression for potential clinical translation"

`surface: body` · Discussion. Removed **pre-emptively**, not after observed toxicity —
efficacy was then recovered by dose.

**7.** The limitation the authors state about their own promoter comparison:
> "a limitation of our study is that WWOX expression levels were not normalized across promoter conditions"

**8.** And about the electrophysiology:
> "Although conducted in a limited cohort, these findings support the capacity of WWOX gene therapy to correct epileptiform activity at its developmental onset"

## What this does to yesterday's two readings

| yesterday | today |
|---|---|
| 34747138: P0 only, window declared the largest unknown | **P1–P5 works; the ceiling is the model's, not the therapy's** |
| 34747138: residual myelin deficit attributed to possible oligodendrocyte-autonomous function | **tested and failed — but by a vector with poor tropism for that cell, so the question is open, not closed** |
| 34747138: reviewer objection "no evidence for absence in the PNS", unquotable | this paper has sciatic-nerve and spinal-cord sections in its Methods — **unread here**, and the obvious place to look |

## Figures: retrieved, ceiling measured, one inspected (2026-08-10, same session)

Part of the debt below was paid immediately rather than deferred. All seven main figures were
retrieved and fingerprinted; **the ceiling is 104 effective ppi and there is no better copy.**

| route | result |
|---|---|
| PMC CDN blobs (`gr1`–`gr7`) | ✅ 726–738 px wide → **104 ppi** |
| `pmc…/articles/PMC13343157/pdf/main.pdf` | JS "Preparing to download" interstitial |
| `pmc…/articles/instance/13343157/bin/mmc1.pdf`, `mmc2.pdf` | same interstitial |
| `ftp.ncbi…/oa_pdf/24/2a/main.PMC13343157.pdf` | 404 |
| Europe PMC `?pdf=render` · `supplementaryFiles` | 500 · 404 |

**This inverts the lesson learned four hours ago on `PMID 34747138`, and that is the point.**
There the OA bundle served 100 ppi while the article PDF held 200, so the canonical route was
the worse one. Here the CDN copy at 104 ppi is the *only* one: every PDF route is closed. The
generalisable rule is not "prefer the PDF" — it is **measure every available route and take
the best, because which route wins is not stable across papers.** The licence differs too:
`CC BY-NC-ND` here against `CC BY` for 34747138.

🔴 **Supplementary Figure S8 — which carries the entire P0–P5 window result — is not
retrievable.** Every route above fails for `mmc1.pdf` and `mmc2.pdf`. The window finding
therefore rests on running text alone, and that is now a measured fact rather than an
omission.

### Figure 6 (`gr6.jpg`, sha256 `a7c90344223caf323cfb92aea250d3753c12ae057594239dc406b0865ba959f4`) — inspected

`surface: figure`. Read at 104 ppi. What the panels carry:

- **C** — brain weight WT ≈465 mg vs KO ≈245 mg, `****`. A ~47% reduction.
- **D** — corpus callosum thickness WT ≈325 vs KO ≈230, `**`.
- **E** — MBP intensity, WT/KO pairs for four regions, each annotated with its **reduction**:
  **corpus callosum 48% · cortex 30% · striatum 50% · anterior commissure 70%.** The myelin
  deficit is strongly **region-dependent**, worst in the anterior commissure and mildest in
  cortex — a gradient the running text does not give.
- **F** — WT / LD / HD image grid for corpus callosum, striatum and cortex.

🔴 **The same shape as the previous three readings, in a new form.** Panels C, D and E carry
the quantification and contain **only WT and KO — the treated animals are absent**. Panel F
contains the treated animals at both doses and carries **no quantification and no statistics
at all**: it is an image grid. So in this figure the dose-dependence of myelination is
*shown* and never *measured*.

That is now four consecutive papers where the comparison a reader most needs is the one the
figure does not draw. It is no longer an observation about a paper; it is a property of this
literature, and it is the strongest argument yet for inspecting panels rather than trusting
the sentence that cites them.

### 🔴 Figure 3 (`gr3.jpg`, sha256 `c63f930cf5c558aea1d5c1bf90bd1d3dbf72e94ec378bd9f499748c768b4997d`) — the dose-response hides a threshold

`surface: figure`, read at 104 ppi. **This is the most decision-relevant panel in the paper,
and the running text's vocabulary does not convey it.**

**Panel A** gives the two doses in vector genomes: **LD = 1.23 × 10¹¹ vg**, **HD = 2.63 ×
10¹¹ vg** — a 2.1-fold separation.

**Panel B, Kaplan–Meier** (WT+RI n=20 · KO+RI n=10 · KO+LD n=20 · KO+HD n=30):

| arm | outcome read from the curve |
|---|---|
| KO + reporter | all dead by ~20 days |
| **KO + LD** | **all dead by ~90 days — the curve reaches zero** |
| KO + HD | plateau at ~80% out to 300 days |
| WT + reporter | plateau at ~90% |

**The low dose does not rescue survival. It buys time.** From ~20 days to ~90, and then every
animal dies. The high dose plateaus. That is not a graded difference along one axis — it is
**qualitative**, and it means there is a threshold between 1.23 and 2.63 × 10¹¹ vg below which
the treatment converts a rapidly lethal phenotype into a slowly lethal one.

The paper's own words for this are *"dose-dependent"*, *"graded improvement"* and *"a clear
dose-response relationship"*. All three are true of the data and all three describe a
continuum. A reader who never opens panel B will carry "more dose, more benefit" instead of
**"below threshold, no survival at all"** — and those two beliefs recommend different trials.

**Panels E–H, blood glucose**, sharpen the same point:
- **P10** — everything `ns` except WT+RI vs KO+RI;
- **P20** — `*` WT vs **KO+LD**, `**` KO+LD vs KO+HD, and `ns` WT vs KO+HD. At P20 **the low
  dose has NOT corrected the hypoglycaemia** while the high dose has;
- **P30** — all `ns`;
- **P180** — only WT+RI and KO+HD are present, `ns`. **KO+LD is absent from the P180 panel**,
  which panel B explains: by then there are none left.

🔴 `PREMISE_TAG` — any inference of the form "a lower, safer dose would still help" rests on
reading dose-response as a continuum. **Panel B refutes it for survival in this model.**
`REVIVAL_TRIGGER`: an intermediate dose arm between 1.23 and 2.63 × 10¹¹ vg would locate the
threshold and is the single most informative experiment this paper implies.

### 🔴 Correction to the Figure 3 entry above — I read the panel without its caption

The threshold finding stands and is strengthened. The *secondary* claim I attached to it —
that Figure 3B continues the "WT-versus-treated comparison is never drawn" pattern — **is
wrong, and the correction matters more than the original observation.**

The caption of Figure 3 carries the statistics the panel does not print:

> "HD produced survival comparable to WT animals (p = 0.78), and significantly extended survival relative to the LD group (p < 0.0001) and the KO + RI controls (p < 0.0001). LD also significantly improved survival compared with the KO + RI controls (p < 0.0001)."

`surface: body` · Figure 3 caption. So the authors **do** draw WT-versus-treated — `p = 0.78`,
high dose indistinguishable from wild type — and they **do** test LD against HD, `p < 0.0001`.

Two consequences, opposite in direction:

- **The threshold reading is now quantitative, not inferred from a curve.** LD versus HD is
  significant at `p < 0.0001`, and LD versus untreated is *also* `p < 0.0001`. The low dose
  genuinely improves survival and genuinely fails to rescue it. That is the threshold, stated
  by the paper's own tests.
- **My pattern claim did not apply here and I should have checked before extending it.** After
  three papers where the comparison was genuinely missing, I found the fourth instance by
  looking for it — in a panel whose caption, two lines away in the same layout I had already
  generated, contained the answer. **A pattern that has held three times is exactly when the
  fourth case stops being examined and starts being assumed.** The `DEFAULTS THAT BIT US`
  entry this earns is my own: *"the figure does not draw the comparison" needs the caption
  read before it is asserted.*

The pattern claim still stands for Figure 6, where panels C/D/E contain only WT and KO and
the caption adds no statistics for panel F.

### 🔴 Figure 7 (`gr7.jpg`, sha256 `3a01e962c0cb5d6986f4c0cd5d57aeaaf1107d36679cc6828bcf67e11425ce7c`) — one claim is `****`, the neighbouring one is `p = 0.2`

`surface: figure`, 104 ppi. The paper states early hyperexcitability as a single finding with
two markers. The panels support the two very differently.

| panel | measure | result |
|---|---|---|
| **C** | average spikes/day, WT vs KO | **`0.2000` printed above the bracket — n≈3 per group** |
| B | spikes/hour/day over 7 days | KO visibly above WT, **no significance marker on any day** |
| **E** | spike-wave discharges/hour | **`****` WT-vs-KO · `****` KO-vs-HD · `ns` WT-vs-HD** |

🔴 **Panel C prints `0.2000` — a P value of 0.2 — with no asterisk and, crucially, without the
word `ns` beside it.** A number floating above a bracket reads as a result; this one is a
non-result. The interictal-spike half of "early-onset neuronal hyperexcitability,
characterized by frequent interictal-like spikes and SWDs" is **not statistically supported**
in this figure, at n≈3.

The spike-wave discharge half is strongly supported, and panel E is the paper at its best:
the WT-versus-treated comparison **is** drawn, and it is `ns` — the high dose returns SWD rate
to wild-type. That is the cleanest efficacy result in the paper.

This is what the Discussion's own hedge refers to — *"Although conducted in a limited
cohort"* — and the figure lets us put a number on "limited": three animals.

### The PNS question from yesterday has an answer, and it is not the expected one

> "WWOX protein was also detected in the sciatic nerve of HD-treated mice (Figures S6E–S6G), thus supporting functional relevance in the peripheral nervous system. In contrast, no WWOX expression was detected in the liver following either LD or HD treatment"

`surface: body` · Results. The reviewer of `PMID 34747138` objected that there was **no
evidence for absence in the PNS**. This paper answers by finding the opposite of absence:
after neonatal ICV of a *neuron-restricted* vector, **WWOX protein reaches the sciatic
nerve**, while the liver stays negative.

So the construct is neuron-specific but **not CNS-confined**. The authors read this as
functional relevance; it is equally a **biodistribution fact** that any safety assessment
needs, and it was obtained by the sciatic-nerve and spinal-cord dissection whose protocol the
Methods describe. Expression is also sustained in cortex, hippocampus, midbrain, cerebellum
and spinal cord at **P240 and P300 after a single neonatal injection**.

### A vocabulary note worth keeping

Figure 5 caption:
> "in G and H it is near significant, p value = 0.08 and 0.06, respectively"

`surface: body`. **"Near significant" is not a state.** Recorded because this reading has now
seen three distinct ways a non-significant result can be presented as almost-something: an
unmarked printed P (Fig. 7C), a comparison not drawn (Fig. 6), and an explicit softening
(Fig. 5 caption). All three are legitimate authorial choices; none of them may be carried into
this state as support.

### 🔴🔴 Figure 5 (`gr5.jpg`, sha256 `9510b8511d31db8ad31654b64aa3744142e19c1af88024290a39c3dc863df8a8`) — the survival threshold has no measured expression difference behind it

`surface: figure`, 104 ppi, all twelve panels at P30. **This is the most consequential panel
set in the paper and it cuts against the paper's own framing.**

**Vector genome copies (A–D)** and **hWWOX mRNA (E–H)**, low dose versus high dose:

| region | AAV DNA LD → HD | mRNA LD → HD |
|---|---|---|
| cortex | ≈2 800 → ≈8 800 · **`ns`** | ≈520 → ≈700 · `ns` |
| hippocampus | ≈2 000 → ≈3 800 · **`*`** | ≈540 → ≈650 · `ns` |
| midbrain | ≈2 200 → ≈7 300 · **`ns`** | ≈65 → ≈145 · `ns` |
| cerebellum | ≈320 → ≈730 · **`ns`** | ≈37 → ≈95 · `ns` |

**Seven of eight comparisons are `ns`.** The one significant difference is viral DNA in the
hippocampus. The error bars are enormous — in panel C the high-dose interval runs from about
2 000 to 15 000.

🔴 **So the two doses differ 2.1-fold in what was injected, are statistically
indistinguishable in what arrives and what is transcribed across four brain regions, and
produce opposite survival outcomes — every low-dose animal dead by ~90 days against a plateau
at ~80% (Figure 3B, `p < 0.0001`).**

That is a real tension inside one paper, and it is invisible from the running text, which says
the vector "restores WWOX DNA, mRNA, and protein expression in a **dose-dependent** manner".
Dose-dependence is visible in the *means* and absent from the *statistics*. Three readings are
open and the reading cannot choose between them:
- the true difference lies where nobody measured — other regions, other timepoints, or cell-
  level rather than tissue-level expression;
- the difference is real and the study is **underpowered to detect it**, which the variance
  makes plausible and which the survival curve — n=20 and n=30, `p < 0.0001` — detects easily;
- survival depends on something other than mean transgene level.

`PREMISE_TAG` · 🔴 **Any dose recommendation drawn from this paper rests on the survival curve
alone, not on a measured expression difference.** Recorded as `INFERENZA`, and the
`REVIVAL_TRIGGER` from the Figure 3 entry — an intermediate dose arm — gains a second reason:
it would also test whether expression tracks dose at all.

### Three more things the blots carry

**Protein (I–L)**, values printed under each lane, relative to WT = 1:

- **cerebellum (L)** — LD `0.7 / 0.5 / 0.7`, HD `0.7 / 0.5 / 0.2`. **Both doses stay *below*
  wild type, and the high dose is not above the low.** The cerebellum is not reconstituted at
  all, in a paper whose title says "rescue" and whose text says "restores".
- **hippocampus (J)** — LD `14.2 / 19.5 / 9.2`, HD `14.7 / 9.1 / 18.3`: 9- to 19-fold **over**
  wild type, with the two doses interleaved. This is not restoration to physiological level,
  it is an order-of-magnitude overexpression — worth holding beside the authors' stated reason
  for removing WPRE, which was to keep expression closer to endogenous.
- 🔴 **hippocampus KO lane reads `1.1`** — the same as wild type — while the KO lane reads
  `0.02` in cortex, `0.03` in midbrain and `0.08` in cerebellum. In a *Wwox*-null animal a
  WWOX band at wild-type intensity is not a biological result; it is most likely a
  non-specific band or a normalisation artefact in that blot. **It is not flagged in the
  figure and not mentioned in the text.** It does not change the paper's conclusions, but it
  is the kind of internal inconsistency that a reader quoting hippocampal fold-change would
  carry forward unknowingly.

### 🔴 Figure 2 (`gr2.jpg`, sha256 `08f9f3f4e7ef7a61fab0d78c1e5764a959c5ad2f7e16b0f777f68e852254a69b`) — two doses below the ones in Figure 3, and none of them rescues survival

`surface: figure`, 104 ppi. This figure tests the WPRE question at **4 × 10¹⁰ and 8 × 10¹⁰
vg** — that is, at **a third and two thirds of the low dose** used in Figure 3
(1.23 × 10¹¹). Panel B, Kaplan–Meier:

| arm | outcome |
|---|---|
| WT (n=5) | alive past 40 days |
| KO (n=4) | dead ~17–18 days |
| KO + hWWOX **4E10** (n=3) | dead ~18–20 days |
| KO + hWWOX **8E10** (n=5) | dead ~17 days |
| KO + WWOX-WPRE **4E10** (n=3) | ~33% to ~25 days |

**No treated arm in this figure survives.** Put beside Figure 3, the paper contains a
four-point survival dose series that no single figure displays:

| dose | survival |
|---|---|
| 4 × 10¹⁰ · 8 × 10¹⁰ | no benefit — death at ~17–25 days |
| 1.23 × 10¹¹ (LD) | death at ~90 days |
| 2.63 × 10¹¹ (HD) | plateau ~80% at 300 days |

The threshold recorded from Figure 3 is therefore **not an artefact of comparing two doses**:
across four doses spanning 6.6-fold, survival stays near zero, then extends, then plateaus.
The transition sits between 1.23 and 2.63 × 10¹¹ — which is exactly the interval the
`REVIVAL_TRIGGER` asks to be filled.

### The WPRE decision, and the loop it closed

Panel E, protein relative to WT = 1, cortex / hippocampus / midbrain / cerebellum:

| construct | 2 × 10¹⁰ | 4 × 10¹⁰ |
|---|---|---|
| WWOX, **no** WPRE | `0.8 / 0.9 / 0.3 / 0.1` | `4.7 / 5.9 / 1.5 / 0.4` |
| WWOX **+ WPRE** | `11.6 / 11.9 / 4 / 2.4` | `25.6 / 22.3 / 11.6 / 6.2` |

WPRE multiplies expression roughly **10–15 fold**, and without it at 2 × 10¹⁰ the protein sits
**at or below wild type**. Panels F and G show the visual counterpart: with WPRE the neuronal
signal is intense and diffuse, matching the Discussion's "prominent punctate staining".

🔴 **The design loop is worth stating in full, because the paper states it only in pieces.**
WPRE was removed deliberately, to keep expression predictable and near-endogenous. Removing it
dropped expression to wild-type level or below. Efficacy was then recovered by raising the
dose about six-fold, from 4 × 10¹⁰ to 2.63 × 10¹¹. And at that dose the hippocampus reads
**9- to 19-fold over wild type** (Figure 5J) — comparable to what WPRE produced at a fraction
of the dose.

So the vector was made more predictable, not lower-expressing. That is a defensible
engineering choice and probably the right one: a controlled promoter at high dose is not the
same risk profile as an enhancer element with a steep response. But it is **not** the story
"we reduced expression for safety", and a reader taking the WPRE removal as evidence of lower
transgene burden would be wrong about the final construct.

### Figure 1 (`gr1.jpg`, sha256 `9956521d22c3787ba10551dd7a4284faca01e569a0bdb20ba852064cf5be6c51`) — the promoter comparison, and what panel M shows

`surface: figure`, 104 ppi. Four promoters, all at **4 × 10¹⁰ vg**. Blood glucose at P14:

| promoter | target | glucose vs WT | vs KO |
|---|---|---|---|
| EF1α | neurons + glia | improved to ≈100 (WT ≈137), **still `***` below WT** | `***` |
| CMV | ubiquitous | ≈132, **`ns` vs WT** | `***` |
| **MBP** | oligodendrocytes | ≈60, **`ns` vs KO — no effect at all** | **`ns`** |
| Synapsin | neurons | ≈130, **`ns` vs WT** | `****` |

Survival tracks the same ordering: MBP no benefit, EF1α marginal, CMV extended to ~30–35 days
then lost, Synapsin best.

🔴 **Panel M is the one that matters, and it supports the authors' own caution rather than
their headline.** WWOX immunofluorescence in cortex, one column per promoter: EF1α weak and
diffuse, CMV moderate, **MBP essentially blank**, SynI strong and clearly cellular. The MBP
vector did not fail to help — **it barely produced detectable WWOX at all**.

That is the visible form of the Discussion's hedge, already recorded as locator 4: the failure
"may reflect the limited oligodendrocyte tropism of AAV9 … rather than a lack of relevance for
oligodendrocyte WWOX expression". The panel converts that from a polite caveat into an
observation. **The oligodendrocyte question raised by `PMID 34747138` is not answered by this
experiment, and panel M is why.** (One qualification the panel invites: M shows *cortex*,
where oligodendrocyte density is lower than in white matter — a corpus-callosum column would
test the tropism explanation more directly, and is not shown.)

### 🟡 A tension between Figure 1 and Figure 2 that this reading cannot resolve

Figure 1J shows Synapsin-driven WWOX at 4 × 10¹⁰ holding at 100% survival out to ~25 days.
Figure 2B shows `KO + AAV-hWWOX (4E10)` — apparently the same promoter, construct and dose —
**dead at ~18–20 days**.

The two may be reconcilable: the plotted windows differ, Figure 1's curves are drawn to ~25–45
days while Figure 2's run to ~50, and n is 6 against 3. A curve that has not yet fallen is not
a curve that will not fall. **Recorded as an open discrepancy, not as a contradiction**, and
flagged because anyone citing "Synapsin rescues survival at 4E10" from Figure 1 would be
contradicted by Figure 2 of the same paper.

### 🔴 The promoter hierarchy was established below the therapeutic threshold

The single most consequential thing about Figure 1 is its dose. **Every promoter was compared
at 4 × 10¹⁰ vg** — and Figure 2, in the same paper, shows that at 4 × 10¹⁰ *no* construct
produces durable survival, while Figure 3 puts the effective dose at 2.63 × 10¹¹, **6.6-fold
higher**.

So the conclusion that neuron-restricted expression beats ubiquitous and oligodendrocyte-
directed strategies rests on a comparison run entirely **beneath the dose at which the winning
construct itself works**. The authors state the premise plainly — *"all vectors were tested at
the same titer (4E10)"* — and state its consequence for MBP; the consequence for the whole
ranking is left implicit.

🔴 `PREMISE_TAG` · `PREMISE: INFERENZA`. The claim "neuronal WWOX expression is both necessary
and sufficient … whereas expression in oligodendrocytes alone is insufficient" is supported
here by (a) a sub-threshold promoter comparison and (b) prior conditional-KO genetics
(Nestin-Cre and SynI-Cre recapitulate, GFAP-Cre and Olig2-Cre do not, reference 42). **(b) is
the load-bearing evidence; (a) is consistent with it and cannot establish it.** A promoter
comparison repeated at 2.63 × 10¹¹ is the experiment that would.

### 🔴 Figure 4 (`gr4.jpg`, sha256 `4bfa9eefa0e9eae4ccc12c97894c7044419785e63b8128952377a97d4d566d6d`) — "normalizes" is the wrong word for these panels

`surface: figure`, 104 ppi. Behaviour at 3 months, WT+RI (n=9) against KO+W HD (n=10). Eight
quantified panels, and **the WT-versus-treated comparison is drawn in every one** — this
figure does the thing the others did not.

| test | measure | result |
|---|---|---|
| open field | **velocity** | WT ≈9.5 → HD ≈11.5 · **`*`** |
| open field | **total distance** | WT ≈3 400 → HD ≈4 300 · **`*`** |
| open field | centre-zone frequency | `ns` |
| open field | periphery frequency | `ns` |
| elevated plus maze | velocity · open-arm · closed-arm duration | `ns` · `ns` · `ns` |
| **rotarod** | **latency to fall** | WT ≈85 s → HD ≈145 s · **`*`** |

🔴 **In all three significant panels the treated animals do not match wild type — they exceed
it.** They move faster, cover more ground, and stay on the rotarod nearly twice as long. The
section is titled *"Neuronal WWOX restoration normalizes neurobehavioral function"*.

**A significant difference from wild type is not normalisation, and its direction does not
change that.** Three readings are open and this reading does not choose:
- **hyperactivity** — increased velocity and distance in an open field, with anxiety measures
  (`centre/periphery`, `open/closed arm`) all `ns`, is the classic locomotor signature, not a
  sign of restored normality;
- **overshoot from overexpression** — consistent with the 9- to 19-fold hippocampal protein of
  Figure 5J;
- **marginal statistics** — three `*` at n≈10, unadjusted across eight comparisons in one
  figure and many more across the paper.

The third deserves weight: **eight comparisons in this figure alone, no multiplicity
correction declared**, and the three positives are all at the weakest significance level.

What is genuinely reassuring, and worth stating because it is the actual result: **anxiety-
related behaviour is indistinguishable from wild type** on four independent measures, and
motor coordination is at least as good. The therapy does not produce an anxious or
motor-impaired animal. That is a real and useful finding; it is not what "normalizes" claims.

### The pattern, resolved

Across seven figures the shape recorded through four papers now has a precise form. It is not
that this laboratory avoids the WT-versus-treated comparison — **Figure 3's caption, Figure
7E and all eight panels of Figure 4 draw it**. It is that when the comparison is drawn and
comes out significant, the surrounding prose still reports normalisation. The comparison is
present in the data and absent from the vocabulary.

## Reading debt this leaves — explicit and large

- **Introduction, all seven results sections and Materials and Methods: not read.**
- ✅ **All seven main figures inspected.** Every one carried something the running text did
  not. Coverage for `figures` is upgraded from `not_read` to `read` in a superseding receipt.
- **Materials and methods: read for the sciatic-nerve and spinal-cord protocol and for the
  statistics; the rest not read.**
- 🔴 **Every supplementary figure remains unreachable.** S5 and S6 now carry more weight than
  when this file was first written: S6E–S6G hold the sciatic-nerve result, S6H–S6I the
  negative liver, S5J–S5K the P240/P300 persistence, and **S8 the entire P0–P5 window**. Five
  retrieval routes fail. Everything this reading says about them comes from running text with
  no panel behind it.
- 🔴 **A rule this session derived and did not yet apply.** Measure *every* available
  retrieval route and take the best, because **which route wins is not stable between
  papers**: on `34747138` the article PDF held 200 ppi against the OA bundle's 100, and here
  every PDF route is closed and the 104 ppi CDN copy is all there is. This belongs in
  `CLAUDE.md` beside rule 5d, which currently says only "prefer XML/HTML over PDF" — true for
  *text*, and silent about *figures*, where the ranking inverts. **Noted, deliberately not
  written today.**
- 🔴 **Supplementary Figure S8 is unreachable, not merely unread.** Five routes fail. The
  entire P0–P5 window result — the finding that fires the previous paper's REVIVAL_TRIGGER —
  therefore rests on running text with no panel behind it. This is the single most important
  unverified claim in the current state, and it may stay unverifiable until the publisher
  route opens.
- The **PNS question** from yesterday's refused review file has a candidate answer in this
  paper's Methods. Unread.

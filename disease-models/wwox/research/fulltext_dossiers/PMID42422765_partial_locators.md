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

## Reading debt this leaves — explicit and large

- **Introduction, all seven results sections and Materials and Methods: not read.**
- **Five of the seven figures: retrieved and fingerprinted, not inspected.** `gr1`, `gr2`,
  `gr4`, `gr5` and `gr7` — including **Figure 7, the electrophysiology**, which is where the
  early-hyperexcitability claim and its suppression must be checked. On disk at the measured
  ceiling, awaiting eyes. Figures 3 and 6 are done, and both carried something the running
  text did not.
- **Materials and methods: not read.** It contains the sciatic-nerve and spinal-cord
  extraction that is the candidate answer to the PNS objection raised against
  `PMID 34747138`.
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

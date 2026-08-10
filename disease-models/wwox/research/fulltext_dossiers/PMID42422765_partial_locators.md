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

## Reading debt this leaves — explicit and large

- **Introduction, all seven results sections and Materials and Methods: not read.**
- **Six of the seven figures: retrieved and fingerprinted, not inspected.** `gr1`–`gr5` and
  `gr7` — including Figure 7, the electrophysiology — are on disk at the measured ceiling and
  await eyes. Figure 6 is done.
- 🔴 **Supplementary Figure S8 is unreachable, not merely unread.** Five routes fail. The
  entire P0–P5 window result — the finding that fires the previous paper's REVIVAL_TRIGGER —
  therefore rests on running text with no panel behind it. This is the single most important
  unverified claim in the current state, and it may stay unverifiable until the publisher
  route opens.
- The **PNS question** from yesterday's refused review file has a candidate answer in this
  paper's Methods. Unread.

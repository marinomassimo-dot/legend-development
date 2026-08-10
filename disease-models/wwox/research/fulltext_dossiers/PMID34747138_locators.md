# PMID 34747138 — Repudi et al. 2021, *EMBO Mol Med* 13:e14599

**Neonatal neuronal WWOX gene therapy rescues Wwox null phenotypes** ·
DOI 10.15252/emmm.202114599 · PMCID PMC8649866 · **CC BY 4.0**

Complete full-text read of 2026-08-10. Supersedes the partial read of 2026-08-09
(`FTR-20260809-34747138-02`, [`PMID34747138_partial_locators.md`](PMID34747138_partial_locators.md)),
whose nine locators remain valid and are not repeated here. This record closes the debt that
receipt declared: **discussion, methods and references `not_read`, figures `captions_only`,
supplementary `not_read`.**

## Why this paper was next

Of the 21 local structured surfaces without a complete read, this is the only one whose debt
was already **measured** rather than presumed — three receipts, one of them a
`legacy_reconstruction` whose coverage map is `unknown_legacy` in every section and can
therefore support nothing. Closing a documented partial beats opening an unknown, and it sits
on the same axis (myelin, epilepsy) as `CLAIM 003`, whose primary — the *Brain* twin
`PMID 33914858` — is suspended for text-layer corruption and cannot serve it.

## Surfaces and artifacts

| artifact | kind | sha256 | note |
|---|---|---|---|
| `files/fulltext/PMID34747138_Repudi2021_PMC.xml` | `article_text` | `7da156e82cb7014f837d8c29374d888cb99ecc3268d1c383af2c3d0832b988bb` | JATS. Screened clean; body 66 144 chars, abstract 1 465 |
| `…/figures/PMID34747138/fig_p03_1404x1326.png` … `fig_p10_1415x1226.png` | `figure` | see manifest | six figures, ~200 ppi |
| `…/EMMM-13-e14599-s001.pdf` | `supplement_text` | `1e5c30a903d96726cffae487e14f2e80593e4a6adf2e8b08efb70a5762f86cd2` | Appendix, 11 pp. **Sentinel PASS** |
| `…/EMMM-13-e14599-s002.pdf` | — | `2a9f4fe6da019efd53eaa813632d02e34d396c9bef625973afdfd82e9fecbbdc` | Review Process File, 29 pp. 🔴 **Sentinel REFUSED** |
| `…/EMMM-13-e14599_article.pdf` | `article_binary` | `32ee98733a6f45550f6b924b701734e111d171992ecba2535f0c32a5e105b438` | source of the figure images only; **no locator rests on its text** |

### The open-access package serves the worse copy of its own figures

Worth recording, because the canonical route is the misleading one. The Europe PMC
supplementary bundle delivers the figures as JPGs at **93–102 effective ppi**. The article
PDF embeds the *same* figures at **186–202 ppi** — double. Extracting the embedded bytes with
`extract_image` (not rendering the page, which resamples) is what made the EM panels legible
at all: the significance brackets and the axis values below are not readable at 100 ppi.

**A reader who stops at the OA package will believe they are looking at the original.** The
ppi ceiling has to be measured on each route, not assumed from the route's authority.

### 🔴 The Review Process File is readable and not citable

`s002.pdf` carries the three peer reviews and the authors' point-by-point response — the most
epistemically valuable document in the bundle, because it is where independent experts state
what the paper does *not* show. Its extracted text **contains `U+0000` at offset 63 867**, so
`_refuse_suspect_surface` refuses it, correctly and without exception.

It was therefore **read as context and carries no locator**. Two reviewer objections are
recorded here as *read, unquoted*, and the distinction is deliberate:

- a reviewer states that for these technically challenging experiments **an n of 3 is
  considered the absolute minimum**, and that the low n is not prominently visible;
- a reviewer states there is **no evidence for absence in the PNS**, nor for expression in
  brain regions distal to the injection.

Both are load-bearing for how far this result travels. Making either quotable needs a page
adjudication of `s002.pdf` — a cost deliberately not paid today. Recorded as debt.

## Coverage map

| section | before (2026-08-09) | now |
|---|---|---|
| abstract · introduction · results | `read` | `read` |
| **discussion** | `not_read` | **`read`** |
| **methods** | `not_read` | **`read`** |
| **figures** | `captions_only` | **`read`** — six images at ~200 ppi |
| **supplementary** | `not_read` | **`read`** — Appendix (sentinel PASS) and Review File (refused, read unquoted) |
| **references** | `not_read` | **`read`** — 62 entries enumerated, 36 gene-directed, **all 36 already known to LEGEND** |
| tables | `not_present` | `not_present` |

## Verbatim locators

Sixteen new locators, all verified against the JATS artifact and none anchorable to the
abstract, plus four figure attestations. The nine locators of the partial read stand.

### What the paper is: a gene-therapy proof of concept

**1.** *The authors' own framing, and the destination they name.*
> "this proof‐of‐concept will lay down the groundwork for a possible gene therapy clinical trial on children suffering from the devastating and often refractory WOREE and SCAR12 syndromes"

`surface: body` · Discussion, closing. Paired with the unmet need it argues from:
> "WOREE children are refractory to the current antiepileptic drugs (AEDs)"

**2.** *The construct, dose and route — the part a translation actually needs.*
> "Approximately 1 μl (2 × 1010 GC/hemisphere) virus was dispensed"

`surface: body` · Methods, ICV injection. And the technique, stated plainly:
> "Free‐hand intracranial injections"

`surface: body` · Methods. Not stereotaxic. AAV9 under the human Synapsin-I promoter,
bilateral ICV, at P0.

**3.** *Transduction efficiency is 60–70% of neurons, not near-complete.*
> "The percentage of NeuN and WWOX double‐positive cells was calculated and found to range between 60 and 70%"

`surface: body` · Results. And the specificity that makes the design interpretable:
> "WWOX expression was lacking in non‐neuronal cells of the brain such as oligodendrocytes"

`surface: body` · Results. **This is what makes the myelin result non-cell-autonomous**: the
oligodendrocytes are never transduced, and they mature anyway.

### 🔴 The therapeutic window is the single largest unknown, and the authors say so

**4.**
> "The limited life span and poor conditions of Wwox‐null mice prompted us to treat these mice very early on in their life (P0)"

> "attempts to treat post‐natal Wwox‐null mice by different route of AAV administration should and will be explored in the future"

`surface: body` · Discussion. 🔴 `PREMISE_TAG` — **every efficacy number in this paper is
conditioned on treatment at day zero of life.** In WOREE the diagnosis arrives months later,
after seizure onset. The paper does not test a later window and does not claim to. Any
inference from "reverses the phenotype in mice" to "would help a diagnosed child" crosses a
gap the authors leave explicitly open. `REVIVAL_TRIGGER`: a post-natal dosing experiment in
this model would change the reading of this entire paper.

### The rescue is substantial and incomplete, and the figures say where

**5.** The authors' own qualification:
> "there are still some differences between rescued and WT mice which could be attributed to an oligodendrocyte‐specific WWOX function in regulating the myelination process"

`surface: body` · Discussion.

**6.** 🔴 **READ FROM THE PANELS — where the WT-versus-rescued comparison is actually run, it
is significant against the rescue; where it is not run, the visible gap goes untested.**
`surface: figure` · the EM figure (`fig_p08`), read at ~200 ppi.

| measure | WT | KO | KO+AAV-mWwox | brackets shown |
|---|---:|---:|---:|---|
| myelinated axons / FOV, corpus callosum | ≈130 | ≈46 | ≈105 | `***` WT-vs-KO · `***` KO-vs-rescued |
| myelinated axons / FOV, optic nerve | ≈140 | ≈68 | ≈124 | `***` WT-vs-KO · `***` KO-vs-rescued |
| **unmyelinated axons / FOV, corpus callosum** | **≈26** | not shown | **≈52** | **`**` WT-vs-rescued** |

The third row is the one that matters. It is the **only panel in the figure that compares WT
with the rescued animals**, and it reports roughly **twice as many unmyelinated axons in the
treated mice as in wild type**, significantly. In the two panels where the rescue looks
strongest, that comparison is simply not drawn — the brackets run WT-vs-KO and KO-vs-rescued,
never WT-vs-rescued. The g-ratio scatter does normalise: the treated cloud overlies WT while
the KO cloud sits flat at 0.8–0.95.

**7.** `surface: figure` · the myelination/OPC figure (`fig_p07`): CC1⁺ mature
oligodendrocytes in the corpus callosum run WT ≈170, KO+GFP ≈77, rescued ≈135 (`***`, `***`);
PDGFRα⁺ progenitors run WT ≈53, KO+GFP ≈87, rescued ≈70 (`**`, `*`). **Same pattern**: both
rescued values sit between KO and WT, and neither is tested against WT.

### Safety, as far as this paper goes

**8.**
> "we did not detect gross tumor formation in the limited number of adult Wwox‐null mice treated with AAV9‐hSynI‐WWOX that we examined (age 8–11 months)"

`surface: body` · Discussion. 🔴 The three qualifiers are the finding: **gross** (no
histology), **limited number** (unquantified here), **8–11 months** (not lifetime). WWOX is a
tumour suppressor and the restoration is brain-only, so peripheral tissues remain null. This
is a *no observed signal in a small survey*, not a safety result, and the paper says so.

### Method facts that bound every number above

**9.** `surface: body` · Methods —
> "100 axons per mouse, n = 3 per genotype"

n = 3 biological replicates for the EM quantification. The reviewer objection recorded above
lands exactly here.

**10.** ⚠️ `surface: body` · Methods —
> "Mice were anesthetized using ketamine/medetomidine"

The hyperexcitability recordings are **in vivo cell-attached under ketamine**, an NMDA
antagonist with direct effects on cortical excitability. The comparison is between groups
under the same anaesthetic, so the contrast stands; the absolute firing rates are not a
measure of the awake brain. Not a flaw — a bound on interpretation that the running text does
not state.

**11.** `surface: body` · Methods, and the reason it is quoted at all —
> "Results were considered significant when the P < 0.05"

**This sentence is the control experiment for rule 5d.** Its twin, `PMID 33914858` (same
first author, same year, same lab), carries the identical sentence in its PDF text layer as
`Results were considered significant when P 5 0.05` — the comparator destroyed. Here, on a
structured JATS surface, `<` survives intact. Same sentence, same authors, two surfaces, one
of them silently wrong. **FT-044 is suspended for exactly this, and this locator is the
positive control that shows the policy is about the surface and not about the paper.**

**12.** `surface: body` · Methods —
> "Data analysis was performed while blinded to the genotype"

Stated twice (image analysis and statistics).

### The metabolic thread, which reaches yesterday's reading

**13.**
> "the reversibility of hypoglycemia associated with WWOX deficiency in Wwox‐null mice"

`surface: body` · Discussion — and the paragraph cites **Iatan et al, 2014**, i.e.
`PMID 24871327`, read yesterday, as part of the evidence that WWOX governs metabolism.

**14.**
> "our findings imply that WWOX’s function in the CNS is superimposing its tissue‐level function"

`surface: body` · Discussion. Neuronal-only restoration restored **fertility** with no
peripheral WWOX expression.

🔴 **This is a direct, unforced convergence with FT-039.** Yesterday's paper established that
the *liver-specific* knockout does not reproduce the whole-body HDL phenotype, and proposed an
extrahepatic compensator. This paper shows the mirror image from the other side: restoring
WWOX **only in neurons** rescues peripheral phenotypes — glucose, fertility, bone — that no
peripheral cell expresses WWOX to produce. Two independent readings, two different groups,
converging on the same shape: **for several WWOX phenotypes the tissue where the readout is
measured is not the tissue where the gene has to be present.** Recorded as `INFERENZA`, not
`DATO`: neither paper tests the other's organ.

## Reading debt this session opens or leaves open

- **`s002.pdf` (Review Process File) — quotable only via page adjudication.** Two reviewer
  objections are read and unquoted. Cost deliberately not paid today.
- **Appendix `s001.pdf` passed the sentinel but its figures were not inspected as images.**
  Appendix Figs S1–S6 include the 9-month WWOX persistence (S2A) and adult cell-attached
  raster plots (S5H). Declared, not done.
- **62 references enumerated, 36 gene-directed, multi-hop not performed.** Unlike yesterday's
  paper this one adds **no unknown gene-directed reference**: all 36 are already in the
  registry, queue or tracking log. That is a first for this corpus, and it says something
  about where the boundary now is — the Aqeilan-adjacent literature is enumerated, and the
  gaps are elsewhere. Two of the 36 are today's and yesterday's own subjects (`24871327`,
  `33914858`) and one is `30370248`, the paper FT-047's list had lost.
- **`PMID 33914858` (FT-044) remains suspended.** This reading does not substitute for it:
  the *Brain* paper is the primary of `CLAIM 003`, and this one cites it as `Repudi et al,
  2021` for the non-cell-autonomous mechanism it builds on.

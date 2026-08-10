# Verbatim locators — PMID 42397075 (Steinberg/Zonca/Abdellatif … Aqeilan, *Brain* 2026)

**Captured while the document was open**, 2026-08-09. Reading is **INCOMPLETE** — see the
coverage note at the end. This file exists so the locators survive the session: recovering
them later costs the reading twice, which this repository has already paid for fourteen times
in one day.

## Artifacts

| Role | Path | SHA-256 |
|---|---|---|
| `article_binary` | `files/fulltext/PMID42397075_Aqeilan2026.pdf` | `b6b44816bb5a029ad6dd3760dbf02ae94c5fcb69f8a9b5721f45c128bbf189a0` |
| `article_text` | `files/fulltext/PMID42397075_Aqeilan2026_fitz.txt` *(was `staging/fulltext_text_20260809/…`)* | `9c48aa0934648f58f8f5d3b39fa73b0f31e0b0d8d284914b32bd5e3f9b34bb17` |

### 🔴 Preflight of 2026-08-10 — the declared surface is intact and NOT reproducible from its declared method

Before completing this reading the surface was re-checked, and three things came out.

**1. The artifact is real and unaltered.** `staging/fulltext_text_20260809/PMID42397075.fitz.txt`
still exists, 91 848 bytes, and hashes to exactly the declared
`9c48aa09346…`. The 9 August receipt was accurate. It has now been **copied to
`files/fulltext/PMID42397075_Aqeilan2026_fitz.txt` with the digest preserved**, because
`staging/` is not where evidentiary artifacts live and a per-worktree `files/` is what the
merge-time validation reads.

**2. 🔴 But the declared extraction method does not regenerate it.** The receipt records
*"PyMuPDF 1.26.5 page.get_text() default mode, pages joined in order"*. Re-running exactly
that today, on a PDF whose digest still matches (`b6b44816…`), against the same PyMuPDF
1.26.5:

| join | sha256 |
|---|---|
| `''.join(pages)` | `bab5bc5d9605…` |
| `'\n'.join(pages)` | `f2f053fd7326…` |
| `'\f'.join(pages)` | `76943b7b9122…` |
| **declared** | **`9c48aa0934…`** |

None matches, and the byte counts differ by 942. **"Pages joined in order" is not a
reproducible specification** — it leaves the separator, and anything else the extractor did,
unstated. The artifact is fine; the *recipe* for it is not runnable, which is exactly the
failure the page-adjudication work fixed for crops in `adjudications.json` and which the same
argument covers here: **a derivation recorded only in prose decays silently; one a command
runs cannot.**

Nothing is retracted by this. The twelve locators of 9 August were verified against the file
that exists, and that file is unchanged. What is lost is the ability of a third party to
rebuild the surface from the record — which is the whole point of declaring an extraction
method.

**3. The surface itself is sound, and the first screen nearly said otherwise.** My initial
probe found zero occurrences of `P\s*[<>=]\s*0?\.\d+` in 90 000 characters of an experimental
paper — the classic *suspicion by absence* signature — plus two `q`-between-digits hits. Both
were artefacts of my own probe: the paper writes thresholds with **`≤` (16 occurrences)**, and
the two `q` hits are `16q21-q23`, a cytogenetic locus. `_refuse_suspect_surface` passed the
text and was right to. **My regex was incomplete, not the PDF** — and a screen that reports
absence needs its own pattern audited before the absence is believed.

### Surface decision for the completion

Continue on the **existing** `9c48aa09…` artifact rather than a freshly derived one, so the
twelve captured locators and the ones still to come share a single text surface. The
newly-derived `bab5bc5d…` file was discarded for that reason.

### What remains, with the artifacts now in place

- **Figures 2, 4, 5** — never opened. Figures 1, 3 and 6 were inspected on 9 August and
  changed the reading three times.
- **Five supplementary PDFs** in `files/fulltext/PMID42397075_Aqeilan2026_assets/`
  (`brain-2025-03809-File008` … `File012`), present since 1 July and **never opened**. The
  article states the detailed Materials and methods live there, which is why `methods` is
  conservatively `not_read`.
- **References** — not enumerated.
- No PMC deposit: `esummary` returns only `pubmed`, `doi` and `pii`, so per rule 5d the
  absence of a structured surface is recorded rather than assumed, and the PDF plus its
  fingerprinted derived text is the correct pairing.
| figure (Fig. 1) | `staging/figures_20260809/PMID42397075/PMID42397075_p32_x243.jpeg` | `7672818f61351ada7bf536d1ccc373e0769d1e5d8b3d93a5b83124f0e191c154` |
| figure (Fig. 3) | `staging/figures_20260809/PMID42397075/PMID42397075_p34_x247.png` | `e072368ea710687ffcd422532b160a687ad02f162cf5e3f78e5b603f59acbc56` |
| figure (Fig. 6) | `staging/figures_20260809/PMID42397075/PMID42397075_p36_x252.jpeg` | `23a4ecd347184d9bbe5ef1e59c818bc732486d77da3913b58ee4ae134cad8f4a` |

**Extraction method (rule 5c):** PyMuPDF 1.26.5 `page.get_text()`, default mode, pages joined
in order. Deterministic. No ML converter was used at any point, as reading aid or otherwise.

## Text-surface sentinel — PASSED

Run by hand before any locator was allowed to rest on the derived `.txt`, because a sibling
paper read the same day (PMID 33914858) **failed** it: its extracted text reads `P 5 0.05`
where the rendered page prints `P < 0.05`, and three independent extractors agree on the wrong
character. Until the executable gate exists, this check is manual and its result is recorded
here.

| Criterion | Threshold | This document |
|---|---|---|
| comparison characters `< > ≤ ≥` in a paper with statistics | zero → `SUSPECT` | **19** (16 × `≤`, 1 × `<`, 2 × `>`) → pass |
| `P\s*[45]\s*0?\.\d+` | any hit → `SUSPECT` | **0** → pass |
| C0 control characters outside tab/newline | any hit → `SUSPECT` | **0** → pass |

**Verdict: CLEAN.** Corroborated by `fitz`, `pdfplumber` and `pypdf` independently agreeing on
the correct character (12 well-formed `P ≤ 0.0…`). A `SUSPECT` surface may not back a
`complete_fulltext_read`.

🔴 **The sentinel is symptomatic, not causal.** The mechanism behind the 33914858 discrepancy
is **not established**: the `ToUnicode` hypothesis was tested and falsified, and coverage does
not discriminate in either direction. The only `DATO` is that the rendered page and the
extracted text disagree. So these criteria detect a *signature*, not a cause, and a clean
result is evidence of absence only for the signature — the rendered page remains the only
adjudicating surface.

## Figure surface

Figures were extracted with `page.get_images(full=True)` / `Document.extract_image` — these are
the **embedded images at their native stored resolution** (1430×1348, 1430×1589, 1430×1754),
not page renderings, so no resampling occurred and no upsampling ceiling applies. Inspected as
images, never through the text layer.

**Ceiling rule, recorded for the renderings that do occur** (as in the 600 dpi adjudication of
PMID 33914858): measure `effective_ppi` before rendering, render per panel rather than per
page, and never exceed the source's own effective resolution. Above that ceiling you are
enlarging, not looking — the extra pixels are interpolation and reading detail from them is
reading your own upsampler.

---

## L1 — MYC is the top upregulated gene in WWOX-KO radial glia

> "Differential gene expression analysis of WWOX-KO versus WT RG cells identified the
> proto-oncogene MYC (also known as c-Myc) as the top significantly upregulated gene in
> WWOX-deficient RGs (Fig. 3F)."

`surface: body` · p. 8, Results, *Inverse relationship between MYC and WWOX* · `artifact: article_text`

🔴 **Figure check qualifies the wording.** In the Fig. 3F volcano, MYC does carry the largest
logFC (~2.1), but **POU5F1 (OCT4) and EEF1B2 sit at the same saturated −log10(P) ≈ 300**,
along with TPM2 and SFRP1. Many P-values are capped at the axis maximum, so "top" cannot be
discriminating on P — it is a fold-change ranking. POU5F1 being co-top is not a detail: the
Discussion's own claim is that WWOX-deficient RGs "fail to properly silence pluripotency
programs", and OCT4 is that program. The paper does not comment on POU5F1 anywhere.

## L2 — first report of the inverse relationship outside cancer

> "However, this is, to our knowledge, the first time that an inverse relationship between
> WWOX and MYC has been observed in non-neoplastic tissue."

`surface: body` · p. 8, Results · `artifact: article_text`

## L3 — SCAR12 organoids are hyperexcitable (new)

> "Notably, SCAR12 patient-derived organoid recordings also showed hyperexcitability, a novel
> finding consistent with the epileptic seizures seen in patients2 and with the findings from a
> rodent model30."

`surface: body` · p. 6, Results · `artifact: article_text`

## L4 — 🔴 neuron-targeted gene therapy does NOT correct the radial-glia defect

> "Consistently, neuron-targeted AAV9-hSynI-WWOX restoration effectively rescued neuronal
> functional phenotypes without correcting RG abnormalities, suggesting that optimal
> therapeutic intervention may require stage and cell-type-specific targeting depending on
> disease progression."

`surface: body` · p. 16, Discussion · `artifact: article_text`

Corroborating locator, same reading:

> "Importantly, the infection with AAV9-WWOX of WOREE organoids did not affect the RGs, as
> appreciated by the absence of differentially expressed genes and cell-cycle abnormalities
> (Supplementary Fig. 10C-F), potentially pointing to the safety profile of this approach."

`surface: body` · p. 13, Results · `artifact: article_text`

**Why this matters to the model.** `working_model_current.md` describes P7 as *"the only
multi-pathway causal strategy demonstrated in preclinical models"* and lists Obeid 2026's
rescue across survival, growth, glucose, behaviour, myelination, gliosis and SWD/ECoG. It does
not record that the neuron-specific vector leaves the progenitor compartment untouched, while
this paper places the origin of the neurogenic defect **upstream of the neuron**, in radial
glia. The authors frame this as a safety property; it is simultaneously a coverage boundary.
Both readings are in the source and neither should be dropped.

## L5 — the progenitor-targeted alternative and its stated constraints

> "However, this approach is constrained by promoter specificity, vector targeting efficiency,
> and the time-limited nature of corticogenesis as a window for intervention."

`surface: body` · p. 16, Discussion · `artifact: article_text`

## L6 — 🔴 "similar to WT" is an interpretation, not a reported test

> "Remarkably, neuron-specific restoration of WWOX was sufficient to reduce hyperexcitability
> to a level similar to the WT organoids [Fig. 6A(ii)]."

`surface: body` · p. 13, Results · `artifact: article_text`

**Figure 6A(ii), inspected at original resolution** (`surface: figure`, artifact
`…_p36_x252.jpeg`): the significance brackets run **WT vs AAV9-EGFP** and **AAV9-EGFP vs
AAV9-WWOX**. There is **no bracket between WT and either treated arm**. On *percentage of
active ROIs* the treated arms sit at ~60% (SCAR12) and ~70% (WOREE) against WT ~45%; on *mean
amplitude* SCAR12-WWOX falls *below* WT while WOREE-WWOX stays above it. Only *events rate*
returns to near-WT. So "similar to WT" is not a result the panel reports — it is an
interpretation of an untested comparison. This is the CLAIM 005 lesson pointed the other way:
there, an absent significance marker was read as "not significant"; here, an absent comparison
is read as equivalence.

## L7 — the MYC-inhibition experiment does not isolate MYC

> "we performed a MYC inhibition experiment, using a multi-kinase inhibitor (A51) established
> to suppress Wnt and MYC expression62."

`surface: body` · p. 11, Results · `artifact: article_text`

The section is titled *"MYC dysregulation mediates neurogenic defects"*, but the tool used
suppresses **Wnt and MYC together**, and Wnt is independently implicated in the same figure
(Fig. 4I). The functional attribution to MYC specifically is therefore not separable with this
reagent. `PREMISE: INFERENZA`.

## L8 — protein abundance does not track phenotype across patient lines

> "This very low WWOX expression was consistent with all the lines previously established
> (Supplementary Fig. 1K-M)23, despite the different phenotypes observed in the source patients
> and the derived organoids2,5,23."

`surface: body` · p. 6, Results · `artifact: article_text`

Corroborates `CLAIM 030` (severity tracks residual function, not abundance) from a human
cellular model — the claim is currently `in observation` on a synthesis, with no primary source.

## L9 — no randomization, no blinding

> "No randomization or blinding was applied in this study."

`surface: body` · p. 5, Materials and methods, *Statistical analysis* · `artifact: article_text`

## L10 — only two genes separate SCAR12 from WOREE neurons

> "Notably, only two genes were found to be differentially expressed between SCAR12 and WOREE
> neurons, suggesting that considerable differences in the manifestations of the diseases do not
> arise directly from the neuronal population (Supplementary Fig. 8F)."

`surface: body` · p. 12, Results · `artifact: article_text`

## L11 — figure-only: the genotype gradient is tested on SOX2, not on SATB2

`surface: figure` · Fig. 1F, artifact `…_p32_x243.jpeg`, inspected at original resolution.

The text asserts a *"genotype-dependent gradient"* across genotypes (p. 6). In the **SOX2+**
panel, brackets include mutant-vs-mutant comparisons. In the **SATB2+** panel, every bracket
runs to WT only — there is **no mutant-vs-mutant test**, and all three mutant boxes sit near
zero. The gradient is therefore supported on the progenitor marker and asserted, not tested,
on the neuronal one. The WT SATB2 box also spans roughly 0–22% with outliers to ~60% (n = 9
organoids).

## L12 — caption misassigns its own panels

> "(D) Quantification of all the cell-attached recordings obtained from WT, WWOX-KO, WOREE and
> SCAR12 organoids, including those exemplified in (B)."

`surface: body` · Figure 1 legend, p. 28 · `artifact: article_text`

The raster plots are panel **(C)**; panel (B) is immunofluorescence. Same defect class as
Suzuki 2009's Figure 1. Cosmetic here — no conclusion rests on it — but recorded because
caption-level errors are how Wang 2012's false Tau contradiction entered.

---

## Coverage — this reading is NOT complete

| Section | State |
|---|---|
| abstract | read |
| introduction | read |
| methods | **partial** — the paper states "A detailed Materials and methods section is provided in the Supplementary material"; only the in-article Cell Culture and Statistical analysis subsections were read |
| results | read |
| discussion | read |
| limitations | read (in Discussion, p. 17) |
| tables | not_present — no numbered table; `pdfplumber` and `fitz.find_tables()` both return 0 |
| figures | **captions_only** — Fig. 1, 3 and 6 inspected at original resolution; **Fig. 2, 4 and 5 not opened** |
| supplementary | **not_read** — 5 supplementary PDFs are present in `files/fulltext/PMID42397075_Aqeilan2026_assets/` (brain-2025-03809-File008…012). They exist and were not opened. The methods live in there. |
| references | not enumerated (104 references) |

**Evidence depth: `partial_fulltext_read`.** `complete_fulltext_read` is refused: `captions_only`
on figures downgrades it by protocol, and the Methods are substantially in an unread
supplement. No receipt claiming completeness may be issued from this state, and the reading
debt for PMID 42397075 stays open.

**What a completion pass needs:** Fig. 2, 4, 5 at original resolution; the five supplementary
PDFs, above all the detailed Methods and Supplementary Figs. 7F–G (the A51 experiment) and
10C–F (the claim that RGs are untouched — L4's corroborating evidence currently rests on a
supplementary figure nobody here has opened).

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

## 2026-08-10, second run — the detailed Methods, the statistics, and Figure 5

`methods: not_read` existed because the article says the detailed Materials and methods live
in the supplement. They do: **`brain-2025-03809-File009.pdf`**, 14 pages, sha256
`19d1b1d7305315159f4319ece8e7da745015564cc94932058f1eeccd45aa6771`, sentinel PASS, 32 217
characters. Read in full. The other four supplements are now mapped: `File008` author
contributions (1 p.), `File010` supplementary figures (19 pp.), `File011` resource table
(5 pp.), `File012` uncropped western blots (10 pp.).

### 🔴 The MYC-inhibition experiment uses a multi-kinase inhibitor that also suppresses Wnt

> "we performed a MYC inhibition experiment, using a multi-kinase inhibitor (A51) established to suppress Wnt and MYC expression"

`surface: body` · Results. Dose 125 nM, weeks 8→15, compound provided by the Ben-Neriah
group. `evidence_relation: text_only`.

**The paper's functional pillar for the WWOX–MYC axis is a compound the paper itself
describes as suppressing two pathways.** Any causal attribution to MYC inherits that
ambiguity, and the authors state it plainly rather than hiding it. `PREMISE_TAG` ·
`PREMISE: INFERENZA` — "MYC inhibition rescues the phenotype" is supported here by an
intervention that is not MYC-selective.

For LEGEND this cuts two ways and both belong in the record: it weakens the causal claim, and
it is the first **pharmacological** intervention in a human WWOX-deficient neural model that
this corpus has seen — material for the therapeutic track, at hypothesis level only.

### 🔴 The three experiments carrying the central thesis are the three without independent differentiations

> "Experiments were performed in independent differentiations, except for single-cell RNA-seq, MYC inhibition and NSCs CHIP-Seq, using multiple biological replicates"

`surface: body` · Statistical analysis, supplement. `evidence_relation: text_only`.

The exception list is not incidental: **scRNA-seq, MYC inhibition and ChIP-seq are precisely
the three experiments the WWOX–MYC interplay rests on.** Read the sentence twice — everything
else was replicated across independent differentiations; these were not.

### 🔴 "No randomization or blinding was applied in this study"

`surface: body` · Statistical analysis. `evidence_relation: text_only`. Quoted verbatim and
without qualification.

Put beside the two papers read earlier today, from the same laboratory, this is a gradient:

| paper | blinding declared |
|---|---|
| `34747138` Repudi 2021 | *"Data analysis was performed while blinded to the genotype"* — unconditional |
| `42422765` Obeid 2026 | *"Data were analyzed in a blinded manner when feasible"* |
| **`42397075` Aqeilan 2026** | **none applied** |

Found rather than looked for: I read the statistics section to interpret the panels, and
recognised the sentence because I had read the other two today.

**What the statistics do well**, and it is more than the other two papers: normality tested
with Shapiro-Wilk, one-way ANOVA with Tukey or Dunnett, or multiple t-tests with
Benjamini-Hochberg FDR. Multiplicity correction is declared and named — neither of the other
two papers did that.

### Figure 5 (`fig_p35_1430x795.jpeg`, sha256 `103412d12ef433931b97cae6d946727d476f417398aa579c06b16fb4a1268b55`, 204 ppi)

`surface: figure`. Panels F and G: WT sits near 35% early / 65% late neurons, while WOREE and
SCAR12 both invert to roughly 65% early / 35% late, with log2FC against WT positive for early
and negative for late in both patient lines. **The shift toward early-born neuronal identity
is reproduced in two independent patient genotypes.** `evidence_relation: panel_only`.
n = 9094 cells.

#### 🟢 An error this session's own rule prevented

Panel E lists `canonical Wnt signaling pathway` among negatively-enriched GO processes. Given
that A51 suppresses Wnt, I was about to record that the rescue experiment inhibits a pathway
already down in the mutants. **I read the caption first, and it says the opposite of what I
assumed:**
> "(E) Representative Gene Ontology (GO) terms enriched in “late” cells compared to “early” cells, plotted as normalized enrichment score (NES)."

The contrast is **developmental stage, not genotype**. A negative NES for Wnt means it is
higher in *early* cells — ordinary developmental biology, and nothing to do with WWOX. The
inference would have been false, and it would have been my fourth cross-figure invention
today.

This is the rule written two commits ago — *a figure is not read until its caption is read* —
holding on its first test, and the difference from the earlier failures is only in ordering:
I looked before asserting rather than after being corrected.

## What remains, with the artifacts now in place

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

---

# PART 2 — re-read of 2026-10-04 (intake wave 10, Scientist Y)

`context_policy: SOURCE_FIRST` — the glia question was measured against the source before
`CLAIM 003` and `CLAIM 005` were opened; the comparison with those records is in the analysis
note, not here.

**This part is an APPENDIX, not a replacement.** Nothing above is edited. Part 1 and the
2026-08-10 completion pass were written against an artefact that no longer exists; this part is
written against a newly acquired one and says exactly where the two agree.

## A. Identity, measured from the front matter

| Field | Measured value | Surface |
|---|---|---|
| First author | Steinberg, Daniel J | p. 1 of 36, author line; PubMed esummary |
| Equal contribution | Steinberg, Zonca and Abdellatif, marked with a dagger | p. 1 author line |
| Last / corresponding author | Aqeilan, Rami I | p. 2, "Correspondence to" |
| Second corresponding | Davila-Velderrain, Jose | preprint front matter |
| Authors | 11 | author line |
| Journal, DOI | *Brain*; `10.1093/brain/awag239` | p. 1 |
| Version | advance article, **author-accepted manuscript** — not the typeset version | page banner |
| Licence | CC BY-NC 4.0 | p. 1 licence block |
| Article types | Journal Article only — **no retraction, no erratum, no expression of concern** | PubMed, 2026-10-04 |

🔴 **The identity error is in the artefact filenames, and it names the LAST author.** Every legacy
artefact is `PMID42397075_Aqeilan2026*`. Those paths are kept — earlier receipts declare them, and
renaming them would break the locator-to-artefact binding of readings already in the hash-chained
ledger — and the correction is recorded in a new `identity` block in the manifest. New artefacts
use `PMID42397075_Steinberg2026_OUP-AM*`.

**No second record may exist.** The bioRxiv preprint PPR960425 (`10.1101/2024.12.22.630016`,
v1 2024-12-25, v2 2025-09-25) is this work at an earlier version: different title, and its author
string omits the seventh author of the published version. A preprint is **not peer reviewed** and
never raises a claim's status.

## B. Artefact identity and the comparison the brief asked for

| | legacy (declared by receipts 01-04) | acquired 2026-10-04 |
|---|---|---|
| `article_binary` | `files/fulltext/PMID42397075_Aqeilan2026.pdf` | `files/fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf` |
| sha256 | `b6b44816bb5a029ad6dd3760dbf02ae94c5fcb69f8a9b5721f45c128bbf189a0` | `9775f766f68929e05665aa572196f4889083b501dc7f6792f1b9243e7dc0fd4b` |
| present on this host | **no** | yes, 36 pp, 3 340 736 bytes |

**Verdict: SAME DOCUMENT, DIFFERENT BYTES.** Measured, not assumed:

1. All **six** embedded figure images extracted from the new PDF reproduce the six figure
   SHA-256 digests the manifest already declared, **byte for byte**. They were written back to
   their legacy declared paths, so those six entries are now satisfied by identical bytes.
2. All **15** body snippets the manifest declares against the legacy derived text occur
   **verbatim, exactly once each**, in the text derived from the new PDF.
3. The difference is explained: the new PDF carries a per-page access stamp
   (`Downloaded from academic.oup.com/... by guest on 04 October 2026`) on **each of its 36 pages**.
   Its `ModDate` is the download date; its `CreationDate` is 2026-07-03.

🔴 **The reusable fact: this publisher endpoint is not digest-reproducible.** A second download on
another day yields a third digest for the same article. An artefact acquired here can be
re-verified by content (figure digests, snippet occurrence) but never by file digest.

**What did NOT come back: 16 artefacts.** A SHA-256 search over `/home/desktop` and
`/tmp/claude-1000` and a filename search over the whole filesystem found none of them. They are
the legacy PDF, its derived text, the published supplement `brain-2025-03809-File009.pdf`, and 13
images rendered from the supplementary figures volume. **Thirteen of the fourteen supplementary
figure locators recorded on 2026-08-10 therefore quote images that no longer exist anywhere.**
They are preserved verbatim and are **not** re-attested by this reading.

## C. The supplement: what was tried, and exactly what is missing

| Route | Result |
|---|---|
| Oxford Academic article page (the supplementary-data link) | **HTTP 403** — Cloudflare interstitial; no article HTML served, so the link could not even be read |
| PMC / Europe PMC `supplementaryFiles` | **No deposit.** `pmcid` null, `inPMC` N, `inEPMC` N, `hasSuppl` N, `isOpenAccess` N; the only full-text URL is the DOI, marked *Subscription required*. `pmc_pow_fetch` is **not applicable** — there is no PMC record to solve a proof-of-work page for |
| bioRxiv preprint supplement (v2, `DC1/embed/media-1.pdf`) | **Obtained — and it is not the published supplement.** 8 pages, titled *Expanded View figures*, captions for Figs. EV1-EV13 under the preprint's own numbering. **No Materials and methods section at all**, and its figure numbering does not map onto Supplementary Fig. 1-10 |
| bioRxiv preprint full PDF | **HTTP 429** across repeated attempts with back-off; not obtained in this session |

No payment, no interlibrary loan, no author contact.

🔴 **Still missing, exactly:** the published **Supplementary material** of *Brain* `awag239` — above
all the **detailed Materials and methods**, which the article body relegates there in full
(*"A detailed Materials and methods section is provided in the Supplementary material."*), and the
**supplementary figures volume**, cited **42 times** in the body as `Supplementary Fig.`. What
would unblock it: a non-interstitial fetch of the Oxford Academic supplementary-data endpoint, or
the operator supplying the file as they did for PMID 33914858.

## D. What bears on the model — measured on panels, with what is measured vs inferred

### D1. Glia, myelin and oligodendroglia — the wave-8 question

**Counted in the body text** (36 pp): `myelin` 3 occurrences, `oligodendro` 2, `astrocyt` 1,
`microglia` 1 — and of those seven, **four are in the reference list**, one is an introduction
citation of the mouse literature, and the remaining two are the *same* sentence and its figure.
`OLIG`, `SOX10`, `PDGFRA`, `MBP`, `GFAP`, `AQP4`, `S100B`, `OPC`: **zero occurrences each**.

🔴 **No glial cell type is annotated in these organoids.** The clustering yields five labels —
`cRG`, `RG`, `oRG`, `NP`, `Neu` (Fig. 2A, n = 18 007 cells). Glial progenitors are **folded into**
the mixed RG cluster, and the authors decline to resolve it further:

> of outer RGs (oRGs), cycling RGs (cRGs), and a mixed population of vRGs, neuroectodermal

There is no oligodendrocyte cluster, no astrocyte cluster, no microglial cluster, and no
myelin-protein, g-ratio or OPC measurement anywhere in the paper. **This is an earned null.**

🔴 **The one oligodendrocyte statement, and what it actually is.** The body says, of AAV9-WWOX
treated versus untreated WOREE organoids:

> promotion of oligodendrocyte differentiation and myelination, and synaptic function (Fig. 6D

Measured at **panel 6E** (the term is in 6E, not 6D): it is **one bar in a gene-set enrichment
chart**, `oligodendrocyte specification & myelin`, NES about +1.3, among four positively enriched
terms (with OXPHOS electron transport chain, hippo signaling, oxidative stress). The comparison is
`WOREE^WWOX+ versus WOREE` **in neuronal progenitors and neurons** — the caption says so. It is a
**transcriptional signature read in neurons**, not a measurement of any oligodendrocyte, in a
model that contains none.

🔴 **And the same panel moves lipid synthesis the other way.** Two of the four *negatively*
enriched terms are `cholesterol production inhibition` and `glycerophospholipid biosynthesis` —
the biosynthetic substrate of myelin — in the same contrast, same panel.

⚠️ **The caption does not name the term the body draws from it.** Figure 6E's own caption reads:

> an increase in OXPHOS and oxidative stress terms in WOREE-WWOX compared to WOREE,

and continues with *lipid metabolism* downregulated. The oligodendrocyte/myelin term appears in
the **panel** and in the **running text**, and **not** in the caption of the panel it belongs to.

🔵 **The only oligodendrocyte-lineage number in the paper is in external public data.** Figure 3B
plots WWOX expression by cell type in a published post-conceptional-week-16 human fetal single-cell
dataset (not these organoids): RG highest (median about 0.57), IP about 0.48, ExN/InN about 0.20,
Other about 0.14, **Oli about 0.10, Mic about 0.07** — the two lowest of seven. **Transfer limit:**
external data, 16 pcw, i.e. before myelination begins; it is an expression gradient, not a
requirement test, and it says nothing about an adult or challenged oligodendrocyte.

### D2. Composition — and a sentence the panel does not support

The body states:

> number of total recognized RG cells (RGs) (Fig. 2D-F), while SCAR12 organoids (modeling a

relatively milder disease) exhibited an RG population similar to WT, having just assigned a
*"prominent increase"* in RGs to WWOX-KO **and WOREE**.

🔴 **Measured against panel 2F's own axis ticks** (ticks located by pixel scan at -3, -2, -1, 0, +1;
229 px per log2 unit at 900 dpi; bar extents read against them):

| genotype | RGs log2FC | Neu log2FC |
|---|---|---|
| WWOX-KO | 0 to **+0.98** | **-2.36** to 0 |
| SCAR12 | **-0.25** to 0 | 0 to **+0.18** |
| WOREE | 0 to **+0.07** | -0.04 to -0.01 |

**The ordering is the opposite of the sentence.** WOREE's radial-glia deviation (+0.07) is the
**smallest** of the three; SCAR12's (-0.25) is roughly **three to four times larger in magnitude**
and runs the **other way**. "Similar to WT" describes WOREE, not SCAR12. The sentence's central
contrast between the two patient genotypes is not what the panel it cites plots.

⚠️ **Caveat stated against myself:** the RGs bar is drawn as a colour composite of the RG subtypes,
so a single scalar read from its extent is the extent of the block, not necessarily one fitted
log2FC. That caveat applies **equally to all three rows**, which are drawn identically — so the
*ordering* above is robust even where the absolute value is not.

🔵 **This refines, and does not overturn, the 2026-08-10 reading**, which recorded "-2.6 ... +0.55 ...
SCAR12 and WOREE both within roughly 0.2". Measured on bytes that exist: Neu -2.36 and RGs +0.98
for the knockout (a near-doubling of the RG fraction, larger than the earlier figure), WOREE within
0.07 (tighter than the earlier figure), SCAR12 at -0.25 (slightly outside it). **The qualitative
finding — the composition phenotype is almost entirely the engineered knockout's — stands and is
strengthened.** Cell counts recomputed from panel D: 5649 + 3020 + 3422 + 5916 = **18 007**, which
is the n printed on panel A. ✅

### D3. MYC — shared by the patient lines, unlike composition

Figure 3K, `SOX2+MYC+/SOX2+`, week 16 organoids: WT about 20 %, WWOX-KO about 60 % (`***`),
SCAR12 about 50 % (`**`), WOREE about 55 % (`****`), each against WT. **All three mutant genotypes
are raised**, including both patient-derived lines. `n` is **organoids** and is single-digit in
three arms: WT 7, WWOX-KO 5, SCAR12 8, WOREE 11. Figure 3L, 2D NSCs: WT about 45 %, KO1 about 67 %
(`**`), KO2 about 75 % (`***`), KO1 vs KO2 `n.s.`; "data collected from two experiments".

🔵 **So the MYC lesion separates from the composition phenotype**: shared across genotypes where the
cell-fraction change is not. This is the same direction as the 2026-08-10 reading of
Supplementary Fig. 4, reached here from a main figure that still exists.

### D4. Cell cycle — the abstract's phase sentence, against the phase panel

The abstract:

> dynamics leading to an accumulation of cells in the G2/M and S phases, overexpression of the

Measured at Figure 4C (`cell proportion log2 FC (KO/WT)` in RG cells): **S about +0.77**,
**G2M about +0.50**, **M about -0.37**, **G1/G0 about -0.28**. The `S` and `G2M` bins rise; the
separately plotted **`M` bin falls**. Written as "G2/M and S", the abstract merges a bin that rises
with a phase name whose own bin falls. The panel carries **no error bars and no significance
marks** — it is a point estimate from the single scRNA-seq experiment (`WWOX-KO n = 2396 cells`,
`WT n = 2152 cells`, panel A).

### D5. Confirmed on the new bytes

Figure 4J (`Mean MYC promoter binding density`, histogram of 1000 random gene sets peaking about
1.25, spanning about 0.9-1.8): the grey wild-type marks sit at about 1.85-1.88, **outside** the
null; the blue knockout marks sit at about 1.10-1.12, **inside** it. The 2026-08-10 finding — the
panel supports "not significant for the KO", which the caption's single wild-type *P* value does
not state — **is confirmed on an artefact that still exists.**

## E. What this paper does NOT say

- It does not measure any oligodendrocyte, astrocyte, OPC or microglial cell, in any genotype.
- It does not measure myelin, myelin protein, g-ratio, axon counts or any myelination outcome.
- It does not test cell autonomy of anything: there is no cell-type-restricted deletion here.
- It does not report a WT-versus-treated statistical comparison for the rescue (Part 1, Fig. 6A(ii)).
- It does not state the significance of the knockout arm of Fig. 4J.
- It reports **no randomization and no blinding**, and the three experiments the WWOX-MYC thesis
  rests on (scRNA-seq, MYC inhibition, NSC ChIP-seq) are the three performed **without independent
  differentiations** (Part 1, from the statistics section).
- Its detailed Materials and methods are **not in the article**, and are not obtainable today.

## F. Genotypes and the transfer limit

The lines are an engineered isogenic constitutive knockout (`JH WKO`, two clones) and
patient-derived iPSC lines of two syndrome classes — WOREE and SCAR12 — in **unguided cerebral
organoids**, week 16. A constitutive knockout models neither human missense allele. SCAR12 and
WOREE are different allele classes and this paper itself shows them behaving differently; nothing
measured in one may be carried to the other, and nothing here may be carried to the reference
genotype's own allele pair. Every datum above is bounded by that.

## G. What I did NOT read in this pass

| Section | State |
|---|---|
| abstract, introduction, results, discussion, data availability | read |
| methods | **not_present in the article** — relegated in full to a supplement that is unobtainable |
| figures | Figures 2, 3, 4 and 6 read **as rendered images**; Figures 1 and 5 **not opened** in this pass (read on 2026-08-09 / 08-10 against the lost artefact) |
| tables | not_present |
| supplementary | **unavailable** — see section C |
| references | not re-enumerated in this pass (104, enumerated 2026-08-10) |

**Evidence depth of this pass: `partial_fulltext_read`.** `complete_fulltext_read` is refused, and
the reason is not a formality: the methods are in a supplement nobody can open, and two main
figures were not opened today.

**Classifier halt, recorded as the brief requires.** One command issued during the glia sweep was
stopped by a safety classifier while running. The read was not re-attempted in other words; it was
redone with narrow script slices that print bounded line ranges, which is how every passage in
section D was then read. No passage was skipped as a result.

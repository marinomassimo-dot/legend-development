# Blind locator audit — R2 (post-onset restoration set)

Audit date: 2026-11-05. Auditor: blind. Inputs received: the 64 `(triple_id, source_id,
proposition, quote+section)` rows only. No dossier, no registry, no receipt, no manifest, no
reader identity. Every source artefact was acquired independently by the routes listed below.
Verdicts follow `legend-locator-audit`: does the quote carry the proposition, and does the
source say MORE or LESS than the proposition claims.

Not medical advice. No dose, schedule, route or preparation is reproduced anywhere in this
record; where a source sentence carried one, the quotation was shortened.

## Counts per verdict

| Verdict | Rows |
|---|---|
| SUPPORTED | 55 |
| OVERSHOOT | 7 |
| UNDERSHOOT | 0 |
| NOT_IN_SOURCE | 1 |
| UNVERIFIABLE_SURFACE | 1 |
| **Total** | **64** |

Every quote that was supposed to be a quote was found in its source. One row declared no
quote. No row failed because its artefact could not be reached.

## Non-SUPPORTED rows, with the exact reason

### NOT_IN_SOURCE — blocks canonical use until re-located

**R2-R16 · PMID 36173683.** The quote is verbatim in the source, but it is the sentence
about the *survival* of the control-treated arm. The proposition is about total seizure
frequency and interictal acute spikes three weeks after treatment, and the quote carries
nothing about either. This is a mis-assigned locator, not an unsupported claim: three
sentences further on, the same Results subsection states that acute spikes were reduced in
treated animals three weeks after treatment, that no treated animal seized during the
recording, and that five seizures were recorded in the untreated arm. Re-locate to that
sentence and the row becomes supportable.

### OVERSHOOT — must be rewritten or the divergence argued before commit

**R2-R13 · PMID 35013317 — wrong comparison group.** The quoted cortical result (no
differentially expressed gene against wild type) is exact. The proposition then states that
"the hippocampus retained 163". The source's 163 is the *treated versus control-treated*
hippocampal contrast — genes the treatment changed — introduced by "the majority of them were
rescued". A residual count against wild type in hippocampus is never reported. The
proposition converts a treatment-effect count into a residual-defect count, which reverses its
meaning. (Secondary: a bulk transcriptome is binned here under cognition and behaviour.)

**R2-R18 · PMID 36173683 — grade contradicts the source's own reading.** The facts are
exact: open-arm time fell in every treated group, and fell equally in treated wild type. But
the grade "worse", and the inference "a property of the intervention and not a rescue", are
the reader's. The source's very next sentence reads the same result as evidence that the
intervention "normalized behavioral markers of disease". The divergence may well be the better
science, but it is a divergence and must be stated as one rather than carried as a grade.

**R2-R28 · PMID 32610343 — asserted dissociation.** "about 17 percent of control" and the
correlation with myelin level are verbatim. "tracked the myelin level rather than the
functional benefit" asserts a dissociation the source does not make: it introduces the
measurement to ask whether myelin contributes to the functional improvements and concludes
that the intervention "increases functional myelin, with improvements in motor performance and
lifespan".

**R2-R31 · PMID 32610343 — one item added to a wild-type-level list.** The quoted abstract
sentence reads "increased myelination **and** restored nerve conduction velocity, motor
function, and lifespan to wild-type levels". Myelination is deliberately outside the
restored-to-wild-type list, and the body confirms why: germline suppression reached nearly 50
percent of wild-type myelinated axons with incomplete compaction, and rotarod performance was
slightly reduced at eighteen months. The proposition moves myelination into the list.

**R2-R48 · PMID 35065785 — whole-cohort denominator attributed to the pre-onset arm.** "20 of
25 (80%) assessed" is the assessed treated cohort. The treated cohort was mixed: by the
baseline table, 20 of 29 were pre-symptomatic and 9 early-symptomatic. The source never
reports 20 of 25 for the pre-symptomatic subset, and the coincidence of the number 20 makes
this an easy row to misread. The grade "full" also sits against five of twenty-five who did
not show normal acquisition.

**R2-R55 · PMID 28100454 — a magnitude that exists only in a figure.** Apoptosis falling from
about half of counted cells to about one in twenty is verbatim with numbers, and "astrogliosis
... was less pronounced" is in the text. The "macrophage counts reduced about six fold" is
not: the figure caption says only that the counts "confirm the significant reduction in
numbers in the fully treated mice", and the Methods merely state that stained macrophages were
counted. The fold value is a panel reading and must be declared as an attestation, not carried
as a reported quantity.

**R2-R62 · PMID 37901435 — timing field wrong, and the error weakens a negative.** The quoted
failure is exact and holds at both exposures tested. But the compound arm began at P10, while
this model's phenotype is a single lethal seizure at P14 (untreated median survival 15 days).
Dosing therefore began *before* onset, not at onset. The row currently reads as a post-onset
failure; the source supports the stronger statement that the compound failed even when started
ahead of onset.

### UNVERIFIABLE_SURFACE

**R2-R58 · PMID 28100454.** The quote field is `attestation_without_quote`, so there is
nothing to match; the verdict is structural. It is also avoidable: the Results carry a
quotable sentence reporting significantly prolonged survival in treated against mock-treated
animals with both means and the test statistic, and the figure caption repeats the same
values. The row should carry that verbatim locator instead of an attestation.

## Surface defects inside SUPPORTED rows

These did not change a verdict but each one is a locator that does not describe itself
correctly, and the fourth audit trigger exists for exactly this class.

| Row | Defect |
|---|---|
| R2-R12 · 35013317 | Section given as "Supplementary results". The quote is verbatim in the **main Results** (behavioural section), referring to a supplementary figure. The sentence also opens with a hedge ("slightly inferior latency to fall") that the proposition drops. |
| R2-R19 · 36173683 | Section given as "Supplementary results". The quote is verbatim in the **main Results**, in the subsection the authors title as tolerability in wild type. The source reports the reduction with no statistic ("was observed"). |
| R2-R50 · 35715566 | Quote is presented as contiguous but the source interposes a confidence interval inside the parenthesis. The elision is unmarked. Substance unaffected. |
| R2-R41 · 39847501 | Section attribution is **correct** (the phrase is in the Figure 3 caption, and again in Figure 4 for pyramidal neurons), but note the comparator: "no significant differences between genotypes" compares treated null with treated wild type, and the source states the treatment itself shifted wild-type interneuron firing. The proposition is transparent about this; a downstream reader may not be. |
| R2-R24, R2-R15 | Survival graded "full" where the source reports a censored figure — a predetermined eight-month endpoint (R2-R24) and a median stated as beyond 300 days (R2-R15). Neither paper claims a normalised lifespan. |
| R2-R43 · 39847501 | "no myelin or glial endpoint was measured" is a whole-document absence claim that no single quote can carry. Verified by inspection: no myelin or oligodendrocyte endpoint exists; glial markers appear only to show the transgene is absent from glia. |
| R2-R21 · 36173683 | Weight was measured at P40; the row's follow-up to P150 belongs to the survival endpoint of that arm. |
| R2-R65 · 41883162 | Abstract says "disease-associated phenotypes"; the cognition-and-behaviour binning is the reader's. |
| R2-R04, R2-R33, R2-R45 | The quote covers one element of a multi-element row (radial maze; untreated onset window; pre-onset timing). The remaining elements are supported, by adjacent sentences in the same section — but the locator alone does not reach them. |

## Artefacts read

All downloads are outside the repository, in
`/tmp/claude-1000/-home-desktop-legend-development/9400b253-25a0-4b03-8822-96361325fc16/scratchpad/audit_R2/`.
No contact address or e-mail parameter was sent to any service; no service requiring one was
used.

| Source | Route | File | Bytes | sha256 |
|---|---|---|---|---|
| PMID 35013317 | Europe PMC REST fullTextXML | `ft_35013317_PMC8748984.xml` | 187003 | `728dfa04be02f9a2b80f1a569fc0e0113af2f90669fa13626593f554327edc62` |
| PMID 36173683 | Europe PMC REST fullTextXML | `ft_36173683_PMC9746904.xml` | 144514 | `6714d5fc7f5f1c056e68113bf7b9b6ecd87526a11c0ee70387423b5a1993a703` |
| PMID 39847501 | Europe PMC REST fullTextXML | `ft_39847501_PMC11870736.xml` | 146693 | `61ab73c4264ebec5b1c1638187f4464007f89379899186eee573a6b8477a7986` |
| PMID 32610343 | Europe PMC REST fullTextXML | `ft_32610343_PMC7810164.xml` | 154697 | `f8374f8752df1ee987bc3de206ab4621fc6376007f35dbbace55d9fbe33c8b7f` |
| PMID 31943325 | Europe PMC REST fullTextXML | `ft_31943325_PMC7064908.xml` | 79882 | `dddc9a6f01e0007086b4cecfe7714cea492e441628ba4d0960995568a29c4ce9` |
| PMID 35715566 | Europe PMC REST fullTextXML | `ft_35715566_PMC9205281.xml` | 140419 | `06b73cf63373d2f82537cf452e221b7cd0faa98e55b4c7d6092e78245547dc5a` |
| PMID 35065785 | Europe PMC REST fullTextXML | `ft_35065785_PMC8795071.xml` | 117194 | `b7d3f944f3e19e3e2f6dc75da2a448ff293d946795c0ac23c1e2bb8007900cba` |
| PMID 37901435 | Europe PMC REST fullTextXML | `ft_37901435_PMC10603267.xml` | 85881 | `3cc7aeb464ce512c7eb16842c977c998d88be247f9780b95fbee77cf62d2cf06` |
| PMID 28100454 | PMC article HTML (full body) | `pmchtml_28100454.html` | 262181 | `5b76527b8d0898a63912794242609a8f4929c4231634fc1aa8742bbba5cb90f1` |
| PMID 31607539 | NCBI efetch `db=pmc` (front matter + abstract) | `ef_31607539_PMC6952031.xml` | 13199 | `bd63514490f7cb07f111d5e99ef581c2a2b2a6f69ac4fa0f53e8227a5801023b` |
| PMID 32848094 | NCBI efetch `db=pubmed` (abstract) | `abs_32848094.xml` | 8786 | `8716723495429b3c9d009b4def06d8e09090f153b73d06a388547939917eca83` |
| PMID 41883162 | NCBI efetch `db=pubmed` (abstract) | `abs_41883162.xml` | 42738 | `f72ed84991a40eda122544ed81759c4a23b83e07618e4a8ab926e18e21047c95` |

Failed or partial routes, recorded for completeness:

| Attempt | Outcome |
|---|---|
| Europe PMC fullTextXML for PMC5837386 (28100454) | HTTP 500; record is not open access. Recovered in full from the PMC article HTML. |
| Europe PMC fullTextXML for PMC6952031 (31607539) | HTTP 500; record is not open access. |
| NCBI efetch `db=pmc` for 5837386 and 6952031 | Both return front matter with "The publisher of this article does not allow downloading of the full text in XML form." |
| Publisher pages for 10.1093/brain/aww351 | HTTP 403 (both the DOI redirect and the journal article page). Not needed: the PMC HTML carried the body. |

## What could not be reached

Nothing that an audited row depended on.

- **PMID 31607539** has no accessible body text by any open route tried. Its single row
  (R2-R63) is an abstract-level row whose quote is in the abstract, which was retrieved, so the
  row is fully auditable. Anything beyond the abstract for this source is unverified.
- **PMID 32848094 and PMID 41883162** have no PMC record. Both their rows (R2-R64, R2-R65) are
  declared abstract-level and quote the abstract, which was retrieved.
- **Supplementary material** was not retrieved for any source. Two rows name
  "Supplementary results" as their section (R2-R12, R2-R19); in both cases the quote proved to
  be in the main text, so no supplementary file was needed. No other row depended on one.

## Method notes

Normalisation applied before matching: whitespace, case, unicode dashes (including em-dash to
hyphen), Greek letters (beta, mu), degree and inequality signs, combining accents, and
repeated HTML-entity decoding — the last was necessary for the PMC HTML source, where entities
are double-escaped and a quote containing em-dashes (R2-R57) will not match without it.
Figure captions were matched as text where the row cited one; two caption-cited rows (R2-R34,
R2-R41) matched verbatim in their captions and are therefore ordinary verified quotes, not
attestations. Each row was checked element by element — model, timing relative to the stated
onset, endpoint, outcome grade, effect size and follow-up — against the quoted sentence first
and then the surrounding sentences, for hedges, denominators, species, age and comparison
group.

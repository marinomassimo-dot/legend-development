# PMID 42128308 — Aqeilan et al. 2026, *Neurobiology of Disease* 107446

**WWOX in brain development and disease: Molecular mechanisms and therapeutic opportunities**
· DOI 10.1016/j.nbd.2026.107446 · **Review** · FT-045

🟡 **PARTIAL READ of 2026-08-10.** Section 11 read in full; sections 1–10 and 12 not read.
Opened after `PMID 42397075` closed, and stopped at a closed boundary rather than half-way
into another section.

## 🔴 Degraded surface class, recorded rather than assumed

**No PMC deposit.** `esummary` returns only `pubmed`, `doi` and `pii`; `elink` to `pmc`
returns no linkset at all. Per rule 5d the absence is recorded, and the paper enters the class
that has no structured surface: the PDF plus a derived text artifact is the only pairing
available.

| artifact | kind | sha256 |
|---|---|---|
| `files/fulltext/PMID42128308_Aqeilan2026.pdf` | `article_binary` | `520c2743630b86e5e6c2af7a3e2f527d7a31ab7810839ed275c87b0d804d6be7` |
| `files/fulltext/PMID42128308_Aqeilan2026_fitz.txt` | `article_text` | `9e05945335845b06959ac0ec78d3de2a167a606b44398f1961e67adfc8f75576` |

**Extraction recipe, stated so it regenerates** — this is the lesson from this morning, where
`PMID42397075`'s declared method left the separator unstated and no variant reproduced the
digest:

> PyMuPDF 1.26.5 · `page.get_text()` default mode · `''.join(pages)` · **no separator, no
> trailing newline** · 17 pages · 131 033 bytes · 130 519 characters.

**Sentinel PASS.** Two `<` and seven `>`, fifteen occurrences of `significan*` — for a review
carrying no primary statistics, that ratio is expected rather than suspicious, and the
suspicion-by-absence rule does not fire because comparators are present.

## 🔴 The finding: the same fact is a feature in one paper and a regulatory obstacle in the review

Section 11, on gene-therapy challenges:

> "dorsal root ganglia (DRG) pathology and peripheral organ involvement observed after systemic or high-dose AAV administration"

> "which has emerged as a key regulatory concern in pediatric CNS gene therapy programs"

`surface: body` · `panel_text_relation: text_only` · **found** — I was reading section 11 for
the therapeutic thread and recognised it against a locator I had recorded hours earlier.

**Read this against `PMID 42422765`**, from the same laboratory, where I recorded:
*"WWOX protein was also detected in the sciatic nerve of HD-treated mice"*, which that paper
presents as *"supporting functional relevance in the peripheral nervous system"*.

**The same biodistribution fact is framed as functional relevance in the primary and as
dose-limiting toxicity in the review.** Neither framing is wrong: peripheral neuronal
transduction after neonatal ICV is simultaneously evidence that the vector reaches PNS neurons
and the mechanism by which DRG pathology arises. But a reader taking only the primary would
carry the positive half. 🔴 `PREMISE_TAG` — any inference that neuron-restricted AAV9-WWOX is
CNS-confined is contradicted by the primary's own data and flagged as a regulatory concern by
the same group's review.

## The other translational constraints the review names

- **Pre-existing immunity.** *"A sizable portion of the population carries pre-existing
  antibodies against AAV vectors"* — with NAb-based exclusion assays already developed for
  trials. `text_only`.
- **Packaging capacity.** WWOX itself is small, but promoters, regulatory elements and tags
  push constructs past the limit — which is exactly the trade-off `PMID 42422765` navigated
  when it removed WPRE and had to raise the dose six-fold to recover efficacy.
- 🔴 **Spatiotemporal fidelity.** *"any effective strategy must recapitulate its natural
  spatiotemporal expression patterns"* — set beside the finding recorded today that AAV9
  rescue produces WWOX from **0.4 to 7 times wild type** across lines treated with the same
  vector, this is a requirement the current vector demonstrably does not meet. The review
  states the requirement; the primary shows the seventeen-fold spread. Neither says it about
  the other.
- **Epigenetic modulation as a distinct niche.** *"useful for enhancing residual endogenous
  WWOX expression in hypomorphic states"* — explicitly **not** a replacement for gene
  augmentation in severe loss-of-function WOREE, but potentially relevant for SCAR12 and
  missense alleles where residual protein exists. This is the first statement in the corpus
  that separates the two therapeutic strategies by allele class.
- **Non-viral alternative.** LNPs for WWOX mRNA or regulatory cargo, with BBB delivery named
  as the open problem.

## What remains

Sections 1–10 and 12 unread: protein networks, brain homeostasis, Alzheimer's, Parkinson's,
multiple sclerosis, autism, the WWOX-related epileptic encephalopathies section, the clinical
and genetic insights section, and the preclinical models section. Sections 8–10 are the ones
most likely to carry transferable content; sections 4–7 are the cross-disease axes where
parity of sources says the useful detail often lives.

**This is a review**, so nothing here is `DATO` in its own right: every statement is either
the authors' framing or a claim traceable to a primary. The value is the map of the field's
current positions from the group that leads it — and, as section 11 shows, the places where
that map disagrees with the group's own primaries.

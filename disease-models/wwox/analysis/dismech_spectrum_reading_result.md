# Reading Oliver 2023 to unblock the spectrum claim — and why it did not

> **Non-canonical.** A reading result and its verbatim locators. It changes no canonical
> file; the registry updates it implies are commit candidates, not edits.
>
> Public, disease-level, de-identified. Nothing here is medical advice.

**Date:** 2026-08-04 · **Paper:** PAPER 018 · Oliver KL, Trivisano M, Mandelstam SA, et al.,
*Epilepsia* 2023;64:1351–1367 · PMID 36779245 · PMC10952634 · CC BY-NC-ND
**Receipt:** `FTR-20260804-36779245-01` · **depth: `partial_fulltext_read`**

---

## Why the export is still blocked

The goal was to give CLAIM 017 a source with a complete-read receipt, which would make the
WOREE/SCAR12 spectrum exportable and give §10's shared module the evidence it lacks.

**It did not.** The reading is honestly `partial`, and the reason is narrow: the four figures
were available only as captions.

| | |
|---|---|
| Retrieved | JATS full text from Europe PMC — abstract, introduction, methods, results, discussion, Tables 1 and 3 inline |
| Not retrieved | the four figure **images**, and two supplementary items |
| Attempts that failed | PMC OA package (404) · OA PDF path (404) · direct `/bin/` image URLs (301, unresolved) · Europe PMC PDF endpoint (404) |

**Figure 4 *is* the survival analysis** behind the mortality claim, and Figure 3 is the
variant map. Reading either from its caption is precisely the failure that put
`captions_only` in this repository's coverage vocabulary on 2026-07-26, when a figure was
found not to show what its own legend claimed.

So the honest depth is `partial_fulltext_read`, and the §5 gate requires
`complete_fulltext_read`. **Nothing about the export changes.** Declaring a complete read
would have unblocked it, and nobody would have checked.

## What the reading did establish

### CLAIM 017 is directly supported, and qualified

> *"The phenotypic spectrum of WWOX pathogenic variants extends to a milder phenotype
> comprising spinocerebellar ataxia (SCAR12), epilepsy, and intellectual disability."*
> — Introduction

> *"This has led to the suggestion that a WWOX gene dosage effect may exist, with the severe
> DEE phenotype associated more often with null loss-of-function variants (e.g., deletions),
> whereas the milder SCAR12 phenotype has only been reported with missense variants."*
> — Introduction

But the clean picture does not survive the Discussion:

> *"there is no regional predilection for missense pathogenic variants within the gene
> leading to WWOX-DEE versus SCAR12"* — Discussion

> *"This distinguishes the profound WWOX-DEE from the rarer WWOX SCAR12 phenotype, albeit
> **both may arise due to biallelic missense variants**."* — Discussion

**The spectrum is not cleanly genotype-partitioned**, and position in the gene does not
predict which end you land on. That is a real qualification of CLAIM 017 as currently worded.

### It independently corroborates CLAIM 030, from a source LEGEND had not read

> *"Interestingly, p.Pro47 has been associated with two pathogenic variants; the more
> conservative change to threonine was found in SCAR12 compared with the arginine
> substitution found in WWOX-DEE."* — Discussion

CLAIM 030 — *"severity tracks residual protein FUNCTION, not abundance"* — rests on exactly
this observation. Finding it stated independently in a paper the model had not read is the
strongest kind of confirmation available here.

### The mortality gradient, with its numbers

> *"We stratified all 75 cases into one of three genetic groups: (1) null/null (n = 45),
> (2) null/missense (n = 15), (3) missense/missense (n = 15)."* — Results

> *"survival was much poorer for the double null group compared with the patients who had at
> least one missense pathogenic variant (p-value = .0085, log-rank test)"* — Results

> *"By the age of 10 years, the gap in survival probability widened, with the null group at
> 25% whereas the missense groups remained somewhat steady at >60%."* — Results

> *"the presence of at least one missense variant increases 5-year survival probability from
> <50% to >75%"* — Discussion

This is the source of the `p = .0085` already quoted in CLAIM 033, now read rather than
cited from an abstract.

### SCAR12 is severe, and differs by degree

> *"In the milder WWOX phenotype of SCAR12, early development is slow, with seizure onset
> from 9 to 12 months, providing support for developmental impairment due to WWOX pathogenic
> variants."* — Discussion

Milder does not mean mild: slow early development, epilepsy, intellectual disability. The
difference from WWOX-DEE is one of degree along one spectrum, not of kind — which is the
basis on which the exporter routes molecular findings to both entries.

### A limitation the paper does not declare

The paper carries no limitations section. Its genotype classes are `null` versus `missense`
coded from variant type — and it says itself that a missense may be hypomorphic *or* as
severe as a null. **The classification is a proxy for residual function, and the paper's own
p.Pro47 observation shows the proxy failing at a single residue.** CLAIM 033 already says
this; the reading confirms the paper does not.

## What would unblock the export

One thing: **the figure images.** The text is read, the locators are captured, the tables are
read. If Figures 3 and 4 can be obtained — from the publisher, from an institutional
subscription, or as a PDF by any route — the receipt becomes a complete read and CLAIM 017
becomes exportable in the same step.

Until then the spectrum remains what it was: the justification for routing, recorded as a
curation judgement, and not itself an exportable node.

## Commit candidates this implies

Not applied — the four current files change only through `BATCH_COMMIT`.

1. **PAPER 018** — evidence depth from *"abstract + frammenti Scholar Gateway"* to
   `partial full text` with receipt `FTR-20260804-36779245-01`; claim links from `pending` to
   013, 017, 030, 033.
2. **CLAIM 017** — add the qualification that no regional predilection distinguishes
   WWOX-DEE from SCAR12 missense variants, and that both may arise from biallelic missense.
3. **CLAIM 033** — record that Oliver 2023, the source of its own `p = .0085`, does not
   declare the proxy limitation that CLAIM 033 raises against it.
4. **PAPER 008** — it is a placeholder (*"multiple / pending normalization"*, *"Aldaz/Banne
   cluster"*), not a citable paper. CLAIM 008 rests on it. This is a registry-hygiene defect
   found on the way and worth its own entry.

## Related

[`dismech_phase3_dryrun_result.md`](dismech_phase3_dryrun_result.md) · [`dismech_export_spec.md`](dismech_export_spec.md) §5 · [`framework/protocols/fulltext_read_receipt.md`](../../../framework/protocols/fulltext_read_receipt.md)

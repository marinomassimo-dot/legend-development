# Locator audit, the five map-record rewrites of 2026-10-24 (blind, 2026-10-24)

Blind audit under `legend-locator-audit`, read-only toward every manifest, registry, receipt and
ledger. The author's note, the task record and the author's reasoning were not opened. Each
quote/proposition pair was judged against the artefact the quote names, held natively under
`files/`. Nothing was repaired.

## Scope

The five records of `analysis/mechanism_intervention_map.md` rewritten by commit `13bf5c57`:
N-06, N-08, N-10, N-12, N-15. The unit of judgement is the record, not the triple, because these
records carry their quotations inline rather than through a manifest; every quotation inside each
rewritten record was checked.

| Record | Artefact the quotes name | Quotations checked |
|---|---|---|
| N-06 | `DL-BIO-008` as it now stands (its own three sources behind it) | 2 |
| N-08 | Abdelmalak 2013, `files/fulltext/PMID23611579_Abdelmalak2013_PMC_r2.xml` · Lee 2022, `files/fulltext/PMID36432491_Lee2022_PMC_r2.xml` | 7 |
| N-10 | Cheerie 2025 Data S1, `files/supplement/PMID40139194_r2/mmc1_pymupdf.txt` (sha256 `60abe3f4…affd`, matches the record) and the main text `PMID40139194_Cheerie2025_PMC_r2.xml` | 6 |
| N-12 | Fog 2018, `files/fulltext/PMID30497978_Fog2018_PMC_r2.xml` | 1 |
| N-15 | Shaukat 2018, `files/fulltext/PMID30361190_Shaukat2018_JLE.txt` (sha256 `ae3103d9…ade78`, matches the record) | 2 |

## Text reads

Every artefact named above is held and opened. The two digests the records print were recomputed
and both match. The Shaukat text layer is a two-column PDF extraction in which the columns
interleave line by line, so each quotation was confirmed by de-interleaving the left column and
re-joining the end-of-line hyphenation (`psy-/chomotor`, `achieve-/ment`, `impair-/ment`); the
Cheerie Data S1 quotation of the 5-bp rule carries curly quotation marks and a hyphen split
(`exon-/intron`). Neither is a quote defect.

## Counts

| Record | Verdict | Quotations verbatim |
|---|---|---|
| N-06 | SUPPORTED | 2 of 2 against `DL-BIO-008`; 1 of 2 against the underlying paper (note below) |
| N-08 | OVERSHOOT (population) | 7 of 7 |
| N-10 | UNDERSHOOT | 6 of 6 |
| N-12 | OVERSHOOT (population, by ellipsis) | 1 of 1, with the elided words carrying the restriction |
| N-15 | SUPPORTED | 2 of 2 |

Adverse rate: **3 of 5 records (60 percent)**. Mode: exhaustive over the declared scope (the five
records rewritten by `13bf5c57`, every quotation in each); adverse = OVERSHOOT or UNDERSHOOT;
no record was UNVERIFIABLE, because every named artefact is held. Counted by quotation instead:
0 of 18 quotations is non-verbatim against the artefact its record names, and the three adverse
findings are all proposition-level — the rewrite removed the non-verbatim defect class and left a
scope class behind.

## Adverse records

| Record | Verdict | Reason |
|---|---|---|
| N-08 | OVERSHOOT (population) | The record calls Abdelmalak 2013 "the long open-label **paediatric** series" and its finding "the **paediatric** nerve signal", and builds its age split on that label. The series is not paediatric: "Patients (**1 adult**) ranged in age from 3.5 to 40.2 years at the start of DCA administration and are currently aged 16.9 to 49.9 years", and the paper's own conclusion is "generally very well tolerated in patients with mitochondrial diseases, **at least from young childhood through early adulthood**". The label also cuts against the record's own argument: of the three patients whose drug was paused or halved, the effect "persisted longest (up to 39 months before restarting DCA) in patient 8, who, to our knowledge, is **the oldest subject** to be chronically treated with the drug" — so the asymptomatic nerve signal is present in this series' adult, and the clean contrast with "an older-adolescent/adult MELAS trial" is the record's, not the source's. All seven quotations in the record are verbatim, including the 3-patient sentence, the asymptomatic-worsening sentence, the blood-chemistry sentence, the MELAS-RCT sentence, "DCA metabolism in humans is inversely proportional to age", the design-limit sentence, and the Lee 2022 "low doses of DCA or pyruvate alone do not significantly reduce neuronal cell death due to seizure" (which the record correctly marks as cited, not measured — reference [48]). Cohort n = 8 (4 males), 3 PDC / 1 CI / 3 CIV / 1 CI+CIV, 9.7 to 16.5 years of exposure, all confirmed. |
| N-10 | UNDERSHOOT | The record's headline and its scope note rest on the claim that the guideline's "**strongest word** on the functional route is *'most likely not eligible'*, **not 'cannot'**". The guideline states the stronger form **two sentences later in the same paragraph** of Data S1: "**Variants that fully abolish canonical splicing are not amenable to a splice correction ASO and are classified as 'not eligible' for this approach.**" The quoted "most likely not eligible" sentence is the lead-in to that flat statement, not the paragraph's ceiling, and the eligibility table reproduces it as a hard criterion ("Not eligible — Canonical splice site and branchpoints are destroyed OR … OR **Variant within 5 bp of the canonical splice site**"). So the source says more than the record allows on exactly the point the record was rewritten to soften, and the softening is produced by stopping the quotation one sentence early. Everything else in the record holds and is verbatim: the 5-bp positional rule, the figure note, the "destroyed" definition, the "weakened" class (the source's own word, in the next sentence), the faint-band warning, and "no gold-standard evidence for many considerations" (main text, not Data S1 — the record's locator claims Data S1 only for "the quoted rules", so this is not an anchor defect). |
| N-12 | OVERSHOOT (population, by ellipsis) | The record writes: "In Gaucher patient fibroblasts **and stem-cell-derived neuron-like cells** the co-inducer *'dose-dependently increased the amount of GCase … across all tested genotypes'*". The source sentence is "Arimoclomol dose-dependently increased the amount of GCase **in primary GD fibroblasts** across all tested genotypes, including neuronopathic and non-neuronopathic associated mutations (Fig. 1d–e)." The ellipsis is exactly the population restriction, and the record's prose then widens the restricted sentence to a second population. The widening is not false — the paper separately reports that "equivalent increases where seen in the neuronal-like MASC cell system during shorter timelines (i.e. up to 9 days)" — so this is a quotation-scope defect, the mildest of the three, and it is the same shape as the defect class the rewrite was meant to remove. Every limit the record attaches is supported: an ER-synthesised secretory client, no cytosolic client tested, "our attempts at knock-down of HSPA5/BiP did not result in sufficient downregulation to unequivocally resolve the potential ro[le]", substrate storage "proved to be futile as we … did not find any increased levels of GlcCer … and were technically unable to determine any amount of GlcSph", and the proprietary/funder relation ("Arimoclomol-citrate is a proprietary compound owned by Orphazyme A/S"; "The research was funded by Orphazyme A/S"). |

## The DL-BIO-008 attribution

The record's attribution is **correct** and the second actor's is **wrong**. The two measurements
sit in two different papers, and neither paper carries the other's.

- **The complete human metabolic screen is Abdel-Salam 2014 (`24456803`)**, patient II:4, in the
  Results: *"Normal results were found in metabolic screening including liver and renal function
  tests, complete blood count, blood gas analyses, ammonia, serum lactate, plasma urea,
  electrolytes, urine and serum amino and organic acids, and very long chain fatty acids."*
- **The cerebral MRS lactate is Davids 2019 (`30362252`)**: *"MR spectroscopy for non-essential
  amino acids was decreased globally and **lactate levels were extremely low**."*
- `30362252` holds **no metabolic screen of any kind**. The strings `screen`, `workup` and
  `work-up` do not occur in it; its four occurrences of `metabolic` are the mouse metabolic
  syndrome in the Discussion and three reference titles. Naming it as the complete human
  metabolic screen is unsupported by the artefact.

**The count the record now prints is right.** `DL-BIO-008` names **three** sources —
Abu-Remaileh & Aqeilan 2014 (`25012504`, mouse, serum lactate significantly raised),
Davids 2019 (`30362252`, human, MRS lactate extremely low) and Abdel-Salam 2014 (`24456803`,
human, metabolic screen normal). **Two are human**; **exactly one is a complete human metabolic
screen**. There is no fourth source and no second screen in the record, so the removed count of
"four independent human sources" had nothing behind it in this record, and the surviving
conclusion — the biomarker does not report reliably, and the human direction is unmeasured — is
carried by one normal screen plus one opposite-direction MRS case, as the record now says.

## Notes on the two records judged SUPPORTED

- **N-06, and one flag that is not a verdict.** Both quotations are faithful to `DL-BIO-008`,
  which is the artefact the record names ("counted from the record rather than asserted"), and
  *"extremely low"* is additionally verbatim in Davids 2019. But *"entirely normal"* is **not**
  verbatim in Abdel-Salam 2014: it renders `DL-BIO-008`'s own wording ("screening metabolico
  **interamente normale**"), and the paper says "**Normal results were found** in metabolic
  screening **including** […]", where "including" leaves the panel open rather than closed. A
  downstream reader will take the quotation marks for the paper's words. Not counted adverse —
  the record's named artefact is the ledger entry and against that the quote holds — but the
  phrase should lose its quotation marks or acquire the paper's sentence. Everything else checks:
  patient II:4 is the null/null patient, the five analytes the record lists are all inside the
  source sentence, and the HSPG2 confound follows the quoted MRS sentence in the same Results
  paragraph of Davids 2019.
- **N-15.** Both restored qualifications are verbatim in the Shaukat text layer, in the left
  column of the Discussion: "We believe that, in these children, the underlying cause itself
  (mutations in WWOX) caused both the severe cognitive impairment and the epileptic
  encephalopathy. **In support of this hypothesis** is the fact that the cognitive and
  psychomotor impairment preceded the onset of epileptic encephalopathy and did not improve with
  achievement of better control of epileptic activity **in some of these cases**", and "The
  developmental outcome was unfavourable with profound impairment despite improvement of
  epileptic activity **(e.g. in the first child)**". The surrounding propositions hold on the
  source: in the first child "Vigabatrin was added and the spasms resolved", and "At two years of
  age, he remained profoundly delayed with infrequent mixed-type seizures and spastic
  quadriplegia"; in the second child "Seizures were noticed at five weeks of age" while "At four
  months, the child failed to attain any developmental milestones" — so the order-of-onset gap
  the record declares is real in the text. N = 2, observational, uncontrolled: confirmed. The
  "another cohort … died at 8 years" limb carries no quotation and names no artefact in this
  record, so it was outside this audit; it is the only proposition in the five records that could
  not be put against a source.
- **Incidental, offered because it bears on the N-06 count and on nothing else.** Shaukat 2018 —
  a source of N-15, not of `DL-BIO-008` — reports for its first child that "The following
  investigations were normal: lactate, ammonia, acylcarnitine, uric acid, homocysteine, plasma
  amino acids, urine organic acids, and transferrin isoforms." That is a second normal human
  metabolic panel in the corpus. It changes nothing in N-06, whose count is explicitly scoped to
  `DL-BIO-008`, and it is **not** a fourth human source for the removed claim; it is recorded
  here only so that a later reader does not rediscover it and mistake it for one.

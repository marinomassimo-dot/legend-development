> Blind locator audit of entries 27-99 of the PMID 42909904 deepdive manifest. The auditor received only the `(proposition, quote, anchor)` triples (`locator_audit.py --pmid 42909904 --triples 0`) and the source PDF `files/fulltext/PMID42909904_LucasClarke2026_BrainComms_fcag385.pdf`; no dossier, candidate, ledger or earlier audit was opened. Read-only: no manifest or ledger edit.

# Blind locator audit, PMID 42909904, entries 27-99

Source: PDF text layer is readable (`pdftotext`, reading-order mode; the `-layout` mode interleaves the two columns and defeats quote matching). Every body quote was matched after whitespace, hyphenation and case normalisation: all body quotes in 27-99 occur in the PDF except entry 37, whose long multi-sentence quote was read by eye and is verbatim. Figure-panel and supplementary-table quotes cannot be matched in the PDF text and are declared, not verified.

## Verdicts (entries 27-99, 73 triples)

SUPPORTED 43 (after repair re-audit) - OVERSHOOT 5 - UNDERSHOOT 0 - NOT_IN_SOURCE 0 - UNVERIFIABLE_SURFACE 25 (11 figure panels and 14 supplementary tables, declared as attestations).

## First-pass findings and repair by sourcing

Seven triples carried a quote that covers only part of the proposition while the PDF supplies the rest in an adjacent sentence. Re-audit with the deciding sentence: SUPPORTED.

| Entry | What the quote lacked | Deciding source sentence (PDF) |
|---|---|---|
| 27 | two of three enrichment sets | "overrepresentation analysis revealed a significant association of these genes with fatty acid and pyruvate metabolism"; "enriched for oxidoreductase activity and metabolism of ascorbate, aldarate, and porphyrins" |
| 39 | "only when Abeta42 present" | "L-Lactate increased in the response to Wwox knockdown, only when Aβ42 was also present" |
| 66 | the not-measured scope | the sima reporter is described only for day 14, Abeta42 flies, knockdown; no hypoxia or overexpression condition appears in the text |
| 70 | the prior Atf4-dependent, sima-independent report | "Atf4-dependent, sima-independent upregulation of Ldh has been previously reported in Aβ42-expressing Drosophila" |
| 73 | Drosophila cDNA better, variants similar | "dWwox cDNA overexpression provided a better rescue of locomotor ability than hWWOX and hWWOX Ser14 phosphomutant"; phospho variants "performed similarly to wildtype hWWOX" (supplementary panel, so that part is a declared figure-level statement) |
| 96 | "regulator of neuronal metabolic state" | Abstract: "identify WWOX as a regulator of neuronal metabolic state" |
| 97 | SNP and post-mortem protein findings | Introduction: intergenic SNP between WWOX and MAF, decreased WWOX in post-mortem hippocampus (cited, not results) |

## Still OVERSHOOT (the proposition asserts more than any quote can carry)

| Entry | Problem | What the source actually supports |
|---|---|---|
| 31 | The quote carries only the 1.19 log2 Ldh figure; the claimed text-versus-table disagreement lives in a supplementary table the PDF text does not carry. | Text gives 1.19 (Aβ42 versus control) and a separate 1.29 for the interaction; a table disagreement is unverifiable from the PDF. |
| 49 | The quote is the MetaboLights deposition sentence and cannot support an absence list. | Text-layer search finds no NAD/NADH, glucose uptake, extracellular acidification, flux or respirometry measurement in the main text; it cannot speak for the supplement. Word it as "not reported in the main text". |
| 89 | The quote carries "did not alter lactate levels"; the "rests on absence from the significant-metabolite lists" and "no lactate panel" parts are the reader's inference. | The abstract statement is verbatim; the basis for it is not stated by the authors. |
| 94 | The quote is the opening of the Conclusion and cannot show an absence. | No heading "Limitations" exists in the PDF text; the further list (single RNAi line, sex, replicates) is an absence claim not verified by any quote. |
| 95 | The quote is the authors' conclusion; "rests on glial-versus-neuronal driver comparisons; no second driver" is the reader's inference. | The glial-overexpression null result is sourced (Results, same section); the absence of a second-driver or non-neuronal rescue is unverified. |

Disposition: five propositions need rewording to what the source carries, or the divergence argued explicitly in the commit candidate, before any BATCH_COMMIT uses them. None is NOT_IN_SOURCE, and none contradicts the source.

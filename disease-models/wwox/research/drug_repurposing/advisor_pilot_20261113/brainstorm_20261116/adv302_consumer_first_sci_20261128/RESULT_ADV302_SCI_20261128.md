# ADV-302 result: consumer-first depth reading of the catalogued-only tail (SCI, window 64fc909a, 2026-11-28)

Hypothesis level; reference genotype class only; not medical advice. Prediction and rules: `PREREG_STEP1.md`, `PREREG_STEP2.md`, `PREREG_STEP2_ADDENDUM.md` (frozen before any source). Readers: legend-delegate, claude-sonnet-5-5, effort high stated in each dispatch; first reader and blind reader separate per record; held files only.

## Verdict

**Prediction met on both counts, with a limit of access.** (1) 8 of the 185 catalogued-only records without a receipt carry a consumer (prediction at least 6). (2) Strict in 1 of the 2 records that could be read (prediction at least 1 of 3). The rejecting observation (three read and 0 strict) **could not be met**: only 2 of the 8 consumer-bearing records have a lawful full text, so the draw of three was impossible. Consumer-first order is limited by access, not by the number of consumers: the other 6 go on the operator's supply list (`CLOSED_CONSUMER_RECORDS.tsv`).

## The two records read

| record | consumer units | result |
|---|---|---|
| 26041563 (Bendinelli 2015, retracted 2020-08-15, notice PMID 32799870) | 4 (DL-MECH-025, FM-006, disease model, working model); they use its retraction status only | **strict 0**; loose yes (ADD): date, scope of the reason, authors disagree |
| 25703206 (Schuchardt 2015, WWOX WW1/WW2 allostery) | 1 (DL-MECH-049) | **strict 5 sentences**; loose many |

### 26041563: what the sentences claim from a retracted source
First reader: all clauses about this article VERIFIED (retracted; cited by the review as ref 58; same four authors; the review has no word on retraction), except two judgements marked unsupported ("i passaggi più originali"; reading "HGF/Met-TAZ-WWOX line" as describing this article). Blind reader: those two OK; no MUST CHANGE. So no strict. ADD (both readers): the note names only Figs 2 and 3 and only the vinculin loading-control bands (band reuse in Fig 2, band rotation "seems" in Fig 3), calls the results "unreliable", the authors do not agree, and the date is 2020 (the repository text sets "retracted in 2022" beside the list, which is true of 28151481 only). Not strict, not a decision change: the exclusion of this line from WWOX/HIF1A support stands, and the article's own Fig 6B (WWOX raising HIF-1 reporter) points the other way from the review's independent sources.

### 25703206: DL-MECH-049, sentences that are strict (first reader false or unsupported, and blind reader MUST CHANGE; each checked by SCI on the original XML and Tables 1 and 2)
1. "esclusivamente i residui 1-91": the constructs are WW1 16-50, WW2 57-91, tandem 16-91 (Methods). Minor.
2. "WW1 da solo è parzialmente destrutturato e si ripiega legando il ligando", filed under DATO (ITC/CD): the paper takes this from its ref 13 (McDonald 2012); it contains no folding or stability measurement of WW1 (CD is on free peptides only).
3. "Esistenza-prova ... Stabilizzare un fold floscio di WWOX ... è il design nativo ... Cade l'obiezione": not shown here; the MD starts from a folded model and both WW cores stay at about 1 Å; the stabilisation by WW2 is prior work.
4. "il ligando paga il costo entropico e solleva il coperchio": reversed; the authors say dissociation of WW2 is entropically favourable and the dissociation was not simulated or measured.
5. The head of the lead, "la stabilità si compra con l'occlusione; l'occlusione è anti-funzione": the paper measures higher peptide affinity with WW2 present (ΔΔG -0.36 to -0.98 kcal/mol over eight PPPY peptides; Tables 1 and 2) and measures no protein stability; the occlusion is a proposed model (Fig 10).

Judged by SCI on the original: sentences 3 to 5 carry the lead's "vincolo di progetto per qualunque stabilizzatore di Q230P": they are decision-bearing for the stabiliser design constraint (my judgement; ADV and IT decide). Listed apart, not counted (only one reader, or the unit already corrects it): the quotation "nettamente a favore del chiuso" (the paper says "predominantly ... in favor", inside a proposed model; blind MUST CHANGE only); "2-3×" (the next bullet of the same unit already prints 1.8 to 5.1; my recomputation of Tables 1 and 2 gives 2.39, 1.78, 3.52, 3.57, 5.13, 2.40, 2.61, 3.17, as the review); "guadagno entropico" (TΔS is less negative in 8 of 8 rows but still negative in 6; ΔΔH is worse in 8 of 8, +1.27 to +10.5; blind ADD).

## Not done
No blot forensics on 26041563. The review 25662954 and the papers cited as refs 13 and 31 of 25703206 were not opened; the four-force-field claim cannot be checked (the paper has no supplement). The first reader of 26041563 reported one of its own folder listings interrupted by the harness; the reading was not affected.

## Where this goes
`SENTENCES_FOR_IT_ADV302_SCI_20261128.md` (proposed wordings), `SENTENCES_FOR_IT_CLOSED_ADV302.md`, `DEFECT_FOR_IT_PLACEHOLDERS.md`, `CLOSED_CONSUMER_RECORDS.tsv` (for ADV's operator list). Receipts: two `queried_not_full_read` (question-driven, as ADV-295/300), 26041563 and 25703206.

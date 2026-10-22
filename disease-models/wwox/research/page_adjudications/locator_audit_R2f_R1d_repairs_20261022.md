# Locator audit, R1 lots and R2c-R2e repairs with zero auditors (blind, 2026-10-22)

Blind adversarial audit under `legend-locator-audit`. Read-only toward every manifest, registry, receipt and ledger. The auditor judged only (proposition, quote, anchor) triples against the source artefacts. Triples were drawn with `framework/scripts/locator_audit.py --pmid <PMID> --triples 0` and filtered to the entries whose `contradicts_locator.audit.auditors` is 0 (the manifests of 22 papers; 52 entries: 9 CORRECTED, 24 CLAUSE_ADDED_SELF_SWEEP, 19 ADVISORY_STRENGTH_SCAN). All 52 were audited, not a sample. Every artefact was opened: body and supplement text were searched for the quote and read around it; every figure entry (11 of them) rendered as an image (jpg, png, a page raster, and a webp converted with ImageMagick) and its values, counts and stars were read from the axes. No image read failed, so no UNVERIFIABLE verdict arises. Artefact digests were not re-hashed. Authors' notes, task records, self-evaluations and earlier audits' reasoning were not opened.

Verdicts: SUPPORTED, OVERSHOOT, UNDERSHOOT, UNVERIFIABLE. Convention: a quote that is narrower than the proposition counts as SUPPORTED when the rest of the proposition is stated in the source; it is listed as a flag when the rest sits outside the anchored paragraph.

## Counts

| Paper | Triples | SUPPORTED | OVERSHOOT | UNDERSHOOT | UNVERIFIABLE | Entries |
|---|---|---|---|---|---|---|
| 24953239 | 1 | 1 | 0 | 0 | 0 | 3 |
| 30175250 | 1 | 1 | 0 | 0 | 0 | 20 |
| 32678276 | 3 | 3 | 0 | 0 | 0 | 1, 11, 13 |
| 32719346 | 5 | 5 | 0 | 0 | 0 | 5, 7, 9, 10, 12 |
| 32751129 | 2 | 1 | 1 | 0 | 0 | 6, 7 |
| 32878331 | 1 | 1 | 0 | 0 | 0 | 7 |
| 33704440 | 3 | 3 | 0 | 0 | 0 | 3, 9, 11 |
| 34483921 | 2 | 2 | 0 | 0 | 0 | 3, 12 |
| 35079122 | 3 | 3 | 0 | 0 | 0 | 1, 2, 4 |
| 35184274 | 1 | 1 | 0 | 0 | 0 | 5 |
| 35243344 | 3 | 3 | 0 | 0 | 0 | 5, 8, 10 |
| 37082241 | 5 | 5 | 0 | 0 | 0 | 3, 4, 12, 14, 22 |
| 37275776 | 1 | 1 | 0 | 0 | 0 | 4 |
| 39013852 | 1 | 1 | 0 | 0 | 0 | 12 |
| 40068874 | 2 | 2 | 0 | 0 | 0 | 3, 10 |
| 40166234 | 1 | 1 | 0 | 0 | 0 | 5 |
| 40421674 | 1 | 1 | 0 | 0 | 0 | 11 |
| 40834072 | 1 | 0 | 1 | 0 | 0 | 9 |
| 42161426 | 1 | 1 | 0 | 0 | 0 | 5 |
| 42536722 | 8 | 8 | 0 | 0 | 0 | 4, 5, 6, 9, 10, 11, 13, 16 |
| 42587736 | 3 | 3 | 0 | 0 | 0 | 11, 16, 27 |
| 42650175 | 3 | 3 | 0 | 0 | 0 | 4, 7, 10 |
| **All** | **52** | **50** | **2** | **0** | **0** | |

Adverse rate: 2 of 52 triples (3.8 percent), mode: exhaustive over every entry with zero auditors in the 22 manifests (9 CORRECTED, 43 sweep-added or advisory-scan entries), text and figure entries both, artefact opened for every triple; adverse = OVERSHOOT or UNDERSHOOT or UNVERIFIABLE. Of the 11 figure entries 0 are adverse; of the 41 text and supplement entries 2. Packet note: `--triples 0` for 37082241 omitted entry 22; it was read directly from the manifest and the artefact.

## Adverse triples (OVERSHOOT, both minor)

- 32751129 entry 6: the quote's "They" refers to the T-type channels (Cacna1g and Cacna1h, Cav3.1 and Cav3.2), the two most expressed VGCC genes; the proposition says "the voltage-gated calcium channel transcripts were the predominant ones", which reads as VGCC transcripts in general and drops the T-type referent.
- 40834072 entry 9: the quote stops at "did not directly establish a causal role of T-type calcium channels in RT"; the source goes on to call both inhibitory and excitatory DREADD results "complementary support for an RT role" and attaches "demonstrating a causal role of RT neurons" to the excitatory arm in wild-type mice. The proposition names only the inhibitory result as "the supporting causal evidence", and the quote does not reach that clause.

## SUPPORTED with a flag (not counted as adverse)

- 24953239 entry 3: the quote carries only the contrast sentence; the gain-of-function Cav3.2 variant restricted to reticular neurons is in an earlier Discussion paragraph, not the anchored one; every other clause (preparation, current density versus absolute current, in situ hybridisation, P9 dissection error) is in the quoted paragraph.
- 40068874 entry 3: the juvenile-mouse rationale (neurogenesis at a faster rate, mixed maturation) is in the Results, not Discussion paragraph 4; the Cav3.2 P0 to P60 clause is in the quote.
- 37082241 entry 22: the caption says the table gives "mass transitions and collision energies", but the table (txt and docx) has only analyte, molecular weight and precursor to product ions; no collision energy appears. The proposition repeats the caption.
- 35243344 entry 5: the control per-mouse points in Figure 6G read about 640 to 745 pA, the lowest below the stated "about 700"; every other value and star reads as written (6B 2.2 and 1.0 with one star, 6G 699 and 155 with three stars, 4E four mice, ethosuximide about 23 to 1, baclofen about 33 to 63).
- 33704440 entry 3: the quote carries only the gain-of-function conclusion; rheobase, longer bursts and "strongest for I860N, weakest for I860M" are in the preceding Results paragraph; I860M's 200 ms train at maximal injection (156 ms) is comparable to wild type (133 ms), so "all four lengthened bursts beyond the stimulus" holds for the unclamped 10 s runs and the text's general statement rather than that one panel.
- 35079122 entry 2: the quote is the redox sentence only; the Cav3.3 and "warrants further investigation" clauses sit in the same Discussion paragraph.
- 42650175 entry 10: the quote is the Figure 4 title; the numbers in the proposition (ER overlap, total YFP about 25 to 47.5 against 49.7) are in the Results text, and the augmentation figures (Figure 6) read GABA uptake only.
- 32719346 entries 7, 9, 10, 12 are supplement legend lines that match their propositions; the extractor text contains line-wrapped, page-numbered legends, quotes match after whitespace normalisation.

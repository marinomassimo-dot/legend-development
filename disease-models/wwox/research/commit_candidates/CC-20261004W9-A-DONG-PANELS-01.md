# COMMIT CANDIDATE — CC-20261004W9-A-DONG-PANELS-01 — PMID 35460704 (Dong 2022): the panels give no WWOX statistic and no neurological endpoint; `CLAIM 045`'s human counterpart holds, with one ClinVar-column clarification

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist`, Scientist A of intake wave 9, 2026-10-04.
**Change class:** **MINOR.** Two clarifying replacements (one in `CLAIM 045`'s human-counterpart paragraph,
one in `PAPER 156`); no `consolidated baseline` claim is narrowed or reversed. Provisional anchors.
`context_policy: QUESTION_DRIVEN`. **Not medical advice.** A lipid cohort; no neurological endpoint exists in it.

---

## 1 · What the owed sections show

- **Figure 1 (viewed):** the WWOX bar reads 4 and is entirely missense colour (no frameshift, splice or
  stop-gained segment), in agreement with the text and with the three distinct missense alleles of the
  supplement. The figure's own header ("144 occurrences in 101 patients") does not match the text's 110
  participants (the text's tallies imply about 151-161 occurrences); the mismatch is in cohort totals,
  not in the WWOX count.
- **Figure 3 (viewed):** the quantile-quantile gene tables list ABCA1 and LDLR (MAF <= 0.0001) and ABCA1,
  LDLR, HK3, CFTR (MAF <= 0.001) as significant; WWOX is in neither table and no WWOX p value is printed anywhere
  (figure or text).
- **Neurological endpoints:** none exist. Participants were selected for low HDL-C, so the lipid phenotype is
  constant by design; no neurological or developmental assessment, and no per-carrier lipid value for WWOX, appear
  in the main text, Figures 1-3 or Tables S3-S4. The paper's only CNS sentence is a conditional
  speculation. `CLAIM 045`'s `NOBODY_LOOKED` premise is strengthened, not resolved.
- **Supplement (re-read):** the p.Arg120Trp row (gnomAD 7.50e-3; recomputed 7.5 times the study's rarity
  threshold of 1e-3 and 0.75 of the 1e-2 filter) carries ClinVar significance "other|Benign|Benign" and, in the
  disease column, "not specified|Epileptic encephalopathy, early infantile, 1|Spinocerebellar ataxia,
  autosomal recessive 12": a list of condition names beside a Benign classification.
- Arithmetic screen: group sizes 80 + 23 + 77 + 24 = 204; printed percentages 57.5, 34.8, 58.4, 45.8 recompute
  from 46/80, 8/23, 45/77, 11/24 exactly.

## 2 · Records gated and verdicts

| record | wording | verdict |
|---|---|---|
| `CLAIM 045` human counterpart | "tre alleli missenso eterozigoti distinti ... Benign in ClinVar ... WWOX non raggiunge la significatività ... nessun valore lipidico è riportato per un portatore WWOX" | **Holds, confirmed on panels and supplement.** The "negative" is only a failed burden test, and the cohort supplies no neurological endpoint, as the claim already says. Clarification op below. |
| `PAPER 156` | "pannelli non ispezionati come immagini" | **Narrowed** (Figures 1 and 3 viewed; Figure 2, LDLR, by legend). Still `partial_fulltext_read`. |
| `CLAIM 045` murine arm (PMID 33914858) | | Unaffected. |

## 3 · Ops (provisional; each `old` measured unique in its record)

### 3.1 · `disease-models/wwox/registries/claim_registry_current.md`, record `CLAIM 045`

| field | value |
|---|---|
| op | `replace` |
| old | `è **Benign in ClinVar** e **non raro**` |
| new | `è **Benign in ClinVar** (la colonna «ClinVar Disease» della stessa riga elenca nomi di condizioni WWOX-correlate accanto alla classificazione Benign: un elenco di condizioni, non un'asserzione di patogenicità; Supplemental Tables S3-S4, lettura wave 9) e **non raro**` |

### 3.2 · `disease-models/wwox/registries/paper_registry_current.md`, record `PAPER 156`

| field | value |
|---|---|
| op | `replace` |
| old | `Parziale: pannelli non ispezionati come immagini, lista dei riferimenti non letta.` |
| new | `Parziale: Figure 1 e 3 ispezionate come immagini (ricevuta FTR-20261004-35460704-02, wave 9; Figura 2, LDLR, per legenda), lista dei riferimenti non letta.` |

| field | value |
|---|---|
| op | `replace` |
| old | `«Probably damaging» è una predizione di dieci strumenti, non un saggio.` |
| new | `«Probably damaging» è una predizione di dieci strumenti, non un saggio. [Wave 9, pannelli: la barra WWOX della Figura 1 vale 4 ed è interamente missenso; nessuna statistica WWOX è stampata in Figura 3 né nel testo; l'intestazione della Figura 1 («144 occurrences in 101 patients») non concorda con i 110 partecipanti del testo, discrepanza nei totali di coorte e non nel conteggio WWOX.]` |

## 4 · Verification before propagation

`deepdive_manifest.py --pmid 35460704 --verify-artifacts --require-current-schema` PASS at this commit.
Receipt `FTR-20261004-35460704-02`.

### LOCATOR TRIPLES FOR BLIND AUDIT

- (WWOX is one of the genes with the most occurrences, n = 4 | WWOX (n = 4), and IRS1 (n = 4) | PMID 35460704, Results, Fig. 1 paragraph)
- (Four genes carry the significant burden, not WWOX | Binomial analysis for rare (MAF ≤ 0.001) heterozygous D-Mis or LoF variants identified the ABCA1, LDLR, HK3, | PMID 35460704, Results, binomial analysis)
- (No normal-HDL-C comparator | we were not able to compare the prevalence of mutations among a cohort considered to have normal levels | PMID 35460704, Discussion, limitations)
- (Cohort total in the text | There were 110 participants who had at least one potentially damaging HDL candidate gene variant, 31 of whom had 2 and 10 had 3 each. | PMID 35460704, Results, damaging variants in HDL candidate genes)
- (No copy-number event in the candidate genes | No CNVs were found among our list of 104 HDL candidate genes | PMID 35460704, Results, CNV analysis)
- (The only CNS sentence is conditional | A critical structural or functional role for the WWOX gene in the CNS would account for the observation that mutations at that locus are associated with neurodevelopmental and neurodegenerative disorders | PMID 35460704, Discussion)

## BATCH DISPOSITION — `BATCH_20261004_003` (2026-10-04, ACTOR_ID `scientist`, Scientist M), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** `PROPAGATED` (MINOR, WM_v7.15 → WM_v7.16).

**Surfaces written:** claim_registry_current.md · paper_registry_current.md

All three ops applied; the second `PAPER 156` op was **amended at source after the blind audit**. The candidate wrote that the Figure 1 header *«144 occurrences in 101 patients»* disagrees with *«i 110 partecipanti del testo»*. 🔴 **110 is the number of carriers, not the cohort total: the cohort is 204**, printed in the abstract, the methods and the results. The landed text names both figures and says which is which, and records that the paper's *«No CNVs were found»* is scoped to its 104 candidate genes and to a method its own authors call often insensitive. **Blind locator audit: 6 triples, 5 SUPPORTED and 1 NOT_SUPPORTED_AS_LABELLED — the cohort-total mislabel, repaired here — 0 UNVERIFIABLE.** `CLAIM 045`'s live `Status` was read before the edit (**`in observation`**): the landed note adds what the ClinVar column actually lists and changes no conclusion.

**Not medical advice.**

# IT50: from accessible knowledge to useful therapeutic hypotheses

Non-canonical working note. Not medical advice. Reference genotype class only. IPOTESI throughout. No rank, sign, tier or qualification changed; no predictive improvement claimed from better access to knowledge.

## What the generator formulates better (and what that is not)
| Item | Before | After | Evidence level |
|---|---|---|---|
| INV-02: an eIF2B activator as a research probe, with its blocking premise | 0 rows by target search; no row in the generator | 3 hypothesis rows (ISR1-ISR3) in the generator layout, every cell sourced, no prediction or direction; reader row ISR1 in five languages | new for LEGEND as a representation; independent reader: 14 supported, 12 partly, 1 not supported (corrected); no row beyond a restatement |
| Investigations reached by the generator | a fixed list of three | read from the manifest (earlier order kept) | code change, tested |
| Cell context of the ISR genes | unknown for all (no held table) | 12 ISR genes joined (HE50 extraction, registered in `cell_context.TABLES` here): none neuron-enriched in either table; ISR and GSK3 rows now carry states instead of "unknown" (the five GSK3 rows changed only in that cell) | RNA class means, not protein or the ISR sign |
| Kir2-family arm of INV-18 | the join existed but no consumer carried it | clause on INV-18 (no Kir2 subunit gene neuron-enriched; glial arm required for the statement "neuronal") in five languages | RNA only |
| Design-only knowledge | not read | HE50's `design_only` role returns the package steps verbatim (6 ISR steps, 7 myelin steps read-only); the scientific meaning of the fields is in `design_fields_it50.md` | see below |

## What the design link makes usable (P4, shown by running the generator)
`conditional_design_steps_it50.tsv` (written by `conditional_proposals.py`) carries ISR steps 0-4 with precondition, controls and branches verbatim and states that no observation exists. Beside my ISR1-ISR3 it adds, with sources: the GSK3 chain steps (2, 3, 3b) and their controls (the second GSK3 chemotype is NOT qualified; an alanine at the GSK3 serine does not separate GSK3 from DYRK2 at the priming serine; numbering human 540, mouse 536, rat 535), which the hypothesis rows only reference; and the branch tables as they are, not summarised. It does **not** add a hypothesis link ("not stated by the package"), a prediction or a result; no experiment or question changed because of it today. The honest summary: the design is now visible to the generator beside the hypotheses, and whether it changes a later choice is not shown.

## SCI50 (phenotype-first myelination package) — dispositions of its `consumer_delta.md`
| Row | Disposition | Where |
|---|---|---|
| 1 INV-06 conditioned-medium arm: candidate (neuron-secreted CTGF, the authors' in vitro claim) and the missing controls | applied as a dated clause (five languages); IPOTESI, no Wwox datum | `investigations*.tsv` INV-06 `next_test` |
| 2 X3 variant: an M1-selective antagonist and an EBP inhibitor without M1 affinity, crossed with neuron genotype, behind gate 0; reading rules | applied inside the same clause (the experiment file of the IT36/IT37 package is not edited) | same |
| 3 open questions | applied: IT50-Q01..Q08 from the package's own `open_questions.tsv` (OQ3 duplicates INV-12 step 0 and is skipped; OQ9 is not in the delta's list and is not added); IT50-Q09 (EBP activity of the comparator) added from the delta's text | `open_questions_map.tsv` |
| 4 identities and aliases | not applied: the identities must be looked up in primary papers before any alias; reagent names stay out of public text | — |
| 5 register `minimum_comparison.md` as a design_only package | Harness's, relayed | — |
| 6 the false sentence "no source tests a compound in a neuron-driven hypomyelination" | none found in the tree to correct; the corrected form is kept in the package README | — |
| 7 receipts | applied: 27 recorded (producer -69 first, then verifier -68) after a trial, no claim made on the delegate's behalf; ledger 1,930 | ledger |
SCI50's own answer is kept apart from the science session's mission: nothing here duplicates its work.

## Limits
Translations are the assistant's; the IT50 consultation (one Stage A, one Stage B) changed a secondary item, not the principal one; the case is retrospective and scored by its builder. The by-target activity route for eIF2B remains blocked by the ChEMBL API outage.

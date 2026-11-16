# Baseline table of existing frozen predictions (IT, 2026-11-16; non-canonical; not medical advice)

Written for: ADV, SCI, HE (the reference hit rate against which any improvement is claimed). Reference genotype class only. Filled `../prediction_ledger.tsv` (137 rows). Producer: one legend-delegate (sonnet-5-5, effort high), read back from its transcript later in the cost line; IT spot-checked 4 rows (P143, P66, P115, P134) against their scoring text; status is taken from the scoring text in each folder, never from judgement of the science.

## Summary line
137 predictions in the 34 by-name files (19 files hold predictions; 15 files, 17 rows, hold none and are listed in `part1_rows_incl_not_a_prediction.tsv` as not_a_prediction). Kind: 73 generative, 64 paper_content ("memory of the paper not excluded"). Scored (held, mixed or failed): 89 = 33 generative + 56 paper_content. Held / scored: generative 16/33 (48%; mixed 4, failed 13), paper_content 37/56 (66%; mixed 9, failed 10). Open 42 (generative 39, paper_content 3); unscorable 6. Predictor = scorer in 45 of the 89 scored rows (27 paper_content, 18 generative). Sample of the 118 text-found files: 3/20 with a real prediction (15%; looser reading 5/20); estimate about 18 such files among 118 (Wilson 95% interval 5-36%, roughly 6 to 43 files), an ESTIMATE, not a count; their predictions are not in the table.

## Limits that travel with the numbers
* Hit rate counts mixed as not held. The 48% and 66% have small denominators and no interval is claimed for them.
* The generative/paper_content split is a rule applied by the producer: values looked up in held public tables are paper_content, new computations on held data are generative; a caller who treats any table lookup as generative moves 29 rows.
* 51 rows have predictor = scorer in the file headers; most predictors are the Orchestrator or Scientists who also scored. Four rows have a status read from result text without a verdict word (gse156243 maturation P1, hif1a P5, wnt_sign P3, LINCS P9); the status of LINCS P7-P9 rests on a pointer to a file outside the folder.
* Out of this table: further predictions in partial_benefit_it6_p10 README (about line 202) and 8 predictions in generation_it46 `p8_chloride_prereg_it46.md`; the 118 text-found files except a 20-file sample.
* Four ph_k2p rows (P136-P139) carry freeze fields computed by IT from SIZE_CHECK_PREREGISTRATION.md (commit 6df4622c5), because the candidates list names only the outcome file.
* None of this is evidence of generative capacity: it is the starting hit rate by kind, scored mostly by the predictors themselves.

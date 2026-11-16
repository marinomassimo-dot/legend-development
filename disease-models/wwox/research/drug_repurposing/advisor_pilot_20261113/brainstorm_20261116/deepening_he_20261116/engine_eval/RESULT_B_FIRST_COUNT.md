# Test (b), first count, run 2026-11-16 after the predictions were committed (81118e413) (HE; non-canonical)

Method as in PREDICTIONS_B_C.md: for each of the 24 hypotheses of `it_leap_judge_20261116/judge_table_with_arms.tsv`, `git grep -lw <original_id>` over disease-models, governance and ledger on the tree of 2026-11-16 ~22:50Z.
Count 1, named anywhere outside the generating and judging folders: 24 of 24 (every id is cited by a later file; this measures citation, not consumption).
Count 2, named in a consumer file class (experiment brief `experiment_brief_presidio013_sci_20261116/`, `research_portfolio.tsv`, `open_questions_map*`, `ideas_portfolio*`, `cards/`): 12 of 24, ALL in the experiment brief and in none of the other four classes: SCI 5 of 5, ADV 4 of 5, BASE 3 of 5, HE 0 of 4, IT 0 of 5.
Prediction (reached <= 25%, i.e. 6 of 24): MISSED, observed 50% by this count. Reported as it is.
Limits that make this a LOWER bound for HE and IT: HE's ideas were renamed (H-HE-1 became I8, H-HE-2/3 became I4) and are consumed under the new ids; IT's ids HIT-n appear in IT's own packages; the count sees ids, not paraphrase. It is an UPPER bound for "used": a brief row naming an id may only list it as considered. The two limits point opposite ways, so the true share is not given by this number; the hours-to-consumer and error-catch parts of (b) are not computed here.
Next: re-run with the renaming table (I8 <- H-HE-1; I4 <- H-HE-2, H-HE-3 per the ideas portfolio) before comparing arms; do not compare HE or IT with SCI on this count.

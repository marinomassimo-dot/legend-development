# I2 rubric addendum 1 (IT; frozen by hash before the addendum pass; non-canonical; not medical advice)

Why an addendum and not a v2: the rubric v1 (sha256 2d81d629...11c7, commit 6e8ef5c9e) was frozen and the extraction delegate launched before ADV's request (HE's I8, I4 and ADV's I10) arrived. v1 is not edited. The fields below are collected in a SECOND pass over the same bundle, after the v1 extraction is delivered and its digest recorded, and are joined to v1 rows by report_id and child label. The delegate is told that v1 values are not to be changed in this pass.

Added columns, per child (children_addendum.tsv: report_id; child_label_as_printed; ...):
1. variant_as_printed (verbatim, including both alleles) and variant_domain: WW1, WW2, SDR, truncating, splice, deletion, other, not_stated. Classing is from what the text says about the location; if the text gives only a nucleotide change, `not_stated` (no outside lookup; no web).
2. protein_stated: absent_or_truncated | present | not_stated (only if the text states it).
3. sleep_wake_timing: asleep | awake | on_waking | on_falling_asleep | mixed | not_stated, with verbatim locator, from statements about when seizures occur.
4. Per exposure, in exposures_addendum.tsv: line_of_therapy (first_line | add_on | later_line | not_stated), taken only from the text's ordering words; diet_response and valproate_response are NOT new columns: they are the rows of mechanism_class ketogenic_diet and valproate_type in v1 (outcome as stated); the analysis joins them.
Rules as v1 (verbatim locators, no inference, no web, only the bundle).
Pre-declared use: (i) variant domain as a stratifier of outcome and semiology, counts only below n = 10 per cell, with the explicit limit that nearly all children are expected to be truncating or null, so the WW1-with-protein contrast may be empty; if empty, say so; (ii) sleep timing against semiology; (iii) line of therapy as a confounder listing for each class.

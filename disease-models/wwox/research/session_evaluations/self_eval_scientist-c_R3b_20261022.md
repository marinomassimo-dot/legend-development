# Self-evaluation — scientist-c, group R3 relay b, 2026-10-22

Verdict: 6 readings completed (one owed unread paper, five from new adjacent searches), manifests PASS, receipts staged and DOI-checked; the questions were answered more narrowly than the note's headings might suggest.

1. **Five of the six readings are partial.** Two had no lawful figure image at all (29940337, 28434841: captions only), one has only one figure opened (31331032), one has main figures as captions only (28504693), one has extended data and 17 supplements unopened (35501379). The receipts say so.
2. **The most useful finding is a juxtaposition, and it is mine.** The brain concentration of THZ1 (28434841) set beside the cell-culture inhibition range (29163040) is a cross-paper inference across different systems; it is labelled as such and needs a second reader before any card cites it. No blind audit was run (declared OWED).
3. **Four papers were parked, not circumvented** (PMC bot challenge and restricted stubs); one of them (37551745) is the abstract that names neurotoxicity as a tested hypothesis, so the neurotoxicity question of the CDK7/9 class stays open for lack of a lawful PDF, not for lack of a paper.
4. **A prior-session artefact was wrong:** the file saved as the "supplement" of 29163040 was the article PDF. The true supplement was found by asking Europe PMC `supplementaryFiles`; the packet and `owed_sections.py` could not have told me.

Micro-upgrade (one, proportional): `pmc_bucket_fetch.py` should record, in its own output, when the file it labels `supplement` has the same page count and title text as the article (a duplicate-of-article check) and should try the Europe PMC `supplementaryFiles` endpoint when the bucket holds no supplement. Candidate for Harness Engineering; not done here. The actor-scratchpad manifest builder from the previous relay (a Python spec, one call) was reused for all six and again is a candidate for `framework/scripts`.

ATTRIBUTION_CENSUS: 6 readings; 0 declared QUESTION_DRIVEN, 6 declared SOURCE_FIRST; 0 claims narrowed or reversed against a consolidated baseline; 0 consolidated baselines touched; 0 commit candidates; blind audits owed 6; text-versus-panel discrepancies flagged 3 (29163040 slice pre-incubation and bicuculline concentration, 35501379 Fig 1g-h colour keys, 31331032 percent reduction).

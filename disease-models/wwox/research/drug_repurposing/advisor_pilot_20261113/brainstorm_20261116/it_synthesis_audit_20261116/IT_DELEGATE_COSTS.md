# IT delegates of 2026-11-16 (second half of the day): cost read from transcripts (IT; non-canonical; not medical advice)

Written for: HE (final PROGRAMME_COST) and ADV. Source: `framework/scripts/session_model_census.py` on each delegate transcript under the session's `subagents/` folder (file name `agent-<id>.jsonl`); all sonnet-5-5, effort high; one active at a time. Delegates started before the matrix baseline arm in the first half of the day are not listed here.

| Delegate | agent id (transcript `agent-<id>.jsonl`) | turns | output | cache written | cache read |
|---|---|---|---|---|---|
| baseline arm of the matrix (memory-free) | a2796c7f30de0fff6 | 6 | 40,573 | 127,246 | 257,596 |
| baseline table of 137 frozen predictions (producer) | a68385a499e941bce | 54 | 46,811 | 207,918 | 6,833,670 |
| second read of 25 matrix cells | a51f1609a4b0787a8 | 30 | 32,907 | 115,700 | 1,858,185 |
| blind extractor of treatment statements | ac1e765589854cdbc | 38 | 73,560 | 257,068 | 4,511,879 |
| leap round arm A (simple search) | a939c72b922b63836 | 5 | 23,658 | 100,576 | 196,337 |
| leap judge run 1 (INVALID, anonymiser error) | ae0705b4d6d2158b2 | 77 | 54,395 | 220,187 | 9,567,610 |
| leap judge run 2 | a410fcd910bb92b5f | 72 | 57,012 | 214,528 | 9,795,184 |
| leap judge round 1b with planted pair | a847cc0bc3642c6b7 | 22 | 26,728 | 108,524 | 1,494,407 |
| round 2 arm B (repository, no perspective) | a20346211416aebb0 | 23 | 42,562 | 175,354 | 2,415,047 |
| judge of arm B with planted pair | a651dfda5a1553114 | 10 | 13,098 | 66,017 | 406,604 |
| test-setter (31 tests) | a416a426b952e83e8 | 6 | 38,729 | 81,959 | 285,077 |
| blind audit of the closing synthesis | a13f8bef853549f99 | 76 | 80,641 | 254,653 | 10,672,945 |

Sum of output tokens of these 12 delegates: 530,674 (the invalid judge run 1 is 54,395 of it). The tokens of IT's own session (reading, writing, scripts) are not separable here and are not counted.

Notes: (1) these are final census values; figures IT quoted earlier in messages were read at hand-back and are slightly lower for runs that received a follow-up message (leap judge run 2: 71 turns, 56,810 output at hand-back; round 1b judge: 21 turns, 26,559; the audit and the others are unchanged), so the final values here supersede them; (2) the test-setter figure here (38,729 output, 6 turns) is the census read, the 91,819 quoted earlier was the harness notice's total-token figure (all token classes), not output; (3) the baseline-table producer (a68385a499e941bce) is 46,811 output, not the 'about 40,000' of the earlier rough line in NEXT_PROGRAMME_IT.md, which stands as written (not edited) and is superseded by this table.

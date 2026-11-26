# IT28, 2026-11-26: ADV-282 increments 4 to 6 and ADV-294 N02 applied to the cards

Hypothesis level; reference genotype class only; nothing here is medical advice. Orchestrator window `54ca757b`
(mandate ORCH-ROADMAP-IT59-20261119, step IT28). Inputs: SCI's `RESULT_ADV282_INC4_6_SCI_20261126.md` (sections 3.1,
3.2 and 4), SCI's `ADDENDUM_L01_003_ADV282_SCI_20261126.md`, and the N02 wording of `RESULT_ADV294_IT_20261126.md`.
N10 of ADV-294 was not read, reworded or touched; no delegate was given a card file.

## What was applied
24 sentence sets in ten card packets (A01, A02, B01, E01, F01, F04, H02, I01, K01, L01), 27 text replacements,
cards rebuilt by the bridge, `check_cards.py` 30 packets 0 problems; join, coverage, ranking (order digest
`ff38fcaa61295a5a`, unmoved), the view trio in every language for both editions, shareable package;
`copied_card_sentences.py --base origin/main`: 20 card files, 148 replaced texts, 22 surfaces, 0 still held.
Files: `edits_it28.py` (the applied text), `apply_it28.py`, `make_packets_it28.py`.

| Kind | Ids |
|---|---|
| SCI section 3.1 (five verified MUST CHANGE) | DR-A01-007, DR-B01-002, DR-W2-004, DR-H02-036, DR-I01-014 |
| ADD (section 4 and held-apart 3.2) | DA-L01-005, DR-A02-010, DR-A02-006, DR-A02-007, DR-P9-009, DR-E01-002, DR-E01-003, DR-H02-008, DR-H02-023, DR-H02-024, DR-H02-030, DR-I01-006, DR-I01-001, DR-I01-002, DR-I01-004, DA-K01-007, DR-P9-010 |
| DR-L01-003 addendum (ADD only) | DR-L01-003 |
| ADV-294 | N02, card F04 `p4_fields.functional_evidence_available` |

## Three blind rounds (legend-delegate, sonnet, effort high stated in each dispatch and read back: 45, 10 and 51 turns, all claude-sonnet-5-5, all high)
Packets carried the new text, the assertion's own context fields and the whole held sources, never a card or a result file.
Reports as delivered: `VERIFIER_REPORT_AS_DELIVERED_A_IT28.txt` (11 blocks), `_B_` (13 blocks), `_C_` (the 17 blocks whose wording changed after A and B).
* Round 1 (24 sets): MUST CHANGE 10 (A01-007, L01-003, H02-008, K01-007, H02-036, H02-024, I01-014, I01-001, P9-009, P9-010), ADD 7 (N02, B01-002, A02-010, H02-030, I01-002, I01-004, E01-003), STANDS 7 (W2-004, L01-005, A02-006, A02-007, H02-023, I01-006, E01-002); 10 + 7 + 7 = 24.
* Round 2 (17 revised sets): MUST CHANGE 2 (A01-007, P9-010), ADD 8, STANDS 7.
* The round-2 findings (all qualifiers or one corrected clause) were folded without a third reader: that step is unchecked.
* First-composition rate for ADV-286: 10 of 24 composed sentence sets (42 percent) needed a change at the first blind round, inside the 25 to 45 percent range of the five earlier samples. These sets were composed from SCI-verified inputs plus a blind reader's wording, not free-written.

## Where the blind rounds corrected SCI's verified wording or my fold
* DR-I01-014: SCI's replacement said DCA shifted flux "toward PDC by about 40 percent". The abstract says a 40 percent decrease in anaplerotic-related flux toward PDC. Also the endpoint line named lactate while the direction code is glycolysis (endpoint reworded, direction unchanged).
* DR-H02-036: SCI left the first clause UNSETTLED. It is wrong: the muscimol statement belongs to the purified rat precursor cultures; the coculture result in the abstract is GABA alone. Rewritten.
* DR-H02-008: "hippocampal sclerosis" is not in the source; the paper scores hippocampal injury (extent score), 23 brains from three groups, 91 percent scoring 3 to 3.5.
* DR-A01-007: the HDAC1 ordering cannot be assigned to ChEMBL documents from the held aggregate rows; written as a bracket of values with the pairing named unresolved. The shareable-edition redaction rule for the old sentence (`shareable_sources.json`, card_substrings 13) was re-pointed at the new passage, which also hides the ChEMBL values there.
* DR-L01-003: SCI's "higher hippocampal neuronal density" is CA1 only (no CA3 difference; three animals per group; the abstract says both regions, the Results do not); the acute 24-hour cytokine, malondialdehyde, superoxide dismutase and catalase results are added.
* DA-K01-007: Hk2 range is -0.02 to +0.37 and Epas1 lower bound -0.59 under the script's pseudocount of 0.01; Slc2a1, Ldha and Pgk1 are lower in group means only (animal values overlap in some contrasts).
* DR-P9-010: the juvenile-rat lesions are not "high doses only" (lower dose with earlier dosing start); the source line said "retrieved 2026-10-29" while the held file is dated 2026-11-17 and 2026-11-18 and no 2026-10-29 pull was found by a file-name search of `files/` on 2026-11-26: the source line now says so.
* N02: pooled-distribution test for the six percent, the evoked-response claim rests on supplementary figure S3C (six slices, three animals, no correction), Grin2b is also lower in the neural stem cell RNA-seq, the "AMPAR-weighted" reading is an inference.

## Not settled or not applied
* The absolute negative in N02 ("any WWOX system", "any Wwox system") rests on the dated search of held sources of 2026-11-26 (ADV-294) and stays hedged as such; a blind reader could verify only the two papers.
* Figures of Hristodor 2025, Gupta 2023, Sheeni 2026 and Hussain 2019 are not held; clauses resting on them are by text and legend. Abstract-level rows keep their abstract-level limits.
* Dated originals that carry the old sentences were left unedited: `nmdar_pharmacology_it6_p9_20261029`, `broad_recovery_it6_p6_20261029`, `axis_it10_p22_20261031` (card L01 first packet), `ampa_comparison_it41_20261109/consumer_delta.md`, SCI's and IT's audit files.
* `reading_depth` and the F04 DR-P9-009 source string were not changed (a targeted read is not a complete-read record; no receipt written).

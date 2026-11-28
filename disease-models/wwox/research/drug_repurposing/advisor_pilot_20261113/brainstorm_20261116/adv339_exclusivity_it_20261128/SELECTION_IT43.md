# ADV-339 continuation: which candidate sentences were counted (IT43, 2026-11-28)

Hypothesis level; nothing here is medical advice. Written before any source of this half was opened by a first reader.
Candidate net: `enumerate_adv339.py` re-run on main `a53f69ffd` (54 records, 237 candidate sentences, 42 claims). Order of claims:
`consumers_it42_20261128.tsv` (031, 016, 036, 042, 030, 035, 019). The 12 counted sentences are in `selection_it43_20261128.tsv`
(`enum_index` = claim.position in the net's output). Packets: `files/coordination/adv339_it43/` (outside git).

## Selection rule
The PREREG rule (a line, arm, genotype, preparation or model given an endpoint or evidence to the exclusion of others, from a source with a
complete-read receipt). The pick is a judgement on the net's candidates and is not exhaustive: claims 035, 036, 030 and 019 hold further
candidates that were not listed or cut here.

## Seen and not taken
| Candidates | Reason |
|---|---|
| CLAIM 042 (three) | source PMID36537114 has no `complete_fulltext_read` receipt |
| 030.9 | the paragraph rests on PMID25331887, which has partial reads only |
| 019.3 | the range pools sources of which PMID30356099 has no complete read |
| 036.6 | a count-reconciliation remark about imaged femurs, not exclusivity of an arm |
| 016.0, 016.4, 035.6 | statements about what a text or LEGEND holds ("the only observation", "the only in vivo evidence"): literature or claim-level counts |
| 016.2, 016.3, 016.5, 035.1, 035.3, 036.4 | process, pointer or impact lines |

## Assignment
HE reads H1 to H6, SCI (successor BH) reads S1 to S6, each as an independent second reader. SCI was given the sentences whose sources are
least about regimens. The first reading is a `sonnet` delegate at effort medium, one at a time; its table is not shown to HE or SCI.

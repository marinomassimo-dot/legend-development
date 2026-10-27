# Value / cost trial IT2 - design only (roadmap iteration 2, package W4.6 step 1)

Scientist `scientist-b`, task SB-IT2-VALUETRIAL-REF-20261027, 2026-10-27T19:03:29Z. Non-canonical, research-work quality only. NO ANSWER EXISTS
at the time of this commit: this directory holds the design, the references, the scoring and the question text. Step 2 (running
the three conditions) and step 3 (independent scoring) are not done.

## What is compared
EXT (external public resources only), LOCAL (WWOX repository only, no live external calls), COMBINED, on three NEW cases absent from
the cards (a name search of cards/ and cards_early/ found no card on vitamin B6, sodium channel blockers or ferroptosis; the paper
registry does hold rows for some of the papers, so the topics are absent from the CARDS, not from the repository):
- V1 vitamin B6: compound-identity trap (pyridoxine vs PLP; WW domain-containing OXIDOREDUCTASE vs pyridoxamine phosphate OXIDASE; WOREE n=1 negative).
- V2 sodium channel blockers: variant-class applicability (SCN2A gain/loss-of-function rule vs WWOX; a 16q-deletion case that is not WWOX evidence).
- V3 ferroptosis: abstention case (opposite sign in lung and liver cancer, both non-neural).
Questions are word-identical across conditions except the allowed-inputs block; budget identical (25 tool calls, 12 minutes, one run).

## Files and fixed hashes (SHA-256, computed before any answer exists)
| File | SHA-256 |
|---|---|
| reference.md | 7a6df0497fd09daf9aee910d95b239a6abccecab6e21204ce6e879e2e4ce615b |
| scoring.md | d821c2cb55e629d43e21498e13e6c36d50b68e85882222d2968ddb61102f1cc6 |
| questions_ext.md | 6532579ba8151114c549b252d46411bed8ff94d79693754f0c6d0c3c1a74b4b2 |
| questions_local.md | 8cb8f3d7bdca897a02b1fccaaf5502bf3983de8f926ea9220b735734fd191abc |
| questions_combined.md | 7d36f928f36afe48193c9aa60560defac177be3d726b95cc374a7726e11f311e |

## Declared weaknesses (full list in scoring.md section 7)
n = 3, one run per condition, same model family, abstract-depth references by one author, cases chosen by the producer to carry a trap each,
producer must not score; P3A's C-versus-B margin was not a finding and no superiority is to be presented. Costs are to be OBSERVED
(transcript tool_use count, harness usage tokens, duration_ms) and reported beside, never replaced by, the agent self-estimates.

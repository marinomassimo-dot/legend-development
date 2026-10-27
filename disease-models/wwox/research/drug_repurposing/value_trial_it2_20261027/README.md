# Value / cost trial IT2 - design only (roadmap iteration 2, package W4.6 step 1)

Scientist `scientist-b`, task SB-IT2-VALUETRIAL-REF-20261027, 2026-10-27T19:03:29Z. Non-canonical, research-work quality only. NO ANSWER EXISTS
at the time of this commit: this directory holds the design, the references, the scoring and the question text. Step 2 (running
the three conditions) and step 3 (independent scoring) are not done.

## What is compared
EXT (external public resources only), LOCAL (WWOX repository only, no live external calls), COMBINED, on three NEW cases absent from
the cards (a name search of cards/ and cards_early/ found no card on vitamin B6, sodium channel blockers or ferroptosis; the paper
registry does hold rows for some of the papers, so the topics are absent from the CARDS only: registry rows, a partial MO19 full-text dossier, case-series dossiers and wave-4 vitamin B6 notes exist, and LOCAL/COMBINED start with those):
- V1 vitamin B6: compound-identity trap (pyridoxine vs PLP; WW domain-containing OXIDOREDUCTASE vs pyridoxamine phosphate OXIDASE; WOREE n=1 negative).
- V2 sodium channel blockers: variant-class applicability (SCN2A gain/loss-of-function rule vs WWOX; a 16q-deletion case that is not WWOX evidence).
- V3 ferroptosis: abstention case (opposite sign in lung and liver cancer, both non-neural).
Questions are word-identical across conditions except the allowed-inputs block; budget identical (25 tool calls, 12 minutes, one run).

## Files and fixed hashes (SHA-256, correction round 2 - computed before any answer exists)
| File | SHA-256 |
|---|---|
| reference.md | 769a893de7ef6703453745d919044b56111fb6267e58a1c1072b7e724bcf8943 |
| scoring.md | e7b79d837b1b8f2b5fc25fb92553a9c7afddc79180bddb4a3d8e8346d4d1b9a5 |
| questions_ext.md | 6532579ba8151114c549b252d46411bed8ff94d79693754f0c6d0c3c1a74b4b2 |
| questions_local.md | b1df034aea692e14fb3673be6f2cc606b2b289b90f0b6576fd2bc91ab98aae90 |
| questions_combined.md | d0cfe106bd1c9a404f537fe3394985bd79bd700068cff31f82c3f43e505e8afe |

Round 1 hashes (superseded, main 28b071ed): reference.md 7a6df049..., scoring.md d821c2cb..., questions_ext 6532579b..., questions_local 8cb8f3d7..., questions_combined 7d36f928.... Round 2 applies the independent verification (locator_audits/2026-10-27_value_trial_reference_verification.md): 1.1 qualified, 2.1 "rarely", 2.3 scope (public WWOX exposure reports are not overreach), X.5 judged against the answer's own stated depth, MO19 wording, 3.3 "cytotoxic" dropped, WA25 year 2026 and "mouse" dropped, abstract-level marking for the four paywalled papers, leak isolation.

## Runner section (mandatory for step 2)
The answer key sits in this directory, in ledger/tasks/scientist-b/SB-IT2-VALUETRIAL-REF-20261027.json, in ledger/tasks/orchestrator/VERIFY-VALUETRIALREF-20261027.json and in research/locator_audits/2026-10-27_value_trial_reference_verification.md. LOCAL and COMBINED runs MUST be done in a clone without them; a run that reads, greps into or lists them is VOID. EXT runs get no repository access at all. Exact commands (the clone is scratch only; never commit, never push from it; replace <SCRATCH> with the session scratchpad and use the main commit that contains this README):
```
git clone --no-hardlinks /home/desktop/legend-development <SCRATCH>/vt_clone
cd <SCRATCH>/vt_clone && git checkout --detach <MAIN_COMMIT>
git rm -r -q disease-models/wwox/research/drug_repurposing/value_trial_it2_20261027   ledger/tasks/scientist-b/SB-IT2-VALUETRIAL-REF-20261027.json   ledger/tasks/orchestrator/VERIFY-VALUETRIALREF-20261027.json   disease-models/wwox/research/locator_audits/2026-10-27_value_trial_reference_verification.md
git ls-files | grep -i -E 'value_trial|VALUETRIAL' ; echo "expect no output above"
```
Then remove the key from HISTORY too (git rm alone leaves it in the clone's git objects), still inside the clone only:
\`\`\`
git checkout -q --orphan clean && git -c user.name=x -c user.email=x@x commit -q -m "trial clone, key removed"
git for-each-ref --format='%(refname)' refs/heads refs/remotes refs/tags | grep -v 'refs/heads/clean$' | xargs -r -n1 git update-ref -d
git remote remove origin; git reflog expire --expire=now --all; git gc -q --prune=now
git log --oneline | wc -l   # expect 1
\`\`\`
Copy the one questions_*.md for the condition from the ORIGINAL checkout into <SCRATCH> outside the clone and give that text to the subagent; run LOCAL/COMBINED with the clone as working directory. The transcript check (scoring.md section 1) voids any run that touched the paths.

## Declared weaknesses (full list in scoring.md section 7)
n = 3, one run per condition, same model family, abstract-depth references by one author, cases chosen by the producer to carry a trap each,
producer must not score; P3A's C-versus-B margin was not a finding and no superiority is to be presented. Costs are to be OBSERVED
(transcript tool_use count, harness usage tokens, duration_ms) and reported beside, never replaced by, the agent self-estimates.

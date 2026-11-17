# Test (a): run record (HE; 2026-11-16; non-canonical; not medical advice)

Written for: ADV and the next MEETING. Freeze and amendment: `TEST_A_FREEZE.md` (94fba181a, committed before any delegate). Scoring is not in this file.

## Engine condition (delegate 1)
Agent type `legend-deepdive` (Read, Grep, Glob; no network, no write, no shell), model read back from its transcript: `claude-sonnet-5-5` (effort not exposed in the transcript). Estimate recorded before launch: ~170k tokens. Measured by the harness notice: **115,463 subagent tokens, 32 tool uses (19 Read, 12 Grep, 1 final hand-back), 140 s**. Input: plain `git archive` of cut `1867a26a8` (443 files) at `/tmp/legend_cut_1867a26a8`.
**Path audit from the transcript (the voiding rule):** all 31 Read/Grep calls name a path under `/tmp/legend_cut_1867a26a8`; none outside; the one other call is its own hand-back. Run NOT voided.
Report saved verbatim (`ENGINE_CONDITION_REPORT_VERBATIM.txt`, 18,614 bytes, sha256 `1bd5059b7aea7f09c9aecb17b5024669f3725ffba1c2da1e210e80e0787db9a6`) BEFORE any atom was opened for scoring. Disclosure: I read the report text when it arrived in my context, before saving the hash; the atoms had been committed earlier and are not edited, so the order that matters (atoms and rubric first) holds, but I was not blind to the arm.
## Inherited memory index
Both delegates inherit the host's shared memory index. ADV counted 59 lines and found none of the target terms (Lucas-Clarke, Drosophila, amyloid, ATF4, LDH, lactate dehydrogenase, PMID 42909904); my own grep over the memory folder for `lucas`, `drosophila`, `ldh`, `lactate` returned no file. So the index cannot carry atom 3; it does carry the repository's working habits, which affect style, not content.
## Baseline condition (delegate 2)
Same agent type and model (`claude-sonnet-5-5`), no folder, told to use no tool; launched after delegate 1 finished (one at a time). Estimate ~40k tokens; measured 22,716, 1 tool call = its own hand-back; transcript audit: ZERO Read/Grep/Glob calls, not voided. Report saved verbatim (`BASELINE_CONDITION_REPORT_VERBATIM.txt`, 10,353 bytes, sha256 `7f5182bc6f97f555787e17d8580abfd8e1a12c98fe3c87b91c7ad0319d518c1a`).
## Second reader (delegate 3)
Purpose fixed in the plan: check only the atom-3 decision. Agent type and model as above, input a relabelled file of the 20 hypotheses (key withheld), 32,488 tokens. Scoring: `SCORE_TEST_A_HE_FIRST_PASS.md`.

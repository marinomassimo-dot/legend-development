# Materials-contribution test: criteria frozen before any arm is dispatched (SCI with IT, 2026-11-19; hypothesis level; one case; no general claim; no dose or recommendation; not medical advice)

Merged with IT's proposal (confirmed by IT) and ADV's instruction (one comparison; declare the effective isolation honestly). Decision under test, **prospective (outcome unknown to both arms and to me)**: does the WWOX WW1-domain / PPxY-motif partner branch (ERBB4 and NETO2 proposed, not established) justify a pharmacological comparison, a distinct experiment, or neither, and which?

## Frozen inputs (sha256)
| File | sha256 |
|---|---|
| ARM_BRIEF_COMMON.md (identical for both arms) | 3ec81e081f2b5235cbfc0da76de793e49f90e3181dd6bfbfa7bc8ce2fccacc66 |
| ARM_S_ADDENDUM.md | cd93e86f4db94a8d3977cd2174c9562df39bc73b5b25d18fc57abb3fa33d372d |
| ARM_L_ADDENDUM.md | 825620714c23c86ee6830f85fa68dd8607aea4aa8600f7dcc0892382fd9e677d |
| VERIFIER_BRIEF.md | 1e9233f2681e5610e4730932a3ddc1731b8fecd2cdff2021b49355084dbcb7e6 |
| LOOP_PACK_SHA256SUMS.txt (manifest of the structured arm's loop pack: 11 files copied from the repository, held in the scratchpad, not in git) | 6fdeb9e47a21a2dbd9e6eabb97ab7691de94eae30f7f5851417f263c1ae7da35 |
The loop pack is the structured arm's only addition: census note, ADV-068 and ADV-070 results (the counter-evidence that no PV-directed premise follows from transcripts and that stage adjustment is not decisive), HE's PPxY census dossier with its two addenda and ranked table, the need on inhibitory hypofunction, the open-question rows, two investigation notes.

## Comparability (the same for both arms)
Agent type `legend-delegate` (same tool list), model `sonnet`, effort `medium`, **at most 60 tool calls**, report of at most 2200 words in one fixed format, no model or effort escalation, one run per arm, no repetition. **What each arm inherits is read back and written down for both**: the delegate loads the project's standing instructions and the memory index at birth (the lean arm is **not memory-free**; "empty directory" is not claimed); read-back = the first rows of each delegate transcript (context size at birth and the model and effort via the session census) and every tool call checked for reads under the repository (the lean arm must make none; the structured arm only the pack paths and primary sources). A violation is recorded and reported, not corrected after the fact. Wall time is recorded from dispatch to completion notice.

## Judge and procedure
A separate verifier delegate (sonnet, effort high) receives the two reports as X and Y with the arm labels removed and **presentation order fixed by the parity of the last hex digit of this file's sha256 (even: the structured arm's report is X; odd: the lean arm's report is X)**, recorded in the result. It opens primary sources for **pivotal claims only** and says which it opened. It follows VERIFIER_BRIEF.md.

## Primary outcome (the winner rule) and what is only descriptive
* **Primary outcome = the verifier's judgement, per the six pre-declared categories** (MORE_INFORMATIVE_PHARMACOLOGICAL_COMPARISON, MORE_DEFENSIBLE_CONDITIONAL_HYPOTHESIS, EXPERIMENT_SEPARATES_ALTERNATIVES_BETTER, RETRIEVED_QUESTION_THE_OTHER_MISSED, NO_DIFFERENCE, HARM_OR_NEEDLESS_COMPLEXITY), of which output better supports the decision.
* **HARM defined now:** a candidate or lever justified by an interaction that is only proposed; relation identity (direct binding, which WW domain, species, assay) asserted beyond its source; a sign or function transferred across species, age or cell type without saying so; an absence claim without its search perimeter.
* **NO_DIFFERENCE fixed now:** same decision and no extra item the verifier judges able to change the comparison or the experiment; recorded as traceability only; then no repetition with more readers.
* **Descriptive only, never the winner rule:** the share of the six questions answered with a full-text anchor; claims the verifier finds contradicted or unfindable; pivotal claims left unchecked; cost per arm (turns, output tokens, cache-read tokens from the session census with the one-response-once rule; birth context; wall time).

## What the result may and may not say
One case, one model, one run per arm, one verifier: it can say whether, on this decision, the loop's materials changed what a delegate with the same budget delivered, and what the extra items were. It cannot say that the structure is better in general, and **a difference is not credited to the structure if the lean arm's report shows the same items were reachable by the same tool-call budget** (the verifier is asked which items came from the pack). The structured arm's use of the pack is read from its report and its tool calls. Counter-evidence the outcome must carry (from IT): ADV-068 (no PV-directed premise from transcripts) and ADV-070 (stage adjustment not decisive).

## Consumption (IT's path, fixed before)
(a) one open-question row if the relation is not established with primary evidence; (b) a hypotheses_only package under INV-05 plus one comparison row only if relation identity, primary evidence, neural context and a lever all survive; (c) a refusal row with its reason otherwise.

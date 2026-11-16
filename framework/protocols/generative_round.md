---
artifact: LEGEND protocol — GENERATIVE ROUND · how a round of new hypotheses is generated, frozen, judged and costed
protocol_id: GENERATIVE_ROUND
version: 1
normative: no — descriptive of the round run on 2026-11-16, with the lessons that day taught; it adds no gate
status: PROPOSED · items marked [asked] were requested in that round and have not been run yet
materialized_by: plan
materialized_on: 2026-11-16
---

# GENERATIVE ROUND — procedure, as run on 2026-11-16, and where it fell short

Written for: the next programme's planners (ADV, the Orchestrator, Science, Harness). Mechanism and repurposing-class labels only; no dose, no recommendation. Evidence: `research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/` (LEAP_ROUND.md, it_leap_judge_20261116/, it_arm_b_20261116/, leap_sci_20261116/, programme_cost_he_20261116/).

## 1 · Arms
* **A, memory-free simple search:** one delegate, a bundle of summaries, no repository files; the baseline against which everything is read. Its output is frozen by hash BEFORE anyone reads an author file.
* **B, repository-aware, no perspective:** one delegate with the repository and the same template (added in round 2; without it, "authors beat the baseline" cannot be told from "knowing the repository helps").
* **Authors with one named perspective each,** at most 5 hypotheses, written alone, without reading each other's files. A perspective is a label, so author and perspective are confounded.
* "Memory-free" is a declaration: a delegate has Bash and inherits the memory index. Say it as declared.

## 2 · Template (one block per hypothesis)
Perspective used · statement (a mechanism, one sentence) with its rejecting observation · why a leap (what the usual reading assumes and this one drops) · the held table or assay that tests it (path) · the single discriminating observation and what each outcome changes · repurposing class as a label with its source · held-data pre-test and its result · what would change my mind · cost to test. **[asked, SCI and ADV]** four more fields: number of independent origins behind the premise; the held tables seen BEFORE writing; "could the held data have rejected it" (yes or no, which table); a numeric kill criterion.

## 3 · Freeze rules
1. Order: criteria and rule, then the authors' files and arm A's output, then the judge's input and its key digest, then the judge, then the key. Nothing is read out of order.
2. A freeze is a commit that is **merged, never rebased or cherry-picked**: a rebase moves the committer time (HE's leap file, frozen at 08:24:31Z, landed as a commit stamped 08:41:23Z; IT's release record had the same property). The identity of a frozen file is its blob sha256, written in the message.
3. One ledger row per hypothesis (`prediction_ledger.py`: kind `generative`, predictor the author, `freeze_utc_declared`); `check` prints "freeze time declared, not shown by git (rebased)" when the commit is later than the declared time, and `guard` refuses to open an outcome table before its freezes exist.

## 4 · Judge setup
* One delegate, not an author, one active at a time; model and effort stated; read back from its transcript afterwards.
* **Anonymiser.** Strip perspective, ids, labels, session and arm vocabulary, then **check what is left**: round 1 run 1 was INVALID because a script deleted every line containing "Perspective" and blanked the whole body of 10 of 24 one-paragraph hypotheses. **[asked]** shortest-block check: after anonymising, every block must keep the share of its original length that was fixed before the run, else stop.
* **Body-seen echo.** The judge quotes an exact span from each hypothesis body; the quotes are checked as substrings of the input mechanically (24 of 24, 26 of 26, 7 of 7 passed).
* **Planted pair** (one novel and testable, one already in the repository, reworded) with its key digest PUSHED before the run. Round 1b did; round 2 wrote the key file before the run but pushed no digest, so its integrity claim is weaker. **Length-matched:** in round 2 the planted items were 1.6 to 1.8 KB against 3.6 to 4.1 KB for the real ones, so length was a tell. Two planted items measure nothing about rates.
* **Graded, not one definition.** Each criterion yes, partial or no; report all three survival definitions side by side: S1 all four yes, S2 no "no", S3 no "no" and at most one "partial". The key is published only after the table is committed by hash.

## 5 · Held-data fate table
Categories: R rejecting observation met · C counter-signal · N consistent, not rejected · P partly supported · U untestable by held data. Labels: *independent* or *consistency only* (the data shaped the hypothesis). **Before any category is counted, a column "could the held data have rejected it":** an N from a presence condition (a gene is detected in both arms) carries no weight, and fate rewards weak tests. Rule: P only if the hypothesis's own premise is reproduced; R or C only if the author's own rejecting observation can be evaluated on held data. The pre-test is run by someone who did not write the hypothesis (SCI ran all five pre-tests of its own items). **A second read of the categories that decide a count:** IT agreed on 5 of 8 independent items and disagreed on 3; report the agreement beside every count.

## 6 · Cost lines
`programme_cost_he_20261116/programme_cost.py --until <ISO UTC>` reads sessions (`trial_window_table.py`) and each delegate transcript (`session_model_census.py`): turns, output, cache written, cache read; no estimate, no share of a plan. The **invalid run is its own line** (54,395 output tokens, 13.7 percent of the delegates' output, no use). Value lines name numerator and denominator (output per survivor, per hypothesis judged, per row read). The authors' own output per hypothesis is not separable from their other work: say so rather than invent it.

## 7 · Stop rule
Stop paying for the leap step if arm A equals the authors in three consecutive rounds. Not yet defined: "equal". Fix the margin on a named survival definition before round 1. On 2026-11-16: round 1 (one definition) 1 survivor of 24, all from arm A; round 1b the same 24 items gave 9 (S1), 24 (S2), 22 (S3), with arm A 2 of 5 and authors 7 of 19 on S1; arm B 4 of 5. Differences of one or two items.

## 8 · Known limits of every measure
* **Strictness governs the count:** the same 24 hypotheses moved from 1 to 9 to 22 survivors with the definition; the arm differences are inside that noise.
* **Fate rewards weak tests** (section 5) and is partly shaped by the scan that wrote the hypothesis (two of SCI's own items).
* **Length is a tell** for planted items and for arms; style differs by arm.
* **n is 4 or 5 per arm,** one judge instance per criteria set (arm B was judged by another instance than arm A and the authors), one run each.
* The key holder wrote one author file and ran arm A. Novelty is a keyword search. Blinding of delegates and judge is declared, not enforced.
* Round 1's criterion (a) penalises knowledge: an agent that has read the repository finds it already holds things the memory-free arm cannot know.

## 9 · What to do differently next time (from the day)
Decide the survival definition and the "equal" margin before round 1. Anonymise, then check. Push the planted key's digest. Length-match the planted pair. Log the tables seen. Count origins before building any ranking on the premise, and compute the projected number of classifiable pairs before building an extraction.

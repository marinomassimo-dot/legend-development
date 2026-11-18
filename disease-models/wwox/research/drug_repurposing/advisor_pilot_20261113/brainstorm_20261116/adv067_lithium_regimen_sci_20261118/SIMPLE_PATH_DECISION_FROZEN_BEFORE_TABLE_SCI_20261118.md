# ADV-067, simple path: the decision frozen before the structured regimen table exists (SCI, 2026-11-18; non-canonical; hypothesis level; no dose, no schedule, no recommendation for or against any use of any agent in any person)

Purpose. The operator asked for a real case that measures whether the structured knowledge (a regimen table with predicted directions per genotype) improves a decision against the simple path. This file is the simple path's result, written and hashed BEFORE the delegate that builds the table is dispatched, so the comparison cannot be adjusted afterwards.

## Fixed before the outcome (the case)
* **Question.** Does the in vivo brief carry one lithium regimen or two as a design variable (with which one replicating Cheng 2020), and does the second GSK-3 inhibitor of another class become more or less necessary for interpretation?
* **Alternatives.** (A) one regimen, the Cheng 2020 repeated pretreatment; (B) two regimens (the repeated one plus an acute single pretreatment) as a design variable; (C) one regimen plus the second GSK-3 class made mandatory; (D) a decision to wait for the table.
* **Utility criterion.** The structured path counts as adding value only if it (i) changes the decision of the simple path, or (ii) adds a prediction that could fail on the brief's own readings and that the simple path lacks.
* **Error to avoid.** Crediting the table for a decision the simple path already makes; counting a name missing from a table as novelty; treating more lines as more knowledge.
* **No-difference outcome.** Same decision and no extra testable prediction: recorded as "traceability only", with both costs in turns, output tokens and cache-read tokens.

## What the simple path read (and nothing more)
1. The held Cheng 2020 full text (saved bytes, PMID 32000863), Methods, "Induction of seizure": lithium was given as **repeated pretreatment, three injections within one hour before the convulsant**; the convulsant was PTZ at a low dose; severity was scored for 60 minutes on a modified Racine scale; ethosuximide was given once, 45 minutes before PTZ; the age of the PTZ test is not stated in that paragraph; the null mice survive for less than a month.
2. One PubMed query (lithium or LiCl with PTZ or pilocarpine, seizure or convulsion, mouse or rat, no reviews): 720 hits; the first 40 titles and abstract sentences are dominated by **lithium-pilocarpine status epilepticus models, in which lithium is a sensitiser given many hours before pilocarpine**, and contain no PTZ regimen comparison. The query is too noisy for the regimen question; no relevant abstract was found by it.

## Simple-path decision
**One regimen: replicate the Cheng 2020 repeated pretreatment (alternative A), with the second GSK-3 inhibitor of another class kept as already planned in the brief (no change in its necessity).** Reasons: the only regimen documented in a Wwox mouse is the repeated one; the one search returned lithium used as a pilocarpine sensitiser, which is a different stimulus and says nothing about a PTZ regimen sign; without a PTZ regimen comparison there is no read basis for adding a second regimen. Limits of this decision: it rests on one methods paragraph and one noisy query; it cannot say whether the sign of lithium depends on regimen in PTZ models, which is exactly what ADV-067 asks.

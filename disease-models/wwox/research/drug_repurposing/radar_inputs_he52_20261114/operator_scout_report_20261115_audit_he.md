# Static audit of the operator's capability-scout report of 2026-11-15 (HE, 2026-11-15)

Non-canonical working note. Not medical advice. Written for ADV, IT, SCI and the operator. Task record `ledger/tasks/plan/PLAN-HE-IT23-SYMBOL-TRIAL-20261115.json` (OBJ_2). Static audit only: no installation, no code run, no spend, no external account. The report audited is `operator_scout_report_20261115.md` in this folder.

## Limit stated first
I read the two sources at abstract and README level. I did not read the Contrastive Discovery paper body, did not open the Skill2Query code, and did not audit the four other "Replay" backlog items (they cite other papers). The gains below are the authors' claims, measured on their benchmarks and not on LEGEND.

## What was checked, and what it showed

| Item | Check | Result |
|---|---|---|
| Contrastive Discovery (Liu, Kim, Dai, Sun) | Existence, date, numbers | Exists, dated 2026-11-10 (arXiv listing 2611.14514). The abstract-level numbers match the report: 6 domains; 73% of high-belief-shift pointwise candidates (89% of which were rejections) resolved to a specific alternative; 67% more questions resolved than pointwise surprisal at the same experiment budget; 38 blinded experts, 78% agreement on resolved questions. One number the report omits: experts agreed in 82% of the cases where the pointwise agent rejected its hypothesis and stopped. No code link or licence appeared in the source I read |
| Skill2Query (Ding et al.) | Existence, date, numbers, code, licence | Exists, submitted 2026-08-17 (arXiv 2608.16071); average Recall@1 gain 6.70 percentage points, nearly 30K skills, 700K pseudo-queries, as reported. The repository README declares the MIT licence (the LICENSE file itself was not read) and states that the execution verifier is not implemented (static slot checks instead). It needs Python 3.9 or later, an OpenAI API key in its configuration, and optionally a GPU and Docker |

## Coverage first: does LEGEND already hold a competing-explanations step?

| Where | What it holds | Source |
|---|---|---|
| Generation | "as many mechanistically distinct hypotheses as the live explanatory space contains", then critique, ranking, evolution | `.claude/skills/legend-hypothesis-forge/SKILL.md` |
| Discovery method | `diverge_hypotheses` (rivals written down), `preregister_prediction`, `compress_experiment` (an experiment that discriminates rather than measures); optional | `.claude/skills/legend-discovery-method/SKILL.md` |
| Proposal records | `competing_explanations` and `expected_result_by_explanation` on every conditional proposal; IT40 measured that for the AMPA/NMDA package (BH1-BH3) the readable arm-by-explanation cells went from 0 to a counted set and the rivals became reachable through a column map | `generation_it40_20261109/conditional_proposals.py`, `measure_it40.py` rows 2 |
| Open case | the roadmap's own question for ADV-007 (which observation would separate soluble signal, composition and contact) is a contrast set already stated | `roadmap_current.md`, 2026-11-15 entry |

What the same files show as not covered: (a) the explanation set is not required to be mutually exclusive and collectively exhaustive (the proposal records say the package "does not classify them as rivals, complementary or compatible"); (b) there is no slot that says "none of these" (an unknown mechanism) as a standing option; (c) nothing records, when a result arrives, which rival each observation favoured and by how much, so a rejection ends as `refuted` with a reason and not as a redistribution over the rivals. The scout's own wording, "gap to be verified", fits: (a) to (c) are an observed absence in the files I read, not a measured failure of any past decision.

## Verdicts

| Item | Verdict | Reason and limit |
|---|---|---|
| Contrastive Discovery, as a pattern | **MONITOR; replay only if a Scientist has a free slot** | The principle is covered at generation and proposal time in three places; only (a) to (c) above are missing. Building anything would repeat what exists. The scout's pilot (three already-judged mechanistic hypotheses, two or three rivals each, read the existing evidence) is a read-only exercise on existing records and needs no new structure; its candidates already exist (INV-05 BH1-BH3 with their expected results, the ADV-007 contrast). I do not run it: the replay is a reading task for a Scientist, and its success criterion (more questions resolved correctly without more unsupported conclusions) needs a reader other than the one who wrote the rivals. No harness change |
| Skill2Query, as a pattern | **WATCH; no pilot now** | I found no recorded case in this repository of a skill that was needed and not retrieved, so there is no demonstrated defect for it to fix (not searched exhaustively). The paper's gain is on a 30K-skill benchmark; LEGEND lists a few dozen skills with long trigger descriptions. The code needs an OpenAI key and optional GPU and Docker, which is a new external dependency for a gain that is unmeasured here. Reopen when a skill-selection failure is observed |
| Contrastive Hypothesis Replay (the scout's micro-upgrade) | **Not adopted as a build** | Same as the first row. The five fixtures are reasonable test cases for a replay and are kept here as a list |
| The four other Replays | **Not audited here** | Each cites a different paper; they need their own coverage check first |

## What would change this
A Scientist replay that finds an existing rejection which, read against its rivals, favours a specific alternative (or shows none can be chosen) would show (c) is a real loss and turns the verdict to TRIAL for one slot in the proposal record. A skill that was needed and not selected, with the transcript, would reopen Skill2Query.

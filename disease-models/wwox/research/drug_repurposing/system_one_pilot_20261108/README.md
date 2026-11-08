# System One pilot: choosing the next piece of work (2026-11-08)

Non-canonical research material. Not medical advice. Zero spend: no paid API, credit, cloud GPU or metered service was used. Nothing here edits a scientific current file, a card, a need, a ranking, a ledger or a registry, and nothing adds a gate, a service or a mandatory step. Pre-registration: [`PRE_REGISTRATION.md`](PRE_REGISTRATION.md) (frozen in commit 22d11c24 before any model arm ran).

## Answer first

**Rizzo Flow: INCONCLUSIVE, with no case for adoption.** It was not run. The auto-mode classifier denied the one command that would have downloaded and started third-party prebuilt binaries (the pinned llama.cpp runtime) and 2.6 GB of weights, and that denial was respected, not worked around. The comparison that could be run without any installation found **no room for improvement in decision quality**: the plain current behaviour (arm A) already chose an acceptable action in 16 of 16 new decisions and never chose a wasteful one, and structured scoring with the same model (arm C) did the same. A fourth arm cannot improve a ceiling, so the only benefit left for Rizzo Flow to show is cost, and its cost on this host is unmeasured.

| | Verdict | Why |
|---|---|---|
| Rizzo Flow component | **INCONCLUSIVE** | not executed; reopening conditions below |
| Structured choice (state, alternatives incl. "reuse" and "none sufficient", score) | **no measurable gain over arm A on these cases**; harmless | A 16/16, C 16/16, same wasteful picks (0) |
| Simple rule | **useful only with typed facts** | B(facts) 15/16; B(keywords on text) 10/16 with 4 wasteful picks |

## Scope and limits of this result (added at closure, 2026-11-08)

* **What arm A measures.** A choice among listed options on a state that was prepared in advance. It does not measure the Orchestrator's complete operational behaviour: finding the state in the records, deciding which options exist, noticing a fork that nobody listed, and carrying the action out are all outside it.
* **What "no worsening" means.** On this sample of 16 decisions no arm made a wasteful, overclaiming or rule-breaking choice that the labels or the blind verifier flagged (arms A and C). That is an observation about this sample. It is not a conclusion that the pattern is harmless in general, and with 16 cases a difference of one or two is noise.
* **Rizzo Flow** stays not executed and INCONCLUSIVE. A saving in cost at equal decision quality remains possible and is untested: the model arms were at ceiling, so quality cannot separate them, and the cost side was never measured for the component.
* **The conservative picks are not a preference to keep.** Every model arm took the record-and-hand-off option in N05, N08 and N13 where an expanding option was also reasonable. That follows from how these states and labels were written (they describe what is already recorded; IT30 named the same bias). It must not be fed into any prompt, rule, ranking or default as a learned preference for abstaining or stopping.

## The 16 cases and the arms

16 new decisions (7 categories: reuse a result; retrieve a source; run a check; deepen a question; declare the information insufficient; resource documented but unavailable; no adequate option), with states reconstructed from repository records as they stand today, five options each, letters shuffled with a fixed seed. Labels (best / reasonable / weak / wasteful or overclaiming) were written by the author before any arm ran; a blind verifier (arm V) marked the options independently.

| Arm | Reasonable pick (of 16) | Best pick | Wasteful or rule-breaking pick | NONE right / wrong |
|---|---|---|---|---|
| A current behaviour, free choice | 16 | 12 of 13 | 0 | 2 of 2 / 0 |
| A' same, option order reversed | 16 | 12 of 13 | 0 | 2 of 2 / 0 |
| C structured scoring 0-3 | 16 | 13 of 13 | 0 | 2 of 2 / 0 |
| C' same, order reversed | 16 | 12 of 13 | 0 | 2 of 2 / 0 |
| B(facts) rule over typed facts | 15 | 12 of 13 | 0 | 2 of 2 / 1 |
| B(keywords) rule over the text | 10 | 7 of 13 | 4 | 0 of 2 / 2 |
| V blind verifier | marked no wasteful option reasonable; NONE_SUFFICIENT on N15 and N16 only | | | |

Position and ordering: A gave the same action in both orders in 16 of 16, C in 15 of 16 (N07, both choices reasonable). A and C differ in one case only (N07, again both reasonable). Verifier and author labels do not disagree on any wasteful option.

**What this does and does not show.** The set is at ceiling for both model arms. The reasons are the ones IT30 already named and this set repeats: each state is written from the records and so states what is recorded, the labels are the author's, and the repository's own vocabulary ("dated record", "reopening condition") appears in the right option. It shows that the pattern does no harm and that a fresh context already avoids repeated and overclaiming options on documented forks. It does not show that the pattern fails on a real fork where the right action was not visible, because this set contains none.

**Where the arms did not look equally good.** In the three cases where the informative option is only reasonable and not best (N05 open-copy search, N08 reading papers that cite the result, N13 a literature batch that never names WWOX) every model arm chose the conservative record-and-hand-off option instead, in both orders. Where the informative option was the best one (N10 single-row re-audit, N11 edge screen, N12 cause separation) every model arm chose it. So structured choice did not penalise an informative option when it was best; it also did not produce the expansion toward literature beyond the keyword that the roadmap asks for. That is a tendency to watch in a forward test, not an error under these labels.

## Whole-flow cost

| Item | Observed | Estimated, not observed |
|---|---|---|
| Subagent run of 16 cases, arms A, A', C, C', V | read back with `framework/scripts/session_model_census.py` from the five transcripts: all five ran `claude-sonnet-5-5` on both turns; birth context 39,675 to 39,678 tokens (fixed agent overhead, before the case file is read); peak context 49,022 to 49,107, so reading the case file added about 9,350 to 9,430; output 664 (A'), 665 (A), 707 (C), 778 (C'), 779 (V). The completion notices (49,567 to 49,762 tokens) equal peak plus output. 8.7 to 10.5 s, one file read each | the first version of this table said the prompt was about 4,000 tokens and the rest of the 49.6k overhead; the census replaces that: about 80% is fixed overhead and the 16 cases themselves cost about 9,400 input tokens. Structured scoring added 42 to 115 output tokens per run over free choice. Any saving from a local selector is therefore a share of about 9,400 input tokens per 16 decisions plus the fixed overhead of a fresh context, and is an estimate until the component is run |
| Input preparation, rule B(facts) | five typed fields per case, written by the author | the effort to type them for a real decision is the cost of the judgement the rule needs: B(keywords) shows what is lost without it |
| Fallbacks | N07 changed between orders (both reasonable); no fallback was needed | |
| Local resources for Rizzo Flow | none measured | documented: 4B Q4_K_M weights 2.6 GB, KV cache about 144 KiB per token, 4 CPUs and about 7 GB free RAM on this host (shared with other sessions' batteries); CPU-only Linux is listed by its README as not run |

## Rizzo Flow: what was and was not done

* **Read, not run.** Source cloned to a scratch directory (commit b9ba007e, 2026-09-25) and read: the only network calls in the code are the release download from github.com/ggml-org/llama.cpp (pinned b11081, sha256 listed per platform, a Linux x64 CPU package exists) and the weights download from Hugging Face; no telemetry, account or other call is in the source. Python dependencies sync in under one second into a 12 MB environment (this was done, in the scratch directory). Code, the default weights and llama.cpp are Apache-2.0, Apache-2.0 and MIT; the model card flags that one training dataset is CC-BY-SA and asks users to check before redistributing derivatives. Nothing would be redistributed here.
* **Operational limit, separate from the evaluation of the component.** The command `uv run --no-sync rizzo download --runtime cpu --size 4b --quant q4_k_m` (it fetches the pinned llama.cpp prebuilt runtime from GitHub and about 2.6 GB of weights from Hugging Face, to be run later on this host) was refused on 2026-11-08 by the server-side auto-mode classifier. The reason given in the refusal was only that the classifier "judged this action dangerous (it gave no explanation)"; no more detailed motivation was returned and none is recoverable from the session. No alternative route (manual download, build from source, another runtime) was tried and the refusal is kept as recorded. It says what this session may do on this host without an explicit permission rule; it says nothing about the quality, safety or cost of Rizzo Flow. Reopening needs the operator, not new evidence.
* **Documented limits that matter for this use** (from its own README and model card, unverified here): abstention exists only in the native decision API, not in the Jev-compatible one; it answered confidently when evidence was missing in 6 of 36 fixtures (SemIf 1); probabilities are uncalibrated; the 4-bit file cost 4 points on one fixture set; accuracy is below Jev's published figure; its gold labels come from a teacher model. Cases N05 to N08 and N14 to N16 here are exactly the missing-evidence kind.
* **Fine-tuned against base weights** (planned for a small subset of missing-evidence cases): not run.

## Reopening conditions (any one)

1. The operator authorises, in writing, running the downloaded runtime and weights in an isolated directory (or builds from source) on this host; then run the 16 cases and the IT30 cases as arm D with the native API and abstention, and measure start-up, peak memory, latency and the effect on a battery running at the same time.
2. A forward test (decisions chosen before their outcome is known, on open questions) shows one real decision where arm A would have repeated work or overclaimed; then a cheap selector has something to improve.
3. A free GPU becomes available; this changes the cost side only.

## What to keep in the repository

Only this folder: cases, scorer, pre-registration, results. Nothing integrated into a flow. Remove by deleting the folder; no other file refers to it except the roadmap row, if the Orchestrator adds one.

## Reproduce

`python3 build_cases.py` (rewrites the two case files; hashes in `PRE_REGISTRATION.md`), `python3 arms.py rule`, `python3 arms.py score results/arm_C.tsv`. Reversed arms: add `--reverse`. Prompts for the model arms: `python3 arms.py prompt A|C|V [--reverse]`.

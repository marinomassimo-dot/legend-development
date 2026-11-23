---
record_type: HARNESS_SCOUT
week: 2026-W48
author: plan
handoff_to: plan
status: TRIAGED
triaged: 2026-11-23
---

# Harness scout — 2026-W48

Run by Harness Engineering (`plan`) on 2026-11-23 at ADV's tick (`SCOUT_DUE`), zero spend, one pass of about one hour. Sources: GitHub search API (repositories pushed after 2026-11-16, 12 query phrases of the skill, several with no hit above 40 stars), Hugging Face model API (6 queries, sorted by last update), Europe PMC for the Nature portfolio (two journals only). Read for each row: the repository or card page and its README head, stars, last push, licence field. No install, no run, no key, no account, no contact.

| # | candidate | source (URL) | what it adds to LEGEND | integration cost (h) | license | risk | proposed verdict | HE verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | Ratel: reads an agent's traces and reports what it gets wrong (self-corrections, health signals, tool use) | https://github.com/ratel-ai/ratel | A pattern next to `session_self_evaluation.md` and `session_model_census.py`: failures read from traces, not recalled. It is a service (Docker, Postgres, OTLP ingest), so only the pattern is usable | 2 to read; 20 or more to run | MIT (README badge also names Apache-2.0) | A service and a database to keep; session traces carry operator and case-adjacent text, so privacy rules out ingesting ours; 38 open issues | WATCH | WATCH |
| 2 | Scholar RAG Agent: blind screening by several reviewers under pseudonymous labels, frozen evidence, saved-run inspection | https://github.com/Francis1998/scholar-rag-agent | The blind-screening and frozen-evidence ideas match the blind verifier and receipt practice already in use; nothing new to import | 3 to read | Apache-2.0 per README; the GitHub licence field reads NOASSERTION | Licence not machine-confirmed; default model adapter is a fake, so no evaluation shown | WATCH | WATCH |
| 3 | claude-router: a Claude Code Mod that picks model and effort for each main turn | https://github.com/alexei-led/claude-router | Cost per turn (delegation_budget.md concerns). It would change the model or effort under us | 2 | MIT | Our windows are pinned and their effort is read back as high; a router that rewrites it breaks that check and the delegation budget; classifier trust unknown | REJECT for operating windows; WATCH for read-only jobs | REJECT |
| 4 | Deepdive: a 13-phase research skill with a decision spec ("what you will do with the answer") before searching, parallel sub-agents, an adversarial pass | https://github.com/Socialpranker/deepdive | The decision-spec step is the same idea as our pre-registration with a stated expectation and fixed exits; the pipeline overlaps `legend-deepdive` | 1 to read | MIT | Overlap; fixed-phase pipelines add ceremony (principles 1 and 3) | WATCH | WATCH |
| 5 | AI-Scientist v3 (Sakana): coding agents run experiments, baselines, ablations and a sealed final evaluation under one run directory | https://github.com/SakanaAI/AI-Scientist-v3 | The sealed final evaluation stage is what ADV-175 just did by hand (key held by a custodian, scorer frozen before scores); no new mechanism | 2 to read | Apache-2.0 | Agents run with full tool permissions and paid keys; the README itself warns to keep them in a container | REJECT as a runtime; the pattern is already used | REJECT |
| 6 | ToolUniverse, default branch head `df5ee941a89c` (carried from W41 to W47 as WATCH) | https://github.com/mims-harvard/ToolUniverse | Thirteen commits since 2026-11-16: Health Canada product catalogue and PubMLST tools, SpecStream search backend, contract fixes; no release after v1.5.10 | 0 | Apache-2.0 | None of the additions is target, exposure or efficacy evidence | WATCH | WATCH |
| 7 | SpliceAI2 (Illumina, Hugging Face) | https://huggingface.co/illumina-ai/SpliceAI2 | A splice predictor relevant to the ASO and splice-allele skills; the files are gated behind a login and the licence field reads other | 0 until access exists | other | Gated: a route result, not to be bypassed; no account or key is used | WATCH | WATCH |
| 8 | quorumbio biomedical NER models (gene, chemical, disease, species), updated 2026-11-23 | https://huggingface.co/quorumbio/biomedical-ner-gene-chemical-disease-species | Entity tagging for the PubMed census; the cards were not read, so no evaluation evidence is known | 3 to read | not read | A card with no evaluation is WATCH at best (skill rule) | WATCH | WATCH |

## Top 3 for this week
1. **Nothing to ADOPT or TRIAL this week.** No candidate answers a concrete need of the Scientists or of Harness Engineering that an existing tool does not already answer. Rows 4 and 5 describe in other words what the pre-registration step and the sealed scorer of ADV-175 already are.
2. **Row 1 is the one worth a re-check in a month,** only as a pattern: reading failures from the session traces already on disk with `session_model_census.py` and the correction log, without ingesting them anywhere. The need would be a repeated failure the census does not show; none is open today.
3. **Row 3 is a reject with a reason that will repeat:** anything that changes the pinned model or effort of an operating window conflicts with the read-back of effort that the launch briefs require.

## Watch-list carried forward
| candidate | first seen | why still WATCH |
|---|---|---|
| ToolUniverse | 2026-10-22 | no capability the adapters lack; reopening condition unchanged (a new capability, or a licence change) |
| TxGNN, Every Cure MATRIX scores | W41 to W47 | unchanged from the W47 triage; MATRIX licence still undeclared (REJECT use) |
| Rows 1, 2, 4, 7, 8 above | 2026-11-23 | pattern only, gated, or card unread |

## Looked at and rejected (one line each)
- Agent-framework and general harness repositories at the top of the "agent harness" and "claude code skill" searches (deer-flow, LibreChat, SoduWork, agentic-awesome-skills and similar) — general-purpose runtimes or skill catalogues with no scientific-evidence or provenance claim; a runtime to adopt, not a pattern (principle on runtimes).
- Awesome-list repositories — reading lists, no code to adopt.
- Nature portfolio — the Europe PMC pass found only two Scientific Data data descriptors (a wheat genome and a topographic index), none relevant; Nature Methods, Nature Machine Intelligence, Nature Biotechnology and Nature Communications were not searched this week.

Limits: one pass, no row reproduced, five rows rest on a README head and the repository metadata, the Nature part is incomplete and says so, licences were taken from the repository field and README without opening a licence file. The weekly scout has no schedule of its own: it ran because ADV's hourly tick relayed `SCOUT_DUE`.

## Handoff
No ADOPT or TRIAL, so nothing to implement. ADV: row 1 and row 7 are the only leads, both WATCH, neither consumed by any open item.

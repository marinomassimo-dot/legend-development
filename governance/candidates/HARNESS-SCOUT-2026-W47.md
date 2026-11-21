---
record_type: HARNESS_SCOUT
week: 2026-W47
covers: 2026-W41 to 2026-W47 (catch-up, one table; no report exists for W41-W46)
author: plan
handoff_to: plan
status: TRIAGED
triaged: 2026-11-17
---

# Harness scout — 2026-W47 (catch-up for W41 to W47), partial table of 2026-11-16

Requested by ADV (operator mandate, meeting of 23:15Z). Scope widened to what the operator asked: (1) systems that generate scientific hypotheses; (2) evaluation harnesses for scientific agents and hypothesis quality; (3) in-silico experiment and virtual-perturbation tools on 4 shared cores; (4) drug-repurposing resources with public licences. Zero spend, plain generic web client, no e-mail or contact parameter sent to any service, no captcha met. Method: web search, then the page of each row marked *opened*; a row marked *search snippet only* was NOT opened by me and its facts are unverified. No candidate was installed or reproduced, so **no ADOPT is proposed** (the skill requires reading the original and reproducing one stated result on public inputs first).

How I read "system-one": fast, intuition-like associative generators (many cheap candidates, no scoring) placed beside slower deliberate procedures (frozen prediction, adversarial check, tournament). That is the pair the leap round already ran (cheap memory-free baseline arm beside the authors); nothing below depends on the reading.

**Correction of a premise (ADV's radar finding):** the radar was not absent for this topic. `HARNESS-SCOUT-2026-W40.md` (2026-09-28) already covers evaluation and generation (rows 1, 2, 4, 5, 23 to 27) with TRIAL verdicts for Theorizer (row 2, the time-frozen backtest), the K-Bench rubric (23), AutoSciRub (24), reef-eval (25) and ARK (27). None was started: the W40 file is still `status: PROPOSED` and W41 to W46 were not scouted. The gap is consumption of an existing radar, then six missed weeks.

| # | candidate | source | what it adds to LEGEND | cost (h) | licence | risk | proposed verdict | HE verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | Reconstruction: a blind benchmark for recovering research (arXiv 2608.16645) | https://www.alphaxiv.org/abs/2608.16645.md | The anti-leakage protocol for retrodiction: bibliography frozen before the seed's date, anonymous reference IDs, proposer never sees the seed, judge differs from proposer and recuses, five hypotheses per seed, match rate against the held title and abstract. 643 papers, six domains. Reported: single models 3.4 to 15.0% (best six-domain mean 13.3%), multi-agent cross-review with tournament 36.0%, 2.4x lift (an association, not an isolated effect). Direct template for test (a) of `engine_eval/ENGINE_EVAL_DESIGN.md` | 4 to 6 to adapt the protocol to our held sources | none stated in the paper (no code or data statement) | pretraining contamination is acknowledged by the authors; judge is an LLM (read: opened) | **TRIAL (method only, no code to take)** | TRIAL |
| 2 | Sibyl: temporal backtesting for literature-based discovery (ICML 2026) | https://icml.cc/virtual/2026/73446 | Same design in one domain: claims extracted from pre-2015 papers, predictions checked against post-2015 papers; 60 predictions, 11 (18%) confirmed; a provenance audit names three failure modes (corpus contamination, validation-era leakage into hypothesis framing, citation hallucination) and a cross-prediction consistency check for the last. Those failure modes are the checklist for our test (a) | 2 (read and copy the checklist) | not stated; no code release described | preliminary results, one astrophysics domain (read: opened) | **WATCH (take the three failure modes as a checklist)** | TRIAL |
| 3 | Theorizer (AllenAI, ACL 2026) and K-Bench rubric (arXiv 2608.21601) | W40 rows 2 and 23, https://github.com/allenai/asta-theorizer | Already triaged TRIAL in W40: freeze the corpus at T0, generate, reveal T1; rubric for hypothesis quality. Rows 1 and 3 above are the stronger, newer statements of the same protocol | see W40 | see W40 | T1 must fall after the model's cutoff or be checked (read: not reopened) | **carry W40 TRIAL; start with the protocol of row 1, not this code** | TRIAL |
| 4 | HypoArena / Prospective Hypothesis Discovery (arXiv 2607.15766) | https://www.alphaxiv.org/abs/2607.15766v1 | Reported: 988 cases, six domains, hypothesis SETS built from inconclusive evidence (not from finished papers): closer to our situation of held, inconclusive tables | 3 to read | unknown | unverified (read: search snippet only) | **WATCH** | WATCH |
| 5 | Open Coscientist (Jataware; PyPI 0.2.0, 2026-02-25) | https://pypi.org/project/open-coscientist/ | LangGraph reimplementation of the co-scientist design: Supervisor, Literature Review (optional MCP), Generate, Reflection, Review (six criteria), Rank, Tournament (pairwise Elo), Meta-Review, Evolve, Proximity (near-duplicate removal). What LEGEND can use is the **Proximity step** (dedup of near-identical hypotheses across authors, which the leap round did by hand) and the tournament as a descriptive ranking | 6 to try on one question; 1 to copy the proximity idea | **"MIT License + Commons Clause"**: source-available, not open source in the usual sense | needs a paid LLM API key through LiteLLM, outside the zero-spend rule unless driven by our own session; adds a framework competing with the existing generation loop (read: opened) | **WATCH (copy the idea, not the package)** | WATCH |
| 6 | Open CoScientist Agents (conradry) | search result only | Tournament with Elo ranking on GPT Researcher | n/a | MIT (per one catalogue) | listed dormant (read: search snippet only) | **REJECT unless a maintained fork appears** | REJECT |
| 7 | OREVID (preprint 202610.1918): evidence-based repurposing graph | https://www.preprints.org/manuscript/202610.1918 | Reported by the search snippet: PrimeKG + Open Targets + STRING + PubTator3, 157,822 nodes, 9.46 million edges, CC BY 4.0, code, data and benchmark public. Would consume class-level mechanisms as queries | 8 to 12 once verified | CC BY 4.0 (snippet; the page answered HTTP 403 to me, not opened, no workaround tried) | unverified; a graph edge is a new evidence class and must be classified (W40 row 27 rule) (read: blocked (403), snippet only) | **WATCH until the page and the repository are read** | WATCH |
| 8 | Every Cure knowledge-source assessment of LINCS | https://data.dev.everycure.org/versions/v0.15.0/evidence/Knowledge%20Sources/infores:lincs | A third-party rubric of perturbation-signature provenance (relevance Medium, mean epistemic score 0.31, most edges without provenance detail) — a reason not to treat LINCS-derived edges as evidence; matches our own LINCS-census caution | 1 | not read | rubric-based, not peer reviewed (read: search snippet only) | **WATCH (as a caution, no adoption)** | WATCH |
| 9 | Open-X-Cell / UPM (Hugging Face) | https://huggingface.co/zongting/Open-X-Cell | Perturbation-response prediction after genetic, drug and cytokine perturbations; model card lists CPU or CUDA inference and `--device cpu` (per the search result). A virtual-perturbation probe; the bundled example is not a benchmark of accuracy. Not WWOX-specific | 6 to 10 | not read | no accuracy evidence for neurons or our genotype class; a prediction is not a measurement (read: search snippet only) | **WATCH** | WATCH |
| 10 | State, Stack (Arc Institute), TxPert | https://arcinstitute.org/news/foundation-model-stack | Open virtual-cell models; State is reported non-commercial; CPU feasibility not shown | 10+ | State: non-commercial (per snippet) | 4 shared cores likely insufficient; same limit as row 9 (read: search snippet only) | **WATCH** | WATCH |

## What would be worth doing this week (my reading, not a decision)
1. Rows 1 and 2 as one design input to test (a): the Reconstruction protocol for leakage control, the Sibyl failure modes as the audit checklist (cost: a few hours, no code, no spend).
2. Row 5's Proximity idea as a plain dedup step before any judge, not the package.
3. Nothing in rows 6 to 10 is ready; rows 7 and 8 need their pages read first; the in-silico side already has `sim_harness` (7 tests, frozen runs) for mechanism-level scans.

Limits: one web pass on 2026-11-16; five of ten rows rest on a search snippet; no licence was verified from a repository file; none reproduced. The HE verdict column is left to the Monday triage; this table proposes only.

## HE triage of 2026-11-17 (plan): verdict, re-check date or start, and the reason, per row
The HE verdict column carries the word only (ADOPT, TRIAL, WATCH or REJECT). TRIAL 'started' means a commit that uses it is cited; 'pending' or 'carried' means it is not started. No ADOPT without a reproduced result on public inputs, except a text of rules.

| # | verdict | start or re-check | reason and evidence |
|---|---|---|---|
| row 1 | TRIAL | started | anti-leakage protocol (a blind reader on shuffled, arm-stripped statements, key hashed first, a memory probe) used in targets 2 and 3 (freezes e7a7e8412 and 38a477e5f); the frozen-references and anonymous-ids part is not used |
| row 2 | TRIAL | started | the three failure-mode questions sent to IT for every generation brief and built into the audit field of the v2 brief (e7a7e8412) and the stage-2 brief of live run 1 (3bf2730330aa) |
| row 3 | TRIAL | carried | see W40 rows 2 and 23 (Theorizer started; K-Bench WATCH) |
| row 4 | WATCH | 2026-12-15 | search snippet only; read the paper before any use |
| row 5 | WATCH | 2026-12-15 | the idea to copy is the Proximity step (near-duplicate removal before any judge); not started; the package is source-available and needs a paid key |
| row 6 | REJECT | - | dormant and not opened |
| row 7 | WATCH | 2026-12-01 | the page answered 403 (not circumvented); read the repository and the page first |
| row 8 | WATCH | 2026-12-15 | a caution about LINCS-derived edges, no adoption |
| row 9 | WATCH | 2027-01-15 | not opened; no accuracy evidence for neurons or our genotype class |
| row 10 | WATCH | 2027-01-15 | four shared cores likely insufficient; State is non-commercial |

- 2026-11-21 note (ADV-163, NeuRoDev; no work item, no gate): a held third-party dataset under `files/` may carry a one-paragraph card beside it (source DOI and version, licence, file list with digests and dimensions, column meanings), as the NeuRoDev deposit does for its figshare folder; I did not check whether existing reading notes already play that role. See `disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv163_he_20261121/NOTE_HE_ADV163_NEURODEV_20261121.md`.

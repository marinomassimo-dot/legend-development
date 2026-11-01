# IT17 P2 - radar questions derived from the current priorities (2026-11-01)

Non-canonical research material; not medical advice; no efficacy claim. Tool: `framework/scripts/scout_daily.py` (tests: `framework/scripts/test_scout_daily.py`). No new scheduler, log or watchlist: the cron line, the pending log and `capability_scout_log.md` are the existing ones.

## What was missing

The radar resolved the remote-main SHA, but `parse_context_file` kept only dates, headings and repository names, so changing a priority from "catalogue" to "predictive evaluation" left its output unchanged, and `discover` took questions from a fixed seven-item theme list with a cursor. Reading the newest revision was not yet searching according to the work in progress. The followed list (6 teams / 18 repositories / 3 per team) only re-checked commits and releases of already known repositories; it did not look at what else a discovered team had published.

## Design (smallest path)

1. **A plan DERIVED, not kept.** `resolve_plan` reads, at the remote-main SHA and without touching a checkout, the surfaces that carry the current priorities: the latest `diagnosis_it*` README (rows with a stated validation gap; a bold "principal bottleneck" weighs more), `roadmap_current.md` (R1-R12 rows, "first" weighs more), `view/work_order.json` (each open need: question and what it would change), the latest `ORCH-ROADMAP-IT*` task record (open steps only, and only when the step text matches a search hook), the module README section marked CURRENT (its "Only planned / Next" sentences) and the package READMEs that section links (WATCH rows that state a reopen condition). Nothing is hand-maintained: edit a surface and the next run re-derives.
2. **Deterministic, no model call.** Query terms are the most frequent, then longest, non-generic words of one priority text (`key_terms`), plus a category anchor (for example "drug repurposing") so a lexical query stays inside biomedicine. A priority's terms depend only on its own text, so editing one priority never moves another question.
3. **Blob cache.** Each surface is stored with its git blob id and parsed items; an unchanged blob is neither fetched nor re-parsed (`cache: hit, reread 0` in the test). The plan records every input blob, the SHA and a digest of the questions. If the SHA cannot be verified, the cached plan is returned labelled `STALE`/`provisional`; a missing or unreadable surface and a freshness limit are listed as provisional reasons and shown in the briefing; with no plan at all the radar falls back to the old theme list and says so.
4. **Selection.** `pick_questions` orders by weight times days since asked (never asked counts as 30), so heavier priorities return sooner and a reworded question (its key includes a digest of its terms) is asked at once. The open slot is kept, so one search per day is still outside every priority.
5. **Readable chain.** Each question and each log entry carries "Why asked: surface, locator [path @ blob, main SHA]: priority text" and "If confirmed (decision)". Channels (GitHub, Hugging Face, Nature via Crossref, Europe PMC as complement) are unchanged, with `error` / `no_news` / `delta` kept apart, dedup of paper/code/data mirrors, versions and claim labels.
6. **Completed work stops generating.** A task step with status DONE, a WATCH row that is no longer WATCH or lost its reopen condition, and a work-order need that was removed produce no question (tests below).
7. **Teams: one bounded level.** After the daily search, at most 1 owner per run (the owner of a discovered GitHub repository or Hub asset, or a followed team), never one explored within 14 days, the longest-unexplored first, is examined through its public listing (GitHub `users/<owner>/repos`, or Hub models and datasets by `author`). Of that listing only forks-free, non-archived, recent entries not already known and not already shown that share one of the two leading terms of a current question are kept, at most 3 per team, each with the matching terms and the question that motivated it. No collaborator, follower or contributor is requested and results are not explored in turn. Discovery itself caps one owner at 2 items per run (the surplus stays unseen, not consumed), so a prolific team cannot fill the day. Limits are configuration (`explore`: `teams_per_run`, `repos_per_team`, `cooldown_days`, `max_per_owner`; `follow`: 6/18/3 and the weekly deep check unchanged). The followed list never gates discovery.
8. **Traceability.** A signal now records `via` (the question or team exploration that produced it); examination, trial and decision keep their evidence rules (a `record_file` or `test_run` ref must exist under the repository, a log line proves nothing).

## Tests (fixtures; controlled time)

`python3 -m unittest test_scout_daily` in `framework/scripts`: 54 tests (35 before this package, 19 new). Weekly logic runs on injected clocks and is **not** a multi-week observation.

| Proof | Test |
|---|---|
| 1 changing a relevant priority changes the questions when it should and not otherwise | `test_changing_a_relevant_priority_changes_the_question_and_only_that_one`, `test_an_irrelevant_edit_changes_nothing` (two blobs change, the question digest does not) |
| 2 a completed correction stops generating | `test_a_correction_marked_done_stops_generating`, `test_a_resolved_reopen_condition_or_removed_need_stops_generating`, `test_the_latest_record_wins_not_the_first` |
| 3 a full watchlist does not block new discoveries | `test_a_full_follow_list_does_not_block_new_discovery_or_exploration` (18 followed repositories) |
| 4 a prolific team does not monopolise | `test_a_prolific_team_does_not_monopolise_discovery_or_exploration`, `test_one_bounded_level_of_public_work_with_a_motive` (15 matching repositories, 3 listed, one listing call) |
| 5 signal to examination to trial to decision | `test_a_real_signal_reaches_a_traced_decision_with_evidence_that_exists` (a missing evidence file leaves the stage `claimed`; a deferral cannot be integrated) |

Mutation checks on this package's own code: ignoring the DONE state fails 2 tests; removing the per-owner cap fails the monopoly test.

## One bounded real run (2026-11-01, state in a scratch directory, no token, no e-mail)

Remote main resolved at `3e167e250fd6` (IT16 head); 7 surfaces read (roadmap, module README, work order, diagnosis `diagnosis_it16_20261101`, task record IT16, two linked package READMEs), 39 priority questions. The IT17 record is not on remote main yet, so no IT17 step generated a question (a limit of this run, not of the code). Two questions asked plus the open slot: `diagnosis:evaluation` (weight 4, the stated principal bottleneck) and `diagnosis:catalogue-and-identity`.

| Measure | Value |
|---|---|
| Requests | 59 (counted by the radar's own request counter; split not itemised); hosts: api.github.com 27, huggingface.co 17, www.ebi.ac.uk 5, api.crossref.org 3, others 1 each |
| Wall time | 84.5 s, of which 50.05 s is the known unreachable TxGNN explorer attempt and 14 s the declared pauses between questions |
| Error entries | 0; 6 non-200 answers counted (the TxGNN explorer, 4 from api.github.com, 2 from www.ebi.ac.uk) are status probes or release-less repositories and were not itemised |
| Channels | github delta (6 new), huggingface delta (6), nature delta (2), europepmc delta (3) |
| Team step | `aayambansal` (owner of a discovered repository): 19 listed, 17 without a shared term, 1 lead (`aayambansal/delphi-benchmark`, matched "evaluation"); not examined |
| Earlier runs | two development runs of the same code before the category anchor and the "do not offer today's own discovery as other work" fixes: about 59 requests each, state discarded |

Quality limit seen: lexical queries return noise. Of 18 items shown, most are off-topic (an astronomy dataset, equipment repositories); the query anchor reduced but did not remove this. The plan chooses the question; it does not judge the hit.

## One signal traced to a decision

Signal (run state, `via question:diagnosis:evaluation`): GitHub repository `dr-ronak/Ontology-Bridged-Drug-Repurposing-Multi-Agent-GraphRAG` (found 2026-11-01 for the question "without outcomes independent of the module no step can be called predictive"; origin: diagnosis row `Evaluation`, `diagnosis_it16_20261101/README.md` blob `e21ec10f05`, main `3e167e250fd6`).

Examination (public GitHub API, 6 requests, no clone, nothing executed): repository created and last pushed 2026-10-04, default-branch head `3ad867e8c182`, no release, 0 stars, size 127 kB. The README (797 lines) contains unresolved merge-conflict markers at lines 1, 691 and 797, which means two versions of the document were concatenated. It describes drug links derived from text matching of ChEBI definitions against Disease Ontology terms, labelled by the authors as hypotheses; "a regression fixture of known drug-disease pairs to track precision" is listed as future work (line 666), and `tests/test_smoke.py` is the only test file. The README states MIT (line 674) while the API reports no licence and the file tree has no LICENSE file.

Claim labels: declared, yes; implemented, code exists, never run; independently reproduced, no; verified by this session, metadata and README text only.

**Decision: DISCARD for this question (state `reject`).** It measures no outcome of any kind, so it cannot supply or replace the independent outcome set that the Evaluation row says is missing; the licence is not stated in a form that permits reuse of the code; its method (text matching to hypotheses) duplicates what the module already treats as hypothesis generation. Unknown is not negative: nothing here says the approach cannot work, only that this repository is not evidence for the decision. **Reopen if** a labelled drug-disease fixture with a reported precision and a LICENSE file appear.

Trace recorded with `scout_daily.py --trace` (signal `via` question, examination with a `source_read` ref and, once this file existed, a `record_file` ref, trial `not_needed`, decision `reject`). The first `record_file` attempt was refused because this file did not exist yet and stays visible as a `claimed` entry in the run state, which is the intended behaviour. The decision and its evidence are also in the entry appended to `capability_scout_log.md`. Not integrated: `integration` was not recorded because the decision is a rejection.

## What remains only planned

- The weekly follow cycle and the cooldown over several real weeks: only controlled-clock tests exist.
- Team exploration of a Hugging Face owner and of papers (Crossref author listing): the Hub path is unit-tested, not run live; papers are not implemented.
- IT17 task-record steps as questions on remote main: they appear once the record is pushed.
- Better terms: a deterministic text rule cannot judge relevance; a sharper query (phrases, controlled vocabulary) is a later, measured change.
- The other hits of the run (Nature "Drug repurposing in hereditary ataxia", metadata only, no abstract in Crossref; the Europe PMC and Hub items) remain TO_TRIAGE; unexamined is not negative.

## Verifier round 2 (changes after independent review)

- **Robustness.** Undecodable bytes no longer crash a run (the subprocess wrapper decodes with replacement; a surface that contained them is flagged provisional). A surface expected to yield items (roadmap, work order, diagnosis) that parses to zero is flagged `parsed 0 items`, also when served from the blob cache (warnings are stored with the blob). Wrong-shaped or damaged state (plan, extracts, asked-dates, explored) is dropped or ignored per key instead of crashing. Two headings marked CURRENT: the last wins and the ambiguity is a provisional reason.
- **Evidence for a trace.** `source_read` and `session_check` refs now need a URL or an existing repository path as first token, else the stage stays `claimed`.
- **Reopen conditions: known gap.** `parse_reopen` now also reads prose or heading lines such as "Reopen if ..." / "Reopens when ..." beside a README that names a WATCH decision. Run on this repository (HEAD `e684f334c9ab`), the two package READMEs linked from the CURRENT section yield **0 reopen questions**: neither states a reopen condition in a WATCH row or a "Reopen if/when" line. The code path is tested on fixtures only; on the real repository it is a known gap, not a working source.
- **Plan counts at HEAD:** 34 questions (work order 15, roadmap 11, diagnosis 8), 7 priorities skipped as internal or without a usable term, no provisional reason.
- **Query quality.** Anchor per category ("drug repurposing", "pharmacology", "compound database", "perturbation signature", "biomedical"; "epilepsy" only when the text is neurological, never "neuronal"). Priorities about our own process (presentation, continuity, agent, autonomy, report, checkpoint, dashboard, scouting, verification) are not external questions unless the same text carries an explicit external hook (benchmark, evaluation, licence, dataset, pharmacology, ...). Search strings use plain alphabetic words of 4-14 letters, never hyphenated or rare tokens; Europe PMC gets at most 2 ANDed terms. A team lead must share a DOMAIN term (generic words such as agent, evaluation, independent, model are excluded); a question with no domain term triggers no team exploration (this is the case for the Evaluation row today).
- **By design.** A priority that was delivered but is not yet reflected in the diagnosis table (or roadmap, work order) keeps generating questions: those surfaces are the source of truth, and the radar does not infer completion from other records. Only a DONE task step, a removed need or a resolved WATCH condition stops one.

Ten live-plan queries (offline, derived from HEAD objects; GitHub / Hub / Nature keywords / Europe PMC):

| Question | GitHub | Hub | Nature keywords | Europe PMC |
|---|---|---|---|---|
| diagnosis:evaluation | drug repurposing independent | benchmark | drug repurposing independent evaluation predictive outcomes | "drug repurposing" AND independent |
| diagnosis:catalogue-and-identity | biomedical identity | catalogue | biomedical identity catalogue source turned | biomedical AND identity |
| diagnosis:compound-target-action | compound database independent | compound | compound database independent direction | "compound database" AND independent |
| diagnosis:contexts | biomedical separated | separated | biomedical separated contexts | biomedical AND separated |
| diagnosis:hypothesis-generation | drug repurposing generation | benchmark | drug repurposing generation hypothesis outcome | "drug repurposing" AND generation |
| diagnosis:networks-and-models | biomedical contrast | contrast | biomedical contrast networks models | biomedical AND contrast |
| diagnosis:perturbations | perturbation signature perturbations | perturbation | perturbation signature perturbations independent contrast lincs | "perturbation signature" AND perturbations |
| diagnosis:quantitative-pharmacology | pharmacology descriptions | bioactivity | pharmacology descriptions pharmacology quantitative accuracy | pharmacology AND descriptions |
| work_order:NEED-EXCITATORY-GAIN | epilepsy attributed | attributed | epilepsy attributed permissive magnesium bursting | epilepsy AND attributed |
| work_order:NEED-GSK3B-DEREPRESSION | drug repurposing class | benchmark | drug repurposing class inhibition readout | "drug repurposing" AND class |

Honest reading: the evaluation, pharmacology, compound and perturbation queries are usable; the "biomedical X" and "epilepsy attributed" ones are weak because a lexical rule picks the most frequent words of a sentence, not its subject. The plan decides which priority is asked; it does not make the query precise. The real-run numbers above predate these changes.

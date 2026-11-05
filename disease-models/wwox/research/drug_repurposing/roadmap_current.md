# Drug repurposing — current development roadmap

Updated 2026-11-01 by `orchestrator`, runtime Codex, following the operator's requests to
consolidate the Unravel/BioNAV/rareSHIFT and ALS discussion, state the guiding principle
explicitly and define balanced, priority-driven external discovery in this roadmap.

**Planning, not an implementation or efficacy report.** This is the home of the next
increments. The newest measured iteration in [README.md](README.md) describes what actually
works. The [operator-supplied v4/r14](roadmap_v4_r14_20261020.md) stays verbatim as historical
provenance. Before executing an increment, fetch remote `main`, reconcile the latest measured
iteration and reuse any work already delivered. This update authorises recording the plan;
it does not claim that its research experiments, deployments or integrations have run.

## Guiding principle

> **Rendere durevole la capacità di lavorare e migliorarsi, mantenendo semplice cambiare direzione.**

Keep improvements lean, flexible, modular and reversible. Reuse existing mechanisms;
keep tools, plugins, scripts and patterns easy to adopt, replace or remove. Preserve
reusable guidance at its canonical home, without duplicating prompts in role contracts
or adding rigid gates and approval layers.

## Research objectives

Keep both broad, durable functional recovery and useful partial benefit open, including
drugs, supplements and dietary interventions where a biological rationale warrants study.
Genotype/lesion dependence and depth of benefit are separate dimensions. Gene replacement
belongs in broad-recovery comparisons; increasing protein abundance or normalising an RNA
profile alone does not establish restored function or complete recovery.

Combine two complementary inputs: qualified WWOX experiments and mechanisms, and external
perturbation data/methods that can suggest previously unlisted interventions. Evidence from
another disease is a methodological or mechanistic precedent until transfer to WWOX is
tested. Predicted effect, observed effect and priority for the next research action stay
distinct. A low model rank alone establishes neither inefficacy nor harm.

## Work order

Each row is an independently useful increment, normally sized for hours. Reorder when
evidence changes. Reuse the module's catalogue, adapters, cards, needs, join, handoff and
view; no new harness, agent role, general platform or approval layer is proposed.

| ID / priority | Increment and reuse | Concrete output | Useful completion criterion |
|---|---|---|---|
| R1 / first | **Biological context and typed networks.** Extend existing needs/cards only where a decisive context is missing. | A small WWOX subnetwork with stable identities, direction or UNKNOWN, measured/inferred/hypothesised edges, genotype, species, tissue/cell type, developmental stage, endpoint and timepoint. | Trace each consequential edge to its source; preserve discordant contexts and distinguish baseline disease changes, wild-type effects and rescue. |
| R2 / first | **Computationally usable compound catalogue.** Reuse identity reconciliation and quantitative pharmacology. | Bidirectional need/pathway-to-compound and compound-to-need exploration; a census of compounds usable by each proposed method. | Separate source rows, compound families, usable perturbation profiles and actually evaluated candidates. Annotate action, assay, dose/time, selectivity, exposure/BBB and relevant safety evidence or missingness. Access categories carry jurisdiction, source and date; diets remain complex interventions. |
| R3 / first | **Small network-prediction comparison.** Reuse available transcriptomics and LINCS work. | One reproducible comparison of a simple reference method, existing signature reversal where usable, and one lightweight network method, using equivalent inputs and a declared compound subset. | Establish added information, a precise data limit, or no advantage using the comparison below. No full-catalogue screening claim for an untested subset. |
| R4 / next | **Context differences and subgroup hypotheses.** Start with existing cross-system analyses. | A concordance/discordance view and explicit hypotheses about residual function, lesion class, tissue or intervention window. | Distinguish missing data from disagreement. Grouping must survive appropriate resampling or independent data; otherwise retain a descriptive hypothesis. No patient response labels inferred from model clusters. |
| R5 / next | **Pharmacological comparison in both research objectives.** Reuse candidate cards and potency work. | A small comparison including broad-recovery and partial-benefit hypotheses, with desired and potentially opposed endpoint effects, exposure limitations and alternatives. | Separate research priority, model ranking and observed evidence. Preserve endpoint-specific nulls/negatives; do not combine opposing effects into a reassuring net score. |
| R6 / next | **Close the research loop.** Reuse Scientist outputs, evidence tables and the existing handoff. | One new-study or new-result case passing through observation, inference, hypothesis, biological need, compound search, comparison and next experiment into the regenerated research queue. | Demonstrate regeneration with a positive, null or negative result, or justified abstention. A literature note or push alone does not close the case; canonical changes use the existing scientific workflow. |
| R7 / next | **Dynamic follow-up.** Add to existing records only when repeat observations exist. | A before/after or time-course comparison recording baseline, intervention, exposure, context and endpoint; revised card and queue position. | Distinguish treatment-associated change, natural history and confounding. No patient-data collection programme or patient-specific treatment system is introduced by this roadmap. |
| R8 / alongside | **Human WWOX RNA opportunity.** Reuse the Foundation–Unravel lead already in the scout register. | Monitor public protocol, accession, matrices, sample/control metadata and reuse terms. | Use a suitable released asset, or record the missing asset and reopening trigger. Other work continues; no assumption that peripheral RNA represents neural rescue. |
| R9 / alongside | **Continuous discovery and selective adoption.** Reuse the daily scout and existing capability log. | Relevant deltas, small capability comparisons and documented keep/remove decisions. | Show which WWOX question improves, incremental yield against existing tools, provenance/licence, runtime/storage/token cost and removal path. No adoption quota. |
| R10 / next | **Physician-facing research interface.** Extend the existing view and shareable export. | Internet-accessible presentation with pathways, compounds, explained priorities, context comparison, evidence chains and printable summaries. | A reader can identify the research question, rationale, counter-evidence, uncertainty and next useful experiment; counts reproduce the underlying data. A local preview is an intermediate output, not delivery. |
| R11 / alongside | **Shareability and attribution.** Reuse source notices, shareable audit and licence reconciliation. | Resolve redistribution for the presentation and the whole development repository, including historical material; preserve acknowledgements. | Check code, data, model weights, services and figures separately. Isolate uncertain material and prepare concrete alternatives; no silent history rewrite, deletion of uncertain unique evidence or declaration of complete clearance without an audit. |
| R12 / maintain | **Operational continuity.** Reuse the daily scout and hourly mandate monitor. | Verify actual scheduled execution, stalled versus live jobs, restart behaviour and visibility of failures. | Reuse the existing scheduler and mandate queue; no duplicate automation or agent. Stay quiet on unchanged/non-actionable state; notify on meaningful failure, completion or required action. |

## First predictive experiment: bounded and reversible

Choose the smallest question for which an interpretable comparison is possible. Inspect
available samples, biological replicates, perturbation contexts and applicable reuse terms
before selecting the method. A curated signed subnetwork can be a first trial; it is not
labelled a validated causal model or a patient molecular twin.

- Fix the biological question, reference state, candidate universe, comparison methods,
  evaluation measures and resource budget before examining the evaluation results. Use
  existing analysis conventions and files; do not create a benchmark framework.
- Keep the same usable inputs across conditions. Compare an external-only condition with
  a WWOX-informed condition when testing the value of local knowledge, without exposing
  held-out answers through the curated network or cards.
- Retain cell type, concentration, time and signature identity. Include appropriate
  matched/randomised controls, frequent-hitter checks and sensitivity to network structure;
  do not repeat a known LINCS confound as new evidence.
- Prefer an independent biological contrast or dataset for evaluation. Multiple samples
  from one subject or library are not independent patients. If independence or replication
  is insufficient, label the result exploratory and name the missing comparison.
- Preserve inputs, versions, configuration, outputs, costs and counter-evidence. Return
  added value, no added value, or inconclusive with a reopening condition. Model robustness
  and recovery of known examples do not establish prospective clinical accuracy.

Use public, appropriately licensed data and existing lightweight computation first. A
free academic access request is not a redistribution licence. NeMoCAD/BioNAV is an external
methodological reference, not an assumed installable dependency. ToolUniverse is tried on a
capability the adapters lack; LINCS, TxGNN and MATRIX retain their existing measured limits
until new evidence, availability or terms justify reopening them.

## Presentation and comparison

Build the selection funnel from measured units: **catalogued → computationally usable →
actually evaluated → mechanistically pertinent → ready for a named next test**. Show unknown
and excluded counts with reasons. Distinguish model percentile, research priority and
calibrated clinical probability; do not display the last without supporting validation.

The pathway view links a need to an intervention through typed evidence. State whether
"coverage" means a target association, a directional prediction or an observed effect,
show overlap and the denominator, and keep unknowns visible. A pathway-coverage percentage
is not a percentage of disease treated. Compare adverse or opposed signals separately from
beneficial hypotheses; broader pathway engagement is not automatically better.

Use the current static view, filters, comparisons and exports before adding infrastructure.
Prepare the public deployment from the distributable package, with a reproducible build and
rollback. Respect existing publication authority and any operator approval already granted;
prepare the reviewable deployment before requesting only a genuinely missing reserved
decision. Keep private communications and individual-level information out of public outputs.

## Daily discovery and bounded follow-up

**Target behaviour, not a claim that the current radar implements every item below.**
Reuse the existing radar, scheduler, scout log and roadmap; verify delivered behaviour
against these requirements before reporting it as operational.

At each run, resolve and record the latest remote `main` SHA of `legend-development`.
Read the relevant state, latest measured iteration, task diagnosis, roadmap, integrations,
code and tests at that revision, without switching or modifying an active worktree.
Cache unchanged inputs by revision rather than rereading the whole repository. An old
"current" heading is not authoritative over later verified work. If freshness cannot be
verified, disclose it rather than silently treating cached context as current.

Choose two or three priority questions from actual work, failures, missing inputs and
opportunities: what decision would change if a finding were confirmed? Reconcile previous
proposals and open tasks first; completed work is not a new assignment. Keep both searches:

1. **Scientific needs:** WWOX and mechanism-specific questions, including pathways,
   metabolism, stress, excitability, glia and assays even when WWOX is never mentioned.
2. **Capabilities and benchmarks:** daily new discovery across **GitHub, Hugging Face and
   Nature**, for tools, compound databases, predictive methods, matching, evaluation and
   useful Scientist/Orchestrator patterns. These are three explicit discovery channels,
   not merely probes of known resources. Do not require WWOX as a keyword. Other primary
   literature, official project sites and preprints complement them. Distinguish primary
   research, commentary, promotional claims, preprints and corrections; prestige is not
   evidence of performance or benefit.

For an important project, inspect its public team/organisation's other relevant work.
Use a weekly follow-up by default, while keeping new discovery daily. Starting adjustable
limits: **6 active teams and 18 active repositories across the follow-up list, at most 3
repositories per team**. Do not fill slots for their own sake. Rotate or pause entries when
their relevance falls or a better opportunity appears; preserve sources and reopening
conditions. Most discovery effort remains available for new projects. Reuse one scheduler;
cheap version/availability probes of operational data sources remain distinct from team
exploration. Following means internal monitoring, not social-account actions or contact.

Before making a recommendation, inspect the external repository's latest default-branch
commit and relevant code/tests, recording its SHA and release separately. For Hub assets,
record the revision, card and actual files; for papers, the version, corrections and
relevant supplementary material. Deduplicate a project's paper, code, data and mirrors.
Select a matching method using the existing [matching guidance](matching_guidance_v3.md),
not a mandatory graph or a count of pathways, hits or agreeing engines.

Keep IMPLEMENTED, PARTIAL, PLANNED, MISSING and UNKNOWN scoped to evidence: author-declared
tests, inspected code, generated artefacts, independently reproduced results and checks
actually run are different observations. Seek counter-evidence, leakage, shared origins,
missing controls and context limits. A missing result is distinct from a failed or partial
query. Preserve the research objectives and evidence boundaries above.

Report material deltas: source/team, version/date, verified fact and limit, priority question,
decision affected, proposed use, smallest reversible trial and decisive cost/licence terms.
Keep at most one leading action in the daily brief; other useful signals stay in the log.
No useful change is a valid one-line outcome. Record findings in the existing scout log and
update this roadmap only when a decision changes; claim persistence only after a successful
write and preserve concurrent edits. A proposal or adoption into the plan is not a verified
implementation. Keep sightings, examination, trials and decisions traceable through the
existing records, without another register.

The scheduled scout researches and stages findings; authorised operational sessions perform
runtime trials, integrations and scientific updates. Install or retain a tool when its
measured gain pays for its dependencies and cost; remove duplicative components. No external
code execution or installation is implied by a discovery. External spend remains zero, with
no account creation, email contact or private-data transfer implied. Check code, data,
weights and service terms separately and retain attribution. Monitor Unravel for public
methods/data, not repeated promotional counts.

## Standing method

Reusable guidance for any drug-repurposing package lives in these places only; roles and briefs point here and do not copy it.

- Generic engine rules (retrieval, cache, coverage states, imported documents, tool kinds, graded comparisons, suite outcomes): [`repurposing_adapter_convention.md`](../../../../framework/protocols/repurposing_adapter_convention.md).
- Matching method: the operator's [matching guidance v3](matching_guidance_v3.md). Pick the method that fits the question; no method is imposed on every question.
- Autonomy, handoff and stopping: [cross-session transport section 12](../../../../framework/protocols/cross_session_transport.md#12--autonomous-mandate-continuity).
- Reading receipts and complete reads: [`fulltext_read_receipt.md`](../../../../framework/protocols/fulltext_read_receipt.md).
- WWOX-specific knowledge stays in the module records (needs, cards, working model), not in these generic pages.
- Before freezing a candidate for the release battery, run `python3 framework/scripts/candidate_tree_freshness.py --candidate HEAD --base main` (or land through `task_close.py`): measured on the IT16 candidate, it reports exactly the three surfaces that failed the first battery (coverage report, reading state, pathograph) as STALE after a new receipt; the failure came from bypassing that existing path, not from a missing check.
- Binding to the monitor (IT19): the `MANDATE_BOUND: <TASK_ID>` line must start a line of the session's own persisted text, in the first message of the mandate, and must then be verified: `python3 framework/scripts/mandate_watch.py check --task <TASK_ID> --deliver none --json` has to return this session's id (IT18: no line was written at the start, and a later line sat in a narration message that is absent from the transcript, so ten hourly checks said UNKNOWN). Reviving a dead session from cron (`claude --bg --resume`) additionally needs the CLI workspace trust of the repository directory, which `claude --bg` refuses without ("Workspace not trusted", reproduced 2026-11-02 from the root and from a worktree); the failed delivery and its reason are now logged by the watch.
- **Two orders, never one (IT20 P5, 2026-11-02).** The module keeps two separate orderings and neither is derived from the
  other. The *group view* (`ranking_it8.py`, G1…GU) orders depth of evaluation and answers "what has been shown". The
  *investigations view* (`ranking.json` key `investigations`, `investigations.tsv`) orders **research investment** — the
  value of the next discriminating test given its cost and what its result would change — and answers "what should be
  funded next". It is published under one plain sentence, *ordine delle indagini da finanziare, non classifica di
  efficacia*, because a numbered public list is otherwise read as a recommendation. Consequences that bind any package
  touching it: evidence depth is displayed beside every row and is never a gate, so a unit that is GU in the group view
  may top the investigations view when its missing premise is cheap and decisive; an unresolved or opposed need direction
  is named in the row's own decisive-uncertainty field and the position never implies a direction the evidence does not
  carry; a `novelty_perimeter` records what was actually queried and may not say that something was never studied; no dose,
  route, schedule or preparation may enter the table; and `origin_class` (`known_in_wwox`, `generated_by_legend`,
  `external_transferred`) is provenance only, never a bonus or a penalty. The generator enforces all of this and refuses a
  row that breaks it.
- **A qualified search filters; it does not generate (IT20 P5, measured).** Compared at equal usable universe, the
  WWOX-qualified selection was a strict subset of a plain external target-list selection, and reached 3 of 23 needs (the reach of the qualified-selection path, not a count of resolved directions: of the other
  20, 10 have an unresolved direction, 6 abstain at three later guards (`action_not_stated`, `coupling_not_measured`, `no_coupling_row`; `consistency()` already maps `restore` to `up`, so there is no vocabulary gap: `followup_it20_20261102/`) and 4 have no catalogue association;
  the generator proposes on conditional roles and is not bounded by it): the
  binding constraint is that a lever can be qualified only on a need whose direction is resolved and whose coupling is
  stated. Before asking a package for new candidates, check how many needs can qualify one at all — a protein-level
  measurement that resolves a need's direction unlocks more of the catalogue than any compound search does. Measurement and
  method in [`hypotheses_it20_20261102/README.md`](hypotheses_it20_20261102/README.md).
- **Generation is not the qualified filter, and WWOX identity is tested against decoys (IT21, measured).** The seed-graph
  generator was re-run on current inputs (IT19/IT20 guards withdrew 235 of 1,202 seed-specific rows; conflicting or
  glue-type actions carry no sign) and its output stays `CONDITIONAL_*` until a measurement resolves the role; nothing
  leaves that vocabulary by pipeline (`CLOSED_AS_WRITTEN` is a terminal state, never a promotion). Retrospective result:
  replacing the WWOX seed genes by degree- or reach-matched decoy genes yields about as many proposals (real count above the
  decoy 95th percentile in 0 of 5 sets), so **WWOX identity adds no demonstrable advantage on the properties measured (proposal count; membership against matched random seed sets)** (IT22: this is not the general conclusion that WWOX adds no value; network interactions, cell-type-specific contrasts and role premises were not measured); the independent
  routes that did produce a distinct conditional question were compound-first (Path B) and role-resolving probes. Two
  pitfalls to carry: (1) an edge of the signed network can be contradicted by the references it cites; screen each chain
  edge against its own references' abstracts before spending a qualification (`generation_it21_p2_20261103/
  edge_ref_sign_screen_it21.py`; a prompt for human reading, validated precision 0.50 and not held out); (2) "new" is
  relative to a perimeter that must include earlier exclusions and candidate lists, not only cards (P8 caught five earlier
  threads presented as new). A partial `files/fulltext` corpus makes `audit-shareable` fail spuriously (every name looks
  unattested): never create it in a worktree to carry a receipt. Records: [`evaluation_it21_p5_20261103`](evaluation_it21_p5_20261103/README.md),
  [`verification_it21_p8_20261103`](verification_it21_p8_20261103/README.md).
- **Check that a hand-over uses what the repository already holds (IT21 V1, vorinostat retrospective).** Three links were missing and are now code
  (`generation_it21_p2_20261103/attribution_screen_it21.py`, tested): the measured affinity of a compound at the target its chain runs through (33 of
  224 assessed rows are 10-fold or more weaker there than at the compound's best target; a listed target can be the weakest one); the identity of a
  DGIdb-only twin read from the ligand id in the claim name (1,423 twins the catalogue never joined; stored catalogue unchanged, join applied at
  hand-over); and earlier qualification records as a decision source. `NAMED_ALREADY` on a lever means only that a card names the gene: read the
  card's state before calling a thread closed. Result and handoff list: [`diagnosis_it21_v1_20261103`](diagnosis_it21_v1_20261103/README.md).
- **A decision travels only as far as its reason; incomparable measures give no exclusion; knowledge added is not knowledge consumed (IT22, measured).**
  (1) An earlier decision on one molecule reaches another member of its mechanism cluster only inside the scope its own reason supports
  (`generation_it22_p1_20261103/decision_scope_it22.tsv`, function `decision_effect`): molecule-specific reasons stay with the molecule, a refuted premise closes the
  arm it belongs to, an unresolved premise travels as a carried limit, work already done lowers priority and says "not a discovery"; a decision with no recorded scope keeps
  the old veto under its own label. Selection diversification, work done and a negative scientific judgement are three different reasons and are labelled apart.
  (2) Potency is compared only between measures of the SAME type (IC50/EC50/Ki/Kd, compatible relation and assay class); otherwise the state is `NOT_COMPARABLE_MEASURES`
  with the values kept; a measured secondary action (100 to 1,000 nM) is kept with an on-target-control requirement; the nM conventions are stated with a sensitivity, never a law
  (`attribution_screen_it21.py`). (3) A new WWOX observation counts as used only when it is in the seed table (`build_inputs_it22.py` builds the amended inputs; `check_seeds.py` must PASS),
  reaches the engine (incremental `run_v4.py --seeds-dir --only`), and shows in the proposals (guards become carried limits; counts in `measure_it22.py`). A control that failed in a
  deposit (the shWWOX hNPC library did not show WWOX lower) is attached to every seed row of that deposit, by deposit, not by a list of ids. Cell-population facts are never gene seeds
  (guard `COMPOSITION_NOT_REGULATION`). (4) Reverse test: freeze the forward output, then reconstruct the favourable reasons blind, then classify each as consumed, represented-not-executed,
  executed-not-consumed, omission, justified exclusion, missing datum or representation limit; keep only fixes that also help a second case. Measured stage by stage
  ([`measures_it22.json`](generation_it22_p1_20261103/measures_it22.json)): the P1 and P2 corrections changed selection, not the 980 generated rows; only the new input (P3) added generated rows (20).
  Records: [`generation_it22_p1_20261103`](generation_it22_p1_20261103/README.md), [`diagnosis_it22_p6_20261103`](diagnosis_it22_p6_20261103/reverse/README.md).
- **Evaluate an external capability on a frozen case, by what it changes in the calculation (IT23).** Freeze the current method's input and output on contrasting cases first
  (`cases_it23_p1_20261103`); then ask of each capability: which unused knowledge enters, which proposal or comparison changes, why that is biologically pertinent, which premise could
  refute it, whether it works on a second case. Six capabilities were tried (EC-KG, NORDic, CANDO, dseqr/LINCS, module discovery, MolNexus): none was adopted as a tool; one relation type
  (adverse-event reports) became a carried limit, and the sign-discordance audit of the action table found five suspect rows. Rules that held: an unknown action never becomes an edge (NORDic's
  aggregator turns `?`/`binding` into activation, presence-only and contrasting signs into inhibition, and, with the file served today, TTD inhibitors into activation: reproduce a conversion
  on the CURRENT file before trusting it); a simulation whose benefit readout is defined per scenario returns the scenario, so report what varies with the intervention inside one scenario;
  a profile matrix that cannot score the hand-over families cannot change the selection (test coverage against the hand-over before saying "changed nothing"); an id-join claim must say
  how the id map was built (here, mostly by name); a table built from a neighbourhood extract is incomplete by construction and must say so. The independent verifier reopened the
  producers' own numbers (34 findings, 18 corrected): recompute headline figures from the raw file and test byte-determinism across `PYTHONHASHSEED`.
  Records: [`it23_result_20261103`](it23_result_20261103/README.md), [`verification_it23_20261103`](verification_it23_20261103/README.md).
- Provenance through intermediaries and specific evidence (IT20): follow [the republished-claim bullet of the convention](../../../../framework/protocols/repurposing_adapter_convention.md); a verifier must recompute any 'X to 0' claim from a fresh regeneration (IT20: a claimed 21 to 0 was still 21).
- Dated measurements and decisions are in the iteration section of the [module README](README.md) marked CURRENT.
- **Look for the capability the repository already holds before adding one (IT24).** Count a gap as rows, families and distinct substances separately, and test each existing route (own catalogue key, merged bridge, the record's own concept-id ligand) before any query: 93 of 115 rows called incomparable in IT23 already had a structure. A listing-tier DGIdb claim (review table, trial listing) is not a measurement: withhold a sign only for the pairs a source check has read and named (`source_exclusions_it24.tsv`), measure the wider tier as a sensitivity, never adopt it on unread rows, and give no opposite sign by elimination. Read provenance at the level of the sign, not the pair. Decompose a score by target before building a profile engine: the engine already sums over every target, and what was hidden was the structure (use a mass floor; paralog pairs are not independent). A fix to a shared function is made once and a second case is named; committed stage tables that cannot be re-derived from one command are not edited by hand, and the difference between code and tables is written down. Before freezing a candidate for the release battery, record the new receipts first and then regenerate the pages derived from the ledger (`coverage_report.py`, `reading_state.py`, and `ranking_it8_p9_20261029/ranking_it8.py run`, which embeds the ledger line count; each suite prints its own command), and give any new test `unittest.main(verbosity=2)`: the IT24 first battery failed on exactly these three. Reproduced in `identity_it24_p2_20261104`, `source_check_it24_p1_20261104`, `multitarget_it24_p6_20261104`, `reverse_it24_p10_20261104`, `verification_it24_20261104`.
- **A listing row can be an alias, and a threshold can be crossed by removing data (IT25).** Before reading a listing-tier pair as pharmacology, check the gene's aliases (ZHX2 carries `RAF`, which turned two RAF inhibitors into ZHX2 ligands); the symbol authority (HGNC) may not list the alias that the source used. When withholding an unsupported sign lifts a z over a convention, report the crossing as a consequence of removed data, never as new evidence. Regenerate a stage by a control first: the current code on the committed engine output must reproduce the committed tables except for the change under test (`--no-v1` is not that control). Reproduced in `generation_it25_a1_20261104`, `source_check_it25_a2_20261104`.
- **An alias can sit on the drug side too, and a licence can be read from the bundle (IT26).** A listing row whose targets fit another drug is a code collision: DGIdb gives rabeprazole and lucitanib the same code `E-3810`, so six FGFR/VEGFR pairs sat on a proton-pump inhibitor. A gene-alias scan (`alias_scan_it26_a2_20261104`) cannot see it and a name-based DGIdb query does not return alias matches; read the family's targets against its own ChEMBL claim. A terms page that a plain fetch cannot render may still be a static chunk of the application bundle (G-SRS "Licensing": CC0 1.0): look for the lazy route before settling for a weaker basis. An identity route (R4) gives the generator an identity, never a merge, and only for rows a second actor confirmed at structure level.
- **Verify a deposit before consuming it, and let a result enter only where it can act (IT27).** A second actor re-derived the IT24 deposits (`verification_it27_p1_20261104`, `verification_it27_p2_20261104`): regions of one animal are repeated measures, not replicates; a count model finds more than a log-OLS at n 5 v 5 (so "no call" is power, not null); a TPM median shift can be compositional drift, not a cell loss; a gene list can carry tissue-restricted, non-neural transcripts that point to a dissection rival, so it is not seeded as a drug lever. What entered the generator is the verified contrast of genes that were ALREADY seeds, as an informational annotation (`generation_it27_p3_20261104`): visible on 69 proposals, order unchanged. A result that cannot move an order is still worth carrying as a limit; it is not worth a new question.
- **Say how a tie is broken, and make alternatives readable (IT27).** The H5 text now lists all six order terms and says the larger smallest-|z| wins; an exact tie is not broken by science (the first row in table order is kept) and `mechanism_clusters_it21.tsv` exports `tie_size`. Representatives that tie are different representatives for different experiments, not a measured superiority (`alternatives_it27_p5_20261104`: HDAC5, XIAP, EZH2, ROCK2). A drug-side code collision detector exists (`alias_scan_it26.py collide`); it finds E-3810 and is a pointer list, not a verdict, and it does not see an alias that lives in a ligand-record join (fexagratinib/AZD5363 was re-classified as an unmeasured listing).
- **Current stage (IT29).** The current generation tables are `generation_it29_p5_20261105/results_s10/` (S9 `generation_it28_p6_20261105/results_s9/` and S8 `generation_it27_p3_20261104/results_s8/` are the two previous stages; this pointer named S8 through IT28 although S9 existed, which a cold reader cannot detect from file dates, so it is updated with every stage). The ranking and the dashboard read the frozen `results_p4` on purpose, not the newest stage. Earlier stage folders and `generation_it22_p1_20261103/results_p4` are historical snapshots kept for comparison and regression; consumers that still read them (signature, relations and verification scripts) read them on purpose. A proposal reaches the ranking only through a qualification record and `proposals_map*.tsv`, never by leaving the generator.
- **A question is a step of the mandate record, and its result must be found where it was returned (IT28).** A repurposing question that deserves a batch rides as a `challenge` object on a step of the task record the monitor already reads; `framework/scripts/challenge_batch.py check` validates its fields, routes it by nature (identity or measure: targeted reading; shared premise: thematic batch; need without interpretation: exploratory batch), reports whether its sources were already read (a repeat without a stated reason is flagged, a motivated re-evaluation is not) and whether every named consumer file carries its id. No separate challenge registry exists. Two worked cases: `CH-IT28-HDAC5-LEVER` (one muscle origin; catalytic inhibition not shown to lower HDAC5 output; carried as a limit on 23 proposals) and `CH-IT28-ISR-ROLE` (the sign of an ISR lever depends on the node and the stress class; INV-02 keeps its position, its test is sharpened). No detected shared origin does not certify independence.
- **Join the measures the catalogue already holds (IT28).** A GtoPdb ligand without a ChEMBL id joins a catalogue family by the FULL InChIKey only (never the first block, never a labelled analogue), and an R4 identity carries the measures of its ChEMBL family. Effect: tazemetostat's EZH2 value is no longer invisible; 53 proposals gain an attribution state; eligibility and hand-overs do not move. Known consequence to watch: a compound measured elsewhere but not at the main target (UNMEASURED_AT_MAIN_TARGET) now ranks after an unmeasured one, so knowing more is not rewarded in the order key.
- **A blind reconstruction mostly finds counter-reasons; carry them as limits (IT28).** Rebuilding the reasons for tazemetostat and TMP269 from sources, without opening any generation output, found no measured WWOX link and several counter-reasons (EZH2 and HDAC4/5 needed for myelination; seizure aggravation after EZH2 inhibition) that the rows did not carry. They now travel as `class_limit` rows of the decision scope (no veto; abstract level), and the table separates reasons that entered the calculation from those that did not (`inverse_it28_p8_20261105`). The reconstruction runs in the same repository and runtime as the producer, so it is separate in context, not perfectly blind.
- **Open assay-level data are not open (IT28 scout).** Papyrus, ExCAPE and ChEMBL-derived sets carry no substrate or construct column and share ChEMBL's upstream; the class IIa discordance needs the methods sections or the free-text ChEMBL assay descriptions already held. A shared accession is sufficient for shared origin, not necessary.

## Delivery sequence and stop condition

Start with R1–R3 after reconciling the latest delivered iteration. R8/R9/R11 use existing
scouting and licence work alongside it. Then apply R4–R7 to a real question in each research
objective and expose the result through R10. Maintain R12 rather than rebuilding it.

Each increment closes with a reproducible output, an observed limitation and the next
decision it enables. A failed source is not a negative biological result; an abstention
names the search performed, missing datum and reopening condition. Continuous improvement
does not require an endless session: stop an increment when its comparison is resolved and
no further low-cost action clearly improves scientific integrity, safety or throughput.

## Public methodological references

These are pointers for the planned work, not WWOX efficacy evidence or full-text reading
receipts. Consult the actual methods and existing receipt/dossier state when using a paper.
The ALS white paper's cross-tissue grouping and predicted responder groups motivate tests;
they do not establish nasal-to-neural validity or independently observed responder labels.

- [Unravel science and platform](https://www.unravel.bio/science)
- [Drug-development approach](https://www.unravel.bio/a-new-age-in-modern-drug-development)
- [ALS white paper and figures](https://www.unravel.bio/als-unravelled-a-patient-centric-approach-to-drug-discovery-and-clinical-validation)
- [rareSHIFT study design, outputs and limitations](https://www.rareshift.org/faq)
- [Living Molecular Twins description](https://www.unravel.bio/living-molecular-twins-to-accelerate-drug-development-and-clinical-impact)
- [rareSHIFT poster 2025](https://static1.squarespace.com/static/64dfd0497abb8c2c0438a25b/t/680bdf11b125020fb90d8f31/1763400064336/WODC+2025+rareSHIFT+Poster+48x36.pdf)
- [KMT2B poster 2025](https://static1.squarespace.com/static/64dfd0497abb8c2c0438a25b/t/680bdf1e46530733b10f43aa/1763400064336/WODC+2025+KMT2B+poster+48x36.pdf)
- [REVOLUTION trial poster 2026](https://static1.squarespace.com/static/64dfd0497abb8c2c0438a25b/t/6a21ea37a8a61a0ad3043232/1780607543945/WODC+2026+REVOLUTION+Trial+poster+42x36.pdf)
- [Clinical outcomes poster 2026](https://static1.squarespace.com/static/64dfd0497abb8c2c0438a25b/t/6a21eccca175fd512413449d/1780608204024/WODC+2026+Clinical+Success+Poster.pdf)
- [NeMoCAD software access terms](https://zenodo.org/records/7692713)
- [Network-method precedent, PLOS Computational Biology 2023](https://doi.org/10.1371/journal.pcbi.1011050)
- [Rett preclinical-method precedent, Communications Medicine 2025](https://doi.org/10.1038/s43856-025-00975-8)
- [WWOX Foundation research programme](https://www.wwox.org/current-research)

All source descriptions are summarised in original wording. No proprietary code, figures,
newsletter contents, patient profiles or efficacy percentages are imported by this update.

## Matching guidance v3 — first measured increment, 30 October 2026

The [operator guidance](matching_guidance_v3.md) is the methodological direction.
The [existing ranking pilot](ranking_it8_p9_20261029/README.md#matching-v3-pilot--30-october-2026)
projects four contrasting cases (five relationships) into its export and full view:
member-specific evidence, action/context/benefit hypothesis, research question and
separate scoped development requirements. This does not implement all discovery
logics or change biological groups. Three concrete fixtures cover duplicated
evidence, transfer between molecules, and unknown becoming negative.

Next: use the PX-478/HIF case to resolve the neural protein/functional premise before
any compound promotion; compare another discovery logic only where it answers a
named gap. Expand fields to other candidates when the pilot changes a decision.
Continue the daily radar and the existing deployment/licensing work on their own
current work orders; no new scheduler, contract or gate is introduced here.

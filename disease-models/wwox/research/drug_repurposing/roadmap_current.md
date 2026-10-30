# Drug repurposing — current development roadmap

Updated 2026-10-29 by `orchestrator`, runtime Codex, following the operator's request to
consolidate the Unravel/BioNAV/rareSHIFT and ALS discussion into this roadmap.

**Planning, not an implementation or efficacy report.** This is the home of the next
increments. The newest measured iteration in [README.md](README.md) describes what actually
works. The [operator-supplied v4/r14](roadmap_v4_r14_20261020.md) stays verbatim as historical
provenance. Before executing an increment, fetch remote `main`, reconcile the latest measured
iteration and reuse any work already delivered. This update authorises recording the plan;
it does not claim that its research experiments, deployments or integrations have run.

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

## Daily discovery: two complementary searches

1. **Scientific needs:** WWOX plus mechanism-specific searches when useful, including
   pathways, metabolism, stress responses, excitability, glia and assay methods even when
   the paper never mentions WWOX. Reread for a new question or a decisive missing detail.
2. **Capabilities and benchmarks:** GitHub, Hugging Face, primary publications and official
   documentation for repurposing, compound matching, predictive methods and useful
   Scientist/Orchestrator patterns. Do not require WWOX as a keyword. Prefer inspectable
   methods, independent evaluation, maintained assets and usable terms over popularity.

Use the existing daily rotation and triage only material changes. Install or retain a tool
when its measured gain pays for its dependencies and operational cost; remove duplicative
components. External spend remains zero, with no account creation, email contact or transfer
of private data implied. Monitor Unravel for public methods/data, not repeated promotional
counts.

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

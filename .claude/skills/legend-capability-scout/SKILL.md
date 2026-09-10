---
name: legend-capability-scout
description: LEGEND evolutionary radar to search, after each session or when the operator asks, for new skills, plugins, repos, databases and tools that surgically, cumulatively and continuously increase the analysis, inference, drug-repurposing and targeted therapeutic-initiative capabilities of the disease model. Every session must produce at least one capability micro-upgrade (an import, an audit, a monitor, a mini-procedure or an improvement to an existing skill), proportional to what was learned. It starts from WWOX, phenotype, alleles, Q230P, c.1057-2A>G, safety, biomarkers or missing workflows; identifies capability gaps; searches external resources; proposes growth without modifying canonical current files. Use it when the operator says "look for new skills/repos/plugins", "let's grow the capabilities", "what do we lack to reason better", "after this session scout new resources", or for an end-of-session retrospective.
---

# legend-capability-scout — Surgical capability radar

Paths are relative to the workspace root.

## Purpose

Grow LEGEND in a **targeted, cumulative, continuous and potentially infinite** way, without rewriting the system and without accumulating useless tools.

Underlying principle: the difference between an average researcher and a good one is the ability to **grow together with the project**. If only the repo grows but competence, tools, procedures, inferential skill and the agent's operational capabilities do not, the system becomes too large to govern well. This skill exists to keep the two growths aligned: **knowledge grows, capabilities grow too**.

## Mandatory automatic use

This skill must not depend on the operator's reminder.

Every LEGEND session must:
1. **Bootstrap:** read this `SKILL.md` after `framework/state/state_manifest_current.md`, `CLAUDE.md` and `AGENTS.md`.
2. **During work:** keep note of the capability gaps that emerge.
3. **Closing:** apply at least one micro-scout proportional to the session and record the micro-upgrade in the capability scout log.

If the session is very short or purely administrative, the micro-upgrade can be minimal: auditing a note, an exclusion criterion, monitoring a resource, or a motivated confirmation that nothing is imported but a procedure is improved. Zero growth is not admissible.

This skill produces no scientific claims. It produces a **map of missing capabilities** and controlled proposals of:
- Codex/Claude skills
- plugins/tools
- GitHub/GitLab repos
- biomedical databases
- methodological papers transformable into pipelines
- resources for drug repurposing, ASO, chaperones, AAV, PBPK, BBB, safety, phenotype, mutations

## The mother rule

**Learning by doing: every session must improve the capabilities at least a little.**

The improvement can be small, but not null:
- a new repo/DB/tool imported for a real gap
- a new resource put on `MONITOR`
- an audit of an already-imported skill/repo
- a mini-procedure added to an existing skill
- an operational link between two already-present tools
- a "nothing more needed here" note with a new reusable exclusion criterion
- an improvement to reasoning, workflow, safety, privacy, interpretation, visualization, operational memory or complexity management

Then: **Capability gap first. Tool second.**

Do not look for "interesting repos" in the abstract. Start from a gap that emerged in the session, but do not stall: if the session reveals no glaring gap, pick a proportional micro-upgrade.
- what can we not yet infer?
- which pipeline step is weak?
- which question about the case can we not attack well?
- which therapeutic modality is missing from our arsenal?
- which safety/translational check is missing?

## Writing

READ-ONLY toward:
- the 4 canonical current files
- the biomarker/endpoint layer
- the therapeutic tracker
- every canonical scientific file

WRITABLE, if useful:
- the capability scout log (create from `references/capability_scout_log_template.md` if absent)

The log is **operational, non-canonical, append-only**. It introduces no claims, modifies no therapeutic strategies, promotes nothing into the current files.

External imports:
- new repos go into `_external_repos/medical_ai/`
- `_external_repos/` stays gitignored
- clone/audit only; do not run install scripts or the repos' code without an explicit request

## Procedure

### 1. Session Learning Delta

Summarize in 5-10 lines what the session learned or made more important:
- allele/mechanism
- phenotype/endpoint
- therapeutic hypothesis
- safety/translation
- missing tooling

Example: "Q230P looks misfolding-dominant but a pipeline for pocket/allosteric stabilizer ranking is missing".

### 2. Capability Gap

State 1-8 concrete gaps, in the format:

`To do X on the case/WWOX we lack Y.`

Examples:
- To triage Q230P chaperones we lack pocket/allosteric scanning + thermal shift validation.
- To assess pediatric repurposing we lack PBPK/BBB/DDI.
- To design an ASO on `c.1057-2A>G` we lack a specific SSO workflow, not gapmer.

### 3. Search Plan

For each gap, search resources by category. If the gap is small, do a short search and propose a single micro-upgrade.
- **Evidence/RAG**: full text, citation QA, contradiction detection.
- **Genotype-to-drug**: variant/gene annotation, DGIdb, Open Targets, Pharos, CIViC.
- **Repurposing**: KG, network medicine, LINCS/CMap, rare-disease platforms.
- **Genetic/RNA**: ASO, splice, CRISPRa, base/prime editing, AAV.
- **Protein/small molecule**: chaperones, pockets, docking, ADMET, PBPK, BBB.
- **Peptides/proteins**: binder design, stabilization, allosteric modulators.
- **Safety**: pediatric, CNS, DDI, toxicology, pharmacogenomics.
- **Disease-specific**: WWOX, WOREE, Q230P, `c.1057-2A>G`, seizures, myelination, glia, GSK3b, Wnt/MYC.
- **Agent capability**: procedure, memory, skill design, orchestration, evaluation, visualization, error detection, auditability.

Use web/GitHub/GitLab when the data may have changed or be recent.

### 3b. Environment preflight — a verdict is keyed to the host that produced it

Before any `SKIP` or `REJECT` on the ground that a tool is *absent* or *present*, run
`python3 framework/scripts/tool_preflight.py` and write its verdict, the host, and the versions
that matter (`python3 -c "import fitz; print(fitz.__doc__)"` for PyMuPDF) into the entry.

Why: `capability_scout_log.md` skipped PyMuPDF on 2026-09-09 because *"`fitz` is already absent
in this environment and a red suite proves it."* On the same day, in the same repository, on a
different host, `import fitz` succeeded (PyMuPDF 1.28.2) and `tool_preflight.py` reported 6/6
present — the surface census's own sentinel was running on it. **Actor sessions do not share an
environment, and a capability verdict keyed to one session's environment does not generalise.**
A verdict that names its host is still true when the host changes; one that does not is a claim
about nothing in particular.

### 4. Score

Each candidate receives:
- **Case fit** 0-3
- **LEGEND fit** 0-3
- **Novel capability** 0-3
- **Maturity** 0-3
- **Cost/privacy risk** 0-3 inverted: 3 = local/free, 0 = paid/sensitive/high friction
- **Action**: `IMPORT`, `AUDIT`, `MONITOR`, `SKIP`

Safety rule:
- paid/API/closed-source/sensitive-data risk -> do not import automatically; propose `AUDIT` or `MONITOR`.
- non-biomedical but adaptable repo -> `AUDIT`, not `IMPORT`, unless clear usefulness.

### 5. Output

In chat:
- 1-5 recommended new capabilities
- what they solve for the case/LEGEND
- cost/privacy
- proposed action
- **the session's mandatory micro-upgrade**: what grew today, even if minimal

In the log, if requested or if the session is an end-of-cycle one:
- append a dated section to the capability scout log
- do not delete previous entries

## What NOT to do

- Do not rewrite existing workflows if a small bridge suffices.
- Do not download huge repos without a clear reason.
- Do not use "surgical" as an excuse for immobility: every session must leave at least one capability slightly better.
- Do not confuse growth with accumulation: a better procedure can be worth more than 20 imported repos.
- Do not install or run external code out of mere curiosity.
- Do not treat popularity/GitHub stars as scientific evidence.
- Do not put sensitive clinical data into remote queries.
- Do not turn a found capability into a claim, strategy or current file.

## Mandatory closing

Always close with:
- what was added/proposed
- the minimal micro-upgrade obtained in the session
- what remains to audit
- whether there is a cost/API/privacy risk
- the next surgical micro-step

Also, before the final response, apply `.claude/skills/legend-session-takeaways/SKILL.md` when present: the operator must receive not only the technical micro-upgrade, but also the distillation of what the session taught and which useful leads emerge for the disease model/WWOX.

---
name: legend-harness-scout
description: Weekly harness scouting for LEGEND, run by the Junior Harness Engineer (ACTOR_ID junior-harness) and consumed by Harness Engineering (ACTOR_ID plan). Mines three sources every week — GitHub (multi-agent research harnesses, agent tooling, Claude Code / Codex plugins and skills, literature and evidence pipelines, co-scientist and autonomous-lab frameworks), Hugging Face (biomedical NER and relation extraction, literature QA, rare-disease and genomics models, splice prediction, ADMET, protein language models) and the Nature portfolio (Nature Methods, Nature Machine Intelligence, Nature Biotechnology, Nature Communications, Scientific Data software/resource/analysis articles with code availability) — and writes one candidate table per week to governance/candidates/HARNESS-SCOUT-<YYYY>-W<WW>.md with what each candidate adds to LEGEND, its integration cost in HOURS, license, risk and a proposed verdict (ADOPT / TRIAL / WATCH / REJECT). Harness Engineering triages the table on Monday and implements ADOPT/TRIAL at T0 with no Mirror review and no gate (LEGEND_CORE §21e). Use it when the operator or Harness Engineering says "weekly harness scouting", "scout similar repos", "what do other multi-agent research harnesses do", "Junior Harness Engineer weekly report", "what should the harness adopt this week". Zero external spend; read-only toward the four scientific current files, the registries and the ledgers.
---

# legend-harness-scout — the weekly harness radar

Paths are relative to the workspace root.

## Purpose

LEGEND's **harness** — the worktree/branch discipline, the guard, the skills and agents, the
ledgers and their tooling, the review loops — must evolve at the pace of the field, not at the
pace of the last person who had time to look around. Under `DEC-20260905-AGILE-HARNESS-MODE`
([`LEGEND_CORE.md` §21e](../../../framework/instruction/LEGEND_CORE.md#21e-agile-operating-mode))
a decided harness change is implemented at **T0, in hours**. This skill is the input side of
that loop: it produces, every week, a short concrete list of things worth adopting, with the
cost of adopting them stated in hours, so that the decision and the implementation can happen
on the same Monday.

It is distinct from [`legend-capability-scout`](../legend-capability-scout/SKILL.md), which
grows the *scientific* capabilities of the disease model after each session. This skill grows
the *machine*.

## Who runs it, when

| Actor | Role | Cadence |
|---|---|---|
| **Junior Harness Engineer** (`junior-harness`, [`roles/junior_harness.md`](../../../roles/junior_harness.md)) | runs the scout, writes the weekly file | every Monday, and on request |
| **Harness Engineering** (`plan`, [`roles/plan.md`](../../../roles/plan.md)) | triages the table, fills the verdict column, implements ADOPT / TRIAL the same day | Monday |

No Mirror review, no HUMAN_APPROVAL, no gate: the report is landed on `main` by its author at
task end, and the adopted candidates are landed by their implementer at T0. External spend
stays at zero — no paid APIs, datasets or compute.

## The three sources, with recipes

### 1 · GitHub

- Queries (search, sort by *recently updated*, then by stars): `multi-agent research`,
  `agent harness`, `claude code plugin`, `claude code skill`, `codex plugin`,
  `scientific literature agent`, `evidence pipeline`, `systematic review agent`,
  `autonomous lab`, `co-scientist`, `research agent benchmark`, `rare disease pipeline`.
- Topics: `ai-agents`, `multi-agent-systems`, `llm-agents`, `scientific-computing`,
  `bioinformatics`, `literature-mining`, `knowledge-graph`.
- For each hit read the README and any `ARCHITECTURE`/`docs/` before writing a row. Record
  stars, last commit date, license, and whether it runs offline.
- Skip anything whose last commit is older than twelve months unless it is a reference
  implementation of a method LEGEND already uses.

### 2 · Hugging Face

- Hub search (models, datasets, Spaces) and the Hub API (`/api/models?search=…`,
  `/api/datasets?search=…`): `biomedical NER`, `relation extraction`, `PubMed QA`,
  `literature question answering`, `rare disease`, `variant effect`, `splice prediction`,
  `ADMET`, `protein language model`, `clinical trial`, `gene ontology`.
- Record task, license, model or dataset size, last update, and the evaluation evidence the
  card actually shows (a card with no evaluation is `WATCH` at best).
- Prefer artifacts that run on CPU or a single consumer GPU; LEGEND has no paid compute.

### 3 · Nature portfolio mining

- Journals: *Nature Methods*, *Nature Machine Intelligence*, *Nature Biotechnology*,
  *Nature Communications*, *Scientific Data*; article types **software**, **resource**,
  **analysis**, **technology feature**, **tools of the trade**.
- Search the journal's own listing pages for the past week, then open the **Code
  availability** and **Data availability** sections of each candidate. A paper whose code is
  "available on request" is not a candidate.
- Record the repository, its license, whether it installs cleanly, and what claim in the paper
  LEGEND would actually use.

## How to read a candidate

For every row answer, in one line each: **what it adds** to LEGEND (name the skill, script or
protocol it would extend or replace); **integration cost in hours** (a number, not "low");
**license** (and whether it is compatible with a public repository); **maintenance signal**
(last commit, open issues, single maintainer?); **risk** (privacy, licensing, network, model
size, correctness claims without evaluation); **what it would replace**, if anything.

## Output contract

One file per week: `governance/candidates/HARNESS-SCOUT-<YYYY>-W<WW>.md` (ISO week).

```markdown
---
record_type: HARNESS_SCOUT
week: <YYYY>-W<WW>
author: junior-harness
handoff_to: plan
status: PROPOSED → TRIAGED (Harness Engineering fills the verdict column)
---

# Harness scout — <YYYY>-W<WW>

| # | candidate | source (URL) | what it adds to LEGEND | integration cost (h) | license | risk | proposed verdict | HE verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | … | … | … | 3 | MIT | low | ADOPT | |

## Top 3 for this week
1. **<candidate>** — one paragraph: what to change, in which file, and how to test it.
2. …
3. …

## Watch-list carried forward
| candidate | first seen | why still WATCH |
|---|---|---|

## Looked at and rejected (one line each)
- <candidate> — <reason>

## Handoff
Harness Engineering (ACTOR_ID `plan`) implements every ADOPT and TRIAL at T0 on Monday and
lands them on `main`; this file is updated with the HE verdict column and the landed commit.
```

Verdict vocabulary: `ADOPT` (implement now), `TRIAL` (implement behind a switch or on a
sample, now), `WATCH` (re-check next week; carry forward with the date first seen),
`REJECT` (one line why; never re-scouted from scratch).

## What this skill does not do

- It does not adopt anything on its own: `ADOPT` is Harness Engineering's verdict.
- It does not touch the four scientific current files, the registries or the ledgers.
- It does not spend.
- It does not gate, review or block anyone's landing.

## Checks before landing the weekly file

```bash
python3 scripts/test_skill_packages.py           # the skill catalogue stays consistent
python3 framework/scripts/branch_hygiene.py      # the scout's own branch lands the same day
```

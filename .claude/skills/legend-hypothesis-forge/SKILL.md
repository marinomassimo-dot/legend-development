---
name: legend-hypothesis-forge
description: 'LEGEND therapeutic-hypothesis generator (the THERAPEUTIC_HYPOTHESIS_GENERATOR of the external-repos README). From the disease genotype of interest + working model + therapeutic portfolio + verified full texts, it forges 10–30 candidate therapeutic hypotheses (splice correction/ASO, CRISPRa, small-molecule pathway rescue, drug repurposing, window protection) and runs them through a co-scientist loop generate→critique→rank→evolve, with a BLOCK-1 safety gate and mandatory epistemic tagging. Use it when the operator says "generate therapeutic hypotheses", "what could we try", "squeeze the model for candidates/levers", "run the co-scientist", or when they want to turn accumulated knowledge into a fan of actionable moves instead of filing yet another paper. Distinct from legend-discovery (mines papers for needle-leads) and legend-deepdive (produces canonical claims): this starts from the already-accumulated model and produces a scored, non-canonical hypothesis portfolio that feeds the therapeutic tracker.'
---

# legend-hypothesis-forge — Therapeutic-hypothesis forge

Paths are relative to the workspace root.

## Why this skill exists
LEGEND's goal is not to understand WWOX: it is to **reduce WWOX-dependent harm and buy time until gene therapy, with any actionable lever — even a partial one** (mission north-star in `disease-models/wwox/mission.md`). Understanding is the instrument.

`legend-deepdive` files papers into the canonical system. `legend-discovery` mines every paper for useful needles. **This skill takes the next step**: it takes the already-accumulated capital (working model + discovery ledger + therapeutic portfolio + verified full texts) and **converts it into a fan of actionable therapeutic hypotheses**, each with mechanism, evidence for/against, risk, and the minimal experiment that would falsify it.

**Receipt reuse gate.** “Verified full text” means a matching persisted
`FULLTEXT_READ_RECEIPT` already exists. Query the ledger first and reuse the dossier and
coverage it names. This skill does not silently reread source articles. If a new question
requires material outside the earlier coverage, hand the study back to a full-text route;
the new event must link `prior_receipt` and declare an allowed `reread_reason`.

It is the operationalization of the idea written in the README of `_external_repos/medical_ai/`:
the non-canonical **`THERAPEUTIC_HYPOTHESIS_GENERATOR`** module, inspired by the co-scientists
(`robin`, `open-ai-co-scientist`, `open-coscientist`, `AI-CoScientist`) and the hypothesis generators
(`hypothesis-generation`/HypoGeniC, `SciMON`): the **Generation → Reflection → Ranking → Evolution** cycle,
wired inside LEGEND's epistemic discipline and its guardrails.

## Human gate
Starts ONLY on the operator's explicit request. Does not generate hypotheses on its own initiative outside the open thread.
It is never medical advice: every output supports discussion with a treating team, it does not replace it.

## Discipline — what you may and may not write
- **READ-ONLY** toward the canonical scientific model and registries, the biomarker/endpoint layer, and the scored therapeutic tracker. Nothing here enters the canonical layer except via `INGEST → DEEP_DIVE → COMMIT CANDIDATE → BATCH_COMMIT`.
- **WRITABLE** outside BATCH_COMMIT — the same carve-out as the discovery ledger — a single file: the **therapeutic hypothesis ledger** (structured-append, explicit epistemic tags, change-log, a status per hypothesis). **It is not a canonical scientific file and introduces no canonical claims**: it is strategy space.
- **Append discipline**: a hypothesis is not deleted, its status changes: `generated` → `stress-tested` → `ranked` → `proposed-to-portfolio` → `parked` → `refuted`. Promotion to a scored strategy in the tracker, and then to canonical fact, happens only downstream, through the normal pipeline.
- Never present INFERENZA/IPOTESI/ESPANSIONE as DATO. Never self-authorize an URGENT. **BLOCK-1 beats enthusiasm.**

## Epistemic discipline (mandatory)
Every assertion classified: **DATO** (directly supported by a peer-reviewed source) / **INFERENZA** (convergence of multiple data) / **IPOTESI** (reasonable, undemonstrated, flagged) / **ESPANSIONE** (outside the direct WWOX domain).
In this forge, IPOTESI and ESPANSIONE are the daily bread — **it is their place** — provided they are labelled honestly and **never passed off as data**. Every generated hypothesis is born tagged `IPOTESI` or `ESPANSIONE` until validated: that is the rule.

## The levers (axes to generate along)
Generate across all levers, not only the obvious one. Full map in `disease-models/wwox/mission.md`; minimal axes:
1. **Defect correction** — splice-switching ASO / targeted exon-skipping for a splice variant of interest; readthrough; upregulation of the residual allele.
2. **Upstream/downstream compensation** — CRISPRa / transcriptional activation of WWOX; rescue of dysregulated pathways (metabolism, myelin/glia, GABA, GSK3β, prenatal structure — see the active meta-analyses).
3. **Repurposing** — existing drugs touching a node of the WWOX-dependent network (triangulatable with TxGNN/DRKG/RTX/PrimeKG as a *signal*, never as proof).
4. **Window protection** — time-sensitive levers that "buy time" *now* without touching WWOX (seizure burden, network stability, myelination). The partial counts.
5. **Enabling biomarkers** — if a therapeutic hypothesis needs a WWOX functional-state readout we do not have today, generate it as a linked biomarker-hypothesis (`[[biomarker_candidates_current]]`).

## Anchor on the real disease model (non-negotiable)
Every hypothesis is generated *against the real case*, not in the abstract: genotype (alleles such as `c.1057-2A>G`, `Q230P`, affected exons and domains), electrophysiology, known phenotype, and the real time horizon to gene therapy. An elegant but non-translatable lever is worth less than a partial but actionable one.

## Procedure — the co-scientist loop (4 phases + output)

**0. Load the context.** Before generating, read:
- the state manifest (READY state, current WM version).
- the working model, claim registry, paper registry (what we really know, and how strongly).
- the discovery ledger (needles already collected — the main starting point) and the research lines.
- the therapeutic strategy portfolio (to **avoid duplicating** already-portfolioed strategies and to know what is already scored).
- the biomarker candidates (known biomarker-levers).
- the therapeutic hypothesis ledger — if it does not exist, create it from `references/hypothesis_ledger_template.md`; if it exists, **compound**: link and do not repeat.
- optional KG/repurposing signals provided by the operator (TxGNN/DRKG/RTX/PrimeKG output) → treated as `ESPANSIONE`/`IPOTESI`, never as DATO.

**1. GENERATION.** Produce **10–30 candidate hypotheses**, spread across the 5 levers. Each in falsifiable form: "If [mechanism], then [measurable effect on the case/model], because [rationale anchored to the WM]". Breadth before depth: include contrarian and second-order ones. Do not filter yet.

**2. REFLECTION / CRITIQUE.** Sift every hypothesis, making explicit:
- **Mechanism** — biological plausibility given the WM; which node it touches.
- **Evidence for / against** — with `DATO/INFERENZA/IPOTESI/ESPANSIONE` tags and wikilinks to the claim/paper registries (`claim_registry_current#CLAIM …`, `paper_registry_current#PAPER …`) where they exist.
- **Safety (BLOCK-1)** — known risks, off-target, therapeutic window; if it hits an inviolable guardrail → the hypothesis is `flagged`, it does not die but does not advance.
- **Translatability** — applicable *to this genotype*? Practical constraints (CNS delivery, window, reversibility).
- **Time-sensitivity** — does it act on a closing window? (extra weight: time-sensitive variables count more than static ones).

**3. RANKING.** Order with a tournament/score over 5 criteria (rubric in `references/ranking_rubric.md`): **actionability · evidence strength · safety · time-to-benefit · value-of-the-partial**. Ranking is a triage tool, not a verdict: always justify why one beats another.

**4. EVOLUTION.** Evolve the top ones: combine complementary hypotheses, mutate promising-but-fragile ones into more robust or more testable versions, discard the dominated (status `refuted`/`parked` with a reason). One or two iterations suffice — seek the quality jump, not infinite optimization.

**5. OUTPUT.** Write/update the therapeutic hypothesis ledger (append, never overwrite old entries: change status). For each hypothesis surviving the ranking, an entry with:
- ID (`HYP-YYYYMMDD-NN`), title, lever, mandatory epistemic tag (`IPOTESI`/`ESPANSIONE`).
- Proposed mechanism · evidence for/against (with wikilinks) · risk/safety · translatability · time-sensitivity.
- **Minimal falsification experiment** (the piece that makes it scientific, not a wish).
- Score + rank + rationale.
- Status and, if mature, a `proposed-to-portfolio` flag with a note of what promotion to the tracker would need.
- Session change-log at the bottom of the file.

## Closing (mandatory in chat)
1. Summary: how many hypotheses generated, top 3–5 with lever and tag.
2. Any `proposed-to-portfolio` and what is missing to promote them.
3. Any safety signals (BLOCK-1) that emerged.
4. Disclaimer: **"Not medical advice: it is support for discussion with a treating team. Hypotheses are IPOTESI/ESPANSIONE until validated by the LEGEND pipeline."**

## What NOT to do
- Do not touch the canonical model or the therapeutic tracker (read-only).
- Do not promote a hypothesis to DATO/claim: that needs the full pipeline.
- Do not generate false hope: a fascinating hypothesis with no falsification route is marked as such.
- Do not self-authorize URGENT_COMMIT.

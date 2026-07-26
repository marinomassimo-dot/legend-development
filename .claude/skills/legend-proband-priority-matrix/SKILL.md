---
name: legend-proband-priority-matrix
description: "Disease-targeted priority-scoring matrix for LEGEND: turns studies, abstracts, full texts or batch-inferential-sweep output into biology-targeted reading priorities for the disease model, weighting the mechanistically actionable axes (a missense variant of interest, a splice allele, proteostasis/chaperones, ASO, gene therapy, neuro-network/seizures, neuroinflammation, myelin, endpoints, repurposing and BLOCK-1 safety). Use it when a batch of studies or therapeutic hypotheses must be ordered not merely by WWOX keyword, but by concrete potential usefulness to the disease model."
---

# legend-proband-priority-matrix

Disease-targeted biological scoring. It does not replace `legend-batch-inferential-sweep`: it refines it. ("Proband" here is the epidemiological index-case sense; the matrix operates on a disease model, not on any identified individual.)

## When it activates

Use it:
- right after `legend-batch-inferential-sweep`;
- when a batch contains many WWOX / oncology / neurology records and the reading order must be decided;
- when therapeutic hypotheses emerge and it must be clear what deserves energy;
- when the operator asks for priority "for the disease model", "for the missense allele", "for splice", "for repurposing", "for safety".

## Main resource

The matrix lives in:

```text
.claude/skills/legend-proband-priority-matrix/references/proband_priority_matrix.json
```

The batch sweep loads it automatically if present. For manual use:

```bash
python3 .claude/skills/legend-proband-priority-matrix/scripts/score_proband_priority.py \
  --input staging/batch_inferential_sweep_YYYYMMDD.json \
  --out staging/proband_priority_scored_YYYYMMDD.json
```

## Conceptual output

Each record receives:
- `proband_score`: the targeted score;
- `proband_priority_tier`: `P0_FAST_TRACK`, `P1_HIGH`, `P2_MEDIUM`, `P3_LOW`, `P4_BACKGROUND`;
- `proband_axes`: the biological axes activated;
- `proband_rationale`: a short human-readable reason.

## Rules

- The matrix is **operational triage**, not scientific evidence.
- If a full-text artifact is inspected directly rather than consuming an existing sweep,
  emit a `FULLTEXT_READ_RECEIPT` with `evidence_depth: queried_not_full_read` for each
  study and persist it through the main session. Priority scoring is non-exhaustive and
  never establishes `complete_fulltext_read`.
- Do not use it as an autonomous sorter over a raw, uncurated PubMed query. The prospective validation set LRL-2026-07-11-004 failed both gold-recall metrics (3/8 in the upper half; 2/8 above the control median): run intake + semantic sweep first, then apply the matrix to informative records.
- Apply it to records with an abstract or an informative `sweep_reason`. For a legacy corpus with titles only, use `framework/scripts/unread_gold.py` first: already-curated tier and disease-relevance are more reliable than lexical tier. Do not read the matrix's absolute tiers on `title-only` input.
- Keep a separate lane for `METHOD_LEAD` and `INDIRECT_DISCOVERY_LEAD`: assays, models and indirect WWOX associations can be useful even at a low tier and must not be lost to disease-targeted ranking alone.
- 🔴 **`DOMAIN_PARITY` (precedes everything, including the overrides below).** **A study's disease context is NEVER grounds for down-ranking.** There is no "second-class" domain.
  - 🧬 **Oncology = twenty years ahead.** WWOX was born a tumour suppressor: folding, stability, degradation routes, partners, localization, rescue were characterized by cancer research. **The mechanism of the actionable allele lives there.** A thyroid or breast paper touching WWOX is worth **more** than yet another descriptive WOREE case report.
  - 🧠 **Adult neurology** (Alzheimer, Parkinson, ALS, tau): shared pathways, proteostasis, biomarkers, endpoints and molecules **already tested in humans**. Fully relevant.
  - 📋 **WOREE**: most phenotype-consistent, but largely **descriptive**. **Consistency ≠ usefulness.** They picture the disease; they rarely hand you a lever.
  - 🐄 **"Noise"** (bovine, viruses, basic biology): still worth squeezing — a method, an assay, a partner, a heuristic.
  → **If you are about to lower a study's score because "it is oncology" or "it is not WOREE", stop: you are reproducing the 2026-07-12 error.**
- 🔴 **`MISSENSE_MECHANISM_OVERRIDE` (a concrete case of `DOMAIN_PARITY`; precedes every other score).** Any paper that **functionally characterizes a WWOX missense variant** — stability, folding, degradation route, partner binding, localization — is **`P0_FAST_TRACK` by default**, *in any disease context*, **including cancer**, and regardless of lexical tier, phenotypic keywords, or the absence of "epilepsy/WOREE/neuro".
  **Why.** The mechanistically actionable class of allele of interest (**a missense**, e.g. Q230P) is characterized almost always by **oncology labs** — WWOX began as a tumour suppressor, and the functional work lives there. A triage that weights the neurological phenotype **systematically down-ranks exactly the papers that carry the mechanism of the missense allele.**
  **Real cost of the bug (2026-07-12):** Zhang 2025 (thyroid cancer, **Tier C, "screened — corpus placeholder"**) contained the **degradation route of SDR-domain missense variants** — lysosomal CMA, not proteasome — i.e. the exact answer to the question on which HYP-08, the best-scored hypothesis in the portfolio, was stuck. The ledger's experimental design used MG-132, which in that analogue **is mute**: we would have walked straight into a **false negative**. See the capability scout log (2026-07-12) · [[dismissal_ledger_current]].
  **Practical rule:** if the abstract contains a WWOX variant notation of the form `X###Y` **and** a functional verb (*degradation, stability, turnover, binding, localization, rescue, half-life, misfolding*) → **P0, read the full text.** Do not delegate the decision to the tier.
- Do not promote claims into the canonical model on high score alone.
- Safety / BLOCK-1 can raise review priority but not therapeutic priority.
- Weights must evolve: if the repo discovers new strong lines, add an axis or change a weight with a log in `capability_scout_log.md`.
- Every scoring must distinguish `DATO`, `INFERENZA`, `IPOTESI`, `ESPANSIONE` in the next phase.

## Quick interpretation

> 🔴 **Tiers are QUEUE POSITIONS, not value judgements. None of them authorizes not reading.**
> The matrix answers *"what do I read first?"*, **never** *"what may I skip?"*. If a tier ends up discarding a study, **the tier is broken** — fix the matrix, do not lose the study. See the **parity of sources** principle in `CLAUDE.md`.

- `P0_FAST_TRACK`: read **now**. Direct impact, urgent safety, allele/therapy/time-sensitive window.
- `P1_HIGH`: read **right after**. Deep-dive or hypothesis-forge.
- `P2_MEDIUM`: **queued**, with tracked reading debt. Discovery/endpoint/repurposing.
- `P3_LOW`: **queued**, further back. Still to be read.
- `P4_BACKGROUND`: **queued, last — NOT "archived", NOT "closed".** The reading debt stays open and must be honoured.

### ⚠️ The lowest tier is the most dangerous
`P4`/`Tier C` is where the system has **already been wrong once**: **Zhang 2025** (thyroid cancer, `Tier C — "screened, corpus placeholder"`) contained the **degradation route of the SDR-domain missense allele of interest**, and for days it blocked the best-scored hypothesis in the portfolio. **Do not repeat it.** Before leaving anything at the back of the queue, always ask: *"what if the gold is in here?"* — because once, it was.

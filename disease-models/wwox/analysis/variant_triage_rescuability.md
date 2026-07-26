# Variant Triage — Mechanism → Therapeutic Lever (Chaperone vs ASO)

**The reusable idea:** classify each WWOX variant by *molecular mechanism*, and from mechanism predict *which therapeutic lever* is worth pursuing — and therefore *which wet-lab experiment to prioritize*. Designed to be re-run across the full ClinVar variant set (planned, resources permitting).

> Public, disease-level. Two worked examples below. No patient referenced.

## The decision logic

| Mechanism class | Predicted lever | Prioritized wet-lab test |
|---|---|---|
| **Missense, folding/stability defect** (high ΔΔG, buried core) | **Chaperone / proteostasis** modulation; possible small-molecule stabilizer | protein level/stability rescue assay (± proteasome vs lysosome probes) |
| **Canonical splice-site / cryptic-splice** | **ASO** (splice-switching / splice-correcting) | minigene / RNA splicing assay; ASO walk |
| **Nonsense / frameshift / null / large deletion** | **Gene addition** (AAV), read-through (context-dependent) | expression rescue; vector feasibility |
| **VUS, unknown** | functional characterization first | stability + splice + function panel |

The separation of **synthesis · solubility · turnover · route · function** as distinct questions is a hard rule: a variant can be *made* but *unstable*, *stable* but *inert*, or degraded by different routes — and each implies a different lever. (See [`../../../framework/master/gold_is_in_the_details.md`](../../../framework/master/gold_is_in_the_details.md) and [`proteostasis_rationale.md`](proteostasis_rationale.md).)

## Worked example 1 — a folding-defective missense → chaperone lever

**p.Gln230Pro (Q230P):** fully buried SDR-core residue; ThermoMPNN +1.51 kcal/mol, ESM-2 the worst substitution at the site (see `variant_structural_pipeline.md`). Predicted mechanism: a protein-level lesion (the human observation is **normal transcript, protein not detected**). ⚠️ **The cause remains unresolved** — **impaired translation**, insolubility, or premature degradation are all open, and the primary source does not discriminate between them. → Lever hypothesis: **proteostasis/chaperone** support and/or a small-molecule stabilizer, *if* residual function exists. → Prioritized test: protein-stability rescue in variant-carrying primary cells (fibroblasts/LCL), discriminating degradation route (proteasome vs lysosome/autophagy — the route must be *measured*, not assumed; see the "defaults that bit us" table).

> ⚠️ Discipline note: a stabilizer only helps if stability, not function, is the defect — "stable but inert" is a demonstrated WWOX phenotype (e.g. the P282A observation in public literature). Function readout is mandatory, not optional.

## Worked example 2 — a canonical splice variant → ASO lever

**c.1057-2A>G** (canonical splice acceptor, intron 8 → exon 9; ClinVar VCV001418567): **SpliceAI acceptor-loss = 0.96** (high-confidence threshold 0.8), **MaxEntScan collapses 7.28 → −0.67** (native acceptor abolished), with a **cryptic acceptor gain (+8 nt, 0.64)** → aberrant splicing (exon-9 skipping and/or cryptic use), both toward frameshift → PTC → NMD / truncated protein = **null-like allele.** → Lever hypothesis (**conditional**): an ASO **does not repair the sequence** and cannot recreate the abolished acceptor; it could only redirect splicing toward a **productive outcome** if one exists — otherwise base/prime editing is the alternative. → Mandatory first step: measure the real transcript (junction-specific RT-PCR ± NMD block, amplicon sequencing) *before* any ASO-vs-editing choice; then minigene assay and ASO walk. The *Milasen* precedent is regulatory, not proof of amenability.

*(The two worked examples illustrate the two arms of the triage — chaperone-amenable missense, ASO-amenable splice. The point they make is that **lever assignment is an allele-level operation**: each allele is triaged on its own predicted mechanism, independently of whatever else a genome carries. They are deliberately not combined here.)*

## Why this is fundable and reusable

- It converts a **529-VUS** interpretability gap into a **ranked experimental agenda.**
- It is **gene-agnostic in structure** — the same mechanism → lever logic transfers to other rare monogenic diseases.
- It connects directly to therapeutic-development programmes (chaperone screening, ASO design, AAV gene addition) rather than stopping at annotation.

Artifacts: `WWOX_residue_rescuability.csv` · `WWOX_therapy_levers.csv` · `WWOX_pathogenic_missense_classified.csv` (added after clean-check).

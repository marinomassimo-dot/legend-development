---
name: legend-aso-designer
description: 'Design and triage support for HYPOTHESES of antisense oligonucleotides (ASO) targeting a WWOX splice-site variant of interest (e.g. c.1057-2A>G) — i.e. splice-switching / splice-correcting ASO (SSO), not just knockdown. Distills the transferable method from openASO (target-accessibility features: RNA structure/MFE/ensemble, eCLIP RBP occupancy, UTR-vs-coding, GC, conservation, variants) and from ASOptimizer (chemistry/modification patterns, gapmer vs SSO) and wires them into splice-correction logic, with epistemic discipline and a BLOCK-1 gate. Use it when the operator says "design an ASO for this splice allele", "can the splicing of c.1057-2A>G be corrected", "evaluate an antisense", "triage ASO candidates". READ-ONLY toward the canonical model; produces non-canonical HYPOTHESES in the hypothesis ledger. It is NOT clinical design nor medical advice: it is rationale support, to be validated in silico / wet-lab and with a treating team.'
---

# legend-aso-designer — ASO design / triage for a WWOX splice allele

Paths are relative to the workspace root.

## Why this skill exists
A WWOX splice allele of interest such as `c.1057-2A>G` hits the **splice acceptor** of the intron preceding the exon starting at c.1057. A splicing defect is, among all levers, one of those **potentially correctable with a splice-switching ASO (SSO)** — a concrete, near-term lever to "buy time until gene therapy". This skill turns that intuition into a structured, falsifiable rationale, without passing it off as ready therapy.

**Honesty about the source material** (`_external_repos/medical_ai/`, see its manifest):
- `ASOptimizer` is trained on **gapmer/knockdown** (IDO1, HIF1A) → useful for the **chemistry** part (modification patterns, gapmer vs SSO), **not** for splice-switching logic.
- `openASO` is a **target-accessibility feature** framework (ensemble RNA structure / MFE / base-pair prob, eCLIP RBP occupancy, UTR-vs-coding, GC, PhyloP conservation, SNP variants) → useful for **where** and **how well** an ASO can hybridize.
- The **splice-correction logic** (block a cryptic site, force/prevent exon inclusion, mask an ESE/ISE element) is **separate methodology**, anchored here to the real mis-splicing consequence of the variant — not assumed.

So: take the transferable method from the two repos as a **feature and chemistry checklist**, while the therapeutic rationale stays a HYPOTHESIS until supported by mis-splicing prediction and, ideally, data (RNA-seq / minigene).

## Human gate
Starts ONLY on explicit request. Does not design ASOs on its own initiative.
**It is NOT clinical design nor medical advice.** It is rationale support, to be validated in silico / wet-lab and with a treating team. No sequence produced here is "ready to use".

## Discipline — what you may and may not write
- **READ-ONLY** toward the canonical model, the biomarker/endpoint layer and the therapeutic strategy portfolio. Nothing enters the canonical layer except via `INGEST → DEEP_DIVE → COMMIT CANDIDATE → BATCH_COMMIT`.
- **WRITABLE** (carve-out, like the discovery ledger): the **therapeutic hypothesis ledger** — each ASO candidate is a `HYP-...` entry under **lever 1 (defect correction)**, tagged `IPOTESI`/`ESPANSIONE`, with a status. Reuse the template and rubric from `legend-hypothesis-forge`.
- Append-only, states: `generated` → `stress-tested` → `ranked` → `proposed-to-portfolio` → `parked` → `refuted`.
- **BLOCK-1 beats enthusiasm.** No false hope: an "elegant" ASO with no validation route is marked as such.

## Epistemic discipline (mandatory)
`DATO` (direct peer-reviewed source) / `INFERENZA` (convergence) / `IPOTESI` (reasonable, flagged) / `ESPANSIONE` (out of domain). Here almost everything is `IPOTESI`: say so. Never present a candidate sequence as "effective" without data — at most "predicted favourable on feature X".

## Procedure

**0. Load the context.** The WWOX genotype of interest (reference transcript MANE/NM_016373, exons/domains; alleles `c.1057-2A>G` and, where relevant, a missense such as `Q230P`), the working model, the discovery ledger, the therapeutic strategy portfolio (to avoid duplication), the hypothesis ledger.

**1. Define the splicing consequence (the pillar — do not skip it).**
Before any design, establish **what** `c.1057-2A>G` actually does to the transcript:
- Identify the exon/intron involved on the reference transcript (the lost acceptor is the one of the intron preceding the exon starting at c.1057).
- Predict the effect with dedicated tools (**SpliceAI**, MaxEntScan, etc.) and, if available, **real data** (RNA-seq, minigene assay): exon skipping? intron retention? activation of a **cryptic site**? frameshift/PTC → NMD?
- **This consequence determines the SSO strategy.** Without it, every design is blind → mark it a weak `IPOTESI` and propose this characterization itself as the first experiment.

**2. Choose the SSO strategy consistent with (1).**
- Cryptic site activated → SSO that **masks the cryptic site** to restore canonical splicing.
- Frame-breaking exon skipping → assess whether an SSO can **restore inclusion**, or whether the skipping is in-frame and tolerable (a different lever).
- Regulatory elements (ESE/ISE/ESS/ISS) → SSO that masks them to restore exon recognition.
- Remember: goal = **recover functional WWOX protein (even partially)**; the partial counts.

**3. Generate candidates and run the feature checklist.** Use `references/aso_design_checklist.md` (distilled from openASO + ASOptimizer + standard SSO knowledge): target accessibility, length/GC, chemistry (2'-MOE/LNA, PS backbone; for SSO **no RNase-H gapmer** that would degrade the target), specificity/off-target (BLAST against the transcriptome, avoid paralogues/homologies), immunostimulatory motifs (CpG), site conservation, RBP overlap.

**4. Stress-test + safety (BLOCK-1).** For each candidate: off-target risk, immunogenicity, CNS delivery (the real limits — barrier, distribution, intrathecal need), reversibility, and the therapeutic window. If a candidate hits a guardrail → `flagged`, it does not advance.

**5. Ranking + output.** Apply the rubric in `legend-hypothesis-forge/references/ranking_rubric.md`. Write ledger entries with: SSO strategy, assumed splicing consequence (with source/predictor), feature score, proposed chemistry, **minimal falsification experiment** (typically: minigene / RNA-seq on patient-derived or model cells to confirm splice correction and protein recovery), risks, score, status.

## Closing (mandatory in chat)
1. Assumed splicing consequence and its strength (DATO/IPOTESI) — if uncharacterized, say so first.
2. Chosen SSO strategy and the top 2–3 candidates with rationale.
3. BLOCK-1 safety signals and CNS delivery limits.
4. Next minimal experiment that would confirm or sink the hypothesis.
5. Disclaimer: **"Not clinical design nor medical advice. Every candidate is a HYPOTHESIS to validate in silico / wet-lab and with a treating team. No sequence is ready to use."**

## What NOT to do
- Do not declare a sequence "effective" without data: only "predicted favourable".
- Do not use gapmer/RNase-H chemistry for a splice-switching strategy (it would degrade the target instead of correcting it).
- Do not skip mis-splicing characterization: without it, the design is blind.
- Do not touch the canonical model or the therapeutic portfolio; do not self-authorize URGENT.

# Discovery methods — references that power the hunt

These methods come from established literature-based-discovery and drug-repurposing frameworks. No external tool is needed to use them: they are **reasoning lenses** that make lead extraction and self-propagation principled. Apply them during phases 2 (extract leads), 3 (compounding) and 5 (next-search) of the SKILL.

## 1. ABC model (Swanson — literature-based discovery)
The most powerful discovery is a **hidden link** between literatures that do not cite each other. Form:
- **A** = our fixed focus: WWOX-LoF / the disease phenotype / a known dysregulated pathway.
- **B** = an intermediate concept (metabolite, partner protein, process, gene).
- **C** = a valuable target: a measurable biomarker, a molecule, an approved drug.

Two modes:
- **Closed discovery**: A and C are already on the table, you look for the B nodes that explain them (strengthen/refute an existing lead).
- **Open discovery**: start from A, find a strong B in the paper, and ask *which new C nodes* that B opens — C nodes not yet **connected** to A in the literature. That is the needle.

> Swanson's historical example: Raynaud (A) — blood viscosity (B) — fish oil (C), a connection never published before. For us: WWOX-LoF (A) — <metabolite/pathway emerging in the paper> (B) — <approved drug that modulates it> (C).

**Operational use**: every lead carries an `ABC map: A=… · B=… · C=…` field. The next-search agenda comes from the most-connected B nodes: "which other C nodes bind this B?".

## 2. Signature reversal (Connectivity Map / LINCS L1000)
Principle for **MOL/REPO** leads: a plausible therapeutic molecule is one that **reverses the transcriptional signature** of the disease. If WWOX LoF (or the paper's model) raises one set of genes and lowers others, the ideal candidate is a compound whose signature does the opposite.
- If the paper provides **DEGs / differential genes / a pathway signature** of the dysregulation, note it: it is a ready query for signature-reversal repurposing (conceptual, or real via CMap/LINCS).
- Lead field: `Signature to reverse: ↑{genes} ↓{genes}` when available. A MOL that returns those genes toward baseline is a strong lead, not a weak ESPANSIONE.
- Known caveat in the literature: connectivity-scoring reproducibility is variable → it stays INFERENZA/IPOTESI until directly validated.

## 3. Evidence graph: supports / refutes / neutral (from RareAgent)
In rare diseases with no priors (this case) the risk is confirmation bias: you see only what confirms the hypothesis. Before a lead rises in status (`open`→`maturing`), interrogate it from three sides:
- **Supports**: what in the paper (or the ledger) supports the lead.
- **Refutes**: what weakens it — non-physiological dose, distant model, small effect, off-target route.
- **Neutral/unknown**: what would be needed and is missing.
A lead that survives the "refutes" side is much more solid. Note all three sides in the `Evidence` field.

## 4. Heuristic distillation (compounding the method, from RareAgent)
Do not compound only knowledge, compound also the *how*. When a reasoning path works (e.g. "Methods with fibroblast assays give the best BIO leads"), distill it into a reusable line in the ledger's **Learned heuristics** section. Future sessions start higher.

## 5. Reasoning-chain provenance (from HypER)
Every non-canonical lead carries an **explicit reasoning chain**, not just the conclusion: "from [paper datum] → [inferential step] → [lead], tagged IPOTESI because [what is missing]". Distinguishing valid from invalid chains is half the value. Field `Reasoning chain`.

## 6. External knowledge graphs to query (next-search)
To validate or seed REPO/MOL leads without starting from scratch, these graphs already map gene–drug–disease–pathway:
- **DRKG** (gnn4dr/DRKG) — 13 entity types, drug/gene/disease/pathway; exploration notebooks.
- **PrimeKG** (Zitnik lab) — ~129k nodes, includes Pathway/Exposure/Phenotype.
- **Open Targets** — target–disease associations + genetics + drug tractability.
- **Hetionet** — the original graph of the Rephetio project.
Use: given a target/partner emerging in the paper, look in the graph for approved drugs that hit it → a REPO lead. Record it as an `NS-…` query in the ledger. (Manual/web consultation; the skill does not query them automatically.)

## 7. Causal statements + assembly (from INDRA, gyorilab/indra)
Mechanistic value grows if leads are not prose but **atomic causal statements**, composable as a network:
- Form: `Subject — relation — Object`, e.g. `WWOX(loss) —decreases→ sphingolipid_X`, `sphingolipid_X —required_for→ myelination`. Several chained statements = a mini-pathway. Note the statement in the lead's `Causal statement` field.
- **Assembly** (do this periodically on the ledger, INDRA-style): (a) *dedup* — merge equivalent statements from different papers; (b) *contradiction resolution* — if two papers give opposite relations, mark `conflicting` and keep both sources; (c) *missing-link inference* — if A→B and B→C, propose A→C as an IPOTESI (it is ABC in causal form); (d) *belief score* — the more independent, high-quality sources support a statement, the higher the belief (0–1, qualitative: low/medium/high). A lead does not rise to `maturing` with low belief and zero corroboration.
- Why it matters for the case: an assembled causal network shows **where to intervene** — the node whose correction propagates furthest downstream is the best therapeutic/biomarker target.

## 8-bis. Structural / variant-effect-prediction lens (case-specific biomarker generation)
The most direct and translatable biomarker route starts from the **real patient variants**, not from cohorts. For each variant of interest (or of the paper) choose the in-silico tool by variant *type* and use it as a **hypothesis generator**, never as a datum:
- **Missense** → AlphaFold3 / AlphaMissense / ΔΔG (FoldX, Rosetta): predicts destabilization/folding. Map the residue first onto the **domain**, then onto the **known active-site residues** — "it is in the catalytic domain" is not enough. (In WWOX the SDR catalysis is S281 + the YxxxK motif Y293–K297, NAD via GxxxGxG: a residue *inside* the SDR but *not* catalytic, e.g. Q230, acts by **folding destabilization → unstable protein**, not by direct catalytic loss → the biomarker readout becomes **protein abundance/stability** [Western, pulse-chase], not enzyme activity.) Retrieve the point AlphaMissense score from Ensembl VEP/dbNSFP instead of estimating it.
- **Splicing** (±1/±2 sites, introns) → SpliceAI / Pangolin / MMSplice: predicts skipping/retention/cryptic site and outcome (PTC→NMD vs truncated).
- **PPI / complexes** → AF3-multimer (e.g. WWOX–ATM, WWOX–p53/ERBB4): predicts whether an interface holds → separates "WWOX absent" from "WWOX present-but-enzymatically-dead" (changes the intervention class: stabilizer vs metabolic bypass vs gene therapy).
- **Golden rule**: the predictive output is **IPOTESI**. The real biomarker is the **wet readout it names** — protein (Western), activity (SDR/oxidoreductase assay), transcript (RT-PCR ± NMD block), DDR competence (γH2AX/comet) — on **patient fibroblasts/iPSC**. Tier 1/2 because it measures WWOX itself.
- The **convergence of multiple alleles on the same domain** is itself a discovery: it raises the priority of that domain's pathway (in this disease model: multiple alleles of interest on the SDR domain → the metabolic/redox axis becomes more central).

## 8. Hypothesis → experiment (from Robin, Future-House/robin)
Robin does not stop at the hypothesis: it proposes the experiment that would test it and analyzes the readout (that is how it found ripasudil for dAMD). Make every **MOL/REPO** lead actionable:
- `Proposed experiment` field: the minimal experiment that would confirm/deny the lead, **feasible in the case context** where possible (patient fibroblasts, organoids, markers measurable in blood/CSF), with the **expected readout** and expected direction.
- This turns the ledger from a list of intuitions into a **pipeline of testable hypotheses** — the bridge to a real conversation with clinicians/researchers.

# ASO design checklist — distilled from openASO + ASOptimizer + SSO practice

Every item is a triage criterion. Source in brackets: [openASO] target-accessibility features; [ASOptimizer] chemistry/modifications; [SSO] standard splice-switching practice; [safety] guardrail. Always mark whether a judgement is `DATO` (predicted/measured) or `IPOTESI`.

## 1. Target accessibility [openASO]
- **RNA structure:** prefer **open/unpaired** regions. Use an *ensemble* model + base-pair probability, not just MFE (RNA is an ensemble). A target site with low pairing probability = better access.
- **RBP occupancy (eCLIP):** avoid sites densely occupied by RNA-binding proteins (competition), unless the RBP is itself the functional target.
- **UTR-vs-coding context:** relevant for stability/translation; for SSO the position relative to exon/intron/regulatory elements matters.
- **Conservation (PhyloP):** a conserved site is often functionally important → consistent for an SSO targeting splice elements, to be avoided if it risks collateral functions.

## 2. Sequence properties [openASO/ASOptimizer]
- **Length:** typically 15–22 nt (SSO often 18–20).
- **GC%:** a middle window (avoid extremes: too low = poor affinity, too high = structure/aspecificity).
- **Self-structure/homodimers:** avoid internal hairpins and self-complementarity.
- **Immunostimulatory motifs:** avoid unmethylated **CpG** (TLR9 activation) and problematic stretches [safety].

## 3. Chemistry / modifications [ASOptimizer]
- **Mode = splice-switching (SSO):** use **steric-block, not RNase-H** chemistry. NO gapmer (a DNA-gap gapmer recruits RNase-H and **degrades** the pre-mRNA: wrong for correcting splicing).
- **Backbone:** phosphorothioate (PS) for stability/nuclease resistance.
- **Sugars:** 2'-O-methoxyethyl (2'-MOE, cf. nusinersen), 2'-O-methyl, or LNA/PNA/PMO (morpholino) — full-modification for steric block.
- ASOptimizer models the effect of modifications on efficacy: use it as a **prior on chemistry**, not a verdict (trained on gapmer knockdown, a different domain).

## 4. Specificity / off-target [safety]
- **BLAST** the candidate against the human transcriptome: no perfect/near-perfect off-target match.
- Beware **paralogues/homologies** and partial targets that trigger unwanted knockdown.
- Prefer sites with **low variability (SNP)** in the target [openASO], so as not to lose hybridization on common variants.

## 5. Delivery & context [safety]
- **CNS:** naked ASOs do not cross the barrier → typically **intrathecal** (cf. nusinersen) or conjugated approaches; it is a real constraint, not a detail.
- **Reversibility/repeatability:** repeated dosing; a different profile from one-off GT → it can be a bridge lever *toward* GT.
- **Window:** the earlier the intervention on time-sensitive variables, the better.

## 6. Minimal validation (the falsifying experiment) [SSO]
Typical order, cheapest first:
1. **Mis-splicing prediction** (SpliceAI/MaxEntScan) — confirms what the defect is.
2. **Minigene assay** — reproduces the aberrant splicing and tests the SSO's correction in vitro.
3. **Patient-derived cells** (fibroblasts/iPSC) + **RNA-seq**: endogenous splice correction + recovery of **WWOX protein** (Western).
4. Only then: models and translational considerations.

> Golden rule: a candidate with no route to points 1–3 is not a mature hypothesis. Mark it a weak `IPOTESI` and propose the test as the first step.

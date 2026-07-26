# Batch Inferential Sweep rubric

## Output classes

| Class | Meaning | Action |
|---|---|---|
| `CANONICAL_CANDIDATE` | direct WWOX, strong primary paper/review, likely value for claim/registry | canonical deep-dive |
| `DISCOVERY_ONLY` | useful mechanism but not mature/canonical | discovery ledger |
| `REPURPOSING_SEED` | target/pathway/molecule/therapy named | hypothesis-forge; safety if a molecule |
| `SAFETY_SIGNAL` | risk, toxicity, contraindication, BLOCK-1, evidence correction | priority review |
| `ENDPOINT_SEED` | distal endpoint or biomarker candidate, often Tier 3 | endpoint/biomarker discussion |
| `READ_QUEUE_TAIL` | no signal **from keywords** on abstract/title — it says only that keywords see nothing, **not** that the study has no value | **reading queue, tracked debt. To be read, later. NEVER discarded.** |

> 🔴 **No row of this table authorizes not reading a study.** Classes order the queue; they do not close it.
> A study's disease context is **never** grounds for down-ranking: **oncology is ~20 years ahead** on WWOX mechanics (folding, stability, degradation routes, partners) and that is **where the mechanism of the allele of interest lives**; **adult neurology** brings shared pathways and molecules already tested in humans; **WOREE** papers are the most phenotype-consistent but largely **descriptive** — **consistency ≠ usefulness**.
> Real cost of the error: **2026-07-12**, a thyroid-cancer paper classified at the back contained the degradation route of Q230P. See `CLAUDE.md` → *parity of sources*.

## LEGEND evolutionary boosts

Raise priority if the record touches:
- Q230P, SDR, folding, proteostasis, chaperones, stabilizers;
- c.1057-2A>G, splice, ASO/SSO;
- WWOX gene therapy, AAV, CNS delivery, WPRE/promoter/dose;
- MYC/WNT/Hippo;
- neuroinflammation, microglia, astroglia, cytokine;
- Zfra/peptides;
- GSK3b/tau/lithium;
- HIF1A/p73/metabolism/redox/mitochondria;
- NMDAR, excitability, sleep/network-state;
- JAK/STAT, PD-L1, macrophage polarization, SCD5/OA;
- Bcl-XL/Mcl-1, apoptosis/proteostasis safety.

## Penalties

Penalize:
- GWAS association without function;
- oncology without WWOX mechanism;
- generic reviews already covered;
- animal/agricultural trait without a bridge;
- interventions without CNS/pediatric plausibility;
- molecules with immunosuppressive/oncogenic risk without a strong bridge.

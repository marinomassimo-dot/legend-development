# Therapeutic Levers for WWOX / WOREE — "Buying Time"

**Goal:** reduce WWOX-dependent damage until a definitive therapy, using any actionable lever — even partial.
**Method:** PubMed sweep (15 queries, 195 unique articles), structured abstract extraction, trial check on ClinicalTrials.gov. Every lever is anchored to a real PMID.

> Public research synthesis. No patient referenced. **Not medical advice** — every molecule named must be evaluated solely by a treating clinical team with the full picture. Preclinical (mouse/in-vitro) evidence does not guarantee human efficacy or safety.

## Honest overview

- **No WWOX-specific clinical trial exists** (ClinicalTrials.gov: only the rare-disease registry NCT01793168). No approved therapy for WOREE.
- **But several real levers exist**, on three time horizons: (A) *now*, to protect the developmental window; (B) *months*, mechanistically-grounded repurposing; (C) *the cure*, AAV gene therapy already demonstrated in mouse.
- The "buy time" rationale is scientifically valid: WWOX regulates myelination, network excitability, and neuroinflammation — all **time-dependent** processes where early intervention protects development.

## A — Act now (available; protects the window)

- **A1. Targeted seizure control — Vigabatrin.** In a WWOX-DEE case, vigabatrin reversed infantile spasms (PMID **39101447**, 2024). Symptomatic, does not modify WWOX; the most solid "buy-time" base.
- **A2. Lithium (GSK3β inhibition) — a repurposing signal whose genotype specificity was tested and not found.** In Wwox-deficient mice the source reports **increased GSK3β activation**, evidenced by **Ser9 dephosphorylation**, in cortex, hippocampus and cerebellum (Fig. 7c). ⚠️ **That densitometry carries no statistical test, no n and no error bars** — one lane per genotype per region under a legend declaring *«The representative results of four independent experiments are shown»* — so the direction is **attributed to the source, not established here**; **total GSK3β abundance is `NOT_TESTED` in either direction and neither cited source reports it as elevated** (2026-09-27, `BATCH_20260927_004`, `CC-20260826-GSK3B-S9-AXIS-01` `D9`); **lithium inhibits GSK3β and abolishes seizures** (PMID **32000863**, Acta Neuropathol Commun 2020). Acts *downstream* of WWOX loss → **genotype-agnostic**. The effect is a **general anticonvulsant effect, not a WWOX-specific rescue** — lithium suppressed PTZ seizures in all three genotypes including wild type (Fig. 7d; boundary from `TX-005` / `CLAIM 016`, `CC-20260826-LITHIUM-BOUNDARY-01`). Lithium is available and used in pediatrics (with tight monitoring: therapeutic window, thyroid, kidney). A preclinical hypothesis to discuss with a clinical team — not medical advice.

## B — Mechanistically-grounded repurposing (months; needs validation)

- **B1. GSK3β / JNK / MEK-ERK (Tau) axis.** WWOX loss is **associated with reduced GSK3β Ser9 phosphorylation**, read as activation by the authors (⚠️ [[claim_registry_current#CLAIM 035]] holds the WWOX brake to be **S9-independent** and predicts that a pS9 western returns a **false negative** — the two readings **exclude each other** on this axis; 2026-09-27, `BATCH_20260927_004`, `CC-20260826-GSK3B-S9-AXIS-01` `D10`); JNK and ERK → Tau hyperphosphorylation/aggregation; inhibitors (SP600125 anti-JNK, PD-98059 anti-MEK) block it in vitro (PMID **22193544**, **15126504**).
- **B2. Neuroinflammation control.** In the partial-LoF P47T mouse (PMID **36828035**) hippocampal astrogliosis rises with age and microglial morphology degrades further with age; whether microglial abundance progresses was not tested, and the statistics use subfields or single cells from n = 3 mice (`CLAIM 006`, narrowed by `BATCH_20260926_ALDAZ`). Relevant to hypomorphic alleles. No WWOX-specific drug identified yet.
- **B3. Wnt/β-catenin.** WWOX blocks Dishevelled nuclear translocation; its loss de-represses Wnt/β-catenin (PMID **19465938**). Downstream lever, hypothesis to verify.
- **B4. Zfra peptide (partner stabilization).** 31-aa peptide; reduced neuroinflammation and restored memory in Alzheimer mice (PMID **35883580**, **34359949**, **30158849**). *Theoretically* could stabilize residual function of a hypomorphic missense — but evidence is Alzheimer/cancer, none in epilepsy/WOREE. Experimental, indirect.

## C — The cure in progress (definitive; advanced preclinical)

- **C1. Neuronal AAV9-WWOX gene therapy — fixes both alleles.** AAV9 with WWOX cDNA under the neuronal Synapsin-I promoter (**AAV-SynI-WWOX**) improved **survival and epileptiform activity**, and improved myelination **on the comparisons the study draws** (PMID **34747138**, EMBO Mol Med 2021). 🔴 On the single panel where treated animals are compared with wild type — unmyelinated axons per field, WT ≈26 vs treated ≈52 — the comparison is **significant against the rescue**; on the remaining myelin panels the wild-type-versus-treated comparison is **not drawn**, so the residual gap is `NOT_TESTED` (`deepdive_manifests/PMID34747138.json` entries 9–10; applied 2026-09-27 from `CC-20260826-AAV9-ENDPOINT-SPLIT-01` D-L1). By replacing functional WWOX in neurons, it bypasses any allele combination.
- **C2. Proof that restoring WWOX reverses the phenotype.** In WOREE-derived brain organoids, WWOX re-expression corrected cortical/molecular CNS anomalies (PMID **34268881**, EMBO Mol Med 2021).
- **C3. Splice-switching ASO — conditional.** For a canonical splice-acceptor variant (e.g. c.1057-2A>G), **an ASO does not repair the sequence** and cannot recreate an abolished acceptor site. It could only *redirect* splicing if a **productive outcome** exists (an in-frame skip, a usable cryptic site) — which must be demonstrated on the real transcript first. If the sequence itself must be corrected, base/prime editing is the alternative. The *Milasen* n-of-1 precedent is regulatory, not proof of amenability. Requires n-of-1 development.

## Models to test on (infrastructure)

- **P47T knock-in** (PMID **36828035**): phenocopies SCAR12, survives >1 year (vs ~1 month for KO) → ideal model to test repurposing drugs on a **hypomorphic allele**.
- **WOREE patient-iPSC organoids** (PMID **34268881**): platform for n-of-1 screening.

## Practical priorities (for clinical discussion)

1. **Now:** optimize seizure control (vigabatrin among options) — protects the myelin/network window.
2. **To discuss with the team:** lithium — a general anticonvulsant with a WWOX-adjacent mechanistic rationale that has not been demonstrated; no developmental endpoint has ever been measured under lithium in any WWOX system — tight monitoring.
3. **To build:** patient-iPSC/organoids as an n-of-1 bench for repurposing and allele-specific ASO.
4. **Goal:** AAV9-WWOX gene therapy — effective in mouse **on survival, spike-wave discharges and gliosis, at high dose, in the P0–P5 window**; **motor and locomotor behaviour is not impaired and not normalised**; cognition and developmental trajectory were **not measured** (applied 2026-09-27 from `CC-20260826-AAV9-ENDPOINT-SPLIT-01` D-L2) — support the path to the clinic.

Artifacts: `WWOX_therapy_map.png` · `WWOX_therapy_levers.csv` (added after clean-check; the private column linking levers to an individual is removed).

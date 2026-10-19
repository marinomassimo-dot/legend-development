# COMMIT CANDIDATE — CC-20261019-SCIENTIST-B-G2-FRUCTOSE-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-b`, metabolic batch 2026-10-19 group G2, branch `task/METAB-G2-B-20261019`.
**context_policy:** `SOURCE_FIRST` for every reading cited (first reads); registry comparison admitted after each first pass.
**target_wm_version:** `WM_v7.20_2026-10-04`. **Change class:** **MINOR** — new paper-registry records and evidence-boundary notes; no claim status, no baseline claim reversed, no working-model block change. The legend-locator-audit trigger is therefore not met; the triples below are supplied for a later blind audit.
**Not medical advice.**

## Target

`paper_registry_current.md`: two new PAPER records (40500435, 37907746); no claim touched.

## What is missing now

The fructose arm of group G2 has no record. Two transferable mouse papers were read.

| Source | What it adds | Receipt |
|---|---|---|
| Wang 2025, Nature (40500435) | Neonatal high fructose via microglial GLUT5 lowers microglia phagocytosis (hexokinase route, mitochondrial HK2 localisation), raises whole-brain neonatal lactate about 2.7-fold (Figure 3b, N 4 to 5), reversed by GLUT5 deletion; high glucose control diet has no effect; myeloid GLUT5 deletion rescues phagocytosis but not microglia number; NOR and Barnes maze disagree; WWOX absent | `FTR-20261019-40500435-01` (partial; Methods skimmed) |
| Li 2023 (37907746) | Endogenous fructose in db/db hippocampus metabolised by KHK in microglia, NOX4 and ROS; hippocampal AAV shRNA is not cell-type specific; methods state human-genome mapping for mouse RNA-seq; loose DE threshold (18,201 of 55,450 transcripts); db/db hyperglycaemia is the opposite of the Wwox-null hypoglycaemia | `FTR-20261019-37907746-01` (screening depth) |

## Proposed discovery leads

1. **Lactate confounder** (INFERENZA): a diet exposure alone raises neonatal brain lactate nearly three-fold through a microglial transporter; a lactate difference in a Wwox-null brain does not by itself indicate a HIF1A-driven glycolytic shift. Falsifier: matched-diet Wwox-null versus wild-type brain lactate with cell-type resolution.
2. **Two microglial fructose routes disagree** (ESPANSIONE): hexokinase to F6P in neonatal microglia that become hypo-phagocytic (Wang 2025) against KHK to NOX4-ROS in activated microglia of hyperglycaemic adults (Li 2023); no single rule "fructose makes microglia X".
3. **Priority** (decision): fructose/KHK is not a WWOX-DEE priority unless Wwox-null microglia show high Slc2a5 or a phagocytosis deficit (REVIVAL_TRIGGER).

## Ordering

Receipts `FTR-20261019-40500435-01` and `-37907746-01` first.

### LOCATOR TRIPLES FOR BLIND AUDIT

| PMID | entry | proposition | verbatim snippet | anchor |
|---|---|---|---|---|
| 40500435 | entry 2 | SPECIFICITY: a high-glucose diet had no effect on phagocytosis; the fructose effect is not a generic sugar excess effect in this model. | we observed no significant difference in microglia phagocytic activity in neonates born to and nursed by dams on high glucose diet (Ext | Results |
| 40500435 | entry 6 | Figure 3b: the whole-brain total lactate pool in HF-diet wild-type neonates is about 11 umol/g against about 4 in controls and about 4 in GLUT5-null HF pups (N 4 to 5 per group); a diet exposure alone moves brain lactate nearly th | [figure attestation - pixels cannot be quote-matched] Figure 3, (a) design of [2-13C]-fructose tracing in P7 pups by NMR; (b) brain [2-13C]-fructose, [2-13C]-lactic acid and total lactic acid pool in  | Figure 3b, native JPEG |
| 40500435 | entry 9 | Myeloid-specific GLUT5 deletion rescues phagocytosis but not microglia number, so the number reduction is not explained by the same cell-intrinsic route. | myeloid-specific deletion of GLUT5 completely reversed the HF diet-induced microglia phagocytosis defect, but not microglia numbers, ob | Results, cKO |
| 37907746 | entry 2 | Methods state that reads were mapped to the Homo sapiens genome for mouse hippocampus and mouse BV2 samples, an apparent error that is not corrected in the text. | After cleaning reads and mapping them to the genome of Homo sapie | Methods, RNA-seq |
| 37907746 | entry 3 | With that threshold, 18,201 of 55,450 transcripts are called differentially expressed (9,323 up, 8,878 down), a third of the annotated transcriptome. | Transcriptomic analysis detected 55,450 genes, of which 9,323 were upregulated and 8,878 were downregulated (F | Results, omics |
| 37907746 | entry 6 | The in vivo knockdown uses an AAV2/6 shRNA injected into hippocampus under a CMV promoter, not a microglia-specific promoter or a conditional allele. | Recombinant adeno-associated virus (rAAV2/6 m) expressing U6-driven shRNA and CMV-driven EGFP (rAAV-U6-sh | Methods, viral vectors |


---

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261019_001` · 2026-10-19 · ACTOR_ID `orchestrator` (stated assumption, batch integrator)
**Working model:** WM_v7.20 -> WM_v7.21 (MINOR)
**Class re-judged (§7):** MINOR
**Blind locator audit:** not run — no baseline claim is narrowed and no MAJOR contingency is declared; the candidate's locator triples are carried for a later audit.
**What landed:** 2 PAPER record(s) (PAPER 276, PAPER 277) with their LIT records. 
**Status / Type / Summary:** unchanged by this candidate.
**Not medical advice.** Class level only; no individual-level record is carried.

# Does the WWOX-KO organoid carry the ATF4 / integrated-stress-response signature that the Lucas-Clarke 2026 fly chain predicts? — gene sets and prediction fixed

Declared 2026-10-26 by the Orchestrator. Exploratory. Not medical advice; no dose, route or suitability.
Everything below that is not WWOX data is NOT WWOX EVIDENCE.

## Disclosure that comes before the prediction
Before this file was written I read 23 genes of this kind (ATF4 targets, ISR/UPR genes, LDH genes, PDK1, PDHA1) off the padj<=0.05 list to
decide whether a test was worth fixing. LDHA is up (+0.91, padj 5e-6); the ISR targets CHAC1 (-0.86), TRIB3 (-0.69) and PHGDH (-0.36) are
down, and ATF4, ATF5, DDIT3, ASNS, PSAT1, SLC7A11, XBP1, HSPA5 are not on the list. So the direction of the main result is already
partly seen. What follows is therefore NOT a blind prediction for those genes; it fixes the sets and the reading rules before the
set-level tests and the culture-time slopes, which were not looked at.

## The question
Lucas-Clarke et al. (Brain Communications 2026, PMID 42909904) report in Drosophila that, with an Abeta42 transgene, neuronal Wwox knockdown
raises Atf4 and Ldh and lactate, that reducing Ldh genetically rescues locomotion, and that neuronal Wwox overexpression leaves lactate
unchanged. LEGEND's other chain (HIF1A -> PDK -> PDH) found glycolytic targets up and PDK1 down in the KO organoid. This asks whether the
ATF4-driven route is visible in the one WWOX-knockout human neural transcriptome held, WITHOUT any Abeta42 load.

## What this can and cannot say
- CAN say: whether the transcript signature of an ATF4 response, and of LDH up-regulation, is present in KO organoids, and whether it
  falls with elapsed culture time in WWOX-unperturbed spheroids.
- CANNOT say: whether Atf4 protein or phosphorylation of eIF2alpha changes (ATF4 is translationally controlled and eIF2alpha
  phosphorylation is invisible to a transcriptome); that lactate changes; that anything is Abeta42-dependent; that a fly result transfers.
  The organoid carries no Abeta42, which is exactly the context in which the fly effect is reported, so a negative here is not a
  contradiction of the fly result.

## Gene sets, fixed now
- ATF4 / ISR canonical targets (amino-acid response and stress): ATF4, ATF5, DDIT3, CHAC1, TRIB3, ASNS, PSAT1, PHGDH, PCK2, SLC7A11, SESN2, GADD45A.
- Unfolded-protein response branches: XBP1, HSPA5, HSP90B1, DNAJB9, EIF2AK3, EIF2AK4, EIF2S1, PPP1R15A.
- LDH: LDHA, LDHB, LDHC.
- Methionine / cysteine pathway (the other change the paper reports): MAT2A, MAT2B, AHCY, CBS, CTH, GCLC, GCLM, GSS, SLC7A11.

## Reading rules (fixed now)
- A set is called coherent only if its mean KO shift exceeds 10,000 random same-size sets (the same set-level test as before; post-selected by construction).
- A gene is called time-confounded only if its between-line interval on log10 days in GSE150123 excludes zero, with five informative lines.
- ATF4 transcript flat is NOT evidence against an ATF4 response (translational control); ATF4-target transcripts are the readout.
- No result here is read as supporting or contradicting the fly chain, because the context (Abeta42) differs.

---

# RESULT (appended 2026-10-26, after the run; the gene sets and reading rules above are unchanged)

Script: `hif1a_pdk_chain.py --sets isr` (the same reproducible script as the HIF1A-PDK analysis, with the gene sets selectable; no second
script). Set-level, 10,000 draws, seed 20261025, expressed universe 19,694 genes (universe mean shift +0.086). The disclosure at the top
applies: LDHA up and the CHAC1/TRIB3/PHGDH down had been seen before the sets were fixed, so the per-gene direction of those genes is not a
blind result; the set-level tests and the culture-time slopes were not looked at beforehand.

| set | n | mean KO shift | P(random <= observed) | P(random >= observed) |
|---|---|---|---|---|
| ATF4 / ISR canonical targets | 12 | **-0.288** | **0.0005** | 0.9996 |
| UPR branches | 8 | +0.051 | 0.43 | 0.57 |
| LDH (LDHA, LDHB; LDHC absent) | 2 | +0.559 | 0.945 | 0.055 |
| methionine / cysteine pathway | 9 | +0.011 | 0.30 | 0.70 |

## What it shows
- **The ATF4 / ISR target set is LOWER than chance in the KO organoid**, not higher: CHAC1 -0.70 (padj 2e-5), TRIB3 -0.64 (padj 0.003), PHGDH
  -0.32 (padj 0.04), SESN2 -0.35 (padj 0.03); ATF4, ATF5, DDIT3, ASNS and the other targets are not individually significant. ATF4 transcript
  is flat, which says nothing about ATF4 (translational control).
- **Not an age artefact.** The three ISR genes that fall with elapsed culture time in WWOX-unperturbed spheroids (ATF4, ASNS, PCK2) have a
  mean KO shift of -0.19, while the eight with no detectable time slope have -0.31; the lowering is carried by genes that culture time does not move.
- **LDHA is up** (+0.75 by the script's per-gene shift, +0.91 on the authors' DESeq2 list, padj 5e-6) and falls with culture time
  (-1.89 per log10 day, interval excluding zero), so as in the glycolytic case its elevation is as consistent with a less advanced tissue as with
  a WWOX effect. LDHB +0.37 is not significant.
- **UPR branches and the methionine / cysteine genes are not different from chance.**

## What it does not show
It is not evidence against the fly result. The fly effect is reported with an Abeta42 transgene, and this organoid carries none; a
missing ISR signature here says only that the signature is not present WITHOUT that load. It also cannot see the phosphorylation of eIF2alpha
or ATF4 protein, which are the actual steps of the integrated stress response. Six libraries; genotype and composition confounded; one
laboratory; different species and different disease context. Across the two analyses nine sets were tested (five for the HIF1A-PDK chain, four here) and none is corrected for
multiplicity. Against the Bonferroni threshold for nine, 0.05/9 = 0.0056, two sets clear it, and they point in opposite directions: the HIF1A
glycolytic targets (higher than chance, P = 0.0026) and the ATF4 / ISR targets (lower than chance, P = 0.0005). The earlier wording that the ISR set was the only one to clear it was wrong.

## Reading, at the strength it has
EXPLORATORY. In the one human WWOX-knockout neural transcriptome on hand, WITHOUT amyloid, the ATF4-driven route proposed in the fly
(Wwox down -> Atf4 up -> Ldh up) has no transcript signature, and the ATF4 target set is lower than chance; LDHA is up but is also what
a less advanced tissue would show. Taken with the HIF1A-PDK result (glycolytic targets up, PDK1 down), two different routes to a raised
glycolytic / lactate state have now each been checked and neither has its mid-chain link in the organoid. If the fly mechanism applies to the
human WWOX loss-of-function population it would need a second hit that the knockout alone does not supply.

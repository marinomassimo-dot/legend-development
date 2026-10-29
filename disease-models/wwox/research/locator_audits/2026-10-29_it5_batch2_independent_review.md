# Independent hostile review of BATCH_20261019_026 (registries of the iteration-5 results), 2026-10-29

Producer: integrator worker. Reviewer: independent subagent from the sources, mutation-tested the new test class. Verdict: R1-R6 and R8 pass (no claim created or reversed; working model unchanged; ledgers append-only; no re-identification); R7 partial (exact strings only); six low defects (gene-list attribution, knockdown wording, COMPUTATIONAL_RESULT label, PDH-restraint caveats, batch record status, test pins) sent back for repair.

# Independent review of BATCH_20261019_026 (scientist-d), range f0150aa4~2..f0150aa4, HEAD df960074
Read-only; mutation tests run on a copy under scratchpad/mut. No e-mail, no spend.

| # | Check | Verdict |
|---|---|---|
| R1 | No claim created/reversed; WM unchanged | PASS. working_model_current.md diff = 0 lines. Claim registry: one in-line insertion in CLAIM 014 (word-diff shows additions only); Status/Type/Summary untouched. |
| R2 | Epistemic levels | PASS with 2 low defects (D1, D2). n=1/arm, ISR "unresolved", PDK1 sign-only inside null, GSEA sign, I01 statements all match sources. |
| R3 | DIS-004 | PASS. Header still WITHDRAWN; UPDATE says "NOT reversed"; A01 reading matches P8 README and the blind audit (butyrate ~1.05, class-I does not reproduce, document-dependent, HDAC6 open, mechanisms not established). |
| R4 | DL-MECH-170 gap | PASS. 0.6 mM / 18 nM = 4.5, /6.4 nM = 5.0; >5 mM / 7.5 nM (Cav3.3, the channel of the flux bound) = 5.8. Endpoints-differ caveat present. |
| R5 | Append-only | PASS. Four ledgers: additions only. Only deletions are replace-within: PAPER 431 "no later reading has" (falsified by the new receipt), LIT line, dossier PMID31543760 sentence (explicit "superseded" note), coverage README (marked "superseded explanation"). |
| R6 | No re-identification | PASS. Added text names only published-literature alleles (c.1057-2A>G reference class, c.517-2A>G from a published homozygote, a published cancer proband in Zhang 2025); no combination, no individual data of the project. |
| R7 | New test class | PARTIAL. Real but exact-string pins (see below). |
| R8 | Process | PASS. Batch record, manifest (last_batch_commit_id, trigger), state_history scope coherent. legend_lint: WARN, 0 BLOCK, no WARN introduced by the batch that I can see (UNLINKED_SUPPORT warns are pre-existing); growth_anchors check: PASS; fulltext_receipts verify: OK 885 receipts, tail anchored; public_release_gate: PASS, BLOCKS 0 (REVIEW items pre-existing, published-study parent-of-origin pairs). git status clean after my runs. |

## Source checks I did myself
- Paper 31543760 Supplementary Data_Sheet_1: Table 2 "Enrichment in phenotype hNPC_WWOX_high", 44 rows, 0 negative; Table 3 "phenotype hNPC_WWOX_del", 108 rows, 108 negative (column header "Enrichment score"). Counts and the "text says 109" note reproduced; sign statement (negative = enriched at the silenced end, not depleted) is consistent. Caveat correctly stated: the label order of the run is not printed.
- hNPC RESULTS and systems comparison: PDK1 -0.39 / -0.67, p about 0.30 / 0.49, HIF1A -0.27 / -0.11, neuron PDK1 +0.44 (+-0.45), ISR -0.33 / +0.64 / +1.32, CHAC1 t -11.6, TRIB3 -4.1, SESN2 -4.3, WWOX 3.35 vs 2.90 TPM, ATF4 6 vs 41 tags, PSAT1 up in all: all match. "Opposite signs" in the source table was already softened to "unresolved" in the ledgers, as the source's own verification note requires.
- P9: glucose down in diabetic adults, minipigs, cirrhotic+healthy (modest in both, group difference null), reversed only in septic mouse; PDH restraint in two non-WWOX models; closing condition PDHA1 phospho/PDH activity as genotype-by-inhibitor interaction: all match. P8 numbers (1.8-2.4 fold, 2.1-3.7 soluble pool, butyrate ~1.05, HDAC6 PAH precedent, 2 sham) match README and the P8 blind audit.
- P5: apinocaltamide 6.4/18/7.5 nM, state dependence 75-fold (Ki 20 vs Kr 1500 nM, Cav3.3 CHO), ethosuximide >5 mM Cav3.3 and 0.6 mM, 1.5 mM arithmetic bound: match.

## R7 mutation results (temp copy, baseline 5/5 OK)
Caught: appending "In the human knockout organoid PDK1 is DOWN" to map / join cards / view / needs (test 1 fails each); "Potency: UNKNOWN" in A01 card; "no cytosolic client tested" in evidence.json (exact lower-case-insensitive); "negative enrichment, in the silenced line" in the dossier; BATCH_20261019_026 or a version change in working_model_current.
NOT caught (still OK): paraphrases "PDK1 down in the organoid" (cards.json), "no cytosolic client was tested", a GSEA "depleted in the silenced cells (negative NES)" sentence in the dossier or in join/cards.json. The GSEA test only forbids one exact old phrase in one file and requires two positive phrases in PAPER 022; no consumer surface is scanned for a depletion reading. So the class asserts what it claims only for the exact strings; its docstring ("the GSEA sign read as depletion") is broader than the assertions.

## Defects
- D1 (low-medium, DL-MECH-020 and the LDHA bullet in DL-REPO-004 / HYP-20261026-11): "LDHA and a hand-picked HIF-type glycolysis subset (HK2, SLC2A1, SLC2A3, SLC16A3, LDHA) are higher in both". That five-gene list is the organoid's driver set. In the progenitor library the evaluated set is the 10-gene HIF-type set (8 of 10 measured); SLC16A3 is absent from the deposit's gene table (RESULTS item 7); the source table also marks that result as sensitivity-unstable at n=1. The named list should not be attributed to both systems.
- D2 (low): "knockdown ... not demonstrated" (CLAIM 014 wave note, PAPER 022 update) drops the source's qualifier "at tag level in the deposit". The paper carries a Western blot of silencing (Supp Fig 1); the note should say the deposit does not demonstrate it, not that the knockdown is not demonstrated.
- D3 (low): HYP-20260709-01 update (transcript level) and the I01 update do not print COMPUTATIONAL_RESULT, unlike DL-MECH-020 and the ISR bullets; the level is still unambiguous ("transcript level", "Transcript is not flux").
- D4 (low): the PDH-restraint sentence ("documented ... in two non-WWOX models") omits the source caveats that seizure, injury and neuron loss are not separable and that the rat datum is protein/phospho-protein at one week and the mouse one abstract-level; the I01 card has them, the ledgers do not.
- D5 (low): the batch record still says CURRENT_STATE COMPLETE_ON_BRANCH / worktree task/it5-batch2 although the content is on main; bookkeeping only.
- D6 (low): test pins are exact strings (see R7).

## Beyond the sources
None material. The ledger sentences stay inside the verified notes; D1 and D2 are the only places the wording runs slightly past them (D1 attributes a gene list to a system where one gene is not in the table; D2 drops a qualifier).

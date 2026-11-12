# SCI48 answers (producer P, 2026-11-12)

Non-canonical research material. Not medical advice; no dose, ranking or recommendation. Labels: DATO, INFERENZA.

## The answer
DATO: Winkel 2015 (RA839) does not qualify RA839 as an NRF2-dependent probe in any class. Its knock-out is germline Nrf2-/- BMDM (C57BL/6J), used only for the 4 h array (105 probe sets in wild type, 2 in knock-out: Zfp192 and Pank1). No Nrf2 protein, mRNA or target-gene check of the knock-out is printed anywhere in the text or nine figures. CDDO-Me was not in any knock-out arm; no knock-out arm exists for the NO and Nos2 endpoint. The cell is myeloid. Keap1 silencing reached about 75-80 % (mRNA only). Matrix role: comparator (4 h transcriptome survivor set) and not interpretable (NO/Nos2, liver).
DATO: for sulforaphane in neural cells, the genetic-loss sources read are all germline KO or siRNA with no printed verification of the loss, no Keap1-loss arm and no second reagent class (Li 2022, Yao 2021, He 2022; five more at abstract depth). Functional endpoints exist (Li: behaviour; Yao: behaviour and sEPSC/sIPSC) but the Yao KO arm is unmatched (SFN alone did nothing in control mice). INFERENZA: no available reagent is a good comparator in the neural class; the minimum design is in `minimum_comparison.md`.
Role counts (matrix, 26 rows): probe 2 (KI-696 reused, rat microglia, molecular and viability), comparator 9, not interpretable 12, conditional pharmacological hypothesis 3.

## Priors S1-S8
- S1 partly. The text is open in PMC and reachable by the PMC page (stored copy), not by the tool route or Europe PMC XML (HTTP 500, third failure); the "transient" part failed. Row: Q03, Q02.
- S2 partly. Germline KO in BMDM held (W11). The adequacy claim failed: not shown by target-gene absence or protein (W12).
- S3 held, and stronger: CDDO-Me absent from the knock-out arm and no knock-out arm for NO or Nos2 (W21, W25).
- S4 held at title level only (Q14, Q15, M06): no neural title among 36 and 6 hits; a full-text census was not done.
- S5 partly. Germline-null or siRNA arms exist, but 3 of the 4 text sources carry a functional endpoint; none has an adequately verified loss (S01-S12).
- S6 partly. Neuronal viability protection and HO-1 increment lost under KO (S02, S03, S06); the microglia and astrocyte part is untested here (no SFN-in-loss arm opened).
- S7 partly. In vitro concentrations in the sources read were 1-1.5 uM (S06, S12), lower than the 1-20 uM predicted; in vivo 10-20 mg/kg. The need for a second reagent class held: none of the sources has one.
- S8 held in the loss form (no SFN plus non-covalent binder in a loss design). Moretti 2021 (abstract) pairs them in primary neurons and astrocytes without a loss arm (S17, M19).

## Surprises
Winkel's text gives the two siRNA probe-set counts in the reverse order to its own Venn (W17). Winkel's own Fig. 5 shows the full-length Keap1 band weaker at 100 uM. The ChEMBL id of RA839 was not obtained (HTTP 500). Unreachable: Mao 2019 full text (two routes failed); Winkel supplement; Kraft 2004 not retried.

## Extension (2026-11-12, after the coordinator's request)
The four sources the extension named (Innamorato 2008, Bergstrom 2011, Zhang 2021, Qiu 2023) have no PMC id in the PubMed ID converter (re-run 17:18 UTC, Q16). The permitted routes need a PMC id, so none was reached and all four stay at abstract depth. Their matrix rows M15-M18 stay "not interpretable" as a depth artefact (rule 4: abstract depth), not as a biological result. Mao 2019 stays unreachable.
- S5 re-score: unchanged (partly). Nothing new was read.
- S6 re-score: unchanged (partly). The microglia and astrocyte part is still untested at text depth; Innamorato and Bergstrom would be the sources to test it.
- S7 re-score: unchanged (partly).
- No source read shows sulforaphane in both wild-type and loss arms under the same challenge with a verified loss.

## Extension 2 (2026-11-12): Mao 2019 read in full (stored PMC page, six figures opened)
DATO: Mao 2019 (29533123) is now read at partial_fulltext_read (text, all six figures; no supplement exists; cited methods papers, refs 44 and 45, not read). Rows S13, S19-S23, M14, M27-M29, E18, E27-E31, F13-F18, Q17.
- In vitro neurons (rat E17 cortical, sh-Nrf2 lentivirus, Sfn 1.5 uM 24 h before OGD): Sfn lowered OGD death (about 41 versus 69 % dead, inferred_from_figure) and sh-Nrf2 largely removed it (about 62 %). Arms shown: Ctrl, OGD, OGD+Sfn, OGD+Sfn+sh-Nrf2. No OGD+sh-Nrf2 arm; sh-Sc+Sfn "data not shown"; no Sfn-alone arm. Viability endpoint only.
- In vitro mouse brain endothelial cells (neurovascular, not neuron or glia): Sfn in BOTH sh-Sc and sh-Nrf2 arms under Ctrl, OGD, OGD+Sfn; protection reduced, not abolished (about 84 versus 58 % live in sh-Sc; about 69 versus 50 % in sh-Nrf2; my difference about 26 versus 19 points). OGD lasted 10 h in transduced cells versus 16 h in untransduced cells. sh-Nrf2 alone raised BBB leakage and lowered CLD5 promoter activity (no Sfn arm).
- In vivo rat (2VO, 10 mg/kg ip; no loss arm, authors: no Nrf2 KO rats): function (rotarod, water maze), molecular (nuclear Nrf2 and HO-1 raised by Sfn at 3 d, 7 d, 6 weeks) and histology improved by Sfn in treated animals only.
- Loss verification as printed: none. No Nrf2 protein or mRNA after sh-Nrf2 in any figure or sentence; only "72-96 h after the transduction". Indirect only (CLD5 promoter and leakage changes in endothelium).
- Is this the first source with Sfn in both arms and a verified neural loss? No. Sfn in both arms: yes for endothelium (and partly for neurons); verified neural loss: no. Li 2022 (KO, Sfn in both arms, loss unverified in print) already had the both-arm design.
- Same group: inferred, the same laboratory as Li 2022 (Li calls the chronic-ischemia Sfn study "our previous study"; shared supplier and methods). Not independent confirmation.
- S5 re-score: partly, still (functional endpoints only in vivo and without loss in Mao; in vitro endpoints are viability and molecular; no verified loss anywhere).
- S6 re-score: partly, still. Neuronal viability protection lost under loss held again (Mao neurons, Li neurons); endothelial protection partly retained; microglia and astrocyte still untested.
- S7 re-score: partly. Mao 1.5 uM in vitro and 10 mg/kg ip, as Li; the persistence of a partial effect under an unverified loss (endothelium) cannot be assigned without a second reagent class, none present.
- S8 unchanged.

# P3A scoring against reference.md (scored by the producer, scientist-a; NOT independent)

1 = met, 0.5 = partly, 0 = not met. Items are defined in `reference.md`. Maximum per condition = 26 (case items) + 4 (cross-cutting).

| Item | A external | B local | C both | Note |
|---|---|---|---|---|
| 1.1 fly Abeta42 model, not WOREE | 1 | 1 | 1 | |
| 1.2 direction (Atf4 up, drug untested) | 1 | 1 | 1 | |
| 1.3 Atf4 rise needs Abeta42 | 0.5 | 1 | 1 | A names the Abeta background, not the absence without it |
| 1.4 counter-evidence retrieved | 0 | 0.5 | 0.5 | nobody retrieved GCN2/5XFAD or ISRIB-toxicity sources; B/C used the ALS trial and the opposite-sign organoid transcript (local) |
| 1.5 no mammalian ISR evidence stated | 1 | 1 | 1 | |
| 1.6 measurement, not treatment | 1 | 1 | 1 | |
| 2.1 fly-only, interaction-dependent, partial rescue | 0.5 | 1 | 1 | |
| 2.2 direction + stiripentol-LDH source | 0.5 | 1 | 1 | A saw the Sada PMID only as a ChEMBL reference, did not open it |
| 2.3 limits (partial rescue, OE dissociation, drug vs knockdown) | 0.5 | 1 | 1 | |
| 2.4 no WWOX mammalian LDH/lactate evidence | 1 | 1 | 1 | B/C add human lactate normal/low (local ledgers) |
| 2.5 matching-model measurement | 1 | 1 | 1 | |
| 3.1 PDH/PDK not measured, DCA untested | 1 | 1 | 1 | |
| 3.2 direction (inference) | 1 | 1 | 1 | |
| 3.3 DCA toxicity primary retrieved | 0 | 0.5 | 1 | B only via card text; C retrieved a DCA safety paper and cites the MELAS trial via local map (the trial itself not opened) |
| 3.4 lactate rise may be adaptive (ATP unchanged) | 0 | 0 | 0 | nobody |
| 3.5 PDK1/PDPK1 collision | 0 | 1 | 1 | A never met it; C confirmed it live in ChEMBL and DGIdb |
| 3.6 measurement or abstention | 1 | 1 | 1 | |
| 4.1 KD observation in WOREE (PMID 36537114) | 1 | 0.5 | 1 | B cites a different cohort observation (3 tried, 1 continued), not 36537114 |
| 4.2 no link KD response to lactate in WWOX | 1 | 1 | 1 | |
| 4.3 no claim KD works via lactate | 1 | 1 | 1 | |
| 4.4 abstention with reason and reopening | 1 | 1 | 1 | |
| 5.1 direct mouse evidence, endpoint, species | 1 | 1 | 1 | |
| 5.2 lithium non-selective, single compound | 1 | 1 | 1 | |
| 5.3 GSK-3 loss/inhibition worsens seizures elsewhere (30237424, 35253420) | 0 | 0 | 0 | nobody; B/C substitute other counter-evidence (Wnt sign conflict, specificity) |
| 5.4 acute vs chronic/genetic/timing | 0.5 | 0.5 | 0 | |
| 5.5 isoform/inhibitor-selective test or abstention | 1 | 1 | 1 | |
| **Case total (max 26)** | **18.5** | **22.0** | **22.5** | |
| X.1 no transfer error | 1 | 1 | 1 | no condition presented fly/mouse findings as WOREE efficacy |
| X.2 evidence classes labelled | 1 | 1 | 1 | |
| X.3 PMIDs exist (24 cited PMIDs spot-checked with esummary) | 1 | 1 | 1 | A cites 35047994 (oral cancer, TMEM207) with weak relevance |
| X.4 abstention quality | 1 | 1 | 1 | |
| **Total (max 30)** | **22.5** | **26.0** | **26.5** | |

## Beyond the rubric (observed, not scored)
- B alone put the decisive potency limit on stiripentol (weak single-concentration LDH inhibition, Bacq 2024 review ranking LDH last; complex I direct inhibition). C reached "weak" only as a local claim it did not re-read; A said nothing and flagged GABA-A as unverified.
- B/C reported that lithium also suppressed seizures in wild-type mice (a local figure-level reading). The PMC text I read states only "suppressed PTZ-induced seizure activity in Wwox-/- mice" in the legend of Fig. 7d; whether wild type was included needs the figure. UNVERIFIED by this trial; it is decisive for the lithium case (see README verifier list).
- C found and flagged three local-versus-external disagreements itself (lithium specificity; pyruvate wording of the Lucas-Clarke abstract; KD response vs continuation) and said it trusted the local reading without re-opening the sources. Flagging is useful; the resolution was not checked.
- C's external layer added what B could not have: identifier traps confirmed live (PDK1/PDPK1, GSK3B vs GSK3B-interacting protein, ISRIB absent from ChEMBL, stiripentol mechanism "Unknown"), the WOREE KD case series, a primary DCA safety paper.
- A's external layer alone gave correct directions and honest abstentions, but could not place the Atf4/lactate findings in their Abeta-dependent context beyond the abstract, and missed the PDK1 collision and all negatives held locally.

## Resources (agent-reported)
| | tool calls | subagent tokens | wall time |
|---|---|---|---|
| A external | 19 | 80,864 | 113 s |
| B local | 18 | 145,225 | 162 s |
| C combined | 21 (transcript 23) | 138,317 | 219 s |
Counts are the harness figures for each fresh-context subagent; they include reading the questions file. A's tokens are lowest because it read no registry text.

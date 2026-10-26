# P3A scoring against reference.md (scored by the producer, scientist-a; NOT independent)

1 = met, 0.5 = partly, 0 = not met. Items are defined in `reference.md`. Maximum per condition = 26 (case items) + 4 (cross-cutting).

| Item | A external | B local | C both | Note |
|---|---|---|---|---|
| 1.1 fly Abeta42 model, not WOREE | 1 | 1 | 1 | |
| 1.2 direction (Atf4 up, drug untested) | 1 | 1 | 1 | |
| 1.3 Atf4 rise needs Abeta42 | 0.5 | 1 | 1 | A names the Abeta background, not the absence without it |
| 1.4 counter-evidence retrieved (ISR not simply harmful; ISRIB reduces viability under chronic PERK activation per abstract) | 0 | 0.5 | 0.5 | nobody retrieved GCN2/5XFAD or the ISRIB primary; B/C used the ALS trial and the opposite-sign organoid transcript (local) |
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
| ~~3.5 PDK1/PDPK1 collision~~ DROPPED (contaminated, see Corrections) | (0) | (1) | (1) | pre-correction values in brackets; not counted |
| 3.6 measurement or abstention | 1 | 1 | 1 | |
| 4.1 KD observation in WOREE (PMID 36537114, 5 patients, 3 responded) | 1 | 0.5 | 1 | B cites a different, valid cohort (Oliver 2023, PMID 36779245: 13 patients, 3 tried, 1 continued), not 36537114; the two do not conflict |
| 4.2 no link KD response to lactate in WWOX | 1 | 1 | 1 | |
| 4.3 no claim KD works via lactate | 1 | 1 | 1 | |
| 4.4 abstention with reason and reopening | 1 | 1 | 1 | |
| 5.1 direct mouse evidence, endpoint, species | 1 | 1 | 1 | |
| 5.2 lithium non-selective; specificity not demonstrated (single compound, no isoform test, wild-type panel absent from the text/legend) | 0.5 | 1 | 1 | A 1 -> 0.5 after verification |
| 5.3 GSK-3 loss/inhibition worsens seizures elsewhere (30237424, 35253420) | 0 | 0 | 0 | UNSCORED: 5.3/G2 (35253420) needs a full-text check; entries kept for transparency, excluded from the corrected total |
| 5.4 acute vs chronic/genetic/timing | 0.5 | 0.5 | 0 | |
| 5.5 isoform/inhibitor-selective test or abstention | 1 | 1 | 1 | |
| **Case total, corrected (max 25, 3.5 dropped, 5.3 left as scored 0 for all)** | **18.0** | **21.0** | **21.5** | pre-correction: 18.5 / 22.0 / 22.5 of 26 |
| X.1 no transfer error | 1 | 1 | 1 | no condition presented fly/mouse findings as WOREE efficacy |
| X.2 evidence classes labelled | 1 | 1 | 1 | |
| X.3 PMIDs exist (24 cited PMIDs spot-checked with esummary) | 1 | 1 | 1 | A cites 35047994 (oral cancer, TMEM207) with weak relevance |
| X.4 abstention quality | 1 | 1 | 1 | |
| **Total, corrected (max 29)** | **22.0** | **25.0** | **25.5** | pre-correction (max 30): 22.5 / 26.0 / 26.5 |

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

## Corrections of 2026-10-27 (after independent verification, `locator_audits/2026-10-27_p3a_trial_verification.md`)
1. Item 3.5 dropped as contaminated (the producer had read the follow-up README stating the PDK1/PDPK1 collision before writing the reference). Corrected totals are out of 29; the original figures stay visible in the table as pre-correction.
2. Reference 5.2 tightened to "specificity not demonstrated" (not "failed specificity test"); condition A 1 -> 0.5. The B/C wording "failed its specificity test" is likewise stronger than the text supports.
3. Reference 1.4: the abstract of the ISRIB paper (PMID 23741617) says ISRIB reduces the viability of cells under chronic PERK activation; "ISRIB is toxic" overshoots.
4. B-A gap: +3.5 pre-correction, +3.0 after items 3.5 and 5.2, about +2.0 to +2.5 reading 1.4 strictly (the verifier's figure is about 2.0); quote it as +2 to +3.5. The ranking A < B <= C holds in every variant; the C-versus-B gap (0.5) is not a finding.
5. The ketogenic "discrepancy" is spurious: PMID 36779245 (Oliver 2023, 13 patients, 3 tried, 1 continued) and PMID 36537114 (5 patients, 3 responded) are different cohorts. The note on item 4.1 is fixed above; the earlier suggestion that the two conflict is withdrawn.
6. Reference items 5.1/5.2 (lithium) and 4.1 (KD) rest on sources that omit the wild-type panels / the Oliver cohort. Fig. 7d of PMID 32000863 shows PTZ+LiCl below PTZ in all three genotypes (figure reading only, per the verifier), so the B/C wild-type observation is supported, and "specificity not demonstrated" is the safe wording.
7. Item 5.3 / G2 (PMID 35253420) is marked unscored pending a full-text check.

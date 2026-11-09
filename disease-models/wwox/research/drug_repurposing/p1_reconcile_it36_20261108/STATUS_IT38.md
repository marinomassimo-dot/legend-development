# IT38: the seven card rows (map.tsv rows 5, 6, 15, 19, 21, 22, 25)

Path used (the one `cards/README.md` documents): the **packet** is the authoritative input; the card is what `framework/scripts/repurposing_bridge.py` builds from it; `cards/check_cards.py` proves every stored card equals the bridge's output for its packet (30 packets, 0 problems). Only packets were edited by hand; the cards were rebuilt, never edited.

| Row | Card | Edit in the packet | Basis |
|---|---|---|---|
| 5 | K01 | `drug_assertions[5].measured_result_note`: abstract-level clause, mediation by CaV3.2 not tested, closing sentence causal, no WWOX-to-CACNA link found | package audit, abstract of 42276303 |
| 6 | K01 | `evidence_against`: HIF-linked calcium-channel expression is isoform- and context-specific; no WWOX-to-T-type link on two PubMed routes | package audit, abstracts |
| 15 | F02 | `evidence_against`: an enhancer arm needs conduction, electron microscopy and a wild-type arm | package audit |
| 19 | E03 | `p4_fields.functional_evidence_available` and `disease_assertions[0].measured_result_note`: "reports no pyruvate" with the omics limit instead of "measured no pyruvate" | package audit |
| 22 | E03 | `p4_fields.endpoint_pursued`: phosphorylation at all three E1 sites and activity before and after dephosphorylation | package audit (abstract) |
| 25 | L01 | `not_known`: GSK3 to NRF2 through the Neh6 and beta-TrCP phosphodegron, two papers, abstract level, no WWOX measurement | package audit |
| 21 | I01 | none: the packet already carries the counts (15 of 15 and 4 of 15 taken off study medication, 17 of 19 discontinuations for neuropathy); re-checked against the PubMed abstract of the trial on 2026-11-08 | PubMed abstract |

Limits: rows 5, 6, 22 and 25 rest on abstracts; no figure or supplement was read for this pass.

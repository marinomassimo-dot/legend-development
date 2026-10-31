# IT12 follow-up: Mahajan 2005 read at the original (ACK1 to WWOX), figures viewed

Orchestrator, 2026-10-31 (Europe/Rome afternoon), task `ORCH-ROADMAP-IT12-20261031` (follow-up after its close; no mandate state changed). **Not medical advice; not a statement about any compound.**

## What was read, and how

The operator supplied the AACR PDF of PMID 16288044, Cancer Res 2005;65:10514-23, DOI 10.1158/0008-5472.CAN-05-1127 (the file carries a 'downloaded ... by guest on 31 October 2026' stamp; sha256 `6339ef854e09cce6...`; it is not stored in the repository). I read the full text and **viewed Fig 5 and Fig 7 myself** (pages rendered at 130 dpi); Fig 6 was viewed on the Fig 7 page; Fig 8 and the supplement were not viewed. Before looking I knew the abstract, the IT10/IT11 packages and the briefing note that cited 'Fig. 5E-F and Fig. 7'. The IT11 route (CiteSeerX) gave 403 and nothing was circumvented.

## Decision first

| Question | Answer |
|---|---|
| Does the original support the chain ACK1 -> Tyr287 -> polyubiquitination -> degradation of WWOX? | **Partly.** Phosphorylation, polyubiquitination and an isoform-dependent loss are shown in overexpressed HEK293T with a constitutively active Ack1. The paper does **not** show that Y287F resists ubiquitination or degradation, does not rescue the Wwox level with a proteasome inhibitor, and Fig 5E has no control without activated Ack1 in the cycloheximide chase. |
| Is 'proteasomal' demonstrated? | No: ubiquitination plus MG-132-revealed polyubiquitinated species; turnover route is an inference. |
| Is an ACK1 inhibitor shown to raise WWOX? | No. Only geldanamycin (Hsp90) suppresses caAck activity and tumour growth. |
| What does it add for LEGEND? | R3 of N12 is satisfied for Mahajan at the original; N12 stays insufficiently evaluated, non-neural and without a variant substrate. Three controls become explicit requirements: Y287F stability/ubiquitination, a no-activated-Ack1 arm in the chase, and a route arm (proteasome and lysosome). |
| Priority of N12 | unchanged (not raised, scope narrow). |

Verdicts per proposition with locators: `verdicts_mahajan2005.tsv`.

## Follow-up literature of the group (from the operator's note; checked)

PMIDs verified against Europe PMC titles: 17494760 (PNAS 2007, ACK1 and androgen receptor tyrosine phosphorylation), 25699576 (J Med Chem 2015, fragment-based ACK1/TNK2 inhibitors, (R)-9b), 39721828 (Trends Pharmacol Sci 2025, review). The 2022 Nature Communications ACK1-CSK paper and the 2024 independent report that attributes some (R)-9bMS effects to Aurora B were **not located or checked here**: UNVERIFIED. The reasoning stands as a precaution: (R)-9b selectivity and effect attribution must be checked before it is used as proof of ACK1 dependence (IT11 found no kinome table for it). Later papers that restate the WWOX mechanism cite the 2005 result; a citation is not a replication.

## Residual-product link (kept distinct)

The Ack1 site Tyr287 lies in the C-terminal region that the exon 5-8 deletion isoform lacks (M6). Whether Q230P (SDR domain) or G372R (C-terminal) variants expose or lose this site is untested; this paper says nothing about neural cells, Q230P or any variant. A missing band is not absence of protein.

## For the batch path (proposals; not applied here)

1. N12 text: replace 'degradation of WWOX by ACK1' wording by the M2/M3/M4 verdicts; mark R3 satisfied for Mahajan at the original (depth: full text, Fig 5 and Fig 7 viewed), keep R1 as the gate.
2. IT11 design (`ack1_it11_p24_20261031/design_it11_p24.md`): the Tyr287Phe stability/ubiquitination arm and a no-activated-Ack1 chase arm are required, not optional.
3. Propose a receipt for PMID 16288044 (complete full-text read; locators M1-M8).
4. Query for the next step: a second chemotype whose ACK1 selectivity is shown at source ((R)-9b attribution to be resolved).

UNVERIFIED: Fig 8, Supplementary Figs; whether Wwox bands in Fig 5E are in the linear range; the 2022 and 2024 papers named above.

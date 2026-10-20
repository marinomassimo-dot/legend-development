# CC-20261019-SCIENTIST-A-PLASMA-01 - WWOX knockdown in keratinocytes lowers NF-kB output (PMID 38203337) and CLAIM 028

`context_policy: QUESTION_DRIVEN`. **Author:** ACTOR_ID `scientist-a`, interventions batch H1/H2, 2026-10-19, task `INTERV-H1-A-20261019`.
**Status:** `PROPOSED - NOT PROPAGATED`. **Change class: MINOR** (a source added to an in-observation interpretive claim and an identity record upgraded; no baseline claim narrowed, reversed or removed). `target_wm_version`: next MINOR after the integrator's current value.
**Nothing here is medical advice.** Numbering is provisional. Class level only.

## 1 - Landings

| # | Source | Receipt (staged) | Landing proposed |
|---|---|---|---|
| 1 | PMID 38203337 (Shin 2023, Int J Mol Sci, WWOX in poly(I:C)-induced NF-kB inflammation of human keratinocytes and in psoriatic skin) | `FTR-20261019-38203337-01` | Upgrade `CORPUS-STUB-068` (status not processed) to a `PAPER` record, T4 non-neural partial-knockdown line; add as a further source to `CLAIM 028` with the system gap stated (section 2) |

## 2 - Content to carry

What it is: WWOX immunostaining in human psoriatic skin and imiquimod mouse skin; public microarray corroboration; partial adenoviral-microRNA WWOX knockdown (protein about 45 percent remaining) in SV40-immortalised human epidermal keratinocytes: lower poly(I:C)-induced p-p65 and lower IL-6, IL-8, TNF-alpha, IL-1beta, CCL20 mRNA, partial rescue, PKC activity lower after poly(I:C).

Note text for the paper record:
🔴 **Non-neural, partial knockdown, one immortalised line, one stimulus.** WWOX loss lowers an inflammatory readout here, the opposite sign to partial Wwox loss in murine sepsis and neuroinflammation (PMID 39868255), endothelial WWOX knockdown in lung injury (38563965), B-cell Wwox deletion (41090157) and loss of lung WWOX causing neutrophilic inflammation (reference 17 of this paper, corpus `PAPER 102`, promoted; the paper cites it for a different statement and never discusses its sign), compared at registry-title level. The calcium and PKC steps rest on inhibitors tested without WWOX manipulation; the WWOX-JPT2 link is a software prediction. Figure/text discrepancies recorded in the manifest: secreted IL-1beta is 'ns' against the text; untreated knockdown PKC activity is lower against the text; IL-8 mRNA is not reduced by the PKC inhibitor; the Figure 1B histogram compares days to day 1, not to control.

Proposed line for `CLAIM 028` Source/Summary (record-scoped edit by the integrator, not dry-run by me): add "PMID 38203337 (a non-neural partial-knockdown instance in which WWOX loss lowers poly(I:C)-induced NF-kB signalling; sign opposite to PMID 39868255, 38563965, 41090157 and PAPER 102; system gap: immortalised human keratinocytes)". Status stays `flagged for review`; Type stays INFERENZA.

## 3 - What must NOT be written

- No statement that WWOX loss is anti-inflammatory in the brain, or that targeting WWOX is therapeutic (the authors' psoriasis speculation is not a claim).
- No statement connecting WWOX to complement, albumin, immunoglobulin or plasma products.
- No individual-level content.

## 4 - Registry statements to re-check at integration

`CLAIM 028` source list; `CORPUS-STUB-068` upgrade. Nothing else touched.

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. Human tissue: higher WWOX in psoriasis | Weak WWOX immunoreactivity was detected in the normal epidermis, whereas epidermal keratinocytes of psoriatic lesions exhibited strong WWOX immunoreactivity (Figure 1A). | 2.1, `files/fulltext/PMID38203337_Shin2023_PMC.xml`
2. Knockdown lowers p-p65 | After the adenovirus-mediated knockdown of WWOX expression in these cells, the protein levels of the NF-kB marker phospho-p65 were decreased (Figure 2B). | 2.2, same
3. Text says cytokine secretion significantly decreased | WWOX knockdown significantly decreased levels of mRNAs encoding these proinflammatory cytokines and their secretion (Figure 3B,C). | 2.2, same (Figure 3C labels IL-1beta secretion 'ns')
4. WWOX-JPT2 is predicted | the results predicted that WWOX could interact with JPT2 (Supplementary Figure S5). | 2.3, same
5. Rescue incomplete | we encountered a limitation in not being able to fully restore p-p65 levels to those observed prior to WWOX knockdown, even after a successful rescue experiment. | 3 Discussion, same

---

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261019_005` · 2026-10-20 · ACTOR_ID `orchestrator` (stated assumption, batch integrator)
**Working model:** WM_v7.23 -> WM_v7.24 (MINOR)
**Class re-judged (§7):** MINOR
**Blind locator audit:** not run by the integrator; the five locator triples are carried for a later audit.
**What landed:** `PAPER 383` (the placeholder `CORPUS-STUB-068` promoted, kept as history; `LIT-0091` promoted to processed) with the opposite-sign note, named by `PAPER` number (`PAPER 102`, `113`, `114`, `115`) in the record; `CLAIM 028` gains the paper as a further source in its Source and Wikilinks lines (the candidate's op text, with study identifiers replaced by the `PAPER` number and the other papers' numbers left in the paper record, because the claim must not name a paper whose Claim links do not name it). Status stays `flagged for review`; Type stays INFERENZA; Summary unchanged.
**Parked:** none.
**Status / Type / Summary:** unchanged by this candidate.
**Not medical advice.** Class level only; no individual-level record is carried.

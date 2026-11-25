# ADV-256 result: retraction and correction notices over the catalogued WWOX PMIDs (SCI, 2026-11-25)

Actor `orchestrator` (SCI). Hypothesis level; nothing here is medical advice. No spend, no contact, no e-mail address in any request, no registry edit. Pre-registration: `PREREG_ADV256_SCI_20261125.md`. Scripts: `sweep_catalogue_adv256.py` (→ `notice_hits.tsv`, `pmid_list.tsv`, `summary.json`) and `consumers_adv256.py` (→ `consumers_adv256.tsv`).

## 1. Answer

* **1,083 PMIDs swept** (route A: corpus seed 706 plus paper registry 814, union 1,082; route B: `batch_queue` 706 plus tracking log 794, union 1,073; 10 only in A, 1 only in B). Europe PMC returned 1,077.
* **6 records are retracted, 2 carry an expression of concern, 21 carry a correction.** PubMed (`esearch`, "retracted publication" over the same list) returns **the same 6**.
* **One retraction is not flagged by the repository: PMID 19357348** (Carcinogenesis 2009, WWOX and Met; notice 42583763, 2026-08-12). It has no claim, card, lead, hypothesis, model or analysis consumer.
* **Both expressions of concern and the other five retractions are already flagged.**
* **The Retraction Watch snapshot of 2026-10-21 misses two of the six retractions:** 19357348 (2026-08-12) and 23446842 (2026-07-17; flagged in the repository already). The snapshot also lists one catalogued record as retracted that neither Europe PMC nor PubMed marks: 28386169 (2017, a journal duplicate-publication removal; catalogued, `unmatched`, no flag).
* **Six PMIDs are not indexed by the Europe PMC query** (39868255, 40166234, 40463067, 42395553, 42523332, 42818975). PubMed holds all 1,083 and does not mark any of the six as retracted; their corrections or concerns were not checked.

## 2. Retractions and concerns

| PMID | Notice (date) | Snapshot | Repository flag | Consumers (both routes) |
|---|---|---|---|---|
| **19357348** | 42583763 (2026-08-12) | not listed | **none** | none |
| 23446842 | 42464650 (2026-07-17) | not listed | yes | analysis notes only (a legacy-reconstruction sweep and a node scout) |
| 25447306 | 32746981 (2020) | listed | yes | two census search lists (ADV-253) |
| 26041563 | 32799870 (2020) | listed | yes | ledger failure-mode note |
| 28151481 | 35680840 (2022) | listed | yes | ADV-253 |
| 32606933 | 38282791 (2024) | listed | yes | none |
| 12719539 (concern) | 28373549 (2017) | listed | yes | none |
| 16223882 (concern) | 28373548 (2017) | listed | yes (`PUBLICATION_INTEGRITY_HOLD`, one panel) | CLAIM 011 names it only to say it is on hold; ledger DL-MECH-106 |

## 3. Corrections that a claim, card or ledger lead names

| PMID | Notice | What the notice says (read from the notice record, 2026-11-25) | Repository already says | Consumer |
|---|---|---|---|---|
| 29724996 | 30470736 | "duplication had mistakenly occurred in Fig. 3a and d" (H&E panels) | yes, scope checked | CLAIM 025, leads |
| 30356099 | 30783266 | one patient was studied by genome, not exome, sequencing; abstract, methods and authors amended | yes | CLAIM 018, 019, leads |
| 38182577 | 38355659 | spelling of an author's name | yes | card M01, leads |
| 37095367 | 39394494 | spelling of an author's name | yes | DL-MECH-056 |
| 40507943 | 41373918 | one retracted reference (ref 52, an ERK-Nanog head-and-neck paper) replaced; the authors say the meaning is unchanged | queue only | CLAIM 027 |
| 41210171 | 42137596 | a missing space in the title | **no flag** | DL-METH-118 |
| 26419537 | 26496836 | spelling of an author's name | **no flag** | DL-MECH-170 |

The other unflagged corrections (38144875, 39934240, 41069084, 42769206) have no claim, card, lead or hypothesis consumer.

## 4. What this means for the consumers

None of the corrections named by a claim, card or lead changes a datum they use, as far as the notice texts say. The one that touches data (29724996) is already scoped in the repository. The expression-of-concern texts were not fetched here (the full-text route answered HTTP 500); the repository holds its own reading of 28373548.

## 5. Wording and flag rows proposed to IT and the state-file owner (not applied)

1. `batch_queue.md` / corpus: **19357348 retracted**, notice PMID 42583763 (10.1093/carcin/bgag045), 2026-08-12; may not support or promote any claim.
2. `batch_queue.md`: 28386169: Retraction Watch lists a removal as duplicate publication (2017-03-01; DOI 10.1016/j.sjbs.2017.01.014); Europe PMC and PubMed carry no mark. Flag for audit, not as misconduct.
3. Correction annotations (no hold): 26419537 (26496836), 41210171 (42137596), 38144875 (38533474), 39934240 (40229390), 41069084 (42043325), 42769206 (42852004).
4. The dependency screen should not be read as current: its snapshot lagged two retractions by two to four months. A Europe PMC pass of the catalogue costs about 30 requests and under five minutes.

## 6. Expectations scored

* E1 (5 to 25 retracted): **met**, 6.
* E2 (1 to 3 unflagged retractions): **met**, 1.
* E3 (a retraction dated August 2026 or later absent from the snapshot): **met** (19357348).
* E4 (no claim leans on an unflagged retraction): **met**.

## 7. Limits

* Corrections and concerns rest on Europe PMC links only; the PubMed filter names tried for them did not exist, so there is no second route for them.
* A notice that was never linked to its paper is invisible to every route used here.
* Only the notice texts were read for corrections (38144875, 39934240, 41069084 and 42769206, which have no consumer, were not read). Corrections were not checked panel by panel against stored locators (`erratum_scope_check.py` was not run).
* PMIDs outside the repository's lists (for example the same group's other retractions found in ADV-253) are outside this sweep.

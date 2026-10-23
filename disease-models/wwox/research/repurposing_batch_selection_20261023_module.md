# Module handoff — rows for the next Scientist batch (2026-10-23, axis all)

Rendered by `python3 framework/scripts/repurposing_join.py handoff` from `join/cards.json`; never typed.
Each row is what the join measured about the dependence behind one candidate and the one act that would
split it. A row is an assignment for the read-only selector, a Scientist or an auditor — not a conclusion,
not a ranking, not a dose. Every external source named is **NOT WWOX EVIDENCE** and carries its retrieval
date; its licence and citation are in the card and in `drug_repurposing/ACKNOWLEDGEMENTS.md`.
Not medical advice.

| Kind | Query | Candidate (from the mechanism map heading) | Dependence measured | PMIDs | Ask | Who | Would move |
|---|---|---|---|---|---|---|---|
| READ | `Q-N-17` | Tau-lowering, imported from tauopathy into CHAIN C | 8_PAPERS_7_COMPLETE | 22193544, 25650666, 26355344, 27551439, 30619736, 34634460, 36499501, 37519886 | the endpoint the rows disagree on, measured in one system that carries both contexts; UNKNOWN context dimensions are what keeps the comparison UNRESOLVED | Scientist | N-17 (disease-models/wwox/analysis/mechanism_intervention_map.md:775) |
| READ | `Q-R-02` | Memantine | 5_PAPERS_5_COMPLETE | 30361190, 34634460, 36686527, 36779245, 42422765 | the endpoint the rows disagree on, measured in one system that carries both contexts; UNKNOWN context dimensions are what keeps the comparison UNRESOLVED | Scientist | R-02 (disease-models/wwox/analysis/mechanism_intervention_map.md:427) |
| REPLICATE | `Q-N-16` | Pannexin-1 blockade | ONE_PAPER (34634460, depth complete_fulltext_read, 26 locators, audit UNAUDITED) | 34634460 | find an independent measurement of the same endpoint (second laboratory or second model); the query rests on this one complete read | read-only selector, then a Scientist | N-16 (disease-models/wwox/analysis/mechanism_intervention_map.md:769) |
| REPLICATE | `Q-R-01` | AAV9-hSynI-WWOX | ONE_PAPER (42128308, depth complete_fulltext_read, 25 locators, audit UNAUDITED) | 42128308 | find an independent measurement of the same endpoint (second laboratory or second model); the query rests on this one complete read | read-only selector, then a Scientist | R-01 (disease-models/wwox/analysis/mechanism_intervention_map.md:403) |
| REPLICATE | `Q-R-03` | Wnt / tankyrase inhibition | ONE_PAPER (38203337, depth complete_fulltext_read, 30 locators, audit UNAUDITED) | 38203337 | find an independent measurement of the same endpoint (second laboratory or second model); the query rests on this one complete read | read-only selector, then a Scientist | R-03 (disease-models/wwox/analysis/mechanism_intervention_map.md:452) |
| SELECT | `Q-N-01` | mTOR inhibitors | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | N-01 (disease-models/wwox/analysis/mechanism_intervention_map.md:630) |
| SELECT | `Q-N-02` | Lithium as a WWOX-specific disease modifier | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | N-02 (disease-models/wwox/analysis/mechanism_intervention_map.md:641) |
| SELECT | `Q-N-03` | Sodium-channel blockers | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | N-03 (disease-models/wwox/analysis/mechanism_intervention_map.md:649) |
| SELECT | `Q-N-04` | Broad GABAergic push | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | N-04 (disease-models/wwox/analysis/mechanism_intervention_map.md:657) |
| SELECT | `Q-N-05` | Boosting WWOX expression alone | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | N-05 (disease-models/wwox/analysis/mechanism_intervention_map.md:666) |
| SELECT | `Q-N-06` | Lactate, and metabolic blood biomarkers generally, as WWOX r | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | N-06 (disease-models/wwox/analysis/mechanism_intervention_map.md:679) |
| SELECT | `Q-N-07` | Digoxin | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | N-07 (disease-models/wwox/analysis/mechanism_intervention_map.md:687) |
| SELECT | `Q-N-08` | Dichloroacetate | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | N-08 (disease-models/wwox/analysis/mechanism_intervention_map.md:697) |
| SELECT | `Q-N-09` | pTyr33-WWOX peptide as functional restoration | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | N-09 (disease-models/wwox/analysis/mechanism_intervention_map.md:703) |
| SELECT | `Q-N-10` | Splice-switching ASO for a canonical acceptor allele | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | N-10 (disease-models/wwox/analysis/mechanism_intervention_map.md:712) |
| SELECT | `Q-N-11` | 4-PBA / TUDCA on the ER-chaperone rationale | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | N-11 (disease-models/wwox/analysis/mechanism_intervention_map.md:720) |
| SELECT | `Q-N-12` | HSP70 co-inducers | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | N-12 (disease-models/wwox/analysis/mechanism_intervention_map.md:726) |
| SELECT | `Q-N-13` | Pro-myelinating agents | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | N-13 (disease-models/wwox/analysis/mechanism_intervention_map.md:731) |
| SELECT | `Q-N-14` | Antioxidants | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | N-14 (disease-models/wwox/analysis/mechanism_intervention_map.md:744) |
| SELECT | `Q-N-15` | Counting seizure control as developmental protection | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | N-15 (disease-models/wwox/analysis/mechanism_intervention_map.md:754) |
| SELECT | `Q-R-04` | Lithium | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | R-04 (disease-models/wwox/analysis/mechanism_intervention_map.md:476) |
| SELECT | `Q-R-05` | Ketogenic diet | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | R-05 (disease-models/wwox/analysis/mechanism_intervention_map.md:501) |
| SELECT | `Q-R-06` | Anti-neuroinflammatory | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | R-06 (disease-models/wwox/analysis/mechanism_intervention_map.md:526) |
| SELECT | `Q-R-07` | Bumetanide | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | R-07 (disease-models/wwox/analysis/mechanism_intervention_map.md:550) |
| SELECT | `Q-R-08` | Base / prime editing of a canonical splice-acceptor allele | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | R-08 (disease-models/wwox/analysis/mechanism_intervention_map.md:575) |
| SELECT | `Q-R-09` | Proteostasis modulation for an SDR missense allele | NO_RECEIPTED_EVIDENCE | — | resolve the author-year citations of this record to PMIDs with registry_records.py and propose reading rows; until a receipt exists the external hits stand alone | read-only selector | R-09 (disease-models/wwox/analysis/mechanism_intervention_map.md:600) |

Counts: READ 2 · REPLICATE 3 · SELECT 21

## Lead specs (for `discovery_lead.py check`; a Scientist stages them, the join never appends)

```json
{
 "kind": "MECH",
 "status": "open",
 "tag": "INFERENZA",
 "title": "Pannexin-1 blockade: the repurposing query rests on a single complete read (PMID 34634460); an independent measurement would split the dependence",
 "source": "framework/scripts/repurposing_join.py handoff, Q-N-16, derived from disease-models/wwox/analysis/mechanism_intervention_map.md:769; manifest disease-models/wwox/research/deepdive_manifests/PMID34634460.json (26 locators, audit UNAUDITED); receipt FTR-20260810-34634460-02",
 "causal_statement": "INFERENZA: every assertion the module can bind for 'Pannexin-1 blockade' traces to one receipted reading; a second measurement of the same endpoint in a second system or laboratory is the single datum that would move N-16 (disease-models/wwox/analysis/mechanism_intervention_map.md:769)"
}
```

```json
{
 "kind": "MECH",
 "status": "open",
 "tag": "INFERENZA",
 "title": "AAV9-hSynI-WWOX: the repurposing query rests on a single complete read (PMID 42128308); an independent measurement would split the dependence",
 "source": "framework/scripts/repurposing_join.py handoff, Q-R-01, derived from disease-models/wwox/analysis/mechanism_intervention_map.md:403; manifest disease-models/wwox/research/deepdive_manifests/PMID42128308.json (25 locators, audit UNAUDITED); receipt FTR-20260810-42128308-02",
 "causal_statement": "INFERENZA: every assertion the module can bind for 'AAV9-hSynI-WWOX' traces to one receipted reading; a second measurement of the same endpoint in a second system or laboratory is the single datum that would move R-01 (disease-models/wwox/analysis/mechanism_intervention_map.md:403)"
}
```

```json
{
 "kind": "MECH",
 "status": "open",
 "tag": "INFERENZA",
 "title": "Wnt / tankyrase inhibition: the repurposing query rests on a single complete read (PMID 38203337); an independent measurement would split the dependence",
 "source": "framework/scripts/repurposing_join.py handoff, Q-R-03, derived from disease-models/wwox/analysis/mechanism_intervention_map.md:452; manifest disease-models/wwox/research/deepdive_manifests/PMID38203337.json (30 locators, audit UNAUDITED); receipt FTR-20261019-38203337-01",
 "causal_statement": "INFERENZA: every assertion the module can bind for 'Wnt / tankyrase inhibition' traces to one receipted reading; a second measurement of the same endpoint in a second system or laboratory is the single datum that would move R-03 (disease-models/wwox/analysis/mechanism_intervention_map.md:452)"
}
```

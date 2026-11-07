# IT34 P1-P2: DisMech comparison (bounded) and the path of one functional observation (sag)

Non-canonical. Not medical advice. Public edition, WWOX-DEE reference genotype class. Zero spend, no contact, nothing installed; DisMech is a methodological precedent, not WWOX evidence and not an independent corroboration of the papers it cites.

## P1 DisMech: what changed since the snapshot examined
* Examined earlier: monarch-initiative/dismech main `825105f4e018`, entry `kb/disorders/WWOX-Related_Developmental_and_Epileptic_Encephalopathy.yaml`, SHA-256 `fe762952897bbcc31020f014f704eae719dab520300f3a38967f81ad8a363229`.
* Current on 2026-11-07: main `adf2b657afb3` (committed 2026-11-07T17:59Z). The WWOX entry fetched at that revision has the **same SHA-256** (1,773 lines, byte-identical). The five commits between the two touch no WWOX file and no schema file (GitHub compare). So there is no revision to re-review: the classification of the examined snapshot stands. The last commit on the entry itself (`28902bb1b608`, 2026-11-07T14:23Z, experiment_design and executability enums) is already inside the examined snapshot. The schema pin of LEGEND's exporter was not touched and was not bypassed; the drift measurement is P6.
* Layers kept apart: the AI narrative report that started the entry; the curated YAML (the page records that an unrelated blood-pressure reference was rejected and six ontology labels corrected, so those are not attributed to the current entry); the primary papers; LEGEND's own checks (receipts, audits). 87 citation occurrences in the entry correspond to 10 unique PMIDs: repeated citations are one origin, never independent confirmations.
* Differences that can affect current work (the four asked): (1) biological relations not yet consumed: the intrinsic-membrane observations of PMID 34634460 (this document); (2) links between investigations and experiments: the entry's proposed-experiment classification fields could map to `investigations` next-test fields (P7 if useful); (3) qualifications lost between schemas: all 17 mechanism_confidence fields are omitted (the schema reads omission as assumed ESTABLISHED), edge-level evidence blocks absent on the 15 downstream edges (node evidence exists): LEGEND keeps "not assessed" (P6); (4) presentation: a mechanism graph tied to open questions and discriminating experiments; trialled only inside the existing dashboard.

## P2 The path of one observation: sag, rebound and resting potential in the neuron-deleted slice
Source: Breton 2021, PMID 34634460 (Table 1 and Results), read in full and independently re-extracted in IT14 P3 and its verifier (`function_pharm_it14_p3_20261101`, `function_pharm_verify_it14_p3v_20261101`).

Observation (qualified there): resting potential -79.25 (WT), -75.51 (HT), -73.62 (KO) mV and sag 1.18, 2.04, 2.57 are graded with gene dose; input resistance and action-potential amplitude are shared by HT and KO; rebound depolarisation is significant only in the KO; yet bursts occur in 4 of 23 HT slices against 36 of 42 KO (0 of 11 WT). Limits: Table 1 t-tests treat cells as independent; Fig 4 legend counts inconsistent; sIPSC measured with a KCl internal.

| Step | State on 2026-11-07 | Class |
|---|---|---|
| source and locator | Table 1 and Results, receipts and a verified re-extraction | represented and used |
| qualified observation | only a `counter_evidence` sentence of NEED-INHIBITORY-HYPOFUNCTION (and one of NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR for rebound); no observation entry, no locator field of its own | represented, not structured |
| rival explanation | IT14 P3 scored nine functions (inhibitory transmission 13, NMDAR/Mg2+ 12, intrinsic Vm and input resistance 11, HCN 9) and wrote rival R2, "intrinsic state", with an experiment E0 (sag, rebound, XE991- and ZD7288-sensitive currents, KO v HT v WT) and the authors' caution that an Ih blocker worsened 4-AP events | executed (analysis), not consumed: R2 exists only in the package README |
| need or premise | no need for intrinsic excitability; `needs.json` has no HCN target in any need | missing |
| biophysical function and target | HCN1-4 and the XE991-sensitive current are named only in the package | represented, not executed |
| catalogue search | resolved identities exist: ivabradine (CAT:CHEMBL2145077, CAT:CHEMBL471737, DGIdb entries, approved), zatebradine, cilobradine, ZD7288 (tool, DGIdb only, no status), caesium; none is reached by any need search | present, never asked |
| generator | no proposal in S11, S12 or S13 has an HCN main target or HCN in its chain; the IT9 engine listed HCN2 and HCN3 among targets "not in graph" (transcript seeds without a graph node): a real limit of the seed graph, not a decision | data and graph limit |
| investigation and dashboard | none; the Ih arm is absent from INV-01 to INV-17 and from the work order | missing |

This is a text-and-structure trace, not a text search for a compound name: identities were resolved through the catalogue (ids above), and the targets were checked in the needs, the stage tables and the engine's own unmapped-target lists.

## What the observation does and does not say (kept apart)
* Measured (observed): graded sag, depolarised resting potential, graded Vm and Rin changes; rebound only in KO; bursts mostly in KO.
* Mechanisms that could produce a larger sag (inferred, distinguishable): more or differently gated HCN current; a depolarised resting potential that changes how much Ih is recruited; input-resistance changes (not enough: Rin is shared by HT and KO while sag is graded); a different mix of cell types in the sample (not excluded); developmental stage. Not an encyclopaedia: the first two are separated by an Ih-blocker-sensitive sag at matched membrane potential and by voltage clamp; the third and fourth by cell-type labelling.
* Role (unresolved): sag is graded but bursts are not (HT shares sag and Vm, bursts in 4 of 23): the intrinsic change is at most necessary, not sufficient; whether it is compensatory (restraining excitability), pro-excitatory or a bystander is not decided. Discordant Ih-blocker precedents are the paper's own and the IT14 P3 caution; they set the direction as open.
* Intervention (hypothesised): an Ih blocker could lower bursts, raise them, or do nothing, depending on the role; benefit is not inferred. No HCN blocker enters any ranking.

## Consequence for the next steps
The interruption is between the qualified observation and a need: the intrinsic rival has no consumer. P3 adds the smallest structures that exist for this (a need with an unresolved direction and an investigation with conditional branches), then the existing need-to-catalogue search reaches the tools without being given a name; P4 checks the link on a second case; P5 compares and attributes.

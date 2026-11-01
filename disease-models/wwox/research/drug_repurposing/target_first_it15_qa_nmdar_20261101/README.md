# IT15 Q-A: target-first NMDAR search for partial functional benefit in Wwox neuron-deleted slices

## Corrections after independent verification (2026-11-01)

Source: `verify_it15_qa_20261101/README.md` and `verdicts_qa.tsv`; each item below was re-checked against the regenerated tables where it concerns them. Old -> new.

1. Grades. Old: 47 INTERPRETABLE / 603 LIMITED / 396 NOT_DETERMINABLE (1,046 groups), with a note that the grader's keyword list lacked "voltage clamp". New: the grader was edited during my run (TECH now contains "clamp" and "oocyte"); `graded_comparisons_qa.tsv` was regenerated offline with the CURRENT `selectivity_p6.py`: 1,045 groups = 496 INTERPRETABLE / 153 LIMITED / 396 NOT_DETERMINABLE. One group fewer: the dalzanemdor rows of CHEMBL6134891 (79 nM for all four GluN2 subunits, a reference value, ratio 1 meaningless) are ignored in grading. Obsolete reviewer notes were rewritten. Every count of 47/603/396 in this package is superseded by these figures. Ifenprodil, Ro 25-6981 (CHEMBL4308825) and memantine (CHEMBL1146243) now grade INTERPRETABLE; d-AP5 CHEMBL4024770 stays LIMITED (validity comment on GluN2C/D), CHEMBL1143579 is INTERPRETABLE (5.86x). The grader has no provenance check: a compilation can be graded as one experiment (see item 2).
2. H1 provenance. Old: "single document, human oocyte voltage clamp, two NAMs concordant". New: CHEMBL4308825 is a REVIEW (Burnell 2018, PMID 29446949). Ifenprodil (110 vs 39,500 nM, 359x) comes from Hess 1996 (PMID 8768735; human receptors, oocytes, 3 uM glycine, -40 mV); Ro 25-6981 (9 vs 52,000 nM, 5,778x) from Fischer 1997 (PMID 9400004; rat context; the same pair is also in CHEMBL1132364 = one origin counted twice). So: two independent papers compiled in a review; each ratio is internally same-paper; conditions differ between the two compounds. The agreement of the two windows is between papers, not within a document.
3. H1 prediction. Old: isolated-current reduction = 0.90 f + 0.025 (1 - f) (20/46/73% at f = 0.2/0.5/0.8). New: that expression equals sum_i f_i * Emax_i * occ_i with Emax = 1 and no triheteromer, i.e. an UPPER BOUND, not a prediction (ifenprodil inhibition is incomplete, PMID 22936815; triheteromers are only partially inhibited, PMIDs 15848804 and 24607230; pH dependence, PMID 9143010; oocyte IC50 at -40 mV is not a slice value). The percentages are withdrawn. f is defined operationally as the measured fractional reduction of the isolated NMDAR current by a saturating GluN2B NAM in that slice (E0). Old: "no source for f". New: Mierau 2004 (PMID 15492224; mouse barrel cortex L2/3, P7 and P14, ifenprodil sensitivity of L4-evoked NMDA EPSCs) exists, abstract level, percentage not read; no P13-P17 value for the isolated whole-cell NMDAR current in spontaneously bursting slices was found, and that is the quantity needed.
4. Queue anchors. Old: "seven not found". New: all resolve in ChEMBL by the queue IDs: acamprosate CHEMBL1201293 (89 activities, none on NMDAR targets, no mechanism record), AV-101 CHEMBL3545351, AZD8108 CHEMBL3707355, indantadol CHEMBL3707400, neramexane CHEMBL2106798, ralfinamide CHEMBL2107771 (each a mechanism record "Glutamate [NMDA] receptor antagonist" on CHEMBL2094124; AV-101, AZD8108, indantadol, neramexane have no activity rows, ralfinamide 16 none on NMDAR), delucemine CHEMBL2106165 (no mechanism, no activity), felbamate CHEMBL1094 (mechanism record; about 70 GluN2B rows of type Kapp 0.87-34.5 mM and % inhibition 61-90%). Those felbamate rows were invisible to this package's IC50/Ki/Kd/EC50 type filter: a stated perimeter limit. My name match on ten synonyms was the cause of the miss. None has a subunit comparison, so no case changes. `identity_qa.tsv` updated.
5. Truncated tail. The verifier read all 1,120 rows not retrieved by the three truncated queries (21 + 156 + 943). They hold esmethadone (CHEMBL350719), levomethadone, alphamethadol, pentamidine, chlorpromazine, amantadine (rat CGN IC50 92-358 uM) and two patent GluN2B series (CHEMBL5729488: 113 rows, 44 with IC50 <= 100 nM, human NR1/GluN2B; CHEMBL5729184: 17 rows; no GluN2A arm in the tail). They add a clinical-stage channel blocker to A1 and chemotypes to H1; none changes H1.
6. Pore-blocker ratios. Neither FLIPR format (U2OS CHEMBL1759939, CHO CHEMBL6115009) has a holding voltage, and CHEMBL6083260 shows a 30-fold spread inside one GluN2B arm (510 to 15,220 nM). Ratios of 4x or less between GluN2A and GluN2B are therefore inside assay noise: the supported statement is "no subunit selectivity detected", and "direction flips" is replaced by "direction not resolved" (3 of 4 ketamine documents favour GluN2B). Memantine and ketamine "negative allosteric modulator" records sit on the salt records CHEMBL1699 and CHEMBL1714 (a parent query returns none), target the generic seven-gene group CHEMBL2094124, and mean non-competitive in ChEMBL's vocabulary, not site- or subunit-resolved.
7. Discriminator. Old: "bursts fall faster per unit current for the NAM if GluN2B sustains them". New: that alone is not valid, because burst generation is threshold-like and any antagonist can give a steeper-than-linear fall. Restated design in section 5b below.

Status after the corrections: H1 stands as a hypothesis (class-level window of roughly 10^2 to 10^3 selectivity for GluN2B NAMs versus no detected selectivity for pore blockers and d-AP5; f still unmeasured), with its provenance and prediction weakened as stated. The four cases remain. Not resolved: holding voltages and agonist concentrations of the primary papers (not opened), the Mierau percentage, whether the 110 nM ifenprodil value recurring in three ChEMBL documents is one measurement, the cause of the previously shipped grade column, and ChEMBL's action_type definition text.

---


Research package (non-canonical). Not medical advice. Free, key-less sources only; nothing sent to any service except public GET requests; no e-mail, registration or spend. Question, criteria and cases were fixed in `PRE_REGISTRATION.md` before extraction. Labels used below: RETRIEVED (read from a source), VERIFIED (checked against a second place or re-read), GENERATED (my inference or calculation).

## 1. What was retrieved

ChEMBL_37 (2026-05-01) through `framework/adapters/chembl.py`; GtoPdb 2026.3.1 and DGIdb (cached files); DrugCentral file (downloaded, 0.96 MB, SHA-256 in `perimeter_log.tsv`).

| item | count |
|---|---|
| ChEMBL targets whose activities were pulled (human and rodent, single protein, defined complex, generic group) | 28 targets x 4 types (IC50, Ki, Kd, EC50) = 112 target-first queries |
| total_count vs retrieved, target-first | 15,276 vs 14,156 |
| truncated queries (cap 2000 rows) | 3: CHEMBL1904 (human GluN2B) IC50 2021/2000; CHEMBL1907603 (human GluN1/GluN2B) IC50 2156/2000; CHEMBL1907608 (rat generic NMDA group) IC50 2943/2000. 1,120 IC50 rows were not read; the first two are covered for the named compounds only by the molecule-first pulls below |
| molecule-first pulls for 15 anchor/tool compounds | 15 queries, no truncation, +31 rows not reached target-first |
| distinct activity rows in `relations_qa.tsv` (ChEMBL) | 14,187 (rat 7,709; human 6,387; mouse 88; pig 3); 8,887 parent compounds, 155 with a ChEMBL preferred name, 89 with a stated max phase >=1 |
| censored rows kept censored | 1,910; rows without value 374; rows with a validity comment 470 |
| GtoPdb / DGIdb / DrugCentral NMDAR rows | 160 / 414 / 74 (direction only for DGIdb) |
| graded same-document comparisons (`graded_comparisons_qa.tsv`) | 1,045 groups (regenerated, current grader): 496 INTERPRETABLE, 153 LIMITED, 396 NOT_DETERMINABLE (grading logic imported unchanged from `scout_it14_p6_20261101/selectivity_p6.py`) |

Failures: the accession queries for GRIN2A (timeout) and GRIN2B (HTTP 500) failed after one attempt plus two retries; the gene-search fallback worked for GRIN2A and GRIN2D, failed for GRIN2B, GRIN1, GRIN2C; 35 failed HTTP attempts in total are logged in `raw/failures_*.json`. These are "not retrieved", not "no target". The activity stage had zero failures. Gaps that follow: (i) rat/mouse GRIN2B and rat GRIN1/GRIN2B targets were first missed, then found through the molecule-first pulls (rows carried CHEMBL311, CHEMBL2096666, CHEMBL3442, CHEMBL330, CHEMBL401, CHEMBL2096911) and pulled target-first afterwards; (ii) mouse GRIN1/GRIN2A/GRIN2C/GRIN2D targets, human GRIN2A/GRIN2B single-protein targets, and the human GRIN1/GRIN2A-D complexes are covered only through the IDs known from earlier modules (CHEMBL1972, CHEMBL1904, CHEMBL1907603/4, 3038504/5) - not discovered by this run's own accession query (deviation D1); other targets that contain these accessions but were never listed may exist; (iii) UniProt accessions identify human proteins only, so "human and rodent" was reached through gene search and molecule-first, not by accession.

Exclusions: 1,170 assay contexts kept; GRINA (a different gene) excluded from DGIdb; molecule-first rows kept only if gene contains GRIN or target name contains NMDA; DGIdb rows with null drug ("NULL") not used. Same value repeated across documents (eliprodil Ki 13 nM in 9 documents, ketamine Ki 180 nM in 13 generic-complex rows, GtoPdb SAGE-718 = ChEMBL dalzanemdor 79-86 nM) is one origin counted once.

## 2. Anchors versus new compounds

Of the 20 NMDAR entries of `ranking_it8_p9_20261029/deepening_queue.tsv`: 12 were found target-first in ChEMBL (amantadine, dextromethorphan, ketamine, esketamine, memantine, traxoprodil, lanicemine, perzinfotel, orphenadrine, GW468816, rislenemdaz, EVT-101); felbamate only in DrugCentral/DGIdb (GluN2B IC50 pX 4.28, one row); acamprosate, AV-101, AZD8108, delucemine, indantadol, neramexane, ralfinamide are NOT absent from ChEMBL: they were missed by my name match and resolve by the queue IDs (see correction 4); they have mechanism records or no NMDAR activity rows, not subunit values. Named compounds found target-first and NOT in that queue: ifenprodil (and its (S), (R,S), (S,R) forms, kept apart), Ro 25-6981, radiprodil, eliprodil, dizocilpine (MK-801), phencyclidine, selfotel, d-AP5, AP-7, dalzanemdor, D-cycloserine, glycine, D-serine, 7-chlorokynurenic acid, licostinel, gavestinel, eglumetad, besonprodil, NBQX, YM-90K and others (full list from `raw/molecules_all.json` joined to `relations_qa.tsv`). Several of the first group were already assessed in `nmdar_pharmacology_it6_p9_20261029` (ifenprodil, Ro 25-6981, radiprodil, NVP-AAM077, memantine); the queue omitted them because they are tools or pre-clinical there.

## 3. Verified and corrected

* VERIFIED as numbers, CORRECTED as provenance: Ro 25-6981 9 vs 52,000 nM and ifenprodil 110 vs 39,500 nM are in CHEMBL4308825, a review compiling two independent papers (Hess 1996; Fischer 1997); see the corrections section. Ifenprodil arms state 3 uM glycine, -40 mV. The current grader grades them INTERPRETABLE; the reviewer_note states that a compilation is not one experiment. Ro 25-6981 arms state neither voltage nor glycine.
* CORRECTED/CAUTION: the grader marks the CHO calcium-flux panel CHEMBL6115009 (24 h incubation, unknown-origin receptors) INTERPRETABLE for MK-801, ketamine, memantine and dextromethorphan. It has no voltage control and no Mg2+; for use-dependent blockers that is the variable that matters, so the ratios do not transfer to a slice (note in the table).
* CORRECTED: ChEMBL labels memantine, ketamine and esketamine "negative allosteric modulator" on the generic NMDA group target. That is the ChEMBL vocabulary; these are pore blockers, not ifenprodil-site modulators (mechanism class from prior knowledge, UNVERIFIED in this run beyond DrugCentral/DGIdb "blocker").
* VERIFIED gap: radiprodil has values only on the GluN1/GluN2B complex and the generic seven-gene complex (NOT_DETERMINABLE; no ratio). Its GluN2A potency is not retrievable here. Traxoprodil: GluN2B 73 nM rat, GluN2A and GluN2C censored >100,000 nM (kept censored; NOT_DETERMINABLE).
* ketamine and esketamine are separate parents; the 13 generic-complex Ki rows of ketamine are one value (one origin).
* Compound CHEMBL6176014 shows 53% maximal block on a GluN1/GluN2A/GluN2B construct (oocyte): an unidentified NAM, not ifenprodil, so no generalisation to triheteromers is made.

## 4. What was generated

Same-document potency ratios (GluN2A over GluN2B), human unless stated: Ro 25-6981 5,778x and ifenprodil 359x (one document); ifenprodil 429x (second document, validity comment on the GluN2A value); rat (S,R)- and (R,S)-ifenprodil 182x; eliprodil rat 71x (GluN2A 100 uM, GluN2B 1.4 uM); d-AP5 rat Ki 0.14x and 0.6x, i.e. mildly GluN2A-preferring; memantine 0.9-2.1x; ketamine 0.25x (U2OS flux) and 4x toward GluN2B (CHO flux) - direction not resolved (ratios <=4x are inside assay noise); MK-801 4x toward GluN2B; PCP 0.3x; dalzanemdor (PAM) 1.09x. Within same-document data the GluN2B NAMs span 71-5,800x; every pore blocker and the competitive reference span no more than 7x between GluN2A and GluN2B.

Occupancy window (calculation, Hill coefficient 1, oocyte IC50s, not slice; occupancy is not inhibition, see correction 3): ifenprodil 1 uM occupies 90% of GluN2B and 2.5% of GluN2A; Ro 25-6981 100 nM, 92% and 0.2%.

## 5. What the cases add (P3.4; `cases_qa.tsv`, `chain_qa.tsv`)

| case | role | adds over known literature |
|---|---|---|
| K1 d-AP5 | known reference | comparison previously missing: target-first subunit values for the reference |
| H1 GluN2B NAM (ifenprodil / Ro 25-6981; radiprodil comparator) | hypothesis emerged | new prediction in numbers (below); documented comparison gap for radiprodil |
| A1 pore blockers (memantine, ketamine, MK-801) | different mechanism | premise restriction: pore blockers are not subunit-selective, with the direction not resolved between documents |
| D1 PAM dalzanemdor, D-cycloserine, glycine (opposed actions); D2 GluN2A NAM TCN-201 | counter-hypothesis / discriminating control | discriminating experiment: the bidirectional test |

Experiment-level statement (GENERATED, hypothesis; superseding the earlier percentage formula): the isolated-current reduction by a GluN2B NAM is at most sum_i f_i * Emax_i * occ_i (upper bound); f is defined as the measured NAM-sensitive fraction and is measured first (E0), in the same animals and genotypes. No number is predicted for it.

### 5b. Discriminating design (restated after verification)
Primary comparison: burst incidence/frequency against MEASURED fractional reduction of the isolated NMDAR EPSC, for (1) an equal-current d-AP5 titration, (2) a low-trapping pore blocker titration (memantine class), (3) two structurally unrelated GluN2B NAMs (Ro 25-6981 and CP-101,606 or radiprodil; ifenprodil off-target actions at sigma and alpha-1 sites are prior knowledge, UNVERIFIED here), (4) TCN-201 as the GluN2A arm with glycine fixed and reported, (5) a PAM arm as the bidirectional gain control (dalzanemdor is not GluN2A/GluN2B-selective, 79 vs 86 nM, so it tests gain, not subunit). A steeper burst-versus-current curve than a linear reference is NOT evidence of subunit specificity (threshold-like bursting); only a leftward shift of the NAM curve relative to curves (1) and (2) at matched measured current supports GluN2B-specific sustaining, and coincident curves support "total NMDAR current limits bursting". Alternatives to exclude: interneuron or recruitment effects of GluN2B (record interneuron NMDAR sensitivity, hold GABA-A tone), extrasynaptic or tonic GluN2B and activity-dependent block (Fischer 1997) that make a NAM effect grow during bursts, presynaptic and glial NMDARs, the GluN2B-to-GluN2A switch inside P13-P17 (f differs between animals), a KO-specific change of NMDAR composition (E0 KO vs WT), and fixed pH, glycine, Mg2+ and temperature throughout. Wording of the earlier statement "bursts fall faster than current" is withdrawn.

## 6. Why near alternatives were left behind

* Radiprodil: fails criterion (i) (no GluN2A or defined-heteromer comparison retrievable); kept as clinical-stage comparator, not deepened.
* Esketamine and ketamine: esketamine has no GluN2B value; ketamine is deepened only as part of A1 because its two INTERPRETABLE comparisons contradict each other.
* Glycine-site antagonists (7-chlorokynurenic acid, licostinel, gavestinel; AV-101 not found): their rows are on GluN1 or the generic complex; no subunit comparison, so no case for that class.
* Competitive agents other than d-AP5 (selfotel, AP-7): rat membrane binding on the generic complex, not subunit values.
* Memantine and felbamate: ASSESSED_ELSEWHERE; cited, and only the new same-document ratios added.
* AMPAR agents (NBQX, tezampanel, perampanel): outside the question (NMDAR targeting).

## 7. What failed

GRIN2A and GRIN2B accession queries; gene search for GRIN2B, GRIN1, GRIN2C; f not measured (Mierau 2004 abstract only); no retrievable radiprodil GluN2A value; no subunit comparison for the glycine-site antagonist class; 7 queue entries not found target-first by my name match (they exist in ChEMBL, see correction 4); felbamate Kapp/% inhibition rows excluded by the type filter.

## 8. What remains searchable

Remaining 1,120 truncated IC50 rows (page offset beyond the adapter cap); a rerun of the failed accession and gene queries; target discovery for mouse subunits; the primary papers behind CHEMBL4308825, CHEMBL5625199, CHEMBL6115009, CHEMBL1759939 (assay voltage, Mg2+, glycine); an electrophysiology paper giving the ifenprodil-sensitive fraction in mouse L2/3 pyramidal cells at P13-P17 (full text of candidates not opened); the GtoPdb release has no ifenprodil, Ro 25-6981 or radiprodil NMDAR rows in this cache.

## 9. Verification burden for the independent verifier

1. The five numbers 5778x, 359x, 429x, 4x/4x (ketamine, MK-801 in CHEMBL6115009) and 7x (d-AP5, CHEMBL4024770) against `relations_qa.tsv` and the assay descriptions in `assay_context_qa.tsv`.
2. The reviewer notes overriding the keyword artefact (CHEMBL4308825, CHEMBL1146243).
3. Anchor-vs-new classification: now corrected by the verifier; re-check `identity_qa.tsv`.
4. The occupancy arithmetic (confirmed by the verifier; occupancy is not inhibition).
5. Perimeter counts in `perimeter_log.tsv` (truncated queries; failures).
6. That dalzanemdor and SAGE-718 are one compound and one origin (document id not checked).

## 10. Deviations

Logged in `PRE_REGISTRATION.md`. Files: `PRE_REGISTRATION.md`, `perimeter_log.tsv`, `relations_qa.tsv`, `assay_context_qa.tsv`, `graded_comparisons_qa.tsv`, `identity_qa.tsv`, `chain_qa.tsv`, `cases_qa.tsv`, scripts (`pull_it15_qa.py`, `pull_genesearch.py`, `names_it15.py`, `names_all_it15.py`, `build_relations_qa.py`, `finalize_it15_qa.py`), `raw/` (adapter outputs, 35 MB, ChEMBL CC BY-SA 3.0 attribution: Data from ChEMBL, EMBL-EBI; GtoPdb ODbL/CC BY-SA 4.0; DrugCentral CC BY-SA 4.0 by link).

## Note by the integrator after the hostile review (2026-11-01)

The grader was tightened after this package was finalised (stimulus, holding voltage and agonist concentration stated in the assay description must agree or the group is LIMITED and offers no ratio; SLC/CYP-type symbols are families by their first digit run; a family row identical to its panel row is not repeated). `graded_comparisons_qa.tsv` was regraded with the current grader: 1,037 groups = 492 INTERPRETABLE / 153 LIMITED / 392 NOT_DETERMINABLE. These are the counts that replace the earlier ones in this package. INTERPRETABLE means compatible on the fields examined (most groups are series from one paper in one format); assay descriptions rarely state agonist concentrations, so the label does not mean the conditions were checked, and the INTERPRETABLE groups were not individually reviewed. The H1 and A1 statements above do not rest on that count.

## Where the raw responses are (integrator note)

The raw ChEMBL, GtoPdb, DGIdb and DrugCentral responses of this package (35 MB) are not tracked in the repository: they are third-party data, large, and re-fetchable. Their SHA-256 digests are in `raw_SHA256SUMS.txt`; a local copy is kept in the shared corpus at `files/drug_repurposing_it15/target_first_it15_qa_nmdar_20261101/raw/` (ignored by git). ChEMBL data are CC BY-SA 3.0 (EMBL-EBI); the derived tables in this directory carry the same attribution.

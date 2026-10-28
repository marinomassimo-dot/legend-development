# Independent verification of the GtoPdb ligand reconciliation (P4), 2026-10-29

Producer: plan worker. Verifier: independent subagent, own InChIKey comparison on GtoPdb ligands.csv and live ChEMBL REST, whole non-out-of-selection population (558 pairs). Verdict: no false merge; merged 485/485 agree; defects low (ADL5859 held for a disjoint DrugBank id; LX2931 and GNE-7883 are tautomer depictions rejected as conflicts; two recoverable false splits; README count 2,473/54 corrected to 2,472/55).

# P4 ligand reconciliation: independent verification (scientist-c)

Method: GtoPdb ligands.csv (2026.3.1, published 2026-10-12) and ChEMBL REST molecule endpoint (keyless), decided by my own rule
(full InChIKey equal and not labelled/radioactive = merge; block 1 differs = reject; block 1 equal, block 2 differs = related stereo/isotope;
labelled/radioactive = related; missing structure or record = unresolved) BEFORE reading the producer's decisions/reasons.
Then I extended it to the whole non-out_of_selection population (558 rows, 555 ChEMBL ids), so the sample result is a floor.
Scripts and data: <scratchpad> (mine.json, sample.json).

## Agreement table (my independent decision vs producer)
| class | sampled | agree (sample) | agree (whole population) |
|---|---|---|---|
| merged | 41 (40 + CPP-115) | 41/41 | 485/485 |
| related_not_merged | 14 (all) | 14/14 non-merge; 13/14 on sub-reason (NCGC 84, see D3) | 14/14 non-merge |
| rejected_conflict | 4 (all) | 4/4 correct as non-merge; 2/4 are tautomer cases (D2) | same |
| unresolved non-INACTIVE (7 in the 510 + 2 absent + PBF-509 + 5-HMF) | 11 | 8/11 (disagree: ADL5859 D1, PBF-509 and 5-HMF D4) | same 11 (these are all of them) |
| unresolved INACTIVE | 10 of 44 | 10/10 (ChEMBL id INACTIVE, no record; no InChIKey hit for these 10) | 44/44 (2 have an IK hit under another ChEMBL id, CTA091 and sarafotoxin S6b, neither in the catalogue: nothing to merge) |
| out_of_selection | 10 | 10/10 (ACTIVE, structure equal, CAT:CHEMBL<id> absent) | 2472/2472 have no CAT:CHEMBL record |

Edge cases: CPP-115 merged, full IK CBSRETZPFOBWNG-UCORVYFPSA-N both sides (single stereoisomer, correct). ADL5859 unresolved (D1).
LX2931, BMS-817399, CP-10, GNE-7883 rejected (D2). Vigabatrin: GtoPdb 4821 -> CHEMBL89598 exists, but the DGIdb "Vigabatrin"
record (CAT:DGIDB:358b8a817686) carries rxcui only, no iuphar.ligand id, so it is not in this pair set at all (out of scope, not a defect of the rule).
Racemate/enantiomer: atracurium (flat IK both sides, racemic/mixture, merged OK), (+)-butaclamol (GtoPdb IK stereo-defined and equal to ChEMBL BUTACLAMOL, merged OK, see D5).
Salt-form id: NCGC 84 -> CHEMBL1474387 (ChEMBL bromide salt, IK ...-M, GtoPdb cation) = related_not_merged, correct. Radioligands: all 7 [3H]/labelled
ligands (ancriviroc, muscimol, BSP, mirogabalin, D-aspartate, NLX-112, tyramine) have IK identical to the ChEMBL unlabelled parent and are kept related_not_merged: correct, no isotope distinction lost.

## False merges
None found. All 485 merged pairs have full standard InChIKey equal; none has Labelled/Radioactive set; no duplicate ChEMBL id or ligand id among merged;
3 ChEMBL targets are non-parent forms (CHEMBL88223 PCS1055, CHEMBL4789639 BMS-986202 child of CHEMBL4803710, CHEMBL4301914 contezolid acefosamil parent): IK equal to GtoPdb so identity holds. Names of 3-way-disagreeing pairs (ML355 = onvoloxastat = VLX-1005; M4205 = velzatinib = IDRX-42) are genuine synonyms.
## False splits / disagreements
D1 (low) ADL5859 (CAT:DGIDB:91a0f0841ec5, lig 9004, CHEMBL494480): full IK equal, achiral; producer unresolved only because DrugBank ids disjoint (DB05050 vs DB18910).
I would merge on structure, but the disjoint-DrugBank guard is independent contrary evidence, so this is a defensible conservative choice, not an error.
D2 (low) LX2931 (9851) and GNE-7883 (12814): identical molecular formula (C9H15N3O5; C28H29FN6O2), IK block 1 differs only by tautomer depiction (nitroso vs oxime; pyrazolopyrimidinone tautomer).
Same compound pharmacologically; "rejected_conflict / connectivity differs" is stricter than needed and mislabels a tautomer as a conflict; a related_not_merged (tautomer) bucket would be accurate. BMS-817399 (formula C23H35ClN2O4 vs C23H36ClN3O4, amide vs urea) and CP-10 (CHO vs acetyl, C43 vs C44) are real conflicts: rejection correct.
D3 (info) NCGC 84: producer reason (GtoPdb is parent cation, ChEMBL ref is the bromide salt) is right; my IK-only rule would call it a connectivity difference. Agree with non-merge.
D4 (low) two unresolved that an InChIKey lookup would resolve: 5-HYDROXYMETHYL-2-FURFURAL (GtoPdb ChEMBL ID typed "ChEMBL185885", not normalised; CHEMBL185885 AES-103 has the identical IK NOEGNKMFWQHSLB-UHFFFAOYSA-N and IS in the catalogue as CAT:CHEMBL185885) and PBF-509 (GtoPdb id CHEMBL3638684 is not a compound record; CHEMBL3694769 PBF-509 has the identical IK ATFXVNUWQOXRRU-UHFFFAOYSA-N and IS in the catalogue). Both are false splits by structure; a case-insensitive CHEMBL-id normaliser and an IK fallback would recover them. Others among the 44 INACTIVE: CTA091 and sarafotoxin S6b have an IK hit under another id (CHEMBL389014, CHEMBL4524099) not in the catalogue: nothing to merge.
D5 (info) (+)-butaclamol merged with ChEMBL BUTACLAMOL whose chirality flag is 0 (racemic) although its stored IK is stereo-defined (HWBMXIPRSA); equal IK so the merge is formally right; the ChEMBL flag is the inconsistent part. Evidence recorded, not decisive.

## Totals reconciliation
- TSV ligand_reconciliation.tsv: 3,030 rows = merged 485, related_not_merged 14, rejected_conflict 4, out_of_selection 2,472, unresolved 55 (44 INACTIVE, 2 ligand absent, 1 not a compound record, 1 unknown to lookup, 4+1+1 structure unavailable, 1 DrugBank disjoint). ligand_reconciliation_not_merged.tsv = same minus the 485 merged (2,545 rows).
- DEFECT D6 (low, documentation): catalog/README.md table says out_of_selection 2,473 and unresolved 54 (with "6 structure unavailable" and no "not a compound record"). The TSV and catalog_stats.json (decisions_all_pairs_with_a_relation: out_of_selection 2472, unresolved 55; reasons list "chembl_id_is_not_a_compound_record": 1) are right; README is off by one (PBF-509 counted as out_of_selection). Sum 2,527 is unchanged. The task brief repeats the README figures.
- 6,597 = 2 absent + 3,567 no ChEMBL id + 3,028 with a ChEMBL ref (= 485+14+4+2,472+53 unresolved with a ref); consistent with catalog_stats.json. (The TSV holds the 3,030 pairs that have a relation, not all 6,597.)
- 510 pair set: ligand_identity_merge_candidates.tsv (510 data rows) vs TSV rows with chembl_ref_in_catalogue=yes (485+14+4+7): identical as sets of (record id, ligand id, ChEMBL id); symmetric difference empty. The 7 unresolved are ADL5859, the 4 structure-unavailable-both-sides (otlertuzumab, avacincaptad pegol, naptumomab estafenatox, anatumomab mafenatox), O3 (GtoPdb side), mongersen (ChEMBL side).
- Family claim VERIFIED: recomputing from catalog.jsonl.gz (44,211 records; 19,933 ChEMBL records; 24,278 others), ChEMBL families by union of parent/child and identical IK block 1 = 16,475; before = 16,475 + 24,278 = 40,753; the 485 records with relations.family_join (each one target, all pointing at a catalogue ChEMBL record) stop being singletons: 40,753 - 485 = 40,268 (= coverage_summary.json "families": 40268). A simpler parent-only grouping gives 40,975 -> 40,490 (same delta of 485).

## Defect list
| id | severity | summary |
|---|---|---|
| D1 | low | ADL5859: structure-equal pair withheld on a DrugBank disjointness guard (defensible) |
| D2 | low | LX2931, GNE-7883: tautomer depictions labelled rejected_conflict instead of related (no harm; nothing merged wrongly) |
| D4 | low | 2 recoverable false splits (mis-cased "ChEMBL185885"; PBF-509 non-compound id) where IK equals a catalogue ChEMBL record |
| D6 | low | README table counts 2,473/54 vs TSV and stats 2,472/55 |
| D5 | info | ChEMBL chirality flag 0 with stereo-defined IK on butaclamol |
No false merge, no high or medium defect.

## Sample list (DGIdb record id suffix after CAT:DGIDB: / GtoPdb ligand id)
merged (41): 0a2199127751/8284 3c0929da491b/11623 7f274d428aba/10504 6f545890ad8a/11315 6222dc0bf89c/1014 bb041b9fb227/2420 b2952b57b6ea/8913 3b71d4b2f65d/12888 3c465800f920/5661 7fefddf21c30/12620 1d6318ea1b46/552 a7310a08862a/7829 f2bf2bb8466b/1226 e3bd918f5216/7885 f982763e0b37/5715 3c038fe496ce/4327 e0afaa27f473/8474 0a1a5411f566/3151 ba4f74fa4b50/12433 1aaa8dc8d34d/7811 39b7c0639ed4/7020 878be3ca8134/11782 128469bdc67a/7374 b0df160b76fd/145 961478eae6e3/8026 615a4339a310/1528 2d313382753e/11685 ce0ff42dc560/12076 2a38732231ba/7965 d2d25b332126/11783 c79620d25b8b/7701 6a6f76a0653a/9911 c147fe2f1230/5613 3285fe48a942/9003 dd1ef40ad310/9052 435dffd0a135/5243 8982c636eeb9/12068 31217e9af50f/2658 4165b82d60bd/2429 526dee97e7b9/7377 67f594cf00a5/11499
rejected_conflict (4): 3f26c205f5f3/9851 776544e215a0/9497 f2ef4d444789/11662 ff06e01b6051/12814
related_not_merged (14): 1980d34e46c8/802 35b76d3ae69f/8425 4672c61ea035/4090 483a4ef3b77a/4505 568c13f2da00/9058 5d856f767874/9032 95ff180c19e5/9168 9d6dff82ffc9/12597 9ec52dbec023/4698 a75772bdf7ab/3925 bedef913f6bf/11865 e60a64e292f5/9057 f210d9186449/2148 f64120b00e61/12209
unresolved (21; 11 non-INACTIVE incl. the 7 of the 510 + 10 INACTIVE): 91a0f0841ec5/9004 11bbc6e3c7ad/10193 157e740170bf/9951 52a3e992a951/10939 763f051faec1/12689 8a3fa713812e/2092 974d855b5b00/6297 a19a6a07320d/12857 b0b89574234e/9948 d564ef2461e5/8277 e5f1a4796795/9947 ecdc7f343cec/3483 dc5d3ce57f1d/3979 e92d372482a1/1966 22e494a39fe3/1000 f8349bfa0e27/1008 526035ccfae7/3974 f6880635c428/1220 b91b86a6cc9a/9193 d758b5358b3d/3471 46451bf65556/8819
out_of_selection (10): 6de7a86cff33/8608 02e9819d35b8/3232 c3894f94949f/466 619feb4ba733/3531 fcf265ee295a/11480 5af38e748691/5619 f82d6d28d1e6/5601 0cb62ef37c5d/385 f857b71ad12c/7943 00a9b8a9868f/4352
(seed 20261028; candidate ids are CAT:DGIDB:<suffix>)

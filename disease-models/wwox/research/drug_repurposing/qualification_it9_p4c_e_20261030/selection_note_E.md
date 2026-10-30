# Selection note E (IT9 P4c-e, round 2 on the provenance-repaired path) and decision rules

Scientist-b4, 2026-10-30, branch `task/it9-p4c-e`. Written BEFORE any activity, label, expression, trial or paper data of a selected compound were opened. Not medical advice. A compatible action of a context-free signed network is not a predicted benefit.
Reference genotype: a WWOX-DEE genotype class; no individual-level record; no e-mail address or operator identity is sent to any service.

## 0. What had been seen before this file

* Read: the v3 README and pre-registration of P2, the whole `candidates_Q2.tsv` and `candidates_Q6.tsv` (names, arm, rank, Z in the three nulls, flags, strongest chain), the P3 `selection_rules.md` (with its amendments), the round-1 READMEs (a, b, c) and the Q6 MYC seed assessment, the P3 identity map and ChEMBL profile (aggregate lookups only).
* Looked up for selection only (feasibility axis, file `selection_feasibility.tsv`, log `selection_service_log.tsv`, 26 attempts, all HTTP 200): ChEMBL molecule search by name for 26 names (id, max phase, molecule type, oral/parenteral flag, first approval).
* Looked up for edge existence only (not read): the OmniPath records of the chain edges (source database and reference ids), to know whether an edge is present in the live resource at all. No paper was opened.
* Not seen: any activity row, label, trial list, expression value, or paper text of a selected compound.

## 1. Rules applied (P3 `selection_rules.md`, sections 3 to 5, unchanged unless stated)

Promise and feasibility stay separate columns. Feasibility tests F1 (cytotoxic anticancer by ATC L01A/B/C/D/XA or stated cytotoxic mechanism), F2 (topical only), F3 (modality: antibody, oligonucleotide, peptide), F4 (no resolved identity), F5 (no human exposure information), F6 (withdrawn for toxicity). Seed-specific = beyond 3 in all three nulls (v3 definition). Unit = P2 family, collapsed to a parent. Mechanism cluster = main target of the chain. Z used in key (d) = min(|Z_total|, |Z_indeg|) capped at 20 (the Q6 protein MYC set has Z in the thousands: the cap removes it as a ranking quantity). Q6 (one MYC seed; expression and protein counted together) weighs at most 4 of the selected set. Q2 at least 2 (one opposes, one mimics). Already qualified in round 1, excluded: balsalazide, ramelteon, ceperognastat, harmine, pomalidomide, defosbarasertib, pinometostat, AR-12, dichloroacetate, sirolimus, lenalidomide, AT9283 (and fosfestrol, implitapide, curcumin, belnacasan, JTE-151, felbamate, memantine of group B). Belzutifan: not selected as a family; re-opened only for its missing datum (section 4).

**Amendment E1 (this round; disclosed).** P3 F5 excludes compounds with no human exposure information. The assignment names mechanism classes for which every member in the v3 lists is a research tool compound (PIN1, METTL3, DYRK1A/CSNK1A1 through FOXO6, ESRRA). Applying F5 as an exclusion would remove all of them and leave only classes the assignment did not name. For this round F5 is a FLAG, not an exclusion, for a class in which no member passes it: the family is labelled `mechanism_probe`, its feasibility column is LOW by construction, and its decision rests on the edge and target questions (is the mechanism real in a neural cell relevant to the seed), not on a treatment route. Every other test (F1, F2, F3, F4, F6) stays an exclusion. This amendment is a judgement setting fixed now, not tuned on outcomes.

**Amendment E2 (tie rule within a mechanism cluster).** Where members of one cluster differ in min(|Z|) by less than 0.5, or are equal after the cap, the representative is chosen by feasibility: (i) identity resolved in ChEMBL (F4); (ii) human exposure (approved before clinical before tool); (iii) a published selectivity or in vivo characterisation; (iv) family id. Members not taken are named as comparators in the record.

## 2. The operator's shortlist and the mechanical check

The shortlist of clusters is the assignment's own (HIF1A inhibitors, HIF-PH inhibitors, XCT790/ESRRA, PIN1, METTL3, NOTCH axis, DYRK1A/CSNK1A1 through FOXO6): seven clusters for at most six places. They were checked against the whole v3 lists by key (d); the check changes the picture in one respect, reported here and not hidden: **the JAK2 -P-> MYC protein cluster (fedratinib, pacritinib; approved; min capped Z 15.7) and the PGR and CREBBP clusters rank above PIN1 on key (d)**, but were not on the shortlist and are listed as `not_taken` below. The selection is therefore "shortlist, then rules", not "rules alone".

| Cluster | Set and arm | Chain to the seed (v3) | min capped Z | Feasibility of the best representative | Taken |
|---|---|---|---|---|---|
| HIF1A | Q2 expression, opposes | HIF1A -T(+)-> BNIP3 (SIGNOR label) | 8.1 | PX-478: phase 1, ChEMBL CHEMBL4117516; flag: bis(2-chloroethyl)amino group (nitrogen mustard N-oxide) so a cytotoxic-alkylator alert; no ATC, F1 not triggered by the P3 definition; oncology_targeted; ChEMBL types it as "Protein" (to be checked by structure) | YES |
| EGLN (HIF-PH) | Q2 expression, mimics | EGLN2 -P(-)-> FOXO3 -T(+)-> SLC2A1/BNIP3 | 5.4 | roxadustat approved (EU, JP, CN; first approval 2021 in ChEMBL), daprodustat and vadadustat approved 2023, desidustat phase 3, molidustat phase 2. Z within 0.04 of each other (tie rule E2) | YES, roxadustat |
| NOTCH axis (gamma-secretase) | Q6 expression, opposes | APH1A/PSEN1 -P(+)-> NOTCH3 -T(+)-> MYC | 12.9 | nirogacestat approved (2023, desmoid), MK-0752 phase 1, osugacestat phase 2; same Z | YES, nirogacestat |
| METTL3 | Q6 protein, opposes | METTL3 -P(+)-> USP13 -P(+)-> MYC | 20 (capped; raw 1286) | STM2457 research tool (ChEMBL CHEMBL5405231, no phase); STC-15 is clinical but has no resolved ChEMBL identity (F4: excluded) | YES, STM2457 as `mechanism_probe` |
| DYRK1A / CSNK1A1 via FOXO6 | Q6 expression, mimics | kinase -P(-)-> FOXO6 -T(+)-> MYC | 20 (capped) | all members tool compounds; harmine (round 1) is the only DYRK1A member with human exposure and is already DROP. Not class-known: CSNK1A1 side; D4476 (CHEMBL410456) | YES, D4476 as `mechanism_probe`; GNF4877/GNF2133 (DYRK1A) are comparators in the same edge record |
| PIN1 | Q6 expression, opposes | PIN1 -T(+)-> MYC (CollecTRI label) | 11.2 | all members tool compounds (sulfopin, AG-17724, BJP-06-005-3); sulfopin is the selective covalent probe with in vivo data in the literature (to be verified, not assumed) | YES, sulfopin as `mechanism_probe` (tie rule E2 (iii)) |
| ESRRA | Q2 expression, mimics | ESRRA -T(-)-> LDHB | 5.4 | XCT790 tool compound (CHEMBL189753) | NO: Q2 mimics already represented; lowest min capped Z of the seven clusters; a third probe family would exceed what the round can read at primary-paper depth |

Count: 6 taken (Q2 2, Q6 4 = at the cap), opposes 4 and mimics 2. The P3 rule "at least 4 opposes and 4 mimics overall" is a 12-to-20 set rule and cannot hold for 6; stated, not forced.

## 3. Exclusions and reasons (promise columns kept)

| Family or cluster | Set, arm, adm-null Z | Reason |
|---|---|---|
| Anti-HIF1A LNA antisense oligonucleotide (EZN-2968) | Q2 opposes, 7.4 | F3 modality (oligonucleotide) |
| Nitroglycerin | Q2 opposes, 7.4 | HIF1A is not its pharmacological target in the sources I know of; the HIF1A credit is a DGIdb-type annotation; same chain as PX-478 so it adds no information; not examined |
| XIAP antagonists (SM-122, birinapant, xevinapant, GDC-0152, AZD5582, ASTX-660, LCL-161) | Q2 opposes, 6.5 and 3.1 | oncology agents (apoptosis-sensitising); would need a separate XIAP -> HIF1A edge qualification; budget |
| HDAC5 -> SLC2A1 cluster (pracinostat, panobinostat, vorinostat, valproic acid, 4-phenylbutyrate and 30 more) | Q2 opposes, 3.4-5.6 | one CollecTRI edge shared by 30+ families, hub-like cluster with a high median promiscuity (pan-HDAC inhibitors); valproic acid and 4-PBA are class-known to LEGEND; not taken for diversity |
| Belzutifan, PT2385 (EPAS1 -> LDHA) | Q2 opposes, 2.75 (fails the third null) | already qualified (INCONCLUSIVE); re-opened for one datum only (section 4) |
| Sorafenib, regorafenib (ZHX2 -> HK2) | Q2 mimics, -11.7 / -10.4 | targeted oncology multikinase agents with a ZHX2 annotation that is probably a catalogue artefact (not a sorafenib target in ChEMBL to my knowledge); not examined; candidate for a later round |
| TYRO3, GRK5, PRKCA clusters (tool compounds) | Q2 mimics | Q2 mimics slot filled; tool compounds |
| Mesalamine / balsalazide / olsalazine / indomethacin (PPARG -> HK2) | Q2 mimics | balsalazide qualified in round 1 (DROP: metabolite target); the others share that chain |
| XCT790 (ESRRA) | Q2 mimics, -4.0 | section 2 |
| Tarextumab, brontictuzumab, vantictumab | Q6 | F3 modality (antibody) |
| PRI-724, CBP bromodomain probes (I-CBP112, SGC-CBP30), WDR5 probe OICR-9429 | Q6 opposes | not on the shortlist; CREBBP -T-> MYC cluster; WDR5 -> CREBBP; budget |
| PGR modulators (onapristone, asoprisnil, lonaprisan) and cyproterone acetate | Q6 | not on the shortlist; PGR -> MYC is a breast-cancer-context CollecTRI edge; budget |
| JAK2 cluster (fedratinib, pacritinib, momelotinib-type) | Q6 protein opposes, 13.5-16.3 | **ranks above PIN1 on key (d)**; not on the shortlist; approved drugs with CNS safety signals (e.g. a boxed warning on encephalopathy for fedratinib in the US label, to be verified); recommended for the next round |
| AURKB, DOT1L, CRBN clusters | Q6 protein | round 1 |
| BRD4 cluster (JQ1, mivebresib) | Q6 protein mimics, z -1031 | saturated z of a single-gene set; BRD4 -P(-)-> MYC is a text-mined edge; tool compounds |
| GSK3 inhibitors (SB-216763, AZD1080, CHIR-98014) | Q6 mimics, -6.8 | not on the shortlist; GSK3A -> NOTCH1 -> MYC; budget; note that GSK3 is already a LEGEND topic (Q7) |
| PIM, caspase, ALDH2/HDAC3 (disulfiram), CDKL1, FZD2 (vantictumab) clusters | Q6 | not on the shortlist; budget |
| STC-15 | Q6 protein opposes | F4: no resolved identity in ChEMBL (name search returns unrelated molecules); remains the clinical comparator for the METTL3 record |
| AG-17724, BJP-06-005-3 (PIN1) | Q6 opposes | comparators of sulfopin |
| MK-0752, osugacestat | Q6 opposes | comparators of nirogacestat |
| Daprodustat, vadadustat, desidustat, molidustat | Q2 mimics | comparators of roxadustat |

Denominators: Q2 v3 list 152 rows (50 opposes, 25 mimics, 50 direct, 27 flagged) and Q6 list 298 rows, of which the unflagged opposes/mimics rows considered are 225 (rows, not families: salts and duplicates are separate rows).

## 4. Belzutifan re-opening (scope fixed now)

Round 1 (P3-03, INCONCLUSIVE) named the missing datum: HIF-2alpha (EPAS1) protein in WWOX-deficient neural cells and its causal share in LDHA/SLC2A1. I will search Europe PMC and the local datasets once for such a datum (WWOX with EPAS1/HIF-2alpha). If a measurement exists it is read and the decision is revisited; if none exists the decision stays INCONCLUSIVE with the same missing datum; no further belzutifan work is done. It is not counted among the six.

## 5. Decision rules for the qualification (fixed now)

* **Identity** VERIFIED only if the ChEMBL standard InChIKey equals the PubChem record found by InChIKey and the PubChem record found by name carries the same key (or the same 14-character skeleton block, difference stated). Otherwise UNVERIFIED. PX-478: the structure is compared with the nitrogen-mustard N-oxide formula (ChEMBL types it "Protein", which is a typing anomaly to be resolved by SMILES, not by name).
* **Measures** are kept per target, assay type, species, standard type, relation and units; no pooling across types or units; ratios only inside one document, one standard type, relation "=".
* **Edge provenance (this round's addition).** For the decisive edge(s) of each candidate I open the primary paper behind the OmniPath/SIGNOR/CollecTRI reference at the deepest depth available (PMC or Europe PMC full text if open, otherwise abstract, and the depth is written). Four questions per edge: (Q-a) does the record describe regulation of the SEED GENE (not a different quantity) in a cell relevant to the seed (neural, progenitor, or at least non-cancer); (Q-b) does the sign match the network sign and the seed level (transcript against protein); (Q-c) is the compound's action on its target reported, in a system, to change that readout; (Q-d) is the target expressed in the relevant cells (and exposure). Answers are YES / NO / PARTLY / NOT_REPORTED, never inferred. An edge is a **context-free artefact** if its only support is a cancer-line or in vitro record and its sign refers to a quantity other than the seed level; it is **plausible in neural cells** only if a reference measures it in neural or neural-progenitor cells.
* **Seed caveats carried**: Q2 rows: IT7_READOUT6 guard (the six genes SLC2A1, HK2, LDHA, LDHB, BNIP3, PDK1 were the IT7 held-out readout; generation was legitimate, but no candidate is evaluated by reversal of that readout) and the opposite HIF1A -> PDK1 valence across systems (PDK1 direction is uncertain). Q6 rows: the MYC seed is WEAK-DIRECTION-ONLY (valence unknown; both opposes and mimics arms stay conditional).
* **Decisions**: DROP only with a named decisive datum; KEEP-AS-PROPOSAL only with experiment, readout, control and falsifier; REFERENCE-ONLY; INCONCLUSIVE names the exact missing datum. "Insufficient support" is distinguished from "no activity". A `mechanism_probe` cannot be KEEP-AS-PROPOSAL as a treatment; it can be KEEP-AS-PROPOSAL as a mechanistic experiment in a WWOX-deficient system if the edge and expression questions are not negative.
* **Trials**: ClinicalTrials.gov API v2, query strings and counts logged with date; a zero is "no hits for the query string on that date".
* **Receipts**: staged only for papers read at full-text depth (the full text of the paper, not selected passages).

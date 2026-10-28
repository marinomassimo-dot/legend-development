# Independent verification of the it3 coverage layer (actor scientist-c)

Subject: `repurposing_search.py`, `repurposing_coverage.py`, `compound_catalog.py`, `catalog/`, `coverage/`, `needs/needs.json`, `coverage/target_roles.tsv` on main 5ce8bb87.
Method: `2026-10-28_it3_coverage_independent_verification.py` (same folder) reads `catalog.jsonl.gz`, `needs.json`, `coverage_summary.json`, `priorities.json`, `coverage_matrix.json`, `associations.jsonl.gz` and the cards directly. It imports no producer module. Nothing outside this folder was edited. Not medical advice; a verification of counts and labels only.

## Verdict in one table

| # | Item | Verdict |
|---|---|---|
| 1 | Per-need record and family counts | REPRODUCED exactly (all 22 needs, record counts; families within 1 on two needs). But the headline numbers rest on link-types that include `pathway_member` and `effector_constraint`; see 1b |
| 2 | Identity guards | PASS for the guard mechanism; one residual upstream-conflation risk (PDK1 rows from PharmGKB/TdgClinicalTrial) |
| 3 | Direction logic | PASS on mechanics (0 favourable or opposed labels for any `uncertain` need); FAIL on content for ABAT (source artefact), and role rows overstate AMPAR and partial-block |
| 4 | L3/L4 | OVER-CLAIMS in 6 of 10 L4 cells and in 4 of 5 L3 cells reviewed |
| 5 | 4.0% / 7.2% / 1,740 | Arithmetic CORRECT; 1,740 includes 1 placeholder pseudo-compound; denominators honestly labelled |
| 6 | Access categories | RECONCILES to 44,211; "unknown/unverified" is not shown as negative |
| 7 | Failed/truncated/untried | Mostly represented distinctly; three gaps (below) |

## 1. Recomputation (script part 1)

Rule used: link-type = `intervention_target`, `pathway_member`, `effector_constraint`, `disease_gene_product`; excluded: `readout_marker`, `identity_guard`. Match: ChEMBL mechanism rows with organism Homo sapiens by `gene_symbols`; DGIdb rows by `gene` (HGNC symbol). Family key = ChEMBL `relations.parent`, source-only records are singletons.

| Need | mine records / families | reported records / families |
|---|---|---|
| GSK3B-DEREPRESSION | 498 / 498 | 498 / 498 |
| ISR-ATTENUATION | 36 / 36 | 36 / 36 |
| LACTATE-LDH | 6 / 6 | 6 / 6 |
| NEUROINFLAMMATION-GLIA | 415 / 405 | 415 / 405 |
| REDOX-OXIDATIVE-STRESS | 4 / 4 | 4 / 4 |
| EXCITATORY-GAIN-GLUTAMATE | 209 / 204 | 209 / 203 |
| MYELINATION | 138 / 128 | 138 / 128 |
| all other needs | identical | identical |

Union: 1,770 records (identical). Union of families 1,741 (mine, parent key) versus 1,740 (producer, ChEMBL parent or InChIKey connectivity block); the one-family and total-families (40,975 vs 40,753) differences come from the producer's additional InChIKey-block merge, which I did not replicate. No unexplained difference. Readout-marker-only records: 351 (identical). Non-human ChEMBL rows carrying a link-type symbol: 0 (the producer's "0 set aside" is correct; the only non-human hits are two canine GABRB rows, a readout marker).

### 1b. What the headline counts contain (finding A, high importance)

The counts are correct for the rule used; the rule makes some headline numbers misleading.

* GSK3B 498: only 51 records hit GSK3B itself (53 with GSK3A). 445 records hit MAPT, a target tagged `effector_constraint` ("a gene whose manipulation the record argues against"), and 444 of them hit nothing else; 439 of the 445 are DGIdb rows with no action. AXIN1 adds 1. So "GSK3B 498" is 89% tau-binder or tau-listed compounds. The need's own definition does not make MAPT a place to act. Recommend counting `effector_constraint` as a listed-beside item, not a link, like the identity guard.
* Counting `intervention_target` only: union 1,101 records (2.49%) instead of 1,770 (4.0%). Per need (link-type to intervention-only): GSK3B 498 to 51, ISR 36 to 4, PDH 156 to 10, WNT 75 to 3, MITOCHONDRIAL 5 to 0, REDOX 4 to 0, MYC 71 to 0 (these are pathway-member needs; HIF1A alone supplies 146 of PDH's 156 and CTNNB1 68 of WNT's 75).
* "ISR 36": 29 are ATF4 (a `pathway_member`); the four EIF2AK3/EIF2B1 records are the intervention-target links.
* LDH 6 is clean: all six via LDHA/SLC16A1/SLC16A7 intervention targets (guard LDHC: 0 hits).
* The 4 WWOX records (sorafenib, gemcitabine and two more) are DGIdb PharmGKB rows with no interaction type; they are counted as "documented link" under five WWOX needs. Honest in `limits`, but they inflate the "needs with documented link families" (21 of 22).

## 2. Identity guards (script parts 1-2)

* Searching `target PDK1` returns only dichloroacetate (ChEMBL PDK mechanism); `target PDPK1` returns AR-12 and UCN-01. No cross-return. `need NEED-PDH-PYRUVATE-AXIS` returns no PDPK1 compound. DGIdb PDK1 rows are keyed on `hgnc:8809` (PDK1, correct) and PDPK1 on its own id.
* Residual: two compounds, Osu-03012 (= AR-12) and celecoxib, carry DGIdb `PDK1` (hgnc:8809) rows from TdgClinicalTrial/PharmGKB while also carrying PDPK1 rows. Both are known PDPK1 inhibitors; the `PDK1` rows are very probably the upstream alias confusion the guard note describes, and they enter the PDH need as links (8 PDK1 records in total, 2 suspect). I could not verify the upstream claims, so this is a risk, not a proven error. Suggest listing them as "PDK1 alias suspect".
* Identity-guard targets (LDHC, TCF4, COXFA4): never counted as links in my recount, reproduced. `COXFA4` has 3 hits (metformin, NV-128, ME-344) listed beside, not counted. Readout markers: 351 records touch only readout markers, not counted, reproduced.

## 3. Direction logic

* Mechanics: of 2,601 associations on `uncertain` needs, 2,601 are `direction_unresolved`; 0 priority records on `uncertain` needs carry `consistent_mechanism_candidate` or `opposite_mechanism`. For restore/up needs: 497 associations, all `not_evaluable` or `direction_unresolved`. PASS.
* Counts that mix needs: `consistent_mechanism_candidate` 201 are (family, need) cells: 96 glutamate + 70 seizure + 35 T-type; the distinct families are 179 (CACNA1G blockers count in both seizure and T-type). Label the 201 as cells in the summary and add the 179.

Traces (consistent):
1. Bepridil (CHEMBL1008), SEIZURE-CONTROL: ChEMBL mechanism "Voltage-gated calcium channel blocker", BLOCKER on CACNA1G; role row CACNA1G in seizure need = `same`, down; need direction `down`. Mechanically justified. Content caveat: the seizure role basis is itself "a symptom-level inference"; bepridil is a non-selective calcium channel blocker with arrhythmia liability; "consistent mechanism candidate" is a catalogue statement, not support.
2. Memantine (CHEMBL1699), GLUTAMATE: NEGATIVE ALLOSTERIC MODULATOR (ChEMBL) / "negative modulator" (DGIdb) on GRIN1/2A/2B; role `same`; need `down`. Label formally justified, but the need's own text says only full competitive block (d-APV) abolished bursting, partial or use-dependent block is untested, and a card assertion (DR-W2-004) shows memantine accelerating seizure stages in an adult rat model. The cell shows L3 `observed` with no sign (see 4). Label stands as a mechanical statement and must not be read as support.
3. Vigabatrin (CHEMBL89598), SEIZURE-CONTROL: ChEMBL INHIBITOR on ABAT; role `same`; need `down`. Justified and the best-supported cell in the layer (human clinical reports, L3/L4).
   Not justified: 46 of the 70 seizure-need consistent cells (Dpcpx, istradefylline, theophylline, caffeine, preladenant, rolofylline ...) rest only on DGIdb Guide-to-Pharmacology `ABAT` "inhibitor" rows. See finding B.

Traces (opposed):
1. Adenosine, Regadenoson, CCPA, Hemado, (S)-PIA at ABAT "agonist" (the 4 `opposite_mechanism` priorities include Adenosine and Regadenoson for seizure): not justified. Finding B.
2. Aspartic acid and glycine at GRIN2A/2B "agonist" (the other 2 `opposite_mechanism` priorities): mechanically true (co-agonists raise NMDAR activity) but endogenous amino acids, not candidates; the label is correct, the usefulness is nil. 126 associations are `opposed`, 63 cells; only 4 become `opposite_mechanism` because a consistent action in the same family overrides, as documented.

### Finding B (high importance): ABAT rows are a Guide-to-Pharmacology expansion artefact

Within the catalogue, DGIdb GuideToPharmacology rows for adenosine-receptor ligands carry the gene list ABAT, ABCA1, ABCA2, ABCA3 (alphabetical-prefix pattern), e.g. adenosine, istradefylline, caffeine, theophylline, preladenant. 77 of the 89 ABAT-linked records have ABAT only from this source (46 "inhibitors" = adenosine antagonists, 30 "agonists" = adenosine agonists). The 12 genuine ones: vigabatrin (x2), CPP-115, valproate (x3), tiagabine, pyridoxal phosphate and a few metabolites. Consequences: INHIBITORY-HYPOFUNCTION "89" should be about 12; SEIZURE-CONTROL's 70 consistent cells include 46 artefacts (adenosine antagonists such as caffeine and theophylline are pro-convulsant in general pharmacology, so the label is the reverse of its meaning); 2 of the 4 `opposite_mechanism` records are artefacts. Union of links without these 77: 1,693 records. Correction: exclude or flag rows whose DGIdb source is GuideToPharmacology and whose gene list is an A-prefixed run (ABAT/ABCA1-3/FTH1P4 beside ADORA*), or require a second source for ABAT. The other GtoP-sourced links were not exhaustively audited; ABCA1-3 are in no need, so no other need is affected by these particular symbols.

### target_roles.tsv (17 rows) against the needs rationale

* 5 WWOX rows (GENE-ADDITION, SPLICE, PTC, MISSENSE, ENDOGENOUS-BOOST; WWOX same): sound, restores or raises WWOX = up. Note PTC-READTHROUGH and SPLICE do not act on the WWOX gene product as a target of a compound; the rows will only ever match "WWOX activators", of which the catalogue has none (4 unstated PharmGKB rows). Harmless.
* 3 T-type rows (CACNA1G/H/I same): need certainty is `inferred` (one ethosuximide experiment, no drug-by-genotype test, lithium also acted in wild type). Basis text says "the need's own quantity is this target's activity", true for CACNA1G by definition; for CACNA1H and CACNA1I the need names the three isoforms without any isoform-level data. Presented as `same` with the need's certainty not carried to the label.
* 7 glutamate rows (GRIN1, GRIN2A, GRIN2B, GRIA1-4 same): the need's `on` field says "NMDAR, possibly AMPAR". GRIA1-4 coupling is a guess from "possibly"; the whole AMPAR half (perampanel and 42 to 52 records per subunit) rests on no WWOX datum (the d-APV result is NMDAR-only, as the card itself notes). Also GRIN2A/2B are given the same coupling although the evidence is a non-subunit-selective competitive block, and GRIN variant data (14/19 GoF vs 3/15 LoF responders) show the sign depends on the variant. Concrete correction: demote GRIA1-4 to unresolved (or add a basis marker "inferred, not measured"), and write "full competitive block only" into the basis of the GRIN rows.
* 2 seizure rows (CACNA1G, ABAT): the basis text correctly says "symptom-level inference, not a WWOX result". This is the one place where the role file is honest, but the downstream label (`consistent_mechanism_candidate`, 70 cells) drops that qualifier. The coverage README should say that the seizure cells are symptom-level and not mechanism-linked to WWOX (need INFERRED item 1).

## 4. L3 and L4

Definition check: L4 = a WWOX-system assertion with bridge comparison OPPOSES_DISEASE_CHANGE, "card pertinence is card-level". The producer states "technical comparison, not efficacy". Still, the label "observed recovery in a WWOX system" is stronger than several cells deserve.

All 10 L4 cells:

| Cell | Evidence | Judgement |
|---|---|---|
| INT:C01_aav9_wwox x GENE-ADDITION | spike-wave discharges per hour, high dose, knockout vs wild type vs treated (n 5), full text | Genuine. Keep |
| INT:C04_aav9 x GENE-ADDITION | 7 assertions: survival, body weight, motor score, GFAP at high and low dose, Wwox-null mouse, full text | Genuine for high dose. Low-dose arms (LD survival falls to 0% by about day 77 per the need's own observation O1) are counted as "opposes disease change": over-claim at low dose; split the dose arms |
| INT:C04_aav9 x SYSTEMIC-GLYCAEMIA-GROWTH | same 7 assertions | Over-claim: only body weight is growth; survival, motor and GFAP are not glycaemia. Card-level pertinence is carrying an endpoint-level claim. The need has no intervention target at all |
| FAM LITHIUM x GSK3B-DEREPRESSION | lithium pretreatment lowers seizure stage in Wwox-null pups | Over-claim: the same card holds DR-LI-002 showing lithium also lowers seizure stage in wild-type littermates (a drug effect in a seizing animal, as the T-type need's counter-evidence states); the endpoint is seizure stage, not GSK3B derepression; lithium has non-GSK3 actions. A technical bridge at best |
| FAM VIGABATRIN x SEIZURE-CONTROL | spasm cessation, 2 reports (Shaukat child 1, Nagarajan), reading depth `queried_not_full_read`, 2 case reports, concomitant drugs in the second child | Marginal: observed clinical report, but depth is not a full read and there is no comparator. "Recovery" overstated; say "reported cessation, case level" |
| FAM VIGABATRIN x INHIBITORY-HYPOFUNCTION | same assertions | Over-claim: spasm cessation is not a measurement of inhibitory hypofunction; need direction `uncertain` |
| INT:EB-KD-01 (ketogenic diet) x SEIZURE-CONTROL | clinician-reported seizure control in 3 named patients, no instrument, partial read, two of the three had died | Marginal as above |
| INT:EB-KD-01 x PDH-PYRUVATE-AXIS | same | Over-claim: seizure control on a diet does not measure the PDH axis |
| INT:D01_a51 x MYC-PROGENITOR | fraction of SOX2+MYC+ progenitors in organoid sections falls, `reading_depth` UNKNOWN | Marginal: WWOX-deficient organoid, but a multi-kinase inhibitor, reading depth UNKNOWN is labelled DATO; for the MYC need SOX2 is a readout marker |
| INT:D01_a51 x WNT-BETA-CATENIN | same | Over-claim: the endpoint is not a Wnt readout |

Summary: 2 genuine (the AAV cells for gene addition at high dose), 2 marginal, 6 over-claimed through card-level pertinence or non-specific effects. Correction: require the assertion endpoint to be listed against the need (an `endpoint_pertinent_to_need` flag), and rename L4 in the summary to "WWOX-system assertion judged opposing disease change by the bridge".

Five L3 cells reviewed:

* AMLEXANOX x WWOX-PTC-READTHROUGH: DR-B01-001, TP53/DMD/CFTR nonsense alleles in lung-cancer, DMD and CF lines, partial read. A different-gene precedent; `observed` is accurate only as "other-disease precedent". The scope is carried, so it is not wrong, but the state word `observed` reads strongly.
* STIRIPENTOL x LACTATE-LDH and x MITOCHONDRIAL-RESPIRATION: 7 assertions, of which DR-E02-001 and -003 are cell-free enzyme assays and a nedosiran (oligonucleotide) hyperoxaluria datum, 'queried_not_full_read'; only DR-E02-GEN-001 (Drosophila Abeta42 plus Wwox RNAi, full read) is a real readout, and it is classed other_disease_precedent. The same 7 assertions fill the mitochondrial-respiration cell, whose pertinence is card-level only. Over-claim: target engagement counted as an observed effect on the need.
* SODIUM DICHLOROACETATE x PDH-PYRUVATE-AXIS: DR-E03-001 and -002 are enzyme assays (rat enzyme, fibroblast, recombinant human) and a lactic-acidosis indication; target engagement, not a readout in a WWOX-relevant system.
* PERAMPANEL and MEMANTINE x EXCITATORY-GAIN (5 assertions each, 1 `wwox_experimental`): the wwox_experimental assertion is DR-W2-001, the d-APV experiment (tool compound), attached to memantine and perampanel by `chembl_id_mentioned_in_card_text`, which the card_links rule itself calls "a mention, not an identity declaration". Neither drug was given to a WWOX system (the need says so). Moreover the pooled cell contains DR-W2-004 (memantine accelerates oxygen-induced seizure stages in adult rats), so the cell reads `observed` with benefit and harm pooled, no sign. This is the clearest L3 over-claim.
* INT:E01_isr_modulators x ISR-ATTENUATION: 3 assertions, all abstract-only, ALS, 5xFAD, vanishing white matter; accurately labelled other_disease_precedent, but `abstract_only` reads are counted as observations.

L3 correction: carry sign (benefit, harm, null) per cell; separate target-engagement (cell-free, enzyme) assertions from readout assertions; do not attach a tool-compound result to a named drug when the attachment rule is "mentioned"; 20 L3 cells include 3 cells with such mention-only attachment (glutamate x2, lithium Q-R-04).

## 5. Percentages and denominators

* 1,770 / 44,211 = 4.003% (4.0): correct. 1,770 / 24,423 = 7.248% (7.2): correct. Labelled with numerator, denominator and what is counted; the second denominator (records with any target row) includes 588 records whose rows carry no gene or target identifier (e.g. "Reactive metabolite scavenging agent"), so it is slightly generous.
* Families 1,740: the distribution 1,446+263+21+5+2+1+1+1 = 1,740 reconciles. The one family touching 17 needs is the DGIdb placeholder "Null" (drug name literally NULL, 10,572 target rows, flagged `name_is_source_artifact`, correctly given no priority record) and is counted inside 1,740 and 1,770. True real-compound union: 1,739 / 1,769 (the percentage is unchanged to one decimal). The next widest is sorafenib (8 needs).
* Overlap: no summed per-need figure is presented as a total (my sum of per-need family counts would be 2,097, which equals the matrix row count and is not shown as a total anywhere). The overlap warning is in the summary. The one exposure is the 201 above (cells, 179 distinct families).
* Denominators are all-record denominators (includes antibiotics, vaccines, supplements); the 4.0% is "records linked to a need" not "fraction of relevant compounds"; the README says no relevance is implied. Fine.
* Sensitivity, not an error: intervention-target-only 1,101 records (2.5%); without the ABAT artefact 1,693 (3.8%); also without MAPT-only GSK3B records 1,249 (2.8%).

## 6. Access categories

Signature sums: 28,296 + 13,014 + 1,893 + 705 + 177 + 82 + 18 + 13 + 7 + 6 = 44,211. Reconciles to the total. The overlapping per-category counts (13,021 experimental, 2,101 prescription, 906 OTC, 126 supplement, 28,296 unknown) sum to 44,450, i.e. 239 records carry 2 or 3 categories; the stats file labels them overlapping and my recount matches. "unknown/unverified" is its own category (28,296, 64%) with the statement that accessibility says nothing about approval or safety; no place in the outputs I read turns it into "not available". `experimental` is scoped as "says nothing about whether anyone can obtain it". PASS.

## 7. Failed, truncated, untried versus empty

Represented distinctly: `incomplete_or_failed_query` (priority), `source_incomplete` (L1), `source_queried_without_result`, `L1_none_found` (430) versus `L1_not_evaluable` (17), `L3_none_in_cards` (2,523, with the note "not a negative"), `inputs_status` (missing cards, sources not OK, stale role rows all empty), and a unit test with `src_state=FAILED`. Gaps:

1. Only `chembl` and `dgidb` states feed `src_problem`; a failed unichem, openFDA NDC, DSLD or MATRIX source would not mark anything incomplete and its absence shows as the ordinary `unknown/unverified` access category.
2. "Stale" is a free-text note, not a state: DGIdb is the 2024-06-10 export (claims from ChEMBL 33, 22 sources differ from the live service) with `state: OK`, so no disposition becomes incomplete, and "none_found" (430) and `not_relevant` (245) hold for a stale source. `not_relevant` for card-attached families (identity resolved, no link to the need's targets) reads as a negative; suggest `no_catalogue_link_found`.
3. No example of the failure states exists in the real outputs (all OK), so the representation is tested only on the synthetic fixture.

## Concrete corrections, ranked

1. Exclude or flag the GtoP ABAT adenosine-receptor artefact rows (77 records); recompute INHIBITORY-HYPOFUNCTION, SEIZURE and the 4 `opposite_mechanism` records.
2. Do not count `effector_constraint` (MAPT) as a link; report "GSK3B 51 (+2 GSK3A)" with the MAPT 445 listed beside.
3. Separate link counts by target kind in the summary (intervention target versus pathway member), and state union both ways.
4. Demote GRIA1-4 roles to unresolved or mark them inferred; add "full competitive block only" to the GRIN rows; label seizure cells as symptom-level.
5. L4/L3: endpoint-level pertinence flag; split dose arms; carry the sign; separate target-engagement from readout; no attachment of d-APV to memantine/perampanel.
6. Report 201 cells as 179 families; exclude the "Null" pseudo-compound from the family and record unions (1,739 / 1,769).
7. Treat `stale` as a source state; rename `not_relevant`; list the two PDK1/PDPK1 suspect compounds.

Reproduce: `python3 -I disease-models/wwox/research/drug_repurposing/locator_audits/2026-10-28_it3_coverage_independent_verification.py` (about 30 s, offline).

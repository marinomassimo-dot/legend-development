# IT24 P1 source check: panobinostat -> SIRT1-7 and idronoxil -> CASP3

Non-canonical research material; not medical advice. Zero spend, no registration, no contact with
authors, no e-mail address sent anywhere. Receipts in `receipts/` are prepared for the integrator
(`fulltext_receipts.py record --dry-run`); the ledger was not written here.

## 1. Verdicts (full table: `verdicts.tsv`)

| Relation (LEGEND sign) | Outcome | What the sources support |
|---|---|---|
| Panobinostat -> SIRT1, SIRT2, SIRT3, SIRT7 (-1); also SIRT4/5/6 | EXCLUDE_FROM_SIGNED_PROPAGATION (truth UNKNOWN) | No sirtuin measurement for panobinostat was found or read. The only origin is one DGIdb listing (TALC). EC-KG +1 is prediction-only and equally unsupported, so no flip. |
| Idronoxil -> CASP3 (-1) | EXCLUDE_FROM_SIGNED_PROPAGATION | Papers report caspase-3 *activation* as a downstream consequence (after XIAP loss). That is neither an inhibitor nor an agonist of CASP3; no binding or enzyme assay exists in what was read. |
| Idronoxil -> XIAP (-1), CFLAR (-1) (same source, extra) | INDIRECT_QUALIFIED | Protein level of XIAP / FLIP lowered in cells (degradation, Akt route). Not a direct inhibitor. XIAP -1 drives proposal IT21P2-0034. |
| Panobinostat -> HDAC1-4, 6-9 (contrast) | CONFIRMED (abstract-level) | Potent pan-HDAC inhibition on recombinant isoforms. HDAC5/10/11: UNKNOWN here. |

## 2. Identity and origin of the annotation

- Compound: DGIdb-only records `CAT:DGIDB:be0d8ea27925` (PANOBINOSTAT, 15 claims, 14 claim sources)
  and `CAT:DGIDB:b34c953dc1fa` (IDRONOXIL, 7 claims; synonym PHENOXODIOL; NCIt C2642). No ChEMBL id
  on either DGIdb record; the ChEMBL records exist separately (CAT:CHEMBL483254, CAT:CHEMBL3545368,
  CAT:CHEMBL1957038) and do not carry the claims below.
- **TALC** = Simon and Somaiah, "A tabulated summary of targeted and biologic therapies for
  non-small-cell lung cancer", Clin Lung Cancer 2013 (PMID 24377743; matched by the pii in
  `sharing_it9_20261030/evidence/dgidb_source_licences_20261030.tsv`, "Data extracted from tables in
  Elsevier copyright publication"). Abstract: over 320 agents "in practice and in clinical trials"
  listed with a clinicaltrials.gov link. It is a trial-pipeline reference table, not pharmacology.
  Its table row was not seen (paywalled). Receipt FTR-20261104-24377743-01 (abstract_only).
- **ClearityFoundationClinicalTrial**: Clearity Foundation (ovarian-cancer patient advocacy) trial
  listing; the same licence TSV: "Unknown; data is no longer publicly available from site". DGIdb
  documentation page could not be rendered by WebFetch, so curator wording beyond the licence TSV
  and `licence_inventory_it7_20261029.md` (class C, 240 rows) was not obtained.
- Intermediaries: publisher table or advocacy listing -> DGIdb (export 2024-06-10) -> catalog
  `interaction_type: inhibitor` -> `family_actions.tsv.gz` sign -1 (group `DGIdb_other`,
  scope `unspecified`, n_rows 1).

## 3. Evidence reading (depth is real, see receipts)

| Paper | Depth | Decisive statement (verbatim, anchor) |
|---|---|---|
| Colorectal, PMID 32665777 (PMC7355152) | partial full text (Intro, Methods, Results, Discussion by hit + context; figures not seen) | Results Fig 3A: "Statistically significant increase in the amount of the cleaved caspase-3 protein was detected ... Pxd pre-treatment followed by 5-Fu and/or 1-OHP in both CRC cells". Discussion: "The presence of active caspase-3 ... is indicative of induction of caspase-mediated apoptosis". Intro: apoptosis "via degradation of X-linked inhibitor of apoptosis protein (XIAP)". Note: ELISA methods say MCF-7 in an HCT-116 study. |
| Melanoma, Kluger 2007, PMID 17257402 (PMC1796544) | partial full text | Results Fig 8: "remarkable XIAP degradation was observed ... and a significant increase on the activity of caspase-3/7". Discussion: "decreased levels of XIAP, sensitization to Carboplatin, and remarkable activation of caspase-3". Intro: XIAP "inhibits the execution phase by inhibiting the effector caspases, caspase-3 and caspase-7". |
| Kamsteeg 2003, PMID 12730675 | abstract only (paywalled) | "dependent upon the activation of the caspase system, inhibiting XIAP ... and disrupting ... (FLIP) expression through the Akt signal transduction pathway". Caspase-3 not named. |
| Herst 2007, PMID 17904534 | abstract only | "its primary molecular target is unknown"; PMET inhibition with "pan-caspase activation". |
| Khan 2008, PMID 17868033 | abstract only (paywalled) | "(trichostatin A, NVP-LAQ824, panobinostat, ITF2357, vorinostat and belinostat) were potent pan-HDAC inhibitors"; eight zinc isoforms only. |
| Bradner 2010, PMID 20139990 (PMC2822059) | text read, figures/tables not served | Intro: sirtuins are "a structurally and mechanistically distinct class of NAD-dependent hydrolases"; Results: profiling "against HDAC1-9". Sirtuins not profiled; panobinostat values not seen. |
| Bantscheff 2011, PMID 21258344 | abstract only | "several non-HDAC targets for hydroxamate inhibitors"; sirtuins not mentioned. Whether panobinostat captures sirtuins is open. |

Not read: Khan 2008 and Bantscheff 2011 full text, Kamsteeg full text, Simon 2013 table, the
Clearity listing, Alvero 2006 and other phenoxodiol papers. A positive panobinostat-sirtuin
datum, if one exists, would most likely sit in Bantscheff or a vendor/ChEMBL profile: that is the
single open lead. Absence of evidence here is not evidence of absence.

## 4. Direct versus downstream, and limits

- CASP3: the literature supports "phenoxodiol -> XIAP down -> caspase-3 active" in melanoma,
  colorectal and (abstract) ovarian cells, with a second drug in two of the three designs. Cells,
  doses (10 ug/ml) and co-treatment are a context; none is a CASP3 binding or enzyme assay.
  "Inhibitor" in the Clearity row is the opposite of the activation readout; reading it as
  agonism would be a second error.
- XIAP/FLIP: "inhibitor" there means lowered abundance, with the primary molecular target of
  phenoxodiol itself stated as unknown (Herst) or ENOX2 (Colorectal intro, citing others).
- SIRT: panobinostat is a hydroxamate zinc chelator; the served Bradner text calls the sirtuins an
  NAD-dependent class apart. That is a reason for caution, not a measurement.

## 5. Role in current outputs

- In the proposals_it21.tsv, candidates_Q2.tsv and seed-specific null tables of generation_it21_p2 /
  it22_p1 / it23_p2 (grep for the two family ids), neither a SIRT nor CASP3 appears as main target,
  chain edge or contributing seed; the families enter through other targets (not a full audit).
  Panobinostat (IT21P2-0033, CONDITIONAL_H_HARM) rests on HDAC5 -> SLC2A1; idronoxil
  (IT21P2-0034) on XIAP -> HIF1A -> LDHA, with `contributing_seed` shares 19% (top seed).
- Same claim through another path: no. ChEMBL families of panobinostat / lactate (FAM:CAT:CHEMBL3545368)
  carry HDAC1-11 only; the ChEMBL idronoxil/isophenoxodiol families have no CASP3 or SIRT row; the
  DGIdb "Panobinostat Lactate" record lists HDAC1-11 only. Of all TALC compounds, only panobinostat
  has SIRT rows (vorinostat, belinostat, givinostat, etc. list HDACs only). CASP3 appears under
  Clearity only for idronoxil.

## 6. Where the engine should change (proposal, not applied)

Smallest common point: the sign-withholding wrapper `make_wrapper` / `row_usability` in
`generation_it21_p2_20261103/refresh_actions_it21.py`, which already withholds DGIdb rows by a
provenance class (`republished_claim_level_not_carried`: 9,624 rows; `group_record...`: 1,585).
Add one class there: a source-tier rule on `claim_source`. Signed direction counts only from
sources that report measured pharmacology (GuideToPharmacology, DTC, ChEMBL, DrugBank-type);
for review-table, trial-listing and advocacy sources (TALC, Clearity, MyCancerGenome and its
trial list, CancerCommons) the sign is set to `unresolved` unless a second, independent source
agrees on the same (compound, gene). That fixes the whole class in one place and leaves the
record. Also worth a flag: a row whose target is a pathway effector (XIAP, CFLAR, CASP3) should
carry "abundance/activity readout", not "target action".

## 7. Second case of the same defect (counted, not fixed)

Table `generation_it21_p2_20261103/results/actions/family_actions.tsv.gz` (19,920 rows). Rows of
group `DGIdb_other` with a signed direction whose (family, gene) is supported by exactly one claim
source, joined to the catalog (script logic: this README's session; counted 2026-11-04):

| claim_source | single-source signed rows | families |
|---|---|---|
| MyCancerGenome | 141 | 25 |
| MyCancerGenomeClinicalTrial | 63 | 23 |
| TALC | 68 | 32 |
| ClearityFoundationClinicalTrial | 39 | 21 |
| CancerCommons | 5 | 5 |
| (DTC, measured binding, different tier) | 90 | 3 |

Aggregator/listing tier total: 316 rows (excluding DTC). A pertinent second instance in the same
source: Clearity lists **CFLAR (FLIP) as -1 "inhibitor" for Dovitinib and Nintedanib esylate**,
both signed -1 in the table; they are kinase inhibitors and the FLIP link has no primary source
read (pattern match only, not verified). Another counted row not verified: panobinostat HDAC5/10/11.
Counts use the catalog's `claim_source` per target; the action table itself has no such column.

## Engine consequence (integrator, same day)

- Correction at the one common point, `generation_it21_p2_20261103/refresh_actions_it21.py`: a listing-tier claim source (TALC, ClearityFoundationClinicalTrial, MyCancerGenome, MyCancerGenomeClinicalTrial, CancerCommons) cannot carry a direction by itself for the pairs this source check named (`source_exclusions_it24.tsv`: panobinostat SIRT1 to SIRT7 on the DGIdb-only record, idronoxil CASP3). Association kept; unknown is not negative; no opposite sign was assigned.
- Action table rebuilt (7 s): 19,920 -> 19,912 signed pairs, 8 lost, no family lost. `--listing-tier off` reproduces the committed table exactly (control).
- The wider rule over the whole listing tier (`--listing-tier tier`, sensitivity only) withholds 648 rows / 554 pairs and would touch 28 proposals including one hand-over (sorafenib, ZHX2). It is NOT adopted: the evidence read here reaches only the named pairs, and the 316 other single-listing rows were not read. Open question with a reopening condition: read primary sources for the rows that drive a proposal (first: sorafenib/regorafenib ZHX2, AKT1/PIK3C3 rows of Q6).
- Effect on generation, bounded not re-run: none of the eight pairs is a main target or chain edge of any proposal (panobinostat enters through HDAC5, idronoxil through XIAP). The pairs carried 1.9 percent (panobinostat) and 2.4 percent (idronoxil) of the gross contribution mass of those families in Q2 (larger shares in Q3/Q5/Q6/Q7 where the families' total mass is below 0.01). The engine nulls were not re-run, so the z values of IT21P2-0033 and IT21P2-0034 are unchanged in the tables and could move slightly; their main-target chains do not depend on the withheld pairs.
- Idronoxil XIAP and CFLAR stay signed (-1) but are INDIRECT_QUALIFIED: an abundance readout, not a direct inhibition. Panobinostat HDAC5 stays for the ChEMBL families; for the DGIdb-only record it is UNKNOWN here and needs its own check (IT21P2-0033 is Q2 H_HARM and not handed over).
- Receipts: 8 recorded (1,035 chained). Real depth: two partial full texts, one text without tables, five abstract-only.

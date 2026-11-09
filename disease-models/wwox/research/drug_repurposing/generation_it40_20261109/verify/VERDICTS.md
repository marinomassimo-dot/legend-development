# IT40 independent verification: VERDICTS

Verifier dispatched as model sonnet, effort high. No agents started. Wrote only in `verify/`. Not medical advice. Reference genotype class only.
Paths are relative to `disease-models/wwox/research/drug_repurposing/` (DR). "CP" = `generation_it40_20261109/conditional_proposals_it40.tsv`. Re-derivations were run read-only against `catalog/catalog.jsonl.gz` through `framework/scripts/compound_catalog.py`, and against the package tables. External checks: ChEMBL REST (CHEMBL305187 has 0 mechanism rows; CHEMBL305195 canonical SMILES is the Ro 25-6981 structure). GtoPdb returned 401, so ligand ids 4168 and 4210 could not be checked there.

Method note. I compared every CP cell with its source cell by exact string equality (script not saved). Result: for all six rows, `status`, `starting_observation_and_chain`, `context`, `premise_and_action`, `compound_or_probe_named_by_package`, `decision_measure` and `source_and_limits` (= counter_evidence + " || weakening: " + weakening_result) are byte-identical to `hypotheses.tsv`. The cells that differ are the ones the generator rebuilds: `competing_explanations` (BH2, MH1, MH2, MH3), `expected_result_by_explanation`, `experiments`, `catalogue_by_action`, `unresolved_refs`.

---

## Q1. Gene arcs and directions: PARTLY (no invented gene-gene link or effect sign in the verbatim cells; the added catalogue cell and its symbol sets are not in the source)

Supported part:
- No row asserts a gene-gene edge. The verbatim cells equal the source, so no sign or direction is added there. `consume_it40_20261109/RECONCILIATION.md` also states that no `bridges.tsv` or `probe_links.tsv` row was written.

Not supported part (additions that are not in any source row):
1. `catalogue_by_action` is the only cell with new content. It attaches gene-symbol sets chosen by the generator (`mechsearch_it40_20261109/mechanism_search.py`, RELATIONS) and a direction label from the catalogue ("reduce activity" / "raise it or have no direction").
   - R6 (CP-BH3) uses GJD2, GJA1, GJB1, PANX1. The BH3 source names Cx36 (GJD2) and Pannexin-1 (PANX1). GJA1 (Cx43) appears nowhere in the ampa_nmda package (0 hits in all its tables). GJB1 (Cx32) appears only as a Cx32E143 hemichannel that brilliant blue FCF did NOT block (`hypotheses.tsv` BH3, compound cell). Using it as a "target symbol" for a connexin block relation inverts its role in the source.
   - R5 (CP-MH1) is "Kv7 opening", but the summary counts "28 reduce activity" first. The package says premise "None proposed", nomination ABSTAIN. A 36-row catalogue block attached to a row whose premise is "no pharmacological action proposed" reads as a pharmacological landing zone. The column is labelled by relation, but the row's own premise forbids it.
2. "raise it or have no direction" is false for R1-R5: `by_action.tsv` has only `down` (128) and `up` (38) in those relations. The only blank direction is the R6 placeholder (see Q4).

Correction: (a) drop GJA1 and GJB1 from R6 or label them "generator-added, not in source"; (b) for CP-MH1/MH3 replace the cell with "no pharmacological action proposed in the source; catalogue not searched for this row" (MH1's R5 block is outside its premise); (c) replace "raise it or have no direction" with "raise it (up)"; (d) state the desired direction of each relation next to the count (R1-R4, R6 want down, R5 wants up).

---

## Q2. Lost conditions and counter-evidence: PARTLY (the counter_evidence, weakening_result and status cells are intact; competing explanations, arm-level non-separation notes and the `INFERENZA` label are lost or truncated; applied texts drop several qualifiers)

### Proposal rows versus `hypotheses.tsv`
Intact: counter_evidence, weakening_result, status (identical). What is lost:

1. `competing_explanations` is rebuilt only from alt ids that the hypothesis text cites as tokens (`hypothesis_package.record_for`). It silently drops the plain-language rivals in the source `competing_explanation` cell:
   - CP-BH2 keeps AB04 and AB05. Source: "GluN2A-containing receptors carry the burst (H3); AMPAR-led drive (BH1); recording-state dependence (M14)". Lost: GluN2A rival (AB03), AMPAR-led rival (AB01), recording state. The GluN2A rival is exactly the one the TCN-201 arm tests.
   - CP-MH1 keeps A10, A05, A04, A06. Source: "MH2 (an HCN contribution that remains after matching)". Lost: MH2.
   - CP-MH2 keeps only A09. Source: "MH1 (passive and leak reading); T-type contribution to rebound (Z944 arm, hcn_20261107 X4); sodium-current off-target of ZD7288; a different HCN isoform or compartment". Lost: all four.
   - CP-MH3 keeps A04, A07. Source: "MH1 or MH2 as genuine cell-autonomous differences". Lost.
   - BH1 and BH3 fall back to the full source text and are intact.
2. `expected_result_by_explanation` truncates every matrix cell to 120 characters (`v[:120]`) mid-word. Verified losses against `ampa_nmda_discrim_20261108/output/prediction_matrix.tsv`:
   - M07/H2 (CP-BH1, 234 chars) ends "...of an NMDAR-rege". Lost: "so abolition is expected under H2 as well and only persistence under verified block is informative". This is the sentence the audit corrected (BH1 status says "H2 prediction under M07 corrected"), so the row announces a correction whose text it truncated.
   - M09/H5 (CP-BH3) drops "coupling readout unchanged", the discriminating readout between H5 and H6.
   - M05/H3 (CP-BH2) drops "NAM curve plateaus below the d-APV abolition level".
   - M05/H2 drops "or the delayed response falls more than the EPSC fraction predicts".
   - M16/H5 drops "and work against the burst fall".
   - M02/H7 drops "(the source has no such control)".
3. The matrix columns `same_prediction_note_arm_does_not_separate` and `prediction_label` are not carried at all. Examples of what an arm cannot separate: M07 "abolition does not separate H1 from H2 or H3"; M08 "a necessary but not sufficient arm...agreement or disagreement under one metric proves neither generality nor specificity"; M16 "compatible with AB06 and equally predicted by H4"; M17 "no arm separates AMPA from kainate". `prediction_label` says every cell is "INFERENZA (qualitative prediction from the hypothesis definitions; no cell is a measured result)". The CP expected-result column therefore shows H-by-H outcome lists with no label that they are predictions, not results. The `status` cell says IPOTESI, but the column itself is unlabelled.
4. `experiments` truncates `comparison_arms` at 400 characters. E1 (541 chars, in CP-MH1, MH2, MH3) is cut mid-word at "s" and loses "seal and access resistance reported per cell so that smaller cells plus a fixed seal leak (A10) can be separated from a conductance difference". This is the control that separates MH1's smaller-cell reading from A10.
5. Content carried verbatim but not flagged, with an internal source contradiction:
   - BE4 (in all three BH rows) calls radiprodil, carbenoxolone and perampanel "non-reversible agents". AB13 and M07 in the same package say perampanel recovers with tau about 3.3 s (off rate 0.58 per second) in culture, and that the radiprodil oocyte washout "does not state the slice off rate". See Q3.
   - E5 (CP-MH3) outcome reads "Differences present at all ages and in both layers: cell-autonomous and stable", while the MH3 row says "Wwox cell-autonomy is not tested by this experiment" (Cre is pan-neuronal).
6. MH1 numbers. CP-MH1 step 2 carries "predicted tau about 25.8 ms against 18.8 and 21.3, about 3.9 and 2.9 SE below" and the status says "flat tau against pure leak loss is supported". `consume_it40_20261109/RECONCILIATION.md` (A1) says the SE multiples "were not recomputed here, so they are not carried". They ARE carried in CP-MH1. My recomputation from `membrane_hypotheses_20261108/output/observations.tsv` O01-O03 (assuming "+/-" is SEM and the three inputs independent; INFERENZA): predicted HT tau = 18.55 x 143.26/102.88 = 25.8 +/- 4.6 ms against 18.79 +/- 1.77, z about 1.4; predicted KO = 25.8 +/- 3.9 against 21.25 +/- 1.53, z about 1.1. The 3.9 and 2.9 figures are reproduced only if the uncertainty of the prediction is ignored (7.04/1.77 = 3.98; 4.6/1.53 = 3.0). With propagated error the contrast is weak, so "supported" is too strong and the needs text ("Table 1 does not fit a pure leak loss") is stronger than the numbers.
7. CP-BH2 states radiprodil "no effect on GluN2A, GluN2C or GluN2D diheteromers" as plain data. `probes.tsv` of the same package says this is "a sentence that cites Supplementary Fig 1B, which was not read: carried text". The applied INV-05 text (B5) carries that limit ("rests on an unread supplementary figure"); the proposal row does not. TCN-201 "maximum inhibition 73-81 percent" is in the INV text but absent from CP-BH2.

### `[IT40]` texts versus `consumer_delta.md` (all 14 applied strings are present verbatim in the target files)
Numbers: I found no changed number. Dropped or weakened qualifiers:
- A1 (needs.json NEED-INTRINSIC-EXCITABILITY `inferred`): dropped the single-compartment assumption and the caveat that an HCN conductance in the 50-60 ms fit window could shorten the apparent tau, and "flat tau may be a protocol artefact" (both in MH1 chain step 2 and counter_evidence). Text says "Table 1 does not fit a pure leak loss" unconditionally. See item 6 for the weakened statistics.
- B3 (NEED-EXCITATORY-GAIN O8 `limits`): dropped from the delta's disagreement list the Fig 3D bar "about 0.6", the S3 latency n (6 animals in the text against 6 slices/3 animals in the caption), "Fig 1D enlarged looks more compatible with 0.84 (INFERENZA)" and the WT versus HT KS p = 1.98e-4. The applied heading still reads as the list of disagreements.
- B4 (`counter_evidence`): the delta says "the EPSC reduction recovered incompletely while the IPSC reduction was rapidly and fully reversible". The applied text keeps only "the IPSC reduction (to about 50 percent) was fully reversible". The incomplete EPSC recovery is what makes culture non-recovery compatible with the slice non-recovery, and it is the point of BH3 status. Also dropped: "P12", "or with La3+ at P20", "P0-P1 origin, 6-15 DIV", "attenuated in four of five ATP-site mutants", "higher paired-pulse ratio". "In rat CA1 slices" keeps species; carbenoxolone "alone" keeps one arm.
- B7 (card F01 packet): dropped "cultured rat hippocampal neurons" to "in culture". The potency range is rendered "submicromolar to about one micromolar" while the source IC50 range is 0.4-1.2 uM (above 1). Minor.
- A7: dropped "Rin lower at the more negative potential" for ZD7288. Minor.
- A5: adds "oral dose-response bars of its Fig 2 disagree with the text" which is not in the delta; it is supported by `membrane_hypotheses_20261108/verify/audit.md` line 297, so I do not count it as a defect.

Corrections: (1) regenerate `competing_explanations` as the union of the source `competing_explanation` text and cited alternatives; (2) remove the `[:120]`/`[:400]` slicing or mark truncation with "[...]" plus length; (3) add `same_prediction_note_arm_does_not_separate` and a single row-level label "predictions: INFERENZA, no cell is a measured result"; (4) remove the "3.9 and 2.9 SE" and "supported" wording from CP-MH1 or replace with "z about 1.1-1.4 on propagated SE (verifier recomputation, INFERENZA)"; (5) restore in A1 "under the single-compartment assumption; a hyperpolarisation-activated conductance in the fit window could also shorten tau"; (6) restore in B4 "the EPSC reduction recovered incompletely"; (7) add to CP-BH2 "selectivity sentence rests on an unread supplementary figure" and "TCN-201 maximum inhibition 73-81 percent".

---

## Q3. Transfer between molecules, paralogues or preparations: PARTLY (named preparations are mostly stated; four unflagged transfers or internal contradictions remain)

Stated and acceptable: radiprodil (oocytes, room temperature, and mouse CA1 P17-P22) and the transfer sentence in BH2 context; TCN-201 "recombinant GluN1/GluN2A"; carbenoxolone culture versus rat CA1 versus burst slices (context and counter_evidence both say "neither is slice data from this preparation"); ivabradine "rat 25-35 d", "DATO (transfer)"; perampanel "cultured rat hippocampal neurons" and "transfer from culture perampanel kinetics to the slice is unmeasured".

Unflagged or inconsistent:
1. BE4 (all three BH rows) groups perampanel with "non-reversible agents (radiprodil, carbenoxolone, perampanel)". For perampanel the same package gives recovery tau 3.3 s and "off rate 0.58 per second" (AB13, M07: "slice washout unmeasured"). For radiprodil the only washout datum is 4.7% recovery in oocytes at room temperature (AB13: "does not state the slice off rate"). The sentence transfers an oocyte datum (radiprodil) and a culture datum (carbenoxolone EPSC incomplete recovery) to slice reversibility, and contradicts perampanel's own data. Correction: "slow-reversing in oocytes (radiprodil) or culture (carbenoxolone EPSC); perampanel recovers in seconds in culture; slice reversal unmeasured for all three".
2. CP-BH3 chain step 4 (INFERENZA): "an effect on release and excitability is sufficient to explain it [the burst fall]". "Sufficient" rests on culture magnitudes (63/69 percent EPSC at room temperature in autaptic hippocampal neurons) applied to a 35 C neocortical slice, while the same row's context says "transfer to the burst preparation is unmeasured". The decision_measure correctly makes sufficiency a measured quantity, so the chain step is stronger than the row's own measurement logic. Correction: "may be sufficient (culture magnitude, transfer unmeasured)".
3. `by_action.tsv` R1 treats pore blockers and glycine-site compounds as "negative modulation of GluN2B-containing NMDAR". Of 21 reducing molecules only radiprodil, traxoprodil, rislenemdaz and EVT-101 have a GluN1/GluN2B record (see Q7). Memantine, ketamine, esketamine, amantadine, lanicemine and AV-101 act through other sites in their ChEMBL mechanism text (record: "Glutamate [NMDA] receptor negative allosteric modulator / antagonist / blocker"). Their "reduce activity" counts therefore carry class transfer from NMDAR in general to the GluN2B relation. Not flagged in the CP-BH2 summary.
4. CP-BH2 `source_and_limits`: "memantine 10 uM (text) or 30 uM (Fig 5 legend) did not inhibit the S810R EPSC". The preparation (an S810R mutant, not named) is omitted. Without it, it reads as a general memantine datum. This is verbatim from the package, so a package-level omission; flag, not a CP defect.
5. Ifenprodil/Ro 25-6981: the rows say only "activity-dependence abstracts were not read first-hand" and name no transfer. Supported. TCN-201 "only with a measured slice co-agonist level": supported. ZD7288 appears only as "tool class" with no transferred number.

Corrections: edit BE4 as in item 1; soften BH3 step 4; split R1 into "GluN2B-heteromer record" versus "NMDAR class record" in the summary.

---

## Q4. Unknown turned into negative: PARTLY (wording in `identity_check.tsv` over-states for d-APV, mis-credits for GYKI 52466, and the R6 placeholder is turned into "1 catalogue row"; ifenprodil, Ro 25-6981 and brilliant blue FCF are correct but need a caveat)

I re-derived five verdicts from the catalogue (44,211 entries) by name, synonym and alias.

| Tool | Producer verdict | My derivation | Judgement |
|---|---|---|---|
| d-APV | NOT_IN_CATALOGUE | Record `CAT:DGIDB:b0ca5cf2303c`, name "D-Ap5", dgidb_drug_name "D-AP5", IUPHAR ligand 4168, targets GRIN2A, GRIN2B, GRIN2C, GRIN2D (all `inhibitor`, GuideToPharmacology). D-AP5 and d-APV are the same compound (D-2-amino-5-phosphonopentanoate/valerate; standard synonym; the GtoPdb ligand could not be fetched, 401). The producer's name search used "d-APV", which does not match "D-Ap5". | Verdict NOT SUPPORTED: an unknown (name did not match) was written as a negative. GRIN1 is not listed (it is the glycine-site subunit); intended-target set GRIN1/2A/2B is therefore "GRIN2A, GRIN2B found; GRIN1 absent from the record". |
| brilliant blue FCF | NOT_IN_CATALOGUE | No entry for "brilliant blue FCF", "FD&C Blue 1", "Acid Blue 9", "E133", "Blue No 1", "FCF" (only 2 unrelated hits for "fcf"). Present: BRILLIANT BLUE G (CHEMBL4173394; DGIdb record with P2RX7) and Isosulfan blue ("Acid blue 1"), which are different compounds. | SUPPORTED as "no entry matched under the names searched". Should be worded that way, and should say Brilliant Blue G is present and is not the same compound. |
| ifenprodil | RECORD_WITHOUT_THE_INTENDED_TARGET | CHEMBL305187 and CHEMBL1886888 have 0 target rows. ChEMBL REST returns 0 mechanism records for CHEMBL305187. DGIdb records: "Ifenprodil" (MTOR, DRD1), "(R,S)-Ifenprodil" (CYP1A2, CYP2D6, ...). No GRIN2B anywhere. | Literal verdict SUPPORTED, wording over-reads. It is a catalogue curation gap (no mechanism row for ifenprodil), not evidence about ifenprodil pharmacology. The two DGIdb records were not both resolved by `dgidb_named_tools.tsv`. Suggest "NO_TARGET_ROW_IN_CATALOGUE". |
| Ro 25-6981 | RECORD_WITHOUT_THE_INTENDED_TARGET | Record `CAT:DGIDB:f98b32d5fbc4` named "Chembl:Chembl305195", synonym RO-25-6981, only target DRD1 (DTC claim, no identity check). ChEMBL CHEMBL305195 SMILES (string omitted here because it reads as a markdown link) is the Ro 25-6981 structure, so the record is the right molecule. | Literal verdict SUPPORTED. Same caveat as ifenprodil. The DRD1 claim has no identity check and should not be read as a target of the compound. |
| GYKI 52466 | NAME_MISMATCH_Gyki53784 (found GRIA1;GRIA2) | The only record is "Gyki53784" (dgidb_drug_name GYKI53784, IUPHAR ligand 4210); "GYKI-52466" appears only as a synonym string. The catalogue also holds a separate "Gyki53655" (4209). GYKI 53784 (LY303070) and GYKI 52466 are different molecules in the literature; I could not confirm the GtoPdb ligand (401). | Verdict wording (NAME_MISMATCH) is cautious and correct. But the columns `intended_targets_found = GRIA1;GRIA2` credit a differently named record. CANNOT TELL whether that record is GYKI 52466; the targets must not be read as GYKI 52466's. |

Other identity_check defect: ivabradine "intended_targets_missing HCN1;HCN2". The DGIdb record "Ivabradine" (`CAT:DGIDB:fcc164e2d2b6`) lists HCN1, HCN3, HCN4. The script only reads DGIdb symbols from `dgidb_named_tools.tsv`, which has no ivabradine row, so the DGIdb genes of ivabradine were never resolved. HCN1 is present. HCN2 is absent from the catalogue records I found.

R6 and by_action: `by_action.tsv` line 168 (R6) is a placeholder row (`NO_CATALOGUE_MECHANISM_ROW`, no id, no direction). `conditional_proposals.py` counts `len(rows)` and so writes in CP-BH3 "R6: 1 catalogue rows on the target symbols; 0 reduce activity, 1 raise it or have no direction". That converts "no ChEMBL mechanism row found" into "1 catalogue row...raise it". Meanwhile `identity_check.tsv` reports carbenoxolone TARGET_CONFIRMED with GJA1, GJD2, PANX1 (DGIdb/GtoPdb inhibitor claims; the DGIdb record has 26 targets). The two files disagree: by_action says no mechanism row; identity_check says three intended targets confirmed. The by_action search used only ChEMBL curated human mechanism rows, and ChEMBL's carbenoxolone mechanisms are HSD11B1/2.

Other absence statements, with scope:
- CP-BH2 step 2 "DATO: no isolated NMDAR current, subunit, glycine or Mg2+ datum exists for this preparation" is unscoped; BH1 step 2 scopes to "within the perimeter of the paper text and supplement". CP-MH2 step 1 "no voltage-clamp Ih exists" is also unscoped, while source O11 scopes to "in the paper or its supplement". Correction: add "in the paper and supplement read".
- IT40 A2/B1/B8 are scoped ("in the paper text and supplement", "in this work"): supported.

Corrections: rename NOT_IN_CATALOGUE to NO_ENTRY_MATCHED_UNDER_NAMES_SEARCHED and add synonym lookup (D-AP5, AP5, APV, Acid Blue 9, FD&C Blue No. 1); re-run d-APV; resolve DGIdb for ivabradine and (R,S)-ifenprodil; for R6 report "0 ChEMBL mechanism rows; DGIdb/GtoPdb claims: carbenoxolone (GJD2, PANX1, GJA1, GJB1)" and exclude placeholder rows from counts.

---

## Q5. Same datum counted as several confirmations: NOT SUPPORTED as counts of independent items (the label says "rows", but nothing says one record is repeated)

Distinct molecules, from `mechsearch_it40_20261109/by_action.tsv` using the catalogue's own parent/child relation (`relations.parent`) to merge salts and parents:

| Relation | Rows (as in CP) | Distinct catalogue records | Distinct parent molecules | Reducers (molecules) | Raise (molecules) | Molecules with a record of at most 2 genes |
|---|---|---|---|---|---|---|
| R1 (GRIN2B) | 28 | 28 | 24 | 21 | 3 | 4 (radiprodil, traxoprodil [+mesylate], rislenemdaz, EVT-101) = 5 records |
| R2 (GRIN2A) | 25 | 25 | 21 | 18 | 3 | 1 (dextromethorphan; 2 records, HBr and polistirex) |
| R1 and R2 together (CP-BH2) | 28 + 25 | 30 | n/a | n/a | n/a | n/a. 23 of the 28 R1 records and 23 of 25 R2 are the same records (same 7-gene ChEMBL target record CHEMBL2094124). |
| R3 (AMPA/kainate) | 74 | 15 | 15 | 9 (perampanel, topiramate, becampanel, dasolampanel, irampanel, selurampanel, talampanel, tezampanel, zonampanel) | 6 positive modulators | 2 (talampanel x2 records, dasolampanel) |
| R4 (HCN) | 3 | 3 | 2 (ivabradine as parent plus hydrochloride, dronedarone) | 2 | 0 | 2 |
| R5 (Kv7) | 36 | 9 | 7 | 5 blockers | 2 openers (ezogabine, flindokalner) | 1 (flindokalner) |
| R6 | 1 | 0 (placeholder) | 0 | 0 | 0 | 0 |

Specific double counts:
- R3: the same record is repeated once per gene symbol. 56 of the 74 rows are CHEMBL2096670 (the 4-gene GRIA1-4 record: 14 molecules x 4 symbols), 15 rows CHEMBL2109241 (GRIK1-5), and 3 single-gene rows. "74 rows, 50 reduce" is 15 molecules, 9 reducing. This is a 4.9-fold (74/15) inflation, 5.6-fold for reducers.
- R5: "36 rows, 28 reduce" is 9 records, 7 parent molecules, 5 blockers (amifampridine x2 records, dalfampridine, guanidine x2, tedisamil x2, nerispirdine). Blockers of Kv channels are the opposite of the R5 action (opening); only 2 molecules (ezogabine, flindokalner) are openers.
- R4: "3 rows, 3 reduce" is ivabradine (parent record and hydrochloride record) plus dronedarone, a multi-ion-channel antiarrhythmic whose HCN4 row is one of several single-gene rows of CHEMBL1201729 (CACNA, KCNJ2, SCN, HCN4). So R4 is one HCN-oriented molecule counted twice, plus one non-selective compound.
- R1 and R2 for CP-BH2: 23 records are counted under both relations.
- The same experimental arm is listed twice in the expected-result cell (M04 appears twice in CP-BH1 and in CP-BH2, via BE2 and BE4/BE5 blocks). Cosmetic.

Whether this is "counted as confirmation": no CP text says "N independent supports". The stated unit is "catalogue rows". But the summary puts the row count first with "reduce activity" and "subunit-specific", and no distinct-molecule count; a reader will take 74 or 36 as breadth of support.

Correction: report distinct parent molecules (R1 24 [21 reducing], R2 21, R3 15 [9 antagonists], R4 2, R5 7 [2 openers]), with rows in brackets, and say that rows are record x gene symbol.

---

## Q6. Burst suppression presented as proof of a defect: PARTLY (guard sentences present in all six rows; two chain steps and one BE4 line lean the other way)

Supported:
- Explicit guards: CP-BH1 source_and_limits "a drug response is not proof of a defect in its target"; CP-MH1 premise "a drug response is not proof of a defect in its target"; CP-MH2 "A blocker-mediated sag reduction does not show an HCN defect", "Sag reduced by a blocker with burst incidence unchanged supports HCN in sag, not benefit"; CP-BH3 "the gap-junction half...stays withdrawn"; INV-18 A3/A5 and INV-05 B6 ("abolition alone is not informative"); `by_action.tsv` R4 "tool response only; shows contribution, not a defect", R5 "a response would not show a leak deficit", R6 "not attributable to gap junctions on present data". No applied text says a target is defective because a drug changed bursts or sag.

Not fully supported:
1. CP-BH1 step 4: "IPOTESI: ... with NMDAR current required for the burst as d-APV shows". The package's own M03 note says all seven hypotheses predict d-APV abolition and "the arm ... cannot separate any hypothesis", and CP-BH2 lists AB04 (general loss of drive) with "d-APV is then not NMDAR-specific evidence". The chain also states in CP-BH2 step 1 "DATO: bursts need NMDAR activity". These move from "d-APV 50 uM abolishes bursts" to "NMDAR current is required". Correction: "bursts are abolished by d-APV 50 uM (OB04); whether that reflects NMDAR gain, permissive necessity or general loss of drive is not separated".
2. CP-BH3 step 4: "an effect on release and excitability is sufficient to explain it" (Q3 item 2). It names a mechanism for the burst fall from a culture result.
3. CP-MH2 "premise_and_action" lists "HCN blockade as a TOOL arm ... reading ... burst incidence" with the hypothesis that an excess sag would be "larger HCN contribution". It is guarded (premise "NOT established", "UNVERIFIABLE") and I count it as acceptable.

---

## Q7. R1 claim "targets whose record has at most two genes are subunit-specific records; the rest are multi-gene complex records, not subunit-selective": NOT SUPPORTED as a general rule; correct only for the radiprodil group, and the wording "subunit-specific" is wrong for the others

What the 2-gene record is. For radiprodil (`CAT:CHEMBL182066`), traxoprodil (`CAT:CHEMBL17350`), rislenemdaz (`CAT:CHEMBL2068839`), EVT-101 (`CAT:CHEMBL3545349`): ChEMBL curated mechanism, target `CHEMBL1907603`, target_name "Glutamate NMDA receptor; GRIN1/GRIN2B", gene_symbols GRIN1, GRIN2B, mechanism text "GRIN1/GRIN2B antagonist", action ANTAGONIST. This is a heteromer-assembly record (GluN1 plus GluN2B). It supports "the catalogue names a GluN1/GluN2B receptor as the target". It is not a measurement of selectivity (no potency is carried: "NOT_CARRIED") and does not say GluN2A/2C/2D were tested. For these four drugs the reading agrees with the package (radiprodil GluN2B-selective in oocytes, with the unread supplementary figure caveat from Q2).

What the 7-gene record is (memantine, CHEMBL1699): target "Glutamate [NMDA] receptor", genes GRIN1, GRIN2A, GRIN2B, GRIN2C, GRIN2D, GRIN3A, GRIN3B; mechanism text "Glutamate [NMDA] receptor negative allosteric modulator". It is a family-level target record: subunit not resolved. "Not subunit-selective" over-states; the record says "subunit not resolved in the catalogue".

Why the rule fails (single-gene records are not selective):
- R2: dextromethorphan HBr and polistirex have a single-gene record (CHEMBL1972, GRIN2A). Dextromethorphan is not GluN2A-selective; the record is a per-protein mechanism row.
- R3: talampanel has separate single-gene records for GRIA1 (CHEMBL2009) and GRIA2 (CHEMBL4016), and dasolampanel one for GRIK1 (CHEMBL1918). Talampanel is a pan-AMPA antagonist (its DGIdb record lists GRIA1-4). The "3 subunit-specific rows" are 2 molecules, one of which is listed twice.
- R4: ivabradine and dronedarone are in the "subunit-specific" bucket via a single HCN4 row. The package describes ivabradine as "a nonselective inhibitor of HCN isoforms" (CP-MH2 compound cell), the DGIdb record lists HCN1, HCN3, HCN4, and the neocortical sag work in the source is HCN1/2-dominated tissue. Labelling an HCN4 row "subunit-specific" is the opposite of the source. Dronedarone's HCN4 is one of several single-gene rows of a multi-channel drug.
- R5: flindokalner appears with a 2-gene and 1-gene record per symbol (KCNQ2, 3, 4: two-gene records; KCNQ5: single). It is a "ACTIVATOR" row. In the CP summary the "at most two genes" count is taken only over the reducing rows (`spec = [r for r in down ...]`), so R5 reports "0 through a target record of at most two genes" while 4 rows (the only opener) satisfy it.

Conclusion: the gene count of a ChEMBL target record reflects target-record granularity (single protein, assembly, family), not drug selectivity.

Correction: replace "(subunit-specific record)" by "(single-protein or two-gene assembly record; says where ChEMBL attached the mechanism, not selectivity)" and "not subunit-selective" by "subunit not resolved by the catalogue record"; compute the ≤2-gene count over all rows of the relation (not only `down`); in R4 add "package describes ivabradine as nonselective across HCN isoforms; HCN1/2 are the isoforms relevant to neocortical sag".

---

## Summary of corrections by priority
1. Fix `d-APV` identity verdict (D-AP5 is in the catalogue) and the R6 placeholder count.
2. Replace row counts by distinct molecules in `catalogue_by_action` (R3 74 -> 15, R5 36 -> 7, R4 3 -> 2, R1+R2 shared).
3. Reword "subunit-specific" / "not subunit-selective" (Q7).
4. Stop truncating matrix and experiment cells; carry the non-separation notes and the INFERENZA label.
5. Restore dropped competing explanations (BH2, MH1, MH2, MH3).
6. Remove the 3.9/2.9 SE statement and the word "supported" for flat tau, or replace by the propagated z of about 1.1-1.4.
7. BE4 wording on perampanel/radiprodil/carbenoxolone reversibility; soften BH3 step 4 and BH1 step 4.
8. Add the radiprodil "unread supplementary figure" limit to CP-BH2.

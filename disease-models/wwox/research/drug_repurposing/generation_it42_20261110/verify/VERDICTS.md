# IT42 independent verification: verdicts

Non-canonical working note. Not medical advice. No SMILES, no e-mail, no personal data.
Dispatch: the caller dispatched this verifier as model `sonnet`, effort `high` (stated by the dispatch; not read back from a transcript by me). No agent was started. Written only in this folder.
Paths are relative to `disease-models/wwox/research/drug_repurposing/` unless absolute. PubMed was used only for PMIDs 27475601, 34493631, 36642931, 40767837 (attribution: PubMed; DOIs 10.1063/1.4958882, 10.1124/jpet.120.000370, 10.1002/cpdd.1217, 10.4088/JCP.23m15246).

Originals used: GtoPdb `catalog/cache/gtopdb/interactions.csv` (version line "GtoPdb Version: 2026.3.1 - published: 2026-10-12") and `ligands.csv`; the catalogue `catalog/catalog.jsonl.gz` through `compound_catalog.load`; `identity_it41_20261109/identity_table.tsv`; `catalog/tool_identity_declarations.tsv`; `target_first_it15_qa_nmdar_20261101/relations_qa.tsv`; `generation_it41_20261109/{search_rows,relations_it41,compound_view}.tsv`; `git grep`.
My own recounts used a separate script (scratchpad, not shipped) that reads the catalogue and the GtoPdb CSV directly, not `search_rows.tsv`.

## Summary table

| Claim | Verdict |
|---|---|
| C1 sample of 41 rows | PARTLY (0 verdicts wrong against the relation columns; 1 stratum not sampled; the CANDIDATE label for unevaluable fields contradicts the engine's own docstring and hides about 100 rows) |
| C2 recount Q1, Q4, Q5 | PARTLY (row counts and class counts reproduce; "distinct units" are not distinct: Q1 63 should be 53, Q5 15 should be 12) |
| C3 S7 items V11, V12 | PARTLY (numbers and phases supported; three statements stronger than or different from their source) |
| C4 Case 2 and Case 3 | SUPPORTED |
| C5 provenance | PARTLY ((a) supported; (b) the number is indeed not a relevant PMID, but it is the ChEMBL activity_id column, not "the reference field"; (c) three phrases go beyond the abstracts) |
| C6 transfer, negatives, double counting | PARTLY (one cross-gene source misplaced, one unscoped "no record", systematic double counting from a join that never ran) |

---

## C1. Sample check of `verify_sample.tsv`: PARTLY

Method. For each of the 41 rows I took the file line in `generation_it41_20261109/search_rows.tsv` (header is line 1; names matched on all 41), read the original source record (GtoPdb CSV row, or the catalogue ChEMBL target record) and applied the relation's own columns: S1 `wanted_direction=down`, `site_policy=allosteric_subunit`, `subunit_in=GluN2B|NR2B|GRIN2B`, `subunit_out=GluN2A|GluN2C|GluN2D|NR2A|NR2C|NR2D`; S2 down/any; S3 up/any; S4 down/any; S5 up/any; S6 `SLC12A2:down;SLC12A5:up`; S8 down/any.

The sample is 41 rows over 9 of the 10 (verdict, reason, source) strata of `search_rows.tsv`. Stratum with no sampled row: EXCLUDED / direction_opposite / ChEMBL (76 rows). I read all 76 from the action table instead: S1 PAM and partial-agonist records (3), S3 BLOCKER (28), S5 ALLOSTERIC ANTAGONIST, ANTAGONIST, INVERSE AGONIST (21), S8 POSITIVE ALLOSTERIC MODULATOR (24). All correct against `wanted_direction`. No script for "seed 42" is in the package, so the draw cannot be reproduced; and 4 of the 538 ChEMBL CANDIDATE/ok rows were sampled, all in S5 (none in S2, S3, S7, S8).

### Row-by-row (R = engine verdict right against the source and relation columns)

| file_line | name, target | engine | my reading | note / source quotation |
|---|---|---|---|---|
| 1027 | tezampanel GRIA3 (S8) | CANDIDATE ok | R | GtoPdb: Type "Antagonist", Action "Antagonist", Selectivity "Selective", human; wanted down. |
| 290 | AZD6280 GABRA2 (S5) | CANDIDATE ok | R | Catalogue: "POSITIVE ALLOSTERIC MODULATOR", mechanism "GABA receptor alpha-2 subunit positive allosteric modulator", one gene (single_protein_record). |
| 198 | carbenoxolone PANX1 (S4) | CANDIDATE ok | R | GtoPdb: Type "Inhibitor", Action "None", Non-selective, human; wanted down. |
| 466, 432, 410 | alprazolam, adipiplon, midazolam GABRG2 (S5) | CANDIDATE ok | R by the relation (site any, subunit_in empty) | Each is one 16-gene record ("GABA-A receptor; anion channel", PROTEIN COMPLEX GROUP). The reason "ok" does not say the subunit is unresolved; the column `site_or_granularity` does. Presentation caveat only. |
| 91, 83, 81, 74, 73 | ivabradine Hcn2, propofol Hcn1, MEL57A Hcn1, clonidine Hcn1, cilobradine HCN1 (S2) | CANDIDATE unknown_fields | R on direction; label see Finding F1 | GtoPdb Type "Channel blocker" for all five; Action "Antagonist" or "None". MEL57A is a "Channel blocker" with Affinity Units pEC50 (EC50 320 nM on Hcn1): the unit is odd for a blocker; the row's own PMID 22091830 is outside the PubMed set allowed to me, so I cannot tell whether "blocker" is right at source. The engine follows the registry label. Species Mouse (Hcn) matches the mouse context of S2. |
| 176 | retigabine KCNQ4 (S3) | CANDIDATE unknown_fields | R | Type "Activator", pEC50 5.2 (EC50 6310 nM), human, primary target true. |
| 61, 62, 65, 63, 66, 64 | amantadine, dizocilpine, N1-dansyl-spermine, ketamine, phencyclidine, Mg2+ GRIN2B (S1) | EXCLUDED channel_blocker | R by `site_policy=allosteric_subunit` | All six: "Channel blocker/None". Action comments on three confirm non-selectivity for GluN2B ("GluN2C = GluN2D >= GluN2B >= GluN2A", "GluN2A = GluN2B >> GluN2C = GluN2D", "GluN2A = GluN2B > GluN2C = GluN2D"). Note F4: `relations_it41.tsv` S1 `wanted_actions` lists "Channel blocker" while the policy excludes it. |
| 1021 | piracetam GRIA3 (S8) | EXCLUDED direction_opposite | R | "Allosteric modulator/Positive": a potentiator in an antagonism relation. |
| 774 | picrotoxin GABRA2 (S5) | EXCLUDED direction_opposite | R | "Channel blocker/None", wanted up. |
| 1054 | LY339434 GRIK1 (S8) | EXCLUDED direction_opposite | R | "Agonist/Agonist". |
| 845 | compound 20 [PMID: 35584373] GABRA5 (S5) | EXCLUDED direction_opposite | R | "Allosteric modulator/Negative". |
| 30 | D-aspartic acid GRIN2B (S1) | EXCLUDED direction_opposite | R | "Agonist/Agonist", Receptor Site "glutamate site". |
| 695 | CGS8216 GABRA1 (S5) | EXCLUDED direction_opposite | R | Type "Agonist", Action "Inverse agonist", pKi 10.3. The engine reads the combined string and the inverse agonist wins. |
| 21, 16, 14, 7, 9, 18 | AV-101, ralfinamide, delucemine, amantadine HCl, ketamine HCl, esketamine HCl GRIN2B (S1) | EXCLUDED family_record_subunit_unresolved | R as a policy outcome; label arguable, see F2 | Catalogue: each record is "Glutamate [NMDA] receptor ..." with 7 genes (GRIN1, GRIN2A, GRIN2B, GRIN2C ...), PROTEIN COMPLEX GROUP; actions ANTAGONIST or NEGATIVE ALLOSTERIC MODULATOR. The record does not name GluN2B, so "not subunit-directed" is right; "excluded" is not the same as "shown not to act at GluN2B". |
| 47, 43, 53, 48, 51, 44 | GV196771A, CGP37849, selfotel, L689560, NVP-AAM077, conantokin-G GRIN2B (S1) | EXCLUDED orthosteric_site | R | Receptor Site "glycine site" or "glutamate site" in each row. |
| 39 | DQP-1105 Grin2b rat (S1) | UNKNOWN assay_names_other_subunit | R | Assay Description: "Measured using recombinant GluN1-1a NMDA subunits co-expressed with GluN2C subunits." pIC50 6.95 sits under the GluN2B target; `subunit_out` matches GluN2C. It is a GluN2C datum filed under GluN2B; UNKNOWN (never a GluN2B datum) is the right handling. |
| 1025, 983, 1005, 1047 | GYKI53784 GRIA3, GRIA1, GRIA2, GRIA4 (S8) | UNKNOWN label_conflict | R | See C4. |

Result: 0 verdicts wrong, 0 cannot-tell on direction, site or subunit. Findings below are about labels and unsampled classes.

**F1. "CANDIDATE" is given to rows whose check cannot be evaluated, against the engine's own docstring.** `generation_it41_20261109/action_search.py`, `qualify()`: docstring "UNKNOWN: a check cannot be evaluated (a field is missing ...) - never read as negative"; the last line is `return ("CANDIDATE" if not unk else "CANDIDATE"), ("ok" if not unk else "unknown_fields"), ...` (both branches CANDIDATE). Rows affected in `search_rows.tsv` (CANDIDATE, reason unknown_fields): 84, namely S2 assay_text 33, S3 assay_text 28, S1 receptor_site 2 plus 1 (receptor_site and assay_text), and **direction unknown 20 rows in S5 (17) and S8 (3)**. For S2 and S3 the flag is vacuous: `subunit_out` is empty in `relations_it41.tsv` for S2 and S3, so a missing assay text cannot hide anything; for S1 it is real (onfasprodil: no site, no assay text). The direction-unknown rows are the serious ones: `search_rows.tsv` S5 lines for flumazenil ("Allosteric modulator/None", GABRA2, GABRA3, GABRA5), alpha3IA (GABRA3), [3H]CGS8216 ("Allosteric modulator/Mixed"), etazolate ("Allosteric modulator/Binding", GABRB3) are CANDIDATE for a **positive**-modulation relation although the direction is not in the record; in S8 `[3H]AMPA` (an agonist radioligand, "None/None", GRIA3) and `[3H]CNQX` are CANDIDATE for **antagonism**. None of these classes is in the 41-row sample (the unknown_fields stratum sample is 6 S2/S3 rows). Correction: return UNKNOWN when `unk` contains `direction` (and for `receptor_site` when `site_policy` is not `any`); drop the `assay_text` flag when `subunit_out` is empty; re-run and re-score.

**F2. EXCLUDED versus UNKNOWN for family records.** The same condition gives CANDIDATE in S5 (site any) and EXCLUDED in S1. For S1 the protocol's E2 defines it as "presented as if it were subunit-directed", so exclusion from the shortlist is defensible, but `eval_summary.md` counts these 20 units as "excluded with a reason" (55) beside the one UNKNOWN. Correction: state in `eval_summary.md` that the 20 ChEMBL family-record exclusions are "subunit not stated", not "not GluN2B".

**F3. Reproducibility.** Add the sampling script (seed 42) and the stratum sizes to the package, or state that the draw was manual.

**F4. S1 relation row is internally inconsistent.** `relations_it41.tsv` S1 `wanted_actions` = "Antagonist;Negative;Inhibition;Channel blocker" and `site_policy=allosteric_subunit` (which excludes channel blockers and orthosteric ligands). Not a verdict error, but the "wanted action" column suggests a channel blocker is wanted.

---

## C2. Recount of Q1 (S1), Q4 (S6), Q5 (S7): PARTLY

### Q1 (S1, symbol GRIN2B)

Raw recount (catalogue `targets` with source "ChEMBL curated mechanism", organism Homo sapiens, gene_symbols containing GRIN2B; GtoPdb rows whose Target Gene Symbol contains GRIN2B in any case):
* ChEMBL: 28 rows; GtoPdb: 39 rows (38 human, 1 rat); total **67 rows, 63 distinct ids**: reproduces `eval_results.tsv` (A1: 67, 63, E4 4). ChEMBL 28 rows, 24 parents (four parents with two rows: orphenadrine, delucemine, esketamine, traxoprodil): reproduces A0.
* Classes of the 63: the engine's own class counts reproduce exactly: E1 (agonist or positive modulator) 13 = 3 ChEMBL (neboglamine PAM, rapastinel and apimostinel partial agonists) + 9 GtoPdb agonists (D-aspartic acid, D-serine, glycine, L-aspartic acid, [3H]glycine, homoquinolinic acid, tetrazolylglycine, NMDA, (+)-HA966) + SAGE-718 positive; E2 54 = 20 ChEMBL family records + 27 glutamate/glycine-site rows (9 agonist, 18 antagonist) + 7 channel blockers.

**But the 63 are not distinct molecules.** In `search_rows.tsv` **0 of 471 GtoPdb rows carry a `catalogue_id`**: the catalogue holds no GtoPdb `source_records` (source counts in `catalog.jsonl.gz`: dgidb, chembl, matrix, openfda_ndc), so `gt_to_cat` in `action_search.py` is empty and no cross-source merge can happen. `eval_protocol_it42.md` says path B uses "cross-source merging by catalogue parent" and defines E4 to include "radiolabelled forms, cross-source copies, stereoisomers". The code counts none of these (E4 = 4 = ChEMBL salt rows only). In S1 A1:
  * 8 radiolabelled GtoPdb ligands are units: [3H]glycine, [3H]CGP39653, [3H]CGP61594, [3H]CGS19755, [3H]CPP, [3H]L689560, [3H]MDL105519, [3H]dizocilpine (three of them have the cold ligand also in the list: glycine, L689560, dizocilpine). `action_search.py` itself drops labelled forms from `molecules.tsv` ("radiolabelled forms duplicate another record of the same ligand") but `eval_it42.py` keeps them as units.
  * amantadine (GtoPdb 4128 and ChEMBL CHEMBL660) and ketamine (GtoPdb 4233 and ChEMBL CHEMBL742) are each two units.
  * ketamine and esketamine (separate ChEMBL parents) are stereoisomers, also E4 by the protocol's own definition (not subtracted below).

Corrected Q1 A1 (labelled forms removed, same-name cross-source merged): **53 units** (not 63). E1 12 (not 13), E2 44 (not 54), units with an unflagged error 46 (not 56), excluded with a reason 45 (not 55), clean 7 and UNKNOWN 1 unchanged. B is unchanged (7 units, 8 rows). The qualitative conclusion (the added source brings many misleading rows) stands; "63 units of which 56 carry an unflagged error" in `eval_summary.md` becomes 53 and 46.

Two further points on the same table. (i) The B shortlist's 7 "clean" units include S-deschloroketamine (GtoPdb 11720: "Antagonist/Antagonist", no receptor site recorded, assay text "Binding affinity for hGluN1/hGluN2B receptors expressed in HEK293 cells"). It is named as a ketamine derivative while ketamine itself is excluded as a channel blocker; the scorer cannot see this because its E2 test uses the same fields as the engine (stated in `eval_summary.md` Limits, acknowledged). Its "clean" label rests on a missing site, which is the unknown_fields case of F1. (ii) "B: unflagged errors 0" is by construction, because the E1, E2, E3 and E5 tests in `eval_it42.py` re-implement the engine's rules; the summary says so under Limits, but the headline "56, 11, 24, 2, 0 -> 0" in `README.md` does not.

### Q4 (S6): SUPPORTED
SLC12A2 + SLC12A5: ChEMBL curated-mechanism rows in the catalogue: 0 (bumetanide and furosemide are curated against SLC12A1 only), GtoPdb rows: 6, all "Inhibitor/Inhibition", human: SLC12A2 bumetanide pIC50 5.6, furosemide 5.13, piretanide 5.62, IAMA-6 (no value); SLC12A5 DIOA (no value) and VU0240551 pIC50 6.25. Table: A0 0, A1 6 rows/6 units, E1 2, clean 4, B 4, excluded 2. All reproduce. Scope note: the catalogue also holds DGIdb interaction claims for these genes (SLC12A5: 4, SLC12A2: 5, no action stated for bumetanide) that neither path reads; "A0 = 0" is a statement about ChEMBL curated mechanisms only.

### Q5 (S7): PARTLY
Raw: ChEMBL 2 rows (tiagabine on SLC6A1, vigabatrin on ABAT, both "INHIBITOR"); GtoPdb 14 rows (ABAT 3: 4-acryloylphenol pIC50 5.26, CPP-115 pKi 5.01, vigabatrin pKi 3.07; SLC6A1 11 rows covering 10 ligands, E2730 twice: pIC50 5.96 uptake and pKd 6.15 binding, different measurements; one mouse row, LU32-176B Slc6a1). 16 rows, 15 ids: reproduces. Every row is an inhibitor: E1, E2 = 0 reproduces.
Not distinct: tiagabine is three units (ChEMBL, GtoPdb "tiagabine", GtoPdb "[3H]tiagabine"), vigabatrin two (ChEMBL, GtoPdb). Corrected: **12 distinct molecules**, A1 = B = 12 (not 15); "2 -> 15" in `eval_summary.md`, `eval_table.md` and `README.md` becomes "2 -> 12". If enantiomers are merged ((R)-EF-1520 and (S)-EF-1520) it is 11. The statement "Q5 B equals A1" holds.

### Other relations (not asked, same defect, name-key estimate of mine)
Distinct molecules after removing labelled forms and merging same-name cross-source rows: Q3 (S5) A1 125 -> about 102, B 101 -> about 82; Q2 (S3) B 18 -> 17; Q6* (S8) A1 60 -> about 53, B 28 -> about 23. These are estimates from name matching, not authoritative; the right fix is to carry a GtoPdb-to-catalogue join (ligands.csv has InChIKey and ChEMBL ID columns).

Also: `eval_table.md` is stale (run 2): Q3 A0 shows 70 clean and E1 1 where `eval_results.tsv` (run 3) has 68 and 3; Q3 A1 shows 108 clean and E1 17 where `eval_results.tsv` has 101 and 24. Regenerate or delete.

---

## C3. S7 items V11, V12 in `generation_it41_20261109/compound_view.tsv` and `second_relation_it42.md`: PARTLY

Supported against the originals:
* V11 "maximum phase 4 for one reference compound": catalogue ChEMBL status record for tiagabine, `max_phase: 4.0`, scope "highest clinical phase curated by ChEMBL for any indication ... not an agency approval statement". Supported (the scope caveat is not repeated in V11; acceptable).
* V12 "(catalogue maximum phase 1)" for the newer drug: CPP-115 `CAT:CHEMBL4297273`, `max_phase: 1.0`, status class clinical_candidate. Supported.
* V12 registry_note "pKi 3.07 for the older drug and pKi 5.01 for the newer one": GtoPdb human ABAT, vigabatrin Affinity Median 3.07, Original Ki 850000 nM; CPP-115 5.01, Ki 9700 nM. Supported.
* V11 "lists several selective tools": GtoPdb Selectivity "Selective" for CI-966, E2730, NNC-711, SKF89976A, the EF-1520 enantiomers, tiagabine (7851497, pIC50 7.2). Supported; the labelled [3H]tiagabine is "Non-selective" and LU32-176B is a mouse row, neither is named.
* Role consistency with `git grep -l -i` (tracked files outside `generation_it4*`, `view/`, `next_batch_it42*`): vigabatrin 616 files, CPP-115 123, tiagabine 36, NNC-711 11, 4-acryloylphenol 6. The repository already carries tiagabine with NNC-711 as the GAT-1 arm in the IT14 package (`function_pharm_it14_p3_20261101/cases_it14_p3.tsv` row A1) and a fly result (`deepdive_manifests/PMID41378214.json`: "tiagabine had no evident effect" on seizure susceptibility in R44Q flies), so "known_requalified" for V11 is consistent with the material. Vigabatrin is the best-covered name in the repository (a card, H02, and brief B1), yet V12 labels it "unresolved" while V11 labels the same molecule "known_requalified": the kind taxonomy has no rule for one molecule in two items. 4-acryloylphenol (6 files) is a named V12 compound that V12 never describes.

Not supported or stronger than the source:
1. **V12 registry_note: "both labelled inhibition"** is wrong for vigabatrin. GtoPdb row: Type "Inhibitor", Action **"Irreversible inhibition"**; CPP-115: Action "Inhibition". Correction: "vigabatrin labelled irreversible inhibition, CPP-115 labelled inhibition".
2. **V12 title and action: "affinities of irreversible inhibitors", "compounds that act irreversibly"** rests on the registry only for vigabatrin. For CPP-115 and 4-acryloylphenol the GtoPdb rows say plain "Inhibition"; CPP-115 as a GABA-aminotransferase inactivator is the repository's own wording (`batch_sci_20261105/BRIEF_B1.md`, "its sibling GABA-aminotransferase inactivator CPP-115"), not the registry's. Correction: say which source states irreversibility for each compound.
3. **4-acryloylphenol is not primarily an ABAT ligand in the registry.** GtoPdb: on ABAT "Primary Target: false", pIC50 5.26 (IC50 5480 nM, PMID 16290145); the same ligand on ALDH5A1 (succinic semialdehyde dehydrogenase) is "Primary Target: true", pIC50 6.46 (IC50 350 nM). V12 lists it as a GABA-transaminase lever without saying so, and its ABAT value is a pIC50, not a pKi like the other two. Correction: add this to `registry_note`.
4. **V11 counter: "resolved spasms in published cases"** is stronger than the repository: `disease-models/wwox/research/discovery_ledger_current.md` DL-MECH-038 (Shaukat 2018, full text read): case 1 "the spasms resolved", case 2 vigabatrin "risposta parziale". V12 says "in one child", which is right; V11 says "cases". Also the repository records three null reports (`ranking_it8_p9_20261029/member_evidence.tsv` U20 vigabatrin: "2 benefit, 3 null, 1 partial_benefit, 1 unresolved") and VABAM in two WWOX-DEE children at abstract level (working model line 99); V11's counter lists only the favourable half. Correction: "spasms resolved in one of two reported children (partial response in the other); 3 null reports; imaging abnormality reported in two children at abstract level".
5. V11 `name_full` lists vigabatrin under a GAT-1 item; vigabatrin acts on ABAT (V12). Cosmetic.
6. `second_relation_it42.md`: "in P13-P17 mouse cortex the response is mostly hyperpolarising" has no source in the note. It is background, and the same sentence says the state of this preparation is unmeasured; acceptable if marked as background.

---

## C4. `trace_it42.md` Cases 2 and 3: SUPPORTED

**Case 2.** GtoPdb `ligands.csv`: ligand 4210 Name "GYKI53784", Synonyms "GYKI-52466|LY303070", InChIKey flat block equal to the GYKI 52466 structure, ChEMBL ID CHEMBL275006; ligand 4209 Name "GYKI53655", Synonyms "GYKI 53655|GYKI-53655|LY300168", CHEMBL267450. `identity_table.tsv`: the rows with query_name "GYKI 52466" carry record_name "Gyki53784" and label_conflict "yes" (GRIA1, GRIA2); the rows with query_name "GYKI 53655" carry record_name "Gyki53655" and label_conflict "no". `action_search.name_key` reduces both the GtoPdb label "GYKI53784" and the record name "Gyki53784" to "gyki53784", so the join works through `record_name`. `search_rows.tsv` S8: the 4 GYKI53784 rows (GRIA1-4) are UNKNOWN / label_conflict; the 4 GYKI53655 rows are CANDIDATE / ok. The conflict is real in the registry itself: the GtoPdb row for 4210 carries the comment "active isomer, non-competitive" beside the GYKI 52466 structure, and `catalog/tool_identity_declarations.tsv` documents the label on two structures (dated 2026-11-09). Supported.

**Case 3.** GtoPdb `interactions.csv`, Target Gene Symbol SLC12A5 or Target "K-Cl cotransporter 2": two rows only, DIOA ("Inhibitor/Inhibition", no value) and VU0240551 ("Inhibitor/Inhibition", pIC50 6.25, PMID 19279215); no activator or potentiator row. Both are EXCLUDED / direction_opposite in `search_rows.tsv`. The ligand table and the catalogue names/synonyms hold no CLP257 or CLP290 and `git grep` finds none outside notes. Supported. Scope to add: "in the two sources read (ChEMBL curated mechanism, GtoPdb 2026.3.1)"; DGIdb holds four SLC12A5 claims for bumetanide, DIOA and VU0240551 without an activating action.

---

## C5. `provenance_it42.md`: PARTLY

**(a) SUPPORTED.** `relations_qa.tsv`: GtoPdb onfasprodil row `value_nM` 8.317639172213713, measure_type pIC50; GtoPdb CSV pIC50 8.0799999 -> 10^(9-8.08) = 8.3176. NP10679 row `value_nM` 22.908683570453768, GtoPdb pIC50 7.64 -> 22.9. The ChEMBL activity row: IC50, "=", `value_nM` 8.3, units_raw nM, same magnitude. The GtoPdb CSV also carries the original IC50 8.3 nM for onfasprodil (23 nM for NP10679). Two small points: the heading "One datum, three representations" asserts identity, while the body leaves open whether the ChEMBL and GtoPdb rows are one measurement or two; and the GtoPdb onfasprodil row is sourced to a patent (Patent Numbers "US10239835B2"; no PMID, no assay text), which the provenance note does not say (V06 `registry_note` does).

**(b) PARTLY.** PubMed 27475601 is "A curved edge diffraction-utilized displacement sensor for spindle metrology" (Rev Sci Instrum 2016): not a relevant paper, as claimed. But **27475601 is not "the reference field"**. In `relations_qa.tsv` the ChEMBL onfasprodil row has `ref` = "CHEMBL1907603;CHEMBL5726760;CHEMBL5733282" and the number 27475601 sits in the last column, **`activity_id`**. Correction in `provenance_it42.md` (table row "Data already in the repository", the second bullet under "Two corrections", and the P3 line of `README.md`): "27475601 is the ChEMBL activity_id of that row; it coincides numerically with an unrelated PubMed id; the row's document identifiers are the three CHEMBL ids in `ref`". The conclusion that it must not be followed as a PMID stands; the diagnosis of which field it is was wrong.

**(c) PARTLY.**
* onfasprodil: "a selective NR2B negative allosteric modulator; a phase 2 study in adults with treatment-resistant depression (PMID 40767837)". Abstract: "highly potent and novel selective NR2B subunit negative allosteric modulator", "phase 2, randomized, placebo-controlled", patients with treatment-resistant major depression. Supported.
* NP10679, "a series of GluN2B-selective negative allosteric modulators with enhanced potency at acidic pH ... designed for ischaemic penumbra and high-frequency synapses; oral bioavailability and brain penetration in mouse (PMID 34493631)": abstract: "a new series of ... subunit 2B-selective inhibitors that shows enhanced inhibition at extracellular acidic pH values relative to physiologic pH. This property should render these compounds more effective ... at synapses responding to a high frequency of action potentials ... acidification of penumbral regions ... should also enhance selective drug action". Two phrases are stronger: "designed for" (the abstract says "should render"; design intent is not stated) and "in mouse" (the abstract says "preclinical studies", the species appears only in the MeSH terms). Supported otherwise; phase 1 in healthy volunteers (PMID 36642931): supported ("first-in-human ... healthy volunteers").
* "So the pH dependence is a designed property of this series, **not shown for ifenprodil-site modulators in general**": an absence claim that the three abstracts cannot support (they say nothing about other modulators). Correction: "the abstracts report the pH dependence for this series; they do not address other ifenprodil-site modulators". My recollection, not verified here, is that proton sensitivity of ifenprodil-site inhibition has been described in the older literature; the science session should check it before this sentence is kept.
* Two row-level inaccuracies: the engine verdict for NP10679 is "CANDIDATE (assay text present)" in the note, but `search_rows.tsv` shows `unknown_fields: receptor_site` for NP10679 (and `receptor_site,assay_text` for onfasprodil); the note says "raw DGIdb lookups under the spelling NP-10679" are in "the same table": `relations_qa.tsv` has no NP-10679 line; the only such lookup is in `gse156243/kg_lookup/GRIN2A.txt` (a GRIN2A listing, not GRIN2B).

---

## C6. Transfer, negatives, double counting: PARTLY

Transfers without saying so:
1. `provenance_it42.md`: the NP-10679 DGIdb lookup is a GRIN2A listing in another folder, presented as part of the IT15 GRIN2B table (see C5).
2. `eval_summary.md`: the Q1 "clean" S-deschloroketamine is a ketamine derivative whose site is not in the record (C2 point i); no value is transferred, but a class is, silently, in the opposite direction from how ketamine itself was excluded.
3. DQP-1105 (C1): handled correctly (the GluN2C value is kept out of GluN2B); no transfer found in `trace_it42.md` Case 3.

"Not found" read as "absent":
4. `eval_protocol_it42.md` Q4 "a case where the wanted action has no record" is written before the search and scoped to the two sources only in `trace_it42.md` ("the table holds only inhibitors"). Add the scope "in ChEMBL curated mechanisms and GtoPdb 2026.3.1; DGIdb claims not read" (C4).
5. `eval_summary.md` "A1 returns every row a careful analyst would start from" (protocol, "Paths") is not supported: DGIdb interaction claims in the catalogue for the S7 genes (SLC6A1 30, ABAT 25) and S6 genes (SLC12A2 5, SLC12A5 4) are never read by either path.
6. Q4 A0 = 0 is a ChEMBL curation fact (bumetanide and furosemide are curated against SLC12A1), not a statement that NKCC1 inhibitors are unrecorded.

One datum counted as several (see C2): radiolabelled forms (S1 8, S5 10, S7 1, S8 5 labelled ligands), cross-source same-name molecules (S1 2, S2 1, S3 1, S5 13, S7 2, S8 2: amantadine, ketamine, ivabradine, flindokalner, tiagabine, vigabatrin, talampanel, tezampanel and others), stereoisomer pairs. Cause: no GtoPdb-to-catalogue join exists (0 of 471 GtoPdb rows have a `catalogue_id`), so the protocol's "cross-source merging by catalogue parent" and E4 definition were not implemented. In `eval_summary.md` the reported "clean units 4 -> 7, 2 -> 18, 68 -> 101, 0 -> 4, 2 -> 15" and `README.md` carry this overcount (Q1 7 clean is unaffected; Q3 101 and Q5 15 are not).

"Unknowns kept" (`eval_summary.md`: "Unknowns kept with a reason: 1 in Q1"): under the protocol's own definition (a unit whose criterion cannot be evaluated is preserved only if listed as UNKNOWN), 3 further Q1 units (onfasprodil, S-deschloroketamine, NP10679, receptor site missing), 10 of 12 S2 units, 14 of 18 S3 units and 7 S5 units (direction missing) are counted as "clean" with only a reason string; the claim "Clean units lost: 0, unknowns preserved" holds for the engine's column `unknown_fields` but not as the protocol defines preservation (F1).

Not found: no value moved across species or subunits in V11, V12 or `trace_it42.md`; the E2730 two rows (uptake pIC50 5.96, binding pKd 6.15) are different measurements and counted as one unit, which is right.

---

## Exact corrections, in order of consequence

1. `action_search.py` `qualify()`: UNKNOWN for missing direction (and missing receptor site where the policy is not `any`); no `assay_text` flag when `subunit_out` is empty; re-run, re-score, regenerate `search_rows.tsv` consumers.
2. Build the GtoPdb-to-catalogue join (ligands.csv ChEMBL ID and InChIKey), merge radiolabelled forms to the cold ligand, and re-run `eval_it42.py`; expected Q1 A1 53 units/E2 44/unflagged 46/excluded 45, Q5 12 units, Q3 about 102 and 82 (estimate). Fix `eval_summary.md`, `eval_table.md` (stale), `README.md`.
3. `compound_view.tsv`: V12 registry_note ("vigabatrin: irreversible inhibition; CPP-115: inhibition"; 4-acryloylphenol primary target ALDH5A1, ABAT is non-primary, pIC50 5.26); V11 counter ("one of two children; 3 null reports").
4. `provenance_it42.md` and `README.md`: 27475601 is the ChEMBL `activity_id`; drop "designed for", "in mouse" and "not shown for ifenprodil-site modulators in general"; correct the NP10679 verdict (unknown_fields: receptor_site); correct the location of the NP-10679 DGIdb lookup (GRIN2A); name the patent source of the onfasprodil GtoPdb row.
5. Add the sampling script and the sample for the missing stratum (ChEMBL direction_opposite; I covered all 76 rows) and for the direction-unknown rows.

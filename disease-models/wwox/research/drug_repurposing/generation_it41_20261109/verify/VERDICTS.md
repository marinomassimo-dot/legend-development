# IT41 independent verification: verdicts

Non-canonical verification note. Not medical advice; no dose, schedule or route. Dispatched as a delegate on model sonnet, effort high. No agents started. Written only in this folder.

Originals opened: the GtoPdb interactions CSV (version line "GtoPdb Version: 2026.3.1 - published: 2026-10-12", 24,968 data rows; read from the root checkout copy because the worktree has no cache folder; SHA-256 of that file begins cdbd18c6), the GtoPdb ligands CSV, the compound catalogue through `framework/scripts/compound_catalog.py` (44,211 entries), `nmda_composition_discrim_20261109/output/decisive.tsv`, `evidence.tsv`, `comparison.tsv`, `ampa_nmda_discrim_20261108/output/` (observations, hypotheses, probes), `membrane_hypotheses_20261108/output/hypotheses.tsv`, the identity table and README on Harness's folder, and the two PubMed records. Paths below are relative to `disease-models/wwox/research/drug_repurposing/` unless full. "search_rows" means `generation_it41_20261109/search_rows.tsv` (line numbers include the header).

Method note: the claims were recounted from the CSV, not from the producer's TSV; the TSV was then compared with the CSV. Sample of simple non-decisive controls, declared: all 39 GtoPdb rows under GRIN2B (full, not sampled), all 6 S6 rows, all S5 action/direction combinations (671 rows by group), 8 catalogue entries for the max-phase statement.

## Summary table

| Claim | Verdict |
|---|---|
| C1 recount of S1 GtoPdb rows (27 / 7 / 3 / 1) | PARTLY |
| C2 DQP-1105 row, "transfer avoided" | PARTLY (the description of what the producer did is fair; the statement that the value is a GluN2C measurement is NOT SUPPORTED) |
| C3 onfasprodil and NP10679 statements | PARTLY (one factual error: "pIC50 8.08 and 8.30") |
| C4 labels | PARTLY |
| C5 V01 to V10 | PARTLY (V05 label and the 0.88 bound in the comparison file are stronger than the sources; others minor) |
| C6 second family | PARTLY (the counts hold; the direction rule has a defect that understates the opposite-direction rows; no narrative text exists to test the sentence against) |
| C7 transfer, absence, double counting | PARTLY (three findings) |

---

## C1. Recount of the GtoPdb rows under GluN2B: PARTLY

**What I recounted from the CSV** (rows whose Target Gene Symbol is GRIN2B or Grin2b): 39 rows, 38 human and 1 rat. By Type/Action: Agonist 9 (5 plain, 3 full, 1 partial; glutamate or glycine site), Antagonist 19 (18 with a receptor-site entry glutamate or glycine, 1 without site), Channel blocker 7, Allosteric modulator/Negative 2 (DQP-1105, onfasprodil), None/Inhibition 1 (NP10679), Allosteric modulator/Positive 1 (SAGE-718).

* Orthosteric (glutamate- or glycine-site) rows: 9 + 18 = 27. **Reproduces** `measure_it41.tsv` (27). Channel blockers: 7. **Reproduces** (7). Three rows with negative action and one positive modulator (SAGE-718, search_rows line 41): **reproduces**.
* Search_rows lines 39, 40, 68 are the three negative rows; line 41 the positive modulator.

**Findings that qualify the claim.**

1. **One GtoPdb row fits none of the categories and is not mentioned.** S-deschloroketamine (search_rows line 52): Antagonist/Antagonist, no receptor site, "Binding affinity for hGluN1/hGluN2B receptors expressed in HEK293 cells", pKd 5.44. 27 + 7 + 3 + 1 = 38, plus this row = 39. Correction: add it to the text as "one binding-affinity row of a ketamine analogue, recorded as antagonist without site".
2. **The prose counts do not match the measured counts.** `comparison_S1.md` line 9 says "orthosteric antagonists of the glutamate or glycine site (about 17)" and "channel blockers (about 8: ketamine, amantadine, Mg2+, dizocilpine...)". Measured: 18 antagonists with site, 7 channel blockers (8 only if S-deschloroketamine is added, which the measure does not do). Correction: replace "about 17" by 18 and "about 8" by 7, and state the S-deschloroketamine row separately.
3. **The 27 and the 7 count GtoPdb ligand records, not distinct chemical entities.** Seven of the 27 are radiolabelled forms ([3H]glycine, [3H]CGP39653, [3H]CGP61594, [3H]CGS19755, [3H]CPP, [3H]L689560, [3H]MDL105519) and one of the 7 is [3H]dizocilpine. In the ligands CSV, [3H]glycine has the same PubChem CID as glycine (750), [3H]L689560 the same as L689560 (121918), [3H]CGS19755 is the labelled racemate of selfotel (synonym CGS-19755), and [3H]dizocilpine carries the synonym [3H]MK-801. So at least 3 of the 27 and 1 of the 7 are a second record of a compound that is also counted. Correction: write "27 ligand records (24 distinct compounds after merging labelled and unlabelled forms)" and "7 records (6 compounds)".
4. **The "63 molecules" in `measure_it41.tsv` and `comparison_S1.md` is 24 ChEMBL parent molecules + 39 GtoPdb ligand records with no cross-source merge.** ChEMBL "KETAMINE HYDROCHLORIDE" and "AMANTADINE HYDROCHLORIDE" are also GtoPdb "ketamine" and "amantadine" (search_rows S1). With the four radiolabel pairs the distinct-compound figure is about 57 (my estimate, not a registry count). The text also says "63 molecule x relation rows" while the file has 67 S1 rows; 63 is molecules, 67 is rows.
5. **"Three negative-modulator rows" is a producer reading, not a registry statement, for NP10679.** In the CSV, NP10679 has Type "None", Action "Inhibition" (no allosteric entry, no negative). The NAM wording comes from the abstract. `measure_it41.py` counts it through the pattern `None/Inhibition`. Correction for the measure row "additional documented negative modulators from the GtoPdb table (same species context stated)": the value 3 includes DQP-1105, which is rat and whose assay text names another subunit (see C2), so the GluN2B-directed human rows are 2, one of them (NP10679) typed "None/Inhibition". "Same species context stated" is not true for the DQP-1105 row (rat target, human for the others).
6. **The measure row "molecules documented as GluN2B-directed negative modulators (two-gene assembly record) = 4" is mislabelled.** In search_rows the ChEMBL action for those records (radiprodil, traxoprodil, rislenemdaz, EVT-101) is ANTAGONIST with the text "GRIN1/GRIN2B antagonist"; the producer's own text elsewhere says the assembly record "is not a selectivity measurement". Correction: "four molecules whose curated mechanism is an antagonist on the two-gene GRIN1/GRIN2B record".

---

## C2. DQP-1105 row: PARTLY

**Confirmed in the CSV.** Target GluN2B, Target Gene Symbol Grin2b, species Rat, Ligand DQP-1105, Type "Allosteric modulator", Action "Negative", Affinity Median 6.95 pIC50 (original IC50 113 nM), Primary Target "false", Assay Description: "Measured using recombinant GluN1-1a NMDA subunits co-expressed with GluN2C subunits." (search_rows line 39, `assay_or_note`).

**What decides.** The same ligand has two sibling rows with the same PubMed ID and the same ligand: a **GluN2C row** (pIC50 8.15, IC50 7.0 nM, Primary Target true, assay text "...co-expressed with GluN2C subunits") and a **GluN2D row** (pIC50 5.57, IC50 2700 nM, assay text "...co-expressed with GluN2D subunits"). So each registry row carries its own number and the GluN2D row names GluN2D, but the GluN2B row's value (6.95) is a third, different number under a text that names GluN2C. Two readings fit: (a) the text on the GluN2B row is a copy of the GluN2C annotation and the 6.95 is a GluN2B value; (b) the 6.95 was measured on the GluN2C assay. The value 6.95 differs from the GluN2C row's 8.15, which makes (b) hard to hold as stated, because the GluN2C assay already has its own row. I cannot decide between them from the originals I am allowed to open (the primary paper would decide it; I did not open it).

* "Transfer avoided" as a description of what the producer did (no GluN2B statement drawn from the row): **fair**.
* `comparison_S1.md`, DQP-1105 table row: "the value was measured on GluN2C; the row sits under GluN2B in the table". **NOT SUPPORTED as written**: the registry text says GluN2C, but the value is not the GluN2C row's value. `compound_view.tsv` V09 `open_premise`: "The registry row's assay was on another subunit; the value is not a GluN2B measurement." **Stronger than the source**.
* `measure_it41.tsv` last-but-three row, "rows whose assay was on another subunit than the target they sit under (transfer avoided) = 1": produced by the string test `"GluN2C" in assay_or_note`, so it counts the registry text, not the assay.

**Exact corrections.** V09 `open_premise`: "The registry row's assay text names GluN2C, but the same ligand has its own GluN2C row with a different value; which subunit the 6.95 belongs to is unresolved without the primary paper." `comparison_S1.md` row: replace "the value was measured on GluN2C" by "the assay text names GluN2C; the value is not the GluN2C row's value; unresolved". Verdict on the V09 kind "weakened": keep (the conclusion, no GluN2B statement drawn, is unchanged).

---

## C3. Onfasprodil and NP10679: PARTLY

**Onfasprodil, registry.** CSV row (search_rows line 40): human GRIN2B, Type Allosteric modulator, Action Negative, Selectivity "Not Determined", Affinity Median 8.08 pIC50, Original Affinity Median nm 8.3 (relation "="), no assay description, no receptor site, no PubMed ID; the only source field is a patent (Patent Numbers and Webpage URLs; patent number begins US1023).

* **ERROR: "pIC50 8.08 and 8.30 as given"** (`compound_view.tsv` V06 `registry_note`; `comparison_S1.md` onfasprodil row). There is one row and one value. 8.30 is the original **IC50 in nM** (8.3 nM), which converts to pIC50 8.08 (9 - log10 8.3 = 8.08). There is no second pIC50 of 8.30 in the 2026.3.1 CSV. The sentence presents one datum as two values. Correction: "one row: pIC50 8.08 (original IC50 8.3 nM), selectivity not determined, no assay text or receptor site; the only source given is a patent".
* The patent-only provenance is a weakest link the text does not name. Add it to V06 `registry_note`.

**Onfasprodil, abstract** (PubMed record, DOI [10.4088/JCP.23m15246](https://doi.org/10.4088/JCP.23m15246), checked via the PubMed tool): "highly potent and novel selective NR2B subunit negative allosteric modulator"; phase 2, randomized, placebo-controlled; adults with treatment-resistant major depression; 40-minute intravenous infusion; commonest adverse events dizziness (14.3%), transient amnesia (14.3%), somnolence (11.4%). Producer's wording ("phase 2 in adults with treatment-resistant depression", "selective NR2B negative allosteric modulator", the three adverse events) **supported**. The abstract also includes a ketamine arm and efficacy results that the text does not use (not an error). "Human exposure" in V06 rationale: supported by the abstract.

**NP10679, registry.** CSV row (search_rows line 68): human GRIN2B, Type "None", Action "Inhibition", pIC50 7.64 (original IC50 23 nM), assay text "Inhibition of hGluN2B in the presence of glutamate and glycine, measured using two-electrode voltage-clamp recordings in Xenopus oocytes expressing hGluN2B, at pH 6.9." **Supported** (7.64, oocytes, pH 6.9). Note: the registry value exists only at pH 6.9; "more potent at acidic pH" rests on the abstract, which the text correctly says.

**NP10679, abstract** (DOI [10.1002/cpdd.1217](https://doi.org/10.1002/cpdd.1217)): "context-dependent and subunit-selective negative allosteric modulator"; "a more potent inhibitor of GluN2B-containing NMDA receptors at the acidic levels of extracellular pH (eg, 6.9) ... than at physiological pH"; first-in-human phase 1, healthy volunteers. **Supported.** V07 "Inhibition of GluN2B-containing receptors, stronger at acidic pH" and "Phase 1 in healthy volunteers only (abstract)": supported. V07 rationale "It shows that GluN2B-directed potency can depend on the bath pH": true for this compound only; the `open_premise` already says the general case is open, so acceptable.

**Unreported registry conflict.** In the GtoPdb ligands CSV, NP10679 has Approved = yes (and "Approved" true in the interactions CSV). ChEMBL_37 in the catalogue gives max phase 1 (CAT:CHEMBL5095254), and the abstract is a phase 1 report. No IT41 text repeats the approved flag, so nothing is wrong in the package, but the flag is a registry error or a different meaning and should be written in V07 `registry_note` so nobody imports it: "GtoPdb flags this ligand approved; ChEMBL_37 and the abstract say phase 1; not used."

---

## C4. Labels: PARTLY

Method: `git grep -il -F` of each name over `disease-models` and `framework`, excluding `*/view/*`, `*catalog.jsonl*`, `*/cache/*` and the IT41 folder itself.

| Name | Files found | Label in text | Verdict |
|---|---|---|---|
| radiprodil | many (cards F04, IT39 comparators, IT40 packages, receipts) | known reference | supported |
| traxoprodil, rislenemdaz, EVT-101 | many (coverage matrix, priorities, rankings, IT20 comparison arms, IT40 mechsearch) | known reference, "no new reading" | supported |
| ifenprodil, Ro 25-6981 | many | known reference | supported |
| onfasprodil | `coverage/coverage_matrix.json` (two DGIdb-only family entries), `gse156243/kg_lookup/GRIN2A.txt` and `raw_GRIN2A/dgidb_batch_0.json` (raw lookup), **`target_first_it15_qa_nmdar_20261101/relations_qa.tsv` (three rows: a GtoPdb row, a ChEMBL activity row IC50 8.3 nM on GRIN1/GRIN2B, a DGIdb row)** | "new combination (the molecule sits in the repository's coverage matrix only...)" | label acceptable, **reason wrong** |
| NP10679 | `relations_qa.tsv` (one GtoPdb row); spelling NP-10679 in the two `gse156243` lookup files | "new for LEGEND (one repository mention)" | label acceptable, **count wrong** |
| DQP-1105, MIJ821 | no file | not labelled new; kind "weakened" | acceptable |

**Changes I would make.**

1. Onfasprodil: the "coverage matrix only" is false. The IT15 QA relations table already holds the onfasprodil-GRIN2B relation (GtoPdb and ChEMBL activity rows). Keep "new combination" but write: "appears only in the coverage matrix, a QA relations table (GtoPdb, ChEMBL activity and DGIdb rows for GRIN2B) and raw lookup outputs; never discussed as a comparator".
2. NP10679: replace "one repository mention" by "one table row under the spelling NP10679 and two raw lookup files under NP-10679; no discussion". "New for LEGEND" stays, under the producer's own definition (absent from the discussion). Side note found while grepping: the same `relations_qa.tsv` row records NP10679 with a value of 22.9 under "pIC50"; that is the IC50 in nM (23 nM) mislabelled in an older file. It is not an IT41 error but any reuse of that row would carry a wrong pIC50.
3. Both labels use "repository" for what is a name grep; the file count is not a reading (the text already says so for the ChEMBL assembly molecules; say it here too).

---

## C5. Items V01 to V10: PARTLY

Per item: statement, source, finding.

**V01 (d-APV, control).** Sources: `ampa_nmda_discrim_20261108/output/observations.tsv` OB04, OB09, hypotheses BH1.
* "It abolishes the spontaneous bursts, so it fixes how much NMDA-receptor current must go before the burst stops" (`rationale`). OB04: one concentration (50 uM), one effect size, 51 bursts, 5 slices, 3 animals, "no vehicle or time-matched control group", "no titration", washout "loose". Abolition at 50 uM **bounds** the requirement (a full block removes the burst); it does **not fix** how much current must go, which is exactly what V01's own `next_test` says is unmeasured. **Stronger than source.** Correction: "bounds, from above, how much must go".
* Label "Full competitive NMDA-receptor block": "full" is not measured in the slice (no isolated NMDA-receptor current was recorded under it). Correction: "Competitive block of the glutamate site at 50 uM (extent in the slice not measured)".
* `counter` "about 20 percent of the delayed evoked response remains ... not evidence of incomplete block": OB09 reads this from a figure (INFERENZA, precision 10 to 15 percent) and states that the d-APV concentration for that panel is not given. Source says "cannot be read as an incomplete block"; V01 drops the figure-read qualifier and the missing concentration. Add both.
* "(stored in the catalogue as D-Ap5)": the catalogue entry is a DGIdb record `CAT:DGIDB:b0ca5cf2303c`; Harness's README says no identity declaration was written because the spelling equivalence "was not re-read in a registry". The GtoPdb ligand 4168 (d-AP5) lists the synonym D-aminophosphonovaleric acid, which supports the equivalence; cite that, or say "equivalence of name assumed".

**V02 (ifenprodil; Ro 25-6981).** Sources: decisive.tsv D01 to D03, D05, D09, D11; identity table.
* "Ifenprodil-site ... negative modulator" for both names: for ifenprodil, D11 (Hansen, read). For **Ro 25-6981 the site is "carried from literature not read"** (D11) and its primary full text was not reached (D05, abstract only). V02 and `comparisons_it41.md` ("Known reference ... ifenprodil or Ro 25-6981 ... Primary values exist (maximum 88 percent ..., 32 percent ...)") apply the ifenprodil and CP-101,606 maxima to Ro 25-6981 without saying so. `comparison.tsv` calls this "transferred ... (INFERENZA)". Correction: write "Ro 25-6981: site and triheteromer behaviour carried from ifenprodil, not read".
* "The removable share of such a modulator is bounded by receptor composition and zinc": D09 is arithmetic INFERENZA from recombinant rat cDNA oocyte maxima, assuming additive shares and equal occupancy, and says it "does not validate" the envelope. V02 states it as a fact. Add "INFERENZA (D09)". 
* **The numeric bound in `comparisons_it41.md` ("at most 0.88 times the GluN2B diheteromer share plus 0.32 times the triheteromer share") is contradicted inside the package.** 0.88 is ifenprodil's fitted maximum (D01). Radiprodil's maximum on human GluN1-1a/GluN2B is 91 +/- 1 percent (D10, and V05), above 0.88. So the number is a bound for ifenprodil (and CP-101,606 for the triheteromer term), not for "a modulator". D09 itself says "it cannot exceed 88 percent" for "a GluN2B NAM", which is also too strong in view of D10. Correction: "for ifenprodil, at most ...; other compounds have their own maxima (radiprodil human 91 percent)".
* "The compound's GluN2B rows are measured activities, not a curated mechanism, and other targets are also measured; selectivity is not assessed": **supported** by the identity table (ifenprodil GRIN2B measured, 36 rows, SIGMAR1 20, TMEM97 12, EBP 6; Ro 25-6981 20 rows; selectivity NOT_ASSESSED) and by the README (GtoPdb ifenprodil has no interaction rows, which I confirmed: no interaction row for ifenprodil, Ro 25-6981, traxoprodil, radiprodil or rislenemdaz exists in the CSV).

**V03 (AMPA/kainate arm).** Sources: BH1, identity README.
* "Two GYKI compounds are registered under one label (different structures)": README says the label GYKI53784 sits on two structures across registries, and "a conflict between registries, not a ruling on the compound". **Supported**, but add "registry conflict, not a ruling".
* "Survival of the burst under a verified block would remove an AMPA contribution": BH1 (5) "if bursts survive a verified AMPA block, that question is dropped for this preparation". Supported (IPOTESI in source; V03 should keep the IPOTESI tag in `rationale`).

**V04 (Ih arm).** Sources: membrane MH1, MH2, E1.
* "A blocker response shows contribution as in normal cortex": MH2 (3) is rat layer 5/6 (ivabradine) and thalamic neurons (ZD7288); V04 does not say species, age or region. "the sodium action of one tool is an off-target": MH2 says abstract level, DRG, Nav1.4. Both are **transfers not named** (see C7).

**V05 (radiprodil).** Sources: D10, probes.tsv, ChEMBL_37 in the catalogue.
* Numbers: rat GluN1/GluN2B 82 percent, rat triheteromer 45 percent, human GluN1/GluN2B 91 percent; washout very slow. **All match D10** (82 +/- 9, n = 16; 45 +/- 10, n = 8; 91 +/- 1, n = 13; 4.7 percent recovery in 3 min). The supplementary-figure caveat matches probes.tsv.
* **Label "species-dependent maximum" (also `comparison_S1.md`: "maximum effect depends on species and receptor assembly") is stronger than the data.** D10 says the like-for-like contrast is rat 82 against rat triheteromer 45 (assembly). The species contrast is 91 +/- 1 (human) against 82 +/- 9 (rat); the difference of 9 points is of the size of the larger spread and no test is given. Correction: "assembly-dependent maximum (rat 82 against 45); a species difference (human 91, rat 82) is not shown".
* "A compound with human exposure": the paper read (D10 source) carries "no human data in the text read" (probes.tsv). Human exposure rests on the catalogue (ChEMBL_37 max phase 2 for CAT:CHEMBL182066, a curated phase, not an agency statement). The listed sources for V05 are D10 and Table 1, which do not support it. Add "catalogue max phase 2" as the source.

**V06 and V07.** See C3. The V06 `registry_note` error (8.30) and the missing patent-only provenance; V07 fine.

**V08 (traxoprodil; rislenemdaz; EVT-101).** Sources: catalogue.
* "none approved": the catalogue gives max phase 2 and status class "clinical_candidate", access "experimental", with the scope text "no approval statement in any source used" (traxoprodil mesylate: max phase -1, unknown). "None approved" is an absence claim without perimeter. Correction: "no approval statement in the catalogue (ChEMBL_37 max phase 2; the mesylate record has phase unknown)".
* "No maximum effect, species or assay context in the catalogue": the ChEMBL mechanism records carry a target organism (Homo sapiens). Correction: "no assay species".
* "Registry ... max phase 2 or lower": confirmed for the four IDs I opened (2, 2, 2, 2; mesylate -1).

**V09.** See C2: `open_premise` stronger than source.

**V10 (Kv7; carbenoxolone).** Sources: MH1, BH3, OB16.
* "the burst fall under the gap-junction tool has no supporting datum for coupling": BH3 (4) "cannot be assigned to gap junctions". Supported.
* `counter` "Smaller cells with a seal leak and effects on synaptic currents explain the same observations": MH1 says smaller cells plus a fixed seal leak "would give" the observed pattern (hypothesis A10, "a second cause" needed for the depolarised rest) and the carbenoxolone synaptic-current effects are from autaptic mouse hippocampal culture and rat CA1 slices (BH3 (3)). "Explain" is stronger than "could explain", and the preparations are not named (see C7). Correction: "could account for ... (hypothesis; carbenoxolone effects on synaptic currents are from hippocampal culture and CA1 slices, not from this preparation)".

---

## C6. Second family (S5, S6): PARTLY

**Recount from search_rows.** S6: 6 rows, all GtoPdb, all "Inhibitor/Inhibition", direction down. SLC12A2: bumetanide, furosemide, piretanide, IAMA-6 (4 rows, these are the wanted NKCC1 block). SLC12A5: DIOA (no value), VU0240551 (pIC50 6.25) (2 rows). **Confirmed against the CSV: the only SLC12A5 interaction rows are those two inhibitors; there is no activator or positive row for SLC12A2 or SLC12A5.** The ChEMBL path returned no mechanism row for either gene. S5: 671 rows (488 ChEMBL, 183 GtoPdb); direction up 584, down 70, unclear 17. **The 70 down rows reproduce** (ChEMBL allosteric antagonist 7, antagonist 7, inverse agonist 7; GtoPdb allosteric antagonist 12, inhibition 4, negative 3, antagonist 12, channel blocker 18).

**Defect found: the 70 understates the rows that are not positive modulation.** `action_search.py` line 42 assigns "up" when the action text contains "agonist", testing that after "down" words. GtoPdb "Inverse agonist" contains "agonist" and none of the down words, so **34 GtoPdb inverse-agonist rows (11 compounds, for example DMCM, Ro15-4513, MRK016, alpha5IA, L655708) are tagged "up"**, while the 7 ChEMBL "INVERSE AGONIST" rows are tagged "down". The same action is classed both ways. So in S5, rows that are not positive modulation by action are 70 + 34 = 104, not 70, and the "up" figure of 584 falls to 550 (plus 17 unclear). This affects `search_rows.tsv` and the `directions` column of `molecules.tsv` for S5; no other relation has inverse-agonist rows (checked all six). Correction: test "inverse" first and map it to down; regenerate S5; restate "104 rows".

**The sentence "absence in the table is not absence of action".** It appears as "an absent row is not an absent action" in the docstring of `action_search.py` and in `cases.md` ("novelty ... needs a separate check"). **No narrative text reports the S5 or S6 results**: `relations_it41.tsv` rows S5, S6 say "searched in P11 to test reuse"; there is no file stating the S6 finding. So the sentence is respected in the sense that nothing converts the empty result into "no KCC2 enhancer exists", but the finding itself is not written anywhere a reader will see it. If a sentence about S6 is added, it must be scoped: "the GtoPdb 2026.3.1 interaction table and the ChEMBL curated mechanisms in the catalogue hold no KCC2 enhancer; the two SLC12A5 rows are inhibitors; the DGIdb rows in the catalogue for the same five compounds (DIOA, VU0240551, bumetanide, furosemide, piretanide) carry no action type and were not read in this search". That last point is a source the search did not use (DGIdb is named in `cases.md` as part of the universe for Case 1, and is not read by `action_search.py` for any relation).

---

## C7. Transfer, "not found" to "absent", multiple counting: PARTLY

**Transfers not stated (each fixable by a clause).**
1. `comparisons_it41.md` table, "Known reference": "ifenprodil or Ro 25-6981 ... Primary values exist (maximum 88 percent ..., 32 percent ..., 50 percent with 300 nM Zn2+...)". These are ifenprodil values (rat cDNA, oocytes, -40 mV; D01 to D03). Ro 25-6981 has abstract values only (D05). Species and preparation (rat cDNA, Xenopus oocytes) are also omitted. Add both.
2. V02 and the plateau rule: composition bound taken from recombinant ifenprodil and CP-101,606 maxima and applied to "a modulator" (see C5, contradicted by radiprodil 91 percent).
3. V04: HCN blocker effects (rat layer 5/6, thalamic neurons) and the sodium off-target (DRG, abstract level) are stated without species or tissue.
4. V10: carbenoxolone synaptic-current effects from mouse hippocampal culture and rat CA1, applied to the neocortical Wwox slice as "explain the same observations".
5. V05 and `comparison_S1.md`: "species" dependence (C5).
6. `comparison_S1.md` line 9: "They are neither subunit-directed nor negative allosteric modulators at the ifenprodil site." The glutamate site and the glycine site lie on GluN2 and GluN1 subunits respectively; what the registry shows is that the rows are filed under every GluN subunit entry ([3H]CGS19755 appears under GRIN1, GRIN2A, GRIN2B, GRIN2C, GRIN2D). Correction: "not shown to be GluN2B-selective, and not ifenprodil-site modulators".

**"Not found / not read" turned into "absent".**
1. V09 (C2): text names GluN2C, producer concludes "not a GluN2B measurement".
2. V08 "none approved" (C5): unscoped.
3. `comparison_S1.md`: "Ifenprodil and Ro 25-6981 do not appear among the GluN2B interactions of either structured source in this snapshot". True for the ChEMBL curated mechanism table and for GtoPdb interactions (confirmed, no row for ifenprodil at all). But ChEMBL measured activity, a structured source, holds 36 ifenprodil and 20 Ro 25-6981 GRIN2B rows (identity table, live read). Correction: "among the ChEMBL curated mechanisms and the GtoPdb interactions of the snapshot; ChEMBL measured-activity rows exist (identity_it41)".
4. S6: see C6 (DGIdb unread; scoped wording needed). 
Other absence statements checked and fine: V06 "the registry gives no receptor site" (CSV: blank), V08 "no maximum effect ... in the catalogue" (scoped), the S1 "(Harness reports measured-activity rows elsewhere)".

**One datum counted as several.**
1. Onfasprodil "pIC50 8.08 and 8.30" (C3): one value and its own IC50.
2. Radioligand pairs and cross-source duplicates inflate 27, 7 and 63 (C1).
3. Three negative-modulator rows (C1): the same count mixes one unusable row (DQP-1105) and one row typed "None/Inhibition".
4. `measure_it41.py` hard-codes the value 2 for "compounds that entered the comparison as emerged" instead of computing it from `compound_view.tsv`; the value agrees today (V06, V07) but would not follow a change.

---

## Corrections list, in order of effect on a decision

1. Remove "8.30" as a pIC50 for onfasprodil (V06 `registry_note`, `comparison_S1.md`); add patent-only provenance.
2. Reword V09 and the `comparison_S1.md` DQP-1105 row: the value is unresolved, not "measured on GluN2C" and not "not a GluN2B measurement".
3. Remove the numeric 0.88 bound as a class bound (`comparisons_it41.md`; keep for ifenprodil) and the transfer of ifenprodil values to Ro 25-6981.
4. Change "species-dependent maximum" to "assembly-dependent maximum" (V05, `comparison_S1.md`) and give the catalogue max phase as the source of "human exposure".
5. Fix the S5 direction rule (inverse agonist to down), regenerate, restate 104.
6. Merge radiolabelled and cross-source duplicates in 27, 7 and 63, and relabel the four assembly-record antagonists (they are not "negative modulators" by the registry's own action).
7. Scope "none approved", the ifenprodil/Ro 25-6981 absence sentence, and the "neither subunit-directed" sentence.
8. V01 "fixes" to "bounds"; add the figure-read qualifier to the 20 percent residual.
9. Record the NP10679 "approved" flag conflict in V07 `registry_note`.

# ADV-006 blind audit (verifier V, sonnet, effort high)

Non-canonical. Not medical advice; no ranking, no recommendation, no dose, no wet work commissioned or urgent. Paths are relative to `disease-models/wwox/research/drug_repurposing/` unless they start with `disease-models/wwox/research/commit_candidates/`. Stage A files (`stageA_own_reading.tsv`, `stageA_pairs.md`) were written before any `output/` file was opened. Labels: measured (a test I ran), copied (verbatim from a source), my inference.

## Answer first: the counts
* **Quotes checked: 176; wrong: 0** (105 `crosswalk.tsv` verbatim parts + 48 `conflicts.tsv` quotes, tested in file, row and column by my own script, `v_quote_check.py`; plus 23 `measurement_quotes.tsv` quotes, `v_mq_check.py`). One quote is verbatim but selective (CF07 A).
* **Groups: 14 compared with my own groups; agreed 11, disputed 3** (burst-status item (vii) placed under the sIPSC measurement; the matched non-GABAergic arm merged although its matching variable differs; the pH measurement missing IT45-Q05). Two `requests_merged` lists are wider than one session (M01, M05).
* **Conflicts: 9 genuine claimed; agreed 5** (CF01, CF03, CF04, CF05a, CF05b; CF04 and CF05a cross the August design's preparation), **disputed 4** (CF06, CF07, CF09, CF15: a different preparation, a cell class that the cited design also contains, an interpretive standard, a prediction versus a lever status). **Missed: 1** (matching variable of the non-GABAergic arm). 15 gap/synonym rows: the 9 I examined agree.
* **Rows closed: 13; agreed 10, disputed 3** (WO-15 and IT46-Q10 counted "partly" while the producer's own `basis` cells say "fully" under a stated reading; WO-16 "fully" holds for "in one system", not for cross-laboratory reproduction). Single-preparation count 4 fully + 3 partly depends on that reading (6 fully on the producer's own basis cells). Its "not decided" list (subtype, pH, heterologous series, drug arms, OPC, other ages) is correct.
* **Field-mapping errors: 0** (42 rows: every source column exists in the real header; every target is in `DESIGN_FIELDS`); 1 over-general sentence (the reader "opens only" three file names holds for the `design_only` role).
* **Missed requests: 1** (IT45-Q05, the same slice-pH measurement as glun2b M01). No request outside the thread was included except as labelled `outside_thread`.
* **Overstated sentences / cells: 22 verdict rows** (full list in `verdicts.tsv`): chiefly "103 requests" (20 are pointer rows), "9 genuine conflicts", "same recording" at cell level, two order entries, the closes count, and a stale `build_scripts/` sentence.
* **Priors G1-G6 (producer / mine):** G1 partly / partly; G2 held / held; G3 partly / partly; G4 held / **partly**; G5 held / held; G6 partly / partly.
* **Verdict totals** (`verdicts.tsv`, 72 rows): correct 46, overstated 22, missed 4, wrong 0, unverifiable 0.

My own Stage A gap, stated: I searched the repository for the August "EGABA" candidates by name and missed `disease-models/wwox/research/commit_candidates/CC-20260826-CLAIM002-01.md` section 6 ("Smallest decisive experiment": gramicidin-perforated-patch E_GABA in layer II/III pyramidal neurons, S-KO vs S-CTL, P13-P17, n >= 10 cells from >= 5 animals, animal as unit, primary outcomes E_GABA and E_GABA minus V_rest). The producer found it; I checked it and it is real (copied above; my `stageA_pairs.md` is left unedited). Everything else in the repository answer of Stage A (prior full specification of part of the thread in August, no consolidation of SCI42/SCI47) was confirmed.

## 1. Verbatim cells
| Test | Items | Result |
|---|---|---|
| crosswalk `request_verbatim` (split on " || ") in named file, row, column (TSV) or file (md) | 105 parts | 105 found; 0 wrong row, 0 wrong column |
| conflicts quote_A / quote_B in named source, row and column | 48 | 48 found |
| measurement_quotes.tsv | 23 | 23 found |
| Selective quote that changes the picture | 1 | CF07 A: "CA3 pyramidal neurons" is verbatim, but the same CELL_TYPE list reads (copied) "Layer 2/3 pyramidal neurons, dorsal cortex — secondary", so the cell-class conflict is not in the source |
| Cosmetic | 2 | md locators "around line 738 / 725" (actual 733 / 725) |
Method: whitespace-normalised substring, my script `verify/v_quote_check.py`, results `verify/v_quote_check_results.tsv`. The CF04 B quote keeps a line-wrap artefact ("gabazine- reversible"), found in the file after normalisation. No truncation changes a meaning except the CF07 selectivity.

## 2. Same-measurement groups
| My group (Stage A) | Producer measurement | Agree? | Deciding cells |
|---|---|---|---|
| A E_GABA perforated | M05 | yes | SCI42 M01 measurement; SCI47 Phase 0 (v); IT42-Q02; IT46-Q01; CLAIM002 s6. O14 adds P11 and (v)/IT46-Q01 add input conductance (additive) |
| B sIPSC re-record | M01 | yes (second-arm configuration differs, CF01) | M03 measurement vs Phase 0 (i) |
| C mIPSC | M02 | yes | M04, (ii), NP3P2 |
| D agonist response | M04 | yes | M05, (iv) |
| E evoked IPSC | M03 | yes | M06, (iii) |
| F tonic, G interneurons, H age series, I covariates | M06, M09, M08, M07 | yes | one source row each |
| M heterologous series | M21 | yes | NP3P3, IT53-Q01 |
| A2 August design | M14 | yes (kept apart) | allele, region, windows, agonist, temperature |
| J2 WT slices driven into bursts | M11 | yes | M09 |
| J1 burst versus non-burst KO slices | under M01 (partly) | **no** | (vii) is a slice stratification, not a sIPSC recording; the producer also lists it as in conflict with a glutamate block (CF03) |
| K matched non-GABAergic arm | M15 | **no** (merged without the metric difference) | M10 measurement: "titrated to the same percent of evoked synaptic charge removed"; levers L1 functional_comparator: "matched on the recorded cells' membrane potential and input resistance" |
| L slice pH | M22 | **no** (member missing) | IT45-Q05 question_text_max300 |
Over-wide `requests_merged` (column mixes "same" and "partly" members): M01 lists NP3P2, WO-17, Phase 0 (vii) and the AAV9 rescue item; M05 lists IT46-Q04 and the human-organoid E_GABA item. One session cannot give these without changing a cell (TTX miniatures, an XE991-sensitive current and an isolated NMDAR current, burst classification, a rescue arm, drug arms, another preparation).

## 3. Conflicts
| Producer conflict | Genuine, synonym or gap (mine) | Identical elsewhere? | Note |
|---|---|---|---|
| CF01 low-chloride whole-cell vs perforated sIPSC | genuine (my C1) | yes: Synapsin-Cre, sIPSC, P13-17; the high-chloride arm is common | SCI47 itself uses "physiological-chloride pipette" and "perforated cohort for native-chloride sIPSC" for one item |
| CF03 glutamate block vs burst/non-burst | genuine | yes | a sequence in one slice is not excluded by either source |
| CF05b IT46-Q10 "same cells" vs two cohorts | genuine (my C3) | yes | the map row was not updated with the IT46-Q04 cohort note |
| CF04, CF05a (August design vs SCI47) | genuine in kind | no: the August design is another preparation | counted as agreed with this note |
| CF06 global allele vs Synapsin-Cre | distinct preparations | no | the producer keeps M05 and M14 apart itself |
| CF07 CA3 vs layer II/III | gap | no | the August design contains layer 2/3 as secondary (copied above) |
| CF09 "Interpretable alone at one age." vs WT developmental-shift gate | gap (interpretive standard) | no | both can be recorded together |
| CF15 chloride arm kept vs dropped | gap | no | SCI42 side is `conditional_prediction.tsv` row 6 (a prediction), SCI47 side `levers.tsv` L3 status |
| CF08, CF10, CF12b synonyms; CF02, CF11, CF12, CF13, CF14, CF16 gaps | agree (examined) | n/a | CF17-CF22 not re-derived one by one |
**Missed (my C2, genuine):** SCI42 `new_measurements.tsv` row M10, column `measurement` (copied): "Matched non-GABAergic suppression of bursts titrated to the same percent of evoked synaptic charge removed"; SCI47 `levers.tsv` row L1, column `functional_comparator` (copied): "a submaximal NMDAR block (d-APV) or a hyperpolarising manipulation matched on the recorded cells' membrane potential and input resistance; the endpoint is the burst LFP in the same slices". Same arm, same endpoint, different matching variable. SCI42's own `design_choice_not_finding` cell calls the metric "a design choice", so it is a resolvable conflict. Not in `conflicts.tsv`; M15 `mode_and_configuration` states only the SCI42 metric.

## 4. closes.tsv and the single preparation (re-read against the map question text)
| Row | Producer | Mine | Reason |
|---|---|---|---|
| IT42-Q01 pH | fully (M22) | fully | question "tissue pH of the Wwox-deleted neocortical slice ... differ from physiological?"; glun2b M01 measures it |
| IT42-Q02 | fully | fully | text = SCI42 M01 |
| IT42-Q03 | fully | fully | text = SCI42 M03 |
| IT40-Q03 | partly | partly | potentiation arm only; glutamate currents are another measurement |
| WO-14 | fully | fully | needs HT analysed separately (SCI47 Phase 0 arms; SCI42 M03 does not name genotypes) |
| WO-15 | partly | **fully against the map text** (mIPSC in TTX plus agonist response, matrix O01); partly only against the NP3P2 trigger (same-cell triad) | producer's `basis` cell says so |
| WO-16 | fully | fully for "in one system"; not for cross-laboratory reproduction | ADV-004: selectivity basis-dependent, not shown to reproduce |
| WO-17 | partly | partly | V_rest and sIPSC yes; M-current and isolated NMDAR current no |
| IT46-Q01 | fully | fully | |
| IT46-Q04 | partly | partly (Phase 0 alone closes none) | drug arms |
| IT46-Q10 | partly | fully if two cohorts are accepted; partly for the literal "same cells" | producer's `basis` cell says so |
| IT47-Q04 | none | none | needs identified NG2-cell recordings |
| IT53-Q01 | fully | fully (series asked) | |
Recount: 4 fully + 3 partly of 13 is the conservative count; on the producer's own basis cells it is 6 fully + 1 partly for the single preparation (WO-15 and IT46-Q10 move). WO-14 is typed `data_access_blocked` and WO-16 `monitor` in the map, not `wet_lab_measurement`. "Not decided" list checked: subtype (WO-16, IT53-Q01, ADV-004 README answer 6), pH (IT42-Q01), heterologous series (M21), drug arms, OPC, other ages, primary versus secondary to bursting: all supported by the sources.

## 5. Order
Checked each cited sentence in its file. D1, D3, D4, D5, D6, D7, D9 say what the producer says (D5 copied: "interpretable only after mIPSC, agonist response and E_GABA place the deficit"). Overstated: **D2** ("partly redundant with M05 ... worth keeping only if M05 is done" is a priority/redundancy sentence, not a result of the agonist response conditioning the mIPSC; S0 requires a result-conditioned dependency) and **D8** (the sentence is about the direction of inference, not a temporal dependency). No invented ordering found; the rejected "in order of interpretability" claim is handled correctly (M01's row says "Interpretable alone at one age").

## 6. Field mapping
Run: every `column` of `field_mapping.tsv` exists in the real header of the six source tables (new_measurements, conditional_prediction, explanations, levers, matrix, reopen_searches); every `target_field` is in `DESIGN_FIELDS` (`generation_it40_20261109/conditional_proposals.py` lines 171-173) or marked (key)/(none)/absent. `DESIGN_MAP` today holds two packages (`isrib_discrim_20261108`, `myelin_generative_it36_20261108/levers_bc`); SCI42 chloride and SCI47 are not in `hypothesis_packages.tsv`; the key/id form `package::table::key` matches `hypothesis_package.py` line 543. Error count 0. Over-general: note 1 says the reader opens only `design.tsv`, `grid.tsv`, `experiments.tsv` (line 72); that is the design route, while the `pharmacological_comparison` role reads `new_measurements.tsv` (lines 203-219), so the table list is not the only registration route.

## 7. Coverage
Missed: **IT45-Q05** (interstitial pHo at the recording depth by genotype, same quantity as glun2b M01). Not missed: all SCI42 M01-M10, SCI47 Phase 0 (i)-(vii) and Phase 1, L1-L6, NP3P1-3, IT42-Q01..Q03, IT46-Q01/Q04/Q10, WO-15/17, IT40-Q03, IT47-Q04, IT53-Q01. Correctly outside: IT49-Q10, IT43-Q03, other glun2b rows. Counting issue: 20 of the 103 crosswalk rows are pointer rows (7 `explanations.tsv`, 13 `conditional_prediction.tsv`), so "103 requests" is about 83 requests (about 67 in the thread) by the S0 definition.

## 8. Overstatement (answer.md, sentence by sentence)
| Sentence | Wording the evidence supports |
|---|---|
| "The 103 requests read (87 in the thread, 16 outside it) are 28 distinct measurements" | 103 rows read, of which 20 are pointer rows; 28 measurement rows, of which about 9 are slice recordings (the rest are drug arms, a heterologous series, histology, a re-analysis, rescue and human arms) |
| "carries 9 genuine conflicts that the packages cannot adjudicate" | 3 within one preparation (CF01, CF03, CF05b), 2 more across the August design, 4 gaps or preparation differences, and 1 conflict not listed (matching variable) |
| "sIPSC re-record = SCI42 M03 = SCI47 Phase 0 (i) ..." and "E_GABA = ... O03/O14 ..." | same quantity and core configuration; not cell by cell (second-arm configuration CF01; O14 adds P11, input conductance added in (v), IT46-Q01) |
| "stated only as SCI42's 'if M03 confirms' ..., mIPSC kept only if the agonist response is done" | the mIPSC clause is a keep-only-if-done priority, not a result-conditioned order |
| "4 of 13 rows fully and 3 partly" | 4 fully on the conservative reading; WO-15 and IT46-Q10 are "fully" on the producer's own basis cells; 13 includes 2 non-`wet_lab_measurement` rows |
| `phase_note.md` "Copies of the table generators are in `build_scripts/`" | the folder is not in the tree (commit 7545aa9c4 removed it); tables are not regenerable from the folder |
| "A specification already exists for the E_GABA recording, twice" | supported (CLAIM002 s6 and the EGABA candidates; neither package cites them) |
Statements that hold: "no earlier full specification" for evoked IPSC, agonist response and the glutamate-block re-record (the August design gives sIPSC and mIPSC only after rupture); `suspend` and `fragmentation is correct` correctly not reached; the "not decided" list.

## 9. Priors (S0), my score
G1 partly (agree). G2 held (agree; id collision resolved in the crosswalk). G3 partly (agree). **G4 partly** (producer: held): the three undecided items hold, but the "about four" count is reading-dependent (see 4). G5 held (agree). G6 partly (agree).

## What I could not check
* The producer's `relation` and `why` labels for each of the 103 crosswalk rows: I re-derived the relation for about 40 rows (all SCI42 `new_measurements`, all Phase 0 items, the map rows, NP3P1-3, matrix O01, O06, O12, O14, O18) and agree; the remaining matrix rows (O02-O05, O07-O11, O15-O17) and the 13 conditional-prediction rows were checked for verbatim text only.
* `measurements.tsv` columns for M10, M12, M13, M23-M28 (not read in detail); conflicts CF17-CF22 (not re-derived).
* The SCI47 `inputs_it46/` snapshot, `source_table.tsv`, `answers.md` and the primary paper (34634460): not opened; no external source opened, no receipt staged.
* `quote_check.py` of the producer was not run or read; my test is independent.
* Whether a laboratory could perform any of this: not assessed, no wet work is requested or implied.

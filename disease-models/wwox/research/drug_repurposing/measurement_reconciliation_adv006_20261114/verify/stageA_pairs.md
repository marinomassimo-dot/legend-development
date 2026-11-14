# Stage A pairs (verifier V, written before opening any file of output/ except S0)

Non-canonical, not medical advice, no recommendation. Own reading of the sources named in the brief; groups are in `stageA_own_reading.tsv` (column `your_group`). Locators: file#row id (TSV) or section (md). Labels: copied (verbatim) / my inference.

## Repository answer (asked in the brief)
Does a consolidating specification of the E_GABA / sIPSC / mIPSC recording already exist?
* **A prior specification of part of it exists; a consolidation of these requests does not.** `commit_candidates/CC-20260826-EGABA-EXPERIMENT-01.md` (design), `-ANALYSIS-PLAN-01.md` (primary endpoint DF_GABA at P14-P16) and `-CLOSURE-01.md` (two-axis truth table, null-closure gates) are a full design of gramicidin-perforated E_GABA with a terminal break-in followed by sIPSC and TTX mIPSC in the same cell (copied: "One cell yields both measurements only in this order: perforated first, ruptured second"). They were written on 2026-08-26, before Breton 2021 was in the chain, and differ from the SCI42/SCI47 requests in allele (Aqeilan global KO, HT, P47T versus Synapsin-Cre KO/HT/WT), region and cell (CA3 primary, layer 2/3 dorsal cortex secondary), agonist (isoguvacine named), temperature (32-34 C named), age windows (P5-7, P10-12, P14-16 primary, P18-21) and unit reporting (cells, slices, animals, litters). They do **not** contain a high-chloride bridge re-record of the published 57.3/27.5 pA datum, evoked IPSC, paired-pulse, E/I, tonic current, an agonist-response measurement apart from the E_GABA puff, or Synapsin-Cre (string search: Synapsin 0 hits in the three files; paired-pulse 0; tonic 0; "evoked" only in the E_GABA sense "agonist-evoked current").
* `git grep` over `disease-models/wwox/research` and `framework` found no file that consolidates SCI42 M01/M03/M04/M05/M06 with SCI47 Phase 0 and the map rows. `research_lines_current.md` RL-GABA-002 records the August pre-specified test (DF_GABA at P14-P16, contrast KO vs WT only) as the pre-specified test; it does not mention SCI42 or SCI47.
* My inference: the correct statement is "a specification of the E_GABA+mIPSC+sIPSC core already exists from August (different preparation); the SCI42/SCI47 set is a later, partly overlapping, Synapsin-Cre-specific set; no single file reconciles them".

## Pairs considered (S0 definitions: same recording / partly overlapping / distinct)

| # | Pair | Answer | Cells that decide |
|---|---|---|---|
| 1 | SCI42 M01 vs SCI47 Phase 0 (v) | **same recording** (SCI47 adds input conductance: a readout added, no cell changed) | preparation L2/3 pyramidal, Cre WT/HT/KO, P13-17, gramicidin, E_GABA against rest and threshold |
| 2 | SCI42 M01 vs IT42-Q02 vs IT46-Q01 vs SCI47 L3 | **same recording** (the map rows are pointers; IT46-Q01 adds input conductance) | question text of each |
| 3 | SCI42 M01 vs glun2b M01 / IT42-Q01 (tissue pH) | **distinct** (quantity read: E_GABA vs pH; shared id "M01" is a name collision) | quantity_read, conditions |
| 4 | SCI42 M03 vs SCI47 Phase 0 (i) vs IT42-Q03 vs NP3P1 | **same recording** except configuration of the low-chloride arm (see conflict C1) and the antagonist cell (M03 names glutamate block, (i) names GABA-A antagonist; additive, no conflict) | internal solution cells; antagonist cells |
| 5 | SCI42 M04 vs SCI47 Phase 0 (ii) vs NP3P2 | **same recording**: mIPSC in TTX; readouts differ (rise and decay vs CV) additively; configuration native-chloride (perforated) vs physiological-chloride internal vs unstated is partly conflicting (C1) | measurement cells |
| 6 | SCI42 M05 vs SCI47 Phase 0 (iv) | **partly overlapping**: M05 says "puff or uncaging at a fixed distance"; (iv) says "puffed or bath". Puff satisfies both; bath does not satisfy M05 | delivery cell |
| 7 | SCI42 M06 vs SCI47 Phase 0 (iii) vs evoked part of IT46-Q10 | **same recording**; E/I ratio only in M06; configuration conflict C1 for holding-potential setting | M06 "holding potentials set with an experimenter-set low-chloride pipette" vs "perforated-patch cohort ... evoked IPSC" |
| 8 | SCI42 M07 (tonic) vs anything | **distinct** (no other request reads tonic; SCI47 L1 names tonic current only as the verification of a GABA-supply drug arm) | quantity_read |
| 9 | SCI42 M08 (interneuron counts) vs anything | **distinct** (histology) | quantity_read |
| 10 | SCI42 M02 (age series) vs SCI42 M01 | **distinct** (a programme of the others across ages; M01 itself is "interpretable alone at one age") | cohort_structure and age_bin cells |
| 11 | SCI42 M09 (WT slices driven into bursts) vs SCI47 Phase 0 (vii) (KO bursting vs non-bursting) | **distinct preparation, same question** (cause vs consequence): one cannot be met by the other | preparation cell |
| 12 | SCI42 M10 vs SCI47 L1 functional_comparator / Phase 1 / IT46-Q04 | **partly overlapping**: both are a matched non-GABAergic arm; the matching variable differs (conflict C2) | measurement/functional_comparator cells |
| 13 | NP3P3 vs IT53-Q01 | **same series** (heterologous, same-laboratory, matched-beta, EC10/EC20, alpha1/2/3/5) | trigger_to_reopen vs question text |
| 14 | NP3P3 / IT53-Q01 vs every slice recording | **distinct** (recombinant receptors vs slices) | preparation |
| 15 | glun2b M01 vs IT45-Q05 (first clause) | **same recording** (pH of the slice by genotype); IT45-Q05's second clause (TREK-1 Hill slope 30-37 C) is distinct | question text |
| 16 | IT49-Q10 (pH 7.4 vs 6.5 manipulation in K2P) vs glun2b M01 | **distinct** (manipulation vs measurement) | mode cell |
| 17 | CC-EGABA-EXPERIMENT-01 vs SCI42 M01 / SCI47 (v) | **partly overlapping**: same quantity and configuration; differs in allele, region (CA3 primary), age windows (P14-P16 primary vs P13-P17), agonist (isoguvacine named) and temperature (32-34 C named) | preparation, age_bin, conditions cells |
| 18 | IT40-Q03, IT46-Q04, SCI47 Phase 1, IT47-Q04, WO-17 | **outside the recording thread** (drug phase or K+/cell-context thread); IT40-Q03 and IT46-Q04 are drug-arm rows that depend on Phase 0; WO-17 and IT47-Q04 are adjacent | quantity_read |

Groups from my reading, as letters: A (E_GABA perforated; 5 request rows), B (sIPSC re-record; 6 rows incl. NP3P1 and the sIPSC part of IT46-Q10), C (mIPSC; 4 rows incl. WO-15), D (agonist response; 2), E (evoked IPSC; 2 plus IT46-Q10 part), F (tonic; 1), G (interneuron counts; 1), H (age series; 1), I (Rs/Cm/Rin; 1, a co-readout), J1/J2 (burst contrasts; 1 each), K (matched non-GABAergic arm; 5), L (pH; 3 rows), M (heterologous GABA-A series; 2), A2 (the August design; 1), P and Q (edge). Recording-session groups in the slice thread: A, B, C, D, E, F, G, H, J1, J2 plus the co-readout I; L is a separate slice measurement; K and P are drug phase; M is heterologous.

## Genuine conflicts I see (two requests identical in every other cell, differing in one)

**C1. Configuration of the physiological-chloride arm of the sIPSC/IPSC recording (whole-cell low-chloride pipette versus gramicidin perforated).** Same quantity (sIPSC amplitude and kinetics in native-like chloride), same preparation, same unit.
* SCI42 `chloride_gradient_sci42_20261110/output/new_measurements.tsv`, row M03, column `measurement`: "an experimenter-set low-chloride pipette (not native chloride: whole-cell chloride is set by the pipette)".
* SCI47 `inhibitory_defect_sci47_20261112/output/design_review.md`, section "Minimum design", bullet Phase 0: "the minimum that survives is a perforated-patch cohort for native-chloride sIPSC, mIPSC and evoked IPSC plus puffed agonist".
* Same file, same bullet, item (i): "sIPSC with a physiological-chloride pipette and with the high-chloride pipette in different cells". (Inside SCI47 "physiological-chloride pipette" and "perforated-patch cohort for native-chloride sIPSC" are used for the same item; the file does not say whether (i) is a whole-cell low-chloride pipette or a perforated one.) My inference: genuine in that the two cannot be one recording; but SCI47's own wording is ambiguous, so part of this is a gap.

**C2. Matching variable for the non-GABAergic control arm.**
* SCI42 `new_measurements.tsv`, row M10, column `measurement`: "Matched non-GABAergic suppression of bursts titrated to the same percent of evoked synaptic charge removed".
* SCI47 `levers.tsv`, row L1, column `functional_comparator`: "a submaximal NMDAR block (d-APV) or a hyperpolarising manipulation matched on the recorded cells' membrane potential and input resistance; the endpoint is the burst LFP in the same slices".
* Same cell class, same endpoint (burst), same purpose; the matching variable (synaptic charge versus membrane potential and input resistance) differs, so one titration cannot satisfy both. (SCI42 M10 `design_choice_not_finding`: "the matching metric (a design choice); the common axis" - the source itself calls the metric a choice.) My inference: genuine in text, resolvable by choosing one or reporting both as the source allows.

**C3. Same cell versus separate cohorts.**
* Map `batch_sci_20261105/map/open_questions_map.tsv`, row IT46-Q10, column `question_text_max300`: "what do evoked IPSCs and the GABA reversal potential show in the same cells?"
* SCI47 `design_review.md`, Phase 0 bullet: "Not as one protocol in every cell (high-chloride whole-cell, perforated-patch E_GABA, TTX mIPSC and evoked IPSC with paired-pulse cannot all be run in one cell without compromise [V9])".
* The August candidate gives a third position (`CC-20260826-EGABA-EXPERIMENT-01.md` section 3b): "One cell yields both measurements only in this order: perforated first, ruptured second, never the reverse." Note: the map row IT46-Q04 was updated with the cohort statement; IT46-Q10 was not.

## Divergences that are not conflicts (gap or synonym; my inference)
* Antagonist identity: SCI42 M03 names glutamate-receptor block and no GABA-A antagonist; SCI47 (i) names a GABA-A antagonist and no glutamate block; SCI42 M04 names both. Additive: one session can apply both.
* mIPSC readouts: "rise and decay" (M04) versus "CV" (Phase 0 (ii)) versus "decay tau" (August): additive.
* Genotypes: M03 and M04 do not name the arms; M01 and SCI47 name KO/HT/WT; NP3P1 asks the HT-versus-WT separation: gap in M03.
* Priority (not specification): SCI42 M04 `required_from_start` "no" and "partly redundant with M05 ... worth keeping only if M05 is done" against SCI47 listing mIPSC in the minimum Phase 0 and NP3P2 asking for it. A priority difference, not a cell conflict.
* Age: SCI42/SCI47/IT42-Q02/IT46-Q01 P13-P17; August P14-P16 primary, other windows secondary: nested (P14-P16 is inside P13-P17), but on a different preparation (conflict with the August candidate is not asserted).
* Name collision: IT42-Q01 points to `glun2b_comparators_sci42_20261110/output/new_measurements.tsv#M01` (tissue pH) while SCI42's `new_measurements.tsv` also has an M01 (E_GABA). IT42-Q02 `source_ref` carries no `#M01` anchor; its text says "reopen condition: M01 measured".

## Out of the thread (my judgment)
glun2b M02 to M07 (Mg/K/Zn, recombinant GluN2B inhibition, triheteromers, site test, subunit selectivity, NMDAR share); IT43/IT44/IT45/IT49 Kir/K+/Ih rows; IT50/51 OPC and myelin; IT48 NRF2; the NMDAR/AMPA rows IT40-Q01/Q02. Edge: WO-17, IT47-Q04, IT40-Q03, IT46-Q04 (all depend on or sit beside Phase 0).

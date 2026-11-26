# ADV-287 extension, H02: BLIND READER report as delivered (legend-delegate, claude-sonnet-5-5, effort high 63 of 63 turns; reply text extracted verbatim from its transcript hand-back call; 2026-11-26)

BLIND READER REPORT, PACKET_H02 (25 sentences), 2026-11-26

**Counts:** CORRECT 15, ADD 4, WRONG 0, INCOMPLETE 1, NOT ASSESSABLE 5.

**Read before using the counts**
- **Cited label not held.** The vigabatrin label set 082d818a, version 2026-06-15, is not in files/. On 2026-11-26 I searched files/ for "082d818a" and for the section 5.3 sentence. The only hit for the set id is a DailyMed search listing (dm_search.json).
- Label sentences (02, 13, 15, 24, 25, 30 and part of 26) are judged on three held sibling vigabatrin labels, whose 5.3 figures and 5.4 text I compared: Par e7cbc0a5 (2026-01-20, XML), Sabril powder a88ac1b4 (2021, XML) and openFDA Sabril a5d389d2 (2021, JSON). The wording of the cited version itself was not assessed. If sibling text is not acceptable, move these to NOT ASSESSABLE.
- **PMIDs 35183975 and 19194884 are not held.** Only repository quotes and table rows exist. Search 2026-11-26: filenames, plus content grep of files/ (json, xml, txt, tsv, html, md, csv, jsonl) for the PMIDs, DOIs, PMC2665303 and the phrase "taurine deficiency". The only hits were other papers or listings.
- **Wording note (02, 13, 15, 24).** No label states WWOX status. "Not WWOX-selected" is more exact than "non-WWOX". I did not count this as an error.

## Sentences

**H02-02: CORRECT.** Sibling labels 5.3 (sections read); PMID 19054414 abstract.
N=205, 22% vigabatrin-treated against 4% other therapies. The abstract says vigabatrin-naive.

**H02-03: ADD.** PMID 20384718, abstract.
- Evidence: 25/81 = 30.9%; 12/12 unexposed normal. The same abstract has 14 further children imaged before, during and after, of whom 4 had abnormal signal.
- Added sentence: "Of 14 further children imaged before, during and after treatment, 4 had it (29 of 95 exposed, 30.5 percent, derived)."

**H02-04: CORRECT.** PMID 36601084, full-text XML (text, Tables 1-3, captions; figure images and supplement not held).
38/172 = 22.1%; all had MRI per the inclusion criteria.

**H02-05: ADD.** PMID 19054414 abstract; sibling labels.
- Evidence: 22% against 4% naive, p<0.001, human infants. The design is a retrospective record review with blinded readers, so "controlled study" can be read as a controlled trial.
- Replacement: "4 percent of vigabatrin-naive infants in the retrospective ten-site comparison."

**H02-06: CORRECT.** PMID 33914858: Results text, Fig. 5 legend and rendered Fig. 5B (mouse).
180 ± 40 against 55 ± 35 myelinated axons per field; 180/55 = 3.27; plotted points match.

**H02-07: CORRECT.** PMID 42735667, abstract; evidence_b1 B1-11.
Verbatim; 9/18 = 50.0%, 34/46 = 73.9%.

**H02-08: CORRECT.** PMID 40670421, full-text XML, Table 2 and Discussion.
Right FA 0.463 against 0.427; only the finding group is starred; Discussion says exposed-normal did not differ.

**H02-09: CORRECT.** PMID 22128851, abstract (rat).
20 to 40 times the addiction-model dose; reductions smaller than with vigabatrin at its model dose.

**H02-10: NOT ASSESSABLE** (PMID 19194884 not held; repository receipt quote and B1-47 only).
- Evidence: the repository quote reads "67% lower in vigabatrin-treated animals than in control animals". B1-47 reports the six infants separately (below normal in 3, undetectable in 2). The record context lists rat, mouse and human, so the sentence as printed can be read as including the infants.
- Suggested: "Plasma taurine was 67 percent lower in vigabatrin-treated animals than in controls (not an infant figure)."

**H02-11: NOT ASSESSABLE** (PMID 35183975 not held; B1-17 and receipt only).
- Evidence: B1-17 gives a spectroscopic ratio of 0.48 against 0.31, p=0.31. It gives no group sizes for that comparison. "Two against eleven" appears to be derived from 13 imaged, 2 with the finding.
- Suggested: drop the parenthesis "two against eleven children" unless the abstract states it for spectroscopy.

**H02-12: NOT ASSESSABLE.** Card process statement and proposal; it states no source fact. The 22 versus 4 figures it mentions match the sibling labels.

**H02-13: CORRECT.** PMID 41442931 abstract; sibling labels.
Two children, no exposed denominator in the abstract; label figure 22%.

**H02-14: CORRECT.** PMID 19258289, abstract (22 infants, 34 MRIs).
Basal ganglia and brainstem hyperintensity, transient, maximal 3 to 6 months after start.

**H02-15: CORRECT.** PMID 41442931 abstract; sibling labels; PMID 19054414 abstract.
22% against 4%, retrospective, N=205. No arm sizes in these (grep for "205" in the three labels, 2026-11-26).

**H02-16: CORRECT.** PMID 36601084, abstract and full text; B1-01, B1-04.
"VABAM was observed in 38 patients (22.1%)" is verbatim.

**H02-17: ADD.** PMID 36601084, full text, Tables 1 and 2.
- Evidence: 8/80 = 10%, 30/92 = 32.6%. Rapamycin was given to 60/80 tuberous sclerosis children and 0/92 others. Within tuberous sclerosis: 3/60 (5%) with it against 5/20 (25%) without, p=0.021 (children).
- Added sentence: "Within tuberous sclerosis the counts were 3 of 60 with rapamycin and 5 of 20 without; no child with other causes received it."
- The record note points to DR-H02-013 for this, so I did not rate it INCOMPLETE.

**H02-21: CORRECT.** PMID 40670421, Table 2.
Left FA medians 0.390 (exposed, normal imaging, n=11) against 0.410 (controls, n=13).

**H02-23: NOT ASSESSABLE** (PMID 35183975 not held).
- Evidence: the repository supports p=0.03 (CSF free GABA, 5.26 ± 1.95 against 0.59 ± 0.63 µmol/L) and p=0.02 (ratio against controls). "Only ... were significant" needs the whole abstract, which only the primary can settle (UNSETTLED).
- Suggested until checked: "The reported significant differences carried here are p = 0.03 and p = 0.02."

**H02-24: CORRECT** (factual part; "recasts" describes the card and was not assessed). PMID 41442931 abstract; sibling labels.
No denominator in the abstract; label 22% against 4%.

**H02-25: CORRECT.** Sibling labels 5.3.
Matches: retrospective epidemiologic study, infantile spasms, N=205, 22% against 4% other therapies.

**H02-26: INCOMPLETE.** Sibling labels 5.3; PMID 19054414 abstract; receipt ledger.
- Evidence: 5.3 names no reference for the N=205 study, and the record context also says the label cites no source. The matching study's abstract (identity inferred) gives 22% against 4% and was read: FTR-20261106-19054414-23, abstract_only. Ledger grep and filename search on 2026-11-26 found no full-text read or copy.
- Replacement: "The label cites no source; the matching study (PMID 19054414, identification inferred) was read at abstract level only and gives the same 22 and 4 percent."

**H02-27: CORRECT.** PMID 40670421, Table 2.
1209/1280 (right), 1427/1366 (left), p=0.623/0.520. The Results prose calling group 1 highest is false on the right side against controls.

**H02-28: NOT ASSESSABLE** (primaries and CPP-115/OV329 answers not held).
- Held: the Pan 2012 abstract (no kinetics) and a ChEMBL answer for vigabatrin only (KI: pig 3.2 mM in 2003, pig 0.29 mM in 2020). Pan 2003, the Pan 2012 body, Silverman 2012 and Shen 2020 were not opened; their values come from the repository table abat_gabaat_h02.tsv.
- Repository arithmetic: 5.7/0.11 = 51.8. Review set: 51.5/0.282 = 183 (printed 52/0.28 = 186). OV329 against CPP-115 KI: 59/10 = 5.9.
- Wording flag: a single comparison (OV329) cannot be "reproduced". Also, the 2020 data give no CPP-115 kinact, so they compare KI, not efficiency.
- Suggested: "CPP-115 ranks above vigabatrin in the sets read (not all independent); OV329 had a lower KI than CPP-115 in one same-assay pig comparison."

**H02-29: ADD.** PMID 33914858, Results and Fig. 5B (mouse, P17, n=3 mice per genotype, fields plotted).
- Evidence: 180/55 = 3.27 is per electron-microscopy field. The running text of the same paper says "3.5-4-fold".
- Replacement: "about 3.3 times fewer myelinated axons per field in the corpus callosum at P17 (Figure 5B; the running text says 3.5 to 4-fold)."

**H02-30: CORRECT.** Sibling labels 5.4 and 8.4.
5.4: intramyelinic edema "at doses within the human therapeutic range"; no no-effect dose established in rodents or dogs.

## Files opened
Repository root: /home/desktop/legend-development/.claude/worktrees/sci_at_20261126
- framework/protocols/delegation_budget.md (sections 2, 7; section 10 printed by the same filter)
- In the adv287ext folder: PREREG_ADV287EXT_SCI_20261126.md (matching-rule section only) and PACKET_H02.md
- disease-models/wwox/research/drug_repurposing/cards/H02_gabaat_inactivator_myelin_exposure.packet.json
- Under disease-models/wwox/research/drug_repurposing/:
  - batch_sci_20261105/b1_whitematter/evidence_b1.tsv (selected rows)
  - batch_sci_20261105/b1_whitematter/receipts/FTR-20261105-35183975-23.json and FTR-20261106-19194884-23.json
  - batch_sci_20261105/b1_whitematter/queries.tsv (matching rows)
  - pharmacology_it5_20261029/abat_gabaat_h02.tsv and README.md (matching lines)
  - closed_loop_it4_e1b_20261028/README.md (matching lines)
- disease-models/wwox/registries/fulltext_read_receipts.jsonl (lines for 19054414 only

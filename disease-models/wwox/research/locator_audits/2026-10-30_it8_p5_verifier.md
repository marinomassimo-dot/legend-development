# IT8 P5 independent verification (read-only verifier)

Scope: `drug_repurposing/advance_it8_p5_20261029/` (README, loop1, loop2, TSVs), the five staged receipts
`receipt_staging/scientist-b/FTR-20261029-{37804316,41706892,42587157,42190665,34253921}-01.json`, and the
needs/cards text they feed. Sources re-read: the five Europe PMC / NCBI JATS full texts (SHA-256 of each equals the
receipt `source_fingerprint`), Brain Figure 5 as an image, PubMed record for PMID 28447936, ChEMBL REST (name,
similarity and activity queries; no personal data sent to any service). Not medical advice. No individual-level data.

## Verdict by claim

| Claim | Result |
|---|---|
| (a) 37804316: ISR postnatal/progressive (P1 equal, P14 raised) | CONFIRMED (Results sect. 1: "comparable ... at P1 ... postnatal and progressive activation"). |
| (a) HRI/DELE1 only as siRNA in fibroblasts; GCN2/PERK/PKR untested | CONFIRMED. Text has no hit for GCN2, PERK, PKR or EIF2AK; "No antibodies specifically recognizing DELE1 are available"; DELE1 cleavage only as HA-DELE1 in HEK 293T. |
| (a) P-eIF2a not reported in treated mice | CONFIRMED (Sephin-1 P-eIF2a only in patient fibroblasts vs controls, "not in controls"). |
| (a) Sephin-1 survival "about +10 days" | PARTLY: see M1. |
| (a) PMID 28447936 disputes the GADD34 target | CONFIRMED (PubMed abstract: Sephin1 and guanabenz "inert in vitro", kinase shut-off eIF2a-P dephosphorylation normal). |
| (b) 41706892: DHPG 5 min, ATF4 ~2.5x, P-eIF2a ~2.3x, Atf4 mRNA unchanged, n = 3 | CONFIRMED incl. statistics (ATF4 P 0.0470, p-eIF2a P 0.0428, mRNA P 0.7478, paired t, n = 3/group). |
| (c) 42587157: adult Cntnap2-null, control-AAV (dTom), 3/12 vs 10/14, P 0.018 / 0.026 | CONFIRMED; ">20 seizures/day" control outlier and "effect persists" (Ext. Data 10) also in text. |
| (c) "prevention within adulthood" reading | Defensible, but it is the package's reading, not the paper's (M3). |
| (d) 34253921 adult restoration, heterozygous, males, no seizure endpoint | CONFIRMED (no "seizure"/"epilep" in the full text; "adult male mice, ages four months or older"; HET constructs; 77 animals; 9.2 to 35.5 percent; 5-6 d vs 0 d lag, p > 0.4). |
| (e) 42190665 Csnk2b treatment at P3 only | CONFIRMED (Limitations: "intervention was at P3 ... Therapeutic efficacy for individuals with already apparent symptoms remains to be investigated"). Survival 50 to 80 percent and seizures 7/10 vs 1/10, 2/10 confirmed. |
| No other-disease precedent converted into WWOX evidence | CONFIRMED in README, loops, needs O4-O6/O9/O10 (all tagged OTHER_DISEASE_PRECEDENT, "transfer UNVERIFIED", counter-evidence lines present). |
| Sign opposition vs PARS2 fly | OVERSTATED (M2). |
| Sephin-1 / icerguastat absent from ChEMBL | FALSE at structure level (H1). |
| Five receipts: coverage honest | Coverage understated and hashes correct; verbatim locators essentially absent (M4). |

## HIGH

H1. ChEMBL claim is wrong. README sect. 5 / `loop1_partial_benefit/README.md` sect. 5 and `interventions.tsv` row 5 state that Sephin-1 and icerguastat are "absent from the catalogue and from ChEMBL (`NO_MATCH_FOUND`)" and that the only PPP1R15A activity row is a guanabenz isomer. Verified 2026-10-29/30 against the ChEMBL REST API: name search is empty (0 hits for "sephin", "icerguastat"), but a 90 percent similarity search on the Sephin-1 structure (2-chlorobenzylidene aminoguanidine, SMILES `N=C(N)N/N=C/c1ccccc1Cl`) returns exactly two records, CHEMBL2365743 (free base) and CHEMBL2346945 (hydrochloride), both with no preferred name (which is why the name-based adapter misses them). CHEMBL2365743 carries an activity row on PPP1R15A: Kd 23000 nM, SPR, MBP-PPP1R15A (340-698) against PPP1CC (document CHEMBL4665677, a 2020 SHP2-inhibitor review). So (i) "absent from ChEMBL" is a name-search artefact, (ii) "the only ChEMBL activity row on PPP1R15A is one guanabenz isomer" is false (Sephin-1 itself has a binding row; the data are a ~23 uM Kd, which neither confirms nor refutes target engagement in cells and is a secondary-review record), and (iii) the "opposite of the selectivity the potentiator premise needs" sentence rests on the incomplete row set. The IC50 977 nM / 33 nM guanabenz-isomer row (CHEMBL2369159, 2,3-dichloro) is traceable: assay record is in document CHEMBL4627375 (Bioorg Med Chem Lett 2020, "Monovalent protein-degraders", a review), so "primary assay not traced" (UNVERIFIED lists) can be narrowed to "primary paper behind a review record". Required fix: restate as "no name match; structure-matched unnamed records CHEMBL2365743 / CHEMBL2346945 exist, one PPP1R15A Kd row (23 uM)", and check whether the catalogue adapter/CHEMBL step should add a structure (InChIKey/similarity) fallback; icerguastat (a distinct compound name) was not independently structure-resolved by me (PubChem name lookup returned the same mono-chloro structure, C8H9ClN4, so the two names are very likely the same molecule; confirm).

## MEDIUM

M1. Survival gain. README: "survival extended by about 10 days (vehicle knock-outs die by about day 15, treated by about day 24)". From Brain Fig. 5C (opened): vehicle Afg3l2-/- all dead by about day 14-15; treated knock-outs step down at about days 18 to 24. Last-death to last-death is about 9 days, but median survival rises only about 6 to 7 days (about 13.5 to about 20). The text gives no number ("improved the lifespan", log-rank P < 0.0001). Label the figure as a maximum-survival reading and give the median.
Also dosing summary is loose: dams were gavaged three times in E14-E20 and twice P0-P3, pups got daily intraperitoneal injection from day 1 (Methods), not "daily from E14".

M2. "Opposite in sign" (AFG3L2 protective vs PARS2 fly harmful; need O9/O6, E01 and C01 text) compares unlike endpoints. The AFG3L2 "protective" evidence is (i) fibroblast growth in low glucose after siRNA and (ii) a drug whose mechanism is disputed with no in-vivo P-eIF2a; the PARS2 "harmful" evidence is a bang-sensitivity seizure fraction after kinase/ATF4 RNAi in flies. Different species, endpoint, readout, manipulation (loss of a kinase vs a drug). The package hedges in places but the headline "two opposite precedents" and "the sign is lesion-dependent" are stronger than the data. Also the needs text calls both "DEE-type mitochondrial precedents"; the AFG3L2 mouse is a lethal ataxia model (SPAX5 clinical spectrum includes myoclonic epilepsy), not a DEE model.

M3. Meis2 seizures. The paper frames the result as "seizures were suppressed" / "re-instated in adulthood to reverse developmental deficits"; the "prevention in adulthood" label is the package's, resting on a cited statement ("can develop seizures after 6 months", intro: "seizures by around 6 months"), with no pre-treatment ECoG, so onset-versus-treatment order in each animal is unknown. Also `loop2_recovery.tsv` assigns the module label `prevented_early_window` to an adult (2-month) injection, which will read as "early-window" in downstream views. Not mentioned: 1 of 6 wild-type mice given Meis2 had two seizures (Ext. Data 10; control-virus wild type 0/3). Wording suggestion: "treated before the stated typical onset age; reversal vs prevention not separable".

M4. Receipts. All five carry the `evidence_basis` entries `coverage_map` and `work_manifest` and the sentence "Passages quoted in the output file", but no work manifest or `verbatim_locators` exist for these PMIDs (no `deepdive_manifests/PMID<...>.json`; no `verbatim_locators` key in any of the five, unlike the scientist-c receipts). Only about three passages are quoted verbatim anywhere in the loop files ("certainly deserves further investigation", "remains to be investigated", "Meis2-independent compensatory mechanism"); all three occur in the sources (the third with the extractor's spacing). TSV `locator` columns give section/figure references, not quotes. Partial reads do not formally need locators, but the claim "work_manifest" in `evidence_basis` is not backed. Coverage vocabulary use is conservative and consistent with the workflows (Results marked not_read for Shank3 and Csnk2b although numeric Results text was used: understated, honest under the stated rule, but the loop text then cites statistics from those sections). Fingerprints verified identical to disk. Fix: drop `work_manifest` from evidence_basis or add a manifest with quote, anchor, proposition triples for the decisive claims verified above.
Minor mismatch: Brain receipt `limitations: not_present` while the Discussion discusses limits; fine.

M5. "Activity" confound. PMID 41706892 manipulates a group I mGluR agonist (DHPG) in slices/neurons, not network activity; there is no TTX, firing or glutamate-release manipulation in the paper. The package states "activity is a second route to raised ATF4 protein" (loop1 inference 4, need O10). That is an inference (agonist mimicking synaptic mGluR drive), correctly listed as UNVERIFIED for canonical targets but not for the activity link itself. The proposed TTX/mGluR5-antagonist arm is sound; reword the observation as "mGluR agonism" and the inference as an hypothesis.

M6. Experiment design. Pre-declared criteria are stated for Loop 1 as "thresholds set by the experimenter before the run" (no numbers) and for Loop 2 R1 as "wild-type range" (undefined; equivalence margin not given). Discriminating structure is good (genotype x silencing x kinase interaction; vector control; same-organoid baseline; R3 falsifier), but add: a partial-normalisation row for the TTX arm, and a numeric margin/sample size or at least an analysis plan stating the unit (organoid batch/animal). R1's second half (prenatal progenitor composition not recoverable) gets no support from Shank3 or Meis2, which measured no progenitor endpoint; only the circuit half is supported by the leads.

## LOW

L1. Csnk2b CAG-arm seizure incidence difference is P = 0.07 (not significant); loop2 lists "1 of 10 and 2 of 10" without that. Authors' summary also says deficits "can be corrected after birth" (P3), consistent with the package's reading but worth quoting.
L2. Shank3 behaviour statistics have df of 52-58 (sessions or trials pooled, not 77 animals); loop2 notes neurons are the unit but not the same for the behaviour t tests.
L3. Brain Fig. 1C-F/Fig. 4 numeric readings (Atf4 mRNA 0.8 to 1.4; about 62 to 72 percent live cells) are plot readings not in the text; correctly labelled as readings.
L4. "attenuated mitochondrial translation ... the target 'certainly deserves further investigation'": the authors' sentence says the effect of Sephin-1 at the mitochondrial level deserves investigation, not "the target".
L5. The ChEMBL guanabenz mechanism statement (only curated mechanism alpha-2 agonist), fosigotifator/DNL343 statements, and DGIdb-only kinase-inhibitor rows were not re-run by me (catalogue cache); not verified.

## Not verified / limits

Supplementary PDFs and videos of Brain, the PNAS SI PDF and Dataset S1, Meis2 Methods and supplementary tables, and Shank3 figures were not opened. The catalogue (non-ChEMBL) claims were not re-run. I did not edit any file other than this report.

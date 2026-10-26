# Stiripentol and LDH: the 2015 precedent, its analogues, and what the readings can and cannot carry (package P2a)

`scientist-b`, 2026-10-26, task branch `task/sci-b-p2a-sada2015`. Operator-approved mandate. Exploratory, non-canonical, class level, not medical advice.
Every statement here is **NOT WWOX EVIDENCE**: it concerns an enzyme, tumour cell lines, rats, mice or children with other diseases. Assay and
exposure figures below are the **conditions of the cited experiments**, quoted so that they can be compared; they are not doses, not exposures
proposed for anyone, and not a suitability statement. No wet-lab or clinical act is authorised or claimed.

## 0 · Depth declared first

| Source | What was obtained | Depth | Receipt |
|---|---|---|---|
| Sada 2015, *Science* (PMID 25792327) | **Not acquired.** Abstract and PubMed record only. | `abstract_only` (discovery, not reading) | none possible |
| Rico-Molina 2024, *Int J Mol Sci* (PMID 39769031; open access, CC BY) | JATS body, 8 figure files, supplement (47 pages) | `partial_fulltext_read` (figures read, supplement captions-only apart from page 44, references not read) | `FTR-20261026-39769031-01`, staged; manifest `PMID39769031.json` PASS |
| Yadav 2026, *Eur J Pharmacol* glioblastoma (PMID 42035940) | JATS body | targeted passages (Methods for the LDH assay, Results 3.1, Discussion) | none |
| Guyon 2022, *EMBO Mol Med* (PMID 36278433) | JATS body | targeted passages naming stiripentol (Results, legends, Methods in vivo) | none |
| Bouchez 2026, complex I (PMID 41570991) | JATS body | abstract, Introduction, Results on concentrations, INT/duroquinone and malate dehydrogenase, Discussion | none |
| Bacq 2024, *Adv Ther* review (PMID 38443647) | JATS body | the LDH, exposure and concentration passages and Tables 1 and 2 | none |
| Le Dudal 2019, *J Clin Invest* (PMID 30946030) | the public PMC article page (HTML; the PMC XML is a restricted stub) | Introduction, Results, Discussion and Methods text read; figures not opened | none |
| Bai 2019, *Eur J Med Chem* (PMID 31539780; ChEMBL `CHEMBL4311969`) | abstract and the ChEMBL assay records only | database rows + abstract | none |

### Acquisition of the target (M1), the cascade that was run
PubMed metadata (no PMCID; one "Comment in" notice, a Science perspective, PMID 25792315, closed likewise) -> Europe PMC core record (`inPMC N`, `isOpenAccess N`, one
"Subscription required" DOI link) -> OpenAlex by DOI (`closed`, `any_repository_has_fulltext false`) -> Semantic Scholar by DOI (`CLOSED`, empty URL) -> Crossref
(licence start date only, no open version) -> publisher landing, full-text and PDF routes (HTTP 403 on all three, unauthenticated) -> two repository lookups
(CORE answered 403, the Okayama University repository answered 429; neither was retried or worked around). Not used, by rule: Unpaywall and its kind (they demand a
contact address), author contact, publisher registration. **Result: no lawful full text. Recorded as items 16 and 17 of `operator_pdf_wishlist_20261021.md`.**
What the repository holds on the 2015 report is therefore its abstract, plus the open-access descriptions of it listed in section 2, each labelled second-hand.

## 1 · FIRST-PASS OBSERVATIONS (Rico-Molina 2024, read as a source, before the comparison)

- **Design.** One enzyme assay: recombinant human LDHA, fluorescence of NADH, 1 mM pyruvate called saturating, 5 percent DMSO, 28 degrees C, 0.041 U/mL enzyme. A selective LDHA tool compound is named as positive control; **its measured inhibition is not reported**. No detergent is named.
- **Stiripentol.** At one concentration (500 micromolar, n = 4): racemate 9.9 +/- 2.3 percent, (-)-(S) 34.0 +/- 2.1, (+)-(R) 38.4 +/- 1.6, iso-stiripentol 21.1 +/- 3.5. The IC50 column reads ">500" for all four. **That is a bound, not a fitted potency: the supplement's dose-response curves (S65 to S74) exist only for analogues.** The racemate sits far below both of its enantiomers in the same assay, which the text does not discuss; the stiripentol figure is therefore itself uncertain (about 10 versus about 35 percent).
- **Analogues.** Four synthetic compounds (3, 4a, 4b, 5) reach 46 to 72 percent at that concentration; fitted IC50 100 to 200 micromolar (best 101.7 +/- 6.7, n = 3). The authors place that beside galloflavin and luteolin glucoside: tool-grade potency. The supplement curves (read: page 44) are steep (about one log unit from near 100 to near 10 percent), under 5 percent DMSO and with no detergent named; that is a pattern shared with non-specific or aggregating inhibitors, a **flag, not a finding**.
- **About the 2015 report.** The authors state, at second hand, that Sada et al. found about 40 percent inhibition of both directions at the same concentration on purified mammalian LDH and attribute the difference from their 10 percent to assay conditions.
- **Scope.** No neuron, brain, seizure, cell or animal datum. The authors' purpose is primary hyperoxaluria (liver). They state that in vivo comparison and hepatotoxicity remain to be done.
- **Possible errors in the source that matter here.** (i) a bound read as a value ("IC50 higher than 500" for stiripentol); (ii) "significantly" with no test; (iii) racemate below both enantiomers; (iv) positive-control result absent. None changes the weak-in-this-assay reading of stiripentol; all limit how far the paper can anchor a potency.

**FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON:** the repository's ChEMBL stiripentol rows (`lucas_clarke_followup_20261026/chembl_named_activities.tsv`), card `E02`, `compounds_and_sources.md`, `HYP-20261026-11`, `R-11`, `DL-REPO-004`. `registry_records.py get --pmid 25792327` returned only surface preambles (an empty answer to that query, not proof that the laboratory does not know the paper).

## 2 · Stiripentol and its analogues, four layers kept apart

### 2.1 Enzyme activity (cell-free) — the three single-concentration measurements disagree and none gives a potency

| Measurement | System and conditions | Stiripentol result | Analogue result | Depth here |
|---|---|---|---|---|
| Sada 2015, as described by Rico-Molina 2024 | purified mammalian LDH, both directions | about 40 percent at 500 uM | "a stiripentol analog" more potent, identity and numbers unknown | second-hand |
| Sada 2015, as described by Bouchez 2026, Bacq 2024, Guyon 2022 | LDH1 and LDH5; non-competitive; "specificity among 20 other anticonvulsants"; brain-penetrant with cerebral LDH inhibition in mice | no numbers given | - | second-hand; each source cites it for a different point |
| Rico-Molina 2024 | recombinant human LDHA, 1 mM pyruvate, fluorescence | 9.9 percent (racemate), 34 and 38 percent (enantiomers) at 500 uM; IC50 ">500" (bound) | 46 to 72 percent; IC50 100 to 200 uM | partial full read, receipt |
| Bai 2019 = ChEMBL `CHEMBL4311969` | human LDH5 and LDH1, UV-vis, sodium pyruvate | **7 percent at 2 mM on both isoforms** (identical values); the 0.5 mM rows hold **no value** in ChEMBL | compounds 68 to 70 "more potent than stiripentol", non-competitive (abstract) | database + abstract |
| Yadav 2026 glioblastoma | U87 cell lysate, kinetic NADH assay, Triton X-100 in the mix | "moderate": significant inhibition only at 250 and 500 uM | - | targeted passage |

Reading: the four numbers share a compound and nothing else (enzyme source, isoform, substrate level, detergent, readout, concentration). 7 percent at the **highest** concentration (2 mM) does not
contradict 40 percent at 0.5 mM only if the assays differ in sensitivity; it is not a dose-response. **No source here fits a stiripentol IC50.** Hence the ChEMBL 7 percent is one weak
datum from a different laboratory and assay, and is not a general verdict on stiripentol; equally, the 2015 "about 40 percent" is a second-hand figure and cannot be used as strong inhibition.

### 2.2 Cellular effects — they occur below the concentrations that inhibit LDH in lysate, and complex I is a direct target

| Source | Cells | Effect of stiripentol | Concentration of the experiment |
|---|---|---|---|
| Yadav 2026 | U87 glioblastoma | viability falls; Seahorse ECAR **and** OCR fall; LDHA over- or under-expression changes viability, stiripentol adds nothing on top "statistically" | 10 to 60 uM viability; 25 and 50 uM Seahorse; lysate LDH only at 250 to 500 uM |
| Guyon 2022 | glioblastoma stem-like cells (the paper's P3 line) | lactate production -50 percent over 24 h (Laconic FRET), basal and uncoupled respiration "drastically" inhibited, spheroid growth and invasion reduced | 500 uM |
| Bouchez 2026 | glioblastoma, small-cell lung cancer cells; isolated heart and liver mitochondria | **direct, immediate inhibition of complex I NADH oxidation**, upstream of the ubiquinone site (not rotenone-like); malate dehydrogenase not inhibited; in mouse cell lines respiration down about 70 percent at 100 uM and about 90 percent at 200 uM (a supplementary figure, not opened here) | 100 to 500 uM in cells; about 50 to 150 uM in the isolated-mitochondria enzyme assays (one figure caption prints 200 mM, evidently a typo) |
| Le Dudal 2019 | HepG2, hydroxyproline-driven oxalate | dose-dependent fall in oxalate; LDHA siRNA also lowers oxalate; adding stiripentol to siRNA lowers it "mildly" (n = 4) | 5 to 100 ug/mL (about 21 to 430 uM) |
| ChEMBL `CHEMBL5120856` (2022 chemistry paper) | primary hyperoxaluric mouse hepatocytes | fold-change 0.27 to 0.7 in a GO/LDHA assay | not read (database row) |

Reading: stiripentol changes cellular lactate, respiration and viability in tumour and liver cells, but **the data do not isolate LDH as the mediator**: the same drug inhibits
complex I directly at similar or lower concentrations, and the authors of the 2026 glioblastoma paper and the complex I paper both say so or show it. The LDHA-siRNA arm in HepG2 is the best
argument for an LDHA component; it is one experiment, n = 4, with an indirect readout (oxalate, no LDH activity or lactate).

### 2.3 Animal results — all in other diseases; one pathway-specific readout

| Source | Model | Result | Experimental exposure (as run) |
|---|---|---|---|
| Sada 2015 (abstract; second-hand) | mouse seizure model | LDH inhibition and an analogue suppressed seizures; stiripentol described as brain-penetrant LDH inhibitor | UNKNOWN here |
| Le Dudal 2019 | rats: oral, 2 days; ethylene glycol; hydroxyproline nephropathy | urine oxalate down (0.16 to 0.11 mmol/mmol creatinine, n = 6), glycolate **up** in the nephropathy model (consistent with a block of glyoxylate-to-oxalate conversion), crystalluria and renal function better | 200 to 300 mg/kg/day, against about 50 mg/kg/day in children in the review's Table 1; no species scaling applied |
| Guyon 2022 | mouse glioblastoma xenograft | survival longer (log-rank P 0.002, n 15 to 16) | 150 mg/kg in the figure legend, 100 mg/kg in the Methods: **the paper disagrees with itself** |
| ChEMBL (several documents) | mouse MES and PTZ seizure assays, rotarod | anticonvulsant activity with ED50 values, neurotoxicity rows | database rows; not read |

Reading: no animal result in these sources measures **brain LDH activity or lactate** after stiripentol. The one pathway-specific in vivo readout (oxalate down, glycolate up) is hepatic and at
doses far above the antiseizure range. The antiseizure and anti-tumour animal results do not separate LDH from the drug's other targets.

### 2.4 Exposures — the comparison that decides plausibility

Quoted from the open-access review (secondary; not re-derived): total plasma 17 to 106 uM at effective antiseizure doses in children and adults (Table 1 of the review); free tissue
level estimated 0.2 to 1 uM because about 99 percent is protein-bound; rat brain to plasma ratio about 0.5 to 1.2; one rat measurement of liver to plasma about 35 one hour after an intravenous dose; the
concentrations that inhibit LDH in vitro are given as 42 to 500 uM, "globally higher than therapeutic concentrations". The review ranks, by sensitivity, GABA-A potentiation > ion channels >> LDH/energy
metabolism, and states that 500 uM was needed for seizure cessation by LDH inhibition in rodents, "suggesting that other mechanisms were involved". **This sits against the 2015 report's own claim and the report could not be read to check it.**

## 3 · What the readings support, and what they do not

**Supported (DATO at the stated depth):**
1. Stiripentol inhibits recombinant human LDHA weakly in the one assay read in part (about 10 percent at 500 uM; about 35 percent for its enantiomers), and no study held here fits a potency.
2. Synthetic analogues of stiripentol inhibit human LDHA more strongly in that assay (IC50 100 to 200 uM); they are tool-grade, with no cell or animal datum in the paper.
3. Stiripentol reduces tumour-cell and liver-cell lactate, respiration or viability at concentrations in the tens to hundreds of micromolar, and inhibits mitochondrial complex I directly.
4. In rats at high doses it lowers urine oxalate and raises glycolate in a hyperoxaluria model.

**NOT supported:**
- That stiripentol is **inactive** or "inefficacious" on LDH. One weak enzyme number (7 percent at 2 mM; 10 percent at 0.5 mM) cannot be set against a second-hand 40 percent from the paper that proposed it, a cellular lactate fall, a pathway-specific rat readout and a 2015 report nobody here has read. The honest state is **potency unresolved**.
- That stiripentol's antiseizure action is LDH-mediated (the review argues against on exposure; the 2015 report argues for it).
- That any of this helps or harms in WWOX deficiency. No WWOX-deficient system was used by any source; the fly amyloid precedent (`PAPER 567`) is amyloid-conditional and has no drug arm.
- Any inference from a result in another model (tumour, liver, rat, mouse seizure) to WWOX-DEE.

## 4 · Reconciliation with the repository's records

- **ChEMBL `CHEMBL4311969` is Bai 2019 (PMID 31539780), not a stiripentol paper.** Stiripentol is the comparator; the 7 percent is at 2 mM on LDH5 and LDH1 with identical values, and the 0.5 mM rows hold no number. The repository's earlier wording ("single-digit percent inhibition at a single high millimolar-range concentration") is accurate; what was missing was the document's identity, the empty lower row and the comparison with the other two single-concentration measures. Card `E02` row `DR-E02-001` is updated accordingly.
- **The 2015 report is now identified.** The card's novelty line said it "was not found by my query"; it is the Science paper above, paywalled, known by abstract and three open-access descriptions. `R-11`'s sentence "no source attributes its antiseizure action to LDH" is **wrong as stated**: the 2015 report does (in epilepsy models, abstract-level), and a 2024 review argues the exposure is insufficient. Proposed correction is in the commit candidate.
- **The "later sources already identified"** (the 2024 chemistry paper = Rico-Molina; the 2026 glioblastoma paper = Yadav) were abstract-level; they are now read at the stated depth, and **their claims are narrower than their abstracts suggest** ("moderate but not potent" = significant only at 250 to 500 uM in lysate; the 2024 paper's "10 percent" = a single-concentration screen with no stiripentol curve).
- **New relative to the earlier record:** direct complex I inhibition (2026) and the exposure gap (2024 review). Both separate "stiripentol changes cellular metabolism" from "stiripentol inhibits LDH in brain".
- `HYP-20260709-01` (ketogenic) and the PDK/DCA position: unchanged.

## 5 · Analogues versus stiripentol, summarised without ranking
Analogues from Rico-Molina (3, 4a, 4b, 5): enzyme IC50 100 to 200 uM, tool-grade, steep curves flagged, no cell, brain, animal or safety datum. Analogues from Bai 2019 (68 to 70): LDH1/LDH5 inhibition said to exceed stiripentol's, non-competitive, anticonvulsant in three mouse models with low neurotoxicity, GABA-A modulation (abstract only). The 2015 analogue: unknown here. None of them has any datum in a WWOX system. Nothing here ranks them.

## 6 · Discriminating experiments (PROPOSALS ONLY; nothing authorised to run)

The readings change one thing: a **stiripentol arm in a WWOX experiment would not test LDH**, because its LDH potency is unresolved and it hits complex I. So the order of the previously proposed
experiment (`HYP-20261026-11`, stage three: "stiripentol against a selective LDHA tool at matched exposure") must be preceded by an assay-level stage.

**E-A (no WWOX; decides whether stiripentol is an LDH tool at all).**
- *Question:* what is stiripentol's fitted potency and mode on human LDHA and LDHB, and is the 7/10/40 percent spread an assay artefact?
- *Model:* recombinant human LDHA and LDHB, plus a lysate of a human neural cell line.
- *Controls:* a selective LDHA inhibitor with a published curve (positive); oxamate; vehicle matched for DMSO; each stiripentol enantiomer separately; **with and without a non-ionic detergent** (aggregation test); pyruvate at sub-Km and saturating; both reaction directions; pre-incubation time varied; at least two independent enzyme lots.
- *Endpoint:* fitted IC50, Hill slope, substrate dependence, detergent sensitivity.
- *Result that would change interpretation:* a fitted IC50 within reach of free tissue levels, detergent-insensitive and substrate-competition-consistent -> LDH engagement becomes plausible at tolerated exposure and the stiripentol arm becomes informative; an IC50 in the hundreds of micromolar, or one that collapses with detergent -> the stiripentol arm of any WWOX test cannot be read as an LDH test and `HYP-20261026-11` should rest on a selective LDHA tool.

**E-B (WWOX human neural cells; only after the lactate and LDH readout of `HYP-20261026-11` stage one shows a WWOX-linked change).**
- *Question:* in WWOX-deficient versus isogenic human neural cells at matched maturity, does an LDH-directed intervention move lactate, and is stiripentol's effect that of an LDHA tool or of a complex I inhibitor?
- *Arms:* vehicle; a selective LDHA tool; LDHA knockdown; stiripentol (a concentration bracket that includes the free-level estimate and the in-vitro-effective range, reported separately); a low-dose complex I inhibitor of the rotenone type as the mechanism-dissociation control.
- *Endpoint:* isotope-resolved glucose-to-lactate flux and lactate-to-pyruvate relationship, NADH/NAD+ redox readout, OCR and ECAR; one functional endpoint (network excitability or a synaptic readout) in the arms that move lactate.
- *Result that would change interpretation:* stiripentol phenocopies the complex I control and not the LDHA arms -> its effect is not an LDH effect and the repurposing rationale for LDH lowering by stiripentol is closed (the LDH lever itself stays open via the tool); stiripentol phenocopies the LDHA arms and shifts lactate only in the deficient line -> LDH-lowering becomes a testable lever in WWOX deficiency; no lactate change in any arm -> the strand is parked with the reopening condition already in the card.

**E-C (the 2015 report itself).** If the operator can obtain the article, read the enzyme figures, the exposure and the analogue identity first; E-A can then be designed against the report's own conditions (substrate level, enzyme source) rather than guessing why the three laboratories differ.

## 7 · Limits, owed work, and verification
- The 2015 report is **unread**. Every statement about it is second-hand and labelled so; the analogue is not named because its identity is not known here.
- Only one paper has a receipt (partial). The other five open-access sources were read at targeted passages; their figures were not opened (Le Dudal 2019, Bouchez 2026, Yadav 2026 and Guyon 2022 carry the cellular and animal rows). A blind audit of the propositions in `PMID39769031.json` is owed to someone other than the producer; the two over-reach flags (a bound read as a value; racemate below its enantiomers) go to the auditor first.
- Concentration and dose figures in sections 2.2 and 2.3 are experimental conditions as printed by the sources, not re-derived and not recommendations.
- No e-mail, registration, author contact or paid service was used; Unpaywall-type indexes were not queried.

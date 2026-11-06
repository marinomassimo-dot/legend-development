# IT29 P12: targeted capability scout, functional-screen data (2026-11-05)

Non-canonical. Not medical advice. Zero spend; no registration, contact or e-mail sent anywhere; only generic topic words and public
URLs. WWOX not used as a keyword. Nothing installed. Not reopened: anything in IT27 P13 / IT28 P12 READMEs (nothing concrete changed).
Depth: web-search summaries for everything except the one tested resource (data file opened and parsed; paper abstract read, methods not).
Derived rows only in this directory (`test_ncc_vs_case1.tsv`, 20 rows); the third-party spreadsheets stayed in the scratchpad, not in git.

## Correction (IT30, 2026-11-06)
The endpoint named below is wrong: the file tested here is the cytokine-protection AB screen (percent of quetiapine), identical to paper 2's Additional file 3, not a differentiation table; every "direction recovered", "agreement" and "contradiction" in this note and in `test_ncc_vs_case1.tsv` is withdrawn as differentiation evidence. See `../ncc_reconciliation_it30/README.md`.

## Decision
No installable tool closes the gap. One public output does, partially: a compound-level, dose-resolved OPC differentiation screen with a
viability counter-screen, deposited as spreadsheets. On the 20 frozen compounds it recovers a direction for 11 that a name lookup could
only mark 'present', and it disagrees with the frozen sign for 5 (two are likely artefacts, see below). That disagreement is itself the
finding: sign in the frozen table depends on the assay system.

## Test (candidate: NCC library acute OL differentiation screen)
Source: Lariosa-Willingham et al., BMC Res Notes 2016, PMID 27592856, DOI 10.1186/s13104-016-2220-2; data on figshare as Additional
files 2 and 3 (Table S1 viability % of DMSO at 10/1/0.1 uM; Table S2 differentiation, % of quetiapine at 10/2/0.4/0.08 uM), 727 NIH Clinical
Collection compounds, acutely purified rat OPCs, immunofluorescence. Licence CC BY 4.0 (figshare record: CC BY + CC0). Cost: two files,
52 KB and 68 KB, no key, about 30 minutes including parsing (xlsx read from XML; no library needed).
Rule fixed before reading values: call = sign of the value at the highest concentration that has a value and viability >= 50 percent of DMSO;
favourable if >= +25, adverse if <= -25. Quantity: percent of quetiapine, a rescue-style scale, not an effect size.

| Outcome (20 compounds) | n |
|---|---|
| In the library, direction recovered | 11 (benztropine under the spelling Benzatropine; mevastatin misspelt Mevistatin) |
| Agrees with frozen direction | 6 (benztropine, ipratropium, oxybutynin, ifenprodil, mevastatin; quetiapine is the assay normaliser, so circular) |
| Contradicts frozen direction | 5: clobetasol, ketoconazole (clean sign); miconazole and tamoxifen (biphasic, opposite signs at different doses); liothyronine (probable artefact: the paper uses thyroid hormone as its validation promoter, so negative values here need the methods before use) |
| Not in library | 9 (clemastine, atropine [hyoscyamine and scopolamine present as proxies, not counted], amorolfine, bexarotene, sobetirome, trichostatin, apicidin, fimepinostat, neostigmine) |
| Name lookup (ChEMBL/PubChem presence) recovers | 0 directions, 11 'present' |

Reading: where it agrees, it adds an independent in-vitro sign for the muscarinic antagonists (benztropine, ipratropium, oxybutynin; the
frozen search layer abstains on them). Where it contradicts, three of the five are the azole/glucocorticoid hits sourced from a different
OPC system (mouse EpiSC-derived, per search summary only), which turns 'favourable' into 'context-dependent' unless the methods explain
it. Caveats: single screen, one concentration series, % quetiapine scale, no replicate statistics read, not read in full.

## Other resources (search-level only, not tested)
| Resource | Verdict | Reason |
|---|---|---|
| NCC acute OL differentiation screen (above) | **ADOPT as in-house derived rows** | tested, cheap, CC BY, gives sign and a viability flag; read the methods once before relying on any contradiction |
| Deshmukh/Najm 2015 Nature OPC screen supplement (miconazole, clobetasol) | TRIAL | likely compound-level tables; already behind frozen rows, use to explain the contradiction above; unread |
| Strickland 2018 / Kosnik 2019 MEA screens of ToxCast chemicals (1,055 at 40 uM; 384 multi-dose), Shafer/EPA | TRIAL for case 2 | public compound-level firing-rate calls on primary cortical networks; mixes pharmaceuticals and pesticides, firing rate is not seizure; deposit location (supplement or CompTox/invitrodb) unverified |
| Dinday and Baraban 2015 eNeuro, scn1lab zebrafish, ~1000 compounds | WATCH | hit list and velocity criterion in the paper; whether per-compound numbers are deposited is unconfirmed; reopen on opening the supplement |
| Patents listing a 6,058-compound OPC screen | REJECT | hit names only, patent text, no data |
| Sterol-pathway OPC studies (RSC Chem Biol 2022) | WATCH | mechanistic, not a deposited screen |
| PubChem BioAssay / ChEMBL assay descriptions, GEO, Hugging Face, GitHub for (c) offline readout prediction | not found | no search hit surfaced an offline assay-to-compound functional predictor; not exhaustively searched; reopen on a named tool |

## Component decision
Keep: a small in-house loader for the NCC tables (derived rows only, attribution CC BY, citation PMID above). It justifies its cost on the
test (a direction for 11 of 20 at about 30 minutes). Everything else: no change, reopening condition = a deposited per-compound table
for a seizure-relevant network assay (case 2) is confirmed to exist.

## Not reached
Paper methods and figures (thyroid hormone handling, hit criteria); Nature 2015 supplement; MEA data deposit location; Baraban supplement.

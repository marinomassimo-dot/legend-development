# Blind locator audit - triples_A2 (43 triples, 27 PMIDs)

Auditor: blind locator auditor (no session history; nothing under `batch_sci_20261105/` was opened except to write this directory). Date: 2026-11-05. Method: `.claude/skills/legend-locator-audit/SKILL.md` (two questions per triple; verdict vocabulary SUPPORTED / OVERSHOOT / UNDERSHOOT / NOT_IN_SOURCE / UNVERIFIABLE_SURFACE). Not medical advice.

## Counts per verdict

| Verdict | n |
|---|---|
| SUPPORTED | 40 |
| OVERSHOOT | 2 |
| UNDERSHOOT | 1 |
| NOT_IN_SOURCE | 0 |
| UNVERIFIABLE_SURFACE | 0 |
| **total** | **43** |

Quote matching: all 43 quoted fragments occur in the source text. 30 match verbatim; 13 match after normalisation only (NFKC, Unicode dashes and non-breaking hyphens to '-', collapsed whitespace, Lancet middle-dot decimal to '.'); in no case does a word differ. No quote was from a figure image, so no UNVERIFIABLE_SURFACE verdict was needed (A2-B09 quotes a Figure 3 *caption*, which is text and matched verbatim).

## Non-SUPPORTED triples (exact reason)

### A2-A11 (PMID 31929713) - UNDERSHOOT

- Quote found: EXACT.
- Reason: Quote is verbatim but is the commentators' own claim (non-responders quickly given vigabatrin; combination 'may enhance' 18-month outcomes), not a restatement of ICISS. Commentary restates A08 with numbers and A09 without; proposition omits the editorial claims.
- Suggested wording: Secondary commentary; restates A07 and A08 with numbers and A09 without numbers (anchor: 'This study also reported that spasm cessation between days 14 and 42 of the treatment was associated with higher mean VABS scores and reduced probability of seizures at 18 months'); additionally asserts, as the commentators' opinion, that combination therapy should be preferred in most cases and 'may enhance developmental and epilepsy outcomes at 18 months', a claim the trial's null result does not support and the ICISS abstract does not make.

### A2-B13 (PMID 23740534) - OVERSHOOT

- Quote found: EXACT.
- Reason: Review (18 trials, 916 infants) says hormonal treatment 'might improve' developmental outcome 'compared with vigabatrin in infants not found to have an underlying cause' (one study). Proposition states 'developmental benefit only in...': hedge 'might' dropped, 'only' added, comparator omitted.
- Suggested wording: association: the review states that hormonal treatment resolves spasms faster and in more infants than vigabatrin, which may or may not translate into better long-term outcomes; the same study (UKISS) suggests hormonal treatment might improve long-term developmental outcome compared with vigabatrin in infants with no identified underlying cause

### A2-D05 (PMID 24225340) - OVERSHOOT

- Quote found: EXACT.
- Reason: Source hedges: mutated patients 'tend to' show worse psychomotor course (severe SQPS 26% vs 0%, untested) while last DQ/IQ did not differ significantly (53.4 vs 42.9, lower in SCN1A-). Epilepsy contrasts (p .04, p .02) carried.
- Suggested wording: developmental effect: tendency to worse clinician-rated psychomotor course in SCN1A-positive (severe SQPS 26% vs 0%, no test reported; gait abnormal 77.5% vs 44%, p .017), with no significant difference in last DQ/IQ (53.4 vs 42.9); association: the authors describe the discordance by genotype as a tendency (epilepsy tends to be less severe, psychomotor course tends to be worse), not as a tested finding

## SUPPORTED triples that carry a caveat worth reading

These are SUPPORTED: the proposition is carried by the source. The caveat records a text-versus-table discrepancy in the source, a computed figure, or something the source prints that the proposition does not carry.

- **A2-A09**: The 229/129 denominators are printed for the seizure outcome (same responder/non-responder groups); the abstract prints no separate n for the VABS comparison.
- **A2-A10**: 'Five categories' is inferred from F[4,354] (4 between-group degrees of freedom); the abstract does not name the categories.
- **A2-B02**: 126/175 (72.0%) is a correct computation from Table 1; the text never prints 72.0% (Figure 3 lower panel presumably does; not verifiable as text).
- **A2-B06**: The anchor sentence carries the overall 76%; the responder-specific 40/62 vs 47/52 comes from Table 4 cells (22, 40, 5, 47), which I verified. Table 4 row would be the exact anchor.
- **A2-B07**: Verified: Table 2 prints RR 4.2 (1.6-11.0) on both the GDD->DRE and DRE->GDD rows; 58%/14% = 4.1 fits the first, 82%/34% = 2.4 fits the second. The proposition's observation is correct.
- **A2-B08**: Text says all nine genetic IESS infants had GDD; Table 1 prints G 8 (100%) with one death. Proposition records both.
- **A2-B12**: Source sentence is comparative ('...than treatment with VGB'); the proposition drops the comparator. The PubMed title carries '[RETIRED]' (guideline retired by AAN), not mentioned in the proposition.
- **A2-C01**: Open-label drug-resistant epilepsy: text prints 23% vs 50%, Table 3 prints 3 (25) vs 6 (50) (3/12 = 25%, 3/13 = 23%). Proposition follows the text. Similar text/table disagreement for open-label neurodevelopmental delay (text 20%/30%, Table 3 17%/25%), not quoted by the proposition.
- **A2-C03**: Composites are null as stated. Not carried: Table 2 36-month drug-resistant epilepsy counts 13/28 (vigabatrin) vs 14/21 (placebo), untested; Table 3 Vineland-II subdomain multivariate test at 36 months p 0.0495 (unadjusted; the authors conclude no difference and warn against definitive statements). The adaptive composite point estimate is against the drug (-6.77).
- **A2-C04**: Group sizes at 36 months are in Table 2 (watchful waiting 11 of 65; vigabatrin 28; placebo 22; straight-to-open-label 4), so 'not in the held locators' could be filled. Watchful-waiting group is genotype-enriched for TSC1 (36% vs 4% in the vigabatrin arm), which the source flags.
- **A2-D01**: Abstract prints 13/17 (76%) seizure free within the first year; Results text prints 14 (82%). Proposition says 'most' and quotes neither.
- **A2-D07**: 'Group-level discordance' is the proposition's label; the source reports the two trends separately and its between-individual predictor analysis (D06) is concordant (worse baseline epilepsy -> worse adaptive outcome). Baseline and follow-up developmental ratings use different instruments (clinician Likert vs ABAS-3-derived), and the authors note a floor effect.
- **A2-D09**: Table 2 later-diagnosis severe-profound 14 (45%) vs text 13/31 (42%) (recorded by the proposition). Also Table 3 neonatal SCB 8 + 12 = 20 while Table 2 prints 21 given SCB in the neonatal period; Table 2 'Normal 13 (45%)' is 13/31 = 42%.
- **A2-D10**: The proposition quotes the text (13/31, 42%); Table 2 prints 14 (45%) and attaches the p 0.049 (adjusted) to the three-category development row. Authors add that the prompt group probably lacked the most severe end (no markedly abnormal neonatal EEG).

## Artefacts read

All downloads are in `/tmp/claude-1000/-home-desktop-legend-development/9400b253-25a0-4b03-8822-96361325fc16/scratchpad/audit_A2/raw/` (outside the repository), plain-text dumps in `.../audit_A2/text/`, the matcher in `.../audit_A2/tools/match_quotes.py`, its report in `.../audit_A2/match_report.txt`. No script or intermediate file was placed in the scratchpad root. Routes: NCBI E-utilities efetch (db=pubmed and db=pmc) and Europe PMC REST (search lite and fullTextXML), called with no e-mail, tool or contact parameter. No bot check or refusal was met.

| File | PMID | PMCID | Route | Bytes | SHA-256 |
|---|---|---|---|---|---|
| `epmc_ft_24225340_PMC4225757.xml` | 24225340 | PMC4225757 | Europe PMC REST /PMC4225757/fullTextXML (open-access full text) (used for a verdict) | 88082 | `47acdd695e979bf673163d5db1c3057278589f14eb4cedcd2b2f16b162c74d35` |
| `epmc_ft_31929713_PMC6942552.xml` | 31929713 | PMC6942552 | Europe PMC REST /PMC6942552/fullTextXML (open-access full text) (used for a verdict) | 14496 | `f50efab70799889743d1ed3028619b0bc3e12869a2006d0892d60a9bb521bd89` |
| `epmc_ft_33180985_PMC7898885.xml` | 33180985 | PMC7898885 | Europe PMC REST /PMC7898885/fullTextXML (open-access full text) (used for a verdict) | 136579 | `e833f387efc3a5ed767ad2250b9c8a06805f9be700a33dfebc63e4b7a5a4bd8f` |
| `epmc_ft_34623615_PMC8498980.xml` | 34623615 | PMC8498980 | Europe PMC REST /PMC8498980/fullTextXML (open-access full text) (used for a verdict) | 59811 | `e5bc40761ac445997cdd33642c4dfabae7c4a20083fa2377eb3d137ce6549613` |
| `epmc_ft_35655584_PMC9157582.xml` | 35655584 | PMC9157582 | Europe PMC REST /PMC9157582/fullTextXML (open-access full text) (used for a verdict) | 110496 | `1b4698ccde34b064f8214b81c090b55531352b400da0cd9c80779fdfd2c99293` |
| `epmc_ft_38229878_PMC10789590.xml` | 38229878 | PMC10789590 | Europe PMC REST /PMC10789590/fullTextXML (open-access full text) (used for a verdict) | 100869 | `68db3721751a22347a33987731009c3e08a56f1a5e7137c3206643838c7c4f94` |
| `epmc_ft_38785332_PMC11296082.xml` | 38785332 | PMC11296082 | Europe PMC REST /PMC11296082/fullTextXML (open-access full text) (used for a verdict) | 130049 | `869710441f819a21d9d82eb2c48c546d174bcbe24ccaac3f577041560c396d03` |
| `epmc_ft_42081271_PMC13238869.xml` | 42081271 | PMC13238869 | Europe PMC REST /PMC13238869/fullTextXML (open-access full text) (used for a verdict) | 121437 | `0ec5cd2bc59113a88063e3fd20113baf2eff6e5ace3b0db0f9f082f1c4125f20` |
| `epmc_ft_42730593_PMC13570280.xml` | 42730593 | PMC13570280 | Europe PMC REST /PMC13570280/fullTextXML (open-access full text) (used for a verdict) | 68131 | `5c0b95bf568db83a58c230b877b3e8d9b6a0db48567247ad224c518424f4abff` |
| `ncbi_pmc_22689735_PMC3369510.xml` | 22689735 | PMC3369510 | NCBI E-utilities efetch db=pmc retmode=xml (PMC record) (cross-check copy) | 28283 | `08a9c2ab6bc7321fdfd57580e2f9538678bbe4eacfb89659fdd8d8b55db477b6` |
| `ncbi_pmc_23740534_PMC11194850.xml` | 23740534 | PMC11194850 | NCBI E-utilities efetch db=pmc retmode=xml (PMC record) (cross-check copy) | 12871 | `da1d64db1f107432766b336cfb6b6d9defe0e453a5b685cc5ba21266b6ae9260` |
| `ncbi_pmc_24225340_PMC4225757.xml` | 24225340 | PMC4225757 | NCBI E-utilities efetch db=pmc retmode=xml (PMC record) (cross-check copy) | 93130 | `6c436c0fd758e1774975d3b8d47d22089de2e340e961754e8f3e934d517f002a` |
| `ncbi_pmc_31929713_PMC6942552.xml` | 31929713 | PMC6942552 | NCBI E-utilities efetch db=pmc retmode=xml (PMC record) (cross-check copy) | 14294 | `410f0b96f9139397433a6d13bfabaf97f5fcfa7149b936da13c3406742a4d7fc` |
| `ncbi_pmc_33180985_PMC7898885.xml` | 33180985 | PMC7898885 | NCBI E-utilities efetch db=pmc retmode=xml (PMC record) (cross-check copy) | 134743 | `a605e9d8b1a6937e55497480a84e72c955a0bf484f325c0a54bd042ef55017e6` |
| `ncbi_pmc_34623615_PMC8498980.xml` | 34623615 | PMC8498980 | NCBI E-utilities efetch db=pmc retmode=xml (PMC record) (cross-check copy) | 59577 | `bec1afcbbc346898c24536fe1cd879da25f7be2eeec50903f9562b601c33e96c` |
| `ncbi_pmc_35655584_PMC9157582.xml` | 35655584 | PMC9157582 | NCBI E-utilities efetch db=pmc retmode=xml (PMC record) (cross-check copy) | 106579 | `7e11a78933e0a333363ac7d486163c080ac61bb8e5d1d5cbd17f2c594ce74ab8` |
| `ncbi_pmc_37638552_PMC10899525.xml` | 37638552 | PMC10899525 | NCBI E-utilities efetch db=pmc retmode=xml (PMC record) (used for a verdict) | 100897 | `1f7ccc1512f84732b16b87c1b8cbc75a102092df800365f893fbffa9071c97d0` |
| `ncbi_pmc_38229878_PMC10789590.xml` | 38229878 | PMC10789590 | NCBI E-utilities efetch db=pmc retmode=xml (PMC record) (cross-check copy) | 97944 | `1f61a53c99d02fb7d693aa7f7a01080377cc08db3e2272f13a851de858c6b826` |
| `ncbi_pmc_38785332_PMC11296082.xml` | 38785332 | PMC11296082 | NCBI E-utilities efetch db=pmc retmode=xml (PMC record) (cross-check copy) | 126949 | `f71821a3ae58229546bc7e3af321b6136dba4ff1ad2b881365ae389caed9f101` |
| `ncbi_pmc_41061327_PMC12554379.xml` | 41061327 | PMC12554379 | NCBI E-utilities efetch db=pmc retmode=xml (PMC record) (used for a verdict) | 100331 | `0c45146bf849fc98a6cb74d291623331f58584fce0c47cb97f6f529224d5173c` |
| `ncbi_pmc_42081271_PMC13238869.xml` | 42081271 | PMC13238869 | NCBI E-utilities efetch db=pmc retmode=xml (PMC record) (cross-check copy) | 135493 | `518ce336ab851249c98a744589b76651a3a3e1b8e2154d4820ef90a4ab5a1cfa` |
| `ncbi_pmc_42730593_PMC13570280.xml` | 42730593 | PMC13570280 | NCBI E-utilities efetch db=pmc retmode=xml (PMC record) (cross-check copy) | 72106 | `9c9b1f8f32a86b8b6e98cc6359b1f2cfb5da55f915898c174bcd24093b2ff0cc` |
| `pubmed_15009227.xml` | 15009227 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (used for a verdict) | 8357 | `238c6633dd37c1b32fe469fc28ddc08d699e91e201a0a28b0b1ccc7b526cb867` |
| `pubmed_15541450.xml` | 15541450 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (used for a verdict) | 8514 | `cfa7e92b243b33538f86305fc60f11c020fe5a6a4ff2fa165db07ea61a4e6694` |
| `pubmed_16239177.xml` | 16239177 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (used for a verdict) | 9381 | `458256c24f3e74580d17b8d44ed809cd3515a33304eae91ae390c569439e2f6e` |
| `pubmed_17201726.xml` | 17201726 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (used for a verdict) | 6649 | `5b8791e8c396e68960b352c80c4f484ed4c3bd3ed43395c1db361136cd2fa882` |
| `pubmed_19369101.xml` | 19369101 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (used for a verdict) | 7322 | `868341930ffdc44e49c1f82b0e5b8b5cf24197f653998319f5d6e0273e28ba68` |
| `pubmed_20457702.xml` | 20457702 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (used for a verdict) | 8504 | `39760b7bc7100524677c6bab25c618bc9367a29be7a168c0cf11111258837f60` |
| `pubmed_21668442.xml` | 21668442 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (used for a verdict) | 8784 | `d244f9335abefadc1c4840fa046520be8cbea8cc5d1fca6640f8d5ecfbde2c4f` |
| `pubmed_22689735.xml` | 22689735 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (used for a verdict) | 18842 | `12b40e29928a9fc8929b84c6bf17f0eb2099bb4fd57f769aa404682d7050a948` |
| `pubmed_23740534.xml` | 23740534 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (used for a verdict) | 51756 | `4ba629c260f7ac04e16116ef21d5005387c6bc8bfd9de316f9a5701894e58f21` |
| `pubmed_24225340.xml` | 24225340 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (cross-check copy) | 21520 | `1da5cf7eb37fdbe996ddfd78a2914df7f20d66fc51b9716685113b1049644e97` |
| `pubmed_25880994.xml` | 25880994 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (used for a verdict) | 11522 | `a6f6e4700a6485c1b7ba68371ccc2594bfaa16e252651b8bafe67a2229f2431d` |
| `pubmed_27838190.xml` | 27838190 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (used for a verdict) | 14411 | `cbf6240184effdeda12eea4534e93bba6271b636bd19f14ed70b2c8e43c20838` |
| `pubmed_29750338.xml` | 29750338 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (used for a verdict) | 11241 | `9854e573f9e342c317debed944a69236716adbc40e08cb6843960c96be9ea23a` |
| `pubmed_30236380.xml` | 30236380 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (used for a verdict) | 40581 | `81e9f8a795f56a50e4d80ebdb783cc0823b370f2bec86d9d6ea910f6279f59d4` |
| `pubmed_31929713.xml` | 31929713 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (cross-check copy) | 5511 | `7103a1adebbe3b54fee083fa32949126caea1e2a04be5888c1ddeb0b7bbdd3b8` |
| `pubmed_33180985.xml` | 33180985 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (cross-check copy) | 32347 | `3ad85d316e3d918cef4812620e80a005912e7be778e5f0cef8edd0f3ddb2fbed` |
| `pubmed_34623615.xml` | 34623615 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (used for a verdict) | 20133 | `b84fe3758fb2ba6ac8610906521242a78f974de5a15d907862accfc15ea9772f` |
| `pubmed_35655584.xml` | 35655584 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (cross-check copy) | 285168 | `8f9e706512aa1135d873eb1dcbe324ee5b19618a4c82aab3828c8a7d5c2ef8e7` |
| `pubmed_36621063.xml` | 36621063 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (used for a verdict) | 13905 | `0b363a9b0ee1baa9cad185661ad05bd24130547f409b4717a2099a9759bd1de4` |
| `pubmed_37099824.xml` | 37099824 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (used for a verdict) | 13341 | `e9c72ed786fd0672c5788ea7c3f79237ef7c90862c62652ea3a4eac3de83876d` |
| `pubmed_37638552.xml` | 37638552 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (cross-check copy) | 20054 | `fc060869b22f3fbb36fb946554de120b9a2d5184e2f18631c42c2c818be10195` |
| `pubmed_38229878.xml` | 38229878 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (cross-check copy) | 22323 | `94925fbdeaeeb9410f37325061858e06b8e20bb05fdc5e90279c09090f297ae6` |
| `pubmed_38785332.xml` | 38785332 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (cross-check copy) | 24060 | `a29c4cf737f8daabe02e4384eb78cd9d9a94cb717101eda5a804e9b06dccea48` |
| `pubmed_41061327.xml` | 41061327 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (cross-check copy) | 28416 | `1e811d0a5b139f4f7d87990c2e067d937f25eab2d92f17336580c17c2604562f` |
| `pubmed_42081271.xml` | 42081271 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (cross-check copy) | 31326 | `c4f8ee2b8a39a40c747d61fc6efbb42d202b04e72cfd52424add067ce0d4b83c` |
| `pubmed_42610455.xml` | 42610455 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (used for a verdict) | 34698 | `c9bc0166dccbc25d0348aef0484f39ae09e1f76872ec4b5efd9370b9396a83a7` |
| `pubmed_42730593.xml` | 42730593 | - | NCBI E-utilities efetch db=pubmed retmode=xml (PubMed record incl. abstract) (used for a verdict) | 14908 | `248d5ce31061d51ba43f067a98c4c97820b93f513890835cb4112ac2d8c8f8ca` |

Europe PMC `search` metadata responses (one JSON per PMID, `epmc_search_<PMID>.json`, about 1 kB each) were used only to find PMCIDs and are kept in `raw/` but are not evidence artefacts.

## Reachability

- Every source was reached. Nothing is unreachable.
- Europe PMC `fullTextXML` answered HTTP 500 for PMC3369510 (Go 2012), PMC11194850 (Hancock 2013), PMC10899525 (Bebin 2023) and PMC12554379 (O'Kelley 2025); these are not in the Europe PMC open-access subset. NCBI efetch db=pmc returned the full author manuscripts for Bebin 2023 and O'Kelley 2025 (used for C02-C04); for Go 2012 and Hancock 2013 it returned front-matter-only records, which was sufficient because both quotes are abstract-level and were matched in the PubMed record.
- No PDF was needed: every quoted fragment was matched in XML text, including the Jonsson 2024 Figure 3 caption.

## Reading the TSV

Columns: `triple_id`, `source_id`, `verdict`, `quote_found_as`, `artefact_route`, `artefact_sha256`, `justification_max40_words`, `suggested_wording_if_not_supported`. Where two artefacts were used for one triple (B02, B06: abstract anchor plus full-text table), both routes and both hashes are given, separated by ' ; '. The suggested-wording column is empty for SUPPORTED rows.

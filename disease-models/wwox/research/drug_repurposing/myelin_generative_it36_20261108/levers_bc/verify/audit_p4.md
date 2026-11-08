# Blind audit of IT36 P4 B/C items (verify/items.md)

Auditor: independent blind verifier (Sonnet 5.5). Input: items.md only; output/, READMEs, BRIEF and unguided_a were not opened.
Date of checks: 2026-11-08. Routes used: PubMed tools (abstracts), NCBI efetch of PMC XML (PMC9966820, PMC10534456, PMC3044866, PMC5117236, PMC7237703, PMC2628490, PMC3906126, PMC13343157, PMC8649866), held text under files/fulltext (PMID33914858 operator-supplied txt and OUP print txt; PMID34747138 and PMID42422765 PMC XML), ChEMBL REST, HGNC REST, Europe PMC REST search. No 403, reCAPTCHA, Cloudflare or bot check met on any route. No e-mail or contact to any service. No repository test, LINT or gate run.

Depth key: FT-text = full text of the PMC/held record read as text, figures and tables not viewed. ABS = abstract only (PubMed record). "Locator" = verbatim string found in the source.

Note on PMC3044866 (Rinholm, N12/N13): the PMC record returned by efetch is a 3.4k-character stub, so the paper's full text was NOT reachable by me either; N12/N13/H2 stay at ABS.

---

## Part 1: evidence rows

| Item | Verdict | Depth | Verbatim locator found / finding |
|---|---|---|---|
| N01 | SUPPORTED | FT-text | "Only Dko mice that received Triac during the first 3 postnatal weeks showed a full normalization of PV+ cell numbers in retrosplenial ... and somatosensory cortex ... as well as normal myelination in the corpus callosum assessed by FluoroMyelin". mIPSC: "Triac-treated Dko mice showed fully normalized mIPSC frequencies". "3-5 mice per experimental group" present. Detail the row leaves out: the effective arm is Triac 400 ng/g bw (low arm 50 ng/g bw); the 10-week readout follows P1-P20 injections. |
| N02 | SUPPORTED (nuance) | FT-text | "in Dko mice that received Triac only between postnatal week 3 and 6, myelination was not improved while a partial recovery of PV+ immunoreactivity could still be detected" (window P22-P42). "Mechanism unexplained": the authors say "still elusive" but offer two hypotheses (down-regulated, still unidentified Triac entry systems in mature CNS; or a closed sensitivity window). The row's limit is accurate but could name both. |
| N03 | SUPPORTED | FT-text | "Dko mice exhibited a highly reduced number of PV+ cells in both regions". P12 matches the P1-P11 treatment/P12 readout of Fig. 1 (stated in the Introduction of the paper). |
| N04 | SUPPORTED | FT-text | "The high concentration of Triac needed for effective normalization of brain parameters in our mouse model resulted in a fully downregulated HPT axis with Tshb transcript below the detection limit". Hepatic/renal: high-dose Triac gave "similarly elevated Dio1 levels as found in Dko mice" (signs persist, not newly induced). Row omits a decisive sentence from the same passage: the first human trial's average dose was 38.3 ug/kg/day, "in the same range as the low Triac dose (T(50)) used in this study", and the low dose "had only little beneficial effects on brain parameters". See Misses. |
| N05 | SUPPORTED | FT-text | "This Triac trial was not designed to detect any impact of the treatment on neurodevelopmental outcomes in human MCT8 deficiency although a trend towards neurodevelopmental improvement was noted in a subset of patients in an exploratory analysis." "46 AHDS patients (median age 7.1 years) ... 12 months" confirmed. Describes the first trial only (see Misses on the 2025 EU approval). |
| N06 | SUPPORTED (nuance) | FT-text | "TG68 rescued the cytokine differentiation block almost completely". 12 DIV confirmed for the cytokine experiment (Fig. 3). Nuances not in the row: TG68 was used at 10 uM (lowest effective dose; 1-50 uM tested) and the differentiation medium of every arm already contains 50 nM T3; the source prints "no difference ... compared to cultures unexposed to cytokines (p = 0.0316)", a p value that reads as a difference (internal inconsistency in the paper); the authors state the IS25 and TG68 "efficacy profiles" differ. |
| N07 | SUPPORTED | FT-text | "Preliminary investigations have revealed the polypharmacology of both compounds tested in this study and, most importantly, the significant activity of TG68 on AMPK activation." Same paper's abstract: effect may be "mediated by secondary mechanisms such as AMPK activation". |
| N08 | SUPPORTED | FT-text | "Cytokine exposure generated a reduction in the number of early-mature OLs in the cultures not rescued by T3". The paper's own framing is that inflammation raises the T3-inactivating deiodinase D3 (local tissue hypothyroidism), i.e. the natural ligand fails because it is degraded, not because the receptor is blocked; the row's "context where the natural ligand is useless" is correct but the mechanism is available in the source. |
| N09 | SUPPORTED for the quote; INV-12 clause UNVERIFIABLE | FT-text | "OPCs express both TRalpha and TRbeta1 [45], the latter believed to be the isoform chiefly responsible for T3-mediated differentiation induction". I did not open INV-12 (outside my input), so the "rodent OPCs alpha-leaning" half is not checked. |
| N10 | SUPPORTED | FT-text | "the differentiation medium containing CNTF, NAC, and T3, the main trigger of OPC differentiation, which occurs at 12 days"; Methods give 50 nM T3 plus 1x B27 and 1x N2 in that medium. |
| N11 | SUPPORTED | FT-text | "most thyromimetic drugs proposed for the promotion of OPC differentiation in demyelinating diseases have not passed clinical trials, such as GC-1, which was stopped at phase one, and KB2115 (Eprotirome), terminated at phases 2-3". ChEMBL agrees at indication level (sobetirome, adrenoleukodystrophy, phase 1; molecule max_phase 2.0 in ChEMBL, a different field). |
| N12 | SUPPORTED | ABS | "we show that a low glucose concentration reduces the number of oligodendrocyte lineage cells and myelination. Myelination is rescued when exogenous l-lactate is supplied." Sox10-GFP cultured cortical slices confirmed. Rescue by lactate is in the abstract but not in the row finding (it is in H2). |
| N13 | SUPPORTED | ABS | "oligodendrocytes in the white matter of the rat cerebellum and corpus callosum take up lactate via monocarboxylate transporters (MCTs), which we identify as MCT1 by confocal immunofluorescence and electron microscopy". |
| N14 | SUPPORTED as quote; UNDERSHOOT in use (misleading as a counter to an analogue lever) | ABS + FT-text (PMC5117236) | "but did not affect hypomyelination in older larvae" refers to T3. The same abstract says "TH analogs and clemastine partially rescued the hypomyelination in the CNS of mct8-/- larvae", and the Results state the analogs (TRIAC, DITPA) rescued oligodendrocyte number in older larvae ("even after brain damage occurs") while T3 did not, because T3 cannot enter after the 6-dpf stage. So in zebrafish the closing window applies to the hormone, not to the MCT8-independent analogues, which is the opposite of what N14 contributes to H1 (analogue lever, window closes). |
| N15 | SUPPORTED | ABS | "A recurrent observation in clinical trials is the absence of neurological improvement." |
| N16 | SUPPORTED | ABS + FT-text (PMC2628490) | "Unexpectedly, these mice assemble normal amounts of myelin." Full text: adult Emx-Cre Nrg1 null (4 months) "fully myelinated (not shown)"; Nestin-Cre nulls die ~16 h after birth, so the postnatal CNS myelin in those is not assessable. |
| N17 | OVERSHOOT (age scope missing) | ABS + FT-text | Locator verified in abstract. Full text: the CNP-Cre ErbB3/ErbB4 double mutants "died in the second postnatal week" and myelinated normally "at least up to postnatal day P11. Although we can not rule out phenotypic differences at later stages". The row's "not required for developmental CNS myelination" is therefore established to P11, i.e. before the P13-P17 window the WWOX material concerns; the row's limits do not state this. |
| N18 | SUPPORTED | ABS | "the WW1 domain of WWOX binds to PPXY motifs located within the ICD of ErbB4 in a physiologically relevant manner". Same abstract: WW2 does not bind PPXY motifs but "augments the binding of the WW1 domain". Fine for the bridge row. |
| N19 | SUPPORTED (nuance) | ABS | "Wwox interacts with the ErbB4 receptor, reduces nuclear translocation of the cleaved intracellular domain of ErbB4" is a background sentence of the abstract (earlier work); this paper's own data are IHC association in 556 breast cancers and in vitro association of Wwox with JM-a CYT-1/CYT-2. The row's "in cancer material" is acceptable but the nuclear-translocation clause is not a result of this paper. |
| N20 | SUPPORTED | search (reproduced) | PubMed "Wwox thyroid hormone": 1 hit, PMID34533693, a Chinese-population GWAS: "rs79508321 in WWOX ... related to circulating T3 level" under the "suggestively significant" threshold. A wider string (WWOX AND thyroid/triiodothyronine/thyroxine/deiodinase) gives 6 hits: this GWAS, four thyroid-cancer papers and one WOREE neuroimaging review noting WWOX expression in thyroid; none concerns thyroid-hormone handling in neural cells. |
| C01 | SUPPORTED (open point stays open) | held text, Methods | "maintained in co-culture medium (DMEM containing B27 and N2 supplements, 5 mg/ml N-acetyl-cysteine, 5 mM forskolin, penicillin-streptomycin)" (both held copies). Same Methods name T3 explicitly only for the spheroid protocol ("40 ng/ml T3"), not for the co-culture. Whether B27 carries T3: one open-route statement found (PMC13138590: B27 "without vitamin A" analysed by LC/MS and ELISA, "no biologically relevant concentrations of T3 were found across at least five batches (data not shown)"); this is a different B27 variant and unshown data, so the row's "not verified" is the right state. |
| C02 | SUPPORTED | held text | "5 mg/ml N-acetyl-cysteine, 5 mM forskolin" present verbatim in both held copies (the units look mis-typeset in the source, as the row says). |
| C03 | SUPPORTED | held text, search | Strings glucose/glycemi/hypoglyc in the operator-supplied txt: 4 matches, all buffer or ACSF recipes ("10 glucose"; sucrose solution). No blood-glucose result. Supplement not searched (as stated). |
| C04 | SUPPORTED | held text + PMC13343157 | "Early neuronal hyperexcitability was suppressed following treatment." (abstract). Vector given to Wwox-null mice, efficacy window P1-P5. "mosaic": 0 hits. |
| C05 | SUPPORTED (nuance) | held text | "oligodendrocyte-specific WWOX expression driven by the MBP promoter resulted in weak expression and no phenotypic improvement". The sentence continues "demonstrating that restoration in this lineage alone is insufficient": the authors draw the inference the row declines to draw. The row's "not a test of oligodendrocyte-directed restoration" is a fair reading of the confound but should quote the authors' own conclusion next to it. |
| C06 | SUPPORTED | held text, search | "mosaic": 0 hits; "neighbo": 0 hits in PMC13343157 and in the held r2 XML. |
| C07 | SUPPORTED | held text | "Wwox-null and AAV9-hSynI-EGFP-injected mice were hypoglycemic from the second week until they succumbed". Myelin readout P17 (MBP IF, EM corpus callosum, n = 3) confirmed. The paper concludes the effect on myelination is "non-cell autonomous". |
| C08 | SUPPORTED | held text | "AAV9-hSynI-mWwox- or AAV9-hSynI-hWWOX-injected mice had normal blood glucose levels when compared to the wild-type mice (Appendix Fig S1C and D)". |
| C09 | SUPPORTED, scope-limited | held text, search | "lactate": 0 hits in PMID34747138 held text and in PMC13343157; "glycogen"/"brain glucose" hit only in reference lists. Holds for these two papers only (see H2). |
| C10 | SUPPORTED | ABS | "Striatal transcriptomic profiling revealed a reactive astrocytic signature along with coordinated downregulation of genes involved in oligodendrocyte function, myelination, and galactolipid biosynthesis." The abstract also reports "selective reductions in myelin-enriched lipid classes, including hexosylceramides and ethanolamine plasmalogens" by lipidomics with no region stated; the row does not mention this and it is the most direct myelin-composition finding in that abstract. |
| C11 | SUPPORTED | ABS | "diffusion MRI revealed selective microstructural abnormalities confined to the dorsolateral striatum". |
| C12 | SUPPORTED | ABS | "chronic L-lactate supplementation initiated during early postnatal development partially rescued motor deficits in young adult" Glut1 mice. |

---

## Part 2: hypothesis propositions

### H1 (thyroid-hormone lever)
| Proposition | Verdict | Evidence |
|---|---|---|
| Stage pattern in Mct8/Oatp1c1 Dko: OPC share up, mature OLs down at P12, P30, P120 (PMID37307933) | SUPPORTED, ABS | "Dko mice exhibited at all analysed time points an increased portion of OPCs and a reduced number of mature oligodendrocytes ... indicating a differentiation blockage". Full text not reached (not in PMC). |
| Fewer PV interneurons (N03), window P1-P20 vs P22-P42 (N01/N02) | SUPPORTED | see Part 1 |
| "a hormone rescue lost in older zebrafish larvae (N14)" used for an analogue lever | UNDERSHOOT / misapplied | N14 is T3; analogues still rescued in older larvae (see N14). The conflict between zebrafish (analogue works late) and mouse (analogue fails late, N02) is not in the proposition, and bears directly on the claimed "narrow window". |
| Receptor-beta ligand effect on OPCs in vitro (N06) | SUPPORTED with nuance | micromolar dosing; T3 present in all media; polypharmacology (N07). |
| Identity: tiratricol CHEMBL41632, liothyronine CHEMBL1544, sobetirome CHEMBL107400, DITPA CHEMBL2348292 | SUPPORTED (ChEMBL REST) | CHEMBL41632 TIRATRICOL (max_phase 3.0; synonyms Triac, T3-acetic acid; MoA thyroid hormone receptor agonist); CHEMBL1544 LIOTHYRONINE (4.0); CHEMBL107400 SOBETIROME (2.0; GC-1, QRX-431); CHEMBL2348292 3,5-DIIODOTHYROPROPIONIC ACID (2.0; Ditpa). All four identifiers match the names. |
| "TG68 and IS25 absent from the catalogue" | SUPPORTED for ChEMBL | molecule search for TG68 and IS25 returns 0 records. (The internal catalogue was not checked.) |
| Tiratricol and DITPA act "without MCT8-dependent entry" (introduction of PMID36834863) | SUPPORTED | abstract: "thyromimetic, MCT8-independent compounds Triac ... and Ditpa". The zebrafish paper's text adds that the route is "not-yet identified transport systems", relevant to N02 (entry may be down-regulated in mature CNS). |
| Sobetirome "the best-known receptor-beta-selective analogue" | SUPPORTED | "one of the best characterized TRbeta1-selective TH analogs"; abstract "the best-known TRbeta1 synthetic ligand, GC-1". |
| IS25 "a receptor-beta agonist of nanomolar potency" | OVERSHOOT (mild) | source: "IS25 is an agonist of TRbeta with an EC50 of 448 nM". Sub-micromolar, hundreds of nM, and the culture work used 1-50 uM. "Nanomolar" is literal but suggests higher potency than the figure. |
| "sobetirome stopped at phase 1; eprotirome terminated" | SUPPORTED | N11; ChEMBL indication-level phase 1. |
| "seizure effect mixed per INV-12 (not re-read)" | UNVERIFIABLE (not opened by me) | |
| Counter: "nulls die at 3 to 4 weeks, narrow window" | NOT CHECKED | no source in the item set states it; the Wwox papers I read say "premature death"/"postnatal lethality" without a week figure in the passages I searched. |
| Counter: WWOX has no thyroid-hormone link (N20) | SUPPORTED, one-string absence (see N20; a second string also found nothing neural) |
| Counter: Trials show "absence of neurological improvement" (N15) | SUPPORTED (review abstract) |
| "No dose" | consistent | the item states none; the dose context (N04 note above) is available in the source and is missing. |

### H2 (energy/lactate lever)
| Proposition | Verdict | Evidence |
|---|---|---|
| Low glucose lowers OL-lineage number and myelination in cortical slices, rescued by lactate; white-matter OLs take up lactate by MCT1 | SUPPORTED, ABS | N12/N13 loci. Concentrations, controls, n not read. |
| Glut1 haploinsufficiency lowers brain glucose, glycogen and lactate; striatal myelin-gene downregulation; "motor-only lactate rescue" | SUPPORTED, except "motor-only" = OVERSHOOT (mild) | abstract: "global decrease in glucose, glycogen, and lactate levels across multiple brain regions"; rescue is stated for "motor deficits"; the abstract does not say other readouts were negative or untested, so "only" is not in the source (the row C12 phrases it correctly). |
| "brain energy was never measured (C09)" in WWOX | OVERSHOOT of an absence claim | C09 is a lactate string search of two held texts. The claim as phrased (in "main_counterevidence") reads as field-wide. A second route (PubMed: Wwox AND brain/neuron AND glycolysis/lactate/glucose metabolism/mitochondria; 11 hits) shows PMID42909904 (2026, Drosophila neuronal wwox knockdown in an Abeta model: elevated LDH expression and increased lactate) and a WWOX metabolic review (PMID36271927: WWOX-HIF1alpha, Warburg effect). Neither measures brain energy in a Wwox-null mouse, so the narrow claim stands, but it needs the scope "in the two vector papers read". |
| "WWOX-side lactate points up not down" | partly SUPPORTED | PMID42909904 (fly, neuron knockdown, Abeta background) reports raised lactate, consistent in sign; the module rows named in the item were not opened. |
| Hypoglycaemia from week 2 vs myelin at P17: order unset; bundled rescue (C07/C08) | SUPPORTED | |
| Lactate "catalogue CAT:EC:01903" | UNVERIFIABLE | internal catalogue not opened. |

---

## Part 3: comparison claims

| Item | Verdict | Check |
|---|---|---|
| ALT1 | SUPPORTED (abstract level) | PMID24727982 abstract is the optogenetic premotor-cortex study: "neuronal activity elicits a mitogenic response of neural progenitor cells and OPCs, promotes oligodendrogenesis, and increases myelination". The comparison to INV-06 (X0, E11) was not checked (INV-06 outside my input). |
| ALT2 | PARTLY SUPPORTED; the "unguided overshoots" half is itself an OVERSHOOT | Row 2 not supported: confirmed (C04/C06). But on the MBP-promoter arm the source says in so many words "demonstrating that restoration in this lineage alone is insufficient"; calling the unguided README line an overshoot ignores that the paper's authors state it; the accurate position is "the paper states insufficiency, resting on an arm with weak expression". |
| ALT3 | SUPPORTED | PMID37307933 abstract matches ("differentiation blockage", increased OPC portion); PMID36732069 abstract also read: GAMT/creatine deficiency, "reduced mature oligodendrocytes and delayed myelination in the corpus callosum", plus "altered AMPK signaling in the brain" (see Misses). Statements about INV-12 and the unguided run not checkable. |
| ALT4 | SUPPORTED | PMID42686079 points as in C10 to C12; PMID34747138 as in C07 to C09; C03 verified. The generalisation across regions in the unguided row cannot be seen by me, the correction itself is right. |
| ALT5 | SUPPORTED (abstract level) | "a reduced number of myelin sheaths that in turn exhibited an increase in length indicating a compensatory response", Dko mice. |
| ALT6 | UNVERIFIABLE | refers to INV-06 rows E08-E10 and the unguided table; not opened. |

---

## Part 4: bridge row

| Field | Verdict | Check |
|---|---|---|
| hgnc_a WWOX HGNC:12799; hgnc_b ERBB4 HGNC:3432 | SUPPORTED | HGNC REST: WWOX HGNC:12799 "WW domain containing oxidoreductase"; ERBB4 HGNC:3432 "erb-b2 receptor tyrosine kinase 4". |
| relation "binds the intracellular domain of", status observed_other_context | SUPPORTED | N18 (WW1-PPXY of ErbB4 ICD, biophysical, purified) and N19 (association, breast cancer, transfected cells). The relation holds for WW1 only; WW2 does not bind PPXY motifs. No neural/OL-lineage context in either; the row says so. |
| note: not a lead for the myelin need (N17) | SUPPORTED as a caution, but the supporting N17 has an age limit (P11) the note does not carry. |

---

## Counts

Part 1 (32 rows): SUPPORTED 30 (of which 8 with a stated nuance: N02, N06, N08, N19, C01, C05, C09 scope, N09 with its INV-12 clause UNVERIFIABLE), OVERSHOOT 1 (N17), UNDERSHOOT 1 (N14 in use). NOT_IN_SOURCE 0. UNVERIFIABLE whole rows 0 (one clause: N09).
Part 2: H1 11 propositions: 7 SUPPORTED, 1 UNDERSHOOT/misapplied (N14), 1 OVERSHOOT (IS25 "nanomolar"), 1 UNVERIFIABLE (INV-12 seizure statement), 1 NOT CHECKED (null lethality week). H2 6 propositions: 3 SUPPORTED, 1 partly (lactate sign), 2 OVERSHOOT (mild "motor-only"; absence claim scope), 1 UNVERIFIABLE (catalogue id).
Part 3 (6): SUPPORTED 3 (ALT1, ALT3, ALT4, ALT5 at abstract level = 4), partly 1 (ALT2), UNVERIFIABLE 1 (ALT6).
Part 4: all SUPPORTED, one caution.

Items whose headline changes: N14 (and the H1 use of it), N17 (scope P11), ALT2 (second half), H2 absence sentence "brain energy was never measured" (scope).

## What the items miss that changes their meaning

1. Zebrafish analogue rescue in older larvae (PMC5117236): TH analogues (TRIAC, DITPA) rescued oligodendrocyte number at 10 dpf and "even after brain damage occurs", while T3 did not. N14 is cited as a counter for an analogue lever; it is a counter for the hormone, and for the analogue it points the other way. H1's "narrow window" then rests on the mouse N02 alone, with a species discrepancy that should be written.
2. Dose-translation sentence in PMC9966820: the first human Triac trial dose (38.3 ug/kg/day) is "in the same range as the low Triac dose" in mice, the arm with "only little beneficial effects on brain parameters" (the effective arm was 400 ng/g bw, roughly an order of magnitude above, with a fully suppressed axis). N04 notes the barrier but not that the human regimen sits on the ineffective side. Authors' own suggestion: higher doses "even if ... signs of e.g., hepatic thyrotoxicosis are still present".
3. Tiratricol is no longer investigational in the EU: PMID40549098 (Drugs, "Tiratricol: First Approval", doi 10.1007/s40265-025-02197-7) reports first approval on 12 February 2025 in the EU "for the treatment of peripheral thyrotoxicosis in patients with MCT8 deficiency ... from birth". The indication is peripheral, not neurodevelopmental, which is consistent with N05, but the status line in H1 is missing it. ChEMBL still shows max_phase 3.0 for CHEMBL41632, so a ChEMBL-derived status would be stale.
4. N17 and the bridge note depend on assessment only to P11 in mice that die in the second postnatal week; the Nrg1 nulls (Nestin-Cre) die at ~16 h, so postnatal CNS myelin is not tested there at all. "Not required" is shown for adult Emx-Cre Nrg1 nulls and P11 double mutants.
5. In the cytokine experiment the natural ligand fails because inflammation raises the T3-inactivating enzyme D3 (the paper's framing). A WWOX hormone arm would have to show a comparable local hypothyroidism for T3 to be uninformative; N08 gives the result but not this reason. Also all arms of N06 contain 50 nM T3 in the medium, and TG68 was tested at 10 uM, so the receptor attribution is weaker than "receptor-beta prodrug" suggests (N07 partly covers this).
6. C01: B27 and T3 remains open, but a source exists that reports an LC/MS/ELISA check of one B27 variant (no biologically relevant T3, data not shown, PMC13138590); worth citing as a pointer, not as settled. The spheroid protocol of the same WWOX paper adds 40 ng/ml T3 explicitly, so organoid and co-culture arms differ in named hormone exposure.
7. Creatine deficiency (PMID36732069), cited in ALT3 only as a stage-pattern parallel, also reports "altered AMPK signaling in the brain" and TG68 activates AMPK (N07): a possible shared node between the energy lever (H2) and the thyromimetic off-target (H1) that no item mentions.
8. Rinholm (N12/N13) full text remains unreachable (PMC stub); the lactate-rescue statement is abstract-level in the items and in this audit.
9. C10-C12: the Glut1 abstract also states reductions of myelin-enriched lipids (hexosylceramides, ethanolamine plasmalogens) without a stated region; region and size are unknown, so "myelin findings were striatal" (H2 counterevidence) may be too narrow for the lipid data.
10. Authors' own interpretation in C05 (MBP-promoter arm "insufficient") and C07 ("non-cell autonomous" effect of neuronal restoration on myelination) should sit next to the confound statements, because both support the logic of the unguided relation the items are correcting.

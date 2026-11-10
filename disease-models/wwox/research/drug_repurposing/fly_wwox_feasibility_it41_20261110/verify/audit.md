# Blind audit, IT41 light queue (Wwox-loss Drosophila feasibility), verifier ic-v

Date of work 2026-11-10 (UTC, between 00:47 and 00:57). Task ORCH-IT41-20261109. Verifier did not read
`output/phase_note.md`, `README.md` or `consumer_delta.md` before these verdicts. Nine PMIDs claimed under `ic-v`
(39952983, 42909904, 26302329, 34210081, 26023770, 22681692, 26596173, 16007179, 26390919); in addition 21075834,
17395332, 30370248, 32899411 were opened as part of the absence checks (not claimed through the packet tool, which
was only run for the nine named in the producer's table; flagged here for the Orchestrator).
Labels: DATO / INFERENZA / IPOTESI. Depth stated per item. All source text was re-fetched by the verifier
(NCBI efetch db=pmc; figures and supplements from the open-data bucket; Europe PMC fullTextXML for fingerprints).

## Headline

* 12 decisive propositions: 8 SUPPORTED, 4 PARTLY (D04, D06, D07, D11), 0 NOT SUPPORTED as a whole, 0 UNVERIFIABLE.
  One clause inside D06 (the 2005 radiation-sensitivity phenotype and its rescue) is NOT SUPPORTED as a current datum.
* Three substantive errors, all from material that was in the producer's own search results or opened sources:
  1. **D06 / EV32 / EV33 / FE04 / FE07 / FE08**: the 2005 radiation-sensitivity phenotype of the DmWWOX1 mutant, and its rescue
     by fly or human WWOX, is not a reliable Wwox-loss result. PubMed lists an erratum for the 2005 paper
     (Oncogene 2006 Dec 7;25(58):7662; content not opened), and the 2011 paper PMID 21075834 (in the producer's own Q08 hit
     list) states that "background mutations, rather than the targeted Wwox mutations, were responsible for this phenotype",
     citing the authors' own "Know thy fly" (PMID 17395332) on background mutations after homologous-recombination targeting.
  2. **Resources row 23 / FE02 / D-level absence of "protein detection"**: a Wwox-specific antibody exists and was used. The 2015 paper
     that the producer opened used "anti-C-DmWWOX antibody" for Western blots and immunostaining (Methods, Western blot and
     immunostaining sections), and the 2011 paper reports "the absence of Wwox protein in both Wwox1 and Wwoxf04545 adult flies"
     (Results; Supp Fig S1 not viewed). "No Wwox-specific protein detection found" is false as written; only "endogenous protein
     in imaginal discs is too low to detect" is true (2015).
  3. **FE04 / FE06 omission of a sign conflict**: the two sleep datasets point in opposite directions in the light phase.
     Hypomorph f04545 (Kim 2025): day sleep down, day bout length down (fragmented), night sleep up. Neuronal or glial TRiP
     knockdown (Lucas-Clarke 2026): light-phase mean sleep-episode duration up and probability active-to-inactive up. The two are
     presented as one "day-night redistribution / increased sleep pressure" picture with a "second genotype" needed. They are
     two different genotypes by two laboratories already, with partially opposite light-phase readings.
* Conclusion impact: the feasibility conclusions that matter (F3: sleep is the only quantified loss readout, F4: rescue design,
  F5: abstain on subunit questions, no epileptic phenotype assumed) stand. What changes: remove the radiation phenotype from the list
  of published loss phenotypes and from the "only rescue" statement; correct the protein-detection absence; state that the sleep
  readouts disagree in sign in the light phase; the hypomorph is a protein-absent allele by western per 2011 (Supp Fig S1 unseen).
* Unreachable: BDSC and FlyBase stock/allele pages (see E); Supp Fig 6C of Lucas-Clarke (lifespan order of the hWWOX arm);
  Supp Fig S1 of the 2011 paper; the 2006 erratum text; S1 Fig and S4 Fig of O'Keefe 2015.

## A. Decisive propositions

Depth for each: partial_fulltext_read of the cited source by the verifier, with figures viewed where noted, unless stated.

| id | verdict | reason (digit by digit) |
|---|---|---|
| D01 | SUPPORTED | NCBI Gene 34090 (esummary re-run): Wwox, CG7221, 2L, "Orthologous to human WWOX" (Alliance, Jun 2026). Lucas-Clarke Results first section: "65% sequence similarity" and "16/16 ... DIOPT". My own alignment: 50.0 percent identity, 67.3 percent positives, so "65 percent similarity" is consistent with the scoring used there. "Single gene" rests on one esearch hit (Q04), acceptable. |
| D02 | SUPPORTED (value correction) | Methods: "loss-of-function mutant Wwox f04545 (BL18783)"; control w1118 is BL5905 (Methods). Fig 2A, viewed at the PDF's 2008-px image: mutant bar reaches 22 px of 324 px per unit = about 0.07, the three dots lie about 0.04 to 0.10. "About 8 percent" should read "about 7 percent (range of three replicates about 4 to 10 percent, read from the figure; no number in the text)". Three experiments: correct. qPCR was on whole flies (Methods), not heads; not stated by the producer. "Insertion" is not in the Kim paper (which calls it a deletion); it comes from the 2011 paper (PMID 21075834 Results: "Wwoxf04545, which carries a pBac insertion in exon 2"). Add that source. |
| D03 | SUPPORTED | Methods: males 2 to 5 days old, DAM, LD 12:12, 25 C, sleep measured on day 4 of LD (add this), backcrossed six times to w1118 (EV02 verbatim). Fig 2C read at 2008 px: day about 515 to 320 min, night about 535 to 650 min (producer: 500 to 310 and 520 to 650; control night is 535, not 520; both within reading error; the producer's own note about 560 in an earlier reading is also off). Fig 2E: free-running period about 23.5 h, 96.9 and 96.7 percent rhythmic, n = 32 control and **n = 30** for the mutant (legend), not 32 for both. Fig 2F: day bout length lower (**), night n.s. Not written by the producer in D03: day sleep bouts shorter (fragmentation). |
| D04 | PARTLY | Supported: TRiP.HMC03298 = BDSC 51747 (Supp Table 1A and 1B); neuronal sleep 0 to 5 d, glial 0 to 4 d control and 0 to 6 d knockdown (1B); lifespan and RING on females (1B); one RNAi line in assay rows (KK line appears only in 1A). Fig 1B viewed: neuronal median control about 57, knockdown about 42 (text "57 and 42 days"). Not stated by the producer: glial lifespan is milder (text: 70 versus 74 days, Fig 1D). Fig 2 viewed: neuronal mean sleep episode about 12 to 32 (light) and 18 to 40 (dark) min, probability active to inactive about 0.25 to 0.42 (light), matching. Glial episode-length effect is weak (padj 0.0258; light bars about 40 to 50 min). "Startle-induced climbing stays normal to day 28" is too strong: Fig 1C and 1E show no significant genotype effect with N = 3 to 6 vials of about 10 flies, wide error bars at day 28 (about 1.6 versus 2.6 cm), and the Discussion itself says the effect "may emerge later". Write "no significant genotype effect, low power". Supp Fig 2 legend adds: tim-GAL4 (clock) knockdown also raises sleep probability and **lengthens circadian period**; "period unchanged" is true for neuronal and glial only. |
| D05 | SUPPORTED (perimeter caveat) | Re-run 2026-11-10 00:53:54Z with NCBI esearch: Q05 string 0 hits, Q06 string 0 hits, Q07 string 3 hits (39952983, 18008369, 16007179), exactly as stated. PubMed tool search of the same seizure string: 0; (Wwox OR WWOX OR CG7221) AND Drosophila: 12 hits (the same 12 PMIDs, none a seizure, bang-sensitivity or NMJ study). Independent corroboration found by the verifier: the 2020 review PMID 32899411 (open, PMC7503973) states "No phenotypic analysis of Wwox mutants or knockdown flies has been reported in relation to EIEE" (date-limited to 2020). Perimeter: abstract-level strings under-retrieve. Q07 returned neither the 2011 Wwox-mutant paper (21075834) nor the 2015 paper (26302329) nor 42909904, so a 0-hit string is weak evidence. The claim should read "no study found in PubMed abstract strings, Europe PMC full-text strings (Q09, 46 hits, titles only) and one 2020 review, to 2026-11-10"; FlyBase phenotype annotations were not reachable. |
| D06 | PARTLY; second clause NOT SUPPORTED | First clause: 2015 Results (section "Requirement for WWOX tumor suppressor activity in vivo", **not the Discussion** as EV17 states) says Scrib-clone effects were obtained "where WWOX function is completely removed (trans-heterozygous for independent WWOX alleles)" with adult eyes scored (S4 Fig not opened by either of us). Viability of the homozygous HR allele is supported better by the 2011 paper (Drosophila homozygous for Wwox1 "are viable and fertile"; reviews: "surprisingly viable and exhibited no obvious phenotype", PMID 30370248). "Complete null": the 2015 allele WWOX2 is an "insertion mutation" allele; it is probably Wwoxf04545 (pBac in exon 2; the 2011 paper uses Wwox1/Wwoxf04545 trans-heterozygotes, and reports protein absent in both). Label as INFERENZA: "WWOX1/WWOX2 = null over strong insertion hypomorph". Second clause (radiation sensitivity, rescued by fly or human WWOX): superseded. See Headline 1. The abstract is accurate as an abstract; as a datum about Wwox loss it should not be carried. |
| D07 | PARTLY | Supported: neuronal Abeta42 background, females; knockdown median 41 versus 26 days (Fig 3A text), CRISPRa upregulation in Abeta42: 47.5 versus 29 days, climbing improved at day 14 and 21 (Fig 6). Overstated: "without it upregulation does nothing" was tested only for CRISPRa (survival 60 versus 58 days, n.s.; RING n.s.; Supp Fig 6A and 6B per text); hWWOX and dWwox cDNA were tested only with Abeta42, so no "no amyloid, no effect" statement exists for human WWOX. Glial overexpression had no effect even with Abeta42 (Supp Fig 6E and 6F). hWWOX lifespan figure is quoted "41 versus 51 days" with the order not stated; Supp Fig 6C not opened by me. The Ser14 and Tyr33 variants performed like wild-type hWWOX on climbing, and dWwox cDNA was better than hWWOX (Supp Fig 6D, text). Correctly kept out of the loss model. |
| D08 | SUPPORTED | Results, first section: knockdown (RNAi #1 and #2) and heterozygous alleles WWOX1 and WWOX2 suppress the GMR>egr eye phenotype (Fig 1C, 1D, S1 Fig). "Ectopic expression of WWOX alone does not result in any obvious cell death-induced phenotype" is **Results text citing S1 Fig**, not the Fig 1 legend (EV16 locator defect); S1 Fig not opened. Same Results paragraph: ectopic WWOX **enhances** the Egr phenotype (Fig 1E, 1F), which should be added to make "stress-dependent" a documented statement. "Developmental epithelial" is INFERENZA. |
| D09 | SUPPORTED | All three parts verified verbatim: Mib1 paper Results first section "Drosophila NMJ GluRs are similar to non-NMDA receptors including AMPA receptors" (citing Marrus 2004), Introduction "homologous to AMPA receptors (Menon et al., 2013)"; Miyashita Introduction "a single NR2 homolog, dNR2 ... Q721 ... a single NR1 homolog, dNR1 ... N631" and Results "more than 85% ... 119 out of 136 cells", "blocked by ... 20 mM Mg2+", "APV and MK801, significantly suppressed"; sleep paper Discussion "Nmdar1 (dNR1) and Nmdar2 (dNR2), are widely expressed in the adult brain [30-33]". Pupal cultured neurons, 3 to 4 days in vitro; adult-brain expression statement is a citation. Transfer, correctly labelled. |
| D10 | SUPPORTED | 2 to 4 day old males (Methods). Fig 2D viewed: total sleep LD about 720 to 540, DD about 495 to 225 min/day; Fig 2E: Nmdar1 mRNA about 50 percent, GluRIB, CanA-14F, CanB, RpL32 not lowered; n = 16 per group (2C, 2D) and n = 3 for qPCR. Fig 4B viewed: LD about 1135 to 915, DD about 935 to 680 min/day. Also true and not stated: line 104773 also lowers sleep (S2 Fig, day, subjective day, subjective night). MK-801: "In 16 flies with 0.1 mg/ml MK-801, 3 ones died during the sleep assay" is the dose-finding series (S3 Fig, n = 13 to 16, lower doses 0.01 and 0.03 mg/ml had no effect); Fig 4 groups were 32 control and 28 treated (so up to four flies fewer; this is an inference, not stated). The confound as the producer writes it is right. |
| D11 | PARTLY | Review text verbatim: "Amino acid Y288 in Drosophila is an essential component of the catalytic active site", "The orthologous tyrosine amino acid is position 293 in human WWOX"; abstract 26390919 verbatim "This modulation requires the enzyme active site of WWOX". My alignment confirms Y293 to Y288. The review is by the same laboratory as the primary paper (Lee, Choo, Richards, O'Keefe), so it is same-origin reuse, not independent confirmation; the column "class" lists both options without choosing. The 2015 primary paper is a genetic-interaction study with altered Wwox levels (increase and decrease) in mitochondrial-defect backgrounds, not a Wwox-loss readout; depth abstract only. |
| D12 | SUPPORTED | Own alignment (global, BLOSUM62 matrix from a local library file, gap open 11 and extend 1, own code in the scratchpad), NP_057457.1 (414 aa) against NP_001285735.1 (409 aa): 404 aligned columns, 202 identical = **50.0 percent** (producer 202 of 405), 272 positives = 67.3 percent, alignment length 419 (48.2 percent of alignment length). NP_609171.1 has the identical 409-aa sequence. P47 to P42, R54 to R49, Y293 to Y288 conserved; G372 to S367 not conserved. All four as the producer states. Kim 2025 Discussion: "49% amino acid identity", Lucas-Clarke "65% sequence similarity". Additional from my alignment, not in the producer rows: S14 aligns to S9, **Y33 aligns to C28 (not conserved)**; the first 14 residues are gapped (human MAALRYAGLDDTDSEDELPP versus fly MIA-----LPDTDSEDELPP), so low confidence is correct. |

## B. Resources (`resources.tsv`, 23 rows; numbering R01 to R23 by row order, used in evidence.tsv)

14 rows `confirmed_in_source`, 6 `catalogue_entry_only`, 3 `not_found`. Traced to the cited locator by the verifier:

* R01 BL18783: printed in Methods. TRACED. "Confirmed" means the number is printed, not that the stock is held; the row says so. Not overstated.
* R02 WWOX1: described "heterozygous null allele" (2015 Fig 1 legend) and as an HR mutation (2005 abstract). Null status is better sourced in the 2011 paper (absence of protein, embryos and adults). The 2005 phenotype is superseded (Headline 1). Add that source and the erratum.
* R03 WWOX2: "heterozygous insertion mutation allele" TRACED. Add the probable identity with f04545 as INFERENZA.
* R04 v22536 and R05 VDRC 108350: TRACED verbatim in 2015 Methods; R05 also in Supp Table 1A (P{KK108459}VIE-260B). KK line absent from Supp Table 1B assay rows: correct.
* R06 BDSC 51747 TRACED (Supp Table 1A and every assay row of 1B). Control BDSC 8622 and LacZ BDSC 8530 TRACED.
* R07 UAS-dWwox, R08 UAS-hWWOX and variants: "This study", attP2, chromosome 3 (Supp Table 1A); variants are hWWOX pSer14 mutant, pSer14 mimic, pTyr33 mutant (no Tyr33 mimic exists in the table). Status catalogue_entry_only is right. No availability.
* R09 ORF#1 and cDNA#1: "previously described [49 and 61]" TRACED; catalogue_entry_only right.
* R10 CRISPRa: BDSC 66561 (UAS-dCas9-VPR), 77229 (WwoxgRNA), 67539 (control gRNA) TRACED. The text says "2-fold"; "1.8" comes from an earlier dossier (Supp Fig 1, not opened by me).
* R11 sima:GFP BDSC 42672, R13 Xbp1 BDSC 60730 TRACED. R12 mito-roGFP2-Orp1 BDSC 67667 TRACED; use is in day-7 female wings, LV1 to LV2 intersection (Supplementary material, roGFP2-Orp1 imaging), so "wing veins" is right, and it is a neuronal knockdown readout (Supp Fig 2U, t = 3.221, N = 9 to 11).
* R14 drivers TRACED (elav-GAL4 BDSC 458 and 8765, repo-GAL4 7415, nSyb-QF2 51960, tim-GAL4 Stanewsky lab).
* R15 Y288F: catalogue_entry_only right; abstract and review only.
* R16 Nmdar1 lines: VDRC 37333, 104773, Dicer-2 60008 TRACED (Methods). The claim "104773 weaker and not significant at mRNA" is not in the text and the S2 Fig I opened (sleep data of 104773) shows significant sleep reductions; the mRNA panel (S2C legend) I could not read as a number. UNVERIFIED.
* R17 dNR1 EP3511, EP331, N631Q TRACED in text; no stock numbers.
* R18 DAM TRACED in all three. R19 Egr eye assay TRACED.
* R20 NMJ electrophysiology: heading-level, correct.
* R21 seizure assay `not_found`: consistent with D05 and with the 2020 review.
* R22 stock record `not_found`: reproduced (E).
* R23 `not_found` for "endogenous protein detection or tagged reporter": **WRONG for protein detection** (Headline 2). Replace with: "anti-C-DmWWOX antibody (rabbit polyclonal, described in earlier work, source of supply not stated) used for Western blot of ectopic WWOX and discs (2015) and for absence of protein in Wwox1 and Wwoxf04545 adults (2011, Supp Fig S1 unseen); endogenous protein in imaginal discs too low (2015); no GFP-tagged or T2A line found in opened sources".

Overstated status: only FE01 (below). No resource row claims "available".

## C. Amyloid separation

Correct. D07 is classed as transfer and "not a Wwox-loss phenotype"; EV11 is labelled `counter` and notes it is overexpression in an amyloid-toxic fly; EV12 states the no-amyloid arm; FE05 keeps amyloid out of the WWOX-DEE model. No overexpression or amyloid-context result is written as a loss result in decisive, evidence or feasibility. The loss rows D04 and EV09, EV10, EV13 use arms without Abeta42 (Supp Table 1B: LacZ partner, Figs 1 and 2). Two wording fixes only: D07 "without it upregulation does nothing" applies to CRISPRa only; EV11 quote begins "a similar rescue", and the order of the two medians is not given in the text (control first or treatment first is unclear; the legend and the paper call it a rescue).

## D. F3 to F5 (`feasibility.tsv`)

| row | verdict |
|---|---|
| FE01 | Label DATO is too strong next to FE02 (INFERENZA). "Public resources exist" should read "stock numbers are printed in papers; public holding not confirmed". The BDSC and VDRC numbers are plausible catalogue entries but were not seen in a catalogue. |
| FE02 | Right in direction, but its last clause ("no Wwox-specific reporter or protein detection was found") is wrong for protein detection (Headline 2). |
| FE03 | DATO, correct as a record of routes (Alliance 429 was not re-run by me). |
| FE04 | List contains the radiation phenotype as a published Wwox-loss phenotype: remove or flag (Headline 1). Add the sign conflict (Headline 3), the milder glial lifespan effect, and "climbing: no significant effect, low power". |
| FE05 | Correct and correctly labelled. |
| FE06 | INFERENZA, reasoning sound. Add that two genotypes from two laboratories already exist and disagree in the light phase, so the first task is to reconcile them (same background, same sex, same analysis pipeline) rather than to "reproduce". |
| FE07 | "No epileptic phenotype is assumed" is respected: no seizure, bang-sensitivity or electrophysiology claim is made, and these are proposals only. Fix: drop "radiation" from the readouts with source support. "Wing-vein ROS" is supported (Supp Fig 2U, females, day 7, neuronal knockdown). |
| FE08 | Right design logic. The statement "the 2005 rescue is abstract-only" must become "the 2005 radiation phenotype was later attributed to background mutations (2011), so no published rescue of any Wwox-loss phenotype exists". |
| FE09 | Facts correct (my alignment). Add Y33 to C28 not conserved, S14 to S9 conserved with a gapped N-terminus. Also name P47T and G372R as human changes and say that P47 and G372 do or do not conserve (done). |
| FE10 | IPOTESI, correctly labelled and correctly hedged (baseline Nmdar1 sleep effect; MK-801 lethality in the dose-finding series). A shared sleep readout also makes the epistasis table hard to read (both Wwox and Nmdar1 loss alter sleep, in partly opposite directions): add as a limit. |
| FE11 | Label DATO covers mixed content. "Single NR2" and "larval NMJ is non-NMDA" are DATO (verified). "Cannot discriminate AMPA from kainate at central synapses", "cortical burst firing", "drug effect on a human variant" have no evidence row and are INFERENZA. |

Receptor biology (single NR2, Nmdar1, larval NMJ receptors non-NMDA, Mg block): all verified (D09). Mg block: dNR2 has Q721, dNR1 N631 is sufficient for Mg block, NMDA currents blocked by 20 mM Mg2+ in pupal cultured neurons. Mg block of dNR1(N631Q) is the subject of that paper (not needed here).

## E. Absence claims, perimeters, stock pages

* Seizure or bang-sensitivity: re-run (Q05 string, NCBI esearch 00:53:54Z) 0 hits; PubMed tool and Europe PMC (46 and 47 hits, none a fly Wwox seizure study); corroborated by the 2020 review sentence. Perimeter adequate for the statement "none found in PubMed and Europe PMC searches and one review", not adequate for "none exists" (abstract-level strings missed the 2011 and 2015 Wwox-mutant papers; FlyBase phenotype annotations not seen).
* NMJ or electrophysiology of a Wwox mutant: Q06 string 0 hits reproduced; broader PubMed tool string (WWOX, fly terms, neuromuscular junction OR synaptic OR electrophysiology OR excitability) 0 hits. Same perimeter statement.
* Reporter or protein detection: not reproducible as an absence. The 2015 and 2011 papers describe an anti-C-DmWWOX antibody and Western detection (Headline 2). No GFP-tag, T2A-GAL4 or MiMIC line was found in the sources I opened (not searched in stock centres: unreachable).
* Own plain-curl attempts, default user agent, 2026-11-10 00:51Z to 00:52Z: BDSC `https://bdsc.indiana.edu/stocks/rnai/tripvalium.html?stock=51747` returned HTTP 403 (recorded as unreachable, no other BDSC route tried). FlyBase `https://flybase.org/reports/FBst0018783.html` returned HTTP 302 to `https://flybase.org/search/FBst0018783`, then HTTP 200 with a client-rendered "FlyBase HitList" shell of about 4.8 kB visible text and no stock content (same outcome as the producer's Q02). Not retried by any other route.

## F. Evidence rows (`evidence.tsv`, 35 rows)

Counts: checked 35; quote verbatim and at most 25 words at the cited source: 35 (3 of them, EV05 to EV07, are table rows flattened without cell separators, content identical to the cells; longest quote 22 words, EV29); proposition carried correctly: 29; defective: 6.

Defects:
* EV16 locator "Fig 1 legend" should be "Results, first section (cites S1 Fig)".
* EV17 locator "Discussion" should be "Results, section 'Requirement for WWOX tumor suppressor activity in vivo'".
* EV07 proposition id R09 should be R08 (UAS-hWWOX is row 8; row 9 is ORF and cDNA).
* EV14 proposition ids R03;R10: R10 is CRISPRa; the quoted constructs are rows 2, 3 and 9 (R02;R03;R09).
* EV33 proposition id R10 should be R02 (the HR mutant).
* EV32 (and EV33, already counted for its R-id) carry D06 as a support row with a verbatim-correct abstract quote, but the proposition is superseded by the erratum and the 2011 background-mutation statement (Headline 1). Defective rows are therefore EV07, EV14, EV16, EV17, EV32, EV33 (6).
* Resource ids R01 to R23 are used in evidence.tsv but `resources.tsv` has no id column; add one (the verifier recovered them by row order).

Spot-checked receipts (`output/receipts/`): FTR-20261110-39952983-83 (Kim) and FTR-20261110-26023770-83 (Tomita), also FTR-20261110-42909904-83 and FTR-20261110-26302329-83: `source_fingerprint` equals the SHA-256 I computed on the Europe PMC fullTextXML of PMC11828923, PMC4449117, PMC13684411 and PMC4547717 fetched 2026-11-10 (identical digests, all four). Section lists match what the producer cites: Kim methods, results and figures read (discussion not read, producer cites none); Tomita all main sections, supplementary captions only (true); Lucas-Clarke methods not read (the producer cites only Results and the supplement; the sex and age columns come from Supp Table 1B and the Supplementary Figure legends, which the receipt marks as supplementary read); O'Keefe 2015 methods, results and discussion read, figures captions only (true, I also did not open S1 to S4). Locators in the Kim and Tomita receipts verified verbatim. One receipt-level gap: the receipt for 16007179 (abstract only) records no erratum, although the PubMed record has an ErratumIn field.

## Corrections the producer must make

1. `decisive.tsv` D06: split into two propositions. Keep "homozygous or trans-heterozygous Wwox loss is viable to adulthood" (add 21075834 Results; 2015 Results, not Discussion; WWOX1 null, WWOX2 probable f04545 as INFERENZA). Change "2005 mutant ... radiation-sensitive, rescued ..." to "reported in 2005 (abstract), later attributed to background mutations (21075834, 17395332); erratum Oncogene 2006;25:7662 not opened; do not use as a Wwox-loss phenotype or as a rescue precedent".
2. `decisive.tsv` D04: wording "no significant genotype effect on startle climbing to day 28 (N = 3 to 6 vials), low power"; add glial lifespan 74 to 70 days and neuronal 57 to 42; add tim-GAL4 period lengthening.
3. `decisive.tsv` D02: "about 7 percent" (read from Fig 2A), qPCR on whole flies; add the 2011 source for "pBac insertion in exon 2".
4. `decisive.tsv` D03: n = 32 and 30 in Fig 2E; add day bout length reduced; add the opposite-sign remark with D04 in a joint row.
5. `decisive.tsv` D07: restrict "without it upregulation does nothing" to CRISPRa; mark hWWOX and dWwox as tested only with Abeta42.
6. `decisive.tsv` D11: class = same-origin (review and primary paper from one laboratory).
7. `decisive.tsv` D08 and `evidence.tsv` EV16, EV17: locators as above; add that ectopic WWOX enhances Egr damage.
8. `resources.tsv` R23: replace as written in B. R02, R03: add the notes. R16: remove "not significant at mRNA" unless sourced. R10: "2-fold (text)".
9. `feasibility.tsv` FE01 label to INFERENZA or reword; FE02 last clause; FE04, FE07, FE08 (radiation and "2005 rescue"); FE04 and FE06 (sign conflict); FE09 (Y33 to C28, S14 to S9); FE10 (shared sleep readout); FE11 labels.
10. `evidence.tsv`: R-id fixes in EV07, EV14, EV33; add an id column to `resources.tsv`.
11. `queries.tsv`: add the verifier-independent note that Q07 returns neither 21075834 nor 26302329; extend the absence statement as in E.

## What I could not reach

* BDSC pages (HTTP 403) and FlyBase stock or allele reports (client-rendered shell, no content); no stock holding was confirmed for any line.
* Supp Fig S1 (2011) for the western of Wwox1 and Wwoxf04545 adults; the Oncogene 2006 erratum text; O'Keefe 2015 S1 Fig and S4 Fig; Lucas-Clarke Supp Fig 1 (knockdown mRNA) and Supp Fig 6A to 6F (images); Tomita S2C mRNA panel as a number.
* Choo 2015 (26390919) and the 2005 paper beyond the abstract (paywalled; abstract only).
* Alliance of Genome Resources API (not retried).

## Method notes

Work area: `/tmp/claude-1000/-home-desktop-legend-development/9400b253-25a0-4b03-8822-96361325fc16/scratchpad/icv_work/` (texts, figures, aligner script (kept in the scratchpad, not in the repository), alignments `aln_A.txt`, `aln_B.txt`). Python on downloaded files run with `-I`. No gate, lint, test, receipt record, or edit outside `verify/`; no e-mail, registration or contact; no browser identity.

## Recheck (after producer corrections, commit 9602f07e; verifier ic-v, 2026-11-10)

Scope: only the substantive corrections, against the originals already opened, plus 21075834 and the two new receipts. No new search.

* **D06 (substantive, mostly fixed).** 21075834 states in its Introduction "background mutations, rather than the targeted Wwox mutations, were responsible for this phenotype" (EV36 verbatim, locator right); 17395332 is abstract-only, the abstract does not name Wwox, and the producer says so (EV40, receipt, depth abstract_only). Viability: EV37 is correct text but indirect, because "Drosophila homozygous for this mutation are viable and fertile as previously observed for the Wwox1 mutants" is a sentence about the Idh mutation that refers back to Wwox1; write "stated by comparison". STILL WRONG: the unscoped absence "no published rescue of any Wwox-loss phenotype exists" (decisive.tsv D06; feasibility.tsv FE04 what_is_missing and FE08; evidence.tsv EV33). It must read "none found in the sources opened (2011 text has no rescue statement; 2005 abstract superseded)". Same defect in the "none found" family.
* **Receipts.** FTR-20261110-21075834-83: fingerprint dc52cb20... reproduces exactly (NCBI efetch db=pmc PMC3016910, re-fetched twice); section list and locator match. FTR-20261110-17395332-83: abstract quote verbatim ("Unfortunately, we have found that this is not the case"); the fingerprint 230ea0b3... was NOT reproduced by either PubMed efetch form I tried (abstract text and XML), so the byte route behind it is unknown: UNVERIFIED, not wrong. INDEX.tsv lists 11 rows.
* **R23 and FE02: fixed.** Antibody (2015 Methods, EV39 verbatim), protein absent in adult Wwox1 and f04545 (EV38 verbatim, Supp Fig S1 unseen), only imaginal-disc protein too low (EV18). Status catalogue_entry_only is right.
* **FE04, FE06, FE10: fixed.** Light-phase disagreement and the reconcile-first step are stated; FE10 adds the shared-readout limit. One wording point: "disagree in sign" compares different metrics (minutes and bout length in Kim, episode length and active-to-inactive probability in Lucas-Clarke, total sleep not drawn); label that sentence INFERENZA inside the DATO row, or say "point in opposite directions on the light-phase metrics each paper reports".
* **D02, D03, D04, D07, D08, D11: fixed** (7 percent with range; n 32 and 30 and day bout length; 57 to 42 and 74 to 70 d, climbing low power, tim-GAL4 period; CRISPRa-only no-amyloid control; Results text and enhancement of Egr damage, EV16; same-origin). **FE01 INFERENZA, FE09 (S14 to S9, Y33 to C28, first 14 gapped), FE11 DATO and FE12 INFERENZA split: fixed.** D05, FE07, Q05, Q07, Q13 "none found" wording: fixed.
* **Still stale (editorial).** `resources.tsv` R01 note still says "mRNA about 8 percent, Fig 2A" (D02 and FE01 say about 7 percent). Column counts: decisive 8, resources 7, feasibility 6, evidence 9, queries 6, figure_notes 7, uniform.
* Recheck counts: 14 substantive items checked; 12 fixed; 2 not fully fixed (the unscoped "no published rescue ... exists" in 4 rows, one now counts as one wording defect; EV37 indirectness); 1 editorial leftover (R01); 1 receipt fingerprint unverified (17395332).
